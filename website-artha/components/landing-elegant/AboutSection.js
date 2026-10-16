"use client";
import { motion } from "framer-motion";
import { aboutText, timeline } from "@/data/siteData";

export default function AboutSection() {
  return (
    <section id="tentang" className="py-24 sm:py-32 bg-[#F7F7F8] text-[#111111] border-b border-black/10 overflow-hidden">
      <div className="max-w-[1400px] mx-auto px-6 sm:px-12 lg:px-20">
        
        {/* Section Header */}
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ margin: "-100px" }}
          transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
          className="mb-20"
        >
          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-8 pb-10 border-b border-black/10">
            <div>
              <div className="flex items-center gap-3 mb-4">
                <span className="w-2.5 h-2.5 bg-[#111111] inline-block" />
                <p className="text-xs font-bold tracking-[0.25em] uppercase text-[#111111]">
                  Profil Lembaga
                </p>
              </div>
              <h2 className="text-5xl sm:text-7xl lg:text-8xl font-black uppercase tracking-tighter text-[#111111] leading-none">
                TENTANG KAMI
              </h2>
            </div>
            
            <p className="text-sm sm:text-base text-[#666666] max-w-md leading-relaxed">
              Mengenal lebih dekat Bimbel Artha, visi misi pendidikan, serta perjalanan kami mendidik generasi berprestasi sejak tahun 1997.
            </p>
          </div>
        </motion.div>

        {/* 3 Core Blocks with Scroll Entrance Animations */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-24">
          
          {/* Block 1: Siapa Kami */}
          <motion.div
            initial={{ opacity: 0, y: 60, scale: 0.95 }}
            whileInView={{ opacity: 1, y: 0, scale: 1 }}
            viewport={{ margin: "-50px" }}
            transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}
            className="bg-white p-8 sm:p-10 border border-black/10 flex flex-col justify-between shadow-sm hover:shadow-xl transition-all"
          >
            <div>
              <span className="text-xs font-mono font-bold text-[#888888] tracking-widest block mb-4">
                01 / PROFIL
              </span>
              <h3 className="text-2xl font-black uppercase tracking-tight text-[#111111] mb-4">
                Siapa Kami
              </h3>
              <p className="text-sm text-[#555555] leading-[1.8]">
                {aboutText.description}
              </p>
            </div>
          </motion.div>

          {/* Block 2: Visi Kami */}
          <motion.div
            initial={{ opacity: 0, y: 60, scale: 0.95 }}
            whileInView={{ opacity: 1, y: 0, scale: 1 }}
            viewport={{ margin: "-50px" }}
            transition={{ duration: 0.7, delay: 0.12, ease: [0.22, 1, 0.36, 1] }}
            className="bg-white p-8 sm:p-10 border border-black/10 flex flex-col justify-between shadow-sm hover:shadow-xl transition-all"
          >
            <div>
              <span className="text-xs font-mono font-bold text-[#888888] tracking-widest block mb-4">
                02 / VISI
              </span>
              <h3 className="text-2xl font-black uppercase tracking-tight text-[#111111] mb-4">
                Visi Kami
              </h3>
              <p className="text-sm text-[#555555] leading-[1.8]">
                {aboutText.visi}
              </p>
            </div>
          </motion.div>

          {/* Block 3: Misi Kami */}
          <motion.div
            initial={{ opacity: 0, y: 60, scale: 0.95 }}
            whileInView={{ opacity: 1, y: 0, scale: 1 }}
            viewport={{ margin: "-50px" }}
            transition={{ duration: 0.7, delay: 0.24, ease: [0.22, 1, 0.36, 1] }}
            className="bg-white p-8 sm:p-10 border border-black/10 flex flex-col justify-between shadow-sm hover:shadow-xl transition-all"
          >
            <div>
              <span className="text-xs font-mono font-bold text-[#888888] tracking-widest block mb-4">
                03 / MISI
              </span>
              <h3 className="text-2xl font-black uppercase tracking-tight text-[#111111] mb-4">
                Misi Kami
              </h3>
              <ul className="space-y-2.5">
                {aboutText.misi.map((m, i) => (
                  <li key={i} className="flex items-start gap-2.5 text-xs sm:text-sm text-[#555555] leading-relaxed">
                    <span className="w-1.5 h-1.5 bg-[#2727E6] rounded-full mt-2 shrink-0" />
                    <span>{m}</span>
                  </li>
                ))}
              </ul>
            </div>
          </motion.div>

        </div>

        {/* Timeline Sejarah Perjalanan with Staggered Scroll Animation */}
        <div className="pt-16 border-t border-black/10">
          <motion.div
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ margin: "-50px" }}
            transition={{ duration: 0.7 }}
            className="mb-12"
          >
            <div className="flex items-center gap-3 mb-4">
              <span className="w-2.5 h-2.5 bg-[#111111] inline-block" />
              <p className="text-xs font-bold tracking-[0.25em] uppercase text-[#111111]">
                Milestones
              </p>
            </div>
            <h3 className="text-3xl sm:text-4xl lg:text-5xl font-black uppercase tracking-tight text-[#111111]">
              SEJARAH & PERKEMBANGAN
            </h3>
          </motion.div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8">
            {timeline.map((item, index) => (
              <motion.div
                key={item.year}
                initial={{ opacity: 0, y: 50 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ margin: "-50px" }}
                transition={{ delay: index * 0.1, duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
                className="border-t-2 border-black pt-6"
              >
                <span className="text-2xl font-black text-[#2727E6] tracking-tight block mb-2 font-mono">
                  {item.year}
                </span>
                <h4 className="text-sm font-bold uppercase tracking-tight text-[#111111] mb-2">
                  {item.title}
                </h4>
                <p className="text-xs text-[#666666] leading-relaxed">
                  {item.description}
                </p>
              </motion.div>
            ))}
          </div>
        </div>

      </div>
    </section>
  );
}
