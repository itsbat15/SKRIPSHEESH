"use client";
import { motion } from "framer-motion";
import { aboutText, timeline } from "@/data/siteData";
import { Calendar } from "lucide-react";

const HandDrawnOval = ({ color = "#FF6600" }) => (
  <svg
    viewBox="0 0 200 100"
    className="absolute inset-0 w-full h-full overflow-visible pointer-events-none scale-110"
    preserveAspectRatio="none"
  >
    <path
      d="M10,50 C10,10 190,5 190,50 C190,95 10,90 10,50 Z"
      fill="none"
      stroke={color}
      strokeWidth="4"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
    <path
      d="M5,55 C5,15 195,10 195,55 C195,95 5,90 5,55"
      fill="none"
      stroke={color}
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      opacity="0.5"
    />
  </svg>
);

export default function AboutSection() {
  return (
    <section id="tentang" className="pt-10 pb-20 sm:pt-16 sm:pb-32 bg-[#F5F7FF] overflow-hidden">
      <div className="max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Diagram Layout */}
        <div className="flex flex-col items-center mb-24">
          
          {/* Main Title Node */}
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            whileInView={{ scale: 1, opacity: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, type: "spring" }}
            className="relative inline-block text-center z-10 mb-2"
          >
            <HandDrawnOval color="#FF6600" />
            <div className="px-16 py-12 sm:px-24 sm:py-16">
              <h2 className="text-4xl sm:text-5xl lg:text-6xl font-normal text-[#111118] leading-tight tracking-tight">
                Tentang<br />Bimbel Artha
              </h2>
            </div>
          </motion.div>

          {/* Branching Arrows (Desktop/Tablet) */}
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, delay: 0.3 }}
            className="hidden md:block w-full max-w-[1000px] h-[160px] relative -mt-16 z-0"
          >
            <svg viewBox="0 0 1000 200" className="w-full h-full overflow-visible pointer-events-none">
              {/* Left arrow (Visi) */}
              <path d="M300,-10 Q200,60 160,170" fill="none" stroke="#FF6600" strokeWidth="5" strokeLinecap="round" />
              <path d="M145,150 L160,170 L180,155" fill="none" stroke="#FF6600" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round" />
              
              {/* Center arrow (Siapa Kami) */}
              <path d="M500,70 Q500,120 500,180" fill="none" stroke="#FF6600" strokeWidth="5" strokeLinecap="round" />
              <path d="M485,165 L500,180 L515,165" fill="none" stroke="#FF6600" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round" />
              
              {/* Right arrow (Misi) */}
              <path d="M700,-10 Q800,60 840,170" fill="none" stroke="#FF6600" strokeWidth="5" strokeLinecap="round" />
              <path d="M820,155 L840,170 L855,150" fill="none" stroke="#FF6600" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          </motion.div>

          {/* Mobile Arrows (Vertical) - Hidden on md+ */}
          <div className="md:hidden w-10 h-16 flex justify-center items-center my-4 opacity-50">
             <div className="w-1 h-full bg-[#FF6600] rounded-full relative">
               <div className="absolute -bottom-2 left-1/2 -translate-x-1/2 w-4 h-4 border-b-4 border-r-4 border-[#FF6600] rotate-45" />
             </div>
          </div>

          {/* Sub Nodes Grid */}
          <motion.div 
            initial="hidden"
            whileInView="show"
            viewport={{ once: true, amount: 0.2 }}
            variants={{
              hidden: { opacity: 0 },
              show: {
                opacity: 1,
                transition: { staggerChildren: 0.2 }
              }
            }}
            className="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-8 w-full z-10 relative"
          >
            
            {/* Visi */}
            <motion.div
              variants={{
                hidden: { opacity: 0, y: 100 },
                show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 100, damping: 15 } }
              }}
              className="text-center flex flex-col items-center bg-white border-[3px] border-[#111118] p-8 shadow-[8px_8px_0_0_#111118] hover:translate-y-2 hover:shadow-none transition-all"
            >
              <div className="relative inline-block mb-6">
                <h3 className="text-3xl font-black uppercase tracking-widest px-6 py-3 text-white bg-[#2727E6] border-[3px] border-[#111118] transform -skew-x-6 shadow-[4px_4px_0_0_#111118]">
                  Visi Kami
                </h3>
              </div>
              <p className="text-base font-bold text-[#111118]/80 leading-relaxed text-center px-4 uppercase tracking-widest">
                {aboutText.visi}
              </p>
            </motion.div>

            {/* Siapa Kami */}
            <motion.div
              variants={{
                hidden: { opacity: 0, y: 100 },
                show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 100, damping: 15 } }
              }}
              className="text-center flex flex-col items-center bg-white border-[3px] border-[#111118] p-8 shadow-[8px_8px_0_0_#111118] hover:translate-y-2 hover:shadow-none transition-all"
            >
              <div className="relative inline-block mb-6">
                <h3 className="text-3xl font-black uppercase tracking-widest px-6 py-3 text-[#111118] bg-[#FFD600] border-[3px] border-[#111118] transform -skew-x-6 shadow-[4px_4px_0_0_#111118]">
                  Siapa Kami
                </h3>
              </div>
              <p className="text-base font-bold text-[#111118]/80 leading-relaxed text-center px-4 uppercase tracking-widest">
                {aboutText.description}
              </p>
            </motion.div>

            {/* Misi */}
            <motion.div
              variants={{
                hidden: { opacity: 0, y: 100 },
                show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 100, damping: 15 } }
              }}
              className="text-center flex flex-col items-center bg-white border-[3px] border-[#111118] p-8 shadow-[8px_8px_0_0_#111118] hover:translate-y-2 hover:shadow-none transition-all"
            >
              <div className="relative inline-block mb-6">
                <h3 className="text-3xl font-black uppercase tracking-widest px-6 py-3 text-white bg-[#1EAB55] border-[3px] border-[#111118] transform -skew-x-6 shadow-[4px_4px_0_0_#111118]">
                  Misi Kami
                </h3>
              </div>
              <ul className="text-base font-bold text-[#111118]/80 leading-relaxed text-left px-4 list-disc pl-8 space-y-2 uppercase tracking-widest">
                {aboutText.misi.map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>
            </motion.div>

          </motion.div>
        </div>

        {/* Timeline - Neo Brutalist Style */}
        <div className="mt-40 relative pb-20">
          
          {/* Timeline Title Block */}
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            whileInView={{ y: 0, opacity: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
            className="relative mx-auto bg-[#FEFDF9] border-[3px] border-[#111118] shadow-[8px_8px_0_0_#111118] px-6 py-10 sm:p-12 max-w-3xl text-center mb-32 z-10"
          >
            <div className="absolute -top-4 left-1/2 -translate-x-1/2 bg-[#8AD9E8] border-[2px] border-[#111118] px-5 py-1.5 text-xs sm:text-sm font-black uppercase tracking-widest text-[#111118]">
              Sejarah Kami
            </div>
            <h3 className="text-4xl sm:text-5xl font-black text-[#111118] uppercase tracking-tight leading-[1.1]">
              Perjalanan & Pencapaian<br />Bimbel Artha
            </h3>
          </motion.div>

          <div className="relative max-w-5xl mx-auto px-4 sm:px-0">
            {/* Center Line (Hidden on very small screens, placed left on mobile, center on md+) */}
            <motion.div 
              initial={{ height: 0 }}
              whileInView={{ height: "100%" }}
              viewport={{ once: true }}
              transition={{ duration: 1.5, ease: "easeOut" }}
              className="absolute left-[34px] md:left-1/2 top-0 w-0.5 bg-[#111118] md:-translate-x-1/2 z-0" 
            />

            {/* Timeline Items */}
            {timeline.map((item, index) => {
              const isEven = index % 2 === 0;
              // Add a slight rotation for playfulness, alternating
              const rotation = isEven ? "md:rotate-1" : "md:-rotate-1";
              
              // If isEven, card is on the LEFT side of the center line (because of flex-row-reverse).
              // We want to push it further left, away from the center line, so we add margin-right.
              const marginClass = isEven ? 'md:mr-16 lg:mr-24' : 'md:ml-16 lg:ml-24';
              const slideInit = isEven ? -50 : 50;

              return (
                <div key={item.year} className={`relative flex items-center w-full mb-16 md:mb-24 ${isEven ? 'md:flex-row-reverse' : 'md:flex-row'}`}>
                  
                  {/* Center Node Square */}
                  <motion.div 
                    initial={{ scale: 0 }}
                    whileInView={{ scale: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.4, delay: index * 0.15 + 0.3 }}
                    className="absolute left-[20px] md:left-1/2 w-7 h-7 bg-[#FFD600] border-[3px] border-[#111118] shadow-[3px_3px_0_0_#111118] md:-translate-x-1/2 z-10" 
                  />

                  {/* Content Card Spacer (for alternating layout) */}
                  <div className="hidden md:block md:w-1/2" />

                  {/* Content Card */}
                  <div className="w-[calc(100%-50px)] ml-[50px] md:ml-0 md:w-1/2 flex justify-center z-10">
                    <motion.div
                      initial={{ x: slideInit, opacity: 0 }}
                      whileInView={{ x: 0, opacity: 1 }}
                      viewport={{ once: true }}
                      transition={{ duration: 0.6, delay: index * 0.15, type: "spring", stiffness: 100 }}
                      className={`w-full max-w-[420px] bg-[#FEFDF9] border-[3px] border-[#111118] shadow-[6px_6px_0_0_#111118] p-6 sm:p-8 transition-transform hover:-translate-y-1 hover:shadow-[8px_8px_0_0_#111118] ${rotation} ${marginClass}`}
                    >
                      <div className="text-[#2727E6] font-extrabold text-sm sm:text-base mb-3">
                        {item.year}
                      </div>
                      <h4 className="text-xl sm:text-2xl font-black text-[#111118] uppercase mb-4 leading-tight">
                        {item.title}
                      </h4>
                      <p className="text-sm sm:text-base font-medium text-[#111118]/80 leading-relaxed">
                        {item.description}
                      </p>
                    </motion.div>
                  </div>
                  
                </div>
              );
            })}
          </div>
        </div>

      </div>
    </section>
  );
}
