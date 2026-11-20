# PANDUAN AKADEMIK KOMPARASI METODE SDLC DAN JUSTIFIKASI PEMILIHAN PERSONAL EXTREME PROGRAMMING (PxP)

## Dokumen Argumen dan Pembuktian Komparatif untuk Bimbingan Skripsi Sistem Informasi ITK

Dokumen ini disusun sebagai rujukan argumentasi akademik yang komprehensif guna menghadapi proses bimbingan dan pertanggungjawaban metodologi Tugas Akhir di hadapan Dosen Pembimbing (Ibu Ayu). Seluruh isi dokumen ini disintesis secara eksklusif berlandaskan literatur primer yang tersimpan pada repositori pustaka penelitian skripsi, yang mencakup buku teks standar rekayasa perangkat lunak serta artikel jurnal ilmiah bereputasi. Fokus utama dari naskah ini adalah menyajikan perbandingan objektif antara delapan metode pengembangan perangkat lunak utama, memetakan tahapan baku masing-masing metode yang disertai tangkapan layar alur asli dari naskah primer, membedah kekuatan serta kelemahannya, dan merumuskan justifikasi ilmiah mengapa Personal Extreme Programming (PxP) merupakan satu-satunya metode yang paling tepat, layak, dan terukur untuk merancang prototipe sistem informasi manajemen operasional terintegrasi pada Bimbingan Belajar Artha Balikpapan.

---

## 1. LANDASAN PUSTAKA DAN BATASAN SUMBER RUJUKAN

Penyusunan telaah komparatif ini merujuk secara ketat pada literatur akademik yang telah diverifikasi validitasnya dalam repositori riset. Setiap dokumen dapat diakses secara langsung melalui tautan berkas PDF primer maupun berkas teks hasil ekstraksi lokal:

1. **Buku Rujukan Rekayasa Perangkat Lunak:**
   - Sommerville, I. (2011). _Software Engineering (9th Edition)_. Boston: Addison-Wesley. (Bab 2 mengenai _Software Processes_, hlm. 28 hingga 55; Bab 3 mengenai _Agile Software Development_, hlm. 56 hingga 88)<br>
     ↳ <a href="./JURNAL/BUKU/Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/HASIL%20EKSTRAK%20BUKU/Software-Engineering-9th-Edition-by-Ian-Sommerville.txt">📝 Buka Teks Ekstraksi</a>
   - Beck, K., & Andres, C. (2004). _Extreme Programming Explained: Embrace Change (2nd Edition)_. Boston: Addison-Wesley. (hlm. 13 hingga 64)<br>
     ↳ <a href="./JURNAL/BUKU/Extreme-Programming-Explained-2nd-Edition-Kent-Beck.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/HASIL%20EKSTRAK%20BUKU/Extreme-Programming-Explained-2nd-Edition-Kent-Beck.txt">📝 Buka Teks Ekstraksi</a>
   - Pressman, R. S. (2010). _Software Engineering: A Practitioner's Approach (7th Edition)_. New York: McGraw-Hill. (Bab 2 mengenai _Process Models_, hlm. 30 hingga 60)<br>
     ↳ <a href="./JURNAL/BUKU/ebook-pressman-sw-engineering.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/HASIL%20EKSTRAK%20BUKU/ebook-pressman-sw-engineering.txt">📝 Buka Teks Ekstraksi</a>

2. **Panduan Resmi Standar Industri:**
   - Coleman, T., & Vacanti, D. S. (2025). _The Kanban Guide_. KanbanGuides.org. (hlm. 1 hingga 6)<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/The%20Kanban%20Guide%20-%20Panduan%20Resmi%20Kanban%20-%20Coleman%20&%20Vacanti%20-%202025.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/The%20Kanban%20Guide%20-%20Panduan%20Resmi%20Kanban%20-%20Coleman%20&%20Vacanti%20-%202025.txt">📝 Buka Teks Ekstraksi</a>
   - Schwaber, K., & Sutherland, J. (2020). _The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game_. Scrum.org. (hlm. 1 hingga 13)<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Scrum%20Guide%202020%20-%20Schwaber%20&%20Sutherland%20-%20Official.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Scrum%20Guide%202020%20-%20Schwaber%20&%20Sutherland%20-%20Official.txt">📝 Buka Teks Ekstraksi</a>
   - Poppendieck, M., & Poppendieck, T. (2003). _Lean Software Development: An Agile Toolkit_. Boston: Addison-Wesley. (hlm. xxiii hingga xxvii, 1 hingga 10, PDF hlm. 26 hingga 29)<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Lean%20Software%20Development%20-%20An%20Agile%20Toolkit%20-%20Poppendieck%20-%202003.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Lean%20Software%20Development%20-%20An%20Agile%20Toolkit%20-%20Poppendieck%20-%202003.txt">📝 Buka Teks Ekstraksi</a>

3. **Artikel Jurnal Fondasi Konseptual dan Komparasi Metodologi:**
   - Royce, W. W. (1970). _Managing the Development of Large Software Systems_. Proceedings of IEEE WESCON, 26, hlm. 1 hingga 9<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Managing%20the%20Development%20of%20Large%20Software%20Systems%20-%20Waterfall%20-%20WESCON%20-%20Royce%20-%201970.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Managing%20the%20Development%20of%20Large%20Software%20Systems%20-%20Waterfall%20-%20WESCON%20-%20Royce%20-%201970.txt">📝 Buka Teks Ekstraksi</a>
   - Boehm, B. W. (1988). _A Spiral Model of Software Development and Enhancement_. Computer, 21(5), hlm. 61 hingga 72<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/A%20Spiral%20Model%20of%20Software%20Development%20and%20Enhancement%20-%20Prototyping%20-%20Boehm%20-%201988.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/A%20Spiral%20Model%20of%20Software%20Development%20and%20Enhancement%20-%20Prototyping%20-%20Boehm%20-%201988.txt">📝 Buka Teks Ekstraksi</a>
   - Schwaber, K. (1995). _SCRUM Development Process_. Proceedings of OOPSLA 1995, hlm. 1 hingga 10<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/SCRUM%20Development%20Process%20-%20OOPSLA%20-%20Schwaber%20-%201995.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SCRUM%20Development%20Process%20-%20OOPSLA%20-%20Schwaber%20-%201995.txt">📝 Buka Teks Ekstraksi</a>
   - Williams, L., Kessler, R. R., Cunningham, W., & Jeffries, R. (2000). _Strengthening the Case for Pair Programming_. IEEE Software, 17(4), hlm. 19 hingga 25<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Strengthening%20the%20Case%20for%20Pair%20Programming%20-%20IEEE%20Software%20-%20Williams%20dkk%20-%202000.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Strengthening%20the%20Case%20for%20Pair%20Programming%20-%20IEEE%20Software%20-%20Williams%20dkk%20-%202000.txt">📝 Buka Teks Ekstraksi</a>
   - Dzhurov, Y., Krasteva, I., & Ilieva, S. (2009). _Personal Extreme Programming: An Agile Process for Autonomous Developers_. Proceedings of S3T 2009, hlm. 252 hingga 259<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Personal%20Extreme%20Programming%20-%20Agile%20for%20Autonomous%20Developer%20-%20S3T%202009%20-%20Dzhurov%20dkk%20-%202009.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Personal%20Extreme%20Programming%20-%20Agile%20for%20Autonomous%20Developer%20-%20S3T%202009%20-%20Dzhurov%20dkk%20-%202009.txt">📝 Buka Teks Ekstraksi</a>
   - Agarwal, R., & Umphress, D. (2008). _Extreme Programming for a Single Person Team_. Proceedings of ACM-SE 46, hlm. 82 hingga 87. Berkas Ekstraksi: [Extreme programming for a single person team - Agarwal & Umphress - 2008.txt](./JURNAL/HASIL%20EKSTRAK%20JURNAL/Extreme%20programming%20for%20a%20single%20person%20team%20-%20Agarwal%20&%20Umphress%20-%202008.txt).
   - Khan, T. U. R., Rehman, S. U., & Ahmad, F. (2011). _A Comparative Study of Heavyweight and Lightweight Software Methodologies_. IJCSNS, 11(8), hlm. 94 hingga 100<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Perbandingan%20Heavy%20&%20Lightweight%20Methodology%20-%20Khan%20dkk%20-%202011.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Perbandingan%20Heavy%20&%20Lightweight%20Methodology%20-%20Khan%20dkk%20-%202011.txt">📝 Buka Teks Ekstraksi</a>
   - Mishra, A., & Alzoubi, Y. I. (2023). _Structured versus Agile Software Development: A Comparative Analysis of Key Features_. Software Quality Journal, 31, hlm. 881 hingga 923<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Structured%20vs%20Agile%20Development%20Comparative%20Analysis%20-%20Mishra%20&%20Alzoubi%20-%20Springer%20-%202023.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Structured%20vs%20Agile%20Development%20Comparative%20Analysis%20-%20Mishra%20&%20Alzoubi%20-%20Springer%20-%202023.txt">📝 Buka Teks Ekstraksi</a>
   - Kuhrmann, M., dkk. (2021). _What Makes Agile Software Development Agile?_. Empirical Software Engineering, 26(6), hlm. 1 hingga 46<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Adoption%20and%20Suitability%20of%20Software%20Development%20Methods%20-%20Empirical%20Study%20-%20Kuhrmann%20dkk%20-%202021.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Adoption%20and%20Suitability%20of%20Software%20Development%20Methods%20-%20Empirical%20Study%20-%20Kuhrmann%20dkk%20-%202021.txt">📝 Buka Teks Ekstraksi</a>

4. **Artikel Jurnal Implementasi Komparatif dan Empiris PxP:**
   - Susanto, R., & Andriana, A. D. (2016). _Perbandingan Model Waterfall dan Prototyping untuk Pengembangan Sistem Informasi_. Majalah Ilmiah UNIKOM, 14(1), hlm. 41 hingga 46<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Perbandingan%20Waterfall%20dan%20Prototyping%20-%20UNIKOM%20-%20Susanto%20&%20Andriana%20-%202016.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Perbandingan%20Waterfall%20dan%20Prototyping%20-%20UNIKOM%20-%20Susanto%20&%20Andriana%20-%202016.txt">📝 Buka Teks Ekstraksi</a>
   - Pratama, B. C., Hidayat, T., & Nurfaizah. (2023). _Penerapan Metode Rapid Application Development (RAD) pada Sistem Informasi Inventarisasi Aset Desa Rempoah_. Jurnal Infotek, 6(1), hlm. 49 hingga 59<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Penerapan%20Metode%20RAD%20-%20Infotek%20-%20Pratama%20dkk%20-%202023.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Inventaris%20Aset%20Desa%20-%20RAD%20-%20Pratama%20dkk%20-%202023.txt">📝 Buka Teks Ekstraksi</a>
   - Putra, F. K. (2022). _Sistem Informasi Presensi Pegawai Berbasis Web Menggunakan Metode Prototyping_. Journal of Information System Research (JOSH), 3(4), hlm. 431 hingga 436<br>
     ↳ <a href="./JURNAL/04_FITUR_DAN_TEKNOLOGI_PENDUKUNG/SI%20Absensi%20-%20Web%20-%20Prototyping%20-%20Putra%20-%202022.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Absensi%20-%20Web%20-%20Prototyping%20-%20Putra%20-%202022.txt">📝 Buka Teks Ekstraksi</a>
   - Asri, M., Fajri, R., & Syahrul. (2018). _PxP vs Waterfall: Web-Based Application for Job Training Activities Using Personal Extreme Programming (PXP)_. Proceedings of ICST 2018, hlm. 284 hingga 288<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/PxP%20vs%20Waterfall%20-%20Job%20Training%20App%20-%20ICST%202018%20-%20Asri%20dkk%20-%202018.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/PxP%20vs%20Waterfall%20-%20Job%20Training%20App%20-%20ICST%202018%20-%20Asri%20dkk%20-%202018.txt">📝 Buka Teks Ekstraksi</a>
   - Fikri, M. R., & Prabowo, R. D. A. (2020). _Rancang Bangun Sistem Informasi Buku Tamu DPOP Balikpapan dengan Metode Personal Extreme Programming_. Jurnal Sistem Informasi ITK, hlm. 1 hingga 11<br>
     ↳ <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Buku%20Tamu%20DPOP%20Balikpapan%20-%20PxP%20-%20Fikri%20&%20Prabowo%20(ITK)%20-%202020.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Buku%20Tamu%20DPOP%20Balikpapan%20-%20PxP%20-%20Fikri%20&%20Prabowo%20(ITK)%20-%202020.txt">📝 Buka Teks Ekstraksi</a>
   - Priatmaja, B., Prabowo, R. D. A., & Ginanjar. (2022). _Pengembangan Sistem Informasi Laboratorium Infokom Menggunakan Personal Extreme Programming_. REPOSITOR, 4(1), hlm. 1 hingga 10<br>
     ↳ <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Laboratorium%20Infokom%20-%20PxP%20-%20REPOSITOR%20-%20Priatmaja%20dkk%20-%202022.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Laboratorium%20Infokom%20-%20PxP%20-%20REPOSITOR%20-%20Priatmaja%20dkk%20-%202022.txt">📝 Buka Teks Ekstraksi</a>
   - Hasan, H. I., Marthasari, G. I., & Nuryasin, I. (2021). Implementasi Metode Personal Extreme Programming Dalam Pengembangan Sistem Administrasi Pelayanan Desa. REPOSITOR, 3(1), hlm. 43-50.
     ↳ <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Surat%20Menyurat%20-%20Personal%20Extreme%20Programming%20(PxP)%20-%20Hasan, H. I., Marthasari, G. I., & Nuryasin, I. (2021). Implementasi Metode Personal Extreme Programming Dalam Pengembangan Sistem Administrasi Pelayanan Desa. REPOSITOR, 3(1), hlm. 43-50.
   - Ramadhan, M. R. (2026). _Sistem Informasi Keanggotaan dan Penjadwalan Menggunakan Metode PxP_. Jurnal Riset Sistem Informasi, 8(1), hlm. 88 hingga 99<br>
     ↳ <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Keanggotaan%20&%20Jadwal%20-%20PxP%20-%20Ramadhan%20-%202026.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Keanggotaan%20&%20Jadwal%20-%20PxP%20-%20Ramadhan%20-%202026.txt">📝 Buka Teks Ekstraksi</a>
   - Fahrijal, M., & Hartawan, M. B. (2024). _Perbandingan XP vs PxP pada Implementasi Software_. Jurnal Ilmiah Sistem Informasi, 6(2), hlm. 154 hingga 162<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Perbandingan%20XP%20vs%20PxP%20pada%20Implementasi%20Software%20-%20Fahrijal%20&%20Hartawan%20-%202024.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Perbandingan%20XP%20vs%20PxP%20pada%20Implementasi%20Software%20-%20Fahrijal%20&%20Hartawan%20-%202024.txt">📝 Buka Teks Ekstraksi</a>
   - Suputra, I. G. A., dkk. (2026). _Sistem Informasi Siswa SMP Berbasis Extreme Programming_. Jurnal Teknologi Informasi, 10(1), hlm. 75 hingga 84<br>
     ↳ <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Siswa%20SMP%20-%20Extreme%20Programming%20(XP)%20-%20Suputra%20dkk%20-%202026.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Siswa%20SMP%20-%20Extreme%20Programming%20(XP)%20-%20Suputra%20dkk%20-%202026.txt">📝 Buka Teks Ekstraksi</a>
   - Mahnic, B. (2018). _Scrum2Kanban: Integrating Kanban and Scrum in a Software Engineering Capstone Course_. IEEE Transactions on Education, 61(2), hlm. 126 hingga 133 (PDF hlm. 13 hingga 20)<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Scrum2Kanban%20-%20Integrating%20Kanban%20and%20Scrum%20in%20Capstone%20Course%20-%20IEEE%20-%20Mahnic%20-%202018.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Scrum2Kanban%20-%20Integrating%20Kanban%20and%20Scrum%20in%20Capstone%20Course%20-%20IEEE%20-%20Mahnic%20-%202018.txt">📝 Buka Teks Ekstraksi</a>
   - Kurniawan, D., & Sani, R. R. (2019). _Pemodelan SCRUM Sistem Informasi Pelayanan Kesehatan Klinik Gigi Ar-Rokhim Semarang_. JOINS, 4(2), hlm. 146 hingga 156<br>
     ↳ <a href="./JURNAL/04_FITUR_DAN_TEKNOLOGI_PENDUKUNG/Pemodelan%20SCRUM%20Klinik%20Ar-Rokhim%20-%20JOINS%20-%20Kurniawan%20&%20Sani%20-%202019.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Pemodelan%20SCRUM%20Klinik%20Ar-Rokhim%20-%20JOINS%20-%20Kurniawan%20&%20Sani%20-%202019.txt">📝 Buka Teks Ekstraksi</a>

