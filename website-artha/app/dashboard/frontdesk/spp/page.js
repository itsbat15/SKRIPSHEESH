"use client";
import { useState, useMemo, useEffect } from "react";
import {
  CreditCard,
  MessageCircle,
  Filter,
  CheckCircle,
  AlertCircle,
  Clock,
  Printer,
  Receipt,
  Search,
  Building2,
  Send,
  X,
  FileCheck,
  Check
} from "lucide-react";
import {
  bills,
  payments,
  students,
  cabangInfo,
  feeTariffs
} from "@/data/mockFrontdeskData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";

const formatRp = (n) =>
  new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", minimumFractionDigits: 0 }).format(n || 0);

export default function SPPPage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const [activeBills, setActiveBills] = useState(bills);
  const [activePayments, setActivePayments] = useState(payments);

  const [filterStatus, setFilterStatus] = useState("all");
  const [filterJenjang, setFilterJenjang] = useState("all");
  const [searchQuery, setSearchQuery] = useState("");

  // Payment Form Modal State
  const [payingBill, setPayingBill] = useState(null);
  const [paymentMethod, setPaymentMethod] = useState("cash");
  const [paymentNotes, setPaymentNotes] = useState("");

  // Receipt Modal State
  const [viewingReceipt, setViewingReceipt] = useState(null);

  // Keyboard Escape listener for Accessibility (R-32)
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") {
        if (payingBill) setPayingBill(null);
        if (viewingReceipt) setViewingReceipt(null);
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [payingBill, viewingReceipt]);

  // Map enriched bills
  const enrichedBills = useMemo(() => {
    return activeBills.map((b) => {
      const student = students.find((s) => s.id === b.student_id);
      const payment = activePayments.find((p) => p.bill_id === b.id);

      const monthNames = {
        "2026-07": "Juli 2026",
        "2026-08": "Agustus 2026",
        "2026-09": "September 2026",
        "2026-10": "Oktober 2026",
      };

      return {
        ...b,
        student,
        payment,
        monthName: monthNames[b.bill_period] || b.bill_period,
      };
    });
  }, [activeBills, activePayments]);

  // Filtered bills
  const filtered = useMemo(() => {
    return enrichedBills.filter((b) => {
      if (filterStatus !== "all" && b.payment_status !== filterStatus) return false;
      if (filterJenjang !== "all" && b.student?.grade_level !== filterJenjang) return false;
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        const name = b.student?.full_name?.toLowerCase() || "";
        const reg = b.student?.registration_no?.toLowerCase() || "";
        if (!name.includes(q) && !reg.includes(q)) return false;
      }
      return true;
    });
  }, [enrichedBills, filterStatus, filterJenjang, searchQuery]);

  // KPI Calculations
  const totalLunasAmount = enrichedBills
    .filter((b) => b.payment_status === "paid")
    .reduce((sum, b) => sum + b.total_amount, 0);

  const totalTunggakanAmount = enrichedBills
    .filter((b) => b.payment_status !== "paid")
    .reduce((sum, b) => sum + b.total_amount, 0);

  const totalTargetAmount = totalLunasAmount + totalTunggakanAmount;

  // Handle Pay Action
  const handleExecutePayment = (e) => {
    e.preventDefault();
    if (!payingBill) return;

    const newReceiptNo = `KW-2607-${String(activePayments.length + 1).padStart(3, "0")}`;
    const newPayment = {
      id: activePayments.length + 1,
      bill_id: payingBill.id,
      verified_by_user_id: 1, // Admin Frontdesk
      receipt_no: newReceiptNo,
      amount_paid: payingBill.total_amount,
      payment_method: paymentMethod,
      proof_image_url: null,
      payment_date: new Date().toISOString().split("T")[0],
      verified_at: new Date().toISOString().split("T")[0],
      notes: paymentNotes || (payingBill.discount_amount > 0 ? "Termasuk diskon saudara Rp 200.000" : null),
    };

    // Update state
    setActivePayments([newPayment, ...activePayments]);
    setActiveBills((prev) =>
      prev.map((b) => (b.id === payingBill.id ? { ...b, payment_status: "paid" } : b))
    );

    // Open receipt modal immediately
    const fullReceipt = {
      ...payingBill,
      payment: newPayment,
    };
    setPayingBill(null);
    setViewingReceipt(fullReceipt);
  };

  return (
    <div className="space-y-6">
      {/* Header Info */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div>
          <h2 className="font-heading font-black text-2xl flex items-center gap-2.5" style={{ color: isDark ? "#f1f5f9" : B }}>
            <span className="p-2 rounded-xl bg-[#1EAB55] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]">
              <CreditCard size={20} />
            </span>
            Kasir SPP &amp; Pembayaran
          </h2>
          <p className="text-xs sm:text-sm mt-1" style={{ color: isDark ? "#94a3b8" : "#64748b" }}>
            Pencatatan pembayaran SPP siswa • Pembuatan kuitansi digital &amp; notifikasi WhatsApp otomatis
          </p>
        </div>

        <div className="flex items-center gap-2">
          <span className="text-xs font-bold px-3 py-1.5 rounded-lg bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300 border border-blue-300 dark:border-blue-800 flex items-center gap-1.5">
            <Building2 size={13} /> {cabangInfo.branch_name} • Periode Juli 2026
          </span>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#1EAB55", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-xl p-5 text-white transition-all"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-emerald-100">Total Terbayar (Lunas)</p>
          <p className="font-heading font-black text-2xl sm:text-3xl my-1">{formatRp(totalLunasAmount)}</p>
          <p className="text-xs text-emerald-100 font-semibold">
            {enrichedBills.filter((b) => b.payment_status === "paid").length} siswa telah membayar
          </p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#E11D48", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-xl p-5 text-white transition-all"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-rose-100">Total Tertunggak</p>
          <p className="font-heading font-black text-2xl sm:text-3xl my-1">{formatRp(totalTunggakanAmount)}</p>
          <p className="text-xs text-rose-100 font-semibold">
            {enrichedBills.filter((b) => b.payment_status !== "paid").length} siswa belum bayar / jatuh tempo
          </p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#2727E6", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-xl p-5 text-white transition-all"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-blue-100">Target Penerimaan SPP</p>
          <p className="font-heading font-black text-2xl sm:text-3xl my-1">{formatRp(totalTargetAmount)}</p>
          <p className="text-xs text-blue-100 font-semibold">
            Total {enrichedBills.length} tagihan terbit bulan Juli 2026
          </p>
        </div>
      </div>

      {/* Rekening Resmi Bimbel Banner */}
      <div className="p-4 rounded-xl bg-amber-50 dark:bg-amber-950/40 border-2 border-amber-300 dark:border-amber-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 text-xs">
        <div className="space-y-0.5">
          <span className="font-black uppercase tracking-wide text-amber-900 dark:text-amber-200 block">
            Rekening Resmi Pembayaran SPP Bimbel Artha
          </span>
          <p className="text-slate-600 dark:text-slate-300">
            Bank BCA: <strong className="font-mono text-slate-900 dark:text-white">024-9988-771</strong> a/n Bimbel Artha Mandiri
          </p>
        </div>
        <span className="text-[11px] font-bold px-2.5 py-1 rounded bg-amber-200 dark:bg-amber-900 text-amber-900 dark:text-amber-100 shrink-0">
          Semua transfer langsung ke Rekening Pusat
        </span>
      </div>

      {/* Filter and Search Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 bg-white dark:bg-slate-900 p-3.5 rounded-xl border-2 border-[#111118]">
        {/* Search */}
        <div className="relative flex-1 min-w-[220px]">
          <Search size={15} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            type="text"
            placeholder="Cari nama siswa atau no. registrasi..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-3 py-2 rounded-lg text-xs font-medium border-2 border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 outline-none"
          />
        </div>

        {/* Filter Status Tabs */}
        <div className="flex items-center gap-1.5 flex-wrap">
          {[
            { id: "all", label: "Semua Tagihan" },
            { id: "unpaid", label: "Belum Bayar" },
            { id: "overdue", label: "Jatuh Tempo" },
            { id: "paid", label: "Lunas" },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setFilterStatus(tab.id)}
              className={`px-3 py-1.5 rounded-lg text-xs font-black uppercase transition-all ${
                filterStatus === tab.id
                  ? "bg-[#111118] text-white shadow-[2px_2px_0_0_#2727E6]"
                  : "bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* Jenjang Filter */}
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
      </div>

      {/* Table Tagihan & Pembayaran */}
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
            Daftar Tagihan SPP Siswa ({filtered.length} data)
          </h3>
          <span className="text-xs text-slate-500 font-bold">Periode: Juli 2026</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              <tr className="bg-[#111118] text-white/80">
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">No. Reg / Siswa</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Jenjang &amp; Kelas</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Periode</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Tarif Pokok</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Potongan</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Total Tagihan</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Status</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Metode</th>
                <th className="text-center px-4 py-3 font-black uppercase tracking-wider">Aksi Kasir</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200 dark:divide-slate-800">
              {filtered.length === 0 ? (
                <tr>
                  <td colSpan={9} className="px-4 py-8 text-center text-slate-600 dark:text-slate-300 font-semibold">
                    Tidak ada data tagihan SPP yang sesuai dengan filter atau kata kunci pencarian.
                  </td>
                </tr>
              ) : (
                filtered.map((item, idx) => {
                  const isPaid = item.payment_status === "paid";
                  const isOverdue = item.payment_status === "overdue";

                  return (
                    <tr
                      key={item.id}
                      className={`hover:bg-slate-50 dark:hover:bg-slate-800/50 transition-colors ${
                        idx % 2 === 0 ? "bg-white dark:bg-slate-900" : "bg-slate-50/50 dark:bg-slate-900/40"
                      }`}
                    >
                      <td className="px-4 py-3">
                        <div className="font-mono text-[10px] text-slate-500 dark:text-slate-400">
                          {item.student?.registration_no || `ID #${item.id}`}
                        </div>
                        <strong className="text-xs text-slate-900 dark:text-slate-100 block">
                          {item.student?.full_name || "-"}
                        </strong>
                        <span className="text-[11px] text-slate-600 dark:text-slate-400">Wali: {item.student?.parent_name}</span>
                      </td>

                      <td className="px-4 py-3">
                        <span className="font-bold text-slate-800 dark:text-slate-200">
                          {item.student?.grade_level === "TK"
                            ? "TK (Calistung)"
                            : `${item.student?.grade_level} Kelas ${item.student?.class_grade}`}
                        </span>
                        <span className="block text-[11px] text-slate-500 dark:text-slate-400">{item.student?.school_origin}</span>
                      </td>

                      <td className="px-4 py-3 text-slate-700 dark:text-slate-300 font-medium">
                        {item.monthName}
                      </td>

                      <td className="px-4 py-3 font-medium text-slate-700 dark:text-slate-300">
                        {formatRp(item.base_amount)}
                      </td>

                      <td className="px-4 py-3">
                        {item.discount_amount > 0 ? (
                          <span className="text-[11px] font-black text-green-600 dark:text-green-400">
                            -{formatRp(item.discount_amount)} (Kakak-Adik)
                          </span>
                        ) : (
                          <span className="text-slate-500 dark:text-slate-400 font-bold">-</span>
                        )}
                      </td>

                      <td className="px-4 py-3 font-black text-slate-900 dark:text-white">
                        {formatRp(item.total_amount)}
                      </td>

                      <td className="px-4 py-3">
                        {isPaid ? (
                          <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-black uppercase bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-800">
                            <CheckCircle size={10} /> Lunas
                          </span>
                        ) : isOverdue ? (
                          <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-black uppercase bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border border-rose-300 dark:border-rose-800">
                            <AlertCircle size={10} /> Jatuh Tempo
                          </span>
                        ) : (
                          <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-black uppercase bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 border border-amber-300 dark:border-amber-800">
                            <Clock size={10} /> Belum Bayar
                          </span>
                        )}
                      </td>

                      <td className="px-4 py-3 text-slate-700 dark:text-slate-300 capitalize font-medium">
                        {item.payment
                          ? item.payment.payment_method === "cash"
                            ? "Tunai"
                            : item.payment.payment_method === "bank_transfer"
                            ? "Transfer"
                            : "QRIS"
                          : "-"}
                      </td>

                      <td className="px-4 py-3 text-center">
                        {!isPaid ? (
                          <div className="flex items-center justify-center gap-1.5">
                            <button
                              onClick={() => setPayingBill(item)}
                              style={{ border: `1.5px solid ${B}`, boxShadow: "2px 2px 0 0 #111118" }}
                              className="px-2.5 py-1 rounded-md text-[11px] font-black uppercase bg-[#1EAB55] text-white hover:opacity-90 active:translate-y-0.5"
                            >
                              Bayar
                            </button>
                            <button
                              onClick={() => {
                                const msg = encodeURIComponent(
                                  `Halo Bapak/Ibu ${item.student?.parent_name}, mengingatkan tagihan SPP ${item.monthName} ananda ${item.student?.full_name} sebesar ${formatRp(item.total_amount)} jatuh tempo tanggal ${item.due_date}. Pembayaran dapat melalui transfer BCA: 024-9988-771 a/n Bimbel Artha Mandiri. Terima kasih.`
                                );
                                window.open(
                                  `https://wa.me/${item.student?.parent_phone_wa?.replace(/[^0-9]/g, "")}?text=${msg}`,
                                  "_blank"
                                );
                              }}
                              title="Kirim Pengingat WhatsApp"
                              style={{ border: `1.5px solid ${B}` }}
                              className="p-1 rounded-md bg-[#25D366] text-white hover:opacity-90"
                            >
                              <MessageCircle size={14} />
                            </button>
                          </div>
                        ) : (
                          <div className="flex items-center justify-center gap-1.5">
                            <button
                              onClick={() => setViewingReceipt(item)}
                              style={{ border: `1.5px solid ${B}` }}
                              className="px-2.5 py-1 rounded-md text-[11px] font-bold bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:bg-slate-200 flex items-center gap-1"
                            >
                              <Receipt size={12} /> Kuitansi
                            </button>
                          </div>
                        )}
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* MODAL: FORM PEMBAYARAN KASIR */}
      {payingBill && (
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
                <CreditCard size={18} className="text-[#1EAB55]" />
                Input Pembayaran SPP
              </h3>
              <button
                onClick={() => setPayingBill(null)}
                className="p-1 rounded-lg border border-slate-300 dark:border-slate-700"
              >
                <X size={16} />
              </button>
            </div>

            <form onSubmit={handleExecutePayment} className="space-y-4 text-xs">
              <div className="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 space-y-1.5">
                <div className="flex justify-between">
                  <span className="text-slate-500">Nama Siswa:</span>
                  <strong className="text-slate-900 dark:text-white">{payingBill.student?.full_name}</strong>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Bulan Periode:</span>
                  <span className="font-semibold">{payingBill.monthName}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Tarif Pokok:</span>
                  <span>{formatRp(payingBill.base_amount)}</span>
                </div>
                {payingBill.discount_amount > 0 && (
                  <div className="flex justify-between text-green-600 font-bold">
                    <span>Diskon Kakak-Adik:</span>
                    <span>-{formatRp(payingBill.discount_amount)}</span>
                  </div>
                )}
                <div className="flex justify-between pt-1 border-t text-sm font-black text-slate-900 dark:text-white">
                  <span>Total Bayar:</span>
                  <span className="text-[#1EAB55]">{formatRp(payingBill.total_amount)}</span>
                </div>
              </div>

              <div>
                <label className="font-black uppercase text-slate-500 block mb-1">
                  Metode Pembayaran Kasir:
                </label>
                <select
                  value={paymentMethod}
                  onChange={(e) => setPaymentMethod(e.target.value)}
                  className="w-full p-2.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100 font-semibold outline-none"
                >
                  <option value="cash">Tunai (Diterima Langsung di Kasir)</option>
                  <option value="bank_transfer">Transfer Bank BCA (024-9988-771)</option>
                  <option value="qris">QRIS Bimbel Artha</option>
                </select>
              </div>

              <div>
                <label className="font-black uppercase text-slate-500 block mb-1">
                  Catatan Transaksi:
                </label>
                <input
                  type="text"
                  placeholder="Contoh: Diterima oleh Siti / Mutasi BCA dicek"
                  value={paymentNotes}
                  onChange={(e) => setPaymentNotes(e.target.value)}
                  className="w-full p-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100 outline-none"
                />
              </div>

              <div className="flex justify-end gap-2 pt-2 border-t">
                <button
                  type="button"
                  onClick={() => setPayingBill(null)}
                  className="px-3 py-2 rounded-lg font-bold border border-slate-300 dark:border-slate-700"
                >
                  Batal
                </button>
                <button
                  type="submit"
                  style={{ border: `2px solid ${B}`, boxShadow: "2px 2px 0 0 #111118" }}
                  className="px-4 py-2 rounded-lg font-black uppercase text-white bg-[#1EAB55] hover:opacity-95"
                >
                  Konfirmasi Pembayaran
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* MODAL: KUITANSI RESMI PEMBAYARAN */}
      {viewingReceipt && (
        <div className="fixed inset-0 z-50 bg-black/60 flex items-center justify-center p-4">
          <div
            style={{
              backgroundColor: isDark ? "#1e293b" : "#fff",
              border: `3px solid ${B}`,
              boxShadow: "6px 6px 0 0 #111118",
            }}
            className="w-full max-w-lg rounded-2xl p-6 sm:p-8 space-y-4 animate-in fade-in"
          >
            {/* Header Kuitansi */}
            <div className="flex items-center justify-between border-b-2 border-dashed border-slate-300 dark:border-slate-700 pb-4">
              <div>
                <span className="text-[10px] font-black uppercase tracking-wider px-2 py-0.5 rounded bg-emerald-100 text-emerald-800">
                  Kuitansi Resmi SPP
                </span>
                <h3 className="font-heading font-black text-xl text-slate-900 dark:text-white mt-1">
                  Bimbel Artha {cabangInfo.branch_name}
                </h3>
                <p className="text-[11px] text-slate-500">{cabangInfo.address} • Telp/WA: {cabangInfo.phone_wa}</p>
              </div>
              <div className="text-right">
                <span className="text-[10px] text-slate-400 font-bold block uppercase">No. Kuitansi</span>
                <span className="font-mono font-black text-sm px-2 py-0.5 bg-yellow-300 text-slate-900 rounded border border-slate-800">
                  {viewingReceipt.payment?.receipt_no || "KW-2607-001"}
                </span>
              </div>
            </div>

            {/* Rincian Kuitansi */}
            <div className="space-y-2.5 text-xs">
              <div className="flex justify-between py-1 border-b border-slate-100 dark:border-slate-800">
                <span className="text-slate-500">Telah Terima Dari:</span>
                <strong className="text-slate-900 dark:text-white">
                  {viewingReceipt.student?.parent_name} (Wali {viewingReceipt.student?.full_name})
                </strong>
              </div>
              <div className="flex justify-between py-1 border-b border-slate-100 dark:border-slate-800">
                <span className="text-slate-500">No. Registrasi Siswa:</span>
                <span className="font-mono">{viewingReceipt.student?.registration_no}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-slate-100 dark:border-slate-800">
                <span className="text-slate-500">Untuk Pembayaran:</span>
                <span className="font-bold">
                  SPP Bulan {viewingReceipt.monthName} ({viewingReceipt.student?.grade_level} Kelas {viewingReceipt.student?.class_grade})
                </span>
              </div>
              <div className="flex justify-between py-1 border-b border-slate-100 dark:border-slate-800">
                <span className="text-slate-500">Metode Pembayaran:</span>
                <span className="font-semibold uppercase">{viewingReceipt.payment?.payment_method || "Tunai"}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-slate-100 dark:border-slate-800">
                <span className="text-slate-500">Tanggal Pembayaran:</span>
                <span>{viewingReceipt.payment?.payment_date || "2026-07-05"}</span>
              </div>
              {viewingReceipt.discount_amount > 0 && (
                <div className="flex justify-between py-1 text-green-600 font-semibold">
                  <span>Potongan Diskon Saudara Kandung:</span>
                  <span>-{formatRp(viewingReceipt.discount_amount)}</span>
                </div>
              )}
              <div className="flex justify-between p-3 rounded-xl bg-slate-100 dark:bg-slate-800/80 font-black text-sm text-slate-900 dark:text-white mt-2">
                <span>Jumlah Lunas:</span>
                <span className="text-base text-emerald-600 dark:text-emerald-400">
                  {formatRp(viewingReceipt.total_amount)}
                </span>
              </div>
            </div>

            {/* Footer & Actions */}
            <div className="pt-3 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-2">
              <button
                onClick={() => setViewingReceipt(null)}
                style={{ border: `1.5px solid ${B}` }}
                className="px-3 py-2 rounded-lg text-xs font-bold bg-white text-slate-800 hover:bg-slate-100"
              >
                Tutup
              </button>

              <div className="flex gap-2">
                <button
                  onClick={() => {
                    const msg = encodeURIComponent(
                      `Kuitansi Pembayaran SPP Bimbel Artha:\nNo: ${viewingReceipt.payment?.receipt_no}\nSiswa: ${viewingReceipt.student?.full_name}\nBulan: ${viewingReceipt.monthName}\nJumlah: ${formatRp(viewingReceipt.total_amount)}\nStatus: LUNAS\nTerima kasih atas pembayarannya!`
                    );
                    window.open(
                      `https://wa.me/${viewingReceipt.student?.parent_phone_wa?.replace(/[^0-9]/g, "")}?text=${msg}`,
                      "_blank"
                    );
                  }}
                  style={{ border: `1.5px solid ${B}`, boxShadow: "2px 2px 0 0 #111118" }}
                  className="px-3 py-2 rounded-lg text-xs font-black uppercase tracking-wide bg-[#25D366] text-white flex items-center gap-1.5 hover:opacity-90"
                >
                  <Send size={13} /> Kirim WhatsApp
                </button>
                <button
                  onClick={() => window.print()}
                  style={{ border: `1.5px solid ${B}`, boxShadow: "2px 2px 0 0 #111118" }}
                  className="px-4 py-2 rounded-lg text-xs font-black uppercase tracking-wide bg-[#FFD600] text-slate-900 flex items-center gap-1.5 hover:opacity-90"
                >
                  <Printer size={13} /> Cetak Kuitansi
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
