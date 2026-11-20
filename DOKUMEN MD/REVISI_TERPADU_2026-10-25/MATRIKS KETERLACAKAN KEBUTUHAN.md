# Matriks keterlacakan kebutuhan ARTHA

Matriks ini menghubungkan kebutuhan dengan sumber, cerita pengguna, use case, iterasi, pengujian, dan tabel. Seluruh baris merupakan rancangan dan tidak menyatakan aplikasi telah lulus pengujian atau semua kebijakan telah disahkan mitra.

## 1. Pemetaan inti

Kode sumber S-01 sampai S-07 mengikuti Tabel 3.5 pada Bab 3. Kelompok PU merupakan kelompok pemeriksaan, sedangkan kode BB menunjuk kasus rinci pada lampiran pengujian.

| KF | Sumber | US | UC | Iterasi | Kelompok | Kasus BB | UAT | Tabel utama |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| KF-01 | S-02/S-05 | US-01 | UC-00 | I-01 | PU-01 | BB-01, BB-30 | UAT-01 | `users`, `branches`, `activity_logs` |
| KF-02 | S-01/S-04 | US-02 | UC-01 | I-01 | PU-02 | BB-02 | UAT-02 | `students`, `branches`, `academic_years`, `activity_logs` |
| KF-03 | S-04/S-06 | US-03 | UC-02 | I-01 | PU-03 | BB-03, BB-26 | UAT-03 | `classes`, `class_rooms`, `branches`, `academic_years`, `activity_logs` |
| KF-04 | S-06 | US-04 | UC-03 | I-02 | PU-04 | BB-04, BB-05, BB-06, BB-07, BB-26 | UAT-04 | `class_enrollments`, `students`, `classes`, `class_schedules`, `class_rooms`, `activity_logs` |
| KF-05 | S-02/S-04/S-05 | US-05 | UC-04 | I-02 | PU-05 | BB-08, BB-09, BB-29, BB-31 | UAT-05 | `class_schedules`, `mentors`, `mentor_subjects`, `subjects`, `classes`, `class_rooms`, `activity_logs` |
| KF-06 | S-01/S-03/S-04 | US-06 | UC-05 | I-01 | PU-06 | BB-10, BB-11, BB-27 | UAT-06 | `fee_tariffs`, `bills`, `students`, `users`, `academic_years`, `branches`, `activity_logs` |
| KF-07 | S-03/S-04 | US-07 | UC-06 | I-03 | PU-07 | BB-12 | UAT-07 | `payments`, `payment_allocations`, `bills`, `users`, `activity_logs` |
| KF-08 | S-03/S-06/S-07 | US-08 | UC-07 | I-03 | PU-08 | BB-13, BB-14, BB-25 | UAT-08 | `payments`, `payment_allocations`, `bills`, `bank_accounts`, `users`, `activity_logs` |
| KF-09 | S-03/S-06/S-07 | US-09 | UC-08 | I-03 | PU-09 | BB-14, BB-15, BB-16, BB-24, BB-25, BB-32 | UAT-09 | `payment_reviews`, `payments`, `payment_allocations`, `bills`, `bank_entries`, `bank_matches`, `bank_accounts`, `users`, `activity_logs` |
| KF-10 | S-04/S-06 | US-10 | UC-09 | I-03 | PU-10 | BB-17, BB-18 | UAT-10 | `reminder_actions`, `bills`, `payment_allocations`, `payments`, `students`, `users` |
| KF-11 | S-03/S-04/S-07 | US-11 | UC-10 | I-04 | PU-11 | BB-19, BB-20 | UAT-11 | `cash_batches`, `cash_batch_items`, `payments`, `bank_accounts`, `users`, `activity_logs` |
| KF-12 | S-02/S-03 | US-12 | UC-12 | I-04 | PU-12 | BB-21, BB-33 | UAT-12 | `branches`, `students`, `classes`, `class_enrollments`, `class_schedules`, `mentors`, `subjects`, `bills`, `payments`, `payment_allocations`, `payment_reviews`, `cash_batches`, `cash_batch_items`, `bank_entries`, `bank_matches`, `reminder_actions` |
| KF-13 | S-03/S-07 | US-13 | UC-11 | I-04 | PU-13 | BB-15, BB-20, BB-22, BB-24, BB-32, BB-33 | UAT-13 | `bank_entries`, `bank_matches`, `payments`, `cash_batches`, `cash_batch_items`, `bank_accounts`, `users`, `activity_logs` |
| KF-14 | S-02/S-05/S-07 | US-14 | UC-13 | I-01 | PU-14 | BB-23, BB-24, BB-28, BB-30 | UAT-14 | `academic_years`, `branches`, `users`, `subjects`, `mentors`, `mentor_subjects`, `bank_accounts`, `activity_logs` |

## 2. Keterlacakan nonfungsional

Kebutuhan nonfungsional diperiksa bersama fungsi yang terkait dan konteks lingkungan yang dicatat. Kriteria kinerja kuantitatif belum ditetapkan, sehingga pengukuran tanggapan belum memiliki keputusan lulus sebelum target disepakati.

| Kebutuhan | Rujukan pemeriksaan |
| :--- | :--- |
| KNF-01 Pembatasan akses | BB-01, BB-24, BB-30 |
| KNF-02 Integritas transaksi | BB-07, BB-11, BB-12, BB-16, BB-25, BB-32 |
| KNF-03 Ketertelusuran | BB-06, BB-14, BB-19, BB-21, BB-27 |
| KNF-04 Kerahasiaan bukti | BB-24 |
| KNF-05 Kemudahan penggunaan | Seluruh UAT; catatan bantuan serta kesalahan pengguna |
| KNF-06 Kesesuaian tampilan | Seluruh layar inti pada komputer dan telepon yang dicatat |
| KNF-07 Konsistensi data | BB-15, BB-20, BB-21, BB-22, BB-33 |
| KNF-08 Pemulihan | BB-28 |
| KNF-09 Kinerja | Rencana pengukuran setelah perangkat, data, jaringan, dan batas diterima ditetapkan |

## 3. Hubungan rumusan masalah

Rumusan masalah pertama dijawab melalui integrasi identitas, kelas, jadwal, tagihan, serta pembayaran sesuai kewenangan. Rumusan masalah kedua dijawab melalui dasbor, penelusuran penerimaan, setoran, dan pencocokan manual yang dibatasi dalam rancangan.

Rumusan masalah ketiga dijawab menggunakan hasil pengujian dan evaluasi pengguna atas fungsi tersebut. Hubungan dengan hasil, pembahasan, serta simpulan baru dapat diperiksa setelah implementasi dan evaluasi menghasilkan bukti.
