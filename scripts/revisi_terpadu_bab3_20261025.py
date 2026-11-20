from pathlib import Path
import re, json, hashlib, shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'DOKUMEN MD/REVISI_TERPADU_2026-10-25'
SUP = ROOT/'BAB3_PENDUKUNG_2026-10-25'
CH = ROOT/'BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md'
BACK = OUT/'SEBELUM_REVISI'
BACK.mkdir(parents=True, exist_ok=True)
if not (BACK/CH.name).exists(): shutil.copy2(CH, BACK/CH.name)
original = (BACK/CH.name).read_text(encoding='utf-8')
t = original
table_map = {1:1,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:14,13:15,14:17,15:18,16:19,17:20}
t = re.sub(r'Tabel 3\.(\d+)\b', lambda m:'Tabel 3.'+str(table_map[int(m[1])]), t)

def section(key, text):
    global t
    pattern = r'(^#{2,3} '+re.escape(key)+r' [^\n]+\n)(.*?)(?=^#{2,3} 3\.|\Z)'
    assert len(re.findall(pattern,t,re.M|re.S)) == 1, key
    t = re.sub(pattern,lambda m:m[1]+'\n'+text.strip()+'\n\n',t,flags=re.M|re.S)

def link(path, label): return f'[{label}](<{(ROOT/path).as_posix()}>)'
def fig(n, name, alt, caption, explanation):
    path=(SUP/'gambar'/name).as_posix()
    return f'Gambar 3.{n} memperlihatkan rancangan {caption.lower()}. {explanation}\n\n![{alt}](<{path}.png>)\n\n**Gambar 3.{n} {caption}**\n\nSumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.'

section('3.1', '''Prototipe ARTHA berupa sistem informasi manajemen operasional berbasis web untuk Bimbel Artha Balikpapan. Sistem menghubungkan administrasi siswa, kelas, jadwal, tagihan, dan penerimaan pada delapan cabang melalui kewenangan Admin Cabang serta Super Admin.''')
section('3.1.1', '''Kebutuhan pengembangan bersumber dari dokumentasi wawancara pengelola dan staf administrasi Artha. Penelitian sistem bimbel digunakan sebagai pembanding integrasi data siswa, jadwal, dan pembayaran (Fajriansyah dkk., 2026, hlm. 116, 124 sampai 125; Gunawan dkk., 2025, hlm. 424).''')
section('3.1.2', '''Admin Cabang mengelola kegiatan pada cabang penugasannya, sedangkan Super Admin memantau lintas cabang dan menjalankan pengendalian berwenang. Pemisahan akses cabang dan pemantauan pusat mempunyai pembanding pada Ahadi dkk. (2025, hlm. 764 sampai 765) serta Thiovanda (2026, hlm. 4).

Pengingat tunggakan menggunakan tombol WhatsApp dengan nomor dan pesan yang disiapkan sistem, kemudian dikirim oleh admin. Pengelolaan kelas menyediakan peringatan hampir penuh dan menolak penambahan ketika penuh, sementara tempat kembali tersedia setelah keanggotaan siswa diakhiri.

Pembayaran transfer dirancang melalui pengajuan Admin Cabang dan pemeriksaan Super Admin, dengan kewenangan rekening yang akan divalidasi bersama mitra. Lingkup inti mencakup administrasi internal dan pencocokan penerimaan manual, sedangkan pengiriman WhatsApp otomatis, integrasi bank otomatis, serta pembelajaran daring berada di luar lingkup tersebut.''')
section('3.1.3', '''Pengembangan individual menggunakan metode *Personal Extreme Programming* (PxP), yang meliputi penggalian kebutuhan, perencanaan, inisialisasi iterasi, perancangan, implementasi, pengujian sistem, dan evaluasi iterasi (Dzhurov dkk., 2009, hlm. 253 sampai 256). Penelitian Fikri dan Arthawan Sugih Prabowo (2021, hlm. 103 sampai 105) menjadi pembanding penerapannya pada pengembangan sistem informasi.''')
section('3.1.4', '''Luaran yang ditargetkan meliputi perangkat lunak prototipe, dokumentasi pengembangan, dan bukti evaluasi bersama calon pengguna. Pengembangan diarahkan pada TKT 5 sesuai panduan tugas akhir prototipe, dengan bukti pencapaian yang akan diperiksa berdasarkan pelaksanaan (Institut Teknologi Kalimantan, 2026, hlm. 4).

Dokumentasi disiapkan untuk laporan, artikel ilmiah, dan bahan pengajuan HKI. Hasil pengujian dan penerimaan mitra akan dilaporkan setelah kegiatan dilaksanakan.''')

# Preserve the stage table and its citations; add explicit decision semantics.
t=t.replace('Apabila masih terdapat fungsi yang direncanakan, pengembangan dilanjutkan ke inisialisasi iterasi berikutnya. Apabila masukan pengguna mengubah kebutuhan, perubahan dicatat dan dinilai kembali sebelum dimasukkan dalam rencana pekerjaan.',
'''Hasil pengujian yang belum memenuhi kriteria dikembalikan ke implementasi untuk diperbaiki dan diuji ulang sebelum iterasi ditutup. Setelah evaluasi iterasi, pekerjaan tersisa diarahkan ke inisialisasi berikutnya, sedangkan fungsi yang siap diarahkan ke UAT.

Masukan UAT yang mengubah kebutuhan dikembalikan ke penggalian kebutuhan serta perencanaan. Masukan yang hanya memerlukan koreksi fungsi dikembalikan ke pekerjaan perbaikan, kemudian diuji ulang sebelum keputusan penerimaan dan penyiapan luaran.''')

sources = '''Tabel 3.2 membedakan dokumen yang telah tersedia dari klarifikasi yang masih direncanakan. Tanggal pelaksanaan akan dicocokkan dengan bukti asli karena penulisan tanggal pada notulensi belum seluruhnya tervalidasi.

**Tabel 3.2 Sumber Kebutuhan dan Status Bukti**

| Kode | Sumber dan cakupan | Informasi yang digunakan | Tanggal dan status |
| :--- | :--- | :--- | :--- |
| S-01 | Wawancara pertama pengelola | Pendaftaran, paket, dan kebutuhan administrasi | Transkrip tersedia; tanggal perlu pemeriksaan |
| S-02 | Wawancara kedua, Om Anang | Sistem lama, kebutuhan integrasi, dan akses cabang | Transkrip tersedia; tanggal perlu pemeriksaan |
| S-03 | Wawancara ketiga, Mama Radit | Tarif, potongan, penerimaan, dan pencocokan bank | Transkrip tersedia; tanggal perlu pemeriksaan |
| S-04 | Wawancara frontdesk, konteks Cabang 5 | Pelaksanaan pendaftaran, jatuh tempo, ruang, dan pelaporan harian | Transkrip tersedia; cakupan cabang diklarifikasi |
| S-05 | Bimbingan Bu Ayu dan Pak Arif | Batas lingkup, keluwesan aturan, metode, dan evaluasi | Transkrip tersedia; arahan dipetakan ke rancangan |
| S-06 | Penjelasan pengguna selama penyusunan | WhatsApp manual dan penolakan kelas penuh | Keputusan rancangan pengguna; bukan persetujuan seluruh mitra |
| S-07 | Pengelola keuangan dan admin yang ditunjuk | Pemeriksa rekening, tarif berlaku, setoran, serta parameter kapasitas | Klarifikasi lanjutan belum dilaksanakan |

Indeks berkas, penanda waktu, dan batas penafsiran disimpan pada lampiran sumber kebutuhan. Catatan tarif atau peristiwa pada satu cabang digunakan sesuai konteksnya sampai pengelola menetapkan cakupan yang lebih luas.'''
anchor='Wawancara lanjutan dilakukan secara semiterstruktur'
idx=t.index(anchor)
t=t[:idx]+sources+'\n\n'+t[idx:]

