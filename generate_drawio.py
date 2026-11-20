import os

output_dirs = [
    os.path.abspath('DRAFT PROPOSAL MD/BAB 3/ASET BAB 3'),
    os.path.abspath('ASET BAB 3')
]

for d in output_dirs:
    os.makedirs(d, exist_ok=True)

# -------------------------------------------------------------
# 1. DRAW.IO: USE CASE DIAGRAM (Gambar 3.5)
# -------------------------------------------------------------
def get_use_case_drawio():
    xml = '''<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="diagram_uc" name="Use Case Diagram ARTHA">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="950" background="#ffffff">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- System Boundary Box -->
        <mxCell id="sys_box" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;&amp;laquo;subsystem&amp;raquo;&lt;br&gt;Sistem Informasi ARTHA&lt;/b&gt;" style="shape=rect;whiteSpace=wrap;html=1;verticalAlign=top;align=left;spacingLeft=20;spacingTop=15;fillColor=#FAFAFA;strokeColor=#000000;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="240" y="40" width="700" height="850" as="geometry" />
        </mxCell>

        <!-- Actor: Staf Cabang (Left) -->
        <mxCell id="act_staf" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Staf Administrasi&lt;br&gt;Cabang&lt;/b&gt;" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;" vertex="1" parent="1">
          <mxGeometry x="110" y="380" width="45" height="90" as="geometry" />
        </mxCell>

        <!-- Actor: Super Admin (Right) -->
        <mxCell id="act_admin" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Super Admin&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#555555&quot;&gt;(Pemilik Lembaga)&lt;/font&gt;" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;strokeColor=#000000;strokeWidth=2;fillColor=#FFFFFF;" vertex="1" parent="1">
          <mxGeometry x="1035" y="460" width="45" height="90" as="geometry" />
        </mxCell>

        <!-- Use Cases (Ovals) -->
        <!-- UC-01: Autentikasi -->
        <mxCell id="uc_01" value="Melakukan Autentikasi Masuk" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="510" y="85" width="180" height="55" as="geometry" />
        </mxCell>

        <!-- UC-02: Mendaftarkan Siswa Baru -->
        <mxCell id="uc_02" value="Mendaftarkan Siswa Baru" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="290" y="175" width="180" height="55" as="geometry" />
        </mxCell>

        <!-- UC-03: Memvalidasi Kuota Rombel -->
        <mxCell id="uc_03" value="Memvalidasi Kuota Rombel" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="690" y="175" width="180" height="55" as="geometry" />
        </mxCell>

        <!-- UC-04: Mencatat Pembayaran Kasir Cabang -->
        <mxCell id="uc_04" value="Mencatat Pembayaran&lt;br&gt;Kasir Cabang" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="290" y="285" width="180" height="60" as="geometry" />
        </mxCell>

        <!-- UC-05: Mengunggah Bukti Transfer Bank -->
        <mxCell id="uc_05" value="Mengunggah Bukti Transfer Bank" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="690" y="285" width="185" height="55" as="geometry" />
        </mxCell>

        <!-- UC-06: Mencetak Kuitansi Pembayaran (PDF) -->
        <mxCell id="uc_06" value="Mencetak Kuitansi&lt;br&gt;Pembayaran (PDF)" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="500" y="395" width="180" height="55" as="geometry" />
        </mxCell>

        <!-- UC-07: Melakukan Rekonsiliasi Kas Harian -->
        <mxCell id="uc_07" value="Melakukan Rekonsiliasi&lt;br&gt;Kas Harian" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="290" y="510" width="180" height="55" as="geometry" />
        </mxCell>

        <!-- UC-08: Mengelola Pengguna dan Cabang -->
        <mxCell id="uc_08" value="Mengelola Pengguna&lt;br&gt;dan Cabang" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="690" y="470" width="180" height="55" as="geometry" />
        </mxCell>

        <!-- UC-09: Mengelola Master Rombel -->
        <mxCell id="uc_09" value="Mengelola Master Rombel" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="690" y="560" width="180" height="55" as="geometry" />
        </mxCell>

        <!-- UC-10: Memvalidasi Pembayaran Transfer Bank -->
        <mxCell id="uc_10" value="Memvalidasi Pembayaran&lt;br&gt;Transfer Bank" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="690" y="650" width="180" height="55" as="geometry" />
        </mxCell>

        <!-- UC-11: Memantau Tunggakan dan Jatuh Tempo SPP -->
        <mxCell id="uc_11" value="Memantau Tunggakan &amp;amp;&lt;br&gt;Jatuh Tempo SPP" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="690" y="740" width="180" height="55" as="geometry" />
        </mxCell>

        <!-- UC-12: Melihat Dasbor Konsolidasi Keuangan -->
        <mxCell id="uc_12" value="Melihat Dasbor&lt;br&gt;Konsolidasi Keuangan" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="690" y="825" width="180" height="55" as="geometry" />
        </mxCell>

        <!-- Associations (Solid Lines) -->
        <!-- Staf to UC-01 -->
        <mxCell id="edge_s1" style="endArrow=none;html=1;strokeWidth=1.5;strokeColor=#000000;exitX=1;exitY=0.33;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="act_staf" target="uc_01">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Staf to UC-02 -->
        <mxCell id="edge_s2" style="endArrow=none;html=1;strokeWidth=1.5;strokeColor=#000000;exitX=1;exitY=0.33;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="act_staf" target="uc_02">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Staf to UC-04 -->
        <mxCell id="edge_s4" style="endArrow=none;html=1;strokeWidth=1.5;strokeColor=#000000;exitX=1;exitY=0.33;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="act_staf" target="uc_04">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Staf to UC-07 -->
        <mxCell id="edge_s7" style="endArrow=none;html=1;strokeWidth=1.5;strokeColor=#000000;exitX=1;exitY=0.33;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="act_staf" target="uc_07">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Admin to UC-01 -->
        <mxCell id="edge_a1" style="endArrow=none;html=1;strokeWidth=1.5;strokeColor=#000000;exitX=0;exitY=0.33;exitDx=0;exitDy=0;exitPerimeter=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="act_admin" target="uc_01">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Admin to UC-08 -->
        <mxCell id="edge_a8" style="endArrow=none;html=1;strokeWidth=1.5;strokeColor=#000000;exitX=0;exitY=0.33;exitDx=0;exitDy=0;exitPerimeter=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="act_admin" target="uc_08">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Admin to UC-09 -->
        <mxCell id="edge_a9" style="endArrow=none;html=1;strokeWidth=1.5;strokeColor=#000000;exitX=0;exitY=0.33;exitDx=0;exitDy=0;exitPerimeter=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="act_admin" target="uc_09">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Admin to UC-10 -->
        <mxCell id="edge_a10" style="endArrow=none;html=1;strokeWidth=1.5;strokeColor=#000000;exitX=0;exitY=0.33;exitDx=0;exitDy=0;exitPerimeter=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="act_admin" target="uc_10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Admin to UC-11 -->
        <mxCell id="edge_a11" style="endArrow=none;html=1;strokeWidth=1.5;strokeColor=#000000;exitX=0;exitY=0.33;exitDx=0;exitDy=0;exitPerimeter=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="act_admin" target="uc_11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Admin to UC-12 -->
        <mxCell id="edge_a12" style="endArrow=none;html=1;strokeWidth=1.5;strokeColor=#000000;exitX=0;exitY=0.33;exitDx=0;exitDy=0;exitPerimeter=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="act_admin" target="uc_12">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Include & Extend Relationships (Dashed Arrows) -->
        <!-- UC-02 <<include>> UC-03 -->
        <mxCell id="rel_inc1" value="&amp;laquo;include&amp;raquo;" style="endArrow=open;dashed=1;html=1;strokeWidth=1.5;strokeColor=#000000;fontSize=11;fontStyle=2;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="uc_02" target="uc_03">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- UC-05 <<extend>> UC-04 (points from extension to base) -->
        <mxCell id="rel_ext1" value="&amp;laquo;extend&amp;raquo;" style="endArrow=open;dashed=1;html=1;strokeWidth=1.5;strokeColor=#000000;fontSize=11;fontStyle=2;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="uc_05" target="uc_04">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- UC-04 <<include>> UC-06 -->
        <mxCell id="rel_inc2" value="&amp;laquo;include&amp;raquo;" style="endArrow=open;dashed=1;html=1;strokeWidth=1.5;strokeColor=#000000;fontSize=11;fontStyle=2;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=0.8;exitY=1;exitDx=0;exitDy=0;edgeStyle=orthogonalEdgeStyle;rounded=0;" edge="1" parent="1" source="uc_04" target="uc_06">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- UC-10 <<include>> UC-06 -->
        <mxCell id="rel_inc3" value="&amp;laquo;include&amp;raquo;" style="endArrow=open;dashed=1;html=1;strokeWidth=1.5;strokeColor=#000000;fontSize=11;fontStyle=2;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;edgeStyle=orthogonalEdgeStyle;rounded=0;" edge="1" parent="1" source="uc_10" target="uc_06">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml


# -------------------------------------------------------------
# 2. DRAW.IO: ACTIVITY DIAGRAM 1 (Gambar 3.6)
# -------------------------------------------------------------
def get_activity_1_drawio():
    xml = '''<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="diagram_act1" name="Activity Diagram Pendaftaran Kasir">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1050" pageHeight="1120" background="#ffffff">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Box -->
        <mxCell id="title_box" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;Activity Diagram Pendaftaran Siswa dan Transaksi Kasir Cabang&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;" vertex="1" parent="1">
          <mxGeometry x="35" y="25" width="930" height="42" as="geometry" />
        </mxCell>

        <!-- Swimlane 1: Staf Cabang -->
        <mxCell id="lane1" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Staf Administrasi Cabang&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=38;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="35" y="67" width="310" height="990" as="geometry" />
        </mxCell>
        <!-- Initial Node -->
        <mxCell id="init_node" value="" style="ellipse;fillColor=#000000;strokeColor=none;" vertex="1" parent="lane1">
          <mxGeometry x="141" y="65" width="28" height="28" as="geometry" />
        </mxCell>
        <!-- Action 1 -->
        <mxCell id="act_1" value="Membuka Formulir&lt;br&gt;Pendaftaran Siswa Baru" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="123" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Action 3 -->
        <mxCell id="act_3" value="Mengisi Biodata Siswa &amp;amp;&lt;br&gt;Memilih Rombel Belajar" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="228" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Action 5: Alternatif -->
        <mxCell id="act_5" value="Peringatan Kuota Penuh &amp;amp;&lt;br&gt;Pilih Rombel Alternatif" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="331" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Action 7: Bayar Tunai -->
        <mxCell id="act_7" value="Pilih Kasir Tunai &amp;amp;&lt;br&gt;Input Nominal Uang Diterima" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="513" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Action 11: Serahkan Kuitansi -->
        <mxCell id="act_11" value="Menyerahkan Kuitansi&lt;br&gt;Fisik ke Orang Tua Siswa" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="803" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Final State -->
        <mxCell id="final_node" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;strokeWidth=1.8;" vertex="1" parent="lane1">
          <mxGeometry x="140" y="908" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Swimlane 2: Antarmuka Web -->
        <mxCell id="lane2" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Antarmuka Web ARTHA&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=38;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="345" y="67" width="310" height="990" as="geometry" />
        </mxCell>
        <!-- Action 2 -->
        <mxCell id="act_2" value="Menampilkan Formulir &amp;amp;&lt;br&gt;Daftar Rombel Aktif" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="50" y="123" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Decision: Kuota? -->
        <mxCell id="dec_kuota" value="" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="lane2">
          <mxGeometry x="133" y="333" width="44" height="44" as="geometry" />
        </mxCell>
        <!-- Action 6 -->
        <mxCell id="act_6" value="Kunci Kursi Rombel &amp;amp;&lt;br&gt;Hitung Rincian Tagihan" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="45" y="413" width="220" height="48" as="geometry" />
        </mxCell>
        <!-- Action 8 -->
        <mxCell id="act_8" value="Menghitung Nominal&lt;br&gt;Uang Kembalian" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="50" y="513" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Action 10 -->
        <mxCell id="act_10" value="Mencetak Kuitansi Resmi&lt;br&gt;Berformat PDF" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="50" y="803" width="210" height="48" as="geometry" />
        </mxCell>

        <!-- Swimlane 3: Basis Data & Server -->
        <mxCell id="lane3" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Basis Data &amp;amp; Server ARTHA&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=38;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="655" y="67" width="310" height="990" as="geometry" />
        </mxCell>
        <!-- Action 4 -->
        <mxCell id="act_4" value="Memvalidasi Sisa Kuota&lt;br&gt;Rombel Belajar" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane3">
          <mxGeometry x="50" y="228" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Fork Bar -->
        <mxCell id="fork_1" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=none;" vertex="1" parent="lane3">
          <mxGeometry x="45" y="593" width="220" height="6" as="geometry" />
        </mxCell>
        <!-- Action 9a -->
        <mxCell id="act_9a" value="Simpan Data &amp;amp;&lt;br&gt;Mutasi Kas Masuk" style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="lane3">
          <mxGeometry x="45" y="633" width="105" height="58" as="geometry" />
        </mxCell>
        <!-- Action 9b -->
        <mxCell id="act_9b" value="Kunci Tanggal&lt;br&gt;Jatuh Tempo SPP" style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="lane3">
          <mxGeometry x="160" y="633" width="105" height="58" as="geometry" />
        </mxCell>
        <!-- Join Bar -->
        <mxCell id="join_1" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=none;" vertex="1" parent="lane3">
          <mxGeometry x="45" y="728" width="220" height="6" as="geometry" />
        </mxCell>

        <!-- Connecting Edges -->
        <!-- init to act1 -->
        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="init_node" target="act_1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- act1 to act2 -->
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_1" target="act_2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- act2 to act3 -->
        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_2" target="act_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- act3 to act4 -->
        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_3" target="act_4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- act4 to dec_kuota -->
        <mxCell id="e5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_4" target="dec_kuota">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- dec_kuota to act5 [Penuh / Nol] -->
        <mxCell id="e6" value="[Penuh / Nol]" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;fontSize=11;fontStyle=1;" edge="1" parent="1" source="dec_kuota" target="act_5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- act5 back to act3 -->
        <mxCell id="e7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_5" target="act_3">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="190" y="360" />
              <mxPoint x="120" y="360" />
              <mxPoint x="120" y="343" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- dec_kuota to act6 [Tersedia] -->
        <mxCell id="e8" value="[Tersedia]" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;fontSize=11;fontStyle=1;" edge="1" parent="1" source="dec_kuota" target="act_6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- act6 to act7 -->
        <mxCell id="e9" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_6" target="act_7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- act7 to act8 -->
        <mxCell id="e10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_7" target="act_8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- act8 to fork1 -->
        <mxCell id="e11" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_8" target="fork_1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- fork1 to 9a and 9b -->
        <mxCell id="e12a" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="fork_1" target="act_9a">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e12b" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="fork_1" target="act_9b">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- 9a and 9b to join1 -->
        <mxCell id="e13a" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_9a" target="join_1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e13b" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_9b" target="join_1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- join1 to act10 -->
        <mxCell id="e14" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="join_1" target="act_10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- act10 to act11 -->
        <mxCell id="e15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_10" target="act_11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- act11 to final -->
        <mxCell id="e16" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_11" target="final_node">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml


