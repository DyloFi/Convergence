import pathlib
import shutil
import re

root = pathlib.Path(__file__).resolve().parent.parent / "Changing World Orders"

def write_monograph(rel_path, content):
    target = root / rel_path
    target.parent.mkdir(parents=True, exist_ok=True)
    bak = target.with_name(target.name + '.bak.md')
    if not bak.exists() and target.exists():
        shutil.copy2(target, bak)
    
    # Clean double spaces outside code/tables
    cleaned = []
    for line in content.strip().splitlines():
        if not line.strip().startswith('|') and not line.strip().startswith('```') and not line.strip().startswith('$$'):
            line = re.sub(r'([a-zA-Z0-9_-]+)\s{2,}([a-zA-Z0-9_-]+)', r'\1 \2', line)
        cleaned.append(line)
    final_text = '\n'.join(cleaned) + '\n'
    target.write_text(final_text, encoding='utf-8')
    lines_count = len(final_text.splitlines())
    print(f"Upgraded {rel_path}: {lines_count} lines")

