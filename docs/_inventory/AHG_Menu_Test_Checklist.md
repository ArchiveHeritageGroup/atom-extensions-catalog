# AHG — Menu-Driven Manual Test Checklist

Every navigation menu item is a **screen**; under each, every link/URL reachable from it is a tick-box test item. Walk the menus top-to-bottom. Tick ☐→☑; record Pass/Fail + notes.

Source: AtoM `menu` table + plugin route registrations. Generated 2026-06-27.


# MENU: Add (create records)


## Archival descriptions  ·  `addInformationObject`

*Linked panels & sub-functions:* Core ISAD(G) fields; linked panels — Provenance, AI (NER/summarise/translate/spellcheck/suggest/face), Rights (PREMIS/CC/RightsStatements/embargo/TK), Digital object (upload/IIIF/media/3D/watermark/metadata), Security classification, Custom fields, Audit, Version control, Preservation, Share link

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | | |
| ☐ | `/informationobject/browse` | browse | ahgDisplayPlugin | | |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☐ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | | |
| ☐ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | | |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☐ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | | |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☐ | `/object/export` | index | ahgExportPlugin | | |
| ☐ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | | |
| ☐ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | | |
| ☐ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | | |
| ☐ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | | |
| ☐ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | | |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | | |


## Accession records  ·  `addAccessionRecord`

*Linked panels & sub-functions:* Core accession; Donor + donor agreement, Rights holder, Physical storage, create-description, deaccession, audit

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/donor/autocomplete/accessions` | autocompleteAccessions | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/autocomplete/records` | autocompleteRecords | ahgDonorAgreementPlugin | | |
| ☐ | `/accession/:slug` | index | ahgAccessionManagePlugin | | |
| ☐ | `/accession/:slug/delete` | delete | ahgAccessionManagePlugin | | |
| ☐ | `/accession/:slug/edit` | edit | ahgAccessionManagePlugin | | |
| ☐ | `/accession/browse` | browse | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/dashboard` | dashboard | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/submit` | submit | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/review` | review | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/accept` | accept | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/reject` | reject | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/return` | returnRevision | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/timeline` | timeline | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/checklist` | checklist | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/attachments` | attachments | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/intake` | queueDetail | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/queue` | queue | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/queue/assign` | assign | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/config` | config | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/numbering` | numbering | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/checklist/:id/toggle` | apiChecklistToggle | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/checklist/apply-template` | apiChecklistApplyTemplate | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/attachment/:id/delete` | apiAttachmentDelete | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/appraisal` | appraisal | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/appraisal/save` | appraisalSave | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/valuation` | valuation | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/valuation/add` | valuationAdd | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/appraisal-templates` | appraisalTemplates | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/valuation-report` | valuationReport | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/appraisal/:id/score` | apiAppraisalScore | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/containers` | containers | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/rights` | rights | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container/save` | apiContainerSave | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container/:id/delete` | apiContainerDelete | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container-item/save` | apiContainerItemSave | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container-item/:id/delete` | apiContainerItemDelete | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container-item/:id/link` | apiContainerItemLink | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/barcode/lookup` | apiBarcodeLookup | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/rights/save` | apiRightsSave | ahgAccessionManagePlugin | | |


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
| ☐ | `/actor/add` | edit | ahgActorManagePlugin | | |
| ☐ | `/actor/browse` | browse | ahgActorManagePlugin | | |
| ☐ | `/actor/autocomplete` | autocomplete | ahgActorManagePlugin | | |
| ☐ | `/api/heritage/actor-autocomplete` | actorAutocomplete | ahgHeritageAccountingPlugin | | |
| ☐ | `/informationobject/actorAutocomplete` | actorAutocomplete | ahgInformationObjectManagePlugin | | |


## Archival institutions  ·  `addRepository`

*Linked panels & sub-functions:* Core ISDIAH fields; logo/theme, holdings, uploads path, custom fields, audit

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/repository/add` | edit | ahgRepositoryManagePlugin | | |
| ☐ | `/repository/browse` | browse | ahgRepositoryManagePlugin | | |
| ☐ | `/statistics/repository/:id` | repository | ahgStatisticsPlugin | | |
| ☐ | `/export/repository` | repository | ahgExportPlugin | | |
| ☐ | `/informationobject/repositoryAutocomplete` | repositoryAutocomplete | ahgInformationObjectManagePlugin | | |


## Terms  ·  `addTerm`

*Linked panels & sub-functions:* Term labels/scope/relationships (SKOS); semantic/thesaurus sync, used-in, SKOS export

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/term/:slug/edit` | edit | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug/delete` | delete | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug` | index | ahgTermTaxonomyPlugin | | |
| ☐ | `/api/v2/taxonomies/:id/terms` | taxonomyTerms | ahgAPIPlugin | | |
| ☐ | `/informationobject/termAutocomplete` | termAutocomplete | ahgInformationObjectManagePlugin | | |


## Function  ·  `addFunction`

*Linked panels & sub-functions:* Core ISDF fields; relationships, linked records

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/functions/browse` | functionBrowse | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/function/save` | apiFunctionSave | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/function/:id/delete` | apiFunctionDelete | ahgAuthorityPlugin | | |
| ☐ | `/function/:slug` | view | ahgFunctionManagePlugin | | |
| ☐ | `/function/:slug/delete` | delete | ahgFunctionManagePlugin | | |
| ☐ | `/function/:slug/edit` | edit | ahgFunctionManagePlugin | | |
| ☐ | `/function/add` | edit | ahgFunctionManagePlugin | | |
| ☐ | `/function/browse` | browse | ahgFunctionManagePlugin | | |


# MENU: Manage


## Accessions  ·  `accessions`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/donor/autocomplete/accessions` | autocompleteAccessions | ahgDonorAgreementPlugin | | |
| ☐ | `/accession/:slug` | index | ahgAccessionManagePlugin | | |
| ☐ | `/accession/:slug/delete` | delete | ahgAccessionManagePlugin | | |
| ☐ | `/accession/:slug/edit` | edit | ahgAccessionManagePlugin | | |
| ☐ | `/accession/browse` | browse | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/dashboard` | dashboard | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/submit` | submit | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/review` | review | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/accept` | accept | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/reject` | reject | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/return` | returnRevision | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/timeline` | timeline | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/checklist` | checklist | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/attachments` | attachments | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/intake` | queueDetail | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/queue` | queue | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/queue/assign` | assign | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/config` | config | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/numbering` | numbering | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/checklist/:id/toggle` | apiChecklistToggle | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/checklist/apply-template` | apiChecklistApplyTemplate | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/attachment/:id/delete` | apiAttachmentDelete | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/appraisal` | appraisal | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/appraisal/save` | appraisalSave | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/valuation` | valuation | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/valuation/add` | valuationAdd | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/appraisal-templates` | appraisalTemplates | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/valuation-report` | valuationReport | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/appraisal/:id/score` | apiAppraisalScore | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/containers` | containers | ahgAccessionManagePlugin | | |
| ☐ | `/admin/accessions/:id/rights` | rights | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container/save` | apiContainerSave | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container/:id/delete` | apiContainerDelete | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container-item/save` | apiContainerItemSave | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container-item/:id/delete` | apiContainerItemDelete | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container-item/:id/link` | apiContainerItemLink | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/barcode/lookup` | apiBarcodeLookup | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/rights/save` | apiRightsSave | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/rights/:id/delete` | apiRightsDelete | ahgAccessionManagePlugin | | |


## Donors  ·  `donors`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/donor/dashboard` | dashboard | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/agreement/browse` | browse | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/agreement/add` | add | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/agreement/:id` | view | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/agreement/:id/edit` | edit | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/agreement/:id/delete` | delete | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/agreement/reminders` | reminders | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/autocomplete/accessions` | autocompleteAccessions | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/autocomplete/records` | autocompleteRecords | ahgDonorAgreementPlugin | | |
| ☐ | `/donor/:slug` | view | ahgDonorManagePlugin | | |
| ☐ | `/donor/:slug/delete` | delete | ahgDonorManagePlugin | | |
| ☐ | `/donor/:slug/edit` | edit | ahgDonorManagePlugin | | |
| ☐ | `/donor/add` | edit | ahgDonorManagePlugin | | |
| ☐ | `/donor/browse` | browse | ahgDonorManagePlugin | | |


