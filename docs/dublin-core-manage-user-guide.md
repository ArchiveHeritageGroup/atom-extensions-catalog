# Dublin Core Descriptive Standard

## A Guide for Archivists and Cataloguers

---

## What is it?

The Dublin Core Descriptive Standard plugin (`ahgDcManagePlugin`) provides a create-and-edit form for describing resources using **Dublin Core (DC)**, the widely adopted, lightweight metadata standard. When an information object is set to use the Dublin Core standard, this plugin renders the edit screen using Dublin Core elements and terminology instead of the fuller ISAD(G) archival layout.

Dublin Core is ideal for simple, interoperable descriptions — digital resources, web content, and collections that do not need the depth of a full archival standard. The plugin adds no new database tables; it stores values in the standard AtoM information-object tables and only changes the form presentation.

## Key features

- Dublin Core create and edit form for information objects.
- Field groups arranged around the Dublin Core elements, including:
  - **Elements area** — Identifier, Title, Description (an abstract, table of contents or description of the resource), Subject, Level of description, Format (the file format, physical medium, or dimensions), Relation/Source (a related resource from which the described resource is derived), Relation (isLocatedAt), and Rights (information about rights held in and over the resource).
  - **Administration area** — administrative metadata for the record.
- Subject access points via a type-ahead "Type to add subject..." control.
- Helpful inline guidance text drawn directly from the Dublin Core element definitions.
- Standard repeatable rows and search/type-ahead controls shared with the other descriptive-standard forms.

## How to use it

1. **Create a new description.** Go to `/informationobject/add`. If the record uses the Dublin Core standard, the DC form is displayed (*Add new archival description*).
2. **Edit an existing description.** Open the record and choose **Edit**, or visit `/informationobject/<slug>/edit`.
3. **Enter the core elements.** Provide a Title and Identifier, then add a Description, Subject(s), Format, Relation/Source, and Rights as needed. The on-screen hints explain what each element captures.
4. **Add subjects.** Use the *Type to add subject...* field to attach controlled subject terms.
5. **Save.** Submitting writes the values back to the information object.

Editing is restricted to authenticated **Administrator** or **Editor** users.

## Tips & FAQ

- **When should I use Dublin Core instead of ISAD(G)?** Choose Dublin Core for simple, interoperable records (especially born-digital or web resources) where the 15-element model is sufficient. Use ISAD(G), DACS, MODS or RAD for in-depth archival description.
- **Keep descriptions concise.** Dublin Core's strength is simplicity and cross-system interoperability — record the essentials in each element.
- **Subjects are controlled terms.** Adding subjects via the type-ahead keeps them linked to your taxonomy so they remain searchable and faceted.
- **No dedicated settings.** This plugin has no admin settings; it relies on the shared information-object editing infrastructure.
