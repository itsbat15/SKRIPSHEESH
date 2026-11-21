import { dueDate, nextPeriod, passwordHash, today, transaction } from "./artha-db.mjs";

export const levels = ["TK", "SD", "SMP", "SMA"];

export class InputError extends Error {
  constructor(message, status = 400) {
    super(message);
    this.status = status;
  }
}

function requireValue(condition, message, status) {
  if (!condition) throw new InputError(message, status);
}

const needRow = (row) => {
  requireValue(row, "Data tidak ditemukan.", 404);
  return row;
};
const plainRows = (rows) => rows.map((row)=>({...row}));

const text = (data, key, label, max = 200, optional = false) => {
  const value = String(data.get(key) ?? "").trim();
  requireValue((optional || value.length > 0) && value.length <= max, `${label} tidak valid (maks. ${max} karakter).`);
  return value;
};
const integer = (data, key, label, min = 1, max = 1_000_000_000) => {
  const raw = text(data,key,label,12), value = Number(raw);
  requireValue(/^\d+$/.test(raw) && value >= min && value <= max, `${label} tidak valid.`);
  return value;
};
const select = (data, key, label, values) => {
  const value = text(data,key,label);
  requireValue(values.includes(value), `${label} tidak valid.`);
  return value;
};
const validDate = (value) => {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
  const date = new Date(value);
  return !Number.isNaN(date.valueOf()) && date.toISOString().slice(0,10) === value;
};
const date = (data, key, label, max) => {
  const value = text(data,key,label,10);
  requireValue(validDate(value) && (!max || value <= max), `${label} tidak valid.`);
  return value;
};
const flag = (data) => Number(select(data,"active","Status",["0","1"]));

const occupancy = `(SELECT COUNT(*) FROM enrollments e WHERE e.group_id=g.id AND e.status IN ('active','pending'))`;
const groupList = `SELECT g.*, b.name branch_name, ${occupancy} occupied FROM study_groups g JOIN branches b ON b.id=g.branch_id`;
const billList = `SELECT t.*, s.name student_name, s.phone, s.guardian, s.level, g.name group_name, b.name branch_name,
  COALESCE((SELECT SUM(p.amount) FROM payments p WHERE p.bill_id=t.id AND p.status='confirmed'),0) paid,
  COALESCE((SELECT SUM(p.amount) FROM payments p WHERE p.bill_id=t.id AND p.status='pending'),0) pending
  FROM tuition_bills t JOIN enrollments e ON e.id=t.enrollment_id JOIN students s ON s.id=e.student_id
  JOIN study_groups g ON g.id=e.group_id JOIN branches b ON b.id=t.branch_id`;
const paymentList = `SELECT p.*, s.name student_name, t.kind, t.period, t.amount bill_amount, b.name branch_name,
  cp.name package_name, u.name cashier, b.address branch_address,
  (SELECT COALESCE(SUM(x.amount),0) FROM payments x WHERE x.bill_id=t.id AND x.status='confirmed') bill_paid
  FROM payments p JOIN tuition_bills t ON t.id=p.bill_id JOIN enrollments e ON e.id=t.enrollment_id
  JOIN students s ON s.id=e.student_id JOIN branches b ON b.id=p.branch_id
  JOIN course_packages cp ON cp.id=e.package_id JOIN users u ON u.id=p.recorded_by`;

function scope(user, column) {
  return user.role === "super_admin" ? ["1=1", []] : [`${column}=?`, [user.branch_id]];
}

export function issueMonthlyBills(db, user, day = today()) {
  const [where, ids] = scope(user,"e.branch_id");
  const through = nextPeriod(day.slice(0,7));
  const recurring = db.prepare(`SELECT e.id,e.branch_id,e.due_day,e.monthly_fee,
    COALESCE((SELECT MAX(period) FROM tuition_bills WHERE enrollment_id=e.id AND kind='tuition'),substr(e.registered_on,1,7)) last_period
    FROM enrollments e JOIN branches b ON b.id=e.branch_id WHERE e.status='active' AND b.active=1 AND ${where}`).all(...ids);
  if (!recurring.some((row) => row.last_period < through)) return;
  transaction(db, () => {
    const insert = db.prepare(`INSERT OR IGNORE INTO tuition_bills (branch_id,enrollment_id,kind,period,due_on,amount)
      VALUES (?,?,'tuition',?,?,?)`);
    for (const row of recurring) {
      for (let period = nextPeriod(row.last_period); period <= through; period = nextPeriod(period)) {
        insert.run(row.branch_id,row.id,period,dueDate(period,row.due_day),row.monthly_fee);
      }
    }
  });
}

