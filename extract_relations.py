with open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 2\2.2_Penelitian_Terdahulu.md', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if line.startswith('|') and not line.startswith('| No') and not line.startswith('| :---:'):
        parts = [p.strip() for p in line.split('|')[1:-1]]
        if len(parts) >= 6:
            row_no = parts[0]
            author = parts[1]
            relation = parts[5]
            print(f"=== BARIS {row_no} ({author[:30]}) ===")
            print(relation)
            print()

