# Extended Rights Management

## User Guide

Manage copyright, licensing, access restrictions, and cultural heritage labels for your archival records.

---

## Workflow Overview
```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Select     │    │   Choose     │    │   Set        │    │   Apply      │
│   Record     │ ──▶│   Rights     │ ──▶│   Details    │ ──▶│   & Save     │
│              │    │   Type       │    │              │    │              │
│ Find item    │    │ Copyright    │    │ Dates        │    │ Record       │
│ to manage    │    │ License      │    │ Holder       │    │ updated      │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

---

## What Extended Rights Manages
```
┌─────────────────────────────────────────────────────────────┐
│                    EXTENDED RIGHTS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📜 RIGHTS STATEMENTS                                       │
│     Standard copyright status indicators                    │
│     (In Copyright, No Copyright, Unknown, etc.)             │
│                                                             │
│  🅭 CREATIVE COMMONS                                        │
│     Open licenses for sharing and reuse                     │
│     (CC BY, CC BY-SA, CC BY-NC, CC0, etc.)                 │
│                                                             │
│  🔒 EMBARGO                                                 │
│     Temporary access restrictions                           │
│     (Closed until specific date)                            │
│                                                             │
│  🏷️  TRADITIONAL KNOWLEDGE LABELS                           │
│     Indigenous community protocols                          │
│     (TK Labels from Local Contexts)                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## How to Access
```
Option A: From a Record                Option B: From Admin
───────────────────────                ────────────────────
                                       
  View Archival Description              Main Menu
         │                                   │
         ▼                                   ▼
  Scroll to "Rights" section             Admin
         │                                   │
         ▼                                   ▼
  Click "Add Extended Rights"            Rights Dashboard
         │                                   │
         ▼                                   ▼
  Extended Rights Form                   Overview of all rights
```

---

## Part 1: Rights Statements

### What Are Rights Statements?

Rights Statements are standardised indicators that tell users what they can do with a digital object.
```
┌─────────────────────────────────────────────────────────────┐
│ RIGHTS STATEMENTS CATEGORIES                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🔴 IN COPYRIGHT                                            │
│     ├── In Copyright                                        │
│     ├── In Copyright - Educational Use Permitted            │
│     ├── In Copyright - EU Orphan Work                       │
│     ├── In Copyright - Non-Commercial Use Permitted         │
│     └── In Copyright - Rights-holder Unlocatable            │
│                                                             │
│  🟢 NO COPYRIGHT                                            │
│     ├── No Copyright - Contractual Restrictions             │
│     ├── No Copyright - Non-Commercial Use Only              │
│     ├── No Copyright - Other Known Legal Restrictions       │
│     └── No Copyright - United States                        │
│                                                             │
│  🟡 OTHER                                                   │
│     ├── Copyright Not Evaluated                             │
│     ├── Copyright Undetermined                              │
│     └── No Known Copyright                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Choosing a Rights Statement
```
                    Is copyright status known?
                           │
              ┌────────────┴────────────┐
              │                         │
             YES                        NO
              │                         │
              ▼                         ▼
      Is item in copyright?      ┌─────────────┐
              │                  │ Copyright   │
     ┌────────┴────────┐        │ Not         │
     │                 │        │ Evaluated   │
    YES               NO        └─────────────┘
     │                 │
     ▼                 ▼
┌──────────┐    ┌──────────┐
│   In     │    │   No     │
│Copyright │    │Copyright │
│(choose   │    │(choose   │
│ subtype) │    │ subtype) │
└──────────┘    └──────────┘
```

---

## Part 2: Creative Commons Licenses

### Understanding CC Licenses
```
┌─────────────────────────────────────────────────────────────┐
│ LICENSE        │ MEANING                                    │
├────────────────┼────────────────────────────────────────────┤
│                │                                            │
│  CC0           │ No rights reserved (public domain)         │
│                │ Anyone can use for any purpose             │
│                │                                            │
│  CC BY         │ Credit must be given                       │
│                │ Commercial use allowed                     │
│                │                                            │
│  CC BY-SA      │ Credit + Share alike                       │
│                │ Derivatives must use same license          │
│                │                                            │
│  CC BY-NC      │ Credit + Non-commercial only               │
│                │ No commercial use                          │
│                │                                            │
│  CC BY-NC-SA   │ Credit + Non-commercial + Share alike      │
│                │ Strictest open license                     │
│                │                                            │
│  CC BY-ND      │ Credit + No derivatives                    │
│                │ Cannot modify or remix                     │
│                │                                            │
│  CC BY-NC-ND   │ Credit + Non-commercial + No derivatives   │
│                │ Most restrictive CC license                │
│                │                                            │
└────────────────┴────────────────────────────────────────────┘
```

### Which License to Choose?
```
         Do you want to allow commercial use?
                        │
              ┌─────────┴─────────┐
              │                   │
             YES                  NO
              │                   │
              ▼                   ▼
    Allow modifications?    Allow modifications?
              │                   │
      ┌───────┴───────┐    ┌──────┴──────┐
      │       │       │    │      │      │
     YES  SHARE-ALIKE NO  YES    SA     NO
      │       │       │    │      │      │
      ▼       ▼       ▼    ▼      ▼      ▼
   ┌────┐ ┌──────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐
   │BY  │ │BY-SA │ │BY- │ │BY- │ │BY- │ │BY- │
   │    │ │      │ │ND  │ │NC  │ │NC- │ │NC- │
   │    │ │      │ │    │ │    │ │SA  │ │ND  │
   └────┘ └──────┘ └────┘ └────┘ └────┘ └────┘
