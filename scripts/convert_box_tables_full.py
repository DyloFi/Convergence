import pathlib
import re
import shutil

root = pathlib.Path(__file__).resolve().parent.parent

def convert_boxes_in_text(text):
    lines = text.splitlines()
    new_lines = []
    i = 0
    in_box = False
    box_lines = []
    in_code_block = False
    code_fence = ""
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check for code block fences wrapping boxes
        if stripped.startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_fence = line
                # Lookahead: is the next line a box?
                if i + 1 < len(lines) and lines[i+1].strip().startswith("┌"):
                    # We will drop the fence and convert the box!
                    i += 1
                    continue
            else:
                in_code_block = False
                # If we were in a box that just ended, drop the closing fence
                if len(new_lines) > 0 and (new_lines[-1] == "" or new_lines[-1].startswith("|")):
                    i += 1
                    continue
                    
        # Detect start of box
        if stripped.startswith('┌') and ('Figure' in stripped or 'Architecture' in stripped or 'Dynamics' in stripped or '──' in stripped):
            in_box = True
            box_lines = [line]
            i += 1
            continue
            
        if in_box:
            box_lines.append(line)
            if stripped.startswith('└') and ('End Figure' in stripped or '──' in stripped):
                in_box = False
                table_lines = parse_box_to_table(box_lines)
                new_lines.extend(table_lines)
                box_lines = []
            i += 1
            continue
            
        new_lines.append(line)
        i += 1
        
    if in_box and box_lines:
        new_lines.extend(box_lines)
        
    return '\n'.join(new_lines) + '\n'

def parse_box_to_table(box_lines):
    data_rows = []
    for l in box_lines:
        s = l.strip()
        if s.startswith('│') and s.endswith('│'):
            raw_cells = s[1:-1].split('│')
            cells = [c.strip() for c in raw_cells]
            if len(cells) == 1 and not ('Phase' in cells[0] or 'Dimension' in cells[0]):
                continue
            data_rows.append(cells)
            
    if not data_rows:
        return []
        
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
        
    num_cols = len(header)
    md_table = []
    md_table.append("| " + " | ".join(header) + " |")
    md_table.append("| " + " | ".join(["---"] * num_cols) + " |")
    for r in rows:
        if len(r) < num_cols:
            r = r + [""] * (num_cols - len(r))
        elif len(r) > num_cols:
            r = r[:num_cols]
        md_table.append("| " + " | ".join(r) + " |")
        
    return [""] + md_table + [""]

# Process all files in Technological Singularity
ts_dir = root / 'Technological Singularity'
upgraded = 0
for f in ts_dir.rglob("*.md"):
    if f.name.endswith("_Expert_Review.md") or f.name.endswith(".bak.md"):
        continue
    content = f.read_text(encoding='utf-8')
    if any(c in content for c in '┌├└'):
        # backup
        bak = f.with_name(f.name + '.bak.md')
        if not bak.exists():
            shutil.copy2(f, bak)
        new_content = convert_boxes_in_text(content)
        f.write_text(new_content, encoding='utf-8')
        upgraded += 1
        print(f"Converted tables in: {f.name}")

print(f"Total files converted: {upgraded}")
