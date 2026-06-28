# ahgRdmPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Sovereign (POPIA-resident) research-data-management module: dataset deposit, AI-assisted human-gated POPIA sensitivity scan, access/embargo + DOI, compliance dashboard. Reverse port of Heratio ahg-rdm (heratio#1337).

## Overview

- **Name:** RDM Manager
- **Machine name:** `ahgRdmPlugin`
- **Version:** 0.1.0
- **Category:** research
- **Dependencies:** `ahgCorePlugin`, `ahgIngestPlugin`, `ahgInformationObjectManagePlugin`, `ahgResearchPlugin`
- **License:** AGPL-3.0

### Features

- Dataset wrapper over a container information_object
- Per-file deposit as child IO + master digital_object (no bespoke storage)
- POPIA sensitivity scan (deterministic + lexicon + gateway NER) [later phases]
- Human-gated review of scan findings [later phases]
- Access/embargo (ODRL) + DataCite DOI + public landing [later phases]
- Compliance scoreboard + roll-up dashboard [later phases]

## Database tables

- `rdm_dataset`
- `rdm_dataset_file`
- `rdm_protected_object`
- `rdm_scan_finding`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `rdm_datasets_index` | `/research/datasets` | index |
| `rdm_datasets_dashboard` | `/research/datasets/dashboard` | dashboard |
| `rdm_datasets_compliance` | `/research/datasets/compliance` | compliance |
| `rdm_datasets_create` | `/research/datasets/create` | create |
| `rdm_datasets_show` | `/research/datasets/:id` | show |
| `rdm_datasets_deposit` | `/research/datasets/:id/deposit` | deposit |
| `rdm_datasets_scan` | `/research/datasets/:id/scan` | scan |
| `rdm_datasets_file` | `/research/datasets/:id/file/:fid` | fileDownload |
| `rdm_datasets_finding_resolve` | `/research/datasets/:id/findings/:fid/resolve` | resolveFinding |
| `rdm_datasets_disposition` | `/research/datasets/:id/disposition` | disposition |
| `rdm_datasets_dmp_link` | `/research/datasets/:id/dmp` | linkDmp |
| `rdm_datasets_dmp_unlink` | `/research/datasets/:id/dmp/unlink` | unlinkDmp |
| `rdm_datasets_landing` | `/research/datasets/:id/landing` | landing |

## Module actions

**`rdm`** — `index`, `create`, `show`, `linkDmp`, `unlinkDmp`, `dashboard`, `compliance`, `fileDownload`, `landing`, `resolveFinding`, `disposition`, `deposit`, `scan`

## CLI tasks

- `php symfony rdm:demo` — Run the full POPIA RDM demo on synthetic data (deposit->scan->gate->DOI->landing).
- `php symfony rdm:scan` — Run the POPIA sensitivity scan for an RDM dataset in the background

## Service layer

### `PopiaScanService`  
`lib/Services/PopiaScanService.php`

Public methods: `scanDataset()`

### `DatasetFileGuardService`  
`lib/Services/DatasetFileGuardService.php`

Public methods: `protectedDir()`, `accelPrefix()`, `protect()`, `release()`, `protectedPathForDo()`, `accelUri()`

### `DashboardService`  
`lib/Services/DashboardService.php`

Public methods: `overview()`

### `PopiaGateService`  
`lib/Services/PopiaGateService.php`

Public methods: `resolveFinding()`, `setDisposition()`, `gateStatus()`

### `DmpLinkService`  
`lib/Services/DmpLinkService.php`

Public methods: `context()`, `link()`, `createAndLink()`, `unlink()`

### `DatasetReleaseService`  
`lib/Services/DatasetReleaseService.php`

Public methods: `apply()`

### `DatasetService`  
`lib/Services/DatasetService.php`

Public methods: `create()`, `deposit()`, `get()`, `files()`, `list()`

### `ComplianceReportService`  
`lib/Services/ComplianceReportService.php`

Public methods: `rows()`, `institutions()`, `summary()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
