import pathlib
import collections

filepath = pathlib.Path("Kondratiev Waves/Analysis/Notebooks/Notebooks Deep Dive.md")
text = filepath.read_text(encoding='utf-8')

# Remove flowchart box pipes and down arrows
lines = text.splitlines()
new_lines = []
for l in lines:
    s = l.strip()
    if s == '│' or s == '▼':
        continue
    if s == '----------------':
        continue
    if s == '| :--- | :--- | :--- | :--- |':
        new_lines.append('| :-------------------------------- | :----------------- | :----------------------------- | :---------------------------------- |')
        continue
    if 'Y_{t, kondratiev_wave}' in l:
        new_lines.append(r'$$Y_{t, \text{nb\_pipeline}} = \mu_{\text{nb\_pipeline}} + Y_{t-1, \text{nb\_pipeline}} + \epsilon_{t, \text{nb\_pipeline}}$$')
        continue
    new_lines.append(l)

text = '\n'.join(new_lines) + '\n'
filepath.write_text(text, encoding='utf-8')
print("Successfully normalized Notebooks Deep Dive.md")
