import os

p_as_is = 'DRAFT PROPOSAL MD/BAB 3/3.4 Konsep Prototipe MD/3.4.1_Analisis_Proses_Bisnis_Berjalan_As_Is.md'
p_to_be = 'DRAFT PROPOSAL MD/BAB 3/3.4 Konsep Prototipe MD/3.4.2_Perancangan_Proses_Bisnis_Usulan_To_Be.md'

with open(p_as_is, encoding='utf-8') as f:
    text_as_is = f.read()

with open(p_to_be, encoding='utf-8') as f:
    text_to_be = f.read()

print("=== AS-IS CONTENT ===")
print(text_as_is[:2000])
print("\n" + "="*50 + "\n")
print("=== TO-BE CONTENT ===")
print(text_to_be[:2000])

