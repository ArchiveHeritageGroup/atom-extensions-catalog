# ahgUserRegistrationPlugin - Technical Documentation

> Maintained by hand. Last reviewed 2026-08-13. Public user self-registration with email verification and admin approval workflow

## Overview

- **Name:** AHG User Registration
- **Machine name:** `ahgUserRegistrationPlugin`
- **Version:** 1.0.0
- **Category:** user
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

### Features

- Public self-registration form
- Email verification with token
- Admin approval queue
- Role assignment on approval
- Email notifications (new registration, approval, rejection)
- Rate limiting per IP
- Configurable default group assignment (default: authenticated, group 99)
- Administrator notification of waiting requests (AhgNav badge + injected banner)
- Re-application on an address whose earlier request is finished

## Database tables

- `ahg_registration_request`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

### `user_id` and the cascading delete

`ahg_registration_request.user_id` records the account an approval created, with

```sql
FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE
```

so deleting a user deletes the request that produced it. This is a database constraint rather
than application code on purpose: AtoM deletes users from base code this plugin cannot hook,
and users also disappear via CLI tasks and via the `object` -> `actor` -> `user` cascade. A
cleanup in one code path would be missed by the others.

Without it the request outlived the account, and because `uk_email` is UNIQUE across *every*
status - not just pending and verified - that orphan made the address permanently
unregisterable: the insert broke on the unique index and surfaced as an unhandled error page.

Applied by `database/migrations/2026_08_12_link_request_to_user.sql`, which is guarded on the
column, index and constraint and is safe to re-run.

> **Joining to `user` on a string column needs an explicit collation.** AtoM's `user` table is
> `utf8mb4_0900_ai_ci` (the MySQL 8 default) while this plugin's table declares
> `utf8mb4_unicode_ci`, so a bare `u.email = r.email` fails with *Illegal mix of collations*.
> Put `COLLATE utf8mb4_general_ci` on both sides - it exists on MySQL 5.7, MySQL 8 and MariaDB,
> whereas `utf8mb4_0900_ai_ci` does not. This applies to any AHG plugin table joined to a core
> AtoM table.

## Routes

| Route name | URL | Action |
|---|---|---|
| `user_register` | `/register` | register |
| `user_verify_email` | `/register/verify/:token` | verify |
| `admin_registrations_approve` | `/admin/registrations/approve` | approve |
| `admin_registrations_verify` | `/admin/registrations/verify` | markVerified |
| `admin_registrations_reject` | `/admin/registrations/reject` | reject |
| `admin_registrations` | `/admin/registrations` | pending |

## Module actions

**`userRegistration`** - `register`, `verify`, `pending`, `markVerified`, `approve`, `reject`

## CLI tasks

- `php symfony registration:cleanup` - Clean up expired registration requests

## Service layer

### `RegistrationService`  
`lib/Services/RegistrationService.php`

Public methods: `createRequest()`, `verifyEmail()`, `markVerified()`, `getPendingRegistrations()`, `getAllRegistrations()`, `approve()`, `reject()`, `cleanupExpired()`, `getRequest()`

State handling worth knowing:

- `createRequest()` considers a request in **any** status. One awaiting review is refused; a
  finished one with no live account is reused in place, clearing the earlier decision so the
  new application reaches the queue as pending. The write is wrapped, so a race returns a
  message rather than an error page.
- `approve()` and `markVerified()` answer for the state the request is actually in. Already
  approved returns `success` with `already: true` and the existing `user_id`, returning before
  the transaction so nothing is written twice. Rejected and expired get their own messages.
  Reporting "already done" as a failure is what made a working approval look broken when an
  administrator clicked twice.
- Approval writes a password hash AtoM itself can verify - `password_hash(sha1(salt . password))`
  with a random 16-byte salt - not Argon2id, which stock `QubitUser::checkCredentials()` cannot
  read.

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
