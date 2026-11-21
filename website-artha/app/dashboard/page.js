import { redirect } from "next/navigation";
import { dashboardFor, requireDashboardUser } from "@/lib/artha-session";

export default async function DashboardPage() {
  redirect(dashboardFor(await requireDashboardUser()));
}
