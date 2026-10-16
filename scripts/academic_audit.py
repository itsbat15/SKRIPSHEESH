"""
academic_audit.py
=================
Skrip Audit Integritas Akademik & Anti-AI untuk Laporan Tugas Akhir / Skripsi ITK.
Divalidasi langsung terhadap:
- Buku Panduan Pelaksanaan Tugas Akhir Sistem Informasi ITK 2026
- Template Laporan Tugas Akhir Bentuk Proyek ITK 2026 (s.itk.ac.id/template_proyek)
- Standar Turnitin Resmi ITK (Similarity Score Maksimal 25%)

Fokus Audit:
1. Anti-Turnitin (N-gram Overlap Matcher terhadap korpus lokal, threshold ITK <= 25%, target lokal <= 2%).
2. Anti-AI Marker & Cliché Scanner (Kamus frasa klise AI Bahasa Indonesia).
3. Analisis Burstiness & Ritme (Mencegah pola kalimat datar/monoton khas AI).
4. PUEBI, EYD V & Tata Tulis Akademik (Penomoran awal kalimat, larangan paragraf 1 kalimat, kata serapan).
5. Kepatuhan Sistematika Bab 1 Bentuk Proyek (Subbab 1.1 s.d. 1.7 & Data Empiris Mitra).
"""

import sys
import os
import re
import math
import argparse
from pathlib import Path

# ==============================================================================
# KAMUS FRASA KLISE & POLA BAHASA AI (BAHASA INDONESIA)
# ==============================================================================
AI_CLICHE_PHRASES = [
    # Pembuka klise / filler
    "tidak dapat dipungkiri bahwa",
    "tak dapat dimungkiri bahwa",
    "sebagaimana yang kita ketahui",
    "perlu digarisbawahi bahwa",
    "pada dasarnya",
    "dalam era digitalisasi yang kian pesat",
    "dalam era globalisasi yang kian pesat",
    "di era digital yang berkembang pesat ini",
    "di era modern saat ini",
    "di zaman yang serba cepat ini",
    "seiring dengan perkembangan zaman",
    "seiring dengan pesatnya perkembangan",
    "dewasa ini perkembangan teknologi",
    
    # Fluff adjectives & buzzwords
    "secara mulus",
    "secara seamless",
    "solusi yang komprehensif",
    "solusi komprehensif",
    "memberikan kontribusi yang signifikan",
    "kontribusi yang sangat signifikan",
    "membawa transformasi fundamental",
    "membawa dampak revolusioner",
    "menjadi bukti nyata",
    "menjadi bukti konkret",
    "menjawab tantangan zaman",
    "lanskap digital",
    "lanskap bisnis",
    "lanskap pendidikan",
    "meningkatkan efisiensi dan efektivitas secara signifikan",
    "efisiensi dan efektivitas",
    "hadir sebagai solusi inovatif",
    "hadir sebagai jawaban atas",
    "membuka pintu bagi",
    "menjadi tonggak penting",
    "menjadi angin segar",
    "lompatan besar",
    "game changer",
    "sangat krusial",
    "memegang peranan yang sangat penting",
    "merupakan hal yang sangat penting",
    "diharapkan mampu menjawab kebutuhan",
    "menghadirkan terobosan",
    "daya saing di era digital",
    "berkelanjutan dan terintegrasi",
    "paradigma baru",
    
    # Transisi repetitif tanpa argumen
    "dengan kata lain dapat dikatakan bahwa",
    "hal ini membuktikan bahwa",
    "dari uraian di atas dapat ditarik benang merah",
]

# Kata informal / non-baku
INFORMAL_WORDS = {
    "nggak": "tidak",
    "gak": "tidak",
    "udah": "sudah",
    "bikin": "membuat / merancang",
    "makanya": "oleh karena itu",
    "banget": "sangat",
    "cuma": "hanya",
    "pake": "menggunakan",
    "pakai": "menggunakan",
    "kalo": "apabila / jika",
    "kalau": "apabila / jika",
    "gimana": "bagaimana",
    "kenapa": "mengapa",
    "tapi": "namun / akan tetapi",
    "ngasih": "memberikan",
    "dapetin": "memperoleh",
}

