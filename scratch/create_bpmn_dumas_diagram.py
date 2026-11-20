import os
from pathlib import Path
import fitz  # PyMuPDF

# Paths
ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
BAB2_DIR = ROOT / "DRAFT PROPOSAL MD" / "BAB 2" / "ASET BAB 2.1"
ASET_OLD_DIR = ROOT / "ASET BAB 2.1"
ARTIFACT_DIR = Path(r"C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb")

BAB2_DIR.mkdir(parents=True, exist_ok=True)

# 1. Generate Draw.io XML
drawio_xml = '''<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="diagram_bpmn_dumas" name="Gambar 2.3 Contoh Kolaborasi BPMN Dumas 2018">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="680" background="#ffffff">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Box -->
        <mxCell id="title_box" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;Gambar 2.3 Contoh Alur Proses Bisnis Kolaboratif Antarorganisasi Berstandar BPMN (Dumas dkk., 2018)&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#F8F9FA;strokeColor=#495057;strokeWidth=1.5;align=center;" vertex="1" parent="1">
          <mxGeometry x="40" y="20" width="1120" height="36" as="geometry" />
        </mxCell>

        <!-- Pool 1: Pelanggan (Black-Box Pool) -->
        <mxCell id="pool_customer" value="&lt;b&gt;Entitas Eksternal: Pelanggan / Pemohon Layanan&lt;/b&gt;" style="swimlane;html=1;startSize=26;horizontal=0;fillColor=#E9ECEF;strokeColor=#495057;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="40" y="75" width="1120" height="90" as="geometry" />
        </mxCell>

        <!-- Pool 2: Organisasi Penyedia Layanan (White-Box Pool) -->
        <mxCell id="pool_org" value="&lt;b&gt;Organisasi Penyedia Layanan (Unit Pengelola)&lt;/b&gt;" style="swimlane;html=1;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;startSize=28;horizontal=0;horizontalStack=0;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="40" y="210" width="1120" height="420" as="geometry" />
        </mxCell>

        <!-- Lane 1: Divisi Pelayanan & Administrasi -->
        <mxCell id="lane_admin" value="&lt;b&gt;Divisi Pelayanan &amp; Administrasi&lt;/b&gt;" style="swimlane;html=1;startSize=26;horizontal=0;fillColor=#F8F9FA;strokeColor=#6C757D;strokeWidth=1.2;" vertex="1" parent="pool_org">
          <mxGeometry x="28" y="0" width="1092" height="210" as="geometry" />
        </mxCell>

        <!-- Lane 2: Divisi Keuangan & Verifikasi -->
        <mxCell id="lane_finance" value="&lt;b&gt;Divisi Keuangan &amp; Verifikasi&lt;/b&gt;" style="swimlane;html=1;startSize=26;horizontal=0;fillColor=#F8F9FA;strokeColor=#6C757D;strokeWidth=1.2;" vertex="1" parent="pool_org">
          <mxGeometry x="28" y="210" width="1092" height="210" as="geometry" />
        </mxCell>

        <!-- START EVENT -->
        <mxCell id="start_evt" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#EBFBEE;strokeColor=#2B8A3E;strokeWidth=2;" vertex="1" parent="lane_admin">
          <mxGeometry x="40" y="80" width="36" height="36" as="geometry" />
        </mxCell>
        <mxCell id="lbl_start" value="Permintaan&lt;br&gt;Diterima" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#2B8A3E;fontStyle=1;" vertex="1" parent="lane_admin">
          <mxGeometry x="20" y="122" width="76" height="30" as="geometry" />
        </mxCell>

        <!-- TASK 1: Memverifikasi Dokumen -->
        <mxCell id="task_1" value="Memverifikasi&lt;br&gt;Kelayakan Dokumen" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_admin">
          <mxGeometry x="120" y="70" width="130" height="56" as="geometry" />
        </mxCell>

        <!-- DATA OBJECT: Formulir Permintaan -->
        <mxCell id="do_form" value="Formulir&lt;br&gt;Permintaan" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;fillColor=#FFF9DB;strokeColor=#F59F00;strokeWidth=1.2;size=14;fontSize=9;align=center;" vertex="1" parent="lane_admin">
          <mxGeometry x="155" y="10" width="60" height="42" as="geometry" />
        </mxCell>

        <!-- XOR SPLIT -->
        <mxCell id="gw_split" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF9DB;strokeColor=#E67700;strokeWidth=2;fontSize=14;fontStyle=1;fontColor=#D9480F;" vertex="1" parent="lane_admin">
          <mxGeometry x="290" y="78" width="40" height="40" as="geometry" />
        </mxCell>

        <!-- TASK 1B: Meminta Perbaikan (Reject/Revise branch) -->
        <mxCell id="task_revisi" value="Mengirimkan Notifikasi&lt;br&gt;Perbaikan Berkas" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_admin">
          <mxGeometry x="370" y="15" width="140" height="50" as="geometry" />
        </mxCell>

        <!-- INTERMEDIATE EVENT: Menunggu Berkas -->
        <mxCell id="evt_inter" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFF9DB;strokeColor=#F59F00;strokeWidth=1.5;" vertex="1" parent="lane_admin">
          <mxGeometry x="550" y="24" width="32" height="32" as="geometry" />
        </mxCell>
        <mxCell id="evt_inter_inner" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFF9DB;strokeColor=#F59F00;strokeWidth=1.5;" vertex="1" parent="lane_admin">
          <mxGeometry x="554" y="28" width="24" height="24" as="geometry" />
        </mxCell>
        <mxCell id="lbl_inter" value="Berkas Revisi&lt;br&gt;Diterima" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#D9480F;fontStyle=1;" vertex="1" parent="lane_admin">
          <mxGeometry x="526" y="58" width="80" height="30" as="geometry" />
        </mxCell>

        <!-- TASK 2 (LANE 2): Menghitung Biaya & Tagihan -->
        <mxCell id="task_2" value="Menghitung Biaya&lt;br&gt;&amp;amp; Validasi Tagihan" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_finance">
          <mxGeometry x="440" y="75" width="130" height="56" as="geometry" />
        </mxCell>

        <!-- DATA STORE: Basis Data Finansial -->
        <mxCell id="ds_db" value="Pangkalan Data&lt;br&gt;Finansial" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=12;fillColor=#E7F5FF;strokeColor=#1971C2;strokeWidth=1.5;fontSize=9;align=center;" vertex="1" parent="lane_finance">
          <mxGeometry x="465" y="145" width="80" height="46" as="geometry" />
        </mxCell>

        <!-- TASK 3 (LANE 2): Mencatat Jurnal Pembayaran -->
        <mxCell id="task_3" value="Membukukan Transaksi&lt;br&gt;ke Buku Rekening" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_finance">
          <mxGeometry x="615" y="75" width="135" height="56" as="geometry" />
        </mxCell>

        <!-- XOR JOIN -->
        <mxCell id="gw_join" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF9DB;strokeColor=#E67700;strokeWidth=2;fontSize=14;fontStyle=1;fontColor=#D9480F;" vertex="1" parent="lane_admin">
          <mxGeometry x="790" y="78" width="40" height="40" as="geometry" />
        </mxCell>

        <!-- TASK 4: Menerbitkan Bukti Layanan -->
        <mxCell id="task_4" value="Menerbitkan Kuitansi&lt;br&gt;&amp;amp; Dokumen Bukti" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_admin">
          <mxGeometry x="870" y="70" width="135" height="56" as="geometry" />
        </mxCell>

        <!-- END EVENT -->
        <mxCell id="end_evt" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFF5F5;strokeColor=#C92A2A;strokeWidth=4.5;" vertex="1" parent="lane_admin">
          <mxGeometry x="1040" y="80" width="36" height="36" as="geometry" />
        </mxCell>
        <mxCell id="lbl_end" value="Layanan Resmi&lt;br&gt;Telah Aktif" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#C92A2A;fontStyle=1;" vertex="1" parent="lane_admin">
          <mxGeometry x="1015" y="122" width="86" height="30" as="geometry" />
        </mxCell>

        <!-- ==================== FLOWS ==================== -->
        <!-- Sequence Flows Lane 1 -->
        <mxCell id="sf1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="start_evt" target="task_1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="sf2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_1" target="gw_split">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Branch: Tidak Lengkap -->
        <mxCell id="sf_revisi" value="[Tidak Lengkap]" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=0.5;exitY=0;fontSize=10;fontColor=#C92A2A;" edge="1" parent="1" source="gw_split" target="task_revisi">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="sf_rev_inter" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_revisi" target="evt_inter">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="sf_loop" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0.5;entryY=0;exitX=1;exitY=0.5;" edge="1" parent="1" source="evt_inter" target="task_1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="640" y="249" />
              <mxPoint x="640" y="270" />
              <mxPoint x="213" y="270" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Branch: Lengkap -> Lane 2 -->
        <mxCell id="sf_lengkap" value="[Dokumen Lengkap]" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=0.5;exitY=1;fontSize=10;fontColor=#2B8A3E;" edge="1" parent="1" source="gw_split" target="task_2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="sf3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_2" target="task_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="sf4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0.5;entryY=1;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_3" target="gw_join">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="sf5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="gw_join" target="task_4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="sf6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_4" target="end_evt">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Data Associations (Dotted) -->
        <mxCell id="da1" style="edgeStyle=none;rounded=0;html=1;dashed=1;strokeColor=#868E96;strokeWidth=1.2;entryX=0.5;entryY=0;exitX=0.5;exitY=1;" edge="1" parent="1" source="do_form" target="task_1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="da2" style="edgeStyle=none;rounded=0;html=1;dashed=1;strokeColor=#868E96;strokeWidth=1.2;entryX=0.5;entryY=0;exitX=0.5;exitY=1;" edge="1" parent="1" source="task_2" target="ds_db">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Message Flows between Customer and Org (Dashed with open circle start and open arrowhead) -->
        <mxCell id="mf1" value="Kirim Berkas Permintaan" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;dashed=1;dashPattern=5 5;strokeColor=#495057;strokeWidth=1.5;startArrow=oval;startFill=0;endArrow=open;entryX=0.5;entryY=0;exitX=0.15;exitY=1;fontSize=10;fontColor=#495057;" edge="1" parent="1" source="pool_customer" target="start_evt">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="mf2" value="Kirim Notifikasi Revisi" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;dashed=1;dashPattern=5 5;strokeColor=#495057;strokeWidth=1.5;startArrow=oval;startFill=0;endArrow=open;entryX=0.45;entryY=1;exitX=0.5;exitY=0;fontSize=10;fontColor=#495057;" edge="1" parent="1" source="task_revisi" target="pool_customer">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="mf3" value="Kirim Bukti Kuitansi &amp; Layanan" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;dashed=1;dashPattern=5 5;strokeColor=#495057;strokeWidth=1.5;startArrow=oval;startFill=0;endArrow=open;entryX=0.88;entryY=1;exitX=0.5;exitY=0;fontSize=10;fontColor=#495057;" edge="1" parent="1" source="task_4" target="pool_customer">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

# Write drawio file to both asset folders
out_drawio1 = BAB2_DIR / "Gambar_2_3_Contoh_Diagram_BPMN_Dumas.drawio"
out_drawio2 = ASET_OLD_DIR / "Gambar_2_3_Contoh_Diagram_BPMN_Dumas.drawio"
out_drawio1.write_text(drawio_xml, encoding="utf-8")
out_drawio2.write_text(drawio_xml, encoding="utf-8")
print(f"Saved Drawio to {out_drawio1}")

# 2. Render SVG
svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="1200" height="680" style="background:#ffffff; font-family:'Segoe UI', Inter, Arial, sans-serif;">
  <defs>
    <filter id="cardShadow" x="-2%" y="-2%" width="104%" height="106%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <marker id="arrowSolid" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#000000"/>
    </marker>
    <marker id="arrowOpen" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <polyline points="1 1, 9 4, 1 7" fill="none" stroke="#495057" stroke-width="1.8"/>
    </marker>
    <marker id="circleOpen" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <circle cx="4" cy="4" r="3" fill="#FFFFFF" stroke="#495057" stroke-width="1.5"/>
    </marker>
  </defs>

  <!-- Title Card -->
  <rect x="40" y="20" width="1120" height="38" rx="4" fill="#F8F9FA" stroke="#495057" stroke-width="1.5"/>
  <text x="600" y="44" font-size="14" font-weight="700" fill="#212529" text-anchor="middle">Gambar 2.3 Contoh Alur Proses Bisnis Kolaboratif Antarorganisasi Berstandar BPMN (Dumas dkk., 2018)</text>

  <!-- Pool 1: Pelanggan (Black Box) -->
  <rect x="40" y="75" width="1120" height="85" fill="#E9ECEF" stroke="#495057" stroke-width="1.5" rx="2" filter="url(#cardShadow)"/>
  <rect x="40" y="75" width="30" height="85" fill="#CED4DA" stroke="#495057" stroke-width="1.5"/>
  <text x="55" y="117" font-size="11" font-weight="700" fill="#212529" text-anchor="middle" transform="rotate(-90 55 117)">Entitas Eksternal: Pelanggan</text>
  <text x="600" y="122" font-size="13" font-style="italic" fill="#495057" text-anchor="middle">[ Black-Box Pool: Detail Alur Internal Pelanggan Tidak Ditampilkan ]</text>

  <!-- Pool 2: Organisasi Penyedia Layanan (White Box) -->
  <rect x="40" y="205" width="1120" height="440" fill="#FFFFFF" stroke="#000000" stroke-width="2" rx="2" filter="url(#cardShadow)"/>
  <!-- Pool Header -->
  <rect x="40" y="205" width="30" height="440" fill="#212529" stroke="#000000" stroke-width="2"/>
  <text x="55" y="425" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" transform="rotate(-90 55 425)">Organisasi Penyedia Layanan (Unit Pengelola)</text>

  <!-- Lane 1: Pelayanan & Administrasi -->
  <rect x="70" y="205" width="1090" height="220" fill="#FCFCFD" stroke="#ADB5BD" stroke-width="1.2"/>
  <rect x="70" y="205" width="26" height="220" fill="#E9ECEF" stroke="#ADB5BD" stroke-width="1.2"/>
  <text x="83" y="315" font-size="10" font-weight="700" fill="#343A40" text-anchor="middle" transform="rotate(-90 83 315)">Divisi Pelayanan &amp; Administrasi</text>

  <!-- Lane 2: Keuangan & Verifikasi -->
  <rect x="70" y="425" width="1090" height="220" fill="#F8F9FA" stroke="#ADB5BD" stroke-width="1.2"/>
  <rect x="70" y="425" width="26" height="220" fill="#E9ECEF" stroke="#ADB5BD" stroke-width="1.2"/>
  <text x="83" y="535" font-size="10" font-weight="700" fill="#343A40" text-anchor="middle" transform="rotate(-90 83 535)">Divisi Keuangan &amp; Verifikasi</text>

  <!-- START EVENT (Lane 1) -->
  <circle cx="140" cy="315" r="18" fill="#EBFBEE" stroke="#2B8A3E" stroke-width="2.5"/>
  <text x="140" y="348" font-size="10" font-weight="700" fill="#2B8A3E" text-anchor="middle">Permintaan</text>
  <text x="140" y="360" font-size="10" font-weight="700" fill="#2B8A3E" text-anchor="middle">Diterima</text>

  <!-- TASK 1: Memverifikasi Kelayakan Dokumen -->
  <rect x="205" y="287" width="140" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="275" y="312" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Memverifikasi</text>
  <text x="275" y="327" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Kelayakan Dokumen</text>

  <!-- DATA OBJECT: Formulir Permintaan -->
  <path d="M 255 225 L 285 225 L 295 235 L 295 265 L 255 265 Z" fill="#FFF9DB" stroke="#F59F00" stroke-width="1.5"/>
  <path d="M 285 225 L 285 235 L 295 235" fill="none" stroke="#F59F00" stroke-width="1.5"/>
  <text x="275" y="248" font-size="8" font-weight="600" fill="#D9480F" text-anchor="middle">Formulir</text>
  <text x="275" y="258" font-size="8" font-weight="600" fill="#D9480F" text-anchor="middle">Fisik</text>
  <line x1="275" y1="265" x2="275" y2="287" stroke="#ADB5BD" stroke-width="1.2" stroke-dasharray="3 3"/>

  <!-- XOR GATEWAY SPLIT -->
  <polygon points="390 315, 412 293, 434 315, 412 337" fill="#FFF9DB" stroke="#E67700" stroke-width="2"/>
  <text x="412" y="321" font-size="16" font-weight="800" fill="#D9480F" text-anchor="middle">✕</text>

  <!-- TASK REVISI (LENGKAP = TIDAK) -->
  <rect x="465" y="230" width="145" height="50" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="537" y="252" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Mengirimkan Notifikasi</text>
  <text x="537" y="267" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Perbaikan Berkas</text>

  <!-- INTERMEDIATE EVENT (Lane 1) -->
  <circle cx="670" cy="255" r="17" fill="#FFF9DB" stroke="#F59F00" stroke-width="1.8"/>
  <circle cx="670" cy="255" r="13" fill="#FFF9DB" stroke="#F59F00" stroke-width="1.8"/>
  <!-- Envelope Icon inside Intermediate Event -->
  <rect x="663" y="249" width="14" height="11" fill="none" stroke="#E67700" stroke-width="1.2"/>
  <polyline points="663 249, 670 255, 677 249" fill="none" stroke="#E67700" stroke-width="1.2"/>
  <text x="670" y="284" font-size="10" font-weight="700" fill="#D9480F" text-anchor="middle">Berkas Revisi</text>
  <text x="670" y="295" font-size="10" font-weight="700" fill="#D9480F" text-anchor="middle">Diterima</text>

  <!-- TASK 2 (Lane 2): Menghitung Biaya & Tagihan -->
  <rect x="495" y="505" width="145" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="567" y="530" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Menghitung Biaya</text>
  <text x="567" y="545" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">&amp; Validasi Tagihan</text>

  <!-- DATA STORE: Basis Data Finansial -->
  <g transform="translate(537, 580)">
    <ellipse cx="30" cy="8" rx="28" ry="7" fill="#E7F5FF" stroke="#1971C2" stroke-width="1.5"/>
    <rect x="2" y="8" width="56" height="24" fill="#E7F5FF" stroke="none"/>
    <line x1="2" y1="8" x2="2" y2="32" stroke="#1971C2" stroke-width="1.5"/>
    <line x1="58" y1="8" x2="58" y2="32" stroke="#1971C2" stroke-width="1.5"/>
    <path d="M 2 18 A 28 7 0 0 0 58 18" fill="none" stroke="#1971C2" stroke-width="1"/>
    <path d="M 2 32 A 28 7 0 0 0 58 32" fill="none" stroke="#1971C2" stroke-width="1.5"/>
    <text x="30" y="24" font-size="8" font-weight="600" fill="#1864AB" text-anchor="middle">Pangkalan Data</text>
  </g>
  <line x1="567" y1="561" x2="567" y2="580" stroke="#ADB5BD" stroke-width="1.2" stroke-dasharray="3 3"/>

  <!-- TASK 3 (Lane 2): Membukukan Transaksi -->
  <rect x="695" y="505" width="145" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="767" y="530" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Membukukan Transaksi</text>
  <text x="767" y="545" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">ke Buku Rekening</text>

  <!-- XOR GATEWAY JOIN (Lane 1) -->
  <polygon points="860 315, 882 293, 904 315, 882 337" fill="#FFF9DB" stroke="#E67700" stroke-width="2"/>
  <text x="882" y="321" font-size="16" font-weight="800" fill="#D9480F" text-anchor="middle">✕</text>

  <!-- TASK 4: Menerbitkan Kuitansi & Layanan -->
  <rect x="940" y="287" width="145" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="1012" y="312" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Menerbitkan Kuitansi</text>
  <text x="1012" y="327" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">&amp; Dokumen Bukti</text>

  <!-- END EVENT (Lane 1) -->
  <circle cx="1115" cy="315" r="18" fill="#FFF5F5" stroke="#C92A2A" stroke-width="4.5"/>
  <text x="1115" y="348" font-size="10" font-weight="700" fill="#C92A2A" text-anchor="middle">Layanan Resmi</text>
  <text x="1115" y="360" font-size="10" font-weight="700" fill="#C92A2A" text-anchor="middle">Telah Aktif</text>

  <!-- ==================== SEQUENCE FLOWS ==================== -->
  <!-- Start -> Task 1 -->
  <line x1="158" y1="315" x2="205" y2="315" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <!-- Task 1 -> XOR Split -->
  <line x1="345" y1="315" x2="390" y2="315" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- Split -> Revisi [Tidak Lengkap] -->
  <path d="M 412 293 L 412 255 L 465 255" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <rect x="360" y="260" width="85" height="18" fill="#FFF5F5" stroke="#FFA8A8" stroke-width="0.8" rx="3"/>
  <text x="402" y="272" font-size="9" font-weight="700" fill="#C92A2A" text-anchor="middle">Tidak Lengkap</text>

  <!-- Revisi -> Intermediate Event -->
  <line x1="610" y1="255" x2="653" y2="255" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <!-- Intermediate Event -> Loop back to Task 1 -->
  <path d="M 687 255 L 720 255 L 720 220 L 275 220 L 275 287" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- Split -> Task 2 [Dokumen Lengkap] -->
  <path d="M 412 337 L 412 533 L 495 533" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <rect x="360" y="355" width="95" height="18" fill="#EBFBEE" stroke="#8CE99A" stroke-width="0.8" rx="3"/>
  <text x="407" y="367" font-size="9" font-weight="700" fill="#2B8A3E" text-anchor="middle">Dokumen Lengkap</text>

  <!-- Task 2 -> Task 3 -->
  <line x1="640" y1="533" x2="695" y2="533" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- Task 3 -> XOR Join -->
  <path d="M 840 533 L 882 533 L 882 337" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- XOR Join -> Task 4 -->
  <line x1="904" y1="315" x2="940" y2="315" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <!-- Task 4 -> End Event -->
  <line x1="1085" y1="315" x2="1097" y2="315" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- ==================== MESSAGE FLOWS (INTER-POOL) ==================== -->
  <!-- 1. Customer -> Start Event -->
  <line x1="140" y1="160" x2="140" y2="297" stroke="#495057" stroke-width="1.8" stroke-dasharray="6 4" marker-start="url(#circleOpen)" marker-end="url(#arrowOpen)"/>
  <rect x="85" y="172" width="110" height="20" fill="#F1F3F5" stroke="#CED4DA" stroke-width="1" rx="4"/>
  <text x="140" y="186" font-size="9" font-weight="600" fill="#495057" text-anchor="middle">Kirim Permintaan</text>

  <!-- 2. Task Revisi -> Customer -->
  <line x1="537" y1="230" x2="537" y2="160" stroke="#495057" stroke-width="1.8" stroke-dasharray="6 4" marker-start="url(#circleOpen)" marker-end="url(#arrowOpen)"/>
  <rect x="475" y="172" width="125" height="20" fill="#F1F3F5" stroke="#CED4DA" stroke-width="1" rx="4"/>
  <text x="537" y="186" font-size="9" font-weight="600" fill="#495057" text-anchor="middle">Notifikasi Perbaikan</text>

  <!-- 3. Task 4 -> Customer -->
  <line x1="1012" y1="287" x2="1012" y2="160" stroke="#495057" stroke-width="1.8" stroke-dasharray="6 4" marker-start="url(#circleOpen)" marker-end="url(#arrowOpen)"/>
  <rect x="945" y="172" width="135" height="20" fill="#F1F3F5" stroke="#CED4DA" stroke-width="1" rx="4"/>
  <text x="1012" y="186" font-size="9" font-weight="600" fill="#495057" text-anchor="middle">Kirim Kuitansi &amp; Bukti</text>

</svg>'''

# Save SVG
svg_path = BAB2_DIR / "Gambar_2_3_Contoh_Diagram_BPMN_Dumas.svg"
svg_path.write_text(svg_content, encoding="utf-8")
print(f"Saved SVG to {svg_path}")

# Render to 300 DPI PNG via PyMuPDF
doc = fitz.open(stream=svg_content.encode("utf-8"), filetype="svg")
page = doc.load_page(0)
pix = page.get_pixmap(dpi=300)

png_filename = "Gambar 2.3 Contoh Alur Proses Bisnis Kolaboratif BPMN Dumas 2018.png"
out_png1 = BAB2_DIR / png_filename
out_png2 = ASET_OLD_DIR / png_filename
artifact_png = ARTIFACT_DIR / "Gambar_2_3_Contoh_Diagram_BPMN_Dumas.png"

pix.save(str(out_png1))
pix.save(str(out_png2))
pix.save(str(artifact_png))
print(f"Saved PNG to {out_png1}")
print(f"PNG resolution: {pix.width}x{pix.height}")

