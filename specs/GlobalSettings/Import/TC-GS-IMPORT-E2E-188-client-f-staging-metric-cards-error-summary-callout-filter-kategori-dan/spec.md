---
id: TC-GS-IMPORT-E2E-188-client-f-staging-metric-cards-error-summary-callout-filter-kategori-dan
title: "Client F: Staging Metric Cards, Error Summary Callout, filter kategori, dan retensi state (sidebar, Back, F5)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-459
  - TC-GS-IMPORT-460
  - TC-GS-IMPORT-461
  - TC-GS-IMPORT-462
  - TC-GS-IMPORT-463
  - TC-GS-IMPORT-467
  - TC-GS-IMPORT-468
  - TC-GS-IMPORT-469
  - TC-GS-IMPORT-470
  - TC-GS-IMPORT-473
  - TC-GS-IMPORT-764
  - TC-GS-IMPORT-765
coverage:
  web: automated
---

# Client F: Staging Metric Cards, Error Summary Callout, filter kategori, dan retensi state (sidebar, Back, F5)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client F (Hendra Wijaya) `totalControl_automated_qaTeam6@qwertysystem.net`, password `Spectra.env.GS_CLIENTF_TC_PASSWORD` (TC tidak menyebut password per akun, lihat Temuan untuk QA).
- Layar awal: hook `beforeEach` membuka Import > Brand Client F.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-10: draft Brand campuran Client F (5 `pending`, 3 `error`, 2 `duplicate`; Row # 1 `Nexus`, 2 `Orion`, 3 `Vertex`, 4 `Helios`, 5 `Samsung`, 6 `Pioneer`, 7 nama 121 karakter, 8 `Rocket 🚀`, 9 `Star ⭐`, 10 `Pioneer`), disiapkan oleh langkah 1 lewat skrip seed (reset Client F lalu seed; mekanisme skrip disediakan tim FE/BE). Nilai literal dipakai karena asersi bergantung pada urutan dan nama baris; Client F khusus draft campuran dan draft dibuang di hook `after`.
- Spec read-only: tidak ada mutasi draft; semua langkah hanya filter dan navigasi.
- Cleanup (hook `after`): draft Brand Client F dibuang lewat skrip reset.
- Kemampuan teknis: navigasi sidebar, tombol Back browser, `F5`.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Screening kartu dan Callout (TC-GS-IMPORT-459, 467)

1. Reset Client F lewat skrip fixture dan seed draft Brand D-10 (10 baris campuran)
2. Muat ulang halaman Import > Brand
3. Verifikasi kartu Total Rows 10 (Active, tone netral), Ready to Import 5, Errors 3, Duplicates 2 tampil di atas toolbar
4. Verifikasi keempat kartu Enabled
5. Verifikasi angka kartu Ready to Import sama dengan angka pada footer `[Import (5)]`
6. Verifikasi Staging Table memuat 5 baris berbadge `pending` (Row # 1, 2, 3, 4, dan 10), sama dengan angka kartu Ready to Import
7. Verifikasi Error Summary Callout bertone danger memuat baris pesan `Brand Name: Max. 120 characters` dengan badge "1 row", lalu `Brand name contains invalid characters` dengan badge "2 rows", sesuai urutan itu
8. Verifikasi baris pesan Callout tidak mencantumkan nomor baris
9. Verifikasi tiap baris pesan Callout memiliki `[View Data]` dan `[Delete All Rows]`
10. Verifikasi tidak ada `[Create Missing Divisions]` maupun `[Create Missing Positions]` di Tab Brand

### Klik kartu memfilter tabel (TC-GS-IMPORT-460, 463, 461, 462)

11. Klik kartu Errors
12. Verifikasi tabel hanya menampilkan 3 baris `error` (Row # 7, 8, dan 9)
13. Verifikasi kartu Errors Active (tone danger)
14. Verifikasi kartu Total Rows tidak lagi Active
15. Verifikasi angka kartu tetap Total Rows 10, Ready to Import 5, Errors 3, Duplicates 2
16. Klik kartu Total Rows
17. Klik kartu Errors
18. Verifikasi tabel menampilkan 3 baris `error`
19. Klik kartu Total Rows
20. Verifikasi tabel menampilkan 10 baris
21. Verifikasi kartu Total Rows Active (tone netral)
22. Verifikasi kartu Errors tidak lagi Active
23. Klik kartu Ready to Import
24. Verifikasi tabel menampilkan 5 baris `pending` (Row # 1, 2, 3, 4, dan 10)
25. Verifikasi kartu Ready to Import Active dengan tone primary, sama seperti badge `pending`
26. Verifikasi kartu Total Rows tidak lagi Active
27. Verifikasi footer tetap `[Import (5)]`
28. Klik kartu Total Rows
29. Klik kartu Duplicates
30. Verifikasi tabel menampilkan 2 baris `duplicate` (Row # 5 dan 6) dengan latar baris bertone warning
31. Verifikasi kartu Duplicates Active (tone warning)
32. Klik kartu Total Rows

### View Data dan chip filter kategori (TC-GS-IMPORT-468, 469, 470)

33. Klik `[View Data]` pada baris pesan `Brand name contains invalid characters`
34. Verifikasi kartu Errors Active
35. Verifikasi tabel hanya memuat 2 baris pelanggar kategori itu (Row # 8 dan 9) dan Row # 7 tidak tampil
36. Verifikasi chip "Showing rows with: Brand name contains invalid characters" dengan `[×]` tampil di atas tabel
37. Verifikasi angka kartu tetap Total Rows 10, Ready to Import 5, Errors 3, Duplicates 2
38. Verifikasi footer tetap `[Import (5)]`
39. Klik `[×]` pada chip
40. Verifikasi chip hilang dan tabel menampilkan seluruh 3 baris `error` (Row # 7, 8, dan 9)
41. Verifikasi kartu Errors tetap Active
42. Klik `[View Data]` pada baris pesan `Brand name contains invalid characters`
43. Klik kartu Ready to Import
44. Verifikasi chip filter kategori terlepas
45. Verifikasi kartu Ready to Import Active
46. Verifikasi tabel menampilkan 5 baris `pending`
47. Klik kartu Total Rows

### Retensi state (TC-GS-IMPORT-473, 764, 765)

48. Klik `[View Data]` pada baris pesan `Brand name contains invalid characters`
49. Verifikasi kartu Errors Active dan chip "Showing rows with: Brand name contains invalid characters" tampil
50. Klik menu Master Reference di sidebar
51. Klik menu Import di sidebar
52. Verifikasi halaman Import terbuka di Tab Brand dengan kartu Total Rows Active
53. Verifikasi tidak ada chip filter kategori
54. Verifikasi tabel menampilkan 10 baris
55. Klik `[View Data]` pada baris pesan `Brand name contains invalid characters`
56. Klik menu Master Reference di sidebar
57. Tekan tombol Back browser
58. Verifikasi halaman Import terbuka di Tab Brand dengan kartu Errors Active
59. Verifikasi chip "Showing rows with: Brand name contains invalid characters" tampil
60. Verifikasi tabel memuat 2 baris (Row # 8 dan 9)
61. Klik kartu Total Rows
62. Klik `[View Data]` pada baris pesan `Brand name contains invalid characters`
63. Tekan `F5`
64. Verifikasi halaman Import terbuka di Tab Brand dengan kartu Errors Active
65. Verifikasi chip "Showing rows with: Brand name contains invalid characters" tampil
66. Verifikasi tabel memuat 2 baris (Row # 8 dan 9)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 66 langkah, di atas 35 langkah. Alasan: satu dataset read-only (D-10) dan semua blok berdiri sendiri dengan pemulihan eksplisit antar blok (langkah 16, 28, 32, 47, 61); tidak ada mutasi, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Screening (TC-459, 467) di awal; retensi state yang meninggalkan halaman (TC-473, 764, 765) paling akhir.
- Langkah penghubung (klik kartu Total Rows pada langkah 16, 28, 32, 47, 61) melepas filter kartu dan kategori sebelum blok berikutnya (S-03, S-09). Langkah 1 dan 2 (reset Client F, seed D-10, muat ulang) adalah langkah pembuka penghubung (S-03): seed dipasang sesudah reset `beforeEach`.
- Langkah 17 sampai 22 adalah isi TC-GS-IMPORT-463 (Errors lalu Total Rows).
- Urutan 460, 463, 461, 462 menjaga kartu aktif pada Total Rows di tiap awal blok.
- Temuan untuk QA:
  - TC-GS-IMPORT-459 sampai 765 tidak mencantumkan rujukan data yang membuat D-10 selain TC-GS-IMPORT-458 (kolom TC dependensi); spec ini menyiapkannya lewat skrip seed (kemampuan disediakan tim FE/BE), bukan menumpang spec 187.
  - TC-GS-IMPORT-473 menyebut "menu Master Reference di sidebar" sebagai tujuan sementara; nama menu dipakai persis dari TC.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
