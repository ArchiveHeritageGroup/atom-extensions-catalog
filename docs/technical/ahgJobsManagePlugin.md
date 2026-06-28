# ahgJobsManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Background jobs browse, delete, and report management using Laravel Query Builder

## Overview

- **Name:** Background Jobs Manage
- **Machine name:** `ahgJobsManagePlugin`
- **Version:** 1.0.0
- **Category:** admin
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Routes

| Route name | URL | Action |
|---|---|---|
| `jobs_browse` | `/jobs` | browse |
| `jobs_report` | `/jobs/report/:id` | report |
| `jobs_delete` | `/jobs/delete` | delete |
| `jobs_export` | `/jobs/export` | export |
| `queue_browse` | `/admin/queue` | queueBrowse |
| `queue_detail` | `/admin/queue/detail/:id` | queueDetail |
| `queue_batches` | `/admin/queue/batches` | queueBatches |
| `queue_progress` | `/admin/queue/progress` | queueProgress |
| `queue_retry` | `/admin/queue/retry` | queueRetry |
| `queue_cancel` | `/admin/queue/cancel` | queueCancel |

## Module actions

**`jobsManage`** — `browse`, `report`, `delete`, `queueBrowse`, `queueDetail`, `queueBatches`, `queueProgress`, `queueRetry`, `queueCancel`, `export`

## Service layer

### `JobsService`  
`lib/Services/JobsService.php`

Public methods: `browse()`, `getById()`, `getNotes()`, `deleteInactive()`, `deleteSingle()`, `getStats()`, `exportCsv()`, `getStatusLabel()`, `getStatusBadge()`

### `QueueJobsService`  
`lib/Services/QueueJobsService.php`

Public methods: `browseQueueJobs()`, `getQueueJob()`, `getQueueStats()`, `browseQueueBatches()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