# -------------------------------------------------------------
# 3. DRAW.IO: ACTIVITY DIAGRAM 2 (Gambar 3.7)
# -------------------------------------------------------------
def get_activity_2_drawio():
    xml = '''<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="diagram_act2" name="Activity Diagram Validasi Transfer">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1050" pageHeight="1150" background="#ffffff">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Box -->
        <mxCell id="title_box" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;Activity Diagram Validasi Bukti Transfer Bank Kantor Pusat&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;" vertex="1" parent="1">
          <mxGeometry x="35" y="25" width="930" height="42" as="geometry" />
        </mxCell>

        <!-- Swimlane 1: Staf Cabang -->
        <mxCell id="lane1" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Staf Administrasi Cabang&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=38;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="35" y="67" width="310" height="1030" as="geometry" />
        </mxCell>
        <!-- Initial Node -->
        <mxCell id="init_node" value="" style="ellipse;fillColor=#000000;strokeColor=none;" vertex="1" parent="lane1">
          <mxGeometry x="141" y="65" width="28" height="28" as="geometry" />
        </mxCell>
        <!-- Action 1 -->
        <mxCell id="act_1" value="Mengunggah Foto&lt;br&gt;Bukti Transfer Perbankan" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="123" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Action 6c: Terima Notif Tolak -->
        <mxCell id="act_6c" value="Menerima Notifikasi Penolakan&lt;br&gt;&amp;amp; Hubungi Wali Murid" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="564" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Final State 1 (Tolak) -->
        <mxCell id="final_1" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;strokeWidth=1.8;" vertex="1" parent="lane1">
          <mxGeometry x="140" y="650" width="30" height="30" as="geometry" />
        </mxCell>
        <!-- Action 9: Cetak Kuitansi Lunas -->
        <mxCell id="act_9" value="Mencetak Kuitansi Lunas&lt;br&gt;untuk Orang Tua Siswa" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="873" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Final State 2 (Lunas) -->
        <mxCell id="final_2" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;strokeWidth=1.8;" vertex="1" parent="lane1">
          <mxGeometry x="140" y="960" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Swimlane 2: Super Admin -->
        <mxCell id="lane2" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Super Admin (Pemilik Lembaga)&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=38;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="345" y="67" width="310" height="1030" as="geometry" />
        </mxCell>
        <!-- Action 3 -->
        <mxCell id="act_3" value="Membuka Menu Antrean&lt;br&gt;Validasi Pembayaran Pusat" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="50" y="228" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Action 5 -->
        <mxCell id="act_5" value="Mencocokkan Nominal &amp;amp;&lt;br&gt;Nama Pengirim ke Rekening" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="45" y="333" width="220" height="48" as="geometry" />
        </mxCell>
        <!-- Decision: Valid? -->
        <mxCell id="dec_valid" value="" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="lane2">
          <mxGeometry x="133" y="435" width="44" height="44" as="geometry" />
        </mxCell>
        <!-- Action 6a: Catatan Tolak (BENAR DI LANE SUPER ADMIN) -->
        <mxCell id="act_6a" value="Memasukkan Catatan&lt;br&gt;Alasan Penolakan Transaksi" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="50" y="498" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Action 7a: Konfirmasi Valid -->
        <mxCell id="act_7a" value="Menekan Tombol Konfirmasi&lt;br&gt;Validasi Pembayaran" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="50" y="688" width="210" height="48" as="geometry" />
        </mxCell>

        <!-- Swimlane 3: Sistem Informasi ARTHA -->
        <mxCell id="lane3" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Sistem Informasi ARTHA&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=38;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="655" y="67" width="310" height="1030" as="geometry" />
        </mxCell>
        <!-- Action 2 -->
        <mxCell id="act_2" value="Menyimpan Berkas &amp;amp; Setel&lt;br&gt;Status 'Menunggu Validasi'" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane3">
          <mxGeometry x="50" y="123" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Action 4 -->
        <mxCell id="act_4" value="Menampilkan Antrean &amp;amp;&lt;br&gt;Pratinjau Bukti Transfer" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane3">
          <mxGeometry x="50" y="228" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Action 6b: Set Ditolak & Notif -->
        <mxCell id="act_6b" value="Setel Status 'Ditolak' &amp;amp;&lt;br&gt;Kirim Notifikasi ke Cabang" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane3">
          <mxGeometry x="50" y="498" width="210" height="48" as="geometry" />
        </mxCell>
        <!-- Fork Bar -->
        <mxCell id="fork_2" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=none;" vertex="1" parent="lane3">
          <mxGeometry x="45" y="710" width="220" height="6" as="geometry" />
        </mxCell>
        <!-- Action 7b -->
        <mxCell id="act_7b" value="Ubah Status&lt;br&gt;Menjadi 'Lunas'" style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="lane3">
          <mxGeometry x="45" y="748" width="105" height="55" as="geometry" />
        </mxCell>
        <!-- Action 7c -->
        <mxCell id="act_7c" value="Tambah Kas Bank&lt;br&gt;&amp;amp; Kunci SPP" style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="lane3">
          <mxGeometry x="160" y="748" width="105" height="55" as="geometry" />
        </mxCell>
        <!-- Join Bar -->
        <mxCell id="join_2" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=none;" vertex="1" parent="lane3">
          <mxGeometry x="45" y="838" width="220" height="6" as="geometry" />
        </mxCell>
        <!-- Action 8 -->
        <mxCell id="act_8" value="Menerbitkan Hak Cetak&lt;br&gt;Kuitansi PDF di Cabang" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane3">
          <mxGeometry x="50" y="873" width="210" height="48" as="geometry" />
        </mxCell>

        <!-- Connecting Edges -->
        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="init_node" target="act_1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_1" target="act_2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_2" target="act_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_3" target="act_4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_4" target="act_5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_5" target="dec_valid">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- dec to 6a [Tidak Valid] -->
        <mxCell id="e7" value="[Tidak Valid]" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;fontSize=11;fontStyle=1;" edge="1" parent="1" source="dec_valid" target="act_6a">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_6a" target="act_6b">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e9" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_6b" target="act_6c">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_6c" target="final_1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- dec to 7a [Valid / Cocok] -->
        <mxCell id="e11" value="[Valid / Cocok]" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;fontSize=11;fontStyle=1;" edge="1" parent="1" source="dec_valid" target="act_7a">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="550" y="525" />
              <mxPoint x="550" y="730" />
              <mxPoint x="500" y="730" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="e12" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_7a" target="fork_2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e13a" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="fork_2" target="act_7b">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e13b" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="fork_2" target="act_7c">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e14a" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_7b" target="join_2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e14b" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_7c" target="join_2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="join_2" target="act_8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e16" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_8" target="act_9">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e17" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_9" target="final_2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml


# -------------------------------------------------------------
# 4. DRAW.IO: ACTIVITY DIAGRAM 3 (Gambar 3.8)
# -------------------------------------------------------------
def get_activity_3_drawio():
    xml = '''<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="diagram_act3" name="Activity Diagram Rekonsiliasi Kas">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1050" pageHeight="1120" background="#ffffff">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Box -->
        <mxCell id="title_box" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;Activity Diagram Rekonsiliasi Kas Harian dan Pemantauan Tunggakan SPP&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;" vertex="1" parent="1">
          <mxGeometry x="35" y="25" width="930" height="42" as="geometry" />
        </mxCell>

        <!-- Swimlane 1: Staf Cabang -->
        <mxCell id="lane1" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Staf Administrasi Cabang&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=38;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="35" y="67" width="310" height="990" as="geometry" />
        </mxCell>
        <mxCell id="init_node" value="" style="ellipse;fillColor=#000000;strokeColor=none;" vertex="1" parent="lane1">
          <mxGeometry x="141" y="65" width="28" height="28" as="geometry" />
        </mxCell>
        <mxCell id="act_1" value="Membuka Menu Tutup&lt;br&gt;Kasir Harian Cabang" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="123" width="210" height="48" as="geometry" />
        </mxCell>
        <mxCell id="act_3" value="Menghitung Fisik Uang Kasir &amp;amp;&lt;br&gt;Input Nominal ke Sistem" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="228" width="210" height="48" as="geometry" />
        </mxCell>
        <mxCell id="act_5a" value="Mengisi Formulir Justifikasi&lt;br&gt;Keterangan Selisih Kasir" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="311" width="210" height="48" as="geometry" />
        </mxCell>
        <mxCell id="act_6" value="Menekan Tombol Tutup&lt;br&gt;Buku Kasir Harian Cabang" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="498" width="210" height="48" as="geometry" />
        </mxCell>

        <!-- Swimlane 2: Sistem ARTHA -->
        <mxCell id="lane2" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Sistem Informasi ARTHA&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=38;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="345" y="67" width="310" height="990" as="geometry" />
        </mxCell>
        <mxCell id="act_2" value="Menghitung Akumulasi&lt;br&gt;Penerimaan Kasir Hari Berjalan" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="50" y="123" width="210" height="48" as="geometry" />
        </mxCell>
        <mxCell id="act_4" value="Mengkalkulasi Selisih Saldo&lt;br&gt;Sistem vs Fisik Kasir" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="50" y="228" width="210" height="48" as="geometry" />
        </mxCell>
        <mxCell id="dec_selisih" value="" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="lane2">
          <mxGeometry x="133" y="313" width="44" height="44" as="geometry" />
        </mxCell>
        <mxCell id="act_5b" value="Tandai Status Laporan&lt;br&gt;'Perlu Peninjauan Pusat'" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="45" y="379" width="220" height="48" as="geometry" />
        </mxCell>
        <mxCell id="fork_3" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=none;" vertex="1" parent="lane2">
          <mxGeometry x="45" y="578" width="220" height="6" as="geometry" />
        </mxCell>
        <mxCell id="act_7a" value="Kunci Transaksi &amp;amp;&lt;br&gt;Terbitkan PDF Berita Acara" style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="45" y="618" width="105" height="58" as="geometry" />
        </mxCell>
        <mxCell id="act_7b" value="Sinkronisasi ke&lt;br&gt;Dasbor Multicabang" style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11;fontStyle=1;" vertex="1" parent="lane2">
          <mxGeometry x="160" y="618" width="105" height="58" as="geometry" />
        </mxCell>
        <mxCell id="join_3" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=none;" vertex="1" parent="lane2">
          <mxGeometry x="45" y="713" width="220" height="6" as="geometry" />
        </mxCell>

        <!-- Swimlane 3: Super Admin -->
        <mxCell id="lane3" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;Super Admin (Pemilik Lembaga)&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=38;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="655" y="67" width="310" height="990" as="geometry" />
        </mxCell>
        <mxCell id="act_8" value="Menerima Rekapitulasi Kas&lt;br&gt;Real-Time Seluruh Cabang" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane3">
          <mxGeometry x="50" y="729" width="210" height="48" as="geometry" />
        </mxCell>
        <mxCell id="act_9" value="Memantau Daftar Siswa Lewat&lt;br&gt;Batas Jatuh Tempo SPP" style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11.5;fontStyle=1;" vertex="1" parent="lane3">
          <mxGeometry x="50" y="818" width="210" height="48" as="geometry" />
        </mxCell>
        <mxCell id="final_3" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;strokeWidth=1.8;" vertex="1" parent="lane3">
          <mxGeometry x="140" y="908" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Connecting Edges -->
        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="init_node" target="act_1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_1" target="act_2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_2" target="act_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_3" target="act_4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_4" target="dec_selisih">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- dec to act5a [Ada Selisih] -->
        <mxCell id="e6" value="[Ada Selisih]" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;fontSize=11;fontStyle=1;" edge="1" parent="1" source="dec_selisih" target="act_5a">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_5a" target="act_5b">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_5b" target="act_6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- dec to act6 [Selisih = 0] (routes around act5b!) -->
        <mxCell id="e9" value="[Selisih = 0]" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;fontSize=11;fontStyle=1;" edge="1" parent="1" source="dec_selisih" target="act_6">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="625" y="400" />
              <mxPoint x="625" y="525" />
              <mxPoint x="190" y="525" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- act6 to fork3 -->
        <mxCell id="e10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_6" target="fork_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e11a" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="fork_3" target="act_7a">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e11b" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="fork_3" target="act_7b">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e12a" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_7a" target="join_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e12b" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_7b" target="join_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e13" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="join_3" target="act_8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e14" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_8" target="act_9">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;strokeWidth=1.5;strokeColor=#000000;endArrow=block;endFill=1;" edge="1" parent="1" source="act_9" target="final_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml


# Write individual .drawio files
files_to_generate = [
    ('Gambar_3_5_Use_Case_Diagram_ARTHA.drawio', get_use_case_drawio()),
    ('Gambar_3_6_Activity_Diagram_Pendaftaran_Kasir.drawio', get_activity_1_drawio()),
    ('Gambar_3_7_Activity_Diagram_Validasi_Transfer.drawio', get_activity_2_drawio()),
    ('Gambar_3_8_Activity_Diagram_Rekonsiliasi_Kas.drawio', get_activity_3_drawio())
]

for filename, content in files_to_generate:
    for d in output_dirs:
        target_path = os.path.join(d, filename)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated: {target_path}")

print("ALL DRAW.IO FILES SUCCESSFULLY CREATED!")

# -------------------------------------------------------------
# 5. GENERATE UNIFIED MULTI-PAGE DRAW.IO FILE
# -------------------------------------------------------------
import re

p_base = output_dirs[0]

def extract_diagram_xml(filepath, page_name, diag_id):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'<diagram\s+[^>]*>(.*?)</diagram>', c, re.DOTALL)
    if m:
        inner = m.group(1).strip()
        return f'  <diagram id="{diag_id}" name="{page_name}">\n    {inner}\n  </diagram>'
    return ''

d1 = extract_diagram_xml(os.path.join(p_base, 'Gambar_3_5_Use_Case_Diagram_ARTHA.drawio'), 'Gambar 3.5 Use Case', 'diag_3_5')
d2 = extract_diagram_xml(os.path.join(p_base, 'Gambar_3_6_Activity_Diagram_Pendaftaran_Kasir.drawio'), 'Gambar 3.6 Pendaftaran Kasir', 'diag_3_6')
d3 = extract_diagram_xml(os.path.join(p_base, 'Gambar_3_7_Activity_Diagram_Validasi_Transfer.drawio'), 'Gambar 3.7 Validasi Transfer', 'diag_3_7')
d4 = extract_diagram_xml(os.path.join(p_base, 'Gambar_3_8_Activity_Diagram_Rekonsiliasi_Kas.drawio'), 'Gambar 3.8 Rekonsiliasi Kas', 'diag_3_8')

master_xml = f'''<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
{d1}
{d2}
{d3}
{d4}
</mxfile>'''

all_dirs = output_dirs + [
    os.path.abspath('DRAFT PROPOSAL MD/BAB 3/3.4 Konsep Prototipe MD/ASET BAB 3')
]

for d in all_dirs:
    os.makedirs(d, exist_ok=True)
    master_path = os.path.join(d, 'ARTHA_Semua_Diagram_UML_Bab3.drawio')
    with open(master_path, 'w', encoding='utf-8') as f:
        f.write(master_xml)
    print(f"Master Draw.io created: {master_path}")
    
    # Also sync all individual drawio files
    for fn, ct in files_to_generate:
        with open(os.path.join(d, fn), 'w', encoding='utf-8') as f:
            f.write(ct)

print("SYNC COMPLETE FOR ALL DRAW.IO DIRECTORIES!")
