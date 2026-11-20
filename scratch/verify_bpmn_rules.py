import re

with open('DRAFT PROPOSAL MD/BAB 2/2.1.3_Business_Process_Model_and_Notation.md', encoding='utf-8') as f:
    text = f.read()

# 1. Em-dash check
dashes = re.findall(r'[—–]|--', text)
print(f'Em-dashes found: {len(dashes)}')

# 2. Check sentences starting with digits
sentences = [s.strip() for s in re.split(r'[\.\?!]\s+', text) if s.strip()]
digit_starts = [s for s in sentences if re.match(r'^\d+', s) and not s.startswith('2.1.3') and not s.startswith('2.2')]
print(f'Sentences starting with digits: {len(digit_starts)}')
for ds in digit_starts:
    print('  Digit start:', ds[:50])

# 3. Check paragraphs
paragraphs = [p.strip() for p in text.split('\n\n') if p.strip() and not p.strip().startswith('#') and not p.strip().startswith('|') and not p.strip().startswith('Tabel')]
print(f'Prose paragraphs: {len(paragraphs)}')
for idx, p in enumerate(paragraphs):
    s_count = len([s for s in re.split(r'[\.\?!]\s+', p) if s.strip()])
    print(f'  Paragraph {idx+1}: {s_count} sentences')

# 4. Red citations
red_citations = re.findall(r'<span style="color: red;">\(.*?\)</span>', text)
print(f'Red citations found: {len(red_citations)}')
for rc in red_citations:
    print('  Citation:', rc)

