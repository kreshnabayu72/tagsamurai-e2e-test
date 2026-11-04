---
id: TC-FA-LBL-E2E-054-modal-changelog-labels-setup-column-pagination-dan-download
title: "Modal Changelog: Labels: Setup Column, Pagination, dan Download (menu, nama berkas, kolom, dan baris)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-03/setup-column/hide-show
  - FALB:obl/T-ALB-03/setup-column/reorder
  - FALB:obl/T-ALB-03/setup-column/reset
  - FALB:obl/T-ALB-03/pagination
  - FALB:obl/T-ALB-03/download
  - FALB:global-table-rules/pagination
coverage:
  web: automated
---

# Modal Changelog: Labels: Setup Column, Pagination, dan Download (menu, nama berkas, kolom, dan baris)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Pelaku kedua seeding lewat sesi API: `DU-31`, env `FA_TC2_EMAIL` dan `FA_TC2_PASSWORD`.
- Data uji `DU-62` (Dataset Changelog: Labels), bersuffix `{runId}-054`, label `Log-{runId}-054-nn`, dibuat lewat sesi API di hook `before`: Create label `-01` sampai `-08` oleh `DU-01`, Edit Label Name dan Edit Color `-01` oleh `DU-31`, Create `-09` oleh `DU-31`, dan Delete `-09` oleh `DU-31`; total N = 12 entri bersuffix `{runId}-054` (lebih dari 10, sehingga ada halaman 2 saat ukuran halaman 10). N dibaca lewat kemampuan baca BE (entri Changelog bersuffix) sebelum uji, bukan dari tabel satu halaman. Hook `after` menghapus label `-01` sampai `-08` lewat sesi API.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label dan membaca entri Changelog; kemampuan membaca berkas unduhan (baris header dan jumlah baris data CSV dan XLSX); keduanya disediakan tim FE/BE. Isi sel berkas dibahas di spec 067.
- State global: konfigurasi kolom Setup Column Modal Changelog disimpan di cache browser (`localStorage`); spec memulihkannya ke default dengan langkah eksplisit (langkah 19 dan 25) dan hook `after` menghapus preferensi kolom akun `DU-01` sebagai cadangan. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik ikon Changelog pada toolbar tabel
2. Ketik Search `DU-62`, tekan Enter
3. Verifikasi baris entri milik `DU-62` tampil pada tabel Modal Changelog: Labels

### FALB:obl/T-ALB-03/setup-column/hide-show: Sembunyikan dan tampilkan kolom Hideable

4. Buka modal Setup Column lewat header kolom Actions `⋯` pada tabel Modal Changelog dan item `Setup Column...`
5. Verifikasi modal Setup Column tampil dengan judul `Setup Column`
6. Hilangkan centang kolom Field dan Old Value
7. Verifikasi tabel di balik modal tidak lagi menampilkan kolom Field dan Old Value
8. Klik `[Save]`
9. Verifikasi header Date, Action, Label Name, New Value, dan Modified By tampil sedangkan header Field dan Old Value tidak tampil
10. Buka modal Setup Column lewat header kolom Actions `⋯` pada tabel Modal Changelog dan item `Setup Column...`
11. Centang kembali kolom Field dan Old Value, klik `[Save]`
12. Verifikasi header Field dan Old Value tampil kembali sehingga ketujuh header tampil

### FALB:obl/T-ALB-03/setup-column/reorder: Geser urutan kolom

13. Buka modal Setup Column lewat header kolom Actions `⋯` pada tabel Modal Changelog dan item `Setup Column...`
14. Geser kolom Date ke posisi terakhir
15. Verifikasi tabel di balik modal menampilkan kolom Date sebagai kolom data terakhir
16. Klik `[Save]`
17. Verifikasi urutan header Action, Label Name, Field, Old Value, New Value, Modified By, Date
18. Buka modal Setup Column lewat header kolom Actions `⋯` pada tabel Modal Changelog dan item `Setup Column...`
19. Geser kolom Date kembali ke posisi pertama, klik `[Save]`

### FALB:obl/T-ALB-03/setup-column/reset: Reset to Default

20. Buka modal Setup Column lewat header kolom Actions `⋯` pada tabel Modal Changelog dan item `Setup Column...`
21. Hilangkan centang kolom Modified By
22. Klik `[Reset to Default]`
23. Verifikasi tabel di balik modal menampilkan ketujuh kolom dengan urutan default Date, Action, Label Name, Field, Old Value, New Value, Modified By
24. Klik `[Save]`
25. Verifikasi urutan header Date, Action, Label Name, Field, Old Value, New Value, Modified By

