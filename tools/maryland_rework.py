"""Exact append-only builder for the bundled Maryland correction/current/future inputs.

No network access or model calls. Run on a clean clone at the manifest's base.
"""
import argparse,csv,gzip,hashlib,io,json,os,subprocess,sys,time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

def git(repo,*args):
    result=subprocess.run(['git','-c','gc.auto=0','-C',str(repo),*args],capture_output=True,check=True)
    return result.stdout.decode('utf8').strip()
def sha(body):return hashlib.sha256(body).hexdigest()
def blob(body):return hashlib.sha1(b'blob '+str(len(body)).encode()+b'\0'+body).hexdigest()
def stamp(day):
    d=datetime.fromisoformat(day+'T12:00:00').replace(tzinfo=ZoneInfo('America/New_York'))
    return f'{int(d.timestamp())} {d.strftime("%z")}'
class Writer:
    def __init__(self,repo,head,branch='main'):
        self.parent=head;self.mark=0;self.branch=branch
        self.ct=int(git(repo,'log','-1','--format=%ct',head));self.tz=git(repo,'log','-1','--format=%ci',head).split()[-1]
        self.process=subprocess.Popen(['git','-c','gc.auto=0','-C',str(repo),'fast-import','--quiet','--done','--date-format=raw'],stdin=subprocess.PIPE)
    def write(self,s):self.process.stdin.write(s)
    def data(self,s):
        b=s.encode('utf8') if isinstance(s,str) else s
        self.write(f'data {len(b)}\n'.encode()+b+b'\n')
    def commit(self,author,when,message,files):
        self.mark+=1;self.ct+=1
        self.write(f'commit refs/heads/{self.branch}\nmark :{self.mark}\nauthor {author[0]} <{author[1]}> {when}\ncommitter Lexifina <united-states-maryland-law@lexifina.com> {self.ct} {self.tz}\n'.encode())
        self.data(message)
        self.write((f'from {self.parent}\n' if isinstance(self.parent,str) else f'from :{self.parent}\n').encode())
        for p,t in sorted(files.items()):
            if t is None:self.write(f'D {p}\n'.encode())
            else:self.write(f'M 100644 inline {p}\n'.encode());self.data(t)
        self.parent=self.mark
    def finish(self):
        self.write(b'done\n');self.process.stdin.close()
        if self.process.wait():raise RuntimeError('fast-import failed')
def load_package(root):
    data=root/'data/rework';manifest=json.loads((data/'manifest.json').read_bytes())
    for p,record in manifest['files'].items():
        content=(root/p).read_bytes()
        if sha(content)!=record['sha256']:raise ValueError('package hash mismatch: '+p)
        if p.endswith('.gz') and sha(gzip.decompress(content))!=record['uncompressed_sha256']:raise ValueError('input hash mismatch: '+p)
    def read(name):return json.loads(gzip.decompress((data/name).read_bytes()))
    return manifest,read('current-corpus.json.gz'),read('corrections.json.gz'),read('future-versions.json.gz'),read('documentation.json.gz')
