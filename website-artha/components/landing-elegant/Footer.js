"use client";
import Image from "next/image";
import { siteConfig } from "@/data/siteData";
import { ArrowUp } from "lucide-react";
import { animate } from "framer-motion";

export default function ElegantFooter() {
  const scrollToTop = () => {
    animate(window.scrollY, 0, {
      duration: 0.9,
      ease: [0.22, 1, 0.36, 1],
      onUpdate: (v) => window.scrollTo(0, v),
    });
  };

  return (
    <footer className="relative bg-[#FFFFFF] text-[#0F172A] border-t border-[#0F172A]/10 pt-12 pb-12 overflow-hidden select-none">
      
      {/* Artha Navy Halftone texture background */}
      <div
        className="absolute inset-0 pointer-events-none opacity-20"
        style={{
          backgroundImage: "radial-gradient(circle, #1E3A8A 0.6px, transparent 0.6px)",
          backgroundSize: "18px 18px",
        }}
      />

      <div className="relative z-10 max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16">
        
        {/* GIANT "ARTHA" WATERMARK TEXT */}
        <div className="my-8 sm:my-12 overflow-hidden">
          <h1 className="text-[7rem] sm:text-[12rem] md:text-[16rem] lg:text-[20rem] xl:text-[24rem] font-black tracking-[-0.07em] text-[#0F172A] leading-[0.8] uppercase text-center sm:text-left select-none opacity-[0.92]">
            AR<span className="relative inline-block">T<span className="absolute left-0 right-0 top-[38%] h-[0.06em] bg-[#0F172A]" /></span>HA
          </h1>
        </div>

        {/* BOTTOM SECTION: 3 Columns */}
        <div className="grid grid-cols-1 md:grid-cols-12 gap-10 pt-10 border-t border-[#0F172A]/10 text-xs">
          
          {/* Column 1: HEAD OFFICE (Left) */}
          <div className="md:col-span-5 space-y-3">
            <span className="text-[10px] font-mono font-bold tracking-[0.25em] text-[#2563EB] uppercase block mb-2">
              HEAD OFFICE
            </span>
            <p className="font-bold text-[#0F172A] leading-relaxed">
              {siteConfig.address}
            </p>
            <p className="text-[#475569] font-mono">
              Telp / WhatsApp: {siteConfig.phone} | Email: {siteConfig.email}
            </p>
            <p className="text-[10px] text-[#94A3B8] font-mono tracking-wider pt-2">
              ESTABLISHED OCTOBER 10, 1997 · BALIKPAPAN
            </p>
          </div>

          {/* Column 2: Main Links (Center) */}
          <div className="md:col-span-3 space-y-2">
            <span className="text-[10px] font-mono font-bold tracking-[0.25em] text-[#2563EB] uppercase block mb-2">
              NAVIGASI UTAMA
            </span>
            <ul className="space-y-2 font-bold uppercase text-[11px] text-[#0F172A]">
              <li><a href="#tentang" className="hover:text-[#2563EB] transition-colors">Tentang Kami</a></li>
              <li><a href="#layanan" className="hover:text-[#2563EB] transition-colors">Program Belajar</a></li>
              <li><a href="#tim" className="hover:text-[#2563EB] transition-colors">Team Pengajar</a></li>
              <li><a href="#galeri" className="hover:text-[#2563EB] transition-colors">Galeri Kegiatan</a></li>
              <li><a href="#artikel" className="hover:text-[#2563EB] transition-colors">Artikel & Berita</a></li>
              <li><a href="#cabang" className="hover:text-[#2563EB] transition-colors">8 Cabang Balikpapan</a></li>
            </ul>
          </div>

          {/* Column 3: Policy & Back to Top (Right) */}
          <div className="md:col-span-4 flex flex-col justify-between space-y-6">
            <div>
              <span className="text-[10px] font-mono font-bold tracking-[0.25em] text-[#2563EB] uppercase block mb-2">
                INFORMASI HUKUM & LISENSI
              </span>
              <ul className="space-y-2 text-[#475569] text-[11px]">
                <li><a href="#faq" className="hover:text-[#0F172A] transition-colors">Syarat & Ketentuan Pendaftaran</a></li>
                <li><a href="#faq" className="hover:text-[#0F172A] transition-colors">Kebijakan Privasi Siswa</a></li>
                <li><a href="#faq" className="hover:text-[#0F172A] transition-colors">Pertanyaan Umum (FAQ)</a></li>
                <li><span className="text-[#94A3B8]">Izin Operasional Dinas Pendidikan Balikpapan</span></li>
              </ul>
            </div>

            <div className="flex items-center justify-between pt-4 border-t border-[#0F172A]/10">
              <span className="text-[10px] font-mono text-[#94A3B8]">
                © {new Date().getFullYear()} BIMBEL ARTHA. ALL RIGHTS RESERVED.
              </span>
              <button
                onClick={scrollToTop}
                className="inline-flex items-center gap-1 text-[10px] font-bold uppercase tracking-widest text-[#0F172A] hover:text-[#2563EB] transition-colors"
              >
                Back to Top <ArrowUp size={14} />
              </button>
            </div>
          </div>

        </div>

      </div>
    </footer>
  );
}
