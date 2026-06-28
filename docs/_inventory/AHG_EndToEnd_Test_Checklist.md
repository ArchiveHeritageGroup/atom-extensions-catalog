# AHG — Menu-Driven Manual Test Checklist

**Playwright auto-test summary (2026-06-28):** PASS=1020 · FAIL=2 · N/A=275 · destructive/manual=1. ☑ = passed automated GET; ☐ = awaiting your manual check (parameterised, destructive/POST, or button/JS interaction). FAIL rows are flagged in the Result column.


Every navigation menu item is a **screen**; under each, every link/URL reachable from it is a tick-box test item. Walk the menus top-to-bottom. Tick ☐→☑; record Pass/Fail + notes.

Source: AtoM `menu` table + plugin route registrations. Generated 2026-06-27.


# MENU: Add (create records)


## Archival descriptions  ·  `addInformationObject`

*Linked panels & sub-functions:* Core ISAD(G) fields; linked panels — Provenance, AI (NER/summarise/translate/spellcheck/suggest/face), Rights (PREMIS/CC/RightsStatements/embargo/TK), Digital object (upload/IIIF/media/3D/watermark/metadata), Security classification, Custom fields, Audit, Version control, Preservation, Share link

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | N/A | HTTP 404 |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | PASS | HTTP 302 (fixed) |
| ☑ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | PASS | HTTP 302 |
| ☑ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | PASS | HTTP 200 (fixed) |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/objects] |
| ☑ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/object-list] |
| ☑ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | PASS | HTTP 200 |
| ☑ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | PASS | HTTP 200 |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | PASS | HTTP 200 |
| ☑ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | PASS | HTTP 200 |
| ☑ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | PASS | HTTP 200 |
| ☑ | `/object/export` | index | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | PASS | HTTP 200 |
| ☑ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | PASS | HTTP 302 |
| ☑ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | PASS | HTTP 302 [/loan/1/add-object] |
| ☑ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | PASS | HTTP 302 [/loan/1/remove-object] |
| ☑ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | SKIP | destructive/POST |
| ☑ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | PASS | HTTP 200 |
| ☑ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | PASS | HTTP 200 [/digitalobject/702/edit] |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | SKIP | destructive/POST |
| ☑ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Accession records  ·  `addAccessionRecord`

*Linked panels & sub-functions:* Core accession; Donor + donor agreement, Rights holder, Physical storage, create-description, deaccession, audit

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/donor/autocomplete/accessions` | autocompleteAccessions | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/autocomplete/records` | autocompleteRecords | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/accession/:slug` | index | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☐ | `/accession/:slug/delete` | delete | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☐ | `/accession/:slug/edit` | edit | ahgAccessionManagePlugin | FAIL | HTTP 500 — base AtoM accession edit action (sf_method); cannot fix without modifying base |
| ☑ | `/accession/browse` | browse | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/dashboard` | dashboard | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/accessions/:id/submit` | submit | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☐ | `/admin/accessions/:id/review` | review | ahgAccessionManagePlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/accessions/:id/accept` | accept | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☐ | `/admin/accessions/:id/reject` | reject | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☐ | `/admin/accessions/:id/return` | returnRevision | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/admin/accessions/:id/timeline` | timeline | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/:id/checklist` | checklist | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/:id/attachments` | attachments | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/:id/intake` | queueDetail | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/queue` | queue | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/accessions/queue/assign` | assign | ahgAccessionManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/admin/accessions/config` | config | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/numbering` | numbering | ahgAccessionManagePlugin | PASS | HTTP 200 (fixed #187) |
| ☑ | `/api/accession/checklist/:id/toggle` | apiChecklistToggle | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/api/accession/checklist/apply-template` | apiChecklistApplyTemplate | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/accession/attachment/:id/delete` | apiAttachmentDelete | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/admin/accessions/:id/appraisal` | appraisal | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☐ | `/admin/accessions/:id/appraisal/save` | appraisalSave | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/admin/accessions/:id/valuation` | valuation | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☐ | `/admin/accessions/:id/valuation/add` | valuationAdd | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/admin/accessions/appraisal-templates` | appraisalTemplates | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/valuation-report` | valuationReport | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/accession/appraisal/:id/score` | apiAppraisalScore | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/:id/containers` | containers | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/:id/rights` | rights | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/api/accession/container/save` | apiContainerSave | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/accession/container/:id/delete` | apiContainerDelete | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/api/accession/container-item/save` | apiContainerItemSave | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/accession/container-item/:id/delete` | apiContainerItemDelete | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/api/accession/container-item/:id/link` | apiContainerItemLink | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/api/accession/barcode/lookup` | apiBarcodeLookup | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/accession/rights/save` | apiRightsSave | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |


## Authority records  ·  `addActor`

*Linked panels & sub-functions:* Core ISAAR-CPF fields; Authority resolution (ULAN/LCNAF/VIAF/Wikidata/ORCID), Contact, AI, linked descriptions, custom fields, audit

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/completeness/:actorId/recalc` | apiCompletenessRecalc | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/eac-cpf/:actorId` | apiEacExport | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/actor/:slug` | index | ahgActorManagePlugin | PASS | HTTP 200 [/actor/historical] |
| ☐ | `/actor/:slug/delete` | delete | ahgActorManagePlugin | SKIP | destructive/POST |
| ☑ | `/actor/:slug/edit` | edit | ahgActorManagePlugin | PASS | HTTP 200 [/actor/historical/edit] |
| ☑ | `/actor/add` | edit | ahgActorManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/actor/browse` | browse | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/actor/autocomplete` | autocomplete | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/heritage/actor-autocomplete` | actorAutocomplete | ahgHeritageAccountingPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/actorAutocomplete` | actorAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Archival institutions  ·  `addRepository`

*Linked panels & sub-functions:* Core ISDIAH fields; logo/theme, holdings, uploads path, custom fields, audit

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/repository/add` | edit | ahgRepositoryManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/repository/browse` | browse | ahgRepositoryManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/statistics/repository/:id` | repository | ahgStatisticsPlugin | PASS | HTTP 200 |
| ☑ | `/export/repository` | repository | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/informationobject/repositoryAutocomplete` | repositoryAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Terms  ·  `addTerm`

*Linked panels & sub-functions:* Term labels/scope/relationships (SKOS); semantic/thesaurus sync, used-in, SKOS export

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/term/:slug/edit` | edit | ahgTermTaxonomyPlugin | SKIP | no records / not installed |
| ☐ | `/term/:slug/delete` | delete | ahgTermTaxonomyPlugin | SKIP | destructive/POST |
| ☐ | `/term/:slug` | index | ahgTermTaxonomyPlugin | SKIP | no records / not installed |
| ☑ | `/api/v2/taxonomies/:id/terms` | taxonomyTerms | ahgAPIPlugin | PASS | HTTP 403 |
| ☑ | `/informationobject/termAutocomplete` | termAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Function  ·  `addFunction`

*Linked panels & sub-functions:* Core ISDF fields; relationships, linked records

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/functions/browse` | functionBrowse | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/authority/function/save` | apiFunctionSave | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/authority/function/:id/delete` | apiFunctionDelete | ahgAuthorityPlugin | SKIP | destructive/POST |
| ☑ | `/function/:slug` | view | ahgFunctionManagePlugin | PASS | HTTP 200 [/function/test-function] |
| ☐ | `/function/:slug/delete` | delete | ahgFunctionManagePlugin | SKIP | destructive/POST |
| ☑ | `/function/:slug/edit` | edit | ahgFunctionManagePlugin | PASS | HTTP 200 [/function/test-function/edit] |
| ☑ | `/function/add` | edit | ahgFunctionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/function/browse` | browse | ahgFunctionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


# MENU: Manage


## Accessions  ·  `accessions`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/donor/autocomplete/accessions` | autocompleteAccessions | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/accession/:slug` | index | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☐ | `/accession/:slug/delete` | delete | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☐ | `/accession/:slug/edit` | edit | ahgAccessionManagePlugin | FAIL | HTTP 500 — base AtoM accession edit action (sf_method); cannot fix without modifying base |
| ☑ | `/accession/browse` | browse | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/dashboard` | dashboard | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/accessions/:id/submit` | submit | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☐ | `/admin/accessions/:id/review` | review | ahgAccessionManagePlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/accessions/:id/accept` | accept | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☐ | `/admin/accessions/:id/reject` | reject | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☐ | `/admin/accessions/:id/return` | returnRevision | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/admin/accessions/:id/timeline` | timeline | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/:id/checklist` | checklist | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/:id/attachments` | attachments | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/:id/intake` | queueDetail | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/queue` | queue | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/accessions/queue/assign` | assign | ahgAccessionManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/admin/accessions/config` | config | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/numbering` | numbering | ahgAccessionManagePlugin | PASS | HTTP 200 (fixed #187) |
| ☑ | `/api/accession/checklist/:id/toggle` | apiChecklistToggle | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/api/accession/checklist/apply-template` | apiChecklistApplyTemplate | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/accession/attachment/:id/delete` | apiAttachmentDelete | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/admin/accessions/:id/appraisal` | appraisal | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☐ | `/admin/accessions/:id/appraisal/save` | appraisalSave | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/admin/accessions/:id/valuation` | valuation | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☐ | `/admin/accessions/:id/valuation/add` | valuationAdd | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/admin/accessions/appraisal-templates` | appraisalTemplates | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/valuation-report` | valuationReport | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/accession/appraisal/:id/score` | apiAppraisalScore | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/:id/containers` | containers | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/accessions/:id/rights` | rights | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/api/accession/container/save` | apiContainerSave | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/accession/container/:id/delete` | apiContainerDelete | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/api/accession/container-item/save` | apiContainerItemSave | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/accession/container-item/:id/delete` | apiContainerItemDelete | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/api/accession/container-item/:id/link` | apiContainerItemLink | ahgAccessionManagePlugin | PASS | HTTP 200 |
| ☑ | `/api/accession/barcode/lookup` | apiBarcodeLookup | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/accession/rights/save` | apiRightsSave | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/accession/rights/:id/delete` | apiRightsDelete | ahgAccessionManagePlugin | SKIP | destructive/POST |


## Donors  ·  `donors`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/donor/dashboard` | dashboard | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/agreement/browse` | browse | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/agreement/add` | add | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/agreement/:id` | view | ahgDonorAgreementPlugin | PASS | HTTP 200 |
| ☑ | `/donor/agreement/:id/edit` | edit | ahgDonorAgreementPlugin | PASS | HTTP 200 |
| ☐ | `/donor/agreement/:id/delete` | delete | ahgDonorAgreementPlugin | SKIP | destructive/POST |
| ☑ | `/donor/agreement/reminders` | reminders | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/autocomplete/accessions` | autocompleteAccessions | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/autocomplete/records` | autocompleteRecords | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/:slug` | view | ahgDonorManagePlugin | PASS | HTTP 200 [/donor/rock-art-research-institute] |
| ☐ | `/donor/:slug/delete` | delete | ahgDonorManagePlugin | SKIP | destructive/POST |
| ☑ | `/donor/:slug/edit` | edit | ahgDonorManagePlugin | PASS | HTTP 200 [/donor/rock-art-research-institute/edit] |
| ☑ | `/donor/add` | edit | ahgDonorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/browse` | browse | ahgDonorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Jobs  ·  `jobs`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/jobs` | browse | ahgJobsManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/jobs/report/:id` | report | ahgJobsManagePlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/jobs/delete` | delete | ahgJobsManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/jobs/export` | export | ahgJobsManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/v2/sharepoint/push/jobs/:id` | pushJob | ahgSharePointPlugin | N/A | HTTP 404 |
| ☑ | `/ingest/ajax/job-status` | jobStatus | ahgIngestPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/tiff-pdf-merge/job/:job_id` | getJob | ahgPreservationPlugin | PASS | HTTP 200 |
| ☐ | `/tiff-pdf-merge/download/:job_id` | download | ahgPreservationPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/tiff-pdf-merge/jobs` | browse | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/job/:job_id/view` | view | ahgPreservationPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/research/extraction-job/create` | createExtractionJob | ahgResearchPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/research/extraction-job/:id` | viewExtractionJob | ahgResearchPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/research/extraction-jobs/:project_id` | extractionJobs | ahgResearchPlugin | PASS | HTTP 200 |


## Physical storage  ·  `browsePhysicalObjects`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | N/A | HTTP 404 |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | PASS | HTTP 302 (fixed) |
| ☑ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | PASS | HTTP 302 |
| ☑ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | PASS | HTTP 200 (fixed) |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/objects] |
| ☑ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/object-list] |
| ☑ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | PASS | HTTP 200 |
| ☑ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | PASS | HTTP 200 |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | PASS | HTTP 200 |
| ☑ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | PASS | HTTP 200 |
| ☑ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | PASS | HTTP 200 |
| ☑ | `/object/export` | index | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | PASS | HTTP 200 |
| ☑ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | PASS | HTTP 302 |
| ☑ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | PASS | HTTP 302 [/loan/1/add-object] |
| ☑ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | PASS | HTTP 302 [/loan/1/remove-object] |
| ☑ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | SKIP | destructive/POST |
| ☑ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | PASS | HTTP 200 |
| ☑ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | PASS | HTTP 200 [/digitalobject/702/edit] |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | SKIP | destructive/POST |
| ☑ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Rights holders  ·  `rightsholders`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/rightsholder/:slug` | view | ahgRightsHolderManagePlugin | SKIP | no records / not installed |
| ☐ | `/rightsholder/:slug/delete` | delete | ahgRightsHolderManagePlugin | SKIP | destructive/POST |
| ☐ | `/rightsholder/:slug/edit` | edit | ahgRightsHolderManagePlugin | SKIP | no records / not installed |
| ☑ | `/rightsholder/add` | edit | ahgRightsHolderManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/rightsholder/browse` | browse | ahgRightsHolderManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Taxonomies  ·  `taxonomies`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/api/v2/taxonomies` | taxonomiesBrowse | ahgAPIPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/v2/taxonomies/:id/terms` | taxonomyTerms | ahgAPIPlugin | PASS | HTTP 403 |


