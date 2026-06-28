# AHG — Master Test Checklist (merged)

Menu-driven manual + automated test checklist. **Part 1** walks every navigation menu item as a screen, listing every link/URL under it (auto-tested where parameterless). **Part 2** details the linked-panel sub-functions for the core entity screens. Tick ☐→☑; record Pass/Fail + notes.

Generated 2026-06-27.

---

# PART 1 — Menus → screens → links/URLs


# MENU: Add (create records)


## Archival descriptions  ·  `addInformationObject`

*Linked panels & sub-functions:* Core ISAD(G) fields; linked panels — Provenance, AI (NER/summarise/translate/spellcheck/suggest/face), Rights (PREMIS/CC/RightsStatements/embargo/TK), Digital object (upload/IIIF/media/3D/watermark/metadata), Security classification, Custom fields, Audit, Version control, Preservation, Share link

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☑ | `/object/export` | index | ahgExportPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | | |
| ☐ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | | |
| ☑ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | | |
| ☑ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Accession records  ·  `addAccessionRecord`

*Linked panels & sub-functions:* Core accession; Donor + donor agreement, Rights holder, Physical storage, create-description, deaccession, audit

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/donor/autocomplete/accessions` | autocompleteAccessions | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/autocomplete/records` | autocompleteRecords | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/accession/:slug` | index | ahgAccessionManagePlugin | | |
| ☐ | `/accession/:slug/delete` | delete | ahgAccessionManagePlugin | | |
| ☐ | `/accession/:slug/edit` | edit | ahgAccessionManagePlugin | | |
| ☑ | `/accession/browse` | browse | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/dashboard` | dashboard | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/accessions/:id/submit` | submit | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/review` | review | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/accept` | accept | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/reject` | reject | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/return` | returnRevision | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/timeline` | timeline | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/checklist` | checklist | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/attachments` | attachments | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/intake` | queueDetail | ahgAccessionManagePlugin | | |
| ☑ | `/admin/accessions/queue` | queue | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/accessions/queue/assign` | assign | ahgAccessionManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/admin/accessions/config` | config | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/numbering` | numbering | ahgAccessionManagePlugin | PASS | HTTP 200 (fixed #187) |
| ☐ | `/api/accession/checklist/:id/toggle` | apiChecklistToggle | ahgAccessionManagePlugin | | |
| ☑ | `/api/accession/checklist/apply-template` | apiChecklistApplyTemplate | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/accession/attachment/:id/delete` | apiAttachmentDelete | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/appraisal` | appraisal | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/appraisal/save` | appraisalSave | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/valuation` | valuation | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/valuation/add` | valuationAdd | ahgAccessionManagePlugin | | |
| ☑ | `/admin/accessions/appraisal-templates` | appraisalTemplates | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/valuation-report` | valuationReport | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/accession/appraisal/:id/score` | apiAppraisalScore | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/containers` | containers | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/rights` | rights | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container/save` | apiContainerSave | ahgAccessionManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/api/accession/container/:id/delete` | apiContainerDelete | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container-item/save` | apiContainerItemSave | ahgAccessionManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/api/accession/container-item/:id/delete` | apiContainerItemDelete | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container-item/:id/link` | apiContainerItemLink | ahgAccessionManagePlugin | | |
| ☑ | `/api/accession/barcode/lookup` | apiBarcodeLookup | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/accession/rights/save` | apiRightsSave | ahgAccessionManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |


## Authority records  ·  `addActor`

*Linked panels & sub-functions:* Core ISAAR-CPF fields; Authority resolution (ULAN/LCNAF/VIAF/Wikidata/ORCID), Contact, AI, linked descriptions, custom fields, audit

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/completeness/:actorId/recalc` | apiCompletenessRecalc | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/eac-cpf/:actorId` | apiEacExport | ahgAuthorityPlugin | | |
| ☐ | `/actor/:slug` | index | ahgActorManagePlugin | | |
| ☐ | `/actor/:slug/delete` | delete | ahgActorManagePlugin | | |
| ☐ | `/actor/:slug/edit` | edit | ahgActorManagePlugin | | |
| ☑ | `/actor/add` | edit | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/actor/browse` | browse | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/actor/autocomplete` | autocomplete | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/heritage/actor-autocomplete` | actorAutocomplete | ahgHeritageAccountingPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/actorAutocomplete` | actorAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Archival institutions  ·  `addRepository`

*Linked panels & sub-functions:* Core ISDIAH fields; logo/theme, holdings, uploads path, custom fields, audit

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/repository/add` | edit | ahgRepositoryManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/repository/browse` | browse | ahgRepositoryManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/statistics/repository/:id` | repository | ahgStatisticsPlugin | | |
| ☑ | `/export/repository` | repository | ahgExportPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/repositoryAutocomplete` | repositoryAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Terms  ·  `addTerm`

*Linked panels & sub-functions:* Term labels/scope/relationships (SKOS); semantic/thesaurus sync, used-in, SKOS export

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/term/:slug/edit` | edit | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug/delete` | delete | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug` | index | ahgTermTaxonomyPlugin | | |
| ☐ | `/api/v2/taxonomies/:id/terms` | taxonomyTerms | ahgAPIPlugin | | |
| ☑ | `/informationobject/termAutocomplete` | termAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Function  ·  `addFunction`

*Linked panels & sub-functions:* Core ISDF fields; relationships, linked records

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | | |
| ☑ | `/admin/authority/functions/browse` | functionBrowse | ahgAuthorityPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/authority/function/save` | apiFunctionSave | ahgAuthorityPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/authority/function/:id/delete` | apiFunctionDelete | ahgAuthorityPlugin | | |
| ☐ | `/function/:slug` | view | ahgFunctionManagePlugin | | |
| ☐ | `/function/:slug/delete` | delete | ahgFunctionManagePlugin | | |
| ☐ | `/function/:slug/edit` | edit | ahgFunctionManagePlugin | | |
| ☑ | `/function/add` | edit | ahgFunctionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/function/browse` | browse | ahgFunctionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


# MENU: Manage


## Accessions  ·  `accessions`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/donor/autocomplete/accessions` | autocompleteAccessions | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/accession/:slug` | index | ahgAccessionManagePlugin | | |
| ☐ | `/accession/:slug/delete` | delete | ahgAccessionManagePlugin | | |
| ☐ | `/accession/:slug/edit` | edit | ahgAccessionManagePlugin | | |
| ☑ | `/accession/browse` | browse | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/dashboard` | dashboard | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/accessions/:id/submit` | submit | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/review` | review | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/accept` | accept | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/reject` | reject | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/return` | returnRevision | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/timeline` | timeline | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/checklist` | checklist | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/attachments` | attachments | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/intake` | queueDetail | ahgAccessionManagePlugin | | |
| ☑ | `/admin/accessions/queue` | queue | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/accessions/queue/assign` | assign | ahgAccessionManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/admin/accessions/config` | config | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/numbering` | numbering | ahgAccessionManagePlugin | PASS | HTTP 200 (fixed #187) |
| ☐ | `/api/accession/checklist/:id/toggle` | apiChecklistToggle | ahgAccessionManagePlugin | | |
| ☑ | `/api/accession/checklist/apply-template` | apiChecklistApplyTemplate | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/accession/attachment/:id/delete` | apiAttachmentDelete | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/appraisal` | appraisal | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/appraisal/save` | appraisalSave | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/valuation` | valuation | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/valuation/add` | valuationAdd | ahgAccessionManagePlugin | | |
| ☑ | `/admin/accessions/appraisal-templates` | appraisalTemplates | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/accessions/valuation-report` | valuationReport | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/accession/appraisal/:id/score` | apiAppraisalScore | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/containers` | containers | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/rights` | rights | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container/save` | apiContainerSave | ahgAccessionManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/api/accession/container/:id/delete` | apiContainerDelete | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container-item/save` | apiContainerItemSave | ahgAccessionManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/api/accession/container-item/:id/delete` | apiContainerItemDelete | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container-item/:id/link` | apiContainerItemLink | ahgAccessionManagePlugin | | |
| ☑ | `/api/accession/barcode/lookup` | apiBarcodeLookup | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/accession/rights/save` | apiRightsSave | ahgAccessionManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/api/accession/rights/:id/delete` | apiRightsDelete | ahgAccessionManagePlugin | | |


## Donors  ·  `donors`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/donor/dashboard` | dashboard | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/agreement/browse` | browse | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/agreement/add` | add | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/donor/agreement/:id` | view | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/agreement/:id/edit` | edit | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/agreement/:id/delete` | delete | ahgDonorAgreementPlugin | | |
| ☑ | `/donor/agreement/reminders` | reminders | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/autocomplete/accessions` | autocompleteAccessions | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/autocomplete/records` | autocompleteRecords | ahgDonorAgreementPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/donor/:slug` | view | ahgDonorManagePlugin | | |
| ☐ | `/donor/:slug/delete` | delete | ahgDonorManagePlugin | | |
| ☐ | `/donor/:slug/edit` | edit | ahgDonorManagePlugin | | |
| ☑ | `/donor/add` | edit | ahgDonorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/donor/browse` | browse | ahgDonorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Jobs  ·  `jobs`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/jobs` | browse | ahgJobsManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/jobs/report/:id` | report | ahgJobsManagePlugin | | |
| ☑ | `/jobs/delete` | delete | ahgJobsManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/jobs/export` | export | ahgJobsManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/v2/sharepoint/push/jobs/:id` | pushJob | ahgSharePointPlugin | | |
| ☑ | `/ingest/ajax/job-status` | jobStatus | ahgIngestPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/job/:job_id` | getJob | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/download/:job_id` | download | ahgPreservationPlugin | | |
| ☑ | `/tiff-pdf-merge/jobs` | browse | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/job/:job_id/view` | view | ahgPreservationPlugin | | |
| ☑ | `/research/extraction-job/create` | createExtractionJob | ahgResearchPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/research/extraction-job/:id` | viewExtractionJob | ahgResearchPlugin | | |
| ☐ | `/research/extraction-jobs/:project_id` | extractionJobs | ahgResearchPlugin | | |


## Physical storage  ·  `browsePhysicalObjects`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☑ | `/object/export` | index | ahgExportPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | | |
| ☐ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | | |
| ☑ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | | |
| ☑ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Rights holders  ·  `rightsholders`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/rightsholder/:slug` | view | ahgRightsHolderManagePlugin | | |
| ☐ | `/rightsholder/:slug/delete` | delete | ahgRightsHolderManagePlugin | | |
| ☐ | `/rightsholder/:slug/edit` | edit | ahgRightsHolderManagePlugin | | |
| ☑ | `/rightsholder/add` | edit | ahgRightsHolderManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/rightsholder/browse` | browse | ahgRightsHolderManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Taxonomies  ·  `taxonomies`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/api/v2/taxonomies` | taxonomiesBrowse | ahgAPIPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/v2/taxonomies/:id/terms` | taxonomyTerms | ahgAPIPlugin | | |


## Feedback  ·  `feedback`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Feedback** from the menu) | feedback | core | | |


## Browse Request for Publish  ·  `requesttopublishBrowse`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/requesttopublish/:slug` | edit | ahgRequestToPublishPlugin | | |
| ☐ | `/requesttopublish/delete/:slug` | delete | ahgRequestToPublishPlugin | | |
| ☐ | `/requestToPublish/submit/:slug` | submit | ahgRequestToPublishPlugin | | |
| ☑ | `/requesttopublish/browse` | browse | ahgRequestToPublishPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/requesttopublish` | browse | ahgRequestToPublishPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/requesttopublish/` | browse | ahgRequestToPublishPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/requesttopublish/receipt` | receipt | ahgRequestToPublishPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/requesttopublish/receipt/:token` | receipt | ahgRequestToPublishPlugin | | |
| ☑ | `/requesttopublish/inbox` | inbox | ahgRequestToPublishPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/requesttopublish/review/:id` | review | ahgRequestToPublishPlugin | | |


## Collection assistant  ·  `collectionAssistant`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/favorites/send-to-collection` | sendToCollection | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/marketplace/collection/:slug` | collection | ahgMarketplacePlugin | | |
| ☑ | `/marketplace/sell/collections` | sellerCollections | ahgMarketplacePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/collections/create` | sellerCollectionCreate | ahgMarketplacePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/researcher/from-collection/:collectionId` | createFromCollection | ahgResearcherPlugin | | |
| ☑ | `/manifest-collections/autocomplete` | autocomplete | ahgIiifPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/manifest-collections` | index | ahgIiifPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/manifest-collection/new` | new | ahgIiifPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/manifest-collection/create` | create | ahgIiifPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/manifest-collection/reorder` | reorder | ahgIiifPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/manifest-collection/:id/view` | view | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/:id/edit` | edit | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/:id/update` | update | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/:id/delete` | delete | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/:id/items/add` | addItems | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/item/:item_id/remove` | removeItem | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/:slug/manifest.json` | manifest | ahgIiifPlugin | | |
| ☐ | `/api/research/collections/:id` | collection | ahgResearchPlugin | | |
| ☐ | `/api/research/collections` | collections | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/research/collection/:id` | viewCollection | ahgResearchPlugin | | |
| ☑ | `/research/collections` | collections | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/ajax/add-to-collection` | addToCollection | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/ajax/create-collection` | createCollectionAjax | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/research/collection/:id/export/:format` | exportFindingAid | ahgResearchPlugin | | |
| ☐ | `/research/ro-crate/collection/:id` | packageCollection | ahgResearchPlugin | | |


## Researcher Copilot  ·  `researchCopilot`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/researcher` | dashboard | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/submissions` | submissions | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/submission/new` | newSubmission | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/researcher/submission/:id` | viewSubmission | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/edit` | editSubmission | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/item/add` | addItem | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/item/:itemId` | editItem | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/item/:itemId/delete` | deleteItem | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/submit` | submit | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/resubmit` | resubmit | ahgResearcherPlugin | | |
| ☐ | `/researcher/from-collection/:collectionId` | createFromCollection | ahgResearcherPlugin | | |
| ☑ | `/researcher/import` | importExchange | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/researcher/submission/:id/publish` | publish | ahgResearcherPlugin | | |
| ☑ | `/researcher/api/upload` | apiUpload | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/api/delete-file` | apiDeleteFile | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/api/autocomplete` | apiAutocomplete | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/datasets` | index | ahgRdmPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/datasets/dashboard` | dashboard | ahgRdmPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/datasets/compliance` | compliance | ahgRdmPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/datasets/create` | create | ahgRdmPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/research/datasets/:id` | show | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/deposit` | deposit | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/scan` | scan | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/file/:fid` | fileDownload | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/findings/:fid/resolve` | resolveFinding | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/disposition` | disposition | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/dmp` | linkDmp | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/dmp/unlink` | unlinkDmp | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/landing` | landing | ahgRdmPlugin | | |
| ☑ | `/admin/naz/researchers` | researchers | ahgNAZPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/naz/researcher/create` | researcherCreate | ahgNAZPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/naz/researcher/:id/edit` | researcherEdit | ahgNAZPlugin | | |
| ☐ | `/admin/naz/researcher/:id` | researcherView | ahgNAZPlugin | | |
| ☑ | `/naz/researchers` | researchers | ahgNAZPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/research/stats` | stats | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/api/research/annotations` | annotations | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/api/research/bibliographies/:id/export/:format` | exportBibliography | ahgResearchPlugin | | |
| ☐ | `/api/research/bibliographies` | bibliographies | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/api/research/citations/:id/:format` | citation | ahgResearchPlugin | | |
| ☐ | `/api/research/bookings` | bookings | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |


## Provenance graph  ·  `provenanceGraph`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | | |
| ☐ | `/api/graphql` | index | ahgGraphQLPlugin | N/A | HTTP 400 (pw 2026-06-27) |
| ☐ | `/api/graphql/playground` | playground | ahgGraphQLPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/:slug/cco/provenance` | provenance | ahgMuseumPlugin | | |
| ☑ | `/museum/provenance/save` | provenanceSave | ahgMuseumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/museum/provenance/get` | provenanceGet | ahgMuseumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/museum/provenance/delete` | provenanceDelete | ahgMuseumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/museum/provenance/export` | provenanceExport | ahgMuseumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/spectrum/provenance/ajax` | provenanceAjax | ahgSpectrumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/favorites/send-to-bibliography` | sendToBibliography | ahgFavoritesPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/provenance/coverage` | coverage | ahgProvenancePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/provenance/coverage-data` | apiCoverage | ahgProvenancePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/provenance/trace/:id` | apiTrace | ahgProvenancePlugin | | |
| ☐ | `/provenance/authenticity/:id` | authenticity | ahgProvenancePlugin | | |
| ☑ | `/statistics/geographic` | geographic | ahgStatisticsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/research/bibliographies/:id/export/:format` | exportBibliography | ahgResearchPlugin | | |
| ☐ | `/api/research/bibliographies` | bibliographies | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/research/bibliography/:id/export/:format` | exportBibliography | ahgResearchPlugin | | |
| ☐ | `/research/bibliography/:id/add` | addBibliographyEntry | ahgResearchPlugin | | |
| ☐ | `/research/bibliography/:id` | viewBibliography | ahgResearchPlugin | | |
| ☑ | `/research/bibliographies` | bibliographies | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/research/ajax/add-to-bibliography` | addToBibliographyAjax | ahgResearchPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | | |
| ☑ | `/research/knowledge-graph-data` | knowledgeGraphData | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/research/knowledge-graph/:project_id` | knowledgeGraph | ahgResearchPlugin | | |
| ☐ | `/research/network-graph/:project_id/export/graphml` | exportGraphML | ahgResearchPlugin | | |
| ☐ | `/research/network-graph/:project_id/export/gexf` | exportGraphGEXF | ahgResearchPlugin | | |
| ☑ | `/research/network-graph-data` | networkGraphData | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/research/network-graph/:project_id` | networkGraph | ahgResearchPlugin | | |


# MENU: Import


## XML  ·  `importXml`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | PASS | HTTP 302 (fixed #187) |
| ☑ | `/ahgSettings/import` | import | ahgSettingsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/portable-export/import` | import | ahgPortableExportPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | PASS | HTTP 405 (pw 2026-06-27) |
| ☐ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | N/A | HTTP 400 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | PASS | HTTP 405 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/favorites/import` | import | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import` | bulkImport | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import-sample` | bulkImportSample | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/library/copy-cataloguing/import` | import | ahgLibraryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/researcher/import` | importExchange | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/customFields/import` | import | ahgCustomFieldsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/registry/admin/import` | adminImport | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | | |
| ☐ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | | |


## CSV  ·  `importCsv`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | PASS | HTTP 302 (fixed #187) |
| ☑ | `/ahgSettings/import` | import | ahgSettingsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/portable-export/import` | import | ahgPortableExportPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | PASS | HTTP 405 (pw 2026-06-27) |
| ☐ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | N/A | HTTP 400 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | PASS | HTTP 405 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/favorites/import` | import | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import` | bulkImport | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import-sample` | bulkImportSample | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/library/copy-cataloguing/import` | import | ahgLibraryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/researcher/import` | importExchange | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/customFields/import` | import | ahgCustomFieldsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/registry/admin/import` | adminImport | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | | |
| ☐ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | | |


## Validate CSV  ·  `validateCsv`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | PASS | HTTP 405 (pw 2026-06-27) |
| ☐ | `/ingest/:id/validate` | validate | ahgIngestPlugin | | |
| ☑ | `/api/preservation/package/validate` | apiPackageValidate | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/api/report-builder/query/validate` | apiQueryValidate | ahgReportBuilderPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/bulk-validate` | bulkValidate | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/research/validate/:id` | validateResult | ahgResearchPlugin | | |


## SKOS  ·  `importSkos`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | PASS | HTTP 302 (fixed #187) |
| ☑ | `/ahgSettings/import` | import | ahgSettingsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/portable-export/import` | import | ahgPortableExportPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | PASS | HTTP 405 (pw 2026-06-27) |
| ☐ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | N/A | HTTP 400 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | PASS | HTTP 405 (pw 2026-06-27) |
| ☑ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/favorites/import` | import | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import` | bulkImport | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/acquisition/bulk-import-sample` | bulkImportSample | ahgLibraryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/library/copy-cataloguing/import` | import | ahgLibraryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/researcher/import` | importExchange | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/customFields/import` | import | ahgCustomFieldsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/registry/admin/import` | adminImport | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | | |
| ☐ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | | |


## FTP Upload  ·  `ftpUpload`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/condition/check/:id/upload` | upload | ahgConditionPlugin | | |
| ☑ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/tenant/branding/logo-upload` | uploadLogo | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/training/upload` | apiTrainingUpload | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/client-upload-consent` | apiClientUploadConsent | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/api/upload` | apiUpload | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/v2/upload` | fileUpload | ahgAPIPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/api/v2/descriptions/:slug/upload` | descriptionUpload | ahgAPIPlugin | | |
| ☐ | `/ahg3DModel/upload` | upload | ahg3DModelPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/ingest/:id/upload` | upload | ahgIngestPlugin | | |
| ☑ | `/tiff-pdf-merge/upload` | upload | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/registry/my/vendor/software/:id/upload` | myVendorSoftwareUpload | ahgRegistryPlugin | | |
| ☑ | `/ftp-upload` | index | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/upload` | upload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/chunk` | uploadChunk | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/list` | listFiles | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/delete` | deleteFile | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/loan/:id/upload-document` | uploadDocument | ahgLoanPlugin | | |
| ☐ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/api/report-builder/attachment/upload` | apiAttachmentUpload | ahgReportBuilderPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/research/ajax/upload-note-image` | uploadNoteImage | ahgResearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |


# MENU: Admin


## Users  ·  `users`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
| ☑ | `/user/add` | edit | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user/list` | browse | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user` | browse | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user/login` | login | ahgUserManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/user/logout` | logout | ahgUserManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☑ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | | |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | | |


## Groups  ·  `groups`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | | |


## Static pages  ·  `staticPages`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/staticpage/:id/delete` | delete | ahgStaticPagePlugin | | |
| ☐ | `/staticpage/:id/edit` | edit | ahgStaticPagePlugin | | |
| ☑ | `/staticpage/home` | edit | ahgStaticPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/staticpage/add` | edit | ahgStaticPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/staticpage/list` | list | ahgStaticPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/privacyAdmin/getNerEntitiesForPage` | getNerEntitiesForPage | ahgPrivacyPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/iiif/activity/page/:n` | activityPage | ahgIiifPlugin | | |
| ☑ | `/discovery/pageindex` | pageindex | ahgDiscoveryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/discovery/pageindex/api` | pageindexApi | ahgDiscoveryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages` | list | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/create` | create | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/admin/landing-pages/:id/edit` | edit | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/:id/preview` | preview | ahgLandingPagePlugin | | |
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
| ☐ | `/condition/photo/:id/update-meta` | updatePhotoMeta | ahgConditionPlugin | | |
| ☑ | `/ahgSettings/autoUpdate` | autoUpdate | ahgSettingsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/spectrum/:slug/workflow/update` | workflowUpdate | ahgSpectrumPlugin | | |
| ☐ | `/admin/doi/update/:id` | update | ahgDoiPlugin | | |
| ☐ | `/admin/scan/:id/update` | update | ahgScanPlugin | | |
| ☐ | `/admin/tenants/:id/update` | updateTenant | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/reports/descriptions` | descriptions | ahgReportsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/privacy/dsar/:id/update` | dsarUpdate | ahgPrivacyPlugin | | |
| ☐ | `/cart/update-products` | updateProducts | ahgCartPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/cart/update-item` | updateItem | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/manifest-collection/:id/update` | update | ahgIiifPlugin | | |
| ☐ | `/media/audio-description/:id` | audioDescription | ahgIiifPlugin | | |
| ☐ | `/media/audio-description/:id/edit` | audioDescriptionEdit | ahgIiifPlugin | | |
| ☑ | `/api/v2/descriptions` | descriptionsBrowse | ahgAPIPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/v2/descriptions/:slug/citation` | descriptionsCitation | ahgAPIPlugin | | |
| ☐ | `/api/v2/descriptions/:slug` | descriptionsRead | ahgAPIPlugin | | |
| ☐ | `/api/v2/descriptions/:slug/conditions` | descriptionConditions | ahgAPIPlugin | | |
| ☐ | `/api/v2/descriptions/:slug/asset` | descriptionAsset | ahgAPIPlugin | | |
| ☐ | `/api/v2/descriptions/:slug/upload` | descriptionUpload | ahgAPIPlugin | | |
| ☐ | `/registry/api/sync/update` | apiSyncUpdate | ahgRegistryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/search/descriptionUpdates` | descriptionUpdates | ahgSearchPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/update-block` | updateBlock | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/landing-pages/ajax/update-settings` | updateSettings | ahgLandingPagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/research/hypothesis/:id/update` | updateHypothesis | ahgResearchPlugin | | |
| ☐ | `/research/odrl/update/:id` | updateOdrlPolicy | ahgResearchPlugin | | |
| ☐ | `/research/room/:id/update` | updateRoom | ahgResearchPlugin | | |


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
| ☐ | `/condition/check/:id/export` | exportReport | ahgConditionPlugin | | |
| ☐ | `/condition/template/:id/export` | template | ahgConditionPlugin | | |
| ☑ | `/jobs/export` | export | ahgJobsManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/museum/provenance/export` | provenanceExport | ahgMuseumPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/forms/template/:id/export` | templateExport | ahgFormsPlugin | | |
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
| ☐ | `/favorites/export/:format` | export | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/export/:format` | exportFolder | ahgFavoritesPlugin | | |
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
| ☐ | `/admin/integrity/run/:id` | runDetail | ahgIntegrityPlugin | | |
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
| ☐ | `/api/integrity/run/:id` | apiRun | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/schedule/:id/toggle` | apiScheduleToggle | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/schedule/:id/delete` | apiScheduleDelete | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/dead-letter/:id/action` | apiDeadLetterAction | ahgIntegrityPlugin | | |
| ☑ | `/api/integrity/stats` | apiStats | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/integrity/schedule/:id/run` | apiRunSchedule | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/policy/:id/toggle` | apiPolicyToggle | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/policy/:id/delete` | apiPolicyDelete | ahgIntegrityPlugin | | |
| ☑ | `/api/integrity/hold/place` | apiHoldPlace | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/integrity/hold/:id/release` | apiHoldRelease | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/disposition/:id/action` | apiDispositionAction | ahgIntegrityPlugin | | |
| ☑ | `/api/integrity/retention/scan` | apiRetentionScan | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/integrity/alert/save` | apiAlertSave | ahgIntegrityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/integrity/alert/:id/delete` | apiAlertDelete | ahgIntegrityPlugin | | |
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
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
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
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☑ | `/marketplace/sell/profile` | sellerProfile | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☑ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | | |
| ☐ | `/api/research/profile` | profile | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | | |
| ☐ | `/research/orcid/pull-profile` | orcidPullProfile | ahgResearchPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/research/profile/api-keys` | apiKeys | ahgResearchPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/research/profile` | profile | ahgResearchPlugin | PASS | HTTP 302 (pw 2026-06-27) |


## Archival description permissions  ·  `userInformationObjectAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
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
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |


## Authority record permissions  ·  `userActorAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
| ☑ | `/user/add` | edit | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/list` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/login` | login | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user/logout` | logout | ahgUserManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/completeness/:actorId/recalc` | apiCompletenessRecalc | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/eac-cpf/:actorId` | apiEacExport | ahgAuthorityPlugin | | |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/actor/:slug` | index | ahgActorManagePlugin | | |
| ☐ | `/actor/:slug/delete` | delete | ahgActorManagePlugin | | |
| ☐ | `/actor/:slug/edit` | edit | ahgActorManagePlugin | | |
| ☑ | `/actor/add` | edit | ahgActorManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/actor/browse` | browse | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/actor/autocomplete` | autocomplete | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☑ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | | |


## Archival institution permissions  ·  `userRepositoryAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
| ☑ | `/user/add` | edit | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/list` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/login` | login | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user/logout` | logout | ahgUserManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☑ | `/repository/add` | edit | ahgRepositoryManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/repository/browse` | browse | ahgRepositoryManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
| ☐ | `/statistics/repository/:id` | repository | ahgStatisticsPlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☑ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | | |
| ☑ | `/export/repository` | repository | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/informationobject/repositoryAutocomplete` | repositoryAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | | |


## Taxonomy permissions  ·  `userTermAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
| ☑ | `/user/add` | edit | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/list` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user` | browse | ahgUserManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/user/login` | login | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/user/logout` | logout | ahgUserManagePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/term/:slug/edit` | edit | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug/delete` | delete | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug` | index | ahgTermTaxonomyPlugin | | |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/api/v2/taxonomies/:id/terms` | taxonomyTerms | ahgAPIPlugin | | |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☑ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | | |
| ☑ | `/informationobject/termAutocomplete` | termAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | | |


# MENU: Admin — Groups


## Profile  ·  `groupProfile`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/glam/profiles` | profiles | ahgDisplayPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/glam/assignProfile` | assignProfile | ahgDisplayPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/profile` | sellerProfile | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | | |
| ☐ | `/api/research/profile` | profile | ahgResearchPlugin | N/A | HTTP 401 (pw 2026-06-27) |
| ☐ | `/research/orcid/pull-profile` | orcidPullProfile | ahgResearchPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/research/profile/api-keys` | apiKeys | ahgResearchPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/research/profile` | profile | ahgResearchPlugin | PASS | HTTP 302 (pw 2026-06-27) |


## Archival description permissions  ·  `groupInformationObjectAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | | |


## Authority record permissions  ·  `groupActorAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/completeness/:actorId/recalc` | apiCompletenessRecalc | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/eac-cpf/:actorId` | apiEacExport | ahgAuthorityPlugin | | |
| ☐ | `/actor/:slug` | index | ahgActorManagePlugin | | |
| ☐ | `/actor/:slug/delete` | delete | ahgActorManagePlugin | | |
| ☐ | `/actor/:slug/edit` | edit | ahgActorManagePlugin | | |
| ☑ | `/actor/add` | edit | ahgActorManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/actor/browse` | browse | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/actor/autocomplete` | autocomplete | ahgActorManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | | |
| ☑ | `/api/heritage/actor-autocomplete` | actorAutocomplete | ahgHeritageAccountingPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/actorAutocomplete` | actorAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Archival institution permissions  ·  `groupRepositoryAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/repository/add` | edit | ahgRepositoryManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/repository/browse` | browse | ahgRepositoryManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/statistics/repository/:id` | repository | ahgStatisticsPlugin | | |
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | | |
| ☑ | `/export/repository` | repository | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/informationobject/repositoryAutocomplete` | repositoryAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Taxonomy permissions  ·  `groupTermAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/term/:slug/edit` | edit | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug/delete` | delete | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug` | index | ahgTermTaxonomyPlugin | | |
| ☐ | `/api/v2/taxonomies/:id/terms` | taxonomyTerms | ahgAPIPlugin | | |
| ☑ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☑ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☑ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | | |
| ☑ | `/informationobject/termAutocomplete` | termAutocomplete | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


# MENU: Static pages


## Favorites  ·  `favorites`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/favorites` | browse | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/favorites/add/:slug` | add | ahgFavoritesPlugin | | |
| ☐ | `/favorites/remove/:id` | remove | ahgFavoritesPlugin | | |
| ☑ | `/favorites/clear` | clear | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/favorites/bulk` | bulk | ahgFavoritesPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/favorites/move` | moveToFolder | ahgFavoritesPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/favorites/notes/:id` | updateNotes | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/create` | folderCreate | ahgFavoritesPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/favorites/folder/:id` | folderView | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/edit` | folderEdit | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/delete` | folderDelete | ahgFavoritesPlugin | | |
| ☐ | `/favorites/ajax/toggle` | ajaxToggle | ahgFavoritesPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/favorites/ajax/toggle-custom` | ajaxToggleCustom | ahgFavoritesPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/favorites/ajax/search` | ajaxSearch | ahgFavoritesPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/favorites/ajax/status/:slug` | ajaxStatus | ahgFavoritesPlugin | | |
| ☑ | `/favorites/ajax/folders` | ajaxFolders | ahgFavoritesPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/favorites/export/:format` | export | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/export/:format` | exportFolder | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/share` | shareFolder | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/revoke-share` | revokeSharing | ahgFavoritesPlugin | | |
| ☐ | `/favorites/shared/:token` | viewShared | ahgFavoritesPlugin | | |
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
| ☐ | `/cart/add/:slug` | add | ahgCartPlugin | | |
| ☐ | `/cart/remove/:id` | remove | ahgCartPlugin | | |
| ☑ | `/cart/clear` | clear | ahgCartPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/cart/thank-you` | thankYou | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/cart/checkout` | checkout | ahgCartPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/cart/update-products` | updateProducts | ahgCartPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/cart/update-item` | updateItem | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/cart/save-selections` | saveSelections | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/cart/payment-return/:order` | paymentReturn | ahgCartPlugin | | |
| ☐ | `/cart/payment/:order` | payment | ahgCartPlugin | | |
| ☐ | `/cart/payment/success/:order` | paymentSuccess | ahgCartPlugin | | |
| ☐ | `/cart/payment/cancel/:order` | paymentCancel | ahgCartPlugin | | |
| ☑ | `/cart/payment/notify` | paymentNotify | ahgCartPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/cart/order/:order` | orderConfirmation | ahgCartPlugin | | |
| ☑ | `/cart/orders` | orders | ahgCartPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/cart/download/:token` | download | ahgCartPlugin | | |


# MENU: Browse / Discovery


## Archival descriptions  ·  `browseInformationObjects`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☑ | `/object/export` | index | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | | |
| ☐ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | | |
| ☑ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | | |
| ☑ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | | |
| ☑ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


## Authority records  ·  `browseActors`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/completeness/:actorId/recalc` | apiCompletenessRecalc | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/eac-cpf/:actorId` | apiEacExport | ahgAuthorityPlugin | | |
| ☐ | `/actor/:slug` | index | ahgActorManagePlugin | | |
| ☐ | `/actor/:slug/delete` | delete | ahgActorManagePlugin | | |
| ☐ | `/actor/:slug/edit` | edit | ahgActorManagePlugin | | |
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
| ☐ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | | |
| ☑ | `/admin/authority/functions/browse` | functionBrowse | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/authority/function/save` | apiFunctionSave | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/api/authority/function/:id/delete` | apiFunctionDelete | ahgAuthorityPlugin | | |
| ☐ | `/function/:slug` | view | ahgFunctionManagePlugin | | |
| ☐ | `/function/:slug/delete` | delete | ahgFunctionManagePlugin | | |
| ☐ | `/function/:slug/edit` | edit | ahgFunctionManagePlugin | | |
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
| ☐ | `/marketplace/sector/:sector` | sector | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/category/:sector/:slug` | category | ahgMarketplacePlugin | | |
| ☑ | `/marketplace/auctions` | auctionBrowse | ahgMarketplacePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/marketplace/featured` | featured | ahgMarketplacePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/marketplace/collection/:slug` | collection | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/seller/:slug` | seller | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/listing/:slug` | listing | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/buy/:slug` | buy | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/offer/:slug` | offerForm | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/bid/:slug` | bidForm | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/enquiry/:slug` | enquiryForm | ahgMarketplacePlugin | | |
| ☑ | `/marketplace/my/purchases` | myPurchases | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/my/bids` | myBids | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/my/offers` | myOffers | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/my/following` | myFollowing | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/marketplace/follow/:seller` | follow | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/review/:id` | reviewForm | ahgMarketplacePlugin | | |
| ☑ | `/marketplace/sell` | dashboard | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/register` | sellerRegister | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/profile` | sellerProfile | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/listings` | sellerListings | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/marketplace/sell/listings/create` | sellerListingCreate | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/marketplace/sell/listings/:id/edit` | sellerListingEdit | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/listings/:id/images` | sellerListingImages | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/listings/:id/publish` | sellerListingPublish | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/listings/:id/withdraw` | sellerListingWithdraw | ahgMarketplacePlugin | | |
| ☑ | `/marketplace/sell/offers` | sellerOffers | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/marketplace/sell/offers/:id/respond` | sellerOfferRespond | ahgMarketplacePlugin | | |
| ☑ | `/marketplace/sell/transactions` | sellerTransactions | ahgMarketplacePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/marketplace/sell/transactions/:id` | sellerTransactionDetail | ahgMarketplacePlugin | | |
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
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☑ | `/object/export` | index | ahgExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | | |
| ☐ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | | |
| ☑ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | | |
| ☑ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | | |
| ☑ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | PASS | HTTP 200 (pw 2026-06-27) |


# MENU: Browse — our collection


## Archival Holdings  ·  `browseInformationObjectsInstitution`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☑ | `/registry/admin/institutions` | adminInstitutions | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/institutions/verify` | adminInstitutionVerify | ahgRegistryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/institutions/:id/edit` | institutionEdit | ahgRegistryPlugin | | |
| ☑ | `/registry/my/institution` | myInstitutionDashboard | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/register` | institutionRegister | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/edit` | institutionEdit | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/contacts` | myInstitutionContacts | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/contacts/add` | myInstitutionContactAdd | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/institution/contacts/:id/edit` | myInstitutionContactEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/contacts/:id/delete` | myInstitutionContactDelete | ahgRegistryPlugin | | |
| ☑ | `/registry/my/institution/instances` | myInstitutionInstances | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/instances/add` | myInstitutionInstanceAdd | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/institution/instances/:id/edit` | myInstitutionInstanceEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/instances/:id/delink` | myInstitutionInstanceDelink | ahgRegistryPlugin | | |


## Digital objects  ·  `browseDigitalObjectsInstitution`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/informationobject/browse` | browse | ahgDisplayPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☑ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☑ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☑ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☑ | `/registry/admin/institutions` | adminInstitutions | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/admin/institutions/verify` | adminInstitutionVerify | ahgRegistryPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/institutions/:id/edit` | institutionEdit | ahgRegistryPlugin | | |
| ☑ | `/registry/my/institution` | myInstitutionDashboard | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/register` | institutionRegister | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/edit` | institutionEdit | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/contacts` | myInstitutionContacts | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/contacts/add` | myInstitutionContactAdd | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/institution/contacts/:id/edit` | myInstitutionContactEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/contacts/:id/delete` | myInstitutionContactDelete | ahgRegistryPlugin | | |
| ☑ | `/registry/my/institution/instances` | myInstitutionInstances | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/registry/my/institution/instances/add` | myInstitutionInstanceAdd | ahgRegistryPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/institution/instances/:id/edit` | myInstitutionInstanceEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/instances/:id/delink` | myInstitutionInstanceDelink | ahgRegistryPlugin | | |


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
| ☐ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | | |
| ☐ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | | |


## Admin  ·  `admin`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☑ | `/admin/rights` | index | ahgExtendedRightsPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/admin/rights/batch` | batch | ahgExtendedRightsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/admin/condition` | admin | ahgConditionPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/authority/dashboard` | dashboard | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/authority/workqueue` | workqueue | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/merge/:id` | merge | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/split/:id` | split | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | | |
| ☑ | `/admin/authority/functions/browse` | functionBrowse | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | | |
| ☑ | `/admin/authority/config` | config | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/authority/dedup` | index | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/authority/dedup/scan` | scan | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/admin/authority/dedup/compare/:id` | compare | ahgAuthorityPlugin | | |
| ☑ | `/admin/authority/ner-pipeline` | index | ahgAuthorityPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/admin/queue` | queueBrowse | ahgJobsManagePlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/admin/queue/detail/:id` | queueDetail | ahgJobsManagePlugin | | |
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
| ☐ | `/admin/forms/template/:id/edit` | templateEdit | ahgFormsPlugin | | |
| ☐ | `/admin/forms/template/:id/delete` | templateDelete | ahgFormsPlugin | | |
| ☐ | `/admin/forms/template/:id/clone` | templateClone | ahgFormsPlugin | | |
| ☐ | `/admin/forms/template/:id/export` | templateExport | ahgFormsPlugin | | |
| ☑ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | PASS | HTTP 302 (fixed #187) |
| ☐ | `/admin/forms/template/:id/builder` | builder | ahgFormsPlugin | | |
| ☑ | `/admin/forms/assignments` | assignments | ahgFormsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/admin/forms/assignment/create` | assignmentCreate | ahgFormsPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☐ | `/admin/forms/assignment/:id/delete` | assignmentDelete | ahgFormsPlugin | | |
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
| ☐ | `/security/clearance/:id` | view | ahgSecurityClearancePlugin | | |
| ☑ | `/security/clearance/grant` | grant | ahgSecurityClearancePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/security/clearance/:id/revoke` | revoke | ahgSecurityClearancePlugin | | |
| ☑ | `/security/clearance/bulk-grant` | bulkGrant | ahgSecurityClearancePlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
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
| ☐ | `/condition/check/:id/upload` | upload | ahgConditionPlugin | | |
| ☑ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/portable-export/api/clipboard-export` | apiClipboardExport | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/portable-export/download` | download | ahgPortableExportPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/tenant/branding/logo-upload` | uploadLogo | ahgMultiTenantPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☑ | `/privacyAdmin/downloadRedactedFile` | downloadRedactedFile | ahgPrivacyPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/training/upload` | apiTrainingUpload | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ai-condition/api/client-upload-consent` | apiClientUploadConsent | ahgAiConditionPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/researcher/api/upload` | apiUpload | ahgResearcherPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/cart/download/:token` | download | ahgCartPlugin | | |
| ☐ | `/media/download/:id` | download | ahgIiifPlugin | | |
| ☐ | `/api/v2/upload` | fileUpload | ahgAPIPlugin | N/A | HTTP 404 (pw 2026-06-27) |
| ☐ | `/api/v2/descriptions/:slug/upload` | descriptionUpload | ahgAPIPlugin | | |
| ☑ | `/ahg3DModel/upload` | upload | ahg3DModelPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/ingest/:id/upload` | upload | ahgIngestPlugin | | |
| ☐ | `/admin/preservation/package/:id/download` | packageDownload | ahgPreservationPlugin | | |
| ☑ | `/tiff-pdf-merge/upload` | upload | ahgPreservationPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/tiff-pdf-merge/download/:job_id` | download | ahgPreservationPlugin | | |
| ☑ | `/statistics/downloads` | downloads | ahgStatisticsPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/registry/my/vendor/software/:id/upload` | myVendorSoftwareUpload | ahgRegistryPlugin | | |
| ☑ | `/ftp-upload` | index | ahgFtpPlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/ftp-upload/upload` | upload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/chunk` | uploadChunk | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/list` | listFiles | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/delete` | deleteFile | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☑ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | PASS | HTTP 200 (pw 2026-06-27) |
| ☐ | `/loan/:id/upload-document` | uploadDocument | ahgLoanPlugin | | |
| ☑ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | PASS | HTTP 403 (pw 2026-06-27) |
| ☑ | `/api/report-builder/attachment/upload` | apiAttachmentUpload | ahgReportBuilderPlugin | PASS | HTTP 302 (pw 2026-06-27) |
| ☐ | `/research/reproduction/download/:token` | reproductionDownload | ahgResearchPlugin | | |
| ☐ | `/research/studio/:projectId/artefact/:artefactId/download` | studioDownload | ahgResearchPlugin | | |
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
| ☐ | `/admin/accessions/:id/appraisal/save` | appraisalSave | ahgAccessionManagePlugin | | |
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

---

# PART 2 — Screen panel detail (linked sub-functions)

---

## 1. ISAD(G) — Archival Description (Information Object)

The description view/edit screen (`/informationobject/<slug>` and its edit). From here a user can:

### 1.1 Core ISAD(G) description
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Identity area | Reference code, title, level of description, dates, extent | | |
| ☐ | Context area | Name of creator, admin/biographical history, archival history, acquisition | | |
| ☐ | Content & structure | Scope & content, appraisal, accruals, system of arrangement | | |
| ☐ | Conditions of access & use | Access conditions, reproduction, language, physical characteristics, finding aids | | |
| ☐ | Allied materials | Originals, copies, related units, publication note | | |
| ☐ | Notes / access points | Subjects, places, names, genres | | |
| ☐ | Description control | Identifier, rules/conventions, status, dates, language, sources | | |
| ☐ | Save / publish | Create → validation fires → save → publish (draft↔published) | | |

### 1.2 Provenance (ahgProvenancePlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | View provenance | Chain-of-custody timeline on the record | | |
| ☐ | Edit provenance record | Acquisition method, certainty, Nazi-era / cultural-property / POPIA fields | | |
| ☐ | Add event | Add a custody/transfer event | | |
| ☐ | Delete event | Remove an event | | |
| ☐ | Documents | Attach / delete a provenance document | | |
| ☐ | Authenticity report | C2PA + AI-inference trust verdict | | |

### 1.3 AI (ahgAIPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | NER | Extract persons / orgs / places / dates → link as access points | | |
| ☐ | Summarize | AI summary of scope & content | | |
| ☐ | Translate | Machine-translate the description | | |
| ☐ | Spellcheck | Spelling / grammar check | | |
| ☐ | Suggest description | LLM description suggestion | | |
| ☐ | Face detection | Detect faces on the digital object, match to authorities | | |

### 1.4 Rights (ahgRightsPlugin / ahgExtendedRightsPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | PREMIS rights | Add a rights statement (act, basis, restriction) | | |
| ☐ | Creative Commons | Apply a CC licence | | |
| ☐ | RightsStatements.org | Apply a rights-statement URI | | |
| ☐ | Embargo | Set an embargo-until date | | |
| ☐ | TK / ICIP labels | Apply Traditional-Knowledge labels | | |
| ☐ | Orphan works | Mark orphan-work status | | |

### 1.5 Digital object (ahgIiifPlugin / ahgDAMPlugin / ahg3DModelPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Upload | Attach a master digital object | | |
| ☐ | Derivatives | Reference + thumbnail generate | | |
| ☐ | IIIF viewer | Open the IIIF/Mirador viewer; deep-zoom | | |
| ☐ | Media | Audio/video player + waveform/transcription | | |
| ☐ | 3D | 3D model viewer, hotspots, AR | | |
| ☐ | Watermark | Apply derivative watermark | | |
| ☐ | Metadata extraction | EXIF / IPTC / XMP pulled into the record | | |

### 1.6 Other linked panels
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Security classification (ahgSecurityClearancePlugin) | Set classification + clearance/embargo gate | | |
| ☐ | Custom fields (ahgCustomFieldsPlugin) | Institution-defined fields render + save | | |
| ☐ | Audit trail (ahgAuditTrailPlugin) | Changes logged + viewable | | |
| ☐ | Version control (ahgVersionControlPlugin) | View versions / restore | | |
| ☐ | Preservation (ahgPreservationPlugin) | Checksum / fixity / PREMIS event | | |
| ☐ | Share link (ahgTimeLimitedShareLinkPlugin) | Create a time-limited public link | | |

---

## 2. ISAAR-CPF — Authority Record (Actor)

The actor view/edit screen (`/actor/<slug>`). From here a user can:

### 2.1 Core ISAAR-CPF
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Identity area | Type (person/family/corporate), authorised/parallel/other names, dates | | |
| ☐ | Description area | Places, legal status, functions/occupations, history, general context | | |
| ☐ | Relationships | Related actors (hierarchical/associative/temporal) | | |
| ☐ | Control area | Identifier, rules, status, level of detail, sources, maintenance | | |
| ☐ | Save / publish | Create → validate → save → publish | | |

### 2.2 Authority resolution (ahgAuthorityResolutionPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Match | Reconcile to ULAN / LCNAF / VIAF / Wikidata / ORCID | | |
| ☐ | Store identifier | Save the external URI on the actor | | |
| ☐ | Merge / dedupe | Merge duplicate authority records | | |

### 2.3 Contact (ahgContactPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Extended contact | Add phones / emails / addresses / web | | |

### 2.4 AI + linked records
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | AI (ahgAIPlugin) | NER / translate / summarize on the history | | |
| ☐ | Linked descriptions | Records created by / related to this actor | | |
| ☐ | Custom fields / audit | Custom fields render + save; changes logged | | |

---

## 3. ISDIAH — Repository (Archival Institution)

The repository view/edit screen (`/repository/<slug>`). From here a user can:

### 3.1 Core ISDIAH
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Identity area | Identifier, authorised/parallel names, type | | |
| ☐ | Contact area | Address, phone, email, contacts | | |
| ☐ | Description area | History, geo/cultural context, mandates, structure, holdings, finding aids | | |
| ☐ | Access area | Opening times, conditions, accessibility | | |
| ☐ | Services area | Research services, reproduction, public areas | | |
| ☐ | Control area | Identifier, rules, status, sources | | |

### 3.2 Repository extras
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Logo / theme | Upload logo; per-repository branding | | |
| ☐ | Holdings | Linked descriptions for this repository | | |
| ☐ | Uploads path | Digital objects route to the repo's NAS path | | |
| ☐ | Custom fields / audit | Render + save; changes logged | | |

---

## 4. Accession

The accession view/edit screen (`/accession/<slug>`). From here a user can:

### 4.1 Core accession
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Identity | Accession number, acquisition date, title, scope | | |
| ☐ | Acquisition | Source of acquisition, type, processing status/priority | | |
| ☐ | Appraisal / disposal | Appraisal, accrual, disposal notes | | |
| ☐ | Create description | Generate an information_object from the accession | | |

### 4.2 Donor & agreements (ahgDonorManagePlugin / ahgDonorAgreementPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Donor | Link / create a donor record (contact, PII) | | |
| ☐ | Donor agreement | Attach / generate the donor agreement (SA compliance) | | |

### 4.3 Rights holder & storage
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Rights holder (ahgRightsHolderManagePlugin) | Link / create a rights holder | | |
| ☐ | Physical storage (ahgStorageManagePlugin) | Assign a physical location / container | | |
| ☐ | Deaccession | Record a deaccession | | |
| ☐ | Audit | Changes logged | | |

---

## 5. Term / Taxonomy

The term view/edit + taxonomy browse (`/taxonomy/...`, `/term/<slug>`). From here a user can:

### 5.1 Term management (ahgTermTaxonomyPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Browse taxonomy | Open a taxonomy; navigate terms | | |
| ☐ | View term | Term detail + scope note | | |
| ☐ | Edit term (ACL-gated) | Preferred/alt labels, scope note, code | | |
| ☐ | Relationships | Broader / narrower / related (SKOS) | | |
| ☐ | Delete (ACL-gated) | Remove a non-protected term | | |
| ☐ | SKOS export | `/taxonomy/<id>/skos` export | | |

### 5.2 Semantic / thesaurus (ahgSemanticSearchPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Thesaurus sync | WordNet / Wikidata enrichment | | |
| ☐ | Used-in | Records using this term | | |

---

## 6. Function (ISDF)

The function view/edit screen (ahgFunctionManagePlugin). From here a user can:

| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Identity area | Type, authorised/parallel names, classification | | |
| ☐ | Context area | Dates, description, history, legislation | | |
| ☐ | Relationships | Related functions / actors | | |
| ☐ | Control area | Identifier, rules, status, sources | | |
| ☐ | Linked records | Actors / descriptions performing this function | | |

---

## 7. Digital Object (stand-alone view)

The digital-object view + actions (IIIF/DAM/preservation). From here a user can:

### 7.1 View & derivatives (ahgIiifPlugin / ahgDAMPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | View / stream | IIIF deep-zoom, media player, 3D viewer | | |
| ☐ | Derivatives | Reference + thumbnail; regen-derivatives | | |
| ☐ | DAM metadata | IPTC / XMP / EXIF panel | | |
| ☐ | Watermark | Apply / preview watermark | | |

### 7.2 Preservation (ahgPreservationPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Checksum / fixity | Generate checksum; verify fixity | | |
| ☐ | Format ID | Siegfried / PRONOM identification | | |
| ☐ | PREMIS event | Event recorded per action | | |
| ☐ | Replication | Replicate to a configured target | | |

### 7.3 Text & rights
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | OCR / HTR | Extract text from image/PDF | | |
| ☐ | Rights / ODRL | Access policy on the object (download gated) | | |

---

## 8. Research Portal

The researcher-facing area (`/research/...`). From here a user can:

### 8.1 Researcher & reading room (ahgResearchPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Registration / profile | Register; set experience level | | |
| ☐ | Booking | Reading-room booking; seat map; retrieval queue | | |
| ☐ | Projects | Create a research project / evidence set | | |
| ☐ | Journal & annotations | Research journal; annotation studio | | |
| ☐ | Bibliographies | Build / export a bibliography (citation formats) | | |
| ☐ | DMP | Author a Data Management Plan | | |

### 8.2 Requests & datasets
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Request to publish (ahgRequestToPublishPlugin) | Submit a publication request; receipt token; curator inbox | | |
| ☐ | Cart (ahgCartPlugin) | Add reproductions; checkout; pay (PayFast); download | | |
| ☐ | Favorites (ahgFavoritesPlugin) | Bookmark records | | |
| ☐ | RDM datasets (ahgRdmPlugin) | Deposit → POPIA scan → gate → DOI → landing (see RDM) | | |

---

## 9. GLAM Browse & Search

The public discovery surface. From here a user can:

### 9.1 Browse & display (ahgDisplayPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | GLAM browse | Display modes; grid/list | | |
| ☐ | Guest published-only | Logged-out users see published records only | | |
| ☐ | Landing page (ahgLandingPagePlugin) | Visual landing blocks render | | |

### 9.2 Search (ahgSearchPlugin / ahgSemanticSearchPlugin / ahgDiscoveryPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Global search | Query + autocomplete | | |
| ☐ | Facets | Filter by repository / level / date / subject | | |
| ☐ | Semantic / discovery | Natural-language query; semantic results | | |

### 9.3 Sector browse
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Library (ahgLibraryPlugin) | OPAC search; FRBR clusters; export (CSV/BibTeX/RIS); MARC | | |
| ☐ | Museum (ahgMuseumPlugin) | Museum browse; Spectrum; CIDOC-CRM | | |
| ☐ | Gallery (ahgGalleryPlugin) | Gallery browse / show | | |
| ☐ | DAM (ahgDAMPlugin) | DAM browse; rights/technical metadata | | |

---

## 10. Reports & Dashboards

The reporting/admin surface (`/reports`). From here a user (admin) can:

### 10.1 Reports (ahgReportsPlugin / ahgReportBuilderPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Central reports | Descriptions / authorities / repositories / accessions reports | | |
| ☐ | Report builder | Sections, rich text, SQL queries, templates | | |
| ☐ | Export | Word / PDF / XLSX / CSV | | |
| ☐ | Sharing / scheduling | Time-limited share link; scheduled run | | |

### 10.2 Statistics, audit & compliance
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Statistics (ahgStatisticsPlugin) | Usage stats | | |
| ☐ | Audit reports (ahgAuditTrailPlugin) | Logs; statistics; seal/chain | | |
| ☐ | Privacy / data protection (ahgPrivacyPlugin / ahgCDPAPlugin) | PII scan; DPIA/ROPA; POPIA/GDPR/CDPA | | |
| ☐ | Heritage accounting (ahgHeritageAccountingPlugin / ahgIPSASPlugin) | GRAP 103 / IPSAS asset reports | | |
| ☐ | RDM compliance / dashboard (ahgRdmPlugin) | Scoreboard + roll-up dashboard | | |

---

*Coverage: the central GLAM entity screens + the cross-cutting panels and surfaces. Add institution-specific screens (Zimbabwe NAZ/NMMZ/CDPA, exhibitions, loans, heritage discovery) as needed.*
