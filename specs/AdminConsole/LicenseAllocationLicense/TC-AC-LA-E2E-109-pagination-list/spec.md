---
id: TC-AC-LA-E2E-109-pagination-list
title: "Pagination List: Ukuran Halaman, Navigasi, Reset Halaman, dan Tanpa Pagination Allocation Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-335
  - TC-AC-LA-336
  - TC-AC-LA-337
  - TC-AC-LA-338
  - TC-AC-LA-339
coverage:
  web: automated
---

# Pagination List: Ukuran Halaman, Navigasi, Reset Halaman, dan Tanpa Pagination Allocation Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status, lebih dari 25 baris di tab Current, sedikitnya 3 halaman pada 10 data per halaman; Client `PT Sejahtera`) dan Pre-setup #55 (alokasi dengan riwayat log lengkap, total 12 entri, berada di tab Current; Allocation ID-nya dirujuk lewat `Fixture.license-allocation-license`) bersifat baca-saja untuk spec ini.
- Parameter langkah 17 sampai 18 (TC-AC-LA-336), satu baris per nilai input nomor halaman tidak valid: `0`, `-1`, `abc`, `999` (nomor melebihi halaman terakhir).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-335: Pagination default dan pilihan ukuran halaman

1. Verifikasi default 10 data per halaman
2. Verifikasi pagination tampil
3. Buka overlay page size
4. Verifikasi pilihan 10, 25, 50, dan 100
5. Verifikasi tidak ada opsi `All`
6. Tekan `Esc` untuk menutup overlay
7. Pindah ke halaman 2
8. Buka overlay page size dan pilih 25
9. Verifikasi tabel kembali ke halaman 1

### TC-AC-LA-336: Navigasi halaman

10. Klik menu `License Allocation` di sidebar
11. Klik halaman berikutnya
12. Verifikasi tabel berpindah ke halaman 2
13. Klik halaman sebelumnya
14. Verifikasi tabel berpindah ke halaman 1
15. Ketik nomor halaman `2` di input nomor halaman, tekan Enter
16. Verifikasi tabel berpindah ke halaman 2
17. Untuk setiap baris tabel parameter (langkah 17 sampai 18): ketik Nilai di input nomor halaman, tekan Enter
18. Verifikasi input tidak valid diabaikan dan tabel tetap di halaman 2

### TC-AC-LA-337: Search mereset ke halaman 1

19. Klik menu `License Allocation` di sidebar
20. Pindah ke halaman 2
21. Ketik Search `Sejahtera`, tekan Enter
22. Verifikasi tabel kembali ke halaman 1

### TC-AC-LA-338: Pindah tab menampilkan halaman 1

23. Klik menu `License Allocation` di sidebar
24. Pindah ke halaman 3 di tab Current
25. Klik tab `History`
26. Verifikasi tab History mulai pada halaman 1 dengan 10 data per halaman

### TC-AC-LA-339: Allocation Log tanpa pagination

27. Klik menu `License Allocation` di sidebar
28. Ketik Search Allocation ID alokasi riwayat lengkap (Pre-setup #55), tekan Enter
29. Buka Allocation Log alokasi itu dengan klik Allocation ID-nya
30. Verifikasi seluruh entri (lebih dari 10) dimuat dalam satu daftar scroll
31. Verifikasi tidak ada pagination pada Allocation Log
32. Tutup Allocation Log

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 17 sampai 18 diulang untuk empat baris tabel parameter (8 langkah terekspansi; total sekitar 38 langkah terekspansi). Verifikasi tetap satu per iterasi.
- Langkah penghubung (S-03): langkah 10, 19, 23, 27 (klik menu sidebar mereset Search, Sort, Filter, dan paginasi), langkah 28 (Search untuk menemukan baris target, R-16), langkah 32 (menutup Allocation Log).
- Temuan untuk QA:
  - TC-AC-LA-336 menyebut "nomor melebihi halaman terakhir" tanpa nilai; spec memakai `999`.
  - TC-AC-LA-338 menyebut "kunjungan pertama" tab History tanpa menyatakan cara memastikan kunjungan pertama; spec mereset lewat klik menu sidebar sebelum pindah tab.
  - TC-AC-LA-339 tidak menyebut cara membuka Allocation Log, tab asal alokasi Pre-setup #55 (riwayat memuat status expired, sehingga bisa berada di tab History), dan Allocation ID-nya; spec mengasumsikan alokasi berada di tab Current dan dibuka lewat klik Allocation ID (TC-AC-LA-4).
  - TC-AC-LA-337 judul menyebut Apply Filter, tetapi langkah dan Expected hanya Search; spec mengikuti langkah TC.
