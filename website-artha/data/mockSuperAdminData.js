// ============================================
// DATA MOCK SUPER ADMIN / MANAJEMEN PUSAT
// Monitoring 8 Cabang Bimbel Artha
// ============================================

export const allBranches = [
  { id: 1, branch_name: "Artha 1", address: "Balikpapan Baru, J-2 No. 7", phone_wa: "081234567890", google_maps_url: "https://maps.google.com/?q=-1.2379,116.8529", total_rooms: 5, is_active: true, label: "Pusat" },
  { id: 2, branch_name: "Artha 2", address: "Jl. Soekarno Hatta KM 2", phone_wa: "081234567891", google_maps_url: "https://maps.google.com/?q=-1.2543,116.8612", total_rooms: 4, is_active: true, label: "" },
  { id: 3, branch_name: "Artha 3", address: "Jl. MT Haryono No. 18", phone_wa: "081234567892", google_maps_url: "https://maps.google.com/?q=-1.2401,116.8498", total_rooms: 3, is_active: true, label: "" },
  { id: 4, branch_name: "Artha 4", address: "Perum Borneo Paradiso B2/5", phone_wa: "081234567893", google_maps_url: "https://maps.google.com/?q=-1.2290,116.8750", total_rooms: 4, is_active: true, label: "" },
  { id: 5, branch_name: "Artha 5", address: "Jl. Ruhui Rahayu Blok A1", phone_wa: "081234567894", google_maps_url: "https://maps.google.com/?q=-1.2615,116.8430", total_rooms: 3, is_active: true, label: "" },
  { id: 6, branch_name: "Artha 6", address: "Jl. Letjen Suprapto No. 45", phone_wa: "081234567895", google_maps_url: "https://maps.google.com/?q=-1.2688,116.8580", total_rooms: 3, is_active: true, label: "" },
  { id: 7, branch_name: "Artha 7", address: "Perum Graha Indah D5/12", phone_wa: "081234567896", google_maps_url: "https://maps.google.com/?q=-1.2320,116.8920", total_rooms: 4, is_active: true, label: "" },
  { id: 8, branch_name: "Artha 8", address: "Jl. Syarifuddin Yoes KM 5", phone_wa: "081234567897", google_maps_url: "https://maps.google.com/?q=-1.2450,116.9010", total_rooms: 3, is_active: true, label: "" },
];

export const allUsers = [
  { id: 1, branch_id: null, name: "Ibu Emi Ratnawati", email: "emi@bimbelartha.id", role: "super_admin", is_active: true, last_login_at: "2026-10-08 09:15:00" },
  { id: 2, branch_id: null, name: "Om Tok (Miskam Yudianto)", email: "omtok@bimbelartha.id", role: "super_admin", is_active: true, last_login_at: "2026-10-07 14:30:00" },
  { id: 3, branch_id: null, name: "Pak Subagio", email: "subagio@bimbelartha.id", role: "super_admin", is_active: true, last_login_at: "2026-10-06 10:00:00" },
  { id: 4, branch_id: 1, name: "Siti Rahmawati", email: "siti@bimbelartha.id", role: "branch_admin", is_active: true, last_login_at: "2026-10-08 08:00:00" },
  { id: 5, branch_id: 2, name: "Andi Firmansyah", email: "andi@bimbelartha.id", role: "branch_admin", is_active: true, last_login_at: "2026-10-08 07:45:00" },
  { id: 6, branch_id: 3, name: "Rina Susanti", email: "rina@bimbelartha.id", role: "branch_admin", is_active: true, last_login_at: "2026-10-07 08:10:00" },
  { id: 7, branch_id: 4, name: "Budi Hartono", email: "budi@bimbelartha.id", role: "branch_admin", is_active: true, last_login_at: "2026-10-08 08:30:00" },
  { id: 8, branch_id: 5, name: "Wulan Sari", email: "wulan@bimbelartha.id", role: "branch_admin", is_active: true, last_login_at: "2026-10-07 12:15:00" },
  { id: 9, branch_id: 6, name: "Dian Permata", email: "dian@bimbelartha.id", role: "branch_admin", is_active: true, last_login_at: "2026-10-08 09:00:00" },
  { id: 10, branch_id: 7, name: "Faisal Rahman", email: "faisal@bimbelartha.id", role: "branch_admin", is_active: true, last_login_at: "2026-10-06 16:00:00" },
  { id: 11, branch_id: 8, name: "Maya Anggraini", email: "maya@bimbelartha.id", role: "branch_admin", is_active: false, last_login_at: "2026-09-15 11:00:00" },
];

