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
# 1. DRAW.IO XML GENERATOR FOR CHEN NOTATION ERD
# -----------------------------------------------------------------------------
def get_chen_drawio_xml():
    # Style presets matching the user's reference image:
    # Entities: rectangle, white fill, black border, bold text
    # Attributes: ellipse, white fill, black border, normal text (PK underlined)
    # Relationships: rhombus/diamond, white fill, black border, bold/normal text
    # Lines: straight, no arrows, black stroke
    
    xml = '''<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="diagram_chen" name="Gambar 3.9 ERD Notasi Chen ARTHA">
    <mxGraphModel dx="2200" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2000" pageHeight="1600" background="#ffffff">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Block -->
        <mxCell id="title" value="&lt;b style=&quot;font-size: 16px;&quot;&gt;Entity Relationship Diagram (ERD) - Notasi Peter Chen&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#555555&quot;&gt;Sistem Informasi Bimbingan Belajar Multicabang ARTHA&lt;/font&gt;" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="550" height="40" as="geometry" />
        </mxCell>

        <!-- Legend Block -->
        <mxCell id="legend" value="&lt;b&gt;Standar Simbol Notasi Chen:&lt;/b&gt;&lt;br&gt;[ Persegi Panjang ] = Entitas &amp;nbsp;&amp;nbsp;|&amp;nbsp;&amp;nbsp; ( Elips ) = Atribut &amp;nbsp;&amp;nbsp;|&amp;nbsp;&amp;nbsp; ( &lt;u&gt;Garis Bawah&lt;/u&gt; ) = Primary Key &amp;nbsp;&amp;nbsp;|&amp;nbsp;&amp;nbsp; &amp;lt; Belah Ketupat &amp;gt; = Relasi &amp;nbsp;&amp;nbsp;|&amp;nbsp;&amp;nbsp; 1 / N = Rasio Kardinalitas" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FAFAFA;strokeColor=#000000;strokeWidth=1;align=center;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1080" y="20" width="850" height="36" as="geometry" />
        </mxCell>

        <!-- ============================================================= -->
        <!-- 1. ENTITY: branches (x=450, y=240, w=130, h=45)               -->
        <!-- ============================================================= -->
        <mxCell id="ent_branches" value="&lt;b&gt;branches&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="450" y="240" width="130" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes branches -->
        <mxCell id="att_br_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="340" y="140" width="85" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_id" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0;entryDx=0;entryDy=0;exitX=0.8;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_br_id" target="ent_branches"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_br_code" value="branch_code" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="460" y="140" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_code" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_br_code" target="ent_branches"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_br_name" value="branch_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="585" y="140" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_name" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0;entryDx=0;entryDy=0;exitX=0.2;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_br_name" target="ent_branches"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_br_addr" value="address" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="320" y="246" width="85" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_addr" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_br_addr" target="ent_branches"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_br_phone" value="phone" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="340" y="315" width="85" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_phone" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=1;entryDx=0;entryDy=0;exitX=0.8;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_br_phone" target="ent_branches"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- ============================================================= -->
        <!-- 2. ENTITY: users (x=160, y=600, w=120, h=45)                  -->
        <!-- ============================================================= -->
        <mxCell id="ent_users" value="&lt;b&gt;users&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="160" y="600" width="120" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes users -->
        <mxCell id="att_u_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="50" y="525" width="75" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_u_id" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0;entryDx=0;entryDy=0;exitX=1;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_u_id" target="ent_users"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_u_email" value="email" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="580" width="80" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_u_email" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0.4;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_u_email" target="ent_users"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_u_name" value="name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="635" width="80" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_u_name" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0.7;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_u_name" target="ent_users"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_u_pwd" value="password" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="50" y="690" width="80" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_u_pwd" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.2;entryY=1;entryDx=0;entryDy=0;exitX=0.9;exitY=0.2;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_u_pwd" target="ent_users"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_u_role" value="role" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="145" y="700" width="75" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_u_role" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.5;entryY=1;entryDx=0;entryDy=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_u_role" target="ent_users"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- ============================================================= -->
        <!-- 3. ENTITY: study_groups (x=980, y=240, w=140, h=45)            -->
        <!-- ============================================================= -->
        <mxCell id="ent_study_groups" value="&lt;b&gt;study_groups&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="980" y="240" width="140" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes study_groups -->
        <mxCell id="att_sg_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="880" y="140" width="80" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_id" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0;entryDx=0;entryDy=0;exitX=0.8;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_sg_id" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_sg_name" value="group_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="980" y="140" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_name" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.4;entryY=0;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_sg_name" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_sg_day" value="schedule_day" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1095" y="140" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_day" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.8;entryY=0;entryDx=0;entryDy=0;exitX=0.3;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_sg_day" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_sg_time" value="schedule_time" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1145" y="195" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_time" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.2;entryDx=0;entryDy=0;exitX=0;exitY=0.7;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_sg_time" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_sg_max" value="max_capacity" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1145" y="250" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_max" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.7;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_sg_max" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_sg_curr" value="current_count" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1145" y="305" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_curr" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.9;entryY=1;entryDx=0;entryDy=0;exitX=0;exitY=0.3;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_sg_curr" target="ent_study_groups"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- ============================================================= -->
        <!-- 4. ENTITY: course_packages (x=1600, y=240, w=150, h=45)        -->
        <!-- ============================================================= -->
        <mxCell id="ent_course_packages" value="&lt;b&gt;course_packages&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="1600" y="240" width="150" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes course_packages -->
        <mxCell id="att_cp_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1510" y="140" width="80" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_id" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.2;entryY=0;entryDx=0;entryDy=0;exitX=0.8;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_cp_id" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_cp_name" value="package_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1610" y="140" width="100" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_name" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_cp_name" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_cp_grade" value="grade_level" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1730" y="140" width="90" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_grade" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.8;entryY=0;entryDx=0;entryDy=0;exitX=0.2;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_cp_grade" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_cp_fee" value="monthly_fee" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1780" y="200" width="90" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_fee" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.2;entryDx=0;entryDy=0;exitX=0;exitY=0.7;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_cp_fee" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_cp_desc" value="description" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1780" y="255" width="90" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_desc" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.7;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_cp_desc" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_cp_act" value="is_active" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1780" y="310" width="85" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_act" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.9;entryY=1;entryDx=0;entryDy=0;exitX=0;exitY=0.3;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_cp_act" target="ent_course_packages"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- ============================================================= -->
        <!-- 5. ENTITY: students (x=520, y=600, w=130, h=45)               -->
        <!-- ============================================================= -->
        <mxCell id="ent_students" value="&lt;b&gt;students&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="520" y="600" width="130" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes students (radiating out) -->
        <mxCell id="att_st_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="400" y="520" width="75" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_id" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0;entryDx=0;entryDy=0;exitX=1;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_st_id" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_reg" value="registration_no" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="490" y="520" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_reg" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.3;entryY=0;entryDx=0;entryDy=0;exitX=0.6;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_st_reg" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_fn" value="full_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="600" y="520" width="90" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_fn" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.7;entryY=0;entryDx=0;entryDy=0;exitX=0.3;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_st_fn" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_bp" value="birth_place" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="380" y="575" width="85" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_bp" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0.4;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_st_bp" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_bd" value="birth_date" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="380" y="625" width="85" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_bd" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0.7;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_st_bd" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_gen" value="gender" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="400" y="680" width="80" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_gen" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.1;entryY=1;entryDx=0;entryDy=0;exitX=0.8;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_st_gen" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_sch" value="school_origin" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="495" y="695" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_sch" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.4;entryY=1;entryDx=0;entryDy=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_st_sch" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_grd" value="grade_level" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="605" y="695" width="90" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_grd" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.7;entryY=1;entryDx=0;entryDy=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_st_grd" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_addr" value="home_address" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="705" y="680" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_addr" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=1;entryDx=0;entryDy=0;exitX=0.2;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_st_addr" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_pn" value="parent_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="400" y="745" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_pn" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.2;entryY=1;entryDx=0;entryDy=0;exitX=0.7;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_st_pn" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_st_pp" value="parent_phone" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="515" y="755" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_st_pp" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.5;entryY=1;entryDx=0;entryDy=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_st_pp" target="ent_students"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- ============================================================= -->
        <!-- 6. ENTITY: enrollments (x=1050, y=600, w=130, h=45)           -->
        <!-- ============================================================= -->
        <mxCell id="ent_enrollments" value="&lt;b&gt;enrollments&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="1050" y="600" width="130" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes enrollments -->
        <mxCell id="att_en_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1205" y="535" width="75" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_en_id" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.2;entryDx=0;entryDy=0;exitX=0;exitY=0.8;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_en_id" target="ent_enrollments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_en_date" value="registration_date" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1215" y="585" width="105" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_en_date" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_en_date" target="ent_enrollments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_en_day" value="due_day" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1215" y="635" width="85" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_en_day" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.8;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_en_day" target="ent_enrollments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_en_stat" value="status" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1205" y="685" width="75" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_en_stat" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.9;entryY=1;entryDx=0;entryDy=0;exitX=0;exitY=0.2;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_en_stat" target="ent_enrollments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- ============================================================= -->
        <!-- 7. ENTITY: tuition_bills (x=1050, y=950, w=130, h=45)         -->
        <!-- ============================================================= -->
        <mxCell id="ent_tuition_bills" value="&lt;b&gt;tuition_bills&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="1050" y="950" width="130" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes tuition_bills -->
        <mxCell id="att_tb_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="920" y="910" width="75" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_tb_id" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0.2;entryDx=0;entryDy=0;exitX=1;exitY=0.8;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_tb_id" target="ent_tuition_bills"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_tb_per" value="bill_period" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="915" y="960" width="85" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_tb_per" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_tb_per" target="ent_tuition_bills"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_tb_amt" value="amount" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="920" y="1010" width="80" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_tb_amt" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0.8;entryDx=0;entryDy=0;exitX=1;exitY=0.3;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_tb_amt" target="ent_tuition_bills"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_tb_due" value="due_date" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1000" y="1040" width="85" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_tb_due" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.3;entryY=1;entryDx=0;entryDy=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_tb_due" target="ent_tuition_bills"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_tb_stat" value="payment_status" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1105" y="1040" width="100" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_tb_stat" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.7;entryY=1;entryDx=0;entryDy=0;exitX=0.4;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_tb_stat" target="ent_tuition_bills"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- ============================================================= -->
        <!-- 8. ENTITY: payments (x=1560, y=950, w=130, h=45)              -->
        <!-- ============================================================= -->
        <mxCell id="ent_payments" value="&lt;b&gt;payments&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="1560" y="950" width="130" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes payments -->
        <mxCell id="att_pay_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1465" y="860" width="75" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_pay_id" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.2;entryY=0;entryDx=0;entryDy=0;exitX=0.8;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_pay_id" target="ent_payments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pay_rec" value="receipt_number" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1560" y="860" width="105" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_pay_rec" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_pay_rec" target="ent_payments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pay_meth" value="payment_method" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1685" y="860" width="110" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_pay_meth" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.8;entryY=0;entryDx=0;entryDy=0;exitX=0.2;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_pay_meth" target="ent_payments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pay_amt" value="amount_paid" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1730" y="930" width="90" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_pay_amt" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.4;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_pay_amt" target="ent_payments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pay_date" value="payment_date" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1730" y="985" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_pay_date" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.8;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_pay_date" target="ent_payments"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- ============================================================= -->
        <!-- 9. ENTITY: payment_proofs (x=1560, y=1330, w=140, h=45)       -->
        <!-- ============================================================= -->
        <mxCell id="ent_payment_proofs" value="&lt;b&gt;payment_proofs&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="1560" y="1330" width="140" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes payment_proofs -->
        <mxCell id="att_pp_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1440" y="1336" width="75" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_pp_id" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_pp_id" target="ent_payment_proofs"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pp_path" value="file_path" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1440" y="1395" width="80" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_pp_path" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=1;entryDx=0;entryDy=0;exitX=1;exitY=0.2;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_pp_path" target="ent_payment_proofs"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pp_time" value="validated_at" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1540" y="1425" width="90" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_pp_time" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.4;entryY=1;entryDx=0;entryDy=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_pp_time" target="ent_payment_proofs"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pp_stat" value="validation_status" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1650" y="1425" width="105" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_pp_stat" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.7;entryY=1;entryDx=0;entryDy=0;exitX=0.4;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_pp_stat" target="ent_payment_proofs"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_pp_note" value="rejection_note" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1745" y="1375" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_pp_note" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=1;entryDx=0;entryDy=0;exitX=0;exitY=0.2;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_pp_note" target="ent_payment_proofs"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- ============================================================= -->
        <!-- 10. ENTITY: daily_reconciliations (x=240, y=1100, w=160, h=45)-->
        <!-- ============================================================= -->
        <mxCell id="ent_daily_rec" value="&lt;b&gt;daily_reconciliations&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="240" y="1100" width="160" height="45" as="geometry" />
        </mxCell>
        <!-- Attributes daily_reconciliations -->
        <mxCell id="att_dr_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="90" y="1030" width="75" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_id" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0;entryDx=0;entryDy=0;exitX=0.9;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_dr_id" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_date" value="reconciliation_date" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="80" y="1080" width="115" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_date" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0.3;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_dr_date" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_sysc" value="system_cash_total" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="75" y="1130" width="120" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_sysc" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=0.7;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_dr_sysc" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_syst" value="system_transfer_tot" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="75" y="1180" width="120" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_syst" style="endArrow=none;html=1;strokeColor=#000000;entryX=0;entryY=1;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_dr_syst" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_phy" value="physical_cash_amt" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="140" y="1230" width="115" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_phy" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.2;entryY=1;entryDx=0;entryDy=0;exitX=0.7;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_dr_phy" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_disc" value="discrepancy_amount" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="270" y="1230" width="125" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_disc" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.5;entryY=1;entryDx=0;entryDy=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_dr_disc" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_note" value="discrepancy_note" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="410" y="1230" width="115" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_note" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.8;entryY=1;entryDx=0;entryDy=0;exitX=0.3;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_dr_note" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_rev" value="review_status" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="440" y="1175" width="95" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_rev" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.8;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_dr_rev" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_lock" value="is_locked" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="440" y="1120" width="85" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_lock" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_dr_lock" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_ltime" value="locked_at" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="440" y="1065" width="85" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_ltime" style="endArrow=none;html=1;strokeColor=#000000;entryX=1;entryY=0.2;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_dr_ltime" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="att_dr_pdf" value="report_pdf_path" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="440" y="1010" width="105" height="32" as="geometry" />
        </mxCell>
        <mxCell id="edge_dr_pdf" style="endArrow=none;html=1;strokeColor=#000000;entryX=0.9;entryY=0;entryDx=0;entryDy=0;exitX=0;exitY=0.8;exitDx=0;exitDy=0;" edge="1" parent="1" source="att_dr_pdf" target="ent_daily_rec"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ============================================================= -->
        <!-- RELATIONSHIPS (DIAMONDS) & CARDINALITY (1, N)                  -->
        <!-- ============================================================= -->

        <!-- 1. branches -[1]- <Memiliki> -[N]- users -->
        <mxCell id="rel_memiliki" value="Memiliki" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="270" y="420" width="100" height="50" as="geometry" />
        </mxCell>
        <!-- Line: branches to Memiliki -->
        <mxCell id="edge_br_mem" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.1;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_branches" target="rel_memiliki">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_br_mem_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_br_mem">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="-12" y="-5" as="offset" /></mxGeometry>
        </mxCell>
        <!-- Line: Memiliki to users -->
        <mxCell id="edge_mem_usr" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.6;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_memiliki" target="ent_users">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mem_usr_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mem_usr">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" y="5" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 2. branches -[1]- <Mengelola> -[N]- study_groups -->
        <mxCell id="rel_mengelola" value="Mengelola" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="740" y="238" width="110" height="50" as="geometry" />
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
          <mxGeometry x="460" y="420" width="100" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_mng" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_branches" target="rel_menaungi">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_br_mng_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_br_mng">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mng_st" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.3;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_menaungi" target="ent_students">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mng_st_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mng_st">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 4. students -[1]- <Mengambil> -[N]- enrollments -->
        <mxCell id="rel_mengambil" value="Mengambil" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="830" y="598" width="110" height="50" as="geometry" />
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
          <mxGeometry x="1000" y="420" width="100" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_sg_dtp" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_study_groups" target="rel_ditempati">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_sg_dtp_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_sg_dtp">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_dtp_en" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.3;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_ditempati" target="ent_enrollments">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_dtp_en_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_dtp_en">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 6. course_packages -[1]- <Ditawarkan> -[N]- enrollments -->
        <mxCell id="rel_ditawarkan" value="Ditawarkan" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1350" y="420" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_cp_dtw" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.2;exitY=1;exitDx=0;exitDy=0;entryX=0.8;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_course_packages" target="rel_ditawarkan">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_cp_dtw_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_cp_dtw">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_dtw_en" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.2;exitY=1;exitDx=0;exitDy=0;entryX=0.7;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_ditawarkan" target="ent_enrollments">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_dtw_en_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_dtw_en">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 7. enrollments -[1]- <Menerbitkan> -[N]- tuition_bills -->
        <mxCell id="rel_menerbitkan" value="Menerbitkan" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1055" y="780" width="120" height="50" as="geometry" />
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
          <mxGeometry x="1330" y="948" width="120" height="50" as="geometry" />
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
          <mxGeometry x="1565" y="1135" width="120" height="50" as="geometry" />
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
        <mxCell id="rel_mengadakan" value="Mengadakan" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="270" y="870" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_mgd" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0;exitY=0.8;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_branches" target="rel_mengadakan">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="325" y="276" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lbl_br_mgd_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_br_mgd">
          <mxGeometry x="-0.6" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mgd_dr" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_mengadakan" target="ent_daily_rec">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mgd_dr_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mgd_dr">
          <mxGeometry x="0.4" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 11. users -[1]- <Melakukan> -[N]- daily_reconciliations -->
        <mxCell id="rel_melakukan" value="Melakukan" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="170" y="870" width="100" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_usr_mlk" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_users" target="rel_melakukan">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_usr_mlk_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_usr_mlk">
          <mxGeometry x="-0.3" relative="1" as="geometry"><mxPoint x="-12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mlk_dr" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.2;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_melakukan" target="ent_daily_rec">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mlk_dr_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mlk_dr">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="-12" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 12. users -[1]- <Melayani> -[N]- payments -->
        <mxCell id="rel_melayani" value="Melayani" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1330" y="830" width="100" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_usr_mly" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_users" target="rel_melayani">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="320" y="622" />
              <mxPoint x="320" y="855" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lbl_usr_mly_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_usr_mly">
          <mxGeometry x="-0.8" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mly_pay" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.2;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_melayani" target="ent_payments">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mly_pay_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mly_pay">
          <mxGeometry x="0.4" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 13. users -[1]- <Memvalidasi> -[N]- payment_proofs -->
        <mxCell id="rel_memvalidasi" value="Memvalidasi" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1330" y="1328" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_usr_mvl" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_users" target="rel_memvalidasi">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="220" y="1353" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lbl_usr_mvl_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_usr_mvl">
          <mxGeometry x="-0.8" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mvl_pp" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_memvalidasi" target="ent_payment_proofs">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mvl_pp_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mvl_pp">
          <mxGeometry x="0.4" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>

        <!-- 14. branches -[1]- <Menerima> -[N]- payments -->
        <mxCell id="rel_menerima" value="Menerima" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1575" y="720" width="100" height="50" as="geometry" />
        </mxCell>
        <mxCell id="edge_br_mnr" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.9;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="ent_branches" target="rel_menerima">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="567" y="100" />
              <mxPoint x="1625" y="100" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lbl_br_mnr_1" value="1" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_br_mnr">
          <mxGeometry x="-0.8" relative="1" as="geometry"><mxPoint y="-10" as="offset" /></mxGeometry>
        </mxCell>
        <mxCell id="edge_mnr_pay" style="endArrow=none;html=1;strokeColor=#000000;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="rel_menerima" target="ent_payments">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="lbl_mnr_pay_n" value="N" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=13;fontStyle=1;" vertex="1" connectable="0" parent="edge_mnr_pay">
          <mxGeometry x="0.3" relative="1" as="geometry"><mxPoint x="12" as="offset" /></mxGeometry>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml

# -----------------------------------------------------------------------------
# 2. GENERATE SVG FOR CHEN NOTATION
# -----------------------------------------------------------------------------
def generate_chen_svg():
    width = 1920
    height = 1520

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      .title {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 18px; font-weight: bold; fill: #000000; }}
      .sub-title {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #444444; }}
      .legend-box {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 11.5px; fill: #000000; text-anchor: middle; }}
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

  <!-- Background -->
  <rect width="{width}" height="{height}" fill="#ffffff" />

  <!-- Title Block -->
  <text x="50" y="38" class="title">Entity Relationship Diagram (ERD) - Notasi Peter Chen</text>
  <text x="50" y="58" class="sub-title">Sistem Informasi Pengelolaan Bimbingan Belajar Multicabang ARTHA</text>

  <!-- Legend -->
  <g transform="translate(1050, 22)">
    <rect width="820" height="42" rx="4" ry="4" fill="#FAFAFA" stroke="#000000" stroke-width="1.2" />
    <text x="410" y="26" class="legend-box"><b>Standar Simbol Notasi Chen:</b> &nbsp; [ Persegi Panjang ] = Entitas &nbsp;|&nbsp; ( Elips ) = Atribut &nbsp;|&nbsp; <u>Garis Bawah</u> = Kunci Utama (PK) &nbsp;|&nbsp; &lt; Belah Ketupat &gt; = Relasi &nbsp;|&nbsp; 1 / N = Rasio Kardinalitas</text>
  </g>

  <!-- ================= 1. ENTITY: branches ================= -->
  <!-- Entity Box -->
  <rect x="450" y="240" width="130" height="45" class="box-ent" />
  <text x="515" y="268" class="ent-label">branches</text>

  <!-- Attribute Lines & Ovals -->
  <line x1="382" y1="172" x2="470" y2="240" class="line-att" />
  <rect x="340" y="140" width="85" height="32" rx="16" ry="16" class="box-att" />
  <text x="382" y="161" class="att-pk">id</text>

  <line x1="507" y1="172" x2="515" y2="240" class="line-att" />
  <rect x="460" y="140" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="507" y="161" class="att-label">branch_code</text>

  <line x1="632" y1="172" x2="560" y2="240" class="line-att" />
  <rect x="585" y="140" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="632" y="161" class="att-label">branch_name</text>

  <line x1="405" y1="262" x2="450" y2="262" class="line-att" />
  <rect x="320" y="246" width="85" height="32" rx="16" ry="16" class="box-att" />
  <text x="362" y="267" class="att-label">address</text>

  <line x1="408" y1="315" x2="450" y2="280" class="line-att" />
  <rect x="340" y="315" width="85" height="32" rx="16" ry="16" class="box-att" />
  <text x="382" y="336" class="att-label">phone</text>


  <!-- ================= 2. ENTITY: users ================= -->
  <rect x="160" y="600" width="120" height="45" class="box-ent" />
  <text x="220" y="628" class="ent-label">users</text>

  <line x1="125" y1="550" x2="160" y2="600" class="line-att" />
  <rect x="50" y="525" width="75" height="32" rx="16" ry="16" class="box-att" />
  <text x="87" y="546" class="att-pk">id</text>

  <line x1="120" y1="596" x2="160" y2="610" class="line-att" />
  <rect x="40" y="580" width="80" height="32" rx="16" ry="16" class="box-att" />
  <text x="80" y="601" class="att-label">email</text>

  <line x1="120" y1="651" x2="160" y2="630" class="line-att" />
  <rect x="40" y="635" width="80" height="32" rx="16" ry="16" class="box-att" />
  <text x="80" y="656" class="att-label">name</text>

  <line x1="130" y1="700" x2="180" y2="645" class="line-att" />
  <rect x="50" y="690" width="80" height="32" rx="16" ry="16" class="box-att" />
  <text x="90" y="711" class="att-label">password</text>

  <line x1="182" y1="700" x2="210" y2="645" class="line-att" />
  <rect x="145" y="700" width="75" height="32" rx="16" ry="16" class="box-att" />
  <text x="182" y="721" class="att-label">role</text>


  <!-- ================= 3. ENTITY: study_groups ================= -->
  <rect x="980" y="240" width="140" height="45" class="box-ent" />
  <text x="1050" y="268" class="ent-label">study_groups</text>

  <line x1="944" y1="172" x2="990" y2="240" class="line-att" />
  <rect x="880" y="140" width="80" height="32" rx="16" ry="16" class="box-att" />
  <text x="920" y="161" class="att-pk">id</text>

  <line x1="1027" y1="172" x2="1035" y2="240" class="line-att" />
  <rect x="980" y="140" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="1027" y="161" class="att-label">group_name</text>

  <line x1="1120" y1="172" x2="1090" y2="240" class="line-att" />
  <rect x="1095" y="140" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="1142" y="161" class="att-label">schedule_day</text>

  <line x1="1145" y1="211" x2="1120" y2="245" class="line-att" />
  <rect x="1145" y="195" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="1192" y="216" class="att-label">schedule_time</text>

  <line x1="1145" y1="266" x2="1120" y2="266" class="line-att" />
  <rect x="1145" y="250" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="1192" y="271" class="att-label">max_capacity</text>

  <line x1="1145" y1="315" x2="1110" y2="285" class="line-att" />
  <rect x="1145" y="305" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="1192" y="326" class="att-label">current_count</text>


  <!-- ================= 4. ENTITY: course_packages ================= -->
  <rect x="1600" y="240" width="150" height="45" class="box-ent" />
  <text x="1675" y="268" class="ent-label">course_packages</text>

  <line x1="1574" y1="172" x2="1625" y2="240" class="line-att" />
  <rect x="1510" y="140" width="80" height="32" rx="16" ry="16" class="box-att" />
  <text x="1550" y="161" class="att-pk">id</text>

  <line x1="1660" y1="172" x2="1670" y2="240" class="line-att" />
  <rect x="1610" y="140" width="100" height="32" rx="16" ry="16" class="box-att" />
  <text x="1660" y="161" class="att-label">package_name</text>

  <line x1="1750" y1="172" x2="1715" y2="240" class="line-att" />
  <rect x="1730" y="140" width="90" height="32" rx="16" ry="16" class="box-att" />
  <text x="1775" y="161" class="att-label">grade_level</text>

  <line x1="1780" y1="216" x2="1750" y2="248" class="line-att" />
  <rect x="1780" y="200" width="90" height="32" rx="16" ry="16" class="box-att" />
  <text x="1825" y="221" class="att-label">monthly_fee</text>

  <line x1="1780" y1="271" x2="1750" y2="271" class="line-att" />
  <rect x="1780" y="255" width="90" height="32" rx="16" ry="16" class="box-att" />
  <text x="1825" y="276" class="att-label">description</text>

  <line x1="1780" y1="320" x2="1740" y2="285" class="line-att" />
  <rect x="1780" y="310" width="85" height="32" rx="16" ry="16" class="box-att" />
  <text x="1822" y="331" class="att-label">is_active</text>


  <!-- ================= 5. ENTITY: students ================= -->
  <rect x="520" y="600" width="130" height="45" class="box-ent" />
  <text x="585" y="628" class="ent-label">students</text>

  <line x1="455" y1="545" x2="520" y2="600" class="line-att" />
  <rect x="400" y="520" width="75" height="32" rx="16" ry="16" class="box-att" />
  <text x="437" y="541" class="att-pk">id</text>

  <line x1="545" y1="552" x2="555" y2="600" class="line-att" />
  <rect x="490" y="520" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="537" y="541" class="att-label">registration_no</text>

  <line x1="630" y1="552" x2="615" y2="600" class="line-att" />
  <rect x="600" y="520" width="90" height="32" rx="16" ry="16" class="box-att" />
  <text x="645" y="541" class="att-label">full_name</text>

  <line x1="465" y1="591" x2="520" y2="615" class="line-att" />
  <rect x="380" y="575" width="85" height="32" rx="16" ry="16" class="box-att" />
  <text x="422" y="596" class="att-label">birth_place</text>

  <line x1="465" y1="635" x2="520" y2="630" class="line-att" />
  <rect x="380" y="625" width="85" height="32" rx="16" ry="16" class="box-att" />
  <text x="422" y="646" class="att-label">birth_date</text>

  <line x1="470" y1="685" x2="530" y2="645" class="line-att" />
  <rect x="400" y="680" width="80" height="32" rx="16" ry="16" class="box-att" />
  <text x="440" y="701" class="att-label">gender</text>

  <line x1="542" y1="695" x2="560" y2="645" class="line-att" />
  <rect x="495" y="695" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="542" y="716" class="att-label">school_origin</text>

  <line x1="640" y1="695" x2="610" y2="645" class="line-att" />
  <rect x="605" y="695" width="90" height="32" rx="16" ry="16" class="box-att" />
  <text x="650" y="716" class="att-label">grade_level</text>

  <line x1="720" y1="680" x2="645" y2="645" class="line-att" />
  <rect x="705" y="680" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="752" y="701" class="att-label">home_address</text>

  <line x1="465" y1="745" x2="540" y2="645" class="line-att" />
  <rect x="400" y="745" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="447" y="766" class="att-label">parent_name</text>

  <line x1="562" y1="755" x2="585" y2="645" class="line-att" />
  <rect x="515" y="755" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="562" y="776" class="att-label">parent_phone</text>


  <!-- ================= 6. ENTITY: enrollments ================= -->
  <rect x="1050" y="600" width="130" height="45" class="box-ent" />
  <text x="1115" y="628" class="ent-label">enrollments</text>

  <line x1="1205" y1="560" x2="1180" y2="610" class="line-att" />
  <rect x="1205" y="535" width="75" height="32" rx="16" ry="16" class="box-att" />
  <text x="1242" y="556" class="att-pk">id</text>

  <line x1="1215" y1="601" x2="1180" y2="622" class="line-att" />
  <rect x="1215" y="585" width="105" height="32" rx="16" ry="16" class="box-att" />
  <text x="1267" y="606" class="att-label">registration_date</text>

  <line x1="1215" y1="645" x2="1180" y2="635" class="line-att" />
  <rect x="1215" y="635" width="85" height="32" rx="16" ry="16" class="box-att" />
  <text x="1257" y="656" class="att-label">due_day</text>

  <line x1="1205" y1="695" x2="1165" y2="645" class="line-att" />
  <rect x="1205" y="685" width="75" height="32" rx="16" ry="16" class="box-att" />
  <text x="1242" y="706" class="att-label">status</text>


  <!-- ================= 7. ENTITY: tuition_bills ================= -->
  <rect x="1050" y="950" width="130" height="45" class="box-ent" />
  <text x="1115" y="978" class="ent-label">tuition_bills</text>

  <line x1="995" y1="935" x2="1050" y2="960" class="line-att" />
  <rect x="920" y="910" width="75" height="32" rx="16" ry="16" class="box-att" />
  <text x="957" y="931" class="att-pk">id</text>

  <line x1="1000" y1="976" x2="1050" y2="972" class="line-att" />
  <rect x="915" y="960" width="85" height="32" rx="16" ry="16" class="box-att" />
  <text x="957" y="981" class="att-label">bill_period</text>

  <line x1="1000" y1="1015" x2="1050" y2="985" class="line-att" />
  <rect x="920" y="1010" width="80" height="32" rx="16" ry="16" class="box-att" />
  <text x="960" y="1031" class="att-label">amount</text>

  <line x1="1042" y1="1040" x2="1085" y2="995" class="line-att" />
  <rect x="1000" y="1040" width="85" height="32" rx="16" ry="16" class="box-att" />
  <text x="1042" y="1061" class="att-label">due_date</text>

  <line x1="1145" y1="1040" x2="1140" y2="995" class="line-att" />
  <rect x="1105" y="1040" width="100" height="32" rx="16" ry="16" class="box-att" />
  <text x="1155" y="1061" class="att-label">payment_status</text>


  <!-- ================= 8. ENTITY: payments ================= -->
  <rect x="1560" y="950" width="130" height="45" class="box-ent" />
  <text x="1625" y="978" class="ent-label">payments</text>

  <line x1="1525" y1="892" x2="1585" y2="950" class="line-att" />
  <rect x="1465" y="860" width="75" height="32" rx="16" ry="16" class="box-att" />
  <text x="1502" y="881" class="att-pk">id</text>

  <line x1="1612" y1="892" x2="1625" y2="950" class="line-att" />
  <rect x="1560" y="860" width="105" height="32" rx="16" ry="16" class="box-att" />
  <text x="1612" y="881" class="att-label">receipt_number</text>

  <line x1="1710" y1="892" x2="1665" y2="950" class="line-att" />
  <rect x="1685" y="860" width="110" height="32" rx="16" ry="16" class="box-att" />
  <text x="1740" y="881" class="att-label">payment_method</text>

  <line x1="1730" y1="946" x2="1690" y2="965" class="line-att" />
  <rect x="1730" y="930" width="90" height="32" rx="16" ry="16" class="box-att" />
  <text x="1775" y="951" class="att-label">amount_paid</text>

  <line x1="1730" y1="1001" x2="1690" y2="985" class="line-att" />
  <rect x="1730" y="985" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="1777" y="1006" class="att-label">payment_date</text>


  <!-- ================= 9. ENTITY: payment_proofs ================= -->
  <rect x="1560" y="1330" width="140" height="45" class="box-ent" />
  <text x="1630" y="1358" class="ent-label">payment_proofs</text>

  <line x1="1515" y1="1352" x2="1560" y2="1352" class="line-att" />
  <rect x="1440" y="1336" width="75" height="32" rx="16" ry="16" class="box-att" />
  <text x="1477" y="1357" class="att-pk">id</text>

  <line x1="1515" y1="1405" x2="1560" y2="1375" class="line-att" />
  <rect x="1440" y="1395" width="80" height="32" rx="16" ry="16" class="box-att" />
  <text x="1480" y="1416" class="att-label">file_path</text>

  <line x1="1585" y1="1425" x2="1610" y2="1375" class="line-att" />
  <rect x="1540" y="1425" width="90" height="32" rx="16" ry="16" class="box-att" />
  <text x="1585" y="1446" class="att-label">validated_at</text>

  <line x1="1690" y1="1425" x2="1660" y2="1375" class="line-att" />
  <rect x="1650" y="1425" width="105" height="32" rx="16" ry="16" class="box-att" />
  <text x="1702" y="1446" class="att-label">validation_status</text>

  <line x1="1745" y1="1385" x2="1700" y2="1370" class="line-att" />
  <rect x="1745" y="1375" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="1792" y="1396" class="att-label">rejection_note</text>


  <!-- ================= 10. ENTITY: daily_reconciliations ================= -->
  <rect x="240" y="1100" width="160" height="45" class="box-ent" />
  <text x="320" y="1128" class="ent-label">daily_reconciliations</text>

  <line x1="165" y1="1055" x2="240" y2="1100" class="line-att" />
  <rect x="90" y="1030" width="75" height="32" rx="16" ry="16" class="box-att" />
  <text x="127" y="1051" class="att-pk">id</text>

  <line x1="195" y1="1096" x2="240" y2="1115" class="line-att" />
  <rect x="80" y="1080" width="115" height="32" rx="16" ry="16" class="box-att" />
  <text x="137" y="1101" class="att-label">reconciliation_date</text>

  <line x1="195" y1="1146" x2="240" y2="1130" class="line-att" />
  <rect x="75" y="1130" width="120" height="32" rx="16" ry="16" class="box-att" />
  <text x="135" y="1151" class="att-label">system_cash_total</text>

  <line x1="195" y1="1196" x2="240" y2="1145" class="line-att" />
  <rect x="75" y="1180" width="120" height="32" rx="16" ry="16" class="box-att" />
  <text x="135" y="1201" class="att-label">system_transfer_tot</text>

  <line x1="220" y1="1230" x2="265" y2="1145" class="line-att" />
  <rect x="140" y="1230" width="115" height="32" rx="16" ry="16" class="box-att" />
  <text x="197" y="1251" class="att-label">physical_cash_amt</text>

  <line x1="332" y1="1230" x2="320" y2="1145" class="line-att" />
  <rect x="270" y="1230" width="125" height="32" rx="16" ry="16" class="box-att" />
  <text x="332" y="1251" class="att-label">discrepancy_amount</text>

  <line x1="445" y1="1230" x2="375" y2="1145" class="line-att" />
  <rect x="410" y="1230" width="115" height="32" rx="16" ry="16" class="box-att" />
  <text x="467" y="1251" class="att-label">discrepancy_note</text>

  <line x1="440" y1="1191" x2="400" y2="1138" class="line-att" />
  <rect x="440" y="1175" width="95" height="32" rx="16" ry="16" class="box-att" />
  <text x="487" y="1196" class="att-label">review_status</text>

  <line x1="440" y1="1136" x2="400" y2="1125" class="line-att" />
  <rect x="440" y="1120" width="85" height="32" rx="16" ry="16" class="box-att" />
  <text x="482" y="1141" class="att-label">is_locked</text>

  <line x1="440" y1="1081" x2="400" y2="1110" class="line-att" />
  <rect x="440" y="1065" width="85" height="32" rx="16" ry="16" class="box-att" />
  <text x="482" y="1086" class="att-label">locked_at</text>

  <line x1="440" y1="1035" x2="385" y2="1100" class="line-att" />
  <rect x="440" y="1010" width="105" height="32" rx="16" ry="16" class="box-att" />
  <text x="492" y="1031" class="att-label">report_pdf_path</text>


  <!-- ================= RELATIONSHIPS (DIAMONDS & LINES) ================= -->

  <!-- 1. branches -[1]- <Memiliki> -[N]- users -->
  <polygon points="320,420 370,445 320,470 270,445" class="box-rel" />
  <text x="320" y="449" class="rel-label">Memiliki</text>
  <line x1="465" y1="285" x2="320" y2="420" class="line-solid" />
  <text x="450" y="315" class="card-label">1</text>
  <line x1="320" y1="470" x2="230" y2="600" class="line-solid" />
  <text x="245" y="580" class="card-label">N</text>

  <!-- 2. branches -[1]- <Mengelola> -[N]- study_groups -->
  <polygon points="795,238 850,263 795,288 740,263" class="box-rel" />
  <text x="795" y="267" class="rel-label">Mengelola</text>
  <line x1="580" y1="263" x2="740" y2="263" class="line-solid" />
  <text x="600" y="255" class="card-label">1</text>
  <line x1="850" y1="263" x2="980" y2="263" class="line-solid" />
  <text x="955" y="255" class="card-label">N</text>

  <!-- 3. branches -[1]- <Menaungi> -[N]- students -->
  <polygon points="510,420 560,445 510,470 460,445" class="box-rel" />
  <text x="510" y="449" class="rel-label">Menaungi</text>
  <line x1="515" y1="285" x2="510" y2="420" class="line-solid" />
  <text x="522" y="315" class="card-label">1</text>
  <line x1="510" y1="470" x2="560" y2="600" class="line-solid" />
  <text x="540" y="585" class="card-label">N</text>

  <!-- 4. students -[1]- <Mengambil> -[N]- enrollments -->
  <polygon points="885,598 940,623 885,648 830,623" class="box-rel" />
  <text x="885" y="627" class="rel-label">Mengambil</text>
  <line x1="650" y1="623" x2="830" y2="623" class="line-solid" />
  <text x="670" y="615" class="card-label">1</text>
  <line x1="940" y1="623" x2="1050" y2="623" class="line-solid" />
  <text x="1025" y="615" class="card-label">N</text>

  <!-- 5. study_groups -[1]- <Ditempati> -[N]- enrollments -->
  <polygon points="1050,420 1100,445 1050,470 1000,445" class="box-rel" />
  <text x="1050" y="449" class="rel-label">Ditempati</text>
  <line x1="1050" y1="285" x2="1050" y2="420" class="line-solid" />
  <text x="1058" y="315" class="card-label">1</text>
  <line x1="1050" y1="470" x2="1090" y2="600" class="line-solid" />
  <text x="1070" y="585" class="card-label">N</text>

  <!-- 6. course_packages -[1]- <Ditawarkan> -[N]- enrollments -->
  <polygon points="1405,420 1460,445 1405,470 1350,445" class="box-rel" />
  <text x="1405" y="449" class="rel-label">Ditawarkan</text>
  <line x1="1630" y1="285" x2="1460" y2="445" class="line-solid" />
  <text x="1605" y="315" class="card-label">1</text>
  <line x1="1350" y1="445" x2="1150" y2="600" class="line-solid" />
  <text x="1170" y="585" class="card-label">N</text>

  <!-- 7. enrollments -[1]- <Menerbitkan> -[N]- tuition_bills -->
  <polygon points="1115,780 1175,805 1115,830 1055,805" class="box-rel" />
  <text x="1115" y="809" class="rel-label">Menerbitkan</text>
  <line x1="1115" y1="645" x2="1115" y2="780" class="line-solid" />
  <text x="1122" y="675" class="card-label">1</text>
  <line x1="1115" y1="830" x2="1115" y2="950" class="line-solid" />
  <text x="1122" y="930" class="card-label">N</text>

  <!-- 8. tuition_bills -[1]- <Diselesaikan> -[N]- payments -->
  <polygon points="1390,948 1450,973 1390,998 1330,973" class="box-rel" />
  <text x="1390" y="977" class="rel-label">Diselesaikan</text>
  <line x1="1180" y1="973" x2="1330" y2="973" class="line-solid" />
  <text x="1200" y="965" class="card-label">1</text>
  <line x1="1450" y1="973" x2="1560" y2="973" class="line-solid" />
  <text x="1535" y="965" class="card-label">N</text>

  <!-- 9. payments -[1]- <Melampirkan> -[1]- payment_proofs -->
  <polygon points="1625,1135 1685,1160 1625,1185 1565,1160" class="box-rel" />
  <text x="1625" y="1164" class="rel-label">Melampirkan</text>
  <line x1="1625" y1="995" x2="1625" y2="1135" class="line-solid" />
  <text x="1632" y="1025" class="card-label">1</text>
  <line x1="1625" y1="1185" x2="1625" y2="1330" class="line-solid" />
  <text x="1632" y="1310" class="card-label">1</text>

  <!-- 10. branches -[1]- <Mengadakan> -[N]- daily_reconciliations -->
  <polygon points="325,870 380,895 325,920 270,895" class="box-rel" />
  <text x="325" y="899" class="rel-label">Mengadakan</text>
  <path d="M 450 275 L 325 275 L 325 870" class="line-solid" />
  <text x="420" y="268" class="card-label">1</text>
  <line x1="325" y1="920" x2="320" y2="1100" class="line-solid" />
  <text x="328" y="1080" class="card-label">N</text>

  <!-- 11. users -[1]- <Melakukan> -[N]- daily_reconciliations -->
  <polygon points="220,870 270,895 220,920 170,895" class="box-rel" />
  <text x="220" y="899" class="rel-label">Melakukan</text>
  <line x1="220" y1="645" x2="220" y2="870" class="line-solid" />
  <text x="205" y="675" class="card-label">1</text>
  <line x1="220" y1="920" x2="270" y2="1100" class="line-solid" />
  <text x="278" y="1080" class="card-label">N</text>

  <!-- 12. users -[1]- <Melayani> -[N]- payments -->
  <polygon points="1380,830 1430,855 1380,880 1330,855" class="box-rel" />
  <text x="1380" y="859" class="rel-label">Melayani</text>
  <path d="M 280 622 L 320 622 L 320 855 L 1330 855" class="line-solid" />
  <text x="330" y="615" class="card-label">1</text>
  <line x1="1430" y1="855" x2="1560" y2="955" class="line-solid" />
  <text x="1530" y="935" class="card-label">N</text>

  <!-- 13. users -[1]- <Memvalidasi> -[N]- payment_proofs -->
  <polygon points="1385,1328 1440,1353 1385,1378 1330,1353" class="box-rel" />
  <text x="1385" y="1357" class="rel-label">Memvalidasi</text>
  <path d="M 190 645 L 190 1353 L 1330 1353" class="line-solid" />
  <text x="200" y="675" class="card-label">1</text>
  <line x1="1440" y1="1353" x2="1560" y2="1353" class="line-solid" />
  <text x="1535" y="1345" class="card-label">N</text>

  <!-- 14. branches -[1]- <Menerima> -[N]- payments -->
  <polygon points="1625,720 1675,745 1625,770 1575,745" class="box-rel" />
  <text x="1625" y="749" class="rel-label">Menerima</text>
  <path d="M 567 240 L 567 100 L 1625 100 L 1625 720" class="line-solid" />
  <text x="575" y="125" class="card-label">1</text>
  <line x1="1625" y1="770" x2="1625" y2="950" class="line-solid" />
  <text x="1632" y="930" class="card-label">N</text>

</svg>'''
    return svg

