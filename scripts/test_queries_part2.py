import json
from pathlib import Path
import fitz

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
AUD = ROOT / "JURNAL" / "AUDIT_SITASI_BAB1_2026-10-25"
data = json.loads((AUD / "MATRIKS_KLAIM_DAN_HALAMAN.json").read_text(encoding="utf-8"))
sources = {s["id"]: s for s in data["sources"]}

def test_queries(s_id, pno, queries):
    s = sources[s_id]
    doc = fitz.open(s["file"])
    page = doc[pno - 1]
    print(f"\n--- {s_id} ({Path(s['file']).name}) Page {pno} ---")
    for q in queries:
        res = page.search_for(q)
        print(f"  Query '{q}': {len(res)} match(es)")
    doc.close()

# S01 Tiana: Page 1, 2
test_queries("S01", 1, ["bimbingan belajar", "alternatif pendidikan non-formal", "pendaftaran", "jadwal", "pembayaran"])
test_queries("S01", 2, ["bimbingan belajar", "administrasi", "Waterfall"])

# S02 Pradana: Page 2, 4
test_queries("S02", 2, ["sistem informasi yang terintegrasi", "manajemen pendidikan", "teknologi informasi"])
test_queries("S02", 4, ["otomatisasi", "administrasi", "keuangan"])

# S03 Fajriansyah: Page 2, 10, 11
test_queries("S03", 2, ["efisiensi operasional", "Bee Hive", "pendaftaran siswa"])
test_queries("S03", 10, ["Analisis Efektivitas dan Dampak Operasional", "pendaftaran", "10-15 menit"])
test_queries("S03", 11, ["kesimpulan", "efektivitas", "pendaftaran siswa"])

# S05 Hendri: Page 1, 2
test_queries("S05", 1, ["catatan siswa dan catatan bendahara", "SPP", "Yayasan Semesta Khatulistiwa"])
test_queries("S05", 2, ["penerimaan kas", "catatan", "bendahara"])

# S06 Ramadhan: Page 13, 15, 17
test_queries("S06", 13, ["pencatatan", "cabang", "kantor pusat", "Rams Dimsum"])
test_queries("S06", 15, ["pencatatan transaksi secara mandiri", "laporan keuangan cabang", "rekapitulasi"])
test_queries("S06", 17, ["Rekap Penjualan Harian", "Tabel 8", "kesimpulan"])

# S07 Sudirman: Page 1, 2
test_queries("S07", 1, ["rekening koran bank", "rekonsiliasi", "kas"])
test_queries("S07", 2, ["rekening koran bank", "pengendalian kas", "metode rekonsiliasi"])

# S08 Kabisatullah: Page 5, 6, 7
test_queries("S08", 5, ["reservasi", "ruang rapat", "antarmuka", "kapasitas"])
test_queries("S08", 6, ["Capacity", "Constraint Satisfaction Problem", "constraint"])
test_queries("S08", 7, ["pengujian", "Constraint Satisfaction Problem", "kesimpulan"])

# S09 Khafidhoh: Page 1, 2, 5
test_queries("S09", 1, ["uneven distribution of teaching assignments", "jadwal", "AHE"])
test_queries("S09", 2, ["Sistem Penjadwalan", "algoritma genetika", "konflik"])
test_queries("S09", 5, ["Sistem Penjadwalan", "pengujian", "kesimpulan"])

# S10 Gunawan: Page 1, 9
test_queries("S10", 1, ["registrasi", "penjadwalan", "presensi", "verifikasi pembayaran"])
test_queries("S10", 9, ["verifikasi pembayaran", "pembayaran", "antarmuka"])

# S12 Thiovanda: Page 1, 4, 5
test_queries("S12", 1, ["penjadwalan", "pembayaran", "Jia Jia Education"])
test_queries("S12", 4, ["Cabang Management", "cabang", "admin"])
test_queries("S12", 5, ["verifikasi pembayaran", "bukti pembayaran", "kesimpulan"])

# S16 Beck: Page 104
test_queries("S16", 104, ["Pair Programming", "Write all production programs with two people"])

# S18 Mishra: Page 3, 4, 9, 12
test_queries("S18", 3, ["team cohesiveness", "Agile"])
test_queries("S18", 4, ["team cohesiveness", "Extreme Programming"])
test_queries("S18", 9, ["Agile development frameworks", "Extreme Programming", "XP"])
test_queries("S18", 12, ["Extreme Programming", "Table 4", "expertise"])

# UU01
uu_path = ROOT / "JURNAL" / "UNDANG UNDANG BIMBEL" / "UU Nomor 20 Tahun 2003.pdf"
doc_uu = fitz.open(uu_path)
print(f"\n--- UU01 (UU Nomor 20 Tahun 2003.pdf) ---")
for pno in [13, 14, 46]:
    page = doc_uu[pno - 1]
    print(f"Page {pno}:")
    for q in ["Pendidikan Nonformal", "Pasal 26", "lembaga kursus", "berfungsi sebagai pengganti"]:
        res = page.search_for(q)
        print(f"  Query '{q}': {len(res)} match(es)")
doc_uu.close()