## Jobs  ·  `jobs`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/jobs` | browse | ahgJobsManagePlugin | | |
| ☐ | `/jobs/report/:id` | report | ahgJobsManagePlugin | | |
| ☐ | `/jobs/delete` | delete | ahgJobsManagePlugin | | |
| ☐ | `/jobs/export` | export | ahgJobsManagePlugin | | |
| ☐ | `/api/v2/sharepoint/push/jobs/:id` | pushJob | ahgSharePointPlugin | | |
| ☐ | `/ingest/ajax/job-status` | jobStatus | ahgIngestPlugin | | |
| ☐ | `/tiff-pdf-merge/job/:job_id` | getJob | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/download/:job_id` | download | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/jobs` | browse | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/job/:job_id/view` | view | ahgPreservationPlugin | | |
| ☐ | `/research/extraction-job/create` | createExtractionJob | ahgResearchPlugin | | |
| ☐ | `/research/extraction-job/:id` | viewExtractionJob | ahgResearchPlugin | | |
| ☐ | `/research/extraction-jobs/:project_id` | extractionJobs | ahgResearchPlugin | | |


## Physical storage  ·  `browsePhysicalObjects`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | | |
| ☐ | `/informationobject/browse` | browse | ahgDisplayPlugin | | |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☐ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | | |
| ☐ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | | |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☐ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | | |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☐ | `/object/export` | index | ahgExportPlugin | | |
| ☐ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | | |
| ☐ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | | |
| ☐ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | | |
| ☐ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | | |
| ☐ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | | |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | | |


## Rights holders  ·  `rightsholders`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/rightsholder/:slug` | view | ahgRightsHolderManagePlugin | | |
| ☐ | `/rightsholder/:slug/delete` | delete | ahgRightsHolderManagePlugin | | |
| ☐ | `/rightsholder/:slug/edit` | edit | ahgRightsHolderManagePlugin | | |
| ☐ | `/rightsholder/add` | edit | ahgRightsHolderManagePlugin | | |
| ☐ | `/rightsholder/browse` | browse | ahgRightsHolderManagePlugin | | |


## Taxonomies  ·  `taxonomies`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/api/v2/taxonomies` | taxonomiesBrowse | ahgAPIPlugin | | |
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
| ☐ | `/requesttopublish/browse` | browse | ahgRequestToPublishPlugin | | |
| ☐ | `/requesttopublish` | browse | ahgRequestToPublishPlugin | | |
| ☐ | `/requesttopublish/` | browse | ahgRequestToPublishPlugin | | |
| ☐ | `/requesttopublish/receipt` | receipt | ahgRequestToPublishPlugin | | |
| ☐ | `/requesttopublish/receipt/:token` | receipt | ahgRequestToPublishPlugin | | |
| ☐ | `/requesttopublish/inbox` | inbox | ahgRequestToPublishPlugin | | |
| ☐ | `/requesttopublish/review/:id` | review | ahgRequestToPublishPlugin | | |


## Collection assistant  ·  `collectionAssistant`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/favorites/send-to-collection` | sendToCollection | ahgFavoritesPlugin | | |
| ☐ | `/marketplace/collection/:slug` | collection | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/collections` | sellerCollections | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/collections/create` | sellerCollectionCreate | ahgMarketplacePlugin | | |
| ☐ | `/researcher/from-collection/:collectionId` | createFromCollection | ahgResearcherPlugin | | |
| ☐ | `/manifest-collections/autocomplete` | autocomplete | ahgIiifPlugin | | |
| ☐ | `/manifest-collections` | index | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/new` | new | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/create` | create | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/reorder` | reorder | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/:id/view` | view | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/:id/edit` | edit | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/:id/update` | update | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/:id/delete` | delete | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/:id/items/add` | addItems | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/item/:item_id/remove` | removeItem | ahgIiifPlugin | | |
| ☐ | `/manifest-collection/:slug/manifest.json` | manifest | ahgIiifPlugin | | |
| ☐ | `/api/research/collections/:id` | collection | ahgResearchPlugin | | |
| ☐ | `/api/research/collections` | collections | ahgResearchPlugin | | |
| ☐ | `/research/collection/:id` | viewCollection | ahgResearchPlugin | | |
| ☐ | `/research/collections` | collections | ahgResearchPlugin | | |
| ☐ | `/research/ajax/add-to-collection` | addToCollection | ahgResearchPlugin | | |
| ☐ | `/research/ajax/create-collection` | createCollectionAjax | ahgResearchPlugin | | |
| ☐ | `/research/collection/:id/export/:format` | exportFindingAid | ahgResearchPlugin | | |
| ☐ | `/research/ro-crate/collection/:id` | packageCollection | ahgResearchPlugin | | |


## Researcher Copilot  ·  `researchCopilot`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/researcher` | dashboard | ahgResearcherPlugin | | |
| ☐ | `/researcher/submissions` | submissions | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/new` | newSubmission | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id` | viewSubmission | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/edit` | editSubmission | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/item/add` | addItem | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/item/:itemId` | editItem | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/item/:itemId/delete` | deleteItem | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/submit` | submit | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/resubmit` | resubmit | ahgResearcherPlugin | | |
| ☐ | `/researcher/from-collection/:collectionId` | createFromCollection | ahgResearcherPlugin | | |
| ☐ | `/researcher/import` | importExchange | ahgResearcherPlugin | | |
| ☐ | `/researcher/submission/:id/publish` | publish | ahgResearcherPlugin | | |
| ☐ | `/researcher/api/upload` | apiUpload | ahgResearcherPlugin | | |
| ☐ | `/researcher/api/delete-file` | apiDeleteFile | ahgResearcherPlugin | | |
| ☐ | `/researcher/api/autocomplete` | apiAutocomplete | ahgResearcherPlugin | | |
| ☐ | `/research/datasets` | index | ahgRdmPlugin | | |
| ☐ | `/research/datasets/dashboard` | dashboard | ahgRdmPlugin | | |
| ☐ | `/research/datasets/compliance` | compliance | ahgRdmPlugin | | |
| ☐ | `/research/datasets/create` | create | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id` | show | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/deposit` | deposit | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/scan` | scan | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/file/:fid` | fileDownload | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/findings/:fid/resolve` | resolveFinding | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/disposition` | disposition | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/dmp` | linkDmp | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/dmp/unlink` | unlinkDmp | ahgRdmPlugin | | |
| ☐ | `/research/datasets/:id/landing` | landing | ahgRdmPlugin | | |
| ☐ | `/admin/naz/researchers` | researchers | ahgNAZPlugin | | |
| ☐ | `/admin/naz/researcher/create` | researcherCreate | ahgNAZPlugin | | |
| ☐ | `/admin/naz/researcher/:id/edit` | researcherEdit | ahgNAZPlugin | | |
| ☐ | `/admin/naz/researcher/:id` | researcherView | ahgNAZPlugin | | |
| ☐ | `/naz/researchers` | researchers | ahgNAZPlugin | | |
| ☐ | `/api/research/stats` | stats | ahgResearchPlugin | | |
| ☐ | `/api/research/annotations` | annotations | ahgResearchPlugin | | |
| ☐ | `/api/research/bibliographies/:id/export/:format` | exportBibliography | ahgResearchPlugin | | |
| ☐ | `/api/research/bibliographies` | bibliographies | ahgResearchPlugin | | |
| ☐ | `/api/research/citations/:id/:format` | citation | ahgResearchPlugin | | |
| ☐ | `/api/research/bookings` | bookings | ahgResearchPlugin | | |


## Provenance graph  ·  `provenanceGraph`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | | |
| ☐ | `/api/graphql` | index | ahgGraphQLPlugin | | |
| ☐ | `/api/graphql/playground` | playground | ahgGraphQLPlugin | | |
| ☐ | `/:slug/cco/provenance` | provenance | ahgMuseumPlugin | | |
| ☐ | `/museum/provenance/save` | provenanceSave | ahgMuseumPlugin | | |
| ☐ | `/museum/provenance/get` | provenanceGet | ahgMuseumPlugin | | |
| ☐ | `/museum/provenance/delete` | provenanceDelete | ahgMuseumPlugin | | |
| ☐ | `/museum/provenance/export` | provenanceExport | ahgMuseumPlugin | | |
| ☐ | `/spectrum/provenance/ajax` | provenanceAjax | ahgSpectrumPlugin | | |
| ☐ | `/favorites/send-to-bibliography` | sendToBibliography | ahgFavoritesPlugin | | |
| ☐ | `/provenance/coverage` | coverage | ahgProvenancePlugin | | |
| ☐ | `/provenance/coverage-data` | apiCoverage | ahgProvenancePlugin | | |
| ☐ | `/provenance/trace/:id` | apiTrace | ahgProvenancePlugin | | |
| ☐ | `/provenance/authenticity/:id` | authenticity | ahgProvenancePlugin | | |
| ☐ | `/statistics/geographic` | geographic | ahgStatisticsPlugin | | |
| ☐ | `/api/research/bibliographies/:id/export/:format` | exportBibliography | ahgResearchPlugin | | |
| ☐ | `/api/research/bibliographies` | bibliographies | ahgResearchPlugin | | |
| ☐ | `/research/bibliography/:id/export/:format` | exportBibliography | ahgResearchPlugin | | |
| ☐ | `/research/bibliography/:id/add` | addBibliographyEntry | ahgResearchPlugin | | |
| ☐ | `/research/bibliography/:id` | viewBibliography | ahgResearchPlugin | | |
| ☐ | `/research/bibliographies` | bibliographies | ahgResearchPlugin | | |
| ☐ | `/research/ajax/add-to-bibliography` | addToBibliographyAjax | ahgResearchPlugin | | |
| ☐ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | | |
| ☐ | `/research/knowledge-graph-data` | knowledgeGraphData | ahgResearchPlugin | | |
| ☐ | `/research/knowledge-graph/:project_id` | knowledgeGraph | ahgResearchPlugin | | |
| ☐ | `/research/network-graph/:project_id/export/graphml` | exportGraphML | ahgResearchPlugin | | |
| ☐ | `/research/network-graph/:project_id/export/gexf` | exportGraphGEXF | ahgResearchPlugin | | |
| ☐ | `/research/network-graph-data` | networkGraphData | ahgResearchPlugin | | |
| ☐ | `/research/network-graph/:project_id` | networkGraph | ahgResearchPlugin | | |


