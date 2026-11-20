from pathlib import Path
import json, re, hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'DOKUMEN MD/REVISI_TERPADU_2026-10-25'
TARGET = ROOT / 'DOKUMEN MD/PERANCANGAN BASIS DATA (SKEMA & ERD).md'
OUT.mkdir(parents=True, exist_ok=True)
schema = []

def field(name, typ, nullable, description, ref=None, unique=False):
    return dict(name=name, type=typ, nullable=nullable, description=description, ref=ref, unique=unique)

def fk(name, ref, description, nullable=False, unique=False):
    return field(name, 'BIGINT UNSIGNED', nullable, description, ref, unique)

def c(name, typ, description, nullable=False, unique=False):
    return field(name, typ, nullable, description, None, unique)

def table(name, label, purpose, fields, rules, mutable=True):
    common = [c('id', 'BIGINT UNSIGNED', 'Kunci utama, AUTO_INCREMENT', unique=True)]
    common += fields + [c('created_at', 'DATETIME(6)', 'Waktu pencatatan, disimpan dalam UTC')]
    if mutable:
        common += [c('updated_at', 'DATETIME(6)', 'Waktu perubahan terakhir, disimpan dalam UTC')]
    schema.append(dict(name=name, label=label, purpose=purpose, fields=common, rules=rules))

table('academic_years', 'Tahun ajaran',
      'Menyimpan rentang tahun ajaran yang dipakai kelas, tarif, dan tagihan. Arsip tahun sebelumnya tetap tersedia ketika tahun operasional berubah.', [
    c('name', 'VARCHAR(30)', 'Nama tahun ajaran', unique=True),
    c('start_date', 'DATE', 'Tanggal mulai tahun ajaran'),
    c('end_date', 'DATE', 'Tanggal akhir tahun ajaran'),
    c('is_active', 'BOOLEAN', 'Penanda tahun operasional aktif, awal FALSE'),
], ['Tanggal akhir tidak mendahului tanggal mulai. Pergantian tahun aktif dilakukan dalam transaksi yang mencegah lebih dari satu tahun aktif.',
    'Tanggal kalender tahun ajaran berasal dari ketentuan mitra. Aktivasi tahun baru tidak mengubah tingkat kelas pada tagihan historis.'])

table('branches', 'Cabang',
      'Menyimpan identitas cabang untuk pemisahan data operasional. Jumlah ruang diperoleh dari data ruang aktif, sehingga tidak ditulis ulang sebagai penghitung bebas.', [
    c('code', 'VARCHAR(20)', 'Kode cabang', unique=True),
    c('name', 'VARCHAR(100)', 'Nama cabang'),
    c('address', 'TEXT', 'Alamat cabang', nullable=True),
    c('phone_wa', 'VARCHAR(20)', 'Kontak cabang dengan format internasional', nullable=True),
    c('is_active', 'BOOLEAN', 'Status operasional cabang'),
], ['Cabang yang mempunyai transaksi dinonaktifkan, bukan dihapus. Lokasi pada peta publik tidak menjadi kebutuhan inti prototipe.'])

table('users', 'Akun pengguna',
      'Menyimpan akun Admin Cabang dan Super Admin. Peran menentukan izin fungsi, sedangkan penugasan cabang membatasi objek yang dapat diakses.', [
    fk('branch_id', 'branches.id', 'Cabang penugasan Admin Cabang; kosong untuk Super Admin', nullable=True),
    c('name', 'VARCHAR(100)', 'Nama pengguna'),
    c('email', 'VARCHAR(190)', 'Identitas masuk yang unik', unique=True),
    c('password_hash', 'VARCHAR(255)', 'Hasil hash kata sandi, bukan kata sandi terbuka'),
    c('role', "ENUM('branch_admin','super_admin')", 'Peran yang diberikan melalui proses berwenang'),
    c('is_active', 'BOOLEAN', 'Status akun aktif'),
    c('last_login_at', 'DATETIME(6)', 'Waktu masuk terakhir', nullable=True),
], ['Admin Cabang wajib mempunyai branch_id yang sah; Super Admin menggunakan branch_id kosong. Nilai cabang kosong pada akun tidak sah tidak memberikan hak Super Admin.',
    'Pemeriksaan izin dijalankan pada peladen untuk setiap objek. Mutasi akun tidak mengubah cabang pemilik transaksi lama atau menghapus jejak pelakunya.'])

table('subjects', 'Mata pelajaran',
      'Menyediakan nama mata pelajaran yang dipakai pada jadwal. Mata pelajaran dilekatkan pada sesi jadwal agar satu kelompok belajar dapat mengikuti beberapa mata pelajaran.', [
    c('code', 'VARCHAR(20)', 'Kode mata pelajaran', unique=True),
    c('name', 'VARCHAR(100)', 'Nama mata pelajaran'),
    c('is_active', 'BOOLEAN', 'Status penggunaan mata pelajaran'),
], ['Mata pelajaran yang sudah dipakai dinonaktifkan tanpa menghapus riwayat. Daftar mata pelajaran ditetapkan dari layanan yang benar-benar tersedia.'])

table('fee_tariffs', 'Tarif berdasarkan cabang dan sesi',
      'Menyimpan tarif yang dapat dikelola Super Admin melalui aplikasi. Pemilihan tarif memperhitungkan cabang, sesi, jenjang, program, jenis biaya, dan periode pembayaran.', [
    fk('branch_id', 'branches.id', 'Cabang tempat tarif berlaku, tanpa tarif global implisit'),
    fk('academic_year_id', 'academic_years.id', 'Tahun ajaran tarif'),
    c('session_code', 'VARCHAR(30)', 'Kode sesi belajar atau kode all yang dipilih secara eksplisit'),
    c('learning_program', "ENUM('reguler','intensif','paket')", 'Kategori program, bukan penentu otomatis siklus pembayaran'),
    c('grade_level', "ENUM('TK','SD','SMP','SMA')", 'Jenjang sasaran'),
    c('class_grade_start', 'TINYINT UNSIGNED', 'Tingkat awal; kosong untuk TK', nullable=True),
    c('class_grade_end', 'TINYINT UNSIGNED', 'Tingkat akhir; kosong untuk TK', nullable=True),
    c('fee_type', "ENUM('tuition','module','registration')", 'Komponen biaya'),
    c('billing_cycle', "ENUM('monthly','semester','annual','once')", 'Siklus kewajiban yang ditetapkan mitra'),
    c('amount', 'DECIMAL(14,2)', 'Nominal tarif dasar yang positif'),
    c('valid_from', 'DATE', 'Tanggal mulai berlaku'),
    c('valid_until', 'DATE', 'Tanggal akhir berlaku'),
    c('description', 'VARCHAR(255)', 'Dasar atau nama paket', nullable=True),
    c('is_active', 'BOOLEAN', 'Status ketersediaan untuk tagihan baru'),
], ['Tidak boleh ada dua tarif aktif dengan cakupan cabang, sesi, program, jenjang, komponen, siklus, tingkat, dan tanggal yang bertumpang tindih. Pemeriksaan rentang dilakukan pada aplikasi dalam transaksi.',
    'Tarif tidak dipilih melalui prioritas tersembunyi antara sesi tertentu dan all. Pengguna memilih cakupan yang sah dan sistem menolak kandidat ambigu.',
    'Perubahan tarif hanya memengaruhi tagihan baru. Tarif yang sudah dirujuk tidak diubah nominal atau cakupannya, melainkan diganti versi baris baru dengan masa berlaku yang tidak bertumpang tindih.',
    'Nilai yang sudah dikenakan disimpan pada bills bersama periode dan dasar penyesuaiannya. Identitas tarif sumber tetap dapat ditelusuri pada baris terdahulu.'])

