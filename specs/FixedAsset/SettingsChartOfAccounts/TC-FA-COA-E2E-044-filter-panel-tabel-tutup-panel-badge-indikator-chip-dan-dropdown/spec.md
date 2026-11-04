---
id: TC-FA-COA-E2E-044-filter-panel-tabel-tutup-panel-badge-indikator-chip-dan-dropdown
title: "Filter Panel Tabel: Tutup Panel, Badge Indikator, Chip, dan Dropdown"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-214
  - TC-FA-COA-215
  - TC-FA-COA-218
  - TC-FA-COA-329
  - TC-FA-COA-330
  - TC-FA-COA-331
coverage:
  web: automated
---

# Filter Panel Tabel: Tutup Panel, Badge Indikator, Chip, dan Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup yang hanya dibaca dan tidak diubah (disediakan tim FE lewat `Fixture.settingsChartOfAccounts.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):
  - P1 `Fixture.settingsChartOfAccounts.p1` (Function Depreciation Expense, Active).
  - P2 `Fixture.settingsChartOfAccounts.p2` (Function Capitalization Offset, Active).
  - P3 `Fixture.settingsChartOfAccounts.p3` (Function Gain on Disposal, Inactive).
  - P5 `Fixture.settingsChartOfAccounts.p5` (Function Capitalization Offset, Active).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-214: Tutup panel dengan klik di luar panel membuang perubahan yang belum di-Apply

1. Klik ikon Filter di toolbar, pilih Active = `Active`, klik `[Apply]`
2. Pilih Function = `Depreciation Expense` tanpa klik `[Apply]`
3. Klik di area luar Filter Panel
4. Verifikasi sedikitnya satu baris akun tampil pada halaman 1
5. Verifikasi seluruh baris di halaman 1 berstatus Active (tabel tetap menampilkan hasil filter Active = `Active`)
6. Verifikasi baris P3 (`Fixture.settingsChartOfAccounts.p3.code`) tidak tampil
7. Klik ikon Filter di toolbar untuk membuka kembali Filter Panel
8. Verifikasi panel menampilkan Active = `Active` (ter-Apply terakhir)
9. Verifikasi field Function kosong
10. Klik `Clear all`

### TC-FA-COA-215: Tutup panel dengan klik ulang ikon Filter membuang perubahan yang belum di-Apply

11. Klik ikon Filter di toolbar, pilih Active = `Active`, klik `[Apply]`
12. Pilih Function = `Depreciation Expense` tanpa klik `[Apply]`
13. Klik ikon Filter kembali untuk menutup panel
14. Verifikasi sedikitnya satu baris akun tampil pada halaman 1
15. Verifikasi seluruh baris di halaman 1 berstatus Active (tabel tetap menampilkan hasil filter Active = `Active`)
16. Verifikasi baris P3 (`Fixture.settingsChartOfAccounts.p3.code`) tidak tampil
17. Klik ikon Filter di toolbar untuk membuka kembali Filter Panel
18. Verifikasi panel menampilkan Active = `Active` (ter-Apply terakhir)
19. Verifikasi field Function kosong
20. Klik `Clear all`

### TC-FA-COA-218: Indikator filter aktif, badge titik pada ikon Filter

21. Klik ikon Filter di toolbar, pilih Active = `Inactive`, klik `[Apply]`
22. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel terbuka
23. Tutup Filter Panel dengan klik ikon Filter
24. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel tertutup
25. Klik ikon Filter di toolbar untuk membuka panel, klik `Clear Field`, lalu klik `[Apply]`
26. Verifikasi badge titik pada ikon Filter hilang

### TC-FA-COA-329: Search internal dropdown filter menyaring opsi

27. Buka dropdown Function pada Filter Panel yang masih terbuka sesudah `[Apply]`
28. Ketik `Gain` di kotak pencarian dropdown
29. Verifikasi opsi dropdown hanya memuat `Gain on Disposal`
30. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-COA-330: Chip filter dihapus lewat (X) dan membatalkan centang di dropdown

31. Klik ikon Filter di toolbar, pilih Active = `Active` dan Function = `Capitalization Offset`, klik `[Apply]`
32. Klik `(X)` pada chip Active
33. Verifikasi chip Active hilang
34. Verifikasi tabel mengikuti filter Function saja (baris P2 `Fixture.settingsChartOfAccounts.p2.code` dan P5 `Fixture.settingsChartOfAccounts.p5.code` tampil, baris P1 `Fixture.settingsChartOfAccounts.p1.code` tidak tampil)
35. Pada Filter Panel yang masih terbuka sesudah `[Apply]`, buka dropdown Active
36. Verifikasi dropdown Active tidak lagi memiliki opsi tercentang
37. Klik `Clear all`