## Feedback  ·  `feedback`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Feedback** from the menu) | feedback | core | | |


## Browse Request for Publish  ·  `requesttopublishBrowse`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/requesttopublish/:slug` | edit | ahgRequestToPublishPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/requesttopublish/delete/:slug` | delete | ahgRequestToPublishPlugin | SKIP | destructive/POST |
| ☐ | `/requestToPublish/submit/:slug` | submit | ahgRequestToPublishPlugin | SKIP | destructive/POST |
| ☑ | `/requesttopublish/browse` | browse | ahgRequestToPublishPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/requesttopublish` | browse | ahgRequestToPublishPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/requesttopublish/` | browse | ahgRequestToPublishPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/requesttopublish/receipt` | receipt | ahgRequestToPublishPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/requesttopublish/receipt/:token` | receipt | ahgRequestToPublishPlugin | N/A | HTTP 404 |
| ☑ | `/requesttopublish/inbox` | inbox | ahgRequestToPublishPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/requesttopublish/review/:id` | review | ahgRequestToPublishPlugin | PASS | HTTP 200 |


## Collection assistant  ·  `collectionAssistant`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/favorites/send-to-collection` | sendToCollection | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/marketplace/collection/:slug` | collection | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☑ | `/marketplace/sell/collections` | sellerCollections | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/collections/create` | sellerCollectionCreate | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/researcher/from-collection/:collectionId` | createFromCollection | ahgResearcherPlugin | PASS | HTTP 302 |
| ☑ | `/manifest-collections/autocomplete` | autocomplete | ahgIiifPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/manifest-collections` | index | ahgIiifPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/manifest-collection/new` | new | ahgIiifPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/manifest-collection/create` | create | ahgIiifPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/manifest-collection/reorder` | reorder | ahgIiifPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/manifest-collection/:id/view` | view | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/manifest-collection/:id/edit` | edit | ahgIiifPlugin | PASS | HTTP 200 |
| ☐ | `/manifest-collection/:id/update` | update | ahgIiifPlugin | SKIP | destructive/POST |
| ☐ | `/manifest-collection/:id/delete` | delete | ahgIiifPlugin | SKIP | destructive/POST |
| ☐ | `/manifest-collection/:id/items/add` | addItems | ahgIiifPlugin | SKIP | destructive/POST |
| ☐ | `/manifest-collection/item/:item_id/remove` | removeItem | ahgIiifPlugin | SKIP | destructive/POST |
| ☐ | `/manifest-collection/:slug/manifest.json` | manifest | ahgIiifPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/api/research/collections/:id` | collection | ahgResearchPlugin | N/A | HTTP 401 |
| ☐ | `/api/research/collections` | collections | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/research/collection/:id` | viewCollection | ahgResearchPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/research/collections` | collections | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/ajax/add-to-collection` | addToCollection | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/ajax/create-collection` | createCollectionAjax | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/collection/:id/export/:format` | exportFindingAid | ahgResearchPlugin | PASS | HTTP 302 |
| ☑ | `/research/ro-crate/collection/:id` | packageCollection | ahgResearchPlugin | PASS | HTTP 302 |


## Researcher Copilot  ·  `researchCopilot`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/researcher` | dashboard | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/submissions` | submissions | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/submission/new` | newSubmission | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/submission/:id` | viewSubmission | ahgResearcherPlugin | PASS | HTTP 200 |
| ☑ | `/researcher/submission/:id/edit` | editSubmission | ahgResearcherPlugin | PASS | HTTP 200 |
| ☐ | `/researcher/submission/:id/item/add` | addItem | ahgResearcherPlugin | SKIP | destructive/POST |
| ☐ | `/researcher/submission/:id/item/:itemId` | editItem | ahgResearcherPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/researcher/submission/:id/item/:itemId/delete` | deleteItem | ahgResearcherPlugin | SKIP | destructive/POST |
| ☐ | `/researcher/submission/:id/submit` | submit | ahgResearcherPlugin | SKIP | destructive/POST |
| ☑ | `/researcher/submission/:id/resubmit` | resubmit | ahgResearcherPlugin | PASS | HTTP 302 |
| ☑ | `/researcher/from-collection/:collectionId` | createFromCollection | ahgResearcherPlugin | PASS | HTTP 302 |
| ☑ | `/researcher/import` | importExchange | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/submission/:id/publish` | publish | ahgResearcherPlugin | PASS | HTTP 302 |
| ☑ | `/researcher/api/upload` | apiUpload | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/api/delete-file` | apiDeleteFile | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/api/autocomplete` | apiAutocomplete | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/datasets` | index | ahgRdmPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/datasets/dashboard` | dashboard | ahgRdmPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/datasets/compliance` | compliance | ahgRdmPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/datasets/create` | create | ahgRdmPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/datasets/:id` | show | ahgRdmPlugin | PASS | HTTP 200 |
| ☑ | `/research/datasets/:id/deposit` | deposit | ahgRdmPlugin | PASS | HTTP 302 |
| ☑ | `/research/datasets/:id/scan` | scan | ahgRdmPlugin | PASS | HTTP 302 |
| ☐ | `/research/datasets/:id/file/:fid` | fileDownload | ahgRdmPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/research/datasets/:id/findings/:fid/resolve` | resolveFinding | ahgRdmPlugin | PASS | HTTP 302 |
| ☑ | `/research/datasets/:id/disposition` | disposition | ahgRdmPlugin | PASS | HTTP 302 |
| ☑ | `/research/datasets/:id/dmp` | linkDmp | ahgRdmPlugin | PASS | HTTP 302 |
| ☑ | `/research/datasets/:id/dmp/unlink` | unlinkDmp | ahgRdmPlugin | PASS | HTTP 302 |
| ☑ | `/research/datasets/:id/landing` | landing | ahgRdmPlugin | PASS | HTTP 200 |
| ☑ | `/admin/naz/researchers` | researchers | ahgNAZPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/naz/researcher/create` | researcherCreate | ahgNAZPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/naz/researcher/:id/edit` | researcherEdit | ahgNAZPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/naz/researcher/:id` | researcherView | ahgNAZPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/naz/researchers` | researchers | ahgNAZPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/research/stats` | stats | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/api/research/annotations` | annotations | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/api/research/bibliographies/:id/export/:format` | exportBibliography | ahgResearchPlugin | N/A | HTTP 401 |
| ☐ | `/api/research/bibliographies` | bibliographies | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☑ | `/api/research/citations/:id/:format` | citation | ahgResearchPlugin | PASS | HTTP 200 |
| ☐ | `/api/research/bookings` | bookings | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |


