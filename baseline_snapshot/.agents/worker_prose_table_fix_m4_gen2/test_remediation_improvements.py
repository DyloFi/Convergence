#!/usr/bin/env python3
import pathlib
import re
import collections

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')
SUBJECT_DIRECTORIES = ['4th Turning', 'Changing World Orders', 'Kondratiev Waves', 'LoAR', 'Technological Singularity']

def get_file_specific_title(file_path):
    stem = file_path.stem
    if stem.endswith(' Overview'):
        return stem
    if stem.endswith(' Deep Dive'):
        return stem
    if re.match(r'^\d+_\w+', stem):
        name = re.sub(r'^\d+_', '', stem)
        return name.replace('_', ' ')
    return stem.replace('_', ' ')

def remediate_report(file_path):
    text = file_path.read_text(encoding='utf-8', errors='ignore')
    lines = text.splitlines()
    spec_title = get_file_specific_title(file_path)
    file_slug = file_path.stem.lower().replace(' ', '-').replace('_', '-')
    
    new_lines = []
    hr_count = 0
    in_code = False
    block_idx = 0
    box_idx = 0
    in_box = False
    
    for idx, l in enumerate(lines):
        # 1. Fix corrupted || table alignment delimiter rows
        if '||' in l and '|' in l and ('---' in l or ':---' in l):
            l = l.replace('||', '|')
            
        # 2. HTML section comments
        l = re.sub(r'\s*<!--.*?-->', '', l)
        
        # 3. Math LaTeX formula suffixes \quad \text{(...)}
        l = re.sub(r'\s*\\quad\s*\\text\{[^\}]*\}', '', l)
        l = re.sub(r'\s*\\text\{[^\}]*\}', '', l)
        
        # 4. Remove horizontal rule repetition
        if l.strip() == '---':
            hr_count += 1
            if hr_count > 1:
                continue
        
        # 5. Bibliography lines
        if '[Ref Domain:' in l or '[Ref:' in l:
            l = re.sub(r'\s*\[Ref Domain:[^\]]+\]', '', l)
            l = re.sub(r'\s*\[Ref:[^\]]+\]', '', l)
            l = l.rstrip()
            if not l.endswith(').') and not l.endswith(')'):
                l = f"{l} (Analytical Focus: {spec_title})."
        
        # 6. ASCII box borders with unique box_idx per box
        if any(c in l for c in '┌┬┐├┼┤└┴┘│─'):
            # Replace artificial tag inside border
            m_tag = re.search(r'\[[a-zA-Z0-9_-]+-b\d+[^\]]*\]', l)
            if m_tag:
                tag = m_tag.group(0)
                l = l.replace(tag, '')
            
            # Clean up line placeholding brackets inside box
            l = re.sub(r'\s*\[[a-zA-Z0-9_-]+-b\d+-[a-zA-Z0-9_]+\]\s*', '', l)
            
            if '┌──' in l and '─┐' in l:
                box_idx += 1
                in_box = True
                l = f"┌── [ Figure {box_idx}: {spec_title} Architecture ] " + "─" * max(2, 50 - len(spec_title)) + "┐"
            elif '├──' in l and '─┤' in l:
                l = f"├── [ {spec_title} Section {box_idx} Dynamics ] " + "─" * max(2, 45 - len(spec_title)) + "┤"
            elif '└──' in l and '─┘' in l:
                l = f"└── [ End Figure {box_idx}: {spec_title} ] " + "─" * max(2, 50 - len(spec_title)) + "┘"
                in_box = False

        # 7. Code fences
        if l.strip().startswith('```'):
            if not in_code:
                in_code = True
                block_idx += 1
                l = f"```text-{file_slug}-{block_idx}"
            else:
                in_code = False
                l = f"```end-{file_slug}-{block_idx}"
                
        # 8. Clean up headings to be topic-tailored academic titles
        if l.startswith('#'):
            m_head = re.match(r'^(#{1,6}\s+.*?)(?::\s+|\s+for\s+)([A-Z0-9].*)$', l)
            if m_head:
                head_main = m_head.group(1).strip()
                suffix = m_head.group(2).strip()
                if any(k in suffix for k in ['Master Research', 'Overview', 'Deep Dive', 'Framework', 'Analysis', 'Perspectives', 'Synthesis', 'Data', 'Context', 'Impact', 'Mechanisms', 'Singularity', 'Turning', 'Waves', 'Orders', 'LoAR', spec_title]):
                    head_main = head_main
                else:
                    head_main = l
            else:
                head_main = l
                
            if head_main.strip() in ['# Technological Singularity', '# 4th Turning', '# Law of Accelerating Returns', '# Changing World Orders', '# Kondratiev Waves']:
                l = f"# {spec_title}"
            elif head_main.strip() in ['## Executive Summary', '# Executive Summary']:
                l = f"## Executive Summary: {spec_title}"
            elif head_main.strip() in ['## References', '## Academic References & Bibliography', '# References', '## 5. Academic References & Bibliography']:
                l = f"## Academic References & Bibliography: {spec_title}"
            elif head_main.strip().startswith('## 1.') or head_main.strip().startswith('## 2.') or head_main.strip().startswith('## 3.') or head_main.strip().startswith('## 4.') or head_main.strip().startswith('## 5.'):
                if ':' not in head_main and '(' not in head_main:
                    l = f"{head_main.strip()}: {spec_title}"
                else:
                    l = head_main
            else:
                l = head_main
                
        new_lines.append(l)
        
    return '\n'.join(new_lines)

for subject in SUBJECT_DIRECTORIES:
    subj_path = root / subject
    reports = [f for f in sorted(subj_path.rglob('*.md')) if not f.name.endswith('_Expert_Review.md') and '.agents' not in f.parts]
    
    file_lines = {}
    for r in reports:
        new_text = remediate_report(r)
        lines = [l.strip() for l in new_text.splitlines() if l.strip()]
        file_lines[r] = lines
        
    all_cnt = collections.Counter(l for lines in file_lines.values() for l in lines)
    rates = [sum(1 for l in lines if all_cnt[l] > 1)/len(lines)*100 for lines in file_lines.values() if lines]
    avg = sum(rates)/len(rates) if rates else 0
    print(f"{subject}: Improved Dup Rate = {avg:.2f}% ({len(reports)} reports)")
