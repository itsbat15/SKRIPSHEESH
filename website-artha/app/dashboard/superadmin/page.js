"use client";
import { useState, useMemo } from "react";
import {
  LayoutDashboard,
  Building2,
  Users,
  TrendingUp,
  AlertCircle,
  CheckCircle2,
  Calendar,
  Filter,
  ArrowUpRight,
  ChevronRight,
  ShieldAlert,
  GraduationCap,
  Trophy,
  PieChart
} from "lucide-react";
import Link from "next/link";
import {
  allBranches,
  branchSummaries,
  revenueTrend,
  revenueValidations,
  allMentorsSuperAdmin
} from "@/data/mockSuperAdminData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";

const formatRp = (n) =>
  new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", minimumFractionDigits: 0 }).format(n || 0);

export default function SuperAdminExecutivePage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const [selectedBranchFilter, setSelectedBranchFilter] = useState("all");
  const [selectedPeriod, setSelectedPeriod] = useState("2026-10");

  // Summary Metrics Across All 8 Branches
  const totalSiswaAktif = useMemo(() => {
    return branchSummaries.reduce((sum, b) => sum + b.siswa_aktif, 0);
  }, []);

  const totalRevenueBulanIni = useMemo(() => {
    return branchSummaries.reduce((sum, b) => sum + b.revenue_bulan_ini, 0);
  }, []);

  const totalTargetRevenue = useMemo(() => {
    return branchSummaries.reduce((sum, b) => sum + b.target_revenue, 0);
  }, []);

  const totalTunggakan = useMemo(() => {
    return branchSummaries.reduce((sum, b) => sum + b.tunggakan, 0);
  }, []);

  const pencapaianPersen = Math.round((totalRevenueBulanIni / totalTargetRevenue) * 100);

  // Filtered Branch Summaries
  const displayedBranches = useMemo(() => {
    if (selectedBranchFilter === "all") return branchSummaries;
    return branchSummaries.filter((b) => String(b.branch_id) === selectedBranchFilter);
  }, [selectedBranchFilter]);

  // Top Performing Branch
  const topBranch = useMemo(() => {
    return [...branchSummaries].sort((a, b) => b.revenue_bulan_ini - a.revenue_bulan_ini)[0];
  }, []);

  return (
    <div className="space-y-6">
      {/* Top Banner Executive */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="p-2 rounded-xl bg-[#2727E6] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]">
              <LayoutDashboard size={20} />
            </span>
            <h2 className="font-heading font-black text-2xl text-slate-900 dark:text-white">
              Executive Multi-Branch Overview
            </h2>
          </div>
          <p className="text-xs sm:text-sm mt-1 text-slate-500 dark:text-slate-400">
            Pemantauan langsung performa 8 cabang Bimbel Artha Balikpapan secara konsolidasian
          </p>
        </div>

        <div className="flex items-center gap-2.5">
          <select
            value={selectedBranchFilter}
            onChange={(e) => setSelectedBranchFilter(e.target.value)}
            className="text-xs font-bold px-3 py-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 outline-none"
          >
            <option value="all">Semua Cabang (Artha 1 - 8)</option>
            {allBranches.map((br) => (
              <option key={br.id} value={String(br.id)}>
                {br.branch_name} {br.label ? `(${br.label})` : ""}
              </option>
            ))}
          </select>

          <span className="text-xs font-bold px-3 py-2 rounded-lg bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 border border-amber-300">
            TA 2026/2027
          </span>
        </div>
      </div>

      {/* KPI Cards (4 Cards) */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#2727E6", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-5 text-white transition-all hover:-translate-y-0.5"
        >
          <div className="flex items-center justify-between opacity-80 text-xs font-bold uppercase tracking-wider mb-1">
            <span>Siswa Aktif (8 Cabang)</span>
            <Users size={16} />
          </div>
          <p className="font-heading font-black text-3xl my-1">{totalSiswaAktif}</p>
          <p className="text-xs text-blue-100 font-semibold">
            +44 pendaftar baru bulan ini
          </p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#1EAB55", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-5 text-white transition-all hover:-translate-y-0.5"
        >
          <div className="flex items-center justify-between opacity-80 text-xs font-bold uppercase tracking-wider mb-1">
            <span>Total Revenue (Bulan Ini)</span>
            <TrendingUp size={16} />
          </div>
          <p className="font-heading font-black text-2xl sm:text-3xl my-1">{formatRp(totalRevenueBulanIni)}</p>
          <p className="text-xs text-emerald-100 font-semibold">
            {pencapaianPersen}% dari target ({formatRp(totalTargetRevenue)})
          </p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#FFD600", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-5 text-slate-900 transition-all hover:-translate-y-0.5"
        >
          <div className="flex items-center justify-between opacity-80 text-xs font-bold uppercase tracking-wider mb-1 text-slate-800">
            <span>Cabang Teratas</span>
            <Trophy size={16} />
          </div>
          <p className="font-heading font-black text-2xl sm:text-3xl my-1">{topBranch?.branch_name}</p>
          <p className="text-xs text-slate-800 font-semibold">
            {formatRp(topBranch?.revenue_bulan_ini)} ({topBranch?.siswa_aktif} siswa)
          </p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#E11D48", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-5 text-white transition-all hover:-translate-y-0.5"
        >
          <div className="flex items-center justify-between opacity-80 text-xs font-bold uppercase tracking-wider mb-1">
            <span>Tunggakan SPP Total</span>
            <AlertCircle size={16} />
          </div>
          <p className="font-heading font-black text-3xl my-1">{totalTunggakan} Siswa</p>
          <p className="text-xs text-rose-100 font-semibold">
            Perlu tindak lanjut admin cabang
          </p>
        </div>
      </div>

      {/* Visual Bar Comparison 8 Cabang */}
      <div
        style={{
          backgroundColor: isDark ? "#1e293b" : "#fff",
          border: `2px solid ${B}`,
          boxShadow: S,
        }}
        className="rounded-2xl p-5 sm:p-6 space-y-4"
      >
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 border-b pb-4 border-slate-200 dark:border-slate-800">
          <div>
            <h3 className="font-heading font-black text-lg text-slate-900 dark:text-white flex items-center gap-2">
              <Building2 size={20} className="text-[#2727E6]" />
              Performa Pendapatan &amp; Target 8 Cabang
            </h3>
            <p className="text-xs text-slate-500">Perbandingan perolehan SPP aktual vs target bulanan tiap cabang</p>
          </div>
          <Link
            href="/dashboard/superadmin/revenue"
            className="text-xs font-black text-indigo-600 dark:text-indigo-400 hover:underline inline-flex items-center gap-1"
          >
            Lihat Validasi Rekening Detail <ArrowUpRight size={14} />
          </Link>
        </div>

        {/* Branch Bars */}
        <div className="space-y-4 pt-2">
          {displayedBranches.map((br) => {
            const pct = Math.round((br.revenue_bulan_ini / br.target_revenue) * 100);
            const isTop = br.branch_name === topBranch?.branch_name;

            return (
              <div key={br.branch_id} className="space-y-1.5 text-xs">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <span className="font-heading font-black text-sm text-slate-900 dark:text-white">
                      {br.branch_name}
                    </span>
                    {isTop && (
                      <span className="px-2 py-0.5 rounded-full text-[10px] font-black uppercase bg-amber-200 text-amber-900 border border-amber-400">
                        Tertinggi
                      </span>
                    )}
                    <span className="text-[11px] text-slate-600 dark:text-slate-400">
                      • {br.siswa_aktif} siswa • {br.kelas_aktif} kelas • {br.total_tentor} tentor
                    </span>
                  </div>
                  <div className="text-right">
                    <span className="font-black text-slate-900 dark:text-white">
                      {formatRp(br.revenue_bulan_ini)}
                    </span>
                    <span className="text-slate-600 dark:text-slate-400 font-medium"> / {formatRp(br.target_revenue)} ({pct}%)</span>
                  </div>
                </div>

                {/* Progress bar */}
                <div className="w-full h-3 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden border border-slate-200 dark:border-slate-700">
                  <div
                    style={{
                      width: `${pct}%`,
                      backgroundColor: pct >= 90 ? "#1EAB55" : pct >= 80 ? "#2727E6" : "#FF6600",
                    }}
                    className="h-full rounded-full transition-all duration-500"
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Grid: Rekap Distribusi Jenjang & Validasi Cepat */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Distribusi Jenjang Seluruh Cabang */}
        <div
          style={{
            backgroundColor: isDark ? "#1e293b" : "#fff",
            border: `2px solid ${B}`,
            boxShadow: S,
          }}
          className="rounded-2xl p-5 space-y-4"
        >
          <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
            <h3 className="font-heading font-black text-base text-slate-900 dark:text-white flex items-center gap-2">
              <PieChart size={18} className="text-[#FF6600]" />
              Distribusi Jenjang Siswa (Konsolidasi 8 Cabang)
            </h3>
            <span className="text-xs font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-800">
              Total {totalSiswaAktif} Siswa
            </span>
          </div>

          <div className="grid grid-cols-2 gap-3 text-xs">
            <div className="p-3.5 rounded-xl bg-blue-50 dark:bg-blue-950/40 border border-blue-200 dark:border-blue-800">
              <span className="text-[11px] font-black uppercase text-blue-700 dark:text-blue-300">Sekolah Dasar (SD)</span>
              <p className="font-heading font-black text-2xl text-blue-900 dark:text-blue-100 mt-1">
                {branchSummaries.reduce((sum, b) => sum + b.siswa_sd, 0)} Siswa
              </p>
              <p className="text-[10px] text-blue-600 dark:text-blue-400 mt-0.5">Segmen terbesar (kelas 1-6)</p>
            </div>

            <div className="p-3.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-800">
              <span className="text-[11px] font-black uppercase text-emerald-700 dark:text-emerald-300">SMP</span>
              <p className="font-heading font-black text-2xl text-emerald-900 dark:text-emerald-100 mt-1">
                {branchSummaries.reduce((sum, b) => sum + b.siswa_smp, 0)} Siswa
              </p>
              <p className="text-[10px] text-emerald-600 dark:text-emerald-400 mt-0.5">Persiapan UN & asesmen</p>
            </div>

            <div className="p-3.5 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-800">
              <span className="text-[11px] font-black uppercase text-rose-700 dark:text-rose-300">SMA &amp; Paket 12</span>
              <p className="font-heading font-black text-2xl text-rose-900 dark:text-rose-100 mt-1">
                {branchSummaries.reduce((sum, b) => sum + b.siswa_sma, 0)} Siswa
              </p>
              <p className="text-[10px] text-rose-600 dark:text-rose-400 mt-0.5">SNBT & Kedinasan</p>
            </div>

            <div className="p-3.5 rounded-xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800">
              <span className="text-[11px] font-black uppercase text-amber-700 dark:text-amber-300">TK / Calistung</span>
              <p className="font-heading font-black text-2xl text-amber-900 dark:text-amber-100 mt-1">
                {branchSummaries.reduce((sum, b) => sum + b.siswa_tk, 0)} Siswa
              </p>
              <p className="text-[10px] text-amber-600 dark:text-amber-400 mt-0.5">Maks 5 siswa / rombel</p>
            </div>
          </div>
        </div>

        {/* Status Validasi Rekening Pusat */}
        <div
          style={{
            backgroundColor: isDark ? "#1e293b" : "#fff",
            border: `2px solid ${B}`,
            boxShadow: S,
          }}
          className="rounded-2xl p-5 space-y-4"
        >
          <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
            <h3 className="font-heading font-black text-base text-slate-900 dark:text-white flex items-center gap-2">
              <CheckCircle2 size={18} className="text-[#1EAB55]" />
              Status Validasi Rekening Bank Pusat (BCA)
            </h3>
            <span className="text-xs font-bold text-slate-500">Juli 2026</span>
          </div>

          <div className="divide-y divide-slate-100 dark:divide-slate-800 text-xs">
            {revenueValidations.slice(0, 5).map((rv) => {
              const br = allBranches.find((b) => b.id === rv.branch_id);
              const isValidated = rv.validation_status === "validated";
              const isDiscrepancy = rv.validation_status === "discrepancy";

              return (
                <div key={rv.id} className="py-2.5 flex items-center justify-between">
                  <div>
                    <div className="flex items-center gap-2">
                      <strong className="text-slate-900 dark:text-white">{br?.branch_name}</strong>
                      {isValidated ? (
                        <span className="text-[10px] font-bold text-emerald-600 uppercase flex items-center gap-0.5">
                          <CheckCircle2 size={10} /> Divalidasi
                        </span>
                      ) : isDiscrepancy ? (
                        <span className="text-[10px] font-bold text-rose-600 uppercase flex items-center gap-0.5">
                          <AlertCircle size={10} /> Ada Selisih
                        </span>
                      ) : (
                        <span className="text-[10px] font-bold text-amber-600 uppercase">
                          Menunggu Cek
                        </span>
                      )}
                    </div>
                    <span className="text-[11px] text-slate-500 block">
                      Target: {formatRp(rv.expected_revenue)} • Aktual: {formatRp(rv.actual_revenue)}
                    </span>
                  </div>

                  <Link
                    href="/dashboard/superadmin/revenue"
                    className="px-2.5 py-1 rounded-md text-[11px] font-bold bg-slate-100 dark:bg-slate-800 hover:bg-slate-200"
                  >
                    Detail
                  </Link>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
