import json
from pathlib import Path
import fitz

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
AUD = ROOT / "JURNAL" / "AUDIT_SITASI_BAB1_2026-10-25"
data = json.loads((AUD / "MATRIKS_KLAIM_DAN_HALAMAN.json").read_text(encoding="utf-8"))
sources = {s["id"]: s for s in data["sources"]}

# Add UU01 to rows
all_rows = [
    {
        "id": "UU01",
        "paragraph": 1,
        "source": "UU01",
        "file": str(ROOT / "JURNAL" / "UNDANG UNDANG BIMBEL" / "UU Nomor 20 Tahun 2003.pdf"),
        "author": "Undang-Undang RI Nomor 20 Tahun 2003",
        "title": "Undang-Undang Republik Indonesia Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional",
        "status": "DIDUKUNG",
        "claim": "mengakui pendidikan nonformal sebagai jalur yang sah dalam mendukung pencapaian kompetensi akademik peserta didik",
        "locations": [
            [13, "13", "Bagian Kelima Pendidikan Nonformal, Pasal 26 ayat (1) dan (2)"],
            [14, "14", "Bagian Kelima Pendidikan Nonformal, Pasal 26 ayat (4), (5), dan (6)"],
            [46, "9", "Penjelasan Pasal 26 ayat (1) sampai (5)"]
        ],
        "anchor": "Pendidikan nonformal diselenggarakan bagi warga masyarakat yang memerlukan layanan pendidikan"
    }
]

for r in data["rows"]:
    s = sources[r["source"]]
    all_rows.append({
        "id": r["id"],
        "paragraph": r["paragraph"],
        "source": r["source"],
        "file": s["file"],
        "author": s["author"],
        "title": s["title"],
        "status": r["status"],
        "claim": r["claim"],
        "locations": r["locations"],
        "anchor": r["anchor"],
        "finding": r["finding"]
    })

print(f"Total items to verify: {len(all_rows)}")

# Test search for each
for item in all_rows:
    pdf_path = Path(item["file"])
    doc = fitz.open(pdf_path)
    locs = item["locations"]
    print(f"\n=== [{item['id']}] {item['author']} ({pdf_path.name}) ===")
    print(f"Anchor: '{item['anchor']}'")
    for loc in locs:
        pno = loc[0] - 1 # 0-indexed
        if pno < len(doc):
            page = doc[pno]
            # Try searching anchor or partial
            matches = page.search_for(item["anchor"])
            print(f"  Page {loc[0]} (print {loc[1]}): {len(matches)} match(es) for '{item['anchor']}'")
            if not matches:
                # Let's search words
                words = item["anchor"].split()
                if len(words) > 1:
                    w_match = page.search_for(words[0])
                    print(f"    Fallback search '{words[0]}': {len(w_match)} match(es)")
        else:
            print(f"  Page {loc[0]} out of range! (Max {len(doc)})")
    doc.close()