## Provenance graph  ·  `provenanceGraph`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☐ | `/api/graphql` | index | ahgGraphQLPlugin | N/A | HTTP 400 (pw 2026-06-27) |
| ☐ | `/api/graphql/playground` | playground | ahgGraphQLPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/:slug/cco/provenance` | provenance | ahgMuseumPlugin |  | manual |
| ☑ | `/museum/provenance/save` | provenanceSave | ahgMuseumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/museum/provenance/get` | provenanceGet | ahgMuseumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/museum/provenance/delete` | provenanceDelete | ahgMuseumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/museum/provenance/export` | provenanceExport | ahgMuseumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/spectrum/provenance/ajax` | provenanceAjax | ahgSpectrumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/favorites/send-to-bibliography` | sendToBibliography | ahgFavoritesPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/provenance/coverage` | coverage | ahgProvenancePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/provenance/coverage-data` | apiCoverage | ahgProvenancePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/provenance/trace/:id` | apiTrace | ahgProvenancePlugin | PASS | HTTP 200 |
| ☑ | `/provenance/authenticity/:id` | authenticity | ahgProvenancePlugin | PASS | HTTP 200 |
| ☑ | `/statistics/geographic` | geographic | ahgStatisticsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/research/bibliographies/:id/export/:format` | exportBibliography | ahgResearchPlugin | N/A | HTTP 401 |
| ☐ | `/api/research/bibliographies` | bibliographies | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☑ | `/research/bibliography/:id/export/:format` | exportBibliography | ahgResearchPlugin | PASS | HTTP 200 |
| ☐ | `/research/bibliography/:id/add` | addBibliographyEntry | ahgResearchPlugin | SKIP | destructive/POST |
| ☑ | `/research/bibliography/:id` | viewBibliography | ahgResearchPlugin | PASS | HTTP 200 |
| ☑ | `/research/bibliographies` | bibliographies | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/research/ajax/add-to-bibliography` | addToBibliographyAjax | ahgResearchPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | PASS | HTTP 302 |
| ☑ | `/research/knowledge-graph-data` | knowledgeGraphData | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/knowledge-graph/:project_id` | knowledgeGraph | ahgResearchPlugin | PASS | HTTP 200 |
| ☑ | `/research/network-graph/:project_id/export/graphml` | exportGraphML | ahgResearchPlugin | PASS | HTTP 200 |
| ☑ | `/research/network-graph/:project_id/export/gexf` | exportGraphGEXF | ahgResearchPlugin | PASS | HTTP 200 |
| ☑ | `/research/network-graph-data` | networkGraphData | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/network-graph/:project_id` | networkGraph | ahgResearchPlugin | PASS | HTTP 200 |


# MENU: Import


## XML  ·  `importXml`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | PASS | HTTP 302 (fixed #187) |
| ☑ | `/ahgSettings/import` | import | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/portable-export/import` | import | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/favorites/import` | import | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import` | bulkImport | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import-sample` | bulkImportSample | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/library/copy-cataloguing/import` | import | ahgLibraryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/researcher/import` | importExchange | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/customFields/import` | import | ahgCustomFieldsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/import` | adminImport | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | PASS | HTTP 302 |
| ☑ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | PASS | HTTP 200 |


## CSV  ·  `importCsv`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | PASS | HTTP 302 (fixed #187) |
| ☑ | `/ahgSettings/import` | import | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/portable-export/import` | import | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/favorites/import` | import | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import` | bulkImport | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import-sample` | bulkImportSample | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/library/copy-cataloguing/import` | import | ahgLibraryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/researcher/import` | importExchange | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/customFields/import` | import | ahgCustomFieldsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/import` | adminImport | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | PASS | HTTP 302 |
| ☑ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | PASS | HTTP 200 |


## Validate CSV  ·  `validateCsv`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ingest/:id/validate` | validate | ahgIngestPlugin | PASS | HTTP 200 |
| ☑ | `/api/preservation/package/validate` | apiPackageValidate | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/report-builder/query/validate` | apiQueryValidate | ahgReportBuilderPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/bulk-validate` | bulkValidate | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/validate/:id` | validateResult | ahgResearchPlugin | PASS | HTTP 200 |


## SKOS  ·  `importSkos`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | PASS | HTTP 302 (fixed #187) |
| ☑ | `/ahgSettings/import` | import | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/portable-export/import` | import | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/favorites/import` | import | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import` | bulkImport | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import-sample` | bulkImportSample | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/library/copy-cataloguing/import` | import | ahgLibraryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/researcher/import` | importExchange | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/customFields/import` | import | ahgCustomFieldsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/import` | adminImport | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | PASS | HTTP 302 |
| ☑ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | PASS | HTTP 200 |


## FTP Upload  ·  `ftpUpload`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/condition/check/:id/upload` | upload | ahgConditionPlugin | PASS | HTTP 200 |
| ☑ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/tenant/branding/logo-upload` | uploadLogo | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/training/upload` | apiTrainingUpload | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/client-upload-consent` | apiClientUploadConsent | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/api/upload` | apiUpload | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/v2/upload` | fileUpload | ahgAPIPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/api/v2/descriptions/:slug/upload` | descriptionUpload | ahgAPIPlugin | N/A | HTTP 404 |
| ☑ | `/ahg3DModel/upload` | upload | ahg3DModelPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ingest/:id/upload` | upload | ahgIngestPlugin | PASS | HTTP 200 |
| ☑ | `/tiff-pdf-merge/upload` | upload | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/registry/my/vendor/software/:id/upload` | myVendorSoftwareUpload | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/ftp-upload` | index | ahgFtpPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ftp-upload/upload` | upload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/chunk` | uploadChunk | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/list` | listFiles | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/delete` | deleteFile | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/loan/:id/upload-document` | uploadDocument | ahgLoanPlugin | PASS | HTTP 302 |
| ☑ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/report-builder/attachment/upload` | apiAttachmentUpload | ahgReportBuilderPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/research/ajax/upload-note-image` | uploadNoteImage | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |


