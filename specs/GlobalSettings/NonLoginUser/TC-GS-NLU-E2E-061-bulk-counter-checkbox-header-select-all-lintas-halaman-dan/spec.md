---
id: TC-GS-NLU-E2E-061-bulk-counter-checkbox-header-select-all-lintas-halaman-dan
title: "Bulk: Counter, Checkbox Header, Select All Lintas Halaman, dan Unselect"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-214
  - TC-GS-NLU-215
  - TC-GS-NLU-216
  - TC-GS-NLU-217
coverage:
  web: automated
---

# Bulk: Counter, Checkbox Header, Select All Lintas Halaman, dan Unselect

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Active, Division Operations, Represented By Ahmad Fauzi): 12 Non-Login User `Hitung 01 {runId}-061` sampai `Hitung 12 {runId}-061`. Search `{runId}-061` menyaring tepat 12 baris sehingga N = 12 (turunan seeding, bukan dibaca dari tabel; bagian 8b butir 10) dan tabel memuat lebih dari 10 baris pada page size default 10 (dua halaman). Pengganti Budi Kurniawan dan Siti Rahayu Pre-setup agar TC populasi tidak bergantung pada data bersama.
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-214: Counter Bulk Action Bar

1. Ketik Search `{runId}-061`, tekan Enter
2. Centang baris `Hitung 01 {runId}-061`
3. Verifikasi Bulk Action Bar menampilkan `1 Non-Login User selected`
4. Centang baris `Hitung 02 {runId}-061`
5. Verifikasi Bulk Action Bar menampilkan `2 Non-Login Users selected`
6. Hapus centang baris `Hitung 02 {runId}-061`
7. Verifikasi Bulk Action Bar kembali menampilkan `1 Non-Login User selected`
8. Klik icon `(X)`
9. Verifikasi seluruh seleksi dibatalkan
10. Verifikasi Bulk Action Bar tertutup

### TC-GS-NLU-215: Checkbox header memilih seluruh baris halaman aktif

11. Centang satu baris `Hitung 01 {runId}-061`
12. Verifikasi checkbox header berstatus indeterminate
13. Klik checkbox header
14. Verifikasi seluruh 10 baris halaman aktif tercentang
15. Verifikasi counter menampilkan total baris halaman: `10 Non-Login Users selected`
16. Klik checkbox header lagi
17. Verifikasi seluruh baris tidak tercentang
18. Verifikasi Bulk Action Bar hilang

### TC-GS-NLU-216: Select All lintas halaman dan Unselect All

19. Centang baris `Hitung 01 {runId}-061`
20. Klik button `Select All (12 records)`
21. Verifikasi seluruh baris lintas halaman terpilih
22. Verifikasi counter menjadi total global: `12 Non-Login Users selected`
23. Pindah ke halaman 2
24. Verifikasi baris pada halaman 2 tetap tercentang
25. Verifikasi button menjadi `Unselect All`
26. Klik button `Unselect All`
27. Verifikasi seluruh seleksi dibatalkan
28. Verifikasi Bulk Action Bar tertutup

### TC-GS-NLU-217: Uncheck satu baris saat semua terpilih

29. Kembali ke halaman 1
30. Centang baris `Hitung 01 {runId}-061` agar button Select All tampil
31. Klik button `Select All (12 records)`
32. Hapus centang satu baris
33. Verifikasi Bulk Action Bar tetap tampil dengan sisa 11 baris terpilih
34. Verifikasi button berubah menjadi `Select All (11 records)`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 29, 30.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1.
- Temuan untuk QA:
  - TC-217 Langkah Uji langsung mengklik `Select All ({N} records)` tanpa menyebut seleksi awal, sedangkan button itu hanya tampil setelah ada baris tercentang; spec menambah langkah penghubung memusatkan satu baris.
  - TC-215 Expected b: "counter total baris halaman" dituliskan sebagai `10 Non-Login Users selected` (page size default 10); teks plural mengikuti TC-214.
  - TC-216 dan TC-217 menyebut {N} tanpa nilai; spec memakai N = 12 dari seeding.
