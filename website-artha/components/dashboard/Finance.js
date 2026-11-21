"use client";

import { useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import { billKind, EditDialog, Feedback, Field, FileLink, linkClass, money, Panel, paymentNumber, Status, Submit, Table, useMutation } from "./OperationsUI";
import { levelOptions, PaymentFields, PaymentHistory } from "./Registration";

function PayForm({row,day,finish}) {
  const operation = useMutation("pay",finish);
  return <form onSubmit={operation.submit} className="grid gap-3">
    <input type="hidden" name="id" value={row.id} />
    <PaymentFields day={day} max={row.amount-row.paid-row.pending} />
    <Feedback error={operation.error} />
    <Submit busy={operation.busy}>Simpan Pembayaran</Submit>
  </form>;
}

function reminder(row) {
  const phone = row.phone.startsWith("0") ? "62"+row.phone.slice(1) : row.phone;
  const message = `Yth. Bapak/Ibu ${row.guardian}, kami dari Bimbel Artha ${row.branch_name.replace(/^Artha /,"")}. SPP ${row.student_name} periode ${row.period} dengan sisa ${money(row.amount-row.paid)} telah jatuh tempo pada ${row.due_on}. Mohon konfirmasi apabila sudah membayar. Terima kasih.`;
  return `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
}

export function Bills({data,center=false,overdueOnly=false}) {
  const [level,setLevel] = useState("");
  const [group,setGroup] = useState("");
  const [filter,setFilter] = useState(overdueOnly ? "overdue" : "all");
  const [search,setSearch] = useState("");
  const [branch,setBranch] = useState("");
  const rows = data.bills.filter((bill)=>(filter !== "overdue" || (bill.overdue && bill.kind === "tuition")) &&
    (filter !== "open" || bill.paid < bill.amount) && (!group || bill.group_name === group) &&
    (!branch || String(bill.branch_id)===branch) && (!level || bill.level === level) && bill.student_name.toLowerCase().includes(search.toLowerCase()));
  const groups = [...new Set(data.groups.filter((row)=>(!level || row.level===level)&&(!branch || String(row.branch_id)===branch)).map((item)=>item.name))];
  return <Panel title={overdueOnly ? "Tunggakan SPP multicabang" : "Daftar tagihan"} description="Tanggal SPP mengikuti tanggal pendaftaran dan disesuaikan dengan akhir bulan.">
    <div className="mb-4 grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
      <Field label="Cari nama siswa" name="search" type="search" value={search} onChange={(event)=>setSearch(event.target.value)} />
      {center && <Field label="Cabang" name="branch" value={branch} onChange={(event)=>{setBranch(event.target.value);setGroup("");}}
        options={[["","Semua cabang"],...data.branches.map((row)=>[row.id,row.name])]} />}
      <Field label="Jenjang" name="level" options={[["","Semua jenjang"],...levelOptions]} value={level}
        onChange={(event)=>{setLevel(event.target.value);setGroup("");}} />
      <Field label="Kelompok" name="group" options={[["","Semua kelompok"],...groups.map((name)=>[name,name])]} value={group}
        onChange={(event)=>setGroup(event.target.value)} />
      {!overdueOnly && <Field label="Filter tagihan" name="filter" options={[["all","Semua tagihan"],["open","Belum lunas"],["overdue","Tunggakan SPP"]]}
        value={filter} onChange={(event)=>setFilter(event.target.value)} />}
    </div>
    <Table rows={rows} columns={[
      ["Siswa",(row)=><><strong>{row.student_name}</strong><div>{row.level} · {row.group_name}</div></>],
      ...(center ? [["Cabang","branch_name"]] : []),
      ["Tagihan",(row)=><>{billKind(row.kind)}<div>{row.period}</div></>],
      ["Jatuh tempo","due_on"],
      ["Sisa tagihan",(row)=><>{money(row.amount-row.paid)}{row.pending>0 && <div className="text-xs">{money(row.pending)} sedang diverifikasi</div>}</>],
      ["Status",(row)=><><Status value={row.status} />{row.overdue && row.status==="pending" && <div className="mt-1"><Status value="overdue" /></div>}</>],
      ...(!center ? [["Aksi",(row)=><div className="flex flex-wrap items-center gap-3">
        {row.paid+row.pending<row.amount && <EditDialog label="Bayar" title="Catat pembayaran" description={`${row.student_name} | ${billKind(row.kind)} ${row.period}`}>
          {(finish)=><PayForm row={row} day={data.today} finish={finish} />}
        </EditDialog>}
        {row.overdue && row.kind==="tuition" && <FileLink href={reminder(row)}>WhatsApp wali</FileLink>}
      </div>]] : []),
    ]} />
  </Panel>;
}

function ReviewForm({row,finish}) {
  const [decision,setDecision] = useState("approve");
  const operation = useMutation("review-payment",finish);
  return <form onSubmit={operation.submit} className="grid gap-4">
    <input type="hidden" name="id" value={row.id} />
    <div className="grid gap-2 text-sm">
      <p>Pengirim: <strong>{row.sender}</strong></p><p>Tanggal transfer: <strong>{row.transfer_on}</strong></p>
      <p>Nominal: <strong>{money(row.amount)}</strong></p>
      <FileLink href={`/api/artha/proof/${row.id}`}>Buka pratinjau bukti transfer</FileLink>
    </div>
    <Field label="Hasil pemeriksaan" name="decision" value={decision} onChange={(event)=>setDecision(event.target.value)}
      options={[["approve","Konfirmasi pembayaran"],["reject","Tolak bukti transfer"]]} />
    {decision==="reject" && <Field label="Alasan penolakan" name="reason" type="textarea" maxLength={400} />}
    <Feedback error={operation.error} />
    <Submit busy={operation.busy}>Simpan Hasil Pemeriksaan</Submit>
  </form>;
}

export function Transfers({data}) {
  const rows = data.payments.filter((row)=>row.method==="transfer");
  const pending = rows.filter((row)=>row.status==="pending");
  return <>
    <Panel title="Antrean validasi transfer" description="Cocokkan nominal, tanggal, dan pengirim dengan mutasi rekening bank.">
      <Table rows={pending} empty="Tidak ada transfer yang menunggu validasi." columns={[
        ["Nomor",(row)=>paymentNumber(row.id)],["Cabang","branch_name"],["Siswa","student_name"],["Pengirim","sender"],
        ["Tanggal","transfer_on"],["Nominal",(row)=>money(row.amount)],
        ["Pemeriksaan",(row)=><EditDialog label="Periksa" title="Validasi pembayaran transfer" description={`${paymentNumber(row.id)} | ${row.student_name}`}>
          {(finish)=><ReviewForm row={row} finish={finish} />}
        </EditDialog>],
      ]} />
    </Panel>
    <Panel title="Riwayat transfer"><PaymentHistory rows={rows} center /></Panel>
  </>;
}

export function dashboardCash(data, day=data.today) {
  return data.payments.filter((row)=>row.status==="confirmed" && row.recognized_on === day)
    .reduce((acc,row)=>({...acc,[row.method]:acc[row.method]+row.amount}),{cash:0,transfer:0});
}

function CloseForm({cash}) {
  const [physical,setPhysical] = useState("");
  const diff = physical === "" ? null : Number(physical)-cash;
  const operation = useMutation("close-day");
  return <form onSubmit={operation.submit} className="mt-4 grid gap-3">
    <Field label="Uang tunai fisik (Rp)" name="physical" type="number" min={0} value={physical}
      onChange={(event)=>setPhysical(event.target.value)} />
    {diff !== null && <p className={`text-sm font-bold ${diff ? "text-rose-700 dark:text-rose-300" : "text-emerald-800 dark:text-emerald-300"}`}>
      Selisih kas: {money(diff)}{diff !== 0 && " · Catatan wajib diisi."}
    </p>}
    <Field label="Catatan selisih" name="note" type="textarea" maxLength={400} required={diff !== null && diff !== 0} />
    <Feedback error={operation.error} notice={operation.notice} />
    <div><Submit busy={operation.busy}>Tutup Buku Kasir Harian</Submit></div>
  </form>;
}

function ApprovalForm({row,finish}) {
  const operation = useMutation("approve-close",finish);
  return <form onSubmit={operation.submit} className="grid gap-4">
    <input type="hidden" name="id" value={row.id} />
    <p>Selisih: <strong>{money(row.physical-row.cash)}</strong></p>
    <p>Catatan cabang: {row.note || "Tidak ada catatan."}</p>
    <Feedback error={operation.error} />
    <Submit busy={operation.busy}>Setujui Rekonsiliasi</Submit>
  </form>;
}

export function Reconciliation({data,center=false}) {
  const closed = data.reconciliations.find((row)=>row.day===data.today);
  const {cash,transfer} = closed || dashboardCash(data);
  return <>
    {!center && <Panel title={`Kas hari ini · ${data.today}`}
      description="Hitung kas fisik sebelum menutup transaksi tunai hari ini. Transfer baru dibukukan setelah divalidasi.">
      <dl className="grid gap-3 sm:grid-cols-2"><div><dt>Tunai sistem</dt><dd className="text-xl font-extrabold">{money(cash)}</dd></div>
        <div><dt>Transfer terkonfirmasi</dt><dd className="text-xl font-extrabold">{money(transfer)}</dd></div></dl>
      {closed ? <div className="mt-4 flex items-center gap-4"><Status value={closed.status} />
        <FileLink href={`/api/artha/close/${closed.id}`}>Buka berita acara PDF</FileLink></div> :
        <CloseForm cash={cash} />}
    </Panel>}
    <Panel title={center ? "Tutup kas cabang" : "Riwayat tutup kas"} description="Selisih dihitung dari kas fisik dikurangi kas tunai sistem.">
      <Table rows={data.reconciliations} columns={[
        ["Tanggal","day"],...(center ? [["Cabang","branch_name"]] : []),
        ["Tunai",(row)=>money(row.cash)],["Transfer",(row)=>money(row.transfer)],["Kas fisik",(row)=>money(row.physical)],
        ["Selisih",(row)=><span className={row.physical!==row.cash ? "font-bold text-rose-700 dark:text-rose-300" : ""}>{money(row.physical-row.cash)}</span>],
        ["Catatan","note"],["Status",(row)=><Status value={row.status} />],
        ["Aksi",(row)=><div className="grid gap-2 justify-items-start">
          <FileLink href={`/api/artha/close/${row.id}`}>Berita acara PDF</FileLink>
          {center && row.status!=="approved" && <EditDialog label="Tinjau" title="Tinjau rekonsiliasi cabang"
            description={`${row.branch_name} | ${row.day}`}>{(finish)=><ApprovalForm row={row} finish={finish} />}</EditDialog>}
        </div>],
      ]} />
    </Panel>
  </>;
}

export function Revenue({data,report,overview=false}) {
  const {rows,from,to,branch,error} = report;
  const max = Math.max(1,...rows.map((row)=>row.cash+row.transfer));
  const total = rows.reduce((sum,row)=>sum+row.cash+row.transfer,0);
  const query = new URLSearchParams({from,to,...(branch ? {branch} : {})});
  const router=useRouter(), path=usePathname();
  const paymentRows=data.payments.filter((row)=>row.status==="confirmed" && row.recognized_on >= from &&
    row.recognized_on <= to && (!branch || String(row.branch_id)===branch));
  const apply=(event)=>{
    event.preventDefault();
    const values=new FormData(event.currentTarget);
    router.push(`${path}?${new URLSearchParams(values)}`);
  };
  return <>
    <Panel title={overview ? "Pendapatan harian per cabang" : "Pendapatan menurut periode"}
      description={`${from} sampai ${to} · Total ${money(total)}`}>
      {!overview && <form key={query.toString()} onSubmit={apply} className="mb-4 grid items-end gap-3 sm:grid-cols-2 xl:grid-cols-4">
        <Field label="Dari tanggal" name="from" type="date" defaultValue={from} />
        <Field label="Sampai tanggal" name="to" type="date" defaultValue={to} />
        <Field label="Cabang" name="branch" required={false} defaultValue={branch} options={[["","Semua cabang"],...data.branches.map((row)=>[row.id,row.name])]} />
        <Submit>Terapkan Filter</Submit>
      </form>}
      <Feedback error={error} />
      {!error && <div className="grid gap-3 mb-4" role="img" aria-label="Grafik perbandingan pendapatan. Rincian tersedia dalam tabel di bawahnya.">
        {rows.map((row)=><div key={row.id} className="grid grid-cols-[6rem_1fr] items-center gap-3 text-sm">
          <span className="truncate font-semibold" title={row.branch_name}>{row.branch_name}</span>
          <div className="relative h-6 rounded bg-slate-100 dark:bg-slate-800">
            <div className="h-full rounded bg-primary dark:bg-indigo-400" style={{width:`${(row.cash+row.transfer)*100/max}%`}} />
            <span className="absolute right-2 top-0.5 rounded bg-white/95 px-1 text-xs font-bold text-slate-950">{money(row.cash+row.transfer)}</span>
          </div>
        </div>)}
      </div>}
      <Table rows={rows} columns={[
        ["Cabang","branch_name"],["Tunai",(row)=>money(row.cash)],["Transfer",(row)=>money(row.transfer)],
        ["Total",(row)=>money(row.cash+row.transfer)],["Transaksi","transactions"],
      ]} />
      {!error && !overview && <div className="mt-4 flex flex-wrap gap-3">
        <a className={linkClass} href={`/api/artha/report?${query}&format=pdf`} target="_blank" rel="noopener noreferrer">Laporan PDF</a>
        <a className={linkClass} href={`/api/artha/report?${query}&format=xlsx`}>Unduh Excel</a>
      </div>}
    </Panel>
    {!overview && !error && <Panel title="Rincian transaksi periode ini"><PaymentHistory rows={paymentRows} center /></Panel>}
  </>;
}
