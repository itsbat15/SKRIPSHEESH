"use client";
import { useState, useEffect } from "react";
import Image from "next/image";
import { Menu, X, ChevronDown, ArrowUpRight } from "lucide-react";
import { motion, AnimatePresence, animate } from "framer-motion";

export const navLinksWithSub = [
  { label: "Beranda", href: "#beranda" },
  { label: "Tentang Kami", href: "#tentang" },
  { label: "Layanan", href: "#layanan" },
  { label: "Team Pengajar", href: "#tim" },
  {
    label: "Galeri",
    href: "#galeri",
    subItems: [
      { label: "TK / Prasekolah", href: "#layanan" },
      { label: "Sekolah Dasar (SD)", href: "#layanan" },
      { label: "Sekolah Menengah (SMP)", href: "#layanan" },
      { label: "Sekolah Atas (SMA)", href: "#layanan" },
      { label: "Bahasa Inggris", href: "#layanan" },
    ],
  },
  { label: "Pendaftaran", href: "#pendaftaran" },
  { label: "Artikel", href: "#artikel" },
  { label: "Kontak Kami", href: "#cabang" },
];

const ovalVariants = {
  initial: { pathLength: 0, opacity: 0 },
  hover: { pathLength: 1, opacity: 1, transition: { duration: 0.45, ease: "easeInOut" } }
};

// Hand Drawn Oval SVG Hover Effect (Matching Image 2 in Artha Royal Blue #2727E6)
const HandDrawnBlueOval = () => (
  <svg
    viewBox="0 0 200 100"
    className="absolute inset-0 w-full h-full overflow-visible pointer-events-none scale-[1.35] z-0"
    preserveAspectRatio="none"
  >
    <motion.path
      d="M 140,15 C 80,-5 10,10 10,50 C 10,90 80,95 140,95 C 190,95 190,70 190,50 C 190,20 160,10 90,15"
      fill="none"
      stroke="#2727E6"
      strokeWidth="4"
      strokeLinecap="round"
      strokeLinejoin="round"
      variants={ovalVariants}
    />
  </svg>
);

