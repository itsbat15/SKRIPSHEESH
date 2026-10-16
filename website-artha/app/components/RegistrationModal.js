"use client";
import { useState } from "react";
import { X, Send, User, Phone, BookOpen, MapPin, CheckCircle2 } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { programs, branches, siteConfig } from "../data/siteData";

export default function RegistrationModal({ isOpen, onClose }) {
  const [formData, setFormData] = useState({
    studentName: "",
    parentName: "",
    phone: "",
    program: "",
    branch: "",
  });
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const buildWhatsAppMessage = () => {
    const selectedProgram = programs.find((p) => p.id === formData.program);
    const selectedBranch = branches.find((b) => b.id === parseInt(formData.branch));

    const message = `Hallo kak, saya ingin mendaftarkan anak saya di Bimbel Artha.

📋 *DATA PENDAFTARAN*
👤 Nama Siswa: ${formData.studentName}
👨‍👩‍👧 Nama Orang Tua: ${formData.parentName}
📱 No. HP: ${formData.phone}
📚 Program: ${selectedProgram?.title || "-"}
📍 Cabang: ${selectedBranch?.name || "-"} (${selectedBranch?.address || "-"})

Mohon informasi lebih lanjut mengenai jadwal dan biaya pendaftaran. Terima kasih 🙏`;

    return encodeURIComponent(message);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const selectedBranch = branches.find((b) => b.id === parseInt(formData.branch));
    const whatsappNumber = selectedBranch?.whatsapp || siteConfig.whatsapp;
    const message = buildWhatsAppMessage();
    const waUrl = `https://wa.me/${whatsappNumber}?text=${message}`;

    window.open(waUrl, "_blank");
    setIsSubmitted(true);
  };

  const handleClose = () => {
    setIsSubmitted(false);
    setFormData({ studentName: "", parentName: "", phone: "", program: "", branch: "" });
    onClose();
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-[60] flex items-center justify-center p-4">
          {/* Backdrop */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.3 }}
            className="absolute inset-0 bg-secondary-dark/60 backdrop-blur-sm"
            onClick={handleClose}
          />

          {/* Modal */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.9, y: 20 }}
            transition={{ type: "spring", stiffness: 350, damping: 25 }}
            className="relative bg-white rounded-3xl shadow-2xl w-full max-w-lg max-h-[90vh] overflow-y-auto z-10"
          >
            {/* Close button */}
            <button
              onClick={handleClose}
              className="absolute top-4 right-4 p-2 rounded-xl text-muted hover:text-foreground hover:bg-surface transition-colors z-10"
            >
              <X size={20} />
            </button>

            {isSubmitted ? (
              /* Success State */
              <motion.div
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                className="p-8 sm:p-10 text-center"
              >
                <div className="w-20 h-20 bg-accent/10 rounded-full flex items-center justify-center mx-auto mb-6">
                  <CheckCircle2 size={40} className="text-accent" />
                </div>
                <h3 className="font-heading font-bold text-2xl text-foreground mb-3">
                  Pendaftaran Terkirim! 🎉
                </h3>
                <p className="text-muted mb-6 leading-relaxed">
                  Ringkasan pendaftaran telah dikirim melalui WhatsApp. Tim Bimbel Artha akan
                  segera menghubungi Anda untuk konfirmasi.
                </p>
                <motion.button
                  onClick={handleClose}
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  className="bg-primary hover:bg-primary-dark text-white font-semibold px-8 py-3 rounded-xl transition-colors"
                >
                  Tutup
                </motion.button>
              </motion.div>
            ) : (
              /* Form */
              <>
                {/* Header */}
                <div className="bg-gradient-to-r from-primary to-primary-dark p-8 rounded-t-3xl">
                  <h3 className="font-heading font-bold text-2xl text-white mb-1">
                    Pendaftaran Murid Baru
                  </h3>
                  <p className="text-white/80 text-sm">
                    Isi formulir berikut dan kirim ringkasan via WhatsApp
                  </p>
                </div>

                <form onSubmit={handleSubmit} className="p-8 space-y-5">
                  {/* Nama Siswa */}
                  <div>
                    <label className="flex items-center gap-2 text-sm font-semibold text-foreground mb-2">
                      <User size={16} className="text-primary" />
                      Nama Siswa
                    </label>
                    <input
                      type="text"
                      name="studentName"
                      value={formData.studentName}
                      onChange={handleChange}
                      required
                      placeholder="Masukkan nama lengkap siswa"
                      className="w-full px-4 py-3 rounded-xl border border-border bg-surface text-foreground placeholder:text-muted/60 focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-all"
                    />
                  </div>

                  {/* Nama Orang Tua */}
                  <div>
                    <label className="flex items-center gap-2 text-sm font-semibold text-foreground mb-2">
                      <User size={16} className="text-secondary" />
                      Nama Orang Tua / Wali
                    </label>
                    <input
                      type="text"
                      name="parentName"
                      value={formData.parentName}
                      onChange={handleChange}
                      required
                      placeholder="Masukkan nama orang tua/wali"
                      className="w-full px-4 py-3 rounded-xl border border-border bg-surface text-foreground placeholder:text-muted/60 focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-all"
                    />
                  </div>

                  {/* No. HP */}
                  <div>
                    <label className="flex items-center gap-2 text-sm font-semibold text-foreground mb-2">
                      <Phone size={16} className="text-accent" />
                      No. HP / WhatsApp
                    </label>
                    <input
                      type="tel"
                      name="phone"
                      value={formData.phone}
                      onChange={handleChange}
                      required
                      placeholder="08xxxxxxxxxx"
                      className="w-full px-4 py-3 rounded-xl border border-border bg-surface text-foreground placeholder:text-muted/60 focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-all"
                    />
                  </div>

                  {/* Program */}
                  <div>
                    <label className="flex items-center gap-2 text-sm font-semibold text-foreground mb-2">
                      <BookOpen size={16} className="text-primary" />
                      Program yang Dipilih
                    </label>
                    <select
                      name="program"
                      value={formData.program}
                      onChange={handleChange}
                      required
                      className="w-full px-4 py-3 rounded-xl border border-border bg-surface text-foreground focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-all appearance-none"
                    >
                      <option value="">- Pilih Program -</option>
                      {programs.map((prog) => (
                        <option key={prog.id} value={prog.id}>
                          {prog.title} ({prog.subtitle})
                        </option>
                      ))}
                    </select>
                  </div>

                  {/* Cabang */}
                  <div>
                    <label className="flex items-center gap-2 text-sm font-semibold text-foreground mb-2">
                      <MapPin size={16} className="text-primary-dark" />
                      Pilihan Cabang
                    </label>
                    <select
                      name="branch"
                      value={formData.branch}
                      onChange={handleChange}
                      required
                      className="w-full px-4 py-3 rounded-xl border border-border bg-surface text-foreground focus:outline-none focus:ring-2 focus:ring-primary/30 focus:border-primary transition-all appearance-none"
                    >
                      <option value="">- Pilih Cabang -</option>
                      {branches.map((branch) => (
                        <option key={branch.id} value={branch.id}>
                          {branch.name} - {branch.address}
                        </option>
                      ))}
                    </select>
                  </div>

                  {/* Submit */}
                  <motion.button
                    type="submit"
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    className="w-full flex items-center justify-center gap-2 bg-accent hover:bg-accent-dark text-white font-bold text-base px-6 py-4 rounded-xl shadow-lg shadow-accent/25 hover:shadow-accent/40 transition-all"
                  >
                    <Send size={18} />
                    Kirim via WhatsApp
                  </motion.button>

                  <p className="text-center text-muted text-xs">
                    Data Anda aman & akan dikirim langsung ke WhatsApp cabang yang dipilih
                  </p>
                </form>
              </>
            )}
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
}
