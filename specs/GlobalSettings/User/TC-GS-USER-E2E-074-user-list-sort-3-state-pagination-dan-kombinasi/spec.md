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
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan Custom Field aktif No. 24, hanya dibaca): `Dewi Lestari` (Active), `Budi Hartono` dan `Jane Smith` (Inactive), `John Doe` (Activated, TAG `TAG-4F7K2XQ9`), `Rina Putri` (Activated), `Mike Tan` (Pending Activation), `Ahmad Fauzi`, `Lilis Handayani` (tanpa Position dan Employee ID), serta user Pre-setup lain di tabel Login User. Tabel Login User memuat sedikitnya 21 baris (Pre-setup ditambah A, B, C) untuk TC-GS-USER-458. Last Update baris `Dewi Lestari` dan `Ahmad Fauzi` lebih lama dari hari uji (kondisi disediakan tim FE; spec tidak mengubah Pre-setup).
- Data Dinamis, di-seed lewat API di hook `before`. Kemampuan seeding user lewat API disediakan tim FE/BE (endpoint tidak disebut di TC dan PRD). Field wajib yang bukan objek uji: Access sesuai tabel, Division sesuai tabel, dan Custom Field `Emergency Phone` (Required, Tabel Pre-setup No. 24) dengan Country Code `🇮🇩 +62` dan Number `81234567890`.
  - A (dibuat lewat sesi API Total Control, sehingga Modified By `Siti N`): First Name `anton`, Last Name `Wibisono {runId}-074`, Email `wibisono+{runId}-074@qwertysystem.net`, Division `Finance`, Position `Supervisor`, Employee ID `EMP-0743-{runId}`, Access `Fixed Asset` dan `Supply Asset`, Temporary User dengan Temporary Until hari uji + 20 hari. Status awal `Pending Activation`.
  - B (dibuat lewat sesi API admin kedua, sehingga Modified By berbeda): Name `Bunga Citra {runId}-074`, Email `adit+{runId}-074@qwertysystem.net`, Division `Logistics`, Position `Internal Auditor`, Employee ID `EMP-0741-{runId}`, Access `Fixed Asset`, bukan Temporary User.
  - C (dibuat lewat sesi API Total Control): First Name `citra`, Last Name `Dewanti {runId}-074`, Email `mulia+{runId}-074@qwertysystem.net`, Division `Legal`, tanpa Position dan Employee ID, Access `Fixed Asset`, `Supply Asset`, dan `Global Settings`, Temporary User dengan Temporary Until hari uji + 40 hari.
  - Seeding minimal (S-11): tiga user dengan awal Name huruf kecil dan besar bercampur, nilai berbeda pada kolom yang di-sort, dan satu nilai kosong (`—`) pada Position, Employee ID, serta TAG; baris Pre-setup (`John Doe`, `Rina Putri`, `Mike Tan`, `Dewi Lestari`, `Budi Hartono`, `Jane Smith`, `Ahmad Fauzi`, `Lilis Handayani`) hanya pembanding untuk kolom Activation Status, TAG, Active, dan Last Update.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus A, B, dan C lewat API.
- Date Format General Settings client tidak diubah; Temporary Until dihitung dari hari uji pada zona waktu client.
- State yang diubah dan dipulihkan: ukuran halaman 100 (langkah 1) dikembalikan ke 10 (langkah 137); kolom `Activation Status`, `TAG`, `Temporary Until` ditampilkan lewat Overlay Column Visibility (langkah 2 sampai 6), kolom `Temporary User` dan `Emergency Phone` lewat Setup Column `[Save]`; seluruhnya dikembalikan ke default lewat `[Reset to Default]` dan `[Save]` (langkah 133 sampai 136); sort dikembalikan ke default di akhir tiap blok TC; Search ditutup dan Filter dikosongkan di langkah 120. Hook `after` sebagai cadangan mengembalikan konfigurasi kolom ke default (mekanisme penghapusan preferensi kolom User List di browser disediakan tim FE/BE).
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

### TC-GS-USER-435: Sort 3-state kolom kelas teks A-Z

