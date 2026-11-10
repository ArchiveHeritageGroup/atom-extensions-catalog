---
title: "Training: Authorities and People, Part 1 - Authority Records and Contacts"
subtitle: "Step-by-step guide to browsing authority records, the authority dashboard, external identifiers, and adding contact details that stay with staff"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Authorities and People, Part 1 - Authority Records and Contacts |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 9 November 2026 |
| Prepared for | Archivists who create and maintain authority records |
| Classification | Public |
| Reference | AHG-TRN-PPL-01 |

: Document control

This guide goes with part 1 of the authorities and people training videos. An authority record describes a person, a family or an organisation that created or appears in the records. The guide shows how to find authority records, how the authority dashboard measures how complete they are, how to link a record to Wikidata or VIAF, and how to add contact details. It ends with what a visitor sees, because a person's or a family's contact details are personal information. Allow about 10 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | An editor or administrator. The dashboard is for administrators. |
| Plugins | Actor management (ahgActorManagePlugin), authority (ahgAuthorityPlugin) and contact (ahgContactPlugin), enabled. |
| Completeness scores | Worked out by `php symfony authority:completeness-scan`, run as the web server user. Schedule it weekly by cron; without it the dashboard shows every record as unscored. |
| External lookups | Each source (Wikidata, VIAF, ULAN, LCNAF) is switched on in the authority configuration. |

: What you need before you start

## 1. Browse authority records

Open **Browse > Authority records**. The **Entity type** filter on the left narrows the list to persons, corporate bodies or families, with a count for each. Choose **Family**, then open a record. In the video it is the Van der Berg Family.

## 2. Read the record

The record follows ISAAR(CPF), the international standard for authority records:

| Area | What it holds |
|---|---|
| Identity area | The type of entity and the authorized form of the name |
| Description area | Dates of existence, history, places and functions |
| Contact information | Shown to staff only, for persons and families (see section 6) |
| Control area | Status, level of detail and the sources used |

: Areas of an authority record

## 3. Check completeness on the dashboard

Administrators open the authority dashboard at `/admin/authority/dashboard`. It has no menu entry yet, so bookmark it. It shows how many records have been scored, the average score, and how many records sit at each level: **Stub**, **Minimal**, **Partial** and **Full**. A record's score is built from its ISAAR fields, its external identifiers, its relations to other authorities, the descriptions it is linked to, and its contacts.

The levels tell you where the cataloguing work is. A catalogue where most records are stubs or minimal needs histories, dates and relations added before it needs anything else. The **Quick actions** panel leads on to the work queue, deduplication, the name-recognition pipeline, functions and the configuration.

Scores are not updated live. They change the next time the scan runs.

## 4. Link external identifiers

On the record's page, staff see the link **Add Wikidata, VIAF and other identifiers**, which opens its External identifiers page (`/admin/authority/<id>/identifiers`). **Search external authorities** looks the name up in the sources that are switched on, for example Wikidata and VIAF. Link the match that is the same person, family or organisation, so other catalogues and tools can tell they are one and the same. The **Occupations** page next to it holds structured occupations with dates.

## 5. Add a contact

1. Open the record and choose **Edit**.
2. Open the **Contact information** section.
3. Fill in what you have: contact person, role, email, telephone, address, town, country and a note saying what the contact is for.
4. Tick **Primary contact** if this is the main one. **Add another contact** adds a second.
5. Choose **Save**.

The contact shows in the record's **Contact information** area. The contact page (`/admin/authority/<id>/contact`) lists every contact for the record in one place.

## 6. What visitors see

A person's or a family's contact details are personal information under POPIA, so only signed-in editors and administrators see them. A visitor opening the same record sees no contact information area at all. A record with no entity type set is treated the same way, since it may well be a person.

Organisations (corporate bodies) are different: their contact details are usually public, and visitors see them.

## Recap

| Step | Where |
|---|---|
| Browse by entity type | Browse > Authority records |
| Check completeness | /admin/authority/dashboard |
| Link external identifiers | Add Wikidata, VIAF and other identifiers, on the record |
| Add a contact | Edit > Contact information |
| Contacts of people and families | Staff only |

: Recap

Next, part 2: resolving names to the right authority record, with the evidence for each match.
