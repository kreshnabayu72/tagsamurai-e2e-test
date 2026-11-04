---
id: TC-FA-LBL-E2E-056-modal-changelog-labels-filter-per-kolom
title: "Modal Changelog: Labels: Filter Panel per kolom"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-03/filter-panel
  - FALB:obl/T-ALB-03/filter/FLD-11
  - FALB:obl/T-ALB-03/filter/FLD-12
  - FALB:obl/T-ALB-03/filter/FLD-13
  - FALB:obl/T-ALB-03/filter/FLD-14
  - FALB:obl/T-ALB-03/filter/FLD-17
  - FALB:defaults-ordering-spec/default-filter-tabel
coverage:
  web: automated
---

# Modal Changelog: Labels: Filter Panel per kolom

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Pelaku kedua seeding lewat sesi API: `DU-31`, env `FA_TC2_EMAIL` dan `FA_TC2_PASSWORD`.
- Data uji `DU-62` (Dataset Changelog: Labels), bersuffix `{runId}-056`, label `Log-{runId}-056-nn`, dibuat lewat sesi API di hook `before` dengan urutan tulis: (a) Create label `-04` sampai `-09` oleh `DU-01`; (b) Create `-01` oleh `DU-01`, Edit Label Name `-01` menjadi `-01-baru` oleh `DU-31`, Edit Color `-01` dari `#3B82F6` ke `#EF4444` oleh `DU-31`, Create `-02` oleh `DU-31`, Create `-03` oleh `DU-01`, lalu Delete `-03` oleh `DU-01`. Total 12 entri; semua entri tertulis pada hari run. Hook `after` menghapus label `-01-baru`, `-02`, dan `-04` sampai `-09` lewat sesi API.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label dan membaca entri Changelog, disediakan tim FE/BE. Tanggal "hari ini" dan "kemarin" pada field Date mengikuti Time Zone General Settings akun `DU-01`.
- State global: tidak ada yang diubah; Filter Panel adalah state tampilan Modal Changelog. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik ikon Changelog pada toolbar tabel
2. Ketik Search `DU-62`, tekan Enter
3. Verifikasi baris entri milik `DU-62` tampil pada tabel Modal Changelog

### FALB:defaults-ordering-spec/default-filter-tabel: Tidak ada filter ter-Apply saat Modal Changelog dibuka

4. Klik ikon Filter pada toolbar Modal Changelog
5. Verifikasi Filter Panel tampil di bawah toolbar dengan field Date (placeholder `Select date`), Action (`All actions`), Label Name (`All labels`), Field (`All fields`), dan Modified By (`All users`) tanpa nilai terpilih

### FALB:obl/T-ALB-03/filter-panel: Filter Panel: Apply, Clear Field, dan kombinasi antar field

6. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan, serta field Date, Action, Label Name, dan Field di baris pertama sedangkan Modified By di baris kedua
7. Pilih opsi `Edit` pada dropdown Action dan nama lengkap akun `DU-31` pada dropdown Modified By, klik `[Apply]`
8. Verifikasi baris Edit dengan Field `Label Name` milik `DU-62` tampil
9. Verifikasi baris Create label `-02` milik `DU-62` oleh `DU-31` tidak tampil
10. Klik `[Clear Field]`, klik `[Apply]`
11. Verifikasi baris Create label `-02` milik `DU-62` tampil kembali

### FALB:obl/T-ALB-03/filter/FLD-11: Filter kolom Date

12. Pilih rentang tanggal hari ini sampai hari ini pada field Date, klik `[Apply]`
13. Verifikasi baris Create label `-02` milik `DU-62` tampil
14. Ganti rentang tanggal pada field Date menjadi kemarin sampai kemarin, klik `[Apply]`
15. Verifikasi empty state Modal Changelog menampilkan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
16. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-03/filter/FLD-12: Filter kolom Action

