"use client";
import { useState } from "react";
import { Building2, Eye, Target } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { aboutText, timeline } from "../data/siteData";

export default function AboutSection() {
  const [activeTab, setActiveTab] = useState("about");

  return (
    <section id="tentang" className="py-20 lg:py-28 bg-surface overflow-hidden">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <span className="inline-block bg-primary-50 text-primary font-semibold text-sm px-4 py-1.5 rounded-full mb-4">
            Tentang Kami
          </span>
          <h2 className="font-heading font-extrabold text-3xl sm:text-4xl lg:text-5xl text-foreground mb-4">
            Mengenal Lebih Dekat{" "}
            <span className="gradient-text">Bimbel Artha</span>
          </h2>
          <p className="text-muted text-lg max-w-2xl mx-auto">
            Lebih dari 28 tahun mengabdi untuk pendidikan anak-anak Balikpapan
          </p>
        </motion.div>

        {/* Tab Switcher with layoutId */}
        <div className="flex justify-center gap-2 mb-12">
          {[
            { id: "about", label: "Profil", icon: Building2 },
            { id: "visi", label: "Visi & Misi", icon: Eye },
            { id: "sejarah", label: "Sejarah", icon: Target },
          ].map(({ id, label, icon: Icon }) => (
            <button
              key={id}
              onClick={() => setActiveTab(id)}
              className="relative flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold transition-colors"
            >
              {activeTab === id && (
                <motion.div
                  layoutId="activeTabBadge"
                  className="absolute inset-0 bg-primary rounded-xl shadow-lg shadow-primary/25"
                  transition={{ type: "spring", stiffness: 400, damping: 30 }}
                />
              )}
              <span className={`relative z-10 flex items-center gap-2 ${activeTab === id ? "text-white" : "text-muted hover:text-foreground"}`}>
                <Icon size={16} />
                {label}
              </span>
            </button>
          ))}
        </div>

        {/* Tab Content with AnimatePresence */}
        <AnimatePresence mode="wait">
          {activeTab === "about" && (
            <motion.div
              key="about"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.4 }}
              className="max-w-4xl mx-auto"
            >
              <div className="bg-white rounded-3xl p-8 sm:p-12 shadow-lg border border-border/50">
                <p className="text-foreground/80 text-lg leading-relaxed">
                  {aboutText.description}
                </p>
              </div>
            </motion.div>
          )}

          {activeTab === "visi" && (
            <motion.div
              key="visi"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.4 }}
              className="max-w-4xl mx-auto grid md:grid-cols-2 gap-6"
            >
              <div className="bg-white rounded-3xl p-8 shadow-lg border border-border/50">
                <div className="w-14 h-14 bg-primary-50 rounded-2xl flex items-center justify-center mb-5">
                  <Eye className="text-primary" size={28} />
                </div>
                <h3 className="font-heading font-bold text-xl text-foreground mb-4">Visi</h3>
                <p className="text-foreground/70 leading-relaxed">{aboutText.visi}</p>
              </div>
              <div className="bg-white rounded-3xl p-8 shadow-lg border border-border/50">
                <div className="w-14 h-14 bg-secondary/10 rounded-2xl flex items-center justify-center mb-5">
                  <Target className="text-secondary" size={28} />
                </div>
                <h3 className="font-heading font-bold text-xl text-foreground mb-4">Misi</h3>
                <ul className="space-y-3">
                  {aboutText.misi.map((item, i) => (
                    <li key={i} className="flex items-start gap-3">
                      <span className="mt-1.5 w-2 h-2 bg-primary rounded-full shrink-0" />
                      <span className="text-foreground/70 text-sm leading-relaxed">{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </motion.div>
          )}

          {activeTab === "sejarah" && (
            <motion.div
              key="sejarah"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.4 }}
              className="max-w-3xl mx-auto"
            >
              <div className="relative">
                <div className="absolute left-6 sm:left-8 top-0 bottom-0 w-0.5 bg-gradient-to-b from-primary via-primary-light to-primary-dark" />

                <div className="space-y-8">
                  {timeline.map((item, index) => (
                    <motion.div
                      key={index}
                      initial={{ opacity: 0, x: -30 }}
                      whileInView={{ opacity: 1, x: 0 }}
                      viewport={{ once: true }}
                      transition={{ duration: 0.5, delay: index * 0.1 }}
                      className="relative flex gap-6 sm:gap-8"
                    >
                      <div className="relative z-10 shrink-0">
                        <div className="w-12 h-12 sm:w-16 sm:h-16 bg-primary rounded-2xl flex items-center justify-center shadow-lg shadow-primary/25">
                          <Building2 className="text-white" size={20} />
                        </div>
                      </div>
                      <div className="bg-white rounded-2xl p-6 shadow-md border border-border/50 flex-1 hover:shadow-xl transition-shadow">
                        <span className="inline-block bg-primary-50 text-primary text-xs font-bold px-3 py-1 rounded-full mb-3">
                          {item.year}
                        </span>
                        <h4 className="font-heading font-bold text-lg text-foreground mb-2">
                          {item.title}
                        </h4>
                        <p className="text-foreground/70 text-sm leading-relaxed">
                          {item.description}
                        </p>
                      </div>
                    </motion.div>
                  ))}
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </section>
  );
}
