"use client";
import { usePathname } from "next/navigation";
import Sidebar from "@/components/dashboard/Sidebar";
import Header from "@/components/dashboard/Header";
import SuperAdminSidebar from "@/components/dashboard/SuperAdminSidebar";
import SuperAdminHeader from "@/components/dashboard/SuperAdminHeader";

export default function DashboardShell({ children }) {
  const pathname = usePathname();
  const isSuperAdmin = pathname?.startsWith("/dashboard/superadmin");

  if (isSuperAdmin) {
    return (
      <>
        <SuperAdminSidebar />
        <div className="flex-1 flex flex-col min-h-screen">
          <SuperAdminHeader />
          <main className="flex-1 p-4 lg:p-6">{children}</main>
        </div>
      </>
    );
  }

  return (
    <>
      <Sidebar />
      <div className="flex-1 flex flex-col min-h-screen">
        <Header />
        <main className="flex-1 p-4 lg:p-6">{children}</main>
      </div>
    </>
  );
}
