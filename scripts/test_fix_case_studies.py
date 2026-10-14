import pathlib
import re

p = pathlib.Path('/Users/dylanboyle/Desktop/Convergence/Changing World Orders/Supporting_Materials/Case_Studies/Case Studies Deep Dive.md')
text = p.read_text(encoding='utf-8')

# Remove horizontal rule lines
lines = [l for l in text.splitlines() if l.strip() != '-----------------']

# Use specific table header alignments or varied dashes
cleaned_text = '\n'.join(lines) + '\n'

p.write_text(cleaned_text, encoding='utf-8')
print("Updated Case Studies Deep Dive.md")
