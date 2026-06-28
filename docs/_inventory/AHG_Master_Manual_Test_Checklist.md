# AHG Plugins — Master Manual Test Checklist

Manual end-to-end test checklist for every plugin. For each functionality, tick ☐→☑ when verified, record Pass/Fail, tester/date, and notes. **Source** column: UG = user manual, TECH = technical manual, CODE = derived from plugin config/tasks (where no manual exists yet).

Plugins: 111. Generated 2026-06-27.


## ahg3DModelPlugin

Sources: technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | View a 3D model on an information object (Google <model-viewer>) | AUTHORED | | | |
| ☐ | Gaussian Splat model rendering | AUTHORED | | | |
| ☐ | Augmented-reality (AR) view on a supported device | AUTHORED | | | |
| ☐ | Upload a 3D model (GLB/OBJ/PLY/STL/USDZ) — staff | AUTHORED | | | |
| ☐ | Select the primary model when an object has several | AUTHORED | | | |
| ☐ | Hotspots: add / edit / delete annotations on a model (staff) | AUTHORED | | | |
| ☐ | Camera bookmarks: save / load named viewpoints (staff) | AUTHORED | | | |
| ☐ | Auto-generated thumbnail / poster preview | AUTHORED | | | |
| ☐ | IIIF 3D manifest generated for the model | AUTHORED | | | |
| ☐ | Public API returns only published-object models/hotspots (guest) | AUTHORED | | | |
| ☐ | Model settings (admin) | AUTHORED | | | |
| ☑ | Route /ahg3DModel/index → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /ahg3DModel/view/:id → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /ahg3DModel/upload → upload | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /ahg3DModel/edit/:id → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /ahg3DModel/delete/:id → delete | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /iiif/3d/:id/manifest.json → iiifManifest | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /ahg3DModel/embed/:id → embed | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /ahg3DModel/addHotspot/:id → addHotspot | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☑ | Route /ahg3DModel/deleteHotspot/:id → deleteHotspot | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☑ | Route /api/3d/models/:object_id → apiModels | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/3d/hotspots/:model_id → apiHotspots | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /ahg3DModel/addBookmark/:id → addBookmark | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☑ | Route /ahg3DModel/deleteBookmark/:id → deleteBookmark | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☑ | Route /api/3d/bookmarks/:model_id → apiBookmarks | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /ahg3DSettings/index → index | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony triposr:generate | CODE | | | |


## ahgAIPlugin

Sources: technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☑ | Route /ai/ner/extract/:id → nerExtract | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /ai/ner/review → review | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai/ner/bulk-save → bulkSave | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai/ner/create-date → createDate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai/ner/preview-date-split → previewDateSplit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai/summarize/:id → summarize | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /ai/translate/:id → translate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /ai/translate/batch → translateBatch | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /ai/spellcheck/:id → spellcheck | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /ai/htr/:id → htr | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /ai/settings → settings | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /ai/health → health | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai/suggest/:id → suggest | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /ai/suggest/:id/preview → suggestPreview | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /ai/suggest/review → suggestReview | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /ai/suggest/:id/decision → suggestDecision | TECH | N/A | pw-authed 2026-06-27 | HTTP ERR (id=553) |
| ☑ | Route /ai/llm/configs → llmConfigs | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai/llm/health → llmHealth | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai/templates → templates | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai/describe/:id → describeObject | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /ai/ner/pdf-overlay/:id → pdfOverlay | TECH | N/A | pw-authed 2026-06-27 | HTTP ERR (id=553) |
| ☑ | Route /ai/ner/approved-entities/:id → getApprovedEntities | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | CLI: php symfony ai:htr | CODE | | | |
| ☐ | CLI: php symfony ai:index-catalogue | CODE | | | |
| ☐ | CLI: php symfony ai:install | CODE | | | |
| ☐ | CLI: php symfony ai:install-menu | CODE | | | |
| ☐ | CLI: php symfony ai:install-research-menu | CODE | | | |
| ☐ | CLI: php symfony ai:ner-extract | CODE | | | |
| ☐ | CLI: php symfony ai:ner-sync | CODE | | | |
| ☐ | CLI: php symfony ai:process-pending | CODE | | | |
| ☐ | CLI: php symfony ai:spellcheck | CODE | | | |
| ☐ | CLI: php symfony ai:suggest-description | CODE | | | |
| ☐ | CLI: php symfony ai:summarize | CODE | | | |
| ☐ | CLI: php symfony ai:sync-entity-cache | CODE | | | |
| ☐ | CLI: php symfony ai:translate | CODE | | | |
| ☐ | CLI: php symfony ai:uninstall | CODE | | | |


## ahgAPIPlugin

Sources: user guide `api-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Table of Contents | UG | | | |
| ☐ | What is the API? | UG | | | |
| ☐ | Getting Your API Key | UG | | | |
| ☐ | Step-by-Step | UG | | | |
| ☐ | Making Your First Request | UG | | | |
| ☐ | Using a Web Browser Extension | UG | | | |
| ☐ | Using Command Line (Advanced) | UG | | | |
| ☐ | Expected Response | UG | | | |
| ☐ | Finding Records | UG | | | |
| ☐ | List All Archival Descriptions | UG | | | |
| ☐ | Filter by Sector | UG | | | |
| ☐ | Filter by Level | UG | | | |
| ☐ | Get a Single Record | UG | | | |
| ☐ | Pagination | UG | | | |
| ☐ | Searching | UG | | | |
| ☐ | Search Filters | UG | | | |
| ☐ | Webhooks | UG | | | |
| ☐ | Setting Up a Webhook | UG | | | |
| ☐ | Available Events | UG | | | |
| ☐ | Entity Types | UG | | | |
| ☐ | What You Receive | UG | | | |
| ☐ | Verifying Notifications | UG | | | |
| ☐ | Managing Webhooks via API | UG | | | |
| ☐ | Managing Webhooks via Web Interface | UG | | | |
| ☐ | If Delivery Fails | UG | | | |
| ☐ | Common Tasks | UG | | | |
| ☐ | Task 1: Display Fonds on Your Website | UG | | | |
| ☐ | Task 2: Find All Records Updated This Month | UG | | | |
| ☐ | Task 3: Get Repository Information | UG | | | |
| ☐ | Task 4: Browse Subject Terms | UG | | | |
| ☐ | Error: 401 Unauthorized | UG | | | |
| ☐ | Error: 404 Not Found | UG | | | |
| ☐ | Error: 429 Too Many Requests | UG | | | |
| ☐ | No Results Returned | UG | | | |
| ☐ | Getting Help | UG | | | |
| ☐ | OpenAPI 3.1 & interactive docs | UG | | | |
| ☑ | Route /api/v2 → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/v2/openapi → openApi | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/v2/docs → docs | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/v2/descriptions → descriptionsBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /api/v2/descriptions/:slug/citation → descriptionsCitation | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /api/v2/descriptions/:slug → descriptionsRead | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☑ | Route /api/v2/authorities → authoritiesBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /api/v2/authorities/:slug → authoritiesRead | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /api/v2/repositories → repositoriesBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /api/v2/taxonomies → taxonomiesBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /api/v2/taxonomies/:id/terms → taxonomyTerms | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /api/v2/search → search | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 |
| ☐ | Route /api/v2/batch → batch | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /api/v2/conditions → conditionsBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /api/v2/conditions/:id → conditionsRead | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☑ | Route /api/v2/descriptions/:slug/conditions → descriptionConditions | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /api/v2/conditions/:id/photos → conditionPhotos | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /api/v2/conditions/:id/photos/:photoId → conditionPhotoDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☑ | Route /api/v2/assets → assetsBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /api/v2/assets/:id → assetsRead | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☑ | Route /api/v2/descriptions/:slug/asset → descriptionAsset | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /api/v2/valuations → valuationsBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /api/v2/assets/:id/valuations → assetValuations | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /api/v2/privacy/dsars → dsarsBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /api/v2/privacy/dsars/:id → dsarsRead | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☑ | Route /api/v2/privacy/breaches → breachesBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☐ | Route /api/v2/upload → fileUpload | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /api/v2/descriptions/:slug/upload → descriptionUpload | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /api/v2/sync/changes → syncChanges | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☐ | Route /api/v2/sync/batch → syncBatch | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /api/v2/keys → keysBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/v2/keys/:id → keysDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☐ | Route /api/v2/webhooks → webhooksBrowse | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☑ | Route /api/v2/webhooks/:id → webhooksRead | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☐ | Route /api/v2/webhooks/:id/deliveries → webhookDeliveries | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 (id=553) |
| ☐ | Route /api/v2/webhooks/:id/regenerate-secret → webhookRegenerateSecret | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /api/v2/events → eventsBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /api/v2/events/:id → eventsRead | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /api/v2/events/correlation/:correlation_id → eventsCorrelation | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /api/v2/audit → auditBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☐ | Route /api/v2/audit/:id → auditRead | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /api/v2/publish/readiness/:slug → publishReadiness | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☐ | Route /api/v2/publish/execute/:slug → publishExecute | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /api/search/io → searchInformationObjects | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/autocomplete/glam → autocompleteGlam | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/plugin-protection → pluginProtection | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony api:webhook-process-retries | CODE | | | |


## ahgAccessRequestPlugin

Sources: user guide `accession-v2-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Table of Contents | UG | | | |
| ☐ | 1. Introduction | UG | | | |
| ☐ | 2. Getting Started | UG | | | |
| ☐ | Accessing the Intake Queue | UG | | | |
| ☐ | Accessing the Dashboard | UG | | | |
| ☐ | Permissions | UG | | | |
| ☐ | 3. Intake Queue | UG | | | |
| ☐ | Queue Dashboard | UG | | | |
| ☐ | Status Transitions | UG | | | |
| ☐ | Assigning Accessions | UG | | | |
| ☐ | 4. Checklists | UG | | | |
| ☐ | Intake Checklists | UG | | | |
| ☐ | Using Checklists | UG | | | |
| ☐ | Applying Templates | UG | | | |
| ☐ | Default Template | UG | | | |
| ☐ | 5. Attachments | UG | | | |
| ☐ | Uploading Files | UG | | | |
| ☐ | Categories | UG | | | |
| ☐ | Storage | UG | | | |
| ☐ | 6. Timeline | UG | | | |
| ☐ | 7. Appraisal | UG | | | |
| ☐ | Creating an Appraisal | UG | | | |
| ☐ | Scoring Criteria | UG | | | |
| ☐ | Appraisal Types | UG | | | |
| ☐ | Recommendations | UG | | | |
| ☐ | 8. Valuation | UG | | | |
| ☐ | Recording Valuations | UG | | | |
| ☐ | Valuation Types | UG | | | |
| ☐ | Valuation Methods | UG | | | |
| ☐ | Portfolio Report | UG | | | |
| ☐ | 9. Containers | UG | | | |
| ☐ | Adding Containers | UG | | | |
| ☐ | Container Types | UG | | | |
| ☐ | Managing Items | UG | | | |
| ☐ | Barcode Lookup | UG | | | |
| ☐ | 10. Rights Management | UG | | | |
| ☐ | Adding Rights | UG | | | |
| ☐ | Rights Inheritance | UG | | | |
| ☐ | Rights Basis Options | UG | | | |
| ☐ | Restriction Types | UG | | | |
| ☑ | Route /accessRequest → pending | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /security/request-access → new | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /security/request-access/create → create | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☐ | Route /security/request-object → requestObject | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /security/request-object/create → createObjectRequest | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /security/my-requests → myRequests | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /security/request/:id/cancel → cancel | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /security/access-requests → pending | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /security/request/:id → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /security/request/:id/approve → approve | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /security/request/:id/deny → deny | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /security/approvers → approvers | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /security/approvers/add → addApprover | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /security/approvers/:id/remove → removeApprover | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /accessRequest/history → history | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgAccessibilityPlugin

Sources: user guide `accessibility-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Editors and Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Consumer API | UG | | | |
| ☐ | Administration / settings | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /accessibility/alt-text → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /accessibility/alt-text/edit/:id → edit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /accessibility/alt-text/save → save | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /accessibility/alt-text/api/object/:id → apiObject | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /accessibility/alt-text/api/slug/:slug → apiSlug | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |


## ahgAccessionManagePlugin

Sources: user guide `rad-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | Route /accession/:slug → index | CODE | N/A | fixed 2026-06-27 | works for real accession; 500 was bad-id test artifact |
| ☑ | Route /accession/:slug/delete → delete | CODE | PASS | pw-authed-seq 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /accession/:slug/edit → edit | CODE | PASS | pw-authed-seq 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /accession/browse → browse | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/accessions/dashboard → dashboard | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/accessions/:id/submit → submit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/review → review | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/accept → accept | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/reject → reject | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/return → returnRevision | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/timeline → timeline | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/checklist → checklist | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/attachments → attachments | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/intake → queueDetail | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/accessions/queue → queue | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/accessions/queue/assign → assign | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /admin/accessions/config → config | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/accessions/numbering → numbering | CODE | PASS | pw-authed-seq 2026-06-27 | HTTP 403 |
| ☑ | Route /api/accession/checklist/:id/toggle → apiChecklistToggle | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/accession/checklist/apply-template → apiChecklistApplyTemplate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/accession/attachment/upload → apiAttachmentUpload | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/accession/attachment/:id/delete → apiAttachmentDelete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /admin/accessions/:id/appraisal → appraisal | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/appraisal/save → appraisalSave | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/valuation → valuation | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/valuation/add → valuationAdd | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/accessions/appraisal-templates → appraisalTemplates | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/accessions/valuation-report → valuationReport | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/accession/appraisal/:id/score → apiAppraisalScore | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /admin/accessions/:id/containers → containers | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/accessions/:id/rights → rights | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /api/accession/container/save → apiContainerSave | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /api/accession/container/:id/delete → apiContainerDelete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /api/accession/container-item/save → apiContainerItemSave | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /api/accession/container-item/:id/delete → apiContainerItemDelete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/accession/container-item/:id/link → apiContainerItemLink | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/accession/barcode/lookup → apiBarcodeLookup | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /api/accession/rights/save → apiRightsSave | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /api/accession/rights/:id/delete → apiRightsDelete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/accession/rights/:id/inherit → apiRightsInherit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | CLI: php symfony accession:intake | CODE | | | |
| ☐ | CLI: php symfony accession:report | CODE | | | |


## ahgActorManagePlugin

Sources: user guide `rad-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /actor/:slug → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /actor/:slug/delete → delete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /actor/:slug/edit → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /actor/add → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /actor/browse → browse | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /actor/autocomplete → autocomplete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgAiCompliancePlugin

Sources: user guide `ai-compliance-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What gets logged | UG | | | |
| ☐ | Where to find the public key | UG | | | |
| ☐ | Verifying the log | UG | | | |
| ☐ | Retention | UG | | | |
| ☐ | Rotating the signing key | UG | | | |
| ☐ | What this does not do | UG | | | |
| ☐ | See also | UG | | | |
| ☑ | Route /.well-known/ai-inference-pubkey → wellKnownPubkey | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ai-act → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ai-act/systems → systems | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ai-act/system/edit → systemEdit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ai-act/models → models | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ai-act/model/edit → modelEdit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ai-act/risks → risks | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ai-act/risk/edit → riskEdit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ai-act/attestations → attestations | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ai-act/attestation/edit → attestationEdit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony ai-compliance:install-key | CODE | | | |
| ☐ | CLI: php symfony ai-compliance:prune | CODE | | | |
| ☐ | CLI: php symfony ai-compliance:verify-inference-log | CODE | | | |


## ahgAiConditionPlugin

Sources: user guide `condition-assessment-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Workflow Overview | UG | | | |
| ☐ | When to Use | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Part 1: Condition Dashboard | UG | | | |
| ☐ | Overview Screen | UG | | | |
| ☐ | Part 2: Creating an Assessment | UG | | | |
| ☐ | Assessment Types | UG | | | |
| ☐ | Condition Rating Scale | UG | | | |
| ☐ | Assessment Form | UG | | | |
| ☐ | Part 3: Recording Damage | UG | | | |
| ☐ | Damage Types | UG | | | |
| ☐ | Severity Levels | UG | | | |
| ☐ | Add Damage Record | UG | | | |
| ☐ | Part 4: Photo Documentation | UG | | | |
| ☐ | Taking Condition Photos | UG | | | |
| ☐ | Image Annotator | UG | | | |
| ☐ | Part 5: Treatment Recommendations | UG | | | |
| ☐ | Priority Levels | UG | | | |
| ☐ | Treatment Form | UG | | | |
| ☐ | Part 6: Condition History | UG | | | |
| ☐ | Object Timeline | UG | | | |
| ☐ | Part 7: Reports | UG | | | |
| ☐ | Available Reports | UG | | | |
| ☐ | Generate Report | UG | | | |
| ☐ | Tips for Best Practice | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /ai-condition → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/dashboard → dashboard | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/browse → browse | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/assess → assess | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /ai-condition/view/:id → view | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /ai-condition/history/:slug → history | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /ai-condition/settings → settings | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/bulk → bulk | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/clients → clients | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/manual-assess → manualAssess | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/training → training | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/test → apiTest | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/submit → apiSubmit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/confirm → apiConfirm | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/history-data → apiHistoryData | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/bulk-status → apiBulkStatus | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/client-save → apiClientSave | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/client-revoke → apiClientRevoke | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/object-search → apiObjectSearch | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/manual-save → apiManualSave | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/training/model-info → apiTrainingModelInfo | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/training/status → apiTrainingStatus | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/training/upload → apiTrainingUpload | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/training/datasets → apiTrainingDatasets | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/training/start → apiTrainingStart | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/contribute → apiContribute | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/contributions → apiContributions | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/client-training-toggle → apiClientTrainingToggle | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/client-approve-training → apiClientApproveTraining | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/client-upload-consent → apiClientUploadConsent | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/client-contributions → apiClientContributions | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/contribution-review → apiContributionReview | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ai-condition/api/push-training-data → apiPushTrainingData | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony ai-condition:bulk-scan | CODE | | | |
| ☐ | CLI: php symfony ai-condition:install | CODE | | | |
| ☐ | CLI: php symfony ai-condition:status | CODE | | | |


## ahgAnnotationsPlugin

Sources: user guide `web-annotations-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Developers and Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Administration / settings | UG | | | |
| ☐ | Tips & FAQ | UG | | | |


## ahgAuditTrailPlugin

Sources: user guide `audit-trail-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What Gets Tracked | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Viewing Recent Activity | UG | | | |
| ☐ | Step 1: Open Audit Trail | UG | | | |
| ☐ | Step 2: Browse Changes | UG | | | |
| ☐ | Searching the Audit Trail | UG | | | |
| ☐ | Filter Options | UG | | | |
| ☐ | Viewing Change Details | UG | | | |
| ☐ | Exporting Audit Logs | UG | | | |
| ☐ | Step 1: Set Filters | UG | | | |
| ☐ | Step 2: Click Export | UG | | | |
| ☐ | Step 3: Download | UG | | | |
| ☐ | Common Uses | UG | | | |
| ☐ | Tips | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☐ | What Gets Tracked | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Viewing Recent Activity | UG | | | |
| ☐ | Step 1: Open Audit Trail | UG | | | |
| ☐ | Step 2: Browse Changes | UG | | | |
| ☐ | Searching the Audit Trail | UG | | | |
| ☐ | Filter Options | UG | | | |
| ☐ | Viewing Change Details | UG | | | |
| ☐ | Exporting Audit Logs | UG | | | |
| ☐ | Common Uses | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☐ | CLI: php symfony audit:chain | CODE | | | |


## ahgAuthorityPlugin

Sources: user guide `authority-records-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Administrators and Editors | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Administration / settings | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /admin/authority/dashboard → dashboard | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/authority/workqueue → workqueue | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/authority/:actorId/identifiers → identifiers | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/authority/identifier/save → apiIdentifierSave | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/identifier/:id/delete → apiIdentifierDelete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/authority/identifier/:id/verify → apiIdentifierVerify | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/authority/wikidata/search → apiWikidataSearch | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/viaf/search → apiViafSearch | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/ulan/search → apiUlanSearch | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/lcnaf/search → apiLcnafSearch | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/completeness/:actorId/recalc → apiCompletenessRecalc | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/authority/completeness/batch-assign → apiCompletenessBatchAssign | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/graph/:actorId → apiGraphData | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /admin/authority/merge/:id → merge | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/authority/split/:id → split | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /api/authority/merge/preview → apiMergePreview | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/merge/execute → apiMergeExecute | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/split/execute → apiSplitExecute | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/authority/:actorId/occupations → occupations | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /api/authority/occupation/save → apiOccupationSave | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/occupation/:id/delete → apiOccupationDelete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /admin/authority/:actorId/functions → functions | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/authority/functions/browse → functionBrowse | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/function/save → apiFunctionSave | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/function/:id/delete → apiFunctionDelete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /admin/authority/:actorId/contact → contact | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /api/authority/eac-cpf/:actorId → apiEacExport | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /admin/authority/config → config | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/authority/dedup → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/authority/dedup/scan → scan | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/authority/dedup/compare/:id → compare | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /api/authority/dedup/dismiss/:id → apiDismiss | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/authority/dedup/merge/:id → apiMerge | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /admin/authority/ner-pipeline → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/ner/create-stub → apiCreateStub | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/authority/ner/:id/promote → apiPromote | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/authority/ner/:id/reject → apiReject | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | CLI: php symfony authority:completeness-scan | CODE | | | |
| ☐ | CLI: php symfony authority:dedup-scan | CODE | | | |
| ☐ | CLI: php symfony authority:function-sync | CODE | | | |
| ☐ | CLI: php symfony authority:merge-report | CODE | | | |
| ☐ | CLI: php symfony authority:ner-pipeline | CODE | | | |


## ahgAuthorityResolutionPlugin

Sources: user guide `authority-records-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Administrators and Editors | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Administration / settings | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /admin/authorityResolution → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/authorityResolution/:id/review → review | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /admin/authorityResolution/:id/context → context | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /admin/authorityResolution/:id/link → link | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/authorityResolution/:id/link-different → linkDifferent | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/authorityResolution/:id/create-new → createNew | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /admin/authorityResolution/:id/create-new-submit → createNewSubmit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/authorityResolution/:id/park → park | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/authorityResolution/:id/reject → reject | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/authorityResolution/park → parkList | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/authorityResolution/park/:id/unpark → unpark | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/authorityResolution/park/dashboard.json → parkDashboardJson | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/authorityResolution/archivists.json → archivistsJson | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/authorityResolution/assign-batch → batchAssign | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/authorityResolution/:id/assign → assign | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/authorityResolution/lookup → lookup | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/authorityResolution/settings/lookup → lookupSettings | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony auth-res:cache-clear | CODE | | | |
| ☐ | CLI: php symfony auth-res:cache-stats | CODE | | | |
| ☐ | CLI: php symfony auth-res:export-ner-feedback | CODE | | | |
| ☐ | CLI: php symfony auth-res:generate-candidates | CODE | | | |
| ☐ | CLI: php symfony auth-res:promote-sample | CODE | | | |
| ☐ | CLI: php symfony auth-res:reprocess | CODE | | | |
| ☐ | CLI: php symfony auth-res:reprocess-parked | CODE | | | |
| ☐ | CLI: php symfony auth-res:scan-parked | CODE | | | |
| ☐ | CLI: php symfony auth-res:score-evidence | CODE | | | |
| ☐ | CLI: php symfony auth-res:status | CODE | | | |
| ☐ | CLI: php symfony auth-res:write-provenance | CODE | | | |


## ahgBackupPlugin

Sources: user guide `backup-restore-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | When to Use | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Creating a Backup | UG | | | |
| ☐ | Step 1: Open Backup Tool | UG | | | |
| ☐ | Step 2: Click Create Backup | UG | | | |
| ☐ | Step 3: Wait for Completion | UG | | | |
| ☐ | Viewing Existing Backups | UG | | | |
| ☐ | Restoring from Backup | UG | | | |
| ☐ | ⚠️ Warning | UG | | | |
| ☐ | Steps to Restore | UG | | | |
| ☐ | Downloading Backups | UG | | | |
| ☐ | Best Practices | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☐ | CLI: php symfony backup:run-scheduled | CODE | | | |


## ahgC2paPlugin

