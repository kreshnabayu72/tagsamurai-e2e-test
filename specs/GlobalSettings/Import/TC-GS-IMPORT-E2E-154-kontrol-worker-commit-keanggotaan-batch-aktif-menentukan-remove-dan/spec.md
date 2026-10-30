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
2. Muat ulang halaman Import > Brand
3. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
4. Klik `[Import (248)]`
5. Tunggu aksi selesai (permintaan mendapat respons)
6. Muat ulang halaman Import > Brand
7. Atur Rows per page 100
8. Buka menu `⋯` baris #40
9. Hover Remove
10. Verifikasi Remove baris #40 (`Brand Impor 040`) tetap tampil dan Disabled
11. Verifikasi tooltip pada Remove baris #40 "Can't do this while an import is in progress."
12. Tutup menu dengan menekan Esc
13. Hover checkbox baris #40
14. Verifikasi checkbox baris #40 tetap tampil dan Disabled
15. Verifikasi tooltip pada checkbox baris #40 "Can't do this while an import is in progress."
16. Buka halaman 3
17. Buka menu `⋯` baris #230
18. Hover Remove
19. Verifikasi Remove baris #230 (`Brand Impor 230`) tetap tampil dan Enabled
20. Verifikasi tidak ada tooltip pada Remove baris #230
21. Tutup menu dengan menekan Esc
22. Hover checkbox baris #230
23. Verifikasi checkbox baris #230 tetap tampil dan Enabled
24. Verifikasi tidak ada tooltip pada checkbox baris #230

### TC-GS-IMPORT-743: Keanggotaan batch pertama (error dan duplicate bukan anggota, pending ke-100 terkunci, ke-101 di luar batch)

25. Reset Client E (D-47) dan seed draft Brand D-57 lewat skrip fixture
26. Muat ulang halaman Import > Brand
27. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
28. Klik `[Import (248)]`
29. Tunggu aksi selesai (permintaan mendapat respons)
30. Muat ulang halaman Import > Brand
31. Atur Rows per page 100
32. Buka menu `⋯` baris #5 (`error`)
33. Hover Remove
34. Verifikasi Remove baris #5 (`error`) Enabled
35. Tutup menu dengan menekan Esc
36. Buka menu `⋯` baris #20 (`duplicate`)
37. Hover Remove
38. Verifikasi Remove baris #20 (`duplicate`) Enabled
39. Tutup menu dengan menekan Esc
40. Buka halaman 2
41. Buka menu `⋯` baris #102 (`Brand Impor 102`, baris `pending` ke-100)
42. Hover Remove
43. Verifikasi Remove baris #102 tetap tampil dan Disabled
44. Verifikasi tooltip pada Remove baris #102 "Can't do this while an import is in progress."
45. Tutup menu dengan menekan Esc
46. Buka menu `⋯` baris #103 (`Brand Impor 103`, baris `pending` ke-101)
47. Hover Remove
48. Verifikasi Remove baris #103 Enabled
49. Tutup menu dengan menekan Esc
50. Buka halaman 1
51. Buka menu `⋯` baris #5 (`error`)
52. Pilih Remove
53. Klik `[Delete]` pada dialog Delete Row
54. Verifikasi toast sukses "Success, row has been deleted."
55. Verifikasi kartu Total Rows menampilkan 249

### TC-GS-IMPORT-377: Remove baris di luar batch aktif diizinkan selama committing

56. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
57. Muat ulang halaman Import > Brand
58. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
59. Klik `[Import (250)]`
60. Tunggu aksi selesai (permintaan mendapat respons)
61. Muat ulang halaman Import > Brand
62. Atur Rows per page 100
63. Buka halaman 3
64. Buka menu `⋯` baris #230
65. Pilih Remove
66. Klik `[Delete]` pada dialog Delete Row
67. Verifikasi toast sukses "Success, row has been deleted."
68. Verifikasi baris `Brand Impor 230` tidak lagi tampil
69. Verifikasi kartu Total Rows menampilkan 249
70. Verifikasi kartu Ready to Import menampilkan 249

### TC-GS-IMPORT-744: Keanggotaan batch kedua (di dalam batch kedua Disabled, di luar Enabled)

