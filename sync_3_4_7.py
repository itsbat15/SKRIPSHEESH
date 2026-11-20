import os
import re

# Read standalone 3.4.7
with open('DRAFT PROPOSAL MD/BAB 3/3.4 Konsep Prototipe MD/3.4.7_Perancangan_Antarmuka_Pengguna.md', 'r', encoding='utf-8') as f:
    standalone_text = f.read()

# -------------------------------------------------------------
# 1. SYNC TO 3.4_Konsep_Prototipe.md
# -------------------------------------------------------------
p_parent1 = 'DRAFT PROPOSAL MD/BAB 3/3.4 Konsep Prototipe MD/3.4_Konsep_Prototipe.md'
with open(p_parent1, 'r', encoding='utf-8') as f:
    parent1_text = f.read()

# Convert standalone headings to parent1 headings:
# # 3.4.7 -> ## 3.4.7
# ## A. -> ### A.
# ## B. -> ### B.
# ## C. -> ### C.
# Image path: <../ASET BAB 3/ -> <ASET BAB 3/
text_for_parent1 = standalone_text
text_for_parent1 = text_for_parent1.replace('# 3.4.7', '## 3.4.7')
text_for_parent1 = text_for_parent1.replace('## A.', '### A.')
text_for_parent1 = text_for_parent1.replace('## B.', '### B.')
text_for_parent1 = text_for_parent1.replace('## C.', '### C.')
text_for_parent1 = text_for_parent1.replace('<../ASET BAB 3/', '<ASET BAB 3/')

# Replace ## 3.4.7 section in parent1
parent1_updated = re.sub(r'## 3\.4\.7.*', text_for_parent1, parent1_text, flags=re.DOTALL)
with open(p_parent1, 'w', encoding='utf-8') as f:
    f.write(parent1_updated)
print(f'Synced to {p_parent1}')

# -------------------------------------------------------------
# 2. SYNC TO BAB_3_DESAIN_DAN_IMPLEMENTASI.md
# -------------------------------------------------------------
p_parent2 = 'DRAFT PROPOSAL MD/BAB 3/BAB_3_DESAIN_DAN_IMPLEMENTASI.md'
with open(p_parent2, 'r', encoding='utf-8') as f:
    parent2_text = f.read()

# Convert standalone headings to parent2 headings:
# # 3.4.7 -> ### 3.4.7
# ## A. -> #### A.
# ## B. -> #### B.
# ## C. -> #### C.
# Image path: <../ASET BAB 3/ -> <ASET BAB 3/
text_for_parent2 = standalone_text
text_for_parent2 = text_for_parent2.replace('# 3.4.7', '### 3.4.7')
text_for_parent2 = text_for_parent2.replace('## A.', '#### A.')
text_for_parent2 = text_for_parent2.replace('## B.', '#### B.')
text_for_parent2 = text_for_parent2.replace('## C.', '#### C.')
text_for_parent2 = text_for_parent2.replace('<../ASET BAB 3/', '<ASET BAB 3/')

# Replace ### 3.4.7 section in parent2
parent2_updated = re.sub(r'### 3\.4\.7.*', text_for_parent2 + '\n\n---\n', parent2_text, flags=re.DOTALL)
with open(p_parent2, 'w', encoding='utf-8') as f:
    f.write(parent2_updated)
print(f'Synced to {p_parent2}')

