"use client";
import { TrendingUp, TrendingDown, ArrowUpRight, CalendarCheck, CheckSquare2, Plus, X, ClipboardList, CreditCard, CheckSquare, Zap } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart";
import { AreaChart, Area, XAxis, YAxis, CartesianGrid } from "recharts";
import Link from "next/link";
import { useState } from "react";
import { dashboardStats, siswaData, chartPendaftaran, tagihanSPP } from "@/data/mockFrontdeskData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const jadwalHariIni = [
  { jam: "07.30", kelas: "Matematika 9A", tentor: "Pak Budi", ruang: "R.01", status: "Berlangsung" },
  { jam: "09.00", kelas: "B. Inggris 7B", tentor: "Miss Rina", ruang: "R.02", status: "Berlangsung" },
  { jam: "10.30", kelas: "IPA 8C", tentor: "Bu Sari", ruang: "R.03", status: "Belum Mulai" },
  { jam: "13.00", kelas: "Fisika 12A", tentor: "Pak Arman", ruang: "R.01", status: "Belum Mulai" },
  { jam: "15.00", kelas: "Calistung SD", tentor: "Bu Dewi", ruang: "R.04", status: "Belum Mulai" },
];

const initialTodos = [
  { id: 1, text: "Follow-up 5 siswa tunggakan SPP", done: false },
  { id: 2, text: "Bagikan modul Matematika kelas 9A", done: false },
  { id: 3, text: "Konfirmasi jadwal tryout SNBT", done: true },
  { id: 4, text: "Rekap pendaftaran bulan Juli", done: false },
];

const chartConfig = { pendaftar: { label: "Pendaftar", color: "#2727E6" } };

const quickActions = [
  { label: "Daftarkan Siswa Baru", href: "/dashboard/frontdesk/pendaftaran", icon: ClipboardList, bg: "#2727E6", text: "#fff" },
  { label: "Terima Pembayaran SPP", href: "/dashboard/frontdesk/spp", icon: CreditCard, bg: "#1EAB55", text: "#fff" },
  { label: "Lihat Jadwal Kelas", href: "/dashboard/frontdesk/kelas", icon: CheckSquare, bg: "#FF6600", text: "#fff" },
];

const kpiCards = [
  { label: "Siswa Aktif", getValue: (s) => s.siswaAktif, trend: "+5 dari bulan lalu", trendUp: true, bg: "#FFD600", fg: "#111118", trendFg: "#1a5200" },
  { label: "Pendaftar Baru", getValue: (s) => s.pendaftarBulanIni, trend: "+3 dari bulan lalu", trendUp: true, bg: "#1EAB55", fg: "#ffffff", trendFg: "#d4fde4" },
  { label: "Tunggakan SPP", getValue: (s) => s.tunggakanSPP, trend: "Perlu follow-up!", trendUp: false, bg: "#E11D48", fg: "#ffffff", trendFg: "#fecdd3" },
  { label: "Kelas Aktif", getValue: (s) => `${s.kelasAktif}/${s.totalKelas}`, trend: "2 kelas tersedia", trendUp: true, bg: "#2727E6", fg: "#ffffff", trendFg: "#c7d2fe" },
];

const sppStatus = (status) => {
  if (status === "Jatuh Tempo") return { bg: "#E11D48", fg: "#fff", label: status };
  if (status === "Belum Bayar") return { bg: "#FF6600", fg: "#fff", label: status };
  return { bg: "#1EAB55", fg: "#fff", label: status };
};

const programColor = (prog) => {
  const map = { "SD": "#2727E6", "SMP": "#1EAB55", "SMA": "#E11D48", "Calistung": "#FF6600", "B.Inggris": "#9333ea" };
  return map[prog] || "#64748b";
};

