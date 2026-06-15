# Zimbabwe NAZ Compliance — User Guide

## A Guide for Archivists and Compliance Administrators

**Plugin:** `ahgNAZPlugin` v1.0.0
**Platform:** AtoM Heratio (AtoM 2.10 + AHG Framework)
**Author:** The Archive and Heritage Group (Pty) Ltd

---

## What is it?

The NAZ Compliance plugin supports institutions that operate under the **National Archives of Zimbabwe Act [Chapter 25:06]**. It manages the statutory **closure rule** (records are typically closed for 25 years), the **research permit** regime for access to closed and protected material, **records schedules** for retention and disposal, **transfers** of public records to the National Archives, and a register of **protected records**.

It gives administrators a dashboard that continuously checks for overdue closure reviews, expired closures still awaiting release, expired or stale permits, and overdue transfers.

---

## Key features

- **Closure periods** — record a closure against an information object with a closure type, reason, start date, length in years (defaulting to **25**), end date, authority reference and review date. The plugin can tell you whether a given record is currently closed.
- **25-year rule enforcement** — closures default to 25 years; expired closures still marked *active* are flagged for release.
- **Researcher register** — register researchers and maintain their details.
- **Research permits** — apply for, approve, take payment against (with receipt) and track research permits, including recording research **visits** under a permit.
- **Records schedules** — maintain retention/disposal schedules.
- **Transfers** — propose, schedule and complete transfers of public records to the National Archives, with line-level transfer items.
- **Protected records** — flag and look up records that carry protected status.
- **Compliance dashboard** — a status view returning *compliant / warning / non-compliant* with the specific drivers.
- **Audit log and visit log** — actions and research visits are recorded.

---

## How to use it

Screens are available both under `/admin/naz/...` (admin area) and at the shorter `/naz/...` paths:

- **Dashboard** — `/admin/naz`
- **Closures** — `/admin/naz/closures`, create `/admin/naz/closure/create`, edit `/admin/naz/closure/:id/edit`
- **Research permits** — `/admin/naz/permits`, create `/admin/naz/permit/create`, view `/admin/naz/permit/:id`
- **Researchers** — `/admin/naz/researchers`, create `/admin/naz/researcher/create`, edit `/admin/naz/researcher/:id/edit`, view `/admin/naz/researcher/:id`
- **Records schedules** — `/admin/naz/schedules`, create `/admin/naz/schedule/create`, view `/admin/naz/schedule/:id`
- **Transfers** — `/admin/naz/transfers`, create `/admin/naz/transfer/create`, view `/admin/naz/transfer/:id`
- **Protected records** — `/admin/naz/protected`
- **Reports** — `/admin/naz/reports`
- **Configuration** — `/admin/naz/config`

### Command line (for scheduled checks)

```bash
php symfony naz:closure-check    # Check closure periods for expiry and releases
php symfony naz:permit-expiry    # Check research permits for expiry
php symfony naz:transfer-due     # List pending and overdue records transfers
php symfony naz:report           # Generate NAZ compliance reports
```

Run `naz:closure-check`, `naz:permit-expiry` and `naz:transfer-due` from cron so that releases, expiries and due transfers surface automatically.

---

## Compliance notes

- The plugin implements the **National Archives of Zimbabwe Act [Chapter 25:06]**, in particular the closure (access-restriction) regime, permit-controlled access, scheduled transfer of public records to the National Archives, and protected-records management.
- The default closure length is **25 years**, in line with the standard NAZ closure rule; you can override the period per record where the law allows a longer or shorter closure.
- The dashboard treats **closure periods overdue for review** as a hard issue. Expired-but-unreleased closures, expired active permits, permit applications pending more than 7 days, and overdue transfers are raised as warnings.
- Releasing a closure records who released it, when, and any notes — preserving the access-decision trail.
- A permit can carry a payment with a receipt number, supporting fee-based access.

---

## Tips & FAQ

**Q: How do I check whether a specific record is closed?**
The service exposes a closed/open check for any information object; the closures dashboard also lists active closures by end date.

**Q: When does a closure count as expired?**
When its end date has passed but its status is still *active* — those appear as a warning prompting release.

**Q: What happens to permits that pass their end date?**
They are flagged as expired in the compliance check while still marked active, so they can be reviewed and closed out.

**Q: Can I track who visited the reading room under a permit?**
Yes — visits can be recorded against a permit and listed per permit and per researcher.
