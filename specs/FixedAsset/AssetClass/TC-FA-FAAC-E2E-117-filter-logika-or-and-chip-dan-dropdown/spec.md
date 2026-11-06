---
id: TC-FA-FAAC-E2E-117-filter-logika-or-and-chip-dan-dropdown
title: "Filter Tabel Asset Class: Logika OR dan AND, Search di Dropdown, dan Chip pada Field Multi-Select"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-369
  - TC-FA-FAAC-370
  - TC-FA-FAAC-371
  - TC-FA-FAAC-372
  - TC-FA-FAAC-373
coverage:
  web: automated
---

# Filter Tabel Asset Class: Logika OR dan AND, Search di Dropdown, dan Chip pada Field Multi-Select

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Nilai yang dipakai asersi: Commercial Method IT-EQ = Declining Balance, MACHINERY = Units of Production (Accounts Incomplete), LAND = Not Depreciated, sisanya Straight Line; Tax Depreciation Class tersedia di dropdown: Bukan bangunan – Kelompok 1, Bukan bangunan – Kelompok 2, Bukan bangunan – Kelompok 3, Bangunan permanen, Tanah. Seed disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-369: Logika OR dalam satu field dan AND antar field

1. Klik icon Filter untuk membuka Filter Panel
2. Pilih Commercial Method = Declining Balance dan Units of Production, klik `[Apply]`
3. Verifikasi dua opsi pada Commercial Method digabung OR: hanya baris IT-EQ dan MACHINERY yang tampil, baris contoh lain (HEAVY-EQ) tidak tampil
4. Tambahkan Accounts = Incomplete, klik `[Apply]`
5. Verifikasi field berbeda digabung AND: hanya baris MACHINERY yang tampil, baris contoh lain (IT-EQ) tidak tampil
6. Klik `[Clear Field]`, lalu `[Apply]`

### TC-FA-FAAC-370: Search di dalam dropdown filter

7. Buka dropdown Tax Depreciation Class
8. Ketik `kelompok 2` pada kotak search dropdown
9. Verifikasi daftar opsi menyempit menjadi `Bukan bangunan – Kelompok 2`
10. Ganti isi kotak search dropdown dengan `xyz`
11. Verifikasi tidak ada opsi yang cocok sehingga tidak ada opsi yang dapat dipilih
12. Kosongkan kotak search dropdown dan tutup dropdown Tax Depreciation Class

### TC-FA-FAAC-371: Kemunculan chip pada field multi-select Filter Panel

13. Buka dropdown Commercial Method, centang Straight Line
14. Verifikasi chip `Straight Line` tampil di dalam field Commercial Method
15. Centang Declining Balance
16. Verifikasi chip `Declining Balance` tampil di samping chip pertama dan tidak menimpanya
17. Klik `[Clear Field]`

### TC-FA-FAAC-372: Hapus opsi terpilih lewat ikon X pada chip

18. Pilih Commercial Method = Straight Line dan Declining Balance
19. Klik ikon X pada chip Straight Line tanpa membuka dropdown
20. Verifikasi chip Straight Line hilang
21. Verifikasi chip Declining Balance tetap ada
22. Buka dropdown Commercial Method
23. Verifikasi checkbox Straight Line di dalam dropdown tidak tercentang
24. Verifikasi checkbox Declining Balance tetap tercentang
25. Klik `[Apply]`
26. Verifikasi hanya baris IT-EQ yang tampil, baris contoh lain (HEAVY-EQ) tidak tampil
27. Klik `[Clear Field]`, lalu `[Apply]`

### TC-FA-FAAC-373: Hapus opsi terpilih lewat uncheck di dalam dropdown

28. Pilih Commercial Method = Straight Line dan Declining Balance
29. Buka dropdown Commercial Method, hilangkan centang Straight Line
30. Verifikasi chip Straight Line hilang dari field
31. Verifikasi chip Declining Balance tetap ada
32. Klik `[Apply]`
33. Verifikasi hanya baris IT-EQ yang tampil, baris contoh lain (HEAVY-EQ) tidak tampil
34. Klik `[Clear Field]`, lalu `[Apply]`

## Notes

- Langkah penghubung (S-03): langkah 6, 27, 34 (melepas filter di akhir tiap TC, S-09), langkah 12 (mengosongkan kotak search dropdown dan menutup dropdown sebelum TC berikutnya, S-09), langkah 17 (melepas pilihan chip TC-FA-FAAC-371 yang tidak di-Apply, S-09). TC-FA-FAAC-371 tidak menekan `[Apply]`.
- Klausa "hanya baris ... yang tampil" dan "baris contoh lain tidak tampil" diasersi bersama pada satu `Verifikasi` dengan satu baris pembanding yang dijamin ada (8b butir 2).
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan nilai persis, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: tidak ada.