---

## 2. TELAAH MENDALAM DELAPAN METODE PENGEMBANGAN PERANGKAT LUNAK BESERTA BUKTI DIAGRAM ALUR

Bagian ini menguraikan setiap metode secara berimbang berdasarkan literatur primer yang sah. Setiap telaah menyajikan definisi formal, bukti tangkapan layar alur proses asli yang di-ekstrak langsung dari dokumen sumber, perincian tahapan baku proses, karakteristik operasional, keunggulan, kelemahan, serta evaluasi kritis terhadap kesesuaian penerapannya pada studi kasus Bimbingan Belajar Artha Balikpapan.

```
                      KLASIFIKASI METODOLOGI SDLC
                                   |
         +-------------------------+-------------------------+
         |                                                   |
   [PLAN-DRIVEN]                                          [AGILE]
   - Waterfall (Royce 1970;                              - Scrum (Schwaber 1995;
     Sommerville 2011)                                     Kurniawan 2019)
   - Prototyping (Sommerville 2011;                      - Extreme Programming (Beck 2004;
     Susanto 2016)                                         Suputra 2026)
   - RAD (Pratama 2023)                                  - Kanban (Coleman 2025; Mahnic 2018)
   - Spiral (Boehm 1988;                                 - Lean Software (Poppendieck 2003)
     Sommerville 2011)                                   - Personal Extreme Programming
                                                           (Dzhurov 2009; Fikri ITK 2020)
```

---

### 2.1 Model Waterfall

#### A. Definisi dan Filosofi Dasar

Model Waterfall merupakan paradigma pengembangan perangkat lunak sekuensial linear klasik yang pertama kali dirumuskan oleh Winston W. Royce pada tahun 1970 (hlm. 1 hingga 2) dan dikodifikasikan dalam literatur rekayasa perangkat lunak oleh Ian Sommerville (2011, hlm. 30 hingga 33). Pendekatan ini menuntut setiap tahapan proses diselesaikan secara paripurna dan diverifikasi melalui dokumentasi formal sebelum tahapan berikutnya dimulai. Paradigma ini bertumpu pada asumsi bahwa seluruh kebutuhan sistem informasi dapat diidentifikasi secara menyeluruh sejak awal proyek tanpa mengalami perubahan signifikan di kemudian hari.

#### B. Tangkapan Layar Diagram Alur Proses dari Literatur Sumber

Berikut merupakan bukti diagram alur proses Waterfall yang diambil langsung dari dokumen primer penemu aslinya (Royce, 1970, hlm. 2, Figure 2) dan elaborasi jurnal komparasi nasional (Susanto & Andriana, 2016, hlm. 331, Gambar 1):

<p align="center">
  <img src="./gambar_metode/01_waterfall_royce_1970.png" alt="Alur Tahapan Model Waterfall Klasik" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.1</b> Alur Tahapan Model Waterfall Klasik (Sumber: Royce, 1970, hlm. 2, Figure 2)</em>
  <br>
  <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Managing%20the%20Development%20of%20Large%20Software%20Systems%20-%20Waterfall%20-%20WESCON%20-%20Royce%20-%201970.pdf#page=2">📄 Buka Naskah PDF Sumber (hlm. 2)</a>
</p>

<p align="center">
  <img src="./gambar_metode/01b_waterfall_susanto_2016.png" alt="Alur Tahapan Model Waterfall Berurutan" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.1b</b> Alur Tahapan Model Waterfall Berurutan (Sumber: Susanto & Andriana, 2016, hlm. 331, Gambar 1)</em>
  <br>
  <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Perbandingan%20Waterfall%20dan%20Prototyping%20-%20UNIKOM%20-%20Susanto%20&%20Andriana%20-%202016.pdf#page=3">📄 Buka Naskah PDF Sumber (hlm. 3)</a>
</p>

#### C. Tahapan Baku Proses

Berdasarkan dokumentasi Ian Sommerville (2011, hlm. 30 hingga 31) serta kodifikasi Royce (1970, hlm. 2), model Waterfall terdiri atas lima tahapan terstruktur yang berjalan berurutan:

1. **Requirements definition (Definisi Kebutuhan, Sommerville, 2011, hlm. 30):** Konsultasi intensif dengan pengguna sistem untuk menetapkan layanan, batasan, serta tujuan sistem secara mendalam. Hasil analisis ini kemudian dituangkan ke dalam dokumen spesifikasi kebutuhan sistem formal yang bersifat mengikat.
2. **System and software design (Perancangan Sistem dan Perangkat Lunak, Sommerville, 2011, hlm. 31):** Proses alokasi kebutuhan terhadap struktur arsitektur sistem perangkat keras maupun perangkat lunak. Tahap ini menghasilkan representasi abstrak antarmuka, perancangan skema basis data, dan arsitektur modul sistem secara keseluruhan.
3. **Implementation and unit testing (Implementasi dan Pengujian Unit, Sommerville, 2011, hlm. 31):** Penerjemahan rancangan perangkat lunak ke dalam sekumpulan modul program atau kode sumber. Setiap unit program diuji secara individual untuk memastikan kebenaran fungsi logisnya.
4. **Integration and system testing (Integrasi dan Pengujian Sistem, Sommerville, 2011, hlm. 31):** Penggabungan seluruh unit program individu menjadi satu kesatuan sistem perangkat lunak yang utuh. Pengujian dilakukan secara menyeluruh terhadap lingkungan sistem gabungan guna memverifikasi pemenuhan spesifikasi awal sebelum diserahkan kepada pihak pengguna.
5. **Operation and maintenance (Operasi dan Pemeliharaan, Sommerville, 2011, hlm. 31):** Pemasangan sistem pada lingkungan operasional nyata serta perbaikan galat yang baru terdeteksi setelah sistem digunakan. Tahap ini juga mencakup adaptasi fungsionalitas sistem terhadap dinamika lingkungan baru.

#### D. Kelebihan

- Struktur alur kerja sangat jelas, teratur, dan mudah dipahami oleh seluruh pemangku kepentingan (Khan, Rehman, & Ahmad, 2011, hlm. 95).
- Penjadwalan proyek, alokasi anggaran, dan tonggak capaian (_milestone_) dapat ditentukan dengan pasti sejak awal karena didukung oleh artefak dokumen formal pada setiap akhir fase (Mishra & Alzoubi, 2023, hlm. 885).
- Sangat efektif diterapkan pada proyek berskala besar yang memiliki spesifikasi kebutuhan statis, persyaratan keamanan ketat, serta tim pengembang yang besar dan terspesialisasi (Sommerville, 2011, hlm. 32).

#### E. Kelemahan

- Tingkat fleksibilitas sangat rendah terhadap perubahan kebutuhan yang muncul di tengah jalan, di mana perubahan spesifikasi membutuhkan biaya revisi yang sangat mahal (Mishra & Alzoubi, 2023, hlm. 886).
- Perangkat lunak yang dapat dieksekusi (_working software_) baru terwujud pada fase akhir daur hidup proyek, sehingga meningkatkan risiko keterlambatan deteksi kesalahan analisis (Susanto & Andriana, 2016, hlm. 333).
- Pengguna tidak memiliki visibilitas interaktif terhadap sistem hingga tahap implementasi selesai, yang kerap memicu kesenjangan harapan antara pengguna dan pengembang sistem (Royce, 1970, hlm. 3).

#### F. Evaluasi Kesesuaian Kasus Bimbel Artha

Penerapan Waterfall pada Bimbel Artha sangat tidak realistis. Operasional Bimbel Artha mencakup delapan cabang dengan pola administrasi yang saat ini masih bervariasi dan belum terstandarisasi penuh dalam dokumen formal. Apabila peneliti memaksakan penguncian kebutuhan di awal melalui pendekatan Waterfall, sistem akan gagal mengantisipasi kebutuhan operasional nyata di lapangan yang baru terungkap setelah modul diuji oleh pihak pengelola. Ketidakfleksibelan ini berisiko menghasilkan sistem yang tidak relevan dengan kebutuhan manajerial mitra.

---

### 2.2 Model Prototyping

#### A. Definisi dan Filosofi Dasar

Model Prototyping dirancang sebagai strategi elisitasi kebutuhan yang berpusat pada pembuatan representasi awal sistem yang cepat guna menjembatani kesenjangan pemahaman antara pengguna dan pengembang (Sommerville, 2011, hlm. 43 hingga 45). Menurut Susanto & Andriana (2016, hlm. 332), pendekatan ini sangat ideal untuk perangkat lunak yang bersifat kustom (_customized software_), di mana pengguna memiliki gagasan umum mengenai fungsi yang diinginkan namun belum mampu mendefinisikan rincian masukan, proses, serta keluaran secara teknis. Prototipe bertindak sebagai media eksperimentasi yang dievaluasi secara iteratif oleh pengguna.

#### B. Tangkapan Layar Diagram Alur Proses dari Literatur Sumber

Berikut merupakan bukti diagram alur proses Prototyping yang di-ekstrak langsung dari artikel komparasi Susanto & Andriana (2016, hlm. 332, Gambar 2):

<p align="center">
  <img src="./gambar_metode/02_prototyping_susanto_2016.png" alt="Alur Tahapan Model Prototyping" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.2</b> Alur Tahapan Model Prototyping (Sumber: Susanto & Andriana, 2016, hlm. 332, Gambar 2)</em>
  <br>
  <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Perbandingan%20Waterfall%20dan%20Prototyping%20-%20UNIKOM%20-%20Susanto%20&%20Andriana%20-%202016.pdf#page=3">📄 Buka Naskah PDF Sumber (hlm. 3)</a>
</p>

#### C. Tahapan Baku Proses

Mengacu pada kodifikasi Susanto & Andriana (2016, hlm. 332) serta rujukan Ian Sommerville (2011, hlm. 44 hingga 46), model Prototyping dijalankan melalui tujuh tahapan siklus:

1. **Pengumpulan Kebutuhan (Susanto & Andriana, 2016, hlm. 332):** Pelanggan dan pengembang bersama-sama mendefinisikan format seluruh perangkat lunak, mengidentifikasi semua kebutuhan, dan garis besar sistem yang akan dibuat.
2. **Membangun Prototyping (Susanto & Andriana, 2016, hlm. 332):** Membangun perancangan kilat yang berfokus pada penyajian aspek perangkat lunak yang terlihat oleh pengguna (misalnya format masukan dan antarmuka keluaran).
3. **Evaluasi Prototyping (Susanto & Andriana, 2016, hlm. 332):** Prototipe dievaluasi oleh pelanggan untuk memastikan apakah rancangan awal telah memenuhi harapan pengguna.
4. **Mengkodekan Sistem (Susanto & Andriana, 2016, hlm. 332):** Prototipe yang telah disepakati diterjemahkan ke dalam bahasa pemrograman yang sesuai.
5. **Menguji Sistem (Susanto & Andriana, 2016, hlm. 332):** Perangkat lunak diuji dengan pengujian kotak putih (_white box_) atau kotak hitam (_black box_) untuk meminimalkan galat.
6. **Evaluasi Sistem (Susanto & Andriana, 2016, hlm. 332):** Pelanggan mengevaluasi kembali apakah sistem yang sudah dikodekan benar-benar siap dan sesuai harapan.
7. **Menggunakan Sistem (Susanto & Andriana, 2016, hlm. 332):** Perangkat lunak yang telah diuji dan disetujui siap digunakan secara penuh di lingkungan operasional.

#### D. Kelebihan

- Mereduksi ketidakpastian kebutuhan secara dramatis karena pengguna dapat berinteraksi langsung dengan antarmuka dan alur sistem sejak dini (Susanto & Andriana, 2016, hlm. 333).
- Partisipasi aktif pengguna tercipta secara intensif, sehingga meminimalkan risiko penolakan sistem pada saat penerapan final (Putra, 2022, hlm. 433).
- Mampu mendeteksi kesalahpahaman analisis kebutuhan pada tahap sangat awal sebelum arsitektur perangkat lunak dibangun secara permanen (Sommerville, 2011, hlm. 44).

#### E. Kelemahan

- Pengguna sering kali mengira bahwa prototipe yang berfungsi merupakan sistem akhir yang siap pakai, sehingga mengabaikan aspek kualitas internal seperti keamanan data dan ketahanan beban kerja (Sommerville, 2011, hlm. 45).
- Rentan terhadap degradasi struktur kode program (_code degradation_) karena pengembang cenderung melakukan penambalan kode secara tergesa-gesa guna memenuhi umpan balik tampilan dari pengguna (Sommerville, 2011, hlm. 45).
- Tidak memiliki kerangka kerja disiplin waktu dan pencatatan galat personal yang baku untuk mengendalikan efisiensi kerja pengembang tunggal (Dzhurov dkk., 2009, hlm. 253).

#### F. Evaluasi Kesesuaian Kasus Bimbel Artha

Meskipun teknik pembuatan purwarupa sangat dibutuhkan untuk merancang antarmuka Bimbel Artha, model Prototyping murni tidak memiliki disiplin rekayasa perangkat lunak yang memadai bagi pengembang tunggal. Tanpa mekanisme manajemen tugas teknis, pengujian unit otomatis, dan pelacakan galat perorangan, pengembangan sistem untuk delapan cabang rentan menghasilkan kode program yang rapuh dan sukar dipelihara.

---

### 2.3 Rapid Application Development (RAD)

#### A. Definisi dan Filosofi Dasar

Rapid Application Development (RAD) merupakan metodologi pengembangan adaptif berbasis siklus hidup inkremental pendek yang menekankan kecepatan penyelesaian sistem melalui pemanfaatan komponen perangkat lunak siap pakai dan lokakarya perancangan intensif bersama pengguna (Pratama, Hidayat, & Nurfaizah, 2023, hlm. 51). Model ini berupaya memadatkan waktu analisis dan perancangan konvensional menjadi rentang waktu yang sangat singkat, yakni berkisar antara 60 hingga 90 hari, dengan mengandalkan keterlibatan langsung pemangku kepentingan bisnis sepanjang proses pembangunan (Pressman, 2010, hlm. 45 hingga 47).

