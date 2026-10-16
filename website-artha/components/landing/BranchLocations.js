"use client";
import { useState } from "react";
import { motion } from "framer-motion";
import { MapPin, Phone } from "lucide-react";
import { branches } from "@/data/siteData";

export default function BranchLocations() {
  const [activeBranch, setActiveBranch] = useState(branches[0]);

  return (
    <section id="cabang" className="superhi-section bg-[#1EAB55] mt-4">
      <div className="max-w-[1440px] mx-auto">
        <motion.h2
          initial={{ y: 20, opacity: 0 }}
          whileInView={{ y: 0, opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5 }}
          className="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white mb-4 tracking-tight"
        >
          8 Cabang di Balikpapan
        </motion.h2>
        <motion.p
          initial={{ y: 20, opacity: 0 }}
          whileInView={{ y: 0, opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5, delay: 0.1 }}
          className="text-lg sm:text-xl text-white/90 mb-10 font-medium max-w-2xl"
        >
          Temukan cabang Bimbel Artha terdekat dari lokasi Anda. Klik pada kartu cabang untuk melihat detail lokasi di peta.
        </motion.p>

        <div className="flex flex-col lg:flex-row gap-6 lg:gap-8 h-auto lg:h-[600px]">
          
          {/* Left Column: Scrollable List of Branches */}
          <div className="w-full lg:w-5/12 flex flex-col gap-4 overflow-y-auto pr-2 sm:pr-4 custom-scrollbar lg:h-full snap-y">
            {branches.map((branch, index) => {
              const isActive = activeBranch.id === branch.id;
              
              return (
                <motion.div
                  key={branch.id}
                  initial={{ x: -20, opacity: 0 }}
                  whileInView={{ x: 0, opacity: 1 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.3, delay: index * 0.05 }}
                  onClick={() => setActiveBranch(branch)}
                  className={`cursor-pointer border-[3px] border-[#111118] p-5 sm:p-6 transition-all duration-300 snap-start
                    ${isActive 
                      ? "bg-[#FFD600] translate-x-2 shadow-[6px_6px_0_0_#111118]" 
                      : "bg-white hover:bg-[#FEFDF9] shadow-[4px_4px_0_0_#111118] hover:translate-x-1"
                    }
                  `}
                >
                  <div className="flex items-center justify-between mb-4">
                    <h3 className="text-xl font-black text-[#111118] uppercase tracking-tight">{branch.name}</h3>
                    {branch.label && (
                      <span className="text-xs font-bold bg-[#111118] text-white px-3 py-1 uppercase tracking-widest">
                        {branch.label}
                      </span>
                    )}
                  </div>

                  <div className="flex items-start gap-3 mb-3">
                    <MapPin size={18} className="text-[#111118] shrink-0 mt-0.5" />
                    <p className="text-sm font-medium text-[#111118]/80 leading-relaxed">{branch.address}</p>
                  </div>

                  <div className="flex items-center gap-3">
                    <Phone size={16} className="text-[#111118] shrink-0" />
                    <span className="text-sm font-bold text-[#111118]">{branch.phone}</span>
                  </div>
                </motion.div>
              );
            })}
          </div>

          {/* Right Column: Google Maps iframe */}
          <div className="w-full lg:w-7/12 h-[400px] lg:h-full border-[3px] border-[#111118] shadow-[8px_8px_0_0_#111118] bg-[#111118] overflow-hidden relative">
            <iframe 
              src={`https://maps.google.com/maps?q=${activeBranch.mapQuery}&t=&z=15&ie=UTF8&iwloc=&output=embed`}
              width="100%" 
              height="100%" 
              style={{ border: 0, filter: "contrast(1.1) saturation(1.2)" }} 
              allowFullScreen="" 
              loading="lazy" 
              referrerPolicy="no-referrer-when-downgrade"
              className="absolute inset-0"
            ></iframe>
            
            {/* Map Overlay info (Optional styling) */}
            <div className="absolute top-4 left-4 bg-white border-[3px] border-[#111118] p-4 shadow-[4px_4px_0_0_#111118] max-w-[280px] pointer-events-none hidden sm:block">
              <h4 className="font-black text-[#111118] text-lg uppercase leading-none mb-1">{activeBranch.name}</h4>
              <p className="text-xs font-bold text-[#111118]/60 uppercase">{activeBranch.address}</p>
            </div>
            
            {/* Open in Google Maps Button */}
            <a 
              href={`https://maps.google.com/?q=${activeBranch.mapQuery}`}
              target="_blank"
              rel="noopener noreferrer"
              className="absolute bottom-4 right-4 bg-[#2727E6] border-[3px] border-[#111118] text-white font-black uppercase text-xs px-4 py-3 shadow-[4px_4px_0_0_#111118] hover:translate-y-1 hover:shadow-none transition-all z-10"
            >
              Buka di Google Maps →
            </a>
          </div>

        </div>
      </div>
    </section>
  );
}
