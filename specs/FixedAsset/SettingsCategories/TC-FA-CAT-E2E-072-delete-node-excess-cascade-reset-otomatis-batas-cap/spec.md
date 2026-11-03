---
id: TC-FA-CAT-E2E-072-delete-node-excess-cascade-reset-otomatis-batas-cap
title: "Delete pada Node Excess: Cascade ke Descendant Excess, Reset Otomatis Excess saat Jumlah Mencapai Cap, dan Batas Cap"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-219
  - TC-FA-CAT-227
  - TC-FA-CAT-231
  - TC-FA-CAT-232
  - TC-FA-CAT-261
coverage:
  web: automated
---

# Delete pada Node Excess: Cascade ke Descendant Excess, Reset Otomatis Excess saat Jumlah Mencapai Cap, dan Batas Cap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatExcess (Pre-setup #31), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #31 (CatExcess, plan Starter, cap 5, T-0 sudah lewat, 9 kategori): usable `Electronics` (berisi `Laptop`, `Monitor`), `Office`, `Spare Parts` (berisi `Old Parts` Excess); Excess `Heavy Equipment`, `Vehicle`, `Furniture` (Total Asset 5), `Old Parts`. Varian 6 kategori untuk batas cap: `Electronics`, `Laptop`, `Monitor`, `Office`, `Spare Parts` usable dan `Furniture` Excess.
- Spec menghapus kategori Pre-setup #31 karena kondisi Excess bergantung pada jumlah seluruh kategori client sehingga tidak dapat dimiliki spec. Pemulihan ke 9 kategori (atau varian 6 kategori) lewat fixture backend yang disediakan tim FE/BE, dijalankan di hook `before`, hook `after`, dan sebagai langkah penghubung antar blok TC; efeknya (entri Changelog dan Last Updated) dicatat sebagai efek spec ini. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: membaca jumlah baris Changelog dengan Field dan Category Name tertentu sebelum dan sesudah aksi (baseline); disediakan tim FE/BE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-219: Cascade family delete ikut menghapus descendant Excess tanpa dialog tambahan

1. Klik elipsis (⋯) pada baris `Spare Parts` > `Delete`
2. Verifikasi dialog D-08 menghitung `Old Parts` dalam `1 subcategory`
3. Klik `[Delete]`
4. Verifikasi `Spare Parts` dan `Old Parts` terhapus dari tabel dan sidebar
5. Verifikasi tidak ada dialog atau pengecualian tambahan untuk node Excess
6. Pulihkan client CatExcess ke 9 kategori awal (fixture pemulihan) dan muat ulang halaman Categories

### TC-FA-CAT-227: Node Excess kosong dapat dihapus

7. Klik elipsis (⋯) pada baris `Vehicle` > `Delete`
8. Verifikasi dialog D-09 tampil
9. Klik `[Delete]`
10. Verifikasi toast `Success, category has been deleted.` tampil
11. Verifikasi `Vehicle` terhapus dari tabel
12. Pulihkan client CatExcess ke 9 kategori awal (fixture pemulihan) dan muat ulang halaman Categories

### TC-FA-CAT-231: Delete yang menurunkan jumlah kategori ke cap melepas seluruh Excess dalam transaksi yang sama

13. Catat baseline N1 jumlah baris Changelog `Restored from Excess (Category Consolidation)` untuk `Furniture`
14. Klik elipsis (⋯) pada baris `Heavy Equipment` > `Delete`, lalu klik `[Delete]` (jumlah menjadi 8)
15. Verifikasi `Furniture` tampil redup
16. Verifikasi row action `Edit` dan `+ Add Subcategory` pada `Furniture` Hidden
17. Klik elipsis (⋯) pada baris `Vehicle` > `Delete`, lalu klik `[Delete]` (jumlah menjadi 7)
18. Verifikasi `Furniture` tetap tampil redup
19. Verifikasi row action `Edit` dan `+ Add Subcategory` pada `Furniture` tetap Hidden
20. Klik elipsis (⋯) pada baris `Spare Parts` > `Delete`, lalu klik `[Delete]` (ikut menghapus `Old Parts`, jumlah menjadi 5)
21. Verifikasi `Furniture` tidak lagi redup (otomatis usable)
22. Verifikasi row action `Edit` dan `+ Add Subcategory` pada `Furniture` tampil
23. Verifikasi Alert Consolidation hilang
24. Buka Modal Changelog
25. Verifikasi Changelog bertambah tepat satu baris `Restored from Excess (Category Consolidation)` dengan Field `Excess`, Old `Excess`, New `Usable` untuk `Furniture` (N1 + 1)
26. Verifikasi Modified By baris itu adalah aktor Delete
27. Tutup Modal Changelog dan pulihkan client CatExcess ke varian 6 kategori (fixture pemulihan), lalu muat ulang halaman Categories

### TC-FA-CAT-232: Batas tepat cap, jumlah cap+1 tetap Excess dan jumlah sama dengan cap melepas Excess

28. Verifikasi `Furniture` tampil redup pada jumlah 6 (cap+1)
29. Verifikasi row action `Edit` dan `+ Add Subcategory` pada `Furniture` Hidden
30. Klik elipsis (⋯) pada baris `Office` > `Delete`
31. Klik `[Delete]` (jumlah menjadi 5)
32. Verifikasi `Furniture` usable kembali (tidak redup, `Edit` dan `+ Add Subcategory` tampil)
33. Pulihkan client CatExcess ke 9 kategori awal (fixture pemulihan) dan muat ulang halaman Categories

### TC-FA-CAT-261: Bulk Delete, reset otomatis Excess di dalam transaksi baris yang membuat jumlah mencapai cap

34. Catat baseline N2 jumlah baris Changelog `Restored from Excess (Category Consolidation)` untuk `Furniture`
35. Centang checkbox baris `Heavy Equipment`, `Vehicle`, `Office`, dan `Spare Parts`
36. Klik `[Delete]` pada Bulk Action Bar, lalu klik `[Delete]` pada dialog
37. Verifikasi `Heavy Equipment`, `Vehicle`, `Office`, `Spare Parts` dan `Old Parts` terhapus dengan jumlah akhir 4
38. Verifikasi `Furniture` usable kembali
39. Buka Modal Changelog
40. Verifikasi Changelog memuat baris Delete untuk tiap node yang dihapus
41. Verifikasi Changelog bertambah tepat satu baris `Restored from Excess (Category Consolidation)` untuk `Furniture` (N2 + 1) dengan Modified By aktor Bulk Delete
42. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (fungsional Delete pada node Excess), satu client, dan berdiri sendiri karena tiap blok dimulai dari state hasil pemulihan; 8 langkah di antaranya hanya pemulihan dan pencatatan baseline.
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): pemulihan client CatExcess antar blok, baseline Changelog, menutup Modal Changelog.
- Dua aksi Delete + `[Delete]` pada satu baris langkah ditulis sebagai satu aksi atomik per node (S-01 tidak terpengaruh karena tanpa Verifikasi di antaranya).
- Temuan untuk QA:
  - TC-FA-CAT-231 dan TC-FA-CAT-261 menyebut baris Changelog tanpa baseline; spec memakai selisih +1 terhadap baseline (S-12) karena pemulihan client dapat menghasilkan nama sama pada run berbeda.
  - Teks dialog D-09 tidak tertulis di TC-FA-CAT-227; spec hanya meng-assert dialog tampil.
