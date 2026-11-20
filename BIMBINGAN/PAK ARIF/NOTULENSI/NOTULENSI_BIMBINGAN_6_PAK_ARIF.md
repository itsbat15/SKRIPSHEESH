# NOTULENSI BIMBINGAN TUGAS AKHIR KE-6
## Dosen Pembimbing 1: Bapak Arif Rahman, S.Kom., M.T.

---

### Informasi Pelaksanaan Bimbingan
* **Hari, Tanggal**: Rabu, 28 Oktober 2026
* **Waktu Pelaksanaan**: Pukul 12.00 sampai 12.45 WITA
* **Tempat Pelaksanaan**: Ruang Dosen Program Studi Sistem Informasi, Institut Teknologi Kalimantan (ITK)
* **Dosen Pembimbing 1**: Bapak Arif Rahman, S.Kom., M.T. (Pak Arif)
* **Mahasiswa Bimbingan**: Ariel (NIM. 10221074)
* **Topik Tugas Akhir**: Pengembangan Sistem Informasi Manajemen Operasional Bimbingan Belajar Artha Balikpapan Multicabang Berbasis Web Menggunakan Metode Personal Extreme Programming

---

## Notulensi

1. Menanyakan batasan modul penjadwalan dan mengingatkan bahwa penjadwalan kelas yang mencakup pembuatan kelas, penetapan tentor, dan alokasi kuota siswa masih tergolong wajar serta realistis untuk diselesaikan.
2. Menegaskan agar sistem tidak diperluas menjadi Learning Management System (LMS) seperti materi mingguan, video pembelajaran, kuis, atau modul bank soal, agar fokus penelitian tidak mengabur.
3. Menjelaskan prinsip arsitektur sistem bahwa transaksi di dunia nyata perlu menyediakan dua jalur masukan: jalur mandiri oleh pengguna dan jalur perantara oleh staf administrasi (admin input) atas nama pengguna.
4. Menekankan bahwa meskipun data dimasukkan melalui dua alur yang berbeda, struktur data, status verifikasi transaksi, dan dokumen bukti pembayaran yang tersimpan di backend harus tetap seragam.
5. Mengingatkan bahwa ketersediaan arsip digital terpusat sangat krusial agar manajemen memiliki pegangan bukti audit ketika terjadi komplain atau selisih pencatatan kas.
6. Menyetujui mekanisme pengadaan tablet di delapan cabang dan mengarahkan agar antarmuka staf administrasi dilengkapi tombol unggah dokumen untuk melampirkan berkas bukti pembayaran dan formulir pendaftaran fisik.
7. Menjelaskan bahwa dengan tersimpannya seluruh arsip di peladen pusat, sistem secara otomatis dapat mengolah omzet harian per cabang dan omzet kumulatif lembaga tanpa mengharuskan pengantaran rekapan kertas secara manual ke kantor pusat.
8. Menegaskan bahwa pembahasan penelitian terdahulu tidak boleh berdiri sendiri secara terisolasi tanpa korelasi ilmiah.
9. Menginstruksikan mahasiswa untuk membangun garis penghubung (benang merah) yang menerangkan kelemahan atau keterbatasan metode pada penelitian bimbingan belajar terdahulu (seperti sifat kaku Waterfall atau fokus cabang tunggal).
10. Mewajibkan mahasiswa menjelaskan secara lugas bagaimana metodologi Personal Extreme Programming (PxP) yang diterapkan pada ARTHA mampu melengkapi dan menyelesaikan kelemahan-kelemahan penelitian terdahulu tersebut.
11. Menyetujui penyederhanaan rumusan masalah menjadi dua butir fokus yang terarah.
12. Menyetujui batasan sistem yang berfokus pada dasbor manajemen operasional internal multicabang tanpa payment gateway berbayar.
13. Mengarahkan agar mekanisme notifikasi tagihan SPP tidak menggunakan bot otomatis atau peladen siaran (broadcast server) yang memerlukan API berbayar, melainkan menyediakan tombol aksi tautan WhatsApp pada setiap baris data siswa yang langsung membuka aplikasi pesan dengan nomor kontak wali murid dan draf pesan penagihan siap kirim.
14. Menyetujui pencantuman sejarah dan rujukan awal kemunculan metode guna memberikan pemahaman komprehensif bagi pembaca mengenai latar belakang lahirnya PxP.
15. Menegaskan bahwa tahapan operasional yang dieksekusi dalam metodologi penelitian harus tetap konsisten mengikuti tahapan baku yang distandarisasikan oleh Dzhurov dkk. (2009).
16. Menyetujui pemisahan arsitektur antara frontend Next.js dan backend Laravel REST API sebagai keputusan arsitektural yang tepat, di mana pertukaran data dijembatani melalui protokol HTTP dengan format REST API standar.
17. Meluruskan bahwa fungsi perutean API telah ditangani secara terpadu oleh Laravel sehingga tidak memerlukan API Gateway terpisah.
18. Memberikan persetujuan penuh terhadap penambahan kolom khusus pembeda atau keterkaitan terhadap ARTHA pada tabel komparasi penelitian terdahulu, karena hal tersebut memberikan nilai tambah ilmiah yang membuktikan kemampuan analisis kritis mahasiswa.
