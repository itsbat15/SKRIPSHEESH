from pathlib import Path

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")

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

print("Bab 1 files to delete:")
for f in bab1_to_delete:
    print(f"  {f.name} (exists: {f.exists()})")

print("\nBab 3 files to delete:")
for f in bab3_to_delete:
    print(f"  {f.name} (exists: {f.exists()})")

print("\nFiles to KEEP:")
print(f"  BAB 1: {(ROOT / 'BAB 1 - PENDAHULUAN (VERSI 11 PARAGRAF).md').exists()}")
print(f"  BAB 2: {(ROOT / 'BAB_2_TINJAUAN_PUSTAKA.md').exists()}")
print(f"  BAB 3 (REVISI TEMPLATE TERBARU copy): {(ROOT / 'BAB 3 - RANCANGAN PROTOTIPE (REVISI TEMPLATE TERBARU) copy.md').exists()}")
print(f"  BAB 3 (DRAFT 1 copy): {(ROOT / 'BAB 3 - RANCANGAN PROTOTIPE (DRAFT 1) copy.md').exists()}")
