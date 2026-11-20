# Panduan isi Bab 2 sesuai susunan final

Panduan ini disesuaikan pada 27 Oktober 2026 dengan susunan yang telah disepakati. Naskah Bab 2 yang sudah ada dan lampiran pengguna tidak ditimpa.

Berikut panduan isi untuk setiap subbab. **Bab 2 menjelaskan dasar konsep dan alasan penggunaannya, sedangkan Bab 3 menunjukkan penerapannya secara khusus pada ARTHA.** Karena itu, Bab 2 tidak perlu memuat seluruh diagram, tabel kebutuhan, kode program, atau prosedur pengujian ARTHA.

**2.1 Kajian Teknologi atau Metode Terkait**

Awali dengan paragraf pengantar yang menjelaskan kelompok kajian dalam bagian ini. Sampaikan bahwa metode pengembangan, pemodelan, teknologi, dan pengujian digunakan sebagai dasar perancangan prototipe ARTHA.

**2.1.1 Sistem Informasi Manajemen dan Pengembangannya**

Bagian ini memberikan dasar mengenai sistem yang dibangun sebelum membahas metode pengembangannya. Pembahasannya perlu menghubungkan pengolahan data dengan kebutuhan informasi bagi pengelola.

Isi yang disarankan:

- Pengertian sistem informasi dan sistem informasi manajemen.
- Hubungan masukan, proses, penyimpanan, dan keluaran informasi.
- Peran informasi dalam pemantauan operasional dan pengambilan keputusan.
- Konsep pengembangan sistem informasi serta tahapan umum SDLC.
- Perbandingan pendekatan pengembangan yang relevan sebagai dasar pemilihan PxP.

Akhiri dengan alasan kebutuhan proses pengembangan yang sesuai untuk ARTHA. **Hindari menyimpulkan metode lain tidak sah atau PxP pasti paling unggul**; gunakan karakteristik proyek sebagai pertimbangan.

Rujukan kerja yang disarankan: Laudon dan Laudon (2014); Sommerville (2011); Pressman (2010). Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.2 Personal Extreme Programming**

Jelaskan PxP sebagai proses pengembangan individual beserta disiplin pelaksanaannya. Bagian ini tidak cukup hanya berisi definisi dan daftar tujuh tahapan.

Isi yang disarankan:

- Latar belakang dan tujuan PxP.
- Hubungannya dengan praktik XP dan disiplin PSP.
- Prinsip pengukuran pekerjaan, pengujian berkelanjutan, serta perbaikan proses.
- Tujuh tahapan: *requirements, planning, iteration initialization, design, implementation, system testing*, dan *retrospective*.
- Perencanaan tugas dan estimasi durasi.
- Pencatatan waktu, cacat, perubahan kebutuhan, dan usulan perbaikan.
- Unit testing, TDD, serta refactoring pada tahap implementasi.

Sertakan **gambar tahapan PxP** dari sumber yang jelas, kemudian jelaskan hubungan antartahapnya. Rencana iterasi, pembagian fitur, jadwal, dan formulir pencatatan ARTHA ditempatkan pada Bab 3.

Rujukan kerja yang disarankan: Dzhurov, Krasteva, dan Ilieva (2009); Beck dan Andres (2004). Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.3 User Stories**

Jelaskan cerita pengguna sebagai cara menyampaikan kebutuhan dari sudut pandang pengguna. Tekankan bahwa cerita singkat tersebut perlu diperjelas melalui diskusi dan kriteria penerimaan.

Isi yang disarankan:

- Pengertian dan tujuan user stories.
- Unsur pengguna, kebutuhan, dan manfaat.
- Format: “Sebagai …, saya ingin …, agar ….”
- Kriteria penerimaan yang dapat diperiksa.
- Hubungannya dengan perencanaan tugas dan pengujian.

Satu contoh sederhana dapat diberikan untuk membantu pembaca. Daftar lengkap cerita pengguna ARTHA dan pemetaannya terhadap kebutuhan ditempatkan pada Bab 3.

Rujukan kerja yang disarankan: Beck dan Andres (2004); Cohn (2004), ditambah cuplikan resmi buku dan artikel penulis. Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.4 Use Case Diagram**

