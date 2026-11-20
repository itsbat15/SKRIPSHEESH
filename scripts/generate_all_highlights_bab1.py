"""
generate_all_highlights_bab1.py
===============================
Skrip otomatis untuk menandai (stabilo kuning / native PDF highlight annotation)
seluruh 22 sumber rujukan Bab 1 (28 titik sitasi: UU01 + A01 s.d. A27).
Sesuai Opsi 1: Seluruh PDF hasil stabilo disimpan ke folder khusus:
C:\\Users\\ARIEL\\OneDrive - MSFT\\Documents\\ARTHA\\JURNAL\\PDF_TERSTABILO_BAB1\\
tanpa menimpa berkas asli.
"""

import json
import time
from pathlib import Path
import fitz

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
OUT_DIR = ROOT / "JURNAL" / "PDF_TERSTABILO_BAB1"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Konfigurasi 22 dokumen sumber dan target penandaan
CONFIG = [
    {
        "id": "UU01",
        "title": "Undang-Undang RI Nomor 20 Tahun 2003",
        "src_path": ROOT / "JURNAL" / "UNDANG UNDANG BIMBEL" / "UU Nomor 20 Tahun 2003.pdf",
        "out_name": "STABILO_UU_Nomor_20_Tahun_2003.pdf",
        "pages_info": [
            {
                "pno": 13,
                "note": "UU01 (Pasal 26 ayat 1-2): Pendidikan nonformal sebagai pelengkap/pengganti pendidikan formal",
                "queries": [
                    "berfungsi sebagai pengganti",
                    "Pendidikan Nonformal",
                    "Pasal 26"
                ]
            },
            {
                "pno": 14,
                "note": "UU01 (Pasal 26 ayat 4-6): Lembaga kursus dan kesetaraan hasil pendidikan nonformal",
                "queries": [
                    "lembaga kursus",
                    "dihargai setara dengan hasil program pendidikan formal"
                ]
            },
            {
                "pno": 46,
                "note": "UU01 (Penjelasan Pasal 26): Tambahan Lembaran Negara",
                "queries": [
                    "Pasal 26"
                ]
            }
        ]
    },
    {
        "id": "S01_A01",
        "title": "Tiana dan Gunanto (2026)",
        "src_path": ROOT / "JURNAL" / "02_STUDI_KASUS_BIMBEL_DAN_KURSUS" / "SI Bimbel - Web Mobile - Waterfall - Tiana & Gunanto - 2026.pdf",
        "out_name": "STABILO_SI_Bimbel_Tiana_Gunanto_2026.pdf",
        "pages_info": [
            {
                "pno": 1,
                "note": "A01: Pengelolaan pendaftaran, jadwal, kehadiran dan pembayaran bimbel",
                "queries": [
                    "alternatif pendidikan non-formal",
                    "bimbingan belajar",
                    "pendaftaran",
                    "jadwal",
                    "pembayaran"
                ]
            },
            {
                "pno": 2,
                "note": "A01: Administrasi bimbingan belajar",
                "queries": [
                    "administrasi"
                ]
            }
        ]
    },
    {
        "id": "S02_A02",
        "title": "Pradana (2024)",
        "src_path": ROOT / "JURNAL" / "02_STUDI_KASUS_BIMBEL_DAN_KURSUS" / "Peran TI Manajemen Pendidikan - JRPP - Pradana - 2024.pdf",
        "out_name": "STABILO_Peran_TI_Pradana_2024.pdf",
        "pages_info": [
            {
                "pno": 2,
                "note": "A02: Pembahasan integrasi sistem informasi dan administrasi pendidikan",
                "queries": [
                    "sistem informasi yang terintegrasi"
                ]
            },
            {
                "pno": 4,
                "note": "A02: Administrasi dan keuangan pendidikan",
                "queries": [
                    "administrasi",
                    "keuangan"
                ]
            }
        ]
    },
    {
        "id": "S03_A03_A11",
        "title": "Fajriansyah dkk. (2026)",
        "src_path": ROOT / "JURNAL" / "02_STUDI_KASUS_BIMBEL_DAN_KURSUS" / "SI Bimbel Bee Hive - Efisiensi Operasional - JRIS - Fajriansyah dkk - 2026.pdf",
        "out_name": "STABILO_SI_Bimbel_Bee_Hive_Fajriansyah_2026.pdf",
        "pages_info": [
            {
                "pno": 2,
                "note": "A03/A11: Efisiensi operasional dan integrasi data bimbel Bee Hive",
                "queries": [
                    "efisiensi operasional",
                    "Bee Hive",
                    "pendaftaran siswa"
                ]
            },
            {
                "pno": 10,
                "note": "A03/A11: Analisis Efektivitas dan Dampak Operasional administrasi",
                "queries": [
                    "Analisis Efektivitas dan Dampak Operasional",
                    "pendaftaran"
                ]
            },
            {
                "pno": 11,
                "note": "A03/A11: Kesimpulan integrasi pendaftaran siswa",
                "queries": [
                    "pendaftaran siswa"
                ]
            }
        ]
    },
    {
        "id": "S04_A04_A17",
        "title": "Ahadi dkk. (2025)",
        "src_path": ROOT / "JURNAL" / "05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA" / "01_Multicabang_Hotel_Laravel_Djtechno_Ahadi_2025.pdf",
        "out_name": "STABILO_Multicabang_Hotel_Ahadi_2025.pdf",
        "pages_info": [
            {
                "pno": 7,
                "note": "A04/A17: Pemisahan hak akses Owner dan PIC Cabang serta laporan terpusat",
                "queries": [
                    "Owner",
                    "PIC Cabang"
                ]
            },
            {
                "pno": 8,
                "note": "A04/A17: Tabel pembagian peran multicabang (Owner, PIC Cabang, Front Office)",
                "queries": [
                    "Owner",
                    "PIC Cabang",
                    "Front Office"
                ]
            }
        ]
    },
    {
        "id": "S05_A05",
        "title": "Hendri dkk. (2025)",
        "src_path": ROOT / "JURNAL" / "05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA" / "05_Penerimaan Kas.pdf",
        "out_name": "STABILO_Penerimaan_Kas_Hendri_2025.pdf",
        "pages_info": [
            {
                "pno": 1,
                "note": "A05: Masalah pencocokan catatan siswa dan catatan bendahara SPP",
                "queries": [
                    "catatan siswa dan catatan bendahara",
                    "SPP",
                    "Yayasan Semesta Khatulistiwa"
                ]
            },
            {
                "pno": 2,
                "note": "A05: Alur penerimaan kas bendahara",
                "queries": [
                    "penerimaan kas",
                    "bendahara"
                ]
            }
        ]
    },
    {
        "id": "S06_A06_A18",
        "title": "Ramadhan dan Widodo (2026)",
        "src_path": ROOT / "JURNAL" / "05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA" / "02_Keuangan_Pusat_Cabang_Rams_Dimsum_IJLER_Ramadhan_2026.pdf",
        "out_name": "STABILO_Keuangan_Pusat_Cabang_Ramadhan_2026.pdf",
        "pages_info": [
            {
                "pno": 13,
                "note": "A06: Pencatatan operasional cabang dan kantor pusat",
                "queries": [
                    "pencatatan",
                    "kantor pusat",
                    "Rams Dimsum"
                ]
            },
            {
                "pno": 15,
                "note": "A06/A18: Rekomendasi pencatatan transaksi secara mandiri tiap cabang dan rekapitulasi",
                "queries": [
                    "pencatatan transaksi secara mandiri",
                    "rekapitulasi"
                ]
            },
            {
                "pno": 17,
                "note": "A18: Tabel 8 Rekap Penjualan Harian cabang ke pusat",
                "queries": [
                    "Rekap Penjualan Harian",
                    "Tabel 8"
                ]
            }
        ]
    },
    {
        "id": "S07_A07",
        "title": "Sudirman dan Tristianti (2021)",
        "src_path": ROOT / "JURNAL" / "05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA" / "06_Rekonsiliasi_Kas_Bank_MEANS_Sudirman_2021.pdf",
        "out_name": "STABILO_Rekonsiliasi_Kas_Bank_Sudirman_2021.pdf",
        "pages_info": [
            {
                "pno": 1,
                "note": "A07: Pencocokan catatan kas dengan rekening koran bank",
                "queries": [
                    "rekening koran bank",
                    "rekonsiliasi"
                ]
            },
            {
                "pno": 2,
                "note": "A07: Metode pengendalian kas bank dengan rekonsiliasi",
                "queries": [
                    "rekening koran bank",
                    "pengendalian kas",
                    "metode rekonsiliasi"
                ]
            }
        ]
    },
    {
        "id": "S08_A08_A16",
        "title": "Kabisatullah dan Noprisson (2026)",
        "src_path": ROOT / "JURNAL" / "05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA" / "04_Kapasitas_Ruang_RapaTrack_JUSIBI_Kabisatullah_2026.pdf",
        "out_name": "STABILO_Kapasitas_Ruang_Kabisatullah_2026.pdf",
        "pages_info": [
            {
                "pno": 5,
                "note": "A08: Antarmuka reservasi ruang dan kapasitas",
                "queries": [
                    "reservasi",
                    "antarmuka",
                    "kapasitas"
                ]
            },
            {
                "pno": 6,
                "note": "A08/A16: Constraint Capacity dan Constraint Satisfaction Problem",
                "queries": [
                    "Capacity",
                    "Constraint Satisfaction Problem",
                    "constraint"
                ]
            },
            {
                "pno": 7,
                "note": "A16: Validasi Constraint Satisfaction Problem",
                "queries": [
                    "Constraint Satisfaction Problem"
                ]
            }
        ]
    },
    {
        "id": "S09_A09_A15",
        "title": "Khafidhoh dkk. (2026)",
        "src_path": ROOT / "JURNAL" / "05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA" / "03_Penjadwalan_Bimbel_AHE_JTI_Khafidhoh_2026.pdf",
        "out_name": "STABILO_Penjadwalan_Bimbel_Khafidhoh_2026.pdf",
        "pages_info": [
            {
                "pno": 1,
                "note": "A09: Masalah uneven distribution of teaching assignments pada bimbel",
                "queries": [
                    "uneven distribution of teaching assignments",
                    "jadwal",
                    "AHE"
                ]
            },
            {
                "pno": 2,
                "note": "A09/A15: Sistem Penjadwalan algoritma genetika mengatasi konflik",
                "queries": [
                    "Sistem Penjadwalan",
                    "algoritma genetika",
                    "konflik"
                ]
            },
            {
                "pno": 5,
                "note": "A15: Hasil pengujian sistem penjadwalan",
                "queries": [
                    "Sistem Penjadwalan",
                    "pengujian",
                    "kesimpulan"
                ]
            }
        ]
    },
    {
        "id": "S10_A10",
        "title": "Gunawan dkk. (2025)",
        "src_path": ROOT / "JURNAL" / "02_STUDI_KASUS_BIMBEL_DAN_KURSUS" / "SI Bimbel RSDC - Web - Waterfall - RJTI - Gunawan dkk - 2025.pdf",
        "out_name": "STABILO_SI_Bimbel_RSDC_Gunawan_2025.pdf",
        "pages_info": [
            {
                "pno": 1,
                "note": "A10: Modul registrasi, penjadwalan, presensi dan verifikasi pembayaran",
                "queries": [
                    "penjadwalan",
                    "presensi",
                    "verifikasi pembayaran"
                ]
            },
            {
                "pno": 9,
                "note": "A10: Antarmuka verifikasi pembayaran bimbel",
                "queries": [
                    "verifikasi pembayaran",
                    "pembayaran"
                ]
            }
        ]
    },
    {
        "id": "S11_A12",
        "title": "Barizi dkk. (2023)",
        "src_path": ROOT / "JURNAL" / "02_STUDI_KASUS_BIMBEL_DAN_KURSUS" / "Aplikasi Administrasi Sekolah Musik ABC - Pembayaran & Penjadwalan - Barizi dkk - 2023.pdf",
        "out_name": "STABILO_Administrasi_Sekolah_Musik_Barizi_2023.pdf",
        "pages_info": [
            {
                "pno": 1,
                "note": "A12: Integrasi penjadwalan dan pembayaran kursus pada Sekolah Musik berbasis Java",
                "queries": [
                    "Sekolah Musik",
                    "Java",
                    "pembayaran",
                    "penjadwalan"
                ]
            },
            {
                "pno": 6,
                "note": "A12: Tampilan modul transaksi pembayaran dan jadwal",
                "queries": [
                    "jadwal",
                    "pembayaran",
                    "transaksi"
                ]
            },
            {
                "pno": 7,
                "note": "A12: Simpulan implementasi penjadwalan dan pembayaran kursus",
                "queries": [
                    "Java",
                    "penjadwalan",
                    "pembayaran"
                ]
            }
        ]
    },
    {
        "id": "S12_A13",
        "title": "Thiovanda (2026)",
        "src_path": ROOT / "JURNAL" / "02_STUDI_KASUS_BIMBEL_DAN_KURSUS" / "SI Penjadwalan & Pembayaran Les Jia Jia Education - Web - Thiovanda.pdf",
        "out_name": "STABILO_SI_Les_Jia_Jia_Thiovanda_2026.pdf",
        "pages_info": [
            {
                "pno": 1,
                "note": "A13: Sistem penjadwalan dan pembayaran les Jia Jia Education",
                "queries": [
                    "penjadwalan",
                    "pembayaran",
                    "Jia Jia Education"
                ]
            },
            {
                "pno": 4,
                "note": "A13: Fitur Cabang Management dan pembatasan akses admin",
                "queries": [
                    "Cabang Management",
                    "cabang",
                    "admin"
                ]
            },
            {
                "pno": 5,
                "note": "A13: Verifikasi bukti pembayaran les",
                "queries": [
                    "verifikasi pembayaran",
                    "bukti pembayaran",
                    "kesimpulan"
                ]
            }
        ]
    },
    {
        "id": "S13_A14",
        "title": "Safitri dkk. (2026)",
        "src_path": ROOT / "JURNAL" / "02_STUDI_KASUS_BIMBEL_DAN_KURSUS" / "SI Manajemen Bimbel Ilman Nafi - Notifikasi - Waterfall - Safitri dkk - 2026.pdf",
        "out_name": "STABILO_SI_Bimbel_Ilman_Nafi_Safitri_2026.pdf",
        "pages_info": [
            {
                "pno": 1,
                "note": "A14: Fitur notifikasi otomatis melalui WhatsApp untuk bimbel",
                "queries": [
                    "WhatsApp",
                    "notifikasi"
                ]
            },
            {
                "pno": 5,
                "note": "A14: Broadcast jadwal WhatsApp dan modul pembayaran",
                "queries": [
                    "WhatsApp",
                    "notifikasi",
                    "broadcast",
                    "pembayaran"
                ]
            },
            {
                "pno": 6,
                "note": "A14: Tabel 1 pengujian fungsional notifikasi WhatsApp",
                "queries": [
                    "WhatsApp",
                    "notifikasi",
                    "Tabel 1",
                    "logout"
                ]
            }
        ]
    },
    {
        "id": "S14_A19",
        "title": "Schwaber dan Sutherland (2020)",
        "src_path": ROOT / "JURNAL" / "01_FONDASI_DAN_KOMPARASI_METODOLOGI" / "Scrum Guide 2020 - Schwaber & Sutherland - Official.pdf",
        "out_name": "STABILO_Scrum_Guide_2020_Schwaber.pdf",
        "pages_info": [
            {
                "pno": 6,
                "note": "A19: Struktur Scrum Team dan akuntabilitas Developers, Product Owner, Scrum Master",
                "queries": [
                    "Scrum Team",
                    "Developers",
                    "Product Owner",
                    "Scrum Master"
                ]
            },
            {
                "pno": 10,
                "note": "A19: Daily Scrum (partisipasi PO/SM sebagai Developers jika mengerjakan backlog)",
                "queries": [
                    "Daily Scrum",
                    "Product Owner",
                    "Scrum Master",
                    "Developers"
                ]
            }
        ]
    },
    {
        "id": "S15_A20_A24",
        "title": "Sommerville (2011)",
        "src_path": ROOT / "JURNAL" / "BUKU" / "Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf",
        "out_name": "STABILO_Software_Engineering_Sommerville_2011.pdf",
        "pages_info": [
            {
                "pno": 62,
                "note": "A20: Prototyping process, Figure 2.9, dan Evaluation report",
                "queries": [
                    "Prototyping",
                    "Figure 2.9",
                    "Evaluation report"
                ]
            },
            {
                "pno": 63,
                "note": "A20: Throwaway prototype dan keterbatasan dokumentasi",
                "queries": [
                    "throwaway",
                    "prototype"
                ]
            },
            {
                "pno": 77,
                "note": "A24: Customer involvement pada metode Agile",
                "queries": [
                    "Customer involvement",
                    "Agile"
                ]
            },
            {
                "pno": 760,
                "note": "A24: Glosarium definisi rapid application development (RAD)",
                "queries": [
                    "rapid application development",
                    "RAD"
                ]
            }
        ]
    },
    {
        "id": "S16_A21",
        "title": "Beck dan Andres (2004)",
        "src_path": ROOT / "JURNAL" / "BUKU" / "Extreme-Programming-Explained-2nd-Edition-Kent-Beck.pdf",
        "out_name": "STABILO_Extreme_Programming_Explained_Beck_2004.pdf",
        "pages_info": [
            {
                "pno": 104,
                "note": "A21: Bab 7 Pair Programming (Write all production programs with two people)",
                "queries": [
                    "Pair Programming",
                    "Write all production programs with two people"
                ]
            }
        ]
    },
    {
        "id": "S17_A22",
        "title": "Agarwal dan Umphress (2008)",
        "src_path": ROOT / "JURNAL" / "01_FONDASI_DAN_KOMPARASI_METODOLOGI" / "Extreme programming for a single person team.pdf",
        "out_name": "STABILO_Extreme_Programming_Single_Person_Agarwal_2008.pdf",
        "is_scanned": True,
        "pages_info": [
            {
                "pno": 4,
                "note": "A22: Table 2 - On-site Customer: Perbandingan keterlibatan pelanggan XP vs PXP",
                "coord_rect": fitz.Rect(52, 230, 545, 328)
            }
        ]
    },
    {
        "id": "S18_A23",
        "title": "Mishra dan Alzoubi (2023)",
        "src_path": ROOT / "JURNAL" / "01_FONDASI_DAN_KOMPARASI_METODOLOGI" / "Structured vs Agile Development Comparative Analysis - Mishra & Alzoubi - Springer - 2023.pdf",
        "out_name": "STABILO_Structured_vs_Agile_Mishra_2023.pdf",
        "pages_info": [
            {
                "pno": 3,
                "note": "A23: Kajian kohesivitas tim (team cohesiveness) dalam Agile",
                "queries": [
                    "team cohesiveness"
                ]
            },
            {
                "pno": 4,
                "note": "A23: Tabel kajian terdahulu tentang kohesivitas tim",
                "queries": [
                    "team cohesiveness"
                ]
            },
            {
                "pno": 9,
                "note": "A23: Agile development frameworks & Extreme Programming (XP)",
                "queries": [
                    "Agile development frameworks",
                    "Extreme Programming"
                ]
            },
            {
                "pno": 12,
                "note": "A23: Tabel perbandingan keahlian (expertise) tim pengembangan",
                "queries": [
                    "expertise"
                ]
            }
        ]
    },
    {
        "id": "S19_A25",
        "title": "Pressman (2010)",
        "src_path": ROOT / "JURNAL" / "BUKU" / "ebook-pressman-sw-engineering.pdf",
        "out_name": "STABILO_Software_Engineering_Pressman_2010.pdf",
        "pages_info": [
            {
                "pno": 79,
                "note": "A25: 2.4.1 Component-Based Development",
                "queries": [
                    "Component-Based Development"
                ]
            },
            {
                "pno": 80,
                "note": "A25: Lanjutan Component-Based Development dan aspek reuse",
                "queries": [
                    "Component-Based Development",
                    "reuse"
                ]
            }
        ]
    },
    {
        "id": "S20_A26",
        "title": "Fikri dan Arthawan (2020)",
        "src_path": ROOT / "JURNAL" / "03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU" / "SI Buku Tamu DPOP Balikpapan - PxP - Fikri & Prabowo (ITK) - 2020.pdf",
        "out_name": "STABILO_SI_Buku_Tamu_DPOP_PxP_Fikri_2020.pdf",
        "pages_info": [
            {
                "pno": 3,
                "note": "A26: Tahapan Requirements dan Personal Extreme Programming (PxP)",
                "queries": [
                    "Requirements",
                    "Personal Extreme Programming"
                ]
            },
            {
                "pno": 4,
                "note": "A26: Alur Planning, Design, Implementation, dan System Testing",
                "queries": [
                    "Planning",
                    "Design",
                    "Implementation",
                    "System Testing"
                ]
            },
            {
                "pno": 5,
                "note": "A26: Evaluasi pengujian bersama klien pada iterasi",
                "queries": [
                    "klien"
                ]
            }
        ]
    },
    {
        "id": "S21_A27",
        "title": "Sidiq dkk. (2025)",
        "src_path": ROOT / "JURNAL" / "03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU" / "SI Surat Menyurat - Personal Extreme Programming (PxP) - Sidiq dkk - 2025.pdf",
        "out_name": "STABILO_SI_Surat_Menyurat_PxP_Sidiq_2025.pdf",
        "pages_info": [
            {
                "pno": 3,
                "note": "A27: Alasan pemilihan Personal Extreme Programming (PxP)",
                "queries": [
                    "Personal Extreme Programming",
                    "PxP"
                ]
            },
            {
                "pno": 4,
                "note": "A27: Fase Design, Implementation, System Testing, dan Retrospective",
                "queries": [
                    "Design",
                    "Implementation",
                    "System Testing",
                    "Retrospective"
                ]
            },
            {
                "pno": 11,
                "note": "A27: Simpulan waktu pengembangan (total 50 hari, implementasi 37 hari)",
                "queries": [
                    "50 hari",
                    "37 hari",
                    "pengujian"
                ]
            }
        ]
    }
]

