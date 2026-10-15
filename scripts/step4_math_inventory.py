import pathlib, re, json

root = pathlib.Path(__file__).resolve().parent.parent

# Fix double $ in line 114 of Convergence_Master_Synthesis.md
synth = root / 'Convergence_Master_Synthesis.md'
txt = synth.read_text(encoding='utf-8')
txt = txt.replace(r'\alpha(\gamma - 1)}$$,', r'\alpha(\gamma - 1)}$,')
synth.write_text(txt, encoding='utf-8')

# Inventory all math expressions in active markdown files
math_expressions = []
issues = []

for p in root.rglob('*.md'):
    if any(x in p.parts for x in ['.git', 'baseline_snapshot', 'audit']) or p.name.endswith('.bak.md'):
        continue
    txt = p.read_text(encoding='utf-8')
    lines = txt.splitlines()
    
    # Check block math $$...$$
    blocks = re.findall(r'\$\$(.*?)\$\$', txt, flags=re.DOTALL)
    for b in blocks:
        math_expressions.append({'file': str(p.relative_to(root)), 'type': 'block', 'expr': b.strip()})
        
    # Check inline math $...$
    txt_no_blocks = re.sub(r'\$\$.*?\$\$', '', txt, flags=re.DOTALL)
    inlines = re.findall(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', txt_no_blocks)
    for inl in inlines:
        math_expressions.append({'file': str(p.relative_to(root)), 'type': 'inline', 'expr': inl.strip()})
        
    # Check lines for remaining anomalies
    for i, line in enumerate(lines, 1):
        if '36646' in line or '36689' in line or '41166' in line:
            issues.append({'file': str(p.relative_to(root)), 'line': i, 'type': 'pid_leak', 'text': line})
        # Look for literal rac{ not preceded by f
        if re.search(r'(?<!f)rac\{', line):
            issues.append({'file': str(p.relative_to(root)), 'line': i, 'type': 'corrupted_frac', 'text': line})
        if 'kondratiev_wave' in line and not r'\text{kondratiev\_wave}' in line:
            issues.append({'file': str(p.relative_to(root)), 'line': i, 'type': 'unformatted_kw_subscript', 'text': line})
        if ' imes ' in line:
            issues.append({'file': str(p.relative_to(root)), 'line': i, 'type': 'corrupted_times', 'text': line})

print(f'Total math expressions inventoried: {len(math_expressions)}')
print(f'Real issues found: {len(issues)}')
for iss in issues:
    print(f'  {iss}')

with open(root / 'audit/math_inventory.json', 'w', encoding='utf-8') as f:
    json.dump({
        'total_math_expressions': len(math_expressions),
        'issues_found': len(issues),
        'issues': issues,
        'math_expressions': math_expressions
    }, f, indent=2)

print('Wrote audit/math_inventory.json')