section('3.3.2', '''Perencanaan dilakukan dengan memecah kebutuhan menjadi tugas analisis, perancangan, pengodean, pengujian, dan perbaikan. Estimasi awal menggunakan rincian pekerjaan, kemudian diperbarui berdasarkan durasi aktual pada tugas sejenis (Dzhurov dkk., 2009, hlm. 254 sampai 255).

Empat iterasi diusulkan berdasarkan ketergantungan data dan proses pada Tabel 3.4. Akun, cabang, siswa, kelas, dan tarif menjadi prasyarat penempatan, penjadwalan, transaksi, serta rekap pusat.

**Tabel 3.4 Rencana Iterasi dan Ketergantungan Kebutuhan**

| Iterasi | Kebutuhan dan cerita pengguna | Lingkup pekerjaan | Prasyarat dan keluaran |
| :--- | :--- | :--- | :--- |
| I-01 | KF-01, KF-02, KF-03, KF-06, KF-14; US dengan nomor yang sama | Akun, cabang, siswa, ruang, kelas, serta dasar tarif dan tagihan | Data dasar dan pembatasan akses dapat diperiksa |
| I-02 | KF-04, KF-05; US-04 dan US-05 | Keanggotaan, kapasitas, jadwal, serta pemeriksaan irisan | Master I-01 tersedia; kelas penuh dan konflik diuji |
| I-03 | KF-07, KF-08, KF-09, KF-10; US dengan nomor yang sama | Tunai, pengajuan transfer, pemeriksaan, serta tautan WhatsApp | Tagihan tersedia; layanan pencocokan transfer dasar dibuat agar verifikasi dapat diuji |
| I-04 | KF-11, KF-12, KF-13; US dengan nomor yang sama | Setoran, rekap pusat, pencocokan, serta integrasi | Penerimaan I-03 tersedia; transaksi sumber dapat ditelusuri |

Pencocokan transfer pada I-03 memakai komponen dasar rekening dan referensi bank yang diperlukan untuk persetujuan. Pada I-04, komponen tersebut diperluas untuk pencocokan setoran tunai dan rekap lintas proses.

Setiap iterasi dialokasikan dua minggu sebagai rencana awal dalam rentang iterasi PxP satu sampai tiga minggu (Dzhurov dkk., 2009, hlm. 255). Rincian jam per tugas belum ditetapkan dan akan diisi sebelum iterasi dimulai, sedangkan kalender dua belas minggu pada Subbab 3.6 masih bersifat relatif.

Permintaan perubahan dicatat bersama sumber, kebutuhan terdampak, ketergantungan, serta pengaruhnya terhadap waktu dan pengujian. Formulir estimasi dan perubahan ditempatkan pada lampiran pelaksanaan agar penambahan pekerjaan tetap dapat ditelusuri.''')

section('3.3.6', '''Pengujian sistem menggunakan pendekatan kotak hitam atau *Black Box Testing* untuk memeriksa keluaran terhadap kebutuhan. Penerapannya bersama PxP mempunyai pembanding pada Apriyanti dkk. (2024, hlm. 3679, 3683), sedangkan kasus ARTHA disusun dari aturan akses, kelas, dan transaksi.

Pengembang melaksanakan pemeriksaan pada lingkungan uji terpisah dengan data buatan atau tersamarkan. Identitas versi, perangkat, zona waktu, dan data awal dicatat sebelum kasus dijalankan agar hasil dapat diperiksa ulang.

Tabel 3.5 menampilkan contoh kasus berisiko, sedangkan seluruh kasus BB-01 sampai BB-33 disimpan pada lampiran pengujian. Kelompok pemeriksaan PU-01 sampai PU-14 menghubungkan kasus tersebut dengan kebutuhan fungsional pada Tabel 3.13.

**Tabel 3.5 Contoh Kasus Pengujian Sistem**

| Kode | Kondisi yang diperiksa | Keluaran yang diharapkan | Pelaksanaan |
| :--- | :--- | :--- | :--- |
| BB-01 | Akun cabang meminta objek cabang lain | Akses ditolak dan objek tidak dikirim | Belum diuji |
| BB-07 | Dua permintaan mengisi satu tempat terakhir | Hanya satu keanggotaan aktif baru tersimpan | Belum diuji |
| BB-14 | Pengajuan dikembalikan kemudian diajukan ulang | Pengajuan lama tetap tersimpan dan pengajuan baru tertaut | Belum diuji |
| BB-16 | Persetujuan transfer dikirim berulang | Penerimaan, alokasi, serta pencocokan hanya berlaku sekali | Belum diuji |
| BB-17 | Admin membuka pesan tunggakan | Nomor dan isi sesuai; pembukaan tidak dianggap bukti terkirim | Belum diuji |
| BB-20 | Setoran kas dicocokkan dengan dana bank | Status setoran berubah tanpa menambah penerimaan siswa | Belum diuji |

Setiap kasus merekam prasyarat, langkah, masukan, keluaran yang diharapkan, hasil aktual, serta bukti pelaksanaan. Galat kritis meliputi akses cabang tanpa kewenangan, penghitungan pembayaran ganda, dan pelampauan kapasitas kelas.

Perbaikan diperiksa melalui pengulangan kasus gagal beserta kasus terkait. Hasil sebelum perbaikan tetap disimpan dan dihubungkan dengan versi yang diperiksa ulang.''')

# Retain PxP retrospective table, shorten repeated interpretive audit prose.
t=t.replace('Data ini tidak digunakan untuk menyimpulkan PxP lebih unggul daripada metode lain karena penelitian tidak merancang eksperimen pembandingan metode.',
'Formulir lengkap catatan waktu, galat, perubahan, dan evaluasi ditempatkan pada lampiran pelaksanaan.')

