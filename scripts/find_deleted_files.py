import os
import sys
from pathlib import Path
import subprocess

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")

print("=== 1. Checking git status for deleted files ===")
res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=ROOT)
for line in res.stdout.splitlines():
    if line.strip().startswith("D "):
        print(f"Git deleted: {line.strip()}")

print("\n=== 2. Checking BAB3_PENDUKUNG_2026-10-25 ===")
p_dir = ROOT / "BAB3_PENDUKUNG_2026-10-25"
if p_dir.exists():
    for f in p_dir.glob("**/*"):
        if f.is_file():
            print(f"  {f.relative_to(ROOT)} ({f.stat().st_size} bytes)")

print("\n=== 3. Checking other folders for draft copies ===")
for pattern in ["*BAB 1*", "*BAB 3*", "*DRAFT*", "*REVISI*"]:
    for f in ROOT.glob(pattern):
        if f.is_file():
            print(f"Root match: {f.name} ({f.stat().st_size} bytes)")

print("\n=== 4. Checking git fsck / lost-found ===")
res_fsck = subprocess.run(["git", "fsck", "--lost-found"], capture_output=True, text=True, cwd=ROOT)
print(res_fsck.stdout[:500])
