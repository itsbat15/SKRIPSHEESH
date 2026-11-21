"use client";

import { useState } from "react";
import Link from "next/link";
import { billKind, EditDialog, Feedback, Field, FileLink, money, Panel, paymentNumber, Status, Submit, Table, useMutation } from "./OperationsUI";

export const jenjang = ["TK","SD","SMP","SMA"];
export const levelOptions = jenjang.map((level)=>[level,level]);
export const activeOptions = [[1,"Aktif"],[0,"Nonaktif"]];

function Bio({row={},day,onLevel}) {
  return <>
    <Field label="Nama lengkap siswa" name="name" defaultValue={row.name} maxLength={200} />
    <Field label="Tanggal lahir" name="birth_date" type="date" defaultValue={row.birth_date} max={day} />
    <Field label="Asal sekolah" name="school" defaultValue={row.school} maxLength={200} />
    <Field label="Jenjang" name="level" defaultValue={row.level || "SD"} options={row.id ? [[row.level,row.level]] : levelOptions} onChange={onLevel} />
    <Field label="Nama orang tua / wali" name="guardian" defaultValue={row.guardian} maxLength={200} />
    <Field label="Nomor WhatsApp wali" name="phone" type="tel" defaultValue={row.phone} maxLength={24} placeholder="0812…" />
    <Field label="Alamat siswa" name="address" defaultValue={row.address} maxLength={400} />
  </>;
}

export function PaymentFields({day,max}) {
  const [method,setMethod] = useState("cash");
  return <>
    <Field label="Metode pembayaran" name="method" options={[["cash","Tunai"],["transfer","Transfer bank"]]} value={method}
      onChange={(event)=>setMethod(event.target.value)} />
    <Field key={max} label="Nominal diterima (Rp)" name="amount" type="number" min={1} max={max} defaultValue={max || undefined} />
    {method === "transfer" && <>
      <Field label="Nama pengirim" name="sender" maxLength={200} />
      <Field label="Tanggal transfer" name="transfer_on" type="date" max={day} defaultValue={day} />
      <Field label="Bukti transfer" name="proof" type="file" accept="image/jpeg,image/png,application/pdf">JPG, PNG, atau PDF. Maksimal 5 MB.</Field>
    </>}
  </>;
}

export function Registration({data}) {
  const [level,setLevel] = useState("SD");
  const [selected,setSelected] = useState("");
  const [result,setResult] = useState(null);
  const packages = data.packages.filter((item)=>item.level === level && item.active);
  const groups = data.groups.filter((item)=>item.level === level && item.active && item.occupied < item.capacity);
  const pack = packages.find((item)=>String(item.id) === selected) || packages[0];
  const payment = data.payments.find((row)=>row.id === result);
  const operation = useMutation("register",({paymentId},form)=>{
    form.reset();
    setLevel("SD");
    setSelected("");
    setResult(paymentId);
  });
  return <Panel title="Formulir siswa baru" description="Pilih paket dan sesi belajar, lalu catat pembayaran pendaftaran.">
    <form onSubmit={operation.submit} className="grid gap-5">
      <div className="grid gap-4 md:grid-cols-2">
        <Bio day={data.today} onLevel={(event)=>{setLevel(event.target.value);setSelected("");}} />
        <Field label="Paket belajar" name="package_id" value={pack?.id || ""} onChange={(event)=>setSelected(event.target.value)}
          options={packages.length ? packages.map((item)=>[item.id,item.name]) : [["","Tidak ada paket aktif"]]} />
        <Field key={level} label="Kelompok belajar" name="group_id" options={groups.length ?
          groups.map((item)=>[item.id,`${item.name} | ${item.schedule} | ${item.capacity-item.occupied} kursi`]) :
          [["","Tidak ada sesi dengan kursi tersedia"]]} />
      </div>
      {pack && <div className="rounded-lg border border-slate-300 bg-indigo-50 p-4 text-sm text-slate-900">
        Biaya pendaftaran: {money(pack.registration_fee)} · SPP pertama: {money(pack.monthly_fee)}
        <p className="mt-1 font-extrabold">Total tagihan: {money(pack.registration_fee+pack.monthly_fee)}</p>
      </div>}
      <div className="grid gap-4 md:grid-cols-2"><PaymentFields key={result || 0} day={data.today} max={pack ? pack.registration_fee+pack.monthly_fee : undefined} /></div>
      <Feedback error={operation.error} notice={operation.notice} />
      {payment && <div className="flex flex-wrap items-center gap-3 text-sm"><span>{paymentNumber(payment.id)}</span>
        <Status value={payment.status} />
        {payment.status === "confirmed" && payment.bill_paid >= payment.bill_amount &&
          <FileLink href={`/api/artha/receipt/${payment.id}`}>Buka kuitansi PDF</FileLink>}
        <Link className="font-semibold text-primary underline dark:text-indigo-300" href="/dashboard/frontdesk/spp">Lihat riwayat pembayaran</Link>
      </div>}
      <div><Submit busy={operation.busy || !pack || !groups.length}>Simpan Pendaftaran</Submit></div>
    </form>
  </Panel>;
}