uat_rows = [
('A dan S','Masuk, memeriksa cakupan akses, dan keluar','Akun sesuai peran dan data cabang lain terlindungi'),
('A','Mendaftarkan dan memperbarui siswa','Data wajib benar dan riwayat tetap tersedia'),
('A dan S','Menyiapkan kelas serta ruang','Batas kelas sesuai ruang dan parameter terlihat'),
('A','Menambah peserta, memeriksa penuh, lalu mengakhiri keanggotaan','Penambahan ditolak saat penuh dan tempat kembali tersedia setelah keluar'),
('A','Menyusun serta menyunting jadwal','Irisan relevan ditampilkan tanpa benturan dengan jadwal sendiri'),
('A dan S','Memilih tarif dan menerbitkan tagihan periode','Tarif tepat dan tagihan tidak terbit ganda'),
('A','Mencatat uang tunai dan mencetak kuitansi','Penerimaan sah tercatat satu kali'),
('A','Mengajukan transfer untuk beberapa tagihan siswa yang sama','Alokasi benar dan pengajuan belum melunasi tagihan'),
('S','Memeriksa transfer, mengembalikan, atau menyetujui','Keputusan dan referensi dana masuk dapat ditelusuri'),
('A','Membuka pesan WhatsApp dari tunggakan','Nomor, periode, nominal, dan jatuh tempo sesuai'),
('A dan S','Menyerahkan serta menerima setoran tunai','Daftar pembayaran sumber dan petugas tercatat'),
('A dan S','Menelusuri ringkasan ke transaksi sumber','Total, periode, cabang, dan status sesuai'),
('S','Mencocokkan penerimaan dengan contoh mutasi','Referensi tidak dipakai ganda dan setoran tidak menjadi pendapatan baru'),
('S','Mengelola akun dan data induk','Perubahan hanya dilakukan petugas berwenang')]
uat_table='\n'.join(f'| UAT-{i:02} | {a} | {b} | {c} |' for i,(a,b,c) in enumerate(uat_rows,1))
section('3.3.8', '''Pengujian penerimaan pengguna atau *User Acceptance Testing* (UAT) dilakukan bersama petugas yang menjalankan administrasi cabang dan pengawasan pusat. Pemilihan peserta dilakukan secara bertujuan menurut kewenangan, pengalaman tugas, kesediaan, dan cakupan proses yang diuji.

Rencana peserta mencakup sekurang-kurangnya perwakilan kedua peran, sedangkan nama, jumlah akhir, cabang, serta waktu pertemuan ditetapkan bersama mitra. Petugas yang sama dapat menilai beberapa tugas sesuai kewenangannya, tetapi penerimaan satu cabang tidak digeneralisasi sebagai pendapat seluruh delapan cabang.

Sebelum UAT, pengembang menyiapkan versi uji, cadangan awal, akun terpisah, data simulasi, dan panduan singkat. Pemeriksaan awal memastikan fungsi inti dapat dijalankan serta peserta hanya memperoleh hak yang diperlukan untuk tugasnya.

Pelaksanaan diawali pengarahan tujuan, penjelasan data uji, dan persetujuan pencatatan bukti. Peserta kemudian menjalankan tugas tanpa perubahan langkah yang tidak terdokumentasi, sedangkan pengembang mengamati, mencatat bantuan yang diberikan, dan menyimpan hasil sesuai kode tugas.

Tabel 3.7 merangkum tugas penerimaan dengan A sebagai Admin Cabang dan S sebagai Super Admin. Lembar rinci memuat identitas peserta atau kode, versi aplikasi, langkah, hasil aktual, bantuan, keputusan, alasan, serta penunjuk bukti.

**Tabel 3.7 Rancangan Tugas Penerimaan Berdasarkan Kebutuhan**

| Kode | Peran | Tugas | Dasar penerimaan |
| :--- | :--- | :--- | :--- |
'''+uat_table+'''

Instrumen diperiksa keterbacaan dan kesesuaian isinya oleh pembimbing serta perwakilan mitra sebelum pelaksanaan. Penggunaan evaluasi bersama pengguna mempunyai pembanding pada Apriyanti dkk. (2024, hlm. 3683 sampai 3685), sedangkan instrumen ARTHA berbentuk tugas operasional.

Setiap pelaksanaan tugas diberi keputusan diterima, memerlukan perbaikan, atau belum dapat dievaluasi, disertai alasan. Kegagalan akibat data yang belum tersedia dibedakan dari galat aplikasi, kemudian tugas yang diperbaiki diuji ulang pada versi yang dicatat.

Analisis pengujian sistem menyajikan jumlah kasus direncanakan, dijalankan, lulus, gagal, dan belum dijalankan. Persentase kelulusan dihitung terhadap kasus yang dijalankan, sedangkan cakupan pelaksanaan dihitung terhadap kasus yang direncanakan.

Analisis UAT menggunakan satuan pelaksanaan tugas per peserta dan per versi yang dinyatakan jelas. Penerimaan dihitung dari pelaksanaan tugas yang diterima dibagi pelaksanaan tugas yang telah dievaluasi, sedangkan tugas belum dievaluasi serta hasil uji ulang tetap dilaporkan terpisah.

Penerimaan menyeluruh memerlukan selesainya tugas penting dan tidak adanya galat kritis yang terbuka. Hasil dibahas menurut integrasi fungsi, pemantauan penerimaan, dan kesesuaian kebutuhan, tanpa menyatakan penghematan waktu apabila pengukuran pembanding tidak dilakukan.

Setelah tindak lanjut, pengembang menyiapkan versi serah uji, panduan penggunaan, daftar keterbatasan, prosedur pencadangan, dan berita acara evaluasi. Penyerahan untuk pemakaian operasional dilakukan sesuai persetujuan mitra, sehingga akses uji tidak otomatis diperlakukan sebagai penerapan produksi.''')

