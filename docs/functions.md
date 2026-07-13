# AtoM Heratio (PSIS) - Complete Function Reference

**Platform:** AtoM 2.10.1 base (Symfony) + atom-framework + atom-ahg-plugins
**Instance:** PSIS / archive (`/usr/share/nginx/archive`)
**Last updated:** 13 July 2026

Complete listing of the functionality across the AHG plugin suite on the PSIS/archive stack, generated from a full audit of every installed plugin's routes (user-facing functions) and CLI tasks in the live `atom_plugin` registry. The AtoM 2.10.1 base additionally provides the core archival functions (ISAD(G)/ISAAR/ISDF/ISDIAH description, authority records, repositories, taxonomies, digital objects, search, import/export) that these plugins extend.

Plugins on disk: 111

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
### Model3d
- Add Bookmark
- Add Hotspot
- Api Bookmarks
- Api Hotspots
- Api Models
- Delete
- Delete Bookmark
- Delete Hotspot
- Create / edit
- Embed
- Iiif Manifest
- View
- Upload
- View
### Model3dSettings
- View
- Triposr
### CLI Commands
- `php symfony triposr:generate` - Generate 3D model from 2D image using TripoSR

## AI (ahgAIPlugin)
*Category: ahg - enabled*

AI-powered tools: NER, Translation, Summarization, Spellcheck
### Ai
- Assistant (`/ai/assistant`)
- Assistant Ask (`/ai/assistant/ask`)
- Batch (`/ai/batch`)
- Batch Action (`/ai/batch/:id/action`)
- Batch Create (`/ai/batch/create`)
- Batch Process (`/ai/batch/:id/process`)
- Batch Progress (`/ai/batch/:id/progress`)
- Batch View (`/ai/batch/:id`)
- Bulk Save (`/ner/bulk-save`)
- Catalog (`/ai/catalog/:id`)
- Catalog Apply (`/ai/catalog/:id/apply`)
- Create Actor (`/ai/ner/create/actor`)
- Create Place (`/ai/ner/create/place`)
- Create Subject (`/ai/ner/create/subject`)
- Donut Dashboard (`/ai/donut`)
- Donut Finalize (`/ai/donut/finalize`)
- Donut Positions (`/ai/donut/positions`)
- Donut Prefill (`/ai/donut/prefill`)
- Donut Result (`/ai/donut/results/:id`)
- Extract (`/ner/extract/:id`)
- Get Approved Entities (`/ai/ner/approved-entities/:id`)
- Get Entities (`/ner/entities/:id`)
- Governance (`/ai/governance`)
- Governance Inferences (`/ai/governance/inferences`)
- Governance Models (`/ai/governance/models`)
- Health (`/ai/ner/health`)
- Htr (`/ner/htr/:id`)
- Job View (`/ai/job/:id`)
- Llm Configs (`/ai/llm/configs`)
- Llm Health (`/ai/llm/health`)
- Pdf Overlay (`/ai/ner/pdf-overlay/:id`)
- Research (`/ai/research`)
- Research Ask (`/ai/research/ask`)
- Research Session (`/ai/research/session/:id`)
- Research Sessions (`/ai/research/sessions`)
- Review (`/ner/review`)
- Suggest (`/ai/suggest/:id`)
- Suggest Decision (`/ai/suggest/:id/decision`)
- Suggest Object (`/ai/suggest/object/:id`)
- Suggest Preview (`/ai/suggest/:id/preview`)
- Suggest Review (`/ai/suggest/review`)
- Suggest View (`/ai/suggest/:id/view`)
- Summarize (`/ner/summarize/:id`)
- Templates (`/ai/templates`)
- Update Entity (`/ai/ner/entity/update`)
### CLI Commands
- `php symfony ai:htr` - Extract handwritten text from digital objects using TrOCR
- `php symfony ai:index-catalogue` - Build the gateway-fed semantic search index (Qdrant) for published descriptions
- `php symfony ai:install` - Install ahgAIPlugin database tables
- `php symfony ai:install-menu` - Add the Collection assistant nav link (idempotent)
- `php symfony ai:install-research-menu` - Add the Researcher Copilot nav link (idempotent)
- `php symfony ai:ner-extract` - Extract named entities from archival records
- `php symfony ai:ner-sync` - Sync NER corrections to training server
- `php symfony ai:process-pending` - Process pending AI extraction queue
- `php symfony ai:spellcheck` - Check spelling in archival records
- `php symfony ai:suggest-description` - Generate AI description suggestions for archival records
- `php symfony ai:summarize` - Generate summaries for archival records
- `php symfony ai:sync-entity-cache` - Sync approved NER entities to heritage discovery cache
- `php symfony ai:translate` - Translate archival records between cultures
- `php symfony ai:uninstall` - Uninstall ahgAIPlugin

## API (ahgAPIPlugin)
*Category: ahg - enabled*
### Api
- Autocomplete Glam
- Plugin Protection
- Search Information Objects
### Apiv2
- Asset Valuations
- Assets Browse
- Assets Create
- Assets Read
- Assets Update
- Audit Browse
- Audit Read
- Authorities Browse
- Authorities Read
- Batch
- Breaches Browse
- Breaches Create
- Condition Photo Delete
- Condition Photo Upload
- Condition Photos
- Conditions Browse
- Conditions Create
- Conditions Delete
- Conditions Read
- Conditions Update
- Description Asset
- Description Conditions
- Description Upload
- Descriptions Browse
- Descriptions Citation
- Descriptions Create
- Descriptions Delete
- Descriptions Read
- Descriptions Update
- Digital Objects Read
- Docs
- Dsars Browse
- Dsars Create
- Dsars Read
- Dsars Update
- Events Browse
- Events Correlation
- Events Read
- File Upload
- View
- Keys Browse
- Keys Create
- Keys Delete
- Not Found
- Open Api
- Publish Execute
- Publish Readiness
- Repositories Browse
- Search
- Sync Batch
- Sync Changes
- Taxonomies Browse
- Taxonomy Terms
- Valuations Browse
- Valuations Create
- Webhook Deliveries
- Webhook Regenerate Secret
- Webhooks Browse
- Webhooks Create
- Webhooks Delete
- Webhooks Read
- Webhooks Update
### IdentifierApi
- Barcode
- Detect
- Lookup
- Types
- Validate
### CLI Commands
- `php symfony api:webhook-process-retries` - Process pending webhook retries

## Access Request (ahgAccessRequestPlugin)
*Category: ahg - enabled, locked*

Researcher access request management for restricted materials
### AccessRequest
- Add Approver (`/security/approvers/add`)
- Approve (`/security/request/:id/approve`)
- Approvers (`/security/approvers`)
- Cancel (`/security/request/:id/cancel`)
- Create (`/security/request-access/create`)
- Create Object Request (`/security/request-object/create`)
- Deny (`/security/request/:id/deny`)
- My Requests (`/security/my-requests`)
- New (`/security/request-access`)
- Pending (`/security/requests`)
- Remove Approver (`/security/approvers/:id/remove`)
- Request Object (`/security/request-object`)
- View (`/security/request/:id/review`)

## Accessibility (ahgAccessibilityPlugin)
*Category: reporting - enabled*

WCAG accessibility tooling (image alternative text)
### Accessibility
- Api Object
- Api Slug
- Create / edit
- View
- Save

## Accession Manage (ahgAccessionManagePlugin)
*Category: browse - enabled, locked*

High-performance accession browse and management
### Accession
- Delete (`/accession/:slug/delete`)
- Create / edit (`/accession/add`)
- View (`/accession/:slug`)
### AccessionManage
- Browse (`/accession/browse`)
### CLI Commands
- `php symfony accession:intake` - Manage accession intake queue
- `php symfony accession:report` - Accession reports and exports

## Actor Manage (ahgActorManagePlugin)
*Category: browse - enabled, locked*

High-performance actor browse, autocomplete, and management
### ActorManage
- Autocomplete (`/actor/autocomplete`)
- Browse (`/actor/browse`)
### SfIsaarPlugin
- Delete (`/actor/:slug/delete`)
- Create / edit (`/actor/add`)
- View (`/actor/:slug`)

## AI Compliance (ahgAiCompliancePlugin)
*Category: general - enabled*
### AiActGovernance
- Attestation Edit
- Attestations
- View
- Model Edit
- Models
- Risk Edit
- Risks
- System Edit
- Systems
### AiCompliance
- Well Known Pubkey
### CLI Commands
- `php symfony ai-compliance:install-key` - Generate the Ed25519 signing keypair for the AI inference log
- `php symfony ai-compliance:prune` - Null payload_json on inference-log rows older than the retention window
- `php symfony ai-compliance:verify-inference-log` - Walk the ai_inference_log chain and validate hashes + signatures

## AI Condition (ahgAiConditionPlugin)
*Category: ai - enabled*

AI-powered condition assessment for archival materials using YOLOv8 and EfficientNet
### AiCondition
- Api Bulk Status
- Api Client Approve Training
- Api Client Contributions
- Api Client Revoke
- Api Client Save
- Api Client Training Toggle
- Api Client Upload Consent
- Api Confirm
- Api Contribute
- Api Contribution Review
- Api Contributions
- Api History Data
- Api Manual Save
- Api Object Search
- Api Push Training Data
- Api Submit
- Api Test
- Api Training Datasets
- Api Training Model Info
- Api Training Start
- Api Training Status
- Api Training Upload
- Assess
- Browse
- Bulk
- Clients
- Dashboard
- History
- View
- Manual Assess
- Configure
- Training
- View
### CLI Commands
- `php symfony ai-condition:bulk-scan` - Bulk scan digital objects for condition assessment
- `php symfony ai-condition:install` - Install AI Condition Assessment tables
- `php symfony ai-condition:status` - Check AI Condition Service health

## Annotations (ahgAnnotationsPlugin)
*Category: advanced_features - enabled*

W3C Web Annotation Data Model + Protocol backend
### Annotation
- Container (`/annotations`)
- Single (`/annotations/:uuid`)

## Audit Trail (ahgAuditTrailPlugin)
*Category: ahg - enabled*

Comprehensive audit trail logging for AtoM with POPIA/NARSSA compliance
### AuditTrail
- Authentication (`/admin/audit/authentication`)
- Browse (`/admin/audit`)
- Compare Data (`/admin/audit/compare/:id`)
- Entity History (`/admin/audit/entity/:entity_type/:entity_id`)
- Export (`/admin/audit/export`)
- Integrity (`/admin/audit/integrity`)
- Configure (`/admin/audit/settings`)
- Statistics (`/admin/audit/statistics`)
- User Activity (`/admin/audit/user/:user_id`)
- View (`/admin/audit/view/:id`)
### CLI Commands
- `php symfony audit:chain` - Verify (or --seal) the ahg_audit_log tamper-evident hash chain

