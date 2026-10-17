#!/usr/bin/env python3
"""Step 13: reproduce the birth and fertility tables in
`4th Turning/Demographic Trends/Demographic Trends Deep Dive.md`.

Data: NCHS "Births and General Fertility Rates: United States, 1909-2018"
(data.cdc.gov dataset e6fc-ccez), saved unchanged at
`4th Turning/Demographic Trends/data/nchs_births_gfr_us_1909_2018.csv`.
Births for 1909-1958 are NCHS estimates adjusted for under-registration.
"""
import csv
import pathlib
import statistics as st

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "4th Turning" / "Demographic Trends" / "data" / "nchs_births_gfr_us_1909_2018.csv"

# Generation birth years as given by Strauss and Howe (Howe's current definitions).
GENERATIONS = {
    "G.I. (1901-1924; data from 1909)": (1909, 1924),
    "Silent (1925-1942)": (1925, 1942),
    "Boom (1943-1960)": (1943, 1960),
    "13th / Gen X (1961-1981)": (1961, 1981),
    "Millennial (1982-2005)": (1982, 2005),
    "Homeland (2006-; data to 2018)": (2006, 2018),
}
# Turnings as dated by Strauss and Howe; each window ends the year before the next turning starts.
TURNINGS = {
    "Unraveling 1908-1929": (1909, 1928),
    "Crisis 1929-1946": (1929, 1945),
    "High 1946-1964": (1946, 1963),
    "Awakening 1964-1984": (1964, 1983),
    "Unraveling 1984-2008": (1984, 2007),
    "Crisis 2008- (data to 2018)": (2008, 2018),
}


def load():
    rows = list(csv.DictReader(open(DATA, encoding="utf-8")))
    births = {int(r["Year"]): int(float(r["Birth Number"])) for r in rows}
    gfr = {int(r["Year"]): float(r["General Fertility Rate"]) for r in rows}
    return births, gfr


def main():
    births, gfr = load()
    print("Generation | mean births/yr (M) | mean GFR")
    for name, (a, b) in GENERATIONS.items():
        ys = range(a, b + 1)
        print(f"{name} | {st.mean(births[y] for y in ys)/1e6:.2f} | {st.mean(gfr[y] for y in ys):.1f}")
    print("\nTurning | GFR first year | GFR last year | mean | low (year)")
    for name, (a, b) in TURNINGS.items():
        ys = range(a, b + 1)
        lo = min(ys, key=lambda y: gfr[y])
        print(f"{name} | {gfr[a]:.1f} | {gfr[b]:.1f} | {st.mean(gfr[y] for y in ys):.1f} | {gfr[lo]:.1f} ({lo})")
    changes = sorted(((births[y] - births[y - 1]) / births[y - 1], y) for y in births if y - 1 in births)
    print("\nLargest one-year rises in births:", [(y, f"{p:+.1%}") for p, y in changes[-3:][::-1]])
    print("Largest one-year falls in births:", [(y, f"{p:+.1%}") for p, y in changes[:3]])


if __name__ == "__main__":
    main()
