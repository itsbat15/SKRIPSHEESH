"use client";
import { motion } from "framer-motion";
import { ArrowLeft, ArrowRight } from "lucide-react";

// Data for "Around the web" (Local News about Bimbel Artha)
const aroundTheWebCards = [
  {
    id: 1,
    tag: "BERITA LOKAL",
    title: "Kisah Sukses Bimbel Artha Mengawal Ratusan Pelajar Balikpapan Menembus PTN",
    domain: "TRIBUNKALTIM.CO",
    color: "bg-[#2727E6]",
    url: "https://kaltim.tribunnews.com/",
  },
  {
    id: 2,
    tag: "ARTIKEL PENDIDIKAN",
    title: "Pentingnya Pendidikan Calistung di Usia Dini, Pendekatan Menarik dari Bimbel Artha",
    domain: "KALTIMPOST.JAWAPOS.COM",
    color: "bg-[#FF6600]",
    url: "https://kaltimpost.jawapos.com/",
  },
  {
    id: 3,
    tag: "SOROTAN",
    title: "Lebih Dekat dengan Siswa: Konsep Kelas Kecil Bimbel Artha Jadi Sorotan Positif Orang Tua",
    domain: "PROKAL.CO",
    color: "bg-[#1EAB55]",
    url: "https://prokal.co/",
  },
  {
    id: 4,
    tag: "WAWANCARA",
    title: "Mengapa Bimbingan Belajar Tetap Relevan? Wawancara dengan Founder Bimbel Artha",
    domain: "EDUKASIKALTIM.ID",
    color: "bg-[#FFD600]",
    url: "https://edukasikaltim.id/",
  },
  {
    id: 5,
    tag: "SEJARAH",
    title: "Sejarah Panjang Bimbel Artha, Berdiri Sejak 1997 dan Terus Mencetak Generasi Cerdas",
    domain: "BALIKPAPANPOS.CO.ID",
    color: "bg-[#FFBAD2]",
    url: "https://balikpapanpos.jawapos.com/",
  },
];

export default function AroundTheWebSection() {
  const scrollLeft = () => {
    document.getElementById("around-the-web-scroll").scrollBy({ left: -300, behavior: "smooth" });
  };
  const scrollRight = () => {
    document.getElementById("around-the-web-scroll").scrollBy({ left: 300, behavior: "smooth" });
  };

  return (
    <section className="py-16 sm:py-20 bg-[#FEFDF9] overflow-hidden">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Massive Yellow Container Box */}
        <div className="bg-[#FFD600] rounded-[2.5rem] sm:rounded-[3rem] p-6 sm:p-12 lg:p-16 shadow-sm">
          
          {/* Header: Title and Arrows */}
          <div className="flex items-end justify-between mb-8 sm:mb-12">
            <div>
              <h2 className="text-4xl sm:text-5xl lg:text-6xl font-normal text-[#111118] mb-2 tracking-tight">
                Around the web
              </h2>
              <p className="text-sm sm:text-base text-[#111118] font-normal">
                Have you heard? Bimbel Artha in the spotlights, as told by the internet
              </p>
            </div>
            <div className="hidden sm:flex items-center gap-2">
              <button onClick={scrollLeft} className="w-10 h-10 rounded-full bg-white flex items-center justify-center text-[#111118] hover:bg-white/80 transition-colors shadow-sm">
                <ArrowLeft size={20} />
              </button>
              <button onClick={scrollRight} className="w-10 h-10 rounded-full bg-[#2727E6] flex items-center justify-center text-white hover:bg-[#2727E6]/90 transition-colors shadow-sm">
                <ArrowRight size={20} />
              </button>
            </div>
          </div>

          {/* Horizontal Scroll Cards */}
          <div 
            id="around-the-web-scroll"
            className="flex gap-4 sm:gap-6 overflow-x-auto pb-8 -mx-6 px-6 sm:-mx-12 sm:px-12 lg:-mx-16 lg:px-16 snap-x snap-mandatory scrollbar-hide"
          >
            {aroundTheWebCards.map((card, i) => (
              <motion.a
                key={card.id}
                href={card.url}
                target="_blank"
                rel="noopener noreferrer"
                initial={{ y: 30, opacity: 0 }}
                whileInView={{ y: 0, opacity: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: i * 0.1 }}
                className="bg-white rounded-2xl w-[280px] sm:w-[320px] shrink-0 snap-start flex flex-col overflow-hidden shadow-[0_10px_30px_rgb(0,0,0,0.05)] card-hover cursor-pointer"
              >
                {/* Card Image Area */}
                <div className={`h-40 sm:h-48 w-full ${card.color} p-4 flex items-center justify-center`}>
                  <span className="text-3xl sm:text-4xl font-black text-white/50 tracking-tighter uppercase text-center leading-none mix-blend-overlay">
                    {card.domain.split('.')[0]}
                  </span>
                </div>
                
                {/* Card Content */}
                <div className="p-6 flex flex-col flex-grow">
                  <div className="border border-[#111118]/20 rounded-full px-3 py-1 text-[10px] sm:text-xs font-bold text-[#111118]/70 inline-flex w-fit mb-4">
                    {card.tag}
                  </div>
                  <h3 className="text-lg sm:text-xl font-normal text-[#111118] mb-6 leading-tight tracking-tight">
                    {card.title}
                  </h3>
                  <div className="mt-auto pt-4 border-t border-[#111118]/10 text-[10px] sm:text-xs font-bold text-[#111118]/50 uppercase tracking-widest">
                    {card.domain}
                  </div>
                </div>
              </motion.a>
            ))}
          </div>

        </div>
      </div>
    </section>
  );
}
