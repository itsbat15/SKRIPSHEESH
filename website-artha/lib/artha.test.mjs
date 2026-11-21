import assert from "node:assert/strict";
import { afterEach, beforeEach, test } from "node:test";
import { dueDate, openDatabase } from "./artha-db.mjs";
import { closeReport, receipt, revenueExcel, revenuePdf } from "./artha-documents.mjs";
import { issueMonthlyBills, mutate, paymentDocument, reconciliationDocument, revenue, snapshot, totals } from "./artha-operations.mjs";

let db, artha1, artha2, center, group1, group2;
const day = "2026-01-31";

beforeEach(() => {
  db = openDatabase(":memory:",{demo:true});
  const find = (email)=>db.prepare("SELECT id,branch_id,role FROM users WHERE email=?").get(email);
  [artha1,artha2,center]=["cabang1@artha.example","cabang2@artha.example","pusat@artha.example"].map(find);
  const group = (id)=>db.prepare("SELECT id FROM study_groups WHERE branch_id=? AND level='SD'").get(id).id;
  [group1,group2]=[group(artha1.branch_id),group(artha2.branch_id)];
});

afterEach(()=>db.close());

function form(input) {
  const result=new FormData();
  for (const [key,value] of Object.entries(input)) result.set(key,value);
  return result;
}
const registration=(extra={})=>form({name:"Siswa Baru",birth_date:"2016-04-10",school:"SD Uji",
  level:"SD",guardian:"Wali Uji",phone:"081211112222",address:"Balikpapan",package_id:2,group_id:group1,
  amount:400000,method:"cash",...extra});
const transfer=(extra={})=>({method:"transfer",sender:"Wali Uji",transfer_on:day,
  proof:new File(["%PDF-1.7\n"],"bukti.pdf",{type:"application/pdf"}),...extra});
const assertStatus=(status)=>({status});

test("UC-01: branch-scoped registration, capacity, cash receipt and month-end bills",async()=>{
  await assert.rejects(mutate(db,artha1,"register",registration({group_id:group2}),day),assertStatus(404));
  await assert.rejects(mutate(db,center,"register",registration(),day),assertStatus(403));
  const {paymentId}=await mutate(db,artha1,"register",registration({amount:100000}),day);
  const bill=db.prepare("SELECT bill_id FROM payments WHERE id=?").get(paymentId).bill_id;
  assert.throws(()=>paymentDocument(db,artha1,paymentId,"receipt"),assertStatus(409));
  await assert.rejects(mutate(db,artha2,"pay",form({id:bill,method:"cash",amount:300000}),day),assertStatus(404));
  await assert.rejects(mutate(db,artha1,"register",registration(),day),assertStatus(409));
  await mutate(db,artha1,"pay",form({id:bill,method:"cash",amount:300000}),day);
  db.prepare("UPDATE study_groups SET capacity=2 WHERE id=?").run(group1);
  await assert.rejects(mutate(db,artha1,"register",registration({name:"Siswa Penuh"}),day),assertStatus(409));
  assert.throws(()=>paymentDocument(db,artha2,paymentId,"receipt"),assertStatus(404));
  assert.deepEqual(Buffer.from(await receipt(paymentDocument(db,artha1,paymentId,"receipt"))).subarray(0,5),Buffer.from("%PDF-"));
  issueMonthlyBills(db,artha1,day);
  const next=db.prepare(`SELECT due_on FROM tuition_bills WHERE kind='tuition' AND enrollment_id=(
    SELECT enrollment_id FROM tuition_bills WHERE id=?)`).get(bill);
  assert.equal(next.due_on,"2026-02-28");
  assert.equal(dueDate("2028-02",31),"2028-02-29");
  assert.equal(totals(db,artha1.branch_id,day).cash,400000);
  const data=snapshot(db,artha1);
  assert.ok(data.students.every((student)=>student.branch_id===artha1.branch_id));
  for (const rows of [data.branches,data.groups,data.students,data.packages,data.bills,data.payments]) {
    assert.ok(rows.every((row)=>Object.getPrototypeOf(row)===Object.prototype));
  }
});

