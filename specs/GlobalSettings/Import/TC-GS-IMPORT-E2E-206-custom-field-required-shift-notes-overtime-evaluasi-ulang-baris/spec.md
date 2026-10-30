---
id: TC-GS-IMPORT-E2E-206-custom-field-required-shift-notes-overtime-evaluasi-ulang-baris
title: "Custom Field Required (Shift Notes, Overtime): evaluasi ulang baris, pemulihan lewat Edit, Edit this page, callout per kategori"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-509
  - TC-GS-IMPORT-941
  - TC-GS-IMPORT-942
  - TC-GS-IMPORT-943
coverage:
  web: automated
---

# Custom Field Required (Shift Notes, Overtime): evaluasi ulang baris, pemulihan lewat Edit, Edit this page, callout per kategori

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memutasi Custom Field Client A (state global) dan memulihkannya (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC2_PASSWORD` (nama env baru). Sesi API menjadikan Custom Field Required; klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > User Login Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-05: draft User Login 8 baris `pending` dari `user-login-8.csv` pada Client A (Shift `Siang` pada Row # 1 dan 2, `Pagi` pada Row # 3, kosong pada Row # 4 sampai 8; Overtime Hours `1.25` pada Row # 4; Custom Field Active `Shift Notes` (Text Area) Optional dan kosong pada seluruh baris), disiapkan lewat skrip seed dan dibuat ulang sebelum tiap TC (Kontrak Fixture R2).
- Nilai uji: Shift Notes Row # 1 `Catatan shift pagi` (TC-GS-IMPORT-941); Shift Notes Row # 1 sampai 8 `Catatan 1` sampai `Catatan 8` (TC-GS-IMPORT-942).
- Custom Field Client A (Pre-setup, Optional, Active): Shift, Shift Notes, Overtime Hours (Numeric 2 desimal), Emergency Phone, Join Date. Nama literal dipakai (pengecualian S-12 butir (ii): nama field menentukan teks pesan error `Shift notes must not be empty` dan `Overtime hours must not be empty`).
- Urutan TC: 509, 941, 942, 943 (TC-943 menghapus baris di akhir). Pemulihan Custom Field ke Optional dan draft D-05 dilakukan sebagai langkah aksi di akhir tiap blok (Kontrak Fixture R2) dan oleh hook `after` sebagai cadangan.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): `Shift Notes` dan `Overtime Hours` dipulihkan ke Optional, draft User Login Client A dipulihkan ke D-05.
- Kemampuan teknis: skrip seed D-05; sesi API Admin kedua.
- State global: Custom Field Client A (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Shift Notes Required, Save diblokir (TC-GS-IMPORT-509)

1. Admin kedua Client A (sesi API) menjadikan Custom Field `Shift Notes` Required hingga tersimpan
2. Tekan `F5` pada halaman Import
3. Verifikasi seluruh 8 baris berstatus `error`
4. Verifikasi sel `Shift Notes` tiap baris kosong dengan border `danger`
5. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 0, Errors 8
6. Verifikasi Error Summary Callout memuat `Shift notes must not be empty` dengan badge "8 rows"
7. Klik row action `⋯` pada Row # 1 lalu Edit
8. Tambahkan `X` di akhir nilai Last Name pada Row # 1
9. Klik `[Save]`
10. Verifikasi `[Save]` ditolak dan sesi edit tetap terbuka
11. Verifikasi sel Shift Notes Row # 1 berborder `danger`
12. Klik `[Cancel]`
13. Klik `[Discard]` pada Dialog Discard Changes
14. Verifikasi sesi edit berakhir
15. Verifikasi nilai Last Name Row # 1 tidak berubah
16. Pulihkan: Admin kedua mengembalikan `Shift Notes` ke Optional, buat ulang draft D-05, muat ulang halaman

### Pulih lewat Edit (TC-GS-IMPORT-941)

17. Admin kedua Client A (sesi API) menjadikan Custom Field `Shift Notes` Required hingga tersimpan
18. Tekan `F5` pada halaman Import
19. Klik row action `⋯` pada Row # 1 lalu Edit
20. Isi sel `Shift Notes` Row # 1 dengan `Catatan shift pagi`
21. Klik `[Save]`
22. Verifikasi muncul toast sukses: "Success, row has been updated."
23. Verifikasi Row # 1 berstatus `pending`
24. Verifikasi Row # 2 sampai 8 tetap `error`
25. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 1, Errors 7
26. Verifikasi Error Summary Callout memuat `Shift notes must not be empty` dengan badge "7 rows"
27. Pulihkan: Admin kedua mengembalikan `Shift Notes` ke Optional, buat ulang draft D-05, muat ulang halaman

### Edit this page mengisi seluruh baris (TC-GS-IMPORT-942)

28. Admin kedua Client A (sesi API) menjadikan Custom Field `Shift Notes` Required hingga tersimpan
29. Tekan `F5` pada halaman Import
30. Klik toggle `Edit this page`
31. Isi sel `Shift Notes` pada Row # 1 sampai 8 dengan `Catatan 1` sampai `Catatan 8`
32. Klik `[Save]`
33. Verifikasi muncul toast sukses: "Success, row has been updated."
34. Verifikasi seluruh 8 baris berstatus `pending`
35. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 8, Errors 0
36. Verifikasi Error Summary Callout tidak tampil
37. Pulihkan: Admin kedua mengembalikan `Shift Notes` ke Optional, buat ulang draft D-05, muat ulang halaman

### Callout per Custom Field Required dan Delete All Rows (TC-GS-IMPORT-943)

38. Admin kedua Client A (sesi API) menjadikan Custom Field `Shift Notes` dan `Overtime Hours` Required hingga tersimpan
39. Tekan `F5` pada halaman Import
40. Verifikasi seluruh 8 baris berstatus `error`
41. Verifikasi Error Summary Callout memuat baris pesan `Shift notes must not be empty` dengan badge "8 rows"
42. Verifikasi Error Summary Callout memuat baris pesan `Overtime hours must not be empty` dengan badge "7 rows"
43. Klik `[Delete All Rows]` pada baris pesan `Overtime hours must not be empty`
44. Verifikasi baris dihapus seketika tanpa dialog konfirmasi
45. Verifikasi muncul toast sukses: "Success, row has been deleted."
46. Verifikasi Staging Table hanya memuat Row # 4 (`Overtime Hours` `1.25`) berstatus `error`
47. Verifikasi Staging Metric Cards: Total Rows 1, Ready to Import 0, Errors 1
48. Verifikasi Error Summary Callout hanya memuat `Shift notes must not be empty` dengan badge "1 row"
49. Pulihkan: Admin kedua mengembalikan `Shift Notes` dan `Overtime Hours` ke Optional, buat ulang draft D-05

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 49 langkah, di atas 35 langkah. Alasan: empat blok berpola sama (jadikan Custom Field Required lewat sesi API, F5, baca Staging Table User Login) pada satu Sub-Tab dan satu dataset D-05; tiap blok berdiri sendiri dan dipulihkan eksplisit (langkah 16, 27, 37, 49). TC-GS-IMPORT-943 menghapus baris dan diletakkan paling akhir.
- P-2: Admin kedua hanya memicu perubahan definisi Custom Field lewat sesi API; hasil diasersi hanya di sesi admin pertama.
- Langkah 16, 27, 37, dan 49 adalah langkah pemulihan tanpa `Verifikasi` (S-09); hook `after` adalah cadangan.
- Langkah 16 mengosongkan kondisi setelah `[Discard]` dan memuat ulang draft D-05 sebagai penghubung (S-03).
- Temuan untuk QA:
  - TC-GS-IMPORT-509 mensyaratkan `[Save]` ditolak "selama sel masih kosong" tanpa menyebut pesan atau toast; spec hanya mengasersi sesi edit tetap terbuka dan border `danger`.
  - TC-GS-IMPORT-509 langkah 7-8 memakai `[Cancel]` lalu `[Discard]` untuk menutup edit dirty; konvensi S-08 menutup form dirty lewat `✕`, tetapi TC menetapkan jalur `[Cancel]` pada sesi Edit Baris sehingga spec mengikuti TC.
  - TC-GS-IMPORT-943 Expected c menyebut Row # 4 setelah penghapusan tanpa menjelaskan penomoran ulang (baris pertama tersisa Row # 4 menurut TC).
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
