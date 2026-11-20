import fitz
from pathlib import Path
from PIL import Image

# Output paths
ROOT = Path("c:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA")
OUT_DIR = ROOT / "ASET BAB 2.1"
DRAFT_DIR = ROOT / "DRAFT PROPOSAL MD/BAB 2/ASET BAB 2.1"
ARTIFACT_DIR = Path("C:/Users/ARIEL/.gemini/antigravity/brain/b4f2bb35-f783-4d11-88ed-819fbfb3f0fb")

# Dimensions
WIDTH = 1000
HEIGHT = 720

svg_content = f'''<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Background Canvas -->
  <rect width="{WIDTH}" height="{HEIGHT}" fill="#FFFFFF"/>

  <!-- Top Right Title Badge: MVC -->
  <text x="910" y="55" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="28" font-weight="800" fill="#0F172A" text-anchor="middle" letter-spacing="2">MVC</text>

  <!-- ==================== USER / CLIENT ACTOR (TOP RIGHT) ==================== -->
  <rect x="710" y="25" width="160" height="46" rx="8" fill="#F8FAFC" stroke="#64748B" stroke-width="1.8"/>
  <text x="790" y="53" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">User / Pengguna</text>

  <!-- Arrow: User -> View (User Events) -->
  <line x1="790" y1="71" x2="790" y2="125" stroke="#1E293B" stroke-width="2"/>
  <polygon points="785,123 790,133 795,123" fill="#1E293B"/>
  <rect x="800" y="85" width="105" height="24" rx="4" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
  <text x="852" y="101" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="11" font-weight="600" fill="#334155" text-anchor="middle">User Events</text>

  <!-- ==================== 1. CONTROLLER CARD (TOP LEFT) ==================== -->
  <!-- Outer Card -->
  <rect x="70" y="135" width="350" height="185" rx="10" fill="#FFFFFF" stroke="#334155" stroke-width="2"/>
  <!-- Header Bar -->
  <rect x="85" y="150" width="320" height="46" rx="6" fill="#F1F5F9" stroke="#475569" stroke-width="1.5"/>
  <text x="245" y="179" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="17" font-weight="700" fill="#0F172A" text-anchor="middle">Controller</text>
  <!-- Content Details -->
  <text x="105" y="222" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="13" font-weight="600" fill="#334155">• Maps User Actions to Model Updates</text>
  <text x="105" y="246" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="13" font-weight="600" fill="#334155">• Selects and Directs View</text>
  <text x="105" y="270" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="12" font-style="italic" fill="#64748B">(Logika Pengendali &amp; Alur Sistem)</text>

  <!-- ==================== 2. VIEW CARD (TOP RIGHT) ==================== -->
  <!-- Outer Card -->
  <rect x="580" y="135" width="350" height="185" rx="10" fill="#FFFFFF" stroke="#334155" stroke-width="2"/>
  <!-- Header Bar -->
  <rect x="595" y="150" width="320" height="46" rx="6" fill="#F1F5F9" stroke="#475569" stroke-width="1.5"/>
  <text x="755" y="179" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="17" font-weight="700" fill="#0F172A" text-anchor="middle">View</text>
  <!-- Content Details -->
  <text x="615" y="222" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="13" font-weight="600" fill="#334155">• Renders Model Data</text>
  <text x="615" y="246" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="13" font-weight="600" fill="#334155">• Sends User Events to Controller</text>
  <text x="615" y="270" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="12" font-style="italic" fill="#64748B">(Tampilan Antarmuka &amp; Presentasi)</text>

  <!-- ==================== 3. MODEL CARD (BOTTOM CENTER) ==================== -->
  <!-- Outer Card -->
  <rect x="325" y="420" width="350" height="185" rx="10" fill="#FFFFFF" stroke="#334155" stroke-width="2"/>
  <!-- Header Bar -->
  <rect x="340" y="435" width="320" height="46" rx="6" fill="#F1F5F9" stroke="#475569" stroke-width="1.5"/>
  <text x="500" y="464" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="17" font-weight="700" fill="#0F172A" text-anchor="middle">Model</text>
  <!-- Content Details -->
  <text x="360" y="507" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="13" font-weight="600" fill="#334155">• Encapsulates Application State</text>
  <text x="360" y="531" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="13" font-weight="600" fill="#334155">• Notifies View of State Changes</text>
  <text x="360" y="555" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="12" font-style="italic" fill="#64748B">(Struktur Data &amp; Operasi Basis Data)</text>

  <!-- ==================== INTER-COMPONENT CONNECTING ARROWS ==================== -->

  <!-- 1. Controller -> View (Selects View / View Selection) -->
  <line x1="420" y1="185" x2="570" y2="185" stroke="#1E293B" stroke-width="2"/>
  <polygon points="568,180 578,185 568,190" fill="#1E293B"/>
  <rect x="445" y="162" width="110" height="22" rx="4" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="500" y="177" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="11" font-weight="600" fill="#1E293B" text-anchor="middle">Selects View</text>

  <!-- 2. View -> Controller (Sends User Events) -->
  <line x1="580" y1="245" x2="430" y2="245" stroke="#1E293B" stroke-width="2"/>
  <polygon points="432,240 422,245 432,250" fill="#1E293B"/>
  <rect x="435" y="250" width="130" height="22" rx="4" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="500" y="265" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="11" font-weight="600" fill="#1E293B" text-anchor="middle">Sends User Events</text>

  <!-- 3. Controller -> Model (Maps User Actions to Model Updates / State Change) -->
  <!-- Orthogonal Connector: From Controller Bottom down then into Model Left -->
  <path d="M 245 320 L 245 490 L 315 490" fill="none" stroke="#1E293B" stroke-width="2"/>
  <polygon points="313,485 323,490 313,495" fill="#1E293B"/>
  <!-- Label pill -->
  <rect x="135" y="380" width="175" height="42" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="222" y="398" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Maps User Actions</text>
  <text x="222" y="413" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="11" font-weight="600" fill="#475569" text-anchor="middle">to Model Updates</text>

  <!-- 4. Model -> View (Notifies View of State Changes / Change Notification) -->
  <!-- Orthogonal Connector: From Model Right to right then up into View Bottom -->
  <path d="M 675 490 L 755 490 L 755 330" fill="none" stroke="#1E293B" stroke-width="2"/>
  <polygon points="750,332 755,322 760,332" fill="#1E293B"/>
  <!-- Label pill -->
  <rect x="690" y="380" width="175" height="42" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="777" y="398" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Change Notification</text>
  <text x="777" y="413" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="11" font-weight="600" fill="#475569" text-anchor="middle">(Notifies State Change)</text>

  <!-- 5. View -> Model (Requests Model Updates / State Query) -->
  <!-- Diagonal Dashed Connector between View and Model -->
  <path d="M 620 320 L 530 410" fill="none" stroke="#64748B" stroke-width="1.8" stroke-dasharray="5,4"/>
  <polygon points="530,402 524,416 538,410" fill="#64748B"/>
  <rect x="535" y="340" width="125" height="22" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="597" y="355" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="10.5" font-weight="600" fill="#475569" text-anchor="middle">State Query / Renders</text>

  <!-- ==================== BOTTOM CAPTIONS ==================== -->
  <text x="500" y="650" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="14.5" font-weight="700" fill="#0F172A" text-anchor="middle">Fig. 6.3. The organization of the Model-View-Controller (MVC) pattern.</text>
  <text x="500" y="675" font-family="'Segoe UI', Inter, Arial, sans-serif" font-size="12.5" font-style="italic" fill="#64748B" text-anchor="middle">Sumber: Diadaptasi dan digambar ulang dari Sommerville (2011)</text>
</svg>'''