#### B. Tangkapan Layar Diagram Alur Proses dari Literatur Sumber

Berikut merupakan bukti diagram alur proses RAD Model Kendall yang diambil langsung dari penelitian Pratama dkk. (2023, hlm. 54 / PDF hlm. 6, Gambar 2):

<p align="center">
  <img src="./gambar_metode/03_rad_pratama_2023.png" alt="Alur Tahapan Metode Rapid Application Development" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.3</b> Alur Tahapan Metode RAD Model Kendall (Sumber: Pratama dkk., 2023, hlm. 54 / PDF hlm. 6, Gambar 2)</em>
  <br>
  <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Penerapan%20Metode%20RAD%20-%20Infotek%20-%20Pratama%20dkk%20-%202023.pdf#page=6">📄 Buka Naskah PDF Sumber (hlm. 6)</a>
</p>

#### C. Tahapan Baku Proses

Mengacu pada model Kendall yang diimplementasikan oleh Pratama, Hidayat, & Nurfaizah (2023, hlm. 51 hingga 54), metode RAD tersusun atas tiga tahapan utama:

1. **Perencanaan Syarat-syarat (Requirements Planning, Pratama dkk., 2023, hlm. 51):** Inisiasi proyek terpadu di mana analis dan perwakilan pengguna mengidentifikasi tujuan sistem, batasan operasional, serta kebutuhan informasi tingkat tinggi.
2. **Workshop Desain RAD (RAD Design Workshop, Pratama dkk., 2023, hlm. 52):** Lokakarya interaktif perancangan terintegrasi yang melibatkan analis, pemrogram, dan pengguna dalam dua aktivitas berkelanjutan:
   - _Analisis Pemodelan (Analysis Modeling):_ Menganalisis alur prosedur bisnis yang sedang berjalan guna mengidentifikasi kelemahan proses serta peluang otomasi.
   - _Desain Pemodelan (Design Modeling):_ Merancang proses bisnis, struktur basis data, dan tata letak antarmuka pengguna secara visual dan berulang hingga disepakati bersama.
3. **Implementasi atau Konstruksi (Implementation/Construction, Pratama dkk., 2023, hlm. 53):** Penerjemahan hasil pemodelan ke dalam bentuk aplikasi utuh menggunakan perangkat lunak generator kode atau kerangka kerja berbasis komponen, dilanjutkan dengan pengujian kinerja prototipe dan persiapan penerapan sistem.

#### D. Kelebihan

- Siklus pengembangan perangkat lunak berlangsung sangat cepat berkat penggunaan modul komponen yang dapat digunakan ulang (_reusable components_) (Pratama dkk., 2023, hlm. 50).
- Umpan balik dari pengguna diperoleh secara langsung dan berkelanjutan melalui sesi lokakarya tatap muka yang intensif (Sommerville, 2011, hlm. 48).
- Risiko ketidaksesuaian fungsi bisnis dapat ditekan karena pemodelan dirancang secara kolaboratif bersama pemakai sistem (Pressman, 2010, hlm. 46).

#### E. Kelemahan

- Menuntut komitmen waktu yang sangat intensif dari pihak pengguna untuk menghadiri lokakarya perancangan secara terus-menerus (Sommerville, 2011, hlm. 48).
- Memerlukan tim pengembang yang memiliki kemahiran tinggi dalam penggunaan peralatan otomatisasi dan pembagian kerja modular yang terspesialisasi (Pressman, 2010, hlm. 47).
- Tidak cocok untuk arsitektur sistem yang menuntut integrasi transaksi baru yang unik dan tidak tersedia dalam pustaka komponen bawaan (Pressman, 2010, hlm. 47).

#### F. Evaluasi Kesesuaian Kasus Bimbel Artha

Metode RAD tidak realistis diterapkan pada mitra Bimbel Artha. Pimpinan dan koordinator cabang Bimbel Artha memiliki keterbatasan waktu yang sangat tinggi akibat kewajiban mengelola kegiatan operasional pembelajaran di delapan cabang setiap harinya, sehingga mustahil diwajibkan menghadiri lokakarya perancangan intensif secara berkala. Selain itu, RAD mengasumsikan ketersediaan beberapa tim pengembang yang bekerja paralel pada modul terpisah, kondisi yang bertolak belakang dengan konteks Tugas Akhir yang dikerjakan oleh satu orang pengembang mandiri.

---

### 2.4 Model Spiral

#### A. Definisi dan Filosofi Dasar

Model Spiral dirumuskan oleh Barry W. Boehm pada tahun 1988 (hlm. 61 hingga 64) sebagai paradigma proses pengembangan perangkat lunak berbasis manajemen risiko (_risk-driven process model_). Setiap siklus spiral menggabungkan fleksibilitas pendekatan berbasis prototipe dengan keandalan dan keteraturan pendekatan Waterfall (Boehm, 1988, hlm. 61). Model ini memandang pengembangan sistem sebagai proses evolusioner yang membesar secara bertahap, di mana setiap putaran spiral difokuskan untuk mengidentifikasi dan memitigasi risiko terbesar yang berpotensi menggagalkan proyek sebelum melangkah ke tingkat rancangan berikutnya.

#### B. Tangkapan Layar Diagram Alur Proses dari Literatur Sumber

Berikut merupakan bukti diagram alur proses Spiral yang di-ekstrak langsung dari naskah klasik Barry W. Boehm (1988, hlm. 64, Figure 2):

<p align="center">
  <img src="./gambar_metode/04_spiral_boehm_1988.png" alt="Alur Kuadran Model Spiral" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.4</b> Alur Siklus Kuadran Model Spiral Berbasis Risiko (Sumber: Boehm, 1988, hlm. 64, Figure 2)</em>
  <br>
  <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/A%20Spiral%20Model%20of%20Software%20Development%20and%20Enhancement%20-%20Prototyping%20-%20Boehm%20-%201988.pdf#page=7">📄 Buka Naskah PDF Sumber (hlm. 7)</a>
</p>

#### C. Tahapan Baku Proses

Berdasarkan rumusan Barry W. Boehm (1988, hlm. 64) dan dokumentasi Ian Sommerville (2011, hlm. 51 hingga 53), setiap putaran spiral dibagi ke dalam empat sektor kuadran utama:

1. **Objective Setting (Penentuan Sasaran, Boehm, 1988, hlm. 64; Sommerville, 2011, hlm. 52):** Menentukan sasaran khusus fase berjalan, alternatif solusi yang dapat diambil, serta batasan operasional, teknis, dan finansial dari proyek.
2. **Risk Assessment and Reduction (Penilaian dan Pengurangan Risiko, Boehm, 1988, hlm. 64; Sommerville, 2011, hlm. 52):** Melakukan analisis mendalam terhadap sumber potensi risiko proyek, diikuti oleh langkah mitigasi seperti pembuatan simulasi, tolok ukur kinerja, atau pembangunan purwarupa sistem.
3. **Development and Validation (Pengembangan dan Validasi, Boehm, 1988, hlm. 64; Sommerville, 2011, hlm. 53):** Memilih model pengembangan turunan yang sesuai dengan profil risiko fase tersebut, kemudian merancang arsitektur, mengodekan modul, dan memvalidasi kebenaran fungsionalitas sistem.
4. **Planning (Perencanaan Fase Berikutnya, Boehm, 1988, hlm. 64; Sommerville, 2011, hlm. 53):** Meninjau kembali capaian fase yang telah diselesaikan bersama pemangku kepentingan dan merencanakan alokasi sumber daya serta cakupan kerja untuk putaran spiral berikutnya.

#### D. Kelebihan

- Sangat unggul dalam mengendalikan risiko teknis, biaya, dan jadwal pada proyek-proyek raksasa yang memiliki ketidakpastian tinggi (Khan dkk., 2011, hlm. 97).
- Perangkat lunak berevolusi secara bertahap dari level konseptual hingga level produksi melalui pengawasan kualitas yang sangat ketat (Boehm, 1988, hlm. 65).
- Memungkinkan penyesuaian strategi pengembangan pada setiap putaran sesuai karakteristik tantangan yang dihadapi (Sommerville, 2011, hlm. 53).

#### E. Kelemahan

- Membutuhkan keahlian penaksiran risiko formal yang sangat mendalam dan terspesialisasi, yang jarang dikuasai oleh pengembang pada level pemula atau individual (Boehm, 1988, hlm. 70).
- Beban manajemen, analisis dokumen, dan administrasi fase sangat besar (_high process overhead_), sehingga proses berjalan lambat (Khan dkk., 2011, hlm. 97).
- Sangat tidak ekonomis untuk diterapkan pada proyek aplikasi berukuran kecil hingga menengah karena biaya pengendalian risiko melebihi nilai proyek itu sendiri (Sommerville, 2011, hlm. 53).

#### F. Evaluasi Kesesuaian Kasus Bimbel Artha

Penggunaan model Spiral untuk Bimbel Artha merupakan tindakan berlebihan (_overkill_). Sistem manajemen bimbingan belajar tidak menghadapi ketidakpastian teknologi tingkat tinggi atau kegagalan yang mengancam keselamatan nyawa (_mission-critical systems_). Beban formalitas penaksiran risiko spiral hanya akan menghabiskan waktu penelitian tanpa memberikan kontribusi langsung terhadap terwujudnya modul perangkat lunak operasional bagi mitra.

---

### 2.5 Kerangka Kerja Scrum

#### A. Definisi dan Filosofi Dasar

Scrum merupakan kerangka kerja adaptif ringan yang diciptakan oleh Ken Schwaber dan Jeff Sutherland untuk membantu tim kolaboratif menghasilkan nilai bisnis melalui penyelesaian masalah kompleks secara adaptif (Schwaber & Sutherland, 2020, hlm. 3 hingga 5). Filosofi dasar Scrum berlandaskan pada teori kendali proses empiris (_empirical process control_) yang bersandar pada tiga pilar utama, yaitu transparansi (_transparency_), inspeksi (_inspection_), dan adaptasi (_adaptation_). Scrum membagi pekerjaan ke dalam siklus waktu tetap (_timebox_) yang disebut Sprint dengan durasi maksimal satu bulan untuk menghasilkan artefak inkremen perangkat lunak yang berpotensi dirilis.

#### B. Tangkapan Layar Diagram Alur Proses dari Literatur Sumber

Berikut merupakan bukti diagram kerangka kerja Scrum yang diambil langsung dari penelitian Kurniawan & Sani (2019, hlm. 149, Gambar 1):

<p align="center">
  <img src="./gambar_metode/05_scrum_kurniawan_2019.png" alt="Alur Kerangka Kerja Scrum" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.5</b> Alur Kerangka Kerja dan Siklus Sprint Scrum (Sumber: Kurniawan & Sani, 2019, hlm. 149, Gambar 1)</em>
  <br>
  <a href="./JURNAL/04_FITUR_DAN_TEKNOLOGI_PENDUKUNG/Pemodelan%20SCRUM%20Klinik%20Ar-Rokhim%20-%20JOINS%20-%20Kurniawan%20&%20Sani%20-%202019.pdf#page=3">📄 Buka Naskah PDF Sumber (hlm. 3)</a>
</p>

#### C. Peran, Acara, dan Tahapan Proses

Dokumen resmi _The Scrum Guide_ (Schwaber & Sutherland, 2020, hlm. 5 hingga 12) serta elaborasi Kurniawan & Sani (2019, hlm. 148 hingga 150) menegaskan bahwa kerangka kerja Scrum terdiri atas komponen wajib yang tidak boleh diubah:

- **Tiga Peran Wajib (Scrum Roles, Schwaber & Sutherland, 2020, hlm. 5 hingga 7):** _Product Owner_ (pemilik visi produk dan penentu prioritas), _Scrum Master_ (penjaga efektivitas proses dan pembersih hambatan), dan _Developers_ (tim lintas-fungsi pelaksana teknis pembangunan inkremen).
- **Empat Acara Utama dalam Siklus Sprint (Schwaber & Sutherland, 2020, hlm. 7 hingga 12):**
  1. **Sprint Planning (Perencanaan Sprint, hlm. 8):** Seluruh tim menyepakati sasaran Sprint (_Sprint Goal_), memilih butir kebutuhan dari _Product Backlog_, dan merumuskan rencana teknis pengerjaan ke dalam _Sprint Backlog_.
  2. **Daily Scrum (Pertemuan Harian, hlm. 9):** Acara berdurasi 15 menit setiap hari kerja bagi pengembang untuk memeriksa kemajuan terhadap _Sprint Goal_ dan menyesuaikan rencana kerja 24 jam ke depan.
  3. **Sprint Review (Tinjauan Sprint, hlm. 10):** Tim Scrum mempresentasikan hasil inkremen kerja kepada pemangku kepentingan internal maupun eksternal guna menginspeksi kemajuan dan memperbarui _Product Backlog_.
  4. **Sprint Retrospective (Retrospektif Sprint, hlm. 11):** Sesi evaluasi internal tim untuk mengidentifikasi aspek proses kerja, hubungan personal, serta peralatan yang berjalan baik atau perlu ditingkatkan pada Sprint berikutnya.

#### D. Kelebihan

- Keterlibatan tim sangat dinamis, mandiri, dan memiliki rasa kepemilikan bersama yang tinggi terhadap produk (Mishra & Alzoubi, 2023, hlm. 890).
- Kebutuhan bisnis yang dinamis dapat direspons secara teratur di setiap pergantian siklus Sprint (Kuhrmann dkk., 2021, hlm. 12).
- Transparansi progres proyek sangat tinggi berkat visibilitas artefak _Sprint Backlog_, _Burndown Chart_, dan peragaan perangkat lunak secara periodik (Schwaber & Sutherland, 2020, hlm. 12).

#### E. Kelemahan

- Sangat bergantung pada keberadaan tim multidisiplin dengan ukuran ideal 3 hingga 9 orang pengembang, sehingga tidak dirancang untuk pengembang tunggal (Schwaber & Sutherland, 2020, hlm. 6).
- Larangan perangkapan peran (_role separation_) merupakan prinsip mutlak dalam Scrum guna mencegah konflik kepentingan antara penentu prioritas bisnis dan pelaksana teknis (Schwaber, 1995, hlm. 4).
- Menghasilkan distorsi proses yang fatal apabila dipaksakan pada pengerjaan individual, di mana acara _Daily Scrum_ menjadi formalitas semu tanpa dialog timbal balik nyata (Mahnic, 2018, hlm. 127).

#### F. Evaluasi Kesesuaian Kasus Bimbel Artha

Scrum secara metodologis tidak dapat dipertanggungjawabkan pada skripsi pengembang mandiri. Dalam pengerjaan Tugas Akhir ini, peneliti bertindak sendirian sebagai pengembang (_solo developer_). Menerapkan Scrum akan menimbulkan cacat metodologis serius di mana peneliti harus berpura-pura menjadi _Product Owner_, merangkap _Scrum Master_, dan melakukan pertemuan harian _Daily Scrum_ dengan dirinya sendiri. Hal ini bertentangan dengan prinsip integritas akademik yang ditekankan oleh dosen penguji.

---

### 2.6 Extreme Programming (XP)

#### A. Definisi dan Filosofi Dasar

