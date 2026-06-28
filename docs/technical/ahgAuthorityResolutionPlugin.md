# ahgAuthorityResolutionPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Evidence-based authority resolution for persons, places, and organisations. Replaces name-only matching with an archivist-driven workflow that surfaces neighbourhood-context evidence, ranked candidates, and provenance-tracked decisions. Provenance writes to Fuseki as RDF-Star.

## Overview

- **Name:** AHG Authority Resolution Engine
- **Machine name:** `ahgAuthorityResolutionPlugin`
- **Version:** 0.1.0
- **Category:** authority
- **Dependencies:** `ahgCorePlugin`, `ahgActorManagePlugin`, `ahgAIPlugin`
- **License:** GPL-3.0

## Database tables

- `ahg_authority_lookup_cache`
- `ahg_mention`
- `ahg_mention_candidate`
- `ahg_mention_context`
- `ahg_mention_decision`
- `ahg_mention_park`
- `ahg_ner_feedback`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `ar_auth_res_index` | `/admin/authorityResolution` | index |
| `ar_auth_res_review` | `/admin/authorityResolution/:id/review` | review |
| `ar_auth_res_context` | `/admin/authorityResolution/:id/context` | context |
| `ar_auth_res_link` | `/admin/authorityResolution/:id/link` | link |
| `ar_auth_res_link_different` | `/admin/authorityResolution/:id/link-different` | linkDifferent |
| `ar_auth_res_create_new` | `/admin/authorityResolution/:id/create-new` | createNew |
| `ar_auth_res_create_new_submit` | `/admin/authorityResolution/:id/create-new-submit` | createNewSubmit |
| `ar_auth_res_park` | `/admin/authorityResolution/:id/park` | park |
| `ar_auth_res_reject` | `/admin/authorityResolution/:id/reject` | reject |
| `ar_auth_res_park_list` | `/admin/authorityResolution/park` | parkList |
| `ar_auth_res_unpark` | `/admin/authorityResolution/park/:id/unpark` | unpark |
| `ar_auth_res_park_dashboard_json` | `/admin/authorityResolution/park/dashboard.json` | parkDashboardJson |
| `ar_auth_res_archivists_json` | `/admin/authorityResolution/archivists.json` | archivistsJson |
| `ar_auth_res_batch_assign` | `/admin/authorityResolution/assign-batch` | batchAssign |
| `ar_auth_res_assign` | `/admin/authorityResolution/:id/assign` | assign |
| `ar_auth_res_lookup` | `/admin/authorityResolution/lookup` | lookup |
| `ar_auth_res_lookup_settings` | `/admin/authorityResolution/settings/lookup` | lookupSettings |

## Module actions

**`authorityResolution`** — `index`, `review`, `context`, `link`, `linkDifferent`, `createNew`, `createNewSubmit`, `lookupSettings`, `lookupSettingsSave`, `park`, `reject`, `parkList`, `unpark`, `parkDashboardJson`, `lookup`, `assign`, `batchAssign`, `archivistsJson`

## CLI tasks

- `php symfony auth-res:cache-clear` — Evict rows from ahg_authority_lookup_cache by source or wholesale.
- `php symfony auth-res:cache-stats` — Report ahg_authority_lookup_cache contents grouped by source (entity-type breakdown + oldest/newest retrieval).
- `php symfony auth-res:export-ner-feedback` — Export rejected-mention feedback as a training corpus (JSONL or CoNLL).
- `php symfony auth-res:generate-candidates` — Generate ranked authority candidates for an ahg_mention.
- `php symfony auth-res:promote-sample` — Promote PERSON/ORG/GPE entities for an information object into the authority-resolution mention workflow.
- `php symfony auth-res:reprocess` — Re-run candidate generation + evidence scoring for a mention (or every pending mention).
- `php symfony auth-res:reprocess-parked` — Bulk-unpark every ahg_mention_park row parked since DATE and re-run candidate generation + scoring.
- `php symfony auth-res:scan-parked` — Flag parked mentions whose candidate set has changed since parking.
- `php symfony auth-res:score-evidence` — Score evidence signals + composite for each candidate of a mention. Re-ranks by composite.
- `php symfony auth-res:status` — Summarise the authority-resolution working set (mentions, candidates, decisions, parked, feedback, cache, Fuseki).
- `php symfony auth-res:write-provenance` — Write RDF-Star provenance for an authority-resolution decision to Fuseki.

## Service layer

### `AssignmentService`  
`lib/Services/AssignmentService.php`

Public methods: `assign()`, `assignBatch()`, `archivists()`

### `NerFeedbackService`  
`lib/Services/NerFeedbackService.php`

Public methods: `captureFromRejection()`, `exportUnexported()`

### `ContextDerivationService`  
`lib/Services/ContextDerivationService.php`

Public methods: `derive()`

### `ParkQueueService`  
`lib/Services/ParkQueueService.php`

Public methods: `listFor()`, `unparkAndRereview()`, `scanForNewCandidates()`, `dashboardByUser()`

### `CandidateGeneratorService`  
`lib/Services/CandidateGeneratorService.php`

Public methods: `generate()`, `nameSimilarity()`

### `FusekiUpdateService`  
`lib/Services/FusekiUpdateService.php`

Public methods: `executeUpdate()`, `executeQuery()`, `queryCount()`

### `PromoteToMentionService`  
`lib/Services/PromoteToMentionService.php`

Public methods: `promote()`, `promoteAllForObject()`, `fetchSourceText()`

### `DocumentPriorService`  
`lib/Services/Evidence/DocumentPriorService.php`

Public methods: `priorForObject()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