table('students', 'Siswa dan kontak wali',
      'Menyimpan identitas siswa yang dibutuhkan administrasi. Kontak wali menjadi tujuan pesan, sedangkan potongan biaya tidak dipatok sebagai nilai global pada profil siswa.', [
    fk('branch_id', 'branches.id', 'Cabang administratif siswa saat ini'),
    fk('academic_year_id', 'academic_years.id', 'Tahun ajaran pendaftaran pertama'),
    c('registration_no', 'VARCHAR(30)', 'Nomor pendaftaran unik', unique=True),
    c('full_name', 'VARCHAR(100)', 'Nama lengkap siswa'),
    c('birth_date', 'DATE', 'Tanggal lahir jika dibutuhkan formulir', nullable=True),
    c('parent_name', 'VARCHAR(100)', 'Nama wali yang dihubungi'),
    c('parent_phone_wa', 'VARCHAR(20)', 'Nomor WhatsApp wali tervalidasi formatnya'),
    c('school_origin', 'VARCHAR(150)', 'Sekolah asal', nullable=True),
    c('grade_level', "ENUM('TK','SD','SMP','SMA')", 'Jenjang pendidikan'),
    c('class_grade', 'TINYINT UNSIGNED', 'Tingkat kelas; kosong untuk TK', nullable=True),
    c('home_address', 'TEXT', 'Alamat atau kelurahan sesuai kebutuhan data', nullable=True),
    c('learning_program', "ENUM('reguler','intensif','paket')", 'Program administratif saat ini'),
    c('session_code', 'VARCHAR(30)', 'Sesi administratif untuk pemilihan tarif'),
    c('family_reference', 'VARCHAR(50)', 'Kode kelompok saudara setelah diperiksa admin', nullable=True),
    c('status', "ENUM('active','alumni','inactive')", 'Status administratif siswa'),
    c('registered_at', 'DATETIME(6)', 'Waktu pendaftaran'),
], ['Tingkat TK kosong, SD satu sampai enam, SMP tujuh sampai sembilan, dan SMA sepuluh sampai dua belas. Kelengkapan akhir formulir dikonfirmasi kepada mitra.',
    'Kode keluarga mendukung lebih dari dua saudara tanpa menentukan diskon otomatis. Nominal, alasan, dan pemberi persetujuan potongan disimpan pada tagihan.',
    'Perpindahan cabang merupakan tindakan berwenang yang tercatat pada activity_logs dan mengakhiri keanggotaan lama bila diperlukan. Cabang tagihan dan penerimaan yang telah tercatat tidak ikut berubah.'])

table('mentors', 'Tentor',
      'Menyimpan satu identitas tentor yang digunakan lintas cabang. Identitas ini memungkinkan pemeriksaan benturan tanpa menggandakan tentor pada setiap cabang.', [
    fk('branch_id', 'branches.id', 'Cabang pangkalan, boleh kosong bagi tentor lintas cabang', nullable=True),
    c('full_name', 'VARCHAR(100)', 'Nama tentor'),
    c('phone_wa', 'VARCHAR(20)', 'Kontak tentor bila diperlukan', nullable=True),
    c('is_active', 'BOOLEAN', 'Status aktif tentor'),
], ['Tentor tidak memperoleh akun dasbor dalam lingkup inti. Jumlah tentor tidak dipatok sebelum daftar mitra diperiksa.'])

table('mentor_subjects', 'Kompetensi mata pelajaran tentor',
      'Menghubungkan tentor dengan mata pelajaran yang dapat diampunya. Hubungan ini dipakai saat penugasan jadwal dan tidak membentuk akun pengguna baru.', [
    fk('mentor_id', 'mentors.id', 'Tentor'),
    fk('subject_id', 'subjects.id', 'Mata pelajaran'),
], ['Pasangan mentor_id dan subject_id unik. Penghapusan penugasan kompetensi tidak menghapus jadwal historis.'], mutable=False)

table('class_rooms', 'Ruang fisik',
      'Menyimpan ruang dan daya tampung fisik pada suatu cabang. Data ini dibedakan dari kelompok belajar agar pemakaian ruang pada setiap jadwal dapat diperiksa.', [
    fk('branch_id', 'branches.id', 'Cabang pemilik ruang'),
    c('room_name', 'VARCHAR(60)', 'Nama ruang yang unik dalam cabang'),
    c('physical_capacity', 'SMALLINT UNSIGNED', 'Daya tampung fisik yang positif'),
    c('is_active', 'BOOLEAN', 'Status ruang tersedia untuk penjadwalan'),
], ['Pasangan branch_id dan room_name unik. Penurunan kapasitas ruang diperiksa terhadap seluruh kelas dan jadwal aktif yang masih berlaku sebelum disimpan.'])

table('classes', 'Kelompok belajar',
      'Menyimpan identitas dan batas peserta kelompok belajar. Kondisi penuh dihitung dari keanggotaan aktif, sehingga tidak dicampur dengan status kelas ditutup.', [
    fk('branch_id', 'branches.id', 'Cabang penyelenggara kelas'),
    fk('academic_year_id', 'academic_years.id', 'Tahun ajaran kelas'),
    c('class_name', 'VARCHAR(100)', 'Nama kelompok belajar'),
    c('learning_program', "ENUM('reguler','intensif','paket')", 'Kategori program kelas'),
    c('session_code', 'VARCHAR(30)', 'Sesi kelompok belajar'),
    c('grade_level', "ENUM('TK','SD','SMP','SMA')", 'Jenjang kelompok belajar'),
    c('class_grade', 'TINYINT UNSIGNED', 'Tingkat kelas; kosong untuk TK', nullable=True),
    c('max_students', 'SMALLINT UNSIGNED', 'Batas peserta aktif yang positif'),
    c('near_full_remaining', 'SMALLINT UNSIGNED', 'Ambang sisa tempat untuk peringatan, ditetapkan sebelum UAT'),
    c('status', "ENUM('active','closed')", 'Status operasional kelompok belajar'),
], ['Nama kelas unik dalam cabang dan tahun ajaran. near_full_remaining bernilai paling sedikit satu dan tidak melebihi max_students; nilai aktual ditetapkan bersama mitra.',
    'current_students dan indikator almost_full atau full merupakan nilai turunan dari keanggotaan aktif, bukan kolom penghitung tersimpan. Kelas penuh tetap dapat berstatus active.',
    'Penerimaan anggota baru mensyaratkan sedikitnya satu jadwal aktif yang masih berlaku dengan ruang aktif. max_students tidak melebihi kapasitas setiap ruang pada jadwal aktif yang relevan.'])

table('class_schedules', 'Jadwal kelas',
      'Menghubungkan kelas, mata pelajaran, tentor, dan ruang pada suatu rentang tanggal. Rentang tersebut mencegah jadwal lama atau nonaktif dianggap benturan yang masih berlaku.', [
    fk('class_id', 'classes.id', 'Kelompok belajar'),
    fk('subject_id', 'subjects.id', 'Mata pelajaran sesi'),
    fk('mentor_id', 'mentors.id', 'Tentor dengan kompetensi yang sesuai'),
    fk('room_id', 'class_rooms.id', 'Ruang yang berada pada cabang kelas'),
    c('day_of_week', 'TINYINT UNSIGNED', 'Hari satu sampai tujuh, Senin sampai Minggu'),
    c('start_time', 'TIME', 'Jam mulai pada zona waktu operasional'),
    c('end_time', 'TIME', 'Jam selesai pada hari yang sama'),
    c('valid_from', 'DATE', 'Tanggal awal jadwal berlaku'),
    c('valid_until', 'DATE', 'Tanggal akhir jadwal berlaku'),
    c('is_active', 'BOOLEAN', 'Status jadwal aktif'),
], ['Jam selesai sesudah jam mulai dan tanggal akhir tidak mendahului tanggal awal. Jadwal wajib berada dalam rentang tahun ajaran kelas.',
    'Benturan diperiksa jika ada kejadian hari yang sama dalam irisan rentang tanggal dan jamnya beririsan. Pengubahan jadwal mengecualikan id jadwal yang sedang disunting.',
    'Benturan ditampilkan sebagai peringatan untuk ditinjau, bukan diklaim sebagai larangan mutlak yang telah disepakati mitra. Calon jadwal dapat disimpan nonaktif sampai penetapan ditinjau; aktivasi dengan konflik belum diaktifkan sebelum kebijakan mitra ditetapkan.',
    'Tentor diperiksa lintas cabang; ruang dan kelompok belajar diperiksa pada identitasnya. Admin Cabang hanya menerima informasi konflik yang diperlukan, tanpa memperoleh daftar lengkap data cabang lain.',
    'Perubahan ruang, jadwal, kapasitas kelas, dan kapasitas ruang menggunakan pemeriksaan yang saling konsisten. Penugasan tentor harus sesuai pasangan kompetensi mentor_subjects.'])

