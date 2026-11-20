from pathlib import Path
import json, re, shutil

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'DOKUMEN MD/REVISI_TERPADU_2026-10-25'
SUP=ROOT/'BAB3_PENDUKUNG_2026-10-25'
contract=json.loads((OUT/'KONTRAK KEBUTUHAN.json').read_text(encoding='utf-8'))
def save(name,text): (OUT/name).write_text(text.strip()+'\n',encoding='utf-8')
def link(path,label): return f'[{label}](<{(ROOT/path).as_posix()}>)'

cases=[
('01','PU-01','Akun Admin Cabang A dan siswa B tersedia','Masuk sebagai A; minta rincian siswa B melalui halaman dan layanan','Akses ditolak dan data B tidak dikirim'),
('02','PU-02','Formulir siswa baru tersedia','Kosongkan kolom wajib; simpan; lengkapi termasuk jenjang TK; simpan kembali','Data tidak lengkap ditolak; data lengkap tersimpan pada cabang benar'),
('03','PU-03','Ruang uji berkapasitas dua belas dan kelas belum aktif','Atur kapasitas kelas melebihi ruang; perbaiki dan isi ambang sisa tempat yang sah','Kapasitas tidak sah ditolak; batas serta ambang sah dapat disimpan'),
('04','PU-04','Kelas kapasitas dua belas berisi sebelas peserta aktif','Tambahkan satu peserta yang memenuhi syarat','Peserta menjadi dua belas dan kondisi penuh ditampilkan'),
('05','PU-04','Kelas sudah penuh','Coba tambah peserta melalui antarmuka dan permintaan langsung','Penambahan ditolak dan jumlah aktif tidak berubah'),
('06','PU-04','Kelas penuh dengan riwayat peserta tersedia','Akhiri satu keanggotaan beserta alasan; masukkan kembali siswa jika syarat terpenuhi','Tempat terbuka; masuk kembali memakai interval baru tanpa menghapus yang lama'),
('07','PU-04','Dua sesi admin dan satu tempat terakhir','Kirim dua permintaan penempatan secara bersamaan','Hanya satu peserta baru aktif; kapasitas tidak terlampaui'),
('08','PU-05','Tentor yang sama memiliki jadwal berlaku di Cabang A','Buat jadwal pada cabang lain dengan hari, masa berlaku, dan jam beririsan','Peringatan irisan tentor ditampilkan tanpa membuka rincian cabang lain kepada akun yang tidak berwenang'),
('09','PU-05','Jadwal aktif, nonaktif, dan periode berbeda tersedia','Sunting jadwal tanpa mengubah jam; coba tanggal yang tidak beririsan','Tidak muncul benturan dengan dirinya sendiri atau jadwal yang tidak relevan'),
('10','PU-06','Tarif uji berbeda menurut cabang, sesi, dan siklus','Pilih siswa serta periode; terbitkan tagihan dari tarif yang tepat','Tarif sesuai cakupan, periode paket benar, dan nilai aktual tersimpan'),
('11','PU-06','Tagihan paket semester dan tagihan bulanan tersedia','Ulangi penerbitan untuk periode sama; coba penerbitan paket sebagai tagihan bulanan','Duplikasi ditolak dan paket tidak diterbitkan bulanan tanpa dasar'),
('12','PU-07','Siswa memiliki dua tagihan belum lunas','Catat pembayaran tunai untuk keduanya; ulangi permintaan yang sama','Alokasi sesuai sisa, kuitansi tunggal, dan penerimaan dihitung sekali'),
('13','PU-08','Tagihan dan rekening tujuan aktif tersedia','Unggah bukti dan ajukan pembayaran transfer','Status submitted; antrean tampil; sisa tagihan belum berkurang'),
('14','PU-08/PU-09','Pengajuan transfer telah dikembalikan beserta alasan','Buat pengajuan perbaikan melalui tindakan pengajuan ulang','Baris baru merujuk pengajuan lama; bukti dan keputusan lama tetap tersedia'),
('15','PU-09/PU-13','Pengajuan dua tagihan dan satu dana masuk sesuai tersedia','Periksa rekening, nominal, tanggal, dan referensi; setujui','Satu match dan review tersimpan; pembayaran verified; sisa berkurang sesuai alokasi'),
('16','PU-09','Pengajuan telah berhasil disetujui','Kirim ulang permintaan persetujuan, termasuk permintaan serentak','Tidak ada penerimaan, keputusan, kuitansi, atau match kedua'),
('17','PU-10','Tagihan lewat jatuh tempo dengan sisa dan nomor wali sah','Periksa pratinjau; buka tautan WhatsApp','Nomor, siswa, periode, sisa, dan jatuh tempo sesuai; log hanya tindakan tautan'),
('18','PU-10','Nomor wali tidak sah atau tagihan sudah lunas','Coba bentuk tautan dari kondisi tersebut','Tautan penagihan ditolak atau dinonaktifkan dengan alasan yang dapat dipahami'),
('19','PU-11','Pembayaran tunai sah satu cabang tersedia','Masukkan dalam kelompok kas; ajukan penyerahan; pusat mencatat penerimaan','Pembayaran asal unik; penyerah dan penerima tercatat; belum otomatis dianggap disetor bank'),
('20','PU-11/PU-13','Kas diterima pusat dan kemudian disetor ke rekening resmi','Catat setoran; cocokkan dana masuk nominal penuh; periksa total penerimaan','Status perpindahan dapat ditelusuri; setoran tidak menambah penerimaan siswa'),
('21','PU-12','Siswa mempunyai transaksi lama lalu dipindah cabang secara berwenang','Bandingkan rekap sebelum dan setelah pemindahan; telusuri rincian','Penerimaan historis tetap pada cabang transaksi dan tidak berlipat karena alokasi'),
('22','PU-13','Referensi mutasi sudah dipakai atau nominal berbeda','Coba cocokkan untuk sumber lain; coba sumber berbeda nominal','Penggunaan ulang dan pencocokan nominal tidak sesuai ditolak; selisih ditampilkan'),
('23','PU-14','Akun cabang dan akun Super Admin aktif tersedia','Ubah peran, data rekening, atau tahun aktif dengan kedua akun','Hanya kewenangan yang sah diterima; perubahan tercatat dan tahun aktif konsisten'),
('24','PU-09/PU-13/PU-14','Bukti transfer privat dan rekening resmi tersedia','Minta bukti atau referensi melalui akun tidak berwenang serta tautan langsung','Akses ditolak dan data privat tidak tersedia melalui alamat publik'),
('25','PU-08/PU-09','Dua pengajuan berbeda menunjuk sisa tagihan yang sama','Setujui pengajuan pertama; coba setujui pengajuan kedua','Validasi ulang menolak alokasi yang melampaui sisa; dana tidak dihitung ganda'),
('26','PU-03/PU-04','Kelas aktif mempunyai peserta dan ruang memadai','Pindahkan ke ruang lebih kecil atau turunkan kapasitas di bawah jumlah aktif','Perubahan yang melanggar daya tampung ditolak tanpa mengubah riwayat peserta'),
('27','PU-06','Tarif normal dan potongan yang telah diotorisasi tersedia sebagai data uji','Terbitkan tagihan dengan alasan serta pemberi persetujuan; ubah tarif berikutnya','Potongan aktual tertelusur dan tagihan lama tidak berubah'),
('28','PU-14','Cadangan basis data dan berkas bukti dari versi uji tersedia','Pulihkan pada lingkungan terpisah; periksa relasi serta akses berkas','Data dan bukti dapat diakses sesuai kewenangan tanpa ketidaksesuaian relasi'),
('29','PU-05','Ruang Cabang B dan kelas Cabang A tersedia','Buat jadwal kelas A menggunakan ruang B tanpa kebijakan lintas cabang','Penetapan tidak sah ditolak; waktu selesai harus sesudah mulai'),
('30','PU-01/PU-14','Akun cabang kehilangan penugasan atau sesi telah diakhiri','Akses ulang layanan dengan sesi lama atau cabang kosong','Tidak memperoleh akses operasional atau hak Super Admin dari cabang kosong'),
('31','PU-05','Dua kelas memiliki sesi pada ruang sama; satu kelas memiliki dua calon sesi','Buat sesi beririsan dengan tentor berbeda pada ruang sama; ulangi untuk kelas sama pada ruang berbeda','Konflik ruang dan konflik kelompok masing-masing ditampilkan; calon jadwal nonaktif sampai peninjauan selesai'),
('32','PU-09/PU-13','Pengajuan submitted dan rujukan bank cocok tersedia pada lingkungan uji','Simulasikan kegagalan penyimpanan setelah match mulai dibuat sebelum keputusan tersimpan; periksa keadaan akhir','Seluruh transaksi dibatalkan; tidak ada match, review, kuitansi, atau pelunasan sebagian yang tertinggal'),
('33','PU-12/PU-13','Kelompok kas memuat pembayaran dua bulan dan dicocokkan pada bulan ketiga','Bandingkan penerimaan dan dana cocok pada filter bulan penerimaan serta filter tanggal pencocokan','Perbandingan memakai sumber dan periode yang sama; tanggal pencocokan tidak memindahkan penerimaan atau membuat selisih palsu')]

