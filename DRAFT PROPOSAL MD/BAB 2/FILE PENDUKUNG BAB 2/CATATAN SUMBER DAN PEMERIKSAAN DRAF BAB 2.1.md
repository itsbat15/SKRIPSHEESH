# Catatan pendamping draf baru Bab 2.1

Berkas `BAB 2 - TINJAUAN PUSTAKA (DRAF BARU BAB 2.1).md` disusun pada 27 Oktober 2026 mengikuti panduan isi dan urutan empat belas subbab yang telah disepakati. Naskah ini merupakan draf untuk ditelaah dan direvisi mahasiswa, dengan uraian teori, alasan pemilihan, serta kaitannya dengan ARTHA; berkas Bab 2 sebelumnya dipertahankan.

## 1. Cakupan pekerjaan

Draf mencakup bagian 2.1.1 sampai 2.1.14, satu gambar tahapan PxP, enam tabel, dan daftar pustaka kerja. Bagian 2.2 Penelitian Terdahulu belum ditulis karena pembahasan saat ini berfokus pada Bab 2.1 dan pemilihan sumbernya; daftar pustaka kerja dipindahkan ke daftar pustaka proposal ketika naskah digabungkan.

Sidiq tidak dipakai sebagai sitasi pada draf ini karena teori PxP sudah didukung sumber asli dan contoh penerapan yang edisinya terverifikasi. Artikel tersebut tetap ada dalam koleksi dengan catatan cakupan edisi 2025 yang belum pasti, sedangkan Priatmaja yang telah dihapus tidak digunakan sebagai sumber.

## 2. Peta pemeriksaan sumber

Nomor halaman PDF di bawah merupakan nomor urut berkas, sedangkan nomor cetak adalah nomor yang tertera pada halaman sumber. Untuk sumber web, lokator menggunakan judul bagian, URL dalam daftar pustaka, dan tanggal akses karena tidak mempunyai nomor halaman tetap.

| Subbab | Sumber dan lokasi yang diperiksa | Batas penggunaan |
| :--- | :--- | :--- |
| 2.1.1 | Laudon dan Laudon: cetak 45 sampai 48/PDF 47 sampai 50, serta cetak 77 sampai 80/PDF 79 sampai 82; Sommerville: cetak 28 sampai 33/PDF 45 sampai 50 dan cetak 63 sampai 64/PDF 80 sampai 81 | PDF Laudon adalah edisi global ke-13 tahun 2014. Alasan pemilihan PxP merupakan pertimbangan rancangan ARTHA, bukan klaim metode lain tidak dapat digunakan. |
| 2.1.2 | Dzhurov: cetak 253 sampai 256/PDF 2 sampai 5; gambar sumber pada cetak 255/PDF 4; Beck dan Andres: bagian Test-First Programming/PDF 120 | Sumber Dzhurov berbentuk prosiding asli. Gambar draf digambar ulang dengan terjemahan, penyederhanaan, dan penjelasan hubungan log. |
| 2.1.3 | Cohn: cetak 4 sampai 5/PDF 13 sampai 14 dan cetak 17/PDF 26; artikel resmi penulis tentang format cerita; ISTQB Acceptance Testing: PDF 11 dan 15 sampai 16 | Salinan Cohn berupa bab contoh resmi. Contoh cerita dan kriteria kelas merupakan ilustrasi penulis berdasarkan konteks ARTHA, bukan kutipan contoh asli Cohn. |
| 2.1.4 | Sommerville: cetak 124 sampai 126/PDF 141 sampai 143; OMG UML Bab 18, terutama §18.1/PDF 681 sampai 685 | Tabel merupakan ringkasan bentuk dan makna notasi. Include dan extend tidak harus digunakan pada setiap diagram ARTHA. |
| 2.1.5 | OMG BPMN §7.3, cetak 26 sampai 29/PDF 56 sampai 59 dan Bab 10; ISTQB Acceptance Testing PDF 19 sampai 21 | Tahun 2013 mengikuti halaman judul spesifikasi versi 2.0.2 yang tersedia. BPMN memodelkan proses bisnis dan tidak menggantikan gambar siklus PxP. |
| 2.1.6 | Sommerville: cetak 129 sampai 133/PDF 146 sampai 150; OMG UML §11.4, cetak 194 dan seterusnya/PDF 236 dan seterusnya, beserta Bab 7 dan Bab 9 | Class diagram ARTHA tetap perlu dibuat di Bab 3 dengan operasi dan tanggung jawab yang benar-benar dirancang. |
| 2.1.7 | Chen: cetak 9 sampai 13/PDF 1 sampai 5; dokumentasi Mermaid bagian ERD; manual MySQL bagian FOREIGN KEY Constraints | Salinan Chen hanya cuplikan lima halaman. Notasi Crow’s Foot dan PK/FK tidak seluruhnya diatribusikan kepada Chen. |
| 2.1.8 | Dokumentasi Next.js: What is Next.js serta Layouts and Pages; React: Managing State | Tidak menyatakan seluruh fitur Next.js sudah dipakai proyek. Versi implementasi tetap dicocokkan pada Bab 3. |
| 2.1.9 | Dokumentasi Tailwind CSS: Styling with Utility Classes dan Responsive Design | Fasilitas responsif tidak dinyatakan otomatis membuktikan kemudahan penggunaan. |
| 2.1.10 | Laravel 12.x: Routing, Validation, Database, Eloquent, Migrations, Sanctum: SPA Authentication, Authorization; Kismantoro dan Ibadi cetak 3195/PDF 1 | Dokumentasi 12.x merupakan versi rujukan, bukan bukti versi terpasang. Pemakaian MVC oleh INET tidak dijadikan bukti bahwa ARTHA menyajikan halaman melalui Blade. |
| 2.1.11 | Fielding Bab 5, terutama §5.1.3 dan §5.1.5; RFC 9110 §9 dan §15 | API ARTHA dijelaskan sebagai API HTTP yang mengadopsi pemodelan sumber daya dan metode HTTP, dengan pilihan sesi yang tidak diklaim memenuhi stateless REST secara penuh. |
| 2.1.12 | Manual MySQL §1.2.1, §15.1.20.5, §17.2 dan §17.7.2; titik awal cetak 4/PDF 36, cetak 3152/PDF 3184, cetak 3234/PDF 3266 | Salinan manual seri 8.4 sampai 8.4.9. Rincian aturan transaksi tetap memerlukan rancangan aplikasi dan konfigurasi yang tepat. |
| 2.1.13 | ISTQB CTFL v4.0.1 PDF 39 sampai 41; Dzhurov cetak 255 sampai 256/PDF 4 sampai 5 | Contoh kapasitas satu sampai dua puluh bersifat ilustratif. Varian yang dicontohkan adalah BVA dua nilai, bukan penetapan kapasitas kelas mitra. |
| 2.1.14 | Sommerville cetak 228 sampai 230/PDF 245 sampai 247; ISTQB Acceptance Testing PDF 11 dan 15 sampai 16; Apriyanti cetak 3678/PDF 1 | Tidak menggunakan angka hasil UAT penelitian lain sebagai hasil ARTHA. Likert tidak diperlakukan sebagai kewajiban UAT atau dasar otomatis persentase kelayakan. |