# MENU: Import


## XML  ·  `importXml`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | | |
| ☐ | `/ahgSettings/import` | import | ahgSettingsPlugin | | |
| ☐ | `/portable-export/import` | import | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | | |
| ☐ | `/favorites/import` | import | ahgFavoritesPlugin | | |
| ☐ | `/acquisition/bulk-import` | bulkImport | ahgLibraryPlugin | | |
| ☐ | `/acquisition/bulk-import-sample` | bulkImportSample | ahgLibraryPlugin | | |
| ☐ | `/library/copy-cataloguing/import` | import | ahgLibraryPlugin | | |
| ☐ | `/researcher/import` | importExchange | ahgResearcherPlugin | | |
| ☐ | `/admin/customFields/import` | import | ahgCustomFieldsPlugin | | |
| ☐ | `/registry/admin/import` | adminImport | ahgRegistryPlugin | | |
| ☐ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | | |
| ☐ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | | |
| ☐ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | | |


## CSV  ·  `importCsv`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | | |
| ☐ | `/ahgSettings/import` | import | ahgSettingsPlugin | | |
| ☐ | `/portable-export/import` | import | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | | |
| ☐ | `/favorites/import` | import | ahgFavoritesPlugin | | |
| ☐ | `/acquisition/bulk-import` | bulkImport | ahgLibraryPlugin | | |
| ☐ | `/acquisition/bulk-import-sample` | bulkImportSample | ahgLibraryPlugin | | |
| ☐ | `/library/copy-cataloguing/import` | import | ahgLibraryPlugin | | |
| ☐ | `/researcher/import` | importExchange | ahgResearcherPlugin | | |
| ☐ | `/admin/customFields/import` | import | ahgCustomFieldsPlugin | | |
| ☐ | `/registry/admin/import` | adminImport | ahgRegistryPlugin | | |
| ☐ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | | |
| ☐ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | | |
| ☐ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | | |


## Validate CSV  ·  `validateCsv`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | | |
| ☐ | `/ingest/:id/validate` | validate | ahgIngestPlugin | | |
| ☐ | `/api/preservation/package/validate` | apiPackageValidate | ahgPreservationPlugin | | |
| ☐ | `/api/report-builder/query/validate` | apiQueryValidate | ahgReportBuilderPlugin | | |
| ☐ | `/research/bulk-validate` | bulkValidate | ahgResearchPlugin | | |
| ☐ | `/research/validate/:id` | validateResult | ahgResearchPlugin | | |


## SKOS  ·  `importSkos`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | | |
| ☐ | `/ahgSettings/import` | import | ahgSettingsPlugin | | |
| ☐ | `/portable-export/import` | import | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | | |
| ☐ | `/favorites/import` | import | ahgFavoritesPlugin | | |
| ☐ | `/acquisition/bulk-import` | bulkImport | ahgLibraryPlugin | | |
| ☐ | `/acquisition/bulk-import-sample` | bulkImportSample | ahgLibraryPlugin | | |
| ☐ | `/library/copy-cataloguing/import` | import | ahgLibraryPlugin | | |
| ☐ | `/researcher/import` | importExchange | ahgResearcherPlugin | | |
| ☐ | `/admin/customFields/import` | import | ahgCustomFieldsPlugin | | |
| ☐ | `/registry/admin/import` | adminImport | ahgRegistryPlugin | | |
| ☐ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | | |
| ☐ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | | |
| ☐ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | | |


## FTP Upload  ·  `ftpUpload`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/condition/check/:id/upload` | upload | ahgConditionPlugin | | |
| ☐ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | | |
| ☐ | `/tenant/branding/logo-upload` | uploadLogo | ahgMultiTenantPlugin | | |
| ☐ | `/ai-condition/api/training/upload` | apiTrainingUpload | ahgAiConditionPlugin | | |
| ☐ | `/ai-condition/api/client-upload-consent` | apiClientUploadConsent | ahgAiConditionPlugin | | |
| ☐ | `/researcher/api/upload` | apiUpload | ahgResearcherPlugin | | |
| ☐ | `/api/v2/upload` | fileUpload | ahgAPIPlugin | | |
| ☐ | `/api/v2/descriptions/:slug/upload` | descriptionUpload | ahgAPIPlugin | | |
| ☐ | `/ahg3DModel/upload` | upload | ahg3DModelPlugin | | |
| ☐ | `/ingest/:id/upload` | upload | ahgIngestPlugin | | |
| ☐ | `/tiff-pdf-merge/upload` | upload | ahgPreservationPlugin | | |
| ☐ | `/registry/my/vendor/software/:id/upload` | myVendorSoftwareUpload | ahgRegistryPlugin | | |
| ☐ | `/ftp-upload` | index | ahgFtpPlugin | | |
| ☐ | `/ftp-upload/upload` | upload | ahgFtpPlugin | | |
| ☐ | `/ftp-upload/chunk` | uploadChunk | ahgFtpPlugin | | |
| ☐ | `/ftp-upload/list` | listFiles | ahgFtpPlugin | | |
| ☐ | `/ftp-upload/delete` | deleteFile | ahgFtpPlugin | | |
| ☐ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | | |
| ☐ | `/loan/:id/upload-document` | uploadDocument | ahgLoanPlugin | | |
| ☐ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | | |
| ☐ | `/api/report-builder/attachment/upload` | apiAttachmentUpload | ahgReportBuilderPlugin | | |
| ☐ | `/research/ajax/upload-note-image` | uploadNoteImage | ahgResearchPlugin | | |


# MENU: Admin


## Users  ·  `users`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/add` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/list` | browse | ahgUserManagePlugin | | |
| ☐ | `/user` | browse | ahgUserManagePlugin | | |
| ☐ | `/user/login` | login | ahgUserManagePlugin | | |
| ☐ | `/user/logout` | logout | ahgUserManagePlugin | | |
| ☐ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | | |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | | |
| ☐ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | | |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | | |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | | |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | | |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | | |


