import pathlib
import re

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

subject_dirs = [
    "Changing World Orders",
    "4th Turning",
    "Kondratiev Waves",
    "LoAR",
    "Technological Singularity"
]

reports = []
for s in subject_dirs:
    sp = root / s
    for f in sp.rglob("*.md"):
        if not f.name.endswith("_Expert_Review.md") and not f.name.endswith(".bak.md"):
            reports.append(f)

no_table = []
for f in reports:
    text = f.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    has_table = any(line.strip().startswith("|") and line.strip().endswith("|") and "---" in line for line in lines)
    if not has_table:
        no_table.append(f)

print(f"Total subject reports lacking tables: {len(no_table)}")
for f in no_table:
    print(f"  {f.relative_to(root)}")

