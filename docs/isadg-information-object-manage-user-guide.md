# ISAD(G) Information Object Management

## A Guide for Archivists

---

## What is it?

The ISAD(G) Information Object Manage plugin (`ahgInformationObjectManagePlugin`) is the high-performance create, edit, and delete engine for archival descriptions in AtoM Heratio. It intercepts the standard `/informationobject/...` editing URLs and serves a modern ISAD(G) edit form, plus digital-object upload/edit/delete and treeview navigation, all backed by the Laravel Query Builder instead of the slower legacy path.

This is the default editing experience for archival descriptions catalogued to **ISAD(G)** (General International Standard Archival Description). It adds no new database tables — it writes to the standard AtoM information-object tables — and it also provides the autocomplete and identifier-generation services that the descriptive-standard forms (DACS, Dublin Core, MODS, RAD) rely on.

## Key features

- **Create and edit** archival descriptions via an ISAD(G) form, organised into the ISAD(G) areas:
  - Identity area, Context area, Content and structure area, Conditions of access and use area, Allied materials area, Notes area, and Description control area.
  - Field groups include identifier and alternative identifiers, scope and content, conditions governing access and reproduction, existence and location of originals, related units of description, publication notes, language and script notes, and access points (subject, place, name, genre).
- **Delete** descriptions (`delete` action) with confirmation.
- **Digital object management**: upload (`/digitalobject/upload`), edit (`/digitalobject/<id>/edit`), and delete (`/digitalobject/<id>/delete`).
- **Treeview navigation** of the description hierarchy, including full-tree and drag-to-sort reordering actions.
- **Type-ahead autocomplete** services for actors/creators, repositories, and terms (used by this form and the other descriptive-standard plugins).
- **Identifier generation** (`/informationobject/generateIdentifierJson`): a sector-aware numbering service that produces an identifier from the selected repository and parent, falling back gracefully to legacy logic if needed.

## How to use it

1. **Add a description.** Go to `/informationobject/add`. The ISAD(G) edit form opens (*Add new archival description*). Enter the title (mandatory) and level of description (mandatory), select a repository, and either type an identifier or click **Generate**.
2. **Edit a description.** Open any archival description and choose **Edit**, or go to `/informationobject/<slug>/edit`.
3. **Build the hierarchy.** Use the treeview to navigate parents and children, and drag items to reorder siblings where supported.
4. **Attach digital objects.** Use the digital-object upload action to add a master file; edit or delete it later via the digital-object edit/delete actions.
5. **Add access points and notes.** Use the type-ahead controls to link subjects, places, names, and creators; complete scope and content, access conditions, and notes.
6. **Save.** Submitting persists the description to the information-object tables.
7. **Delete.** From the description, choose **Delete** (`/informationobject/<slug>/delete`) and confirm.

Creating, editing, and deleting are restricted to authenticated **Administrator** and **Editor** users.

## Administration / settings

This plugin has no settings page of its own. Two behaviours are configuration-driven:

- **Identifier generation** uses the sector-aware numbering scheme (archive numbering); select a repository before generating.
- **Browse/sort defaults** honour the site-wide AtoM settings (e.g. hits-per-page).

## Tips & FAQ

- **The edit URL looks the same as base AtoM — is that intentional?** Yes. The plugin overrides the `/informationobject/...` edit, add, and delete routes so existing links keep working while serving the faster form.
- **Generate produces nothing.** Choose a repository first; the numbering scheme is repository- and parent-aware.
- **Why is editing faster than before?** The form uses the Laravel Query Builder and batched lookups rather than the legacy per-row queries that caused slow loads on large hierarchies.
- **Different standard, different form.** Records assigned to DACS, Dublin Core, MODS, or RAD are served by their respective descriptive-standard plugins; ISAD(G) records use this one.
