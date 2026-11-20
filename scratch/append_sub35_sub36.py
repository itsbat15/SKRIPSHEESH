import os

master_path = r'DRAFT PROPOSAL MD\BAB 3\BAB_3_DESAIN_DAN_IMPLEMENTASI.md'
with open(master_path, 'r', encoding='utf-8') as f:
    content = f.read()

sub35_path = r'DRAFT PROPOSAL MD\BAB 3\3.5_Spesifikasi_Teknis.md'
with open(sub35_path, 'r', encoding='utf-8') as f:
    sub35_text = f.read()

sub36_path = r'DRAFT PROPOSAL MD\BAB 3\3.6_Jadwal_Pembuatan_Prototipe.md'
with open(sub36_path, 'r', encoding='utf-8') as f:
    sub36_text = f.read()

# Replace the text of Gambar 3.17 to the perfected version if needed, and append Subbab 3.5 and 3.6
# Remove any trailing '---' at the end of master_path
trimmed_content = content.rstrip()
if trimmed_content.endswith('---'):
    trimmed_content = trimmed_content[:-3].rstrip()

new_content = trimmed_content + "\n\n---\n\n" + sub35_text + "\n\n---\n\n" + sub36_text + "\n"

with open(master_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated BAB_3_DESAIN_DAN_IMPLEMENTASI.md successfully!")
print("New total lines:", len(new_content.splitlines()))

