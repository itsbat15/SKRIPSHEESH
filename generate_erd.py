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
# 1. GENERATE DRAW.IO XML FOR ERD (Gambar 3.9)
# -----------------------------------------------------------------------------
def get_erd_drawio():
    xml = '''<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="diagram_erd" name="Gambar 3.9 ERD MySQL ARTHA">
    <mxGraphModel dx="1600" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1500" pageHeight="1000" background="#ffffff">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Block -->
        <mxCell id="title_box" value="&lt;b style=&quot;font-size: 16px;&quot;&gt;Entity Relationship Diagram (ERD) - Sistem Informasi ARTHA&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#555555&quot;&gt;Pemodelan Basis Data Relasional MySQL (Notasi Crow&#39;s Foot)&lt;/font&gt;" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="50" y="15" width="600" height="40" as="geometry" />
        </mxCell>

        <!-- Legend Block -->
        <mxCell id="legend_box" value="&lt;b&gt;Legenda Kelompok Entitas:&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#0288D1&quot;&gt;■&lt;/font&gt; Master Organisasi &amp;amp; Pengguna &amp;nbsp;&amp;nbsp; &lt;font color=&quot;#2E7D32&quot;&gt;■&lt;/font&gt; Akademik &amp;amp; Rombel &amp;nbsp;&amp;nbsp; &lt;font color=&quot;#E65100&quot;&gt;■&lt;/font&gt; Transaksi Keuangan &amp;amp; Rekonsiliasi" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8F9FA;strokeColor=#CFD8DC;align=center;fontSize=11;strokeWidth=1;" vertex="1" parent="1">
          <mxGeometry x="780" y="15" width="570" height="38" as="geometry" />
        </mxCell>

        <!-- ================= ENTITY TABLES ================= -->

        <!-- 1. branches -->
        <mxCell id="tbl_branches" value="&lt;b&gt;branches&lt;/b&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=28;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#E1F5FE;strokeColor=#0288D1;strokeWidth=1.5;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="50" y="80" width="270" height="152" as="geometry" />
        </mxCell>
        <mxCell id="b_row1" value="PK | id : INT(10)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontStyle=1;" vertex="1" parent="tbl_branches">
          <mxGeometry y="28" width="270" height="24" as="geometry" />
        </mxCell>
        <mxCell id="b_row2" value="UK | branch_code : VARCHAR(10)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_branches">
          <mxGeometry y="52" width="270" height="24" as="geometry" />
        </mxCell>
        <mxCell id="b_row3" value="   | branch_name : VARCHAR(100)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_branches">
          <mxGeometry y="76" width="270" height="24" as="geometry" />
        </mxCell>
        <mxCell id="b_row4" value="   | address : TEXT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_branches">
          <mxGeometry y="100" width="270" height="24" as="geometry" />
        </mxCell>
        <mxCell id="b_row5" value="   | phone : VARCHAR(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_branches">
          <mxGeometry y="124" width="270" height="24" as="geometry" />
        </mxCell>

        <!-- 2. users -->
        <mxCell id="tbl_users" value="&lt;b&gt;users&lt;/b&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=28;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#E1F5FE;strokeColor=#0288D1;strokeWidth=1.5;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="50" y="290" width="270" height="176" as="geometry" />
        </mxCell>
        <mxCell id="u_row1" value="PK | id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontStyle=1;" vertex="1" parent="tbl_users">
          <mxGeometry y="28" width="270" height="24" as="geometry" />
        </mxCell>
        <mxCell id="u_row2" value="FK | branch_id : INT(10) [NULL]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#0288D1;" vertex="1" parent="tbl_users">
          <mxGeometry y="52" width="270" height="24" as="geometry" />
        </mxCell>
        <mxCell id="u_row3" value="UK | email : VARCHAR(100)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_users">
          <mxGeometry y="76" width="270" height="24" as="geometry" />
        </mxCell>
        <mxCell id="u_row4" value="   | name : VARCHAR(100)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_users">
          <mxGeometry y="100" width="270" height="24" as="geometry" />
        </mxCell>
        <mxCell id="u_row5" value="   | password : VARCHAR(255)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_users">
          <mxGeometry y="124" width="270" height="24" as="geometry" />
        </mxCell>
        <mxCell id="u_row6" value="   | role : ENUM('super','branch')" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_users">
          <mxGeometry y="148" width="270" height="24" as="geometry" />
        </mxCell>

        <!-- 3. daily_reconciliations -->
        <mxCell id="tbl_daily_rec" value="&lt;b&gt;daily_reconciliations&lt;/b&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=28;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#FFF3E0;strokeColor=#E65100;strokeWidth=1.5;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="50" y="525" width="290" height="344" as="geometry" />
        </mxCell>
        <mxCell id="dr_row1" value="PK | id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontStyle=1;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="28" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row2" value="FK | branch_id : INT(10)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#0288D1;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="52" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row3" value="FK | user_id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#0288D1;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="76" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row4" value="   | reconciliation_date : DATE" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="100" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row5" value="   | system_cash_total : DECIMAL(12,2)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="124" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row6" value="   | system_transfer_total : DECIMAL" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="148" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row7" value="   | physical_cash_amount : DECIMAL" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="172" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row8" value="   | discrepancy_amount : DECIMAL" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="196" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row9" value="   | discrepancy_note : TEXT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="220" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row10" value="   | review_status : ENUM" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="244" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row11" value="   | is_locked : BOOLEAN" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="268" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row12" value="   | locked_at : TIMESTAMP" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="292" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="dr_row13" value="   | report_pdf_path : VARCHAR(255)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_daily_rec">
          <mxGeometry y="316" width="290" height="24" as="geometry" />
        </mxCell>

        <!-- 4. students -->
        <mxCell id="tbl_students" value="&lt;b&gt;students&lt;/b&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=28;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#E8F5E9;strokeColor=#2E7D32;strokeWidth=1.5;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="380" y="80" width="290" height="320" as="geometry" />
        </mxCell>
        <mxCell id="s_row1" value="PK | id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontStyle=1;" vertex="1" parent="tbl_students">
          <mxGeometry y="28" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="s_row2" value="FK | branch_id : INT(10)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#0288D1;" vertex="1" parent="tbl_students">
          <mxGeometry y="52" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="s_row3" value="UK | registration_no : VARCHAR(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_students">
          <mxGeometry y="76" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="s_row4" value="   | full_name : VARCHAR(150)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_students">
          <mxGeometry y="100" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="s_row5" value="   | birth_place : VARCHAR(50)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_students">
          <mxGeometry y="124" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="s_row6" value="   | birth_date : DATE" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_students">
          <mxGeometry y="148" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="s_row7" value="   | gender : ENUM('L','P')" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_students">
          <mxGeometry y="172" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="s_row8" value="   | school_origin : VARCHAR(100)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_students">
          <mxGeometry y="196" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="s_row9" value="   | grade_level : VARCHAR(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_students">
          <mxGeometry y="220" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="s_row10" value="   | home_address : TEXT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_students">
          <mxGeometry y="244" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="s_row11" value="   | parent_name : VARCHAR(100)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_students">
          <mxGeometry y="268" width="290" height="24" as="geometry" />
        </mxCell>
        <mxCell id="s_row12" value="   | parent_phone : VARCHAR(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_students">
          <mxGeometry y="292" width="290" height="24" as="geometry" />
        </mxCell>

        <!-- 5. study_groups -->
        <mxCell id="tbl_study_groups" value="&lt;b&gt;study_groups&lt;/b&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=28;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#E8F5E9;strokeColor=#2E7D32;strokeWidth=1.5;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="720" y="80" width="280" height="200" as="geometry" />
        </mxCell>
        <mxCell id="sg_row1" value="PK | id : INT(10)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontStyle=1;" vertex="1" parent="tbl_study_groups">
          <mxGeometry y="28" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="sg_row2" value="FK | branch_id : INT(10)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#0288D1;" vertex="1" parent="tbl_study_groups">
          <mxGeometry y="52" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="sg_row3" value="   | group_name : VARCHAR(50)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_study_groups">
          <mxGeometry y="76" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="sg_row4" value="   | schedule_day : VARCHAR(50)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_study_groups">
          <mxGeometry y="100" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="sg_row5" value="   | schedule_time : VARCHAR(30)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_study_groups">
          <mxGeometry y="124" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="sg_row6" value="   | max_capacity : INT(5)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_study_groups">
          <mxGeometry y="148" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="sg_row7" value="   | current_count : INT(5)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_study_groups">
          <mxGeometry y="172" width="280" height="24" as="geometry" />
        </mxCell>

        <!-- 6. course_packages -->
        <mxCell id="tbl_course_packages" value="&lt;b&gt;course_packages&lt;/b&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=28;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#E1F5FE;strokeColor=#0288D1;strokeWidth=1.5;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="1060" y="80" width="280" height="176" as="geometry" />
        </mxCell>
        <mxCell id="cp_row1" value="PK | id : INT(10)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontStyle=1;" vertex="1" parent="tbl_course_packages">
          <mxGeometry y="28" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="cp_row2" value="   | package_name : VARCHAR(100)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_course_packages">
          <mxGeometry y="52" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="cp_row3" value="   | grade_level : ENUM('SD','SMP','SMA')" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_course_packages">
          <mxGeometry y="76" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="cp_row4" value="   | monthly_fee : DECIMAL(12,2)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_course_packages">
          <mxGeometry y="100" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="cp_row5" value="   | description : TEXT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_course_packages">
          <mxGeometry y="124" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="cp_row6" value="   | is_active : BOOLEAN" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_course_packages">
          <mxGeometry y="148" width="280" height="24" as="geometry" />
        </mxCell>

        <!-- 7. enrollments -->
        <mxCell id="tbl_enrollments" value="&lt;b&gt;enrollments&lt;/b&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=28;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#E8F5E9;strokeColor=#2E7D32;strokeWidth=1.5;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="720" y="340" width="280" height="200" as="geometry" />
        </mxCell>
        <mxCell id="en_row1" value="PK | id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontStyle=1;" vertex="1" parent="tbl_enrollments">
          <mxGeometry y="28" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="en_row2" value="FK | student_id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#2E7D32;" vertex="1" parent="tbl_enrollments">
          <mxGeometry y="52" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="en_row3" value="FK | study_group_id : INT(10)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#2E7D32;" vertex="1" parent="tbl_enrollments">
          <mxGeometry y="76" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="en_row4" value="FK | course_package_id : INT(10)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#0288D1;" vertex="1" parent="tbl_enrollments">
          <mxGeometry y="100" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="en_row5" value="   | registration_date : DATE" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_enrollments">
          <mxGeometry y="124" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="en_row6" value="   | due_day : INT(2)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_enrollments">
          <mxGeometry y="148" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="en_row7" value="   | status : ENUM('active','grad','drop')" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_enrollments">
          <mxGeometry y="172" width="280" height="24" as="geometry" />
        </mxCell>

        <!-- 8. tuition_bills -->
        <mxCell id="tbl_tuition_bills" value="&lt;b&gt;tuition_bills&lt;/b&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=28;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#FFF3E0;strokeColor=#E65100;strokeWidth=1.5;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="720" y="595" width="280" height="176" as="geometry" />
        </mxCell>
        <mxCell id="tb_row1" value="PK | id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontStyle=1;" vertex="1" parent="tbl_tuition_bills">
          <mxGeometry y="28" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="tb_row2" value="FK | enrollment_id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#2E7D32;" vertex="1" parent="tbl_tuition_bills">
          <mxGeometry y="52" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="tb_row3" value="   | bill_period : VARCHAR(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_tuition_bills">
          <mxGeometry y="76" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="tb_row4" value="   | amount : DECIMAL(12,2)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_tuition_bills">
          <mxGeometry y="100" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="tb_row5" value="   | due_date : DATE" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_tuition_bills">
          <mxGeometry y="124" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="tb_row6" value="   | payment_status : ENUM" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_tuition_bills">
          <mxGeometry y="148" width="280" height="24" as="geometry" />
        </mxCell>

        <!-- 9. payments -->
        <mxCell id="tbl_payments" value="&lt;b&gt;payments&lt;/b&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=28;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#FFF3E0;strokeColor=#E65100;strokeWidth=1.5;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="1060" y="320" width="280" height="224" as="geometry" />
        </mxCell>
        <mxCell id="p_row1" value="PK | id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontStyle=1;" vertex="1" parent="tbl_payments">
          <mxGeometry y="28" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="p_row2" value="FK | tuition_bill_id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#E65100;" vertex="1" parent="tbl_payments">
          <mxGeometry y="52" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="p_row3" value="FK | branch_id : INT(10)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#0288D1;" vertex="1" parent="tbl_payments">
          <mxGeometry y="76" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="p_row4" value="FK | user_id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#0288D1;" vertex="1" parent="tbl_payments">
          <mxGeometry y="100" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="p_row5" value="UK | receipt_number : VARCHAR(50)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_payments">
          <mxGeometry y="124" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="p_row6" value="   | payment_method : ENUM" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_payments">
          <mxGeometry y="148" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="p_row7" value="   | amount_paid : DECIMAL(12,2)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_payments">
          <mxGeometry y="172" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="p_row8" value="   | payment_date : TIMESTAMP" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_payments">
          <mxGeometry y="196" width="280" height="24" as="geometry" />
        </mxCell>

        <!-- 10. payment_proofs -->
        <mxCell id="tbl_payment_proofs" value="&lt;b&gt;payment_proofs&lt;/b&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=28;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#FFF3E0;strokeColor=#E65100;strokeWidth=1.5;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="1060" y="605" width="280" height="200" as="geometry" />
        </mxCell>
        <mxCell id="pp_row1" value="PK | id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontStyle=1;" vertex="1" parent="tbl_payment_proofs">
          <mxGeometry y="28" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="pp_row2" value="FK | payment_id : BIGINT(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#E65100;" vertex="1" parent="tbl_payment_proofs">
          <mxGeometry y="52" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="pp_row3" value="FK | validated_by : BIGINT [NULL]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;fontColor=#0288D1;" vertex="1" parent="tbl_payment_proofs">
          <mxGeometry y="76" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="pp_row4" value="   | file_path : VARCHAR(255)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_payment_proofs">
          <mxGeometry y="100" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="pp_row5" value="   | validated_at : TIMESTAMP" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_payment_proofs">
          <mxGeometry y="124" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="pp_row6" value="   | validation_status : ENUM" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_payment_proofs">
          <mxGeometry y="148" width="280" height="24" as="geometry" />
        </mxCell>
        <mxCell id="pp_row7" value="   | rejection_note : TEXT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=11;" vertex="1" parent="tbl_payment_proofs">
          <mxGeometry y="172" width="280" height="24" as="geometry" />
        </mxCell>

        <!-- ================= RELATIONSHIP CONNECTORS (CROW'S FOOT) ================= -->
        <!-- 1. branches -> users (1:M) -->
        <mxCell id="rel_br_usr" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#0288D1;strokeWidth=1.5;exitX=0.35;exitY=1;exitDx=0;exitDy=0;entryX=0.35;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_branches" target="tbl_users">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 2. branches -> students (1:M) -->
        <mxCell id="rel_br_stu" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#0288D1;strokeWidth=1.5;exitX=1;exitY=0.3;exitDx=0;exitDy=0;entryX=0;entryY=0.15;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_branches" target="tbl_students">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 3. branches -> study_groups (1:M) -->
        <mxCell id="rel_br_sg" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#0288D1;strokeWidth=1.5;exitX=0.75;exitY=0;exitDx=0;exitDy=0;entryX=0.25;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_branches" target="tbl_study_groups">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="253" y="62" />
              <mxPoint x="790" y="62" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 4. branches -> payments (1:M) -->
        <mxCell id="rel_br_pay" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#0288D1;strokeWidth=1.5;exitX=0.9;exitY=0;exitDx=0;exitDy=0;entryX=0.65;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_branches" target="tbl_payments">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="293" y="52" />
              <mxPoint x="1242" y="52" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 5. branches -> daily_reconciliations (1:M) -->
        <mxCell id="rel_br_dr" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#0288D1;strokeWidth=1.5;exitX=0;exitY=0.7;exitDx=0;exitDy=0;entryX=0;entryY=0.15;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_branches" target="tbl_daily_rec">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="25" y="186" />
              <mxPoint x="25" y="577" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 6. users -> daily_reconciliations (1:M) -->
        <mxCell id="rel_usr_dr" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#0288D1;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_users" target="tbl_daily_rec">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 7. users -> payments (1:M) -->
        <mxCell id="rel_usr_pay" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#0288D1;strokeWidth=1.5;exitX=1;exitY=0.65;exitDx=0;exitDy=0;entryX=0;entryY=0.65;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_users" target="tbl_payments">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="350" y="404" />
              <mxPoint x="350" y="470" />
              <mxPoint x="695" y="470" />
              <mxPoint x="695" y="466" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 8. users -> payment_proofs (validated_by, 1:M optional) -->
        <mxCell id="rel_usr_pp" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#0288D1;strokeWidth=1.5;exitX=0.85;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_users" target="tbl_payment_proofs">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="280" y="485" />
              <mxPoint x="350" y="485" />
              <mxPoint x="350" y="810" />
              <mxPoint x="1035" y="810" />
              <mxPoint x="1035" y="705" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 9. students -> enrollments (1:M) -->
        <mxCell id="rel_stu_en" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#2E7D32;strokeWidth=1.5;exitX=1;exitY=0.85;exitDx=0;exitDy=0;entryX=0;entryY=0.2;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_students" target="tbl_enrollments">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 10. study_groups -> enrollments (1:M) -->
        <mxCell id="rel_sg_en" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#2E7D32;strokeWidth=1.5;exitX=0.45;exitY=1;exitDx=0;exitDy=0;entryX=0.45;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_study_groups" target="tbl_enrollments">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 11. course_packages -> enrollments (1:M) -->
        <mxCell id="rel_cp_en" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#0288D1;strokeWidth=1.5;exitX=0;exitY=0.65;exitDx=0;exitDy=0;entryX=1;entryY=0.35;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_course_packages" target="tbl_enrollments">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1035" y="194" />
              <mxPoint x="1035" y="410" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 12. enrollments -> tuition_bills (1:M) -->
        <mxCell id="rel_en_tb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#2E7D32;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_enrollments" target="tbl_tuition_bills">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 13. tuition_bills -> payments (1:M) -->
        <mxCell id="rel_tb_pay" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmany;strokeColor=#E65100;strokeWidth=1.5;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.35;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_tuition_bills" target="tbl_payments">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1035" y="657" />
              <mxPoint x="1035" y="398" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 14. payments -> payment_proofs (1:1) -->
        <mxCell id="rel_pay_pp" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;endArrow=ERmandOne;strokeColor=#E65100;strokeWidth=1.5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="tbl_payments" target="tbl_payment_proofs">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml

# -----------------------------------------------------------------------------
# 2. GENERATE ULTRA-CRISP SVG FOR ACADEMIC PUBLICATION (Gambar 3.9)
# -----------------------------------------------------------------------------
def generate_erd_svg():
    width = 1420
    height = 920

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      .diagram-title {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; fill: #1A237E; }}
      .diagram-sub {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; fill: #555555; }}
      .legend-text {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #333333; }}
      .tbl-header {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; font-weight: bold; fill: #ffffff; text-anchor: middle; }}
      .col-key {{ font-family: 'Consolas', monospace; font-size: 10.5px; font-weight: bold; fill: #C62828; }}
      .col-fk {{ font-family: 'Consolas', monospace; font-size: 10.5px; font-weight: bold; fill: #1565C0; }}
      .col-name {{ font-family: 'Consolas', monospace; font-size: 11px; font-weight: 600; fill: #212121; }}
      .col-type {{ font-family: 'Consolas', monospace; font-size: 10.5px; fill: #616161; text-anchor: end; }}
      .crow-line {{ fill: none; stroke-width: 1.6; }}
      .crow-blue {{ stroke: #0288D1; }}
      .crow-green {{ stroke: #2E7D32; }}
      .crow-orange {{ stroke: #E65100; }}
    </style>

    <!-- Crow's Foot Markers -->
    <!-- Mandatory One (||) -->
    <marker id="one-blue" viewBox="0 0 16 16" refX="1" refY="8" markerWidth="10" markerHeight="10" orient="auto">
      <line x1="6" y1="2" x2="6" y2="14" stroke="#0288D1" stroke-width="2" />
      <line x1="12" y1="2" x2="12" y2="14" stroke="#0288D1" stroke-width="2" />
    </marker>
    <marker id="one-green" viewBox="0 0 16 16" refX="1" refY="8" markerWidth="10" markerHeight="10" orient="auto">
      <line x1="6" y1="2" x2="6" y2="14" stroke="#2E7D32" stroke-width="2" />
      <line x1="12" y1="2" x2="12" y2="14" stroke="#2E7D32" stroke-width="2" />
    </marker>
    <marker id="one-orange" viewBox="0 0 16 16" refX="1" refY="8" markerWidth="10" markerHeight="10" orient="auto">
      <line x1="6" y1="2" x2="6" y2="14" stroke="#E65100" stroke-width="2" />
      <line x1="12" y1="2" x2="12" y2="14" stroke="#E65100" stroke-width="2" />
    </marker>

    <!-- Many / Crow's Foot (>|) -->
    <marker id="many-blue" viewBox="0 0 16 16" refX="15" refY="8" markerWidth="10" markerHeight="10" orient="auto">
      <path d="M 0 2 L 14 8 L 0 14 M 14 2 L 14 14" fill="none" stroke="#0288D1" stroke-width="1.8" />
    </marker>
    <marker id="many-green" viewBox="0 0 16 16" refX="15" refY="8" markerWidth="10" markerHeight="10" orient="auto">
      <path d="M 0 2 L 14 8 L 0 14 M 14 2 L 14 14" fill="none" stroke="#2E7D32" stroke-width="1.8" />
    </marker>
    <marker id="many-orange" viewBox="0 0 16 16" refX="15" refY="8" markerWidth="10" markerHeight="10" orient="auto">
      <path d="M 0 2 L 14 8 L 0 14 M 14 2 L 14 14" fill="none" stroke="#E65100" stroke-width="1.8" />
    </marker>
  </defs>

  <!-- Background -->
  <rect width="{width}" height="{height}" fill="#FAFAFA" />

  <!-- Title & Legend -->
  <text x="45" y="32" class="diagram-title">Entity Relationship Diagram (ERD) - Sistem Informasi ARTHA</text>
  <text x="45" y="50" class="diagram-sub">Pemodelan Basis Data Relasional MySQL Menggunakan Notasi Crow's Foot</text>

  <!-- Legend Box -->
  <g transform="translate(740, 16)">
    <rect width="630" height="36" rx="5" ry="5" fill="#ffffff" stroke="#D1D5DB" stroke-width="1.2" />
    <rect x="15" y="11" width="14" height="14" rx="2" fill="#0288D1" />
    <text x="36" y="23" class="legend-text" font-weight="600">Master &amp; Pengguna</text>
    
    <rect x="175" y="11" width="14" height="14" rx="2" fill="#2E7D32" />
    <text x="196" y="23" class="legend-text" font-weight="600">Akademik &amp; Rombel</text>

    <rect x="345" y="11" width="14" height="14" rx="2" fill="#E65100" />
    <text x="366" y="23" class="legend-text" font-weight="600">Keuangan &amp; Kas Harian</text>

    <text x="530" y="23" class="legend-text" font-style="italic">PK = Primary, FK = Foreign</text>
  </g>

  <!-- ================= ENTITY TABLE HELPER FUNCTION IN SVG ================= -->
'''

    # Function to render an entity table in SVG
    def render_table(x, y, w, header_title, header_color, bg_color, border_color, rows):
        row_height = 22
        h = 28 + len(rows) * row_height
        res = f'''
  <!-- Table: {header_title} -->
  <g transform="translate({x}, {y})">
    <rect width="{w}" height="{h}" rx="4" ry="4" fill="{bg_color}" stroke="{border_color}" stroke-width="1.6" filter="drop-shadow(0px 2px 3px rgba(0,0,0,0.06))" />
    <path d="M 0 4 Q 0 0 4 0 L {w-4} 0 Q {w} 0 {w} 4 L {w} 28 L 0 28 Z" fill="{header_color}" />
    <text x="{w/2}" y="19" class="tbl-header">{header_title}</text>
'''
        for idx, (key_label, col_name, col_type) in enumerate(rows):
            ry = 28 + idx * row_height
            bg_alt = '#F8FAFC' if idx % 2 == 1 else '#FFFFFF'
            res += f'    <rect x="1" y="{ry}" width="{w-2}" height="{row_height}" fill="{bg_alt}" />\n'
            res += f'    <line x1="1" y1="{ry}" x2="{w-1}" y2="{ry}" stroke="#EEEEEE" stroke-width="1" />\n'
            
            # Key styling
            if key_label == 'PK':
                res += f'    <text x="8" y="{ry+15}" class="col-key">PK</text>\n'
            elif key_label == 'FK':
                res += f'    <text x="8" y="{ry+15}" class="col-fk">FK</text>\n'
            elif key_label == 'UK':
                res += f'    <text x="8" y="{ry+15}" class="col-key" fill="#7B1FA2">UK</text>\n'
            
            res += f'    <text x="34" y="{ry+15}" class="col-name">{col_name}</text>\n'
            res += f'    <text x="{w-10}" y="{ry+15}" class="col-type">{col_type}</text>\n'

        res += '  </g>\n'
        return res

    # Table 1: branches
    svg += render_table(45, 80, 275, 'branches', '#0288D1', '#FFFFFF', '#0288D1', [
        ('PK', 'id', 'INT(10)'),
        ('UK', 'branch_code', 'VARCHAR(10)'),
        ('', 'branch_name', 'VARCHAR(100)'),
        ('', 'address', 'TEXT'),
        ('', 'phone', 'VARCHAR(20)')
    ])

    # Table 2: users
    svg += render_table(45, 280, 275, 'users', '#0288D1', '#FFFFFF', '#0288D1', [
        ('PK', 'id', 'BIGINT(20)'),
        ('FK', 'branch_id', 'INT(10) [NULL]'),
        ('UK', 'email', 'VARCHAR(100)'),
        ('', 'name', 'VARCHAR(100)'),
        ('', 'password', 'VARCHAR(255)'),
        ('', 'role', 'ENUM(2)')
    ])

    # Table 3: daily_reconciliations
    svg += render_table(45, 510, 295, 'daily_reconciliations', '#E65100', '#FFFFFF', '#E65100', [
        ('PK', 'id', 'BIGINT(20)'),
        ('FK', 'branch_id', 'INT(10)'),
        ('FK', 'user_id', 'BIGINT(20)'),
        ('', 'reconciliation_date', 'DATE'),
        ('', 'system_cash_total', 'DECIMAL(12,2)'),
        ('', 'system_transfer_tot', 'DECIMAL(12,2)'),
        ('', 'physical_cash_amount', 'DECIMAL(12,2)'),
        ('', 'discrepancy_amount', 'DECIMAL(12,2)'),
        ('', 'discrepancy_note', 'TEXT'),
        ('', 'review_status', 'ENUM(3)'),
        ('', 'is_locked', 'BOOLEAN'),
        ('', 'locked_at', 'TIMESTAMP'),
        ('', 'report_pdf_path', 'VARCHAR(255)')
    ])

    # Table 4: students
    svg += render_table(380, 80, 295, 'students', '#2E7D32', '#FFFFFF', '#2E7D32', [
        ('PK', 'id', 'BIGINT(20)'),
        ('FK', 'branch_id', 'INT(10)'),
        ('UK', 'registration_no', 'VARCHAR(20)'),
        ('', 'full_name', 'VARCHAR(150)'),
        ('', 'birth_place', 'VARCHAR(50)'),
        ('', 'birth_date', 'DATE'),
        ('', 'gender', 'ENUM(L/P)'),
        ('', 'school_origin', 'VARCHAR(100)'),
        ('', 'grade_level', 'VARCHAR(20)'),
        ('', 'home_address', 'TEXT'),
        ('', 'parent_name', 'VARCHAR(100)'),
        ('', 'parent_phone', 'VARCHAR(20)')
    ])

    # Table 5: study_groups
    svg += render_table(730, 80, 280, 'study_groups', '#2E7D32', '#FFFFFF', '#2E7D32', [
        ('PK', 'id', 'INT(10)'),
        ('FK', 'branch_id', 'INT(10)'),
        ('', 'group_name', 'VARCHAR(50)'),
        ('', 'schedule_day', 'VARCHAR(50)'),
        ('', 'schedule_time', 'VARCHAR(30)'),
        ('', 'max_capacity', 'INT(5)'),
        ('', 'current_count', 'INT(5)')
    ])

    # Table 6: course_packages
    svg += render_table(1070, 80, 280, 'course_packages', '#0288D1', '#FFFFFF', '#0288D1', [
        ('PK', 'id', 'INT(10)'),
        ('', 'package_name', 'VARCHAR(100)'),
        ('', 'grade_level', 'ENUM(SD/SMP/SMA)'),
        ('', 'monthly_fee', 'DECIMAL(12,2)'),
        ('', 'description', 'TEXT'),
        ('', 'is_active', 'BOOLEAN')
    ])

    # Table 7: enrollments
    svg += render_table(730, 340, 280, 'enrollments', '#2E7D32', '#FFFFFF', '#2E7D32', [
        ('PK', 'id', 'BIGINT(20)'),
        ('FK', 'student_id', 'BIGINT(20)'),
        ('FK', 'study_group_id', 'INT(10)'),
        ('FK', 'course_package_id', 'INT(10)'),
        ('', 'registration_date', 'DATE'),
        ('', 'due_day', 'INT(2)'),
        ('', 'status', 'ENUM(3)')
    ])

    # Table 8: tuition_bills
    svg += render_table(730, 585, 280, 'tuition_bills', '#E65100', '#FFFFFF', '#E65100', [
        ('PK', 'id', 'BIGINT(20)'),
        ('FK', 'enrollment_id', 'BIGINT(20)'),
        ('', 'bill_period', 'VARCHAR(20)'),
        ('', 'amount', 'DECIMAL(12,2)'),
        ('', 'due_date', 'DATE'),
        ('', 'payment_status', 'ENUM(3)')
    ])

    # Table 9: payments
    svg += render_table(1070, 315, 280, 'payments', '#E65100', '#FFFFFF', '#E65100', [
        ('PK', 'id', 'BIGINT(20)'),
        ('FK', 'tuition_bill_id', 'BIGINT(20)'),
        ('FK', 'branch_id', 'INT(10)'),
        ('FK', 'user_id', 'BIGINT(20)'),
        ('UK', 'receipt_number', 'VARCHAR(50)'),
        ('', 'payment_method', 'ENUM(3)'),
        ('', 'amount_paid', 'DECIMAL(12,2)'),
        ('', 'payment_date', 'TIMESTAMP')
    ])

    # Table 10: payment_proofs
    svg += render_table(1070, 585, 280, 'payment_proofs', '#E65100', '#FFFFFF', '#E65100', [
        ('PK', 'id', 'BIGINT(20)'),
        ('FK', 'payment_id', 'BIGINT(20)'),
        ('FK', 'validated_by', 'BIGINT [NULL]'),
        ('', 'file_path', 'VARCHAR(255)'),
        ('', 'validated_at', 'TIMESTAMP'),
        ('', 'validation_status', 'ENUM(3)'),
        ('', 'rejection_note', 'TEXT')
    ])

    # ================= RELATIONSHIP CONNECTORS (CROW'S FOOT SVG PATHS) =================
    svg += '''
  <!-- ================= RELATIONSHIP PATHS ================= -->
  <!-- 1. branches (1) -> users (M) -->
  <path d="M 140 218 L 140 280" class="crow-line crow-blue" marker-start="url(#one-blue)" marker-end="url(#many-blue)" />

  <!-- 2. branches (1) -> students (M) -->
  <path d="M 320 120 L 380 120" class="crow-line crow-blue" marker-start="url(#one-blue)" marker-end="url(#many-blue)" />

  <!-- 3. branches (1) -> study_groups (M) -->
  <path d="M 230 80 L 230 60 L 780 60 L 780 80" class="crow-line crow-blue" marker-start="url(#one-blue)" marker-end="url(#many-blue)" />

  <!-- 4. branches (1) -> payments (M) -->
  <path d="M 270 80 L 270 50 L 1280 50 L 1280 315" class="crow-line crow-blue" marker-start="url(#one-blue)" marker-end="url(#many-blue)" />

  <!-- 5. branches (1) -> daily_reconciliations (M) -->
  <path d="M 45 160 L 22 160 L 22 555 L 45 555" class="crow-line crow-blue" marker-start="url(#one-blue)" marker-end="url(#many-blue)" />

  <!-- 6. users (1) -> daily_reconciliations (M) -->
  <path d="M 180 440 L 180 510" class="crow-line crow-blue" marker-start="url(#one-blue)" marker-end="url(#many-blue)" />

  <!-- 7. users (1) -> payments (M) -->
  <path d="M 320 395 L 350 395 L 350 480 L 700 480 L 700 410 L 1070 410" class="crow-line crow-blue" marker-start="url(#one-blue)" marker-end="url(#many-blue)" />

  <!-- 8. users (1) -> payment_proofs (validated_by, M optional) -->
  <path d="M 280 440 L 280 495 L 360 495 L 360 835 L 1040 835 L 1040 655 L 1070 655" class="crow-line crow-blue" marker-start="url(#one-blue)" marker-end="url(#many-blue)" />

  <!-- 9. students (1) -> enrollments (M) -->
  <path d="M 675 365 L 730 365" class="crow-line crow-green" marker-start="url(#one-green)" marker-end="url(#many-green)" />

  <!-- 10. study_groups (1) -> enrollments (M) -->
  <path d="M 820 262 L 820 340" class="crow-line crow-green" marker-start="url(#one-green)" marker-end="url(#many-green)" />

  <!-- 11. course_packages (1) -> enrollments (M) -->
  <path d="M 1070 190 L 1040 190 L 1040 380 L 1010 380" class="crow-line crow-blue" marker-start="url(#one-blue)" marker-end="url(#many-blue)" />

  <!-- 12. enrollments (1) -> tuition_bills (M) -->
  <path d="M 870 522 L 870 585" class="crow-line crow-green" marker-start="url(#one-green)" marker-end="url(#many-green)" />

  <!-- 13. tuition_bills (1) -> payments (M) -->
  <path d="M 1010 635 L 1040 635 L 1040 360 L 1070 360" class="crow-line crow-orange" marker-start="url(#one-orange)" marker-end="url(#many-orange)" />

  <!-- 14. payments (1) -> payment_proofs (1:1) -->
  <path d="M 1210 519 L 1210 585" class="crow-line crow-orange" marker-start="url(#one-orange)" marker-end="url(#one-orange)" />

</svg>'''
    return svg

