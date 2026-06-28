# ahgUserManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). User browse and management using Laravel Query Builder

## Overview

- **Name:** AHG User Manage
- **Machine name:** `ahgUserManagePlugin`
- **Version:** 1.0.0
- **Category:** browse
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

### Features

- User browse via Laravel Query Builder
- Sort by username, email, date modified
- Filter by active/inactive status
- Inline search by username and email
- Group membership display via GROUP_CONCAT
- Theme-compatible templates (SimplePager)

## Routes

| Route name | URL | Action |
|---|---|---|
| `user_view_override` | `/user/:slug` | view |
| `user_delete_override` | `/user/:slug/delete` | delete |
| `user_edit_override` | `/user/:slug/edit` | edit |
| `user_add_override` | `/user/add` | edit |
| `user_list_override` | `/user/list` | browse |
| `user_index_override` | `/user` | browse |
| `user_login_passthrough` | `/user/login` | login |
| `user_logout_passthrough` | `/user/logout` | logout |
| `user_password_edit_passthrough` | `/user/passwordEdit` | passwordEdit |
| `user_clipboard_passthrough` | `/user/clipboard` | clipboard |
| `user_password_reset_passthrough` | `/user/passwordReset` | passwordReset |

## Module actions

**`userManage`** — `browse`, `view`, `edit`, `delete`

## Service layer

### `UserCrudService`  
`lib/Services/UserCrudService.php`

Public methods: `getById()`, `getBySlug()`, `getUserGroups()`, `getAssignableGroups()`, `getEntityTypes()`, `create()`, `update()`, `delete()`, `getApiKey()`, `generateApiKey()`, `deleteApiKey()`, `verifyPassword()`, `getTranslateLanguages()`, `saveTranslateLanguages()`, `getAvailableLanguages()`, `usernameExists()`, `emailExists()`

### `UserBrowseService`  
`lib/Services/UserBrowseService.php`

Public methods: `browse()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
