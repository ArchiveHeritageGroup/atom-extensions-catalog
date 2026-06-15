# Menu Configuration Management User Guide

## A Guide for Administrators

---

## What is it?

The AHG Menu Configuration Manage plugin (`ahgMenuManagePlugin`) lets administrators **list, create, edit, reorder and delete the navigation menus** of AtoM/Heratio. It manages the site's menu hierarchy directly through the Laravel Query Builder, maintaining the underlying nested-set (lft/rgt) tree so menu items stay correctly ordered and nested.

It is an **administrator-only** tool: every screen requires the administrator role.

## Key features

- **Tree view** of all menu items, indented by depth, sorted in display order.
- **Create** new menu items under any parent (or at the top level).
- **Edit** an item's label, path, description and parent menu.
- **Reorder** items inline using move-up / move-down (before/after a sibling).
- **Re-parent** items by changing the parent in the edit form.
- **Delete** items (and their sub-items), with confirmation.
- **Protected core menus** are safeguarded — they cannot be renamed or deleted.

## How to use it

**List menus** — go to `/menu/list`. This shows the full menu tree. Each item displays its label and offers edit, delete and reorder controls. Items with children are marked accordingly.

**Add a menu item** — go to `/menu/add`. Fill in:
- **Label** (required) — the text shown to users.
- **Name** (required, must be unique) — the internal identifier.
- **Path** — the URL or route the menu points to.
- **Parent** — choose "(Top level)" or another menu to nest under.
- **Description** — optional notes.

**Edit a menu item** — go to `/menu/<id>/edit` (or click Edit in the list). You can change the label, path, description and parent. Changing the parent moves the item (and its sub-items) to the new location in the tree.

**Reorder items** — from the list, the move-up / move-down controls call `/menu/list?move=<id>&before=<id>` or `...&after=<id>` to swap an item with its sibling. Reordering only works between items that share the same parent.

**Delete a menu item** — go to `/menu/<id>/delete` (or click Delete in the list) and confirm. Deleting a menu also removes any items nested beneath it.

## Administration / settings

- **Access:** All actions require the **administrator** role; non-administrators are redirected to the secure/login screen.
- **Protected menus:** The following core AtoM menus cannot be deleted, and their internal *name* cannot be changed: `mainMenu`, `browse`, `add`, `manage`, `import`, `admin`, `browseInstitution`, `staticPagesMenu`, `clipboard`. You can still edit their label, path and description.
- **Tree integrity:** The plugin maintains the nested-set structure automatically, so adds, moves and deletes keep the menu order consistent.

## Tips & FAQ

- **Why is the Name field locked on some items?** That menu is protected — its name is fixed, but you can still change its label and path.
- **Why won't my reorder work?** You can only reorder an item relative to a sibling under the same parent. To move it elsewhere, edit it and change the parent.
- **"A menu with this name already exists."** Menu names must be unique; pick a different internal name.
- **Deleting a parent** also deletes everything nested under it — move children out first if you want to keep them.
- **Label vs. Name:** the *label* is what visitors see; the *name* is the internal key the system uses.
