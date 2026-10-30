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

1. Klik [Upload File] di toolbar
2. Pilih berkas `user-login-store-supervisor-1.csv` di file picker
3. Biarkan seluruh dropdown File Column pada nilai auto-match
4. Klik [Confirm Mapping]
5. Admin kedua Client C (sesi API): buat Position `Store Supervisor` hingga tersimpan
6. Total Control Client C (halaman Import belum dimuat ulang): klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
7. Verifikasi toast error "Error, failed to create position."
8. Verifikasi UI membaca ulang Staging Table dan baris #1 berstatus `pending` tanpa muat ulang manual
9. Verifikasi Error Summary Callout tidak tampil
10. Buka Global Settings > User > Position
11. Verifikasi daftar Position memuat tepat satu `Store Supervisor` (6 baris pada tabel)

### TC-GS-IMPORT-337: Nama dibuat pihak lain tepat sebelum klik ditolak, baris tetap pulih

12. Hapus Position `Store Supervisor` lewat API dan reset draft Tab User Login Client C ke tanpa draft
13. Buka Global Settings > User > Division
14. Klik icon `[Changelog]`
15. Klik icon Filter
16. Pilih Action `Create` pada dropdown Action
17. Klik `[Apply]`
18. Catat angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state)
19. Buka Import > User Login
20. Klik [Upload File] di toolbar
21. Pilih berkas `user-login-logistik-4.csv` di file picker
22. Biarkan seluruh dropdown File Column pada nilai auto-match
23. Klik [Confirm Mapping]
24. Admin kedua Client C (sesi API): buat Division `Logistik` hingga tersimpan
25. Total Control Client C (halaman Import belum dimuat ulang): klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
26. Verifikasi toast error "Error, failed to create division."
27. Verifikasi UI membaca ulang Staging Table dan keempat baris berstatus `pending` tanpa muat ulang manual
28. Verifikasi Error Summary Callout tidak tampil
29. Buka Global Settings > User > Division
30. Klik icon `[Changelog]`
31. Klik icon Filter
32. Pilih Action `Create` pada dropdown Action
33. Klik `[Apply]`
34. Baca angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state)
35. Verifikasi total pada Pagination Changelog Division dengan Filter Action `Create` bertambah tepat 1 dibanding langkah 18
36. Verifikasi entri teratas Changelog Division memuat Division Name `Logistik` dan Modified By `Oki S`

### TC-GS-IMPORT-735: Position dibuat pihak lain membuat baris pulih ke pending pada pembacaan berikutnya

37. Hapus Division `Logistik` lewat API, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
38. Klik [Upload File] di toolbar dan pilih berkas `user-login-store-supervisor-1.csv`
39. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
40. Verifikasi baris #1 berstatus `error`
41. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "1 row"
42. Admin kedua Client C (sesi API): buat Position `Store Supervisor` hingga tersimpan
43. Total Control Client C: muat ulang halaman Import > User Login
44. Verifikasi baris #1 berstatus `pending`
45. Verifikasi Staging Metric Cards: Total Rows 1, Ready to Import 1, Errors 0
46. Verifikasi Error Summary Callout tidak tampil
47. Buka Global Settings > User > Position
48. Verifikasi daftar Position memuat tepat satu `Store Supervisor` (6 baris pada tabel)

### TC-GS-IMPORT-855: Create Missing Divisions per-baris pada baris yang dihapus admin lain menjadi no-op

49. Hapus Position `Store Supervisor` lewat API, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
50. Unggah berkas `user-login-logistik-2.csv`, klik [Confirm Mapping], dan buka menu `⋯` baris #1 (jangan muat ulang halaman setelahnya)
51. Admin kedua Client C (sesi API): hapus baris #1 hingga tersimpan
52. Total Control Client C: pilih [Create Missing Divisions] pada menu baris #1
53. Verifikasi tidak ada dialog tampil
54. Verifikasi tidak ada toast tampil
55. Verifikasi UI di-refresh dan draft menampilkan 1 baris `error` dengan Division `Logistik`
56. Buka Global Settings > User > Division
57. Verifikasi daftar Division memuat `Engineering` sebagai pembanding
58. Verifikasi daftar Division tidak memuat `Logistik`

### TC-GS-IMPORT-858: Bulk Create Missing dari halaman basi setelah baris kategori dihapus admin lain menjadi no-op

59. Reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
60. Klik [Upload File] dan pilih berkas `user-login-logistik-plus-5.csv`
61. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
62. Admin kedua Client C (sesi API): hapus baris #1 sampai #4 (keempatnya Division `Logistik`) hingga tersimpan
63. Total Control Client C (halaman belum dimuat ulang): klik [Create Missing Divisions] pada kategori "Division not found" di Error Summary Callout
64. Verifikasi tidak ada dialog tampil
65. Verifikasi tidak ada toast tampil
66. Verifikasi Staging Table menampilkan 1 baris `pending` (Division `Engineering`)
67. Verifikasi Error Summary Callout tidak tampil
68. Buka Global Settings > User > Division
69. Verifikasi daftar Division memuat `Engineering` sebagai pembanding
70. Verifikasi daftar Division tidak memuat `Logistik`

### TC-GS-IMPORT-875: Bulk Create Missing dari halaman basi, nama yang baris sumbernya dihapus dilewati

71. Reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
72. Unggah `user-login-logistik-pengadaan-4.csv` dan klik [Confirm Mapping]
73. Admin kedua Client C (sesi API): hapus baris #1 dan #2 (Division `Logistik`) hingga tersimpan
74. Total Control Client C (halaman belum dimuat ulang): klik [Create Missing Divisions] pada kategori "Division not found" di Error Summary Callout
75. Verifikasi toast sukses "Success, division has been created. Some items were skipped."
76. Verifikasi draft menampilkan 2 baris `pending` (Division `Pengadaan`)
77. Verifikasi Error Summary Callout tidak tampil
78. Buka Global Settings > User > Division
79. Verifikasi daftar Division memuat `Pengadaan`
80. Verifikasi daftar Division tidak memuat `Logistik`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-335, 337, 735, 855, 858, 875).
- P-2: Admin kedua Client C hanya memicu perubahan state (membuat Position atau Division, menghapus baris draft) lewat sesi API; seluruh asersi di sesi Total Control Client C. TC-GS-IMPORT-337 membaca Changelog Division di sesi Total Control untuk entri yang dibuat Admin kedua.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (335, 337, 735, 855, 858, 875) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12, 37, 49, 59, dan 71 (hapus master data buatan Admin kedua dan reset draft sebagai precondition TC berikutnya, Kontrak Fixture R1 dan R2); langkah 13 sampai 19 membuka Division dan Changelog serta mencatat baseline di TC-GS-IMPORT-337; langkah 56, 68, dan 78 membuka daftar Division. Langkah 57 dan 69 adalah `Verifikasi` data pembanding sebagai anchor asersi absence `Logistik` (8b butir 2).
- Spec berisi 80 langkah, di atas sekitar 35 langkah. Alasan: enam blok berstatus Edge dengan pola sama (unggah, Admin kedua mengubah data lebih dulu, aksi dari halaman basi, verifikasi), tiap blok berdiri sendiri dengan draft dan master data yang di-reset di langkah pembuka, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok baca Changelog (langkah 13 sampai 18 dan 29 sampai 36) adalah blok baca-log berpola dan tidak dihitung ke estimasi.
- Pembagian TC lintas spec: pola Create Missing per-baris dan bulk tanpa konflik ada di spec 123 dan 124; kegagalan sebagian dan kategori Callout baru di spec 125; konflik kunci sesi di spec 126.
- Temuan untuk QA:
  - TC-GS-IMPORT-335, 337, dan 735 menulis Admin kedua membuat Position atau Division lewat UI (`[+ Position]` atau `[+ Division]`, isi nama, `[Submit]`); spec memakai sesi API sesuai P-2 karena hasil di sesi itu tidak diasersi.
  - TC-GS-IMPORT-855, 858, dan 875 menulis "lewat fixture permintaan" tanpa mendefinisikan fixture itu di Kontrak Fixture; dicatat sebagai kemampuan disediakan tim FE/BE tanpa mengarang endpoint.
  - TC-GS-IMPORT-337 menulis Precondition b "User berada di Global Settings > User > Division" sedangkan Precondition lain berawal di Import > User Login; spec berawal di Division sesuai Langkah Uji 1 sampai 5.
  - TC-GS-IMPORT-855 dan 858 mengasersi "tidak ada dialog dan tidak ada toast"; ketiadaan toast diasersi segera setelah pemicu dengan anchor pemicu klik dan refresh draft pada langkah berikutnya.
  - Post Condition "Position Store Supervisor tersimpan di Client C" (TC-GS-IMPORT-335, 735) dan "Division Logistik tersimpan di Client C" (TC-GS-IMPORT-337) diamati lewat daftar Position atau Changelog Division, bukan lewat pembacaan data BE; "Tidak ada Division baru" pada TC-GS-IMPORT-855 dan 858 diamati lewat daftar Division.
