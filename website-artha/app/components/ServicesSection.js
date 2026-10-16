"use client";
import { useState } from "react";
import Image from "next/image";
import { Clock, CheckCircle2 } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { programs, schedule } from "../data/siteData";

export default function ServicesSection() {
  const [activeProgram, setActiveProgram] = useState("calistung");
  const [showSchedule, setShowSchedule] = useState(false);

  const selected = programs.find((p) => p.id === activeProgram);

  return (
    <section id="layanan" className="py-20 lg:py-28 bg-surface overflow-hidden">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <span className="inline-block bg-primary-50 text-primary font-semibold text-sm px-4 py-1.5 rounded-full mb-4">
            Program Layanan
          </span>
          <h2 className="font-heading font-extrabold text-3xl sm:text-4xl lg:text-5xl text-foreground mb-4">
            Layanan{" "}
            <span className="gradient-text">Bimbel Artha</span>
          </h2>
          <p className="text-muted text-lg max-w-2xl mx-auto">
            Program bimbingan belajar lengkap dari tingkat TK hingga SMA dan Bahasa Inggris
          </p>
        </motion.div>

        {/* Program Tabs with layoutId */}
        <div className="flex flex-wrap justify-center gap-3 mb-12">
          {programs.map((prog) => (
            <button
              key={prog.id}
              onClick={() => setActiveProgram(prog.id)}
              className="relative flex items-center gap-2 px-5 py-3 rounded-xl text-sm font-semibold transition-colors"
            >
              {activeProgram === prog.id && (
                <motion.div
                  layoutId="activeServiceTabBadge"
                  className="absolute inset-0 bg-primary rounded-xl shadow-lg shadow-primary/25"
                  transition={{ type: "spring", stiffness: 400, damping: 30 }}
                />
              )}
              <span className={`relative z-10 flex items-center gap-2 ${activeProgram === prog.id ? "text-white" : "text-muted hover:text-foreground"}`}>
                <Image src={prog.image} alt={prog.title} width={20} height={20} />
                {prog.title}
              </span>
            </button>
          ))}
        </div>

        {/* Selected Program Detail with AnimatePresence */}
        <AnimatePresence mode="wait">
          {selected && (
            <motion.div
              key={selected.id}
              initial={{ opacity: 0, y: 20, scale: 0.98 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: -20, scale: 0.98 }}
              transition={{ duration: 0.4 }}
              className="bg-white rounded-3xl shadow-lg border border-border/50 overflow-hidden"
            >
              <div className="grid md:grid-cols-2">
                {/* Left: Info */}
                <div className="p-8 sm:p-10">
                  <div className="flex items-center gap-3 mb-4">
                    <div className="w-14 h-14 bg-primary-50 rounded-2xl flex items-center justify-center">
                      <Image src={selected.image} alt={selected.title} width={32} height={32} />
                    </div>
                    <div>
                      <h3 className="font-heading font-bold text-2xl text-foreground">
                        {selected.title}
                      </h3>
                      <p className="text-muted text-sm">{selected.subtitle}</p>
                    </div>
                  </div>

                  <p className="text-foreground/70 text-base leading-relaxed mb-6">
                    {selected.description}
                  </p>

                  <h4 className="font-heading font-semibold text-sm text-foreground mb-3 uppercase tracking-wide">
                    Mata Pelajaran
                  </h4>
                  <div className="space-y-2">
                    {selected.subjects.map((subject, i) => (
                      <motion.div
                        key={i}
                        initial={{ opacity: 0, x: -10 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: i * 0.08 }}
                        className="flex items-center gap-3"
                      >
                        <CheckCircle2 size={18} className="text-accent shrink-0" />
                        <span className="text-foreground/70 text-sm">{subject}</span>
                      </motion.div>
                    ))}
                  </div>
                </div>

                {/* Right: Schedule Preview */}
                <div className="bg-gradient-to-br from-secondary-dark to-secondary p-8 sm:p-10 text-white">
                  <div className="flex items-center gap-2 mb-6">
                    <Clock size={20} />
                    <h4 className="font-heading font-bold text-lg">Jadwal & Biaya</h4>
                  </div>

                  <div className="space-y-3">
                    {schedule.slice(0, showSchedule ? schedule.length : 4).map((s, i) => (
                      <motion.div
                        key={i}
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: i * 0.05 }}
                        className="flex items-center justify-between bg-white/10 rounded-xl px-4 py-3 backdrop-blur-sm"
                      >
                        <div>
                          <p className="font-semibold text-sm">{s.session}</p>
                          <p className="text-white/70 text-xs">{s.time}</p>
                        </div>
                        <span
                          className={`font-bold text-sm ${
                            s.price === "GRATIS"
                              ? "text-green-300 bg-green-500/20 px-3 py-1 rounded-full"
                              : "text-primary-light"
                          }`}
                        >
                          {s.price === "GRATIS" ? "GRATIS" : `Rp ${s.price}`}
                        </span>
                      </motion.div>
                    ))}
                  </div>

                  {!showSchedule && (
                    <button
                      onClick={() => setShowSchedule(true)}
                      className="mt-4 w-full text-center text-white/80 hover:text-white text-sm font-medium underline underline-offset-4 transition-colors"
                    >
                      Lihat semua jadwal →
                    </button>
                  )}

                  <p className="mt-6 text-white/60 text-xs">
                    * Hari: Senin-Rabu-Jumat / Selasa-Kamis-Sabtu (3-4x per minggu)
                  </p>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </section>
  );
}