export function snapshot(db, user) {
  const day = today();
  issueMonthlyBills(db,user,day);
  const query = (sql, col, suffix = "") => {
    const [where, ids] = scope(user,col);
    return plainRows(db.prepare(`${sql} WHERE ${where} ${suffix}`).all(...ids));
  };
  const center = user.role === "super_admin";
  const bills = query(billList,"t.branch_id","ORDER BY t.due_on DESC,t.id DESC");
  return {
    today: day,
    user,
    branches: query("SELECT id,name,address,active FROM branches","id","ORDER BY id"),
    users: center ? plainRows(db.prepare(`SELECT u.id,u.name,u.email,u.branch_id,u.active,b.name branch_name
      FROM users u JOIN branches b ON b.id=u.branch_id WHERE u.role='branch_admin' ORDER BY u.name`).all()) : [],
    packages: plainRows(db.prepare("SELECT * FROM course_packages ORDER BY level,name").all()),
    groups: query(groupList,"g.branch_id","ORDER BY g.name"),
    students: query(`SELECT s.*, e.id enrollment_id,e.status,e.registered_on,e.due_day,e.group_id,e.package_id,
      g.name group_name,b.name branch_name,cp.name package_name FROM students s
      JOIN enrollments e ON e.student_id=s.id JOIN study_groups g ON g.id=e.group_id
      JOIN branches b ON b.id=s.branch_id JOIN course_packages cp ON cp.id=e.package_id`,"s.branch_id","ORDER BY s.name"),
    bills: bills.map((bill) => ({...bill, status: bill.paid >= bill.amount ? "paid" : bill.pending ? "pending" :
      bill.due_on < day ? "overdue" : bill.paid ? "partial" : "unpaid", overdue: bill.paid < bill.amount && bill.due_on < day})),
    payments: query(paymentList,"p.branch_id","ORDER BY p.id DESC"),
    reconciliations: query(`SELECT r.*,b.name branch_name,u.name cashier FROM daily_reconciliations r
      JOIN branches b ON b.id=r.branch_id JOIN users u ON u.id=r.closed_by`,"r.branch_id","ORDER BY r.day DESC"),
  };
}

function openCashDay(db, branch, day) {
  requireValue(!db.prepare("SELECT 1 FROM daily_reconciliations WHERE branch_id=? AND day=?").get(branch,day),
    "Kas hari ini telah ditutup. Catat pembayaran tunai pada hari operasional berikutnya.",409);
}

function firstPostingDay(db, branch, day) {
  while (db.prepare("SELECT 1 FROM daily_reconciliations WHERE branch_id=? AND day=?").get(branch,day)) {
    const date = new Date(day);
    date.setUTCDate(date.getUTCDate()+1);
    day = date.toISOString().slice(0,10);
  }
  return day;
}

async function preparePayment(data, day) {
  const method = select(data,"method","Metode",["cash","transfer"]);
  const amount = integer(data,"amount","Nominal pembayaran");
  if (method === "cash") return {method,amount};
  const sender = text(data,"sender","Nama pengirim");
  const transferOn = date(data,"transfer_on","Tanggal transfer",day);
  const file = data.get("proof");
  requireValue(file instanceof File && file.size > 0 && file.size <= 5*1024*1024,
    "Unggah bukti transfer berukuran maksimal 5 MB.");
  const body = Buffer.from(await file.arrayBuffer());
  const signatures = {"image/jpeg":"ffd8ff","image/png":"89504e470d0a1a0a","application/pdf":"255044462d"};
  requireValue(Object.hasOwn(signatures,file.type) && body.toString("hex",0,8).startsWith(signatures[file.type]),
    "Bukti harus berupa JPG, PNG, atau PDF yang valid.");
  return {method,amount,sender,transferOn,body,type:file.type};
}

function activateIfPaid(db, bill) {
  if (bill.kind !== "registration") return;
  const {total} = db.prepare("SELECT COALESCE(SUM(amount),0) total FROM payments WHERE bill_id=? AND status='confirmed'").get(bill.id);
  if (total >= bill.amount) db.prepare("UPDATE enrollments SET status='active' WHERE id=? AND status='pending'").run(bill.enrollment_id);
}