export default function ElegantNavbar({ onOpenRegistration }) {
  const [isMobileOpen, setIsMobileOpen] = useState(false);
  const [scrollY, setScrollY] = useState(0);
  const [activeDropdown, setActiveDropdown] = useState(null);

  useEffect(() => {
    const onScroll = () => {
      setScrollY(window.scrollY);
    };
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const logoOpacity = Math.max(0, Math.min(1, (scrollY - 220) / 160));

  const handleNavClick = (href) => {
    setIsMobileOpen(false);
    setActiveDropdown(null);
    if (href === "#pendaftaran" && onOpenRegistration) {
      onOpenRegistration();
      return;
    }
    const el = document.querySelector(href);
    if (el) {
      const y = el.getBoundingClientRect().top + window.scrollY - 90;
      animate(window.scrollY, y, {
        duration: 0.9,
        ease: [0.22, 1, 0.36, 1],
        onUpdate: (v) => window.scrollTo(0, v),
      });
    }
  };

  return (
    <header className="fixed top-0 left-0 right-0 z-50 pointer-events-none px-4 sm:px-8 pt-4">
      {/* Floating Pill Navbar */}
      <div
        className={`w-full max-w-[1380px] mx-auto rounded-full transition-all duration-500 pointer-events-auto border border-[#0F172A]/10 shadow-md ${
          scrollY > 250
            ? "bg-white/95 backdrop-blur-md py-2.5 px-6"
            : "bg-white/80 backdrop-blur-sm py-3 px-6"
        }`}
      >
        <div className="flex items-center justify-between w-full">
          
          {/* Left: Official Bimbel Artha Logo */}
          <a
            href="#beranda"
            onClick={(e) => { e.preventDefault(); handleNavClick("#beranda"); }}
            className="flex items-center shrink-0"
          >
            <div
              style={{
                opacity: logoOpacity,
                transform: `scale(${0.85 + logoOpacity * 0.15})`,
                transition: "opacity 0.2s ease-out, transform 0.2s ease-out",
              }}
              className={`relative w-28 h-8 sm:w-32 sm:h-9 shrink-0 ${
                logoOpacity > 0.1 ? "pointer-events-auto" : "pointer-events-none"
              }`}
            >
              <Image
                src="/images/bimbelarthalogo-1.png"
                alt="Logo Bimbel Artha"
                fill
                className="object-contain object-left"
                priority
              />
            </div>
          </a>

          {/* Desktop Nav Links with Artha Blue Hand-Drawn Oval Hover (Image 2 style) */}
          <nav className="hidden xl:flex items-center gap-2 text-[11px] font-black tracking-[0.08em] uppercase text-[#0F172A]">
            {navLinksWithSub.map((link) => {
              const hasSub = !!link.subItems;

              return (
                <div
                  key={link.label}
                  className="relative"
                  onMouseEnter={() => hasSub && setActiveDropdown(link.label)}
                  onMouseLeave={() => hasSub && setActiveDropdown(null)}
                >
                  <motion.button
                    initial="initial"
                    whileHover="hover"
                    onClick={() => handleNavClick(link.href)}
                    className="relative px-3 py-2 flex items-center gap-1 hover:text-[#2727E6] transition-colors z-10"
                  >
                    <HandDrawnBlueOval />
                    <span className="relative z-10">{link.label}</span>
                    {hasSub && (
                      <ChevronDown
                        size={12}
                        className={`transition-transform duration-200 relative z-10 ${
                          activeDropdown === link.label ? "rotate-180 text-[#2727E6]" : ""
                        }`}
                      />
                    )}
                  </motion.button>

                  {/* Submenu Dropdown */}
                  {hasSub && (
                    <AnimatePresence>
                      {activeDropdown === link.label && (
                        <motion.div
                          initial={{ opacity: 0, y: 8 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: 8 }}
                          transition={{ duration: 0.18 }}
                          className="absolute top-full left-0 w-52 bg-white backdrop-blur-md border border-[#0F172A]/10 shadow-xl py-2 z-50 rounded-xl mt-1 overflow-hidden"
                        >
                          {link.subItems.map((sub) => (
                            <button
                              key={sub.label}
                              onClick={() => handleNavClick(sub.href)}
                              className="w-full text-left px-4 py-2 text-[10px] font-bold tracking-wider uppercase text-[#334155] hover:bg-[#F1F5F9] hover:text-[#2727E6] transition-colors border-b border-[#0F172A]/5 last:border-0"
                            >
                              {sub.label}
                            </button>
                          ))}
                        </motion.div>
                      )}
                    </AnimatePresence>
                  )}
                </div>
              );
            })}
          </nav>

          {/* Right: CTA Button */}
          <div className="flex items-center gap-3 shrink-0">
            <button
              onClick={onOpenRegistration}
              className="inline-flex items-center gap-1.5 px-5 py-2 bg-[#111118] text-white rounded-full text-[10px] font-bold uppercase tracking-wider hover:bg-[#2727E6] transition-all shadow-sm"
            >
              Daftar Sekarang
              <ArrowUpRight size={12} />
            </button>

            {/* Mobile Menu Trigger */}
            <button
              onClick={() => setIsMobileOpen(!isMobileOpen)}
              className="xl:hidden p-2 bg-white rounded-full border border-[#0F172A]/10 text-[#0F172A]"
              aria-label="Toggle Menu"
            >
              {isMobileOpen ? <X size={18} /> : <Menu size={18} />}
            </button>
          </div>

        </div>
      </div>

      {/* Mobile Drawer */}
      <AnimatePresence>
        {isMobileOpen && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className="xl:hidden fixed inset-x-4 top-20 pointer-events-auto bg-[#111118] text-white rounded-2xl p-6 shadow-2xl border border-white/10 overflow-hidden max-h-[80vh] overflow-y-auto"
          >
            <div className="flex flex-col gap-1">
              {navLinksWithSub.map((link) => (
                <div key={link.label} className="border-b border-white/10 pb-2 mb-1">
                  <button
                    onClick={() => handleNavClick(link.href)}
                    className="text-left py-2 text-[11px] font-bold tracking-widest uppercase text-white hover:text-[#2727E6] transition-colors w-full flex items-center justify-between"
                  >
                    <span>{link.label}</span>
                    {link.subItems && <ChevronDown size={14} />}
                  </button>
                  {link.subItems && (
                    <div className="pl-4 space-y-1 mt-1 border-l border-white/20">
                      {link.subItems.map((sub) => (
                        <button
                          key={sub.label}
                          onClick={() => handleNavClick(sub.href)}
                          className="block text-left py-1.5 text-[10px] text-white/70 hover:text-white uppercase tracking-wider"
                        >
                          • {sub.label}
                        </button>
                      ))}
                    </div>
                  )}
                </div>
              ))}
              <button
                onClick={() => { setIsMobileOpen(false); onOpenRegistration?.(); }}
                className="mt-4 flex items-center justify-center gap-2 py-3 px-6 bg-[#2727E6] text-white rounded-full text-[11px] font-bold uppercase tracking-widest"
              >
                Daftar Sekarang
                <ArrowUpRight size={13} />
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
