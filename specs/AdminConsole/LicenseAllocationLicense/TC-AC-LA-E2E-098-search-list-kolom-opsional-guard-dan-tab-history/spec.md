---
id: TC-AC-LA-E2E-098-search-list-kolom-opsional-guard-dan-tab-history
title: "Search List: Kolom Opsional, Guard Last Updated, Visibilitas Kolom, Trim, dan Tab History"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-285
  - TC-AC-LA-286
  - TC-AC-LA-287
  - TC-AC-LA-288
  - TC-AC-LA-289
  - TC-AC-LA-290
coverage:
  web: automated
---

# Search List: Kolom Opsional, Guard Last Updated, Visibilitas Kolom, Trim, dan Tab History

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab; Plan `Growth`, Payment `Wallet` dan `Free`, Paid From `PT ABC (Principal)`, Cost `$3,650.00` dan `—`, Client `PT Sejahtera`) bersifat baca-saja untuk spec ini; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column (menampilkan `Plan`, `Payment`, `Paid From`, `Cost`). Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-285: Search kolom Curated Plan, Payment, dan Paid From

1. Ketik Search `Growth` saat kolom Plan disembunyikan, tekan Enter
2. Verifikasi `No results found` tampil
3. Klik ikon panah `(←)`
4. Klik `⋯` pada header kolom Actions
5. Klik `Setup Column...`
6. Centang `Plan`, `Payment`, dan `Paid From`
7. Klik `[Save]`
8. Ketik Search `Growth`, tekan Enter
9. Verifikasi baris dengan Plan `Growth` tampil
10. Ganti isi kotak search dengan `wallet`, tekan Enter
11. Verifikasi baris dengan Payment `Wallet` tampil
12. Ganti isi kotak search dengan `PT ABC`, tekan Enter
13. Verifikasi baris dengan Paid From `PT ABC (Principal)` tampil

### TC-AC-LA-286: Search kolom Cost

14. Klik `⋯` pada header kolom Actions
15. Klik `Setup Column...`
16. Centang `Cost`
17. Klik `[Save]`
18. Ganti isi kotak search dengan `3,650`, tekan Enter
19. Verifikasi baris dengan Cost `$3,650.00` tampil
20. Verifikasi baris dengan Cost `—` (Payment Free) tidak tampil

### TC-AC-LA-287: Guard kolom Last Updated

21. Catat teks sel Last Updated pada baris pertama tabel
22. Ganti isi kotak search dengan teks Last Updated yang dicatat pada langkah 21, tekan Enter
23. Verifikasi `No results found` tampil

### TC-AC-LA-288: Search terikat visibilitas kolom

24. Ganti isi kotak search dengan `Sejahtera`, tekan Enter
25. Verifikasi baris dengan Client `PT Sejahtera` tampil
26. Klik `⋯` pada header kolom Actions
27. Hapus centang `Client` pada overlay Column Visibility
28. Tekan `Esc` untuk menutup overlay
29. Ganti isi kotak search dengan `Sejahtera`, tekan Enter
30. Verifikasi `No results found` tampil
31. Klik `⋯` pada header kolom Actions
32. Centang `Client` pada overlay Column Visibility
33. Tekan `Esc` untuk menutup overlay
34. Ganti isi kotak search dengan `Sejahtera`, tekan Enter
35. Verifikasi baris dengan Client `PT Sejahtera` tampil

### TC-AC-LA-289: Trim dan karakter khusus

36. Catat isi halaman pertama hasil Search `Sejahtera`
37. Ganti isi kotak search dengan `  Sejahtera  ` (spasi di kedua tepi), tekan Enter
38. Verifikasi hasil identik dengan hasil Search `Sejahtera` yang dicatat pada langkah 36
39. Verifikasi isi input tetap `  Sejahtera  ` seperti yang diketik
40. Ganti isi kotak search dengan `<b>x</b>`, tekan Enter
41. Verifikasi `<b>x</b>` diperlakukan sebagai teks biasa tanpa error
42. Ganti isi kotak search dengan `%`, tekan Enter
43. Verifikasi `%` diperlakukan sebagai teks biasa tanpa error

### TC-AC-LA-290: Search pada tab History

44. Klik tab `History`
45. Ketik Search `Sejahtera`, tekan Enter
46. Verifikasi sedikitnya satu baris tampil
47. Verifikasi hanya baris tab History yang cocok tampil
48. Verifikasi baris tab Current tidak ikut tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 3 (menutup search bar), langkah 21 (mencatat teks sel), langkah 28 dan 33 (menutup overlay), langkah 36 (baseline).
- Alasan spec melewati sekitar 35 langkah: semua blok satu kelas harness (fungsional) dan satu dataset baca-saja (#54); tiap blok Search berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Konfigurasi kolom hasil langkah 6 dan 16 (kolom `Plan`, `Payment`, `Paid From`, `Cost` tampil) dipulihkan hook `after`; konfigurasi itu dipakai sebagai precondition TC-AC-LA-287 sampai TC-AC-LA-290 dan tidak diasersi.
- Temuan untuk QA:
  - TC-AC-LA-287 menyebut "teks tanggal dari kolom Last Updated" tanpa nilai konkret; spec memakai teks sel Last Updated baris pertama yang dibaca saat uji.
  - TC-AC-LA-289 Expected b ("diperlakukan sebagai teks biasa tanpa error atau interpretasi") tidak menyebut hasil yang teramati; spec mengasersi kalimat itu apa adanya.
  - TC-AC-LA-290 tidak menyebut status kotak Search sesudah pindah tab; spec memakai langkah Search atomik sesudah klik tab `History`.
  - TC-AC-LA-286 dan TC-AC-LA-285 tidak menyebut cara menutup overlay Column Visibility; spec memakai `Esc`.
