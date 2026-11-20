import subprocess
from pathlib import Path

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")

# 1. Search git log for any mention of "SITASI LANGSUNG" or "BAB 1" or "BAB 3"
print("=== Git log search for files ===")
res = subprocess.run(["git", "log", "--all", "--full-history", "--diff-filter=A", "--summary"], capture_output=True, text=True, cwd=ROOT)
for line in res.stdout.splitlines():
    if "create mode" in line and (".md" in line):
        print(line)

print("\n=== Check git lost-found blobs for keywords ===")
# run git fsck --lost-found
subprocess.run(["git", "fsck", "--lost-found"], capture_output=True, text=True, cwd=ROOT)
lost_found = ROOT / ".git/lost-found/other"
if lost_found.exists():
    for b in lost_found.glob("*"):
        try:
            content = b.read_text(encoding="utf-8", errors="ignore")
            first_line = content.splitlines()[0] if content.splitlines() else ""
            if "BAB" in content[:200] or "SITASI LANGSUNG" in content[:500] or "PENDAHULUAN" in content[:200]:
                print(f"Blob {b.name}: {first_line[:80]} (size: {b.stat().st_size})")
        except Exception as e:
            pass
