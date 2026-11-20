import os
import re
from playwright.sync_api import sync_playwright

output_dirs = [
    os.path.abspath('DRAFT PROPOSAL MD/BAB 3/ASET BAB 3'),
    os.path.abspath('ASET BAB 3'),
    os.path.abspath('DRAFT PROPOSAL MD/BAB 3/3.4 Konsep Prototipe MD/ASET BAB 3')
]

for d in output_dirs:
    os.makedirs(d, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. PERFECT DRAW.IO XML GENERATOR (ZERO COLLISION, CHEN NOTATION)
# -----------------------------------------------------------------------------
def get_chen_v2_drawio():
    xml = '''<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="diagram_chen_v2" name="Gambar 3.9 ERD Notasi Chen ARTHA">
    <mxGraphModel dx="2400" dy="1800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2300" pageHeight="1700" background="#ffffff">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Block -->
        <mxCell id="title" value="&lt;b style=&quot;font-size: 17px;&quot;&gt;Entity Relationship Diagram (ERD) - Notasi Peter Chen&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#555555&quot;&gt;Pemodelan Konseptual Basis Data Relasional Sistem Informasi ARTHA&lt;/font&gt;" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="50" y="25" width="600" height="40" as="geometry" />
        </mxCell>

        <!-- Legend Block -->
        <mxCell id="legend" value="&lt;b&gt;Standar Notasi Peter Chen (1976):&lt;/b&gt;&amp;nbsp;&amp;nbsp; [ Persegi Panjang ] = Entitas &amp;nbsp;|&amp;nbsp; ( Elips ) = Atribut &amp;nbsp;|&amp;nbsp; ( &lt;u&gt;Garis Bawah&lt;/u&gt; ) = Primary Key &amp;nbsp;|&amp;nbsp; &amp;lt; Belah Ketupat &amp;gt; = Relasi &amp;nbsp;|&amp;nbsp; 1 / N = Rasio Kardinalitas" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FAFAFA;strokeColor=#000000;strokeWidth=1.2;align=center;fontSize=11.5;" vertex="1" parent="1">
          <mxGeometry x="1320" y="25" width="920" height="38" as="geometry" />
        </mxCell>

        <!-- ============================================================= -->
        <!-- 1. ENTITY: branches (x=460, y=280, w=140, h=45)               -->
        <!-- ============================================================= -->
        <mxCell id="ent_branches" value="&lt;b&gt;branches&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="460" y="280" width="140" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes branches (Top & Left) -->
        <mxCell id="att_br_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="340" y="170" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_id" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_br_id" target="ent_branches"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_br_code" value="branch_code" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="450" y="170" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_code" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.35;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_br_code" target="ent_branches"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_br_name" value="branch_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="575" y="170" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_name" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.3;exitY=1;exitDx=0;exitDy=0;entryX=0.8;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_br_name" target="ent_branches"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_br_addr" value="address" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="300" y="240" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_addr" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.25;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_br_addr" target="ent_branches"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_br_phone" value="phone" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="300" y="300" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_phone" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.75;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_br_phone" target="ent_branches"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ============================================================= -->
        <!-- 2. ENTITY: users (x=200, y=650, w=140, h=45)                  -->
        <!-- ============================================================= -->
        <mxCell id="ent_users" value="&lt;b&gt;users&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="200" y="650" width="140" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes users (Far Left) -->
        <mxCell id="att_u_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="50" y="550" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_u_id" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_u_id" target="ent_users"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_u_email" value="email" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="610" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_u_email" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.3;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_u_email" target="ent_users"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_u_name" value="name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="670" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_u_name" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.7;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_u_name" target="ent_users"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_u_pwd" value="password" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="730" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_u_pwd" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_u_pwd" target="ent_users"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_u_role" value="role" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="60" y="790" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_u_role" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0;exitDx=0;exitDy=0;entryX=0.2;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_u_role" target="ent_users"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ============================================================= -->
        <!-- 3. ENTITY: daily_reconciliations (x=200, y=1180, w=180, h=45) -->
        <!-- ============================================================= -->
        <mxCell id="ent_daily_rec" value="&lt;b&gt;daily_reconciliations&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="200" y="1180" width="180" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes daily_rec (Fanned around Bottom & Left) -->
        <mxCell id="att_dr_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="1060" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_id" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_dr_id" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_date" value="reconciliation_date" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="30" y="1120" width="125" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_date" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.25;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_dr_date" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_sysc" value="system_cash_total" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="20" y="1180" width="130" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_sysc" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_dr_sysc" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_syst" value="system_transfer_tot" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="20" y="1240" width="130" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_syst" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.75;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_dr_syst" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_phy" value="physical_cash_amt" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="1300" width="125" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_phy" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0;exitDx=0;exitDy=0;entryX=0;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_dr_phy" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_disc" value="discrepancy_amount" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="90" y="1360" width="135" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_disc" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.7;exitY=0;exitDx=0;exitDy=0;entryX=0.2;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_dr_disc" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_note" value="discrepancy_note" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="245" y="1360" width="125" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_note" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_dr_note" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_rev" value="review_status" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="390" y="1360" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_rev" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.3;exitY=0;exitDx=0;exitDy=0;entryX=0.8;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_dr_rev" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_lock" value="is_locked" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="420" y="1300" width="90" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_lock" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0;exitDx=0;exitDy=0;entryX=1;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_dr_lock" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_ltime" value="locked_at" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="420" y="1240" width="90" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_ltime" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.75;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_dr_ltime" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_pdf" value="report_pdf_path" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="420" y="1180" width="115" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_pdf" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.25;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_dr_pdf" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ============================================================= -->
        <!-- 4. ENTITY: study_groups (x=1050, y=280, w=150, h=45)          -->
        <!-- ============================================================= -->
        <mxCell id="ent_study_groups" value="&lt;b&gt;study_groups&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="1050" y="280" width="150" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes study_groups (Top & Right) -->
        <mxCell id="att_sg_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="950" y="170" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_id" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_sg_id" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_sg_name" value="group_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1050" y="170" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_name" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.35;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_sg_name" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_sg_day" value="schedule_day" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1170" y="170" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_day" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.3;exitY=1;exitDx=0;exitDy=0;entryX=0.8;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_sg_day" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_sg_time" value="schedule_time" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1230" y="230" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_time" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.25;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_sg_time" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_sg_max" value="max_capacity" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1230" y="290" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_max" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_sg_max" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_sg_curr" value="current_count" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1230" y="350" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_curr" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.75;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_sg_curr" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ============================================================= -->
        <!-- 5. ENTITY: course_packages (x=1750, y=280, w=160, h=45)       -->
        <!-- ============================================================= -->
        <mxCell id="ent_course_packages" value="&lt;b&gt;course_packages&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="1750" y="280" width="160" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes course_packages (Top & Right) -->
        <mxCell id="att_cp_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1650" y="170" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_id" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_cp_id" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_cp_name" value="package_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1750" y="170" width="105" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_name" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.35;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_cp_name" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_cp_grade" value="grade_level" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1875" y="170" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_grade" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.3;exitY=1;exitDx=0;exitDy=0;entryX=0.8;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_cp_grade" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_cp_fee" value="monthly_fee" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1940" y="230" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_fee" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.25;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_cp_fee" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_cp_desc" value="description" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1940" y="290" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_desc" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_cp_desc" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_cp_act" value="is_active" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1940" y="350" width="90" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_act" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.75;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_cp_act" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ============================================================= -->
        <!-- 6. ENTITY: students (x=600, y=650, w=140, h=45)               -->
        <!-- ============================================================= -->
        <mxCell id="ent_students" value="&lt;b&gt;students&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="600" y="650" width="140" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes students (Cleanly arranged on Top & Bottom) -->
        <mxCell id="att_st_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="480" y="550" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_id" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_st_id" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_reg" value="registration_no" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="580" y="550" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_reg" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.3;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_st_reg" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_fn" value="full_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="700" y="550" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_fn" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.3;exitY=1;exitDx=0;exitDy=0;entryX=0.8;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_st_fn" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_bp" value="birth_place" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="450" y="610" width="90" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_bp" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.3;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_st_bp" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_bd" value="birth_date" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="450" y="670" width="90" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_bd" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.7;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_st_bd" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_gen" value="gender" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="470" y="730" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_gen" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0;exitDx=0;exitDy=0;entryX=0.1;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_st_gen" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_sch" value="school_origin" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="570" y="740" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_sch" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.4;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_st_sch" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_grd" value="grade_level" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="690" y="740" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_grd" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.3;exitY=0;exitDx=0;exitDy=0;entryX=0.7;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_st_grd" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_addr" value="home_address" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="470" y="800" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_addr" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0;exitDx=0;exitDy=0;entryX=0.2;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_st_addr" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_pn" value="parent_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="590" y="810" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_pn" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_st_pn" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_pp" value="parent_phone" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="710" y="810" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_pp" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.3;exitY=0;exitDx=0;exitDy=0;entryX=0.8;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_st_pp" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ============================================================= -->
        <!-- 7. ENTITY: enrollments (x=1150, y=650, w=140, h=45)          -->
        <!-- ============================================================= -->
        <mxCell id="ent_enrollments" value="&lt;b&gt;enrollments&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="1150" y="650" width="140" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes enrollments (Right side) -->
        <mxCell id="att_en_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1330" y="590" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_en_id" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=1;exitDx=0;exitDy=0;entryX=1;entryY=0.2;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_en_id" target="ent_enrollments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_en_date" value="registration_date" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1330" y="650" width="115" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_en_date" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_en_date" target="ent_enrollments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_en_day" value="due_day" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1330" y="710" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_en_day" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.8;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_en_day" target="ent_enrollments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_en_stat" value="status" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1330" y="770" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_en_stat" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0;exitDx=0;exitDy=0;entryX=1;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_en_stat" target="ent_enrollments"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ============================================================= -->
        <!-- 8. ENTITY: tuition_bills (x=1150, y=1000, w=140, h=45)       -->
        <!-- ============================================================= -->
        <mxCell id="ent_tuition_bills" value="&lt;b&gt;tuition_bills&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="1150" y="1000" width="140" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes tuition_bills (Left & Bottom) -->
        <mxCell id="att_tb_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1010" y="930" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_tb_id" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_tb_id" target="ent_tuition_bills"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_tb_per" value="bill_period" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1000" y="990" width="90" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_tb_per" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.4;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_tb_per" target="ent_tuition_bills"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_tb_amt" value="amount" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1000" y="1050" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_tb_amt" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.8;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_tb_amt" target="ent_tuition_bills"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_tb_due" value="due_date" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1060" y="1120" width="90" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_tb_due" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.7;exitY=0;exitDx=0;exitDy=0;entryX=0.3;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_tb_due" target="ent_tuition_bills"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_tb_stat" value="payment_status" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1170" y="1120" width="105" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_tb_stat" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.3;exitY=0;exitDx=0;exitDy=0;entryX=0.7;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_tb_stat" target="ent_tuition_bills"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ============================================================= -->
        <!-- 9. ENTITY: payments (x=1750, y=1000, w=140, h=45)            -->
        <!-- ============================================================= -->
        <mxCell id="ent_payments" value="&lt;b&gt;payments&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="1750" y="1000" width="140" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes payments (Right side) -->
        <mxCell id="att_pay_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1930" y="920" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_pay_id" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=1;exitDx=0;exitDy=0;entryX=1;entryY=0.2;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_pay_id" target="ent_payments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pay_rec" value="receipt_number" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1930" y="975" width="110" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_pay_rec" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.4;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_pay_rec" target="ent_payments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pay_meth" value="payment_method" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1930" y="1030" width="115" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_pay_meth" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.6;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_pay_meth" target="ent_payments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pay_amt" value="amount_paid" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1930" y="1085" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_pay_amt" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.8;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_pay_amt" target="ent_payments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pay_date" value="payment_date" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1930" y="1140" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_pay_date" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0;exitDx=0;exitDy=0;entryX=1;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_pay_date" target="ent_payments"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ============================================================= -->
        <!-- 10. ENTITY: payment_proofs (x=1750, y=1340, w=150, h=45)      -->
        <!-- ============================================================= -->
        <mxCell id="ent_payment_proofs" value="&lt;b&gt;payment_proofs&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="1750" y="1340" width="150" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes payment_proofs (Bottom & Right) -->
        <mxCell id="att_pp_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1670" y="1450" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_pp_id" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.8;exitY=0;exitDx=0;exitDy=0;entryX=0.2;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_pp_id" target="ent_payment_proofs"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pp_path" value="file_path" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1770" y="1450" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_pp_path" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_pp_path" target="ent_payment_proofs"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pp_time" value="validated_at" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1875" y="1450" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_pp_time" style="endArrow=none;html=1;strokeColor=#000000;exitX=0.3;exitY=0;exitDx=0;exitDy=0;entryX=0.8;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_pp_time" target="ent_payment_proofs"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pp_stat" value="validation_status" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1940" y="1390" width="110" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_pp_stat" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.75;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_pp_stat" target="ent_payment_proofs"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pp_note" value="rejection_note" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1940" y="1330" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="edge_pp_note" style="endArrow=none;html=1;strokeColor=#000000;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.25;entryDx=0;entryDy=0;" edge="1" parent="1" source="att_pp_note" target="ent_payment_proofs"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ============================================================= -->
        <!-- 14 RELATIONSHIPS (DIAMONDS) & ZERO-COLLISION CONNECTOR PATHS   -->
        <!-- ============================================================= -->

        <!-- 1. branches -[1]- <Memiliki> -[N]- users -->
        <mxCell id="rel_memiliki" value="Memiliki" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="340" y="470" width="105" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_mem" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.2;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_branches" target="rel_memiliki">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_br_mem_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_br_mem">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="-12" y="-5" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mem_usr" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.7;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_memiliki" target="ent_users">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mem_usr_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mem_usr">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" y="5" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 2. branches -[1]- <Mengelola> -[N]- study_groups -->
        <mxCell id="rel_mengelola" value="Mengelola" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="810" y="278" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_mgl" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_branches" target="rel_mengelola">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_br_mgl_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_br_mgl">
          <mxGeometry x="-0.4" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mgl_sg" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_mengelola" target="ent_study_groups">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mgl_sg_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mgl_sg">
          <mxGeometry x="0.4" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 3. branches -[1]- <Menaungi> -[N]- students -->
        <mxCell id="rel_menaungi" value="Menaungi" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="580" y="470" width="105" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_mng" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.8;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_branches" target="rel_menaungi">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_br_mng_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_br_mng">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mng_st" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.4;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_menaungi" target="ent_students">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mng_st_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mng_st">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 4. students -[1]- <Mengambil> -[N]- enrollments -->
        <mxCell id="rel_mengambil" value="Mengambil" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="930" y="648" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_mgb" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_students" target="rel_mengambil">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_st_mgb_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_st_mgb">
          <mxGeometry x="-0.4" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mgb_en" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_mengambil" target="ent_enrollments">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mgb_en_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mgb_en">
          <mxGeometry x="0.4" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 5. study_groups -[1]- <Ditempati> -[N]- enrollments -->
        <mxCell id="rel_ditempati" value="Ditempati" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1090" y="470" width="105" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_dtp" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_study_groups" target="rel_ditempati">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_sg_dtp_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_sg_dtp">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_dtp_en" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.25;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_ditempati" target="ent_enrollments">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_dtp_en_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_dtp_en">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 6. course_packages -[1]- <Ditawarkan> -[N]- enrollments -->
        <mxCell id="rel_ditawarkan" value="Ditawarkan" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1450" y="470" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_dtw" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.2;exitY=1;exitDx=0;exitDy=0;entryX=0.8;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_course_packages" target="rel_ditawarkan">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_cp_dtw_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_cp_dtw">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_dtw_en" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.2;exitY=1;exitDx=0;exitDy=0;entryX=0.75;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_ditawarkan" target="ent_enrollments">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_dtw_en_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_dtw_en">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 7. enrollments -[1]- <Menerbitkan> -[N]- tuition_bills -->
        <mxCell id="rel_menerbitkan" value="Menerbitkan" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1160" y="830" width="120" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_en_mnb" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_enrollments" target="rel_menerbitkan">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_en_mnb_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_en_mnb">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mnb_tb" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_menerbitkan" target="ent_tuition_bills">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mnb_tb_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mnb_tb">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 8. tuition_bills -[1]- <Diselesaikan> -[N]- payments -->
        <mxCell id="rel_diselesaikan" value="Diselesaikan" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1480" y="998" width="120" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_tb_dsl" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_tuition_bills" target="rel_diselesaikan">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_tb_dsl_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_tb_dsl">
          <mxGeometry x="-0.4" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_dsl_pay" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_diselesaikan" target="ent_payments">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_dsl_pay_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_dsl_pay">
          <mxGeometry x="0.4" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 9. payments -[1]- <Melampirkan> -[1]- payment_proofs -->
        <mxCell id="rel_melampirkan" value="Melampirkan" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1760" y="1170" width="120" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_pay_mlp" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_payments" target="rel_melampirkan">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_pay_mlp_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_pay_mlp">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mlp_pp" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_melampirkan" target="ent_payment_proofs">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mlp_pp_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mlp_pp">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 10. branches -[1]- <Mengadakan> -[N]- daily_reconciliations -->
        <!-- Clean orthogonal corridor along x=330, y=980 -->
        <mxCell id="rel_mengadakan" value="Mengadakan" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="290" y="980" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_mgd" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0;exitY=0.75;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_branches" target="rel_mengadakan">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="345" y="314" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lbl_br_mgd_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_br_mgd">
          <mxGeometry x="-0.8" relative="1" as="geometry"><mxPoint x="10" y="-10" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mgd_dr" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.8;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_mengadakan" target="ent_daily_rec">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mgd_dr_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mgd_dr">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 11. users -[1]- <Melakukan> -[N]- daily_reconciliations -->
        <mxCell id="rel_melakukan" value="Melakukan" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="890" width="100" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_usr_mlk" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.4;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_users" target="rel_melakukan">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_usr_mlk_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_usr_mlk">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="-12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mlk_dr" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.3;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_melakukan" target="ent_daily_rec">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mlk_dr_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mlk_dr">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="-12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 12. users -[1]- <Melayani> -[N]- payments -->
        <!-- Clean horizontal path below students (y=890) -->
        <mxCell id="rel_melayani" value="Melayani" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1510" y="865" width="100" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_usr_mly" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.75;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_users" target="rel_melayani">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="360" y="684" />
              <mxPoint x="360" y="890" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lbl_usr_mly_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_usr_mly">
          <mxGeometry x="-0.85" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mly_pay" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.25;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_melayani" target="ent_payments">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1680" y="890" />
              <mxPoint x="1680" y="1011" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lbl_mly_pay_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mly_pay">
          <mxGeometry x="0.5" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 13. users -[1]- <Memvalidasi> -[N]- payment_proofs -->
        <!-- Clean runway across y=1362 -->
        <mxCell id="rel_memvalidasi" value="Memvalidasi" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1480" y="1337" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_usr_mvl" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.8;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_users" target="rel_memvalidasi">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="312" y="730" />
              <mxPoint x="550" y="730" />
              <mxPoint x="550" y="1362" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lbl_usr_mvl_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_usr_mvl">
          <mxGeometry x="-0.85" relative="1" as="geometry"><mxPoint x="10" y="10" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mvl_pp" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_memvalidasi" target="ent_payment_proofs">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mvl_pp_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mvl_pp">
          <mxGeometry x="0.4" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 14. branches -[1]- <Menerima> -[N]- payments -->
        <!-- Clean perimeter path along top y=80 and far right x=2120 -->
        <mxCell id="rel_menerima" value="Menerima" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="2070" y="650" width="100" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_mnr" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_branches" target="rel_menerima">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="530" y="80" />
              <mxPoint x="2120" y="80" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lbl_br_mnr_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_br_mnr">
          <mxGeometry x="-0.85" relative="1" as="geometry"><mxPoint x="15" y="-5" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mnr_pay" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.75;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_menerima" target="ent_payments">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="2120" y="1220" />
              <mxPoint x="1855" y="1220" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lbl_mnr_pay_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mnr_pay">
          <mxGeometry x="0.6" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml

# -----------------------------------------------------------------------------
# 2. GENERATE MATCHING SVG V2
# -----------------------------------------------------------------------------
def get_chen_v2_svg():
    width = 2240
    height = 1580

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      .title {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 18px; font-weight: bold; fill: #000000; }}
      .sub-title {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #444444; }}
      .legend-box {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; fill: #000000; text-anchor: middle; }}
      .ent-label {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 13.5px; font-weight: bold; fill: #000000; text-anchor: middle; }}
      .att-label {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #000000; text-anchor: middle; }}
      .att-pk {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 11.5px; font-weight: bold; text-decoration: underline; fill: #000000; text-anchor: middle; }}
      .rel-label {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; font-weight: bold; fill: #000000; text-anchor: middle; }}
      .card-label {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; font-weight: bold; fill: #000000; }}
      .line-solid {{ stroke: #000000; stroke-width: 1.5; fill: none; }}
      .line-att {{ stroke: #000000; stroke-width: 1.1; fill: none; }}
      .box-ent {{ fill: #ffffff; stroke: #000000; stroke-width: 1.8; }}
      .box-att {{ fill: #ffffff; stroke: #000000; stroke-width: 1.2; }}
      .box-rel {{ fill: #ffffff; stroke: #000000; stroke-width: 1.6; }}
    </style>
  </defs>

  <rect width="{width}" height="{height}" fill="#ffffff" />

  <!-- Title -->
  <text x="50" y="42" class="title">Entity Relationship Diagram (ERD) - Notasi Peter Chen</text>
  <text x="50" y="62" class="sub-title">Pemodelan Konseptual Basis Data Relasional Sistem Informasi ARTHA</text>

  <!-- Legend -->
  <g transform="translate(1250, 26)">
    <rect width="940" height="42" rx="4" ry="4" fill="#FAFAFA" stroke="#000000" stroke-width="1.2" />
    <text x="470" y="26" class="legend-box"><b>Standar Notasi Peter Chen (1976):</b> &nbsp; [ Persegi Panjang ] = Entitas &nbsp;|&nbsp; ( Elips ) = Atribut &nbsp;|&nbsp; <u>Garis Bawah</u> = Kunci Utama (PK) &nbsp;|&nbsp; &lt; Belah Ketupat &gt; = Relasi &nbsp;|&nbsp; 1 / N = Rasio Kardinalitas</text>
  </g>

  <!-- ================= 1. ENTITY: branches ================= -->
  <rect x="460" y="280" width="140" height="45" class="box-ent" />
  <text x="530" y="308" class="ent-label">branches</text>

  <line x1="420" y1="204" x2="475" y2="280" class="line-att" />
  <rect x="340" y="170" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="380" y="192" class="att-pk">id</text>

  <line x1="497" y1="204" x2="510" y2="280" class="line-att" />
  <rect x="450" y="170" width="95" height="34" rx="17" ry="17" class="box-att" />
  <text x="497" y="192" class="att-label">branch_code</text>

  <line x1="610" y1="204" x2="570" y2="280" class="line-att" />
  <rect x="575" y="170" width="95" height="34" rx="17" ry="17" class="box-att" />
  <text x="622" y="192" class="att-label">branch_name</text>

  <line x1="385" y1="257" x2="460" y2="290" class="line-att" />
  <rect x="300" y="240" width="85" height="34" rx="17" ry="17" class="box-att" />
  <text x="342" y="262" class="att-label">address</text>

  <line x1="385" y1="317" x2="460" y2="315" class="line-att" />
  <rect x="300" y="300" width="85" height="34" rx="17" ry="17" class="box-att" />
  <text x="342" y="322" class="att-label">phone</text>


  <!-- ================= 2. ENTITY: users ================= -->
  <rect x="200" y="650" width="140" height="45" class="box-ent" />
  <text x="270" y="678" class="ent-label">users</text>

  <line x1="130" y1="584" x2="200" y2="650" class="line-att" />
  <rect x="50" y="550" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="90" y="572" class="att-pk">id</text>

  <line x1="125" y1="627" x2="200" y2="660" class="line-att" />
  <rect x="40" y="610" width="85" height="34" rx="17" ry="17" class="box-att" />
  <text x="82" y="632" class="att-label">email</text>

  <line x1="125" y1="687" x2="200" y2="675" class="line-att" />
  <rect x="40" y="670" width="85" height="34" rx="17" ry="17" class="box-att" />
  <text x="82" y="692" class="att-label">name</text>

  <line x1="125" y1="747" x2="200" y2="690" class="line-att" />
  <rect x="40" y="730" width="85" height="34" rx="17" ry="17" class="box-att" />
  <text x="82" y="752" class="att-label">password</text>

  <line x1="140" y1="790" x2="225" y2="695" class="line-att" />
  <rect x="60" y="790" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="100" y="812" class="att-label">role</text>


  <!-- ================= 3. ENTITY: daily_reconciliations ================= -->
  <rect x="200" y="1180" width="180" height="45" class="box-ent" />
  <text x="290" y="1208" class="ent-label">daily_reconciliations</text>

  <line x1="120" y1="1094" x2="200" y2="1180" class="line-att" />
  <rect x="40" y="1060" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="80" y="1082" class="att-pk">id</text>

  <line x1="155" y1="1137" x2="200" y2="1190" class="line-att" />
  <rect x="30" y="1120" width="125" height="34" rx="17" ry="17" class="box-att" />
  <text x="92" y="1142" class="att-label">reconciliation_date</text>

  <line x1="150" y1="1197" x2="200" y2="1202" class="line-att" />
  <rect x="20" y="1180" width="130" height="34" rx="17" ry="17" class="box-att" />
  <text x="85" y="1202" class="att-label">system_cash_total</text>

  <line x1="150" y1="1257" x2="200" y2="1215" class="line-att" />
  <rect x="20" y="1240" width="130" height="34" rx="17" ry="17" class="box-att" />
  <text x="85" y="1262" class="att-label">system_transfer_tot</text>

  <line x1="165" y1="1300" x2="210" y2="1225" class="line-att" />
  <rect x="40" y="1300" width="125" height="34" rx="17" ry="17" class="box-att" />
  <text x="102" y="1322" class="att-label">physical_cash_amt</text>

  <line x1="185" y1="1360" x2="240" y2="1225" class="line-att" />
  <rect x="90" y="1360" width="135" height="34" rx="17" ry="17" class="box-att" />
  <text x="157" y="1382" class="att-label">discrepancy_amount</text>

  <line x1="305" y1="1360" x2="290" y2="1225" class="line-att" />
  <rect x="245" y="1360" width="125" height="34" rx="17" ry="17" class="box-att" />
  <text x="307" y="1382" class="att-label">discrepancy_note</text>

  <line x1="420" y1="1360" x2="340" y2="1225" class="line-att" />
  <rect x="390" y="1360" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="440" y="1382" class="att-label">review_status</text>

  <line x1="420" y1="1300" x2="370" y2="1225" class="line-att" />
  <rect x="420" y="1300" width="90" height="34" rx="17" ry="17" class="box-att" />
  <text x="465" y="1322" class="att-label">is_locked</text>

  <line x1="420" y1="1257" x2="380" y2="1215" class="line-att" />
  <rect x="420" y="1240" width="90" height="34" rx="17" ry="17" class="box-att" />
  <text x="465" y="1262" class="att-label">locked_at</text>

  <line x1="420" y1="1197" x2="380" y2="1195" class="line-att" />
  <rect x="420" y="1180" width="115" height="34" rx="17" ry="17" class="box-att" />
  <text x="477" y="1202" class="att-label">report_pdf_path</text>


  <!-- ================= 4. ENTITY: study_groups ================= -->
  <rect x="1050" y="280" width="150" height="45" class="box-ent" />
  <text x="1125" y="308" class="ent-label">study_groups</text>

  <line x1="1025" y1="204" x2="1065" y2="280" class="line-att" />
  <rect x="950" y="170" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="990" y="192" class="att-pk">id</text>

  <line x1="1100" y1="204" x2="1105" y2="280" class="line-att" />
  <rect x="1050" y="170" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="1100" y="192" class="att-label">group_name</text>

  <line x1="1200" y1="204" x2="1165" y2="280" class="line-att" />
  <rect x="1170" y="170" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="1220" y="192" class="att-label">schedule_day</text>

  <line x1="1230" y1="247" x2="1200" y2="290" class="line-att" />
  <rect x="1230" y="230" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="1280" y="252" class="att-label">schedule_time</text>

  <line x1="1230" y1="307" x2="1200" y2="305" class="line-att" />
  <rect x="1230" y="290" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="1280" y="312" class="att-label">max_capacity</text>

  <line x1="1230" y1="367" x2="1200" y2="320" class="line-att" />
  <rect x="1230" y="350" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="1280" y="372" class="att-label">current_count</text>


  <!-- ================= 5. ENTITY: course_packages ================= -->
  <rect x="1750" y="280" width="160" height="45" class="box-ent" />
  <text x="1830" y="308" class="ent-label">course_packages</text>

  <line x1="1725" y1="204" x2="1765" y2="280" class="line-att" />
  <rect x="1650" y="170" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="1690" y="192" class="att-pk">id</text>

  <line x1="1800" y1="204" x2="1810" y2="280" class="line-att" />
  <rect x="1750" y="170" width="105" height="34" rx="17" ry="17" class="box-att" />
  <text x="1802" y="192" class="att-label">package_name</text>

  <line x1="1900" y1="204" x2="1870" y2="280" class="line-att" />
  <rect x="1875" y="170" width="95" height="34" rx="17" ry="17" class="box-att" />
  <text x="1922" y="192" class="att-label">grade_level</text>

  <line x1="1940" y1="247" x2="1910" y2="290" class="line-att" />
  <rect x="1940" y="230" width="95" height="34" rx="17" ry="17" class="box-att" />
  <text x="1987" y="252" class="att-label">monthly_fee</text>

  <line x1="1940" y1="307" x2="1910" y2="305" class="line-att" />
  <rect x="1940" y="290" width="95" height="34" rx="17" ry="17" class="box-att" />
  <text x="1987" y="312" class="att-label">description</text>

  <line x1="1940" y1="367" x2="1900" y2="325" class="line-att" />
  <rect x="1940" y="350" width="90" height="34" rx="17" ry="17" class="box-att" />
  <text x="1985" y="372" class="att-label">is_active</text>


  <!-- ================= 6. ENTITY: students ================= -->
  <rect x="600" y="650" width="140" height="45" class="box-ent" />
  <text x="670" y="678" class="ent-label">students</text>

  <line x1="550" y1="584" x2="615" y2="650" class="line-att" />
  <rect x="480" y="550" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="520" y="572" class="att-pk">id</text>

  <line x1="635" y1="584" x2="645" y2="650" class="line-att" />
  <rect x="580" y="550" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="630" y="572" class="att-label">registration_no</text>

  <line x1="730" y1="584" x2="705" y2="650" class="line-att" />
  <rect x="700" y="550" width="95" height="34" rx="17" ry="17" class="box-att" />
  <text x="747" y="572" class="att-label">full_name</text>

  <line x1="540" y1="627" x2="600" y2="665" class="line-att" />
  <rect x="450" y="610" width="90" height="34" rx="17" ry="17" class="box-att" />
  <text x="495" y="632" class="att-label">birth_place</text>

  <line x1="540" y1="687" x2="600" y2="680" class="line-att" />
  <rect x="450" y="670" width="90" height="34" rx="17" ry="17" class="box-att" />
  <text x="495" y="692" class="att-label">birth_date</text>

  <line x1="545" y1="730" x2="620" y2="695" class="line-att" />
  <rect x="470" y="730" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="510" y="752" class="att-label">gender</text>

  <line x1="620" y1="740" x2="650" y2="695" class="line-att" />
  <rect x="570" y="740" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="620" y="762" class="att-label">school_origin</text>

  <line x1="715" y1="740" x2="690" y2="695" class="line-att" />
  <rect x="690" y="740" width="95" height="34" rx="17" ry="17" class="box-att" />
  <text x="737" y="762" class="att-label">grade_level</text>

  <line x1="560" y1="800" x2="630" y2="695" class="line-att" />
  <rect x="470" y="800" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="520" y="822" class="att-label">home_address</text>

  <line x1="640" y1="810" x2="665" y2="695" class="line-att" />
  <rect x="590" y="810" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="640" y="832" class="att-label">parent_name</text>

  <line x1="735" y1="810" x2="710" y2="695" class="line-att" />
  <rect x="710" y="810" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="760" y="832" class="att-label">parent_phone</text>


  <!-- ================= 7. ENTITY: enrollments ================= -->
  <rect x="1150" y="650" width="140" height="45" class="box-ent" />
  <text x="1220" y="678" class="ent-label">enrollments</text>

  <line x1="1330" y1="615" x2="1290" y2="660" class="line-att" />
  <rect x="1330" y="590" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="1370" y="612" class="att-pk">id</text>

  <line x1="1330" y1="667" x2="1290" y2="672" class="line-att" />
  <rect x="1330" y="650" width="115" height="34" rx="17" ry="17" class="box-att" />
  <text x="1387" y="672" class="att-label">registration_date</text>

  <line x1="1330" y1="727" x2="1290" y2="685" class="line-att" />
  <rect x="1330" y="710" width="85" height="34" rx="17" ry="17" class="box-att" />
  <text x="1372" y="732" class="att-label">due_day</text>

  <line x1="1330" y1="775" x2="1285" y2="695" class="line-att" />
  <rect x="1330" y="770" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="1370" y="792" class="att-label">status</text>


  <!-- ================= 8. ENTITY: tuition_bills ================= -->
  <rect x="1150" y="1000" width="140" height="45" class="box-ent" />
  <text x="1220" y="1028" class="ent-label">tuition_bills</text>

  <line x1="1080" y1="955" x2="1150" y2="1010" class="line-att" />
  <rect x="1010" y="930" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="1050" y="952" class="att-pk">id</text>

  <line x1="1090" y1="1007" x2="1150" y2="1020" class="line-att" />
  <rect x="1000" y="990" width="90" height="34" rx="17" ry="17" class="box-att" />
  <text x="1045" y="1012" class="att-label">bill_period</text>

  <line x1="1085" y1="1060" x2="1150" y2="1030" class="line-att" />
  <rect x="1000" y="1050" width="85" height="34" rx="17" ry="17" class="box-att" />
  <text x="1042" y="1072" class="att-label">amount</text>

  <line x1="1120" y1="1120" x2="1185" y2="1045" class="line-att" />
  <rect x="1060" y="1120" width="90" height="34" rx="17" ry="17" class="box-att" />
  <text x="1105" y="1142" class="att-label">due_date</text>

  <line x1="1215" y1="1120" x2="1235" y2="1045" class="line-att" />
  <rect x="1170" y="1120" width="105" height="34" rx="17" ry="17" class="box-att" />
  <text x="1222" y="1142" class="att-label">payment_status</text>


  <!-- ================= 9. ENTITY: payments ================= -->
  <rect x="1750" y="1000" width="140" height="45" class="box-ent" />
  <text x="1820" y="1028" class="ent-label">payments</text>

  <line x1="1930" y1="945" x2="1890" y2="1010" class="line-att" />
  <rect x="1930" y="920" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="1970" y="942" class="att-pk">id</text>

  <line x1="1930" y1="992" x2="1890" y2="1020" class="line-att" />
  <rect x="1930" y="975" width="110" height="34" rx="17" ry="17" class="box-att" />
  <text x="1985" y="997" class="att-label">receipt_number</text>

  <line x1="1930" y1="1047" x2="1890" y2="1030" class="line-att" />
  <rect x="1930" y="1030" width="115" height="34" rx="17" ry="17" class="box-att" />
  <text x="1987" y="1052" class="att-label">payment_method</text>

  <line x1="1930" y1="1095" x2="1890" y2="1040" class="line-att" />
  <rect x="1930" y="1085" width="95" height="34" rx="17" ry="17" class="box-att" />
  <text x="1977" y="1107" class="att-label">amount_paid</text>

  <line x1="1930" y1="1145" x2="1875" y2="1045" class="line-att" />
  <rect x="1930" y="1140" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="1980" y="1162" class="att-label">payment_date</text>


  <!-- ================= 10. ENTITY: payment_proofs ================= -->
  <rect x="1750" y="1340" width="150" height="45" class="box-ent" />
  <text x="1825" y="1368" class="ent-label">payment_proofs</text>

  <line x1="1725" y1="1450" x2="1775" y2="1385" class="line-att" />
  <rect x="1670" y="1450" width="80" height="34" rx="17" ry="17" class="box-att" />
  <text x="1710" y="1472" class="att-pk">id</text>

  <line x1="1812" y1="1450" x2="1820" y2="1385" class="line-att" />
  <rect x="1770" y="1450" width="85" height="34" rx="17" ry="17" class="box-att" />
  <text x="1812" y="1472" class="att-label">file_path</text>

  <line x1="1900" y1="1450" x2="1865" y2="1385" class="line-att" />
  <rect x="1875" y="1450" width="95" height="34" rx="17" ry="17" class="box-att" />
  <text x="1922" y="1472" class="att-label">validated_at</text>

  <line x1="1940" y1="1407" x2="1900" y2="1375" class="line-att" />
  <rect x="1940" y="1390" width="110" height="34" rx="17" ry="17" class="box-att" />
  <text x="1995" y="1412" class="att-label">validation_status</text>

  <line x1="1940" y1="1347" x2="1900" y2="1350" class="line-att" />
  <rect x="1940" y="1330" width="100" height="34" rx="17" ry="17" class="box-att" />
  <text x="1990" y="1352" class="att-label">rejection_note</text>


  <!-- ================= 14 RELATIONSHIPS (DIAMONDS & LINES) ================= -->

  <!-- 1. branches -[1]- <Memiliki> -[N]- users -->
  <polygon points="392,470 445,495 392,520 340,495" class="box-rel" />
  <text x="392" y="499" class="rel-label">Memiliki</text>
  <line x1="488" y1="325" x2="392" y2="470" class="line-solid" />
  <text x="465" y="355" class="card-label">1</text>
  <line x1="392" y1="520" x2="298" y2="650" class="line-solid" />
  <text x="315" y="630" class="card-label">N</text>

  <!-- 2. branches -[1]- <Mengelola> -[N]- study_groups -->
  <polygon points="865,278 920,303 865,328 810,303" class="box-rel" />
  <text x="865" y="307" class="rel-label">Mengelola</text>
  <line x1="600" y1="303" x2="810" y2="303" class="line-solid" />
  <text x="630" y="295" class="card-label">1</text>
  <line x1="920" y1="303" x2="1050" y2="303" class="line-solid" />
  <text x="1015" y="295" class="card-label">N</text>

  <!-- 3. branches -[1]- <Menaungi> -[N]- students -->
  <polygon points="632,470 685,495 632,520 580,495" class="box-rel" />
  <text x="632" y="499" class="rel-label">Menaungi</text>
  <line x1="572" y1="325" x2="632" y2="470" class="line-solid" />
  <text x="585" y="360" class="card-label">1</text>
  <line x1="632" y1="520" x2="656" y2="650" class="line-solid" />
  <text x="635" y="625" class="card-label">N</text>

  <!-- 4. students -[1]- <Mengambil> -[N]- enrollments -->
  <polygon points="985,648 1040,673 985,698 930,673" class="box-rel" />
  <text x="985" y="677" class="rel-label">Mengambil</text>
  <line x1="740" y1="673" x2="930" y2="673" class="line-solid" />
  <text x="765" y="665" class="card-label">1</text>
  <line x1="1040" y1="673" x2="1150" y2="673" class="line-solid" />
  <text x="1115" y="665" class="card-label">N</text>

  <!-- 5. study_groups -[1]- <Ditempati> -[N]- enrollments -->
  <polygon points="1142,470 1195,495 1142,520 1090,495" class="box-rel" />
  <text x="1142" y="499" class="rel-label">Ditempati</text>
  <line x1="1125" y1="325" x2="1142" y2="470" class="line-solid" />
  <text x="1135" y="360" class="card-label">1</text>
  <line x1="1142" y1="520" x2="1185" y2="650" class="line-solid" />
  <text x="1170" y="625" class="card-label">N</text>

  <!-- 6. course_packages -[1]- <Ditawarkan> -[N]- enrollments -->
  <polygon points="1505,470 1560,495 1505,520 1450,495" class="box-rel" />
  <text x="1505" y="499" class="rel-label">Ditawarkan</text>
  <line x1="1782" y1="325" x2="1560" y2="495" class="line-solid" />
  <text x="1745" y="365" class="card-label">1</text>
  <line x1="1450" y1="495" x2="1255" y2="650" class="line-solid" />
  <text x="1275" y="630" class="card-label">N</text>

  <!-- 7. enrollments -[1]- <Menerbitkan> -[N]- tuition_bills -->
  <polygon points="1220,830 1280,855 1220,880 1160,855" class="box-rel" />
  <text x="1220" y="859" class="rel-label">Menerbitkan</text>
  <line x1="1220" y1="695" x2="1220" y2="830" class="line-solid" />
  <text x="1228" y="735" class="card-label">1</text>
  <line x1="1220" y1="880" x2="1220" y2="1000" class="line-solid" />
  <text x="1228" y="970" class="card-label">N</text>

  <!-- 8. tuition_bills -[1]- <Diselesaikan> -[N]- payments -->
  <polygon points="1540,998 1600,1023 1540,1048 1480,1023" class="box-rel" />
  <text x="1540" y="1027" class="rel-label">Diselesaikan</text>
  <line x1="1290" y1="1023" x2="1480" y2="1023" class="line-solid" />
  <text x="1315" y="1015" class="card-label">1</text>
  <line x1="1600" y1="1023" x2="1750" y2="1023" class="line-solid" />
  <text x="1715" y="1015" class="card-label">N</text>

  <!-- 9. payments -[1]- <Melampirkan> -[1]- payment_proofs -->
  <polygon points="1820,1170 1880,1195 1820,1220 1760,1195" class="box-rel" />
  <text x="1820" y="1199" class="rel-label">Melampirkan</text>
  <line x1="1820" y1="1045" x2="1820" y2="1170" class="line-solid" />
  <text x="1828" y="1085" class="card-label">1</text>
  <line x1="1820" y1="1220" x2="1820" y2="1340" class="line-solid" />
  <text x="1828" y="1315" class="card-label">1</text>

  <!-- 10. branches -[1]- <Mengadakan> -[N]- daily_reconciliations -->
  <polygon points="345,980 400,1005 345,1030 290,1005" class="box-rel" />
  <text x="345" y="1009" class="rel-label">Mengadakan</text>
  <path d="M 460 314 L 345 314 L 345 980" class="line-solid" />
  <text x="420" y="307" class="card-label">1</text>
  <line x1="345" y1="1030" x2="345" y2="1180" class="line-solid" />
  <text x="352" y="1155" class="card-label">N</text>

  <!-- 11. users -[1]- <Melakukan> -[N]- daily_reconciliations -->
  <polygon points="250,890 300,915 250,940 200,915" class="box-rel" />
  <text x="250" y="919" class="rel-label">Melakukan</text>
  <line x1="250" y1="695" x2="250" y2="890" class="line-solid" />
  <text x="235" y="735" class="card-label">1</text>
  <line x1="250" y1="940" x2="250" y2="1180" class="line-solid" />
  <text x="258" y="1155" class="card-label">N</text>

  <!-- 12. users -[1]- <Melayani> -[N]- payments -->
  <polygon points="1560,865 1610,890 1560,915 1510,890" class="box-rel" />
  <text x="1560" y="894" class="rel-label">Melayani</text>
  <path d="M 340 684 L 360 684 L 360 890 L 1510 890" class="line-solid" />
  <text x="370" y="880" class="card-label">1</text>
  <path d="M 1610 890 L 1680 890 L 1680 1011 L 1750 1011" class="line-solid" />
  <text x="1710" y="1003" class="card-label">N</text>

  <!-- 13. users -[1]- <Memvalidasi> -[N]- payment_proofs -->
  <polygon points="1535,1337 1590,1362 1535,1387 1480,1362" class="box-rel" />
  <text x="1535" y="1366" class="rel-label">Memvalidasi</text>
  <path d="M 312 695 L 312 730 L 550 730 L 550 1362 L 1480 1362" class="line-solid" />
  <text x="560" y="1352" class="card-label">1</text>
  <line x1="1590" y1="1362" x2="1750" y2="1362" class="line-solid" />
  <text x="1715" y="1354" class="card-label">N</text>

  <!-- 14. branches -[1]- <Menerima> -[N]- payments -->
  <polygon points="2120,650 2170,675 2120,700 2070,675" class="box-rel" />
  <text x="2120" y="679" class="rel-label">Menerima</text>
  <path d="M 530 280 L 530 80 L 2120 80 L 2120 650" class="line-solid" />
  <text x="540" y="110" class="card-label">1</text>
  <path d="M 2120 700 L 2120 1220 L 1855 1220 L 1855 1045" class="line-solid" />
  <text x="1862" y="1075" class="card-label">N</text>

</svg>'''
    return svg

# -----------------------------------------------------------------------------
# 3. WRITE FILES & RENDER HIGH-RES PNG
# -----------------------------------------------------------------------------
drawio_content = get_chen_v2_drawio()
svg_content = get_chen_v2_svg()

for d in output_dirs:
    drawio_p = os.path.join(d, 'Gambar_3_9_ERD_Chen_ARTHA.drawio')
    svg_p = os.path.join(d, 'Gambar_3_9_ERD_Chen_ARTHA.svg')
    with open(drawio_p, 'w', encoding='utf-8') as f:
        f.write(drawio_content)
    with open(svg_p, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Updated Draw.io & SVG at: {d}")

# Render PNG via Playwright
primary_svg = os.path.join(output_dirs[0], 'Gambar_3_9_ERD_Chen_ARTHA.svg')
with open(primary_svg, 'r', encoding='utf-8') as f:
    svg_data = f.read()

html_content = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{
      margin: 0;
      padding: 0;
      background: white;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
  </style>
</head>
<body>
  {svg_data}
</body>
</html>'''

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge')
    page = browser.new_page(viewport={"width": 2240, "height": 1580}, device_scale_factor=2)
    page.set_content(html_content)

    for out_d in output_dirs:
        png_path = os.path.join(out_d, 'Gambar_3_9_ERD_Chen_ARTHA.png')
        page.screenshot(path=png_path)
        print(f"Rendered PNG: {png_path}")

    artifact_png = r'C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\Gambar_3_9_ERD_Chen_ARTHA.png'
    page.screenshot(path=artifact_png)
    print(f"Rendered Artifact PNG: {artifact_png}")

    page.close()
    browser.close()

# Also update master Draw.io file
for d in output_dirs:
    master_p = os.path.join(d, 'ARTHA_Semua_Diagram_UML_Bab3.drawio')
    if os.path.exists(master_p):
        with open(master_p, 'r', encoding='utf-8') as f:
            mc = f.read()
        m = re.search(r'<diagram\s+[^>]*>(.*?)</diagram>', drawio_content, re.DOTALL)
        if m:
            inner = m.group(1).strip()
            # Replace existing diag_chen_3_9 or append
            if 'diag_chen_3_9' in mc:
                mc = re.sub(r'<diagram id="diag_chen_3_9"[^>]*>.*?</diagram>', f'<diagram id="diag_chen_3_9" name="Gambar 3.9 ERD Chen ARTHA">\n    {inner}\n  </diagram>', mc, flags=re.DOTALL)
            else:
                chen_page = f'  <diagram id="diag_chen_3_9" name="Gambar 3.9 ERD Chen ARTHA">\n    {inner}\n  </diagram>'
                mc = mc.replace('</mxfile>', f'{chen_page}\n</mxfile>')
            with open(master_p, 'w', encoding='utf-8') as f:
                f.write(mc)
            print(f"Updated Master Drawio: {master_p}")

print("V2 ZERO-COLLISION CHEN DIAGRAM COMPLETE!")

