---
id: TC-GS-IMPORT-E2E-127-create-missing-divisions-dan-positions-saat-admin-lain-mengubah-data
title: "Create Missing Divisions dan Positions saat admin lain mengubah data lebih dulu: duplicate ditolak, baris pulih, no-op dari halaman basi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-335
  - TC-GS-IMPORT-337
  - TC-GS-IMPORT-735
  - TC-GS-IMPORT-855
  - TC-GS-IMPORT-858
  - TC-GS-IMPORT-875
coverage:
  web: automated
---

# Create Missing Divisions dan Positions saat admin lain mengubah data lebih dulu: duplicate ditolak, baris pulih, no-op dari halaman basi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
- Pelaku kedua: Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net` (Pre-setup), hanya memicu pembuatan Position atau Division dan penghapusan baris draft lewat sesi API (P-2) dengan `Spectra.env.GS_CLIENTC_TC2_PASSWORD`; tidak ada sesi UI kedua. Kemampuan "buat Position", "buat Division", dan "hapus baris draft" atas nama Admin kedua disediakan tim FE/BE (fixture permintaan); mekanisme tidak disebut TC.
- Layar awal: hook `beforeEach` suite membuka Import > User Login (Client C). TC-GS-IMPORT-337 berawal di Global Settings > User > Division sehingga langkah pertamanya berpindah ke sana.
- Data Pre-setup Client C (tidak diubah): Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang` (5 baris); Position `Store Manager`, `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor` (5 baris). Client C tanpa draft Tab User Login pada awal spec (Kontrak Fixture R1).
- Data Dinamis (fixture baru `Fixture.import.berkas`, disediakan tim QA; berkas User Login standar D-45): `user-login-store-supervisor-1.csv` (1 baris: Siti Rahmawati, Division `Engineering`, Position `Store Supervisor`), `user-login-logistik-4.csv` (4 baris Division `Logistik`), `user-login-logistik-2.csv` (2 baris Division `Logistik`), `user-login-logistik-plus-5.csv` (5 baris: baris 1 sampai 4 Division `Logistik`, baris 5 Division `Engineering`), `user-login-logistik-pengadaan-4.csv` (4 baris: baris 1 dan 2 `Logistik`, baris 3 dan 4 `Pengadaan`).
- Nama master data `Logistik`, `Pengadaan`, dan `Store Supervisor` literal tanpa suffix karena isi berkas CSV menentukan hasil "not found" (pengecualian S-12 nama literal). Hook `before` menghapus sisa nama itu lewat API; langkah penghubung menghapusnya di antara TC; hook `after` menghapusnya lagi dan melakukan Discard Draft Tab User Login Client C.
- Layanan AI mock mode normal (D-40, tabel D-41 dan D-42): disetel di hook `before`, dikembalikan di hook `after`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Baseline Changelog Division (TC-GS-IMPORT-337): angka total Pagination dengan Filter Action `Create` dicatat sebelum aksi (S-12); tidak ada asersi angka absolut.
- Kemampuan teknis disediakan tim FE/BE: reset draft Tab User Login Client C (Kontrak Fixture R1) dan hapus Division atau Position lewat API (R2). Sinkronisasi jam browser dan jam server tidak dibutuhkan (tidak ada asersi waktu).
- State global: master data Client C dan mock AI; suite berjalan serial (`parallel: false`).
- Env var: `GS_CLIENTC_TC_PASSWORD`, `GS_CLIENTC_TC2_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-335: Position dibuat pihak lain tepat sebelum klik ditolak sebagai duplicate

1. Klik [Upload File] di Dropzone
2. Pilih berkas `user-login-store-supervisor-1.csv` di file picker
3. Biarkan seluruh dropdown File Column pada nilai auto-match
4. Klik [Confirm Mapping]
5. Tunggu aksi selesai (Modal Column Mapping tertutup)
6. Admin kedua Client C (sesi API): buat Position `Store Supervisor` hingga tersimpan
7. Total Control Client C (halaman Import belum dimuat ulang): klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
8. Verifikasi toast error "Error, failed to create position."
9. Verifikasi UI membaca ulang Staging Table dan baris #1 berstatus `pending` tanpa muat ulang manual
10. Verifikasi Error Summary Callout tidak tampil
11. Buka Global Settings > User > Position
12. Verifikasi daftar Position memuat tepat satu `Store Supervisor` (6 baris pada tabel)

### TC-GS-IMPORT-337: Nama dibuat pihak lain tepat sebelum klik ditolak, baris tetap pulih

13. Hapus Position `Store Supervisor` lewat API dan reset draft Tab User Login Client C ke tanpa draft
14. Buka Global Settings > User > Division
15. Klik icon `[Changelog]`
16. Klik icon Filter
17. Pilih Action `Create` pada dropdown Action
18. Klik `[Apply]`
19. Catat angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state)
20. Tutup modal Changelog Division
21. Buka Import > User Login
22. Klik [Upload File] di Dropzone
23. Pilih berkas `user-login-logistik-4.csv` di file picker
24. Biarkan seluruh dropdown File Column pada nilai auto-match
25. Klik [Confirm Mapping]
26. Tunggu aksi selesai (Modal Column Mapping tertutup)
27. Admin kedua Client C (sesi API): buat Division `Logistik` hingga tersimpan
28. Total Control Client C (halaman Import belum dimuat ulang): klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
29. Verifikasi toast error "Error, failed to create division."
30. Verifikasi UI membaca ulang Staging Table dan keempat baris berstatus `pending` tanpa muat ulang manual
31. Verifikasi Error Summary Callout tidak tampil
32. Buka Global Settings > User > Division
33. Klik icon `[Changelog]`
34. Klik icon Filter
35. Pilih Action `Create` pada dropdown Action
36. Klik `[Apply]`
37. Baca angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state)
38. Verifikasi total pada Pagination Changelog Division dengan Filter Action `Create` bertambah tepat 1 dibanding langkah 19
39. Verifikasi entri teratas Changelog Division memuat Division Name `Logistik` dan Modified By `Oki S`
40. Tutup modal Changelog Division

### TC-GS-IMPORT-735: Position dibuat pihak lain membuat baris pulih ke pending pada pembacaan berikutnya

41. Hapus Division `Logistik` lewat API, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
42. Klik [Upload File] di Dropzone dan pilih berkas `user-login-store-supervisor-1.csv`
43. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
44. Verifikasi baris #1 berstatus `error`
45. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "1 row"
46. Admin kedua Client C (sesi API): buat Position `Store Supervisor` hingga tersimpan
47. Total Control Client C: muat ulang halaman Import > User Login
48. Verifikasi baris #1 berstatus `pending`
49. Verifikasi Staging Metric Cards: Total Rows 1, Ready to Import 1, Errors 0
50. Verifikasi Error Summary Callout tidak tampil
51. Buka Global Settings > User > Position
52. Verifikasi daftar Position memuat tepat satu `Store Supervisor` (6 baris pada tabel)

### TC-GS-IMPORT-855: Create Missing Divisions per-baris pada baris yang dihapus admin lain menjadi no-op

53. Hapus Position `Store Supervisor` lewat API, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
54. Unggah berkas `user-login-logistik-2.csv`, klik [Confirm Mapping], dan buka menu `⋯` baris #1 (jangan muat ulang halaman setelahnya)
55. Tunggu aksi selesai (Modal Column Mapping tertutup)
56. Admin kedua Client C (sesi API): hapus baris #1 hingga tersimpan
57. Total Control Client C: pilih [Create Missing Divisions] pada menu baris #1
58. Verifikasi tidak ada dialog tampil
59. Verifikasi tidak ada toast tampil
60. Verifikasi UI di-refresh dan draft menampilkan 1 baris `error` dengan Division `Logistik`
61. Buka Global Settings > User > Division
62. Verifikasi daftar Division memuat `Engineering` sebagai pembanding
63. Verifikasi daftar Division tidak memuat `Logistik`

### TC-GS-IMPORT-858: Bulk Create Missing dari halaman basi setelah baris kategori dihapus admin lain menjadi no-op

64. Reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
65. Klik [Upload File] dan pilih berkas `user-login-logistik-plus-5.csv`
66. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
67. Tunggu aksi selesai (Modal Column Mapping tertutup)
68. Admin kedua Client C (sesi API): hapus baris #1 sampai #4 (keempatnya Division `Logistik`) hingga tersimpan
69. Total Control Client C (halaman belum dimuat ulang): klik [Create Missing Divisions] pada kategori "Division not found" di Error Summary Callout
70. Verifikasi tidak ada dialog tampil
71. Verifikasi tidak ada toast tampil
72. Verifikasi Staging Table menampilkan 1 baris `pending` (Division `Engineering`)
73. Verifikasi Error Summary Callout tidak tampil
74. Buka Global Settings > User > Division
75. Verifikasi daftar Division memuat `Engineering` sebagai pembanding
76. Verifikasi daftar Division tidak memuat `Logistik`

### TC-GS-IMPORT-875: Bulk Create Missing dari halaman basi, nama yang baris sumbernya dihapus dilewati

77. Reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
78. Unggah `user-login-logistik-pengadaan-4.csv` dan klik [Confirm Mapping]
79. Tunggu aksi selesai (Modal Column Mapping tertutup)
80. Admin kedua Client C (sesi API): hapus baris #1 dan #2 (Division `Logistik`) hingga tersimpan
81. Total Control Client C (halaman belum dimuat ulang): klik [Create Missing Divisions] pada kategori "Division not found" di Error Summary Callout
82. Verifikasi toast sukses "Success, division has been created. Some items were skipped."
83. Verifikasi draft menampilkan 2 baris `pending` (Division `Pengadaan`)
84. Verifikasi Error Summary Callout tidak tampil
85. Buka Global Settings > User > Division
86. Verifikasi daftar Division memuat `Pengadaan`
87. Verifikasi daftar Division tidak memuat `Logistik`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-335, 337, 735, 855, 858, 875).
- P-2: Admin kedua Client C hanya memicu perubahan state (membuat Position atau Division, menghapus baris draft) lewat sesi API; seluruh asersi di sesi Total Control Client C. TC-GS-IMPORT-337 membaca Changelog Division di sesi Total Control untuk entri yang dibuat Admin kedua.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (335, 337, 735, 855, 858, 875) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13, 41, 53, 64, dan 77 (hapus master data buatan Admin kedua dan reset draft sebagai precondition TC berikutnya, Kontrak Fixture R1 dan R2); langkah 14 sampai 19 membuka Division dan Changelog serta mencatat baseline di TC-GS-IMPORT-337; langkah 20 dan 40 menutup modal Changelog Division sebelum pindah ke Import atau ke blok berikutnya (S-09); langkah 61, 74, dan 85 membuka daftar Division. Langkah 62 dan 75 adalah `Verifikasi` data pembanding sebagai anchor asersi absence `Logistik` (8b butir 2). Langkah 5, 26, 55, 67, 79 (Tunggu aksi selesai: menunggu aksi tanpa `Verifikasi` selesai sebelum Admin kedua mengubah data lewat sesi API; penanda Modal Column Mapping tertutup).
- Spec berisi 87 langkah, di atas sekitar 35 langkah. Alasan: enam blok berstatus Edge dengan pola sama (unggah, Admin kedua mengubah data lebih dulu, aksi dari halaman basi, verifikasi), tiap blok berdiri sendiri dengan draft dan master data yang di-reset di langkah pembuka, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok baca Changelog (langkah 14 sampai 19 dan 32 sampai 39) adalah blok baca-log berpola dan tidak dihitung ke estimasi.
- Pembagian TC lintas spec: pola Create Missing per-baris dan bulk tanpa konflik ada di spec 123 dan 124; kegagalan sebagian dan kategori Callout baru di spec 125; konflik kunci sesi di spec 126.
- Temuan untuk QA:
  - TC-GS-IMPORT-335, 337, dan 735 menulis Admin kedua membuat Position atau Division lewat UI (`[+ Position]` atau `[+ Division]`, isi nama, `[Submit]`); spec memakai sesi API sesuai P-2 karena hasil di sesi itu tidak diasersi.
  - TC-GS-IMPORT-855, 858, dan 875 menulis "lewat fixture permintaan" tanpa mendefinisikan fixture itu di Kontrak Fixture; dicatat sebagai kemampuan disediakan tim FE/BE tanpa mengarang endpoint.
  - TC-GS-IMPORT-337 menulis Precondition b "User berada di Global Settings > User > Division" sedangkan Precondition lain berawal di Import > User Login; spec berawal di Division sesuai Langkah Uji 1 sampai 5.
  - TC-GS-IMPORT-855 dan 858 mengasersi "tidak ada dialog dan tidak ada toast"; ketiadaan toast diasersi segera setelah pemicu dengan anchor pemicu klik dan refresh draft pada langkah berikutnya.
  - Post Condition "Position Store Supervisor tersimpan di Client C" (TC-GS-IMPORT-335, 735) dan "Division Logistik tersimpan di Client C" (TC-GS-IMPORT-337) diamati lewat daftar Position atau Changelog Division, bukan lewat pembacaan data BE; "Tidak ada Division baru" pada TC-GS-IMPORT-855 dan 858 diamati lewat daftar Division.