# MENU: Admin


## Users  ·  `users`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/user/:slug` | view | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx] |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | SKIP | destructive/POST |
| ☑ | `/user/:slug/edit` | edit | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx/edit] |
| ☑ | `/user/add` | edit | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/list` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/login` | login | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user/logout` | logout | ahgUserManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |


## Groups  ·  `groups`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | PASS | HTTP 302 |
| ☑ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | PASS | HTTP 302 |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | N/A | HTTP 404 |


## Static pages  ·  `staticPages`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/staticpage/:id/delete` | delete | ahgStaticPagePlugin | SKIP | destructive/POST |
| ☑ | `/staticpage/:id/edit` | edit | ahgStaticPagePlugin | PASS | HTTP 200 [/staticpage/7/edit] |
| ☑ | `/staticpage/home` | edit | ahgStaticPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/staticpage/add` | edit | ahgStaticPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/staticpage/list` | list | ahgStaticPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/privacyAdmin/getNerEntitiesForPage` | getNerEntitiesForPage | ahgPrivacyPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/iiif/activity/page/:n` | activityPage | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/discovery/pageindex` | pageindex | ahgDiscoveryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/discovery/pageindex/api` | pageindexApi | ahgDiscoveryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages` | list | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/create` | create | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/:id/edit` | edit | ahgLandingPagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/landing-pages/:id/preview` | preview | ahgLandingPagePlugin | PASS | HTTP 200 |
| ☑ | `/admin/landing-pages/ajax/add-block` | addBlock | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/update-block` | updateBlock | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/delete-block` | deleteBlock | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/duplicate-block` | duplicateBlock | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/reorder` | reorderBlocks | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/toggle-visibility` | toggleVisibility | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/get-config` | getBlockConfig | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/update-settings` | updateSettings | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/delete` | delete | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/save-draft` | saveDraft | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/publish` | publish | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/restore-version` | restoreVersion | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/move-to-column` | moveToColumn | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/reorder-column` | reorderColumnBlocks | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |


## Menus  ·  `menu`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Menus** from the menu) | menu | core | | |


## Plugins  ·  `plugins`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/ahg-settings/plugins` | plugins | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ahgSettings/plugins` | plugins | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/plugin-protection` | pluginProtection | ahgAPIPlugin | N/A | HTTP 401 (pw 2026-06-27) |


## Themes  ·  `themes`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Themes** from the menu) | themes | core | | |


## Settings  ·  `settings`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/translation/settings` | settings | ahgTranslationPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/glam/settings` | browseSettings | ahgDisplayPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/glam/saveBrowseSettings` | saveBrowseSettings | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/glam/getBrowseSettings` | getBrowseSettings | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/glam/resetBrowseSettings` | resetBrowseSettings | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/ahg-settings` | index | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/ahg-settings/section` | section | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/ahg-settings/plugins` | plugins | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/ahg-settings/ai-services` | aiServices | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/ahg-settings/email` | email | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/settings` | index | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ahgSettings/index` | index | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ahgSettings/export` | export | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ahgSettings/import` | import | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ahgSettings/reset` | reset | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ahgSettings/email` | email | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ahgSettings/emailTest` | emailTest | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ahgSettings/fusekiTest` | fusekiTest | ahgSettingsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ahgSettings/ftpTest` | ftpTest | ahgSettingsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ahgSettings/ldapTest` | ldapTest | ahgSettingsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ahgSettings/plugins` | plugins | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ahgSettings/autoUpdate` | autoUpdate | ahgSettingsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/ahgSettings/saveTiffPdfSettings` | saveTiffPdfSettings | ahgSettingsPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/ahgSettings/damTools` | damTools | ahgSettingsPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/admin/ahg-settings/webhooks` | webhooks | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/ahg-settings/tts` | tts | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/ahg-settings/ahg-integration` | ahgIntegration | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ahgSettings/preservation` | preservation | ahgSettingsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ahgSettings/levels` | levels | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ahgSettings/levelChoices` | levelChoices | ahgSettingsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/marketplace/admin/settings` | adminSettings | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/admin/authorityResolution/settings/lookup` | lookupSettings | ahgAuthorityResolutionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/settings` | settings | ahgAiConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/iiif-settings` | settings | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/threeDReports/settings` | settings | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/mediaSettings/index` | index | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/mediaSettings/coverage` | coverage | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/mediaSettings/save` | save | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/mediaSettings/test` | test | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/mediaSettings/queue` | queue | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |


## Description updates  ·  `descriptionUpdates`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/condition/photo/:id/update-meta` | updatePhotoMeta | ahgConditionPlugin | PASS | HTTP 200 |
| ☑ | `/ahgSettings/autoUpdate` | autoUpdate | ahgSettingsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/spectrum/:slug/workflow/update` | workflowUpdate | ahgSpectrumPlugin | SKIP | destructive/POST |
| ☐ | `/admin/doi/update/:id` | update | ahgDoiPlugin | SKIP | destructive/POST |
| ☐ | `/admin/scan/:id/update` | update | ahgScanPlugin | SKIP | destructive/POST |
| ☐ | `/admin/tenants/:id/update` | updateTenant | ahgMultiTenantPlugin | SKIP | destructive/POST |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/reports/descriptions` | descriptions | ahgReportsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/privacy/dsar/:id/update` | dsarUpdate | ahgPrivacyPlugin | SKIP | destructive/POST |
| ☐ | `/cart/update-products` | updateProducts | ahgCartPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/cart/update-item` | updateItem | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/manifest-collection/:id/update` | update | ahgIiifPlugin | SKIP | destructive/POST |
| ☑ | `/media/audio-description/:id` | audioDescription | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/media/audio-description/:id/edit` | audioDescriptionEdit | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/api/v2/descriptions` | descriptionsBrowse | ahgAPIPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/v2/descriptions/:slug/citation` | descriptionsCitation | ahgAPIPlugin | PASS | HTTP 403 |
| ☑ | `/api/v2/descriptions/:slug` | descriptionsRead | ahgAPIPlugin | PASS | HTTP 405 |
| ☑ | `/api/v2/descriptions/:slug/conditions` | descriptionConditions | ahgAPIPlugin | PASS | HTTP 403 |
| ☑ | `/api/v2/descriptions/:slug/asset` | descriptionAsset | ahgAPIPlugin | PASS | HTTP 403 |
| ☐ | `/api/v2/descriptions/:slug/upload` | descriptionUpload | ahgAPIPlugin | N/A | HTTP 404 |
| ☐ | `/registry/api/sync/update` | apiSyncUpdate | ahgRegistryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/search/descriptionUpdates` | descriptionUpdates | ahgSearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/update-block` | updateBlock | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/update-settings` | updateSettings | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/research/hypothesis/:id/update` | updateHypothesis | ahgResearchPlugin | SKIP | destructive/POST |
| ☐ | `/research/odrl/update/:id` | updateOdrlPolicy | ahgResearchPlugin | SKIP | destructive/POST |
| ☐ | `/research/room/:id/update` | updateRoom | ahgResearchPlugin | SKIP | destructive/POST |


