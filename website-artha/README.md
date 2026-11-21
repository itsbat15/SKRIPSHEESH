# SIMBA: Sistem Informasi Manajemen Operasional Bimbel Artha

SIMBA membantu staf cabang mencatat pendaftaran, pembayaran, dan tutup kas. Manajemen pusat memeriksa pembayaran transfer dan memantau pendapatan seluruh cabang.

## Menjalankan demo

Gunakan Node.js 24 LTS dan npm. Dari direktori `website-artha`, jalankan:

```sh
npm ci
npm run dev
```

Buka [http://localhost:3000/login](http://localhost:3000/login) atau pilih **Masuk staf** dari halaman publik. Basis data demo dibuat otomatis pada akses pertama dengan delapan cabang, empat jenjang paket, kelompok belajar, akun staf, dan contoh transaksi.

| Peran | Email demo | Kata sandi demo |
| --- | --- | --- |
| Super Admin | `pusat@artha.example` | `ArthaDemo2026!` |
| Admin Artha 1 | `cabang1@artha.example` | `ArthaDemo2026!` |
| Admin Artha 2 | `cabang2@artha.example` | `ArthaDemo2026!` |

Akun `cabang3@artha.example` hingga `cabang8@artha.example` menggunakan kata sandi demo yang sama. Semua data dan kontak demo bersifat fiktif. Jangan kirim pesan WhatsApp ke nomor contoh.

## Alur berdasarkan proposal

| Kebutuhan | Cara mencoba |
| --- | --- |
| FR-01, FR-02 / US-01, US-02 | Masuk dengan kedua peran. Super Admin dapat menambah, mengedit, menempatkan dan menonaktifkan staf, serta mengelola cabang dan paket; akses Admin Cabang dibatasi pada cabang penugasan. |
| FR-03 sampai FR-06 / UC-01 | Dari **Pendaftaran**, masukkan biodata dan pilih sesi dengan kursi tersedia. Biaya awal mencakup biaya pendaftaran dan SPP pertama. Pembayaran tunai terkonfirmasi langsung; kuitansi PDF tersedia setelah tagihan lunas. |
| FR-07, FR-08 / UC-02 | Pilih metode transfer dan unggah JPG, PNG, atau PDF, maksimal 5 MB. Super Admin membuka **Validasi Transfer**, memeriksa bukti, kemudian mengonfirmasi atau menolak dengan alasan. Cabang melihat hasil dan dapat mencatat pembayaran ulang jika ditolak. |
| FR-09, FR-10 / US-09, US-10 | Dari **Tagihan & Pembayaran**, gunakan filter tunggakan, jenjang, atau kelompok. SPP terbit otomatis mengikuti tanggal pendaftaran mulai bulan berikutnya; tanggal yang tidak ada disesuaikan ke akhir bulan. Tautan WhatsApp menyiapkan pesan, tidak mengirimkannya otomatis. |
| FR-11, FR-12 / UC-03 | Admin Cabang memasukkan kas fisik di **Rekonsiliasi Kas**. Selisih mewajibkan catatan; tutup kas mengunci pencatatan tunai hari itu dan menghasilkan berita acara PDF. Super Admin memeriksa dan menyetujui penutupan, memantau tunggakan, memfilter pendapatan per periode/cabang, dan mengunduh PDF atau Excel dari **Laporan Keuangan**. |

Pembayaran yang belum mencapai total tagihan dicatat sebagai pembayaran sebagian. Pembayaran transfer masuk laporan pada hari konfirmasi; bila hari tersebut sudah ditutup, pembukuan masuk pada tanggal berikutnya yang belum ditutup. Tanggal operasional menggunakan zona waktu Asia/Makassar.

## Penyimpanan dan penggunaan non-demo

Proposal menggunakan Laravel/Sanctum dan MySQL. Implementasi ini tetap memisahkan antarmuka, logika bisnis, dan lapisan data dengan Next.js App Router, REST Route Handlers, serta SQLite bawaan Node.js (`node:sqlite`). Sepuluh entitas ERD dipertahankan: `branches`, `users`, `course_packages`, `study_groups`, `students`, `enrollments`, `tuition_bills`, `payments`, `payment_proofs`, dan `daily_reconciliations`. Tabel tambahan `sessions` menyimpan sesi yang dapat dicabut.

Basis data bawaan berada di `.artha/artha.sqlite` dan tidak dilacak oleh Git. Gunakan `ARTHA_DB_PATH` untuk menentukan direktori data persisten; basis data dan bukti transfer harus hanya dapat diakses oleh proses server. Gunakan satu host dengan disk persisten, cadangkan basis data, dan letakkan aplikasi di balik HTTPS untuk penggunaan di jaringan.

Untuk penggunaan non-demo dengan basis data kosong, tetapkan `ARTHA_DEMO=0`, `ARTHA_DB_PATH`, `ARTHA_ADMIN_EMAIL`, dan `ARTHA_ADMIN_PASSWORD` (minimal 12 karakter) di lingkungan server, kemudian jalankan `npm run build` dan `npm run start`. Jangan memakai berkas basis data demo untuk data operasional. Untuk menjalankan build produksi secara lokal melalui HTTP, gunakan `ARTHA_INSECURE_COOKIE=1` hanya pada mesin pengembangan.

## Pemeriksaan

Jalankan `npm test` untuk pengujian alur pendaftaran, isolasi cabang, pembayaran, validasi transfer, penutupan kas dan hasil ekspor. Jalankan `npm run build` untuk build Next.js. Pengujian ini bukan UAT bersama staf maupun pengukuran kinerja delapan cabang; keduanya memerlukan kondisi lapangan dan peserta yang relevan.

Pembelajaran daring, bank soal, pelaporan nilai, dan payment gateway tidak termasuk ruang lingkup proposal. Menu mock modul, pengeluaran, dan tentor juga tidak disertakan dalam dashboard operasional.
