---
id: TC-FA-TDC-E2E-202-used-by-guard-deactivate-delete-lolos-dan-label-modal
title: "Used By: Guard Deactivate dan Delete Menjadi Lolos, dan Label Modal Mengikuti Class Name"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-746
  - TC-FA-TDC-747
  - TC-FA-TDC-748
sourceRules: ["D-02", "FATDC-LOGIC-08a", "§4.2c#r14", "D-01", "FATDC-LOGIC-08h", "D-05", "FATDC-LOGIC-09b", "F-FATDC-06.k2", "D-06", "D-04", "FATDC-LOGIC-09c", "§4.1.6#p1", "FATDC-LOGIC-11d.1"]
smoke: []
dependsOn: []
trace:
  "D-02": [3, 16]
  "FATDC-LOGIC-08a": 3
  "§4.2c#r14": 3
  "D-01": 15
  "FATDC-LOGIC-08h": [15, 16]
  "D-05": [21, 30]
  "FATDC-LOGIC-09b": 21
  "F-FATDC-06.k2": 21
  "D-06": 29
  "D-04": 30
  "FATDC-LOGIC-09c": 30
  "§4.1.6#p1": 37
  "FATDC-LOGIC-11d.1": 37
coverage:
  web: automated
---

# Used By: Guard Deactivate dan Delete Menjadi Lolos, dan Label Modal Mengikuti Class Name

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, kunci `exampleDataPlusNb3`, fixture belum ada): sembilan class Example Data PRD ditambah class seed NB-3, sehingga tabel berisi 10 baris dalam satu halaman (10 baris per halaman) dan baris target tidak dicari lewat Search. Kondisi yang dipakai: NB-4 (`Bukan bangunan – Kelompok 4`) Active, tanpa Last Posted Tax Year; NB-3 (`Bukan bangunan – Kelompok 3`) Active, Used By 0. Class Code dibatasi 15 karakter sehingga kode memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Data Asset Class (disediakan tim FE/BE lewat fixture BE): `AC-LAPTOP` (kunci `assetClassLaptop`) memakai NB-4 dengan Tax Method `Straight Line` (TC-746, 747, 748). Dibentuk dan dipulihkan lewat seeding di langkah penghubung blok (langkah 1, 18, 32) dan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class dan Asset Class pemakai lewat API, pemulihan data lewat API.
- State global yang diubah: Asset Class pemakai NB-4 dan NB-3 (AC-LAPTOP dipindah lalu dihapus), dan Class Name NB-4. Dipulihkan di hook `after` lewat seeding ulang data di atas.

## Test Steps

### TC-FA-TDC-746: Deactivate yang diblokir menjadi lolos saat Used By turun dari 1 ke 0

1. Seed `AC-LAPTOP` yang memakai NB-4 (Tax Method `Straight Line`, Active) lewat seeding API, lalu muat ulang halaman
2. Klik toggle `Active` baris NB-4
3. Verifikasi dialog blok "Cannot Deactivate Tax Depreciation Class" dengan kalimat "Used by 1 asset class. Change it in Asset Class first."
4. Klik `[OK]` pada dialog blok
5. Klik tab Asset Class
6. Ketik Search `AC-LAPTOP`, tekan Enter
7. Buka Drawer Edit Asset Class AC-LAPTOP
8. Klik dropdown Tax Depreciation Class
9. Pilih `Bukan bangunan – Kelompok 3 — 16 yrs`
10. Klik dropdown Tax Method
11. Pilih `Straight Line`
12. Klik `[Save]` hingga Asset Class berhasil tersimpan
13. Klik tab Tax Depreciation Class
14. Klik toggle `Active` baris NB-4
15. Verifikasi dialog konfirmasi "Deactivate Tax Depreciation Class" dengan bullet `• NB-4 – Bukan bangunan – Kelompok 4` dan tombol `[Deactivate]`
16. Verifikasi dialog blok "Cannot Deactivate Tax Depreciation Class" tidak tampil
17. Klik `[Cancel]` pada dialog konfirmasi

### TC-FA-TDC-747: Delete yang diblokir Guard 2 menjadi lolos saat Asset Class pemakai dihapus

