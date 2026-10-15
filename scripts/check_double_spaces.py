import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent

files_to_fix = [
    'Changing World Orders/Current_Geopolitical/01_US_China_Competition_and_Multipolarity.md',
    'Changing World Orders/Foundations/Foundations Deep Dive.md',
    'Kondratiev Waves/Analysis/Analysis Deep Dive.md',
    'Kondratiev Waves/Concept/01_Structural_Mechanisms_of_Long_Waves.md'
]

for rel in files_to_fix:
    p = root / rel
    lines = p.read_text(encoding='utf-8').splitlines()
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith('```') or line.strip().startswith('|') or line.strip().startswith('┌'):
            continue
        m = re.findall(r'\b[a-zA-Z0-9_-]+\s{2,}[a-zA-Z0-9_-]+\b', line)
        if m:
            print(f'{rel}:{idx} -> {m} -> {repr(line)}')
