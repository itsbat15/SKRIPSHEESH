# coding: utf-8
"""
Modul Audit dan Estimasi Persentase AI Writing (Turnitin-like Simulation)
Khusus Naskah Tugas Akhir Sistem Informasi ITK
Bimbingan Belajar ARTHA Balikpapan
"""

import os
import sys
import re
import statistics

BASE_DIR = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD"

TARGET_FILES = {
    "BAB 1": os.path.join(BASE_DIR, "BAB 1", "BAB 1 PENDAHULUAN.md"),
    "BAB 2": os.path.join(BASE_DIR, "BAB 2", "BAB_2_TINJAUAN_PUSTAKA.md"),
    "BAB 3": os.path.join(BASE_DIR, "BAB 3", "BAB_3_DESAIN_DAN_IMPLEMENTASI.md"),
}

AI_CLICHES = [
    "merupakan salah satu",
    "memegang peranan penting",
    "peran penting dalam",
    "dalam era digital",
    "era globalisasi",
    "tidak dapat dipungkiri",
    "oleh karena itu",
    "selain itu",
    "hal ini menunjukkan bahwa",
    "hal ini membuktikan bahwa",
    "dapat disimpulkan bahwa",
    "secara keseluruhan",
    "penting untuk dicatat",
    "memberikan kontribusi",
    "efektif dan efisien",
    "efisien dan efektif",
    "seiring dengan perkembangan",
    "dalam hal ini",
    "tidak hanya",
    "tetapi juga",
    "diharapkan dapat memberikan",
    "sangat krusial untuk",
    "memainkan peran"
]

EMPIRICAL_ANCHORS = [
    "artha", "balikpapan", "cabang", "delapan", "buku besar", "kuitansi",
    "folio", "kasir", "wita", "tentor", "spp", "rupiah", "laci", "memo",
    "peter chen", "bizagi", "sanctum", "next.js", "laravel", "mysql",
    "dzhurov", "sommerville", "laudon", "tuition_bills", "daily_reconciliations"
]

def analyze_paragraph(para_text):
    words = para_text.split()
    word_count = len(words)
    if word_count < 15:
        return None
    
    sentences = [s.strip() for s in re.split(r"[.!?]+", para_text) if len(s.strip().split()) > 3]
    if len(sentences) < 2:
        cv = 0.1
    else:
        sent_lengths = [len(s.split()) for s in sentences]
        avg_len = statistics.mean(sent_lengths)
        std_len = statistics.stdev(sent_lengths) if len(sent_lengths) > 1 else 0
        cv = std_len / avg_len if avg_len > 0 else 0
    
    para_lower = para_text.lower()
    
    # 1. Skor keseragaman kalimat (Burstiness) -> bobot 40%
    if cv < 0.20:
        burst_score = 40.0
    elif cv < 0.30:
        burst_score = 30.0
    elif cv < 0.40:
        burst_score = 15.0
    else:
        burst_score = 0.0
        
    # 2. Skor frasa klise AI -> bobot 35%
    cliche_hits = [c for c in AI_CLICHES if c in para_lower]
    cliche_score = min(len(cliche_hits) * 15.0, 35.0)
    
    # 3. Skor prediktabilitas struktur kalimat -> bobot 25%
    starters = [s.split()[0].lower() for s in sentences if len(s.split()) > 0]
    unique_starters = len(set(starters))
    if len(starters) > 2 and (unique_starters / len(starters)) < 0.7:
        starter_penalty = 20.0
    else:
        starter_penalty = 5.0
        
    raw_ai_prob = burst_score + cliche_score + starter_penalty
    
    # 4. Diskon data empiris lokal (Human Anchor Discount)
    anchor_hits = [a for a in EMPIRICAL_ANCHORS if a in para_lower]
    anchor_discount = min(len(anchor_hits) * 6.0, 30.0)
    
    final_ai_prob = max(0.0, min(100.0, raw_ai_prob - anchor_discount))
    
    if final_ai_prob >= 50.0:
        status = "AI_FLAGGED"
    elif final_ai_prob >= 35.0:
        status = "WARNING"
    else:
        status = "HUMAN_AUTHENTIC"
        
    return {
        "text": para_text,
        "word_count": word_count,
        "sent_count": len(sentences),
        "cv": cv,
        "cliches": cliche_hits,
        "anchors": anchor_hits,
        "ai_prob": final_ai_prob,
        "status": status
    }

