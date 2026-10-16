"use client";
import { Bell, Search, Menu, Sun, Moon, Shield, Building2 } from "lucide-react";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import {
  Sheet,
  SheetContent,
  SheetTrigger,
} from "@/components/ui/sheet";
import SuperAdminSidebar from "./SuperAdminSidebar";
import { useTheme } from "./ThemeProvider";

export default function SuperAdminHeader() {
  const { theme, toggleTheme } = useTheme();
  const isDark = theme === "dark";

  return (
    <header className={`sticky top-0 z-20 border-b px-4 lg:px-6 py-3 transition-colors duration-300 ${isDark ? "bg-slate-900 border-slate-700" : "bg-white border-slate-200"}`}>
      <div className="flex items-center justify-between gap-4">
        {/* Mobile menu trigger */}
        <Sheet>
          <SheetTrigger asChild>
            <Button variant="ghost" size="icon" className="lg:hidden">
              <Menu size={20} />
            </Button>
          </SheetTrigger>
          <SheetContent side="left" className="p-0 w-64">
            <SuperAdminSidebar />
          </SheetContent>
        </Sheet>

        {/* Page Title & Badge Pusat */}
        <div className="hidden sm:block">
          <div className="flex items-center gap-2">
            <h1 className={`font-heading font-black text-lg ${isDark ? "text-white" : "text-slate-900"}`}>
              Manajemen Pusat Bimbel Artha
            </h1>
            <span className="px-2 py-0.5 rounded text-[10px] font-black uppercase bg-[#2727E6] text-white">
              Super Admin
            </span>
          </div>
          <p className={`text-xs ${isDark ? "text-slate-400" : "text-slate-500"}`}>
            Monitoring Terpusat 8 Cabang Balikpapan • TA 2026/2027
          </p>
        </div>

        {/* Search */}
        <div className="flex-1 max-w-md hidden md:block">
          <div className="relative">
            <Search size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
            <Input
              placeholder="Cari cabang, tentor, rekening, atau data master..."
              className={`pl-9 rounded-lg h-9 text-xs border ${
                isDark
                  ? "bg-slate-800 border-slate-600 text-white placeholder:text-slate-500"
                  : "bg-slate-50 border-slate-200"
              }`}
            />
          </div>
        </div>

        {/* Right Actions */}
        <div className="flex items-center gap-3">
          {/* Theme Toggle */}
          <button
            onClick={toggleTheme}
            className={`relative h-8 w-14 rounded-full border transition-all duration-300 flex items-center px-1 ${
              isDark ? "bg-slate-700 border-slate-600" : "bg-slate-200 border-slate-300"
            }`}
            aria-label="Toggle theme"
          >
            <div
              className={`h-6 w-6 rounded-full flex items-center justify-center transition-transform duration-300 ${
                isDark ? "translate-x-6 bg-slate-900 text-yellow-400" : "translate-x-0 bg-white text-slate-700 shadow-sm"
              }`}
            >
              {isDark ? <Moon size={13} /> : <Sun size={13} />}
            </div>
          </button>

          {/* Notifications */}
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" size="icon" className="relative">
                <Bell size={18} />
                <span className="absolute -top-0.5 -right-0.5 w-4 h-4 rounded-full bg-[#E11D48] text-[9px] font-black text-white flex items-center justify-center">
                  2
                </span>
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-72">
              <DropdownMenuLabel className="font-heading font-black text-xs">
                Notifikasi Pusat
              </DropdownMenuLabel>
              <DropdownMenuSeparator />
              <DropdownMenuItem className="text-xs flex flex-col items-start gap-1 p-2.5">
                <span className="font-bold text-rose-600">Selisih Revenue Artha 5</span>
                <span className="text-[11px] text-slate-500">Ada selisih Rp 1.300.000 pada tagihan Juli 2026</span>
              </DropdownMenuItem>
              <DropdownMenuItem className="text-xs flex flex-col items-start gap-1 p-2.5">
                <span className="font-bold text-amber-600">Beban Tentor Om Imam Tinggi</span>
                <span className="text-[11px] text-slate-500">Mengajar 28 jam/minggu (indikator kuning)</span>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>

          {/* User Profile */}
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <button className="flex items-center gap-2 pl-2 border-l border-slate-200 dark:border-slate-700 text-left outline-none">
                <Avatar className="h-8 w-8 border-2 border-[#111118]">
                  <AvatarFallback className="bg-[#FFD600] text-slate-900 font-black text-xs">
                    ER
                  </AvatarFallback>
                </Avatar>
                <div className="hidden lg:block">
                  <p className="text-xs font-black text-slate-900 dark:text-white leading-tight">
                    Ibu Emi Ratnawati
                  </p>
                  <p className="text-[10px] text-indigo-600 dark:text-indigo-400 font-bold">
                    Owner / Super Admin
                  </p>
                </div>
              </button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-56">
              <DropdownMenuLabel className="font-heading font-bold text-xs">
                Akun Super Admin
              </DropdownMenuLabel>
              <DropdownMenuSeparator />
              <DropdownMenuItem className="text-xs">Profil Pengguna</DropdownMenuItem>
              <DropdownMenuItem className="text-xs">Pengaturan Sistem</DropdownMenuItem>
              <DropdownMenuSeparator />
              <DropdownMenuItem className="text-xs text-rose-600 font-bold">
                Keluar (Logout)
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>
    </header>
  );
}
