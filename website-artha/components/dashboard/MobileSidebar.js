"use client";
import Link from "next/link";
import Image from "next/image";
import { usePathname } from "next/navigation";
import {
  LayoutDashboard, UserPlus, Users, CalendarDays, CreditCard, Receipt, BookCopy,
} from "lucide-react";
import { cn } from "@/lib/utils";
import { ScrollArea } from "@/components/ui/scroll-area";

const menuItems = [
  { label: "Overview", href: "/dashboard/frontdesk", icon: LayoutDashboard },
  { label: "Pendaftaran", href: "/dashboard/frontdesk/pendaftaran", icon: UserPlus },
  { label: "Data Siswa", href: "/dashboard/frontdesk/siswa", icon: Users },
  { label: "Plotting Kelas", href: "/dashboard/frontdesk/kelas", icon: CalendarDays },
  { label: "Kasir SPP", href: "/dashboard/frontdesk/spp", icon: CreditCard },
  { label: "Pengeluaran", href: "/dashboard/frontdesk/pengeluaran", icon: Receipt },
  { label: "Modul Belajar", href: "/dashboard/frontdesk/modul", icon: BookCopy },
];

export default function MobileSidebar() {
  const pathname = usePathname();

  return (
    <div className="flex flex-col h-full bg-white">
      <div className="flex items-center gap-3 px-4 py-5 border-b border-slate-100">
        <div className="relative w-9 h-9 rounded-lg overflow-hidden">
          <Image src="/images/bimbelarthalogo-1.png" alt="Logo" fill className="object-contain p-0.5" />
        </div>
        <div>
          <p className="font-heading font-bold text-sm text-slate-900">Bimbel Artha</p>
          <p className="text-[10px] text-slate-500">Dashboard Admin</p>
        </div>
      </div>
      <ScrollArea className="flex-1 px-3 py-4">
        <p className="text-[10px] font-semibold text-slate-400 uppercase tracking-wider px-3 mb-2">
          Menu Frontdesk
        </p>
        <div className="space-y-1">
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isActive = pathname === item.href;
            return (
              <Link
                key={item.href}
                href={item.href}
                className={cn(
                  "flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-all",
                  isActive
                    ? "bg-primary text-white shadow-md shadow-primary/25"
                    : "text-slate-600 hover:bg-slate-100"
                )}
              >
                <Icon size={18} className={cn(isActive ? "text-white" : "text-slate-400")} />
                {item.label}
              </Link>
            );
          })}
        </div>
      </ScrollArea>
    </div>
  );
}
