---
id: TC-GS-IMPORT-E2E-124-create-missing-divisions-dan-positions-bulk-dari-callout-dedup-nama
title: "Create Missing Divisions dan Positions bulk dari Callout: dedup nama tidak peka huruf besar-kecil; record tetap ada setelah Discard Draft"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-327
  - TC-GS-IMPORT-328
  - TC-GS-IMPORT-329
  - TC-GS-IMPORT-345
  - TC-GS-IMPORT-717
  - TC-GS-IMPORT-718
coverage:
  web: automated
---

# Create Missing Divisions dan Positions bulk dari Callout: dedup nama tidak peka huruf besar-kecil; record tetap ada setelah Discard Draft

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import; sub-tab dipilih di `## Test Steps`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Pre-setup Client C (tidak diubah): Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang` (5 item, `Logistik` belum ada); Position `Store Manager`, `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor` (5 item, `Store Supervisor` belum ada). Client C tanpa draft Tab User Login dan User Non Login sebelum tiap TC (fixture reset, Kontrak Fixture R1).
- Data Dinamis (berkas disediakan tim QA, fixture baru `Fixture.import.berkas`; berkas standar D-45): `user-login-logistik-4.csv` (Siti Rahmawati, Budi Santoso, Andi Pratama, Rina Wijaya; Division `Logistik`; Position kosong), `user-login-logistik-case.csv` (3 baris; Division `Logistik` baris #1, `LOGISTIK` baris #2, ` logistik ` dengan spasi di awal dan di akhir baris #3), `user-login-store-supervisor-3.csv` (3 baris; Division `Engineering`, Position `Store Supervisor`), `user-non-login-logistik-3.csv` (Ayu Lestari, Dimas Prakoso, Maya Anggraini; Division `Logistik`; Represented By `budi.manager.c@example.com`), `user-non-login-store-supervisor-3.csv` (tiga baris yang sama; Division `Engineering`, Position `Store Supervisor`). Nama `Logistik` dan `Store Supervisor` literal sesuai TC (pengecualian S-12 untuk Name literal penentu hasil auto-generate Code); record yang dibuat spec dihapus lewat API setelah tiap TC (R2) dan sisa run sebelumnya dibersihkan di hook `before`.
- Kemampuan teknis: hook umur draft D-76 varian (1) (memundurkan `created_at` draft 25 jam lewat fixture timestamp atau jam server non-produksi; dipakai pada TC-GS-IMPORT-345 agar Unsaved Banner tampil); fixture reset draft client; penghapusan Division dan Position lewat API; pembacaan pagination Division dan Position.
- State global: jam server tidak digeser bila hook umur draft memakai fixture timestamp; bila memakai jam server, dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).
- Cleanup (hook `afterEach`/`after`, tidak berasumsi setup berhasil penuh): hapus Division `Logistik` dan Position `Store Supervisor` bila ada, reset draft User Login dan User Non Login Client C, pulihkan jam server bila digeser.

## Test Steps

### TC-GS-IMPORT-327: Bulk Create Missing Divisions dari Error Summary Callout melakukan dedup nama identik

1. Pilih sub-tab User Login
2. Klik [Upload File] di toolbar dan pilih berkas `user-login-logistik-4.csv`
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "4 rows"
5. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
6. Verifikasi tidak ada dialog konfirmasi
7. Verifikasi toast sukses: "Success, division has been created."
8. Muat ulang halaman Import > User Login
9. Verifikasi keempat baris berstatus `pending`
10. Verifikasi Staging Metric Cards: Total Rows 4, Ready to Import 4, Errors 0
11. Buka Global Settings > User > Division dan perhatikan daftar Division
12. Verifikasi daftar Division memuat tepat satu `Logistik`
13. Verifikasi tabel Division menampilkan 6 baris
14. Hapus Division `Logistik` lewat API dan reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-329: Dedup nama tidak peka huruf besar-kecil dan trim spasi tepi, ejaan kemunculan pertama menurut Row #

15. Buka Import dan pilih sub-tab User Login
16. Klik [Upload File] di toolbar dan pilih berkas `user-login-logistik-case.csv`
17. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
18. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
19. Verifikasi toast sukses: "Success, division has been created."
20. Muat ulang halaman Import > User Login
21. Verifikasi ketiga baris berstatus `pending`
22. Buka Global Settings > User > Division dan perhatikan daftar Division
23. Verifikasi daftar Division memuat tepat satu `Logistik`
24. Verifikasi tabel Division menampilkan 6 baris
25. Verifikasi daftar Division tidak memuat `LOGISTIK` maupun `logistik`
26. Hapus Division `Logistik` lewat API dan reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-328: Bulk Create Missing Positions dari Callout untuk 3 baris yang merujuk Position sama

27. Buka Import dan pilih sub-tab User Login
28. Klik [Upload File] di toolbar dan pilih berkas `user-login-store-supervisor-3.csv`
29. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
30. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "3 rows"
31. Klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
32. Verifikasi toast sukses: "Success, position has been created."
33. Muat ulang halaman Import > User Login
34. Verifikasi ketiga baris berstatus `pending`
35. Buka Global Settings > User > Position dan perhatikan daftar Position
36. Verifikasi daftar Position memuat tepat satu `Store Supervisor`
37. Verifikasi tabel Position menampilkan 6 baris
38. Hapus Position `Store Supervisor` lewat API dan reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-717: Bulk Create Missing Divisions dari Callout Tab User Non Login melakukan dedup nama identik

39. Buka Import dan pilih sub-tab User Non Login
40. Klik [Upload File] di toolbar dan pilih berkas `user-non-login-logistik-3.csv`
41. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
42. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "3 rows"
43. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
44. Verifikasi toast sukses: "Success, division has been created."
45. Muat ulang halaman Import > User Non Login
46. Verifikasi ketiga baris berstatus `pending`
47. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 3, Errors 0
48. Buka Global Settings > User > Division dan perhatikan daftar Division
49. Verifikasi daftar Division memuat tepat satu `Logistik`
50. Verifikasi tabel Division menampilkan 6 baris
51. Hapus Division `Logistik` lewat API dan reset draft User Non Login Client C lewat fixture reset

### TC-GS-IMPORT-718: Bulk Create Missing Positions dari Callout Tab User Non Login melakukan dedup nama identik

52. Buka Import dan pilih sub-tab User Non Login
53. Klik [Upload File] di toolbar dan pilih berkas `user-non-login-store-supervisor-3.csv`
54. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
55. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "3 rows"
56. Klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
57. Verifikasi toast sukses: "Success, position has been created."
58. Muat ulang halaman Import > User Non Login
59. Verifikasi ketiga baris berstatus `pending`
60. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 3, Errors 0
61. Buka Global Settings > User > Position dan perhatikan daftar Position
62. Verifikasi daftar Position memuat tepat satu `Store Supervisor`
63. Verifikasi tabel Position menampilkan 6 baris
64. Hapus Position `Store Supervisor` lewat API dan reset draft User Non Login Client C lewat fixture reset

### TC-GS-IMPORT-345: Record hasil Create Missing tetap ada setelah Discard Draft

65. Buka Import dan pilih sub-tab User Login
66. Klik [Upload File] di toolbar dan pilih berkas `user-login-logistik-4.csv`
67. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
68. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
69. Tunggu aksi selesai (permintaan mendapat respons)
70. Mundurkan umur draft 25 jam lewat hook umur draft (D-76), lalu muat ulang halaman Import > User Login
71. Klik [Discard] pada Unsaved Banner
72. Klik [Discard Draft] pada dialog
73. Verifikasi toast sukses: "Success, draft has been discarded."
74. Verifikasi Tab User Login menampilkan Dropzone (belum ada draft)
75. Buka Global Settings > User > Division dan perhatikan daftar Division
76. Verifikasi daftar Division memuat `Logistik`
77. Verifikasi tabel Division menampilkan 6 baris
78. Hapus Division `Logistik` lewat API

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Subjudul `###` memetakan langkah ke id TC.
- Urutan: TC-GS-IMPORT-327, 329 (Division), 328 (Position), 717, 718 (User Non Login), lalu TC-GS-IMPORT-345 terakhir karena menghapus draft (aksi merusak ditaruh paling akhir).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 15, 27, 39, 52, 65 (memilih sub-tab), 11, 22, 35, 48, 61, 75 (membuka daftar master data), 14, 26, 38, 51, 64, 78 (pemulihan master data dan draft, R2 dan S-09), 69 (menunggu aksi Create Missing selesai sebelum umur draft dimundurkan, bagian 8b butir 8), 70 (pemicu umur draft, hook D-76, dan muat ulang), 71 (membuka dialog Discard).
- Langkah 69 menunggu permintaan Create Missing Divisions selesai sebelum langkah 70 memundurkan umur draft lewat hook dan memuat ulang halaman, supaya hook dan muat ulang tidak berlomba dengan permintaan yang belum selesai; langkah 69 tanpa `Verifikasi` karena TC tidak memuat Expected penyelesaian untuk aksi itu; penanda memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati.
- Absence langkah 6 (dialog konfirmasi) diletakkan segera setelah pemicu dan berjangkar pada toast langkah 7; absence langkah 25 berjangkar pada langkah 23.
- Spec melewati sekitar 35 langkah (78 langkah): enam blok homogen (bulk Create Missing per Tab atau jenis), satu kelas fungsional, tiap blok berdiri sendiri dengan master data dan draft sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Pembagian TC lintas spec: Create Missing per-baris ada di spec 123; kegagalan sebagian di spec 125; konflik data admin lain di spec 127; pencatatan log di spec 128.
- Temuan untuk QA:
  - TC-GS-IMPORT-345: langkah 4 TC ("lewat hook umur draft... lalu klik `[Discard]` pada Unsaved Banner") menggabungkan pemicu hook, muat ulang, dan klik dalam satu langkah; spec memecahnya menjadi langkah 70 dan 71. Munculnya Unsaved Banner tidak punya Expected sendiri di TC dan tidak diasersi.
  - TC-GS-IMPORT-345: langkah 3 TC tidak memuat Expected penyelesaian untuk `[Create Missing Divisions]`; pemulihan keempat baris ke `pending` menurut PRD hanya teramati pada pembacaan Staging Table berikutnya (setelah muat ulang), sehingga langkah 69 tidak menegaskan Callout hilang atau baris `pending` sebelum muat ulang langkah 70. Penanda yang teramati sebelum muat ulang belum ditetapkan TC atau PRD.
  - TC-GS-IMPORT-329: Expected c membedakan `Logistik`, `LOGISTIK`, dan `logistik` hanya dari daftar Division tanpa memeriksa Row # yang tersimpan; spec mengikuti Expected TC (ejaan kemunculan pertama = baris #1 `Logistik`).
  - Berkas `user-login-logistik-case.csv`, `user-login-store-supervisor-3.csv`, `user-non-login-logistik-3.csv`, dan `user-non-login-store-supervisor-3.csv` hanya didefinisikan pada kolom Data Uji TC.
  - Hitungan "6 baris" mengandalkan Pre-setup 5 Division dan 5 Position tanpa record sisa spec lain.
  - Post Condition semua TC (isi draft dan record tersimpan) tanpa langkah observasi tersendiri tidak diasersi, kecuali yang sudah menjadi Expected.
