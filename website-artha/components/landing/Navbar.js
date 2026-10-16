"use client";
import { useState, useEffect } from "react";
import Image from "next/image";
import { Menu, X } from "lucide-react";
import { motion, AnimatePresence, animate } from "framer-motion";
import { navLinks } from "@/data/siteData";

const searchPlaceholderTexts = [
  "Cari program les...",
  "Jadwal tryout SNBT...",
  "Cabang terdekat...",
  "Testimoni alumni...",
];

function TypewriterSearch() {
  const [placeholderText, setPlaceholderText] = useState("");
  const [wordIndex, setWordIndex] = useState(0);
  const [isDeleting, setIsDeleting] = useState(false);

  useEffect(() => {
    const currentWord = searchPlaceholderTexts[wordIndex];
    let typingSpeed = isDeleting ? 40 : 100;

    if (!isDeleting && placeholderText === currentWord) {
      typingSpeed = 2000;
      setTimeout(() => setIsDeleting(true), typingSpeed);
      return;
    }

    if (isDeleting && placeholderText === "") {
      setIsDeleting(false);
      setWordIndex((prev) => (prev + 1) % searchPlaceholderTexts.length);
      typingSpeed = 500;
      return;
    }

    const timeout = setTimeout(() => {
      setPlaceholderText((prev) => 
        isDeleting 
          ? currentWord.substring(0, prev.length - 1)
          : currentWord.substring(0, prev.length + 1)
      );
    }, typingSpeed);

    return () => clearTimeout(timeout);
  }, [placeholderText, isDeleting, wordIndex]);

  return (
    <div className="hidden lg:flex items-center">
      {/* Search Input Container */}
      <div className="flex items-center border-[2px] border-[#111118] bg-[#F4F7FE] shadow-[2px_2px_0_0_#111118] rounded-lg overflow-hidden h-9 w-48 xl:w-60 relative group transition-colors focus-within:bg-white">
        <input 
          type="text"
          placeholder={placeholderText + "|"}
          className="w-full h-full pl-3 pr-4 bg-transparent outline-none font-bold text-[#111118] text-xs placeholder:text-[#111118]/80 placeholder:font-medium"
        />
      </div>
    </div>
  );
}

const ovalVariants = {
  initial: { pathLength: 0, opacity: 0 },
  hover: { pathLength: 1, opacity: 1, transition: { duration: 0.5, ease: "easeInOut" } }
};

const HandDrawnOval = ({ color = "#FF6600" }) => (
  <svg
    viewBox="0 0 200 100"
    className="absolute inset-0 w-full h-full overflow-visible pointer-events-none scale-[1.35]"
    preserveAspectRatio="none"
  >
    <motion.path
      d="M 140,15 C 80,-5 10,10 10,50 C 10,90 80,95 140,95 C 190,95 190,70 190,50 C 190,20 160,10 90,15"
      fill="none"
      stroke={color}
      strokeWidth="5"
      strokeLinecap="round"
      strokeLinejoin="round"
      variants={ovalVariants}
    />
  </svg>
);

export default function Navbar({ onOpenRegistration }) {
  const [isMobileOpen, setIsMobileOpen] = useState(false);

  const handleNavClick = (href) => {
    setIsMobileOpen(false);
    const el = document.querySelector(href);
    if (el) {
      const y = el.getBoundingClientRect().top + window.scrollY;
      const offset = 100;
      const targetY = y - offset;
      
      // Menggunakan framer-motion animate untuk scroll yang 100% halus (custom easing)
      animate(window.scrollY, targetY, {
        duration: 0.8,
        ease: [0.22, 1, 0.36, 1], // Custom spring-like easing
        onUpdate: (latest) => window.scrollTo(0, latest)
      });
    }
  };

  return (
    <>
      <div className="sticky top-2 z-50 px-4 sm:px-6 lg:px-8 pointer-events-none h-0">
      <header className="w-full max-w-[1440px] mx-auto mt-6 bg-white rounded-full border-[3px] border-[#111118] shadow-[4px_4px_0_0_#111118] pointer-events-auto transition-all h-14 flex flex-col justify-center">
        <div className="px-4 sm:px-6 flex items-center justify-between w-full">

          {/* Left: Logo + Nav Links */}
          <div className="flex items-center gap-6 lg:gap-8">
            {/* Logo */}
            <a
              href="#beranda"
              className="flex items-center shrink-0"
              onClick={(e) => { e.preventDefault(); handleNavClick("#beranda"); }}
            >
              <div className="relative w-24 h-8 sm:w-28 sm:h-9 shrink-0 transition-transform hover:scale-105">
                <Image
                  src="/images/bimbelarthalogo-1.png"
                  alt="Logo Bimbel Artha"
                  fill
                  className="object-contain"
                  priority
                />
              </div>
            </a>

            {/* Desktop Nav Links */}
            <nav className="hidden xl:flex items-center gap-4 ml-4">
              {navLinks.map((link) => (
                <motion.button
                  key={link.href}
                  onClick={() => handleNavClick(link.href)}
                  initial="initial"
                  whileHover="hover"
                  className="relative px-2 py-1 text-[13px] font-black uppercase tracking-widest text-[#111118] whitespace-nowrap"
                >
                  <HandDrawnOval color="#FF6600" />
                  <span className="relative z-10">{link.label}</span>
                </motion.button>
              ))}
            </nav>
          </div>

          {/* Right: Search + CTA + Mobile Toggle */}
          <div className="flex items-center gap-3">
            
            <TypewriterSearch />

            {/* CTA Daftar (desktop) */}
            <button
              onClick={onOpenRegistration}
              className="hidden sm:inline-flex bg-[#2727E6] text-white border-[2px] border-[#111118] rounded-md text-[11px] font-black uppercase tracking-widest px-4 h-9 items-center justify-center shadow-[2px_2px_0_0_#111118] hover:translate-y-[1px] hover:shadow-[1px_1px_0_0_#111118] transition-all"
            >
              Daftar Sekarang
            </button>

            {/* Mobile Toggle */}
            <button
              onClick={() => setIsMobileOpen(!isMobileOpen)}
              className="xl:hidden p-1.5 rounded-lg text-[#111118] border-[2px] border-[#111118] bg-[#FFD600] shadow-[2px_2px_0_0_#111118]"
              aria-label="Toggle menu"
            >
              {isMobileOpen ? <X size={20} /> : <Menu size={20} />}
            </button>
          </div>
        </div>
      </header>
    </div>

      {/* Mobile Dropdown */}
      <AnimatePresence>
        {isMobileOpen && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.25, ease: "easeInOut" }}
            className="fixed top-24 left-4 right-4 z-40 xl:hidden overflow-hidden bg-white border-[3px] border-[#111118] shadow-[6px_6px_0_0_#111118] p-4 space-y-2"
          >
            {navLinks.map((link) => (
              <button
                key={link.href}
                onClick={() => handleNavClick(link.href)}
                className="block w-full text-left px-4 py-4 text-base font-black uppercase tracking-widest text-[#111118] border-b-[2px] border-[#111118]/10 hover:bg-[#FFD600] transition-colors"
              >
                {link.label}
              </button>
            ))}
            <div className="pt-4">
              <button
                onClick={() => { setIsMobileOpen(false); onOpenRegistration?.(); }}
                className="w-full bg-[#2727E6] text-white border-[3px] border-[#111118] font-black uppercase tracking-widest py-4 shadow-[4px_4px_0_0_#111118] hover:translate-y-1 hover:shadow-none transition-all"
              >
                Daftar Sekarang
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