# 1. Write SVG to ASET BAB 2.1 in workspace and draft folder
svg_path1 = OUT_DIR / "Gambar_2_5_Arsitektur_MVC.svg"
svg_path2 = DRAFT_DIR / "Gambar_2_5_Arsitektur_MVC.svg"
svg_path1.write_text(svg_content, encoding="utf-8")
svg_path2.write_text(svg_content, encoding="utf-8")
print(f"Saved SVG to {svg_path1}")

# 2. Render to High-Resolution PNG via PyMuPDF (fitz)
doc = fitz.open(stream=svg_content.encode("utf-8"), filetype="svg")
# Render at 300 DPI (approx 3x scale of 72 dpi)
zoom = 300 / 72
mat = fitz.Matrix(zoom, zoom)
pix = doc[0].get_pixmap(matrix=mat)

# Save PNGs
png_path1 = OUT_DIR / "Gambar_2_5_Arsitektur_MVC.png"
png_path2 = DRAFT_DIR / "Gambar_2_5_Arsitektur_MVC.png"
pix.save(str(png_path1))
pix.save(str(png_path2))

# Also backup and update "Gambar 2.5 Arsitektur MVC Sommerville 2011.png"
bak_path = OUT_DIR / "Gambar 2.5 Arsitektur MVC Sommerville 2011_OLD_RASTER.png"
if not bak_path.exists():
    (OUT_DIR / "Gambar 2.5 Arsitektur MVC Sommerville 2011.png").rename(bak_path)

pix.save(str(OUT_DIR / "Gambar 2.5 Arsitektur MVC Sommerville 2011.png"))
pix.save(str(DRAFT_DIR / "Gambar 2.5 Arsitektur MVC Sommerville 2011.png"))

# Copy to artifacts directory
artifact_png = ARTIFACT_DIR / "Gambar_2_5_Arsitektur_MVC.png"
pix.save(str(artifact_png))
print(f"Saved PNG to {png_path1} and artifact: {artifact_png}")
print(f"Resolution: {pix.width}x{pix.height}")

