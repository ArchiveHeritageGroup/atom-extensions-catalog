# ahgAuthorityPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Comprehensive authority record enhancements: external linking (Wikidata, VIAF, ULAN, LCNAF), completeness dashboard, NER-to-authority pipeline, relationship graph, merge/split workflow, bulk deduplication, structured occupations, ISDF functions, EAC-CPF export enrichment, and contact panel surfacing.

## Overview

- **Name:** AHG Authority Records Enhancement
- **Machine name:** `ahgAuthorityPlugin`
- **Version:** 1.0.0
- **Category:** authority
- **Dependencies:** `ahgCorePlugin`, `ahgActorManagePlugin`
- **License:** GPL-3.0

## Database tables

- `ahg_actor_completeness`
- `ahg_actor_function_link`
- `ahg_actor_identifier`
- `ahg_actor_merge`
- `ahg_actor_occupation`
- `ahg_authority_config`
- `ahg_ner_authority_stub`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `ahg_authority_dashboard` | `/admin/authority/dashboard` | dashboard |
| `ahg_authority_workqueue` | `/admin/authority/workqueue` | workqueue |
| `ahg_authority_identifiers` | `/admin/authority/:actorId/identifiers` | identifiers |
| `ahg_authority_identifier_save` | `/api/authority/identifier/save` | apiIdentifierSave |
| `ahg_authority_identifier_delete` | `/api/authority/identifier/:id/delete` | apiIdentifierDelete |
| `ahg_authority_identifier_verify` | `/api/authority/identifier/:id/verify` | apiIdentifierVerify |
| `ahg_authority_wikidata_search` | `/api/authority/wikidata/search` | apiWikidataSearch |
| `ahg_authority_viaf_search` | `/api/authority/viaf/search` | apiViafSearch |
| `ahg_authority_ulan_search` | `/api/authority/ulan/search` | apiUlanSearch |
| `ahg_authority_lcnaf_search` | `/api/authority/lcnaf/search` | apiLcnafSearch |
| `ahg_authority_completeness_recalc` | `/api/authority/completeness/:actorId/recalc` | apiCompletenessRecalc |
| `ahg_authority_completeness_batch` | `/api/authority/completeness/batch-assign` | apiCompletenessBatchAssign |
| `ahg_authority_graph_data` | `/api/authority/graph/:actorId` | apiGraphData |
| `ahg_authority_merge` | `/admin/authority/merge/:id` | merge |
| `ahg_authority_split` | `/admin/authority/split/:id` | split |
| `ahg_authority_merge_preview` | `/api/authority/merge/preview` | apiMergePreview |
| `ahg_authority_merge_execute` | `/api/authority/merge/execute` | apiMergeExecute |
| `ahg_authority_split_execute` | `/api/authority/split/execute` | apiSplitExecute |
| `ahg_authority_occupations` | `/admin/authority/:actorId/occupations` | occupations |
| `ahg_authority_occupation_save` | `/api/authority/occupation/save` | apiOccupationSave |
| `ahg_authority_occupation_delete` | `/api/authority/occupation/:id/delete` | apiOccupationDelete |
| `ahg_authority_functions` | `/admin/authority/:actorId/functions` | functions |
| `ahg_authority_function_browse` | `/admin/authority/functions/browse` | functionBrowse |
| `ahg_authority_function_save` | `/api/authority/function/save` | apiFunctionSave |
| `ahg_authority_function_delete` | `/api/authority/function/:id/delete` | apiFunctionDelete |
| `ahg_authority_contact` | `/admin/authority/:actorId/contact` | contact |
| `ahg_authority_eac_export` | `/api/authority/eac-cpf/:actorId` | apiEacExport |
| `ahg_authority_config` | `/admin/authority/config` | config |
| `ahg_authority_dedup` | `/admin/authority/dedup` | index |
| `ahg_authority_dedup_scan` | `/admin/authority/dedup/scan` | scan |
| `ahg_authority_dedup_compare` | `/admin/authority/dedup/compare/:id` | compare |
| `ahg_authority_dedup_dismiss` | `/api/authority/dedup/dismiss/:id` | apiDismiss |
| `ahg_authority_dedup_merge` | `/api/authority/dedup/merge/:id` | apiMerge |
| `ahg_authority_ner_pipeline` | `/admin/authority/ner-pipeline` | index |
| `ahg_authority_ner_create_stub` | `/api/authority/ner/create-stub` | apiCreateStub |
| `ahg_authority_ner_promote` | `/api/authority/ner/:id/promote` | apiPromote |
| `ahg_authority_ner_reject` | `/api/authority/ner/:id/reject` | apiReject |

