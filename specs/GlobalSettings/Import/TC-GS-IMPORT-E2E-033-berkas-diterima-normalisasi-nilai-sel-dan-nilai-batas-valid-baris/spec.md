---
id: TC-GS-IMPORT-E2E-033-berkas-diterima-normalisasi-nilai-sel-dan-nilai-batas-valid-baris
title: "Berkas Diterima: Normalisasi Nilai Sel dan Nilai Batas Valid (Baris Kosong, Numeric, Phone, Date, Dropdown, XLSX Non-Text, Access, dan Kolom Access pada Non Login)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-128
  - TC-GS-IMPORT-565
  - TC-GS-IMPORT-618
  - TC-GS-IMPORT-619
  - TC-GS-IMPORT-620
coverage:
  web: automated
---

# Berkas Diterima: Normalisasi Nilai Sel dan Nilai Batas Valid (Baris Kosong, Numeric, Phone, Date, Dropdown, XLSX Non-Text, Access, dan Kolom Access pada Non Login)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data: Client C tanpa draft Tab Brand, User Login, dan User Non Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager` (Pre-setup, Kontrak Fixture R4); User Login aktif `rina.admin.c@example.com` (Pre-setup); produk organisasi Global Settings dan Fixed Asset; Custom Field Active Shift (Dropdown Pagi/Siang/Malam), Overtime Hours (Numeric 2 desimal), Emergency Phone (Phone), Join Date (Date). Zona waktu Client C dipakai untuk tanggal relatif hari uji; tim FE/BE menyiapkan berkas per run.
- Berkas fixture D-07 (isi literal; kolom standar User Login mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,`, angka pada Email dan Employee ID mengikuti nomor baris data; kolom standar User Non Login mengikuti pola `Siti,Rahayu,siti.rahayu2@example.com,Engineering,,,rina.admin.c@example.com,`):
  - `brand-blank-rows.csv`: header `Brand Name,Catatan`; baris data 1 `Acme Corp,A`; baris data 2 `,` (kosong sepenuhnya); baris data 3 `Nikon,B`; satu baris kosong di akhir berkas.
  - `user-login-cf-valid-edges.csv`: header `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period,Shift,Shift Notes,Overtime Hours,Emergency Phone,Join Date`; 10 baris; kolom Custom Field lain kosong; Overtime Hours baris 1 `.5`, baris 2 `5.`, baris 3 `-0`, baris 4 `007.5`, baris 5 `123456789012345` (tepat 15 digit), baris 6 `1234567890123.45` (13 digit bulat + 2 desimal); Emergency Phone baris 7 `+62 8123` (tepat 4 digit setelah kode negara), baris 8 `+62812345678901234` (tepat 15 digit tanpa spasi); Join Date baris 9 15 Maret tahun lalu (YYYY-MM-DD); Shift baris 10 `siang` (huruf kecil).
  - `user-login-xlsx.xlsx`: sheet pertama header `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period,Overtime Hours,Join Date`; 1 baris: Budi / Setiawan / budi.setiawan1@example.com / Engineering / Finance Manager / Employee ID sel bertipe Number bernilai 42 (tampil `42`) / Global Settings / Active Period sel bertipe Date 30 hari setelah hari ini (format tampilan YYYY-MM-DD) / Overtime Hours sel bertipe Number bernilai 1.5 berformat tampilan dua desimal (tampil `1.50`) / Join Date sel bertipe Date 15 Maret tahun lalu (format tampilan YYYY-MM-DD); sheet kedua berisi teks `abaikan`.
  - `user-login-access-norm.csv`: header `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period`; 3 baris; Access baris 1 `  global settings ; FIXED ASSET  `, baris 2 `Fixed Asset;;Global Settings;`, baris 3 `Fixed Asset;fixed asset`.
  - `user-non-login-with-access.csv`: header `First Name,Last Name,Email,Division,Position,Employee ID,Represented By,Active Period,Access`; 2 baris; kolom `Access` berisi `Payroll` pada kedua baris.
- Reset dan cleanup: tiap blok membuat draft pada Client C; draft dibuang (langkah reset eksplisit) sebelum blok yang memakai Sub-Tab yang sama (S-09) dan di hook `after`; tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker dengan berkas XLSX bertipe sel Number/Date; skrip reset draft; penyiapan berkas dengan tanggal relatif hari uji.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-565: Baris berkas yang seluruh selnya kosong diabaikan

1. Klik `[Upload File]`
2. Pilih berkas `brand-blank-rows.csv` di file picker
3. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
4. Verifikasi modal tertutup tanpa Error Banner
5. Verifikasi muncul toast "Success, row has been added."
6. Perhatikan Staging Table dan Staging Metric Cards
7. Verifikasi Staging Table menampilkan 2 baris (`Acme Corp` dan `Nikon`) berstatus `pending`
8. Verifikasi tidak ada pesan `Brand name must not be empty` untuk baris kosong sepenuhnya
9. Verifikasi Staging Metric Cards: Total Rows 2 (Active), Ready to Import 2, Errors 0 (Disabled), Duplicates 0 (Disabled)
10. Buang draft Brand Client C (reset ke tanpa draft, Kontrak Fixture R1)

### TC-GS-IMPORT-618: Nilai Custom Field Numeric, Phone, Date, dan Dropdown di sisi valid batas diterima

11. Klik Sub-Tab User Login
12. Klik `[Upload File]`
13. Pilih berkas `user-login-cf-valid-edges.csv` di file picker
14. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
15. Verifikasi modal tertutup
16. Verifikasi muncul toast "Success, row has been added."
17. Verifikasi tidak ada Error Banner pada Modal Column Mapping
18. Perhatikan Staging Table, Error Summary Callout, dan Staging Metric Cards
19. Verifikasi Staging Table menampilkan 10 baris berstatus `pending`
20. Verifikasi Error Summary Callout tidak tampil
21. Verifikasi Staging Metric Cards: Total Rows 10 (Active), Ready to Import 10, Errors 0 (Disabled), Duplicates 0 (Disabled)
22. Buang draft User Login Client C (reset ke tanpa draft, Kontrak Fixture R1)

### TC-GS-IMPORT-619: Sel XLSX non-Text dibaca sebagai teks tampilannya dan sheet lain diabaikan

23. Klik `[Upload File]`
24. Pilih berkas `user-login-xlsx.xlsx` di file picker
25. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
26. Verifikasi modal tertutup
27. Verifikasi muncul toast "Success, row has been added."
28. Perhatikan baris pada Staging Table dan Error Summary Callout
29. Verifikasi Staging Table menampilkan 1 baris berstatus `pending`
30. Verifikasi sel Employee ID menampilkan `42`
31. Verifikasi sel Overtime Hours menampilkan `1.50`
32. Verifikasi sel Active Period menampilkan tanggal 30 hari setelah hari uji (zona waktu Client C) dalam format YYYY-MM-DD
33. Verifikasi sel Join Date menampilkan 15 Maret tahun lalu (tahun hari uji dikurangi 1) dalam format YYYY-MM-DD
34. Verifikasi Error Summary Callout tidak tampil
35. Verifikasi Staging Metric Cards: Total Rows 1 (Active), Ready to Import 1, Errors 0 (Disabled), Duplicates 0 (Disabled)
36. Buang draft User Login Client C (reset ke tanpa draft, Kontrak Fixture R1)

### TC-GS-IMPORT-620: Nilai Access dinormalisasi

37. Klik `[Upload File]`
38. Pilih berkas `user-login-access-norm.csv` di file picker
39. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
40. Verifikasi modal tertutup
41. Verifikasi muncul toast "Success, row has been added."
42. Verifikasi tidak ada Error Banner pada Modal Column Mapping
43. Perhatikan Staging Table, Error Summary Callout, dan Staging Metric Cards
44. Verifikasi Staging Table menampilkan 3 baris berstatus `pending`
45. Verifikasi Error Summary Callout tidak tampil
46. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled)
47. Verifikasi sel Access Row # 1 menampilkan `Global Settings;Fixed Asset`
48. Verifikasi sel Access Row # 2 menampilkan `Global Settings;Fixed Asset`
49. Verifikasi sel Access Row # 3 menampilkan `Fixed Asset`

### TC-GS-IMPORT-128: Kolom Access pada berkas User Non Login tidak masuk Target Attribute dan nilainya tidak divalidasi

50. Klik Sub-Tab User Non Login
51. Klik `[Upload File]`
52. Pilih berkas `user-non-login-with-access.csv` di file picker
53. Perhatikan daftar Target Attribute pada Modal Column Mapping
54. Verifikasi daftar Target Attribute memuat atribut `First Name` dan `Represented By`
55. Verifikasi daftar Target Attribute tidak memuat atribut Access
56. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
57. Verifikasi modal tertutup
58. Verifikasi muncul toast "Success, row has been added."
59. Verifikasi Staging Table menampilkan 2 baris berstatus `pending`
60. Verifikasi Staging Table tanpa kolom Access
61. Verifikasi Error Summary Callout tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 565 (Brand), 618, 619, 620 (User Login), 128 (User Non Login). Urutan menyimpang dari urutan angka TC supaya blok pada Sub-Tab yang sama berurutan dan draft dibuang sebelum blok berikutnya (langkah 10, 22, 36); draft TC-GS-IMPORT-620 dan 128 dibuang hook `after`.
- Alasan di atas sekitar 35 langkah (61 langkah): satu topik (berkas diterima dengan nilai sel yang dinormalisasi atau di sisi valid batas) pada satu client; tiap blok membuat draft sendiri dan berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 18, 28, 43, 53 (mengamati sesuai Langkah Uji TC), langkah 10, 22, 36 (reset draft), langkah 11 dan 50 (pindah Sub-Tab).
- Langkah 54 (`Verifikasi` daftar Target Attribute memuat atribut `First Name` dan `Represented By`) adalah asersi tambahan di luar Expected TC: anchor positif untuk absence atribut Access pada langkah 55 (8b butir 2, S-03).
- Temuan untuk QA:
  - TC-GS-IMPORT-620 dan TC-GS-IMPORT-128 tidak menyebut Row # tempat nilai diamati selain Row # 1 sampai 3 (620); spec mengikuti Expected.
  - Tanggal relatif hari uji (TC-GS-IMPORT-619) bergantung zona waktu Client C; dekat tengah malam nilai dapat berbeda antar run. Berkas disiapkan tim FE/BE per run.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nama data literal tanpa suffix `{runId}`; keunikan dijaga lewat reset draft.