// --- Per-Branch Summary Stats ---
export const branchSummaries = [
  { branch_id: 1, branch_name: "Artha 1", siswa_aktif: 47, siswa_sd: 22, siswa_smp: 13, siswa_sma: 8, siswa_tk: 4, pendaftar_baru: 8, tunggakan: 5, revenue_bulan_ini: 14500000, target_revenue: 16000000, kelas_aktif: 8, total_kelas: 8, total_tentor: 7 },
  { branch_id: 2, branch_name: "Artha 2", siswa_aktif: 38, siswa_sd: 18, siswa_smp: 11, siswa_sma: 6, siswa_tk: 3, pendaftar_baru: 5, tunggakan: 3, revenue_bulan_ini: 11800000, target_revenue: 13000000, kelas_aktif: 6, total_kelas: 7, total_tentor: 5 },
  { branch_id: 3, branch_name: "Artha 3", siswa_aktif: 32, siswa_sd: 15, siswa_smp: 10, siswa_sma: 4, siswa_tk: 3, pendaftar_baru: 4, tunggakan: 4, revenue_bulan_ini: 9600000, target_revenue: 11000000, kelas_aktif: 5, total_kelas: 6, total_tentor: 4 },
  { branch_id: 4, branch_name: "Artha 4", siswa_aktif: 41, siswa_sd: 20, siswa_smp: 12, siswa_sma: 5, siswa_tk: 4, pendaftar_baru: 6, tunggakan: 2, revenue_bulan_ini: 13200000, target_revenue: 14000000, kelas_aktif: 7, total_kelas: 7, total_tentor: 6 },
  { branch_id: 5, branch_name: "Artha 5", siswa_aktif: 28, siswa_sd: 14, siswa_smp: 8, siswa_sma: 4, siswa_tk: 2, pendaftar_baru: 3, tunggakan: 6, revenue_bulan_ini: 8200000, target_revenue: 9500000, kelas_aktif: 5, total_kelas: 6, total_tentor: 4 },
  { branch_id: 6, branch_name: "Artha 6", siswa_aktif: 35, siswa_sd: 16, siswa_smp: 11, siswa_sma: 5, siswa_tk: 3, pendaftar_baru: 7, tunggakan: 3, revenue_bulan_ini: 10900000, target_revenue: 12000000, kelas_aktif: 6, total_kelas: 6, total_tentor: 5 },
  { branch_id: 7, branch_name: "Artha 7", siswa_aktif: 44, siswa_sd: 21, siswa_smp: 13, siswa_sma: 7, siswa_tk: 3, pendaftar_baru: 9, tunggakan: 4, revenue_bulan_ini: 14100000, target_revenue: 15000000, kelas_aktif: 7, total_kelas: 8, total_tentor: 6 },
  { branch_id: 8, branch_name: "Artha 8", siswa_aktif: 25, siswa_sd: 12, siswa_smp: 7, siswa_sma: 4, siswa_tk: 2, pendaftar_baru: 2, tunggakan: 5, revenue_bulan_ini: 7500000, target_revenue: 8500000, kelas_aktif: 4, total_kelas: 5, total_tentor: 3 },
];

// --- Revenue Trend (Monthly) ---
export const revenueTrend = [
  { bulan: "Jul", artha1: 14500000, artha2: 11800000, artha3: 9600000, artha4: 13200000, artha5: 8200000, artha6: 10900000, artha7: 14100000, artha8: 7500000, total: 89800000 },
  { bulan: "Aug", artha1: 15200000, artha2: 12100000, artha3: 10200000, artha4: 13500000, artha5: 8800000, artha6: 11200000, artha7: 14800000, artha8: 7900000, total: 93700000 },
  { bulan: "Sep", artha1: 14800000, artha2: 11500000, artha3: 9900000, artha4: 13800000, artha5: 8500000, artha6: 11500000, artha7: 14300000, artha8: 7200000, total: 91500000 },
  { bulan: "Oct", artha1: 15500000, artha2: 12500000, artha3: 10500000, artha4: 14000000, artha5: 9000000, artha6: 11800000, artha7: 15000000, artha8: 8200000, total: 96500000 },
];

