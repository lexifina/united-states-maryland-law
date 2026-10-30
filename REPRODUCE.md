# How this repository was made (United States (Maryland))

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Maryland General Assembly, Laws: Statutes (per-article PDF, text layer) | <https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes> | 2026-10-30 | Public statute text |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of Maryland | 1 | 2026-10-30 to 2026-10-30 |
| `criminal-law` | Maryland Code, Criminal Law Article | 1 | 2026-10-30 to 2026-10-30 |
| `real-property` | Maryland Code, Real Property Article | 1 | 2026-10-30 to 2026-10-30 |
| `corporations-and-associations` | Maryland Code, Corporations and Associations Article | 1 | 2026-10-30 to 2026-10-30 |

The build made 4 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 4 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (America/New_York) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: No dated history is published: each text is the oldest version available, dated from the retrieval day. https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `0dbe6eff763c5742032a244cc1f092e634a863d3d88d7d151e013a6d18a1e0b6` (4580265 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- English only. First build: the Constitution and the Code articles: Criminal Law, Real Property, Corporations and Associations.
- Every text has one version, "oldest version available", dated from the retrieval day and credited to the publisher; the site publishes only current text.
- Where the PDF marks a section with a status (IN EFFECT, TAKES EFFECT or EFFECTIVE on a date, EFFECTIVE UNTIL, SUBJECT TO REFERENDUM), the version in force on 2026-10-30 is taken and future-dated or referendum-pending versions are left out; the markers themselves are not kept.
- Text comes from the text layer of the official article PDFs; page numbers and running titles are dropped, lettered and numbered subsections each start a line, and the en dash in section numbers becomes a hyphen.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none (scripts only; no model wrote or altered legal text)
