---
id: TC-GS-IMPORT-E2E-167-isi-berkas-download-template-tab-user-login-dan-user-non-login-sheet-1
title: "Isi berkas Download Template Tab User Login dan User Non Login: Sheet 1 dan Sheet Field Limit termasuk Custom Field Active Client A"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-443
  - TC-GS-IMPORT-444
  - TC-GS-IMPORT-445
  - TC-GS-IMPORT-446
coverage:
  web: automated
---

# Isi berkas Download Template Tab User Login dan User Non Login: Sheet 1 dan Sheet Field Limit termasuk Custom Field Active Client A

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): suite mengubah state global dan Custom Field Client A dibaca lintas spec; lihat `suite.md`. Spec ini hanya membaca (tidak membuat atau mengubah data).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client A dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas XLSX pada buffer unduhan (nama berkas, nama sheet, isi sel, jumlah baris) tanpa membuka aplikasi spreadsheet.
- Data Pre-setup Client A (hanya dibaca, tidak diubah spec ini): Custom Field Active `Emergency Phone` (Phone), `Join Date` (Date), `Overtime Hours` (Numeric 2 desimal), `Shift` (Dropdown: Pagi, Siang, Malam), `Shift Notes` (Text Area), seluruhnya Optional; Custom Field `Old Badge` nonaktif.
- Nilai relatif hari uji: Example baris "Active Period" pada Sheet 2 adalah tanggal pada bulan berikutnya dari hari uji dalam format YYYY-MM-DD; nilai dihitung saat run dari tanggal hari uji.
- Satu unduhan per Sub-Tab dipakai untuk Sheet 1 (TC-443, 445) dan Sheet 2 (TC-444, 446) karena TC sumber mengunduh berkas yang sama pada Sub-Tab yang sama.
- Pemulihan (hook `after`): tidak ada data yang dibuat; kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-443 dan TC-GS-IMPORT-444: Tab User Login

1. Pilih Sub-Tab User Login
2. Klik `[Download Template]` di toolbar
3. Verifikasi berkas `Template-Import-User-Login.xlsx` terunduh langsung
4. Verifikasi tidak ada toast yang tampil
5. Buka berkas XLSX yang terunduh pada pembaca buffer
6. Verifikasi berkas memuat 2 sheet
7. Verifikasi Sheet 1 bernama `User Login`
8. Verifikasi baris 1 (header) persis nama Target Attribute: First Name; Last Name; Email; Division; Position; Employee ID; Access; Active Period
9. Verifikasi header diikuti kolom Custom Field Active Client A (Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes) di akhir header
10. Verifikasi baris 2 sampai 4 berisi 3 baris contoh: (Ahmad, Fauzi, ahmad.fauzi@example.com, Engineering, Senior Developer, , Global Settings, ) | (Budi, Setiawan, budi.setiawan@example.com, Finance, Finance Manager, EMP-1002, Global Settings;Fixed Asset, ) | (Citra, Lestari, citra.lestari@example.com, Marketing, , , Global Settings, )
11. Verifikasi baris 5 ke bawah kosong
12. Buka Sheet 2 `Field Limit`
13. Verifikasi Sheet 2 bernama "Field Limit" dengan kolom "Column", "Data Type", "Description", "Constraint", dan "Example"
14. Verifikasi baris "First Name": Data Type "Text", Description "First name of the user.", Constraint "Required. Max 120 characters.", Example "Ahmad"
15. Verifikasi baris "Last Name": Data Type "Text", Description "Last name of the user.", Constraint "Required. Max 120 characters.", Example "Fauzi"
16. Verifikasi baris "Email": Data Type "Email", Description "Email address of the user.", Constraint "Required. Valid email format. Max 120 characters. Must be unique across the platform, including Non-Login Users.", Example "ahmad.fauzi@example.com"
17. Verifikasi baris "Division": Data Type "Text", Description "Division the user belongs to.", Constraint "Required. Must match an existing division.", Example "Engineering"
18. Verifikasi baris "Position": Data Type "Text", Description "Position of the user.", Constraint "Optional. If filled, must match an existing position.", Example "Senior Developer"
19. Verifikasi baris "Employee ID": Data Type "Text", Description "Employee identifier.", Constraint "Optional. Max 120 characters. All printable characters except emoji. Must be unique within the organization, across Login and Non-Login Users.", Example "EMP-1002"
20. Verifikasi baris "Access": Data Type "Option", Description "Products the user can access.", Constraint "Required. One or more of the products available to your organization, separated by ;.", Example "Global Settings;Fixed Asset"
21. Verifikasi baris "Active Period": Data Type "Date", Description "Makes the user a Temporary User until this date.", Constraint "Optional. Date in YYYY-MM-DD format, tomorrow or later. Leave blank for a regular user.", Example tanggal pada bulan berikutnya dari hari uji dalam format YYYY-MM-DD

### TC-GS-IMPORT-445 dan TC-GS-IMPORT-446: Tab User Non Login