## 3. Keputusan penulisan dan pemeriksaan substansi

Narasi mengikuti pola konsep, unsur atau cara kerja, kemudian keterkaitan dengan penelitian tanpa mengulang seluruh rancangan Bab 3. Kutipan menggunakan Author-Year secara langsung, sementara halaman dicantumkan pada bagian sumber yang lokasinya telah dapat diperiksa; tidak digunakan penanda catatan kaki sitasi.

Daftar pustaka hanya memuat sumber yang benar-benar dikutip dalam draf. Sumber web dari lembaga yang sama dibedakan menggunakan akhiran huruf yang konsisten dalam dokumen ini, sehingga Laravel memakai t.t.-a sampai t.t.-g, Tailwind Labs memakai t.t.-a sampai t.t.-b, dan Vercel memakai t.t.-a sampai t.t.-b.

Berkas `ASET BAB 2.1/REFERENSI DRAF BAB 2.1.bib` menyediakan 29 entri untuk diimpor ke pengelola referensi. Akhiran huruf dalam daftar pustaka yang digabungkan perlu mengikuti keluaran pengelola referensi tersebut, karena urutan akhirnya dapat berubah ketika sumber dari bab lain ikut dimasukkan.

Metadata INET diperiksa kembali pada laman penerbit: DOI yang digunakan adalah `10.36040/jati.v10i2.17875` dan rentang halaman 3195 sampai 3203. Rujukan tersedia pada https://mail.ejournal.itn.ac.id/jati/article/view/17875 serta daftar isi https://ejournal.itn.ac.id/jati/issue/view/459; nama penulis pertama dipertahankan sebagai nama tunggal Kismantoro sesuai PDF.

Gambar PxP tersedia dalam PNG untuk penyisipan naskah dan SVG untuk penyuntingan. Bentuk notasi UML, BPMN, serta ERD pada tabel dijelaskan melalui deskripsi grafis; jika pembimbing menghendaki kolom simbol berupa gambar, deskripsi itu dapat dilengkapi ilustrasi simbol tanpa mengubah maknanya.

## 4. Hal yang perlu diselaraskan saat proposal digabungkan

Bab 1 versi revisi malam masih menyatakan pemeriksaan transfer dilakukan Admin Cabang, sedangkan rancangan Bab 3 dan use case terbaru menempatkan pengajuan pada Admin Cabang serta pemeriksaan pada Super Admin. Bab 2 baru mengikuti rancangan terbaru, sehingga kalimat yang bertentangan pada Bab 1 perlu direvisi pada pekerjaan penyelarasan naskah berikutnya.

Bab 3 yang diperiksa juga belum mempunyai subbagian khusus class diagram dan masih menggunakan beberapa klaim keberhasilan yang terlalu kuat untuk tahap rancangan. Kehadiran teori class diagram pada Bab 2 perlu diikuti pemodelan yang benar-benar dipakai pada tahap perancangan; kalimat seperti keamanan atau efektivitas yang sudah terbukti perlu diperiksa berdasarkan bukti pengujian yang tersedia.

Sebelum dipindahkan ke Word, mahasiswa perlu membaca kembali paragraf, memeriksa halaman sumber, dan memastikan dapat menjelaskan alasan setiap metode serta teknologi yang digunakan. Nomor tabel dan gambar, akhiran huruf sumber tanpa tahun, serta daftar pustaka kemudian disatukan melalui pengelola referensi agar konsisten di seluruh proposal.

Instrumen Likert belum dilengkapi sebagai bagian operasional draf karena keputusan penggunaannya belum ditetapkan. Apabila pengukuran kepuasan dipilih, tambahkan sumber instrumen, indikator, pilihan respons, dan cara analisis yang sesuai sebelum memasukkan rumus atau kategori hasil.
