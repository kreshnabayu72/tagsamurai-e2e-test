---
id: TC-FA-CAT-E2E-183-izin-dicabut-saat-bulk-delete-dan-wizard-consolidation-terbuka
title: "Izin Dicabut Saat Dialog Bulk Delete dan Popup Consolidation Terbuka: Aksi Ditolak 403 dan UI Di-refresh"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-541
  - TC-FA-CAT-542
coverage:
  web: automated
---

# Izin Dicabut Saat Dialog Bulk Delete dan Popup Consolidation Terbuka: Aksi Ditolak 403 dan UI Di-refresh

## Prerequisites

- Mode: FE+BE (backend nyata; pencabutan capability dan Access Level dilakukan Principal Automation lewat sesi API, tanpa intercept).
- Akun aktor pertama: Delete-Only (Pre-setup #6) `deleteOnly_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_DO_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai lewat langkah Ganti akun: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password `Spectra.env.FA_TC_PASSWORD`.
- Pelaku pengubah: Principal Automation (Pre-setup #11), akun Admin Console; email dan kredensial tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE. Dijalankan lewat sesi API aktor (lihat `suite.md`); kemampuan mencabut capability Delete, mengubah Access Level aktor, dan memulihkannya disediakan tim FE/BE tanpa endpoint karangan.
- Data Pre-setup #20 (CatMain) dan #39: baris `Vehicle` (Total Asset 0) dan `Heavy Tools` (Code `HT`, leaf, Total Asset 0) menjadi target Bulk Delete yang ditolak; keduanya tetap ada.
- Data Pre-setup #33 (CatPostT0, T-0 sudah lewat, Starter cap 5, 8 kategori usable `Alpha Tech`, `Beta Tools`, dan seterusnya, belum pernah Submit selection): Alert Consolidation dan `[Choose Categories]` tampil bagi Total Control. Spec tidak menyimpan seleksi; status Excess tidak berubah.
- Kemampuan teknis: membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline, S-12) dan membaca status Excess kategori dari state BE; disediakan tim FE/BE.
- State global yang diubah: capability Delete akun Delete-Only dan Access Level akun Total Control CatPostT0. Pemulihan: langkah penghubung memulihkan keduanya setelah tiap blok, dan hook `after` memulihkannya bila spec berhenti di tengah.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_DO_PASSWORD` dan `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-541: Hak Delete dicabut saat dialog Bulk Delete D-11 terbuka

1. Catat baseline jumlah entri Changelog kategori (N1)
2. Centang baris `Vehicle` dan `Heavy Tools`
3. Klik `[Delete]` pada Bulk Action Bar sampai dialog D-11 tampil
4. Principal Automation (sesi API) mencabut capability Delete aktor hingga perubahan tersimpan
5. Klik `[Delete]` pada dialog
6. Verifikasi toast error `You don't have permission to do this.` tampil
7. Verifikasi halaman tidak berpindah (tanpa redirect)
8. Verifikasi aksi atau menu Delete hilang sesuai capability baru (UI di-refresh)
9. Verifikasi baris `Vehicle` tetap ada di tabel
10. Verifikasi baris `Heavy Tools` tetap ada di tabel
11. Verifikasi jumlah entri Changelog sama dengan N1 (tidak ada baris log baru)
12. Principal Automation (sesi API) memulihkan capability Delete aktor hingga perubahan tersimpan
13. Muat ulang halaman Categories agar seleksi baris dibersihkan

### TC-FA-CAT-542: Access Level Total Control dicabut saat popup Consolidation terbuka

14. Ganti akun: logout, lalu login sebagai Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 dengan `Spectra.env.FA_TC_PASSWORD`
15. Catat baseline jumlah entri Changelog kategori CatPostT0 (N2)
16. Klik `[Choose Categories]`
17. Centang `Keep usable` pada `Alpha Tech`
18. Centang `Keep usable` pada `Beta Tools`
19. Principal Automation (sesi API) mengubah Access Level aktor menjadi Read Only hingga perubahan tersimpan
20. Klik `[Save Selection]`
21. Verifikasi toast error `You don't have permission to do this.` tampil
22. Verifikasi halaman tidak berpindah (tanpa redirect)
23. Verifikasi popup Consolidation tetap terbuka
24. Verifikasi seleksi `Alpha Tech` dan `Beta Tools` dipertahankan
25. Klik icon close (✕) pada popup Consolidation
26. Verifikasi Alert Consolidation Hidden (UI di-refresh)
27. Verifikasi `[Choose Categories]` Hidden
28. Verifikasi tidak ada status Excess yang berubah: jumlah kategori Excess CatPostT0 sama dengan sebelum aksi (dibaca dari state BE)
29. Verifikasi jumlah entri Changelog sama dengan N2 (tidak ada baris log)
30. Principal Automation (sesi API) memulihkan Access Level aktor menjadi Total Control hingga perubahan tersimpan

## Notes

- Dua blok berdiri sendiri dan berpola sama (izin atau Access Level dicabut saat dialog atau popup terbuka). TC-FA-CAT-527, 209, dan 539 ada di spec 043.
- Pelaku pengubah memakai sesi API (bagian 3 P-2, 2026-10-30): tidak ada konteks UI kedua.
- Langkah penghubung (S-03, S-09): langkah 1 dan 15 (baseline log, S-12), langkah 12 dan 30 (memulihkan state), langkah 13 (muat ulang agar seleksi dibersihkan; tidak ada form dirty), langkah 14 (ganti akun eksplisit, S-07), langkah 25 (menutup popup Consolidation; TC menyebut "setelah popup ditutup").
- Asersi "tidak ada baris log" (langkah 11, 29) ditulis dengan baseline di spec ini karena spec absence tidak memuat aksi kedua TC ini (S-05). Surface yang diperiksa hanya Changelog.
- Temuan untuk QA:
  - TC-FA-CAT-541 tidak menyatakan apakah dialog D-11 dan seleksi baris masih ada setelah toast 403; spec memuat ulang halaman sebagai pembersih seleksi (ambigu, S-15).
  - TC-FA-CAT-542 tidak menyatakan apakah menutup popup Consolidation yang berisi seleksi memunculkan dialog Unsaved Changes; spec tidak menulis langkah dialog itu.
  - Surface log pada Expected "Tidak ada baris log" TC-FA-CAT-541 dan 542 tidak disebut; spec memeriksa Changelog saja.
  - Email dan password Principal Automation (Pre-setup #11) tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE" (S-11).
