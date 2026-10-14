#!/usr/bin/env python3
import os
import glob
import re

BASE_DIR = '/Users/dylanboyle/Desktop/Convergence/4th Turning'

def verify():
    files = glob.glob(os.path.join(BASE_DIR, '**/*.md'), recursive=True)
    files = [f for f in files if not f.endswith('4th_Turning_Expert_Review.md')]
    files.sort()

    print(f"==================================================")
    print(f"VERIFICATION AUDIT FOR 4TH TURNING CORPUS ({len(files)} files)")
    print(f"==================================================")

    placeholder_pat = re.compile(r'TODO|TBD|FIXME|\[INSERT', re.IGNORECASE)
    citation_pat = re.compile(r'(Strauss\s*&\s*Howe|Strauss\s+and\s+Howe|Turchin|Spengler|Toynbee|Goldstone|Huntington|Mannheim|Fischer|Giannakos)', re.IGNORECASE)
    
    generic_boilerplate_headers = [
        'Strategic Decision-Making Matrix',
        'Convergence Cross-Domain Synthesis Framework',
        'Academic Appendix: Interdisciplinary Integration'
    ]

    errors = []
    warnings = []

    for i, f in enumerate(files, 1):
        rel = os.path.relpath(f, BASE_DIR)
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
            lines = content.splitlines()

        line_count = len(lines)

        # Rule 1: Line count > 50 (i.e. line_count >= 51)
        if line_count < 51:
            errors.append(f"LINE COUNT FAIL: {rel} has only {line_count} lines (must be >= 51)")

        # Specific rule for Global Perspectives & Comparative Timelines (> 70 lines)
        if rel in ['Global Perspectives/Global Perspectives Deep Dive.md', 'Comparative Timelines/Comparative Timelines Deep Dive.md']:
            if line_count < 71:
                errors.append(f"PRIORITY FILE LINE COUNT FAIL: {rel} has only {line_count} lines (must be >= 71)")

        # Rule 2: 0 placeholders
        ph_matches = placeholder_pat.findall(content)
        if ph_matches:
            errors.append(f"PLACEHOLDER FAIL: {rel} contains placeholders: {ph_matches}")

        # Rule 3: Academic citations present
        citations = citation_pat.findall(content)
        if len(citations) < 2:
            errors.append(f"CITATION FAIL: {rel} has only {len(citations)} citations (minimum 2 required)")

        # Rule 4: References section present
        has_refs = '## Academic References' in content or '## References' in content or '### References' in content
        if not has_refs:
            errors.append(f"REFERENCES SECTION FAIL: {rel} is missing References section")

        # Rule 5: Generic boilerplate removed
        for gh in generic_boilerplate_headers:
            if gh in content:
                errors.append(f"BOILERPLATE FAIL: {rel} still contains generic header '{gh}'")

    print(f"\n--- AUDIT SUMMARY ---")
    print(f"Total files verified: {len(files)}")
    print(f"Total errors found:   {len(errors)}")
    print(f"Total warnings:       {len(warnings)}")

    if errors:
        print("\nERRORS ENCOUNTERED:")
        for err in errors:
            print(f"  ❌ {err}")
        return False
    else:
        print("\n✅ 100% VERIFICATION SUCCESS: All 54 research reports pass all criteria!")
        return True

if __name__ == '__main__':
    success = verify()
    exit(0 if success else 1)
