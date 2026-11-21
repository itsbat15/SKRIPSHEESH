import { Suspense } from "react";
import { notFound } from "next/navigation";
import { navigation } from "@/lib/artha-navigation";
import Workspace from "@/components/dashboard/Workspace";

export default async function DashboardPage({params}) {
  const {role,module: parts = []} = await params;
  if (!Object.hasOwn(navigation,role)) notFound();
  const section = parts[0] || "";
  const item = navigation[role].find(([key]) => key === section);
  if (parts.length>1 || !item) notFound();
  return <Suspense fallback={<p role="status" className="p-6">Memuat data operasional…</p>}>
    <Workspace role={role} section={section} title={item[1]} />
  </Suspense>;
}
