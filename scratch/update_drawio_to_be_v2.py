import os
from pathlib import Path
import fitz  # PyMuPDF

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
BAB3_ASET = ROOT / "DRAFT PROPOSAL MD" / "BAB 3" / "ASET BAB 3"
BAB3_OLD_ASET = ROOT / "DRAFT PROPOSAL MD" / "BAB 3" / "3.4 Konsep Prototipe MD" / "ASET BAB 3"
ARTIFACT_DIR = Path(r"C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb")

BAB3_ASET.mkdir(parents=True, exist_ok=True)

# 1. DRAW.IO XML GENERATION
drawio_xml = '''<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="diagram_bpmn_tobe_v2" name="BPMN To-Be ARTHA (2 End Events)">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1880" pageHeight="780" background="#ffffff">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Box -->
        <mxCell id="title_box" value="&lt;b style=&quot;font-size: 15px;&quot;&gt;Gambar 3.2 Proses Bisnis Usulan (To-Be) Operasional Terintegrasi Bimbel ARTHA (Sesuai Dumas et al., 2018)&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#EBFBEE;strokeColor=#2B8A3E;strokeWidth=1.5;align=center;" vertex="1" parent="1">
          <mxGeometry x="40" y="20" width="1800" height="40" as="geometry" />
        </mxCell>

        <!-- Pool: Bimbel ARTHA Usulan -->
        <mxCell id="pool_tobe" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Bimbingan Belajar ARTHA Balikpapan (Proses Usulan / To-Be)&lt;/b&gt;" style="swimlane;html=1;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;startSize=30;horizontal=0;horizontalStack=0;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="40" y="75" width="1800" height="660" as="geometry" />
        </mxCell>

        <!-- Lane 1: Wali Murid / Siswa -->
        <mxCell id="lane_wali" value="&lt;b&gt;Wali Murid / Siswa&lt;/b&gt;" style="swimlane;html=1;startSize=26;horizontal=0;fillColor=#F1F3F5;strokeColor=#495057;strokeWidth=1.2;" vertex="1" parent="pool_tobe">
          <mxGeometry x="30" y="0" width="1770" height="210" as="geometry" />
        </mxCell>

        <!-- Lane 2: Staf Administrasi Cabang -->
        <mxCell id="lane_staf" value="&lt;b&gt;Staf Administrasi Cabang&lt;br&gt;(Kak Agian)&lt;/b&gt;" style="swimlane;html=1;startSize=26;horizontal=0;fillColor=#FFFFFF;strokeColor=#495057;strokeWidth=1.2;" vertex="1" parent="pool_tobe">
          <mxGeometry x="30" y="210" width="1770" height="230" as="geometry" />
        </mxCell>

        <!-- Lane 3: Pengelola Keuangan Pusat -->
        <mxCell id="lane_pemilik" value="&lt;b&gt;Pengelola Keuangan Pusat&lt;br&gt;(Ibu Emi / Pemilik)&lt;/b&gt;" style="swimlane;html=1;startSize=26;horizontal=0;fillColor=#F8F9FA;strokeColor=#495057;strokeWidth=1.2;" vertex="1" parent="pool_tobe">
          <mxGeometry x="30" y="440" width="1770" height="220" as="geometry" />
        </mxCell>

        <!-- ==================== LANE 1: WALI MURID ==================== -->
        <!-- Start Event -->
        <mxCell id="start_tb" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#EBFBEE;strokeColor=#2B8A3E;strokeWidth=2;" vertex="1" parent="lane_wali">
          <mxGeometry x="40" y="85" width="36" height="36" as="geometry" />
        </mxCell>
        <mxCell id="lbl_start" value="Mulai" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=11;fontColor=#2B8A3E;fontStyle=1;" vertex="1" parent="lane_wali">
          <mxGeometry x="35" y="125" width="46" height="20" as="geometry" />
        </mxCell>

        <!-- Task 1: Mengisi Formulir -->
        <mxCell id="task_1" value="Mengisi Lembar Formulir&lt;br&gt;Pendaftaran di Meja Cabang" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_wali">
          <mxGeometry x="110" y="75" width="150" height="56" as="geometry" />
        </mxCell>

        <!-- Data Object: Formulir Fisik -->
        <mxCell id="do_form" value="Formulir Fisik&lt;br&gt;Pendaftaran" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;fillColor=#FFF9DB;strokeColor=#F59F00;strokeWidth=1.2;size=14;fontSize=9;align=center;" vertex="1" parent="lane_wali">
          <mxGeometry x="145" y="12" width="80" height="45" as="geometry" />
        </mxCell>

        <!-- Task 4b: Transfer via m-Banking -->
        <mxCell id="task_4b" value="Mentransfer Biaya via&lt;br&gt;m-Banking &amp;amp; Kirim Bukti" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_wali">
          <mxGeometry x="690" y="75" width="150" height="56" as="geometry" />
        </mxCell>

        <!-- Data Object: Bukti Transfer -->
        <mxCell id="do_bukti" value="Bukti Transfer&lt;br&gt;/ QRIS" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;fillColor=#FFF9DB;strokeColor=#F59F00;strokeWidth=1.2;size=14;fontSize=9;align=center;" vertex="1" parent="lane_wali">
          <mxGeometry x="725" y="12" width="80" height="45" as="geometry" />
        </mxCell>

        <!-- End Event 1: Siswa Terdaftar -->
        <mxCell id="end_siswa" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFF5F5;strokeColor=#C92A2A;strokeWidth=4.5;" vertex="1" parent="lane_wali">
          <mxGeometry x="1690" y="85" width="36" height="36" as="geometry" />
        </mxCell>
        <mxCell id="lbl_end_siswa" value="&lt;b&gt;Siswa Resmi Terdaftar &amp;amp;&lt;br&gt;Siap Mengikuti KBM&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#C92A2A;" vertex="1" parent="lane_wali">
          <mxGeometry x="1635" y="127" width="146" height="30" as="geometry" />
        </mxCell>

        <!-- ==================== LANE 2: STAF ADMINISTRASI ==================== -->
        <!-- Task 2: Input Web ARTHA -->
        <mxCell id="task_2" value="Memasukkan Data Siswa ke&lt;br&gt;Aplikasi Web ARTHA" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_staf">
          <mxGeometry x="270" y="80" width="150" height="56" as="geometry" />
        </mxCell>

        <!-- Data Store: Basis Data MySQL Cloud -->
        <mxCell id="ds_mysql" value="Basis Data Terpusat&lt;br&gt;MySQL Cloud" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=12;fillColor=#E7F5FF;strokeColor=#1971C2;strokeWidth=1.5;fontSize=9;align=center;" vertex="1" parent="lane_staf">
          <mxGeometry x="300" y="150" width="90" height="52" as="geometry" />
        </mxCell>

        <!-- Task 3: Memeriksa Kuota Sesi -->
        <mxCell id="task_3" value="Memeriksa Ketersediaan&lt;br&gt;Kuota Sesi secara Digital" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_staf">
          <mxGeometry x="445" y="80" width="150" height="56" as="geometry" />
        </mxCell>

        <!-- XOR SPLIT: METODE PEMBAYARAN -->
        <mxCell id="gw_split_metode" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF9DB;strokeColor=#E67700;strokeWidth=2;fontSize=14;fontStyle=1;fontColor=#D9480F;" vertex="1" parent="lane_staf">
          <mxGeometry x="615" y="88" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="lbl_gw_metode" value="Metode&lt;br&gt;Pembayaran?" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=bottom;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#D9480F;fontStyle=1;" vertex="1" parent="lane_staf">
          <mxGeometry x="595" y="52" width="80" height="30" as="geometry" />
        </mxCell>

        <!-- Task 4a: Terima Uang Tunai -->
        <mxCell id="task_4a" value="Menerima Uang Tunai &amp;amp;&lt;br&gt;Konfirmasi Lunas di Web" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_staf">
          <mxGeometry x="690" y="145" width="150" height="56" as="geometry" />
        </mxCell>

        <!-- Task 4c: Mengunggah Bukti Pembayaran -->
        <mxCell id="task_4c" value="Mengunggah Bukti Transfer&lt;br&gt;ke Dasbor Cabang Web" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_staf">
          <mxGeometry x="875" y="80" width="150" height="56" as="geometry" />
        </mxCell>

        <!-- Task 5 Rejection Notice -->
        <mxCell id="task_5_rej" value="Menolak Bukti &amp;amp; Meminta&lt;br&gt;Koreksi Bukti Bayar" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFF5F5;strokeColor=#E03131;strokeWidth=1.5;fontSize=10;fontColor=#C92A2A;" vertex="1" parent="lane_staf">
          <mxGeometry x="1055" y="150" width="140" height="50" as="geometry" />
        </mxCell>

        <!-- XOR JOIN: PEMBAYARAN SAH -->
        <mxCell id="gw_join_pay" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF9DB;strokeColor=#E67700;strokeWidth=2;fontSize=14;fontStyle=1;fontColor=#D9480F;" vertex="1" parent="lane_staf">
          <mxGeometry x="1225" y="88" width="40" height="40" as="geometry" />
        </mxCell>

        <!-- PARALLEL GATEWAY (AND-SPLIT +) -->
        <mxCell id="gw_and_split" value="+" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF9DB;strokeColor=#E67700;strokeWidth=2;fontSize=18;fontStyle=1;fontColor=#D9480F;" vertex="1" parent="lane_staf">
          <mxGeometry x="1295" y="88" width="40" height="40" as="geometry" />
        </mxCell>

        <!-- Task 6: Cetak Kuitansi PDF -->
        <mxCell id="task_6" value="Mencetak Kuitansi Resmi&lt;br&gt;Format PDF Digital" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_staf">
          <mxGeometry x="1365" y="80" width="145" height="56" as="geometry" />
        </mxCell>

        <!-- Data Object: Kuitansi PDF -->
        <mxCell id="do_pdf" value="Kuitansi Resmi&lt;br&gt;PDF Digital" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;fillColor=#FFF9DB;strokeColor=#F59F00;strokeWidth=1.2;size=14;fontSize=9;align=center;" vertex="1" parent="lane_staf">
          <mxGeometry x="1400" y="152" width="75" height="45" as="geometry" />
        </mxCell>

        <!-- Task 7: Menyerahkan Kuitansi & Tempatkan Siswa -->
        <mxCell id="task_7" value="Menyerahkan Kuitansi &amp;amp;&lt;br&gt;Menempatkan Siswa ke Rombel" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_staf">
          <mxGeometry x="1535" y="80" width="155" height="56" as="geometry" />
        </mxCell>

        <!-- ==================== LANE 3: MANAJEMEN PUSAT ==================== -->
        <!-- Task 5: Validasi Bukti Transfer -->
        <mxCell id="task_5" value="Memvalidasi Bukti Transfer&lt;br&gt;via Dasbor Pusat (Web)" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_pemilik">
          <mxGeometry x="875" y="70" width="150" height="56" as="geometry" />
        </mxCell>

        <!-- XOR SPLIT: BUKTI VALID? -->
        <mxCell id="gw_split_valid" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF9DB;strokeColor=#E67700;strokeWidth=2;fontSize=14;fontStyle=1;fontColor=#D9480F;" vertex="1" parent="lane_pemilik">
          <mxGeometry x="1055" y="78" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="lbl_gw_valid" value="Bukti Bayar&lt;br&gt;Valid?" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=bottom;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#D9480F;fontStyle=1;" vertex="1" parent="lane_pemilik">
          <mxGeometry x="1035" y="42" width="80" height="30" as="geometry" />
        </mxCell>

        <!-- Task 8: Monitoring Rekapitulasi Kas Cabang -->
        <mxCell id="task_8" value="Memantau Rekapitulasi Kas&lt;br&gt;8 Cabang via Dasbor Pusat" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#1C7ED6;strokeWidth=1.8;fontSize=11;fontColor=#000000;" vertex="1" parent="lane_pemilik">
          <mxGeometry x="1365" y="70" width="150" height="56" as="geometry" />
        </mxCell>

        <!-- End Event 2: Rekapitulasi Kas Terkonsolidasi -->
        <mxCell id="end_kas" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFF5F5;strokeColor=#C92A2A;strokeWidth=4.5;" vertex="1" parent="lane_pemilik">
          <mxGeometry x="1575" y="80" width="36" height="36" as="geometry" />
        </mxCell>
        <mxCell id="lbl_end_kas" value="&lt;b&gt;Penerimaan Kas 8 Cabang&lt;br&gt;Terkonsolidasi Real-Time&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#C92A2A;" vertex="1" parent="lane_pemilik">
          <mxGeometry x="1515" y="122" width="156" height="30" as="geometry" />
        </mxCell>

        <!-- ==================== FLOWS / EDGES ==================== -->
        <!-- Sequence Flows Lane 1 -> Lane 2 -->
        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="start_tb" target="task_1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_1" target="task_2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_2" target="task_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_3" target="gw_split_metode">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Method Branch 1: Tunai -->
        <mxCell id="e_tunai" value="Tunai" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=0.5;exitY=1;fontSize=10;fontColor=#1C7ED6;" edge="1" parent="1" source="gw_split_metode" target="task_4a">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_tunai_join" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0.5;entryY=1;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_4a" target="gw_join_pay">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Method Branch 2: Transfer -->
        <mxCell id="e_trans" value="Transfer" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=0.5;exitY=0;fontSize=10;fontColor=#D9480F;" edge="1" parent="1" source="gw_split_metode" target="task_4b">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0.5;entryY=0;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_4b" target="task_4c">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0.5;entryY=0;exitX=0.5;exitY=1;" edge="1" parent="1" source="task_4c" target="task_5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_5" target="gw_split_valid">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Valid Split: Tidak Valid -->
        <mxCell id="e_tidak_valid" value="[Tidak Valid]" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0.5;entryY=1;exitX=0.5;exitY=1;fontSize=9;fontColor=#C92A2A;" edge="1" parent="1" source="gw_split_valid" target="task_5_rej">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_loop_rej" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=1;entryY=0.5;exitX=0;exitY=0.5;" edge="1" parent="1" source="task_5_rej" target="task_4c">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1040" y="440" />
              <mxPoint x="1040" y="318" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Valid Split: Valid -> Join -->
        <mxCell id="e_valid_join" value="[Valid]" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;fontSize=10;fontColor=#2B8A3E;" edge="1" parent="1" source="gw_split_valid" target="gw_join_pay">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1170" y="535" />
              <mxPoint x="1170" y="318" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Join -> AND Split (+) -->
        <mxCell id="e8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.8;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="gw_join_pay" target="gw_and_split">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- AND Split (+) Stream 1: Siswa Operasional -->
        <mxCell id="e_stream1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.8;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="gw_and_split" target="task_6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e9" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_6" target="task_7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_7" target="end_siswa">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- AND Split (+) Stream 2: Monitoring Kas Pusat -->
        <mxCell id="e_stream2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.8;entryX=0;entryY=0.5;exitX=0.5;exitY=1;" edge="1" parent="1" source="gw_and_split" target="task_8">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1345" y="370" />
              <mxPoint x="1345" y="543" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="e11" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1.5;entryX=0;entryY=0.5;exitX=1;exitY=0.5;" edge="1" parent="1" source="task_8" target="end_kas">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Data Associations (Dotted) -->
        <mxCell id="da1" style="edgeStyle=none;rounded=0;html=1;dashed=1;strokeColor=#868E96;strokeWidth=1.2;entryX=0.5;entryY=0;exitX=0.5;exitY=1;" edge="1" parent="1" source="do_form" target="task_1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="da2" style="edgeStyle=none;rounded=0;html=1;dashed=1;strokeColor=#868E96;strokeWidth=1.2;entryX=0.5;entryY=0;exitX=0.5;exitY=1;" edge="1" parent="1" source="task_2" target="ds_mysql">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="da3" style="edgeStyle=none;rounded=0;html=1;dashed=1;strokeColor=#868E96;strokeWidth=1.2;entryX=0.5;entryY=0;exitX=0.5;exitY=1;" edge="1" parent="1" source="do_bukti" target="task_4b">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="da4" style="edgeStyle=none;rounded=0;html=1;dashed=1;strokeColor=#868E96;strokeWidth=1.2;entryX=0.5;entryY=0;exitX=0.5;exitY=1;" edge="1" parent="1" source="task_6" target="do_pdf">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

# Write drawio files
drawio_path1 = BAB3_ASET / "Gambar_3_2_BPMN_To_Be_ARTHA.drawio"
drawio_path2 = BAB3_OLD_ASET / "Gambar_3_2_BPMN_To_Be_ARTHA.drawio"
drawio_path1.write_text(drawio_xml, encoding="utf-8")
if BAB3_OLD_ASET.exists():
    drawio_path2.write_text(drawio_xml, encoding="utf-8")
print(f"Saved Drawio to {drawio_path1}")

# 2. SVG VECTOR GENERATION
svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1880 780" width="1880" height="780" style="background:#ffffff; font-family:'Segoe UI', Inter, Arial, sans-serif;">
  <defs>
    <filter id="cardShadow" x="-1%" y="-1%" width="102%" height="104%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <marker id="arrowSolid" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#000000"/>
    </marker>
  </defs>

  <!-- Title Card -->
  <rect x="40" y="20" width="1800" height="40" rx="4" fill="#EBFBEE" stroke="#2B8A3E" stroke-width="1.5"/>
  <text x="940" y="45" font-size="15" font-weight="700" fill="#2B8A3E" text-anchor="middle">Gambar 3.2 Proses Bisnis Usulan (To-Be) Operasional Terintegrasi Bimbel ARTHA (Sesuai Dumas et al., 2018)</text>

  <!-- Main Pool Container -->
  <rect x="40" y="75" width="1800" height="660" fill="#FFFFFF" stroke="#000000" stroke-width="2" rx="2" filter="url(#cardShadow)"/>
  <!-- Pool Header -->
  <rect x="40" y="75" width="30" height="660" fill="#212529" stroke="#000000" stroke-width="2"/>
  <text x="55" y="405" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle" transform="rotate(-90 55 405)">Bimbingan Belajar ARTHA Balikpapan (Proses Usulan / To-Be)</text>

  <!-- Lane 1: Wali Murid / Siswa -->
  <rect x="70" y="75" width="1770" height="210" fill="#F8F9FA" stroke="#ADB5BD" stroke-width="1.2"/>
  <rect x="70" y="75" width="26" height="210" fill="#E9ECEF" stroke="#ADB5BD" stroke-width="1.2"/>
  <text x="83" y="180" font-size="11" font-weight="700" fill="#343A40" text-anchor="middle" transform="rotate(-90 83 180)">Wali Murid / Siswa</text>

  <!-- Lane 2: Staf Administrasi Cabang -->
  <rect x="70" y="285" width="1770" height="230" fill="#FFFFFF" stroke="#ADB5BD" stroke-width="1.2"/>
  <rect x="70" y="285" width="26" height="230" fill="#E9ECEF" stroke="#ADB5BD" stroke-width="1.2"/>
  <text x="83" y="400" font-size="11" font-weight="700" fill="#343A40" text-anchor="middle" transform="rotate(-90 83 400)">Staf Administrasi Cabang</text>

  <!-- Lane 3: Pengelola Keuangan Pusat -->
  <rect x="70" y="515" width="1770" height="220" fill="#F8F9FA" stroke="#ADB5BD" stroke-width="1.2"/>
  <rect x="70" y="515" width="26" height="220" fill="#E9ECEF" stroke="#ADB5BD" stroke-width="1.2"/>
  <text x="83" y="625" font-size="11" font-weight="700" fill="#343A40" text-anchor="middle" transform="rotate(-90 83 625)">Pengelola Keuangan Pusat (Pemilik)</text>

  <!-- ==================== LANE 1 ELEMENTS ==================== -->
  <!-- Start Event -->
  <circle cx="140" cy="180" r="18" fill="#EBFBEE" stroke="#2B8A3E" stroke-width="2.5"/>
  <text x="140" y="213" font-size="11" font-weight="700" fill="#2B8A3E" text-anchor="middle">Mulai</text>

  <!-- Task 1: Formulir Pendaftaran -->
  <rect x="210" y="152" width="150" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="285" y="177" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Mengisi Lembar Formulir</text>
  <text x="285" y="192" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Pendaftaran di Cabang</text>

  <!-- Data Object: Formulir Fisik -->
  <path d="M 265 92 L 295 92 L 305 102 L 305 132 L 265 132 Z" fill="#FFF9DB" stroke="#F59F00" stroke-width="1.5"/>
  <path d="M 295 92 L 295 102 L 305 102" fill="none" stroke="#F59F00" stroke-width="1.5"/>
  <text x="285" y="115" font-size="8" font-weight="600" fill="#D9480F" text-anchor="middle">Formulir</text>
  <text x="285" y="125" font-size="8" font-weight="600" fill="#D9480F" text-anchor="middle">Fisik</text>
  <line x1="285" y1="132" x2="285" y2="152" stroke="#ADB5BD" stroke-width="1.2" stroke-dasharray="3 3"/>

  <!-- Task 4b: Transfer via m-Banking -->
  <rect x="790" y="152" width="150" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="865" y="177" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Mentransfer Biaya via</text>
  <text x="865" y="192" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">m-Banking &amp; Kirim Bukti</text>

  <!-- Data Object: Bukti Transfer -->
  <path d="M 845 92 L 875 92 L 885 102 L 885 132 L 845 132 Z" fill="#FFF9DB" stroke="#F59F00" stroke-width="1.5"/>
  <path d="M 875 92 L 875 102 L 885 102" fill="none" stroke="#F59F00" stroke-width="1.5"/>
  <text x="865" y="115" font-size="8" font-weight="600" fill="#D9480F" text-anchor="middle">Bukti</text>
  <text x="865" y="125" font-size="8" font-weight="600" fill="#D9480F" text-anchor="middle">Transfer</text>
  <line x1="865" y1="132" x2="865" y2="152" stroke="#ADB5BD" stroke-width="1.2" stroke-dasharray="3 3"/>

  <!-- End Event 1: Siswa Terdaftar -->
  <circle cx="1775" cy="180" r="18" fill="#FFF5F5" stroke="#C92A2A" stroke-width="4.5"/>
  <text x="1775" y="213" font-size="10" font-weight="700" fill="#C92A2A" text-anchor="middle">Siswa Resmi Terdaftar &amp;</text>
  <text x="1775" y="225" font-size="10" font-weight="700" fill="#C92A2A" text-anchor="middle">Siap Mengikuti KBM</text>

  <!-- ==================== LANE 2 ELEMENTS ==================== -->
  <!-- Task 2: Input Web ARTHA -->
  <rect x="370" y="372" width="150" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="445" y="397" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Memasukkan Data Siswa</text>
  <text x="445" y="412" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">ke Aplikasi Web ARTHA</text>

  <!-- Data Store: Basis Data MySQL Cloud -->
  <g transform="translate(415, 442)">
    <ellipse cx="30" cy="8" rx="28" ry="7" fill="#E7F5FF" stroke="#1971C2" stroke-width="1.5"/>
    <rect x="2" y="8" width="56" height="24" fill="#E7F5FF" stroke="none"/>
    <line x1="2" y1="8" x2="2" y2="32" stroke="#1971C2" stroke-width="1.5"/>
    <line x1="58" y1="8" x2="58" y2="32" stroke="#1971C2" stroke-width="1.5"/>
    <path d="M 2 18 A 28 7 0 0 0 58 18" fill="none" stroke="#1971C2" stroke-width="1"/>
    <path d="M 2 32 A 28 7 0 0 0 58 32" fill="none" stroke="#1971C2" stroke-width="1.5"/>
    <text x="30" y="24" font-size="8" font-weight="600" fill="#1864AB" text-anchor="middle">MySQL Cloud</text>
  </g>
  <line x1="445" y1="428" x2="445" y2="442" stroke="#ADB5BD" stroke-width="1.2" stroke-dasharray="3 3"/>

  <!-- Task 3: Cek Kuota Sesi -->
  <rect x="545" y="372" width="150" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="620" y="397" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Memeriksa Ketersediaan</text>
  <text x="620" y="412" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Kuota Sesi secara Digital</text>

  <!-- XOR Split 1: Metode Pembayaran -->
  <polygon points="730 400, 750 380, 770 400, 750 420" fill="#FFF9DB" stroke="#E67700" stroke-width="2"/>
  <text x="750" y="406" font-size="15" font-weight="800" fill="#D9480F" text-anchor="middle">✕</text>
  <text x="750" y="368" font-size="9" font-weight="700" fill="#D9480F" text-anchor="middle">Metode Bayar?</text>

  <!-- Task 4a: Terima Uang Tunai -->
  <rect x="790" y="435" width="150" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="865" y="460" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Menerima Uang Tunai &amp;</text>
  <text x="865" y="475" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Konfirmasi Lunas di Web</text>

  <!-- Task 4c: Unggah Bukti Bayar -->
  <rect x="975" y="372" width="150" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="1050" y="397" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Mengunggah Bukti Bayar</text>
  <text x="1050" y="412" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">ke Dasbor Cabang</text>

  <!-- Task Rejection Koreksi -->
  <rect x="1155" y="442" width="140" height="50" rx="8" fill="#FFF5F5" stroke="#E03131" stroke-width="1.8"/>
  <text x="1225" y="464" font-size="10" font-weight="600" fill="#C92A2A" text-anchor="middle">Menolak Bukti &amp; Minta</text>
  <text x="1225" y="477" font-size="10" font-weight="600" fill="#C92A2A" text-anchor="middle">Koreksi Bukti Bayar</text>

  <!-- XOR Join: Pembayaran Lunas -->
  <polygon points="1325 400, 1345 380, 1365 400, 1345 420" fill="#FFF9DB" stroke="#E67700" stroke-width="2"/>
  <text x="1345" y="406" font-size="15" font-weight="800" fill="#D9480F" text-anchor="middle">✕</text>

  <!-- PARALLEL GATEWAY (AND-SPLIT +) -->
  <polygon points="1395 400, 1415 380, 1435 400, 1415 420" fill="#FFF9DB" stroke="#E67700" stroke-width="2"/>
  <text x="1415" y="407" font-size="20" font-weight="800" fill="#D9480F" text-anchor="middle">+</text>

  <!-- Task 6: Cetak Kuitansi PDF -->
  <rect x="1465" y="372" width="145" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="1537" y="397" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Mencetak Kuitansi Resmi</text>
  <text x="1537" y="412" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Format PDF Digital</text>

  <!-- Data Object: Kuitansi PDF -->
  <path d="M 1522 444 L 1552 444 L 1562 454 L 1562 484 L 1522 484 Z" fill="#FFF9DB" stroke="#F59F00" stroke-width="1.5"/>
  <path d="M 1552 444 L 1552 454 L 1562 454" fill="none" stroke="#F59F00" stroke-width="1.5"/>
  <text x="1542" y="467" font-size="8" font-weight="600" fill="#D9480F" text-anchor="middle">Kuitansi</text>
  <text x="1542" y="477" font-size="8" font-weight="600" fill="#D9480F" text-anchor="middle">PDF</text>
  <line x1="1537" y1="428" x2="1537" y2="444" stroke="#ADB5BD" stroke-width="1.2" stroke-dasharray="3 3"/>

  <!-- Task 7: Serahkan Kuitansi & Tempatkan Siswa -->
  <rect x="1635" y="372" width="155" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="1712" y="397" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Menyerahkan Kuitansi &amp;</text>
  <text x="1712" y="412" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Tempatkan ke Rombel</text>

  <!-- ==================== LANE 3 ELEMENTS ==================== -->
  <!-- Task 5: Validasi Bukti Transfer -->
  <rect x="975" y="597" width="150" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="1050" y="622" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Memvalidasi Bukti Transfer</text>
  <text x="1050" y="637" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">via Dasbor Manajemen Pusat</text>

  <!-- XOR Split 2: Bukti Valid? -->
  <polygon points="1155 625, 1175 605, 1195 625, 1175 645" fill="#FFF9DB" stroke="#E67700" stroke-width="2"/>
  <text x="1175" y="631" font-size="15" font-weight="800" fill="#D9480F" text-anchor="middle">✕</text>
  <text x="1175" y="593" font-size="9" font-weight="700" fill="#D9480F" text-anchor="middle">Bukti Valid?</text>

  <!-- Task 8: Monitoring Rekapitulasi Kas -->
  <rect x="1465" y="597" width="155" height="56" rx="8" fill="#FFFFFF" stroke="#1C7ED6" stroke-width="2"/>
  <text x="1542" y="622" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">Memantau Rekapitulasi Kas</text>
  <text x="1542" y="637" font-size="11" font-weight="600" fill="#1864AB" text-anchor="middle">8 Cabang secara Real-Time</text>

  <!-- End Event 2: Rekapitulasi Kas -->
  <circle cx="1695" cy="625" r="18" fill="#FFF5F5" stroke="#C92A2A" stroke-width="4.5"/>
  <text x="1695" y="658" font-size="10" font-weight="700" fill="#C92A2A" text-anchor="middle">Penerimaan Kas 8 Cabang</text>
  <text x="1695" y="670" font-size="10" font-weight="700" fill="#C92A2A" text-anchor="middle">Terkonsolidasi Real-Time</text>

  <!-- ==================== FLOW ARROWS ==================== -->
  <!-- Start -> Task 1 -->
  <line x1="158" y1="180" x2="210" y2="180" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <!-- Task 1 -> Task 2 -->
  <path d="M 360 180 L 365 180 L 365 400 L 370 400" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <!-- Task 2 -> Task 3 -->
  <line x1="520" y1="400" x2="545" y2="400" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <!-- Task 3 -> XOR Split 1 -->
  <line x1="695" y1="400" x2="730" y2="400" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- XOR Split 1 -> Tunai (Task 4a) -->
  <path d="M 750 420 L 750 463 L 790 463" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <rect x="705" y="445" width="40" height="16" fill="#E7F5FF" stroke="#A5D8FF" stroke-width="0.8" rx="2"/>
  <text x="725" y="456" font-size="9" font-weight="700" fill="#1864AB" text-anchor="middle">Tunai</text>

  <!-- Tunai (Task 4a) -> XOR Join -->
  <path d="M 940 463 L 1345 463 L 1345 420" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- XOR Split 1 -> Transfer (Task 4b) -->
  <path d="M 750 380 L 750 180 L 790 180" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <rect x="695" y="275" width="50" height="16" fill="#FFF4E6" stroke="#FFD8A8" stroke-width="0.8" rx="2"/>
  <text x="720" y="286" font-size="9" font-weight="700" fill="#D9480F" text-anchor="middle">Transfer</text>

  <!-- Task 4b -> Task 4c -->
  <path d="M 940 180 L 1050 180 L 1050 372" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- Task 4c -> Task 5 (Lane 3) -->
  <line x1="1050" y1="428" x2="1050" y2="597" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- Task 5 -> XOR Split 2 (Bukti Valid?) -->
  <line x1="1125" y1="625" x2="1155" y2="625" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- XOR Split 2 -> Tidak Valid -> Rejection Notice -->
  <path d="M 1175 605 L 1175 467 L 1155 467" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <rect x="1182" y="525" width="65" height="16" fill="#FFF5F5" stroke="#FFA8A8" stroke-width="0.8" rx="2"/>
  <text x="1214" y="536" font-size="8" font-weight="700" fill="#C92A2A" text-anchor="middle">Tidak Valid</text>

  <!-- Rejection Notice -> Loop back to Task 4c -->
  <path d="M 1155 467 L 1135 467 L 1135 400 L 1125 400" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- XOR Split 2 -> [Valid] -> XOR Join -->
  <path d="M 1195 625 L 1310 625 L 1310 400 L 1325 400" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <rect x="1210" y="617" width="40" height="16" fill="#EBFBEE" stroke="#8CE99A" stroke-width="0.8" rx="2"/>
  <text x="1230" y="628" font-size="9" font-weight="700" fill="#2B8A3E" text-anchor="middle">Valid</text>

  <!-- XOR Join -> AND Split (+) -->
  <line x1="1365" y1="400" x2="1395" y2="400" stroke="#000000" stroke-width="2" marker-end="url(#arrowSolid)"/>

  <!-- AND Split (+) Stream 1: Siswa Operasional -->
  <line x1="1435" y1="400" x2="1465" y2="400" stroke="#000000" stroke-width="2" marker-end="url(#arrowSolid)"/>
  <line x1="1610" y1="400" x2="1635" y2="400" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>
  <path d="M 1790 400 L 1800 400 L 1800 180 L 1793 180" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

  <!-- AND Split (+) Stream 2: Monitoring Kas Pusat -->
  <path d="M 1415 420 L 1415 625 L 1465 625" fill="none" stroke="#000000" stroke-width="2" marker-end="url(#arrowSolid)"/>
  <line x1="1620" y1="625" x2="1677" y2="625" stroke="#000000" stroke-width="1.8" marker-end="url(#arrowSolid)"/>

</svg>'''

# Save SVG
svg_path = BAB3_ASET / "Gambar_3_2_BPMN_To_Be_ARTHA.svg"
svg_path.write_text(svg_content, encoding="utf-8")
print(f"Saved SVG to {svg_path}")

# Render 300 DPI PNG via PyMuPDF
doc = fitz.open(stream=svg_content.encode("utf-8"), filetype="svg")
page = doc.load_page(0)
pix = page.get_pixmap(dpi=300)

png_path1 = BAB3_ASET / "Gambar_3_2_BPMN_To_Be_ARTHA.png"
png_path2 = BAB3_OLD_ASET / "Gambar_3_2_BPMN_To_Be_ARTHA.png"
artifact_png = ARTIFACT_DIR / "Gambar_3_2_BPMN_To_Be_ARTHA.png"

pix.save(str(png_path1))
if BAB3_OLD_ASET.exists():
    pix.save(str(png_path2))
pix.save(str(artifact_png))

print(f"Saved PNG to {png_path1}")
print(f"Resolution: {pix.width}x{pix.height}")