## Authority (ahgAuthorityPlugin)
*Category: authority - enabled*
### Authority
- Api Completeness Batch Assign
- Api Completeness Recalc
- Api Eac Export
- Api Function Delete
- Api Function Save
- Api Graph Data
- Api Identifier Delete
- Api Identifier Save
- Api Identifier Verify
- Api Lcnaf Search
- Api Merge Execute
- Api Merge Preview
- Api Occupation Delete
- Api Occupation Save
- Api Split Execute
- Api Ulan Search
- Api Viaf Search
- Api Wikidata Search
- Configure
- Contact
- Dashboard
- Function Browse
- Functions
- Identifiers
- Merge
- Occupations
- Split
- Workqueue
### AuthorityDedup
- Api Dismiss
- Api Merge
- Compare
- View
- Scan
### AuthorityNer
- Api Create Stub
- Api Promote
- Api Reject
- View
### CLI Commands
- `php symfony authority:completeness-scan` - Calculate completeness scores for authority records
- `php symfony authority:dedup-scan` - Scan for duplicate authority records
- `php symfony authority:function-sync` - Sync and validate actor-function links
- `php symfony authority:merge-report` - Generate authority merge/split report
- `php symfony authority:ner-pipeline` - Create authority stubs from NER entities

## Authority Resolution (ahgAuthorityResolutionPlugin)
*Category: authority - enabled*
### AuthorityResolution
- Archivists Json
- Assign
- Batch Assign
- Context
- Create New
- Create New Submit
- View
- Link
- Link Different
- Lookup
- Lookup Settings
- Lookup Settings Save
- Park
- Park Dashboard Json
- Park List
- Reject
- Review
- Unpark
### CLI Commands
- `php symfony auth-res:cache-clear` - Evict rows from ahg_authority_lookup_cache by source or wholesale.
- `php symfony auth-res:cache-stats` - Report ahg_authority_lookup_cache contents grouped by source (entity-type breakdown + oldest/newest retrieval).
- `php symfony auth-res:export-ner-feedback` - Export rejected-mention feedback as a training corpus (JSONL or CoNLL).
- `php symfony auth-res:generate-candidates` - Generate ranked authority candidates for an ahg_mention.
- `php symfony auth-res:promote-sample` - Promote PERSON/ORG/GPE entities for an information object into the authority-resolution mention workflow.
- `php symfony auth-res:reprocess` - Re-run candidate generation + evidence scoring for a mention (or every pending mention).
- `php symfony auth-res:reprocess-parked` - Bulk-unpark every ahg_mention_park row parked since DATE and re-run candidate generation + scoring.
- `php symfony auth-res:scan-parked` - Flag parked mentions whose candidate set has changed since parking.
- `php symfony auth-res:score-evidence` - Score evidence signals + composite for each candidate of a mention. Re-ranks by composite.
- `php symfony auth-res:status` - Summarise the authority-resolution working set (mentions, candidates, decisions, parked, feedback, cache, Fuseki).
- `php symfony auth-res:write-provenance` - Write RDF-Star provenance for an authority-resolution decision to Fuseki.

## Backup (ahgBackupPlugin)
*Category: ahg - enabled*

Database and file backup with scheduling, restore, upload and retention management
### Backup
- Create
- Create Incremental
- Create Schedule
- Delete
- Delete Schedule
- Delete Upload
- Do Restore
- Do Restore Upload
- Do Upload
- Download
- View
- Restore
- Restore Upload
- Schedules
- Configure
- Test Connection
- Toggle Schedule
- Upload
### CLI Commands
- `php symfony backup:run-scheduled` - Execute due scheduled backups

## C2PA (ahgC2paPlugin)
*Category: ahg - enabled*
### C2pa
- Manifest
- Manifests
- Verify
- Well Known

## CDPA (ahgCDPAPlugin)
*Category: ahg - enabled*

Zimbabwe Cyber and Data Protection Act [Chapter 12:07] compliance - POTRAZ regulated
### Cdpa
- Breach Create
- Breach View
- Breaches
- Configure
- Consent
- Dpia
- Dpia Create
- Dpia View
- Dpo
- Dpo Edit
- View
- License
- License Edit
- Processing
- Processing Create
- Processing Edit
- Reports
- Request Create
- Request View
- Requests
### CLI Commands
- `php symfony cdpa:license-check` - Check POTRAZ license expiry
- `php symfony cdpa:report` - Generate CDPA compliance report
- `php symfony cdpa:requests` - List data subject requests
- `php symfony cdpa:status` - Show CDPA compliance dashboard

## Cart (ahgCartPlugin)
*Category: ahg - enabled*

Shopping cart for reproduction requests
### Cart
- Download (`/cart/download/:token`)
- Order Confirmation (`/cart/order/:order`)
- Payment Notify (`/cart/payment/notify`)

## Condition (ahgConditionPlugin)
*Category: ahg - enabled*

Condition assessment and reporting for physical objects with Spectrum 5.0 compliance
### Condition
- Administer
- Ai Assess
- Annotate
- Condition Check
- Delete Photo
- Export Report
- Get Annotation
- List Photos
- Object Autocomplete
- Photos
- Save Annotation
- Template
- Update Photo Meta
- Upload
- View
- View Photo

## Contact (ahgContactPlugin)
*Category: ahg - enabled*

Extended contact information for actors

## Core (ahgCorePlugin)
*Category: core - enabled, core, locked*

Core utilities and shared services for AHG plugins
### Tts
- Pdf Text (`/tts/pdfText`)
- Configure (`/tts/settings`)
### CLI Commands
- `php symfony ahg:optimize-pdfs` - Generate web-optimized PDF siblings so large documents load fast
- `php symfony central:heartbeat` - Send a heartbeat (alive + version) to AHG Central.
- `php symfony central:ping` - Ping the configured AHG Central endpoint and report HTTP status.
- `php symfony central:sync-errors` - Sync the open ahg_error_log rows to AHG Central (redacted, full replace).

## Custom Fields (ahgCustomFieldsPlugin)
*Category: metadata - enabled*

Admin-configurable custom metadata fields for any entity type
### CustomField
- Get Values
- Save Values
### CustomFieldAdmin
- Delete
- Create / edit
- Export
- Import
- View
- Reorder
- Save

## DAM (ahgDAMPlugin)
*Category: ahg - enabled*

Digital Asset Management with IPTC metadata, watermarks, derivatives, and Creative Commons licensing
### Dam
- Add
- Browse
- Bulk Create
- Convert
- Create
- Dashboard
- Create / edit
- Edit Iptc
- Extract Metadata
- View
### DamReports
- Assets
- Export Csv
- View
- Iptc
- Metadata
- Storage

## DACS Manage (ahgDacsManagePlugin)
*Category: descriptive-standard - enabled*

DACS information object CRUD management
### DacsManage
- Create / edit

## Data Migration (ahgDataMigrationPlugin)
*Category: ahg - enabled*

Data migration tool for moving records between GLAM sectors
### DataMigration
- Ahg Import Results (`/dataMigration/ahgImportResults`)
- Batch Export (`/dataMigration/batchExport`)
- Cancel Job (`/dataMigration/job/cancel`)
- Download (`/admin/data-migration/download`)
- Execute (`/dataMigration/execute`)
- Execute Ahg Import (`/dataMigration/executeAhgImport`)
- Export (`/admin/data-migration/export`)
- Export Csv (`/dataMigration/exportCsv`)
- Export Mapping (`/dataMigration/exportMapping/:id`)
- Get Mapping (`/admin/data-migration/mapping`)
- Import (`/admin/data-migration/import`)
- Import Mapping (`/dataMigration/importMapping`)
- View (`/dataMigration`)
- Job Progress (`/dataMigration/job/progress`)
- Job Status (`/dataMigration/job/:id`)
- Jobs (`/dataMigration/jobs`)
- Load Mapping (`/dataMigration/loadMapping`)
- Map (`/dataMigration/map`)
- Preservica Export (`/admin/data-migration/preservica/export/:id`)
- Preservica Import (`/admin/data-migration/preservica/import`)
- Preview (`/dataMigration/preview`)
- Preview Validation (`/dataMigration/previewValidation`)
- Queue Job (`/dataMigration/queue`)
- Save Mapping (`/dataMigration/saveMapping`)
- Sector Export (`/dataMigration/export/:sector`)
- Upload (`/dataMigration/upload`)
- Validate (`/dataMigration/validate`)
### CLI Commands
- `php symfony archives-csv-import` - Import archives CSV data with ISAD-G validation
- `php symfony dam-csv-import` - Import DAM CSV data with Dublin Core/IPTC validation
- `php symfony gallery-csv-import` - Import gallery CSV data with CCO validation
- `php symfony library-csv-import` - Import library CSV data with MARC/RDA validation
- `php symfony migration:import` - Import data using saved field mappings
- `php symfony museum-csv-import` - Import museum CSV data with Spectrum validation
- `php symfony preservica:export` - Export data to Preservica OPEX or PAX format
- `php symfony preservica:import` - Import data from Preservica OPEX or PAX format
- `php symfony preservica:info` - Show Preservica format information and field mappings

## DC Manage (ahgDcManagePlugin)
*Category: descriptive-standard - enabled*

Dublin Core information object CRUD management
### DcManage
- Create / edit

## Dedupe (ahgDedupePlugin)
*Category: ahg - enabled*

Duplicate detection for archival records
### Dedupe
- Api Check
- Api Realtime
- Browse
- Compare
- Dismiss
- View
- Merge
- Report
- Rule Create
- Rule Delete
- Rule Edit
- Rules
- Scan
- View
### CLI Commands
- `php symfony dedupe:merge` - Merge duplicate records
- `php symfony dedupe:report` - Generate duplicate detection reports
- `php symfony dedupe:scan` - Scan for duplicate records

## Discovery (ahgDiscoveryPlugin)
*Category: search - enabled*
### Discovery
- Build
- Click
- View
- Pageindex
- Pageindex Api
- Popular
- Related
- Search
- Suggest

## Display (ahgDisplayPlugin)
*Category: ahg - enabled, locked*

GLAM browser and display modes for archival content
### Digitalobject
- Delete
- Create / edit
- Upload
### Display
- Assign Profile
- Browse
- Browse Ajax
- Browse Settings
- Bulk Set Type
- Change Type
- Export Csv
- Fields
- Get Browse Settings
- View
- Levels
- Print
- Profiles
- Reset Browse Settings
- Save Browse Settings
- Set Type
- Toggle Glam Browse
### DisplaySearch
- Autocomplete
- Browse
- Facets
- Reindex
- Search
- Update Mapping
### Informationobject
- Add Cart
- Add Favorites
- Edit Request To Publish
- Isbn Lookup
- Multi File Upload
- Remove Cart
- Remove Favorites
- Rename
### Object
- Add Digital Object
### Physicalobject
- Browse
- Delete
- Create / edit
- View
### Treeview
- Sort
- View
### CLI Commands
- `php symfony ahg:add-fulltext-indexes` - Add FULLTEXT indexes for fuzzy search
- `php symfony ahg:refresh-facet-cache` - Refresh display facet cache
- `php symfony display:auto-detect` - Auto-detect GLAM types for all information objects
- `php symfony display:reindex` - Reindex display data in Elasticsearch

