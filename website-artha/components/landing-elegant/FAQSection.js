"use client";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Plus, Minus } from "lucide-react";
import { faqItems } from "@/data/siteData";

export default function FAQSection() {
  const [openIndex, setOpenIndex] = useState(0);

  return (
    <section id="faq" className="py-24 sm:py-32 bg-[#FFFFFF] text-[#111111] border-b border-black/10 overflow-hidden">
      <div className="max-w-[1200px] mx-auto px-6 sm:px-12 lg:px-20">
        
        {/* Section Header with Scroll Animation */}
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ margin: "-100px" }}
          transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
          className="mb-20 text-center max-w-3xl mx-auto"
        >
          <div className="flex items-center justify-center gap-3 mb-4">
            <span className="w-2.5 h-2.5 bg-[#111111] inline-block" />
            <p className="text-xs font-bold tracking-[0.25em] uppercase text-[#111111]">
              Informasi & Bantuan
            </p>
          </div>
          <h2 className="text-5xl sm:text-7xl lg:text-8xl font-black uppercase tracking-tighter text-[#111111] leading-none mb-6">
            FAQS
          </h2>
          <p className="text-sm sm:text-base text-[#666666] leading-relaxed">
            Jawaban lengkap atas pertanyaan yang sering diajukan mengenai program, jadwal, dan sistem belajar di Bimbel Artha.
          </p>
        </motion.div>

        {/* 5 FAQ Accordion Items with Scroll Entrance Animations */}
        <div className="space-y-0 border-t border-black/10">
          {faqItems.map((item, index) => {
            const isOpen = openIndex === index;
            const num = String(index + 1).padStart(2, "0");

            return (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 40 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ margin: "-50px" }}
                transition={{ delay: index * 0.08, duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
                className="border-b border-black/10"
              >
                <button
                  onClick={() => setOpenIndex(isOpen ? -1 : index)}
                  className="w-full py-8 sm:py-10 flex items-start sm:items-center justify-between text-left group gap-6"
                >
                  <div className="flex items-start sm:items-center gap-6 sm:gap-8">
                    <span className="text-xs font-mono font-bold text-[#888888] tracking-widest pt-1 sm:pt-0">
                      {num}
                    </span>
                    <h3 className="text-lg sm:text-2xl font-bold uppercase tracking-tight text-[#111111] group-hover:text-[#2727E6] transition-colors">
                      {item.question}
                    </h3>
                  </div>

                  <div className="w-10 h-10 border border-black/20 flex items-center justify-center shrink-0 group-hover:bg-[#111118] group-hover:text-white transition-all">
                    {isOpen ? <Minus size={16} /> : <Plus size={16} />}
                  </div>
                </button>

                <AnimatePresence initial={false}>
                  {isOpen && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: "auto", opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }}
                      className="overflow-hidden"
                    >
                      <div className="pl-14 sm:pl-16 pr-6 pb-8 pt-0">
                        <p className="text-sm sm:text-base text-[#555555] leading-[1.8]">
                          {item.answer}
                        </p>
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </motion.div>
            );
          })}
        </div>

      </div>
    </section>
  );
}
