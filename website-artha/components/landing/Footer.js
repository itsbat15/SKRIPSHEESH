"use client";
import Image from "next/image";
import { siteConfig } from "@/data/siteData";
import { motion } from "framer-motion";
const footerColumns = [
  {
    title: "Layanan",
    links: [
      { label: "Calistung (TK)", href: "#layanan" },
      { label: "SD", href: "#layanan" },
      { label: "SMP", href: "#layanan" },
      { label: "SMA", href: "#layanan" },
      { label: "Bahasa Inggris", href: "#layanan" },
    ],
  },
  {
    title: "Perusahaan",
    links: [
      { label: "Tentang Kami", href: "#tentang" },
      { label: "Tim Pengajar", href: "#tim" },
      { label: "Cabang", href: "#cabang" },
      { label: "Testimoni", href: "#" },
    ],
  },
  {
    title: "Bantuan",
    links: [
      { label: "FAQ", href: "#faq" },
      { label: "Syarat & Ketentuan", href: "#" },
      { label: "Kebijakan Privasi", href: "#" },
      { label: "Kontak", href: "#kontak" },
    ],
  },
];

const socialLinks = [
  { 
    name: "Instagram", 
    href: siteConfig.socialMedia.instagram || "#", 
    color: "bg-[#FFBAD2]", 
    icon: (
      <svg viewBox="0 0 24 24" fill="currentColor" className="w-6 h-6">
        <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069ZM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0Zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324ZM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8Zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881Z" />
      </svg>
    ) 
  },
  { 
    name: "TikTok", 
    href: siteConfig.socialMedia.tiktok || "#", 
    color: "bg-[#B8F0D8]", 
    icon: (
      <svg viewBox="0 0 24 24" fill="currentColor" className="w-6 h-6">
        <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 15.68a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1.04-.08z" />
      </svg>
    )
  },
  { 
    name: "Facebook", 
    href: siteConfig.socialMedia.facebook || "#", 
    color: "bg-[#FFD600]", 
    icon: (
      <svg viewBox="0 0 24 24" fill="currentColor" className="w-6 h-6">
        <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073Z" />
      </svg>
    ) 
  },
  { 
    name: "Website", 
    href: siteConfig.socialMedia.website || "#", 
    color: "bg-[#C5E8F7]", 
    icon: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" className="w-6 h-6">
        <circle cx="12" cy="12" r="10"></circle>
        <line x1="2" y1="12" x2="22" y2="12"></line>
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
      </svg>
    ) 
  },
];

