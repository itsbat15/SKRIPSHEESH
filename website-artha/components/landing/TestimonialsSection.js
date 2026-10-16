"use client";
import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";
import { testimonials } from "@/data/siteData";

const colorMap = {
  pink: { bg: "bg-[#FFBAD2]", text: "text-[#111118]" },
  blue: { bg: "bg-[#2727E6]", text: "text-white" },
  yellow: { bg: "bg-[#FFD600]", text: "text-[#111118]" },
  green: { bg: "bg-[#1EAB55]", text: "text-white" },
  orange: { bg: "bg-[#FF6600]", text: "text-white" },
  purple: { bg: "bg-[#8AD9E8]", text: "text-[#111118]" },
  sky: { bg: "bg-[#C5E8F7]", text: "text-[#111118]" },
};

// 16 scattered positions for a massive overlapping collage effect
const cardConfigs = [
  { top: "2%", left: "2%", rotate: -3, z: 10, width: "w-[380px]", textSize: "text-2xl sm:text-3xl leading-tight" },
  { top: "5%", left: "30%", rotate: 2, z: 20, width: "w-[320px]", textSize: "text-lg leading-snug" },
  { top: "0%", left: "60%", rotate: -2, z: 15, width: "w-[420px]", textSize: "text-2xl sm:text-4xl leading-[1.1]" },
  { top: "20%", left: "10%", rotate: 4, z: 30, width: "w-[350px]", textSize: "text-xl leading-snug" },
  { top: "22%", left: "42%", rotate: -3, z: 40, width: "w-[380px]", textSize: "text-2xl leading-tight" },
  { top: "28%", left: "70%", rotate: 3, z: 25, width: "w-[300px]", textSize: "text-lg leading-relaxed" },
  { top: "45%", left: "5%", rotate: -2, z: 50, width: "w-[400px]", textSize: "text-3xl leading-tight" },
  { top: "48%", left: "35%", rotate: 3, z: 60, width: "w-[330px]", textSize: "text-xl leading-snug" },
  { top: "52%", left: "65%", rotate: -4, z: 55, width: "w-[360px]", textSize: "text-2xl leading-tight" },
  { top: "68%", left: "15%", rotate: 2, z: 70, width: "w-[300px]", textSize: "text-lg leading-snug" },
  { top: "70%", left: "45%", rotate: -3, z: 80, width: "w-[400px]", textSize: "text-3xl leading-tight" },
  { top: "65%", left: "75%", rotate: 5, z: 65, width: "w-[280px]", textSize: "text-base leading-relaxed" },
  { top: "12%", left: "80%", rotate: -5, z: 5, width: "w-[300px]", textSize: "text-xl leading-snug" },
  { top: "38%", left: "25%", rotate: 6, z: 45, width: "w-[280px]", textSize: "text-base leading-relaxed" },
  { top: "8%", left: "48%", rotate: -1, z: 35, width: "w-[340px]", textSize: "text-xl leading-snug" },
  { top: "60%", left: "38%", rotate: 1, z: 75, width: "w-[380px]", textSize: "text-2xl leading-tight" },
];

