def create_drawio_to_be():
    content = """<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="diagram_bpmn_tobe" name="BPMN To-Be ARTHA">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1650" pageHeight="800" background="#ffffff">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Box -->
        <mxCell id="title_box" value="&lt;b style=&quot;font-size: 15px;&quot;&gt;Gambar 3.2 Proses Bisnis Usulan (To-Be) Operasional Terintegrasi Bimbel ARTHA (Sesuai Dumas et al., 2018)&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#EBFBEE;strokeColor=#2B8A3E;strokeWidth=1.5;align=center;" vertex="1" parent="1">
          <mxGeometry x="40" y="20" width="1560" height="40" as="geometry" />
        </mxCell>

        <!-- Pool: Bimbel ARTHA Usulan -->
        <mxCell id="pool_tobe" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Bimbingan Belajar ARTHA Balikpapan (Proses Usulan / To-Be)&lt;/b&gt;" style="swimlane;html=1;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;startSize=30;horizontal=0;horizontalStack=0;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="40" y="75" width="1560" height="660" as="geometry" />
        </mxCell>

        <!-- Lane 1: Wali Murid / Siswa -->
        <mxCell id="lane_wali_tb" value="&lt;b&gt;Wali Murid / Siswa&lt;/b&gt;" style="swimlane;html=1;startSize=26;horizontal=0;fillColor=#F1F3F5;strokeColor=#495057;strokeWidth=1.2;" vertex="1" parent="pool_tobe">
          <mxGeometry x="30" y="0" width="1530" height="210" as="geometry" />
        </mxCell>

        <!-- Lane 2: Staf Administrasi Cabang -->
        <mxCell id="lane_staf_tb" value="&lt;b&gt;Staf Administrasi Cabang&lt;br&gt;(Kak Agian)&lt;/b&gt;" style="swimlane;html=1;startSize=26;horizontal=0;fillColor=#FFFFFF;strokeColor=#495057;strokeWidth=1.2;" vertex="1" parent="pool_tobe">
          <mxGeometry x="30" y="210" width="1530" height="230" as="geometry" />
        </mxCell>

        <!-- Lane 3: Pengelola Keuangan Pusat (Pemilik Lembaga) -->
        <mxCell id="lane_pemilik_tb" value="&lt;b&gt;Pengelola Keuangan Pusat&lt;br&gt;(Ibu Emi / Pemilik)&lt;/b&gt;" style="swimlane;html=1;startSize=26;horizontal=0;fillColor=#F8F9FA;strokeColor=#495057;strokeWidth=1.2;" vertex="1" parent="pool_tobe">
          <mxGeometry x="30" y="440" width="1530" height="220" as="geometry" />
        </mxCell>

        <!-- === LANE 1 ELEMENTS === -->
        <!-- Start Event -->
        <mxCell id="start_tb" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#D4EDDA;strokeColor=#28A745;strokeWidth=2;" vertex="1" parent="lane_wali_tb">
          <mxGeometry x="40" y="85" width="36" height="36" as="geometry" />
        </mxCell>
        <mxCell id="lbl_start_tb" value="Mulai" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=11;" vertex="1" parent="lane_wali_tb">
          <mxGeometry x="35" y="125" width="46" height="20" as="geometry" />
        </mxCell>

        <!-- Task 1: Mengisi Formulir -->
        <mxCell id="task_1_tb" value="Mengisi Lembar Formulir&lt;br&gt;Pendaftaran di Meja Cabang" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#212529;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane_wali_tb">
          <mxGeometry x="110" y="75" width="150" height="56" as="geometry" />
        </mxCell>

        <!-- Data Object: Formulir Fisik -->
        <mxCell id="do_formulir_tb" value="Formulir Fisik&lt;br&gt;Pendaftaran" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;fillColor=#FFF9DB;strokeColor=#F59F00;strokeWidth=1.2;size=14;fontSize=10;" vertex="1" parent="lane_wali_tb">
          <mxGeometry x="145" y="12" width="80" height="45" as="geometry" />
        </mxCell>

        <!-- Task 4b: Transfer via m-Banking -->
        <mxCell id="task_4b_tb" value="Mentransfer Biaya &amp;amp;&lt;br&gt;Mengunggah Bukti Bayar" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#212529;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane_wali_tb">
          <mxGeometry x="770" y="75" width="160" height="56" as="geometry" />
        </mxCell>

        <!-- Data Object: Bukti Bayar -->
        <mxCell id="do_bukti_tb" value="Bukti Transfer&lt;br&gt;/ QRIS" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;fillColor=#FFF9DB;strokeColor=#F59F00;strokeWidth=1.2;size=14;fontSize=10;" vertex="1" parent="lane_wali_tb">
          <mxGeometry x="810" y="12" width="80" height="45" as="geometry" />
        </mxCell>

        <!-- End Event -->
        <mxCell id="end_tb" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#F8D7DA;strokeColor=#DC3545;strokeWidth=3.5;" vertex="1" parent="lane_wali_tb">
          <mxGeometry x="1450" y="85" width="36" height="36" as="geometry" />
        </mxCell>
        <mxCell id="lbl_end_tb" value="Siswa Resmi Terdaftar&lt;br&gt;&amp;amp; Mengikuti KBM" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=11;" vertex="1" parent="lane_wali_tb">
          <mxGeometry x="1410" y="125" width="120" height="30" as="geometry" />
        </mxCell>

        <!-- === LANE 2 ELEMENTS === -->
        <!-- Task 2: Input Web ARTHA -->
        <mxCell id="task_2_tb" value="Memasukkan Data Siswa ke&lt;br&gt;Aplikasi Web ARTHA" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#212529;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane_staf_tb">
          <mxGeometry x="290" y="80" width="160" height="56" as="geometry" />
        </mxCell>

        <!-- Data Store: Basis Data MySQL Terpusat -->
        <mxCell id="ds_mysql_tb" value="Basis Data Terpusat&lt;br&gt;MySQL Cloud" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=8;fillColor=#E3FAFC;strokeColor=#1098AD;strokeWidth=1.2;fontSize=10;" vertex="1" parent="lane_staf_tb">
          <mxGeometry x="325" y="148" width="90" height="52" as="geometry" />
        </mxCell>

        <!-- Task 3: Cek Kuota Digital -->
        <mxCell id="task_3_tb" value="Memeriksa Ketersediaan&lt;br&gt;Kuota Sesi secara Digital" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#212529;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane_staf_tb">
          <mxGeometry x="490" y="80" width="160" height="56" as="geometry" />
        </mxCell>

        <!-- XOR-Split Gateway -->
        <mxCell id="gw_split_tb" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF3BF;strokeColor=#FAB005;strokeWidth=1.8;fontSize=16;fontStyle=1;" vertex="1" parent="lane_staf_tb">
          <mxGeometry x="690" y="88" width="40" height="40" as="geometry" />
        </mxCell>

        <!-- Task 4a: Kasir Tunai Web -->
        <mxCell id="task_4a_tb" value="Menerima Uang Tunai &amp;amp;&lt;br&gt;Konfirmasi Lunas di Web" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#212529;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane_staf_tb">
          <mxGeometry x="770" y="80" width="160" height="56" as="geometry" />
        </mxCell>

        <!-- XOR-Join Gateway (Dumas Compliance!) -->
        <mxCell id="gw_join_tb" value="X" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF3BF;strokeColor=#FAB005;strokeWidth=1.8;fontSize=16;fontStyle=1;" vertex="1" parent="lane_staf_tb">
          <mxGeometry x="970" y="88" width="40" height="40" as="geometry" />
        </mxCell>

        <!-- Task 6: Cetak Kuitansi PDF -->
        <mxCell id="task_6_tb" value="Mencetak Kuitansi Resmi&lt;br&gt;Format PDF Digital" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#212529;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane_staf_tb">
          <mxGeometry x="1050" y="80" width="160" height="56" as="geometry" />
        </mxCell>

        <!-- Data Object: Kuitansi PDF -->
        <mxCell id="do_pdf_tb" value="Kuitansi Resmi&lt;br&gt;PDF Digital" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;fillColor=#FFF9DB;strokeColor=#F59F00;strokeWidth=1.2;size=14;fontSize=10;" vertex="1" parent="lane_staf_tb">
          <mxGeometry x="1090" y="148" width="80" height="45" as="geometry" />
        </mxCell>

        <!-- Task 7: Serahkan Kuitansi & Rombel -->
        <mxCell id="task_7_tb" value="Menyerahkan Kuitansi &amp;amp;&lt;br&gt;Menempatkan Siswa ke Rombel" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#212529;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane_staf_tb">
          <mxGeometry x="1250" y="80" width="160" height="56" as="geometry" />
        </mxCell>

        <!-- === LANE 3 ELEMENTS === -->
        <!-- Task 5b: Verifikasi Dasbor Pusat -->
        <mxCell id="task_5b_tb" value="Memvalidasi Bukti Bayar via&lt;br&gt;Dasbor Manajemen Pusat" style="rounded=1;whiteSpace=wrap;html=1;arcSize=18;fillColor=#FFFFFF;strokeColor=#212529;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane_pemilik_tb">
          <mxGeometry x="770" y="70" width="170" height="56" as="geometry" />
        </mxCell>

        <!-- === SEQUENCE FLOW EDGES (Orthogonal) === -->
        <!-- Start -> Task 1 -->
        <mxCell id="e1_tb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;" edge="1" parent="pool_tobe" source="start_tb" target="task_1_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Task 1 -> Task 2 -->
        <mxCell id="e2_tb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;" edge="1" parent="pool_tobe" source="task_1_tb" target="task_2_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Task 2 -> Task 3 -->
        <mxCell id="e3_tb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;" edge="1" parent="pool_tobe" source="task_2_tb" target="task_3_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Task 3 -> Gateway Split -->
        <mxCell id="e4_tb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;" edge="1" parent="pool_tobe" source="task_3_tb" target="gw_split_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Gateway Split -> Task 4a (Tunai) -->
        <mxCell id="e_tunai_tb" value="Tunai" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="pool_tobe" source="gw_split_tb" target="task_4a_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Gateway Split -> Task 4b (Transfer) -->
        <mxCell id="e_trans_tb" value="Transfer" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="pool_tobe" source="gw_split_tb" target="task_4b_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Task 4b -> Task 5b (Verifikasi Pusat) -->
        <mxCell id="e5_tb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;" edge="1" parent="pool_tobe" source="task_4b_tb" target="task_5b_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Task 4a -> Gateway Join -->
        <mxCell id="e6_tb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;" edge="1" parent="pool_tobe" source="task_4a_tb" target="gw_join_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Task 5b -> Gateway Join -->
        <mxCell id="e7_tb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;" edge="1" parent="pool_tobe" source="task_5b_tb" target="gw_join_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Gateway Join -> Task 6 -->
        <mxCell id="e8_tb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;" edge="1" parent="pool_tobe" source="gw_join_tb" target="task_6_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Task 6 -> Task 7 -->
        <mxCell id="e9_tb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;" edge="1" parent="pool_tobe" source="task_6_tb" target="task_7_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Task 7 -> End Event -->
        <mxCell id="e10_tb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#212529;strokeWidth=1.5;" edge="1" parent="pool_tobe" source="task_7_tb" target="end_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Data Associations (Dashed) -->
        <mxCell id="da1_tb" style="edgeStyle=none;html=1;strokeColor=#868E96;strokeWidth=1.2;dashed=1;endArrow=none;" edge="1" parent="pool_tobe" source="do_formulir_tb" target="task_1_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="da2_tb" style="edgeStyle=none;html=1;strokeColor=#868E96;strokeWidth=1.2;dashed=1;endArrow=none;" edge="1" parent="pool_tobe" source="task_2_tb" target="ds_mysql_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="da3_tb" style="edgeStyle=none;html=1;strokeColor=#868E96;strokeWidth=1.2;dashed=1;endArrow=none;" edge="1" parent="pool_tobe" source="do_bukti_tb" target="task_4b_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="da4_tb" style="edgeStyle=none;html=1;strokeColor=#868E96;strokeWidth=1.2;dashed=1;endArrow=none;" edge="1" parent="pool_tobe" source="task_6_tb" target="do_pdf_tb">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    return content

out_path = 'DRAFT PROPOSAL MD/BAB 3/ASET BAB 3/Gambar_3_2_BPMN_To_Be_ARTHA.drawio'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(create_drawio_to_be())
print(f"Created {out_path} successfully!")

