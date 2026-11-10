---
title: "Training: Authorities and People, Part 3 - Donors and Donor Agreements"
subtitle: "Step-by-step guide to the donor dashboard, adding a donor, recording a deed of gift with its scope and dates, and setting reminders"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Authorities and People, Part 3 - Donors and Donor Agreements |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 9 November 2026 |
| Prepared for | Archivists and registrars who record acquisitions |
| Classification | Public |
| Reference | AHG-TRN-PPL-03 |

: Document control

This guide goes with part 3 of the authorities and people training videos. Every acquisition starts with a donor and, usually, a written agreement: a deed of gift, a deposit, a purchase or a loan. The donor agreement plugin keeps that agreement next to the donor record, with what was given, how it arrived, the dates that matter, the signed documents and reminders for what has to happen next. Allow about 10 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | An editor or administrator. |
| Plugins | Donor management (ahgDonorManagePlugin) and donor agreements (ahgDonorAgreementPlugin), enabled. |
| Visibility | Donor records and agreements are for signed-in staff only. A visitor who opens a donor page is sent to the login page. |
| Version | Plugins v3.121.160 or later. Earlier versions could not save a new agreement, dropped most of its fields, or could not delete one. |

: What you need before you start

## 1. The donor dashboard

Open **Donor Management** at `/donor/dashboard`. The cards along the top show:

| Card | What it counts |
|---|---|
| Total donors | All donor records, and how many are active |
| Active agreements | Agreements with the status Active, out of all agreements |
| Expiring soon | Agreements whose expiry date falls in the next 30 days |
| Pending reminders | Reminders that need action |

: The dashboard cards

Below them are counts by status (drafts, review due, expired, terminated), the most recent agreements, and the reminders. The repository list at the top narrows the dashboard to one repository.

An agreement's status is set by hand: an agreement past its expiry date stays Active until someone changes it, so use **Expiring soon** to catch them in time.

## 2. Add a donor

1. Choose **Add Donor** on the dashboard, or **Add new** on Browse donors.
2. Enter the donor's name.
3. Open **Contact area** and fill in the contact person, email, telephone, address, town and country.
4. Choose **Create**.

A donor's contact details are personal information when the donor is a person. Record what you need to manage the gift, and no more.

## 3. Record the agreement

Open **New Agreement** (`/donor/agreement/add`). The form is long, but only the type is required. Fill in what the agreement actually says:

| Section | What goes in it |
|---|---|
| Agreement details | Type (deed of gift, deposit, purchase, loan, bequest and others), title, description. The number is generated if left empty, for example DOG-2026-0002 for a deed of gift. |
| Donor information | The donor (type part of the name to find them), with an override name and contact if the agreement names someone else |
| Institution and legal representative | Who signs for the institution, and any legal representative |
| Contract documents | The signed agreement and any drafts, amendments, correspondence or inventories, each with a type |
| Scope & transfer | What was given, the extent, how it arrived, when, and who received it |
| Financial terms | For purchases: amount, currency and payment terms |
| Terms & conditions | General terms and any special conditions |
| Important dates | Agreement, effective, review, expiry and termination dates |
| Signatures | Who signed for the donor, for the institution, and as witness, with dates |
| Internal notes | Staff notes that are not part of the agreement |

: The agreement form

Set the **status** (draft, pending review, pending signature, active, expired or terminated) and choose **Create Agreement**. Archival descriptions and accessions are linked afterwards, from **Edit**.

## 4. Add reminders

In the **Reminders** section of the form, choose **Add Reminder** and pick the kind: review due, expiry warning, renewal required, donor contact, follow up, restriction ending, payment due, anniversary, audit, preservation check or custom. Give it a date and a short message. Add as many as the agreement needs.

Reminders appear on the agreement's page, on the dashboard, and on **Pending reminders** (`/donor/agreement/reminders`), which lists every active reminder due in the next 30 days across all agreements. Reminders are shown in the system; they are not sent by email.

## 5. The agreement page

The agreement page shows everything recorded: details, donor, scope and transfer, dates, signatures, documents and reminders, with the history of changes. **Edit** changes any of it.

## Recap

| Step | Where |
|---|---|
| See the overview | /donor/dashboard |
| Add the donor | Add Donor |
| Record the agreement | New Agreement |
| Add reminders | Reminders section of the form |
| Check what is due | /donor/agreement/reminders |

: Recap

Next, part 4: rights holders and vendors.
