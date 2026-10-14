import pathlib
import sys
import collections
import re
sys.path.insert(0, ".")

from scripts.audit_verification import ConvergenceAuditor, EXPERT_REVIEW_FILES, BROKEN_TEMPLATE_PATTERNS

root = pathlib.Path("Kondratiev Waves/Data")

# Load existing other files in Kondratiev Waves to build the baseline lines counter
kw_root = pathlib.Path("Kondratiev Waves")
all_kw_files = [f for f in sorted(kw_root.rglob("*.md")) if not f.name.endswith("_Expert_Review.md")]

cases = [
    ("Data Deep Dive.md", "### Empirical Time Series Harmonization Framework"),
    ("Documentation/Documentation Deep Dive.md", "### Data Lineage and Metadata Provenance Architecture"),
    ("Processed/CSV/CSV Deep Dive.md", "### Comma-Separated Values Tabular Data Specification"),
    ("Processed/JSON/JSON Deep Dive.md", "### Hierarchical JSON Data Serialization Architecture"),
    ("Processed/Processed Deep Dive.md", "### Processed Data Transformation Pipeline and Quality Assurance"),
    ("Processed/SQLite/SQLite Deep Dive.md", "### Relational Database Schema and Query Optimization"),
    ("README.md", "### Repository Structural Architecture and Data Inventory"),
    ("Raw/Historical/Historical Deep Dive.md", "### Historical Cliometric Archives and Primary Source Methodology"),
    ("Raw/Raw Deep Dive.md", "### Raw Data Ingestion Protocol and Raw Observation Taxonomy"),
]

target_paths = {root / rel: marker for rel, marker in cases}

bases = {}
for p, marker in target_paths.items():
    text = p.read_text(encoding="utf-8")
    bases[p] = text.split(marker)[0].rstrip()

print("Loaded bases for 9 files.")
