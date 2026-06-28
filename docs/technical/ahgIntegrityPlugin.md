# ahgIntegrityPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Enterprise-grade automated integrity assurance: scheduled fixity verification, scoped validation, concurrency controls, append-only ledger, dead-letter queue, retention policies, legal holds, disposition review, threshold alerting

## Overview

- **Name:** Integrity Assurance
- **Machine name:** `ahgIntegrityPlugin`
- **Version:** 1.1.0
- **Category:** preservation
- **Dependencies:** `ahgCorePlugin`, `ahgPreservationPlugin`
- **License:** AGPL-3.0

## Database tables

- `destruction_certificate`
- `integrity_alert_config`
- `integrity_dead_letter`
- `integrity_disposition_queue`
- `integrity_ledger`
- `integrity_legal_hold`
- `integrity_retention_policy`
- `integrity_run`
- `integrity_schedule`
- `record_declaration`
- `retention_trigger_event`
- `vital_record`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `integrity_index` | `/admin/integrity` | index |
| `integrity_schedules` | `/admin/integrity/schedules` | schedules |
| `integrity_schedule_edit` | `/admin/integrity/schedule/edit` | scheduleEdit |
| `integrity_runs` | `/admin/integrity/runs` | runs |
| `integrity_run_detail` | `/admin/integrity/run/:id` | runDetail |
| `integrity_ledger` | `/admin/integrity/ledger` | ledger |
| `integrity_dead_letter` | `/admin/integrity/dead-letter` | deadLetter |
| `integrity_report` | `/admin/integrity/report` | report |
| `integrity_export` | `/admin/integrity/export` | export |
| `integrity_export_csv` | `/admin/integrity/export/csv` | exportCsv |
| `integrity_export_auditor` | `/admin/integrity/export/auditor` | exportAuditor |
| `integrity_policies` | `/admin/integrity/policies` | policies |
| `integrity_policy_edit` | `/admin/integrity/policy/edit` | policyEdit |
| `integrity_holds` | `/admin/integrity/holds` | holds |
| `integrity_disposition` | `/admin/integrity/disposition` | disposition |
| `integrity_records` | `/admin/integrity/records` | records |
| `integrity_alerts` | `/admin/integrity/alerts` | alerts |
| `integrity_api_verify` | `/api/integrity/verify` | apiVerify |
| `integrity_api_run` | `/api/integrity/run/:id` | apiRun |
| `integrity_api_schedule_toggle` | `/api/integrity/schedule/:id/toggle` | apiScheduleToggle |
| `integrity_api_schedule_delete` | `/api/integrity/schedule/:id/delete` | apiScheduleDelete |
| `integrity_api_dead_letter_action` | `/api/integrity/dead-letter/:id/action` | apiDeadLetterAction |
| `integrity_api_stats` | `/api/integrity/stats` | apiStats |
| `integrity_api_run_schedule` | `/api/integrity/schedule/:id/run` | apiRunSchedule |
| `integrity_api_policy_toggle` | `/api/integrity/policy/:id/toggle` | apiPolicyToggle |
| `integrity_api_policy_delete` | `/api/integrity/policy/:id/delete` | apiPolicyDelete |
| `integrity_api_hold_place` | `/api/integrity/hold/place` | apiHoldPlace |
| `integrity_api_hold_release` | `/api/integrity/hold/:id/release` | apiHoldRelease |
| `integrity_api_disposition_action` | `/api/integrity/disposition/:id/action` | apiDispositionAction |
| `integrity_api_retention_scan` | `/api/integrity/retention/scan` | apiRetentionScan |
| `integrity_api_alert_save` | `/api/integrity/alert/save` | apiAlertSave |
| `integrity_api_alert_delete` | `/api/integrity/alert/:id/delete` | apiAlertDelete |
| `integrity_api_ledger` | `/api/integrity/ledger` | apiLedger |
| `integrity_api_runs` | `/api/integrity/runs` | apiRuns |
| `integrity_api_holds` | `/api/integrity/holds` | apiHolds |
| `integrity_api_policies` | `/api/integrity/policies` | apiPolicies |
| `integrity_api_daily_trend` | `/api/integrity/daily-trend` | apiDailyTrend |
| `integrity_api_repo_breakdown` | `/api/integrity/repo-breakdown` | apiRepoBreakdown |
| `integrity_api_format_breakdown` | `/api/integrity/format-breakdown` | apiFormatBreakdown |
| `integrity_api_throughput` | `/api/integrity/throughput` | apiThroughput |
| `integrity_api_storage_growth` | `/api/integrity/storage-growth` | apiStorageGrowth |

