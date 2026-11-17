---
id: TC-FA-TDC-E2E-109-class-yang-pernah-diposting-siklus-deactivate-activate-dan-edit-lalu-delete
title: "Class yang Pernah Diposting, Siklus Deactivate dan Activate, serta Edit lalu Delete Class Inactive"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-902
  - TC-FA-TDC-903
  - TC-FA-TDC-904
  - TC-FA-TDC-908
sourceRules: ["D-02", "D-04", "D-01", "FATDC-LOGIC-08h", "§3.6#r5", "§4.1.1#r9", "L-04", "T-02a", "FATDC-LOGIC-08g", "§3.6#r12", "F-FATDC-06.k6"]
smoke: []
dependsOn: []
trace:
  "D-02": 3
  "D-04": [6, 14, 15]
  "D-01": 9
  "FATDC-LOGIC-08h": [11, 20]
  "§3.6#r5": 12
  "§4.1.1#r9": 21
  "L-04": [24, 25]
  "T-02a": 30
  "FATDC-LOGIC-08g": 31
  "§3.6#r12": 34
  "F-FATDC-06.k6": 35
coverage:
  web: automated
---

# Class yang Pernah Diposting, Siklus Deactivate dan Activate, serta Edit lalu Delete Class Inactive

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Kebutuhan spec ini:
  - NB-1: Active, Last Posted Tax Year 2026, Used By 5 (TC-FA-TDC-903).
  - NB-KHS: Active, Last Posted Tax Year 2026, Used By 0 (TC-FA-TDC-902); NB-1, NB-2, dan NB-SL masih Active.
  - NB-4: Active, Used By 0 (TC-FA-TDC-904); target tiga perubahan status berurutan.
  - NB-OLD: Inactive, Used By 0, Last Posted Tax Year kosong (TC-FA-TDC-908); dihapus oleh spec ini.
  Asset Class pemakai dan Last Posted Tax Year dibentuk lewat fixture API (disediakan tim FE/BE). Sembilan baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` memulihkannya (NB-KHS Active, NB-4 Active, NB-OLD ada dengan Class Name semula). Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan class, Last Posted Tax Year, dan Asset Class pemakai lewat API; kemampuan baca jumlah entri Changelog Status class NB-4 (baseline dicatat sebelum aksi dan dibandingkan sesudahnya, 8b.10, S-12).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-903: Class dengan Used By lebih dari 0 dan sudah diposting: Deactivate diblokir D-02 dan Delete diblokir D-04

1. Catat baseline jumlah entri Status Changelog class NB-4
2. Klik toggle `Active` baris NB-1
3. Verifikasi dialog blok `Cannot Deactivate Tax Depreciation Class` dengan kalimat `Used by 5 asset classes. Change them in Asset Class first.`
4. Klik `[OK]` pada dialog
5. Klik tombol `⋯` baris NB-1 lalu `Delete`
6. Verifikasi dialog blok `Cannot Delete Tax Depreciation Class` dengan kalimat `It was used for fiscal depreciation in 2026.`
7. Klik `[OK]` untuk menutup dialog

### TC-FA-TDC-902: Class yang pernah diposting dengan Used By 0 tetap dapat dinonaktifkan tetapi tidak dapat dihapus

8. Klik toggle `Active` baris NB-KHS
9. Verifikasi dialog `Deactivate Tax Depreciation Class` tampil
10. Klik `[Deactivate]` pada dialog
11. Verifikasi toggle `Active` baris NB-KHS menjadi Off
12. Verifikasi toast sukses `Success, tax depreciation class has been deactivated.` tampil
13. Klik tombol `⋯` baris NB-KHS lalu `Delete`
14. Verifikasi dialog blok `Cannot Delete Tax Depreciation Class` dengan kalimat `It was used for fiscal depreciation in 2026.` tampil
15. Verifikasi dialog memuat tombol `[OK]`
16. Klik `[OK]` untuk menutup dialog

### TC-FA-TDC-904: Deactivate lalu Activate lalu Deactivate pada class yang sama mencatat tiga kejadian berurutan

17. Nonaktifkan NB-4 lewat toggle `Active` dan Confirm `[Deactivate]`
18. Aktifkan NB-4 lewat toggle `Active` dan Confirm `[Activate]`
19. Nonaktifkan NB-4 lewat toggle `Active` dan Confirm `[Deactivate]`
20. Verifikasi toggle `Active` baris NB-4 berakhir Off
21. Verifikasi kolom Used By baris NB-4 tetap 0
22. Klik ikon Changelog di toolbar
23. Filter Class Code `NB-4`
24. Verifikasi jumlah entri Status Changelog NB-4 bertambah tepat tiga dibanding baseline langkah 1
25. Verifikasi tiga baris teratas Status NB-4, tanpa mengandalkan urutan di antaranya, terdiri dari dua baris Active ke Inactive dan satu baris Inactive ke Active
26. Tutup modal Changelog

### TC-FA-TDC-908: Class Inactive tetap dapat diedit lalu dihapus

27. Klik link Class Code `NB-OLD`
28. Ubah Class Name menjadi `Kelompok lama revisi`
29. Klik `[Save]`
30. Verifikasi toast sukses `Success, tax depreciation class has been updated.` tampil
31. Verifikasi status NB-OLD tetap Inactive (toggle `Active` baris NB-OLD Off)
32. Klik tombol `⋯` baris NB-OLD lalu `Delete`
33. Klik `[Delete]` pada dialog
34. Verifikasi toast sukses `Success, tax depreciation class has been deleted.` tampil
35. Verifikasi baris NB-OLD tidak ada di tabel

## Notes

- Urutan TC: 903, 902, 904, 908. Blok yang hanya membaca dialog blok lebih dulu, blok yang mengubah status berikutnya, dan aksi yang menghapus data (TC-FA-TDC-908) di akhir.
- Langkah penghubung (S-03): langkah 1 (baseline Changelog, dibandingkan pada langkah 24; tidak ada aksi pada NB-4 sebelum langkah 17), langkah 4, 7, dan 16 (menutup dialog blok dengan `[OK]`), langkah 23 (Filter Class Code yang diminta TC pada langkah 4 TC-FA-TDC-904), dan langkah 26 (menutup modal Changelog). Pembukaan Drawer Edit memakai link Class Code (langkah 27).
- Pada TC-FA-TDC-902 dan TC-FA-TDC-903 Expected TC memakai penomoran lokal ("Langkah 1", "Langkah 2", "Langkah 3"); spec memetakannya ke langkah 9 sampai 12 dan 14 sampai 15 (902) serta langkah 3 dan 6 (903) (R-04).
- Cara baca langkah 25 (S-14): tiga entri Status dibuat berturut-turut dalam waktu singkat sedangkan kolom Date berketelitian menit, sehingga urutan di antara ketiganya tidak teramati; spec membaca tiga baris teratas hasil Filter sebagai himpunan, setelah selisih tiga dari baseline dibuktikan pada langkah 24, dan tidak mengasersi urutan.
- Baris hilang pada langkah 35 memakai toast sukses langkah 34 sebagai anchor (8b.2).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - TC-FA-TDC-908 tidak menyebut apakah Drawer Edit menutup sesudah `[Save]` dan cara membuka Drawer; spec membuka lewat link Class Code dan mengikuti perilaku Drawer yang menutup sesudah Save pada TC lain, tanpa asersi tambahan.
  - TC-FA-TDC-904 Expected c ("Kolom Used By NB-4 tetap 0") tidak menyebut lokasi pembacaan; spec membaca kolom Used By di tabel (langkah 21).
  - TC-FA-TDC-904 Expected b menyebut tiga baris Status "berurutan terbaru di atas" tanpa pembanding jumlah; spec memakai selisih terhadap baseline (langkah 24).
  - TC-FA-TDC-904 Expected b meminta urutan tiga entri yang dibuat berturut-turut dalam satu menit, padahal Date berketelitian menit sehingga urutan itu tidak teramati; spec mengasersi himpunan tiga baris tanpa urutan (S-14, S-15). Perlu konfirmasi QA agar Expected diubah menjadi himpunan.
