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

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 402 132" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="401" height="131" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="20.8" y1="34.0" x2="24.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="26.0" x2="20.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="34.0" x2="28.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="34.0" x2="31.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="34.0" x2="35.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="34.0" x2="38.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="50.0" x2="60.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="42.0" x2="56.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="50.0" x2="56.8" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="50.0" x2="64.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="50.0" x2="67.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="50.0" x2="71.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="50.0" x2="74.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="66.0" x2="60.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="58.0" x2="56.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="66.0" x2="56.8" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="66.0" x2="64.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="66.0" x2="67.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="66.0" x2="71.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="66.0" x2="74.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="82.0" x2="60.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="74.0" x2="56.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="82.0" x2="56.8" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="82.0" x2="64.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="82.0" x2="67.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="82.0" x2="71.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="82.0" x2="74.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="98.0" x2="60.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="90.0" x2="56.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="98.0" x2="56.8" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="98.0" x2="64.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="98.0" x2="67.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="98.0" x2="71.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="98.0" x2="74.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="114.0" x2="60.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="106.0" x2="56.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="114.0" x2="64.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="114.0" x2="67.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="114.0" x2="71.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="114.0" x2="74.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><path d="M318.2 46.0 L325.2 50.0 L318.2 54.0 Z" fill="#10373E"/><path d="M318.2 62.0 L325.2 66.0 L318.2 70.0 Z" fill="#10373E"/><path d="M318.2 78.0 L325.2 82.0 L318.2 86.0 Z" fill="#10373E"/><path d="M318.2 94.0 L325.2 98.0 L318.2 102.0 Z" fill="#10373E"/><path d="M318.2 110.0 L325.2 114.0 L318.2 118.0 Z" fill="#10373E"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">\RuntimeException</text><text x="46.0" y="38.0" font-size="9.5" fill="#10373E">ShareLinkException</text><text x="82.0" y="54.0" font-size="9.5" fill="#10373E">NotAuthenticatedException</text><text x="334.0" y="54.0" font-size="9.5" fill="#10373E">HTTP</text><text x="370.0" y="54.0" font-size="9.5" fill="#10373E">401</text><text x="82.0" y="70.0" font-size="9.5" fill="#10373E">PermissionDeniedException</text><text x="334.0" y="70.0" font-size="9.5" fill="#10373E">HTTP</text><text x="370.0" y="70.0" font-size="9.5" fill="#10373E">403</text><text x="82.0" y="86.0" font-size="9.5" fill="#10373E">InsufficientClearanceException</text><text x="334.0" y="86.0" font-size="9.5" fill="#10373E">HTTP</text><text x="370.0" y="86.0" font-size="9.5" fill="#10373E">403</text><text x="82.0" y="102.0" font-size="9.5" fill="#10373E">ExpiryCapExceededException</text><text x="334.0" y="102.0" font-size="9.5" fill="#10373E">HTTP</text><text x="370.0" y="102.0" font-size="9.5" fill="#10373E">422</text><text x="82.0" y="118.0" font-size="9.5" fill="#10373E">InvalidRequestException</text><text x="334.0" y="118.0" font-size="9.5" fill="#10373E">HTTP</text><text x="370.0" y="118.0" font-size="9.5" fill="#10373E">422</text></svg></div>

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

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 474 772" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="473" height="771" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="34.0" x2="17.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="34.0" x2="20.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="34.0" x2="24.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="34.0" x2="28.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="34.0" x2="31.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="17.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="50.0" x2="20.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="50.0" x2="24.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="50.0" x2="28.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="50.0" x2="31.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="17.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="13.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="66.0" x2="20.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="66.0" x2="24.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="66.0" x2="28.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="66.0" x2="31.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="17.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="74.0" x2="13.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="13.6" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="82.0" x2="20.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="82.0" x2="24.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="82.0" x2="28.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="82.0" x2="31.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="17.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="90.0" x2="13.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="13.6" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="98.0" x2="20.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="98.0" x2="24.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="98.0" x2="28.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="98.0" x2="31.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="106.0" x2="13.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="13.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="114.0" x2="46.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="106.0" x2="42.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="114.0" x2="42.4" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="114.0" x2="49.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="114.0" x2="53.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="114.0" x2="56.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="114.0" x2="60.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="122.0" x2="13.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="13.6" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="46.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="122.0" x2="42.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="42.4" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="130.0" x2="49.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="130.0" x2="53.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="130.0" x2="56.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="130.0" x2="60.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="138.0" x2="13.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="13.6" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="146.0" x2="46.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="138.0" x2="42.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="146.0" x2="42.4" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="146.0" x2="49.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="146.0" x2="53.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="146.0" x2="56.8" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="146.0" x2="60.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="154.0" x2="13.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="13.6" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="162.0" x2="46.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="154.0" x2="42.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="162.0" x2="42.4" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="162.0" x2="49.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="162.0" x2="53.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="162.0" x2="56.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="162.0" x2="60.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="170.0" x2="13.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="13.6" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="178.0" x2="46.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="170.0" x2="42.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="178.0" x2="42.4" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="178.0" x2="49.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="178.0" x2="53.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="178.0" x2="56.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="178.0" x2="60.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="186.0" x2="13.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="194.0" x2="13.6" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="194.0" x2="46.0" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="186.0" x2="42.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="194.0" x2="42.4" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="194.0" x2="49.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="194.0" x2="53.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="194.0" x2="56.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="194.0" x2="60.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="202.0" x2="13.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="210.0" x2="13.6" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="210.0" x2="46.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="202.0" x2="42.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="210.0" x2="42.4" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="210.0" x2="49.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="210.0" x2="53.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="210.0" x2="56.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="210.0" x2="60.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="218.0" x2="13.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="226.0" x2="13.6" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="226.0" x2="46.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="218.0" x2="42.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="226.0" x2="42.4" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="226.0" x2="49.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="226.0" x2="53.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="226.0" x2="56.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="226.0" x2="60.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="234.0" x2="13.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="242.0" x2="13.6" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="242.0" x2="46.0" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="234.0" x2="42.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="242.0" x2="42.4" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="242.0" x2="49.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="242.0" x2="53.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="242.0" x2="56.8" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="242.0" x2="60.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="250.0" x2="13.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="258.0" x2="13.6" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="258.0" x2="46.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="250.0" x2="42.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="258.0" x2="49.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="258.0" x2="53.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="258.0" x2="56.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="258.0" x2="60.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="274.0" x2="17.2" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="266.0" x2="13.6" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="274.0" x2="13.6" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="274.0" x2="20.8" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="274.0" x2="24.4" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="274.0" x2="28.0" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="274.0" x2="31.6" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="290.0" x2="17.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="282.0" x2="13.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="290.0" x2="20.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="290.0" x2="24.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="290.0" x2="28.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="290.0" x2="31.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="306.0" x2="46.0" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="298.0" x2="42.4" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="306.0" x2="42.4" y2="314.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="306.0" x2="49.6" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="306.0" x2="53.2" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="306.0" x2="56.8" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="306.0" x2="60.4" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="322.0" x2="46.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="314.0" x2="42.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="322.0" x2="49.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="322.0" x2="53.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="322.0" x2="56.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="322.0" x2="60.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="338.0" x2="74.8" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="330.0" x2="71.2" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="338.0" x2="71.2" y2="346.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="338.0" x2="78.4" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="338.0" x2="82.0" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="338.0" x2="85.6" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="338.0" x2="89.2" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="354.0" x2="74.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="346.0" x2="71.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="354.0" x2="71.2" y2="362.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="354.0" x2="78.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="354.0" x2="82.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="354.0" x2="85.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="354.0" x2="89.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="370.0" x2="74.8" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="362.0" x2="71.2" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="370.0" x2="71.2" y2="378.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="370.0" x2="78.4" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="370.0" x2="82.0" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="370.0" x2="85.6" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="370.0" x2="89.2" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="386.0" x2="74.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="378.0" x2="71.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="386.0" x2="71.2" y2="394.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="386.0" x2="78.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="386.0" x2="82.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="386.0" x2="85.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="386.0" x2="89.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="402.0" x2="74.8" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="394.0" x2="71.2" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="402.0" x2="78.4" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="402.0" x2="82.0" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="402.0" x2="85.6" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="402.0" x2="89.2" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="450.0" x2="17.2" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="442.0" x2="13.6" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="450.0" x2="13.6" y2="458.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="450.0" x2="20.8" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="450.0" x2="24.4" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="450.0" x2="28.0" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="450.0" x2="31.6" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="466.0" x2="17.2" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="458.0" x2="13.6" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="466.0" x2="13.6" y2="474.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="466.0" x2="20.8" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="466.0" x2="24.4" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="466.0" x2="28.0" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="466.0" x2="31.6" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="482.0" x2="17.2" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="474.0" x2="13.6" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="482.0" x2="13.6" y2="490.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="482.0" x2="20.8" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="482.0" x2="24.4" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="482.0" x2="28.0" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="482.0" x2="31.6" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="498.0" x2="17.2" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="490.0" x2="13.6" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="498.0" x2="13.6" y2="506.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="498.0" x2="20.8" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="498.0" x2="24.4" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="498.0" x2="28.0" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="498.0" x2="31.6" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="506.0" x2="13.6" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="514.0" x2="13.6" y2="522.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="514.0" x2="46.0" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="506.0" x2="42.4" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="514.0" x2="42.4" y2="522.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="514.0" x2="49.6" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="514.0" x2="53.2" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="514.0" x2="56.8" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="514.0" x2="60.4" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="522.0" x2="13.6" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="530.0" x2="13.6" y2="538.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="530.0" x2="46.0" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="522.0" x2="42.4" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="530.0" x2="49.6" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="530.0" x2="53.2" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="530.0" x2="56.8" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="530.0" x2="60.4" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="546.0" x2="17.2" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="538.0" x2="13.6" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="546.0" x2="13.6" y2="554.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="546.0" x2="20.8" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="546.0" x2="24.4" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="546.0" x2="28.0" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="546.0" x2="31.6" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="554.0" x2="13.6" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="562.0" x2="13.6" y2="570.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="562.0" x2="46.0" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="554.0" x2="42.4" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="562.0" x2="42.4" y2="570.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="562.0" x2="49.6" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="562.0" x2="53.2" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="562.0" x2="56.8" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="562.0" x2="60.4" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="570.0" x2="13.6" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="578.0" x2="13.6" y2="586.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="578.0" x2="46.0" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="570.0" x2="42.4" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="578.0" x2="42.4" y2="586.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="578.0" x2="49.6" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="578.0" x2="53.2" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="578.0" x2="56.8" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="578.0" x2="60.4" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="586.0" x2="13.6" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="594.0" x2="13.6" y2="602.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="594.0" x2="46.0" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="586.0" x2="42.4" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="594.0" x2="42.4" y2="602.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="594.0" x2="49.6" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="594.0" x2="53.2" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="594.0" x2="56.8" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="594.0" x2="60.4" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="602.0" x2="13.6" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="610.0" x2="13.6" y2="618.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="610.0" x2="46.0" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="602.0" x2="42.4" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="610.0" x2="49.6" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="610.0" x2="53.2" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="610.0" x2="56.8" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="610.0" x2="60.4" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="626.0" x2="17.2" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="618.0" x2="13.6" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="626.0" x2="13.6" y2="634.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="626.0" x2="20.8" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="626.0" x2="24.4" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="626.0" x2="28.0" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="626.0" x2="31.6" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="642.0" x2="17.2" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="634.0" x2="13.6" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="642.0" x2="20.8" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="642.0" x2="24.4" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="642.0" x2="28.0" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="642.0" x2="31.6" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="658.0" x2="46.0" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="650.0" x2="42.4" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="658.0" x2="42.4" y2="666.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="658.0" x2="49.6" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="658.0" x2="53.2" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="658.0" x2="56.8" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="658.0" x2="60.4" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="674.0" x2="46.0" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="666.0" x2="42.4" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="674.0" x2="42.4" y2="682.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="674.0" x2="49.6" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="674.0" x2="53.2" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="674.0" x2="56.8" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="674.0" x2="60.4" y2="674.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="690.0" x2="46.0" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="682.0" x2="42.4" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="690.0" x2="42.4" y2="698.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="690.0" x2="49.6" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="690.0" x2="53.2" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="690.0" x2="56.8" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="690.0" x2="60.4" y2="690.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="706.0" x2="46.0" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="698.0" x2="42.4" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="706.0" x2="42.4" y2="714.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="706.0" x2="49.6" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="706.0" x2="53.2" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="706.0" x2="56.8" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="706.0" x2="60.4" y2="706.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="722.0" x2="46.0" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="714.0" x2="42.4" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="722.0" x2="42.4" y2="730.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="722.0" x2="49.6" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="722.0" x2="53.2" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="722.0" x2="56.8" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="722.0" x2="60.4" y2="722.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="738.0" x2="46.0" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="730.0" x2="42.4" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="738.0" x2="42.4" y2="746.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="738.0" x2="49.6" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="738.0" x2="53.2" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="738.0" x2="56.8" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="738.0" x2="60.4" y2="738.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="754.0" x2="46.0" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="746.0" x2="42.4" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="754.0" x2="49.6" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="754.0" x2="53.2" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="754.0" x2="56.8" y2="754.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="754.0" x2="60.4" y2="754.0" stroke="#10373E" stroke-width="1.3"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">ahgTimeLimitedShareLinkPlugin/</text><text x="38.8" y="38.0" font-size="9.5" fill="#10373E">config/ahgTimeLimitedShareLinkPluginConfiguration.class.php</text><text x="38.8" y="54.0" font-size="9.5" fill="#10373E">database/install.sql</text><text x="38.8" y="70.0" font-size="9.5" fill="#10373E">database/seed-acl-permissions.sql</text><text x="38.8" y="86.0" font-size="9.5" fill="#10373E">extension.json</text><text x="38.8" y="102.0" font-size="9.5" fill="#10373E">lib/</text><text x="67.6" y="118.0" font-size="9.5" fill="#10373E">Listeners/ViewLinkInjector.php</text><text x="67.6" y="134.0" font-size="9.5" fill="#10373E">Services/AccessResult.php</text><text x="67.6" y="150.0" font-size="9.5" fill="#10373E">Services/AccessService.php</text><text x="67.6" y="166.0" font-size="9.5" fill="#10373E">Services/AclCheck.php</text><text x="67.6" y="182.0" font-size="9.5" fill="#10373E">Services/ClearanceCheck.php</text><text x="67.6" y="198.0" font-size="9.5" fill="#10373E">Services/Exceptions/*.php</text><text x="290.8" y="198.0" font-size="9.5" fill="#10373E">(one</text><text x="326.8" y="198.0" font-size="9.5" fill="#10373E">class</text><text x="370.0" y="198.0" font-size="9.5" fill="#10373E">per</text><text x="398.8" y="198.0" font-size="9.5" fill="#10373E">file)</text><text x="67.6" y="214.0" font-size="9.5" fill="#10373E">Services/IssueService.php</text><text x="67.6" y="230.0" font-size="9.5" fill="#10373E">Services/PruneService.php</text><text x="67.6" y="246.0" font-size="9.5" fill="#10373E">Services/RevokeService.php</text><text x="67.6" y="262.0" font-size="9.5" fill="#10373E">Services/TokenService.php</text><text x="38.8" y="278.0" font-size="9.5" fill="#10373E">lib/task/shareLinkPruneTask.class.php</text><text x="38.8" y="294.0" font-size="9.5" fill="#10373E">modules/shareLink/</text><text x="67.6" y="310.0" font-size="9.5" fill="#10373E">actions/actions.class.php</text><text x="67.6" y="326.0" font-size="9.5" fill="#10373E">templates/</text><text x="96.4" y="342.0" font-size="9.5" fill="#10373E">adminShowSuccess.php</text><text x="96.4" y="358.0" font-size="9.5" fill="#10373E">adminSuccess.php</text><text x="96.4" y="374.0" font-size="9.5" fill="#10373E">deniedSuccess.php</text><text x="96.4" y="390.0" font-size="9.5" fill="#10373E">errorSuccess.php</text><text x="96.4" y="406.0" font-size="9.5" fill="#10373E">recipientSuccess.php</text><text x="10.0" y="438.0" font-size="9.5" fill="#10373E">ahg-share-link/</text><text x="334.0" y="438.0" font-size="9.5" fill="#10373E">#</text><text x="348.4" y="438.0" font-size="9.5" fill="#10373E">Heratio</text><text x="38.8" y="454.0" font-size="9.5" fill="#10373E">composer.json</text><text x="38.8" y="470.0" font-size="9.5" fill="#10373E">database/install.sql</text><text x="38.8" y="486.0" font-size="9.5" fill="#10373E">database/seed-acl-permissions.sql</text><text x="38.8" y="502.0" font-size="9.5" fill="#10373E">database/migrations/</text><text x="67.6" y="518.0" font-size="9.5" fill="#10373E">2026_05_12_000010_create_share_link_tables.php</text><text x="67.6" y="534.0" font-size="9.5" fill="#10373E">2026_05_12_000020_seed_share_link_acl_permissions.php</text><text x="38.8" y="550.0" font-size="9.5" fill="#10373E">resources/views/</text><text x="67.6" y="566.0" font-size="9.5" fill="#10373E">admin/index.blade.php</text><text x="67.6" y="582.0" font-size="9.5" fill="#10373E">admin/show.blade.php</text><text x="67.6" y="598.0" font-size="9.5" fill="#10373E">denied.blade.php</text><text x="67.6" y="614.0" font-size="9.5" fill="#10373E">recipient.blade.php</text><text x="38.8" y="630.0" font-size="9.5" fill="#10373E">routes/web.php</text><text x="38.8" y="646.0" font-size="9.5" fill="#10373E">src/</text><text x="67.6" y="662.0" font-size="9.5" fill="#10373E">Console/PruneCommand.php</text><text x="67.6" y="678.0" font-size="9.5" fill="#10373E">Controllers/ShareLinkAdminController.php</text><text x="67.6" y="694.0" font-size="9.5" fill="#10373E">Controllers/ShareLinkIssueController.php</text><text x="67.6" y="710.0" font-size="9.5" fill="#10373E">Controllers/ShareLinkRecipientController.php</text><text x="67.6" y="726.0" font-size="9.5" fill="#10373E">Http/Middleware/ShareLinkInjector.php</text><text x="67.6" y="742.0" font-size="9.5" fill="#10373E">Providers/AhgShareLinkServiceProvider.php</text><text x="67.6" y="758.0" font-size="9.5" fill="#10373E">Services/</text><text x="334.0" y="758.0" font-size="9.5" fill="#10373E">#</text><text x="348.4" y="758.0" font-size="9.5" fill="#10373E">mirror</text><text x="398.8" y="758.0" font-size="9.5" fill="#10373E">of</text><text x="420.4" y="758.0" font-size="9.5" fill="#10373E">AtoM</text></svg></div>

---

© 2026 The Archive and Heritage Group (Pty) Ltd. AGPL-3.0-or-later.
