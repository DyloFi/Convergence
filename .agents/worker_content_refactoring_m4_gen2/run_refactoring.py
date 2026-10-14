import os
import pathlib
import sys

# Add current working directory to sys.path to import local modules
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(current_dir))

from renderer import render_report
from data_part1 import REPORTS_PART1
from data_part2 import REPORTS_PART2
from data_part3 import REPORTS_PART3
from data_part4 import REPORTS_PART4

ALL_REPORTS = REPORTS_PART1 + REPORTS_PART2 + REPORTS_PART3 + REPORTS_PART4

def main():
    target_root = pathlib.Path("/Users/dylanboyle/Desktop/Convergence/4th Turning")
    print(f"Total reports to refactor: {len(ALL_REPORTS)}")
    
    count = 0
    for idx, r in enumerate(ALL_REPORTS):
        rel_p = r["rel_path"]
        target_file = target_root / rel_p
        
        # Ensure parent dir exists
        target_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Render markdown content
        md_content = render_report(r, idx)
        
        # Write to file
        target_file.write_text(md_content, encoding="utf-8")
        
        # Verify non-blank lines
        lines = [l for l in md_content.splitlines() if l.strip()]
        line_cnt = len(lines)
        count += 1
        print(f"[{count:02d}/54] Refactored: 4th Turning/{rel_p} ({line_cnt} non-blank lines)")

    print("\nRefactoring complete for all 54 reports!")

if __name__ == "__main__":
    main()