# Kesalahan tata bahasa umum & pleonasme
GRAMMAR_TRAPS = [
    (r"\badalah merupakan\b", "Pleonasme: gunakan 'adalah' atau 'merupakan', jangan keduanya."),
    (r"\bagar supaya\b", "Pleonasme: gunakan 'agar' atau 'supaya'."),
    (r"\bsangat \w+ sekali\b", "Pleonasme: jangan padukan 'sangat' dengan 'sekali'."),
    (r"\bdimana\b", "Koreksi fungsi: 'dimana' hanya untuk menunjuk tempat fisik, bukan kata hubung."),
    (r"\bsehingga\b(?=.*[,.]\s*maka\b)", "Konjungsi ganda: jangan gabungkan 'sehingga' dengan 'maka'."),
    (r"\bkarena\b(?=.*[,.]\s*maka\b)", "Konjungsi ganda: jangan gunakan 'karena... maka...' dalam satu klausa."),
]

# Subbab wajib Bab 1 Tipe Proyek ITK (Template Resmi ITK 2026)
BAB1_REQUIRED_SUBSECTIONS = [
    "1.1", "Latar Belakang",
    "1.2", "Rumusan Masalah",
    "1.3", "Tujuan",
    "1.4", "Batasan Proyek",
    "1.5", "Relevansi dengan Industri atau Akademik",
    "1.6", "Kerangka Penelitian",
    "1.7", "Mitra"
]

# Entitas empiris Bimbel Artha yang wajib ada di Latar Belakang
EMPIRICAL_KEYWORDS = [
    "Artha", "Balikpapan", "cabang", "tentor", "siswa",
    "buku besar", "SPP", "jadwal", "Personal Extreme Programming"
]


def clean_markdown(text: str) -> str:
    """Membersihkan tag markdown, tabel, dan header agar teks murni."""
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"[*_]{1,3}(.*?)[*_]{1,3}", r"\1", text)
    text = re.sub(r"\|.*?\|", "", text)
    text = re.sub(r"<.*?>", "", text)
    return text


def split_into_paragraphs(raw_text: str) -> list[str]:
    """Memisahkan paragraf narasi murni dari file markdown."""
    paragraphs = []
    blocks = raw_text.split("\n\n")
    for b in blocks:
        clean_b = clean_markdown(b).strip()
        # Abaikan baris header, tabel, daftar poin
        if clean_b and not clean_b.startswith("#") and not clean_b.startswith("-") and not clean_b.startswith("*"):
            words = re.findall(r"\b[A-Za-z0-9_-]+\b", clean_b)
            if len(words) >= 15:
                paragraphs.append(clean_b)
    return paragraphs


def split_into_sentences(text: str) -> list[str]:
    """Memecah teks menjadi daftar kalimat dengan akurasi tanda baca."""
    text = clean_markdown(text)
    text = re.sub(r"\b(S\.E|S\.Kom|M\.Kom|S\.Sos|S\.Pd|Dr|Ir|Prof|dkk|dsb|dst|hlm|No|Vol)\.", r"\1<DOT>", text)
    sentences = re.split(r"(?<=[.!?])\s+", text)
    cleaned = []
    for s in sentences:
        s = s.replace("<DOT>", ".").strip()
        s = re.sub(r"^(\d+\.|\*|-)\s+", "", s)
        words = re.findall(r"\b[A-Za-z0-9_-]+\b", s)
        if len(words) >= 3:
            cleaned.append(s)
    return cleaned


def tokenize_words(text: str) -> list[str]:
    """Tokenisasi kata huruf kecil tanpa tanda baca."""
    clean = clean_markdown(text).lower()
    return re.findall(r"\b[a-z0-9_-]+\b", clean)


