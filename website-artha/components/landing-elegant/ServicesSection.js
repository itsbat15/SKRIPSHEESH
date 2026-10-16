"use client";
import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";
import Image from "next/image";
import { programs } from "@/data/siteData";

function StaggeredTextRoll({ text }) {
  const letters = text.split("");

  return (
    <div className="relative overflow-hidden inline-flex items-center font-extrabold tracking-[0.15em]">
      {/* Default Row */}
      <span className="inline-flex">
        {letters.map((char, i) => (
          <span
            key={i}
            className="inline-block transition-transform duration-300 ease-out group-hover:-translate-y-full"
            style={{ transitionDelay: `${i * 20}ms` }}
          >
            {char === " " ? "\u00A0" : char}
          </span>
        ))}
      </span>

      {/* Hover Row */}
      <span className="absolute inset-0 inline-flex">
        {letters.map((char, i) => (
          <span
            key={i}
            className="inline-block translate-y-full transition-transform duration-300 ease-out group-hover:translate-y-0 text-white"
            style={{ transitionDelay: `${i * 20}ms` }}
          >
            {char === " " ? "\u00A0" : char}
          </span>
        ))}
      </span>
    </div>
  );
}

export default function ServicesSection() {
  return (
    <section id="layanan" className="py-24 sm:py-32 bg-[#FFFFFF] text-[#0F172A] border-b border-[#0F172A]/10 overflow-hidden">
      <div className="max-w-[1400px] mx-auto px-6 sm:px-12 lg:px-20">
        
        {/* Section Header */}
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ margin: "-100px" }}
          transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
          className="mb-20"
        >
          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-8 pb-10 border-b border-[#0F172A]/10">
            <div>
              <div className="flex items-center gap-3 mb-4">
                <span className="w-2.5 h-2.5 bg-[#2563EB] inline-block" />
                <p className="text-xs font-bold tracking-[0.25em] uppercase text-[#2563EB]">
                  Program Bimbingan Belajar
                </p>
              </div>
              <h2 className="text-5xl sm:text-7xl lg:text-8xl font-black uppercase tracking-tighter text-[#0F172A] leading-none">
                PROGRAM POPULER
              </h2>
            </div>
            
            <p className="text-sm sm:text-base text-[#475569] max-w-md leading-relaxed">
              Pilihan program bimbingan belajar berkualitas yang disesuaikan dengan kurikulum sekolah dan kebutuhan akademik siswa.
            </p>
          </div>
        </motion.div>

        {/* 5 Programs Stack */}
        <div className="space-y-8 mb-20">
          {programs.map((prog, index) => {
            return (
              <motion.div
                key={prog.id}
                initial={{ opacity: 0, y: 60, scale: 0.97 }}
                whileInView={{ opacity: 1, y: 0, scale: 1 }}
                viewport={{ margin: "-50px" }}
                transition={{ duration: 0.7, delay: index * 0.08, ease: [0.22, 1, 0.36, 1] }}
                className="bg-[#F8FAFC] border border-[#0F172A]/10 p-8 sm:p-12 transition-all duration-300 hover:shadow-xl hover:border-[#2563EB]/40"
              >
                <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                  
                  {/* Left: Program Title & Description */}
                  <div className="lg:col-span-5">
                    <h3 className="text-4xl sm:text-5xl lg:text-6xl font-black uppercase tracking-tight mb-4 text-[#0F172A]">
                      {prog.title}
                    </h3>

                    <p className="text-sm sm:text-base text-[#475569] leading-[1.8]">
                      {prog.description}
                    </p>
                  </div>

                  {/* Center: Subjects List (Artha Navy Solid Bullets) */}
                  <div className="lg:col-span-4 border-t lg:border-t-0 lg:border-l border-[#0F172A]/10 pt-6 lg:pt-0 lg:pl-8">
                    <span className="text-[10px] font-bold uppercase tracking-[0.2em] text-[#2563EB] block mb-3">
                      MATERI & FOKUS BELAJAR
                    </span>
                    <ul className="space-y-2.5">
                      {prog.subjects && prog.subjects.map((subj, i) => (
                        <li key={i} className="flex items-center gap-2.5 text-xs sm:text-sm text-[#0F172A] font-medium">
                          <span className="w-1.5 h-1.5 bg-[#0F172A] rounded-full shrink-0" />
                          <span>{subj}</span>
                        </li>
                      ))}
                    </ul>
                  </div>

                  {/* Right: Button */}
                  <div className="lg:col-span-3 flex justify-start lg:justify-end">
                    <a
                      href={`https://wa.me/6285102233666?text=Halo%20saya%20ingin%20tanya%20detail%20program%20${encodeURIComponent(prog.title)}`}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="group relative inline-flex items-center justify-between w-full sm:w-60 h-14 px-6 border-b-2 border-[#0F172A] bg-transparent text-[#0F172A] text-xs font-bold uppercase tracking-widest transition-all duration-500 ease-out hover:bg-[#0F172A] hover:text-white hover:border-[#0F172A] hover:shadow-md"
                    >
                      <ArrowRight size={16} className="hidden group-hover:block transition-transform duration-300 transform group-hover:scale-110 text-[#2563EB]" />
                      <StaggeredTextRoll text="DETAIL PROGRAM" />
                      <ArrowRight size={16} className="block group-hover:hidden transition-all duration-300" />
                    </a>
                  </div>

                </div>
              </motion.div>
            );
          })}
        </div>

      </div>
    </section>
  );
}