def reproduction(manifest,root,lawtip):
    rows=['# Reproducing the Maryland correction and future build','',
          'This package reproduces the appended current corrections, closing documentation, and 105 source-dated future versions. It uses complete reviewed input snapshots and correction plans; it does not obtain or regenerate official PDFs. Source acquisition and the earlier input-preparation programs are outside this executable recipe. No model runs during this build.','',
          'The complete program used for this append is [maryland_rework.py](tools/maryland_rework.py). Its documentation assembly, correction writer and future writer are included. The older shared tools remain available as separately pinned checking/reading tools, rather than being described as this complete custom pipeline.','',
          '## Immutable inputs and program pins','',
          f'- Published starting head: `{manifest["base_head"]}`.',
          f'- Corrected law tip before the closing documentation: `{lawtip}`.',
          f'- Source-input preparation retained reviewed correction part SHA-256 `{manifest["reviewed_part_sha256"]}`.',
          f'- Package manifest Git blob: `{blob((root/"data/rework/manifest.json").read_bytes())}`.',
          '- Source PDFs are identified by official URL, size and SHA-256 in the bundled source manifest; current per-act source hashes remain in `data/versions.json`.','',
          '| File | Git blob | SHA-256 | Uncompressed SHA-256 |','| --- | --- | --- | --- |']
    for p,r in sorted(manifest['files'].items()):rows.append(f'| `{p}` | `{r["git_blob"]}` | `{r["sha256"]}` | `{r.get("uncompressed_sha256", "")}` |')
    rows+=['','## Previous published identifiers','',
           'These are the original baseline identifiers; they are retained as provenance, not claims that the older four-article documentation or retrieval-date policy describes the corrected corpus.','',
           '- Baseline corpus SHA-256: `48df9aa86112d00fd0d8bcd6a7a7b265726519a93dd0a8187614709e708216c1` (59,517,630 bytes).',
           '- Baseline builder `build.py`: `a4faa25af85facb64b956b372f6b528aafdd7ec1`; checker `check.py`: `3d00541d258745461ab52b1b0cb4e1716a27a95d`; reader `on.py`: `644a6c0857fbcc72562032b58d57aa113fee0641`.',
           '- Baseline toolchain: Python 3.12.10; git version 2.46.0.windows.1.','',
           '## Toolchain for this package','',
           f'Python {manifest["toolchain"]["python"]}; {manifest["toolchain"]["git"]}; source text extraction used PyMuPDF {manifest["toolchain"]["pymupdf"]}. The executable append uses Python standard-library modules and Git; source extraction is not required for replaying the bundled inputs. Time zone: America/New_York. Input/documentation date: 2026-11-03.','',
           '## Executable recipe','',
           'Copy this package from a checked-out candidate repository, create a fresh clone at the starting head above, and run the program from the package. The program populates a narrow scratch index, refuses a different base or existing future branch, verifies all package hashes, and preserves existing tags. It does not push.','',
           '```powershell',
           'git clone --filter=blob:none --no-checkout https://github.com/lexifina/united-states-maryland-law.git rebuild',
           'python -X utf8 tools/maryland_rework.py --repo rebuild',
           'python -X utf8 tools/check_repo.py rebuild --corpus rebuild-rework-input/corpus.json',
           '```','',
           'If published main has moved, provide a clean clone at the pinned starting head; the builder refuses to silently choose another head. To check exact reproduction, build a second fresh clone from the same base with this package and compare `git show-ref --heads --tags` in both outputs. Input files are gzip-compressed with fixed metadata and marked binary in `.gitattributes`.','',
           '## Validation and scope','',
           'The bundled statutory inputs were independently checked against official PDF wording: 37 acts, 39,769 current sections, 775 lossless decimal-section splits, and 39,556 sections in the final future snapshot. The corrected capture baselines retain Text-as-of and In-force-basis; source section dates are not generalized into whole-Article commencement dates. No OCR or model-written law words. GPT-6 wrote the packaging and executable code.','',
           'Two fresh package-only builds and old/new/live reader and checker gates are required for sign-off; the review record reports their observed results. Deterministic reproduction is separate from official-source word verification.']
    return '\n'.join(rows)+'\n'
def future_message(v,act):
    files={act['slug']+'/'+k+'.md':u['text'] if u else None for k,u in v['changes'].items()}
    message=f'{act["short"]}: source-dated alternative, {v["from"]}\n\nFuture source text; outside current main. Expiration of an alternative is not labelled as legislative repeal.\n\nKind: uncredited\nIn-force: {v["from"]}\nIn-force-basis: {v["in_force_basis"]}\nSource: {v["source_url"]}\nText-source: {v["source_url"]}\nAct-path: {act["slug"]}\n'+'\n'.join('Files: '+p for p in files)+'\n'
    return message,files
