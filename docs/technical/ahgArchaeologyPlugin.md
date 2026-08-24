# ahgArchaeologyPlugin - Technical Documentation

## Overview

Records archaeological excavation: sites, stratigraphic contexts, the relationships between them, and finds. Computes the Harris Matrix from the recorded relationships, checks the record for contradictions, and exchanges data with the formats other stratigraphy software uses.

The design decision the plugin exists to serve: **stratigraphy is a directed acyclic graph, not a tree**. AtoM's nested set gives each record exactly one parent, whereas a context can lie beneath several at once, and two contexts in different trenches can be the same feature. Relationships therefore live in their own table while every context remains a full `information_object`, with the ACL, search indexing, digital objects and export that implies. Nothing is duplicated, and the sequence is never flattened into the hierarchy.

### Features

- Sites with coordinates, elevation, positional accuracy, period, site type, permit and excavator
- Contexts with type, phase, top and bottom elevations, excavation references and dates
- Nine relationship types, stored bidirectionally with automatic reciprocals
- Harris Matrix with correlation merging, longest-path layering and transitive reduction
- Finds linked to their context
- Dig plan with scaled sections and a tile-free locator
- PDF context sheets
- Six consistency checks
- Import and export in interchange formats

## Database tables

| Table | Purpose |
|---|---|
| `archaeology_site` | One row per site. Carries `information_object_id`, coordinates, `spatial_accuracy_m`, `site_type_id`, `period_id`, excavation metadata. |
| `archaeology_context` | One row per context. Carries `information_object_id`, `site_id`, `context_number`, `context_type_id`, `phase_id`, elevations. |
| `archaeology_context_relationship` | Stratigraphic edges. `UNIQUE KEY uk_arch_ctxrel (context_id, related_context_id, relationship_type)` makes writes idempotent. |
| `archaeology_object` | Finds. Carries `context_id`, `site_id`, accession number, dimensions, recovery method, storage location. |

Both entity tables reference an `information_object`, created through the framework's write service. Note that the write services do not populate `lft`/`rgt`, so `placeInNestedSet()` puts new descriptions into the tree; a record that exists but is not in the tree is invisible to browse.

## Relationship model

`ArchaeologyService::REL_TYPES` defines nine types, each with a reciprocal and a direction:

| Type | Reciprocal | Direction |
|---|---|---|
| `above` | `below` | later |
| `cuts` | `cut_by` | later |
| `fills` | `filled_by` | later |
| `same_as` | `same_as` | none |
| `bonds_with` | `bonds_with` | none |
| `abuts` | `abuts` | none |

`LATER_THAN` is the subset that carries sequence: `above`, `cuts`, `fills`. Only those form matrix edges.

`addRelationship()` writes both directions, rejects self-reference, and refuses any relationship that would create a loop by testing reachability before insert. It returns `existed` so callers can distinguish an addition from a re-import.

## The matrix

`harrisMatrix(int $siteId)` returns `tiers`, `edges`, `has_cycle`, `mermaid`, `context_count`, `relationship_count` and `redundant_count`. It is computed on every call and never stored, so the diagram cannot drift from the record.

1. **Correlation merging** - union-find with path halving over `same_as`, so correlated contexts become one node.
2. **Edge construction** - directed edges between merged nodes, from `LATER_THAN` relationships only.
3. **Layering** - Kahn longest-path over the full edge set. Level 0 is latest, drawn at the top. Fewer nodes drained than exist means a cycle, reported rather than silently dropping contexts.
4. **Transitive reduction** - applied to the drawn edges only, never to the record.

### Transitive reduction

Harris's Law of Stratigraphic Succession requires a matrix to show only immediate relationships. Where A is above B, B above C and A above C is also recorded, the third is implied and must not be drawn.

Reachability is computed **once**, as bitsets of descendants over a reverse topological order. The obvious implementation - a graph search per edge - is O(E x (V+E)) and was measured at 10.5 seconds on 3,000 contexts with 12,000 relationships, on a method that runs on every page view. The bitset form returns the same result in 60 ms.

Only valid on a DAG; the caller must not pass a cyclic graph, since the topological order would not exist. `redundant_count` is surfaced so a reader can tell a correct reduction from lost data.

## Consistency checks

`consistencyReport(int $siteId)` returns findings and the list of checks performed. Every check is deliberately conservative: a check that reports ordinary excavation messiness gets switched off, and then catches nothing.

| Check | Severity | Notes |
|---|---|---|
| Stratigraphic loops | error | From `has_cycle` |
| Contexts with no relationships | warning | Outside the sequence entirely |
| Sequence in unconnected pieces | warning | Undirected connectivity; normal for separate trenches |
| `same_as` contradicting superposition | error | Cannot be the same feature and one above the other |
| Elevations against superposition | warning | **`above` only**, strict inequality |
| Phase against superposition | warning | Convention inferred, not assumed |

