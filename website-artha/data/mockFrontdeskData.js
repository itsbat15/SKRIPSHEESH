// ============================================
// DATA MOCK FRONTDESK / ADMIN CABANG
// Diselaraskan dengan Skema Database 20 Tabel
// ============================================

// --- GRUP A: FONDASI & KONFIGURASI ---

export const cabangInfo = {
  id: 1,
  branch_name: "Artha 1",
  label: "Pusat",
  address: "Balikpapan Baru, J-2 No. 7",
  phone_wa: "081234567890",
  google_maps_url: "https://maps.google.com/?q=Bimbel+Artha+1",
  total_rooms: 5,
  is_active: true,
  adminName: "Siti Rahmawati",
};

export const academicYears = [
  { id: 1, name: "2025/2026", start_date: "2025-07-01", end_date: "2026-06-30", is_active: false },
  { id: 2, name: "2026/2027", start_date: "2026-07-01", end_date: "2027-06-30", is_active: true },
];

export const subjects = [
  { id: 1, subject_name: "Matematika", description: "Matematika dasar dan lanjut", is_active: true },
  { id: 2, subject_name: "Bahasa Inggris", description: "Grammar, vocabulary, dan conversation", is_active: true },
  { id: 3, subject_name: "IPA", description: "Ilmu Pengetahuan Alam", is_active: true },
  { id: 4, subject_name: "Fisika", description: "Fisika SMA", is_active: true },
  { id: 5, subject_name: "Calistung", description: "Baca Tulis Hitung untuk TK/SD Kelas 1", is_active: true },
  { id: 6, subject_name: "Bahasa Indonesia", description: "Tata bahasa dan sastra Indonesia", is_active: true },
];

export const learningPrograms = [
  { id: 1, program_name: "Reguler", description: "Program belajar reguler 3x seminggu", is_active: true },
  { id: 2, program_name: "Intensif", description: "Program intensif 5x seminggu menjelang ujian", is_active: true },
  { id: 3, program_name: "Paket SMA 12", description: "Paket khusus kelas 12 SMA menuju SNBT/UTBK", is_active: true },
];

export const feeTariffs = [
  { id: 1, academic_year_id: 2, learning_program_id: 1, grade_level: "TK", class_grade_start: 0, class_grade_end: 0, fee_type: "spp_monthly", amount: 250000, description: "SPP Bulanan TK (Calistung)", is_active: true },
  { id: 2, academic_year_id: 2, learning_program_id: 1, grade_level: "SD", class_grade_start: 1, class_grade_end: 3, fee_type: "spp_monthly", amount: 250000, description: "SPP Bulanan SD Kelas 1-3", is_active: true },
  { id: 3, academic_year_id: 2, learning_program_id: 1, grade_level: "SD", class_grade_start: 4, class_grade_end: 6, fee_type: "spp_monthly", amount: 330000, description: "SPP Bulanan SD Kelas 4-6", is_active: true },
  { id: 4, academic_year_id: 2, learning_program_id: 1, grade_level: "SMP", class_grade_start: 7, class_grade_end: 9, fee_type: "spp_monthly", amount: 350000, description: "SPP Bulanan SMP", is_active: true },
  { id: 5, academic_year_id: 2, learning_program_id: 1, grade_level: "SMA", class_grade_start: 10, class_grade_end: 11, fee_type: "spp_monthly", amount: 380000, description: "SPP Bulanan SMA Kelas 10-11", is_active: true },
  { id: 6, academic_year_id: 2, learning_program_id: 3, grade_level: "SMA", class_grade_start: 12, class_grade_end: 12, fee_type: "spp_monthly", amount: 2250000, description: "Paket SMA Kelas 12 (Lunas)", is_active: true },
  { id: 7, academic_year_id: 2, learning_program_id: 1, grade_level: "SD", class_grade_start: 1, class_grade_end: 6, fee_type: "module_semester", amount: 200000, description: "Biaya Modul/Buku Les SD per semester", is_active: true },
  { id: 8, academic_year_id: 2, learning_program_id: 1, grade_level: "SMP", class_grade_start: 7, class_grade_end: 9, fee_type: "module_semester", amount: 200000, description: "Biaya Modul/Buku Les SMP per semester", is_active: true },
  { id: 9, academic_year_id: 2, learning_program_id: 1, grade_level: "SMA", class_grade_start: 10, class_grade_end: 12, fee_type: "module_semester", amount: 200000, description: "Biaya Modul/Buku Les SMA per semester", is_active: true },
];