## Groups  ·  `groups`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☐ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | | |
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
| ☐ | `/staticpage/home` | edit | ahgStaticPagePlugin | | |
| ☐ | `/staticpage/add` | edit | ahgStaticPagePlugin | | |
| ☐ | `/staticpage/list` | list | ahgStaticPagePlugin | | |
| ☐ | `/privacyAdmin/getNerEntitiesForPage` | getNerEntitiesForPage | ahgPrivacyPlugin | | |
| ☐ | `/iiif/activity/page/:n` | activityPage | ahgIiifPlugin | | |
| ☐ | `/discovery/pageindex` | pageindex | ahgDiscoveryPlugin | | |
| ☐ | `/discovery/pageindex/api` | pageindexApi | ahgDiscoveryPlugin | | |
| ☐ | `/admin/landing-pages` | list | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/create` | create | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/:id/edit` | edit | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/:id/preview` | preview | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/add-block` | addBlock | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/update-block` | updateBlock | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/delete-block` | deleteBlock | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/duplicate-block` | duplicateBlock | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/reorder` | reorderBlocks | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/toggle-visibility` | toggleVisibility | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/get-config` | getBlockConfig | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/update-settings` | updateSettings | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/delete` | delete | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/save-draft` | saveDraft | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/publish` | publish | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/restore-version` | restoreVersion | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/move-to-column` | moveToColumn | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/reorder-column` | reorderColumnBlocks | ahgLandingPagePlugin | | |


## Menus  ·  `menu`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Menus** from the menu) | menu | core | | |


## Plugins  ·  `plugins`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/ahg-settings/plugins` | plugins | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/plugins` | plugins | ahgSettingsPlugin | | |
| ☐ | `/api/plugin-protection` | pluginProtection | ahgAPIPlugin | | |


## Themes  ·  `themes`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Themes** from the menu) | themes | core | | |


## Settings  ·  `settings`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/translation/settings` | settings | ahgTranslationPlugin | | |
| ☐ | `/glam/settings` | browseSettings | ahgDisplayPlugin | | |
| ☐ | `/glam/saveBrowseSettings` | saveBrowseSettings | ahgDisplayPlugin | | |
| ☐ | `/glam/getBrowseSettings` | getBrowseSettings | ahgDisplayPlugin | | |
| ☐ | `/glam/resetBrowseSettings` | resetBrowseSettings | ahgDisplayPlugin | | |
| ☐ | `/admin/ahg-settings` | index | ahgSettingsPlugin | | |
| ☐ | `/admin/ahg-settings/section` | section | ahgSettingsPlugin | | |
| ☐ | `/admin/ahg-settings/plugins` | plugins | ahgSettingsPlugin | | |
| ☐ | `/admin/ahg-settings/ai-services` | aiServices | ahgSettingsPlugin | | |
| ☐ | `/admin/ahg-settings/email` | email | ahgSettingsPlugin | | |
| ☐ | `/settings` | index | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/index` | index | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/export` | export | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/import` | import | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/reset` | reset | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/email` | email | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/emailTest` | emailTest | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/fusekiTest` | fusekiTest | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/ftpTest` | ftpTest | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/ldapTest` | ldapTest | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/plugins` | plugins | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/autoUpdate` | autoUpdate | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/saveTiffPdfSettings` | saveTiffPdfSettings | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/damTools` | damTools | ahgSettingsPlugin | | |
| ☐ | `/admin/ahg-settings/webhooks` | webhooks | ahgSettingsPlugin | | |
| ☐ | `/admin/ahg-settings/tts` | tts | ahgSettingsPlugin | | |
| ☐ | `/admin/ahg-settings/ahg-integration` | ahgIntegration | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/preservation` | preservation | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/levels` | levels | ahgSettingsPlugin | | |
| ☐ | `/ahgSettings/levelChoices` | levelChoices | ahgSettingsPlugin | | |
| ☐ | `/marketplace/admin/settings` | adminSettings | ahgMarketplacePlugin | | |
| ☐ | `/admin/authorityResolution/settings/lookup` | lookupSettings | ahgAuthorityResolutionPlugin | | |
| ☐ | `/ai-condition/settings` | settings | ahgAiConditionPlugin | | |
| ☐ | `/admin/iiif-settings` | settings | ahgIiifPlugin | | |
| ☐ | `/threeDReports/settings` | settings | ahgIiifPlugin | | |
| ☐ | `/mediaSettings/index` | index | ahgIiifPlugin | | |
| ☐ | `/mediaSettings/coverage` | coverage | ahgIiifPlugin | | |
| ☐ | `/mediaSettings/save` | save | ahgIiifPlugin | | |
| ☐ | `/mediaSettings/test` | test | ahgIiifPlugin | | |
| ☐ | `/mediaSettings/queue` | queue | ahgIiifPlugin | | |


## Description updates  ·  `descriptionUpdates`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/condition/photo/:id/update-meta` | updatePhotoMeta | ahgConditionPlugin | | |
| ☐ | `/ahgSettings/autoUpdate` | autoUpdate | ahgSettingsPlugin | | |
| ☐ | `/spectrum/:slug/workflow/update` | workflowUpdate | ahgSpectrumPlugin | | |
| ☐ | `/admin/doi/update/:id` | update | ahgDoiPlugin | | |
| ☐ | `/admin/scan/:id/update` | update | ahgScanPlugin | | |
| ☐ | `/admin/tenants/:id/update` | updateTenant | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | | |
| ☐ | `/reports/descriptions` | descriptions | ahgReportsPlugin | | |
| ☐ | `/privacy/dsar/:id/update` | dsarUpdate | ahgPrivacyPlugin | | |
| ☐ | `/cart/update-products` | updateProducts | ahgCartPlugin | | |
| ☐ | `/cart/update-item` | updateItem | ahgCartPlugin | | |
| ☐ | `/manifest-collection/:id/update` | update | ahgIiifPlugin | | |
| ☐ | `/media/audio-description/:id` | audioDescription | ahgIiifPlugin | | |
| ☐ | `/media/audio-description/:id/edit` | audioDescriptionEdit | ahgIiifPlugin | | |
| ☐ | `/api/v2/descriptions` | descriptionsBrowse | ahgAPIPlugin | | |
| ☐ | `/api/v2/descriptions/:slug/citation` | descriptionsCitation | ahgAPIPlugin | | |
| ☐ | `/api/v2/descriptions/:slug` | descriptionsRead | ahgAPIPlugin | | |
| ☐ | `/api/v2/descriptions/:slug/conditions` | descriptionConditions | ahgAPIPlugin | | |
| ☐ | `/api/v2/descriptions/:slug/asset` | descriptionAsset | ahgAPIPlugin | | |
| ☐ | `/api/v2/descriptions/:slug/upload` | descriptionUpload | ahgAPIPlugin | | |
| ☐ | `/registry/api/sync/update` | apiSyncUpdate | ahgRegistryPlugin | | |
| ☐ | `/search/descriptionUpdates` | descriptionUpdates | ahgSearchPlugin | | |
| ☐ | `/admin/landing-pages/ajax/update-block` | updateBlock | ahgLandingPagePlugin | | |
| ☐ | `/admin/landing-pages/ajax/update-settings` | updateSettings | ahgLandingPagePlugin | | |
| ☐ | `/research/hypothesis/:id/update` | updateHypothesis | ahgResearchPlugin | | |
| ☐ | `/research/odrl/update/:id` | updateOdrlPolicy | ahgResearchPlugin | | |
| ☐ | `/research/room/:id/update` | updateRoom | ahgResearchPlugin | | |


## Global search/replace  ·  `globalReplace`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/search/globalReplace` | globalReplace | ahgSearchPlugin | | |


## Visible elements  ·  `visibleElements`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Visible elements** from the menu) | visibleElements | core | | |


## Portable Export  ·  `portableExport`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/condition/check/:id/export` | exportReport | ahgConditionPlugin | | |
| ☐ | `/condition/template/:id/export` | template | ahgConditionPlugin | | |
| ☐ | `/jobs/export` | export | ahgJobsManagePlugin | | |
| ☐ | `/museum/provenance/export` | provenanceExport | ahgMuseumPlugin | | |
| ☐ | `/admin/forms/template/:id/export` | templateExport | ahgFormsPlugin | | |
| ☐ | `/glam/exportCsv` | exportCsv | ahgDisplayPlugin | | |
| ☐ | `/ahgSettings/export` | export | ahgSettingsPlugin | | |
| ☐ | `/spectrum/export` | export | ahgSpectrumPlugin | | |
| ☐ | `/portable-export` | index | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/start` | apiStartExport | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/quick-start` | apiQuickStart | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/clipboard-export` | apiClipboardExport | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/fonds-search` | apiFondsSearch | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/progress` | apiProgress | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/list` | apiList | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/delete` | apiDelete | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/token` | apiToken | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/estimate` | apiEstimate | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/download` | download | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/import` | import | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | | |
| ☐ | `/favorites/export/:format` | export | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/export/:format` | exportFolder | ahgFavoritesPlugin | | |
| ☐ | `/admin/doi/export` | export | ahgDoiPlugin | | |
| ☐ | `/library/export` | export | ahgLibraryPlugin | | |
| ☐ | `/library/marc-export` | marcExport | ahgLibraryPlugin | | |
| ☐ | `/library/kbart/export` | export | ahgLibraryPlugin | | |
| ☐ | `/admin/customFields/export` | export | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/integrity/export` | export | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/export/csv` | exportCsv | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/export/auditor` | exportAuditor | ahgIntegrityPlugin | | |
| ☐ | `/api/preservation/package/export` | apiPackageExport | ahgPreservationPlugin | | |
| ☐ | `/statistics/export` | export | ahgStatisticsPlugin | | |
| ☐ | `/export` | index | ahgExportPlugin | | |
| ☐ | `/export/archival` | archival | ahgExportPlugin | | |
| ☐ | `/export/authority` | authority | ahgExportPlugin | | |
| ☐ | `/export/repository` | repository | ahgExportPlugin | | |


## Integrity  ·  `integrity`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/integrity` | index | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/schedules` | schedules | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/schedule/edit` | scheduleEdit | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/runs` | runs | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/run/:id` | runDetail | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/ledger` | ledger | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/dead-letter` | deadLetter | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/report` | report | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/export` | export | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/export/csv` | exportCsv | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/export/auditor` | exportAuditor | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/policies` | policies | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/policy/edit` | policyEdit | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/holds` | holds | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/disposition` | disposition | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/records` | records | ahgIntegrityPlugin | | |
| ☐ | `/admin/integrity/alerts` | alerts | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/verify` | apiVerify | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/run/:id` | apiRun | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/schedule/:id/toggle` | apiScheduleToggle | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/schedule/:id/delete` | apiScheduleDelete | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/dead-letter/:id/action` | apiDeadLetterAction | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/stats` | apiStats | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/schedule/:id/run` | apiRunSchedule | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/policy/:id/toggle` | apiPolicyToggle | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/policy/:id/delete` | apiPolicyDelete | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/hold/place` | apiHoldPlace | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/hold/:id/release` | apiHoldRelease | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/disposition/:id/action` | apiDispositionAction | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/retention/scan` | apiRetentionScan | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/alert/save` | apiAlertSave | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/alert/:id/delete` | apiAlertDelete | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/ledger` | apiLedger | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/runs` | apiRuns | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/holds` | apiHolds | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/policies` | apiPolicies | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/daily-trend` | apiDailyTrend | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/repo-breakdown` | apiRepoBreakdown | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/format-breakdown` | apiFormatBreakdown | ahgIntegrityPlugin | | |
| ☐ | `/api/integrity/throughput` | apiThroughput | ahgIntegrityPlugin | | |


# MENU: Admin — Users


## Profile  ·  `userProfile`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/add` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/list` | browse | ahgUserManagePlugin | | |
| ☐ | `/user` | browse | ahgUserManagePlugin | | |
| ☐ | `/user/login` | login | ahgUserManagePlugin | | |
| ☐ | `/user/logout` | logout | ahgUserManagePlugin | | |
| ☐ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | | |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | | |
| ☐ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | | |
| ☐ | `/glam/profiles` | profiles | ahgDisplayPlugin | | |
| ☐ | `/glam/assignProfile` | assignProfile | ahgDisplayPlugin | | |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | | |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☐ | `/marketplace/sell/profile` | sellerProfile | ahgMarketplacePlugin | | |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | | |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | | |
| ☐ | `/api/research/profile` | profile | ahgResearchPlugin | | |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | | |
| ☐ | `/research/orcid/pull-profile` | orcidPullProfile | ahgResearchPlugin | | |
| ☐ | `/research/profile/api-keys` | apiKeys | ahgResearchPlugin | | |
| ☐ | `/research/profile` | profile | ahgResearchPlugin | | |


## Archival description permissions  ·  `userInformationObjectAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/add` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/list` | browse | ahgUserManagePlugin | | |
| ☐ | `/user` | browse | ahgUserManagePlugin | | |
| ☐ | `/user/login` | login | ahgUserManagePlugin | | |
| ☐ | `/user/logout` | logout | ahgUserManagePlugin | | |
| ☐ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | | |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | | |
| ☐ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | | |
| ☐ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | | |
| ☐ | `/informationobject/browse` | browse | ahgDisplayPlugin | | |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | | |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☐ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | | |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | | |
| ☐ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | | |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☐ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | | |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |


## Authority record permissions  ·  `userActorAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/add` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/list` | browse | ahgUserManagePlugin | | |
| ☐ | `/user` | browse | ahgUserManagePlugin | | |
| ☐ | `/user/login` | login | ahgUserManagePlugin | | |
| ☐ | `/user/logout` | logout | ahgUserManagePlugin | | |
| ☐ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | | |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | | |
| ☐ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | | |
| ☐ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/completeness/:actorId/recalc` | apiCompletenessRecalc | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/graph/:actorId` | apiGraphData | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/eac-cpf/:actorId` | apiEacExport | ahgAuthorityPlugin | | |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | | |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | | |
| ☐ | `/actor/:slug` | index | ahgActorManagePlugin | | |
| ☐ | `/actor/:slug/delete` | delete | ahgActorManagePlugin | | |
| ☐ | `/actor/:slug/edit` | edit | ahgActorManagePlugin | | |
| ☐ | `/actor/add` | edit | ahgActorManagePlugin | | |
| ☐ | `/actor/browse` | browse | ahgActorManagePlugin | | |
| ☐ | `/actor/autocomplete` | autocomplete | ahgActorManagePlugin | | |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | | |


## Archival institution permissions  ·  `userRepositoryAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/add` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/list` | browse | ahgUserManagePlugin | | |
| ☐ | `/user` | browse | ahgUserManagePlugin | | |
| ☐ | `/user/login` | login | ahgUserManagePlugin | | |
| ☐ | `/user/logout` | logout | ahgUserManagePlugin | | |
| ☐ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | | |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | | |
| ☐ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | | |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | | |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☐ | `/repository/add` | edit | ahgRepositoryManagePlugin | | |
| ☐ | `/repository/browse` | browse | ahgRepositoryManagePlugin | | |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | | |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
| ☐ | `/statistics/repository/:id` | repository | ahgStatisticsPlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | | |
| ☐ | `/export/repository` | repository | ahgExportPlugin | | |
| ☐ | `/informationobject/repositoryAutocomplete` | repositoryAutocomplete | ahgInformationObjectManagePlugin | | |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | | |


## Taxonomy permissions  ·  `userTermAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/:slug` | view | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/delete` | delete | ahgUserManagePlugin | | |
| ☐ | `/user/:slug/edit` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/add` | edit | ahgUserManagePlugin | | |
| ☐ | `/user/list` | browse | ahgUserManagePlugin | | |
| ☐ | `/user` | browse | ahgUserManagePlugin | | |
| ☐ | `/user/login` | login | ahgUserManagePlugin | | |
| ☐ | `/user/logout` | logout | ahgUserManagePlugin | | |
| ☐ | `/user/passwordEdit` | passwordEdit | ahgUserManagePlugin | | |
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | | |
| ☐ | `/user/passwordReset` | passwordReset | ahgUserManagePlugin | | |
| ☐ | `/term/:slug/edit` | edit | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug/delete` | delete | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug` | index | ahgTermTaxonomyPlugin | | |
| ☐ | `/sharepoint/user-mappings` | userMappings | ahgSharePointPlugin | | |
| ☐ | `/sharepoint/user-mappings/:id` | userMappingEdit | ahgSharePointPlugin | | |
| ☐ | `/admin/tenants/assign-user` | assignTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-user` | removeTenantUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/update-user-role` | updateTenantUserRole | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/:id/super-users` | superUsers | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/assign-super-user` | assignSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/admin/tenants/remove-super-user` | removeSuperUser | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/:id/users` | index | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/assign` | assign | ahgMultiTenantPlugin | | |
| ☐ | `/tenant/users/remove` | remove | ahgMultiTenantPlugin | | |
| ☐ | `/api/v2/taxonomies/:id/terms` | taxonomyTerms | ahgAPIPlugin | | |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users` | adminUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/manage` | adminUserManage | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/edit` | adminUserEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/users/:id/reset-password` | adminUserResetPassword | ahgRegistryPlugin | | |
| ☐ | `/informationobject/termAutocomplete` | termAutocomplete | ahgInformationObjectManagePlugin | | |
| ☐ | `/audit/user/:id` | user | ahgResearchPlugin | | |


# MENU: Admin — Groups


## Profile  ·  `groupProfile`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/glam/profiles` | profiles | ahgDisplayPlugin | | |
| ☐ | `/glam/assignProfile` | assignProfile | ahgDisplayPlugin | | |
| ☐ | `/marketplace/sell/profile` | sellerProfile | ahgMarketplacePlugin | | |
| ☐ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☐ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | | |
| ☐ | `/api/research/profile` | profile | ahgResearchPlugin | | |
| ☐ | `/research/orcid/pull-profile` | orcidPullProfile | ahgResearchPlugin | | |
| ☐ | `/research/profile/api-keys` | apiKeys | ahgResearchPlugin | | |
| ☐ | `/research/profile` | profile | ahgResearchPlugin | | |


## Archival description permissions  ·  `groupInformationObjectAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | | |
| ☐ | `/informationobject/browse` | browse | ahgDisplayPlugin | | |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☐ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | | |
| ☐ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | | |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☐ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | | |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☐ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☐ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | | |
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
| ☐ | `/actor/add` | edit | ahgActorManagePlugin | | |
| ☐ | `/actor/browse` | browse | ahgActorManagePlugin | | |
| ☐ | `/actor/autocomplete` | autocomplete | ahgActorManagePlugin | | |
| ☐ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☐ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | | |
| ☐ | `/api/heritage/actor-autocomplete` | actorAutocomplete | ahgHeritageAccountingPlugin | | |
| ☐ | `/informationobject/actorAutocomplete` | actorAutocomplete | ahgInformationObjectManagePlugin | | |


## Archival institution permissions  ·  `groupRepositoryAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/repository/add` | edit | ahgRepositoryManagePlugin | | |
| ☐ | `/repository/browse` | browse | ahgRepositoryManagePlugin | | |
| ☐ | `/statistics/repository/:id` | repository | ahgStatisticsPlugin | | |
| ☐ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☐ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | | |
| ☐ | `/export/repository` | repository | ahgExportPlugin | | |
| ☐ | `/informationobject/repositoryAutocomplete` | repositoryAutocomplete | ahgInformationObjectManagePlugin | | |


## Taxonomy permissions  ·  `groupTermAcl`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/term/:slug/edit` | edit | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug/delete` | delete | ahgTermTaxonomyPlugin | | |
| ☐ | `/term/:slug` | index | ahgTermTaxonomyPlugin | | |
| ☐ | `/api/v2/taxonomies/:id/terms` | taxonomyTerms | ahgAPIPlugin | | |
| ☐ | `/registry/admin/groups` | adminGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/verify` | adminGroupVerify | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/edit` | adminGroupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/members` | adminGroupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/groups/:id/email` | adminGroupEmail | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups` | myGroups | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/create` | groupCreate | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/edit` | groupEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/groups/:id/members` | groupMembersManage | ahgRegistryPlugin | | |
| ☐ | `/registry/groups` | groupBrowse | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/join` | groupJoin | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/leave` | groupLeave | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/notifications` | groupToggleNotifications | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions` | discussionList | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/new` | discussionNew | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id` | discussionView | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/discussions/:id/reply` | discussionReply | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug/members` | groupMembers | ahgRegistryPlugin | | |
| ☐ | `/registry/groups/:slug` | groupView | ahgRegistryPlugin | | |
| ☐ | `/informationobject/termAutocomplete` | termAutocomplete | ahgInformationObjectManagePlugin | | |


