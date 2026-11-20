# ABSTRAK DAN ABSTRACT PROPOSAL TUGAS AKHIR
**PROGRAM STUDI SISTEM INFORMASI — INSTITUT TEKNOLOGI KALIMANTAN**

---

### Catatan Penyelarasan Kata Kunci (*Keywords*)

Terkait pertanyaan apakah kata kunci pada versi Bahasa Indonesia dan Bahasa Inggris sama atau berbeda:
* **Secara substansi konsep, kata kuncinya sama persis**, karena kata kunci berfungsi sebagai indeks pengelompokan topik penelitian.
* **Secara linguistik, kata kunci diterjemahkan ke dalam padanan istilah akademis bahasa Inggris internasional** yang lazim digunakan pada repositori dan jurnal ilmiah bereputasi.
* Format penulisan kata kunci mengikuti ketentuan Panduan Tugas Akhir ITK 2026, yaitu terdiri atas maksimal 5 kata kunci dan diakhiri dengan kata penghubung *"dan"* (pada versi Indonesia) serta *"and"* (pada versi Inggris).

Berikut adalah pemetaan kata kuncinya:
1. **Bimbingan Belajar** $\rightarrow$ *Tutoring Center*
2. **Manajemen Operasional Multicabang** $\rightarrow$ *Multi-Branch Operational Management*
3. ***Personal Extreme Programming*** $\rightarrow$ *Personal Extreme Programming*
4. ***Role-Based Access Control*** $\rightarrow$ *Role-Based Access Control*
5. **Sistem Informasi Berbasis Web** $\rightarrow$ *Web-Based Information System*

---

## 1. Naskah Halaman 11: ABSTRAK (Bahasa Indonesia — Tepat 275 Kata)

**RANCANG BANGUN SISTEM INFORMASI MANAJEMEN OPERASIONAL BIMBINGAN BELAJAR BERBASIS WEB MENGGUNAKAN METODE PERSONAL EXTREME PROGRAMMING (STUDI KASUS: BIMBEL ARTHA BALIKPAPAN)**

Nama Mahasiswa: Ariel Itsbat Nurhaq  
NIM: 10231018  
Dosen Pembimbing Utama: Arif Wicaksono Septyanto, M.Kom.  
Dosen Pembimbing Pendamping: Sri Rahayu Natasia, S.Komp., M.Si., M.Sc.  

**ABSTRAK**

Bimbingan Belajar (Bimbel) Artha Balikpapan merupakan lembaga pendidikan nonformal yang mengelola delapan kantor cabang aktif dengan 60 tentor dan 2.400 siswa di Kota Balikpapan, namun pengelolaan operasionalnya masih manual menggunakan formulir kertas, buku besar fisik, kuitansi kertas, serta penagihan melalui WhatsApp dengan mencari nomor kontak orang tua satu per satu secara manual. Kondisi ini menyebabkan tingginya beban kerja staf cabang, risiko selisih perhitungan kas harian, keterlambatan pelacakan siswa yang menunggak Sumbangan Pembinaan Pendidikan (SPP) bulanan, dan ketiadaan laporan keuangan terpusat bagi pemilik lembaga. Penelitian ini bertujuan merancang dan membangun prototipe sistem informasi manajemen operasional bimbingan belajar multicabang berbasis web untuk mendigitalisasi empat fungsi utama, yaitu pendaftaran siswa baru, pencatatan transaksi kasir cabang, verifikasi bukti transfer pembayaran, dan rekonsiliasi kas harian terpusat. Dampak fungsional sistem ini adalah meningkatkan efisiensi kerja administrasi dan akurasi pencatatan keuangan multicabang. Konsep desain sistem dimodelkan melalui *Business Process Model and Notation* (BPMN), *Use Case Diagram*, *Activity Diagram*, *Entity Relationship Diagram* (ERD), antarmuka Next.js dan Tailwind CSS, *backend* Laravel RESTful API, serta basis data MySQL. Metode implementasi yang digunakan adalah *Personal Extreme Programming* (PXP) yang adaptif untuk pengembang individu, menghasilkan 12 *user story* melalui empat iterasi. Fitur kritis yang dibangun meliputi pembatasan hak akses data cabang berbasis *Role-Based Access Control* (RBAC), penetapan tanggal jatuh tempo SPP bulanan otomatis disertai tautan pengingat WhatsApp, validasi berkas transfer bank, dan *dashboard* konsolidasi kas delapan cabang secara *real-time*. Pengujian sistem dirancang melalui *Unit Testing*, *Black Box Testing* untuk memvalidasi fungsionalitas fitur, serta *User Acceptance Testing* (UAT) bersama pemilik lembaga dan staf administrasi cabang. Penerapan metode PXP diharapkan efektif untuk pengembangan mandiri, sehingga sistem informasi operasional mampu mendigitalisasi seluruh layanan Bimbel ARTHA secara terstruktur, akurat, dan terpusat.

**Kata kunci:** Bimbingan Belajar, Manajemen Operasional Multicabang, *Personal Extreme Programming*, *Role-Based Access Control* dan Sistem Informasi Berbasis Web

---

## 2. Naskah Halaman 12: ABSTRACT (Bahasa Inggris — Tepat 286 Kata)

**DESIGN AND DEVELOPMENT OF A WEB-BASED OPERATIONAL MANAGEMENT INFORMATION SYSTEM FOR A TUTORING CENTER USING THE PERSONAL EXTREME PROGRAMMING METHOD (CASE STUDY: BIMBEL ARTHA BALIKPAPAN)**

By: Ariel Itsbat Nurhaq  
Student Identity Number: 10231018  
Supervisor: Arif Wicaksono Septyanto, M.Kom.  
Co-Supervisor: Sri Rahayu Natasia, S.Komp., M.Si., M.Sc.  

**ABSTRACT**

Bimbel Artha Balikpapan is a non-formal educational institution managing eight active branch offices with 60 tutors and 2,400 students in Balikpapan, yet its operational management remains manual using paper forms, physical ledger books, paper receipts, and billing via WhatsApp by manually searching parent contact numbers one by one. This condition causes high workloads for branch staff, risks of daily cash calculation discrepancies, delays in tracking students with monthly tuition fee arrears, and the absence of centralized financial reporting for the institution owner. This study aims to design and build a web-based multi-branch operational management information system prototype to digitalize four main functions: new student registration, branch cashier transactions, payment transfer verification, and centralized daily cash reconciliation. The functional impact of this system is to improve administrative work efficiency and the accuracy of multi-branch financial recording. The system design concept is modeled through Business Process Model and Notation (BPMN), Use Case Diagrams, Activity Diagrams, Entity Relationship Diagrams (ERD), Next.js and Tailwind CSS interfaces, Laravel RESTful API backend, and a MySQL database. The implementation method utilized is Personal Extreme Programming (PXP), which is adaptive for individual developers, producing 12 user stories across four iterations. Critical features developed include branch data access restrictions based on Role-Based Access Control (RBAC), automated monthly tuition due date determinations equipped with direct WhatsApp reminder links, bank transfer verification, and a real-time multi-branch cash consolidation dashboard. System evaluation is designed through Unit Testing, Black Box Testing to validate feature functionality, and User Acceptance Testing (UAT) with the institution owner and branch administrative staff. The application of the PXP method is expected to be effective for independent development, ensuring the operational information system digitalizes all Bimbel ARTHA services in a structured, accurate, and centralized manner.

**Keywords:** Multi-Branch Operational Management, Personal Extreme Programming, Role-Based Access Control, Tutoring Center and Web-Based Information System
