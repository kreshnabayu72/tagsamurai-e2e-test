---
id: TC-GS-IMPORT-E2E-166-isi-berkas-download-template-tab-brand-measurement-position-division
title: "Isi berkas Download Template Tab Brand, Measurement, Position, Division: Sheet 1 header dan baris contoh, Sheet Field Limit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-435
  - TC-GS-IMPORT-436
  - TC-GS-IMPORT-437
  - TC-GS-IMPORT-438
  - TC-GS-IMPORT-439
  - TC-GS-IMPORT-440
  - TC-GS-IMPORT-441
  - TC-GS-IMPORT-442
coverage:
  web: automated
---

# Isi berkas Download Template Tab Brand, Measurement, Position, Division: Sheet 1 header dan baris contoh, Sheet Field Limit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): suite mengubah state global dan Custom Field Client A dibaca lintas spec; lihat `suite.md`. Spec ini hanya membaca (tidak membuat atau mengubah data).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client A dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas XLSX pada buffer unduhan (nama berkas, nama sheet, isi sel, jumlah baris) tanpa membuka aplikasi spreadsheet.
- Data Pre-setup Client A (hanya dibaca, tidak diubah spec ini): Custom Field Active `Emergency Phone` (Phone), `Join Date` (Date), `Overtime Hours` (Numeric 2 desimal), `Shift` (Dropdown: Pagi, Siang, Malam), `Shift Notes` (Text Area), seluruhnya Optional; Custom Field `Old Badge` nonaktif. Template Tab Brand, Measurement, Position, dan Division tidak memuat Custom Field.
- Satu unduhan per Sub-Tab dipakai untuk Sheet 1 (TC-435, 437, 439, 441) dan Sheet 2 (TC-436, 438, 440, 442) karena TC sumber mengunduh berkas yang sama pada Sub-Tab yang sama.
- Pemulihan (hook `after`): tidak ada data yang dibuat; kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-435 dan TC-GS-IMPORT-436: Tab Brand

1. Pilih Sub-Tab Brand
2. Klik `[Download Template]` di toolbar
3. Verifikasi berkas `Template-Import-Brand.xlsx` terunduh langsung
4. Verifikasi tidak ada toast yang tampil
5. Buka berkas XLSX yang terunduh pada pembaca buffer
6. Verifikasi berkas memuat 2 sheet
7. Verifikasi Sheet 1 bernama `Brand`
8. Verifikasi baris 1 (header) persis nama Target Attribute: Brand Name
9. Verifikasi baris 2 sampai 4 berisi 3 baris contoh: (Acme Corp) | (Lenovo) | (Zebra Technologies)
10. Verifikasi baris 5 ke bawah kosong
11. Buka Sheet 2 `Field Limit`
12. Verifikasi Sheet 2 bernama "Field Limit" dengan kolom "Column", "Data Type", "Description", "Constraint", dan "Example"
13. Verifikasi baris "Brand Name": Data Type "Text", Description "Name of the brand.", Constraint "Required. Max 120 characters. All printable characters except emoji. Must be unique within the organization (case-insensitive).", Example "Acme Corp"
14. Verifikasi Sheet 2 tidak memuat baris Custom Field (Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes)

### TC-GS-IMPORT-437 dan TC-GS-IMPORT-438: Tab Measurement

15. Pilih Sub-Tab Measurement
16. Klik `[Download Template]` di toolbar
17. Verifikasi berkas `Template-Import-Measurement.xlsx` terunduh langsung
18. Verifikasi tidak ada toast yang tampil
19. Buka berkas XLSX yang terunduh pada pembaca buffer
20. Verifikasi berkas memuat 2 sheet
21. Verifikasi Sheet 1 bernama `Measurement`
22. Verifikasi baris 1 (header) persis nama Target Attribute: Unit Name; Symbol
23. Verifikasi baris 2 sampai 4 berisi 3 baris contoh: (Kilogram, kg) | (Meter, m) | (Piece, pcs)
24. Verifikasi baris 5 ke bawah kosong
25. Buka Sheet 2 `Field Limit`
26. Verifikasi Sheet 2 bernama "Field Limit" dengan kolom "Column", "Data Type", "Description", "Constraint", dan "Example"
27. Verifikasi baris "Unit Name": Data Type "Text", Description "Name of the unit of measurement.", Constraint "Required. Max 120 characters. All printable characters except emoji. Must be unique within the organization (case-insensitive).", Example "Kilogram"
28. Verifikasi baris "Symbol": Data Type "Text", Description "Short symbol for the unit.", Constraint "Required. Max 10 characters. All printable characters except emoji. Does not need to be unique.", Example "kg"
29. Verifikasi Sheet 2 tidak memuat baris Custom Field (Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes)

### TC-GS-IMPORT-439 dan TC-GS-IMPORT-440: Tab Position

