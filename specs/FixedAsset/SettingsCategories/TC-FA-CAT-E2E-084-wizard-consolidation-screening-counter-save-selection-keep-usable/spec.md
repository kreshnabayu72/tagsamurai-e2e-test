---
id: TC-FA-CAT-E2E-084-wizard-consolidation-screening-counter-save-selection-keep-usable
title: "Wizard Category Consolidation: Screening Popup, Counter Keep usable, Save Selection, Retensi Centang, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-288
  - TC-FA-CAT-289
  - TC-FA-CAT-290
  - TC-FA-CAT-291
  - TC-FA-CAT-297
  - TC-FA-CAT-543
coverage:
  web: automated
---

# Wizard Category Consolidation: Screening Popup, Counter Keep usable, Save Selection, Retensi Centang, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, belum pernah submit selection): 8 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`; varian 12 kategori dengan tambahan `Extra 01` sampai `Extra 04` untuk TC-FA-CAT-297. Pergantian varian dan pemulihan lewat fixture backend yang disediakan tim FE/BE, dijalankan di hook `before`, hook `after`, dan sebagai langkah penghubung.
- Spec menyimpan seleksi pada TC-FA-CAT-543 sehingga mengubah state Pre-setup #33 (tiga kategori menjadi Excess dan entri Changelog `Marked as Excess (Category Consolidation)`); dipulihkan lewat fixture di atas. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: membaca jumlah baris Changelog `Marked as Excess (Category Consolidation)` sebelum aksi (baseline); disediakan tim FE/BE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-288: Screening popup Category Consolidation dari Alert pasca-T-0

1. Klik `[Choose Categories]` pada Alert Category Consolidation
2. Verifikasi header `Choose which categories stay active`
3. Verifikasi subtitle `You can keep up to 5 categories. The rest will become read-only until you free up space.`
4. Verifikasi counter realtime `0 of 5 categories selected`
5. Verifikasi Toolbar Search dan Filter tampil
6. Verifikasi tabel T-FACAT-06 dengan checkbox `Keep usable` semuanya unchecked (tanpa pra-isi)
7. Verifikasi pagination standar default 10
8. Verifikasi Footer tombol `[Cancel]` dan `[Save Selection]` (primary) tampil
9. Verifikasi `[Save Selection]` disabled karena belum ada centang

### TC-FA-CAT-291: Tanpa centang Save Selection disabled karena tidak ada node penampung darurat

10. Verifikasi `[Save Selection]` disabled saat tidak ada centang (X = 0 tidak diizinkan)
11. Verifikasi tidak ada node `Uncategorized` di tabel

### TC-FA-CAT-289: Counter Keep usable berubah realtime dan Save Selection aktif bila ada centang dalam batas cap

12. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, dan `Gamma Parts`
13. Verifikasi counter `3 of 5 categories selected`
14. Hapus centang `Gamma Parts`
15. Verifikasi counter `2 of 5 categories selected`
16. Verifikasi `[Save Selection]` aktif selama ada centang dan jumlah tidak melebihi 5

### TC-FA-CAT-290: Keep usable melebihi cap, counter danger dan Save Selection disabled

17. Centang `Keep usable` pada `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, dan `Zeta Vehicle` (total 6 centang bersama `Alpha Tech` dan `Beta Tools`)
18. Verifikasi counter `6 of 5 categories selected` berseverity danger
19. Verifikasi `[Save Selection]` disabled
20. Klik `[Cancel]`
21. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]` tampil
22. Klik `[Leave]` pada dialog

### TC-FA-CAT-297: Centang dipertahankan saat Search, Filter, dan pindah halaman

23. Terapkan varian 12 kategori CatPostT0 (fixture) dan muat ulang halaman Categories
24. Klik `[Choose Categories]` pada Alert Category Consolidation
25. Centang `Keep usable` pada `Alpha Tech`
26. Ketik Search `Beta`, tekan Enter
27. Centang `Keep usable` pada `Beta Tools`
28. Klik `(←)` pada kotak Search
29. Pindah ke halaman 2
30. Verifikasi counter `2 of 5 categories selected` (menghitung semua yang tercentang termasuk yang sedang tidak tampil)
31. Pindah ke halaman 1
32. Verifikasi centang `Alpha Tech` dan `Beta Tools` tetap ada
33. Klik `[Cancel]`
34. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]` tampil
35. Klik `[Leave]` pada dialog

### TC-FA-CAT-543: Klik ganda cepat pada [Save Selection] hanya menerapkan seleksi sekali

36. Terapkan varian 8 kategori CatPostT0 (fixture pemulihan) dan muat ulang halaman Categories
37. Catat baseline N1 jumlah baris Changelog `Marked as Excess (Category Consolidation)`
38. Klik `[Choose Categories]` pada Alert Category Consolidation
39. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear`
40. Klik `[Save Selection]` dua kali dengan cepat
41. Verifikasi hanya satu toast `Success, category consolidation has been updated.`
42. Buka Modal Changelog
43. Verifikasi Changelog bertambah tepat tiga baris `Marked as Excess (Category Consolidation)` (`Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`), tanpa baris ganda (N1 + 3)
44. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (fungsional Wizard Consolidation pada satu client), dan berdiri sendiri; sebagian langkah hanya pergantian varian, penutupan popup, dan pencatatan baseline.
- Urutan TC: TC-FA-CAT-288, TC-FA-CAT-291, TC-FA-CAT-289, TC-FA-CAT-290, TC-FA-CAT-297, lalu TC-FA-CAT-543 (aksi yang mengubah state di akhir, S-10). Popup yang sama dipakai berulang untuk kasus tanpa submit (satu pembukaan, centang dikosongkan di antara kasus); TC-FA-CAT-291 dan TC-FA-CAT-289 tidak membuka ulang popup karena state-nya sama.
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): pergantian varian CatPostT0 dan muat ulang, `[Cancel]`, `(←)` pada Search, berpindah halaman, pencatatan baseline, menutup Modal Changelog. Dialog `Unsaved Changes` sesudah `[Cancel]` pada popup yang berisi centang diverifikasi lalu `[Leave]` (S-08).
- Temuan untuk QA:
  - TC-FA-CAT-290 mensyaratkan 6 centang dari keadaan nol; spec melanjutkan dari 2 centang TC-FA-CAT-289 (`Alpha Tech`, `Beta Tools`) sehingga total tetap 6.
  - TC-FA-CAT-543 menyebut tiga baris `Marked as Excess` tanpa baseline; spec memakai selisih +3 (S-12).
  - TC-FA-CAT-297 tidak menyebut Filter pada langkah walau judul menyebutnya; spec tidak menguji Filter.