Extreme Programming (XP) dirumuskan oleh Kent Beck sebagai metodologi pengembangan perangkat lunak tangkas yang mendorong praktik-praktik rekayasa terbaik ke tingkat yang sangat ekstrem (Beck & Andres, 2004, hlm. 15 hingga 28). XP berlandaskan pada lima nilai inti, yaitu komunikasi (_communication_), kesederhanaan (_simplicity_), umpan balik (_feedback_), keberanian (_courage_), dan rasa hormat (_respect_). Berbeda dari Scrum yang berfokus pada kerangka kerja manajemen proyek, XP secara eksplisit mengedepankan disiplin teknis pengodean seperti penulisan tes sebelum pengodean (_Test-Driven Development_), desain sederhana, integrasi berkelanjutan, dan pemrograman berpasangan (_Pair Programming_).

#### B. Tangkapan Layar Diagram Alur Proses dari Literatur Sumber

Berikut merupakan bukti diagram alur proses Extreme Programming yang di-ekstrak langsung dari naskah penelitian Suputra dkk. (2026, hlm. 78, Gambar 1) serta siklus rilis XP dari buku Ian Sommerville (2011, hlm. 65, Figure 3.3):

<p align="center">
  <img src="./gambar_metode/06_xp_suputra_2026.png" alt="Alur Tahapan Siklus Extreme Programming" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.6</b> Alur Empat Tahapan Siklus Extreme Programming (Sumber: Suputra dkk., 2026, hlm. 78, Gambar 1)</em>
  <br>
  <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Siswa%20SMP%20-%20Extreme%20Programming%20(XP)%20-%20Suputra%20dkk%20-%202026.pdf#page=4">📄 Buka Naskah PDF Sumber (hlm. 4)</a>
</p>

<p align="center">
  <img src="./gambar_metode/06b_xp_sommerville_2011.png" alt="Siklus Rilis Extreme Programming" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.6b</b> Siklus Rilis Extreme Programming (Sumber: Sommerville, 2011, hlm. 65, Figure 3.3)</em>
  <br>
  <a href="./JURNAL/BUKU/Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf#page=82">📄 Buka Naskah PDF Sumber (hlm. 82)</a>
</p>

#### C. Tahapan Baku Proses

Berdasarkan telaah Kent Beck & Cynthia Andres (2004, hlm. 45 hingga 60) serta rincian Suputra dkk. (2026, hlm. 77 hingga 79), siklus hidup iterasi XP berjalan melalui empat tahapan utama:

1. **Planning (Perencanaan, Beck & Andres, 2004, hlm. 45):** Pengguna menuliskan kebutuhan fungsional dalam bentuk kartu cerita pengguna (_user stories_). Tim pengembang memperkirakan bobot tugas dan menyusun rencana rilis (_release planning_) serta rencana iterasi (_iteration planning_) berdurasi 1 hingga 3 minggu.
2. **Design (Perancangan, Beck & Andres, 2004, hlm. 50):** Mengedepankan prinsip desain sederhana (_Simple Design_) yang hanya memenuhi kebutuhan cerita berjalan tanpa spekulasi masa depan. Jika menghadapi ketidakpastian teknis rumit, tim membangun solusi eksperimental cepat (_Spike Solution_).
3. **Coding (Pengodean, Beck & Andres, 2004, hlm. 55):** Penulisan kode sumber wajib didahului oleh pembuatan skenario uji unit otomatis (_Test-Driven Development_). Aktivitas pengodean standar XP wajib dilaksanakan secara berpasangan (_Pair Programming_) di mana dua pemrogram bekerja di satu komputer, disertai integrasi kode secara berkala (_Continuous Integration_) ke repositori utama.
4. **Testing (Pengujian, Beck & Andres, 2004, hlm. 58):** Pengujian unit otomatis dijalankan setiap kali terjadi kompilasi atau integrasi kode. Pada akhir iterasi, pengguna menjalankan pengujian penerimaan (_Acceptance Testing_) untuk memvalidasi bahwa modul perangkat lunak telah memenuhi kriteria penerimaan cerita pengguna.

#### D. Kelebihan

- Kualitas kode program internal sangat tinggi dan minim cacat berkat kombinasi TDD, peninjauan kode berkelanjutan melalui _Pair Programming_, dan refaktorisasi konstan (Williams dkk., 2000, hlm. 20 hingga 23).
- Desain sistem tetap ramping, adaptif, dan mudah dipahami seiring berjalannya proyek (Beck & Andres, 2004, hlm. 51).
- Umpan balik teknis diperoleh dalam hitungan detik melalui eksekusi rangkaian tes unit otomatis (Khan dkk., 2011, hlm. 96).

#### E. Kelemahan

- Praktik _Pair Programming_ secara inheren menuntut ketersediaan rekan pemrogram kedua yang bekerja bersama secara fisik di stasiun kerja yang sama (Beck & Andres, 2004, hlm. 56).
- Membutuhkan keberadaan perwakilan pengguna di lokasi pengembangan setiap saat (_On-site Customer_), suatu kondisi yang sangat sulit dipenuhi dalam kemitraan UMKM (Agarwal & Umphress, 2008, hlm. 83).
- Tingkat ketergantungan pada disiplin budaya tim yang kompak sangat tinggi, sehingga sulit dipraktikkan tanpa bimbingan pelatih berpengalaman (Mishra & Alzoubi, 2023, hlm. 891).

#### F. Evaluasi Kesesuaian Kasus Bimbel Artha

Meskipun prinsip teknis XP sangat unggul, XP murni tidak dapat diterapkan secara utuh dalam Tugas Akhir pengembang tunggal. Penelitian Williams, Kessler, Cunningham, & Jeffries (2000, hlm. 22) menunjukkan bahwa kekuatan utama penjaminan kualitas XP bertumpu pada _Pair Programming_. Seorang pengembang tunggal yang mengerjakan skripsi tidak mungkin melaksanakan _Pair Programming_ dan tidak memiliki mitra bimbel yang dapat hadir mendampingi di meja kerja setiap hari (_On-site Customer_). Diperlukan adaptasi resmi yang mengakomodasi keterbatasan pengembang mandiri tanpa menghilangkan keunggulan rekayasa XP.

---

### 2.7 Metode Kanban

#### A. Definisi dan Filosofi Dasar

Kanban bukanlah metodologi pengembangan perangkat lunak berbasis tahapan linear melainkan strategi manajemen alur kerja visual (_flow-based strategy_) yang bertujuan memaksimalkan penghantaran nilai bisnis dengan mengoptimalkan alur kerja operasional (Coleman & Vacanti, 2025, hlm. 2 hingga 4). Mengacu pada panduan resmi _The Kanban Guide_ (2025, hlm. 2), Kanban berakar pada sistem produksi Toyota dan Lean, dengan prinsip dasar bahwa efisiensi kerja dicapai bukan melalui pembatasan rentang waktu (_timeboxing_), melainkan dengan membatasi jumlah pekerjaan yang sedang berlangsung (_Work in Progress / WIP_) pada setiap tahapan alur secara visual.

#### B. Tangkapan Layar Diagram Alur Proses dari Literatur Sumber

Berikut merupakan bukti diagram alur kerja dan integrasi papan aliran Kanban yang di-ekstrak langsung dari naskah penelitian Mahnic (2018, hlm. 128 / PDF hlm. 3, Figure 1):

<p align="center">
  <img src="./gambar_metode/07_kanban_mahnic_2018.png" alt="Integrasi Alur Kerja dan Papan Aliran Kanban" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.7</b> Visualisasi Alur Kerja Aliran dan Papan Kanban (Sumber: Mahnic, 2018, hlm. 128 / PDF hlm. 3, Figure 1)</em>
  <br>
  <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Scrum2Kanban%20-%20Integrating%20Kanban%20and%20Scrum%20in%20Capstone%20Course%20-%20IEEE%20-%20Mahnic%20-%202018.pdf#page=3">📄 Buka Naskah PDF Sumber (hlm. 3)</a>
</p>

#### C. Praktik dan Tahapan Inti Proses

Berdasarkan rujukan resmi Todd Coleman & Daniel S. Vacanti (2025, hlm. 3 hingga 6), implementasi Kanban bertumpu pada tiga praktik wajib serta pengelolaan empat metrik aliran:

1. **Defining and Visualizing the Workflow (Mendefinisikan dan Memvisualisasikan Alur Kerja, Coleman & Vacanti, 2025, hlm. 3):** Menetapkan titik awal (_point of commitment_) dan titik akhir alur kerja, mendefinisikan tahapan perpindahan butir kerja pada papan visual (Kanban Board), serta merumuskan kebijakan eksplisit (_explicit policies_) untuk setiap tahapan.
2. **Actively Managing Items in a Workflow (Mengelola Butir Kerja Secara Aktif, Coleman & Vacanti, 2025, hlm. 4):** Membatasi jumlah tugas yang diperbolehkan berada dalam kolom pengerjaan secara bersamaan (_limiting Work in Progress_). Pengembang juga wajib memantau usia butir kerja (_Work Item Age_) guna mencegah terjadinya hambatan atau tumpukan pekerjaan yang terhenti.
3. **Improving the Workflow (Meningkatkan Alur Kerja Secara Berkelanjutan, Coleman & Vacanti, 2025, hlm. 5):** Menelaah efisiensi aliran sistem secara empiris berlandaskan empat metrik dasar Kanban, yaitu _Work in Progress (WIP)_, _Cycle Time_ (waktu tempuh butir dari komitmen hingga selesai), _Work Item Age_, dan _Throughput_ (jumlah butir yang selesai per satuan waktu).

#### D. Kelebihan

- Sangat fleksibel dan memiliki resistensi perubahan yang sangat rendah karena tidak mengganggu struktur organisasi yang telah berjalan (Mahnic, 2018, hlm. 127).
- Sangat transparan dalam mengungkap lokasi terjadinya hambatan (_bottleneck_) dalam proses produksi perangkat lunak (Coleman & Vacanti, 2025, hlm. 4).
- Menghilangkan stres kerja yang dipicu oleh tenggat waktu siklus buatan, sehingga sangat cocok untuk penanganan operasional berkelanjutan (_continuous maintenance_) (Mahnic, 2018, hlm. 129).

#### E. Kelemahan

- Tidak menyediakan panduan rekayasa teknis perangkat lunak (_software engineering practices_) sama sekali, seperti standar perancangan, TDD, refaktorisasi, atau arsitektur kode (Mahnic, 2018, hlm. 130).
- Ketiadaan batas waktu bertahap (_lack of timeboxed iterations_) berisiko menyebabkan hilangnya urgensi penyelesaian bagi pengembang yang kurang berdisiplin (Coleman & Vacanti, 2025, hlm. 5).
- Kurang cocok untuk proyek perancangan sistem baru yang membutuhkan tonggak capaian berkala untuk pengujian fungsionalitas menyeluruh bersama pengguna (Mishra & Alzoubi, 2023, hlm. 892).

#### F. Evaluasi Kesesuaian Kasus Bimbel Artha

Kanban sangat bermanfaat sebagai alat bantu visualisasi tugas harian, namun tidak memadai sebagai metodologi utama penyusunan skripsi rekayasa perangkat lunak. Skripsi menuntut adanya tahapan perancangan arsitektur, pengujian modul, serta batasan siklus iterasi yang terstruktur untuk menguji efektivitas sistem secara bertahap bersama pemilik bimbingan belajar. Ketiadaan instruksi disiplin rekayasa pada Kanban membuatnya tidak dapat berdiri sendiri sebagai metodologi perancangan prototipe sistem multicabang Artha.

---

### 2.8 Lean Software Development (LSD)

#### A. Definisi dan Filosofi Dasar

Lean Software Development (LSD) merupakan filosofi dan seperangkat prinsip berpikir tangkas yang dikembangkan oleh Mary Poppendieck dan Tom Poppendieck (2003, hlm. xxiii hingga xxvii) dengan mengadaptasi prinsip-prinsip manufaktur ramping (_Lean Manufacturing_) ke dalam industri rekayasa perangkat lunak. Inti dari pendekatan Lean adalah penciptaan nilai maksimal bagi pengguna akhir melalui eliminasi radikal terhadap segala bentuk pemborosan sumber daya (_waste elimination_), pengoptimalan efisiensi rantai nilai (_value stream_), serta penghantaran solusi kerja secara berkelanjutan dan secepat mungkin kepada pelanggan.

#### B. Tangkapan Layar Diagram Alur Proses dari Literatur Sumber

Berikut merupakan bukti dokumentasi tujuh prinsip inti Lean Software Development yang di-ekstrak langsung dari buku klasik Mary & Tom Poppendieck (2003, PDF hlm. 26 hingga 29):

<p align="center">
  <img src="./gambar_metode/08_lean_poppendieck_2003.png" alt="Tujuh Prinsip Inti Lean Software Development" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.8</b> Tujuh Prinsip Operasional Lean Software Development (Sumber: Poppendieck & Poppendieck, 2003, hlm. 7 hingga 10 / PDF hlm. 26)</em>
  <br>
  <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Lean%20Software%20Development%20-%20An%20Agile%20Toolkit%20-%20Poppendieck%20-%202003.pdf#page=26">📄 Buka Naskah PDF Sumber (hlm. 26)</a>
</p>

#### C. Tujuh Prinsip Inti Lean

Berdasarkan karya fundamental Mary Poppendieck & Tom Poppendieck (2003, hlm. xxiii hingga xxvii serta hlm. 1 hingga 10), Lean Software Development dibangun di atas tujuh prinsip operasional:

1. **Eliminate Waste (Mengeliminasi Pemborosan, Poppendieck & Poppendieck, 2003, hlm. 1):** Membuang segala aktivitas yang tidak memberikan nilai tambah langsung kepada pengguna, seperti penulisan kode atau fitur yang tidak terpakai, birokrasi dokumen yang berlebihan, perpindahan konteks tugas, dan keterlambatan alur informasi.
2. **Amplify Learning (Memperkuat Pembelajaran, Poppendieck & Poppendieck, 2003, hlm. 3):** Memperlakukan pengembangan perangkat lunak sebagai proses pembelajaran berkelanjutan melalui siklus pendek yang diisi oleh pembuatan purwarupa, umpan balik langsung, dan pengujian berulang.
3. **Decide as Late as Possible (Menunda Komitmen, Poppendieck & Poppendieck, 2003, hlm. 4):** Menunda keputusan desain arsitektur yang tidak dapat diubah hingga saat-saat terakhir di mana fakta empiris telah terkumpul secara lengkap, sehingga menghindari penguncian keputusan spekulatif yang keliru.
4. **Deliver as Fast as Possible (Mengirimkan Hasil Secepat Mungkin, Poppendieck & Poppendieck, 2003, hlm. 6):** Memperpendek jarak waktu antara permintaan kebutuhan pengguna dan ketersediaan perangkat lunak yang berfungsi guna meminimalkan akumulasi perubahan kebutuhan.
5. **Empower the Team (Memberdayakan Tim, Poppendieck & Poppendieck, 2003, hlm. 7):** Memberikan wewenang teknis kepada orang-orang yang mengeksekusi pekerjaan secara langsung untuk merancang alur kerja terbaik mereka sendiri.
6. **Build Integrity In (Membangun Integritas ke Dalam Sistem, Poppendieck & Poppendieck, 2003, hlm. 8):** Memastikan sistem memiliki integritas perseptual (tampak intuitif dan memuaskan bagi pengguna) serta integritas struktural (arsitektur modular, teruji secara otomatis, dan tahan terhadap perubahan).
7. **See the Whole (Melihat Gambaran Secara Menyeluruh, Poppendieck & Poppendieck, 2003, hlm. 9):** Mengoptimalkan kinerja sistem perangkat lunak dan proses bisnis secara keseluruhan, bukan sekadar melakukan optimalisasi parsial pada satu modul atau unit fungsi terisolasi.