```

---

## Part 3: Embargo Management

### What is an Embargo?

An embargo restricts access to a record until a specific date.
```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   EMBARGO TIMELINE                                          │
│                                                             │
│   Today           Embargo End        After Embargo          │
│     │                 │                   │                 │
│     ▼                 ▼                   ▼                 │
│   ━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶      │
│                       │                                     │
│   🔒 RESTRICTED       │   🔓 OPEN ACCESS                    │
│   • Hidden from       │   • Visible to all                  │
│     public search     │   • Searchable                      │
│   • Staff access      │   • Downloadable                    │
│     only              │                                     │
│                       │                                     │
└─────────────────────────────────────────────────────────────┘
```

### Setting an Embargo
```
┌─────────────────────────────────────────────────────────────┐
│ SET EMBARGO                                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Record:        ABC/001/005 - Personal Correspondence       │
│                                                             │
│  Embargo Type:  [ Time-based           ▼]                   │
│                 ┌─────────────────────────┐                 │
│                 │ Time-based              │                 │
│                 │ Death + Years           │                 │
│                 │ Donor Restriction       │                 │
│                 │ Legal Hold              │                 │
│                 └─────────────────────────┘                 │
│                                                             │
│  Start Date:    [ 01/01/2020  📅]                          │
│                                                             │
│  End Date:      [ 01/01/2050  📅]  ← Access opens           │
│                                                             │
│  Reason:        [Personal information - 30 year closure___] │
│                                                             │
│  Exceptions:    ☐ Allow researcher access with approval     │
│                 ☐ Allow staff access                        │
│                 ☐ Show metadata only                        │
│                                                             │
│                              [ Cancel ]  [ Apply Embargo ]  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Embargo Status Dashboard
```
┌─────────────────────────────────────────────────────────────┐
│ EMBARGO OVERVIEW                                            │
├──────────────────┬──────────────────┬───────────────────────┤
│                  │                  │                       │
│   ACTIVE         │  EXPIRING SOON   │   EXPIRED             │
│   EMBARGOES      │  (next 90 days)  │   (review needed)     │
│                  │                  │                       │
│      47          │       5          │       12              │
│    records       │    records       │     records           │
│                  │     ⚠️            │                       │
│                  │                  │                       │
└──────────────────┴──────────────────┴───────────────────────┘

EXPIRING SOON:
┌─────────────────────────────────────────────────────────────┐
│ Reference    │ Title              │ Expires    │ Action    │
├──────────────┼────────────────────┼────────────┼───────────┤
│ ABC/001/005  │ Smith Letters      │ 15 Feb 26  │ [Review]  │
│ DEF/003/012  │ Board Minutes 1995 │ 28 Feb 26  │ [Review]  │
│ GHI/007/001  │ Personnel File     │ 01 Mar 26  │ [Review]  │
└──────────────┴────────────────────┴────────────┴───────────┘
```

---

## Part 4: Traditional Knowledge Labels

### What Are TK Labels?

