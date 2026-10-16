"use client";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Plus, X } from "lucide-react";
import { faqItems } from "@/data/siteData";

export default function FAQSection() {
  const [openIndex, setOpenIndex] = useState(0);

  return (
    <section id="faq" className="py-16 sm:py-24 bg-[#F5F7FF]">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8">
        {/* Title - SuperHi big text style */}
        <motion.h2
          initial={{ y: 20, opacity: 0 }}
          whileInView={{ y: 0, opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5 }}
          className="text-6xl sm:text-7xl lg:text-[5.5rem] font-normal text-[#111118] mb-12 sm:mb-16 tracking-tight"
        >
          FAQs
        </motion.h2>

        {/* FAQ Accordion */}
        <div className="space-y-4">
          {faqItems.map((item, index) => {
            const isOpen = openIndex === index;
            return (
              <motion.div
                key={index}
                initial={{ opacity: 0 }}
                whileInView={{ opacity: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.3, delay: index * 0.05 }}
                className="bg-white rounded-3xl overflow-hidden shadow-sm"
              >
                <button
                  onClick={() => setOpenIndex(isOpen ? -1 : index)}
                  className="w-full flex items-start justify-between px-6 sm:px-8 py-6 sm:py-8 text-left group"
                >
                  <span className="text-2xl sm:text-3xl lg:text-4xl font-normal text-[#111118] pr-8 leading-tight tracking-tight">
                    {item.question}
                  </span>
                  <div className="shrink-0 pt-1">
                    {isOpen ? (
                      <X size={32} strokeWidth={1} className="text-[#111118]" />
                    ) : (
                      <Plus size={32} strokeWidth={1} className="text-[#111118]" />
                    )}
                  </div>
                </button>

                <AnimatePresence initial={false}>
                  {isOpen && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: "auto", opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.3, ease: "easeInOut" }}
                      className="overflow-hidden"
                    >
                      <div className="px-6 sm:px-8 pb-8 sm:pb-10 pt-2">
                        <p className="text-base sm:text-lg text-[#111118]/80 leading-relaxed max-w-4xl font-medium">
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
