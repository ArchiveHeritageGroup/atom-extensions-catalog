# ahgVersionControlPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Version history with diff and restore for information_object and actor. Mirrors the AHG version-snapshot pattern used by reports, landing pages and heritage contributions. Integrates with ahgAuditTrailPlugin and ahgSecurityClearancePlugin.

## Overview

- **Name:** Version Control
- **Machine name:** `ahgVersionControlPlugin`
- **Version:** 0.1.0
- **Category:** records-management
- **Dependencies:** `ahgCorePlugin`
- **License:** proprietary

## Database tables

- `actor_version`
- `guards`
- `information_object_version`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Module actions

**`versionControl`** — `list`, `show`, `restore`, `diff`

## CLI tasks

- `php symfony ahg-vc:regression` — AtoM-side regression sweep for F1/F2/F3 (GCIS RFB-001 wiring assertions)
- `php symfony version:backfill` — Create v1 baseline versions for entities that have no version history
- `php symfony version:capture` — Build snapshot + write as the next version for an entity
- `php symfony version:diff` — Print a structured diff between two stored versions
- `php symfony version:prune` — Apply retention rules to version history (preserves v1 + most-recent N).
- `php symfony version:snapshot` — Print a SnapshotBuilder JSON snapshot for an entity (smoke test)

## Service layer

### `RestoreService`  
`lib/Services/RestoreService.php`

Public methods: `restore()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
