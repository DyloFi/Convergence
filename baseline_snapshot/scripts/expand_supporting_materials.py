import pathlib

root = pathlib.Path("/Users/dylanboyle/Desktop/Convergence/Changing World Orders")
sm_dir = root / "Supporting_Materials"

# 1. Case Studies Deep Dive.md
# Needs to expand from 111 lines to >165 lines with bespoke historical narratives, unique data tables, and distinct citations.
cs_path = sm_dir / "Case_Studies" / "Case Studies Deep Dive.md"
cs_text = cs_path.read_text()

# Check what citations are currently at the bottom of cs_path
print("Current Case Studies lines:", len(cs_text.splitlines()))

# Let's write comprehensive expansions for all 5 files in Supporting_Materials