### FALB:obl/T-ALB-03/pagination: Ukuran halaman default dan navigasi halaman

26. Verifikasi tabel menampilkan 10 baris pada halaman pertama dengan ukuran halaman default 10
27. Klik halaman berikutnya pada kontrol Pagination
28. Verifikasi halaman 2 menampilkan N dikurangi 10 baris, yaitu 2 baris entri `DU-62`

### FALB:global-table-rules/pagination: Pilihan ukuran halaman Modal Changelog sama dengan Labels List

29. Buka pilihan jumlah baris per halaman
30. Verifikasi pilihan jumlah baris per halaman adalah 10, 25, 50, dan 100
31. Pilih 25
32. Verifikasi N = 12 baris entri `DU-62` tampil pada satu halaman

### FALB:obl/T-ALB-03/download: Download CSV dan XLSX mengikuti Search dan kolom tampil

33. Klik Download pada toolbar Modal Changelog
34. Verifikasi menu menampilkan `Download as CSV` dan `Download as XLSX`
35. Klik `Download as CSV`
36. Verifikasi tidak ada toast sukses
37. Verifikasi berkas `Changelog-Labels.csv` terunduh
38. Verifikasi baris header berkas memuat Date, Action, Label Name, Field, Old Value, New Value, Modified By
39. Verifikasi berkas memuat N = 12 baris data, hanya entri hasil Search `DU-62`
40. Klik Download pada toolbar Modal Changelog, pilih `Download as XLSX`
41. Verifikasi tidak ada toast sukses
42. Verifikasi berkas `Changelog-Labels.xlsx` terunduh
43. Verifikasi baris header sheet memuat Date, Action, Label Name, Field, Old Value, New Value, Modified By
44. Verifikasi sheet memuat N = 12 baris data, hanya entri hasil Search `DU-62`

## Notes

- Langkah penghubung (S-03): langkah 1 membuka modal; langkah 2 mempersempit tabel ke entri `DU-62` (R-16); langkah 4, 10, 13, 18, dan 20 membuka modal Setup Column; langkah 27 dan 29 menggerakkan Pagination; langkah 33 dan 40 membuka menu Download.
- Pemulihan Setup Column (bagian 8b butir 14): langkah 10 sampai 12 mengembalikan kolom Field dan Old Value; langkah 18 sampai 19 mengembalikan urutan kolom Date; langkah 20 sampai 25 mengembalikan konfigurasi ke default lewat `[Reset to Default]` setelah `[Save]`. Hook `after` hanya cadangan.
- Anchor positif (bagian 8b butir 2): langkah 3 membuktikan entri `DU-62` sudah termuat sebelum asersi kolom tidak tampil (langkah 9) dan header yang tersisa (langkah 9) menjadi pembanding; langkah 36 dan 41 (absence toast) ditaruh segera setelah pemicu unduh dan sebelum asersi berkas terunduh sebagai anchor positif (butir 11).
- Pembagian klausa lintas spec: `FALB:global-table-rules/pagination` dikutip spec 035, 050, dan spec ini; spec ini mengasersi nilai default dan pilihan Pagination pada Modal Changelog, spec 035 pada Labels List, dan spec 050 pada Tagged Asset List. `FALB:obl/T-ALB-03/download` dikutip spec 054 dan spec 067; spec ini mengasersi menu, nama berkas, header kolom, dan jumlah baris (kelas fungsional, konvensi prinsip 13 butir f), spec 067 mengasersi nilai sel, BOM, dan sheet.
- Klausa Filter dan kolom tersembunyi atas isi berkas: berkas diasersi dengan Search `DU-62` dan ketujuh kolom tampil (langkah 38 sampai 44). Pengaruh Filter Panel dan kolom tersembunyi atas isi berkas diasersi di spec 067.
- Alasan spec melewati 35 langkah: semua blok satu kelas harness (fungsional UI Modal Changelog) dengan data `DU-62` yang sama; tiap blok berdiri sendiri karena blok yang mengubah Setup Column memulihkannya sendiri di akhir blok (langkah 10 sampai 12, 18 sampai 19, dan 20 sampai 25) dan blok Pagination serta Download tidak bergantung pada hasil blok lain. Pemecahan menambah login dan seeding `DU-62` per spec.
