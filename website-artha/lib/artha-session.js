import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { randomBytes } from "node:crypto";
import { getDatabase, tokenHash, verifyPassword } from "./artha-db.mjs";
import { InputError } from "./artha-operations.mjs";

const cookie = "artha_session";
const age = 60 * 60 * 8;
const attempts = new Map();
const activeUsers = `FROM users u LEFT JOIN branches b ON b.id=u.branch_id
  WHERE u.active=1 AND (u.branch_id IS NULL OR b.active=1)`;

export function dashboardFor(user) {
  return user.role === "super_admin" ? "/dashboard/superadmin" : "/dashboard/frontdesk";
}

export async function currentUser(db) {
  const value = (await cookies()).get(cookie)?.value;
  if (!value || !/^[a-f0-9]{64}$/.test(value)) return null;
  db ??= getDatabase();
  const user = db.prepare(`SELECT u.id,u.name,u.role,u.branch_id,b.name branch_name ${activeUsers}
    AND EXISTS (SELECT 1 FROM sessions s WHERE s.user_id=u.id AND s.token_hash=? AND s.expires>?)`)
    .get(tokenHash(value),Date.now());
  return user ? {...user} : null;
}

export async function requireDashboardUser(role) {
  const user = await currentUser();
  if (!user) redirect("/login");
  if (role && user.role !== role) redirect(dashboardFor(user));
  return user;
}

export async function login(db, data, request) {
  const email = String(data.get("email") || "").trim().toLowerCase();
  const password = String(data.get("password") || "");
  if (!email || email.length > 200 || !password || password.length > 128) {
    throw new InputError("Email atau kata sandi salah.",401);
  }
  const now = Date.now();
  for (const [key, entry] of attempts) {
    if (entry.until <= now) attempts.delete(key);
  }
  if ((attempts.get(email)?.count ?? 0) >= 10 || attempts.size >= 1000) {
    throw new InputError("Terlalu banyak percobaan. Coba lagi dalam beberapa menit.",429);
  }
  const user = db.prepare(`SELECT u.* ${activeUsers} AND u.email=?`).get(email);
  if (!verifyPassword(password,user?.password_hash) || !user) {
    attempts.set(email,{count:(attempts.get(email)?.count ?? 0)+1,until:now+5*60*1000});
    throw new InputError("Email atau kata sandi salah.",401);
  }
  attempts.delete(email);
  const store = await cookies();
  const existing = store.get(cookie)?.value;
  if (existing) db.prepare("DELETE FROM sessions WHERE token_hash=?").run(tokenHash(existing));
  db.prepare("DELETE FROM sessions WHERE expires<=?").run(now);
  const token = randomBytes(32).toString("hex");
  db.prepare("INSERT INTO sessions VALUES (?,?,?)").run(tokenHash(token),user.id,now+age*1000);
  store.set(cookie,token,{
    httpOnly:true,sameSite:"lax",path:"/",maxAge:age,
    secure: process.env.NODE_ENV === "production" && process.env.ARTHA_INSECURE_COOKIE !== "1"
      || new URL(request.url).protocol === "https:" || request.headers.get("x-forwarded-proto") === "https",
  });
  return {location:dashboardFor(user)};
}

export async function logout(db) {
  const store = await cookies();
  const token = store.get(cookie)?.value;
  if (token) db.prepare("DELETE FROM sessions WHERE token_hash=?").run(tokenHash(token));
  store.delete(cookie);
}