## DOI (ahgDoiPlugin)
*Category: ahg - enabled*

DOI integration via DataCite
### Doi
- Api Mint
- Api Status
- Batch Mint
- Browse
- Configure
- Config Save
- Config Test
- Deactivate
- Export
- View
- Mint
- Queue
- Queue Retry
- Reactivate
- Report
- Resolve
- Sync
- Update
- Verify
- View
### CLI Commands
- `php symfony doi:deactivate` - Deactivate DOIs (create tombstones)
- `php symfony doi:mint` - Mint DOIs for records via DataCite
- `php symfony doi:process-queue` - Process the DOI minting queue
- `php symfony doi:sync` - Sync DOI metadata with DataCite
- `php symfony doi:verify` - Verify DOIs resolve correctly

## Donor Agreement (ahgDonorAgreementPlugin)
*Category: ahg - enabled*

Comprehensive donor/institution agreement management with contract uploads, rights, restrictions, reminders, and South African compliance.
### Donor
- Autocomplete
### DonorAgreement
- Add
- Autocomplete Accessions
- Autocomplete Records
- Browse
- Dashboard
- Delete
- Create / edit
- Reminders
- View

## Donor Manage (ahgDonorManagePlugin)
*Category: browse - enabled, locked*

Donor browse and management
### DonorManage
- Browse (`/donor/browse`)
- Delete (`/donor/:slug/delete`)
- Create / edit (`/donor/add`)
- View (`/donor/:slug`)

## Email Delivery (ahgEmailDeliveryPlugin)
*Category: communication - enabled*

Email bounce capture + suppression list + send-time gate
### EmailDelivery
- Add (`/admin/email/suppressions/add`)
- Bounce (`/email/bounce`)
- Delete (`/admin/email/suppressions/remove`)
- Suppressions (`/admin/email/suppressions`)

## Exhibition (ahgExhibitionPlugin)
*Category: ahg - enabled*

Exhibition management for GLAM/DAM sectors
### ExhibitionSpace
- Analytics (`/exhibition-space/:slug/analytics`)
- Browse (`/exhibition-space/browse`)
- Builder (`/exhibition-space/:slug/builder`)
- Builder Display Case (`/exhibition-space/:slug/builder/display-case`)
- Builder On Floor (`/exhibition-space/:slug/builder/on-floor`)
- Builder Place (`/exhibition-space/:slug/builder/place`)
- Builder Placements (`/exhibition-space/:slug/builder/placements`)
- Builder Remove (`/exhibition-space/:slug/builder/remove`)
- Builder Size (`/exhibition-space/:slug/builder/size`)
- Builder Spotlight (`/exhibition-space/:slug/builder/spotlight`)
- Builder Tilt (`/exhibition-space/:slug/builder/tilt`)
- Builder View (`/exhibition-space/:slug/builder/view`)
- Builder Wall (`/exhibition-space/:slug/builder/wall`)
- Builder ZOrder (`/exhibition-space/:slug/builder/z-order`)
- Confirm Delete (`/exhibition-space/:slug/delete`)
- Create (`/exhibition-space/add`)
- Destroy (`/exhibition-space/:slug/destroy`)
- Create / edit (`/exhibition-space/:slug/edit`)
- Forecast (`/exhibition-space/:slug/forecast`)
- Generate (`/exhibition-space/generate`)
- Generate Build (`/exhibition-space/generate/build`)
- Generate Suggest (`/exhibition-space/generate/suggest`)
- Place (`/exhibition-space/:slug/place`)
- Plan (`/exhibition-space/:slug/plan`)
- Plan Add Room (`/exhibition-space/:slug/plan/add-room`)
- Plan Corridor Add (`/exhibition-space/:slug/plan/corridor-add`)
- Plan Corridor Move (`/exhibition-space/:slug/plan/corridor-move`)
- Plan Corridor Remove (`/exhibition-space/:slug/plan/corridor-remove`)
- Plan Delete Room (`/exhibition-space/:slug/plan/delete-room`)
- Plan Doors (`/exhibition-space/:slug/plan/doors`)
- Plan Group (`/exhibition-space/:slug/plan/group`)
- Plan Image (`/exhibition-space/:slug/plan/image`)
- Plan Image Clear (`/exhibition-space/:slug/plan/image-clear`)
- Plan Image Rect (`/exhibition-space/:slug/plan/image-rect`)
- Plan Room Floor (`/exhibition-space/:slug/plan/room-floor`)
- Plan Room Lock (`/exhibition-space/:slug/plan/room-lock`)
- Plan Save (`/exhibition-space/:slug/plan/save`)
- Plan Shape (`/exhibition-space/:slug/plan/shape`)
- Plan Stairs (`/exhibition-space/:slug/plan/stairs`)
- Plan Walls (`/exhibition-space/:slug/plan/walls`)
- Plan Windows (`/exhibition-space/:slug/plan/windows`)
- Record Readings (`/exhibition-space/:slug/readings`)
- Remove Placement (`/exhibition-space/placement/:id/remove`)
- Room Dims (`/exhibition-space/:slug/room-dims`)
- Save Layout (`/exhibition-space/:slug/builder/layout`)
- Save Room (`/exhibition-space/:slug/save-room`)
- Sensor Regen (`/exhibition-space/:slug/sensor/regenerate`)
- View (`/exhibition-space/:slug`)
- Simulate Readings (`/exhibition-space/:slug/readings/simulate`)
- Walkthrough (`/exhibition-space/:slug/walkthrough`)
### CLI Commands
- `php symfony museum:exhibition` - Manage museum exhibitions

## Export (ahgExportPlugin)
*Category: ahg - enabled*

Archival export functionality for CSV, EAD, and other formats
### Export
- Accession Csv
- Archival
- Authority
- Csv
- Ead
- View
- Repository

## Extended Rights (ahgExtendedRightsPlugin)
*Category: ahg - enabled*

Extended rights management with RightsStatements.org integration, embargo management, Traditional Knowledge labels, and batch rights assignment
### Embargo
- Add
- Add Exception
- Create / edit
- View
- Lift
- View
### ExtendedRights
- Batch
- Browse
- Clear
- Dashboard
- Create / edit
- Embargo Blocked
- Embargo Status
- Embargoes
- Expiring Embargoes
- Export
- View
- Lift Embargo
### CLI Commands
- `php symfony embargo:process` - Process embargo expiry: auto-lift and send notifications
- `php symfony embargo:report` - Generate embargo reports

## Favorites (ahgFavoritesPlugin)
*Category: ahg - enabled*

User favorites/bookmarks management
### Favorites
- Add
- Ajax Folders
- Ajax Search
- Ajax Status
- Ajax Toggle
- Ajax Toggle Custom
- Browse
- Bulk
- Clear
- Export
- Export Folder
- Folder Create
- Folder Delete
- Folder Edit
- Folder View
- Import
- Move To Folder
- Delete
- Revoke Sharing
- Send To Bibliography
- Send To Collection
- Send To Project
- Share Folder
- Update Notes
- View Shared

## Federation (ahgFederationPlugin)
*Category: integration - enabled*

OAI-PMH Federation for metadata exchange
### Federation
- Add Peer
- Edit Peer
- Harvest
- Harvest Status
- View
- Log
- Peers
- Run Harvest
- Test Peer
- Union

## Feedback (ahgFeedbackPlugin)
*Category: ahg - enabled*

User feedback and suggestions management
### Feedback
- Browse (`/feedback`)
- Delete (`/feedback/:id/delete`)
- Create / edit (`/feedback/:id/edit`)
- General (`/feedback/general`)
- Submit (`/informationobject/:slug/feedback`)
- View (`/feedback/:id`)

## Forms (ahgFormsPlugin)
*Category: ahg - enabled*

Configurable metadata entry forms per repository
### Forms
- Api Autosave
- Api Get Form
- Api Reorder Fields
- Api Save Fields
- Assignment Create
- Assignment Delete
- Assignments
- Browse
- Builder
- Field Add
- Field Delete
- Field Get
- Field Reorder
- Field Update
- View
- Library
- Library Install
- Preview
- Render Edit
- Render New
- Submit
- Template Clone
- Template Create
- Template Delete
- Template Edit
- Template Export
- Template Import
- Templates
### CLI Commands
- `php symfony forms:export` - Export a form template to JSON
- `php symfony forms:import` - Import a form template from JSON
- `php symfony forms:list` - List form templates

## FTP (ahgFtpPlugin)
*Category: import - enabled*

Browser-based FTP/SFTP upload for CSV import digital objects
### FtpUpload
- Clear All
- Delete File
- Import As Upload
- View
- List Files
- Upload
- Upload Chunk

## Function Manage (ahgFunctionManagePlugin)
*Category: manage - enabled*

ISDF function browse and management
### FunctionManage
- Browse (`/function/browse`)
- Delete (`/function/:slug/delete`)
- Create / edit (`/function/add`)
- View (`/function/:slug`)

## Functions Docs (ahgFunctionsDocsPlugin)
*Category: admin - enabled*

Browsable catalogue of routes, CLI tasks and services
### FunctionsDocs
- Catalogue (`/admin/docs/catalogue`)

## GIS (ahgGISPlugin)
*Category: search - enabled*

Geospatial search and GeoJSON export for heritage records
### Gis
- Bbox
- Geojson
- Radius

## Gallery (ahgGalleryPlugin)
*Category: ahg - enabled*

Gallery and exhibition management with artist tracking, loans, insurance, and facility reports
### Gallery
- Add
- Add Exhibition Object
- Artists
- Browse
- Create Artist
- Create Exhibition
- Create Loan
- Create Valuation
- Create Venue
- Dashboard
- Create / edit
- Exhibitions
- Facility Report
- View
- Loans
- Valuations
- Venues
- View Artist
- View Exhibition
- View Loan
- View Venue
### GalleryReports
- Artists
- Exhibitions
- Export Csv
- Facility Reports
- View
- Loans
- Spaces
- Valuations

## GraphQL (ahgGraphQLPlugin)
*Category: integration - enabled*

GraphQL API endpoint providing flexible querying with security safeguards
### Graphql
- View
- Playground

## Help (ahgHelpPlugin)
*Category: admin - enabled*

Online help system with searchable documentation and contextual help
### Help
- Api Chat
- Api Context Map
- Api Search
- Api Search Index
- Api System Map
- Article
- Category
- View
- Search
- System Map
### CLI Commands
- `php symfony help:import` - Import markdown docs into the help system
- `php symfony help:rebuild-index` - Rebuild help article text index and sections from stored markdown