17. Ketik `Edi` pada kotak search dropdown Action
18. Verifikasi opsi `Edit` tampil sedangkan opsi `Create` dan `Delete` tidak tampil pada dropdown Action
19. Pilih opsi `Edit`, klik `[Apply]`
20. Verifikasi baris Edit dengan Field `Color` milik `DU-62` tampil
21. Verifikasi baris Create label `-02` milik `DU-62` tidak tampil
22. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-03/filter/FLD-13: Filter kolom Label Name

23. Ketik nama label `-02` milik `DU-62` pada kotak search dropdown Label Name
24. Verifikasi opsi label `-02` milik `DU-62` tampil pada dropdown Label Name
25. Pilih opsi label `-02`, klik `[Apply]`
26. Verifikasi baris Create label `-02` milik `DU-62` tampil
27. Verifikasi baris Create label `-03` milik `DU-62` tidak tampil
28. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-03/filter/FLD-14: Filter kolom Field

29. Ketik `Col` pada kotak search dropdown Field
30. Verifikasi opsi `Color` tampil sedangkan opsi `Label Name` tidak tampil pada dropdown Field
31. Pilih opsi `Color`, klik `[Apply]`
32. Verifikasi baris Edit dengan Field `Color` milik `DU-62` tampil
33. Verifikasi baris Create label `-02` milik `DU-62` tidak tampil
34. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-03/filter/FLD-17: Filter kolom Modified By

35. Ketik nama lengkap akun `DU-31` pada kotak search dropdown Modified By
36. Verifikasi opsi nama lengkap akun `DU-31` tampil pada dropdown Modified By
37. Pilih opsi nama lengkap akun `DU-31`, klik `[Apply]`
38. Verifikasi baris Create label `-02` milik `DU-62` oleh `DU-31` tampil
39. Verifikasi baris Create label `-03` milik `DU-62` oleh `DU-01` tidak tampil

## Notes

- Langkah penghubung (S-03): langkah 1 membuka modal; langkah 2 mempersempit tabel ke entri `DU-62` (R-16); langkah 4 membuka Filter Panel; langkah 10, 16, 22, 28, dan 34 mengosongkan Filter sebelum blok berikutnya mengandalkan tabel penuh (S-09). Filter Panel tetap terbuka sesudah `[Apply]` (prd-conventions §9.8).
- Anchor positif (bagian 8b butir 2): langkah 3 membuktikan entri `DU-62` sudah termuat; asersi "tidak tampil" tiap blok (langkah 9, 21, 27, 33, 39) didahului asersi baris pembanding milik `DU-62` pada surface yang sama (langkah 8, 20, 26, 32, 38); empty state di langkah 15 didahului langkah 13 yang membuktikan filter Date hari ini menampilkan baris yang sama.
- Opsi dropdown Filter pada surface audit trail permanen diasersi sesudah mengetik di kotak search dropdown (bagian 8b butir 15c): langkah 17 sampai 18, 23 sampai 24, 29 sampai 30, dan 35 sampai 36.
- Kolom Old Value dan New Value tidak Filterable (Tabel 3 PRD §4.1.2), sehingga tidak ada blok Filter untuk `FLD-15` dan `FLD-16`.
- Filter Date: seeding lewat API tidak dapat memundurkan Date entri, sehingga dua kelompok Date dipisahkan sebagai rentang hari ini (entri `DU-62` tampil, termasuk batas inklusif satu hari) dan rentang kemarin (tidak ada entri `DU-62`, langkah 12 sampai 15). Perilaku rentang lebih dari satu hari tidak diasersi.
- Alasan spec melewati 35 langkah: seluruh blok satu kelas harness (fungsional Filter Panel Modal Changelog) dengan data `DU-62` yang sama; tiap blok kolom berdiri sendiri karena mengosongkan Filter di akhir blok (langkah 10, 16, 22, 28, 34) dan hanya mengandalkan baris `DU-62` hasil seeding hook. Pemecahan menambah login dan seeding per spec.
