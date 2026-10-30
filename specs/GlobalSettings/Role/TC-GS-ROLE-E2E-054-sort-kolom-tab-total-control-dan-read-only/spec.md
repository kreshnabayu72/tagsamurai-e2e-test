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
- Data Dinamis milik spec (hook `before`, lewat seeding API), semuanya Total Control dan ditambahkan supaya kolom yang di-sort punya sedikitnya dua nilai distinct bagi asersi urutan (S-11):

| Nama | Email | Kondisi yang disiapkan |
|---|---|---|
| `Sementara Uji {runId}-054` | `sementarauji+{runId}-054@qwertysystem.net` | Active, Activated, Temporary User `Yes` dengan Temporary Until bertanggal berbeda dari Bayu Nugraha, TAG terpasang berkode berbeda dari `TG-00451` (TAG kedua yang belum terpasang disediakan tim FE) |
| `Pending Uji {runId}-054` | `pendinguji+{runId}-054@qwertysystem.net` | Activation Status `Pending Activation` |
| `Konfirmasi Uji {runId}-054` | `konfirmasiuji+{runId}-054@qwertysystem.net` | Activation Status `Pending Email Confirmation` |

- Nilai distinct per kolom yang di-sort pada Tab Total Control: Status `Active` dan `Inactive`; Temporary User `Yes` dan `No`; Last Updated sedikitnya tiga nilai (tanggal assign Dewi Lestari, hari uji untuk user milik spec, dan `—` Default User); Temporary Until dua tanggal berbeda (Bayu Nugraha dan `Sementara Uji {runId}-054`) serta baris kosong; Activation Status `Activated`, `Pending Activation`, dan `Pending Email Confirmation`; TAG dua kode berbeda serta baris belum paired (`—`).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus tiga user di atas dan lepas TAG kedua yang dipasang; kolom Temporary User, Temporary Until, Activation Status, dan TAG dikembalikan lewat `[Reset to Default]` (langkah 127 sampai 129); sort tiap kolom kembali ke default lewat klik ketiga.
- Kemampuan teknis: membaca nilai satu kolom dari seluruh baris lintas halaman untuk mengasersi urutan dan posisi relatif baris; Popup Setup Column untuk menampilkan kolom; seeding API (akses level, status aktivasi, Temporary Until, pemasangan TAG) disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD dan tidak dikarang di spec.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ROLE-152: Sort kolom teks Name, Position, Division, Modified By

1. Klik header Name
2. Verifikasi Name terurut A-Z pada seluruh baris (semua halaman)
3. Klik header Name
4. Verifikasi Name terurut Z-A pada seluruh baris (semua halaman)
5. Klik header Name
6. Verifikasi urutan kembali ke default Name A-Z
7. Klik header Position
8. Verifikasi Position terurut A-Z pada seluruh baris (semua halaman)
9. Verifikasi baris Default User (`—`) berada di akhir
10. Klik header Position
11. Verifikasi Position terurut Z-A pada seluruh baris (semua halaman)
12. Verifikasi baris Default User (`—`) berada di awal
13. Klik header Position
14. Verifikasi urutan kembali ke default Name A-Z
15. Klik header Division
16. Verifikasi Division terurut A-Z pada seluruh baris (semua halaman)
17. Verifikasi baris Default User (`—`) berada di akhir
18. Klik header Division
19. Verifikasi Division terurut Z-A pada seluruh baris (semua halaman)
20. Verifikasi baris Default User (`—`) berada di awal
21. Klik header Division
22. Verifikasi urutan kembali ke default Name A-Z
23. Klik header Modified By
24. Verifikasi Modified By terurut A-Z menurut nama lengkap pada seluruh baris (semua halaman)
25. Verifikasi baris Default User (`—`) berada di akhir
26. Klik header Modified By
27. Verifikasi Modified By terurut Z-A menurut nama lengkap pada seluruh baris (semua halaman)
28. Verifikasi baris Default User (`—`) berada di awal
29. Klik header Modified By
30. Verifikasi urutan kembali ke default Name A-Z
31. Klik Tab Read Only
32. Klik header Name
33. Verifikasi baris `Rina Putri` berada di atas baris `Siti Nurhaliza`
34. Klik header Name
35. Verifikasi baris `Siti Nurhaliza` berada di atas baris `Rina Putri`
36. Klik header Name
37. Verifikasi urutan kembali ke default Name A-Z
38. Klik header Position
39. Verifikasi baris `Siti Nurhaliza` (`Finance Staff`) berada di atas baris `Rina Putri` (`HR Manager`)
40. Klik header Position
41. Verifikasi baris `Rina Putri` (`HR Manager`) berada di atas baris `Siti Nurhaliza` (`Finance Staff`)
42. Klik header Position
43. Verifikasi urutan kembali ke default Name A-Z
44. Klik header Division
45. Verifikasi baris `Siti Nurhaliza` (`Finance`) berada di atas baris `Rina Putri` (`HR`)
46. Klik header Division
47. Verifikasi baris `Rina Putri` (`HR`) berada di atas baris `Siti Nurhaliza` (`Finance`)
48. Klik header Division
49. Verifikasi urutan kembali ke default Name A-Z
50. Klik header Modified By
51. Verifikasi Modified By terurut A-Z menurut nama lengkap pada seluruh baris (semua halaman)
52. Klik header Modified By
53. Verifikasi Modified By terurut Z-A menurut nama lengkap pada seluruh baris (semua halaman)
54. Klik header Modified By
55. Verifikasi urutan kembali ke default Name A-Z

