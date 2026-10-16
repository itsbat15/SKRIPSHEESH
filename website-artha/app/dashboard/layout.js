import DashboardClientWrapper from "@/components/dashboard/DashboardClientWrapper";
import DashboardShell from "@/components/dashboard/DashboardShell";

export const metadata = {
  title: "Dashboard Bimbel Artha",
  description: "Dashboard Manajemen Operasional Bimbel Artha Balikpapan (Frontdesk & Super Admin)",
};

export default function DashboardLayout({ children }) {
  return (
    <DashboardClientWrapper>
      <DashboardShell>{children}</DashboardShell>
    </DashboardClientWrapper>
  );
}