export default function TestimonialsSection() {
  // Duplicate testimonials to fill the collage
  const allTestimonials = [...testimonials, ...testimonials];

  return (
    <section className="superhi-section bg-[#1EAB55] mt-4 overflow-hidden relative">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10 pt-10 pb-20">
        
        {/* Header */}
        <motion.div 
          initial="hidden"
          whileInView="show"
          viewport={{ once: true, amount: 0.5 }}
          variants={{
            hidden: { opacity: 0 },
            show: {
              opacity: 1,
              transition: { staggerChildren: 0.1 }
            }
          }}
          className="text-center mb-16 relative z-50 flex flex-col items-center"
        >
          <motion.h2
            variants={{ hidden: { opacity: 0, y: 50 }, show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 100, damping: 15 } } }}
            className="text-4xl sm:text-5xl lg:text-7xl font-black uppercase text-white mb-6 tracking-tighter drop-shadow-md border-[4px] border-[#111118] bg-[#FFD600] text-[#111118] p-4 -rotate-1 shadow-[8px_8px_0_0_#111118]"
          >
            Dipercaya Ribuan Keluarga
          </motion.h2>
          <motion.p
            variants={{ hidden: { opacity: 0, y: 50 }, show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 100, damping: 15 } } }}
            className="text-xl sm:text-2xl text-white font-black uppercase tracking-widest bg-[#111118] px-6 py-3 shadow-[6px_6px_0_0_rgba(255,255,255,1)]"
          >
            Apa kata orang tua dan siswa tentang Bimbel Artha?
          </motion.p>
        </motion.div>

        {/* Desktop: Overlapping scattered cards */}
        <div className="hidden lg:block relative mx-auto" style={{ height: "1100px", maxWidth: "1200px" }}>
          {allTestimonials.map((t, i) => {
            const config = cardConfigs[i % cardConfigs.length];
            const theme = colorMap[t.color] || colorMap.yellow;
            return (
              <motion.div
                key={i}
                initial={{ y: 200, opacity: 0, scale: 0.8, rotate: 0 }}
                whileInView={{ y: 0, opacity: 1, scale: 1, rotate: config.rotate }}
                viewport={{ once: true, amount: 0.1 }}
                transition={{ duration: 0.8, delay: (i % 8) * 0.1, type: "spring", bounce: 0.4 }}
                whileHover={{ scale: 1.05, rotate: 0, zIndex: 100 }}
                className={`absolute ${theme.bg} border-[3px] border-[#111118] p-8 cursor-pointer shadow-[8px_8px_0_0_#111118] hover:shadow-none transition-all ${config.width}`}
                style={{
                  top: config.top,
                  left: config.left,
                  zIndex: config.z,
                }}
              >
                <p className={`${theme.text} ${config.textSize} font-sans font-bold mb-8 tracking-tight`}>
                  "{t.text}"
                </p>
                <div className="flex items-center gap-3">
                  <div className={`w-12 h-12 flex items-center justify-center text-lg font-black border-[3px] border-[#111118] ${theme.bg === 'bg-[#2727E6]' || theme.bg === 'bg-[#1EAB55]' || theme.bg === 'bg-[#FF6600]' ? 'bg-white text-[#111118]' : 'bg-[#111118] text-white'}`}>
                    {t.name.charAt(0)}
                  </div>
                  <div>
                    <p className={`text-sm font-black uppercase tracking-widest ${theme.text}`}>{t.name}</p>
                    <p className={`text-xs font-bold uppercase tracking-widest opacity-80 ${theme.text}`}>{t.role}</p>
                  </div>
                </div>
              </motion.div>
            );
          })}
        </div>

        {/* Mobile/Tablet: Horizontal/Vertical scrolling cards */}
        <motion.div 
          initial="hidden"
          whileInView="show"
          viewport={{ once: true, amount: 0.1 }}
          variants={{
            hidden: { opacity: 0 },
            show: {
              opacity: 1,
              transition: { staggerChildren: 0.1 }
            }
          }}
          className="lg:hidden flex flex-col gap-6 sm:flex-row sm:flex-wrap sm:justify-center"
        >
          {allTestimonials.slice(0, 8).map((t, i) => {
            const theme = colorMap[t.color] || colorMap.yellow;
            // Alternate slight rotation on mobile for a fun feel
            const rot = i % 2 === 0 ? 'rotate-1' : '-rotate-1';
            return (
              <motion.div
                key={i}
                variants={{
                  hidden: { opacity: 0, scale: 0.8, y: 50 },
                  show: { opacity: 1, scale: 1, y: 0, transition: { type: "spring", stiffness: 100, damping: 15 } }
                }}
                className={`${theme.bg} border-[3px] border-[#111118] p-6 sm:p-8 w-full sm:w-[calc(50%-12px)] shadow-[8px_8px_0_0_#111118] transform ${rot}`}
              >
                <p className={`${theme.text} text-xl sm:text-2xl font-sans font-bold leading-tight mb-6 tracking-tight`}>
                  "{t.text}"
                </p>
                <div className="flex items-center gap-3">
                  <div className={`w-12 h-12 flex items-center justify-center text-lg font-black border-[3px] border-[#111118] ${theme.bg === 'bg-[#2727E6]' || theme.bg === 'bg-[#1EAB55]' || theme.bg === 'bg-[#FF6600]' ? 'bg-white text-[#111118]' : 'bg-[#111118] text-white'}`}>
                    {t.name.charAt(0)}
                  </div>
                  <div>
                    <p className={`text-sm font-black uppercase tracking-widest ${theme.text}`}>{t.name}</p>
                    <p className={`text-xs font-bold uppercase tracking-widest opacity-80 ${theme.text}`}>{t.role}</p>
                  </div>
                </div>
              </motion.div>
            );
          })}
        </motion.div>

        {/* CTA */}
        <motion.div
          initial={{ y: 50, opacity: 0 }}
          whileInView={{ y: 0, opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5, delay: 0.3, type: "spring", stiffness: 100 }}
          className="mt-16 flex justify-center relative z-50"
        >
          <button
            className="px-10 py-5 bg-[#FFD600] text-[#111118] border-[3px] border-[#111118] font-black text-xl uppercase tracking-widest hover:translate-y-1 transition-all flex items-center gap-2 shadow-[6px_6px_0_0_#111118] hover:shadow-none"
            onClick={() => {
              const el = document.querySelector("#faq");
              if (el) el.scrollIntoView({ behavior: "smooth" });
            }}
          >
            Punya pertanyaan?
            <ArrowRight size={24} />
          </button>
        </motion.div>
      </div>
    </section>
  );
}
