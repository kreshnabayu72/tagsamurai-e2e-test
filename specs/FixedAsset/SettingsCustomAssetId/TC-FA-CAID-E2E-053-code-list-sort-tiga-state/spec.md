---
id: TC-FA-CAID-E2E-053-code-list-sort-tiga-state
title: "Modal View Code List: Sort 3-State per Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-128
  - TC-FA-CAID-129
  - TC-FA-CAID-130
coverage:
  web: automated
---

# Modal View Code List: Sort 3-State per Kolom

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE). Spec hanya membaca. Kolom yang di-sort memuat sedikitnya dua nilai distinct (dataset memuat enam Group, empat Category, tiga Asset Name, tiga Division, dan dua Account).
- Data Dinamis: tidak ada. State global: tidak ada yang diubah.

## Test Steps

### TC-FA-CAID-128: Sort 3-state Group Name dan Category Name

1. Klik tautan `[View Code List]`
2. Klik header `Group Name` satu kali
3. Verifikasi klik 1 (↑): `Head Office`, `Head Office > Floor 1`, `Head Office > Floor 2`, `Jakarta Office`, `Surabaya Branch`, `Warehouse`
4. Klik header `Group Name` kedua kali
5. Verifikasi klik 2 (↓): `Warehouse`, `Surabaya Branch`, `Jakarta Office`, `Head Office > Floor 2`, `Head Office > Floor 1`, `Head Office`
6. Klik header `Group Name` ketiga kali
7. Verifikasi klik 3: indikator sort hilang
8. Verifikasi klik 3: urutan kembali default A-Z menurut `Group Name`
9. Klik tab `Category Codes`
10. Klik header `Category Name` satu kali
11. Verifikasi `Category Name` klik 1: `IT Equipment`, `IT Equipment > Laptop`, `Old Equipment`, `Printer`
12. Klik header `Category Name` kedua kali
13. Verifikasi `Category Name` klik 2: `Printer`, `Old Equipment`, `IT Equipment > Laptop`, `IT Equipment`
14. Klik header `Category Name` ketiga kali
15. Verifikasi `Category Name` klik 3: urutan kembali default A-Z

### TC-FA-CAID-129: Sort 3-state Asset Name, Division Name, dan Account Name

16. Klik tab `Asset Name Codes`
17. Klik header `Asset Name` dua kali
18. Verifikasi `Asset Name` Descending: `ThinkPad T490`, `LaserJet Pro`, `Dell, Latitude 14"`
19. Klik tab `Division Codes`
20. Klik header `Division Name` dua kali
21. Verifikasi `Division Name` Descending: `Operations`, `Human Resources`, `Finance`
22. Klik tab `Account Codes`
23. Klik header `Account Name` dua kali
24. Verifikasi `Account Name` Descending: `Office Furniture`, `Computer Equipment`

### TC-FA-CAID-130: Sort 3-state Code pada tab Groups, Asset Names, dan Accounts

25. Klik tab `Group Codes`
26. Klik header `Code` satu kali
27. Verifikasi tab Groups Ascending: `F1`, `F2`, `HO`, `JKT`, `SBY`, `WH`
28. Klik header `Code` kedua kali
29. Verifikasi tab Groups Descending: `WH`, `SBY`, `JKT`, `HO`, `F2`, `F1`
30. Klik tab `Asset Name Codes`
31. Klik header `Code` satu kali
32. Verifikasi tab Asset Names Ascending: `DL14`, `LJP`, `T490`
33. Klik header `Code` kedua kali
34. Verifikasi tab Asset Names Descending: `T490`, `LJP`, `DL14`
35. Klik tab `Account Codes`
36. Klik header `Code` satu kali
37. Verifikasi tab Accounts Ascending: `1210`, `1220`
38. Klik header `Code` kedua kali
39. Verifikasi tab Accounts Descending: `1220`, `1210`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 39 langkah, di atas 35 langkah. Alasan: ketiga blok TC memakai dataset yang sama (Pre-setup No 28) dan satu kelas harness (fungsional baca, tanpa mutasi); setiap tab menyimpan Sort sendiri selama modal terbuka, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan langkah yang berulang per tab (klik tab, klik header, `Verifikasi` urutan) adalah ekspansi, bukan alur berbeda (bagian 8b butir 7).
- Langkah penghubung (tanpa `Verifikasi`): langkah 25 (kembali ke tab `Group Codes`, sort tab itu sudah dikembalikan ke default oleh klik ketiga pada TC-FA-CAID-128).
- Urutan Ascending pada TC-FA-CAID-130 mengikuti Code sebagai teks (`F1`, `F2`, `HO`, ...); urutan tab Accounts mengikuti Code `1210`, `1220`.
- Pembagian TC lintas spec: TC-FA-CAID-131 (Sort tidak mereset Search) ada di spec 052.
