#!/usr/bin/env python3
"""Master script to generate all review deliverables.
Delegates to build_review_deliverables_part1.py and build_review_deliverables_part2.py.
"""
import subprocess
import sys
import pathlib

root = pathlib.Path(__file__).resolve().parent

def main():
    part1 = root / 'build_review_deliverables_part1.py'
    part2 = root / 'build_review_deliverables_part2.py'
    
    print("Running part 1...")
    res1 = subprocess.run([sys.executable, str(part1)], check=True)
    print("Running part 2...")
    res2 = subprocess.run([sys.executable, str(part2)], check=True)
    print("All review deliverables generated successfully!")

if __name__ == '__main__':
    main()
