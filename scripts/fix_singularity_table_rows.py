import pathlib
import re
import shutil

root = pathlib.Path(__file__).resolve().parent.parent / "Technological Singularity"

def clean_table_in_lines(lines):
    new_lines = []
    in_table = False
    table_lines = []
    
    def process_table(tbl):
        if not tbl:
            return []
        # Separate header, separator, data rows
        # A row is a list of cell strings
        rows = []
        for l in tbl:
            # strip leading/trailing pipe and split by pipe
            raw = l.strip()
            if raw.startswith('|') and raw.endswith('|'):
                cells = [c.strip() for c in raw[1:-1].split('|')]
                rows.append(cells)
            else:
                rows.append(None)
        
        # Check if rows[1] is separator (e.g. ['---', '---'])
        if len(rows) >= 2 and rows[1] is not None and all(re.match(r'^:?-+:?$', c) for c in rows[1]):
            header = rows[0]
            separator = rows[1]
            data_rows = []
            for r in rows[2:]:
                if r is None:
                    continue
                # If first cell is empty or multiple cells are empty, check if continuation of previous row
                # Specifically, if len(r) == len(header)
                if len(r) == len(header):
                    if r[0] == '' and len(data_rows) > 0:
                        # continuation row! Merge into previous row
                        prev = data_rows[-1]
                        merged = []
                        for c_prev, c_curr in zip(prev, r):
                            if c_curr:
                                merged.append(f"{c_prev} {c_curr}".strip())
                            else:
                                merged.append(c_prev)
                        data_rows[-1] = merged
                    else:
                        # Clean up any empty trailing cells or empty interior cells if appropriate
                        # Replace any remaining empty cell with '-' if it's genuinely empty
                        cleaned_r = [c if c else '-' for c in r]
                        data_rows.append(cleaned_r)
                else:
                    # length mismatch
                    # Pad or trim
                    if len(r) < len(header):
                        r = r + ['-'] * (len(header) - len(r))
                    else:
                        # If there are empty cells at end, drop them
                        while len(r) > len(header) and r[-1] == '':
                            r.pop()
                        if len(r) > len(header):
                            # merge extras into last cell
                            r = r[:len(header)-1] + [' '.join(r[len(header)-1:])]
                    cleaned_r = [c if c else '-' for c in r]
                    data_rows.append(cleaned_r)
            
            # Format table nicely
            out = []
            out.append('| ' + ' | '.join(header) + ' |')
            out.append('| ' + ' | '.join(separator) + ' |')
            for dr in data_rows:
                out.append('| ' + ' | '.join(dr) + ' |')
            return out
        else:
            return tbl

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('|') and line.strip().endswith('|'):
            table_lines.append(line)
        else:
            if table_lines:
                new_lines.extend(process_table(table_lines))
                table_lines = []
            new_lines.append(line)
        i += 1
    if table_lines:
        new_lines.extend(process_table(table_lines))
    return new_lines

# Test on 01_Definition_Origins_and_Conceptual_Frameworks.md
sample_p = root / 'Core_Concepts/01_Definition_Origins_and_Conceptual_Frameworks.md'
old_lines = sample_p.read_text(encoding='utf-8').splitlines()
cleaned_lines = clean_table_in_lines(old_lines)
print('Before lines count:', len(old_lines), 'After lines count:', len(cleaned_lines))
joined = '\n'.join(cleaned_lines)
matches = re.findall(r'\|\s{2,}\|', joined)
print('Matches for empty column header:', len(matches))
