"use client";
import { useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import Image from "next/image";

const galleryImagesRow1 = [
  { src: "/images/wp-media/group-photo.png", title: "Tim Pengajar Artha Group", aspect: "aspect-[16/10]" },
  { src: "/images/wp-media/artha-class1.jpg", title: "Suasana Belajar Kelas", aspect: "aspect-[4/3]" },
  { src: "/images/wp-media/artha-class2.jpg", title: "Diskusi & Pendampingan", aspect: "aspect-[3/4]" },
  { src: "/images/wp-media/artha5-office.jpg", title: "Kantor Cabang Artha 5", aspect: "aspect-[16/10]" },
  { src: "/images/wp-media/artha6-team.jpg", title: "Team Pengajar Artha 6", aspect: "aspect-[4/3]" },
  { src: "/images/wp-media/artha7-staff.jpg", title: "Staf Pengajar Artha 7", aspect: "aspect-[3/4]" },
];

const galleryImagesRow2 = [
  { src: "/images/wp-media/artha-class3.jpg", title: "Kegiatan Belajar Siswa", aspect: "aspect-[4/3]" },
  { src: "/images/wp-media/artha-branch1.jpg", title: "Cabang Artha 1", aspect: "aspect-[16/10]" },
  { src: "/images/wp-media/artha-branch2.jpg", title: "Cabang Artha 2", aspect: "aspect-[3/4]" },
  { src: "/images/wp-media/artha-branch3.jpg", title: "Cabang Artha 3", aspect: "aspect-[4/3]" },
  { src: "/images/wp-media/artha-branch4.jpg", title: "Cabang Artha 4", aspect: "aspect-[16/10]" },
  { src: "/images/wp-media/artha-branch5.jpg", title: "Cabang Artha 5", aspect: "aspect-[4/3]" },
];

export default function GallerySection() {
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end end"],
  });

  const x1 = useTransform(scrollYProgress, [0, 1], ["0%", "-45%"]);
  const x2 = useTransform(scrollYProgress, [0, 1], ["-30%", "10%"]);

  return (
    <section
      ref={containerRef}
      id="galeri"
      className="relative h-[250vh] bg-[#0B132B] text-white"
    >
      {/* Sticky Inner Container */}
      <div className="sticky top-0 h-screen w-full flex flex-col justify-center overflow-hidden py-12">
        
        {/* Section Header */}
        <div className="max-w-[1440px] mx-auto w-full px-6 sm:px-12 lg:px-20 mb-8 z-10 shrink-0">
          <div className="flex items-center gap-3 mb-2">
            <span className="w-3 h-3 bg-[#FFD600] inline-block" />
            <p className="text-xs font-bold tracking-[0.25em] uppercase text-[#FFD600]">
              Galeri & Suasana Belajar
            </p>
          </div>
          <h2 className="text-4xl sm:text-6xl font-black uppercase tracking-tighter text-white">
            OUR GALLERY & CULTURE
          </h2>
        </div>

        {/* Moving Horizontal Photo Rows (Clean cards without thin hover border outlines) */}
        <div className="space-y-6 overflow-hidden">
          
          {/* Row 1: Moves Left on Scroll */}
          <motion.div style={{ x: x1 }} className="flex gap-6 w-max px-8">
            {galleryImagesRow1.map((item, idx) => (
              <div
                key={idx}
                className={`relative ${item.aspect} h-[200px] sm:h-[260px] rounded-lg overflow-hidden group shrink-0 shadow-2xl transition-all duration-300`}
              >
                <Image
                  src={item.src}
                  alt={item.title}
                  fill
                  className="object-cover group-hover:scale-105 transition-all duration-500"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity p-4 flex items-end">
                  <span className="text-xs font-bold uppercase tracking-wider text-white">
                    {item.title}
                  </span>
                </div>
              </div>
            ))}
          </motion.div>

          {/* Row 2: Moves Right on Scroll */}
          <motion.div style={{ x: x2 }} className="flex gap-6 w-max px-8">
            {galleryImagesRow2.map((item, idx) => (
              <div
                key={idx}
                className={`relative ${item.aspect} h-[200px] sm:h-[260px] rounded-lg overflow-hidden group shrink-0 shadow-2xl transition-all duration-300`}
              >
                <Image
                  src={item.src}
                  alt={item.title}
                  fill
                  className="object-cover group-hover:scale-105 transition-all duration-500"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity p-4 flex items-end">
                  <span className="text-xs font-bold uppercase tracking-wider text-white">
                    {item.title}
                  </span>
                </div>
              </div>
            ))}
          </motion.div>

        </div>

        {/* Scroll hint */}
        <div className="text-center mt-6 shrink-0 z-10">
          <span className="text-[10px] font-mono font-bold tracking-[0.25em] text-[#FFD600] uppercase">
            SCROLL DOWN TO DISCOVER MORE PHOTOS →
          </span>
        </div>

      </div>
    </section>
  );
}