18. Kembalikan AC-LAPTOP ke NB-4 (`Straight Line`, Active) lewat seeding API, lalu muat ulang halaman
19. Klik tombol `⋯` baris NB-4
20. Klik `Delete`
21. Verifikasi dialog blok "Cannot Delete Tax Depreciation Class" dengan kalimat "This class is used by 1 asset class."
22. Klik `[OK]` pada dialog blok
23. Klik tab Asset Class
24. Ganti isi kotak search dengan `AC-LAPTOP`, tekan Enter
25. Hapus Asset Class AC-LAPTOP dan konfirmasi hingga berhasil terhapus
26. Klik tab Tax Depreciation Class
27. Klik tombol `⋯` baris NB-4
28. Klik `Delete`
29. Verifikasi dialog konfirmasi "Delete Tax Depreciation Class" dengan tombol `[Delete]`
30. Verifikasi dialog blok "Cannot Delete Tax Depreciation Class" tidak tampil
31. Klik `[Cancel]` pada dialog konfirmasi

### TC-FA-TDC-748: Label class pada modal Used By mengikuti Class Name terbaru

32. Seed `AC-LAPTOP` yang memakai NB-4 (Tax Method `Straight Line`, Active) lewat seeding API, lalu muat ulang halaman
33. Klik Class Code NB-4
34. Ubah Class Name menjadi `Bukan bangunan – Kelompok 4 Revisi`
35. Klik `[Save]` hingga perubahan berhasil tersimpan
36. Klik angka Used By baris NB-4
37. Verifikasi modal "Used By" menampilkan satu baris teks polos `NB-4 – Bukan bangunan – Kelompok 4 Revisi` di bawah judul

## Notes

- Langkah penghubung (S-03): langkah 1, 18, 32 (seeding, tanpa asersi), langkah 5, 13, 23, 26 (berpindah tab), langkah 6 dan 24 (Search nama Asset Class untuk menemukan baris target, R-16), langkah 4 dan 22 (menutup dialog blok lewat `[OK]`), langkah 17 dan 31 (membatalkan dialog konfirmasi supaya NB-4 tidak berubah). Langkah 6 adalah Search pertama pada tab Asset Class ("Ketik Search"); Search, Filter, Sort, dan halaman dipertahankan sesudah muat ulang halaman (F5, 8b.9) dan nilai Search sebelumnya masih ada, sehingga langkah 24 menulis "ganti isi kotak search". Asumsi (8b.9, keputusan user 2026-11-04): kotak Search tab Asset Class mempertahankan nilainya lintas pindah tab (langkah 13, 23, 26) dan muat ulang halaman (langkah 18), jadi pada langkah 24 kotak itu masih berisi nilai langkah 6; perlu konfirmasi FE.
- Asersi tambahan di luar Expected TC (S-03): langkah 3 dan 21 adalah Expected a TC-746 dan TC-747; langkah 16 dan 30 memecah Expected b TC-746 dan TC-747 ("bukan dialog blok").
- Alasan di atas ~35 langkah (37 langkah, tanpa perulangan): satu topik (modal Used By dan guard Deactivate serta Delete terhadap Asset Class pemakai) dengan tiga blok TC. TC-746, TC-747, dan TC-748 masing-masing dibentuk ulang lewat seeding `AC-LAPTOP` pada langkah penghubung bernama (langkah 1, 18, dan 32), sehingga tidak ada blok yang memakai hasil aksi tulis blok sebelumnya. Yang menghubungkan blok hanya langkah penghubung itu dan pembatalan dialog (langkah 17 dan 31) yang menjaga NB-4 tidak berubah. Langkahnya panjang karena perubahan Asset Class lewat tab Asset Class dan kembali, serta satu `Verifikasi` per klausa (S-01).
- Pembagian TC lintas spec: TC-788, 789, dan 790 (versi dan pembatasan Allowed Methods terhadap Asset Class pemakai) ada di spec 256.
- Temuan untuk QA:
  - TC-746 dan 747 menulis "Confirm" atau tidak menyebut cara menutup dialog lolos setelah diasersi; spec membatalkannya lewat `[Cancel]` (langkah 17 dan 31) supaya NB-4 tidak berubah.
  - TC-746 sampai 748 tidak menyebut cara membuka Drawer Edit dan menghapus Asset Class; spec menulis "Buka Drawer Edit" dan "Hapus ... dan konfirmasi" tanpa label tombol, perlu dilengkapi dari PRD Asset Class.
  - TC-748 Expected menyebut modal "menampilkan satu baris teks polos" tanpa menyebut lokasi tepatnya selain "di bawah judul"; diikuti apa adanya.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang data di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Email akun Total Control tidak tertulis di TC.
