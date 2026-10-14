import pathlib, re

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

matches = []
for p in root.rglob('*.md'):
    if any(x in p.parts for x in ['.git', 'baseline_snapshot', 'audit']) or p.name.endswith('.bak.md'):
        continue
    txt = p.read_text(encoding='utf-8')
    for i, line in enumerate(txt.splitlines(), 1):
        if re.search(r'\|\s*B\s*\|', line) or re.search(r'\|\s*\.\d+B\s*\|', line) or re.search(r'\|\s*,\d+B\s*\|', line):
            matches.append((str(p.relative_to(root)), i, line))

print(f'Matches for stripped dollar cells in active files: {len(matches)}')
for m in matches:
    print(m)
