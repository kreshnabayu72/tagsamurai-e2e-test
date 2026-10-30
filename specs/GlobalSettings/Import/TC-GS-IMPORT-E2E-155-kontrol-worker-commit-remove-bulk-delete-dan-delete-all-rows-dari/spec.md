---
id: TC-GS-IMPORT-E2E-155-kontrol-worker-commit-remove-bulk-delete-dan-delete-all-rows-dari
title: "Kontrol worker commit: Remove, Bulk Delete, dan Delete All Rows dari halaman basi (partial di luar batch, ditolak di dalam batch)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-376
  - TC-GS-IMPORT-378
  - TC-GS-IMPORT-379
  - TC-GS-IMPORT-380
  - TC-GS-IMPORT-748
coverage:
  web: automated
---

# Kontrol worker commit: Remove, Bulk Delete, dan Delete All Rows dari halaman basi (partial di luar batch, ditolak di dalam batch)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (kontrol worker commit) dan master data Pre-setup Client E (Division `Gudang`, Position `Technician`) dan memakai Client E yang dipakai bersama spec commit lain; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Pelaku kedua (pemicu): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC2_PASSWORD`, memakai sesi API untuk permintaan Import fixture, hapus Division, dan ubah nama Position; tidak ada sesi UI kedua karena hasil di sesi itu tidak diasersi (P-2).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; TC-376, 378, 379, 380, 748 tidak merujuk D-47 pada kolom D-ref tetapi membutuhkannya):
  - Kontrol worker commit D-47 mode 2 (dijeda di dalam batch pertama sesudah uji ulang late-binding dan sebelum batch selesai).
  - Sesi API Admin kedua Client E: permintaan Import (memulai commit), hapus Division `Gudang`, ubah nama Position `Technician` menjadi `Technician Lead` (mekanisme lewat fixture).
  - Skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, kembalikan Division `Gudang` dan Position `Technician`, hapus hasil commit) dan seeding draft.
- Data Pre-setup Client E yang diubah TC-380 dan TC-748: Division `Gudang` dihapus dan Position `Technician` diubah namanya menjadi `Technician Lead` oleh pemicu; keduanya tidak dipakai user lain. Reset di awal blok (langkah 1, 17, 31, 46, 66) dan hook `after` memulihkan Division `Gudang` dan Position `Technician` ke kondisi Pre-setup.
- Data Dinamis (milik spec ini; draft dibuang oleh reset dan nama baris berkas literal sesuai Data Uji TC):
  - D-56 `brand-250-impor.csv`: `Brand Impor 001` sampai `Brand Impor 250`, semua valid dan unik.
  - D-57 `brand-250-mixed.csv`: 248 `pending`, baris #5 `error` (Brand Name 121 karakter nilai sumber Brand pertama tabel D-41), baris #20 `duplicate` (`Samsung`); batch pertama = baris #1-#4, #6-#19, #21-#102.
  - `user-login-130.csv`: 130 baris `Pengguna` / `Uji nnn` / `pengguna.ujinnn@example.com` / Access `Global Settings`; Division `Engineering` kecuali baris #1-#3 `Gudang` dan baris #101-#103 `Logistik` (tidak ada di sistem, `error`); Position `Technician` pada baris #4-#6; baris #1-#100 `pending` (batch pertama), baris #101-#103 `error`, baris #104-#130 `pending`.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, hapus draft Client E, pulihkan Division `Gudang` dan Position `Technician`, hapus hasil commit bila ada, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-376: Remove di dalam batch aktif dari halaman basi