# KF dictionary is shared by all revised artefacts.
functions = [
('Autentikasi dan kewenangan','Akses berdasarkan peran serta cabang; sesi dapat diakhiri','00',1,'S-02/S-05'),
('Pengelolaan siswa','Identitas, kontak wali, jenjang termasuk TK, dan status tercatat','01',1,'S-01/S-04'),
('Pengelolaan kelas dan ruang','Kapasitas kelompok, kapasitas ruang, serta ambang hampir penuh tersedia','02',1,'S-04/S-06'),
('Keanggotaan dan kapasitas','Peserta aktif dihitung, kelas penuh ditolak, dan keluar membuka tempat','03',2,'S-06'),
('Pengelolaan jadwal','Irisan tentor dan ruang diperiksa menurut masa berlaku','04',2,'S-02/S-04/S-05'),
('Tarif dan tagihan','Variasi cabang, sesi, siklus, potongan berwenang, dan periode tersimpan','05',1,'S-01/S-03/S-04'),
('Penerimaan tunai','Penerimaan, alokasi tagihan, dan kuitansi dicatat satu kali','06',3,'S-03/S-04'),
('Pengajuan transfer','Bukti dan alokasi diajukan tanpa langsung melunasi tagihan','07',3,'S-03/S-06/S-07'),
('Pemeriksaan transfer','Persetujuan atau pengembalian beserta riwayat keputusan tersimpan','08',3,'S-03/S-06/S-07'),
('Tautan WhatsApp','Nomor dan pesan tunggakan disiapkan untuk dikirim oleh admin','09',3,'S-04/S-06'),
('Setoran tunai','Penyerahan ke pusat dibedakan dari penyetoran ke rekening','10',4,'S-03/S-04/S-07'),
('Dasbor dan laporan','Data cabang serta antrean pemeriksaan ditelusuri ke transaksi sumber','12',4,'S-02/S-03'),
('Pencocokan penerimaan','Transfer atau setoran dihubungkan ke referensi bank secara manual','11',4,'S-03/S-07'),
('Data induk dan akun','Tahun ajaran, cabang, akun, tentor, mapel, dan rekening diatur berwenang','13',1,'S-02/S-05/S-07')]
fc_rows='\n'.join(f'| KF-{i:02} | {a} | {b} |' for i,(a,b,*_) in enumerate(functions,1))
start=t.index('| KF-01 |',t.index('**Tabel 3.9 ')); end=t.index('\n\n',start)
t=t[:start]+fc_rows+t[end:]
t=t.replace('kelas dengan jumlah peserta sama dengan kapasitas selalu berstatus penuh.',
'kondisi penuh dihitung dari jumlah peserta aktif dan tidak menggantikan status operasional kelas.')
t=t.replace('Peringatan konflik ditampilkan sebelum jadwal ditetapkan','Peringatan konflik ditampilkan sebelum jadwal ditetapkan')
t=t.replace('Ambang tersebut tidak boleh melampaui kapasitas,', 'Ambang sisa tempat bernilai satu sampai kapasitas kelas,')

# Replace business rules with bounded, coherent payment semantics; retain relevant journal references.
section('3.4.1', '''Proses usulan menghubungkan pencatatan cabang dengan pengawasan pusat melalui transaksi yang dapat ditelusuri. Kajian penerimaan SPP pada Hendri dkk. (2025, hlm. 124 sampai 125) digunakan sebagai pembanding pencatatan serta penelusuran bukti.

Tabel 3.8 merangkum perubahan proses yang dirancang. Rincian kebijakan pembayaran dan petugas pemeriksa akan divalidasi kepada pihak yang mempunyai kewenangan rekening.

**Tabel 3.8 Proses Berjalan dan Proses Usulan**

| Proses | Dasar yang ditelusuri | Rancangan usulan |
| :--- | :--- | :--- |
| Pendaftaran | Catatan siswa dan pilihan layanan pada cabang | Identitas siswa terpusat dengan pembatasan akses cabang |
| Kelas | Pemeriksaan peserta dan ruang oleh petugas | Hitungan peserta aktif, peringatan hampir penuh, dan penolakan saat penuh |
| Jadwal | Catatan serta komunikasi pengelola | Pemeriksaan irisan tentor dan ruang menurut hari, waktu, serta masa berlaku |
| Penagihan | Jatuh tempo dan pengingat oleh admin | Daftar tunggakan, pratinjau pesan, serta tombol WhatsApp manual |
| Transfer | Bukti disampaikan kepada pihak pengelola | Pengajuan Admin Cabang, pemeriksaan dana masuk, dan keputusan Super Admin |
| Tunai dan setoran | Penerimaan cabang dan penyerahan kepada pusat | Pembayaran siswa, penyerahan kas, serta setoran bank dicatat terpisah |
| Pelaporan | Penghimpunan catatan cabang | Rekap berdasarkan transaksi sah, periode, kanal, dan cabang historis |

Satu pembayaran dirancang untuk satu siswa dan satu cabang transaksi, dengan alokasi ke satu atau beberapa tagihan. Jumlah alokasi harus sama dengan nominal pembayaran, sedangkan tagihan yang dipilih harus berasal dari siswa serta cabang yang sama.

Transfer diajukan dengan status menunggu verifikasi dan belum mengurangi sisa tagihan. Persetujuan dilakukan setelah pemeriksa berwenang mencocokkan dana masuk; pengembalian menyimpan alasan, sedangkan perbaikan diajukan sebagai transaksi baru yang tertaut pada pengajuan sebelumnya.

Pembayaran tunai dihitung sebagai penerimaan setelah uang diterima dan pencatatan diselesaikan. Pada rancangan awal, setiap tagihan yang dipilih dilunasi sebesar sisa kewajibannya; fasilitas cicilan baru diaktifkan jika kebijakannya telah divalidasi.

Penyerahan kas ke pusat memuat pembayaran asal, penyerah, penerima, dan waktu penerimaan. Penyetoran ke bank merupakan tahap berikutnya yang mempunyai rekening, bukti, serta waktu sendiri, sehingga keduanya tidak menghasilkan pendapatan siswa yang baru.

Pencocokan prototipe dibatasi pada satu dana masuk bank untuk satu transfer siswa atau satu setoran kas dengan nominal penuh yang sama. Dana gabungan beberapa sumber, selisih biaya, serta pencocokan sebagian ditandai untuk tindak lanjut di luar cakupan pencocokan prototipe.

Pemisahan pencatatan pusat dan cabang mempunyai pembanding pada Ramadhan dan Widodo (2026, bagian pembahasan). Sudirman dan Tristianti (2021, hlm. 126 sampai 127) menjadi acuan pembahasan pencocokan catatan internal dengan bank, sedangkan sisa tagihan siswa disajikan terpisah dari selisih pencocokan.''')

# Access table updates: dashboard queue requires no persistent notification table.
t=t.replace('| Tarif dan parameter | Menggunakan ketentuan yang berlaku | Mengelola ketentuan sesuai persetujuan mitra |',
'| Tarif dan parameter kelas | Menggunakan tarif; mengelola kelas sesuai penugasan | Menetapkan tarif, kapasitas, dan ambang sesuai kewenangan |')
t=t.replace('| Transfer siswa | Mengajukan bukti dan memperbaiki pengajuan | Memeriksa dan mengambil keputusan verifikasi |',
'| Transfer siswa | Mengajukan bukti dan membuat pengajuan ulang yang tertaut | Memeriksa dana masuk serta menyetujui atau mengembalikan |')