# -----------------------------------------------------------------------------
# 3. WRITE DRAW.IO AND SVG FILES TO ALL ASSET DIRS
# -----------------------------------------------------------------------------
drawio_content = get_erd_drawio()
svg_content = generate_erd_svg()

for d in output_dirs:
    drawio_path = os.path.join(d, 'Gambar_3_9_ERD_MySQL_ARTHA.drawio')
    svg_path = os.path.join(d, 'Gambar_3_9_ERD_MySQL_ARTHA.svg')
    
    with open(drawio_path, 'w', encoding='utf-8') as f:
        f.write(drawio_content)
    print(f"Generated Draw.io: {drawio_path}")

    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated SVG: {svg_path}")

# -----------------------------------------------------------------------------
# 4. RENDER HIGH-RES PNG USING PLAYWRIGHT (2x SCALE FACTOR)
# -----------------------------------------------------------------------------
primary_svg = os.path.join(output_dirs[0], 'Gambar_3_9_ERD_MySQL_ARTHA.svg')
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
    page = browser.new_page(viewport={"width": 1420, "height": 920}, device_scale_factor=2)
    page.set_content(html_content)

    for out_d in output_dirs:
        png_path = os.path.join(out_d, 'Gambar_3_9_ERD_MySQL_ARTHA.png')
        page.screenshot(path=png_path)
        print(f"Rendered PNG: {png_path}")

    # Also save to artifact directory
    artifact_png = r'C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\Gambar_3_9_ERD_MySQL_ARTHA.png'
    page.screenshot(path=artifact_png)
    print(f"Rendered Artifact PNG: {artifact_png}")

    page.close()
    browser.close()

print("ALL ERD ASSETS (DRAWIO, SVG, PNG) SUCCESSFULLY CREATED AND RENDERED!")

