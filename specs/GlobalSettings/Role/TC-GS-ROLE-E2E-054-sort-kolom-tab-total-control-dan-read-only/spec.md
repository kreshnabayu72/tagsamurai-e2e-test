---
id: TC-GS-ROLE-E2E-054-sort-kolom-tab-total-control-dan-read-only
title: "Sort Kolom Tab Total Control dan Tab Read Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-152
  - TC-GS-ROLE-153
  - TC-GS-ROLE-154
  - TC-GS-ROLE-155
  - TC-GS-ROLE-156
coverage:
  web: automated
---

# Sort Kolom Tab Total Control dan Tab Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login di hook `before`): Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD` (sudah terdaftar). Tidak ada env baru.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control (Search, Filter, Sort, dan kolom tabel dalam keadaan bawaan; sort bawaan Name A-Z).
- Data Pre-setup yang dipakai (Tabel Data Uji Pre-setup; hanya dibaca): Tab Total Control berisi Ahmad Fauzi (IT Manager, IT, Active, punya TAG `TG-00451`), Budi Santoso (Default User, Active; Position, Division, Modified By, dan Last Updated `—`), Dewi Lestari (Staff, Finance, Inactive), dan Bayu Nugraha (baris 19, Temporary User `Yes`, Temporary Until terisi). Tab Read Only berisi Siti Nurhaliza (Finance Staff, Finance, Active, Last Updated 12 Jun), Rina Putri (HR Manager, HR, Inactive, Last Updated 3 Jun), dan Intan Permata (baris 19). Kedua tab masing-masing berisi 3 user atau lebih dengan Position dan Division berbeda.
- Tab Total Control memuat sedikitnya dua baris dengan Name berbeda sebagai baris pembanding urutan Name (Ahmad Fauzi dan Bayu Nugraha, ditambah Budi Santoso, Dewi Lestari, dan tiga user milik spec).
- Data Dinamis milik spec (hook `before`, lewat seeding API), semuanya Total Control dan ditambahkan supaya kolom yang di-sort punya sedikitnya dua nilai distinct bagi asersi urutan (S-11):

| Nama | Email | Kondisi yang disiapkan |
|---|---|---|
| `Sementara Uji {runId}-054` | `sementarauji+{runId}-054@qwertysystem.net` | Active, Activated, Temporary User `Yes` dengan Temporary Until bertanggal berbeda dari Bayu Nugraha, TAG terpasang berkode berbeda dari `TG-00451` (TAG kedua yang belum terpasang disediakan tim FE) |
| `Pending Uji {runId}-054` | `pendinguji+{runId}-054@qwertysystem.net` | Activation Status `Pending Activation` |
| `Konfirmasi Uji {runId}-054` | `konfirmasiuji+{runId}-054@qwertysystem.net` | Activation Status `Pending Email Confirmation` |

- Nilai distinct per kolom yang di-sort pada Tab Total Control: Status `Active` dan `Inactive`; Temporary User `Yes` dan `No`; Last Updated sedikitnya tiga nilai (tanggal assign Dewi Lestari, hari uji untuk user milik spec, dan `—` Default User); Temporary Until dua tanggal berbeda (Bayu Nugraha dan `Sementara Uji {runId}-054`) serta baris kosong; Activation Status `Activated`, `Pending Activation`, dan `Pending Email Confirmation`; TAG dua kode berbeda serta baris belum paired (`—`).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus tiga user di atas dan lepas TAG kedua yang dipasang; kolom Temporary User, Temporary Until, Activation Status, dan TAG dikembalikan lewat `[Reset to Default]` (langkah 139 sampai 141), hook `after` sebagai cadangan menghapus preferensi kolom tabel itu di browser (pemulihan lewat langkah UI diterima untuk spec draft); sort tiap kolom kembali ke default lewat klik ketiga.
- Kemampuan teknis: membaca dan menghapus preferensi kolom di penyimpanan browser; membaca nilai satu kolom dari seluruh baris lintas halaman untuk mengasersi urutan dan posisi relatif baris; Popup Setup Column untuk menampilkan kolom; seeding API (akses level, status aktivasi, Temporary Until, pemasangan TAG) disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD dan tidak dikarang di spec.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ROLE-152: Sort kolom teks Name, Position, Division, Modified By

