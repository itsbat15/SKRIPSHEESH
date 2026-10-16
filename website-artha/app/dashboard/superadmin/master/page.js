"use client";
import { useState } from "react";
import {
  Database,
  Coins,
  Percent,
  BookOpen,
  MessageCircle,
  Calendar,
  Save,
  CheckCircle2,
  Edit,
  Plus,
  Trash2,
  HelpCircle,
  Tag
} from "lucide-react";
import {
  feeTariffs,
  discountRules,
  learningPrograms,
  academicYears
} from "@/data/mockFrontdeskData";
import { waTemplates } from "@/data/mockSuperAdminData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";

const formatRp = (n) =>
  new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", minimumFractionDigits: 0 }).format(n || 0);

export default function SuperAdminMasterPage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const [activeTab, setActiveTab] = useState("tariffs");

  // Editable states
  const [tariffsList, setTariffsList] = useState(feeTariffs);
  const [discountsList, setDiscountsList] = useState(discountRules);
  const [programsList, setProgramsList] = useState(learningPrograms);
  const [templatesList, setTemplatesList] = useState(waTemplates);
  const [yearsList, setYearsList] = useState(academicYears);

  const [saveSuccess, setSaveSuccess] = useState(false);

  const triggerSaveNotification = () => {
    setSaveSuccess(true);
    setTimeout(() => setSaveSuccess(false), 2500);
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="p-2 rounded-xl bg-[#2727E6] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]">
              <Database size={20} />
            </span>
            <h2 className="font-heading font-black text-2xl text-slate-900 dark:text-white">
              Master Data &amp; Konfigurasi Sistem
            </h2>
          </div>
          <p className="text-xs sm:text-sm mt-1 text-slate-500 dark:text-slate-400">
            Pusat konfigurasi tarif les, diskon keluarga, program belajar, dan template pesan WhatsApp (Menu 2.5)
          </p>
        </div>

        {saveSuccess && (
          <span className="px-3 py-1.5 rounded-lg bg-emerald-100 text-emerald-800 font-bold text-xs border border-emerald-300 animate-in fade-in flex items-center gap-1.5">
            <CheckCircle2 size={14} /> Konfigurasi Berhasil Disimpan!
          </span>
        )}
      </div>

      {/* Navigation Tabs */}
      <div className="flex items-center gap-2 overflow-x-auto pb-1 border-b border-slate-200 dark:border-slate-800">
        {[
          { id: "tariffs", label: "Master Tarif SPP & Modul", icon: Coins },
          { id: "discounts", label: "Master Diskon & Aturan", icon: Percent },
          { id: "programs", label: "Program Belajar", icon: BookOpen },
          { id: "templates", label: "Template WhatsApp", icon: MessageCircle },
          { id: "years", label: "Tahun Ajaran", icon: Calendar },
        ].map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-black uppercase whitespace-nowrap transition-all ${
                isActive
                  ? "bg-[#2727E6] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]"
                  : "bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-slate-700"
              }`}
            >
              <Icon size={14} />
              {tab.label}
            </button>
          );
        })}
      </div>

      {/* TAB 1: MASTER TARIF SPP & MODUL */}
      {activeTab === "tariffs" && (
        <div
          style={{
            backgroundColor: isDark ? "#1e293b" : "#ffffff",
            border: `2px solid ${B}`,
            boxShadow: S,
          }}
          className="rounded-2xl p-5 space-y-4"
        >
          <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
            <div>
              <h3 className="font-heading font-black text-base text-slate-900 dark:text-white">
                Daftar Tarif Resmi SPP &amp; Biaya Modul (Tabel `fee_tariffs`)
              </h3>
              <p className="text-xs text-slate-500">Berlaku serentak di semua 8 cabang Bimbel Artha</p>
            </div>
            <button
              onClick={triggerSaveNotification}
              style={{ border: `1.5px solid ${B}`, boxShadow: "2px 2px 0 0 #111118" }}
              className="px-3 py-1.5 rounded-lg text-xs font-black uppercase bg-[#1EAB55] text-white hover:opacity-90 flex items-center gap-1.5"
            >
              <Save size={13} /> Simpan Perubahan
            </button>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-xs">
              <thead>
                <tr className="bg-[#111118] text-white/80">
                  <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Jenjang</th>
                  <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Kelas Sekolah</th>
                  <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Jenis Biaya</th>
                  <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Keterangan</th>
                  <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Nominal Tarif (Rp)</th>
                  <th className="text-center px-4 py-3 font-black uppercase tracking-wider">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200 dark:divide-slate-800">
                {tariffsList.map((t, idx) => (
                  <tr key={t.id} className={idx % 2 === 0 ? "bg-white dark:bg-slate-900" : "bg-slate-50 dark:bg-slate-800/40"}>
                    <td className="px-4 py-3 font-black text-slate-900 dark:text-white">{t.grade_level}</td>
                    <td className="px-4 py-3 font-medium">
                      {t.grade_level === "TK"
                        ? "TK (Calistung)"
                        : `Kelas ${t.class_grade_start} - ${t.class_grade_end}`}
                    </td>
                    <td className="px-4 py-3">
                      <span className="font-mono uppercase font-bold text-[10px] px-2 py-0.5 rounded bg-blue-100 text-blue-800">
                        {t.fee_type === "spp_monthly" ? "SPP Bulanan" : "Modul Semester"}
                      </span>
                    </td>
                    <td className="px-4 py-3 text-slate-600 dark:text-slate-300">{t.description}</td>
                    <td className="px-4 py-3">
                      <input
                        type="number"
                        value={t.amount}
                        onChange={(e) => {
                          const val = parseInt(e.target.value) || 0;
                          setTariffsList((prev) =>
                            prev.map((item) => (item.id === t.id ? { ...item, amount: val } : item))
                          );
                        }}
                        className="w-32 p-1.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-mono font-bold text-xs outline-none"
                      />
                    </td>
                    <td className="px-4 py-3 text-center">
                      <span className="text-[10px] font-bold text-emerald-600 uppercase">Aktif</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* TAB 2: MASTER DISKON */}
      {activeTab === "discounts" && (
        <div
          style={{
            backgroundColor: isDark ? "#1e293b" : "#ffffff",
            border: `2px solid ${B}`,
            boxShadow: S,
          }}
          className="rounded-2xl p-5 space-y-4"
        >
          <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
            <div>
              <h3 className="font-heading font-black text-base text-slate-900 dark:text-white">
                Aturan Potongan &amp; Diskon (Tabel `discount_rules`)
              </h3>
              <p className="text-xs text-slate-500">Potongan otomatis pada saat verifikasi pendaftaran dan tagihan</p>
            </div>
            <button
              onClick={triggerSaveNotification}
              style={{ border: `1.5px solid ${B}`, boxShadow: "2px 2px 0 0 #111118" }}
              className="px-3 py-1.5 rounded-lg text-xs font-black uppercase bg-[#1EAB55] text-white hover:opacity-90 flex items-center gap-1.5"
            >
              <Save size={13} /> Simpan Perubahan
            </button>
          </div>

          <div className="space-y-3">
            {discountsList.map((d) => (
              <div
                key={d.id}
                className="p-4 rounded-xl border-2 border-emerald-300 dark:border-emerald-800 bg-emerald-50 dark:bg-emerald-950/30 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 text-xs"
              >
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <Tag size={16} className="text-emerald-600" />
                    <strong className="font-heading font-black text-sm text-emerald-900 dark:text-emerald-100">
                      {d.discount_name}
                    </strong>
                    <span className="px-2 py-0.5 rounded text-[10px] font-black uppercase bg-emerald-200 text-emerald-800">
                      Tipe: {d.discount_type}
                    </span>
                  </div>
                  <p className="text-slate-600 dark:text-slate-300">{d.description}</p>
                </div>

                <div className="flex items-center gap-2">
                  <span className="font-bold text-slate-700 dark:text-slate-300">Nilai Potongan:</span>
                  <input
                    type="number"
                    value={d.discount_value}
                    onChange={(e) => {
                      const val = parseInt(e.target.value) || 0;
                      setDiscountsList((prev) =>
                        prev.map((item) => (item.id === d.id ? { ...item, discount_value: val } : item))
                      );
                    }}
                    className="w-32 p-1.5 rounded-lg border-2 border-emerald-400 bg-white dark:bg-slate-900 font-mono font-bold text-xs outline-none"
                  />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 3: PROGRAM BELAJAR */}
      {activeTab === "programs" && (
        <div
          style={{
            backgroundColor: isDark ? "#1e293b" : "#ffffff",
            border: `2px solid ${B}`,
            boxShadow: S,
          }}
          className="rounded-2xl p-5 space-y-4"
        >
          <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
            <div>
              <h3 className="font-heading font-black text-base text-slate-900 dark:text-white">
                Program Belajar Bimbel Artha (Tabel `learning_programs`)
              </h3>
              <p className="text-xs text-slate-500">Kategori program kursus dan bimbingan belajar</p>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {programsList.map((prog) => (
              <div
                key={prog.id}
                className="p-4 rounded-xl border-2 border-[#111118] bg-slate-50 dark:bg-slate-900/60 space-y-2 text-xs"
              >
                <div className="flex items-center justify-between">
                  <strong className="font-heading font-black text-base text-slate-900 dark:text-white">
                    {prog.program_name}
                  </strong>
                  <span className="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-blue-100 text-blue-800">
                    Aktif
                  </span>
                </div>
                <p className="text-slate-600 dark:text-slate-300">{prog.description}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 4: TEMPLATE WHATSAPP */}
      {activeTab === "templates" && (
        <div
          style={{
            backgroundColor: isDark ? "#1e293b" : "#ffffff",
            border: `2px solid ${B}`,
            boxShadow: S,
          }}
          className="rounded-2xl p-5 space-y-4"
        >
          <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
            <div>
              <h3 className="font-heading font-black text-base text-slate-900 dark:text-white">
                Template Pesan Pengingat WhatsApp Otomatis
              </h3>
              <p className="text-xs text-slate-500">Placeholder otomatis: &#123;parent_name&#125;, &#123;student_name&#125;, &#123;due_date&#125;, &#123;total_amount&#125;</p>
            </div>
            <button
              onClick={triggerSaveNotification}
              style={{ border: `1.5px solid ${B}`, boxShadow: "2px 2px 0 0 #111118" }}
              className="px-3 py-1.5 rounded-lg text-xs font-black uppercase bg-[#1EAB55] text-white hover:opacity-90 flex items-center gap-1.5"
            >
              <Save size={13} /> Simpan Template
            </button>
          </div>

          <div className="space-y-4">
            {templatesList.map((tmpl) => (
              <div key={tmpl.id} className="space-y-1.5 text-xs">
                <div className="flex items-center justify-between">
                  <label className="font-black uppercase text-slate-700 dark:text-slate-300">
                    {tmpl.template_name} ({tmpl.template_type}):
                  </label>
                  <span className="text-[10px] font-mono text-slate-400">ID: #{tmpl.id}</span>
                </div>
                <textarea
                  rows={3}
                  value={tmpl.message_body}
                  onChange={(e) => {
                    const text = e.target.value;
                    setTemplatesList((prev) =>
                      prev.map((t) => (t.id === tmpl.id ? { ...t, message_body: text } : t))
                    );
                  }}
                  className="w-full p-2.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white outline-none"
                />
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 5: TAHUN AJARAN */}
      {activeTab === "years" && (
        <div
          style={{
            backgroundColor: isDark ? "#1e293b" : "#ffffff",
            border: `2px solid ${B}`,
            boxShadow: S,
          }}
          className="rounded-2xl p-5 space-y-4"
        >
          <div className="flex items-center justify-between border-b pb-3 border-slate-200 dark:border-slate-800">
            <div>
              <h3 className="font-heading font-black text-base text-slate-900 dark:text-white">
                Periode Tahun Ajaran (Tabel `academic_years`)
              </h3>
              <p className="text-xs text-slate-500">Atur periode akademik yang sedang berjalan</p>
            </div>
          </div>

          <div className="space-y-3">
            {yearsList.map((y) => (
              <div
                key={y.id}
                className={`p-4 rounded-xl border-2 flex items-center justify-between text-xs ${
                  y.is_active
                    ? "border-emerald-500 bg-emerald-50 dark:bg-emerald-950/30"
                    : "border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-900/40"
                }`}
              >
                <div>
                  <strong className="font-heading font-black text-base text-slate-900 dark:text-white block">
                    Tahun Ajaran {y.name}
                  </strong>
                  <span className="text-slate-500">
                    Periode: {y.start_date} s/d {y.end_date}
                  </span>
                </div>

                <div>
                  {y.is_active ? (
                    <span className="px-3 py-1 rounded-full text-xs font-black uppercase bg-emerald-200 text-emerald-800 border border-emerald-400">
                      Aktif Berjalan
                    </span>
                  ) : (
                    <button
                      onClick={() => {
                        setYearsList((prev) =>
                          prev.map((item) => ({ ...item, is_active: item.id === y.id }))
                        );
                        triggerSaveNotification();
                      }}
                      className="px-3 py-1 rounded-lg text-xs font-bold border border-slate-400 bg-white dark:bg-slate-800"
                    >
                      Jadikan Aktif
                    </button>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