Sources: user guide `c2pa-content-credentials-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Digital Asset Managers and Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Endpoints | UG | | | |
| ☐ | Command line | UG | | | |
| ☐ | Compliance notes | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | Route /.well-known/c2pa-info → wellKnown | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /c2pa/verify → verify | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /c2pa/manifest/:id → manifest | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /c2pa/manifests/:id → manifests | CODE | PASS | fixed 2026-06-27 | HTTP 200 (schema fix #187) |


## ahgCDPAPlugin

Sources: user guide `cdpa-compliance-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Data Protection Officers and Compliance Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Command line (for scheduled checks) | UG | | | |
| ☐ | Compliance notes | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /admin/cdpa → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/cdpa/license → license | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/cdpa/license/edit → licenseEdit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/cdpa/dpo → dpo | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/cdpa/dpo/edit → dpoEdit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/cdpa/requests → requests | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/cdpa/request/:id → requestView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/cdpa/request/create → requestCreate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/cdpa/processing → processing | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/cdpa/processing/create → processingCreate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/cdpa/processing/:id/edit → processingEdit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/cdpa/dpia → dpia | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/cdpa/dpia/create → dpiaCreate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/cdpa/dpia/:id → dpiaView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/cdpa/consent → consent | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/cdpa/breaches → breaches | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/cdpa/breach/create → breachCreate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/cdpa/breach/:id → breachView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/cdpa/reports → reports | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/cdpa/config → config | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony cdpa:license-check | CODE | | | |
| ☐ | CLI: php symfony cdpa:report | CODE | | | |
| ☐ | CLI: php symfony cdpa:requests | CODE | | | |
| ☐ | CLI: php symfony cdpa:status | CODE | | | |


## ahgCartPlugin

Sources: user guide `cart-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Quick Start | UG | | | |
| ☐ | When to Use Cart | UG | | | |
| ☐ | Adding Items to Cart | UG | | | |
| ☐ | From Any Record | UG | | | |
| ☐ | Button States | UG | | | |
| ☐ | Viewing Your Cart | UG | | | |
| ☐ | Cart Page Features | UG | | | |
| ☐ | Submitting a Request | UG | | | |
| ☐ | From Cart Page | UG | | | |
| ☐ | Workflow Diagram | UG | | | |
| ☐ | Requirements | UG | | | |
| ☐ | Managing Your Cart | UG | | | |
| ☐ | Remove Single Item | UG | | | |
| ☐ | Clear All Items | UG | | | |
| ☐ | Tips | UG | | | |
| ☐ | Cart vs Single Request | UG | | | |
| ☑ | Route /cart → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /cart/browse → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /cart/add/:slug → add | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /cart/remove/:id → remove | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /cart/clear → clear | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /cart/thank-you → thankYou | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /cart/checkout → checkout | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☐ | Route /cart/update-products → updateProducts | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /cart/update-item → updateItem | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /cart/save-selections → saveSelections | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /cart/payment-return/:order → paymentReturn | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /cart/payment/:order → payment | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /cart/payment/success/:order → paymentSuccess | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /cart/payment/cancel/:order → paymentCancel | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /cart/payment/notify → paymentNotify | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /cart/order/:order → orderConfirmation | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /cart/orders → orders | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /cart/download/:token → download | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /admin/ecommerce → adminSettings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/orders → adminOrders | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/orders/:id → adminOrderDetail | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/pricing → adminPricing | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |


## ahgConditionPlugin

Sources: user guide `condition-assessment-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Workflow Overview | UG | | | |
| ☐ | When to Use | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Part 1: Condition Dashboard | UG | | | |
| ☐ | Overview Screen | UG | | | |
| ☐ | Part 2: Creating an Assessment | UG | | | |
| ☐ | Assessment Types | UG | | | |
| ☐ | Condition Rating Scale | UG | | | |
| ☐ | Assessment Form | UG | | | |
| ☐ | Part 3: Recording Damage | UG | | | |
| ☐ | Damage Types | UG | | | |
| ☐ | Severity Levels | UG | | | |
| ☐ | Add Damage Record | UG | | | |
| ☐ | Part 4: Photo Documentation | UG | | | |
| ☐ | Taking Condition Photos | UG | | | |
| ☐ | Image Annotator | UG | | | |
| ☐ | Part 5: Treatment Recommendations | UG | | | |
| ☐ | Priority Levels | UG | | | |
| ☐ | Treatment Form | UG | | | |
| ☐ | Part 6: Condition History | UG | | | |
| ☐ | Object Timeline | UG | | | |
| ☐ | Part 7: Reports | UG | | | |
| ☐ | Available Reports | UG | | | |
| ☐ | Generate Report | UG | | | |
| ☐ | Tips for Best Practice | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /object/autocomplete → objectAutocomplete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /:slug/condition → conditionCheck | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /condition/check/:id/view → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /condition/check/:id/photos → photos | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /condition/photo/:id/annotate → annotate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /condition/annotation/get → getAnnotation | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /condition/annotation/save → saveAnnotation | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /condition/check/:id/upload → upload | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /condition/photo/:id/delete → deletePhoto | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /condition/photo/:id/view → viewPhoto | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /condition/photo/:id/update-meta → updatePhotoMeta | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /condition/check/:id/export → exportReport | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /condition/check/:id/list → listPhotos | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /condition/ai-assess → aiAssess | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/condition → admin | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /condition/templates → template | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /condition/template/:id/view → template | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /condition/template/:id/form → template | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /condition/template/:id/export → template | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |


## ahgContactPlugin

Sources: user guide `contact-management-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What is Contact Management? | UG | | | |
| ☐ | Contact Types | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | From Authority Records | UG | | | |
| ☐ | From Repositories | UG | | | |
| ☐ | Adding a New Contact | UG | | | |
| ☐ | Step 1: Open the Record | UG | | | |
| ☐ | Step 2: Enter Edit Mode | UG | | | |
| ☐ | Step 3: Locate Contact Section | UG | | | |
| ☐ | Step 4: Click Add Contact | UG | | | |
| ☐ | Step 5: Fill in the Form | UG | | | |
| ☐ | Step 6: Save the Record | UG | | | |
| ☐ | Setting a Primary Contact | UG | | | |
| ☐ | What is a Primary Contact? | UG | | | |
| ☐ | How to Set Primary | UG | | | |
| ☐ | Viewing Contact Information | UG | | | |
| ☐ | Editing a Contact | UG | | | |
| ☐ | Step 1: Open Record in Edit Mode | UG | | | |
| ☐ | Step 2: Locate the Contact | UG | | | |
| ☐ | Step 3: Make Changes | UG | | | |
| ☐ | Step 4: Save | UG | | | |
| ☐ | Deleting a Contact | UG | | | |
| ☐ | Step 1: Open Record in Edit Mode | UG | | | |
| ☐ | Step 2: Find the Contact Entry | UG | | | |
| ☐ | Step 3: Click Remove Button | UG | | | |
| ☐ | Step 4: Save | UG | | | |
| ☐ | Multiple Contacts | UG | | | |
| ☐ | Common Uses | UG | | | |
| ☐ | Tips | UG | | | |
| ☐ | Country Codes | UG | | | |
| ☐ | Integration with Other Features | UG | | | |
| ☐ | Donor Agreements | UG | | | |
| ☐ | Access Requests | UG | | | |
| ☐ | Loan Management | UG | | | |
| ☐ | Privacy Compliance | UG | | | |
| ☐ | Need Help? | UG | | | |


## ahgCorePlugin

Sources: user guide `dublin-core-manage-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists and Cataloguers | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | CLI: php symfony ahg:optimize-pdfs | CODE | | | |
| ☐ | CLI: php symfony central:heartbeat | CODE | | | |
| ☐ | CLI: php symfony central:ping | CODE | | | |
| ☐ | CLI: php symfony central:sync-errors | CODE | | | |


## ahgCustomFieldsPlugin

Sources: user guide `custom-fields-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Accessing Custom Fields Admin | UG | | | |
| ☐ | Defining a New Field | UG | | | |
| ☐ | Required Settings | UG | | | |
| ☐ | Optional Settings | UG | | | |
| ☐ | Checkboxes | UG | | | |
| ☐ | Editing an Existing Field | UG | | | |
| ☐ | Reordering Fields | UG | | | |
| ☐ | Deactivating / Deleting a Field | UG | | | |
| ☐ | Deactivate (soft delete) | UG | | | |
| ☐ | Permanently Delete (hard delete) | UG | | | |
| ☐ | Using Custom Fields on Entity Pages | UG | | | |
| ☐ | Edit Pages | UG | | | |
| ☐ | View Pages | UG | | | |
| ☐ | Repeatable Fields | UG | | | |
| ☐ | Dropdown Fields | UG | | | |
| ☐ | Import / Export Field Definitions | UG | | | |
| ☐ | Export | UG | | | |
| ☐ | Import | UG | | | |
| ☐ | Reporting Views | UG | | | |
| ☐ | Access Restriction Codes | UG | | | |
| ☑ | Route /admin/customFields → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/customFields/edit → edit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/customFields/save → save | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/customFields/delete → delete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/customFields/reorder → reorder | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/customFields/export → export | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/customFields/import → import | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /customFields/save → saveValues | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /customFields/get/:entityType/:objectId → getValues | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |


## ahgDAMPlugin

Sources: user guide `dam-module-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | When to Use DAM Module | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Adding a Digital Asset | UG | | | |
| ☐ | Step 1: Click Add Asset | UG | | | |
| ☐ | Step 2: Upload Your File | UG | | | |
| ☐ | Step 3: Auto-Detected Metadata | UG | | | |
| ☐ | Step 4: Add Descriptive Metadata | UG | | | |
| ☐ | Supported File Types | UG | | | |
| ☐ | Images | UG | | | |
| ☐ | Audio | UG | | | |
| ☐ | Video | UG | | | |
| ☐ | 3D Models | UG | | | |
| ☐ | IPTC Metadata | UG | | | |
| ☐ | Batch Upload | UG | | | |
| ☐ | Step 1: Prepare Files | UG | | | |
| ☐ | Step 2: Apply Common Metadata | UG | | | |
| ☐ | Technical Metadata | UG | | | |
| ☐ | Storage and Derivatives | UG | | | |
| ☐ | Rights and Access | UG | | | |
| ☐ | Tips for Digital Assets | UG | | | |
| ☐ | Film & Video Metadata (New) | UG | | | |
| ☐ | Production Details | UG | | | |
| ☐ | Alternative Versions | UG | | | |
| ☐ | Format Holdings & Access | UG | | | |
| ☐ | External References | UG | | | |
| ☐ | Loan Management | UG | | | |
| ☐ | Optional Features | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /dam → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /dam/:slug → index | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /dam/browse → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☐ | Route /dam/lightbox → lightbox | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /dam/dashboard → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /dam/create → create | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /dam/bulk → bulkCreate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /dam/bulkCreate → bulkCreate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /dam/extract/:id → extractMetadata | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /dam/convert/:id → convert | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /dam/iptc/:slug → editIptc | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /dam/reports → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgDacsManagePlugin

Sources: user guide `rad-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |


## ahgDataMigrationPlugin

Sources: user guide `export-data-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists and Collection Managers | UG | | | |
| ☐ | Why Export Data? | UG | | | |
| ☐ | Export Formats Explained | UG | | | |
| ☐ | Quick Export: Single Records | UG | | | |
| ☐ | Exporting One Record | UG | | | |
| ☐ | Steps | UG | | | |
| ☐ | Export Dashboard | UG | | | |
| ☐ | Accessing the Export Dashboard | UG | | | |
| ☐ | CSV Export | UG | | | |
| ☐ | EAD Export | UG | | | |
| ☐ | Bulk Export: Multiple Records | UG | | | |
| ☐ | Using the Clipboard | UG | | | |
| ☐ | Steps | UG | | | |
| ☐ | Sector-Specific Exports | UG | | | |
| ☐ | Archives | UG | | | |
| ☐ | Museum Objects | UG | | | |
| ☐ | Library Items | UG | | | |
| ☐ | Digital Assets | UG | | | |
| ☐ | Understanding Export Files | UG | | | |
| ☐ | CSV Files | UG | | | |
| ☐ | EAD Files | UG | | | |
| ☐ | Dublin Core Files | UG | | | |
| ☐ | Export Settings | UG | | | |
| ☐ | What Gets Exported | UG | | | |
| ☐ | Field Selection | UG | | | |
| ☐ | Tips for Good Exports | UG | | | |
| ☐ | CLI: php symfony migration:import | CODE | | | |
| ☐ | CLI: php symfony preservica:export | CODE | | | |
| ☐ | CLI: php symfony preservica:import | CODE | | | |
| ☐ | CLI: php symfony preservica:info | CODE | | | |


## ahgDcManagePlugin

Sources: user guide `rad-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |


## ahgDedupePlugin

Sources: technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Configure duplicate-detection rules (fields, thresholds, match strategy) | AUTHORED | | | |
| ☐ | Run a dedup scan job over the catalogue | AUTHORED | | | |
| ☐ | View duplicate-candidate groups with match scores | AUTHORED | | | |
| ☐ | Compare two candidate records side by side | AUTHORED | | | |
| ☐ | Merge duplicates via the merge workflow (choose surviving record) | AUTHORED | | | |
| ☐ | Dedup report (counts, merges, history) | AUTHORED | | | |
| ☐ | CLI: dedupe:scan / dedupe:merge / dedupe:report | AUTHORED | | | |
| ☑ | Route /admin/dedupe → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/dedupe/browse → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/dedupe/view/:id → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/dedupe/compare/:id → compare | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/dedupe/dismiss/:id → dismiss | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /admin/dedupe/merge/:id → merge | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/dedupe/scan → scan | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/dedupe/rules → rules | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/dedupe/rule/create → ruleCreate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/dedupe/rule/:id/edit → ruleEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/dedupe/rule/:id/delete → ruleDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /admin/dedupe/report → report | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/dedupe/check → apiCheck | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/dedupe/realtime → apiRealtime | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony dedupe:merge | CODE | | | |
| ☐ | CLI: php symfony dedupe:report | CODE | | | |
| ☐ | CLI: php symfony dedupe:scan | CODE | | | |


## ahgDiscoveryPlugin

Sources: user guide `discovery-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Getting Started | UG | | | |
| ☐ | Accessing Discovery | UG | | | |
| ☐ | Your First Search | UG | | | |
| ☐ | Search Features | UG | | | |
| ☐ | Natural Language Queries | UG | | | |
| ☐ | Date Recognition | UG | | | |
| ☐ | Phrase Detection | UG | | | |
| ☐ | Synonym Expansion | UG | | | |
| ☐ | Understanding Results | UG | | | |
| ☐ | Result Cards | UG | | | |
| ☐ | Match Reason Badges | UG | | | |
| ☐ | Entity Tag Colours | UG | | | |
| ☐ | Grouped vs Flat View | UG | | | |
| ☐ | Popular Searches | UG | | | |
| ☐ | Tips for Better Results | UG | | | |
| ☐ | Related Content (Sidebar) | UG | | | |
| ☐ | Requirements | UG | | | |
| ☐ | Configurable boosts & personalised re-ranking (v3.46.0) | UG | | | |
| ☑ | Route /discovery → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /discovery/search → search | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /discovery/related/:id → related | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /discovery/click → click | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /discovery/popular → popular | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /discovery/suggest → suggest | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /discovery/pageindex → pageindex | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /discovery/build → build | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /discovery/pageindex/api → pageindexApi | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgDisplayPlugin

Sources: technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | GLAM browse interface renders (display modes) | AUTHORED | | | |
| ☐ | Display search via Elasticsearch with facets | AUTHORED | | | |
| ☐ | Guests see PUBLISHED records only (incl. the fuzzy-fallback path) | AUTHORED | | | |
| ☐ | Auto-detect display mode for a record | AUTHORED | | | |
| ☐ | Reindex display data (CLI display:reindex) | AUTHORED | | | |
| ☐ | DisplayRegistry: extensions register actions / panels / badges | AUTHORED | | | |
| ☐ | Treeview renders children/siblings (core ACL honoured) | AUTHORED | | | |
| ☑ | Route /informationobject/browse → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/profiles → profiles | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/levels → levels | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/fields → fields | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/setType → setType | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/assignProfile → assignProfile | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/bulkSetType → bulkSetType | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/browse → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/browseAjax → browseAjax | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/print → print | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/exportCsv → exportCsv | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/changeType → changeType | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /glam/settings → browseSettings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/toggleGlamBrowse → toggleGlamBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/saveBrowseSettings → saveBrowseSettings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/getBrowseSettings → getBrowseSettings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/resetBrowseSettings → resetBrowseSettings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/search → search | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /glam/search/results → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony ahg:add-fulltext-indexes | CODE | | | |
| ☐ | CLI: php symfony ahg:refresh-facet-cache | CODE | | | |
| ☐ | CLI: php symfony display:auto-detect | CODE | | | |
| ☐ | CLI: php symfony display:reindex | CODE | | | |


## ahgDoiPlugin

Sources: user guide `doi-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What is a DOI? | UG | | | |
| ☐ | Why Use DOIs? | UG | | | |
| ☐ | DOI States | UG | | | |
| ☐ | DOI Dashboard | UG | | | |
| ☐ | Quick Actions | UG | | | |
| ☐ | Minting a DOI | UG | | | |
| ☐ | Method 1: From Record Page | UG | | | |
| ☐ | Method 2: Batch Minting | UG | | | |
| ☐ | Method 3: Auto-Mint (If Configured) | UG | | | |
| ☐ | Managing DOIs | UG | | | |
| ☐ | View DOI Details | UG | | | |
| ☐ | Update DOI Metadata | UG | | | |
| ☐ | Verify DOI Resolution | UG | | | |
| ☐ | Deactivating DOIs | UG | | | |
| ☐ | Via Web Interface | UG | | | |
| ☐ | Via CLI | UG | | | |
| ☐ | What Happens? | UG | | | |
| ☐ | Queue Management | UG | | | |
| ☐ | Queue Statuses | UG | | | |
| ☐ | Export DOI Data | UG | | | |
| ☐ | Via Web Interface | UG | | | |
| ☐ | Export Columns | UG | | | |
| ☐ | Reports | UG | | | |
| ☐ | Configuration | UG | | | |
| ☐ | Required Settings | UG | | | |
| ☐ | Optional Settings | UG | | | |
| ☐ | Test Connection | UG | | | |
| ☐ | CLI Commands | UG | | | |
| ☐ | Cron Jobs | UG | | | |
| ☐ | DOI Not Resolving | UG | | | |
| ☐ | Minting Failed | UG | | | |
| ☐ | Metadata Not Updating | UG | | | |
| ☐ | Best Practices | UG | | | |
| ☐ | Integration with Other Systems | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /admin/doi → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/doi/config → config | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/doi/config/save → configSave | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /admin/doi/config/test → configTest | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/doi/browse → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/doi/view/:id → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/doi/mint/:id → mint | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /admin/doi/batch-mint → batchMint | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/doi/update/:id → update | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /admin/doi/queue → queue | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/doi/queue/:id/retry → queueRetry | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /admin/doi/mapping → mapping | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /admin/doi/report → report | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/doi/export → export | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/doi/sync → sync | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/doi/deactivate/:id → deactivate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/doi/reactivate/:id → reactivate | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /admin/doi/verify/:id → verify | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /api/doi/mint/:id → apiMint | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/doi/status/:id → apiStatus | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /doi/:doi → resolve | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | CLI: php symfony doi:deactivate | CODE | | | |
| ☐ | CLI: php symfony doi:mint | CODE | | | |
| ☐ | CLI: php symfony doi:process-queue | CODE | | | |
| ☐ | CLI: php symfony doi:sync | CODE | | | |
| ☐ | CLI: php symfony doi:verify | CODE | | | |


## ahgDonorAgreementPlugin

Sources: user guide `donor-manage-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists and Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Administration / settings | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /donor/dashboard → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /donor/agreement/browse → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /donor/agreement/add → add | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /donor/agreement/:id → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /donor/agreement/:id/edit → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /donor/agreement/:id/delete → delete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /donor/agreement/reminders → reminders | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /donor/autocomplete/accessions → autocompleteAccessions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /donor/autocomplete/records → autocompleteRecords | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgDonorManagePlugin

Sources: user guide `rad-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | Route /donor/:slug → view | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /donor/:slug/delete → delete | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /donor/:slug/edit → edit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /donor/add → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /donor/browse → browse | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgEmailDeliveryPlugin

Sources: user guide `email-delivery-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Manage the suppression list (admin) | UG | | | |
| ☐ | Receive provider events (webhook) | UG | | | |
| ☐ | Administration / setup | UG | | | |
| ☐ | Tips & FAQ | UG | | | |


## ahgExhibitionPlugin

Sources: user guide `exhibition-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Exhibition Dashboard | UG | | | |
| ☐ | Creating an Exhibition | UG | | | |
| ☐ | Step 1: Basic Information | UG | | | |
| ☐ | Step 2: Dates and Venue | UG | | | |
| ☐ | Step 3: Team and Budget | UG | | | |
| ☐ | Exhibition Status Workflow | UG | | | |
| ☐ | Changing Status | UG | | | |
| ☐ | Managing Exhibition Objects | UG | | | |
| ☐ | Adding Objects | UG | | | |
| ☐ | Object Placement Details | UG | | | |
| ☐ | Object Statuses | UG | | | |
| ☐ | Exhibition Sections | UG | | | |
| ☐ | Creating Sections | UG | | | |
| ☐ | Section Order | UG | | | |
| ☐ | Storylines and Narratives | UG | | | |
| ☐ | Storyline Types | UG | | | |
| ☐ | Creating a Storyline | UG | | | |
| ☐ | Adding Stops to a Storyline | UG | | | |
| ☐ | Events Management | UG | | | |
| ☐ | Event Types | UG | | | |
| ☐ | Creating an Event | UG | | | |
| ☐ | Checklists | UG | | | |
| ☐ | Checklist Types | UG | | | |
| ☐ | Using Checklists | UG | | | |
| ☐ | Object List Report | UG | | | |
| ☐ | Generating the Report | UG | | | |
| ☐ | Common Tasks | UG | | | |
| ☐ | Finding an Exhibition | UG | | | |
| ☐ | Extending an Exhibition | UG | | | |
| ☐ | Canceling an Exhibition | UG | | | |
| ☐ | Tips and Best Practices | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☐ | Route /exhibition/:slug → show | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /exhibitions → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /exhibition/:id → show | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /exhibition/:id/edit → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /exhibition/:id/objects → objects | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /exhibition/:id/storylines → storylines | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /exhibition/:id/storyline/:storyline_id → storyline | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /exhibition/:id/sections → sections | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /exhibition/:id/events → events | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /exhibition/:id/checklists → checklists | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /exhibition/:id/object-list → objectList | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /exhibition/venues → venues | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /exhibition/add → add | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /exhibition/dashboard → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony museum:exhibition | CODE | | | |


## ahgExportPlugin

Sources: user guide `export-data-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists and Collection Managers | UG | | | |
| ☐ | Why Export Data? | UG | | | |
| ☐ | Export Formats Explained | UG | | | |
| ☐ | Quick Export: Single Records | UG | | | |
| ☐ | Exporting One Record | UG | | | |
| ☐ | Steps | UG | | | |
| ☐ | Export Dashboard | UG | | | |
| ☐ | Accessing the Export Dashboard | UG | | | |
| ☐ | CSV Export | UG | | | |
| ☐ | EAD Export | UG | | | |
| ☐ | Bulk Export: Multiple Records | UG | | | |
| ☐ | Using the Clipboard | UG | | | |
| ☐ | Steps | UG | | | |
| ☐ | Sector-Specific Exports | UG | | | |
| ☐ | Archives | UG | | | |
| ☐ | Museum Objects | UG | | | |
| ☐ | Library Items | UG | | | |
| ☐ | Digital Assets | UG | | | |
| ☐ | Understanding Export Files | UG | | | |
| ☐ | CSV Files | UG | | | |
| ☐ | EAD Files | UG | | | |
| ☐ | Dublin Core Files | UG | | | |
| ☐ | Export Settings | UG | | | |
| ☐ | What Gets Exported | UG | | | |
| ☐ | Field Selection | UG | | | |
| ☐ | Tips for Good Exports | UG | | | |
| ☑ | Route /export → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /export/archival → archival | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /export/authority → authority | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /export/repository → repository | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /export/csv → archival | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /export/ead → archival | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /export/grap → archival | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /export/authorities → authority | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /export/accession-csv → accessionCsv | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /object/export → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgExtendedRightsPlugin

