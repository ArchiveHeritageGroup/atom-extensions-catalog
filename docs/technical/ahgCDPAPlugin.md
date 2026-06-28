# ahgCDPAPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Zimbabwe Cyber and Data Protection Act [Chapter 12:07] compliance — DPO registration, breach management, DPIA, consent tracking, data subject requests, and POTRAZ reporting

## Overview

- **Name:** Zimbabwe CDPA Compliance
- **Machine name:** `ahgCDPAPlugin`
- **Version:** 1.0.0
- **Category:** compliance
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Database tables

- `cdpa_audit_log`
- `cdpa_breach`
- `cdpa_config`
- `cdpa_consent`
- `cdpa_controller_license`
- `cdpa_data_subject_request`
- `cdpa_dpia`
- `cdpa_dpo`
- `cdpa_processing_activity`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `ahg_cdpa_index` | `/admin/cdpa` | index |
| `ahg_cdpa_license` | `/admin/cdpa/license` | license |
| `ahg_cdpa_license_edit` | `/admin/cdpa/license/edit` | licenseEdit |
| `ahg_cdpa_dpo` | `/admin/cdpa/dpo` | dpo |
| `ahg_cdpa_dpo_edit` | `/admin/cdpa/dpo/edit` | dpoEdit |
| `ahg_cdpa_requests` | `/admin/cdpa/requests` | requests |
| `ahg_cdpa_request_view` | `/admin/cdpa/request/:id` | requestView |
| `ahg_cdpa_request_create` | `/admin/cdpa/request/create` | requestCreate |
| `ahg_cdpa_processing` | `/admin/cdpa/processing` | processing |
| `ahg_cdpa_processing_create` | `/admin/cdpa/processing/create` | processingCreate |
| `ahg_cdpa_processing_edit` | `/admin/cdpa/processing/:id/edit` | processingEdit |
| `ahg_cdpa_dpia` | `/admin/cdpa/dpia` | dpia |
| `ahg_cdpa_dpia_create` | `/admin/cdpa/dpia/create` | dpiaCreate |
| `ahg_cdpa_dpia_view` | `/admin/cdpa/dpia/:id` | dpiaView |
| `ahg_cdpa_consent` | `/admin/cdpa/consent` | consent |
| `ahg_cdpa_breaches` | `/admin/cdpa/breaches` | breaches |
| `ahg_cdpa_breach_create` | `/admin/cdpa/breach/create` | breachCreate |
| `ahg_cdpa_breach_view` | `/admin/cdpa/breach/:id` | breachView |
| `ahg_cdpa_reports` | `/admin/cdpa/reports` | reports |
| `ahg_cdpa_config` | `/admin/cdpa/config` | config |

## Module actions

**`cdpa`** — `index`, `license`, `licenseEdit`, `dpo`, `dpoEdit`, `requests`, `requestView`, `requestCreate`, `processing`, `processingCreate`, `processingEdit`, `dpia`, `dpiaCreate`, `dpiaView`, `consent`, `breaches`, `breachCreate`, `breachView`, `reports`, `config`

## CLI tasks

- `php symfony cdpa:license-check` — Check POTRAZ license expiry
- `php symfony cdpa:report` — Generate CDPA compliance report
- `php symfony cdpa:requests` — List data subject requests
- `php symfony cdpa:status` — Show CDPA compliance dashboard

## Service layer

### `CDPAService`  
`lib/Services/CDPAService.php`

Public methods: `getDashboardStats()`, `getComplianceStatus()`, `getCurrentLicense()`, `getLicenseStatus()`, `saveLicense()`, `getExpiringLicenses()`, `getActiveDPO()`, `saveDPO()`, `getRequests()`, `getPendingRequests()`, `getOverdueRequests()`, `createRequest()`, `updateRequestStatus()`, `getProcessingActivities()`, `getProcessingActivity()`, `createProcessingActivity()`, `getDPIAs()`, `getDPIA()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
