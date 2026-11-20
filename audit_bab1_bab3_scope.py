import re

with open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 1\BAB 1 PENDAHULUAN.md', encoding='utf-8') as f:
    bab1 = f.read()

with open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\BAB_3_DESAIN_DAN_IMPLEMENTASI.md', encoding='utf-8') as f:
    bab3 = f.read()

print("=== BAB 1 Scope, Roles, Features ===")
for line in bab1.splitlines():
    if any(k in line.lower() for k in ['cabang', 'tentor', 'siswa', 'peran', 'role', 'pendaftaran', 'rekonsiliasi', 'presensi', 'jadwal', 'lingkup', 'batasan']):
        if len(line.strip()) > 30:
            print("  [BAB 1]", line.strip()[:120])

print("\n=== BAB 3 Roles & Use Cases ===")
for line in bab3.splitlines():
    if any(k in line.lower() for k in ['aktor', 'actor', 'use case', 'super admin', 'admin cabang', 'tentor', 'siswa', 'batasan', 'lingkup']):
        if len(line.strip()) > 30:
            print("  [BAB 3]", line.strip()[:120])

