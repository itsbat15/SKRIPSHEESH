with open('JURNAL/36_REFERENSI_TXT/Dumas_dkk_2018_Fundamentals_of_BPM.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== HALAMAN ')

# Function to search keyword in pages
def find_keyword_pages(keywords, start_p=50, end_p=200):
    results = []
    for idx in range(start_p, min(end_p, len(pages))):
        content = pages[idx]
        if all(k.lower() in content.lower() for k in keywords):
            # find internal page number
            lines = [l.strip() for l in content.split('\n') if l.strip()]
            first_few = " ".join(lines[:4])
            results.append((idx, first_few))
    return results

print("=== CHAPTER 3 START ===")
for p, h in find_keyword_pages(['Chapter 3', 'Essential Process Modeling'], 60, 120):
    print(f"PDF page {p}: {h[:80]}")

print("\n=== FIRST STEPS WITH BPMN (Start/End Event, Activity, Sequence Flow) ===")
for p, h in find_keyword_pages(['First Steps with BPMN'], 80, 120):
    print(f"PDF page {p}: {h[:80]}")

print("\n=== EXCLUSIVE GATEWAY (XOR) ===")
for p, h in find_keyword_pages(['Exclusive Decisions', 'gateway'], 80, 130):
    print(f"PDF page {p}: {h[:80]}")

print("\n=== PARALLEL GATEWAY (AND) ===")
for p, h in find_keyword_pages(['Parallel Execution', 'gateway'], 80, 130):
    print(f"PDF page {p}: {h[:80]}")

print("\n=== POOLS AND LANES (Resources) ===")
for p, h in find_keyword_pages(['Pool', 'Lane'], 100, 150):
    print(f"PDF page {p}: {h[:80]}")

print("\n=== MESSAGE FLOW ===")
for p, h in find_keyword_pages(['Message Flow'], 100, 150):
    print(f"PDF page {p}: {h[:80]}")

print("\n=== INTERMEDIATE EVENT (Chapter 4) ===")
for p, h in find_keyword_pages(['Intermediate', 'Event'], 120, 180):
    print(f"PDF page {p}: {h[:80]}")

