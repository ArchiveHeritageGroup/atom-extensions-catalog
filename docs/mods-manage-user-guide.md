# MODS Descriptive Standard

## A Guide for Cataloguers and Librarians

---

## What is it?

The MODS Descriptive Standard plugin (`ahgModsManagePlugin`) provides a create-and-edit form for describing resources using **MODS — the Metadata Object Description Schema**, a rich, library-oriented metadata standard maintained by the Library of Congress. When an information object is set to use the MODS standard, this plugin renders the edit screen using MODS-aligned field groups and terminology rather than the generic ISAD(G) layout.

MODS sits between simple Dublin Core and full MARC, making it a good fit for library and digital-collection material that needs more structure than Dublin Core but does not require a full archival standard. The plugin adds no new database tables; it stores values in the standard AtoM information-object tables and only changes the form layout.

## Key features

- MODS-oriented create and edit form for information objects.
- Field groups arranged around MODS, including:
  - **Elements area** — Identifier, alternative identifier(s), names and origin info, level of description.
  - **Subject and access points** — Subject access points (with a type-ahead), place access points, and name access points.
  - **Access conditions** — information about restrictions on access to the resource.
  - **Description** — an abstract or description of the resource scope and content.
  - **Administration area** — administrative metadata for the record.
- Repeatable alternative-identifier rows with **Add** / **Remove** controls.
- Type-ahead "Type to add subject..." for controlled subject terms, plus place and name access points.
- Shared identifier-generation and search/type-ahead controls used across the descriptive-standard forms.

## How to use it

1. **Create a new description.** Go to `/informationobject/add`. If the record uses the MODS standard, the MODS form is shown (*Add new archival description*).
2. **Edit an existing description.** Open the record and choose **Edit**, or visit `/informationobject/<slug>/edit`.
3. **Record names and origin info.** Capture the title/identifier, alternative identifier(s), names and origin information, and the level of description.
4. **Add access points.** Use the type-ahead controls to add subject, place, and name access points so the record is properly indexed.
5. **Set access conditions and description.** Note any restrictions on access, then complete the abstract/description of scope and content.
6. **Save.** Submitting writes the values back to the information object.

Editing is restricted to authenticated **Administrator** or **Editor** users.

## Tips & FAQ

- **When should I use MODS?** Choose MODS for library and digital-collection items that need richer, structured description than Dublin Core offers — for example bibliographic and digital-object metadata that maps cleanly to/from MARC.
- **Use access points liberally.** Subject, place, and name access points drive faceted browse and search; entering them via the type-ahead keeps them linked to your authorities and taxonomies.
- **Alternative identifiers.** Record former or external reference numbers as alternative identifiers so legacy references remain findable.
- **No dedicated settings.** This plugin has no admin settings of its own.
