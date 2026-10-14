#!/usr/bin/env python3
import pathlib
import re
import shutil

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence/Changing World Orders')

def backup_and_write(rel_path, content):
    target = root / rel_path
    bak = target.with_name(target.name + '.bak.md')
    if not bak.exists() and target.exists():
        shutil.copy2(target, bak)
    # clean double spaces in body
    cleaned_lines = []
    for line in content.strip().splitlines():
        if not line.strip().startswith('|') and not line.strip().startswith('```'):
            line = re.sub(r'([a-zA-Z0-9_-]+)\s{2,}([a-zA-Z0-9_-]+)', r'\1 \2', line)
        cleaned_lines.append(line)
    final_content = '\n'.join(cleaned_lines) + '\n'
    target.write_text(final_content, encoding='utf-8')
    print(f"Upgraded {rel_path}: {len(final_content.splitlines())} lines")

