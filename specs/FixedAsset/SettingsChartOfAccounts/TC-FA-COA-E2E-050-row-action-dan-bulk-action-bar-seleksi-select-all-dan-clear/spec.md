---
id: TC-FA-COA-E2E-050-row-action-dan-bulk-action-bar-seleksi-select-all-dan-clear
title: "Row Action dan Bulk Action Bar: Seleksi, Select All, dan Clear"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-306
  - TC-FA-COA-307
  - TC-FA-COA-308
  - TC-FA-COA-309
  - TC-FA-COA-310
  - TC-FA-COA-328
coverage:
  web: automated
---

# Row Action dan Bulk Action Bar: Seleksi, Select All, dan Clear

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Satu ganti akun eksplisit di langkah 43 dan 44 (TC-309, client uji P110); hook `after` mengembalikan sesi ke akun default suite.
- Akun Pre-setup (hanya dibaca dan tidak diubah; identitas dibaca dari `Fixture.settingsChartOfAccounts.p<N>`: `.code` Account Code dan `.name` Account Name; kunci ditetapkan tim FE; fixture belum ada):

  | Akun | Account Code | Account Name | Status |
  |---|---|---|---|
  | P1 | `5-6001` | Depreciation Expense – Admin | Active |
  | P3 | `4-7001` | Gain on Disposal | Inactive |
  | P5 | `CAP-6100` | Capitalization Clearing – Repairs | Active |

