# coding: utf-8
"""
Pendeteksi AI Writing Berkas PDF (Open-Source Pipeline Python)
Khusus Naskah Tugas Akhir Akademik Bahasa Indonesia (Format ITK)
Menggunakan PyMuPDF (fitz) dan Analisis Statistik Linguistik Indo-NLP
"""

import os
import sys
import re
import statistics
import fitz  # PyMuPDF

# Daftar frasa klise AI Bahasa Indonesia
AI_CLICHES = [
    "merupakan salah satu", "memegang peranan penting", "peran penting dalam",
    "dalam era digital", "era globalisasi", "tidak dapat dipungkiri",
    "oleh karena itu", "selain itu", "hal ini menunjukkan bahwa",
    "hal ini membuktikan bahwa", "dapat disimpulkan bahwa", "secara keseluruhan",
    "penting untuk dicatat", "memberikan kontribusi", "efektif dan efisien",
    "efisien dan efektif", "seiring dengan perkembangan", "dalam hal ini",
    "tidak hanya", "tetapi juga", "diharapkan dapat memberikan",
    "sangat krusial untuk", "memainkan peran", "dalam rangka untuk"
]

# Kata kunci empiris lokal penurun skor AI (Human Anchors)
EMPIRICAL_ANCHORS = [
    "artha", "balikpapan", "cabang", "delapan", "buku besar", "kuitansi",
    "folio", "kasir", "wita", "tentor", "spp", "rupiah", "laci", "memo",
    "peter chen", "bizagi", "sanctum", "next.js", "laravel", "mysql",
    "dzhurov", "sommerville", "laudon", "tuition_bills", "daily_reconciliations",
    "rombongan belajar", "rombel", "siswa", "orang tua", "jadwal"
]

def analyze_paragraph(para_text):
    words = para_text.split()
    word_count = len(words)
    if word_count < 15:
        return None
    
    # Abaikan baris heading atau tabel murni
    if para_text.strip().startswith("#") or para_text.strip().startswith("|"):
        return None
        
    sentences = [s.strip() for s in re.split(r"[.!?]+", para_text) if len(s.strip().split()) > 3]
    if len(sentences) < 2:
        cv = 0.12
    else:
        sent_lengths = [len(s.split()) for s in sentences]
        avg_len = statistics.mean(sent_lengths)
        std_len = statistics.stdev(sent_lengths) if len(sent_lengths) > 1 else 0
        cv = std_len / avg_len if avg_len > 0 else 0
        
    para_lower = para_text.lower()
    
    # 1. Burstiness (Variasi Panjang Kalimat) - bobot 40%
    if cv < 0.20:
        burst_score = 40.0
    elif cv < 0.30:
        burst_score = 28.0
    elif cv < 0.40:
        burst_score = 14.0
    else:
        burst_score = 0.0
        
    # 2. Frasa Klise AI Bahasa Indonesia - bobot 35%
    cliche_hits = [c for c in AI_CLICHES if c in para_lower]
    cliche_score = min(len(cliche_hits) * 15.0, 35.0)
    
    # 3. Prediktabilitas Struktur Kalimat - bobot 25%
    starters = [s.split()[0].lower() for s in sentences if len(s.split()) > 0]
    unique_starters = len(set(starters))
    if len(starters) > 2 and (unique_starters / len(starters)) < 0.7:
        starter_penalty = 20.0
    else:
        starter_penalty = 5.0
        
    raw_score = burst_score + cliche_score + starter_penalty
    
    # 4. Diskon Fakta Empiris Riil
    anchor_hits = [a for a in EMPIRICAL_ANCHORS if a in para_lower]
    anchor_discount = min(len(anchor_hits) * 6.0, 30.0)
    
    final_prob = max(0.0, min(100.0, raw_score - anchor_discount))
    
    return {
        "text": para_text,
        "word_count": word_count,
        "cv": cv,
        "cliches": cliche_hits,
        "anchors": anchor_hits,
        "ai_prob": final_prob,
        "is_ai": final_prob >= 50.0
    }

def scan_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"Galat: Berkas PDF tidak ditemukan pada {pdf_path}")
        return
        
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    print("=" * 68)
    print(f"  PEMINDAIAN AI WRITING DOKUMEN PDF (STANDAR INDO-NLP / ITK)")
    print("=" * 68)
    print(f"Berkas Target : {os.path.basename(pdf_path)}")
    print(f"Total Halaman : {total_pages} halaman\n")
    
    total_doc_words = 0
    total_ai_words = 0
    flagged_pages = []
    
    for page_idx in range(total_pages):
        page = doc[page_idx]
        page_num = page_idx + 1
        text = page.get_text()
        
        # Abaikan halaman daftar pustaka dan lampiran di akhir
        if "DAFTAR PUSTAKA" in text.upper() and page_num > 120:
            continue
        if "LAMPIRAN" in text.upper() and page_num > 130:
            continue
            
        # Pisahkan blok paragraf
        raw_paras = [p.strip() for p in text.split("\n\n") if p.strip()]
        page_words = 0
        page_ai_words = 0
        
        for p in raw_paras:
            # Hindari nomor halaman terisolasi atau header pendek
            if len(p.split()) < 15:
                continue
            res = analyze_paragraph(p)
            if res:
                page_words += res["word_count"]
                if res["is_ai"]:
                    page_ai_words += res["word_count"]
                    flagged_pages.append({
                        "page": page_num,
                        "prob": res["ai_prob"],
                        "words": res["word_count"],
                        "cliches": res["cliches"],
                        "preview": res["text"][:100].replace("\n", " ")
                    })
                    
        total_doc_words += page_words
        total_ai_words += page_ai_words
        
    doc_ai_pct = (total_ai_words / total_doc_words * 100.0) if total_doc_words > 0 else 0.0
    status = "LOLOS (DI BAWAH 25%)" if doc_ai_pct < 25.0 else "PERLU REVISI (DI ATAS 25%)"
    
    print("-" * 68)
    print(f"RINGKASAN HASIL PEMINDAIAN PDF LENGKAP:")
    print(f"  - Total Kata Dianalisis  : {total_doc_words:,} kata")
    print(f"  - Kata Terindikasi AI    : {total_ai_words:,} kata")
    print(f"  - PERSENTASE AI WRITING  : {doc_ai_pct:.2f}%")
    print(f"  - STATUS KELAYAKAN ITK   : {status}")
    print("-" * 68)
    
    if flagged_pages:
        print(f"\nDaftar Halaman dengan Indikasi Paragraf AI ({len(flagged_pages)} temuan):")
        for item in flagged_pages[:5]:
            print(f"  * Halaman {item['page']} (Probabilitas: {item['prob']:.0f}%, {item['words']} kata)")
            print(f"    Teks: \"{item['preview']}...\"")
            if item['cliches']:
                print(f"    Pemicu Klise: {item['cliches']}")
    else:
        print("\nTidak ditemukan halaman dengan paragraf yang melewati batas kritis AI Writing!")
    print("=" * 68)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DOCS SKRIPSI\PROTOTIPE.pdf"
    scan_pdf(target)

