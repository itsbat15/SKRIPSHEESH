"use client";
import { useState } from "react";
import { Receipt, Plus, X } from "lucide-react";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { pengeluaranData } from "@/data/mockFrontdeskData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";
const formatRp = (n) => new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", minimumFractionDigits: 0 }).format(n);

const statusStyle = (s) => {
  if (s === "Disetujui") return { bg: "#1EAB55", fg: "#fff" };
  if (s === "Menunggu") return { bg: "#FF6600", fg: "#fff" };
  return { bg: "#E11D48", fg: "#fff" };
};

const kategoriColor = (k) => {
  const m = { "Listrik": "#2727E6", "ATK": "#1EAB55", "Kebersihan": "#FF6600", "AC Service": "#E11D48", "Internet": "#9333ea", "Fotokopi": "#F59E0B", "Lainnya": "#64748b" };
  return m[k] || "#64748b";
};

export default function PengeluaranPage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";
  const [showForm, setShowForm] = useState(false);
  const [form, setForm] = useState({ kategori: "", keterangan: "", nominal: "", tanggal: "" });

  const totalDisetujui = pengeluaranData.filter(p => p.status === "Disetujui").reduce((s, p) => s + p.nominal, 0);
  const totalMenunggu = pengeluaranData.filter(p => p.status === "Menunggu").reduce((s, p) => s + p.nominal, 0);

  const db = isDark
    ? { text: "#f1f5f9", muted: "#94a3b8", row1: "#1e293b", row2: "#263148", formBg: "#0f172a", inputBg: "#1e293b", inputBorder: "#334155" }
    : { text: "#111118", muted: "#64748b", row1: "rgba(255,255,255,0.6)", row2: "rgba(255,255,255,0.3)", formBg: "#fff", inputBg: "#f8fafc", inputBorder: "#e2e8f0" };

  const kpis = [
    { label: "Total Disetujui", value: formatRp(totalDisetujui), bg: "#1EAB55", fg: "#fff", sfg: "#d4fde4" },
    { label: "Menunggu Persetujuan", value: formatRp(totalMenunggu), bg: "#FF6600", fg: "#fff", sfg: "#fff0e6" },
    { label: "Total Klaim", value: formatRp(totalDisetujui + totalMenunggu), bg: "#2727E6", fg: "#fff", sfg: "#c7d2fe" },
  ];

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="font-heading font-bold text-xl flex items-center gap-2" style={{ color: db.text }}>
            <Receipt size={22} style={{ color: "#FF6600" }} /> Pengeluaran Operasional
          </h2>
          <p className="text-sm mt-0.5" style={{ color: db.muted }}>Kelola klaim biaya operasional cabang</p>
        </div>
        <Dialog open={showForm} onOpenChange={setShowForm}>
          <DialogTrigger asChild>
            <button style={{ backgroundColor: "#2727E6", color: "#fff", border: `2px solid ${B}`, boxShadow: S }}
              className="inline-flex items-center gap-2 text-xs font-black uppercase tracking-wide px-4 py-2.5 rounded-lg hover:translate-y-px hover:shadow-none transition-all">
              <Plus size={14} /> Tambah Pengeluaran
            </button>
          </DialogTrigger>
          <DialogContent style={{ backgroundColor: db.formBg, border: `2px solid ${B}` }} className="sm:max-w-[420px]">
            <DialogHeader>
              <DialogTitle className="font-heading font-black" style={{ color: db.text }}>Klaim Pengeluaran Baru</DialogTitle>
            </DialogHeader>
            <form className="space-y-4 mt-2" onSubmit={(e) => { e.preventDefault(); setShowForm(false); }}>
              {[
                { label: "Kategori", field: "kategori", type: "select", opts: ["Listrik","ATK","Kebersihan","AC Service","Internet","Fotokopi","Lainnya"] },
                { label: "Keterangan", field: "keterangan", type: "text", placeholder: "Deskripsi pengeluaran" },
                { label: "Nominal (Rp)", field: "nominal", type: "number", placeholder: "0" },
                { label: "Tanggal", field: "tanggal", type: "date" },
              ].map((f) => (
                <div key={f.field}>
                  <label className="text-xs font-black uppercase tracking-wider mb-1.5 block" style={{ color: db.muted }}>{f.label}</label>
                  {f.type === "select" ? (
                    <Select onValueChange={(v) => setForm(p => ({ ...p, [f.field]: v }))}>
                      <SelectTrigger style={{ backgroundColor: db.inputBg, border: `2px solid ${db.inputBorder}`, color: db.text, fontWeight: 600, fontSize: 13 }}>
                        <SelectValue placeholder="Pilih kategori" />
                      </SelectTrigger>
                      <SelectContent>
                        {f.opts.map(o => <SelectItem key={o} value={o}>{o}</SelectItem>)}
                      </SelectContent>
                    </Select>
                  ) : (
                    <input type={f.type} placeholder={f.placeholder}
                      style={{ backgroundColor: db.inputBg, border: `2px solid ${db.inputBorder}`, color: db.text, borderRadius: 8, padding: "8px 12px", fontSize: 13, width: "100%", outline: "none" }}
                      onChange={(e) => setForm(p => ({ ...p, [f.field]: e.target.value }))} />
                  )}
                </div>
              ))}
              <div style={{ borderTop: `2px solid ${B}`, marginTop: 8, paddingTop: 12 }}>
                <button type="submit" style={{ backgroundColor: "#2727E6", color: "#fff", border: `2px solid ${B}`, boxShadow: S, width: "100%", borderRadius: 8, padding: "10px", fontWeight: 900, fontSize: 13, letterSpacing: "0.05em" }}
                  className="uppercase hover:translate-y-px hover:shadow-none transition-all">Simpan Klaim</button>
              </div>
            </form>
          </DialogContent>
        </Dialog>
      </div>

      {/* KPI */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        {kpis.map((k, i) => (
          <div key={i} style={{ backgroundColor: isDark ? "#1e293b" : k.bg, border: `2.5px solid ${B}`, boxShadow: S }}
            className="rounded-xl p-5 transition-all hover:-translate-y-0.5">
            <p className="text-xs font-bold uppercase tracking-wider mb-1" style={{ color: isDark ? db.muted : k.fg, opacity: 0.8 }}>{k.label}</p>
            <p className="font-heading font-black text-2xl" style={{ color: isDark ? db.text : k.fg }}>{k.value}</p>
          </div>
        ))}
      </div>

      {/* Table */}
      <div style={{ backgroundColor: isDark ? "#1e293b" : "#B8F0D8", border: `2px solid ${B}`, boxShadow: S }} className="rounded-xl p-5">
        <h3 className="font-heading font-black text-base mb-4" style={{ color: isDark ? db.text : B }}>
          Riwayat Pengeluaran ({pengeluaranData.length} klaim)
        </h3>
        <div style={{ border: `2px solid ${B}`, borderRadius: 10, overflow: "hidden" }}>
          <table className="w-full text-xs">
            <thead>
              <tr style={{ backgroundColor: B }}>
                {["ID", "Kategori", "Keterangan", "Nominal", "Tanggal", "Status"].map(h => (
                  <th key={h} className="text-left px-4 py-3 font-black uppercase tracking-widest text-white/80">{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {pengeluaranData.map((p, i) => {
                const ss = statusStyle(p.status);
                const kc = kategoriColor(p.kategori);
                return (
                  <tr key={p.id} style={{ backgroundColor: i % 2 === 0 ? db.row1 : db.row2, borderTop: i > 0 ? "1px solid rgba(0,0,0,0.07)" : "none" }}>
                    <td className="px-4 py-3 font-mono" style={{ color: db.muted }}>{p.id}</td>
                    <td className="px-4 py-3">
                      <span style={{ backgroundColor: kc + "22", color: kc, border: `1.5px solid ${kc}55` }} className="inline-flex px-2 py-0.5 rounded-md text-[10px] font-black">{p.kategori}</span>
                    </td>
                    <td className="px-4 py-3 font-medium" style={{ color: isDark ? db.text : B }}>{p.keterangan}</td>
                    <td className="px-4 py-3 font-bold" style={{ color: isDark ? db.text : B }}>{formatRp(p.nominal)}</td>
                    <td className="px-4 py-3" style={{ color: db.muted }}>{p.tanggal}</td>
                    <td className="px-4 py-3">
                      <span style={{ backgroundColor: ss.bg, color: ss.fg, border: `1.5px solid ${B}` }} className="text-[10px] font-black px-2.5 py-1 rounded-full">{p.status}</span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