- Jumlah total akun client default (N pada `Select All (N records)`) lebih dari 10 dan diturunkan dari seeding Pre-setup P1 sampai P117, dicatat di fixture oleh seed (`Fixture.settingsChartOfAccounts.totalAkun`, 8b.10).
- Client uji tabel 25 akun (Pre-setup P110, plan Growth, tepat 25 akun Active dan Inactive, di bawah Selection Limit client itu, akun P1 termasuk) dan akun Total Control client itu `totalControlFixedAsset_automated_{namaCompanyP110}@qwertysystem.net` dengan password `Spectra.env.FA_TC_PASSWORD`: disediakan tim FE/BE (lihat Seed dan pemulihan di `suite.md`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Ukuran halaman tabel default 10; spec memakai ukuran 100 sementara pada langkah 36 dan memulihkannya pada langkah 42.
- Spec tidak menulis data: seleksi checkbox adalah state sisi klien. Tidak ada pembersihan data selain pemulihan ukuran halaman dan Search.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`); untuk akun client P110 flag itu disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-306: Screening overlay row action

1. Ketik Search `Fixture.settingsChartOfAccounts.p1.code`, tekan Enter
2. Verifikasi baris akun P1 tampil di tabel
3. Klik tombol ⋯ pada baris akun P1
4. Verifikasi overlay memuat aksi `Edit` dengan ikon `Edit2Line` (severity dark)
5. Verifikasi overlay memuat aksi `Delete` dengan ikon `DeleteBin6Line` (severity danger)
6. Verifikasi overlay tidak memuat `Activate` dan `Deactivate`
7. Tekan `Esc` untuk menutup overlay

### TC-FA-COA-307: Screening Bulk Action Bar

8. Centang checkbox baris akun P1
9. Klik `(←)` pada kotak Search
10. Verifikasi counter Bulk Action Bar `1 Account selected`
11. Verifikasi Bulk Action Bar memuat `Select All (N records)` dengan N total baris
12. Verifikasi Bulk Action berisi `Deactivate` dan `Delete`
13. Verifikasi ikon `(X)` tampil pada Bulk Action Bar
14. Ketik Search `Fixture.settingsChartOfAccounts.p5.code`, tekan Enter
15. Centang checkbox baris akun P5
16. Verifikasi counter Bulk Action Bar `2 Accounts selected`
17. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p3.code`, tekan Enter
18. Centang checkbox baris akun P3
19. Verifikasi counter Bulk Action Bar `3 Accounts selected`
20. Verifikasi Bulk Action memuat `Activate` (ikon `CheckLine`, severity dark), `Deactivate` (ikon `CloseLine`, severity dark), dan `Delete` (ikon `DeleteBin6Line`, severity danger)

### TC-FA-COA-310: Ikon (X) membersihkan seleksi

21. Klik ikon `(X)` pada Bulk Action Bar
22. Verifikasi seluruh seleksi dilepas (checkbox baris akun P3 tidak tercentang)
23. Verifikasi Bulk Action Bar tertutup
24. Verifikasi tidak ada dialog yang tampil
25. Verifikasi switch Status akun P3 tetap Inactive
26. Klik `(←)` pada kotak Search

### TC-FA-COA-308: Checkbox header dan state indeterminate

27. Centang checkbox baris pertama di tabel
28. Verifikasi checkbox header berstatus indeterminate
29. Klik checkbox header
30. Verifikasi seluruh 10 baris di halaman tercentang
31. Verifikasi counter Bulk Action Bar `10 Accounts selected`
32. Klik checkbox header lagi
33. Verifikasi seluruh seleksi halaman dilepas
34. Verifikasi Bulk Action Bar tertutup

### TC-FA-COA-328: Seleksi dipertahankan saat Search dikosongkan

35. Ketik Search `Depreciation`, tekan Enter
36. Pilih ukuran halaman 100
37. Centang checkbox baris akun P1
38. Klik `(←)` pada kotak Search
39. Verifikasi checkbox baris akun P1 tetap tercentang
40. Verifikasi Bulk Action Bar tetap tampil dengan counter `1 Account selected`
41. Klik ikon `(X)` pada Bulk Action Bar
42. Pilih kembali ukuran halaman 10

### TC-FA-COA-309: Select All lintas halaman pada client P110

43. Klik Logout dari akun aktor default
44. Login sebagai Total Control client uji P110, lalu buka Fixed Asset > Settings > Accounting > Chart of Accounts
45. Verifikasi tabel menampilkan 10 baris pada halaman pertama
46. Centang satu baris
47. Klik `Select All (25 records)`
48. Verifikasi seluruh 25 akun terpilih dengan counter `25 Accounts selected`
49. Verifikasi tombol berubah menjadi `Unselect All`
50. Uncheck satu baris
51. Verifikasi tombol kembali `Select All (25 records)`
52. Verifikasi counter `24 Accounts selected`
53. Klik `Select All (25 records)`
54. Klik `Unselect All`
55. Verifikasi seluruh seleksi lintas halaman dilepas
56. Verifikasi Bulk Action Bar tertutup

## Notes

- Alasan spec di atas sekitar 35 langkah (56 langkah): seluruh blok memakai satu halaman, satu Bulk Action Bar, satu kelas harness (fungsional) dan berdiri sendiri; seleksi dibersihkan di antara blok sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Selisih jumlah langkah terhadap TC sumber berasal dari Search untuk membuka baris target (8b.13), bukan dari asersi tambahan.
- Langkah penghubung (S-03): langkah 1, 14, 17, 35 (Search untuk menemukan baris target, R-16); langkah 7 (menutup overlay); langkah 9, 26, 38 (menutup kotak Search dan mereset tabel); langkah 36 dan 42 (ukuran halaman 100 sementara agar baris P1 tampil dan pemulihannya); langkah 43 dan 44 (ganti akun ke client P110, TC-309); langkah 21 sampai 26 mengikuti TC-310; langkah 45 (`Verifikasi tabel menampilkan 10 baris pada halaman pertama`) bukan Expected TC-309 melainkan pengamatan penghubung untuk precondition c TC-309 (25 akun dengan ukuran halaman 10), agar `Select All (25 records)` bermakna lintas halaman.
- TC-310 langkah 1 (centang P1 dan P5) dipenuhi oleh seleksi P1, P5, dan P3 yang dibangun TC-307 (langkah 8 sampai 18); kondisi awal TC-310 adalah seleksi yang mencakup P1 dan P5. Asersi "tidak ada perubahan data" diamati pada baris P3 yang tampil (langkah 25), karena P1 dan P5 tidak tampil pada hasil Search akhir.
- Pencarian P1 pada langkah 1 tetap berlaku sampai langkah 9 (centang P1 langsung tanpa mengosongkan lalu mengetik ulang Search yang sama).
- TC-308 memakai client default yang berisi lebih dari 10 akun hasil seed Pre-setup; TC-309 memakai client P110 (25 akun).
- Temuan untuk QA:
  - TC-309 menyebut client uji P110 tanpa email akun aktornya; spec memakai `totalControlFixedAsset_automated_{namaCompanyP110}@qwertysystem.net` dan `FA_TC_PASSWORD` sebagai asumsi yang perlu dikonfirmasi tim FE.
  - TC-328 tidak menyebut cara menemukan baris P1 pada hasil Search `Depreciation` dan setelah Search dikosongkan; spec memakai ukuran halaman 100 sebagai langkah penghubung.
  - TC-307 butir a menyebut "N total baris" tanpa nilai; N diturunkan dari seeding (Prerequisites).
  - TC-306 sampai TC-310 dan TC-328 tidak memiliki Post Condition yang membutuhkan langkah observasi tambahan.
