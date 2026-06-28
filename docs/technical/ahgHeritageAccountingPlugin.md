# ahgHeritageAccountingPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Multi-regional heritage asset financial accounting with support for IPSAS, GRAP, FRS, GASB, AASB, PSAS standards

## Overview

- **Name:** Heritage Asset Accounting
- **Machine name:** `ahgHeritageAccountingPlugin`
- **Version:** 2.0.0
- **Category:** accounting
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Database tables

- `heritage_accounting_standard`
- `heritage_asset`
- `heritage_asset_class`
- `heritage_compliance_rule`
- `heritage_impairment_assessment`
- `heritage_institution_config`
- `heritage_journal_entry`
- `heritage_movement_register`
- `heritage_regional_config`
- `heritage_transaction_log`
- `heritage_valuation_history`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `heritage_dashboard` | `/heritage/dashboard` | dashboard |
| `heritage_settings` | `/heritage/settings` | settings |
| `heritage_browse` | `/heritage/browse` | browse |
| `heritage_add` | `/heritage/add` | add |
| `heritage_view` | `/heritage/:id` | view |
| `heritage_edit` | `/heritage/:id/edit` | edit |
| `heritage_valuation_add` | `/heritage/:id/valuation/add` | addValuation |
| `heritage_impairment_add` | `/heritage/:id/impairment/add` | addImpairment |
| `heritage_movement_add` | `/heritage/:id/movement/add` | addMovement |
| `heritage_journal_add` | `/heritage/:id/journal/add` | addJournal |
| `heritage_view_by_object` | `/heritage/object/:slug` | viewByObject |
| `heritage_edit_by_object` | `/heritage/object/:slug/edit` | editByObject |
| `heritage_reports` | `/heritage/reports` | index |
| `heritage_report_asset_register` | `/heritage/report/asset-register` | assetRegister |
| `heritage_report_valuation` | `/heritage/report/valuation` | valuation |
| `heritage_report_movement` | `/heritage/report/movement` | movement |
| `grap_dashboard` | `/grap/dashboard` | dashboard |
| `grap_check` | `/grap/check/:id` | check |
| `grap_batch_check` | `/grap/batch-check` | batchCheck |
| `grap_national_treasury` | `/grap/national-treasury-report` | nationalTreasuryReport |
| `heritage_api_asset` | `/api/heritage/asset/:id` | asset |
| `heritage_api_actor_autocomplete` | `/api/heritage/actor-autocomplete` | actorAutocomplete |
| `heritage_api_autocomplete` | `/api/heritage/autocomplete` | autocomplete |
| `heritage_api_summary` | `/api/heritage/summary` | summary |

## Module actions

**`heritageAccounting`** — `dashboard`, `browse`, `view`, `add`, `edit`, `addValuation`, `addImpairment`, `addMovement`, `addJournal`, `settings`, `viewByObject`, `editByObject`
**`heritageAdmin`** — `index`, `regions`, `regionInstall`, `regionUninstall`, `regionSetActive`, `regionInfo`, `standardList`, `standardAdd`, `standardEdit`, `standardToggle`, `standardDelete`, `ruleList`, `ruleAdd`, `ruleEdit`, `ruleToggle`, `ruleDelete`
**`heritageReport`** — `index`, `assetRegister`, `valuation`, `movement`
**`heritageApi`** — `autocomplete`, `summary`, `asset`, `actorAutocomplete`
**`grapCompliance`** — `dashboard`, `check`, `batchCheck`, `nationalTreasuryReport`

## CLI tasks

- `php symfony heritage:install` — Install heritage accounting database schema
- `php symfony heritage:region` — Manage heritage accounting regions

## Service layer

### `GrapService`  
`lib/Extensions/Grap/Services/GrapService.php`

Public methods: `getAsset()`, `saveAsset()`, `logTransaction()`, `recordRevaluation()`, `recordImpairment()`, `runComplianceCheck()`, `getStatistics()`, `exportAssetRegister()`, `createSnapshot()`

### `GrapComplianceService`  
`lib/Services/GrapComplianceService.class.php`

Public methods: `getStandardId()`, `checkCompliance()`, `getComplianceSummary()`

### `HeritageComplianceService`  
`lib/Services/HeritageComplianceService.class.php`

Public methods: `checkCompliance()`, `getComplianceSummary()`, `getRulesForStandard()`, `getStandardsWithRuleCounts()`

### `HeritageAssetService`  
`lib/Services/HeritageAssetService.class.php`

Public methods: `getAccountingStandards()`, `getAssetClasses()`, `getAsset()`, `getAssetByObjectId()`, `browse()`, `create()`, `update()`, `delete()`, `addValuation()`, `addImpairment()`, `addMovement()`, `addJournal()`, `getValuationHistory()`, `getImpairmentAssessments()`, `getMovements()`, `getJournalEntries()`, `getDashboardStats()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
