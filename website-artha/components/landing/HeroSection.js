"use client";
import { motion } from "framer-motion";
import { siteConfig } from "@/data/siteData";

const containerVariants = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.2, delayChildren: 0.1 }
  }
};

const itemVariants = {
  hidden: { opacity: 0, y: 50 },
  show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 100, damping: 15 } }
};

export default function HeroSection({ onOpenRegistration }) {
  return (
    <section
      id="beranda"
      className="relative flex items-center justify-center overflow-hidden min-h-[100vh] pt-28 pb-12 sm:pt-32 sm:pb-16 lg:pt-40 lg:pb-20 bg-[#FFD600]"
    >
      {/* Brutalist Abstract Shapes */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <motion.div 
          initial={{ x: -100, y: -100, rotate: -20, opacity: 0 }}
          animate={{ x: 0, y: 0, rotate: -10, opacity: 1 }}
          transition={{ duration: 0.8, type: "spring", bounce: 0.5 }}
          className="absolute top-10 left-[-5%] w-64 h-64 bg-[#2727E6] border-[4px] border-[#111118]" 
        />
        <motion.div 
          initial={{ x: 100, y: -100, rotate: 20, opacity: 0 }}
          animate={{ x: 0, y: 0, rotate: 15, opacity: 1 }}
          transition={{ duration: 0.8, type: "spring", bounce: 0.5, delay: 0.1 }}
          className="absolute top-[15%] right-[-2%] w-48 h-48 rounded-full bg-[#FFBAD2] border-[4px] border-[#111118]" 
        />
        <motion.div 
          initial={{ x: -100, y: 100, rotate: 45, opacity: 0 }}
          animate={{ x: 0, y: 0, rotate: 25, opacity: 1 }}
          transition={{ duration: 0.8, type: "spring", bounce: 0.5, delay: 0.2 }}
          className="absolute bottom-[10%] left-[5%] w-0 h-0 border-l-[80px] border-l-transparent border-r-[80px] border-r-transparent border-b-[140px] border-[#1EAB55]" 
        />
        <motion.div 
          initial={{ x: 100, y: 100, rotate: -45, opacity: 0 }}
          animate={{ x: 0, y: 0, rotate: -20, opacity: 1 }}
          transition={{ duration: 0.8, type: "spring", bounce: 0.5, delay: 0.3 }}
          className="absolute bottom-[15%] right-[8%] w-56 h-32 bg-[#8AD9E8] border-[4px] border-[#111118]" 
        />
      </div>

      {/* Content */}
      <motion.div 
        variants={containerVariants}
        initial="hidden"
        whileInView="show"
        viewport={{ once: true, amount: 0.3 }}
        className="relative z-10 max-w-5xl mx-auto px-4 text-center"
      >
        {/* Main Heading */}
        <motion.h1
          variants={itemVariants}
          className="text-4xl sm:text-6xl lg:text-[4.5rem] font-black text-[#111118] uppercase leading-[0.95] tracking-tighter mb-8"
        >
          {siteConfig.tagline}
        </motion.h1>

        {/* Sub-heading */}
        <motion.div variants={itemVariants} className="bg-white border-[3px] border-[#111118] shadow-[6px_6px_0_0_#111118] p-6 max-w-2xl mx-auto mb-10 -rotate-1">
          <p className="text-lg sm:text-xl font-bold text-[#111118] uppercase tracking-widest leading-relaxed">
            {siteConfig.subTagline}
          </p>
        </motion.div>

        {/* CTA Buttons */}
        <motion.div
          variants={itemVariants}
          className="flex flex-col sm:flex-row items-center justify-center gap-6"
        >
          <button
            onClick={() => {
              const el = document.querySelector("#layanan");
              if (el) el.scrollIntoView({ behavior: "smooth" });
            }}
            className="w-full sm:w-auto bg-[#1EAB55] text-white border-[3px] border-[#111118] font-black uppercase text-lg sm:text-xl px-10 py-5 shadow-[6px_6px_0_0_#111118] hover:translate-y-1 hover:shadow-none transition-all"
          >
            Lihat Program
          </button>
          <button
            onClick={onOpenRegistration}
            className="w-full sm:w-auto bg-[#111118] text-white border-[3px] border-[#111118] font-black uppercase text-lg sm:text-xl px-10 py-5 shadow-[6px_6px_0_0_#FFF] hover:translate-y-1 hover:shadow-none transition-all"
          >
            Daftar Gratis
          </button>
        </motion.div>
      </motion.div>
    </section>
  );
}
