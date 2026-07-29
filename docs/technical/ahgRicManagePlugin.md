# ahgRicManagePlugin - Technical Documentation

> Records in Context (RiC-O 1.0) as a selectable descriptive standard for information objects: capture form, record-view panel, typed relations, and RiC-O JSON-LD export. MySQL-only (no Fuseki dependency).

## Overview

- **Name:** AHG RiC Manage
- **Machine name:** `ahgRicManagePlugin`
- **Category:** descriptive standard
- **Dependencies:** `ahgCorePlugin`, `ahgInformationObjectManagePlugin` (shared IO form + `IoFormHelper`)
- **Scope:** PSIS / archive only (not deployed on archaeology)
- **Distinct from** `ahgRicExplorerPlugin` (graph/visualisation). Manage = capture + standard; Explorer = graph.

RiC is a *record-centric* implementation: an AtoM `information_object` **is** a RiC Record. Agents, places and functions remain the existing `actor` / `term` / `function` entities, linked by typed relations. No records are duplicated.

## Installation

```bash
php symfony ric:install
```

The task seeds a `ric` term in taxonomy 70 (`INFORMATION_OBJECT_TEMPLATE_ID`) and creates the plugin tables. It requires an sf context and disables search during the run:

- `sfContext::createInstance($this->configuration)` - term creation needs a context, or you get "default context does not exist".
- `QubitSearch::disable()` before saving - the CLI has no search config and `arOpenSearch` fatals on a null language list otherwise.

**Caution:** a failed `ric:install` can leave orphan taxonomy-70 terms (code NULL / name NULL) which then break record views (`QubitMetadataRoute::getActionParameter` throws on an unknown/NULL code). Clean up with `DELETE FROM term_i18n/term/object WHERE id IN (...)` then `php symfony propel:build-nested-set`.

## How a standard is dispatched (two layers)

A descriptive standard has to be wired in **two** independent places or a record on it 500s:

1. **View** - base `lib/routing/QubitMetadataRoute.class.php` (patched via `atom-framework/patches/`): `'ric' => 'sfIsadPlugin'` in `$METADATA_PLUGINS` **and** `'ric'` in the `getActionParameter()` whitelist (~line 152). RiC records render through the full ISAD template plus the RiC panel. Missing either entry = 500.
2. **Edit** - `IoFormHelper::MODULE_MAP['ric'] = 'ricManage'` + a `TERM_NAME_PATTERNS` entry `'Records in Context' => 'ric'`. `detectStandard()` maps the record's `display_standard_id` term to `ric`; `ioManage::executeEdit` forwards to `ricManage::executeEdit`.

> The `TERM_NAME_PATTERN` must be specific (`'Records in Context'`). An earlier over-broad `'RiC'` pattern matched "ame**RIC**an" inside the DACS label and misrouted DACS records.

Since atom-framework v2.13.45, the bare-slug record-view Edit button also reaches these AHG forms (`QubitMetadataRoute` routes `action=edit` to `ioManage`).

## Database

| Table | Purpose |
|---|---|
| `ric_record_meta` | Per-record RiC metadata. `object_id` (UNIQUE), `entity_type` VARCHAR, `ric_data` JSON (record-centric properties). |
| `ric_relation_meta` | Sidecar on a base `relation` row: `relation_id` (PK), `rico_predicate`, `inverse_predicate`, `domain_class`, `range_class`, `dropdown_code`, `certainty`, `evidence`. |

RiC relation types are **not** a table - they live in the `ahg_dropdown` taxonomy `ric_relation_type` (30 rows). Each row's `metadata` JSON carries `{predicate, inverse, domain, range, category, symmetric}`, which is decoded into `ric_relation_meta` on save.

## Routes

| Name | URL | Action |
|---|---|---|
| `ric_get` | `/ricManage/get/:objectId` | read entity type + properties + relations |
| `ric_save` | `/ricManage/save` | upsert entity type + properties |
| `ric_save_relation` | `/ricManage/saveRelation` | create a typed relation (v1.1) |
| `ric_delete_relation` | `/ricManage/deleteRelation` | delete a typed relation (v1.1) |
| `ric_search_targets` | `/ricManage/searchTargets` | title search for a relation target (v1.1) |
| `ric_export` | `/ricManage/export/:objectId` | RiC-O JSON-LD |

The write/search AJAX actions are editor-gated in code (`hasGroup(ADMINISTRATOR_ID) || hasGroup(EDITOR_ID)`); `security.yml` carries **no** `credentials:` (that would 403 administrators, who do not hold the literal `editor` credential).

## RicManageService (key methods)

- `getRecordMeta` / `saveRecordMeta` - entity type + `PROPERTY_FIELDS` (authenticity_note, integrity_note). `PROPERTY_PREDICATES` maps each key to its RiC-O predicate.
- `getTypedRelations` - joins `relation` + `ric_relation_meta`; returns predicate (direction-aware), target, `relation_id`, code, certainty, evidence.
- `getRelationTypes` - the 30 `ric_relation_type` dropdown entries with metadata decoded.
- `saveRelation($subjectId, $targetId, $code, $certainty, $evidence, $culture)` - writes the base `relation` via `AhgCore\Services\RelationService::save` (**creates the base `object` row first** - `relation.id` is a non-auto_increment QubitObject id under STRICT mode - `type_id` = 177 "Converse term"), then inserts `ric_relation_meta`.
- `deleteRelation` - removes the sidecar + the base relation.
- `searchTargets` - MySQL `title LIKE` search (self-contained, no Elasticsearch), excludes self + root.
- `exportRicO` - assembles the JSON-LD: entity type; authenticity/integrity from `ric_record_meta`; identifier/scope/history from the IO's own fields; subjects/places/genres/holder/names derived from access points + repository; typed relations.

## Capture form

`ricManage/editSuccess.php` is the full ISAD form plus a "Records in Context (RiC)" section (entity type + RiC-only notes). Every archival field is annotated at runtime with its RiC-O predicate via a client-side label map (`rico-auto-badge`, keyed by label `for=` id + text fallback), marking entity-mediated fields honestly ("via Instantiation" / "via Activity"). The RiC metadata saves via a prior AJAX POST to `/ricManage/save`.

> **Do not** write to `ric_record_meta` (an Illuminate write) inside the same request as `IoFormHelper::handlePost` - it silently voids the IO update (Propel/Illuminate share the request transaction). Save RiC metadata in its own AJAX request. The relation AJAX endpoints follow the same rule.

## Panel

`templates/display/_ric_panel.php`, loaded via `extension.json` `display_panels` (context `informationobject`, position `before-notes`). Gated to records whose standard is `ric` or that already have a `ric_record_meta` row. Editors get inline edit of the entity type/notes and the typed-relation add/delete controls (autocomplete via `ric_search_targets`, save/delete via the AJAX endpoints, self-saving through the theme CSRF-shim fetch then a reload).

## Related

- User guide: `docs/ric-descriptive-standard-user-guide.md`
- RiC Explorer (graph): `docs/technical/ahgRicExplorerPlugin.md`