# MENU: Static pages


## Favorites  ·  `favorites`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/favorites` | browse | ahgFavoritesPlugin | | |
| ☐ | `/favorites/add/:slug` | add | ahgFavoritesPlugin | | |
| ☐ | `/favorites/remove/:id` | remove | ahgFavoritesPlugin | | |
| ☐ | `/favorites/clear` | clear | ahgFavoritesPlugin | | |
| ☐ | `/favorites/bulk` | bulk | ahgFavoritesPlugin | | |
| ☐ | `/favorites/move` | moveToFolder | ahgFavoritesPlugin | | |
| ☐ | `/favorites/notes/:id` | updateNotes | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/create` | folderCreate | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id` | folderView | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/edit` | folderEdit | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/delete` | folderDelete | ahgFavoritesPlugin | | |
| ☐ | `/favorites/ajax/toggle` | ajaxToggle | ahgFavoritesPlugin | | |
| ☐ | `/favorites/ajax/toggle-custom` | ajaxToggleCustom | ahgFavoritesPlugin | | |
| ☐ | `/favorites/ajax/search` | ajaxSearch | ahgFavoritesPlugin | | |
| ☐ | `/favorites/ajax/status/:slug` | ajaxStatus | ahgFavoritesPlugin | | |
| ☐ | `/favorites/ajax/folders` | ajaxFolders | ahgFavoritesPlugin | | |
| ☐ | `/favorites/export/:format` | export | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/export/:format` | exportFolder | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/share` | shareFolder | ahgFavoritesPlugin | | |
| ☐ | `/favorites/folder/:id/revoke-share` | revokeSharing | ahgFavoritesPlugin | | |
| ☐ | `/favorites/shared/:token` | viewShared | ahgFavoritesPlugin | | |
| ☐ | `/favorites/import` | import | ahgFavoritesPlugin | | |
| ☐ | `/favorites/send-to-collection` | sendToCollection | ahgFavoritesPlugin | | |
| ☐ | `/favorites/send-to-project` | sendToProject | ahgFavoritesPlugin | | |
| ☐ | `/favorites/send-to-bibliography` | sendToBibliography | ahgFavoritesPlugin | | |
| ☐ | `/registry/favorite/toggle` | favoriteToggle | ahgRegistryPlugin | | |
| ☐ | `/registry/my/favorites` | myFavorites | ahgRegistryPlugin | | |


## Feedback  ·  `feedbackMenu`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | (open **Feedback** from the menu) | feedbackMenu | core | | |


## Cart  ·  `cart`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/cart` | browse | ahgCartPlugin | | |
| ☐ | `/cart/browse` | browse | ahgCartPlugin | | |
| ☐ | `/cart/add/:slug` | add | ahgCartPlugin | | |
| ☐ | `/cart/remove/:id` | remove | ahgCartPlugin | | |
| ☐ | `/cart/clear` | clear | ahgCartPlugin | | |
| ☐ | `/cart/thank-you` | thankYou | ahgCartPlugin | | |
| ☐ | `/cart/checkout` | checkout | ahgCartPlugin | | |
| ☐ | `/cart/update-products` | updateProducts | ahgCartPlugin | | |
| ☐ | `/cart/update-item` | updateItem | ahgCartPlugin | | |
| ☐ | `/cart/save-selections` | saveSelections | ahgCartPlugin | | |
| ☐ | `/cart/payment-return/:order` | paymentReturn | ahgCartPlugin | | |
| ☐ | `/cart/payment/:order` | payment | ahgCartPlugin | | |
| ☐ | `/cart/payment/success/:order` | paymentSuccess | ahgCartPlugin | | |
| ☐ | `/cart/payment/cancel/:order` | paymentCancel | ahgCartPlugin | | |
| ☐ | `/cart/payment/notify` | paymentNotify | ahgCartPlugin | | |
| ☐ | `/cart/order/:order` | orderConfirmation | ahgCartPlugin | | |
| ☐ | `/cart/orders` | orders | ahgCartPlugin | | |
| ☐ | `/cart/download/:token` | download | ahgCartPlugin | | |


# MENU: Browse / Discovery


## Archival descriptions  ·  `browseInformationObjects`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | | |
| ☐ | `/informationobject/browse` | browse | ahgDisplayPlugin | | |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☐ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | | |
| ☐ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | | |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☐ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | | |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☐ | `/object/export` | index | ahgExportPlugin | | |
| ☐ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | | |
| ☐ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | | |
| ☐ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | | |
| ☐ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | | |
| ☐ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | | |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | | |


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
| ☐ | `/actor/add` | edit | ahgActorManagePlugin | | |
| ☐ | `/actor/browse` | browse | ahgActorManagePlugin | | |
| ☐ | `/actor/autocomplete` | autocomplete | ahgActorManagePlugin | | |
| ☐ | `/api/heritage/actor-autocomplete` | actorAutocomplete | ahgHeritageAccountingPlugin | | |
| ☐ | `/informationobject/actorAutocomplete` | actorAutocomplete | ahgInformationObjectManagePlugin | | |


## Archival institutions  ·  `browseRepositories`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/reports/repositories` | repositories | ahgReportsPlugin | | |
| ☐ | `/api/v2/repositories` | repositoriesBrowse | ahgAPIPlugin | | |


## Functions  ·  `browseFunctions`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/functions/browse` | functionBrowse | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/function/save` | apiFunctionSave | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/function/:id/delete` | apiFunctionDelete | ahgAuthorityPlugin | | |
| ☐ | `/function/:slug` | view | ahgFunctionManagePlugin | | |
| ☐ | `/function/:slug/delete` | delete | ahgFunctionManagePlugin | | |
| ☐ | `/function/:slug/edit` | edit | ahgFunctionManagePlugin | | |
| ☐ | `/function/add` | edit | ahgFunctionManagePlugin | | |
| ☐ | `/function/browse` | browse | ahgFunctionManagePlugin | | |


## Subjects  ·  `browseSubjects`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/library/suggestSubjects` | suggestSubjects | ahgLibraryPlugin | | |
| ☐ | `/admin/library/subjects` | subjects | ahgLibraryPlugin | | |


## Places  ·  `browsePlaces`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/marketplace` | browse | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/search` | search | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sector/:sector` | sector | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/category/:sector/:slug` | category | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/auctions` | auctionBrowse | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/featured` | featured | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/collection/:slug` | collection | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/seller/:slug` | seller | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/listing/:slug` | listing | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/buy/:slug` | buy | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/offer/:slug` | offerForm | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/bid/:slug` | bidForm | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/enquiry/:slug` | enquiryForm | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/my/purchases` | myPurchases | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/my/bids` | myBids | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/my/offers` | myOffers | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/my/following` | myFollowing | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/follow/:seller` | follow | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/review/:id` | reviewForm | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell` | dashboard | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/register` | sellerRegister | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/profile` | sellerProfile | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/listings` | sellerListings | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/listings/create` | sellerListingCreate | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/listings/:id/edit` | sellerListingEdit | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/listings/:id/images` | sellerListingImages | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/listings/:id/publish` | sellerListingPublish | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/listings/:id/withdraw` | sellerListingWithdraw | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/offers` | sellerOffers | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/offers/:id/respond` | sellerOfferRespond | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/transactions` | sellerTransactions | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/transactions/:id` | sellerTransactionDetail | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/payouts` | sellerPayouts | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/reviews` | sellerReviews | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/enquiries` | sellerEnquiries | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/collections` | sellerCollections | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/collections/create` | sellerCollectionCreate | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/sell/analytics` | sellerAnalytics | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/admin` | adminDashboard | ahgMarketplacePlugin | | |
| ☐ | `/marketplace/admin/listings` | adminListings | ahgMarketplacePlugin | | |


## Digital objects  ·  `browseDigitalObjects`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | | |
| ☐ | `/informationobject/browse` | browse | ahgDisplayPlugin | | |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☐ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | | |
| ☐ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | | |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☐ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | | |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☐ | `/object/export` | index | ahgExportPlugin | | |
| ☐ | `/security/request-object` | requestObject | ahgAccessRequestPlugin | | |
| ☐ | `/security/request-object/create` | createObjectRequest | ahgAccessRequestPlugin | | |
| ☐ | `/heritage/object/:slug` | viewByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/heritage/object/:slug/edit` | editByObject | ahgHeritageAccountingPlugin | | |
| ☐ | `/loan/:id/add-object` | addObject | ahgLoanPlugin | | |
| ☐ | `/loan/:id/remove-object` | removeObject | ahgLoanPlugin | | |
| ☐ | `/loan/search-objects` | searchObjects | ahgLoanPlugin | | |
| ☐ | `/informationobject/:slug/delete` | delete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/:slug/edit` | edit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/edit` | doEdit | ahgInformationObjectManagePlugin | | |
| ☐ | `/digitalobject/:id/delete` | doDelete | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/treeview` | treeview | ahgInformationObjectManagePlugin | | |
| ☐ | `/informationobject/treeviewFull` | treeviewFull | ahgInformationObjectManagePlugin | | |


# MENU: Browse — our collection


