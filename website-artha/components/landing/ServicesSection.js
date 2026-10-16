"use client";
import { motion } from "framer-motion";
import { ArrowRight, Pencil, BookOpen, Globe, Atom, Languages } from "lucide-react";
import { programs } from "@/data/siteData";

const iconMap = {
  Pencil, BookOpen, Globe, Atom, Languages,
};

const cardStyles = [
  {
    bgRight: "bg-[#8AD9E8]", // light blue
    textRight: "text-[#111118]",
    buttonRight: "bg-white text-[#111118] hover:bg-white/90",
    iconBg: "bg-[#2727E6]",
    iconColor: "text-white",
  },
  {
    bgRight: "bg-[#1EAB55]", // green
    textRight: "text-white",
    buttonRight: "bg-white text-[#111118] hover:bg-white/90",
    iconBg: "bg-[#2727E6]",
    iconColor: "text-white",
  },
  {
    bgRight: "bg-[#FFBAD2]", // pink
    textRight: "text-[#111118]",
    buttonRight: "bg-white text-[#111118] hover:bg-white/90",
    iconBg: "bg-[#2727E6]",
    iconColor: "text-white",
  },
  {
    bgRight: "bg-[#FFD600]", // yellow
    textRight: "text-[#111118]",
    buttonRight: "bg-white text-[#111118] hover:bg-white/90",
    iconBg: "bg-[#2727E6]",
    iconColor: "text-white",
  },
  {
    bgRight: "bg-[#2727E6]", // blue
    textRight: "text-white",
    buttonRight: "bg-white text-[#111118] hover:bg-white/90",
    iconBg: "bg-[#FFD600]",
    iconColor: "text-[#111118]",
  }
];

export default function ServicesSection() {
  return (
    <section id="layanan" className="py-20 sm:py-28 bg-[#F5F7FF]">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Header - The SuperHi way style */}
        <div className="text-center mb-12 sm:mb-16">
          <motion.h2
            initial={{ y: 20, opacity: 0 }}
            whileInView={{ y: 0, opacity: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
            className="text-5xl sm:text-6xl lg:text-7xl font-normal text-[#111118] tracking-tight mb-8"
          >
            Program Populer
          </motion.h2>

          {/* Decorative Pills */}
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            whileInView={{ y: 0, opacity: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, delay: 0.1 }}
            className="flex flex-wrap items-center justify-center gap-3"
          >
            {programs.map((prog, idx) => {
              const dots = ["bg-[#8AD9E8]", "bg-[#1EAB55]", "bg-[#FFD600]", "bg-[#FFBAD2]", "bg-[#2727E6]"];
              return (
                <div key={idx} className="bg-white px-4 py-2 rounded-full shadow-sm flex items-center gap-2 border border-[#111118]/5">
                  <span className={`w-2.5 h-2.5 rounded-full ${dots[idx % dots.length]}`} />
                  <span className="text-[15px] font-medium text-[#111118]">{prog.title}</span>
                </div>
              );
            })}
          </motion.div>
        </div>

        {/* Big Cards Stack */}
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
          className="space-y-12 sm:space-y-16"
        >
          {programs.map((program, index) => {
            const style = cardStyles[index % cardStyles.length];
            const IconComp = iconMap[program.icon] || BookOpen;

            return (
              <motion.div
                key={program.id}
                variants={{
                  hidden: { opacity: 0, x: index % 2 === 0 ? -100 : 100 },
                  show: { opacity: 1, x: 0, transition: { type: "spring", stiffness: 100, damping: 15 } }
                }}
                className="w-full flex flex-col md:flex-row min-h-[320px] border-[4px] border-[#111118] bg-white shadow-[12px_12px_0_0_#111118] hover:translate-x-2 hover:-translate-y-2 hover:shadow-[16px_16px_0_0_#111118] transition-all duration-300 group"
              >
                {/* Left Side: Abstract Geometric Art */}
                <div className="w-full md:w-1/2 relative min-h-[250px] md:min-h-full border-b-[4px] md:border-b-0 md:border-r-[4px] border-[#111118] overflow-hidden">
                  {index % 2 === 0 ? (
                    // Grid Style Abstract (like Card 1 in screenshot)
                    <div className="absolute inset-0 flex">
                      <div className="w-1/2 h-full flex flex-col border-r-[4px] border-[#111118]">
                        <div className="h-2/3 bg-[#FFD600] border-b-[4px] border-[#111118]" />
                        <div className="h-1/3 bg-[#1EAB55] flex">
                          <div className="w-1/3 bg-[#1EAB55] border-r-[4px] border-[#111118]" />
                          <div className="w-2/3 bg-[#2727E6]" />
                        </div>
                      </div>
                      <div className="w-1/2 h-full flex flex-col">
                        <div className="h-1/3 bg-[#FFBAD2] border-b-[4px] border-[#111118]" />
                        <div className="h-1/6 bg-[#FF3B30] border-b-[4px] border-[#111118]" />
                        <div className="h-1/6 bg-[#8AD9E8] border-b-[4px] border-[#111118]" />
                        <div className="h-1/3 bg-[#FFD600]" />
                      </div>
                    </div>
                  ) : (
                    // Circles Style Abstract (like Card 2 in screenshot)
                    <div className="absolute inset-0 flex">
                      <div className="w-1/2 h-full bg-[#FFD600] relative overflow-hidden border-r-[4px] border-[#111118]">
                        <div className="absolute right-0 top-1/2 -translate-y-1/2 w-[150%] aspect-square bg-[#1EAB55] border-[4px] border-[#111118] rounded-full translate-x-1/2" />
                      </div>
                      <div className="w-1/2 h-full bg-[#8AD9E8] relative overflow-hidden">
                        <div className="absolute left-0 top-1/2 -translate-y-1/2 w-[150%] aspect-square bg-[#2727E6] border-[4px] border-[#111118] rounded-full -translate-x-1/2" />
                      </div>
                    </div>
                  )}
                  {/* Hover overlay element */}
                  <div className="absolute inset-0 bg-[#111118]/0 group-hover:bg-[#111118]/10 transition-colors" />
                </div>

                {/* Right Side: Content */}
                <div className={`w-full md:w-1/2 p-8 sm:p-12 flex flex-col justify-center ${style.bgRight}`}>
                  <h3 className={`text-4xl sm:text-5xl lg:text-6xl font-black uppercase ${style.textRight} tracking-tighter leading-[1] mb-6`}>
                    {program.title}
                  </h3>
                  
                  <div className="bg-white border-[3px] border-[#111118] shadow-[4px_4px_0_0_#111118] p-4 mb-8 -rotate-1">
                    <p className={`text-base sm:text-lg font-bold uppercase tracking-widest text-[#111118] leading-relaxed`}>
                      {program.subtitle} - {program.description}
                    </p>
                  </div>

                  <div className="mt-auto">
                    <button className={`inline-flex items-center justify-center gap-2 px-8 py-4 border-[3px] border-[#111118] text-lg font-black uppercase tracking-widest transition-transform hover:-translate-y-1 shadow-[4px_4px_0_0_#111118] hover:shadow-none ${style.buttonRight}`}>
                      Detail Program
                      <ArrowRight size={24} />
                    </button>
                  </div>
                </div>
              </motion.div>
            );
          })}
        </motion.div>

      </div>
    </section>
  );
}