## Module actions

**`integrity`** — `records`, `index`, `schedules`, `scheduleEdit`, `runs`, `runDetail`, `ledger`, `deadLetter`, `report`, `export`, `exportCsv`, `exportAuditor`, `policies`, `policyEdit`, `holds`, `disposition`, `alerts`, `apiVerify`, `apiRun`, `apiScheduleToggle`, `apiScheduleDelete`, `apiRunSchedule`, `apiDeadLetterAction`, `apiStats`, `apiPolicyToggle`, `apiPolicyDelete`, `apiHoldPlace`, `apiHoldRelease`, `apiDispositionAction`, `apiRetentionScan`, `apiAlertSave`, `apiAlertDelete`, `apiLedger`, `apiRuns`, `apiHolds`, `apiPolicies`, `apiDailyTrend`, `apiRepoBreakdown`, `apiFormatBreakdown`, `apiThroughput`, `apiStorageGrowth`

## CLI tasks

- `php symfony integrity:report` — Generate integrity verification reports
- `php symfony integrity:retention` — Manage retention policies, legal holds, and disposition queue
- `php symfony integrity:schedule` — Manage integrity verification schedules
- `php symfony integrity:verify` — Run fixity verification on digital objects

## Service layer

### `IntegrityRetentionService`  
`lib/Services/IntegrityRetentionService.php`

Public methods: `listPolicies()`, `getPolicy()`, `createPolicy()`, `updatePolicy()`, `deletePolicy()`, `togglePolicy()`, `placeHold()`, `releaseHold()`, `listHolds()`, `isUnderHold()`, `scanEligible()`, `listDispositionQueue()`, `reviewDisposition()`, `processApprovedDispositions()`, `getDispositionStats()`

### `IntegrityService`  
`lib/Services/IntegrityService.php`

Public methods: `runMigration()`, `verifyObject()`, `executeBatchVerification()`, `buildScopeQuery()`, `verifyByObjectId()`, `updateDeadLetterStatus()`, `createSchedule()`, `updateSchedule()`, `deleteSchedule()`, `toggleSchedule()`, `getDashboardStats()`, `getRecentRuns()`, `getRecentFailures()`, `exportLedgerCsv()`, `generateAuditorPack()`, `renderAuditorSummaryHtml()`, `calculateBacklog()`, `calculateThroughput()`

### `IntegrityRecordsService`  
`lib/Services/IntegrityRecordsService.php`

Public methods: `isVital()`, `flagAsVital()`, `unflagVital()`, `reviewVitalRecord()`, `getVitalRecords()`, `getOverdueReviews()`, `getRecordStatus()`, `declareRecord()`, `approveDeclaration()`, `getDeclarations()`, `getCertificateNumber()`, `generateCertificate()`, `getCertificates()`, `getCertificate()`, `getEventTypes()`, `fireRetentionEvent()`, `getRetentionEvents()`

### `IntegrityAlertService`  
`lib/Services/IntegrityAlertService.php`

Public methods: `checkThresholds()`, `sendAlert()`, `sendEmailAlert()`, `sendWebhookAlert()`, `sendScheduleNotification()`, `listAlertConfigs()`, `createAlertConfig()`, `updateAlertConfig()`, `deleteAlertConfig()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
