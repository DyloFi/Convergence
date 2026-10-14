import pathlib
p = pathlib.Path('/Users/dylanboyle/Desktop/Convergence/Technological Singularity/Technological Singularity Overview.md')
lines = p.read_text(encoding='utf-8').splitlines()
for idx, l in enumerate(lines):
    if any(c in l for c in '┌├└│'):
        print(f"{idx}: {l}")
