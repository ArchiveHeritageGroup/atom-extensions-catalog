# User Registration

## A Guide for Administrators and Staff

## What is it?

The User Registration module (`ahgUserRegistrationPlugin`) lets members of the public request
their own account through a self-service form, then routes that request through email
verification and an administrator approval queue before any account is created. Nothing is
activated automatically - an administrator must approve each request. Registration data is held
in the `ahg_registration_request` table until a request is approved (which creates the real
user), rejected, or expires.

## Key features

- **Public self-registration form** capturing full name, email, username, password,
  institution, research interest, and a required reason for the request.
- **Email verification** - a verification link (valid for 48 hours) is emailed to the
  applicant; the request only enters the admin queue once the email is verified.
- **Admin approval queue** showing all requests, filterable by status (pending, verified,
  approved, rejected, expired).
- **Approve, reject, or manually mark-verified** actions for administrators.
- **Group assignment on approval** - choose a group from a dropdown, or fall back to the
  configured default group.
- **Email notifications** for verification, admin notice of a new verified request, approval,
  and rejection (rejection can include a reason).
- **Rate limiting per IP address** to curb abuse.
- **Daily cleanup** of stale, unverified requests via a CLI task.
- **Administrator notification** when requests are waiting: a banner on every page and a
  counted entry in the navigation, so a request cannot sit unnoticed.
- **Re-application** after a request was rejected, expired, or approved and the account later
  deleted. The address becomes available again rather than being permanently blocked.

## How to use it

**For applicants (public):**

- **`/register`** - the registration form. After submitting, the applicant receives a
  verification email.
- **`/register/verify/<token>`** - the link in that email; clicking it marks the email
  verified and notifies administrators. The token expires after 48 hours, after which the
  applicant registers again with the same address.

If registration has been disabled, the form shows a "registration disabled" notice. Logged-in
users visiting `/register` are redirected to the home page.

**For administrators:**

- **`/admin/registrations`** - the approval queue. Add `?status=verified` (or `pending`,
  `approved`, `rejected`, `expired`) to filter.
- From the queue, administrators can:
  - **Approve** a verified request - this creates an active user, assigns the group chosen in
    the approval dialog, and emails the applicant naming the access level granted.

    The dialog offers **authenticated** and defaults to it. Authenticated is an ordinary
    signed-in account with no editing rights, which is the right starting point for someone who
    has just asked for access; grant contributor or editor deliberately, not by default. No
    group row is written for authenticated - AtoM treats every signed-in user as a member of it
    already.
  - **Reject** a request, optionally with a reason that is emailed to the applicant.
  - **Mark verified** - manually verify a pending request when the verification email could
    not be delivered and identity is confirmed out-of-band.

Only email-**verified** requests can be approved. Approving a request that has already been
approved is reported as done rather than as an error.

**Finding out that a request is waiting.** Administrators do not have to check the queue. While
anything is awaiting review, a banner appears below the header on every page with a **Review**
button, and the navigation carries a **Registrations** entry showing the count. Both are visible
only to administrators, and both disappear once the queue is clear. On an instance running the
AHG theme the notice appears in that theme's own notification strip instead, alongside access
requests and error-log entries.

## Administration / settings

The module reads these AHG settings:

- **`registration_enabled`** (default `1`) - turn public registration on or off.
- **`registration_max_per_hour`** (default `5`) - maximum requests allowed per IP per hour.
- **`registration_default_group`** (default `99`, authenticated) - the group assigned on
  approval when none is chosen. It was previously contributor, which granted editing rights to
  every approved applicant without the approving administrator being shown that this was
  happening.

**Scheduled cleanup:** run the CLI task to expire unverified requests older than 48 hours:

```
php symfony registration:cleanup
```

Run this daily via cron to keep the queue tidy.

## Tips & FAQ

- **A request never appeared in the queue.** It is likely still *pending* - the applicant has
  not clicked the verification link, or the email did not arrive. Use **Mark verified** to
  proceed manually.
- **Verification link expired?** Tokens last 48 hours; the applicant simply registers again
  with the same address.
- **Duplicate email or username?** The form rejects an address that already has a request
  awaiting review, or that belongs to an existing account, and re-checks at approval time in
  case an account appeared in the meantime. An address whose earlier request was rejected or
  expired, or whose account has since been deleted, is free to apply again - the old request is
  replaced and the earlier decision is cleared, so the new one reaches the queue as pending.
- **Deleting a user.** Removing an account also removes the registration request that created
  it. Nothing is left behind to block that person from applying again.
- **Approval requires a verified request** - pending requests cannot be approved directly.
- **Emails not sending?** Delivery failures are non-fatal - the request still appears in the
  admin queue so it can be processed.
