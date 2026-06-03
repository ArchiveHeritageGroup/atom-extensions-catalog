# Circulation & Interlibrary Loan

## A Guide for Circulation Desk and ILL Staff

---

## Circulation

- **Patrons** — register patrons with categories (public, staff, student, researcher), borrowing limits and expiry.
- **Checkout / return / renew** — at the desk or by barcode; loan period and renewal limits come from the loan rules for the item + patron type.
- **Holds** — place holds, managed as a queue; the next hold is promoted automatically on return.
- **Overdue** — overdue items are detected and fines calculated per the loan rule.

## Interlibrary Loan (ISO 10160/10161)

ILL requests follow the **ISO 10160/10161** state machine, so a request only moves through legal transitions:

`submitted → pending → shipped → received → returned → checked_in → completed`

with branches for `conditional`, `renew_requested → renewed`, `overdue`, `recalled`, `unfilled`, `lost` and `cancelled`. Illegal jumps are rejected, and every transition is recorded in the request's **status history**.

### Borrowing / lending

1. Create an ILL request (borrow or lend), optionally citing an EDI **trading partner**.
2. Advance the request through the workflow; on **shipped**, if a trading partner is configured an **EDI message** (EANCOM / X12) is dispatched automatically.
3. Receive, renew, recall, return and check in as the loan progresses.

---

## For Administrators

- Tables: `library_patron`, `library_checkout`, `library_hold`, `library_fine`, `library_loan_rule`, `library_ill_request`, `library_ill_status_history`, `library_trading_partner`.
- The ILL state set + allowed transitions are defined in `ILLService::ILL_TRANSITIONS`.
- EDI trading partners (endpoints + message profiles) are managed under **Trading Partners**.
