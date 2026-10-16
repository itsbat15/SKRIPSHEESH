"use client";
import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import Image from "next/image";
import {
  LayoutDashboard,
  UserPlus,
  Users,
  CalendarDays,
  CreditCard,
  Receipt,
  BookCopy,
  ChevronLeft,
  ChevronRight,
  LogOut,
  FileText,
  Shield,
} from "lucide-react";
import { cn } from "@/lib/utils";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Button } from "@/components/ui/button";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { useTheme } from "./ThemeProvider";

const menuItems = [
  { label: "Overview", href: "/dashboard/frontdesk", icon: LayoutDashboard },
  { label: "Pendaftaran", href: "/dashboard/frontdesk/pendaftaran", icon: UserPlus },
  { label: "Data Siswa", href: "/dashboard/frontdesk/siswa", icon: Users },
  { label: "Plotting Kelas", href: "/dashboard/frontdesk/kelas", icon: CalendarDays },
  { label: "Kasir SPP", href: "/dashboard/frontdesk/spp", icon: CreditCard },
  { label: "Pengeluaran", href: "/dashboard/frontdesk/pengeluaran", icon: Receipt },
  { label: "Modul Belajar", href: "/dashboard/frontdesk/modul", icon: BookCopy },
  { label: "Laporan Cabang", href: "/dashboard/frontdesk/laporan", icon: FileText },
];

export default function Sidebar() {
  const pathname = usePathname();
  const [collapsed, setCollapsed] = useState(false);
  const { theme } = useTheme();
  const isDark = theme === "dark";

  return (
    <aside
      className={cn(
        "hidden lg:flex flex-col border-r transition-all duration-300 h-screen sticky top-0",
        collapsed ? "w-[68px]" : "w-64",
        isDark
          ? "bg-slate-900 border-slate-700"
          : "bg-white border-slate-200"
      )}
    >
      {/* Logo Header */}
      <div className={`flex items-center gap-3 px-4 py-5 border-b ${isDark ? "border-slate-700" : "border-slate-100"}`}>
        <div className={`relative w-9 h-9 rounded-lg overflow-hidden shrink-0 border-[2px] ${isDark ? "border-slate-600 bg-slate-800" : "border-[#111118] bg-[#FFD600]"} shadow-[2px_2px_0_0_#111118]`}>
          <Image
            src="/images/bimbelarthalogo-1.png"
            alt="Logo"
            fill
            className="object-contain p-0.5"
          />
        </div>
        {!collapsed && (
          <div className="overflow-hidden">
            <p className={`font-heading font-black text-sm truncate ${isDark ? "text-white" : "text-slate-900"}`}>Bimbel Artha</p>
            <p className={`text-[10px] font-medium truncate ${isDark ? "text-slate-400" : "text-slate-500"}`}>Dashboard Frontdesk</p>
          </div>
        )}
      </div>

      {/* Navigation */}
      <ScrollArea className="flex-1 px-3 py-4">
        <div className="space-y-1">
          {!collapsed && (
            <p className={`text-[10px] font-black uppercase tracking-widest px-3 mb-2 ${isDark ? "text-slate-500" : "text-slate-400"}`}>
              Menu Utama
            </p>
          )}
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isActive = pathname === item.href;
            const linkContent = (
              <Link
                key={item.href}
                href={item.href}
                className={cn(
                  "flex items-center gap-3 text-sm font-bold transition-all duration-200 border-[2px]",
                  collapsed ? "justify-center p-3 rounded-xl" : "px-3 py-2.5 rounded-xl",
                  isActive
                    ? "bg-[#2727E6] text-white border-[#111118] shadow-[3px_3px_0_0_#111118] translate-y-0"
                    : isDark
                      ? "text-slate-400 hover:text-white hover:bg-slate-800 border-transparent hover:border-slate-600"
                      : "text-slate-600 hover:text-slate-900 hover:bg-slate-100 border-transparent hover:border-slate-300"
                )}
              >
                <Icon
                  size={18}
                  className={cn(
                    "shrink-0",
                    isActive ? "text-white" : isDark ? "text-slate-500" : "text-slate-400"
                  )}
                />
                {!collapsed && <span>{item.label}</span>}
              </Link>
            );

            if (collapsed) {
              return (
                <Tooltip key={item.href} delayDuration={0}>
                  <TooltipTrigger asChild>{linkContent}</TooltipTrigger>
                  <TooltipContent side="right" sideOffset={10}>
                    {item.label}
                  </TooltipContent>
                </Tooltip>
              );
            }

            return <div key={item.href}>{linkContent}</div>;
          })}
        </div>
      </ScrollArea>

      {/* Footer */}
      <div className={`px-3 py-3 border-t space-y-2 ${isDark ? "border-slate-700" : "border-slate-100"}`}>
        {!collapsed ? (
          <Link
            href="/dashboard/superadmin"
            className="flex items-center gap-2 p-2 rounded-xl text-xs font-black bg-indigo-50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300 border-2 border-indigo-200 dark:border-indigo-800 hover:bg-indigo-100 transition-colors"
          >
            <Shield size={16} className="text-indigo-600 shrink-0" />
            <span>Panel Super Admin (8 Cabang)</span>
          </Link>
        ) : (
          <Tooltip delayDuration={0}>
            <TooltipTrigger asChild>
              <Link
                href="/dashboard/superadmin"
                className="flex items-center justify-center p-2 rounded-xl text-xs font-black bg-indigo-50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300 border border-indigo-200 hover:bg-indigo-100"
              >
                <Shield size={16} />
              </Link>
            </TooltipTrigger>
            <TooltipContent side="right">Panel Super Admin (8 Cabang)</TooltipContent>
          </Tooltip>
        )}

        <Tooltip delayDuration={0}>
          <TooltipTrigger asChild>
            <button
              onClick={() => setCollapsed(!collapsed)}
              className={cn(
                "w-full flex items-center justify-center gap-2 rounded-xl p-2 text-xs font-bold transition-colors border-[2px] border-transparent",
                isDark
                  ? "text-slate-400 hover:bg-slate-800 hover:text-slate-200 hover:border-slate-600"
                  : "text-slate-500 hover:bg-slate-100 hover:text-slate-700 hover:border-slate-200"
              )}
            >
              {collapsed ? <ChevronRight size={18} /> : <ChevronLeft size={18} />}
              {!collapsed && <span>Perkecil Sidebar</span>}
            </button>
          </TooltipTrigger>
          {collapsed && (
            <TooltipContent side="right" sideOffset={10}>
              Perlebar Sidebar
            </TooltipContent>
          )}
        </Tooltip>
      </div>
    </aside>
  );
}
