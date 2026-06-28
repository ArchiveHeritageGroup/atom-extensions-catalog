# ahgAccessionManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). First-class accession management with intake queue, appraisal workflow, container tracking, rights inheritance, and multi-tenant isolation

## Overview

- **Name:** AHG Accession Manage
- **Machine name:** `ahgAccessionManagePlugin`
- **Version:** 2.0.0
- **Category:** browse
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

### Features

- Accession browse via direct ES HTTP queries
- Intake queue with status workflow (draft/submitted/under_review/accepted/rejected/returned)
- Configurable intake checklists with templates
- Accession timeline (chain-of-custody audit trail)
- File attachments (deed of gift, photos, correspondence)
- Formal appraisal with weighted scoring criteria and templates
- Heritage asset valuation history (GRAP 103/IPSAS 45)
- Portfolio valuation reporting
- Physical container tracking with barcode support
- Container item management with IO linking
- PREMIS-aligned rights management with inheritance to child IOs
- Per-repository accession numbering sequences
- Multi-tenant isolation (tenant_id on all tables)
- CLI tasks: accession:intake, accession:report

## Database tables

- `accession_appraisal`
- `accession_appraisal_criterion`
- `accession_appraisal_template`
- `accession_attachment`
- `accession_config`
- `accession_container`
- `accession_container_item`
- `accession_intake_checklist`
- `accession_intake_template`
- `accession_numbering_sequence`
- `accession_rights`
- `accession_rights_inherited`
- `accession_timeline`
- `accession_v2`
- `accession_valuation_history`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `accession_view_override` | `/accession/:slug` | index |
| `accession_delete_override` | `/accession/:slug/delete` | delete |
| `accession_edit_override` | `/accession/:slug/edit` | edit |
| `accession_browse_override` | `/accession/browse` | browse |
| `accession_dashboard` | `/admin/accessions/dashboard` | dashboard |
| `accession_intake_submit` | `/admin/accessions/:id/submit` | submit |
| `accession_intake_review` | `/admin/accessions/:id/review` | review |
| `accession_intake_accept` | `/admin/accessions/:id/accept` | accept |
| `accession_intake_reject` | `/admin/accessions/:id/reject` | reject |
| `accession_intake_return` | `/admin/accessions/:id/return` | returnRevision |
| `accession_intake_timeline` | `/admin/accessions/:id/timeline` | timeline |
| `accession_intake_checklist` | `/admin/accessions/:id/checklist` | checklist |
| `accession_intake_attachments` | `/admin/accessions/:id/attachments` | attachments |
| `accession_intake_detail` | `/admin/accessions/:id/intake` | queueDetail |
| `accession_intake_queue` | `/admin/accessions/queue` | queue |
| `accession_intake_assign` | `/admin/accessions/queue/assign` | assign |
| `accession_intake_config` | `/admin/accessions/config` | config |
| `accession_intake_numbering` | `/admin/accessions/numbering` | numbering |
| `accession_api_checklist_toggle` | `/api/accession/checklist/:id/toggle` | apiChecklistToggle |
| `accession_api_checklist_apply` | `/api/accession/checklist/apply-template` | apiChecklistApplyTemplate |
| `accession_api_attachment_upload` | `/api/accession/attachment/upload` | apiAttachmentUpload |
| `accession_api_attachment_delete` | `/api/accession/attachment/:id/delete` | apiAttachmentDelete |
| `accession_appraisal_form` | `/admin/accessions/:id/appraisal` | appraisal |
| `accession_appraisal_save` | `/admin/accessions/:id/appraisal/save` | appraisalSave |
| `accession_valuation_view` | `/admin/accessions/:id/valuation` | valuation |
| `accession_valuation_add` | `/admin/accessions/:id/valuation/add` | valuationAdd |
| `accession_appraisal_templates` | `/admin/accessions/appraisal-templates` | appraisalTemplates |
| `accession_valuation_report` | `/admin/accessions/valuation-report` | valuationReport |
| `accession_api_appraisal_score` | `/api/accession/appraisal/:id/score` | apiAppraisalScore |
| `accession_containers_view` | `/admin/accessions/:id/containers` | containers |
| `accession_rights_view` | `/admin/accessions/:id/rights` | rights |
| `accession_api_container_save` | `/api/accession/container/save` | apiContainerSave |
| `accession_api_container_delete` | `/api/accession/container/:id/delete` | apiContainerDelete |
| `accession_api_container_item_save` | `/api/accession/container-item/save` | apiContainerItemSave |
| `accession_api_container_item_delete` | `/api/accession/container-item/:id/delete` | apiContainerItemDelete |
| `accession_api_container_item_link` | `/api/accession/container-item/:id/link` | apiContainerItemLink |
| `accession_api_barcode_lookup` | `/api/accession/barcode/lookup` | apiBarcodeLookup |
| `accession_api_rights_save` | `/api/accession/rights/save` | apiRightsSave |
| `accession_api_rights_delete` | `/api/accession/rights/:id/delete` | apiRightsDelete |
| `accession_api_rights_inherit` | `/api/accession/rights/:id/inherit` | apiRightsInherit |

