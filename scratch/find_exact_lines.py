import json

keywords = [
    ("purpose of this paper", "P1 #1 Abstract"),
    ("unattainable", "P1 #2 Section 2 PXP"),
    ("user stories are written", "P2 #3 Section 3 / Table 1"),
    ("developed in iterations", "P3 #4 Section 3 / Baselines"),
    ("simple design", "P3 #5 Table 2 Core Practices"),
    ("iterative development cycle", "P4 #6 Section 4 PXP at Work"),
    ("balance between", "P5 #7 Section 5 Conclusions")
]

for p in range(1, 6):
    with open(f"c:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/scratch/p{p}_lines.json", "r", encoding="utf-8-sig") as f:
        lines = json.load(f)
    print(f"=== Page {p} ({len(lines)} lines) ===")
    for idx, item in enumerate(lines):
        text = item["Text"]
        for kw, desc in keywords:
            if kw.lower() in text.lower():
                print(f"  [{desc}] Line {idx}: {repr(text)}")
                print(f"    box: X={item['X']:.1f}, Y={item['Y']:.1f}, W={item['W']:.1f}, H={item['H']:.1f}")
                # Print surrounding lines
                start = max(0, idx - 2)
                end = min(len(lines), idx + 8)
                print("    Surrounding context:")
                for j in range(start, end):
                    print(f"      [{j}] {lines[j]['Text']}  (X={lines[j]['X']:.1f}, Y={lines[j]['Y']:.1f}, W={lines[j]['W']:.1f}, H={lines[j]['H']:.1f})")
