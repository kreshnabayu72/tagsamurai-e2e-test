---
id: TC-FA-TDC-E2E-202-used-by-penanda-warning-guard-deactivate-delete-lolos-dan-label-modal
title: "Used By: Penanda Warning Hilang, Guard Deactivate dan Delete Menjadi Lolos, dan Label Modal Mengikuti Class Name"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-745
  - TC-FA-TDC-746
  - TC-FA-TDC-747
  - TC-FA-TDC-748
sourceRules: ["FATDC-LOGIC-11d.5", "§4.1.6#r1", "F-FATDC-10.k5", "FATDC-LOGIC-10d", "S-11c", "D-02", "FATDC-LOGIC-08a", "§4.2c#r14", "D-01", "FATDC-LOGIC-08h", "D-05", "FATDC-LOGIC-09b", "F-FATDC-06.k2", "D-06", "D-04", "FATDC-LOGIC-09c", "§4.1.6#p1", "FATDC-LOGIC-11d.1"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-11d.5": 2
  "§4.1.6#r1": 2
  "F-FATDC-10.k5": 2
  "FATDC-LOGIC-10d": 12
  "S-11c": 12
  "D-02": [16, 29]
  "FATDC-LOGIC-08a": 16
  "§4.2c#r14": 16
  "D-01": 28
  "FATDC-LOGIC-08h": [28, 29]
  "D-05": [34, 43]
  "FATDC-LOGIC-09b": 34
  "F-FATDC-06.k2": 34
  "D-06": 42
  "D-04": 43
  "FATDC-LOGIC-09c": 43
  "§4.1.6#p1": 50
  "FATDC-LOGIC-11d.1": 50
coverage:
  web: automated
---

# Used By: Penanda Warning Hilang, Guard Deactivate dan Delete Menjadi Lolos, dan Label Modal Mengikuti Class Name

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, kunci `exampleDataPlusNb3`, fixture belum ada): sembilan class Example Data PRD ditambah class seed NB-3, sehingga tabel berisi 10 baris dalam satu halaman (10 baris per halaman) dan baris target tidak dicari lewat Search. Kondisi yang dipakai: NB-SL (`Kelompok khusus Straight Line`) hanya mengizinkan Straight Line; NB-4 (`Bukan bangunan – Kelompok 4`) Active, tanpa Last Posted Tax Year; NB-3 (`Bukan bangunan – Kelompok 3`) Active, Used By 0. Class Code dibatasi 15 karakter sehingga kode memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Data Asset Class (disediakan tim FE/BE lewat fixture BE): `AC-MESIN` (kunci `assetClassMesin`) memakai NB-SL dengan Tax Method `Declining Balance` sehingga barisnya bertanda ikon ⚠ di modal "Used By" NB-SL (TC-745); `AC-LAPTOP` (kunci `assetClassLaptop`) memakai NB-4 dengan Tax Method `Straight Line` (TC-746, 747, 748). Dibentuk dan dipulihkan lewat seeding di langkah penghubung blok (langkah 14, 31, 45) dan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class dan Asset Class pemakai lewat API (termasuk Tax Method yang tidak diizinkan class), pemulihan data lewat API.
- State global yang diubah: Tax Method AC-MESIN, Asset Class pemakai NB-4 dan NB-3 (AC-LAPTOP dipindah lalu dihapus), dan Class Name NB-4. Dipulihkan di hook `after` lewat seeding ulang data di atas.

## Test Steps

### TC-FA-TDC-745: Penanda peringatan hilang setelah Tax Method diganti ke metode yang diizinkan

1. Klik angka Used By baris NB-SL
2. Verifikasi baris AC-MESIN pada modal "Used By" tampil dengan ikon ⚠
3. Tutup modal "Used By" lewat `[×]` pada header modal
4. Klik tab Asset Class
5. Ketik Search `AC-MESIN`, tekan Enter
6. Buka Drawer Edit Asset Class AC-MESIN
7. Klik dropdown Tax Method
8. Pilih `Straight Line`
9. Klik `[Save]` hingga Asset Class berhasil tersimpan
10. Klik tab Tax Depreciation Class
11. Klik angka Used By baris NB-SL
12. Verifikasi baris AC-MESIN tampil tanpa ikon ⚠
13. Tutup modal "Used By" lewat `[×]` pada header modal

### TC-FA-TDC-746: Deactivate yang diblokir menjadi lolos saat Used By turun dari 1 ke 0

14. Seed `AC-LAPTOP` yang memakai NB-4 (Tax Method `Straight Line`, Active) lewat seeding API, lalu muat ulang halaman
15. Klik toggle `Active` baris NB-4
16. Verifikasi dialog blok "Cannot Deactivate Tax Depreciation Class" dengan kalimat "Used by 1 asset class. Change it in Asset Class first."
17. Klik `[OK]` pada dialog blok
18. Klik tab Asset Class
19. Ganti isi kotak search dengan `AC-LAPTOP`, tekan Enter
20. Buka Drawer Edit Asset Class AC-LAPTOP
21. Klik dropdown Tax Depreciation Class
22. Pilih `Bukan bangunan – Kelompok 3 — 16 yrs`
23. Klik dropdown Tax Method
24. Pilih `Straight Line`
25. Klik `[Save]` hingga Asset Class berhasil tersimpan
26. Klik tab Tax Depreciation Class
27. Klik toggle `Active` baris NB-4
28. Verifikasi dialog konfirmasi "Deactivate Tax Depreciation Class" dengan bullet `• NB-4 – Bukan bangunan – Kelompok 4` dan tombol `[Deactivate]`
29. Verifikasi dialog blok "Cannot Deactivate Tax Depreciation Class" tidak tampil
30. Klik `[Cancel]` pada dialog konfirmasi

