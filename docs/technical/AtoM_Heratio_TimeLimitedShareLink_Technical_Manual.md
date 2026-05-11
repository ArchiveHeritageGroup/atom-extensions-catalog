# Time-Limited Share Link — Technical Manual

**Plugin:** `ahgTimeLimitedShareLinkPlugin` (AtoM) / `ahg-share-link` (Heratio)
**Version:** 0.1.0
**Audience:** Developers and DBAs operating an AtoM Heratio installation
**Cross-surface:** byte-equivalent schema, audit payload, and token format on both AtoM (Symfony 1.x) and Heratio (Laravel)

---

## 1. Schema

Two tables. Both are mirrored verbatim across AtoM (archive DB) and Heratio (heratio DB).

### 1.1 `information_object_share_token`

```sql
CREATE TABLE information_object_share_token (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    information_object_id INT NOT NULL,
    token VARCHAR(64) NOT NULL UNIQUE,
    issued_by INT NOT NULL,
    recipient_email VARCHAR(320) NULL,
    recipient_note TEXT NULL,
    expires_at DATETIME NOT NULL,
    max_access INT UNSIGNED NULL,
    access_count INT UNSIGNED NOT NULL DEFAULT 0,
    revoked_at DATETIME NULL,
    classification_level_at_issuance INT NULL,
    issuer_download_at_issuance TINYINT(1) NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    INDEX idx_share_token_expires (expires_at),
    INDEX idx_share_token_revoked (revoked_at),
    INDEX idx_share_token_io (information_object_id),
    CONSTRAINT fk_share_token_io FOREIGN KEY (information_object_id)
        REFERENCES information_object (id) ON DELETE CASCADE,
    CONSTRAINT fk_share_token_issuer FOREIGN KEY (issued_by)
        REFERENCES user (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### 1.2 `information_object_share_access`

```sql
CREATE TABLE information_object_share_access (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    token_id BIGINT UNSIGNED NOT NULL,
    accessed_at DATETIME NOT NULL,
    ip_address VARCHAR(45) NULL,
    user_agent VARCHAR(500) NULL,
    action VARCHAR(20) NOT NULL COMMENT 'view, denied_expired, denied_revoked, denied_quota, denied_unknown',
    INDEX idx_share_access_token (token_id),
    INDEX idx_share_access_when (accessed_at),
    CONSTRAINT fk_share_access_token FOREIGN KEY (token_id)
        REFERENCES information_object_share_token (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

The `action` column is intentionally VARCHAR (not ENUM) per the project's "no ENUMs" rule.

---

## 2. Token format

| Step                     | Value                                             |
|--------------------------|---------------------------------------------------|
| Input — io_id            | the information_object's primary key (integer)    |
| Input — expiry_unix      | `expires_at` as unix timestamp                    |
| Input — recipient_email  | the recipient email or empty string               |
| Input — nonce_hex        | `bin2hex(random_bytes(16))` per call              |
| Input format             | `{io_id}\|{expiry_unix}\|{recipient_email}\|{nonce_hex}` |
| HMAC algorithm           | SHA-256                                           |
| HMAC key                 | `ahg_settings.share_link.hmac_secret` (64 hex chars, auto-bootstrapped) |
| Output                   | base64url, unpadded — exactly 43 characters       |
| Storage                  | `information_object_share_token.token` (UNIQUE)   |

10,000-iteration collision test in development was uniqueness-clean; the 256-bit random nonce per call dominates the entropy.

---

## 3. Services

Both surfaces use the same class names under namespace `AhgShareLink\Services\`. AtoM uses an autoloader that maps the namespace to `lib/Services/`; Heratio uses PSR-4 from `packages/ahg-share-link/src/Services/`.

| Class             | Responsibility                                                                |
|-------------------|--------------------------------------------------------------------------------|
| `TokenService`    | Generate token (Section 2). Bootstrap the HMAC secret if missing.             |
| `AclCheck`        | 5 permission constants. Admin (group 100) bypass. User grants then group grants. |
| `ClearanceCheck`  | Resolve the record's classification level. Compare against the user's clearance under `ahgSecurityClearancePlugin`. Fails open if the plugin schema is missing. |
| `IssueService`    | Run every issue guard (auth, ACL, classified, expiry cap), insert the token, dual-write the audit row. |
| `AccessService`   | Look up token, evaluate guards (revoked / expired / quota), atomically log access + increment counter (transactional), dual-write audit. Returns an `AccessResult` value object. |
| `RevokeService`   | Idempotent revoke with own-vs-others ACL check. Audits real revocations only. |
| `PruneService`    | Two independent sweeps (Section 7). Reads retention from `ahg_settings`. Audits non-empty runs only. |
| `AccessResult`    | Final-property value object: `allowed`, `tokenRow`, `action`, `reason`, `httpStatus`. |

### 3.1 Exception hierarchy

```
\RuntimeException
 └── ShareLinkException
      ├── NotAuthenticatedException        → HTTP 401
      ├── PermissionDeniedException        → HTTP 403
      ├── InsufficientClearanceException   → HTTP 403
      ├── ExpiryCapExceededException       → HTTP 422
      └── InvalidRequestException          → HTTP 422
```

Each class lives in its own file (PSR-4 one-class-per-file).

---

## 4. HTTP routes

| Method | URL                                       | AtoM module/action        | Heratio name                  | Auth      |
|:-------|-------------------------------------------|---------------------------|-------------------------------|-----------|
| GET    | `/share/{token}`                          | `shareLink/recipient`     | `share-link.recipient`        | none (token IS credential) |
| POST   | `/shareLink/issue` (AtoM) `/share-link/issue` (Heratio) | `shareLink/issue`         | `share-link.issue`            | session   |
| GET    | `/admin/share-links`                      | `shareLink/admin`         | `share-link.admin.index`      | session + ACL `share_link.list_all` |
| GET    | `/admin/share-links/{id}`                 | `shareLink/adminShow`     | `share-link.admin.show`       | session + ACL `share_link.list_all` |
| POST   | `/admin/share-links/{id}/revoke`          | `shareLink/revoke`        | `share-link.admin.revoke`     | session + ACL (own or `share_link.revoke_others`) |

Token regex: `[A-Za-z0-9_\-]{32,64}`. The base64url shape rules out path-traversal injection.

The recipient route is intentionally **outside** the `auth` middleware — the token is the credential. Every guard is enforced by `AccessService`, not by route middleware.

---

## 5. JSON contracts (issue endpoint)

### 5.1 Success (201)

```json
{
  "ok": true,
  "token": "abc...xyz",
  "token_id": 42,
  "expires_at": "2026-05-25 14:00:00",
  "public_url": "https://psis.theahg.co.za/share/abc...xyz"
}
```

### 5.2 Error (status varies)

```json
{
  "ok": false,
  "error": {
    "code": "permission_denied",
    "message": "You do not have permission to issue share links"
  }
}
```

Error codes: `not_authenticated` (401), `permission_denied` (403), `insufficient_clearance` (403), `expiry_cap_exceeded` (422), `invalid_request` (422), `server_error` (500), `method_not_allowed` (405).

---

## 6. UI injection

Both surfaces inject the **Share this record** button + Bootstrap 5 modal into IO show pages via a server-side HTML rewrite — the locked descriptive-standard show templates are never touched.

### 6.1 AtoM

A `response.filter_content` event listener (`lib/Listeners/ViewLinkInjector.php`) checks:

- module is one of: `informationobject`, `sfIsadPlugin`, `sfRadPlugin`, `sfDcPlugin`, `sfModsPlugin`, `sfDacsPlugin`
- action is one of: `index`, `view`, `show`
- request method GET, not XHR
- response Content-Type `text/html`
- user authenticated AND has `share_link.create`

If yes, the listener appends the banner + modal HTML just after the first match of `<div id="main-column">`, `<main>`, or `.content` opening tag. The `<script>` tag carries the CSP nonce read from `sfConfig::get('csp_nonce')`.

### 6.2 Heratio

A response middleware (`src/Http/Middleware/ShareLinkInjector.php`) is appended to the `web` middleware group in `bootstrap/app.php`. Same logic, slug-based resolution (Heratio's IO show is `/{slug}` via catch-all). The CSP nonce comes from `app('csp-nonce')` — `InjectCspNonces` later re-checks any inline script without a nonce, so the chain is safe even if the lookup misses.

---

## 7. Retention pruning

```php
// Sweep 1 — tokens
DELETE FROM information_object_share_token
WHERE (expires_at IS NOT NULL AND expires_at < <token_cutoff>)
   OR (revoked_at IS NOT NULL AND revoked_at < <token_cutoff>);
-- CASCADE removes child access rows

// Sweep 2 — access log
DELETE FROM information_object_share_access
WHERE accessed_at < <access_cutoff>;
```

`<token_cutoff>`  = `NOW() - share_link.token_retain_days days` (default 365)
`<access_cutoff>` = `NOW() - share_link.access_log_retain_days days` (default 180)

Each non-empty run writes one `share_link_prune` row to `ahg_audit_log`. No-op runs write nothing.

CLI:
- AtoM:    `php symfony share-link:prune [--dry-run]`
- Heratio: `php artisan share-link:prune [--dry-run]`

Recommended cron: `15 3 * * *` (daily 03:15).

---

## 8. ACL

### 8.1 Permissions

5 actions in `acl_permission.action`:

| Action                                  | Effect                                                  |
|-----------------------------------------|---------------------------------------------------------|
| `share_link.create`                     | Open the Share modal, POST `/.../issue`                 |
| `share_link.create_classified`          | Allow issuance for records with non-null classification |
| `share_link.create_unlimited_expiry`    | Bypass the `max_expiry_days` cap                        |
| `share_link.list_all`                   | View `/admin/share-links` and per-token detail          |
| `share_link.revoke_others`              | Revoke a link issued by a different user                |

### 8.2 Default grants

Seed file `database/seed-acl-permissions.sql` (idempotent, NOT-EXISTS-guarded):

| Group | Granted actions                                            |
|-------|------------------------------------------------------------|
| 101 editor       | create, list_all, revoke_others                |
| 102 contributor  | create                                          |
| 103 translator   | none                                            |

Administrator (100) bypasses every check in code (`AclCheck::ACL_GROUP_ADMINISTRATOR`).

Heratio applies the same seeds via migration `2026_05_12_000020_seed_share_link_acl_permissions`.

---

## 9. Audit shape

All rows written to `ahg_audit_log` with `module = 'share_link'`.

| `action`                | `entity_type`                         | `action_name`                            | `status`              |
|-------------------------|---------------------------------------|------------------------------------------|-----------------------|
| `share_link_issued`     | `information_object_share_token`      | `issue`                                  | `success`             |
| `share_link_accessed`   | `information_object_share_token`      | `view` / `denied_expired` / `denied_revoked` / `denied_quota` / `denied_unknown` | `success` / `failure` |
| `share_link_revoked`    | `information_object_share_token`      | `revoke`                                 | `success`             |
| `share_link_prune`      | `information_object_share_token`      | `prune`                                  | `success`             |

`metadata` JSON shape per action:

```jsonc
// share_link_issued
{
  "token_id": 42,
  "expires_at": "2026-05-25 14:00:00",
  "recipient_email": "r@example.com",
  "recipient_note": "free text",
  "max_access": 5,
  "classification_level": null,
  "parent_entity_type": "information_object",
  "parent_entity_id": 553
}

// share_link_accessed
{
  "token_id": 42,
  "access_action": "view",
  "parent_entity_type": "information_object",
  "parent_entity_id": 553,
  "recipient_email": "r@example.com"
}

// share_link_revoked
{
  "token_id": 42,
  "parent_entity_type": "information_object",
  "parent_entity_id": 553,
  "recipient_email": "r@example.com",
  "expires_at": "2026-05-25 14:00:00",
  "access_count": 3,
  "was_owner": true,
  "reason": "User requested revoke"
}

// share_link_prune
{
  "tokens_deleted": 17,
  "access_rows_deleted": 412,
  "token_retain_days": 365,
  "access_log_retain_days": 180,
  "dry_run": false
}
```

---

## 10. Settings

Stored in `ahg_settings` with `setting_group = 'share_link'`.

| Key                                       | Type     | Default    | Notes |
|-------------------------------------------|----------|-----------|-------|
| `share_link.default_expiry_days`          | integer  | 14        | Pre-fill in the Share modal |
| `share_link.max_expiry_days`              | integer  | 90        | Hard cap unless `share_link.create_unlimited_expiry` |
| `share_link.token_retain_days`            | integer  | 365       | Retention for token rows |
| `share_link.access_log_retain_days`       | integer  | 180       | Retention for access-log rows |
| `share_link.hmac_secret`                  | string (sensitive) | auto | 64-hex per-install HMAC key |

Admin UI:

- AtoM: **Admin > AHG Settings > Share Links** (integrated section in `ahgSettingsPlugin`).
- Heratio: **`/admin/settings/ahg/share_link`** (served by the generic `ahgSection` handler in `ahg-settings`).

---

## 11. Concurrency notes

- **Quota race.** `AccessService` wraps the access-log insert + `access_count` increment in a single transaction. The guard `access_count >= max_access` runs **before** the transaction, so two near-simultaneous requests at quota minus one CAN both pass the guard and both succeed; the access_count ends at `max_access + 1`. This is an acceptable trade-off — alternative (`SELECT FOR UPDATE` then increment) costs a row lock per recipient hit. The hard ceiling is enforced on the *next* request.
- **Issue collisions.** Token uniqueness is enforced by a UNIQUE constraint on the `token` column. The 256-bit random nonce per call makes collisions vanishingly unlikely; the DB will reject any duplicate with a `Duplicate entry` error and the caller's transaction rolls back.

---

## 12. Test coverage

- **Phase B/C:** 100-iteration token-uniqueness + admin issuance + 4-guard rejection paths.
- **Phase D:** valid / expired / revoked / quota-exhausted / bogus → HTTP code + audit row + DB state.
- **Phase E:** authenticated POST `/.../issue` → JSON contract; 7 guard rejection paths.
- **Phase F:** 5 filter buckets × admin list + detail + 404.
- **Phase G:** admin own / admin others / contributor own / contributor others (denied) / anonymous (denied) / idempotent re-revoke / bogus id → 404.
- **Phase H:** dry-run / real-run / no-op-no-audit / settings-override / per-row retention math.
- **Phase I:** ACL admin bypass + editor grants + classified/unlimited admin-only.
- **Phase K:** all 4 audit actions × metadata shape + audit page renders.

Full regression sweep: **34/34** assertions pass on Heratio. AtoM-port surface verified service-level via Capsule against the archive DB.

---

## 13. Operations runbook

| Scenario                                  | Action                                                                          |
|-------------------------------------------|---------------------------------------------------------------------------------|
| Recipient reports broken link             | Check `/admin/share-links?q=<token-prefix>`. Status column tells you whether expired/revoked/quota. |
| Need to invalidate every existing link    | Rotate `share_link.hmac_secret` in the DB (no UI button by design). All existing tokens fail HMAC re-derivation. Audit row is NOT written for rotation; do this only in coordination with archive management. |
| Audit log growing too fast                | Lower `share_link.access_log_retain_days`. Next nightly prune trims the older rows. |
| Plugin disabled in atom_plugin            | Set `is_enabled = 1`; `php symfony cc`; restart `php8.3-fpm`. |
| Plugin needs to be reinstalled            | Idempotent: re-run `database/install.sql` (CREATE TABLE IF NOT EXISTS) and `database/seed-acl-permissions.sql` (NOT EXISTS guards). |

---

## 14. Files of record

```
ahgTimeLimitedShareLinkPlugin/
├── config/ahgTimeLimitedShareLinkPluginConfiguration.class.php
├── database/install.sql
├── database/seed-acl-permissions.sql
├── extension.json
├── lib/
│   ├── Listeners/ViewLinkInjector.php
│   ├── Services/AccessResult.php
│   ├── Services/AccessService.php
│   ├── Services/AclCheck.php
│   ├── Services/ClearanceCheck.php
│   ├── Services/Exceptions/*.php      (one class per file)
│   ├── Services/IssueService.php
│   ├── Services/PruneService.php
│   ├── Services/RevokeService.php
│   └── Services/TokenService.php
├── lib/task/shareLinkPruneTask.class.php
└── modules/shareLink/
    ├── actions/actions.class.php
    └── templates/
        ├── adminShowSuccess.php
        ├── adminSuccess.php
        ├── deniedSuccess.php
        ├── errorSuccess.php
        └── recipientSuccess.php

ahg-share-link/                              # Heratio
├── composer.json
├── database/install.sql
├── database/seed-acl-permissions.sql
├── database/migrations/
│   ├── 2026_05_12_000010_create_share_link_tables.php
│   └── 2026_05_12_000020_seed_share_link_acl_permissions.php
├── resources/views/
│   ├── admin/index.blade.php
│   ├── admin/show.blade.php
│   ├── denied.blade.php
│   └── recipient.blade.php
├── routes/web.php
└── src/
    ├── Console/PruneCommand.php
    ├── Controllers/ShareLinkAdminController.php
    ├── Controllers/ShareLinkIssueController.php
    ├── Controllers/ShareLinkRecipientController.php
    ├── Http/Middleware/ShareLinkInjector.php
    ├── Providers/AhgShareLinkServiceProvider.php
    └── Services/                            # mirror of AtoM
```

---

© 2026 The Archive and Heritage Group (Pty) Ltd. AGPL-3.0-or-later.