71. Reset Client E (D-47) dan seed draft Brand D-57 lewat skrip fixture
72. Muat ulang halaman Import > Brand
73. Aktifkan kontrol worker commit mode 4 (dijeda di dalam batch kedua setelah batch pertama selesai)
74. Klik `[Import (248)]`
75. Tunggu aksi selesai (permintaan mendapat respons)
76. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
77. Verifikasi kartu Total Rows menampilkan 150
78. Atur Rows per page 100
79. Buka menu `⋯` baris `Brand Impor 150` (anggota batch kedua; Row #50, baris ke-50 dari atas pada halaman 1)
80. Hover Remove
81. Verifikasi Remove baris `Brand Impor 150` tetap tampil dan Disabled
82. Verifikasi tooltip pada Remove baris `Brand Impor 150` "Can't do this while an import is in progress."
83. Tutup menu dengan menekan Esc
84. Buka halaman 2
85. Buka menu `⋯` baris `Brand Impor 230` (di luar batch kedua; Row #130, baris ke-30 dari atas pada halaman 2)
86. Hover Remove
87. Verifikasi Remove baris `Brand Impor 230` Enabled

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah keanggotaan batch aktif pada job `committing` yang dibentuk kontrol worker D-47.
- Alasan melewati sekitar 35 langkah (87 langkah nominal): empat blok homogen (hover row action Remove dan checkbox pada job `committing`), semua satu kelas dan berdiri sendiri dengan reset Client E di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Urutan blok: TC-742 dan TC-743 (read-only sampai aksi Remove terakhir), lalu TC-377 (Remove sukses), lalu TC-744 (menunggu batch pertama selesai).
- Penanda selesai untuk langkah 5, 29, 60, dan 75 tidak disebut di TC atau PRD; "permintaan mendapat respons" dipakai sampai QA menetapkan penanda yang teramati.
- Pembagian TC dalam blok: TC-GS-IMPORT-743 menghapus baris #5 di akhir (langkah 51 sampai 55, aksi yang menghapus data di akhir blok); asersi kartu Total Rows 249 mengikuti Expected e.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 25, 56, 71), "Muat ulang halaman Import > Brand" sesudah reset (langkah 2, 26, 57, 72; reset membuang atau mengganti draft sementara halaman Import dari blok atau hook sebelumnya masih terbuka, `suite.md`), aktivasi kontrol worker, pengaturan Rows per page, pindah halaman, hover, menutup menu `⋯` lewat Esc (langkah 12, 21, 35, 39, 45, 49, 83), langkah 5, 29, 60, dan 75 (Tunggu aksi selesai: permintaan mendapat respons, memisahkan klik `[Import (N)]` dari muat ulang), dan polling job (langkah 76) yang menunggu job latar belakang dan bukan menunggu jam. Pada TC-377 langkah 62 sampai 65 memakai halaman 3 karena baris #230 berada di luar batch aktif.
- Langkah 20 dan 24 (tidak ada tooltip) adalah asersi absence atas elemen UI pada halaman yang sudah termuat; langkah 19 dan 23 (tombol atau checkbox Enabled) tampil lebih dulu sebagai anchor positif pada elemen yang sama.
- Temuan untuk QA:
  - TC-GS-IMPORT-377, 742, 743, 744 tidak merujuk kontrol worker D-47 pada kolom D-ref; TC-GS-IMPORT-744 tidak menyebut nomor mode D-47 yang dimaksud (spec memakai mode 4: dijeda di dalam batch kedua setelah batch pertama selesai).
  - TC-GS-IMPORT-744 Expected a menyebut kartu Total Rows 150 sesudah batch pertama selesai; angka ini bergantung pada seluruh 100 baris batch pertama terkomit dan pada urutan baris yang tersisa (baris `error`, baris `duplicate`, lalu `Brand Impor 103` sampai `250`) yang hanya tertulis di Data Uji TC.
  - TC-GS-IMPORT-744 menyebut `Brand Impor 150` sebagai Row #50 dan `Brand Impor 230` sebagai Row #130 setelah 100 baris batch pertama terhapus dari Staging Table; spec memakai penunjukan baris menurut nama.
  - Post Condition TC-GS-IMPORT-377 ("draft berisi 249 baris `pending`"), TC-GS-IMPORT-742, 743, 744 ("job committing dengan worker dijeda; draft tetap 250 baris atau 150 baris") tidak punya langkah observasi tersendiri selain Expected dan tidak diasersi tambahan (S-01).
  - TC-GS-IMPORT-743 mengasersi Remove baris `error` dan `duplicate` Enabled (Expected a dan b) tanpa tooltip; spec mengikuti Expected dan tidak menambah asersi absence tooltip pada baris itu.
