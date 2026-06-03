# Library Acquisitions

## A Guide for Acquisitions and Collection-Development Staff

---

## What the Acquisitions module does

The Acquisitions module manages the purchase of library materials from order to receipt, with GRAP-aligned budget control:

- **Vendors** — order from local and international suppliers (shared with the Vendor register).
- **Orders & order lines** — place, track and receive orders line by line.
- **Budgets** — allocate funds, track commitments (encumbrance) and expenditure.
- **Fund codes & splits** — charge an order line to a single fund or split it across several.

---

## Placing an order

1. Go to **Acquisitions → New Order**.
2. Choose a **vendor** (from the vendor register) and a **budget code**.
3. Add **order lines** — title, ISBN, quantity, unit price. The line total and order total are calculated automatically.
4. For a split charge, add **fund allocations** to the line (each a fund code + amount).
5. **Send** the order — this marks it *sent* and **encumbers** its total against the budget (committed funds).

## Receiving

On **Receive**, enter the quantity received per line. Lines become *partial* or *received*, and the order rolls up to *received* when all lines arrive.

## Budgets

Each budget tracks **allocated**, **committed** (encumbered) and **spent** amounts; *available* = allocated − spent − committed. Sending an order encumbers; receiving/invoicing converts commitment to expenditure.

---

## For Administrators

- Vendors are managed in the **Vendor** register (`ahgVendorPlugin`) and surfaced in the order form's vendor picker — no separate acquisitions vendor list to maintain.
- REST API: orders, order lines and budgets are exposed under `/api/library/*` (X-API-Key).
- Tables: `library_order`, `library_order_line`, `library_order_line_fund`, `library_budget`.
