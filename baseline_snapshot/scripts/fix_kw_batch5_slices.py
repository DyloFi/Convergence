import pathlib
import re

cases = [
    ('Kondratiev Waves/Kondratiev Waves Overview.md', 110, 126),
    ('Kondratiev Waves/Media_Analysis/Media Analysis Deep Dive.md', 103, 118),
    ('Kondratiev Waves/Policy_Implications/Policy Implications Deep Dive.md', 100, 116),
    ('Kondratiev Waves/Technology/01_The_6th_Kondratiev_Wave_AI_Biotech_Cleantech.md', 106, 128),
    ('Kondratiev Waves/Technology/Technology Deep Dive.md', 118, 133),
]

for rel_path, start_idx, end_idx in cases:
    p = pathlib.Path(rel_path)
    lines = p.read_text(encoding='utf-8').splitlines()
    cleaned = lines[:start_idx] + lines[end_idx:]
    p.write_text('\n'.join(cleaned) + '\n', encoding='utf-8')
    print(f"Cleaned {rel_path}: {len(cleaned)} lines")