30. Pilih Sub-Tab Position
31. Klik `[Download Template]` di toolbar
32. Verifikasi berkas `Template-Import-Position.xlsx` terunduh langsung
33. Verifikasi tidak ada toast yang tampil
34. Buka berkas XLSX yang terunduh pada pembaca buffer
35. Verifikasi berkas memuat 2 sheet
36. Verifikasi Sheet 1 bernama `Position`
37. Verifikasi baris 1 (header) persis nama Target Attribute: Position Name
38. Verifikasi baris 2 sampai 4 berisi 3 baris contoh: (Store Manager) | (Warehouse Supervisor) | (Field Technician)
39. Verifikasi baris 5 ke bawah kosong
40. Buka Sheet 2 `Field Limit`
41. Verifikasi Sheet 2 bernama "Field Limit" dengan kolom "Column", "Data Type", "Description", "Constraint", dan "Example"
42. Verifikasi baris "Position Name": Data Type "Text", Description "Name of the position.", Constraint "Required. Max 120 characters. All printable characters except emoji. Must be unique within the organization (case-insensitive).", Example "Store Manager"
43. Verifikasi Sheet 2 tidak memuat baris Custom Field (Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes)

### TC-GS-IMPORT-441 dan TC-GS-IMPORT-442: Tab Division

44. Pilih Sub-Tab Division
45. Klik `[Download Template]` di toolbar
46. Verifikasi berkas `Template-Import-Division.xlsx` terunduh langsung
47. Verifikasi tidak ada toast yang tampil
48. Buka berkas XLSX yang terunduh pada pembaca buffer
49. Verifikasi berkas memuat 2 sheet
50. Verifikasi Sheet 1 bernama `Division`
51. Verifikasi baris 1 (header) persis nama Target Attribute: Division Name; Code
52. Verifikasi baris 2 sampai 4 berisi 3 baris contoh: (Finance & Accounting, FIN) | (Operations, ) | (IT Support, ITS)
53. Verifikasi baris 5 ke bawah kosong
54. Buka Sheet 2 `Field Limit`
55. Verifikasi Sheet 2 bernama "Field Limit" dengan kolom "Column", "Data Type", "Description", "Constraint", dan "Example"
56. Verifikasi baris "Division Name": Data Type "Text", Description "Name of the division.", Constraint "Required. Max 120 characters. All printable characters except emoji. Must be unique within the organization (case-insensitive).", Example "Finance & Accounting"
57. Verifikasi baris "Code": Data Type "Text", Description "Short identifier for the division.", Constraint "Optional — leave blank to auto-generate. Max 15 characters. Letters, numbers, -, _, and . only. Converted to uppercase. Must be unique.", Example "FIN"
58. Verifikasi Sheet 2 tidak memuat baris Custom Field (Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: binary buffer (f); objek uji adalah isi berkas XLSX hasil unduhan, bukan kegagalan unduh (kegagalan unduh ada di spec 147).
- Alasan melewati sekitar 35 langkah (58 langkah nominal): empat blok homogen (satu Sub-Tab per blok, dua TC per blok yang membaca berkas yang sama), semua satu kelas binary buffer dan berdiri sendiri tanpa data bersama, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok mengikuti TC (Brand, Measurement, Position, Division).
- Langkah penghubung (tanpa `Verifikasi`): pemilihan Sub-Tab, klik `[Download Template]`, pembukaan berkas pada pembaca buffer, dan pembukaan Sheet 2 (langkah 1, 2, 5, 11 dan padanannya). Pembaruan nama berkas diasersi segera setelah unduh (langkah 3 dan 4, state sementara toast); asersi absence toast didahului berkas terunduh sebagai anchor positif yang terhubung ke pemicu. Asersi absence Custom Field di Sheet 2 (langkah 14, 29, 43, 58) didahului Verifikasi baris Field Limit pada sheet yang sama sebagai pembanding.
- Temuan untuk QA:
  - TC-GS-IMPORT-435 sampai 442 memuat "Post Condition: -" dan tidak punya keadaan lain yang perlu dipulihkan; spec tidak membuat data.
  - TC-GS-IMPORT-435, 437, 439, 441 (Sheet 1) dan TC-GS-IMPORT-436, 438, 440, 442 (Sheet 2) mengunduh berkas yang sama pada Sub-Tab yang sama; spec membaca kedua sheet dari satu unduhan per Sub-Tab (penghematan), bukan dua unduhan.
  - TC-GS-IMPORT-441 baris contoh kedua `(Operations, )` berarti Code kosong; asersi sel kosong mengikuti nilai tertulis di Expected.
  - Template tidak memuat Custom Field untuk Tab Brand, Measurement, Position, Division; TC-GS-IMPORT-436, 438, 440, 442 mengasersi hal itu pada Sheet 2.
