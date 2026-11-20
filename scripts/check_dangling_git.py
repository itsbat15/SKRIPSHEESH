import subprocess
from pathlib import Path

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")

# Get all dangling objects from git fsck
res = subprocess.run(["git", "fsck", "--lost-found"], cwd=ROOT, capture_output=True, text=True)
for line in res.stdout.splitlines():
    parts = line.strip().split()
    if len(parts) >= 3 and parts[0] == "dangling":
        obj_type = parts[1]
        obj_hash = parts[2]
        if obj_type == "tree":
            # list tree
            res_tree = subprocess.run(["git", "ls-tree", obj_hash], cwd=ROOT, capture_output=True, text=True)
            for item in res_tree.stdout.splitlines():
                if ".md" in item:
                    print(f"Tree {obj_hash} contains: {item}")
        elif obj_type == "commit":
            # show commit summary
            res_commit = subprocess.run(["git", "show", "--stat", "--oneline", obj_hash], cwd=ROOT, capture_output=True, text=True)
            print(f"Commit {obj_hash}: {res_commit.stdout[:200]}")
