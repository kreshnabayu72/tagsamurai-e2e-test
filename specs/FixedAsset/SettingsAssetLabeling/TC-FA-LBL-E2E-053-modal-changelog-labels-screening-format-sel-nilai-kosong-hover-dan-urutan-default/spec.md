---
id: TC-FA-LBL-E2E-053-modal-changelog-labels-screening-format-sel-nilai-kosong-hover-dan-urutan-default
title: "Modal Changelog: Labels: screening, format sel, nilai kosong, hover, penutupan keyboard, dan urutan default"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-03/screening
  - FALB:obl/T-ALB-03/cell-format
  - FALB:obl/T-ALB-03/keyboard
  - FALB:obl/T-ALB-03/sort-default
  - FALB:obl/T-ALB-03/empty-value/FLD-15
  - FALB:obl/T-ALB-03/empty-value/FLD-16
  - FALB:obl/T-ALB-03/hover/FLD-17
  - FALB:global-table-rules/changelog
  - FALB:defaults-ordering-spec/default-sort-modal-changelog
  - FALB:defaults-ordering-spec/tampilan-nilai-kosong
coverage:
  web: automated
---

# Modal Changelog: Labels: screening, format sel, nilai kosong, hover, penutupan keyboard, dan urutan default

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Pelaku kedua seeding lewat sesi API: Total Control kedua (`DU-31`), env `FA_TC2_EMAIL` dan `FA_TC2_PASSWORD`.
- Data uji `DU-62` (Dataset Changelog: Labels), bersuffix `{runId}-053`, label `Log-{runId}-053-nn`, dibuat lewat sesi API di hook `before` dengan urutan tulis: (a) Create label `-04` sampai `-09` oleh `DU-01`; (b) Create `-01` oleh `DU-01`, Edit Label Name `-01` menjadi `-01-baru` oleh `DU-31`, Edit Color `-01` dari `#3B82F6` ke `#EF4444` oleh `DU-31`, Create `-02` oleh `DU-31`, Create `-03` oleh `DU-01`, lalu Delete `-03` oleh `DU-01` (entri yang ditulis terakhir). Total 12 entri; enam entri bagian (b) menjadi entri terbaru sehingga tampil di halaman pertama. Hook `after` menghapus label `-01-baru`, `-02`, dan `-04` sampai `-09` lewat sesi API.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label dan membaca entri Changelog, disediakan tim FE/BE. Format tanggal mengikuti Global Settings > General Settings akun `DU-01`.
- State global: tidak ada yang diubah; spec hanya membaca Modal Changelog. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB:obl/T-ALB-03/screening: Screening kolom default Modal Changelog: Labels

1. Klik ikon Changelog pada toolbar tabel
2. Verifikasi Modal Changelog: Labels tampil dengan judul `Changelog: Labels`
3. Verifikasi header kolom tampil berurutan Date, Action, Label Name, Field, Old Value, New Value, Modified By
4. Klik ikon Search pada toolbar Modal Changelog
5. Verifikasi input Search Modal Changelog memiliki placeholder `Search label name, action...`
6. Ketik Search `DU-62`, tekan Enter
7. Verifikasi baris entri milik `DU-62` tampil pada tabel Modal Changelog

### FALB:obl/T-ALB-03/cell-format: Format sel dan nilai tampilan tiap kolom

8. Verifikasi sel Date tiap baris tampil dalam format tanggal dan jam sesuai Date Format dan Time Format General Settings akun `DU-01`
9. Verifikasi sel Action tiap baris berisi salah satu dari `Create`, `Edit`, atau `Delete`
10. Verifikasi sel Field tiap baris berisi `Label Name` atau `Color`
11. Verifikasi sel Modified By tiap baris berformat `[First Name] [Last Initial]` dari nama lengkap `DU-01` atau `DU-31`, bukan nama lengkap

### FALB:obl/T-ALB-03/sort-default: Urutan default saat Modal Changelog pertama dimuat

12. Verifikasi header kolom Date menampilkan indikator sort aktif Newest First sedangkan header kolom lain netral
13. Verifikasi baris pertama tabel adalah entri Delete label `-03` milik `DU-62`

### FALB:defaults-ordering-spec/default-sort-modal-changelog: Default sort Modal Changelog kolom Date Newest First

14. Verifikasi nilai Date baris pertama sampai baris kesepuluh pada halaman pertama tidak bertambah dari atas ke bawah (terbaru di atas)

### FALB:obl/T-ALB-03/empty-value/FLD-15: Nilai kosong kolom Old Value tampil `—`

15. Verifikasi baris Create label `-02` milik `DU-62` menampilkan Old Value `—`