table('class_enrollments', 'Riwayat keanggotaan kelas',
      'Mencatat setiap interval masuk dan keluar siswa pada kelompok belajar. Siswa yang kembali setelah keluar memperoleh baris interval baru agar sejarah sebelumnya tidak ditimpa.', [
    fk('class_id', 'classes.id', 'Kelompok belajar'),
    fk('student_id', 'students.id', 'Siswa yang menjadi anggota'),
    fk('created_by_user_id', 'users.id', 'Pengguna yang menempatkan siswa'),
    c('joined_at', 'DATETIME(6)', 'Waktu mulai keanggotaan'),
    c('ended_at', 'DATETIME(6)', 'Waktu akhir keanggotaan; kosong ketika aktif', nullable=True),
    c('end_reason', 'VARCHAR(255)', 'Alasan keluar atau selesai; wajib jika ended_at terisi', nullable=True),
], ['Satu siswa tidak boleh mempunyai dua interval aktif pada kelas yang sama. Baris lama boleh tetap ada untuk keanggotaan yang sudah berakhir.',
    'Jumlah peserta aktif diperoleh dari ended_at kosong; pengaktifan baru dimulai segera dan tidak dijadwalkan ke masa depan pada lingkup inti. Penempatan siswa pada cabang berbeda tidak diaktifkan sebelum kebijakannya ditetapkan.',
    'Semua jalur tambah dan keluar anggota mengunci baris kelas dalam transaksi. Indeks unik bersyarat melalui kolom generated yang bernilai NULL untuk interval berakhir dapat digunakan pada MySQL dan harus diuji saat migrasi fisik.'])

table('bills', 'Tagihan dan nilai historis',
      'Menyimpan kewajiban yang diterbitkan untuk siswa pada cabang tertentu. Nilai dasar, potongan, periode, dan cabang pemilik merupakan rekaman historis saat penerbitan.', [
    fk('student_id', 'students.id', 'Siswa yang ditagih'),
    fk('branch_id', 'branches.id', 'Cabang pemilik tagihan yang tidak mengikuti mutasi siswa'),
    fk('academic_year_id', 'academic_years.id', 'Tahun ajaran tagihan'),
    fk('fee_tariff_id', 'fee_tariffs.id', 'Tarif sumber penerbitan'),
    fk('created_by_user_id', 'users.id', 'Penerbit tagihan'),
    c('fee_type', "ENUM('tuition','module','registration')", 'Salinan jenis kewajiban'),
    c('billing_cycle', "ENUM('monthly','semester','annual','once')", 'Salinan siklus kewajiban'),
    c('period_key', 'VARCHAR(30)', 'Kode periode yang baku menurut siklus'),
    c('period_start', 'DATE', 'Tanggal awal cakupan biaya'),
    c('period_end', 'DATE', 'Tanggal akhir cakupan biaya'),
    c('base_amount', 'DECIMAL(14,2)', 'Nilai dasar saat diterbitkan'),
    c('discount_amount', 'DECIMAL(14,2)', 'Potongan aktual, awal nol'),
    c('discount_reason', 'VARCHAR(255)', 'Dasar potongan; wajib jika ada potongan', nullable=True),
    fk('discount_approved_by_user_id', 'users.id', 'Pemberi persetujuan potongan berwenang', nullable=True),
    c('total_amount', 'DECIMAL(14,2)', 'Nilai dasar dikurangi potongan'),
    c('due_date', 'DATE', 'Jatuh tempo spesifik tagihan'),
    c('status', "ENUM('issued','cancelled')", 'Status penerbitan, berbeda dari pelunasan'),
], ['Kunci bisnis unik adalah student_id, branch_id, academic_year_id, fee_type, billing_cycle, dan period_key. Satu komponen tidak ditagih dua kali untuk periode sama.',
    'Nilai dasar positif, potongan antara nol dan nilai dasar, serta total_amount sama dengan base_amount dikurangi discount_amount. Potongan positif memerlukan alasan serta pemberi persetujuan.',
    'Tarif sumber harus berasal dari cabang, tahun ajaran, jenjang, program, dan sesi yang sesuai pada saat penerbitan. Penugasan serta identitas historis tagihan tidak boleh mengikuti perubahan profil siswa secara otomatis.',
    'Kode bulanan menggunakan YYYY-MM; semester menggunakan kode tahun ajaran dan S1 atau S2; tahunan menggunakan tahun ajaran; sekali menggunakan kode kewajiban yang disepakati. Paket semester tidak diterbitkan setiap bulan.',
    'Status unpaid, partial, paid, dan penanda lewat jatuh tempo dihitung terpisah dari alokasi pembayaran sah. Pembatalan hanya boleh sebelum terdapat pembayaran sah atau pengajuan aktif yang terkait.'])

table('payments', 'Penerimaan atau pengajuan pembayaran',
      'Menyimpan satu pembayaran untuk satu siswa, cabang historis, dan kanal. Satu bukti dapat dialokasikan ke beberapa tagihan melalui payment_allocations tanpa menggandakan penerimaan.', [
    fk('student_id', 'students.id', 'Siswa pemilik seluruh tagihan alokasi'),
    fk('branch_id', 'branches.id', 'Cabang pemilik seluruh tagihan alokasi'),
    fk('submitted_by_user_id', 'users.id', 'Admin yang mencatat atau mengajukan'),
    fk('bank_account_id', 'bank_accounts.id', 'Rekening tujuan; wajib untuk transfer, kosong untuk tunai', nullable=True),
    fk('resubmission_of_id', 'payments.id', 'Pengajuan returned yang diperbaiki; kosong untuk pengajuan awal', nullable=True, unique=True),
    c('submission_no', 'VARCHAR(40)', 'Nomor pencatatan atau pengajuan yang unik', unique=True),
    c('idempotency_key', 'VARCHAR(80)', 'Kunci permintaan agar kiriman ulang tidak membuat transaksi ganda', unique=True),
    c('payment_method', "ENUM('cash','bank_transfer')", 'Kanal inti prototipe'),
    c('status', "ENUM('recorded','submitted','verified','returned')", 'recorded hanya tunai; status lain mengikuti pemeriksaan transfer'),
    c('amount_paid', 'DECIMAL(14,2)', 'Nominal penerimaan atau pengajuan positif'),
    c('payment_date', 'DATETIME(6)', 'Waktu penerimaan tunai atau transfer menurut bukti'),
    c('submitted_at', 'DATETIME(6)', 'Waktu pencatatan atau pengajuan disimpan'),
    c('proof_storage_key', 'VARCHAR(255)', 'Kunci berkas privat, wajib untuk transfer', nullable=True),
    c('proof_sha256', 'CHAR(64)', 'Digest berkas untuk penelusuran, bukan bukti keaslian', nullable=True),
    c('receipt_no', 'VARCHAR(40)', 'Kuitansi resmi setelah recorded atau verified', nullable=True, unique=True),
    c('confirmed_at', 'DATETIME(6)', 'Waktu penerimaan sah; kosong sebelum konfirmasi', nullable=True),
    c('notes', 'TEXT', 'Catatan transaksi', nullable=True),
], ['Seluruh rincian alokasi harus memiliki student_id dan branch_id yang sama dengan induk. Jumlah alokasi sama persis dengan amount_paid.',
    'Tunai recorded dan transfer verified dihitung sebagai penerimaan sah. Transfer submitted atau returned tidak mengurangi sisa tagihan dan tidak memperoleh kuitansi resmi.',
    'Bukti serta rincian pengajuan transfer tidak disunting setelah submitted. Perbaikan membuat baris baru yang merujuk pengajuan returned, sedangkan baris lama dan keputusan lamanya dipertahankan.',
    'Satu pengajuan returned mempunyai paling banyak satu pengajuan lanjutan langsung. Gunakan UNIQUE(resubmission_of_id), cegah siklus rujukan, dan izinkan rantai perbaikan melalui pengajuan berikutnya.',
    'Perubahan status dilakukan hanya melalui transaksi prosedur yang sah. Koreksi pembayaran yang sudah terkonfirmasi memerlukan prosedur koreksi berwenang tersendiri dan bukan penghapusan transaksi lama.'])