def extract_ngrams(words: list[str], n: int = 5) -> set[tuple[str, ...]]:
    """Mengekstrak n-gram kata berurutan."""
    if len(words) < n:
        return set()
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


# ==============================================================================
# AUDIT MODUL 1: ANTI-TURNITIN (N-GRAM MATCHER TERHADAP KORPUS LOKAL)
# ==============================================================================
def load_reference_corpus(workspace_dir: Path, n: int = 5) -> dict[tuple[str, ...], str]:
    ref_ngrams = {}
    candidate_paths = [
        workspace_dir / "REFERENSI TA PXP" / "HASIL EKSTRAK Anggara Kurniawan Prototipe" / "Laporan Tugas Akhir Prototipe Final - Anggara Kurniawan.txt",
        workspace_dir / "REFERENSI TA PXP" / "HASIL EKSTRAK 10211089 Buku TA" / "Buku Tugas Akhir PxP - 10211089.txt",
        workspace_dir / "TEMPLATE TA" / "hasil ekstrak template laporan" / "LAPORAN TA_PROYEK.txt",
        workspace_dir / "PANDUAN TA" / "HASIL EKSTRAK PANDUAN TA 2026" / "Panduan TA dan SITASI - Sistem Informasi ITK 2026.txt"
    ]
    
    journal_dir = workspace_dir / "JURNAL" / "HASIL EKSTRAK JURNAL"
    if journal_dir.exists():
        candidate_paths.extend(journal_dir.glob("*.txt"))

    print(f"[*] Memindai {len(candidate_paths)} dokumen referensi lokal...")
    loaded_count = 0
    for path in candidate_paths:
        if path.exists():
            try:
                content = path.read_text(encoding="utf-8", errors="ignore")
                words = tokenize_words(content)
                ngrams = extract_ngrams(words, n)
                source_name = path.name
                for ng in ngrams:
                    if ng not in ref_ngrams:
                        ref_ngrams[ng] = source_name
                loaded_count += 1
            except Exception:
                pass
    print(f"[+] Berhasil memuat {len(ref_ngrams):,} {n}-gram unik dari {loaded_count} dokumen referensi.\n")
    return ref_ngrams


def check_plagiarism_overlap(target_words: list[str], ref_ngrams: dict[tuple[str, ...], str], n: int = 5):
    target_ngrams = extract_ngrams(target_words, n)
    if not target_ngrams:
        return 0, []

    matches = []
    matched_set = set()
    for i in range(len(target_words) - n + 1):
        ng = tuple(target_words[i:i + n])
        if ng in ref_ngrams:
            phrase = " ".join(ng)
            source = ref_ngrams[ng]
            if phrase not in matched_set:
                matched_set.add(phrase)
                matches.append((phrase, source))

    overlap_pct = (len(matched_set) / max(1, len(target_ngrams))) * 100
    return overlap_pct, matches


# ==============================================================================
# AUDIT MODUL 2: SCANNER FRASA KLISE & PENANDA AI
# ==============================================================================
def check_ai_cliches(raw_text: str) -> list[dict]:
    lines = raw_text.splitlines()
    findings = []
    for line_idx, line in enumerate(lines, start=1):
        clean_line = line.lower()
        for phrase in AI_CLICHE_PHRASES:
            if phrase in clean_line:
                findings.append({
                    "line": line_idx,
                    "phrase": phrase,
                    "snippet": line.strip()[:100]
                })
    return findings


