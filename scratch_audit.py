import os

ref_dir = 'JURNAL/34_REFERENSI_TXT'

def audit_paper(fname, terms):
    p = os.path.join(ref_dir, fname)
    if not os.path.exists(p):
        print(f"FILE NOT FOUND: {fname}")
        return
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        t = f.read()
    t_lower = t.lower()
    print(f"\n==============================")
    print(f"FILE: {fname}")
    for term in terms:
        cnt = t_lower.count(term.lower())
        print(f"  term '{term}': {cnt} found")
        if cnt > 0:
            idx = t_lower.find(term.lower())
            snippet = t[max(0, idx-40):min(len(t), idx+140)].replace('\n', ' ')
            print(f"    -> snippet: ...{snippet}...")

# 1. Point 1: Requirements
audit_paper('33_Dzhurov_dkk_2009_Personal_Extreme_Programming.txt', ['requirements phase', 'functional and non-functional requirements'])
audit_paper('26_Sommerville_2011_Software_Engineering.txt', ['requirements document', 'functional and non-functional requirements'])
audit_paper('06_Febrianto_dkk_2020_JuTISI_SINTA3.txt', ['user story', 'acceptance criteria'])
audit_paper('13_Musofa_dkk_2025_JTIIK_SINTA2.txt', ['user story', 'requirement'])
audit_paper('23_Fikri_Arthawan_2020_Multitek_SINTA4.txt', ['requirements', 'user story'])
audit_paper('14_Apriyanti_dkk_2024_JATI_SINTA4.txt', ['user story', 'kebutuhan'])

# 2. Point 2: Planning
audit_paper('33_Dzhurov_dkk_2009_Personal_Extreme_Programming.txt', ['planning phase', 'set of tasks', 'major design decisions'])
audit_paper('28_Beck_Andres_2004_Extreme_Programming_Explained.txt', ['planning', 'weekly cycle'])
audit_paper('13_Musofa_dkk_2025_JTIIK_SINTA2.txt', ['planning', 'story point', 'estimasi'])
audit_paper('06_Febrianto_dkk_2020_JuTISI_SINTA3.txt', ['story point', 'fibonacci', 'product backlog'])
audit_paper('29_Cohn_2004_User_Stories_Applied.txt', ['story point', 'fibonacci'])
audit_paper('23_Fikri_Arthawan_2020_Multitek_SINTA4.txt', ['planning', 'jadwal'])
audit_paper('02_Kurniawan_2018_JTIIK_SINTA2.txt', ['jadwal', 'perencanaan'])

# 3. Point 3: Iteration Initialization
audit_paper('33_Dzhurov_dkk_2009_Personal_Extreme_Programming.txt', ['iteration initialization', 'time recording'])
audit_paper('32_Agarwal_Umphress_2008_Single_Person_Extreme_Programming.txt', ['taskprioritylist', 'tasks'])
audit_paper('13_Musofa_dkk_2025_JTIIK_SINTA2.txt', ['iteration initialization', 'velocity'])
audit_paper('23_Fikri_Arthawan_2020_Multitek_SINTA4.txt', ['iteration initialization'])
audit_paper('02_Kurniawan_2018_JTIIK_SINTA2.txt', ['time recording', 'iterasi'])

# 4. Point 4: Design
audit_paper('33_Dzhurov_dkk_2009_Personal_Extreme_Programming.txt', ['design phase', 'simple design'])
audit_paper('27_Pressman_Maxim_2010_Software_Engineering.txt', ['simple design', 'unified modeling language'])
audit_paper('05_Zakaria_dkk_2023_JuTISI_SINTA3.txt', ['bpmn', 'uml'])
audit_paper('34_Hasanah_Untari_2020_Buku_Ajar_RPL.txt', ['use case diagram', 'class diagram', 'activity diagram'])
audit_paper('02_Kurniawan_2018_JTIIK_SINTA2.txt', ['use case diagram', 'class diagram', 'activity diagram'])
audit_paper('31_Chen_1976_ER_Model.txt', ['entity-relationship'])
audit_paper('23_Fikri_Arthawan_2020_Multitek_SINTA4.txt', ['design', 'low fidelity prototype', 'entity relationship diagram'])
audit_paper('16_Wiarso_Anwar_2024_JATI_SINTA4.txt', ['wireframe', 'antarmuka', 'tailwindcss'])

# 5. Point 5: Implementation
audit_paper('33_Dzhurov_dkk_2009_Personal_Extreme_Programming.txt', ['implementation phase', 'unit testing', 'code refactoring', 'code reviews'])
audit_paper('26_Sommerville_2011_Software_Engineering.txt', ['implementation', 'refactoring'])
audit_paper('23_Fikri_Arthawan_2020_Multitek_SINTA4.txt', ['implementation', 'unit testing', 'refactor'])
audit_paper('14_Apriyanti_dkk_2024_JATI_SINTA4.txt', ['laravel', 'framework'])
audit_paper('13_Musofa_dkk_2025_JTIIK_SINTA2.txt', ['implementasi', 'laravel', 'kode'])
audit_paper('16_Wiarso_Anwar_2024_JATI_SINTA4.txt', ['code review', 'coding standard'])
audit_paper('32_Agarwal_Umphress_2008_Single_Person_Extreme_Programming.txt', ['coding standard', 'baseline'])

# 6. Point 6: System Testing
audit_paper('33_Dzhurov_dkk_2009_Personal_Extreme_Programming.txt', ['system testing phase', 'defect recording', 'defect type standard'])
audit_paper('27_Pressman_Maxim_2010_Software_Engineering.txt', ['black-box testing', 'equivalence partitioning'])
audit_paper('22_Widarti_Akbar_2026_JOISM_SINTA4.txt', ['black box', 'pengujian'])
audit_paper('01_Yuanita_dkk_2022_JUTIF_SINTA2.txt', ['pengujian sistem', 'kebutuhan'])
audit_paper('14_Apriyanti_dkk_2024_JATI_SINTA4.txt', ['black box testing', 'user acceptance testing'])
audit_paper('03_Fajriansyah_dkk_2026_JRIS_SINTA3.txt', ['black box', 'pengujian', 'uat'])

# 7. Point 7: Retrospective
audit_paper('33_Dzhurov_dkk_2009_Personal_Extreme_Programming.txt', ['retrospective', 'process improvement proposal'])
audit_paper('28_Beck_Andres_2004_Extreme_Programming_Explained.txt', ['root-cause analysis'])
audit_paper('13_Musofa_dkk_2025_JTIIK_SINTA2.txt', ['retrospektive', 'evaluasi'])
audit_paper('23_Fikri_Arthawan_2020_Multitek_SINTA4.txt', ['retrospective', 'kesimpulan'])
audit_paper('14_Apriyanti_dkk_2024_JATI_SINTA4.txt', ['retrospective', 'evaluasi', 'iterasi'])
audit_paper('32_Agarwal_Umphress_2008_Single_Person_Extreme_Programming.txt', ['iteration release', 'post mortem'])

