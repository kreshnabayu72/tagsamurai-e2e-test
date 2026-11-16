---
id: TC-FA-TDC-E2E-199-asset-class-dropdown-hanya-class-active-serta-aktivasi-deaktivasi-dan-penghapusan-class
title: "Asset Class: Dropdown Tax Depreciation Class Hanya Memuat Class Active dan Mengikuti Aktivasi, Deaktivasi, dan Penghapusan"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-725
  - TC-FA-TDC-726
  - TC-FA-TDC-727
  - TC-FA-TDC-728
sourceRules: ["§11.1#r1", "FATDC-LOGIC-08b", "§4.1.1#r24", "S-05a", "§4.1.5#r3", "S-06a", "S-07b"]
smoke: []
dependsOn: []
trace:
  "§11.1#r1": [4, 6]
  "FATDC-LOGIC-08b": [5, 6]
  "§4.1.1#r24": 5
  "S-05a": 15
  "§4.1.5#r3": [24, 36]
  "S-06a": 25
  "S-07b": 37
coverage:
  web: automated
---

# Asset Class: Dropdown Tax Depreciation Class Hanya Memuat Class Active dan Mengikuti Aktivasi, Deaktivasi, dan Penghapusan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, kunci `exampleDataPlusNb3`, fixture belum ada): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) ditambah class seed NB-3 (`Bukan bangunan – Kelompok 3`, Useful Life 16), sehingga tabel Tax Depreciation Class berisi 10 baris dalam satu halaman (10 baris per halaman) dan baris target tidak dicari lewat Search. Kondisi yang dipakai langkah: NB-4 (`Bukan bangunan – Kelompok 4`, Useful Life 20) Active, Used By 0, tanpa Last Posted Tax Year; NB-OLD (`Kelompok khusus lama`, Useful Life 5) Inactive, Used By 0; NB-3 Active, Used By 0. Class Code dibatasi 15 karakter sehingga kode memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class lewat API dan pemulihannya (termasuk mengembalikan NB-4 menjadi Active, Used By 0); membuka Drawer Create Asset Class dan membaca opsi dropdown; menutup dropdown dengan `Esc`.
- State global yang diubah: status Active NB-OLD dan NB-4, serta penghapusan NB-4 (data seed spec). Dipulihkan di hook `after` lewat seeding ulang kondisi data di atas.

## Test Steps

### TC-FA-TDC-725: Dropdown hanya memuat class Active

1. Klik tab Asset Class
2. Klik `+ Asset Class`
3. Klik dropdown Tax Depreciation Class
4. Verifikasi opsi `Bukan bangunan – Kelompok 4 — 20 yrs` tampil di dropdown
5. Verifikasi opsi untuk NB-OLD (`Kelompok khusus lama`) tidak tampil di dropdown
6. Verifikasi setiap opsi yang tampil adalah class berstatus Active
7. Tekan Esc untuk menutup dropdown
8. Klik `[×]` pada header Drawer Create Asset Class

### TC-FA-TDC-727: Class yang diaktifkan muncul di dropdown

9. Klik tab Tax Depreciation Class
10. Klik toggle `Active` baris NB-OLD
11. Klik `[Activate]` pada dialog konfirmasi `Activate Tax Depreciation Class` hingga status NB-OLD berhasil tersimpan
12. Klik tab Asset Class
13. Klik `+ Asset Class`
14. Klik dropdown Tax Depreciation Class
15. Verifikasi opsi `Kelompok khusus lama — 5 yrs` tampil di dropdown
16. Tekan Esc untuk menutup dropdown
17. Klik `[×]` pada header Drawer Create Asset Class

### TC-FA-TDC-726: Class yang dinonaktifkan hilang dari dropdown

