import { notFound } from "next/navigation";
import { getDatabase, today } from "@/lib/artha-db.mjs";
import { revenue, snapshot } from "@/lib/artha-operations.mjs";
import { navigation } from "@/lib/artha-navigation";
import { requireDashboardUser } from "@/lib/artha-session";
import DashboardShell from "@/components/dashboard/DashboardShell";
import Operations from "@/components/dashboard/Operations";

export default async function Workspace({params,searchParams}) {
  const {role,module: parts = []} = await params;
  if (!Object.hasOwn(navigation,role)) notFound();
  const user = await requireDashboardUser(role === "superadmin" ? "super_admin" : "branch_admin");
  const section = parts[0] || "";
  const item = navigation[role].find(([key]) => key === section);
  if (parts.length>1 || !item) notFound();
  const db = getDatabase();
  const data = snapshot(db,user);
  let report = null;
  if (role === "superadmin" && ["","revenue"].includes(section)) {
    const query = await searchParams;
    const day = today();
    const branch = data.branches.some((row) => String(row.id) === query.branch) ? query.branch : "";
    const from = typeof query.from === "string" ? query.from : (section ? day.slice(0,7)+"-01" : day);
    const to = typeof query.to === "string" ? query.to : day;
    try {
      report = {from,to,branch,rows:revenue(db,user,from,to,branch)};
    } catch (error) {
      if (error.status !== 400) throw error;
      report = {from:day.slice(0,7)+"-01",to:day,branch:"",rows:[],error:error.message};
    }
  }
  return <DashboardShell user={user} role={role} active={section}>
    <Operations key={`${role}/${section}`} role={role} section={section} title={item[1]} data={data} report={report} />
  </DashboardShell>;
}
