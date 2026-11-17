---
id: TC-FA-TDC-E2E-186-android-toolbar-aksi-baris-restore-guided-tooltip-dan-akses-read-only
title: "Android: Toolbar, Aksi Baris, Restore Default Classes, Guided Tooltip, dan Akses Read Only"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-666
  - TC-FA-TDC-667
  - TC-FA-TDC-669
  - TC-FA-TDC-670
  - TC-FA-TDC-671
  - TC-FA-TDC-662
  - TC-FA-TDC-668
sourceRules: ["§4.6#b5", "§4.6#b4", "§4.1.1#p8", "§4.6#b6", "§4.8#r13", "§4.8#r15", "ST-23", "§4.7#p2", "FATDC-LOGIC-08i", "FATDC-LOGIC-08h", "§4.8#r2", "§4.8#r3", "§4.8#r9"]
smoke: []
dependsOn: []
trace:
  "§4.6#b5": [1, 5, 8, 20, 21]
  "§4.6#b4": 3
  "§4.1.1#p8": 3
  "§4.6#b6": 6
  "§4.8#r13": 14
  "§4.8#r15": 14
  "ST-23": 18
  "§4.7#p2": [28, 30]
  "FATDC-LOGIC-08i": 35
  "FATDC-LOGIC-08h": 38
  "§4.8#r2": 39
  "§4.8#r3": 39
  "§4.8#r9": 40
anchor: [11, 26, 36, 37]
coverage:
  mobile: automated
---

