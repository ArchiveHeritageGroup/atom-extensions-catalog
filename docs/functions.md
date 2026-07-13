# AtoM Heratio (PSIS) - Function Reference & Link Test

**Instance:** PSIS / archive - tested authenticated as johan (admin)
**Tested:** 13 July 2026 15:07 SAST

Every navigable (GET) route below was requested with a logged-in admin session and its HTTP status recorded. Write/destructive actions (delete, save, update, approve, upload, export, etc.) are listed but NOT auto-triggered - they need a manual click-test. `:slug`/`:id` routes were tested against a real sample record.

**Results:** ✅ 55 passed (200) · ❌ 0 failed · — 368 not auto-tested (write action / needs param)

---

## Table of Contents

1. [3D Model (ahg3DModelPlugin)](#3d-model-ahg3dmodelplugin)
2. [AI (ahgAIPlugin)](#ai-ahgaiplugin)
3. [API (ahgAPIPlugin)](#api-ahgapiplugin)
4. [Access Request (ahgAccessRequestPlugin)](#access-request-ahgaccessrequestplugin)
5. [Accessibility (ahgAccessibilityPlugin)](#accessibility-ahgaccessibilityplugin)
6. [Accession Manage (ahgAccessionManagePlugin)](#accession-manage-ahgaccessionmanageplugin)
7. [Actor Manage (ahgActorManagePlugin)](#actor-manage-ahgactormanageplugin)
8. [AI Compliance (ahgAiCompliancePlugin)](#ai-compliance-ahgaicomplianceplugin)
9. [AI Condition (ahgAiConditionPlugin)](#ai-condition-ahgaiconditionplugin)
10. [Annotations (ahgAnnotationsPlugin)](#annotations-ahgannotationsplugin)
11. [Audit Trail (ahgAuditTrailPlugin)](#audit-trail-ahgaudittrailplugin)
12. [Authority (ahgAuthorityPlugin)](#authority-ahgauthorityplugin)
13. [Authority Resolution (ahgAuthorityResolutionPlugin)](#authority-resolution-ahgauthorityresolutionplugin)
14. [Backup (ahgBackupPlugin)](#backup-ahgbackupplugin)
15. [C2PA (ahgC2paPlugin)](#c2pa-ahgc2paplugin)
16. [CDPA (ahgCDPAPlugin)](#cdpa-ahgcdpaplugin)
17. [Cart (ahgCartPlugin)](#cart-ahgcartplugin)
18. [Condition (ahgConditionPlugin)](#condition-ahgconditionplugin)
19. [Contact (ahgContactPlugin)](#contact-ahgcontactplugin)
20. [Core (ahgCorePlugin)](#core-ahgcoreplugin)
21. [Custom Fields (ahgCustomFieldsPlugin)](#custom-fields-ahgcustomfieldsplugin)
22. [DAM (ahgDAMPlugin)](#dam-ahgdamplugin)
23. [DACS Manage (ahgDacsManagePlugin)](#dacs-manage-ahgdacsmanageplugin)
24. [Data Migration (ahgDataMigrationPlugin)](#data-migration-ahgdatamigrationplugin)
25. [DC Manage (ahgDcManagePlugin)](#dc-manage-ahgdcmanageplugin)
26. [Dedupe (ahgDedupePlugin)](#dedupe-ahgdedupeplugin)
27. [Discovery (ahgDiscoveryPlugin)](#discovery-ahgdiscoveryplugin)
28. [Display (ahgDisplayPlugin)](#display-ahgdisplayplugin)
29. [DOI (ahgDoiPlugin)](#doi-ahgdoiplugin)
30. [Donor Agreement (ahgDonorAgreementPlugin)](#donor-agreement-ahgdonoragreementplugin)
31. [Donor Manage (ahgDonorManagePlugin)](#donor-manage-ahgdonormanageplugin)
32. [Email Delivery (ahgEmailDeliveryPlugin)](#email-delivery-ahgemaildeliveryplugin)
33. [Exhibition (ahgExhibitionPlugin)](#exhibition-ahgexhibitionplugin)
34. [Export (ahgExportPlugin)](#export-ahgexportplugin)
35. [Extended Rights (ahgExtendedRightsPlugin)](#extended-rights-ahgextendedrightsplugin)
36. [Favorites (ahgFavoritesPlugin)](#favorites-ahgfavoritesplugin)
37. [Federation (ahgFederationPlugin)](#federation-ahgfederationplugin)
38. [Feedback (ahgFeedbackPlugin)](#feedback-ahgfeedbackplugin)
39. [Forms (ahgFormsPlugin)](#forms-ahgformsplugin)
40. [FTP (ahgFtpPlugin)](#ftp-ahgftpplugin)
41. [Function Manage (ahgFunctionManagePlugin)](#function-manage-ahgfunctionmanageplugin)
42. [Functions Docs (ahgFunctionsDocsPlugin)](#functions-docs-ahgfunctionsdocsplugin)
43. [GIS (ahgGISPlugin)](#gis-ahggisplugin)
44. [Gallery (ahgGalleryPlugin)](#gallery-ahggalleryplugin)
45. [GraphQL (ahgGraphQLPlugin)](#graphql-ahggraphqlplugin)
46. [Help (ahgHelpPlugin)](#help-ahghelpplugin)
47. [Heritage Accounting (ahgHeritageAccountingPlugin)](#heritage-accounting-ahgheritageaccountingplugin)
48. [Heritage (ahgHeritagePlugin)](#heritage-ahgheritageplugin)
49. [ICIP (ahgICIPPlugin)](#icip-ahgicipplugin)
50. [IPSAS (ahgIPSASPlugin)](#ipsas-ahgipsasplugin)
51. [IIIF (ahgIiifPlugin)](#iiif-ahgiiifplugin)
52. [Image Ar (ahgImageArPlugin)](#image-ar-ahgimagearplugin)
53. [Information Object Manage (ahgInformationObjectManagePlugin)](#information-object-manage-ahginformationobjectmanageplugin)
54. [Ingest (ahgIngestPlugin)](#ingest-ahgingestplugin)
55. [Integrity (ahgIntegrityPlugin)](#integrity-ahgintegrityplugin)
56. [Jobs Manage (ahgJobsManagePlugin)](#jobs-manage-ahgjobsmanageplugin)
57. [Label (ahgLabelPlugin)](#label-ahglabelplugin)
58. [Landing Page (ahgLandingPagePlugin)](#landing-page-ahglandingpageplugin)
59. [Library (ahgLibraryPlugin)](#library-ahglibraryplugin)
60. [Loan (ahgLoanPlugin)](#loan-ahgloanplugin)
61. [Marketplace (ahgMarketplacePlugin)](#marketplace-ahgmarketplaceplugin)
62. [Menu Manage (ahgMenuManagePlugin)](#menu-manage-ahgmenumanageplugin)
63. [Metadata Export (ahgMetadataExportPlugin)](#metadata-export-ahgmetadataexportplugin)
64. [Metadata Extraction (ahgMetadataExtractionPlugin)](#metadata-extraction-ahgmetadataextractionplugin)
65. [MODS Manage (ahgModsManagePlugin)](#mods-manage-ahgmodsmanageplugin)
66. [Multi Tenant (ahgMultiTenantPlugin)](#multi-tenant-ahgmultitenantplugin)
67. [Museum (ahgMuseumPlugin)](#museum-ahgmuseumplugin)
68. [NARSSA (ahgNARSSAPlugin)](#narssa-ahgnarssaplugin)
69. [NAZ (ahgNAZPlugin)](#naz-ahgnazplugin)
70. [NMMZ (ahgNMMZPlugin)](#nmmz-ahgnmmzplugin)
71. [Observability (ahgObservabilityPlugin)](#observability-ahgobservabilityplugin)
72. [Ocfl (ahgOcflPlugin)](#ocfl-ahgocflplugin)
73. [Portable Export (ahgPortableExportPlugin)](#portable-export-ahgportableexportplugin)
74. [Preservation (ahgPreservationPlugin)](#preservation-ahgpreservationplugin)
75. [Privacy (ahgPrivacyPlugin)](#privacy-ahgprivacyplugin)
76. [Provenance (ahgProvenancePlugin)](#provenance-ahgprovenanceplugin)
77. [RAD Manage (ahgRadManagePlugin)](#rad-manage-ahgradmanageplugin)
78. [Rdm (ahgRdmPlugin)](#rdm-ahgrdmplugin)
79. [Records Manage (ahgRecordsManagePlugin)](#records-manage-ahgrecordsmanageplugin)
80. [Registry (ahgRegistryPlugin)](#registry-ahgregistryplugin)
81. [Report Builder (ahgReportBuilderPlugin)](#report-builder-ahgreportbuilderplugin)
82. [Reports (ahgReportsPlugin)](#reports-ahgreportsplugin)
83. [Repository Manage (ahgRepositoryManagePlugin)](#repository-manage-ahgrepositorymanageplugin)
84. [Request To Publish (ahgRequestToPublishPlugin)](#request-to-publish-ahgrequesttopublishplugin)
85. [Research (ahgResearchPlugin)](#research-ahgresearchplugin)
86. [Researcher (ahgResearcherPlugin)](#researcher-ahgresearcherplugin)
87. [Resource Sync (ahgResourceSyncPlugin)](#resource-sync-ahgresourcesyncplugin)
88. [RiC Explorer (ahgRicExplorerPlugin)](#ric-explorer-ahgricexplorerplugin)
89. [Rights Holder Manage (ahgRightsHolderManagePlugin)](#rights-holder-manage-ahgrightsholdermanageplugin)
90. [Rights (ahgRightsPlugin)](#rights-ahgrightsplugin)
91. [Scan (ahgScanPlugin)](#scan-ahgscanplugin)
92. [Search (ahgSearchPlugin)](#search-ahgsearchplugin)
93. [Security Clearance (ahgSecurityClearancePlugin)](#security-clearance-ahgsecurityclearanceplugin)
94. [Semantic Search (ahgSemanticSearchPlugin)](#semantic-search-ahgsemanticsearchplugin)
95. [Settings (ahgSettingsPlugin)](#settings-ahgsettingsplugin)
96. [Share Point (ahgSharePointPlugin)](#share-point-ahgsharepointplugin)
97. [Spectrum (ahgSpectrumPlugin)](#spectrum-ahgspectrumplugin)
98. [Static Page (ahgStaticPagePlugin)](#static-page-ahgstaticpageplugin)
99. [Statistics (ahgStatisticsPlugin)](#statistics-ahgstatisticsplugin)
100. [Storage Manage (ahgStorageManagePlugin)](#storage-manage-ahgstoragemanageplugin)
101. [Term Taxonomy (ahgTermTaxonomyPlugin)](#term-taxonomy-ahgtermtaxonomyplugin)
102. [Theme B5 (ahgThemeB5Plugin)](#theme-b5-ahgthemeb5plugin)
103. [TIFF/PDF Merge (ahgTiffPdfMergePlugin)](#tiff-pdf-merge-ahgtiffpdfmergeplugin)
104. [Time Limited Share Link (ahgTimeLimitedShareLinkPlugin)](#time-limited-share-link-ahgtimelimitedsharelinkplugin)
105. [Translation (ahgTranslationPlugin)](#translation-ahgtranslationplugin)
106. [UI Overrides (ahgUiOverridesPlugin)](#ui-overrides-ahguioverridesplugin)
107. [User Manage (ahgUserManagePlugin)](#user-manage-ahgusermanageplugin)
108. [User Registration (ahgUserRegistrationPlugin)](#user-registration-ahguserregistrationplugin)
109. [Vendor (ahgVendorPlugin)](#vendor-ahgvendorplugin)
110. [Version Control (ahgVersionControlPlugin)](#version-control-ahgversioncontrolplugin)
111. [Workflow (ahgWorkflowPlugin)](#workflow-ahgworkflowplugin)

---

## 3D Model (ahg3DModelPlugin)
*Category: ahg - enabled*

3D model viewing with Google Model Viewer, AR support, hotspots, and IIIF 3D manifests

## AI (ahgAIPlugin)
*Category: ahg - enabled*

AI-powered tools: NER, Translation, Summarization, Spellcheck

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Assistant Ask | GET/POST | `/ai/assistant/ask` | — | write/action - manual test |
| Assistant | GET/POST | `/ai/assistant` | — | write/action - manual test |
| Batch Action | GET/POST | `/ai/batch/:id/action` | — | write/action - manual test |
| Batch Process | GET/POST | `/ai/batch/:id/process` | — | write/action - manual test |
| Batch Progress | GET/POST | `/ai/batch/:id/progress` | — | write/action - manual test |
| Batch View | GET/POST | `/ai/batch/:id` | — | write/action - manual test |
| Batch Create | GET/POST | `/ai/batch/create` | — | write/action - manual test |
| Batch | GET/POST | `/ai/batch` | — | write/action - manual test |
| Catalog Apply | GET/POST | `/ai/catalog/:id/apply` | — | write/action - manual test |
| Catalog | GET/POST | `/ai/catalog/:id` | — | write/action - manual test |
| Donut Finalize | GET/POST | `/ai/donut/finalize` | — | write/action - manual test |
| Donut Positions | GET/POST | `/ai/donut/positions` | — | write/action - manual test |
| Donut Prefill | GET/POST | `/ai/donut/prefill` | — | write/action - manual test |
| Donut Result | GET/POST | `/ai/donut/results/:id` | — | write/action - manual test |
| Donut Dashboard | GET/POST | `/ai/donut` | — | write/action - manual test |
| Governance Inferences | GET/POST | `/ai/governance/inferences` | — | write/action - manual test |
| Governance Models | GET/POST | `/ai/governance/models` | — | write/action - manual test |
| Governance | GET/POST | `/ai/governance` | — | write/action - manual test |
| Htr | GET/POST | `/ai/htr/:id` | — | write/action - manual test |
| Job View | GET/POST | `/ai/job/:id` | — | write/action - manual test |
| Llm Configs | GET/POST | `/ai/llm/configs` | — | write/action - manual test |
| Llm Health | GET/POST | `/ai/llm/health` | — | write/action - manual test |
| Get Approved Entities | GET/POST | `/ai/ner/approved-entities/:id` | — | write/action - manual test |
| Bulk Save | GET/POST | `/ai/ner/bulk-save` | — | write/action - manual test |
| Create Actor | GET/POST | `/ai/ner/create/actor` | — | write/action - manual test |
| Create Place | GET/POST | `/ai/ner/create/place` | — | write/action - manual test |
| Create Subject | GET/POST | `/ai/ner/create/subject` | — | write/action - manual test |
| Get Entities | GET/POST | `/ai/ner/entities/:id` | — | write/action - manual test |
| Update Entity | GET/POST | `/ai/ner/entity/update` | — | write/action - manual test |
| Extract | GET/POST | `/ai/ner/extract/:id` | — | write/action - manual test |
| Health | GET/POST | `/ai/ner/health` | — | write/action - manual test |
| Pdf Overlay | GET/POST | `/ai/ner/pdf-overlay/:id` | — | write/action - manual test |
| Review | GET/POST | `/ai/ner/review` | — | write/action - manual test |
| Research Ask | GET/POST | `/ai/research/ask` | — | write/action - manual test |
| Research Session | GET/POST | `/ai/research/session/:id` | — | write/action - manual test |
| Research Sessions | GET/POST | `/ai/research/sessions` | — | write/action - manual test |
| Research | GET/POST | `/ai/research` | — | write/action - manual test |
| Suggest Decision | GET/POST | `/ai/suggest/:id/decision` | — | write/action - manual test |
| Suggest Preview | GET/POST | `/ai/suggest/:id/preview` | — | write/action - manual test |
| Suggest View | GET/POST | `/ai/suggest/:id/view` | — | write/action - manual test |
| Suggest | GET/POST | `/ai/suggest/:id` | — | write/action - manual test |
| Suggest Object | GET/POST | `/ai/suggest/object/:id` | — | write/action - manual test |
| Suggest Review | GET/POST | `/ai/suggest/review` | — | write/action - manual test |
| Summarize | GET/POST | `/ai/summarize/:id` | — | write/action - manual test |
| Templates | GET/POST | `/ai/templates` | — | write/action - manual test |
| Bulk Save | GET/POST | `/ner/bulk-save` | — | write/action - manual test |
| Get Entities | GET/POST | `/ner/entities/:id` | — | write/action - manual test |
| Extract | GET/POST | `/ner/extract/:id` | — | write/action - manual test |
| Htr | GET/POST | `/ner/htr/:id` | — | write/action - manual test |
| Review | GET/POST | `/ner/review` | — | write/action - manual test |
| Summarize | GET/POST | `/ner/summarize/:id` | — | write/action - manual test |

## API (ahgAPIPlugin)
*Category: ahg - enabled*

## Access Request (ahgAccessRequestPlugin)
*Category: ahg - enabled, locked*

Researcher access request management for restricted materials

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Pending | GET/POST | `/accessRequest` | — | write/action - manual test |
| Pending | GET/POST | `/security/access-requests` | — | write/action - manual test |
| Remove Approver | GET/POST | `/security/approvers/:id/remove` | — | write/action - manual test |
| Add Approver | GET/POST | `/security/approvers/add` | — | write/action - manual test |
| Approvers | GET/POST | `/security/approvers` | — | write/action - manual test |
| My Requests | GET/POST | `/security/my-requests` | — | write/action - manual test |
| Create | GET/POST | `/security/request-access/create` | — | write/action - manual test |
| New | GET/POST | `/security/request-access` | — | write/action - manual test |
| Create Object Request | GET/POST | `/security/request-object/create` | — | write/action - manual test |
| Request Object | GET/POST | `/security/request-object` | — | write/action - manual test |
| Approve | GET/POST | `/security/request/:id/approve` | — | write/action - manual test |
| Cancel | GET/POST | `/security/request/:id/cancel` | — | write/action - manual test |
| Deny | GET/POST | `/security/request/:id/deny` | — | write/action - manual test |
| View | GET | `/security/request/:id/review` | — | needs param sample |
| View | GET | `/security/request/:id` | — | needs param sample |
| Pending | GET/POST | `/security/requests` | — | write/action - manual test |
| Pending | GET/POST | `/security/request` | — | write/action - manual test |

## Accessibility (ahgAccessibilityPlugin)
*Category: reporting - enabled*

WCAG accessibility tooling (image alternative text)

## Accession Manage (ahgAccessionManagePlugin)
*Category: browse - enabled, locked*

High-performance accession browse and management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Delete | GET/POST | `/accession/:slug/delete` | — | write/action - manual test |
| Create / edit | GET | `/accession/2026-02-15-3/edit` | ✅ 200 | |
| View | GET | `/accession/2026-02-15-3` | ✅ 200 | |
| Create / edit | GET | `/accession/add` | ✅ 200 | |
| Browse | GET | `/accession/browse` | ✅ 200 | |

## Actor Manage (ahgActorManagePlugin)
*Category: browse - enabled, locked*

High-performance actor browse, autocomplete, and management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Delete | GET/POST | `/actor/:slug/delete` | — | write/action - manual test |
| Create / edit | GET | `/actor/:slug/edit` | — | needs param sample |
| View | GET | `/actor/:slug` | — | needs param sample |
| Create / edit | GET | `/actor/add` | ✅ 200 | |
| Autocomplete | GET | `/actor/autocomplete` | ✅ 200 | |
| Browse | GET | `/actor/browse` | ✅ 200 | |

## AI Compliance (ahgAiCompliancePlugin)
*Category: general - enabled*

## AI Condition (ahgAiConditionPlugin)
*Category: ai - enabled*

AI-powered condition assessment for archival materials using YOLOv8 and EfficientNet

## Annotations (ahgAnnotationsPlugin)
*Category: advanced_features - enabled*

W3C Web Annotation Data Model + Protocol backend

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Single | GET/POST | `/annotations/:uuid` | — | write/action - manual test |
| Container | GET/POST | `/annotations` | — | write/action - manual test |

## Audit Trail (ahgAuditTrailPlugin)
*Category: ahg - enabled*

Comprehensive audit trail logging for AtoM with POPIA/NARSSA compliance

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Authentication | GET/POST | `/admin/audit/authentication` | — | write/action - manual test |
| Compare Data | GET/POST | `/admin/audit/compare/:id` | — | write/action - manual test |
| Entity History | GET/POST | `/admin/audit/entity/:entity_type/:entity_id` | — | write/action - manual test |
| Export | GET/POST | `/admin/audit/export` | — | write/action - manual test |
| Integrity | GET/POST | `/admin/audit/integrity` | — | write/action - manual test |
| Configure | GET | `/admin/audit/settings` | ✅ 200 | |
| Statistics | GET | `/admin/audit/statistics` | ✅ 200 | |
| User Activity | GET/POST | `/admin/audit/user/:user_id` | — | write/action - manual test |
| View | GET | `/admin/audit/view/:id` | — | needs param sample |
| Browse | GET | `/admin/audit` | ✅ 200 | |

## Authority (ahgAuthorityPlugin)
*Category: authority - enabled*

## Authority Resolution (ahgAuthorityResolutionPlugin)
*Category: authority - enabled*

## Backup (ahgBackupPlugin)
*Category: ahg - enabled*

Database and file backup with scheduling, restore, upload and retention management

## C2PA (ahgC2paPlugin)
*Category: ahg - enabled*

## CDPA (ahgCDPAPlugin)
*Category: ahg - enabled*

Zimbabwe Cyber and Data Protection Act [Chapter 12:07] compliance - POTRAZ regulated

## Cart (ahgCartPlugin)
*Category: ahg - enabled*

Shopping cart for reproduction requests

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Download | GET/POST | `/cart/download/:token` | — | write/action - manual test |
| Order Confirmation | GET/POST | `/cart/order/:order` | — | write/action - manual test |
| Payment Notify | GET/POST | `/cart/payment/notify` | — | write/action - manual test |

## Condition (ahgConditionPlugin)
*Category: ahg - enabled*

Condition assessment and reporting for physical objects with Spectrum 5.0 compliance

## Contact (ahgContactPlugin)
*Category: ahg - enabled*

Extended contact information for actors

## Core (ahgCorePlugin)
*Category: core - enabled, core, locked*

Core utilities and shared services for AHG plugins

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Pdf Text | GET/POST | `/tts/pdfText` | — | write/action - manual test |
| Configure | GET | `/tts/settings` | ✅ 200 | |

## Custom Fields (ahgCustomFieldsPlugin)
*Category: metadata - enabled*

Admin-configurable custom metadata fields for any entity type

## DAM (ahgDAMPlugin)
*Category: ahg - enabled*

Digital Asset Management with IPTC metadata, watermarks, derivatives, and Creative Commons licensing

## DACS Manage (ahgDacsManagePlugin)
*Category: descriptive-standard - enabled*

DACS information object CRUD management

## Data Migration (ahgDataMigrationPlugin)
*Category: ahg - enabled*

Data migration tool for moving records between GLAM sectors

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Download | GET/POST | `/admin/data-migration/download` | — | write/action - manual test |
| Export | GET/POST | `/admin/data-migration/export` | — | write/action - manual test |
| Import | GET/POST | `/admin/data-migration/import` | — | write/action - manual test |
| Get Mapping | GET/POST | `/admin/data-migration/mapping` | — | write/action - manual test |
| Preservica Export | GET/POST | `/admin/data-migration/preservica/export/:id` | — | write/action - manual test |
| Preservica Export | GET/POST | `/admin/data-migration/preservica/export` | — | write/action - manual test |
| Preservica Import | GET/POST | `/admin/data-migration/preservica/import` | — | write/action - manual test |
| Preview | GET | `/admin/data-migration/preview` | ✅ 200 | |
| View | GET | `/admin/data-migration` | ✅ 200 | |
| Ahg Import Results | GET/POST | `/dataMigration/ahgImportResults` | — | write/action - manual test |
| Batch Export | GET/POST | `/dataMigration/batchExport` | — | write/action - manual test |
| Execute Ahg Import | GET/POST | `/dataMigration/executeAhgImport` | — | write/action - manual test |
| Execute | GET/POST | `/dataMigration/execute` | — | write/action - manual test |
| Sector Export | GET/POST | `/dataMigration/export/:sector` | — | write/action - manual test |
| Export Csv | GET/POST | `/dataMigration/exportCsv` | — | write/action - manual test |
| Export Mapping | GET/POST | `/dataMigration/exportMapping/:id` | — | write/action - manual test |
| Import Mapping | GET/POST | `/dataMigration/importMapping` | — | write/action - manual test |
| Job Status | GET/POST | `/dataMigration/job/:id` | — | write/action - manual test |
| Cancel Job | GET/POST | `/dataMigration/job/cancel` | — | write/action - manual test |
| Job Progress | GET/POST | `/dataMigration/job/progress` | — | write/action - manual test |
| Jobs | GET/POST | `/dataMigration/jobs` | — | write/action - manual test |
| Load Mapping | GET/POST | `/dataMigration/loadMapping` | — | write/action - manual test |
| Map | GET | `/dataMigration/map` | ✅ 200 | |
| Preview Validation | GET/POST | `/dataMigration/previewValidation` | — | write/action - manual test |
| Preview | GET | `/dataMigration/preview` | ✅ 200 | |
| Queue Job | GET/POST | `/dataMigration/queue` | — | write/action - manual test |
| Save Mapping | GET/POST | `/dataMigration/saveMapping` | — | write/action - manual test |
| Upload | GET/POST | `/dataMigration/upload` | — | write/action - manual test |
| Validate | GET/POST | `/dataMigration/validate` | — | write/action - manual test |
| View | GET | `/dataMigration` | ✅ 200 | |

## DC Manage (ahgDcManagePlugin)
*Category: descriptive-standard - enabled*

Dublin Core information object CRUD management

## Dedupe (ahgDedupePlugin)
*Category: ahg - enabled*

Duplicate detection for archival records

## Discovery (ahgDiscoveryPlugin)
*Category: search - enabled*

## Display (ahgDisplayPlugin)
*Category: ahg - enabled, locked*

GLAM browser and display modes for archival content

## DOI (ahgDoiPlugin)
*Category: ahg - enabled*

DOI integration via DataCite

## Donor Agreement (ahgDonorAgreementPlugin)
*Category: ahg - enabled*

Comprehensive donor/institution agreement management with contract uploads, rights, restrictions, reminders, and South African compliance.

## Donor Manage (ahgDonorManagePlugin)
*Category: browse - enabled, locked*

Donor browse and management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Delete | GET/POST | `/donor/:slug/delete` | — | write/action - manual test |
| Create / edit | GET | `/donor/rock-art-research-institute/edit` | ✅ 200 | |
| View | GET | `/donor/rock-art-research-institute` | ✅ 200 | |
| Create / edit | GET | `/donor/add` | ✅ 200 | |
| Browse | GET | `/donor/browse` | ✅ 200 | |

## Email Delivery (ahgEmailDeliveryPlugin)
*Category: communication - enabled*

Email bounce capture + suppression list + send-time gate

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Add | GET | `/admin/email/suppressions/add` | ✅ 200 | |
| Remove | GET/POST | `/admin/email/suppressions/remove` | — | write/action - manual test |
| Suppressions | GET/POST | `/admin/email/suppressions` | — | write/action - manual test |
| Bounce | GET/POST | `/email/bounce` | — | write/action - manual test |

## Exhibition (ahgExhibitionPlugin)
*Category: ahg - enabled*

Exhibition management for GLAM/DAM sectors

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Analytics | GET/POST | `/exhibition-space/:slug/analytics` | — | write/action - manual test |
| Builder Display Case | GET/POST | `/exhibition-space/:slug/builder/display-case` | — | write/action - manual test |
| Save Layout | GET/POST | `/exhibition-space/:slug/builder/layout` | — | write/action - manual test |
| Builder On Floor | GET/POST | `/exhibition-space/:slug/builder/on-floor` | — | write/action - manual test |
| Builder Placements | GET/POST | `/exhibition-space/:slug/builder/placements` | — | write/action - manual test |
| Builder Place | GET/POST | `/exhibition-space/:slug/builder/place` | — | write/action - manual test |
| Builder Remove | GET/POST | `/exhibition-space/:slug/builder/remove` | — | write/action - manual test |
| Builder Size | GET/POST | `/exhibition-space/:slug/builder/size` | — | write/action - manual test |
| Builder Spotlight | GET/POST | `/exhibition-space/:slug/builder/spotlight` | — | write/action - manual test |
| Builder Tilt | GET/POST | `/exhibition-space/:slug/builder/tilt` | — | write/action - manual test |
| Builder View | GET/POST | `/exhibition-space/:slug/builder/view` | — | write/action - manual test |
| Builder Wall | GET/POST | `/exhibition-space/:slug/builder/wall` | — | write/action - manual test |
| Builder ZOrder | GET/POST | `/exhibition-space/:slug/builder/z-order` | — | write/action - manual test |
| Builder | GET/POST | `/exhibition-space/:slug/builder` | — | write/action - manual test |
| Confirm Delete | GET/POST | `/exhibition-space/:slug/delete` | — | write/action - manual test |
| Destroy | GET/POST | `/exhibition-space/:slug/destroy` | — | write/action - manual test |
| Create / edit | GET | `/exhibition-space/:slug/edit` | — | needs param sample |
| Forecast | GET/POST | `/exhibition-space/:slug/forecast` | — | write/action - manual test |
| Place | GET/POST | `/exhibition-space/:slug/place` | — | write/action - manual test |
| Plan Add Room | GET/POST | `/exhibition-space/:slug/plan/add-room` | — | write/action - manual test |
| Plan Corridor Add | GET/POST | `/exhibition-space/:slug/plan/corridor-add` | — | write/action - manual test |
| Plan Corridor Move | GET/POST | `/exhibition-space/:slug/plan/corridor-move` | — | write/action - manual test |
| Plan Corridor Remove | GET/POST | `/exhibition-space/:slug/plan/corridor-remove` | — | write/action - manual test |
| Plan Delete Room | GET/POST | `/exhibition-space/:slug/plan/delete-room` | — | write/action - manual test |
| Plan Doors | GET/POST | `/exhibition-space/:slug/plan/doors` | — | write/action - manual test |
| Plan Group | GET/POST | `/exhibition-space/:slug/plan/group` | — | write/action - manual test |
| Plan Image Clear | GET/POST | `/exhibition-space/:slug/plan/image-clear` | — | write/action - manual test |
| Plan Image Rect | GET/POST | `/exhibition-space/:slug/plan/image-rect` | — | write/action - manual test |
| Plan Image | GET/POST | `/exhibition-space/:slug/plan/image` | — | write/action - manual test |
| Plan Room Floor | GET/POST | `/exhibition-space/:slug/plan/room-floor` | — | write/action - manual test |
| Plan Room Lock | GET/POST | `/exhibition-space/:slug/plan/room-lock` | — | write/action - manual test |
| Plan Save | GET/POST | `/exhibition-space/:slug/plan/save` | — | write/action - manual test |
| Plan Shape | GET/POST | `/exhibition-space/:slug/plan/shape` | — | write/action - manual test |
| Plan Stairs | GET/POST | `/exhibition-space/:slug/plan/stairs` | — | write/action - manual test |
| Plan Walls | GET/POST | `/exhibition-space/:slug/plan/walls` | — | write/action - manual test |
| Plan Windows | GET/POST | `/exhibition-space/:slug/plan/windows` | — | write/action - manual test |
| Plan | GET/POST | `/exhibition-space/:slug/plan` | — | write/action - manual test |
| Simulate Readings | GET/POST | `/exhibition-space/:slug/readings/simulate` | — | write/action - manual test |
| Record Readings | GET/POST | `/exhibition-space/:slug/readings` | — | write/action - manual test |
| Room Dims | GET/POST | `/exhibition-space/:slug/room-dims` | — | write/action - manual test |
| Save Room | GET/POST | `/exhibition-space/:slug/save-room` | — | write/action - manual test |
| Sensor Regen | GET/POST | `/exhibition-space/:slug/sensor/regenerate` | — | write/action - manual test |
| Walkthrough | GET/POST | `/exhibition-space/:slug/walkthrough` | — | write/action - manual test |
| View | GET | `/exhibition-space/:slug` | — | needs param sample |
| Create | GET/POST | `/exhibition-space/add` | — | write/action - manual test |
| Browse | GET | `/exhibition-space/browse` | ✅ 200 | |
| Generate Build | GET/POST | `/exhibition-space/generate/build` | — | write/action - manual test |
| Generate Suggest | GET/POST | `/exhibition-space/generate/suggest` | — | write/action - manual test |
| Generate | GET/POST | `/exhibition-space/generate` | — | write/action - manual test |
| Remove Placement | GET/POST | `/exhibition-space/placement/:id/remove` | — | write/action - manual test |

## Export (ahgExportPlugin)
*Category: ahg - enabled*

Archival export functionality for CSV, EAD, and other formats

## Extended Rights (ahgExtendedRightsPlugin)
*Category: ahg - enabled*

Extended rights management with RightsStatements.org integration, embargo management, Traditional Knowledge labels, and batch rights assignment

## Favorites (ahgFavoritesPlugin)
*Category: ahg - enabled*

User favorites/bookmarks management

## Federation (ahgFederationPlugin)
*Category: integration - enabled*

OAI-PMH Federation for metadata exchange

## Feedback (ahgFeedbackPlugin)
*Category: ahg - enabled*

User feedback and suggestions management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Delete | GET/POST | `/feedback/:id/delete` | — | write/action - manual test |
| Create / edit | GET | `/feedback/:id/edit` | — | needs param sample |
| View | GET | `/feedback/:id` | — | needs param sample |
| General | GET/POST | `/feedback/general` | — | write/action - manual test |
| Browse | GET | `/feedback` | ✅ 200 | |
| Submit | GET/POST | `/informationobject/:slug/feedback` | — | write/action - manual test |

## Forms (ahgFormsPlugin)
*Category: ahg - enabled*

Configurable metadata entry forms per repository

## FTP (ahgFtpPlugin)
*Category: import - enabled*

Browser-based FTP/SFTP upload for CSV import digital objects

## Function Manage (ahgFunctionManagePlugin)
*Category: manage - enabled*

ISDF function browse and management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Delete | GET/POST | `/function/:slug/delete` | — | write/action - manual test |
| Create / edit | GET | `/function/:slug/edit` | — | needs param sample |
| View | GET | `/function/:slug` | — | needs param sample |
| Create / edit | GET | `/function/add` | ✅ 200 | |
| Browse | GET | `/function/browse` | ✅ 200 | |

## Functions Docs (ahgFunctionsDocsPlugin)
*Category: admin - enabled*

Browsable catalogue of routes, CLI tasks and services

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Catalogue | GET/POST | `/admin/docs/catalogue` | — | write/action - manual test |

## GIS (ahgGISPlugin)
*Category: search - enabled*

Geospatial search and GeoJSON export for heritage records

## Gallery (ahgGalleryPlugin)
*Category: ahg - enabled*

Gallery and exhibition management with artist tracking, loans, insurance, and facility reports

## GraphQL (ahgGraphQLPlugin)
*Category: integration - enabled*

GraphQL API endpoint providing flexible querying with security safeguards

## Help (ahgHelpPlugin)
*Category: admin - enabled*

Online help system with searchable documentation and contextual help

## Heritage Accounting (ahgHeritageAccountingPlugin)
*Category: ahg - enabled*

## Heritage (ahgHeritagePlugin)
*Category: ahg - enabled*

Heritage discovery platform with contributor system, custodian management, and analytics

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Request Access | GET/POST | `/heritage/access/request/:slug` | — | write/action - manual test |
| Admin Access Requests | GET/POST | `/heritage/admin/access-requests` | — | write/action - manual test |
| Admin Branding | GET/POST | `/heritage/admin/branding` | — | write/action - manual test |
| Admin Config | GET/POST | `/heritage/admin/config` | — | write/action - manual test |
| Admin Embargoes | GET/POST | `/heritage/admin/embargoes` | — | write/action - manual test |
| Admin Featured Collections | GET/POST | `/heritage/admin/featured-collections` | — | write/action - manual test |
| Admin Features | GET/POST | `/heritage/admin/features` | — | write/action - manual test |
| Admin Hero Slides | GET/POST | `/heritage/admin/hero-slides` | — | write/action - manual test |
| Admin Popia | GET/POST | `/heritage/admin/popia` | — | write/action - manual test |
| Admin Users | GET/POST | `/heritage/admin/users` | — | write/action - manual test |
| Admin Dashboard | GET/POST | `/heritage/admin` | — | write/action - manual test |
| Analytics Alerts | GET/POST | `/heritage/analytics/alerts` | — | write/action - manual test |
| Analytics Content | GET/POST | `/heritage/analytics/content` | — | write/action - manual test |
| Analytics Search | GET/POST | `/heritage/analytics/search` | — | write/action - manual test |
| Analytics Dashboard | GET/POST | `/heritage/analytics` | — | write/action - manual test |
| Api Analytics | GET/POST | `/heritage/api/analytics` | — | write/action - manual test |
| Api Autocomplete | GET/POST | `/heritage/api/autocomplete` | — | write/action - manual test |
| Api Click | GET/POST | `/heritage/api/click` | — | write/action - manual test |
| Api Contribution Status | GET/POST | `/heritage/api/contribution/:id` | — | write/action - manual test |
| Api Submit Contribution | GET/POST | `/heritage/api/contribution/submit` | — | write/action - manual test |
| Api Discover | GET/POST | `/heritage/api/discover` | — | write/action - manual test |
| Api Dwell | GET/POST | `/heritage/api/dwell` | — | write/action - manual test |
| Api Entity Related | GET/POST | `/heritage/api/entity/:id/related` | — | write/action - manual test |
| Api Entity | GET/POST | `/heritage/api/entity/:type/:value` | — | write/action - manual test |
| Api Entity Search | GET/POST | `/heritage/api/entity/search` | — | write/action - manual test |
| Api Explore Categories | GET/POST | `/heritage/api/explore-categories` | — | write/action - manual test |
| Api Explore Category Items | GET/POST | `/heritage/api/explore/:category/items` | — | write/action - manual test |
| Api Featured Collections | GET/POST | `/heritage/api/featured-collections` | — | write/action - manual test |
| Api Graph Stats | GET/POST | `/heritage/api/graph/stats` | — | write/action - manual test |
| Api Hero Slides | GET/POST | `/heritage/api/hero-slides` | — | write/action - manual test |
| Api Landing | GET/POST | `/heritage/api/landing` | — | write/action - manual test |
| Api Suggest Tags | GET/POST | `/heritage/api/suggest-tags` | — | write/action - manual test |
| Api Timeline Periods | GET/POST | `/heritage/api/timeline-periods` | — | write/action - manual test |
| Api Timeline Period Items | GET/POST | `/heritage/api/timeline/:period_id/items` | — | write/action - manual test |
| Collections | GET/POST | `/heritage/collection/:id` | — | write/action - manual test |
| Collections | GET/POST | `/heritage/collections` | — | write/action - manual test |
| Contribute | GET/POST | `/heritage/contribute/:slug` | — | write/action - manual test |
| Contributor Profile | GET/POST | `/heritage/contributor/:id` | — | write/action - manual test |
| Creators Autocomplete | GET/POST | `/heritage/creators/autocomplete` | — | write/action - manual test |
| Creators | GET/POST | `/heritage/creators` | — | write/action - manual test |
| Custodian Item | GET/POST | `/heritage/custodian/:slug` | — | write/action - manual test |
| Custodian Batch | GET/POST | `/heritage/custodian/batch` | — | write/action - manual test |
| Custodian History | GET/POST | `/heritage/custodian/history` | — | write/action - manual test |
| Custodian Dashboard | GET/POST | `/heritage/custodian` | — | write/action - manual test |
| Entity | GET/POST | `/heritage/entity/:type/:value` | — | write/action - manual test |
| Explore | GET/POST | `/heritage/explore/:category` | — | write/action - manual test |
| Explore | GET/POST | `/heritage/explore` | — | write/action - manual test |
| Graph Data | GET/POST | `/heritage/graph/data` | — | write/action - manual test |
| Graph | GET/POST | `/heritage/graph` | — | write/action - manual test |
| Landing | GET | `/heritage/index` | ✅ 200 | |
| Leaderboard | GET/POST | `/heritage/leaderboard` | — | write/action - manual test |
| Contributor Login | GET/POST | `/heritage/login` | — | write/action - manual test |
| Contributor Logout | GET/POST | `/heritage/logout` | — | write/action - manual test |
| My Access Requests | GET/POST | `/heritage/my/access-requests` | — | write/action - manual test |
| My Contributions | GET/POST | `/heritage/my/contributions` | — | write/action - manual test |
| Contributor Register | GET/POST | `/heritage/register` | — | write/action - manual test |
| Review Contribution | GET/POST | `/heritage/review/:id` | — | write/action - manual test |
| Review Queue | GET/POST | `/heritage/review` | — | write/action - manual test |
| Search | GET | `/heritage/search` | ✅ 200 | |
| Timeline | GET | `/heritage/timeline/:period_id` | — | needs param sample |
| Timeline | GET | `/heritage/timeline` | ✅ 200 | |
| Trending | GET/POST | `/heritage/trending` | — | write/action - manual test |
| Contributor Verify | GET/POST | `/heritage/verify/:token` | — | write/action - manual test |
| Landing | GET | `/heritage` | ✅ 200 | |

## ICIP (ahgICIPPlugin)
*Category: ahg - enabled*

Indigenous Cultural and Intellectual Property management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Acknowledge | GET/POST | `/icip/acknowledge/:notice_id` | — | write/action - manual test |
| Api Check Access | GET/POST | `/icip/api/check-access/:object_id` | — | write/action - manual test |
| Api Summary | GET/POST | `/icip/api/summary/:object_id` | — | write/action - manual test |
| Communities | GET/POST | `/icip/communities` | — | write/action - manual test |
| Community Delete | GET/POST | `/icip/community/:id/delete` | — | write/action - manual test |
| Community Edit | GET/POST | `/icip/community/:id/edit` | — | write/action - manual test |
| Community View | GET/POST | `/icip/community/:id` | — | write/action - manual test |
| Community Edit | GET/POST | `/icip/community/add` | — | write/action - manual test |
| Consent Edit | GET/POST | `/icip/consent/:id/edit` | — | write/action - manual test |
| Consent View | GET/POST | `/icip/consent/:id` | — | write/action - manual test |
| Consent Edit | GET/POST | `/icip/consent/add` | — | write/action - manual test |
| Consent List | GET/POST | `/icip/consent` | — | write/action - manual test |
| Consultation Edit | GET/POST | `/icip/consultation/:id/edit` | — | write/action - manual test |
| Consultation View | GET/POST | `/icip/consultation/:id` | — | write/action - manual test |
| Consultation Edit | GET/POST | `/icip/consultation/add` | — | write/action - manual test |
| Consultations | GET/POST | `/icip/consultations` | — | write/action - manual test |
| Notice Types | GET/POST | `/icip/notice-types` | — | write/action - manual test |
| Notices | GET/POST | `/icip/notices` | — | write/action - manual test |
| Report Community | GET/POST | `/icip/reports/community/:id` | — | write/action - manual test |
| Report Expiry | GET/POST | `/icip/reports/consent-expiry` | — | write/action - manual test |
| Report Pending | GET/POST | `/icip/reports/pending-consultation` | — | write/action - manual test |
| Reports | GET | `/icip/reports` | ✅ 200 | |
| Restrictions | GET/POST | `/icip/restrictions` | — | write/action - manual test |
| Tk Labels | GET/POST | `/icip/tk-labels` | — | write/action - manual test |
| Dashboard | GET | `/icip` | ✅ 200 | |
| Object Consent | GET/POST | `/object/:slug/icip/consent` | — | write/action - manual test |
| Object Consultations | GET/POST | `/object/:slug/icip/consultations` | — | write/action - manual test |
| Object Labels | GET/POST | `/object/:slug/icip/labels` | — | write/action - manual test |
| Object Notices | GET/POST | `/object/:slug/icip/notices` | — | write/action - manual test |
| Object Restrictions | GET/POST | `/object/:slug/icip/restrictions` | — | write/action - manual test |
| Object Icip | GET/POST | `/object/:slug/icip` | — | write/action - manual test |

## IPSAS (ahgIPSASPlugin)
*Category: ahg - enabled*

IPSAS Heritage Asset Management - International public sector accounting for heritage assets

## IIIF (ahgIiifPlugin)
*Category: ahg - enabled*

IIIF plugin for manifests, viewer, and collections

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Autocomplete | GET | `/iiif/v3/manifest/:slug/autocomplete` | — | needs param sample |
| Search | GET | `/iiif/v3/manifest/:slug/search` | — | needs param sample |

## Image Ar (ahgImageArPlugin)
*Category: advanced_features - enabled*

Place a flat 2D image into augmented reality (WebXR)

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| View | GET | `/imagear/:slug` | — | needs param sample |
| View | GET | `/imagear` | ℹ️ n/a | by design: no index page - `/imagear/:slug` renders per object |

## Information Object Manage (ahgInformationObjectManagePlugin)
*Category: manage - enabled*

ISAD(G) information object CRUD management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Do Delete | GET/POST | `/digitalobject/:id/delete` | — | write/action - manual test |
| Do Edit | GET/POST | `/digitalobject/:id/edit` | — | write/action - manual test |
| Do Upload | GET/POST | `/digitalobject/attach/file` | — | write/action - manual test |
| Delete | GET/POST | `/informationobject/:slug/delete` | — | write/action - manual test |
| Create / edit | GET | `/informationobject/:slug/edit` | — | needs param sample |
| Actor Autocomplete | GET/POST | `/informationobject/actorAutocomplete` | — | write/action - manual test |
| Create / edit | GET | `/informationobject/add` | ✅ 200 | |
| Generate Identifier | GET/POST | `/informationobject/generateIdentifierJson` | — | write/action - manual test |
| Repository Autocomplete | GET/POST | `/informationobject/repositoryAutocomplete` | — | write/action - manual test |
| Term Autocomplete | GET/POST | `/informationobject/termAutocomplete` | — | write/action - manual test |

## Ingest (ahgIngestPlugin)
*Category: ingestion - enabled*

OAIS-aligned multi-stage ingestion pipeline

## Integrity (ahgIntegrityPlugin)
*Category: preservation - enabled*

Enterprise-grade automated integrity assurance: scheduled fixity verification, append-only ledger, dead-letter queue

## Jobs Manage (ahgJobsManagePlugin)
*Category: admin - available*

Background jobs browse and management

## Label (ahgLabelPlugin)
*Category: ahg - enabled*

Label generation for archival objects with customizable templates

## Landing Page (ahgLandingPagePlugin)
*Category: ahg - enabled*

Visual landing page builder with drag-and-drop blocks

## Library (ahgLibraryPlugin)
*Category: ahg - enabled*

Library cataloging with MARC-inspired fields, ISBN lookup, and bibliographic management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Counter5 | GET/POST | `/sushi/counter5` | — | write/action - manual test |

## Loan (ahgLoanPlugin)
*Category: ahg - enabled*

Shared loan management for GLAM institutions

## Marketplace (ahgMarketplacePlugin)
*Category: ecommerce - enabled*

Online marketplace for buying and selling across all GLAM sectors

## Menu Manage (ahgMenuManagePlugin)
*Category: admin - enabled*

Menu configuration management

## Metadata Export (ahgMetadataExportPlugin)
*Category: export - enabled*

GLAM Metadata Export Framework

## Metadata Extraction (ahgMetadataExtractionPlugin)
*Category: preservation - available*

Universal metadata extraction from digital objects

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Batch Extract | GET | `/metadataExtraction/batchExtract` | — | plugin not enabled |
| Delete | GET | `/metadataExtraction/delete` | — | plugin not enabled |
| Extract | GET | `/metadataExtraction/extract` | — | plugin not enabled |
| Status | GET | `/metadataExtraction/status` | — | plugin not enabled |
| View | GET | `/metadataExtraction/view/:id` | — | plugin not enabled |
| View | GET | `/metadataExtraction` | — | plugin not enabled |

## MODS Manage (ahgModsManagePlugin)
*Category: descriptive-standard - enabled*

MODS information object CRUD management

## Multi Tenant (ahgMultiTenantPlugin)
*Category: ahg - available*

Repository-based multi-tenancy with user hierarchy (Admin > Super User > User)

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Get Switcher | GET | `/tenant/switcher` | — | plugin not enabled |

## Museum (ahgMuseumPlugin)
*Category: ahg - enabled*

Museum cataloging with CCO (Cataloging Cultural Objects), CIDOC-CRM, and Spectrum 5.0 integration

## NARSSA (ahgNARSSAPlugin)
*Category: compliance - enabled*

NARSSA transfer manifest generator

## NAZ (ahgNAZPlugin)
*Category: ahg - enabled*

National Archives of Zimbabwe Act [Chapter 25:06] compliance - 25-year rule

## NMMZ (ahgNMMZPlugin)
*Category: ahg - enabled*

National Museums and Monuments of Zimbabwe Act [Chapter 25:11] - heritage protection

## Observability (ahgObservabilityPlugin)
*Category: integration - enabled*

## Ocfl (ahgOcflPlugin)
*Category: preservation - enabled*

## Portable Export (ahgPortableExportPlugin)
*Category: export - enabled*

Standalone portable catalogue viewer for CD/USB/ZIP distribution

## Preservation (ahgPreservationPlugin)
*Category: ahg - enabled*

Digital preservation: checksums, fixity verification, PREMIS events, format registry

## Privacy (ahgPrivacyPlugin)
*Category: ahg - enabled*

POPIA/GDPR Privacy Compliance Management

## Provenance (ahgProvenancePlugin)
*Category: ahg - enabled*

Chain of custody and provenance tracking

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Create / edit | GET | `/provenance/:slug/edit` | — | needs param sample |
| Export | GET/POST | `/provenance/:slug/export` | — | write/action - manual test |
| Timeline | GET | `/provenance/:slug/timeline` | — | needs param sample |
| View | GET | `/provenance/:slug` | — | needs param sample |
| Add Event | GET/POST | `/provenance/addEvent` | — | write/action - manual test |
| Delete Document | GET/POST | `/provenance/deleteDocument/:id` | — | write/action - manual test |
| Delete Event | GET/POST | `/provenance/deleteEvent` | — | write/action - manual test |
| Search Agents | GET/POST | `/provenance/searchAgents` | — | write/action - manual test |
| View | GET | `/provenance` | ✅ 200 | |

## RAD Manage (ahgRadManagePlugin)
*Category: descriptive-standard - enabled*

RAD information object CRUD management

## Rdm (ahgRdmPlugin)
*Category: research - enabled*

## Records Manage (ahgRecordsManagePlugin)
*Category: general - on disk*

## Registry (ahgRegistryPlugin)
*Category: community - enabled*

AtoM/Heratio Community Hub & Registry - Directory of institutions, vendors, software, user groups, discussions, blog, and sync API.

## Report Builder (ahgReportBuilderPlugin)
*Category: ahg - enabled*

Custom report builder with drag-drop designer, charts, scheduling, and export

## Reports (ahgReportsPlugin)
*Category: ahg - enabled*

Central reporting dashboard for AtoM

## Repository Manage (ahgRepositoryManagePlugin)
*Category: browse - enabled, locked*

High-performance archival institution browse and management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Delete | GET/POST | `/repository/:slug/delete` | — | write/action - manual test |
| Create / edit | GET | `/repository/:slug/edit` | — | needs param sample |
| View | GET | `/repository/:slug` | — | needs param sample |
| Create / edit | GET | `/repository/add` | ✅ 200 | |
| Browse | GET | `/repository/browse` | ✅ 200 | |

## Request To Publish (ahgRequestToPublishPlugin)
*Category: ahg - enabled*

Manage publication requests for archival images and digital objects

## Research (ahgResearchPlugin)
*Category: ahg - enabled*

Research support plugin with reading room booking, researcher registration, and workspace management

## Researcher (ahgResearcherPlugin)
*Category: research - enabled*

Researcher collection upload and approval workflow

## Resource Sync (ahgResourceSyncPlugin)
*Category: integration - enabled*

## RiC Explorer (ahgRicExplorerPlugin)
*Category: ahg - enabled*

Records in Context (RiC) visualization, exploration, and Fuseki triplestore integration

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Ajax Cleanup Orphans | GET/POST | `/admin/ric/ajax/cleanup-orphans` | — | write/action - manual test |
| Ajax Integrity Check | GET/POST | `/admin/ric/ajax/integrity-check` | — | write/action - manual test |
| Ajax Clear Queue Item | GET/POST | `/admin/ric/ajax/queue-item` | — | write/action - manual test |
| Ajax Resync | GET/POST | `/admin/ric/ajax/resync` | — | write/action - manual test |
| Ajax Stats | GET/POST | `/admin/ric/ajax/stats` | — | write/action - manual test |
| Ajax Update Orphan | GET/POST | `/admin/ric/ajax/update-orphan` | — | write/action - manual test |
| Configure | GET | `/admin/ric/config` | ✅ 200 | |
| Logs | GET/POST | `/admin/ric/logs` | — | write/action - manual test |
| Orphans | GET/POST | `/admin/ric/orphans` | — | write/action - manual test |
| Queue | GET/POST | `/admin/ric/queue` | — | write/action - manual test |
| Report | GET | `/admin/ric/shacl/report/:id` | — | needs param sample |
| Run | GET/POST | `/admin/ric/shacl/run` | — | write/action - manual test |
| View | GET | `/admin/ric/shacl` | ✅ 200 | |
| Sync Status | GET/POST | `/admin/ric/sync-status` | — | write/action - manual test |
| View | GET | `/admin/ric` | ✅ 200 | |
| Autocomplete | GET | `/ricExplorer/autocomplete` | ✅ 200 | |
| Get Data | GET/POST | `/ricExplorer/getData` | — | write/action - manual test |
| Knowledge Graph | GET/POST | `/ricExplorer/knowledge-graph/:id` | — | write/action - manual test |
| Knowledge Graph | GET/POST | `/ricExplorer/knowledge-graph` | — | write/action - manual test |
| Provenance Graph | GET/POST | `/ricExplorer/provenance/:id` | — | write/action - manual test |
| Provenance Graph | GET/POST | `/ricExplorer/provenance` | — | write/action - manual test |
| Ajax Validate Entity | GET/POST | `/ricShacl/ajaxValidateEntity` | — | write/action - manual test |

## Rights Holder Manage (ahgRightsHolderManagePlugin)
*Category: browse - enabled, locked*

Rights holder browse and management using Laravel Query Builder

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Delete | GET/POST | `/rightsholder/:slug/delete` | — | write/action - manual test |
| Create / edit | GET | `/rightsholder/:slug/edit` | — | needs param sample |
| View | GET | `/rightsholder/:slug` | — | needs param sample |
| Create / edit | GET | `/rightsholder/add` | ✅ 200 | |
| Browse | GET | `/rightsholder/browse` | ✅ 200 | |

## Rights (ahgRightsPlugin)
*Category: ahg - enabled*

Core rights management including PREMIS rights, Creative Commons, rights holders, and orphan works tracking

## Scan (ahgScanPlugin)
*Category: ingestion - enabled*

## Search (ahgSearchPlugin)
*Category: search - enabled*

Global search, autocomplete, description updates, and search/replace

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Autocomplete | GET | `/search/autocomplete` | ✅ 200 | |
| Description Updates | GET/POST | `/search/descriptionUpdates` | — | write/action - manual test |
| Global Replace | GET/POST | `/search/globalReplace` | — | write/action - manual test |
| View | GET | `/search/index` | ℹ️ n/a | by design: non-primary - use `/informationobject/browse` (base `/search` also 404s) |
| View | GET | `/search/semantic` | ✅ 200 | |

## Security Clearance (ahgSecurityClearancePlugin)
*Category: ahg - enabled, core, locked*

Security classification, user clearance, embargo, watermarking and extended rights management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Acl Group Edit | GET/POST | `/admin/security/acl-group/:id` | — | write/action - manual test |
| Acl Groups | GET/POST | `/admin/security/acl-groups` | — | write/action - manual test |
| Security Compliance | GET/POST | `/admin/security/compliance` | — | write/action - manual test |
| Revoke Access | GET/POST | `/security/access/:id/revoke` | — | write/action - manual test |
| Revoke | GET/POST | `/security/clearance/:id/revoke` | — | write/action - manual test |
| View | GET | `/security/clearance/:id` | — | needs param sample |
| Bulk Grant | GET/POST | `/security/clearance/bulk-grant` | — | write/action - manual test |
| Grant | GET/POST | `/security/clearance/grant` | — | write/action - manual test |
| User | GET/POST | `/security/clearance/user/:slug` | — | write/action - manual test |
| View | GET | `/security/clearances` | ✅ 200 | |
| Compartments | GET/POST | `/security/compartments` | — | write/action - manual test |
| Dashboard | GET | `/security/dashboard` | ✅ 200 | |
| Report | GET | `/security/report` | ✅ 200 | |
| Create Object Request | GET/POST | `/security/request/submit` | — | write/action - manual test |

## Semantic Search (ahgSemanticSearchPlugin)
*Category: ahg - enabled*

Semantic search with thesaurus, WordNet/Wikidata sync, and vector embeddings

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Admin Templates | GET/POST | `/admin/search/templates` | — | write/action - manual test |
| Configure | GET | `/admin/semantic-search/config` | ✅ 200 | |
| Search Logs | GET/POST | `/admin/semantic-search/search-logs` | — | write/action - manual test |
| Sync Logs | GET/POST | `/admin/semantic-search/sync-logs` | — | write/action - manual test |
| Term View | GET/POST | `/admin/semantic-search/term/:id` | — | write/action - manual test |
| Term Add | GET/POST | `/admin/semantic-search/term/add` | — | write/action - manual test |
| Terms | GET/POST | `/admin/semantic-search/terms` | — | write/action - manual test |
| View | GET | `/admin/semantic-search` | ✅ 200 | |
| Delete Saved Search | GET/POST | `/search/delete/:id` | — | write/action - manual test |
| History | GET/POST | `/search/history` | — | write/action - manual test |
| Run Saved Search | GET/POST | `/search/run/:id` | — | write/action - manual test |
| Saved Searches | GET/POST | `/search/saved` | — | write/action - manual test |
| Save Search | GET/POST | `/search/save` | — | write/action - manual test |
| Run Template | GET/POST | `/search/template/:id` | — | write/action - manual test |
| Run Sync | GET/POST | `/semanticSearchAdmin/runSync` | — | write/action - manual test |
| Test Expand | GET/POST | `/semanticSearchAdmin/testExpand` | — | write/action - manual test |

## Settings (ahgSettingsPlugin)
*Category: admin - enabled, core*

AHG Settings Management

## Share Point (ahgSharePointPlugin)
*Category: integration - enabled*

## Spectrum (ahgSpectrumPlugin)
*Category: ahg - enabled*

Spectrum 5.0 museum procedures - acquisition, loans, movement, conservation, valuation, and workflow management

## Static Page (ahgStaticPagePlugin)
*Category: admin - enabled*

Static page management

## Statistics (ahgStatisticsPlugin)
*Category: ahg - enabled*

Usage statistics tracking

## Storage Manage (ahgStorageManagePlugin)
*Category: browse - enabled, locked*

Physical storage browse and management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Autocomplete | GET | `/physicalobject/autocomplete` | ✅ 200 | |
| Box List | GET/POST | `/physicalobject/boxList` | — | write/action - manual test |
| Browse | GET | `/physicalobject/browse` | ✅ 200 | |
| Holdings Report Export | GET/POST | `/physicalobject/holdingsReportExport` | — | write/action - manual test |
| Assign | GET/POST | `/strongroom/:slug/assign` | — | write/action - manual test |
| Delete | GET/POST | `/strongroom/:slug/delete` | — | write/action - manual test |
| Create / edit | GET | `/strongroom/:slug/edit` | — | needs param sample |
| View | GET | `/strongroom/:slug` | — | needs param sample |
| Create | GET/POST | `/strongroom/add` | — | write/action - manual test |
| Browse | GET | `/strongroom/browse` | ✅ 200 | |
| Unassign | GET/POST | `/strongroom/unassign` | — | write/action - manual test |

## Term Taxonomy (ahgTermTaxonomyPlugin)
*Category: browse - enabled, locked*

High-performance term and taxonomy browse

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Export Skos | GET/POST | `/taxonomy/:id/skos` | — | write/action - manual test |
| Taxonomy Index | GET/POST | `/taxonomy/:id` | — | write/action - manual test |
| Delete | GET/POST | `/term/:slug/delete` | — | write/action - manual test |
| Create / edit | GET | `/term/:slug/edit` | — | needs param sample |
| Related Authorities | GET/POST | `/term/:slug/related-authorities` | — | write/action - manual test |
| View | GET | `/term/:slug` | — | needs param sample |
| Create / edit | GET | `/term/add` | ✅ 200 | |

## Theme B5 (ahgThemeB5Plugin)
*Category: ahg - available, core, locked*

Modern Bootstrap 5 theme for Access to Memory

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Describe Image | GET | `/ahgVoice/describeImage` | — | plugin not enabled |
| Describe Object | GET | `/ahgVoice/describeObject` | — | plugin not enabled |
| Get Settings | GET | `/ahgVoice/getSettings` | — | plugin not enabled |
| Save Description | GET | `/ahgVoice/saveDescription` | — | plugin not enabled |

## TIFF/PDF Merge (ahgTiffPdfMergePlugin)
*Category: ahg - enabled*

TIFF and PDF merge job management for digital preservation

## Time Limited Share Link (ahgTimeLimitedShareLinkPlugin)
*Category: records-management - enabled*

Time-limited, auditable share links for information_object records (anonymous bearer-token access, HMAC-SHA256 tokens, admin revocation, retention sweeps)

## Translation (ahgTranslationPlugin)
*Category: ahg - enabled*

Machine Translation with LibreTranslate

## UI Overrides (ahgUiOverridesPlugin)
*Category: ahg - enabled, locked*

UI action overrides for AtoM modules - centralized location for action customizations

## User Manage (ahgUserManagePlugin)
*Category: browse - enabled*

User browse and management

| Function | Method | URL | Status | Why (if not 200) |
|---|---|---|---|---|
| Delete | GET/POST | `/user/:slug/delete` | — | write/action - manual test |
| Create / edit | GET | `/user/:slug/edit` | — | needs param sample |
| View | GET | `/user/:slug` | — | needs param sample |
| Create / edit | GET | `/user/add` | ✅ 200 | |
| Clipboard | GET/POST | `/user/clipboard` | — | write/action - manual test |
| Browse | GET | `/user/list` | ✅ 200 | |
| Login | GET/POST | `/user/login` | — | write/action - manual test |
| Logout | GET/POST | `/user/logout` | — | write/action - manual test |
| Password Edit | GET/POST | `/user/passwordEdit` | — | write/action - manual test |
| Password Reset | GET/POST | `/user/passwordReset` | — | write/action - manual test |
| Browse | GET | `/user` | ✅ 200 | |

## User Registration (ahgUserRegistrationPlugin)
*Category: user - enabled*

Public user self-registration with email verification and admin approval workflow

## Vendor (ahgVendorPlugin)
*Category: ahg - enabled*

## Version Control (ahgVersionControlPlugin)
*Category: records-management - enabled*

Version history with diff and restore for information_object and actor

## Workflow (ahgWorkflowPlugin)
*Category: ahg - enabled*

Configurable approval workflow system
