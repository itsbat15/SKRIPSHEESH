# SIMBA: Sistem Informasi Manajemen Operasional Bimbel Artha

SIMBA membantu staf cabang mencatat pendaftaran, pembayaran, dan tutup kas. Manajemen pusat memeriksa pembayaran transfer dan memantau pendapatan seluruh cabang.

## Menjalankan demo

Gunakan Node.js 24 LTS, npm, PHP 8.3, Composer 2, dan MySQL 8. Buat basis data lokal `artha` dan `artha_test`, lalu beri akun MySQL lokal akses ke keduanya. Aktifkan ekstensi PHP PDO MySQL, mbstring, XML, cURL, ZIP, dan GD.

Dari `website-artha/backend`, siapkan dan jalankan Laravel:

```sh
composer install
cp .env.example .env
php artisan key:generate
# Isi DB_HOST, DB_PORT, DB_DATABASE, DB_USERNAME, dan DB_PASSWORD di .env.
ARTHA_DEMO=true php artisan migrate --seed
php -d post_max_size=8M -d upload_max_filesize=6M -S 127.0.0.1:8000 -t public public/index.php
```

Di terminal lain, jalankan frontend dari `website-artha`:

```sh
npm ci
ARTHA_API_URL=http://127.0.0.1:8000 npm run dev
```

Buka [http://localhost:3000/login](http://localhost:3000/login) atau pilih **Masuk staf** dari halaman publik. Seeder demo membuat delapan cabang, empat jenjang paket, kelompok belajar, akun staf, dan contoh transaksi.

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

Next.js dan Tailwind menyajikan antarmuka. REST API Laravel pada `backend/` memvalidasi masukan, membatasi akses per cabang, dan memakai token Laravel Sanctum yang berlaku delapan jam dan dapat dicabut. MySQL menyimpan sepuluh entitas ERD: `branches`, `users`, `course_packages`, `study_groups`, `students`, `enrollments`, `tuition_bills`, `payments`, `payment_proofs`, dan `daily_reconciliations`. Sanctum menyimpan token dalam tabel tambahan `personal_access_tokens`.

Secara bawaan Next.js meneruskan permintaan `/api/artha/*` ke `ARTHA_API_URL` (standar: `http://127.0.0.1:8000`). Untuk akses browser langsung, tentukan `NEXT_PUBLIC_ARTHA_API_URL` sebelum build dan isi `ARTHA_FRONTEND_ORIGINS` di Laravel dengan daftar origin frontend yang dipisahkan koma. Laravel menyimpan bukti transfer di MySQL dan hanya menyajikannya ke pengguna yang berwenang. Cadangkan basis data dan gunakan HTTPS untuk penggunaan di jaringan.

Untuk basis data non-demo yang kosong, gunakan `APP_ENV=production`, `APP_DEBUG=false`, `ARTHA_DEMO=false`, `ARTHA_ADMIN_EMAIL`, dan `ARTHA_ADMIN_PASSWORD` (minimal 12 karakter), lalu jalankan `php artisan migrate --seed --force`. Jangan gunakan basis data demo untuk data operasional. Layani Laravel melalui direktori `backend/public` pada server web dengan PHP, lalu jalankan `npm run build` dan `npm run start` untuk frontend.

## Pemeriksaan

Jalankan `composer test` dari `website-artha/backend` untuk memeriksa autentikasi, isolasi cabang, pendaftaran, pembayaran, validasi transfer, penutupan kas, dan ekspor. PHPUnit menyegarkan skema basis data `artha_test`, jadi gunakan basis data uji yang terpisah dari data operasional. Jalankan `npm run build` dari `website-artha` untuk memeriksa build Next.js. Pengujian ini tidak menggantikan UAT bersama staf atau pengukuran kinerja di delapan cabang.

Pembelajaran daring, bank soal, pelaporan nilai, dan payment gateway tidak termasuk ruang lingkup proposal. Menu mock modul, pengeluaran, dan tentor juga tidak disertakan dalam dashboard operasional.
