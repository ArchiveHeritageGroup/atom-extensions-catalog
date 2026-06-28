# ahgIPSASPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). International Public Sector Accounting Standards (IPSAS 45) heritage asset accounting — asset register, valuations, impairments, insurance, depreciation, disposals, and financial year reporting

## Overview

- **Name:** IPSAS Heritage Accounting
- **Machine name:** `ahgIPSASPlugin`
- **Version:** 1.0.0
- **Category:** finance
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Database tables

- `ipsas_asset_category`
- `ipsas_audit_log`
- `ipsas_config`
- `ipsas_depreciation`
- `ipsas_disposal`
- `ipsas_financial_year_summary`
- `ipsas_heritage_asset`
- `ipsas_impairment`
- `ipsas_insurance`
- `ipsas_valuation`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `ipsas_index` | `/admin/ipsas` | index |
| `ipsas_assets` | `/admin/ipsas/assets` | assets |
| `ipsas_asset_create` | `/admin/ipsas/asset/create` | assetCreate |
| `ipsas_asset_view` | `/admin/ipsas/asset/:id` | assetView |
| `ipsas_asset_edit` | `/admin/ipsas/asset/:id/edit` | assetEdit |
| `ipsas_valuations` | `/admin/ipsas/valuations` | valuations |
| `ipsas_valuation_create` | `/admin/ipsas/valuation/create` | valuationCreate |
| `ipsas_impairments` | `/admin/ipsas/impairments` | impairments |
| `ipsas_insurance` | `/admin/ipsas/insurance` | insurance |
| `ipsas_reports` | `/admin/ipsas/reports` | reports |
| `ipsas_financial_year` | `/admin/ipsas/financial-year` | financialYear |
| `ipsas_config` | `/admin/ipsas/config` | config |

## Module actions

**`ipsas`** — `index`, `assets`, `assetCreate`, `assetView`, `assetEdit`, `valuations`, `valuationCreate`, `impairments`, `insurance`, `reports`, `financialYear`, `config`

## CLI tasks

- `php symfony ipsas:report` — Generate IPSAS heritage asset reports

## Service layer

### `for`  
`lib/Services/IPSASService.php`

Public methods: `getDashboardStats()`, `getComplianceStatus()`, `getAssets()`, `createAsset()`, `getAsset()`, `updateAsset()`, `getAssetValuations()`, `createValuation()`, `getValuations()`, `createImpairment()`, `getImpairments()`, `getInsurancePolicies()`, `createInsurance()`, `getCategories()`, `getFinancialYearSummary()`, `calculateFinancialYearSummary()`, `getConfig()`, `setConfig()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
