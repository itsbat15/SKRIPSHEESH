from pathlib import Path
import json, re, hashlib

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'DOKUMEN MD/REVISI_TERPADU_2026-10-25'
p=ROOT/'DOKUMEN MD/PERANCANGAN BASIS DATA (SKEMA & ERD).md'
meta=json.loads((OUT/'SKEMA_TERSTRUKTUR.json').read_text(encoding='utf-8'))
t=p.read_text(encoding='utf-8')
tables=meta['tables']
names={x['name'] for x in tables}
checks={}
checks['tables_exactly_23']=len(tables)==23 and len(names)==23
erd=t.split('```mermaid',1)[1].split('```',1)[0]
erd_names=set(re.findall(r'^    ([a-z_]+) \{',erd,re.M))
checks['all_erd_entities_match_metadata']=erd_names==names
dictionary=re.findall(r'^### 3\.\d+ ([a-z_]+):',t,re.M)
checks['dictionary_names_match_metadata']=set(dictionary)==names and len(dictionary)==23
field_checks=[]
fk_checks=[]
nullable_checks=[]
for tb in tables:
    e=re.search(r'^    '+tb['name']+r' \{\n(.*?)^    \}',erd,re.M|re.S).group(1)
    efields={re.split(r'\s+',row.strip())[1] for row in e.splitlines() if row.strip()}
    field_checks.append(efields=={f['name'] for f in tb['fields']})
    for f in tb['fields']:
        if f['ref']:
            parent,field=f['ref'].split('.')
            valid=parent in names and field in {q['name'] for q in next(b for b in tables if b['name']==parent)['fields']}
            fk_checks.append(valid)
            left='|o' if f['nullable'] else '||'
            right='o|' if f['unique'] else 'o{'
            nullable_checks.append(f'    {parent} {left}--{right} {tb["name"]} : "{f["name"]}"' in erd)
checks['all_erd_fields_match_metadata']=all(field_checks)
checks['all_foreign_keys_have_valid_targets']=all(fk_checks)
checks['all_51_foreign_keys_have_matching_cardinality']=len(nullable_checks)==51 and all(nullable_checks)
matrix=t.split('## 6. Hubungan',1)[1].split('## 7.',1)[0]
checks['all_tables_covered_by_usecase_mapping']=all(re.search(r'\b'+name+r'\b',matrix) for name in names)
checks['fourteen_usecases_present']=set(re.findall(r'UC-\d{2}',matrix))=={f'UC-{i:02d}' for i in range(14)}
checks['no_long_dash_in_prose']='\u2014' not in t and '\u2013' not in t
codefree=re.sub(r'```.*?```','',t,flags=re.S)
checks['no_double_dash_in_prose']='--' not in re.sub(r'^\|.*$','',codefree,flags=re.M)
short=[]
for block in codefree.split('\n\n'):
    if not block.strip() or block.startswith(('#','|','- ')):continue
    sentences=[s for s in re.split(r'(?<=[.!?])\s+',block) if s.strip()]
    if len(sentences)<2:short.append(block)
checks['all_prose_paragraphs_have_two_sentences']=not short
counts=[]
for block in t.split('\n\n'):
    if block.startswith('|'):
        counts.append(len({len(re.split(r'(?<!\\)\|',line)) for line in block.splitlines() if line.startswith('|')})==1)
checks['all_markdown_tables_have_matching_columns']=all(counts)
checks['explicitly_design_not_executed_ddl']='belum merupakan migrasi SQL yang telah dieksekusi' in t
checks['review_is_single_final_decision']=next(f for q in tables if q['name']=='payment_reviews' for f in q['fields'] if f['name']=='payment_id')['unique']
checks['bankmatch_source_columns_are_optional_and_unique']=all(next(f for q in tables if q['name']=='bank_matches' for f in q['fields'] if f['name']==col)['nullable'] and next(f for q in tables if q['name']=='bank_matches' for f in q['fields'] if f['name']==col)['unique'] for col in ('payment_id','cash_batch_id'))
result=dict(date='2026-10-25', scope='Document structure, field metadata and declared rules only; not SQL migration, concurrency test, or partner acceptance', file=str(p), sha256=hashlib.sha256(p.read_bytes()).hexdigest(),tables=len(tables),fields=sum(len(q['fields']) for q in tables),foreign_keys=len(fk_checks),checks=checks,short_paragraphs=short,implementation_tests_executed=False)
(OUT/'VALIDASI_BASIS_DATA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(passed=sum(checks.values()),total=len(checks),failed=[k for k,v in checks.items() if not v],tables=len(tables),fields=result['fields'],foreign_keys=len(fk_checks)),ensure_ascii=False))
assert all(checks.values()),result
