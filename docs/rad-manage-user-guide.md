# RAD Descriptive Standard

## A Guide for Archivists

---

## What is it?

The RAD Descriptive Standard plugin (`ahgRadManagePlugin`) provides a create-and-edit form for cataloguing archival descriptions using **RAD — Rules for Archival Description**, the Canadian archival descriptive standard. When an information object is set to use the RAD standard, this plugin renders the edit screen using the multi-level area structure and terminology that RAD practitioners expect, rather than the generic ISAD(G) layout.

The plugin adds no new database tables; it stores everything in the standard AtoM information-object tables and only changes how the edit form is organised so RAD metadata can be entered fully and consistently.

## Key features

- RAD-oriented create and edit form for information objects, organised into RAD's descriptive areas:
  - **Title and statement of responsibility area** — level of description, identifier, alternative identifier(s).
  - **Edition area** — including statement of responsibility relating to the edition.
  - **Class of material specific details area.**
  - **Dates of creation area.**
  - **Physical description area** — physical description.
  - **Archival description area** — scope and content.
  - **Notes area** — physical condition, language and script notes, location of originals, restrictions on access, related material descriptions, and other notes (repeatable).
  - **Standard number area.**
  - **Access points** — subject, place, genre, and name access points.
  - **Control area** — description record identifier, institution identifier, language(s) and script(s) of description.
  - **Administration area** — administrative metadata.
- Repeatable rows (e.g. alternative identifiers and notes) with **Add** / **Remove** controls.
- Linked related-material descriptions with a checkbox to remove a link on save.
- Type-ahead "Type to add subject..." and other access-point controls, plus shared identifier-generation.

## How to use it

1. **Create a new description.** Go to `/informationobject/add`. If the record uses the RAD standard, the RAD form is shown (*Add new archival description*).
2. **Edit an existing description.** Open the record and choose **Edit**, or visit `/informationobject/<slug>/edit`.
3. **Work down the areas.** Complete the title and statement of responsibility, edition, class-of-material details, dates, physical description, and scope and content in turn.
4. **Add notes and access points.** Record physical condition, language/script notes, location of originals and access restrictions; add subject, place, genre, and name access points via the type-ahead controls.
5. **Complete the control area.** Enter the description record identifier, institution identifier, and language(s)/script(s) of description.
6. **Save.** Submitting writes the values back to the information object.

Editing is restricted to authenticated **Administrator** or **Editor** users.

## Tips & FAQ

- **When should I use RAD?** Use RAD when your institution follows the Canadian *Rules for Archival Description*; the area structure mirrors RAD's chapters.
- **Genre access points are RAD-specific.** RAD records include a genre access-point group in addition to subject, place, and name — use it for form/genre terms.
- **Removing a related description.** In the related-material section, uncheck a linked description before saving to remove the link.
- **No dedicated settings.** This plugin has no admin settings of its own.
