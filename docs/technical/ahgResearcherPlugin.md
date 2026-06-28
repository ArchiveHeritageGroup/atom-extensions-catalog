# ahgResearcherPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Researcher collection upload and approval workflow — online submissions and offline exchange import with two-step archivist review

## Overview

- **Name:** Researcher Collection Upload
- **Machine name:** `ahgResearcherPlugin`
- **Version:** 1.0.0
- **Category:** research
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Database tables

- `researcher_submission`
- `researcher_submission_file`
- `researcher_submission_item`
- `researcher_submission_review`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `researcher_dashboard` | `/researcher` | dashboard |
| `researcher_submissions` | `/researcher/submissions` | submissions |
| `researcher_new_submission` | `/researcher/submission/new` | newSubmission |
| `researcher_view_submission` | `/researcher/submission/:id` | viewSubmission |
| `researcher_edit_submission` | `/researcher/submission/:id/edit` | editSubmission |
| `researcher_add_item` | `/researcher/submission/:id/item/add` | addItem |
| `researcher_edit_item` | `/researcher/submission/:id/item/:itemId` | editItem |
| `researcher_delete_item` | `/researcher/submission/:id/item/:itemId/delete` | deleteItem |
| `researcher_submit` | `/researcher/submission/:id/submit` | submit |
| `researcher_resubmit` | `/researcher/submission/:id/resubmit` | resubmit |
| `researcher_from_collection` | `/researcher/from-collection/:collectionId` | createFromCollection |
| `researcher_import_exchange` | `/researcher/import` | importExchange |
| `researcher_publish` | `/researcher/submission/:id/publish` | publish |
| `researcher_api_upload` | `/researcher/api/upload` | apiUpload |
| `researcher_api_delete_file` | `/researcher/api/delete-file` | apiDeleteFile |
| `researcher_api_autocomplete` | `/researcher/api/autocomplete` | apiAutocomplete |

## Module actions

**`researcher`** — `dashboard`, `submissions`, `newSubmission`, `viewSubmission`, `editSubmission`, `addItem`, `editItem`, `deleteItem`, `submit`, `resubmit`, `importExchange`, `createFromCollection`, `publish`, `apiUpload`, `apiDeleteFile`, `apiAutocomplete`

## Service layer

### `PublishService`  
`lib/Services/PublishService.php`

Public methods: `publish()`

### `SubmissionService`  
`lib/Services/SubmissionService.php`

Public methods: `getStagingDir()`, `createSubmission()`, `getSubmission()`, `getSubmissions()`, `getPendingReviews()`, `updateSubmission()`, `deleteSubmission()`, `recalculateTotals()`, `addItem()`, `updateItem()`, `deleteItem()`, `getItem()`, `addFile()`, `addFileFromData()`, `deleteFile()`, `getFile()`, `submitForReview()`, `resubmit()`

### `ExchangeImportService`  
`lib/Services/ExchangeImportService.php`

Public methods: `import()`, `parseExchangeJson()`, `importNotesCollection()`, `importFilesCollection()`, `importNewItemsCollection()`, `importNewCreatorsCollection()`, `importNewRepositoriesCollection()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
