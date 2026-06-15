# IPSAS 45 Heritage Asset Accounting — User Guide

## A Guide for Finance Officers and Administrators

**Plugin:** `ahgIPSASPlugin` v1.0.0
**Platform:** AtoM Heratio (AtoM 2.10 + AHG Framework)
**Author:** The Archive and Heritage Group (Pty) Ltd

---

## What is it?

The IPSAS Heritage Accounting plugin lets a public-sector institution account for its heritage collections in line with the **International Public Sector Accounting Standards**, specifically **IPSAS 45 (Property, Plant and Equipment — heritage assets)**. It maintains a **heritage asset register**, records **valuations**, **impairments**, **depreciation**, **insurance** policies and **disposals**, and produces a **financial-year summary** that rolls opening balances forward to closing balances.

It is a dedicated finance module — separate from the descriptive catalogue — that gives accountants the figures and movement schedules they need for the notes to the financial statements.

---

## Key features

- **Heritage asset register** — record assets with an acquisition cost, current carrying value, status and asset category.
- **Asset categories** — classify assets for reporting.
- **Valuations** — record valuations, including revaluations, with a change amount so increases and decreases can be reported separately.
- **Impairments** — recognise impairment losses against an asset with a recognition date.
- **Depreciation** — track depreciation entries.
- **Insurance** — maintain insurance policies covering the collection.
- **Disposals** — record disposals with a carrying value at disposal.
- **Financial-year summary** — compute, for a given year, opening assets/value, additions, disposals, revaluation increases and decreases, impairments, and closing assets/value.
- **Compliance dashboard** — a status view highlighting accounting gaps (e.g. assets without valuations).
- **Audit log** — finance actions are recorded.

---

## How to use it

All screens are in the admin area:

- **Dashboard** — `/admin/ipsas`
- **Asset register** — `/admin/ipsas/assets`, create `/admin/ipsas/asset/create`, view `/admin/ipsas/asset/:id`, edit `/admin/ipsas/asset/:id/edit`
- **Valuations** — `/admin/ipsas/valuations`, create `/admin/ipsas/valuation/create`
- **Impairments** — `/admin/ipsas/impairments`
- **Insurance** — `/admin/ipsas/insurance`
- **Financial-year summary** — `/admin/ipsas/financial-year`
- **Reports** — `/admin/ipsas/reports`
- **Configuration** — `/admin/ipsas/config`

### Command line

```bash
php symfony ipsas:report    # Generate IPSAS heritage asset reports
```

---

## Compliance notes

- The plugin is aligned to **IPSAS 45**, the international public-sector standard for property, plant and equipment that addresses the recognition, measurement and disclosure of **heritage assets**. (Its design parallels the South African **GRAP 103** heritage-asset standard, which IPSAS 45 is consistent with.)
- The **financial-year summary** is the headline IPSAS deliverable: it derives opening totals from assets created before the year start (excluding disposed/lost/destroyed), adds additions and revaluation movements during the year, subtracts disposals at carrying value, deducts recognised impairments, and presents closing asset count and value — i.e. a movement reconciliation suitable for the financial-statement notes.
- The financial year boundary is configurable (default start `01-01`) so the summary can match your reporting cycle.
- Revaluation increases and decreases are reported separately (driven by the sign of the valuation change amount), supporting the revaluation-surplus/deficit presentation IPSAS expects.
- Disposed, lost or destroyed assets are excluded from closing balances so the register reflects assets still held.

---

## Tips & FAQ

**Q: Does the closing value use acquisition cost or current value?**
Closing value sums the assets' current (carrying) value, while opening value is based on acquisition cost of assets held before year start; record valuations to keep current values meaningful.

**Q: How do I get a clean year-end movement schedule?**
Open the Financial-year screen and select the year — the summary computes opening, additions, disposals, revaluations, impairments and closing figures for you.

**Q: Why is an asset missing from the closing count?**
Assets with status disposed, lost or destroyed are excluded from closing balances by design.

**Q: Can I change the financial year start?**
Yes — set the financial-year start in the configuration screen; the summary uses it to compute the year window.
