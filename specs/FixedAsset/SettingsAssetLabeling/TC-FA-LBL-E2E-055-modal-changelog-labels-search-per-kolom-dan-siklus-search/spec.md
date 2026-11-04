---
id: TC-FA-LBL-E2E-055-modal-changelog-labels-search-per-kolom-dan-siklus-search
title: "Modal Changelog: Labels: Search per kolom dan siklus Search"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-03/search-cycle
  - FALB:obl/T-ALB-03/search/FLD-12
  - FALB:obl/T-ALB-03/search/FLD-13
  - FALB:obl/T-ALB-03/search/FLD-14
  - FALB:obl/T-ALB-03/search/FLD-15
  - FALB:obl/T-ALB-03/search/FLD-16
  - FALB:obl/T-ALB-03/search/FLD-17
coverage:
  web: automated
---

# Modal Changelog: Labels: Search per kolom dan siklus Search

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Pelaku kedua seeding lewat sesi API: `DU-31`, env `FA_TC2_EMAIL` dan `FA_TC2_PASSWORD`.
- Data uji `DU-62` (Dataset Changelog: Labels), bersuffix `{runId}-055`, label `Log-{runId}-055-nn`, dibuat lewat sesi API di hook `before` dengan urutan tulis: (a) Create label `-04` sampai `-09` oleh `DU-01`; (b) Create `-01` oleh `DU-01`, Edit Label Name `-01` menjadi `-01-baru` oleh `DU-31`, Edit Color `-01` dari `#3B82F6` ke `#EF4444` oleh `DU-31`, Create `-02` oleh `DU-31`, Create `-03` oleh `DU-01`, lalu Delete `-03` oleh `DU-01`. Total 12 entri; entri bagian (b) adalah entri terbaru sehingga tampil di halaman pertama pada Newest First (default). Hook `after` menghapus label `-01-baru`, `-02`, dan `-04` sampai `-09` lewat sesi API.
- Data uji `DU-58` (kata kunci Search tanpa hasil): `zzz-{runId}-055`.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label dan membaca entri Changelog, disediakan tim FE/BE. Search hanya menyaring saat Enter (PRD §5 Search; prd-conventions §9.1b).
- State global: tidak ada yang diubah; Search adalah state tampilan Modal Changelog dan direset saat modal ditutup. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik ikon Changelog pada toolbar tabel

### FALB:obl/T-ALB-03/search-cycle: Siklus Search: Enter, kosongkan, tanpa hasil, dan reset ke halaman 1

2. Ketik Search `DU-62`, tekan Enter
3. Verifikasi baris entri milik `DU-62` tampil pada tabel Modal Changelog
4. Klik halaman 2 pada kontrol Pagination
5. Ganti isi kotak search dengan `Edit`, tekan Enter
6. Verifikasi kontrol Pagination menunjukkan halaman 1
7. Klik `(←)` pada kotak Search Modal Changelog
8. Verifikasi baris Delete label `-03` milik `DU-62` tampil pada tabel tanpa Search
9. Ketik Search `DU-58`, tekan Enter
10. Verifikasi empty state Modal Changelog menampilkan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
11. Klik `(←)` pada kotak Search Modal Changelog

### FALB:obl/T-ALB-03/search/FLD-12: Search menemukan baris lewat nilai kolom Action

12. Ketik Search `Edit`, tekan Enter
13. Verifikasi baris Edit dengan Field `Label Name` milik `DU-62` tampil
14. Verifikasi baris Create label `-02` milik `DU-62` tidak tampil
15. Klik `(←)` pada kotak Search Modal Changelog

### FALB:obl/T-ALB-03/search/FLD-13: Search menemukan baris lewat nilai kolom Label Name

16. Ketik Search nama label `-02` milik `DU-62`, tekan Enter
17. Verifikasi baris Create label `-02` milik `DU-62` tampil
18. Verifikasi baris Create label `-03` milik `DU-62` tidak tampil
19. Klik `(←)` pada kotak Search Modal Changelog

### FALB:obl/T-ALB-03/search/FLD-14: Search menemukan baris lewat nilai kolom Field

20. Ketik Search `Color`, tekan Enter
21. Verifikasi baris Edit dengan Field `Color` milik `DU-62` tampil
22. Verifikasi baris Create label `-02` milik `DU-62` tidak tampil
23. Klik `(←)` pada kotak Search Modal Changelog

### FALB:obl/T-ALB-03/search/FLD-15: Search menemukan baris lewat nilai kolom Old Value

24. Ketik Search `#3B82F6`, tekan Enter
25. Verifikasi baris Edit Color dengan Old Value `#3B82F6` milik `DU-62` tampil
26. Verifikasi baris Edit dengan Field `Label Name` milik `DU-62` tidak tampil
27. Klik `(←)` pada kotak Search Modal Changelog

### FALB:obl/T-ALB-03/search/FLD-16: Search menemukan baris lewat nilai kolom New Value

28. Ketik Search `#EF4444`, tekan Enter
29. Verifikasi baris Edit Color dengan New Value `#EF4444` milik `DU-62` tampil
30. Verifikasi baris Create label `-02` milik `DU-62` tidak tampil
31. Klik `(←)` pada kotak Search Modal Changelog

### FALB:obl/T-ALB-03/search/FLD-17: Search menemukan baris lewat nilai kolom Modified By

32. Ketik Search nama lengkap akun `DU-31`, tekan Enter
33. Verifikasi baris Create label `-02` milik `DU-62` oleh `DU-31` tampil
34. Verifikasi baris Create label `-03` milik `DU-62` oleh `DU-01` tidak tampil

## Notes

- Langkah penghubung (S-03): langkah 1 membuka modal; langkah 4 pindah ke halaman 2 sebelum Search diganti (pemicu reset halaman); langkah 7, 11, 15, 19, 23, 27, dan 31 menutup input Search sehingga tabel kembali tanpa Search sebelum blok berikutnya (S-09). Search di spec ini adalah objek klausa, bukan alat membuka baris target (R-16 tidak berlaku).
- Anchor positif (bagian 8b butir 2): langkah 3 membuktikan entri `DU-62` sudah termuat; langkah 8 membuktikan tabel pulih tanpa Search; asersi "tidak tampil" tiap blok (langkah 14, 18, 22, 26, 30, 34) didahului asersi baris pembanding milik `DU-62` pada surface yang sama (langkah 13, 17, 21, 25, 29, 33).
- Kolom Date tidak Searchable (Tabel 3 PRD §4.1.2) sehingga tidak ada blok Search untuk `FLD-11`; kolom Action, Label Name, Field, Old Value, New Value, dan Modified By Searchable. Klausa Search Modified By memakai nama lengkap akun (catatan baris `FLD-17`).
- Asersi baris pada halaman pertama berlaku karena entri `DU-62` bagian (b) adalah entri terbaru dan suite berjalan serial; hasil Search dibaca pada halaman pertama Newest First.
- Batas asersi: kata kunci Search untuk kolom Action, Field, Old Value, New Value, dan Modified By (`Edit`, `Color`, kode hex, nama lengkap aktor) tidak unik per run dan Changelog adalah surface audit permanen client; asersi hanya menyatakan baris `DU-62` tampil atau tidak tampil, bukan ketiadaan baris lain dengan kata kunci yang sama.