15. Klik header Name
16. Verifikasi kolom Name, klik 1: A-Z case-insensitive: baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`
17. Klik header Name
18. Verifikasi kolom Name, klik 2: Z-A: baris `citra Dewanti {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `anton Wibisono {runId}-074`
19. Klik header Name
20. Verifikasi kolom Name, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
21. Klik header Email
22. Verifikasi kolom Email, klik 1: A-Z case-insensitive: baris `Bunga Citra {runId}-074` (`adit+...`) di atas `citra Dewanti {runId}-074` (`mulia+...`), `citra Dewanti {runId}-074` di atas `anton Wibisono {runId}-074` (`wibisono+...`)
23. Klik header Email
24. Verifikasi kolom Email, klik 2: Z-A: baris `anton Wibisono {runId}-074` di atas `citra Dewanti {runId}-074`, `citra Dewanti {runId}-074` di atas `Bunga Citra {runId}-074`
25. Klik header Email
26. Verifikasi kolom Email, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
27. Klik header Division
28. Verifikasi kolom Division, klik 1: A-Z case-insensitive: baris `anton Wibisono {runId}-074` (Finance) di atas `citra Dewanti {runId}-074` (Legal), `citra Dewanti {runId}-074` di atas `Bunga Citra {runId}-074` (Logistics)
29. Klik header Division
30. Verifikasi kolom Division, klik 2: Z-A: baris `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`, `citra Dewanti {runId}-074` di atas `anton Wibisono {runId}-074`
31. Klik header Division
32. Verifikasi kolom Division, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
33. Klik header Modified By
34. Verifikasi kolom Modified By, klik 1: A-Z case-insensitive: nilai sel Modified By pada baris `anton Wibisono {runId}-074`, `Bunga Citra {runId}-074`, dan `citra Dewanti {runId}-074` terurut menaik
35. Klik header Modified By
36. Verifikasi kolom Modified By, klik 2: Z-A: nilai sel Modified By pada baris `anton Wibisono {runId}-074`, `Bunga Citra {runId}-074`, dan `citra Dewanti {runId}-074` terurut menurun
37. Klik header Modified By
38. Verifikasi kolom Modified By, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
39. Klik header Activation Status
40. Verifikasi kolom Activation Status, klik 1: A-Z case-insensitive: baris `John Doe` dan `Rina Putri` (Activated) berada di atas baris `Mike Tan` dan baris `anton Wibisono {runId}-074` (Pending Activation)
41. Klik header Activation Status
42. Verifikasi kolom Activation Status, klik 2: Z-A: baris `Mike Tan` dan baris `anton Wibisono {runId}-074` (Pending Activation) berada di atas baris `John Doe` dan `Rina Putri` (Activated)
43. Klik header Activation Status
44. Verifikasi kolom Activation Status, klik 3: urutan kembali ke default sort tabel Name A-Z: baris `anton Wibisono {runId}-074` di atas `John Doe`, `John Doe` di atas `Mike Tan`, `Mike Tan` di atas `Rina Putri`

### TC-GS-USER-436: Sort 3-state kolom kelas teks dengan kosong di akhir

45. Klik header Position
46. Verifikasi kolom Position, klik 1: A-Z: baris `Bunga Citra {runId}-074` (`Internal Auditor`) di atas `anton Wibisono {runId}-074` (`Supervisor`); nilai `—` di akhir: baris `citra Dewanti {runId}-074` dan baris `Lilis Handayani` berada di bawah baris `anton Wibisono {runId}-074` dan `Bunga Citra {runId}-074`
47. Klik header Position
48. Verifikasi kolom Position, klik 2: Z-A: baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`; nilai `—` tetap di akhir: baris `citra Dewanti {runId}-074` dan baris `Lilis Handayani` berada di bawah baris `anton Wibisono {runId}-074` dan `Bunga Citra {runId}-074`
49. Klik header Position
50. Verifikasi kolom Position, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
51. Klik header Employee ID
52. Verifikasi kolom Employee ID, klik 1: A-Z: baris `Bunga Citra {runId}-074` (`EMP-0741-{runId}`) di atas `anton Wibisono {runId}-074` (`EMP-0743-{runId}`); nilai `—` di akhir: baris `citra Dewanti {runId}-074` dan baris `Lilis Handayani` berada di bawah baris `anton Wibisono {runId}-074` dan `Bunga Citra {runId}-074`
53. Klik header Employee ID
54. Verifikasi kolom Employee ID, klik 2: Z-A: baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`; nilai `—` tetap di akhir: baris `citra Dewanti {runId}-074` dan baris `Lilis Handayani` berada di bawah baris `anton Wibisono {runId}-074` dan `Bunga Citra {runId}-074`
55. Klik header Employee ID
56. Verifikasi kolom Employee ID, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)
57. Klik header TAG
58. Verifikasi kolom TAG, klik 1: A-Z: baris `John Doe` (`TAG-4F7K2XQ9`) di atas baris `anton Wibisono {runId}-074`, `Bunga Citra {runId}-074`, dan `citra Dewanti {runId}-074` (nilai `—` di akhir)
59. Klik header TAG
60. Verifikasi kolom TAG, klik 2: Z-A: baris `John Doe` tetap di atas baris `anton Wibisono {runId}-074`, `Bunga Citra {runId}-074`, dan `citra Dewanti {runId}-074` (nilai `—` tetap di akhir)
61. Klik header TAG
62. Verifikasi kolom TAG, klik 3: urutan kembali ke default sort tabel Name A-Z: baris `anton Wibisono {runId}-074` di atas baris `John Doe`

