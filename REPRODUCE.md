# Reproducing the Maryland correction and future build

This package reproduces the appended current corrections, closing documentation, and 105 source-dated future versions. It uses complete reviewed input snapshots and correction plans; it does not obtain or regenerate official PDFs. Source acquisition and the earlier input-preparation programs are outside this executable recipe. No model runs during this build.

The complete program used for this append is [maryland_rework.py](tools/maryland_rework.py). Its documentation assembly, correction writer and future writer are included. The older shared tools remain available as separately pinned checking/reading tools, rather than being described as this complete custom pipeline.

## Immutable inputs and program pins

- Published starting head: `4d120b87d18f816d07ed6dd38340b1b13e951406`.
- Corrected law tip before the closing documentation: `578d7ec965d58cf39582772319678c867ed1260c`.
- Source-input preparation retained reviewed correction part SHA-256 `f95c68034199cb2d61185076f6c2bf4dece552780197c4ae21e62ed31ed19830`.
- Package manifest Git blob: `f71ded45ebc202c7f824449804cc629f8d38af19`.
- Source PDFs are identified by official URL, size and SHA-256 in the bundled source manifest; current per-act source hashes remain in `data/versions.json`.

| File | Git blob | SHA-256 | Uncompressed SHA-256 |
| --- | --- | --- | --- |
| `data/rework/corrections.json.gz` | `4b4205a169bbda27cf2adf513e473ca0a191a4c8` | `ffcc8d5c4e4c4db1e7a0b72fdf1b949d62c757acdda4ae5c01c71733704a4b1f` | `393eac0466274a8c394df77ab08d5a9b36c373ded8d87393bb312e04b8ad0c1d` |
| `data/rework/current-corpus.json.gz` | `1e57ec44ba831c0dadbfdfec444f5a7bf255c656` | `27d3a6e9b706475a0e27e977ed38d822d7872daf1ad824a9e597ad47b2561428` | `7cc170ade92b8ea9169861c96ca318c840c48ef9db12fb29a5c2855fbbe638ee` |
| `data/rework/documentation.json.gz` | `7787aca0940f81784e24decf5481b9d57381f6a3` | `8126e98ac6ba87ae3047534680a70242af9c738b1fcef4e30926c8b742c4a5d1` | `5d308757567a93e7be3328af5b7eaf5ae882aea457406a33d8efd75d71fe6a4d` |
| `data/rework/future-versions.json.gz` | `bb7b8e5cb896e167c45cec12fa9bfac407a12bf5` | `fdd741d0c27ab70b60df1713ae0251247271f74a829351c8e1871184c0e9cabf` | `bddc4fff225639dbb3dc258b3886ce0e644b5abb95c84a5bc204cb8cd8851624` |
| `data/rework/source-manifest.json.gz` | `bff1aea19b9941244439ee74228d064143c0330e` | `9d42a05435504141142a78869acff9e63ff88f1078afd935a0a09968826e001e` | `28a38f3c5bde4a9ab926a503a57d73651c792b83c75640dec6c4c9053a8b2445` |
| `tools/maryland_rework.py` | `fc970aae8feb60b00a96c8895a31975352f589b1` | `b7ed661e62e50f76bd8da7f0492c33a9487f109bbda462d762e7a56307dc384d` | `` |

## Previous published identifiers

These are the original baseline identifiers; they are retained as provenance, not claims that the older four-article documentation or retrieval-date policy describes the corrected corpus.

- Baseline corpus SHA-256: `48df9aa86112d00fd0d8bcd6a7a7b265726519a93dd0a8187614709e708216c1` (59,517,630 bytes).
- Baseline builder `build.py`: `a4faa25af85facb64b956b372f6b528aafdd7ec1`; checker `check.py`: `3d00541d258745461ab52b1b0cb4e1716a27a95d`; reader `on.py`: `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Baseline toolchain: Python 3.12.10; git version 2.46.0.windows.1.

## Toolchain for this package

Python 3.12.10; git version 2.46.0.windows.1; source text extraction used PyMuPDF 2.0. The executable append uses Python standard-library modules and Git; source extraction is not required for replaying the bundled inputs. Time zone: America/New_York. Input/documentation date: 2026-11-03.

## Executable recipe

Copy this package from a checked-out candidate repository, create a fresh clone at the starting head above, and run the program from the package. The program populates a narrow scratch index, refuses a different base or existing future branch, verifies all package hashes, and preserves existing tags. It does not push.

```powershell
git clone --filter=blob:none --no-checkout https://github.com/lexifina/united-states-maryland-law.git rebuild
python -X utf8 tools/maryland_rework.py --repo rebuild
python -X utf8 tools/check_repo.py rebuild --corpus rebuild-rework-input/corpus.json
```

If published main has moved, provide a clean clone at the pinned starting head; the builder refuses to silently choose another head. To check exact reproduction, build a second fresh clone from the same base with this package and compare `git show-ref --heads --tags` in both outputs. Input files are gzip-compressed with fixed metadata and marked binary in `.gitattributes`.

## Validation and scope

The bundled statutory inputs were independently checked against official PDF wording: 37 acts, 39,769 current sections, 775 lossless decimal-section splits, and 39,556 sections in the final future snapshot. The corrected capture baselines retain Text-as-of and In-force-basis; source section dates are not generalized into whole-Article commencement dates. No OCR or model-written law words. GPT-6 wrote the packaging and executable code.

Two fresh package-only builds and old/new/live reader and checker gates are required for sign-off; the review record reports their observed results. Deterministic reproduction is separate from official-source word verification.
