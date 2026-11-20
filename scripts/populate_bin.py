import subprocess
from pathlib import Path

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
BIN_DIR = ROOT / "bin"
BIN_DIR.mkdir(parents=True, exist_ok=True)

# Map target filename in bin -> git blob or git path
git_items = {
    "BAB 1 - PENDAHULUAN (REVISI SITASI SAJA - BERANOTASI).md": "92aa5c16d6dda02d715739390f1bfbddab4886d3",
    "BAB 1 - PENDAHULUAN (SITASI LANGSUNG).md": "0aca6ecbb418b7c95248892b82eecb3e2a72cf74",
    "BAB 1 - PENDAHULUAN.md": "c3561cf08d32fb8cb04ba69b8419a8a2ffa0e2be",
    "BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md": "02aa78441b85894a9f71f1d5edea9ce82c44aee9",
    "BAB 3 - RANCANGAN PROTOTIPE (DRAFT 1).md": "ca084220e7bdafd0ef0524a2536b7287445dcf7c",
    "BAB 3 - RANCANGAN PROTOTIPE (REVISI TEMPLATE TERBARU).md": "b6006d30515e50f4fc0caf7163b486318641e9c3",
    "BIMBINGAN_KE_1_BU_AYU.md": "HEAD:BIMBINGAN/BU AYU/BIMBINGAN_KE_1_BU_AYU.md",
    "WAWANCARA_PERTAMA_ARTHA.md": "HEAD:WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA_PERTAMA_ARTHA.md",
    "antislop.md": "dc3a3aab343cb1a950b07957bceaece31f2aad56",
}

for fname, source in git_items.items():
    dest_path = BIN_DIR / fname
    res = subprocess.run(["git", "cat-file", "-p", source], cwd=ROOT, capture_output=True)
    if res.returncode == 0 and len(res.stdout) > 0:
        dest_path.write_bytes(res.stdout)
        print(f"Restored to bin: {fname:<55} ({len(res.stdout):>6} bytes)")
    else:
        print(f"FAILED to extract: {fname} from {source}")

print("\nRestoration to bin complete!")