us=[
('Pengguna masuk dan keluar sesuai peran','Akses data sesuai tugas','Akses Admin Cabang ke cabang lain ditolak; Super Admin sesuai kewenangan; sesi keluar tidak dapat dipakai'),
('Admin mendaftarkan serta memperbarui siswa','Data siswa dapat ditelusuri','Data wajib lengkap; penonaktifan tidak menghapus transaksi'),
('Admin menyiapkan kelas; Super Admin menetapkan ruang dan kapasitas','Batas peserta terlihat sebelum penempatan','Kapasitas kelas sesuai ruang dan ambang sisa tempat tersimpan'),
('Admin mengelola masuk dan keluar kelas','Tempat tersedia serta riwayat benar','Penuh menolak penambahan; keluar membuka satu tempat'),
('Admin menyusun jadwal','Potensi irisan diketahui','Konflik tentor lintas cabang dan ruang terkait ditampilkan'),
('Super Admin menetapkan tarif dan Admin menerbitkan tagihan','Kewajiban mengikuti ketentuan berlaku','Cabang, sesi, periode, potongan, serta nilai historis tepat'),
('Admin menerima pembayaran tunai','Penerimaan sah dan kuitansi tercatat','Total alokasi benar dan pengiriman ulang tidak menggandakan transaksi'),
('Admin mengajukan transfer','Bukti dapat diperiksa pusat','Status menunggu; beberapa tagihan satu siswa dialokasikan dengan benar'),
('Super Admin memeriksa transfer','Dana masuk terkonfirmasi','Persetujuan dengan referensi unik; pengembalian mempunyai alasan'),
('Admin membuka pesan tunggakan','Pesan sesuai kewajiban siswa','Nomor, periode, nominal, dan jatuh tempo benar; pengiriman manual'),
('Admin menyerahkan dan pusat menerima kas','Perpindahan dana dapat ditelusuri','Penerimaan pusat dibedakan dari penyetoran bank'),
('Pengguna menelusuri dasbor sesuai kewenangan','Ringkasan mempunyai transaksi sumber','Pengajuan tertunda terpisah dan cabang historis tidak berubah'),
('Super Admin mencocokkan penerimaan','Dana yang cocok dapat dikenali','Satu referensi bank tidak digunakan untuk dua sumber'),
('Super Admin mengelola data induk dan akun','Akses serta parameter dasar terkendali','Perubahan berwenang tercatat tanpa menghapus riwayat')]
us_table='\n'.join(f'| US-{i:02} | {a} | {b} | {c} |' for i,(a,b,c) in enumerate(us,1))
trace='\n'.join(f'| KF-{i:02} | {s} | US-{i:02} | UC-{uc} | I-{it:02} | PU-{i:02}; UAT-{i:02} |' for i,(_,_,uc,it,s) in enumerate(functions,1))
section('3.4.4', '''Cerita pengguna disusun dengan peran, tindakan, manfaat, serta kriteria penerimaan yang dapat diamati. Penyusunannya mempunyai pembanding pada Fikri dan Arthawan Sugih Prabowo (2021, hlm. 105), sedangkan isi Tabel 3.12 berasal dari kebutuhan ARTHA.

**Tabel 3.12 Cerita Pengguna dan Kriteria Penerimaan**

| Kode | Peran dan tindakan | Manfaat | Kriteria penerimaan |
| :--- | :--- | :--- | :--- |
'''+us_table+'''

Tabel 3.13 menghubungkan setiap kebutuhan dengan sumber, cerita pengguna, use case, iterasi, dan kelompok pemeriksaan. Prioritas seluruh kebutuhan adalah inti, sedangkan urutan pengerjaannya mengikuti ketergantungan pada Tabel 3.4.

**Tabel 3.13 Keterlacakan Kebutuhan sampai Evaluasi**

| Kebutuhan | Sumber | Cerita | Use case | Iterasi | Pemeriksaan |
| :--- | :--- | :--- | :--- | :--- | :--- |
'''+trace+'''

Kelompok PU mencakup kasus normal, pengecualian, dan batas yang relevan, bukan satu hasil uji tunggal. Matriks rinci menghubungkan kelompok tersebut dengan kasus BB, tabel sumber, bukti, dan status validasi pada lampiran keterlacakan.''')

section('3.4.5', '''Pemodelan kasus penggunaan atau *use case* menggambarkan tujuan pengguna di dalam batas sistem. Penggunaan model ini mempunyai pembanding pada Ahadi dkk. (2025, hlm. 765), sedangkan Gambar 3.2 memakai katalog yang telah diselaraskan dengan rancangan data ARTHA.

![Use case inti sistem ARTHA](<'''+(SUP/'gambar/Gambar_3_2_Use_Case_Inti.png').as_posix()+'''>)

**Gambar 3.2 Diagram Kasus Penggunaan Sistem Informasi ARTHA**

Sumber: rancangan penelitian berdasarkan kebutuhan ARTHA.

Katalog memuat empat belas tujuan UC-00 sampai UC-13 dengan dua aktor pengguna. Tabel 3.14 merangkum contoh proses lintas peran, sedangkan seluruh skenario dan peta perubahan kode lama disimpan pada dokumen use case pendamping.

**Tabel 3.14 Skenario Pengajuan dan Pemeriksaan Transfer**

| Unsur | Rancangan |
| :--- | :--- |
| Identitas | UC-07 pengajuan transfer dan UC-08 pemeriksaan transfer |
| Pelaksana | Admin Cabang sebagai pengaju; Super Admin sebagai pemeriksa berwenang |
| Prasyarat | Akun sah, tagihan tersedia, rekening resmi aktif, dan kewenangan pemeriksa telah ditetapkan |
| Pengajuan | Pilih tagihan satu siswa serta cabang, isi nominal, tanggal dan rekening, unggah bukti, lalu kirim |
| Keadaan antara | Status menunggu verifikasi; tagihan belum dilunasi dan antrean tampil pada dasbor |
| Pemeriksaan | Bandingkan identitas, nominal, rekening, dan tanggal dengan referensi dana masuk yang dicatat manual |
| Persetujuan | Kunci transaksi terkait, periksa ulang sisa tagihan serta referensi, lalu simpan keputusan dan pencocokan satu kali |
| Pengembalian | Simpan alasan; perbaikan menghasilkan pengajuan baru dengan tautan ke pengajuan lama |
| Pengecualian | Bukti tidak terbaca, nominal berbeda, referensi sudah digunakan, sisa tagihan berubah, atau akses tidak berwenang |
| Pascakondisi | Riwayat tersimpan; hanya pembayaran terkonfirmasi mengurangi sisa; kuitansi final terbit setelah persetujuan |

Pembatasan akses berlaku pada setiap tindakan dan objek yang diproses. Diagram tidak memisahkan setiap validasi formulir menjadi tujuan pengguna tersendiri, sedangkan skenario menjelaskan kondisi normal serta pengecualiannya.''')

