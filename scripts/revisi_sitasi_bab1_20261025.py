from pathlib import Path
import json, hashlib, re

ROOT = Path(__file__).resolve().parents[1]
AUD = ROOT / 'JURNAL/AUDIT_SITASI_BAB1_2026-10-25'
audit = json.loads((AUD / 'MATRIKS_KLAIM_DAN_HALAMAN.json').read_text(encoding='utf-8'))
src = ROOT / 'BAB 1 - PENDAHULUAN (VERSI 11 PARAGRAF).md'
original = src.read_text(encoding='utf-8')
assert hashlib.sha256(src.read_bytes()).hexdigest() == audit['snapshot_sha256']
sources = {s['id']: s for s in audit['sources']}
for s in sources.values():
    assert hashlib.sha256(Path(s['file']).read_bytes()).hexdigest() == s['sha256'], s['id']

# Ordered citation occurrences. The surrounding prose is deliberately untouched.
changes = [
('A01','(Tiana & Gunanto, 2026)','(Tiana & Gunanto, 2026, hlm. 1631 sampai 1632)'),
('A02','(Pradana, 2024)',''),
('A03','(Fajriansyah dkk., 2026)','(Fajriansyah dkk., 2026, hlm. 116, 124 sampai 125)'),
('A04','(Ahadi dkk., 2025)','(Ahadi dkk., 2025, hlm. 764 sampai 765)'),
('A05','(Hendri dkk., 2025)','(Hendri dkk., 2025, hlm. 124 sampai 125)'),
('A06+A07','(Ramadhan & Widodo, 2026; Sudirman & Tristianti, 2021)','(Ramadhan & Widodo, 2026, bagian pembahasan dan kesimpulan; Sudirman & Tristianti, 2021, hlm. 126 sampai 127)'),
('A08','(Kabisatullah & Noprisson, 2026)','(Kabisatullah & Noprisson, 2026, hlm. 93 sampai 94)'),
('A09','(Khafidhoh dkk., 2026)','(Khafidhoh dkk., 2026, hlm. 15 sampai 16)'),
('A10','Gunawan dkk. (2025)','Gunawan dkk. (2025, hlm. 424, 432)'),
('A11','Fajriansyah dkk. (2026)','Fajriansyah dkk. (2026, hlm. 116, 124 sampai 125)'),
('A12','Barizi dkk. (2023)','Barizi dkk. (2023, hlm. 332, 336 sampai 338)'),
('A13','Thiovanda (2026)','Thiovanda (2026, hlm. 1, 4 sampai 5)'),
('A14','Safitri dkk. (2026)','Safitri dkk. (2026, hlm. 2349 sampai 2350)'),
('A15','Khafidhoh dkk. (2026)','Khafidhoh dkk. (2026, hlm. 15 sampai 16, 19)'),
('A16','Kabisatullah & Noprisson (2026)','Kabisatullah & Noprisson (2026, hlm. 94 sampai 95)'),
('A17','Ahadi dkk. (2025)','Ahadi dkk. (2025, hlm. 764 sampai 765)'),
('A18','Ramadhan & Widodo (2026)','Ramadhan & Widodo (2026, bagian pembahasan dan kesimpulan)'),
('A19','(Schwaber & Sutherland, 2020)',''),
('A20','(Sommerville, 2011)',''),
('A21','(Beck & Andres, 2004)','(Beck & Andres, 2004, Bab 7, bagian Pair Programming)'),
('A22','(Agarwal & Umphress, 2008)','(Agarwal & Umphress, 2008, hlm. 85)'),
('A23','(Mishra & Alzoubi, 2023)',''),
('A24','(Sommerville, 2011)',''),
('A25','(Pressman, 2010)',''),
('A26','(Fikri & Arthawan, 2020)','(Fikri & Arthawan, 2020, hlm. 103 sampai 105)'),
('A27','(Sidiq dkk., 2025)','(Sidiq dkk., 2025, hlm. 37 sampai 38, 45)'),
]
rows = {r['id']: r for r in audit['rows']}
cursor = 0
parts, log, notes = [], [], []
for ids, old, new in changes:
    pos = original.find(old, cursor)
    assert pos >= cursor, ids
    used = ids.split('+')
    marker = ''.join('[^SIT-' + i + ']' for i in used)
    replacement = new + marker
    parts += [original[cursor:pos], replacement]
    cursor = pos + len(old)
    log.append(dict(ids=used, original=old, replacement=replacement, source_line=original[:pos].count('\n')+1))
    for rid in used:
        r = rows[rid]
        s = sources[r['source']]
        loc = '; '.join('PDF urutan ' + str(x[0]) + ', cetak ' + str(x[1]) + ', ' + x[2] for x in r['locations'])
        if rid == 'A21':
            loc = 'PDF urutan 104, Bab 7 bagian Pair Programming; nomor cetak asli tidak tersedia pada salinan digital ini'
        if rid in ('A06','A18'):
            loc = '; '.join('PDF urutan ' + str(x[0]) + ', ' + x[2] for x in r['locations']) + '; footer PDF tidak konsisten sehingga tidak dipakai sebagai nomor cetak'
        if r['status'] in ('TIDAK DIDUKUNG','BERTENTANGAN'):
            action = 'Atribusi lama ditarik. Kalimat asli dipertahankan atas permintaan pengguna, tetapi klaim ini belum sah dipertahankan sebagai pernyataan bersumber.'
        elif r['status'] == 'SEBAGIAN':
            action = 'Sitasi ini hanya mendukung bagian klaim yang dijelaskan berikut. Klaim selebihnya tetap memerlukan revisi isi atau bukti lapangan.'
        else:
            action = 'Lokator sumber ditambahkan untuk memudahkan pemeriksaan manual. Dukungan ini tidak menjadikan artikel sebagai bukti kondisi lapangan ARTHA.'
        notes.append(f"[^SIT-{rid}]: **{r['status']}**. {action} {r['finding']} Lokator: {loc}. Sumber: [{s['author']}, {s['title']}](<{Path(s['file']).as_posix()}>). Saran audit: {r['correction']}")