table('payment_allocations', 'Alokasi pembayaran ke tagihan',
      'Mencatat pembagian satu pembayaran ke satu atau beberapa tagihan. Rincian ini membuat jumlah kuitansi dan jumlah penerimaan tetap satu meskipun mencakup beberapa periode.', [
    fk('payment_id', 'payments.id', 'Induk penerimaan atau pengajuan'),
    fk('bill_id', 'bills.id', 'Tagihan tujuan alokasi'),
    c('amount', 'DECIMAL(14,2)', 'Nominal alokasi yang positif'),
], ['Pasangan payment_id dan bill_id unik. Tagihan berbeda siswa atau cabang ditolak, serta total alokasi wajib sama dengan nominal induk.',
    'Alokasi hanya menuju tagihan issued dan tidak boleh melampaui sisa tagihan saat konfirmasi. Pembayaran sebagian secara bawaan tidak diaktifkan sebelum validasi mitra, sehingga setiap alokasi harus melunasi sisa tagihan yang dipilih.',
    'Pengajuan menunggu pemeriksaan tidak dianggap pelunasan dan tidak menjamin saldo masih tersedia. Saat disetujui, seluruh tagihan dikunci berurutan dan sisa dihitung ulang.'], mutable=False)

table('payment_reviews', 'Keputusan pemeriksaan transfer',
      'Menyimpan keputusan pemeriksa atas satu pengajuan transfer. Keputusan lama tidak diganti ketika Admin membuat pengajuan perbaikan baru.', [
    fk('payment_id', 'payments.id', 'Pengajuan yang diputuskan', unique=True),
    fk('reviewer_user_id', 'users.id', 'Super Admin dengan kewenangan yang telah ditetapkan'),
    c('decision', "ENUM('verified','returned')", 'Keputusan akhir untuk pengajuan tersebut'),
    c('reason', 'TEXT', 'Wajib untuk returned; catatan pemeriksaan untuk verified', nullable=True),
    c('reviewed_at', 'DATETIME(6)', 'Waktu keputusan disimpan'),
], ['Hanya transfer submitted dapat diputuskan. Setiap pengajuan mempunyai paling banyak satu keputusan akhir, sedangkan tindak lanjut perbaikan menjadi pengajuan baru.',
    'Keputusan verified mensyaratkan bank_matches yang sah dan dibuat atomik bersama pembaruan status, alokasi, serta nomor kuitansi. Pengembalian tidak membuat pencocokan bank.'], mutable=False)

table('cash_batches', 'Penyerahan dan setoran kas',
      'Mengelompokkan penerimaan tunai cabang untuk penyerahan kepada pusat dan penyetoran ke rekening. Penyerahan kepada pusat dibedakan dari masuknya uang ke bank.', [
    fk('branch_id', 'branches.id', 'Cabang asal seluruh pembayaran tunai'),
    fk('created_by_user_id', 'users.id', 'Penyusun kelompok penerimaan'),
    fk('submitted_by_user_id', 'users.id', 'Penyerah yang mengajukan, kosong sebelum diserahkan', nullable=True),
    fk('received_by_user_id', 'users.id', 'Penerima pusat, kosong sebelum penerimaan dikonfirmasi', nullable=True),
    fk('deposited_by_user_id', 'users.id', 'Petugas pencatat setoran bank, kosong sebelum disetor', nullable=True),
    fk('bank_account_id', 'bank_accounts.id', 'Rekening tujuan setoran, wajib ketika deposited', nullable=True),
    c('batch_no', 'VARCHAR(40)', 'Nomor kelompok kas yang unik', unique=True),
    c('status', "ENUM('draft','submitted','received','deposited')", 'Tahap penguasaan kas'),
    c('submitted_at', 'DATETIME(6)', 'Waktu penyerahan diajukan', nullable=True),
    c('received_at', 'DATETIME(6)', 'Waktu penerimaan pusat dikonfirmasi', nullable=True),
    c('deposited_at', 'DATETIME(6)', 'Waktu kas disetor ke bank', nullable=True),
    c('handover_proof_key', 'VARCHAR(255)', 'Bukti penyerahan privat jika digunakan', nullable=True),
    c('deposit_proof_key', 'VARCHAR(255)', 'Bukti setoran bank privat', nullable=True),
    c('notes', 'TEXT', 'Catatan penyerahan atau selisih yang perlu ditindaklanjuti', nullable=True),
], ['Jumlah kelompok berasal dari penjumlahan cash_batch_items, bukan nilai target tagihan. Anggota hanya pembayaran tunai recorded dari cabang yang sama.',
    'Daftar anggota dapat diperbaiki pada draft; setelah submitted, daftar dikunci. Kolom petugas dan waktu tiap tahap wajib terisi berpasangan sesuai statusnya.',
    'Prototipe mengasumsikan satu kelompok disetor penuh dalam satu transaksi bank. Pemecahan atau penggabungan setoran lintas kelompok memerlukan perubahan kebutuhan dan alokasi yang belum diaktifkan.',
    'Penerimaan pusat dan pencocokan setoran tidak menghasilkan pendapatan siswa baru. Kelompok received yang belum deposited menunjukkan kas di pusat, bukan selisih bank otomatis.'])

table('cash_batch_items', 'Rincian asal kas',
      'Menghubungkan kelompok kas dengan pembayaran tunai sumbernya. Hubungan ini memungkinkan pusat menelusuri nominal setoran sampai ke kuitansi siswa.', [
    fk('cash_batch_id', 'cash_batches.id', 'Kelompok penyerahan kas'),
    fk('payment_id', 'payments.id', 'Pembayaran tunai sumber', unique=True),
    c('amount', 'DECIMAL(14,2)', 'Seluruh nominal pembayaran tunai sumber'),
], ['Satu pembayaran tunai hanya menjadi anggota satu kelompok kas. Nominal anggota harus sama dengan nominal pembayaran, tanpa pembagian setoran pada lingkup inti.',
    'Penghapusan anggota hanya diperbolehkan pada draft dan dicatat dalam jejak aktivitas. Anggota kelompok submitted atau sesudahnya tidak dihapus diam-diam.'], mutable=False)