export const discountRules = [
  { id: 1, discount_name: "Diskon Kakak-Adik", discount_type: "fixed_amount", discount_value: 200000, description: "Potongan untuk siswa yang memiliki saudara kandung terdaftar", is_active: true },
];

export const capacityRules = [
  { id: 1, grade_level: "TK", class_grade_start: 0, class_grade_end: 0, room_type: "standard", max_students: 5, description: "TK/Calistung max 5 siswa", is_active: true },
  { id: 2, grade_level: "SD", class_grade_start: 1, class_grade_end: 1, room_type: "standard", max_students: 5, description: "SD Kelas 1 max 5 siswa (intensif calistung)", is_active: true },
  { id: 3, grade_level: "SD", class_grade_start: 2, class_grade_end: 2, room_type: "standard", max_students: 7, description: "SD Kelas 2 max 6-7 siswa", is_active: true },
  { id: 4, grade_level: "SD", class_grade_start: 3, class_grade_end: 6, room_type: "standard", max_students: 10, description: "SD Kelas 3-6 max 8-10 siswa", is_active: true },
  { id: 5, grade_level: "SMP", class_grade_start: 7, class_grade_end: 9, room_type: "standard", max_students: 12, description: "SMP max 10-12 siswa (ruang standar)", is_active: true },
  { id: 6, grade_level: "SMP", class_grade_start: 7, class_grade_end: 9, room_type: "large", max_students: 14, description: "SMP max 14 siswa (ruang besar)", is_active: true },
  { id: 7, grade_level: "SMA", class_grade_start: 10, class_grade_end: 12, room_type: "standard", max_students: 14, description: "SMA max 12-14 siswa", is_active: true },
];

// --- GRUP B: DATA OPERASIONAL ---

export const mentors = [
  { id: 1, branch_id: 1, full_name: "Om Imam", phone_wa: "081111111101", is_active: true },
  { id: 2, branch_id: 1, full_name: "Tante Slamet", phone_wa: "081111111102", is_active: true },
  { id: 3, branch_id: 1, full_name: "Tante Novia", phone_wa: "081111111103", is_active: true },
  { id: 4, branch_id: 1, full_name: "Tante Sulis", phone_wa: "081111111104", is_active: true },
  { id: 5, branch_id: 1, full_name: "Tante Zulfa", phone_wa: "081111111105", is_active: true },
  { id: 6, branch_id: 1, full_name: "Om Arman", phone_wa: "081111111106", is_active: true },
  { id: 7, branch_id: 1, full_name: "Tante Dewi", phone_wa: "081111111107", is_active: true },
];

export const mentorSubjects = [
  { id: 1, mentor_id: 1, subject_id: 1 }, // Om Imam → Matematika
  { id: 2, mentor_id: 1, subject_id: 3 }, // Om Imam → IPA
  { id: 3, mentor_id: 2, subject_id: 5 }, // Tante Slamet → Calistung
  { id: 4, mentor_id: 3, subject_id: 1 }, // Tante Novia → Matematika
  { id: 5, mentor_id: 4, subject_id: 6 }, // Tante Sulis → B. Indonesia
  { id: 6, mentor_id: 5, subject_id: 2 }, // Tante Zulfa → B. Inggris
  { id: 7, mentor_id: 6, subject_id: 4 }, // Om Arman → Fisika
  { id: 8, mentor_id: 7, subject_id: 5 }, // Tante Dewi → Calistung
];

export const classRooms = [
  { id: 1, branch_id: 1, room_name: "Ruang 1", room_type: "standard", physical_capacity: 12, is_active: true },
  { id: 2, branch_id: 1, room_name: "Ruang 2", room_type: "standard", physical_capacity: 12, is_active: true },
  { id: 3, branch_id: 1, room_name: "Ruang 3", room_type: "large", physical_capacity: 16, is_active: true },
  { id: 4, branch_id: 1, room_name: "Ruang 4", room_type: "standard", physical_capacity: 10, is_active: true },
  { id: 5, branch_id: 1, room_name: "Ruang 5", room_type: "standard", physical_capacity: 10, is_active: true },
];

