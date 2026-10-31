---
id: TC-GS-IMPORT-E2E-140-late-binding-referensi-saat-commit-division-dihapus-position-di-rename
title: "Late-binding referensi saat commit: Division dihapus, Position di-rename, Represented By berubah, referensi hanya di draft tidak sah"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-322
  - TC-GS-IMPORT-388
  - TC-GS-IMPORT-389
  - TC-GS-IMPORT-390
  - TC-GS-IMPORT-391
  - TC-GS-IMPORT-751
  - TC-GS-IMPORT-752
coverage:
  web: automated
---

# Late-binding referensi saat commit: Division dihapus, Position di-rename, Represented By berubah, referensi hanya di draft tidak sah

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pelaku kedua: Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC2_PASSWORD`, hanya lewat sesi API sebagai pemicu perubahan master data (P-2); tidak ada asersi di sesi itu. Pemicu TC-GS-IMPORT-322 memakai sesi API akun Total Control Client E yang sama.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > User Login (Client E); perpindahan Sub-Tab atau halaman lain ditulis sebagai langkah.
- Data Pre-setup Client E (diubah lalu dipulihkan): Division `Gudang` dan `Engineering`; Position `Technician` dan `Finance Manager`; Login User aktif `rina.admin.e@example.com`, `budi.manager.e@example.com`, `dewi.anggraini.e@example.com`; produk organisasi Global Settings dan Fixed Asset.
- Data Dinamis (berkas dan draft lewat fixture `Fixture.import.lateBinding140`, fixture baru; nama literal dari Data Dinamis karena asersi bergantung pada nama dan jumlah): user-login-gudang-engineering.csv (berkas khusus commit D-45: Bambang Hartono Division `Gudang`, Citra Wulandari Division `Engineering`); D-54 (user-login-commit-8.csv, 8 baris `pending`); D-55 (user-non-login-commit-5.csv, 5 baris `pending`); division-ref-1.csv (`Legal`/`LGL`); user-login-ref-div-1.csv (Kevin Anggara / kevin.anggara@example.com / Division `Legal` / Access Global Settings); position-ref-1.csv (`Sales Executive`); user-login-ref-pos-1.csv (Kevin Anggara / Division `Engineering` / Position `Sales Executive` / Access Global Settings).
- Kemampuan teknis (disediakan tim FE/BE): mock layanan AI mode normal (D-40, D-42) dipulihkan ke normal di hook `after`; skrip reset Client E sesuai D-47 (hapus User Login, User Non Login, Division, Position hasil commit, kembalikan nama Division dan Position, pulihkan Division `Gudang`, Position `Finance Manager`, status dan email Login User Pre-setup, hapus draft, hasil commit terakhir); permintaan hapus Division, ubah nama Position, nonaktifkan Login User, dan ubah email Login User dengan email baru yang langsung berlaku (tanpa konfirmasi), atas nama Admin kedua Client E, lewat klien HTTP.
- State global: master data Client E dimutasi lalu dipulihkan (R2). Suite Import berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset Client E sesuai D-47 dan mock AI dikembalikan ke normal.

## Test Steps

### TC-GS-IMPORT-322: Baris yang gagal FK saat commit tetap menampilkan opsi AI Reference Suggestion

1. Reset Client E ke tanpa draft Tab User Login (D-47), pastikan Division `Gudang` dan `Engineering` ada dan mock AI mode normal (D-40, D-42), lalu muat ulang halaman Import > User Login
2. Klik [Upload File] di toolbar dan pilih berkas user-login-gudang-engineering.csv
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Verifikasi Staging Table menampilkan 2 baris `pending`
5. Verifikasi Footer menampilkan `[Import (2)]`
6. Ubah Division Name `Gudang` menjadi `Gudang Pusat` lewat sesi API Total Control Client E hingga tersimpan (pemicu, bukan tab UI kedua)
7. Kembali ke tab Import tanpa memuat ulang halaman, klik [Import (2)]
8. Muat ulang halaman Import berkala sampai Footer menampilkan `[Import (0)]` Disabled dengan tooltip "No rows are ready to import."
9. Verifikasi Staging Table berisi 1 baris berstatus `error` dengan Division `Gudang`
10. Verifikasi Staging Metric Cards Total Rows 1
11. Verifikasi Staging Metric Cards Errors 1
12. Verifikasi sel Division pada baris tersebut menampilkan pesan "Division 'Gudang' was not found. Check spelling, or create the missing division from this row."
13. Verifikasi sel Division pada baris tersebut menampilkan badge inline "Did you mean 'Gudang Pusat'?"
14. Verifikasi badge disertai `[Accept]` dan `[Dismiss]`
15. Hapus User Login `citra.wulandari@example.com`, kembalikan nama Division `Gudang Pusat` menjadi `Gudang`, dan hapus draft User Login Client E lewat fixture pembersihan (D-47)

### TC-GS-IMPORT-388: Division dihapus setelah staging, baris User gagal uji ulang FK saat commit tanpa memblokir baris lain

16. Reset Client E ke tanpa draft (D-47), siapkan draft User Login 8 baris D-54 (user-login-commit-8.csv, Division `Gudang` pada baris #5, #6, dan #7) lewat fixture; Division `Gudang` tidak dipakai user maupun Position manapun
17. Muat ulang halaman Import > User Login dan tunggu Staging Table termuat
18. Verifikasi footer menampilkan `[Import (8)]` Enabled
19. Hapus Division `Gudang` Client E lewat sesi API Admin kedua Client E hingga tersimpan
20. Pada halaman yang sama (tanpa memuat ulang) klik [Import (8)]
21. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
22. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 3 errors remain." tampil
23. Verifikasi Staging Table menampilkan 3 baris berstatus `error`: Fajar Hidayat, Gita Savitri, Hendra Gunawan (Division `Gudang`)
24. Verifikasi Error Summary Callout memuat "Division not found"
25. Verifikasi Error Summary Callout menampilkan badge "3 rows"
26. Verifikasi Error Summary Callout menampilkan `[View Data]`, `[Delete All Rows]`, dan `[Create Missing Divisions]`
27. Buka halaman User > User List > Login User
28. Atur Rows per page 100
29. Verifikasi halaman User > User List > Login User Client E memuat 5 user baru: Rizky Pratama, Sinta Maharani, Doni Kurniawan, Eka Putri, Indah Permata
30. Verifikasi user Fajar Hidayat, Gita Savitri, Hendra Gunawan tidak ada

### TC-GS-IMPORT-389: Position di-rename setelah staging, baris menjadi error saat commit

31. Reset Client E ke tanpa draft dan pulihkan master data (D-47), siapkan draft User Login 8 baris D-54 (Position `Finance Manager` pada baris #3) lewat fixture
32. Buka Import > User Login dan tunggu Staging Table termuat
33. Verifikasi footer menampilkan `[Import (8)]` Enabled
34. Ubah nama Position `Finance Manager` menjadi `Finance Head` lewat sesi API Admin kedua Client E hingga tersimpan
35. Pada halaman yang sama (tanpa memuat ulang) klik [Import (8)]
36. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
37. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
38. Verifikasi Staging Table menampilkan 1 baris berstatus `error`: Doni Kurniawan (Position `Finance Manager`)
39. Verifikasi Error Summary Callout memuat "Position not found"
40. Verifikasi Error Summary Callout menampilkan badge "1 row"
41. Verifikasi Error Summary Callout menampilkan `[View Data]`, `[Delete All Rows]`, dan `[Create Missing Positions]`
42. Buka halaman User > User List > Login User
43. Atur Rows per page 100
44. Verifikasi halaman User > User List > Login User Client E memuat 7 user baru
45. Verifikasi user Doni Kurniawan tidak ada

### TC-GS-IMPORT-390: Represented By dinonaktifkan setelah staging, baris User Non Login error saat commit

46. Reset Client E ke tanpa draft dan pulihkan master data (D-47), siapkan draft User Non Login 5 baris D-55 (Represented By `rina.admin.e@example.com` pada baris #1 dan #4) lewat fixture
47. Buka Import > User Non Login dan tunggu Staging Table termuat
48. Verifikasi footer menampilkan `[Import (5)]` Enabled
49. Nonaktifkan Login User `rina.admin.e@example.com` lewat sesi API Admin kedua Client E hingga tersimpan
50. Pada halaman yang sama (tanpa memuat ulang) klik [Import (5)]
51. Muat ulang halaman Import > User Non Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
52. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 2 errors remain." tampil
53. Verifikasi Staging Table menampilkan 2 baris berstatus `error`: Joko Santoso dan Maya Sari (Represented By `rina.admin.e@example.com`)
54. Verifikasi Error Summary Callout memuat "Represented by must be an active User Login account"
55. Verifikasi Error Summary Callout menampilkan badge "2 rows"
56. Buka halaman User > User List > Non-Login User
57. Verifikasi halaman User > User List > Non-Login User Client E memuat 3 user baru: Kartika Dewi, Lukman Hakim, Nanda Wijaya
58. Verifikasi user Joko Santoso dan Maya Sari tidak ada

### TC-GS-IMPORT-391: Represented By di-rename (email berubah) setelah staging, baris error

59. Reset Client E ke tanpa draft dan pulihkan master data (D-47), siapkan draft User Non Login 5 baris D-55 (Represented By `budi.manager.e@example.com` pada baris #2 dan #5) lewat fixture
60. Buka Import > User Non Login dan tunggu Staging Table termuat
61. Verifikasi footer menampilkan `[Import (5)]` Enabled
62. Ubah email Login User `budi.manager.e@example.com` menjadi `budi.manager2.e@example.com` lewat sesi API Admin kedua Client E hingga tersimpan, dengan fixture yang menerapkan email baru langsung
63. Pada halaman yang sama (tanpa memuat ulang) klik [Import (5)]
64. Muat ulang halaman Import > User Non Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
65. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 2 errors remain." tampil
66. Verifikasi Staging Table menampilkan 2 baris berstatus `error`: Kartika Dewi dan Nanda Wijaya (Represented By `budi.manager.e@example.com`)
67. Verifikasi Error Summary Callout memuat "Represented by must be an active User Login account"
68. Verifikasi Error Summary Callout menampilkan badge "2 rows"
69. Buka halaman User > User List > Non-Login User
70. Verifikasi halaman User > User List > Non-Login User Client E memuat 3 user baru: Joko Santoso, Lukman Hakim, Maya Sari
71. Verifikasi user Kartika Dewi dan Nanda Wijaya tidak ada

### TC-GS-IMPORT-751: Division yang hanya ada di draft Tab Division tidak diakui sebagai referensi sah pada Tab User Login sampai di-commit

72. Reset Client E ke tanpa draft (D-47), siapkan draft Division 1 baris dari division-ref-1.csv (Legal/LGL) dan draft User Login 1 baris dari user-login-ref-div-1.csv (Kevin Anggara, Division `Legal`) lewat fixture, lalu buka Import > User Login
73. Verifikasi baris Kevin Anggara berstatus `error`
74. Verifikasi Error Summary Callout memuat "Division not found"
75. Verifikasi Error Summary Callout menampilkan badge "1 row"
76. Klik Sub-Tab Division
77. Klik [Import (1)]
78. Muat ulang halaman Import > Division setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
79. Verifikasi Dropzone tampil di Tab Division
80. Buka halaman User > Division
81. Ketik Search `Legal`, tekan Enter
82. Verifikasi Search `Legal` pada halaman User > Division Client E menampilkan baris bernama persis `Legal`
83. Buka halaman Import > User Login
84. Verifikasi baris Kevin Anggara berstatus `pending`
85. Verifikasi kartu Ready to Import menampilkan 1
86. Verifikasi kartu Errors Disabled (0)

### TC-GS-IMPORT-752: Position yang hanya ada di draft Tab Position tidak diakui sebagai referensi sah pada Tab User Login sampai di-commit

87. Reset Client E ke tanpa draft (D-47), siapkan draft Position 1 baris dari position-ref-1.csv (Sales Executive) dan draft User Login 1 baris dari user-login-ref-pos-1.csv (Kevin Anggara, Division `Engineering`, Position `Sales Executive`) lewat fixture, lalu muat ulang halaman Import > User Login
88. Verifikasi baris Kevin Anggara berstatus `error`
89. Verifikasi Error Summary Callout memuat "Position not found"
90. Verifikasi Error Summary Callout menampilkan badge "1 row"
91. Klik Sub-Tab Position
92. Klik [Import (1)]
93. Muat ulang halaman Import > Position setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
94. Verifikasi Dropzone tampil di Tab Position
95. Buka halaman User > Position
96. Ketik Search `Sales Executive`, tekan Enter
97. Verifikasi Search `Sales Executive` pada halaman User > Position Client E menampilkan baris bernama persis `Sales Executive`
98. Buka halaman Import > User Login
99. Verifikasi baris Kevin Anggara berstatus `pending`
100. Verifikasi kartu Ready to Import menampilkan 1
101. Verifikasi kartu Errors Disabled (0)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (322, 388, 389, 390, 391, 751, 752) dipertahankan; TC-GS-IMPORT-322 pertama karena memakai Division `Gudang` sebelum TC-GS-IMPORT-388 menghapusnya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah pertama tiap blok (reset Client E dan penyiapan draft karena Precondition tiap TC mensyaratkan Client E direset sebelum TC), langkah pemicu Admin kedua, langkah menunggu commit selesai, langkah pindah halaman dan Rows per page 100, serta langkah pemulihan di akhir TC-GS-IMPORT-322.
- P-2: Admin kedua Client E (dan sesi API akun Total Control Client E pada TC-GS-IMPORT-322) hanya memicu perubahan master data lewat sesi API dan bukan objek asersi. TC-GS-IMPORT-322 menyebut tab peramban kedua dengan akun yang sama; ditulis sebagai sesi API karena hanya berfungsi sebagai pemicu (keputusan 2026-10-21).
- Pembagian TC lintas spec: TC-GS-IMPORT-322 berada di section 3j (AI Reference) pada TC sumber, tetapi skenarionya commit dengan late-binding FK pada Client E; dikerjakan di spec ini. Pemicu kelas c (tab kedua) dan kelas d (kontrol worker) tidak dipakai.
- Anchor positif untuk absence: halaman Login User atau Non-Login User memuat daftar user baru (verifikasi nama) sebelum verifikasi user tertentu tidak ada.
- Spec melewati sekitar 35 langkah. Alasan: tujuh blok TC homogen (satu objek uji, late-binding saat commit di Client E) yang berdiri sendiri dan masing-masing mereset Client E; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan langkah prefix berulang (upload, tunggu commit, pindah halaman) mendominasi jumlah langkah.
- Pola halaman basi (late-binding saat commit, TC-GS-IMPORT-388..391): halaman Import dimuat dan Staging Table dibaca sebelum pemicu, lalu `[Import (N)]` diklik pada halaman yang sama tanpa dimuat ulang, dengan N dari sebelum pemicu. Referensi, duplikat, dan opsi dievaluasi ulang saat commit selain saat pembacaan Staging Table (PRD `import.md` baris 994, 1164, 1195). `Verifikasi` footer `[Import (N)]` sebelum pemicu adalah `Verifikasi` tambahan di luar Expected TC yang membuktikan draft sudah dibaca pada halaman itu.
- Muat ulang sesudah reset fixture: langkah 1, 17, dan 87 memakai "Muat ulang halaman Import > User Login" karena reset membuang atau mengganti draft sementara halaman Import yang sama masih terbuka dari langkah atau hook sebelumnya (`suite.md`); halaman dimuat segar sebelum pemicu Admin kedua dan tidak dimuat ulang sesudahnya (TC-GS-IMPORT-388 sampai 391).
- Temuan untuk QA:
  - TC-GS-IMPORT-322: berada di section 3j (AI Reference) padahal skenarionya commit dengan late-binding FK pada Client E; sebaiknya dipindah ke section late-binding (3m). Expected b menyatakan Total Rows 1 dan Errors 1 sementara baris kedua (Citra Wulandari) sudah terkomit; spec mengikuti TC.
  - TC-GS-IMPORT-322: Post Condition a (User Login `citra.wulandari@example.com` tersimpan dan draft berisi 1 baris `error`) tidak punya langkah observasi di TC; tidak diasersi.
  - TC-GS-IMPORT-388, 389, 390, 391: Post Condition (kondisi master data: Division `Gudang` tidak ada, Position `Finance Head` ada, Login User `rina.admin.e` berstatus Inactive, email berubah) tidak punya langkah observasi di TC dan tidak diasersi; sisanya teramati lewat Expected.
  - TC-GS-IMPORT-391: fixture ubah email diasumsikan menerapkan email baru langsung (tanpa konfirmasi email); TC tidak menyebut mekanisme perubahan email yang diizinkan PRD User.
  - TC-GS-IMPORT-751 dan 752: Post Condition hanya teramati lewat Expected; tidak ada observasi tambahan.
  - Kontrol worker commit tidak disebut TC; commit diselesaikan dengan memuat ulang halaman setiap 5 detik sampai batas 2 menit.
  - Data Dinamis commit (nama user D-54, D-55, `Legal`, `Sales Executive`) literal tanpa suffix per run karena asersi bergantung pada nama; pengecualian S-12 untuk data ini belum dinyatakan di konvensi, dipertahankan dengan reset D-47 dan suite serial.