### TC-GS-USER-437: Sort 3-state kolom kelas toggle

63. Klik header Active
64. Verifikasi kolom Active, klik 1: Active First: baris `Dewi Lestari` (Active) di atas `Budi Hartono` (Inactive) dan baris `anton Wibisono {runId}-074` (Active) di atas `Jane Smith` (Inactive)
65. Klik header Active
66. Verifikasi kolom Active, klik 2: Inactive First: baris `Budi Hartono` di atas `Dewi Lestari` dan baris `Jane Smith` di atas `anton Wibisono {runId}-074`
67. Klik header Active
68. Verifikasi kolom Active, klik 3: urutan kembali ke default sort tabel Name A-Z: baris `Budi Hartono` di atas `Dewi Lestari` dan baris `anton Wibisono {runId}-074` di atas `Jane Smith`

### TC-GS-USER-438: Sort 3-state kolom kelas chip +N more

69. Klik header Access
70. Verifikasi kolom Access, klik 1: paling sedikit produk dulu: baris `Bunga Citra {runId}-074` (1 produk) di atas `anton Wibisono {runId}-074` (2 produk), `anton Wibisono {runId}-074` di atas `citra Dewanti {runId}-074` (3 produk)
71. Klik header Access
72. Verifikasi kolom Access, klik 2: paling banyak produk dulu: baris `citra Dewanti {runId}-074` di atas `anton Wibisono {runId}-074`, `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`
73. Klik header Access
74. Verifikasi kolom Access, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)

### TC-GS-USER-439: Sort 3-state kolom kelas tanggal

