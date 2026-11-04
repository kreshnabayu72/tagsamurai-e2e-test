---
id: TC-FA-COA-E2E-043-filter-panel-tabel-periode-date-range-used-by-dan-kombinasi-and
title: "Filter Panel Tabel: Periode, Date Range, Used By, dan Kombinasi AND"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-77
  - TC-FA-COA-78
  - TC-FA-COA-181
  - TC-FA-COA-323
  - TC-FA-COA-324
coverage:
  web: automated
---

# Filter Panel Tabel: Periode, Date Range, Used By, dan Kombinasi AND

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup yang hanya dibaca dan tidak diubah (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):
  - P1 `Fixture.settingsChartOfAccounts.p1` (Account Code `5-6001`, Depreciation Expense, Active, Used By 0, Last Used in Journal kosong, Last Updated hari ini).
  - P2 `Fixture.settingsChartOfAccounts.p2` (Account Code `6-2001`, Function Capitalization Offset, Active, Used By 0, Last Used in Journal `Aug 2026`).
  - P3 `Fixture.settingsChartOfAccounts.p3` (Account Code `4-7001`, Function Gain on Disposal, Inactive).
  - P4 `Fixture.settingsChartOfAccounts.p4` (Account Code `1-1002`, Function Asset Cost, Inactive, Last Used in Journal `Mar 2025`, Last Updated lebih dari 30 hari sebelum hari ini).
  - P5 `Fixture.settingsChartOfAccounts.p5` (Account Code `CAP-6100`, Function Capitalization Offset, Active).
- Rentang tanggal Last Updated pada langkah 20 adalah hari ini sampai hari ini (nilai tanggal dihitung saat run).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-77: Filter Last Used in Journal berbasis periode bulan (inklusif)

1. Klik ikon Filter di toolbar
2. Buka filter Last Used in Journal
3. Verifikasi placeholder `Select period` (bukan "Select date")
4. Pilih rentang Jun 2026 sampai Oct 2026, klik `[Apply]`
5. Verifikasi tabel memuat baris P2 (`Fixture.settingsChartOfAccounts.p2.code`, Aug 2026)
6. Verifikasi baris P4 (`Fixture.settingsChartOfAccounts.p4.code`, Mar 2025) tidak tampil
7. Verifikasi akun dengan Last Used in Journal kosong tidak tampil (baris P1 `Fixture.settingsChartOfAccounts.p1.code` tidak tampil)
8. Ubah rentang menjadi Aug 2026 sampai Aug 2026, klik `[Apply]`
9. Verifikasi baris P2 (Aug 2026) tetap tampil (rentang inklusif)
10. Klik `Clear all`

### TC-FA-COA-78: Filter Used By min dan max untuk akun dengan Used By 0

11. Klik ikon Filter di toolbar
12. Verifikasi placeholder `Min` dan `Max` pada field Used By
13. Isi Used By Min `0` dan Max `0`, klik `[Apply]`
14. Verifikasi tabel memuat akun berstatus Used By 0 (sedikitnya satu baris akun tampil pada halaman 1)
15. Verifikasi nilai Used By pada setiap baris di halaman 1 adalah "0" dan ditampilkan sebagai teks biasa (bukan link)
16. Klik `Clear all`

### TC-FA-COA-181: Filter Last Updated, date range dengan placeholder "Select date"

17. Klik ikon Filter di toolbar
18. Verifikasi field berlabel `Last Updated` bertipe date range
19. Verifikasi placeholder field Last Updated `Select date`
20. Pilih rentang hari ini sampai hari ini, klik `[Apply]`
21. Verifikasi tabel memuat baris P1 (`Fixture.settingsChartOfAccounts.p1.code`)
22. Verifikasi baris P4 (`Fixture.settingsChartOfAccounts.p4.code`) tidak tampil
23. Verifikasi chip filter Last Updated aktif dengan `Clear all`
24. Klik `Clear all`

### TC-FA-COA-323: Filter dua field berlaku bersamaan (AND)

25. Klik ikon Filter di toolbar
26. Pilih Active = `Active` dan Function = `Capitalization Offset`
27. Klik `[Apply]`
28. Verifikasi tabel memuat akun yang Active dan Function-nya Capitalization Offset (baris P2 dan P5 tampil)
29. Verifikasi tidak ada akun Inactive atau Function lain pada tabel
30. Verifikasi chip filter Active dan Function tampil dengan `Clear all`
31. Klik `Clear all`

### TC-FA-COA-324: Filter diterapkan lebih dulu lalu Search, hasil irisan keduanya

32. Klik ikon Filter di toolbar
33. Pilih Active = `Active`, klik `[Apply]`
34. Ketik Search `Depreciation`, tekan Enter
35. Verifikasi tabel memuat baris P1 (`Fixture.settingsChartOfAccounts.p1.code`)
36. Verifikasi setiap baris pada tabel Active dan mengandung `Depreciation`
37. Verifikasi tidak ada akun Inactive pada tabel
38. Verifikasi chip filter Active tetap tampil
39. Klik `Clear all`
40. Klik `(←)` pada kotak Search

## Notes

- Spec melewati sekitar 35 langkah (40 langkah). Alasan: satu kelas harness (fungsional Filter), satu halaman, satu dataset read-only (P1 sampai P5); lima TC berurutan pada Filter Panel yang sama; Expected bermajemuk dipecah satu Verifikasi per klausa (S-01); tiap blok berdiri sendiri dan diakhiri `Clear all`.
- Langkah penghubung (S-03): langkah 4, 8, 13, 20, 27, 33 (klik `[Apply]`, TC tidak selalu menuliskannya tetapi Expected membutuhkan tabel terfilter); langkah 10, 16, 24, 31, 39 (`Clear all` membersihkan filter sebelum TC berikutnya, S-09); langkah 40 (`(←)` menutup kotak Search dan mereset tabel); langkah 1, 11, 17, 25, 32 (membuka Filter Panel).
- Langkah 5, 21, dan 35 memverifikasi baris yang harus tampil sebelum asersi absence (8b.2).
- Langkah 14 dan 15: filter Used By 0 meloloskan sekitar 96 akun (10 baris per halaman, urut Account Code A-Z); P1 (sekitar posisi 22) dan P2 (sekitar posisi 45) tidak dijamin di halaman 1, jadi spec mengasersi pembanding generik halaman 1 (sedikitnya satu baris tampil) lalu nilai Used By `0` pada setiap baris halaman 1 (S-14, R-23).
- Temuan untuk QA:
  - TC-FA-COA-77, 78, 181, dan 323 tidak menyebut klik `[Apply]` padahal Expected membutuhkan tabel terfilter; spec menambahkannya.
  - TC-FA-COA-77 butir c ("akun dengan Last Used kosong tidak tampil") tidak menyebut akun sasaran; spec memakai P1 (Last Used in Journal kosong).
  - TC-FA-COA-78 butir b ("menampilkan 0 sebagai teks biasa") tidak menyebut cara memeriksanya; spec mengasersi sel Used By bukan link.
  - TC-FA-COA-181 memakai Last Updated P1 hari ini dan P4 lebih dari 30 hari sebelum hari ini (precondition seeding, disediakan tim FE/BE).
