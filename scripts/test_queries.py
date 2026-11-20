import json
from pathlib import Path
import fitz

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
AUD = ROOT / "JURNAL" / "AUDIT_SITASI_BAB1_2026-10-25"
data = json.loads((AUD / "MATRIKS_KLAIM_DAN_HALAMAN.json").read_text(encoding="utf-8"))
sources = {s["id"]: s for s in data["sources"]}

# Check specific queries
def test_queries(s_id, pno, queries):
    s = sources[s_id]
    doc = fitz.open(s["file"])
    page = doc[pno - 1]
    print(f"\n--- {s_id} ({Path(s['file']).name}) Page {pno} ---")
    for q in queries:
        res = page.search_for(q)
        print(f"  Query '{q}': {len(res)} match(es)")
    doc.close()

# Ahadi: S04 - Page 7, 8
test_queries("S04", 7, ["Owner", "PIC Cabang", "Hak Akses"])
test_queries("S04", 8, ["Owner", "PIC Cabang", "Front Office"])

# Fikri: S20 - Page 3, 4, 5
test_queries("S20", 3, ["Requirements", "Personal Extreme Programming", "PxP"])
test_queries("S20", 4, ["Planning", "Design", "Implementation", "System Testing"])
test_queries("S20", 5, ["Retrospective", "klien", "pengujian"])

# Sidiq: S21 - Page 3, 4, 11
test_queries("S21", 3, ["Personal Extreme Programming", "PxP", "iterasi"])
test_queries("S21", 4, ["Design", "Implementation", "System Testing", "Retrospective"])
test_queries("S21", 11, ["kesimpulan", "50 hari", "37 hari", "pengujian"])

# Barizi: S11 - Page 1, 5, 6, 7
test_queries("S11", 1, ["Sekolah Musik", "Java", "pembayaran", "penjadwalan"])
test_queries("S11", 5, ["menu", "pembayaran", "jadwal", "tampilan"])
test_queries("S11", 6, ["jadwal", "pembayaran", "transaksi"])
test_queries("S11", 7, ["kesimpulan", "Java", "penjadwalan", "pembayaran"])

# Safitri: S13 - Page 1, 5, 6
test_queries("S13", 1, ["WhatsApp", "notifikasi", "SPP"])
test_queries("S13", 5, ["WhatsApp", "notifikasi", "broadcast", "pembayaran"])
test_queries("S13", 6, ["WhatsApp", "notifikasi", "Tabel 1", "logout"])

# Schwaber: S14 - Page 6, 10
test_queries("S14", 6, ["Scrum Team", "Developers", "Product Owner", "Scrum Master"])
test_queries("S14", 10, ["Daily Scrum", "Product Owner", "Scrum Master", "Developers"])

# Sommerville: S15 - Page 62, 63, 77, 760
test_queries("S15", 62, ["Prototyping", "Figure 2.9", "Evaluation report"])
test_queries("S15", 63, ["prototype", "throw-away", "throwaway"])
test_queries("S15", 77, ["Customer involvement", "Agile"])
test_queries("S15", 760, ["rapid application development", "RAD"])

# Pressman: S19 - Page 79, 80
test_queries("S19", 79, ["Component-Based Development", "component"])
test_queries("S19", 80, ["Component-Based Development", "reuse"])