function StudentForm({row,data,finish}) {
  const operation = useMutation("save-student",finish);
  const groups = data.groups.filter((group)=>group.level === row.level && (group.id === row.group_id || (group.active && group.occupied < group.capacity)));
  return <form className="grid gap-3 sm:grid-cols-2" onSubmit={operation.submit}>
    <input type="hidden" name="id" value={row.id} />
    <Bio row={row} day={data.today} />
    <Field label="Kelompok belajar" name="group_id" defaultValue={row.group_id} options={groups.map((group)=>[group.id,group.name])} />
    <Field label="Keikutsertaan" name="active" defaultValue={row.status === "inactive" ? 0 : 1}
      options={[[1,row.status === "pending" ? "Menunggu pelunasan" : "Aktif"],[0,"Nonaktif"]]} />
    <div className="sm:col-span-2 grid gap-3"><Feedback error={operation.error} /><Submit busy={operation.busy}>Simpan Siswa</Submit></div>
  </form>;
}

export function Students({data,center}) {
  const [search,setSearch]=useState("");
  const [branch,setBranch]=useState("");
  const rows = data.students.filter((row)=>(!branch || String(row.branch_id)===branch) &&
    `${row.name} ${row.school} ${row.guardian}`.toLowerCase().includes(search.toLowerCase()));
  return <Panel title="Daftar siswa" description="Biodata, kontak wali, dan penempatan sesi.">
    <div className="grid gap-3 md:grid-cols-2 mb-4">
      <Field label="Cari siswa, sekolah, atau wali" name="search" type="search" value={search} onChange={(event)=>setSearch(event.target.value)} />
      {center && <Field label="Cabang" name="branch" value={branch} onChange={(event)=>setBranch(event.target.value)}
        options={[["","Semua cabang"],...data.branches.map((item)=>[item.id,item.name])]} />}
    </div>
    <Table rows={rows} columns={[
      ["Siswa",(row)=><><strong>{row.name}</strong><div>{row.school} · {row.level}</div></>],
      ...(center ? [["Cabang","branch_name"]] : []),
      ["Wali",(row)=><>{row.guardian}<div>{row.phone}</div></>],
      ["Kelompok","group_name"],["Terdaftar","registered_on"],
      ["Status",(row)=><Status value={row.status} label={row.status === "pending" ? "Menunggu pelunasan" : undefined} />],
      ...(!center ? [["Aksi",(row)=><EditDialog label="Edit" title="Edit data siswa" description={row.name}>
        {(finish)=><StudentForm row={row} data={data} finish={finish} />}
      </EditDialog>]] : []),
    ]} />
  </Panel>;
}

function GroupForm({row={},finish}) {
  const operation = useMutation("save-group",finish);
  return <form className="grid gap-3" onSubmit={operation.submit}>
    {row.id && <input type="hidden" name="id" value={row.id} />}
    <Field label="Nama kelompok" name="name" defaultValue={row.name} maxLength={200} />
    <Field label="Jenjang" name="level" options={levelOptions} defaultValue={row.level || "SD"} />
    <Field label="Jadwal sesi" name="schedule" defaultValue={row.schedule} maxLength={200} placeholder="Senin & Rabu, 16.00" />
    <Field label="Kapasitas kursi" name="capacity" type="number" min={1} max={200} defaultValue={row.capacity || 10} />
    <Field label="Status" name="active" options={activeOptions} defaultValue={row.active ?? 1} />
    <Feedback error={operation.error} /><Submit busy={operation.busy}>Simpan Kelompok</Submit>
  </form>;
}

export function Groups({data,center}) {
  const edit = (row) => <EditDialog label={row ? "Edit" : "Tambah Kelompok"} title={row ? "Edit kelompok" : "Kelompok belajar baru"}
    description="Tentukan sesi dan batas jumlah peserta.">{(finish)=><GroupForm row={row} finish={finish} />}</EditDialog>;
  return <Panel title="Kelompok belajar" description="Kuota mencakup siswa aktif dan siswa yang menunggu pelunasan."
    actions={!center && edit()}>
    <Table rows={data.groups} columns={[
      ["Nama","name"],...(center ? [["Cabang","branch_name"]] : []),["Jenjang","level"],["Jadwal","schedule"],
      ["Terisi / kapasitas",(row)=>`${row.occupied} / ${row.capacity}`],
      ["Status",(row)=><Status value={row.active ? "active" : "inactive"} />],
      ...(!center ? [["Aksi",(row)=>edit(row)]] : []),
    ]} />
  </Panel>;
}

export function PaymentHistory({rows,center=false}) {
  return <Table rows={rows} empty="Belum ada riwayat transaksi." columns={[
    ["Transaksi",(row)=><><strong>{paymentNumber(row.id)}</strong><div>{row.recorded_on}</div></>],
    ...(center ? [["Cabang","branch_name"]] : []),["Siswa","student_name"],
    ["Tagihan",(row)=><>{billKind(row.kind)}<div>{row.period}</div></>],
    ["Pembayaran",(row)=><>{money(row.amount)}<div>{row.method === "cash" ? "Tunai" : "Transfer"}</div></>],
    ["Status",(row)=><><Status value={row.status} />{row.rejection_reason && <div className="mt-1 text-rose-700 dark:text-rose-300">{row.rejection_reason}</div>}</>],
    ["Berkas",(row)=><div className="grid gap-1">
      {row.method === "transfer" && <FileLink href={`/api/artha/proof/${row.id}`}>Bukti transfer</FileLink>}
      {row.status === "confirmed" && row.bill_paid >= row.bill_amount && <FileLink href={`/api/artha/receipt/${row.id}`}>Kuitansi PDF</FileLink>}
    </div>],
  ]} />;
}
