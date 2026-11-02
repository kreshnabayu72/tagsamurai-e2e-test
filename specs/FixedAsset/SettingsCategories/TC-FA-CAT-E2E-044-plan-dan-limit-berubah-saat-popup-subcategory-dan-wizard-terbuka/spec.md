---
id: TC-FA-CAT-E2E-044-plan-dan-limit-berubah-saat-popup-subcategory-dan-wizard-terbuka
title: "Plan atau Limit Berubah Saat Popup New Subcategory dan Popup Consolidation Terbuka: Submit Ditolak Server"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-528
  - TC-FA-CAT-529
  - TC-FA-CAT-301
coverage:
  web: automated
---

# Plan atau Limit Berubah Saat Popup New Subcategory dan Popup Consolidation Terbuka: Submit Ditolak Server

## Prerequisites

- Mode: FE+BE (backend nyata; perubahan plan, Hierarchy Depth Limit, dan cap Category count dilakukan Principal Automation lewat sesi API, tanpa intercept).
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatGrowth (Pre-setup #28), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Akun yang dipakai lewat langkah Ganti akun: Total Control yang sama pada client CatDepthLimit (Pre-setup #30), lalu pada client CatPostT0 (Pre-setup #33); password `Spectra.env.FA_TC_PASSWORD`.
- Pelaku pengubah: Principal Automation (Pre-setup #11), akun Admin Console yang mengubah plan client dan System Limits; email dan kredensial tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE. Dijalankan lewat sesi API aktor (lihat `suite.md`).
- Data Pre-setup #28 (CatGrowth, plan Growth, cap Category count 20 dan depth 2): `Growth Root` (Code `GR`) > `Growth Child` (Code `GC`). Principal menurunkan plan ke Starter (cap depth 1) dan memulihkannya ke Growth.
- Data Pre-setup #30 (CatDepthLimit, base Hierarchy Depth Limit 5, rantai `Depth 1` sampai `Depth 5`; varian limit 6 hanya untuk TC-FA-CAT-529): hook `before` spec ini menyetel Hierarchy Depth Limit CatDepthLimit ke 6 lewat fixture atau kemampuan System Limits yang disediakan tim FE/BE, lalu Principal menurunkannya dari 6 menjadi 5 pada langkah 18 dan langkah 27 memulihkan ke base limit 5 (bukan 6), agar spec lain (201, D-04) tidak terpengaruh.
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, 8 kategori usable `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`): Principal menurunkan cap Category count plan dari 5 menjadi 4 lalu memulihkannya ke 5. Spec tidak menyimpan seleksi.
- Data Dinamis: Category Name `Race Depth {runId}-044` dan `Race Limit {runId}-044` (keduanya ditolak server, tidak tersimpan).
- Kemampuan teknis: membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline, S-12) dan membaca state BE kategori; disediakan tim FE/BE.
- State global yang diubah: plan client CatGrowth, Hierarchy Depth Limit CatDepthLimit (disetel 6 di hook `before`, dipulihkan ke base 5), dan cap Category count CatPostT0. Pemulihan: langkah penghubung memulihkan tiap state setelah blok, dan hook `after` memulihkan Hierarchy Depth Limit CatDepthLimit ke 5 bila spec berhenti di tengah.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-528: Plan diturunkan saat popup New Subcategory terbuka

1. Catat baseline jumlah entri Changelog kategori CatGrowth (N1)
2. Klik elipsis (⋯) pada baris `Growth Root` > `+ Add Subcategory`
3. Isi Category Name `Race Depth {runId}-044`
4. Principal Automation (sesi API) menurunkan plan client CatGrowth ke Starter (cap depth 1) hingga perubahan tersimpan
5. Klik `[Submit]`
6. Verifikasi dialog kontekstual `Cannot Add Category` · `This exceeds the category depth limit for your plan. Upgrade to nest deeper.` · `[OK]` tampil (server menolak dengan 409)
7. Verifikasi toast generik tidak tampil
8. Klik `[OK]` pada dialog
9. Klik node `Growth Root` di Sidebar Category Tree
10. Verifikasi baris `Growth Child` tampil di tabel (pembanding pada surface yang sama)
11. Verifikasi kategori `Race Depth {runId}-044` tidak tersimpan: tidak ada baris dengan nama itu di bawah `Growth Root`
12. Verifikasi jumlah entri Changelog sama dengan N1 (tidak ada baris log)
13. Principal Automation (sesi API) memulihkan plan client CatGrowth ke Growth hingga perubahan tersimpan

### TC-FA-CAT-529: Hierarchy Depth Limit diturunkan saat popup New Subcategory terbuka

