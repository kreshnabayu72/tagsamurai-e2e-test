---
id: TC-FA-GRP-E2E-222-tab-assets-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4
title: "Tab Assets Setup Column: Screening Overlay dan Popup, Guard Kolom Terakhir, dan Pin ke-4 Diblok"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-704
  - TC-FA-GRP-705
  - TC-FA-GRP-718
  - TC-FA-GRP-1090
coverage:
  web: automated
---

# Tab Assets Setup Column: Screening Overlay dan Popup, Guard Kolom Terakhir, dan Pin ke-4 Diblok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite pada `suite.md` berlaku.
- Data Pre-setup (hanya dibaca): Warehouse A (WH-A, Assignable, 24 aset aktif variasi Brand, Model/Type, dan status, ditambah 2 Disposed) pada pohon group Tabel A. Kolom Tab Assets berada pada konfigurasi default sebagai kondisi awal.
- Setup Column: spec tidak menyimpan konfigurasi (tidak ada langkah `[Save]`); hook `after` menghapus preferensi kolom Tab Assets di browser sebagai cadangan (kemampuan disediakan tim FE).
- Ketersediaan kolom Custom Field pada overlay dan popup mengikuti hak aktor Total Control dan AST-LOGIC-10 (data Custom Field aktif client disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-704: Screening overlay Column Visibility Tab Assets

1. Klik angka Total Asset Warehouse A
2. Hover icon (⋯) pada header kolom terakhir
3. Verifikasi tooltip `Column Visibility` tampil saat hover
4. Klik icon (⋯)
5. Verifikasi overlay terbuka dengan item `Setup Column...` di bagian bawah panel
6. Verifikasi daftar kolom overlay berurutan Name (☑ Hideable checked & enabled) · Asset ID (☑ Hideable checked & enabled) · TAG (☑ Hideable checked & enabled) · Brand (☑ Hideable checked & enabled) · Model/Type (☑ Hideable checked & enabled) · Measurement (☐ Curated unchecked & enabled) · Category (☐ Curated unchecked & enabled) · Label (☐ Curated unchecked & enabled) · Status (☑ Hideable checked & enabled) · Transactional Policy (☐ Curated unchecked & enabled) · Last Scanned (☐ Curated unchecked & enabled) · Asset Value (Commercial) · Asset Value (Fiscal) (☐ Curated unchecked & enabled) · Warranty Expiry (☐ Curated unchecked & enabled) · [Field Name] per Custom Field Active yang tersedia bagi aktor (☐ Curated unchecked & enabled) · Last Updated (☑ Hideable checked & enabled)
7. Verifikasi overlay tidak memuat kolom Group
8. Verifikasi tiap baris kolom pada overlay punya drag handle

### TC-FA-GRP-705: Screening popup Setup Column Tab Assets (3 zona + Live Preview)

9. Klik `Setup Column...` pada overlay
10. Verifikasi Header popup memuat Title `Setup Column`
11. Verifikasi Header popup memuat teks panduan drag/check/pin
12. Verifikasi Header popup memuat icon close (X)
13. Verifikasi Body popup memuat daftar kolom Name (☑ Hideable checked & enabled) · Asset ID (☑ Hideable checked & enabled) · TAG (☑ Hideable checked & enabled) · Brand (☑ Hideable checked & enabled) · Model/Type (☑ Hideable checked & enabled) · Measurement (☐ Curated unchecked & enabled) · Category (☐ Curated unchecked & enabled) · Label (☐ Curated unchecked & enabled) · Status (☑ Hideable checked & enabled) · Transactional Policy (☐ Curated unchecked & enabled) · Last Scanned (☐ Curated unchecked & enabled) · Asset Value (Commercial) · Asset Value (Fiscal) (☐ Curated unchecked & enabled) · Warranty Expiry (☐ Curated unchecked & enabled) · [Field Name] per Custom Field Active yang tersedia bagi aktor (☐ Curated unchecked & enabled) · Last Updated (☑ Hideable checked & enabled)
14. Verifikasi daftar kolom popup tanpa kolom Group
15. Verifikasi tiap baris kolom popup punya drag handle dan icon Pin
16. Verifikasi Live Preview menampilkan header kolom dan sel data sesuai tabel asli
17. Verifikasi Footer memuat `[Reset to Default]` (text, primary)
18. Verifikasi Footer memuat `[Save]` (filled, success)
19. Verifikasi Footer tidak memuat `[Cancel]`

### TC-FA-GRP-718: Guard kolom terakhir yang visible

20. Uncheck Asset ID
21. Uncheck TAG
22. Uncheck Brand
23. Uncheck Model/Type
24. Uncheck Status
25. Uncheck Last Updated
26. Hover checkbox kolom Name
27. Verifikasi checkbox kolom Name disabled dan tetap tampil
28. Verifikasi tooltip "At least one column must remain visible."

### TC-FA-GRP-1090: Pin ke-4 diblok setelah tiga kolom terpin

29. Klik (X) pada header popup
30. Klik icon (⋯) pada header kolom terakhir
31. Klik [Setup Column]
32. Klik icon Pin Name
33. Klik icon Pin Asset ID
34. Klik icon Pin Brand
35. Verifikasi kolom Name, Asset ID, dan Brand berstatus terpin
36. Hover icon Pin kolom Model/Type
37. Verifikasi icon Pin kolom Model/Type disabled (tidak dapat diklik, kolom tidak beku)
38. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
39. Klik icon Pin Brand untuk unpin
40. Hover icon Pin kolom Model/Type
41. Verifikasi icon Pin kolom Model/Type kembali aktif
42. Klik (X) pada header popup

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 9 melanjutkan overlay yang terbuka dari TC-FA-GRP-704 (TC-FA-GRP-705 membuka popup lewat icon (⋯) lalu `[Setup Column]`, item yang sama dengan `Setup Column...` pada overlay); langkah 29 menutup popup dan membuang perubahan TC-FA-GRP-718 tanpa menyimpan; langkah 42 menutup popup tanpa menyimpan.
- Alasan di atas 35 langkah: seluruh blok satu kelas (Setup Column Tab Assets, dataset Warehouse A yang sama), tiap blok berdiri sendiri (popup ditutup dan dibuka ulang antar blok), dan 6 dari langkah adalah uncheck kolom berulang (langkah 20 sampai 25) yang dibutuhkan agar tersisa satu kolom.
- Kolom yang tersisa pada TC-FA-GRP-718 dipilih Name; TC tidak menyebut kolom mana yang tersisa.
- Temuan untuk QA:
  - TC-FA-GRP-705 Expected "Teks panduan drag/check/pin" tidak memuat teks persisnya, sehingga langkah 11 hanya mengasersi keberadaan teks panduan.
  - TC-FA-GRP-718 Langkah 4 "Uncheck seluruh kolom kecuali satu" tidak menyebut kolom yang tersisa.
  - TC-FA-GRP-704 Expected b menyebut tiga zona Hideable/Curated tetapi baris `Asset Value (Commercial) · Asset Value (Fiscal)` ditulis dengan satu keterangan state; spec mengikuti teks TC apa adanya.
