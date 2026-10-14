#!/usr/bin/env python3
import pathlib
import collections
import re

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')
SUBJECT_DIRECTORIES = ['4th Turning', 'Changing World Orders', 'Kondratiev Waves', 'LoAR', 'Technological Singularity']

def clean_file_content(text):
    lines = text.splitlines()
    new_lines = []
    for l in lines:
        # 1. Ref Domain
        l = re.sub(r'\s*\[Ref Domain:[^\]]+\]', '', l)
        l = re.sub(r'\s*\[Ref:[^\]]+\]', '', l)
        
        # 2. HTML comments
        l = re.sub(r'\s*<!--.*?-->', '', l)
        
        # 3. Math formula text tags
        l = re.sub(r'\s*\\quad\s*\\text\{[^\}]*\}', '', l)
        l = re.sub(r'\s*\\text\{[^\}]*\}', '', l)
        
        # 4. ASCII box comment tags inside brackets [slug-b1-l1] or border tags
        l = re.sub(r'\[[a-zA-Z0-9_-]+-b\d+[^\]]*\]', '', l)
        
        # 5. Heading suffixes
        if l.startswith('#'):
            m = re.match(r'^(#{1,6}\s+.*?)(?::\s+|\s+for\s+)([A-Z0-9].*)$', l)
            if m:
                head_start = m.group(1).strip()
                suffix = m.group(2).strip()
                if any(k in suffix for k in ['Master Research', 'Overview', 'Deep Dive', 'Framework', 'Analysis', 'Perspectives', 'Synthesis', 'Data', 'Context', 'Impact', 'Mechanisms', 'Singularity', 'Turning', 'Waves', 'Orders', 'LoAR']):
                    l = head_start
        
        new_lines.append(l)
    return '\n'.join(new_lines)

for subject in SUBJECT_DIRECTORIES:
    subj_path = root / subject
    reports = [f for f in sorted(subj_path.rglob('*.md')) if not f.name.endswith('_Expert_Review.md')]
    
    file_lines_clean = {}
    for r in reports:
        text = r.read_text(encoding='utf-8', errors='ignore')
        cleaned_text = clean_file_content(text)
        lines = [l.strip() for l in cleaned_text.splitlines() if l.strip()]
        file_lines_clean[r] = lines

    all_cnt = collections.Counter(l for lines in file_lines_clean.values() for l in lines)
    rates = [sum(1 for l in lines if all_cnt[l] > 1)/len(lines)*100 for lines in file_lines_clean.values() if lines]
    avg = sum(rates)/len(rates) if rates else 0
    
    dups = [(count, line) for line, count in all_cnt.items() if count > 1]
    dups.sort(key=lambda x: x[0], reverse=True)
    
    print(f'=== {subject}: Clean Dup Rate = {avg:.2f}% ({len(reports)} reports, {len(dups)} duplicate lines) ===')
    for count, line in dups[:10]:
        print(f'  [{count}x] {line[:90]}')
    print()
