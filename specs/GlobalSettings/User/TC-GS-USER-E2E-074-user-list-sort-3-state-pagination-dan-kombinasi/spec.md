---
id: TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi
title: "User List: Sort 3-State per Kelas Kolom, Pagination, Kombinasi Search+Filter+Sort+Pagination, Badge Temporary User, dan Nilai Phone"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-435
  - TC-GS-USER-436
  - TC-GS-USER-437
  - TC-GS-USER-438
  - TC-GS-USER-439
  - TC-GS-USER-440
  - TC-GS-USER-1068
  - TC-GS-USER-458
  - TC-GS-USER-459
  - TC-GS-USER-1061
  - TC-GS-USER-1078
coverage:
  web: automated
---

# User List: Sort 3-State per Kelas Kolom, Pagination, Kombinasi Search+Filter+Sort+Pagination, Badge Temporary User, dan Nilai Phone

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD` (admin kedua; hanya sesi API untuk membuat B agar Modified By berbeda dari A dan C). Keduanya didaftarkan di `executionConfig.environmentVariables`.
- Admin kedua: akun Total Control kedua yang disediakan tim FE (tidak ada di Tabel Pre-setup TC). Sesi UI kedua tidak dipakai.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan Custom Field aktif No. 24, hanya dibaca): user Pre-setup di tabel Login User dan Custom Field `Emergency Phone` (No. 24). Blok sort TC-GS-USER-435 sampai 440 dan 1068 tidak memakai baris Pre-setup sebagai pembanding: tabel dibatasi Search `{runId}-074` sehingga hanya baris seed spec ini (A sampai E) yang tampil. Tabel Login User memuat sedikitnya 21 baris (Pre-setup ditambah A sampai E) untuk TC-GS-USER-458, yang dijalankan setelah Search ditutup.
- Data Dinamis, di-seed lewat API di hook `before`. Kemampuan seeding user lewat API disediakan tim FE/BE (endpoint tidak disebut di TC dan PRD). Field wajib yang bukan objek uji: Access sesuai tabel, Division sesuai tabel, dan Custom Field `Emergency Phone` (Required, Tabel Pre-setup No. 24) dengan Country Code `🇮🇩 +62` dan Number `81234567890`.
  - A (dibuat lewat sesi API Total Control, sehingga Modified By `Siti N`): First Name `anton`, Last Name `Wibisono {runId}-074`, Email `wibisono+{runId}-074@qwertysystem.net`, Division `Finance`, Position `Supervisor`, Employee ID `EMP-0743-{runId}`, Access `Fixed Asset` dan `Supply Asset`, Temporary User dengan Temporary Until hari uji + 20 hari. Status awal `Pending Activation`.
  - B (dibuat lewat sesi API admin kedua, sehingga Modified By berbeda): Name `Bunga Citra {runId}-074`, Email `adit+{runId}-074@qwertysystem.net`, Division `Logistics`, Position `Internal Auditor`, Employee ID `EMP-0741-{runId}`, Access `Fixed Asset`, bukan Temporary User.
  - C (dibuat lewat sesi API Total Control): First Name `citra`, Last Name `Dewanti {runId}-074`, Email `mulia+{runId}-074@qwertysystem.net`, Division `Finance`, tanpa Position dan Employee ID, Access `Fixed Asset`, `Supply Asset`, dan `Global Settings`, Temporary User dengan Temporary Until hari uji + 40 hari.
  - D (dibuat lewat sesi API Total Control, pertama): First Name `Dian`, Last Name `Kusuma {runId}-074`, Email `diankusuma+{runId}-074@qwertysystem.net`, Division `Finance`, tanpa Position dan Employee ID, Access `Fixed Asset`, bukan Temporary User, Activated lalu dinonaktifkan (Inactive); tanpa TAG. Pembanding kolom Active, Activation Status, Position, Employee ID, dan Last Update (paling lama).
  - E (dibuat lewat sesi API Total Control, sesudah penantian hook dan bersama A dalam satu kelompok seeding): First Name `Fajar`, Last Name `Nugroho {runId}-074`, Email `fajarnugroho+{runId}-074@qwertysystem.net`, Division `Finance`, Access `Fixed Asset`, bukan Temporary User, Activated dan Active, dengan TAG terpasang lewat seeding (satu-satunya nilai TAG non-kosong). Pembanding kolom Activation Status, TAG, Active, dan Last Update.
  - Urutan seeding: D lebih dahulu, lalu satu penantian hook (maksimum 60 detik; nilai ini pilihan spec, bukan nilai TC, agar Last Update D berbeda pada sel yang terbaca; mekanisme disediakan tim FE/BE), lalu kelompok E dan A. Last Update D lebih lama daripada E dan A (TC-GS-USER-439); urutan E terhadap A tidak diasersi.
  - Seeding minimal (S-11): lima user dengan awal Name huruf kecil dan besar bercampur, nilai berbeda pada kolom yang di-sort, dan nilai kosong (`—`) pada Position, Employee ID, serta TAG. Baris Pre-setup tidak dipakai sebagai pembanding sort.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus A, B, C, D, dan E lewat API.
- Date Format General Settings client tidak diubah; Temporary Until dihitung dari hari uji pada zona waktu client.
- State yang diubah dan dipulihkan: ukuran halaman 100 (langkah 1) dikembalikan ke 10 (langkah 148); kolom `Activation Status`, `TAG`, `Temporary Until` ditampilkan lewat Overlay Column Visibility (langkah 2 sampai 6), kolom `Temporary User` dan `Emergency Phone` lewat Setup Column `[Save]`; seluruhnya dikembalikan ke default lewat `[Reset to Default]` dan `[Save]` (langkah 144 sampai 147); sort dikembalikan ke default di akhir tiap blok TC; Search ditutup dan Filter dikosongkan di langkah 129, dan Search yang dibuka lagi di langkah 140 ditutup di langkah 143. Hook `after` sebagai cadangan mengembalikan konfigurasi kolom ke default (mekanisme penghapusan preferensi kolom User List di browser disediakan tim FE/BE).
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: membaca urutan baris tabel dan indikator sort pada header kolom; membaca nilai sel kolom Access (+N more), Modified By, dan Emergency Phone; mengetik nomor halaman pada input Pagination.

## Test Steps

### Persiapan tampilan

1. Pilih 100 baris per halaman pada Pagination
2. Klik header kolom Column Visibility (⋯)
3. Centang `Activation Status`
4. Centang `TAG`
5. Centang `Temporary Until`
6. Tekan Esc untuk menutup Overlay Column Visibility

### TC-GS-USER-1061: Kolom curated Temporary User menampilkan badge Yes/No

7. Klik header kolom Column Visibility (⋯)
8. Klik `Setup Column...`
9. Centang `Temporary User`
10. Klik `[Save]`
11. Verifikasi kolom `Temporary User` tampil di tabel
12. Verifikasi baris `anton Wibisono {runId}-074`: badge `Yes`
13. Verifikasi baris `Bunga Citra {runId}-074`: badge `No`
14. Verifikasi sel Temporary User baris `anton Wibisono {runId}-074` dan baris `Bunga Citra {runId}-074` tidak kosong dan bukan `—`

### Persiapan sort: batasi tabel ke baris seed spec ini

15. Klik icon Search, ketik `{runId}-074`, tekan Enter

### TC-GS-USER-435: Sort 3-state kolom kelas teks A-Z

16. Klik header Name
17. Verifikasi kolom Name, klik 1: A-Z case-insensitive: baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`
18. Klik header Name
19. Verifikasi kolom Name, klik 2: Z-A: baris `citra Dewanti {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `anton Wibisono {runId}-074`
20. Klik header Name
21. Verifikasi kolom Name, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
22. Klik header Email
23. Verifikasi kolom Email, klik 1: A-Z case-insensitive: baris `Bunga Citra {runId}-074` (`adit+...`) di atas `citra Dewanti {runId}-074` (`mulia+...`), `citra Dewanti {runId}-074` di atas `anton Wibisono {runId}-074` (`wibisono+...`)
24. Klik header Email
25. Verifikasi kolom Email, klik 2: Z-A: baris `anton Wibisono {runId}-074` di atas `citra Dewanti {runId}-074`, `citra Dewanti {runId}-074` di atas `Bunga Citra {runId}-074`
26. Klik header Email
27. Verifikasi kolom Email, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
28. Klik header Division
29. Verifikasi kolom Division, klik 1: A-Z case-insensitive: baris `anton Wibisono {runId}-074` (Finance) dan baris `citra Dewanti {runId}-074` (Finance) di atas baris `Bunga Citra {runId}-074` (Logistics)
30. Klik header Division
31. Verifikasi kolom Division, klik 2: Z-A: baris `Bunga Citra {runId}-074` (Logistics) di atas baris `anton Wibisono {runId}-074` dan baris `citra Dewanti {runId}-074` (Finance)
32. Klik header Division
33. Verifikasi kolom Division, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
34. Klik header Modified By
35. Verifikasi kolom Modified By, klik 1: A-Z case-insensitive: nilai sel Modified By pada baris `anton Wibisono {runId}-074`, `Bunga Citra {runId}-074`, dan `citra Dewanti {runId}-074` terurut menaik
36. Klik header Modified By
37. Verifikasi kolom Modified By, klik 2: Z-A: nilai sel Modified By pada baris `anton Wibisono {runId}-074`, `Bunga Citra {runId}-074`, dan `citra Dewanti {runId}-074` terurut menurun
38. Klik header Modified By
39. Verifikasi kolom Modified By, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
40. Klik header Activation Status
41. Verifikasi kolom Activation Status, klik 1: A-Z case-insensitive: baris `Fajar Nugroho {runId}-074` (Activated) berada di atas baris `anton Wibisono {runId}-074` (Pending Activation)
42. Klik header Activation Status
43. Verifikasi kolom Activation Status, klik 2: Z-A: baris `anton Wibisono {runId}-074` (Pending Activation) berada di atas baris `Fajar Nugroho {runId}-074` (Activated)
44. Klik header Activation Status
45. Verifikasi kolom Activation Status, klik 3: urutan kembali ke default sort tabel Name A-Z: baris `anton Wibisono {runId}-074` di atas `Dian Kusuma {runId}-074`, `Dian Kusuma {runId}-074` di atas `Fajar Nugroho {runId}-074`

### TC-GS-USER-436: Sort 3-state kolom kelas teks dengan kosong di akhir

46. Klik header Position
47. Verifikasi kolom Position, klik 1: A-Z: baris `Bunga Citra {runId}-074` (`Internal Auditor`) di atas baris `anton Wibisono {runId}-074` (`Supervisor`)
48. Verifikasi kolom Position, klik 1: nilai `—` di akhir: baris `citra Dewanti {runId}-074` dan baris `Dian Kusuma {runId}-074` berada di bawah baris `anton Wibisono {runId}-074` dan `Bunga Citra {runId}-074`
49. Klik header Position
50. Verifikasi kolom Position, klik 2: Z-A: baris `anton Wibisono {runId}-074` (`Supervisor`) di atas baris `Bunga Citra {runId}-074` (`Internal Auditor`)
51. Verifikasi kolom Position, klik 2: nilai `—` di awal: baris `citra Dewanti {runId}-074` dan baris `Dian Kusuma {runId}-074` berada di atas baris `anton Wibisono {runId}-074` dan `Bunga Citra {runId}-074`
52. Klik header Position
53. Verifikasi kolom Position, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
54. Klik header Employee ID
55. Verifikasi kolom Employee ID, klik 1: A-Z: baris `Bunga Citra {runId}-074` (`EMP-0741-{runId}`) di atas baris `anton Wibisono {runId}-074` (`EMP-0743-{runId}`)
56. Verifikasi kolom Employee ID, klik 1: nilai `—` di akhir: baris `citra Dewanti {runId}-074` dan baris `Dian Kusuma {runId}-074` berada di bawah baris `anton Wibisono {runId}-074` dan `Bunga Citra {runId}-074`
57. Klik header Employee ID
58. Verifikasi kolom Employee ID, klik 2: Z-A: baris `anton Wibisono {runId}-074` (`EMP-0743-{runId}`) di atas baris `Bunga Citra {runId}-074` (`EMP-0741-{runId}`)
59. Verifikasi kolom Employee ID, klik 2: nilai `—` di awal: baris `citra Dewanti {runId}-074` dan baris `Dian Kusuma {runId}-074` berada di atas baris `anton Wibisono {runId}-074` dan `Bunga Citra {runId}-074`
60. Klik header Employee ID
61. Verifikasi kolom Employee ID, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
62. Klik header TAG
63. Verifikasi kolom TAG, klik 1: nilai `—` di akhir: baris `Fajar Nugroho {runId}-074` (ber-TAG) di atas baris `anton Wibisono {runId}-074`, `Bunga Citra {runId}-074`, dan `citra Dewanti {runId}-074`
64. Klik header TAG
65. Verifikasi kolom TAG, klik 2: nilai `—` di awal: baris `anton Wibisono {runId}-074`, `Bunga Citra {runId}-074`, dan `citra Dewanti {runId}-074` berada di atas baris `Fajar Nugroho {runId}-074`
66. Klik header TAG
67. Verifikasi kolom TAG, klik 3: urutan kembali ke default sort tabel Name A-Z: baris `anton Wibisono {runId}-074` di atas baris `Fajar Nugroho {runId}-074`

### TC-GS-USER-437: Sort 3-state kolom kelas toggle

68. Klik header Active
69. Verifikasi kolom Active, klik 1: Active First: baris `Fajar Nugroho {runId}-074` (Active) di atas `Dian Kusuma {runId}-074` (Inactive) dan baris `anton Wibisono {runId}-074` (Active) di atas `Dian Kusuma {runId}-074` (Inactive)
70. Klik header Active
71. Verifikasi kolom Active, klik 2: Inactive First: baris `Dian Kusuma {runId}-074` di atas `Fajar Nugroho {runId}-074` dan baris `Dian Kusuma {runId}-074` di atas `anton Wibisono {runId}-074`
72. Klik header Active
73. Verifikasi kolom Active, klik 3: urutan kembali ke default sort tabel Name A-Z: baris `anton Wibisono {runId}-074` di atas `Dian Kusuma {runId}-074` dan baris `Dian Kusuma {runId}-074` di atas `Fajar Nugroho {runId}-074`

### TC-GS-USER-438: Sort 3-state kolom kelas chip +N more

74. Klik header Access
75. Verifikasi kolom Access, klik 1: paling sedikit produk dulu: baris `Bunga Citra {runId}-074` (1 produk) di atas `anton Wibisono {runId}-074` (2 produk), `anton Wibisono {runId}-074` di atas `citra Dewanti {runId}-074` (3 produk)
76. Klik header Access
77. Verifikasi kolom Access, klik 2: paling banyak produk dulu: baris `citra Dewanti {runId}-074` di atas `anton Wibisono {runId}-074`, `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`
78. Klik header Access
79. Verifikasi kolom Access, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)

### TC-GS-USER-439: Sort 3-state kolom kelas tanggal

80. Klik header Last Update
81. Verifikasi kolom Last Update, klik 1: Oldest First: baris `Dian Kusuma {runId}-074` di atas `Fajar Nugroho {runId}-074` dan baris `Dian Kusuma {runId}-074` di atas `anton Wibisono {runId}-074`
82. Klik header Last Update
83. Verifikasi kolom Last Update, klik 2: Newest First: baris `Fajar Nugroho {runId}-074` di atas `Dian Kusuma {runId}-074` dan baris `anton Wibisono {runId}-074` di atas `Dian Kusuma {runId}-074`
84. Klik header Last Update
85. Verifikasi kolom Last Update, klik 3: urutan kembali ke default sort tabel Name A-Z: baris `anton Wibisono {runId}-074` di atas `Dian Kusuma {runId}-074` dan baris `Dian Kusuma {runId}-074` di atas `Fajar Nugroho {runId}-074`
86. Klik header Temporary Until
87. Verifikasi kolom Temporary Until, klik 1: Oldest First: baris `anton Wibisono {runId}-074` (hari uji + 20 hari) di atas baris `citra Dewanti {runId}-074` (hari uji + 40 hari)
88. Verifikasi kolom Temporary Until, klik 1: nilai kosong di akhir: baris `Bunga Citra {runId}-074` berada di bawah baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074`
89. Klik header Temporary Until
90. Verifikasi kolom Temporary Until, klik 2: Newest First: baris `citra Dewanti {runId}-074` di atas baris `anton Wibisono {runId}-074`
91. Verifikasi kolom Temporary Until, klik 2: nilai kosong di awal: baris `Bunga Citra {runId}-074` berada di atas baris `citra Dewanti {runId}-074` dan `anton Wibisono {runId}-074`
92. Klik header Temporary Until
93. Verifikasi kolom Temporary Until, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)