### TC-GS-ROLE-153: Sort kolom Status (Active First / Inactive First)

56. Klik Tab Total Control
57. Klik header Status
58. Verifikasi seluruh baris Status `Active` berada di atas seluruh baris Status `Inactive`
59. Verifikasi baris `Ahmad Fauzi` dan `Budi Santoso` (Default User, Status `Active`) berada di atas baris `Dewi Lestari` (Status `Inactive`)
60. Klik header Status
61. Verifikasi seluruh baris Status `Inactive` berada di atas seluruh baris Status `Active`
62. Verifikasi baris `Dewi Lestari` (Status `Inactive`) berada di atas baris `Ahmad Fauzi` dan `Budi Santoso` (Status `Active`)
63. Klik header Status
64. Verifikasi urutan kembali ke default Name A-Z
65. Klik Tab Read Only
66. Klik header Status
67. Verifikasi baris `Siti Nurhaliza` (Status `Active`) berada di atas baris `Rina Putri` (Status `Inactive`)
68. Klik header Status
69. Verifikasi baris `Rina Putri` (Status `Inactive`) berada di atas baris `Siti Nurhaliza` (Status `Active`)
70. Klik header Status
71. Verifikasi urutan kembali ke default Name A-Z

### TC-GS-ROLE-154: Sort kolom Temporary User (Yes First / No First)

72. Klik Tab Total Control
73. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
74. Centang kolom Temporary User
75. Klik `[Save]`
76. Klik header Temporary User
77. Verifikasi Yes First: seluruh baris Temporary User `Yes` berada di atas seluruh baris `No` (baris `Bayu Nugraha` di atas baris `Ahmad Fauzi`)
78. Klik header Temporary User
79. Verifikasi No First: seluruh baris Temporary User `No` berada di atas seluruh baris `Yes` (baris `Ahmad Fauzi` di atas baris `Bayu Nugraha`)
80. Klik header Temporary User
81. Verifikasi urutan kembali ke default Name A-Z

### TC-GS-ROLE-155: Sort kolom tanggal Last Updated dan Temporary Until

82. Klik header Last Updated
83. Verifikasi Last Updated Oldest First pada seluruh baris (semua halaman)
84. Verifikasi baris Default User (`—`) berada di akhir
85. Klik header Last Updated
86. Verifikasi Last Updated Newest First pada seluruh baris (semua halaman)
87. Verifikasi baris Default User (`—`) berada di awal
88. Klik header Last Updated
89. Verifikasi urutan kembali ke default Name A-Z
90. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
91. Centang kolom Temporary Until
92. Klik `[Save]`
93. Klik header Temporary Until
94. Verifikasi Temporary Until Oldest First pada seluruh baris (semua halaman)
95. Verifikasi baris tanpa Temporary Until (kosong) berada di akhir
96. Klik header Temporary Until
97. Verifikasi Temporary Until Newest First pada seluruh baris (semua halaman)
98. Verifikasi baris tanpa Temporary Until (kosong) berada di awal
99. Klik header Temporary Until
100. Verifikasi urutan kembali ke default Name A-Z
101. Klik Tab Read Only
102. Klik header Last Updated
103. Verifikasi baris `Rina Putri` (3 Jun) berada di atas baris `Siti Nurhaliza` (12 Jun)
104. Klik header Last Updated
105. Verifikasi baris `Siti Nurhaliza` (12 Jun) berada di atas baris `Rina Putri` (3 Jun)
106. Klik header Last Updated
107. Verifikasi urutan kembali ke default Name A-Z

### TC-GS-ROLE-156: Sort kolom Activation Status dan TAG

