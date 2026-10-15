import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent

modified = []
frac_fixes = 0
times_fixes = 0

for p in root.rglob('*.md'):
    if any(x in p.parts for x in ['.git', 'baseline_snapshot', 'audit']) or p.name.endswith('.bak.md'):
        continue
    txt = p.read_text(encoding='utf-8')
    orig = txt
    
    # 1. Fix stripped / form-feed rac{ -> \frac{
    if 'rac{' in txt:
        # replace \x0crac{
        txt = txt.replace('\x0crac{', r'\frac{')
        # replace (not preceded by \) rac{
        txt = re.sub(r'(?<!\\)rac\{', r'\\frac{', txt)
        frac_fixes += 1
        
    # 2. Fix tab-corrupted times: ' imes ' -> r' \times '
    if ' imes ' in txt:
        txt = txt.replace(' imes ', r' \times ')
        times_fixes += 1
        
    # 3. Fix \frac next to bare numbers if any (e.g. \frac 1 2 -> \frac{1}{2})
    # Also check broken sub/superscripts like _{... without closing or naked subscripts
    
    if txt != orig:
        p.write_text(txt, encoding='utf-8')
        modified.append(str(p.relative_to(root)))

print(f'Frac fixes: {frac_fixes}, Times fixes: {times_fixes}, Total modified: {len(modified)}')
for m in modified:
    print(f'  {m}')
