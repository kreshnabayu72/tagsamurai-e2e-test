---
id: TC-FA-CAT-E2E-088-wizard-aset-tidak-dipindahkan-submit-setelah-t0-dan-delete-sesi-lain
title: "Wizard Consolidation: Aset Tidak Dipindahkan, Submit Setelah T-0 Diterapkan Langsung, dan Submit Setelah Delete Sesi Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-312
  - TC-FA-CAT-304
  - TC-FA-CAT-302
coverage:
  web: automated
---

# Wizard Consolidation: Aset Tidak Dipindahkan, Submit Setelah T-0 Diterapkan Langsung, dan Submit Setelah Delete Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini pada client CatPostT0 (Pre-setup #33); halaman dibuka hook `beforeEach` suite. Langkah 7 berganti akun ke Total Control client CatExcess (Pre-setup #31); hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua untuk TC-FA-CAT-302: Total Control Kedua (Pre-setup #46, akun disediakan tim FE) lewat sesi API (butir hook suite di `suite.md`), hanya sebagai pemicu Delete; tidak ada sesi UI kedua.
- Data Pre-setup #33 (CatPostT0, plan Starter cap 5, T-0 sudah lewat, belum pernah submit selection): 8 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`.
- Data Pre-setup #31 (CatExcess, 9 kategori, cap 5): usable `Electronics` (anak `Laptop`, `Monitor`), `Office`, `Spare Parts` (anak `Old Parts`); Excess `Furniture`, `Heavy Equipment`, `Vehicle`, `Old Parts`. `Furniture` memuat 5 aset (Pre-setup #22).
- State yang diubah spec: seleksi CatPostT0 pada langkah 3, seleksi CatExcess pada langkah 13, dan penghapusan `Heavy Equipment`, `Vehicle`, `Spare Parts`, dan `Old Parts` pada langkah 23. Langkah 20 memulihkan Pre-setup #31 lewat fixture backend yang disediakan tim FE/BE; hook `after` memulihkan #33 dan #31. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Modal Changelog sebelum aksi (baseline, S-12).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-312: Submit setelah T-0 tetap diterima selama jumlah kategori melebihi cap dan langsung diterapkan

1. Klik `[Choose Categories]` pada Alert Category Consolidation
2. Centang `Keep usable` pada `Alpha Tech` dan `Beta Tools`
3. Klik `[Save Selection]`
4. Tunggu popup tertutup
5. Verifikasi `Alpha Tech` dan `Beta Tools` berstatus usable
6. Verifikasi `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` berstatus Excess

### TC-FA-CAT-304: Aset di kategori yang menjadi Excess tidak dipindahkan

7. Ganti akun: logout, lalu login sebagai Total Control client CatExcess (Pre-setup #31) dengan `Spectra.env.FA_TC_PASSWORD`
8. Klik `[Choose Categories]` pada Alert Category Consolidation
9. Buka Popup Detail `Furniture` sebelum Submit
10. Catat 5 aset pada tabel Assets `Furniture` dan Total Asset `Furniture`
11. Tutup Popup Detail
12. Centang `Keep usable` pada `Electronics`, `Laptop`, `Monitor`, `Office`, dan `Spare Parts`
13. Klik `[Save Selection]`
14. Tunggu popup tertutup
15. Buka Popup Detail `Furniture` lagi
16. Verifikasi `Furniture` berstatus Excess
17. Verifikasi tabel Assets `Furniture` tetap memuat 5 aset yang sama
18. Verifikasi Total Asset `Furniture` tidak berubah
19. Tutup Popup Detail

### TC-FA-CAT-302: Submit Wizard setelah Delete sesi lain menurunkan jumlah ke cap

20. Pulihkan Pre-setup #31 lewat fixture dan muat ulang halaman Categories
21. Klik `[Choose Categories]` pada Alert Category Consolidation
22. Centang `Keep usable` pada `Furniture`, `Electronics`, `Laptop`, `Monitor`, dan `Office`
23. Total Control Kedua (sesi API) menghapus `Heavy Equipment`, `Vehicle`, dan `Spare Parts` (beserta `Old Parts`) hingga tersimpan sehingga jumlah menjadi 5
24. Tunggu aksi selesai, lalu catat baseline N jumlah baris Changelog
25. Klik `[Save Selection]`
26. Verifikasi toast sukses `Success, category consolidation has been updated.` tampil
27. Verifikasi seluruh node tetap usable dan tidak ada node baru yang ditandai Excess (`Furniture` sudah dilepas oleh Delete sesi kedua)
28. Buka Modal Changelog
29. Verifikasi Changelog memuat tepat satu baris `Restored from Excess (Category Consolidation)` untuk `Furniture`
30. Verifikasi Modified By baris `Restored` itu adalah aktor Delete (Total Control Kedua), bukan aktor Total Control
31. Verifikasi jumlah baris Changelog sama dengan N (Submit tidak menulis baris Changelog apa pun, tidak ada baris `Restored` atau `Marked` atas nama aktor Total Control)
32. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah (32 langkah nominal). Alasan: seluruh blok satu kelas (fungsional Wizard Consolidation pasca-T-0) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-CAT-312 diletakkan pertama karena berjalan pada client CatPostT0 yang diwakili login hook `before`; TC-FA-CAT-304 dan TC-FA-CAT-302 berbagi client CatExcess dengan pemulihan di antaranya (S-09); TC-FA-CAT-302 yang menghapus data diletakkan terakhir (S-10).
- Pelaku kedua memakai sesi API sehingga bukan konteks UI kedua (konvensi bagian 3, P-2 butir 2026-10-30); tidak ada butir `P-2`.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 4, 14 (menunggu popup tertutup), 10 (mencatat aset), 11 dan 19 (menutup Popup Detail), 20 (pemulihan fixture), 24 (baseline), 32 (menutup Modal Changelog).
- Ketentuan baseline N pada langkah 24: dicatat sesudah Delete sesi kedua supaya baris Changelog akibat Delete tidak terhitung sebagai efek Submit (S-12).
- Asersi tidak adanya baris Changelog atas nama aktor Wizard pada langkah 31 ditulis sebagai asersi jumlah terhadap baseline (bukan kelas g); anchor positifnya langkah 29.
- Temuan untuk QA:
  - TC-FA-CAT-302 menyebut "5 kategori" yang dicentang tanpa nama; spec mencentang lima kategori yang masih ada setelah Delete (`Furniture`, `Electronics`, `Laptop`, `Monitor`, `Office`).
  - TC-FA-CAT-304 langkah 2 membuka Popup Detail `Furniture` saat popup Consolidation terbuka; spec membukanya dari popup Consolidation (letak aksi Detail pada popup tidak dijelaskan TC) dan sesudah Submit dari row action tabel.
  - TC-FA-CAT-302 kolom Expected b "seluruh node tetap usable" memuat `Furniture` yang menjadi usable oleh Delete sesi kedua; spec mengasersi bahwa tidak ada node Excess.
