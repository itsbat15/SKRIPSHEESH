import re

with open('DRAFT PROPOSAL MD/BAB 2/2.1.3_Business_Process_Model_and_Notation.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Dash check
dashes = [d for d in ['\u2014', '\u2013', '--'] if d in content]
print('Dash check:', 'CLEAN' if not dashes else f'FOUND {dashes}')

# 2. Citations check
citations = re.findall(r'<span style="color: red;">\((.*?)\)</span>', content)
print('Citations found:', citations)

# 3. Paragraph lengths
paras = [p.strip() for p in content.split('\n\n') if p.strip() and not p.strip().startswith('|') and not p.strip().startswith('Tabel') and not p.strip().startswith('#') and not p.strip().startswith('![') and not p.strip().startswith('**Gambar')]
print(f'Prose paragraphs count: {len(paras)}')
for i, p in enumerate(paras, 1):
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', p) if s.strip()]
    print(f'  P{i}: {len(sentences)} sentences')
    for s in sentences:
        if re.match(r'^\d', s):
            print(f'    ERROR: Sentence starts with digit: {s[:30]}')