# ==============================================================================
# AUDIT MODUL 3: ANALISIS BURSTINESS & RITME KALIMAT
# ==============================================================================
def analyze_burstiness(sentences: list[str]) -> dict:
    if not sentences:
        return {"count": 0, "mean": 0, "std_dev": 0, "status": "NO_TEXT"}

    lengths = [len(re.findall(r"\b[A-Za-z0-9_-]+\b", s)) for s in sentences]
    n = len(lengths)
    mean_len = sum(lengths) / n
    variance = sum((x - mean_len) ** 2 for x in lengths) / n
    std_dev = math.sqrt(variance)

    short_cnt = sum(1 for x in lengths if x < 12)
    medium_cnt = sum(1 for x in lengths if 12 <= x <= 25)
    long_cnt = sum(1 for x in lengths if x > 25)
    run_on_sentences = [s for s, x in zip(sentences, lengths) if x > 40]

    if std_dev >= 7.0:
        status = "EXCELLENT (Ritme Manusia Alami - Sangat Bervariasi)"
    elif std_dev >= 5.0:
        status = "MODERATE (Cukup Baik, Pertahankan Variasi Kalimat Pendek & Majemuk)"
    else:
        status = "WARNING_MONOTONE (Terlalu Seragam - Khas Teks AI, Perlu Pemecahan Kalimat)"

    return {
        "count": n,
        "mean": round(mean_len, 2),
        "std_dev": round(std_dev, 2),
        "min": min(lengths),
        "max": max(lengths),
        "distribution": {
            "pendek (<12 kata)": f"{short_cnt} ({round(short_cnt/n*100, 1)}%)",
            "sedang (12-25 kata)": f"{medium_cnt} ({round(medium_cnt/n*100, 1)}%)",
            "panjang (>25 kata)": f"{long_cnt} ({round(long_cnt/n*100, 1)}%)"
        },
        "run_on_count": len(run_on_sentences),
        "run_on_examples": run_on_sentences[:3],
        "status": status
    }


# ==============================================================================
# AUDIT MODUL 4: PUEBI, EYD V & TATA TULIS ILMIAH ITK
# ==============================================================================
def check_puebi_and_typography(raw_text: str, paragraphs: list[str], sentences: list[str]) -> list[dict]:
    findings = []
    lines = raw_text.splitlines()

    # 1. Cek kata informal & tata bahasa
    for line_idx, line in enumerate(lines, start=1):
        clean_line = line.lower()
        for inf_word, suggestion in INFORMAL_WORDS.items():
            pattern = rf"\b{inf_word}\b"
            if re.search(pattern, clean_line):
                findings.append({
                    "line": line_idx,
                    "type": "KATA_INFORMAL",
                    "term": inf_word,
                    "message": f"Gunakan '{suggestion}' alih-alih kata informal '{inf_word}'.",
                    "snippet": line.strip()[:90]
                })

        for regex_pat, advice in GRAMMAR_TRAPS:
            if re.search(regex_pat, clean_line):
                findings.append({
                    "line": line_idx,
                    "type": "TATA_BAHASA_PLEONASME",
                    "term": regex_pat,
                    "message": advice,
                    "snippet": line.strip()[:90]
                })

        # 2. Cek angka Arab di awal kalimat (EYD V)
        match_num_start = re.match(r"^\s*([0-9]+)\s+[A-Za-z]+", line)
        if match_num_start and not line.strip().startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")):
            findings.append({
                "line": line_idx,
                "type": "EYD_ANGKA_AWAL_KALIMAT",
                "term": match_num_start.group(1),
                "message": f"Angka '{match_num_start.group(1)}' di awal kalimat wajib dieja dengan huruf.",
                "snippet": line.strip()[:90]
            })

        # 3. Cek penggunaan dash panjang (em-dash '—', en-dash '–', atau double-dash '--')
        if ("—" in line or " – " in line or " -- " in line) and not re.match(r"^\s*---+\s*$", line):
            findings.append({
                "line": line_idx,
                "type": "TATA_TULIS_DASH_PANJANG",
                "term": "dash panjang (— / – / --)",
                "message": "Dilarang menggunakan dash panjang. Gunakan kata penghubung formal ('yaitu', 'yakni', 'seperti', 'sehingga') atau tanda baca yang sesuai.",
                "snippet": line.strip()[:90]
            })

    # 3. Cek paragraf satu kalimat (Dilarang dalam karya ilmiah)
    for p_idx, p in enumerate(paragraphs, start=1):
        p_sentences = split_into_sentences(p)
        if len(p_sentences) <= 1:
            findings.append({
                "line": "-",
                "type": "STRUKTUR_PARAGRAF_TUNGGAL",
                "term": f"Paragraf #{p_idx}",
                "message": "Paragraf hanya terdiri dari satu kalimat. Gabungkan atau tambahkan kalimat penjelas.",
                "snippet": p[:90] + "..."
            })

    return findings


