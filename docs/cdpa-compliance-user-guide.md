# Zimbabwe CDPA Compliance — User Guide

## A Guide for Data Protection Officers and Compliance Administrators

**Plugin:** `ahgCDPAPlugin` v1.0.0
**Platform:** AtoM Heratio (AtoM 2.10 + AHG Framework)
**Author:** The Archive and Heritage Group (Pty) Ltd

---

## What is it?

The CDPA Compliance plugin helps a Zimbabwean institution demonstrate and manage compliance with the **Cyber and Data Protection Act [Chapter 12:07]**, the statute administered by the **Postal and Telecommunications Regulatory Authority of Zimbabwe (POTRAZ)**. It provides a single administrative area that tracks your data-controller licensing position, your Data Protection Officer, the obligations you owe to data subjects, and the incidents you must be ready to report.

Everything is recorded in dedicated tables (license, DPO, data-subject requests, processing activities, DPIAs, consent records and breaches) and surfaced as a live compliance dashboard. Every create/update action is written to an internal audit log.

---

## Key features

- **POTRAZ controller licence register** — record your licence number, tier, organisation name, registration/issue/expiry dates and POTRAZ reference. The dashboard automatically flags a licence that is expired, suspended, or expiring within 90 days.
- **Data Protection Officer (DPO) record** — capture the appointed DPO and whether **Form DP2** has been submitted to POTRAZ.
- **Data subject requests** — log access, correction, deletion and objection requests, with automatic due-date tracking and an overdue warning.
- **Processing activity inventory** — maintain a register of your data-processing activities (a record-of-processing obligation).
- **Data Protection Impact Assessments (DPIAs)** — create DPIAs and set a next-review date; overdue reviews are flagged.
- **Consent register** — record consents and withdraw them with a reason.
- **Breach management** — log incidents and track them through investigating/contained/ongoing to closure, with overdue-notification detection.
- **Compliance dashboard** — a single `getComplianceStatus()` view that returns *compliant / warning / non-compliant* with the specific issues and warnings driving the verdict.

---

## How to use it

All screens live under the admin area. Sign in as an administrator and go to:

- **Dashboard** — `/admin/cdpa`
- **Controller licence** — `/admin/cdpa/license` (edit at `/admin/cdpa/license/edit`)
- **Data Protection Officer** — `/admin/cdpa/dpo` (edit at `/admin/cdpa/dpo/edit`)
- **Data subject requests** — `/admin/cdpa/requests`, create at `/admin/cdpa/request/create`, view at `/admin/cdpa/request/:id`
- **Processing activities** — `/admin/cdpa/processing`, create at `/admin/cdpa/processing/create`, edit at `/admin/cdpa/processing/:id/edit`
- **DPIAs** — `/admin/cdpa/dpia`, create at `/admin/cdpa/dpia/create`, view at `/admin/cdpa/dpia/:id`
- **Consent records** — `/admin/cdpa/consent`
- **Breaches** — `/admin/cdpa/breaches`, create at `/admin/cdpa/breach/create`, view at `/admin/cdpa/breach/:id`
- **Reports** — `/admin/cdpa/reports`
- **Configuration** — `/admin/cdpa/config`

### Command line (for scheduled checks)

```bash
php symfony cdpa:status          # Show CDPA compliance dashboard
php symfony cdpa:license-check   # Check POTRAZ licence expiry
php symfony cdpa:requests        # List data subject requests
php symfony cdpa:report          # Generate a CDPA compliance report
```

`cdpa:license-check` is well suited to a daily cron so a lapsing POTRAZ licence is caught early.

---

## Compliance notes

- The plugin is built specifically around the **Cyber and Data Protection Act [Chapter 12:07]** and **POTRAZ** licensing — the licence tiers, the DPO appointment and the Form DP2 submission flag all map to that regime.
- The dashboard treats a **missing/expired licence**, a **missing DPO**, and **overdue data-subject requests** as hard *issues* (non-compliant). Open breaches, an unsubmitted Form DP2, an imminent licence expiry and overdue DPIA reviews are raised as *warnings*.
- Data-subject requests are date-driven: a pending request past its `due_date` becomes an overdue issue, so log the request as soon as it is received.
- All actions are recorded in the `cdpa_audit_log` table for evidentiary purposes.

---

## Tips & FAQ

**Q: How is "expiring soon" defined for the licence?**
Within 90 days of the expiry date. A suspended licence is reported as suspended regardless of date.

**Q: We only have one licence — does saving create duplicates?**
No. Saving the licence updates the most recent record rather than inserting a new row each time.

**Q: A request looks pending but isn't overdue yet — will it warn?**
Only requests whose `due_date` has passed are counted as overdue. Set realistic due dates on creation.

**Q: Can I withdraw a consent?**
Yes — use the consent screen; you can supply a withdrawal reason, which is retained for the record.