TK Labels are designed by indigenous communities to indicate cultural protocols for using traditional knowledge and cultural heritage materials.
```
┌─────────────────────────────────────────────────────────────┐
│ TK LABEL CATEGORIES                                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🔵 PROVENANCE                                              │
│     TK Attribution     - Credit this community              │
│     TK Family          - Family ownership                   │
│     TK Clan            - Clan ownership                     │
│                                                             │
│  🟢 PROTOCOLS                                               │
│     TK Community Voice - Community should be consulted      │
│     TK Culturally Sensitive - Handle with care              │
│     TK Secret/Sacred   - Restricted viewing                 │
│                                                             │
│  🟡 PERMISSIONS                                             │
│     TK Non-Commercial  - No commercial use                  │
│     TK Verified        - Community verified                 │
│     TK Open to Collaboration - Welcomes engagement          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Applying TK Labels
```
┌─────────────────────────────────────────────────────────────┐
│ ADD TRADITIONAL KNOWLEDGE LABELS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Record:  ABC/009/003 - Traditional Healing Practices       │
│                                                             │
│  Select applicable labels:                                  │
│                                                             │
│  ☑ TK Attribution                                           │
│    Credit: [Ndebele Community Council______________]        │
│                                                             │
│  ☑ TK Culturally Sensitive                                  │
│    Note:  [Contains sacred ceremonial information__]        │
│                                                             │
│  ☑ TK Non-Commercial                                        │
│    Note:  [May not be used for commercial purposes_]        │
│                                                             │
│  ☐ TK Secret/Sacred                                         │
│  ☐ TK Community Voice Only                                  │
│  ☐ TK Family                                                │
│                                                             │
│                              [ Cancel ]  [ Apply Labels ]   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Adding Extended Rights to a Record

### Complete Workflow
```
                         START
                           │
                           ▼
              ┌────────────────────────┐
              │  View archival record  │
              │  Click "Edit Rights"   │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │  Select Rights Type    │
              │  (can choose multiple) │
              └───────────┬────────────┘
                          │
        ┌─────────┬───────┴───────┬─────────┐
        │         │               │         │
        ▼         ▼               ▼         ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
   │ Rights  │ │Creative │ │ Set     │ │   TK    │
   │Statement│ │Commons  │ │Embargo  │ │ Labels  │
   └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘
        │           │           │           │
        └─────────┬─┴───────────┴───────────┘
                  │
                  ▼
        ┌────────────────────────┐
        │  Add Rights Holder     │
        │  (name, contact, URI)  │
        └───────────┬────────────┘
                    │
                    ▼
        ┌────────────────────────┐
        │  Set Dates             │
        │  • Effective from      │
        │  • Expires on          │
        └───────────┬────────────┘
                    │
                    ▼
        ┌────────────────────────┐
        │  Add Notes             │
        │  (any special terms)   │
        └───────────┬────────────┘
                    │
                    ▼
        ┌────────────────────────┐
        │        SAVE            │
        └───────────┬────────────┘
                    │
                    ▼
              ┌───────────┐
              │  COMPLETE │
              │  Rights   │
              │  Applied  │
              └───────────┘
```

---

## Extended Rights Form
```
┌─────────────────────────────────────────────────────────────┐
│ EXTENDED RIGHTS                                     [Save]  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Record: ABC/001/012 - Photograph Album 1935                │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  COPYRIGHT STATUS                                           │
│                                                             │
│  Rights Statement:  [ In Copyright              ▼]          │
│                                                             │
│  Creative Commons:  [ CC BY-NC (Attribution-   ▼]          │
│                       Non-Commercial)                       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  RIGHTS HOLDER                                              │
│                                                             │
│  Name:              [Smith Family Trust_________]           │
│  Contact:           [trust@smithfamily.co.za____]           │
│  URI:               [___________________________ ]          │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  DATES                                                      │
│                                                             │
│  Effective From:    [ 01/01/1935  📅]                      │
│  Expires On:        [ 01/01/2035  📅]  (70 years after)    │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  EMBARGO (Optional)                                         │
│                                                             │
│  ☐ Apply embargo    End Date: [___________📅]              │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  TK LABELS (Optional)                                       │
│                                                             │
│  ☐ TK Attribution   ☐ TK Culturally Sensitive              │
│  ☐ TK Non-Commercial ☐ TK Secret/Sacred                    │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  NOTES                                                      │
│                                                             │
│  [Permission granted for non-commercial research use.     ] │
│  [Contact rights holder for publication permissions.      ] │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Rights Display on Record
```
┌─────────────────────────────────────────────────────────────┐
│ 📜 RIGHTS INFORMATION                                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 🔴 IN COPYRIGHT                                      │   │
│  │    This item is protected by copyright.              │   │
│  │                                                      │   │
│  │    Rights Holder: Smith Family Trust                 │   │
│  │    Expires: 01 January 2035                          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 🅭 CC BY-NC                                          │   │
│  │    Attribution-NonCommercial 4.0 International       │   │
│  │                                                      │   │
│  │    You may share and adapt this work for non-        │   │
│  │    commercial purposes with attribution.             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 🏷️ TK ATTRIBUTION                                    │   │
│  │    Credit: Ndebele Community Council                 │   │
│  │                                                      │   │
│  │    Please acknowledge the community when using       │   │
│  │    this material.                                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Quick Reference
```
┌─────────────────────────────────────────────────────────────┐
│  TASK                      │  HOW TO DO IT                  │
├────────────────────────────┼────────────────────────────────┤
│  Add rights to record      │  View record → Edit Rights     │
│  View embargo dashboard    │  Admin → Rights → Embargoes    │
│  Export rights data        │  Admin → Rights → Export       │
│  Check expiring embargoes  │  Admin → Rights → Expiring     │
│  Apply TK labels           │  Edit Rights → TK Labels tab   │
│  Bulk update rights        │  Admin → Rights → Batch Update │
└────────────────────────────┴────────────────────────────────┘
```

