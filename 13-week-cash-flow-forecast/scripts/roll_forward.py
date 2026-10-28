#!/usr/bin/env python3
"""13-week cash roll-forward from a CSV of week_start, description, category, amount. Standard library only."""
import argparse, csv, sys
from collections import OrderedDict
from decimal import Decimal, InvalidOperation

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('csv'); ap.add_argument('--opening', required=True, type=Decimal)
    a = ap.parse_args()
    weeks, problems = OrderedDict(), []
    with open(a.csv, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        need = {'week_start', 'description', 'category', 'amount'}
        if not need <= set(reader.fieldnames or []):
            sys.exit(f'missing columns: {sorted(need - set(reader.fieldnames or []))}')
        for n, row in enumerate(reader, start=2):
            try:
                amt = Decimal(row['amount'].replace(',', '').replace('$', '').strip())
            except (InvalidOperation, AttributeError):
                problems.append(f'line {n}: amount {row.get("amount")!r} is not a number'); continue
            w = weeks.setdefault(row['week_start'].strip(), [Decimal(0), Decimal(0)])
            if amt >= 0: w[0] += amt
            else: w[1] += -amt
    cash, low = a.opening, None
    print('week,week_start,opening,receipts,payments,closing')
    tr = tp = Decimal(0)
    for i, (wk, (r, p)) in enumerate(sorted(weeks.items()), start=1):
        close = cash + r - p
        print(f'{i},{wk},{cash},{r},{p},{close}')
        if low is None or close < low[2]: low = (i, wk, close)
        tr += r; tp += p; cash = close
    print(f'\nweeks={len(weeks)} receipts={tr} payments={tp} closing={cash}')
    if low: print(f'lowest closing: week {low[0]} ({low[1]}) = {low[2]}')
    for p in problems: print('FLAG', p, file=sys.stderr)
    if len(weeks) != 13: print(f'FLAG expected 13 weeks, found {len(weeks)}', file=sys.stderr)

if __name__ == '__main__':
    main()