rows='\n'.join(f'| BB-{n} | {pu} | {pre} | {steps} | {expect} | Belum diuji |' for n,pu,pre,steps,expect in cases)
save('LAMPIRAN PENGUJIAN DAN PELAKSANAAN.md','''# Lampiran rancangan pengujian dan pelaksanaan ARTHA

Lampiran ini memuat kasus uji, bentuk pencatatan PxP, dan lembar penerimaan untuk mendukung Bab 3. Seluruh kasus masih berstatus belum diuji dan tidak merupakan laporan keberhasilan aplikasi.

## 1. Kasus pengujian sistem

Nilai kapasitas, nama cabang, dan transaksi pada prasyarat merupakan data simulasi yang akan disiapkan pengembang. Versi aplikasi, kondisi awal, hasil aktual, serta penunjuk bukti harus dicatat pada saat pelaksanaan.

| Kode | Kelompok | Prasyarat atau data uji | Langkah pokok | Keluaran yang diharapkan | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
'''+rows+'''

Pengujian serentak memerlukan dua sesi atau pengirim permintaan yang benar-benar dijalankan bersamaan, bukan sekadar mengklik berurutan. Bukti mencakup permintaan, hasil masing-masing, dan pemeriksaan keadaan akhir pada versi aplikasi yang sama.

## 2. Lembar hasil kasus

Satu lembar diisi untuk satu pelaksanaan kasus pada satu versi. Ketika dilakukan uji ulang, lembar baru ditautkan pada hasil sebelumnya agar kegagalan tidak terhapus.

| Unsur | Isian saat pelaksanaan |
| :--- | :--- |
| Kode kasus, kebutuhan, dan versi | Belum dilaksanakan |
| Pelaksana, tanggal, serta lingkungan | Belum dilaksanakan |
| Data awal dan langkah aktual | Belum dilaksanakan |
| Keluaran aktual dan penunjuk bukti | Belum dilaksanakan |
| Hasil lulus, gagal, atau terhalang | Belum dilaksanakan |
| Kode galat dan hubungan uji ulang | Belum dilaksanakan |

## 3. Pencatatan waktu dan evaluasi PxP

Durasi dicatat per tugas beserta kategorinya agar waktu pengodean tidak dicampur dengan seluruh waktu proyek. Estimasi pertama diisi sebelum pengerjaan dan diperbarui pada rencana berikutnya dengan merujuk waktu aktual.

| Dokumen | Kolom yang disiapkan |
| :--- | :--- |
| Estimasi tugas | Kode tugas, KF/US, iterasi, prasyarat, uraian, kategori, estimasi jam, dasar estimasi, pelaksana |
| Waktu aktual | Kode tugas, tanggal, mulai, selesai, jeda, durasi bersih, versi, catatan |
| Galat | Kode, kasus pemicu, versi, dampak, prioritas, pelaksana perbaikan, versi perbaikan, uji ulang, status |
| Perubahan | Sumber, tanggal, kebutuhan terdampak, alasan, keputusan, pengaruh jadwal, penanggung jawab |
| Evaluasi iterasi | Rencana dan hasil, selisih waktu, galat terbuka, penyebab, tindakan berikutnya, keputusan menutup atau mengulang |

## 4. Penyiapan dan lembar UAT

Peserta menjalankan tugas sesuai kewenangan pada data simulasi setelah lingkungan lolos pemeriksaan awal. Instrumen perlu ditinjau pembimbing dan perwakilan mitra sebelum dipakai untuk keputusan penerimaan.

| Unsur | Rencana pencatatan |
| :--- | :--- |
| Pemilihan peserta | Peran, pengalaman tugas, cabang, alasan pemilihan, kesediaan; jumlah belum ditetapkan |
| Validasi isi | Nama penelaah, tanggal, pemetaan kebutuhan, catatan bahasa dan perbaikan instrumen |
| Lingkungan | Versi, URL terbatas, perangkat, peramban, jaringan, zona waktu, akun uji |
| Pengarahan | Tujuan, data simulasi, panduan, batas bantuan, persetujuan pencatatan |
| Pelaksanaan tugas | Kode UAT-01 sampai UAT-14, peserta, langkah, hasil aktual, bantuan, bukti |
| Keputusan | Diterima, memerlukan perbaikan, atau belum dievaluasi, disertai alasan |
| Tindak lanjut | Masalah, kebutuhan terdampak, versi perbaikan, tanggal uji ulang, keputusan berikutnya |
| Bukti evaluasi | Lembar keputusan atau berita acara, catatan pengamatan, tangkapan layar yang diizinkan |

Tugas UAT-01 sampai UAT-14 mengikuti urutan KF-01 sampai KF-14 pada Bab 3 dan dokumen use case. Jumlah pelaksanaan bergantung pada peserta yang berwenang, sehingga satu tugas yang dijalankan dua peserta dicatat sebagai dua pelaksanaan.

## 5. Persiapan penyerahan prototipe

Versi yang diserahkan untuk evaluasi dilengkapi panduan dan daftar keterbatasan. Penggunaan untuk operasional nyata memerlukan kesepakatan mitra tentang akses, data, dukungan, dan pencadangan.

| Urutan | Pemeriksaan atau bukti |
| :--- | :--- |
| Penyiapan lingkungan | Dependensi, konfigurasi privat, basis data, berkas, jaringan, dan zona waktu diperiksa |
| Data serta akun | Data simulasi dimuat; akun dua cabang dan pusat diperiksa kewenangannya |
| Pemeriksaan awal | Login, siswa, kelas, pembayaran, serta rekap diuji sebelum pengguna hadir |
| Pencadangan | Basis data dan berkas dicadangkan; pemulihan diperiksa pada lingkungan terpisah |
| Evaluasi | Tugas, hasil, galat, bantuan, dan keputusan dicatat |
| Perbaikan | Galat penting diperbaiki dan diuji ulang; versi sebelumnya tetap dapat ditelusuri |
| Serah uji | Versi, panduan, keterbatasan, daftar akun berwenang, dan berita acara disiapkan |

## 6. Analisis hasil yang akan digunakan

Persentase lulus menggunakan jumlah kasus lulus dibagi kasus yang dijalankan, sedangkan cakupan menggunakan kasus dijalankan dibagi kasus direncanakan. Apabila tidak ada kasus dijalankan, persentase tidak dihitung dan dilaporkan belum tersedia.

Penerimaan UAT dihitung per pelaksanaan tugas yang telah dievaluasi dengan versi serta peserta yang disebutkan. Hasil uji ulang dan tugas belum dievaluasi tetap dilaporkan, sehingga angka agregat tidak menyembunyikan galat kritis atau ketidakterwakilan proses.
''')