## Archival Holdings  ·  `browseInformationObjectsInstitution`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | | |
| ☐ | `/informationobject/browse` | browse | ahgDisplayPlugin | | |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☐ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | | |
| ☐ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | | |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☐ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | | |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☐ | `/registry/admin/institutions` | adminInstitutions | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/institutions/verify` | adminInstitutionVerify | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/institutions/:id/edit` | institutionEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution` | myInstitutionDashboard | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/register` | institutionRegister | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/edit` | institutionEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/contacts` | myInstitutionContacts | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/contacts/add` | myInstitutionContactAdd | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/contacts/:id/edit` | myInstitutionContactEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/contacts/:id/delete` | myInstitutionContactDelete | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/instances` | myInstitutionInstances | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/instances/add` | myInstitutionInstanceAdd | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/instances/:id/edit` | myInstitutionInstanceEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/instances/:id/delink` | myInstitutionInstanceDelink | ahgRegistryPlugin | | |


## Digital objects  ·  `browseDigitalObjectsInstitution`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/object/autocomplete` | objectAutocomplete | ahgConditionPlugin | | |
| ☐ | `/informationobject/browse` | browse | ahgDisplayPlugin | | |
| ☐ | `/api/spectrum/objects/:object_id/events` | spectrumObjectEvents | ahgSpectrumPlugin | | |
| ☐ | `/spectrumReports/objectEntry` | objectEntry | ahgSpectrumPlugin | | |
| ☐ | `/ai-condition/api/object-search` | apiObjectSearch | ahgAiConditionPlugin | | |
| ☐ | `/workflow/history/:object_id` | objectHistory | ahgWorkflowPlugin | | |
| ☐ | `/workflow/start/:object_id` | startWorkflow | ahgWorkflowPlugin | | |
| ☐ | `/workflow/timeline/:object_id` | timeline | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-readiness/:object_id` | publishReadiness | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-simulate/:object_id` | publishSimulate | ahgWorkflowPlugin | | |
| ☐ | `/workflow/publish-execute/:object_id` | publishExecute | ahgWorkflowPlugin | | |
| ☐ | `/iiif/annotations/object/:id` | annotationsList | ahgIiifPlugin | | |
| ☐ | `/admin/iiif-validation/run/:object_id` | validationRun | ahgIiifPlugin | | |
| ☐ | `/iiif/ocr/object/:id` | ocrExport | ahgIiifPlugin | | |
| ☐ | `/threeDReports/digitalObjects` | digitalObjects | ahgIiifPlugin | | |
| ☐ | `/exhibition/:id/objects` | objects | ahgExhibitionPlugin | | |
| ☐ | `/exhibition/:id/object-list` | objectList | ahgExhibitionPlugin | | |
| ☐ | `/api/3d/models/:object_id` | apiModels | ahg3DModelPlugin | | |
| ☐ | `/customFields/get/:entityType/:objectId` | getValues | ahgCustomFieldsPlugin | | |
| ☐ | `/admin/preservation/object/:id` | object | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/add-object` | apiPackageAddObject | ahgPreservationPlugin | | |
| ☐ | `/api/preservation/package/remove-object` | apiPackageRemoveObject | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/:informationObject` | index | ahgPreservationPlugin | | |
| ☐ | `/statistics/item/:object_id` | item | ahgStatisticsPlugin | | |
| ☐ | `/accessibility/alt-text/api/object/:id` | apiObject | ahgAccessibilityPlugin | | |
| ☐ | `/registry/admin/institutions` | adminInstitutions | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/institutions/verify` | adminInstitutionVerify | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/institutions/:id/users` | adminInstitutionUsers | ahgRegistryPlugin | | |
| ☐ | `/registry/admin/institutions/:id/edit` | institutionEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution` | myInstitutionDashboard | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/register` | institutionRegister | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/edit` | institutionEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/contacts` | myInstitutionContacts | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/contacts/add` | myInstitutionContactAdd | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/contacts/:id/edit` | myInstitutionContactEdit | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/contacts/:id/delete` | myInstitutionContactDelete | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/instances` | myInstitutionInstances | ahgRegistryPlugin | | |
| ☐ | `/registry/my/institution/instances/add` | myInstitutionInstanceAdd | ahgRegistryPlugin | | |
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
| ☐ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | | |
| ☐ | `/ahgSettings/import` | import | ahgSettingsPlugin | | |
| ☐ | `/portable-export/import` | import | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/start-import` | apiStartImport | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-progress` | apiImportProgress | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-validate` | apiImportValidate | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/api/import-list` | apiImportList | ahgPortableExportPlugin | | |
| ☐ | `/favorites/import` | import | ahgFavoritesPlugin | | |
| ☐ | `/acquisition/bulk-import` | bulkImport | ahgLibraryPlugin | | |
| ☐ | `/acquisition/bulk-import-sample` | bulkImportSample | ahgLibraryPlugin | | |
| ☐ | `/library/copy-cataloguing/import` | import | ahgLibraryPlugin | | |
| ☐ | `/researcher/import` | importExchange | ahgResearcherPlugin | | |
| ☐ | `/admin/customFields/import` | import | ahgCustomFieldsPlugin | | |
| ☐ | `/registry/admin/import` | adminImport | ahgRegistryPlugin | | |
| ☐ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | | |
| ☐ | `/research/bibliography/:id/import` | importBibliography | ahgResearchPlugin | | |
| ☐ | `/research/annotations/import/:object_id` | importAnnotationsIIIF | ahgResearchPlugin | | |


## Admin  ·  `admin`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/admin/rights` | index | ahgExtendedRightsPlugin | | |
| ☐ | `/admin/rights/batch` | batch | ahgExtendedRightsPlugin | | |
| ☐ | `/admin/condition` | admin | ahgConditionPlugin | | |
| ☐ | `/admin/authority/dashboard` | dashboard | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/workqueue` | workqueue | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/identifiers` | identifiers | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/merge/:id` | merge | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/split/:id` | split | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/occupations` | occupations | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/functions` | functions | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/functions/browse` | functionBrowse | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/:actorId/contact` | contact | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/config` | config | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/dedup` | index | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/dedup/scan` | scan | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/dedup/compare/:id` | compare | ahgAuthorityPlugin | | |
| ☐ | `/admin/authority/ner-pipeline` | index | ahgAuthorityPlugin | | |
| ☐ | `/admin/queue` | queueBrowse | ahgJobsManagePlugin | | |
| ☐ | `/admin/queue/detail/:id` | queueDetail | ahgJobsManagePlugin | | |
| ☐ | `/admin/queue/batches` | queueBatches | ahgJobsManagePlugin | | |
| ☐ | `/admin/queue/progress` | queueProgress | ahgJobsManagePlugin | | |
| ☐ | `/admin/queue/retry` | queueRetry | ahgJobsManagePlugin | | |
| ☐ | `/admin/queue/cancel` | queueCancel | ahgJobsManagePlugin | | |
| ☐ | `/admin/registrations/approve` | approve | ahgUserRegistrationPlugin | | |
| ☐ | `/admin/registrations/verify` | markVerified | ahgUserRegistrationPlugin | | |
| ☐ | `/admin/registrations/reject` | reject | ahgUserRegistrationPlugin | | |
| ☐ | `/admin/registrations` | pending | ahgUserRegistrationPlugin | | |
| ☐ | `/admin/forms` | index | ahgFormsPlugin | | |
| ☐ | `/admin/forms/templates` | templates | ahgFormsPlugin | | |
| ☐ | `/admin/forms/template/create` | templateCreate | ahgFormsPlugin | | |
| ☐ | `/admin/forms/template/:id/edit` | templateEdit | ahgFormsPlugin | | |
| ☐ | `/admin/forms/template/:id/delete` | templateDelete | ahgFormsPlugin | | |
| ☐ | `/admin/forms/template/:id/clone` | templateClone | ahgFormsPlugin | | |
| ☐ | `/admin/forms/template/:id/export` | templateExport | ahgFormsPlugin | | |
| ☐ | `/admin/forms/template/import` | templateImport | ahgFormsPlugin | | |
| ☐ | `/admin/forms/template/:id/builder` | builder | ahgFormsPlugin | | |
| ☐ | `/admin/forms/assignments` | assignments | ahgFormsPlugin | | |
| ☐ | `/admin/forms/assignment/create` | assignmentCreate | ahgFormsPlugin | | |
| ☐ | `/admin/forms/assignment/:id/delete` | assignmentDelete | ahgFormsPlugin | | |
| ☐ | `/admin/forms/mappings` | mappings | ahgFormsPlugin | | |


# MENU: Clipboard


