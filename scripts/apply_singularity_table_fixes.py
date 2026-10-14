import pathlib
import shutil
import re
from scripts.fix_singularity_table_rows import clean_table_in_lines

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence/Technological Singularity')

updated = 0
for p in sorted(root.rglob('*.md')):
    if p.name.endswith('_Expert_Review.md') or p.name.endswith('.bak.md'):
        continue
    old_text = p.read_text(encoding='utf-8')
    if re.search(r'\|\s{2,}\|', old_text):
        bak = p.with_suffix('.bak.md')
        if not bak.exists():
            shutil.copy2(p, bak)
        lines = old_text.splitlines()
        new_lines = clean_table_in_lines(lines)
        new_text = '\n'.join(new_lines) + '\n'
        p.write_text(new_text, encoding='utf-8')
        print(f"Updated {p.name}: old lines={len(lines)}, new lines={len(new_lines)}")
        updated += 1

print(f"Total files updated: {updated}")