function recordPayment(db, user, bill, payment, day) {
  if (payment.method === "cash") openCashDay(db,user.branch_id,day);
  const {total} = db.prepare("SELECT COALESCE(SUM(amount),0) total FROM payments WHERE bill_id=? AND status!='rejected'").get(bill.id);
  requireValue(payment.amount <= bill.amount-total,"Nominal melebihi sisa tagihan yang belum dibayar atau sedang diverifikasi.");
  const cash = payment.method === "cash";
  const {lastInsertRowid} = db.prepare(`INSERT INTO payments
    (branch_id,bill_id,recorded_by,method,status,amount,recorded_on,recognized_on,sender,transfer_on)
    VALUES (?,?,?,?,?,?,?,?,?,?)`).run(user.branch_id,bill.id,user.id,payment.method,cash ? "confirmed" : "pending",
    payment.amount,day,cash ? day : null,payment.sender ?? null,payment.transferOn ?? null);
  if (!cash) db.prepare("INSERT INTO payment_proofs VALUES (?,?,?)").run(lastInsertRowid,payment.type,payment.body);
  else activateIfPaid(db,bill);
  return {paymentId:lastInsertRowid};
}

function bio(data, day) {
  const phone = text(data,"phone","Nomor WhatsApp",24).replace(/[\s()+-]/g,"");
  requireValue(/^(?:0|62)[1-9]\d{7,12}$/.test(phone),"Nomor WhatsApp tidak valid.");
  return [text(data,"name","Nama siswa"),date(data,"birth_date","Tanggal lahir",day),
    text(data,"school","Asal sekolah"),select(data,"level","Jenjang",levels),text(data,"guardian","Nama wali"),
    phone,text(data,"address","Alamat",400)];
}

function register(db,user,data,payment,day) {
  const values = bio(data,day);
  const pack = needRow(db.prepare("SELECT * FROM course_packages WHERE id=? AND active=1").get(integer(data,"package_id","Paket")));
  const group = needRow(db.prepare(`${groupList} WHERE g.id=? AND g.branch_id=? AND g.active=1`)
    .get(integer(data,"group_id","Kelompok"),user.branch_id));
  requireValue(pack.level === values[3] && group.level === values[3],"Jenjang paket dan kelompok harus sesuai dengan siswa.");
  requireValue(group.occupied < group.capacity,"Kelompok belajar penuh. Pilih sesi lain.",409);
  requireValue(!db.prepare("SELECT 1 FROM students WHERE branch_id=? AND name=? AND birth_date=?")
    .get(user.branch_id,values[0],values[1]),"Siswa dengan nama dan tanggal lahir yang sama sudah terdaftar.",409);
  const {lastInsertRowid: studentId} = db.prepare(`INSERT INTO students (branch_id,name,birth_date,school,level,guardian,phone,address)
    VALUES (?,?,?,?,?,?,?,?)`).run(user.branch_id,...values);
  const {lastInsertRowid: enrollmentId} = db.prepare(`INSERT INTO enrollments
    (branch_id,student_id,group_id,package_id,registered_on,due_day,monthly_fee,status) VALUES (?,?,?,?,?,?,?,'pending')`)
    .run(user.branch_id,studentId,group.id,pack.id,day,Number(day.slice(8)),pack.monthly_fee);
  const amount = pack.registration_fee + pack.monthly_fee;
  const {lastInsertRowid: id} = db.prepare(`INSERT INTO tuition_bills (branch_id,enrollment_id,kind,period,due_on,amount)
    VALUES (?,?,'registration',?,?,?)`).run(user.branch_id,enrollmentId,day.slice(0,7),day,amount);
  return recordPayment(db,user,{id,amount,kind:"registration",enrollment_id:enrollmentId},payment,day);
}

function reviewPayment(db,user,data,day) {
  const payment = needRow(db.prepare("SELECT * FROM payments WHERE id=? AND method='transfer' AND status='pending'")
    .get(integer(data,"id","Pembayaran")));
  const approved = select(data,"decision","Keputusan",["approve","reject"]) === "approve";
  const reason = approved ? null : text(data,"reason","Alasan penolakan",400);
  const status = approved ? "confirmed" : "rejected";
  db.prepare(`UPDATE payments SET status=?,recognized_on=?,reviewed_by=?,reviewed_at=?,rejection_reason=? WHERE id=?`)
    .run(status,approved ? firstPostingDay(db,payment.branch_id,day) : null,user.id,new Date().toISOString(),reason,payment.id);
  if (approved) activateIfPaid(db,db.prepare("SELECT * FROM tuition_bills WHERE id=?").get(payment.bill_id));
}

export function totals(db, branch, day) {
  return db.prepare(`SELECT
    COALESCE(SUM(CASE WHEN method='cash' THEN amount END),0) cash,
    COALESCE(SUM(CASE WHEN method='transfer' THEN amount END),0) transfer
    FROM payments WHERE branch_id=? AND recognized_on=? AND status='confirmed'`).get(branch,day);
}