def main():
    os.environ.update(GIT_AUTHOR_NAME='Lexifina',GIT_COMMITTER_NAME='Lexifina',GIT_AUTHOR_EMAIL='united-states-maryland-law@lexifina.com',GIT_COMMITTER_EMAIL='united-states-maryland-law@lexifina.com')
    parser=argparse.ArgumentParser();parser.add_argument('--repo',type=Path,required=True);parser.add_argument('--package',type=Path);a=parser.parse_args()
    root=(a.package or Path(__file__).resolve().parents[1]).resolve();repo=a.repo.resolve()
    m,c,plans,versions,docs=load_package(root)
    if git(repo,'rev-parse','main')!=m['base_head']:raise ValueError('repository is not at the pinned published base')
    if git(repo,'for-each-ref','--format=%(refname)','refs/heads/future'):raise ValueError('future already exists')
    before_tags=git(repo,'show-ref','--tags')
    info=repo/'.git/info';info.mkdir(exist_ok=True);(info/'sparse-checkout').write_text('/README.md\n',encoding='utf8')
    git(repo,'-c','core.sparseCheckout=true','read-tree','-mu','HEAD')
    if git(repo,'-c','core.sparseCheckout=true','status','--porcelain','--untracked-files=no'):raise ValueError('repository has tracked changes')
    inputdir=repo.parent/(repo.name+'-rework-input');inputdir.mkdir(exist_ok=True)
    (inputdir/'corpus.json').write_text(json.dumps(c,ensure_ascii=False,indent=1)+'\n',encoding='utf8')
    canonical={a['slug']+'/'+k+'.md':u['text'] for a in c['acts'] for k,u in a['versions'][0]['units'].items()}
    author=('Lexifina','united-states-maryland-law@lexifina.com')
    w=Writer(repo,m['base_head'])
    for entry in plans:w.commit(author,entry['when'],entry['message'],{p:canonical.get(p) for p in entry['files']})
    w.finish();lawtip=git(repo,'rev-parse','main')
    if lawtip!=m['expected_correction_tip']:raise ValueError('statutory correction commits differ from the independently reviewed commits')
    # The exact documentation assembler and all of its immutable input files are part of this package.
    for p in m['files']:docs[p]=(root/p).read_bytes()
    docs['data/rework/manifest.json']=(root/'data/rework/manifest.json').read_bytes()
    docs['REPRODUCE.md']=reproduction(m,root,lawtip)
    docs['.gitattributes']=docs.get('.gitattributes','')+'\ndata/rework/*.json.gz binary\ntools/maryland_rework.py text eol=lf\ndata/rework/manifest.json text eol=lf\n'
    table=list(csv.DictReader(io.StringIO(docs['data/provisions.tsv']),delimiter='\t'))
    provenance={e['act']:e['commit'] for e in plans}
    for row in table:row['commit']=provenance[row['act']];row['kind']='correction'
    buf=io.StringIO();writer=csv.DictWriter(buf,fieldnames=list(table[0]),delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(table);docs['data/provisions.tsv']=buf.getvalue()
    message=f'Documentation, tables, tools and REPRODUCE.md\n\nAppended {len(plans)} verified corrections to {m["base_head"][:12]}; complete executable package and hash-bound inputs supplied.\n\nKind: documentation\n'+'\n'.join('Redates: '+h+' no-date' for h in sorted({e['supersedes'] for e in plans}))+'\n'
    w=Writer(repo,lawtip);w.commit(author,stamp('2026-11-03'),message,docs);w.finish()
    head=git(repo,'rev-parse','main');w=Writer(repo,head,'future');acts={a['slug']:a for a in c['acts']}
    publisher=(c['country']['publisher']['name'],c['country']['publisher']['email'])
    for version in versions:
        msg,files=future_message(version,acts[version['act']]);w.commit(publisher,stamp(version['from']),msg,files)
    w.finish()
    if before_tags!=git(repo,'show-ref','--tags'):raise ValueError('published tags changed')
    git(repo,'merge-base','--is-ancestor',m['base_head'],head)
    git(repo,'-c','core.sparseCheckout=true','checkout','-q','-f','main')
    print(json.dumps({'base':m['base_head'],'correction_tip':lawtip,'main':head,'future':git(repo,'rev-parse','future'),'corrections':len(plans),'future_versions':len(versions),'input':str(inputdir/'corpus.json')}))
if __name__=='__main__':main()