table_for_uc={
'00':['users','branches','activity_logs'],
'01':['students','branches','academic_years','activity_logs'],
'02':['classes','class_rooms','branches','academic_years','activity_logs'],
'03':['class_enrollments','students','classes','class_schedules','class_rooms','activity_logs'],
'04':['class_schedules','mentors','mentor_subjects','subjects','classes','class_rooms','activity_logs'],
'05':['fee_tariffs','bills','students','users','academic_years','branches','activity_logs'],
'06':['payments','payment_allocations','bills','users','activity_logs'],
'07':['payments','payment_allocations','bills','bank_accounts','users','activity_logs'],
'08':['payment_reviews','payments','payment_allocations','bills','bank_entries','bank_matches','bank_accounts','users','activity_logs'],
'09':['reminder_actions','bills','payment_allocations','payments','students','users'],
'10':['cash_batches','cash_batch_items','payments','bank_accounts','users','activity_logs'],
'11':['bank_entries','bank_matches','payments','cash_batches','cash_batch_items','bank_accounts','users','activity_logs'],
'12':['branches','students','classes','class_enrollments','class_schedules','mentors','subjects','bills','payments','payment_allocations','payment_reviews','cash_batches','cash_batch_items','bank_entries','bank_matches','reminder_actions'],
'13':['academic_years','branches','users','subjects','mentors','mentor_subjects','bank_accounts','activity_logs']}
matrix=[]
for f in contract['functions']:
    group=f['test_group']
    matrix.append({**f,'priority':'Inti','tables':table_for_uc[f['uc'][-2:]],'bb':[f'BB-{n}' for n,groups,*_ in cases if group in groups.split('/')],'implementation_status':'Belum diuji','partner_validation':'Keputusan WhatsApp dan penuh dari pengguna; kebijakan mitra terkait perlu validasi'})