75. Klik header Last Update
76. Verifikasi kolom Last Update, klik 1: Oldest First: baris `Dewi Lestari` di atas `anton Wibisono {runId}-074` dan baris `Ahmad Fauzi` di atas `Bunga Citra {runId}-074`
77. Klik header Last Update
78. Verifikasi kolom Last Update, klik 2: Newest First: baris `anton Wibisono {runId}-074` di atas `Dewi Lestari` dan baris `Bunga Citra {runId}-074` di atas `Ahmad Fauzi`
79. Klik header Last Update
80. Verifikasi kolom Last Update, klik 3: urutan kembali ke default sort tabel Name A-Z: baris `anton Wibisono {runId}-074` di atas `Dewi Lestari` dan baris `Ahmad Fauzi` di atas `Bunga Citra {runId}-074`
81. Klik header Temporary Until
82. Verifikasi kolom Temporary Until, klik 1: Oldest First: baris `anton Wibisono {runId}-074` (hari uji + 20 hari) di atas `citra Dewanti {runId}-074` (hari uji + 40 hari); nilai kosong di akhir: baris `Bunga Citra {runId}-074` di bawah baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074`
83. Klik header Temporary Until
84. Verifikasi kolom Temporary Until, klik 2: Newest First: baris `citra Dewanti {runId}-074` di atas baris `anton Wibisono {runId}-074`
85. Klik header Temporary Until
86. Verifikasi kolom Temporary Until, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)

### TC-GS-USER-440: Sort 3-state kolom kelas Yes/No

87. Klik header Temporary User
88. Verifikasi kolom Temporary User, klik 1: Yes First: baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074` (Yes) di atas baris `Bunga Citra {runId}-074` (No)
89. Klik header Temporary User
90. Verifikasi kolom Temporary User, klik 2: No First: baris `Bunga Citra {runId}-074` (No) di atas baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074` (Yes)
91. Klik header Temporary User
92. Verifikasi kolom Temporary User, klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)

### TC-GS-USER-1068: Sort kolom Temporary User mengikuti siklus 3-tahap

93. Klik header Temporary User
94. Verifikasi klik 1: baris `Yes` di atas (`Yes First`): baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074` di atas baris `Bunga Citra {runId}-074`
95. Klik header Temporary User
96. Verifikasi klik 2: baris `No` di atas (`No First`): baris `Bunga Citra {runId}-074` di atas baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074`
97. Klik header Temporary User
98. Verifikasi klik 3: indikator sort pada header Temporary User hilang
99. Verifikasi klik 3: urutan kembali ke default sort tabel Name A-Z (baris `anton Wibisono {runId}-074` di atas `Bunga Citra {runId}-074`, `Bunga Citra {runId}-074` di atas `citra Dewanti {runId}-074`)

### TC-GS-USER-458: Pagination ubah page size dan input nomor halaman

100. Pilih 25 baris per halaman pada Pagination
101. Verifikasi halaman 1 menampilkan lebih dari 10 baris dan paling banyak 25 baris
102. Pilih 10 baris per halaman pada Pagination
103. Ketik `2` pada input nomor halaman, tekan Enter
104. Verifikasi tabel langsung berpindah ke halaman 2
105. Klik tombol next pada Pagination
106. Verifikasi tabel berpindah ke halaman 3
107. Klik tombol prev pada Pagination
108. Verifikasi tabel berpindah ke halaman 2

### TC-GS-USER-459: Kombinasi Search + Filter + Sort + Pagination berjalan bersamaan

109. Klik icon Search, ketik `{runId}-074`, tekan Enter
110. Klik icon Filter
111. Pilih opsi `Yes` pada Temporary User
112. Klik `[Apply]`
113. Klik header Name
114. Klik header Name
115. Pilih 25 baris per halaman pada Pagination
116. Verifikasi keyword Search tetap `{runId}-074`
117. Verifikasi Filter tetap aktif: baris `anton Wibisono {runId}-074` dan `citra Dewanti {runId}-074` (Temporary User `Yes`) tampil dan baris `Bunga Citra {runId}-074` (`No`) tidak tampil
118. Verifikasi Sort Name Z-A tetap berlaku: baris `citra Dewanti {runId}-074` di atas baris `anton Wibisono {runId}-074`
119. Verifikasi ukuran halaman 25 berlaku pada Pagination
120. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
121. Klik icon Filter
122. Klik `[Clear Field]`
123. Klik `[Apply]`
124. Klik header Name
125. Pilih 10 baris per halaman pada Pagination

### TC-GS-USER-1078: Kolom curated Custom Field Phone menampilkan nilai [+CountryCode] [Number]

126. Klik header kolom Column Visibility (⋯)
127. Klik `Setup Column...`
128. Centang `Emergency Phone`
129. Klik `[Save]`
130. Verifikasi kolom `Emergency Phone` tampil di tabel
131. Verifikasi baris `anton Wibisono {runId}-074`: sel Emergency Phone `+62 81234567890` (satu spasi)
132. Verifikasi sel Emergency Phone baris `anton Wibisono {runId}-074` tidak tampil tanpa spasi (`+6281234567890`)

### Pemulihan state

133. Klik header kolom Column Visibility (⋯)
134. Klik `Setup Column...`
135. Klik `[Reset to Default]`
136. Klik `[Save]`
137. Pilih 10 baris per halaman pada Pagination

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 1061 (menampilkan kolom `Temporary User`), 435, 436, 437, 438, 439, 440, 1068, 458, 459, lalu 1078. Urutan di `tc-user.md`: 435 sampai 440, 1068, 458, 459, 1061, 1078. TC-GS-USER-1061 dipindah ke awal karena TC-GS-USER-440 dan 1068 mengurutkan kolom `Temporary User` yang hidden secara default (TC-GS-USER-1068 menyatakan 1061 sebagai Dependensi); kolom `Activation Status`, `TAG`, dan `Temporary Until` yang hidden secara default ditampilkan lewat Overlay Column Visibility di langkah 2 sampai 6.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 agar baris seed dan Pre-setup berada di halaman yang sama), langkah 2 sampai 6, serta langkah 120 sampai 125 (menutup Search, mengosongkan Filter, mengembalikan sort Name ke default dengan satu klik header Name sesudah dua klik, dan mengembalikan ukuran halaman) serta langkah 133 sampai 137 (memulihkan konfigurasi kolom dan ukuran halaman). TC-GS-USER-458 memilih ukuran 25 lalu mengembalikan ke 10 sesuai langkah TC.
- Pasangan baris pembanding: urutan A-Z dan Z-A diasersi pada pasangan atau kelompok baris seed (A, B, C) dan baris Pre-setup yang urutannya berbeda dari default sort Name A-Z dan dari arah sort lainnya, sehingga klik 1, klik 2, dan klik 3 membedakan tiga keadaan (pengecualian: Name klik 1 dan klik 3 menghasilkan urutan yang sama karena default sort tabel adalah Name A-Z; dibedakan oleh nomor langkah klik).
- Asersi tambahan (S-03): tidak ada `Verifikasi` di luar Expected TC; langkah baca nilai tidak dipakai. TC-GS-USER-1078 dan 1061 memakai user seed A dan B, bukan Dewi Lestari dan Budi Hartono (lihat Temuan untuk QA).
- Spec melewati sekitar 35 langkah karena sebelas TC Sort, Pagination, dan kombinasi berbagi satu layar, satu dataset (A, B, C dan Pre-setup), dan satu kelas harness (fungsional, baca saja). Tiap kolom dalam TC-GS-USER-435 sampai 440 mengulang pola identik (tiga klik, tiga `Verifikasi`) dan berdiri sendiri: kegagalan satu kolom tidak membuat kolom lain kehilangan makna. Memisahkannya mengulang login, seeding, dan pembukaan layar yang sama.
- Pembagian TC lintas spec: Search di spec 071; Filter Panel di spec 072; kombinasi Search dan Filter tanpa Sort di spec 073; Setup Column di spec 075; nilai Phone pada file Download di spec 076 (TC-GS-USER-1079).
- Temuan untuk QA:
  - TC-GS-USER-1061 dan 1068: Pre-setup No. 12 menyebut `Dewi Lestari` Temporary aktif (+30 hari) dan No. 16 menyebut `Budi Hartono` Temporary-expired, sedangkan TC-GS-USER-1061 menyatakan Budi Hartono Temporary User dan Dewi Lestari bukan. Spec memakai user seed A (Temporary, `Yes`) dan B (bukan Temporary, `No`).
  - TC-GS-USER-1078: Pre-setup No. 12 menyebut Emergency Phone `Dewi Lestari` kosong, sedangkan TC menyebut tersimpan `+62 81234567890`. Spec memakai user seed A dengan nilai itu.
  - TC-GS-USER-1061 dan 1078: TC menyebut header kolom `Actions (⋯)` dan menu `[Setup Column]`; TC-GS-USER-441 dan 442 menyebut `Setup Column...` di Overlay. Spec memakai header `Column Visibility (⋯)` dan item `Setup Column...`.
  - TC-GS-USER-436 (TAG): hanya satu nilai TAG non-kosong (`John Doe`) yang dapat di-seed tanpa mekanisme pairing; urutan A-Z dan Z-A antar nilai TAG tidak teramati, hanya nilai `—` di akhir.
  - TC-GS-USER-439 (Temporary Until): kurung "(kosong di akhir untuk Temporary Until)" hanya ditulis pada klik 1; spec mengasersi nilai kosong di akhir hanya pada klik 1.
  - TC-GS-USER-435 (Modified By): nama admin kedua tidak ditetapkan di TC; spec mengasersi urutan menaik dan menurun menurut nilai sel yang terbaca.
  - TC-GS-USER-439 (Last Update): bergantung pada Last Update baris Pre-setup (`Dewi Lestari`, `Ahmad Fauzi`) lebih lama dari hari uji; TC tidak menyebut kondisinya. Disediakan tim FE.
  - TC-GS-USER-459: "Terapkan filter bila tersedia" bersyarat; spec menerapkan Filter Temporary User `Yes` karena Filter Panel tersedia.
  - TC-GS-USER-436 dan 439: contoh nilai kosong `—` untuk Position dan Employee ID memakai baris `Lilis Handayani` (Pre-setup No. 20).
