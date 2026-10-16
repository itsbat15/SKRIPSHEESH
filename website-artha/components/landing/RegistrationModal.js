"use client";
import { useState } from "react";
import { X } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { branches, programs } from "@/data/siteData";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";

export default function RegistrationModal({ isOpen, onClose }) {
  const [formData, setFormData] = useState({
    namaAnak: "",
    kelasSekolah: "",
    namaOrtu: "",
    noHP: "",
    cabang: "",
    program: "",
    sesi: "",
  });

  const handleChange = (field, value) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const selectedBranch = branches.find((b) => b.name === formData.cabang);
    const waNumber = selectedBranch?.whatsapp || "6285102233666";
    const message = `Halo Bimbel ${formData.cabang}, saya ingin mendaftarkan anak saya:\n\n` +
      `👤 Nama Anak: ${formData.namaAnak}\n` +
      `🏫 Kelas: ${formData.kelasSekolah}\n` +
      `👨‍👩‍👦 Nama Orang Tua: ${formData.namaOrtu}\n` +
      `📞 No. HP: ${formData.noHP}\n` +
      `📚 Program: ${formData.program}\n` +
      `⏰ Sesi: ${formData.sesi}\n\n` +
      `Mohon informasi lebih lanjut mengenai pendaftaran. Terima kasih!`;
    
    window.open(`https://wa.me/${waNumber}?text=${encodeURIComponent(message)}`, "_blank");
    onClose();
  };

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="sm:max-w-[500px] rounded-2xl p-0 overflow-hidden border-0">
        {/* Header */}
        <div className="bg-gradient-to-r from-primary to-primary-dark px-6 py-5 text-white">
          <DialogHeader>
            <DialogTitle className="text-white font-heading text-xl font-bold">
              Formulir Pendaftaran
            </DialogTitle>
            <DialogDescription className="text-white/80 text-sm">
              Isi formulir di bawah dan kami akan menghubungi Anda via WhatsApp
            </DialogDescription>
          </DialogHeader>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="p-6 space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label htmlFor="namaAnak">Nama Anak</Label>
              <Input
                id="namaAnak"
                placeholder="Nama lengkap anak"
                value={formData.namaAnak}
                onChange={(e) => handleChange("namaAnak", e.target.value)}
                required
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="kelasSekolah">Kelas Sekolah</Label>
              <Input
                id="kelasSekolah"
                placeholder="Contoh: 5 SD"
                value={formData.kelasSekolah}
                onChange={(e) => handleChange("kelasSekolah", e.target.value)}
                required
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label htmlFor="namaOrtu">Nama Orang Tua</Label>
              <Input
                id="namaOrtu"
                placeholder="Nama orang tua/wali"
                value={formData.namaOrtu}
                onChange={(e) => handleChange("namaOrtu", e.target.value)}
                required
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="noHP">No. HP / WhatsApp</Label>
              <Input
                id="noHP"
                type="tel"
                placeholder="08xxxxxxxxxx"
                value={formData.noHP}
                onChange={(e) => handleChange("noHP", e.target.value)}
                required
              />
            </div>
          </div>

          <div className="space-y-2">
            <Label>Pilih Cabang</Label>
            <Select onValueChange={(val) => handleChange("cabang", val)} required>
              <SelectTrigger>
                <SelectValue placeholder="Pilih cabang terdekat" />
              </SelectTrigger>
              <SelectContent>
                {branches.map((b) => (
                  <SelectItem key={b.id} value={b.name}>
                    {b.name} — {b.address}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label>Program</Label>
              <Select onValueChange={(val) => handleChange("program", val)} required>
                <SelectTrigger>
                  <SelectValue placeholder="Pilih program" />
                </SelectTrigger>
                <SelectContent>
                  {programs.map((p) => (
                    <SelectItem key={p.id} value={p.title}>
                      {p.title} ({p.subtitle})
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label>Sesi Belajar</Label>
              <Select onValueChange={(val) => handleChange("sesi", val)} required>
                <SelectTrigger>
                  <SelectValue placeholder="Pilih sesi" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="Pagi (07.30-09.00)">Pagi (07.30-09.00)</SelectItem>
                  <SelectItem value="Pagi 2 (09.00-10.30)">Pagi 2 (09.00-10.30)</SelectItem>
                  <SelectItem value="Siang (14.00-15.30)">Siang (14.00-15.30)</SelectItem>
                  <SelectItem value="Sore 1 (15.30-17.00)">Sore 1 (15.30-17.00)</SelectItem>
                  <SelectItem value="Sore 2 (17.00-18.30)">Sore 2 (17.00-18.30)</SelectItem>
                  <SelectItem value="Malam (19.00-20.30)">Malam (19.00-20.30)</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>

          <div className="pt-2">
            <Button
              type="submit"
              size="lg"
              className="w-full bg-primary hover:bg-primary-dark text-white font-bold rounded-xl shadow-lg shadow-primary/25"
            >
              Kirim via WhatsApp
            </Button>
          </div>

          <p className="text-xs text-center text-slate-500">
            Data Anda akan dikirim langsung ke WhatsApp cabang yang dipilih
          </p>
        </form>
      </DialogContent>
    </Dialog>
  );
}