const centerActions = ["save-branch","save-user","save-package","review-payment","approve-close"];
const branchActions = ["register","pay","save-group","save-student","close-day"];

export async function mutate(db,user,action,data,day = today()) {
  requireValue((user.role === "super_admin" ? centerActions : branchActions).includes(action),"Anda tidak memiliki akses.",403);
  const payment = ["register","pay"].includes(action) ? await preparePayment(data,day) : null;
  return transaction(db, () => {
    const current = db.prepare(`SELECT u.* FROM users u LEFT JOIN branches b ON b.id=u.branch_id
      WHERE u.id=? AND u.active=1 AND (u.branch_id IS NULL OR b.active=1)`).get(user.id);
    requireValue(current && current.role === user.role && current.branch_id === user.branch_id,"Akses telah berubah. Masuk kembali.",403);
    if (action === "register") return register(db,user,data,payment,day);
    if (action === "pay") {
      const bill = needRow(db.prepare("SELECT * FROM tuition_bills WHERE id=? AND branch_id=?")
        .get(integer(data,"id","Tagihan"),user.branch_id));
      return recordPayment(db,user,bill,payment,day);
    }
    if (action === "review-payment") return reviewPayment(db,user,data,day);
    if (action === "close-day") {
      openCashDay(db,user.branch_id,day);
      const physical = integer(data,"physical","Kas fisik",0);
      const {cash,transfer} = totals(db,user.branch_id,day);
      const note = text(data,"note","Catatan",400,physical === cash);
      db.prepare(`INSERT INTO daily_reconciliations (branch_id,closed_by,day,cash,transfer,physical,note,status)
        VALUES (?,?,?,?,?,?,?,?)`).run(user.branch_id,user.id,day,cash,transfer,physical,note,
        cash === physical ? "submitted" : "needs_review");
      return;
    }
    if (action === "approve-close") {
      const result = db.prepare(`UPDATE daily_reconciliations SET status='approved',reviewed_by=?,reviewed_at=?
        WHERE id=? AND status!='approved'`).run(user.id,new Date().toISOString(),integer(data,"id","Rekonsiliasi"));
      requireValue(result.changes,"Data tidak ditemukan atau sudah disetujui.",404);
      return;
    }

    const id = data.get("id") ? integer(data,"id","Data") : null;
    if (action === "save-student") {
      const student = needRow(db.prepare(`SELECT s.*,e.id enrollment_id,e.group_id,e.status FROM students s
        JOIN enrollments e ON e.student_id=s.id WHERE s.id=? AND s.branch_id=?`).get(id,user.branch_id));
      const values = bio(data,day);
      requireValue(student.level === values[3],"Jenjang siswa tidak dapat diubah dari pendaftaran ini.");
      const group = needRow(db.prepare(`${groupList} WHERE g.id=? AND g.branch_id=?`).get(integer(data,"group_id","Kelompok"),user.branch_id));
      requireValue(group.level === student.level,"Jenjang kelompok tidak sesuai.");
      const status = flag(data) ? (student.status === "pending" ? "pending" : "active") : "inactive";
      if (status !== "inactive" && (group.id !== student.group_id || student.status === "inactive")) {
        requireValue(group.active && group.occupied < group.capacity,"Kelompok belajar tidak aktif atau penuh.",409);
      }
      if (status === "active" && student.status === "inactive") {
        const registration = db.prepare(`${billList} WHERE t.enrollment_id=? AND t.kind='registration'`).get(student.enrollment_id);
        requireValue(registration?.paid >= registration?.amount,"Lunasi biaya pendaftaran sebelum mengaktifkan siswa.");
      }
      db.prepare("UPDATE students SET name=?,birth_date=?,school=?,level=?,guardian=?,phone=?,address=? WHERE id=?").run(...values,id);
      db.prepare("UPDATE enrollments SET group_id=?,status=? WHERE id=?").run(group.id,status,student.enrollment_id);
      return;
    }
    if (action === "save-group") {
      const values = [text(data,"name","Nama kelompok"),select(data,"level","Jenjang",levels),
        text(data,"schedule","Jadwal"),integer(data,"capacity","Kapasitas",1,200),flag(data)];
      if (!id) db.prepare("INSERT INTO study_groups (name,level,schedule,capacity,active,branch_id) VALUES (?,?,?,?,?,?)").run(...values,user.branch_id);
      else {
        const existing = needRow(db.prepare(`${groupList} WHERE g.id=? AND g.branch_id=?`).get(id,user.branch_id));
        requireValue(values[3] >= existing.occupied && (!existing.occupied || values[1] === existing.level),
          "Kapasitas tidak boleh di bawah jumlah peserta dan jenjang tidak dapat berubah selama masih ada peserta.");
        db.prepare("UPDATE study_groups SET name=?,level=?,schedule=?,capacity=?,active=? WHERE id=?").run(...values,id);
      }
      return;
    }
    if (action === "save-branch") {
      const values = [text(data,"name","Nama cabang"),text(data,"address","Alamat",400),flag(data)];
      if (id) needRow(db.prepare("UPDATE branches SET name=?,address=?,active=? WHERE id=? RETURNING id").get(...values,id));
      else db.prepare("INSERT INTO branches (name,address,active) VALUES (?,?,?)").run(...values);
      return;
    }
    if (action === "save-package") {
      const values = [text(data,"name","Nama paket"),select(data,"level","Jenjang",levels),
        integer(data,"registration_fee","Biaya pendaftaran",0),integer(data,"monthly_fee","SPP bulanan"),flag(data)];
      if (id) needRow(db.prepare("UPDATE course_packages SET name=?,level=?,registration_fee=?,monthly_fee=?,active=? WHERE id=? RETURNING id").get(...values,id));
      else db.prepare("INSERT INTO course_packages (name,level,registration_fee,monthly_fee,active) VALUES (?,?,?,?,?)").run(...values);
      return;
    }
    if (action === "save-user") {
      const email = text(data,"email","Email").toLowerCase();
      requireValue(/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email),"Email tidak valid.");
      const branch = integer(data,"branch_id","Cabang");
      needRow(db.prepare("SELECT id FROM branches WHERE id=?").get(branch));
      const values = [branch,text(data,"name","Nama staf"),email,flag(data)];
      const password = String(data.get("password") ?? "");
      requireValue((id && !password) || (password.length >= 12 && password.length <= 128),"Kata sandi harus terdiri dari 12–128 karakter.");
      if (!id) db.prepare("INSERT INTO users (branch_id,name,email,active,password_hash,role) VALUES (?,?,?,?,?,'branch_admin')")
        .run(...values,passwordHash(password));
      else {
        needRow(db.prepare(`UPDATE users SET branch_id=?,name=?,email=?,active=?,password_hash=COALESCE(?,password_hash)
          WHERE id=? AND role='branch_admin' RETURNING id`).get(...values,password ? passwordHash(password) : null,id));
        db.prepare("DELETE FROM sessions WHERE user_id=?").run(id);
      }
    }
  });
}