---

## Tips for Best Practice
```
┌─────────────────────────────────────────────────────────────┐
│  ✓ DO                          │  ✗ DON'T                  │
├────────────────────────────────┼────────────────────────────┤
│  Research copyright status     │  Guess at rights status   │
│  Record rights holder contact  │  Leave holder blank       │
│  Set expiry dates              │  Use indefinite embargoes │
│  Consult communities for TK    │  Apply TK labels alone    │
│  Review embargoes regularly    │  Forget expiring items    │
│  Document your decisions       │  Skip the notes field     │
└────────────────────────────────┴────────────────────────────┘
```

---

## Part 5: CLI Commands (System Administrators)

For system administrators, the plugin provides command-line tools for automated embargo management.

### Automated Embargo Processing
```
┌─────────────────────────────────────────────────────────────┐
│  EMBARGO:PROCESS - Automated Daily Processing               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Process all (lift expired + send notifications):           │
│  $ php symfony embargo:process                              │
│                                                             │
│  Preview without making changes:                            │
│  $ php symfony embargo:process --dry-run                    │
│                                                             │
│  Send notifications only:                                   │
│  $ php symfony embargo:process --notify-only                │
│                                                             │
│  Lift expired embargoes only:                               │
│  $ php symfony embargo:process --lift-only                  │
│                                                             │
│  Custom warning intervals:                                  │
│  $ php symfony embargo:process --warn-days=14,7,3           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Cron Setup
```
┌─────────────────────────────────────────────────────────────┐
│  RECOMMENDED CRON CONFIGURATION                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Run daily at 6am to:                                       │
│  • Automatically lift expired embargoes                     │
│  • Send expiry warning notifications (30, 7, 1 days)        │
│                                                             │
│  Add to crontab:                                            │
│  0 6 * * * cd /usr/share/nginx/archive && \                 │
│            php symfony embargo:process                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Embargo Reports
```
┌─────────────────────────────────────────────────────────────┐
│  EMBARGO:REPORT - Generate Reports                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Summary statistics:                                        │
│  $ php symfony embargo:report                               │
│                                                             │
│  List all active embargoes:                                 │
│  $ php symfony embargo:report --active                      │
│                                                             │
│  List embargoes expiring in N days:                         │
│  $ php symfony embargo:report --expiring=30                 │
│                                                             │
│  List recently lifted embargoes:                            │
│  $ php symfony embargo:report --lifted --days=7             │
│                                                             │
│  List expired but not lifted:                               │
│  $ php symfony embargo:report --expired                     │
│                                                             │
│  Export as CSV:                                             │
│  $ php symfony embargo:report --active --format=csv \       │
│                               --output=/tmp/report.csv      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Report Output Example
```
$ php symfony embargo:report

=== Embargo Status Report ===

Summary Statistics:
  Total Active Embargoes:    47
  Expiring in 30 days:        5
  Expired (not lifted):      12
  Lifted (last 30 days):      8

Embargo Types:
  Full:           23 (49%)
  Metadata Only:  12 (26%)
  Digital Only:    8 (17%)
  Partial:         4 (8%)

Top Embargo Reasons:
  1. Donor Restriction    18
  2. Privacy              14
  3. Copyright             9
  4. Legal                 6
```

---

## Troubleshooting
```
Problem                          Solution
───────────────────────────────────────────────────────────
Can't find rights option      →  Check you have edit permission
                                 May need administrator access
                                 
Embargo not working           →  Check start/end dates
                                 Verify record is published
                                 Clear cache
                                 
TK labels not showing         →  Labels may need approval
                                 Check community settings
                                 
Rights statement missing      →  Administrator may need to
                                 enable vocabulary
                                 
CC license not in list        →  Check license is active
                                 Contact administrator
