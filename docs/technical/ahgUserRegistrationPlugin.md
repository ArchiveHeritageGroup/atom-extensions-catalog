# ahgUserRegistrationPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Public user self-registration with email verification and admin approval workflow

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
- Configurable default group assignment

## Database tables

- `ahg_registration_request`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

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

**`userRegistration`** — `register`, `verify`, `pending`, `markVerified`, `approve`, `reject`

## CLI tasks

- `php symfony registration:cleanup` — Clean up expired registration requests

## Service layer

### `RegistrationService`  
`lib/Services/RegistrationService.php`

Public methods: `createRequest()`, `verifyEmail()`, `markVerified()`, `getPendingRegistrations()`, `getAllRegistrations()`, `approve()`, `reject()`, `cleanupExpired()`, `getRequest()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