section('3.4.6', '''Basis data terpusat dirancang menjadi dua puluh tiga tabel yang memisahkan identitas, keanggotaan, kewajiban, penerimaan, dan perpindahan dana. Gambar 3.3 menampilkan hubungan transaksi utama, sedangkan ERD lengkap serta kamus data tersedia pada dokumen basis data pendamping.

![Hubungan konseptual data ARTHA](<'''+(SUP/'gambar/Gambar_3_3_Model_Data_Konseptual.png').as_posix()+'''>)

**Gambar 3.3 Hubungan Data Utama Prototipe ARTHA**

Sumber: rancangan penelitian berdasarkan pemisahan proses operasional.

Tabel 3.15 merangkum pengelompokan tabel beserta fungsinya. Hubungan pembayaran dan tagihan memakai rincian alokasi agar satu penerimaan dapat digunakan untuk beberapa tagihan siswa yang sama.

**Tabel 3.15 Kelompok Tabel dan Hubungan Utama**

| Kelompok | Tabel | Hubungan utama |
| :--- | :--- | :--- |
| Periode dan kewenangan | `academic_years`, `branches`, `users` | Tahun ajaran, cabang penugasan, dan peran pengguna |
| Identitas dan kompetensi | `students`, `mentors`, `subjects`, `mentor_subjects` | Kontak wali serta satu identitas tentor untuk pemeriksaan lintas cabang |
| Kelas dan jadwal | `class_rooms`, `classes`, `class_schedules`, `class_enrollments` | Ruang fisik, kelompok, masa jadwal, serta riwayat keanggotaan |
| Kewajiban | `fee_tariffs`, `bills` | Tarif menurut cabang, sesi, dan siklus; tagihan menyimpan nilai aktual |
| Penerimaan | `payments`, `payment_allocations`, `payment_reviews` | Induk pembayaran, pembagian ke tagihan, dan keputusan pemeriksaan |
| Perpindahan kas | `cash_batches`, `cash_batch_items` | Satu kelompok penyerahan memuat pembayaran tunai sumber |
| Pencocokan bank | `bank_accounts`, `bank_entries`, `bank_matches` | Rekening resmi, dana masuk manual, dan satu sumber yang dicocokkan |
| Ketertelusuran | `reminder_actions`, `activity_logs` | Tindakan membuka WhatsApp serta perubahan penting oleh petugas |

Tabel 3.16 menjelaskan atribut dan kendala yang paling memengaruhi ketepatan prototipe. Penghitungan peserta aktif, sisa tagihan, kondisi terlambat, dan ringkasan penerimaan diturunkan dari data sumber, bukan angka yang dapat diubah secara terpisah.

**Tabel 3.16 Atribut dan Kendala Kritis Rancangan Data**

| Objek | Atribut atau hubungan penting | Kendala rancangan |
| :--- | :--- | :--- |
| Pengguna | Peran, cabang penugasan, status | Cabang kosong tidak memberikan hak Super Admin |
| Kelas | `max_students`, `near_full_remaining` | Peserta aktif tidak melebihi kapasitas; ambang belum diisi dengan angka kebijakan tanpa validasi |
| Keanggotaan | Siswa, kelas, waktu masuk, waktu keluar, alasan | Tidak ada dua keanggotaan aktif siswa pada kelas yang sama; masuk kembali membuat riwayat baru |
| Jadwal | Hari, jam, rentang tanggal, tentor, ruang, status | Periksa masa berlaku, cabang ruang, irisan, dan pengecualian jadwal yang disunting |
| Tagihan | Cabang historis, periode, tarif, nilai, potongan beralasan | Periode tidak ganda dan perubahan tarif tidak mengubah tagihan lama |
| Pembayaran | Siswa, cabang historis, kanal, status, pengajuan asal | Pengajuan ulang tertaut; pengajuan menunggu atau dikembalikan belum menjadi penerimaan |
| Alokasi | Pembayaran, tagihan, nominal | Siswa serta cabang sama; total sesuai pembayaran dan tidak melebihi sisa sah |
| Pemeriksaan | Pengajuan, petugas, keputusan, waktu, alasan | Riwayat tidak ditimpa dan keputusan final hanya berlaku sekali |
| Pencocokan | Dana masuk dan salah satu sumber | Sumber berupa transfer atau setoran; nominal penuh sama dan referensi tidak dipakai ganda |

Penempatan peserta memerlukan kelas aktif dengan jadwal dan ruang yang memenuhi kapasitas kelompok. Perubahan ruang atau batas kelas diperiksa kembali terhadap peserta aktif, sedangkan hitungan serta penyimpanannya dilindungi oleh transaksi yang sama.

Laporan menggunakan cabang yang tersimpan pada transaksi agar perpindahan siswa tidak memindahkan riwayat penerimaan. Sisa tagihan dihitung dari nilai kewajiban dikurangi alokasi pembayaran sah, sedangkan penanda lewat jatuh tempo dihitung terpisah dari tingkat pelunasannya.

Skema fisik ditargetkan pada MySQL dengan mesin transaksi InnoDB. Rancangan kunci, indeks, penguncian, dan aturan nilai akan diperiksa melalui migrasi serta pengujian implementasi sebelum dinyatakan berjalan.''')

