import json

with open(r'C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\.system_generated\steps\20572\output.txt', encoding='utf-8') as f:
    data = json.load(f)

page = data['pages'][0]
frames = [
    (2, "Gambar 3.10: Mockup Login Cabang", 0.0, 0.0, 1440.0, 960.0),
    (32, "Gambar 3.11: Mockup Dasbor Kasir Cabang", 1600.0, 0.0, 1440.0, 960.0),
    (174, "Gambar 3.12: Mockup Pendaftaran Siswa", 3200.0, 0.0, 1440.0, 960.0),
    (264, "Gambar 3.13: Mockup Kasir & Kuitansi PDF", 4800.0, 0.0, 1440.0, 960.0),
    (371, "Gambar 3.14: Mockup Dasbor Pusat Pemilik", 0.0, 1100.0, 1440.0, 960.0),
    (544, "Gambar 3.15: Mockup Verifikasi Transfer", 1600.0, 1100.0, 1440.0, 960.0),
    (644, "Gambar 3.16: Mockup Pengawasan Tunggakan", 3200.0, 1100.0, 1440.0, 960.0),
    (763, "Gambar 3.17: Mockup Rekapitulasi Kas Multicabang", 4800.0, 1100.0, 1440.0, 960.0),
]

for fid, fname, fx, fy, fw, fh in frames:
    print(f"\n==================== {fname} (ID={fid}) ====================")
    # Find all children overlapping this frame
    texts = []
    for c in page.get('children', []):
        b = c.get('absoluteBounds', {})
        cx = b.get('x', 0)
        cy = b.get('y', 0)
        if fx <= cx < fx + fw and fy <= cy < fy + fh:
            if c.get('type') == 'TEXT':
                texts.append((c.get('name'), c.get('characters', '')))
    print(f"Total text elements: {len(texts)}")
    for tname, tval in texts[:20]:
        print(f"  [{tname}]: {tval}")

