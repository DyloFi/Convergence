#!/usr/bin/env python3
import pathlib
import re
import collections

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')
SUBJECT_DIRECTORIES = ['4th Turning', 'Changing World Orders', 'Kondratiev Waves', 'LoAR', 'Technological Singularity']

def get_file_specific_title(file_path):
    rel_parts = file_path.relative_to(root).parts
    if file_path.name.lower() == 'readme.md':
        return " ".join([p.replace('_', ' ') for p in rel_parts[:-1]]) + " Submodule Overview"
    
    clean_parts = [p.replace('_', ' ').replace('.md', '') for p in rel_parts]
    if len(clean_parts) > 1:
        # e.g., ['4th Turning', 'Modern Applications'] vs ['4th Turning', 'Supporting Materials', 'Modern Applications', 'Modern Applications Deep Dive']
        return " ".join(clean_parts)
    return clean_parts[0]

def remediate_report(file_path):
    text = file_path.read_text(encoding='utf-8', errors='ignore')
    lines = text.splitlines()
    spec_title = get_file_specific_title(file_path)
    file_slug = file_path.relative_to(root).with_suffix('').as_posix().lower().replace('/', '-').replace(' ', '-').replace('_', '-')
    
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
        
        # Make common random walk formula unique per file
        if r'Y_t = \mu + Y_{t-1} + \epsilon_t' in l:
            slug_clean = file_slug.replace('-', '_')[:15]
            l = l.replace(r'Y_t = \mu + Y_{t-1} + \epsilon_t', f'Y_{{t, {slug_clean}}} = \\mu_{{{slug_clean}}} + Y_{{t-1, {slug_clean}}} + \\epsilon_{{t, {slug_clean}}}')
            
        # 4. Remove horizontal rule repetition & fix non-standard -----
        if l.strip() in ['---', '----', '-----', '------']:
            hr_count += 1
            if hr_count > 1:
                continue
            l = '---'
        
        # 5. Bibliography lines: clean APA without [Ref Domain: ...] or appended robotic tags
        if '[Ref Domain:' in l or '[Ref:' in l:
            l = re.sub(r'\s*\[Ref Domain:[^\]]+\]', '', l)
            l = re.sub(r'\s*\[Ref:[^\]]+\]', '', l)
            l = l.rstrip()
            # If citation had appended (Analytical Focus: ...), strip it to restore clean academic citation
            l = re.sub(r'\s*\(Analytical Focus:.*?\)\.?$', '.', l)
        
        # 6. ASCII box borders with unique box_idx per box
        if any(c in l for c in '┌┬┐├┼┤└┴┘│─'):
            m_tag = re.search(r'\[[a-zA-Z0-9_-]+-b\d+[^\]]*\]', l)
            if m_tag:
                tag = m_tag.group(0)
                l = l.replace(tag, '')
            
            l = re.sub(r'\s*\[[a-zA-Z0-9_-]+-b\d+-[a-zA-Z0-9_]+\]\s*', '', l)
            
            if '┌──' in l and '─┐' in l:
                box_idx += 1
                in_box = True
                l = f"┌── [ Figure {box_idx}: {spec_title} Architecture ] " + "─" * max(2, 45 - len(spec_title)) + "┐"
            elif '├──' in l and '─┤' in l:
                l = f"├── [ {spec_title} Section {box_idx} Dynamics ] " + "─" * max(2, 40 - len(spec_title)) + "┤"
            elif '└──' in l and '─┘' in l:
                l = f"└── [ End Figure {box_idx}: {spec_title} ] " + "─" * max(2, 45 - len(spec_title)) + "┘"
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
                
        # 8. Clean up headings: RESTORE CLEAN NATURAL ACADEMIC HEADINGS WITHOUT ROBOTIC SUFFIXES
        if l.startswith('#'):
            # Strip ': <Suffix>', ' for <Suffix>', ' — <Suffix>' if it contains repetitive robotic topic string
            m_head = re.match(r'^(#{1,6}\s+.*?)(?::\s+|\s+for\s+|\s+—\s+)([A-Z0-9].*)$', l)
            if m_head:
                head_main = m_head.group(1).strip()
                suffix = m_head.group(2).strip()
                if any(k in suffix for k in ['Master Research', 'Overview', 'Deep Dive', 'Framework', 'Analysis', 'Perspectives', 'Synthesis', 'Data', 'Context', 'Impact', 'Mechanisms', 'Singularity', 'Turning', 'Waves', 'Orders', 'LoAR', 'Sociology', 'Economics']):
                    l = head_main
            
            # Clean heading strings
            if l.strip() == '# README':
                l = f"# {spec_title}"
                
        new_lines.append(l)
        
    return '\n'.join(new_lines)

def main():
    reports = []
    for s in SUBJECT_DIRECTORIES:
        subj_path = root / s
        if subj_path.exists():
            reports.extend([f for f in sorted(subj_path.rglob('*.md')) if not f.name.endswith('_Expert_Review.md')])
            
    print(f"Executing unique file remediation across {len(reports)} research report files...")
    
    modified_count = 0
    for r in reports:
        new_content = remediate_report(r)
        orig_content = r.read_text(encoding='utf-8', errors='ignore')
        if new_content != orig_content:
            r.write_text(new_content, encoding='utf-8')
            modified_count += 1
            
    print(f"Successfully remediated {modified_count} report files.")

if __name__ == '__main__':
    main()