14. Ganti akun: logout, lalu login sebagai Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatDepthLimit dengan `Spectra.env.FA_TC_PASSWORD`
15. Catat baseline jumlah entri Changelog kategori CatDepthLimit (N2)
16. Klik elipsis (⋯) pada node `Depth 5` (L5) di sidebar > `+ Add Subcategory`
17. Isi Category Name `Race Limit {runId}-044`
18. Principal Automation (sesi API) menurunkan Hierarchy Depth Limit dari 6 menjadi 5 di System Limits hingga perubahan tersimpan
19. Klik `[Submit]`
20. Verifikasi dialog kontekstual `Cannot Add Category` · `You've reached the platform limit of 5 levels. Contact support if you need a higher limit.` · `[OK]` tampil tanpa CTA upgrade (server menolak dengan 409)
21. Klik `[OK]` pada dialog
22. Klik node `Depth 4` di Sidebar Category Tree
23. Verifikasi baris `Depth 5` tampil di tabel (pembanding pada surface yang sama)
24. Klik node `Depth 5` di Sidebar Category Tree
25. Verifikasi kategori `Race Limit {runId}-044` tidak tersimpan: tidak ada anak di bawah node `Depth 5`
26. Verifikasi jumlah entri Changelog sama dengan N2 (tidak ada baris log)
27. Principal Automation (sesi API) memulihkan Hierarchy Depth Limit ke 5 (base limit Pre-setup #30) hingga perubahan tersimpan

### TC-FA-CAT-301: Cap berubah saat popup Consolidation terbuka

28. Ganti akun: logout, lalu login sebagai Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 dengan `Spectra.env.FA_TC_PASSWORD`
29. Klik `[Choose Categories]`
30. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear` (5 kategori)
31. Principal Automation (sesi API) menurunkan cap Category count plan dari 5 menjadi 4 hingga perubahan tersimpan
32. Klik `[Save Selection]`
33. Verifikasi toast error `Error, failed to update category consolidation.` tampil (server menolak validasi X <= cap)
34. Verifikasi counter inline `severity="danger"` diperbarui terhadap cap baru 4
35. Verifikasi popup Consolidation tetap terbuka
36. Verifikasi seleksi 5 kategori dipertahankan
37. Klik icon close (✕) pada popup Consolidation
38. Principal Automation (sesi API) memulihkan cap Category count plan ke 5 hingga perubahan tersimpan

## Notes

- Pelaku pengubah memakai sesi API (bagian 3 P-2, 2026-10-30): tidak ada konteks UI kedua. TC-FA-CAT-168, 210, dan 600 ada di spec 184.
- Langkah penghubung (S-03, S-09, S-14): langkah 1 dan 15 (baseline log, S-12), langkah 8 dan 21 (menutup dialog hasil penolakan), langkah 9, 22, dan 24 (memilih node induk dan pembanding sebelum asersi absence), langkah 13, 27, 38 (memulihkan state), langkah 14 dan 28 (ganti akun eksplisit, S-07), langkah 37 (menutup popup Consolidation).
- Asersi "tidak ada baris log" (langkah 12, 26) ditulis dengan baseline di spec ini; TC-FA-CAT-528 dan 529 tidak punya spec absence yang memuat aksinya (S-05). Surface yang diperiksa hanya Changelog.
- Temuan untuk QA:
  - TC-FA-CAT-528 dan 529 tidak menyatakan apakah popup New Subcategory tertutup setelah dialog konflik `[OK]`; spec tidak menulis penutupan popup tambahan (ambigu, S-15). Langkah 9 dan 22 mengandaikan sidebar dapat diklik sesudah `[OK]` (popup tertutup atau tidak menghalangi); bila popup tetap terbuka, langkah itu perlu penutupan form dirty (S-08) setelah TC memastikan perilakunya.
  - TC-FA-CAT-301 tidak menyatakan apakah menutup popup Consolidation yang berisi seleksi memunculkan dialog Unsaved Changes; spec hanya menutup popup.
  - TC-FA-CAT-301 menyebut "dua sesi" padahal pelaku kedua hanya mengubah cap; spec memakai sesi API Principal.
  - Surface log pada "tidak ada baris log" TC-FA-CAT-528 dan 529 tidak disebut; spec memeriksa Changelog.
  - Email dan password Principal Automation (Pre-setup #11) tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE" (S-11).
- Spec melewati 35 langkah (38 langkah). Alasan: satu kelas harness dan satu dataset; langkah penghubung wajib (S-03, S-08, S-09) menambah langkah dan blok berdiri sendiri.
