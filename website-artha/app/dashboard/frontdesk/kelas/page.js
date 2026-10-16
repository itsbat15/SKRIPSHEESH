"use client";
import { useState, useMemo, useEffect } from "react";
import {
  CalendarDays,
  Users,
  AlertCircle,
  CheckCircle2,
  Clock,
  MapPin,
  GraduationCap,
  Plus,
  UserCheck,
  Search,
  Filter,
  ShieldCheck,
  AlertTriangle,
  UserPlus,
  X
} from "lucide-react";
import {
  classes,
  classSchedules,
  classRooms,
  mentors,
  subjects,
  classEnrollments,
  students,
  capacityRules,
  cabangInfo
} from "@/data/mockFrontdeskData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const border = "#111118";
const shadow = "4px 4px 0 0 #111118";

const cardBgColors = [
  "#ECEAFC", "#B8F0D8", "#FFBAD2", "#C5E8F7",
  "#FFF0D4", "#FFD600", "#E0E7FF", "#DCFCE7",
];

const dayMap = {
  monday: "Senin",
  tuesday: "Selasa",
  wednesday: "Rabu",
  thursday: "Kamis",
  friday: "Jumat",
  saturday: "Sabtu",
  sunday: "Minggu",
};

export default function KelasPage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const [filterJenjang, setFilterJenjang] = useState("all");
  const [filterSubject, setFilterSubject] = useState("all");
  const [selectedClassDetail, setSelectedClassDetail] = useState(null);
  const [showPlottingModal, setShowPlottingModal] = useState(false);
  const [targetClassForPlotting, setTargetClassForPlotting] = useState(null);
  const [studentToPlot, setStudentToPlot] = useState("");

  // Close modals on Escape key press
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") {
        setSelectedClassDetail(null);
        setShowPlottingModal(false);
      }
    };
    if (selectedClassDetail || showPlottingModal) {
      window.addEventListener("keydown", handleKeyDown);
      return () => window.removeEventListener("keydown", handleKeyDown);
    }
  }, [selectedClassDetail, showPlottingModal]);

  // Map Classes with relational entities
  const enrichedClasses = useMemo(() => {
    return classes.map((c) => {
      const schedules = classSchedules.filter((cs) => cs.class_id === c.id);
      const firstSched = schedules[0];
      const mentor = firstSched ? mentors.find((m) => m.id === firstSched.mentor_id) : null;
      const room = firstSched ? classRooms.find((r) => r.id === firstSched.room_id) : null;
      const subject = subjects.find((sb) => sb.id === c.subject_id);

      // Enrollments
      const enrolls = classEnrollments.filter((ce) => ce.class_id === c.id);
      const activeEnrolls = enrolls.filter((ce) => ce.enrollment_status === "active");
      const waitingEnrolls = enrolls.filter((ce) => ce.enrollment_status === "waiting_list");

      // Matching rule
      const capRule = capacityRules.find((cr) => {
        return (
          cr.grade_level === c.grade_level &&
          c.class_grade >= cr.class_grade_start &&
          c.class_grade <= cr.class_grade_end
        );
      });

      const maxLimit = c.max_students || (capRule ? capRule.max_students : 10);
      const isFull = c.current_students >= maxLimit;
      const isNearFull = c.current_students >= maxLimit * 0.8 && !isFull;

      // Bentrok detector (mock check: if schedule conflicts with another mentor or room)
      const hasConflict = false; // All schedules are pre-harmonized in mock

      return {
        ...c,
        schedules,
        mentor,
        room,
        subject,
        capRule,
        maxLimit,
        isFull,
        isNearFull,
        hasConflict,
        activeEnrolls,
        waitingEnrolls,
        enrolledStudents: activeEnrolls.map((ae) => students.find((s) => s.id === ae.student_id)).filter(Boolean),
        waitingStudents: waitingEnrolls.map((we) => students.find((s) => s.id === we.student_id)).filter(Boolean),
      };
    });
  }, []);

  // Filtered classes
  const filteredClasses = useMemo(() => {
    return enrichedClasses.filter((c) => {
      if (filterJenjang !== "all" && c.grade_level !== filterJenjang) return false;
      if (filterSubject !== "all" && String(c.subject_id) !== filterSubject) return false;
      return true;
    });
  }, [enrichedClasses, filterJenjang, filterSubject]);

  // Overall statistics
  const totalClasses = enrichedClasses.length;
  const fullClasses = enrichedClasses.filter((c) => c.isFull).length;
  const availableClasses = enrichedClasses.filter((c) => !c.isFull).length;
  const totalEnrolled = enrichedClasses.reduce((acc, c) => acc + c.current_students, 0);

  const handleOpenPlotting = (cls) => {
    setTargetClassForPlotting(cls);
    setShowPlottingModal(true);
  };

  const handlePlotStudent = (e) => {
    e.preventDefault();
    if (!studentToPlot) return;
    const st = students.find((s) => s.id === parseInt(studentToPlot));
    alert(
      `Berhasil menambahkan siswa ${st?.full_name} ke kelas ${targetClassForPlotting?.class_name}!`
    );
    setShowPlottingModal(false);
    setStudentToPlot("");
  };

  return (
    <div className="space-y-6">
      {/* Header Info */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div>
          <h2 className="font-heading font-black text-2xl flex items-center gap-2.5" style={{ color: isDark ? "#f1f5f9" : border }}>
            <span className="p-2 rounded-xl bg-[#FF6600] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]">
              <CalendarDays size={20} />
            </span>
            Plotting Kelas &amp; Kapasitas
          </h2>
          <p className="text-xs sm:text-sm mt-1" style={{ color: isDark ? "#94a3b8" : "#64748b" }}>
            Manajemen alokasi siswa, batasan rasio tentor (TK max 5, SD 1 max 5, SD 2-6 max 7-10, SMP/SMA max 12-14)
          </p>
        </div>

        <div className="flex items-center gap-2">
          <span className="text-xs font-bold px-3 py-1.5 rounded-lg bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-800 flex items-center gap-1.5">
            <ShieldCheck size={14} /> Bebas Bentrok Jadwal
          </span>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#2727E6", border: `2.5px solid ${border}`, boxShadow: shadow, color: "#fff" }}
          className="rounded-xl p-4 transition-all"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-blue-200">Total Kelas Aktif</p>
          <p className="font-heading font-black text-3xl">{totalClasses}</p>
          <p className="text-[11px] text-blue-100 mt-1">{cabangInfo.branch_name} • TA 2026/2027</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#1EAB55", border: `2.5px solid ${border}`, boxShadow: shadow, color: "#fff" }}
          className="rounded-xl p-4 transition-all"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-emerald-200">Kelas Tersedia</p>
          <p className="font-heading font-black text-3xl">{availableClasses}</p>
          <p className="text-[11px] text-emerald-100 mt-1">Siap menampung siswa baru</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#E11D48", border: `2.5px solid ${border}`, boxShadow: shadow, color: "#fff" }}
          className="rounded-xl p-4 transition-all"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-rose-200">Kelas Penuh</p>
          <p className="font-heading font-black text-3xl">{fullClasses}</p>
          <p className="text-[11px] text-rose-100 mt-1">Waiting list aktif otomatis</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#FFD600", border: `2.5px solid ${border}`, boxShadow: shadow, color: border }}
          className="rounded-xl p-4 transition-all"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-slate-800">Total Siswa Terploting</p>
          <p className="font-heading font-black text-3xl">{totalEnrolled}</p>
          <p className="text-[11px] text-slate-700 mt-1">Rata-rata 7.2 siswa / kelas</p>
        </div>
      </div>

      {/* Rules Notice Box */}
      <div className="p-3.5 rounded-xl bg-amber-50 dark:bg-amber-950/30 border-2 border-amber-300 dark:border-amber-800 flex items-start gap-3 text-xs text-amber-900 dark:text-amber-200">
        <AlertTriangle size={18} className="text-amber-600 shrink-0 mt-0.5" />
        <div className="space-y-1">
          <strong>Aturan Kapasitas Siswa per Jenjang (Tabel `capacity_rules`):</strong>
          <div className="flex flex-wrap gap-x-4 gap-y-1 text-[11px] text-amber-800 dark:text-amber-300">
            <span>• TK/Calistung: <strong>maks 5</strong></span>
            <span>• SD Kelas 1: <strong>maks 5</strong> (intensif membaca)</span>
            <span>• SD Kelas 2: <strong>maks 7</strong></span>
            <span>• SD Kelas 3-6: <strong>maks 10</strong></span>
            <span>• SMP: <strong>maks 12</strong></span>
            <span>• SMA: <strong>maks 14</strong></span>
          </div>
        </div>
      </div>

      {/* Filters Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 bg-white dark:bg-slate-900 p-3 rounded-xl border-2 border-[#111118]">
        <div className="flex flex-wrap items-center gap-2">
          <span className="text-xs font-black uppercase text-slate-500 flex items-center gap-1.5 mr-1">
            <Filter size={14} /> Jenjang:
          </span>
          {["all", "TK", "SD", "SMP", "SMA"].map((jen) => (
            <button
              key={jen}
              onClick={() => setFilterJenjang(jen)}
              className={`px-3 py-1 rounded-lg text-xs font-black uppercase transition-all ${
                filterJenjang === jen
                  ? "bg-[#2727E6] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]"
                  : "bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200"
              }`}
            >
              {jen === "all" ? "Semua Jenjang" : jen}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-2">
          <label className="text-xs font-bold text-slate-500">Mata Pelajaran:</label>
          <select
            value={filterSubject}
            onChange={(e) => setFilterSubject(e.target.value)}
            className="text-xs font-bold p-1.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 outline-none"
          >
            <option value="all">Semua Mapel</option>
            {subjects.map((sb) => (
              <option key={sb.id} value={String(sb.id)}>
                {sb.subject_name}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Class Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        {filteredClasses.length === 0 ? (
          <div className="col-span-full p-8 text-center bg-white dark:bg-slate-900 rounded-xl border-2 border-[#111118]">
            <p className="text-sm font-bold text-slate-800 dark:text-slate-200">Tidak ada kelas ditemukan</p>
            <p className="text-xs text-slate-500 mt-1">Coba sesuaikan filter jenjang atau mata pelajaran.</p>
            <button
              onClick={() => {
                setFilterJenjang("all");
                setFilterSubject("all");
              }}
              className="mt-3 text-xs font-bold text-[#2727E6] dark:text-blue-400 underline hover:no-underline"
            >
              Reset Filter Kelas
            </button>
          </div>
        ) : (
          filteredClasses.map((kelas, idx) => {
          const percentage = Math.min(100, Math.round((kelas.current_students / kelas.maxLimit) * 100));
          const cardBg = isDark ? "#1e293b" : cardBgColors[idx % cardBgColors.length];
          const textMain = isDark ? "#f1f5f9" : "#111118";
          const barColor = kelas.isFull ? "#E11D48" : kelas.isNearFull ? "#FF6600" : "#1EAB55";

          // Formatted schedule text
          const daysText = kelas.schedules
            .map((s) => dayMap[s.day_of_week] || s.day_of_week)
            .join(", ");
          const timeText = kelas.schedules[0]
            ? `${kelas.schedules[0].start_time} - ${kelas.schedules[0].end_time}`
            : "-";

          return (
            <div
              key={kelas.id}
              style={{
                backgroundColor: cardBg,
                border: `2.5px solid ${border}`,
                boxShadow: shadow,
              }}
              className="rounded-2xl p-4 flex flex-col justify-between transition-all hover:-translate-y-1 hover:shadow-[6px_6px_0_0_#111118]"
            >
              <div>
                {/* Header Card */}
                <div className="flex items-start justify-between gap-2 mb-2">
                  <div>
                    <span className="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-white/80 dark:bg-slate-900/80 border border-slate-300 dark:border-slate-700 text-slate-800 dark:text-slate-200">
                      {kelas.grade_level} {kelas.grade_level !== "TK" && `Kelas ${kelas.class_grade}`}
                    </span>
                    <h3 className="font-heading font-black text-lg mt-1" style={{ color: textMain }}>
                      {kelas.class_name}
                    </h3>
                  </div>

                  <span
                    style={{
                      backgroundColor: kelas.isFull ? "#E11D48" : kelas.isNearFull ? "#FF6600" : "#1EAB55",
                      color: "#fff",
                      border: `1.5px solid ${border}`,
                    }}
                    className="text-[10px] font-black uppercase tracking-wide px-2 py-0.5 rounded-md flex items-center gap-1 shrink-0"
                  >
                    {kelas.isFull ? (
                      <>
                        <AlertCircle size={10} /> Penuh
                      </>
                    ) : kelas.isNearFull ? (
                      "Hampir Penuh"
                    ) : (
                      <>
                        <CheckCircle2 size={10} /> {kelas.maxLimit - kelas.current_students} Sisa
                      </>
                    )}
                  </span>
                </div>

                {/* Details Meta */}
                <div className="space-y-1.5 text-xs text-slate-700 dark:text-slate-300 my-3 bg-white/70 dark:bg-slate-900/60 p-2.5 rounded-xl border border-black/10 dark:border-white/10">
                  <div className="flex items-center gap-1.5">
                    <GraduationCap size={13} className="text-[#2727E6] shrink-0" />
                    <span>
                      Tentor: <strong>{kelas.mentor?.full_name || "Belum Ditentukan"}</strong>
                    </span>
                  </div>
                  <div className="flex items-center gap-1.5">
                    <MapPin size={13} className="text-[#E11D48] shrink-0" />
                    <span>
                      Ruang: <strong>{kelas.room?.room_name || "Ruang 1"}</strong> (Tipe {kelas.room?.room_type})
                    </span>
                  </div>
                  <div className="flex items-center gap-1.5">
                    <Clock size={13} className="text-[#FF6600] shrink-0" />
                    <span>
                      Jadwal: <strong>{daysText || "Senin, Rabu, Jumat"}</strong> ({timeText})
                    </span>
                  </div>
                </div>

                {/* Capacity Progress Bar */}
                <div className="mb-3">
                  <div className="flex items-center justify-between text-xs mb-1">
                    <span className="font-bold flex items-center gap-1 text-slate-700 dark:text-slate-300">
                      <Users size={12} /> Terisi / Batas Max
                    </span>
                    <span className="font-black" style={{ color: barColor }}>
                      {kelas.current_students} / {kelas.maxLimit} siswa ({percentage}%)
                    </span>
                  </div>
                  <div className="w-full h-2.5 bg-black/10 dark:bg-white/10 rounded-full overflow-hidden border border-black/20">
                    <div
                      style={{ width: `${percentage}%`, backgroundColor: barColor }}
                      className="h-full transition-all duration-500"
                    />
                  </div>
                  <p className="text-[10px] text-slate-500 dark:text-slate-400 mt-1">
                    Aturan: {kelas.capRule?.description || `Max ${kelas.maxLimit} siswa`}
                  </p>
                </div>

                {/* Seat Slots Dots */}
                <div className="flex gap-1 flex-wrap mb-4">
                  {Array.from({ length: kelas.maxLimit }).map((_, i) => {
                    const occupied = i < kelas.current_students;
                    return (
                      <div
                        key={i}
                        title={occupied ? `Kursi ${i + 1}: Terisi` : `Kursi ${i + 1}: Kosong`}
                        style={{
                          backgroundColor: occupied ? barColor : "rgba(0,0,0,0.06)",
                          color: occupied ? "#fff" : "rgba(0,0,0,0.3)",
                          border: occupied ? `1px solid ${border}` : "1px dashed rgba(0,0,0,0.2)",
                        }}
                        className="w-5 h-5 rounded text-[9px] font-black flex items-center justify-center transition-transform hover:scale-110"
                      >
                        {i + 1}
                      </div>
                    );
                  })}
                </div>
              </div>

              {/* Action Buttons */}
              <div className="pt-2 border-t border-black/10 dark:border-white/10 flex items-center gap-2">
                <button
                  onClick={() => setSelectedClassDetail(kelas)}
                  style={{ border: `1.5px solid ${border}` }}
                  className="flex-1 py-1.5 px-2 rounded-lg text-xs font-bold bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:bg-slate-100 transition-all text-center"
                >
                  Lihat Siswa ({kelas.current_students})
                </button>
                <button
                  onClick={() => handleOpenPlotting(kelas)}
                  disabled={kelas.isFull}
                  style={{
                    border: `1.5px solid ${border}`,
                    backgroundColor: kelas.isFull ? "#94a3b8" : "#2727E6",
                    color: "#fff",
                  }}
                  className="py-1.5 px-2.5 rounded-lg text-xs font-bold flex items-center gap-1 hover:opacity-95 disabled:opacity-50 transition-all"
                  title={kelas.isFull ? "Kelas sudah penuh" : "Plotting siswa ke kelas ini"}
                >
                  <Plus size={13} /> Plot
                </button>
              </div>
            </div>
          );
        }))}
      </div>

      {/* MODAL: DAFTAR SISWA KELAS */}
      {selectedClassDetail && (
        <div className="fixed inset-0 z-50 bg-black/60 flex items-center justify-center p-4">
          <div
            style={{
              backgroundColor: isDark ? "#1e293b" : "#fff",
              border: `3px solid ${border}`,
              boxShadow: "6px 6px 0 0 #111118",
            }}
            className="w-full max-w-lg rounded-2xl p-6 space-y-4 max-h-[85vh] overflow-y-auto animate-in fade-in"
          >
            <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
              <div>
                <span className="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-blue-100 text-blue-800">
                  {selectedClassDetail.grade_level} • {selectedClassDetail.subject?.subject_name}
                </span>
                <h3 className="font-heading font-black text-xl text-slate-900 dark:text-white mt-1">
                  {selectedClassDetail.class_name}
                </h3>
              </div>
              <button
                onClick={() => setSelectedClassDetail(null)}
                className="p-1.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800"
              >
                <X size={16} />
              </button>
            </div>

            {/* List Siswa Aktif */}
            <div className="space-y-2">
              <h4 className="text-xs font-black uppercase text-slate-600 dark:text-slate-400 tracking-wider">
                Siswa Aktif Terdaftar ({selectedClassDetail.enrolledStudents.length} / {selectedClassDetail.maxLimit})
              </h4>

              {selectedClassDetail.enrolledStudents.length === 0 ? (
                <p className="text-xs text-slate-500 italic py-2">Belum ada siswa yang diplotkan ke kelas ini.</p>
              ) : (
                <div className="divide-y divide-slate-100 dark:divide-slate-800 border rounded-xl overflow-hidden">
                  {selectedClassDetail.enrolledStudents.map((st, i) => (
                    <div key={st.id} className="p-2.5 flex items-center justify-between text-xs bg-slate-50 dark:bg-slate-900/50">
                      <div className="flex items-center gap-2">
                        <span className="w-5 h-5 rounded-full bg-blue-600 text-white font-bold flex items-center justify-center text-[10px]">
                          {i + 1}
                        </span>
                        <div>
                          <p className="font-bold text-slate-900 dark:text-slate-100">{st.full_name}</p>
                          <p className="text-[11px] text-slate-500">{st.school_origin} • Wali: {st.parent_name}</p>
                        </div>
                      </div>
                      <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-800">
                        {st.registration_no}
                      </span>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* Waiting List (if any) */}
            {selectedClassDetail.waitingStudents.length > 0 && (
              <div className="space-y-2 pt-2">
                <h4 className="text-xs font-black uppercase text-rose-500 tracking-wider flex items-center gap-1.5">
                  <AlertCircle size={14} /> Daftar Tunggu / Waiting List ({selectedClassDetail.waitingStudents.length})
                </h4>
                <div className="border border-rose-200 dark:border-rose-900/50 rounded-xl divide-y divide-rose-100 dark:divide-rose-950/60 bg-rose-50/50 dark:bg-rose-950/20 text-xs">
                  {selectedClassDetail.waitingStudents.map((st, i) => (
                    <div key={st.id} className="p-2.5 flex items-center justify-between">
                      <div>
                        <p className="font-bold text-rose-900 dark:text-rose-200">{st.full_name}</p>
                        <p className="text-[11px] text-rose-700 dark:text-rose-400">Antrian #{i + 1} • {st.school_origin}</p>
                      </div>
                      <span className="text-[10px] font-bold text-rose-600 uppercase">Menunggu Kuota</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            <div className="pt-2 text-right">
              <button
                onClick={() => setSelectedClassDetail(null)}
                style={{ border: `2px solid ${border}` }}
                className="px-4 py-2 rounded-lg text-xs font-black uppercase tracking-wide bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200"
              >
                Tutup
              </button>
            </div>
          </div>
        </div>
      )}

      {/* MODAL: FORM PLOTTING SISWA KE KELAS */}
      {showPlottingModal && targetClassForPlotting && (
        <div className="fixed inset-0 z-50 bg-black/60 flex items-center justify-center p-4">
          <div
            style={{
              backgroundColor: isDark ? "#1e293b" : "#fff",
              border: `3px solid ${border}`,
              boxShadow: "6px 6px 0 0 #111118",
            }}
            className="w-full max-w-md rounded-2xl p-6 space-y-4 animate-in fade-in"
          >
            <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
              <h3 className="font-heading font-black text-lg text-slate-900 dark:text-white flex items-center gap-2">
                <UserPlus size={18} className="text-[#2727E6]" />
                Plotting Siswa ke {targetClassForPlotting.class_name}
              </h3>
              <button
                onClick={() => setShowPlottingModal(false)}
                className="p-1 rounded-lg border border-slate-300 dark:border-slate-700"
              >
                <X size={16} />
              </button>
            </div>

            <form onSubmit={handlePlotStudent} className="space-y-4 text-xs">
              <div className="p-3 rounded-lg bg-blue-50 dark:bg-blue-950/40 text-blue-800 dark:text-blue-300 border border-blue-200 dark:border-blue-800">
                <p>
                  <strong>Kapasitas Tersedia:</strong> {targetClassForPlotting.maxLimit - targetClassForPlotting.current_students} dari {targetClassForPlotting.maxLimit} kursi.
                </p>
                <p className="mt-1 text-[11px]">
                  Jenjang target: <strong>{targetClassForPlotting.grade_level}</strong> (Mata Pelajaran: {targetClassForPlotting.subject?.subject_name})
                </p>
              </div>

              <div>
                <label className="font-black uppercase text-slate-500 block mb-1.5">
                  Pilih Siswa Cabang Artha 1:
                </label>
                <select
                  value={studentToPlot}
                  onChange={(e) => setStudentToPlot(e.target.value)}
                  required
                  className="w-full p-2.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100 font-medium outline-none text-xs"
                >
                  <option value="">-- Pilih Siswa yang Terdaftar --</option>
                  {students
                    .filter((s) => s.grade_level === targetClassForPlotting.grade_level)
                    .map((s) => (
                      <option key={s.id} value={s.id}>
                        {s.full_name} ({s.registration_no} • Kelas {s.class_grade} {s.grade_level})
                      </option>
                    ))}
                </select>
              </div>

              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowPlottingModal(false)}
                  className="px-3 py-2 rounded-lg font-bold border border-slate-300 dark:border-slate-700"
                >
                  Batal
                </button>
                <button
                  type="submit"
                  style={{ border: `2px solid ${border}`, boxShadow: "2px 2px 0 0 #111118" }}
                  className="px-4 py-2 rounded-lg font-black uppercase text-white bg-[#1EAB55] hover:opacity-95"
                >
                  Simpan Plotting
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
