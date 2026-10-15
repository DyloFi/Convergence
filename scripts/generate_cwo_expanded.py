import pathlib
import shutil
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent / "Changing World Orders"

def backup_and_write(rel_path, content):
    target = root / rel_path
    target.parent.mkdir(parents=True, exist_ok=True)
    bak = target.with_name(target.name + '.bak.md')
    if not bak.exists() and target.exists():
        shutil.copy2(target, bak)
    
    # Strip double space words in prose
    lines = []
    for line in content.strip().splitlines():
        if not line.strip().startswith('|') and not line.strip().startswith('```') and not line.strip().startswith('$$'):
            line = re.sub(r'([a-zA-Z0-9_-]+)\s{2,}([a-zA-Z0-9_-]+)', r'\1 \2', line)
        lines.append(line)
    final_text = '\n'.join(lines) + '\n'
    target.write_text(final_text, encoding='utf-8')
    print(f"Updated {rel_path}: {len(lines)} lines")

print("Script framework ready.")
