# User Management

## A Guide for Administrators

---

## What is it?

The User Management module (`ahgUserManagePlugin`) is an administrator-only screen for
browsing and managing the user accounts in your AtoM/Heratio installation. It replaces the
standard user list with a faster, Laravel Query Builder–driven browse, and provides full
create, view, edit, and delete workflows for individual accounts. Every screen in this module
requires the administrator role — non-administrators are redirected to a secure-access page.

## Key features

- **User browse** with paging, listing username, email, active status, group membership, and
  date modified. Group membership is shown for each user (multiple groups joined together).
- **Sorting** by Username, Email, or Date modified.
- **Filtering** by status: all users, only active, or only inactive.
- **Inline search** matching against both username and email.
- **View a user profile**, including REST API key, OAI API key, translate-language
  permissions, and (where the Security Clearance service is installed) the user's clearance.
- **Create and edit users** — username, email, password (with confirmation), active flag,
  group assignment, an authorized form of name, and contact details (telephone, fax, street
  address, city, region, postal code, country code, website, note).
- **API key management** — generate or delete a user's REST API key and OAI API key from the
  edit screen.
- **Translate-language permissions** — grant a user the languages they may translate into.
- **Delete users**, with a built-in guard preventing you from deleting your own account.

## How to use it

All routes live under `/user`:

- **`/user`** or **`/user/list`** — the user browse list. Use the sort links, the status
  filter, and the search box to narrow the list. Add `?subquery=smith` (or arrive via the
  global search `?query=`) to search username/email.
- **`/user/add`** — open the blank form to create a new user. Username, email and a password
  are required for new accounts; the password must be confirmed.
- **`/user/<slug>`** — view a single user's profile, including their API keys and translate
  permissions.
- **`/user/<slug>/edit`** — edit an existing user. Leave the password fields blank to keep the
  current password; fill them in to change it. Use the API-key controls to generate or remove
  keys, and tick the translate languages to grant.
- **`/user/<slug>/delete`** — delete the user after confirmation.

Saving a new or edited user returns you to that user's profile view.

## Administration / settings

This module has no settings of its own. It honours the standard AtoM **hits per page**
setting (`app_hits_per_page`, default 30) for the browse list. Access is fixed to
administrators only.

Standard AtoM authentication routes (login, logout, password edit, password reset, clipboard)
are deliberately preserved and take priority over this module's URLs, so login and account
self-service continue to work as normal.

## Tips & FAQ

- **Why can't a colleague see the user list?** The whole module is administrator-only.
- **Username or email "already in use" error?** The form checks uniqueness across all
  accounts; pick a different value.
- **Editing without changing the password?** Leave both password fields empty.
- **You can't delete yourself** — the module blocks self-deletion to avoid lock-out.
- **Group membership** shown in the list reflects all ACL groups the user belongs to.
