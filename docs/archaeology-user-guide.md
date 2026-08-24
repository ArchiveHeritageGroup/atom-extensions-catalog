# Archaeological Stratigraphy and the Harris Matrix

## A Guide for Archaeologists and Archivists

## What is it?

The AHG Archaeology plugin records an excavation the way it is actually dug, and keeps it inside the catalogue rather than beside it. It adds **sites**, **stratigraphic contexts**, **relationships between contexts**, and **finds**, then draws the **Harris Matrix** from what has been recorded.

The reason it exists is a mismatch. An archival catalogue is a hierarchy: a fonds, a series, a file, each with exactly one parent. Stratigraphy is not. One context can lie beneath several others at once, and two contexts dug in different trenches can turn out to be the same feature. That is a directed graph, and it will not fold into a tree.

So the plugin keeps both. Every context is a full archival description in its own right, catalogued, searchable, access-controlled, with its photographs attached. The stratigraphic relationships live alongside them, and the matrix is computed from those relationships every time it is drawn. Nothing is duplicated, and the sequence is never flattened to fit the hierarchy.

Everything is behind a login. Site coordinates and unpublished excavation records are exactly the material that should not be browsable anonymously, and a context record can identify the position of a burial.

## Key features

- **Sites** with location, period, site type, excavator, permit number and positional accuracy.
- **Contexts** with type, phase, top and bottom elevations, trench and spit references, excavator, dates and interpretation.
- **Nine relationship types**, each recorded once and mirrored automatically: `above` and `below`, `cuts` and `is cut by`, `fills` and `is filled by`, and the symmetric `is the same as`, `bonds with` and `abuts`.
- **Harris Matrix**, drawn latest at the top and earliest at the bottom, with correlated contexts merged into a single node.
- **Finds** tied to the context they came from, which is what turns a box of objects into an assemblage.
- **Dig plan** with a scaled section per trench and a locator drawn from the recorded coordinate.
- **Context sheets** as printable PDFs.
- **Consistency checks** that report contradictions in the record.
- **Import and export** in the formats other archaeological software already uses.

## How to use it

Start from **Archaeology** in the main menu, then choose a site, or add one.

**Recording contexts.** Open a site and choose *Stratigraphy and Harris Matrix*, then *Add context*. A context number is the only thing required. Everything else can follow as the dig proceeds.

**Recording relationships.** Open a context and record what it lies above, below, cuts or fills. You only ever record one side: if you say 1003 cuts 1002, the plugin writes "1002 is cut by 1003" for you. It will also refuse a relationship that would create a loop, because a context cannot be both earlier and later than another.

**Reading the matrix.** The matrix shows **only immediate relationships**, as Harris's method requires. If you have recorded that 1001 is above 1002, 1002 is above 1005, and also that 1001 is above 1005, the third is implied by the first two and is not drawn. Nothing is deleted, and the page tells you how many were suppressed, so a smaller diagram can never be mistaken for lost data.

Contexts recorded as the same feature appear in one box, joined with an equals sign.

## Consistency checks

Above the matrix the plugin reports contradictions it can find in the record. It is deliberately cautious, because a check that cries wolf on ordinary excavation messiness gets switched off and then catches nothing.

It looks for stratigraphic loops, contexts with no relationships at all, a sequence that has split into unconnected pieces, contexts recorded as both the same feature and one above the other, elevations that contradict a superposition, and phase assignments that disagree with the sequence.

The phase check does not assume which way your phase numbers run. Some sites number the earliest phase 1, others the latest. It works out the convention from your own data and reports only the relationships that disagree with it.

## Importing and exporting

**Export** offers three formats: a **data package** following the table schema used by the Harris Matrix Data Package, **GraphViz DOT** for redrawing the diagram elsewhere, and **Phaser CSV** for the MATRIX project's analysis tool.

**Import** accepts contexts as a spreadsheet, and relationships either as Phaser CSV or as an **LST file**, the format written by BASP Harris, Stratify and ArchEd. That means a dig archive recorded in older software can bring its stratigraphy with it instead of leaving it behind.

Import contexts before relationships. A relationship naming a context this site does not have is reported, never invented. Running the same file twice is safe: it will tell you what was already recorded rather than adding it again.

One relationship is deliberately not imported. LST files carry `contemporary_with`, meaning units of the same period that are not physically joined. The nearest types here both assert physical contact, so mapping it would record an observation nobody made. The count and the reason appear on screen.

## Administration and settings

Access requires a login. Browsing and viewing need the `contributor` credential or above; editing, deleting and importing need `editor` or administrator.

Site types, periods, context types, phases, object types and materials are all ordinary AtoM taxonomies, so an institution can extend them without code changes.

## Tips and FAQ

**Why is my matrix smaller than my list of relationships?** Because it draws only immediate ones. The count of suppressed relationships is shown with the matrix.

**Why will it not let me record a relationship?** Either it would create a loop, or the two contexts are already related that way.

**Can a context belong to two trenches?** Record them as separate contexts and relate them with *is the same as*. They will merge into one node in the matrix while remaining two records.

**Where do the coordinates come from?** From the site record. No map tiles are loaded, so the locator is drawn from the coordinate itself and nothing is sent to an external map service.