Jelaskan diagram ini sebagai pemetaan aktor dan fungsi yang disediakan sistem. Bedakan diagram ringkas tersebut dari skenario yang memperinci interaksi pengguna dengan sistem.

Isi yang disarankan:

- Pengertian dan tujuan use case diagram.
- Aktor, use case, batas sistem, dan hubungan antarunsur.
- Makna hubungan *association, include, extend*, dan *generalization* yang digunakan.
- Unsur skenario use case: tujuan, prasyarat, alur utama, alur alternatif, dan kondisi akhir.
- Hubungannya dengan kebutuhan fungsional.

Sertakan **tabel notasi beserta artinya** berdasarkan sumber yang tepat. Diagram dan seluruh skenario khusus ARTHA disajikan pada Bab 3.

Rujukan kerja yang disarankan: Sommerville (2011); OMG UML 2.5.1 (2017). Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.5 Business Process Model and Notation**

Jelaskan BPMN sebagai notasi pemodelan proses bisnis yang digunakan untuk memahami aktivitas dan koordinasi pihak terkait. Bedakan model proses berjalan dan usulan, serta bedakan BPMN dari diagram alir tahapan penelitian PxP.

Isi yang disarankan:

- Tujuan BPMN dan kegunaannya dalam memahami proses bisnis.
- Event, activity, gateway, pool, lane, sequence flow, message flow, dan data object yang dipakai.
- Aturan dasar pembacaan dan penghubungan notasi.
- Penggambaran pihak, aktivitas, dokumen, keputusan, serta kondisi alternatif.
- Hubungan pemetaan proses dengan penggalian dan validasi kebutuhan.

Sertakan tabel notasi berdasarkan spesifikasi resmi OMG dan gunakan hanya elemen yang relevan. Model proses bisnis ARTHA ditempatkan pada Bab 3 dan divalidasi bersama manajemen; penghapusan Activity Diagram tidak boleh diatribusikan sebagai instruksi eksplisit Bu Ayu karena transkrip hanya menyarankan pemetaan proses bisnis.

Rujukan kerja yang disarankan: OMG BPMN 2.0.2 (2013), ditambahkan. Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.6 Class Diagram**

Jelaskan struktur kelas perangkat lunak dan hubungan antarkelas. Pembahasan ini harus memperlihatkan perbedaannya dengan ERD yang berfokus pada data.

Isi yang disarankan:

- Pengertian dan tujuan class diagram.
- Nama kelas, atribut, operasi, dan visibilitas.
- Hubungan seperti asosiasi, ketergantungan, generalisasi, agregasi, atau komposisi sesuai kebutuhan.
- Multiplicity atau jumlah keterhubungan antarobjek.
- Peran diagram dalam pembagian tanggung jawab perangkat lunak.

Sertakan tabel notasi yang digunakan. **Jangan membuat class diagram sekadar salinan tabel basis data**; rancangan pada Bab 3 perlu menunjukkan operasi dan tanggung jawab kelas yang relevan.

Rujukan kerja yang disarankan: Sommerville (2011); OMG UML 2.5.1 (2017). Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.7 Entity Relationship Diagram**

Jelaskan ERD sebagai dasar pemodelan data dan keterhubungannya. Pilih satu notasi yang konsisten dengan diagram yang akan digunakan.

Isi yang disarankan:

- Pengertian dan tujuan ERD.
- Entitas, atribut, dan hubungan.
- Kardinalitas serta sifat wajib atau opsional suatu hubungan.
- Kunci utama dan kunci asing pada skema relasional.
- Penyelesaian hubungan banyak ke banyak melalui entitas penghubung.
- Integritas data yang relevan.

Sertakan tabel notasi dan contoh hubungan sederhana bila diperlukan. ERD lengkap, rincian tabel, dan kamus data ARTHA ditempatkan pada Bab 3 atau lampiran sesuai kebutuhan.

Rujukan kerja yang disarankan: Pressman (2010); Chen (1976), ditambah cuplikan penulis; dokumentasi Mermaid untuk notasi implementasi. Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.8 Next.js**

