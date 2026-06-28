# ahgSharePointPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Microsoft 365 SharePoint integration: tenant config, drive registration, manual delta sync (Phase 1); webhook records handoff (Phase 2); federated search + M365 connector feed (Phase 3). One-way: SharePoint -> AtoM ingest.

## Overview

- **Name:** SharePoint Integration
- **Machine name:** `ahgSharePointPlugin`
- **Version:** 0.1.0
- **Category:** integration
- **Dependencies:** `ahgCorePlugin`, `ahgSettingsPlugin`, `ahgIngestPlugin`, `ahgAuditTrailPlugin`
- **License:** AGPL-3.0

### Features

- Azure AD app-registration auth (client-credentials flow)
- Tenant + drive registration UI
- Per-drive column mapping editor
- Microsoft Graph delta query sync (manual + scheduled)
- Webhook subscription lifecycle (Phase 2)
- Records handoff via existing IngestCommitService pipeline (Phase 2)
- Purview retention label -> AtoM disposition mapping (Phase 2)
- AtoM-side federated search tab (staff-only, Phase 3)
- M365-side Microsoft Search connector feed (Phase 3)
- Encrypted client_secret storage via framework EncryptionService

## Database tables

- `sharepoint_drive`
- `sharepoint_event`
- `sharepoint_mapping`
- `sharepoint_subscription`
- `sharepoint_sync_state`
- `sharepoint_tenant`
- `sharepoint_user_mapping`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `sharepoint_index` | `/sharepoint` | index |
| `sharepoint_tenants` | `/sharepoint/tenants` | tenants |
| `sharepoint_tenant_edit` | `/sharepoint/tenants/:id` | tenantEdit |
| `sharepoint_tenant_test` | `/sharepoint/tenants/:id/test` | tenantTest |
| `sharepoint_drives` | `/sharepoint/drives` | drives |
| `sharepoint_drive_browse` | `/sharepoint/drives/browse` | driveBrowse |
| `sharepoint_drive_mapping` | `/sharepoint/drives/:id/mapping` | mapping |
| `sharepoint_subscriptions` | `/sharepoint/subscriptions` | subscriptions |
| `sharepoint_events` | `/sharepoint/events` | events |
| `sharepoint_event_detail` | `/sharepoint/events/:id` | eventDetail |
| `sharepoint_webhook` | `/sharepoint/webhook` | webhook |
| `sharepoint_user_mappings` | `/sharepoint/user-mappings` | userMappings |
| `sharepoint_user_mapping_edit` | `/sharepoint/user-mappings/:id` | userMappingEdit |
| `sharepoint_push_projection` | `/api/v2/sharepoint/push/projection` | pushProjection |
| `sharepoint_push` | `/api/v2/sharepoint/push` | push |
| `sharepoint_push_job` | `/api/v2/sharepoint/push/jobs/:id` | pushJob |
| `sharepoint_federated` | `/sharepoint/federated-search` | federatedSearch |
| `sharepoint_rules` | `/sharepoint/rules` | rules |
| `sharepoint_rule_edit` | `/sharepoint/rules/edit` | ruleEdit |
| `sharepoint_rule_save` | `/sharepoint/rules/save` | ruleSave |
| `sharepoint_rule_delete` | `/sharepoint/rules/:id/delete` | ruleDelete |
| `sharepoint_rule_run` | `/sharepoint/rules/:id/run` | ruleRun |
| `sharepoint_mappings` | `/sharepoint/mappings` | mappings |
| `sharepoint_mappings_save` | `/sharepoint/mappings/save` | mappingsSave |
| `sharepoint_mapping_template_delete` | `/sharepoint/mappings/template/delete` | mappingTemplateDelete |
| `sharepoint_columns` | `/sharepoint/columns` | columns |
| `sharepoint_drive_register` | `/sharepoint/drives/register` | driveRegister |
| `sharepoint_drive_save` | `/sharepoint/drives/save` | driveSave |
| `sharepoint_drive_delete` | `/sharepoint/drives/:id/delete` | driveDelete |

## Module actions

**`sharepoint`** — `index`, `tenants`, `tenantEdit`, `tenantTest`, `drives`, `driveBrowse`, `driveRegister`, `driveSave`, `driveDelete`, `columns`, `mapping`, `subscriptions`, `events`, `eventDetail`, `webhook`, `userMappings`, `userMappingEdit`, `pushProjection`, `push`, `pushJob`, `federatedSearch`, `rules`, `ruleEdit`, `ruleSave`, `ruleDelete`, `ruleRun`, `mappings`, `mappingsSave`, `mappingTemplateDelete`

## CLI tasks

- `php symfony sharepoint:auto-ingest` — Cron-driven SharePoint→AtoM ingest
- `php symfony sharepoint:ingest-event` — Process one inbound SharePoint webhook event
- `php symfony sharepoint:install` — Install ahgSharePointPlugin schema (idempotent)
- `php symfony sharepoint:post-ingest-hooks` — Run compliance hooks (sp_xref + version baseline + classification + AIP + PII) on IOs from a given ingest job
- `php symfony sharepoint:renew-subscriptions` — Renew Graph webhook subscriptions expiring within 12h
- `php symfony sharepoint:status` — Print SharePoint integration health (tenants, drives, subs, queue depth)
- `php symfony sharepoint:subscribe` — Create Graph webhook subscriptions (driveItem + list) for a drive
- `php symfony sharepoint:sync` — Delta-poll one or all ingest-enabled SharePoint drives
- `php symfony sharepoint:test-connection` — Test Microsoft Graph connectivity for a configured tenant

## Service layer

### `SharePointSubscriptionService`  
`lib/Services/SharePointSubscriptionService.php`

Public methods: `subscribeDrive()`, `renewExpiring()`, `deleteSubscription()`

### `SharePointAutoIngestService`  
`lib/Services/SharePointAutoIngestService.php`

Public methods: `runDueRules()`, `runRule()`, `materializeMappings()`

### `SharePointPushService`  
`lib/Services/SharePointPushService.php`

Public methods: `project()`, `commit()`

### `SharePointUserMappingService`  
`lib/Services/SharePointUserMappingService.php`

Public methods: `resolve()`

### `SharePointMappingService`  
`lib/Services/SharePointMappingService.php`

Public methods: `project()`

### `SharePointBrowserService`  
`lib/Services/SharePointBrowserService.php`

Public methods: `listSites()`, `listDrives()`, `listChildren()`, `downloadItem()`, `listColumns()`, `getMetadata()`

### `PostIngestHookService`  
`lib/Services/PostIngestHookService.php`

Public methods: `runForJob()`

### `GraphClientService`  
`lib/Services/GraphClientService.php`

Public methods: `acquireToken()`, `acquireOboToken()`, `get()`, `post()`, `patch()`, `delete()`, `downloadDriveItem()`, `downloadDriveItemByDriveId()`, `getListItemFields()`

### `GraphTokenValidatorService`  
`lib/Services/GraphTokenValidatorService.php`

Public methods: `validate()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