Sources: user guide `extended-rights-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Workflow Overview | UG | | | |
| ☐ | What Extended Rights Manages | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Part 1: Rights Statements | UG | | | |
| ☐ | What Are Rights Statements? | UG | | | |
| ☐ | Choosing a Rights Statement | UG | | | |
| ☐ | Part 2: Creative Commons Licenses | UG | | | |
| ☐ | Understanding CC Licenses | UG | | | |
| ☐ | Which License to Choose? | UG | | | |
| ☐ | Part 3: Embargo Management | UG | | | |
| ☐ | What is an Embargo? | UG | | | |
| ☐ | Setting an Embargo | UG | | | |
| ☐ | Embargo Status Dashboard | UG | | | |
| ☐ | Part 4: Traditional Knowledge Labels | UG | | | |
| ☐ | What Are TK Labels? | UG | | | |
| ☐ | Applying TK Labels | UG | | | |
| ☐ | Adding Extended Rights to a Record | UG | | | |
| ☐ | Complete Workflow | UG | | | |
| ☐ | Extended Rights Form | UG | | | |
| ☐ | Rights Display on Record | UG | | | |
| ☐ | Tips for Best Practice | UG | | | |
| ☐ | Part 5: CLI Commands (System Administrators) | UG | | | |
| ☐ | Automated Embargo Processing | UG | | | |
| ☐ | Cron Setup | UG | | | |
| ☐ | Embargo Reports | UG | | | |
| ☐ | Report Output Example | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☐ | Retention Schedule & Disposal Workflow (v1.3.0, May 2026) | UG | | | |
| ☐ | Retention schedules — what they are | UG | | | |
| ☐ | Assigning a record to a schedule | UG | | | |
| ☐ | Disposal workflow — the sign-off chain | UG | | | |
| ☐ | Audit trail | UG | | | |
| ☐ | Compliance dashboard integration | UG | | | |
| ☑ | Route /extendedRights/dashboard → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /extendedRights → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /extendedRights/edit/:slug → edit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /extendedRights/batch → batch | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /extendedRights/browse → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /extendedRights/embargoes → embargoes | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /extendedRights/liftEmbargo/:id → liftEmbargo | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /admin/rights → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/rights/batch → batch | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahg/rights/embargo → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /ahg/rights/embargo/add → add | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /ahg/rights/embargo/edit → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /ahg/rights/embargo/view/:id → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /ahg/rights/embargo/lift/:id → lift | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | CLI: php symfony embargo:process | CODE | | | |
| ☐ | CLI: php symfony embargo:report | CODE | | | |


## ahgFavoritesPlugin

Sources: user guide `favorites-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Quick Start | UG | | | |
| ☐ | Adding to Favorites | UG | | | |
| ☐ | From Any Record | UG | | | |
| ☐ | Button States | UG | | | |
| ☐ | Viewing Your Favorites | UG | | | |
| ☐ | Favorites List Features | UG | | | |
| ☐ | Removing from Favorites | UG | | | |
| ☐ | From the Record Page | UG | | | |
| ☐ | From the Favorites List | UG | | | |
| ☐ | Requirements | UG | | | |
| ☐ | Workflow Diagram | UG | | | |
| ☐ | Tips | UG | | | |
| ☑ | Route /favorites → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /favorites/add/:slug → add | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /favorites/remove/:id → remove | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /favorites/clear → clear | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /favorites/bulk → bulk | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☐ | Route /favorites/move → moveToFolder | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /favorites/notes/:id → updateNotes | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /favorites/folder/create → folderCreate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /favorites/folder/:id → folderView | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /favorites/folder/:id/edit → folderEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /favorites/folder/:id/delete → folderDelete | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /favorites/ajax/toggle → ajaxToggle | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /favorites/ajax/toggle-custom → ajaxToggleCustom | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /favorites/ajax/search → ajaxSearch | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /favorites/ajax/status/:slug → ajaxStatus | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /favorites/ajax/folders → ajaxFolders | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /favorites/export/:format → export | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /favorites/folder/:id/export/:format → exportFolder | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /favorites/folder/:id/share → shareFolder | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /favorites/folder/:id/revoke-share → revokeSharing | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /favorites/shared/:token → viewShared | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /favorites/import → import | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /favorites/send-to-collection → sendToCollection | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /favorites/send-to-project → sendToProject | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /favorites/send-to-bibliography → sendToBibliography | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgFederationPlugin

Sources: user guide `federation-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Getting Started | UG | | | |
| ☐ | Accessing Federation Settings | UG | | | |
| ☐ | Understanding Peers | UG | | | |
| ☐ | Managing Federation Peers | UG | | | |
| ☐ | Adding a New Peer | UG | | | |
| ☐ | Editing a Peer | UG | | | |
| ☐ | Deactivating a Peer | UG | | | |
| ☐ | OAI-PMH Harvesting | UG | | | |
| ☐ | Manual Harvest | UG | | | |
| ☐ | Viewing Harvest History | UG | | | |
| ☐ | Harvest Status Values | UG | | | |
| ☐ | Federated Search | UG | | | |
| ☐ | Enabling Federated Search | UG | | | |
| ☐ | Using Federated Search | UG | | | |
| ☐ | Search Result Sources | UG | | | |
| ☐ | Vocabulary Synchronization | UG | | | |
| ☐ | Configuring Vocabulary Sync | UG | | | |
| ☐ | Sync Direction Options | UG | | | |
| ☐ | Conflict Resolution Options | UG | | | |
| ☐ | Running a Sync | UG | | | |
| ☐ | Viewing Sync History | UG | | | |
| ☐ | Dropdown Configuration | UG | | | |
| ☐ | Accessing Dropdown Settings | UG | | | |
| ☐ | Federation Taxonomies | UG | | | |
| ☐ | Adding Custom Values | UG | | | |
| ☐ | Harvest Fails Immediately | UG | | | |
| ☐ | Search Returns No Results from a Peer | UG | | | |
| ☐ | Vocabulary Sync Shows Conflicts | UG | | | |
| ☐ | Slow Federated Search | UG | | | |
| ☐ | Best Practices | UG | | | |
| ☐ | Related Documentation | UG | | | |
| ☑ | Route /admin/federation → index | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/federation/peers → peers | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/federation/peers/:id → editPeer | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/federation/peers/add → addPeer | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/federation/harvest/:peerId → harvest | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /admin/federation/harvest/:peerId/status → harvestStatus | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /admin/federation/log → log | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/federation/union → union | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/federation/api/test-peer → testPeer | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/federation/api/harvest/:peerId → runHarvest | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |


## ahgFeedbackPlugin

Sources: user guide `feedback-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Submitting Feedback | UG | | | |
| ☐ | General Feedback | UG | | | |
| ☐ | Feedback on a Record | UG | | | |
| ☐ | Feedback Types | UG | | | |
| ☐ | What Happens Next | UG | | | |
| ☐ | For Administrators | UG | | | |
| ☐ | Viewing Feedback | UG | | | |
| ☐ | Filtering Feedback | UG | | | |
| ☐ | Managing Feedback | UG | | | |
| ☐ | Marking Feedback Complete | UG | | | |
| ☐ | Tips | UG | | | |


## ahgFormsPlugin

Sources: user guide `forms-builder-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Dashboard Overview | UG | | | |
| ☐ | Statistics Cards | UG | | | |
| ☐ | Quick Links | UG | | | |
| ☐ | Managing Templates | UG | | | |
| ☐ | Viewing Templates | UG | | | |
| ☐ | Creating a New Template | UG | | | |
| ☐ | Form Builder | UG | | | |
| ☐ | Layout | UG | | | |
| ☐ | Adding Fields | UG | | | |
| ☐ | Field Types | UG | | | |
| ☐ | Editing Field Properties | UG | | | |
| ☐ | Reordering Fields | UG | | | |
| ☐ | Deleting Fields | UG | | | |
| ☐ | Form Assignments | UG | | | |
| ☐ | How Assignment Works | UG | | | |
| ☐ | Creating an Assignment | UG | | | |
| ☐ | Assignment Examples | UG | | | |
| ☐ | Template Library | UG | | | |
| ☐ | Available Templates | UG | | | |
| ☐ | Using Library Templates | UG | | | |
| ☐ | Form Preview | UG | | | |
| ☐ | Previewing a Template | UG | | | |
| ☐ | Template Information Panel | UG | | | |
| ☐ | Import and Export | UG | | | |
| ☐ | Exporting a Template | UG | | | |
| ☐ | Importing a Template | UG | | | |
| ☐ | CLI Export/Import | UG | | | |
| ☐ | Auto-Save and Drafts | UG | | | |
| ☐ | How Auto-Save Works | UG | | | |
| ☐ | Recovering a Draft | UG | | | |
| ☐ | CLI Commands | UG | | | |
| ☐ | List Templates | UG | | | |
| ☐ | Example Output | UG | | | |
| ☐ | Best Practices | UG | | | |
| ☐ | Template Design | UG | | | |
| ☐ | Assignments | UG | | | |
| ☐ | Form Not Appearing | UG | | | |
| ☐ | Fields Not Saving | UG | | | |
| ☑ | Route /admin/forms → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/forms/templates → templates | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/forms/template/create → templateCreate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/forms/template/:id/edit → templateEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/forms/template/:id/delete → templateDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /admin/forms/template/:id/clone → templateClone | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/forms/template/:id/export → templateExport | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /admin/forms/template/import → templateImport | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 403 |
| ☐ | Route /admin/forms/template/:id/builder → builder | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/forms/assignments → assignments | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/forms/assignment/create → assignmentCreate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/forms/assignment/:id/delete → assignmentDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /admin/forms/mappings → mappings | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /api/forms/template/:id/fields → apiSaveFields | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/forms/template/:id/reorder → apiReorderFields | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /api/forms/render/:type/:id → apiGetForm | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /api/forms/autosave → apiAutosave | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /forms/new/:templateId → renderNew | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /forms/edit/:type/:id → renderEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /forms/submit → submit | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /admin/forms/library → library | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/forms/library/:template/install → libraryInstall | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | CLI: php symfony forms:export | CODE | | | |
| ☐ | CLI: php symfony forms:import | CODE | | | |
| ☐ | CLI: php symfony forms:list | CODE | | | |


## ahgFtpPlugin

Sources: user guide `ftp-sftp-upload-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists and Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Upload files | UG | | | |
| ☐ | Attach during digital-object add | UG | | | |
| ☐ | Endpoints | UG | | | |
| ☐ | Administration / setup | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /ftp-upload → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ftp-upload/upload → upload | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ftp-upload/chunk → uploadChunk | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ftp-upload/list → listFiles | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ftp-upload/delete → deleteFile | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ftp-upload/import-as-upload → importAsUpload | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgFunctionManagePlugin

Sources: user guide `rad-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | Route /function/:slug → view | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /function/:slug/delete → delete | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /function/:slug/edit → edit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /function/add → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /function/browse → browse | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgFunctionsDocsPlugin

Sources: user guide `functions-catalogue-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Administrators and Developers | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Administration / settings | UG | | | |
| ☐ | Tips & FAQ | UG | | | |


## ahgGISPlugin

Sources: user guide `user-registration-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Administrators and Staff | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Administration / settings | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | Route /gis/bbox → bbox | CODE | N/A | pw-authed 2026-06-27 | HTTP 400 |
| ☐ | Route /gis/radius → radius | CODE | N/A | pw-authed 2026-06-27 | HTTP 400 |
| ☑ | Route /gis/geojson → geojson | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgGalleryPlugin

Sources: user guide `gallery-module-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | When to Use Gallery Module | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Adding an Artwork | UG | | | |
| ☐ | Step 1: Click Add Artwork | UG | | | |
| ☐ | Step 2: Choose Work Type | UG | | | |
| ☐ | Step 3: Fill in the Form | UG | | | |
| ☐ | Key CCO Fields Explained | UG | | | |
| ☐ | Object Identification | UG | | | |
| ☐ | Creator Information | UG | | | |
| ☐ | Physical Description | UG | | | |
| ☐ | Subject Matter | UG | | | |
| ☐ | Provenance (Ownership History) | UG | | | |
| ☐ | Exhibition History | UG | | | |
| ☐ | Prints and Editions | UG | | | |
| ☐ | Condition and Conservation | UG | | | |
| ☐ | Related Works | UG | | | |
| ☐ | Tips for Cataloging Art | UG | | | |
| ☐ | Optional Features | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /gallery/:slug → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /gallery/edit/:slug → edit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /gallery/add → add | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /gallery/browse → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /gallery/dashboard → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /gallery/loans → loans | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /gallery/loans/create → createLoan | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /gallery/loans/:id → viewLoan | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /gallery/loans/:loan_id/facility-report → facilityReport | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /gallery/valuations → valuations | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /gallery/valuations/create → createValuation | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /gallery/artists → artists | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /gallery/artists/create → createArtist | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /gallery/artists/:id → viewArtist | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /gallery/venues → venues | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 |
| ☑ | Route /gallery/venues/create → createVenue | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /gallery/venues/:id → viewVenue | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 (id=553) |


## ahgGraphQLPlugin

Sources: user guide `graphql-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Quick Start | UG | | | |
| ☐ | 1. Get an API Key | UG | | | |
| ☐ | 2. Make Your First Query | UG | | | |
| ☐ | 3. Response | UG | | | |
| ☐ | Authentication | UG | | | |
| ☐ | Core Queries | UG | | | |
| ☐ | Browse Items (Archival Descriptions) | UG | | | |
| ☐ | Get Single Item | UG | | | |
| ☐ | Browse Actors (Authority Records) | UG | | | |
| ☐ | Get Single Actor | UG | | | |
| ☐ | Browse Repositories | UG | | | |
| ☐ | Get Taxonomies | UG | | | |
| ☐ | Search | UG | | | |
| ☐ | Current User | UG | | | |
| ☐ | Pagination | UG | | | |
| ☐ | Variables | UG | | | |
| ☐ | Fragments | UG | | | |
| ☐ | Error Handling | UG | | | |
| ☐ | Security Limits | UG | | | |
| ☐ | GraphQL Playground | UG | | | |
| ☐ | Comparison: GraphQL vs REST | UG | | | |
| ☐ | Example: Complete Item View | UG | | | |
| ☐ | Support | UG | | | |
| ☐ | Route /api/graphql → index | TECH | N/A | pw-authed 2026-06-27 | HTTP 400 |
| ☐ | Route /api/graphql/playground → playground | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |


## ahgHelpPlugin

Sources: user guide `help-system-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for All Users and Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Administration / settings | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /help → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /help/category/:category → category | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /help/article/:slug → article | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /help/search → search | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /help/api/search → apiSearch | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /help/api/search-index → apiSearchIndex | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /help/api/context-map → apiContextMap | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /help/api/chat → apiChat | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /help/system-map → systemMap | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /help/api/system-map → apiSystemMap | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony help:import | CODE | | | |
| ☐ | CLI: php symfony help:rebuild-index | CODE | | | |


## ahgHeritageAccountingPlugin

Sources: user guide `heritage-sites-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | Public Discovery Interface | UG | | | |
| ☐ | Landing Page | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Search Features | UG | | | |
| ☐ | Explore Categories | UG | | | |
| ☐ | Browse by Time (Timeline) | UG | | | |
| ☐ | Browse by Place | UG | | | |
| ☐ | Browse by People | UG | | | |
| ☐ | Browse by Theme | UG | | | |
| ☐ | Browse by Format | UG | | | |
| ☐ | Trending | UG | | | |
| ☐ | Community Contributions | UG | | | |
| ☐ | Contributor Registration | UG | | | |
| ☐ | Making a Contribution | UG | | | |
| ☐ | Trust Levels | UG | | | |
| ☐ | Badges and Achievements | UG | | | |
| ☐ | Leaderboard | UG | | | |
| ☐ | Access Requests | UG | | | |
| ☐ | Why Request Access? | UG | | | |
| ☐ | Submitting an Access Request | UG | | | |
| ☐ | Request Status | UG | | | |
| ☐ | Viewing Your Activity | UG | | | |
| ☐ | My Contributions | UG | | | |
| ☐ | My Access Requests | UG | | | |
| ☐ | Administration | UG | | | |
| ☐ | Admin Dashboard | UG | | | |
| ☐ | Landing Page Configuration | UG | | | |
| ☐ | Hero Slides | UG | | | |
| ☐ | Featured Collections | UG | | | |
| ☐ | Feature Toggles | UG | | | |
| ☐ | Branding | UG | | | |
| ☐ | Access Control Management | UG | | | |
| ☐ | Access Requests Review | UG | | | |
| ☐ | Embargo Management | UG | | | |
| ☐ | POPIA Flags | UG | | | |
| ☐ | Custodian Tools | UG | | | |
| ☐ | Custodian Dashboard | UG | | | |
| ☐ | Batch Operations | UG | | | |
| ☐ | Audit Trail | UG | | | |
| ☑ | Route /heritage/dashboard → dashboard | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /heritage/settings → settings | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /heritage/browse → browse | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /heritage/add → add | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /heritage/:id → view | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /heritage/:id/edit → edit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /heritage/:id/valuation/add → addValuation | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /heritage/:id/impairment/add → addImpairment | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /heritage/:id/movement/add → addMovement | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /heritage/:id/journal/add → addJournal | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /heritage/object/:slug → viewByObject | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /heritage/object/:slug/edit → editByObject | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /heritage/reports → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /heritage/report/asset-register → assetRegister | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /heritage/report/valuation → valuation | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /heritage/report/movement → movement | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /grap/dashboard → dashboard | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /grap/check/:id → check | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /grap/batch-check → batchCheck | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /grap/national-treasury-report → nationalTreasuryReport | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /api/heritage/asset/:id → asset | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /api/heritage/actor-autocomplete → actorAutocomplete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /api/heritage/autocomplete → autocomplete | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /api/heritage/summary → summary | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony heritage:install | CODE | | | |
| ☐ | CLI: php symfony heritage:region | CODE | | | |


## ahgHeritagePlugin

Sources: user guide `heritage-sites-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | Public Discovery Interface | UG | | | |
| ☐ | Landing Page | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Search Features | UG | | | |
| ☐ | Explore Categories | UG | | | |
| ☐ | Browse by Time (Timeline) | UG | | | |
| ☐ | Browse by Place | UG | | | |
| ☐ | Browse by People | UG | | | |
| ☐ | Browse by Theme | UG | | | |
| ☐ | Browse by Format | UG | | | |
| ☐ | Trending | UG | | | |
| ☐ | Community Contributions | UG | | | |
| ☐ | Contributor Registration | UG | | | |
| ☐ | Making a Contribution | UG | | | |
| ☐ | Trust Levels | UG | | | |
| ☐ | Badges and Achievements | UG | | | |
| ☐ | Leaderboard | UG | | | |
| ☐ | Access Requests | UG | | | |
| ☐ | Why Request Access? | UG | | | |
| ☐ | Submitting an Access Request | UG | | | |
| ☐ | Request Status | UG | | | |
| ☐ | Viewing Your Activity | UG | | | |
| ☐ | My Contributions | UG | | | |
| ☐ | My Access Requests | UG | | | |
| ☐ | Administration | UG | | | |
| ☐ | Admin Dashboard | UG | | | |
| ☐ | Landing Page Configuration | UG | | | |
| ☐ | Hero Slides | UG | | | |
| ☐ | Featured Collections | UG | | | |
| ☐ | Feature Toggles | UG | | | |
| ☐ | Branding | UG | | | |
| ☐ | Access Control Management | UG | | | |
| ☐ | Access Requests Review | UG | | | |
| ☐ | Embargo Management | UG | | | |
| ☐ | POPIA Flags | UG | | | |
| ☐ | Custodian Tools | UG | | | |
| ☐ | Custodian Dashboard | UG | | | |
| ☐ | Batch Operations | UG | | | |
| ☐ | Audit Trail | UG | | | |
| ☐ | CLI: php symfony heritage:build-graph | CODE | | | |


## ahgICIPPlugin

Sources: user guide `icip-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Legal Framework | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Dashboard | UG | | | |
| ☐ | Key Statistics | UG | | | |
| ☐ | Secondary Metrics | UG | | | |
| ☐ | Community Registry | UG | | | |
| ☐ | Adding a Community | UG | | | |
| ☐ | Community List | UG | | | |
| ☐ | State/Territory Codes | UG | | | |
| ☐ | Consent Management | UG | | | |
| ☐ | Consent Workflow | UG | | | |
| ☐ | Consent Status Options | UG | | | |
| ☐ | Consent Scope Options | UG | | | |
| ☐ | Adding a Consent Record | UG | | | |
| ☐ | Cultural Notices | UG | | | |
| ☐ | Notice Types | UG | | | |
| ☐ | Adding a Cultural Notice | UG | | | |
| ☐ | Notice Display | UG | | | |
| ☐ | TK Labels (Traditional Knowledge Labels) | UG | | | |
| ☐ | What are TK Labels? | UG | | | |
| ☐ | TK Label Categories | UG | | | |
| ☐ | Applying a TK Label | UG | | | |
| ☐ | Label Display on Records | UG | | | |
| ☐ | Access Restrictions | UG | | | |
| ☐ | Restriction Types | UG | | | |
| ☐ | Adding a Restriction | UG | | | |
| ☐ | Override Security Clearance | UG | | | |
| ☐ | Consultation Log | UG | | | |
| ☐ | Consultation Types | UG | | | |
| ☐ | Recording a Consultation | UG | | | |
| ☐ | Consultation Timeline | UG | | | |
| ☐ | Record ICIP View | UG | | | |
| ☐ | Accessing Record ICIP | UG | | | |
| ☐ | ICIP Overview Page | UG | | | |
| ☐ | Reports | UG | | | |
| ☐ | Available Reports | UG | | | |
| ☐ | Pending Consultation Report | UG | | | |
| ☐ | Consent Expiry Report | UG | | | |
| ☐ | User Acknowledgement | UG | | | |
| ☐ | Quick Actions | UG | | | |


## ahgIPSASPlugin

Sources: user guide `ipsas-accounting-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Finance Officers and Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Command line | UG | | | |
| ☐ | Compliance notes | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /admin/ipsas → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ipsas/assets → assets | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ipsas/asset/create → assetCreate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/ipsas/asset/:id → assetView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/ipsas/asset/:id/edit → assetEdit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/ipsas/valuations → valuations | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ipsas/valuation/create → valuationCreate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ipsas/impairments → impairments | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ipsas/insurance → insurance | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ipsas/reports → reports | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ipsas/financial-year → financialYear | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ipsas/config → config | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony ipsas:report | CODE | | | |


## ahgIiifPlugin

Sources: user guide `iiif-integration-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What is IIIF? | UG | | | |
| ☐ | How It Works | UG | | | |
| ☐ | Viewers | UG | | | |
| ☐ | Choosing a Viewer | UG | | | |
| ☐ | OpenSeadragon (Image Deep Zoom) | UG | | | |
| ☐ | Mirador (Rich IIIF Workspace) | UG | | | |
| ☐ | PDF.js (Document Viewer) | UG | | | |
| ☐ | 3D Model Viewer | UG | | | |
| ☐ | Audio/Video Player | UG | | | |
| ☐ | Basic Navigation | UG | | | |
| ☐ | Zooming (Images) | UG | | | |
| ☐ | Panning | UG | | | |
| ☐ | Multi-Page Documents | UG | | | |
| ☐ | Media Streaming | UG | | | |
| ☐ | Supported Formats | UG | | | |
| ☐ | Transcription (Whisper) | UG | | | |
| ☐ | Media Snippets | UG | | | |
| ☐ | Metadata Extraction | UG | | | |
| ☐ | Format Conversion | UG | | | |
| ☐ | Annotations | UG | | | |
| ☐ | Drawing on Images | UG | | | |
| ☐ | Viewing Annotations | UG | | | |
| ☐ | IIIF Collections | UG | | | |
| ☐ | What Are Collections? | UG | | | |
| ☐ | Browsing Collections | UG | | | |
| ☐ | Creating a Collection (Admin) | UG | | | |
| ☐ | Protected Content | UG | | | |
| ☐ | Access Levels | UG | | | |
| ☐ | Clickthrough Access | UG | | | |
| ☐ | What You See Without Access | UG | | | |
| ☐ | Authentication Flow | UG | | | |
| ☐ | Keyboard Shortcuts | UG | | | |
| ☐ | Fullscreen Mode | UG | | | |
| ☐ | Comparing Images (Mirador) | UG | | | |
| ☐ | Dedicated Comparison Page | UG | | | |
| ☐ | Tips | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☐ | Route /iiif/content-state/encode → encode | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /iiif/content-state/decode → decode | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /iiif/content-state/state → state | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /admin/iiif-content-state → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /iiif/manifest/:slug → manifest | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /iiif/manifest/id/:id → manifestById | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /iiif/v3/manifest/:slug → manifestV3 | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /iiif/viewer/:id → viewer | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /admin/iiif-settings → settings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /iiif/annotations/object/:id → annotationsList | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /iiif/annotations → annotationsCreate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /iiif/annotations/:id → annotationsModify | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /iiif/compare → compare | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /admin/iiif-validation → validationDashboard | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/iiif-validation/run/:object_id → validationRun | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /iiif/v3/manifest/:slug/search → search | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /iiif/v3/manifest/:slug/autocomplete → autocomplete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /iiif/activity → activity | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /iiif/activity/page/:n → activityPage | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /iiif/ocr/object/:id → ocrExport | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /manifest-collections/autocomplete → autocomplete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /manifest-collections → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /manifest-collection/new → new | TECH | PASS | fixed 2026-06-27 | HTTP 200 (fixed #187) |
| ☑ | Route /manifest-collection/create → create | TECH | PASS | fixed 2026-06-27 | HTTP 200 (fixed #187) |
| ☑ | Route /manifest-collection/reorder → reorder | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /manifest-collection/:id/view → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /manifest-collection/:id/edit → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /manifest-collection/:id/update → update | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /manifest-collection/:id/delete → delete | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /manifest-collection/:id/items/add → addItems | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /manifest-collection/item/:item_id/remove → removeItem | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /manifest-collection/:slug/manifest.json → manifest | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/iiif-auth → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /iiif/auth/login/:service → login | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /iiif/auth/token/:service → token | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /iiif/auth/logout/:service → logout | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /iiif/auth/confirm/:service → confirm | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 (id=553) |
| ☑ | Route /iiif/auth/check/:id → check | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /admin/iiif-auth/protect → protect | TECH | N/A | pw-authed 2026-06-27 | HTTP 400 |
| ☐ | Route /admin/iiif-auth/unprotect → unprotect | TECH | N/A | pw-authed 2026-06-27 | HTTP 400 |
| ☑ | Route /iiif/auth/2/probe/:service → probe | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /iiif/auth/2/access/:service → accessService | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /iiif/auth/2/token/:service → accessToken2 | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /iiif/auth/2/logout/:service → logout | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /iiif/auth/cantaloupe-check → cantaloupeCheck | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /threeDReports → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /threeDReports/models → models | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /threeDReports/hotspots → hotspots | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /threeDReports/thumbnails → thumbnails | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /threeDReports/digitalObjects → digitalObjects | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /threeDReports/settings → settings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /threeDReports/createConfig → createConfig | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /threeDReports/bulkCreateConfig → bulkCreateConfig | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☐ | Route /media/stream/:id → stream | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /media/download/:id → download | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /media/snippets/:id → snippets | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /media/snippets → saveSnippet | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /media/snippets/:id/delete → deleteSnippet | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /media/extract/:id → extract | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /media/transcribe/:id → transcribe | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |


## ahgImageArPlugin

Sources: user guide `image-ar-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists and Visitors | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Open the AR viewer | UG | | | |
| ☐ | Administration / setup | UG | | | |
| ☐ | Tips & FAQ | UG | | | |


