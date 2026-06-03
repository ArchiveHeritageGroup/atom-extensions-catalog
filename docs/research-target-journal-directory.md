# Where to Publish — Target-Journal Directory

_Part of the Research Portal (`ahgResearchPlugin`). PSIS/AtoM parity port of the Heratio
"target-journal directory" (#114 / Heratio #1107)._

## What it does

The target-journal directory is a curated catalogue of journals you might publish **to**.
Each entry records the journal's **subject scope** (what it accepts) and its **submission
rules** — reference style, structure, word and abstract limits, open-access status and APC,
peer-review type, indexing/accreditation, languages and turnaround.

It feeds the **auto-assemble flow**: pick or suggest a target journal → pre-format the
manuscript to that journal's rules → validate → package for submission.

The directory **core is jurisdiction-neutral**. The South-African DHET accredited list ships
as an **accreditation module** (`accreditation_market = 'ZA'`). Other markets seed their own
sets from DOAJ, Scopus, Web of Science or ERIH-PLUS.

## Where to find it

Research Portal sidebar → **Where to Publish**.

Routes (under the authenticated `/research` group):

| Screen | URL |
|--------|-----|
| Directory (list + search + filter) | `/research/target-journals` |
| View a journal | `/research/target-journals/:id` |
| Add a journal | `/research/target-journals/new` |
| Edit a journal | `/research/target-journals/:id/edit` |
| Delete a journal (POST) | `/research/target-journals/:id/delete` |
| Seed DHET starter (POST) | `/research/target-journals/seed-dhet` |
| Best-fit suggestions (JSON) | `/research/target-journals/suggest?text=...` |

## Using the directory

### Browse and search
The index lists every journal with its scope, indexing and reference style. Search matches
title, scope, publisher and accreditation. Filter by **market** (e.g. `ZA`) to focus on a
single accreditation module.

### Add / edit a journal
The builder form captures the full profile: identity (title, publisher, ISSN/eISSN, URLs),
scope, accreditation/indexing and market tag, and the submission rules block (reference
style, word/abstract limits, structure notes, peer review, open access, APC, turnaround,
languages). Status is `active` or `discontinued`.

### Seed the DHET starter set
**Seed DHET starter** loads a representative set of DHET-accredited South African journals
(LIS, archives, heritage and a few multidisciplinary titles). The operation is **idempotent**
— it upserts by title, so re-running refreshes rather than duplicates. ISSNs and exact numeric
limits are left for operators to complete/verify per journal via the admin form.

You can also run the seed from the CLI:

```bash
php bin/atom research:seed-target-journals
```

### Best-fit suggestions (auto-assemble)
The suggestion endpoint scores directory journals by how many of a manuscript's subject terms
(from its abstract/scope text) appear in each journal's scope, and returns the top matches with
a `match_score`. The manuscript builder uses this to recommend targets before pre-formatting.

```
GET /research/target-journals/suggest?text=<manuscript abstract>&limit=5
→ { "count": N, "suggestions": [ { ...journal..., "match_score": K }, ... ] }
```

## Data model

Single table `research_target_journal` (InnoDB, utf8mb4). Key columns:

| Column | Notes |
|--------|-------|
| `title`, `subtitle`, `publisher`, `issn`, `eissn` | Identity (ISSN is unique) |
| `homepage_url`, `submission_url`, `languages` | Access |
| `subject_scope` | Free-text — what the journal mainly accepts |
| `article_types` | e.g. research, review, case study |
| `accreditation` | DHET, IBSS, Scopus, WoS, DOAJ, Sabinet, ERIH-PLUS … |
| `accreditation_market` | Per-market module tag (e.g. `ZA`) |
| `reference_style` | APA, Harvard, Vancouver, Chicago, MLA, IEEE |
| `structure_notes`, `max_words`, `abstract_max_words` | Submission rules |
| `peer_review`, `open_access`, `apc_amount`, `turnaround` | Submission rules |
| `status` | `active` or `discontinued` |

No `ENUM` columns are used — controlled vocabularies are `VARCHAR` with a `COMMENT`.

## Notes

- Authentication is required for all screens.
- Cross-subsystem references (e.g. the manuscript builder) degrade gracefully when the other
  tables are absent.
