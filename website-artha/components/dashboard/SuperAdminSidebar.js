"use client";
import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import Image from "next/image";
import {
  LayoutDashboard,
  TrendingUp,
  GraduationCap,
  Building2,
  Database,
  Users,
  ChevronLeft,
  ChevronRight,
  Shield,
  ArrowLeftRight,
  Layers
} from "lucide-react";
import { cn } from "@/lib/utils";
import { ScrollArea } from "@/components/ui/scroll-area";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { useTheme } from "./ThemeProvider";

const superAdminMenuItems = [
  { label: "Executive Overview", href: "/dashboard/superadmin", icon: LayoutDashboard },
  { label: "Monitoring Revenue", href: "/dashboard/superadmin/revenue", icon: TrendingUp },
  { label: "Beban Mengajar Tentor", href: "/dashboard/superadmin/tentor", icon: GraduationCap },
  { label: "Kelola 8 Cabang", href: "/dashboard/superadmin/cabang", icon: Building2 },
  { label: "Master Data & Tarif", href: "/dashboard/superadmin/master", icon: Database },
  { label: "Manajemen Akun", href: "/dashboard/superadmin/users", icon: Users },
];

export default function SuperAdminSidebar() {
  const pathname = usePathname();
  const [collapsed, setCollapsed] = useState(false);
  const { theme } = useTheme();
  const isDark = theme === "dark";

  return (
    <aside
      className={cn(
        "hidden lg:flex flex-col border-r transition-all duration-300 h-screen sticky top-0 z-30",
        collapsed ? "w-[68px]" : "w-64",
        isDark ? "bg-slate-900 border-slate-700" : "bg-white border-slate-200"
      )}
    >
      {/* Brand Header */}
      <div className={`flex items-center gap-3 px-4 py-5 border-b ${isDark ? "border-slate-700" : "border-slate-100"}`}>
        <div className={`relative w-9 h-9 rounded-lg overflow-hidden shrink-0 border-[2px] ${isDark ? "border-slate-600 bg-slate-800" : "border-[#111118] bg-[#2727E6]"} shadow-[2px_2px_0_0_#111118]`}>
          <Image
            src="/images/bimbelarthalogo-1.png"
            alt="Logo"
            fill
            className="object-contain p-1"
            priority
          />
        </div>

        {!collapsed && (
          <div className="flex flex-col overflow-hidden">
            <span className="font-heading font-black text-sm tracking-tight truncate text-slate-900 dark:text-white flex items-center gap-1.5">
              Super Admin <Shield size={13} className="text-indigo-600" />
            </span>
            <span className="text-[10px] font-bold text-indigo-600 dark:text-indigo-400 truncate uppercase tracking-wider">
              Manajemen Pusat (8 Cabang)
            </span>
          </div>
        )}
      </div>

      {/* Navigation */}
      <ScrollArea className="flex-1 py-3">
        <div className="px-2 space-y-1">
          {superAdminMenuItems.map((item) => {
            const Icon = item.icon;
            const isActive = pathname === item.href;

            const linkContent = (
              <Link
                href={item.href}
                className={cn(
                  "flex items-center gap-3 rounded-xl px-3 py-2.5 text-xs font-bold transition-all relative border-[2px]",
                  isActive
                    ? isDark
                      ? "bg-indigo-950 text-indigo-200 border-indigo-500 shadow-[2px_2px_0_0_#6366f1]"
                      : "bg-[#2727E6] text-white border-[#111118] shadow-[3px_3px_0_0_#111118]"
                    : isDark
                    ? "text-slate-400 border-transparent hover:bg-slate-800 hover:text-slate-200"
                    : "text-slate-600 border-transparent hover:bg-slate-100 hover:text-slate-900"
                )}
              >
                <Icon size={17} className="shrink-0" />
                {!collapsed && <span className="truncate">{item.label}</span>}
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

      {/* Footer & Switch to Frontdesk */}
      <div className={`px-3 py-3 border-t space-y-2 ${isDark ? "border-slate-700" : "border-slate-100"}`}>
        {!collapsed ? (
          <Link
            href="/dashboard/frontdesk"
            className="flex items-center gap-2 p-2 rounded-xl text-xs font-black bg-amber-50 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border-2 border-amber-200 dark:border-amber-800 hover:bg-amber-100 transition-colors"
          >
            <ArrowLeftRight size={15} className="text-amber-600 shrink-0" />
            <span>Ke Panel Frontdesk (Artha 1)</span>
          </Link>
        ) : (
          <Tooltip delayDuration={0}>
            <TooltipTrigger asChild>
              <Link
                href="/dashboard/frontdesk"
                className="flex items-center justify-center p-2 rounded-xl text-xs font-black bg-amber-50 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border border-amber-200 hover:bg-amber-100"
              >
                <ArrowLeftRight size={15} />
              </Link>
            </TooltipTrigger>
            <TooltipContent side="right">Ke Panel Frontdesk (Artha 1)</TooltipContent>
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