### FALB:obl/T-ALB-03/empty-value/FLD-16: Nilai kosong kolom New Value tampil `—`

16. Verifikasi baris Delete label `-03` milik `DU-62` menampilkan New Value `—`

### FALB:defaults-ordering-spec/tampilan-nilai-kosong: Tampilan nilai kosong mengikuti kolom Nilai Kosong Tabel 3

17. Verifikasi baris Create label `-02` milik `DU-62` menampilkan nilai pada kolom Date, Action, Label Name, Field, dan Modified By, tanpa `—`
18. Verifikasi baris Edit Color label `-01` milik `DU-62` menampilkan Old Value `#3B82F6` dan New Value `#EF4444`, tanpa `—`

### FALB:obl/T-ALB-03/hover/FLD-17: Hover kolom Modified By menampilkan nama lengkap

19. Arahkan kursor ke sel Modified By baris Create label `-01` milik `DU-62`
20. Verifikasi tooltip menampilkan nama lengkap akun `DU-01`

### FALB:global-table-rules/changelog: Modal Changelog menampilkan riwayat modifikasi nama dan warna label

21. Verifikasi baris Edit dengan Field `Label Name`, Old Value `Log-{runId}-053-01`, dan New Value `Log-{runId}-053-01-baru` milik `DU-62` tampil
22. Verifikasi baris Edit dengan Field `Color`, Old Value `#3B82F6`, dan New Value `#EF4444` milik `DU-62` tampil

### FALB:obl/T-ALB-03/keyboard: Penutupan Modal Changelog lewat `[✕]` dan Esc

23. Klik area gelap di luar Modal Changelog
24. Verifikasi Modal Changelog: Labels tetap tampil
25. Klik `[✕]` pada header Modal Changelog
26. Verifikasi ikon Changelog tampil pada toolbar tabel Labels List
27. Verifikasi Modal Changelog: Labels tidak tampil
28. Klik ikon Changelog pada toolbar tabel
29. Verifikasi Modal Changelog: Labels tampil dengan judul `Changelog: Labels`
30. Tekan Esc
31. Verifikasi ikon Changelog tampil pada toolbar tabel Labels List
32. Verifikasi Modal Changelog: Labels tidak tampil

## Notes

- Langkah penghubung (S-03): langkah 1 membuka modal; langkah 4 membuka input Search (screening placeholder) dan langkah 6 mempersempit tabel ke entri `DU-62` (R-16, Search sebagai langkah penghubung, bukan objek klausa); langkah 19 hanya menggerakkan kursor; langkah 23 menguji klik di luar modal; langkah 28 membuka ulang modal sebelum Esc.
- Anchor positif (bagian 8b butir 2): langkah 7 membuktikan entri `DU-62` sudah termuat sebelum asersi baris dan nilai kosong; langkah 26 dan 31 (ikon Changelog tampil pada Labels List) menjadi anchor untuk asersi modal tidak tampil di langkah 27 dan 32, dan langkah 24 membuktikan modal masih tampil sesudah klik di luar.
- Urutan default (langkah 12 sampai 14): entri `DU-62` bagian (b) adalah entri terbaru di Changelog dan suite berjalan serial, sehingga entri Delete yang ditulis terakhir tampil di baris pertama (prinsip tabel log: entri yang ditulis lebih akhir tampil lebih atas pada Newest First).
- Kolom Hidden: Tabel 3 PRD §4.1.2 tidak memuat kolom Hidden atau Curated; klausa "kolom Hidden tidak tampil" pada `FALB:obl/T-ALB-03/screening` dipenuhi oleh header tujuh kolom default (langkah 3), dan pengaruh Setup Column diasersi di spec 054.
- Pembagian klausa lintas spec: `FALB:defaults-ordering-spec/tampilan-nilai-kosong` dikutip spec 041 dan spec ini; spec ini mengasersi bagian Modal Changelog (§4.1.2), spec 041 mengasersi bagian Tagged Asset List (§4.1.1).
- Temuan PRD: `FALB:obl/T-ALB-03/keyboard` menyatakan fokus kembali ke pemicu, tetapi PRD hanya menyatakan Modal Changelog ditutup lewat `[✕]` dan Esc (klik backdrop tidak menutup) dan tidak menyatakan elemen yang menerima fokus; fokus kembali ke pemicu tidak diasersi dan menunggu klausa fokus di PRD.
- Temuan PRD: PRD tidak menyatakan Date Format dan Time Format default akun uji; langkah 8 mengasersi kesesuaian dengan General Settings akun `DU-01`, bukan format literal.
