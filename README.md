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

## Expected result for the sample

Opening 18,000 · receipts 32,000 · payments 32,048 · closing 17,952 · lowest: week 5 at 11,413.

More: [free 13-week cash flow forecast template and guide](https://theexpertsai.com/templates/13-week-cash-flow-forecast-template/?utm_source=github&utm_medium=referral&utm_campaign=13-week-skill)

Educational material, not accounting advice. Sample data is fictional. MIT License.
