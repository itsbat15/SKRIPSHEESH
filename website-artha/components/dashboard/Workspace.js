"use client";

import { useEffect, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { accessToken, homeFor, readArtha, workspaceChanged } from "@/lib/artha-client";
import DashboardShell from "./DashboardShell";
import Operations from "./Operations";
import { Feedback } from "./OperationsUI";

export function DashboardEntry() {
  const router = useRouter();
  const [error,setError] = useState("");
  useEffect(()=>{
    const controller = new AbortController();
    if (!accessToken()) router.replace("/login");
    else readArtha("workspace",{signal:controller.signal}).then(
      (data)=>router.replace(homeFor(data.user.role)),
      (problem)=>{
        if (problem.status === 401) router.replace("/login");
        else if (!controller.signal.aborted) setError(problem.message);
      },
    );
    return ()=>controller.abort();
  },[router]);
  return <div className="p-6">{error ? <Feedback error={error} /> : <p role="status">Memeriksa sesi…</p>}</div>;
}

export default function Workspace({role,section,title}) {
  const router = useRouter();
  const query = useSearchParams().toString();
  const [workspace,setWorkspace] = useState(null);
  const [error,setError] = useState("");
  useEffect(()=>{
    const controller = new AbortController();
    let refresh;
    if (!accessToken()) router.replace("/login");
    else {
      refresh = async ()=>{
        try {
          const data = await readArtha("workspace",{signal:controller.signal});
          const home = homeFor(data.user.role);
          if (home !== `/dashboard/${role}`) {
            router.replace(home);
            return;
          }
          let report = null;
          if (role === "superadmin" && ["","revenue"].includes(section)) {
            const filters = new URLSearchParams(query);
            const from = filters.get("from") || (section ? data.today.slice(0,7)+"-01" : data.today);
            const to = filters.get("to") || data.today;
            const branch = filters.get("branch") || "";
            const parameters = new URLSearchParams({from,to,...(branch ? {branch} : {})});
            try {
              report = await readArtha(`reports/revenue?${parameters}`,{signal:controller.signal});
            } catch (problem) {
              if (problem.status !== 422) throw problem;
              report = {from,to,branch,rows:[],error:problem.message};
            }
          }
          if (!controller.signal.aborted) {
            setError("");
            setWorkspace({data,report,role,section});
          }
        } catch (problem) {
          if (controller.signal.aborted) return;
          if (problem.status === 401) router.replace("/login");
          else setError(problem.message);
        }
      };
      window.addEventListener(workspaceChanged,refresh);
      refresh();
    }
    return ()=>{
      controller.abort();
      if (refresh) window.removeEventListener(workspaceChanged,refresh);
    };
  },[role,section,query,router]);

  if (error) return <div className="p-6"><Feedback error={error} /></div>;
  if (workspace?.role !== role || workspace?.section !== section) return <p role="status" className="p-6">Memuat data operasional…</p>;
  const {data,report} = workspace;
  return <DashboardShell user={data.user} role={role} active={section}>
    <Operations key={`${role}/${section}`} role={role} section={section} title={title} data={data} report={report} />
  </DashboardShell>;
}
