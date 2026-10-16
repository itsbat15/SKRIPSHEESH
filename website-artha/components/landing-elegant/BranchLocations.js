"use client";
import { useState } from "react";
import { motion } from "framer-motion";
import { MapPin, Phone, ExternalLink } from "lucide-react";
import { branches } from "@/data/siteData";

export default function BranchLocations() {
  const [activeBranch, setActiveBranch] = useState(branches[0]);

  return (
    <section id="cabang" className="py-24 sm:py-32 bg-[#F4F7FE] text-[#111118] border-b border-black/10 overflow-hidden">
      <div className="max-w-[1400px] mx-auto px-6 sm:px-12 lg:px-20">
        
        {/* Section Header with Scroll Entrance Animation */}
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
                <span className="w-3 h-3 bg-[#2727E6] inline-block" />
                <p className="text-xs font-bold tracking-[0.25em] uppercase text-[#2727E6]">
                  Jaringan Cabang Resmi
                </p>
              </div>
              <h2 className="text-5xl sm:text-7xl lg:text-8xl font-black uppercase tracking-tighter text-[#111118] leading-none">
                8 CABANG DI BALIKPAPAN
              </h2>
            </div>
            
            <p className="text-sm sm:text-base text-[#555555] max-w-md leading-relaxed">
              Temukan cabang Bimbel Artha terdekat dari lokasi Anda di seluruh penjuru kota Balikpapan.
            </p>
          </div>
        </motion.div>

        {/* Master Detail Layout with Scroll Animations */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12">
          
          {/* Left: 8 Branch Cards List with Staggered Scroll Entrance */}
          <div className="lg:col-span-5 space-y-3 max-h-[580px] overflow-y-auto pr-2 custom-scrollbar">
            {branches.map((branch, index) => {
              const isActive = activeBranch.id === branch.id;
              const num = String(index + 1).padStart(2, "0");

              return (
                <motion.button
                  key={branch.id}
                  onClick={() => setActiveBranch(branch)}
                  initial={{ opacity: 0, y: 40 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ margin: "-50px" }}
                  transition={{ delay: index * 0.06, duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
                  className={`w-full text-left p-5 border rounded-xl transition-all duration-300 ${
                    isActive
                      ? "bg-[#111118] text-white border-[#111118] shadow-lg"
                      : "bg-white text-[#111118] border-black/10 hover:border-[#2727E6]"
                  }`}
                >
                  <div className="flex items-center justify-between mb-2">
                    <div className="flex items-center gap-3">
                      <span className={`text-xs font-mono font-bold ${isActive ? "text-[#FFD600]" : "text-[#888888]"}`}>
                        {num}
                      </span>
                      <h4 className="font-black text-base sm:text-lg uppercase tracking-tight">
                        {branch.name}
                      </h4>
                    </div>
                    {branch.label && (
                      <span
                        className={`text-[9px] font-bold tracking-widest uppercase px-2.5 py-0.5 rounded-full ${
                          isActive ? "bg-[#2727E6] text-white" : "bg-black/10 text-black"
                        }`}
                      >
                        {branch.label}
                      </span>
                    )}
                  </div>
                  <p className={`text-xs leading-relaxed ${isActive ? "text-white/70" : "text-[#555555]"}`}>
                    {branch.address}
                  </p>
                </motion.button>
              );
            })}
          </div>

          {/* Right: Active Branch Map & Details with Scroll Entrance Animation */}
          <motion.div
            initial={{ opacity: 0, y: 50, scale: 0.96 }}
            whileInView={{ opacity: 1, y: 0, scale: 1 }}
            viewport={{ margin: "-50px" }}
            transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}
            className="lg:col-span-7 flex flex-col justify-between bg-white border border-black/10 rounded-2xl p-8 sm:p-10 shadow-sm"
          >
            <div className="mb-6">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-black/10 mb-6">
                <div>
                  <span className="text-[10px] font-bold tracking-[0.2em] uppercase text-[#2727E6] block mb-1">
                    DETAIL CABANG
                  </span>
                  <h3 className="text-2xl sm:text-3xl font-black uppercase tracking-tight text-[#111118]">
                    {activeBranch.name}
                  </h3>
                </div>
                <a
                  href={`https://maps.google.com/?q=${encodeURIComponent(activeBranch.name + " " + activeBranch.address)}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-[#2727E6] hover:text-[#E11D48] transition-colors"
                >
                  Buka di Google Maps <ExternalLink size={14} />
                </a>
              </div>

              <div className="space-y-3 mb-6">
                <p className="text-sm text-[#555555] flex items-start gap-3 leading-relaxed">
                  <MapPin size={18} className="text-[#2727E6] shrink-0 mt-0.5" />
                  <span>{activeBranch.address}</span>
                </p>
                {activeBranch.phone && (
                  <p className="text-sm text-[#555555] flex items-center gap-3">
                    <Phone size={18} className="text-[#2727E6] shrink-0" />
                    <span>{activeBranch.phone}</span>
                  </p>
                )}
              </div>
            </div>

            {/* Embedded Google Map */}
            <div className="w-full h-96 border border-black/10 rounded-xl bg-[#EFEFEF] overflow-hidden">
              <iframe
                title={activeBranch.name}
                width="100%"
                height="100%"
                style={{ border: 0 }}
                loading="lazy"
                allowFullScreen
                src={`https://maps.google.com/maps?q=${encodeURIComponent(activeBranch.address || activeBranch.name + " Balikpapan")}&t=&z=15&ie=UTF8&iwloc=&output=embed`}
              />
            </div>
          </motion.div>

        </div>

      </div>
    </section>
  );
}
