"use client";
import { Bell, Search, Menu, Sun, Moon } from "lucide-react";
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
import { cabangInfo } from "@/data/mockFrontdeskData";
import MobileSidebar from "./MobileSidebar";
import { useTheme } from "./ThemeProvider";

export default function Header() {
  const { theme, toggleTheme } = useTheme();
  const isDark = theme === "dark";

  return (
    <header className={`sticky top-0 z-40 border-b px-4 lg:px-6 py-3 transition-colors duration-300 ${isDark ? "bg-slate-900 border-slate-700" : "bg-white border-slate-200"}`}>
      <div className="flex items-center justify-between gap-4">
        {/* Mobile menu */}
        <Sheet>
          <SheetTrigger asChild>
            <Button variant="ghost" size="icon" className="lg:hidden">
              <Menu size={20} />
            </Button>
          </SheetTrigger>
          <SheetContent side="left" className="p-0 w-64">
            <MobileSidebar />
          </SheetContent>
        </Sheet>

        {/* Page Title & Cabang */}
        <div className="hidden lg:block">
          <h1 className={`font-heading font-bold text-lg ${isDark ? "text-white" : "text-slate-900"}`}>
            Dashboard Frontdesk
          </h1>
          <p className={`text-xs ${isDark ? "text-slate-400" : "text-slate-500"}`}>
            {cabangInfo.name} ({cabangInfo.label}) — {cabangInfo.address}
          </p>
        </div>

        {/* Search */}
        <div className="flex-1 max-w-md hidden md:block">
          <div className="relative">
            <Search size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
            <Input
              placeholder="Cari siswa, kelas, atau tagihan..."
              className={`pl-9 rounded-lg h-9 text-sm border ${isDark ? "bg-slate-800 border-slate-600 text-white placeholder:text-slate-500 focus:border-slate-400" : "bg-slate-50 border-slate-200 focus:border-slate-400"}`}
            />
          </div>
        </div>

        {/* Right Actions */}
        <div className="flex items-center gap-2">
          {/* Theme Toggle */}
          <button
            onClick={toggleTheme}
            className={`relative h-8 w-14 rounded-full border transition-all duration-300 flex items-center px-1 ${isDark ? "bg-slate-700 border-slate-600" : "bg-slate-200 border-slate-300"}`}
            aria-label="Toggle theme"
          >
            <span className={`absolute flex items-center justify-center w-6 h-6 rounded-full shadow-sm transition-all duration-300 ${isDark ? "translate-x-6 bg-slate-900" : "translate-x-0 bg-white"}`}>
              {isDark ? <Moon size={12} className="text-blue-400" /> : <Sun size={12} className="text-amber-500" />}
            </span>
          </button>

          {/* Notifications */}
          <Button variant="ghost" size="icon" className="relative">
            <Bell size={18} className={isDark ? "text-slate-300" : "text-slate-600"} />
            <span className="absolute -top-0.5 -right-0.5 h-4 min-w-4 px-1 text-[9px] bg-red-500 text-white rounded-full flex items-center justify-center font-bold">
              3
            </span>
          </Button>

          {/* User Menu */}
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <button className={`flex items-center gap-2 rounded-lg p-1.5 transition-colors ${isDark ? "hover:bg-slate-800" : "hover:bg-slate-100"}`}>
                <Avatar className="h-8 w-8">
                  <AvatarFallback className="bg-[#2727E6] text-white text-xs font-black">
                    {cabangInfo.adminName.split(" ").map(n => n[0]).join("")}
                  </AvatarFallback>
                </Avatar>
                <div className="hidden sm:block text-left">
                  <p className={`text-xs font-semibold ${isDark ? "text-white" : "text-slate-900"}`}>{cabangInfo.adminName}</p>
                  <p className={`text-[10px] ${isDark ? "text-slate-400" : "text-slate-500"}`}>Admin {cabangInfo.name}</p>
                </div>
              </button>
            </DropdownMenuTrigger>
            <DropdownMenuContent
              align="end"
              className={`w-48 border shadow-lg ${isDark ? "bg-slate-800 border-slate-700 text-white" : "bg-white border-slate-200 text-slate-900"}`}
            >
              <DropdownMenuLabel className={isDark ? "text-slate-200" : "text-slate-700"}>Akun Saya</DropdownMenuLabel>
              <DropdownMenuSeparator className={isDark ? "bg-slate-700" : "bg-slate-100"} />
              <DropdownMenuItem className={isDark ? "text-slate-200 hover:bg-slate-700 focus:bg-slate-700" : "text-slate-700 hover:bg-slate-50 focus:bg-slate-50"}>Profil</DropdownMenuItem>
              <DropdownMenuItem className={isDark ? "text-slate-200 hover:bg-slate-700 focus:bg-slate-700" : "text-slate-700 hover:bg-slate-50 focus:bg-slate-50"}>Pengaturan</DropdownMenuItem>
              <DropdownMenuSeparator className={isDark ? "bg-slate-700" : "bg-slate-100"} />
              <DropdownMenuItem className="text-red-500 hover:bg-red-50 focus:bg-red-50 font-medium">Keluar</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>
    </header>
  );
}