table('bank_accounts', 'Rekening resmi',
      'Menyimpan rekening resmi yang boleh menjadi tujuan pembayaran dan setoran. Data rekening dikelola Super Admin tanpa menyimpan kata sandi atau kredensial layanan bank.', [
    c('bank_name', 'VARCHAR(100)', 'Nama bank'),
    c('account_number', 'VARCHAR(40)', 'Nomor rekening', unique=True),
    c('account_holder', 'VARCHAR(100)', 'Nama pemilik rekening'),
    c('is_active', 'BOOLEAN', 'Boleh digunakan untuk pengajuan baru'),
], ['Rekening yang sudah dirujuk tidak dihapus dari sejarah. Kewenangan siapa yang boleh memeriksa mutasi rekening dikonfirmasi sebelum evaluasi mitra.'])

table('bank_entries', 'Rujukan dana masuk bank',
      'Mencatat satu dana masuk dari mutasi yang diperiksa manual oleh petugas berwenang. Tabel ini tidak menyatakan adanya koneksi otomatis dengan bank atau penyimpanan seluruh rekening koran.', [
    fk('bank_account_id', 'bank_accounts.id', 'Rekening tempat dana diterima'),
    fk('recorded_by_user_id', 'users.id', 'Petugas berwenang yang menyalin rujukan'),
    c('entry_reference', 'VARCHAR(120)', 'Referensi unik dalam rekening atau kode sumber yang dapat ditelusuri'),
    c('entry_date', 'DATE', 'Tanggal dana masuk menurut mutasi'),
    c('amount', 'DECIMAL(14,2)', 'Nominal dana masuk positif'),
    c('description', 'VARCHAR(255)', 'Uraian terbatas dari sumber yang diizinkan', nullable=True),
    c('evidence_storage_key', 'VARCHAR(255)', 'Potongan bukti privat bila diizinkan', nullable=True),
    c('status', "ENUM('active','void')", 'Keabsahan rujukan untuk pencocokan'),
    c('void_reason', 'VARCHAR(255)', 'Alasan pembatalan rujukan salah', nullable=True),
], ['Pasangan bank_account_id dan entry_reference unik. Jika mutasi tidak menyediakan nomor unik, petugas memakai kode sumber yang dapat ditemukan ulang pada dokumen dan memeriksa duplikasi tanggal serta nominal.',
    'Rujukan active yang sudah dicocokkan tidak disunting atau dibatalkan melalui alur biasa. Koreksi rujukan yang belum dipakai wajib mencatat alasan dan jejak pelaku.'])

table('bank_matches', 'Pencocokan penuh sumber dengan dana masuk',
      'Menghubungkan satu rujukan dana masuk dengan satu sumber penerimaan. Sumber tersebut hanya boleh transfer siswa atau setoran satu kelompok kas, bukan keduanya.', [
    fk('bank_entry_id', 'bank_entries.id', 'Dana masuk bank yang dipakai sekali', unique=True),
    fk('payment_id', 'payments.id', 'Transfer siswa sumber, kosong bila sumber kelompok kas', nullable=True, unique=True),
    fk('cash_batch_id', 'cash_batches.id', 'Kelompok kas sumber, kosong bila sumber transfer', nullable=True, unique=True),
    fk('matched_by_user_id', 'users.id', 'Pemeriksa pusat yang berwenang'),
    c('matched_amount', 'DECIMAL(14,2)', 'Nominal cocok penuh yang positif'),
    c('matched_at', 'DATETIME(6)', 'Waktu pencocokan'),
    c('notes', 'VARCHAR(255)', 'Penjelasan pemeriksaan jika diperlukan', nullable=True),
], ['Tepat satu dari payment_id dan cash_batch_id wajib terisi. Satu sumber dan satu bank_entry_id hanya dipakai satu kali pada lingkup pencocokan penuh.',
    'matched_amount sama dengan nominal bank_entries dan seluruh nominal sumber, serta rekening tujuan keduanya sama. Sumber payment harus transfer; sumber kelompok kas harus deposited.',
    'Pencocokan transfer dibuat dalam transaksi yang sama dengan keputusan verified dan penerbitan kuitansi. Setoran kas yang cocok hanya mengubah informasi penguasaan dana, bukan pendapatan.',
    'Pencocokan sebagian, satu mutasi untuk beberapa sumber, biaya bank, pengembalian dana, dan pembalikan pencocokan belum menjadi alur inti. Kasus demikian ditandai untuk tindak lanjut tanpa memaksa status cocok.'], mutable=False)

table('reminder_actions', 'Tindakan membuka tautan pengingat',
      'Menyimpan konteks ketika Admin meminta tautan WhatsApp untuk tagihan lewat jatuh tempo. Data ini hanya membuktikan tindakan pada aplikasi, bukan pesan terkirim, diterima, atau dibaca.', [
    fk('bill_id', 'bills.id', 'Tagihan sumber pesan'),
    fk('requested_by_user_id', 'users.id', 'Admin yang meminta tautan'),
    c('recipient_phone', 'VARCHAR(20)', 'Salinan nomor wali saat tindakan'),
    c('message_content', 'TEXT', 'Pratinjau pesan yang disiapkan'),
    c('outstanding_amount', 'DECIMAL(14,2)', 'Sisa tagihan pada waktu tindakan'),
    c('template_version', 'VARCHAR(30)', 'Versi templat aplikasi yang dipakai'),
    c('requested_at', 'DATETIME(6)', 'Waktu permintaan tautan dicatat'),
], ['Tagihan harus issued, lewat jatuh tempo, dan masih mempunyai sisa saat tautan dibentuk. Nomor serta isi pesan diperiksa ulang sebelum admin mengirim melalui WhatsApp.',
    'Tidak ada sent_status, sent_at, atau penjadwal pengiriman otomatis. Templat dasar berada pada berkas aplikasi dan tidak dijanjikan dapat diedit Super Admin melalui dasbor.'], mutable=False)

table('activity_logs', 'Jejak tindakan penting',
      'Mencatat pelaku dan perubahan penting untuk penelusuran operasional. Catatan ini membantu pemeriksaan riwayat tanpa mengklaim sebagai bukti keaslian hukum atau sistem audit yang lengkap.', [
    fk('actor_user_id', 'users.id', 'Pelaku terautentikasi'),
    fk('branch_id', 'branches.id', 'Konteks cabang bila relevan', nullable=True),
    c('action', 'VARCHAR(80)', 'Jenis tindakan yang terdaftar'),
    c('entity_type', 'VARCHAR(80)', 'Jenis objek dari daftar aplikasi yang dibatasi'),
    c('entity_id', 'BIGINT UNSIGNED', 'Identitas objek; rujukan logis polimorfik, bukan FK fisik'),
    c('change_summary', 'JSON', 'Ringkasan perubahan yang tidak memuat kata sandi atau bukti penuh'),
    c('request_id', 'VARCHAR(80)', 'Penanda permintaan untuk penelusuran'),
    c('occurred_at', 'DATETIME(6)', 'Waktu tindakan'),
], ['Jejak aktivitas bersifat tambah saja melalui aplikasi. Pelaku tidak dapat mengubah log melalui fungsi administrasi biasa.',
    'Entity_type dan entity_id tidak digambarkan sebagai FK ke semua tabel. Ketergantungan objek divalidasi oleh aplikasi, sedangkan data rahasia dan kredensial tidak disalin ke log.'], mutable=False)

assert len(schema) == 23
names = {t['name'] for t in schema}
for t in schema:
    assert len({x['name'] for x in t['fields']}) == len(t['fields'])
    for x in t['fields']:
        if x['ref']:
            p, q = x['ref'].split('.')
            assert p in names and q in {y['name'] for y in next(z for z in schema if z['name'] == p)['fields']}