### TC-GS-USER-440: Sort 3-state kolom kelas Yes/No

94. Klik header Temporary User
95. Verifikasi kolom Temporary User, klik 1: Yes First: baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074` (Yes) di atas baris `Bunga Citra {runId}-074` (No)
96. Klik header Temporary User
97. Verifikasi kolom Temporary User, klik 2: No First: baris `Bunga Citra {runId}-074` (No) di atas baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074` (Yes)
98. Klik header Temporary User
99. Verifikasi kolom Temporary User, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)

### TC-GS-USER-1068: Sort kolom Temporary User mengikuti siklus 3-tahap

100. Klik header Temporary User
101. Verifikasi klik 1: baris `Yes` di atas (`Yes First`): baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074` di atas baris `Bunga Citra {runId}-074`
102. Klik header Temporary User
103. Verifikasi klik 2: baris `No` di atas (`No First`): baris `Bunga Citra {runId}-074` di atas baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074`
104. Klik header Temporary User
105. Verifikasi klik 3: indikator sort pada header Temporary User hilang
106. Verifikasi klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)

### TC-GS-USER-458: Pagination ubah page size dan input nomor halaman

107. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
108. Pilih 25 baris per halaman pada Pagination
109. Verifikasi halaman 1 menampilkan lebih dari 10 baris dan paling banyak 25 baris
110. Pilih 10 baris per halaman pada Pagination
111. Ketik `2` pada input nomor halaman, tekan Enter
112. Verifikasi tabel langsung berpindah ke halaman 2
113. Klik tombol next pada Pagination
114. Verifikasi tabel berpindah ke halaman 3
115. Klik tombol prev pada Pagination
116. Verifikasi tabel berpindah ke halaman 2

