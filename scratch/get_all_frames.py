import json

with open(r'C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\.system_generated\steps\20572\output.txt', encoding='utf-8') as f:
    data = json.load(f)

for p in data['pages']:
    print('PAGE:', p.get('name'))
    frames = [c for c in p.get('children', []) if c.get('type') == 'FRAME']
    print(f"Total frames: {len(frames)}")
    for f in frames:
        print(f"ID={f['id']} | Name='{f.get('name')}' | Width={f.get('width')} | Height={f.get('height')} | X={f.get('x')} | Y={f.get('y')}")