1. Klik header Name
2. Verifikasi Name terurut A-Z pada seluruh baris (semua halaman), baris `Ahmad Fauzi` di atas baris `Bayu Nugraha`
3. Klik header Name
4. Verifikasi Name terurut Z-A pada seluruh baris (semua halaman), baris `Bayu Nugraha` di atas baris `Ahmad Fauzi`
5. Klik header Name
6. Verifikasi urutan kembali ke default Name A-Z
7. Klik header Position
8. Verifikasi Position terurut A-Z pada seluruh baris (semua halaman)
9. Pindah ke halaman terakhir tabel
10. Verifikasi baris Default User (`—`) berada di akhir
11. Klik header Position
12. Verifikasi Position terurut Z-A pada seluruh baris (semua halaman)
13. Pindah ke halaman pertama tabel
14. Verifikasi baris Default User (`—`) berada di awal
15. Klik header Position
16. Verifikasi urutan kembali ke default Name A-Z
17. Klik header Division
18. Verifikasi Division terurut A-Z pada seluruh baris (semua halaman)
19. Pindah ke halaman terakhir tabel
20. Verifikasi baris Default User (`—`) berada di akhir
21. Klik header Division
22. Verifikasi Division terurut Z-A pada seluruh baris (semua halaman)
23. Pindah ke halaman pertama tabel
24. Verifikasi baris Default User (`—`) berada di awal
25. Klik header Division
26. Verifikasi urutan kembali ke default Name A-Z
27. Klik header Modified By
28. Verifikasi Modified By terurut A-Z menurut nama lengkap pada seluruh baris (semua halaman)
29. Pindah ke halaman terakhir tabel
30. Verifikasi baris Default User (`—`) berada di akhir
31. Klik header Modified By
32. Verifikasi Modified By terurut Z-A menurut nama lengkap pada seluruh baris (semua halaman)
33. Pindah ke halaman pertama tabel
34. Verifikasi baris Default User (`—`) berada di awal
35. Klik header Modified By
36. Verifikasi urutan kembali ke default Name A-Z
37. Klik Tab Read Only
38. Klik header Name
39. Verifikasi baris `Rina Putri` berada di atas baris `Siti Nurhaliza`
40. Klik header Name
41. Verifikasi baris `Siti Nurhaliza` berada di atas baris `Rina Putri`
42. Klik header Name
43. Verifikasi urutan kembali ke default Name A-Z
44. Klik header Position
45. Verifikasi baris `Siti Nurhaliza` (`Finance Staff`) berada di atas baris `Rina Putri` (`HR Manager`)
46. Klik header Position
47. Verifikasi baris `Rina Putri` (`HR Manager`) berada di atas baris `Siti Nurhaliza` (`Finance Staff`)
48. Klik header Position
49. Verifikasi urutan kembali ke default Name A-Z
50. Klik header Division
51. Verifikasi baris `Siti Nurhaliza` (`Finance`) berada di atas baris `Rina Putri` (`HR`)
52. Klik header Division
53. Verifikasi baris `Rina Putri` (`HR`) berada di atas baris `Siti Nurhaliza` (`Finance`)
54. Klik header Division
55. Verifikasi urutan kembali ke default Name A-Z
56. Klik header Modified By
57. Verifikasi Modified By terurut A-Z menurut nama lengkap pada seluruh baris (semua halaman)
58. Klik header Modified By
59. Verifikasi Modified By terurut Z-A menurut nama lengkap pada seluruh baris (semua halaman)
60. Klik header Modified By
61. Verifikasi urutan kembali ke default Name A-Z

### TC-GS-ROLE-153: Sort kolom Status (Active First / Inactive First)

62. Klik Tab Total Control
63. Klik header Status
64. Verifikasi seluruh baris Status `Active` berada di atas seluruh baris Status `Inactive`
65. Verifikasi baris `Ahmad Fauzi` dan `Budi Santoso` (Default User, Status `Active`) berada di atas baris `Dewi Lestari` (Status `Inactive`)
66. Klik header Status
67. Verifikasi seluruh baris Status `Inactive` berada di atas seluruh baris Status `Active`
68. Verifikasi baris `Dewi Lestari` (Status `Inactive`) berada di atas baris `Ahmad Fauzi` dan `Budi Santoso` (Status `Active`)
69. Klik header Status
70. Verifikasi urutan kembali ke default Name A-Z
71. Klik Tab Read Only
72. Klik header Status
73. Verifikasi baris `Siti Nurhaliza` (Status `Active`) berada di atas baris `Rina Putri` (Status `Inactive`)
74. Klik header Status
75. Verifikasi baris `Rina Putri` (Status `Inactive`) berada di atas baris `Siti Nurhaliza` (Status `Active`)
76. Klik header Status
77. Verifikasi urutan kembali ke default Name A-Z

