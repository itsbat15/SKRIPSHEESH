"use client";
import { useState, useMemo } from "react";
import {
  FileText,
  Printer,
  Download,
  Calendar,
  Building2,
  DollarSign,
  Users,
  CheckCircle,
  AlertCircle,
  TrendingUp,
  CreditCard,
  PieChart,
  BarChart3
} from "lucide-react";
import {
  bills,
  payments,
  students,
  classes,
  cabangInfo,
  pengeluaranData
} from "@/data/mockFrontdeskData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";

const formatRp = (n) =>
  new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", minimumFractionDigits: 0 }).format(n || 0);

export default function LaporanCabangPage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const [selectedDate, setSelectedDate] = useState("2026-07-05");

  // Summary Data
  const summary = useMemo(() => {
    const totalSiswa = students.length;
    const siswaSD = students.filter((s) => s.grade_level === "SD").length;
    const siswaSMP = students.filter((s) => s.grade_level === "SMP").length;
    const siswaSMA = students.filter((s) => s.grade_level === "SMA").length;
    const siswaTK = students.filter((s) => s.grade_level === "TK").length;

    const totalBills = bills.reduce((sum, b) => sum + b.total_amount, 0);
    const paidBills = bills.filter((b) => b.payment_status === "paid");
    const totalPenerimaan = paidBills.reduce((sum, b) => sum + b.total_amount, 0);
    const totalTunggakan = bills.filter((b) => b.payment_status !== "paid").reduce((sum, b) => sum + b.total_amount, 0);

    const totalPengeluaran = pengeluaranData.reduce((sum, p) => sum + p.nominal, 0);
    const labaBersih = totalPenerimaan - totalPengeluaran;

    // Capacity stats
    const totalMaxKapasitas = classes.reduce((sum, c) => sum + c.max_students, 0);
    const totalTerisi = classes.reduce((sum, c) => sum + c.current_students, 0);
    const utilisasiPersen = Math.round((totalTerisi / totalMaxKapasitas) * 100);

    return {
      totalSiswa,
      siswaSD,
      siswaSMP,
      siswaSMA,
      siswaTK,
      totalBills,
      totalPenerimaan,
      totalTunggakan,
      totalPengeluaran,
      labaBersih,
      totalMaxKapasitas,
      totalTerisi,
      utilisasiPersen,
      persenLunas: Math.round((paidBills.length / bills.length) * 100),
    };
  }, []);

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div>
          <h2 className="font-heading font-black text-2xl flex items-center gap-2.5" style={{ color: isDark ? "#f1f5f9" : B }}>
            <span className="p-2 rounded-xl bg-[#FFD600] text-slate-900 border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]">
              <FileText size={20} />
            </span>
            Laporan Operasional Cabang
          </h2>
          <p className="text-xs sm:text-sm mt-1" style={{ color: isDark ? "#94a3b8" : "#64748b" }}>
            Rekapitulasi keuangan harian, pembayaran SPP, dan utilisasi kelas cabang {cabangInfo.branch_name}
          </p>
        </div>

        <div className="flex items-center gap-2">
          <input
            type="date"
            value={selectedDate}
            onChange={(e) => setSelectedDate(e.target.value)}
            className="text-xs font-bold px-3 py-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 outline-none"
          />
          <button
            onClick={() => window.print()}
            style={{ border: `2px solid ${B}`, boxShadow: S }}
            className="inline-flex items-center gap-1.5 text-xs font-black uppercase tracking-wide px-4 py-2.5 rounded-lg bg-[#FFD600] text-slate-900 hover:opacity-95 transition-all"
          >
            <Printer size={14} /> Cetak Laporan (PDF)
          </button>
        </div>
      </div>

      {/* Main KPI Overview */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#1EAB55", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-emerald-100">Penerimaan SPP (Bulan Ini)</p>
          <p className="font-heading font-black text-2xl sm:text-3xl">{formatRp(summary.totalPenerimaan)}</p>
          <p className="text-[11px] text-emerald-100 mt-1">{summary.persenLunas}% tagihan telah lunas</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#E11D48", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-rose-100">Total Piutang / Tunggakan</p>
          <p className="font-heading font-black text-2xl sm:text-3xl">{formatRp(summary.totalTunggakan)}</p>
          <p className="text-[11px] text-rose-100 mt-1">{bills.filter((b) => b.payment_status !== "paid").length} siswa belum bayar</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#2727E6", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-blue-100">Pengeluaran Operasional</p>
          <p className="font-heading font-black text-2xl sm:text-3xl">{formatRp(summary.totalPengeluaran)}</p>
          <p className="text-[11px] text-blue-100 mt-1">Listrik, ATK, internet, dll</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#FFD600", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-xl p-4 text-slate-900"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-slate-800">Kas Bersih Cabang</p>
          <p className="font-heading font-black text-2xl sm:text-3xl">{formatRp(summary.labaBersih)}</p>
          <p className="text-[11px] text-slate-700 mt-1">Surplus operasional berjalan</p>
        </div>
      </div>

      {/* Grid Rekapitulasi Dua Kolom */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Kolom 1: Rekap Distribusi Siswa & Kapasitas */}
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
              <Users size={18} className="text-[#2727E6]" />
              Rekapitulasi Siswa &amp; Kapasitas Ruang
            </h3>
            <span className="text-xs font-bold px-2 py-0.5 rounded bg-blue-100 text-blue-800">
              Total {summary.totalSiswa} Siswa
            </span>
          </div>

          <div className="space-y-3 text-xs">
            <div>
              <div className="flex justify-between font-bold mb-1">
                <span>TK / Calistung:</span>
                <span>{summary.siswaTK} Siswa ({Math.round((summary.siswaTK / summary.totalSiswa) * 100)}%)</span>
              </div>
              <div className="w-full h-2 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
                <div style={{ width: `${(summary.siswaTK / summary.totalSiswa) * 100}%`, backgroundColor: "#FF6600" }} className="h-full" />
              </div>
            </div>

            <div>
              <div className="flex justify-between font-bold mb-1">
                <span>Sekolah Dasar (SD):</span>
                <span>{summary.siswaSD} Siswa ({Math.round((summary.siswaSD / summary.totalSiswa) * 100)}%)</span>
              </div>
              <div className="w-full h-2 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
                <div style={{ width: `${(summary.siswaSD / summary.totalSiswa) * 100}%`, backgroundColor: "#2727E6" }} className="h-full" />
              </div>
            </div>

            <div>
              <div className="flex justify-between font-bold mb-1">
                <span>SMP:</span>
                <span>{summary.siswaSMP} Siswa ({Math.round((summary.siswaSMP / summary.totalSiswa) * 100)}%)</span>
              </div>
              <div className="w-full h-2 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
                <div style={{ width: `${(summary.siswaSMP / summary.totalSiswa) * 100}%`, backgroundColor: "#1EAB55" }} className="h-full" />
              </div>
            </div>

            <div>
              <div className="flex justify-between font-bold mb-1">
                <span>SMA:</span>
                <span>{summary.siswaSMA} Siswa ({Math.round((summary.siswaSMA / summary.totalSiswa) * 100)}%)</span>
              </div>
              <div className="w-full h-2 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
                <div style={{ width: `${(summary.siswaSMA / summary.totalSiswa) * 100}%`, backgroundColor: "#E11D48" }} className="h-full" />
              </div>
            </div>
          </div>

          {/* Utilisasi Kelas */}
          <div className="p-4 rounded-xl bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 space-y-2 mt-4 text-xs">
            <div className="flex justify-between items-center font-bold">
              <span>Tingkat Utilisasi Kursi Kelas:</span>
              <span className="text-[#2727E6] font-black">{summary.totalTerisi} / {summary.totalMaxKapasitas} ({summary.utilisasiPersen}%)</span>
            </div>
            <div className="w-full h-2.5 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
              <div style={{ width: `${summary.utilisasiPersen}%`, backgroundColor: "#2727E6" }} className="h-full" />
            </div>
            <p className="text-[11px] text-slate-500">
              Kapasitas masih longgar dan siap menerima hingga {summary.totalMaxKapasitas - summary.totalTerisi} siswa baru tanpa penambahan rombel.
            </p>
          </div>
        </div>

        {/* Kolom 2: Rekap Transaksi Terakhir (Payments Log) */}
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
              <CreditCard size={18} className="text-[#1EAB55]" />
              Riwayat Pembayaran Kasir Terbaru
            </h3>
            <span className="text-xs font-bold text-slate-500">
              {payments.length} Transaksi Tercatat
            </span>
          </div>

          <div className="divide-y divide-slate-100 dark:divide-slate-800 text-xs overflow-hidden">
            {payments.slice(0, 6).map((p) => {
              const matchedBill = bills.find((b) => b.id === p.bill_id);
              const matchedStudent = matchedBill ? students.find((s) => s.id === matchedBill.student_id) : null;

              return (
                <div key={p.id} className="py-2.5 flex items-center justify-between">
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="font-mono font-bold text-[10px] px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800">
                        {p.receipt_no}
                      </span>
                      <strong className="text-slate-900 dark:text-white">{matchedStudent?.full_name || "Siswa"}</strong>
                    </div>
                    <span className="text-[11px] text-slate-500 block mt-0.5">
                      {p.payment_date} • Metode: <span className="uppercase font-semibold">{p.payment_method}</span>
                    </span>
                  </div>
                  <div className="text-right">
                    <span className="font-black text-slate-900 dark:text-white block">
                      {formatRp(p.amount_paid)}
                    </span>
                    <span className="text-[10px] font-bold text-emerald-600">LUNAS</span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
