import os
import re

ref_dir = 'JURNAL/34_REFERENSI_TXT'

queries = [
    'time recording',
    'defect recording',
    'process improvement proposal',
    'pip',
    'user acceptance testing',
    'uat',
    'story point',
    'velocity',
    'black box',
    'wireframe',
    'refactor',
    'coding standard',
    'bpmn',
    'iteration release'
]

results = {q: [] for q in queries}

for f in sorted(os.listdir(ref_dir)):
    if f.endswith('.txt'):
        p = os.path.join(ref_dir, f)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            c = fp.read().lower()
        for q in queries:
            if q == 'uat':
                if re.search(r'\buat\b', c):
                    results[q].append(f)
            elif q == 'pip':
                if re.search(r'\bpip\b', c):
                    results[q].append(f)
            else:
                if q in c:
                    results[q].append(f)

for q in queries:
    print(f'=== Term: "{q}" ===')
    for f in results[q]:
        print('  ', f)

