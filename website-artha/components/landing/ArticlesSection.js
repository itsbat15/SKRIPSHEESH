"use client";
import { motion } from "framer-motion";
import { BookOpen, Calendar, Clock, User, ArrowUpRight, Sparkles } from "lucide-react";
import { articlesData } from "@/data/siteData";

export default function ArticlesSection() {
  return (
    <section id="artikel" className="py-16 sm:py-24 bg-[#FAF8F5] relative overflow-hidden border-t-[3px] border-b-[3px] border-[#111118]">
      {/* Decorative Background Elements */}
      <div className="absolute top-8 left-6 w-20 h-20 bg-[#FFD600] rounded-full border-[2px] border-[#111118] opacity-20 pointer-events-none" />
      <div className="absolute bottom-10 right-10 w-28 h-28 bg-[#2727E6] rounded-2xl border-[2px] border-[#111118] opacity-15 rotate-12 pointer-events-none" />

      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
          <motion.div
            initial={{ opacity: 0, y: 15 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#FFD600] border-[2px] border-[#111118] shadow-[2px_2px_0_0_#111118] text-xs font-black uppercase tracking-wider text-[#111118] mb-4"
          >
            <Sparkles size={14} className="text-[#111118]" />
            Wawasan &amp; Edukasi Bimbel Artha
          </motion.div>

          <motion.h2
            initial={{ opacity: 0, y: 15 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1 }}
            className="font-heading font-black text-3xl sm:text-4xl md:text-5xl text-[#111118] tracking-tight leading-tight mb-4"
          >
            Artikel &amp; Seputar Edukasi
          </motion.h2>

          <motion.p
            initial={{ opacity: 0, y: 15 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2 }}
            className="text-base sm:text-lg text-slate-700 font-medium"
          >
            Dapatkan tips belajar efektif, informasi jadwal tryout, bocoran kisi-kisi soal TKA/UTBK, serta panduan pendidikan anak untuk orang tua.
          </motion.p>
        </div>

        {/* Articles Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {articlesData.map((article, idx) => (
            <motion.article
              key={article.id}
              initial={{ opacity: 0, y: 25 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: idx * 0.1 }}
              style={{ backgroundColor: article.color }}
              className="rounded-2xl border-[2.5px] border-[#111118] shadow-[4px_4px_0_0_#111118] p-6 flex flex-col justify-between transition-all duration-300 hover:-translate-y-1 hover:shadow-[6px_6px_0_0_#111118]"
            >
              <div>
                {/* Category & Read Time */}
                <div className="flex items-center justify-between gap-2 mb-4">
                  <span
                    style={{ backgroundColor: article.badgeBg, color: article.badgeText }}
                    className="inline-block px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest border border-[#111118]"
                  >
                    {article.category}
                  </span>
                  <span className="text-[11px] font-bold text-[#111118]/70 flex items-center gap-1">
                    <Clock size={12} /> {article.readTime}
                  </span>
                </div>

                {/* Title */}
                <h3 className="font-heading font-black text-lg text-[#111118] leading-snug mb-3 hover:underline cursor-pointer">
                  {article.title}
                </h3>

                {/* Snippet */}
                <p className="text-xs text-[#111118]/80 font-medium leading-relaxed mb-6">
                  {article.snippet}
                </p>
              </div>

              {/* Footer Meta & CTA */}
              <div className="pt-4 border-t border-[#111118]/15 flex items-center justify-between">
                <div className="text-[11px] font-semibold text-[#111118]/80">
                  <p className="font-bold text-[#111118] flex items-center gap-1">
                    <User size={11} /> {article.author}
                  </p>
                  <p className="text-[10px] text-[#111118]/60 flex items-center gap-1 mt-0.5">
                    <Calendar size={10} /> {article.date}
                  </p>
                </div>

                <button
                  style={{ backgroundColor: "#111118", color: "#FFFFFF" }}
                  className="w-8 h-8 rounded-lg flex items-center justify-center border border-[#111118] shadow-[1.5px_1.5px_0_0_#111118] hover:bg-[#2727E6] transition-colors shrink-0"
                  aria-label="Baca Artikel"
                >
                  <ArrowUpRight size={16} />
                </button>
              </div>
            </motion.article>
          ))}
        </div>

        {/* Bottom CTA */}
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mt-12 text-center"
        >
          <a
            href="#artikel"
            className="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-[#2727E6] text-white font-black text-sm uppercase tracking-wider border-[2.5px] border-[#111118] shadow-[4px_4px_0_0_#111118] hover:translate-y-px hover:shadow-[2px_2px_0_0_#111118] transition-all"
          >
            <BookOpen size={16} />
            Lihat Semua Artikel Edukasi
          </a>
        </motion.div>
      </div>
    </section>
  );
}