test("UC-02: review requires center role, rejection reason, retry and scoped proof",async()=>{
  const {paymentId}=await mutate(db,artha1,"register",registration(transfer()),day);
  assert.throws(()=>paymentDocument(db,artha2,paymentId,"proof"),assertStatus(404));
  assert.equal(paymentDocument(db,center,paymentId,"proof").file_type,"application/pdf");
  await assert.rejects(mutate(db,artha1,"review-payment",form({id:paymentId,decision:"approve"}),day),assertStatus(403));
  await assert.rejects(mutate(db,center,"review-payment",form({id:paymentId,decision:"reject"}),day),assertStatus(400));
  await mutate(db,center,"review-payment",form({id:paymentId,decision:"reject",reason:"Tidak cocok"}),day);
  const {bill_id:id,rejection_reason}=db.prepare("SELECT bill_id,rejection_reason FROM payments WHERE id=?").get(paymentId);
  assert.equal(rejection_reason,"Tidak cocok");
  const retry=await mutate(db,artha1,"pay",form({id,amount:400000,...transfer()}),day);
  await mutate(db,center,"review-payment",form({id:retry.paymentId,decision:"approve"}),day);
  assert.equal(paymentDocument(db,artha1,retry.paymentId,"receipt").bill_paid,400000);
  assert.equal(totals(db,artha1.branch_id,day).transfer,400000);
});

test("UC-03: discrepancy note, day lock, center approval and report formats",async()=>{
  const pending=await mutate(db,artha1,"register",registration({name:"Siswa Transfer",...transfer()}),day);
  await mutate(db,artha1,"register",registration(),day);
  await assert.rejects(mutate(db,artha1,"close-day",form({physical:399000}),day),assertStatus(400));
  await mutate(db,artha1,"close-day",form({physical:399000,note:"Selisih penghitungan"}),day);
  await assert.rejects(mutate(db,artha1,"register",registration({name:"Siswa Kas Ditutup"}),day),assertStatus(409));
  assert.equal(db.prepare("SELECT COUNT(*) n FROM students WHERE name='Siswa Kas Ditutup'").get().n,0);
  await mutate(db,center,"review-payment",form({id:pending.paymentId,decision:"approve"}),day);
  const close=db.prepare("SELECT id FROM daily_reconciliations WHERE day=?").get(day);
  assert.throws(()=>reconciliationDocument(db,artha2,close.id),assertStatus(404));
  assert.equal(reconciliationDocument(db,center,close.id).status,"needs_review");
  await mutate(db,center,"approve-close",form(close),day);
  assert.equal(reconciliationDocument(db,artha1,close.id).status,"approved");
  assert.equal(totals(db,artha1.branch_id,day).transfer,0);
  assert.equal(totals(db,artha1.branch_id,"2026-02-01").transfer,400000);
  const summary=revenue(db,center,day,day,String(artha1.branch_id));
  assert.equal(summary.length,1);
  assert.equal(summary[0].cash,400000);
  assert.equal(Buffer.from(await closeReport(reconciliationDocument(db,center,close.id))).subarray(0,5).toString(),"%PDF-");
  assert.equal(Buffer.from(await revenuePdf(summary,day,day)).subarray(0,5).toString(),"%PDF-");
  assert.equal(Buffer.from(await revenueExcel(summary,day,day)).subarray(0,2).toString(),"PK");
});

test("FR-02: unique staff email and deactivation enforce write permissions",async()=>{
  const fields={branch_id:artha1.branch_id,name:"Staf Uji",email:"staf@artha.example",password:"ContohSandi2026!",active:1};
  await mutate(db,center,"save-user",form(fields),day);
  await assert.rejects(mutate(db,center,"save-user",form(fields),day),{errcode:2067});
  const branch=db.prepare("SELECT * FROM branches WHERE id=?").get(artha1.branch_id);
  await mutate(db,center,"save-branch",form({...branch,active:0}),day);
  await assert.rejects(mutate(db,artha1,"close-day",form({physical:0}),day),assertStatus(403));
});
