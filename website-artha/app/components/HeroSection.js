"use client";
import Image from "next/image";
import { Award, MapPin, GraduationCap, Users, ChevronDown } from "lucide-react";
import { motion } from "framer-motion";
import { siteConfig, trustMetrics } from "../data/siteData";

const iconMap = { Award, MapPin, GraduationCap, Users };

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.15,
      delayChildren: 0.2,
    },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 30 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.6, ease: "easeOut" },
  },
};

export default function HeroSection({ onOpenRegistration }) {
  return (
    <section id="beranda" className="relative min-h-screen flex items-center overflow-hidden">
      {/* Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-secondary-dark via-secondary to-secondary-light" />
      <div
        className="absolute inset-0 opacity-10"
        style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.4'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`,
        }}
      />
      {/* Decorative circles */}
      <div className="absolute -top-40 -right-40 w-96 h-96 bg-primary/20 rounded-full blur-3xl" />
      <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-primary-light/15 rounded-full blur-3xl" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-24 pb-16 w-full">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <motion.div
            variants={containerVariants}
            initial="hidden"
            animate="visible"
            className="text-center lg:text-left"
          >
            <motion.div variants={itemVariants} className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm rounded-full px-4 py-2 mb-6 border border-white/20">
              <span className="w-2 h-2 bg-primary rounded-full animate-pulse" />
              <span className="text-white/90 text-sm font-medium">
                Pendaftaran Murid Baru Dibuka!
              </span>
            </motion.div>

            <motion.h1 variants={itemVariants} className="font-heading font-extrabold text-4xl sm:text-5xl lg:text-6xl text-white leading-tight mb-6">
              Raih{" "}
              <span className="text-primary-light">Prestasi Gemilang</span>{" "}
              Bersama Bimbel Artha
            </motion.h1>

            <motion.p variants={itemVariants} className="text-lg sm:text-xl text-white/80 mb-8 max-w-xl mx-auto lg:mx-0 leading-relaxed">
              {siteConfig.subTagline}. Berdiri sejak 1997 dengan 8 cabang di
              Balikpapan, kami siap membimbing putra-putri Anda meraih cita-cita.
            </motion.p>

            <motion.div variants={itemVariants} className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <motion.button
                onClick={onOpenRegistration}
                whileHover={{ scale: 1.05, translateY: -3 }}
                whileTap={{ scale: 0.95 }}
                className="bg-primary hover:bg-primary-dark text-white font-bold text-base px-8 py-4 rounded-2xl shadow-xl shadow-primary/30 hover:shadow-primary/50 transition-shadow"
              >
                Daftar Sekarang • Gratis Konsultasi
              </motion.button>
              <motion.a
                href="#tentang"
                whileHover={{ scale: 1.03 }}
                whileTap={{ scale: 0.97 }}
                className="flex items-center justify-center gap-2 bg-white/10 hover:bg-white/20 text-white font-semibold text-base px-8 py-4 rounded-2xl border border-white/20 transition-colors"
              >
                Pelajari Lebih Lanjut
                <ChevronDown size={18} />
              </motion.a>
            </motion.div>
          </motion.div>

          {/* Right Image */}
          <motion.div
            initial={{ opacity: 0, x: 50, scale: 0.9 }}
            animate={{ opacity: 1, x: 0, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.3, ease: "easeOut" }}
            className="hidden lg:flex justify-center"
          >
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-br from-primary/30 to-primary-dark/20 rounded-3xl blur-2xl scale-110" />
              <motion.div
                animate={{ y: [0, -10, 0] }}
                transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
                className="relative w-80 h-80 xl:w-96 xl:h-96 rounded-3xl overflow-hidden shadow-2xl border-4 border-white/20"
              >
                <Image
                  src="/images/1739838394989-circle.jpeg"
                  alt="Kegiatan Belajar di Bimbel Artha"
                  fill
                  className="object-cover"
                  priority
                />
              </motion.div>

              {/* Floating badge */}
              <motion.div
                initial={{ opacity: 0, scale: 0.5, y: 20 }}
                animate={{ opacity: 1, scale: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.8 }}
                className="absolute -bottom-4 -left-4 bg-white rounded-2xl p-4 shadow-xl"
              >
                <div className="flex items-center gap-3">
                  <div className="w-12 h-12 bg-primary-50 rounded-xl flex items-center justify-center">
                    <GraduationCap className="text-primary" size={24} />
                  </div>
                  <div>
                    <p className="font-heading font-bold text-foreground text-lg">28+ Tahun</p>
                    <p className="text-muted text-xs">Pengalaman Mendidik</p>
                  </div>
                </div>
              </motion.div>
            </div>
          </motion.div>
        </div>

        {/* Trust Metrics Strip */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, delay: 0.6 }}
          className="mt-16 lg:mt-20"
        >
          <div className="glass rounded-2xl p-6 sm:p-8 shadow-xl">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-6 sm:gap-8">
              {trustMetrics.map((metric, index) => {
                const Icon = iconMap[metric.icon];
                return (
                  <motion.div
                    key={index}
                    whileHover={{ scale: 1.05 }}
                    className="text-center group"
                  >
                    <div className="inline-flex items-center justify-center w-12 h-12 bg-primary-50 rounded-xl mb-3 group-hover:bg-primary transition-colors duration-300">
                      <Icon
                        size={22}
                        className="text-primary group-hover:text-white transition-colors duration-300"
                      />
                    </div>
                    <p className="font-heading font-extrabold text-2xl sm:text-3xl text-foreground">
                      {metric.value}
                    </p>
                    <p className="text-muted text-sm mt-1">{metric.label}</p>
                  </motion.div>
                );
              })}
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
