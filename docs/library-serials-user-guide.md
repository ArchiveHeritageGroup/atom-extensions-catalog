# Serials Management

## A Guide for Serials and Periodicals Staff

---

## What the Serials module does

Manages periodical subscriptions from prediction through receipt, claiming and binding:

- **Subscriptions** — vendor, frequency, issues per year, renewal date.
- **Issue prediction** — generate expected issues with enumeration (volume / issue) and chronology.
- **Receiving** — check in expected issues; gaps are flagged automatically.
- **Claiming** — claim missing or late issues.
- **Bindery** — batch received issues, send to the bindery, and mark them returned/bound.
- **Renewal reminders** — scheduled email of subscriptions due for renewal.

---

## Predicting and receiving issues

1. Create a **subscription** (frequency + issues-per-year drive the prediction).
2. **Generate expected issues** for a date range — each predicted issue gets a volume, issue number (cycling within the volume) and expected date.
3. As issues arrive, **check in** the expected issue (status → *received*). The **gaps** view lists expected-but-not-received.
4. **Claim** a late/missing issue — status → *claimed*, with a claim count.

## Bindery

From **Serials → Bindery**: select received issues, **send to bindery** (creates a batch), then **receive** the batch back to mark those issues *bound* (optionally linking the bound volume).

## Renewal reminders

A scheduled task emails staff the subscriptions due for renewal:

```bash
php symfony library:serial-renewal-reminders --days=30
```

Recipients come from `ahg_settings.serial_renewal_recipients` (comma-separated). Add it to cron (e.g. weekly).

---

## For Administrators

- Tables: `library_subscription`, `library_serial_issue`, `library_bindery_batch`.
- Issue status values come from the `serial_issue_status` dropdown taxonomy (expected / received / claimed / missing / bound / damaged).
