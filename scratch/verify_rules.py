import re

files_to_check = [
    r'DRAFT PROPOSAL MD\BAB 3\3.5_Spesifikasi_Teknis.md',
    r'DRAFT PROPOSAL MD\BAB 3\3.6_Jadwal_Pembuatan_Prototipe.md',
    r'DRAFT PROPOSAL MD\BAB 3\3.4 Konsep Prototipe MD\3.4.7_Perancangan_Antarmuka_Pengguna.md',
    r'DRAFT PROPOSAL MD\BAB 3\BAB_3_DESAIN_DAN_IMPLEMENTASI.md',
]

def check_file(filepath):
    print(f"\n=================== Checking {filepath} ===================")
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Rule 1: Em-dash
    em_dashes = re.findall(r'[—–]|--', text)
    if em_dashes:
        print(f"[FAIL] Found {len(em_dashes)} em-dashes: {em_dashes[:5]}")
    else:
        print("[PASS] Zero em-dashes found.")

    # Rule 2: Single sentence paragraphs
    # Split text into paragraphs (separated by 2 or more newlines)
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    single_sentence_paras = []
    for i, p in enumerate(paragraphs):
        # Ignore headings, tables, image tags, horizontal rules, code blocks, bullet/numbered lists
        lines = p.splitlines()
        first_line = lines[0].strip()
        if (first_line.startswith('#') or 
            first_line.startswith('|') or 
            first_line.startswith('![') or 
            first_line.startswith('**Gambar') or 
            first_line.startswith('**Tabel') or 
            first_line.startswith('---') or
            first_line.startswith('```') or
            first_line.startswith('*') or
            re.match(r'^\d+\.', first_line)):
            continue

        # Count sentences
        # Simple heuristic: end with ., ?, or ! followed by space or end of string
        cleaned_p = re.sub(r'\(.*?\)', '', p) # remove parentheses
        sentences = re.split(r'(?<=[.?!])\s+', p.replace('\n', ' ').strip())
        sentences = [s for s in sentences if len(s.strip()) > 5]
        if len(sentences) == 1:
            single_sentence_paras.append((i, p))

    if single_sentence_paras:
        print(f"[WARN] Found {len(single_sentence_paras)} potential single-sentence paragraphs:")
        for idx, p in single_sentence_paras[:3]:
            print(f"  Para {idx}: {p[:120]}...")
    else:
        print("[PASS] No single-sentence paragraphs found in narrative blocks.")

    # Rule 3: Sentences starting with digits
    sentences_starting_with_digit = []
    for line in text.splitlines():
        line_s = line.strip()
        # ignore table rows, numbered lists (e.g. "1. "), headers, and image captions
        if line_s.startswith('|') or re.match(r'^\d+\.\s', line_s) or line_s.startswith('#') or line_s.startswith('![') or line_s.startswith('`'):
            continue
        # check if line starts with a digit that isn't a list item
        if re.match(r'^\d', line_s):
            sentences_starting_with_digit.append(line_s)

    if sentences_starting_with_digit:
        print(f"[WARN] Lines starting with digits: {sentences_starting_with_digit[:3]}")
    else:
        print("[PASS] No narrative lines starting with digits.")

for f in files_to_check:
    check_file(f)

