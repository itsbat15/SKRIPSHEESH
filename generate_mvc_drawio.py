from pathlib import Path

ROOT = Path("c:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA")
OUT1 = ROOT / "ASET BAB 2.1/Gambar_2_5_Arsitektur_MVC.drawio"
OUT2 = ROOT / "DRAFT PROPOSAL MD/BAB 2/ASET BAB 2.1/Gambar_2_5_Arsitektur_MVC.drawio"

drawio_xml = '''<mxfile host="app.diagrams.net" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="diagram_mvc" name="Gambar 2.5 Pola Arsitektur MVC Sommerville 2011">
    <mxGraphModel dx="1200" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1000" pageHeight="720" background="#ffffff">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Top Right Title Badge -->
        <mxCell id="badge_mvc" value="MVC" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=28;fontStyle=1;fontColor=#0F172A;fontFamily=Segoe UI, Arial;" vertex="1" parent="1">
          <mxGeometry x="870" y="30" width="80" height="40" as="geometry" />
        </mxCell>

        <!-- User / Pengguna -->
        <mxCell id="user_box" value="&lt;b&gt;User / Pengguna&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=15;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.8;fontSize=14;fontColor=#0F172A;fontFamily=Segoe UI, Arial;" vertex="1" parent="1">
          <mxGeometry x="710" y="25" width="160" height="46" as="geometry" />
        </mxCell>

        <!-- Controller Card -->
        <mxCell id="card_controller" value="" style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#FFFFFF;strokeColor=#334155;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="70" y="135" width="350" height="185" as="geometry" />
        </mxCell>
        <mxCell id="header_controller" value="&lt;b&gt;Controller&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#F1F5F9;strokeColor=#475569;strokeWidth=1.5;fontSize=17;fontColor=#0F172A;fontFamily=Segoe UI, Arial;" vertex="1" parent="1">
          <mxGeometry x="85" y="150" width="320" height="46" as="geometry" />
        </mxCell>
        <mxCell id="desc_controller" value="&lt;div align=&quot;left&quot;&gt;&amp;bull; Maps User Actions to Model Updates&lt;br&gt;&amp;bull; Selects and Directs View&lt;br&gt;&lt;i style=&quot;color:#64748B;&quot;&gt;(Logika Pengendali &amp;amp; Alur Sistem)&lt;/i&gt;&lt;/div&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=13;fontColor=#334155;fontFamily=Segoe UI, Arial;" vertex="1" parent="1">
          <mxGeometry x="105" y="210" width="290" height="90" as="geometry" />
        </mxCell>

        <!-- View Card -->
        <mxCell id="card_view" value="" style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#FFFFFF;strokeColor=#334155;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="580" y="135" width="350" height="185" as="geometry" />
        </mxCell>
        <mxCell id="header_view" value="&lt;b&gt;View&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#F1F5F9;strokeColor=#475569;strokeWidth=1.5;fontSize=17;fontColor=#0F172A;fontFamily=Segoe UI, Arial;" vertex="1" parent="1">
          <mxGeometry x="595" y="150" width="320" height="46" as="geometry" />
        </mxCell>
        <mxCell id="desc_view" value="&lt;div align=&quot;left&quot;&gt;&amp;bull; Renders Model Data&lt;br&gt;&amp;bull; Sends User Events to Controller&lt;br&gt;&lt;i style=&quot;color:#64748B;&quot;&gt;(Tampilan Antarmuka &amp;amp; Presentasi)&lt;/i&gt;&lt;/div&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=13;fontColor=#334155;fontFamily=Segoe UI, Arial;" vertex="1" parent="1">
          <mxGeometry x="615" y="210" width="290" height="90" as="geometry" />
        </mxCell>

        <!-- Model Card -->
        <mxCell id="card_model" value="" style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#FFFFFF;strokeColor=#334155;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="325" y="420" width="350" height="185" as="geometry" />
        </mxCell>
        <mxCell id="header_model" value="&lt;b&gt;Model&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#F1F5F9;strokeColor=#475569;strokeWidth=1.5;fontSize=17;fontColor=#0F172A;fontFamily=Segoe UI, Arial;" vertex="1" parent="1">
          <mxGeometry x="340" y="435" width="320" height="46" as="geometry" />
        </mxCell>
        <mxCell id="desc_model" value="&lt;div align=&quot;left&quot;&gt;&amp;bull; Encapsulates Application State&lt;br&gt;&amp;bull; Notifies View of State Changes&lt;br&gt;&lt;i style=&quot;color:#64748B;&quot;&gt;(Struktur Data &amp;amp; Operasi Basis Data)&lt;/i&gt;&lt;/div&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=13;fontColor=#334155;fontFamily=Segoe UI, Arial;" vertex="1" parent="1">
          <mxGeometry x="355" y="495" width="290" height="90" as="geometry" />
        </mxCell>

        <!-- Arrows -->
        <!-- User -> View -->
        <mxCell id="edge_user_view" value="User Events" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1E293B;strokeWidth=2;fontSize=11;fontColor=#334155;fontStyle=1;labelBackgroundColor=#F1F5F9;" edge="1" parent="1" source="user_box" target="card_view">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Controller -> View -->
        <mxCell id="edge_ctrl_view" value="Selects View" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1E293B;strokeWidth=2;fontSize=11;fontColor=#1E293B;fontStyle=1;labelBackgroundColor=#F8FAFC;" edge="1" parent="1">
          <mxGeometry x="0.1" y="-10" relative="1" as="geometry">
            <mxPoint x="420" y="185" as="sourcePoint" />
            <mxPoint x="580" y="185" as="targetPoint" />
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>

        <!-- View -> Controller -->
        <mxCell id="edge_view_ctrl" value="Sends User Events" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1E293B;strokeWidth=2;fontSize=11;fontColor=#1E293B;fontStyle=1;labelBackgroundColor=#F8FAFC;" edge="1" parent="1">
          <mxGeometry x="-0.1" y="10" relative="1" as="geometry">
            <mxPoint x="580" y="245" as="sourcePoint" />
            <mxPoint x="420" y="245" as="targetPoint" />
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>

        <!-- Controller -> Model -->
        <mxCell id="edge_ctrl_model" value="Maps User Actions to Model Updates" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1E293B;strokeWidth=2;fontSize=11;fontColor=#0F172A;fontStyle=1;labelBackgroundColor=#F8FAFC;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="245" y="320" as="sourcePoint" />
            <mxPoint x="325" y="490" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- Model -> View -->
        <mxCell id="edge_model_view" value="Change Notification (Notifies State Change)" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1E293B;strokeWidth=2;fontSize=11;fontColor=#0F172A;fontStyle=1;labelBackgroundColor=#F8FAFC;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="675" y="490" as="sourcePoint" />
            <mxPoint x="755" y="320" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- View -> Model (State Query) -->
        <mxCell id="edge_view_model_query" value="State Query / Renders" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#64748B;strokeWidth=1.8;dashed=1;fontSize=11;fontColor=#475569;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="620" y="320" as="sourcePoint" />
            <mxPoint x="530" y="420" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- Captions -->
        <mxCell id="caption_1" value="Fig. 6.3. The organization of the Model-View-Controller (MVC) pattern." style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1;fontColor=#0F172A;fontFamily=Segoe UI, Arial;" vertex="1" parent="1">
          <mxGeometry x="250" y="640" width="500" height="20" as="geometry" />
        </mxCell>
        <mxCell id="caption_2" value="Sumber: Diadaptasi dan digambar ulang dari Sommerville (2011)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=2;fontColor=#64748B;fontFamily=Segoe UI, Arial;" vertex="1" parent="1">
          <mxGeometry x="250" y="665" width="500" height="20" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

OUT1.write_text(drawio_xml, encoding="utf-8")
OUT2.write_text(drawio_xml, encoding="utf-8")
print(f"Generated drawio to {OUT1} and {OUT2}")

