---
id: TC-FA-COA-E2E-042-filter-panel-tabel-struktur-opsi-dan-multi-select
title: "Filter Panel Tabel: Struktur, Opsi, dan Multi-Select"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-75
  - TC-FA-COA-76
  - TC-FA-COA-180
  - TC-FA-COA-186
  - TC-FA-COA-322
coverage:
  web: automated
---

# Filter Panel Tabel: Struktur, Opsi, dan Multi-Select

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup yang hanya dibaca dan tidak diubah (disediakan tim FE lewat `fixtures/settings-chart-of-accounts.json`, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`): akun P1 sampai P5, P7, dan P8 ada sehingga keenam nilai Function dan kedua nilai Active ada di tabel.
  - P1 `Fixture.settingsChartOfAccounts.p1` (Function Depreciation Expense, Active).
  - P2 `Fixture.settingsChartOfAccounts.p2` (Function Capitalization Offset, Active).
  - P3 `Fixture.settingsChartOfAccounts.p3` (Function Gain on Disposal, Inactive).
  - P5 `Fixture.settingsChartOfAccounts.p5` (Function Capitalization Offset, Active).
- P40 (asumsi pre-setup, bukan data PRD): akun P1 terakhir diubah user A (`Fixture.settingsChartOfAccounts.p40.userAName`) dan akun P2 terakhir diubah user B (`Fixture.settingsChartOfAccounts.p40.userBName`); nilai ditulis dalam format Modified By `[First Name] [Last Initial]`.
- Opsi dropdown Function untuk langkah 41: `Asset Cost`, `Accumulated Depreciation`, `Depreciation Expense`, `Gain on Disposal`, `Loss on Disposal`, `Capitalization Offset`.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-322: Struktur Filter Panel tabel utama

1. Klik ikon Filter di toolbar
2. Verifikasi Filter Panel memuat enam field: Active, Function, Used By, Last Used in Journal, Modified By, dan Last Updated
3. Verifikasi field Active bertipe multi-select searchable dengan placeholder `All statuses`
4. Verifikasi field Function bertipe multi-select searchable dengan placeholder `All functions`
5. Verifikasi field Used By berupa Min dan Max numerik dengan placeholder `Min` dan `Max`
6. Verifikasi field Last Used in Journal bertipe date range bulan dengan placeholder `Select period`
7. Verifikasi field Modified By bertipe multi-select searchable dengan placeholder `All users`
8. Verifikasi field Last Updated bertipe date range dengan placeholder `Select date`
9. Verifikasi tombol `[Apply]` tersedia

### TC-FA-COA-75: Filter Active, opsi tanpa "None" dan hanya nilai yang ada di data

10. Verifikasi label field Filter `Active` dengan placeholder "All statuses"
11. Buka dropdown Active
12. Verifikasi opsi Active hanya memuat nilai yang ada di tabel (`Active` dan `Inactive`)
13. Verifikasi tidak ada opsi "None"
14. Pilih Active = `Inactive`, klik `[Apply]`
15. Verifikasi tabel hanya memuat akun Inactive (baris P3 `Fixture.settingsChartOfAccounts.p3.code` tampil, baris P1 `Fixture.settingsChartOfAccounts.p1.code` tidak tampil)
16. Verifikasi chip filter Active aktif dengan `Clear all`
17. Klik `Clear all`

### TC-FA-COA-76: Filter Function multi-select dengan opsi hanya dari data

18. Klik ikon Filter di toolbar
19. Verifikasi label field Filter `Function` dengan placeholder "All functions"
20. Buka filter Function
21. Verifikasi opsi filter hanya memuat nilai yang ada di data tabel
22. Verifikasi tidak ada opsi "None"
23. Pilih `Capitalization Offset` dan `Gain on Disposal`, klik `[Apply]`
24. Verifikasi tabel memuat akun dengan Function salah satu dari dua nilai yang dipilih (baris P2, P3, dan P5 tampil, baris P1 tidak tampil)
25. Klik `Clear all`

### TC-FA-COA-180: Filter Modified By, multi-select searchable

26. Klik ikon Filter di toolbar
27. Verifikasi field berlabel `Modified By` dengan placeholder "All users"
28. Buka opsi field Modified By
29. Verifikasi opsi hanya nilai Modified By yang ada di data tabel, termasuk user A dan user B
30. Verifikasi field dapat dicari (kotak pencarian tersedia di dalam dropdown)
31. Verifikasi field multi-select (opsi dapat dicentang lebih dari satu)
32. Pilih user A, klik `[Apply]`
33. Verifikasi tabel hanya memuat akun yang terakhir diubah user A (baris P1 tampil, baris P2 tidak tampil)
34. Verifikasi chip filter Modified By aktif dengan `Clear all`
35. Klik `Clear all`

### TC-FA-COA-186: Isi opsi dropdown filter bersumber dari data tabel

36. Klik ikon Filter di toolbar
37. Buka dropdown Active dan catat seluruh opsinya
38. Verifikasi opsi Active: `Active` dan `Inactive`
39. Verifikasi tidak ada opsi untuk nilai kosong pada dropdown Active
40. Buka dropdown Function dan catat seluruh opsinya
41. Verifikasi opsi Function: Asset Cost, Accumulated Depreciation, Depreciation Expense, Gain on Disposal, Loss on Disposal, Capitalization Offset
42. Verifikasi tidak ada opsi "None" dan tidak ada opsi untuk nilai kosong pada dropdown Function
43. Buka dropdown Modified By dan catat seluruh opsinya
44. Verifikasi opsi Modified By berupa nama user yang tercatat sebagai pengubah terakhir akun di tabel, termasuk user A dan user B
45. Verifikasi tidak ada opsi Modified By untuk user yang tidak pernah mengubah akun
46. Untuk setiap opsi yang dicatat pada langkah 37, 40, dan 43: pilih opsi itu saja, klik `[Apply]`, catat jumlah baris, lalu klik `Clear Field`
47. Verifikasi setiap opsi pada langkah 38, 41, dan 44 bila dipilih sendiri menghasilkan minimal satu baris
48. Verifikasi placeholder field Active `All statuses`
49. Verifikasi placeholder field Function `All functions`
50. Verifikasi placeholder field Modified By `All users`
51. Tutup Filter Panel dengan klik ikon Filter

## Notes

- Spec melewati sekitar 35 langkah (51 langkah). Alasan: satu kelas harness (fungsional Filter), satu halaman, satu dataset read-only (P1 sampai P8, P40); lima TC berurutan pada Filter Panel yang sama dengan Expected bermajemuk (TC-FA-COA-322 enam field, TC-FA-COA-186 lima butir) yang dipecah satu Verifikasi per klausa (S-01); langkah 46 adalah satu langkah berulang per opsi (8b.7) sehingga tidak menambah nomor langkah; tidak ada state yang berbagi antar-TC sehingga tiap blok berdiri sendiri. Jumlah langkah ditentukan jumlah klausa Expected, bukan topik.
- Langkah penghubung (S-03): langkah 14, 23, 32 (klik `[Apply]`, TC tidak menuliskan Apply tetapi Expected membutuhkan tabel terfilter); langkah 17, 25, 35 (`Clear all` membersihkan filter sebelum TC berikutnya, S-09); langkah 18, 26, 36 (membuka Filter Panel kembali); langkah 51 (menutup panel).
- Langkah 10 dan 19 mengasersi placeholder sebelum opsi dipilih karena placeholder hanya tampil saat field kosong; langkah 48 sampai 50 sesudah `Clear Field`.
- Langkah 15, 24, dan 33 memverifikasi baris yang memang harus tampil sebelum asersi absence (8b.2).
- Langkah 46 per opsi: Active (`Active`, `Inactive`), Function (enam nilai), Modified By (tiap nama user pada daftar yang dicatat).
- Temuan untuk QA:
  - TC-FA-COA-75 dan 76 tidak menyebut klik `[Apply]`; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-COA-180 butir c ("dapat dicari" dan "multi-select") tidak menyebut cara memeriksanya; spec mengasersi kotak pencarian di dalam dropdown dan opsi yang dapat dicentang lebih dari satu.
  - TC-FA-COA-186 butir c ("tidak ada opsi untuk user yang tidak pernah mengubah akun") membutuhkan daftar semua user yang pernah mengubah akun; kemampuan pembacaan daftar itu dari server perlu disediakan tim FE/BE.
  - TC-FA-COA-186 langkah 5 "catat jumlah baris" tidak punya Expected jumlah; hanya butir d (minimal satu baris) yang diasersi.
  - Opsi Modified By memakai format `[First Name] [Last Initial]` (R-14); P40 (user A dan user B) adalah asumsi pre-setup yang perlu dikonfirmasi tim FE.
