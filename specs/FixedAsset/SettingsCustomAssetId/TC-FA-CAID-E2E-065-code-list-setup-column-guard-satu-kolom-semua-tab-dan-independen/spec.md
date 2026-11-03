---
id: TC-FA-CAID-E2E-065-code-list-setup-column-guard-satu-kolom-semua-tab-dan-independen
title: "Modal View Code List: Setup Column Guard Satu Kolom, Perilaku Semua Tab, dan Konfigurasi Independen per Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-139
  - TC-FA-CAID-140
  - TC-FA-CAID-141
coverage:
  web: automated
---

# Modal View Code List: Setup Column Guard Satu Kolom, Perilaku Semua Tab, dan Konfigurasi Independen per Tab

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE). Spec hanya membaca.
- Data Dinamis: tidak ada. State global: Preferensi kolom Setup Column Modal View Code List disimpan di browser; hook `after` spec ini menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE. Kolom `Code` disembunyikan dan disimpan pada kelima tab pada TC-FA-CAID-140 dan 141.

## Test Steps

### TC-FA-CAID-139: Guard satu kolom tersisa

1. Klik tautan `[View Code List]`
2. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
3. Hilangkan centang `Code`
4. Hover checkbox `Group Name`
5. Verifikasi checkbox `Group Name` berstatus disabled
6. Verifikasi checkbox `Group Name` tetap tercentang
7. Verifikasi tooltip berbunyi `At least one column must remain visible.`
8. Klik `[✕]` pada Popup Setup Column (membuang perubahan)

### TC-FA-CAID-141: Konfigurasi kolom tiap tab tersimpan independen

9. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
10. Hilangkan centang `Code`
11. Klik `[Save]`
12. Klik tab `Category Codes`
13. Verifikasi tab `Category Codes` tetap menampilkan kolom `Category Name` dan `Code` (cache kolom tiap tab terpisah)

### TC-FA-CAID-140: Setup Column di tab Categories, Asset Names, Divisions, dan Accounts

14. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
15. Hilangkan centang `Code`
16. Klik `[Save]`
17. Verifikasi tab `Category Codes`: hanya kolom `Category Name` yang tampil dan kolom `Code` tersembunyi
18. Klik tab `Asset Name Codes`
19. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
20. Hilangkan centang `Code`
21. Klik `[Save]`
22. Verifikasi tab `Asset Name Codes`: hanya kolom `Asset Name` yang tampil dan kolom `Code` tersembunyi
23. Klik tab `Division Codes`
24. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
25. Hilangkan centang `Code`
26. Klik `[Save]`
27. Verifikasi tab `Division Codes`: hanya kolom `Division Name` yang tampil dan kolom `Code` tersembunyi
28. Klik tab `Account Codes`
29. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
30. Hilangkan centang `Code`
31. Klik `[Save]`
32. Verifikasi tab `Account Codes`: hanya kolom `Account Name` yang tampil dan kolom `Code` tersembunyi

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 32 langkah.
- Urutan TC di dalam spec: TC-FA-CAID-139, 141, lalu 140. TC-FA-CAID-141 membutuhkan tab `Category Codes` dengan kolom default, sedangkan TC-FA-CAID-140 menyembunyikan kolom `Code` di tab itu.
- Langkah penghubung (tanpa `Verifikasi`): langkah 8 (klik `[✕]` membuang perubahan TC-FA-CAID-139 yang tidak disimpan, S-09) dan langkah 12 (pindah ke tab `Category Codes` adalah langkah TC-FA-CAID-141).
- Pembukaan Popup Setup Column ditulis sebagai satu langkah (klik header kolom Actions (⋯), lalu `Setup Column...`) mengikuti "Buka Popup Setup Column" pada TC. Langkah per tab pada TC-FA-CAID-140 adalah ekspansi empat tab (klik tab, buka popup, hilangkan centang `Code`, `[Save]`, `Verifikasi`).
- Pembagian TC lintas spec: TC-FA-CAID-132 sampai 135 ada di spec 056; TC-FA-CAID-136 sampai 138 ada di spec 057.
