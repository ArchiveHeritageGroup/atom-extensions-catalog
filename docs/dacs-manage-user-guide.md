# DACS Descriptive Standard

## A Guide for Archivists

---

## What is it?

The DACS Descriptive Standard plugin (`ahgDacsManagePlugin`) provides a tailored create-and-edit form for cataloguing archival descriptions using **DACS — Describing Archives: A Content Standard**, the descriptive standard widely used in North American archives. When an information object is set to use the DACS standard, this plugin renders the edit form with the field groupings and terminology that DACS practitioners expect, rather than the generic ISAD(G) layout.

The plugin does not add any new database tables — it stores everything in the standard AtoM information-object tables. It simply changes how the edit screen is laid out so that DACS metadata can be entered cleanly and consistently.

## Key features

- DACS-oriented create and edit form for information objects.
- Field groups arranged to match DACS practice, including:
  - **Identity elements** — Identifier, alternative identifier(s), repository, level of description, title, dates, extent, and name of creator(s).
  - **Content and structure elements** — Scope and content, system of arrangement.
  - **Conditions of access and use elements** — Conditions governing access (physical and technical access), conditions governing reproduction, language(s), script(s), language and script notes, finding aids.
  - **Acquisition and appraisal elements** — Custodial history, immediate source of acquisition.
- Repeatable rows for alternative identifiers, dates, creators, languages, and scripts (each with an **Add** / **Remove** control).
- Identifier auto-generation: pick a repository, then click **Generate** to produce an identifier using the archive numbering scheme.
- Type-ahead search for repositories, creators/actors, and subject terms.
- Inline "Add new child levels" so you can create child descriptions (identifier, level, title) directly from the parent's edit screen.

## How to use it

1. **Create a new description.** Browse to `/informationobject/add` (or use the "Add" action from the archival descriptions area). If the DACS standard is selected for the record, the DACS edit form is shown.
2. **Edit an existing description.** Open any archival description and choose **Edit**, or go to `/informationobject/<slug>/edit`. The form opens at *Edit archival description*.
3. **Complete the identity elements.** Enter the title (mandatory), choose the level of description (mandatory), select the repository, and either type your own identifier or click **Generate** after selecting a repository.
4. **Add dates and creators.** Use **Add date** to record each date (type, start/end, or a free-text expression such as "ca. 1900"). Use the creator type-ahead to attach name of creator(s).
5. **Fill in content, access and acquisition sections.** Work down the form completing scope and content, access and reproduction conditions, languages/scripts, custodial history and source of acquisition.
6. **Save.** Submitting the form persists your changes to the description.

Only authenticated users in the **Administrator** or **Editor** group can open the edit form; others are redirected away.

## Tips & FAQ

- **Why does my form look different from a colleague's?** The layout follows the descriptive standard assigned to the record. DACS records use this plugin's layout; ISAD(G), Dublin Core, MODS, and RAD records use their own plugins.
- **The Generate button does nothing.** Select a repository first — the numbering scheme is repository-aware.
- **Can I build a hierarchy here?** Yes. Use the *Add new child levels* block to create child records without leaving the parent.
- **No new settings to configure.** This plugin has no admin settings of its own; it relies on the shared information-object editing infrastructure and the archive numbering scheme.