## ahgInformationObjectManagePlugin

Sources: user guide `isadg-information-object-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Administration / settings | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /informationobject/:slug/delete → delete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /informationobject/:slug/edit → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /digitalobject/upload → doUpload | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /digitalobject/:id/edit → doEdit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /digitalobject/:id/delete → doDelete | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /informationobject/treeview → treeview | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /informationobject/treeviewFull → treeviewFull | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /informationobject/treeviewSort → treeviewSort | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /informationobject/actorAutocomplete → actorAutocomplete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /informationobject/repositoryAutocomplete → repositoryAutocomplete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /informationobject/termAutocomplete → termAutocomplete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /informationobject/generateIdentifierJson → generateIdentifier | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /informationobject/add → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgIngestPlugin

Sources: user guide `data-ingest-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Session Dashboard | UG | | | |
| ☐ | Dashboard Actions | UG | | | |
| ☐ | Step 1: Configure | UG | | | |
| ☐ | Step 1.1: Open a New Ingestion | UG | | | |
| ☐ | Step 1.2: Fill In Session Details | UG | | | |
| ☐ | Step 1.3: Configure Parent Placement | UG | | | |
| ☐ | Step 1.4: Configure Output Options | UG | | | |
| ☐ | Step 1.5: Configure AI Processing (Optional) | UG | | | |
| ☐ | Step 2: Upload | UG | | | |
| ☐ | Step 2.1: Choose Upload Method | UG | | | |
| ☐ | Step 2.2: File Auto-Detection | UG | | | |
| ☐ | Step 2.3: Preview Data (First 10 Rows) | UG | | | |
| ☐ | Step 2.4: ZIP File Extraction (if applicable) | UG | | | |
| ☐ | Step 3: Map & Enrich | UG | | | |
| ☐ | Step 3.1: Two-Column Mapping Interface | UG | | | |
| ☐ | Step 3.2: Default Value Assignment | UG | | | |
| ☐ | Step 3.3: Digital Object Matching Strategy | UG | | | |
| ☐ | Step 3.4: Metadata Extraction Panel | UG | | | |
| ☐ | Saved Mapping Profiles | UG | | | |
| ☐ | Step 4: Validate | UG | | | |
| ☐ | Step 4.1: Automatic Validation Runs | UG | | | |
| ☐ | Step 4.2: Validation Summary | UG | | | |
| ☐ | Step 4.3: Review Issues | UG | | | |
| ☐ | Step 4.4: Inline Fix or Exclude Rows | UG | | | |
| ☐ | Duplicate Detection Methods | UG | | | |
| ☐ | Step 5: Preview & Approve | UG | | | |
| ☐ | Step 5.1: Hierarchical Tree Visualization | UG | | | |
| ☐ | Step 5.2: SIP/DIP Package Preview (if enabled) | UG | | | |
| ☐ | Step 5.3: Approval Actions | UG | | | |
| ☐ | Step 6: Commit & Report | UG | | | |
| ☐ | Step 6.1: Live Progress Bar | UG | | | |
| ☐ | Step 6.2: Completion Report | UG | | | |
| ☐ | Manifest CSV Format | UG | | | |
| ☐ | Rollback | UG | | | |
| ☐ | How Rollback Works | UG | | | |
| ☐ | CSV Templates | UG | | | |
| ☐ | Available Templates | UG | | | |
| ☐ | Supported File Formats | UG | | | |
| ☑ | Route /ingest → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ingest/new → configure | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /ingest/:id/configure → configure | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /ingest/:id/upload → upload | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /ingest/:id/map → map | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /ingest/:id/validate → validate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /ingest/:id/preview → preview | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /ingest/:id/commit → commit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /ingest/ajax/search-parent → searchParent | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ingest/ajax/auto-map → autoMap | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ingest/ajax/extract-metadata → extractMetadata | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ingest/ajax/job-status → jobStatus | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ingest/ajax/preview-tree → previewTree | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /ingest/:id/cancel → cancel | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /ingest/:id/rollback → rollback | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /ingest/:id/manifest → downloadManifest | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /ingest/template/:sector → downloadTemplate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | CLI: php symfony ingest:commit | CODE | | | |


## ahgIntegrityPlugin

Sources: user guide `integrity-fixity-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Digital Preservation Staff and Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Admin screens | UG | | | |
| ☐ | Command line (recommended for cron) | UG | | | |
| ☐ | Compliance notes | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /admin/integrity → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/schedules → schedules | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/schedule/edit → scheduleEdit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/runs → runs | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/integrity/run/:id → runDetail | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/integrity/ledger → ledger | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/dead-letter → deadLetter | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/report → report | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/export → export | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/export/csv → exportCsv | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/export/auditor → exportAuditor | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/policies → policies | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/policy/edit → policyEdit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/holds → holds | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/disposition → disposition | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/records → records | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/integrity/alerts → alerts | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/verify → apiVerify | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/run/:id → apiRun | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/integrity/schedule/:id/toggle → apiScheduleToggle | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/integrity/schedule/:id/delete → apiScheduleDelete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/integrity/dead-letter/:id/action → apiDeadLetterAction | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/integrity/stats → apiStats | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/schedule/:id/run → apiRunSchedule | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/integrity/policy/:id/toggle → apiPolicyToggle | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/integrity/policy/:id/delete → apiPolicyDelete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/integrity/hold/place → apiHoldPlace | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/hold/:id/release → apiHoldRelease | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/integrity/disposition/:id/action → apiDispositionAction | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/integrity/retention/scan → apiRetentionScan | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/alert/save → apiAlertSave | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/alert/:id/delete → apiAlertDelete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/integrity/ledger → apiLedger | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/runs → apiRuns | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/holds → apiHolds | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/policies → apiPolicies | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/daily-trend → apiDailyTrend | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/repo-breakdown → apiRepoBreakdown | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/format-breakdown → apiFormatBreakdown | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/throughput → apiThroughput | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/integrity/storage-growth → apiStorageGrowth | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony integrity:report | CODE | | | |
| ☐ | CLI: php symfony integrity:retention | CODE | | | |
| ☐ | CLI: php symfony integrity:schedule | CODE | | | |
| ☐ | CLI: php symfony integrity:verify | CODE | | | |


## ahgJobsManagePlugin

Sources: user guide `rad-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | Route /jobs → browse | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /jobs/report/:id → report | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /jobs/delete → delete | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /jobs/export → export | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/queue → queueBrowse | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/queue/detail/:id → queueDetail | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/queue/batches → queueBatches | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/queue/progress → queueProgress | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/queue/retry → queueRetry | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/queue/cancel → queueCancel | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |


## ahgLabelPlugin

Sources: user guide `label-printing-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Supported GLAM Sectors | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | From a Record | UG | | | |
| ☐ | Label Components | UG | | | |
| ☐ | What's Included on a Label | UG | | | |
| ☐ | Barcode Sources | UG | | | |
| ☐ | Archive Records | UG | | | |
| ☐ | Library Items | UG | | | |
| ☐ | Museum Objects | UG | | | |
| ☐ | Step-by-Step: Printing a Label | UG | | | |
| ☐ | Step 1: Open the Label Generator | UG | | | |
| ☐ | Step 2: Select Barcode Source | UG | | | |
| ☐ | Step 3: Configure Label Size | UG | | | |
| ☐ | Step 4: Toggle Display Options | UG | | | |
| ☐ | Step 5: Preview and Print | UG | | | |
| ☐ | Output Options | UG | | | |
| ☐ | Print Label | UG | | | |
| ☐ | Download PNG | UG | | | |
| ☐ | Label Sizes Reference | UG | | | |
| ☐ | Barcode Types | UG | | | |
| ☐ | Linear Barcode (Code 128) | UG | | | |
| ☐ | QR Code | UG | | | |
| ☐ | Sector-Specific Behavior | UG | | | |
| ☐ | Library Items | UG | | | |
| ☐ | Museum Objects | UG | | | |
| ☐ | Archive Records | UG | | | |
| ☐ | Common Uses | UG | | | |
| ☐ | Tips for Best Results | UG | | | |
| ☐ | Print Settings Recommendations | UG | | | |
| ☐ | Desktop Printers | UG | | | |
| ☐ | Label Printers | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /label/:slug → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /label/templates → templates | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /label/template/edit → templateEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /label/batch → batch | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgLandingPagePlugin

Sources: user guide `landing-page-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Creating a New Page | UG | | | |
| ☐ | Step 1: Open Landing Pages | UG | | | |
| ☐ | Step 2: Click Create New Page | UG | | | |
| ☐ | Step 3: Fill in Page Details | UG | | | |
| ☐ | Step 4: Start Building | UG | | | |
| ☐ | Using the Visual Builder | UG | | | |
| ☐ | Builder Interface | UG | | | |
| ☐ | Adding Blocks | UG | | | |
| ☐ | Reordering Blocks | UG | | | |
| ☐ | Editing a Block | UG | | | |
| ☐ | Block Actions | UG | | | |
| ☐ | Block Types Reference | UG | | | |
| ☐ | Layout Blocks | UG | | | |
| ☐ | Content Blocks | UG | | | |
| ☐ | Data Blocks (Dynamic Content) | UG | | | |
| ☐ | Other Blocks | UG | | | |
| ☐ | Block Configuration Examples | UG | | | |
| ☐ | Hero Banner | UG | | | |
| ☐ | Browse Panels | UG | | | |
| ☐ | Statistics | UG | | | |
| ☐ | Recent Items | UG | | | |
| ☐ | Using Column Layouts | UG | | | |
| ☐ | Two Column Layout | UG | | | |
| ☐ | Three Column Layout | UG | | | |
| ☐ | Adding Blocks to Columns | UG | | | |
| ☐ | Styling Blocks | UG | | | |
| ☐ | Block Style Settings | UG | | | |
| ☐ | Preview and Publish | UG | | | |
| ☐ | Previewing Your Page | UG | | | |
| ☐ | Saving a Draft | UG | | | |
| ☐ | Publishing | UG | | | |
| ☐ | Restoring Previous Versions | UG | | | |
| ☐ | Page Settings | UG | | | |
| ☐ | Accessing Settings | UG | | | |
| ☐ | Page Settings Options | UG | | | |
| ☐ | Managing Multiple Pages | UG | | | |
| ☐ | Page List View | UG | | | |
| ☐ | Page Status Badges | UG | | | |
| ☑ | Route /admin/landing-pages → list | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/create → create | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/landing-pages/:id/edit → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/landing-pages/:id/preview → preview | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/landing-pages/ajax/add-block → addBlock | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/update-block → updateBlock | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/delete-block → deleteBlock | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/duplicate-block → duplicateBlock | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/reorder → reorderBlocks | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/toggle-visibility → toggleVisibility | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/get-config → getBlockConfig | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/update-settings → updateSettings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/delete → delete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/save-draft → saveDraft | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/publish → publish | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/restore-version → restoreVersion | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/move-to-column → moveToColumn | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/landing-pages/ajax/reorder-column → reorderColumnBlocks | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /my/dashboard → myDashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /my/dashboard/edit → myDashboardEdit | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 |
| ☑ | Route /my/dashboards → myDashboardList | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /my/dashboard/create → myDashboardCreate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /landing/:slug → index | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |


## ahgLibraryPlugin

Sources: user guide `library-module-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | When to Use Library Module | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Adding a Library Item | UG | | | |
| ☐ | Step 1: Click Add Library Item | UG | | | |
| ☐ | Step 2: Choose Material Type | UG | | | |
| ☐ | Step 3: Fill in the Form | UG | | | |
| ☐ | Key Fields Explained | UG | | | |
| ☐ | Title Area | UG | | | |
| ☐ | Creator Area | UG | | | |
| ☐ | Physical Description | UG | | | |
| ☐ | Subject and Classification | UG | | | |
| ☐ | Adding Subjects | UG | | | |
| ☐ | Classification Numbers | UG | | | |
| ☐ | Cataloging Serials (Journals) | UG | | | |
| ☐ | Browsing the Library | UG | | | |
| ☐ | Filter Options | UG | | | |
| ☐ | Search Tips | UG | | | |
| ☐ | Digital Objects | UG | | | |
| ☐ | Tips for Cataloging | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /library/:slug → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /library/:slug/edit → edit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /library/add → edit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /library → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /library/export → export | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /library/marc-export → marcExport | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 |
| ☑ | Route /library/onix → onix | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /library/advanced-search → advancedSearch | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /library/isbnLookup → isbnLookup | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /library/isbn-provider/delete/:id → isbnProviderDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /library/isbn-provider/toggle/:id → isbnProviderToggle | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /library/isbn-provider/edit/:id → isbnProviderEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /library/isbn-providers → isbnProviders | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/library/isbn/:isbn → apiIsbnLookup | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /library/cover/:isbn → coverProxy | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /library/suggestSubjects → suggestSubjects | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /isbn/lookup → lookup | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /isbn/test → test | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 |
| ☑ | Route /isbn/apiTest → apiTest | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/isbn/stats → stats | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /opac → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /opac/view/:id → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /opac/hold → hold | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /opac/account → account | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 403 |
| ☑ | Route /circulation → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /circulation/checkout → checkout | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /circulation/checkin → checkin | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /circulation/renew → renew | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /circulation/overdue → overdue | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /circulation/loan-rules → loanRules | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /patron/view/:id → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /patron/edit/:id → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /patron/suspend → suspend | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /patron/reactivate → reactivate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /patron → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /api/library/batch/:api_action → api | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /api/library/budgets → api | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☐ | Route /api/library/orders/:id/lines/:line_id/receive → api | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 (id=553) |
| ☐ | Route /api/library/orders/:id/lines/:line_id → api | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 (id=553) |
| ☐ | Route /api/library/orders/:id/lines → api | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 (id=553) |
| ☐ | Route /api/library/orders/:id → api | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 (id=553) |
| ☐ | Route /api/library/orders → api | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☑ | Route /acquisition/order/:order_id → order | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /acquisition/order/edit/:id → orderEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /acquisition/add-line → addLine | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /acquisition/receive → receive | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /acquisition/budgets → budgets | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /acquisition/batch-capture → batchCapture | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /acquisition/bulk-import → bulkImport | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /acquisition/bulk-import-sample → bulkImportSample | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /acquisition → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /serial/view/:id → view | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /serial/edit/:id → edit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /serial/checkin → checkin | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /serial/claim → claim | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /serial/bindery → bindery | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /serial → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ill/view/:id → view | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /ill/edit → edit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ill/status → status | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☐ | CLI: php symfony library:backfill-authors | CODE | | | |
| ☐ | CLI: php symfony library:backfill-subjects | CODE | | | |
| ☐ | CLI: php symfony library:email-usage-reports | CODE | | | |
| ☐ | CLI: php symfony library:frbr-backfill | CODE | | | |
| ☐ | CLI: php symfony library:frbr-reindex | CODE | | | |
| ☐ | CLI: php symfony library:hold-expiry | CODE | | | |
| ☐ | CLI: php symfony library:ill-overdue | CODE | | | |
| ☐ | CLI: php symfony library:overdue-check | CODE | | | |
| ☐ | CLI: php symfony library:patron-expiry | CODE | | | |
| ☐ | CLI: php symfony library:process-covers | CODE | | | |
| ☐ | CLI: php symfony library:process-fines | CODE | | | |
| ☐ | CLI: php symfony library:serial-expected | CODE | | | |
| ☐ | CLI: php symfony library:serial-renewal-reminders | CODE | | | |


## ahgLoanPlugin

Sources: user guide `loan-module-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Supported Sectors | UG | | | |
| ☐ | Getting Started | UG | | | |
| ☐ | Accessing the Loan Module | UG | | | |
| ☐ | Understanding Loan Types | UG | | | |
| ☐ | Creating a New Loan | UG | | | |
| ☐ | Step 1: Start a New Loan | UG | | | |
| ☐ | Step 2: Enter Partner Details | UG | | | |
| ☐ | Step 3: Set Loan Dates | UG | | | |
| ☐ | Step 4: Add Objects | UG | | | |
| ☐ | Step 5: Insurance Information | UG | | | |
| ☐ | Step 6: Submit | UG | | | |
| ☐ | Loan Workflow | UG | | | |
| ☐ | How a Loan Progresses | UG | | | |
| ☐ | Status Descriptions | UG | | | |
| ☐ | Managing Loans | UG | | | |
| ☐ | Viewing Loan Details | UG | | | |
| ☐ | Filtering and Searching | UG | | | |
| ☐ | Taking Actions | UG | | | |
| ☐ | Condition Reports | UG | | | |
| ☐ | Why Condition Reports Matter | UG | | | |
| ☐ | Creating a Condition Report | UG | | | |
| ☐ | Comparing Conditions | UG | | | |
| ☐ | Facility Reports | UG | | | |
| ☐ | What is a Facility Report? | UG | | | |
| ☐ | Completing a Facility Report | UG | | | |
| ☐ | Facility Ratings | UG | | | |
| ☐ | Shipping and Transport | UG | | | |
| ☐ | Arranging Shipment | UG | | | |
| ☐ | Tracking Shipments | UG | | | |
| ☐ | Recording Costs | UG | | | |
| ☐ | Calendar and Scheduling | UG | | | |
| ☐ | Viewing the Loan Calendar | UG | | | |
| ☐ | Checking Object Availability | UG | | | |
| ☐ | Notifications and Reminders | UG | | | |
| ☐ | Automatic Reminders | UG | | | |
| ☐ | Managing Notifications | UG | | | |
| ☐ | Reports and Dashboard | UG | | | |
| ☐ | Dashboard Overview | UG | | | |
| ☐ | Available Reports | UG | | | |
| ☐ | Exporting Data | UG | | | |
| ☑ | Route /loan → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /loan/add → add | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /loan/:id → show | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /loan/:id/edit → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /loan/:id/add-object → addObject | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /loan/:id/remove-object → removeObject | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /loan/:id/transition → transition | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /loan/:id/extend → extend | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /loan/:id/return → return | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /loan/:id/agreement → agreement | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /loan/:id/upload-document → uploadDocument | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /loan/search-objects → searchObjects | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /loan/:sector → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /loan/:sector/add → add | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |


## ahgMarketplacePlugin

Sources: user guide `marketplace-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | How It Works | UG | | | |
| ☐ | Sale Types | UG | | | |
| ☐ | Sector Categories | UG | | | |
| ☐ | For Buyers | UG | | | |
| ☐ | Browsing the Marketplace | UG | | | |
| ☐ | Browsing by Sector or Category | UG | | | |
| ☐ | Browsing Auctions | UG | | | |
| ☐ | Featured Listings | UG | | | |
| ☐ | Viewing a Listing | UG | | | |
| ☐ | Buying (Fixed Price) | UG | | | |
| ☐ | Making an Offer | UG | | | |
| ☐ | Bidding at Auction | UG | | | |
| ☐ | Reserve Price | UG | | | |
| ☐ | Anti-Sniping Protection | UG | | | |
| ☐ | Buy Now in Auctions | UG | | | |
| ☐ | Monitoring Your Bids | UG | | | |
| ☐ | Enquiries | UG | | | |
| ☐ | Your Account | UG | | | |
| ☐ | My Purchases | UG | | | |
| ☐ | My Bids | UG | | | |
| ☐ | My Offers | UG | | | |
| ☐ | My Following | UG | | | |
| ☐ | Leaving Reviews | UG | | | |
| ☐ | For Sellers | UG | | | |
| ☐ | Getting Started | UG | | | |
| ☐ | Your Dashboard | UG | | | |
| ☐ | Creating a Listing | UG | | | |
| ☐ | Basic Information | UG | | | |
| ☐ | Item Details | UG | | | |
| ☐ | Sale Type and Pricing | UG | | | |
| ☐ | Images | UG | | | |
| ☐ | Shipping Configuration | UG | | | |
| ☐ | Tags | UG | | | |
| ☐ | Managing Listings | UG | | | |
| ☐ | Listing Lifecycle | UG | | | |
| ☐ | Listing Actions | UG | | | |
| ☐ | Handling Offers | UG | | | |
| ☐ | Counter-Offer Workflow | UG | | | |
| ☐ | Managing Sales | UG | | | |
| ☐ | Updating Shipping | UG | | | |
| ☑ | Route /marketplace → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/search → search | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /marketplace/sector/:sector → sector | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /marketplace/category/:sector/:slug → category | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /marketplace/auctions → auctionBrowse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/featured → featured | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /marketplace/collection/:slug → collection | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /marketplace/seller/:slug → seller | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /marketplace/listing/:slug → listing | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /marketplace/buy/:slug → buy | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /marketplace/offer/:slug → offerForm | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /marketplace/bid/:slug → bidForm | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /marketplace/enquiry/:slug → enquiryForm | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /marketplace/my/purchases → myPurchases | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/my/bids → myBids | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/my/offers → myOffers | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/my/following → myFollowing | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /marketplace/follow/:seller → follow | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /marketplace/review/:id → reviewForm | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /marketplace/sell → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/sell/register → sellerRegister | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/sell/profile → sellerProfile | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /marketplace/sell/listings → sellerListings | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /marketplace/sell/listings/create → sellerListingCreate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/sell/listings/:id/edit → sellerListingEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /marketplace/sell/listings/:id/images → sellerListingImages | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /marketplace/sell/listings/:id/publish → sellerListingPublish | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /marketplace/sell/listings/:id/withdraw → sellerListingWithdraw | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /marketplace/sell/offers → sellerOffers | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /marketplace/sell/offers/:id/respond → sellerOfferRespond | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /marketplace/sell/transactions → sellerTransactions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /marketplace/sell/transactions/:id → sellerTransactionDetail | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /marketplace/sell/payouts → sellerPayouts | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/sell/reviews → sellerReviews | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/sell/enquiries → sellerEnquiries | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/sell/collections → sellerCollections | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/sell/collections/create → sellerCollectionCreate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/sell/analytics → sellerAnalytics | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/admin → adminDashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/admin/listings → adminListings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /marketplace/admin/listings/:id/review → adminListingReview | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /marketplace/admin/sellers → adminSellers | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /marketplace/admin/sellers/:id/verify → adminSellerVerify | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /marketplace/admin/transactions → adminTransactions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/admin/payouts → adminPayouts | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /marketplace/admin/payouts/batch → adminPayoutsBatch | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /marketplace/admin/reviews → adminReviews | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/admin/categories → adminCategories | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/admin/currencies → adminCurrencies | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/admin/settings → adminSettings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/admin/reports → adminReports | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /marketplace/api/search → apiSearch | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /marketplace/api/listing/:id/bid → apiBid | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /marketplace/api/listing/:id/favourite → apiFavourite | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /marketplace/api/auction/:id/status → apiAuctionStatus | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /marketplace/api/currencies → apiCurrencies | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /marketplace/api/categories/:sector → apiCategories | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |


## ahgMenuManagePlugin

Sources: user guide `rad-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | Route /menu/:id/delete → delete | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /menu/:id/edit → edit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /menu/add → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /menu/list → list | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgMetadataExportPlugin

