# ahgScanPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Watched-folder streaming ingest: configurable watched folders, a scan/watch CLI that detects new files and feeds the ingest pipeline, processed/failed disposition dirs, and dedupe by SHA-256 checksum.

## Overview

- **Name:** Watched Folder Scanner
- **Machine name:** `ahgScanPlugin`
- **Version:** 1.0.0
- **Category:** ingestion
- **Dependencies:** `ahgCorePlugin`, `ahgIngestPlugin`
- **License:** AGPL-3.0

### Features

- Configurable watched folders (path, layout, disposition, quiet period)
- Each folder bound 1:1 to an ahgIngestPlugin session for processing config
- scan:watch CLI detects new files and feeds the ingest commit pipeline
- SHA-256 dedupe — files already ingested in the session are skipped
- Quiet-period guard (skip files still being written)
- Processed (archive) and failed (quarantine) disposition directories
- Per-pass scan_event audit log with counts and errors
- Admin UI at /admin/scan to manage folders and review history

## Database tables

- `IF`
- `scan_event`
- `scan_folder`
- `then`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `scan_index` | `/admin/scan` | index |
| `scan_folder_new` | `/admin/scan/new` | edit |
| `scan_folder_create` | `/admin/scan/create` | create |
| `scan_folder_edit` | `/admin/scan/:id/edit` | edit |
| `scan_folder_update` | `/admin/scan/:id/update` | update |
| `scan_folder_delete` | `/admin/scan/:id/delete` | delete |
| `scan_folder_toggle` | `/admin/scan/:id/toggle` | toggle |
| `scan_folder_run` | `/admin/scan/:id/run` | run |
| `scan_folder_history` | `/admin/scan/:id/history` | history |

## Module actions

**`scanManage`** — `index`, `edit`, `create`, `update`, `delete`, `toggle`, `run`, `history`

## Service layer

### `ScannerService`  
`lib/Services/ScannerService.php`

Public methods: `scanFolder()`

### `WatchedFolderService`  
`lib/Services/WatchedFolderService.php`

Public methods: `listAll()`, `find()`, `findByCode()`, `enabledFolders()`, `create()`, `update()`, `delete()`, `touchScanned()`, `processedDir()`, `failedDir()`, `recentEvents()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
