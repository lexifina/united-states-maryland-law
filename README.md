# United States (Maryland): law history in git

A first build of Maryland law as git: one file per provision, with the text published by the Maryland General Assembly ([mgaleg.maryland.gov](https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes)). It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `united-states/maryland/`. Language: English.

**What is in it now**

| Folder | Law | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of Maryland (1867, as amended) | 1 | Oldest version available (retrieved 2026-10-30) |
| `criminal-law/` | Maryland Code, Criminal Law Article | 1 | Oldest version available (retrieved 2026-10-30) |
| `real-property/` | Maryland Code, Real Property Article | 1 | Oldest version available (retrieved 2026-10-30) |
| `corporations-and-associations/` | Maryland Code, Corporations and Associations Article | 1 | Oldest version available (retrieved 2026-10-30) |

## What it does not show

- **Past versions.** The General Assembly publishes the current Code; future-dated and referendum-pending versions marked in the source are left out. Each text therefore has one commit, "oldest version available", credited to the publisher and dated by the retrieval day.
- **Other law.** The other 32 Code articles are not yet included.
- **Notes.** Source notes, histories and annotations are not law text and are not in the files.

## How it is checked

Every version names its source and the sha256 of the data it was read from. Each version is read back from git and must match `corpus.json` (`tools/check_repo.py`); the results are in `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Licence |
| --- | --- | --- | --- |
| [the Maryland General Assembly](https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes) | Official publisher | no | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020) |

## Licence

See `LICENSE`. This repository is not legal advice and not an official publication.