ui_defs=[
(4,'Gambar_3_4_Dasbor_Cabang','Dasbor Admin Cabang','Dasbor cabang menampilkan tunggakan, pengajuan transfer menunggu pemeriksaan, dan keterisian kelas sesuai cabang pengguna. Daftar tindak lanjut menghubungkan ringkasan dengan transaksi sumber untuk mendukung US-08, US-10, dan US-12.'),
(5,'Gambar_3_5_Keanggotaan_Kelas','Penempatan dan Keanggotaan Kelas','Halaman keanggotaan menampilkan kapasitas, peserta aktif, sisa tempat, serta peringatan hampir penuh untuk US-03 dan US-04. Tombol penambahan dinonaktifkan ketika penuh, sedangkan tindakan mengakhiri keanggotaan menyimpan tanggal serta alasan tanpa menghapus siswa.'),
(6,'Gambar_3_6_Pengajuan_Transfer','Pengajuan Transfer oleh Admin Cabang','Formulir pengajuan menampilkan siswa, cabang, tagihan yang dipilih, jumlah alokasi, rekening tujuan, serta bukti transfer untuk US-08. Pengiriman menghasilkan status menunggu verifikasi, sedangkan perbaikan dari pengajuan yang dikembalikan tetap memperlihatkan hubungan dengan pengajuan sebelumnya.'),
(7,'Gambar_3_7_Pemeriksaan_Transfer','Pemeriksaan Transfer oleh Super Admin','Layar pemeriksaan menyandingkan pengajuan dengan rincian dana masuk yang dimasukkan petugas berwenang untuk US-09. Persetujuan memerlukan nominal dan referensi yang sesuai, sedangkan pengembalian mewajibkan alasan yang dapat ditindaklanjuti admin.'),
(8,'Gambar_3_8_Tunggakan_WhatsApp','Tunggakan dan Pratinjau Pesan WhatsApp','Halaman tunggakan menampilkan periode, sisa tagihan, jatuh tempo, nomor wali, dan pratinjau pesan untuk US-10. Tombol membuka WhatsApp dengan pesan terisi, sementara pengiriman tetap dilakukan admin dan catatan tindakan tidak menunjukkan status pesan terkirim.'),
(9,'Gambar_3_9_Dasbor_Pusat_Pencocokan','Dasbor Pusat dan Pencocokan Penerimaan','Dasbor pusat membedakan tunggakan, penerimaan sah, pengajuan tertunda, dan dana yang telah dicocokkan untuk US-12 serta US-13. Petugas dapat membuka sumber transfer atau setoran, memeriksa referensi bank, dan menelusuri nominal tanpa menghitung setoran sebagai pendapatan siswa yang baru.')]
ui_intro='''Antarmuka disusun menurut urutan kerja dan kewenangan pengguna. Gambar 3.4 sampai Gambar 3.9 memperlihatkan enam rancangan layar inti, sedangkan Tabel 3.17 menghubungkan layar dengan tugas pengguna.

**Tabel 3.17 Rancangan Antarmuka Inti**

| Layar | Cerita pengguna | Tindakan utama |
| :--- | :--- | :--- |
| Dasbor cabang | US-08, US-10, US-12 | Memilih tindak lanjut transaksi serta keterisian |
| Keanggotaan kelas | US-03, US-04 | Menambah peserta atau mengakhiri keanggotaan |
| Pengajuan transfer | US-08 | Memilih tagihan dan mengirim bukti |
| Pemeriksaan transfer | US-09 | Memeriksa dana masuk dan mengambil keputusan |
| Tunggakan WhatsApp | US-10 | Memeriksa pesan dan membuka WhatsApp |
| Dasbor pusat dan pencocokan | US-11, US-12, US-13 | Menelusuri setoran, penerimaan, dan referensi bank |

Angka, nama, serta transaksi pada rancangan layar merupakan data simulasi dan tidak menunjukkan kondisi keuangan mitra. Penanda warna disertai teks, sedangkan istilah status mengikuti skenario serta kamus data yang sama.'''
ui=ui_intro+'\n\n'+'\n\n'.join(fig(n,name,caption,caption,desc) for n,name,caption,desc in ui_defs)
section('3.4.7',ui)

t=t.replace('Pengajuan pembayaran menghasilkan notifikasi dalam dasbor Super Admin melalui penyimpanan notifikasi aplikasi. Mekanisme penyimpanan dan penyajiannya mengikuti dokumentasi notifikasi Laravel, sedangkan notifikasi WhatsApp atau surel otomatis tidak menjadi kebutuhan inti (Laravel, t.t.-b).',
'''Antrean pengajuan menunggu pemeriksaan ditampilkan dari status transaksi pada dasbor Super Admin. Apabila mitra memerlukan status notifikasi dibaca, fasilitas notifikasi tersimpan Laravel dapat ditambahkan sebagai perluasan setelah kebutuhannya disepakati (Laravel, t.t.-b).''')

section('3.5.2', '''Perangkat pengembangan perlu menjalankan penyunting kode, antarmuka web, layanan aplikasi, dan basis data lokal. Tabel 3.18 membedakan informasi yang telah diketahui dari rincian perangkat yang masih perlu dicatat sebelum pengujian.

**Tabel 3.18 Ketersediaan dan Rencana Perangkat Keras**

| Perangkat | Informasi tersedia | Pelengkapan sebelum pengujian |
| :--- | :--- | :--- |
| Komputer penyusunan | Ruang kerja lokal menggunakan Windows | Prosesor, RAM, penyimpanan, dan versi sistem operasi perangkat pengembangan belum terverifikasi |
| Komputer pengguna | Direncanakan untuk tugas administrasi cabang dan pusat | Perangkat, resolusi, peramban, dan jaringan ditetapkan bersama mitra |
| Telepon uji | Direncanakan untuk tampilan sempit dan tautan WhatsApp | Sistem operasi, ukuran layar, peramban, serta aplikasi WhatsApp dicatat |
| Peladen uji | Diperlukan untuk akses evaluasi mitra | Kapasitas, penyimpanan privat, domain, serta konfigurasi jaringan belum ditetapkan |
| Perangkat cetak | Digunakan jika pencetakan kuitansi masuk tugas evaluasi | Kertas dan pengaturan cetak dikonfirmasi |

Kapasitas perangkat tidak ditetapkan dari spesifikasi artikel terdahulu. Inventaris aktual dan kondisi jaringan dicatat bersama hasil agar konteks pelaksanaan dapat diperiksa.''')

# Read lockfile versions without running or modifying the website project.
pkg=json.loads((ROOT/'website-artha/package-lock.json').read_text(encoding='utf-8'))
versions={k:pkg.get('packages',{}).get('node_modules/'+k,{}).get('version','belum diperiksa') for k in ['next','react','tailwindcss']}
section('3.5.3', f'''Ruang kerja telah mempunyai proyek antarmuka `website-artha` dengan berkas penguncian dependensi. Versi pada Tabel 3.19 diperiksa dari berkas tersebut pada 25 Oktober 2026 dan belum menunjukkan bahwa layanan administrasi serta basis data telah selesai diimplementasikan.

**Tabel 3.19 Pilihan Teknologi dan Status Versi**

| Komponen | Pilihan dan bukti tersedia | Status penggunaan |
| :--- | :--- | :--- |
| Antarmuka | Next.js {versions['next']} dan React {versions['react']} pada `package-lock.json` | Tersedia pada proyek lokal; versi evaluasi dibekukan sebelum UAT |
| Tata tampilan | Tailwind CSS {versions['tailwindcss']} pada `package-lock.json` | Tersedia pada proyek antarmuka |
| Layanan aplikasi | Laravel dan PHP | Pilihan rancangan; versi serta berkas penguncian layanan belum tersedia untuk pemeriksaan |
| Autentikasi | Laravel Sanctum berbasis sesi untuk antarmuka milik aplikasi | Direncanakan; konfigurasi domain dan sesi diperiksa pada implementasi |
| Basis data | MySQL dengan InnoDB | DBMS rancangan tunggal; versi dan migrasi belum dibekukan |
| Dependensi | Pengelola paket JavaScript dan Composer | Berkas penguncian disimpan bersama versi kode |
| Pengujian | Pengujian unit aturan bisnis serta pengujian layanan dan antarmuka | Perangkat, versi, dan perintah ditetapkan setelah lingkungan layanan tersedia |
| Dokumentasi | Markdown, diagram PNG/SVG, dan pengelola referensi | Sumber diagram serta matriks rancangan disimpan untuk penelusuran |

Kebutuhan lingkungan antarmuka diperiksa terhadap dokumentasi resmi Next.js sesuai versi yang akhirnya digunakan (Vercel, t.t.). Pasangan PHP dan Laravel dipilih menurut kompatibilitas serta kebijakan dukungan yang berlaku, kemudian dicatat bersama lingkungan evaluasi (Laravel, t.t.-c).

Keberadaan dependensi lokal digunakan sebagai bukti pilihan teknologi yang tersedia, bukan hasil pengujian prototipe. Versi layanan, konfigurasi koneksi, dan hasil migrasi akan dilengkapi sebelum pengujian terintegrasi.''')