// --- Revenue Validations ---
export const revenueValidations = [
  { id: 1, branch_id: 1, period_month: "2026-07", expected_revenue: 16000000, actual_revenue: 14500000, validated_by_user_id: 3, validation_status: "validated", notes: "Sudah dicocokkan dengan rekening BCA pusat", validated_at: "2026-08-05" },
  { id: 2, branch_id: 2, period_month: "2026-07", expected_revenue: 13000000, actual_revenue: 11800000, validated_by_user_id: 3, validation_status: "validated", notes: null, validated_at: "2026-08-05" },
  { id: 3, branch_id: 3, period_month: "2026-07", expected_revenue: 11000000, actual_revenue: 9600000, validated_by_user_id: null, validation_status: "pending", notes: null, validated_at: null },
  { id: 4, branch_id: 4, period_month: "2026-07", expected_revenue: 14000000, actual_revenue: 13200000, validated_by_user_id: 3, validation_status: "validated", notes: null, validated_at: "2026-08-06" },
  { id: 5, branch_id: 5, period_month: "2026-07", expected_revenue: 9500000, actual_revenue: 8200000, validated_by_user_id: null, validation_status: "discrepancy", notes: "Selisih Rp 1.300.000 — perlu pengecekan ulang", validated_at: null },
  { id: 6, branch_id: 6, period_month: "2026-07", expected_revenue: 12000000, actual_revenue: 10900000, validated_by_user_id: 3, validation_status: "validated", notes: null, validated_at: "2026-08-06" },
  { id: 7, branch_id: 7, period_month: "2026-07", expected_revenue: 15000000, actual_revenue: 14100000, validated_by_user_id: null, validation_status: "pending", notes: null, validated_at: null },
  { id: 8, branch_id: 8, period_month: "2026-07", expected_revenue: 8500000, actual_revenue: 7500000, validated_by_user_id: null, validation_status: "pending", notes: null, validated_at: null },
];