export const classes = [
  { id: 1, branch_id: 1, academic_year_id: 2, subject_id: 5, learning_program_id: 1, class_name: "Calistung-A", grade_level: "TK", class_grade: 0, max_students: 5, current_students: 4, status: "open" },
  { id: 2, branch_id: 1, academic_year_id: 2, subject_id: 1, learning_program_id: 1, class_name: "SD-A (Mat)", grade_level: "SD", class_grade: 5, max_students: 10, current_students: 8, status: "almost_full" },
  { id: 3, branch_id: 1, academic_year_id: 2, subject_id: 1, learning_program_id: 1, class_name: "SD-B (Mat)", grade_level: "SD", class_grade: 4, max_students: 10, current_students: 5, status: "open" },
  { id: 4, branch_id: 1, academic_year_id: 2, subject_id: 3, learning_program_id: 1, class_name: "SD-C (IPA)", grade_level: "SD", class_grade: 2, max_students: 7, current_students: 3, status: "open" },
  { id: 5, branch_id: 1, academic_year_id: 2, subject_id: 1, learning_program_id: 1, class_name: "SMP-A (Mat)", grade_level: "SMP", class_grade: 7, max_students: 12, current_students: 7, status: "open" },
  { id: 6, branch_id: 1, academic_year_id: 2, subject_id: 6, learning_program_id: 1, class_name: "SMP-B (B.Indo)", grade_level: "SMP", class_grade: 9, max_students: 12, current_students: 12, status: "full" },
  { id: 7, branch_id: 1, academic_year_id: 2, subject_id: 4, learning_program_id: 1, class_name: "SMA-A (Fis)", grade_level: "SMA", class_grade: 11, max_students: 14, current_students: 6, status: "open" },
  { id: 8, branch_id: 1, academic_year_id: 2, subject_id: 2, learning_program_id: 1, class_name: "ENG-A (B.Ing)", grade_level: "SMP", class_grade: 8, max_students: 12, current_students: 9, status: "almost_full" },
];

export const classSchedules = [
  { id: 1, class_id: 1, mentor_id: 2, room_id: 4, day_of_week: "monday", start_time: "07:30", end_time: "09:00", is_active: true },
  { id: 2, class_id: 1, mentor_id: 2, room_id: 4, day_of_week: "wednesday", start_time: "07:30", end_time: "09:00", is_active: true },
  { id: 3, class_id: 1, mentor_id: 2, room_id: 4, day_of_week: "friday", start_time: "07:30", end_time: "09:00", is_active: true },
  { id: 4, class_id: 2, mentor_id: 1, room_id: 1, day_of_week: "monday", start_time: "15:30", end_time: "17:00", is_active: true },
  { id: 5, class_id: 2, mentor_id: 1, room_id: 1, day_of_week: "wednesday", start_time: "15:30", end_time: "17:00", is_active: true },
  { id: 6, class_id: 2, mentor_id: 1, room_id: 1, day_of_week: "friday", start_time: "15:30", end_time: "17:00", is_active: true },
  { id: 7, class_id: 3, mentor_id: 1, room_id: 2, day_of_week: "tuesday", start_time: "14:00", end_time: "15:30", is_active: true },
  { id: 8, class_id: 3, mentor_id: 1, room_id: 2, day_of_week: "thursday", start_time: "14:00", end_time: "15:30", is_active: true },
  { id: 9, class_id: 3, mentor_id: 1, room_id: 2, day_of_week: "saturday", start_time: "14:00", end_time: "15:30", is_active: true },
  { id: 10, class_id: 4, mentor_id: 3, room_id: 5, day_of_week: "monday", start_time: "09:00", end_time: "10:30", is_active: true },
  { id: 11, class_id: 4, mentor_id: 3, room_id: 5, day_of_week: "wednesday", start_time: "09:00", end_time: "10:30", is_active: true },
  { id: 12, class_id: 4, mentor_id: 3, room_id: 5, day_of_week: "friday", start_time: "09:00", end_time: "10:30", is_active: true },
  { id: 13, class_id: 5, mentor_id: 1, room_id: 1, day_of_week: "monday", start_time: "17:00", end_time: "18:30", is_active: true },
  { id: 14, class_id: 5, mentor_id: 1, room_id: 1, day_of_week: "wednesday", start_time: "17:00", end_time: "18:30", is_active: true },
  { id: 15, class_id: 5, mentor_id: 1, room_id: 1, day_of_week: "friday", start_time: "17:00", end_time: "18:30", is_active: true },
  { id: 16, class_id: 6, mentor_id: 4, room_id: 3, day_of_week: "tuesday", start_time: "17:00", end_time: "18:30", is_active: true },
  { id: 17, class_id: 6, mentor_id: 4, room_id: 3, day_of_week: "thursday", start_time: "17:00", end_time: "18:30", is_active: true },
  { id: 18, class_id: 6, mentor_id: 4, room_id: 3, day_of_week: "saturday", start_time: "17:00", end_time: "18:30", is_active: true },
  { id: 19, class_id: 7, mentor_id: 6, room_id: 1, day_of_week: "monday", start_time: "19:00", end_time: "20:30", is_active: true },
  { id: 20, class_id: 7, mentor_id: 6, room_id: 1, day_of_week: "wednesday", start_time: "19:00", end_time: "20:30", is_active: true },
  { id: 21, class_id: 7, mentor_id: 6, room_id: 1, day_of_week: "friday", start_time: "19:00", end_time: "20:30", is_active: true },
  { id: 22, class_id: 8, mentor_id: 5, room_id: 2, day_of_week: "tuesday", start_time: "17:00", end_time: "18:30", is_active: true },
  { id: 23, class_id: 8, mentor_id: 5, room_id: 2, day_of_week: "thursday", start_time: "17:00", end_time: "18:30", is_active: true },
  { id: 24, class_id: 8, mentor_id: 5, room_id: 2, day_of_week: "saturday", start_time: "17:00", end_time: "18:30", is_active: true },
];

