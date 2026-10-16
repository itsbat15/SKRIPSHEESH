"use client";
import { useState, useMemo, useEffect } from "react";
import {
  Users,
  ShieldCheck,
  Building2,
  Plus,
  Search,
  Filter,
  CheckCircle2,
  AlertCircle,
  Key,
  Edit,
  UserCheck,
  UserX,
  X,
  Save,
  Lock
} from "lucide-react";
import {
  allUsers,
  allBranches
} from "@/data/mockSuperAdminData";
import { useTheme } from "@/components/dashboard/ThemeProvider";

const B = "#111118";
const S = "4px 4px 0 0 #111118";

export default function SuperAdminUsersPage() {
  const { theme } = useTheme();
  const isDark = theme === "dark";

  const [usersList, setUsersList] = useState(allUsers);
  const [search, setSearch] = useState("");
  const [filterRole, setFilterRole] = useState("all");

  const [showAddModal, setShowAddModal] = useState(false);
  const [newUserData, setNewUserData] = useState({
    name: "",
    email: "",
    role: "branch_admin",
    branch_id: 1,
    password: "",
  });

  const [editingUser, setEditingUser] = useState(null);

  // Close modal on Escape key press
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") {
        setShowAddModal(false);
        setEditingUser(null);
      }
    };
    if (showAddModal || editingUser) {
      window.addEventListener("keydown", handleKeyDown);
      return () => window.removeEventListener("keydown", handleKeyDown);
    }
  }, [showAddModal, editingUser]);

  // Enriched users list
  const enrichedUsers = useMemo(() => {
    return usersList.map((u) => {
      const branch = allBranches.find((b) => b.id === u.branch_id);
      return {
        ...u,
        branch,
      };
    });
  }, [usersList]);

  // Filtered
  const filtered = useMemo(() => {
    return enrichedUsers.filter((u) => {
      if (filterRole !== "all" && u.role !== filterRole) return false;
      if (search) {
        const q = search.toLowerCase();
        const name = u.name.toLowerCase();
        const email = u.email.toLowerCase();
        const branchName = (u.branch?.branch_name || "").toLowerCase();
        if (!name.includes(q) && !email.includes(q) && !branchName.includes(q)) return false;
      }
      return true;
    });
  }, [enrichedUsers, filterRole, search]);

  const handleAddUser = (e) => {
    e.preventDefault();
    const newUser = {
      id: usersList.length + 1,
      name: newUserData.name,
      email: newUserData.email,
      role: newUserData.role,
      branch_id: newUserData.role === "super_admin" ? null : parseInt(newUserData.branch_id),
      is_active: true,
      last_login_at: "Belum pernah login",
    };

    setUsersList([...usersList, newUser]);
    setShowAddModal(false);
    setNewUserData({ name: "", email: "", role: "branch_admin", branch_id: 1, password: "" });
  };

  const handleToggleStatus = (userId) => {
    setUsersList((prev) =>
      prev.map((u) => (u.id === userId ? { ...u, is_active: !u.is_active } : u))
    );
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="p-2 rounded-xl bg-[#2727E6] text-white border-2 border-[#111118] shadow-[2px_2px_0_0_#111118]">
              <ShieldCheck size={20} />
            </span>
            <h2 className="font-heading font-black text-2xl text-slate-900 dark:text-white">
              Manajemen Akun Pengguna &amp; Hak Akses
            </h2>
          </div>
          <p className="text-xs sm:text-sm mt-1 text-slate-500 dark:text-slate-400">
            Daftar pengguna terdaftar, otoritas Super Admin (Owner), dan Admin Cabang (Menu 2.6)
          </p>
        </div>

        <button
          onClick={() => setShowAddModal(true)}
          style={{ border: `2px solid ${B}`, boxShadow: S }}
          className="inline-flex items-center gap-2 text-xs font-black uppercase tracking-wide px-4 py-2.5 rounded-lg bg-[#2727E6] text-white hover:opacity-95"
        >
          <Plus size={14} /> Tambah Akun Staf Baru
        </button>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#2727E6", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-blue-200">Total Pengguna</p>
          <p className="font-heading font-black text-3xl">{usersList.length} Akun</p>
          <p className="text-[11px] text-blue-100 mt-1">Terdaftar dalam basis data</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#1EAB55", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-emerald-200">Akun Aktif</p>
          <p className="font-heading font-black text-3xl">
            {usersList.filter((u) => u.is_active).length} Akun
          </p>
          <p className="text-[11px] text-emerald-100 mt-1">Dapat login ke sistem</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#FF6600", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-4 text-white"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-orange-200">Super Admin (Pusat)</p>
          <p className="font-heading font-black text-3xl">
            {usersList.filter((u) => u.role === "super_admin").length} Orang
          </p>
          <p className="text-[11px] text-orange-100 mt-1">Owner &amp; Bendahara Pusat</p>
        </div>

        <div
          style={{ backgroundColor: isDark ? "#1e293b" : "#FFD600", border: `2.5px solid ${B}`, boxShadow: S }}
          className="rounded-2xl p-4 text-slate-900"
        >
          <p className="text-xs font-bold uppercase tracking-wider mb-1 text-slate-800">Admin Cabang</p>
          <p className="font-heading font-black text-3xl">
            {usersList.filter((u) => u.role === "branch_admin").length} Orang
          </p>
          <p className="text-[11px] text-slate-700 mt-1">Petugas Frontdesk 8 Cabang</p>
        </div>
      </div>

      {/* Filter and Search Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 bg-white dark:bg-slate-900 p-3.5 rounded-xl border-2 border-[#111118]">
        <div className="relative flex-1 min-w-[220px]">
          <Search size={15} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            type="text"
            placeholder="Cari nama atau email pengguna..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full pl-9 pr-3 py-2 rounded-lg text-xs font-medium border-2 border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 outline-none"
          />
        </div>

        <div className="flex items-center gap-2">
          <select
            value={filterRole}
            onChange={(e) => setFilterRole(e.target.value)}
            className="text-xs font-bold p-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 outline-none"
          >
            <option value="all">Semua Peran (Role)</option>
            <option value="super_admin">Super Admin (Pusat)</option>
            <option value="branch_admin">Branch Admin (Frontdesk Cabang)</option>
          </select>
        </div>
      </div>

      {/* Main Table: User Accounts */}
      <div
        style={{
          backgroundColor: isDark ? "#1e293b" : "#ffffff",
          border: `2px solid ${B}`,
          boxShadow: S,
        }}
        className="rounded-xl overflow-hidden"
      >
        <div className="p-4 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
          <h3 className="font-heading font-black text-base text-slate-900 dark:text-slate-100 flex items-center gap-2">
            <Users size={18} className="text-[#2727E6]" />
            Daftar Akun Pengguna ({filtered.length} pengguna)
          </h3>
          <span className="text-xs text-slate-500 font-bold">Autentikasi: Password Hashed</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              <tr className="bg-[#111118] text-white/80">
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Nama Staf / Admin</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Email Login</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Role (Peran)</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Cabang Tugas</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Terakhir Login</th>
                <th className="text-left px-4 py-3 font-black uppercase tracking-wider">Status</th>
                <th className="text-center px-4 py-3 font-black uppercase tracking-wider">Aksi</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200 dark:divide-slate-800">
              {filtered.length === 0 ? (
                <tr>
                  <td colSpan={7} className="p-8 text-center bg-white dark:bg-slate-900">
                    <div className="max-w-xs mx-auto space-y-2">
                      <p className="text-sm font-bold text-slate-800 dark:text-slate-200">Tidak ada staf ditemukan</p>
                      <p className="text-xs text-slate-500">Coba ubah kata kunci pencarian atau sesuaikan filter role pengguna.</p>
                      <button
                        onClick={() => {
                          setSearch("");
                          setFilterRole("all");
                        }}
                        className="text-xs font-bold text-[#2727E6] dark:text-blue-400 underline hover:no-underline"
                      >
                        Reset Filter Pengguna
                      </button>
                    </div>
                  </td>
                </tr>
              ) : (
                filtered.map((user, idx) => {
                  const isSuper = user.role === "super_admin";

                  return (
                    <tr
                      key={user.id}
                      className={`hover:bg-slate-50 dark:hover:bg-slate-800/50 transition-colors ${
                        idx % 2 === 0 ? "bg-white dark:bg-slate-900" : "bg-slate-50/50 dark:bg-slate-900/40"
                      }`}
                    >
                    <td className="px-4 py-3">
                      <strong className="text-xs text-slate-900 dark:text-slate-100 block">
                        {user.name}
                      </strong>
                      <span className="text-[11px] text-slate-600 dark:text-slate-400">User ID #{user.id}</span>
                    </td>

                    <td className="px-4 py-3 font-mono text-slate-600 dark:text-slate-300">
                      {user.email}
                    </td>

                    <td className="px-4 py-3">
                      {isSuper ? (
                        <span className="inline-flex items-center gap-1 text-[10px] font-black uppercase px-2 py-0.5 rounded bg-indigo-100 text-indigo-800 dark:bg-indigo-950 dark:text-indigo-300 border border-indigo-300">
                          <ShieldCheck size={11} /> Super Admin
                        </span>
                      ) : (
                        <span className="inline-flex items-center gap-1 text-[10px] font-black uppercase px-2 py-0.5 rounded bg-slate-100 text-slate-800 dark:bg-slate-800 dark:text-slate-200 border border-slate-300">
                          Branch Admin
                        </span>
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {isSuper ? (
                        <span className="font-semibold text-slate-500 italic">Semua Cabang (Pusat)</span>
                      ) : (
                        <span className="font-bold text-slate-800 dark:text-slate-200">
                          {user.branch?.branch_name || `Cabang ${user.branch_id}`}
                        </span>
                      )}
                    </td>

                    <td className="px-4 py-3 text-slate-500 font-mono text-[11px]">
                      {user.last_login_at}
                    </td>

                    <td className="px-4 py-3">
                      {user.is_active ? (
                        <span className="inline-flex items-center gap-1 text-[10px] font-bold text-emerald-600 uppercase">
                          <CheckCircle2 size={11} /> Aktif
                        </span>
                      ) : (
                        <span className="inline-flex items-center gap-1 text-[10px] font-bold text-rose-600 uppercase">
                          <AlertCircle size={11} /> Nonaktif
                        </span>
                      )}
                    </td>

                    <td className="px-4 py-3 text-center">
                      <div className="flex items-center justify-center gap-1.5">
                        <button
                          onClick={() => handleToggleStatus(user.id)}
                          style={{ border: `1.5px solid ${B}` }}
                          className={`px-2 py-1 rounded-md text-[10px] font-bold ${
                            user.is_active
                              ? "bg-rose-50 text-rose-700 hover:bg-rose-100"
                              : "bg-emerald-50 text-emerald-700 hover:bg-emerald-100"
                          }`}
                        >
                          {user.is_active ? "Nonaktifkan" : "Aktifkan"}
                        </button>
                        <button
                          onClick={() => alert(`Reset password link terkirim ke email ${user.email}!`)}
                          title="Reset Password"
                          style={{ border: `1.5px solid ${B}` }}
                          className="p-1 rounded-md bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200"
                        >
                          <Key size={13} />
                        </button>
                      </div>
                    </td>
                  </tr>
                );
              }))}
            </tbody>
          </table>
        </div>
      </div>

      {/* MODAL: TAMBAH AKUN BARU */}
      {showAddModal && (
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
                <Plus size={18} className="text-[#2727E6]" />
                Tambah Akun Staf Baru
              </h3>
              <button
                onClick={() => setShowAddModal(false)}
                className="p-1 rounded-lg border border-slate-300 dark:border-slate-700"
              >
                <X size={16} />
              </button>
            </div>

            <form onSubmit={handleAddUser} className="space-y-4 text-xs">
              <div>
                <label className="font-black uppercase text-slate-600 dark:text-slate-400 block mb-1">Nama Lengkap Staf:</label>
                <input
                  type="text"
                  placeholder="Contoh: Riko Saputra"
                  value={newUserData.name}
                  onChange={(e) => setNewUserData({ ...newUserData, name: e.target.value })}
                  required
                  className="w-full p-2.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white font-bold outline-none"
                />
              </div>

              <div>
                <label className="font-black uppercase text-slate-600 dark:text-slate-400 block mb-1">Email Resmi (Login):</label>
                <input
                  type="email"
                  placeholder="Contoh: riko@bimbelartha.id"
                  value={newUserData.email}
                  onChange={(e) => setNewUserData({ ...newUserData, email: e.target.value })}
                  required
                  className="w-full p-2.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white outline-none"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="font-black uppercase text-slate-600 dark:text-slate-400 block mb-1">Peran (Role):</label>
                  <select
                    value={newUserData.role}
                    onChange={(e) => setNewUserData({ ...newUserData, role: e.target.value })}
                    className="w-full p-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white font-bold outline-none"
                  >
                    <option value="branch_admin">Branch Admin</option>
                    <option value="super_admin">Super Admin</option>
                  </select>
                </div>

                {newUserData.role === "branch_admin" && (
                  <div>
                    <label className="font-black uppercase text-slate-500 block mb-1">Cabang Penugasan:</label>
                    <select
                      value={newUserData.branch_id}
                      onChange={(e) => setNewUserData({ ...newUserData, branch_id: e.target.value })}
                      className="w-full p-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white font-bold outline-none"
                    >
                      {allBranches.map((br) => (
                        <option key={br.id} value={br.id}>
                          {br.branch_name}
                        </option>
                      ))}
                    </select>
                  </div>
                )}
              </div>

              <div>
                <label className="font-black uppercase text-slate-500 block mb-1">Kata Sandi Default:</label>
                <input
                  type="password"
                  placeholder="Minimal 8 karakter"
                  value={newUserData.password}
                  onChange={(e) => setNewUserData({ ...newUserData, password: e.target.value })}
                  required
                  className="w-full p-2.5 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white outline-none"
                />
              </div>

              <div className="flex justify-end gap-2 pt-2 border-t">
                <button
                  type="button"
                  onClick={() => setShowAddModal(false)}
                  className="px-3 py-2 rounded-lg font-bold border border-slate-300 dark:border-slate-700"
                >
                  Batal
                </button>
                <button
                  type="submit"
                  style={{ border: `2px solid ${B}`, boxShadow: "2px 2px 0 0 #111118" }}
                  className="px-4 py-2 rounded-lg font-black uppercase text-white bg-[#2727E6] hover:opacity-95"
                >
                  Simpan Akun
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
