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
        lines = f.readlines()

    # Rule 1: Em-dash in PROSE
    prose_em_dashes = []
    for line_num, line in enumerate(lines, 1):
        line_s = line.strip()
        # ignore table rows and horizontal rules
        if line_s.startswith('|') or line_s.startswith('---'):
            continue
        matches = re.findall(r'[—–]|(?<!- கூட்ட)--(?!-)', line) # or simple find
        # Actually any '—' or '–' or '--' in prose
        for m in re.finditer(r'[—–]|--', line):
            prose_em_dashes.append((line_num, m.group(), line.strip()))

    if prose_em_dashes:
        print(f"[FAIL] Found {len(prose_em_dashes)} em-dashes in prose:")
        for ln, d, text in prose_em_dashes[:5]:
            print(f"  Line {ln}: [{d}] in '{text[:80]}...'")
    else:
        print("[PASS] ZERO em-dashes in prose!")

for f in files_to_check:
    check_file(f)

