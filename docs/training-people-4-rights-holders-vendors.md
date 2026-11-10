---
title: "Training: Authorities and People, Part 4 - Rights Holders and Vendors"
subtitle: "Step-by-step guide to adding rights holders, managing vendors and their services, and tracking items sent out for conservation or other work"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Authorities and People, Part 4 - Rights Holders and Vendors |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 9 November 2026 |
| Prepared for | Archivists, registrars and collections managers |
| Classification | Public |
| Reference | AHG-TRN-PPL-04 |

: Document control

This guide goes with part 4 of the authorities and people training videos. It covers two kinds of outside party. Rights holders are the people and organisations who hold copyright or other rights in your records. Vendors are the services you send items to: conservators, binders, digitisation studios, framers, transport. For vendors the plugin also keeps a record of every item that leaves the building, why, in what condition, and where the work stands. Allow about 10 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | An editor or administrator. |
| Plugins | Rights holder management (ahgRightsHolderManagePlugin) and vendors (ahgVendorPlugin), enabled. |
| Visibility | Both are for signed-in staff only. |
| Version | Plugins v3.121.162 or later. Earlier versions did not save a new vendor's services, the items on a new transaction, or its due date, reference and notes. |

: What you need before you start

## 1. Add a rights holder

1. Open **Rights holders** (`/rightsholder/browse`) and choose **Add new**.
2. Enter the name, then open **Contact area** for the contact person, email, address, town and country.
3. Choose **Create**.

When you add a rights statement to a description, you choose the rights holder from this list, so the same holder is named the same way on every record.

## 2. The vendor dashboard

Open **Vendor Management** (`/vendor`). The cards show:

| Card | What it counts |
|---|---|
| Active vendors | Vendors with the status Active |
| Active transactions | Transactions that are not yet closed |
| Pending approval | Transactions waiting to be approved |
| Overdue | Transactions past their due date |
| Items out | Items currently with a vendor |
| This month | The month's costs |

: The vendor dashboard cards

Below them are the recent transactions, the spread of transactions by status, and quick links. **Service Types** (`/vendor/serviceTypes`) holds the list of services; add your own there.

## 3. Add a vendor

1. Choose **Add Vendor**.
2. Enter the name and type (company, individual, institution or government), registration and VAT numbers if you need them, the address and the contact details.
3. Add banking and insurance details if you pay or insure through this vendor.
4. Tick the services the vendor offers.
5. Choose **Save Vendor**.

The vendor's page lists its services and its transactions, and **Add contact** records the people you deal with there.

## 4. Send an item: a new transaction

A transaction records one job: what goes to which vendor, for which service, and when it should come back.

1. Choose **New Transaction**.
2. Choose the vendor and the service, the request date and the due date, and the priority.
3. Describe the work. The description and priority are kept with the transaction's notes.
4. Under **GLAM/DAM Items**, search by title or identifier and choose each item being sent. For each, record its condition as it leaves and, if needed, its declared value.
5. Add the estimated cost and any reference number, and choose **Create Transaction**.

A new transaction starts as **Pending approval**.

## 5. Track the work

The transaction page shows the vendor, service, dates, items, costs and invoice. **Update Status** moves it on, with a note each time:

| Status | Meaning |
|---|---|
| Pending approval | Waiting for someone to approve it |
| Approved | Cleared to go |
| Dispatched | Has left the building |
| Received by vendor | The vendor has it |
| In progress | Work has started |
| Completed | Work is done |
| Ready for collection | Waiting to be fetched |
| Returned | Back in the building |
| Cancelled | Not going ahead |

: Transaction statuses

Every status change is kept in the transaction's history, with who made it and the note. **Link Item** adds more items to a transaction after it is created.

## Recap

| Step | Where |
|---|---|
| Add a rights holder | /rightsholder/browse > Add new |
| See the vendor overview | /vendor |
| Add a vendor | Add Vendor |
| Record a job | New Transaction |
| Move it on | Update Status on the transaction |

: Recap

Next, part 5: users, and public self-registration with approval.
