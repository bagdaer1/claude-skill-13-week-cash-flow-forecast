"""Checks the worked example in SKILL.md and the bad-row flag. Run: python3 -m unittest discover tests"""
import pathlib, subprocess, sys, tempfile, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1] / '13-week-cash-flow-forecast'
SCRIPT = ROOT / 'scripts' / 'roll_forward.py'
EXAMPLE = ROOT / 'examples' / 'coffee-shop-13-week.csv'


def run(csv_path, opening):
    return subprocess.run([sys.executable, str(SCRIPT), str(csv_path), '--opening', str(opening)], capture_output=True, text=True, check=True)


class WorkedExample(unittest.TestCase):
    def test_totals_and_lowest_week(self):
        out = run(EXAMPLE, 18000)
        self.assertIn('weeks=13 receipts=32000 payments=32048 closing=17952', out.stdout)
        self.assertIn('lowest closing: week 5 (2026-08-03) = 11413', out.stdout)
        self.assertEqual(out.stderr, '')

    def test_each_closing_is_next_opening(self):
        rows = [l.split(',') for l in run(EXAMPLE, 18000).stdout.splitlines()[1:14]]
        for prev, nxt in zip(rows, rows[1:]):
            self.assertEqual(prev[5], nxt[2])

    def test_opening_cash_shifts_every_week(self):
        a = [l.split(',')[5] for l in run(EXAMPLE, 18000).stdout.splitlines()[1:14]]
        b = [l.split(',')[5] for l in run(EXAMPLE, 20000).stdout.splitlines()[1:14]]
        self.assertTrue(all(int(y) - int(x) == 2000 for x, y in zip(a, b)))

    def test_bad_amount_is_flagged_not_guessed(self):
        with tempfile.NamedTemporaryFile('w', suffix='.csv', delete=False) as f:
            f.write('week_start,description,category,amount\n2026-07-06,Sales,Customer receipts,1000\n2026-07-06,Rent,Rent,abc\n')
        out = run(f.name, 500)
        self.assertIn("FLAG line 3: amount 'abc' is not a number", out.stderr)
        self.assertIn('closing=1500', out.stdout)


if __name__ == '__main__':
    unittest.main()