def diagram():
    out = ['```mermaid', 'erDiagram']
    for t in schema:
        out.append('    ' + t['name'] + ' {')
        for f in t['fields']:
            typ = f['type'].split('(')[0].split()[0].lower()
            key = ' PK' if f['name'] == 'id' else (' FK' if f['ref'] else (' UK' if f['unique'] else ''))
            out.append(f"        {typ} {f['name']}{key}")
        out.append('    }')
    for t in schema:
        for f in t['fields']:
            if f['ref']:
                parent = f['ref'].split('.')[0]
                left = '|o' if f['nullable'] else '||'
                right = 'o|' if f['unique'] else 'o{'
                out.append(f"    {parent} {left}--{right} {t['name']} : \"{f['name']}\"")
    return '\n'.join(out + ['```'])

front = '''# PERANCANGAN BASIS DATA (SKEMA DAN ERD)

Dokumen ini memperbarui rancangan basis data prototipe Sistem Informasi Manajemen Operasional Bimbel Artha Balikpapan pada 25 Oktober 2026. Rancangan diselaraskan dengan audit sebelumnya, keputusan pengguna tentang WhatsApp dan kapasitas, serta kebutuhan integrasi pada Bab 1.

Skema terdiri atas **23 tabel rancangan** dengan MySQL dan mesin transaksi InnoDB sebagai DBMS sasaran. Versi implementasi belum dibekukan, sedangkan kamus data dan diagram ini belum merupakan migrasi SQL yang telah dieksekusi atau hasil pengujian aplikasi.

## 1. Dasar keputusan dan batas rancangan

WhatsApp menggunakan tombol yang menyiapkan nomor wali serta pesan tagihan lewat jatuh tempo, kemudian Admin mengirim melalui WhatsApp. Kelas hampir penuh menampilkan peringatan, kelas penuh menolak penambahan, dan tempat tersedia setelah keanggotaan diakhiri tanpa menghapus sejarah.

Pengajuan transfer oleh Admin Cabang dan keputusan oleh Super Admin dipakai sebagai rancangan kerja untuk divalidasi dengan mitra. Akses mutasi rekening, pemberi persetujuan potongan, prosedur tunai, ambang hampir penuh, serta pembayaran sebagian belum dinyatakan sebagai kebijakan mitra yang telah disahkan.

Model mendukung satu penerimaan untuk beberapa tagihan milik siswa dan cabang yang sama. Pembayaran sebagian belum diaktifkan pada rancangan awal, sehingga nominal tiap alokasi wajib sama dengan sisa tagihan yang dipilih sampai kebijakannya ditetapkan.

Pencocokan bank dibatasi pada satu dana masuk untuk satu transfer siswa atau satu setoran kelompok kas dengan nominal penuh. Pencocokan sebagian atau satu mutasi untuk beberapa sumber belum dipaksakan masuk ke rancangan inti, dan perbedaan nominal tetap ditampilkan untuk tindak lanjut.

| Pokok rancangan | Kedudukan dan penerapan |
| :--- | :--- |
| Dua peran pengguna | Admin Cabang dan Super Admin; tentor serta wali tidak memiliki akun dasbor inti |
| Kepemilikan cabang | Data operasional dibatasi penugasan; bills dan payments menyimpan cabang historis |
| Tarif dan diskon | Tarif disimpan per cakupan; potongan aktual disimpan pada tagihan tanpa nominal global |
| Kapasitas | Jumlah aktif dihitung dari interval keanggotaan; status penuh merupakan nilai turunan |
| Jadwal | Mata pelajaran berada pada sesi jadwal; konflik diperiksa menurut masa berlaku |
| Pembayaran | Penerimaan induk dipisahkan dari alokasi tagihan, pengajuan, dan keputusan |
| Kas dan bank | Penerimaan siswa, penyerahan ke pusat, setoran bank, dan pencocokan dibedakan |
| Templat WhatsApp | Berkas aplikasi berversi; Super Admin tidak dijanjikan penyunting templat melalui dasbor |
| Fitur di luar inti | Daftar tunggu otomatis, pengiriman otomatis, portal wali, kartu anggota, QRIS, dan peta publik ditunda |

Jumlah tabel mengikuti kebutuhan riwayat dan hubungan data, bukan sasaran pengurangan tabel. Nama learning_programs, capacity_rules, discount_rules, wa_templates, wa_logs, dan revenue_validations tidak digunakan sebagai tabel aktif pada skema revisi ini.

## 2. Entity Relationship Diagram

Diagram berikut menggambarkan seluruh tabel dan setiap kunci asing yang tercantum dalam kamus data. Kardinalitas opsional mengikuti kolom yang boleh kosong, sedangkan aturan gabungan dan validasi lintas tabel dijelaskan sesudah diagram.

'''

legend = '''

Relasi pengguna atau tentor dengan cabang dapat bersifat opsional sesuai peran atau pangkalannya. Dua relasi sumber pada bank_matches masing-masing opsional, tetapi kendala gabungan mewajibkan tepat satu sumber terisi.

## 3. Kamus data

Setiap tabel mempunyai id sebagai kunci utama, sedangkan atribut FK menunjuk kunci pada tabel yang disebutkan. Kolom created_at mencatat waktu pembuatan, dan updated_at hanya dipakai pada objek yang mempunyai perubahan keadaan.

Nominal menggunakan DECIMAL, bukan bilangan pecahan biner, dengan satuan rupiah. Waktu kejadian disimpan dalam UTC dan ditampilkan sebagai Asia/Makassar, sedangkan tanggal jatuh tempo dan jam jadwal menggunakan kalender operasional Balikpapan.

Nilai ENUM merupakan pilihan rancangan untuk MySQL, bukan klaim portabilitas langsung ke PostgreSQL. Keterangan unik per kolom berbeda dari kunci unik gabungan yang dituliskan pada aturan tiap tabel.

'''

body = []
for i, t in enumerate(schema, 1):
    body += [f"### 3.{i} {t['name']}: {t['label']}", '', t['purpose'], '',
             '| Kolom | Tipe rancangan | Boleh kosong | Kunci atau rujukan | Keterangan |',
             '| :--- | :--- | :---: | :--- | :--- |']
    for f in t['fields']:
        key = 'PK, AUTO_INCREMENT' if f['name'] == 'id' else ('FK ke `' + f['ref'] + '`' if f['ref'] else 'Tidak ada FK')
        if f['unique'] and f['name'] != 'id':
            key += '; UNIQUE'
        body.append(f"| `{f['name']}` | `{f['type']}` | {'Ya' if f['nullable'] else 'Tidak'} | {key} | {f['description']} |")
    body.append('')
    body.extend('- ' + r for r in t['rules'])
    body.append('')