Pembahasan diarahkan pada peran Next.js dalam membangun antarmuka ARTHA. React cukup dijelaskan sebagai dasar komponennya tanpa harus menjadi subbab terpisah.

Isi yang disarankan:

- Pengertian Next.js dan hubungannya dengan React.
- Komponen, halaman, layout, dan navigasi.
- Pengelolaan interaksi serta keadaan antarmuka.
- Pengambilan data dari layanan aplikasi.
- Alasan pemilihannya untuk kebutuhan antarmuka ARTHA.

Hindari uraian panjang tentang sejarah dan panduan instalasi. Versi aktual, struktur proyek, serta konfigurasi implementasi dijelaskan pada Bab 3.

Rujukan kerja yang disarankan: Vercel, dokumentasi Next.js; React, Managing State, ditambahkan. Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.9 Tailwind CSS**

Jelaskan Tailwind CSS sebagai perangkat pengaturan tampilan yang digunakan dalam proyek. Pembahasannya dapat lebih singkat daripada metode pengembangan dan pengujian.

Isi yang disarankan:

- Pengertian pendekatan kelas utilitas.
- Pengaturan warna, tipografi, jarak, dan tata letak.
- Dukungan tampilan responsif.
- Konsistensi gaya melalui komponen yang digunakan kembali.
- Alasan penggunaannya pada antarmuka ARTHA.

Hindari menyatakan bahwa Tailwind otomatis menjamin kemudahan penggunaan. Kemudahan tersebut tetap perlu dinilai melalui evaluasi antarmuka bersama pengguna.

Rujukan kerja yang disarankan: Tailwind Labs, dokumentasi Tailwind CSS, ditambahkan. Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.10 Laravel**

Jelaskan Laravel sebagai teknologi yang direncanakan menangani layanan aplikasi dan aturan bisnis. Bedakan fungsi teknologi tersebut dari bukti bahwa penerapannya pada ARTHA sudah selesai.

Isi yang disarankan:

- Pengertian Laravel dan konsep MVC.
- Peran route, controller, model, dan validasi.
- Pengelolaan data melalui Eloquent serta migration.
- Pengelolaan transaksi basis data.
- Autentikasi sesi menggunakan Sanctum sesuai rancangan.
- Otorisasi berdasarkan peran, cabang, dan data yang diakses.

Terangkan perbedaan **autentikasi** dan **otorisasi** secara jelas. Jangan menyebut Sanctum sebagai autentikasi token apabila implementasi yang dipilih menggunakan sesi berbasis kuki.

Rujukan kerja yang disarankan: Laravel, dokumentasi resmi Sanctum, Authorization, Validation, Database dan Eloquent, ditambahkan. Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.11 REST API**

Jelaskan konsep layanan yang memungkinkan antarmuka dan aplikasi peladen bertukar data. Pembahasannya perlu menunjukkan hubungan dengan arsitektur Next.js dan Laravel yang direncanakan.

Isi yang disarankan:

- Pengertian API dan pendekatan REST.
- Sumber daya, endpoint, serta permintaan dan respons.
- Metode HTTP yang digunakan.
- Format pertukaran data, misalnya JSON.
- Kode status HTTP serta respons kesalahan.
- Hubungan komunikasi API dengan autentikasi dan otorisasi.

Berikan contoh umum jika dibutuhkan untuk memperjelas konsep. Daftar endpoint, struktur payload, dan kontrak API ARTHA merupakan rincian perancangan pada Bab 3 atau dokumentasi teknis.

Rujukan kerja yang disarankan: Fielding (2000); Fielding, Nottingham, dan Reschke (2022), RFC 9110, ditambahkan. Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.12 MySQL**

Pembahasan berfokus pada penyimpanan data relasional yang mendukung operasional sistem. Hubungkan konsepnya dengan kebutuhan menjaga konsistensi data siswa, tagihan, pembayaran, dan cabang.

Isi yang disarankan:

- Pengertian MySQL sebagai sistem pengelolaan basis data relasional.
- Tabel, baris, kolom, serta hubungan antartabel.
- Kunci, batasan data, dan integritas referensial.
- Transaksi basis data dan sifat ACID.
- Alasan pemilihannya untuk rancangan ARTHA.

