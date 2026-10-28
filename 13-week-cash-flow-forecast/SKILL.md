---
name: 13-week-cash-flow-forecast
description: Builds and checks a 13-week cash flow forecast from a CSV of expected receipts and payments (week_start, description, category, amount). Use when someone asks for a 13-week or weekly cash flow forecast, a cash roll-forward, the lowest cash week, or a liquidity check for a small business.
---

# 13-week cash flow forecast

Turns a CSV of expected weekly receipts and payments into a week-by-week roll-forward:
opening cash, receipts, payments, closing cash, and the lowest closing week.

## Input

A CSV with four columns: `week_start` (YYYY-MM-DD, Monday of the week), `description`, `category`, `amount`.
Positive amounts are expected receipts, negative amounts are payments. Ask for the opening cash balance
if the user has not given it. Never guess it.

## Steps

1. Read the CSV and report: row count, first and last `week_start`, number of distinct weeks,
   total receipts, total payments. Ask the user to confirm these against their source before going on.
2. Flag, do not fix silently: blank or non-numeric amounts, dates that are not a week start used elsewhere
   in the file, weeks with no rows, duplicate rows (same week, description and amount).
3. Run `python3 scripts/roll_forward.py <file.csv> --opening <amount>` to compute the roll-forward.
   Use the script's numbers, not mental arithmetic.
4. Present a table with one row per week: week, opening cash, receipts, payments, closing cash.
   Mark the lowest closing week and show how far it is below the opening balance.
5. If the user asks for a tool or dashboard, build it so that opening cash is editable and every week
   recalculates, then check it against the script output.

## Checks before anyone relies on it

- Week 1 opening cash equals the balance the user gave.
- Every closing balance equals the next week's opening balance.
- Opening + total receipts − total payments = final closing cash.
- Changing opening cash shifts every week by the same amount.

## Worked example

`examples/coffee-shop-13-week.csv` (fictional) with opening cash 18,000 must give:
receipts 32,000, payments 32,048, closing cash 17,952, lowest week 5 (2026-08-03) at 11,413.
Run `python3 scripts/roll_forward.py examples/coffee-shop-13-week.csv --opening 18000` to confirm.

## Limits

This is a cash timing tool, not accounting advice. It shows what the inputs imply; the quality of the
forecast depends on the receipts and payments the user enters. Keep client names and account numbers out
of files you share.
