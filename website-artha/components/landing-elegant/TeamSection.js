"use client";
import { motion } from "framer-motion";
import Image from "next/image";
import { teachers } from "@/data/siteData";

export default function TeamSection() {
  const marqueeTeachers = [...teachers, ...teachers, ...teachers, ...teachers];

  return (
    <section id="tim" className="py-24 sm:py-32 bg-[#FFFFFF] text-[#111118] overflow-hidden border-b border-black/10">
      <div className="max-w-[1400px] mx-auto px-6 sm:px-12 lg:px-20 mb-16">
        
        {/* Section Header */}
        <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-8 pb-10 border-b border-black/10">
          <div>
            <div className="flex items-center gap-3 mb-4">
              <span className="w-3 h-3 bg-[#2727E6] inline-block" />
              <p className="text-xs font-bold tracking-[0.25em] uppercase text-[#2727E6]">
                Pendidik & Mentor
              </p>
            </div>
            <motion.h2
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}
              className="text-5xl sm:text-7xl lg:text-8xl font-black uppercase tracking-tighter text-[#111118] leading-none"
            >
              TIM PENGAJAR KAMI
            </motion.h2>
          </div>
          
          <p className="text-sm sm:text-base text-[#555555] max-w-md leading-relaxed">
            Pengajar berpengalaman dan berdedikasi untuk membantu siswa meraih prestasi di setiap jenjang pendidikan.
          </p>
        </div>

      </div>

      {/* Infinite Auto-scrolling Marquee Row (Clean cards without NO number badges) */}
      <div className="w-full overflow-hidden">
        <motion.div
          className="flex gap-6 w-max px-6 py-4"
          animate={{ x: ["0%", "-50%"] }}
          transition={{ repeat: Infinity, ease: "linear", duration: 40 }}
        >
          {marqueeTeachers.map((teacher, index) => {
            return (
              <div
                key={`${teacher.name}-${index}`}
                className="group flex flex-col w-[230px] sm:w-[270px] shrink-0 bg-[#F4F7FE] border border-black/10 p-4 rounded-xl shadow-sm hover:shadow-xl transition-all duration-300"
              >
                {/* Full Color Photo Container (No NO number badges) */}
                <div className="relative w-full aspect-[3/4] bg-white mb-4 overflow-hidden rounded-lg border border-black/10">
                  <Image
                    src={teacher.image}
                    alt={teacher.name}
                    fill
                    className="object-cover object-top group-hover:scale-105 transition-all duration-500 ease-out"
                  />
                </div>

                {/* Teacher Info */}
                <h3 className="text-base font-black uppercase tracking-tight text-[#111118] group-hover:text-[#2727E6] transition-colors">
                  {teacher.name}
                </h3>
                <p className="text-xs text-[#2727E6] font-bold mt-0.5">
                  {teacher.role}
                </p>
                <p className="text-[10px] text-[#666666] font-mono mt-1 pt-2 border-t border-black/10">
                  {teacher.branch}
                </p>
              </div>
            );
          })}
        </motion.div>
      </div>

    </section>
  );
}
