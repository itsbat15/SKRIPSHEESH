"use client";

import { EditDialog, Feedback, Field, money, Panel, Status, Submit, Table, useMutation } from "./OperationsUI";
import { activeOptions, levelOptions } from "./Registration";

const forms = {
  branch:{action:"save-branch",name:"cabang",label:"Kantor Cabang",description:"Kelola profil dan status kantor cabang."},
  user:{action:"save-user",name:"staf",label:"Akun Staf",description:"Kelola akun Admin Cabang dan cabang penugasannya."},
  package:{action:"save-package",name:"paket",label:"Paket Belajar",description:"Atur tarif pendaftaran dan SPP per jenjang."},
};

function MasterForm({type,row={},data,finish}) {
  const operation = useMutation(forms[type].action,finish);
  return <form onSubmit={operation.submit} className="grid gap-3">
    {row.id && <input type="hidden" name="id" value={row.id} />}
    <Field label={`Nama ${forms[type].name}`} name="name" defaultValue={row.name} maxLength={200} />
    {type === "branch" && <Field label="Alamat" name="address" defaultValue={row.address} maxLength={400} />}
    {type === "user" && <>
      <Field label="Email" name="email" type="email" defaultValue={row.email} maxLength={200} />
      <Field label="Cabang penugasan" name="branch_id" options={data.branches.map((branch)=>[branch.id,`${branch.name}${branch.active ? "" : " (nonaktif)"}`])}
        defaultValue={row.branch_id} />
      <Field label={row.id ? "Kata sandi baru (opsional)" : "Kata sandi"} name="password" type="password" autoComplete="new-password"
        required={!row.id} minLength={12} maxLength={128}>Gunakan minimal 12 karakter.</Field>
    </>}
    {type === "package" && <>
      <Field label="Jenjang" name="level" options={levelOptions} defaultValue={row.level || "SD"} />
      <Field label="Biaya pendaftaran (Rp)" name="registration_fee" type="number" min={0} max={1000000000} defaultValue={row.registration_fee} />
      <Field label="SPP bulanan (Rp)" name="monthly_fee" type="number" min={1} max={1000000000} defaultValue={row.monthly_fee} />
    </>}
    <Field label="Status" name="active" options={activeOptions} defaultValue={row.active ?? 1} />
    <Feedback error={operation.error} /><Submit busy={operation.busy}>Simpan</Submit>
  </form>;
}

export default function MasterData({type,data}) {
  const config = forms[type];
  const rows = {branch:data.branches,user:data.users,package:data.packages}[type];
  const open = (row) => <EditDialog label={row ? "Edit" : `Tambah ${config.label}`}
    title={row ? `Edit ${config.name}` : `Tambah ${config.name}`} description={config.description}>
    {(finish)=><MasterForm type={type} row={row} data={data} finish={finish} />}
  </EditDialog>;
  const fields = {
    branch:[["Alamat","address"]],
    user:[["Email","email"],["Cabang","branch_name"]],
    package:[["Jenjang","level"],["Pendaftaran",(row)=>money(row.registration_fee)],["SPP bulanan",(row)=>money(row.monthly_fee)]],
  };
  return <Panel title={config.label} description={config.description} actions={open()}>
    <Table rows={rows} columns={[["Nama","name"],...fields[type],["Status",(row)=><Status value={row.active ? "active" : "inactive"} />],
      ["Aksi",(row)=>open(row)]]} />
  </Panel>;
}