### TC-FA-TDC-747: Delete yang diblokir Guard 2 menjadi lolos saat Asset Class pemakai dihapus

31. Kembalikan AC-LAPTOP ke NB-4 (`Straight Line`, Active) lewat seeding API, lalu muat ulang halaman
32. Klik tombol `⋯` baris NB-4
33. Klik `Delete`
34. Verifikasi dialog blok "Cannot Delete Tax Depreciation Class" dengan kalimat "This class is used by 1 asset class."
35. Klik `[OK]` pada dialog blok
36. Klik tab Asset Class
37. Ganti isi kotak search dengan `AC-LAPTOP`, tekan Enter
38. Hapus Asset Class AC-LAPTOP dan konfirmasi hingga berhasil terhapus
39. Klik tab Tax Depreciation Class
40. Klik tombol `⋯` baris NB-4
41. Klik `Delete`
42. Verifikasi dialog konfirmasi "Delete Tax Depreciation Class" dengan tombol `[Delete]`
43. Verifikasi dialog blok "Cannot Delete Tax Depreciation Class" tidak tampil
44. Klik `[Cancel]` pada dialog konfirmasi

### TC-FA-TDC-748: Label class pada modal Used By mengikuti Class Name terbaru

45. Seed `AC-LAPTOP` yang memakai NB-4 (Tax Method `Straight Line`, Active) lewat seeding API, lalu muat ulang halaman
46. Klik Class Code NB-4
47. Ubah Class Name menjadi `Bukan bangunan – Kelompok 4 Revisi`
48. Klik `[Save]` hingga perubahan berhasil tersimpan
49. Klik angka Used By baris NB-4
50. Verifikasi modal "Used By" menampilkan satu baris teks polos `NB-4 – Bukan bangunan – Kelompok 4 Revisi` di bawah judul

## Notes

- Langkah penghubung (S-03): langkah 3, 13 (menutup modal), langkah 14, 31, 45 (seeding, tanpa asersi), langkah 4, 10, 18, 26, 36, 39 (berpindah tab), langkah 5, 19, 37 (Search nama Asset Class untuk menemukan baris target, R-16), langkah 17 dan 35 (menutup dialog blok lewat `[OK]`), langkah 30 dan 44 (membatalkan dialog konfirmasi supaya NB-4 tidak berubah). Langkah 5 adalah Search pertama pada tab Asset Class ("Ketik Search"); Search, Filter, Sort, dan halaman dipertahankan sesudah muat ulang halaman (F5, 8b.9) dan nilai Search sebelumnya masih ada, sehingga langkah 19 dan 37 menulis "ganti isi kotak search". Asumsi (8b.9, keputusan user 2026-11-04): kotak Search tab Asset Class mempertahankan nilainya lintas pindah tab (langkah 10, 18, 26, 36, 39) dan muat ulang halaman (langkah 14, 31), jadi pada langkah 19 kotak itu masih berisi `AC-MESIN` dan pada langkah 37 berisi nilai langkah 19; perlu konfirmasi FE.
- Asersi tambahan di luar Expected TC (S-03): langkah 2 (baris AC-MESIN bertanda ⚠ sebelum Tax Method diganti) adalah anchor positif supaya langkah 12 ("tanpa ikon ⚠") tidak lulus semu (8b.2); langkah 16 dan 34 adalah Expected a TC-746 dan TC-747; langkah 29 dan 43 memecah Expected b TC-746 dan TC-747 ("bukan dialog blok").
- Alasan di atas ~35 langkah (50 langkah, tanpa perulangan): satu topik (modal Used By dan guard Deactivate serta Delete terhadap Asset Class pemakai) dengan empat blok TC. TC-745 memakai data awal `AC-MESIN`; TC-746, TC-747, dan TC-748 masing-masing dibentuk ulang lewat seeding `AC-LAPTOP` pada langkah penghubung bernama (langkah 14, 31, dan 45), sehingga tidak ada blok yang memakai hasil aksi tulis blok sebelumnya. Yang menghubungkan blok hanya langkah penghubung itu dan pembatalan dialog (langkah 30 dan 44) yang menjaga NB-4 tidak berubah. Langkahnya panjang karena perubahan Asset Class lewat tab Asset Class dan kembali, serta satu `Verifikasi` per klausa (S-01).
- Pembagian TC lintas spec: TC-788, 789, dan 790 (versi dan pembatasan Allowed Methods terhadap Asset Class pemakai) ada di spec 256.
- Temuan untuk QA:
  - TC-745 Expected hanya menyebut "tanpa ikon ⚠" tanpa kondisi awal bertanda ⚠ di langkah TC; spec menambah asersi awal (langkah 2).
  - TC-746 dan 747 menulis "Confirm" atau tidak menyebut cara menutup dialog lolos setelah diasersi; spec membatalkannya lewat `[Cancel]` (langkah 30 dan 44) supaya NB-4 tidak berubah.
  - TC-745 sampai 748 tidak menyebut cara membuka Drawer Edit dan menghapus Asset Class; spec menulis "Buka Drawer Edit" dan "Hapus ... dan konfirmasi" tanpa label tombol, perlu dilengkapi dari PRD Asset Class.
  - TC-748 Expected menyebut modal "menampilkan satu baris teks polos" tanpa menyebut lokasi tepatnya selain "di bawah judul"; diikuti apa adanya.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang data di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Email akun Total Control tidak tertulis di TC.
