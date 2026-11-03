---
id: TC-FA-FAAM-E2E-020-mobile-form-tree-picker-changelog-dan-tabel-detail
title: "Mobile: Form Create-Edit Satu Kolom, Tree Picker, Changelog, dan Tabel Detail Bottom Sheet"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-317
  - TC-FA-FAAM-328
  - TC-FA-FAAM-737
  - TC-FA-FAAM-738
coverage:
  web: unsupported
  mobile: automated
---

# Mobile: Form Create-Edit Satu Kolom, Tree Picker, Changelog, dan Tabel Detail Bottom Sheet

## Prerequisites

- Mode: FE+BE (backend nyata), aplikasi FAMS mobile native Android.
- Perangkat: perangkat atau emulator Android dengan aplikasi FAMS terpasang (disediakan tim FE). Perangkat bersama: `parallel: false`.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di aplikasi di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, `after`, dan seed API per TC dirujuk apa adanya.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `Dell Latitude` (#10, Tab Total Assets) dan Changelog berisi entri contoh PRD §4.1 Modal Changelog Example Data (#28).
- Data Dinamis (suffix `{runId}-020`, seed API di hook `before`, dihapus hook `after`): `Edit Target Item {runId}-020` (salinan fixture #13d, Total Asset 0), hanya dibuka di form Edit tanpa Save.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-737 dan TC-FA-FAAM-328: Form Create, Tree Picker, dan form Edit

1. Tap `[+ Asset Name]`
2. Verifikasi form Create tampil sebagai bottom sheet satu kolom yang dapat di-scroll
3. Scroll form Create sampai bawah
4. Verifikasi footer tetap terlihat saat scroll dan memuat checkbox `Stay on this form after submitting`, `[Clear Field]`, dan `[Submit]`
5. Tap `[Select Category]`
6. Verifikasi Tree Picker tampil sebagai bottom sheet
7. Tutup Tree Picker
8. Tutup form Create dengan `✕` (tanpa perubahan)
9. Ketik Search `Edit Target Item {runId}-020`, tekan Enter
10. Tap `⋯` pada card `Edit Target Item {runId}-020` lalu `Edit`
11. Verifikasi form Edit tampil sebagai bottom sheet satu kolom yang dapat di-scroll
12. Scroll form Edit sampai bawah
13. Verifikasi footer tetap terlihat dan memuat `[Clear Field]` dan `[Save]`
14. Verifikasi footer form Edit tidak memuat checkbox `Stay on this form after submitting`
15. Tutup form Edit dengan `✕` (tanpa perubahan)

### TC-FA-FAAM-317: Mobile: tabel di tab Detail tampil sebagai card list pada bottom sheet

16. Ganti isi Search dengan `Dell Latitude`, tekan Enter
17. Tap card `Dell Latitude`
18. Tap tab Total Assets
19. Verifikasi bottom sheet menampilkan tab dengan card list per aset
20. Tutup bottom sheet Detail

### TC-FA-FAAM-738: Mobile: Changelog tampil sebagai bottom sheet dengan card list

21. Tap ikon Changelog di header halaman
22. Verifikasi Changelog: Asset Name terbuka sebagai bottom sheet dengan Title `Changelog: Asset Name`
23. Verifikasi entri tampil sebagai card list, satu card per entri
24. Tutup bottom sheet Changelog

## Notes

- Mode: FE+BE (aplikasi FAMS Android native). Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular. `coverage.web: unsupported` dan `coverage.mobile: automated`.
- Urutan TC di spec: 737 bersama 328, 317, 738. TC-328 (Tree Picker) memakai form Create yang sudah dibuka TC-737 (satu pembukaan form, bagian 3); form Create dibuka sekali (langkah 1) dan ditutup sekali (langkah 8).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 3 dan 12 (scroll sesuai Langkah uji), langkah 7 (menutup Tree Picker), langkah 8 dan 15 (menutup form tanpa perubahan, sehingga tanpa dialog `Unsaved Changes`), langkah 9 dan 16 (Search untuk menemukan card target, R-16), langkah 20 dan 24 (menutup bottom sheet).
- Langkah 14 (absence checkbox Stay) memakai footer yang terlihat pada langkah 13 sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-737 Langkah 3 menutup form Create sebelum membuka form Edit; spec mengikuti urutan itu. TC-328 tidak menyebut cara menutup Tree Picker; spec menutupnya sebelum menutup form.
  - TC-317 Expected tidak menyebut aset yang diamati pada card list; spec mengasersi bentuk card list per aset tanpa menyebut nilai.
  - TC-738 tidak menyebut jumlah entri Changelog; spec tidak menulis angka literal.
