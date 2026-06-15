# Actor (Authority Record) Browse & Management

## A Guide for Archivists and Staff

---

## What is it?

The AHG Actor Manage plugin (`ahgActorManagePlugin`) provides a high-performance browse and autocomplete experience for **actors** — the authority records for people, families, and organisations (corporate bodies) that create or relate to archival material. It replaces the base AtoM actor browse, which suffered from N+1 query hangs on large datasets, with a fast implementation that queries Elasticsearch directly over HTTP (no Elastica layer) and populates facets in a couple of batched queries.

The plugin adds no new database tables — it browses the standard AtoM actor data and its search index. Viewing and editing individual authority records is handled through the standard ISAAR-aligned actor screens, which this plugin's routing wires up alongside its fast browse and autocomplete.

## Key features

- **Actor browse** (`/actor/browse`) backed by direct Elasticsearch HTTP queries for speed on large authority files.
- **Batch facet population** — sidebar facets are built with two queries instead of one-per-row, avoiding the legacy slowdown.
- **Sidebar facets / filters**, including entity type, languages, repository, occupation, place, subject, media types, and "has digital object."
- **Sorting** by name (alphabetic), with ascending/descending control, honouring the site-wide browser-sort setting.
- **Free-text search** with an optional field selector, plus support for the global search box redirecting into actor browse.
- **Advanced search** with multiple boolean criteria rows (query / field / and-or operator) and a related-authority filter.
- **Multiple display modes** (list, grid, card).
- **Actor autocomplete** (`/actor/autocomplete`) via Elasticsearch prefix search, with a database fallback if the index is unavailable — used by edit forms throughout the system to link creators and related actors.

## How to use it

1. **Browse actors.** Go to `/actor/browse`. Results are paged and sortable; use the sort control to change ordering.
2. **Filter with facets.** Use the sidebar facets (entity type, language, repository, occupation, place, subject, media type, has-digital-object) to narrow the list.
3. **Search.** Type a name or term in the search box. To target a specific field, use the field selector; for richer queries, open the advanced search panel and add boolean criteria rows.
4. **Switch display mode.** Choose list, grid, or card to suit the task.
5. **Open an actor.** Click a result to view the authority record (`/actor/<slug>`). From there you can **Edit** (`/actor/<slug>/edit`) or **Delete** (`/actor/<slug>/delete`), and you can create a new actor at `/actor/add` — these use the standard ISAAR actor screens.
6. **Autocomplete in forms.** When linking a creator or related actor elsewhere in the system, start typing — the autocomplete service suggests matching actors as you go.

## Tips & FAQ

- **Why is browse so much faster now?** It queries Elasticsearch directly and batches its facet lookups, eliminating the N+1 query pattern that made the base browse hang on large authority files.
- **Autocomplete works even when search is down.** If Elasticsearch is unavailable, autocomplete falls back to a database query so creator linking still works.
- **Facets look empty.** Facets are populated from the search index — if the index is stale, reindexing actors will restore accurate counts.
- **Entity types.** The entity-type facet distinguishes persons, families, and corporate bodies, helping you find the right kind of authority record quickly.
- **No dedicated settings.** This plugin has no admin settings of its own; browse defaults follow the site-wide AtoM settings.