## Heritage Accounting (ahgHeritageAccountingPlugin)
*Category: ahg - enabled*
### GrapCompliance
- Batch Check
- Check
- Dashboard
- National Treasury Report
### HeritageAccounting
- Add
- Add Impairment
- Add Journal
- Add Movement
- Add Valuation
- Browse
- Dashboard
- Create / edit
- Edit By Object
- Configure
- View
- View By Object
### HeritageAdmin
- View
- Region Info
- Region Install
- Region Set Active
- Region Uninstall
- Regions
- Rule Add
- Rule Delete
- Rule Edit
- Rule List
- Rule Toggle
- Standard Add
- Standard Delete
- Standard Edit
- Standard List
- Standard Toggle
### HeritageApi
- Actor Autocomplete
- Asset
- Autocomplete
- Summary
### HeritageReport
- Asset Register
- View
- Movement
- Valuation
### CLI Commands
- `php symfony heritage:install` - Install heritage accounting database schema
- `php symfony heritage:region` - Manage heritage accounting regions

## Heritage (ahgHeritagePlugin)
*Category: ahg - enabled*

Heritage discovery platform with contributor system, custodian management, and analytics
### Heritage
- Admin Access Requests (`/heritage/admin/access-requests`)
- Admin Branding (`/heritage/admin/branding`)
- Admin Config (`/heritage/admin/config`)
- Admin Dashboard (`/heritage/admin`)
- Admin Embargoes (`/heritage/admin/embargoes`)
- Admin Featured Collections (`/heritage/admin/featured-collections`)
- Admin Features (`/heritage/admin/features`)
- Admin Hero Slides (`/heritage/admin/hero-slides`)
- Admin Popia (`/heritage/admin/popia`)
- Admin Users (`/heritage/admin/users`)
- Analytics Alerts (`/heritage/analytics/alerts`)
- Analytics Content (`/heritage/analytics/content`)
- Analytics Dashboard (`/heritage/analytics`)
- Analytics Search (`/heritage/analytics/search`)
- Api Analytics (`/heritage/api/analytics`)
- Api Autocomplete (`/heritage/api/autocomplete`)
- Api Click (`/heritage/api/click`)
- Api Contribution Status (`/heritage/api/contribution/:id`)
- Api Discover (`/heritage/api/discover`)
- Api Dwell (`/heritage/api/dwell`)
- Api Entity (`/heritage/api/entity/:type/:value`)
- Api Entity Related (`/heritage/api/entity/:id/related`)
- Api Entity Search (`/heritage/api/entity/search`)
- Api Explore Categories (`/heritage/api/explore-categories`)
- Api Explore Category Items (`/heritage/api/explore/:category/items`)
- Api Featured Collections (`/heritage/api/featured-collections`)
- Api Graph Stats (`/heritage/api/graph/stats`)
- Api Hero Slides (`/heritage/api/hero-slides`)
- Api Landing (`/heritage/api/landing`)
- Api Submit Contribution (`/heritage/api/contribution/submit`)
- Api Suggest Tags (`/heritage/api/suggest-tags`)
- Api Timeline Period Items (`/heritage/api/timeline/:period_id/items`)
- Api Timeline Periods (`/heritage/api/timeline-periods`)
- Collections (`/heritage/collection/:id`)
- Contribute (`/heritage/contribute/:slug`)
- Contributor Login (`/heritage/login`)
- Contributor Logout (`/heritage/logout`)
- Contributor Profile (`/heritage/contributor/:id`)
- Contributor Register (`/heritage/register`)
- Contributor Verify (`/heritage/verify/:token`)
- Creators (`/heritage/creators`)
- Creators Autocomplete (`/heritage/creators/autocomplete`)
- Custodian Batch (`/heritage/custodian/batch`)
- Custodian Dashboard (`/heritage/custodian`)
- Custodian History (`/heritage/custodian/history`)
- Custodian Item (`/heritage/custodian/:slug`)
- Entity (`/heritage/entity/:type/:value`)
- Explore (`/heritage/explore/:category`)
- Graph (`/heritage/graph`)
- Graph Data (`/heritage/graph/data`)
- Landing (`/heritage/index`)
- Leaderboard (`/heritage/leaderboard`)
- My Access Requests (`/heritage/my/access-requests`)
- My Contributions (`/heritage/my/contributions`)
- Request Access (`/heritage/access/request/:slug`)
- Review Contribution (`/heritage/review/:id`)
- Review Queue (`/heritage/review`)
- Search (`/heritage/search`)
- Timeline (`/heritage/timeline/:period_id`)
- Trending (`/heritage/trending`)
### CLI Commands
- `php symfony heritage:build-graph` - Build entity relationship graph from entity cache

## ICIP (ahgICIPPlugin)
*Category: ahg - enabled*

Indigenous Cultural and Intellectual Property management
### Icip
- Acknowledge (`/icip/acknowledge/:notice_id`)
- Api Check Access (`/icip/api/check-access/:object_id`)
- Api Summary (`/icip/api/summary/:object_id`)
- Communities (`/icip/communities`)
- Community Delete (`/icip/community/:id/delete`)
- Community Edit (`/icip/community/:id/edit`)
- Community View (`/icip/community/:id`)
- Consent Edit (`/icip/consent/:id/edit`)
- Consent List (`/icip/consent`)
- Consent View (`/icip/consent/:id`)
- Consultation Edit (`/icip/consultation/:id/edit`)
- Consultation View (`/icip/consultation/:id`)
- Consultations (`/icip/consultations`)
- Dashboard (`/icip`)
- Notice Types (`/icip/notice-types`)
- Notices (`/icip/notices`)
- Object Consent (`/object/:slug/icip/consent`)
- Object Consultations (`/object/:slug/icip/consultations`)
- Object Icip (`/object/:slug/icip`)
- Object Labels (`/object/:slug/icip/labels`)
- Object Notices (`/object/:slug/icip/notices`)
- Object Restrictions (`/object/:slug/icip/restrictions`)
- Report Community (`/icip/reports/community/:id`)
- Report Expiry (`/icip/reports/consent-expiry`)
- Report Pending (`/icip/reports/pending-consultation`)
- Reports (`/icip/reports`)
- Restrictions (`/icip/restrictions`)
- Tk Labels (`/icip/tk-labels`)

## IPSAS (ahgIPSASPlugin)
*Category: ahg - enabled*

IPSAS Heritage Asset Management - International public sector accounting for heritage assets
### Ipsas
- Asset Create
- Asset Edit
- Asset View
- Assets
- Configure
- Financial Year
- Impairments
- View
- Insurance
- Reports
- Valuation Create
- Valuations
### CLI Commands
- `php symfony ipsas:report` - Generate IPSAS heritage asset reports

## IIIF (ahgIiifPlugin)
*Category: ahg - enabled*

