# ahgInformationObjectManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). ISAD(G) information object CRUD management — create, edit, delete, digital object upload, treeview navigation via Laravel Query Builder

## Overview

- **Name:** ISAD(G) Information Object Manage
- **Machine name:** `ahgInformationObjectManagePlugin`
- **Version:** 1.0.0
- **Category:** descriptive-standard
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Routes

| Route name | URL | Action |
|---|---|---|
| `io_delete_override` | `/informationobject/:slug/delete` | delete |
| `io_edit_override` | `/informationobject/:slug/edit` | edit |
| `io_do_upload` | `/digitalobject/upload` | doUpload |
| `io_do_edit` | `/digitalobject/:id/edit` | doEdit |
| `io_do_delete` | `/digitalobject/:id/delete` | doDelete |
| `io_treeview` | `/informationobject/treeview` | treeview |
| `io_treeview_full` | `/informationobject/treeviewFull` | treeviewFull |
| `io_treeview_sort` | `/informationobject/treeviewSort` | treeviewSort |
| `io_actor_autocomplete` | `/informationobject/actorAutocomplete` | actorAutocomplete |
| `io_repository_autocomplete` | `/informationobject/repositoryAutocomplete` | repositoryAutocomplete |
| `io_term_autocomplete` | `/informationobject/termAutocomplete` | termAutocomplete |
| `io_generate_identifier` | `/informationobject/generateIdentifierJson` | generateIdentifier |
| `io_add_override` | `/informationobject/add` | edit |

## Module actions

**`ioManage`** — `edit`, `delete`, `treeview`, `treeviewFull`, `treeviewSort`, `actorAutocomplete`, `repositoryAutocomplete`, `termAutocomplete`, `generateIdentifier`, `doUpload`, `doEdit`, `doDelete`

## Service layer

### `InformationObjectCrudService`  
`lib/Services/InformationObjectCrudService.php`

Public methods: `getById()`, `getBySlug()`, `create()`, `update()`, `delete()`, `getLevelsOfDescription()`, `getDescriptionStatuses()`, `getDescriptionDetails()`, `getEventTypes()`, `getPublicationStatuses()`, `getDisplayStandards()`, `getDcTypeTerms()`, `getModsResourceTypes()`, `getMaterialTypes()`, `getStringProperties()`, `saveStringProperties()`, `getLanguageChoices()`, `getScriptChoices()`

### `TreeviewService`  
`lib/Services/TreeviewService.php`

Public methods: `getAncestors()`, `getChildren()`, `getSiblings()`, `getTreeViewData()`, `moveAfter()`, `getFullWidthTree()`

### `NestedSetService`  
`lib/Services/NestedSetService.php`

Public methods: `insertUnder()`, `removeNode()`, `hasChildren()`

### `DigitalObjectService`  
`lib/Services/DigitalObjectService.php`

Public methods: `getByInformationObjectId()`, `getById()`, `getDerivatives()`, `getMetadata()`, `getFilePath()`, `getWebPath()`, `getInformationObjectId()`, `getIoSlug()`, `getProperties()`, `updateProperties()`, `getMediaTypes()`, `getMediaTypeName()`, `getUsageName()`, `delete()`, `formatFileSize()`, `getMaxUploadSize()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
