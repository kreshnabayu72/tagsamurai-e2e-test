---
id: TC-GS-IMPORT-E2E-205-refleksi-dropdown-option-dan-perubahan-custom-field-pada-seluruh-baris
title: "Refleksi Dropdown option dan perubahan Custom Field pada seluruh baris draft (Save, Remove, Append, pindah Sub-Tab, field baru Optional)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-510
  - TC-GS-IMPORT-511
  - TC-GS-IMPORT-512
  - TC-GS-IMPORT-515
  - TC-GS-IMPORT-804
  - TC-GS-IMPORT-805
  - TC-GS-IMPORT-806
  - TC-GS-IMPORT-949
coverage:
  web: automated
---

# Refleksi Dropdown option dan perubahan Custom Field pada seluruh baris draft (Save, Remove, Append, pindah Sub-Tab, field baru Optional)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memutasi Custom Field Client A (state global) dan memulihkannya (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC2_PASSWORD` (nama env baru). Sesi API mengubah opsi dan definisi Custom Field di Custom Field User; klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > User Login Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-05: draft User Login 8 baris `pending` dari `user-login-8.csv` pada Client A (Shift `Siang` pada Row # 1 dan 2, `Pagi` pada Row # 3, kosong pada Row # 4 sampai 8; Overtime Hours `1.25` pada Row # 4), disiapkan lewat skrip seed dan dibuat ulang sebelum tiap TC (Kontrak Fixture R2).
- Berkas uji (Append): `shift-dini.csv` (header First Name; Last Name; Email; Division; Access; Shift; 1 baris: Nina, Kartika, `nina.kartika+{runId}-205@example.com`, Engineering, Global Settings, `Dini Hari`); `shift-append.csv` (1 baris: Oka, Wibowo, `oka.wibowo+{runId}-205@example.com`, Engineering, Global Settings, `Malam`). Email diberi suffix per run (TC menulis tanpa suffix).
- Custom Field Client A (Pre-setup, Optional, Active): Shift (Dropdown Pagi/Siang/Malam), Shift Notes (Text Area), Overtime Hours (Numeric 2 desimal), Emergency Phone (Phone), Join Date (Date). Nama `Shift`, opsi `Pagi`, `Siang`, dan `Dini Hari` literal (pengecualian S-12 butir (ii): nama dan opsi menentukan nilai sel yang diasersi). Custom Field baru TC-GS-IMPORT-949 diberi nama `Hobi{runId}` (suffix per run) dan header kolom diasersi dengan nama itu.
- Urutan TC: 510, 511, 949, 515, 804, 805, 806, 512 (hapus opsi `Siang` sebagai pemicu error paling akhir). Pemulihan opsi dilakukan sebagai langkah aksi di akhir tiap blok (Kontrak Fixture R2) dan oleh hook `after` sebagai cadangan.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): opsi `Dini Hari` dihapus, opsi `Pagi` dikembalikan dari `Morning`, opsi `Siang` ditambahkan kembali bila hilang (urutan Pagi, Siang, Malam), Custom Field `Hobi{runId}` dihapus, draft User Login Client A dipulihkan ke D-05.
- Kemampuan teknis: skrip seed D-05; sesi API Admin kedua; pemilihan berkas.
- State global: Custom Field Client A (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Opsi ditambahkan (TC-GS-IMPORT-510)

1. Admin kedua Client A (sesi API) menambahkan opsi `Dini Hari` ke Custom Field `Shift` hingga tersimpan
2. Tekan `F5` pada halaman Import
3. Verifikasi Staging Metric Cards tetap Total Rows 8, Ready to Import 8, Errors 0, Duplicates 0
4. Upload `shift-dini.csv`
5. Klik `[Append Records]` pada Dialog Append to Draft
6. Klik `[Confirm Mapping]`
7. Verifikasi muncul toast sukses: "Success, row has been added."
8. Verifikasi Row # 9 bernilai Shift `Dini Hari` berstatus `pending`
9. Verifikasi Staging Metric Cards: Total Rows 9, Ready to Import 9, Errors 0
10. Pulihkan: Admin kedua menghapus opsi `Dini Hari`, buat ulang draft D-05, muat ulang halaman

### Opsi di-rename (TC-GS-IMPORT-511)

11. Admin kedua Client A (sesi API) me-rename opsi `Pagi` menjadi `Morning` pada Custom Field `Shift` hingga tersimpan
12. Tekan `F5` pada halaman Import
13. Verifikasi sel Shift pada Row # 3 menampilkan `Morning`
14. Verifikasi sel Shift pada Row # 1 dan 2 tetap `Siang`
15. Verifikasi Staging Metric Cards tetap Total Rows 8, Ready to Import 8, Errors 0, Duplicates 0
16. Pulihkan: Admin kedua me-rename opsi `Morning` kembali menjadi `Pagi`, buat ulang draft D-05, muat ulang halaman

### Custom Field baru Optional (TC-GS-IMPORT-949)

17. Admin kedua Client A (sesi API) membuat Custom Field `Hobi{runId}` (Data Type Text, Optional, Active) di Custom Field User hingga tersimpan
18. Tekan `F5` pada halaman Import
19. Verifikasi kolom `Hobi{runId}` tampil dengan sel kosong menampilkan `—`
20. Verifikasi sel kolom `Hobi{runId}` tanpa border `danger`
21. Verifikasi seluruh 8 baris tetap `pending`
22. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 8, Errors 0
23. Pulihkan: Admin kedua menghapus Custom Field `Hobi{runId}`, muat ulang halaman

### Refleksi ke seluruh baris setelah Save (TC-GS-IMPORT-515)

24. Admin kedua Client A (sesi API) menghapus opsi `Siang` dari Custom Field `Shift` hingga tersimpan (halaman Import tetap terbuka tanpa dimuat ulang)
25. Klik row action `⋯` pada Row # 5 lalu Edit
26. Tambahkan `X` di akhir nilai Last Name pada Row # 5
27. Klik `[Save]`
28. Verifikasi muncul toast sukses: "Success, row has been updated."
29. Verifikasi Row # 1 dan 2 berstatus `error` (bukan hanya Row # 5 yang disunting)
30. Verifikasi Staging Metric Cards: Ready to Import 6, Errors 2
31. Pulihkan: Admin kedua menambahkan kembali opsi `Siang` ke Custom Field `Shift`, buat ulang draft D-05, muat ulang halaman

### Refleksi ke seluruh baris setelah Remove (TC-GS-IMPORT-804)

32. Admin kedua Client A (sesi API) menghapus opsi `Siang` dari Custom Field `Shift` hingga tersimpan (halaman Import tetap terbuka tanpa dimuat ulang)
33. Klik row action `⋯` pada Row # 5
34. Pilih Remove
35. Klik `[Delete]` pada Dialog Delete Row
36. Verifikasi muncul toast sukses: "Success, row has been deleted."
37. Verifikasi baris bekas Row # 1 dan 2 (Shift `Siang`) berstatus `error`
38. Verifikasi Staging Metric Cards: Total Rows 7, Ready to Import 5, Errors 2
39. Pulihkan: Admin kedua menambahkan kembali opsi `Siang` ke Custom Field `Shift`, buat ulang draft D-05, muat ulang halaman

### Refleksi ke seluruh baris setelah Append (TC-GS-IMPORT-805)

40. Admin kedua Client A (sesi API) menghapus opsi `Siang` dari Custom Field `Shift` hingga tersimpan (halaman Import tetap terbuka tanpa dimuat ulang)
41. Upload `shift-append.csv`
42. Klik `[Append Records]` pada Dialog Append to Draft
43. Klik `[Confirm Mapping]`
44. Verifikasi muncul toast sukses: "Success, row has been added."
45. Verifikasi Row # 1 dan 2 (Shift `Siang`) berstatus `error`
46. Verifikasi Row # 9 (Shift `Malam`) berstatus `pending`
47. Verifikasi Staging Metric Cards: Total Rows 9, Ready to Import 7, Errors 2
48. Pulihkan: Admin kedua menambahkan kembali opsi `Siang` ke Custom Field `Shift`, buat ulang draft D-05, muat ulang halaman

### Refleksi saat kembali ke Sub-Tab User Login (TC-GS-IMPORT-806)

49. Klik Sub-Tab Division
50. Admin kedua Client A (sesi API) menghapus opsi `Siang` dari Custom Field `Shift` hingga tersimpan
51. Klik Sub-Tab User Login
52. Verifikasi Row # 1 dan 2 (Shift `Siang`) berstatus `error`
53. Verifikasi Staging Metric Cards: Ready to Import 6, Errors 2
54. Pulihkan: Admin kedua menambahkan kembali opsi `Siang` ke Custom Field `Shift`, buat ulang draft D-05, muat ulang halaman

### Opsi dihapus (TC-GS-IMPORT-512)

55. Admin kedua Client A (sesi API) menghapus opsi `Siang` dari Custom Field `Shift` hingga tersimpan
56. Tekan `F5` pada halaman Import
57. Verifikasi Row # 1 dan 2 (Shift `Siang`) berstatus `error`
58. Verifikasi Staging Metric Cards: Ready to Import 6, Errors 2
59. Verifikasi Error Summary Callout memuat `Shift: Invalid option` dengan badge "2 rows"
60. Verifikasi 6 baris lain (Row # 3 sampai 8) tetap `pending`
61. Pulihkan: Admin kedua menambahkan kembali opsi `Siang` ke Custom Field `Shift`, buat ulang draft D-05

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 61 langkah, di atas 35 langkah. Alasan: delapan blok berpola sama (mutasi opsi atau definisi Custom Field lewat sesi API, lalu baca Staging Table User Login) pada satu Sub-Tab dan satu dataset D-05; tiap blok berdiri sendiri dan dipulihkan eksplisit (langkah 10, 16, 23, 31, 39, 48, 54, 61).
- P-2: Admin kedua hanya memicu perubahan Custom Field lewat sesi API; hasil diasersi hanya di sesi admin pertama.
- Langkah pemulihan (10, 16, 23, 31, 39, 48, 54, 61) adalah aksi tanpa `Verifikasi` (S-09); hook `after` adalah cadangan.
- TC-GS-IMPORT-512 diletakkan paling akhir sesuai prinsip aksi yang menghabisi data di akhir; TC-GS-IMPORT-515, 804, 805, 806 juga menghapus opsi `Siang` dan dipulihkan di blok masing-masing.
- Langkah 24, 32, 40 menjaga halaman Import tetap terbuka tanpa `F5` sesuai TC (refleksi diterapkan pada aksi Save, Remove, Append).
- Temuan untuk QA:
  - TC-GS-IMPORT-805 dan 510 Data Uji menulis Email tanpa suffix per run; spec memakai suffix per run.
  - TC-GS-IMPORT-949 menamai Custom Field `Hobi`; spec memakai `Hobi{runId}` dengan nama yang sama pada asersi (S-12).
  - TC-GS-IMPORT-512 sampai 806 menghapus opsi `Siang` yang dipakai Row # 1 dan 2; penambahan kembali opsi memulihkan nilai opsi tetapi mungkin mengubah urutan opsi; mekanisme pemulihan persis disediakan tim FE/BE.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
