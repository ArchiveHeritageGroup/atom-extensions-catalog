---
title: "Training: Authorities and People, Part 2 - Resolving Names to Authority Records"
subtitle: "Step-by-step guide to the authority resolution queue: reading a name in its context, weighing the candidates and their evidence, and linking, parking or rejecting"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Authorities and People, Part 2 - Resolving Names to Authority Records |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 9 November 2026 |
| Prepared for | Archivists who link names in descriptions to authority records |
| Classification | Public |
| Reference | AHG-TRN-PPL-02 |

: Document control

This guide goes with part 2 of the authorities and people training videos. Name recognition finds the people, organisations and places mentioned in your descriptions. The authority resolution engine takes each name, finds the authority records it could be, scores them against the evidence around the name, and puts the result in front of an archivist. Nothing is linked automatically: every link is an archivist's decision, and every decision is recorded with what was on screen when it was made. Allow about 15 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | An editor. The lookup settings page is for administrators. |
| Plugin | Authority resolution (ahgAuthorityResolutionPlugin), enabled, with the actor management and AI plugins it depends on. |
| Names | Extracted by the AI plugin's name recognition, then promoted into the review queue. |
| External sources | Optional. VIAF, Wikidata, GeoNames and others are off until an administrator enables them under **Lookup settings**; until then no outside service is called. |

: What you need before you start

## 1. The review queue

Open the queue at `/admin/authorityResolution` (AHG Plugins > Authority Resolution). The counts at the top show how many mentions are pending, linked, parked, rejected and turned into new records. Filter by **entity type** (PERSON, ORG, GPE, LOC, PLACE), by **state**, or by object, and use **Assign** to hand mentions to an archivist.

Each row is one name found in one description. The same person named in five descriptions appears five times, because each mention is decided in its own context.

## 2. Read the name in its context

Choose **Review** on a row. The left column shows:

| Panel | What it tells you |
|---|---|
| Source mention | The name as found, the description it came from, and the name recognition's confidence |
| Context window | The sentence around the name, with the name highlighted. **View full context** and **View full document text** show more. |
| Co-occurring entities | Other names near this one, with their distance in characters |
| Nearby places and dates | Places and dates near the name |

: The context panels

## 3. Weigh the candidates

The middle column lists the authority records the name could be, ranked by score. Each card shows the name similarity, the composite score, and one row per kind of evidence:

| Evidence | For people and organisations |
|---|---|
| Temporal | Do the record's dates fit the dates near the mention? |
| Geographic | Do the record's places appear near the mention? |
| Relational | Is the record related to the other names nearby? |
| Role | Do words about a role or office near the name fit the record? |
| Conflict | Is there a contradiction, such as a person record for a name tagged as an organisation? |

: Evidence for each candidate

Each row reads **Match**, **Conflict**, **Silent** (no bearing either way) or **Absent** (no data to compare). Places are scored on their own dimensions: hierarchy, document, co-occurrence, conflict and scale.

In the video, "Frederick Douglass" has two candidates. The first matches the name exactly but has no dates or history. The second, "Frederick Douglass, 1818-1895", scores a little lower on the name, but its geographic evidence matches places named in the description, and it is the fuller record.

## 4. Decide

The right column holds the five decisions:

| Decision | When |
|---|---|
| Link (top candidate) | The first candidate is right. |
| Link to this (on a candidate card) | A lower-ranked candidate is right. |
| Link to different | The right record is not in the list: search for it. |
| Create new authority record | The name is real but no record exists. The form is pre-filled from the context and any enabled external sources. |
| Park | You cannot decide yet. A reason is required. |
| Reject | The name recognition was wrong. A reason is required. |

: The decisions

After a decision the screen moves on to the next pending mention.

**Park** takes the mention out of the queue but keeps it open. Parked mentions are listed at `/admin/authorityResolution/park`, with who parked them, when and why, and are flagged when new candidates appear. **Un-park & re-review** puts one back.

**Reject** marks the mention as not a real entity of that type, for example "England" tagged as a person. The rejection and its reason are kept as feedback for training the name recognition.

## 5. What is recorded

Each decision adds a row that is never changed afterwards. It holds who decided, when, the candidate chosen, the top score the system gave, and a snapshot of the candidate list and evidence as they were on screen. A link also records the authority record against the extracted name. The decision is written as provenance to the triplestore as well. To change a decision, record a new one; the latest decision sets the mention's state, and the earlier one stays in the history.

Deciding does not change the description itself.

## Recap

| Step | Where |
|---|---|
| Open the queue and filter | /admin/authorityResolution |
| Read the context | Left column of the review screen |
| Weigh the evidence | Candidate cards |
| Link, park or reject | Decisions column |
| Revisit parked mentions | /admin/authorityResolution/park |

: Recap

Next, part 3: donors, and donor agreements with reminders.