### TC-FA-COA-331: Uncheck opsi di dalam dropdown menghapus chip yang sesuai setelah Apply

38. Klik ikon Filter di toolbar, pilih Function = `Capitalization Offset` dan `Gain on Disposal`, klik `[Apply]`
39. Hapus centang `Gain on Disposal` pada Filter Panel yang masih terbuka, klik `[Apply]`
40. Verifikasi chip Function menampilkan hanya `Capitalization Offset`
41. Verifikasi tabel hanya memuat akun Capitalization Offset (baris P2 `Fixture.settingsChartOfAccounts.p2.code` dan P5 `Fixture.settingsChartOfAccounts.p5.code` tampil, baris P3 `Fixture.settingsChartOfAccounts.p3.code` tidak tampil)
42. Klik `Clear all`

## Notes

- Spec memuat 42 langkah (sekitar 35 langkah). Alasan: satu kelas harness (fungsional Filter), satu halaman, satu dataset read-only (P1 sampai P5); enam TC berurutan pada Filter Panel yang sama; Expected bermajemuk dipecah satu Verifikasi per klausa (S-01); tiap blok diakhiri pembersihan filter (S-09) sehingga tidak ada state yang menular antar-TC.
- Langkah penghubung (S-03): klik `[Apply]` pada langkah 1, 11, 21, 25, 31, 38, 39 (Expected membutuhkan tabel terfilter atau badge); langkah 10, 20, 37, 42 (`Clear all` membersihkan filter, S-09); langkah 23 dan 30 (menutup panel); langkah 7 dan 17 (membuka Filter Panel kembali, TC menyebutnya langkah 4); langkah 4 dan 14 (`Verifikasi` sedikitnya satu baris akun tampil pada halaman 1, anchor positif sebelum asersi universal dan absence, 8b.2).
- Langkah 4 sampai 6 dan 14 sampai 16: filter Active = `Active` meloloskan sekitar 85 akun (10 baris per halaman, urut Account Code A-Z), sehingga P2 `6-2001` (sekitar posisi 35) berada di luar halaman 1 dan P1 `5-6001` (posisi 8 atau lebih, bergantung pada akun seed lain) tidak dijamin di halaman 1; keduanya tidak dipakai sebagai pembanding (S-14, R-23). Expected TC-FA-COA-214 dan 215 hanya menyebut tabel tetap menampilkan hasil filter Active, jadi spec lebih dulu mengasersi sedikitnya satu baris tampil pada halaman 1 (pembanding presence, 8b.2; tanpa itu tabel kosong meloloskan asersi universal dan absence), lalu seluruh baris halaman 1 berstatus Active, lalu baris P3 yang Inactive tidak tampil, masing-masing satu `Verifikasi` (S-01). Pada langkah 34 dan 41 (filter Function = `Capitalization Offset`, P2 posisi pertama dan P5 di sekitar posisi empat) kedua akun berada di halaman 1.
- Langkah 27, 35, dan 39 dikerjakan pada Filter Panel yang masih terbuka sesudah `[Apply]` (prd-conventions.md §9.8), sehingga tidak ada klik ikon Filter yang menutup panel; TC-FA-COA-330 langkah 3 hanya menyebut "perhatikan dropdown Active".
- Temuan untuk QA:
  - TC-FA-COA-214, 215, 218, 330, dan 331 tidak menyatakan apakah `Clear all` menutup Filter Panel; langkah 11, 21, dan 38 mengasumsikan panel tertutup sesudah `Clear all` dan membukanya lewat ikon Filter.
  - TC-FA-COA-218 langkah 3 "klik Clear Field lalu Apply" ditulis ulang apa adanya; TC tidak menyebut apakah `Clear Field` pada field Active atau seluruh panel, spec memakai `Clear Field` pada field Active.
  - TC-FA-COA-330 tidak menyebut apakah penghapusan chip lewat `(X)` langsung diterapkan atau butuh `[Apply]`; spec mengasumsikan langsung diterapkan.
  - TC-FA-COA-214 dan 215 langkah 4 menyebut "buka kembali Filter Panel" tanpa memastikan panel tertutup; langkah 3 dan 13 sudah menutupnya.
