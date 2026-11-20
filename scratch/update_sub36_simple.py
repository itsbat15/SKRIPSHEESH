import re

# Text for 3.6_Jadwal_Pembuatan_Prototipe.md matching the user's simple reference
new_sub36 = """# 3.6 Jadwal Pembuatan Prototipe

Rencana jadwal pembuatan prototipe disusun secara menyeluruh untuk memandu pelaksanaan Tugas Akhir agar berlangsung secara sistematis, terukur, dan selesai tepat waktu. Jadwal pengerjaan dirancang mengadopsi tahapan siklus hidup metodologi *Personal Extreme Programming* (PxP) yang dipadukan dengan kalender akademik pelaksanaan Tugas Akhir di Program Studi Sistem Informasi ITK. Rentang waktu pengerjaan terbagi ke dalam dua periode semester pelaksanaan, yaitu periode semester ganjil untuk fase persiapan naskah proposal dan periode semester genap untuk fase konstruksi prototipe hingga evaluasi akhir.

Rangkaian aktivitas pembuatan prototipe mencakup dua belas tahapan kegiatan utama yang tersusun secara berkesinambungan:
1. **Mengidentifikasi Masalah**: Dilaksanakan pada bulan September minggu pertama hingga keempat guna menggali persoalan pencatatan manual dan inefisiensi kasir cabang di Bimbel ARTHA.
2. **Studi Literatur**: Dilaksanakan secara berkelanjutan mulai bulan September minggu ketiga hingga bulan Desember minggu keempat guna menghimpun teori pendukung dan penelitian terdahulu.
3. **Requirements**: Dilaksanakan pada bulan Oktober minggu pertama hingga bulan Desember minggu keempat guna mengumpulkan data kebutuhan, menyusun cerita pengguna (*User Stories*), dan memodelkan proses bisnis BPMN As-Is serta To-Be.
4. **Planning**: Dilaksanakan pada bulan November minggu pertama hingga bulan Desember minggu keempat untuk melakukan estimasi bobot tugas dengan skala Fibonacci, penyusunan arsitektur sistem, dan perancangan skema basis data ERD.
5. **Iteration Initialization**: Dilaksanakan pada bulan April minggu pertama hingga bulan Mei minggu keempat untuk mempersiapkan repositori kode program, inisialisasi lingkungan Next.js dan Laravel, serta penyiapan skema tabel MySQL.
6. **Design**: Dilaksanakan pada bulan April minggu pertama hingga bulan Mei minggu keempat untuk merancang antarmuka kawat (*wireframe*), spesifikasi interaksi sistem, dan struktur komponen visual Tailwind CSS.
7. **Implementation**: Dilaksanakan pada bulan April minggu pertama hingga bulan Mei minggu keempat untuk menuliskan kode program antarmuka web kasir cabang, layanan RESTful API, dan logika validasi transfer bank.
8. **System Testing**: Dilaksanakan berdampingan dengan fase implementasi pada bulan April minggu pertama hingga bulan Mei minggu keempat melalui pengujian unit dan pengujian fungsional *Black Box Testing*.
9. **Retrospective**: Dilaksanakan pada setiap akhir siklus pengerjaan fitur pada bulan April minggu pertama hingga bulan Mei minggu keempat guna mengevaluasi ketercapaian fungsionalitas bersama perwakilan mitra.
10. **Deployment**: Dilaksanakan pada bulan Mei minggu keempat hingga bulan Juni minggu pertama untuk menyebarkan aplikasi ke peladen awan VPS Ubuntu dan platform Vercel agar dapat diakses oleh delapan kantor cabang.
11. **User Training**: Dilaksanakan pada bulan Mei minggu keempat hingga bulan Juni minggu pertama untuk melatih Staf Administrasi Cabang dan Pemilik Lembaga dalam mengoperasikan modul kasir dan dasbor konsolidasi.
12. **Kesimpulan dan Saran**: Dilaksanakan pada bulan Juni minggu pertama untuk menyusun evaluasi akhir ketercapaian prototipe, merumuskan saran pengembangan, dan memfinalisasi naskah laporan Tugas Akhir.

Matriks jadwal pelaksanaan pembuatan prototipe disajikan secara ringkas pada Tabel 3.14. Arsiran blok warna ungu merepresentasikan kegiatan perancangan pada semester ganjil, sedangkan arsiran blok warna toska merepresentasikan kegiatan konstruksi, penyebaran, dan pelatihan operasional pada semester genap.

**Tabel 3.14 Rencana Jadwal Pembuatan Prototipe PxP**

| Kegiatan | Sep (1-4) | Okt (1-4) | Nov (1-4) | Des (1-4) | April (1-4) | Mei (1-4) | Juni (1) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mengidentifikasi Masalah | [X] . . . | . . . . | . . . . | . . . . | . . . . | . . . . | . |
| Studi Literatur | . . [X] [X] | [X] [X] [X] [X] | [X] [X] [X] [X] | [X] [X] [X] [X] | . . . . | . . . . | . |
| *Requirements* | . . . . | [X] [X] [X] [X] | [X] [X] [X] [X] | [X] [X] [X] [X] | . . . . | . . . . | . |
| *Planning* | . . . . | . . . . | [X] [X] [X] [X] | [X] [X] [X] [X] | . . . . | . . . . | . |
| *Iteration Initialization* | . . . . | . . . . | . . . . | . . . . | [X] [X] [X] [X] | [X] [X] [X] [O] | . |
| *Design* | . . . . | . . . . | . . . . | . . . . | [X] [X] [X] [X] | [X] [O] [O] [O] | . |
| *Implementation* | . . . . | . . . . | . . . . | . . . . | [X] [X] [X] [X] | [X] [X] [X] [O] | . |
| *System Testing* | . . . . | . . . . | . . . . | . . . . | [X] [X] [X] [X] | [X] [X] [X] [O] | . |
| *Retrospective* | . . . . | . . . . | . . . . | . . . . | [X] [X] [X] [X] | [X] [X] [X] [O] | . |
| *Deployment* | . . . . | . . . . | . . . . | . . . . | . . . . | . . . [O] | [O] |
| *User Training* | . . . . | . . . . | . . . . | . . . . | . . . . | . . . [O] | [O] |
| Kesimpulan dan Saran | . . . . | . . . . | . . . . | . . . . | . . . . | . . . . | [O] |

Keterangan simbol matriks jadwal:
Tanda `[X]` merepresentasikan pelaksanaan kegiatan perancangan pada periode semester pertama, sedangkan tanda `[O]` merepresentasikan pelaksanaan kegiatan implementasi, pengujian sistem, penyebaran, serta pelatihan pengguna pada periode semester kedua. Format matriks jadwal lengkap dengan arsiran blok warna dapat disalin secara langsung melalui berkas spreadsheet resmi yang telah disediakan.
"""

with open(r'DRAFT PROPOSAL MD\BAB 3\3.6_Jadwal_Pembuatan_Prototipe.md', 'w', encoding='utf-8') as f:
    f.write(new_sub36)

# Update master BAB_3_DESAIN_DAN_IMPLEMENTASI.md
master_path = r'DRAFT PROPOSAL MD\BAB 3\BAB_3_DESAIN_DAN_IMPLEMENTASI.md'
with open(master_path, 'r', encoding='utf-8') as f:
    master_text = f.read()

# Replace section 3.6 in master
sub36_heading = "## 3.6 Jadwal Pembuatan Prototipe"
if sub36_heading in master_text:
    idx = master_text.find(sub36_heading)
    updated_master = master_text[:idx].rstrip() + "\n\n" + new_sub36[2:] # strip leading '# '
    with open(master_path, 'w', encoding='utf-8') as f:
        f.write(updated_master)
    print("Master BAB 3 updated successfully with simplified schedule!")
else:
    print("Heading 3.6 not found in master, check text.")

