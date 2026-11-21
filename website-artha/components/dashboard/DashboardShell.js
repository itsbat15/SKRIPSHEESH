"use client";

import Link from "next/link";
import Image from "next/image";
import { BarChart3, BookOpen, Building2, CircleDollarSign, ClipboardCheck, FileCheck2, LayoutDashboard, LogOut, Moon, Sun, UserPlus, Users, Wallet } from "lucide-react";
import { navigation } from "@/lib/artha-navigation";
import { Feedback, useMutation } from "./OperationsUI";
import { useTheme } from "./ThemeProvider";

const icons = {
  "":LayoutDashboard,pendaftaran:UserPlus,siswa:Users,kelas:BookOpen,spp:Wallet,laporan:ClipboardCheck,
  cabang:Building2,users:Users,master:BookOpen,transfer:FileCheck2,revenue:BarChart3,
};

export default function DashboardShell({user,role,active,children}) {
  const logout = useMutation("logout");
  const {theme,toggleTheme} = useTheme();
  const roleName = role === "superadmin" ? "Super Admin" : "Admin Cabang";
  const identity = user.branch_name || "Manajemen Pusat";
  const base = `/dashboard/${role}`;
  return <div className="min-h-screen w-full lg:grid lg:grid-cols-[15rem_minmax(0,1fr)] text-slate-900 dark:text-slate-100">
    <aside className="bg-white border-b-2 border-[#111118] lg:border-b-0 lg:border-r-2 dark:bg-slate-900 dark:border-slate-600">
      <div className="px-5 py-4 lg:py-6 flex items-center gap-3">
        <Image src="/images/bimbelarthalogo-1.png" alt="Bimbel Artha" width={96} height={32} className="object-contain" />
        <span className="rounded-md border-2 border-[#111118] bg-[#FFD600] px-1.5 py-0.5 text-[10px] font-black text-[#111118]">SIMBA</span>
      </div>
      <nav aria-label="Navigasi operasional" className="flex overflow-auto gap-2 px-4 pb-4 lg:grid">
        {navigation[role].map(([key,label])=>{
          const Icon = icons[key] || CircleDollarSign;
          const selected = key === active;
          return <Link key={key} href={key ? `${base}/${key}` : base} aria-current={selected ? "page" : undefined}
            className={`flex shrink-0 items-center gap-3 rounded-lg border-2 px-3 py-2.5 text-sm font-bold whitespace-nowrap focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary ${selected ?
              "border-[#111118] bg-primary text-white shadow-[2px_2px_0_#111118]" :
              "border-transparent text-slate-700 hover:bg-indigo-50 dark:text-slate-200 dark:hover:bg-slate-800"}`}>
            <Icon size={17} aria-hidden="true" /> {label}
          </Link>;
        })}
      </nav>
    </aside>
    <div className="min-w-0">
      <header className="flex flex-wrap items-center justify-between gap-3 bg-primary px-5 py-3 text-white lg:px-7">
        <div><p className="text-xs font-bold uppercase tracking-widest">{roleName}</p><p className="text-lg font-extrabold">{identity}</p></div>
        <div className="flex items-center gap-3">
          <span className="hidden sm:inline text-sm font-bold">{user.name}</span>
          <button type="button" className="rounded border border-white px-2 py-2 hover:bg-white/15" onClick={toggleTheme}
            aria-label={theme === "dark" ? "Gunakan tema terang" : "Gunakan tema gelap"}>
            {theme === "dark" ? <Sun size={16} /> : <Moon size={16} />}
          </button>
          <form onSubmit={logout.submit}>
            <button type="submit" disabled={logout.busy} className="flex items-center gap-2 rounded border border-white px-2.5 py-2 text-xs font-bold hover:bg-white/15">
              <LogOut size={14} aria-hidden="true" /> Keluar
            </button>
          </form>
        </div>
        <Feedback error={logout.error} />
      </header>
      <main className="mx-auto max-w-7xl p-4 sm:p-6 lg:p-7">{children}</main>
    </div>
  </div>;
}