108. Klik Tab Total Control
109. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
110. Centang kolom Activation Status
111. Centang kolom TAG
112. Klik `[Save]`
113. Klik header Activation Status
114. Verifikasi Activation Status terurut A-Z: `Activated`, `Pending Activation`, `Pending Email Confirmation`
115. Klik header Activation Status
116. Verifikasi Activation Status terurut Z-A: `Pending Email Confirmation`, `Pending Activation`, `Activated`
117. Klik header Activation Status
118. Verifikasi urutan kembali ke default Name A-Z
119. Klik header TAG
120. Verifikasi TAG terurut A-Z menurut kode TAG pada seluruh baris (semua halaman)
121. Verifikasi baris belum paired (`—`) berada di akhir
122. Klik header TAG
123. Verifikasi TAG terurut Z-A menurut kode TAG pada seluruh baris (semua halaman)
124. Verifikasi baris belum paired (`—`) berada di awal
125. Klik header TAG
126. Verifikasi urutan kembali ke default Name A-Z
127. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
128. Klik `[Reset to Default]`
129. Klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): berpindah tab (langkah 31, 56, 72, 101, 108), menampilkan kolom lewat Popup Setup Column (langkah 75, 92, 112), dan memulihkan kolom ke bawaan di akhir spec (langkah 127 sampai 129). Kolom yang ditampilkan tidak dipulihkan di antara TC; pemulihan dilakukan sekali di akhir.
- Klik ketiga tiap header mengembalikan sort ke default Name A-Z (langkah `Verifikasi urutan kembali ke default Name A-Z`), sehingga tidak ada langkah pembersih sort terpisah (S-09).
- Spec melewati sekitar 35 langkah (129 langkah) karena lima TC menguji siklus sort tiga klik pada banyak kolom di dua tab, dan tiap klik menjadi satu langkah aksi dengan satu `Verifikasi` per klausa Expected (urutan, posisi baris kosong; S-01). Seluruh blok satu kelas harness (fungsional), satu aktor, satu dataset (Tab Total Control dan Tab Read Only); tiap kolom ditutup dengan klik ketiga yang mengembalikan sort ke default, sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Asersi urutan memakai seluruh baris lintas halaman karena tiap tab dapat berisi lebih dari satu halaman; asersi posisi relatif memakai baris bernama dari Pre-setup.
- Temuan untuk QA:
  - TC-GS-ROLE-152 Expected b, c, d: klausa posisi baris kosong (`—` di akhir saat ascending, di awal saat descending) berlaku untuk Tab Total Control; Tab Read Only tidak punya baris Default User dan tidak punya baris bernilai `—` pada Position, Division, atau Modified By yang disebut TC, sehingga klausa itu tidak diasersi pada Tab Read Only.
  - TC-GS-ROLE-152 Expected e menyebut Rina Putri dan Siti Nurhaliza bertukar posisi, tetapi Modified By Rina Putri tidak disebut; asersi Modified By Tab Read Only memakai urutan umum menurut nama lengkap. Posisi relatif Position (`Finance Staff` dan `HR Manager`) dan Division (`Finance` dan `HR`) diturunkan dari Pre-setup baris 4.
  - TC-GS-ROLE-152 klik 1 dan klik 3 pada kolom Name menghasilkan urutan yang sama (default Name A-Z); keduanya dibedakan lewat langkah klik bernomor, bukan lewat urutan baris.
  - TC-GS-ROLE-153 dan TC-GS-ROLE-154 tidak menyebut tab; TC-GS-ROLE-154 dan 155 (kolom Temporary User dan Temporary Until) dijalankan pada Tab Total Control, tempat Bayu Nugraha berada.
  - TC-GS-ROLE-155 b: Tab Total Control hanya punya satu user Temporary User di Pre-setup (Bayu Nugraha), sehingga urutan Temporary Until tidak punya dua tanggal berbeda; spec men-seed `Sementara Uji {runId}-054`.
  - TC-GS-ROLE-156 a menyebut tiga nilai Activation Status (`Activated`, `Pending Activation`, `Pending Email Confirmation`) tanpa menyebut user pemilik `Pending Email Confirmation`, dan TC-GS-ROLE-156 b tidak menyebut data TAG selain `TG-00451` milik Ahmad Fauzi; spec men-seed user milik spec dan meminta TAG kedua dari tim FE.
  - TC-GS-ROLE-155 c: tanggal Last Updated Intan Permata tidak disebut; asersi Tab Read Only hanya membandingkan Rina Putri dan Siti Nurhaliza.
