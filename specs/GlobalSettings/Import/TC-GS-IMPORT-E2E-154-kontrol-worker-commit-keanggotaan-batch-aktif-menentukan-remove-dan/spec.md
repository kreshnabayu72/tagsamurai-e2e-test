---
id: TC-GS-IMPORT-E2E-154-kontrol-worker-commit-keanggotaan-batch-aktif-menentukan-remove-dan
title: "Kontrol worker commit: keanggotaan batch aktif menentukan Remove dan checkbox Disabled atau Enabled"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-377
  - TC-GS-IMPORT-742
  - TC-GS-IMPORT-743
  - TC-GS-IMPORT-744
coverage:
  web: automated
---

# Kontrol worker commit: keanggotaan batch aktif menentukan Remove dan checkbox Disabled atau Enabled

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (kontrol worker commit) dan memakai Client E yang dipakai bersama spec commit lain; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; TC-377, 742, 743, 744 tidak merujuk D-47 pada kolom D-ref tetapi membutuhkannya):
  - Kontrol worker commit D-47 mode 2 (dijeda di dalam batch pertama sesudah uji ulang late-binding dan sebelum batch selesai) untuk TC-377, 742, 743; mode 4 (dijeda di dalam batch kedua sesudah batch pertama selesai) untuk TC-744.
  - Skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, hapus Brand hasil commit) dan seeding draft.
  - Jeda nyata: polling "muat ulang setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)" menunggu batch pertama selesai (TC-744), bukan menunggu jam.