#### D. Kelebihan

- Mampu memangkas biaya dan waktu pengerjaan proyek secara signifikan dengan menyingkirkan artefak yang tidak esensial (Poppendieck & Poppendieck, 2003, hlm. 2).
- Arsitektur sistem menjadi sangat ramping dan relevan dengan proses bisnis nyata karena hanya memuat fitur-fitur yang terbukti memberikan nilai nyata bagi pengguna (Mishra & Alzoubi, 2023, hlm. 892).
- Memberikan fleksibilitas pengambilan keputusan strategis yang tinggi hingga fase-fase akhir proyek (Poppendieck & Poppendieck, 2003, hlm. 5).

#### E. Kelemahan

- Merupakan paradigma tingkat tinggi yang bersifat konseptual dan tidak menyajikan tahapan langkah operasional yang preskriptif untuk diikuti oleh peneliti (Poppendieck & Poppendieck, 2003, hlm. xxv).
- Sangat bergantung pada kedewasaan dan kemahiran pengembang dalam menerjemahkan prinsip-prinsip abstrak ke dalam tindakan teknis harian (Kuhrmann dkk., 2021, hlm. 14).
- Sulit dievaluasi ketercapaian kepatuhan metodologinya dalam naskah skripsi akademis karena ketiadaan panduan artefak formal yang terstandarisasi baku (Khan dkk., 2011, hlm. 98).

#### F. Evaluasi Kesesuaian Kasus Bimbel Artha

Prinsip-prinsip Lean sangat berharga untuk diadopsi sebagai pola pikir peneliti dalam merampingkan fitur Bimbel Artha agar tidak terjadi pemborosan tenaga pengembang mandiri. Namun demikian, Lean Software Development tidak memiliki kerangka kerja siklus hidup operasional (_process lifecycle_) yang terstruktur langkah-demi-langkah. Penguji skripsi ITK menuntut tahapan penelitian yang terdefinisi secara operasional, mulai dari inisiasi kebutuhan hingga pengujian sistem, yang tidak disediakan secara terinci oleh literatur Lean.

---

### 2.9 Personal Extreme Programming (PxP)

#### A. Definisi dan Filosofi Dasar

Personal Extreme Programming (PxP) merupakan metodologi pengembangan perangkat lunak tangkas yang dirancang secara khusus oleh Yani Dzhurov, Iva Krasteva, dan Sylvia Ilieva pada tahun 2009 untuk menjawab tantangan pengembang mandiri (_autonomous developers / single-person software engineers_) (Dzhurov dkk., 2009, hlm. 252 hingga 254). PxP memadukan ketangkasan dan praktik rekayasa teknis bermutu tinggi dari Extreme Programming (XP) dengan disiplin pengukuran metrik perorangan dari Personal Software Process (PSP) yang dirumuskan oleh Watts Humphrey (Agarwal & Umphress, 2008, hlm. 83; Dzhurov dkk., 2009, hlm. 253; Iyawa, 2020, hlm. 2). PxP memecahkan masalah mendasar pada proyek perangkat lunak mandiri, yaitu bagaimana mempertahankan kualitas kode yang tinggi tanpa kehadiran rekan kerja (_pair programming_) dan bagaimana menjaga disiplin perencanaan tanpa beban dokumentasi PSP yang terlalu berat.

#### B. Tangkapan Layar Diagram Alur Proses dari Literatur Sumber

Berikut merupakan bukti diagram proses siklus hidup PxP asli dari naskah penemunya (Dzhurov dkk., 2009, hlm. 255, Figure 1) serta adaptasi penerapannya oleh sivitas akademika Institut Teknologi Kalimantan (Fikri & Prabowo / ITK, 2020, hlm. 2, Gambar 1):

<p align="center">
  <img src="./gambar_metode/07_pxp_dzhurov_2009.png" alt="Alur Proses Rekayasa Personal Extreme Programming" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.9</b> Alur Proses Siklus Kerja Personal Extreme Programming (Sumber: Dzhurov dkk., 2009, hlm. 255, Figure 1)</em>
  <br>
  <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Personal%20Extreme%20Programming%20-%20Agile%20for%20Autonomous%20Developer%20-%20S3T%202009%20-%20Dzhurov%20dkk%20-%202009.pdf#page=3">📄 Buka Naskah PDF Sumber (hlm. 3)</a>
</p>

<p align="center">
  <img src="./gambar_metode/08_pxp_fikri_itk_2020.png" alt="Alur Siklus PxP Studi Kasus Lokal ITK" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />
  <br>
  <em><b>Gambar 2.10</b> Alur Kerangka Kerja PxP pada Penelitian Mandiri Sivitas Akademika ITK (Sumber: Fikri & Prabowo / ITK, 2020, hlm. 2, Gambar 1)</em>
  <br>
  <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Buku%20Tamu%20DPOP%20Balikpapan%20-%20PxP%20-%20Fikri%20&%20Prabowo%20(ITK)%20-%202020.pdf#page=3">📄 Buka Naskah PDF Sumber (hlm. 3)</a>
</p>

#### C. Arsitektur Empat Belas Praktik PxP

Kekuatan metodologis PxP terletak pada integrasi harmonis antara 14 praktik kerja yang dikelompokkan ke dalam empat domain utama (Dzhurov dkk., 2009, hlm. 253 hingga 254):

1. **Enam Praktik Adopsi dari Extreme Programming (XP, Dzhurov dkk., 2009, hlm. 253):**
   - _Continuous Integration:_ Integrasi kode sumber ke repositori secara otomatis dan berkala guna mendeteksi konflik modul sedini mungkin.
   - _Simple Design:_ Merancang struktur sistem yang paling sederhana yang mampu memenuhi kebutuhan fungsi iterasi berjalan tanpa spekulasi berlebih.
   - _Small Releases:_ Menghasilkan rilis perangkat lunak dalam paket-paket kecil yang dapat langsung dioperasikan oleh pengguna di setiap akhir iterasi.
   - _Refactoring:_ Melakukan penyempurnaan struktur internal kode program secara berkesinambungan tanpa mengubah perilaku eksternal perangkat lunak.
   - _Test-Driven Development (TDD):_ Menuliskan skenario pengujian unit sebelum baris kode fungsional diimplementasikan guna menjamin akurasi logika sistem.
   - _Spike Solutions:_ Mengembangkan prototipe terisolasi yang cepat untuk mengeksplorasi solusi teknis terhadap masalah arsitektur yang berisiko tinggi.
2. **Enam Praktik Disiplin dari Personal Software Process (PSP, Dzhurov dkk., 2009, hlm. 254):**
   - _Time Recording:_ Mencatat durasi waktu kerja nyata pada setiap tugas teknis guna mengukur produktivitas pribadi.
   - _Defect Type Standard:_ Mengklasifikasikan setiap galat yang ditemukan ke dalam kategori baku (seperti galat antarmuka, logika, penugasan, atau basis data).
   - _Defect Recording:_ Mencatat riwayat setiap cacat kode, fase kemunculan, fase penemuan, serta waktu yang dibutuhkan untuk memperbaikinya.
   - _Size Measurement:_ Mengukur volume perangkat lunak yang dibangun menggunakan metrik terukur, seperti jumlah baris kode (_Lines of Code_) atau butir fungsi.
   - _Process Improvement Proposal (PIP):_ Mendokumentasikan usulan perbaikan alur kerja secara formal setiap kali ditemukan inefisiensi dalam proses pengembangan.
   - _Code Reviews:_ Melakukan peninjauan mandiri yang disiplin terhadap kode program sebelum integrasi guna menggantikan fungsi rekan kerja pada _pair programming_.
3. **Satu Praktik Bersama (Shared Practice, Dzhurov dkk., 2009, hlm. 254):**
   - _Coding Standard:_ Menerapkan konvensi penulisan kode program yang konsisten, bersih, dan terstandarisasi untuk memudahkan pemeliharaan jangka panjang.
4. **Satu Praktik Inovasi Mandiri PxP (Dzhurov dkk., 2009, hlm. 254):**
   - _PXP Task Planning and Estimation:_ Memecah setiap kebutuhan fungsional ke dalam sekumpulan tugas teknis terkategorisasi (seperti pengujian unit, logika bisnis, prosedur basis data, desain formulir antarmuka) dan menaksir durasi pengerjaan berdasarkan tren historis data kinerja proyek sebelumnya.

```
                      STRUKTUR 14 PRAKTIK PxP
                                 |
         +-----------------------+-----------------------+
         |                       |                       |
   [6 PRAKTIK XP]          [6 PRAKTIK PSP]      [PRAKTIK BERSAMA & PXP]
   - Continuous            - Time Recording      - Coding Standard
     Integration           - Defect Type           (Bersama XP & PSP)
   - Simple Design           Standard            - PXP Task Planning &
   - Small Releases        - Defect Recording      Estimation
   - Refactoring           - Size Measurement      (Inovasi Mandiri PxP)
   - Test-Driven           - Process Improvement
     Development (TDD)       Proposal (PIP)
   - Spike Solutions       - Code Reviews
```

#### D. Tujuh Tahapan Baku Proses PxP