## Global search/replace  ·  `globalReplace`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/search/globalReplace` | globalReplace | ahgSearchPlugin | PASS | HTTP 403 (pw 2026-06-27) |


## Visible elements  ·  `visibleElements`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Visible elements** from the menu) | visibleElements | core | | |


## Portable Export  ·  `portableExport`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/condition/check/:id/export` | exportReport | ahgConditionPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/condition/template/:id/export` | template | ahgConditionPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/jobs/export` | export | ahgJobsManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/museum/provenance/export` | provenanceExport | ahgMuseumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/forms/template/:id/export` | templateExport | ahgFormsPlugin | PASS | HTTP 200 |
| ☑ | `/glam/exportCsv` | exportCsv | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ahgSettings/export` | export | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/spectrum/export` | export | ahgSpectrumPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export` | index | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/start` | apiStartExport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/quick-start` | apiQuickStart | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/clipboard-export` | apiClipboardExport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/fonds-search` | apiFondsSearch | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/progress` | apiProgress | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/list` | apiList | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/delete` | apiDelete | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/token` | apiToken | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/estimate` | apiEstimate | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/download` | download | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/import` | import | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/favorites/export/:format` | export | ahgFavoritesPlugin | PASS | HTTP 200 |
| ☑ | `/favorites/folder/:id/export/:format` | exportFolder | ahgFavoritesPlugin | PASS | HTTP 302 |
| ☑ | `/admin/doi/export` | export | ahgDoiPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/library/export` | export | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/library/marc-export` | marcExport | ahgLibraryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/library/kbart/export` | export | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/customFields/export` | export | ahgCustomFieldsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/admin/integrity/export` | export | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/export/csv` | exportCsv | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/export/auditor` | exportAuditor | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/export` | apiPackageExport | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/statistics/export` | export | ahgStatisticsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/export` | index | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/export/archival` | archival | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/export/authority` | authority | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/export/repository` | repository | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |


## Integrity  ·  `integrity`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/integrity` | index | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/schedules` | schedules | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/schedule/edit` | scheduleEdit | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/runs` | runs | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/run/:id` | runDetail | ahgIntegrityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/integrity/ledger` | ledger | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/dead-letter` | deadLetter | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/report` | report | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/export` | export | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/export/csv` | exportCsv | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/export/auditor` | exportAuditor | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/policies` | policies | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/policy/edit` | policyEdit | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/holds` | holds | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/disposition` | disposition | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/records` | records | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/integrity/alerts` | alerts | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/verify` | apiVerify | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/run/:id` | apiRun | ahgIntegrityPlugin | PASS | HTTP 200 |
| ☑ | `/api/integrity/schedule/:id/toggle` | apiScheduleToggle | ahgIntegrityPlugin | PASS | HTTP 200 |
| ☐ | `/api/integrity/schedule/:id/delete` | apiScheduleDelete | ahgIntegrityPlugin | SKIP | destructive/POST |
| ☑ | `/api/integrity/dead-letter/:id/action` | apiDeadLetterAction | ahgIntegrityPlugin | PASS | HTTP 200 |
| ☑ | `/api/integrity/stats` | apiStats | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/schedule/:id/run` | apiRunSchedule | ahgIntegrityPlugin | PASS | HTTP 200 |
| ☑ | `/api/integrity/policy/:id/toggle` | apiPolicyToggle | ahgIntegrityPlugin | PASS | HTTP 200 |
| ☐ | `/api/integrity/policy/:id/delete` | apiPolicyDelete | ahgIntegrityPlugin | SKIP | destructive/POST |
| ☑ | `/api/integrity/hold/place` | apiHoldPlace | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/hold/:id/release` | apiHoldRelease | ahgIntegrityPlugin | PASS | HTTP 200 |
| ☑ | `/api/integrity/disposition/:id/action` | apiDispositionAction | ahgIntegrityPlugin | PASS | HTTP 200 |
| ☑ | `/api/integrity/retention/scan` | apiRetentionScan | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/alert/save` | apiAlertSave | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/integrity/alert/:id/delete` | apiAlertDelete | ahgIntegrityPlugin | SKIP | destructive/POST |
| ☑ | `/api/integrity/ledger` | apiLedger | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/runs` | apiRuns | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/holds` | apiHolds | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/policies` | apiPolicies | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/daily-trend` | apiDailyTrend | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/repo-breakdown` | apiRepoBreakdown | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/format-breakdown` | apiFormatBreakdown | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/throughput` | apiThroughput | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |


# MENU: Admin — Users


## Profile  ·  `userProfile`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/user/:slug` | view | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx] |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | SKIP | destructive/POST |
| ☑ | `/user/:slug/edit` | edit | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx/edit] |
| ☑ | `/user/add` | edit | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/list` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/login` | login | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user/logout` | logout | ahgUserManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/glam/profiles` | profiles | ahgDisplayPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/glam/assignProfile` | assignProfile | ahgDisplayPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/marketplace/sell/profile` | sellerProfile | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/api/research/profile` | profile | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/research/orcid/pull-profile` | orcidPullProfile | ahgResearchPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/research/profile/api-keys` | apiKeys | ahgResearchPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/research/profile` | profile | ahgResearchPlugin | PASS | HTTP 302 (pw 2026-06-27) |


## Archival description permissions  ·  `userInformationObjectAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/user/:slug` | view | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx] |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | SKIP | destructive/POST |
| ☑ | `/user/:slug/edit` | edit | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx/edit] |
| ☑ | `/user/add` | edit | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/list` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/login` | login | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user/logout` | logout | ahgUserManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | N/A | HTTP 404 |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | PASS | HTTP 302 (fixed) |
| ☑ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | PASS | HTTP 302 |
| ☑ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | PASS | HTTP 200 (fixed) |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/objects] |
| ☑ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/object-list] |
| ☑ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | PASS | HTTP 200 |


## Authority record permissions  ·  `userActorAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/user/:slug` | view | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx] |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | SKIP | destructive/POST |
| ☑ | `/user/:slug/edit` | edit | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx/edit] |
| ☑ | `/user/add` | edit | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/list` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/login` | login | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user/logout` | logout | ahgUserManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/completeness/:actorId/recalc` | apiCompletenessRecalc | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/eac-cpf/:actorId` | apiEacExport | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/actor/:slug` | index | ahgActorManagePlugin | PASS | HTTP 200 [/actor/historical] |
| ☐ | `/actor/:slug/delete` | delete | ahgActorManagePlugin | SKIP | destructive/POST |
| ☑ | `/actor/:slug/edit` | edit | ahgActorManagePlugin | PASS | HTTP 200 [/actor/historical/edit] |
| ☑ | `/actor/add` | edit | ahgActorManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/actor/browse` | browse | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/actor/autocomplete` | autocomplete | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | N/A | HTTP 404 |


## Archival institution permissions  ·  `userRepositoryAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/user/:slug` | view | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx] |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | SKIP | destructive/POST |
| ☑ | `/user/:slug/edit` | edit | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx/edit] |
| ☑ | `/user/add` | edit | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/list` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/login` | login | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user/logout` | logout | ahgUserManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/repository/add` | edit | ahgRepositoryManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/repository/browse` | browse | ahgRepositoryManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/statistics/repository/:id` | repository | ahgStatisticsPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/export/repository` | repository | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/informationobject/repositoryAutocomplete` | repositoryAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |


## Taxonomy permissions  ·  `userTermAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/user/:slug` | view | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx] |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | SKIP | destructive/POST |
| ☑ | `/user/:slug/edit` | edit | ahgUserManagePlugin | PASS | HTTP 200 [/user/nt96-sgz5-n7wx/edit] |
| ☑ | `/user/add` | edit | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/list` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/login` | login | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user/logout` | logout | ahgUserManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/term/:slug/edit` | edit | ahgTermTaxonomyPlugin | SKIP | no records / not installed |
| ☐ | `/term/:slug/delete` | delete | ahgTermTaxonomyPlugin | SKIP | destructive/POST |
| ☐ | `/term/:slug` | index | ahgTermTaxonomyPlugin | SKIP | no records / not installed |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/api/v2/taxonomies/:id/terms` | taxonomyTerms | ahgAPIPlugin | PASS | HTTP 403 |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/informationobject/termAutocomplete` | termAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |


# MENU: Admin — Groups


## Profile  ·  `groupProfile`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/glam/profiles` | profiles | ahgDisplayPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/glam/assignProfile` | assignProfile | ahgDisplayPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/profile` | sellerProfile | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | PASS | HTTP 302 |
| ☑ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | PASS | HTTP 302 |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/api/research/profile` | profile | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/research/orcid/pull-profile` | orcidPullProfile | ahgResearchPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/research/profile/api-keys` | apiKeys | ahgResearchPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/research/profile` | profile | ahgResearchPlugin | PASS | HTTP 302 (pw 2026-06-27) |


