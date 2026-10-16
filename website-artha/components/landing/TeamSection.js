"use client";
import { motion } from "framer-motion";
import Image from "next/image";
import { teachers } from "@/data/siteData";

export default function TeamSection() {
  // Duplicate teachers to create a seamless infinite marquee effect
  const marqueeTeachers = [...teachers, ...teachers, ...teachers, ...teachers, ...teachers];

  return (
    <section id="tim" className="superhi-section bg-[#FFD600] my-8 sm:my-12">
      <div className="max-w-[1440px] mx-auto">
        
        {/* Header */}
        <div className="mb-10 text-center">
          <h2 className="text-4xl sm:text-5xl font-extrabold text-[#111118] mb-2 tracking-tight">
            Tim Pengajar Kami
          </h2>
          <p className="text-sm sm:text-base text-[#111118]/80 font-medium max-w-2xl mx-auto">
            Pengajar berpengalaman dan berdedikasi untuk membantu siswa meraih prestasi di setiap jenjang pendidikan.
          </p>
        </div>

      </div>

      {/* Infinite Marquee moving slowly to the RIGHT */}
      {/* We start at -50% and move to 0% so it flows rightwards. Increased duration to slow it down even more. */}
      {/* Added py-8 to prevent the tilted cards from being cropped by overflow */}
      <div className="w-full overflow-hidden">
        <motion.div 
          className="flex gap-6 sm:gap-8 w-max px-4 py-8"
          animate={{ x: ["-50%", "0%"] }}
          transition={{ repeat: Infinity, ease: "linear", duration: 240 }}
        >
          {marqueeTeachers.map((teacher, index) => {
            const bgColors = ["bg-[#7EC8E3]", "bg-[#FFB5A7]", "bg-[#B8F0D8]", "bg-[#ECEAFC]", "bg-white"];
            const cardBg = bgColors[index % bgColors.length];
            
            // Slightly tilt the cards like in the reference image
            const rotations = ["-rotate-1", "rotate-2", "rotate-0", "-rotate-2", "rotate-1"];
            const tilt = rotations[index % rotations.length];

            return (
              <div
                key={`${teacher.name}-${index}`}
                className={`shrink-0 flex flex-col w-[280px] sm:w-[300px] border-[3px] border-[#111118] shadow-[6px_6px_0_0_#111118] transition-transform duration-300 hover:scale-105 hover:z-50 ${cardBg} p-5 relative group ${tilt}`}
              >
                {/* Top: Large Vertical Photo Container */}
                <div className="relative w-full h-[220px] shrink-0 border-[3px] border-[#111118] bg-white mb-5">
                  <Image
                    src={teacher.image}
                    alt={teacher.name}
                    fill
                    className="object-cover object-top"
                  />
                  {/* Yellow Sticker */}
                  <div className="absolute -bottom-3 -left-3 bg-[#FFD600] border-[2px] border-[#111118] px-2 py-0.5 font-black text-xs uppercase -rotate-6 shadow-[2px_2px_0_0_#111118] z-10 whitespace-nowrap">
                    EST 1997
                  </div>
                </div>

                {/* Content Container */}
                <div className="flex flex-col flex-grow justify-between">
                  <div>
                    <h3 className="text-2xl font-black text-[#111118] uppercase tracking-tighter mb-0.5">
                      {teacher.name}
                    </h3>
                    <p className="text-sm font-bold text-[#111118]/70 mb-3">
                      {teacher.branch}
                    </p>
                    <p className="text-sm text-[#111118] font-medium leading-relaxed">
                      Berdedikasi membangun <span className="bg-[#FF6600] text-white px-1 font-bold">pengalaman interaktif</span> melampaui kurikulum. Bimbingan murni untuk potensi siswa.
                    </p>
                  </div>

                  <div className="mt-5">
                    <span className="inline-block bg-[#1EAB55] border-[2px] border-[#111118] text-[#111118] font-black uppercase tracking-widest text-xs px-4 py-2 shadow-[2px_2px_0_0_#111118]">
                      {teacher.role}
                    </span>
                  </div>
                </div>
              </div>
            );
          })}
        </motion.div>
      </div>
    </section>
  );
}
