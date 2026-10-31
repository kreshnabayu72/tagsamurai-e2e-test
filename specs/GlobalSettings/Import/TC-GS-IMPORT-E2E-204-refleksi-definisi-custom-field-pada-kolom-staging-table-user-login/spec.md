---
id: TC-GS-IMPORT-E2E-204-refleksi-definisi-custom-field-pada-kolom-staging-table-user-login
title: "Refleksi definisi Custom Field pada kolom Staging Table User Login: rename, ubah tipe, Decimal Places, nonaktif, aktif kembali, hapus"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-504
  - TC-GS-IMPORT-505
  - TC-GS-IMPORT-506
  - TC-GS-IMPORT-507
  - TC-GS-IMPORT-508
  - TC-GS-IMPORT-514
coverage:
  web: automated
---

# Refleksi definisi Custom Field pada kolom Staging Table User Login: rename, ubah tipe, Decimal Places, nonaktif, aktif kembali, hapus

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memutasi Custom Field Client A (state global) dan memulihkannya (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC2_PASSWORD` (nama env baru). Sesi API mengubah definisi Custom Field di Custom Field User; klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > User Login Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-05: draft User Login 8 baris `pending` dari `user-login-8.csv` pada Client A (Shift `Siang` pada Row # 1 dan 2, `Pagi` pada Row # 3, kosong pada Row # 4 sampai 8; Overtime Hours `1.25` pada Row # 4), disiapkan lewat skrip seed dan dibuat ulang sebelum tiap TC (Kontrak Fixture R2).
- Custom Field Client A (Pre-setup, Optional, Active): Shift (Dropdown Pagi/Siang/Malam), Shift Notes (Text Area), Overtime Hours (Numeric 2 desimal), Emergency Phone (Phone), Join Date (Date); Old Badge nonaktif. Nama literal dipakai (pengecualian S-12 butir (ii): nama field menentukan teks pesan error dan header kolom).
- Urutan TC: 504, 505, 514, 506, 508, 507 (hapus paling akhir). Pemulihan Custom Field dilakukan sebagai langkah aksi di akhir tiap blok (Kontrak Fixture R2) dan oleh hook `after` sebagai cadangan.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): nama `Shift` dipulihkan, tipe `Overtime Hours` dipulihkan ke Numeric dengan Decimal Places 2, Custom Field `Shift` diaktifkan dan dibuat ulang bila dihapus (Dropdown Pagi/Siang/Malam, Optional, Active), draft User Login Client A dipulihkan ke D-05.
- Kemampuan teknis: skrip seed D-05; sesi API Admin kedua.
- State global: Custom Field Client A (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Rename Custom Field (TC-GS-IMPORT-504)

1. Admin kedua Client A (sesi API) mengganti nama Custom Field `Shift` menjadi `Work Shift` hingga tersimpan
2. Tekan `F5` pada halaman Import
3. Verifikasi header kolom Custom Field menjadi `Work Shift`
4. Verifikasi sel Row # 1 dan 2 tetap bernilai `Siang`
5. Verifikasi Staging Metric Cards tetap Total Rows 8, Ready to Import 8, Errors 0, Duplicates 0
6. Pulihkan: Admin kedua mengganti nama kembali menjadi `Shift`, buat ulang draft D-05, muat ulang halaman

### Ubah tipe data (TC-GS-IMPORT-505)

7. Admin kedua Client A (sesi API) mengganti tipe Custom Field `Overtime Hours` dari Numeric ke Date hingga tersimpan
8. Tekan `F5` pada halaman Import
9. Verifikasi Row # 4 (`1.25`) berstatus `error`
10. Verifikasi Error Summary Callout memuat `Overtime hours must be a valid date` dengan badge "1 row"
11. Verifikasi Staging Metric Cards: Ready to Import 7, Errors 1
12. Tekan `F5` sekali lagi
13. Verifikasi Staging Metric Cards tetap Ready to Import 7 dan Errors 1
14. Pulihkan: Admin kedua mengembalikan tipe `Overtime Hours` ke Numeric dengan Decimal Places 2, buat ulang draft D-05, muat ulang halaman

### Ganti Decimal Places (TC-GS-IMPORT-514)

15. Admin kedua Client A (sesi API) mengganti Decimal Places Custom Field `Overtime Hours` dari 2 menjadi 1 hingga tersimpan
16. Tekan `F5` pada halaman Import
17. Verifikasi Row # 4 (`1.25`) berstatus `error`
18. Verifikasi Staging Metric Cards: Ready to Import 7, Errors 1
19. Verifikasi Error Summary Callout memuat `Overtime hours must have at most 1 decimal place` dengan badge "1 row"
20. Pulihkan: Admin kedua mengembalikan Decimal Places `Overtime Hours` ke 2, buat ulang draft D-05, muat ulang halaman

### Nonaktifkan Custom Field (TC-GS-IMPORT-506)

21. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
22. Tekan `F5` pada halaman Import
23. Verifikasi kolom Shift tetap tampil tanpa lencana
24. Verifikasi Banner Custom Field tampil dengan teks "Shift is deactivated. Its values stay hidden on users until it is activated."
25. Verifikasi Banner Custom Field bersifat severity warning
26. Verifikasi Banner Custom Field hanya memuat tombol `[×]`
27. Verifikasi Staging Metric Cards tetap Ready to Import 8 dan Errors 0
28. Klik `⋯` pada Row # 1 lalu pilih Edit
29. Verifikasi sesi Edit Baris dimulai
30. Verifikasi sel Shift pada Row # 1 menjadi Select pencarian yang dapat disunting seperti field Active
31. Pulihkan: klik `[Cancel]`, Admin kedua mengaktifkan kembali Custom Field `Shift`, buat ulang draft D-05, muat ulang halaman

### Aktif kembali (TC-GS-IMPORT-508)

32. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
33. Tekan `F5` pada halaman Import
34. Verifikasi kolom Shift tampil tanpa lencana
35. Verifikasi Banner Custom Field Deactivated tampil
36. Admin kedua Client A (sesi API) mengaktifkan kembali Custom Field `Shift` hingga tersimpan
37. Tekan `F5` pada halaman Import
38. Verifikasi Banner Custom Field tidak tampil
39. Verifikasi sel Shift pada Row # 1 dan 2 tetap bernilai `Siang`
40. Klik `⋯` pada Row # 1 lalu pilih Edit
41. Verifikasi sel Shift pada Row # 1 menjadi Select pencarian yang dapat disunting
42. Klik `[Cancel]` tanpa mengubah nilai
43. Verifikasi sesi edit berakhir tanpa dialog
44. Pulihkan: buat ulang draft D-05, muat ulang halaman

### Hapus Custom Field (TC-GS-IMPORT-507)

45. Admin kedua Client A (sesi API) menghapus Custom Field `Shift` hingga tersimpan
46. Tekan `F5` pada halaman Import
47. Verifikasi kolom Shift tidak tampil di Staging Table
48. Verifikasi Banner Custom Field tampil dengan teks "Shift has been deleted. Its values will not be imported."
49. Verifikasi Banner Custom Field bersifat severity warning
50. Verifikasi Banner Custom Field hanya memuat tombol `[×]`
51. Verifikasi Staging Metric Cards tetap Ready to Import 8 dan Errors 0
52. Klik `⋯` pada Row # 1 lalu pilih Edit
53. Verifikasi sesi Edit Baris dimulai
54. Verifikasi Row # 1 tidak memuat sel Shift
55. Pulihkan: klik `[Cancel]`, Admin kedua membuat ulang Custom Field `Shift` (Dropdown Pagi/Siang/Malam, Optional, Active), buat ulang draft D-05

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 55 langkah, di atas 35 langkah. Alasan: enam blok berpola sama (mutasi definisi Custom Field lewat sesi API, F5, baca Staging Table) pada satu Sub-Tab dan satu dataset D-05; tiap blok berdiri sendiri dan dipulihkan eksplisit (langkah 6, 14, 20, 31, 44, 55), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- P-2: Admin kedua hanya memicu perubahan definisi Custom Field lewat sesi API; hasil diasersi hanya di sesi admin pertama.
- Langkah 6, 14, 20, 31, 44, dan 55 adalah langkah pemulihan tanpa `Verifikasi` (S-09); hook `after` adalah cadangan.
- Langkah 36 dan 37 di blok TC-GS-IMPORT-508 adalah bagian TC (aktif kembali), bukan pemulihan.
- Urutan 504, 505, 514, 506, 508, 507 menempatkan penghapusan (TC-507) paling akhir.
- Temuan untuk QA:
  - TC-GS-IMPORT-514 Precondition d ("Belum ada nilai User tercommit untuk Custom Field `Overtime Hours`") tidak punya langkah observasi; tidak diasersi.
  - TC-GS-IMPORT-504 sampai 514 mengubah Custom Field Client A lewat Admin kedua tanpa menyebut mekanismenya; spec memakai sesi API Admin kedua (kemampuan disediakan tim FE/BE).
  - Pemulihan tipe `Overtime Hours` dari Date ke Numeric dan pembuatan ulang Custom Field `Shift` yang dihapus tidak dijelaskan di TC (Kontrak Fixture R2 hanya menyatakan "dipulihkan ke kondisi Pre-setup"); pembuatan ulang menghasilkan Custom Field baru dan mekanismenya disediakan tim FE/BE.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
