import json

with open(r'C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\.system_generated\steps\20572\output.txt', encoding='utf-8') as f:
    data = json.load(f)

for p in data['pages']:
    print('PAGE:', p.get('name'))
    for c in p.get('children', []):
        name = c.get('name')
        cid = c.get('id')
        ctype = c.get('type')
        bounds = c.get('absoluteBounds')
        print(f"ID={cid} | Type={ctype} | Name='{name}' | Bounds={bounds}")