Two constraints worth stating, because both produced false positives before they were understood:

**Elevation checks apply to `above` only.** A cut extends downward from the surface it was cut from, so its top sitting at the bottom of the deposit it cuts is correct; a fill sits inside that cut. Including `cuts` and `fills` gave a false positive for every one of them.

**Phase numbering direction is a site convention.** Some schemes number the earliest phase 1, others the latest. The check counts which way the site's own relationships run, adopts the majority as the convention, reports only the outliers, and stays silent when there is no clear majority.

## Import and export

### Export

`exportDataPackage()` returns a file map assembled into a zip by the export action. It follows the table schema Thomas Dye defined for the `hm` package, which the Harris Matrix Data Package builds on:

- `contexts.csv` - `label`, `unit-type` (`interface` or `deposit`), `position`, `period`, `phase`, `url`
- `observations.csv` - `younger`, `older`, `url`. No relation-type column: the format records superposition only.
- `correlations.csv` - **AHG extension**, named as such in the descriptor. `same_as` has no home in the two standard tables, and dropping it would lose real information.
- `datapackage.json` - Frictionless `tabular-data-package` descriptor.

`position` is emitted empty. `hm` uses it for surface and basal contexts, and it could be inferred from the top and bottom tiers, but "surface" is a claim about the ground rather than about a diagram.

`exportDot()` emits GraphViz DOT of the **reduced** edge set, with interfaces dashed. `exportPhaserCsv()` emits `siteCode`, `sourceID`, `stratRelationship`, `targetID`, one row per logical relationship - reciprocals are collapsed, so 22 relationships export as 22 rows rather than 44.

### Import

`importRelationshipsCsv()` takes rows of source, type and target. Contexts are matched by number within the site and **never created**: a relationship naming an unknown context is reported. Every row passes through `addRelationship()`, so reciprocity, self-reference and the cycle guard apply exactly as they do to typed entry. The whole run is wrapped in a transaction rolled back unless committed, so a preview reports real counts from a real run.

`parsePhaserCsv()` reads the four-column CSV and ignores rows whose `siteCode` names a different site, reporting how many were skipped. `parseLst()` reads the format written by BASP Harris, Stratify and ArchEd: the first three lines are ignored, the first unit name is on line four, and each unit is followed by exactly four comma-separated relationship lines in the order `above`, `contemporary_with`, `equal_to`, `below`, all four always present.

`contemporary_with` is **declined, not mapped**. It means units of the same period that are not physically joined, whereas `bonds_with` and `abuts` both assert physical contact; mapping it would record an observation nobody made. The count and reason are reported.

`RELATIONSHIP_SYNONYMS` accepts the vocabulary other tools use (`later`, `over`, `equal to`, `same as` and so on) so an import does not reject every file the field produces.

## Routes

Registered by `ahgArchaeologyPluginConfiguration` on `routing.load_configuration`. All numeric parameters are constrained to `\d+`.

| Route | Path |
|---|---|
| `archaeology_index` | `/archaeology` |
| `archaeology_sites` | `/archaeology/sites` |
| `archaeology_map` | `/archaeology/map` |
| `archaeology_site` | `/archaeology/site/:id` |
| `archaeology_contexts` | `/archaeology/site/:siteId/contexts` |
| `archaeology_plan` | `/archaeology/site/:siteId/plan` |
| `archaeology_export` | `/archaeology/site/:siteId/export/:format` |
| `archaeology_import` | `/archaeology/site/:siteId/import` |
| `archaeology_context` | `/archaeology/context/:id` |
| `archaeology_context_pdf` | `/archaeology/context/:id/pdf` |
| `archaeology_objects` | `/archaeology/finds` |
| `archaeology_object` | `/archaeology/find/:id` |

## Security

`modules/archaeology/config/security.yml` secures every action. A missing file inherits `default: is_secure: false` from the application configuration and **fails open**, so the file must exist. Reading requires `contributor`, `editor` or `administrator`; writing requires `editor` or `administrator`. An `all:` fallback secures any action not named individually, so a new action is private by default.

Nothing is public. Site coordinates and unpublished excavation records should not be browsable anonymously, and a context record can identify the position of a burial.

## Standards and conventions

- Laravel Query Builder throughout; no raw PDO
- Vocabularies matched by taxonomy name rather than hardcoded id, so an instance can rename or extend them
- `AhgDb::hasOptionalTable()` guards every optional-table read, so an instance without the schema degrades rather than erroring
- No inline `style` attributes: CSP nonces cover `<style>` elements, never style attributes
- Output escaping unwrapped once per template before array functions, since Symfony hands templates a decorator rather than an array
