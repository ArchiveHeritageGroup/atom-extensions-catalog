# Records in Context (RiC) - Descriptive Standard

## User Guide

Catalogue a record in Records in Context (RiC-O 1.0) the same way you would in ISAD(G), RAD, DACS, MODS or Dublin Core - by choosing it as the record's descriptive standard.

---

## What this is (and what it is not)

There are two RiC features in the system, and it helps to keep them apart.

- The **RiC Explorer** is the graph view - it *visualises* how a record connects to agents, places and other records. It is read-only exploration.
- The **RiC descriptive standard** (this guide) is about *cataloguing*. You pick "Records in Context (RiC)" as a record's standard, and the edit form, the record page, and the export all switch to a RiC-oriented shape - a RiC-O entity type, RiC-O field labels, and typed RiC relations you can add by hand.

A record catalogued in RiC is still an ordinary archival description underneath. Nothing is duplicated or moved; the RiC layer sits on top of the record you already have.

---

## Choosing RiC for a record

RiC appears in the same **Display standard** dropdown as ISAD(G), RAD, DACS, MODS and Dublin Core. Its full label reads *"Records in Context (RiC-O 1.0), International Council on Archives"*.

```
Add / edit archival description
+-------------------------------------------------------------+
| Display standard *                                          |
|  ( ) ISAD(G), 2nd ed.                                        |
|  ( ) RAD, July 2008                                         |
|  ( ) DACS, 2nd ed.                                          |
|  (o) Records in Context (RiC-O 1.0)   <- choose this        |
+-------------------------------------------------------------+
```

**On a new record.** Use **Add > Records in Context** from the main menu, or pick RiC in the Display standard dropdown on the add form. The form reloads into the RiC field set.

**On an existing record.** Open the record for editing and change the **Display standard** dropdown to RiC. The form saves and reloads into the RiC field set, keeping every value you had already entered - a fonds catalogued in ISAD does not lose its title, dates or notes when you switch it to RiC.

**As a child.** On any RiC record's panel there is a **Create RiC child** button. It opens the add form already set to RiC and already parented to the record you were viewing.

---

## The capture form

The RiC edit form carries the full archival field set - Identity, Context, Content and structure, Conditions, Allied materials, Notes - exactly as ISAD does. Nothing an archivist expects is missing. Two things are different.

### 1. A "Records in Context (RiC)" section

Near the top of the form sits a dedicated RiC section with the fields RiC-O has and ISAD does not:

- **RiC-O entity type** - how this record is typed in the ontology: Record, Record Set, Record Part, Record Resource or Instantiation. A fonds is usually a *Record Set*; a single item is usually a *Record*.
- **Authenticity note** (`rico:authenticityNote`) - evidence that the record is what it claims to be.
- **Integrity note** (`rico:integrityNote`) - evidence that it is complete and unaltered.

### 2. Every archival field shows its RiC-O equivalent

So you can see how the description maps into the ontology, each archival field carries a small badge with its RiC-O property. Some values live directly on the record; others - marked "via Instantiation" or "via Activity" - belong to a related entity in RiC-O rather than to the record itself, and the badge says so plainly instead of pretending otherwise.

| Archival field | RiC-O |
|---|---|
| Identifier | `rico:hasOrHadIdentifier` |
| Title | `rico:name` |
| Date(s) | `rico:hasBeginningDate` / `rico:hasEndDate` (via Activity) |
| Level of description | `rico:hasRecordSetType` |
| Extent and medium | `rico:hasExtent` (via Instantiation) |
| Name of creator(s) | `rico:hasCreator` |
| Repository | `rico:hasOrHadHolder` |
| Archival history | `rico:history` |
| Scope and content | `rico:scope` |
| Conditions governing access | `rico:conditionsOfAccess` |
| Conditions governing reproduction | `rico:conditionsOfUse` |
| Language(s) of material | `rico:hasOrHadLanguage` |
| Related units of description | `rico:isAssociatedWithRecordResource` |

You do not have to do anything with the badges - they are guidance. Identifier, Scope and content, and Archival history are captured once, in the ordinary archival fields; the export reads them straight from there.

---

## The record page: the RiC panel

Open a RiC record and a **Records in Context (RiC)** panel appears on the page. It shows, in read-only form for the public and with editing controls for staff:

- the RiC-O entity type and the RiC-specific notes;
- RiC-O relations derived automatically from the description - subjects become `rico:hasOrHadSubject`, places `rico:hasOrHadSpatialCoverage`, genres `rico:hasDocumentaryFormType`, the repository `rico:hasOrHadHolder`, name access points `rico:isAssociatedWith`;
- any **typed RiC relations** you have added by hand (see below);
- an **Export RiC-O (JSON-LD)** button and, where the Explorer is enabled, a **View in graph** link.

Editors also get an inline **Edit RiC** button to change the entity type and the RiC notes without leaving the page.

---

## Typed RiC relations

The derived relations above come from the description for free. Typed RiC relations are the ones you assert deliberately - "this record *has part* that one", "this record *follows* that one", "this record *has provenance* in that agent".

To add one, on the record's RiC panel:

```
Typed RiC relations
  [ rico:hasPart ]  The Smith Correspondence   [x]
  ------------------------------------------------
  ( Has Part          v )  ( Search for a record... )  [ Add ]
```

1. Pick a **relation type** from the dropdown. The list is the 30 RiC-O relation predicates - Has Creator, Has Provenance, Held By, Includes, Has Part, Follows, Documents, and so on.
2. Start typing in the **target** box and choose the record you want to relate to from the suggestions.
3. Click **Add**. The relation appears in the list immediately.

To remove one, click the small **x** next to it.

Each relation is stored as a proper archival relationship with a RiC-O predicate attached, so it flows straight into the JSON-LD export and the graph.

---

## Exporting RiC-O

The **Export RiC-O (JSON-LD)** button (also reachable at `/ricManage/export/<record>`) returns the record as RiC-O JSON-LD: the entity type, the RiC-specific notes, the identifier/scope/history read from the archival fields, the derived subject/place/holder/genre/name relations, and your typed relations. It is a standards-clean serialisation you can hand to any RiC-O consumer.

---

## Tips

- Switching a record's standard never deletes data - it only changes which fields the form presents. You can move a record between ISAD and RiC freely.
- The RiC panel only shows on records whose standard is RiC (or that already carry RiC metadata). Ordinary records are unaffected.
- Editing and adding relations is limited to editors and administrators. The public sees the panel read-only.