Tidak perlu mencantumkan seluruh perintah SQL. Versi MySQL, mesin penyimpanan, dan konfigurasi aktual ditempatkan pada Bab 3.

Rujukan kerja yang disarankan: Oracle, MySQL 8.4 Reference Manual, ditambahkan sebagai tautan resmi. Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.13 Black Box Testing**

Jelaskan pengujian perilaku fungsi berdasarkan spesifikasi dan hasil yang diharapkan. Pembahasan perlu menjadi dasar penyusunan kasus uji, bukan hanya definisi pengujian.

Isi yang disarankan:

- Tujuan dan karakteristik Black Box Testing.
- Unsur kasus uji: prasyarat, masukan, langkah, hasil yang diharapkan, hasil aktual, dan status.
- EP untuk menentukan kelompok masukan yang relevan.
- BVA untuk memeriksa batas kelompok yang memiliki urutan.
- Pengujian alur utama, alternatif, dan perubahan status yang diperlukan.
- Pencatatan kegagalan serta pengujian ulang.

Gunakan contoh sederhana untuk membedakan EP dan BVA. **Seluruh kasus uji ARTHA, data uji, dan kriteria kelulusannya dijelaskan pada Bab 3**, sedangkan hasil pelaksanaannya berada pada Bab 4.

Rujukan kerja yang disarankan: Pressman (2010); ISTQB CTFL v4.0.1 (2024), ditambahkan. Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.1.14 User Acceptance Testing**

Jelaskan evaluasi kesesuaian sistem dengan kebutuhan kerja pengguna. Bedakan penerimaan tugas dari persepsi kemudahan dan kepuasan.

Isi yang disarankan:

- Pengertian dan tujuan UAT.
- Peran pengguna dalam evaluasi.
- Dasar penyusunan tugas dan kriteria penerimaan.
- Pencatatan keberhasilan, kendala, bantuan, serta kebutuhan perbaikan.
- Pengujian ulang setelah perbaikan.
- Kuesioner dan Skala Likert apabila pengukuran persepsi atau kepuasan memang dipilih.

Jika menggunakan persentase skor, jelaskan dasar penskoran dan makna hasilnya. Jangan menyamakan persentase skor kuesioner dengan persentase tugas yang diterima atau menetapkan kategori kelayakan tanpa dasar.

Rujukan kerja yang disarankan: Sommerville (2011); ISTQB Acceptance Testing v1.0 (2019), ditambahkan. Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.

**2.2 Penelitian Terdahulu**

Awali dengan paragraf yang menjelaskan dasar pemilihan penelitian, kemudian sajikan satu tabel perbandingan. Setelah tabel, tulis sintesis yang menunjukkan hubungan penelitian terdahulu dengan posisi ARTHA.

Kolom yang disarankan:

| Kolom | Isi |
| :--- | :--- |
| Penulis dan tahun | Identitas sumber yang sudah diperiksa. |
| Objek dan masalah | Konteks serta masalah penelitian. |
| Metode dan teknologi | Pendekatan pengembangan dan perangkat yang digunakan. |
| Fitur dan hasil evaluasi | Fungsi serta bukti hasil yang dilaporkan. |
| Keterkaitan dengan ARTHA | Bagian yang diadaptasi dan perbedaannya. |

Sintesis perlu membahas pembanding terdekat, terutama Jia Jia Education yang sudah memiliki pengelolaan cabang. **Hindari menganggap fitur tidak tersedia hanya karena tidak dijelaskan dalam artikel**, dan jangan menyatakan pergantian metode menjadi satu-satunya kebaruan penelitian.

Untuk seluruh subbab, gunakan pola **konsep, unsur atau cara kerja, lalu relevansi terhadap penelitian**. Utamakan buku atau sumber primer untuk teori, dokumentasi resmi untuk teknologi, dan artikel penelitian untuk contoh penerapannya.

Catatan penempatan rincian: Bab 3 memuat rencana pengujian, kriteria, serta kasus yang representatif; daftar kasus uji lengkap dapat ditempatkan di lampiran. Hubungan Bab 2, Bab 3, dan hasil Bab 4 perlu dipertahankan tanpa mengulang seluruh dokumen teknis di setiap bab.