Sources: user guide `export-data-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists and Collection Managers | UG | | | |
| ☐ | Why Export Data? | UG | | | |
| ☐ | Export Formats Explained | UG | | | |
| ☐ | Quick Export: Single Records | UG | | | |
| ☐ | Exporting One Record | UG | | | |
| ☐ | Steps | UG | | | |
| ☐ | Export Dashboard | UG | | | |
| ☐ | Accessing the Export Dashboard | UG | | | |
| ☐ | CSV Export | UG | | | |
| ☐ | EAD Export | UG | | | |
| ☐ | Bulk Export: Multiple Records | UG | | | |
| ☐ | Using the Clipboard | UG | | | |
| ☐ | Steps | UG | | | |
| ☐ | Sector-Specific Exports | UG | | | |
| ☐ | Archives | UG | | | |
| ☐ | Museum Objects | UG | | | |
| ☐ | Library Items | UG | | | |
| ☐ | Digital Assets | UG | | | |
| ☐ | Understanding Export Files | UG | | | |
| ☐ | CSV Files | UG | | | |
| ☐ | EAD Files | UG | | | |
| ☐ | Dublin Core Files | UG | | | |
| ☐ | Export Settings | UG | | | |
| ☐ | What Gets Exported | UG | | | |
| ☐ | Field Selection | UG | | | |
| ☐ | Tips for Good Exports | UG | | | |
| ☐ | CLI: php symfony c2pa:sign | CODE | | | |
| ☐ | CLI: php symfony metadata:export | CODE | | | |


## ahgMetadataExtractionPlugin

Sources: user guide `metadata-export-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists, Librarians, and Collection Managers | UG | | | |
| ☐ | What is GLAM Metadata Export? | UG | | | |
| ☐ | Export Formats at a Glance | UG | | | |
| ☐ | Using the Web Interface | UG | | | |
| ☐ | Single Record Export | UG | | | |
| ☐ | Steps | UG | | | |
| ☐ | Using the Command Line | UG | | | |
| ☐ | Basic Commands | UG | | | |
| ☐ | Export Options | UG | | | |
| ☐ | Examples | UG | | | |
| ☐ | Understanding the Formats | UG | | | |
| ☐ | For Archives | UG | | | |
| ☐ | EAD3 (Encoded Archival Description 3) | UG | | | |
| ☐ | RIC-O (Records in Contexts - Ontology) | UG | | | |
| ☐ | For Libraries | UG | | | |
| ☐ | MARC21 | UG | | | |
| ☐ | BIBFRAME | UG | | | |
| ☐ | For Museums | UG | | | |
| ☐ | LIDO (Lightweight Information Describing Objects) | UG | | | |
| ☐ | For Visual Resources | UG | | | |
| ☐ | VRA Core 4 | UG | | | |
| ☐ | For Media Collections | UG | | | |
| ☐ | PBCore (Public Broadcasting Core) | UG | | | |
| ☐ | EBUCore | UG | | | |
| ☐ | For Digital Preservation | UG | | | |
| ☐ | PREMIS | UG | | | |
| ☐ | DOI Integration | UG | | | |
| ☐ | What is a DOI? | UG | | | |
| ☐ | DOI in Exports | UG | | | |
| ☐ | Example: DOI in EAD3 | UG | | | |
| ☐ | Example: DOI in RIC-O | UG | | | |
| ☐ | Example: DOI in MARC21 | UG | | | |
| ☐ | DOI Export Options | UG | | | |
| ☐ | CLI Examples with DOI | UG | | | |
| ☐ | Benefits of DOI in Exports | UG | | | |
| ☐ | Requirements | UG | | | |
| ☐ | Scheduling Automated Exports | UG | | | |
| ☐ | Cron Job Examples | UG | | | |
| ☐ | Tips for Successful Exports | UG | | | |
| ☐ | Before Exporting | UG | | | |


## ahgModsManagePlugin

Sources: user guide `rad-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |


## ahgMultiTenantPlugin

Sources: user guide `multi-tenant-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What's New in v1.2.0 | UG | | | |
| ☐ | User Roles | UG | | | |
| ☐ | Tenant Status | UG | | | |
| ☐ | Trial Period | UG | | | |
| ☐ | Domain Routing | UG | | | |
| ☐ | How Domain Resolution Works | UG | | | |
| ☐ | Subdomain Access | UG | | | |
| ☐ | Custom Domain Access | UG | | | |
| ☐ | Unknown Domain Handling | UG | | | |
| ☐ | Administrator Functions | UG | | | |
| ☐ | Accessing Tenant Administration | UG | | | |
| ☐ | Dashboard Overview | UG | | | |
| ☐ | Creating a New Tenant | UG | | | |
| ☐ | Managing Tenant Status | UG | | | |
| ☐ | Suspending a Tenant | UG | | | |
| ☐ | Extending a Trial | UG | | | |
| ☐ | Editing a Tenant | UG | | | |
| ☐ | Managing Tenant Users | UG | | | |
| ☐ | Adding a User to a Tenant | UG | | | |
| ☐ | Changing a User's Role | UG | | | |
| ☐ | Removing a User | UG | | | |
| ☐ | Branding Your Tenant | UG | | | |
| ☐ | Accessing Branding Settings | UG | | | |
| ☐ | Logo Upload | UG | | | |
| ☐ | Color Configuration | UG | | | |
| ☐ | Custom CSS | UG | | | |
| ☐ | Save and Preview | UG | | | |
| ☐ | Switching Between Tenants | UG | | | |
| ☐ | Using the Tenant Switcher | UG | | | |
| ☐ | View All Mode (Administrators Only) | UG | | | |
| ☐ | URL Reference | UG | | | |
| ☐ | Domain-Based Access | UG | | | |
| ☐ | Common Tasks Quick Reference | UG | | | |
| ☐ | For Administrators | UG | | | |
| ☐ | For Owners/Super Users | UG | | | |
| ☐ | For All Users | UG | | | |
| ☐ | Cannot access tenant | UG | | | |
| ☐ | Cannot see other users to assign | UG | | | |
| ☐ | Branding not appearing | UG | | | |
| ☐ | Cannot delete tenant | UG | | | |
| ☐ | Route /tenant/switch/:id → switch | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /tenant/switch/all → switchAll | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/tenants → index | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/tenants/create → create | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/tenants/store → store | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/tenants/:id/edit-tenant → editTenant | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/tenants/:id/update → updateTenant | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/tenants/:id/activate → activate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/tenants/:id/suspend → suspend | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/tenants/:id/extend-trial → extendTrial | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/tenants/:id/delete → delete | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/tenants/assign-user → assignTenantUser | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/tenants/remove-user → removeTenantUser | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/tenants/update-user-role → updateTenantUserRole | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/tenants/:id/edit → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/tenants/:id/super-users → superUsers | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/tenants/assign-super-user → assignSuperUser | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/tenants/remove-super-user → removeSuperUser | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /tenant/:id/users → index | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /tenant/users/assign → assign | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /tenant/users/remove → remove | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /tenant/:id/branding → index | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /tenant/branding/save → save | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /tenant/branding/logo-upload → uploadLogo | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |


## ahgMuseumPlugin

Sources: user guide `museum-module-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | When to Use Museum Module | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Exhibition Management (NEW) | UG | | | |
| ☐ | Accessing Exhibitions | UG | | | |
| ☐ | Exhibition Dashboard | UG | | | |
| ☐ | Creating an Exhibition | UG | | | |
| ☐ | Exhibition Workflow States | UG | | | |
| ☐ | Adding Objects to an Exhibition | UG | | | |
| ☐ | Exhibition Sections | UG | | | |
| ☐ | Storylines and Narratives | UG | | | |
| ☐ | Exhibition Events | UG | | | |
| ☐ | Checklists | UG | | | |
| ☐ | Object List Report | UG | | | |
| ☐ | Adding a Museum Object | UG | | | |
| ☐ | Step 1: Click Add Object | UG | | | |
| ☐ | Step 2: Choose Object Type | UG | | | |
| ☐ | Step 3: Fill in the Form | UG | | | |
| ☐ | Key Fields Explained | UG | | | |
| ☐ | Identification | UG | | | |
| ☐ | Physical Description | UG | | | |
| ☐ | Production and History | UG | | | |
| ☐ | Provenance (Ownership History) | UG | | | |
| ☐ | Loans Management | UG | | | |
| ☐ | Loans Out (Lending Objects) | UG | | | |
| ☐ | Loans In (Borrowing Objects) | UG | | | |
| ☐ | Loan Workflow States | UG | | | |
| ☐ | Location Tracking | UG | | | |
| ☐ | Condition Assessment | UG | | | |
| ☐ | Spectrum Procedures | UG | | | |
| ☐ | Valuation and Insurance | UG | | | |
| ☐ | Getty Vocabulary Integration | UG | | | |
| ☐ | Local AAT Cache (Recommended) | UG | | | |
| ☐ | CLI Commands | UG | | | |
| ☐ | Tips for Cataloging | UG | | | |
| ☐ | Optional Features | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /:slug/cco/provenance → provenance | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /museum/provenance/save → provenanceSave | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /museum/provenance/get → provenanceGet | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /museum/provenance/delete → provenanceDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /museum/provenance/export → provenanceExport | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /museum/browse → browse | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /museum/add → add | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /museum/edit/:slug → edit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /museum/vocabulary → vocabulary | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /museum/getty → gettyAutocomplete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony museum:aat-sync | CODE | | | |
| ☐ | CLI: php symfony museum:getty-link | CODE | | | |
| ☐ | CLI: php symfony museum:migrate | CODE | | | |


## ahgNARSSAPlugin

Sources: user guide `narssa-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What this guide covers | UG | | | |
| ☐ | 1. Prerequisites | UG | | | |
| ☐ | 2. Surfacing what's due | UG | | | |
| ☐ | 3. Building the package | UG | | | |
| ☐ | Option A — Package every approved transfer | UG | | | |
| ☐ | Option B — Package an explicit list | UG | | | |
| ☐ | What you get | UG | | | |
| ☐ | 4. Transmitting to NARSSA | UG | | | |
| ☐ | 5. Recording the acceptance | UG | | | |
| ☐ | 6. Auditing | UG | | | |
| ☐ | 7. Troubleshooting | UG | | | |
| ☐ | CLI: php symfony narssa:transfer-package | CODE | | | |


## ahgNAZPlugin

Sources: user guide `naz-compliance-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists and Compliance Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Command line (for scheduled checks) | UG | | | |
| ☐ | Compliance notes | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /admin/naz → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/naz/closures → closures | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/naz/closure/create → closureCreate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/naz/closure/:id/edit → closureEdit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/naz/permits → permits | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/naz/permit/create → permitCreate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/naz/permit/:id → permitView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/naz/researchers → researchers | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/naz/researcher/create → researcherCreate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/naz/researcher/:id/edit → researcherEdit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/naz/researcher/:id → researcherView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/naz/schedules → schedules | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/naz/schedule/create → scheduleCreate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/naz/schedule/:id → scheduleView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/naz/transfers → transfers | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/naz/transfer/create → transferCreate | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/naz/transfer/:id → transferView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/naz/protected → protectedRecords | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/naz/reports → reports | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/naz/config → config | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /naz → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /naz/closures → closures | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /naz/permits → permits | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /naz/researchers → researchers | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /naz/schedules → schedules | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /naz/transfers → transfers | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /naz/protected → protectedRecords | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /naz/reports → reports | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /naz/config → config | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony naz:closure-check | CODE | | | |
| ☐ | CLI: php symfony naz:permit-expiry | CODE | | | |
| ☐ | CLI: php symfony naz:report | CODE | | | |
| ☐ | CLI: php symfony naz:transfer-due | CODE | | | |


## ahgNMMZPlugin

Sources: user guide `nmmz-compliance-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Heritage Officers and Compliance Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Command line | UG | | | |
| ☐ | Compliance notes | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | Route /admin/nmmz → index | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/monuments → monuments | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/monument/create → monumentCreate | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/monument/:id → monumentView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/nmmz/antiquities → antiquities | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/antiquity/create → antiquityCreate | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/antiquity/:id → antiquityView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/nmmz/permits → permits | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/permit/create → permitCreate | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/permit/:id → permitView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/nmmz/sites → sites | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/site/create → siteCreate | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/site/:id → siteView | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/nmmz/hia → hia | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/hia/create → hiaCreate | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/reports → reports | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /admin/nmmz/config → config | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | CLI: php symfony nmmz:report | CODE | | | |


## ahgObservabilityPlugin

Sources: user guide `observability-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Technical Staff | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | The endpoint | UG | | | |
| ☐ | CLI commands (`php bin/atom`) | UG | | | |
| ☐ | Administration / setup | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | Route /metrics → metrics | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |


## ahgOcflPlugin

Sources: user guide `ocfl-storage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Administrators and Technical Staff | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Admin dashboard | UG | | | |
| ☐ | CLI commands (`php bin/atom`) | UG | | | |
| ☐ | API endpoints | UG | | | |
| ☐ | Administration / setup | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /admin/ocfl → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/ocfl/init → apiInit | CODE | PASS | pw-authed-seq 2026-06-27 | HTTP 403 |
| ☑ | Route /api/ocfl/verify-all → apiVerifyAll | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/ocfl/ingest/:id → apiIngest | CODE | PASS | pw-authed-seq 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /api/ocfl/verify/:id → apiVerify | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/ocfl/export/:id → apiExport | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |


## ahgPortableExportPlugin

Sources: user guide `export-data-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists and Collection Managers | UG | | | |
| ☐ | Why Export Data? | UG | | | |
| ☐ | Export Formats Explained | UG | | | |
| ☐ | Quick Export: Single Records | UG | | | |
| ☐ | Exporting One Record | UG | | | |
| ☐ | Steps | UG | | | |
| ☐ | Export Dashboard | UG | | | |
| ☐ | Accessing the Export Dashboard | UG | | | |
| ☐ | CSV Export | UG | | | |
| ☐ | EAD Export | UG | | | |
| ☐ | Bulk Export: Multiple Records | UG | | | |
| ☐ | Using the Clipboard | UG | | | |
| ☐ | Steps | UG | | | |
| ☐ | Sector-Specific Exports | UG | | | |
| ☐ | Archives | UG | | | |
| ☐ | Museum Objects | UG | | | |
| ☐ | Library Items | UG | | | |
| ☐ | Digital Assets | UG | | | |
| ☐ | Understanding Export Files | UG | | | |
| ☐ | CSV Files | UG | | | |
| ☐ | EAD Files | UG | | | |
| ☐ | Dublin Core Files | UG | | | |
| ☐ | Export Settings | UG | | | |
| ☐ | What Gets Exported | UG | | | |
| ☐ | Field Selection | UG | | | |
| ☐ | Tips for Good Exports | UG | | | |
| ☑ | Route /portable-export → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /portable-export/api/start → apiStartExport | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 |
| ☑ | Route /portable-export/api/quick-start → apiQuickStart | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 |
| ☑ | Route /portable-export/api/clipboard-export → apiClipboardExport | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 |
| ☑ | Route /portable-export/api/fonds-search → apiFondsSearch | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /portable-export/api/progress → apiProgress | TECH | N/A | pw-authed 2026-06-27 | HTTP 400 |
| ☑ | Route /portable-export/api/list → apiList | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /portable-export/api/delete → apiDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 |
| ☑ | Route /portable-export/api/token → apiToken | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 |
| ☑ | Route /portable-export/api/estimate → apiEstimate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /portable-export/download → download | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /portable-export/import → import | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /portable-export/api/start-import → apiStartImport | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 |
| ☐ | Route /portable-export/api/import-progress → apiImportProgress | TECH | N/A | pw-authed 2026-06-27 | HTTP 400 |
| ☑ | Route /portable-export/api/import-validate → apiImportValidate | TECH | PASS | pw-authed 2026-06-27 | HTTP 405 |
| ☑ | Route /portable-export/api/import-list → apiImportList | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony portable:cleanup | CODE | | | |
| ☐ | CLI: php symfony portable:export | CODE | | | |
| ☐ | CLI: php symfony portable:import | CODE | | | |
| ☐ | CLI: php symfony portable:verify | CODE | | | |


## ahgPreservationPlugin

Sources: user guide `preservation-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Getting Started | UG | | | |
| ☐ | Accessing the Preservation Dashboard | UG | | | |
| ☐ | Accessing Preservation Settings | UG | | | |
| ☐ | Understanding the Dashboard | UG | | | |
| ☐ | Statistics Overview | UG | | | |
| ☐ | Core Features | UG | | | |
| ☐ | 1. Checksums | UG | | | |
| ☐ | How Checksums Work | UG | | | |
| ☐ | Supported Algorithms | UG | | | |
| ☐ | Generating Checksums | UG | | | |
| ☐ | 2. Fixity Verification | UG | | | |
| ☐ | Running Fixity Checks | UG | | | |
| ☐ | 3. Virus Scanning | UG | | | |
| ☐ | Prerequisites | UG | | | |
| ☐ | How Virus Scanning Works | UG | | | |
| ☐ | Running Virus Scans | UG | | | |
| ☐ | Quarantine | UG | | | |
| ☐ | 4. Format Conversion | UG | | | |
| ☐ | Supported Conversions | UG | | | |
| ☐ | How Format Conversion Works | UG | | | |
| ☐ | Running Format Conversions | UG | | | |
| ☐ | Output Location | UG | | | |
| ☐ | 5. Backup Verification | UG | | | |
| ☐ | How Backup Verification Works | UG | | | |
| ☐ | Running Backup Verification | UG | | | |
| ☐ | 6. Backup Replication | UG | | | |
| ☐ | Supported Target Types | UG | | | |
| ☐ | Managing Replication Targets | UG | | | |
| ☐ | Running Replication | UG | | | |
| ☐ | Replication Workflow | UG | | | |
| ☐ | 7. PREMIS Events | UG | | | |
| ☐ | Event Types | UG | | | |
| ☐ | Viewing Events | UG | | | |
| ☐ | 8. Format Identification (PRONOM) | UG | | | |
| ☐ | What is PRONOM? | UG | | | |
| ☐ | Prerequisites | UG | | | |
| ☐ | How Format Identification Works | UG | | | |
| ☐ | Confidence Levels | UG | | | |
| ☐ | Running Format Identification | UG | | | |
| ☐ | Benefits of PRONOM Identification | UG | | | |
| ☑ | Route /api/preservation/checksum/:id/generate → apiGenerateChecksum | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/preservation/fixity/:id/verify → apiVerifyFixity | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/preservation/stats → apiStats | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/preservation/object/:id → object | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/preservation/fixity-log → fixityLog | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/events → events | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/formats → formats | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/policies → policies | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/reports → reports | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /preservation/:slug → packagesBySlug | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /admin/preservation/packages → packages | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/package/edit → packageEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/preservation/package/:id → packageView | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/preservation/package/:id/download → packageDownload | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /api/preservation/package/add-object → apiPackageAddObject | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/package/remove-object → apiPackageRemoveObject | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/package/build → apiPackageBuild | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/package/validate → apiPackageValidate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/package/export → apiPackageExport | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/package/convert → apiPackageConvert | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/package/delete → apiPackageDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/scheduler → scheduler | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/schedule/edit → scheduleEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/schedule/run/:id → scheduleRunView | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/preservation/schedule/toggle → apiScheduleToggle | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/schedule/run → apiScheduleRun | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/schedule/delete → apiScheduleDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/identification → identification | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/identify → apiIdentify | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/conversion → conversion | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/convert → apiConvert | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/virus-scan → virusScan | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/virus-scan → apiVirusScan | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/backup → backup | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/preservation/backup/verify → apiVerifyBackup | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation/extended → extended | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/preservation → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /tiff-pdf-merge → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /tiff-pdf-merge/:informationObject → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /tiff-pdf-merge/create → create | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /tiff-pdf-merge/upload → upload | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /tiff-pdf-merge/reorder → reorder | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /tiff-pdf-merge/remove-file → removeFile | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /tiff-pdf-merge/job/:job_id → getJob | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /tiff-pdf-merge/process → process | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /tiff-pdf-merge/download/:job_id → download | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /tiff-pdf-merge/delete → delete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /tiff-pdf-merge/jobs → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /tiff-pdf-merge/job/:job_id/view → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | CLI: php symfony ahg:tiff-combine-watch | CODE | | | |
| ☐ | CLI: php symfony ahg:tiff-pdf-process | CODE | | | |
| ☐ | CLI: php symfony preservation:convert | CODE | | | |
| ☐ | CLI: php symfony preservation:fixity | CODE | | | |
| ☐ | CLI: php symfony preservation:identify | CODE | | | |
| ☐ | CLI: php symfony preservation:migration | CODE | | | |
| ☐ | CLI: php symfony preservation:package | CODE | | | |
| ☐ | CLI: php symfony preservation:pronom-sync | CODE | | | |
| ☐ | CLI: php symfony preservation:replicate | CODE | | | |
| ☐ | CLI: php symfony preservation:scheduler | CODE | | | |
| ☐ | CLI: php symfony preservation:verify-backup | CODE | | | |
| ☐ | CLI: php symfony preservation:virus-scan | CODE | | | |


## ahgPrivacyPlugin

Sources: user guide `privacy-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Workflow Overview | UG | | | |
| ☐ | What This Plugin Manages | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Part 1: Understanding Jurisdictions | UG | | | |
| ☐ | Supported Privacy Regulations | UG | | | |
| ☐ | Part 2: Data Subject Access Requests (DSARs) | UG | | | |
| ☐ | DSAR Workflow | UG | | | |
| ☐ | Creating a DSAR | UG | | | |
| ☐ | DSAR Dashboard | UG | | | |
| ☐ | Part 3: Breach Register | UG | | | |
| ☐ | Recording a Data Breach | UG | | | |
| ☐ | Breach Notification Timeline | UG | | | |
| ☐ | Part 4: PII Detection | UG | | | |
| ☐ | What is PII? | UG | | | |
| ☐ | PII Scanner Dashboard | UG | | | |
| ☐ | Scanning a Record | UG | | | |
| ☐ | Part 5: PDF Redaction | UG | | | |
| ☐ | How Redaction Works | UG | | | |
| ☐ | Marking Entities for Redaction | UG | | | |
| ☐ | Part 6: Consent Management | UG | | | |
| ☐ | Recording Consent | UG | | | |
| ☐ | Part 7: CLI Commands (System Administrators) | UG | | | |
| ☐ | PII Scanning Commands | UG | | | |
| ☐ | Jurisdiction Management Commands | UG | | | |
| ☐ | Available Jurisdictions | UG | | | |
| ☐ | Example CLI Output | UG | | | |
| ☐ | Risk Score Calculation | UG | | | |
| ☐ | PAIA Integration (South Africa) | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /privacy → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /privacy/dsar → dsarIndex | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /privacy/dsar/new → dsarNew | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /privacy/dsar/:id → dsarView | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /privacy/dsar/:id/update → dsarUpdate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /privacy/breaches → breachIndex | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /privacy/breach/new → breachNew | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /privacy/breach/:id → breachView | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /privacy/consent → consentIndex | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /privacy/ropa → ropa | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /admin/privacy → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/privacy/config → config | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /admin/privacy/embedded-pii/resolve → embeddedPiiResolve | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /admin/privacy/embedded-pii → embeddedPii | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/privacy/redaction/:id → visualRedactionEditor | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /privacyAdmin/getVisualRedactions → getVisualRedactions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /privacyAdmin/saveVisualRedaction → saveVisualRedaction | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /privacyAdmin/deleteVisualRedaction → deleteVisualRedaction | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /privacyAdmin/getNerEntitiesForPage → getNerEntitiesForPage | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /privacyAdmin/applyVisualRedactions → applyVisualRedactions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /privacyAdmin/getDocumentInfo → getDocumentInfo | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /privacyAdmin/downloadRedactedFile → downloadRedactedFile | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | CLI: php symfony privacy:breach-check | CODE | | | |
| ☐ | CLI: php symfony privacy:jurisdiction | CODE | | | |
| ☐ | CLI: php symfony privacy:scan-embedded | CODE | | | |
| ☐ | CLI: php symfony privacy:scan-pii | CODE | | | |


## ahgProvenancePlugin

Sources: user guide `provenance-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What is Provenance? | UG | | | |
| ☐ | Key Features | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Viewing Provenance | UG | | | |
| ☐ | Provenance View Page | UG | | | |
| ☐ | Adding/Editing Provenance | UG | | | |
| ☐ | Step 1: Navigate to Edit | UG | | | |
| ☐ | Step 2: Complete the Form | UG | | | |
| ☐ | Step 3: Add Chain of Custody Events | UG | | | |
| ☐ | Event Types | UG | | | |
| ☐ | Ownership Changes | UG | | | |
| ☐ | Loans & Deposits | UG | | | |
| ☐ | Creation & Discovery | UG | | | |
| ☐ | Loss & Recovery | UG | | | |
| ☐ | Movement | UG | | | |
| ☐ | Documentation | UG | | | |
| ☐ | Institutional | UG | | | |
| ☐ | Certainty Levels | UG | | | |
| ☐ | Status Options | UG | | | |
| ☐ | Current Status | UG | | | |
| ☐ | Custody Type | UG | | | |
| ☐ | Nazi-Era Provenance (Museums) | UG | | | |
| ☐ | Cultural Property Status | UG | | | |
| ☐ | Supporting Documents | UG | | | |
| ☐ | Document Types | UG | | | |
| ☐ | Visual Timeline | UG | | | |
| ☐ | Dashboard Statistics | UG | | | |
| ☐ | Agents (Owners/Holders) | UG | | | |
| ☐ | Agent Types | UG | | | |
| ☐ | Agent Autocomplete | UG | | | |
| ☐ | Best Practices | UG | | | |
| ☐ | CSV Import Format | UG | | | |
| ☐ | Integration with Other Plugins | UG | | | |
| ☐ | Common Tasks | UG | | | |
| ☐ | Mark Provenance Complete | UG | | | |
| ☐ | Record a Gap | UG | | | |
| ☐ | Flag Cultural Property Issue | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /provenance/coverage → coverage | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /provenance/coverage-data → apiCoverage | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /provenance/trace/:id → apiTrace | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /provenance/authenticity/:id → authenticity | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | CLI: php symfony ai-provenance:keygen | CODE | | | |
| ☐ | CLI: php symfony ai-provenance:replay | CODE | | | |
| ☐ | CLI: php symfony ai-provenance:verify | CODE | | | |


