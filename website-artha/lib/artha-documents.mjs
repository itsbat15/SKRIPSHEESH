import { PDFDocument, rgb, StandardFonts } from "pdf-lib";
import ExcelJS from "exceljs";

const units = new Intl.NumberFormat("id-ID");
const money = (value) => `Rp ${units.format(value)}`;
const kind = (value) => value === "registration" ? "Pendaftaran dan SPP pertama" : "SPP bulanan";
const safe = (value) => String(value ?? "").normalize("NFKD").replace(/\p{M}/gu,"").replace(/[^\x20-\x7E]/g,"?");

async function pdf(title, subheading, lines) {
  const doc = await PDFDocument.create();
  doc.setTitle(title);
  const font = await doc.embedFont(StandardFonts.Helvetica);
  const bold = await doc.embedFont(StandardFonts.HelveticaBold);
  let page, y;
  const nextPage = () => {
    page = doc.addPage([595,842]);
    page.drawRectangle({x:0,y:746,width:595,height:96,color:rgb(0.15,0.15,0.90)});
    page.drawText("BIMBEL ARTHA",{x:42,y:806,size:11,font:bold,color:rgb(1,1,1)});
    page.drawText(title,{x:42,y:777,size:20,font:bold,color:rgb(1,1,1)});
    page.drawText(safe(subheading),{x:42,y:720,size:10,font});
    y = 688;
  };
  nextPage();
  for (const line of lines) {
    let remaining = safe(line), first = true;
    while (remaining.length || first) {
      first = false;
      if (y < 48) nextPage();
      let end = remaining.length;
      while (font.widthOfTextAtSize(remaining.slice(0,end),11)>510) end--;
      if (end < remaining.length && remaining.lastIndexOf(" ",end)>0) end = remaining.lastIndexOf(" ",end);
      page.drawText(remaining.slice(0,end),{x:42,y,size:11,font});
      remaining = remaining.slice(end).trimStart();
      y -= 24;
    }
  }
  return doc.save();
}

export function receipt(row) {
  return pdf("Kuitansi Pembayaran", `${row.branch_name} | ${row.branch_address.slice(0,65)}`,[
    `Nomor transaksi: ARTHA-${String(row.id).padStart(6,"0")}`,
    `Siswa: ${row.student_name}`,
    `Paket: ${row.package_name} | Periode: ${row.period} | ${kind(row.kind)}`,
    `Tanggal transaksi: ${row.recorded_on} | Tanggal pembukuan: ${row.recognized_on}`,
    `Metode: ${row.method === "cash" ? "Tunai" : "Transfer bank"}`,
    `Nominal transaksi: ${money(row.amount)}`,
    `Total tagihan: ${money(row.bill_amount)} | Status tagihan: Lunas`,
    `Dicatat oleh: ${row.cashier}`,
  ]);
}

export function closeReport(row) {
  return pdf("Berita Acara Kas Harian", `${row.branch_name} | ${row.day}`,[
    `Petugas: ${row.cashier}`,
    `Penerimaan tunai sistem: ${money(row.cash)}`,
    `Penerimaan transfer sistem: ${money(row.transfer)}`,
    `Kas fisik: ${money(row.physical)}`,
    `Selisih (fisik dikurangi sistem): ${money(row.physical-row.cash)}`,
    `Catatan: ${row.note || "-"}`,
    `Status: ${{submitted:"Ditutup",needs_review:"Perlu ditinjau",approved:"Disetujui"}[row.status]}`,
  ]);
}

export function revenuePdf(rows, from, to) {
  return pdf("Rekapitulasi Pendapatan", `Periode ${from} sampai ${to}`, [
    ...rows.map((r) => `${r.branch_name}: Tunai ${money(r.cash)} | Transfer ${money(r.transfer)} | Total ${money(r.cash+r.transfer)} (${r.transactions} transaksi)`),
    "",
    `Total pendapatan: ${money(rows.reduce((n,r)=>n+r.cash+r.transfer,0))}`,
  ]);
}

export async function revenueExcel(rows, from, to) {
  const book = new ExcelJS.Workbook();
  const sheet = book.addWorksheet("Pendapatan");
  sheet.addRow(["Rekapitulasi Pendapatan Bimbel Artha",from,to]);
  sheet.addRow(["Cabang","Tunai (Rp)","Transfer (Rp)","Total (Rp)","Jumlah transaksi"]);
  for (const row of rows) sheet.addRow([row.branch_name,row.cash,row.transfer,row.cash+row.transfer,row.transactions]);
  sheet.addRow(["Total",rows.reduce((n,r)=>n+r.cash,0),rows.reduce((n,r)=>n+r.transfer,0),
    rows.reduce((n,r)=>n+r.cash+r.transfer,0),rows.reduce((n,r)=>n+r.transactions,0)]);
  sheet.getRow(2).font={bold:true};
  sheet.columns.forEach((column,i)=>{ column.width=i === 0 ? 42 : 23; });
  return book.xlsx.writeBuffer();
}