export function paymentDocument(db,user,id,kind) {
  const [where,args] = scope(user,"p.branch_id");
  if (kind === "proof") return needRow(db.prepare(`SELECT f.* FROM payment_proofs f JOIN payments p ON p.id=f.payment_id
    WHERE p.id=? AND ${where}`).get(id,...args));
  const payment = needRow(db.prepare(`${paymentList} WHERE p.id=? AND p.status='confirmed' AND ${where}`).get(id,...args));
  requireValue(payment.bill_paid >= payment.bill_amount,"Kuitansi terbit setelah tagihan lunas.",409);
  return payment;
}

export function reconciliationDocument(db,user,id) {
  const [where,args] = scope(user,"r.branch_id");
  return needRow(db.prepare(`SELECT r.*,b.name branch_name,u.name cashier FROM daily_reconciliations r
    JOIN branches b ON b.id=r.branch_id JOIN users u ON u.id=r.closed_by WHERE r.id=? AND ${where}`).get(id,...args));
}

export function revenue(db,user,from,to,branch) {
  const [where,args] = scope(user,"b.id");
  requireValue(validDate(from) && validDate(to) && from<=to && (!branch || /^[1-9]\d*$/.test(branch)),"Periode atau cabang tidak valid.");
  return plainRows(db.prepare(`SELECT b.id,b.name branch_name, COALESCE(SUM(CASE WHEN p.method='cash' THEN p.amount END),0) cash,
    COALESCE(SUM(CASE WHEN p.method='transfer' THEN p.amount END),0) transfer,COUNT(p.id) transactions FROM branches b
    LEFT JOIN payments p ON p.branch_id=b.id AND p.status='confirmed' AND p.recognized_on BETWEEN ? AND ?
    WHERE ${where} AND (? IS NULL OR b.id=?) GROUP BY b.id ORDER BY b.id`).all(from,to,...args,branch||null,branch||null));
}