22. Pilih Sub-Tab User Non Login
23. Klik `[Download Template]` di toolbar
24. Verifikasi berkas `Template-Import-User-Non-Login.xlsx` terunduh langsung
25. Verifikasi tidak ada toast yang tampil
26. Buka berkas XLSX yang terunduh pada pembaca buffer
27. Verifikasi berkas memuat 2 sheet
28. Verifikasi Sheet 1 bernama `User Non Login`
29. Verifikasi baris 1 (header) persis nama Target Attribute: First Name; Last Name; Email; Division; Position; Employee ID; Represented By; Active Period
30. Verifikasi header diikuti kolom Custom Field Active Client A (Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes) di akhir header
31. Verifikasi baris 2 sampai 4 berisi 3 baris contoh: (Siti, Rahayu, siti.rahayu@example.com, Warehouse, , , ahmad.fauzi@example.com, ) | (Dewi, Anggraini, dewi.anggraini@example.com, Engineering, Technician, EMP-2002, budi.setiawan@example.com, ) | (Rudi, Hartono, rudi.hartono@example.com, Operations, Supervisor, , citra.lestari@example.com, )
32. Verifikasi baris 5 ke bawah kosong
33. Buka Sheet 2 `Field Limit`
34. Verifikasi Sheet 2 bernama "Field Limit" dengan kolom "Column", "Data Type", "Description", "Constraint", dan "Example"
35. Verifikasi baris "First Name": Data Type "Text", Description "First name of the user.", Constraint "Required. Max 120 characters. All printable characters except emoji.", Example "Ahmad"
36. Verifikasi baris "Last Name": Data Type "Text", Description "Last name of the user.", Constraint "Required. Max 120 characters. All printable characters except emoji.", Example "Fauzi"
37. Verifikasi baris "Email": Data Type "Email", Description "Email address of the user.", Constraint "Required. Valid email format. Max 120 characters. Must be unique across the platform, including Non-Login Users.", Example "ahmad.fauzi@example.com"
38. Verifikasi baris "Division": Data Type "Text", Description "Division the user belongs to.", Constraint "Required. Must match an existing division.", Example "Engineering"
39. Verifikasi baris "Position": Data Type "Text", Description "Position of the user.", Constraint "Optional. If filled, must match an existing position.", Example "Senior Developer"
40. Verifikasi baris "Employee ID": Data Type "Text", Description "Employee identifier.", Constraint "Optional. Max 120 characters. All printable characters except emoji. Must be unique within the organization, across Login and Non-Login Users.", Example "EMP-1002"
41. Verifikasi baris "Represented By": Data Type "Email", Description "The Login User who represents this user.", Constraint "Required. Must be the email of an active User Login account.", Example "ahmad.fauzi@example.com"
42. Verifikasi baris "Active Period": Data Type "Date", Description "Makes the user a Temporary User until this date.", Constraint "Optional. Date in YYYY-MM-DD format, tomorrow or later. Leave blank for a regular user.", Example tanggal pada bulan berikutnya dari hari uji dalam format YYYY-MM-DD
43. Verifikasi Sheet 2 tidak memuat baris "Access"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: binary buffer (f); objek uji adalah isi berkas XLSX hasil unduhan.
- Alasan melewati sekitar 35 langkah (43 langkah nominal): dua blok homogen (satu Sub-Tab per blok, dua TC per blok yang membaca berkas yang sama), satu kelas binary buffer dan berdiri sendiri tanpa data bersama; sebagian besar langkah adalah `Verifikasi` per baris Field Limit (satu per klausa).
- Subjudul `###` memetakan langkah ke id TC granular. Baris Custom Field Active di Sheet 2 diasersi di spec 168 (TC-GS-IMPORT-447, 448).
- Langkah penghubung (tanpa `Verifikasi`): pemilihan Sub-Tab, klik `[Download Template]`, pembukaan berkas pada pembaca buffer, dan pembukaan Sheet 2 (langkah 1, 2, 5, 12, 22, 23, 26, 33). Langkah 4 dan 25 (tidak ada toast) didahului langkah berkas terunduh sebagai anchor positif; langkah 43 (tidak ada baris "Access") didahului Verifikasi baris Field Limit lain pada sheet yang sama sebagai pembanding.
- Temuan untuk QA:
  - TC-GS-IMPORT-443 dan 445 menyebut kolom Custom Field Active Client A di akhir header tanpa menyebut urutannya; spec mengasersi kelima nama kolom tanpa urutan, sedangkan urutan A-Z antar-Custom Field ada di TC-GS-IMPORT-449 (spec 168).
  - TC-GS-IMPORT-444 dan 446 menyebut Example Active Period sebagai "tanggal pada bulan berikutnya dari hari uji"; format dan aturan "bulan berikutnya" (tanggal tetap, tanggal yang sama bulan depan) tidak dirinci; spec menghitung dari tanggal hari uji.
  - Post Condition semua TC di spec ini "-" dan tidak ada data yang perlu dipulihkan.