- Data Dinamis (milik spec ini; draft dibuang oleh reset dan hasil commit batch pertama dihapus oleh reset):
  - D-56 `brand-250-impor.csv`: `Brand Impor 001` (#1) sampai `Brand Impor 250` (#250), semua valid dan unik (TC-377).
  - D-57 `brand-250-mixed.csv` (TC-742, 743, 744): 250 baris `Brand Impor nnn` kecuali baris #5 (`error`, Brand Name 121 karakter nilai sumber Brand pertama tabel D-41, badge saran AI `Samsung Electronics Indonesia`) dan baris #20 (`Samsung`, `duplicate` terhadap sistem); batch pertama = 100 baris `pending` pertama = baris #1-#4, #6-#19, #21-#102; baris #103 dan seterusnya di luar batch pertama; batch kedua = `Brand Impor 103` sampai `Brand Impor 202`; setelah batch pertama selesai, 150 baris tersisa urut: baris `error`, baris `duplicate`, lalu `Brand Impor 103` sampai `Brand Impor 250`.
  - Mock layanan AI mode normal D-40 (tabel D-41 dan D-42) untuk badge saran baris #5.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, hapus draft Client E, hapus Brand hasil commit batch pertama (TC-744), reset hasil commit terakhir, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-742: Remove dan checkbox di dalam batch aktif Disabled, di luar batch Enabled

1. Reset Client E (D-47) dan seed draft Brand D-57 (250 baris: 248 `pending`, 1 `error` baris #5, 1 `duplicate` baris #20) lewat skrip fixture
2. Buka Global Settings > Import, pilih Sub-Tab Brand
3. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
4. Klik `[Import (248)]`
5. Muat ulang halaman Import > Brand
6. Atur Rows per page 100
7. Buka menu `⋯` baris #40
8. Hover Remove
9. Verifikasi Remove baris #40 (`Brand Impor 040`) tetap tampil dan Disabled
10. Verifikasi tooltip pada Remove baris #40 "Can't do this while an import is in progress."
11. Tutup menu dengan menekan Esc
12. Hover checkbox baris #40
13. Verifikasi checkbox baris #40 tetap tampil dan Disabled
14. Verifikasi tooltip pada checkbox baris #40 "Can't do this while an import is in progress."
15. Buka halaman 3
16. Buka menu `⋯` baris #230
17. Hover Remove
18. Verifikasi Remove baris #230 (`Brand Impor 230`) tetap tampil dan Enabled
19. Verifikasi tidak ada tooltip pada Remove baris #230
20. Tutup menu dengan menekan Esc
21. Hover checkbox baris #230
22. Verifikasi checkbox baris #230 tetap tampil dan Enabled
23. Verifikasi tidak ada tooltip pada checkbox baris #230

### TC-GS-IMPORT-743: Keanggotaan batch pertama (error dan duplicate bukan anggota, pending ke-100 terkunci, ke-101 di luar batch)

24. Reset Client E (D-47) dan seed draft Brand D-57 lewat skrip fixture
25. Buka Global Settings > Import, pilih Sub-Tab Brand
26. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
27. Klik `[Import (248)]`
28. Muat ulang halaman Import > Brand
29. Atur Rows per page 100
30. Buka menu `⋯` baris #5 (`error`)
31. Hover Remove
32. Verifikasi Remove baris #5 (`error`) Enabled
33. Tutup menu dengan menekan Esc
34. Buka menu `⋯` baris #20 (`duplicate`)
35. Hover Remove
36. Verifikasi Remove baris #20 (`duplicate`) Enabled
37. Tutup menu dengan menekan Esc
38. Buka halaman 2
39. Buka menu `⋯` baris #102 (`Brand Impor 102`, baris `pending` ke-100)
40. Hover Remove
41. Verifikasi Remove baris #102 tetap tampil dan Disabled
42. Verifikasi tooltip pada Remove baris #102 "Can't do this while an import is in progress."
43. Tutup menu dengan menekan Esc
44. Buka menu `⋯` baris #103 (`Brand Impor 103`, baris `pending` ke-101)
45. Hover Remove
46. Verifikasi Remove baris #103 Enabled
47. Tutup menu dengan menekan Esc
48. Buka halaman 1
49. Buka menu `⋯` baris #5 (`error`)
50. Pilih Remove
51. Klik `[Delete]` pada dialog Delete Row
52. Verifikasi toast sukses "Success, row has been deleted."
53. Verifikasi kartu Total Rows menampilkan 249

### TC-GS-IMPORT-377: Remove baris di luar batch aktif diizinkan selama committing

54. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
55. Buka Global Settings > Import, pilih Sub-Tab Brand
56. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
57. Klik `[Import (250)]`
58. Muat ulang halaman Import > Brand
59. Atur Rows per page 100
60. Buka halaman 3
61. Buka menu `⋯` baris #230
62. Pilih Remove
63. Klik `[Delete]` pada dialog Delete Row
64. Verifikasi toast sukses "Success, row has been deleted."
65. Verifikasi baris `Brand Impor 230` tidak lagi tampil
66. Verifikasi kartu Total Rows menampilkan 249
67. Verifikasi kartu Ready to Import menampilkan 249

### TC-GS-IMPORT-744: Keanggotaan batch kedua (di dalam batch kedua Disabled, di luar Enabled)

68. Reset Client E (D-47) dan seed draft Brand D-57 lewat skrip fixture
69. Buka Global Settings > Import, pilih Sub-Tab Brand
70. Aktifkan kontrol worker commit mode 4 (dijeda di dalam batch kedua setelah batch pertama selesai)
71. Klik `[Import (248)]`
72. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
73. Verifikasi kartu Total Rows menampilkan 150
74. Atur Rows per page 100
75. Buka menu `⋯` baris `Brand Impor 150` (anggota batch kedua; Row #50, baris ke-50 dari atas pada halaman 1)
76. Hover Remove
77. Verifikasi Remove baris `Brand Impor 150` tetap tampil dan Disabled
78. Verifikasi tooltip pada Remove baris `Brand Impor 150` "Can't do this while an import is in progress."
79. Tutup menu dengan menekan Esc
80. Buka halaman 2
81. Buka menu `⋯` baris `Brand Impor 230` (di luar batch kedua; Row #130, baris ke-30 dari atas pada halaman 2)
82. Hover Remove
83. Verifikasi Remove baris `Brand Impor 230` Enabled

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah keanggotaan batch aktif pada job `committing` yang dibentuk kontrol worker D-47.
- Alasan melewati sekitar 35 langkah (83 langkah nominal): empat blok homogen (hover row action Remove dan checkbox pada job `committing`), semua satu kelas dan berdiri sendiri dengan reset Client E di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Urutan blok: TC-742 dan TC-743 (read-only sampai aksi Remove terakhir), lalu TC-377 (Remove sukses), lalu TC-744 (menunggu batch pertama selesai).
- Pembagian TC dalam blok: TC-GS-IMPORT-743 menghapus baris #5 di akhir (langkah 49 sampai 53, aksi yang menghapus data di akhir blok); asersi kartu Total Rows 249 mengikuti Expected e.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 24, 54, 68), aktivasi kontrol worker, pembukaan halaman dan Sub-Tab, pengaturan Rows per page, pindah halaman, hover, menutup menu `⋯` lewat Esc (langkah 11, 20, 33, 37, 43, 47, 79), dan polling job (langkah 72) yang menunggu job latar belakang dan bukan menunggu jam. Pada TC-377 langkah 60 sampai 63 memakai halaman 3 karena baris #230 berada di luar batch aktif.
- Langkah 19 dan 23 (tidak ada tooltip) adalah asersi absence atas elemen UI pada halaman yang sudah termuat; langkah 18 dan 22 (tombol atau checkbox Enabled) tampil lebih dulu sebagai anchor positif pada elemen yang sama.
- Temuan untuk QA:
  - TC-GS-IMPORT-377, 742, 743, 744 tidak merujuk kontrol worker D-47 pada kolom D-ref; TC-GS-IMPORT-744 tidak menyebut nomor mode D-47 yang dimaksud (spec memakai mode 4: dijeda di dalam batch kedua setelah batch pertama selesai).
  - TC-GS-IMPORT-744 Expected a menyebut kartu Total Rows 150 sesudah batch pertama selesai; angka ini bergantung pada seluruh 100 baris batch pertama terkomit dan pada urutan baris yang tersisa (baris `error`, baris `duplicate`, lalu `Brand Impor 103` sampai `250`) yang hanya tertulis di Data Uji TC.
  - TC-GS-IMPORT-744 menyebut `Brand Impor 150` sebagai Row #50 dan `Brand Impor 230` sebagai Row #130 setelah 100 baris batch pertama terhapus dari Staging Table; spec memakai penunjukan baris menurut nama.
  - Post Condition TC-GS-IMPORT-377 ("draft berisi 249 baris `pending`"), TC-GS-IMPORT-742, 743, 744 ("job committing dengan worker dijeda; draft tetap 250 baris atau 150 baris") tidak punya langkah observasi tersendiri selain Expected dan tidak diasersi tambahan (S-01).
  - TC-GS-IMPORT-743 mengasersi Remove baris `error` dan `duplicate` Enabled (Expected a dan b) tanpa tooltip; spec mengikuti Expected dan tidak menambah asersi absence tooltip pada baris itu.
