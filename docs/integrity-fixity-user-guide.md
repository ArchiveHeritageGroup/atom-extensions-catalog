# Integrity Assurance & Fixity — User Guide

## A Guide for Digital Preservation Staff and Administrators

**Plugin:** `ahgIntegrityPlugin` v1.1.0
**Platform:** AtoM Heratio (AtoM 2.10 + AHG Framework)
**Author:** The Archive and Heritage Group (Pty) Ltd

---

## What is it?

The Integrity Assurance plugin provides automated, scheduled **fixity verification** for your digital objects: it recomputes file checksums, compares them to the stored preservation baseline, and records every result in an **append-only ledger**. Around that core it adds scheduling, concurrency controls, a **dead-letter queue** for repeatedly-failing objects, **retention policies** with **legal holds** and a **disposition review** workflow, **threshold alerting**, and an auditor-ready export pack.

It is built for large repositories with strict chain-of-custody requirements. It depends on `ahgPreservationPlugin`, which supplies the checksum baseline.

---

## Key features

- **Fixity verification** — recompute a file's hash (SHA-256 by default; algorithm configurable per schedule) and compare to the baseline. Outcomes are *pass, mismatch, missing, unreadable, error,* or *no-baseline*.
- **Scheduled, scoped runs** — verify globally, by repository, or by a hierarchy branch, on daily/weekly/monthly or cron frequencies.
- **Concurrency & resource guards** — batch size, IO throttle, memory and runtime limits, plus file-lock overlap prevention so two runs don't collide.
- **Append-only ledger** — every result is written immutably with a `previous_hash` link, actor and hostname, enabling chain-of-custody verification.
- **Dead-letter queue** — objects that keep failing are escalated (default 3 retries) and tracked through open → acknowledged → investigating → resolved/ignored.
- **Retention & disposition** — retention policies (by ingest date, last modified, closure date or last access), a disposition review queue, and **legal holds** that block disposition. (Approved dispositions are *marked*, never auto-deleted.)
- **Threshold alerting** — email and HMAC-signed webhook alerts on pass-rate-below, failure-count, dead-letter-count, backlog or run-failure thresholds.
- **Dashboards, reports & exports** — pass rate, throughput, repository/format breakdowns, storage growth, a CSV ledger export and a ZIP **auditor pack** (exceptions, config snapshot, summary).

---

## How to use it

### Admin screens

- **Dashboard** — `/admin/integrity`
- **Schedules** — `/admin/integrity/schedules`, edit `/admin/integrity/schedule/edit`
- **Runs** — `/admin/integrity/runs`, detail `/admin/integrity/run/:id`
- **Ledger** — `/admin/integrity/ledger`
- **Dead-letter queue** — `/admin/integrity/dead-letter`
- **Reports** — `/admin/integrity/report`
- **Exports** — `/admin/integrity/export` (CSV `/admin/integrity/export/csv`, auditor pack `/admin/integrity/export/auditor`)
- **Retention policies** — `/admin/integrity/policies`, edit `/admin/integrity/policy/edit`
- **Legal holds** — `/admin/integrity/holds`
- **Disposition review** — `/admin/integrity/disposition`
- **Records management** — `/admin/integrity/records`
- **Alerts** — `/admin/integrity/alerts`

A JSON API mirrors these (under `/api/integrity/...`) for verify-on-demand, schedule control, hold placement, disposition review and dashboard data.

### Command line (recommended for cron)

```bash
php symfony integrity:schedule --run-due       # Run all due schedules (cron: */15 * * * *)
php symfony integrity:verify --object-id=N     # Verify a single digital object
php symfony integrity:verify --repository-id=N --stale-days=7
php symfony integrity:report --summary         # Summary + recent runs (text/json/csv)
php symfony integrity:report --auditor-pack=/path/pack.zip
php symfony integrity:retention --scan-eligible
php symfony integrity:retention --hold=IO_ID --reason="litigation"
```

A typical setup runs `integrity:schedule --run-due` every 15 minutes so each schedule fires at its next due time.

---

## Compliance notes

- The **append-only ledger** with `previous_hash` chaining, actor and hostname provides a defensible chain of custody for fixity events — suitable for OAIS / preservation audit evidence.
- The **auditor pack** bundles an exceptions list, a configuration snapshot and a summary into one ZIP for handing to an auditor.
- **Legal holds** prevent any record under hold from being disposed, and disposition is a reviewed, multi-state workflow (eligible → pending review → approved/rejected → disposed) — approval only *marks* records; it never performs deletion automatically.
- Default settings: algorithm **sha256**, batch size **200**, max runtime **120 min**, max memory **512 MB**, dead-letter retries **3**.

---

## Tips & FAQ

**Q: What does each outcome mean?**
*pass* = hash matches baseline; *mismatch* = file changed; *missing* = file not found; *unreadable* = exists but cannot be read; *error* = unexpected failure; *no-baseline* = no stored checksum to compare against.

**Q: Will two scheduled runs ever clobber each other?**
No — runs honour a max-concurrent limit and a file lock (with stale-PID recovery), so they serialise safely.

**Q: How are repeatedly failing files handled?**
They escalate to the dead-letter queue after the retry limit and are worked through a status workflow with notes; if a previously-resolved object fails again it auto-reopens.

**Q: Does disposition delete files?**
No. Approved dispositions are marked as disposed for the record; actual deletion is deliberately not automated, and active legal holds block disposition entirely.
