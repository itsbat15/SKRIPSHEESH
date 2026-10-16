"use client";
import { useState, useMemo, useEffect } from "react";
import {
  Users,
  Search,
  Download,
  Eye,
  Filter,
  CheckCircle,
  AlertCircle,
  Clock,
  Phone,
  Home,
  GraduationCap,
  Tag,
  Calendar,
  X,
  CreditCard,
  Building2,
  BookOpen
} from "lucide-react";
import {
  students,
  bills,
  payments,
  classes,
  classEnrollments,
  learningPrograms,
  cabangInfo
} from "@/data/mockFrontdeskData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";

const formatRp = (n) =>
  new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", minimumFractionDigits: 0 }).format(n || 0);

export default function SiswaPage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const [search, setSearch] = useState("");
  const [filterJenjang, setFilterJenjang] = useState("all");
  const [filterStatusSiswa, setFilterStatusSiswa] = useState("all");
  const [filterStatusSPP, setFilterStatusSPP] = useState("all");
  const [selectedStudentDetail, setSelectedStudentDetail] = useState(null);

  // Close modal on Escape key press
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") {
        setSelectedStudentDetail(null);
      }
    };
    if (selectedStudentDetail) {
      window.addEventListener("keydown", handleKeyDown);
      return () => window.removeEventListener("keydown", handleKeyDown);
    }
  }, [selectedStudentDetail]);

  // Enriched Student Data
  const enrichedStudents = useMemo(() => {
    return students.map((s) => {
      const studentBill = bills.find((b) => b.student_id === s.id);
      const studentPayment = studentBill ? payments.find((p) => p.bill_id === studentBill.id) : null;
      const sibling = s.sibling_student_id ? students.find((other) => other.id === s.sibling_student_id) : null;
      const prog = learningPrograms.find((lp) => lp.id === s.learning_program_id);

      // Classes student is enrolled in
      const enrolls = classEnrollments.filter((ce) => ce.student_id === s.id && ce.enrollment_status === "active");
      const enrolledClasses = enrolls.map((ce) => classes.find((c) => c.id === ce.class_id)).filter(Boolean);

      let sppStatus = "paid";
      if (studentBill) {
        sppStatus = studentBill.payment_status;
      }

      return {
        ...s,
        program_name: prog ? prog.program_name : "Reguler",
        bill: studentBill,
        payment: studentPayment,
        sibling,
        sppStatus,
        enrolledClasses,
      };
    });
  }, []);

  // Filtered Students
  const filtered = useMemo(() => {
    return enrichedStudents.filter((s) => {
      if (filterJenjang !== "all" && s.grade_level !== filterJenjang) return false;
      if (filterStatusSiswa !== "all" && s.status !== filterStatusSiswa) return false;
      if (filterStatusSPP !== "all" && s.sppStatus !== filterStatusSPP) return false;

      if (search) {
        const q = search.toLowerCase();
        const name = s.full_name.toLowerCase();
        const reg = s.registration_no.toLowerCase();
        const parent = (s.parent_name || "").toLowerCase();
        const school = (s.school_origin || "").toLowerCase();
        if (!name.includes(q) && !reg.includes(q) && !parent.includes(q) && !school.includes(q)) {
          return false;
        }
      }

      return true;
    });
  }, [enrichedStudents, filterJenjang, filterStatusSiswa, filterStatusSPP, search]);

  // KPIs
  const totalSiswa = enrichedStudents.length;
  const siswaAktif = enrichedStudents.filter((s) => s.status === "active").length;
  const siswaTunggakan = enrichedStudents.filter((s) => s.sppStatus !== "paid").length;
  const siswaDiskon = enrichedStudents.filter((s) => s.discount_amount > 0).length;

  const exportCSV = () => {
    const headers = ["No. Reg", "Nama Siswa", "Jenjang", "Kelas", "Sekolah Asal", "Orang Tua", "No WA", "Status SPP"];
    const rows = filtered.map((s) => [
      s.registration_no,
      s.full_name,
      s.grade_level,
      s.class_grade,
      s.school_origin,
      s.parent_name,
      s.parent_phone_wa,
      s.sppStatus,
    ]);
    const csvContent = "data:text/csv;charset=utf-8," + [headers.join(","), ...rows.map((e) => e.join(","))].join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `data_siswa_${cabangInfo.branch_name}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div>
          <h2 className="font-heading font-black text-2xl flex items-center gap-2.5" style={{ color: isDark ? "#f1f5f9" : B }}>
            <span className="p-2 rounded-xl bg-[#2727E6] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]">
              <Users size={20} />
            </span>
            Data Induk Siswa
          </h2>
          <p className="text-xs sm:text-sm mt-1" style={{ color: isDark ? "#94a3b8" : "#64748b" }}>
            Buku induk siswa cabang {cabangInfo.branch_name} • Sinkronisasi 20 tabel basis data
          </p>
        </div>

        <button
          onClick={exportCSV}
          style={{ border: `2px solid ${B}`, boxShadow: S }}
          className="inline-flex items-center gap-2 text-xs font-black uppercase tracking-wide px-4 py-2.5 rounded-lg bg-[#2727E6] text-white hover:opacity-95 transition-all"
        >
          <Download size={14} /> Ekspor Data Siswa (CSV)
        </button>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#2727E6", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-blue-200">Total Terdaftar</p>
          <p className="font-heading font-black text-3xl">{totalSiswa}</p>
          <p className="text-[11px] text-blue-100 mt-1">Siswa di Cabang Artha 1</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#1EAB55", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-emerald-200">Siswa Aktif</p>
          <p className="font-heading font-black text-3xl">{siswaAktif}</p>
          <p className="text-[11px] text-emerald-100 mt-1">Status belajar aktif</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#E11D48", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-rose-200">Menunggak SPP</p>
          <p className="font-heading font-black text-3xl">{siswaTunggakan}</p>
          <p className="text-[11px] text-rose-100 mt-1">Perlu pengingat WA</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#FFD600", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-xl p-4 text-slate-900"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-slate-800">Diskon Kakak-Adik</p>
          <p className="font-heading font-black text-3xl">{siswaDiskon}</p>
          <p className="text-[11px] text-slate-700 mt-1">Penerima potongan Rp 200rb</p>
        </div>
      </div>

      {/* Filter and Search Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 bg-white dark:bg-slate-900 p-3.5 rounded-xl border-2 border-[#111118]">
        <div className="relative flex-1 min-w-[240px]">
          <Search size={15} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 dark:text-slate-400" />
          <input
            type="text"
            placeholder="Cari nama siswa, nomor reg, orang tua, sekolah..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full pl-9 pr-3 py-2 rounded-lg text-xs font-medium border-2 border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 outline-none"
          />
        </div>

        <div className="flex items-center gap-2 flex-wrap">
          <select
            value={filterJenjang}
            onChange={(e) => setFilterJenjang(e.target.value)}
            className="text-xs font-bold p-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 outline-none"
          >
            <option value="all">Semua Jenjang</option>
            <option value="TK">TK</option>
            <option value="SD">SD</option>
            <option value="SMP">SMP</option>
            <option value="SMA">SMA</option>
          </select>

          <select
            value={filterStatusSPP}
            onChange={(e) => setFilterStatusSPP(e.target.value)}
            className="text-xs font-bold p-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 outline-none"
          >
            <option value="all">Status SPP</option>
            <option value="paid">Lunas</option>
            <option value="unpaid">Belum Bayar</option>
            <option value="overdue">Jatuh Tempo</option>
          </select>

          <select
            value={filterStatusSiswa}
            onChange={(e) => setFilterStatusSiswa(e.target.value)}
            className="text-xs font-bold p-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 outline-none"
          >
            <option value="all">Status Siswa</option>
            <option value="active">Aktif</option>
            <option value="alumni">Alumni</option>
            <option value="inactive">Nonaktif</option>
          </select>
        </div>
      </div>

      {/* Table Siswa */}
      <div
        style={{
          backgroundColor: isDark ? "#1e293b" : "#ffffff",
          border: `2px solid ${B}`,
          boxShadow: S,
        }}
        className="rounded-xl overflow-hidden"
      >
        <div className="p-4 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
          <h3 className="font-heading font-black text-base text-slate-900 dark:text-slate-100">
            Daftar Siswa Terdaftar ({filtered.length} siswa)
          </h3>
          <span className="text-xs text-slate-500 font-bold">Cabang: Artha 1</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              <tr className="bg-[#111118] text-white/80">
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">No. Registrasi</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Nama Lengkap &amp; Gender</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Jenjang &amp; Kelas</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Sekolah Asal</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Orang Tua / Kontak</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Status Diskon</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Status SPP</th>
                <th className="text-center px-4 py-3 font-black uppercase tracking-wider">Aksi</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200 dark:divide-slate-800">
              {filtered.length === 0 ? (
                <tr>
                  <td colSpan={8} className="p-8 text-center bg-white dark:bg-slate-900">
                    <div className="max-w-xs mx-auto space-y-2">
                      <p className="text-sm font-bold text-slate-800 dark:text-slate-200">Tidak ada siswa ditemukan</p>
                      <p className="text-xs text-slate-500">Coba ubah kata kunci pencarian atau sesuaikan filter jenjang dan status.</p>
                      <button
                        onClick={() => {
                          setSearch("");
                          setFilterJenjang("all");
                          setFilterStatusSiswa("all");
                          setFilterStatusSPP("all");
                        }}
                        className="text-xs font-bold text-[#2727E6] dark:text-blue-400 underline hover:no-underline"
                      >
                        Reset Semua Filter
                      </button>
                    </div>
                  </td>
                </tr>
              ) : (
                filtered.map((s, idx) => {
                  const isPaid = s.sppStatus === "paid";
                  const isOverdue = s.sppStatus === "overdue";

                  return (
                    <tr
                      key={s.id}
                      className={`hover:bg-slate-50 dark:hover:bg-slate-800/50 transition-colors ${
                        idx % 2 === 0 ? "bg-white dark:bg-slate-900" : "bg-slate-50/50 dark:bg-slate-900/40"
                      }`}
                    >
                      <td className="px-4 py-3 font-mono font-bold text-slate-600 dark:text-slate-400">
                        {s.registration_no}
                      </td>

                      <td className="px-4 py-3">
                        <strong className="text-slate-900 dark:text-slate-100 text-xs block">
                          {s.full_name}
                        </strong>
                        <span className="text-[11px] text-slate-500">
                          {s.gender === "L" ? "Laki-laki" : "Perempuan"} • {s.birth_place}, {s.birth_date}
                        </span>
                      </td>

                      <td className="px-4 py-3">
                        <span className="font-bold text-slate-800 dark:text-slate-200">
                          {s.grade_level === "TK" ? "TK" : `${s.grade_level} Kelas ${s.class_grade}`}
                        </span>
                        <span className="block text-[11px] text-slate-500 dark:text-slate-400">{s.program_name}</span>
                      </td>

                      <td className="px-4 py-3 text-slate-700 dark:text-slate-300 font-medium">
                        {s.school_origin}
                      </td>

                      <td className="px-4 py-3">
                        <div className="font-semibold text-slate-800 dark:text-slate-200">{s.parent_name}</div>
                        <a
                          href={`https://wa.me/${s.parent_phone_wa?.replace(/[^0-9]/g, "")}`}
                          target="_blank"
                          rel="noreferrer"
                          className="text-[11px] text-emerald-600 dark:text-emerald-400 font-mono flex items-center gap-1 hover:underline"
                        >
                          <Phone size={10} /> {s.parent_phone_wa}
                        </a>
                      </td>

                      <td className="px-4 py-3">
                        {s.discount_amount > 0 ? (
                          <span className="inline-flex items-center gap-1 text-[10px] font-black uppercase px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-300">
                            <Tag size={10} /> Diskon Rp 200rb
                          </span>
                        ) : (
                          <span className="text-slate-500 dark:text-slate-400 text-[11px]">Reguler</span>
                        )}
                      </td>

                      <td className="px-4 py-3">
                        {isPaid ? (
                          <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-300">
                            <CheckCircle size={10} /> Lunas
                          </span>
                        ) : isOverdue ? (
                          <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border border-rose-300">
                            <AlertCircle size={10} /> Jatuh Tempo
                          </span>
                        ) : (
                          <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 border border-amber-300">
                            <Clock size={10} /> Belum Bayar
                          </span>
                        )}
                      </td>

                      <td className="px-4 py-3 text-center">
                        <button
                          onClick={() => setSelectedStudentDetail(s)}
                          style={{ border: `1.5px solid ${B}` }}
                          className="p-1.5 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:bg-slate-200 inline-flex items-center gap-1 text-[11px] font-bold"
                        >
                          <Eye size={13} /> Profil
                        </button>
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* MODAL: PROFIL LENGKAP SISWA */}
      {selectedStudentDetail && (
        <div className="fixed inset-0 z-50 bg-black/60 flex items-center justify-center p-4">
          <div
            style={{
              backgroundColor: isDark ? "#1e293b" : "#fff",
              border: `3px solid ${B}`,
              boxShadow: "6px 6px 0 0 #111118",
            }}
            className="w-full max-w-lg rounded-2xl p-6 space-y-4 max-h-[90vh] overflow-y-auto animate-in fade-in"
          >
            <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
              <div>
                <span className="font-mono text-xs px-2 py-0.5 rounded bg-amber-100 text-amber-800 font-bold">
                  {selectedStudentDetail.registration_no}
                </span>
                <h3 className="font-heading font-black text-xl text-slate-900 dark:text-white mt-1">
                  {selectedStudentDetail.full_name}
                </h3>
              </div>
              <button
                onClick={() => setSelectedStudentDetail(null)}
                className="p-1 rounded-lg border border-slate-300 dark:border-slate-700"
              >
                <X size={16} />
              </button>
            </div>

            {/* Profile Info Grid */}
            <div className="grid grid-cols-2 gap-3 text-xs bg-slate-50 dark:bg-slate-900/60 p-4 rounded-xl border border-slate-200 dark:border-slate-800">
              <div>
                <span className="text-slate-600 dark:text-slate-400 font-semibold block">Tempat, Tgl Lahir:</span>
                <span className="font-bold text-slate-800 dark:text-slate-200">
                  {selectedStudentDetail.birth_place}, {selectedStudentDetail.birth_date}
                </span>
              </div>
              <div>
                <span className="text-slate-600 dark:text-slate-400 font-semibold block">Jenjang &amp; Kelas:</span>
                <span className="font-bold text-slate-800 dark:text-slate-200">
                  {selectedStudentDetail.grade_level} (Kelas {selectedStudentDetail.class_grade})
                </span>
              </div>
              <div>
                <span className="text-slate-600 dark:text-slate-400 font-semibold block">Sekolah Asal:</span>
                <span className="text-slate-800 dark:text-slate-200">{selectedStudentDetail.school_origin}</span>
              </div>
              <div>
                <span className="text-slate-600 dark:text-slate-400 font-semibold block">Alamat Rumah:</span>
                <span className="text-slate-800 dark:text-slate-200">{selectedStudentDetail.home_address}</span>
              </div>
              <div>
                <span className="text-slate-600 dark:text-slate-400 font-semibold block">Orang Tua / Wali:</span>
                <span className="text-slate-800 dark:text-slate-200">{selectedStudentDetail.parent_name}</span>
              </div>
              <div>
                <span className="text-slate-600 dark:text-slate-400 font-semibold block">WhatsApp Wali:</span>
                <span className="font-mono text-emerald-600 dark:text-emerald-400 font-bold">
                  {selectedStudentDetail.parent_phone_wa}
                </span>
              </div>
            </div>

            {/* Sibling Info */}
            {selectedStudentDetail.sibling && (
              <div className="p-3 rounded-lg bg-green-50 dark:bg-green-950/40 border border-green-200 dark:border-green-800 text-xs text-green-800 dark:text-green-300 flex items-start gap-2">
                <Tag size={16} className="text-green-600 shrink-0 mt-0.5" />
                <div>
                  <strong>Terdaftar Saudara Kandung:</strong> {selectedStudentDetail.sibling.full_name} ({selectedStudentDetail.sibling.grade_level} Kelas {selectedStudentDetail.sibling.class_grade}). Mendapat potongan SPP Rp 200.000 setiap tagihan.
                </div>
              </div>
            )}

            {/* Enrolled Classes */}
            <div className="space-y-2">
              <h4 className="text-xs font-black uppercase tracking-wider text-slate-600 dark:text-slate-400">
                Kelas Bimbel Yang Diikuti ({selectedStudentDetail.enrolledClasses.length})
              </h4>
              {selectedStudentDetail.enrolledClasses.length === 0 ? (
                <p className="text-xs text-slate-500 italic">Belum diplotkan ke kelas.</p>
              ) : (
                <div className="divide-y divide-slate-100 dark:divide-slate-800 border rounded-xl overflow-hidden text-xs">
                  {selectedStudentDetail.enrolledClasses.map((cls) => (
                    <div key={cls.id} className="p-2.5 flex items-center justify-between bg-white dark:bg-slate-800">
                      <div className="flex items-center gap-2">
                        <BookOpen size={14} className="text-[#2727E6]" />
                        <div>
                          <p className="font-bold text-slate-900 dark:text-slate-100">{cls.class_name}</p>
                          <p className="text-[11px] text-slate-500">{cls.grade_level} • Kapasitas {cls.current_students}/{cls.max_students}</p>
                        </div>
                      </div>
                      <span className="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-blue-100 text-blue-800">
                        Aktif
                      </span>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* SPP Status */}
            <div className="space-y-2 pt-2 border-t border-slate-200 dark:border-slate-800">
              <h4 className="text-xs font-black uppercase tracking-wider text-slate-500">
                Status Tagihan SPP Juli 2026
              </h4>
              <div className="p-3 rounded-xl border border-slate-200 dark:border-slate-800 flex items-center justify-between text-xs bg-slate-50 dark:bg-slate-900/50">
                <div>
                  <p className="font-bold text-slate-900 dark:text-white">
                    {selectedStudentDetail.bill ? formatRp(selectedStudentDetail.bill.total_amount) : "Rp 0"}
                  </p>
                  <p className="text-[11px] text-slate-500">
                    Jatuh tempo: {selectedStudentDetail.bill?.due_date || "-"}
                  </p>
                </div>
                <div>
                  {selectedStudentDetail.sppStatus === "paid" ? (
                    <span className="text-emerald-600 font-black flex items-center gap-1">
                      <CheckCircle size={14} /> LUNAS
                    </span>
                  ) : (
                    <span className="text-rose-600 font-black flex items-center gap-1">
                      <AlertCircle size={14} /> MENUNGGAK
                    </span>
                  )}
                </div>
              </div>
            </div>

            <div className="pt-2 text-right">
              <button
                onClick={() => setSelectedStudentDetail(null)}
                style={{ border: `2px solid ${B}` }}
                className="px-4 py-2 rounded-lg text-xs font-black uppercase bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200"
              >
                Tutup
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