export const students = [
  { id: 1, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-001", full_name: "Ahmad Farhan", birth_place: "Balikpapan", birth_date: "2015-03-12", gender: "L", parent_name: "Budi Santoso", parent_phone_wa: "081234567890", school_origin: "SDN 004 Balikpapan", grade_level: "SD", class_grade: 5, home_address: "Jl. MT Haryono No. 5", sibling_student_id: null, discount_amount: 0, status: "active", registered_at: "2026-01-15" },
  { id: 2, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-002", full_name: "Putri Amelia", birth_place: "Balikpapan", birth_date: "2012-08-21", gender: "P", parent_name: "Dewi Kartika", parent_phone_wa: "081345678901", school_origin: "SMPN 1 Balikpapan", grade_level: "SMP", class_grade: 9, home_address: "Perum Balikpapan Baru Blok J5", sibling_student_id: null, discount_amount: 0, status: "active", registered_at: "2026-02-03" },
  { id: 3, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-003", full_name: "Rizky Maulana", birth_place: "Samarinda", birth_date: "2009-12-05", gender: "L", parent_name: "Hendra Wijaya", parent_phone_wa: "082456789012", school_origin: "SMAN 1 Balikpapan", grade_level: "SMA", class_grade: 11, home_address: "Jl. Soekarno Hatta KM 2", sibling_student_id: null, discount_amount: 0, status: "active", registered_at: "2025-11-20" },
  { id: 4, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-004", full_name: "Nabila Zahra", birth_place: "Balikpapan", birth_date: "2020-06-18", gender: "P", parent_name: "Rina Agustina", parent_phone_wa: "085567890123", school_origin: "TK Pelita Hati", grade_level: "TK", class_grade: 0, home_address: "Perumahan San Fransisco FB-10", sibling_student_id: null, discount_amount: 0, status: "active", registered_at: "2026-03-10" },
  { id: 5, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-005", full_name: "Dimas Prasetyo", birth_place: "Balikpapan", birth_date: "2014-01-25", gender: "L", parent_name: "Agus Prasetyo", parent_phone_wa: "087678901234", school_origin: "SDN 014 Balikpapan", grade_level: "SD", class_grade: 6, home_address: "Jl. Ruhui Rahayu Blok C3", sibling_student_id: 9, discount_amount: 200000, status: "active", registered_at: "2026-01-22" },
  { id: 6, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-006", full_name: "Salsabila Nur", birth_place: "Balikpapan", birth_date: "2016-09-03", gender: "P", parent_name: "Nur Hidayah", parent_phone_wa: "081789012345", school_origin: "SD Islam Al-Azhar", grade_level: "SD", class_grade: 4, home_address: "Perum Balikpapan Regency A5", sibling_student_id: null, discount_amount: 0, status: "active", registered_at: "2026-04-05" },
  { id: 7, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-007", full_name: "Raffi Aditya", birth_place: "Balikpapan", birth_date: "2013-04-14", gender: "L", parent_name: "Eko Wahyudi", parent_phone_wa: "082890123456", school_origin: "SMPN 4 Balikpapan", grade_level: "SMP", class_grade: 7, home_address: "Jl. Jend Sudirman No. 12", sibling_student_id: null, discount_amount: 0, status: "active", registered_at: "2025-12-18" },
  { id: 8, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-008", full_name: "Ayu Lestari", birth_place: "Balikpapan", birth_date: "2009-07-30", gender: "P", parent_name: "Sri Lestari", parent_phone_wa: "085901234567", school_origin: "SMAN 2 Balikpapan", grade_level: "SMA", class_grade: 11, home_address: "Jl. MT Haryono KM 5", sibling_student_id: null, discount_amount: 0, status: "active", registered_at: "2026-01-08" },
  { id: 9, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-009", full_name: "Muhammad Iqbal", birth_place: "Balikpapan", birth_date: "2018-11-10", gender: "L", parent_name: "Agus Prasetyo", parent_phone_wa: "087678901234", school_origin: "SDN 028 Balikpapan", grade_level: "SD", class_grade: 2, home_address: "Jl. Ruhui Rahayu Blok C3", sibling_student_id: 5, discount_amount: 200000, status: "active", registered_at: "2026-05-01" },
  { id: 10, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-010", full_name: "Anisa Putri", birth_place: "Balikpapan", birth_date: "2015-05-22", gender: "P", parent_name: "Wahyu Saputra", parent_phone_wa: "087123456789", school_origin: "SD Katolik St. Paulus", grade_level: "SD", class_grade: 5, home_address: "Jl. Letjen Suprapto No. 22", sibling_student_id: null, discount_amount: 0, status: "active", registered_at: "2026-02-14" },
  { id: 11, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-011", full_name: "Kevin Pratama", birth_place: "Balikpapan", birth_date: "2013-02-08", gender: "L", parent_name: "Linda Pratama", parent_phone_wa: "082234567890", school_origin: "SMPN 7 Balikpapan", grade_level: "SMP", class_grade: 8, home_address: "Borneo Paradiso A1/5", sibling_student_id: null, discount_amount: 0, status: "active", registered_at: "2026-03-28" },
  { id: 12, branch_id: 1, learning_program_id: 1, academic_year_id: 2, registration_no: "ARH1-2026-012", full_name: "Zahra Alya", birth_place: "Balikpapan", birth_date: "2019-10-15", gender: "P", parent_name: "Ahmad Fauzi", parent_phone_wa: "085345678901", school_origin: "TK Tunas Harapan", grade_level: "TK", class_grade: 0, home_address: "Jl. Syarifuddin Yoes", sibling_student_id: null, discount_amount: 0, status: "active", registered_at: "2026-06-10" },
];

export const classEnrollments = [
  // Calistung-A (class_id: 1) — 4 siswa
  { id: 1, class_id: 1, student_id: 4, enrollment_status: "active", enrolled_at: "2026-03-10" },
  { id: 2, class_id: 1, student_id: 12, enrollment_status: "active", enrolled_at: "2026-06-10" },
  // SD-A (class_id: 2) — 8 siswa
  { id: 3, class_id: 2, student_id: 1, enrollment_status: "active", enrolled_at: "2026-01-15" },
  { id: 4, class_id: 2, student_id: 5, enrollment_status: "active", enrolled_at: "2026-01-22" },
  { id: 5, class_id: 2, student_id: 10, enrollment_status: "active", enrolled_at: "2026-02-14" },
  // SD-B (class_id: 3) — 5 siswa
  { id: 6, class_id: 3, student_id: 6, enrollment_status: "active", enrolled_at: "2026-04-05" },
  // SD-C (class_id: 4) — 3 siswa
  { id: 7, class_id: 4, student_id: 9, enrollment_status: "active", enrolled_at: "2026-05-01" },
  // SMP-A (class_id: 5) — 7 siswa
  { id: 8, class_id: 5, student_id: 7, enrollment_status: "active", enrolled_at: "2025-12-18" },
  // SMP-B (class_id: 6) — 12 siswa (penuh)
  { id: 9, class_id: 6, student_id: 2, enrollment_status: "active", enrolled_at: "2026-02-03" },
  // SMA-A (class_id: 7) — 6 siswa
  { id: 10, class_id: 7, student_id: 3, enrollment_status: "active", enrolled_at: "2025-11-20" },
  { id: 11, class_id: 7, student_id: 8, enrollment_status: "active", enrolled_at: "2026-01-08" },
  // ENG-A (class_id: 8) — 9 siswa
  { id: 12, class_id: 8, student_id: 11, enrollment_status: "active", enrolled_at: "2026-03-28" },
  // Waiting list example
  { id: 13, class_id: 6, student_id: 7, enrollment_status: "waiting_list", waiting_since: "2026-07-15", enrolled_at: null },
];

// --- GRUP C: KEUANGAN & PEMBAYARAN ---

export const bills = [
  { id: 1, student_id: 1, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 330000, discount_amount: 0, total_amount: 330000, payment_status: "paid", due_date: "2026-07-10" },
  { id: 2, student_id: 2, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 350000, discount_amount: 0, total_amount: 350000, payment_status: "unpaid", due_date: "2026-07-10" },
  { id: 3, student_id: 3, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 380000, discount_amount: 0, total_amount: 380000, payment_status: "overdue", due_date: "2026-07-10" },
  { id: 4, student_id: 4, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 250000, discount_amount: 0, total_amount: 250000, payment_status: "paid", due_date: "2026-07-10" },
  { id: 5, student_id: 5, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 330000, discount_amount: 200000, total_amount: 130000, payment_status: "paid", due_date: "2026-07-10" },
  { id: 6, student_id: 6, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 330000, discount_amount: 0, total_amount: 330000, payment_status: "unpaid", due_date: "2026-07-10" },
  { id: 7, student_id: 7, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 350000, discount_amount: 0, total_amount: 350000, payment_status: "paid", due_date: "2026-07-10" },
  { id: 8, student_id: 8, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 380000, discount_amount: 0, total_amount: 380000, payment_status: "overdue", due_date: "2026-07-10" },
  { id: 9, student_id: 9, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 250000, discount_amount: 200000, total_amount: 50000, payment_status: "paid", due_date: "2026-07-10" },
  { id: 10, student_id: 10, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 330000, discount_amount: 0, total_amount: 330000, payment_status: "paid", due_date: "2026-07-10" },
  { id: 11, student_id: 11, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 350000, discount_amount: 0, total_amount: 350000, payment_status: "unpaid", due_date: "2026-07-10" },
  { id: 12, student_id: 12, academic_year_id: 2, bill_type: "spp_monthly", bill_period: "2026-07", base_amount: 250000, discount_amount: 0, total_amount: 250000, payment_status: "paid", due_date: "2026-07-10" },
];

export const payments = [
  { id: 1, bill_id: 1, verified_by_user_id: 1, receipt_no: "KW-2607-001", amount_paid: 330000, payment_method: "cash", proof_image_url: null, payment_date: "2026-07-05", verified_at: "2026-07-05", notes: null },
  { id: 2, bill_id: 4, verified_by_user_id: 1, receipt_no: "KW-2607-002", amount_paid: 250000, payment_method: "qris", proof_image_url: null, payment_date: "2026-07-01", verified_at: "2026-07-01", notes: null },
  { id: 3, bill_id: 5, verified_by_user_id: 1, receipt_no: "KW-2607-003", amount_paid: 130000, payment_method: "bank_transfer", proof_image_url: "/bukti/tf-005.jpg", payment_date: "2026-07-08", verified_at: "2026-07-08", notes: "Diskon kakak-adik Rp 200.000" },
  { id: 4, bill_id: 7, verified_by_user_id: 1, receipt_no: "KW-2607-004", amount_paid: 350000, payment_method: "cash", proof_image_url: null, payment_date: "2026-07-03", verified_at: "2026-07-03", notes: null },
  { id: 5, bill_id: 9, verified_by_user_id: 1, receipt_no: "KW-2607-005", amount_paid: 50000, payment_method: "cash", proof_image_url: null, payment_date: "2026-07-10", verified_at: "2026-07-10", notes: "Diskon kakak-adik Rp 200.000" },
  { id: 6, bill_id: 10, verified_by_user_id: 1, receipt_no: "KW-2607-006", amount_paid: 330000, payment_method: "qris", proof_image_url: null, payment_date: "2026-07-02", verified_at: "2026-07-02", notes: null },
  { id: 7, bill_id: 12, verified_by_user_id: 1, receipt_no: "KW-2607-007", amount_paid: 250000, payment_method: "cash", proof_image_url: null, payment_date: "2026-07-12", verified_at: "2026-07-12", notes: null },
];

// --- DATA TAMBAHAN FRONTDESK ---

export const pengeluaranData = [
  { id: "P001", kategori: "Listrik", keterangan: "Tagihan PLN Juli 2026", nominal: 850000, tanggal: "2026-07-05", status: "Disetujui" },
  { id: "P002", kategori: "ATK", keterangan: "Beli kertas HVS & spidol whiteboard", nominal: 275000, tanggal: "2026-07-08", status: "Disetujui" },
  { id: "P003", kategori: "Kebersihan", keterangan: "Sabun, pel, sapu, tisu", nominal: 120000, tanggal: "2026-07-10", status: "Disetujui" },
  { id: "P004", kategori: "AC Service", keterangan: "Service AC ruang kelas 1 & 2", nominal: 400000, tanggal: "2026-07-15", status: "Menunggu" },
  { id: "P005", kategori: "Internet", keterangan: "Tagihan WiFi Indihome Juli", nominal: 450000, tanggal: "2026-07-05", status: "Disetujui" },
  { id: "P006", kategori: "Fotokopi", keterangan: "Fotokopi soal Try Out SMP & SMA", nominal: 185000, tanggal: "2026-07-12", status: "Disetujui" },
];

export const chartPendaftaran = [
  { bulan: "Jan", pendaftar: 12 },
  { bulan: "Feb", pendaftar: 8 },
  { bulan: "Mar", pendaftar: 15 },
  { bulan: "Apr", pendaftar: 10 },
  { bulan: "Mei", pendaftar: 6 },
  { bulan: "Jun", pendaftar: 4 },
  { bulan: "Jul", pendaftar: 8 },
];

// --- HELPER: Computed Dashboard Stats ---
export const dashboardStats = {
  siswaAktif: 12,
  pendaftarBulanIni: 8,
  tunggakanSPP: 5,
  kelasAktif: 7,
  totalKelas: 8,
};

// --- ENRICHED VIEWS & ADAPTERS (Selaras dengan 20 Tabel DB) ---

// 1. siswaData (Siswa lengkap dengan info program & tagihan)
export const siswaData = students.map((s) => {
  const prog = learningPrograms.find((p) => p.id === s.learning_program_id);
  const studentBill = bills.find((b) => b.student_id === s.id);
  let statusSPP = "Lunas";
  let tunggakan = 0;
  if (studentBill) {
    if (studentBill.payment_status === "paid") statusSPP = "Lunas";
    else if (studentBill.payment_status === "overdue") {
      statusSPP = "Jatuh Tempo";
      tunggakan = studentBill.total_amount;
    } else {
      statusSPP = "Belum Bayar";
      tunggakan = studentBill.total_amount;
    }
  }
  const sibling = s.sibling_student_id ? students.find(other => other.id === s.sibling_student_id) : null;

  return {
    id: s.id,
    registration_no: s.registration_no,
    nama: s.full_name,
    full_name: s.full_name,
    birth_place: s.birth_place,
    birth_date: s.birth_date,
    tanggalLahir: s.birth_date,
    gender: s.gender,
    sekolah: s.school_origin,
    school_origin: s.school_origin,
    grade_level: s.grade_level,
    class_grade: s.class_grade,
    kelas: s.grade_level === "TK" ? "TK" : `${s.class_grade} ${s.grade_level}`,
    alamat: s.home_address,
    home_address: s.home_address,
    parent_name: s.parent_name,
    noHP: s.parent_phone_wa,
    parent_phone_wa: s.parent_phone_wa,
    program: s.grade_level === "TK" ? "Calistung" : s.grade_level,
    learning_program_id: s.learning_program_id,
    program_name: prog ? prog.program_name : "Reguler",
    status: s.status === "active" ? "Aktif" : s.status === "alumni" ? "Alumni" : "Nonaktif",
    statusSPP,
    tunggakan,
    sibling_student_id: s.sibling_student_id,
    sibling_name: sibling ? sibling.full_name : null,
    discount_amount: s.discount_amount,
    registered_at: s.registered_at,
  };
});

// 2. kelasData (Kelas lengkap dengan jadwal, tentor, ruang, kapasitas)
export const kelasData = classes.map((c) => {
  const schedList = classSchedules.filter((cs) => cs.class_id === c.id);
  const firstSched = schedList[0];
  const mentor = firstSched ? mentors.find((m) => m.id === firstSched.mentor_id) : null;
  const room = firstSched ? classRooms.find((r) => r.id === firstSched.room_id) : null;
  const subject = subjects.find((sb) => sb.id === c.subject_id);

  const dayMap = { monday: "Senin", tuesday: "Selasa", wednesday: "Rabu", thursday: "Kamis", friday: "Jumat", saturday: "Sabtu", sunday: "Minggu" };
  const daysFormatted = schedList.map((cs) => dayMap[cs.day_of_week] || cs.day_of_week).join(", ");
  const timeFormatted = firstSched ? `${firstSched.start_time} - ${firstSched.end_time}` : "-";

  let statusLabel = "Tersedia";
  if (c.current_students >= c.max_students) statusLabel = "Penuh";
  else if (c.current_students >= c.max_students * 0.8) statusLabel = "Hampir Penuh";

  return {
    id: c.id,
    namaKelas: c.class_name,
    class_name: c.class_name,
    subject_id: c.subject_id,
    subject_name: subject ? subject.subject_name : "-",
    grade_level: c.grade_level,
    class_grade: c.class_grade,
    jenjang: c.grade_level,
    ruang: room ? room.room_name : `Ruang ${c.id}`,
    room_id: room ? room.id : 1,
    tentor: mentor ? mentor.full_name : "TBA",
    mentor_id: mentor ? mentor.id : 1,
    jadwal: firstSched ? `${daysFormatted} (${timeFormatted})` : "Belum Dijadwalkan",
    schedules: schedList,
    kapasitasMax: c.max_students,
    max_students: c.max_students,
    terisi: c.current_students,
    current_students: c.current_students,
    status: statusLabel,
    db_status: c.status,
  };
});

// 3. tagihanSPP (Tagihan lengkap dengan pembayaran, status, siswa)
export const tagihanSPP = bills.map((b) => {
  const student = students.find((s) => s.id === b.student_id);
  const payment = payments.find((p) => p.bill_id === b.id);

  let statusLabel = "Lunas";
  if (b.payment_status === "overdue") statusLabel = "Jatuh Tempo";
  else if (b.payment_status === "unpaid") statusLabel = "Belum Bayar";

  const monthNames = {
    "2026-07": "Juli 2026",
    "2026-08": "Agustus 2026",
    "2026-09": "September 2026",
    "2026-10": "Oktober 2026",
  };

  return {
    id: b.id,
    bill_id: b.id,
    student_id: b.student_id,
    namaSiswa: student ? student.full_name : `Siswa #${b.student_id}`,
    grade_level: student ? student.grade_level : "SD",
    class_grade: student ? student.class_grade : 1,
    kelas: student ? (student.grade_level === "TK" ? "TK" : `${student.class_grade} ${student.grade_level}`) : "-",
    program: student ? (student.grade_level === "TK" ? "Calistung" : student.grade_level) : "SD",
    bulan: monthNames[b.bill_period] || b.bill_period,
    bill_period: b.bill_period,
    nominal: b.total_amount,
    base_amount: b.base_amount,
    discount_amount: b.discount_amount,
    status: statusLabel,
    payment_status: b.payment_status,
    noHP: student ? student.parent_phone_wa : "-",
    jatuhTempo: b.due_date,
    metode: payment ? (payment.payment_method === "cash" ? "Tunai" : payment.payment_method === "bank_transfer" ? "Transfer Bank" : "QRIS") : "-",
    payment_id: payment ? payment.id : null,
    receipt_no: payment ? payment.receipt_no : null,
    paid_at: payment ? payment.payment_date : null,
  };
});

