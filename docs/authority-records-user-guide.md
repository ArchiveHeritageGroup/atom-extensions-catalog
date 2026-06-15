# Authority Records Enhancement

## A Guide for Administrators and Editors

---

## What is it?

The AHG Authority plugin (`ahgAuthorityPlugin`) is a suite of enhancements for managing the quality
and richness of your authority records (actors — people, organisations, families). It adds external
identifier linking, a completeness dashboard, a relationship graph, merge/split and deduplication
workflows, structured occupations and ISDF functions, a Named Entity Recognition (NER) pipeline, and
enriched EAC-CPF export — all surfacing through an **Authority Records** admin section.

## Key features

- **External identifier linking** — link actors to **Wikidata, VIAF, ULAN, and LCNAF**, with search,
  save, and verification of each identifier. Stored in `ahg_actor_identifier`.
- **Completeness dashboard** — scores how complete each authority record is and surfaces gaps, with
  recalculation per record and batch assignment, plus a completeness badge/panel on records.
- **Relationship graph** — a visual graph of how an actor relates to other actors, driven by graph
  data for each authority record.
- **Merge & split workflow** — preview and execute merges of duplicate authority records, and split
  conflated records apart, with a merge audit trail (`ahg_actor_merge`).
- **Bulk deduplication** — scan the catalogue for likely duplicate actors, compare candidate pairs
  side by side, and dismiss or merge them.
- **NER-to-authority pipeline** — turn named entities detected by the AI/NER tools into authority
  **stubs** (`ahg_ner_authority_stub`), then review, promote, or reject them.
- **Structured occupations** — record occupations against an actor (`ahg_actor_occupation`).
- **ISDF functions** — link actors to ISDF functions and browse functions (`ahg_actor_function_link`).
- **EAC-CPF export enrichment** — export richer EAC-CPF for an actor, including the linked
  identifiers and structured data.
- **Contact panel** — surface extended contact information for an actor.

## How to use it

Open the **Authority Records** admin section (icon: ID card), or go directly to:

- **Dashboard:** `/admin/authority/dashboard` — overview of authority quality.
- **Work queue:** `/admin/authority/workqueue` — records needing attention.
- **Identifiers:** `/admin/authority/:actorId/identifiers` — link/verify Wikidata, VIAF, ULAN, LCNAF.
- **Completeness:** recalculate via `/api/authority/completeness/:actorId/recalc`; the badge/panel
  appears on the record.
- **Relationship graph:** `/api/authority/graph/:actorId` powers the graph panel.
- **Merge / split:** `/admin/authority/merge/:id` and `/admin/authority/split/:id`.
- **Deduplication:** `/admin/authority/dedup`, scan at `/admin/authority/dedup/scan`, compare at
  `/admin/authority/dedup/compare/:id`.
- **NER pipeline:** `/admin/authority/ner-pipeline` to review, promote, or reject entity stubs.
- **Occupations:** `/admin/authority/:actorId/occupations`.
- **Functions:** `/admin/authority/:actorId/functions` and browse at
  `/admin/authority/functions/browse`.
- **Contact:** `/admin/authority/:actorId/contact`.
- **EAC-CPF export:** `/api/authority/eac-cpf/:actorId`.

## Administration / settings

- **Configuration:** `/admin/authority/config` (administrator only) — settings stored in
  `ahg_authority_config`.
- **CLI tasks:** scheduled/maintenance tasks include a completeness scan, deduplication scan, NER
  pipeline run, function sync, and a merge report.
- **Optional integrations:** works better alongside `ahgDedupePlugin`, `ahgAIPlugin`,
  `ahgRicExplorerPlugin`, `ahgWorkflowPlugin`, `ahgContactPlugin`, `ahgExportPlugin`, and
  `ahgFunctionManagePlugin` when those are enabled. Requires `ahgActorManagePlugin`.

## Tips & FAQ

- **Where do duplicates come from?** Bulk imports and OCR/NER ingestion often create near-duplicate
  actors; run the dedup scan periodically and resolve pairs from the compare screen.
- **Merge vs. split?** Merge folds duplicates into one record (keeping a merge audit trail); split
  separates a record that wrongly conflates two distinct entities.
- **Do I have to accept every NER stub?** No — the pipeline is review-first. Promote good ones to
  full authority records and reject the rest.
- **Why link to Wikidata/VIAF?** External identifiers make your authorities interoperable and
  enrich EAC-CPF export for sharing with other institutions.
