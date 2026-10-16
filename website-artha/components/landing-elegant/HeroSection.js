"use client";
import { useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import Image from "next/image";
import { ArrowDown } from "lucide-react";

export default function HeroSection({ onOpenRegistration }) {
  const sectionRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: sectionRef,
    offset: ["start start", "end start"],
  });

  // Logo in Hero Section fades out COMPLETELY (1 -> 0) between scrollYProgress 0 and 0.2 (approx scrollY = 180px)
  // This guarantees it is 100% GONE before the header navbar logo appears at scrollY = 220px!
  const logoScale = useTransform(scrollYProgress, [0, 0.2], [1, 0.45]);
  const logoY = useTransform(scrollYProgress, [0, 0.2], [0, -120]);
  const logoOpacity = useTransform(scrollYProgress, [0, 0.2], [1, 0]);

  const taglineOpacity = useTransform(scrollYProgress, [0, 0.15], [1, 0]);
  const taglineY = useTransform(scrollYProgress, [0, 0.15], [0, -30]);

  const bottomOpacity = useTransform(scrollYProgress, [0, 0.12], [1, 0]);
  const ribbonY = useTransform(scrollYProgress, [0, 1], [0, -180]);

  return (
    <section
      ref={sectionRef}
      id="beranda"
      className="relative h-[160vh] w-full"
    >
      {/* Sticky Inner Viewport Container */}
      <div className="sticky top-0 h-screen w-full bg-[#F4F7FE] text-[#111118] flex flex-col justify-center items-center overflow-hidden">
        
        {/* Vibrant Artha Halftone grain texture background */}
        <div
          className="absolute inset-0 pointer-events-none opacity-[0.35]"
          style={{
            backgroundImage: "radial-gradient(circle, #2727E6 0.8px, transparent 0.8px)",
            backgroundSize: "20px 20px",
          }}
        />

        {/* Vibrant 3D Flowing Ribbon Lines with bold Artha colors (Royal Blue, Crimson Red, Sun Yellow) */}
        <motion.div
          className="absolute inset-0 pointer-events-none z-[1]"
          style={{ y: ribbonY }}
        >
          <svg
            className="w-full h-full"
            viewBox="0 0 1440 900"
            fill="none"
            preserveAspectRatio="xMidYMid slice"
          >
            {[...Array(24)].map((_, i) => {
              const strokeColor = i % 3 === 0 ? "#2727E6" : i % 3 === 1 ? "#E11D48" : "#FFD600";
              return (
                <motion.path
                  key={i}
                  d={`M ${-60 + i * 2} ${950 - i * 14} C ${300 + i * 5} ${830 - i * 12}, ${680 + i * 3} ${520 - i * 9}, ${960 + i * 2} ${280 - i * 5} S ${1300 + i} ${80 - i * 2}, ${1550 + i * 3} ${50 - i}`}
                  stroke={strokeColor}
                  strokeWidth={3 - i * 0.07}
                  strokeOpacity={0.65}
                  fill="none"
                  initial={{ pathLength: 0 }}
                  animate={{ pathLength: 1 }}
                  transition={{ duration: 1.8, delay: i * 0.03, ease: "easeOut" }}
                />
              );
            })}
          </svg>
        </motion.div>

        {/* Center: Official Bimbel Artha Logo (Large) + Slogan */}
        <div className="relative z-10 w-full max-w-[1440px] px-6 sm:px-12 lg:px-20 flex flex-col items-center justify-center">
          
          <div className="flex flex-col lg:flex-row items-center justify-center gap-8 lg:gap-16">
            
            {/* The Official Bimbel Artha Logo Image - Fades out COMPLETELY to opacity 0 on scroll before header logo shows */}
            <motion.div
              style={{
                scale: logoScale,
                opacity: logoOpacity,
                y: logoY,
              }}
              className="relative w-[320px] h-[100px] sm:w-[480px] sm:h-[150px] md:w-[600px] md:h-[185px] lg:w-[680px] lg:h-[210px] shrink-0 filter drop-shadow-md"
            >
              <Image
                src="/images/bimbelarthalogo-1.png"
                alt="Logo Bimbel Artha"
                fill
                className="object-contain"
                priority
              />
            </motion.div>

            {/* Tagline right side with bold vibrant colors */}
            <motion.div
              className="flex flex-col gap-2 text-center lg:text-left"
              style={{ opacity: taglineOpacity, y: taglineY }}
            >
              <span className="text-2xl sm:text-4xl lg:text-5xl font-black uppercase tracking-[-0.02em] text-[#111118] leading-[1.05]">
                RAIH PRESTASI,
              </span>
              <span className="text-2xl sm:text-4xl lg:text-5xl font-black uppercase tracking-[-0.02em] text-[#2727E6] leading-[1.05] drop-shadow-sm">
                GEMILANG BERSAMA
              </span>
              <p className="text-xs sm:text-sm font-bold tracking-[0.2em] text-[#E11D48] uppercase mt-2">
                Bimbingan Belajar Terpercaya Sejak 1997
              </p>
            </motion.div>
          </div>

        </div>

        {/* Bottom "SCROLL TO EXPLORE ↓" */}
        <motion.div
          className="absolute bottom-10 left-1/2 -translate-x-1/2 z-10 flex items-center gap-3 cursor-pointer group"
          style={{ opacity: bottomOpacity }}
          onClick={() => {
            const el = document.querySelector("#layanan");
            if (el) el.scrollIntoView({ behavior: "smooth" });
          }}
        >
          <span className="text-[11px] font-bold uppercase tracking-[0.3em] text-[#111118] group-hover:text-[#2727E6] transition-colors">
            SCROLL TO EXPLORE
          </span>
          <ArrowDown size={14} className="text-[#2727E6] animate-bounce" />
        </motion.div>

      </div>
    </section>
  );
}
