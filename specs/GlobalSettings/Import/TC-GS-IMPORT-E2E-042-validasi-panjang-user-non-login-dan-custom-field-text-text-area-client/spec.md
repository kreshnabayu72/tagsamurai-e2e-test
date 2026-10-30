---
id: TC-GS-IMPORT-E2E-042-validasi-panjang-user-non-login-dan-custom-field-text-text-area-client
title: "Validasi Panjang User Non Login dan Custom Field Text dan Text Area (Client C; Text Client G) serta Nama Akronim Tax ID"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-163
  - TC-GS-IMPORT-164
  - TC-GS-IMPORT-625
  - TC-GS-IMPORT-626
  - TC-GS-IMPORT-627
  - TC-GS-IMPORT-633
  - TC-GS-IMPORT-634
coverage:
  web: automated
---

# Validasi Panjang User Non Login dan Custom Field Text dan Text Area (Client C; Text Client G) serta Nama Akronim Tax ID

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor:
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-164, 633, 634, 625, 626, dan 627. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Total Control Client G (Putri Ananda) `totalControl_automated_qaTeam10@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-163: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTG_TC_PASSWORD` (env baru). Hook `after` mengembalikan sesi ke Total Control Client A.
  - Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data: Client C tanpa draft Tab User Login dan User Non Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager`, User Login aktif `rina.admin.c@example.com`, dan Custom Field Active opsional `Tax ID` (Text) dan `Shift Notes` (Text Area) (Pre-setup, Kontrak Fixture R4). Client G tanpa draft Tab User Login, berisi Division `Engineering`, Position `Finance Manager`, produk Global Settings, dan Custom Field Active Required `Badge Code` (Text) satu-satunya.
- Reset dan cleanup: tiap blok membuat draft pada Client C atau Client G; draft dibuang (langkah reset eksplisit, S-09) sebelum blok berikutnya dan di hook `after`; tidak berasumsi seeding berhasil penuh.
- Berkas fixture D-07 (isi literal; berkas User Login berheader `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period` ditambah kolom Custom Field yang disebut; berkas User Non Login berheader `First Name,Last Name,Email,Division,Position,Employee ID,Represented By,Active Period` ditambah kolom Custom Field yang disebut; baris valid User Login mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,`; baris valid User Non Login mengikuti pola `Siti,Rahayu,siti.rahayu2@example.com,Engineering,,,rina.admin.c@example.com,`; angka pada Email dan Employee ID mengikuti nomor baris data). Email 121 karakter berformat valid: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.example.com`; Email 120 karakter berformat valid: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.example.com`.
- Tabel "Parameter validasi" (satu baris per blok TC pada Client C; langkah per baris identik):

  | TC | Sub-Tab | Berkas dan nilai | Status baris | Sel bermasalah | Error Summary Callout | Staging Metric Cards |
  |---|---|---|---|---|---|---|
  | 164 | User Login | `user-login-cf-ta-361.csv` (kolom tambahan `Shift Notes`): baris ke-2 Shift Notes `N` diulang 361 kali | baris 2 `error`, lain `pending` | sel Shift Notes baris 2 berborder merah dengan ikon penanda merah dan pesan "Max. 360 characters" | satu baris pesan "Shift notes: Max. 360 characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 633 | User Login | `user-login-cf-text-ok.csv` (kolom tambahan `Shift Notes`, `Tax ID`): baris ke-2 Shift Notes `N` diulang 360 kali dan Tax ID `T` diulang 120 kali | 3 baris `pending` | sel Shift Notes dan Tax ID baris 2 tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 634 | User Login | `user-login-cf-acronym.csv` (kolom tambahan `Tax ID`): baris ke-2 Tax ID `T` diulang 121 kali | baris 2 `error`, lain `pending` | sel Tax ID baris 2 berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters" | satu baris pesan "Tax ID: Max. 120 characters" dengan badge "1 row" (akronim `ID` mempertahankan huruf kapital) | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 625 | User Non Login | `user-non-login-len-121.csv` (5 baris data): baris ke-2 First Name `A` x121, baris ke-3 Last Name `S` x121, baris ke-4 Email 121 karakter berformat valid, baris ke-5 Employee ID `E` x121 | baris 2 sampai 5 `error`, baris 1 `pending` | sel First Name baris 2, Last Name baris 3, Email baris 4, dan Employee ID baris 5 masing-masing berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters" | empat baris pesan, masing-masing berbadge "1 row": "First Name: Max. 120 characters", "Last Name: Max. 120 characters", "Email: Max. 120 characters", "Employee ID: Max. 120 characters" | Total Rows 5 (Active), Ready to Import 1, Errors 4, Duplicates 0 (Disabled) |
  | 626 | User Non Login | `user-non-login-len-120.csv` (3 baris data): baris ke-2 First Name `A` x120, Last Name `S` x120, Email 120 karakter berformat valid, Employee ID `E` x120 | 3 baris `pending` | sel First Name, Last Name, Email, dan Employee ID baris 2 tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 627 | User Non Login | `user-non-login-cf-text-len.csv` (kolom tambahan `Shift Notes`, `Tax ID`; 3 baris data): baris ke-2 Shift Notes `N` x361, baris ke-3 Tax ID `T` x121 | baris 2 dan 3 `error`, baris 1 `pending` | sel Shift Notes baris 2 berborder merah dengan ikon penanda merah dan pesan "Max. 360 characters"; sel Tax ID baris 3 berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters" | dua baris pesan, masing-masing berbadge "1 row": "Shift notes: Max. 360 characters" dan "Tax ID: Max. 120 characters" | Total Rows 3 (Active), Ready to Import 1, Errors 2, Duplicates 0 (Disabled) |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; pembacaan gaya border dan ikon sel Staging Table.