## Clear all selections  ·  `clearClipboard`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | | |
| ☐ | `/portable-export/api/clipboard-export` | apiClipboardExport | ahgPortableExportPlugin | | |
| ☐ | `/favorites/clear` | clear | ahgFavoritesPlugin | | |
| ☐ | `/cart/clear` | clear | ahgCartPlugin | | |
| ☐ | `/mediaSettings/clearQueue` | clearQueue | ahgIiifPlugin | | |
| ☐ | `/security/clearances` | index | ahgSecurityClearancePlugin | | |
| ☐ | `/security/clearance/:id` | view | ahgSecurityClearancePlugin | | |
| ☐ | `/security/clearance/grant` | grant | ahgSecurityClearancePlugin | | |
| ☐ | `/security/clearance/:id/revoke` | revoke | ahgSecurityClearancePlugin | | |
| ☐ | `/security/clearance/bulk-grant` | bulkGrant | ahgSecurityClearancePlugin | | |
| ☐ | `/security/clearance/user/:slug` | user | ahgSecurityClearancePlugin | | |
| ☐ | `/research/orcid/credentials/clear` | orcidClearCredentials | ahgResearchPlugin | | |
| ☐ | `/research/ajax/clipboard-to-project` | clipboardToProject | ahgResearchPlugin | | |
| ☐ | `/research/ajax/manage-clipboard-item` | manageClipboardItem | ahgResearchPlugin | | |


## Go to clipboard  ·  `goToClipboard`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | | |
| ☐ | `/portable-export/api/clipboard-export` | apiClipboardExport | ahgPortableExportPlugin | | |
| ☐ | `/research/ajax/clipboard-to-project` | clipboardToProject | ahgResearchPlugin | | |
| ☐ | `/research/ajax/manage-clipboard-item` | manageClipboardItem | ahgResearchPlugin | | |


## Load clipboard  ·  `loadClipboard`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | | |
| ☐ | `/condition/check/:id/upload` | upload | ahgConditionPlugin | | |
| ☐ | `/api/accession/attachment/upload` | apiAttachmentUpload | ahgAccessionManagePlugin | | |
| ☐ | `/portable-export/api/clipboard-export` | apiClipboardExport | ahgPortableExportPlugin | | |
| ☐ | `/portable-export/download` | download | ahgPortableExportPlugin | | |
| ☐ | `/tenant/branding/logo-upload` | uploadLogo | ahgMultiTenantPlugin | | |
| ☐ | `/privacyAdmin/downloadRedactedFile` | downloadRedactedFile | ahgPrivacyPlugin | | |
| ☐ | `/ai-condition/api/training/upload` | apiTrainingUpload | ahgAiConditionPlugin | | |
| ☐ | `/ai-condition/api/client-upload-consent` | apiClientUploadConsent | ahgAiConditionPlugin | | |
| ☐ | `/researcher/api/upload` | apiUpload | ahgResearcherPlugin | | |
| ☐ | `/cart/download/:token` | download | ahgCartPlugin | | |
| ☐ | `/media/download/:id` | download | ahgIiifPlugin | | |
| ☐ | `/api/v2/upload` | fileUpload | ahgAPIPlugin | | |
| ☐ | `/api/v2/descriptions/:slug/upload` | descriptionUpload | ahgAPIPlugin | | |
| ☐ | `/ahg3DModel/upload` | upload | ahg3DModelPlugin | | |
| ☐ | `/ingest/:id/upload` | upload | ahgIngestPlugin | | |
| ☐ | `/admin/preservation/package/:id/download` | packageDownload | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/upload` | upload | ahgPreservationPlugin | | |
| ☐ | `/tiff-pdf-merge/download/:job_id` | download | ahgPreservationPlugin | | |
| ☐ | `/statistics/downloads` | downloads | ahgStatisticsPlugin | | |
| ☐ | `/registry/my/vendor/software/:id/upload` | myVendorSoftwareUpload | ahgRegistryPlugin | | |
| ☐ | `/ftp-upload` | index | ahgFtpPlugin | | |
| ☐ | `/ftp-upload/upload` | upload | ahgFtpPlugin | | |
| ☐ | `/ftp-upload/chunk` | uploadChunk | ahgFtpPlugin | | |
| ☐ | `/ftp-upload/list` | listFiles | ahgFtpPlugin | | |
| ☐ | `/ftp-upload/delete` | deleteFile | ahgFtpPlugin | | |
| ☐ | `/ftp-upload/import-as-upload` | importAsUpload | ahgFtpPlugin | | |
| ☐ | `/loan/:id/upload-document` | uploadDocument | ahgLoanPlugin | | |
| ☐ | `/digitalobject/upload` | doUpload | ahgInformationObjectManagePlugin | | |
| ☐ | `/api/report-builder/attachment/upload` | apiAttachmentUpload | ahgReportBuilderPlugin | | |
| ☐ | `/research/reproduction/download/:token` | reproductionDownload | ahgResearchPlugin | | |
| ☐ | `/research/studio/:projectId/artefact/:artefactId/download` | studioDownload | ahgResearchPlugin | | |
| ☐ | `/research/ajax/upload-note-image` | uploadNoteImage | ahgResearchPlugin | | |
| ☐ | `/research/ajax/clipboard-to-project` | clipboardToProject | ahgResearchPlugin | | |
| ☐ | `/research/ajax/manage-clipboard-item` | manageClipboardItem | ahgResearchPlugin | | |


## Save clipboard  ·  `saveClipboard`

| ✔ | Link / URL | Action | Plugin | Result | Notes |
|---|---|---|---|---|---|
| ☐ | `/user/clipboard` | clipboard | ahgUserManagePlugin | | |
| ☐ | `/condition/annotation/save` | saveAnnotation | ahgConditionPlugin | | |
| ☐ | `/api/authority/identifier/save` | apiIdentifierSave | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/occupation/save` | apiOccupationSave | ahgAuthorityPlugin | | |
| ☐ | `/api/authority/function/save` | apiFunctionSave | ahgAuthorityPlugin | | |
| ☐ | `/museum/provenance/save` | provenanceSave | ahgMuseumPlugin | | |
| ☐ | `/api/forms/autosave` | apiAutosave | ahgFormsPlugin | | |
| ☐ | `/glam/saveBrowseSettings` | saveBrowseSettings | ahgDisplayPlugin | | |
| ☐ | `/sharepoint/rules/save` | ruleSave | ahgSharePointPlugin | | |
| ☐ | `/sharepoint/mappings/save` | mappingsSave | ahgSharePointPlugin | | |
| ☐ | `/sharepoint/drives/save` | driveSave | ahgSharePointPlugin | | |
| ☐ | `/admin/accessions/:id/appraisal/save` | appraisalSave | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container/save` | apiContainerSave | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/container-item/save` | apiContainerItemSave | ahgAccessionManagePlugin | | |
| ☐ | `/api/accession/rights/save` | apiRightsSave | ahgAccessionManagePlugin | | |
| ☐ | `/ahgSettings/saveTiffPdfSettings` | saveTiffPdfSettings | ahgSettingsPlugin | | |
| ☐ | `/spectrum/annotation/save` | saveAnnotation | ahgSpectrumPlugin | | |
| ☐ | `/portable-export/api/clipboard-export` | apiClipboardExport | ahgPortableExportPlugin | | |
| ☐ | `/admin/doi/config/save` | configSave | ahgDoiPlugin | | |
| ☐ | `/tenant/branding/save` | save | ahgMultiTenantPlugin | | |
| ☐ | `/privacyAdmin/saveVisualRedaction` | saveVisualRedaction | ahgPrivacyPlugin | | |
| ☐ | `/ai-condition/api/client-save` | apiClientSave | ahgAiConditionPlugin | | |
| ☐ | `/ai-condition/api/manual-save` | apiManualSave | ahgAiConditionPlugin | | |
| ☐ | `/cart/save-selections` | saveSelections | ahgCartPlugin | | |
| ☐ | `/mediaSettings/save` | save | ahgIiifPlugin | | |
| ☐ | `/admin/customFields/save` | save | ahgCustomFieldsPlugin | | |
| ☐ | `/customFields/save` | saveValues | ahgCustomFieldsPlugin | | |
| ☐ | `/api/integrity/alert/save` | apiAlertSave | ahgIntegrityPlugin | | |
| ☐ | `/security/2fa/policy/save` | mfaPolicy | ahgSecurityClearancePlugin | | |
| ☐ | `/accessibility/alt-text/save` | save | ahgAccessibilityPlugin | | |
| ☐ | `/registry/notes/save` | noteSave | ahgRegistryPlugin | | |
| ☐ | `/ai/ner/bulk-save` | bulkSave | ahgAIPlugin | | |
| ☐ | `/admin/landing-pages/ajax/save-draft` | saveDraft | ahgLandingPagePlugin | | |
| ☐ | `/api/report-builder/query/save` | apiQuerySave | ahgReportBuilderPlugin | | |
| ☐ | `/api/report-builder/template/save` | apiTemplateSave | ahgReportBuilderPlugin | | |
| ☐ | `/api/report-builder/link/save` | apiLinkSave | ahgReportBuilderPlugin | | |
| ☐ | `/api/report-builder/section/save` | apiSectionSave | ahgReportBuilderPlugin | | |
| ☐ | `/api/report-builder/widget/save` | apiWidgetSave | ahgReportBuilderPlugin | | |
| ☐ | `/api/report-builder/save` | apiSave | ahgReportBuilderPlugin | | |
| ☐ | `/research/saved-searches` | savedSearches | ahgResearchPlugin | | |
