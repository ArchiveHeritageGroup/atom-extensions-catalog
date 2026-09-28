# Storage Management User Guide

## A Guide for Archivists

---

## What is it?

The AHG Storage Manage plugin (`ahgStorageManagePlugin`) provides a fast, high-performance way to browse, search and manage **physical storage locations** (physical objects) in AtoM/Heratio, built on the Laravel Query Builder. It also adds an optional **Strongroom** feature for tracking storage spaces, their capacity, and which physical objects are assigned to them.

It works alongside the standard AtoM physical-storage screens, replacing the browse, autocomplete, box-list and holdings-report-export behaviour with a faster implementation.

## Key features

- **Physical storage browse** with inline text search across name, location and type.
- **Sorting** by name or location, ascending or descending (`nameUp`, `nameDown`, `locationUp`, `locationDown`).
- **Autocomplete** for picking physical objects by name.
- **Box list** view showing the descriptions linked to a physical object.
- **Holdings report export** — a background job producing a CSV report.
- **Strongroom space allocation** - create strongrooms, record their capacity (linear meters, shelves, boxes or cubic meters), assign physical objects, and see used vs. remaining capacity.
- **Storage locations** - a hierarchy of places (building, floor, room, aisle, bay, rack, shelf, container, storage unit), so a shelf sits inside a room inside a building rather than in a single free-text field.
- **Movement log** - an append-only record of every move: what moved, where from, where to, when, by whom and why.
- **Bulk relocation** - move many objects to a new location in one action, recorded as one batch.

## How to use it

**Browse physical storage** — go to `/physicalobject/browse`. Type in the search box to filter by name, location or type, and use the sort controls to reorder. A global search (`?query=...`) is automatically applied as a sub-search.

**View boxes / linked descriptions** — `/physicalobject/boxList` lists the information objects (descriptions) attached to a physical object.

**Add / edit a physical object** — use the standard physical-object edit form. You can set the **name**, **location** and **type**. If strongrooms are installed, the edit form also lets you assign the object to a strongroom (with a size used) or unassign it.

**Delete a physical object** — the delete screen shows any linked descriptions before you confirm.

**Export a holdings report** — go to `/physicalobject/holdingsReportExport`. Choose what to include (empty locations, descriptions, accessions). Submitting starts a background job; a notice links you to the **Jobs management** page where you can download the result once complete.

### Strongrooms

- **Browse strongrooms:** `/strongroom/browse` — lists rooms with occupant count and used capacity; search with `?q=`.
- **View a strongroom:** `/strongroom/<slug>` — shows used units, remaining capacity and the list of occupant physical objects.
- **Add a strongroom:** `/strongroom/add` — enter name (required), location description, capacity value, capacity unit and notes.
- **Edit:** `/strongroom/<slug>/edit` — the slug stays fixed even if you rename the room.
- **Assign an object:** `/strongroom/<slug>/assign` — enter the physical object's slug and the size it uses. If this exceeds capacity, the save still succeeds but you get an over-capacity warning.
- **Unassign:** posted from the occupant list on the strongroom page.

## Storage locations

**Browse** - Manage > Storage Locations, or `/storageLocation/browse`. The sidebar shows the hierarchy; the list can be filtered by text or by type.

**Add a location** - Add new. A location needs a **name** and a **type**. Choosing a **parent** puts it inside another location: pick the room to create a shelf in it. Leave the parent empty for a top-level location such as a building.

**Move a location** - edit it and change its parent. Everything underneath moves with it, and the move is written to the movement log. Clearing the parent moves it back to the top level.

**Delete a location** - only possible when it is empty. A location is refused if it has child locations, still holds objects, or appears in the movement log. The history outlives the shelf, deliberately: deleting a location must not erase the record of what passed through it.

## Moving things, and the record of it

Open a location to see **Objects in this location**. Administrators get a checkbox beside each one, a destination list, and a box for the reason.

**To move objects:** tick them, choose the destination, type why, and press Move. Choosing **Out of storage** records that they left storage altogether, which is what you want for material sent for conservation or returned to a depositor.

Everything selected moves as one batch, so a relocation cannot half happen. Objects already in the destination are skipped rather than recorded as moves that did not take place.

**Recent movements** below the list shows the last twenty moves in or out of this location: when, what, from, to, who did it and why.

The log is append-only. A move entered wrongly is corrected by making another move, never by editing history - a record that can be quietly rewritten proves nothing about where the holdings have been. Each entry also keeps a snapshot of the names involved, so it still reads sensibly after a location is renamed or a staff account is deleted.

## Administration / settings

- **Permissions:** Strongroom *browse* and *show* are public; *create, edit, delete, assign* and *unassign* require the **administrator** credential.
- **Storage locations:** browse, view and the JSON endpoints are public; *create, edit, delete* and *move objects* require the **administrator** credential.
- **Capacity units** are fixed to: Linear meters, Shelves, Boxes, Cubic meters.
- A strongroom **cannot be deleted while it still has occupants** — move or unassign them first.

## Tips & FAQ

- **Why can't I delete a strongroom?** It still has assigned physical objects; unassign them first.
- **The export looks empty.** Make sure you ticked at least one option (empty/descriptions/accessions) — otherwise the export is rejected with a prompt.
- **Capacity warnings** never block a save; they just alert you that the room is over capacity.
- **Why can't I delete a storage location?** It has children, still holds objects, or appears in the movement log. Move the contents out first; a location that has history cannot be deleted at all.
- **Can I correct a move I recorded wrongly?** Record the correct move. The log never changes what it already says.
- **Slugs** are how you reference objects when assigning — copy the slug from the physical object's page.
