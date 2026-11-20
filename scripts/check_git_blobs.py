import subprocess
from pathlib import Path

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")

# Run git fsck --lost-found
subprocess.run(["git", "fsck", "--lost-found"], cwd=ROOT, capture_output=True)

lost_other = ROOT / ".git/lost-found/other"
print("Lost found other exists:", lost_other.exists())
if lost_other.exists():
    blobs = list(lost_other.glob("*"))
    print(f"Total dangling blobs/trees: {len(blobs)}")
    for b in blobs:
        try:
            raw = b.read_bytes()
            if b"BAB 1" in raw or b"SITASI" in raw or b"PENDAHULUAN" in raw or b"RANCANGAN PROTOTIPE" in raw:
                head = raw[:150].decode('utf-8', errors='ignore').replace('\n', ' ')
                print(f"Blob {b.name} ({len(raw)} bytes): {head}")
        except Exception as e:
            pass
