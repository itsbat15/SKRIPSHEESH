"use client";
import { useState } from "react";
import { MapPin, Phone, MessageCircle, Navigation } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { branches } from "../data/siteData";

export default function BranchLocations() {
  const [selectedBranch, setSelectedBranch] = useState(branches[0]);

  const getMapUrl = (branch) => {
    return `https://maps.google.com/maps?q=${branch.lat},${branch.lng}&z=15&output=embed`;
  };

  const getDirectionsUrl = (branch) => {
    return `https://www.google.com/maps/dir/?api=1&destination=${branch.lat},${branch.lng}`;
  };

  return (
    <section id="cabang" className="py-20 lg:py-28 bg-white overflow-hidden">
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
            Lokasi Cabang
          </span>
          <h2 className="font-heading font-extrabold text-3xl sm:text-4xl lg:text-5xl text-foreground mb-4">
            <span className="gradient-text">8 Cabang</span> di Balikpapan
          </h2>
          <p className="text-muted text-lg max-w-2xl mx-auto">
            Temukan cabang Bimbel Artha terdekat dari lokasi Anda
          </p>
        </motion.div>

        <div className="grid lg:grid-cols-5 gap-8">
          {/* Branch List */}
          <div className="lg:col-span-2 space-y-3 max-h-[600px] overflow-y-auto pr-2">
            {branches.map((branch, index) => (
              <motion.button
                key={branch.id}
                initial={{ opacity: 0, x: -20 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: index * 0.05 }}
                whileHover={{ scale: 1.01 }}
                onClick={() => setSelectedBranch(branch)}
                className={`w-full text-left p-5 rounded-2xl border transition-all ${
                  selectedBranch.id === branch.id
                    ? "bg-primary-50 border-primary shadow-md shadow-primary/10"
                    : "bg-surface border-border/50 hover:border-primary/30 hover:bg-surface-alt"
                }`}
              >
                <div className="flex items-start gap-4">
                  <div
                    className={`w-10 h-10 rounded-xl flex items-center justify-center shrink-0 transition-colors ${
                      selectedBranch.id === branch.id
                        ? "bg-primary text-white"
                        : "bg-white text-primary border border-border"
                    }`}
                  >
                    <span className="font-heading font-bold text-sm">{branch.id}</span>
                  </div>
                  <div className="flex-1 min-w-0">
                    <h4 className="font-heading font-bold text-base text-foreground">
                      {branch.name}
                      {branch.label && (
                        <span className="ml-2 text-xs bg-primary text-white px-2 py-0.5 rounded-full font-medium">
                          {branch.label}
                        </span>
                      )}
                    </h4>
                    <p className="text-muted text-sm mt-1 flex items-start gap-1.5">
                      <MapPin size={14} className="shrink-0 mt-0.5" />
                      {branch.address}
                    </p>
                    <p className="text-muted text-sm mt-1 flex items-center gap-1.5">
                      <Phone size={14} className="shrink-0" />
                      {branch.phone}
                    </p>
                  </div>
                </div>

                {/* Actions */}
                <AnimatePresence>
                  {selectedBranch.id === branch.id && (
                    <motion.div
                      initial={{ opacity: 0, height: 0 }}
                      animate={{ opacity: 1, height: "auto" }}
                      exit={{ opacity: 0, height: 0 }}
                      transition={{ duration: 0.3 }}
                      className="flex gap-2 mt-4 ml-14 overflow-hidden"
                    >
                      <a
                        href={`https://wa.me/${branch.whatsapp}?text=Hallo%20kak%2C%20saya%20mau%20tanya%20tentang%20Bimbel%20${branch.name}`}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex items-center gap-1.5 bg-accent text-white text-xs font-semibold px-3 py-2 rounded-lg hover:bg-accent-dark transition-colors"
                      >
                        <MessageCircle size={14} />
                        WhatsApp
                      </a>
                      <a
                        href={getDirectionsUrl(branch)}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex items-center gap-1.5 bg-secondary text-white text-xs font-semibold px-3 py-2 rounded-lg hover:bg-secondary-dark transition-colors"
                      >
                        <Navigation size={14} />
                        Rute
                      </a>
                    </motion.div>
                  )}
                </AnimatePresence>
              </motion.button>
            ))}
          </div>

          {/* Map Container */}
          <div className="lg:col-span-3">
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="sticky top-24 bg-surface rounded-3xl overflow-hidden shadow-lg border border-border/50"
            >
              <div className="p-4 bg-white border-b border-border/50">
                <h3 className="font-heading font-bold text-lg text-foreground flex items-center gap-2">
                  <MapPin size={18} className="text-primary" />
                  {selectedBranch.name}
                  {selectedBranch.label && (
                    <span className="text-xs bg-primary-50 text-primary px-2 py-0.5 rounded-full">
                      {selectedBranch.label}
                    </span>
                  )}
                </h3>
                <p className="text-muted text-sm mt-1">{selectedBranch.address}</p>
              </div>
              <div className="relative w-full" style={{ height: "450px" }}>
                <iframe
                  key={selectedBranch.id}
                  src={getMapUrl(selectedBranch)}
                  width="100%"
                  height="100%"
                  style={{ border: 0 }}
                  allowFullScreen
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title={`Peta lokasi ${selectedBranch.name}`}
                />
              </div>
            </motion.div>
          </div>
        </div>
      </div>
    </section>
  );
}