export default function Footer() {
  const handleNavClick = (href) => {
    const el = document.querySelector(href);
    if (el) el.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <footer id="kontak" className="superhi-section bg-[#111118] text-white pt-20 sm:pt-28 pb-12 sm:pb-16 mt-8 overflow-hidden relative">
      <motion.div 
        initial="hidden"
        whileInView="show"
        viewport={{ once: true, amount: 0.1 }}
        variants={{
          hidden: { opacity: 0 },
          show: {
            opacity: 1,
            transition: { staggerChildren: 0.2 }
          }
        }}
        className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10"
      >
        
        {/* TOP: Giant CTA */}
        <motion.div 
          variants={{ hidden: { opacity: 0, y: 100 }, show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 100, damping: 15 } } }}
          className="flex flex-col lg:flex-row items-center justify-between gap-10 border-b-[3px] border-white/20 pb-16 mb-16"
        >
          <div className="lg:w-2/3">
            <h2 className="text-5xl sm:text-7xl lg:text-[5.5rem] font-black uppercase tracking-tighter leading-[0.9] mb-6">
              Siap Masuk <br/><span className="text-[#1EAB55]">PTN Impianmu</span> <br/>Tahun Ini?
            </h2>
            <p className="text-lg sm:text-xl text-white/80 font-medium max-w-lg">
              Bergabunglah bersama ribuan siswa yang telah sukses meraih prestasi dan masa depan gemilang bersama Bimbel Artha.
            </p>
          </div>
          
          <div className="lg:w-1/3 flex lg:justify-end w-full">
            <a 
              href={`https://wa.me/${siteConfig.whatsapp}`} 
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block bg-[#FFD600] text-[#111118] text-xl sm:text-3xl font-black uppercase tracking-tight px-8 sm:px-12 py-5 sm:py-6 border-[4px] border-white shadow-[8px_8px_0_0_#FFF] hover:translate-y-2 hover:shadow-none transition-all w-full lg:w-auto text-center whitespace-nowrap"
            >
              Daftar Sekarang
            </a>
          </div>
        </motion.div>

        {/* MIDDLE: Columns & Newsletter */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-16 mb-20">
          
          {/* Left: Logo and Address */}
          <motion.div 
            variants={{ hidden: { opacity: 0, y: 50 }, show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 100, damping: 15 } } }}
            className="lg:col-span-4 flex flex-col items-start"
          >
            <div className="bg-white p-4 mb-6 border-[3px] border-white shadow-[6px_6px_0_0_#1EAB55] -rotate-2">
              <div className="relative w-36 h-12">
                <Image
                  src="/images/bimbelarthalogo-1.png"
                  alt="Logo Bimbel Artha"
                  fill
                  className="object-contain"
                />
              </div>
            </div>
            <p className="text-white/70 font-medium text-sm leading-relaxed max-w-xs mb-8">
              {siteConfig.address}
            </p>
            
            {/* Brutalist Socials */}
            <div className="flex gap-4">
              {socialLinks.map((social) => (
                <a
                  key={social.name}
                  href={social.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={`w-14 h-14 flex items-center justify-center border-[3px] border-white text-[#111118] shadow-[4px_4px_0_0_#FFF] hover:translate-y-1 hover:shadow-[0px_0px_0_0_#FFF] transition-all ${social.color}`}
                  aria-label={social.name}
                >
                  {social.icon}
                </a>
              ))}
            </div>
          </motion.div>

          {/* Center: Links */}
          <motion.div 
            variants={{ hidden: { opacity: 0, y: 50 }, show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 100, damping: 15 } } }}
            className="lg:col-span-4 grid grid-cols-2 gap-8"
          >
            {footerColumns.slice(0, 2).map((col) => (
              <div key={col.title}>
                <h4 className="text-xl font-black text-[#FFD600] mb-6 uppercase tracking-widest">
                  {col.title}
                </h4>
                <ul className="space-y-4">
                  {col.links.map((link) => (
                    <li key={link.label}>
                      <button
                        onClick={() => handleNavClick(link.href)}
                        className="text-white/80 hover:text-white hover:underline font-bold text-lg transition-colors"
                      >
                        {link.label}
                      </button>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </motion.div>

          {/* Right: Newsletter / Contact */}
          <motion.div 
            variants={{ hidden: { opacity: 0, y: 50 }, show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 100, damping: 15 } } }}
            className="lg:col-span-4"
          >
            <h4 className="text-xl font-black text-[#FFD600] mb-6 uppercase tracking-widest">
              Langganan Info
            </h4>
            <p className="text-white/80 font-medium text-sm mb-6">
              Dapatkan tips belajar dan info pendaftaran terbaru langsung ke email Anda.
            </p>
            <form className="flex flex-col gap-4" onSubmit={(e) => e.preventDefault()}>
              <input 
                type="email" 
                placeholder="ALAMAT EMAIL" 
                className="bg-[#111118] border-[3px] border-white text-white p-4 font-bold placeholder:text-white/40 focus:outline-none focus:bg-white/10 transition-colors uppercase tracking-widest text-sm"
              />
              <button 
                type="submit"
                className="bg-[#1EAB55] text-white border-[3px] border-white font-black uppercase tracking-widest p-4 shadow-[6px_6px_0_0_#FFF] hover:translate-y-1 hover:shadow-[0px_0px_0_0_#FFF] transition-all"
              >
                Berlangganan
              </button>
            </form>
          </motion.div>
        </div>

        {/* BOTTOM: Copyright */}
        <motion.div 
          variants={{ hidden: { opacity: 0 }, show: { opacity: 1, transition: { duration: 1 } } }}
          className="flex flex-col sm:flex-row items-center justify-center pt-8 border-t-[3px] border-white/20 text-white/50 font-bold text-xs uppercase tracking-widest text-center"
        >
          <p>© {new Date().getFullYear()} {siteConfig.name.toUpperCase()}. ALL RIGHTS RESERVED.</p>
        </motion.div>
      </motion.div>

      {/* GIANT WATERMARK BACKGROUND */}
      <motion.div 
        initial={{ y: 200, opacity: 0 }}
        whileInView={{ y: 0, opacity: 0.02 }}
        viewport={{ once: true }}
        transition={{ duration: 1, ease: "easeOut" }}
        className="absolute -bottom-10 sm:-bottom-24 left-0 right-0 overflow-hidden pointer-events-none select-none flex justify-center z-0"
      >
        <h1 className="text-[14rem] sm:text-[22rem] lg:text-[30rem] font-black uppercase text-white whitespace-nowrap leading-none tracking-tighter">
          ARTHA
        </h1>
      </motion.div>
    </footer>
  );
}