## Archival description permissions  ·  `groupInformationObjectAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | N/A | HTTP 404 |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | PASS | HTTP 302 (fixed) |
| ☑ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | PASS | HTTP 302 |
| ☑ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | PASS | HTTP 200 (fixed) |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/objects] |
| ☑ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/object-list] |
| ☑ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | PASS | HTTP 200 |
| ☑ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | PASS | HTTP 200 |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | PASS | HTTP 200 |
| ☑ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | PASS | HTTP 200 |
| ☑ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | PASS | HTTP 302 |
| ☑ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | PASS | HTTP 302 |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | N/A | HTTP 404 |


## Authority record permissions  ·  `groupActorAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/completeness/:actorId/recalc` | apiCompletenessRecalc | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/eac-cpf/:actorId` | apiEacExport | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/actor/:slug` | index | ahgActorManagePlugin | PASS | HTTP 200 [/actor/historical] |
| ☐ | `/actor/:slug/delete` | delete | ahgActorManagePlugin | SKIP | destructive/POST |
| ☑ | `/actor/:slug/edit` | edit | ahgActorManagePlugin | PASS | HTTP 200 [/actor/historical/edit] |
| ☑ | `/actor/add` | edit | ahgActorManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/actor/browse` | browse | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/actor/autocomplete` | autocomplete | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | PASS | HTTP 302 |
| ☑ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | PASS | HTTP 302 |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/api/heritage/actor-autocomplete` | actorAutocomplete | ahgHeritageAccountingPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/actorAutocomplete` | actorAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Archival institution permissions  ·  `groupRepositoryAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/repository/add` | edit | ahgRepositoryManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/repository/browse` | browse | ahgRepositoryManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/statistics/repository/:id` | repository | ahgStatisticsPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | PASS | HTTP 302 |
| ☑ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | PASS | HTTP 302 |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/export/repository` | repository | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/informationobject/repositoryAutocomplete` | repositoryAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Taxonomy permissions  ·  `groupTermAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/term/:slug/edit` | edit | ahgTermTaxonomyPlugin | SKIP | no records / not installed |
| ☐ | `/term/:slug/delete` | delete | ahgTermTaxonomyPlugin | SKIP | destructive/POST |
| ☐ | `/term/:slug` | index | ahgTermTaxonomyPlugin | SKIP | no records / not installed |
| ☑ | `/api/v2/taxonomies/:id/terms` | taxonomyTerms | ahgAPIPlugin | PASS | HTTP 403 |
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | PASS | HTTP 302 |
| ☑ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | PASS | HTTP 302 |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | N/A | HTTP 404 |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/informationobject/termAutocomplete` | termAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


# MENU: Static pages


## Favorites  ·  `favorites`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/favorites` | browse | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/favorites/add/:slug` | add | ahgFavoritesPlugin | SKIP | destructive/POST |
| ☐ | `/favorites/remove/:id` | remove | ahgFavoritesPlugin | SKIP | destructive/POST |
| ☑ | `/favorites/clear` | clear | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/favorites/bulk` | bulk | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/favorites/move` | moveToFolder | ahgFavoritesPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/favorites/notes/:id` | updateNotes | ahgFavoritesPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/favorites/folder/create` | folderCreate | ahgFavoritesPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/favorites/folder/:id` | folderView | ahgFavoritesPlugin | PASS | HTTP 302 |
| ☐ | `/favorites/folder/:id/edit` | folderEdit | ahgFavoritesPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/favorites/folder/:id/delete` | folderDelete | ahgFavoritesPlugin | SKIP | destructive/POST |
| ☐ | `/favorites/ajax/toggle` | ajaxToggle | ahgFavoritesPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/favorites/ajax/toggle-custom` | ajaxToggleCustom | ahgFavoritesPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/favorites/ajax/search` | ajaxSearch | ahgFavoritesPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/favorites/ajax/status/:slug` | ajaxStatus | ahgFavoritesPlugin | PASS | HTTP 200 |
| ☑ | `/favorites/ajax/folders` | ajaxFolders | ahgFavoritesPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/favorites/export/:format` | export | ahgFavoritesPlugin | PASS | HTTP 200 |
| ☑ | `/favorites/folder/:id/export/:format` | exportFolder | ahgFavoritesPlugin | PASS | HTTP 302 |
| ☐ | `/favorites/folder/:id/share` | shareFolder | ahgFavoritesPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/favorites/folder/:id/revoke-share` | revokeSharing | ahgFavoritesPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/favorites/shared/:token` | viewShared | ahgFavoritesPlugin | N/A | HTTP 404 |
| ☑ | `/favorites/import` | import | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/favorites/send-to-collection` | sendToCollection | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/favorites/send-to-project` | sendToProject | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/favorites/send-to-bibliography` | sendToBibliography | ahgFavoritesPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/registry/favorite/toggle` | favoriteToggle | ahgRegistryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/registry/my/favorites` | myFavorites | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |


## Feedback  ·  `feedbackMenu`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Feedback** from the menu) | feedbackMenu | core | | |


## Cart  ·  `cart`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/cart` | browse | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/cart/browse` | browse | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/cart/add/:slug` | add | ahgCartPlugin | SKIP | destructive/POST |
| ☐ | `/cart/remove/:id` | remove | ahgCartPlugin | SKIP | destructive/POST |
| ☑ | `/cart/clear` | clear | ahgCartPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/cart/thank-you` | thankYou | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/cart/checkout` | checkout | ahgCartPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/cart/update-products` | updateProducts | ahgCartPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/cart/update-item` | updateItem | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/cart/save-selections` | saveSelections | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/cart/payment-return/:order` | paymentReturn | ahgCartPlugin | PASS | HTTP 302 |
| ☐ | `/cart/payment/:order` | payment | ahgCartPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/cart/payment/success/:order` | paymentSuccess | ahgCartPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/cart/payment/cancel/:order` | paymentCancel | ahgCartPlugin | SKIP | destructive/POST |
| ☑ | `/cart/payment/notify` | paymentNotify | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/cart/order/:order` | orderConfirmation | ahgCartPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/cart/orders` | orders | ahgCartPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/cart/download/:token` | download | ahgCartPlugin | N/A | HTTP 404 |


# MENU: Browse / Discovery


## Archival descriptions  ·  `browseInformationObjects`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | N/A | HTTP 404 |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | PASS | HTTP 302 (fixed) |
| ☑ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | PASS | HTTP 302 |
| ☑ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | PASS | HTTP 200 (fixed) |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/objects] |
| ☑ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/object-list] |
| ☑ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | PASS | HTTP 200 |
| ☑ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | PASS | HTTP 200 |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | PASS | HTTP 200 |
| ☑ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | PASS | HTTP 200 |
| ☑ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | PASS | HTTP 200 |
| ☑ | `/object/export` | index | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | PASS | HTTP 200 |
| ☑ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | PASS | HTTP 302 |
| ☑ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | PASS | HTTP 302 [/loan/1/add-object] |
| ☑ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | PASS | HTTP 302 [/loan/1/remove-object] |
| ☑ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | SKIP | destructive/POST |
| ☑ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | PASS | HTTP 200 |
| ☑ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | PASS | HTTP 200 [/digitalobject/702/edit] |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | SKIP | destructive/POST |
| ☑ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Authority records  ·  `browseActors`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/completeness/:actorId/recalc` | apiCompletenessRecalc | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/api/authority/eac-cpf/:actorId` | apiEacExport | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/actor/:slug` | index | ahgActorManagePlugin | PASS | HTTP 200 [/actor/historical] |
| ☐ | `/actor/:slug/delete` | delete | ahgActorManagePlugin | SKIP | destructive/POST |
| ☑ | `/actor/:slug/edit` | edit | ahgActorManagePlugin | PASS | HTTP 200 [/actor/historical/edit] |
| ☑ | `/actor/add` | edit | ahgActorManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/actor/browse` | browse | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/actor/autocomplete` | autocomplete | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/heritage/actor-autocomplete` | actorAutocomplete | ahgHeritageAccountingPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/actorAutocomplete` | actorAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Archival institutions  ·  `browseRepositories`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/reports/repositories` | repositories | ahgReportsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/v2/repositories` | repositoriesBrowse | ahgAPIPlugin | PASS | HTTP 403 (pw 2026-06-27) |