## Module actions

**`accessionAppraisal`** — `appraisal`, `appraisalSave`, `apiAppraisalScore`, `valuation`, `valuationAdd`, `appraisalTemplates`, `valuationReport`
**`accessionIntake`** — `queue`, `queueDetail`, `submit`, `assign`, `review`, `accept`, `reject`, `returnRevision`, `timeline`, `checklist`, `apiChecklistToggle`, `apiChecklistApplyTemplate`, `attachments`, `apiAttachmentUpload`, `apiAttachmentDelete`, `config`, `numbering`
**`accessionContainer`** — `containers`, `apiContainerSave`, `apiContainerDelete`, `apiContainerItemSave`, `apiContainerItemDelete`, `apiContainerItemLink`, `apiBarcodeLookup`, `rights`, `apiRightsSave`, `apiRightsDelete`, `apiRightsInherit`
**`accessionManage`** — `browse`, `dashboard`

## CLI tasks

- `php symfony accession:intake` — Manage accession intake queue
- `php symfony accession:report` — Accession reports and exports

## Service layer

### `AccessionCrudService`  
`lib/Services/AccessionCrudService.php`

Public methods: `getById()`, `getBySlug()`, `create()`, `update()`, `delete()`, `getDonors()`, `getAccessionEvents()`, `saveAccessionEvent()`, `deleteAccessionEvent()`, `getDeaccessions()`, `saveDeaccession()`, `deleteDeaccession()`, `getFormChoices()`, `getExtended()`, `getDashboardStats()`

### `AccessionContainerService`  
`lib/Services/AccessionContainerService.php`

Public methods: `scopeQuery()`, `createContainer()`, `updateContainer()`, `deleteContainer()`, `getContainers()`, `addContainerItem()`, `updateContainerItem()`, `deleteContainerItem()`, `linkItemToIO()`, `getContainerItems()`, `lookupBarcode()`, `createRight()`, `updateRight()`, `deleteRight()`, `getRights()`, `inheritRightsToChildren()`, `getInheritedRights()`, `generateNextNumber()`

### `AccessionAppraisalService`  
`lib/Services/AccessionAppraisalService.php`

Public methods: `scopeQuery()`, `createAppraisal()`, `updateAppraisal()`, `getAppraisal()`, `getAppraisalsForAccession()`, `addCriterion()`, `updateCriterion()`, `deleteCriterion()`, `calculateWeightedScore()`, `applyTemplate()`, `listTemplates()`, `recordValuation()`, `getValuationHistory()`, `getCurrentValuation()`, `getValuationReport()`, `deleteAllForAccession()`

### `AccessionIntakeService`  
`lib/Services/AccessionIntakeService.php`

Public methods: `scopeQuery()`, `getQueue()`, `getQueueStats()`, `getV2Record()`, `ensureV2Record()`, `submit()`, `assign()`, `review()`, `accept()`, `reject()`, `returnForRevision()`, `getChecklist()`, `applyChecklistTemplate()`, `toggleChecklistItem()`, `getChecklistProgress()`, `getChecklistTemplates()`, `addTimelineEvent()`, `getTimeline()`

### `AccessionFinalisationService`  
`lib/Services/AccessionFinalisationService.php`

Public methods: `containerBarcodesEnabled()`, `rightsInheritanceEnabled()`, `finalisationBlockers()`, `canFinalise()`, `upsertWorkflow()`, `inheritRightsToIo()`, `nextAccessionNumber()`

### `AccessionBrowseService`  
`lib/Services/AccessionBrowseService.php`

Public methods: `browse()`, `extractI18nField()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
