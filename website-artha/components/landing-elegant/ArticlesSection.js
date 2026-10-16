"use client";
import { motion } from "framer-motion";
import { ArrowUpRight } from "lucide-react";
import Image from "next/image";
import { articlesData } from "@/data/siteData";

const articleImages = [
  "/images/wp-media/artha-class1.jpg",
  "/images/wp-media/artha-class2.jpg",
  "/images/wp-media/artha-class3.jpg",
  "/images/wp-media/artha5-office.jpg",
  "/images/wp-media/artha6-team.jpg",
  "/images/wp-media/artha7-staff.jpg",
  "/images/wp-media/group-photo.png",
  "/images/wp-media/artha-branch1.jpg",
];

export default function ArticlesSection() {
  return (
    <section id="artikel" className="py-24 sm:py-32 bg-[#F4F7FE] text-[#111118] border-b border-black/10 overflow-hidden">
      <div className="max-w-[1400px] mx-auto px-6 sm:px-12 lg:px-20">
        
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ margin: "-100px" }}
          transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
          className="mb-20"
        >
          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-8 pb-10 border-b border-black/10">
            <div>
              <div className="flex items-center gap-3 mb-4">
                <span className="w-3 h-3 bg-[#E11D48] inline-block" />
                <p className="text-xs font-bold tracking-[0.25em] uppercase text-[#E11D48]">
                  Wawasan & Tips Edukasi
                </p>
              </div>
              <h2 className="text-5xl sm:text-7xl lg:text-8xl font-black uppercase tracking-tighter text-[#111118] leading-none">
                ARTIKEL & BERITA
              </h2>
            </div>
            
            <div className="flex flex-col gap-3 items-start lg:items-end">
              <p className="text-sm sm:text-base text-[#555555] max-w-md leading-relaxed text-left lg:text-right">
                Artikel edukasi, bank soal, dan berita terbaru dari tim akademik Bimbel Artha Balikpapan.
              </p>
              <a
                href="https://bimbelartha.id/artikel/"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-[#2727E6] hover:text-[#E11D48] transition-colors border-b-2 border-[#2727E6] hover:border-[#E11D48] pb-1"
              >
                Lihat Semua Artikel
                <ArrowUpRight size={14} />
              </a>
            </div>
          </div>
        </motion.div>

        {/* Articles Box Grid (Clean without overlay badges on top of photos) */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {articlesData.map((article, idx) => {
            const num = String(idx + 1).padStart(2, "0");
            const imageSrc = articleImages[idx % articleImages.length];

            return (
              <motion.a
                key={article.id}
                href={article.link || "#"}
                target="_blank"
                rel="noopener noreferrer"
                initial={{ opacity: 0, y: 60, scale: 0.95 }}
                whileInView={{ opacity: 1, y: 0, scale: 1 }}
                viewport={{ margin: "-50px" }}
                transition={{ duration: 0.6, delay: idx * 0.08, ease: [0.22, 1, 0.36, 1] }}
                className="bg-white border border-black/10 rounded-xl overflow-hidden flex flex-col justify-between group transition-all duration-300 shadow-sm hover:shadow-xl"
              >
                <div>
                  {/* Clean Article Image (No Overlay Badge Tag on Top) */}
                  <div className="relative aspect-[16/10] w-full bg-[#EFEFEF] overflow-hidden border-b border-black/10">
                    <Image
                      src={imageSrc}
                      alt={article.title}
                      fill
                      className="object-cover group-hover:scale-105 transition-all duration-500"
                    />
                  </div>

                  {/* Content Container */}
                  <div className="p-6">
                    <div className="flex items-center justify-between text-[11px] font-mono font-bold text-[#888888] mb-3">
                      <span>{article.date}</span>
                      <span className="text-[#2727E6]">NO {num}</span>
                    </div>

                    <h3 className="text-base sm:text-lg font-black uppercase tracking-tight text-[#111118] group-hover:text-[#2727E6] transition-colors leading-snug mb-3 line-clamp-2">
                      {article.title}
                    </h3>

                    <p className="text-xs text-[#555555] leading-relaxed line-clamp-3 mb-4">
                      {article.snippet}
                    </p>
                  </div>
                </div>

                {/* Card Footer Link */}
                <div className="px-6 py-4 border-t border-black/10 bg-[#F8FAFC] flex items-center justify-between group-hover:bg-[#2727E6] group-hover:text-white transition-colors">
                  <span className="text-[10px] font-bold uppercase tracking-widest">
                    Baca Artikel
                  </span>
                  <ArrowUpRight size={14} className="group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
                </div>

              </motion.a>
            );
          })}
        </div>

      </div>
    </section>
  );
}
