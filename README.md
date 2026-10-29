# 13-week cash flow forecast — a Claude Skill

A free [Agent Skill](https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills) that helps Claude build and check a
13-week cash flow forecast from a simple CSV of expected receipts and payments.

- Week-by-week roll-forward: opening cash, receipts, payments, closing cash
- Finds the lowest cash week
- Flags bad rows instead of guessing
- A small Python script does the arithmetic, so the totals are reproducible
- Fictional coffee-shop sample with expected results to check against

## Install

Copy the `13-week-cash-flow-forecast` folder into your skills folder (for Claude Code: `~/.claude/skills/`),
or upload it as a skill in Claude settings. Then ask: "Build a 13-week cash flow forecast from forecast.csv, opening cash 18,000."

## Use it

- **Claude Code:** copy the `13-week-cash-flow-forecast` folder into `~/.claude/skills/` (or `.claude/skills/` in a project), then ask:
  "Build a 13-week cash flow forecast from forecast.csv, opening cash 18,000."
- **Claude apps:** zip the `13-week-cash-flow-forecast` folder and upload it as a skill in Claude settings.
- **Without Claude:** `python3 13-week-cash-flow-forecast/scripts/roll_forward.py forecast.csv --opening 18000`

Your CSV needs four columns: `week_start` (Monday, YYYY-MM-DD), `description`, `category`, `amount`
(positive = expected receipt, negative = payment). The skill asks for the opening balance instead of guessing it.

## Expected result for the sample

Opening 18,000 · receipts 32,000 · payments 32,048 · closing 17,952 · lowest: week 5 at 11,413.

## Tests

`python3 -m unittest discover tests` checks the worked example, the roll-forward links between weeks,
the effect of changing opening cash, and that a bad amount is flagged rather than guessed.

## Prefer a spreadsheet?

The same forecast as an [Excel template with formulas and checks](https://theexpertsai.com/resources/13-week-cash-flow-forecast-template.xlsx),
or try the [free cash flow dashboard from a CSV](https://theexpertsai.com/tools/cash-flow-dashboard-from-csv/?utm_source=github&utm_medium=referral&utm_campaign=13-week-skill) in your browser.

More: [free 13-week cash flow forecast template and guide](https://theexpertsai.com/templates/13-week-cash-flow-forecast-template/?utm_source=github&utm_medium=referral&utm_campaign=13-week-skill)

Educational material, not accounting advice. Sample data is fictional. MIT License.