# Android: Toolbar, Aksi Baris, Restore Default Classes, Guided Tooltip, dan Akses Read Only

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi native Android Fixed Asset di perangkat atau emulator Android (`coverage.mobile`), disediakan tim FE. Perangkat Android uji dipakai bersama sehingga spec berjalan serial (`parallel: false`, sesuai `suite.md`).
- Akun: Total Control sebagai akun pertama (langkah 1 sampai 31) dan Read Only sebagai akun kedua (langkah 32 sampai 40), keduanya company uji Fixed Asset. Login Total Control di hook `before` spec ini pada aplikasi Android; layar Settings > Accounting > Tax Depreciation Class dibuka hook `before` spec ini (hook `beforeEach` suite membuka halaman web, bukan aplikasi native). Akun Read Only login lewat langkah ganti akun eksplisit (langkah 32 dan 33). Akun dan email kedua role disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD` (Total Control) dan `Spectra.env.FA_RO_PASSWORD` (Read Only). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite dan seeding mengikuti `suite.md`. Pengecualian flag Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tax-depreciation-class` true; spec ini menghapus flag pada langkah 24 untuk blok TC-FA-TDC-671 dan hook `after` memulihkan flag ke true.
- Data Pre-setup (dibaca, tidak diubah kecuali langkah 16; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; NB-OLD Active Off; isi riwayat Changelog tidak diasersi di spec ini (langkah 3 hanya mengasersi judul bottom sheet). Data Dinamis: tidak ada.
- Kemampuan teknis: menghapus seluruh Tax Depreciation Class dan memulihkan sembilan class Example Data lewat seeding API suite (`suite.md`); menghapus flag Guided Tooltip akun (disediakan tim FE/BE; nama kunci flag dari TC); gestur swipe pada walkthrough.
- State global yang diubah: seluruh class dihapus pada blok TC-FA-TDC-670 (langkah 16) dan dipulihkan pada langkah 23 (hook `after` sebagai cadangan); flag Guided Tooltip akun Total Control (langkah 24; hook `after` memulihkan); sesi akun diganti ke Read Only pada langkah 32.

## Test Steps

### TC-FA-TDC-666: Ikon Changelog di header halaman membuka bottom sheet

1. Verifikasi ikon Changelog berada di header halaman, bukan di dalam `[⋯]` toolbar
2. Tap ikon Changelog di header halaman
3. Verifikasi bottom sheet `Changelog: Tax Depreciation Class` tampil
4. Tutup bottom sheet Changelog

### TC-FA-TDC-667: Toolbar `[⋯]` dan `[🔍]`, Filter dan Download di dalam `[⋯]`, dan `+ Class` di bawah toolbar

5. Verifikasi toolbar menampilkan `[⋯]` dan `[🔍]`
6. Verifikasi `+ Class` terlihat di bawah toolbar di atas card list
7. Tap `[⋯]`
8. Verifikasi bottom sheet `[⋯]` memuat Column Visibility, Filter, dan Download
9. Tutup bottom sheet `[⋯]`
10. Tap `[🔍]`
11. Verifikasi search bar inline mengembang
12. Tutup search bar inline

### TC-FA-TDC-669: Aksi baris lewat ikon ⋯ di pojok kanan card

13. Tap ikon `⋯` di pojok kanan card NB-4
14. Verifikasi menu aksi baris memuat `Edit` dan `Delete`
15. Tutup menu aksi baris

### TC-FA-TDC-670: Restore default classes hanya di Empty State

16. Hapus seluruh Tax Depreciation Class (tabel tanpa class)
17. Buka ulang layar Settings > Accounting > Tax Depreciation Class
18. Verifikasi Empty State `No tax depreciation class` memuat tombol `Restore default classes`
19. Tap `[⋯]` pada toolbar
20. Verifikasi bottom sheet `[⋯]` tampil
21. Verifikasi bottom sheet `[⋯]` tidak memuat `Restore default classes`
22. Tutup bottom sheet `[⋯]`
23. Pulihkan sembilan class Example Data

### TC-FA-TDC-671: Guided Tooltip tampil sebagai bottom sheet mini dengan swipe

24. Hapus flag `guided_tooltip_seen_fa-tax-depreciation-class` untuk akun Total Control
25. Buka tab `Tax Depreciation Class` (navigasi baru ke Settings > Accounting > Tax Depreciation Class)
26. Verifikasi walkthrough tampil sebagai bottom sheet mini dengan spotlight
27. Swipe kiri
28. Verifikasi Step 2 tampil
29. Swipe kanan
30. Verifikasi Step 1 tampil
31. Tutup walkthrough

### TC-FA-TDC-662: Tap toggle Disabled menampilkan alasan sebagai tooltip, bukan toast

32. Ganti akun: keluar dari akun Total Control
33. Login sebagai Read Only, lalu buka Settings > Accounting > Tax Depreciation Class
34. Tap toggle Active pada card NB-OLD
35. Verifikasi tooltip `You don't have permission to edit.` tampil
36. Verifikasi tidak ada toast
37. Verifikasi tooltip hilang otomatis
38. Verifikasi toggle NB-OLD tidak berubah (tetap Off)

### TC-FA-TDC-668: + Class tidak tampil bagi aktor tanpa Create

39. Verifikasi toolbar `[⋯]` dan `[🔍]` tampil
40. Verifikasi tombol `+ Class` tidak tampil (Hidden)

## Notes

- Urutan TC dalam spec: TC-FA-TDC-666, 667, 669, 670, 671, lalu TC-FA-TDC-662 dan TC-FA-TDC-668 pada akun Read Only di akhir dengan langkah ganti akun eksplisit (langkah 32 dan 33). TC-FA-TDC-670 menghapus seluruh class sehingga diletakkan sesudah TC yang membutuhkan card list, dan seed dipulihkan pada langkah 23 (S-10).
- Alasan lebih dari sekitar 35 langkah: satu kelas harness (aplikasi Android) dan satu layar; tiap blok TC berdiri sendiri (kegagalan satu blok tidak menghapus makna blok lain), dan 8 langkah di antaranya adalah pengaturan serta pemulihan state (langkah 16, 17, 23, 24, 25, 31, 32, dan 33) yang dibutuhkan precondition TC-FA-TDC-670, TC-FA-TDC-671, dan TC-FA-TDC-662.
- Asersi tambahan di luar Expected TC (S-03): langkah 20 dan 39 (anchor permukaan: bottom sheet `[⋯]` dan toolbar tampil sebelum asersi absence), langkah 35 sebagai anchor positif (tooltip sempat tampil) sebelum langkah 36 dan 37. Urutan 35, 36, 37 mengikuti 8b.5 dan 8b.11: tanpa toast diasersi selagi tooltip masih tampil, sebelum tooltip hilang otomatis, supaya asersi absence toast tidak lulus semu karena toast sudah hilang.
- Langkah penghubung (S-03): langkah 4, 9, 12, 15, 22, dan 31 (menutup bottom sheet, search bar, menu aksi baris, dan walkthrough), langkah 16, 17, 23, 24, dan 25 (mengatur state precondition), langkah 32 dan 33 (ganti akun).
- Temuan untuk QA:
  - Email akun Total Control dan Read Only tidak tertulis di TC.
  - TC-FA-TDC-671 tidak menyebut cara menutup walkthrough bottom sheet mini; spec menulis "Tutup walkthrough" tanpa mekanisme.
  - TC-FA-TDC-666 Expected b (bottom sheet Changelog) tidak menyebut isi yang diasersi; spec hanya mengasersi judul sehingga tidak membutuhkan data riwayat Changelog tertentu (tidak ada penimpaan riwayat lewat Fixture BE).
  - TC-FA-TDC-662 menyebut tooltip "hilang otomatis" tanpa durasi; spec mengasersi tooltip hilang tanpa batas waktu tertulis.
  - TC-FA-TDC-670 tidak menyebut cara mengatur tabel tanpa class; spec memakai seeding API suite.
  - Seluruh TC Android ditandai `Manual Only` karena framework web tidak dapat mengotomasi aplikasi native; spec tetap ditulis dengan `coverage.mobile: automated` untuk eksekusi di perangkat Android lewat TestSpectra mobile (kemampuan disediakan tim FE).