(OUT/'MATRIKS_KETERLACAKAN.json').write_text(json.dumps(matrix,ensure_ascii=False,indent=2),encoding='utf-8')
rows='\n'.join('| '+' | '.join([f['kf'],'/'.join(f['sources']),f['us'],f['uc'],f['iteration'],f['test_group'],', '.join(f['bb']),f['uat'],', '.join('`'+x+'`' for x in f['tables'])])+' |' for f in matrix)
save('MATRIKS KETERLACAKAN KEBUTUHAN.md','''# Matriks keterlacakan kebutuhan ARTHA

Matriks ini menghubungkan kebutuhan dengan sumber, cerita pengguna, use case, iterasi, pengujian, dan tabel. Seluruh baris merupakan rancangan dan tidak menyatakan aplikasi telah lulus pengujian atau semua kebijakan telah disahkan mitra.

## 1. Pemetaan inti

Kode sumber S-01 sampai S-07 mengikuti Tabel 3.2 pada Bab 3. Kelompok PU merupakan kelompok pemeriksaan, sedangkan kode BB menunjuk kasus rinci pada lampiran pengujian.

| KF | Sumber | US | UC | Iterasi | Kelompok | Kasus BB | UAT | Tabel utama |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
'''+rows+'''

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
''')

source_info=[
('S-01','WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA PERTAMA ARTHA_WITH_TIMESTAMPS.txt','Wawancara pertama','Pendaftaran dan pilihan layanan; telusuri sesuai topik pada rekaman'),
('S-02','WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA KEDUA SKRIPSI (OM ANANG)_WITH_TIMESTAMPS.txt','Om Anang','Sistem lama dan kebutuhan integrasi; konfirmasi batas halaman publik'),
('S-03','WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA KETIGA SKRIPSI (MAMA RADIT)_WITH_TIMESTAMPS.txt','Mama Radit','48:18 sampai 48:24 menyebut potongan Rp200.000; konteks dan pengulangan belum dipastikan'),
('S-04','WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt','Frontdesk','14:17 sampai 14:36 tarif sesi; 19:18 sampai 20:51 potongan; 45:19 sampai 46:30 ruang; 50:38 sampai 52:42 laporan serta bukti; 58:19 sampai 59:25 jatuh tempo'),
('S-05a','BIMBINGAN/BU AYU/TRANSKRIP TEKS (TXT)/BIMBINGAN KE-1 (Bu Ayu)_WITH_TIMESTAMPS.txt','Bimbingan Bu Ayu','Batas lingkup, keluwesan aturan, potongan, dan evaluasi; gunakan konteks arahan'),
('S-05b','BIMBINGAN/PAK ARIF/TRANSKRIP TEKS (TXT)/BIMBINGAN KE 5 (Pak Arif)_WITH_TIMESTAMPS.txt','Bimbingan Pak Arif','Jalur prototipe, pemilihan metode, dan pemisahan antarmuka')]
sr='\n'.join(f'| {code} | {link(path,label)} | {scope} |' for code,path,label,scope in source_info)
save('SUMBER KEBUTUHAN DAN KEPUTUSAN TERBUKA.md','''# Sumber kebutuhan dan keputusan yang perlu divalidasi

Sumber lapangan dipakai sesuai peran dan konteks cabangnya. Dokumen notulensi merupakan ringkasan yang perlu dicocokkan kembali dengan transkrip serta rekaman ketika terdapat perbedaan atau bagian yang ambigu.

## 1. Indeks bukti

Penanda waktu membantu pemeriksaan manual terhadap bagian transkrip yang sudah ditelusuri. Indeks ini tidak mengklaim bahwa semua tanggal atau setiap kesimpulan dalam notulensi telah disahkan narasumber.

| Kode | Berkas | Topik dan lokator |
| :--- | :--- | :--- |
'''+sr+'''

Notulensi wawancara pertama sampai ketiga menuliskan tanggal 28, 29, dan 30 Juli 2026 dengan nama hari yang tidak cocok dengan kalender tahun tersebut. Notulensi frontdesk juga menyebut hari Minggu untuk 20 Oktober 2026, sehingga tanggal lapangan belum ditetapkan sebagai fakta final pada Bab 3.

## 2. Register keputusan

Keputusan pengguna dipakai sebagai dasar rancangan yang telah diotorisasi untuk penulisan. Persetujuan pengguna atas penyusunan dokumen tidak dinyatakan sebagai pengesahan kebijakan seluruh mitra.

| Topik | Kedudukan saat revisi | Tindak lanjut |
| :--- | :--- | :--- |
| WhatsApp melalui tombol | Keputusan pengguna | Periksa nomor dan format pesan pada data uji; admin mengirim manual |
| Kelas penuh menolak penambahan | Keputusan pengguna | Tetapkan kapasitas tiap kelas dan ruang serta ambang hampir penuh |
| Transfer Admin mengajukan, Super Admin memeriksa | Rancangan kerja yang diusulkan | Pastikan akses rekening, petugas, dan kewenangan sebelum membekukan kebutuhan |
| Tunai dicatat lalu diserahkan ke pusat | Rancangan berdasarkan proses yang ditelusuri | Tetapkan penerima, jadwal penyerahan, dan kapan disetor ke bank |
| Pembayaran sebagian | Belum ditetapkan; tidak aktif pada rancangan awal | Konfirmasi kemungkinan cicilan dan aturan alokasinya |
| Satu dana masuk untuk satu sumber penuh | Batas rancangan prototipe | Periksa apakah dana gabungan atau selisih memerlukan perluasan lingkup |
| Tarif dan potongan | Nominal global tidak dipatok | Kumpulkan ketentuan berlaku menurut cabang, sesi, siklus, dan kewenangan |
| Potensi benturan jadwal | Pemeriksaan preventif dan peringatan | Tetapkan penanganan pengecualian; jangan mengklaim kejadian berulang tanpa bukti |
| Daftar tunggu dan promosi otomatis | Di luar rancangan inti | Evaluasi sebagai pengembangan berikutnya bila diperlukan |
| Notifikasi surel atau WhatsApp otomatis | Di luar inti | Antrean dasbor cukup untuk rancangan awal; status baca perlu perluasan model |
| Peserta UAT serta jadwal kalender | Belum disepakati | Tetapkan petugas yang mewakili kedua peran dan waktu pelaksanaan |

## 3. Penyelarasan Bab 1 dan Bab 2

Bab 1 dan Bab 2 tidak diubah dalam pekerjaan ini karena keputusan pembayaran dan beberapa parameter masih perlu validasi mitra. Perubahan berikut perlu diterapkan setelah rancangan pelaksanaan ditetapkan agar isi antar bab tidak bertentangan.

| Bagian | Perubahan yang perlu dilakukan |
| :--- | :--- |
| Batasan Bab 1 tentang verifikasi Admin | Sesuaikan menjadi pengajuan Admin dan keputusan Super Admin bila rancangan disetujui |
| Istilah waktu nyata | Jelaskan data terbaru yang dimuat dari layanan; jangan menjanjikan pembaruan serentak tanpa pengujian |
| Rekonsiliasi | Batasi pada pencocokan penerimaan manual; pisahkan tunggakan dari selisih bank |
| Kapasitas dan jadwal | Bedakan penolakan kelas penuh dari peringatan potensi benturan tentor |
| Bab 2 tentang UAT | Selaraskan dengan instrumen berbasis tugas; kuesioner persepsi memerlukan rancangan tambahan sendiri |
| Bab 2 tentang model data dan teknologi | Gunakan model revisi serta versi aktual saat implementasi, bukan spesifikasi artikel sebagai fakta ARTHA |
| Rumusan masalah, tujuan, hasil | Pertahankan tiga arah tujuan dan rujuk bukti pengujian yang relevan setelah tersedia |

## 4. Batas pemeriksaan sumber pustaka

Sitasi jurnal, prosiding, dan peta halamannya dipertahankan dari audit sumber Bab 3 yang telah tersedia. Revisi ini tidak merupakan audit akreditasi SINTA baru untuk seluruh jurnal atau pemeriksaan SK tiap edisi.

Metadata yang masih terbuka tetap mengikuti catatan daftar pustaka pendamping. Penilaian kesiapan seminar harus mempertimbangkan keputusan mitra, kelengkapan instrumen, serta tata letak akhir, bukan hanya kelulusan pemeriksaan struktur Markdown.
''')

# Keep the prior source ledger, update only boundaries changed by the authorised revision.
lp=SUP/'PETA_SUMBER_DAN_SUBBAB.json'
backup=OUT/'SEBELUM_REVISI'/lp.name
if not backup.exists():shutil.copy2(lp,backup)
ledger=json.loads(lp.read_text(encoding='utf-8'))
ledger['revision']='2026-10-25 integrated UC/schema/chapter revision; sources unchanged'
for row in ledger['sections']:
    if row['section']=='3.5.1':row['boundary']='Arsitektur rancangan; antrean pending diturunkan dari submitted. Notifikasi dengan status baca adalah perluasan opsional yang belum dimodelkan.'
    if row['section']=='3.4.6':row['boundary']='Skema revisi 23 tabel dan hubungan alokasi/pemeriksaan/setoran/pencocokan; belum DDL yang dieksekusi.'
    if row['section']=='3.4.7':row['boundary']='Enam wireframe dengan data simulasi; bukan bukti implementasi atau penerimaan mitra.'
lp.write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'test_cases':len(cases),'functional_rows':len(matrix),'coverage_cases':len(set(x for f in matrix for x in f['bb']))},ensure_ascii=False))
