---
title: "Training: Authorities and People, Part 5 - Users and Self-Registration"
subtitle: "Step-by-step guide to public account requests: registering, confirming the email address, approving into a group, and managing users"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Authorities and People, Part 5 - Users and Self-Registration |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 9 November 2026 |
| Prepared for | Administrators who manage user accounts |
| Classification | Public |
| Reference | AHG-TRN-PPL-05 |

: Document control

This guide goes with part 5 of the authorities and people training videos. Without self-registration, every account is made by an administrator. With it, a visitor asks for an account themselves, proves the email address is theirs, and an administrator decides whether to approve the request and which group the new user joins. Nothing is granted until an administrator approves. Allow about 10 minutes.

## Before you start

| What | Notes |
|---|---|
| Plugins | User management (ahgUserManagePlugin) and user registration (ahgUserRegistrationPlugin), enabled. |
| Email | Outgoing email set up under the AHG email settings, so applicants receive their confirmation link and administrators hear about new requests. |
| Who is told | Active access-request approvers with email notifications on, plus the addresses in the **new researcher** notification setting. If neither is set, all active administrators are told. |
| Account | An administrator approves requests. |

: What you need before you start

## 1. A visitor asks for an account

On the login page the visitor chooses **Create an account** (`/register`) and fills in:

| Field | Notes |
|---|---|
| Full name, email address, username | Required. The username takes letters, numbers, dots, hyphens and underscores. |
| Password, confirm password | Required. |
| Institution, research interest | Optional, but they help the administrator decide. |
| Reason for registration | Required. |

: The registration form

**Submit Registration** records the request and sends a confirmation email. An email address can only have one request at a time, and an address that already has an account is refused.

## 2. The applicant confirms their email

The email holds a link. Opening it marks the address as confirmed, and only then can the request be approved. If the email cannot be delivered, an administrator can mark the request as verified by hand, but only after confirming the applicant's identity another way.

## 3. Administrators are told

When the address is confirmed, the people listed under **Before you start** get an email, and every page shows administrators a banner: "account registration request(s) awaiting review", with a **Review** button.

## 4. Approve or reject

Open **Registration Requests** (`/admin/registrations`). The tabs show all requests, those awaiting review, approved and rejected. Each row shows the name, email, username, institution, reason, status and date.

- **Approve** (the tick): choose the group the new user joins and add a note if you like, then confirm. The account is created and the applicant can sign in.
- **Reject** (the cross): give the reason. The request is kept as rejected, with the reason.

The group list starts on **authenticated**, the basic group every signed-in user has. Choose editor, contributor or another group only when the person needs those rights; contributor and editor can change descriptions.

## 5. Manage users

**Admin > Users** (`/user/list`) lists every account, with search, active and inactive filters and sorting. The **User groups** column lists groups beyond the basic authenticated one, so a newly approved user with no extra group shows none there. Open a user to edit their details, groups and access.

## Recap

| Step | Where |
|---|---|
| Visitor asks for an account | Login page > Create an account |
| Applicant confirms | The link in the email |
| Review requests | /admin/registrations |
| Approve into a group, or reject | Tick or cross on the request |
| Manage accounts | /user/list |

: Recap

This completes the authorities and people series. The next series is collections care and integrity.