// --- All Mentors (Across Branches) ---
export const allMentors = [
  // Artha 1
  { id: 1, branch_id: 1, full_name: "Om Imam", phone_wa: "081111111101", is_active: true, total_classes: 4, total_hours_weekly: 18, branches_taught: ["Artha 1"] },
  { id: 2, branch_id: 1, full_name: "Tante Slamet", phone_wa: "081111111102", is_active: true, total_classes: 1, total_hours_weekly: 4.5, branches_taught: ["Artha 1"] },
  { id: 3, branch_id: 1, full_name: "Tante Novia", phone_wa: "081111111103", is_active: true, total_classes: 1, total_hours_weekly: 4.5, branches_taught: ["Artha 1"] },
  { id: 4, branch_id: 1, full_name: "Tante Sulis", phone_wa: "081111111104", is_active: true, total_classes: 1, total_hours_weekly: 4.5, branches_taught: ["Artha 1"] },
  { id: 5, branch_id: 1, full_name: "Tante Zulfa", phone_wa: "081111111105", is_active: true, total_classes: 1, total_hours_weekly: 4.5, branches_taught: ["Artha 1"] },
  { id: 6, branch_id: 1, full_name: "Om Arman", phone_wa: "081111111106", is_active: true, total_classes: 1, total_hours_weekly: 4.5, branches_taught: ["Artha 1"] },
  { id: 7, branch_id: 1, full_name: "Tante Dewi", phone_wa: "081111111107", is_active: true, total_classes: 0, total_hours_weekly: 0, branches_taught: ["Artha 1"] },
  // Artha 2
  { id: 8, branch_id: 2, full_name: "Om Rudi", phone_wa: "081222222201", is_active: true, total_classes: 3, total_hours_weekly: 13.5, branches_taught: ["Artha 2"] },
  { id: 9, branch_id: 2, full_name: "Tante Lisa", phone_wa: "081222222202", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 2"] },
  { id: 10, branch_id: 2, full_name: "Om Dani", phone_wa: "081222222203", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 2", "Artha 3"] },
  { id: 11, branch_id: 2, full_name: "Tante Mega", phone_wa: "081222222204", is_active: true, total_classes: 1, total_hours_weekly: 4.5, branches_taught: ["Artha 2"] },
  { id: 12, branch_id: 2, full_name: "Om Fajar", phone_wa: "081222222205", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 2"] },
  // Artha 3
  { id: 13, branch_id: 3, full_name: "Tante Wati", phone_wa: "081333333301", is_active: true, total_classes: 3, total_hours_weekly: 13.5, branches_taught: ["Artha 3"] },
  { id: 14, branch_id: 3, full_name: "Om Hasan", phone_wa: "081333333302", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 3"] },
  { id: 15, branch_id: 3, full_name: "Tante Yuni", phone_wa: "081333333303", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 3"] },
  { id: 16, branch_id: 3, full_name: "Om Agung", phone_wa: "081333333304", is_active: true, total_classes: 1, total_hours_weekly: 4.5, branches_taught: ["Artha 3"] },
  // Artha 4-8 (simplified)
  { id: 17, branch_id: 4, full_name: "Om Rizal", phone_wa: "081444444401", is_active: true, total_classes: 4, total_hours_weekly: 18, branches_taught: ["Artha 4"] },
  { id: 18, branch_id: 4, full_name: "Tante Ani", phone_wa: "081444444402", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 4"] },
  { id: 19, branch_id: 4, full_name: "Om Joko", phone_wa: "081444444403", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 4"] },
  { id: 20, branch_id: 5, full_name: "Tante Ika", phone_wa: "081555555501", is_active: true, total_classes: 3, total_hours_weekly: 13.5, branches_taught: ["Artha 5"] },
  { id: 21, branch_id: 5, full_name: "Om Bayu", phone_wa: "081555555502", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 5"] },
  { id: 22, branch_id: 6, full_name: "Tante Fitri", phone_wa: "081666666601", is_active: true, total_classes: 3, total_hours_weekly: 13.5, branches_taught: ["Artha 6"] },
  { id: 23, branch_id: 6, full_name: "Om Wahyu", phone_wa: "081666666602", is_active: true, total_classes: 3, total_hours_weekly: 13.5, branches_taught: ["Artha 6"] },
  { id: 24, branch_id: 7, full_name: "Om Surya", phone_wa: "081777777701", is_active: true, total_classes: 4, total_hours_weekly: 18, branches_taught: ["Artha 7"] },
  { id: 25, branch_id: 7, full_name: "Tante Nia", phone_wa: "081777777702", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 7"] },
  { id: 26, branch_id: 7, full_name: "Om Feri", phone_wa: "081777777703", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 7"] },
  { id: 27, branch_id: 8, full_name: "Tante Putri", phone_wa: "081888888801", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 8"] },
  { id: 28, branch_id: 8, full_name: "Om Amir", phone_wa: "081888888802", is_active: true, total_classes: 2, total_hours_weekly: 9, branches_taught: ["Artha 8"] },
];

// --- WA Templates ---
export const waTemplates = [
  { id: 1, template_name: "Reminder SPP H-7", template_type: "spp_h7", message_body: "Assalamualaikum Bapak/Ibu {parent_name}, ini pesan dari Bimbel Artha {branch_name}. Kami ingatkan bahwa SPP {student_name} untuk bulan {bill_period} sebesar {total_amount} akan jatuh tempo pada {due_date}. Terima kasih 🙏", is_active: true },
  { id: 2, template_name: "Reminder SPP H-1", template_type: "spp_h1", message_body: "Assalamualaikum Bapak/Ibu {parent_name}, besok adalah tenggat pembayaran SPP {student_name} bulan {bill_period} sebesar {total_amount}. Mohon segera melakukan pembayaran. Terima kasih 🙏", is_active: true },
  { id: 3, template_name: "Tagihan Terlambat H+3", template_type: "overdue_h3", message_body: "Assalamualaikum Bapak/Ibu {parent_name}, SPP {student_name} bulan {bill_period} sebesar {total_amount} sudah melewati tenggat. Mohon segera melunasi agar proses belajar tidak terganggu. Info: {branch_phone}. Terima kasih 🙏", is_active: true },
];

// --- Super Admin KPI Summary ---
export const superAdminKPI = {
  totalSiswaAktif: 290,
  totalRevenueBulanIni: 89800000,
  cabangTerbaik: "Artha 1",
  totalTunggakan: 32,
  totalTentor: 28,
  totalCabangAktif: 8,
};
