---
title: "Training: Collections Care and Integrity, Part 2 - Integrity Checks and the Fixity Ledger"
subtitle: "Step-by-step guide to the integrity dashboard, scheduling fixity checks by scope, running them, and reading the ledger, the dead letter queue and the exports"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Collections Care and Integrity, Part 2 - Integrity Checks and the Fixity Ledger |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 9 November 2026 |
| Prepared for | Digital preservation staff and system administrators |
| Classification | Public |
| Reference | AHG-TRN-CARE-02 |

: Document control

This guide goes with part 2 of the collections care and integrity training videos. A fixity check reads a stored master file, computes its checksum and compares it with the checksum recorded when the file came in. A difference means the file has changed; no file means it has gone. Run regularly, the checks find silent damage while there is still a backup to restore from. The integrity plugin schedules the checks, keeps an append-only ledger of every result, and queues the failures for someone to deal with. Allow about 10 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | An administrator. |
| Plugin | Integrity (ahgIntegrityPlugin), enabled. |
| Database | The `integrity_ledger` table needs the `actor` and `hostname` columns. Sites set up before November 2026 must add them by hand (the statements are in the plugin's `install.sql`); without them every run fails with "Unknown column 'actor'" and records nothing. |
| Scheduler | A cron job that runs due schedules every hour, as the web server user: `php symfony integrity:schedule --run-due`. Without it, schedules never run on their own. |
| Version | Plugins v3.121.165 or later. Earlier versions switched a schedule off every time it was saved, and had no Run now button. |

: What you need before you start

## 1. The dashboard

Open **Integrity** at `/admin/integrity`.

| Figure | What it means |
|---|---|
| Master objects | Master files held |
| Total verifications | Checks recorded in the ledger |
| Pass rate | Share of checks that passed |
| Open dead letters | Failures nobody has dealt with yet |
| Never verified | Master files that have never been checked |
| Throughput | Files and gigabytes checked per hour over the last week |

: The dashboard figures

Below them, the results are broken down by repository and by file format. The buttons along the top lead to schedules, the ledger, the report, exports, retention policies, legal holds and alerts.

## 2. Schedule a check

Open **Schedules** and choose **New Schedule**.

| Setting | Notes |
|---|---|
| Name, description | What the schedule is for. |
| Enabled | Off means the schedule is kept but never runs. |
| Scope | **Global** checks every master file; **Repository** one repository; **Hierarchy** one record and everything below it, chosen by searching for it. |
| Hash algorithm | SHA-256 or SHA-512. |
| Frequency | Daily, weekly, monthly or ad hoc. An optional cron expression sets an exact time. |
| Files per run | 0 checks every file in scope; a number checks that many each run, for a rolling sample. |
| Limits | Pause between files, memory, maximum run time and how many runs may overlap, to keep checks from slowing the site. |
| Notifications | Email when a run fails or a file has changed, and to whom. |

: Schedule settings

Choose **Save Schedule**.

## 3. Run a check now

Schedules run on their own when due. To check at once, choose the **Run now** button (the play icon) on the schedule's row. The run's results open when it finishes. The same row has **Disable/Enable**, **Edit** and **Delete**.

A large scope takes time: a full check reads every file. On PSIS, 188 master files took under a minute.

## 4. Read the results

The run page shows its status, the schedule, start and end times, the counters (scanned, passed, failed) and every file checked, with its outcome.

| Outcome | Meaning |
|---|---|
| pass | The checksum matches |
| mismatch | The file has changed since its checksum was recorded |
| missing | No file at the stored path |
| unreadable, permission_error | The file is there but cannot be read |
| path_drift | The file has moved |
| no_baseline | No checksum was ever recorded to compare with |
| error | The check itself failed |

: Check outcomes

## 5. The ledger

**Ledger** lists every check ever made: the run, the object, the outcome, the file, whether the checksum matched, and when. Each entry also records who or what ran it (a user, the scheduler or the API) and on which server. The ledger is append-only: entries are never changed or deleted, which is what makes it usable as evidence.

## 6. The dead letter queue

Failures go to the **Dead Letter Queue**, counted as open, acknowledged, investigating, resolved or ignored. Work through each: find out what happened, restore the file from backup if needed, and mark it resolved, so the open count shows only what still needs attention.

## 7. Export for audits

**Export** filters the ledger by date, repository and outcome, then gives either a **CSV** of the ledger or an **Auditor Pack**: a ZIP with a summary page, the exceptions as a spreadsheet and a snapshot of the integrity settings. **Report** gives the same summary on screen, with the matching command-line reports.

## Recap

| Step | Where |
|---|---|
| See what has never been checked | /admin/integrity |
| Schedule checks by scope | Schedules > New Schedule |
| Check now | Run now on the schedule's row |
| Read every result | Ledger |
| Deal with failures | Dead Letter Queue |
| Give an auditor the evidence | Export > Auditor Pack |

: Recap

Next, part 3: OCFL preservation storage and versions.
