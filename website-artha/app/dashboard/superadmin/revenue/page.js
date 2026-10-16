"use client";
import { useState, useMemo, useEffect } from "react";
import {
  TrendingUp,
  Building2,
  CheckCircle2,
  AlertCircle,
  Clock,
  Printer,
  Download,
  Filter,
  Check,
  Search,
  FileCheck,
  ShieldCheck,
  X,
  CreditCard,
  DollarSign
} from "lucide-react";
import {
  allBranches,
  revenueValidations,
  branchSummaries,
  allUsers
} from "@/data/mockSuperAdminData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";

const formatRp = (n) =>
  new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", minimumFractionDigits: 0 }).format(n || 0);

export default function SuperAdminRevenuePage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const [validations, setValidations] = useState(revenueValidations);
  const [selectedPeriod, setSelectedPeriod] = useState("2026-07");
  const [filterStatus, setFilterStatus] = useState("all");
  const [selectedForValidation, setSelectedForValidation] = useState(null);
  const [validationNote, setValidationNote] = useState("");
  const [actionStatus, setActionStatus] = useState("validated");

  // Close modal on Escape key press
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") {
        setSelectedForValidation(null);
      }
    };
    if (selectedForValidation) {
      window.addEventListener("keydown", handleKeyDown);
      return () => window.removeEventListener("keydown", handleKeyDown);
    }
  }, [selectedForValidation]);

  // Enriched Validations list with branch & user info
  const enrichedValidations = useMemo(() => {
    return validations.map((rv) => {
      const branch = allBranches.find((b) => b.id === rv.branch_id);
      const validator = allUsers.find((u) => u.id === rv.validated_by_user_id);
      const discrepancy = rv.expected_revenue - rv.actual_revenue;

      return {
        ...rv,
        branch,
        validator,
        discrepancy,
      };
    });
  }, [validations]);

  // Filtered
  const filtered = useMemo(() => {
    return enrichedValidations.filter((rv) => {
      if (filterStatus !== "all" && rv.validation_status !== filterStatus) return false;
      return true;
    });
  }, [enrichedValidations, filterStatus]);

  // KPI Calculations
  const totalTargetSemua = enrichedValidations.reduce((sum, v) => sum + v.expected_revenue, 0);
  const totalAktualSemua = enrichedValidations.reduce((sum, v) => sum + v.actual_revenue, 0);
  const totalSelisihSemua = totalTargetSemua - totalAktualSemua;
  const countValidated = enrichedValidations.filter((v) => v.validation_status === "validated").length;
  const countPending = enrichedValidations.filter((v) => v.validation_status === "pending").length;
  const countDiscrepancy = enrichedValidations.filter((v) => v.validation_status === "discrepancy").length;

  const handleOpenValidation = (item) => {
    setSelectedForValidation(item);
    setValidationNote(item.notes || "");
    setActionStatus(item.validation_status === "discrepancy" ? "discrepancy" : "validated");
  };

  const handleSaveValidation = (e) => {
    e.preventDefault();
    if (!selectedForValidation) return;

    setValidations((prev) =>
      prev.map((item) => {
        if (item.id === selectedForValidation.id) {
          return {
            ...item,
            validation_status: actionStatus,
            notes: validationNote || (actionStatus === "validated" ? "Sudah dicocokkan dengan mutasi rekening BCA pusat" : "Perlu pengecekan ulang"),
            validated_by_user_id: 3, // Pak Subagio (Bendahara Pusat)
            validated_at: new Date().toISOString().split("T")[0],
          };
        }
        return item;
      })
    );

    setSelectedForValidation(null);
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="p-2 rounded-xl bg-[#1EAB55] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]">
              <TrendingUp size={20} />
            </span>
            <h2 className="font-heading font-black text-2xl text-slate-900 dark:text-white">
              Monitoring &amp; Validasi Revenue 8 Cabang
            </h2>
          </div>
          <p className="text-xs sm:text-sm mt-1 text-slate-500 dark:text-slate-400">
            Rekonsiliasi penerimaan SPP kasir cabang dengan rekening bank BCA pusat (Menu 2.2)
          </p>
        </div>

        <div className="flex items-center gap-2">
          <select
            value={selectedPeriod}
            onChange={(e) => setSelectedPeriod(e.target.value)}
            className="text-xs font-bold px-3 py-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 outline-none"
          >
            <option value="2026-07">Periode Juli 2026</option>
            <option value="2026-08">Periode Agustus 2026</option>
            <option value="2026-09">Periode September 2026</option>
            <option value="2026-10">Periode Oktober 2026</option>
          </select>
          <button
            onClick={() => window.print()}
            style={{ border: `2px solid ${B}`, boxShadow: S }}
            className="inline-flex items-center gap-1.5 text-xs font-black uppercase tracking-wide px-4 py-2 rounded-lg bg-[#FFD600] text-slate-900 hover:opacity-95"
          >
            <Printer size={14} /> Cetak Rekap PDF
          </button>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#2727E6", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-5 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-blue-200">Target Revenue Konsolidasian</p>
          <p className="font-heading font-black text-2xl sm:text-3xl my-1">{formatRp(totalTargetSemua)}</p>
          <p className="text-[11px] text-blue-100">8 Cabang • {selectedPeriod}</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#1EAB55", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-5 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-emerald-200">Realisasi Penerimaan</p>
          <p className="font-heading font-black text-2xl sm:text-3xl my-1">{formatRp(totalAktualSemua)}</p>
          <p className="text-[11px] text-emerald-100">
            {Math.round((totalAktualSemua / totalTargetSemua) * 100)}% dari total target
          </p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#E11D48", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-5 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-rose-200">Total Selisih / Tertunggak</p>
          <p className="font-heading font-black text-2xl sm:text-3xl my-1">{formatRp(totalSelisihSemua)}</p>
          <p className="text-[11px] text-rose-100">Belum masuk kas pusat</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#FFD600", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-5 text-slate-900"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-slate-800">Status Rekonsiliasi</p>
          <p className="font-heading font-black text-3xl my-1">{countValidated} / 8</p>
          <p className="text-[11px] text-slate-800 font-bold">
            {countPending} menunggu • {countDiscrepancy} ada selisih
          </p>
        </div>
      </div>

      {/* Filter Tabs */}
      <div className="flex flex-wrap items-center justify-between gap-3 bg-white dark:bg-slate-900 p-3.5 rounded-xl border-2 border-[#111118]">
        <div className="flex items-center gap-2">
          <span className="text-xs font-black uppercase text-slate-500 mr-2 flex items-center gap-1.5">
            <Filter size={14} /> Status Validasi:
          </span>
          {[
            { id: "all", label: "Semua (8 Cabang)" },
            { id: "validated", label: "Sudah Divalidasi" },
            { id: "pending", label: "Menunggu Cek" },
            { id: "discrepancy", label: "Ada Selisih" },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setFilterStatus(tab.id)}
              className={`px-3 py-1.5 rounded-lg text-xs font-black uppercase transition-all ${
                filterStatus === tab.id
                  ? "bg-[#111118] text-white shadow-[2px_2px_0_0_#1EAB55]"
                  : "bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>

        <div className="text-xs text-slate-500 font-bold">
          Rekening BCA: <strong>024-9988-771</strong> a/n Bimbel Artha Mandiri
        </div>
      </div>

      {/* Main Table: Rekapitulasi 8 Cabang */}
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
            <Building2 size={18} className="text-[#2727E6]" />
            Daftar Rekonsiliasi Penerimaan SPP per Cabang
          </h3>
          <span className="text-xs text-slate-500 font-bold">Periode: {selectedPeriod}</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              <tr className="bg-[#111118] text-white/80">
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Nama Cabang</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Alamat &amp; Kontak</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Target SPP</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Penerimaan Aktual</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Selisih</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Pencapaian</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Status Validasi</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Verifikator &amp; Catatan</th>
                <th className="text-center px-4 py-3 font-black uppercase tracking-wider">Aksi Pusat</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200 dark:divide-slate-800">
              {filtered.length === 0 ? (
                <tr>
                  <td colSpan={9} className="p-8 text-center bg-white dark:bg-slate-900">
                    <div className="max-w-xs mx-auto space-y-2">
                      <p className="text-sm font-bold text-slate-800 dark:text-slate-200">Tidak ada data rekonsiliasi</p>
                      <p className="text-xs text-slate-500">Sesuaikan filter status validasi untuk melihat data cabang.</p>
                      <button
                        onClick={() => setFilterStatus("all")}
                        className="text-xs font-bold text-[#2727E6] dark:text-blue-400 underline hover:no-underline"
                      >
                        Reset Filter Status
                      </button>
                    </div>
                  </td>
                </tr>
              ) : (
                filtered.map((item, idx) => {
                  const pct = Math.round((item.actual_revenue / item.expected_revenue) * 100);
                  const isValidated = item.validation_status === "validated";
                  const isDiscrepancy = item.validation_status === "discrepancy";

                  return (
                    <tr
                      key={item.id}
                      className={`hover:bg-slate-50 dark:hover:bg-slate-800/50 transition-colors ${
                        idx % 2 === 0 ? "bg-white dark:bg-slate-900" : "bg-slate-50/50 dark:bg-slate-900/40"
                      }`}
                    >
                    <td className="px-4 py-3">
                      <strong className="text-xs text-slate-900 dark:text-slate-100 block">
                        {item.branch?.branch_name}
                      </strong>
                      {item.branch?.label && (
                        <span className="text-[10px] font-black uppercase px-1.5 py-0.2 rounded bg-blue-100 text-blue-800">
                          {item.branch.label}
                        </span>
                      )}
                    </td>

                    <td className="px-4 py-3 text-slate-600 dark:text-slate-400">
                      <div>{item.branch?.address}</div>
                      <span className="text-[11px] font-mono text-slate-500">WA: {item.branch?.phone_wa}</span>
                    </td>

                    <td className="px-4 py-3 font-bold text-slate-900 dark:text-white">
                      {formatRp(item.expected_revenue)}
                    </td>

                    <td className="px-4 py-3 font-bold text-emerald-600 dark:text-emerald-400">
                      {formatRp(item.actual_revenue)}
                    </td>

                    <td className="px-4 py-3 font-bold">
                      {item.discrepancy > 0 ? (
                        <span className="text-rose-600 dark:text-rose-400">
                          -{formatRp(item.discrepancy)}
                        </span>
                      ) : (
                        <span className="text-emerald-600">Rp 0 (Sesuai)</span>
                      )}
                    </td>

                    <td className="px-4 py-3">
                      <div className="flex items-center gap-2">
                        <span className="font-bold text-slate-800 dark:text-slate-200">{pct}%</span>
                        <div className="w-16 h-2 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                          <div
                            style={{
                              width: `${pct}%`,
                              backgroundColor: pct >= 90 ? "#1EAB55" : pct >= 80 ? "#2727E6" : "#FF6600",
                            }}
                            className="h-full rounded-full"
                          />
                        </div>
                      </div>
                    </td>

                    <td className="px-4 py-3">
                      {isValidated ? (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-black uppercase bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-300">
                          <CheckCircle2 size={11} /> Divalidasi
                        </span>
                      ) : isDiscrepancy ? (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-black uppercase bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border border-rose-300">
                          <AlertCircle size={11} /> Ada Selisih
                        </span>
                      ) : (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-black uppercase bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 border border-amber-300">
                          <Clock size={11} /> Menunggu Cek
                        </span>
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {isValidated ? (
                        <div>
                          <span className="text-[11px] font-semibold text-slate-800 dark:text-slate-200 block">
                            Oleh: {item.validator?.name || "Pak Subagio"}
                          </span>
                          <span className="text-[10px] text-slate-500">Tgl: {item.validated_at}</span>
                        </div>
                      ) : isDiscrepancy ? (
                        <span className="text-[11px] text-rose-600 font-semibold block">
                          {item.notes || "Selisih belum terjelaskan"}
                        </span>
                      ) : (
                        <span className="text-slate-400 text-[11px]">Belum direkonsiliasi</span>
                      )}
                    </td>

                    <td className="px-4 py-3 text-center">
                      <button
                        onClick={() => handleOpenValidation(item)}
                        style={{ border: `1.5px solid ${B}`, boxShadow: "2px 2px 0 0 #111118" }}
                        className="px-3 py-1.5 rounded-lg text-[11px] font-black uppercase bg-[#2727E6] text-white hover:opacity-90 active:translate-y-0.5"
                      >
                        {isValidated ? "Ubah" : "Validasi"}
                      </button>
                    </td>
                  </tr>
                );
              }))}
            </tbody>
          </table>
        </div>
      </div>

      {/* MODAL: FORM VALIDASI REKENING */}
      {selectedForValidation && (
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
              <h3 className="font-heading font-black text-lg text-slate-900 dark:text-white flex items-center gap-2">
                <ShieldCheck size={18} className="text-[#1EAB55]" />
                Rekonsiliasi Bank - {selectedForValidation.branch?.branch_name}
              </h3>
              <button
                onClick={() => setSelectedForValidation(null)}
                className="p-1 rounded-lg border border-slate-300 dark:border-slate-700"
              >
                <X size={16} />
              </button>
            </div>

            <form onSubmit={handleSaveValidation} className="space-y-4 text-xs">
              <div className="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 space-y-2">
                <div className="flex justify-between">
                  <span className="text-slate-500">Cabang:</span>
                  <strong className="text-slate-900 dark:text-white">{selectedForValidation.branch?.branch_name}</strong>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Periode Tagihan:</span>
                  <span className="font-semibold">{selectedForValidation.period_month}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Target Revenue SPP:</span>
                  <span className="font-bold">{formatRp(selectedForValidation.expected_revenue)}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Penerimaan Kasir Aktual:</span>
                  <span className="font-bold text-emerald-600">{formatRp(selectedForValidation.actual_revenue)}</span>
                </div>
                <div className="flex justify-between pt-1 border-t text-slate-700 dark:text-slate-300 font-bold">
                  <span>Selisih:</span>
                  <span className="text-rose-600">{formatRp(selectedForValidation.discrepancy)}</span>
                </div>
              </div>

              <div>
                <label className="font-black uppercase text-slate-600 dark:text-slate-400 block mb-1">
                  Keputusan Validasi Bendahara Pusat:
                </label>
                <select
                  value={actionStatus}
                  onChange={(e) => setActionStatus(e.target.value)}
                  className="w-full p-2.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100 font-bold outline-none"
                >
                  <option value="validated">✅ Cocok / Sudah Divalidasi dengan Rekening BCA</option>
                  <option value="discrepancy">⚠️ Ada Selisih - Perlu Pengecekan Admin Cabang</option>
                  <option value="pending">⏳ Masih Menunggu Mutasi Bank</option>
                </select>
              </div>

              <div>
                <label className="font-black uppercase text-slate-600 dark:text-slate-400 block mb-1">
                  Catatan Rekonsiliasi &amp; No. Mutasi BCA:
                </label>
                <textarea
                  rows={3}
                  placeholder="Contoh: Cocok dengan mutasi rekening koran BCA tanggal 5 Juli 2026 / Mutasi sudah klir."
                  value={validationNote}
                  onChange={(e) => setValidationNote(e.target.value)}
                  className="w-full p-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100 outline-none"
                />
              </div>

              <div className="flex justify-end gap-2 pt-2 border-t">
                <button
                  type="button"
                  onClick={() => setSelectedForValidation(null)}
                  className="px-3 py-2 rounded-lg font-bold border border-slate-300 dark:border-slate-700"
                >
                  Batal
                </button>
                <button
                  type="submit"
                  style={{ border: `2px solid ${B}`, boxShadow: "2px 2px 0 0 #111118" }}
                  className="px-4 py-2 rounded-lg font-black uppercase text-white bg-[#1EAB55] hover:opacity-95"
                >
                  Simpan Hasil Validasi
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
