"use client";
import Image from "next/image";
import { motion } from "framer-motion";
import { teachers } from "../data/siteData";

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.08,
    },
  },
};

const teacherVariants = {
  hidden: { opacity: 0, scale: 0.8, y: 20 },
  visible: {
    opacity: 1,
    scale: 1,
    y: 0,
    transition: { duration: 0.4, ease: "easeOut" },
  },
};

export default function TeamSection() {
  return (
    <section id="tim" className="py-20 lg:py-28 bg-surface overflow-hidden">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <span className="inline-block bg-secondary/10 text-secondary font-semibold text-sm px-4 py-1.5 rounded-full mb-4">
            Tim Pengajar
          </span>
          <h2 className="font-heading font-extrabold text-3xl sm:text-4xl lg:text-5xl text-foreground mb-4">
            Pengajar{" "}
            <span className="gradient-text-blue">Berpengalaman & Telaten</span>
          </h2>
          <p className="text-muted text-lg max-w-2xl mx-auto">
            Tim pengajar kami yang ulet dan berdedikasi siap membantu putra-putri Anda meraih prestasi
          </p>
        </motion.div>

        {/* Team Grid */}
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-50px" }}
          className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-6"
        >
          {teachers.map((teacher, index) => (
            <motion.div
              key={index}
              variants={teacherVariants}
              whileHover={{ scale: 1.08 }}
              className="group text-center cursor-pointer"
            >
              <div className="relative w-24 h-24 sm:w-28 sm:h-28 mx-auto mb-4 rounded-2xl overflow-hidden shadow-md group-hover:shadow-xl group-hover:shadow-primary/20 transition-all duration-300">
                <Image
                  src={teacher.image}
                  alt={teacher.name}
                  fill
                  className="object-cover"
                  onError={(e) => {
                    e.target.src = "/images/bimbelarthalogo-1.png";
                  }}
                />
                <div className="absolute inset-0 bg-gradient-to-t from-secondary-dark/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
              </div>
              <h4 className="font-heading font-bold text-sm text-foreground">
                {teacher.name}
              </h4>
              <p className="text-muted text-xs mt-0.5">{teacher.role}</p>
              <span className="inline-block mt-1.5 text-[10px] font-semibold bg-primary-50 text-primary px-2 py-0.5 rounded-full">
                {teacher.branch}
              </span>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  );
}
