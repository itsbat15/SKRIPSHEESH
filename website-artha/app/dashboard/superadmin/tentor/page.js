"use client";
import { useState, useMemo, useEffect } from "react";
import {
  GraduationCap,
  Clock,
  Building2,
  AlertCircle,
  CheckCircle2,
  Search,
  Filter,
  Phone,
  Printer,
  Calendar,
  Layers,
  X,
  BookOpen
} from "lucide-react";
import {
  allMentors,
  allBranches
} from "@/data/mockSuperAdminData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";

export default function SuperAdminTentorPage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const [search, setSearch] = useState("");
  const [filterBranch, setFilterBranch] = useState("all");
  const [filterLoad, setFilterLoad] = useState("all");
  const [selectedMentorDetail, setSelectedMentorDetail] = useState(null);

  // Close modal on Escape key press
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") {
        setSelectedMentorDetail(null);
      }
    };
    if (selectedMentorDetail) {
      window.addEventListener("keydown", handleKeyDown);
      return () => window.removeEventListener("keydown", handleKeyDown);
    }
  }, [selectedMentorDetail]);

  // Filtered Mentors
  const filtered = useMemo(() => {
    return allMentors.filter((m) => {
      if (filterBranch !== "all" && String(m.branch_id) !== filterBranch) return false;

      // Load classification
      const load = m.total_hours_weekly > 16 ? "heavy" : m.total_hours_weekly >= 10 ? "medium" : "normal";
      if (filterLoad !== "all" && load !== filterLoad) return false;

      if (search) {
        const q = search.toLowerCase();
        const name = m.full_name.toLowerCase();
        if (!name.includes(q)) return false;
      }

      return true;
    });
  }, [filterBranch, filterLoad, search]);

  // KPIs
  const totalTentor = allMentors.length;
  const heavyLoadTentors = allMentors.filter((m) => m.total_hours_weekly > 16).length;
  const mediumLoadTentors = allMentors.filter((m) => m.total_hours_weekly >= 10 && m.total_hours_weekly <= 16).length;
  const normalLoadTentors = allMentors.filter((m) => m.total_hours_weekly < 10).length;

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="p-2 rounded-xl bg-[#2727E6] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]">
              <GraduationCap size={20} />
            </span>
            <h2 className="font-heading font-black text-2xl text-slate-900 dark:text-white">
              Monitoring Beban Mengajar Tentor
            </h2>
          </div>
          <p className="text-xs sm:text-sm mt-1 text-slate-500 dark:text-slate-400">
            Pengawasan jam mengajar mingguan dan distribusi tentor di 8 cabang (Menu 2.3)
          </p>
        </div>

        <button
          onClick={() => window.print()}
          style={{ border: `2px solid ${B}`, boxShadow: S }}
          className="inline-flex items-center gap-1.5 text-xs font-black uppercase tracking-wide px-4 py-2 rounded-lg bg-[#FFD600] text-slate-900 hover:opacity-95"
        >
          <Printer size={14} /> Cetak Rekap Beban (PDF)
        </button>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#2727E6", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-blue-200">Total Tentor Bimbel</p>
          <p className="font-heading font-black text-3xl">{totalTentor} Guru</p>
          <p className="text-[11px] text-blue-100 mt-1">Tersebar di 8 cabang Balikpapan</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#1EAB55", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-emerald-200">Beban Ideal / Normal</p>
          <p className="font-heading font-black text-3xl">{normalLoadTentors} Guru</p>
          <p className="text-[11px] text-emerald-100 mt-1">&lt; 10 jam / minggu (Kondisi fit)</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#FF6600", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-orange-200">Beban Sedang</p>
          <p className="font-heading font-black text-3xl">{mediumLoadTentors} Guru</p>
          <p className="text-[11px] text-orange-100 mt-1">10 - 16 jam / minggu (Optimal)</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#E11D48", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-rose-200">Beban Berat / Perhatian</p>
          <p className="font-heading font-black text-3xl">{heavyLoadTentors} Guru</p>
          <p className="text-[11px] text-rose-100 mt-1">&gt; 16 jam / minggu (Perlu rotasi)</p>
        </div>
      </div>

      {/* Filter and Search Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 bg-white dark:bg-slate-900 p-3.5 rounded-xl border-2 border-[#111118]">
        <div className="relative flex-1 min-w-[220px]">
          <Search size={15} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            type="text"
            placeholder="Cari nama tentor (Om Imam, Tante Dewi...)"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full pl-9 pr-3 py-2 rounded-lg text-xs font-medium border-2 border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 outline-none"
          />
        </div>

        <div className="flex items-center gap-2 flex-wrap">
          <select
            value={filterBranch}
            onChange={(e) => setFilterBranch(e.target.value)}
            className="text-xs font-bold p-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 outline-none"
          >
            <option value="all">Semua Cabang Penugasan</option>
            {allBranches.map((br) => (
              <option key={br.id} value={String(br.id)}>
                {br.branch_name}
              </option>
            ))}
          </select>

          <select
            value={filterLoad}
            onChange={(e) => setFilterLoad(e.target.value)}
            className="text-xs font-bold p-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 outline-none"
          >
            <option value="all">Semua Tingkat Beban</option>
            <option value="normal">Normal (&lt; 10 jam)</option>
            <option value="medium">Sedang (10 - 16 jam)</option>
            <option value="heavy">Berat (&gt; 16 jam)</option>
          </select>
        </div>
      </div>

      {/* Main Table: Daftar Beban Tentor */}
      <div
        style={{
          backgroundColor: isDark ? "#1e293b" : "#ffffff",
          border: `2px solid ${B}`,
          boxShadow: S,
        }}
        className="rounded-xl overflow-hidden"
      >
        <div className="p-4 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
          <h3 className="font-heading font-black text-base text-slate-900 dark:text-slate-100 flex items-center gap-2">
            <GraduationCap size={18} className="text-[#2727E6]" />
            Daftar Beban Jam Mengajar Tentor ({filtered.length} tentor)
          </h3>
          <span className="text-xs text-slate-500 font-bold">Standard Beban Kerja: Maks 20 Jam / Minggu</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              <tr className="bg-[#111118] text-white/80">
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Nama Tentor</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Cabang Bertugas</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Kontak WhatsApp</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Kelas Aktif</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Jam Mengajar / Minggu</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Status Beban</th>
                <th className="text-center px-4 py-3 font-black uppercase tracking-wider">Aksi</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200 dark:divide-slate-800">
              {filtered.length === 0 ? (
                <tr>
                  <td colSpan={7} className="p-8 text-center bg-white dark:bg-slate-900">
                    <div className="max-w-xs mx-auto space-y-2">
                      <p className="text-sm font-bold text-slate-800 dark:text-slate-200">Tidak ada tentor ditemukan</p>
                      <p className="text-xs text-slate-500">Coba ubah kata kunci pencarian atau sesuaikan filter cabang/beban jam.</p>
                      <button
                        onClick={() => {
                          setSearch("");
                          setFilterBranch("all");
                          setFilterLoad("all");
                        }}
                        className="text-xs font-bold text-[#2727E6] dark:text-blue-400 underline hover:no-underline"
                      >
                        Reset Semua Filter
                      </button>
                    </div>
                  </td>
                </tr>
              ) : (
                filtered.map((mentor, idx) => {
                  const isHeavy = mentor.total_hours_weekly > 16;
                  const isMedium = mentor.total_hours_weekly >= 10 && mentor.total_hours_weekly <= 16;
                  const primaryBranch = allBranches.find((b) => b.id === mentor.branch_id);

                  return (
                    <tr
                      key={mentor.id}
                      className={`hover:bg-slate-50 dark:hover:bg-slate-800/50 transition-colors ${
                        idx % 2 === 0 ? "bg-white dark:bg-slate-900" : "bg-slate-50/50 dark:bg-slate-900/40"
                      }`}
                    >
                    <td className="px-4 py-3">
                      <strong className="text-xs text-slate-900 dark:text-slate-100 block">
                        {mentor.full_name}
                      </strong>
                      <span className="text-[11px] text-slate-400">ID: TNT-{String(mentor.id).padStart(3, "0")}</span>
                    </td>

                    <td className="px-4 py-3">
                      <div className="flex flex-wrap gap-1">
                        {mentor.branches_taught.map((bName) => (
                          <span
                            key={bName}
                            className="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 border border-slate-300 dark:border-slate-700"
                          >
                            {bName}
                          </span>
                        ))}
                      </div>
                    </td>

                    <td className="px-4 py-3">
                      <a
                        href={`https://wa.me/${mentor.phone_wa.replace(/[^0-9]/g, "")}`}
                        target="_blank"
                        rel="noreferrer"
                        className="font-mono text-emerald-600 dark:text-emerald-400 text-[11px] flex items-center gap-1 hover:underline"
                      >
                        <Phone size={10} /> {mentor.phone_wa}
                      </a>
                    </td>

                    <td className="px-4 py-3 font-bold text-slate-800 dark:text-slate-200">
                      {mentor.total_classes} Kelas Rombel
                    </td>

                    <td className="px-4 py-3">
                      <div className="flex items-center gap-2">
                        <span className="font-heading font-black text-sm text-slate-900 dark:text-white">
                          {mentor.total_hours_weekly} Jam
                        </span>
                        <div className="w-16 h-2 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                          <div
                            style={{
                              width: `${Math.min(100, (mentor.total_hours_weekly / 20) * 100)}%`,
                              backgroundColor: isHeavy ? "#E11D48" : isMedium ? "#FF6600" : "#1EAB55",
                            }}
                            className="h-full rounded-full"
                          />
                        </div>
                      </div>
                    </td>

                    <td className="px-4 py-3">
                      {isHeavy ? (
                        <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border border-rose-300">
                          <AlertCircle size={10} /> Beban Berat
                        </span>
                      ) : isMedium ? (
                        <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 border border-amber-300">
                          <Clock size={10} /> Beban Sedang
                        </span>
                      ) : (
                        <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-300">
                          <CheckCircle2 size={10} /> Normal
                        </span>
                      )}
                    </td>

                    <td className="px-4 py-3 text-center">
                      <button
                        onClick={() => setSelectedMentorDetail(mentor)}
                        style={{ border: `1.5px solid ${B}` }}
                        className="px-2.5 py-1 rounded-md text-[11px] font-bold bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:bg-slate-200"
                      >
                        Detail
                      </button>
                    </td>
                  </tr>
                );
              }))}
            </tbody>
          </table>
        </div>
      </div>

      {/* MODAL: DETAIL PENUGASAN TENTOR */}
      {selectedMentorDetail && (
        <div className="fixed inset-0 z-50 bg-black/60 flex items-center justify-center p-4">
          <div
            style={{
              backgroundColor: isDark ? "#1e293b" : "#fff",
              border: `3px solid ${B}`,
              boxShadow: "6px 6px 0 0 #111118",
            }}
            className="w-full max-w-md rounded-2xl p-6 space-y-4 animate-in fade-in"
          >
            <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
              <div>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-100 text-blue-800 uppercase">
                  Profil Tentor
                </span>
                <h3 className="font-heading font-black text-xl text-slate-900 dark:text-white mt-1">
                  {selectedMentorDetail.full_name}
                </h3>
              </div>
              <button
                onClick={() => setSelectedMentorDetail(null)}
                className="p-1 rounded-lg border border-slate-300 dark:border-slate-700"
              >
                <X size={16} />
              </button>
            </div>

            <div className="space-y-3 text-xs bg-slate-50 dark:bg-slate-900/60 p-4 rounded-xl border border-slate-200 dark:border-slate-800">
              <div className="flex justify-between">
                <span className="text-slate-500">Cabang Penugasan:</span>
                <strong>{selectedMentorDetail.branches_taught.join(", ")}</strong>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">No. WhatsApp:</span>
                <span className="font-mono text-emerald-600 font-bold">{selectedMentorDetail.phone_wa}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Jumlah Rombel Aktif:</span>
                <span>{selectedMentorDetail.total_classes} Kelas</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Beban Mengajar:</span>
                <strong className="text-base text-blue-600">{selectedMentorDetail.total_hours_weekly} Jam / Minggu</strong>
              </div>
              <div className="pt-2 border-t text-[11px] text-slate-500">
                {selectedMentorDetail.total_hours_weekly > 16
                  ? "⚠️ Perhatian: Beban mengajar melebihi ambang batas ideal (16 jam). Disarankan untuk menambah tentor pembantu atau membagi kelas."
                  : "✅ Beban mengajar berada dalam kapasitas ideal dan sehat untuk konsistensi pengajaran."}
              </div>
            </div>

            <div className="pt-2 flex justify-end gap-2">
              <button
                onClick={() => setSelectedMentorDetail(null)}
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
