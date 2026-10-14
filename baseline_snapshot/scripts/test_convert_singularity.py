import pathlib
import re

p = pathlib.Path('/Users/dylanboyle/Desktop/Convergence/Technological Singularity/Technological Singularity Overview.md')
text = p.read_text(encoding='utf-8')
print("File length before:", len(text.splitlines()))

# Look for unicode box characters
boxes = re.findall(r'^[┌├└│].*$', text, re.MULTILINE)
print("Unicode box lines found:", len(boxes))
if boxes:
    print("Sample box line:", repr(boxes[0]))
