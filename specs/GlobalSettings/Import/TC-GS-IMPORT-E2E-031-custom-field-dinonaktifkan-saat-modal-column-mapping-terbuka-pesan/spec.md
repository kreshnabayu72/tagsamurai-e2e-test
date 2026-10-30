---
id: TC-GS-IMPORT-E2E-031-custom-field-dinonaktifkan-saat-modal-column-mapping-terbuka-pesan
title: "Custom Field Dinonaktifkan Saat Modal Column Mapping Terbuka: Pesan Level-Kolom (User Login dan User Non Login, Termasuk Kombinasi Per-Baris)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-123
  - TC-GS-IMPORT-133
  - TC-GS-IMPORT-617
  - TC-GS-IMPORT-622
coverage:
  web: automated
---

# Custom Field Dinonaktifkan Saat Modal Column Mapping Terbuka: Pesan Level-Kolom (User Login dan User Non Login, Termasuk Kombinasi Per-Baris)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena spec menonaktifkan Custom Field `Shift` Client C (state global); lihat `suite.md`.
- Akun aktor:
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup): satu-satunya sesi UI. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net` (Pre-setup): hanya sesi API sebagai pemicu penonaktifan Custom Field Shift, tanpa sesi UI dan tanpa asersi di sesi itu (P-2); password `Spectra.env.GS_CLIENTC_TC2_PASSWORD` (env baru). Mekanisme "fixture API" penonaktifan dan pengaktifan kembali Custom Field disediakan tim FE/BE (S-13).
  - Hook `after` mengembalikan sesi UI ke Total Control Client A dan memastikan Custom Field Shift Client C Active kembali walau spec gagal di tengah. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data:
  - Client C tanpa draft Tab User Login dan User Non Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager` (Pre-setup, Kontrak Fixture R4); User Login aktif `rina.admin.c@example.com` (Pre-setup); Custom Field `Shift` (Dropdown; opsi Pagi, Siang, Malam) Active di Client C. Tidak ada draft yang tercipta karena Confirm Mapping ditolak.
  - Berkas fixture D-07 (isi literal): baris valid User Login mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,` (angka pada Email dan Employee ID mengikuti nomor baris data); baris valid User Non Login mengikuti pola `Siti,Rahayu,siti.rahayu2@example.com,Engineering,,,rina.admin.c@example.com,` (angka pada Email mengikuti nomor baris data).
    - `user-login-shift.csv`: header `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period,Shift`; 3 baris; Shift `Siang` pada baris #1-#2 dan `Pagi` pada baris #3.
    - `user-login-shift-blank.csv`: header sama; 3 baris; kolom Shift ada tetapi kosong pada ketiga baris.
    - `user-login-shift-mixed.csv`: header sama; 5 baris; baris ke-3 Email `x@`, baris ke-5 First Name kosong; Shift `Siang` pada baris #1-#2 dan `Pagi` pada baris #3.
    - `user-non-login-shift-inactive.csv`: header `First Name,Last Name,Email,Division,Position,Employee ID,Represented By,Active Period,Shift`; 3 baris; Shift `Pagi` pada baris #1-#2.
- Pemulihan: sesudah tiap blok, Custom Field Shift diaktifkan kembali lewat fixture (R2); hook `after` memastikannya.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; fixture API penonaktifan dan pengaktifan Custom Field (sesi API Admin kedua Client C, disediakan tim FE/BE); skrip reset draft.
- State global: status Custom Field Shift Client C (dipulihkan di langkah dan hook `after`).

## Test Steps

### TC-GS-IMPORT-123: Custom Field dinonaktifkan selagi Modal Column Mapping terbuka menolak Confirm Mapping

1. Klik Sub-Tab User Login
2. Klik `[Upload File]`
3. Pilih berkas `user-login-shift.csv` di file picker
4. Verifikasi dropdown Shift pada Modal Column Mapping terpetakan otomatis ke kolom Shift
5. Admin kedua Client C menonaktifkan Custom Field Shift lewat fixture API (sesi API terpisah) hingga tersimpan, saat Modal Column Mapping masih terbuka
6. Pada Modal Column Mapping klik `[Confirm Mapping]` tanpa mengubah dropdown
7. Verifikasi Modal Column Mapping tetap terbuka
8. Verifikasi Error Banner memuat baris pesan level-kolom `Shift is no longer active and can't be used for import. Please remap this column.`
9. Verifikasi baris pesan itu tidak diikuti nomor baris
10. Verifikasi tidak ada toast
11. Klik `[Cancel]` pada Modal Column Mapping
12. Verifikasi modal tertutup
13. Verifikasi halaman menampilkan Upload Dropzone tanpa Staging Table dan tanpa Unsaved Banner
14. Aktifkan kembali Custom Field Shift lewat fixture API

### TC-GS-IMPORT-133: Hanya pelanggaran level-kolom memakai header yang sama dengan guard pra-konfirmasi

