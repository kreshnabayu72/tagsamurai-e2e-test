---
id: TC-FA-CAT-E2E-043-izin-dicabut-saat-popup-create-edit-delete-terbuka
title: "Izin Dicabut Saat Popup Create, Popup Edit, dan Dialog Delete Terbuka: Aksi Ditolak 403 dan UI Di-refresh"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-527
  - TC-FA-CAT-209
  - TC-FA-CAT-539
coverage:
  web: automated
---

# Izin Dicabut Saat Popup Create, Popup Edit, dan Dialog Delete Terbuka: Aksi Ditolak 403 dan UI Di-refresh

## Prerequisites

- Mode: FE+BE (backend nyata; pencabutan capability dilakukan Principal Automation lewat sesi API, tanpa intercept).
- Akun aktor pertama: Create-Only (Pre-setup #4) `createOnly_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_CO_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai lewat langkah Ganti akun: Update-Only (Pre-setup #5) `updateOnly_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_UO_PASSWORD`; Delete-Only (Pre-setup #6) `deleteOnly_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_DO_PASSWORD`.
- Pelaku pencabut: Principal Automation (Pre-setup #11), akun Admin Console yang mengubah capability; email dan kredensial tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE. Dijalankan lewat sesi API aktor (lihat `suite.md`); kemampuan mencabut dan memulihkan capability Manage Asset Master Data (C, U, D) akun aktor disediakan tim FE/BE tanpa endpoint karangan.
- Data Pre-setup #20 (CatMain): baris `Furniture` (Code `FURN`, leaf) dan `Vehicle` (Code `VEH`, leaf, Total Asset 0) dibaca dan menjadi target aksi yang ditolak server; tidak ada perubahan tersimpan. Data Dinamis: Category Name `Revoked Cat {runId}-043` (ditolak, tidak tersimpan).
- Kemampuan teknis: membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline, S-12) dan membaca state BE kategori; disediakan tim FE/BE.
- State global yang diubah: capability aktor. Pemulihan: langkah penghubung memulihkan capability setelah tiap blok, dan hook `after` memulihkan capability ketiga akun bila spec berhenti di tengah.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_CO_PASSWORD`, `FA_UO_PASSWORD`, dan `FA_DO_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-527: Hak Create dicabut saat popup New Category terbuka

1. Catat baseline jumlah entri Changelog kategori (N1)
2. Klik `[+] Category` pada sidebar
3. Isi Category Name `Revoked Cat {runId}-043`
4. Principal Automation (sesi API) mencabut capability Create aktor hingga perubahan tersimpan
5. Klik `[Submit]`
6. Verifikasi toast error `You don't have permission to do this.` tampil
7. Verifikasi halaman tidak berpindah (tanpa redirect)
8. Klik icon close (✕) pada popup New Category
9. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
10. Klik `[Leave]`
11. Verifikasi aksi atau menu Create hilang sesuai capability baru (UI di-refresh)
12. Verifikasi kategori `Revoked Cat {runId}-043` tidak tersimpan: tidak ada baris dengan nama itu di tabel
13. Verifikasi jumlah entri Changelog sama dengan N1 (tidak ada baris log baru)
14. Principal Automation (sesi API) memulihkan capability Create aktor hingga perubahan tersimpan

### TC-FA-CAT-209: Hak akses dicabut saat popup Edit terbuka

15. Ganti akun: logout, lalu login sebagai Update-Only `updateOnly_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_UO_PASSWORD`
16. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
17. Ubah Description menjadi `Revoked desc`
18. Principal Automation (sesi API) mencabut capability Update aktor hingga perubahan tersimpan
19. Klik `[Save]`
20. Verifikasi toast error `You don't have permission to do this.` tampil
21. Verifikasi halaman tidak berpindah (tanpa redirect)
22. Klik icon close (✕) pada popup Edit
23. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
24. Klik `[Leave]`
25. Verifikasi menu atau aksi Edit hilang sesuai capability baru (UI di-refresh)
26. Verifikasi perubahan Description `Revoked desc` tidak tersimpan (dibaca dari state BE)
27. Principal Automation (sesi API) memulihkan capability Update aktor hingga perubahan tersimpan

### TC-FA-CAT-539: Hak Delete dicabut saat dialog D-09 terbuka

28. Ganti akun: logout, lalu login sebagai Delete-Only `deleteOnly_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_DO_PASSWORD`
29. Catat baseline jumlah entri Changelog kategori (N2)
30. Klik elipsis (⋯) pada baris `Vehicle` > `Delete` sampai dialog D-09 tampil
31. Principal Automation (sesi API) mencabut capability Delete aktor hingga perubahan tersimpan
32. Klik `[Delete]` pada dialog
33. Verifikasi toast error `You don't have permission to do this.` tampil
34. Verifikasi halaman tidak berpindah (tanpa redirect)
35. Verifikasi aksi atau menu Delete hilang sesuai capability baru (UI di-refresh)
36. Verifikasi baris `Vehicle` tetap ada di tabel
37. Verifikasi jumlah entri Changelog sama dengan N2 (tidak ada baris log baru)
38. Principal Automation (sesi API) memulihkan capability Delete aktor hingga perubahan tersimpan

## Notes

- Spec berisi tiga blok yang berdiri sendiri dan berpola sama (izin dicabut saat form atau dialog terbuka), sehingga jumlah langkah (38) melewati sekitar 35 tanpa mengubah makna tiap blok bila blok lain gagal. TC-FA-CAT-541 dan TC-FA-CAT-542 ada di spec 183.
- Pelaku pencabut memakai sesi API (bagian 3 P-2, 2026-10-30): tidak ada konteks UI kedua.
- Langkah penghubung (S-03, S-09): langkah 1, 29 (baseline log, S-12), langkah 8 sampai 10 dan 22 sampai 24 (menutup form dirty secara deterministik, S-08), langkah 14, 27, 38 (memulihkan capability), langkah 15 dan 28 (ganti akun eksplisit, S-07).
- Urutan: Verifikasi "UI di-refresh" (langkah 11, 25) ditulis sesudah popup ditutup, karena TC-FA-CAT-542 menyebut refresh terjadi setelah popup ditutup dan TC sumber tidak menyatakan apakah popup tetap terbuka setelah 403.
- "Tidak ada baris log baru" (langkah 13, 37) ditulis dengan baseline di spec ini; spec absence tidak memuat aksi TC-FA-CAT-527 dan TC-FA-CAT-539, sehingga rujukan saja tidak memenuhi Expected (S-05). Surface yang diperiksa hanya Changelog.
- Temuan untuk QA:
  - TC-FA-CAT-527, 209, 539 tidak menyatakan apakah popup atau dialog tetap terbuka setelah toast 403; spec menutup popup form dengan alur Unsaved Changes (S-08) dan tidak menutup dialog Delete. Perlu ketegasan di TC (ambigu, S-15).
  - Expected "Tidak ada baris log baru" pada TC-FA-CAT-527 dan 539 tidak menyebut surface log (Changelog, System Log, Activity Log); spec memeriksa Changelog saja.
  - Email dan password Principal Automation (Pre-setup #11) tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE" (S-11).
  - TC-FA-CAT-209 tidak punya Expected untuk log dan tidak memberi langkah observasi state tersimpan; langkah 26 memakai pembacaan state BE sesuai Expected b ("perubahan tidak tersimpan").
- Spec melewati 35 langkah (38 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
