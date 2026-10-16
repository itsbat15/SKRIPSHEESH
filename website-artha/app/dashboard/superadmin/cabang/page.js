"use client";
import { useState, useEffect } from "react";
import {
  Building2,
  MapPin,
  Phone,
  DoorOpen,
  Users,
  Edit,
  ExternalLink,
  Plus,
  CheckCircle2,
  ArrowRight,
  X,
  Save
} from "lucide-react";
import Link from "next/link";
import { allBranches, allUsers, branchSummaries } from "@/data/mockSuperAdminData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";

export default function SuperAdminCabangPage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const [branchesList, setBranchesList] = useState(allBranches);
  const [editingBranch, setEditingBranch] = useState(null);

  // Close modal on Escape key press
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") {
        setEditingBranch(null);
      }
    };
    if (editingBranch) {
      window.addEventListener("keydown", handleKeyDown);
      return () => window.removeEventListener("keydown", handleKeyDown);
    }
  }, [editingBranch]);
  const [formData, setFormData] = useState({
    branch_name: "",
    address: "",
    phone_wa: "",
    total_rooms: 3,
    is_active: true,
  });

  const handleOpenEdit = (branch) => {
    setEditingBranch(branch);
    setFormData({
      branch_name: branch.branch_name,
      address: branch.address,
      phone_wa: branch.phone_wa,
      total_rooms: branch.total_rooms,
      is_active: branch.is_active,
    });
  };

  const handleSaveEdit = (e) => {
    e.preventDefault();
    if (!editingBranch) return;

    setBranchesList((prev) =>
      prev.map((b) => (b.id === editingBranch.id ? { ...b, ...formData } : b))
    );
    setEditingBranch(null);
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="p-2 rounded-xl bg-[#2727E6] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]">
              <Building2 size={20} />
            </span>
            <h2 className="font-heading font-black text-2xl text-slate-900 dark:text-white">
              Kelola Data 8 Cabang Bimbel Artha
            </h2>
          </div>
          <p className="text-xs sm:text-sm mt-1 text-slate-500 dark:text-slate-400">
            Manajemen informasi lokasi, jumlah ruang kelas, dan admin penanggung jawab (Menu 2.4)
          </p>
        </div>

        <span className="text-xs font-bold px-3 py-1.5 rounded-lg bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-300 flex items-center gap-1.5">
          <CheckCircle2 size={14} /> 8 Cabang Beroperasi Aktif
        </span>
      </div>

      {/* Grid 8 Cabang Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {branchesList.map((branch) => {
          const summary = branchSummaries.find((bs) => bs.branch_id === branch.id);
          const admin = allUsers.find((u) => u.branch_id === branch.id);

          return (
            <div
              key={branch.id}
              style={{
                backgroundColor: isDark ? "#1e293b" : "#ffffff",
                border: `2.5px solid ${B}`,
                boxShadow: S,
              }}
              className="rounded-2xl p-5 flex flex-col justify-between transition-all hover:-translate-y-1 hover:shadow-[6px_6px_0_0_#111118]"
            >
              <div>
                {/* Header Card */}
                <div className="flex items-start justify-between gap-2 mb-2">
                  <div>
                    <h3 className="font-heading font-black text-lg text-slate-900 dark:text-white">
                      {branch.branch_name}
                    </h3>
                    {branch.label && (
                      <span className="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-[#FFD600] text-slate-900 border border-[#111118]">
                        Kantor {branch.label}
                      </span>
                    )}
                  </div>
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-black uppercase bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-300">
                    Aktif
                  </span>
                </div>

                {/* Info Lokasi & Kontak */}
                <div className="space-y-2 text-xs my-4 bg-slate-50 dark:bg-slate-900/60 p-3 rounded-xl border border-slate-200 dark:border-slate-800">
                  <div className="flex items-start gap-2 text-slate-600 dark:text-slate-300">
                    <MapPin size={14} className="text-[#E11D48] shrink-0 mt-0.5" />
                    <span>{branch.address}</span>
                  </div>

                  <div className="flex items-center gap-2 text-slate-600 dark:text-slate-300">
                    <Phone size={14} className="text-[#1EAB55] shrink-0" />
                    <span className="font-mono">{branch.phone_wa}</span>
                  </div>

                  <div className="flex items-center gap-2 text-slate-600 dark:text-slate-300">
                    <DoorOpen size={14} className="text-[#2727E6] shrink-0" />
                    <span>
                      <strong>{branch.total_rooms} Ruang Belajar</strong> (Kapasitas ~{branch.total_rooms * 12} siswa)
                    </span>
                  </div>

                  <div className="flex items-center gap-2 text-slate-600 dark:text-slate-300">
                    <Users size={14} className="text-[#FF6600] shrink-0" />
                    <span>Admin: <strong>{admin?.name || "Belum Ditugaskan"}</strong></span>
                  </div>
                </div>

                {/* Mini Stats */}
                {summary && (
                  <div className="grid grid-cols-2 gap-2 text-[11px] mb-4 p-2.5 rounded-lg bg-slate-100 dark:bg-slate-800/80 font-semibold">
                    <div>
                      <span className="text-slate-400 block text-[10px]">Siswa Aktif:</span>
                      <strong className="text-slate-900 dark:text-white text-xs">{summary.siswa_aktif} Siswa</strong>
                    </div>
                    <div>
                      <span className="text-slate-400 block text-[10px]">Kelas Aktif:</span>
                      <strong className="text-slate-900 dark:text-white text-xs">{summary.kelas_aktif} Kelas</strong>
                    </div>
                  </div>
                )}
              </div>

              {/* Actions */}
              <div className="pt-3 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-2">
                <button
                  onClick={() => handleOpenEdit(branch)}
                  style={{ border: `1.5px solid ${B}` }}
                  className="flex-1 py-1.5 px-2 rounded-lg text-xs font-bold bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:bg-slate-100 flex items-center justify-center gap-1.5"
                >
                  <Edit size={12} /> Edit Cabang
                </button>

                <Link
                  href="/dashboard/frontdesk"
                  title="Masuk sebagai Frontdesk cabang ini"
                  style={{ border: `1.5px solid ${B}` }}
                  className="p-1.5 rounded-lg bg-[#2727E6] text-white hover:opacity-90"
                >
                  <ArrowRight size={14} />
                </Link>
              </div>
            </div>
          );
        })}
      </div>

      {/* MODAL: EDIT CABANG */}
      {editingBranch && (
        <div className="fixed inset-0 z-50 bg-black/60 flex items-center justify-center p-4">
          <div
            style={{
              backgroundColor: isDark ? "#1e293b" : "#fff",
              border: `3px solid ${B}`,
              boxShadow: "6px 6px 0 0 #111118",
            }}
            className="w-full max-w-md rounded-2xl p-6 space-y-4 animate-in fade-in"
          >
            <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
              <h3 className="font-heading font-black text-lg text-slate-900 dark:text-white flex items-center gap-2">
                <Building2 size={18} className="text-[#2727E6]" />
                Edit Data {editingBranch.branch_name}
              </h3>
              <button
                onClick={() => setEditingBranch(null)}
                className="p-1 rounded-lg border border-slate-300 dark:border-slate-700"
              >
                <X size={16} />
              </button>
            </div>

            <form onSubmit={handleSaveEdit} className="space-y-4 text-xs">
              <div>
                <label className="font-black uppercase text-slate-600 dark:text-slate-400 block mb-1">Nama Cabang:</label>
                <input
                  type="text"
                  value={formData.branch_name}
                  onChange={(e) => setFormData({ ...formData, branch_name: e.target.value })}
                  required
                  className="w-full p-2.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white font-bold outline-none"
                />
              </div>

              <div>
                <label className="font-black uppercase text-slate-600 dark:text-slate-400 block mb-1">Alamat Lengkap:</label>
                <input
                  type="text"
                  value={formData.address}
                  onChange={(e) => setFormData({ ...formData, address: e.target.value })}
                  required
                  className="w-full p-2.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white outline-none"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="font-black uppercase text-slate-600 dark:text-slate-400 block mb-1">Nomor WhatsApp Cabang:</label>
                  <input
                    type="text"
                    value={formData.phone_wa}
                    onChange={(e) => setFormData({ ...formData, phone_wa: e.target.value })}
                    required
                    className="w-full p-2.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white font-mono outline-none"
                  />
                </div>
                <div>
                  <label className="font-black uppercase text-slate-600 dark:text-slate-400 block mb-1">Jumlah Ruang Belajar:</label>
                  <input
                    type="number"
                    min={1}
                    max={10}
                    value={formData.total_rooms}
                    onChange={(e) => setFormData({ ...formData, total_rooms: parseInt(e.target.value) || 1 })}
                    required
                    className="w-full p-2.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white font-bold outline-none"
                  />
                </div>
              </div>

              <div className="flex justify-end gap-2 pt-2 border-t">
                <button
                  type="button"
                  onClick={() => setEditingBranch(null)}
                  className="px-3 py-2 rounded-lg font-bold border border-slate-300 dark:border-slate-700"
                >
                  Batal
                </button>
                <button
                  type="submit"
                  style={{ border: `2px solid ${B}`, boxShadow: "2px 2px 0 0 #111118" }}
                  className="px-4 py-2 rounded-lg font-black uppercase text-white bg-[#1EAB55] hover:opacity-95 flex items-center gap-1.5"
                >
                  <Save size={13} /> Simpan Perubahan
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