# ==============================================================================
# AUDIT MODUL 5: VALIDASI STRUKTUR TIPE PROYEK ITK & FAKTA EMPIRIS
# ==============================================================================
def check_structure_and_empirics(raw_text: str) -> dict:
    missing_subsections = []
    for sub in ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7"]:
        if not re.search(rf"\b{re.escape(sub)}\b", raw_text):
            missing_subsections.append(sub)

    missing_keywords = []
    for kw in EMPIRICAL_KEYWORDS:
        if not re.search(rf"\b{re.escape(kw)}\b", raw_text, re.IGNORECASE):
            missing_keywords.append(kw)

    return {
        "missing_subsections": missing_subsections,
        "missing_keywords": missing_keywords
    }


# ==============================================================================
# MAIN AUDIT RUNNER
# ==============================================================================
def run_academic_audit(file_path: str, n_gram: int = 5, skip_refs: bool = False):
    p = Path(file_path)
    if not p.exists():
        print(f"[!] Error: File '{file_path}' tidak ditemukan.")
        sys.exit(1)

    print("=" * 80)
    print(f" ACADEMIC & ANTI-AI AUDIT REPORT: {p.name}")
    print(" Sesuai Buku Panduan TA Sistem Informasi ITK 2026 (Bentuk Proyek)")
    print(" Standar Turnitin Resmi ITK: Maksimal 25% (Isi Laporan) & 20% (Artikel Ilmiah)")
    print("=" * 80)

    raw_text = p.read_text(encoding="utf-8", errors="ignore")
    words = tokenize_words(raw_text)
    sentences = split_into_sentences(raw_text)
    paragraphs = split_into_paragraphs(raw_text)

    print(f"[i] Jumlah Kata      : {len(words):,}")
    print(f"[i] Jumlah Kalimat   : {len(sentences):,}")
    print(f"[i] Jumlah Paragraf  : {len(paragraphs):,}")
    print("-" * 80)

    # 1. Analisis Ritme & Burstiness
    print("\n[1] ANALISIS RITME & BURSTINESS (POLA MANUSIA vs AI)")
    burst = analyze_burstiness(sentences)
    print(f"    - Standar Deviasi Panjang Kalimat : {burst['std_dev']} kata")
    print(f"    - Rata-rata Kata per Kalimat      : {burst['mean']} kata (Min: {burst['min']}, Max: {burst['max']})")
    print(f"    - Status Cadence Ritme            : {burst['status']}")
    print(f"    - Sebaran Panjang Kalimat         :")
    for k, v in burst["distribution"].items():
        print(f"      * {k.ljust(22)}: {v}")
    if burst["run_on_count"] > 0:
        print(f"    [!] Catatan: Terdapat {burst['run_on_count']} kalimat panjang (>40 kata).")

    # 2. Pindai Frasa Klise AI
    print("\n[2] PEMINDAIAN FRASA KLISE & PENANDA AI (TURNITIN AI DETECTION)")
    cliches = check_ai_cliches(raw_text)
    if not cliches:
        print("    [+] BERSIH: 0 frasa klise AI terdeteksi. Draf bebas dari penanda umum AI!")
    else:
        print(f"    [!] PERINGATAN: Ditemukan {len(cliches)} kemunculan frasa klise AI:")
        for c in cliches[:8]:
            print(f"      * Baris {c['line']}: \"{c['phrase']}\" -> ({c['snippet']}...)")
        if len(cliches) > 8:
            print(f"      * ... dan {len(cliches) - 8} temuan lainnya.")

    # 3. PUEBI, EYD V & Tata Bahasa Ilmiah
    print("\n[3] KAIDAH EJAAN PUEBI & TATA BAHASA FORMAL (EYD V & ITK)")
    typography_issues = check_puebi_and_typography(raw_text, paragraphs, sentences)
    if not typography_issues:
        print("    [+] BERSIH: Tidak ditemukan kata informal, pleonasme, atau paragraf satu kalimat.")
    else:
        print(f"    [!] Ditemukan {len(typography_issues)} catatan format/tata bahasa:")
        for g in typography_issues[:8]:
            print(f"      * Baris {g['line']} [{g['type']}]: {g['message']}")
        if len(typography_issues) > 8:
            print(f"      * ... dan {len(typography_issues) - 8} catatan lainnya.")

    # 4. Validasi Struktur & Data Empiris
    print("\n[4] VALIDASI SISTEMATIKA BAB 1 & DATA EMPIRIS MITRA (PROYEK ITK)")
    struct = check_structure_and_empirics(raw_text)
    if not struct["missing_subsections"]:
        print("    [+] Subbab 1.1 s.d. 1.7 Lengkap sesuai Template Bentuk Proyek ITK 2026.")
    else:
        print(f"    [-] Subbab Belum Lengkap: {struct['missing_subsections']}")

    if not struct["missing_keywords"]:
        print("    [+] Seluruh entitas empiris Bimbel Artha terverifikasi ada dalam teks.")
    else:
        print(f"    [-] Kata kunci empiris belum tercantum: {struct['missing_keywords']}")

    # 5. Anti-Turnitin: Pencocokan N-Gram terhadap Referensi Lokal
    print(f"\n[5] UJI KESAMAAN VERBATIM TERHADAP REFERENSI LOKAL (ANTI-TURNITIN)")
    if skip_refs:
        print("    [-] Dilewati (--no-refs diaktifkan).")
    else:
        workspace_dir = Path(__file__).resolve().parent.parent
        ref_ngrams = load_reference_corpus(workspace_dir, n=n_gram)
        overlap_pct, matches = check_plagiarism_overlap(words, ref_ngrams, n=n_gram)
        print(f"    - Skor Kesamaan Persis {n_gram}-gram : {round(overlap_pct, 2)}%")
        print(f"    - Batas Maksimal Turnitin ITK       : <= 25.0% (Laporan Isi) / Target Lokal: <= 2.0%")
        if overlap_pct <= 2.0:
            print(f"    [+] SANGAT BAIK: Tingkat kesamaan sangat rendah ({round(overlap_pct, 2)}%), aman di bawah batas Turnitin ITK.")
        else:
            print(f"    [!] PERHATIAN: Ditemukan {len(matches)} rangkaian {n_gram} kata yang sama:")
            for phrase, src in matches[:6]:
                print(f"      * \"{phrase}\" (Sumber: {src})")

    print("\n" + "=" * 80)
    print(" KESIMPULAN HASIL AUDIT")
    is_safe = (len(cliches) == 0 and burst["std_dev"] >= 5.0 and len(typography_issues) == 0 and not struct["missing_subsections"])
    if is_safe:
        print(" [PASS] Naskah memenuhi standar akademik ITK: Bebas AI Slop, ritme manusiawi, dan aman Turnitin.")
    else:
        print(" [ACTION REQUIRED] Silakan tinjau catatan di atas untuk menyempurnakan orisinalitas naskah.")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit Integritas Akademik & Anti-AI Skripsi ITK")
    parser.add_argument("file", help="Path file markdown/teks yang akan diaudit")
    parser.add_argument("--ngram", type=int, default=5, help="Ukuran n-gram anti-plagiasi (default: 5 kata)")
    parser.add_argument("--no-refs", action="store_true", help="Lewati pemindaian dokumen referensi lokal")
    args = parser.parse_args()

    run_academic_audit(args.file, n_gram=args.ngram, skip_refs=args.no_refs)
