# Documentation coverage audit — 2026-06-27

111 plugins. Per the Documentation Rules each needs a USER manual (.md+.docx) and a TECHNICAL manual (.md+.docx).

- Technical .md missing: **46**
- Technical .docx missing (md exists): **59**
- User guide missing (excl. infra): **4**

| Plugin | Tech.md | Tech.docx | User | infra |
|---|---|---|---|---|
| ahg3DModelPlugin | ✓ | ✓ | ✓ |  |
| ahgAIPlugin | ✓ | ✗ | ✗ |  |
| ahgAPIPlugin | ✓ | ✗ | ✓ |  |
| ahgAccessRequestPlugin | ✓ | ✗ | ✓ |  |
| ahgAccessibilityPlugin | ✗ | ✗ | ✓ |  |
| ahgAccessionManagePlugin | ✗ | ✗ | ✓ |  |
| ahgActorManagePlugin | ✗ | ✗ | ✓ |  |
| ahgAiCompliancePlugin | ✗ | ✗ | ✓ |  |
| ahgAiConditionPlugin | ✗ | ✗ | ✓ |  |
| ahgAnnotationsPlugin | ✗ | ✗ | ✓ |  |
| ahgAuditTrailPlugin | ✓ | ✗ | ✓ |  |
| ahgAuthorityPlugin | ✗ | ✗ | ✓ |  |
| ahgAuthorityResolutionPlugin | ✗ | ✗ | ✓ |  |
| ahgBackupPlugin | ✓ | ✗ | ✓ |  |
| ahgC2paPlugin | ✗ | ✗ | ✓ |  |
| ahgCDPAPlugin | ✗ | ✗ | ✓ |  |
| ahgCartPlugin | ✓ | ✗ | ✓ |  |
| ahgConditionPlugin | ✓ | ✗ | ✓ |  |
| ahgContactPlugin | ✓ | ✗ | ✓ |  |
| ahgCorePlugin | ✓ | ✗ | ✓ | • |
| ahgCustomFieldsPlugin | ✓ | ✗ | ✓ |  |
| ahgDAMPlugin | ✓ | ✗ | ✓ |  |
| ahgDacsManagePlugin | ✗ | ✗ | ✓ |  |
| ahgDataMigrationPlugin | ✓ | ✗ | ✓ |  |
| ahgDcManagePlugin | ✗ | ✗ | ✓ |  |
| ahgDedupePlugin | ✓ | ✗ | ✗ |  |
| ahgDiscoveryPlugin | ✓ | ✗ | ✓ |  |
| ahgDisplayPlugin | ✓ | ✗ | ✗ |  |
| ahgDoiPlugin | ✓ | ✗ | ✓ |  |
| ahgDonorAgreementPlugin | ✓ | ✗ | ✓ |  |
| ahgDonorManagePlugin | ✗ | ✗ | ✓ |  |
| ahgEmailDeliveryPlugin | ✗ | ✗ | ✓ |  |
| ahgExhibitionPlugin | ✓ | ✗ | ✓ |  |
| ahgExportPlugin | ✓ | ✗ | ✓ |  |
| ahgExtendedRightsPlugin | ✓ | ✗ | ✓ |  |
| ahgFavoritesPlugin | ✓ | ✗ | ✓ |  |
| ahgFederationPlugin | ✓ | ✗ | ✓ |  |
| ahgFeedbackPlugin | ✓ | ✗ | ✓ |  |
| ahgFormsPlugin | ✓ | ✗ | ✓ |  |
| ahgFtpPlugin | ✗ | ✗ | ✓ |  |
| ahgFunctionManagePlugin | ✗ | ✗ | ✓ |  |
| ahgFunctionsDocsPlugin | ✗ | ✗ | ✓ |  |
| ahgGISPlugin | ✗ | ✗ | ✓ |  |
| ahgGalleryPlugin | ✓ | ✗ | ✓ |  |
| ahgGraphQLPlugin | ✓ | ✗ | ✓ |  |
| ahgHelpPlugin | ✗ | ✗ | ✓ | • |
| ahgHeritageAccountingPlugin | ✗ | ✗ | ✓ |  |
| ahgHeritagePlugin | ✓ | ✗ | ✓ |  |
| ahgICIPPlugin | ✓ | ✗ | ✓ |  |
| ahgIPSASPlugin | ✗ | ✗ | ✓ |  |
| ahgIiifPlugin | ✓ | ✓ | ✓ |  |
| ahgImageArPlugin | ✗ | ✗ | ✓ |  |
| ahgInformationObjectManagePlugin | ✗ | ✗ | ✓ |  |
| ahgIngestPlugin | ✓ | ✗ | ✓ |  |
| ahgIntegrityPlugin | ✗ | ✗ | ✓ |  |
| ahgJobsManagePlugin | ✗ | ✗ | ✓ |  |
| ahgLabelPlugin | ✓ | ✗ | ✓ |  |
| ahgLandingPagePlugin | ✓ | ✗ | ✓ |  |
| ahgLibraryPlugin | ✓ | ✗ | ✓ |  |
| ahgLoanPlugin | ✓ | ✗ | ✓ |  |
| ahgMarketplacePlugin | ✓ | ✗ | ✓ |  |
| ahgMenuManagePlugin | ✗ | ✗ | ✓ | • |
| ahgMetadataExportPlugin | ✓ | ✗ | ✓ |  |
| ahgMetadataExtractionPlugin | ✓ | ✗ | ✓ |  |
| ahgModsManagePlugin | ✗ | ✗ | ✓ |  |
| ahgMultiTenantPlugin | ✓ | ✗ | ✓ | • |
| ahgMuseumPlugin | ✓ | ✓ | ✓ |  |
| ahgNARSSAPlugin | ✓ | ✓ | ✓ |  |
| ahgNAZPlugin | ✗ | ✗ | ✓ |  |
| ahgNMMZPlugin | ✗ | ✗ | ✓ |  |
| ahgObservabilityPlugin | ✗ | ✗ | ✓ | • |
| ahgOcflPlugin | ✗ | ✗ | ✓ |  |
| ahgPortableExportPlugin | ✓ | ✗ | ✓ |  |
| ahgPreservationPlugin | ✓ | ✗ | ✓ |  |
| ahgPrivacyPlugin | ✓ | ✗ | ✓ |  |
| ahgProvenancePlugin | ✓ | ✗ | ✓ |  |
| ahgRadManagePlugin | ✗ | ✗ | ✓ |  |
| ahgRdmPlugin | ✗ | ✗ | ✗ |  |
| ahgRecordsManagePlugin | ✓ | ✓ | ✓ |  |
| ahgRegistryPlugin | ✓ | ✗ | ✓ |  |
| ahgReportBuilderPlugin | ✓ | ✗ | ✓ |  |
| ahgReportsPlugin | ✓ | ✗ | ✓ |  |
| ahgRepositoryManagePlugin | ✗ | ✗ | ✓ |  |
| ahgRequestToPublishPlugin | ✓ | ✗ | ✓ |  |
| ahgResearchPlugin | ✓ | ✓ | ✓ |  |
| ahgResearcherPlugin | ✗ | ✗ | ✓ |  |
| ahgResourceSyncPlugin | ✗ | ✗ | ✓ |  |
| ahgRicExplorerPlugin | ✓ | ✗ | ✓ |  |
| ahgRightsHolderManagePlugin | ✗ | ✗ | ✓ |  |
| ahgRightsPlugin | ✓ | ✗ | ✓ |  |
| ahgScanPlugin | ✗ | ✗ | ✓ |  |
| ahgSearchPlugin | ✗ | ✗ | ✓ |  |
| ahgSecurityClearancePlugin | ✓ | ✗ | ✓ |  |
| ahgSemanticSearchPlugin | ✓ | ✗ | ✓ |  |
| ahgSettingsPlugin | ✓ | ✗ | ✓ |  |
| ahgSharePointPlugin | ✗ | ✗ | ✓ |  |
| ahgSpectrumPlugin | ✓ | ✗ | ✓ |  |
| ahgStaticPagePlugin | ✗ | ✗ | ✓ |  |
| ahgStatisticsPlugin | ✓ | ✗ | ✓ |  |
| ahgStorageManagePlugin | ✗ | ✗ | ✓ |  |
| ahgTermTaxonomyPlugin | ✓ | ✗ | ✓ |  |
| ahgThemeB5Plugin | ✓ | ✗ | ✗ | • |
| ahgTiffPdfMergePlugin | ✓ | ✗ | ✓ |  |
| ahgTimeLimitedShareLinkPlugin | ✗ | ✗ | ✓ |  |
| ahgTranslationPlugin | ✓ | ✗ | ✓ |  |
| ahgUiOverridesPlugin | ✓ | ✗ | ✗ | • |
| ahgUserManagePlugin | ✗ | ✗ | ✓ |  |
| ahgUserRegistrationPlugin | ✗ | ✗ | ✓ |  |
| ahgVendorPlugin | ✓ | ✗ | ✓ |  |
| ahgVersionControlPlugin | ✗ | ✗ | ✓ |  |
| ahgWorkflowPlugin | ✓ | ✗ | ✓ |  |