parts.append(original[cursor:])
body = ''.join(parts)
# Verify every original character outside citation spans, not merely semantic similarity.
reconstructed, pos = body, 0
for item in log:
    at = reconstructed.find(item['replacement'], pos)
    assert at >= pos
    reconstructed = reconstructed[:at] + item['original'] + reconstructed[at+len(item['replacement']):]
    pos = at + len(item['original'])
assert reconstructed == original
header = '''> **Draf revisi sitasi saja, 25 Oktober 2026.** Seluruh kalimat, angka, paragraf, gambar, dan susunan subbab dari berkas asal dipertahankan. Perubahan hanya terdapat pada atribusi sitasi, penambahan lokator, dan catatan verifikasi.
>
> **Belum menjadi naskah bersih siap diajukan.** Catatan SIT menandai batas dukungan sumber dan klaim yang belum dapat dibenarkan tanpa perubahan isi. Pada enam penggunaan rujukan yang tidak didukung atau bertentangan, sitasi lama ditarik dan diganti penanda catatan, bukan diganti dengan sumber lain yang tidak menyatakan klaim tersebut.

'''
footer = '\n\n## Catatan verifikasi sitasi (bukan bagian naskah akhir)\n\nNomor PDF dihitung mulai halaman pertama berkas, termasuk sampul. Nomor cetak adalah nomor yang tercantum pada halaman sumber, sehingga keduanya tidak selalu sama.\n\n' + '\n\n'.join(notes) + '\n'
dest = ROOT / 'BAB 1 - PENDAHULUAN (REVISI SITASI SAJA - BERANOTASI).md'
dest.write_text(header + body + footer, encoding='utf-8')
manifest = dict(date='2026-10-25', source=str(src), result=str(dest), source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(), result_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(), original_prose_restored_exactly=(reconstructed==original), original_unchanged=True, citation_replacements=len(log), audited_reference_uses=len(rows), removed_unsupported_attributions=6, changes=log)
(AUD / 'BUKTI_REVISI_SITASI_SAJA.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({k:v for k,v in manifest.items() if k!='changes'}, ensure_ascii=False))
