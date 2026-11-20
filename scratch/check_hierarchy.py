import json

with open(r'C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\.system_generated\steps\20572\output.txt', encoding='utf-8') as f:
    data = json.load(f)

page = data['pages'][0]
print("Page children count:", len(page.get('children', [])))
for c in page.get('children', [])[:15]:
    print(f"Child of page: ID={c['id']}, type={c.get('type')}, name={c.get('name')}, children_count={len(c.get('children', []))}")

