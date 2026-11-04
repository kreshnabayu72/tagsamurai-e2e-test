---
id: TC-FA-TDC-E2E-256-versi-baru-current-scheduled-dan-allowed-methods-dipersempit-pada-asset-class-pemakai
title: "Asset Class Pemakai: Versi Current dan Scheduled Memengaruhi Useful Life dan Rate, serta Allowed Methods Dipersempit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-788
  - TC-FA-TDC-789
  - TC-FA-TDC-790
coverage:
  web: automated
---

# Asset Class Pemakai: Versi Current dan Scheduled Memengaruhi Useful Life dan Rate, serta Allowed Methods Dipersempit

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta) dengan Fiscal Year Start Januari; jam server dan jam browser diatur bersama lewat kendali jam (`suite.md`) di hook `before` dan dipulihkan di hook `after`.
- Data Pre-setup (disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, kunci `exampleDataPlusNb3`, fixture belum ada): sembilan class Example Data PRD ditambah class seed NB-3, sehingga tabel berisi 10 baris dalam satu halaman (10 baris per halaman) dan baris target tidak dicari lewat Search. Kondisi yang dipakai: NB-4 (`Bukan bangunan – Kelompok 4`) versi Current Useful Life 20 (Straight Line Rate 5%, Declining Balance Rate 10%) tanpa versi Scheduled; NB-2 (`Bukan bangunan – Kelompok 2`) mengizinkan Straight Line dan Declining Balance. Class Code dibatasi 15 karakter sehingga kode memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Data Asset Class (disediakan tim FE/BE lewat fixture BE): `AC-LAPTOP` (kunci `assetClassLaptop`) memakai NB-4 dengan Tax Method `Straight Line` (TC-788, 789); `AC-MESIN` (kunci `assetClassMesin`) memakai NB-2 dengan Tax Method `Declining Balance` (TC-790). Dibentuk dan dipulihkan lewat seeding di langkah penghubung blok (langkah 11) dan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class, versi, dan Asset Class pemakai lewat API; pemulihan data lewat API.
- State global yang diubah: jam server dan browser (hook `before`, dipulihkan di `after`), versi NB-4 (Current dan Scheduled), Allowed Methods tidak berubah (Drawer ditutup dengan `[Leave]`), dan Tax Method AC-MESIN. Dipulihkan di hook `after` lewat seeding ulang data di atas.

## Test Steps

### TC-FA-TDC-789: Versi Scheduled belum memengaruhi Useful Life dan rate di Asset Class pemakai

1. Klik Class Code NB-4
2. Ubah Useful Life menjadi `10`
3. Klik `[Save]`
4. Pilih Effective From `Jan 2027`
5. Klik `[Apply]` hingga versi berhasil tersimpan
6. Klik tab Asset Class
7. Ketik Search `AC-LAPTOP`, tekan Enter
8. Buka Drawer Edit Asset Class AC-LAPTOP
9. Verifikasi Useful Life & Rate pada AC-LAPTOP tampil Useful Life 20, Straight Line Rate 5%, dan Declining Balance Rate 10%
10. Klik `[×]` pada header Drawer Edit Asset Class

### TC-FA-TDC-788: Versi baru yang langsung Current tercermin di Asset Class pemakai

11. Pulihkan NB-4 ke versi Current Useful Life 20 tanpa versi Scheduled lewat seeding API (AC-LAPTOP tetap memakai NB-4), lalu muat ulang halaman
12. Klik tab Tax Depreciation Class
13. Klik Class Code NB-4
14. Ubah Useful Life menjadi `10`
15. Klik `[Save]`
16. Pilih Effective From `Jan 2026`
17. Klik `[Apply]` hingga versi berhasil tersimpan
18. Klik tab Asset Class
19. Ganti isi kotak search dengan `AC-LAPTOP`, tekan Enter
20. Buka Drawer Edit Asset Class AC-LAPTOP
21. Verifikasi Useful Life & Rate pada AC-LAPTOP tampil Useful Life 10, Straight Line Rate 10%, dan Declining Balance Rate 20%
22. Klik `[×]` pada header Drawer Edit Asset Class

### TC-FA-TDC-790: Mempersempit Allowed Methods diizinkan setelah Asset Class mengganti Tax Method

23. Ganti isi kotak search dengan `AC-MESIN`, tekan Enter
24. Buka Drawer Edit Asset Class AC-MESIN
25. Klik dropdown Tax Method
26. Pilih `Straight Line`
27. Klik `[Save]` hingga Asset Class berhasil tersimpan
28. Klik tab Tax Depreciation Class
29. Klik Class Code NB-2
30. Hapus pilihan `Declining Balance` di Allowed Methods
31. Klik `[Save]`
32. Verifikasi dialog Save Changes dengan field Effective From tampil
33. Verifikasi dialog "Cannot Remove This Method" tidak tampil
34. Klik `[Cancel]` pada dialog Save Changes
35. Klik `[×]` pada header Drawer Edit
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik `[Leave]`

## Notes

- Urutan TC di spec: 789, 788, 790. TC-789 membuat versi Scheduled pada NB-4 dengan Useful Life Current 20; TC-788 mensyaratkan NB-4 tanpa versi Scheduled sehingga didahului pemulihan seeding (langkah 11) yang menggantikan versi hasil TC-789.
- Langkah penghubung (S-03): langkah 6, 12, 18, 28 (berpindah tab), langkah 7 dan 19 dan 23 (Search AC-LAPTOP atau AC-MESIN untuk menemukan baris target, R-16; kotak Search berisi nilai sebelumnya sehingga langkah 19 dan 23 menggantinya, 8b.9), langkah 10 dan 22 (menutup Drawer yang tidak diubah, tanpa dialog `Unsaved Changes`), langkah 11 (seeding, tanpa asersi), langkah 34 (membatalkan dialog Save Changes), dan langkah 35 sampai 37 (menutup Drawer dirty lewat `[×]` dan `[Leave]`, S-08).
- Asersi tambahan di luar Expected TC (S-03): langkah 33 memecah Expected TC-790 ("Save Changes tampil dan dialog Cannot Remove This Method tidak tampil") menjadi dua `Verifikasi` (S-01), dengan langkah 32 sebagai anchor positif (8b.2).
- Pembagian TC lintas spec: TC-745 sampai 748 (Used By) ada di spec 202.
- Alasan di atas ~35 langkah: sedikit melewati ~35 langkah; tiga blok satu topik (pengaruh versi dan Allowed Methods terhadap Asset Class pemakai), tiap blok berdiri sendiri dengan seeding ulang di langkah penghubung, dan langkah panjangnya adalah perubahan di tab Tax Depreciation Class lalu pembacaan di tab Asset Class; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-788 Expected menyebut Declining Balance Rate 20% dan Straight Line Rate 10% tanpa menyebut asal perhitungannya; nilai diikuti apa adanya (Useful Life 10, rate dihitung server).
  - TC-790 tidak menyebut cara menutup dialog Save Changes dan Drawer sesudah asersi; spec membatalkan dialog dan menutup Drawer dengan `[Leave]` supaya NB-2 tidak berubah.
  - TC-788 sampai 790 tidak menyebut cara membuka Drawer Edit Asset Class; spec menulis "Buka Drawer Edit" tanpa label tombol, perlu dilengkapi dari PRD Asset Class.
  - TC-790 mensyaratkan AC-MESIN memakai NB-2 dengan Declining Balance tanpa menyebut cara menyiapkannya; spec memakai seeding fixture BE.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang data di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Email akun Total Control tidak tertulis di TC.
