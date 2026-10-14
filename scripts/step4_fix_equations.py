import pathlib, re

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

old_eq = r'$$Y_{t, kondratiev_wave} = \mu_{kondratiev_wave} + Y_{t-1, kondratiev_wave} + \epsilon_{t, kondratiev_wave}$$'
new_eq = r'$$Y_{t, \text{kondratiev\_wave}} = \mu_{\text{kondratiev\_wave}} + Y_{t-1, \text{kondratiev\_wave}} + \epsilon_{t, \text{kondratiev\_wave}}$$'

old_subsystem = r'$$Y_{t, \text{analysis_subsystem}} = \mu_{\text{analysis_subsystem}} + Y_{t-1, \text{analysis_subsystem}} + \epsilon_{t, \text{analysis_subsystem}}$$'
new_subsystem = r'$$Y_{t, \text{analysis\_subsystem}} = \mu_{\text{analysis\_subsystem}} + Y_{t-1, \text{analysis\_subsystem}} + \epsilon_{t, \text{analysis\_subsystem}}$$'

old_prove1 = 'This proves macroeconomic shocks exert permanent structural changes rather than temporary deviations around a deterministic 50-year wave.'
new_prove1 = 'This econometric formulation demonstrates that macroeconomic shocks exert persistent structural changes on output levels rather than temporary fluctuations around a deterministic 50-year trend.'

old_prove2 = 'This proves economic shocks exert permanent structural changes rather than temporary deviations around a deterministic 50-year wave.'
new_prove2 = 'This econometric formulation demonstrates that macroeconomic shocks exert persistent structural changes on output levels rather than temporary fluctuations around a deterministic 50-year trend.'

count = 0
for p in root.rglob('*.md'):
    if any(x in p.parts for x in ['.git', 'baseline_snapshot', 'audit']) or p.name.endswith('.bak.md'):
        continue
    txt = p.read_text(encoding='utf-8')
    orig = txt
    
    txt = txt.replace(old_eq, new_eq)
    txt = txt.replace(old_subsystem, new_subsystem)
    txt = txt.replace(old_prove1, new_prove1)
    txt = txt.replace(old_prove2, new_prove2)
    
    if 'Kondratiev Waves' in str(p) and 'This proves' in txt:
        txt = txt.replace('This proves', 'This provides empirical evidence')
        
    if txt != orig:
        p.write_text(txt, encoding='utf-8')
        count += 1
        print(f'Fixed KW equation/assertion in: {p.relative_to(root)}')

print(f'Total files updated: {count}')
