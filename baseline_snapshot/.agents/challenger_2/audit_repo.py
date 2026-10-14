#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path

ROOT_DIR = Path("/Users/dylanboyle/Desktop/Convergence")
EXCLUDED_DIR = ".agents"

REQUIRED_EXPERT_REVIEWS = [
    "4th_Turning_Expert_Review.md",
    "Changing_World_Orders_Expert_Review.md",
    "Kondratiev_Waves_Expert_Review.md",
    "LoAR_Expert_Review.md",
    "Technological_Singularity_Expert_Review.md"
]

PLACEHOLDER_PATTERNS = ["TODO", "TBD", "FIXME", "[INSERT"]

def run_audit():
    md_files = []
    for root, dirs, files in os.walk(ROOT_DIR):
        # Ignore .agents directory
        if EXCLUDED_DIR in Path(root).parts:
            continue
        for file in files:
            if file.endswith(".md"):
                md_files.append(Path(root) / file)
                
    md_files.sort()
    
    total_files = len(md_files)
    total_lines = 0
    min_lines = float('inf')
    min_lines_file = None
    max_lines = 0
    max_lines_file = None
    
    line_violations = []
    placeholder_violations = []
    
    found_expert_reviews = {name: False for name in REQUIRED_EXPERT_REVIEWS}
    expert_review_paths = {}

    file_details = []

    for file_path in md_files:
        rel_path = file_path.relative_to(ROOT_DIR)
        filename = file_path.name

        # Check if it's one of the required expert review files
        if filename in found_expert_reviews:
            found_expert_reviews[filename] = True
            expert_review_paths[filename] = str(rel_path)

        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
            
        num_lines = len(lines)
        total_lines += num_lines
        
        if num_lines < min_lines:
            min_lines = num_lines
            min_lines_file = str(rel_path)
            
        if num_lines > max_lines:
            max_lines = num_lines
            max_lines_file = str(rel_path)
            
        if num_lines <= 50:
            line_violations.append({
                "file": str(rel_path),
                "line_count": num_lines
            })
            
        # Check placeholders
        file_placeholders = []
        for idx, line in enumerate(lines, 1):
            for pattern in PLACEHOLDER_PATTERNS:
                if pattern in line:
                    file_placeholders.append({
                        "line_number": idx,
                        "pattern": pattern,
                        "snippet": line.strip()
                    })
        
        if file_placeholders:
            placeholder_violations.append({
                "file": str(rel_path),
                "matches": file_placeholders
            })

        file_details.append({
            "file": str(rel_path),
            "line_count": num_lines,
            "placeholders": len(file_placeholders)
        })

    missing_expert_reviews = [name for name, found in found_expert_reviews.items() if not found]

    audit_result = {
        "summary": {
            "total_files": total_files,
            "total_lines": total_lines,
            "min_lines": min_lines if min_lines != float('inf') else 0,
            "min_lines_file": min_lines_file,
            "max_lines": max_lines,
            "max_lines_file": max_lines_file,
            "line_violations_count": len(line_violations),
            "placeholder_violations_count": len(placeholder_violations),
            "missing_expert_reviews_count": len(missing_expert_reviews)
        },
        "expert_reviews_status": {
            "found": expert_review_paths,
            "missing": missing_expert_reviews
        },
        "line_violations": line_violations,
        "placeholder_violations": placeholder_violations,
        "file_details": file_details
    }

    output_json_path = Path("/Users/dylanboyle/Desktop/Convergence/.agents/challenger_2/audit_results.json")
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(audit_result, f, indent=2)

    print("=== AUDIT SUMMARY ===")
    print(f"Total Markdown Files: {total_files}")
    print(f"Total Lines: {total_lines}")
    print(f"Min Lines: {min_lines} ({min_lines_file})")
    print(f"Max Lines: {max_lines} ({max_lines_file})")
    print(f"Line Count Violations (<=50 lines): {len(line_violations)}")
    print(f"Placeholder Violations: {len(placeholder_violations)}")
    print(f"Expert Review Files Found: {len(expert_review_paths)} / {len(REQUIRED_EXPERT_REVIEWS)}")
    if missing_expert_reviews:
        print(f"Missing Expert Reviews: {missing_expert_reviews}")
    else:
        print("All 5 Expert Review Files are PRESENT.")

    return audit_result

if __name__ == "__main__":
    run_audit()