15. Klik `[Upload File]`
16. Pilih berkas `user-login-shift-blank.csv` di file picker
17. Verifikasi dropdown Shift pada Modal Column Mapping terpetakan otomatis ke kolom Shift
18. Admin kedua Client C menonaktifkan Custom Field Shift lewat fixture API (sesi API terpisah) hingga tersimpan, saat Modal Column Mapping masih terbuka
19. Pada Modal Column Mapping klik `[Confirm Mapping]` tanpa mengubah dropdown
20. Verifikasi Error Banner tampil di dalam modal dengan header "The following columns contain errors and cannot be imported:"
21. Verifikasi header tidak memuat jumlah baris yang gagal diimpor maupun angka jumlah baris
22. Verifikasi Error Banner memuat baris pesan `Shift is no longer active and can't be used for import. Please remap this column.`
23. Klik `[Cancel]` pada Modal Column Mapping
24. Verifikasi modal tertutup
25. Verifikasi halaman menampilkan Upload Dropzone
26. Verifikasi tidak ada draft Tab User Login
27. Aktifkan kembali Custom Field Shift lewat fixture API

### TC-GS-IMPORT-622: Pelanggaran per-baris dan level-kolom bersamaan

28. Klik `[Upload File]`
29. Pilih berkas `user-login-shift-mixed.csv` di file picker
30. Verifikasi dropdown Shift pada Modal Column Mapping terpetakan otomatis ke kolom Shift
31. Admin kedua Client C menonaktifkan Custom Field Shift lewat fixture API (sesi API terpisah) hingga tersimpan, saat Modal Column Mapping masih terbuka
32. Pada Modal Column Mapping klik `[Confirm Mapping]` tanpa mengubah dropdown
33. Verifikasi Modal Column Mapping tetap terbuka
34. Verifikasi Error Banner tampil di dalam modal dengan header "2 rows couldn't be imported. Fix the following and upload again:"
35. Verifikasi Error Banner memuat baris pesan `First name must not be empty. 5` dan `Invalid email format. 3`
36. Verifikasi Error Banner memuat baris pesan level-kolom `Shift is no longer active and can't be used for import. Please remap this column.` tanpa nomor baris di belakangnya
37. Klik `[Cancel]` pada Modal Column Mapping
38. Verifikasi modal tertutup
39. Verifikasi halaman menampilkan Upload Dropzone
40. Verifikasi tidak ada draft Tab User Login
41. Aktifkan kembali Custom Field Shift lewat fixture API

### TC-GS-IMPORT-617: Custom Field dinonaktifkan selagi Modal Column Mapping User Non Login terbuka menolak Confirm Mapping

42. Klik Sub-Tab User Non Login
43. Klik `[Upload File]`
44. Pilih berkas `user-non-login-shift-inactive.csv` di file picker
45. Verifikasi dropdown Shift pada Modal Column Mapping terpetakan otomatis ke kolom Shift
46. Admin kedua Client C menonaktifkan Custom Field Shift lewat fixture API (sesi API terpisah) hingga tersimpan, saat Modal Column Mapping masih terbuka
47. Pada Modal Column Mapping klik `[Confirm Mapping]` tanpa mengubah dropdown
48. Verifikasi Modal Column Mapping tetap terbuka
49. Verifikasi Error Banner memuat baris pesan level-kolom `Shift is no longer active and can't be used for import. Please remap this column.` tanpa nomor baris di belakangnya
50. Verifikasi tidak ada toast
51. Klik `[Cancel]` pada Modal Column Mapping
52. Verifikasi modal tertutup
53. Verifikasi halaman menampilkan Upload Dropzone tanpa Staging Table dan tanpa Unsaved Banner
54. Aktifkan kembali Custom Field Shift lewat fixture API

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- P-2: Admin kedua Client C hanya memicu penonaktifan Custom Field Shift lewat sesi API (langkah 5, 18, 31, 46), bukan objek uji; tidak ada sesi UI kedua dan tidak ada asersi di sesi Admin kedua. Pemulihan Custom Field Shift ditulis sebagai langkah eksplisit sesudah tiap blok (langkah 14, 27, 41, 54, S-09); hook `after` sebagai cadangan.
- Urutan TC: 123, 133, 622 (Sub-Tab User Login), lalu 617 (Sub-Tab User Non Login).
- Alasan di atas sekitar 35 langkah (54 langkah): satu topik (penonaktifan Custom Field saat modal terbuka) pada satu client; tiap blok berdiri sendiri dengan berkas dan pemulihan sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Asersi absence "tidak ada toast" (langkah 10, 50) didahului `Verifikasi` Error Banner tampil di modal sebagai anchor positif; "tanpa Staging Table dan tanpa Unsaved Banner" (langkah 13, 53) didahului `Verifikasi` Upload Dropzone tampil pada kalimat yang sama. "Tidak ada draft Tab User Login" (langkah 26, 40) didahului `Verifikasi` Upload Dropzone tampil (langkah 25, 39) sebagai anchor positif; langkah 25 dan 39 adalah asersi tambahan di luar Expected TC (anchor positif untuk absence, 8b butir 2, S-03).
- Temuan untuk QA:
  - TC-GS-IMPORT-123, 133, 617, 622 memakai "fixture API (sesi terpisah)" untuk menonaktifkan Custom Field tanpa mendefinisikan mekanismenya di TC, PRD, atau LLD; disediakan tim FE/BE tanpa endpoint karangan (S-13). Password akun Admin kedua Client C tidak ada di TC; env `GS_CLIENTC_TC2_PASSWORD` baru.
  - TC-GS-IMPORT-133 judulnya menyebut "kolom Shift tanpa nilai pada semua baris"; Expected memverifikasi header tanpa jumlah baris dan satu pesan level-kolom. Spec mengikuti Expected.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
