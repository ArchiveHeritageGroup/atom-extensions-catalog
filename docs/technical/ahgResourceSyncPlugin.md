# ahgResourceSyncPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). ResourceSync 1.1 (NISO Z39.99-2017) Source endpoints: Source Description, Capability List, Resource List and Change List as sitemap-formatted XML. Mirrors the OAI-PMH publication filter so aggregators see the same record + tombstone set across both federation surfaces.

## Overview

- **Name:** AHG ResourceSync Plugin
- **Machine name:** `ahgResourceSyncPlugin`
- **Version:** 1.0.0
- **Category:** integration
- **Dependencies:** none
- **License:** GPL-3.0

### Features

- ResourceSync 1.1 Source role
- Source Description (.well-known/resourcesync)
- Capability List
- Resource List (full inventory, paginated)
- Change List (recent updates + tombstones, configurable horizon)
- OAI-PMH publication filter parity (status type_id=158 / status_id=160)
- Tombstones sourced from oai_deleted_record (shared with OAI-PMH)
- Sitemap-formatted XML with rs:md / rs:ln ResourceSync extension

## Database tables

- `IF`
- `oai_deleted_record`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `resourcesync_source_description` | `/.well-known/resourcesync` | sourceDescription |
| `resourcesync_capability_list` | `/resourcesync/capabilitylist.xml` | capabilityList |
| `resourcesync_resource_list` | `/resourcesync/resourcelist.xml` | resourceList |
| `resourcesync_change_list` | `/resourcesync/changelist.xml` | changeList |

## Module actions

**`resourcesync`** — `changeList`
**`resourcesync`** — `capabilityList`
**`resourcesync`** — `resourceList`
**`resourcesync`** — `sourceDescription`

## Service layer

### `ResourceSyncService`  
`lib/Services/ResourceSyncService.php`

Public methods: `sourceDescription()`, `capabilityList()`, `resourceList()`, `changeList()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
