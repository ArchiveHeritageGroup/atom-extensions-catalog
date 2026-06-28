# ahgOcflPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). OCFL v1.1 (Oxford Common File Layout) preservation storage: storage-root management, content-addressed object versioning with deterministic inventory.json + SHA-512 digests, per-version directories, fixity verification and tar export.

## Overview

- **Name:** OCFL Preservation Storage
- **Machine name:** `ahgOcflPlugin`
- **Version:** 1.0.0
- **Category:** preservation
- **Dependencies:** `ahgCorePlugin`
- **License:** AGPL-3.0

## Database tables

- `ahg_ocfl_object_map`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `ocfl_index` | `/admin/ocfl` | index |
| `ocfl_api_init` | `/api/ocfl/init` | apiInit |
| `ocfl_api_verify_all` | `/api/ocfl/verify-all` | apiVerifyAll |
| `ocfl_api_ingest` | `/api/ocfl/ingest/:id` | apiIngest |
| `ocfl_api_verify` | `/api/ocfl/verify/:id` | apiVerify |
| `ocfl_api_export` | `/api/ocfl/export/:id` | apiExport |

## Module actions

**`ocfl`** — `index`, `apiInit`, `apiIngest`, `apiVerify`, `apiVerifyAll`, `apiExport`

## Service layer

### `OcflService`  
`lib/Services/OcflService.php`

Public methods: `rootDir()`, `setting()`, `storageRootPath()`, `layout()`, `digestAlgorithm()`, `exportPath()`, `storageRoot()`, `objectIdForIo()`, `loadDigitalObjects()`, `resolveFilePath()`, `ingestInformationObject()`, `upsertObjectMap()`, `resolveObjectId()`, `exportObject()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
