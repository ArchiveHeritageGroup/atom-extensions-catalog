# Zimbabwe NMMZ Compliance — User Guide

## A Guide for Heritage Officers and Compliance Administrators

**Plugin:** `ahgNMMZPlugin` v1.0.0
**Platform:** AtoM Heratio (AtoM 2.10 + AHG Framework)
**Author:** The Archive and Heritage Group (Pty) Ltd

---

## What is it?

The NMMZ Compliance plugin supports institutions operating under the **National Museums and Monuments of Zimbabwe Act [Chapter 25:11]**. It maintains the statutory **monument register**, an **antiquities** register, **export permits** for cultural property, an **archaeological sites** register, and **heritage impact assessments (HIAs)**. It also tracks **monument inspections**.

Administrators get a dashboard that watches for monuments at risk, monuments overdue for inspection, export permits sitting too long, missing antiquities, and HIAs awaiting review.

---

## Key features

- **Monument register** — record national monuments by category, with status (active, at risk, etc.) and last-inspection date.
- **Monument categories** — maintain the category list that classifies each monument.
- **Antiquities register** — register antiquities and track their status, including a *missing* status that is flagged as a compliance issue.
- **Export permits** — apply for, review and approve permits to export cultural property, with optional approval conditions.
- **Archaeological sites** — maintain a site register.
- **Heritage Impact Assessments (HIAs)** — create HIAs and move them through review.
- **Monument inspections** — record inspections against a monument and list a monument's inspection history.
- **Compliance dashboard** — a *compliant / warning / non-compliant* status with the specific drivers.
- **Audit log** — actions are recorded for accountability.

---

## How to use it

All screens are in the admin area:

- **Dashboard** — `/admin/nmmz`
- **Monuments** — `/admin/nmmz/monuments`, create `/admin/nmmz/monument/create`, view `/admin/nmmz/monument/:id`
- **Antiquities** — `/admin/nmmz/antiquities`, create `/admin/nmmz/antiquity/create`, view `/admin/nmmz/antiquity/:id`
- **Export permits** — `/admin/nmmz/permits`, create `/admin/nmmz/permit/create`, view `/admin/nmmz/permit/:id`
- **Archaeological sites** — `/admin/nmmz/sites`, create `/admin/nmmz/site/create`, view `/admin/nmmz/site/:id`
- **Heritage impact assessments** — `/admin/nmmz/hia`, create `/admin/nmmz/hia/create`
- **Reports** — `/admin/nmmz/reports`
- **Configuration** — `/admin/nmmz/config`

### Command line

```bash
php symfony nmmz:report    # Generate NMMZ heritage reports
```

---

## Compliance notes

- The plugin is built around the **National Museums and Monuments of Zimbabwe Act [Chapter 25:11]**, covering the declaration and management of national monuments, control of antiquities, regulation of the export of cultural property, protection of archaeological sites, and heritage impact assessment.
- The compliance dashboard treats **monuments at risk** and **antiquities reported missing** as hard issues (non-compliant). It raises warnings for monuments **overdue for inspection** (no inspection in the last 2 years), **export permits pending more than 14 days**, and **HIAs under review for more than 30 days**.
- Approving an export permit records the approver and the date, and lets you attach approval conditions — preserving the decision trail required for cultural-property control.
- Inspections feed the inspection-overdue check, so recording them keeps the monument register current.

---

## Tips & FAQ

**Q: When is a monument flagged as overdue for inspection?**
When an active monument has no recorded last-inspection date, or its last inspection is more than two years old.

**Q: What makes the dashboard show "non-compliant" rather than just a warning?**
Monuments marked at risk or antiquities marked missing are treated as issues, which set the overall status to non-compliant.

**Q: Can I attach conditions when approving an export permit?**
Yes — the approval step accepts conditions and records the approving user and timestamp.

**Q: How do I classify monuments consistently?**
Maintain the monument category list and assign each monument to a category on creation.