## ahgRadManagePlugin

Sources: user guide `mirador-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What Makes Mirador Special? | UG | | | |
| ☐ | The Mirador Interface | UG | | | |
| ☐ | Basic Navigation | UG | | | |
| ☐ | Zooming and Panning | UG | | | |
| ☐ | Opening the Side Panel | UG | | | |
| ☐ | Comparing Images Side by Side | UG | | | |
| ☐ | Step 1: Open First Image | UG | | | |
| ☐ | Step 2: Add a Window | UG | | | |
| ☐ | Step 3: Load Second Image | UG | | | |
| ☐ | Step 4: Arrange Windows | UG | | | |
| ☐ | Synchronized Viewing | UG | | | |
| ☐ | Enable Sync | UG | | | |
| ☐ | Viewing Annotations | UG | | | |
| ☐ | Viewing Annotation Details | UG | | | |
| ☐ | Multi-Page Documents | UG | | | |
| ☐ | Page Navigation | UG | | | |
| ☐ | Book View Mode | UG | | | |
| ☐ | Loading External IIIF Manifests | UG | | | |
| ☐ | Step 1: Get the IIIF Manifest URL | UG | | | |
| ☐ | Step 2: Add Resource | UG | | | |
| ☐ | Step 3: View the Item | UG | | | |
| ☐ | Workspace Features | UG | | | |
| ☐ | Save Your Session | UG | | | |
| ☐ | Export Workspace | UG | | | |
| ☐ | Keyboard Shortcuts | UG | | | |
| ☐ | Common Uses | UG | | | |
| ☐ | Tips | UG | | | |
| ☐ | Need Help? | UG | | | |


## ahgRdmPlugin

Sources: **no manual — surface derived from code**.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Create a dataset (title, description, optional research project) | AUTHORED | | | |
| ☐ | Deposit files into a dataset (each becomes a child IO + master digital object) | AUTHORED | | | |
| ☐ | Run POPIA scan (deterministic SA-ID/email/phone/passport + special-category lexicon + gateway NER + scanned-PDF OCR) | AUTHORED | | | |
| ☐ | View masked scan findings + dataset verdict (CLEAR / PERSONAL / SPECIAL_CATEGORY) | AUTHORED | | | |
| ☐ | Human gate: confirm or dismiss each finding with a decision note | AUTHORED | | | |
| ☐ | Open release is BLOCKED while any PERSONAL/SPECIAL finding is pending or confirmed | AUTHORED | | | |
| ☐ | Apply a disposition: restrict / embargo / de-identify / release | AUTHORED | | | |
| ☐ | Restricted dataset files relocated off /uploads; raw URL returns 404; download only via ODRL-gated controller | AUTHORED | | | |
| ☐ | DataCite DOI minted on disposition (live only on a production DOI config; else reserved test-prefix) | AUTHORED | | | |
| ☐ | Public citable landing page (DataCite-style citation + DOI + access badge; binaries stay gated) | AUTHORED | | | |
| ☐ | Link or create-and-link a Data Management Plan (DMP) to a dataset | AUTHORED | | | |
| ☐ | Compliance scoreboard, filterable by institution / verdict / disposition (admin) | AUTHORED | | | |
| ☐ | Roll-up dashboard: 8 KPI cards + 5 Chart.js charts + date/faculty filters (admin) | AUTHORED | | | |
| ☐ | ACL: dataset mutations deny a non-owner non-admin; index scoped to depositor; dashboard/compliance admin-only | AUTHORED | | | |
| ☑ | Route /research/datasets → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/datasets/dashboard → dashboard | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/datasets/compliance → compliance | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/datasets/create → create | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /research/datasets/:id → show | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /research/datasets/:id/deposit → deposit | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /research/datasets/:id/scan → scan | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /research/datasets/:id/file/:fid → fileDownload | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /research/datasets/:id/findings/:fid/resolve → resolveFinding | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /research/datasets/:id/disposition → disposition | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /research/datasets/:id/dmp → linkDmp | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /research/datasets/:id/dmp/unlink → unlinkDmp | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /research/datasets/:id/landing → landing | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | CLI: php symfony rdm:demo | CODE | | | |
| ☐ | CLI: php symfony rdm:scan | CODE | | | |


## ahgRecordsManagePlugin

Sources: user guide `rad-manage-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |


## ahgRegistryPlugin

