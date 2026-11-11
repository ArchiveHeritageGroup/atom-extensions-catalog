---
title: "Training: Data Entry and Workflow, Part 1 - Data-Entry Forms"
subtitle: "Step-by-step guide to copying a form template, adjusting it in the form builder, assigning it to a repository and describing records with it"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Data Entry and Workflow, Part 1 - Data-Entry Forms |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 10 November 2026 |
| Prepared for | Archivists, cataloguers and catalogue managers |
| Classification | Public |
| Reference | AHG-TRN-DATA-01 |

: Document control

This guide goes with part 1 of the data entry and workflow training videos. A data-entry form shows only the fields a team needs, in the order they work, with help text and default values. Behind each field is a mapping to the place in the catalogue where its value is saved, so a record described with a form is an ordinary archival description. Allow about 15 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | An administrator to build and assign forms. Anyone who can add descriptions can use a form. |
| Plugin | Forms (ahgFormsPlugin), enabled. |
| Version | Plugins v3.121.181 or later. Before it, the form showed its HTML as text, Clone gave an error, records saved from a form could not be opened, and several builder fields were never saved. |

: What you need before you start

## 1. The templates

Open **Admin > Form templates** (`/admin/forms`). The dashboard shows the number of templates, active assignments, drafts and recent submissions. **Manage templates** lists them:

| Template | For |
|---|---|
| ISAD-G Minimal | The eight essential ISAD(G) fields |
| ISAD-G Full | All ISAD(G) elements across the seven areas |
| Dublin Core Simple | The fifteen Dublin Core elements |
| Accession Standard | Accession registration |
| Photo Collection Item | Photographs |

: System templates

System templates cannot be changed or deleted. Start from a copy.

## 2. Copy a template

Choose the **Clone** button on a template. Enter a name for the copy and choose **Clone template**. All fields are copied with their mappings, and the copy opens in the form builder. The original is not changed.

## 3. The form builder

The builder has three panels: the fields you can add on the left, the form in the middle and the selected field's properties on the right.

- **Add a field:** click it in the left panel, or drag it onto the form. The **AtoM fields** (title, identifier, level, scope and content, extent, dates, creators, subjects) come with their mapping already set.
- **Change a field:** select it in the form. Change its label, help text, placeholder or **default value**, or make it required or read-only. Choose **Save**.
- **Reorder:** drag fields up or down in the form.
- **Remove:** the bin button on the field.

A default value fills in the field on every new record, for example "1 volume" for extent when a series is all single volumes.

## 4. Assign the form

Open **Assignments** and choose **Create assignment**:

| Field | Meaning |
|---|---|
| Form template | The form to use |
| Repository | Use it for records in this repository; empty means all |
| Level of description | Use it for this level only; empty means all |
| Priority | When several assignments match, the highest priority wins |
| Inherit to child records | Use it for descriptions below these too |

: Assignment settings

New descriptions added under a matching parent in the standard editor also get the form's default values.

## 5. Describe a record with the form

In the template list, choose **Use form** on your template. Fill in the fields:

- Level of description and repository are chosen from lists.
- Creators and subjects suggest names and terms already in the catalogue as you type; choose one so it links to the existing record.
- Dates take a start and an end date.

Choose **Save record**. The description is created as a **draft** at the top level of the catalogue, with its creator, dates, level and repository in place. Check it, move it under its collection if needed, and publish it in the usual way.

To change a record later through its form, open `/forms/edit/informationobject/<id>`. The form loads the record's current values, and saving updates them; it does not add second dates or creators.

## Recap

| Step | Where |
|---|---|
| Copy a template | Form templates, Clone |
| Add fields and defaults | Form builder |
| Decide where it applies | Assignments, Create assignment |
| Describe a record | Template list, Use form |

: Recap

Next in this series: part 2, approval workflow - tasks, pools and claiming.