## Module actions

**`authority`** — `dashboard`, `workqueue`, `identifiers`, `apiIdentifierSave`, `apiIdentifierDelete`, `apiIdentifierVerify`, `apiWikidataSearch`, `apiViafSearch`, `apiUlanSearch`, `apiLcnafSearch`, `apiCompletenessRecalc`, `apiCompletenessBatchAssign`, `apiGraphData`, `merge`, `split`, `apiMergePreview`, `apiMergeExecute`, `apiSplitExecute`, `occupations`, `apiOccupationSave`, `apiOccupationDelete`, `functions`, `functionBrowse`, `apiFunctionSave`, `apiFunctionDelete`, `contact`, `apiEacExport`, `config`
**`authorityDedup`** — `index`, `scan`, `compare`, `apiDismiss`, `apiMerge`
**`authorityNer`** — `index`, `apiCreateStub`, `apiPromote`, `apiReject`

## CLI tasks

- `php symfony authority:completeness-scan` — Calculate completeness scores for authority records
- `php symfony authority:dedup-scan` — Scan for duplicate authority records
- `php symfony authority:function-sync` — Sync and validate actor-function links
- `php symfony authority:merge-report` — Generate authority merge/split report
- `php symfony authority:ner-pipeline` — Create authority stubs from NER entities

## Service layer

### `AuthorityEacExportService`  
`lib/Services/AuthorityEacExportService.php`

Public methods: `getEacIdentifiers()`, `enrichEacXml()`, `exportActor()`

### `AuthorityDedupeService`  
`lib/Services/AuthorityDedupeService.php`

Public methods: `scan()`, `calculateSimilarity()`, `normalizeText()`, `jaroWinkler()`, `getStats()`

### `AuthorityOccupationService`  
`lib/Services/AuthorityOccupationService.php`

Public methods: `getOccupations()`, `save()`, `delete()`, `getOccupationTerms()`, `browseByOccupation()`, `getStats()`

### `AuthorityCompletenessService`  
`lib/Services/AuthorityCompletenessService.php`

Public methods: `calculateScore()`, `determineLevel()`, `getCompleteness()`, `getDashboardStats()`, `getWorkqueue()`, `batchAssign()`, `batchCalculate()`

### `AuthorityMergeService`  
`lib/Services/AuthorityMergeService.php`

Public methods: `getMerge()`, `getMergeHistory()`, `compareActors()`, `createMergeRequest()`, `executeMerge()`, `createSplitRequest()`

### `AuthorityGraphService`  
`lib/Services/AuthorityGraphService.php`

Public methods: `getGraphData()`

### `AuthorityFunctionService`  
`lib/Services/AuthorityFunctionService.php`

Public methods: `isEnabled()`, `getFunctionLinks()`, `getActorsForFunction()`, `save()`, `delete()`, `searchFunctions()`, `browseFunctions()`, `getStats()`

### `AuthorityLookupService`  
`lib/Services/AuthorityLookupService.php`

Public methods: `isSourceEnabled()`, `searchWikidata()`, `searchViaf()`, `searchUlan()`, `searchLcnaf()`, `searchIsni()`

### `AuthorityNerPipelineService`  
`lib/Services/AuthorityNerPipelineService.php`

Public methods: `getPendingEntities()`, `getStubs()`, `findMatchingActors()`, `createStub()`, `promoteStub()`, `rejectStub()`, `getStats()`

### `AuthorityIdentifierService`  
`lib/Services/AuthorityIdentifierService.php`

Public methods: `getIdentifiers()`, `getById()`, `save()`, `delete()`, `verify()`, `hasIdentifiers()`, `getStats()`, `buildUri()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