export default function FrontdeskOverview() {
  const { theme } = useTheme();
  const isDark = theme === "dark";
  const recentStudents = siswaData.slice(0, 5);
  const overduePayments = tagihanSPP.filter((t) => t.status !== "Lunas");
  const [todos, setTodos] = useState(initialTodos);
  const [newTodo, setNewTodo] = useState("");

  const toggleTodo = (id) => setTodos(todos.map(t => t.id === id ? { ...t, done: !t.done } : t));
  const addTodo = () => { if (!newTodo.trim()) return; setTodos([...todos, { id: Date.now(), text: newTodo.trim(), done: false }]); setNewTodo(""); };
  const removeTodo = (id) => setTodos(todos.filter(t => t.id !== id));

  const db = isDark ? { bg: "#0f172a", card: "#1e293b", border: "#334155", text: "#f1f5f9", muted: "#94a3b8", row1: "#1e293b", row2: "#263148" }
    : { bg: "#f8fafc", card: "#ffffff", border: "#e2e8f0", text: "#0f172a", muted: "#64748b", row1: "#ffffff", row2: "#f8fafc" };

  // Section background colors (same palette as landing page)
  const sectionColors = {
    chart: isDark ? "#1e293b" : "#ECEAFC",
    todo: isDark ? "#1e293b" : "#FFD600",
    jadwal: isDark ? "#1e293b" : "#B8F0D8",
    tunggakan: isDark ? "#1e293b" : "#FFBAD2",
    siswa: isDark ? "#1e293b" : "#C5E8F7",
    quickAction: isDark ? "#1e293b" : "#FFD600",
  };
  const sectionBorder = "#111118";
  const sectionShadow = "4px 4px 0 0 #111118";

  return (
    <div className="space-y-6">
      {/* Page Title */}
      <div>
        <h2 style={{ color: db.text }} className="font-heading font-bold text-xl">Overview</h2>
        <p style={{ color: db.muted }} className="text-sm mt-0.5">Ringkasan operasional cabang Artha 1 - Juli 2026</p>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {kpiCards.map((k, i) => (
          <div key={i} style={{ backgroundColor: k.bg, border: `2.5px solid ${sectionBorder}`, boxShadow: sectionShadow }}
            className="rounded-xl p-5 transition-all hover:-translate-y-0.5">
            <p style={{ color: k.fg, opacity: 0.75 }} className="text-xs font-bold uppercase tracking-wider mb-1">{k.label}</p>
            <p style={{ color: k.fg }} className="font-heading font-black text-4xl my-1">{k.getValue(dashboardStats)}</p>
            <p style={{ color: k.trendFg }} className="text-xs flex items-center gap-1 font-semibold mt-2">
              {k.trendUp ? <TrendingUp size={12} /> : <TrendingDown size={12} />}{k.trend}
            </p>
          </div>
        ))}
      </div>

      {/* Quick Actions */}
      <div style={{ backgroundColor: sectionColors.quickAction, border: `2px solid ${sectionBorder}`, boxShadow: sectionShadow }} className="rounded-xl p-4">
        <div className="flex items-center gap-2 mb-3">
          <Zap size={14} style={{ color: isDark ? "#fff" : "#111118" }} fill="currentColor" />
          <span style={{ color: isDark ? "#fff" : "#111118" }} className="text-xs font-black uppercase tracking-widest">Aksi Cepat</span>
        </div>
        <div className="flex flex-wrap gap-2">
          {quickActions.map((a) => {
            const Icon = a.icon;
            return (
              <Link key={a.href} href={a.href}
                style={{ backgroundColor: a.bg, color: a.text, border: `2px solid ${sectionBorder}`, boxShadow: "2px 2px 0 0 #111118" }}
                className="inline-flex items-center gap-2 text-xs font-black uppercase tracking-wide px-4 py-2 rounded-lg hover:translate-y-px hover:shadow-none transition-all">
                <Icon size={13} />{a.label}
              </Link>
            );
          })}
        </div>
      </div>

      {/* Chart + Todo */}
      <div className="grid lg:grid-cols-3 gap-5">
        {/* Chart */}
        <div style={{ backgroundColor: sectionColors.chart, border: `2px solid ${sectionBorder}`, boxShadow: sectionShadow }} className="lg:col-span-2 rounded-xl p-5">
          <h3 style={{ color: db.text }} className="font-heading font-black text-base mb-0.5">Tren Pendaftaran 2026</h3>
          <p style={{ color: db.muted }} className="text-xs mb-4">Jumlah pendaftar baru per bulan di cabang Artha 1</p>
          <ChartContainer config={chartConfig} className="h-[220px] w-full">
            <AreaChart data={chartPendaftaran} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke={isDark ? "#334155" : "#c4b5fd"} />
              <XAxis dataKey="bulan" tick={{ fontSize: 11, fill: isDark ? "#94a3b8" : "#4c1d95" }} axisLine={false} tickLine={false} />
              <YAxis tick={{ fontSize: 11, fill: isDark ? "#94a3b8" : "#4c1d95" }} axisLine={false} tickLine={false} />
              <ChartTooltip content={<ChartTooltipContent />} />
              <defs>
                <linearGradient id="fillPendaftar" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#2727E6" stopOpacity={0.35} />
                  <stop offset="95%" stopColor="#2727E6" stopOpacity={0} />
                </linearGradient>
              </defs>
              <Area type="monotone" dataKey="pendaftar" stroke="#2727E6" fill="url(#fillPendaftar)" strokeWidth={2.5} dot={{ fill: "#2727E6", r: 3 }} />
            </AreaChart>
          </ChartContainer>
        </div>

        {/* Todo */}
        <div style={{ backgroundColor: sectionColors.todo, border: `2px solid ${sectionBorder}`, boxShadow: sectionShadow }} className="rounded-xl p-5">
          <div className="flex items-center gap-2 mb-0.5">
            <CheckSquare2 size={16} style={{ color: isDark ? "#fff" : "#111118" }} />
            <h3 style={{ color: isDark ? "#fff" : "#111118" }} className="font-heading font-black text-base">Tugas Hari Ini</h3>
          </div>
          <p style={{ color: isDark ? "#94a3b8" : "#444" }} className="text-xs mb-4">{todos.filter(t => !t.done).length} tugas belum selesai</p>
          <div className="space-y-2 mb-4">
            {todos.map((todo) => (
              <div key={todo.id} style={{ backgroundColor: isDark ? "rgba(255,255,255,0.07)" : "rgba(0,0,0,0.07)", borderRadius: 8 }}
                className="flex items-center gap-2.5 px-3 py-2.5">
                <input type="checkbox" checked={todo.done} onChange={() => toggleTodo(todo.id)}
                  className="accent-[#111118] w-3.5 h-3.5 shrink-0 cursor-pointer" />
                <span style={{ color: isDark ? (todo.done ? "#64748b" : "#f1f5f9") : (todo.done ? "#666" : "#111118") }}
                  className={`text-xs flex-1 font-medium ${todo.done ? "line-through" : ""}`}>{todo.text}</span>
                <button onClick={() => removeTodo(todo.id)} className="opacity-50 hover:opacity-100 transition-opacity">
                  <X size={12} style={{ color: isDark ? "#fff" : "#111118" }} />
                </button>
              </div>
            ))}
          </div>
          <div className="flex gap-2">
            <input type="text" value={newTodo} onChange={(e) => setNewTodo(e.target.value)} onKeyDown={(e) => e.key === "Enter" && addTodo()}
              placeholder="Tambah tugas..."
              style={{ backgroundColor: isDark ? "rgba(255,255,255,0.1)" : "rgba(0,0,0,0.1)", color: isDark ? "#fff" : "#111118", border: `1.5px solid ${sectionBorder}` }}
              className="flex-1 text-xs px-3 py-2 rounded-lg outline-none placeholder:opacity-60" />
            <button onClick={addTodo} style={{ backgroundColor: "#111118", color: "#fff", border: `2px solid ${sectionBorder}` }}
              className="p-2 rounded-lg hover:opacity-80 transition-opacity">
              <Plus size={14} />
            </button>
          </div>
        </div>
      </div>

      {/* Jadwal + Tunggakan */}
      <div className="grid lg:grid-cols-3 gap-5">
        {/* Jadwal */}
        <div style={{ backgroundColor: sectionColors.jadwal, border: `2px solid ${sectionBorder}`, boxShadow: sectionShadow }} className="lg:col-span-2 rounded-xl p-5">
          <div className="flex items-center justify-between mb-4">
            <div>
              <div className="flex items-center gap-2">
                <CalendarCheck size={16} style={{ color: "#111118" }} />
                <h3 style={{ color: isDark ? "#f1f5f9" : "#111118" }} className="font-heading font-black text-base">Jadwal Kelas Hari Ini</h3>
              </div>
              <p style={{ color: isDark ? "#94a3b8" : "#444" }} className="text-xs mt-0.5">
                {new Date().toLocaleDateString("id-ID", { weekday: "long", day: "numeric", month: "long" })}
              </p>
            </div>
            <Link href="/dashboard/frontdesk/kelas"
              style={{ backgroundColor: "#111118", color: "#fff", border: `2px solid ${sectionBorder}`, boxShadow: "2px 2px 0 0 #33333366" }}
              className="inline-flex items-center gap-1.5 text-xs font-bold px-3 py-1.5 rounded-lg hover:opacity-80 transition-opacity">
              Semua Kelas <ArrowUpRight size={12} />
            </Link>
          </div>
          {/* Table */}
          <div style={{ border: `2px solid ${sectionBorder}`, borderRadius: 10, overflow: "hidden" }}>
            <table className="w-full text-xs">
              <thead>
                <tr style={{ backgroundColor: "#111118" }}>
                  {["Jam", "Kelas", "Tentor", "Ruang", "Status"].map((h, i) => (
                    <th key={h} className={`text-left px-4 py-3 font-black uppercase tracking-widest text-white/80 ${i >= 2 && i <= 3 ? "hidden sm:table-cell" : ""}`}>{h}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {jadwalHariIni.map((j, i) => (
                  <tr key={i} style={{ backgroundColor: i % 2 === 0 ? "rgba(255,255,255,0.55)" : "rgba(255,255,255,0.25)", borderTop: i > 0 ? "1px solid rgba(0,0,0,0.08)" : "none" }}>
                    <td className="px-4 py-3 font-mono font-bold" style={{ color: j.status === "Berlangsung" ? "#065f46" : "#555" }}>{j.jam}</td>
                    <td className="px-4 py-3 font-semibold" style={{ color: "#111118" }}>{j.kelas}</td>
                    <td className="px-4 py-3 hidden sm:table-cell" style={{ color: "#444" }}>{j.tentor}</td>
                    <td className="px-4 py-3 hidden sm:table-cell" style={{ color: "#444" }}>{j.ruang}</td>
                    <td className="px-4 py-3">
                      <span style={{
                        backgroundColor: j.status === "Berlangsung" ? "#1EAB55" : "rgba(0,0,0,0.12)",
                        color: j.status === "Berlangsung" ? "#fff" : "#555",
                        border: `1.5px solid ${j.status === "Berlangsung" ? "#157a3c" : "rgba(0,0,0,0.15)"}`,
                      }} className="inline-flex px-2.5 py-1 rounded-full text-[10px] font-bold">
                        {j.status}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Tunggakan SPP */}
        <div style={{ backgroundColor: sectionColors.tunggakan, border: `2px solid ${sectionBorder}`, boxShadow: sectionShadow }} className="rounded-xl p-5">
          <h3 style={{ color: isDark ? "#f1f5f9" : "#111118" }} className="font-heading font-black text-base mb-0.5">Tunggakan SPP</h3>
          <p style={{ color: isDark ? "#94a3b8" : "#555" }} className="text-xs mb-4">{overduePayments.length} siswa perlu follow-up</p>
          <div className="space-y-3">
            {overduePayments.map((t) => {
              const s = sppStatus(t.status);
              return (
                <div key={t.id} className="flex items-center justify-between"
                  style={{ borderBottom: "1px solid rgba(0,0,0,0.1)", paddingBottom: 10 }}>
                  <div>
                    <p style={{ color: isDark ? "#f1f5f9" : "#111118" }} className="text-sm font-bold">{t.namaSiswa}</p>
                    <p style={{ color: isDark ? "#94a3b8" : "#555" }} className="text-xs">{t.program} · {t.bulan}</p>
                  </div>
                  <span style={{ backgroundColor: s.bg, color: s.fg, border: `1.5px solid ${sectionBorder}` }}
                    className="text-[10px] font-black px-2.5 py-1 rounded-full">{s.label}</span>
                </div>
              );
            })}
          </div>
          <Link href="/dashboard/frontdesk/spp"
            style={{ backgroundColor: "#111118", color: "#fff", border: `2px solid ${sectionBorder}`, boxShadow: "2px 2px 0 0 #55555566" }}
            className="mt-4 flex items-center justify-center gap-1.5 w-full text-xs font-bold py-2.5 rounded-lg hover:opacity-80 transition-opacity">
            Lihat Semua Tagihan <ArrowUpRight size={12} />
          </Link>
        </div>
      </div>

      {/* Siswa Terbaru */}
      <div style={{ backgroundColor: sectionColors.siswa, border: `2px solid ${sectionBorder}`, boxShadow: sectionShadow }} className="rounded-xl p-5">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h3 style={{ color: isDark ? "#f1f5f9" : "#111118" }} className="font-heading font-black text-base">Siswa Terbaru</h3>
            <p style={{ color: isDark ? "#94a3b8" : "#444" }} className="text-xs mt-0.5">5 siswa terakhir yang mendaftar</p>
          </div>
          <Link href="/dashboard/frontdesk/siswa"
            style={{ backgroundColor: "#111118", color: "#fff", border: `2px solid ${sectionBorder}`, boxShadow: "2px 2px 0 0 #33333366" }}
            className="inline-flex items-center gap-1.5 text-xs font-bold px-3 py-1.5 rounded-lg hover:opacity-80 transition-opacity">
            Lihat Semua <ArrowUpRight size={12} />
          </Link>
        </div>
        <div style={{ border: `2px solid ${sectionBorder}`, borderRadius: 10, overflow: "hidden" }}>
          <table className="w-full text-xs">
            <thead>
              <tr style={{ backgroundColor: "#111118" }}>
                {[
                  { label: "ID", cls: "" }, { label: "Nama Siswa", cls: "" }, { label: "Program", cls: "" },
                  { label: "Kelas", cls: "hidden md:table-cell" }, { label: "Status SPP", cls: "" },
                  { label: "Tgl Daftar", cls: "hidden sm:table-cell text-right" }
                ].map((h) => (
                  <th key={h.label} className={`text-left px-4 py-3 font-black uppercase tracking-widest text-white/80 ${h.cls}`}>{h.label}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {recentStudents.map((s, i) => {
                const st = sppStatus(s.statusSPP);
                const pc = programColor(s.program);
                return (
                  <tr key={s.id} style={{ backgroundColor: i % 2 === 0 ? "rgba(255,255,255,0.6)" : "rgba(255,255,255,0.3)", borderTop: i > 0 ? "1px solid rgba(0,0,0,0.08)" : "none" }}>
                    <td className="px-4 py-3 font-mono" style={{ color: "#64748b" }}>{s.id}</td>
                    <td className="px-4 py-3 font-bold" style={{ color: "#111118" }}>{s.nama}</td>
                    <td className="px-4 py-3">
                      <span style={{ backgroundColor: pc + "22", color: pc, border: `1.5px solid ${pc}55` }}
                        className="inline-flex px-2.5 py-1 rounded-md text-[10px] font-black">{s.program}</span>
                    </td>
                    <td className="px-4 py-3 hidden md:table-cell" style={{ color: "#555" }}>{s.kelas}</td>
                    <td className="px-4 py-3">
                      <span style={{ backgroundColor: st.bg, color: st.fg, border: `1.5px solid ${sectionBorder}` }}
                        className="text-[10px] font-black px-2.5 py-1 rounded-full">{st.label}</span>
                    </td>
                    <td className="px-4 py-3 text-right hidden sm:table-cell" style={{ color: "#64748b" }}>{s.tanggalDaftar}</td>
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
