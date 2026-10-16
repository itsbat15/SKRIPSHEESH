import ElegantNavbar from "@/components/landing-elegant/Navbar";
import ElegantFooter from "@/components/landing-elegant/Footer";

export default function ElegantLayout({ children }) {
  return (
    <div className="min-h-screen flex flex-col bg-[#F8FAFC] text-[#0F172A] antialiased selection:bg-[#1E3A8A] selection:text-white" style={{ scrollBehavior: "smooth" }}>
      {/* Global Artha halftone dot texture overlay in subtle Artha Navy tint */}
      <div
        className="fixed inset-0 pointer-events-none z-0 opacity-25"
        style={{
          backgroundImage: "radial-gradient(circle, #1E3A8A 0.65px, transparent 0.65px)",
          backgroundSize: "18px 18px",
        }}
      />
      <div className="relative z-10 flex flex-col min-h-screen">
        <ElegantNavbar />
        <main className="flex-1">{children}</main>
        <ElegantFooter />
      </div>
    </div>
  );
}
