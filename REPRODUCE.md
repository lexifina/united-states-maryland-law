# How this repository was made (United States (Maryland))

This file is written by the build on 2026-11-03, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Maryland General Assembly, Laws: Statutes (per-article PDF, text layer) | <https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes> | 2026-10-30 | Public statute text |
| Maryland General Assembly, Laws: Statutes (every Code article, PDF text layer) | <https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes> | 2026-11-03 | Public statute text |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of Maryland | 1 | 2026-10-30 to 2026-10-30 |
| `criminal-law` | Maryland Code, Criminal Law Article | 1 | 2026-10-30 to 2026-10-30 |
| `real-property` | Maryland Code, Real Property Article | 1 | 2026-10-30 to 2026-10-30 |
| `corporations-and-associations` | Maryland Code, Corporations and Associations Article | 1 | 2026-10-30 to 2026-10-30 |
| `agriculture` | Maryland Code, Agriculture Article | 1 | 2026-11-03 to 2026-11-03 |
| `alcoholic-beverages-and-cannabis` | Maryland Code, Alcoholic Beverages and Cannabis Article | 1 | 2026-11-03 to 2026-11-03 |
| `business-occupations-and-professions` | Maryland Code, Business Occupations and Professions Article | 1 | 2026-11-03 to 2026-11-03 |
| `business-regulation` | Maryland Code, Business Regulation Article | 1 | 2026-11-03 to 2026-11-03 |
| `commercial-law` | Maryland Code, Commercial Law Article | 1 | 2026-11-03 to 2026-11-03 |
| `correctional-services` | Maryland Code, Correctional Services Article | 1 | 2026-11-03 to 2026-11-03 |
| `courts-and-judicial-proceedings` | Maryland Code, Courts and Judicial Proceedings Article | 1 | 2026-11-03 to 2026-11-03 |
| `criminal-procedure` | Maryland Code, Criminal Procedure Article | 1 | 2026-11-03 to 2026-11-03 |
| `economic-development` | Maryland Code, Economic Development Article | 1 | 2026-11-03 to 2026-11-03 |
| `education` | Maryland Code, Education Article | 1 | 2026-11-03 to 2026-11-03 |
| `election-law` | Maryland Code, Election Law Article | 1 | 2026-11-03 to 2026-11-03 |
| `environment` | Maryland Code, Environment Article | 1 | 2026-11-03 to 2026-11-03 |
| `estates-and-trusts` | Maryland Code, Estates and Trusts Article | 1 | 2026-11-03 to 2026-11-03 |
| `family-law` | Maryland Code, Family Law Article | 1 | 2026-11-03 to 2026-11-03 |
| `financial-institutions` | Maryland Code, Financial Institutions Article | 1 | 2026-11-03 to 2026-11-03 |
| `general-provisions` | Maryland Code, General Provisions Article | 1 | 2026-11-03 to 2026-11-03 |
| `health-general` | Maryland Code, Health - General Article | 1 | 2026-11-03 to 2026-11-03 |
| `health-occupations` | Maryland Code, Health Occupations Article | 1 | 2026-11-03 to 2026-11-03 |
| `housing-and-community-development` | Maryland Code, Housing and Community Development Article | 1 | 2026-11-03 to 2026-11-03 |
| `human-services` | Maryland Code, Human Services Article | 1 | 2026-11-03 to 2026-11-03 |
| `insurance` | Maryland Code, Insurance Article | 1 | 2026-11-03 to 2026-11-03 |
| `labor-and-employment` | Maryland Code, Labor and Employment Article | 1 | 2026-11-03 to 2026-11-03 |
| `land-use` | Maryland Code, Land Use Article | 1 | 2026-11-03 to 2026-11-03 |
| `local-government` | Maryland Code, Local Government Article | 1 | 2026-11-03 to 2026-11-03 |
| `natural-resources` | Maryland Code, Natural Resources Article | 1 | 2026-11-03 to 2026-11-03 |
| `public-safety` | Maryland Code, Public Safety Article | 1 | 2026-11-03 to 2026-11-03 |
| `public-utilities` | Maryland Code, Public Utilities Article | 1 | 2026-11-03 to 2026-11-03 |
| `state-finance-and-procurement` | Maryland Code, State Finance and Procurement Article | 1 | 2026-11-03 to 2026-11-03 |
| `state-government` | Maryland Code, State Government Article | 1 | 2026-11-03 to 2026-11-03 |
| `state-personnel-and-pensions` | Maryland Code, State Personnel and Pensions Article | 1 | 2026-11-03 to 2026-11-03 |
| `tax-general` | Maryland Code, Tax - General Article | 1 | 2026-11-03 to 2026-11-03 |
| `tax-property` | Maryland Code, Tax - Property Article | 1 | 2026-11-03 to 2026-11-03 |
| `transportation` | Maryland Code, Transportation Article | 1 | 2026-11-03 to 2026-11-03 |

The build made 37 commits:

| Commits | Kind |
| ---: | --- |
| 37 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-03.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 37 laws in the record.
- 37 tags.

## Dates

Each commit is dated at noon (America/New_York) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: No dated history is published: each text is the oldest version available, dated from the retrieval day. https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `48df9aa86112d00fd0d8bcd6a7a7b265726519a93dd0a8187614709e708216c1` (59517630 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- English only. First build: the Constitution and the Code articles: Criminal Law, Real Property, Corporations and Associations.
- Every text has one version, "oldest version available", dated from the retrieval day and credited to the publisher; the site publishes only current text.
- Where the PDF marks a section with a status (IN EFFECT, TAKES EFFECT or EFFECTIVE on a date, EFFECTIVE UNTIL, SUBJECT TO REFERENDUM), the version in force on 2026-10-30 is taken and future-dated or referendum-pending versions are left out; the markers themselves are not kept.
- Text comes from the text layer of the official article PDFs; page numbers and running titles are dropped, lettered and numbered subsections each start a line, and the en dash in section numbers becomes a hyphen.
- Wave 3 (2026-11-03): every other Code article is added, one act per article, parsed as in the first build; status markers are resolved for 2026-11-03, the retrieval day.
- Each new article is dated by the retrieval day (2026-11-03) and credited to the publisher as the oldest version available, so its current wording is never dated before its latest amendment took effect.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none (scripts only; no model wrote or altered legal text)
