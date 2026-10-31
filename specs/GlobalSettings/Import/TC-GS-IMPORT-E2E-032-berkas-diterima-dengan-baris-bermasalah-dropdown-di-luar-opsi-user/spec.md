---
id: TC-GS-IMPORT-E2E-032-berkas-diterima-dengan-baris-bermasalah-dropdown-di-luar-opsi-user
title: "Berkas Diterima dengan Baris Bermasalah: Dropdown di Luar Opsi (User Login dan User Non Login), Duplikat, dan Panjang atau Karakter Menjadi Error"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-114
  - TC-GS-IMPORT-130
  - TC-GS-IMPORT-131
  - TC-GS-IMPORT-613
coverage:
  web: automated
---

# Berkas Diterima dengan Baris Bermasalah: Dropdown di Luar Opsi (User Login dan User Non Login), Duplikat, dan Panjang atau Karakter Menjadi Error

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data:
  - Client C tanpa draft Tab User Login, User Non Login, dan Brand (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager` (Pre-setup, Kontrak Fixture R4); Brand `Samsung` ada (Pre-setup); User Login aktif `rina.admin.c@example.com` (Pre-setup); Custom Field `Shift` (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam`.
  - Berkas fixture D-07 (isi literal): `user-login-bad-shift.csv` (header `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period,Shift,Shift Notes,Overtime Hours,Emergency Phone,Join Date`; 3 baris; baris ke-2 Shift `Dini`; kolom Custom Field lain kosong; baris valid mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,`); `user-non-login-bad-shift.csv` (header `First Name,Last Name,Email,Division,Position,Employee ID,Represented By,Active Period,Shift,Shift Notes,Overtime Hours,Emergency Phone,Join Date`; 3 baris; baris ke-2 Shift `Dini`; baris valid mengikuti pola `Siti,Rahayu,siti.rahayu2@example.com,Engineering,,,rina.admin.c@example.com,`); `brand-with-duplicate.csv` (header `Brand Name`; Nikon, Canon, Samsung, Sony, Fujifilm); `brand-overlength-only.csv` (header `Brand Name`; Nikon, Canon, Brand Name 121 karakter `B` diulang 121 kali, Sony, Fujifilm). Angka pada Email dan Employee ID mengikuti nomor baris data.
- Reset dan cleanup: tiap blok membuat draft pada Client C; draft dibuang (langkah reset eksplisit) sebelum blok yang memakai Sub-Tab yang sama (S-09) dan di hook `after`; tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-114: Custom Field Dropdown di luar opsi tidak menolak berkas (User Login)

1. Klik Sub-Tab User Login
2. Klik `[Upload File]`
3. Pilih berkas `user-login-bad-shift.csv` di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Perhatikan Modal Column Mapping, toast, Staging Table, Staging Metric Cards, dan Error Summary Callout
6. Verifikasi Modal Column Mapping tertutup
7. Verifikasi tidak ada Error Banner dan tidak ada penolakan berkas
8. Verifikasi Staging Table menampilkan 3 baris
9. Verifikasi baris #1 dan #3 berstatus `pending`
10. Verifikasi baris #2 berstatus `error`
11. Verifikasi sel Shift baris #2 berborder `danger`
12. Verifikasi sel Shift baris #2 memuat pesan "Dini is not a valid option for shift"
13. Verifikasi Error Summary Callout memuat satu baris pesan "Shift: Invalid option" dengan badge "1 row"
14. Verifikasi Error Summary Callout memuat tombol `[View Data]`, `[Delete All Rows]`, dan `[Create Missing Options]`
15. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 2, Errors 1, Duplicates 0

### TC-GS-IMPORT-613: Custom Field Dropdown di luar opsi pada User Non Login tidak menolak berkas

16. Klik Sub-Tab User Non Login
17. Klik `[Upload File]`
18. Pilih berkas `user-non-login-bad-shift.csv` di file picker
19. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
20. Perhatikan Modal Column Mapping, toast, Staging Table, Staging Metric Cards, dan Error Summary Callout
21. Verifikasi Modal Column Mapping tertutup
22. Verifikasi tidak ada Error Banner dan tidak ada penolakan berkas
23. Verifikasi Staging Table menampilkan 3 baris
24. Verifikasi baris #1 dan #3 berstatus `pending`
25. Verifikasi baris #2 berstatus `error`
26. Verifikasi sel Shift baris #2 berborder `danger`
27. Verifikasi sel Shift baris #2 memuat pesan "Dini is not a valid option for shift"
28. Verifikasi Error Summary Callout memuat satu baris pesan "Shift: Invalid option" dengan badge "1 row"
29. Verifikasi Error Summary Callout memuat tombol `[View Data]`, `[Delete All Rows]`, dan `[Create Missing Options]`
30. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 2, Errors 1, Duplicates 0

### TC-GS-IMPORT-130: Baris duplikat tidak menggugurkan pengunggahan

31. Klik Sub-Tab Brand
32. Klik `[Upload File]`
33. Pilih berkas `brand-with-duplicate.csv` di file picker
34. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
35. Verifikasi modal tertutup
36. Verifikasi muncul toast "Success, row has been added."
37. Perhatikan Staging Table dan Staging Metric Cards
38. Verifikasi Staging Table menampilkan 5 baris
39. Verifikasi baris 3 `Samsung` berstatus `duplicate`
40. Verifikasi 4 baris lainnya berstatus `pending`
41. Verifikasi Staging Metric Cards: Total Rows 5 (Active), Ready to Import 4, Errors 0 (Disabled), Duplicates 1

### TC-GS-IMPORT-131: Pelanggaran panjang dan karakter tidak menolak berkas

42. Buang draft Brand Client C (reset ke tanpa draft, Kontrak Fixture R1) lalu muat ulang halaman Import > Brand
43. Klik `[Upload File]`
44. Pilih berkas `brand-overlength-only.csv` di file picker
45. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
46. Verifikasi modal tertutup tanpa Error Banner
47. Verifikasi muncul toast "Success, row has been added."
48. Perhatikan Staging Table dan Error Summary Callout
49. Verifikasi Staging Table menampilkan 5 baris
50. Verifikasi baris 3 berstatus `error`
51. Verifikasi 4 baris lainnya berstatus `pending`
52. Verifikasi Error Summary Callout memuat satu baris pesan "Brand Name: Max. 120 characters" dengan badge "1 row"
53. Verifikasi Staging Metric Cards: Total Rows 5 (Active), Ready to Import 4, Errors 1, Duplicates 0 (Disabled)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 114, 613 (User Login lalu User Non Login), 130, 131 (Brand). Draft Brand TC-GS-IMPORT-130 dibuang pada langkah 42 sebelum TC-GS-IMPORT-131 yang mensyaratkan Client C tanpa draft Tab Brand (S-09).
- Alasan di atas sekitar 35 langkah (53 langkah): satu topik (berkas diterima dengan baris bermasalah, tanpa penolakan) pada satu client; tiap blok membuat draft sendiri pada Sub-Tab sendiri atau setelah reset sehingga berdiri sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 16, 31 (pindah Sub-Tab), langkah 5, 20, 37, 48 (mengamati sesuai Langkah Uji TC), langkah 42 (reset draft).
- Temuan untuk QA:
  - TC-GS-IMPORT-114 dan 613 menyebut Shift `Dini` dengan pesan "Dini is not a valid option for shift" (huruf kecil `shift`); spec mengikuti teks TC.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nama data literal tanpa suffix `{runId}`; keunikan dijaga lewat reset draft.
