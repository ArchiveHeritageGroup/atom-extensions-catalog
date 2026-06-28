# ahgNAZPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Zimbabwe National Archives Act [Chapter 25:06] compliance — 25-year closure rule, researcher permits, records schedules, transfers, and protected records management

## Overview

- **Name:** Zimbabwe NAZ Compliance
- **Machine name:** `ahgNAZPlugin`
- **Version:** 1.0.0
- **Category:** compliance
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Database tables

- `naz_audit_log`
- `naz_closure_period`
- `naz_config`
- `naz_protected_record`
- `naz_records_schedule`
- `naz_research_permit`
- `naz_research_visit`
- `naz_researcher`
- `naz_transfer`
- `naz_transfer_item`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `naz_index` | `/admin/naz` | index |
| `naz_closures` | `/admin/naz/closures` | closures |
| `naz_closure_create` | `/admin/naz/closure/create` | closureCreate |
| `naz_closure_edit` | `/admin/naz/closure/:id/edit` | closureEdit |
| `naz_permits` | `/admin/naz/permits` | permits |
| `naz_permit_create` | `/admin/naz/permit/create` | permitCreate |
| `naz_permit_view` | `/admin/naz/permit/:id` | permitView |
| `naz_researchers` | `/admin/naz/researchers` | researchers |
| `naz_researcher_create` | `/admin/naz/researcher/create` | researcherCreate |
| `naz_researcher_edit` | `/admin/naz/researcher/:id/edit` | researcherEdit |
| `naz_researcher_view` | `/admin/naz/researcher/:id` | researcherView |
| `naz_schedules` | `/admin/naz/schedules` | schedules |
| `naz_schedule_create` | `/admin/naz/schedule/create` | scheduleCreate |
| `naz_schedule_view` | `/admin/naz/schedule/:id` | scheduleView |
| `naz_transfers` | `/admin/naz/transfers` | transfers |
| `naz_transfer_create` | `/admin/naz/transfer/create` | transferCreate |
| `naz_transfer_view` | `/admin/naz/transfer/:id` | transferView |
| `naz_protected` | `/admin/naz/protected` | protectedRecords |
| `naz_reports` | `/admin/naz/reports` | reports |
| `naz_config` | `/admin/naz/config` | config |
| `naz_index_direct` | `/naz` | index |
| `naz_closures_direct` | `/naz/closures` | closures |
| `naz_permits_direct` | `/naz/permits` | permits |
| `naz_researchers_direct` | `/naz/researchers` | researchers |
| `naz_schedules_direct` | `/naz/schedules` | schedules |
| `naz_transfers_direct` | `/naz/transfers` | transfers |
| `naz_protected_direct` | `/naz/protected` | protectedRecords |
| `naz_reports_direct` | `/naz/reports` | reports |
| `naz_config_direct` | `/naz/config` | config |

## Module actions

**`naz`** — `index`, `closures`, `closureCreate`, `closureEdit`, `researchers`, `researcherCreate`, `researcherEdit`, `researcherView`, `permits`, `permitCreate`, `permitView`, `schedules`, `scheduleCreate`, `scheduleView`, `transfers`, `transferCreate`, `transferView`, `protectedRecords`, `reports`, `config`

## CLI tasks

- `php symfony naz:closure-check` — Check closure periods for expiry and releases
- `php symfony naz:permit-expiry` — Check research permits for expiry
- `php symfony naz:report` — Generate NAZ compliance reports
- `php symfony naz:transfer-due` — List pending and overdue records transfers

## Service layer

### `for`  
`lib/Services/NAZService.php`

Public methods: `getDashboardStats()`, `getComplianceStatus()`, `getClosures()`, `createClosure()`, `releaseClosure()`, `isRecordClosed()`, `getResearchers()`, `createResearcher()`, `updateResearcher()`, `getResearcher()`, `getPermits()`, `createPermit()`, `createVisit()`, `getVisitsByPermit()`, `approvePermit()`, `recordPermitPayment()`, `getPermit()`, `getSchedules()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