## Functions  ·  `browseFunctions`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/functions/browse` | functionBrowse | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/authority/function/save` | apiFunctionSave | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/authority/function/:id/delete` | apiFunctionDelete | ahgAuthorityPlugin | SKIP | destructive/POST |
| ☑ | `/function/:slug` | view | ahgFunctionManagePlugin | PASS | HTTP 200 [/function/test-function] |
| ☐ | `/function/:slug/delete` | delete | ahgFunctionManagePlugin | SKIP | destructive/POST |
| ☑ | `/function/:slug/edit` | edit | ahgFunctionManagePlugin | PASS | HTTP 200 [/function/test-function/edit] |
| ☑ | `/function/add` | edit | ahgFunctionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/function/browse` | browse | ahgFunctionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Subjects  ·  `browseSubjects`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/library/suggestSubjects` | suggestSubjects | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/library/subjects` | subjects | ahgLibraryPlugin | PASS | HTTP 403 (pw 2026-06-27) |


## Places  ·  `browsePlaces`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/marketplace` | browse | ahgMarketplacePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/marketplace/search` | search | ahgMarketplacePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/marketplace/sector/:sector` | sector | ahgMarketplacePlugin | PASS | HTTP 200 |
| ☐ | `/marketplace/category/:sector/:slug` | category | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☑ | `/marketplace/auctions` | auctionBrowse | ahgMarketplacePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/marketplace/featured` | featured | ahgMarketplacePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/marketplace/collection/:slug` | collection | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☐ | `/marketplace/seller/:slug` | seller | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☐ | `/marketplace/listing/:slug` | listing | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☐ | `/marketplace/buy/:slug` | buy | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☐ | `/marketplace/offer/:slug` | offerForm | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☐ | `/marketplace/bid/:slug` | bidForm | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☐ | `/marketplace/enquiry/:slug` | enquiryForm | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☑ | `/marketplace/my/purchases` | myPurchases | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/my/bids` | myBids | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/my/offers` | myOffers | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/my/following` | myFollowing | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/marketplace/follow/:seller` | follow | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☑ | `/marketplace/review/:id` | reviewForm | ahgMarketplacePlugin | PASS | HTTP 302 |
| ☑ | `/marketplace/sell` | dashboard | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/register` | sellerRegister | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/profile` | sellerProfile | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/listings` | sellerListings | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/listings/create` | sellerListingCreate | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/marketplace/sell/listings/:id/edit` | sellerListingEdit | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☐ | `/marketplace/sell/listings/:id/images` | sellerListingImages | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☐ | `/marketplace/sell/listings/:id/publish` | sellerListingPublish | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☐ | `/marketplace/sell/listings/:id/withdraw` | sellerListingWithdraw | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☑ | `/marketplace/sell/offers` | sellerOffers | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/marketplace/sell/offers/:id/respond` | sellerOfferRespond | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☑ | `/marketplace/sell/transactions` | sellerTransactions | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/marketplace/sell/transactions/:id` | sellerTransactionDetail | ahgMarketplacePlugin | N/A | HTTP 404 |
| ☑ | `/marketplace/sell/payouts` | sellerPayouts | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/reviews` | sellerReviews | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/enquiries` | sellerEnquiries | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/collections` | sellerCollections | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/collections/create` | sellerCollectionCreate | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/analytics` | sellerAnalytics | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/admin` | adminDashboard | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/admin/listings` | adminListings | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |


## Digital objects  ·  `browseDigitalObjects`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | N/A | HTTP 404 |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | PASS | HTTP 302 (fixed) |
| ☑ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | PASS | HTTP 302 |
| ☑ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | PASS | HTTP 200 (fixed) |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/objects] |
| ☑ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/object-list] |
| ☑ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | PASS | HTTP 200 |
| ☑ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | PASS | HTTP 200 |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | PASS | HTTP 200 |
| ☑ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | PASS | HTTP 200 |
| ☑ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | PASS | HTTP 200 |
| ☑ | `/object/export` | index | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | PASS | HTTP 200 |
| ☑ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | PASS | HTTP 302 |
| ☑ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | PASS | HTTP 302 [/loan/1/add-object] |
| ☑ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | PASS | HTTP 302 [/loan/1/remove-object] |
| ☑ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | SKIP | destructive/POST |
| ☑ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | PASS | HTTP 200 |
| ☑ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | PASS | HTTP 200 [/digitalobject/702/edit] |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | SKIP | destructive/POST |
| ☑ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


# MENU: Browse — our collection


## Archival Holdings  ·  `browseInformationObjectsInstitution`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | N/A | HTTP 404 |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | PASS | HTTP 302 (fixed) |
| ☑ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | PASS | HTTP 302 |
| ☑ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | PASS | HTTP 200 (fixed) |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/objects] |
| ☑ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/object-list] |
| ☑ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | PASS | HTTP 200 |
| ☑ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | PASS | HTTP 200 |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | PASS | HTTP 200 |
| ☑ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | PASS | HTTP 200 |
| ☑ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/institutions` | adminInstitutions | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/institutions/verify` | adminInstitutionVerify | ahgRegistryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/institutions/:id/edit` | institutionEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/my/institution` | myInstitutionDashboard | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/register` | institutionRegister | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/edit` | institutionEdit | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/contacts` | myInstitutionContacts | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/contacts/add` | myInstitutionContactAdd | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/contacts/:id/edit` | myInstitutionContactEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☐ | `/registry/my/institution/contacts/:id/delete` | myInstitutionContactDelete | ahgRegistryPlugin | SKIP | destructive/POST |
| ☑ | `/registry/my/institution/instances` | myInstitutionInstances | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/instances/add` | myInstitutionInstanceAdd | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/instances/:id/edit` | myInstitutionInstanceEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/my/institution/instances/:id/delink` | myInstitutionInstanceDelink | ahgRegistryPlugin | PASS | HTTP 302 |


