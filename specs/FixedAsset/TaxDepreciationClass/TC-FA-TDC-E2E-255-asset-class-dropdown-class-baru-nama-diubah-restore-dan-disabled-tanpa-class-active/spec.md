---
id: TC-FA-TDC-E2E-255-asset-class-dropdown-class-baru-nama-diubah-restore-dan-disabled-tanpa-class-active
title: "Asset Class: Dropdown Tax Depreciation Class Mengikuti Class Baru, Nama Diubah, Restore, dan Disabled Tanpa Class Active"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-729
  - TC-FA-TDC-730
  - TC-FA-TDC-731
  - TC-FA-TDC-732
coverage:
  web: automated
---

# Asset Class: Dropdown Tax Depreciation Class Mengikuti Class Baru, Nama Diubah, Restore, dan Disabled Tanpa Class Active

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, kunci `seedClasses`, fixture belum ada): tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND), semuanya Active, Used By 0, tanpa Last Posted Tax Year, dan tidak ada class dengan Class Code `NB-5`. Tabel berisi 7 baris (kemudian 8 sesudah TC-729) dalam satu halaman (10 baris per halaman) sehingga baris target tidak dicari lewat Search. Class Code dibatasi 15 karakter sehingga kode memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Data uji TC-729: Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `NB-5`, Class Name `Kelompok 5 uji`, Asset Type `Non-building`, Useful Life `10`, Allowed Methods `Straight Line`.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class lewat API, mengosongkan tabel (seluruh class, tanpa Asset Class pemakai) lewat seeding API, dan memulihkan tujuh class seed; membuka Drawer Create Asset Class dan membaca opsi serta state Disabled dropdown.
- Suite berjalan serial (`parallel: false`). Jumlah N pada `Select All (N records)` (langkah 39) = 7, yaitu tujuh class seed yang dipulihkan lewat seeding API pada langkah 36 (8b.10).
- State global yang diubah: isi tabel Tax Depreciation Class (class NB-5 dibuat, Class Name NB-4 diubah, tabel dikosongkan lalu dipulihkan lewat Restore default classes, seluruh class dinonaktifkan). Dipulihkan di hook `after` lewat seeding ulang tujuh class seed; precondition TC-731 (tabel kosong) dan TC-732 (semua class Active, Used By 0) dibentuk sendiri lewat seeding API di langkah 26 dan 36, tidak memakai hasil TC sebelumnya.

## Test Steps

### TC-FA-TDC-729: Class baru muncul di dropdown

1. Klik `+ Class`
2. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
3. Isi Class Code `NB-5`
4. Isi Class Name `Kelompok 5 uji`
5. Pilih Asset Type `Non-building`
6. Isi Useful Life `10`
7. Pilih Allowed Methods `Straight Line`
8. Klik `[Submit]` hingga class NB-5 berhasil tersimpan
9. Klik tab Asset Class
10. Klik `+ Asset Class`
11. Klik dropdown Tax Depreciation Class
12. Verifikasi opsi `Kelompok 5 uji — 10 yrs` tampil di dropdown
13. Tekan Esc untuk menutup dropdown
14. Klik `[×]` pada header Drawer Create Asset Class

### TC-FA-TDC-730: Class Name yang diubah tercermin di dropdown

15. Klik tab Tax Depreciation Class
16. Klik Class Code NB-4
17. Ubah Class Name menjadi `Bukan bangunan – Kelompok 4 Revisi`
18. Klik `[Save]` hingga perubahan berhasil tersimpan
19. Klik tab Asset Class
20. Klik `+ Asset Class`
21. Klik dropdown Tax Depreciation Class
22. Verifikasi opsi `Bukan bangunan – Kelompok 4 Revisi — 20 yrs` tampil di dropdown
23. Verifikasi opsi `Bukan bangunan – Kelompok 4 — 20 yrs` tidak tampil di dropdown
24. Tekan Esc untuk menutup dropdown
25. Klik `[×]` pada header Drawer Create Asset Class

### TC-FA-TDC-731: Class hasil Restore default classes muncul di dropdown