1. Reset Client E (D-47) dan seed draft Brand D-57 (250 baris: 248 `pending`, 1 `error` baris #5, 1 `duplicate` baris #20) lewat skrip fixture
2. Muat ulang halaman Import > Brand
3. Verifikasi footer `[Import (248)]` Enabled
4. Atur Rows per page 100
5. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
6. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
7. Tunggu aksi selesai (permintaan mendapat respons)
8. Pada halaman langkah 2 (tanpa muat ulang) buka menu `⋯` baris #40
9. Pilih Remove
10. Klik `[Delete]` pada dialog Delete Row
11. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
12. Klik `[OK]`
13. Verifikasi dialog menutup
14. Muat ulang halaman Import > Brand
15. Verifikasi kartu Total Rows tetap 250
16. Verifikasi baris #40 (`Brand Impor 040`) masih tampil

### TC-GS-IMPORT-379: Bulk Delete dari halaman basi yang seluruh barisnya di dalam batch aktif

17. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
18. Muat ulang halaman Import > Brand
19. Verifikasi footer `[Import (250)]` Enabled
20. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
21. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
22. Tunggu aksi selesai (permintaan mendapat respons)
23. Pada halaman langkah 18 (tanpa muat ulang) centang baris #1 dan #2
24. Klik Bulk Action > Delete
25. Klik `[Delete]` pada dialog Delete Rows
26. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
27. Klik `[OK]`
28. Muat ulang halaman Import > Brand
29. Verifikasi kartu Total Rows tetap 250
30. Verifikasi baris #1 (`Brand Impor 001`) dan #2 (`Brand Impor 002`) masih tampil

### TC-GS-IMPORT-748: Delete All Rows pada kategori yang seluruh barisnya di dalam batch aktif

31. Reset Client E (D-47) dan seed draft User Login `user-login-130.csv` (127 `pending`, 3 `error` baris #101-#103) lewat skrip fixture
32. Buka Global Settings > Import, pilih Sub-Tab User Login
33. Hapus Division `Gudang` atas nama Admin kedua Client E lewat fixture
34. Ubah nama Position `Technician` menjadi `Technician Lead` atas nama Admin kedua Client E lewat fixture
35. Tunggu aksi selesai (permintaan mendapat respons)
36. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
37. Klik `[Import (127)]`
38. Tunggu aksi selesai (permintaan mendapat respons)
39. Muat ulang halaman Import > User Login
40. Klik `[Delete All Rows]` pada baris pesan Error Summary Callout "Position not found"
41. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
42. Klik `[OK]`
43. Muat ulang halaman Import > User Login
44. Verifikasi Error Summary Callout masih memuat "Position not found" dengan badge "3 rows"
45. Verifikasi baris #4 sampai #6 masih tampil berstatus `error`

### TC-GS-IMPORT-378: Bulk Delete dari halaman basi (di luar batch dihapus, di dalam batch dilewati)

46. Reset Client E (D-47), pulihkan Division `Gudang` dan Position `Technician`, dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
47. Buka Global Settings > Import, pilih Sub-Tab Brand
48. Verifikasi footer `[Import (250)]` Enabled
49. Atur Rows per page 100
50. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
51. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
52. Tunggu aksi selesai (permintaan mendapat respons)
53. Pada halaman langkah 47 (tanpa muat ulang) centang baris #40
54. Buka halaman 3
55. Centang baris #230
56. Klik Bulk Action > Delete
57. Klik `[Delete]` pada dialog Delete Rows
58. Verifikasi toast sukses "Success, row has been deleted. Some items were skipped."
59. Muat ulang halaman Import > Brand
60. Atur Rows per page 100 dan buka halaman 3
61. Verifikasi kartu Total Rows menampilkan 249
62. Verifikasi sedikitnya satu baris tampil pada halaman 3
63. Verifikasi baris `Brand Impor 230` tidak tampil pada halaman 3
64. Buka halaman 1
65. Verifikasi baris #40 (`Brand Impor 040`) tampil

### TC-GS-IMPORT-380: Delete All Rows saat committing (di luar batch dihapus, di dalam batch dilewati)

66. Reset Client E (D-47), pulihkan Division `Gudang` dan Position `Technician`, dan seed draft User Login `user-login-130.csv` (127 `pending`, 3 `error` baris #101-#103) lewat skrip fixture
67. Buka Global Settings > Import, pilih Sub-Tab User Login
68. Hapus Division `Gudang` atas nama Admin kedua Client E lewat fixture
69. Ubah nama Position `Technician` menjadi `Technician Lead` atas nama Admin kedua Client E lewat fixture
70. Tunggu aksi selesai (permintaan mendapat respons)
71. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
72. Klik `[Import (127)]`
73. Tunggu aksi selesai (permintaan mendapat respons)
74. Muat ulang halaman Import > User Login
75. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "6 rows"
76. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "3 rows"
77. Klik `[Delete All Rows]` pada baris pesan Error Summary Callout "Division not found"
78. Verifikasi toast sukses "Success, row has been deleted. Some items were skipped."
79. Muat ulang halaman Import > User Login
80. Verifikasi kartu Total Rows menampilkan 127
81. Verifikasi kartu Errors menampilkan 6
82. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "3 rows"
83. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "3 rows"
84. Klik `[View Data]` pada baris pesan Error Summary Callout "Division not found"
85. Verifikasi chip "Showing rows with: Division not found" tampil
86. Verifikasi Staging Table menampilkan 3 baris berstatus `error`
87. Verifikasi ketiga baris itu memiliki Last Name `Uji 001`, `Uji 002`, `Uji 003` dengan Division `Gudang`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah penolakan atau partial pada aksi hapus dari halaman basi saat job `committing`. Pelaku kedua hanya memicu perubahan state lewat sesi API (P-2); kontrol worker D-47 adalah pemicu.
- Alasan melewati sekitar 35 langkah (87 langkah nominal): lima blok homogen (aksi hapus dari halaman yang tidak dimuat ulang pada job `committing`), semua satu kelas dan berdiri sendiri dengan reset Client E di awal tiap blok. Blok yang menolak aksi (TC-376, 379, 748) mendahului blok yang menghapus (TC-378, 380), sesuai prinsip aksi yang menghapus data diletakkan di akhir.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok mengikuti kebutuhan state, bukan nomor TC.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 17, 31, 46, 66), "Muat ulang halaman Import > Brand" sesudah reset (langkah 2 dan 18; reset membuang atau mengganti draft sementara halaman Import dari blok atau hook sebelumnya masih terbuka, `suite.md`), aktivasi kontrol worker, pembukaan halaman dan Sub-Tab, pengaturan Rows per page, pindah halaman, pemicu Admin kedua (langkah 6, 21, 33, 34, 51, 68, 69), dan langkah 60 yang mengatur ulang Rows per page 100 dan membuka halaman 3 sesudah muat ulang (TC tidak menyebut apakah ukuran halaman bertahan setelah muat ulang; lihat Temuan untuk QA). Langkah 7, 22, 35, 52, dan 70 (Tunggu aksi selesai: permintaan mendapat respons) mengikuti pemicu sesi API Admin kedua dan mendahului aksi UI atau aktivasi kontrol worker berikutnya; langkah 38 dan 73 (Tunggu aksi selesai: permintaan mendapat respons) memisahkan klik `[Import (127)]` dari muat ulang halaman (bagian 8b butir 8, K-16, D-1).
- Langkah 3, 19, dan 48 adalah `Verifikasi` tambahan di luar Expected TC yang membuktikan prasyarat TC (halaman terbuka dengan `[Import (N)]` Enabled sebelum commit dimulai Admin kedua). Langkah 62 adalah anchor positif sebelum asersi absence `Brand Impor 230` pada langkah 63 (butir 2 bagian 8b).
- Temuan untuk QA:
  - TC-GS-IMPORT-380 dan TC-GS-IMPORT-748 mengubah data Pre-setup bersama Client E (menghapus Division `Gudang` dan mengubah nama Position `Technician`); spec mengikuti Langkah TC dan memulihkannya lewat reset dan hook `after` (S-06), dan karena itu suite berjalan serial.
  - TC-GS-IMPORT-378 Expected b/c dan TC-GS-IMPORT-380 tidak menyebut apakah Rows per page 100 bertahan setelah muat ulang; spec mengatur ulang ukuran halaman setelah muat ulang pada TC-378 (langkah 60).
  - TC-GS-IMPORT-376, 378, 379, 380, 748 tidak merujuk D-47 pada kolom D-ref (lihat Prerequisites).
  - TC-GS-IMPORT-380 Langkah 1 dan 2 menyebut Admin kedua mengubah master data "lewat fixture" tanpa menyebut mekanismenya; disediakan tim FE/BE.
  - TC-GS-IMPORT-380 Expected d menyebut "3 baris berstatus `error` dengan Last Name `Uji 001`, `Uji 002`, `Uji 003` (Division `Gudang`)" setelah `[Delete All Rows]` pada kategori "Division not found"; baris `Gudang` yang berada di dalam batch aktif (baris #1-#3) tetap tampil; ini konsisten dengan toast "Some items were skipped".
  - Post Condition TC-GS-IMPORT-376, 379, 748 ("job committing dengan worker dijeda; draft tetap 250 atau 130 baris"), TC-GS-IMPORT-378 ("draft berisi 249 baris `pending`"), dan TC-GS-IMPORT-380 ("draft berisi 127 baris (6 `error`)") dikonfirmasi oleh Expected tiap TC dan tidak diasersi tambahan (S-01).
  - Penanda selesai untuk pemicu sesi API atau fixture tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di surface aktor UI.
