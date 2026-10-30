---
id: TC-GS-IMPORT-E2E-086-presedensi-status-error-kolom-identitas-didahulukan-dari-duplicate-dan
title: "Presedensi status: error kolom identitas didahulukan dari duplicate, dan duplicate didahulukan dari error non-identitas"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-189
  - TC-GS-IMPORT-837
  - TC-GS-IMPORT-839
  - TC-GS-IMPORT-848
  - TC-GS-IMPORT-849
  - TC-GS-IMPORT-850
  - TC-GS-IMPORT-857
  - TC-GS-IMPORT-871@L938
coverage:
  web: automated
---

# Presedensi status: error kolom identitas didahulukan dari duplicate, dan duplicate didahulukan dari error non-identitas

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import untuk Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Layanan AI: mock tetap mode normal (Data Dinamis D-40, tabel D-41 dan D-42; default, tanpa penggantian mode) untuk TC-837 dan TC-839; disediakan tim FE/BE.
- Data Pre-setup Client C (tidak diubah spec ini, R4): Division `Engineering` (Code `ENG`), Position `Finance Manager`; Measurement `Kilogram` (`kg`); User Login `dewi.anggraini.c@example.com` dan `rina.admin.c@example.com`. Division `Logistik` tidak ada di Client C. Client C tanpa draft pada tiap Sub-Tab sebelum tiap TC (Kontrak Fixture R1).
- Data Dinamis (berkas fixture uji, D-07; nilai literal karena draft tidak di-commit, dibuang oleh reset, dan asersi bergantung pada kesamaan dengan data Pre-setup). "121 karakter" berarti huruf yang sama diulang 121 kali:

  | TC | Sub-Tab | Berkas | Isi |
  |---|---|---|---|
  | 189 | Division | `division-code-rows-2.csv` | header `Division Name,Code`; `Billing,BIL` / `Invoicing,BIL` |
  | 871@L938 | Division | `division-code-cmp.csv` | header `Division Name,Code`; baris 1 `Billing`, `BIL`; baris 2 Division Name 121 karakter huruf `D`, `BIL` |
  | 837 | User Login | `user-login-dup-notfound.csv` | header `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period`; baris 1 `Budi,Setiawan,budi.setiawan1@example.com,Engineering,Finance Manager,EMP-1001,Global Settings,`; baris 2 `Dewi,Anggraini,dewi.anggraini.c@example.com,Logistik,,,Global Settings,` |
  | 839 | Brand | `brand-121-twice.csv` | header `Brand Name`; `Nikon` / 121 karakter huruf `A` / 121 karakter huruf `A` yang sama dengan baris 2 |
  | 848 | Measurement | `measurement-dup-symbol.csv` | header `Unit Name,Symbol`; 1 baris `Kilogram` dan Symbol 11 karakter `kg123456789` |
  | 849 | Division | `division-dup-badcode.csv` | header `Division Name,Code`; 1 baris `Engineering` dan Code `E N#G` |
  | 850 | User Login | `user-login-firstname-long-dup-email.csv` | berkas User Login standar (D-45), 1 baris: First Name 121 karakter huruf `A`, Last Name `Rahmawati`, Email `rina.admin.c@example.com`, Division `Engineering`, Position kosong, Access `Global Settings` |
  | 857 | User Login | `user-login-dup-email-longname.csv` | berkas User Login standar (D-45), 2 baris: baris 1 `Budi`, `Santoso`, `baru.dua.c+{runId}-086@example.com`, `Engineering`; baris 2 First Name 121 karakter huruf `A`, `Rahmawati`, `baru.dua.c+{runId}-086@example.com`, `Engineering` (Email belum terdaftar di sistem) |
