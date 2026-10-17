#!/usr/bin/env python3
"""Step 13: reproduce the US labour-productivity growth table in
`LoAR/Theoretical_Comparisons/Theoretical Comparisons Deep Dive.md`.

Data: FRED series OPHNFB (BLS, Nonfarm Business Sector: Labor Productivity, Output per
Hour of All Persons, index 2017=100, quarterly, seasonally adjusted), downloaded
2026-10-17 from https://fred.stlouisfed.org/graph/fredgraph.csv?id=OPHNFB and saved unchanged
at `LoAR/Theoretical_Comparisons/data/fred_OPHNFB_nonfarm_output_per_hour.csv`.
Growth is the compound annual rate between annual averages of the quarterly index.
"""
import collections
import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "LoAR" / "Theoretical_Comparisons" / "data" / "fred_OPHNFB_nonfarm_output_per_hour.csv"
PERIODS = [(1948, 1973), (1973, 1995), (1995, 2004), (2004, 2019), (2019, 2025)]


def annual_averages():
    quarters = collections.defaultdict(list)
    for row in csv.DictReader(open(DATA, encoding="utf-8")):
        value = row["OPHNFB"].strip()
        if value and value != ".":
            quarters[int(row["observation_date"][:4])].append(float(value))
    return {y: sum(v) / len(v) for y, v in quarters.items() if len(v) == 4}


def main():
    avg = annual_averages()
    print("Period | compound annual growth of output per hour")
    for a, b in PERIODS:
        rate = (avg[b] / avg[a]) ** (1 / (b - a)) - 1
        print(f"{a}-{b} | {rate:.1%}")


if __name__ == "__main__":
    main()