### TC-GS-ROLE-154: Sort kolom Temporary User (Yes First / No First)

78. Klik Tab Total Control
79. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
80. Centang kolom Temporary User
81. Klik `[Save]`
82. Klik header Temporary User
83. Verifikasi Yes First: seluruh baris Temporary User `Yes` berada di atas seluruh baris `No` (baris `Bayu Nugraha` di atas baris `Ahmad Fauzi`)
84. Klik header Temporary User
85. Verifikasi No First: seluruh baris Temporary User `No` berada di atas seluruh baris `Yes` (baris `Ahmad Fauzi` di atas baris `Bayu Nugraha`)
86. Klik header Temporary User
87. Verifikasi urutan kembali ke default Name A-Z

### TC-GS-ROLE-155: Sort kolom tanggal Last Updated dan Temporary Until

88. Klik header Last Updated
89. Verifikasi Last Updated Oldest First pada seluruh baris (semua halaman)
90. Pindah ke halaman terakhir tabel
91. Verifikasi baris Default User (`—`) berada di akhir
92. Klik header Last Updated
93. Verifikasi Last Updated Newest First pada seluruh baris (semua halaman)
94. Pindah ke halaman pertama tabel
95. Verifikasi baris Default User (`—`) berada di awal
96. Klik header Last Updated
97. Verifikasi urutan kembali ke default Name A-Z
98. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
99. Centang kolom Temporary Until
100. Klik `[Save]`
101. Klik header Temporary Until
102. Verifikasi Temporary Until Oldest First pada seluruh baris (semua halaman)
103. Pindah ke halaman terakhir tabel
104. Verifikasi baris tanpa Temporary Until (kosong) berada di akhir
105. Klik header Temporary Until
106. Verifikasi Temporary Until Newest First pada seluruh baris (semua halaman)
107. Pindah ke halaman pertama tabel
108. Verifikasi baris tanpa Temporary Until (kosong) berada di awal
109. Klik header Temporary Until
110. Verifikasi urutan kembali ke default Name A-Z
111. Klik Tab Read Only
112. Klik header Last Updated
113. Verifikasi baris `Rina Putri` (3 Jun) berada di atas baris `Siti Nurhaliza` (12 Jun)
114. Klik header Last Updated
115. Verifikasi baris `Siti Nurhaliza` (12 Jun) berada di atas baris `Rina Putri` (3 Jun)
116. Klik header Last Updated
117. Verifikasi urutan kembali ke default Name A-Z

### TC-GS-ROLE-156: Sort kolom Activation Status dan TAG

