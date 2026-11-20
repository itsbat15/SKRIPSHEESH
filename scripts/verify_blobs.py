import subprocess
from pathlib import Path

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")

def get_blob_content(blob_hash):
    res = subprocess.run(["git", "cat-file", "-p", blob_hash], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    return res.stdout

files_to_restore = {
    "BAB 1 - PENDAHULUAN (REVISI SITASI SAJA - BERANOTASI).md": "92aa5c16d6dda02d715739390f1bfbddab4886d3",
    "BAB 1 - PENDAHULUAN (SITASI LANGSUNG).md": "0aca6ecbb418b7c95248892b82eecb3e2a72cf74",
    "BAB 1 - PENDAHULUAN.md": "c3561cf08d32fb8cb04ba69b8419a8a2ffa0e2be",
    "BAB 1 - PENDAHULUAN (PENYEMPURNAAN 2026-10-24).md": "9312ce1f387a750f77b2d766a59f858ca2cb1916",
    "BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md": "02aa78441b85894a9f71f1d5edea9ce82c44aee9",
    "BAB 3 - RANCANGAN PROTOTIPE (DRAFT 1).md": "ca084220e7bdafd0ef0524a2536b7287445dcf7c",
    "BAB 3 - RANCANGAN PROTOTIPE (REVISI TEMPLATE TERBARU).md": "b6006d30515e50f4fc0caf7163b486318641e9c3",
    "KOREKSI AKADEMIK BAB 1 DAN BAB 2 - 2026-10-25.md": "ba7334edb232ff69bb3dbe249afc288136431c85",
    "antislop.md": "dc3a3aab343cb1a950b07957bceaece31f2aad56",
}

print("=== Checking Blobs ===")
for name, blob in files_to_restore.items():
    content = get_blob_content(blob)
    first_line = content.splitlines()[0] if content.splitlines() else ""
    print(f"{name:<55} | {len(content):>7} chars | {first_line[:40]}")