def main():
    print("=" * 70)
    print("MEMPROSES PENANDAAN STABILO KUNING PADA 22 SUMBER RUJUKAN BAB 1")
    print("=" * 70)
    
    summary = []
    
    for cfg in CONFIG:
        t0 = time.time()
        src_file = cfg["src_path"]
        out_file = OUT_DIR / cfg["out_name"]
        
        if not src_file.exists():
            print(f"ERROR: File sumber tidak ditemukan: {src_file}")
            continue
            
        doc = fitz.open(src_file)
        total_highlights = 0
        
        for pinfo in cfg["pages_info"]:
            pno = pinfo["pno"] - 1 # 0-indexed
            if pno >= len(doc):
                print(f"  Warning: Halaman {pinfo['pno']} di luar jangkauan {len(doc)} hal")
                continue
                
            page = doc[pno]
            note = pinfo.get("note", "")
            
            # Khusus PDF pindai gambar (Agarwal)
            if pinfo.get("coord_rect"):
                r = pinfo["coord_rect"]
                annot = page.add_highlight_annot(r)
                annot.set_colors(stroke=[1, 1, 0]) # Kuning cerah
                annot.set_info(content=note)
                annot.update()
                total_highlights += 1
            else:
                # Digital text search
                for q in pinfo.get("queries", []):
                    quads = page.search_for(q)
                    for qd in quads:
                        annot = page.add_highlight_annot(qd)
                        annot.set_colors(stroke=[1, 1, 0]) # Kuning cerah
                        annot.set_info(content=note)
                        annot.update()
                        total_highlights += 1
                        
        doc.save(out_file, garbage=1, deflate=True)
        doc.close()
        t1 = time.time()
        
        file_size_mb = out_file.stat().st_size / (1024 * 1024)
        print(f"[{cfg['id']}] {cfg['out_name']} -> {total_highlights} penanda stabilo dibuat ({t1-t0:.2f}s, {file_size_mb:.2f} MB)")
        summary.append({
            "id": cfg["id"],
            "title": cfg["title"],
            "file": str(out_file),
            "filename": cfg["out_name"],
            "highlights": total_highlights,
            "size_mb": round(file_size_mb, 2)
        })
        
    # Simpan laporan manifest json
    manifest_path = OUT_DIR / "MANIFEST_PDF_TERSTABILO.json"
    manifest_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nManifest berhasil disimpan di: {manifest_path}")
    print(f"Selesai! Seluruh {len(summary)} dokumen PDF telah berhasil distabilo.")

if __name__ == "__main__":
    main()