t=t.replace('Pengujian bersama mitra direncanakan pada lingkungan yang mewakili alur administrasi cabang dan pemantauan pusat. Jumlah akun, jumlah data, kondisi jaringan, versi aplikasi, serta perangkat yang digunakan dicatat agar konteks hasil evaluasi dapat diketahui.',
'''Pengujian bersama mitra menggunakan akun simulasi minimal dua cabang dan satu akun pusat agar pembatasan data dapat diperiksa. Jumlah data uji, kondisi jaringan, versi, dan perangkat dicatat; cakupan tersebut merupakan rencana pengujian, bukan jumlah peserta yang sudah hadir.

Data awal memuat kelas tersedia, hampir penuh, penuh, jadwal beririsan, beberapa siklus tagihan, transfer dikembalikan, serta setoran tunai. Pemeriksaan awal dilakukan setelah pemuatan data dan pencadangan, kemudian keadaan awal dipulihkan bila diperlukan untuk mengulang kasus.''')

section('3.6', '''Rencana pengembangan disusun selama dua belas minggu relatif dengan empat iterasi dua mingguan. Penelaahan wawancara dan penyusunan rancangan telah memiliki artefak per 25 Oktober 2026, sedangkan tanggal mulai implementasi serta evaluasi belum disepakati.

Tabel 3.20 menunjukkan alokasi pelaksanaan berikutnya dan tidak digunakan untuk mengklaim bahwa kegiatan yang telah terdokumentasi harus diulang seluruhnya. Minggu pertama dimulai pada tanggal yang akan ditetapkan bersama pembimbing dan mitra.

**Tabel 3.20 Rencana Jadwal Pelaksanaan Prototipe**

| Kegiatan | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Klarifikasi bukti dan aturan mitra | X | X | | | | | | | | | | |
| Estimasi tugas, instrumen, dan lingkungan | | X | | | | | | | | | | |
| I-01: data dasar dan akses | | | X | X | | | | | | | | |
| I-02: keanggotaan dan jadwal | | | | | X | X | | | | | | |
| I-03: pembayaran dan WhatsApp | | | | | | | X | X | | | | |
| I-04: setoran, laporan, pencocokan | | | | | | | | | X | X | | |
| UAT, perbaikan, dan uji ulang | | | | | | | | | | | X | X |
| Dokumentasi waktu, galat, dan rancangan | | X | X | X | X | X | X | X | X | X | X | X |
| Penyiapan serah uji, laporan, artikel, HKI | | | | | | | | | | | X | X |

Pengujian unit, pengujian sistem, dan evaluasi iterasi berlangsung di dalam setiap alokasi iterasi. Rincian jam tugas dan tanggal kalender dilengkapi sebelum pelaksanaan, kemudian disesuaikan apabila terdapat perubahan kebutuhan atau ketersediaan mitra.

Penyusunan laporan mengikuti panduan kepenulisan ITK, sedangkan luaran prototipe dilaporkan sesuai ketentuan program studi (Institut Teknologi Kalimantan, 2025a; Institut Teknologi Kalimantan, 2026). Jadwal akhir dicatat bersama versi rencana agar perubahan dari usulan awal dapat diperiksa.''')

t=t.replace('Riwayat pembukaan tautan dapat dicatat sebagai tindakan admin.', 'Permintaan pembukaan tautan dicatat sebagai tindakan admin.')
t=t.replace('Periode tagihan, waktu pengajuan, dan waktu pemeriksaan menggunakan zona waktu operasional Balikpapan. Penghitungan jatuh tempo didasarkan pada tanggal yang ditetapkan untuk tagihan, sehingga tidak diasumsikan seluruh siswa mempunyai tanggal jatuh tempo yang sama.',
'''Waktu kejadian disimpan dalam UTC dan ditampilkan dalam zona waktu Asia/Makassar untuk operasional Balikpapan. Tanggal kewajiban dan jatuh tempo menggunakan kalender operasional tersebut, dengan tanggal yang ditetapkan pada setiap tagihan.''')
t=t.replace('Penjadwalan pada ARTHA diarahkan untuk membantu pemeriksaan konflik pada jadwal yang disusun pengelola.',
'''Penjadwalan pada ARTHA membantu pemeriksaan konflik pada jadwal yang disusun pengelola. Calon jadwal berkonflik dapat disimpan nonaktif untuk ditinjau, sedangkan pengaktifan pengecualian belum diberlakukan sebelum kebijakannya ditetapkan bersama mitra.''')
t=t.replace('Gambar 3.4 menyajikan hubungan pengguna', 'Gambar 3.10 menyajikan hubungan pengguna').replace('**Gambar 3.4 Arsitektur', '**Gambar 3.10 Arsitektur').replace('Gambar_3_4_Arsitektur_Prototipe.png','Gambar_3_10_Arsitektur_Prototipe.png')
CH.write_text(t.rstrip()+'\n',encoding='utf-8')
OUT.mkdir(parents=True, exist_ok=True)
(OUT/'KONTRAK KEBUTUHAN.json').write_text(json.dumps({'date':'2026-10-25','functions':[{'kf':f'KF-{i:02}','us':f'US-{i:02}','uc':f'UC-{uc}','test_group':f'PU-{i:02}','uat':f'UAT-{i:02}','iteration':f'I-{it:02}','name':name,'acceptance':acc,'sources':src.split('/')} for i,(name,acc,uc,it,src) in enumerate(functions,1)],'versions_read_from_local_lockfile':versions,'pending':['Kewenangan rekening dan pemeriksa','Tarif, potongan, siklus, serta kapasitas aktual','Peserta dan tanggal UAT','Versi layanan dan perangkat keras','Jadwal kalender','Kesesuaian Bab1/Bab2 setelah keputusan mitra']},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'chapter_words':len(t.split()),'tables':len(re.findall(r'^\*\*Tabel ',t,re.M)),'figures':len(re.findall(r'^\*\*Gambar ',t,re.M)),'versions':versions},ensure_ascii=False))
