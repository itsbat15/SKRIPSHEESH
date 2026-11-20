import json
from pathlib import Path

DIR_BAB1 = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\BAB 1")
MD_DIR = DIR_BAB1 / "md"

print(f"Directory: {DIR_BAB1}")

# 1. Rename PDF files in BAB 1
renamed_files = {}

for f in sorted(DIR_BAB1.glob("*.pdf")):
    old_name = f.name
    if old_name.startswith("STABILO_"):
        new_name = "ditandain_" + old_name[len("STABILO_"):]
    elif not old_name.startswith("ditandain_"):
        new_name = "ditandain_" + old_name
    else:
        new_name = old_name
        
    target_path = DIR_BAB1 / new_name
    if old_name != new_name:
        f.rename(target_path)
        print(f"Renamed PDF: {old_name} -> {new_name}")
    renamed_files[old_name] = new_name

# 2. Check md folder
if MD_DIR.exists():
    for f in list(MD_DIR.glob("*")):
        old_name = f.name
        if "STABILO" in old_name:
            new_name = old_name.replace("TERSTABILO", "DITANDAIN").replace("STABILO", "DITANDAIN")
            target_path = MD_DIR / new_name
            f.rename(target_path)
            print(f"Renamed MD file: {old_name} -> {new_name}")

print("\nPDF renaming completed. Now updating markdown and json...")
