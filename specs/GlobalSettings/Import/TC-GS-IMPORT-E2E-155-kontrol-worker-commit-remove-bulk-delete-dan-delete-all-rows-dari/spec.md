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
- Data Pre-setup Client E yang diubah TC-380 dan TC-748: Division `Gudang` dihapus dan Position `Technician` diubah namanya menjadi `Technician Lead` oleh pemicu; keduanya tidak dipakai user lain. Reset di awal blok (langkah 1, 15, 28, 42, 57) dan hook `after` memulihkan Division `Gudang` dan Position `Technician` ke kondisi Pre-setup.
- Data Dinamis (milik spec ini; draft dibuang oleh reset dan nama baris berkas literal sesuai Data Uji TC):
  - D-56 `brand-250-impor.csv`: `Brand Impor 001` sampai `Brand Impor 250`, semua valid dan unik.
  - D-57 `brand-250-mixed.csv`: 248 `pending`, baris #5 `error` (Brand Name 121 karakter nilai sumber Brand pertama tabel D-41), baris #20 `duplicate` (`Samsung`); batch pertama = baris #1-#4, #6-#19, #21-#102.
  - `user-login-130.csv`: 130 baris `Pengguna` / `Uji nnn` / `pengguna.ujinnn@example.com` / Access `Global Settings`; Division `Engineering` kecuali baris #1-#3 `Gudang` dan baris #101-#103 `Logistik` (tidak ada di sistem, `error`); Position `Technician` pada baris #4-#6; baris #1-#100 `pending` (batch pertama), baris #101-#103 `error`, baris #104-#130 `pending`.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, hapus draft Client E, pulihkan Division `Gudang` dan Position `Technician`, hapus hasil commit bila ada, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-376: Remove di dalam batch aktif dari halaman basi

