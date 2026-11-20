import os
from pathlib import Path

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")

print("=== Search for filenames containing 'SITASI' or 'LANGSUNG' or 'BAB 1' or 'BAB 3' ===")
for p in ROOT.rglob("*.md"):
    name = p.name.lower()
    if any(k in name for k in ["sitasi", "langsung", "bab 1", "bab 3", "draft 1", "revisi template", "draf 2026"]):
        print(f"{p.stat().st_size:>8} bytes | {p.relative_to(ROOT)}")