IIIF plugin for manifests, viewer, and collections
### Iiif
- Autocomplete (`/iiif/v3/manifest/:slug/autocomplete`)
- Search (`/iiif/v3/manifest/:slug/search`)
### CLI Commands
- `php symfony iiif:ai-extract` - Region-scoped VLM extraction over IIIF canvases (#220)

## Image Ar (ahgImageArPlugin)
*Category: advanced_features - enabled*

Place a flat 2D image into augmented reality (WebXR)
### ImageAr
- View (`/imagear`)

## Information Object Manage (ahgInformationObjectManagePlugin)
*Category: manage - enabled*

ISAD(G) information object CRUD management
### IoManage
- Actor Autocomplete (`/informationobject/actorAutocomplete`)
- Delete (`/informationobject/:slug/delete`)
- Do Delete (`/digitalobject/:id/delete`)
- Do Edit (`/digitalobject/:id/edit`)
- Do Upload (`/digitalobject/attach/file`)
- Create / edit (`/informationobject/add`)
- Generate Identifier (`/informationobject/generateIdentifierJson`)
- Repository Autocomplete (`/informationobject/repositoryAutocomplete`)
- Term Autocomplete (`/informationobject/termAutocomplete`)

## Ingest (ahgIngestPlugin)
*Category: ingestion - enabled*

OAIS-aligned multi-stage ingestion pipeline
### Ingest
- Auto Map
- Browse Share Point
- Cancel
- Commit
- Configure
- Download Manifest
- Download Template
- Extract Metadata
- Import From Share Point
- View
- Job Status
- Map
- Preview
- Preview Tree
- Rollback
- Search Parent
- Set Watch Folder
- Upload
- Validate
### CLI Commands
- `php symfony ingest:commit` - Process ingest commit job in background
- `php symfony ingest:rollback` - Roll back an ingest job (delete the records + digital objects it created)
- `php symfony ingest:watch` - Auto-ingest new files dropped in watched (hot) folders

## Integrity (ahgIntegrityPlugin)
*Category: preservation - enabled*

Enterprise-grade automated integrity assurance: scheduled fixity verification, append-only ledger, dead-letter queue
### Integrity
- Alerts
- Api Alert Delete
- Api Alert Save
- Api Daily Trend
- Api Dead Letter Action
- Api Disposition Action
- Api Format Breakdown
- Api Hold Place
- Api Hold Release
- Api Holds
- Api Ledger
- Api Policies
- Api Policy Delete
- Api Policy Toggle
- Api Repo Breakdown
- Api Retention Scan
- Api Run
- Api Run Schedule
- Api Runs
- Api Schedule Delete
- Api Schedule Toggle
- Api Stats
- Api Storage Growth
- Api Throughput
- Api Verify
- Dead Letter
- Disposition
- Export
- Export Auditor
- Export Csv
- Holds
- View
- Ledger
- Policies
- Policy Edit
- Records
- Report
- Run Detail
- Runs
- Schedule Edit
- Schedules
### CLI Commands
- `php symfony integrity:report` - Generate integrity verification reports
- `php symfony integrity:retention` - Manage retention policies, legal holds, and disposition queue
- `php symfony integrity:schedule` - Manage integrity verification schedules
- `php symfony integrity:verify` - Run fixity verification on digital objects

## Jobs Manage (ahgJobsManagePlugin)
*Category: admin - available (not enabled)*

Background jobs browse and management
### JobsManage
- Browse
- Delete
- Export
- Queue Batches
- Queue Browse
- Queue Cancel
- Queue Detail
- Queue Progress
- Queue Retry
- Report

## Label (ahgLabelPlugin)
*Category: ahg - enabled*

Label generation for archival objects with customizable templates
### Label
- Batch
- View
- Template Edit
- Templates

## Landing Page (ahgLandingPagePlugin)
*Category: ahg - enabled*

Visual landing page builder with drag-and-drop blocks
### LandingPageBuilder
- Add Block
- Create
- Delete
- Delete Block
- Duplicate Block
- Create / edit
- Get Block Config
- View
- List
- Move To Column
- My Dashboard
- My Dashboard Create
- My Dashboard Edit
- My Dashboard List
- Preview
- Publish
- Reorder Blocks
- Reorder Column Blocks
- Restore Version
- Save Draft
- Toggle Visibility
- Update Block
- Update Settings

## Library (ahgLibraryPlugin)
*Category: ahg - enabled*

Library cataloging with MARC-inspired fields, ISBN lookup, and bibliographic management
### Sushi
- Counter5 (`/sushi/counter5`)
### CLI Commands
- `php symfony library:backfill-authors` - Upsert an Authority Record (actor) for every library_item_creator row whose actor_id is NULL and link them.
- `php symfony library:backfill-subjects` - Mirror library_item_subject rows into AtoM Subject taxonomy (term + object_term_relation).
- `php symfony library:email-usage-reports` - Email the prior period\
- `php symfony library:frbr-backfill` - Compute and store FRBR work keys for all library items
- `php symfony library:frbr-reindex` - Re-generate frbr_work_key for all library items (full re-index)
- `php symfony library:hold-expiry` - Expire unfulfilled holds past their expiry date
- `php symfony library:ill-overdue` - Check for overdue interlibrary loan items
- `php symfony library:overdue-check` - Check for overdue checkouts and optionally notify patrons
- `php symfony library:patron-expiry` - Flag patrons with expired memberships
- `php symfony library:process-covers` - Process pending book cover downloads from Open Library
- `php symfony library:process-fines` - Process daily overdue fines for active checkouts past due date
- `php symfony library:serial-expected` - Generate expected serial issues based on subscription frequency
- `php symfony library:serial-renewal-reminders` - Email staff the subscriptions due for renewal

## Loan (ahgLoanPlugin)
*Category: ahg - enabled*

Shared loan management for GLAM institutions
### Loan
- Add
- Add Object
- Agreement
- Create / edit
- Extend
- View
- Remove Object
- Return
- Search Objects
- View
- Transition
- Upload Document

## Marketplace (ahgMarketplacePlugin)
*Category: ecommerce - enabled*

Online marketplace for buying and selling across all GLAM sectors
### Marketplace
- Admin Categories
- Admin Currencies
- Admin Dashboard
- Admin Listing Review
- Admin Listings
- Admin Payouts
- Admin Payouts Batch
- Admin Reports
- Admin Reviews
- Admin Seller Verify
- Admin Sellers
- Admin Settings
- Admin Transactions
- Api Auction Status
- Api Bid
- Api Categories
- Api Currencies
- Api Favourite
- Api Search
- Auction Browse
- Bid Form
- Browse
- Buy
- Category
- Collection
- Dashboard
- Enquiry Form
- Featured
- Follow
- Listing
- My Bids
- My Following
- My Offers
- My Purchases
- Offer Form
- Review Form
- Search
- Sector
- Seller
- Seller Analytics
- Seller Collection Create
- Seller Collections
- Seller Enquiries
- Seller Listing Create
- Seller Listing Edit
- Seller Listing Images
- Seller Listing Publish
- Seller Listing Withdraw
- Seller Listings
- Seller Offer Respond
- Seller Offers
- Seller Payouts
- Seller Profile
- Seller Register
- Seller Reviews
- Seller Transaction Detail
- Seller Transactions

## Menu Manage (ahgMenuManagePlugin)
*Category: admin - enabled*

Menu configuration management
### MenuManage
- Delete
- Create / edit
- List

## Metadata Export (ahgMetadataExportPlugin)
*Category: export - enabled*

GLAM Metadata Export Framework
### LinkedData
- Actor
- Dcat
- Feed
- Negotiate
- Record
- Repository
- Sitemap
- Void
### MetadataExport
- Bulk
- Download
- View
- Preview
### CLI Commands
- `php symfony c2pa:sign` - Generate, sign, store and verify C2PA content credentials
- `php symfony metadata:export` - Export archival descriptions to various metadata standards

## Metadata Extraction (ahgMetadataExtractionPlugin)
*Category: preservation - available (not enabled)*

Universal metadata extraction from digital objects
### MetadataExtraction
- Batch Extract (`/metadataExtraction/batchExtract`)
- Delete (`/metadataExtraction/delete`)
- Extract (`/metadataExtraction/extract`)
- View (`/metadataExtraction`)
- Status (`/metadataExtraction/status`)
- View (`/metadataExtraction/view/:id`)

## MODS Manage (ahgModsManagePlugin)
*Category: descriptive-standard - enabled*

MODS information object CRUD management
### ModsManage
- Create / edit

## Multi Tenant (ahgMultiTenantPlugin)
*Category: ahg - available (not enabled)*

Repository-based multi-tenancy with user hierarchy (Admin > Super User > User)
### TenantSwitcher
- Get Switcher (`/tenant/switcher`)

## Museum (ahgMuseumPlugin)
*Category: ahg - enabled*

Museum cataloging with CCO (Cataloging Cultural Objects), CIDOC-CRM, and Spectrum 5.0 integration
### Authority
- Link
### Cco
- Add
- Browse
- Delete
- Create / edit
- View
- Object Comparison
- Provenance
- Provenance Delete
- Provenance Export
- Provenance Get
- Provenance Save
### Cidoc
- Export
### Dashboard
- View
- Missing Field
### Museum
- Add
- Dashboard
- Delete
- Create / edit
- Getty Autocomplete
- View
- Provenance
- Vocabulary
### MuseumApi
- Authority Record
- Authority Search
- Getty Autocomplete
- Getty Links
- Spectrum Update Procedure
- Vocabulary Search
### MuseumReports
- Condition Report
- Creators
- Export Csv
- View
- Materials
- Objects
- Provenance
- Style Period
### CLI Commands
- `php symfony museum:aat-sync` - Sync Getty AAT vocabulary terms to local cache for fast autocomplete
- `php symfony museum:getty-link` - Link taxonomy terms to Getty vocabularies (AAT, TGN, ULAN)
- `php symfony museum:migrate` - Run museum metadata database migrations

## NARSSA (ahgNARSSAPlugin)
*Category: compliance - enabled*

NARSSA transfer manifest generator
### CLI Commands
- `php symfony narssa:transfer-package` - Build a NARSSA-compliant transfer package (METS + EAD2002 + files)

## NAZ (ahgNAZPlugin)
*Category: ahg - enabled*

National Archives of Zimbabwe Act [Chapter 25:06] compliance - 25-year rule
### Naz
- Closure Create
- Closure Edit
- Closures
- Configure
- View
- Permit Create
- Permit View
- Permits
- Protected Records
- Reports
- Researcher Create
- Researcher Edit
- Researcher View
- Researchers
- Schedule Create
- Schedule View
- Schedules
- Transfer Create
- Transfer View
- Transfers
### CLI Commands
- `php symfony naz:closure-check` - Check closure periods for expiry and releases
- `php symfony naz:permit-expiry` - Check research permits for expiry
- `php symfony naz:report` - Generate NAZ compliance reports
- `php symfony naz:transfer-due` - List pending and overdue records transfers

## NMMZ (ahgNMMZPlugin)
*Category: ahg - enabled*

National Museums and Monuments of Zimbabwe Act [Chapter 25:11] - heritage protection
### Nmmz
- Antiquities
- Antiquity Create
- Antiquity View
- Configure
- Hia
- Hia Create
- View
- Monument Create
- Monument View
- Monuments
- Permit Create
- Permit View
- Permits
- Reports
- Site Create
- Site View
- Sites
### CLI Commands
- `php symfony nmmz:report` - Generate NMMZ heritage reports

## Observability (ahgObservabilityPlugin)
*Category: integration - enabled*

## Ocfl (ahgOcflPlugin)
*Category: preservation - enabled*
### Ocfl
- Api Export
- Api Ingest
- Api Init
- Api Verify
- Api Verify All
- View

## Portable Export (ahgPortableExportPlugin)
*Category: export - enabled*

Standalone portable catalogue viewer for CD/USB/ZIP distribution
### PortableExport
- Api Clipboard Export
- Api Delete
- Api Estimate
- Api File
- Api Fonds Search
- Api Import List
- Api Import Progress
- Api Import Validate
- Api List
- Api Manifest
- Api Progress
- Api Quick Start
- Api Start Export
- Api Start Import
- Api Token
- Download
- Import
- View
### CLI Commands
- `php symfony portable:cleanup` - Delete expired portable exports and their files
- `php symfony portable:export` - Generate a portable standalone catalogue viewer
- `php symfony portable:import` - Import an AtoM Heratio archive package
- `php symfony portable:verify` - Verify integrity of a portable archive export package

## Preservation (ahgPreservationPlugin)
*Category: ahg - enabled*

Digital preservation: checksums, fixity verification, PREMIS events, format registry
### Preservation
- Api Convert
- Api Generate Checksum
- Api Identify
- Api Package Add Object
- Api Package Build
- Api Package Convert
- Api Package Delete
- Api Package Export
- Api Package Remove Object
- Api Package Validate
- Api Schedule Delete
- Api Schedule Run
- Api Schedule Toggle
- Api Stats
- Api Verify Backup
- Api Verify Fixity
- Api Virus Scan
- Backup
- Conversion
- Events
- Extended
- Fixity Log
- Formats
- Identification
- View
- Object
- Package Download
- Package Edit
- Package View
- Packages
- Packages By Slug
- Policies
- Reports
- Schedule Edit
- Schedule Run View
- Scheduler
- Virus Scan
### Tiffpdfmerge
- Attach Existing
- Browse
- Create
- Delete
- Download
- Get Job
- Import Folder
- View
- Process
- Ready To Link
- Recreate
- Remove File
- Reorder
- Upload
- View
### CLI Commands
- `php symfony ahg:tiff-combine-watch` - Watch a drop-folder and auto-queue TIFF->PDF/A combine jobs per record
- `php symfony ahg:tiff-pdf-process` - Process queued TIFF->PDF/A combine jobs (background worker)
- `php symfony preservation:convert` - Convert digital objects to preservation-safe formats
- `php symfony preservation:fixity` - Verify file integrity using checksums
- `php symfony preservation:identify` - Identify file formats using Siegfried (PRONOM)
- `php symfony preservation:migration` - Format migration planning and obsolescence reporting
- `php symfony preservation:package` - Manage OAIS preservation packages
- `php symfony preservation:pronom-sync` - Sync format registry from PRONOM (UK National Archives)
- `php symfony preservation:replicate` - Replicate files to backup targets
- `php symfony preservation:scheduler` - Run scheduled preservation workflows
- `php symfony preservation:verify-backup` - Verify backup integrity and replication status
- `php symfony preservation:virus-scan` - Scan digital objects for viruses using ClamAV

## Privacy (ahgPrivacyPlugin)
*Category: ahg - enabled*

POPIA/GDPR Privacy Compliance Management
### Privacy
- Complaint
- Complaint Confirmation
- Dashboard
- Dsar Confirmation
- Dsar Request
- Dsar Status
- View
### PrivacyAdmin
- Add Manual Redaction
- Apply Visual Redactions
- Breach Add
- Breach Edit
- Breach List
- Breach Update
- Breach View
- Clear Pdf Cache
- Complaint Add
- Complaint Edit
- Complaint List
- Complaint Update
- Complaint View
- Configure
- Consent Add
- Consent Edit
- Consent List
- Consent View
- Consent Withdraw
- Delete Visual Redaction
- Download Pdf
- Download Redacted File
- Dpia Archive
- Dpia Form
- Dpia List
- Dpia Review
- Dpia Sign Off
- Dsar Add
- Dsar Edit
- Dsar List
- Dsar Scope
- Dsar Update
- Dsar View
- Embedded Pii
- Embedded Pii Resolve
- Export
- Get Document Info
- Get Ner Entities For Page
- Get Redacted Terms
- Get Visual Redactions
- View
- Jurisdiction Add
- Jurisdiction Delete
- Jurisdiction Edit
- Jurisdiction Info
- Jurisdiction Install
- Jurisdiction List
- Jurisdiction Set Active
- Jurisdiction Toggle
- Jurisdiction Uninstall
- Jurisdictions
- Notification Mark All Read
- Notification Read
- Notifications
- Officer Add
- Officer Edit
- Officer List
- Paia Add
- Paia List
- Pii Entity Action
- Pii Review
- Pii Scan
- Pii Scan Ajax
- Pii Scan Object
- Pii Scan Run
- Redaction Manage
- Remove Manual Redaction
- Report
- Ropa Add
- Ropa Approve
- Ropa Edit
- Ropa List
- Ropa Reject
- Ropa Submit
- Ropa View
- Save Visual Redaction
- Visual Redaction Editor
### CLI Commands
- `php symfony privacy:breach-check` - Check breach notification deadlines (POPIA Section 22)
- `php symfony privacy:jurisdiction` - Manage privacy compliance jurisdictions
- `php symfony privacy:scan-embedded` - Scan embedded EXIF/IPTC metadata for PII (GPS, people, contacts)
- `php symfony privacy:scan-pii` - Scan archival descriptions for PII (Personally Identifiable Information)

## Provenance (ahgProvenancePlugin)
*Category: ahg - enabled*

Chain of custody and provenance tracking
### Provenance
- Add Event (`/provenance/addEvent`)
- Delete Document (`/provenance/deleteDocument/:id`)
- Delete Event (`/provenance/deleteEvent`)
- Create / edit (`/provenance/:slug/edit`)
- Export (`/provenance/:slug/export`)
- View (`/provenance`)
- Search Agents (`/provenance/searchAgents`)
- Timeline (`/provenance/:slug/timeline`)
- View (`/provenance/:slug`)
### CLI Commands
- `php symfony ai-provenance:keygen` - Generate the Ed25519 keypair that signs AI inference manifests
- `php symfony ai-provenance:replay` - Replay queued AI inference + override Fuseki writes
- `php symfony ai-provenance:verify` - Verify Ed25519 signatures on recorded AI inferences

## RAD Manage (ahgRadManagePlugin)
*Category: descriptive-standard - enabled*

RAD information object CRUD management
### RadManage
- Create / edit

## Rdm (ahgRdmPlugin)
*Category: research - enabled*
### Rdm
- Compliance
- Create
- Dashboard
- Deposit
- Disposition
- File Download
- View
- Landing
- Link Dmp
- Resolve Finding
- Scan
- View
- Unlink Dmp
### CLI Commands
- `php symfony rdm:demo` - Run the full POPIA RDM demo on synthetic data (deposit->scan->gate->DOI->landing).
- `php symfony rdm:scan` - Run the POPIA sensitivity scan for an RDM dataset in the background

## Records Manage (ahgRecordsManagePlugin)
*Category: general - on disk*
### RecordsManage
- Email Capture
- File Plan

## Registry (ahgRegistryPlugin)
*Category: community - enabled*

AtoM/Heratio Community Hub & Registry - Directory of institutions, vendors, software, user groups, discussions, blog, and sync API.
### Registry
- Admin Blog
- Admin Dashboard
- Admin Discussions
- Admin Dropdown Delete
- Admin Dropdown Edit
- Admin Dropdowns
- Admin Email
- Admin Erd
- Admin Erd Edit
- Admin Extension Delete
- Admin Extension Edit
- Admin Footer
- Admin Group Edit
- Admin Group Email
- Admin Group Members
- Admin Group Verify
- Admin Groups
- Admin Import
- Admin Institution Users
- Admin Institution Verify
- Admin Institutions
- Admin Newsletter Form
- Admin Newsletter Send
- Admin Newsletters
- Admin Reviews
- Admin Settings
- Admin Setup Guides
- Admin Software
- Admin Software Verify
- Admin Standard Edit
- Admin Standards
- Admin Subscribers
- Admin Sync
- Admin User Edit
- Admin User Manage
- Admin User Reset Password
- Admin Users
- Admin Vendor Verify
- Admin Vendors
- Api Directory
- Api Notification Dismiss Bar
- Api Notification Read
- Api Notifications
- Api Notifications Read All
- Api Software Latest
- Api Sync Heartbeat
- Api Sync Register
- Api Sync Status
- Api Sync Update
- Blog Edit
- Blog List
- Blog New
- Blog Reply
- Blog View
- Community
- Discussion List
- Discussion New
- Discussion Reply
- Discussion View
- Erd Browse
- Erd View
- Favorite Toggle
- Forgot Password
- Group Browse
- Group Create
- Group Edit
- Group Join
- Group Leave
- Group Members
- Group Members Manage
- Group Toggle Notifications
- Group View
- View
- Instance View
- Institution Browse
- Institution Edit
- Institution Register
- Institution View
- Login
- Logout
- Map
- My Blog
- My Favorites
- My Groups
- My Institution Claim
- My Institution Contact Add
- My Institution Contact Delete
- My Institution Contact Edit
- My Institution Contacts
- My Institution Dashboard
- My Institution Instance Add
- My Institution Instance Delete
- My Institution Instance Delink
- My Institution Instance Edit
- My Institution Instance Relink
- My Institution Instances
- My Institution Review
- My Institution Software
- My Institution Unlink
- My Institution Vendor Remove
- My Institution Vendors
- My Vendor Call Log
- My Vendor Call Log Add
- My Vendor Call Log Edit
- My Vendor Call Log View
- My Vendor Client Add
- My Vendor Clients
- My Vendor Contact Add
- My Vendor Contact Edit
- My Vendor Contacts
- My Vendor Dashboard
- My Vendor Software
- My Vendor Software Add
- My Vendor Software Edit
- My Vendor Software Release Add
- My Vendor Software Releases
- My Vendor Software Unlink
- My Vendor Software Upload
- Newsletter Browse
- Newsletter Subscribe
- Newsletter Unsubscribe
- Newsletter View
- Note Delete
- Note Pin
- Note Save
- Notifications
- Oauth Callback
- Oauth Start
- Register
- Reset Password
- Search
- Setup Guide Browse
- Setup Guide View
- Software Browse
- Software Component Add
- Software Component Delete
- Software Component Edit
- Software Components
- Software Link To Institution
- Software Releases
- Software View
- Standard Browse
- Standard Submit
- Standard View
- Standards Schema
- Vendor Browse
- Vendor Edit
- Vendor Register
- Vendor View

## Report Builder (ahgReportBuilderPlugin)
*Category: ahg - enabled*

Custom report builder with drag-drop designer, charts, scheduling, and export
### ReportBuilder
- Api Attachment Delete
- Api Attachment Upload
- Api Attachments
- Api Chart Data
- Api Columns
- Api Comment
- Api Data
- Api Delete
- Api Entity Search
- Api Link Delete
- Api Link Save
- Api Og Fetch
- Api Query Columns
- Api Query Execute
- Api Query Relationships
- Api Query Save
- Api Query Tables
- Api Query Validate
- Api Save
- Api Section Delete
- Api Section Reorder
- Api Section Save
- Api Share Create
- Api Share Deactivate
- Api Snapshot
- Api Status Change
- Api Template Apply
- Api Template Delete
- Api Template Save
- Api Version Create
- Api Version Restore
- Api Versions
- Api Widget Delete
- Api Widget Save
- Api Widgets
- Archive
- Clone Report
- Create
- Delete
- Delete Template
- Create / edit
- Edit Template
- Export
- History
- View
- Preview
- Preview Template
- Query
- Schedule
- Schedule Delete
- Shared View
- Templates
- View
- Widget

## Reports (ahgReportsPlugin)
*Category: ahg - enabled*

Central reporting dashboard for AtoM
### Reports
- Accessions
- Activity
- Authorities
- Descriptions
- Donors
- View
- Recent
- Report
- Report Accession
- Report Authority Record
- Report Donor
- Report Information Object
- Report Physical Storage
- Report Repository
- Report Select
- Report Spatial Analysis
- Report Taxomomy
- Report Updates
- Report User
- Repositories
- Storage
- Taxonomy

## Repository Manage (ahgRepositoryManagePlugin)
*Category: browse - enabled, locked*

High-performance archival institution browse and management
### RepositoryManage
- Browse (`/repository/browse`)
### SfIsdiahPlugin
- Delete (`/repository/:slug/delete`)
- Create / edit (`/repository/add`)
- View (`/repository/:slug`)

## Request To Publish (ahgRequestToPublishPlugin)
*Category: ahg - enabled*

Manage publication requests for archival images and digital objects
### RequestToPublish
- Browse
- Delete
- Create / edit
- Inbox
- Receipt
- Review
- Submit
### Requesttopublish
- Browse
- Edit Request To Publish
- Receipt

## Research (ahgResearchPlugin)
*Category: ahg - enabled*

Research support plugin with reading room booking, researcher registration, and workspace management
### Audit
- Export
- View
- Record
- User
- View
### Research
- Accept Invitation
- Accept Share
- Activities
- Add Assertion Evidence
- Add To Collection
- Admin Reset Password
- Admin Statistics
- Admin Types
- Analytics
- Annotation Studio
- Annotations
- Api Keys
- Approve Researcher
- Assertion Batch Review
- Assertion Conflicts
- Assertions
- Assign Seat
- Batch Checkout
- Batch Return
- Bibliographies
- Book
- Book Equipment
- Bookings
- Browse Assessments
- Build Offline Package
- Bulk Validate
- Check In
- Check Out
- Cite
- Cite Export
- Clipboard To Project
- Collab Comment
- Collab Comment Resolve
- Collab Join
- Collab Panel
- Collab Poll
- Collections
- Comment Api
- Compare Snapshots
- Compliance Dashboard
- Create Annotation V2
- Create Assertion
- Create Collection Ajax
- Create Extraction Job
- Create Odrl Policy
- Create Room
- Create Snapshot
- Cross Fonds Query
- Custody Chain
- Custody Checkin
- Custody Checkout
- Custody Confirm
- Custody Return Verify
- Dashboard
- Delete Odrl Policy
- Delete Snapshot
- Diff Search Results
- Dmp Edit
- Dmp Export
- Dmp View
- Dmps
- Document Templates
- Edit Document Template
- Edit Institution
- Edit Project
- Edit Report
- Edit Report Section
- Edit Researcher Type
- Edit Room
- Entity Resolution
- Equipment
- Equipment History
- Ethics Milestones
- Evaluate Access
- Evidence Viewer
- Export Annotations IIIF
- Export Bibliography
- Export Finding Aid
- Export Graph GEXF
- Export Graph ML
- Export Journal
- Export Notes
- Export Report
- External Access
- Extraction Jobs
- Find Entity Candidates
- Generate Finding Aid
- Hypotheses
- Iiif Rooms
- Import Annotations IIIF
- Import Bibliography
- View
- Institutions
- Invite Collaborator
- Journal
- Journal Entry
- Journal New
- Knowledge Graph
- Knowledge Graph Data
- Manage Clipboard Item
- Manage Milestone
- Map Builder
- Map Data
- Map Point Api
- Metadata Suggestions
- Mint Doi
- Mobile Home
- Network Graph
- Network Graph Data
- New Report
- New Reproduction
- Notebook Delete
- Notebook Promote
- Notebook Show
- Notebooks
- Notifications
- Notifications Api
- Odrl Policies
- Offline Data
- Offline Search
- Offline Sync
- Orcid
- Orcid Callback
- Orcid Clear Credentials
- Orcid Connect
- Orcid Credentials
- Orcid Disconnect
- Orcid Fetch Public
- Orcid Pull Profile
- Orcid Works
- Package Collection
- Package Project
- Password Reset
- Password Reset Request
- Print Call Slips
- Profile
- Project Collaborators
- Project Json Ld
- Projects
- Propose Entity Match
- Public Register
- Register
- Registration Complete
- Reject Researcher
- Remove Collaborator
- Renewal
- Reorder Report Sections
- Reports
- Reproducibility Pack
- Reproductions
- Request Assign
- Request Close
- Request Correspond
- Request Item Ajax
- Request Review
- Request Sla
- Request Triage
- Requests Dashboard
- Researcher View
- Researchers
- Resolve Entity Match
- Resolve Thumbnail
- Retrieval Queue
- Room Annotation Export
- Room Manifest
- Rooms
- Save Experience Level
- Save Source Assessment
- Saved Searches
- Search Entities
- Search Items
- Seat Map
- Seats
- Share Project
- Snapshot Search Results
- Snapshots
- Source Assessment
- Studio
- Studio Delete
- Studio Download
- Studio Generate
- Studio Show
- Submission Edit
- Submission Review
- Submission Review Queue
- Submissions
- Submit Review
- Sync Upload
- Target Journal Builder
- Target Journal Delete
- Target Journal Seed Dhet
- Target Journal Show
- Target Journal Suggest
- Target Journals
- Timeline Builder
- Timeline Data
- Timeline Event Api
- Trust Score
- Update Assertion Status
- Update Hypothesis
- Update Odrl Policy
- Update Room
- Upload Note Image
- Validate Result
- Validation Queue
- View Activity
- View Annotation V2
- View Assertion
- View Bibliography
- View Booking
- View Booking_OLD
- View Collection
- View Extraction Job
- View Hypothesis
- View Project
- View Report
- View Reproduction
- View Researcher
- View Room
- View Snapshot
- View Workspace
- Visualization Data
- Walk In
- Workspace
- Workspaces
### Researchapi
- Annotations
- Bibliographies
- Bookings
- Citation
- Collection
- Collections
- Export Bibliography
- Profile
- Projects
- Searches
- Stats
### Researchjournal
- Article
- Builder
- View
- View
### Training
- Builder
- Certificate
- Complete Module
- Destroy
- Destroy Enrolment
- Edit Assessment
- Edit Module
- Enrol
- View
- Learn
- Set Status
- View
- Store Module
- Submit Assessment
- Take Assessment
### CLI Commands
- `php symfony research:orcid-sync` - Sync linked researchers\

## Researcher (ahgResearcherPlugin)
*Category: research - enabled*

Researcher collection upload and approval workflow
### Researcher
- Add Item
- Api Autocomplete
- Api Delete File
- Api Upload
- Create From Collection
- Dashboard
- Delete Item
- Edit Item
- Edit Submission
- Import Exchange
- New Submission
- Publish
- Resubmit
- Submissions
- Submit
- View Submission

## Resource Sync (ahgResourceSyncPlugin)
*Category: integration - enabled*
### Resourcesync
- Capability List
- Change List
- Resource List
- Source Description

## RiC Explorer (ahgRicExplorerPlugin)
*Category: ahg - enabled*

Records in Context (RiC) visualization, exploration, and Fuseki triplestore integration
### RicDashboard
- Ajax Cleanup Orphans (`/admin/ric/ajax/cleanup-orphans`)
- Ajax Clear Queue Item (`/admin/ric/ajax/queue-item`)
- Ajax Integrity Check (`/admin/ric/ajax/integrity-check`)
- Ajax Resync (`/admin/ric/ajax/resync`)
- Ajax Stats (`/admin/ric/ajax/stats`)
- Ajax Update Orphan (`/admin/ric/ajax/update-orphan`)
- Configure (`/admin/ric/config`)
- View (`/admin/ric`)
- Logs (`/admin/ric/logs`)
- Orphans (`/admin/ric/orphans`)
- Queue (`/admin/ric/queue`)
- Sync Status (`/admin/ric/sync-status`)
### RicExplorer
- Autocomplete (`/ricExplorer/autocomplete`)
- Get Data (`/ricExplorer/getData`)
- Knowledge Graph (`/ricExplorer/knowledge-graph/:id`)
- Provenance Graph (`/ricExplorer/provenance/:id`)
### RicShacl
- Ajax Validate Entity (`/ricShacl/ajaxValidateEntity`)
- View (`/admin/ric/shacl`)
- Report (`/admin/ric/shacl/report/:id`)
- Run (`/admin/ric/shacl/run`)
### CLI Commands
- `php symfony ric:install-provenance-menu` - Add the Provenance graph nav link (idempotent)
- `php symfony ric:queue-process` - Sync AtoM records to Fuseki RiC triplestore
- `php symfony ric:shacl-validate` - Validate the RiC-O graph against RiC-O SHACL shapes

## Rights Holder Manage (ahgRightsHolderManagePlugin)
*Category: browse - enabled, locked*

Rights holder browse and management using Laravel Query Builder
### RightsHolderManage
- Browse (`/rightsholder/browse`)
- Delete (`/rightsholder/:slug/delete`)
- Create / edit (`/rightsholder/add`)
- View (`/rightsholder/:slug`)

## Rights (ahgRightsPlugin)
*Category: ahg - enabled*

Core rights management including PREMIS rights, Creative Commons, rights holders, and orphan works tracking
### Rights
- Add
- Api Check
- Api Embargo
- Delete
- Create / edit
- Edit Embargo
- View
- Orphan Work
- Release Embargo
- Tk Labels
### RightsAdmin
- Add Search Step
- Assign Tk Label
- Complete Orphan Search
- Embargo Edit
- Embargo Extend
- Embargo Lift
- Embargoes
- View
- Orphan Work Edit
- Orphan Works
- Process Expired
- Remove Tk Label
- Report
- Statements
- Tk Labels

## Scan (ahgScanPlugin)
*Category: ingestion - enabled*
### ScanManage
- Create
- Delete
- Create / edit
- History
- View
- Run
- Toggle
- Update

## Search (ahgSearchPlugin)
*Category: search - enabled*

Global search, autocomplete, description updates, and search/replace
### AhgSearch
- Autocomplete (`/search/autocomplete`)
- Description Updates (`/search/descriptionUpdates`)
- Global Replace (`/search/globalReplace`)
- View (`/search/index`)
### RicSemanticSearch
- View (`/search/semantic`)

## Security Clearance (ahgSecurityClearancePlugin)
*Category: ahg - enabled, core, locked*

Security classification, user clearance, embargo, watermarking and extended rights management
### AccessRequest
- Create Object Request (`/security/request/submit`)
### SecurityClearance
- Acl Group Edit (`/admin/security/acl-group/:id`)
- Acl Groups (`/admin/security/acl-groups`)
- Bulk Grant (`/security/clearance/bulk-grant`)
- Compartments (`/security/compartments`)
- Dashboard (`/security/dashboard`)
- Grant (`/security/clearance/grant`)
- View (`/security/clearances`)
- Report (`/security/report`)
- Revoke (`/security/clearance/:id/revoke`)
- Revoke Access (`/security/access/:id/revoke`)
- Security Compliance (`/admin/security/compliance`)
- User (`/security/clearance/user/:slug`)
- View (`/security/clearance/:id`)
### CLI Commands
- `php symfony security:audit-verify` - Verify the tamper-evident hash chain of the security access log
- `php symfony security:update-cache` - Update security classification cache for Cantaloupe watermarks
- `php symfony watermark:apply-derivatives` - Apply watermarks to derivative images

## Semantic Search (ahgSemanticSearchPlugin)
*Category: ahg - enabled*

Semantic search with thesaurus, WordNet/Wikidata sync, and vector embeddings
### SearchEnhancement
- Admin Templates (`/admin/search/templates`)
- Delete Saved Search (`/search/delete/:id`)
- History (`/search/history`)
- Run Saved Search (`/search/run/:id`)
- Run Template (`/search/template/:id`)
- Save Search (`/search/save`)
- Saved Searches (`/search/saved`)
### SemanticSearchAdmin
- Configure (`/admin/semantic-search/config`)
- View (`/admin/semantic-search`)
- Run Sync (`/semanticSearchAdmin/runSync`)
- Search Logs (`/admin/semantic-search/search-logs`)
- Sync Logs (`/admin/semantic-search/sync-logs`)
- Term Add (`/admin/semantic-search/term/add`)
- Term View (`/admin/semantic-search/term/:id`)
- Terms (`/admin/semantic-search/terms`)
- Test Expand (`/semanticSearchAdmin/testExpand`)
### CLI Commands
- `php symfony linked-data:sync` - Link entities to VIAF, Wikidata, and Getty authority sources

## Settings (ahgSettingsPlugin)
*Category: admin - enabled, core*

AHG Settings Management
### AhgDropdown
- Add Term
- Create
- Delete Taxonomy
- Delete Term
- Create / edit
- View
- Move Section
- Rename
- Reorder
- Set Default
- Update Term
### AhgSettings
- Ahg Dashboard
- Ahg Integration
- Ahg Settings
- Ai Services
- Auto Update
- Clipboard
- Cron Jobs
- Csv Validator
- Dam Tools
- Diacritics
- Digital Object Derivatives
- Dip Upload
- Email
- Email Test
- Error Log
- Export
- Finding Aid
- Ftp Test
- Fuseki Test
- Generate Identifier
- Global
- Icip Settings
- Identifier
- Import
- View
- Interface Label
- Inventory
- Language
- Ldap
- Ldap Test
- Level Choices
- Levels
- Markdown
- Numbering Scheme Edit
- Numbering Schemes
- Oai
- Page Elements
- Permissions
- Plugins
- Preservation
- Privacy Notification
- Reset
- Save Tiff Pdf Settings
- Section
- Sector Numbering
- Security
- Services
- Settings Action
- Site Information
- System Info
- Template
- Treeview
- Tts
- Uploads
- Validate Identifier
- Visible Elements
- Webhooks

## Share Point (ahgSharePointPlugin)
*Category: integration - enabled*
### Sharepoint
- Columns
- Drive Browse
- Drive Delete
- Drive Register
- Drive Save
- Drives
- Event Detail
- Events
- Federated Search
- View
- Mapping
- Mapping Template Delete
- Mappings
- Mappings Save
- Push
- Push Job
- Push Projection
- Rule Delete
- Rule Edit
- Rule Run
- Rule Save
- Rules
- Subscriptions
- Tenant Edit
- Tenant Test
- Tenants
- User Mapping Edit
- User Mappings
- Webhook
### CLI Commands
- `php symfony sharepoint:auto-ingest` - Cron-driven SharePoint→AtoM ingest
- `php symfony sharepoint:ingest-event` - Process one inbound SharePoint webhook event
- `php symfony sharepoint:install` - Install ahgSharePointPlugin schema (idempotent)
- `php symfony sharepoint:post-ingest-hooks` - Run compliance hooks (sp_xref + version baseline + classification + AIP + PII) on IOs from a given ingest job
- `php symfony sharepoint:renew-subscriptions` - Renew Graph webhook subscriptions expiring within 12h
- `php symfony sharepoint:status` - Print SharePoint integration health (tenants, drives, subs, queue depth)
- `php symfony sharepoint:subscribe` - Create Graph webhook subscriptions (driveItem + list) for a drive
- `php symfony sharepoint:sync` - Delta-poll one or all ingest-enabled SharePoint drives
- `php symfony sharepoint:test-connection` - Test Microsoft Graph connectivity for a configured tenant

## Spectrum (ahgSpectrumPlugin)
*Category: ahg - enabled*

Spectrum 5.0 museum procedures - acquisition, loans, movement, conservation, valuation, and workflow management
### Spectrum
- Annotation Get
- Annotation Save
- Condition Admin
- Condition Photos
- Condition Report
- Condition Risk
- Dashboard
- Data Quality
- Export
- General
- General Workflow
- General Workflow Transition
- Grap Dashboard
- Grap Spectrum Link
- View
- Install
- Label
- Loan Dashboard
- My Tasks
- Photo Delete
- Photo Rotate
- Photo Set Primary
- Privacy Admin
- Privacy Breach Update
- Privacy Breaches
- Privacy Compliance
- Privacy Dsar
- Privacy Dsar Update
- Privacy Ropa
- Privacy Template Delete
- Privacy Template Download
- Privacy Templates
- Provenance Ajax
- Security Compliance
- Workflow
- Workflow Steps
- Workflow Steps Mode
- Workflow Transition
- Workflow Update
### SpectrumApi
- Event Api
- Statistics Api
### SpectrumReports
- Acquisitions
- Conditions
- Conservation
- View
- Loans
- Movements
- Object Entry
- Valuations

## Static Page (ahgStaticPagePlugin)
*Category: admin - enabled*

Static page management
### StaticPageManage
- Delete
- Create / edit
- List

## Statistics (ahgStatisticsPlugin)
*Category: ahg - enabled*

Usage statistics tracking
### Statistics
- Administer
- Api Chart
- Api Summary
- Bots
- Dashboard
- Downloads
- Export
- Geographic
- Item
- Pixel
- Repository
- Top Items
- Views
### CLI Commands
- `php symfony statistics:aggregate` - Aggregate usage statistics for reporting
- `php symfony statistics:report` - Generate statistics reports

## Storage Manage (ahgStorageManagePlugin)
*Category: browse - enabled, locked*

Physical storage browse and management
### StorageManage
- Autocomplete (`/physicalobject/autocomplete`)
- Box List (`/physicalobject/boxList`)
- Browse (`/physicalobject/browse`)
- Holdings Report Export (`/physicalobject/holdingsReportExport`)
### Strongroom
- Assign (`/strongroom/:slug/assign`)
- Browse (`/strongroom/browse`)
- Create (`/strongroom/add`)
- Delete (`/strongroom/:slug/delete`)
- Create / edit (`/strongroom/:slug/edit`)
- View (`/strongroom/:slug`)
- Unassign (`/strongroom/unassign`)

## Term Taxonomy (ahgTermTaxonomyPlugin)
*Category: browse - enabled, locked*

High-performance term and taxonomy browse
### Term
- Create / edit (`/term/add`)
### TermTaxonomy
- Delete (`/term/:slug/delete`)
- Create / edit (`/term/:slug/edit`)
- Export Skos (`/taxonomy/:id/skos`)
- View (`/term/:slug`)
- Related Authorities (`/term/:slug/related-authorities`)
- Taxonomy Index (`/taxonomy/:id`)
### CLI Commands
- `php symfony skos:import` - Import a SKOS RDF/XML file into a taxonomy
- `php symfony skos:validate` - Validate a taxonomy against core SKOS integrity rules

## Theme B5 (ahgThemeB5Plugin)
*Category: ahg - available (not enabled), core, locked*

Modern Bootstrap 5 theme for Access to Memory
### AhgVoice
- Describe Image (`/ahgVoice/describeImage`)
- Describe Object (`/ahgVoice/describeObject`)
- Get Settings (`/ahgVoice/getSettings`)
- Save Description (`/ahgVoice/saveDescription`)
### CLI Commands
- `php symfony theme:diagnose` - Diagnose ahgThemeB5Plugin configuration issues

## TIFF/PDF Merge (ahgTiffPdfMergePlugin)
*Category: ahg - enabled*

TIFF and PDF merge job management for digital preservation

## Time Limited Share Link (ahgTimeLimitedShareLinkPlugin)
*Category: records-management - enabled*

Time-limited, auditable share links for information_object records (anonymous bearer-token access, HMAC-SHA256 tokens, admin revocation, retention sweeps)
### ShareLink
- Administer
- Admin Show
- Issue
- Recipient
- Revoke
### CLI Commands
- `php symfony share-link:prune` - Apply retention rules to share-link tokens + access log.

## Translation (ahgTranslationPlugin)
*Category: ahg - enabled*

Machine Translation with LibreTranslate
### Translation
- Apply
- Health
- Configure
- Translate

## UI Overrides (ahgUiOverridesPlugin)
*Category: ahg - enabled, locked*

UI action overrides for AtoM modules - centralized location for action customizations
### Repository
- Edit Theme
### SfIsaarPlugin
- Create / edit

## User Manage (ahgUserManagePlugin)
*Category: browse - enabled*

User browse and management
### User
- Clipboard (`/user/clipboard`)
- Login (`/user/login`)
- Logout (`/user/logout`)
- Password Edit (`/user/passwordEdit`)
- Password Reset (`/user/passwordReset`)
### UserManage
- Browse (`/user`)
- Delete (`/user/:slug/delete`)
- Create / edit (`/user/add`)
- View (`/user/:slug`)

## User Registration (ahgUserRegistrationPlugin)
*Category: user - enabled*

Public user self-registration with email verification and admin approval workflow
### UserRegistration
- Approve
- Mark Verified
- Pending
- Register
- Reject
- Verify
### CLI Commands
- `php symfony registration:cleanup` - Clean up expired registration requests

## Vendor (ahgVendorPlugin)
*Category: ahg - enabled*
### Contract
- Add
- Browse
- Delete
- Create / edit
- Reminders
- View
### Vendor
- Add
- Add Contact
- Add Transaction
- Add Transaction Item
- Delete
- Delete Contact
- Create / edit
- Edit Transaction
- View
- List
- Remove Transaction Item
- Service Types
- Transactions
- Update Contact
- Update Transaction Item
- Update Transaction Status
- View
- View Transaction

## Version Control (ahgVersionControlPlugin)
*Category: records-management - enabled*

Version history with diff and restore for information_object and actor
### VersionControl
- Diff
- List
- Restore
- View
### CLI Commands
- `php symfony ahg-vc:regression` - AtoM-side regression sweep for F1/F2/F3 (GCIS RFB-001 wiring assertions)
- `php symfony version:backfill` - Create v1 baseline versions for entities that have no version history
- `php symfony version:capture` - Build snapshot + write as the next version for an entity
- `php symfony version:diff` - Print a structured diff between two stored versions
- `php symfony version:prune` - Apply retention rules to version history (preserves v1 + most-recent N).
- `php symfony version:snapshot` - Print a SnapshotBuilder JSON snapshot for an entity (smoke test)

## Workflow (ahgWorkflowPlugin)
*Category: ahg - enabled*

Configurable approval workflow system
### Workflow
- Add Step
- Administer
- Api Sla Status
- Api Stats
- Api Tasks
- Approve Task
- Bulk Execute
- Bulk Preview
- Change Summary
- Claim Task
- Create Workflow
- Dashboard
- Delete Step
- Delete Workflow
- Designer
- Designer Save
- Diagram
- Edit Step
- Edit Workflow
- Gate Admin
- Gate Rule Delete
- Gate Rule Edit
- History
- Install Spectrum Pack
- My Tasks
- My Work
- Object History
- Overdue
- Pool
- Publish Execute
- Publish Readiness
- Publish Simulate
- Queues
- Reject Task
- Release Task
- Reorder Steps
- Spectrum Chain
- Spectrum Chain Delete
- Spectrum Chain Save
- Spectrum Dashboard
- Spectrum Export Csv
- Start Workflow
- Task Diagram
- Team Work
- Timeline
- View Task
### CLI Commands
- `php symfony spectrum:overdue` - Scan for overdue Spectrum tasks and drop Workbench notifications.
- `php symfony workflow:process` - Process workflow operations (notifications, escalation, cleanup)
- `php symfony workflow:seed-spectrum` - Install the Spectrum 5.1 procedure starter pack — 21 workflows with paraphrased canonical steps.
- `php symfony workflow:status` - View workflow task status and statistics
