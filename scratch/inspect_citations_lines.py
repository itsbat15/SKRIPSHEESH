import json

for p in range(1, 6):
    with open(f"c:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/scratch/p{p}_boxes.json", "r", encoding="utf-8-sig") as f:
        lines = json.load(f)
    print(f"\n================ PAGE {p} ================")
    for idx, item in enumerate(lines):
        text = item["Text"]
        # Match citations
        if p == 1 and "purpose of this paper" in text.lower():
            print(f"--- P1 #1 Abstract (Starts at line {idx}) ---")
            for j in range(idx, idx + 8):
                print(f"  Line {j}: {lines[j]['Text']} -> (X={lines[j]['X']}, Y={lines[j]['Y']}, W={lines[j]['W']}, H={lines[j]['H']})")
        elif p == 1 and "unattainable" in text.lower():
            print(f"--- P1 #2 Sec 2 PXP (Starts at line {idx}) ---")
            for j in range(idx, idx + 12):
                if j < len(lines):
                    print(f"  Line {j}: {lines[j]['Text']} -> (X={lines[j]['X']}, Y={lines[j]['Y']}, W={lines[j]['W']}, H={lines[j]['H']})")
        elif p == 2 and "shows the process script" in text.lower():
            print(f"--- P2 #3 Sec 3 User Stories (Starts at line {idx}) ---")
            for j in range(idx, idx + 9):
                print(f"  Line {j}: {lines[j]['Text']} -> (X={lines[j]['X']}, Y={lines[j]['Y']}, W={lines[j]['W']}, H={lines[j]['H']})")
        elif p == 3 and "developed in iterations" in text.lower():
            print(f"--- P3 #4 Sec 3 Baselines (Starts at line {idx}) ---")
            for j in range(idx, idx + 8):
                print(f"  Line {j}: {lines[j]['Text']} -> (X={lines[j]['X']}, Y={lines[j]['Y']}, W={lines[j]['W']}, H={lines[j]['H']})")
        elif p == 3 and "as a lone developer it is easy" in text.lower():
            print(f"--- P3 #5 Table 2 Practices (Starts at line {idx}) ---")
            for j in range(idx, idx + 12):
                if j < len(lines):
                    print(f"  Line {j}: {lines[j]['Text']} -> (X={lines[j]['X']}, Y={lines[j]['Y']}, W={lines[j]['W']}, H={lines[j]['H']})")
        elif p == 4 and "iterative development cycle" in text.lower():
            print(f"--- P4 #6 Sec 4 PXP at Work (Starts at line {idx}) ---")
            for j in range(idx, idx + 7):
                print(f"  Line {j}: {lines[j]['Text']} -> (X={lines[j]['X']}, Y={lines[j]['Y']}, W={lines[j]['W']}, H={lines[j]['H']})")
        elif p == 5 and "balance between" in text.lower():
            print(f"--- P5 #7 Sec 5 Conclusions (Starts at line {idx}) ---")
            for j in range(idx - 2, idx + 5):
                print(f"  Line {j}: {lines[j]['Text']} -> (X={lines[j]['X']}, Y={lines[j]['Y']}, W={lines[j]['W']}, H={lines[j]['H']})")

