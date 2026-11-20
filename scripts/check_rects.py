with open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Konseptual_ARTHA.svg') as f:
    for i, line in enumerate(f):
        if '<rect' in line:
            print(f"{i}: {line.strip()[:80]}")

