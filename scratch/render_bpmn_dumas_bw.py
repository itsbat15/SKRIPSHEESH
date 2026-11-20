import os
from pathlib import Path
import fitz

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
BAB2_DIR = ROOT / "DRAFT PROPOSAL MD" / "BAB 2" / "ASET BAB 2.1"
ASET_OLD_DIR = ROOT / "ASET BAB 2.1"
ARTIFACT_DIR = Path(r"C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb")

# Monochrome SVG for Gambar 2.3
svg_bw = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="1200" height="680" style="background:#ffffff; font-family:'Segoe UI', Inter, Arial, sans-serif;">
  <defs>
    <marker id="arrowSolid" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#000000"/>
    </marker>
    <marker id="arrowOpen" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <polyline points="1 1, 9 4, 1 7" fill="none" stroke="#000000" stroke-width="1.8"/>
    </marker>
    <marker id="circleOpen" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <circle cx="4" cy="4" r="3" fill="#FFFFFF" stroke="#000000" stroke-width="1.5"/>
    </marker>
  </defs>

  <!-- Title Card (Pure B&W) -->
  <rect x="40" y="20" width="1120" height="38" rx="4" fill="#FFFFFF" stroke="#000000" stroke-width="1.5"/>
  <text x="600" y="44" font-size="14" font-weight="700" fill="#000000" text-anchor="middle">Gambar 2.3 Contoh Alur Proses Bisnis Kolaboratif Antarorganisasi Berstandar BPMN (Dumas dkk., 2018)</text>

  <!-- Pool 1: Pelanggan (Black Box) -->
  <rect x="40" y="75" width="1120" height="85" fill="#F8F9FA" stroke="#000000" stroke-width="1.5" rx="2"/>
  <rect x="40" y="75" width="30" height="85" fill="#E9ECEF" stroke="#000000" stroke-width="1.5"/>
  <text x="55" y="117" font-size="11" font-weight="700" fill="#000000" text-anchor="middle" transform="rotate(-90 55 117)">Entitas Eksternal: Pelanggan</text>
  <text x="600" y="122" font-size="13" font-style="italic" fill="#333333" text-anchor="middle">[ Black-Box Pool: Detail Alur Internal Pelanggan Tidak Ditampilkan ]</text>

  <!-- Pool 2: Organisasi Penyedia Layanan (White Box) -->
  <rect x="40" y="205" width="1120" height="440" fill="#FFFFFF" stroke="#000000" stroke-width="2" rx="2"/>
  <!-- Pool Header -->
  <rect x="40" y="205" width="30" height="440" fill="#000000" stroke="#000000" stroke-width="2"/>
  <text x="55" y="425" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" transform="rotate(-90 55 425)">Organisasi Penyedia Layanan (Unit Pengelola)</text>

  <!-- Lane 1: Pelayanan & Administrasi -->
  <rect x="70" y="205" width="1090" height="220" fill="#FFFFFF" stroke="#000000" stroke-width="1.2"/>
  <rect x="70" y="205" width="26" height="220" fill="#F1F3F5" stroke="#000000" stroke-width="1.2"/>
  <text x="83" y="315" font-size="10" font-weight="700" fill="#000000" text-anchor="middle" transform="rotate(-90 83 315)">Divisi Pelayanan &amp; Administrasi</text>

  <!-- Lane 2: Keuangan & Verifikasi -->
  <rect x="70" y="425" width="1090" height="220" fill="#FFFFFF" stroke="#000000" stroke-width="1.2"/>
  <rect x="70" y="425" width="26" height="220" fill="#F1F3F5" stroke="#000000" stroke-width="1.2"/>
  <text x="83" y="535" font-size="10" font-weight="700" fill="#000000" text-anchor="middle" transform="rotate(-90 83 535)">Divisi Keuangan &amp; Verifikasi</text>

  <!-- START EVENT (Lane 1) -->
  <circle cx="140" cy="315" r="18" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
  <text x="140" y="348" font-size="10" font-weight="700" fill="#000000" text-anchor="middle">Permintaan</text>
  <text x="140" y="360" font-size="10" font-weight="700" fill="#000000" text-anchor="middle">Diterima</text>

  <!-- TASK 1: Memverifikasi Kelayakan Dokumen -->
  <rect x="205" y="287" width="140" height="56" rx="8" fill="#FFFFFF" stroke="#000000" stroke-width="1.8"/>
  <text x="275" y="312" font-size="11" font-weight="600" fill="#000000" text-anchor="middle">Memverifikasi</text>
  <text x="275" y="327" font-size="11" font-weight="600" fill="#000000" text-anchor="middle">Kelayakan Dokumen</text>

  <!-- DATA OBJECT: Formulir Permintaan -->
  <path d="M 255 225 L 285 225 L 295 235 L 295 265 L 255 265 Z" fill="#FFFFFF" stroke="#000000" stroke-width="1.5"/>
  <path d="M 285 225 L 285 235 L 295 235" fill="none" stroke="#000000" stroke-width="1.5"/>
  <text x="275" y="248" font-size="8" font-weight="600" fill="#000000" text-anchor="middle">Formulir</text>
  <text x="275" y="258" font-size="8" font-weight="600" fill="#000000" text-anchor="middle">Fisik</text>
  <line x1="275" y1="265" x2="275" y2="287" stroke="#000000" stroke-width="1.2" stroke-dasharray="3 3"/>

  <!-- XOR GATEWAY SPLIT -->
  <polygon points="390 315, 412 293, 434 315, 412 337" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
  <text x="412" y="321" font-size="16" font-weight="800" fill="#000000" text-anchor="middle">✕</text>

  <!-- TASK REVISI (LENGKAP = TIDAK) -->
  <rect x="465" y="230" width="145" height="50" rx="8" fill="#FFFFFF" stroke="#000000" stroke-width="1.8"/>
  <text x="537" y="252" font-size="11" font-weight="600" fill="#000000" text-anchor="middle">Mengirimkan Notifikasi</text>
  <text x="537" y="267" font-size="11" font-weight="600" fill="#000000" text-anchor="middle">Perbaikan Berkas</text>

  <!-- INTERMEDIATE EVENT (Lane 1) -->
  <circle cx="670" cy="255" r="17" fill="#FFFFFF" stroke="#000000" stroke-width="1.5"/>
  <circle cx="670" cy="255" r="13" fill="#FFFFFF" stroke="#000000" stroke-width="1.5"/>
  <rect x="663" y="249" width="14" height="11" fill="none" stroke="#000000" stroke-width="1.2"/>
  <polyline points="663 249, 670 255, 677 249" fill="none" stroke="#000000" stroke-width="1.2"/>
  <text x="670" y="284" font-size="10" font-weight="700" fill="#000000" text-anchor="middle">Berkas Revisi</text>
  <text x="670" y="295" font-size="10" font-weight="700" fill="#000000" text-anchor="middle">Diterima</text>

  <!-- TASK 2 (Lane 2): Menghitung Biaya & Tagihan -->
  <rect x="495" y="505" width="145" height="56" rx="8" fill="#FFFFFF" stroke="#000000" stroke-width="1.8"/>
  <text x="567" y="530" font-size="11" font-weight="600" fill="#000000" text-anchor="middle">Menghitung Biaya</text>
  <text x="567" y="545" font-size="11" font-weight="600" fill="#000000" text-anchor="middle">&amp; Validasi Tagihan</text>

  <!-- DATA STORE: Basis Data Finansial -->
  <g transform="translate(537, 580)">
    <ellipse cx="30" cy="8" rx="28" ry="7" fill="#FFFFFF" stroke="#000000" stroke-width="1.5"/>
    <rect x="2" y="8" width="56" height="24" fill="#FFFFFF" stroke="none"/>
    <line x1="2" y1="8" x2="2" y2="32" stroke="#000000" stroke-width="1.5"/>
    <line x1="58" y1="8" x2="58" y2="32" stroke="#000000" stroke-width="1.5"/>
    <path d="M 2 18 A 28 7 0 0 0 58 18" fill="none" stroke="#000000" stroke-width="1"/>
    <path d="M 2 32 A 28 7 0 0 0 58 32" fill="none" stroke="#000000" stroke-width="1.5"/>
    <text x="30" y="24" font-size="8" font-weight="600" fill="#000000" text-anchor="middle">Pangkalan Data</text>
  </g>
  <line x1="567" y1="561" x2="567" y2="580" stroke="#000000" stroke-width="1.2" stroke-dasharray="3 3"/>

  <!-- TASK 3 (Lane 2): Membukukan Transaksi -->
  <rect x="695" y="505" width="145" height="56" rx="8" fill="#FFFFFF" stroke="#000000" stroke-width="1.8"/>
  <text x="767" y="530" font-size="11" font-weight="600" fill="#000000" text-anchor="middle">Membukukan Transaksi</text>
  <text x="767" y="545" font-size="11" font-weight="600" fill="#000000" text-anchor="middle">ke Buku Rekening</text>

  <!-- XOR GATEWAY JOIN (Lane 1) -->
  <polygon points="860 315, 882 293, 904 315, 882 337" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
  <text x="882" y="321" font-size="16" font-weight="800" fill="#000000" text-anchor="middle">✕</text>

  <!-- TASK 4: Menerbitkan Kuitansi & Layanan -->
  <rect x="940" y="287" width="145" height="56" rx="8" fill="#FFFFFF" stroke="#000000" stroke-width="1.8"/>
  <text x="1012" y="312" font-size="11" font-weight="600" fill="#000000" text-anchor="middle">Menerbitkan Kuitansi</text>
  <text x="1012" y="327" font-size="11" font-weight="600" fill="#000000" text-anchor="middle">&amp; Dokumen Bukti</text>

  <!-- END EVENT (Lane 1) -->
  <circle cx="1115" cy="315" r="18" fill="#FFFFFF" stroke="#000000" stroke-width="5"/>
  <text x="1115" y="348" font-size="10" font-weight="700" fill="#000000" text-anchor="middle">Layanan Resmi</text>
  <text x="1115" y="360" font-size="10" font-weight="700" fill="#000000" text-anchor="middle">Telah Aktif</text>

  <!-- ==================== SEQUENCE FLOWS ==================== -->
  <line x1="158" y1="315" x2="205" y2="315" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <line x1="345" y1="315" x2="390" y2="315" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- Split -> Revisi [Tidak Lengkap] -->
  <path d="M 412 293 L 412 255 L 465 255" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <rect x="360" y="260" width="85" height="18" fill="#FFFFFF" stroke="#000000" stroke-width="0.8" rx="3"/>
  <text x="402" y="272" font-size="9" font-weight="700" fill="#000000" text-anchor="middle">Tidak Lengkap</text>

  <!-- Revisi -> Intermediate Event -->
  <line x1="610" y1="255" x2="653" y2="255" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <!-- Intermediate Event -> Loop back to Task 1 -->
  <path d="M 687 255 L 720 255 L 720 220 L 275 220 L 275 287" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- Split -> Task 2 [Dokumen Lengkap] -->
  <path d="M 412 337 L 412 533 L 495 533" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <rect x="360" y="355" width="95" height="18" fill="#FFFFFF" stroke="#000000" stroke-width="0.8" rx="3"/>
  <text x="407" y="367" font-size="9" font-weight="700" fill="#000000" text-anchor="middle">Dokumen Lengkap</text>

  <!-- Task 2 -> Task 3 -->
  <line x1="640" y1="533" x2="695" y2="533" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <!-- Task 3 -> XOR Join -->
  <path d="M 840 533 L 882 533 L 882 337" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <!-- XOR Join -> Task 4 -->
  <line x1="904" y1="315" x2="940" y2="315" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <!-- Task 4 -> End Event -->
  <line x1="1085" y1="315" x2="1097" y2="315" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- ==================== MESSAGE FLOWS (INTER-POOL) ==================== -->
  <line x1="140" y1="160" x2="140" y2="297" stroke="#000000" stroke-width="1.8" stroke-dasharray="6 4" marker-start="url(#circleOpen)" marker-end="url(#arrowOpen)"/>
  <rect x="85" y="172" width="110" height="20" fill="#FFFFFF" stroke="#000000" stroke-width="1" rx="4"/>
  <text x="140" y="186" font-size="9" font-weight="600" fill="#000000" text-anchor="middle">Kirim Permintaan</text>

  <line x1="537" y1="230" x2="537" y2="160" stroke="#000000" stroke-width="1.8" stroke-dasharray="6 4" marker-start="url(#circleOpen)" marker-end="url(#arrowOpen)"/>
  <rect x="475" y="172" width="125" height="20" fill="#FFFFFF" stroke="#000000" stroke-width="1" rx="4"/>
  <text x="537" y="186" font-size="9" font-weight="600" fill="#000000" text-anchor="middle">Notifikasi Perbaikan</text>

  <line x1="1012" y1="287" x2="1012" y2="160" stroke="#000000" stroke-width="1.8" stroke-dasharray="6 4" marker-start="url(#circleOpen)" marker-end="url(#arrowOpen)"/>
  <rect x="945" y="172" width="135" height="20" fill="#FFFFFF" stroke="#000000" stroke-width="1" rx="4"/>
  <text x="1012" y="186" font-size="9" font-weight="600" fill="#000000" text-anchor="middle">Kirim Kuitansi &amp; Bukti</text>

</svg>'''

svg_path = BAB2_DIR / "Gambar_2_3_Contoh_Diagram_BPMN_Dumas.svg"
svg_path.write_text(svg_bw, encoding="utf-8")

doc = fitz.open(stream=svg_bw.encode("utf-8"), filetype="svg")
page = doc.load_page(0)
pix = page.get_pixmap(dpi=300)

png_filename = "Gambar 2.3 Contoh Alur Proses Bisnis Kolaboratif BPMN Dumas 2018.png"
out_png1 = BAB2_DIR / png_filename
out_png2 = ASET_OLD_DIR / png_filename
artifact_png = ARTIFACT_DIR / "Gambar_2_3_Contoh_Diagram_BPMN_Dumas.png"

pix.save(str(out_png1))
pix.save(str(out_png2))
pix.save(str(artifact_png))
print(f"Saved pure monochrome Gambar 2.3 to {out_png1} ({pix.width}x{pix.height})")

