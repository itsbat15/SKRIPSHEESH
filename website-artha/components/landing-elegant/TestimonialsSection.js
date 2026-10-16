"use client";
import { motion } from "framer-motion";
import { Quote, Star } from "lucide-react";
import { testimonials } from "@/data/siteData";

export default function TestimonialsSection() {
  return (
    <section className="py-24 sm:py-32 bg-[#0F172A] text-white overflow-hidden border-b border-white/10">
      <div className="max-w-[1400px] mx-auto px-6 sm:px-12 lg:px-20">
        
        {/* Section Header */}
        <div className="mb-20">
          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-8 pb-10 border-b border-white/10">
            <div>
              <div className="flex items-center gap-3 mb-4">
                <span className="w-2.5 h-2.5 bg-[#F59E0B] inline-block" />
                <p className="text-xs font-bold tracking-[0.25em] uppercase text-[#F59E0B]">
                  Kisah & Pengalaman
                </p>
              </div>
              <motion.h2
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}
                className="text-5xl sm:text-7xl lg:text-8xl font-black uppercase tracking-tighter text-white leading-none"
              >
                TESTIMONI SISWA
              </motion.h2>
            </div>
            
            <p className="text-sm sm:text-base text-white/60 max-w-md leading-relaxed">
              Pengalaman nyata dari siswa dan orang tua yang telah belajar dan meraih prestasi bersama Bimbel Artha.
            </p>
          </div>
        </div>

        {/* 8 Testimonials Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {testimonials.map((t, idx) => {
            const num = String(idx + 1).padStart(2, "0");

            return (
              <motion.div
                key={idx}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: idx * 0.05, duration: 0.6 }}
                className="bg-[#1E293B] p-8 border border-white/10 flex flex-col justify-between hover:border-[#2563EB] transition-colors"
              >
                <div>
                  <div className="flex items-center justify-between mb-6">
                    <span className="text-xs font-mono font-bold text-white/40">
                      NO {num}
                    </span>
                    <div className="flex items-center gap-1 text-[#F59E0B]">
                      {[...Array(5)].map((_, i) => (
                        <Star key={i} size={11} fill="#F59E0B" />
                      ))}
                    </div>
                  </div>

                  <p className="text-xs sm:text-sm text-white/85 leading-[1.8] mb-6 font-normal">
                    &ldquo;{t.text}&rdquo;
                  </p>
                </div>

                <div className="pt-4 border-t border-white/10 flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-[#2563EB]/30 text-[#60A5FA] flex items-center justify-center font-bold text-xs border border-[#2563EB]/50">
                    {t.name.charAt(0)}
                  </div>
                  <div>
                    <h4 className="text-xs font-bold text-white uppercase tracking-tight">
                      {t.name}
                    </h4>
                    <p className="text-[10px] text-white/50 font-mono">
                      {t.role}
                    </p>
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
