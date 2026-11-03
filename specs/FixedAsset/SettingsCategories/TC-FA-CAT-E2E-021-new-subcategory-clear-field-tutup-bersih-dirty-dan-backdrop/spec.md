---
id: TC-FA-CAT-E2E-021-new-subcategory-clear-field-tutup-bersih-dirty-dan-backdrop
title: "New Subcategory: Clear Field, Tutup Popup Bersih dan Terisi (Unsaved Changes), serta Klik Backdrop"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-63
  - TC-FA-CAT-68
  - TC-FA-CAT-69
  - TC-FA-CAT-70
  - TC-FA-CAT-71
coverage:
  web: automated
---

# New Subcategory: Clear Field, Tutup Popup Bersih dan Terisi (Unsaved Changes), serta Klik Backdrop

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); baris `Peripheral` (level 1) dipakai sebagai parent dan hanya dibaca. Tidak ada kategori yang tersimpan oleh spec ini (semua popup ditutup tanpa Submit), sehingga tidak ada cleanup data.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-63: [Clear Field] popup New Subcategory mempertahankan banner parent

1. Klik elipsis (⋯) pada baris `Peripheral`
2. Klik `+ Add Subcategory`
3. Isi Category Name `Temp Sub` dan Code `TSUB`
4. Klik `[Clear Field]`
5. Verifikasi Category Name dan Code kosong
6. Verifikasi banner `Adding subcategory under parent: Peripheral` tetap tampil
7. Verifikasi popup tetap terbuka tanpa dialog
8. Klik icon close (✕)

### TC-FA-CAT-68: Menutup popup New Subcategory tanpa isian tidak memunculkan dialog Unsaved Changes

9. Klik elipsis (⋯) pada baris `Peripheral`
10. Klik `+ Add Subcategory`
11. Klik icon close (✕)
12. Verifikasi popup langsung tertutup dan dialog Unsaved Changes tidak muncul
13. Klik elipsis (⋯) pada baris `Peripheral`
14. Klik `+ Add Subcategory`
15. Tekan `Esc`
16. Verifikasi popup langsung tertutup dan dialog Unsaved Changes tidak muncul

### TC-FA-CAT-71: Klik backdrop popup New Subcategory tidak menutup form baik bersih maupun terisi

17. Klik elipsis (⋯) pada baris `Peripheral`
18. Klik `+ Add Subcategory`
19. Klik area backdrop di luar popup
20. Verifikasi popup tetap terbuka
21. Isi Category Name `Backdrop Cat`
22. Klik area backdrop di luar popup lagi
23. Verifikasi popup tetap terbuka
24. Verifikasi input `Backdrop Cat` dipertahankan dan dialog Unsaved Changes tidak muncul

### TC-FA-CAT-69: Menutup popup New Subcategory yang terisi memunculkan dialog Unsaved Changes dan [Cancel] mempertahankan form

25. Ubah isi Category Name menjadi `Dirty Cat`
26. Klik icon close (✕)
27. Verifikasi dialog tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` serta `[Leave]` (severity warning)
28. Pada dialog klik `[Cancel]`
29. Verifikasi dialog tertutup, popup tetap terbuka, dan input `Dirty Cat` dipertahankan

### TC-FA-CAT-70: Dialog Unsaved Changes pada popup New Subcategory: [Leave] menutup popup tanpa menyimpan

30. Ubah isi Category Name menjadi `Leave Cat`
31. Tekan `Esc`
32. Verifikasi `Esc` memunculkan dialog Unsaved Changes yang sama dengan icon close (✕)
33. Pada dialog klik `[Leave]`
34. Verifikasi popup tertutup
35. Verifikasi kategori `Leave Cat` tidak tersimpan: tidak ada di tabel dan sidebar (anchor positif: halaman Categories tampil dengan sidebar)

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan dan penggabungan form (S-10, prinsip 6): TC-FA-CAT-71 diletakkan sebelum TC-FA-CAT-69 dan TC-FA-CAT-70; ketiganya memakai satu sesi popup (langkah 17 sampai 34) dan langkah isinya mengganti nilai Category Name (langkah 25 dan 30). Jumlah buka form (langkah 1, 9, 13, 17) sama dengan jumlah kejadian menutup (langkah 8, 11, 15, 33).
- Langkah penghubung (S-03): langkah 8 (menutup popup sesudah TC-FA-CAT-63; tanpa asersi dialog karena TC sumber tidak menyebutnya), langkah 25 dan 30 (mengganti nilai input).
- Temuan untuk QA:
  - TC-FA-CAT-63 tidak menyebut apakah popup yang sudah di-Clear Field dianggap bersih saat ditutup.
  - TC-FA-CAT-70 Expected b menyebut kategori `Leave Cat` "tidak ada di tabel dan sidebar" tanpa langkah pencarian; spec mengasersi lewat tampilan halaman sesudah popup tertutup.
