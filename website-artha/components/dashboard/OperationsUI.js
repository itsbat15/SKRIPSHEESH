"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";

const inputStyle = "block w-full min-h-10 rounded-lg border border-slate-400 bg-white px-3 py-2 text-sm text-slate-900 focus-visible:outline-2 focus-visible:outline-offset-1 focus-visible:outline-primary dark:border-slate-500 dark:bg-slate-900 dark:text-white";
const interactions = "inline-flex items-center justify-center gap-2 rounded-lg border-2 border-[#111118] px-3.5 py-2 font-bold text-sm shadow-[2px_2px_0_#111118] hover:brightness-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary disabled:opacity-50 disabled:cursor-not-allowed";
export const actionClass = `${interactions} bg-primary text-white`;
export const linkClass = `${interactions} bg-[#FFD600] text-[#111118]`;
export const plainClass = `${interactions} bg-white text-[#111118]`;

export const money = (amount) => new Intl.NumberFormat("id-ID",{style:"currency",currency:"IDR",maximumFractionDigits:0}).format(amount);
export const billKind = (kind) => kind === "registration" ? "Pendaftaran + SPP pertama" : "SPP";
export const paymentNumber = (id) => `ARTHA-${String(id).padStart(6,"0")}`;

export function useMutation(action, after) {
  const router = useRouter();
  const [error,setError] = useState("");
  const [notice,setNotice] = useState("");
  const [busy,setBusy] = useState(false);
  async function submit(event) {
    event.preventDefault();
    if (busy) return;
    setBusy(true);
    setError("");
    setNotice("");
    try {
      const form = event.currentTarget;
      const response = await fetch(`/api/artha/${action}`,{method:"POST",body:new FormData(form)});
      const result = await response.json();
      if (response.status === 401 && action !== "login") {
        window.location.assign("/login");
        return;
      }
      if (!response.ok) throw new Error(result.error || "Permintaan tidak berhasil.");
      if (result.location) {
        window.location.assign(result.location);
        return;
      }
      setNotice("Data berhasil disimpan.");
      after?.(result,form);
      router.refresh();
    } catch (problem) {
      setError(problem.message);
    } finally {
      setBusy(false);
    }
  }
  return {submit,error,notice,busy};
}

export function Feedback({error,notice}) {
  if (error) return <p role="alert" className="rounded-lg bg-rose-50 px-3 py-2 text-sm font-semibold text-rose-800">{error}</p>;
  if (notice) return <p role="status" className="rounded-lg bg-emerald-50 px-3 py-2 text-sm font-semibold text-emerald-800">{notice}</p>;
  return null;
}

export function Submit({busy,children}) {
  return <button type="submit" disabled={busy} className={actionClass}>{busy ? "Memproses…" : children}</button>;
}

export function Field({label,name,options,type="text",required=true,children,...props}) {
  return <label className="grid content-start gap-1.5 text-sm font-semibold">
    <span>{label}</span>
    {options ? <select name={name} required={required} className={inputStyle} {...props}>
      {options.map(([value,title]) => <option key={value} value={value}>{title}</option>)}
    </select> : type === "textarea" ? <textarea name={name} required={required} className={inputStyle} rows={3} {...props} /> :
      <input name={name} type={type} required={required} className={inputStyle} {...props} />}
    {children && <span className="font-normal text-slate-600 dark:text-slate-300">{children}</span>}
  </label>;
}

export function Panel({title,description,actions,children}) {
  return <section className="min-w-0 rounded-2xl border-2 border-[#111118] bg-white shadow-[4px_4px_0_#111118] dark:border-slate-600 dark:bg-slate-900">
    {title && <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-200 px-5 py-4 dark:border-slate-700">
      <div><h2 className="text-lg font-extrabold">{title}</h2>
        {description && <p className="text-sm text-slate-600 dark:text-slate-300">{description}</p>}</div>
      {actions}
    </div>}
    <div className="p-5">{children}</div>
  </section>;
}

export function Table({columns,rows,empty="Belum ada data."}) {
  if (!rows.length) return <p className="rounded-lg bg-slate-100 p-4 text-sm text-slate-700 dark:bg-slate-800 dark:text-slate-200">{empty}</p>;
  return <div className="overflow-x-auto">
    <table className="w-full text-sm">
      <thead className="bg-slate-100 text-left dark:bg-slate-800"><tr>
        {columns.map(([label])=><th key={label} scope="col" className="px-3 py-2.5 font-bold whitespace-nowrap">{label}</th>)}
      </tr></thead>
      <tbody>{rows.map((row)=><tr key={row.id} className="border-b border-slate-200 last:border-0 dark:border-slate-700">
        {columns.map(([label,value])=><td key={label} className="px-3 py-3 align-top">{typeof value === "function" ? value(row) : row[value]}</td>)}
      </tr>)}</tbody>
    </table>
  </div>;
}

const statusStyles = {
  paid:["Lunas","bg-emerald-100 text-emerald-900"],confirmed:["Terkonfirmasi","bg-emerald-100 text-emerald-900"],
  approved:["Disetujui","bg-emerald-100 text-emerald-900"],active:["Aktif","bg-emerald-100 text-emerald-900"],
  overdue:["Terlambat","bg-rose-100 text-rose-900"],rejected:["Ditolak","bg-rose-100 text-rose-900"],
  needs_review:["Perlu ditinjau","bg-rose-100 text-rose-900"],
  pending:["Menunggu validasi","bg-amber-100 text-amber-900"],partial:["Dibayar sebagian","bg-amber-100 text-amber-900"],
  unpaid:["Belum dibayar","bg-slate-100 text-slate-800"],inactive:["Nonaktif","bg-slate-100 text-slate-800"],
  submitted:["Ditutup","bg-blue-100 text-blue-900"],
};

export function Status({value,label}) {
  const [name,style] = statusStyles[value] || [value,"bg-slate-100 text-slate-800"];
  return <span className={`inline-block rounded-full px-2.5 py-1 text-xs font-bold whitespace-nowrap ${style}`}>{label || name}</span>;
}

export function FileLink({href,children}) {
  return <a href={href} target="_blank" rel="noopener noreferrer" className="font-semibold text-primary underline underline-offset-2 dark:text-indigo-300">{children}</a>;
}

export function EditDialog({label,title,description,children}) {
  const [open,setOpen] = useState(false);
  return <Dialog open={open} onOpenChange={setOpen}>
    <DialogTrigger className={plainClass}>{label}</DialogTrigger>
    <DialogContent className="max-h-[90dvh] overflow-y-auto text-slate-900 dark:text-slate-100">
      <DialogHeader><DialogTitle>{title}</DialogTitle><DialogDescription>{description}</DialogDescription></DialogHeader>
      {children(()=>setOpen(false))}
    </DialogContent>
  </Dialog>;
}