18. Klik tab Tax Depreciation Class
19. Klik toggle `Active` baris NB-4
20. Klik `[Deactivate]` pada dialog konfirmasi `Deactivate Tax Depreciation Class` hingga status NB-4 berhasil tersimpan
21. Klik tab Asset Class
22. Klik `+ Asset Class`
23. Klik dropdown Tax Depreciation Class
24. Verifikasi opsi `Bukan bangunan – Kelompok 3 — 16 yrs` masih tampil
25. Verifikasi opsi `Bukan bangunan – Kelompok 4 — 20 yrs` tidak tampil
26. Tekan Esc untuk menutup dropdown
27. Klik `[×]` pada header Drawer Create Asset Class

### TC-FA-TDC-728: Class yang dihapus hilang dari dropdown

28. Pulihkan NB-4 menjadi Active, Used By 0, tanpa Last Posted Tax Year lewat seeding API
29. Klik tab Tax Depreciation Class
30. Klik tombol `⋯` baris NB-4
31. Klik `Delete`
32. Klik `[Delete]` pada dialog konfirmasi `Delete Tax Depreciation Class` hingga NB-4 berhasil terhapus
33. Klik tab Asset Class
34. Klik `+ Asset Class`
35. Klik dropdown Tax Depreciation Class
36. Verifikasi opsi `Bukan bangunan – Kelompok 3 — 16 yrs` tampil
37. Verifikasi opsi `Bukan bangunan – Kelompok 4 — 20 yrs` tidak tampil
38. Tekan Esc untuk menutup dropdown
39. Klik `[×]` pada header Drawer Create Asset Class

## Notes

- Urutan TC di spec: 725, 727, 726, 728. TC-725 mensyaratkan NB-OLD Inactive sehingga mendahului TC-727 (mengaktifkannya); TC-728 mensyaratkan NB-4 Active sehingga mengikuti TC-726 (menonaktifkannya) dengan langkah pemulihan 28. Pembagian TC lintas spec: TC-729 sampai TC-732 ada di spec 255.
- Langkah penghubung (S-03): langkah 7, 8, 16, 17, 26, 27, 38, 39 (menutup dropdown lalu Drawer; form tidak diubah sehingga dialog `Unsaved Changes` tidak muncul), langkah 28 (pemulihan seed NB-4 lewat API, tidak diasersi), dan langkah 9, 12, 18, 21, 29, 33 (berpindah tab).
- Asersi tambahan di luar Expected TC (S-03): langkah 24 dan 36 (opsi NB-3 tampil) adalah Expected b TC-726 yang dipakai di TC-726 dan TC-728 sebagai anchor positif untuk asersi opsi NB-4 tidak tampil (8b.2), sehingga langkah 24 mendahului langkah 25. Pada TC-728 TC tidak memuat opsi pembanding; langkah 36 ditambahkan sebagai anchor.
- Alasan di atas ~35 langkah: semua blok satu topik (isi dropdown Tax Depreciation Class di Drawer Create Asset Class), tiap blok berdiri sendiri dengan kondisi data yang dinyatakan di Prerequisites, dan langkah panjangnya adalah navigasi berulang antar tab (buka Asset Class, `+ Asset Class`, dropdown, tutup); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-726, 727, 728 menulis "Confirm" tanpa label tombol; spec memakai `[Deactivate]`, `[Activate]`, dan `[Delete]` menurut D-01, D-03, dan D-06 PRD.
  - TC-725 menulis precondition NB-4 dan NB-OLD tanpa menyebut data class Example Data lain; spec memakai sembilan Example Data ditambah NB-3 (kebutuhan TC-726).
  - TC-728 tidak menyebut status Active NB-4 pada precondition; spec memakai NB-4 Active (langkah 28) supaya opsi sempat tampil sebelum dihapus.
  - TC-725 Expected c ("setiap opsi yang tampil adalah class berstatus Active") tidak menyebut cara membuktikan status tiap opsi; spec membandingkan opsi dengan daftar class Active hasil seeding.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Email akun Total Control tidak tertulis di TC.
