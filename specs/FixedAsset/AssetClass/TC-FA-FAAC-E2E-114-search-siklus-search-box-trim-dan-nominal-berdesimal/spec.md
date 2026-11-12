---
id: TC-FA-FAAC-E2E-114-search-siklus-search-box-trim-dan-nominal-berdesimal
title: "Search Tabel Asset Class: Siklus Search Box, Pemangkasan Spasi, dan Nominal Berdesimal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-360
  - TC-FA-FAAC-361
  - TC-FA-FAAC-705
coverage:
  web: automated
---

# Search Tabel Asset Class: Siklus Search Box, Pemangkasan Spasi, dan Nominal Berdesimal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ (Heavy Equipment; Capitalization Threshold 5,000,000), VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive).
- Data milik spec (seed di hook `before`, cleanup di hook `after`; TC-FA-FAAC-705): Asset Class B-DEC (Class Name `Decimal Fixture`, Method Straight Line, Useful Life 60, Residual Value unit Amount 2500000.99, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`, Capitalization Threshold 1500.99, tampil `1,500.99`). Precondition TC-FA-FAAC-705 menyebutnya hasil TC pembuatan B-DEC; spec membuat kelas itu lewat seeding API sebagai precondition, tidak diasersi pembuatannya. Seed dan pembersihan disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-360: Siklus interaksi Search box

1. Arahkan kursor ke icon Search
2. Verifikasi tooltip icon berbunyi `Search`
3. Klik icon Search
4. Verifikasi Search bar melebar
5. Verifikasi kursor otomatis fokus pada kotak input
6. Verifikasi placeholder `Search asset class...`
7. Ketik `heavy` (tanpa Enter)
8. Verifikasi icon `✕` muncul di dalam kotak input
9. Verifikasi tabel belum tersaring
10. Tekan Enter
11. Verifikasi tabel tersaring menjadi baris HEAVY-EQ
12. Klik icon `✕` di dalam kotak input
13. Verifikasi teks input terhapus
14. Verifikasi kotak tetap terbuka dengan kursor fokus
15. Verifikasi tabel masih menampilkan hasil pencarian `heavy`
16. Tekan Enter pada input kosong
17. Verifikasi tabel kembali ke semua data
18. Ketik `heavy`, tekan Enter
19. Klik icon `←`
20. Verifikasi kotak Search menutup menjadi icon Search biasa
21. Verifikasi keyword dikosongkan
22. Verifikasi tabel langsung kembali ke semua data

### TC-FA-FAAC-361: Search memangkas spasi awal dan akhir kata kunci saat Enter

23. Ketik Search `  avy equ  ` (dua spasi di awal dan akhir), tekan Enter
24. Verifikasi tabel menampilkan baris HEAVY-EQ (spasi di tengah kata kunci dipertahankan sehingga pencocokan memakai `avy equ`)
25. Verifikasi isi kotak input tetap `  avy equ  `

### TC-FA-FAAC-705: Search pada nominal berdesimal mencocokkan teks yang tampil di kolom Capitalization Threshold

26. Ganti isi kotak search dengan `1,500.99`, tekan Enter
27. Verifikasi baris B-DEC tampil
28. Verifikasi HEAVY-EQ dan baris contoh lain tidak tampil
29. Klik `✕` pada Search, tekan Enter
30. Ketik Search `5,000,000`, tekan Enter
31. Verifikasi baris HEAVY-EQ tampil
32. Verifikasi baris B-DEC tidak tampil
33. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 29 (mengosongkan kotak Search antar kata kunci; 8b butir 9), langkah 33 (menutup input Search dan mereset tabel di akhir spec, S-09; R-16). Langkah 26 memakai "ganti isi kotak search" karena kotak masih berisi hasil TC-FA-FAAC-361.
- Langkah 2 sampai 6 mengikuti urutan state (tooltip sebelum klik, Search bar sesudah klik; 8b butir 5), bukan urutan butir Expected TC-FA-FAAC-360.
- Asersi absence langkah 28 dan 32 punya anchor positif pada surface yang sama: baris B-DEC (langkah 27) dan baris HEAVY-EQ (langkah 31) tampil lebih dulu (8b butir 2).
- TC-FA-FAAC-362 (Search pada kolom yang disembunyikan) ada di spec 132.
- Nama literal Pre-setup (sembilan kelas contoh) dan B-DEC dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai tampil persis (`1,500.99`); B-DEC milik spec ini dibersihkan di hook `after` dan kode literal yang sama dibuat lewat UI oleh spec 131 (suite serial, tiap spec membersihkan kelas yang dibuatnya; S-06, S-12).
- Temuan untuk QA: TC-FA-FAAC-705 memakai B-DEC sebagai "hasil TC pembuatan B-DEC" (TC-FA-FAAC-704); spec menyiapkannya lewat seeding API karena spec tidak boleh menumpang hasil spec lain (S-06).
