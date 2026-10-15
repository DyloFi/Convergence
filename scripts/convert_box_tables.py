import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent

def convert_boxes_in_text(text):
    lines = text.splitlines()
    new_lines = []
    i = 0
    in_box = False
    box_lines = []
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Detect start of box
        if stripped.startswith('┌') and ('Figure' in stripped or 'Architecture' in stripped or 'Dynamics' in stripped or '──' in stripped):
            in_box = True
            box_lines = [line]
            i += 1
            continue
            
        if in_box:
            box_lines.append(line)
            if stripped.startswith('└') and ('End Figure' in stripped or '──' in stripped):
                # End of box! Parse box_lines into markdown table
                in_box = False
                table_lines = parse_box_to_table(box_lines)
                new_lines.extend(table_lines)
                box_lines = []
            i += 1
            continue
            
        new_lines.append(line)
        i += 1
        
    if in_box and box_lines:
        # unclosed box, fallback
        new_lines.extend(box_lines)
        
    return '\n'.join(new_lines) + '\n'

def parse_box_to_table(box_lines):
    # Extract lines that have data (contain │ and not just borders)
    data_rows = []
    for l in box_lines:
        s = l.strip()
        if s.startswith('│') and s.endswith('│'):
            # It's a row
            # Split cells by │
            raw_cells = s[1:-1].split('│')
            cells = [c.strip() for c in raw_cells]
            # Ignore single header title rows like "CROSS-DOMAIN SYNTHESIS"
            if len(cells) == 1 and not ('Phase' in cells[0] or 'Dimension' in cells[0]):
                continue
            data_rows.append(cells)
            
    if not data_rows:
        return []
        
    # The first row with multiple cells is the header
    header = None
    rows = []
    for r in data_rows:
        if len(r) > 1:
            if header is None:
                header = r
            else:
                rows.append(r)
                
    if not header:
        return []
        
    # Normalize row lengths to match header
    num_cols = len(header)
    md_table = []
    md_table.append("| " + " | ".join(header) + " |")
    md_table.append("| " + " | ".join(["---"] * num_cols) + " |")
    for r in rows:
        # pad or truncate
        if len(r) < num_cols:
            r = r + [""] * (num_cols - len(r))
        elif len(r) > num_cols:
            r = r[:num_cols]
        md_table.append("| " + " | ".join(r) + " |")
        
    return [""] + md_table + [""]

# Test on Overview.md
target = root / 'Technological Singularity/Technological Singularity Overview.md'
old_text = target.read_text(encoding='utf-8')
new_text = convert_boxes_in_text(old_text)
print("Old length:", len(old_text.splitlines()))
print("New length:", len(new_text.splitlines()))
print("\nSample converted table snippet:")
for l in new_text.splitlines()[5:25]:
    print(l)