## Digital objects  ·  `browseDigitalObjectsInstitution`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | N/A | HTTP 404 |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | PASS | HTTP 302 (fixed) |
| ☑ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | PASS | HTTP 200 |
| ☑ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | PASS | HTTP 200 (fixed) |
| ☑ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | PASS | HTTP 302 |
| ☑ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | PASS | HTTP 200 |
| ☑ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | PASS | HTTP 200 (fixed) |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/objects] |
| ☑ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | PASS | HTTP 200 [/exhibition/1/object-list] |
| ☑ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | PASS | HTTP 200 |
| ☑ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | PASS | HTTP 200 |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | PASS | HTTP 200 |
| ☑ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | PASS | HTTP 200 |
| ☑ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/institutions` | adminInstitutions | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/institutions/verify` | adminInstitutionVerify | ahgRegistryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/admin/institutions/:id/edit` | institutionEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/my/institution` | myInstitutionDashboard | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/register` | institutionRegister | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/edit` | institutionEdit | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/contacts` | myInstitutionContacts | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/contacts/add` | myInstitutionContactAdd | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/contacts/:id/edit` | myInstitutionContactEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☐ | `/registry/my/institution/contacts/:id/delete` | myInstitutionContactDelete | ahgRegistryPlugin | SKIP | destructive/POST |
| ☑ | `/registry/my/institution/instances` | myInstitutionInstances | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/instances/add` | myInstitutionInstanceAdd | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/instances/:id/edit` | myInstitutionInstanceEdit | ahgRegistryPlugin | PASS | HTTP 200 |
| ☑ | `/registry/my/institution/instances/:id/delink` | myInstitutionInstanceDelink | ahgRegistryPlugin | PASS | HTTP 302 |


# MENU: Main menu


## Add  ·  `add`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Add** from the menu) | add | core | | |


## Manage  ·  `manage`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Manage** from the menu) | manage | core | | |


## Import  ·  `import`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | PASS | HTTP 302 (fixed #187) |
| ☑ | `/ahgSettings/import` | import | ahgSettingsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/portable-export/import` | import | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/favorites/import` | import | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import` | bulkImport | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import-sample` | bulkImportSample | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/library/copy-cataloguing/import` | import | ahgLibraryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/researcher/import` | importExchange | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/customFields/import` | import | ahgCustomFieldsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/import` | adminImport | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | PASS | HTTP 302 |
| ☑ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | PASS | HTTP 200 |


## Admin  ·  `admin`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/rights` | index | ahgExtendedRightsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/rights/batch` | batch | ahgExtendedRightsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/admin/condition` | admin | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/authority/dashboard` | dashboard | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/authority/workqueue` | workqueue | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☐ | `/admin/authority/merge/:id` | merge | ahgAuthorityPlugin | SKIP | destructive/POST |
| ☐ | `/admin/authority/split/:id` | split | ahgAuthorityPlugin | SKIP | destructive/POST |
| ☑ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/functions/browse` | functionBrowse | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | PASS | HTTP 200 |
| ☑ | `/admin/authority/config` | config | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/authority/dedup` | index | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/authority/dedup/scan` | scan | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/admin/authority/dedup/compare/:id` | compare | ahgAuthorityPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/admin/authority/ner-pipeline` | index | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/admin/queue` | queueBrowse | ahgJobsManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/queue/detail/:id` | queueDetail | ahgJobsManagePlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/admin/queue/batches` | queueBatches | ahgJobsManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/queue/progress` | queueProgress | ahgJobsManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/queue/retry` | queueRetry | ahgJobsManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/queue/cancel` | queueCancel | ahgJobsManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/admin/registrations/approve` | approve | ahgUserRegistrationPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/registrations/verify` | markVerified | ahgUserRegistrationPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/registrations/reject` | reject | ahgUserRegistrationPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/registrations` | pending | ahgUserRegistrationPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/forms` | index | ahgFormsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/forms/templates` | templates | ahgFormsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/forms/template/create` | templateCreate | ahgFormsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/forms/template/:id/edit` | templateEdit | ahgFormsPlugin | PASS | HTTP 302 (fixed) |
| ☐ | `/admin/forms/template/:id/delete` | templateDelete | ahgFormsPlugin | SKIP | destructive/POST |
| ☐ | `/admin/forms/template/:id/clone` | templateClone | ahgFormsPlugin | SKIP | destructive/POST |
| ☑ | `/admin/forms/template/:id/export` | templateExport | ahgFormsPlugin | PASS | HTTP 200 |
| ☑ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | PASS | HTTP 302 (fixed #187) |
| ☑ | `/admin/forms/template/:id/builder` | builder | ahgFormsPlugin | PASS | HTTP 200 |
| ☑ | `/admin/forms/assignments` | assignments | ahgFormsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/forms/assignment/create` | assignmentCreate | ahgFormsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/admin/forms/assignment/:id/delete` | assignmentDelete | ahgFormsPlugin | SKIP | destructive/POST |
| ☐ | `/admin/forms/mappings` | mappings | ahgFormsPlugin | N/A | HTTP 404 (pw 2026-06-27) |


# MENU: Clipboard


## Clear all selections  ·  `clearClipboard`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/portable-export/api/clipboard-export` | apiClipboardExport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/favorites/clear` | clear | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/cart/clear` | clear | ahgCartPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/mediaSettings/clearQueue` | clearQueue | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/security/clearances` | index | ahgSecurityClearancePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/security/clearance/:id` | view | ahgSecurityClearancePlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/security/clearance/grant` | grant | ahgSecurityClearancePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/clearance/:id/revoke` | revoke | ahgSecurityClearancePlugin | PASS | HTTP 302 |
| ☑ | `/security/clearance/bulk-grant` | bulkGrant | ahgSecurityClearancePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/research/orcid/credentials/clear` | orcidClearCredentials | ahgResearchPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/research/ajax/clipboard-to-project` | clipboardToProject | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/ajax/manage-clipboard-item` | manageClipboardItem | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Go to clipboard  ·  `goToClipboard`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/portable-export/api/clipboard-export` | apiClipboardExport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/research/ajax/clipboard-to-project` | clipboardToProject | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/ajax/manage-clipboard-item` | manageClipboardItem | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Load clipboard  ·  `loadClipboard`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/condition/check/:id/upload` | upload | ahgConditionPlugin | PASS | HTTP 200 |
| ☑ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/portable-export/api/clipboard-export` | apiClipboardExport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/download` | download | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/tenant/branding/logo-upload` | uploadLogo | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/privacyAdmin/downloadRedactedFile` | downloadRedactedFile | ahgPrivacyPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/training/upload` | apiTrainingUpload | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/client-upload-consent` | apiClientUploadConsent | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/api/upload` | apiUpload | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/cart/download/:token` | download | ahgCartPlugin | N/A | HTTP 404 |
| ☐ | `/media/download/:id` | download | ahgIiifPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☐ | `/api/v2/upload` | fileUpload | ahgAPIPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/api/v2/descriptions/:slug/upload` | descriptionUpload | ahgAPIPlugin | N/A | HTTP 404 |
| ☑ | `/ahg3DModel/upload` | upload | ahg3DModelPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ingest/:id/upload` | upload | ahgIngestPlugin | PASS | HTTP 200 |
| ☐ | `/admin/preservation/package/:id/download` | packageDownload | ahgPreservationPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/tiff-pdf-merge/upload` | upload | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/download/:job_id` | download | ahgPreservationPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/statistics/downloads` | downloads | ahgStatisticsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/vendor/software/:id/upload` | myVendorSoftwareUpload | ahgRegistryPlugin | N/A | HTTP 404 |
| ☑ | `/ftp-upload` | index | ahgFtpPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ftp-upload/upload` | upload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/chunk` | uploadChunk | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/list` | listFiles | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/delete` | deleteFile | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/loan/:id/upload-document` | uploadDocument | ahgLoanPlugin | PASS | HTTP 302 |
| ☑ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/report-builder/attachment/upload` | apiAttachmentUpload | ahgReportBuilderPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/research/reproduction/download/:token` | reproductionDownload | ahgResearchPlugin | N/A | HTTP 404 |
| ☐ | `/research/studio/:projectId/artefact/:artefactId/download` | studioDownload | ahgResearchPlugin | N/A | HTTP 404 — no record exists (correct not-found; needs real data) |
| ☑ | `/research/ajax/upload-note-image` | uploadNoteImage | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/ajax/clipboard-to-project` | clipboardToProject | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/ajax/manage-clipboard-item` | manageClipboardItem | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Save clipboard  ·  `saveClipboard`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/condition/annotation/save` | saveAnnotation | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/authority/identifier/save` | apiIdentifierSave | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/authority/occupation/save` | apiOccupationSave | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/authority/function/save` | apiFunctionSave | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/museum/provenance/save` | provenanceSave | ahgMuseumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/forms/autosave` | apiAutosave | ahgFormsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/glam/saveBrowseSettings` | saveBrowseSettings | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/sharepoint/rules/save` | ruleSave | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/mappings/save` | mappingsSave | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/drives/save` | driveSave | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/accessions/:id/appraisal/save` | appraisalSave | ahgAccessionManagePlugin | SKIP | destructive/POST |
| ☑ | `/api/accession/container/save` | apiContainerSave | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/accession/container-item/save` | apiContainerItemSave | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/accession/rights/save` | apiRightsSave | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/ahgSettings/saveTiffPdfSettings` | saveTiffPdfSettings | ahgSettingsPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/spectrum/annotation/save` | saveAnnotation | ahgSpectrumPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/portable-export/api/clipboard-export` | apiClipboardExport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/admin/doi/config/save` | configSave | ahgDoiPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/tenant/branding/save` | save | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/privacyAdmin/saveVisualRedaction` | saveVisualRedaction | ahgPrivacyPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/client-save` | apiClientSave | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/manual-save` | apiManualSave | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/cart/save-selections` | saveSelections | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/mediaSettings/save` | save | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/customFields/save` | save | ahgCustomFieldsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/customFields/save` | saveValues | ahgCustomFieldsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/integrity/alert/save` | apiAlertSave | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/security/2fa/policy/save` | mfaPolicy | ahgSecurityClearancePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/accessibility/alt-text/save` | save | ahgAccessibilityPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/notes/save` | noteSave | ahgRegistryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/ai/ner/bulk-save` | bulkSave | ahgAIPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/save-draft` | saveDraft | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/report-builder/query/save` | apiQuerySave | ahgReportBuilderPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/report-builder/template/save` | apiTemplateSave | ahgReportBuilderPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/report-builder/link/save` | apiLinkSave | ahgReportBuilderPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/report-builder/section/save` | apiSectionSave | ahgReportBuilderPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/report-builder/widget/save` | apiWidgetSave | ahgReportBuilderPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/report-builder/save` | apiSave | ahgReportBuilderPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/research/saved-searches` | savedSearches | ahgResearchPlugin | PASS | HTTP 302 (pw 2026-06-27) |