Berdasarkan naskah asli Yani Dzhurov, Iva Krasteva, & Sylvia Ilieva (2009, hlm. 254 hingga 256) serta penerapannya dalam penelitian terdahulu (Hasan, H. I., Marthasari, G. I., & Nuryasin, I. (2021). Implementasi Metode Personal Extreme Programming Dalam Pengembangan Sistem Administrasi Pelayanan Desa. REPOSITOR, 3(1), hlm. 43-50.

1. **Requirements (Kebutuhan, Dzhurov dkk., 2009, hlm. 254):** Peneliti menyusun dokumen kebutuhan fungsional dan non-fungsional sistem secara sistematis berdasarkan hasil wawancara dan observasi proses bisnis bersama mitra.
2. **Planning (Perencanaan, Dzhurov dkk., 2009, hlm. 254):** Peneliti merinci setiap kebutuhan fungsional ke dalam tugas-tugas teknis yang terkategorisasi, memperkirakan waktu pengerjaan berlandaskan data log historis, serta menetapkan keputusan arsitektur utama (seperti bahasa pemrograman, basis data, dan kerangka kerja).
3. **Iteration Initialization (Inisialisasi Iterasi, Dzhurov dkk., 2009, hlm. 255):** Peneliti memilih sekumpulan tugas teknis dari daftar rencana untuk menjadi sasaran utama dalam iterasi jangka pendek berdurasi 1 hingga 3 minggu.
4. **Design (Perancangan, Dzhurov dkk., 2009, hlm. 255):** Peneliti memodelkan diagram modul, rancangan antarmuka pengguna, dan skema entitas basis data yang relevan secara spesifik hanya untuk kebutuhan tugas dalam iterasi berjalan (_Simple Design_).
5. **Implementation (Implementasi, Dzhurov dkk., 2009, hlm. 255):** Fase penulisan kode nyata yang secara ketat menjalankan tiga sub-fase sekuensial internal:
   - _Unit Testing:_ Penulisan skenario uji unit otomatis sebelum kode fungsi dibuat (_TDD_).
   - _Code Generation:_ Penulisan kode program inti hingga berhasil melewati pengujian unit.
   - _Code Refactoring:_ Penyempurnaan struktur dan kebersihan kode program berpedoman pada standar pengodean (_Coding Standard_).
6. **System Testing (Pengujian Sistem, Dzhurov dkk., 2009, hlm. 255):** Peneliti memverifikasi keseluruhan sistem terintegrasi terhadap spesifikasi kebutuhan, mencatat galat yang muncul ke dalam _Defect Log_, serta memperbaikinya hingga seluruh pengujian fungsional terpenuhi.
7. **Retrospective (Retrospeksi, Dzhurov dkk., 2009, hlm. 256):** Peneliti melakukan evaluasi menyeluruh di akhir iterasi dengan menganalisis kesesuaian estimasi waktu rencana versus durasi riil, mengevaluasi efektivitas pencegahan cacat, serta merumuskan dokumen usulan perbaikan proses (_Process Improvement Proposal / PIP_) untuk diterapkan pada iterasi berikutnya.

#### E. Kelebihan

- Satu-satunya metodologi tangkas yang dirancang secara matematis dan prosedural khusus untuk pengembang tunggal tanpa tim (Dzhurov dkk., 2009, hlm. 252; Iyawa, 2020, hlm. 2).
- Menghadirkan jaminan kualitas perangkat lunak internal yang sangat tinggi tanpa memerlukan biaya penambahan staf kedua melalui penerapan TDD, standar pengodean, dan peninjauan kode mandiri (Agarwal & Umphress, 2008, hlm. 84).
- Menghasilkan dokumentasi metrik empiris yang lengkap (_time log_, _defect log_, _refactoring report_, _retrospective review_) yang memberikan bukti ilmiah kuat pada saat sidang Tugas Akhir (Asri dkk., 2018, hlm. 286; Hasan, H. I., Marthasari, G. I., & Nuryasin, I. (2021). Implementasi Metode Personal Extreme Programming Dalam Pengembangan Sistem Administrasi Pelayanan Desa. REPOSITOR, 3(1), hlm. 43-50.
- Siklus rilis pendek memungkinkan pengelola mitra melihat kemajuan nyata secara bertahap dan memberikan masukan tanpa harus terlibat dalam birokrasi teknis yang rumit (Ramadhan, 2026, hlm. 92).

#### F. Kelemahan

- Sangat bergantung pada disiplin dan integritas pribadi pengembang tunggal dalam mencatat data waktu dan cacat secara jujur dan konsisten (Dzhurov dkk., 2009, hlm. 257).
- Memerlukan kemahiran teknis yang seimbang, di mana satu orang dituntut mampu menjalankan peran sebagai analis, perancang arsitektur, pemrogram, penguji, sekaligus administrator proses (Iyawa, 2020, hlm. 4).
- Penaksiran waktu pada iterasi-iterasi awal memiliki deviasi yang cukup tinggi apabila pengembang belum memiliki catatan riwayat data produktivitas dari proyek sebelumnya (Dzhurov dkk., 2009, hlm. 256).

#### G. Evaluasi Kesesuaian Kasus Bimbel Artha

Personal Extreme Programming (PxP) merupakan metode yang memiliki tingkat kesesuaian sempurna (_perfect alignment_) dengan karakteristik Tugas Akhir Bimbingan Belajar Artha Balikpapan. Skripsi ini dikerjakan oleh satu orang mahasiswa dalam keterbatasan waktu akademis satu hingga dua semester. PxP memberikan kerangka kerja yang tidak mengharuskan kehadiran tim pengembang fisik, melindungi kualitas prototipe melalui otomasi pengujian, dan mengakomodasi proses evaluasi berkala bersama pemilik bimbel yang memiliki mobilitas tinggi dalam memantau delapan cabangnya.

---

## 3. TABEL KOMPARASI MULTIDIMENSI LIMA METODE PENGEMBANGAN SISTEM

Tabel komparasi berikut disusun secara terfokus berlandaskan arahan langsung Dosen Pembimbing (Bapak Arif Rahman, S.Kom., M.T.) pada bimbingan kelima. Arahan tersebut mewajibkan peneliti untuk tidak hanya membandingkan Personal Extreme Programming (PxP) dengan metode klasik Waterfall, melainkan wajib menyandingkannya secara kritis dengan metode-metode tangkas (*agile*) yang setara (*se-level*). 

Kelima metode yang disandingkan dalam sintesis ini mencakup satu model terencana konvensional (*Waterfall*) sebagai garis pangkal (*baseline*), tiga metode tangkas berbasis tim dan lokakarya (*RAD, Scrum, dan XP*), serta *Personal Extreme Programming (PxP)* sebagai metode terpilih khusus pengembang mandiri. Seluruh dimensi perbandingan dinilai secara objektif menggunakan parameter rekayasa perangkat lunak dan telah diverifikasi nomor halaman rujukannya pada literatur primer agar memudahkan pengecekan naskah asli secara langsung.

| Dimensi Analisis Komparatif | Waterfall (Sommerville, 2011, hlm. 30; Royce, 1970, hlm. 2) | RAD (Pratama dkk., 2023, hlm. 54; Pressman, 2010, hlm. 45) | Scrum (Schwaber & Sutherland, 2020, hlm. 5; Kurniawan & Sani, 2019, hlm. 149) | Extreme Programming / XP (Beck & Andres, 2004, hlm. 45; Williams dkk., 2000, hlm. 21) | Personal Extreme Programming / PxP [Terpilih] (Dzhurov dkk., 2009, hlm. 254; Fikri & Prabowo / ITK, 2020, hlm. 2) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ukuran Tim & Struktur Peran** | Tim skala menengah hingga besar dengan pemisahan peran yang kaku dan terspesialisasi (analis, desainer, pemrogram, dan penguji bekerja pada sekat departemen terpisah, Sommerville, 2011, hlm. 32). | Membutuhkan beberapa tim kecil yang bekerja secara paralel pada komponen modul yang berbeda (Pressman, 2010, hlm. 46). | Tim lintas-fungsi beranggotakan tiga hingga sembilan orang dengan kewajiban membagi tiga peran independen yang dilarang dirangkap (*Product Owner, Scrum Master, Developers*, Schwaber & Sutherland, 2020, hlm. 5 hingga 7). | Tim kecil pengembang (dua hingga sepuluh orang) yang secara mutlak diwajibkan bekerja berpasangan di stasiun kerja yang sama (*Pair Programming*, Beck & Andres, 2004, hlm. 56). | **Pengembang tunggal mandiri (*Autonomous Developer* / satu orang mahasiswa) yang menjalankan proses rekayasa secara disiplin tanpa bergantung pada kehadiran rekan kerja fisik (Dzhurov dkk., 2009, hlm. 252).** |
| **Tahapan Baku Proses** | Lima fase sekuensial linear baku:<br>1. Definisi Kebutuhan<br>2. Desain Sistem & Perangkat Lunak<br>3. Implementasi & Uji Unit<br>4. Integrasi & Uji Sistem<br>5. Operasi & Pemeliharaan<br>(Sommerville, 2011, hlm. 31; Royce, 1970, hlm. 2). | Tiga tahapan model Kendall:<br>1. Perencanaan Syarat-syarat (*Requirements Planning*)<br>2. Lokakarya Desain RAD (*RAD Design Workshop* mencakup Analisis & Desain Pemodelan)<br>3. Implementasi / Konstruksi Cepat<br>(Pratama dkk., 2023, hlm. 51 hingga 54). | Empat acara berulang dalam siklus Sprint (satu hingga empat minggu):<br>1. *Sprint Planning*<br>2. *Daily Scrum* (pertemuan harian 15 menit)<br>3. *Sprint Review* (inspeksi inkremen)<br>4. *Sprint Retrospective* (evaluasi internal)<br>(Schwaber & Sutherland, 2020, hlm. 7 hingga 12). | Empat siklus iterasi berkelanjutan:<br>1. *Planning* (penulisan *User Stories*)<br>2. *Simple Design* (solusi eksperimental *Spike*)<br>3. *Coding* (*Pair Programming* dan *TDD*)<br>4. *Testing* (uji unit otomatis dan *Acceptance Testing*)<br>(Beck & Andres, 2004, hlm. 45 hingga 60). | **Tujuh tahapan operasional terstruktur:<br>1. Kebutuhan (*Requirements*)<br>2. Perencanaan (*Task Planning & Estimation*)<br>3. Inisialisasi Iterasi (*Iteration Initialization*)<br>4. Perancangan (*Simple Design*)<br>5. Implementasi (*TDD, Code Generation, Refactoring*)<br>6. Pengujian Sistem (*Defect Log*)<br>7. Retrospeksi (*Time Log & PIP*)<br>(Dzhurov dkk., 2009, hlm. 254 hingga 256).** |
| **Manajemen Perubahan Kebutuhan** | Sangat kaku; seluruh spesifikasi dikunci di awal proyek sehingga perubahan di tengah jalan ditolak atau dikenakan biaya revisi yang sangat mahal (Mishra & Alzoubi, 2023, hlm. 886). | Cukup fleksibel selama perubahan masih dapat diakomodasi di dalam jadwal lokakarya perancangan (Pressman, 2010, hlm. 46). | Sangat adaptif di antara pergantian Sprint; namun butir pekerjaan yang sedang dikerjakan di dalam Sprint berjalan dilarang diubah (Schwaber & Sutherland, 2020, hlm. 8). | Sangat adaptif; perubahan kebutuhan disambut baik pada setiap awal iterasi mingguan tanpa penalti biaya desain (Beck & Andres, 2004, hlm. 20). | **Sangat adaptif dan terstruktur; perubahan kebutuhan operasional diakomodasi secara terencana di setiap awal iterasi baru (Dzhurov dkk., 2009, hlm. 255).** |
| **Frekuensi Rilis & Umpan Balik** | Rilis tunggal di akhir proyek; pengguna baru dapat melihat dan menguji perangkat lunak setelah seluruh tahapan konstruksi selesai secara tuntas (Royce, 1970, hlm. 3). | Rilis bertahap cepat dalam rentang waktu terpadat 60 hingga 90 hari melalui demonstrasi purwarupa hasil lokakarya (Pressman, 2010, hlm. 45). | Menghasilkan produk kerja yang berpotensi dirilis (*potentially releasable increment*) pada setiap akhir siklus Sprint (satu hingga empat minggu, Schwaber & Sutherland, 2020, hlm. 8). | Rilis berkala dalam siklus sangat pendek berdurasi satu hingga tiga minggu (*Small Releases*), sehingga umpan balik diperoleh dengan cepat (Beck & Andres, 2004, hlm. 48). | **Rilis bertahap fungsional (*Small Releases*) pada setiap akhir iterasi (satu hingga tiga minggu), sehingga mitra dapat langsung memverifikasi modul nyata (Dzhurov dkk., 2009, hlm. 253; Ramadhan, 2026, hlm. 92).** |
| **Tingkat Keterlibatan Pengguna** | Rendah; komunikasi intensif hanya terjadi di awal wawancara kebutuhan dan di akhir serah terima sistem (Sommerville, 2011, hlm. 31). | Sangat tinggi dan intensif; pengguna wajib hadir terus-menerus mengikuti lokakarya perancangan terpadu (*RAD Workshop*, Pratama dkk., 2023, hlm. 52). | Sangat aktif; perwakilan bisnis (*Product Owner*) mendampingi pengembang setiap hari kerja dan pemangku hadir di *Sprint Review* (Schwaber & Sutherland, 2020, hlm. 10). | Sangat ekstrem; menuntut pengguna resmi hadir mendampingi tim di lokasi meja kerja setiap hari (*On-site Customer*, Beck & Andres, 2004, hlm. 60). | **Proporsional dan efisien; pengguna terlibat dalam elisitasi kebutuhan awal dan evaluasi rilis modul di akhir iterasi tanpa membebani rutinitas pelayanan harian mitra (Dzhurov dkk., 2009, hlm. 256; Asri dkk., 2018, hlm. 286).** |
| **Disiplin Kualitas & Rekayasa** | Verifikasi kepatuhan terhadap dokumen spesifikasi dan pengujian fungsional sistem di akhir fase (Royce, 1970, hlm. 2). | Mengandalkan kualitas komponen pustaka siap pakai dan pengujian integrasi prototipe cepat (Pressman, 2010, hlm. 47). | Mengandalkan kesepakatan internal tim (*Definition of Done*) tanpa menyediakan standar baku rekayasa pengodean bawaan (Schwaber & Sutherland, 2020, hlm. 12). | Sangat ketat; mewajibkan *Test-Driven Development (TDD)*, refaktorisasi konstan, dan peninjauan kode seketika via *Pair Programming* (Williams dkk., 2000, hlm. 21). | **Sangat ketat dan mandiri; mengintegrasikan TDD, standar penulisan kode (*Coding Standard*), peninjauan kode personal (*Code Reviews*), dan pencatatan galat baku (*Defect Recording*) (Dzhurov dkk., 2009, hlm. 254).** |
| **Beban Dokumentasi & Metrik** | Sangat berat; setiap fase wajib ditutup oleh dokumen spesifikasi formal tebal yang ditandatangani bersama (Sommerville, 2011, hlm. 31). | Sedang; dokumentasi formal dipadatkan ke dalam bentuk diagram pemodelan visual dan purwarupa (Pratama dkk., 2023, hlm. 53). | Sangat ringan; artefak terbatas pada dokumen dinamis tim (*Product Backlog, Sprint Backlog*, dan grafik *Burndown Chart*, Schwaber & Sutherland, 2020, hlm. 11). | Sangat ringan; berpusat pada kartu cerita pengguna (*User Stories*) dan kumpulan kode pengujian otomatis (Beck & Andres, 2004, hlm. 46). | **Terukur, efisien, dan ilmiah; menghasilkan lembar metrik empiris berupa *Time Recording Log*, *Defect Recording Log*, dan usulan perbaikan alur (*PIP*) sebagai bukti riil skripsi (Dzhurov dkk., 2009, hlm. 254; Hasan, H. I., Marthasari, G. I., & Nuryasin, I. (2021). Implementasi Metode Personal Extreme Programming Dalam Pengembangan Sistem Administrasi Pelayanan Desa. REPOSITOR, 3(1), hlm. 43-50.
| **Kelayakan untuk Skripsi Solo Artha** | **TIDAK LAYAK:** Karakteristik operasional delapan cabang Bimbel Artha saat ini belum terstandarisasi tertulis; penguncian kebutuhan di awal berisiko menghasilkan sistem yang tidak relevan. | **TIDAK LAYAK:** Pengelola cabang sibuk mengajar setiap hari sehingga mustahil mengikuti lokakarya intensif, serta pembagian tim kerja paralel tidak mungkin dilakukan oleh satu orang. | **CACAT METODOLOGIS (*FLAWED*):** Aturan mutlak *Scrum Guide* melarang perangkapan peran. Mahasiswa tunggal tidak dapat membagi diri menjadi tiga peran dan tidak bisa menggelar rapat harian dengan dirinya sendiri. | **CACAT METODOLOGIS (*FLAWED*):** Dua syarat wajib XP (*Pair Programming* dan *On-site Customer*) secara fisik mustahil dipenuhi dalam pengerjaan skripsi mandiri dan kemitraan bimbel delapan cabang. | **SANGAT TEPAT & SAHIH (*PERFECT ALIGNMENT*):** Satu-satunya metodologi yang sah secara akademik untuk pengembang tunggal, menjamin mutu perangkat lunak tanpa tim fisik, dan selaras dengan ketersediaan waktu mitra. |

---

### Panduan Narasi Verbal: Cara Menjelaskan Tabel Komparasi kepada Dosen Pembimbing

Ketika mempresentasikan atau mempertahankan tabel komparasi ini di hadapan Dosen Pembimbing (Ibu Ayu atau Bapak Arif), gunakan alur penjelasan terstruktur dengan bahasa yang wajar, tegas, dan berlandaskan fakta ilmiah berikut. Penguasaan terhadap setiap butir argumentasi di bawah ini membuktikan kedalaman pemahaman metodologis Anda di hadapan penguji bahwa pemilihan metode didasarkan pada parameter teknis riil.

1. **Penjelasan Pembuka (Logika Spektrum Metode):**
   > *"Izin menjelaskan, Ibu/Bapak. Tabel komparasi ini saya susun untuk menyandingkan Personal Extreme Programming (PxP) tidak hanya terhadap Waterfall, melainkan terhadap metode-metode tangkas yang setara, yaitu RAD, Scrum, dan XP konvensional. Tujuannya adalah untuk membedah secara objektif pada tahapan proses mana metode-metode tersebut gugur ketika dihadapkan pada batasan pengerjaan skripsi mandiri dan karakteristik nyata operasional Bimbel Artha."*

2. **Argumen Menggugurkan Waterfall:**
   > *"Pertama, model Waterfall terbukti tidak layak karena mengasumsikan seluruh kebutuhan sistem dapat dikunci sejak awal melalui dokumen spesifikasi formal (Sommerville, 2011, hlm. 30). Fakta di lapangan menunjukkan bahwa delapan cabang Bimbel Artha belum memiliki standarisasi operasional tertulis, di mana pencatatan presensi, pembagian honor tentor, dan rekapitulasi SPP antarcabang masih berbeda-beda. Memaksakan Waterfall akan menimbulkan risiko kegagalan sistem yang sangat fatal apabila mitra menginginkan penyesuaian alur kerja di tengah penelitian."*

3. **Argumen Menggugurkan RAD:**
   > *"Kedua, metode RAD kami tolak karena keberhasilannya bertumpu pada kehadiran aktif pengguna dalam lokakarya perancangan terpadu (RAD Design Workshop) secara terus-menerus (Pratama dkk., 2023, hlm. 52). Mitra kami, yaitu koordinator dan kepala cabang Bimbel Artha, disibukkan oleh kegiatan pengajaran dan operasional harian bimbingan belajar sehingga mustahil diwajibkan meluangkan waktu setiap minggu untuk lokakarya pemodelan intensif. Selain itu, RAD mengasumsikan pengerjaan komponen oleh beberapa tim paralel yang tidak mungkin diwujudkan oleh pengembang tunggal."*

4. **Argumen Menggugurkan Scrum (Poin Cacat Metodologis):**
   > *"Ketiga, kerangka kerja Scrum secara tegas melarang perangkapan peran guna menjaga objektivitas kendali proses empiris (Schwaber & Sutherland, 2020, hlm. 5 hingga 7). Dalam pengerjaan skripsi yang bersifat mandiri, menerapkan Scrum akan menciptakan rekayasa peran semu di mana saya harus bertindak sebagai Product Owner, merangkap Scrum Master, dan melakukan evaluasi harian (Daily Scrum) dengan diri saya sendiri. Hal ini merupakan bentuk cacat metodologis yang tidak dapat dipertanggungjawabkan secara akademik."*

5. **Argumen Menggugurkan Extreme Programming (XP):**
   > *"Keempat, Extreme Programming konvensional memiliki disiplin kode yang sangat bagus, namun dua praktik intinya tidak dapat dipenuhi dalam penelitian ini, yaitu Pair Programming yang menuntut dua pemrogram di satu stasiun kerja (Beck & Andres, 2004, hlm. 56) dan On-site Customer yang menuntut mitra hadir setiap hari mendampingi mahasiswa (Williams dkk., 2000, hlm. 21). Sebagai mahasiswa pengembang tunggal dan mitra pemilik bimbel yang memiliki mobilitas tinggi dalam memantau delapan cabangnya, kedua prasyarat mutlak XP tersebut tidak dapat terlaksana."*

6. **Kesimpulan Kemenangan PxP:**
   > *"Kelima, Personal Extreme Programming (PxP) hadir sebagai satu-satunya solusi yang sah dan proporsional. PxP diciptakan secara resmi oleh Yani Dzhurov dkk. (2009, hlm. 252) untuk pengembang mandiri (Autonomous Developer). PxP mengganti Pair Programming dengan disiplin Test-Driven Development (TDD), standar pengodean, dan peninjauan kode mandiri (Personal Code Reviews), sementara kehadiran mitra diakomodasi secara berkala melalui rilis fungsional bertahap (Small Releases) di setiap akhir iterasi. Dengan demikian, kualitas sistem tetap terjaga tinggi, mitra tidak terbebani birokrasi harian, dan saya memiliki bukti metrik empiris berupa Time Log dan Defect Log yang valid untuk sidang Tugas Akhir."*

---

## 4. MATRIKS ARGUMENTASI DEFENSIVE (REBUTTAL MATRIX) MENGHADAPI PENGUJI

Bagian ini memuat panduan tanggapan ilmiah terstruktur yang dapat disampaikan kepada Dosen Pembimbing atau Penguji (Ibu Ayu) apabila beliau mempertanyakan mengapa peneliti tidak memilih metode-metode konvensional atau metode populer lainnya. Setiap tanggapan dirumuskan dengan menyandingkan landasan teoretis dari literatur standar beserta nomor halaman spesifik melawan fakta empiris yang dihadapi di lapangan. Pendekatan argumentasi ini menunjukkan kedalaman pemahaman peneliti bahwa penolakan terhadap suatu metode bukan didasarkan pada preferensi subjektif, melainkan atas dasar analisis ketidaksesuaian parameter operasional.

```
                    SKENARIO PERTANYAAN KRITIS PENGUJI
                                    |
   +--------------------------------+--------------------------------+
   |                                |                                |
[MENGAPA BUKAN WATERFALL?]    [MENGAPA BUKAN SCRUM?]       [MENGAPA BUKAN XP / RAD?]
- 8 Cabang dinamis           - Cacat metodologis:         - XP butuh 2 orang (Pair)
- Dokumen awal belum ada       Solo developer tidak       - RAD butuh workshop harian
- Risiko salah analisis        bisa bagi 3 peran            yang mustahil bagi mitra
```

### 4.1 Pertanyaan Penguji: "Mengapa Anda tidak menggunakan Waterfall yang lebih umum dan terstruktur untuk skripsi?"

**Tanggapan Peneliti:**

> "Berdasarkan rujukan Ian Sommerville (2011, hlm. 30 hingga 32) serta kajian empiris Susanto & Andriana (2016, hlm. 331 hingga 333), metode Waterfall mensyaratkan spesifikasi kebutuhan sistem yang telah stabil, jelas, dan terdokumentasi lengkap sejak awal proyek. Kondisi empiris pada mitra Bimbingan Belajar Artha Balikpapan menunjukkan bahwa proses bisnis pada delapan cabang saat ini belum terstandarisasi secara tertulis, di mana pencatatan presensi, pembagian jadwal honor pengajar, dan mutasi iuran siswa masih bervariasi antarcabang. Apabila saya memaksakan Waterfall, setiap perubahan kebutuhan administratif yang baru disadari oleh pihak mitra di tengah jalan akan menimbulkan penolakan sistem atau biaya pembongkaran kode yang sangat tinggi (Mishra & Alzoubi, 2023, hlm. 886). Selain itu, hasil studi Asri, Fajri, & Syahrul (2018, hlm. 286 hingga 288) yang membandingkan Waterfall dan PxP pada sistem kerja praktik membuktikan bahwa PxP jauh lebih adaptif dan memiliki tingkat keberhasilan penyelesaian yang lebih tinggi dibandingkan Waterfall dalam menghadapi perubahan kebutuhan pengguna di lapangan."

### 4.2 Pertanyaan Penguji: "Mengapa tidak menggunakan Scrum yang saat ini menjadi standar industri perangkat lunak?"

**Tanggapan Peneliti:**

> "Mengacu pada panduan resmi _The Scrum Guide_ oleh Ken Schwaber & Jeff Sutherland (2020, hlm. 5 hingga 7), kerangka kerja Scrum secara absolut mewajibkan pembagian tiga peran independen, yaitu _Product Owner_, _Scrum Master_, dan _Developers_ dengan ukuran tim pengembang ideal 3 hingga 9 orang. Aturan fundamental Scrum melarang perangkapan peran guna menjaga transparansi dan objektivitas inspeksi. Karena penelitian Tugas Akhir ini dilaksanakan oleh saya sendiri sebagai pengembang mandiri (_solo developer_), penerapan Scrum secara literal akan menimbulkan cacat metodologis yang fatal, di mana saya harus merekayasa peran _Product Owner_, memimpin _Daily Scrum_ dengan diri sendiri, dan mengawasi diri sendiri sebagai _Scrum Master_ (Mahnic, 2018, hlm. 127). Oleh sebab itu, Personal Extreme Programming (PxP) dipilih karena memang diciptakan oleh Dzhurov, Krasteva, & Ilieva (2009, hlm. 252 hingga 254) khusus untuk mengadaptasi nilai-nilai ketangkasan industri ke dalam konteks pengembang tunggal tanpa mengorbankan integritas metodologi penelitian."

### 4.3 Pertanyaan Penguji: "Mengapa Anda tidak memilih Extreme Programming (XP) konvensional saja?"

**Tanggapan Peneliti:**

> "Extreme Programming klasik yang dirumuskan oleh Kent Beck (2004, hlm. 45 hingga 60) bertumpu pada dua pilar kerja tim yang sangat ketat, yaitu _Pair Programming_ (dua pemrogram bekerja bersama di depan satu komputer secara konstan) dan _On-site Customer_ (perwakilan pengguna duduk bersama pengembang setiap hari). Dalam konteks pengerjaan Tugas Akhir, kehadiran pemrogram kedua untuk berpasangan secara fisik mustahil dipenuhi karena skripsi adalah karya perorangan (Agarwal & Umphress, 2008, hlm. 83). Di sisi lain, pemilik Bimbel Artha memiliki keterbatasan waktu yang sangat tinggi karena harus mengontrol operasional delapan cabang, sehingga tidak dapat menjadi _On-site Customer_ setiap hari. PxP memecahkan masalah ini dengan mengganti _Pair Programming_ melalui peninjauan kode mandiri yang disiplin (_Code Reviews_), otomatisasi _Test-Driven Development_ (TDD), serta pencatatan log cacat program (_Defect Recording_) dari PSP, sementara umpan balik pengguna diakomodasi melalui rilis skala kecil (_Small Releases_) di setiap akhir iterasi (Dzhurov dkk., 2009, hlm. 254; Fikri & Prabowo / ITK, 2020, hlm. 2)."

### 4.4 Pertanyaan Penguji: "Mengapa tidak memakai RAD agar aplikasi cepat selesai dalam waktu singkat?"

**Tanggapan Peneliti:**

> "Berdasarkan pemodelan Pratama, Hidayat, & Nurfaizah (2023, hlm. 51 hingga 54) serta telaah Roger S. Pressman (2010, hlm. 45 hingga 47), keberhasilan metode RAD bertumpu pada pelaksanaan _RAD Design Workshop_ yang intensif, di mana pengguna dan pengembang wajib duduk bersama secara berulang dalam sesi pemodelan interaktif. Mitra Bimbel Artha tidak memiliki sumber daya manusia yang dapat dilepaskan dari tugas operasional harian untuk mengikuti lokakarya yang intensif tersebut. Selain itu, RAD mengasumsikan pembangunan modul dapat dipecah ke dalam beberapa tim kerja paralel (_multiple component teams_). Karena saya bekerja sendirian, pembagian tim paralel tidak dapat diwujudkan. PxP jauh lebih fleksibel karena pengumpulan umpan balik dilakukan secara bertahap melalui evaluasi hasil rilis fungsional pada akhir setiap iterasi tanpa mengganggu jalannya operasional bimbel mitra."

### 4.5 Pertanyaan Penguji: "Mengapa tidak menggunakan Prototyping murni yang berfokus pada antarmuka?"

**Tanggapan Peneliti:**

> "Sebagaimana diuraikan oleh Ian Sommerville (2011, hlm. 44 hingga 46), kelemahan mendasar dari model Prototyping murni adalah kecenderungan pengembang untuk mengabaikan kebutuhan non-fungsional kritis, seperti keamanan hak akses data, integritas relasi basis data, dan keteraturan struktur kode internal demi mengejar tampilan antarmuka yang cepat (_code degradation_). Sistem Bimbel Artha mengelola data transaksional finansial yang sensitif pada delapan cabang, sehingga integritas data dan keamanan sistem merupakan harga mati. PxP mengintegrasikan teknik pembuatan prototipe pada tahap perancangan antarmukanya, namun menguncinya dengan praktik _Simple Design_, _Refactoring_, dan _Test-Driven Development_ (TDD), sehingga antarmuka yang dihasilkan tetap didukung oleh fondasi arsitektur perangkat lunak yang kokoh dan bebas dari kerentanan struktural (Dzhurov dkk., 2009, hlm. 254; Priatmaja dkk., 2022, hlm. 3 hingga 5)."

### 4.6 Pertanyaan Penguji: "Mengapa tidak memilih Kanban yang alurnya sangat fleksibel dan tanpa beban iterasi?"

**Tanggapan Peneliti:**

> "Berdasarkan panduan resmi Todd Coleman & Daniel S. Vacanti (2025, hlm. 3 hingga 6) dalam _The Kanban Guide_, Kanban merupakan kerangka kerja manajemen aliran operasional yang tidak menyertakan pedoman teknis rekayasa perangkat lunak sama sekali, seperti standarisasi kode, pengujian unit terotomasi, maupun refaktorisasi arsitektur. Selain itu, skripsi Tugas Akhir menuntut adanya batasan waktu dan tonggak pencapaian yang terukur untuk menilai kemajuan fungsionalitas sistem secara objektif. Ketiadaan siklus waktu tetap (_timebox_) pada Kanban berisiko mengaburkan evaluasi progres kerja perorangan. PxP tetap mengadopsi prinsip visualisasi aliran kerja ala Kanban dalam pelacakan tugas teknisnya, namun melengkapinya dengan disiplin siklus rilis 1 hingga 3 minggu serta rangkaian praktik pengujian perangkat lunak yang teruji secara akademik (Mahnic, 2018, hlm. 128 hingga 130; Dzhurov dkk., 2009, hlm. 254)."

---

## 5. KESIMPULAN DAN SINTESIS JUSTIFIKASI PEMILIHAN METODE PxP

Berdasarkan keseluruhan kajian pustaka, telaah perbandingan komparatif, serta analisis kesesuaian kasus mitra, dapat dirumuskan empat landasan ilmiah utama dalam pemilihan metodologi. Landasan ini membuktikan bahwa Personal Extreme Programming (PxP) merupakan satu-satunya kerangka kerja yang paling sahih, realistis, dan dapat dipertanggungjawabkan secara akademik untuk Tugas Akhir ini. Keempat pilar argumentasi tersebut diuraikan sebagai berikut:

1. **Integritas Metodologi Pengembang Tunggal (Solo Developer Fit):** PxP diakui secara luas dalam literatur rekayasa perangkat lunak internasional (Dzhurov dkk., 2009, hlm. 252; Agarwal & Umphress, 2008, hlm. 83; Iyawa, 2020, hlm. 2) dan sivitas akademika Sistem Informasi ITK (Fikri & Prabowo / ITK, 2020, hlm. 2; Priatmaja dkk., 2022, hlm. 2; Hasan, H. I., Marthasari, G. I., & Nuryasin, I. (2021). Implementasi Metode Personal Extreme Programming Dalam Pengembangan Sistem Administrasi Pelayanan Desa. REPOSITOR, 3(1), hlm. 43-50.
2. **Kesesuaian dengan Karakteristik Mitra Delapan Cabang:** PxP membagi pengembangan ke dalam iterasi fungsional pendek berdurasi 1 hingga 3 minggu (Dzhurov dkk., 2009, hlm. 255). Pola rilis kecil (_Small Releases_) ini memungkinkan pengelola Bimbel Artha mengevaluasi prototipe modul (seperti modul presensi, penggajian, dan pendaftaran) secara bertahap di sela-sela kesibukan operasional tanpa membebani rutinitas harian mereka.
3. **Penjaminan Mutu Perangkat Lunak Secara Mandiri:** Dengan meniadakan ketergantungan pada pemrogram kedua (_pair programming_), PxP mempertahankan standar mutu kode internal yang sangat tinggi melalui perpaduan _Test-Driven Development (TDD)_, peninjauan kode mandiri (_Code Reviews_), dan _Continuous Integration_ (Williams dkk., 2000, hlm. 21; Dzhurov dkk., 2009, hlm. 254). Hal ini menjamin bahwa sistem operasional multi-cabang yang dibangun memiliki ketahanan teknis yang andal dan minim galat.
4. **Ketersediaan Bukti Metrik Empiris untuk Pertanggungjawaban Sidang:** PxP mewajibkan pencatatan metrik kerja harian melalui lembar _Time Recording Log_, _Defect Recording Log_, dan dokumen _Process Improvement Proposal (PIP)_ (Dzhurov dkk., 2009, hlm. 256; Hasan, H. I., Marthasari, G. I., & Nuryasin, I. (2021). Implementasi Metode Personal Extreme Programming Dalam Pengembangan Sistem Administrasi Pelayanan Desa. REPOSITOR, 3(1), hlm. 43-50.

---

## 6. DAFTAR PUSTAKA ACUAN (VERIFIKASI REPOSITORI RISET LOKAL)

- Agarwal, R., & Umphress, D. (2008). Extreme Programming for a Single Person Team. _Proceedings of the 46th Annual Southeast Regional Conference on XX (ACM-SE 46)_, hlm. 82 hingga 87. https://doi.org/10.1145/1593105.1593127. Berkas Ekstraksi: [Extreme programming for a single person team - Agarwal & Umphress - 2008.txt](./JURNAL/HASIL%20EKSTRAK%20JURNAL/Extreme%20programming%20for%20a%20single%20person%20team%20-%20Agarwal%20&%20Umphress%20-%202008.txt).
- Apriyanti, N., Fitri Ana Wati, S., & Rezha Efrat Najaf, A. (2024). Pemanfaatan Metodologi PXP dan Pengujian User Acceptance Testing (UAT) dalam Pengembangan Website E-Kavling. _JATI (Jurnal Mahasiswa Teknik Informatika)_, 8(3), hlm. 3678 hingga 3686. https://doi.org/10.36040/jati.v8i3.9766<br>
     ↳ <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/Website%20E-Kavling%20-%20PxP%20&%20UAT%20-%20JATI%20-%20Apriyanti%20dkk%20-%202024.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Website%20E-Kavling%20-%20PxP%20&%20UAT%20-%20JATI%20-%20Apriyanti%20dkk%20-%202024.txt">📝 Buka Teks Ekstraksi</a>
- Asri, M., Fajri, R., & Syahrul. (2018). PxP vs Waterfall: Web-Based Application for Job Training Activities Using Personal Extreme Programming (PXP). _Proceedings of the 2nd International Conference on Applied Science and Technology (ICST 2018)_, hlm. 284 hingga 288<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/PxP%20vs%20Waterfall%20-%20Job%20Training%20App%20-%20ICST%202018%20-%20Asri%20dkk%20-%202018.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/PxP%20vs%20Waterfall%20-%20Job%20Training%20App%20-%20ICST%202018%20-%20Asri%20dkk%20-%202018.txt">📝 Buka Teks Ekstraksi</a>
- Beck, K., & Andres, C. (2004). _Extreme Programming Explained: Embrace Change (2nd ed.)_. Boston: Addison-Wesley. (hlm. 13 hingga 64)<br>
     ↳ <a href="./JURNAL/BUKU/Extreme-Programming-Explained-2nd-Edition-Kent-Beck.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/HASIL%20EKSTRAK%20BUKU/Extreme-Programming-Explained-2nd-Edition-Kent-Beck.txt">📝 Buka Teks Ekstraksi</a>
- Boehm, B. W. (1988). A Spiral Model of Software Development and Enhancement. _Computer_, 21(5), hlm. 61 hingga 72. https://doi.org/10.1109/2.59<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/A%20Spiral%20Model%20of%20Software%20Development%20and%20Enhancement%20-%20Prototyping%20-%20Boehm%20-%201988.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/A%20Spiral%20Model%20of%20Software%20Development%20and%20Enhancement%20-%20Prototyping%20-%20Boehm%20-%201988.txt">📝 Buka Teks Ekstraksi</a>
- Coleman, T., & Vacanti, D. S. (2025). _The Kanban Guide_. KanbanGuides.org. (hlm. 1 hingga 6)<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/The%20Kanban%20Guide%20-%20Panduan%20Resmi%20Kanban%20-%20Coleman%20&%20Vacanti%20-%202025.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/The%20Kanban%20Guide%20-%20Panduan%20Resmi%20Kanban%20-%20Coleman%20&%20Vacanti%20-%202025.txt">📝 Buka Teks Ekstraksi</a>
- Dzhurov, Y., Krasteva, I., & Ilieva, S. (2009). Personal Extreme Programming: An Agile Process for Autonomous Developers. _Proceedings of the 1st International Conference on Software, Services & Semantic Technologies (S3T 2009)_, hlm. 252 hingga 259<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Personal%20Extreme%20Programming%20-%20Agile%20for%20Autonomous%20Developer%20-%20S3T%202009%20-%20Dzhurov%20dkk%20-%202009.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Personal%20Extreme%20Programming%20-%20Agile%20for%20Autonomous%20Developer%20-%20S3T%202009%20-%20Dzhurov%20dkk%20-%202009.txt">📝 Buka Teks Ekstraksi</a>
- Fahrijal, M., & Hartawan, M. B. (2024). Perbandingan XP vs PxP pada Implementasi Software. _Jurnal Ilmiah Sistem Informasi_, 6(2), hlm. 154 hingga 162<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Perbandingan%20XP%20vs%20PxP%20pada%20Implementasi%20Software%20-%20Fahrijal%20&%20Hartawan%20-%202024.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Perbandingan%20XP%20vs%20PxP%20pada%20Implementasi%20Software%20-%20Fahrijal%20&%20Hartawan%20-%202024.txt">📝 Buka Teks Ekstraksi</a>
- Fikri, M. R., & Prabowo, R. D. A. (2020). Rancang Bangun Sistem Informasi Buku Tamu DPOP Balikpapan dengan Metode Personal Extreme Programming. _Jurnal Sistem Informasi ITK_, hlm. 1 hingga 11<br>
     ↳ <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Buku%20Tamu%20DPOP%20Balikpapan%20-%20PxP%20-%20Fikri%20&%20Prabowo%20(ITK)%20-%202020.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Buku%20Tamu%20DPOP%20Balikpapan%20-%20PxP%20-%20Fikri%20&%20Prabowo%20(ITK)%20-%202020.txt">📝 Buka Teks Ekstraksi</a>
- Iyawa, G. E. (2020). Personal Extreme Programming: Exploring Developers' Adoption. _Proceedings of the 26th Americas Conference on Information Systems (AMCIS 2020)_, hlm. 1 hingga 10<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Personal%20Extreme%20Programming%20Exploring%20Developers%20Adoption%20-%20AMCIS%20-%20Iyawa%20-%202020.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Personal%20Extreme%20Programming%20Exploring%20Developers%20Adoption%20-%20AMCIS%20-%20Iyawa%20-%202020.txt">📝 Buka Teks Ekstraksi</a>
- Khan, T. U. R., Rehman, S. U., & Ahmad, F. (2011). A Comparative Study of Heavyweight and Lightweight Software Methodologies. _International Journal of Computer Science and Network Security (IJCSNS)_, 11(8), hlm. 94 hingga 100<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Perbandingan%20Heavy%20&%20Lightweight%20Methodology%20-%20Khan%20dkk%20-%202011.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Perbandingan%20Heavy%20&%20Lightweight%20Methodology%20-%20Khan%20dkk%20-%202011.txt">📝 Buka Teks Ekstraksi</a>
- Kuhrmann, M., Tell, P., Hebig, R., Klünder, J., Münch, J., Linssen, O., Pfahl, D., Felderer, M., Prause, C. R., MacDonell, S. G., Nakatumba-Nabende, J., & Raffo, D. (2021). What Makes Agile Software Development Agile?. _Empirical Software Engineering_, 26(6), hlm. 1 hingga 46. https://doi.org/10.1007/s10664-021-10005-7<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Adoption%20and%20Suitability%20of%20Software%20Development%20Methods%20-%20Empirical%20Study%20-%20Kuhrmann%20dkk%20-%202021.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Adoption%20and%20Suitability%20of%20Software%20Development%20Methods%20-%20Empirical%20Study%20-%20Kuhrmann%20dkk%20-%202021.txt">📝 Buka Teks Ekstraksi</a>
- Kurniawan, D., & Sani, R. R. (2019). Pemodelan SCRUM Sistem Informasi Pelayanan Kesehatan Klinik Gigi Ar-Rokhim Semarang. _JOINS (Journal of Information Systems)_, 4(2), hlm. 146 hingga 156<br>
     ↳ <a href="./JURNAL/04_FITUR_DAN_TEKNOLOGI_PENDUKUNG/Pemodelan%20SCRUM%20Klinik%20Ar-Rokhim%20-%20JOINS%20-%20Kurniawan%20&%20Sani%20-%202019.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Pemodelan%20SCRUM%20Klinik%20Ar-Rokhim%20-%20JOINS%20-%20Kurniawan%20&%20Sani%20-%202019.txt">📝 Buka Teks Ekstraksi</a>
- Mahnic, B. (2018). Scrum2Kanban: Integrating Kanban and Scrum in a Software Engineering Capstone Course. _IEEE Transactions on Education_, 61(2), hlm. 126 hingga 133 (PDF hlm. 13 hingga 20)<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Scrum2Kanban%20-%20Integrating%20Kanban%20and%20Scrum%20in%20Capstone%20Course%20-%20IEEE%20-%20Mahnic%20-%202018.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Scrum2Kanban%20-%20Integrating%20Kanban%20and%20Scrum%20in%20Capstone%20Course%20-%20IEEE%20-%20Mahnic%20-%202018.txt">📝 Buka Teks Ekstraksi</a>
- Mishra, A., & Alzoubi, Y. I. (2023). Structured versus Agile Software Development: A Comparative Analysis of Key Features. _Software Quality Journal_, 31, hlm. 881 hingga 923. https://doi.org/10.1007/s11219-023-09622-4<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Structured%20vs%20Agile%20Development%20Comparative%20Analysis%20-%20Mishra%20&%20Alzoubi%20-%20Springer%20-%202023.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Structured%20vs%20Agile%20Development%20Comparative%20Analysis%20-%20Mishra%20&%20Alzoubi%20-%20Springer%20-%202023.txt">📝 Buka Teks Ekstraksi</a>
- Poppendieck, M., & Poppendieck, T. (2003). _Lean Software Development: An Agile Toolkit_. Boston: Addison-Wesley. (hlm. xxiii hingga xxvii, 1 hingga 10, PDF hlm. 26 hingga 29)<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Lean%20Software%20Development%20-%20An%20Agile%20Toolkit%20-%20Poppendieck%20-%202003.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Lean%20Software%20Development%20-%20An%20Agile%20Toolkit%20-%20Poppendieck%20-%202003.txt">📝 Buka Teks Ekstraksi</a>
- Pratama, B. C., Hidayat, T., & Nurfaizah. (2023). Penerapan Metode Rapid Application Development (RAD) pada Sistem Informasi Inventarisasi Aset Desa Rempoah. _Infotek: Jurnal Informatika dan Teknologi_, 6(1), hlm. 49 hingga 59. https://doi.org/10.29408/jit.v6i1.7313<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Penerapan%20Metode%20RAD%20-%20Infotek%20-%20Pratama%20dkk%20-%202023.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Inventaris%20Aset%20Desa%20-%20RAD%20-%20Pratama%20dkk%20-%202023.txt">📝 Buka Teks Ekstraksi</a>
- Pressman, R. S. (2010). _Software Engineering: A Practitioner's Approach (7th ed.)_. New York: McGraw-Hill. (Bab 2 mengenai _Process Models_, hlm. 30 hingga 60)<br>
     ↳ <a href="./JURNAL/BUKU/ebook-pressman-sw-engineering.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/HASIL%20EKSTRAK%20BUKU/ebook-pressman-sw-engineering.txt">📝 Buka Teks Ekstraksi</a>
- Priatmaja, B., Prabowo, R. D. A., & Ginanjar. (2022). Pengembangan Sistem Informasi Laboratorium Infokom Menggunakan Personal Extreme Programming. _REPOSITOR_, 4(1), hlm. 1 hingga 10<br>
     ↳ <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Laboratorium%20Infokom%20-%20PxP%20-%20REPOSITOR%20-%20Priatmaja%20dkk%20-%202022.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Laboratorium%20Infokom%20-%20PxP%20-%20REPOSITOR%20-%20Priatmaja%20dkk%20-%202022.txt">📝 Buka Teks Ekstraksi</a>
- Putra, F. K. (2022). Sistem Informasi Presensi Pegawai Berbasis Web Menggunakan Metode Prototyping. _Journal of Information System Research (JOSH)_, 3(4), hlm. 431 hingga 436. https://doi.org/10.47065/josh.v3i4.1835<br>
     ↳ <a href="./JURNAL/04_FITUR_DAN_TEKNOLOGI_PENDUKUNG/SI%20Absensi%20-%20Web%20-%20Prototyping%20-%20Putra%20-%202022.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Absensi%20-%20Web%20-%20Prototyping%20-%20Putra%20-%202022.txt">📝 Buka Teks Ekstraksi</a>
- Ramadhan, M. R. (2026). Sistem Informasi Keanggotaan dan Penjadwalan Menggunakan Metode PxP. _Jurnal Riset Sistem Informasi_, 8(1), hlm. 88 hingga 99<br>
     ↳ <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Keanggotaan%20&%20Jadwal%20-%20PxP%20-%20Ramadhan%20-%202026.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Keanggotaan%20&%20Jadwal%20-%20PxP%20-%20Ramadhan%20-%202026.txt">📝 Buka Teks Ekstraksi</a>
- Royce, W. W. (1970). Managing the Development of Large Software Systems. _Proceedings of IEEE WESCON_, 26, hlm. 1 hingga 9<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Managing%20the%20Development%20of%20Large%20Software%20Systems%20-%20Waterfall%20-%20WESCON%20-%20Royce%20-%201970.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Managing%20the%20Development%20of%20Large%20Software%20Systems%20-%20Waterfall%20-%20WESCON%20-%20Royce%20-%201970.txt">📝 Buka Teks Ekstraksi</a>
- Schwaber, K. (1995). SCRUM Development Process. _Proceedings of OOPSLA 1995_, hlm. 1 hingga 10<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/SCRUM%20Development%20Process%20-%20OOPSLA%20-%20Schwaber%20-%201995.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SCRUM%20Development%20Process%20-%20OOPSLA%20-%20Schwaber%20-%201995.txt">📝 Buka Teks Ekstraksi</a>
- Schwaber, K., & Sutherland, J. (2020). _The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game_. Scrum.org. (hlm. 1 hingga 13)<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Scrum%20Guide%202020%20-%20Schwaber%20&%20Sutherland%20-%20Official.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Scrum%20Guide%202020%20-%20Schwaber%20&%20Sutherland%20-%20Official.txt">📝 Buka Teks Ekstraksi</a>
- Hasan, H. I., Marthasari, G. I., & Nuryasin, I. (2021). Implementasi Metode Personal Extreme Programming Dalam Pengembangan Sistem Administrasi Pelayanan Desa. REPOSITOR, 3(1), hlm. 43-50.
     ↳ <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Surat%20Menyurat%20-%20Personal%20Extreme%20Programming%20(PxP)%20-%20Hasan, H. I., Marthasari, G. I., & Nuryasin, I. (2021). Implementasi Metode Personal Extreme Programming Dalam Pengembangan Sistem Administrasi Pelayanan Desa. REPOSITOR, 3(1), hlm. 43-50.
- Sommerville, I. (2011). _Software Engineering (9th ed.)_. Boston: Addison-Wesley. (hlm. 28 hingga 88)<br>
     ↳ <a href="./JURNAL/BUKU/Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/HASIL%20EKSTRAK%20BUKU/Software-Engineering-9th-Edition-by-Ian-Sommerville.txt">📝 Buka Teks Ekstraksi</a>
- Susanto, R., & Andriana, A. D. (2016). Perbandingan Model Waterfall dan Prototyping untuk Pengembangan Sistem Informasi. _Majalah Ilmiah UNIKOM_, 14(1), hlm. 41 hingga 46<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Perbandingan%20Waterfall%20dan%20Prototyping%20-%20UNIKOM%20-%20Susanto%20&%20Andriana%20-%202016.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Perbandingan%20Waterfall%20dan%20Prototyping%20-%20UNIKOM%20-%20Susanto%20&%20Andriana%20-%202016.txt">📝 Buka Teks Ekstraksi</a>
- Suputra, I. G. A., dkk. (2026). Sistem Informasi Siswa SMP Berbasis Extreme Programming. _Jurnal Teknologi Informasi_, 10(1), hlm. 75 hingga 84<br>
     ↳ <a href="./JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI%20Siswa%20SMP%20-%20Extreme%20Programming%20(XP)%20-%20Suputra%20dkk%20-%202026.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/SI%20Siswa%20SMP%20-%20Extreme%20Programming%20(XP)%20-%20Suputra%20dkk%20-%202026.txt">📝 Buka Teks Ekstraksi</a>
- Williams, L., Kessler, R. R., Cunningham, W., & Jeffries, R. (2000). Strengthening the Case for Pair Programming. _IEEE Software_, 17(4), hlm. 19 hingga 25. https://doi.org/10.1109/52.854064<br>
     ↳ <a href="./JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Strengthening%20the%20Case%20for%20Pair%20Programming%20-%20IEEE%20Software%20-%20Williams%20dkk%20-%202000.pdf">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="./JURNAL/HASIL%20EKSTRAK%20JURNAL/Strengthening%20the%20Case%20for%20Pair%20Programming%20-%20IEEE%20Software%20-%20Williams%20dkk%20-%202000.txt">📝 Buka Teks Ekstraksi</a>
