"use client";
import Image from "next/image";
import { MapPin, Clock, Phone, MessageCircle, ArrowUp } from "lucide-react";
import { motion } from "framer-motion";
import { siteConfig, branches } from "../data/siteData";

export default function Footer() {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <>
      {/* Footer */}
      <footer id="kontak" className="bg-secondary-dark text-white overflow-hidden">
        {/* Top CTA Bar */}
        <div className="bg-gradient-to-r from-primary to-primary-dark">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 flex flex-col sm:flex-row items-center justify-between gap-6">
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5 }}
            >
              <h3 className="font-heading font-bold text-2xl text-white mb-1">
                Siap Bergabung dengan Bimbel Artha?
              </h3>
              <p className="text-white/80 text-sm">
                Konsultasi gratis sekarang juga! Kami siap membantu putra-putri Anda.
              </p>
            </motion.div>

            <motion.a
              href={`https://wa.me/${siteConfig.whatsapp}?text=Hallo%20kak%2C%20saya%20mau%20tanya%20tentang%20Bimbel%20Artha`}
              target="_blank"
              rel="noopener noreferrer"
              whileHover={{ scale: 1.05, translateY: -3 }}
              whileTap={{ scale: 0.95 }}
              className="shrink-0 flex items-center gap-2 bg-white text-primary-dark font-bold px-8 py-4 rounded-2xl shadow-xl hover:shadow-2xl transition-all"
            >
              <MessageCircle size={20} />
              Hubungi via WhatsApp
            </motion.a>
          </div>
        </div>

        {/* Main Footer */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-10">
            {/* Column 1: Brand */}
            <div>
              <div className="flex items-center gap-3 mb-5">
                <div className="w-10 h-10 rounded-xl overflow-hidden bg-white/10 p-1">
                  <Image
                    src="/images/bimbelarthalogo-1.png"
                    alt="Logo Bimbel Artha"
                    width={40}
                    height={40}
                    className="object-contain"
                  />
                </div>
                <div>
                  <p className="font-heading font-bold text-lg">Bimbel Artha</p>
                  <p className="text-white/50 text-xs">Sejak 1997</p>
                </div>
              </div>
              <p className="text-white/60 text-sm leading-relaxed mb-5">
                Bimbingan Belajar terpercaya di Balikpapan dengan 8 cabang dan pengajar berpengalaman.
              </p>
              {/* Social Links */}
              <div className="flex gap-3">
                {[
                  { label: "TikTok", href: siteConfig.socialMedia.tiktok },
                  { label: "Instagram", href: siteConfig.socialMedia.instagram },
                  { label: "Facebook", href: siteConfig.socialMedia.facebook },
                ].map((social) => (
                  <motion.a
                    key={social.label}
                    href={social.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    whileHover={{ scale: 1.15, rotate: 5 }}
                    whileTap={{ scale: 0.9 }}
                    className="w-10 h-10 bg-white/10 hover:bg-primary rounded-xl flex items-center justify-center text-white/70 hover:text-white transition-colors text-xs font-bold"
                    title={social.label}
                  >
                    {social.label.charAt(0)}
                  </motion.a>
                ))}
              </div>
            </div>

            {/* Column 2: Navigasi */}
            <div>
              <h4 className="font-heading font-bold text-sm uppercase tracking-wider text-white/40 mb-5">
                Navigasi
              </h4>
              <ul className="space-y-3">
                {["Beranda", "Tentang Kami", "Layanan", "Lokasi Cabang", "Tim Pengajar", "FAQ"].map(
                  (link) => (
                    <li key={link}>
                      <a
                        href={`#${link.toLowerCase().replace(/\s/g, "-")}`}
                        className="text-white/60 hover:text-primary text-sm transition-colors"
                      >
                        {link}
                      </a>
                    </li>
                  )
                )}
              </ul>
            </div>

            {/* Column 3: Kontak */}
            <div>
              <h4 className="font-heading font-bold text-sm uppercase tracking-wider text-white/40 mb-5">
                Kontak
              </h4>
              <ul className="space-y-4">
                <li className="flex items-start gap-3">
                  <MapPin size={16} className="text-primary shrink-0 mt-0.5" />
                  <span className="text-white/60 text-sm leading-relaxed">
                    {siteConfig.address}
                  </span>
                </li>
                <li className="flex items-center gap-3">
                  <Phone size={16} className="text-primary shrink-0" />
                  <span className="text-white/60 text-sm">{siteConfig.phone}</span>
                </li>
                <li className="flex items-center gap-3">
                  <Clock size={16} className="text-primary shrink-0" />
                  <span className="text-white/60 text-sm">
                    Senin - Sabtu: 07.30 - 20.30 WITA
                  </span>
                </li>
              </ul>
            </div>

            {/* Column 4: Cabang */}
            <div>
              <h4 className="font-heading font-bold text-sm uppercase tracking-wider text-white/40 mb-5">
                Cabang Kami
              </h4>
              <div className="grid grid-cols-2 gap-2">
                {branches.map((branch) => (
                  <a
                    key={branch.id}
                    href="#cabang"
                    className="flex items-center gap-2 text-white/60 hover:text-primary text-sm transition-colors py-1"
                  >
                    <span className="w-5 h-5 bg-white/10 rounded text-[10px] font-bold flex items-center justify-center">
                      {branch.id}
                    </span>
                    {branch.name}
                  </a>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="border-t border-white/10">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex flex-col sm:flex-row items-center justify-between gap-4">
            <p className="text-white/40 text-sm">
              © {new Date().getFullYear()} Bimbel Artha Balikpapan. All Rights Reserved.
            </p>
            <p className="text-white/30 text-xs">
              Rancang Bangun oleh Mahasiswa Tugas Akhir
            </p>
          </div>
        </div>
      </footer>

      {/* Floating WhatsApp Button */}
      <motion.a
        href={`https://wa.me/${siteConfig.whatsapp}?text=Hallo%20kak%2C%20saya%20mau%20bertanya%20tentang%20Bimbel%20Artha`}
        target="_blank"
        rel="noopener noreferrer"
        whileHover={{ scale: 1.15 }}
        whileTap={{ scale: 0.9 }}
        className="fixed bottom-6 right-6 z-50 w-14 h-14 bg-[#25D366] text-white rounded-full shadow-xl shadow-[#25D366]/30 flex items-center justify-center transition-all animate-pulse-glow"
        title="Chat via WhatsApp"
      >
        <MessageCircle size={28} />
      </motion.a>

      {/* Scroll to top */}
      <motion.button
        onClick={scrollToTop}
        whileHover={{ scale: 1.15 }}
        whileTap={{ scale: 0.9 }}
        className="fixed bottom-6 left-6 z-50 w-12 h-12 bg-secondary/80 hover:bg-secondary text-white rounded-full shadow-lg flex items-center justify-center transition-all backdrop-blur-sm"
        title="Kembali ke atas"
      >
        <ArrowUp size={20} />
      </motion.button>
    </>
  );
}