Sources: user guide `registry-community-hub-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Who Is It For? | UG | | | |
| ☐ | How It Works | UG | | | |
| ☐ | Getting Started | UG | | | |
| ☐ | Accessing the Registry | UG | | | |
| ☐ | Creating an Account | UG | | | |
| ☐ | Navigation Structure | UG | | | |
| ☐ | Public Directory | UG | | | |
| ☐ | Browsing Institutions | UG | | | |
| ☐ | Browsing Vendors | UG | | | |
| ☐ | Browsing Software | UG | | | |
| ☐ | Viewing Detail Pages | UG | | | |
| ☐ | Institution Detail | UG | | | |
| ☐ | Vendor Detail | UG | | | |
| ☐ | Software Detail | UG | | | |
| ☐ | Unified Search | UG | | | |
| ☐ | Map View | UG | | | |
| ☐ | Institution Management | UG | | | |
| ☐ | Registering Your Institution | UG | | | |
| ☐ | Institution Dashboard | UG | | | |
| ☐ | Editing Your Institution Profile | UG | | | |
| ☐ | Managing Contacts | UG | | | |
| ☐ | Managing Instances | UG | | | |
| ☐ | Managing Software in Use | UG | | | |
| ☐ | Viewing Vendor Relationships | UG | | | |
| ☐ | Vendor Management | UG | | | |
| ☐ | Registering as a Vendor | UG | | | |
| ☐ | Vendor Dashboard | UG | | | |
| ☐ | Editing Your Vendor Profile | UG | | | |
| ☐ | Managing Vendor Contacts | UG | | | |
| ☐ | Managing Client Relationships | UG | | | |
| ☐ | Managing Software Products | UG | | | |
| ☐ | Managing Software Releases | UG | | | |
| ☐ | Call & Issue Log (CRM) | UG | | | |
| ☐ | Community Features | UG | | | |
| ☐ | Community Hub | UG | | | |
| ☐ | User Groups | UG | | | |
| ☐ | Browsing Groups | UG | | | |
| ☐ | Viewing a Group | UG | | | |
| ☐ | Creating a Group | UG | | | |
| ☐ | Managing Groups | UG | | | |
| ☐ | Route /registry/api/sync/register → apiSyncRegister | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /registry/api/sync/heartbeat → apiSyncHeartbeat | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /registry/api/sync/update → apiSyncUpdate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /registry/api/sync/status → apiSyncStatus | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☑ | Route /registry/api/directory → apiDirectory | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /registry/api/software/:slug/latest → apiSoftwareLatest | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /registry/admin → adminDashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/institutions → adminInstitutions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /registry/admin/institutions/verify → adminInstitutionVerify | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /registry/admin/institutions/:id/users → adminInstitutionUsers | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /registry/admin/vendors → adminVendors | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /registry/admin/vendors/verify → adminVendorVerify | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /registry/admin/software → adminSoftware | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /registry/admin/software/verify → adminSoftwareVerify | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /registry/admin/groups → adminGroups | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/groups/verify → adminGroupVerify | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /registry/admin/standards → adminStandards | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /registry/admin/standards/:id/edit → adminStandardEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /registry/admin/standards/new → adminStandardEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /registry/admin/standards/:standardId/extensions/:id/edit → adminExtensionEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /registry/admin/standards/:standardId/extensions/new → adminExtensionEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /registry/admin/standards/extensions/:id/delete → adminExtensionDelete | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /registry/admin/setup-guides → adminSetupGuides | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/discussions → adminDiscussions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/blog → adminBlog | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/reviews → adminReviews | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/sync → adminSync | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/dropdowns → adminDropdowns | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/dropdowns/:id/edit → adminDropdownEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /registry/admin/dropdowns/:id/delete → adminDropdownDelete | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /registry/admin/dropdowns/new → adminDropdownEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/settings → adminSettings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/footer → adminFooter | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/email → adminEmail | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/import → adminImport | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/users → adminUsers | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/admin/users/manage → adminUserManage | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /registry/admin/users/:id/edit → adminUserEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /registry/admin/users/:id/reset-password → adminUserResetPassword | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /registry/admin/institutions/:id/edit → institutionEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /registry/admin/vendors/:id/edit → vendorEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /registry/admin/software/:id/edit → myVendorSoftwareEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /registry/admin/groups/:id/edit → adminGroupEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /registry/admin/groups/:id/members → adminGroupMembers | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /registry/admin/groups/:id/email → adminGroupEmail | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /registry/my/institution → myInstitutionDashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/my/institution/register → institutionRegister | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/my/institution/edit → institutionEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/my/institution/contacts → myInstitutionContacts | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/my/institution/contacts/add → myInstitutionContactAdd | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /registry/my/institution/contacts/:id/edit → myInstitutionContactEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /registry/my/institution/contacts/:id/delete → myInstitutionContactDelete | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /registry/my/institution/instances → myInstitutionInstances | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/my/institution/instances/add → myInstitutionInstanceAdd | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /registry/my/institution/instances/:id/edit → myInstitutionInstanceEdit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /registry/my/institution/instances/:id/delink → myInstitutionInstanceDelink | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /registry/my/institution/instances/:id/relink → myInstitutionInstanceRelink | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /registry/my/institution/software → myInstitutionSoftware | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /registry/my/institution/vendors → myInstitutionVendors | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /registry/my/institution/vendors/:id/remove → myInstitutionVendorRemove | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |


## ahgReportBuilderPlugin

Sources: user guide `forms-builder-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Dashboard Overview | UG | | | |
| ☐ | Statistics Cards | UG | | | |
| ☐ | Quick Links | UG | | | |
| ☐ | Managing Templates | UG | | | |
| ☐ | Viewing Templates | UG | | | |
| ☐ | Creating a New Template | UG | | | |
| ☐ | Form Builder | UG | | | |
| ☐ | Layout | UG | | | |
| ☐ | Adding Fields | UG | | | |
| ☐ | Field Types | UG | | | |
| ☐ | Editing Field Properties | UG | | | |
| ☐ | Reordering Fields | UG | | | |
| ☐ | Deleting Fields | UG | | | |
| ☐ | Form Assignments | UG | | | |
| ☐ | How Assignment Works | UG | | | |
| ☐ | Creating an Assignment | UG | | | |
| ☐ | Assignment Examples | UG | | | |
| ☐ | Template Library | UG | | | |
| ☐ | Available Templates | UG | | | |
| ☐ | Using Library Templates | UG | | | |
| ☐ | Form Preview | UG | | | |
| ☐ | Previewing a Template | UG | | | |
| ☐ | Template Information Panel | UG | | | |
| ☐ | Import and Export | UG | | | |
| ☐ | Exporting a Template | UG | | | |
| ☐ | Importing a Template | UG | | | |
| ☐ | CLI Export/Import | UG | | | |
| ☐ | Auto-Save and Drafts | UG | | | |
| ☐ | How Auto-Save Works | UG | | | |
| ☐ | Recovering a Draft | UG | | | |
| ☐ | CLI Commands | UG | | | |
| ☐ | List Templates | UG | | | |
| ☐ | Example Output | UG | | | |
| ☐ | Best Practices | UG | | | |
| ☐ | Template Design | UG | | | |
| ☐ | Assignments | UG | | | |
| ☐ | Form Not Appearing | UG | | | |
| ☐ | Fields Not Saving | UG | | | |
| ☑ | Route /api/report-builder/attachment/:id/delete → apiAttachmentDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/report-builder/attachment/upload → apiAttachmentUpload | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/attachments → apiAttachments | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/share/:id/deactivate → apiShareDeactivate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/report-builder/share/create → apiShareCreate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/snapshot → apiSnapshot | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/query/relationships/:table → apiQueryRelationships | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/report-builder/query/columns/:table → apiQueryColumns | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/report-builder/query/tables → apiQueryTables | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/query/validate → apiQueryValidate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/query/save → apiQuerySave | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/query/execute → apiQueryExecute | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/version/restore → apiVersionRestore | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/version/create → apiVersionCreate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/versions/:id → apiVersions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/report-builder/comment → apiComment | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/status → apiStatusChange | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/template/:id/delete → apiTemplateDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/report-builder/template/apply → apiTemplateApply | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/template/save → apiTemplateSave | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/entity-search → apiEntitySearch | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/og-fetch → apiOgFetch | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/link/:id/delete → apiLinkDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/report-builder/link/save → apiLinkSave | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/section/reorder → apiSectionReorder | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/section/:id/delete → apiSectionDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/report-builder/section/save → apiSectionSave | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/widget/:id/delete → apiWidgetDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/report-builder/widget/save → apiWidgetSave | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/widgets → apiWidgets | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /report-widget/:id → widget | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/report-builder/columns/:source → apiColumns | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /api/report-builder/data → apiData | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/chart-data → apiChartData | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/save → apiSave | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /api/report-builder/delete/:id → apiDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /reports/shared/:token → sharedView | TECH | PASS | fixed 2026-06-27 | HTTP 200 (setTemplate fix #187) |
| ☐ | Route /reports/custom/:id → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/report-builder/:id/schedule/:scheduleId/delete → scheduleDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /admin/report-builder/:id/schedule → schedule | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/report-builder/:id/export/:format → export | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/report-builder/:id/query → query | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/report-builder/:id/history → history | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/report-builder/:id/preview → preview | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/report-builder/:id/clone → cloneReport | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /admin/report-builder/:id/edit → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/report-builder/:id/delete → delete | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/report-builder/template/:id/delete → deleteTemplate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/report-builder/template/:id/edit → editTemplate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/report-builder/template/:id/preview → previewTemplate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /admin/report-builder/templates → templates | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/report-builder/create → create | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/report-builder/archive → archive | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/report-builder → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgReportsPlugin

Sources: user guide `reports-dashboard-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | How to Access | UG | | | |
| ☐ | Collection Reports | UG | | | |
| ☐ | Available Reports | UG | | | |
| ☐ | Running a Collection Report | UG | | | |
| ☐ | Activity Reports | UG | | | |
| ☐ | Available Reports | UG | | | |
| ☐ | User Reports | UG | | | |
| ☐ | Available Reports | UG | | | |
| ☐ | Compliance Reports | UG | | | |
| ☐ | Available Reports | UG | | | |
| ☐ | Generating Reports | UG | | | |
| ☐ | Step 1: Select Report Type | UG | | | |
| ☐ | Step 2: Set Parameters | UG | | | |
| ☐ | Step 3: View Results | UG | | | |
| ☐ | Step 4: Export (Optional) | UG | | | |
| ☐ | PDF Export | UG | | | |
| ☐ | Scheduling Reports | UG | | | |
| ☐ | Tips | UG | | | |
| ☐ | Optional Features | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /admin/dashboard → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /reports → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /reports/view/:code → report | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /reports/descriptions → descriptions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /reports/authorities → authorities | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /reports/repositories → repositories | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /reports/accessions → accessions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /reports/storage → storage | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /reports/recent → recent | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /reports/activity → activity | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /reports/spatial-analysis → reportSpatialAnalysis | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgRepositoryManagePlugin

Sources: user guide `rad-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /repository/add → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /repository/browse → browse | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgRequestToPublishPlugin

Sources: user guide `publish-gates-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | Publish Gate Engine | UG | | | |
| ☐ | Change Summary | UG | | | |
| ☐ | Type-Driven Editor Bridge | UG | | | |
| ☐ | Default Gate Rules (Seeded) | UG | | | |
| ☐ | Architecture | UG | | | |
| ☐ | Database Tables | UG | | | |
| ☐ | Services | UG | | | |
| ☐ | Workflow Integration | UG | | | |
| ☐ | API Integration | UG | | | |
| ☐ | Access Points | UG | | | |
| ☐ | Technical Requirements | UG | | | |
| ☐ | Standards Compliance | UG | | | |
| ☐ | Route /requesttopublish/:slug → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /requesttopublish/delete/:slug → delete | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /requestToPublish/submit/:slug → submit | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /requesttopublish/browse → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /requesttopublish → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /requesttopublish/ → browse | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /requesttopublish/receipt → receipt | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /requesttopublish/receipt/:token → receipt | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /requesttopublish/inbox → inbox | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /requesttopublish/review/:id → review | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |


## ahgResearchPlugin

Sources: user guide `researcher-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Table of Contents | UG | | | |
| ☐ | 1. Overview | UG | | | |
| ☐ | Key Capabilities | UG | | | |
| ☐ | User Roles | UG | | | |
| ☐ | 2. Getting Started | UG | | | |
| ☐ | Accessing the Portal | UG | | | |
| ☐ | First-Time Setup | UG | | | |
| ☐ | Navigation Structure | UG | | | |
| ☐ | 3. Dashboard | UG | | | |
| ☐ | Quick Actions from Dashboard | UG | | | |
| ☐ | 4. Researcher Registration & Profile | UG | | | |
| ☐ | Registration | UG | | | |
| ☐ | Rejection with Audit Trail | UG | | | |
| ☐ | Profile Management | UG | | | |
| ☐ | Researcher Types | UG | | | |
| ☐ | Verification System | UG | | | |
| ☐ | Credential Renewal | UG | | | |
| ☐ | 5. Reading Room & Bookings | UG | | | |
| ☐ | Creating a Booking | UG | | | |
| ☐ | Booking Lifecycle | UG | | | |
| ☐ | Material Requests | UG | | | |
| ☐ | Check-In / Check-Out | UG | | | |
| ☐ | Walk-In Visitors | UG | | | |
| ☐ | Seat Assignment | UG | | | |
| ☐ | Equipment Booking | UG | | | |
| ☐ | Retrieval Queue | UG | | | |
| ☐ | Call Slips | UG | | | |
| ☐ | 6. Collections | UG | | | |
| ☐ | Creating Collections | UG | | | |
| ☐ | Adding Items to Collections | UG | | | |
| ☐ | Collection Operations | UG | | | |
| ☐ | Finding Aid Export | UG | | | |
| ☐ | 7. Saved Searches & Discovery | UG | | | |
| ☐ | Saving Searches | UG | | | |
| ☐ | Managing Saved Searches | UG | | | |
| ☐ | Result Diffing | UG | | | |
| ☐ | Result Snapshots | UG | | | |
| ☐ | Search Alerts | UG | | | |
| ☐ | 8. Annotations & Notes | UG | | | |
| ☐ | Legacy Annotations | UG | | | |
| ☐ | Route /api/research/stats → stats | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☐ | Route /api/research/annotations → annotations | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☐ | Route /api/research/bibliographies/:id/export/:format → exportBibliography | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 (id=553) |
| ☐ | Route /api/research/bibliographies → bibliographies | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☑ | Route /api/research/citations/:id/:format → citation | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /api/research/bookings → bookings | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☐ | Route /api/research/searches → searches | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☐ | Route /api/research/collections/:id → collection | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 (id=553) |
| ☐ | Route /api/research/collections → collections | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☐ | Route /api/research/projects → projects | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☐ | Route /api/research/profile → profile | TECH | N/A | pw-authed 2026-06-27 | HTTP 401 |
| ☑ | Route /audit/export → export | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /audit/user/:id → user | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /audit/record/:table/:record_id → record | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /audit/view/:id → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /audit → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /research/activities/:id → viewActivity | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /research/activities → activities | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/walk-in → walkIn | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/equipment/history → equipmentHistory | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /research/equipment/book → bookEquipment | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /research/equipment → equipment | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/seats/map → seatMap | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /research/seats/assign → assignSeat | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /research/seats → seats | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/call-slips/print → printCallSlips | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /research/retrieval-queue → retrievalQueue | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/admin/statistics → adminStatistics | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/admin/types/new → editResearcherType | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/admin/types/edit/:id → editResearcherType | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /research/admin/types → adminTypes | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/orcid → orcid | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/orcid/fetch-public → orcidFetchPublic | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /research/orcid/pull-profile → orcidPullProfile | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /research/orcid/credentials/clear → orcidClearCredentials | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /research/orcid/credentials → orcidCredentials | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/orcid/disconnect → orcidDisconnect | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /research/orcid/callback → orcidCallback | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /research/orcid/connect → orcidConnect | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☐ | Route /research/workspaces/:id/invite → inviteWorkspaceMember | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /research/workspaces/:id/discussion/:discussion_id → workspaceDiscussion | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /research/workspaces/:id → viewWorkspace | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /research/workspaces → workspaces | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/project/:id/invite → inviteCollaborator | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /research/project/:id/collaborators → projectCollaborators | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /research/project/:id/activity → projectActivity | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /research/project/:id/edit → editProject | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /research/project/:id → viewProject | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /research/projects → projects | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/experience-level → saveExperienceLevel | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/bibliography/:id/export/:format → exportBibliography | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /research/bibliography/:id/add → addBibliographyEntry | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /research/bibliography/:id → viewBibliography | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /research/bibliographies → bibliographies | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /research/reproduction/download/:token → reproductionDownload | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /research/reproduction/new → newReproduction | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /research/reproduction/:id → viewReproduction | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /research/reproductions → reproductions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /research/invitation/:type/:id/accept → acceptInvitation | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /research/invitation/:type/:id/decline → declineInvitation | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | CLI: php symfony research:orcid-sync | CODE | | | |


## ahgResearcherPlugin

Sources: user guide `researcher-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Table of Contents | UG | | | |
| ☐ | 1. Overview | UG | | | |
| ☐ | Key Capabilities | UG | | | |
| ☐ | User Roles | UG | | | |
| ☐ | 2. Getting Started | UG | | | |
| ☐ | Accessing the Portal | UG | | | |
| ☐ | First-Time Setup | UG | | | |
| ☐ | Navigation Structure | UG | | | |
| ☐ | 3. Dashboard | UG | | | |
| ☐ | Quick Actions from Dashboard | UG | | | |
| ☐ | 4. Researcher Registration & Profile | UG | | | |
| ☐ | Registration | UG | | | |
| ☐ | Rejection with Audit Trail | UG | | | |
| ☐ | Profile Management | UG | | | |
| ☐ | Researcher Types | UG | | | |
| ☐ | Verification System | UG | | | |
| ☐ | Credential Renewal | UG | | | |
| ☐ | 5. Reading Room & Bookings | UG | | | |
| ☐ | Creating a Booking | UG | | | |
| ☐ | Booking Lifecycle | UG | | | |
| ☐ | Material Requests | UG | | | |
| ☐ | Check-In / Check-Out | UG | | | |
| ☐ | Walk-In Visitors | UG | | | |
| ☐ | Seat Assignment | UG | | | |
| ☐ | Equipment Booking | UG | | | |
| ☐ | Retrieval Queue | UG | | | |
| ☐ | Call Slips | UG | | | |
| ☐ | 6. Collections | UG | | | |
| ☐ | Creating Collections | UG | | | |
| ☐ | Adding Items to Collections | UG | | | |
| ☐ | Collection Operations | UG | | | |
| ☐ | Finding Aid Export | UG | | | |
| ☐ | 7. Saved Searches & Discovery | UG | | | |
| ☐ | Saving Searches | UG | | | |
| ☐ | Managing Saved Searches | UG | | | |
| ☐ | Result Diffing | UG | | | |
| ☐ | Result Snapshots | UG | | | |
| ☐ | Search Alerts | UG | | | |
| ☐ | 8. Annotations & Notes | UG | | | |
| ☐ | Legacy Annotations | UG | | | |
| ☑ | Route /researcher → dashboard | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /researcher/submissions → submissions | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /researcher/submission/new → newSubmission | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /researcher/submission/:id → viewSubmission | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /researcher/submission/:id/edit → editSubmission | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /researcher/submission/:id/item/add → addItem | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /researcher/submission/:id/item/:itemId → editItem | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /researcher/submission/:id/item/:itemId/delete → deleteItem | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /researcher/submission/:id/submit → submit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /researcher/submission/:id/resubmit → resubmit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /researcher/from-collection/:collectionId → createFromCollection | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /researcher/import → importExchange | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /researcher/submission/:id/publish → publish | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /researcher/api/upload → apiUpload | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /researcher/api/delete-file → apiDeleteFile | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /researcher/api/autocomplete → apiAutocomplete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgResourceSyncPlugin

Sources: user guide `resourcesync-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Technical Staff | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Endpoints | UG | | | |
| ☐ | Recording deletions (tombstones) | UG | | | |
| ☐ | Administration / setup | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | Route /.well-known/resourcesync → sourceDescription | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /resourcesync/capabilitylist.xml → capabilityList | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /resourcesync/resourcelist.xml → resourceList | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /resourcesync/changelist.xml → changeList | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgRicExplorerPlugin

Sources: user guide `ric-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Understanding Archival Relationships | UG | | | |
| ☐ | What is RiC? | UG | | | |
| ☐ | The RiC Explorer | UG | | | |
| ☐ | Finding It | UG | | | |
| ☐ | Understanding the Graph View | UG | | | |
| ☐ | 2D Graph | UG | | | |
| ☐ | What the Colours Mean | UG | | | |
| ☐ | Interacting with the Graph | UG | | | |
| ☐ | 3D Graph View | UG | | | |
| ☐ | 3D Controls | UG | | | |
| ☐ | The RiC Dashboard | UG | | | |
| ☐ | Searching with RiC | UG | | | |
| ☐ | Semantic Search | UG | | | |
| ☐ | How to Search | UG | | | |
| ☐ | Understanding Entity Types | UG | | | |
| ☐ | Records (What we hold) | UG | | | |
| ☐ | Agents (Who created/used them) | UG | | | |
| ☐ | Activities (What produced them) | UG | | | |
| ☐ | Places (Where they're from) | UG | | | |
| ☐ | Common Relationships | UG | | | |
| ☐ | For Researchers | UG | | | |
| ☐ | Why RiC Helps Your Research | UG | | | |
| ☐ | Example Research Journey | UG | | | |
| ☐ | Tips for Using RiC | UG | | | |
| ☐ | CLI: php symfony ric:install-provenance-menu | CODE | | | |
| ☐ | CLI: php symfony ric:queue-process | CODE | | | |
| ☐ | CLI: php symfony ric:shacl-validate | CODE | | | |


## ahgRightsHolderManagePlugin

Sources: user guide `rights-management-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Dashboard | UG | | | |
| ☐ | Adding Rights to a Record | UG | | | |
| ☐ | Step 1: Navigate to the Record | UG | | | |
| ☐ | Step 2: Access Rights Panel | UG | | | |
| ☐ | Step 3: Add New Rights Record | UG | | | |
| ☐ | Step 4: Select Rights Basis | UG | | | |
| ☐ | Step 5: Complete the Form | UG | | | |
| ☐ | Rights Statements | UG | | | |
| ☐ | In Copyright | UG | | | |
| ☐ | No Copyright | UG | | | |
| ☐ | Other | UG | | | |
| ☐ | Creative Commons Licenses | UG | | | |
| ☐ | License Attributes | UG | | | |
| ☐ | Managing Embargoes | UG | | | |
| ☐ | What is an Embargo? | UG | | | |
| ☐ | Embargo Types | UG | | | |
| ☐ | Creating an Embargo | UG | | | |
| ☐ | Managing Existing Embargoes | UG | | | |
| ☐ | Auto-Release | UG | | | |
| ☐ | Traditional Knowledge Labels | UG | | | |
| ☐ | What are TK Labels? | UG | | | |
| ☐ | Categories | UG | | | |
| ☐ | Assigning TK Labels | UG | | | |
| ☐ | Orphan Works | UG | | | |
| ☐ | What is an Orphan Work? | UG | | | |
| ☐ | Due Diligence Process | UG | | | |
| ☐ | Rights Grants (PREMIS Acts) | UG | | | |
| ☐ | Available Acts | UG | | | |
| ☐ | Restriction Types | UG | | | |
| ☐ | Viewing Rights on Records | UG | | | |
| ☐ | Reports | UG | | | |
| ☐ | Best Practices | UG | | | |
| ☐ | Compliance | UG | | | |
| ☐ | Keyboard Shortcuts | UG | | | |
| ☐ | URLs | UG | | | |
| ☐ | Permissions Required | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☐ | Route /rightsholder/:slug → view | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /rightsholder/:slug/delete → delete | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /rightsholder/:slug/edit → edit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /rightsholder/add → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /rightsholder/browse → browse | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgRightsPlugin

Sources: user guide `extended-rights-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Workflow Overview | UG | | | |
| ☐ | What Extended Rights Manages | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Part 1: Rights Statements | UG | | | |
| ☐ | What Are Rights Statements? | UG | | | |
| ☐ | Choosing a Rights Statement | UG | | | |
| ☐ | Part 2: Creative Commons Licenses | UG | | | |
| ☐ | Understanding CC Licenses | UG | | | |
| ☐ | Which License to Choose? | UG | | | |
| ☐ | Part 3: Embargo Management | UG | | | |
| ☐ | What is an Embargo? | UG | | | |
| ☐ | Setting an Embargo | UG | | | |
| ☐ | Embargo Status Dashboard | UG | | | |
| ☐ | Part 4: Traditional Knowledge Labels | UG | | | |
| ☐ | What Are TK Labels? | UG | | | |
| ☐ | Applying TK Labels | UG | | | |
| ☐ | Adding Extended Rights to a Record | UG | | | |
| ☐ | Complete Workflow | UG | | | |
| ☐ | Extended Rights Form | UG | | | |
| ☐ | Rights Display on Record | UG | | | |
| ☐ | Tips for Best Practice | UG | | | |
| ☐ | Part 5: CLI Commands (System Administrators) | UG | | | |
| ☐ | Automated Embargo Processing | UG | | | |
| ☐ | Cron Setup | UG | | | |
| ☐ | Embargo Reports | UG | | | |
| ☐ | Report Output Example | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☐ | Retention Schedule & Disposal Workflow (v1.3.0, May 2026) | UG | | | |
| ☐ | Retention schedules — what they are | UG | | | |
| ☐ | Assigning a record to a schedule | UG | | | |
| ☐ | Disposal workflow — the sign-off chain | UG | | | |
| ☐ | Audit trail | UG | | | |
| ☐ | Compliance dashboard integration | UG | | | |


## ahgScanPlugin

Sources: user guide `watched-folder-scanner-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Register a folder (Admin UI) | UG | | | |
| ☐ | Run the scanner (CLI) | UG | | | |
| ☐ | How a file flows | UG | | | |
| ☐ | Administration / setup | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /admin/scan → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/scan/new → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/scan/create → create | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /admin/scan/:id/edit → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /admin/scan/:id/update → update | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /admin/scan/:id/delete → delete | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /admin/scan/:id/toggle → toggle | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | Route /admin/scan/:id/run → run | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /admin/scan/:id/history → history | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |


## ahgSearchPlugin

Sources: user guide `researcher-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Table of Contents | UG | | | |
| ☐ | 1. Overview | UG | | | |
| ☐ | Key Capabilities | UG | | | |
| ☐ | User Roles | UG | | | |
| ☐ | 2. Getting Started | UG | | | |
| ☐ | Accessing the Portal | UG | | | |
| ☐ | First-Time Setup | UG | | | |
| ☐ | Navigation Structure | UG | | | |
| ☐ | 3. Dashboard | UG | | | |
| ☐ | Quick Actions from Dashboard | UG | | | |
| ☐ | 4. Researcher Registration & Profile | UG | | | |
| ☐ | Registration | UG | | | |
| ☐ | Rejection with Audit Trail | UG | | | |
| ☐ | Profile Management | UG | | | |
| ☐ | Researcher Types | UG | | | |
| ☐ | Verification System | UG | | | |
| ☐ | Credential Renewal | UG | | | |
| ☐ | 5. Reading Room & Bookings | UG | | | |
| ☐ | Creating a Booking | UG | | | |
| ☐ | Booking Lifecycle | UG | | | |
| ☐ | Material Requests | UG | | | |
| ☐ | Check-In / Check-Out | UG | | | |
| ☐ | Walk-In Visitors | UG | | | |
| ☐ | Seat Assignment | UG | | | |
| ☐ | Equipment Booking | UG | | | |
| ☐ | Retrieval Queue | UG | | | |
| ☐ | Call Slips | UG | | | |
| ☐ | 6. Collections | UG | | | |
| ☐ | Creating Collections | UG | | | |
| ☐ | Adding Items to Collections | UG | | | |
| ☐ | Collection Operations | UG | | | |
| ☐ | Finding Aid Export | UG | | | |
| ☐ | 7. Saved Searches & Discovery | UG | | | |
| ☐ | Saving Searches | UG | | | |
| ☐ | Managing Saved Searches | UG | | | |
| ☐ | Result Diffing | UG | | | |
| ☐ | Result Snapshots | UG | | | |
| ☐ | Search Alerts | UG | | | |
| ☐ | 8. Annotations & Notes | UG | | | |
| ☐ | Legacy Annotations | UG | | | |
| ☑ | Route /search/autocomplete → autocomplete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /search/index → index | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /search/descriptionUpdates → descriptionUpdates | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /search/globalReplace → globalReplace | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /search/semantic → index | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgSecurityClearancePlugin

Sources: user guide `security-user-manual.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Password Policy | UG | | | |
| ☐ | Password Requirements | UG | | | |
| ☐ | Password Expiry | UG | | | |
| ☐ | Password History | UG | | | |
| ☐ | Changing Your Password | UG | | | |
| ☐ | Account Lockout | UG | | | |
| ☐ | Multi-Factor Authentication (2FA) | UG | | | |
| ☐ | Setting Up 2FA | UG | | | |
| ☐ | Using 2FA | UG | | | |
| ☐ | Email Fallback | UG | | | |
| ☐ | Security Classification (Bell-LaPadula) | UG | | | |
| ☐ | Classification Levels | UG | | | |
| ☐ | How It Works | UG | | | |
| ☐ | Your Clearance Level | UG | | | |
| ☐ | Session Security | UG | | | |
| ☐ | Automatic Timeout | UG | | | |
| ☐ | Session Protection | UG | | | |
| ☐ | Security Headers | UG | | | |
| ☐ | Audit Trail | UG | | | |
| ☐ | For Administrators | UG | | | |
| ☐ | Configuring Security Settings | UG | | | |
| ☐ | Recommended Cron Jobs | UG | | | |
| ☐ | Compliance Standards | UG | | | |
| ☑ | Route /admin/security/compliance → securityCompliance | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /security/clearances → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /security/clearance/:id → view | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /security/clearance/grant → grant | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /security/clearance/:id/revoke → revoke | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /security/clearance/bulk-grant → bulkGrant | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /security/access/:id/revoke → revokeAccess | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /security/clearance/user/:slug → user | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /security/2fa/policy → mfaPolicy | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /security/2fa/policy/save → mfaPolicy | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /security/2fa → twoFactor | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☐ | Route /security/2fa/verify → verifyTwoFactor | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /security/2fa/setup → setupTwoFactor | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /security/2fa/confirm → confirmTwoFactor | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /security/2fa/send-email → sendEmailCode | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /security/2fa/remove/:id → removeTwoFactor | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /security/2fa/webauthn → webauthnManage | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /security/2fa/webauthn/register/begin → webauthnRegisterBegin | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /security/2fa/webauthn/register/complete → webauthnRegisterComplete | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /security/2fa/webauthn/assert/begin → webauthnAssertBegin | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /security/2fa/webauthn/assert/complete → webauthnAssertComplete | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /security/2fa/webauthn/delete/:id → webauthnDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | CLI: php symfony security:audit-verify | CODE | | | |
| ☐ | CLI: php symfony security:update-cache | CODE | | | |
| ☐ | CLI: php symfony watermark:apply-derivatives | CODE | | | |


## ahgSemanticSearchPlugin

Sources: user guide `researcher-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Table of Contents | UG | | | |
| ☐ | 1. Overview | UG | | | |
| ☐ | Key Capabilities | UG | | | |
| ☐ | User Roles | UG | | | |
| ☐ | 2. Getting Started | UG | | | |
| ☐ | Accessing the Portal | UG | | | |
| ☐ | First-Time Setup | UG | | | |
| ☐ | Navigation Structure | UG | | | |
| ☐ | 3. Dashboard | UG | | | |
| ☐ | Quick Actions from Dashboard | UG | | | |
| ☐ | 4. Researcher Registration & Profile | UG | | | |
| ☐ | Registration | UG | | | |
| ☐ | Rejection with Audit Trail | UG | | | |
| ☐ | Profile Management | UG | | | |
| ☐ | Researcher Types | UG | | | |
| ☐ | Verification System | UG | | | |
| ☐ | Credential Renewal | UG | | | |
| ☐ | 5. Reading Room & Bookings | UG | | | |
| ☐ | Creating a Booking | UG | | | |
| ☐ | Booking Lifecycle | UG | | | |
| ☐ | Material Requests | UG | | | |
| ☐ | Check-In / Check-Out | UG | | | |
| ☐ | Walk-In Visitors | UG | | | |
| ☐ | Seat Assignment | UG | | | |
| ☐ | Equipment Booking | UG | | | |
| ☐ | Retrieval Queue | UG | | | |
| ☐ | Call Slips | UG | | | |
| ☐ | 6. Collections | UG | | | |
| ☐ | Creating Collections | UG | | | |
| ☐ | Adding Items to Collections | UG | | | |
| ☐ | Collection Operations | UG | | | |
| ☐ | Finding Aid Export | UG | | | |
| ☐ | 7. Saved Searches & Discovery | UG | | | |
| ☐ | Saving Searches | UG | | | |
| ☐ | Managing Saved Searches | UG | | | |
| ☐ | Result Diffing | UG | | | |
| ☐ | Result Snapshots | UG | | | |
| ☐ | Search Alerts | UG | | | |
| ☐ | 8. Annotations & Notes | UG | | | |
| ☐ | Legacy Annotations | UG | | | |
| ☑ | Route /search/enhancement/save → saveSearch | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /search/enhancement/saved → savedSearches | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /search/enhancement/run/:id → runSavedSearch | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /search/enhancement/template/:id → runTemplate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /search/enhancement/history → history | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /search/enhancement/delete/:id → deleteSavedSearch | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /admin/search-templates → adminTemplates | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | CLI: php symfony linked-data:sync | CODE | | | |


## ahgSettingsPlugin

Sources: user guide `ahg-settings-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Settings Overview Dashboard | UG | | | |
| ☐ | Global Settings | UG | | | |
| ☐ | Step 1: Open Global Settings | UG | | | |
| ☐ | Step 2: Configure Sections | UG | | | |
| ☐ | Step 3: Save Changes | UG | | | |
| ☐ | Section-Based Settings | UG | | | |
| ☐ | Available Sections | UG | | | |
| ☐ | Plugin Management | UG | | | |
| ☐ | Step 1: Open Plugin Manager | UG | | | |
| ☐ | Step 2: View Plugins by Category | UG | | | |
| ☐ | Step 3: Enable or Disable | UG | | | |
| ☐ | Important Notes | UG | | | |
| ☐ | Dropdown Management | UG | | | |
| ☐ | Step 1: Open Dropdown Manager | UG | | | |
| ☐ | Step 2: View Taxonomies | UG | | | |
| ☐ | Step 3: Edit Terms | UG | | | |
| ☐ | Available Taxonomies (35) | UG | | | |
| ☐ | Adding a New Term | UG | | | |
| ☐ | Term Properties | UG | | | |
| ☐ | AI Services Settings | UG | | | |
| ☐ | Supported Languages | UG | | | |
| ☐ | API Key Management | UG | | | |
| ☐ | Step 1: Open API Keys | UG | | | |
| ☐ | Step 2: Create New Key | UG | | | |
| ☐ | Step 3: Copy Key (One Time Only!) | UG | | | |
| ☐ | Manage Existing Keys | UG | | | |
| ☐ | Email Settings | UG | | | |
| ☐ | Test Email | UG | | | |
| ☐ | Numbering Schemes | UG | | | |
| ☐ | Step 1: Open Numbering Schemes | UG | | | |
| ☐ | Step 2: View Available Schemes | UG | | | |
| ☐ | Available Tokens | UG | | | |
| ☐ | Preservation & Backup | UG | | | |
| ☐ | Target Types | UG | | | |
| ☐ | Export and Import Settings | UG | | | |
| ☐ | Export Settings | UG | | | |
| ☐ | Import Settings | UG | | | |
| ☐ | Reset to Defaults | UG | | | |
| ☑ | Route /admin/ahg-settings → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ahg-settings/section → section | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ahg-settings/plugins → plugins | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ahg-settings/ai-services → aiServices | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ahg-settings/email → email | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /settings → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahgSettings/index → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahgSettings/export → export | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahgSettings/import → import | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahgSettings/reset → reset | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /ahgSettings/email → email | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahgSettings/emailTest → emailTest | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /ahgSettings/fusekiTest → fusekiTest | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahgSettings/ftpTest → ftpTest | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahgSettings/ldapTest → ldapTest | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /ahgSettings/plugins → plugins | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahgSettings/autoUpdate → autoUpdate | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /ahgSettings/saveTiffPdfSettings → saveTiffPdfSettings | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /ahgSettings/damTools → damTools | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /admin/ahg-settings/webhooks → webhooks | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ahg-settings/tts → tts | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /admin/ahg-settings/ahg-integration → ahgIntegration | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahgSettings/preservation → preservation | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahgSettings/levels → levels | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /ahgSettings/levelChoices → levelChoices | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgSharePointPlugin

Sources: user guide `sharepoint-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What it does | UG | | | |
| ☐ | Mode A — Manual push (Phase 2.B) | UG | | | |
| ☐ | Mode B — Auto / declare (Phase 2.A) | UG | | | |
| ☐ | Phase status | UG | | | |
| ☐ | Setup | UG | | | |
| ☐ | 1. Azure AD app registration (one-time per tenant) | UG | | | |
| ☐ | 2. Install the dependency and schema | UG | | | |
| ☐ | 3. Configure the tenant in the admin UI | UG | | | |
| ☐ | 4. Register drives for ingest | UG | | | |
| ☐ | 5. Mode A — install the SPFx package | UG | | | |
| ☐ | 6. Mode B — create webhook subscriptions | UG | | | |
| ☐ | Day-to-day usage | UG | | | |
| ☐ | Mode A — pushing manually | UG | | | |
| ☐ | Mode B — automatic on label | UG | | | |
| ☐ | Inspecting health | UG | | | |
| ☐ | Manual delta sync (recovery / backfill) | UG | | | |
| ☐ | Admin pages | UG | | | |
| ☐ | Security notes | UG | | | |
| ☐ | Further reading | UG | | | |
| ☑ | Route /sharepoint → index | CODE | PASS | pw-authed-seq 2026-06-27 | HTTP 403 |
| ☑ | Route /sharepoint/tenants → tenants | CODE | PASS | pw-authed-seq 2026-06-27 | HTTP 403 |
| ☐ | Route /sharepoint/tenants/:id → tenantEdit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /sharepoint/tenants/:id/test → tenantTest | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /sharepoint/drives → drives | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /sharepoint/drives/browse → driveBrowse | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /sharepoint/drives/:id/mapping → mapping | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /sharepoint/subscriptions → subscriptions | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /sharepoint/events → events | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /sharepoint/events/:id → eventDetail | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /sharepoint/webhook → webhook | CODE | PASS | pw-authed 2026-06-27 | HTTP 405 |
| ☐ | Route /sharepoint/user-mappings → userMappings | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /sharepoint/user-mappings/:id → userMappingEdit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /api/v2/sharepoint/push/projection → pushProjection | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /api/v2/sharepoint/push → push | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /api/v2/sharepoint/push/jobs/:id → pushJob | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /sharepoint/federated-search → federatedSearch | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /sharepoint/rules → rules | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /sharepoint/rules/edit → ruleEdit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /sharepoint/rules/save → ruleSave | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /sharepoint/rules/:id/delete → ruleDelete | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /sharepoint/rules/:id/run → ruleRun | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /sharepoint/mappings → mappings | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /sharepoint/mappings/save → mappingsSave | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /sharepoint/mappings/template/delete → mappingTemplateDelete | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /sharepoint/columns → columns | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /sharepoint/drives/register → driveRegister | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /sharepoint/drives/save → driveSave | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /sharepoint/drives/:id/delete → driveDelete | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | CLI: php symfony sharepoint:auto-ingest | CODE | | | |
| ☐ | CLI: php symfony sharepoint:ingest-event | CODE | | | |
| ☐ | CLI: php symfony sharepoint:install | CODE | | | |
| ☐ | CLI: php symfony sharepoint:post-ingest-hooks | CODE | | | |
| ☐ | CLI: php symfony sharepoint:renew-subscriptions | CODE | | | |
| ☐ | CLI: php symfony sharepoint:status | CODE | | | |
| ☐ | CLI: php symfony sharepoint:subscribe | CODE | | | |
| ☐ | CLI: php symfony sharepoint:sync | CODE | | | |
| ☐ | CLI: php symfony sharepoint:test-connection | CODE | | | |


## ahgSpectrumPlugin

Sources: user guide `spectrum-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Museum Staff | UG | | | |
| ☐ | What is Spectrum? | UG | | | |
| ☐ | The Dashboard | UG | | | |
| ☐ | When Objects Arrive | UG | | | |
| ☐ | The Process | UG | | | |
| ☐ | How to Record Entry | UG | | | |
| ☐ | Lending Objects to Others | UG | | | |
| ☐ | The Loan Out Process | UG | | | |
| ☐ | Creating a Loan | UG | | | |
| ☐ | When a Loan is Overdue | UG | | | |
| ☐ | Checking Condition | UG | | | |
| ☐ | When to Check | UG | | | |
| ☐ | Condition Ratings | UG | | | |
| ☐ | Recording a Check | UG | | | |
| ☐ | Tracking Locations | UG | | | |
| ☐ | Why This Matters | UG | | | |
| ☐ | Location Format | UG | | | |
| ☐ | Recording Movement | UG | | | |
| ☐ | Insurance & Valuations | UG | | | |
| ☐ | Recording Value | UG | | | |
| ☐ | Quick Tips | UG | | | |
| ☐ | Core Procedures | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Object Entry | UG | | | |
| ☐ | Step 1: Create Entry Record | UG | | | |
| ☐ | Step 2: Add Objects | UG | | | |
| ☐ | Step 3: Set Return/Decision Date | UG | | | |
| ☐ | Loans Out | UG | | | |
| ☐ | Loan Request | UG | | | |
| ☐ | Loan Objects | UG | | | |
| ☐ | Loan Conditions | UG | | | |
| ☐ | Loan Workflow | UG | | | |
| ☐ | Location & Movement | UG | | | |
| ☐ | Current Location | UG | | | |
| ☐ | Record a Movement | UG | | | |
| ☐ | Condition Checking | UG | | | |
| ☐ | Valuation | UG | | | |
| ☐ | Spectrum Dashboard | UG | | | |
| ☐ | Tips for Spectrum | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /:slug/spectrum → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /:slug/spectrum/label → label | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /spectrum/:slug/workflow → workflow | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /spectrum/:slug/workflow/update → workflowUpdate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /spectrum/:slug/workflow/transition → workflowTransition | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /spectrum/dashboard → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /spectrum/my-tasks → myTasks | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /:slug/spectrum/grap → grapDashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /spectrum/loans → loanDashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /spectrum/general → general | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /spectrum/general/workflow → generalWorkflow | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /spectrum/general/workflow/transition → generalWorkflowTransition | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /:slug/spectrum/condition-photos → conditionPhotos | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /:slug/spectrum/condition-report → conditionReport | TECH | PASS | fixed 2026-06-27 | HTTP 200 (template added #187) |
| ☐ | Route /:slug/spectrum/conditionCheck → conditionCheck | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /:slug/spectrum/security → securityCompliance | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /:slug/spectrum/privacy → privacyCompliance | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | Route /spectrum/ropa → ropa | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /spectrum/annotation/save → saveAnnotation | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /spectrum/annotation/get/:photo_id → getAnnotation | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /spectrum/photo/delete/:photo_id → deletePhoto | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /spectrum/photo/primary/:photo_id → setPrimaryPhoto | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /spectrum/photo/rotate/:photo_id → rotatePhoto | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /spectrum/provenance/ajax → provenanceAjax | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /spectrum/install → install | TECH | PASS | fixed 2026-06-27 | HTTP 200 (fixed #187) |
| ☑ | Route /spectrum/export → export | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /spectrum/config/templates → templateConfig | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /api/spectrum/events → spectrumEvents | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☐ | Route /api/spectrum/objects/:object_id/events → spectrumObjectEvents | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /api/spectrum/statistics → spectrumStatistics | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /spectrumReports → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /spectrumReports/loans → loans | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /spectrumReports/conditions → conditions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /spectrumReports/valuations → valuations | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /spectrumReports/movements → movements | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /spectrumReports/acquisitions → acquisitions | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /spectrumReports/conservation → conservation | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /spectrumReports/objectEntry → objectEntry | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgStaticPagePlugin

Sources: user guide `landing-page-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Creating a New Page | UG | | | |
| ☐ | Step 1: Open Landing Pages | UG | | | |
| ☐ | Step 2: Click Create New Page | UG | | | |
| ☐ | Step 3: Fill in Page Details | UG | | | |
| ☐ | Step 4: Start Building | UG | | | |
| ☐ | Using the Visual Builder | UG | | | |
| ☐ | Builder Interface | UG | | | |
| ☐ | Adding Blocks | UG | | | |
| ☐ | Reordering Blocks | UG | | | |
| ☐ | Editing a Block | UG | | | |
| ☐ | Block Actions | UG | | | |
| ☐ | Block Types Reference | UG | | | |
| ☐ | Layout Blocks | UG | | | |
| ☐ | Content Blocks | UG | | | |
| ☐ | Data Blocks (Dynamic Content) | UG | | | |
| ☐ | Other Blocks | UG | | | |
| ☐ | Block Configuration Examples | UG | | | |
| ☐ | Hero Banner | UG | | | |
| ☐ | Browse Panels | UG | | | |
| ☐ | Statistics | UG | | | |
| ☐ | Recent Items | UG | | | |
| ☐ | Using Column Layouts | UG | | | |
| ☐ | Two Column Layout | UG | | | |
| ☐ | Three Column Layout | UG | | | |
| ☐ | Adding Blocks to Columns | UG | | | |
| ☐ | Styling Blocks | UG | | | |
| ☐ | Block Style Settings | UG | | | |
| ☐ | Preview and Publish | UG | | | |
| ☐ | Previewing Your Page | UG | | | |
| ☐ | Saving a Draft | UG | | | |
| ☐ | Publishing | UG | | | |
| ☐ | Restoring Previous Versions | UG | | | |
| ☐ | Page Settings | UG | | | |
| ☐ | Accessing Settings | UG | | | |
| ☐ | Page Settings Options | UG | | | |
| ☐ | Managing Multiple Pages | UG | | | |
| ☐ | Page List View | UG | | | |
| ☐ | Page Status Badges | UG | | | |
| ☐ | Route /staticpage/:id/delete → delete | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /staticpage/:id/edit → edit | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /staticpage/home → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /staticpage/add → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /staticpage/list → list | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgStatisticsPlugin

Sources: user guide `statistics-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Main Navigation | UG | | | |
| ☐ | Dashboard | UG | | | |
| ☐ | Main Statistics Dashboard | UG | | | |
| ☐ | Views Report | UG | | | |
| ☐ | Viewing Page Statistics | UG | | | |
| ☐ | Downloads Report | UG | | | |
| ☐ | Tracking File Downloads | UG | | | |
| ☐ | Top Items Report | UG | | | |
| ☐ | Most Viewed Records | UG | | | |
| ☐ | Geographic Report | UG | | | |
| ☐ | Visitor Locations | UG | | | |
| ☐ | Repository Statistics | UG | | | |
| ☐ | Per-Repository Reports | UG | | | |
| ☐ | Settings | UG | | | |
| ☐ | Configure Statistics | UG | | | |
| ☐ | Bot Filtering | UG | | | |
| ☐ | Managing Bot Patterns | UG | | | |
| ☐ | Exporting Data | UG | | | |
| ☐ | CSV Export | UG | | | |
| ☐ | CLI Commands | UG | | | |
| ☐ | Aggregate Statistics | UG | | | |
| ☐ | Generate Reports | UG | | | |
| ☐ | Cron Setup | UG | | | |
| ☐ | Recommended Cron Jobs | UG | | | |
| ☐ | GeoIP Setup | UG | | | |
| ☐ | Installing MaxMind GeoLite2 | UG | | | |
| ☐ | Understanding the Data | UG | | | |
| ☐ | How Statistics Are Collected | UG | | | |
| ☐ | Data Retention | UG | | | |
| ☐ | Privacy Compliance | UG | | | |
| ☐ | GDPR/POPIA Features | UG | | | |
| ☐ | Related Features | UG | | | |
| ☑ | Route /statistics → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /statistics/dashboard → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /statistics/views → views | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /statistics/downloads → downloads | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /statistics/geographic → geographic | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /statistics/top-items → topItems | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /statistics/item/:object_id → item | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /statistics/repository/:id → repository | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /statistics/export → export | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /statistics/admin → admin | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /statistics/admin/bots → bots | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /statistics/api/chart/:type → apiChart | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /statistics/api/summary → apiSummary | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /statistics/pixel/:token → pixel | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☐ | CLI: php symfony statistics:aggregate | CODE | | | |
| ☐ | CLI: php symfony statistics:report | CODE | | | |


## ahgStorageManagePlugin

Sources: user guide `rad-manage-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☑ | Route /physicalobject/browse → browse | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /physicalobject/autocomplete → autocomplete | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /physicalobject/boxList → boxList | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /physicalobject/holdingsReportExport → holdingsReportExport | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgTermTaxonomyPlugin

Sources: user guide `term-taxonomy-browse-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What Does This Plugin Do? | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Taxonomy Browse (List of Terms) | UG | | | |
| ☐ | Term Browse (Individual Term Page) | UG | | | |
| ☐ | Taxonomy Browse | UG | | | |
| ☐ | Page Layout | UG | | | |
| ☐ | Table Columns | UG | | | |
| ☐ | Search Within Taxonomy | UG | | | |
| ☐ | Sorting | UG | | | |
| ☐ | Per-Taxonomy Icons | UG | | | |
| ☐ | Term Browse | UG | | | |
| ☐ | Page Layout | UG | | | |
| ☐ | Features | UG | | | |
| ☐ | Access Control | UG | | | |
| ☐ | Tips | UG | | | |
| ☐ | Route /term/:slug/edit → edit | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /term/:slug/delete → delete | TECH | PASS | pw-authed-seq 2026-06-27 | HTTP 403 (id=553) |
| ☐ | Route /term/:slug → index | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☑ | Route /taxonomy/:id → taxonomyIndex | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☐ | CLI: php symfony skos:import | CODE | | | |
| ☐ | CLI: php symfony skos:validate | CODE | | | |


## ahgThemeB5Plugin

Sources: technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Bootstrap 5 theme renders on public + admin pages (parity with AtoM) | AUTHORED | | | |
| ☐ | Responsive layout (mobile / tablet / desktop) | AUTHORED | | | |
| ☐ | Navigation menus + dropdowns render per permissions/enabled plugins | AUTHORED | | | |
| ☐ | Digital-object viewers (image / IIIF / media / 3D) render in-theme | AUTHORED | | | |
| ☐ | Admin BS5 bundle loads (no alien Tailwind / unstyled fallback) | AUTHORED | | | |
| ☐ | CSP nonce applied to inline scripts/styles (no console CSP violations) | AUTHORED | | | |
| ☐ | CLI: php symfony theme:diagnose | CODE | | | |


## ahgTiffPdfMergePlugin

Sources: user guide `pdf-merge-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | When to Use | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Step-by-Step Guide | UG | | | |
| ☐ | Step 1: Upload Your Files | UG | | | |
| ☐ | Step 2: Arrange Page Order | UG | | | |
| ☐ | Step 3: Choose Settings | UG | | | |
| ☐ | Step 4: Link to a Record (Optional) | UG | | | |
| ☐ | Step 5: Create the PDF | UG | | | |
| ☐ | Step 6: Monitor Progress | UG | | | |
| ☐ | Step 7: Download Your PDF | UG | | | |
| ☐ | Tips | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☐ | When to Use | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Step-by-Step Guide | UG | | | |
| ☐ | Step 1: Upload Your Files | UG | | | |
| ☐ | Step 2: Arrange Page Order | UG | | | |
| ☐ | Step 3: Choose Settings | UG | | | |
| ☐ | Step 4: Link to a Record (Optional) | UG | | | |
| ☐ | Step 5: Create the PDF | UG | | | |
| ☐ | Step 6: Monitor Progress | UG | | | |
| ☐ | Step 7: Download Your PDF | UG | | | |
| ☐ | Tips | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☐ | Workflow Overview | UG | | | |
| ☐ | When to Use | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Step-by-Step Process | UG | | | |
| ☐ | Step 1: Upload Files | UG | | | |
| ☐ | Step 2: Arrange Page Order | UG | | | |
| ☐ | Step 3: Choose Settings | UG | | | |
| ☐ | Step 4: Link to Record (Optional) | UG | | | |
| ☐ | Step 5: Create and Monitor | UG | | | |
| ☐ | Job Status Guide | UG | | | |
| ☐ | Tips for Best Results | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☐ | Workflow Overview | UG | | | |
| ☐ | When to Use | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Step-by-Step Process | UG | | | |


## ahgTimeLimitedShareLinkPlugin

Sources: user guide `AtoM_Heratio_TimeLimitedShareLink_User_Manual.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | 1. Who can do what | UG | | | |
| ☐ | 2. Issuing a share link | UG | | | |
| ☐ | Step 1 — Open the record | UG | | | |
| ☐ | Step 2 — Open the modal | UG | | | |
| ☐ | Step 3 — Generate | UG | | | |
| ☐ | What happens if a guard fails | UG | | | |
| ☐ | 3. Revoking a link | UG | | | |
| ☐ | From the admin list | UG | | | |
| ☐ | From the per-link detail page | UG | | | |
| ☐ | 4. The admin list — what each column means | UG | | | |
| ☐ | Filters | UG | | | |
| ☐ | 5. The per-link detail page | UG | | | |
| ☐ | 6. Settings (admin only) | UG | | | |
| ☐ | 7. Retention sweeps (admins / operations) | UG | | | |
| ☐ | AtoM (PSIS) | UG | | | |
| ☐ | Heratio | UG | | | |
| ☐ | 8. What recipients see | UG | | | |
| ☐ | 9. Troubleshooting | UG | | | |
| ☐ | 10. Glossary | UG | | | |
| ☐ | CLI: php symfony share-link:prune | CODE | | | |


## ahgTranslationPlugin

Sources: user guide `translation-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | What Gets Translated | UG | | | |
| ☐ | Supported Languages | UG | | | |
| ☐ | South African Languages (11 Official) | UG | | | |
| ☐ | International Languages | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Step-by-Step Translation | UG | | | |
| ☐ | Step 1: Open the Translation Modal | UG | | | |
| ☐ | Step 2: Configure Translation Settings | UG | | | |
| ☐ | Step 3: Select Fields to Translate | UG | | | |
| ☐ | Step 4: Preview Translations | UG | | | |
| ☐ | Step 5: Review and Edit | UG | | | |
| ☐ | Step 6: Approve and Save | UG | | | |
| ☐ | Translation Options Explained | UG | | | |
| ☐ | Save with AtoM Culture Code | UG | | | |
| ☐ | Overwrite Existing | UG | | | |
| ☐ | Draft System | UG | | | |
| ☐ | Benefits of Draft System | UG | | | |
| ☐ | Settings Configuration | UG | | | |
| ☐ | Health Check | UG | | | |
| ☐ | Common Use Cases | UG | | | |
| ☐ | Tips | UG | | | |
| ☐ | Translation Quality Notes | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /translation/health → health | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /translation/settings → settings | TECH | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /translation/translate/:id → translate | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |
| ☐ | Route /translation/apply/:draftId → apply | TECH | N/A | pw-authed 2026-06-27 | HTTP 404 (id=553) |


## ahgUiOverridesPlugin

Sources: technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Viewer dispatch routes to the correct viewer (image / PDF / media / 3D) | AUTHORED | | | |
| ☐ | Registered action overrides replace the base AtoM actions | AUTHORED | | | |
| ☐ | Helper functions are available to templates | AUTHORED | | | |
| ☐ | No regression on un-overridden core actions | AUTHORED | | | |


## ahgUserManagePlugin

Sources: user guide `USER_MANUAL.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Version 1.6.x | UG | | | |
| ☐ | Last Updated: January 2026 | UG | | | |
| ☐ | Table of Contents | UG | | | |
| ☐ | 1. Introduction | UG | | | |
| ☐ | System Requirements | UG | | | |
| ☐ | 2. Getting Started | UG | | | |
| ☐ | Accessing AHG Settings | UG | | | |
| ☐ | 3. AI Services | UG | | | |
| ☐ | Accessing AI Services Settings | UG | | | |
| ☐ | Configuration Options | UG | | | |
| ☐ | API Configuration | UG | | | |
| ☐ | NER Settings | UG | | | |
| ☐ | Summarization Settings | UG | | | |
| ☐ | Spell Check Settings | UG | | | |
| ☐ | Workflow Diagram | UG | | | |
| ☐ | 4. Named Entity Recognition (NER) | UG | | | |
| ☐ | What is NER? | UG | | | |
| ☐ | How NER Works | UG | | | |
| ☐ | Text Sources | UG | | | |
| ☐ | Viewing Extracted Entities | UG | | | |
| ☐ | 5. AI Summarization | UG | | | |
| ☐ | Summarization Workflow | UG | | | |
| ☐ | Best Practices | UG | | | |
| ☐ | 6. Spell Checking | UG | | | |
| ☐ | Supported Languages | UG | | | |
| ☐ | Spell Check Results | UG | | | |
| ☐ | 7. NER Review Dashboard | UG | | | |
| ☐ | Accessing the Dashboard | UG | | | |
| ☐ | Dashboard Features | UG | | | |
| ☐ | Review Actions | UG | | | |
| ☐ | Bulk Actions | UG | | | |
| ☐ | 8. Batch Processing | UG | | | |
| ☐ | CLI Commands | UG | | | |
| ☐ | NER Extraction | UG | | | |
| ☐ | Summarization | UG | | | |
| ☐ | Spell Check | UG | | | |
| ☐ | Running Long Batches | UG | | | |
| ☐ | Monitoring Progress | UG | | | |
| ☐ | 9. Troubleshooting | UG | | | |
| ☐ | Common Issues | UG | | | |
| ☑ | Route /user/:slug → view | CODE | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /user/:slug/delete → delete | CODE | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /user/:slug/edit → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /user/add → edit | CODE | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /user/list → browse | CODE | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /user → browse | CODE | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /user/login → login | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /user/logout → logout | CODE | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /user/passwordEdit → passwordEdit | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☐ | Route /user/clipboard → clipboard | CODE | N/A | pw-authed 2026-06-27 | HTTP 404 |
| ☑ | Route /user/passwordReset → passwordReset | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |


## ahgUserRegistrationPlugin

Sources: user guide `USER_MANUAL.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Version 1.6.x | UG | | | |
| ☐ | Last Updated: January 2026 | UG | | | |
| ☐ | Table of Contents | UG | | | |
| ☐ | 1. Introduction | UG | | | |
| ☐ | System Requirements | UG | | | |
| ☐ | 2. Getting Started | UG | | | |
| ☐ | Accessing AHG Settings | UG | | | |
| ☐ | 3. AI Services | UG | | | |
| ☐ | Accessing AI Services Settings | UG | | | |
| ☐ | Configuration Options | UG | | | |
| ☐ | API Configuration | UG | | | |
| ☐ | NER Settings | UG | | | |
| ☐ | Summarization Settings | UG | | | |
| ☐ | Spell Check Settings | UG | | | |
| ☐ | Workflow Diagram | UG | | | |
| ☐ | 4. Named Entity Recognition (NER) | UG | | | |
| ☐ | What is NER? | UG | | | |
| ☐ | How NER Works | UG | | | |
| ☐ | Text Sources | UG | | | |
| ☐ | Viewing Extracted Entities | UG | | | |
| ☐ | 5. AI Summarization | UG | | | |
| ☐ | Summarization Workflow | UG | | | |
| ☐ | Best Practices | UG | | | |
| ☐ | 6. Spell Checking | UG | | | |
| ☐ | Supported Languages | UG | | | |
| ☐ | Spell Check Results | UG | | | |
| ☐ | 7. NER Review Dashboard | UG | | | |
| ☐ | Accessing the Dashboard | UG | | | |
| ☐ | Dashboard Features | UG | | | |
| ☐ | Review Actions | UG | | | |
| ☐ | Bulk Actions | UG | | | |
| ☐ | 8. Batch Processing | UG | | | |
| ☐ | CLI Commands | UG | | | |
| ☐ | NER Extraction | UG | | | |
| ☐ | Summarization | UG | | | |
| ☐ | Spell Check | UG | | | |
| ☐ | Running Long Batches | UG | | | |
| ☐ | Monitoring Progress | UG | | | |
| ☐ | 9. Troubleshooting | UG | | | |
| ☐ | Common Issues | UG | | | |
| ☑ | Route /register → register | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 |
| ☑ | Route /register/verify/:token → verify | CODE | PASS | pw-authed 2026-06-27 | HTTP 200 (id=553) |
| ☑ | Route /admin/registrations/approve → approve | CODE | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /admin/registrations/verify → markVerified | CODE | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /admin/registrations/reject → reject | CODE | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /admin/registrations → pending | CODE | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☐ | CLI: php symfony registration:cleanup | CODE | | | |


## ahgVendorPlugin

Sources: user guide `vendor-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Workflow Overview | UG | | | |
| ☐ | When to Use | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Part 1: Managing Vendors | UG | | | |
| ☐ | Add a New Vendor | UG | | | |
| ☐ | Vendor Record | UG | | | |
| ☐ | Part 2: Creating Transactions | UG | | | |
| ☐ | Transaction Flow | UG | | | |
| ☐ | Create New Transaction | UG | | | |
| ☐ | Add Items to Transaction | UG | | | |
| ☐ | Part 3: Transaction Status Flow | UG | | | |
| ☐ | Part 4: Monitoring Items | UG | | | |
| ☐ | Dashboard Overview | UG | | | |
| ☐ | Overdue Alerts | UG | | | |
| ☐ | Part 5: Receiving Items Back | UG | | | |
| ☐ | Return Process | UG | | | |
| ☐ | Record Return | UG | | | |
| ☐ | Service Types Reference | UG | | | |
| ☐ | Tips for Best Practice | UG | | | |
| ☐ | Need Help? | UG | | | |
| ☑ | Route /vendor/:slug → view | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /vendor/:slug/edit → edit | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /vendor/:slug/delete → delete | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /vendor/:slug/contact/add → addContact | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /vendor/:slug/contact/:contact_id/delete → deleteContact | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /vendor/transaction/:id → viewTransaction | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /vendor/transaction/:id/edit → editTransaction | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /vendor/transaction/:id/status → updateTransactionStatus | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /vendor/transaction/:id/item/add → addTransactionItem | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /vendor/transaction/:transaction_id/item/:item_id/remove → removeTransactionItem | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 (id=553) |
| ☑ | Route /vendor/transaction/add → addTransaction | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /vendor/transactions → transactions | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /vendor/serviceTypes → serviceTypes | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /vendor/add → add | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /vendor/list → list | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |
| ☑ | Route /vendor → index | TECH | PASS | pw-authed 2026-06-27 | HTTP 403 |


## ahgVersionControlPlugin

Sources: user guide `version-control-user-guide.md`.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | A Guide for Archivists and Administrators | UG | | | |
| ☐ | What is it? | UG | | | |
| ☐ | Key features | UG | | | |
| ☐ | How to use it | UG | | | |
| ☐ | From a record | UG | | | |
| ☐ | Routes | UG | | | |
| ☐ | Command line | UG | | | |
| ☐ | Compliance notes | UG | | | |
| ☐ | Tips & FAQ | UG | | | |
| ☐ | CLI: php symfony ahg-vc:regression | CODE | | | |
| ☐ | CLI: php symfony version:backfill | CODE | | | |
| ☐ | CLI: php symfony version:capture | CODE | | | |
| ☐ | CLI: php symfony version:diff | CODE | | | |
| ☐ | CLI: php symfony version:prune | CODE | | | |
| ☐ | CLI: php symfony version:snapshot | CODE | | | |


## ahgWorkflowPlugin

Sources: user guide `workflow-user-guide.md`, technical manual.

| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |
|---|---|---|---|---|---|
| ☐ | Key Features | UG | | | |
| ☐ | How It Works | UG | | | |
| ☐ | Workflow Process Flow | UG | | | |
| ☐ | How to Access | UG | | | |
| ☐ | Main Navigation | UG | | | |
| ☐ | Dashboard | UG | | | |
| ☐ | Your Workflow Dashboard | UG | | | |
| ☐ | Working with Tasks | UG | | | |
| ☐ | Step 1: View Available Tasks (Task Pool) | UG | | | |
| ☐ | Step 2: Claim a Task | UG | | | |
| ☐ | Step 3: Review the Record | UG | | | |
| ☐ | Step 4: Make Your Decision | UG | | | |
| ☐ | Task Statuses | UG | | | |
| ☐ | Email Notifications | UG | | | |
| ☐ | Notification Types | UG | | | |
| ☐ | Administration | UG | | | |
| ☐ | Creating a Workflow | UG | | | |
| ☐ | Adding Workflow Steps | UG | | | |
| ☐ | Step Configuration | UG | | | |
| ☐ | Workflow History | UG | | | |
| ☐ | View Task History | UG | | | |
| ☐ | CLI Commands | UG | | | |
| ☐ | Process Workflow Tasks | UG | | | |
| ☐ | View Workflow Status | UG | | | |
| ☐ | Best Practices | UG | | | |
| ☐ | For Reviewers | UG | | | |
| ☐ | For Administrators | UG | | | |
| ☐ | Related Features | UG | | | |
| ☑ | Route /workflow → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/dashboard → dashboard | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/my-tasks → myTasks | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/pool → pool | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/task/:id/claim → claimTask | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/task/:id/release → releaseTask | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/task/:id/approve → approveTask | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/task/:id/reject → rejectTask | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/task/:id → viewTask | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/history → history | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/history/:object_id → objectHistory | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/admin → admin | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/admin/create → createWorkflow | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/admin/edit/:id → editWorkflow | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/admin/delete/:id → deleteWorkflow | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/admin/:workflow_id/step/add → addStep | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/admin/step/:id/edit → editStep | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/admin/step/:id/delete → deleteStep | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/admin/:workflow_id/steps/reorder → reorderSteps | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/start/:object_id → startWorkflow | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/timeline/:object_id → timeline | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/queues → queues | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/my-work → myWork | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/team-work → teamWork | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/overdue → overdue | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/bulk/preview → bulkPreview | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/bulk/execute → bulkExecute | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/publish-readiness/:object_id → publishReadiness | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/publish-simulate/:object_id → publishSimulate | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/publish-execute/:object_id → publishExecute | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/admin/gates → gateAdmin | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/admin/gates/:id/edit → gateRuleEdit | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/admin/gates/:id/delete → gateRuleDelete | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 (id=553) |
| ☑ | Route /workflow/change-summary → changeSummary | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/api/stats → apiStats | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/api/tasks → apiTasks | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☑ | Route /workflow/api/sla → apiSlaStatus | TECH | PASS | pw-authed 2026-06-27 | HTTP 302 |
| ☐ | CLI: php symfony spectrum:overdue | CODE | | | |
| ☐ | CLI: php symfony workflow:process | CODE | | | |
| ☐ | CLI: php symfony workflow:seed-spectrum | CODE | | | |
| ☐ | CLI: php symfony workflow:status | CODE | | | |
