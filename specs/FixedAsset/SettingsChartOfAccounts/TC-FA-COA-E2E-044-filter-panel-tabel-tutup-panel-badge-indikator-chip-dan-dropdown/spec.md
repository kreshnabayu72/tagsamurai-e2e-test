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
- Data Pre-setup yang hanya dibaca dan tidak diubah (disediakan tim FE lewat `fixtures/settings-chart-of-accounts.json`, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):
  - P1 `Fixture.settingsChartOfAccounts.p1` (Function Depreciation Expense, Active).
  - P2 `Fixture.settingsChartOfAccounts.p2` (Function Capitalization Offset, Active).
  - P3 `Fixture.settingsChartOfAccounts.p3` (Function Gain on Disposal, Inactive).
  - P4 `Fixture.settingsChartOfAccounts.p4` (Function Asset Cost, Inactive).
  - P5 `Fixture.settingsChartOfAccounts.p5` (Function Capitalization Offset, Active).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-214: Tutup panel dengan klik di luar panel membuang perubahan yang belum di-Apply

1. Klik ikon Filter di toolbar, pilih Active = `Active`, klik `[Apply]`
2. Pilih Function = `Depreciation Expense` tanpa klik `[Apply]`
3. Klik di area luar Filter Panel
4. Verifikasi tabel tetap menampilkan hasil filter Active = `Active` (baris P1 dan P2 tampil, baris P3 `Fixture.settingsChartOfAccounts.p3.code` tidak tampil)
5. Klik ikon Filter di toolbar untuk membuka kembali Filter Panel
6. Verifikasi panel menampilkan Active = `Active` (ter-Apply terakhir)
7. Verifikasi field Function kosong
8. Klik `Clear all`

### TC-FA-COA-215: Tutup panel dengan klik ulang ikon Filter membuang perubahan yang belum di-Apply

9. Klik ikon Filter di toolbar, pilih Active = `Active`, klik `[Apply]`
10. Pilih Function = `Depreciation Expense` tanpa klik `[Apply]`
11. Klik ikon Filter kembali untuk menutup panel
12. Verifikasi tabel tetap menampilkan hasil filter Active = `Active` (baris P1 dan P2 tampil, baris P3 tidak tampil)
13. Klik ikon Filter di toolbar untuk membuka kembali Filter Panel
14. Verifikasi panel menampilkan Active = `Active` (ter-Apply terakhir)
15. Verifikasi field Function kosong
16. Klik `Clear all`

### TC-FA-COA-218: Indikator filter aktif, badge titik pada ikon Filter

17. Klik ikon Filter di toolbar, pilih Active = `Inactive`, klik `[Apply]`
18. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel terbuka
19. Tutup Filter Panel dengan klik ikon Filter
20. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel tertutup
21. Klik ikon Filter di toolbar untuk membuka panel, klik `Clear Field`, lalu klik `[Apply]`
22. Verifikasi badge titik pada ikon Filter hilang

### TC-FA-COA-329: Search internal dropdown filter menyaring opsi

23. Klik ikon Filter di toolbar, buka dropdown Function
24. Ketik `Gain` di kotak pencarian dropdown
25. Verifikasi opsi dropdown hanya memuat `Gain on Disposal`
26. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-COA-330: Chip filter dihapus lewat (X) dan membatalkan centang di dropdown

27. Klik ikon Filter di toolbar, pilih Active = `Active` dan Function = `Capitalization Offset`, klik `[Apply]`
28. Klik `(X)` pada chip Active
29. Verifikasi chip Active hilang
30. Verifikasi tabel mengikuti filter Function saja (baris P2 dan P5 tampil, baris P1 tidak tampil)
31. Klik ikon Filter di toolbar untuk membuka Filter Panel dan buka dropdown Active
32. Verifikasi dropdown Active tidak lagi memiliki opsi tercentang
33. Klik `Clear all`

### TC-FA-COA-331: Uncheck opsi di dalam dropdown menghapus chip yang sesuai setelah Apply

34. Klik ikon Filter di toolbar, pilih Function = `Capitalization Offset` dan `Gain on Disposal`, klik `[Apply]`
35. Klik ikon Filter di toolbar untuk membuka Filter Panel, hapus centang `Gain on Disposal`, klik `[Apply]`
36. Verifikasi chip Function menampilkan hanya `Capitalization Offset`
37. Verifikasi tabel hanya memuat akun Capitalization Offset (baris P2 dan P5 tampil, baris P3 tidak tampil)
38. Klik `Clear all`

## Notes

- Spec memuat 38 langkah (sekitar 35 langkah). Alasan: satu kelas harness (fungsional Filter), satu halaman, satu dataset read-only (P1 sampai P5); enam TC berurutan pada Filter Panel yang sama; Expected bermajemuk dipecah satu Verifikasi per klausa (S-01); tiap blok diakhiri pembersihan filter (S-09) sehingga tidak ada state yang menular antar-TC.
- Langkah penghubung (S-03): klik `[Apply]` pada langkah 1, 9, 17, 21, 27, 34, 35 (Expected membutuhkan tabel terfilter atau badge); langkah 8, 16, 33, 38 (`Clear all` membersihkan filter, S-09); langkah 19 dan 26 (menutup panel); langkah 5, 13, 31 (membuka Filter Panel kembali, TC menyebutnya langkah 4).
- Langkah 4 dan 12 memverifikasi baris yang harus tampil sebelum asersi absence (8b.2).
- Langkah 31 menggabungkan membuka Filter Panel dan dropdown Active karena TC-FA-COA-330 langkah 3 hanya menyebut "perhatikan dropdown Active".
- Temuan untuk QA:
  - TC-FA-COA-218 langkah 3 "klik Clear Field lalu Apply" ditulis ulang apa adanya; TC tidak menyebut apakah `Clear Field` pada field Active atau seluruh panel, spec memakai `Clear Field` pada field Active.
  - TC-FA-COA-330 tidak menyebut apakah penghapusan chip lewat `(X)` langsung diterapkan atau butuh `[Apply]`; spec mengasumsikan langsung diterapkan.
  - TC-FA-COA-214 dan 215 langkah 4 menyebut "buka kembali Filter Panel" tanpa memastikan panel tertutup; langkah 3 dan 11 sudah menutupnya.
