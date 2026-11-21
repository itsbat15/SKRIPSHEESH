import { createHash, randomBytes, scryptSync, timingSafeEqual } from "node:crypto";
import { mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { DatabaseSync } from "node:sqlite";

const schema = `
CREATE TABLE IF NOT EXISTS branches (
  id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE COLLATE NOCASE,
  address TEXT NOT NULL, active INTEGER NOT NULL DEFAULT 1 CHECK(active IN (0,1))
);
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY, branch_id INTEGER REFERENCES branches, name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE COLLATE NOCASE, password_hash TEXT NOT NULL,
  role TEXT NOT NULL CHECK(role IN ('branch_admin','super_admin')),
  active INTEGER NOT NULL DEFAULT 1 CHECK(active IN (0,1)),
  CHECK((role='super_admin' AND branch_id IS NULL) OR (role='branch_admin' AND branch_id IS NOT NULL))
);
CREATE TABLE IF NOT EXISTS course_packages (
  id INTEGER PRIMARY KEY, name TEXT NOT NULL, level TEXT NOT NULL,
  registration_fee INTEGER NOT NULL CHECK(registration_fee>=0),
  monthly_fee INTEGER NOT NULL CHECK(monthly_fee>0),
  active INTEGER NOT NULL DEFAULT 1 CHECK(active IN (0,1)), UNIQUE(name,level)
);
CREATE TABLE IF NOT EXISTS study_groups (
  id INTEGER PRIMARY KEY, branch_id INTEGER NOT NULL REFERENCES branches,
  name TEXT NOT NULL, level TEXT NOT NULL, schedule TEXT NOT NULL,
  capacity INTEGER NOT NULL CHECK(capacity>0), active INTEGER NOT NULL DEFAULT 1 CHECK(active IN (0,1)),
  UNIQUE(branch_id,name), UNIQUE(id,branch_id)
);
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY, branch_id INTEGER NOT NULL REFERENCES branches,
  name TEXT NOT NULL COLLATE NOCASE, birth_date TEXT NOT NULL, school TEXT NOT NULL,
  level TEXT NOT NULL, guardian TEXT NOT NULL, phone TEXT NOT NULL, address TEXT NOT NULL,
  UNIQUE(branch_id,name,birth_date), UNIQUE(id,branch_id)
);
CREATE TABLE IF NOT EXISTS enrollments (
  id INTEGER PRIMARY KEY, branch_id INTEGER NOT NULL REFERENCES branches,
  student_id INTEGER NOT NULL, group_id INTEGER NOT NULL,
  package_id INTEGER NOT NULL REFERENCES course_packages, registered_on TEXT NOT NULL,
  due_day INTEGER NOT NULL CHECK(due_day BETWEEN 1 AND 31),
  monthly_fee INTEGER NOT NULL CHECK(monthly_fee>0),
  status TEXT NOT NULL CHECK(status IN ('pending','active','inactive')),
  FOREIGN KEY(student_id,branch_id) REFERENCES students(id,branch_id),
  FOREIGN KEY(group_id,branch_id) REFERENCES study_groups(id,branch_id),
  UNIQUE(id,branch_id)
);
CREATE TABLE IF NOT EXISTS tuition_bills (
  id INTEGER PRIMARY KEY, branch_id INTEGER NOT NULL REFERENCES branches,
  enrollment_id INTEGER NOT NULL, kind TEXT NOT NULL CHECK(kind IN ('registration','tuition')),
  period TEXT NOT NULL, due_on TEXT NOT NULL, amount INTEGER NOT NULL CHECK(amount>0),
  FOREIGN KEY(enrollment_id,branch_id) REFERENCES enrollments(id,branch_id),
  UNIQUE(enrollment_id,kind,period), UNIQUE(id,branch_id)
);
CREATE TABLE IF NOT EXISTS payments (
  id INTEGER PRIMARY KEY, branch_id INTEGER NOT NULL REFERENCES branches,
  bill_id INTEGER NOT NULL, recorded_by INTEGER NOT NULL REFERENCES users,
  method TEXT NOT NULL CHECK(method IN ('cash','transfer')),
  status TEXT NOT NULL CHECK(status IN ('confirmed','pending','rejected')),
  amount INTEGER NOT NULL CHECK(amount>0), recorded_on TEXT NOT NULL,
  recognized_on TEXT, sender TEXT, transfer_on TEXT, reviewed_by INTEGER REFERENCES users,
  reviewed_at TEXT, rejection_reason TEXT,
  FOREIGN KEY(bill_id,branch_id) REFERENCES tuition_bills(id,branch_id)
);
CREATE TABLE IF NOT EXISTS payment_proofs (
  payment_id INTEGER PRIMARY KEY REFERENCES payments, file_type TEXT NOT NULL, body BLOB NOT NULL
);
CREATE TABLE IF NOT EXISTS daily_reconciliations (
  id INTEGER PRIMARY KEY, branch_id INTEGER NOT NULL REFERENCES branches,
  closed_by INTEGER NOT NULL REFERENCES users, day TEXT NOT NULL,
  cash INTEGER NOT NULL, transfer INTEGER NOT NULL, physical INTEGER NOT NULL CHECK(physical>=0),
  note TEXT, status TEXT NOT NULL CHECK(status IN ('submitted','needs_review','approved')),
  reviewed_by INTEGER REFERENCES users, reviewed_at TEXT, UNIQUE(branch_id,day)
);
CREATE TABLE IF NOT EXISTS sessions (
  token_hash TEXT PRIMARY KEY, user_id INTEGER NOT NULL REFERENCES users, expires INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS payments_branch_day ON payments(branch_id,recognized_on);
CREATE INDEX IF NOT EXISTS payments_bill ON payments(bill_id,status);
CREATE INDEX IF NOT EXISTS enrollments_group ON enrollments(group_id,status);
`;

export function passwordHash(password) {
  const salt = randomBytes(16).toString("hex");
  return `${salt}:${scryptSync(password, salt, 64).toString("hex")}`;
}

const dummyHash = passwordHash(randomBytes(24).toString("hex"));

export function verifyPassword(password, stored = dummyHash) {
  const [salt, hex] = stored.split(":");
  return timingSafeEqual(scryptSync(password, salt, 64), Buffer.from(hex, "hex"));
}

export const tokenHash = (token) => createHash("sha256").update(token).digest("hex");
export const today = () => new Intl.DateTimeFormat("sv-SE", { timeZone: "Asia/Makassar" }).format(new Date());

export function dueDate(period, day) {
  const [year, month] = period.split("-").map(Number);
  const limit = new Date(Date.UTC(year, month, 0)).getUTCDate();
  return `${period}-${String(Math.min(day, limit)).padStart(2, "0")}`;
}

export function nextPeriod(period) {
  const [year, month] = period.split("-").map(Number);
  return new Date(Date.UTC(year, month, 1)).toISOString().slice(0, 7);
}

export function transaction(db, fn) {
  db.exec("BEGIN IMMEDIATE");
  try {
    const result = fn();
    db.exec("COMMIT");
    return result;
  } catch (error) {
    db.exec("ROLLBACK");
    throw error;
  }
}

function seed(db, demo, setupPassword) {
  if (!demo && (!setupPassword || setupPassword.length < 12)) {
    throw new Error("Set ARTHA_ADMIN_PASSWORD (minimum 12 characters) to initialize the database.");
  }
  const user = db.prepare("INSERT INTO users (branch_id,name,email,password_hash,role) VALUES (?,?,?,?,?)");
  user.run(null, "Manajemen Pusat", process.env.ARTHA_ADMIN_EMAIL || "pusat@artha.example",
    passwordHash(demo ? "ArthaDemo2026!" : setupPassword), "super_admin");
  if (!demo) return;
  const branch = db.prepare("INSERT INTO branches (name,address) VALUES (?,?)");
  const group = db.prepare("INSERT INTO study_groups (branch_id,name,level,schedule,capacity) VALUES (?,?,?,?,?)");
  const pack = db.prepare("INSERT INTO course_packages (name,level,registration_fee,monthly_fee) VALUES (?,?,?,?)");
  for (const [level, monthly] of [["TK",250000],["SD",300000],["SMP",350000],["SMA",400000]]) {
    pack.run("Reguler", level, 100000, monthly);
  }
  const branchHash = passwordHash("ArthaDemo2026!");
  const day = today();
  const [y, m] = day.split("-").map(Number);
  const previous = new Date(Date.UTC(y,m-2,3)).toISOString().slice(0,10);
  for (let i = 1; i <= 8; i++) {
    const {lastInsertRowid: branchId} = branch.run(`Artha ${i}`, "Balikpapan (data demo)");
    const {lastInsertRowid: userId} = user.run(branchId, `Admin Artha ${i}`, `cabang${i}@artha.example`, branchHash, "branch_admin");
    for (const level of ["TK","SD","SMP","SMA"]) group.run(branchId,`${level} Sesi A`,level,"Senin & Rabu, 16.00",10);
    const {id: groupId} = db.prepare("SELECT id FROM study_groups WHERE branch_id=? AND level='SD'").get(branchId);
    const {lastInsertRowid: studentId} = db.prepare(`INSERT INTO students
      (branch_id,name,birth_date,school,level,guardian,phone,address) VALUES (?,?,?,?,?,?,?,?)`)
      .run(branchId,`Siswa Demo ${i}`,"2015-03-12","SD Contoh","SD",`Wali Demo ${i}`,"081200000000","Balikpapan");
    const {lastInsertRowid: enrollmentId} = db.prepare(`INSERT INTO enrollments
      (branch_id,student_id,group_id,package_id,registered_on,due_day,monthly_fee,status) VALUES (?,?,?,?,?,?,?,'active')`)
      .run(branchId,studentId,groupId,2,previous,3,300000);
    const {lastInsertRowid: billId} = db.prepare(`INSERT INTO tuition_bills
      (branch_id,enrollment_id,kind,period,due_on,amount) VALUES (?,?,'registration',?,?,400000)`)
      .run(branchId,enrollmentId,previous.slice(0,7),previous);
    db.prepare(`INSERT INTO payments (branch_id,bill_id,recorded_by,method,status,amount,recorded_on,recognized_on)
      VALUES (?,?,?,'cash','confirmed',400000,?,?)`).run(branchId,billId,userId,previous,previous);
  }
}

export function openDatabase(path, { demo = false, setupPassword } = {}) {
  if (path !== ":memory:") mkdirSync(dirname(path), { recursive: true, mode: 0o700 });
  const db = new DatabaseSync(path);
  try {
    db.exec("PRAGMA foreign_keys=ON; PRAGMA busy_timeout=5000; PRAGMA journal_mode=WAL;");
    transaction(db, () => {
      db.exec(schema);
      if (!db.prepare("SELECT 1 FROM users LIMIT 1").get()) seed(db, demo, setupPassword);
    });
    return db;
  } catch (error) {
    db.close();
    throw error;
  }
}

let database;
export function getDatabase() {
  database ??= openDatabase(resolve(/*turbopackIgnore: true*/ process.cwd(), process.env.ARTHA_DB_PATH || ".artha/artha.sqlite"), {
    demo: process.env.ARTHA_DEMO === "1" || (process.env.ARTHA_DEMO !== "0" && process.env.NODE_ENV === "development"),
    setupPassword: process.env.ARTHA_ADMIN_PASSWORD,
  });
  return database;
}