118. Klik Tab Total Control
119. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
120. Centang kolom Activation Status
121. Centang kolom TAG
122. Klik `[Save]`
123. Klik header Activation Status
124. Verifikasi Activation Status terurut A-Z: `Activated`, `Pending Activation`, `Pending Email Confirmation`
125. Klik header Activation Status
126. Verifikasi Activation Status terurut Z-A: `Pending Email Confirmation`, `Pending Activation`, `Activated`
127. Klik header Activation Status
128. Verifikasi urutan kembali ke default Name A-Z
129. Klik header TAG
130. Verifikasi TAG terurut A-Z menurut kode TAG pada seluruh baris (semua halaman)
131. Pindah ke halaman terakhir tabel
132. Verifikasi baris belum paired (`—`) berada di akhir
133. Klik header TAG
134. Verifikasi TAG terurut Z-A menurut kode TAG pada seluruh baris (semua halaman)
135. Pindah ke halaman pertama tabel
136. Verifikasi baris belum paired (`—`) berada di awal
137. Klik header TAG
138. Verifikasi urutan kembali ke default Name A-Z
139. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
140. Klik `[Reset to Default]`
141. Klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): berpindah tab (langkah 37, 62, 78, 111, 118), menampilkan kolom lewat Popup Setup Column (langkah 81, 100, 122), memindahkan halaman tabel ke halaman terakhir sebelum asersi baris di akhir (langkah 9, 19, 29, 90, 103, 131) dan kembali ke halaman pertama sebelum asersi baris di awal (langkah 13, 23, 33, 94, 107, 135), dan memulihkan kolom ke bawaan di akhir spec (langkah 139 sampai 141). Kolom yang ditampilkan tidak dipulihkan di antara TC; pemulihan dilakukan sekali di akhir.
- Klik ketiga tiap header mengembalikan sort ke default Name A-Z (langkah `Verifikasi urutan kembali ke default Name A-Z`), sehingga tidak ada langkah pembersih sort terpisah (S-09).
- Spec melewati sekitar 35 langkah (141 langkah) karena lima TC menguji siklus sort tiga klik pada banyak kolom di dua tab, dan tiap klik menjadi satu langkah aksi dengan satu `Verifikasi` per klausa Expected (urutan, posisi baris kosong; S-01). Seluruh blok satu kelas harness (fungsional), satu aktor, satu dataset (Tab Total Control dan Tab Read Only); tiap kolom ditutup dengan klik ketiga yang mengembalikan sort ke default, sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Asersi urutan memakai seluruh baris lintas halaman karena tiap tab dapat berisi lebih dari satu halaman; asersi posisi relatif memakai baris bernama dari Pre-setup.
- Temuan untuk QA:
  - TC-GS-ROLE-152 Expected b dan c menulis baris Default User (`—`) "di akhir pada klik 2 (descending)", bertentangan dengan Expected d TC-GS-ROLE-152 (`—` di awal saat descending), TC-GS-ROLE-155 a, dan TC-GS-ROLE-191 b dan c (`—` di akhir saat ascending, di awal saat descending). Spec mengikuti TC-GS-ROLE-155 dan TC-GS-ROLE-191 (baris Default User di awal pada klik 2); TC-GS-ROLE-152 akan dibetulkan pemilik TC.
  - TC-GS-ROLE-152 Expected b, c, d: klausa posisi baris kosong (`—` di akhir saat ascending, di awal saat descending) berlaku untuk Tab Total Control; Tab Read Only tidak punya baris Default User dan tidak punya baris bernilai `—` pada Position, Division, atau Modified By yang disebut TC, sehingga klausa itu tidak diasersi pada Tab Read Only.
  - TC-GS-ROLE-152 Expected e menyebut Rina Putri dan Siti Nurhaliza bertukar posisi, tetapi Modified By Rina Putri tidak disebut; asersi Modified By Tab Read Only memakai urutan umum menurut nama lengkap. Posisi relatif Position (`Finance Staff` dan `HR Manager`) dan Division (`Finance` dan `HR`) diturunkan dari Pre-setup baris 4.
  - TC-GS-ROLE-152 klik 1 dan klik 3 pada kolom Name menghasilkan urutan yang sama (default Name A-Z); keduanya dibedakan lewat langkah klik bernomor, bukan lewat urutan baris.
  - TC-GS-ROLE-153 dan TC-GS-ROLE-154 tidak menyebut tab; TC-GS-ROLE-154 dan 155 (kolom Temporary User dan Temporary Until) dijalankan pada Tab Total Control, tempat Bayu Nugraha berada.
  - TC-GS-ROLE-155 b: Tab Total Control hanya punya satu user Temporary User di Pre-setup (Bayu Nugraha), sehingga urutan Temporary Until tidak punya dua tanggal berbeda; spec men-seed `Sementara Uji {runId}-054`.
  - TC-GS-ROLE-156 a menyebut tiga nilai Activation Status (`Activated`, `Pending Activation`, `Pending Email Confirmation`) tanpa menyebut user pemilik `Pending Email Confirmation`, dan TC-GS-ROLE-156 b tidak menyebut data TAG selain `TG-00451` milik Ahmad Fauzi; spec men-seed user milik spec dan meminta TAG kedua dari tim FE.
  - TC-GS-ROLE-155 c: tanggal Last Updated Intan Permata tidak disebut; asersi Tab Read Only hanya membandingkan Rina Putri dan Siti Nurhaliza.
