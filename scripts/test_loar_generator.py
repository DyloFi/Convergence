import pathlib
import re

root = pathlib.Path("LoAR")

files = [
    f for f in sorted(root.rglob("*.md"))
    if not f.name.endswith("_Expert_Review.md") and not f.name.endswith(".bak.md")
]

print(f"Total LoAR files: {len(files)}")
for f in files:
    lines = len(f.read_text(encoding="utf-8", errors="ignore").splitlines())
    print(f"  {f.name}: {lines} lines")