26. Kosongkan tabel Tax Depreciation Class (tanpa class, semua status, tanpa Asset Class pemakai) lewat seeding API
27. Klik tab Tax Depreciation Class
28. Klik `Restore default classes` di Empty State
29. Klik `[Restore]` pada dialog hingga class default berhasil tersimpan
30. Klik tab Asset Class
31. Klik `+ Asset Class`
32. Klik dropdown Tax Depreciation Class
33. Verifikasi dropdown memuat opsi `Bukan bangunan – Kelompok 1 — 4 yrs`, `Bukan bangunan – Kelompok 2 — 8 yrs`, `Bukan bangunan – Kelompok 3 — 16 yrs`, `Bukan bangunan – Kelompok 4 — 20 yrs`, `Bangunan permanen — 20 yrs`, `Bangunan tidak permanen — 10 yrs`, dan satu opsi untuk class Tanah
34. Tekan Esc untuk menutup dropdown
35. Klik `[×]` pada header Drawer Create Asset Class

### TC-FA-TDC-732: Dropdown Disabled bila tidak ada class Active

36. Pulihkan tujuh class seed (semua Active, Used By 0, tanpa Last Posted Tax Year) lewat seeding API
37. Klik tab Tax Depreciation Class
38. Centang checkbox header tabel
39. Klik `Select All (N records)`
40. Klik `Deactivate` pada Bulk Action Bar
41. Klik `[Deactivate]` pada dialog konfirmasi hingga seluruh class berhasil dinonaktifkan
42. Klik tab Asset Class
43. Klik `+ Asset Class`
44. Verifikasi dropdown Tax Depreciation Class pada Drawer Create Asset Class tampil Disabled
45. Klik dropdown Tax Depreciation Class
46. Verifikasi dropdown Tax Depreciation Class tidak terbuka
47. Klik `[×]` pada header Drawer Create Asset Class

## Notes

- Pembagian TC lintas spec: TC-725 sampai TC-728 ada di spec 199.
- Langkah penghubung (S-03): langkah 13, 14, 24, 25, 34, 35, 47 (menutup dropdown lalu Drawer; form tidak diubah sehingga dialog `Unsaved Changes` tidak muncul), langkah 26 (mengosongkan tabel lewat seeding API; precondition TC-731, tidak diasersi), langkah 36 (memulihkan tujuh class seed Active lewat seeding API; precondition TC-732 tidak bergantung pada hasil Restore TC-731, tidak diasersi), langkah 38 (mencentang checkbox header supaya `Select All (N records)` tersedia), dan langkah berpindah tab 9, 15, 19, 27, 30, 37, 42.
- Urutan TC di spec: 729, 730, 731, 732. TC-731 mensyaratkan tabel kosong (langkah 26) dan TC-732 mensyaratkan seluruh class Active, Used By 0 (langkah 36); keduanya dibentuk lewat seeding API sehingga tiap blok berdiri sendiri.
- Asersi tambahan di luar Expected TC (S-03): langkah 44 dan 46 memecah Expected TC-732 ("Disabled dan tidak dapat dibuka") menjadi dua `Verifikasi` (S-01); langkah 45 adalah aksi yang membuktikan dropdown tidak terbuka.
- Alasan di atas ~35 langkah: semua blok satu topik (isi dropdown Tax Depreciation Class di Drawer Create Asset Class), tiap blok berdiri sendiri dengan kondisi data yang dibentuk sendiri (seeding API pada langkah 26 dan 36 untuk TC-731 dan TC-732) dan dinyatakan di Prerequisites, dan langkah panjangnya (47 langkah) adalah navigasi berulang antar tab (buka Asset Class, `+ Asset Class`, dropdown, tutup); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-729 mensyaratkan "tidak ada class dengan Class Code NB-5" dan mengisi form tanpa label field Asset Type dan Allowed Methods sebagai kontrol (dropdown atau checkbox); spec memakai kata "Pilih".
  - TC-731 Expected tidak menyebut label opsi class Tanah; spec menyebutnya "satu opsi untuk class Tanah" sesuai TC (label menurut TC-737 adalah `Tanah`).
  - TC-731 precondition tabel kosong tidak menyebut cara membuatnya; spec memakai seeding API (S-13, tanpa endpoint karangan).
  - TC-729, 730, 731, 732 menulis "Confirm" tanpa label tombol; spec memakai `[Restore]` dan `[Deactivate]` menurut D-12 dan D-01 PRD.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang data di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Email akun Total Control tidak tertulis di TC.
