import shutil
from pathlib import Path

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
DRAFT_DIR = ROOT / "DRAFT PROPOSAL MD"
BIN_DIR = ROOT / "bin"
BIN_DIR.mkdir(parents=True, exist_ok=True)

# 1. Verify target copies in DRAFT PROPOSAL MD exist before deleting from root
chapter_pairs = [
    (ROOT / "BAB 1 - PENDAHULUAN (VERSI 11 PARAGRAF).md", DRAFT_DIR / "BAB 1" / "BAB 1 - PENDAHULUAN (VERSI 11 PARAGRAF).md"),
    (ROOT / "BAB_2_TINJAUAN_PUSTAKA.md", DRAFT_DIR / "BAB 2" / "BAB_2_TINJAUAN_PUSTAKA.md"),
    (ROOT / "BAB 3 - RANCANGAN PROTOTIPE (REVISI TEMPLATE TERBARU) copy.md", DRAFT_DIR / "BAB 3" / "BAB 3 - RANCANGAN PROTOTIPE (REVISI TEMPLATE TERBARU) copy.md"),
    (ROOT / "BAB 3 - RANCANGAN PROTOTIPE (DRAFT 1) copy.md", DRAFT_DIR / "BAB 3" / "BAB 3 - RANCANGAN PROTOTIPE (DRAFT 1) copy.md"),
]

print("=== 1. Removing duplicate chapter files from root ===")
for root_file, draft_file in chapter_pairs:
    if draft_file.exists() and draft_file.stat().st_size > 0:
        if root_file.exists():
            root_file.unlink()
            print(f"Deleted from root: {root_file.name}")
        else:
            print(f"Already removed: {root_file.name}")
    else:
        print(f"WARNING: Draft copy missing for {root_file.name}! Skipped deletion.")

# 2. Move 3 catatan files from root to bin
catatan_files = [
    "CATATAN PEMBIMBING BAB 3 COPY - 2026-10-25.md",
    "CATATAN PENGGUNAAN DRAF REVISI TERPADU BAB 1.md",
    "CATATAN REVIEW BAB 1 - 2026-10-24.md",
]

print("\n=== 2. Moving catatan files from root to bin ===")
for c_name in catatan_files:
    src = ROOT / c_name
    dest = BIN_DIR / c_name
    if src.exists():
        shutil.move(src, dest)
        print(f"Moved to bin: {c_name} -> bin/{c_name}")
    else:
        print(f"File not found in root: {c_name}")

print("\nCleanup and movement completed successfully!")
