"use client";
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { keunggulan } from "@/data/siteData";
import {
  GraduationCap, Gift, Shield, BookOpen,
  Calendar, Wallet, Users, MessageCircle,
} from "lucide-react";

const iconMap = {
  GraduationCap, Gift, Shield, BookOpen,
  Calendar, Wallet, Users, MessageCircle,
};

export default function WhyChooseUs() {
  const [activeIndex, setActiveIndex] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      const items = document.querySelectorAll(".why-item-elegant");
      let newActiveIndex = activeIndex;
      let minDistance = Infinity;
      const triggerY = window.innerHeight * 0.4;

      items.forEach((item, index) => {
        const rect = item.getBoundingClientRect();
        const distance = Math.abs(rect.top - triggerY);
        if (rect.top < window.innerHeight && rect.bottom > 0) {
          if (distance < minDistance) {
            minDistance = distance;
            newActiveIndex = index;
          }
        }
      });

      if (newActiveIndex !== activeIndex) {
        setActiveIndex(newActiveIndex);
      }
    };

    window.addEventListener("scroll", handleScroll);
    handleScroll();
    return () => window.removeEventListener("scroll", handleScroll);
  }, [activeIndex]);

  return (
    <section className="bg-[#FFFFFF] relative border-b border-[#0F172A]/10">
      <div className="max-w-[1400px] mx-auto px-6 sm:px-12 lg:px-20">
        <div className="flex flex-col md:flex-row relative">
          
          {/* Left Side: Clean Title List Only */}
          <motion.div
            initial="hidden"
            whileInView="show"
            viewport={{ once: true, amount: 0.1 }}
            className="w-full md:w-1/2 py-24 md:py-32 pr-0 md:pr-16 z-10"
          >
            <div className="flex items-center gap-3 mb-6">
              <span className="w-2.5 h-2.5 bg-[#2563EB] inline-block" />
              <p className="text-xs font-bold tracking-[0.25em] uppercase text-[#2563EB]">
                Kenapa Bimbel Artha?
              </p>
            </div>
            
            <h2 className="text-4xl sm:text-6xl font-black uppercase tracking-tighter text-[#0F172A] mb-12">
              KEUNGGULAN KAMI
            </h2>

            <div className="flex flex-col">
              {keunggulan.map((item, index) => {
                const isActive = activeIndex === index;
                const num = String(index + 1).padStart(2, "0");

                return (
                  <div
                    key={index}
                    className="why-item-elegant border-b border-[#0F172A]/10 py-8 transition-all duration-500 cursor-default"
                  >
                    <div className="flex items-center gap-4 mb-2">
                      <span className={`text-xs font-mono font-bold ${isActive ? "text-[#2563EB]" : "text-[#94A3B8]"}`}>
                        {num}
                      </span>
                    </div>

                    <h3
                      className={`text-3xl sm:text-4xl lg:text-5xl font-black uppercase transition-all duration-500 tracking-tight ${
                        isActive ? "text-[#0F172A]" : "text-[#0F172A]/20"
                      }`}
                    >
                      {item.title}.
                    </h3>
                  </div>
                );
              })}
            </div>
          </motion.div>

          {/* Right Side: Sticky Interactive Visual Panel */}
          <div className="hidden md:flex w-1/2 h-screen sticky top-0 items-center justify-center py-12 pl-8">
            <div className="relative w-full h-[75%] border border-[#0F172A]/10 bg-[#F8FAFC] overflow-hidden shadow-xl">
              {keunggulan.map((item, index) => {
                const isActive = activeIndex === index;
                const IconComp = iconMap[item.icon] || Shield;

                return (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, y: 40 }}
                    animate={{ opacity: isActive ? 1 : 0, y: isActive ? 0 : 40 }}
                    transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
                    className={`absolute inset-0 flex flex-col items-center justify-center p-12 bg-[#FFFFFF] ${
                      isActive ? "z-10" : "z-0 pointer-events-none"
                    }`}
                  >
                    {/* Background Icon */}
                    <IconComp size={240} className="text-[#1E3A8A] opacity-5 absolute" />

                    {/* Floating Info Card */}
                    <div className="relative z-10 bg-[#0F172A] text-white p-8 max-w-sm border border-white/10 shadow-2xl">
                      <div className="text-5xl font-mono font-black text-[#F59E0B] mb-3">
                        0{index + 1}
                      </div>
                      <h4 className="text-xl font-extrabold uppercase tracking-tight mb-2 text-white">
                        {item.title}
                      </h4>
                      <p className="text-xs text-white/70 leading-relaxed font-medium">
                        {item.description}
                      </p>
                    </div>
                  </motion.div>
                );
              })}
            </div>
          </div>

        </div>
      </div>
    </section>
  );
}