```

---

## Need Help?

Contact your system administrator if you experience issues.

For more information on standards:
- Rights Statements: https://rightsstatements.org
- Creative Commons: https://creativecommons.org
- TK Labels: https://localcontexts.org

---

## Retention Schedule & Disposal Workflow (v1.3.0, May 2026)

This release adds File-Plan-driven **retention scheduling** and a **multi-stage disposal workflow** with audit dual-write. Designed for any records-management environment that requires configuration per a published File Plan, automated/manual retention enforcement, and controlled disposal workflows with audit logs — including NARSSA, ISO 15489, PRO Act (UK), NARA (US), and equivalent national archives regimes.

### Retention schedules — what they are

A retention schedule is one row in the **File Plan**. It says, for a given record series:

- How long the record stays **active** (operational)
- How long it stays **dormant** (held but not in regular use) after the active period
- What **trigger event** starts the clock (creation date, file closure, fiscal year end, contract end, employment end)
- What **disposal action** is taken at the end (destroy, transfer to NARSSA, transfer to another archive, manual review, or permanent retention)
- Which **sign-offs** are mandatory (records officer is always required; legal and executive are configurable per schedule)
- The **legal basis** for the schedule (e.g. NARSSA Act 1996 §13(2)(d), PFMA, BCEA + POPIA)

Sample seed schedules shipped on every new install (examples — operators replace these with their organisation's File Plan codes):

| Code | Title | Active | Dormant | Trigger | Disposal | Legal/Exec |
|---|---|---|---|---|---|---|
| COMM-001 | Press releases (general) | 2 y | 3 y | creation_date | destroy | — |
| COMM-002 | Cabinet / executive briefings | 5 y | 25 y | creation_date | transfer_narssa | legal + exec |
| CORP-001 | Annual reports | 5 y | 0 y | creation_date | permanent | exec |
| CORP-002 | Procurement records | 5 y | 7 y | fiscal_year_end | destroy | legal |
| HR-001 | Employee personnel files | 7 y | 30 y | employment_end | destroy | legal |
| LEG-001 | Legal opinions | 5 y | 20 y | creation_date | review | legal + exec |

Operators can add/edit/delete schedules via the rights-admin UI or via `RetentionScheduleService` programmatically.

### Assigning a record to a schedule

When a record reaches archival status (typically on ingest from SharePoint or via the 6-step ingest wizard), an archivist:

1. Picks the matching File-Plan code (e.g. `COMM-002`)
2. Supplies the trigger-event date (e.g. file closure date)
3. The system calculates `calculated_disposal_due = trigger_event_date + active_period + dormant_period`

The assignment is stored in `retention_assignment` (one per IO). Reassignment to a different schedule is a simple update (idempotent).

### Disposal workflow — the sign-off chain

When `calculated_disposal_due` arrives, the record surfaces in the **disposal queue**. From there:

1. **Records officer** proposes the disposal action that the schedule prescribes.
2. **Officer signs** → status moves to `officer_signed`. Always required.
3. **Legal counsel signs** → status moves to `legal_signed`. Only when `schedule.requires_legal_signoff = 1`.
4. **Executive signs** → status moves to `executive_signed`. Only when `schedule.requires_executive_signoff = 1`.
5. When every required signature is in, the workflow **auto-advances to `approved`**.
6. The records officer (or automated job) **executes** the action — for `transfer_narssa`, this generates a NARSSA transfer package via `php symfony narssa:transfer-package`; for `destroy`, the record is permanently removed via a separate `disposal:finalize` step.

At any non-terminal stage:

- **Reject** with a reason → status `rejected`. Workflow is over.
- **Defer** with a reason → status `deferred`. The next sweep will re-propose.

### Audit trail

Every state transition writes one row to `ahg_audit_log` with action codes:

`disposal_proposed`, `disposal_officer_signed`, `disposal_legal_signed`, `disposal_executive_signed`, `disposal_approved`, `disposal_executed`, `disposal_rejected`, `disposal_deferred`.

Every disposal decision is captured with timestamp, user, and the JSON-serialised action_type and any notes — satisfying any records-management framework that requires a controlled disposal audit trail (NARSSA, ISO 15489, NARA, PRO Act, and equivalents). No record can be disposed without a complete sign-off chain visible in the audit log.

### Compliance dashboard integration

The new `Records Management Compliance: Retention Status & Lifecycle` report template (in `ahgReportBuilderPlugin`) surfaces:

- All records currently assigned to a schedule
- Records due for disposal in the next 12 months
- Disposal workflow pipeline by status
- Approved transfers awaiting NARSSA packaging

That report is part of the **Consolidated Quarterly Dashboard** template designed for the records management committee.

---

*Part of the AtoM AHG Framework*
