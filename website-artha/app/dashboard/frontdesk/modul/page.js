"use client";
import { BookCopy, ArrowDown, Package } from "lucide-react";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";

const modulData = [
  { id: "M001", nama: "Modul Matematika SD Kelas 4-6", program: "SD", stokAwal: 50, terpakai: 38, sisa: 12, status: "Aman" },
  { id: "M002", nama: "Modul IPA SMP Semester 1", program: "SMP", stokAwal: 30, terpakai: 27, sisa: 3, status: "Segera Pesan" },
  { id: "M003", nama: "Modul Matematika SMP", program: "SMP", stokAwal: 35, terpakai: 22, sisa: 13, status: "Aman" },
  { id: "M004", nama: "Modul Fisika SMA", program: "SMA", stokAwal: 25, terpakai: 20, sisa: 5, status: "Segera Pesan" },
  { id: "M005", nama: "Modul Kimia SMA", program: "SMA", stokAwal: 20, terpakai: 12, sisa: 8, status: "Aman" },
  { id: "M006", nama: "Modul Grammar B.Inggris", program: "B.Inggris", stokAwal: 40, terpakai: 35, sisa: 5, status: "Segera Pesan" },
  { id: "M007", nama: "Buku Latihan Calistung", program: "Calistung", stokAwal: 60, terpakai: 44, sisa: 16, status: "Aman" },
  { id: "M008", nama: "Soal Try Out UTBK", program: "SMA", stokAwal: 30, terpakai: 28, sisa: 2, status: "Habis" },
];

const statusStyle = (s) => {
  if (s === "Aman") return { bg: "#1EAB55", fg: "#fff" };
  if (s === "Segera Pesan") return { bg: "#FF6600", fg: "#fff" };
  return { bg: "#E11D48", fg: "#fff" };
};

const programColor = (p) => {
  const m = { "SD": "#2727E6", "SMP": "#1EAB55", "SMA": "#E11D48", "Calistung": "#FF6600", "B.Inggris": "#9333ea" };
  return m[p] || "#64748b";
};

// Card bg per modul (cycling through landing page colors)
const cardBgs = ["#ECEAFC", "#B8F0D8", "#FFBAD2", "#C5E8F7", "#FFD600", "#FFB5A7", "#B8F0D8", "#ECEAFC"];