- Kemampuan teknis: pemilihan berkas pada dialog unggah, hover pada badge Status, pengamatan toast, skrip reset draft per Sub-Tab, mock layanan AI (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`); mock AI tetap pada mode normal.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): draft Sub-Tab Brand, Measurement, Division, dan User Login Client C dibuang lewat skrip reset.

## Test Steps

### TC-GS-IMPORT-189: Code Division manual identik antar-baris

1. Pilih Sub-Tab Division; reset draft Division Client C lewat skrip reset, lalu muat ulang halaman
2. Klik `[Upload File]`
3. Pilih berkas `division-code-rows-2.csv` pada file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi modal Column Mapping tertutup
6. Verifikasi muncul toast: "Success, row has been added."
7. Verifikasi badge Status baris 1 `Billing` bertuliskan `error`
8. Verifikasi badge Status baris 1 `Billing` tidak bertuliskan `duplicate`
9. Verifikasi badge Status baris 2 `Invoicing` bertuliskan `pending`
10. Verifikasi Staging Metric Cards: Total Rows 2 (Active), Ready to Import 1, Errors 1, Duplicates 0 (Disabled)

### TC-GS-IMPORT-871@L938: Code Division identik dengan baris pembanding yang error pada nama

11. Tunggu toast lama hilang otomatis; reset draft Division Client C lewat skrip reset, lalu muat ulang halaman
12. Klik `[Upload File]`
13. Pilih berkas `division-code-cmp.csv` pada file picker
14. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
15. Verifikasi badge Status baris 1 bertuliskan `pending`
16. Verifikasi badge Status baris 2 bertuliskan `error`
17. Verifikasi Error Summary Callout memuat "Division Name: Max. 120 characters" dengan badge "1 row"
18. Verifikasi Error Summary Callout tidak memuat "Code already exists"
19. Verifikasi Staging Metric Cards: Total Rows 2 (Active), Ready to Import 1, Errors 1, Duplicates 0 (Disabled)

### TC-GS-IMPORT-839: Brand Name 121 karakter muncul dua kali

20. Tunggu toast lama hilang otomatis; pilih Sub-Tab Brand; reset draft Brand Client C lewat skrip reset, lalu muat ulang halaman
21. Klik `[Upload File]`
22. Pilih berkas `brand-121-twice.csv` pada file picker
23. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
24. Verifikasi modal Column Mapping tertutup
25. Verifikasi muncul toast: "Success, row has been added."
26. Verifikasi Staging Table menampilkan 3 baris
27. Verifikasi badge Status baris 1 bertuliskan `pending`
28. Verifikasi badge Status baris 2 dan baris 3 bertuliskan `error`
29. Verifikasi badge Status baris 2 dan baris 3 tidak bertuliskan `duplicate`
30. Verifikasi Error Summary Callout memuat "Brand Name: Max. 120 characters" dengan badge "2 rows"
31. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 1, Errors 2, Duplicates 0 (Disabled)

### TC-GS-IMPORT-850: First Name 121 karakter pada baris dengan Email terdaftar

32. Tunggu toast lama hilang otomatis; pilih Sub-Tab User Login; reset draft User Login Client C lewat skrip reset, lalu muat ulang halaman
33. Klik `[Upload File]`
34. Pilih berkas `user-login-firstname-long-dup-email.csv` pada file picker
35. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
36. Verifikasi modal Column Mapping tertutup
37. Verifikasi muncul toast: "Success, row has been added."
38. Verifikasi baris 1 berstatus `error`
39. Verifikasi baris 1 tidak berstatus `duplicate`
40. Verifikasi sel First Name baris 1 berborder `danger`
41. Verifikasi Error Summary Callout memuat "First Name: Max. 120 characters" dengan badge "1 row"
42. Verifikasi Staging Metric Cards: Total Rows 1 (Active), Ready to Import 0, Errors 1, Duplicates 0 (Disabled)

### TC-GS-IMPORT-857: Dua baris Email sama, baris terbawah error pada First Name

43. Tunggu toast lama hilang otomatis; reset draft User Login Client C lewat skrip reset, lalu muat ulang halaman
44. Klik `[Upload File]`
45. Pilih berkas `user-login-dup-email-longname.csv` pada file picker
46. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
47. Verifikasi baris 1 berstatus `pending`
48. Verifikasi baris 1 tidak berstatus `duplicate`
49. Verifikasi baris 2 berstatus `error`
50. Verifikasi Error Summary Callout memuat "First Name: Max. 120 characters" dengan badge "1 row"
51. Verifikasi Staging Metric Cards: Total Rows 2 (Active), Ready to Import 1, Errors 1, Duplicates 0 (Disabled)

### TC-GS-IMPORT-837: Email terdaftar dengan Division tidak ditemukan (duplicate, bukan error)

52. Tunggu toast lama hilang otomatis; reset draft User Login Client C lewat skrip reset, lalu muat ulang halaman
53. Klik `[Upload File]`
54. Pilih berkas `user-login-dup-notfound.csv` pada file picker
55. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
56. Verifikasi modal Column Mapping tertutup
57. Verifikasi muncul toast: "Success, row has been added."
58. Verifikasi Staging Table menampilkan 2 baris
59. Verifikasi badge Status baris 1 bertuliskan `pending`
60. Verifikasi badge Status baris 2 bertuliskan `duplicate`
61. Arahkan kursor ke badge Status baris 2
62. Verifikasi tooltip pada badge Status baris 2: "Email already exists. This row will be skipped automatically."
63. Verifikasi Error Summary Callout tidak tampil
64. Verifikasi Staging Metric Cards: Total Rows 2 (Active), Ready to Import 1, Errors 0 (Disabled), Duplicates 1

### TC-GS-IMPORT-848: Unit Name sama dengan sistem walau Symbol melanggar batas

65. Tunggu toast lama hilang otomatis; pilih Sub-Tab Measurement; reset draft Measurement Client C lewat skrip reset, lalu muat ulang halaman
66. Klik `[Upload File]`
67. Pilih berkas `measurement-dup-symbol.csv` pada file picker
68. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
69. Verifikasi modal Column Mapping tertutup
70. Verifikasi muncul toast: "Success, row has been added."
71. Verifikasi baris 1 berstatus `duplicate`
72. Verifikasi baris 1 tidak berstatus `error`
73. Arahkan kursor ke badge Status baris 1
74. Verifikasi tooltip pada badge Status: "Unit name already exists. This row will be skipped automatically."
75. Verifikasi Error Summary Callout tidak tampil
76. Verifikasi Error Summary Callout tidak memuat baris pesan "Symbol: Max. 10 characters"
77. Verifikasi Staging Metric Cards: Total Rows 1 (Active), Ready to Import 0, Errors 0 (Disabled), Duplicates 1
78. Verifikasi sel Symbol baris 1 tidak berborder `danger`
79. Verifikasi sel Symbol baris 1 tidak menampilkan pesan
80. Verifikasi baris `duplicate` hanya menampilkan badge Status dan sorotan warning

### TC-GS-IMPORT-849: Division Name sama dengan sistem walau Code berisi karakter terlarang

81. Tunggu toast lama hilang otomatis; pilih Sub-Tab Division; reset draft Division Client C lewat skrip reset, lalu muat ulang halaman
82. Klik `[Upload File]`
83. Pilih berkas `division-dup-badcode.csv` pada file picker
84. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
85. Verifikasi modal Column Mapping tertutup
86. Verifikasi muncul toast: "Success, row has been added."
87. Verifikasi baris 1 berstatus `duplicate`
88. Verifikasi baris 1 tidak berstatus `error`
89. Arahkan kursor ke badge Status baris 1
90. Verifikasi tooltip pada badge Status: "Division name already exists. This row will be skipped automatically."
91. Verifikasi Error Summary Callout tidak tampil
92. Verifikasi Error Summary Callout tidak memuat baris pesan "Code contains invalid characters"
93. Verifikasi Staging Metric Cards: Total Rows 1 (Active), Ready to Import 0, Errors 0 (Disabled), Duplicates 1
94. Verifikasi sel Code baris 1 tidak berborder `danger`
95. Verifikasi sel Code baris 1 tidak menampilkan pesan
96. Verifikasi baris `duplicate` hanya menampilkan badge Status dan sorotan warning

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional (AI mock mode normal adalah default, bukan objek uji).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec berisi 96 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik presedensi status, tiap blok berdiri sendiri dengan reset draft dan unggah sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 11, 20, 32, 43, 52, 65, dan 81 (menunggu toast, pemilihan Sub-Tab, reset draft, muat ulang) menjalankan Precondition "Client C tanpa draft Tab X (fixture direset sebelum TC, Kontrak Fixture R1)".
- Asersi "tidak tampil" atau "tidak memuat" pada langkah 8, 18, 29, 39, 48, 63, 72, 75, 76, 91, 92 didahului baris Staging Table tampil dengan status terverifikasi pada surface yang sama (anchor positif, butir 2 bagian 8b).
- Pembagian TC lintas spec: TC-GS-IMPORT-861 sampai 864 (emoji) ada di spec 089.
- Temuan untuk QA:
  - ID ganda: `TC-GS-IMPORT-871` dipakai dua kali di `tc-import.md` (baris 938 Code Division identik, baris 1080 tab ditutup melepas kunci) dengan isi berbeda; spec ini memakai `871@L938`. TC tidak diubah.
  - TC-GS-IMPORT-189 judul dan Expected b menyebut badge baris 1 `error` (bukan `duplicate`) tanpa menyebut pesan error Code pada Callout; spec mengikuti Expected TC dan tidak mengasersi isi Callout.
  - Post Condition tiap TC (isi draft, direset sebelum TC berikutnya) tidak punya langkah observasi dan padanan Expected-nya sudah diasersi; tidak diasersi terpisah (S-01).
  - Mekanisme skrip reset draft per Sub-Tab dan mock AI D-40 tidak didefinisikan sebagai endpoint di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
