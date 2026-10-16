<!-- antislop:start -->
## antislop
For UI, copy, people, mobile layout, or code comments work, read `antislop.md` (core) and then the skill for the task:
- UI / visual: `.agents/skills/antislop-ui/SKILL.md`
- Copy & text: `.agents/skills/antislop-copywriting/SKILL.md`
- People: `.agents/skills/antislop-human/SKILL.md`
- Mobile / responsive: `.agents/skills/antislop-layoutmobile/SKILL.md`
- Code comments: `.agents/skills/antislop-code/SKILL.md`
Before starting, follow the core's "Two Usage Modes" section in strict order: explicit session instruction first, then global preference, then ask. A session instruction always wins. For a resolved mode, say `antislop active: <mode> (session override).` or `antislop active: <mode> (global preference).` once before presenting findings or making edits, using the actual mode and source. Acknowledging the user's request without naming the source does not replace this notice.
Only an explicit choice of antislop during or after selects a session mode. A request to review, audit, or avoid file edits does not select a mode; read the global preference in that case. Another skill's mode does not select antislop's mode.
If the mode is unresolved, ask during/after and end the response; wait for the answer before any UI review, planning, or concept. For read-only tasks, put the active-mode notice only at the start of the final answer, never in progress messages. For editing tasks, announce before the first edit and omit it from the final answer.
To update antislop later: download `antislop.md` again, or run `npx antislop-ai --update` if it was installed as skill folders.
<!-- antislop:end -->

## Aturan Penulisan Akademik Tugas Akhir / Skripsi ITK
1. **Larangan Dash Panjang (Em-dash)**: Dilarang keras menggunakan tanda dash panjang (`—`, `–`, atau `--`) dalam naskah skripsi / laporan. Selalu gunakan kata penghubung formal yang relevan (seperti: `yaitu`, `yakni`, `seperti`, `sehingga`, `guna`, `untuk`) atau tanda baca koma (`,`) / titik dua (`:`).
2. **Kaidah Paragraf**: Dilarang membuat paragraf yang hanya terdiri dari satu kalimat. Setiap paragraf wajib memiliki kalimat utama dan kalimat penjelas (minimal 2–3 kalimat).
3. **Angka Awal Kalimat**: Dilarang mengawali kalimat dengan angka numerik (misal: "8 cabang..."). Wajib dieja dengan huruf ("Delapan cabang...").
4. **Anti-AI & Orisinalitas**: Hindari frasa klise AI, pertahankan ritme kalimat bervariasi (burstiness alami), dan lakukan parafrase orisinal berlandaskan data empiris riil.
5. **Gaya Sitasi**: Mengikuti kaidah Author-Year sesuai Panduan Tugas Akhir Sistem Informasi ITK 2026.
