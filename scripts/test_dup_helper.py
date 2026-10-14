import pathlib, collections
import scripts.audit_verification as av

root = pathlib.Path(".")
subj = root / "Changing World Orders"
reports = [
    f for f in sorted(subj.rglob("*.md"))
    if not f.name.endswith("_Expert_Review.md") and not f.name.endswith(".bak.md")
]

file_lines = {r: [l.strip() for l in r.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip()] for r in reports}
all_counter = collections.Counter(l for lines in file_lines.values() for l in lines)

print(f"{'Report':<55} | {'Lines':<6} | {'Dups':<5} | {'Rate':<7} | {'Status'}")
print("-" * 85)
for r in reports:
    lines = file_lines[r]
    dups = sum(1 for l in lines if all_counter[l] > 1)
    rate = (dups / len(lines)) * 100.0 if lines else 0.0
    status = "PASS" if rate <= 15.0 and len(lines) >= 150 else "FAIL"
    rel = str(r.relative_to(subj))
    print(f"{rel:<55} | {len(lines):<6} | {dups:<5} | {rate:6.2f}% | {status}")