def analyze_chapter(fpath):
    if not os.path.exists(fpath):
        return None
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
        
    raw_paras = text.split("\n\n")
    paras = []
    for p in raw_paras:
        p_clean = p.strip()
        if not p_clean:
            continue
        if p_clean.startswith("#") or p_clean.startswith("|") or p_clean.startswith("!") or p_clean.startswith("*Keterangan") or p_clean.startswith(">"):
            continue
        paras.append(p_clean)
        
    total_words = 0
    flagged_words = 0
    warning_words = 0
    para_results = []
    
    for idx, p in enumerate(paras, 1):
        res = analyze_paragraph(p)
        if res:
            res["index"] = idx
            total_words += res["word_count"]
            if res["status"] == "AI_FLAGGED":
                flagged_words += res["word_count"]
            elif res["status"] == "WARNING":
                warning_words += res["word_count"]
            para_results.append(res)
            
    ai_percentage = (flagged_words / total_words * 100.0) if total_words > 0 else 0.0
    warning_percentage = ((flagged_words + warning_words) / total_words * 100.0) if total_words > 0 else 0.0
    
    return {
        "total_paras": len(para_results),
        "total_words": total_words,
        "flagged_words": flagged_words,
        "warning_words": warning_words,
        "ai_percentage": ai_percentage,
        "warning_percentage": warning_percentage,
        "paragraphs": para_results
    }

def run_audit():
    print("==================================================================")
    print("  SIMULASI AUDIT AI WRITING TUGAS AKHIR ITK (TURNITIN-LIKE CHECK)")
    print("==================================================================\n")
    
    total_doc_words = 0
    total_doc_flagged = 0
    
    for name, path in TARGET_FILES.items():
        data = analyze_chapter(path)
        if not data:
            print(f"{name}: Berkas tidak ditemukan pada {path}")
            continue
            
        total_doc_words += data["total_words"]
        total_doc_flagged += data["flagged_words"]
        
        status_str = "AMAN (LOLOS < 25%)" if data["ai_percentage"] < 25.0 else "BAHAYA (MELEBIHI 25%)"
        print(f"[{name}]")
        print(f"  - Total Kata Naratif        : {data['total_words']:,} kata")
        print(f"  - Kata Terindikasi AI       : {data['flagged_words']:,} kata")
        print(f"  - ESTIMASI SKOR AI WRITING  : {data['ai_percentage']:.1f}%")
        print(f"  - Status Ambang Batas 25%   : {status_str}")
        print(f"  - Potensi Zona Kuning/Waspada : {data['warning_percentage']:.1f}%")
        
        flagged = [p for p in data["paragraphs"] if p["status"] == "AI_FLAGGED"]
        print(f"  - Jumlah Paragraf Terflag   : {len(flagged)} dari {data['total_paras']} paragraf")
        
        if flagged:
            print("  - Rincian Paragraf Berisiko Tinggi:")
            for f in flagged:
                print(f"    * Paragraf ke-{f['index']} (Prob: {f['ai_prob']:.0f}%, {f['word_count']} kata):")
                preview = f['text'][:120].replace('\n', ' ')
                print(f"      Teks: \"{preview}...\"")
                if f['cliches']:
                    print(f"      Pemicu Klise AI: {f['cliches']}")
                print(f"      Variasi Ritme (CV): {f['cv']:.2f}")
        print("-" * 66)
        
    overall_pct = (total_doc_flagged / total_doc_words * 100.0) if total_doc_words > 0 else 0.0
    overall_status = "LOLOS (DI BAWAH 25%)" if overall_pct < 25.0 else "PERLU REVISI (DI ATAS 25%)"
    print("\n==================================================================")
    print(f"  TOTAL KUMULATIF SELURUH PROPOSAL (BAB 1 + BAB 2 + BAB 3)")
    print(f"  - Total Kata Seluruh Dokumen : {total_doc_words:,} kata")
    print(f"  - Total Kata Terindikasi AI  : {total_doc_flagged:,} kata")
    print(f"  - ESTIMASI SKOR AKHIR AI     : {overall_pct:.1f}%")
    print(f"  - STATUS AKHIR KELAYAKAN     : {overall_status}")
    print("==================================================================")

if __name__ == "__main__":
    run_audit()