### TC-GS-USER-459: Kombinasi Search + Filter + Sort + Pagination berjalan bersamaan

117. Klik icon Search, ketik `{runId}-074`, tekan Enter
118. Klik icon Filter
119. Pilih opsi `Finance` pada Division
120. Klik `[Apply]`
121. Klik header Name
122. Klik header Name
123. Pilih 25 baris per halaman pada Pagination
124. Verifikasi keyword Search tetap `{runId}-074`
125. Verifikasi Filter tetap aktif: baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074` (Division `Finance`) tampil
126. Verifikasi Filter tetap aktif: baris `Bunga Citra {runId}-074` (Division `Logistics`) tidak tampil
127. Verifikasi Sort Name Z-A tetap berlaku: baris `citra Dewanti {runId}-074` di atas baris `anton Wibisono {runId}-074`
128. Verifikasi ukuran halaman 25 berlaku pada Pagination
129. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
130. Klik icon Filter
131. Klik `[Clear Field]`
132. Klik `[Apply]`
133. Klik header Name
134. Pilih 10 baris per halaman pada Pagination

### TC-GS-USER-1078: Kolom curated Custom Field Phone menampilkan nilai [+CountryCode] [Number]

135. Klik header kolom Column Visibility (⋯)
136. Klik `Setup Column...`
137. Centang `Emergency Phone`
138. Klik `[Save]`
139. Verifikasi kolom `Emergency Phone` tampil di tabel
140. Klik icon Search, ketik `anton Wibisono {runId}-074`, tekan Enter
141. Verifikasi baris `anton Wibisono {runId}-074`: sel Emergency Phone `+62 81234567890` (satu spasi)
142. Verifikasi sel Emergency Phone baris `anton Wibisono {runId}-074` tidak tampil tanpa spasi (`+6281234567890`)
143. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### Pemulihan state

144. Klik header kolom Column Visibility (⋯)
145. Klik `Setup Column...`
146. Klik `[Reset to Default]`
147. Klik `[Save]`
148. Pilih 10 baris per halaman pada Pagination

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 1061 (menampilkan kolom `Temporary User`), 435, 436, 437, 438, 439, 440, 1068, 458, 459, lalu 1078. Urutan di `tc-user.md`: 435 sampai 440, 1068, 458, 459, 1061, 1078. TC-GS-USER-1061 dipindah ke awal karena TC-GS-USER-440 dan 1068 mengurutkan kolom `Temporary User` yang hidden secara default (TC-GS-USER-1068 menyatakan 1061 sebagai Dependensi); kolom `Activation Status`, `TAG`, dan `Temporary Until` yang hidden secara default ditampilkan lewat Overlay Column Visibility di langkah 2 sampai 6.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 agar baris seed dan Pre-setup berada di halaman yang sama), langkah 2 sampai 6, langkah 15 (Search `{runId}-074` membatasi tabel ke baris seed A sampai E sebelum blok sort), langkah 107 (menutup Search dan mereset tabel sebelum TC-GS-USER-458 agar Pagination memakai seluruh tabel Login User; Search tertutup berarti kotak kosong saat TC-GS-USER-459 mengetik Search sendiri di langkah 117), langkah 129 sampai 134 (menutup Search, mengosongkan Filter, mengembalikan sort Name ke default dengan satu klik header Name sesudah dua klik, dan mengembalikan ukuran halaman), langkah 140 (Search `anton Wibisono {runId}-074` membatasi tabel ke baris yang dibaca TC-GS-USER-1078 karena Search ditutup di langkah 129 dan tabel Login User lebih dari satu halaman pada page size 10) dan langkah 143 (menutup Search lagi), serta langkah 144 sampai 148 (memulihkan konfigurasi kolom dan ukuran halaman). TC-GS-USER-458 memilih ukuran 25 lalu mengembalikan ke 10 sesuai langkah TC.
- Klausa nilai kosong (`—` di akhir pada klik 1 dan di awal pada klik 2) ditulis satu `Verifikasi` terpisah dari klausa urutan A-Z, Z-A, atau Oldest First, Newest First (S-01; TC-GS-USER-436 dan 439). Pada kolom TAG hanya satu nilai non-kosong yang dapat di-seed, sehingga urutan A-Z dan Z-A antar nilai TAG tidak teramati dan satu `Verifikasi` per klik hanya mengasersi posisi nilai `—`.
- Pasangan baris pembanding: urutan A-Z dan Z-A diasersi pada pasangan atau kelompok baris seed (A sampai E; tabel dibatasi Search `{runId}-074`, tanpa baris Pre-setup) yang urutannya berbeda dari default sort Name A-Z dan dari arah sort lainnya, sehingga klik 1, klik 2, dan klik 3 membedakan tiga keadaan (pengecualian: Name klik 1 dan klik 3 menghasilkan urutan yang sama karena default sort tabel adalah Name A-Z; dibedakan oleh nomor langkah klik).
- Asersi tambahan (S-03): tidak ada `Verifikasi` di luar Expected TC; langkah baca nilai tidak dipakai. TC-GS-USER-1061 memakai user seed A dan B (bukan Budi Hartono dan Joko Susilo) dan TC-GS-USER-1078 memakai user seed A (bukan Dewi Lestari) (lihat Temuan untuk QA).
- Spec melewati sekitar 35 langkah karena sebelas TC Sort, Pagination, dan kombinasi berbagi satu layar, satu dataset (A sampai E; Pre-setup hanya mengisi tabel untuk TC-GS-USER-458), dan satu kelas harness (fungsional, baca saja). Tiap kolom dalam TC-GS-USER-435 sampai 440 mengulang pola identik (tiga klik, tiga `Verifikasi`) dan berdiri sendiri: kegagalan satu kolom tidak membuat kolom lain kehilangan makna. Memisahkannya mengulang login, seeding, dan pembukaan layar yang sama.
- Pembagian TC lintas spec: Search di spec 071; Filter Panel di spec 072; kombinasi Search dan Filter tanpa Sort di spec 073; Setup Column di spec 075; nilai Phone pada file Download di spec 076 (TC-GS-USER-1079).
- Temuan untuk QA:
  - TC-GS-USER-1061 dan 1068: TC-GS-USER-1061 menyebut `Budi Hartono` (Temporary User) dan `Joko Susilo` (bukan Temporary User) sebagai baris uji, sedangkan Pre-setup No. 12 menyebut `Dewi Lestari` Temporary aktif (+30 hari) dan No. 16 menyebut `Budi Hartono` Temporary-expired. Spec memakai user seed A (Temporary, `Yes`) dan B (bukan Temporary, `No`).
  - TC-GS-USER-1078: Pre-setup No. 12 menyebut Emergency Phone `Dewi Lestari` kosong, sedangkan TC menyebut tersimpan `+62 81234567890`. Spec memakai user seed A dengan nilai itu.
  - TC-GS-USER-1061 dan 1078: TC menyebut header kolom `Actions (⋯)` dan menu `[Setup Column]`; TC-GS-USER-441 dan 442 menyebut `Setup Column...` di Overlay. Spec memakai header `Column Visibility (⋯)` dan item `Setup Column...`.
  - TC-GS-USER-436 (TAG): TC memakai `John Doe` (Pre-setup, TAG `TAG-4F7K2XQ9`); spec memakai seed E `Fajar Nugroho {runId}-074` ber-TAG karena tabel dibatasi Search dan baris Pre-setup tidak dipakai. Hanya satu nilai TAG non-kosong yang di-seed; urutan A-Z dan Z-A antar nilai TAG tidak teramati, hanya nilai `—` di akhir.
  - TC-GS-USER-435 (Modified By): nama admin kedua tidak ditetapkan di TC; spec mengasersi urutan menaik dan menurun menurut nilai sel yang terbaca.
  - TC-GS-USER-439 (Last Update): TC bergantung pada Last Update baris Pre-setup (`Dewi Lestari`, `Ahmad Fauzi`) lebih lama dari hari uji dan tidak menyebut kondisinya; spec memakai seed D, lalu satu penantian hook (maksimum 60 detik, pilihan spec), lalu kelompok E dan A, karena baris Pre-setup tidak tampil di tabel yang dibatasi Search. Hanya pasangan D terhadap A dan D terhadap E yang diasersi (langkah 81 dan 83); urutan E terhadap A tidak diasersi. Pertanyaan QA/FE: apakah resolusi sel Last Update cukup halus untuk membedakan D dari E dan A setelah penantian itu, atau perlu penyetelan waktu seed?
  - TC-GS-USER-435 (Activation Status), 436 (TAG), 437 (Active): TC menyebut baris Pre-setup (`John Doe`, `Rina Putri`, `Mike Tan`, `Lilis Handayani`); spec memakai seed D `Dian Kusuma {runId}-074` (Inactive) dan E `Fajar Nugroho {runId}-074` (Activated, ber-TAG) sebagai pembanding. Mekanisme seeding user ber-TAG dan Inactive dengan status Activated disediakan tim FE/BE; nilai kode TAG E tidak diasersi.
  - TC-GS-USER-459: filter pada Division (1 opsi) tanpa nilai; spec memakai `Finance`, dan user seed A, C, D, dan E ber-Division `Finance` supaya baris seed A dan C lolos filter bersama D dan E dan urutan Sort Name Z-A teramati; baris B (`Logistics`) menjadi pembanding yang tersaring.
  - TC-GS-USER-458: Data Uji menyebut tabel berisi 25 baris (fixture BE, Pre-setup No. 29); spec memakai tabel Login User yang memuat sedikitnya 21 baris (Pre-setup ditambah A sampai E) dan mengasersi lebih dari 10 dan paling banyak 25 baris pada page size 25.
  - TC-GS-USER-436 dan 439: contoh nilai kosong `—` untuk Position dan Employee ID memakai seed D `Dian Kusuma {runId}-074` (tanpa Position dan Employee ID) sebagai pengganti `Lilis Handayani` (Pre-setup No. 20), selain seed C.
