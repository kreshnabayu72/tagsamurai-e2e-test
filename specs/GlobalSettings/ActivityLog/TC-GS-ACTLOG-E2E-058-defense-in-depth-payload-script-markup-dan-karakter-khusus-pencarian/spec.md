---
id: TC-GS-ACTLOG-E2E-058-defense-in-depth-payload-script-markup-dan-karakter-khusus-pencarian
title: "Defense-in-Depth: Payload Script, Markup, dan Karakter Khusus Pencarian"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-218
  - TC-GS-ACTLOG-219
  - TC-GS-ACTLOG-220
coverage:
  web: automated
---

# Defense-in-Depth: Payload Script, Markup, dan Karakter Khusus Pencarian

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Total Control Client A dan halaman Global Settings > Brand (kemampuan disediakan tim FE/BE).
- Data Pre-setup: log Session dan User Action Client A sudah berisi baris (hasil login akun aktor dan aksi modul lain) dan tidak ada nilai yang memuat karakter `.*`. Log tidak dapat dihapus, jadi asersi absence pada `<script>alert(1)</script>` tidak dijamin oleh spec (lihat Temuan untuk QA). Pre-setup ini dibaca, tidak diubah.
- Data Dinamis: Brand `<img src=x onerror=alert(1)> {runId}-058` dibuat lewat UI pada TC-GS-ACTLOG-219 dan dihapus lewat API di hook `after`. Payload literal `<img src=x onerror=alert(1)>` dipertahankan utuh karena payload itu objek uji; suffix run ditaruh setelah payload supaya nama Brand unik per run.
- Kemampuan teknis: mendeteksi dialog JavaScript (`alert`) yang terpicu di halaman, dan memeriksa bahwa sebuah sel tabel tidak berisi elemen `img` yang dirender.
- Spec hanya menambah baris log. Suite serial (`parallel: false`) mengikuti `suite.md`.

## Test Steps

### TC-GS-ACTLOG-218: Payload script di kotak Search diperlakukan sebagai teks

1. Buka Global Settings > Activity Log > Session
2. Verifikasi tabel Tab Session menampilkan baris
3. Ketik Search `<script>alert(1)</script>`, tekan Enter
4. Verifikasi tidak ada script yang berjalan (tidak ada dialog `alert` yang terpicu)
5. Verifikasi tabel Tab Session menampilkan `"No results found"`
6. Klik tab "User Action"
7. Verifikasi tabel Tab User Action menampilkan baris
8. Ketik Search `<script>alert(1)</script>`, tekan Enter
9. Verifikasi tidak ada script yang berjalan (tidak ada dialog `alert` yang terpicu)
10. Verifikasi tabel Tab User Action menampilkan `"No results found"`

### Pemulihan state antar TC

11. Klik `(←)` pada kotak Search Tab User Action
12. Klik tab "Session", lalu klik `(←)` pada kotak Search Tab Session

### TC-GS-ACTLOG-220: Karakter khusus pola pencarian diperlakukan sebagai teks biasa

13. Verifikasi tabel Tab Session menampilkan baris
14. Ketik Search `.*`, tekan Enter
15. Verifikasi tabel Tab Session menampilkan `"No results found"` (tidak seluruh baris cocok)
16. Klik tab "User Action"
17. Verifikasi tabel Tab User Action menampilkan baris
18. Ketik Search `.*`, tekan Enter
19. Verifikasi tabel Tab User Action menampilkan `"No results found"` (tidak seluruh baris cocok)

### Pemulihan state antar TC

20. Klik `(←)` pada kotak Search Tab User Action
21. Klik tab "Session", lalu klik `(←)` pada kotak Search Tab Session

### TC-GS-ACTLOG-219: Nilai log berisi markup ditampilkan sebagai teks di Tab User Action

22. Buka Global Settings > Brand, buat Brand `<img src=x onerror=alert(1)> {runId}-058`
23. Tunggu aksi selesai (form tertutup dan tombol aktif kembali)
24. Buka Global Settings > Activity Log > User Action
25. Ketik Search `{runId}-058`, tekan Enter
26. Verifikasi entri `Create` Brand `<img src=x onerror=alert(1)> {runId}-058` tampil
27. Verifikasi kolom Name menampilkan teks `<img src=x onerror=alert(1)> {runId}-058` apa adanya
28. Verifikasi kolom New Value menampilkan teks `<img src=x onerror=alert(1)> {runId}-058` apa adanya
29. Verifikasi tidak ada gambar yang dirender pada kolom Name dan New Value
30. Verifikasi tidak ada script yang berjalan (tidak ada dialog `alert` yang terpicu)

### Pemulihan state akhir spec

31. Klik `(←)` pada kotak Search

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC-GS-ACTLOG-218, 220, lalu 219 (bukan urutan angka TC): TC-GS-ACTLOG-219 membuat data (Brand) sehingga ditaruh paling akhir, setelah dua TC pencarian yang tidak membuat data (S-10).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 11, 12, 20, 21, dan 31 (membersihkan Search lewat `(←)`); langkah 23 (menunggu pembuatan Brand selesai, 8b butir 8); langkah 25 (mencari entri lewat suffix run karena TC hanya menyebut "cari entri tersebut"). Subjudul "Pemulihan state" bukan TC sumber.
- Langkah 2, 7, 13, dan 17 adalah `Verifikasi` data pembanding (tabel menampilkan baris sebelum pencarian) sebagai anchor positif untuk asersi `"No results found"` (8b butir 2, S-03); TC hanya menyebut precondition "data log tersedia".
- Baseline TC-GS-ACTLOG-219 adalah nol karena nama Brand bersuffix unik per run (S-12).
- Spec memuat tiga TC berkelas defense-in-depth (kelas a) dengan harness yang sama (payload di UI tanpa harness eksternal); tidak ada kelas harness lain.
- Pembagian TC lintas spec: TC-GS-ACTLOG-215, 216, dan 217 (request langsung ke endpoint) ada di spec 057.
- Temuan untuk QA:
  - TC-GS-ACTLOG-219 menyebut nama Brand `<img src=x onerror=alert(1)>` literal; spec menambahkan suffix run setelah payload agar nama Brand unik per run. Validasi karakter `<` dan `>` pada field Name Brand tidak dijelaskan di TC; bila Brand menolak karakter itu, TC tidak dapat dijalankan.
  - Temuan sumber (pemilik TC): payload `<script>alert(1)</script>` pada TC-GS-ACTLOG-218 sama dengan payload yang dibuat suite lain (Division spec 073, User spec 155) pada log Client A yang bersama dan append-only, sehingga asersi `"No results found"` hanya valid bila tidak ada baris lain bermuatan sama. Spec tetap memakai payload persis seperti TC; payload perlu penanda unik per run, atau TC perlu precondition entitas log terisolasi.
  - Cara mengamati "tidak ada script yang berjalan" tidak dijelaskan di TC; spec memakai deteksi dialog `alert` sebagai kemampuan teknis.