1. Reset Client E (D-47) dan seed draft Brand D-57 (250 baris: 248 `pending`, 1 `error` baris #5, 1 `duplicate` baris #20) lewat skrip fixture
2. Buka Global Settings > Import, pilih Sub-Tab Brand
3. Verifikasi footer `[Import (248)]` Enabled
4. Atur Rows per page 100
5. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
6. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
7. Pada halaman langkah 2 (tanpa muat ulang) buka menu `⋯` baris #40
8. Pilih Remove
9. Klik `[Delete]` pada dialog Delete Row
10. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
11. Klik `[OK]`
12. Verifikasi dialog menutup
13. Muat ulang halaman Import > Brand
14. Verifikasi kartu Total Rows tetap 250
15. Verifikasi baris #40 (`Brand Impor 040`) masih tampil

### TC-GS-IMPORT-379: Bulk Delete dari halaman basi yang seluruh barisnya di dalam batch aktif

16. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
17. Buka Global Settings > Import, pilih Sub-Tab Brand
18. Verifikasi footer `[Import (250)]` Enabled
19. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
20. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
21. Pada halaman langkah 17 (tanpa muat ulang) centang baris #1 dan #2
22. Klik Bulk Action > Delete
23. Klik `[Delete]` pada dialog Delete Rows
24. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
25. Klik `[OK]`
26. Muat ulang halaman Import > Brand
27. Verifikasi kartu Total Rows tetap 250
28. Verifikasi baris #1 (`Brand Impor 001`) dan #2 (`Brand Impor 002`) masih tampil

### TC-GS-IMPORT-748: Delete All Rows pada kategori yang seluruh barisnya di dalam batch aktif

29. Reset Client E (D-47) dan seed draft User Login `user-login-130.csv` (127 `pending`, 3 `error` baris #101-#103) lewat skrip fixture
30. Buka Global Settings > Import, pilih Sub-Tab User Login
31. Hapus Division `Gudang` atas nama Admin kedua Client E lewat fixture
32. Ubah nama Position `Technician` menjadi `Technician Lead` atas nama Admin kedua Client E lewat fixture
33. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
34. Klik `[Import (127)]`
35. Muat ulang halaman Import > User Login
36. Klik `[Delete All Rows]` pada baris pesan Error Summary Callout "Position not found"
37. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
38. Klik `[OK]`
39. Muat ulang halaman Import > User Login
40. Verifikasi Error Summary Callout masih memuat "Position not found" dengan badge "3 rows"
41. Verifikasi baris #4 sampai #6 masih tampil berstatus `error`

### TC-GS-IMPORT-378: Bulk Delete dari halaman basi (di luar batch dihapus, di dalam batch dilewati)

42. Reset Client E (D-47), pulihkan Division `Gudang` dan Position `Technician`, dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
43. Buka Global Settings > Import, pilih Sub-Tab Brand
44. Verifikasi footer `[Import (250)]` Enabled
45. Atur Rows per page 100
46. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
47. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
48. Pada halaman langkah 43 (tanpa muat ulang) centang baris #40
49. Buka halaman 3
50. Centang baris #230
51. Klik Bulk Action > Delete
52. Klik `[Delete]` pada dialog Delete Rows
53. Verifikasi toast sukses "Success, row has been deleted. Some items were skipped."
54. Muat ulang halaman Import > Brand
55. Atur Rows per page 100 dan buka halaman 3
56. Verifikasi kartu Total Rows menampilkan 249
57. Verifikasi sedikitnya satu baris tampil pada halaman 3
58. Verifikasi baris `Brand Impor 230` tidak tampil pada halaman 3
59. Buka halaman 1
60. Verifikasi baris #40 (`Brand Impor 040`) tampil

### TC-GS-IMPORT-380: Delete All Rows saat committing (di luar batch dihapus, di dalam batch dilewati)

61. Reset Client E (D-47), pulihkan Division `Gudang` dan Position `Technician`, dan seed draft User Login `user-login-130.csv` (127 `pending`, 3 `error` baris #101-#103) lewat skrip fixture
62. Buka Global Settings > Import, pilih Sub-Tab User Login
63. Hapus Division `Gudang` atas nama Admin kedua Client E lewat fixture
64. Ubah nama Position `Technician` menjadi `Technician Lead` atas nama Admin kedua Client E lewat fixture
65. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
66. Klik `[Import (127)]`
67. Muat ulang halaman Import > User Login
68. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "6 rows"
69. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "3 rows"
70. Klik `[Delete All Rows]` pada baris pesan Error Summary Callout "Division not found"
71. Verifikasi toast sukses "Success, row has been deleted. Some items were skipped."
72. Muat ulang halaman Import > User Login
73. Verifikasi kartu Total Rows menampilkan 127
74. Verifikasi kartu Errors menampilkan 6
75. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "3 rows"
76. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "3 rows"
77. Klik `[View Data]` pada baris pesan Error Summary Callout "Division not found"
78. Verifikasi chip "Showing rows with: Division not found" tampil
79. Verifikasi Staging Table menampilkan 3 baris berstatus `error`
80. Verifikasi ketiga baris itu memiliki Last Name `Uji 001`, `Uji 002`, `Uji 003` dengan Division `Gudang`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah penolakan atau partial pada aksi hapus dari halaman basi saat job `committing`. Pelaku kedua hanya memicu perubahan state lewat sesi API (P-2); kontrol worker D-47 adalah pemicu.
- Alasan melewati sekitar 35 langkah (80 langkah nominal): lima blok homogen (aksi hapus dari halaman yang tidak dimuat ulang pada job `committing`), semua satu kelas dan berdiri sendiri dengan reset Client E di awal tiap blok. Blok yang menolak aksi (TC-376, 379, 748) mendahului blok yang menghapus (TC-378, 380), sesuai prinsip aksi yang menghapus data diletakkan di akhir.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok mengikuti kebutuhan state, bukan nomor TC.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 16, 29, 42, 61), aktivasi kontrol worker, pembukaan halaman dan Sub-Tab, pengaturan Rows per page, pindah halaman, pemicu Admin kedua (langkah 6, 20, 31, 32, 47, 63, 64), dan langkah 55 yang mengatur ulang Rows per page 100 dan membuka halaman 3 sesudah muat ulang (TC tidak menyebut apakah ukuran halaman bertahan setelah muat ulang; lihat Temuan untuk QA).
- Langkah 3, 18, dan 44 adalah `Verifikasi` tambahan di luar Expected TC yang membuktikan prasyarat TC (halaman terbuka dengan `[Import (N)]` Enabled sebelum commit dimulai Admin kedua). Langkah 57 adalah anchor positif sebelum asersi absence `Brand Impor 230` pada langkah 58 (butir 2 bagian 8b).
- Temuan untuk QA:
  - TC-GS-IMPORT-380 dan TC-GS-IMPORT-748 mengubah data Pre-setup bersama Client E (menghapus Division `Gudang` dan mengubah nama Position `Technician`); spec mengikuti Langkah TC dan memulihkannya lewat reset dan hook `after` (S-06), dan karena itu suite berjalan serial.
  - TC-GS-IMPORT-378 Expected b/c dan TC-GS-IMPORT-380 tidak menyebut apakah Rows per page 100 bertahan setelah muat ulang; spec mengatur ulang ukuran halaman setelah muat ulang pada TC-378 (langkah 55).
  - TC-GS-IMPORT-376, 378, 379, 380, 748 tidak merujuk D-47 pada kolom D-ref (lihat Prerequisites).
  - TC-GS-IMPORT-380 Langkah 1 dan 2 menyebut Admin kedua mengubah master data "lewat fixture" tanpa menyebut mekanismenya; disediakan tim FE/BE.
  - TC-GS-IMPORT-380 Expected d menyebut "3 baris berstatus `error` dengan Last Name `Uji 001`, `Uji 002`, `Uji 003` (Division `Gudang`)" setelah `[Delete All Rows]` pada kategori "Division not found"; baris `Gudang` yang berada di dalam batch aktif (baris #1-#3) tetap tampil; ini konsisten dengan toast "Some items were skipped".
  - Post Condition TC-GS-IMPORT-376, 379, 748 ("job committing dengan worker dijeda; draft tetap 250 atau 130 baris"), TC-GS-IMPORT-378 ("draft berisi 249 baris `pending`"), dan TC-GS-IMPORT-380 ("draft berisi 127 baris (6 `error`)") dikonfirmasi oleh Expected tiap TC dan tidak diasersi tambahan (S-01).
