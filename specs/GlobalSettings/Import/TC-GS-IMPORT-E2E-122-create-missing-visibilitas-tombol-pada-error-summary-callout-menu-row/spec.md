---
id: TC-GS-IMPORT-E2E-122-create-missing-visibilitas-tombol-pada-error-summary-callout-menu-row
title: "Create Missing: visibilitas tombol pada Error Summary Callout, menu row action, dan Bulk Action Bar (Divisions, Positions, Options)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-344
  - TC-GS-IMPORT-349
  - TC-GS-IMPORT-733
  - TC-GS-IMPORT-734
  - TC-GS-IMPORT-924
  - TC-GS-IMPORT-925
coverage:
  web: automated
---

# Create Missing: visibilitas tombol pada Error Summary Callout, menu row action, dan Bulk Action Bar (Divisions, Positions, Options)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
- Pelaku kedua (TC-GS-IMPORT-925): Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net` hanya lewat sesi API untuk menonaktifkan lalu mengaktifkan kembali Custom Field `Shift` (P-2), password `Spectra.env.GS_CLIENTC_TC2_PASSWORD` (disediakan tim FE).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import; sub-tab dipilih di `## Test Steps`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Pre-setup Client C (tidak diubah spec ini kecuali status Custom Field `Shift` pada TC-GS-IMPORT-925 yang dipulihkan): Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang` (`Logistik` belum ada); Custom Field `Shift` (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam` (`Lembur` dan `Piket` belum menjadi opsi). Client C tanpa draft di semua Tab sebelum tiap TC (fixture reset, Kontrak Fixture R1).
- Data Dinamis (berkas disediakan tim QA, fixture baru `Fixture.import.berkas`): `ai-brand-long.csv` (D-44; Brand Name nilai sumber D-41, 121 karakter); `user-login-first-long-logistik.csv` (berkas User Login standar D-45, 2 baris: #1 First Name nilai sumber D-41 121 karakter, Last Name `Rahmawati`, Division `Engineering`; #2 Budi Santoso, Division `Logistik`; Position kosong); `user-login-logistik-4.csv` (D-45, 4 baris Siti Rahmawati, Budi Santoso, Andi Pratama, Rina Wijaya, Division `Logistik`, Position kosong); D-87 `user-login-shift-mixed.csv` (3 baris, semua `error`); D-79 `user-login-shift-lembur.csv` (baris #1 dan #2 `error`, baris #3 `pending`). Nama `Logistik` literal sesuai TC (tidak dibuat spec ini; hanya muncul sebagai nilai tidak ditemukan).
- Kemampuan teknis: mock layanan AI mode normal (D-40, D-41, D-42); fixture reset draft client; sesi API Admin kedua untuk menonaktifkan dan mengaktifkan Custom Field; Banner Custom Field Deactivated dan pemulihan Custom Field `Shift` oleh fixture.
- State global yang diubah: status Custom Field `Shift` Client C (dinonaktifkan lalu diaktifkan kembali pada TC-GS-IMPORT-925, dipulihkan di hook `after`). Suite berjalan serial (`parallel: false`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset draft semua Tab Client C, aktifkan kembali Custom Field `Shift` bila Inactive.

## Test Steps

### TC-GS-IMPORT-733: Error Summary Callout Tab Brand tidak memiliki tombol Create Missing

1. Pilih sub-tab Brand
2. Klik [Upload File] di Dropzone dan pilih berkas `ai-brand-long.csv`
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Verifikasi Error Summary Callout memuat baris pesan "Brand Name: Max. 120 characters" dengan badge "1 row"
5. Verifikasi baris pesan "Brand Name: Max. 120 characters" memuat `[View Data]` dan `[Delete All Rows]`
6. Verifikasi baris pesan "Brand Name: Max. 120 characters" tidak memuat `[Create Missing Divisions]` maupun `[Create Missing Positions]`
7. Reset draft Brand Client C lewat fixture reset

### TC-GS-IMPORT-349: Create Missing hanya tampil pada baris pesan Division atau Position tidak ditemukan di Tab User Login

8. Pilih sub-tab User Login
9. Klik [Upload File] di Dropzone dan pilih berkas `user-login-first-long-logistik.csv`
10. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
11. Verifikasi baris pesan "First Name: Max. 120 characters" pada Error Summary Callout dengan badge "1 row"
12. Verifikasi baris pesan "First Name: Max. 120 characters" memuat `[View Data]` dan `[Delete All Rows]`
13. Verifikasi baris pesan "First Name: Max. 120 characters" tidak memuat `[Create Missing Divisions]` maupun `[Create Missing Positions]`
14. Verifikasi baris pesan "Division not found" pada Error Summary Callout dengan badge "1 row"
15. Verifikasi baris pesan "Division not found" memuat `[View Data]`, `[Delete All Rows]`, dan `[Create Missing Divisions]`

### TC-GS-IMPORT-734: Menu row action memuat Create Missing hanya pada baris error Division atau Position tidak ditemukan

Draft pada langkah 9-10 dipakai ulang karena TC-GS-IMPORT-349 dan 734 memakai berkas dan precondition yang sama dan tidak ada mutasi di antaranya.

16. Klik `⋯` pada baris #1
17. Verifikasi menu `⋯` baris #1 (error First Name) memuat `Duplicate`, `Edit`, dan `Remove`
18. Verifikasi menu `⋯` baris #1 tidak memuat `[Create Missing Divisions]` maupun `[Create Missing Positions]`
19. Tutup menu `⋯`
20. Klik `⋯` pada baris #2
21. Verifikasi menu `⋯` baris #2 (Division tidak ditemukan) memuat `Duplicate`, `Edit`, `[Create Missing Divisions]`, dan `Remove` dalam urutan tersebut
22. Tutup menu `⋯`, lalu reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-344: Create Missing tidak tersedia di Bulk Action Bar

23. Muat ulang halaman Import > User Login
24. Klik [Upload File] di Dropzone dan pilih berkas `user-login-logistik-4.csv`
25. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
26. Centang kotak pada baris #1
27. Verifikasi Bulk Action Bar menampilkan "1 Row selected"
28. Klik `[Bulk Action ▾]`
29. Verifikasi overlay hanya berisi `[Delete]`
30. Verifikasi overlay tidak memuat `[Create Missing Divisions]` maupun `[Create Missing Positions]`
31. Tutup overlay, hapus centang baris #1, lalu reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-924: Create Missing Options hanya pada baris pesan dan baris error Dropdown tidak ditemukan, berdampingan dengan Create Missing Divisions

32. Muat ulang halaman Import > User Login
33. Klik [Upload File] di Dropzone dan pilih berkas `user-login-shift-mixed.csv`
34. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
35. Verifikasi Error Summary Callout memuat tiga baris pesan berurutan: "First Name: Max. 120 characters" (badge "1 row"), "Division not found" (badge "1 row"), dan "Shift: Invalid option" (badge "2 rows")
36. Verifikasi baris pesan "First Name: Max. 120 characters" hanya memuat `[View Data]` dan `[Delete All Rows]`
37. Verifikasi baris pesan "Division not found" memuat `[View Data]`, `[Delete All Rows]`, dan `[Create Missing Divisions]`
38. Verifikasi baris pesan "Shift: Invalid option" memuat `[View Data]`, `[Delete All Rows]`, dan `[Create Missing Options]`
39. Klik `⋯` pada baris #1
40. Verifikasi menu `⋯` baris #1 memuat `Duplicate`, `Edit`, dan `Remove`
41. Verifikasi menu `⋯` baris #1 tidak memuat tombol Create Missing
42. Tutup menu `⋯`
43. Klik `⋯` pada baris #2
44. Verifikasi menu `⋯` baris #2 memuat `Duplicate`, `Edit`, `[Create Missing Options]`, dan `Remove` dalam urutan tersebut
45. Tutup menu `⋯`
46. Klik `⋯` pada baris #3
47. Verifikasi menu `⋯` baris #3 memuat `Duplicate`, `Edit`, `[Create Missing Divisions]`, `[Create Missing Options]`, dan `Remove` dalam urutan tersebut
48. Tutup menu `⋯`, lalu reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-925: Custom Field Shift dinonaktifkan: kolom tampil seperti field Active tanpa Create Missing Options, tombol kembali bila diaktifkan lagi

49. Muat ulang halaman Import > User Login
50. Total Control Client C: klik [Upload File] di Dropzone dan pilih berkas `user-login-shift-lembur.csv`
51. Total Control Client C: biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
52. Total Control Client C: Tunggu aksi selesai (Modal Column Mapping tertutup)
53. Admin kedua Client C (sesi API): nonaktifkan Custom Field `Shift` hingga tersimpan
54. Total Control Client C: muat ulang halaman Import > User Login
55. Verifikasi kolom Shift tampil tanpa lencana
56. Verifikasi Banner Custom Field Deactivated tampil
57. Verifikasi baris #1 dan #2 tetap `error`
58. Verifikasi Error Summary Callout memuat "Shift: Invalid option" dengan badge "2 rows"
59. Verifikasi baris pesan "Shift: Invalid option" tanpa tombol `[Create Missing Options]`
60. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 1, Errors 2
61. Klik `⋯` pada baris #1
62. Verifikasi menu `⋯` baris #1 memuat `Duplicate`, `Edit`, dan `Remove`
63. Verifikasi menu `⋯` baris #1 tidak memuat `[Create Missing Options]`
64. Tutup menu `⋯`
65. Admin kedua Client C (sesi API): aktifkan kembali Custom Field `Shift` hingga tersimpan
66. Total Control Client C: muat ulang halaman Import > User Login
67. Verifikasi Error Summary Callout memuat "Shift: Invalid option" dengan badge "2 rows"
68. Verifikasi baris pesan "Shift: Invalid option" memuat tombol `[Create Missing Options]`
69. Verifikasi Banner Custom Field tidak tampil
70. Klik `⋯` pada baris #1
71. Verifikasi menu `⋯` baris #1 memuat `[Create Missing Options]`
72. Tutup menu `⋯`, lalu reset draft User Login Client C lewat fixture reset

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Subjudul `###` memetakan langkah ke id TC.
- Urutan: Tab Brand, lalu Tab User Login dengan TC-GS-IMPORT-349 dan 734 berbagi satu draft, TC-GS-IMPORT-344, 924, dan TC-GS-IMPORT-925 terakhir karena mengubah status Custom Field (state global).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 8 (memilih sub-tab), 7, 22, 31, 48, 72 (reset draft, S-09), 23, 32, 49, 54, 66 (muat ulang halaman Import > User Login; langkah 23, 32, dan 49 memuat ulang halaman setelah reset fixture sebelum [Upload File]), 19, 22, 31, 42, 45, 48, 64, 72 (menutup menu atau overlay), 26 dan 31 (centang dan hapus centang), 53 dan 65 (pemicu Admin kedua). Langkah 52 (Tunggu aksi selesai: menunggu aksi tanpa `Verifikasi` selesai sebelum Admin kedua menonaktifkan Custom Field `Shift` lewat sesi API; penanda Modal Column Mapping tertutup).
- Verifikasi pembanding pada absence menu `⋯` (langkah 18, 40, 63): menu berisi `Duplicate`, `Edit`, `Remove` diverifikasi lebih dulu sebagai anchor positif (butir 2 bagian 8b); pada langkah 63 daftar pembanding ini tidak ada di Expected TC dan ditambahkan hanya sebagai anchor. Absence setelah muat ulang (langkah 69) didahului langkah 67 dan 68 pada halaman yang sama.
- P-2: Admin kedua Client C hanya memicu penonaktifan dan pengaktifan Custom Field `Shift` lewat sesi API pada TC-GS-IMPORT-925; semua asersi ada di sesi Total Control Client C.
- Spec melewati sekitar 35 langkah (72 langkah): enam blok satu kelas (fungsional, observasi tombol), tiap blok berdiri sendiri dengan draft dan reset sendiri; kegagalan satu blok tidak menghilangkan makna blok lain. TC-GS-IMPORT-349 dan 734 berbagi satu upload.
- Setelah tiap reset draft lewat fixture pada Tab User Login (langkah 22, 31, 48), halaman dimuat ulang (langkah 23, 32, 49) sebelum [Upload File] agar UI tidak basi dan tidak memunculkan dialog Append lebih dulu.
- Pembagian TC lintas spec: aksi Create Missing sebenarnya ada di spec 123 sampai 130; visibilitas peran Read Only dan Create ada di spec 131 dan 132.
- Temuan untuk QA:
  - TC-GS-IMPORT-925: Expected a berbunyi "kolom Shift tampil tanpa lencana dengan Banner Custom Field Deactivated"; spec memecahnya menjadi dua `Verifikasi` (kolom tanpa lencana, Banner tampil) karena kalimat ambigu tentang hubungan keduanya.
  - TC-GS-IMPORT-925: cara menonaktifkan dan mengaktifkan Custom Field lewat "fixture permintaan" tidak dirinci; disediakan tim FE/BE tanpa endpoint karangan.
  - TC-GS-IMPORT-344: pada Expected b tidak dinyatakan label tombol `[Delete]` selain "hanya berisi `[Delete]`"; spec memverifikasi isi overlay apa adanya.
  - Berkas `user-login-first-long-logistik.csv`, `user-login-logistik-4.csv`, dan `user-login-shift-mixed.csv` didefinisikan pada kolom Data Uji TC (D-87 untuk yang terakhir).
  - Post Condition semua TC (isi draft) tidak punya langkah observasi dan tidak diasersi.