tail = '''## 4. Aturan transaksi dan konsistensi

### 4.1 Penempatan siswa dan perubahan kapasitas

Penambahan anggota, pengakhiran keanggotaan, pengubahan kapasitas, serta penggantian ruang wajib mengikuti penguncian yang konsisten. Pemeriksaan antarmuka membantu pengguna, tetapi keputusan akhir tetap dilakukan ulang oleh peladen pada saat transaksi disimpan.

Urutan penempatan adalah memeriksa kewenangan, memulai transaksi, mengunci baris kelas, lalu menghitung anggota aktif. Sistem menolak kelas ditutup, tidak memiliki jadwal ruang aktif, tidak sesuai cabang atau jenjang, atau telah mencapai kapasitas.

Ketika masih tersedia tempat, satu interval keanggotaan ditambahkan dan jejak tindakan dicatat sebelum transaksi diselesaikan. Ketika siswa keluar, ended_at dan alasan diisi, sehingga hitungan aktif berkurang tanpa menghapus identitas siswa atau interval lama.

Kapasitas ruang diperiksa pada seluruh jadwal aktif yang masa berlakunya masih relevan. Penurunan batas kelas atau daya tampung ruang ditolak bila tidak memenuhi jumlah peserta aktif atau melanggar ruang yang digunakan.

### 4.2 Benturan jadwal

Benturan mensyaratkan jadwal aktif, rentang tanggal yang memiliki kejadian hari sama, serta waktu yang beririsan. Rumus irisan jam adalah mulai_lama < selesai_baru dan selesai_lama > mulai_baru, sehingga dua sesi yang bersentuhan tepat pada batas waktu tidak dianggap bertumpang tindih.

Pada penyuntingan, identitas jadwal sendiri dikecualikan dan masa berlaku diperiksa kembali. Pemeriksaan mencakup tentor lintas cabang, ruang yang sama, dan kelompok belajar yang sama tanpa mengumumkan seluruh rincian cabang lain.

Peringatan benturan menjadi bahan peninjauan pengelola, bukan bukti bahwa seluruh irisan selalu dilarang oleh mitra. Calon jadwal dapat disimpan dengan is_active bernilai FALSE selama peninjauan, sedangkan catatan keputusan dicatat pada activity_logs.

Jadwal yang telah diperbaiki diperiksa ulang sebelum ditetapkan aktif. Kebijakan mengaktifkan jadwal yang masih mempunyai konflik harus ditetapkan bersama mitra terlebih dahulu, sehingga prototipe belum menjanjikan pengabaian konflik secara sepihak.

Penyimpanan jadwal perlu mengunci objek tentor, ruang, dan kelas yang relevan dalam urutan tetap agar dua permintaan tidak lolos bersamaan. Jika pemeriksaan memakai rentang tanggal mingguan, pelaksanaan fisik harus memastikan irisan tersebut benar-benar memuat hari yang dimaksud, bukan hanya menganggap setiap irisan satu hari pasti benturan.

### 4.3 Pembayaran dan alokasi

Penerimaan tunai dicatat satu kali dengan status recorded, alokasi sah, dan nomor kuitansi. Pengajuan transfer diberi status submitted tanpa kuitansi resmi dan belum mengurangi sisa tagihan.

Persetujuan transfer dimulai dengan mengunci pengajuan, seluruh tagihan terkait dalam urutan id, dan rujukan mutasi. Sistem memeriksa status awal, rekening, nominal penuh, sisa tagihan, jumlah alokasi, kewenangan, serta penggunaan rujukan bank sebelum menyimpan bank_matches dan payment_reviews.

Pembaruan status verified, waktu konfirmasi, kuitansi, dan jejak aktivitas disimpan dalam transaksi yang sama. Permintaan ganda mengembalikan hasil yang sudah ada atau ditolak tanpa menambah alokasi sah dan pencocokan kedua.

Pengembalian pengajuan wajib mempunyai alasan dan tidak mencatat dana sebagai diterima. Perbaikan dibuat sebagai pengajuan baru yang merujuk baris returned, sehingga bukti dan keputusan sebelumnya tetap tersedia.

### 4.4 Kas, setoran, dan pencocokan

Kelompok kas hanya memuat pembayaran tunai yang sudah tercatat dari cabang yang sama. Status submitted menandai penyerahan yang diajukan, received menandai penerimaan pusat, dan deposited menandai kas disetor ke rekening resmi.

Pencocokan setoran dilakukan terhadap nominal penuh kelompok dan satu rujukan dana masuk. Satu pembayaran tunai tidak dapat dimasukkan kembali ke kelompok lain, dan satu mutasi tidak boleh dipakai ulang untuk transfer maupun setoran lain.

Uang tunai yang belum disetor tetap termasuk penerimaan siswa dan ditampilkan pada posisi penguasaan kas yang sesuai. Nominal setoran serta bank_matches tidak dijumlahkan lagi sebagai penerimaan siswa, sehingga pengalihan tempat uang tidak menambah pendapatan.

### 4.5 Perlindungan data dan riwayat

Kunci asing transaksi menggunakan pembatasan penghapusan objek yang telah dirujuk. Pengguna, siswa, cabang, tarif, serta rekening dinonaktifkan atau diberi status yang sesuai agar riwayat tetap dapat ditelusuri.

Bukti transfer dan potongan mutasi berada pada penyimpanan privat dengan pemeriksaan izin pada setiap pembacaan. Nomor rekening tidak disertai kredensial bank, dan log tidak menyalin kata sandi, berkas bukti penuh, atau rahasia sesi.

Tindakan penting mencatat pelaku, waktu, objek, dan ringkasan perubahan secara proporsional. Retensi data, akses bukti, serta penghapusan data setelah penelitian ditetapkan bersama mitra sebelum penggunaan data nyata.

## 5. Dasar penghitungan laporan

Penghitungan laporan memisahkan kewajiban siswa, penerimaan sah, dan keberadaan dana pada kas atau bank. Penyaringan periode memakai tanggal yang sesuai untuk ukuran yang dilaporkan, sehingga periode tagihan tidak dicampur dengan waktu penerimaan.

| Ukuran | Dasar penghitungan |
| :--- | :--- |
| Nilai kewajiban | Jumlah total_amount pada tagihan issued sesuai periode cakupan biaya |
| Alokasi sah | Alokasi dengan induk cash recorded atau bank_transfer verified |
| Sisa tagihan | Total tagihan dikurangi alokasi sah; tidak boleh negatif |
| Pelunasan | paid jika sisa nol termasuk pembebasan penuh; unpaid jika kewajiban positif tanpa alokasi; partial jika sisa positif setelah alokasi |
| Lewat jatuh tempo | Tagihan issued dengan sisa positif dan due_date sebelum tanggal operasional saat ini |
| Penerimaan cabang | Jumlah payments sah menurut branch_id historis dan payment_date, bukan jumlah baris setelah JOIN alokasi |
| Pengajuan tertunda | Jumlah transfer submitted, disajikan terpisah dari penerimaan sah |
| Tunai belum diserahkan | Pembayaran tunai yang belum masuk kelompok submitted atau sesudahnya |
| Kas dalam proses penyerahan | Kelompok submitted yang belum received |
| Kas di pusat | Kelompok received yang belum deposited |
| Setoran menunggu pencocokan | Kelompok deposited tanpa bank_matches |
| Dana masuk cocok | Jumlah bank_matches pada sumber yang tepat; bukan tambahan penerimaan siswa |
| Tindakan pengingat | Jumlah reminder_actions; bukan jumlah pesan terbukti terkirim |
| Beban tentor | Jumlah durasi sesi yang berlaku pada minggu yang diperiksa, tanpa label berlebih sebelum batas disepakati |

Laporan penerimaan dihitung pada tingkat induk pembayaran untuk mencegah penggandaan ketika satu pembayaran memiliki beberapa alokasi. Laporan per komponen biaya menggunakan alokasi, dengan agregasi yang menjaga jumlah total tetap sama dengan penerimaan induk.

Perbandingan penerimaan sah dan dana yang telah cocok bank menggunakan kelompok transaksi sumber serta periode penerimaan yang sama. Untuk kelompok kas lintas periode, rincian cash_batch_items ditelusuri ke payment_date sumber, sehingga tanggal pencocokan tidak langsung dibandingkan dengan periode penerimaan yang berbeda.

## 6. Hubungan dengan kebutuhan dan use case

Pemetaan berikut mengikuti penomoran use case revisi yang dipakai pada dokumen skenario dan Bab 3. Rumusan masalah ketiga diwujudkan melalui pengujian serta UAT atas kebutuhan, bukan melalui penambahan tabel operasional bernama UAT.

| Use case | Kelompok tabel utama | Kaitan kebutuhan |
| :--- | :--- | :--- |
| UC-00 Autentikasi | users, branches, activity_logs | Pembatasan akses seluruh fungsi |
| UC-01 Siswa | students, branches, academic_years, activity_logs | Integrasi data pendaftaran, RM 1 |
| UC-02 Kelas dan ruang | classes, class_rooms, branches, academic_years, activity_logs | Kapasitas dan wadah belajar, RM 1 |
| UC-03 Keanggotaan | class_enrollments, students, classes, class_schedules, class_rooms, activity_logs | Penempatan dan siswa keluar, RM 1 |
| UC-04 Jadwal | class_schedules, mentors, mentor_subjects, subjects, classes, class_rooms, activity_logs | Penjadwalan dan pencegahan irisan, RM 1 |
| UC-05 Tarif dan tagihan | fee_tariffs, bills, students, users, academic_years, branches, activity_logs | Kewajiban dan dasar biaya, RM 1 |
| UC-06 Tunai | payments, payment_allocations, bills, users, activity_logs | Penerimaan sah, RM 1 |
| UC-07 Pengajuan transfer | payments, payment_allocations, bills, bank_accounts, users, activity_logs | Pengajuan lintas peran, RM 1 dan RM 2 |
| UC-08 Pemeriksaan transfer | payment_reviews, payments, payment_allocations, bills, bank_entries, bank_matches, bank_accounts, users, activity_logs | Keputusan dan sumber dana, RM 2 |
| UC-09 Tautan WhatsApp | reminder_actions, bills, payment_allocations, payments, students, users | Pengingat manual berbasis tunggakan, RM 1 |
| UC-10 Kelompok kas | cash_batches, cash_batch_items, payments, bank_accounts, users, activity_logs | Penelusuran kas cabang sampai pusat, RM 2 |
| UC-11 Pencocokan bank | bank_entries, bank_matches, payments, cash_batches, cash_batch_items, bank_accounts, users, activity_logs | Pencocokan penerimaan, RM 2 |
| UC-12 Dasbor dan laporan | branches, students, classes, class_enrollments, class_schedules, mentors, subjects, bills, payments, payment_allocations, payment_reviews, cash_batches, cash_batch_items, bank_entries, bank_matches, reminder_actions | Konsolidasi cabang dan penelusuran sumber, RM 2 |
| UC-13 Data induk dan akun | academic_years, branches, users, subjects, mentors, mentor_subjects, bank_accounts, activity_logs | Fondasi seluruh fungsi |

Seluruh tabel mempunyai fungsi yang dapat ditelusuri, tetapi keberadaan rujukan tabel tidak membuktikan implementasi berhasil. Keterlacakan kebutuhan, cerita pengguna, iterasi, dan pengujian dijabarkan lebih lanjut pada matriks pendamping Bab 3.

## 7. Pemeriksaan yang diperlukan sebelum implementasi

Pemeriksaan dokumen memastikan kesamaan nama tabel, atribut, relasi, dan skenario yang direncanakan. Validasi fisik tetap memerlukan migrasi pada versi MySQL terpilih, data uji, serta pengujian transaksi serentak pada aplikasi.

| Pemeriksaan | Hasil yang harus diperiksa saat implementasi |
| :--- | :--- |
| Akun tanpa cabang yang sah | Tidak memperoleh hak Super Admin atau akses cabang lain |
| Dua penempatan pada tempat terakhir | Hanya satu interval aktif baru tersimpan |
| Keluar dan masuk kembali | Interval lama tetap ada dan tidak muncul dua keanggotaan aktif |
| Jadwal disunting atau nonaktif | Tidak berbenturan dengan dirinya sendiri atau jadwal lama yang tidak berlaku |
| Ruang berbeda cabang atau terlalu kecil | Penetapan ditolak dengan alasan yang dapat dipahami |
| Tarif ganda pada cakupan sama | Pemilihan ambigu ditolak sebelum tagihan diterbitkan |
| Paket semester | Tidak dibuat ulang sebagai kewajiban bulanan |
| Satu pembayaran dua tagihan | Alokasi seimbang dan penerimaan dihitung satu kali |
| Bukti dikembalikan lalu diajukan ulang | Rantai pengajuan dan keputusan lama tetap terlihat |
| Dua persetujuan untuk sisa tagihan sama | Konfirmasi kedua tidak melampaui sisa kewajiban |
| Rujukan bank dipakai ulang | Kendala unik dan transaksi menolak pencocokan kedua |
| Tunai diserahkan dan disetor | Tidak menambah penerimaan siswa untuk kedua kalinya |
| Siswa berpindah cabang | Tagihan dan penerimaan historis tetap pada cabang asalnya |
| Tautan WhatsApp dibuka | Log hanya mencatat permintaan tautan, tanpa mengklaim pesan terkirim |

Tidak ada hasil pengujian aplikasi yang dinyatakan lulus dalam dokumen rancangan ini. Bukti eksekusi migrasi, skenario uji, dan penerimaan mitra baru diisi setelah pelaksanaan.

## 8. Perubahan dari rancangan sebelumnya dan keputusan terbuka

Rancangan sebelumnya yang berisi enam belas tabel disimpan pada folder SEBELUM_REVISI untuk pembandingan. Revisi mempertahankan data operasional inti dan menambah hubungan yang diperlukan untuk alokasi, pemeriksaan, kas, bank, serta jejak tindakan.

| Bagian lama | Bentuk revisi |
| :--- | :--- |
| payments langsung ke satu bill | payments sebagai induk dan payment_allocations sebagai rincian beberapa tagihan |
| Penanda verifikasi tanpa riwayat pengembalian | payment_reviews dan resubmission_of_id pada pengajuan baru |
| revenue_validations membandingkan tagihan dengan penerimaan | bank_accounts, bank_entries, bank_matches, cash_batches, dan cash_batch_items |
| wa_logs berstatus terkirim | reminder_actions hanya mencatat permintaan tautan manual |
| Diskon global pada profil siswa | Potongan aktual, alasan, dan pemberi persetujuan pada bills |
| Kelas berstatus hampir penuh atau penuh tersimpan | classes.status active atau closed, dengan keterisian turunan |
| Satu baris siswa dan kelas seumur hidup | Interval keanggotaan yang dapat berulang setelah interval lama berakhir |
| Mata pelajaran langsung pada kelas | Mata pelajaran pada sesi class_schedules |
| Tarif tanpa pembeda cabang atau sesi | Tarif bercabang dan bersesi dengan masa berlaku serta siklus eksplisit |
| Klaim cakupan seratus persen | Pemeriksaan struktur yang dibatasi, diikuti pengujian implementasi yang belum dilaksanakan |

Kewenangan pemeriksa rekening, batas potongan, tarif berlaku, ambang hampir penuh, serta keterwakilan cabang pada UAT tetap dicatat sebagai keputusan terbuka. Kebijakan tersebut perlu ditetapkan sebelum fungsi terkait dibekukan dan digunakan sebagai dasar penerimaan.

Bab 1 yang lama masih menyatakan verifikasi transfer oleh Admin Cabang, sehingga perlu diselaraskan apabila rancangan pemeriksaan pusat dipilih. Perubahan Bab 1 tidak dilakukan diam-diam melalui dokumen basis data ini, dan status rancangan tersebut juga dinyatakan pada Bab 3.
'''

text = front + diagram() + legend + '\n'.join(body) + '\n' + tail
assert '\u2014' not in text and '\u2013' not in text
TARGET.write_text(text, encoding='utf-8')
meta = dict(date='2026-10-25', status='document_design_only_not_executed_ddl', dbms='MySQL with InnoDB; final version pending', tables=schema)
(OUT / 'SKEMA_TERSTRUKTUR.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
stats = dict(tables=len(schema), fields=sum(len(t['fields']) for t in schema), foreign_keys=sum(bool(f['ref']) for t in schema for f in t['fields']), sha256=hashlib.sha256(TARGET.read_bytes()).hexdigest())
print(json.dumps(stats))
