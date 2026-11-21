"use client";

import Link from "next/link";
import { ArrowUpRight, CalendarDays, CircleDollarSign, FileCheck2, Users, Wallet } from "lucide-react";
import { Bills, dashboardCash, Reconciliation, Revenue, Transfers } from "./Finance";
import MasterData from "./MasterData";
import { money, Panel } from "./OperationsUI";
import { Groups, PaymentHistory, Registration, Students } from "./Registration";

function Overview({data,report,center}) {
  const sums = dashboardCash(data);
  const outstanding = data.bills.filter((row)=>row.kind==="tuition" && row.overdue);
  const todayPending = data.payments.filter((row)=>row.status==="pending").length;
  const cards = [
    [Users,"Siswa aktif",data.students.filter((row)=>row.status==="active").length],
    [center ? FileCheck2 : Wallet,center ? "Transfer menunggu" : "Tunai hari ini",center ? todayPending : money(sums.cash)],
    [CircleDollarSign,"Transfer hari ini",money(sums.transfer)],
    [CalendarDays,"Tagihan lewat jatuh tempo",outstanding.length],
  ];
  const links = center ?
    [["transfer","Periksa bukti transfer"],["revenue","Laporan keuangan"],["cabang","Kelola kantor cabang"]] :
    [["pendaftaran","Daftarkan siswa baru"],["spp","Catat pembayaran"],["laporan","Rekonsiliasi kas"]];
  return <>
    <section aria-label="Indikator operasional" className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      {cards.map(([Icon,label,value])=><div key={label} className="rounded-xl border-2 border-[#111118] bg-white p-4 shadow-[4px_4px_0_#111118] dark:bg-slate-900 dark:border-slate-600">
        <Icon size={20} className="mb-3 text-primary dark:text-indigo-300" aria-hidden="true" />
        <p className="text-sm font-semibold text-slate-600 dark:text-slate-300">{label}</p>
        <p className="mt-1 text-2xl font-extrabold">{value}</p>
      </div>)}
    </section>
    <Panel title="Akses cepat">
      <div className="flex flex-wrap gap-3">{links.map(([route,label])=><Link key={route}
        href={`/dashboard/${center ? "superadmin" : "frontdesk"}/${route}`}
        className="inline-flex items-center gap-2 rounded-lg border-2 border-[#111118] bg-[#FFD600] px-3 py-2 text-sm font-bold text-[#111118]">
        {label}<ArrowUpRight size={16} aria-hidden="true" />
      </Link>)}</div>
    </Panel>
    {center ? <Revenue data={data} report={report} overview /> :
      <Panel title="Pembayaran terbaru"><PaymentHistory rows={data.payments.slice(0,6)} /></Panel>}
  </>;
}

export default function Operations({role,section,title,data,report}) {
  const center = role==="superadmin";
  let content;
  switch (section) {
    case "pendaftaran": content=<Registration data={data} />; break;
    case "kelas": content=<Groups data={data} />; break;
    case "siswa": content=<><Students data={data} center={center} />{center && <Groups data={data} center />}</>; break;
    case "spp": content=<><Bills data={data} /><Panel title="Riwayat pembayaran" description="Periksa status transfer, alasan penolakan, dan kuitansi yang sudah terbit."><PaymentHistory rows={data.payments} /></Panel></>; break;
    case "laporan": content=<Reconciliation data={data} />; break;
    case "cabang": content=<MasterData type="branch" data={data} />; break;
    case "users": content=<MasterData type="user" data={data} />; break;
    case "master": content=<MasterData type="package" data={data} />; break;
    case "transfer": content=<Transfers data={data} />; break;
    case "revenue": content=<><Revenue data={data} report={report} /><Reconciliation data={data} center /><Bills data={data} center overdueOnly /></>; break;
    default: content=<Overview data={data} report={report} center={center} />;
  }
  return <div className="grid gap-6">
    <div><p className="text-xs font-bold uppercase tracking-widest text-primary dark:text-indigo-300">Operasional · {data.today}</p>
      <h1 className="mt-1 text-3xl font-extrabold tracking-tight sm:text-4xl">{title}</h1></div>
    {content}
  </div>;
}