export default function ModulPage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const db = isDark
    ? { text: "#f1f5f9", muted: "#94a3b8", row1: "#1e293b", row2: "#263148" }
    : { text: "#111118", muted: "#64748b", row1: "rgba(255,255,255,0.6)", row2: "rgba(255,255,255,0.3)" };

  const kpis = [
    { label: "Total Jenis Modul", value: modulData.length, bg: "#2727E6", fg: "#fff" },
    { label: "Stok Aman", value: modulData.filter(m => m.status === "Aman").length, bg: "#1EAB55", fg: "#fff" },
    { label: "Segera Pesan", value: modulData.filter(m => m.status === "Segera Pesan").length, bg: "#FF6600", fg: "#fff" },
    { label: "Stok Habis", value: modulData.filter(m => m.status === "Habis").length, bg: "#E11D48", fg: "#fff" },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="font-heading font-bold text-xl flex items-center gap-2" style={{ color: db.text }}>
          <BookCopy size={22} style={{ color: "#9333ea" }} /> Stok Modul Belajar
        </h2>
        <p className="text-sm mt-0.5" style={{ color: db.muted }}>Pencatatan keluar/masuk modul &amp; buku les cabang</p>
      </div>

      {/* KPI */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {kpis.map((k, i) => (
          <div key={i} style={{ backgroundColor: isDark ? "#1e293b" : k.bg, border: `2.5px solid ${B}`, boxShadow: S }}
            className="rounded-xl p-5 transition-all hover:-translate-y-0.5">
            <p className="text-xs font-bold uppercase tracking-wider mb-1 opacity-75" style={{ color: isDark ? db.muted : k.fg }}>{k.label}</p>
            <p className="font-heading font-black text-3xl" style={{ color: isDark ? db.text : k.fg }}>{k.value}</p>
          </div>
        ))}
      </div>

      {/* Card Grid View */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {modulData.map((m, i) => {
          const pc = programColor(m.program);
          const ss = statusStyle(m.status);
          const pct = Math.round((m.terpakai / m.stokAwal) * 100);
          const barColor = m.status === "Habis" ? "#E11D48" : m.status === "Segera Pesan" ? "#FF6600" : "#1EAB55";
          return (
            <div key={m.id} style={{ backgroundColor: isDark ? "#1e293b" : cardBgs[i % cardBgs.length], border: `2px solid ${B}`, boxShadow: S }}
              className="rounded-xl p-4 transition-all hover:-translate-y-0.5 hover:shadow-[6px_6px_0_0_#111118]">
              <div className="flex items-start justify-between mb-2">
                <span style={{ backgroundColor: pc + "22", color: pc, border: `1.5px solid ${pc}55` }}
                  className="text-[10px] font-black px-2 py-0.5 rounded-md">{m.program}</span>
                <span style={{ backgroundColor: ss.bg, color: ss.fg, border: `1.5px solid ${B}` }}
                  className="text-[9px] font-black px-2 py-0.5 rounded-full">{m.status}</span>
              </div>
              <p className="text-sm font-black leading-tight mb-3" style={{ color: isDark ? db.text : B }}>{m.nama}</p>
              {/* Stock bar */}
              <div className="mb-2">
                <div className="flex justify-between text-[10px] font-bold mb-1" style={{ color: isDark ? db.muted : "#444" }}>
                  <span>Sisa: <strong style={{ color: isDark ? db.text : B }}>{m.sisa}</strong></span>
                  <span>Terpakai: <span style={{ color: barColor }}>{m.terpakai}/{m.stokAwal}</span></span>
                </div>
                <div style={{ backgroundColor: "rgba(0,0,0,0.12)", borderRadius: 99, overflow: "hidden" }} className="h-2 w-full">
                  <div style={{ width: `${pct}%`, backgroundColor: barColor, borderRadius: 99 }} className="h-full transition-all duration-500" />
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Detail Table */}
      <div style={{ backgroundColor: isDark ? "#1e293b" : "#FFD600", border: `2px solid ${B}`, boxShadow: S }} className="rounded-xl p-5">
        <h3 className="font-heading font-black text-base mb-4" style={{ color: isDark ? db.text : B }}>Detail Stok</h3>
        <div style={{ border: `2px solid ${B}`, borderRadius: 10, overflow: "hidden" }}>
          <table className="w-full text-xs">
            <thead>
              <tr style={{ backgroundColor: B }}>
                {["ID", "Nama Modul", "Program", "Stok Awal", "Terpakai", "Sisa", "Status"].map(h => (
                  <th key={h} className="text-left px-4 py-3 font-black uppercase tracking-widest text-white/80">{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {modulData.map((m, i) => {
                const ss = statusStyle(m.status);
                const pc = programColor(m.program);
                return (
                  <tr key={m.id} style={{ backgroundColor: i % 2 === 0 ? (isDark ? db.row1 : "rgba(255,255,255,0.55)") : (isDark ? db.row2 : "rgba(255,255,255,0.25)"), borderTop: i > 0 ? "1px solid rgba(0,0,0,0.07)" : "none" }}>
                    <td className="px-4 py-3 font-mono" style={{ color: db.muted }}>{m.id}</td>
                    <td className="px-4 py-3 font-semibold" style={{ color: isDark ? db.text : B }}>{m.nama}</td>
                    <td className="px-4 py-3">
                      <span style={{ backgroundColor: pc + "22", color: pc, border: `1.5px solid ${pc}55` }} className="text-[10px] font-black px-2 py-0.5 rounded-md">{m.program}</span>
                    </td>
                    <td className="px-4 py-3 text-center font-medium" style={{ color: db.muted }}>{m.stokAwal}</td>
                    <td className="px-4 py-3 text-center">
                      <span className="inline-flex items-center gap-1 font-bold" style={{ color: "#E11D48" }}>
                        <ArrowDown size={11} />{m.terpakai}
                      </span>
                    </td>
                    <td className="px-4 py-3 text-center font-black" style={{ color: isDark ? db.text : B }}>{m.sisa}</td>
                    <td className="px-4 py-3">
                      <span style={{ backgroundColor: ss.bg, color: ss.fg, border: `1.5px solid ${B}` }} className="text-[10px] font-black px-2.5 py-1 rounded-full">{m.status}</span>
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