# -----------------------------------------------------------------------------
# 3. WRITE DRAW.IO AND SVG FILES
# -----------------------------------------------------------------------------
drawio_content = get_chen_drawio_xml()
svg_content = generate_chen_svg()

for d in output_dirs:
    drawio_path = os.path.join(d, 'Gambar_3_9_ERD_Chen_ARTHA.drawio')
    svg_path = os.path.join(d, 'Gambar_3_9_ERD_Chen_ARTHA.svg')
    
    with open(drawio_path, 'w', encoding='utf-8') as f:
        f.write(drawio_content)
    print(f"Generated Draw.io: {drawio_path}")

    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated SVG: {svg_path}")

# -----------------------------------------------------------------------------
# 4. RENDER HIGH-RES PNG USING PLAYWRIGHT
# -----------------------------------------------------------------------------
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
    page = browser.new_page(viewport={"width": 1920, "height": 1520}, device_scale_factor=2)
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

# -----------------------------------------------------------------------------
# 5. APPEND CHEN DIAGRAM AS NEW TAB IN ARTHA_Semua_Diagram_UML_Bab3.drawio
# -----------------------------------------------------------------------------
for d in output_dirs:
    master_p = os.path.join(d, 'ARTHA_Semua_Diagram_UML_Bab3.drawio')
    if os.path.exists(master_p):
        with open(master_p, 'r', encoding='utf-8') as f:
            mc = f.read()
        
        m = re.search(r'<diagram\s+[^>]*>(.*?)</diagram>', drawio_content, re.DOTALL)
        if m and 'diag_chen_3_9' not in mc:
            chen_page = f'  <diagram id="diag_chen_3_9" name="Gambar 3.9 ERD Chen ARTHA">\n    {m.group(1).strip()}\n  </diagram>'
            mc = mc.replace('</mxfile>', f'{chen_page}\n</mxfile>')
            with open(master_p, 'w', encoding='utf-8') as f:
                f.write(mc)
            print(f"Appended Chen tab to master drawio: {master_p}")

print("CHEN NOTATION ASSETS SUCCESSFULLY CREATED!")

