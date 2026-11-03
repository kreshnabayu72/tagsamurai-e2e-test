---
id: TC-FA-CAID-E2E-049-code-list-screening-isi-tab-dan-aturan-baris
title: "Modal View Code List: Screening, Isi Tab, dan Aturan Baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-116
  - TC-FA-CAID-117
  - TC-FA-CAID-118
  - TC-FA-CAID-119
coverage:
  web: automated
---

# Modal View Code List: Screening, Isi Tab, dan Aturan Baris

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE). Spec hanya membaca; tidak ada data dibuat atau diubah. Dataset itu juga memuat baris yang tidak boleh tampil: Account `Legacy Account` (Inactive, ber-Code) dan `Prepaid Insurance` (Active tanpa Code).
- Data Dinamis: tidak ada. State global: tidak ada yang diubah.

## Test Steps

### TC-FA-CAID-116: Screening Modal View Code List saat dibuka

1. Klik tautan `[View Code List]`
2. Verifikasi Zona Header: Title `Code List Reference` dengan ikon close `[✕]`
3. Verifikasi Zona Header: Description `Review all active abbreviations currently configured in your master taxonomies.`
4. Verifikasi Zona Header: Tabs `Group Codes | Category Codes | Asset Name Codes | Division Codes | Account Codes` dengan `Group Codes` aktif
5. Verifikasi Zona Header: Table Tools `Search | Download` dengan placeholder Search `Search name or code...`
6. Verifikasi Zona Body: kolom `Group Name (sortable)`, `Code (sortable)`, `Actions (⋯)` (unsortable)
7. Verifikasi Zona Body: enam baris `Head Office / HO`, `Head Office > Floor 1 / F1`, `Head Office > Floor 2 / F2`, `Jakarta Office / JKT`, `Surabaya Branch / SBY`, `Warehouse / WH` berurutan A-Z menurut `Group Name`
8. Verifikasi tidak ada Filter dan tidak ada Changelog pada Table Tools
9. Verifikasi Zona Footer: pagination default 10 data per halaman
10. Verifikasi tidak ada kolom checkbox seleksi massal

### TC-FA-CAID-117: Isi tab Groups dan Categories

11. Verifikasi tab `Group Codes`: header kolom `Group Name` dan `Code`
12. Verifikasi nama group tampil sebagai full path (`Head Office > Floor 1`)
13. Klik tab `Category Codes`
14. Verifikasi tab `Category Codes`: header kolom `Category Name` dan `Code`
15. Verifikasi baris `IT Equipment / ITE`, `IT Equipment > Laptop / LAP`, `Old Equipment / OLD`, `Printer / PRN` berurutan A-Z menurut `Category Name`

### TC-FA-CAID-118: Isi tab Asset Names, Divisions, dan Accounts

16. Klik tab `Asset Name Codes`
17. Verifikasi header `Asset Name` dan `Code`
18. Verifikasi baris `Dell, Latitude 14" / DL14`, `LaserJet Pro / LJP`, `ThinkPad T490 / T490` berurutan A-Z
19. Klik tab `Division Codes`
20. Verifikasi header `Division Name` dan `Code`
21. Verifikasi baris `Finance / FIN`, `Human Resources / HR`, `Operations / OPS`
22. Klik tab `Account Codes`
23. Verifikasi header `Account Name` dan `Code`
24. Verifikasi baris `Computer Equipment / 1210` dan `Office Furniture / 1220`

### TC-FA-CAID-119: Baris yang tampil

25. Klik tab `Group Codes`
26. Verifikasi Group `Surabaya Branch` berstatus Excess tetap tampil dengan Code `SBY`
27. Klik tab `Category Codes`
28. Verifikasi Category `Old Equipment` berstatus Locked tetap tampil dengan Code `OLD`
29. Klik tab `Account Codes`
30. Verifikasi hanya Account Active ber-Code yang tampil (`Computer Equipment` dan `Office Furniture`)
31. Verifikasi Account `Legacy Account` (Inactive) tidak tampil
32. Verifikasi Account `Prepaid Insurance` (tanpa Code) tidak tampil

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 32 langkah.
- Subjudul `###` memetakan langkah ke id TC granular. Modal View Code List dibuka sekali pada TC-FA-CAID-116 dan tetap terbuka sampai akhir spec; langkah "Klik tautan `[View Code List]`" pada TC-FA-CAID-117, 118, dan 119 tidak diulang karena modal sudah terbuka (bagian 3, halaman yang sama dipakai berulang).
- Langkah penghubung (tanpa `Verifikasi`): langkah 25 (kembali ke tab `Group Codes` sebelum TC-FA-CAID-119 karena TC-FA-CAID-118 berakhir di tab `Account Codes`).
- Asersi absence (tidak ada Filter dan Changelog, tidak ada kolom checkbox, `Legacy Account` dan `Prepaid Insurance` tidak tampil) didahului `Verifikasi` Table Tools `Search | Download`, enam baris tabel, dan daftar Account Active ber-Code (langkah 30) pada surface yang sama (bagian 8b butir 2).
- Pembagian TC lintas spec: Modal View Code List dikover spec 049 sampai 060, 064, dan 065; TC-FA-CAID-116 sampai 119 hanya ada di spec ini.
- Alasan topik Modal View Code List berada di beberapa spec (bagian 3 prinsip 1): tiap spec memakai dataset berbeda. Spec ini hanya membaca dataset tetap Pre-setup No 28 pada Company Alpha; pagination memakai `Company Volume` 120 master per tab (Pre-setup No 16, spec 054 dan 055) dan teks literal serta nama panjang memakai `Company Code List Khusus` (Pre-setup No 34, spec 050), masing-masing dengan akun sendiri sesuai TC. Ukuran gabungan dataset-dataset itu juga melebihi sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-CAID-116 Expected b menyebut header kolom aksi `Actions (⋯) (unsortable)` tanpa langkah klik header itu; klausa lama "header diklik membuka overlay Column Visibility dengan CTA `[Setup Column]`" tidak lagi ada di TC dan tidak diasersi di spec ini. Perilaku klik header, label tooltip `Column Visibility`, dan item overlay `Setup Column...` diuji TC-FA-CAID-132 (spec 056).
  - TC-FA-CAID-119 menyebut status Excess dan Locked, sedangkan modal tidak punya kolom status; spec hanya mengasersi baris tampil dengan Code yang disebut Expected.