- State global: tidak ada yang diubah selain draft Client C dan Client G (dibuang hook).

## Test Steps

### TC-GS-IMPORT-164, 633, 634 (User Login Client C) lalu TC-GS-IMPORT-625, 626, 627 (User Non Login Client C)

Untuk setiap baris tabel "Parameter validasi" (langkah 1 sampai 13; diulang enam kali berurutan: TC 164, 633, 634, 625, 626, 627):

1. Klik Sub-Tab sesuai kolom Sub-Tab
2. Klik `[Upload File]`
3. Pilih berkas pada kolom Berkas di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi modal tertutup
6. Verifikasi muncul toast "Success, row has been added."
7. Perhatikan baris Data Uji pada Staging Table, Staging Metric Cards, dan Error Summary Callout
8. Verifikasi Staging Table menampilkan jumlah baris dengan status sesuai kolom Status baris
9. Verifikasi sel bermasalah sesuai kolom Sel bermasalah
10. Verifikasi Error Summary Callout sesuai kolom Error Summary Callout
11. Verifikasi Staging Metric Cards sesuai kolom Staging Metric Cards
12. Buang draft pada Sub-Tab itu di Client C (reset ke tanpa draft, Kontrak Fixture R1)
13. Muat ulang halaman Import

### TC-GS-IMPORT-163: Custom Field Text lebih dari 120 karakter menjadi error (Client G)

14. Ganti akun: logout dari Total Control Client C
15. Login sebagai Total Control Client G dengan `Spectra.env.GS_CLIENTG_TC_PASSWORD`
16. Buka Import > User Login
17. Klik `[Upload File]`
18. Pilih berkas `user-login-cf-text-121.csv` di file picker (kolom tambahan `Badge Code`; baris ke-2 Badge Code `K` diulang 121 kali; baris lain `BC-1` dan `BC-3`)
19. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
20. Verifikasi modal tertutup
21. Verifikasi muncul toast "Success, row has been added."
22. Perhatikan baris Data Uji pada Staging Table, Staging Metric Cards, dan Error Summary Callout
23. Verifikasi Staging Table menampilkan 3 baris; baris 2 berstatus `error` dan baris lainnya berstatus `pending`
24. Verifikasi sel Badge Code baris 2 berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters"
25. Verifikasi Error Summary Callout memuat satu baris pesan "Badge code: Max. 120 characters" dengan badge "1 row"
26. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled)
27. Buang draft User Login Client G (reset ke tanpa draft, Kontrak Fixture R1)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Langkah 1 sampai 13 diulang enam kali (ekspansi 78 langkah, ditambah langkah 14 sampai 27 menjadi 92); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 1 sampai 13 (konvensi 8b butir 7).
- Urutan TC: 164, 633, 634 (User Login Client C), 625, 626, 627 (User Non Login Client C), lalu 163 (Client G) dengan langkah ganti akun eksplisit (langkah 14 dan 15). Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Alasan di atas sekitar 35 langkah: enam blok homogen satu pola (upload berkas, Confirm Mapping, verifikasi status dan sel), masing-masing dengan draft yang dibuang sesudahnya; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain; blok Client G terpisah di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pindah Sub-Tab), langkah 7 dan 22 (mengamati sesuai Langkah Uji TC), langkah 12, 13, dan 27 (reset draft dan muat ulang, S-09), langkah 14 sampai 16 (ganti akun dan buka tab).
- Temuan untuk QA:
  - TC-GS-IMPORT-163 berada pada Client G sedangkan TC lain pada Client C; ganti akun dilakukan eksplisit.
  - Skrip reset draft Client C dan Client G tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nilai literal tanpa suffix `{runId}`; data hanya masuk draft Staging Table dan dibuang lewat reset.
