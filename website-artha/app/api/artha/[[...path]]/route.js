import { getDatabase } from "@/lib/artha-db.mjs";
import { closeReport, receipt, revenueExcel, revenuePdf } from "@/lib/artha-documents.mjs";
import { InputError, mutate, paymentDocument, reconciliationDocument, revenue } from "@/lib/artha-operations.mjs";
import { currentUser, login, logout } from "@/lib/artha-session";

export const runtime = "nodejs";

const privateHeaders = {"Cache-Control":"private, no-store","X-Content-Type-Options":"nosniff"};
const json = (data, status = 200) => Response.json(data,{status,headers:privateHeaders});
const pdf = "application/pdf";
const xlsx = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";

function file(body, type, filename, inline = true) {
  return new Response(new Uint8Array(body),{headers:{
    ...privateHeaders,
    "Content-Type":type,
    "Content-Disposition":`${inline ? "inline" : "attachment"}; filename="${filename}"`,
    "Content-Security-Policy":"default-src 'none'; frame-ancestors 'self'",
  }});
}

function failure(error) {
  if (error instanceof InputError) return json({error:error.message},error.status);
  if (error.errcode === 2067) return json({error:"Data sudah terdaftar. Periksa nama, tanggal lahir, atau email."},409);
  console.error("Artha operation failed:",error.code || error.name);
  return json({error:"Terjadi gangguan. Silakan coba kembali."},500);
}

async function signedIn(db) {
  const user = await currentUser(db);
  if (!user) throw new InputError("Silakan masuk kembali.",401);
  return user;
}

function sameOrigin(request) {
  const site = request.headers.get("sec-fetch-site");
  if (site && site !== "same-origin" && site !== "none") return false;
  const origin = request.headers.get("origin");
  if (!origin || site === "same-origin") return true;
  return new URL(origin).host === (request.headers.get("x-forwarded-host") || request.headers.get("host") || new URL(request.url).host);
}

export async function POST(request,{params}) {
  try {
    const {path = []} = await params;
    if (path.length !== 1) throw new InputError("Halaman tidak ditemukan.",404);
    if (!sameOrigin(request)) throw new InputError("Permintaan tidak diizinkan.",403);
    const db = getDatabase();
    if (path[0] === "logout") {
      await logout(db);
      return json({location:"/login"});
    }
    const user = path[0] === "login" ? null : await signedIn(db);
    if (Number(request.headers.get("content-length")) > 6*1024*1024) {
      throw new InputError("Berkas unggahan terlalu besar.",413);
    }
    const data = await request.formData().catch(() => {throw new InputError("Formulir tidak valid.");});
    if (path[0] === "login") return json(await login(db,data,request));
    return json(await mutate(db,user,path[0],data) || {ok:true});
  } catch (error) {
    return failure(error);
  }
}

export async function GET(request,{params}) {
  try {
    const {path = []} = await params;
    const [action, raw] = path;
    const db = getDatabase(), user = await signedIn(db);
    if (action === "report" && path.length === 1) {
      if (user.role !== "super_admin") throw new InputError("Anda tidak memiliki akses.",403);
      const q = new URL(request.url).searchParams;
      const from=q.get("from"),to=q.get("to");
      const rows = revenue(db,user,from,to,q.get("branch"));
      if (q.get("format") === "xlsx") return file(await revenueExcel(rows,from,to),xlsx,"rekap-artha.xlsx",false);
      return file(await revenuePdf(rows,from,to),pdf,"rekap-artha.pdf");
    }
    const id = Number(raw);
    if (path.length !== 2 || !Number.isSafeInteger(id) || id<1) throw new InputError("Data tidak ditemukan.",404);
    if (action === "proof") {
      const proof = paymentDocument(db,user,id,action);
      return file(proof.body,proof.file_type,`bukti-${id}.${{"image/jpeg":"jpg","image/png":"png","application/pdf":"pdf"}[proof.file_type]}`);
    }
    if (action === "receipt") return file(await receipt(paymentDocument(db,user,id,action)),pdf,`kuitansi-${id}.pdf`);
    if (action === "close") return file(await closeReport(reconciliationDocument(db,user,id)),pdf,`kas-harian-${id}.pdf`);
    throw new InputError("Halaman tidak ditemukan.",404);
  } catch (error) {
    return failure(error);
  }
}
