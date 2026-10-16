"use client";
import { useState, useMemo } from "react";
import {
  UserPlus,
  CheckCircle,
  ChevronRight,
  ChevronLeft,
  Printer,
  Tag,
  Percent,
  Users,
  CreditCard,
  Building2,
  Calendar,
  AlertCircle,
  Check,
  Send,
  RotateCcw
} from "lucide-react";
import {
  cabangInfo,
  academicYears,
  learningPrograms,
  feeTariffs,
  discountRules,
  students,
} from "@/data/mockFrontdeskData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";
const steps = ["Data Siswa", "Data Orang Tua & Saudara", "Program & Pembayaran"];
const stepColors = ["#2727E6", "#1EAB55", "#FF6600"];
const stepBgs = ["#ECEAFC", "#B8F0D8", "#FFF0D4"];

const Field = ({ label, required, children, dark, note }) => (
  <div className="space-y-1.5">
    <label className="text-xs font-black uppercase tracking-wider block" style={{ color: dark ? "#94a3b8" : "#475569" }}>
      {label} {required && <span className="text-red-500">*</span>}
    </label>
    {children}
    {note && <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">{note}</p>}
  </div>
);

const inputStyle = (dark) => ({
  backgroundColor: dark ? "#0f172a" : "#ffffff",
  border: `2px solid ${dark ? "#334155" : "#cbd5e1"}`,
  color: dark ? "#f1f5f9" : B,
  borderRadius: 10,
  padding: "10px 14px",
  fontSize: 13,
  width: "100%",
  outline: "none",
  transition: "all 0.2s",
});

const formatRp = (num) =>
  new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", minimumFractionDigits: 0 }).format(num || 0);

export default function PendaftaranPage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const [currentStep, setCurrentStep] = useState(0);
  const [submitted, setSubmitted] = useState(false);
  const [generatedRegNo, setGeneratedRegNo] = useState("");

  // Form State aligned with DB schema (students, learning_programs, fee_tariffs)
  const [formData, setFormData] = useState({
    // Student fields
    fullName: "",
    birthPlace: "Balikpapan",
    birthDate: "",
    gender: "L",
    gradeLevel: "SD",
    classGrade: "4",
    schoolOrigin: "",
    homeAddress: "",

    // Parent fields
    parentName: "",
    relationship: "Ibu",
    parentPhoneWa: "",
    parentJob: "",

    // Sibling Discount fields
    hasSibling: false,
    siblingStudentId: "",

    // Program & Payment
    learningProgramId: 1, // Reguler
    academicYearId: 2, // 2026/2027
    paymentMethod: "cash",
  });

  const set = (field, value) => {
    setFormData((prev) => {
      const next = { ...prev, [field]: value };
      // Auto adjust classGrade when gradeLevel changes
      if (field === "gradeLevel") {
        if (value === "TK") next.classGrade = "0";
        else if (value === "SD" && !["1", "2", "3", "4", "5", "6"].includes(next.classGrade)) next.classGrade = "4";
        else if (value === "SMP" && !["7", "8", "9"].includes(next.classGrade)) next.classGrade = "7";
        else if (value === "SMA" && !["10", "11", "12"].includes(next.classGrade)) next.classGrade = "10";
      }
      return next;
    });
  };

  // Find Sibling Data
  const selectedSibling = useMemo(() => {
    if (!formData.hasSibling || !formData.siblingStudentId) return null;
    return students.find((s) => s.id === parseInt(formData.siblingStudentId));
  }, [formData.hasSibling, formData.siblingStudentId]);

  // Dynamic Fee Calculation from feeTariffs table
  const feeCalculation = useMemo(() => {
    const gradeNum = parseInt(formData.classGrade) || 0;
    const progId = parseInt(formData.learningProgramId) || 1;

    // 1. SPP Tariff lookup
    const matchedSpp = feeTariffs.find((t) => {
      return (
        t.fee_type === "spp_monthly" &&
        t.grade_level === formData.gradeLevel &&
        (t.learning_program_id === progId || progId === 1) &&
        gradeNum >= t.class_grade_start &&
        gradeNum <= t.class_grade_end
      );
    }) || feeTariffs[1]; // fallback SD

    const sppAmount = matchedSpp ? matchedSpp.amount : 330000;

    // 2. Module Fee lookup
    const matchedModul = feeTariffs.find((t) => {
      return (
        t.fee_type === "module_semester" &&
        t.grade_level === formData.gradeLevel &&
        gradeNum >= t.class_grade_start &&
        gradeNum <= t.class_grade_end
      );
    });
    const modulAmount = matchedModul ? matchedModul.amount : 0;

    // 3. Sibling discount
    const siblingDiscount = formData.hasSibling && selectedSibling ? 200000 : 0;

    // Total first month payment
    const totalAwal = Math.max(0, sppAmount + modulAmount - siblingDiscount);

    return {
      sppTariff: matchedSpp,
      sppAmount,
      modulTariff: matchedModul,
      modulAmount,
      siblingDiscount,
      totalAwal,
    };
  }, [formData.gradeLevel, formData.classGrade, formData.learningProgramId, formData.hasSibling, selectedSibling]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const newRegNo = `ARH1-2026-${String(students.length + 1).padStart(3, "0")}`;
    setGeneratedRegNo(newRegNo);
    setSubmitted(true);
  };

  const handleReset = () => {
    setSubmitted(false);
    setCurrentStep(0);
    setFormData({
      fullName: "",
      birthPlace: "Balikpapan",
      birthDate: "",
      gender: "L",
      gradeLevel: "SD",
      classGrade: "4",
      schoolOrigin: "",
      homeAddress: "",
      parentName: "",
      relationship: "Ibu",
      parentPhoneWa: "",
      parentJob: "",
      hasSibling: false,
      siblingStudentId: "",
      learningProgramId: 1,
      academicYearId: 2,
      paymentMethod: "cash",
    });
  };

  // SUCCESS / PROOF MODAL VIEW
  if (submitted) {
    const prog = learningPrograms.find((p) => p.id === parseInt(formData.learningProgramId));
    return (
      <div className="max-w-2xl mx-auto space-y-6 animate-in fade-in duration-300">
        <div
          style={{
            backgroundColor: isDark ? "#1e293b" : "#ffffff",
            border: `3px solid ${B}`,
            boxShadow: "6px 6px 0 0 #111118",
          }}
          className="rounded-2xl p-6 sm:p-8"
        >
          {/* Header Bukti Registrasi */}
          <div className="flex items-center justify-between border-b-2 border-dashed border-slate-300 dark:border-slate-700 pb-5 mb-5">
            <div>
              <span className="px-2.5 py-1 text-[11px] font-black uppercase rounded bg-[#1EAB55] text-white tracking-wide">
                Pendaftaran Berhasil!
              </span>
              <h3 className="font-heading font-black text-2xl mt-2 text-slate-900 dark:text-white">
                Bukti Pendaftaran Siswa Baru
              </h3>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                {cabangInfo.branch_name} ({cabangInfo.address}) • TA 2026/2027
              </p>
            </div>
            <div className="text-right">
              <span className="text-[11px] font-bold text-slate-400 block uppercase">No. Registrasi</span>
              <span className="font-mono font-black text-lg px-2.5 py-1 rounded bg-[#FFD600] text-slate-900 border-2 border-[#111118]">
                {generatedRegNo}
              </span>
            </div>
          </div>

          {/* Rincian Siswa */}
          <div className="grid grid-cols-2 gap-3 text-xs mb-6 bg-slate-50 dark:bg-slate-900/60 p-4 rounded-xl border border-slate-200 dark:border-slate-800">
            <div>
              <span className="text-slate-600 dark:text-slate-300 font-semibold block">Nama Siswa:</span>
              <strong className="text-sm font-black text-slate-900 dark:text-slate-100">{formData.fullName || "-"}</strong>
            </div>
            <div>
              <span className="text-slate-600 dark:text-slate-300 font-semibold block">Jenjang &amp; Kelas:</span>
              <strong className="text-sm font-bold text-slate-900 dark:text-slate-100">
                {formData.gradeLevel === "TK" ? "TK (Calistung)" : `Kelas ${formData.classGrade} ${formData.gradeLevel}`}
              </strong>
            </div>
            <div>
              <span className="text-slate-600 dark:text-slate-300 font-semibold block">Sekolah Asal:</span>
              <span className="text-slate-800 dark:text-slate-200">{formData.schoolOrigin || "-"}</span>
            </div>
            <div>
              <span className="text-slate-600 dark:text-slate-300 font-semibold block">Nama Orang Tua:</span>
              <span className="text-slate-800 dark:text-slate-200">{formData.parentName} ({formData.relationship})</span>
            </div>
            <div>
              <span className="text-slate-600 dark:text-slate-300 font-semibold block">No. WhatsApp Wali:</span>
              <span className="font-mono text-slate-800 dark:text-slate-200">{formData.parentPhoneWa || "-"}</span>
            </div>
            <div>
              <span className="text-slate-600 dark:text-slate-300 font-semibold block">Program Belajar:</span>
              <span className="text-slate-800 dark:text-slate-200 font-semibold">{prog?.program_name || "Reguler"}</span>
            </div>
          </div>

          {/* Rincian Biaya Transaksi Awal */}
          <div className="space-y-2 mb-6">
            <h4 className="text-xs font-black uppercase tracking-wider text-slate-500 dark:text-slate-400">
              Rincian Tagihan Awal (Tabel Bills & Payments)
            </h4>
            <div className="border-2 border-[#111118] rounded-xl overflow-hidden divide-y divide-slate-200 dark:divide-slate-800 text-xs">
              <div className="flex justify-between items-center p-3 bg-white dark:bg-slate-800">
                <div>
                  <div className="font-bold">SPP Bulan Pertama (Juli 2026)</div>
                  <div className="text-[11px] text-slate-400">Tarif otomatis jenjang {formData.gradeLevel}</div>
                </div>
                <div className="font-bold">{formatRp(feeCalculation.sppAmount)}</div>
              </div>

              {feeCalculation.modulAmount > 0 && (
                <div className="flex justify-between items-center p-3 bg-white dark:bg-slate-800">
                  <div>
                    <div className="font-bold">Biaya Modul Belajar (Semester 1)</div>
                    <div className="text-[11px] text-slate-400">Buku panduan bimbel + lembar kerja</div>
                  </div>
                  <div className="font-bold">{formatRp(feeCalculation.modulAmount)}</div>
                </div>
              )}

              {feeCalculation.siblingDiscount > 0 && (
                <div className="flex justify-between items-center p-3 bg-green-50 dark:bg-green-950/40 text-green-700 dark:text-green-300">
                  <div>
                    <div className="font-bold">Potongan Diskon Kakak-Adik</div>
                    <div className="text-[11px]">Saudara kandung: {selectedSibling?.full_name}</div>
                  </div>
                  <div className="font-black">-{formatRp(feeCalculation.siblingDiscount)}</div>
                </div>
              )}

              <div className="flex justify-between items-center p-3 bg-amber-50 dark:bg-amber-950/40 font-black text-sm">
                <div>Total Pembayaran Kasir:</div>
                <div className="text-base text-blue-600 dark:text-blue-400">{formatRp(feeCalculation.totalAwal)}</div>
              </div>
            </div>
          </div>

          <div className="p-3 rounded-lg bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800 text-xs text-blue-800 dark:text-blue-300 flex items-start gap-2 mb-6">
            <CheckCircle size={16} className="shrink-0 mt-0.5 text-blue-600 dark:text-blue-400" />
            <div>
              <strong>Status:</strong> Terdaftar resmi. Tagihan SPP otomatis terbuat untuk bulan Juli 2026. Data siswa langsung dapat diplotkan ke kelas pada menu <strong>Plotting Kelas</strong>.
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex flex-wrap items-center justify-between gap-3 pt-2">
            <button
              onClick={handleReset}
              style={{ border: `2px solid ${B}`, boxShadow: S }}
              className="inline-flex items-center gap-2 px-4 py-2.5 rounded-lg text-xs font-black uppercase tracking-wide bg-white text-slate-800 hover:bg-slate-50 transition-all active:translate-y-0.5"
            >
              <RotateCcw size={14} /> Daftar Siswa Lain
            </button>

            <div className="flex gap-2">
              <button
                onClick={() => {
                  const msg = encodeURIComponent(
                    `Halo Bapak/Ibu ${formData.parentName}, terima kasih telah mendaftarkan ${formData.fullName} di ${cabangInfo.branch_name}. No. Registrasi: ${generatedRegNo}. Total pembayaran: ${formatRp(feeCalculation.totalAwal)}.`
                  );
                  window.open(`https://wa.me/${formData.parentPhoneWa?.replace(/[^0-9]/g, "")}?text=${msg}`, "_blank");
                }}
                style={{ border: `2px solid ${B}`, boxShadow: S }}
                className="inline-flex items-center gap-2 px-4 py-2.5 rounded-lg text-xs font-black uppercase tracking-wide bg-[#1EAB55] text-white hover:opacity-95 transition-all"
              >
                <Send size={14} /> Kirim WA Wali
              </button>
              <button
                onClick={() => window.print()}
                style={{ border: `2px solid ${B}`, boxShadow: S }}
                className="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg text-xs font-black uppercase tracking-wide bg-[#FFD600] text-slate-900 hover:opacity-95 transition-all"
              >
                <Printer size={14} /> Cetak Bukti PDF
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }

  // MAIN MULTI-STEP FORM
  return (
    <div className="max-w-3xl mx-auto space-y-6">
      {/* Header Info */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div>
          <h2 className="font-heading font-black text-2xl flex items-center gap-2.5" style={{ color: isDark ? "#f1f5f9" : B }}>
            <span className="p-2 rounded-xl bg-[#2727E6] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]">
              <UserPlus size={20} />
            </span>
            Pendaftaran Walk-in
          </h2>
          <p className="text-xs sm:text-sm mt-1" style={{ color: isDark ? "#94a3b8" : "#64748b" }}>
            Registrasi siswa baru di kasir cabang • Pengganti buku tulis A4 manual
          </p>
        </div>

        <div className="flex items-center gap-2">
          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300 border border-blue-300 dark:border-blue-800">
            <Building2 size={13} /> {cabangInfo.branch_name}
          </span>
          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 border border-amber-300 dark:border-amber-800">
            <Calendar size={13} /> TA 2026/2027
          </span>
        </div>
      </div>

      {/* Step Indicator */}
      <div className="flex items-center gap-2">
        {steps.map((step, i) => (
          <div key={i} className="flex items-center gap-2 flex-1">
            <button
              type="button"
              onClick={() => setCurrentStep(i)}
              className="flex items-center gap-2 text-left group"
            >
              <div
                style={{
                  backgroundColor: i <= currentStep ? stepColors[i] : isDark ? "#334155" : "#e2e8f0",
                  border: `2px solid ${i <= currentStep ? B : "transparent"}`,
                  boxShadow: i <= currentStep ? "2px 2px 0 0 #111118" : "none",
                  color: i <= currentStep ? "#fff" : isDark ? "#64748b" : "#9ca3af",
                }}
                className="w-8 h-8 rounded-full flex items-center justify-center text-xs font-black shrink-0 transition-all"
              >
                {i < currentStep ? <Check size={14} /> : i + 1}
              </div>
              <span
                className="text-xs font-bold hidden sm:block"
                style={{ color: i <= currentStep ? (isDark ? "#f1f5f9" : B) : isDark ? "#64748b" : "#9ca3af" }}
              >
                {step}
              </span>
            </button>
            {i < steps.length - 1 && (
              <div
                className="flex-1 h-0.5 mx-2"
                style={{ backgroundColor: i < currentStep ? stepColors[i] : isDark ? "#334155" : "#e2e8f0" }}
              />
            )}
          </div>
        ))}
      </div>

      {/* Form Container */}
      <div
        style={{
          backgroundColor: isDark ? "#1e293b" : "#ffffff",
          border: `2px solid ${B}`,
          boxShadow: S,
        }}
        className="rounded-2xl p-6 transition-colors duration-300"
      >
        <div className="flex items-center justify-between mb-6 pb-4 border-b border-slate-200 dark:border-slate-800">
          <div className="flex items-center gap-3">
            <div
              style={{ backgroundColor: stepColors[currentStep], color: "#fff", border: `2px solid ${B}` }}
              className="w-8 h-8 rounded-lg flex items-center justify-center font-black text-sm"
            >
              {currentStep + 1}
            </div>
            <div>
              <h3 className="font-heading font-black text-lg" style={{ color: isDark ? "#f1f5f9" : B }}>
                {steps[currentStep]}
              </h3>
              <p className="text-xs text-slate-500">
                {currentStep === 0 && "Identitas siswa, jenjang kelas, dan asal sekolah"}
                {currentStep === 1 && "Kontak orang tua & verifikasi diskon saudara kandung"}
                {currentStep === 2 && "Pemilihan program & rincian tarif otomatis"}
              </p>
            </div>
          </div>
          <span className="text-xs font-bold px-2.5 py-1 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
            Langkah {currentStep + 1} dari 3
          </span>
        </div>

        <form onSubmit={handleSubmit}>
          {/* STEP 1: DATA SISWA */}
          {currentStep === 0 && (
            <div className="space-y-4">
              <Field label="Nama Lengkap Siswa" required dark={isDark}>
                <input
                  style={inputStyle(isDark)}
                  placeholder="Contoh: Muhammad Kevin Sanjaya"
                  value={formData.fullName}
                  onChange={(e) => set("fullName", e.target.value)}
                  required
                />
              </Field>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <Field label="Tempat Lahir" dark={isDark}>
                  <input
                    style={inputStyle(isDark)}
                    placeholder="Contoh: Balikpapan"
                    value={formData.birthPlace}
                    onChange={(e) => set("birthPlace", e.target.value)}
                  />
                </Field>
                <Field label="Tanggal Lahir" required dark={isDark}>
                  <input
                    type="date"
                    style={inputStyle(isDark)}
                    value={formData.birthDate}
                    onChange={(e) => set("birthDate", e.target.value)}
                    required
                  />
                </Field>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <Field label="Jenis Kelamin" required dark={isDark}>
                  <select
                    style={inputStyle(isDark)}
                    value={formData.gender}
                    onChange={(e) => set("gender", e.target.value)}
                  >
                    <option value="L">Laki-laki</option>
                    <option value="P">Perempuan</option>
                  </select>
                </Field>

                <Field label="Jenjang Pendidikan" required dark={isDark}>
                  <select
                    style={inputStyle(isDark)}
                    value={formData.gradeLevel}
                    onChange={(e) => set("gradeLevel", e.target.value)}
                  >
                    <option value="TK">TK / Calistung</option>
                    <option value="SD">SD (Sekolah Dasar)</option>
                    <option value="SMP">SMP (Sekolah Menengah Pertama)</option>
                    <option value="SMA">SMA (Sekolah Menengah Atas)</option>
                  </select>
                </Field>

                <Field label="Kelas di Sekolah" required dark={isDark}>
                  {formData.gradeLevel === "TK" ? (
                    <input style={inputStyle(isDark)} value="TK (Calistung)" disabled />
                  ) : formData.gradeLevel === "SD" ? (
                    <select
                      style={inputStyle(isDark)}
                      value={formData.classGrade}
                      onChange={(e) => set("classGrade", e.target.value)}
                    >
                      {[1, 2, 3, 4, 5, 6].map((g) => (
                        <option key={g} value={String(g)}>
                          Kelas {g} SD
                        </option>
                      ))}
                    </select>
                  ) : formData.gradeLevel === "SMP" ? (
                    <select
                      style={inputStyle(isDark)}
                      value={formData.classGrade}
                      onChange={(e) => set("classGrade", e.target.value)}
                    >
                      {[7, 8, 9].map((g) => (
                        <option key={g} value={String(g)}>
                          Kelas {g} SMP
                        </option>
                      ))}
                    </select>
                  ) : (
                    <select
                      style={inputStyle(isDark)}
                      value={formData.classGrade}
                      onChange={(e) => set("classGrade", e.target.value)}
                    >
                      {[10, 11, 12].map((g) => (
                        <option key={g} value={String(g)}>
                          Kelas {g} SMA
                        </option>
                      ))}
                    </select>
                  )}
                </Field>
              </div>

              <Field label="Sekolah Asal" dark={isDark}>
                <input
                  style={inputStyle(isDark)}
                  placeholder="Contoh: SDN 004 Balikpapan Selatan"
                  value={formData.schoolOrigin}
                  onChange={(e) => set("schoolOrigin", e.target.value)}
                />
              </Field>

              <Field label="Alamat Domisili Siswa" dark={isDark}>
                <textarea
                  style={{ ...inputStyle(isDark), minHeight: 70 }}
                  placeholder="Contoh: Jl. MT Haryono No. 12, Balikpapan Baru"
                  value={formData.homeAddress}
                  onChange={(e) => set("homeAddress", e.target.value)}
                />
              </Field>
            </div>
          )}

          {/* STEP 2: DATA ORANG TUA & DISKON SAUDARA KANDUNG */}
          {currentStep === 1 && (
            <div className="space-y-4">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <Field label="Nama Orang Tua / Wali" required dark={isDark}>
                  <input
                    style={inputStyle(isDark)}
                    placeholder="Contoh: Ibu Rina Hartati"
                    value={formData.parentName}
                    onChange={(e) => set("parentName", e.target.value)}
                    required
                  />
                </Field>

                <Field label="Hubungan dengan Siswa" required dark={isDark}>
                  <select
                    style={inputStyle(isDark)}
                    value={formData.relationship}
                    onChange={(e) => set("relationship", e.target.value)}
                  >
                    <option value="Ibu">Ibu Kandung</option>
                    <option value="Ayah">Ayah Kandung</option>
                    <option value="Wali">Wali / Keluarga</option>
                  </select>
                </Field>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <Field label="Nomor WhatsApp Wali" required dark={isDark} note="Untuk pengiriman notifikasi kuitansi & pengingat SPP">
                  <input
                    type="tel"
                    style={inputStyle(isDark)}
                    placeholder="Contoh: 081234567890"
                    value={formData.parentPhoneWa}
                    onChange={(e) => set("parentPhoneWa", e.target.value)}
                    required
                  />
                </Field>

                <Field label="Pekerjaan Orang Tua" dark={isDark}>
                  <input
                    style={inputStyle(isDark)}
                    placeholder="Contoh: Karyawan Swasta / Wiraswasta"
                    value={formData.parentJob}
                    onChange={(e) => set("parentJob", e.target.value)}
                  />
                </Field>
              </div>

              {/* FITUR KHUSUS: DISKON KAKAK-ADIK (Sesuai dokumen DISKUSI 1) */}
              <div
                style={{
                  border: `2px solid ${formData.hasSibling ? "#1EAB55" : isDark ? "#334155" : "#e2e8f0"}`,
                  backgroundColor: formData.hasSibling
                    ? isDark
                      ? "#064e3b20"
                      : "#f0fdf4"
                    : isDark
                    ? "#1e293b"
                    : "#f8fafc",
                }}
                className="p-4 rounded-xl space-y-3 transition-colors mt-6"
              >
                <div className="flex items-start justify-between gap-3">
                  <div className="flex items-center gap-2">
                    <input
                      type="checkbox"
                      id="hasSibling"
                      checked={formData.hasSibling}
                      onChange={(e) => set("hasSibling", e.target.checked)}
                      className="w-4 h-4 rounded text-green-600 focus:ring-green-500 cursor-pointer"
                    />
                    <label htmlFor="hasSibling" className="text-xs font-black uppercase tracking-wide cursor-pointer text-slate-800 dark:text-slate-100 flex items-center gap-1.5">
                      <Users size={15} className="text-green-600" />
                      Memiliki Saudara Kandung Les di Bimbel Artha?
                    </label>
                  </div>
                  <span className="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-green-100 text-green-800 dark:bg-green-900/60 dark:text-green-300">
                    Diskon Rp 200.000 / anak
                  </span>
                </div>

                <p className="text-xs text-slate-500 dark:text-slate-400 pl-6">
                  Sesuai aturan operasional: siswa yang memiliki kakak atau adik yang aktif les di Artha berhak mendapatkan potongan SPP <strong>Rp 200.000</strong> setiap tagihan!
                </p>

                {formData.hasSibling && (
                  <div className="pl-6 pt-2 space-y-2">
                    <Field label="Pilih Saudara Kandung yang Terdaftar" dark={isDark}>
                      <select
                        style={inputStyle(isDark)}
                        value={formData.siblingStudentId}
                        onChange={(e) => set("siblingStudentId", e.target.value)}
                      >
                        <option value="">-- Cari Nama Siswa Saudara di Cabang Ini --</option>
                        {students.map((st) => (
                          <option key={st.id} value={st.id}>
                            {st.full_name} ({st.grade_level} Kelas {st.class_grade}) • Wali: {st.parent_name}
                          </option>
                        ))}
                      </select>
                    </Field>

                    {selectedSibling && (
                      <div className="p-3 rounded-lg bg-green-100 dark:bg-green-950/60 border border-green-300 dark:border-green-800 text-xs text-green-800 dark:text-green-200 flex items-center gap-2">
                        <Percent size={16} className="text-green-600 shrink-0" />
                        <div>
                          <strong>Terverifikasi:</strong> Saudara kandung ditemukan atas nama{" "}
                          <strong>{selectedSibling.full_name}</strong> (No. Reg: {selectedSibling.registration_no}).
                          Potongan <strong>Rp 200.000</strong> akan otomatis dikurangkan dari SPP!
                        </div>
                      </div>
                    )}
                  </div>
                )}
              </div>
            </div>
          )}

          {/* STEP 3: PROGRAM BELAJAR & TARIF BIAYA */}
          {currentStep === 2 && (
            <div className="space-y-6">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <Field label="Program Belajar" required dark={isDark}>
                  <select
                    style={inputStyle(isDark)}
                    value={formData.learningProgramId}
                    onChange={(e) => set("learningProgramId", e.target.value)}
                  >
                    {learningPrograms.map((prog) => (
                      <option key={prog.id} value={prog.id}>
                        {prog.program_name} - {prog.description}
                      </option>
                    ))}
                  </select>
                </Field>

                <Field label="Metode Pembayaran Pendaftaran" required dark={isDark}>
                  <select
                    style={inputStyle(isDark)}
                    value={formData.paymentMethod}
                    onChange={(e) => set("paymentMethod", e.target.value)}
                  >
                    <option value="cash">Tunai di Frontdesk</option>
                    <option value="bank_transfer">Transfer Bank BCA (Pusat)</option>
                    <option value="qris">QRIS Bimbel Artha</option>
                  </select>
                </Field>
              </div>

              {/* RINCIAN TARIF OTOMATIS */}
              <div
                style={{
                  border: `2px solid ${B}`,
                  boxShadow: "3px 3px 0 0 #111118",
                  backgroundColor: isDark ? "#0f172a" : "#fff",
                }}
                className="rounded-xl p-4 sm:p-5 space-y-4"
              >
                <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
                  <div className="flex items-center gap-2">
                    <CreditCard size={18} className="text-[#2727E6]" />
                    <h4 className="font-heading font-black text-sm text-slate-900 dark:text-slate-100 uppercase tracking-wide">
                      Kalkulasi Biaya Otomatis (Tarif Resmi)
                    </h4>
                  </div>
                  <span className="text-[11px] font-bold text-slate-400">
                    Jenjang: {formData.gradeLevel} (Kelas {formData.classGrade})
                  </span>
                </div>

                <div className="space-y-2 text-xs">
                  <div className="flex justify-between items-center py-1.5 border-b border-dashed border-slate-200 dark:border-slate-800">
                    <span className="text-slate-600 dark:text-slate-400">
                      Biaya SPP Bulanan ({feeCalculation.sppTariff?.description || "Reguler"})
                    </span>
                    <span className="font-bold text-slate-900 dark:text-slate-100">
                      {formatRp(feeCalculation.sppAmount)}
                    </span>
                  </div>

                  {feeCalculation.modulAmount > 0 && (
                    <div className="flex justify-between items-center py-1.5 border-b border-dashed border-slate-200 dark:border-slate-800">
                      <span className="text-slate-600 dark:text-slate-400">
                        Biaya Modul Belajar (1 Semester)
                      </span>
                      <span className="font-bold text-slate-900 dark:text-slate-100">
                        {formatRp(feeCalculation.modulAmount)}
                      </span>
                    </div>
                  )}

                  {feeCalculation.siblingDiscount > 0 ? (
                    <div className="flex justify-between items-center py-1.5 border-b border-dashed border-slate-200 dark:border-slate-800 text-green-600 dark:text-green-400">
                      <span className="font-bold">Potongan Diskon Saudara Kandung</span>
                      <span className="font-black">-{formatRp(feeCalculation.siblingDiscount)}</span>
                    </div>
                  ) : (
                    <div className="flex justify-between items-center py-1.5 border-b border-dashed border-slate-200 dark:border-slate-800 text-slate-400">
                      <span>Diskon Saudara Kandung</span>
                      <span>Tidak diterapkan</span>
                    </div>
                  )}

                  <div className="flex justify-between items-center pt-2 text-sm font-black text-slate-900 dark:text-white">
                    <span>Total Yang Harus Dibayar Hari Ini:</span>
                    <span className="text-base text-[#2727E6] dark:text-[#60a5fa]">
                      {formatRp(feeCalculation.totalAwal)}
                    </span>
                  </div>
                </div>

                {formData.paymentMethod === "bank_transfer" && (
                  <div className="p-3 rounded-lg bg-slate-100 dark:bg-slate-800/80 text-[11px] space-y-1">
                    <div className="font-bold text-slate-700 dark:text-slate-200">Rekening Resmi Bimbel Artha:</div>
                    <div className="font-mono text-slate-900 dark:text-slate-100 font-bold">BCA: 024-9988-771 a/n Bimbel Artha Mandiri</div>
                    <div className="text-slate-500">Kuitansi akan divalidasi setelah mutasi dicek oleh admin/bendahara.</div>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* Form Actions */}
          <div className="flex items-center justify-between pt-6 border-t border-slate-200 dark:border-slate-800 mt-6">
            <button
              type="button"
              onClick={() => setCurrentStep((prev) => Math.max(0, prev - 1))}
              disabled={currentStep === 0}
              style={{
                backgroundColor: isDark ? "#334155" : "#f1f5f9",
                color: isDark ? "#f1f5f9" : B,
                border: `2px solid ${currentStep === 0 ? "transparent" : B}`,
                opacity: currentStep === 0 ? 0.3 : 1,
              }}
              className="inline-flex items-center gap-1.5 text-xs font-black uppercase tracking-wide px-4 py-2.5 rounded-lg transition-all"
            >
              <ChevronLeft size={14} /> Sebelumnya
            </button>

            {currentStep < 2 ? (
              <button
                type="button"
                onClick={() => {
                  if (currentStep === 0 && !formData.fullName) {
                    alert("Mohon isi Nama Lengkap Siswa terlebih dahulu.");
                    return;
                  }
                  if (currentStep === 1 && !formData.parentName) {
                    alert("Mohon isi Nama Orang Tua/Wali terlebih dahulu.");
                    return;
                  }
                  setCurrentStep((prev) => Math.min(2, prev + 1));
                }}
                style={{
                  backgroundColor: stepColors[currentStep],
                  color: "#fff",
                  border: `2px solid ${B}`,
                  boxShadow: S,
                }}
                className="inline-flex items-center gap-1.5 text-xs font-black uppercase tracking-wide px-5 py-2.5 rounded-lg hover:translate-y-px hover:shadow-none transition-all"
              >
                Selanjutnya <ChevronRight size={14} />
              </button>
            ) : (
              <button
                type="submit"
                style={{
                  backgroundColor: "#1EAB55",
                  color: "#fff",
                  border: `2px solid ${B}`,
                  boxShadow: S,
                }}
                className="inline-flex items-center gap-2 text-xs font-black uppercase tracking-wide px-6 py-2.5 rounded-lg hover:translate-y-px hover:shadow-none transition-all"
              >
                <CheckCircle size={15} /> Simpan & Buat Pendaftaran
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
}
