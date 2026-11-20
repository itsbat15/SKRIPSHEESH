import shutil
from pathlib import Path

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")

# 1. Target files to delete
bab1_to_delete = [
    ROOT / "BAB 1 - PENDAHULUAN (REVISI SITASI SAJA - BERANOTASI).md",
    ROOT / "BAB 1 - PENDAHULUAN (SITASI LANGSUNG).md",
    ROOT / "BAB 1 - PENDAHULUAN.md",
]

bab3_to_delete = [
    ROOT / "BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md",
    ROOT / "BAB 3 - RANCANGAN PROTOTIPE (DRAFT 1).md",
    ROOT / "BAB 3 - RANCANGAN PROTOTIPE (REVISI TEMPLATE TERBARU).md",
]

for f in bab1_to_delete + bab3_to_delete:
    if f.exists():
        f.unlink()
        print(f"Deleted: {f.name}")
    else:
        print(f"Already not present: {f.name}")

# 2. Create DRAFT PROPOSAL MD folder and subfolders
DRAFT_DIR = ROOT / "DRAFT PROPOSAL MD"
BAB1_DIR = DRAFT_DIR / "BAB 1"
BAB2_DIR = DRAFT_DIR / "BAB 2"
BAB3_DIR = DRAFT_DIR / "BAB 3"

BAB1_DIR.mkdir(parents=True, exist_ok=True)
BAB2_DIR.mkdir(parents=True, exist_ok=True)
BAB3_DIR.mkdir(parents=True, exist_ok=True)
print("\nCreated folder structure in DRAFT PROPOSAL MD: BAB 1, BAB 2, BAB 3")

# 3. Copy files into their respective folders
# Bab 1
src_bab1 = ROOT / "BAB 1 - PENDAHULUAN (VERSI 11 PARAGRAF).md"
if src_bab1.exists():
    shutil.copy2(src_bab1, BAB1_DIR / src_bab1.name)
    print(f"Copied {src_bab1.name} -> {BAB1_DIR}")

# Copy image to BAB 1 folder so relative markdown link works seamlessly
src_img = ROOT / "Gambar 1.1 Diagram Alir Kerangka Pengerjaan Tugas Akhir.png"
if src_img.exists():
    shutil.copy2(src_img, BAB1_DIR / src_img.name)
    print(f"Copied image {src_img.name} -> {BAB1_DIR}")

# Bab 2
src_bab2 = ROOT / "BAB_2_TINJAUAN_PUSTAKA.md"
if src_bab2.exists():
    shutil.copy2(src_bab2, BAB2_DIR / src_bab2.name)
    print(f"Copied {src_bab2.name} -> {BAB2_DIR}")

# Bab 3
src_bab3_revisi = ROOT / "BAB 3 - RANCANGAN PROTOTIPE (REVISI TEMPLATE TERBARU) copy.md"
if src_bab3_revisi.exists():
    shutil.copy2(src_bab3_revisi, BAB3_DIR / src_bab3_revisi.name)
    print(f"Copied {src_bab3_revisi.name} -> {BAB3_DIR}")

src_bab3_draft1 = ROOT / "BAB 3 - RANCANGAN PROTOTIPE (DRAFT 1) copy.md"
if src_bab3_draft1.exists():
    shutil.copy2(src_bab3_draft1, BAB3_DIR / src_bab3_draft1.name)
    print(f"Copied {src_bab3_draft1.name} -> {BAB3_DIR}")

print("\nAll operations completed successfully!")
