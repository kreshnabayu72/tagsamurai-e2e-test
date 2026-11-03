---
id: TC-AC-ACHS-E2E-020-role-matrix-visibilitas-elemen-per-role
title: "Role Matrix: Visibilitas Elemen Stock List, Stock Detail, dan Approvals per Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-64
  - TC-AC-ACHS-65
  - TC-AC-ACHS-66
  - TC-AC-ACHS-67
  - TC-AC-ACHS-68
  - TC-AC-ACHS-69
  - TC-AC-ACHS-70
  - TC-AC-ACHS-71
  - TC-AC-ACHS-72
  - TC-AC-ACHS-73
  - TC-AC-ACHS-197
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Stock List, Stock Detail, dan Approvals per Role

## Prerequisites

- Mode: FE+BE.
- Tabel "Role yang diuji" (spec ditulis per blok role; akun pertama login di hook `before`, akun lain lewat Step ganti akun eksplisit):

  | Blok | Role | Akun (Pre-setup) | TC |
  |---|---|---|---|
  | 1 | Read Only | `{Fixture.hardwareStock.account.p03.readOnly.email}` (No 3) | 64, 73, 197 |
  | 2 | Create-Only | `{Fixture.hardwareStock.account.p04.createOnly.email}` (No 4) | 65 |
  | 3 | Delete-Only | `{Fixture.hardwareStock.account.p05.deleteOnly.email}` (No 5) | 66 |
  | 4 | Total Control | `{Fixture.hardwareStock.account.p01.totalControl.email}` (No 1; password `Spectra.env.AC_TC_PASSWORD`) | 67 |
  | 5 | Default User | `{Fixture.hardwareStock.account.p02.defaultUser.email}` (No 2) | 68 |
  | 6 | Additional Approver dengan capability Create | `{Fixture.hardwareStock.account.p06.additionalApproverCreate.email}` (No 6) | 69 |
  | 7 | Additional Approver tanpa capability Manage hardware stock | `{Fixture.hardwareStock.account.p07.additionalApproverOnly.email}` (No 7) | 70 |
  | 8 | Distributor Pre-setup No 10, Local Registration aktif | `{Fixture.hardwareStock.account.p10.distributorCakra.email}` (No 10) | 71 |
  | 9 | Distributor Pre-setup No 12, Local Registration nonaktif | `{Fixture.hardwareStock.account.p12.distributorSumberJaya.email}` (No 12) | 72 |

- Akun aktor pertama: Read Only (blok 1). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Password akun selain Total Control memakai nama env `AC_<ROLE>_PASSWORD` yang ditetapkan tim FE (belum terdaftar; lihat Temuan untuk QA).
- Data Pre-setup (hanya dibaca): Katalog SKU 30 baris (No 16), SKU `{Fixture.hardwareStock.p16.a[3].sku}` (unit milik Distributor Pre-setup No 10 dan Distributor Pre-setup No 11, No 27), SKU `{Fixture.hardwareStock.p16.a[4].sku}` dengan unit Available `{Fixture.hardwareStock.p17.e[10].deviceName}` dan unit Waiting for Approval `{Fixture.hardwareStock.p17.e[28].deviceName}` (No 17), Approvals Tab Active 12 Subject dan Tab History 12 Subject (No 21, 22). Unit Available milik Distributor Pre-setup No 12 pada SKU `{Fixture.hardwareStock.p16.a[3].sku}` yang dipakai blok 9 tidak ada pada Pre-setup No 27; disediakan tim FE/BE (lihat Temuan untuk QA). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p03.readOnly.email}` | No 3 | email akun Pre-setup No 3 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p03.readOnly.email` |
  | `{Fixture.hardwareStock.account.p04.createOnly.email}` | No 4 | email akun Pre-setup No 4 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p04.createOnly.email` |
  | `{Fixture.hardwareStock.account.p05.deleteOnly.email}` | No 5 | email akun Pre-setup No 5 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p05.deleteOnly.email` |
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.account.p02.defaultUser.email}` | No 2 | email akun Pre-setup No 2 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p02.defaultUser.email` |
  | `{Fixture.hardwareStock.account.p06.additionalApproverCreate.email}` | No 6 | email akun Pre-setup No 6 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p06.additionalApproverCreate.email` |
  | `{Fixture.hardwareStock.account.p07.additionalApproverOnly.email}` | No 7 | email akun Pre-setup No 7 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p07.additionalApproverOnly.email` |
  | `{Fixture.hardwareStock.account.p10.distributorCakra.email}` | No 10 | email akun Pre-setup No 10 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p10.distributorCakra.email` |
  | `{Fixture.hardwareStock.account.p12.distributorSumberJaya.email}` | No 12 | email akun Pre-setup No 12 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p12.distributorSumberJaya.email` |
  | `{Fixture.hardwareStock.p16.a[3].sku}` | No 16, 27, Tabel A baris 3 | kode SKU Smart Fixed Reader (8 Total Registered, 8 Available, 0 In Use) | `Fixture.hardwareStock.p16.a[3].sku` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |
  | `{Fixture.hardwareStock.p16.a[4].brand}` | No 16, Tabel A baris 4 | Brand SKU Handheld Reader Long Range (kata kunci Search dan opsi Filter) | `Fixture.hardwareStock.p16.a[4].brand` |
  | `{Fixture.hardwareStock.p17.e[10].deviceName}` | No 17, Tabel E baris N = 10 | Device Name unit Available SKU Long Range dengan N terkecil (N = 10) | `Fixture.hardwareStock.p17.e[10].deviceName` |
  | `{Fixture.hardwareStock.p17.e[28].deviceName}` | No 17, Tabel E baris N = 28 | Device Name unit Waiting for Approval SKU Long Range (N = 28; Current Power `—`) | `Fixture.hardwareStock.p17.e[28].deviceName` |
  | `{Fixture.hardwareStock.p27.fx[1].serialNumber}` | No 27 | Serial Number unit Available Smart Fixed Reader ke-1 (milik Distributor No 10) | `Fixture.hardwareStock.p27.fx[1].serialNumber` |
  | `{Fixture.hardwareStock.p22.d[2].matchedIdentifier}` | No 22, Tabel D baris 2 | Matched Identifier Subject History Approved oleh user Pre-setup No 1 dengan Approval Note berisi teks | `Fixture.hardwareStock.p22.d[2].matchedIdentifier` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen untuk akun aktor default suite. Flag halaman Stock List dan Approvals Hardware Stock untuk akun pada tabel "Role yang diuji" disetel true di hook `before` spec ini dan dipulihkan di hook `after`; kemampuan disediakan tim FE/BE.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Blok 1: Read Only (TC-AC-ACHS-64, 73, 197)

1. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`
2. Verifikasi overlay Stock List hanya berisi `Detail` (row action `Add Stock` Hidden)
3. Tutup overlay dengan `Esc`
4. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
5. Verifikasi tombol `[Add Stock]` Hidden di toolbar Tab Available
6. Ketik Search Device Name `{Fixture.hardwareStock.p17.e[10].deviceName}`, tekan Enter
7. Klik `(⋯)` pada baris unit Available `{Fixture.hardwareStock.p17.e[10].deviceName}`
8. Verifikasi row action `Hardware Log` Show pada overlay unit Available
9. Verifikasi row action `Delete` Hidden pada overlay unit Available
10. Tutup overlay dengan `Esc`
11. Verifikasi Stock List, Stock Detail, icon Download, `[Event Log]`, dan `Hardware Log` Show
12. Klik `(←)` pada kotak Search
13. Verifikasi menu `Approvals > Hardware Stock` Show di sidebar
14. Klik menu Approvals > Hardware Stock di sidebar
15. Verifikasi Tab Active dan Tab History tampil
16. Verifikasi row action `Review` Hidden di Tab Active
17. Klik Tab `History`
18. Verifikasi row action `Detail` Show di Tab History
19. Klik menu Hardware > Stock di sidebar
20. Ketik Search Brand `{Fixture.hardwareStock.p16.a[4].brand}`, tekan Enter
21. Verifikasi Search Show dan berfungsi: sedikitnya satu baris tampil dan setiap baris hasil memuat Brand `{Fixture.hardwareStock.p16.a[4].brand}`
22. Klik icon Filter, pilih Type `Handheld Reader`, klik `[Apply]`
23. Verifikasi Filter Show dan berfungsi: sedikitnya satu baris tampil dan setiap baris hasil bertipe `Handheld Reader`
24. Klik header kolom Total Registered
25. Verifikasi Sort Show dan berfungsi: indikator sort Total Registered aktif
26. Verifikasi Pagination Show dan berfungsi: info pagination tampil
27. Klik header kolom Actions `(⋯)`
28. Verifikasi Column Visibility Show dan berfungsi: overlay Column Visibility terbuka
29. Tutup overlay Column Visibility dengan `Esc`
30. Klik icon Download
31. Verifikasi Download Show dan berfungsi: menu dengan opsi `Download as CSV` tampil
32. Tutup menu Download dengan `Esc`
33. Klik menu Approvals > Hardware Stock di sidebar
34. Pastikan Tab Active aktif
35. Verifikasi sedikitnya satu baris tampil di Tab Active
36. Verifikasi Tab Active tanpa row action `Review`
37. Klik Tab `History`
38. Klik row action `Detail` pada baris `{Fixture.hardwareStock.p22.d[2].matchedIdentifier}`
39. Verifikasi radio Approve/Reject pre-selected `Approve` dan disabled
40. Verifikasi Approval Note berisi teks aktual atau `—` dalam keadaan disabled
41. Verifikasi footer dialog hanya `[Close]`
42. Klik `[Close]`

### Blok 2: Create-Only (TC-AC-ACHS-65)

43. Logout, lalu login sebagai Create-Only (Pre-setup No 4)
44. Klik menu Hardware > Stock di sidebar
45. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`
46. Verifikasi row action `Add Stock` Show pada overlay Stock List
47. Tutup overlay dengan `Esc`
48. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
49. Verifikasi tombol `[Add Stock]` Show di toolbar Tab Available
50. Ketik Search Device Name `{Fixture.hardwareStock.p17.e[10].deviceName}`, tekan Enter
51. Klik `(⋯)` pada baris unit Available `{Fixture.hardwareStock.p17.e[10].deviceName}`
52. Verifikasi row action `Hardware Log` Show pada overlay unit Available
53. Verifikasi row action `Delete` Hidden pada overlay unit Available
54. Tutup overlay dengan `Esc`
55. Verifikasi Stock List, Stock Detail, icon Download, `[Event Log]`, dan `Hardware Log` Show
56. Verifikasi menu `Hardware > Stock` tampil di sidebar
57. Verifikasi menu `Approvals > Hardware Stock` Hidden di sidebar

### Blok 3: Delete-Only (TC-AC-ACHS-66)

58. Logout, lalu login sebagai Delete-Only (Pre-setup No 5)
59. Klik menu Hardware > Stock di sidebar
60. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`
61. Verifikasi overlay Stock List hanya berisi `Detail` (row action `Add Stock` Hidden)
62. Tutup overlay dengan `Esc`
63. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
64. Verifikasi tombol `[Add Stock]` Hidden di toolbar Tab Available
65. Ketik Search Device Name `{Fixture.hardwareStock.p17.e[10].deviceName}`, tekan Enter
66. Klik `(⋯)` pada baris unit Available `{Fixture.hardwareStock.p17.e[10].deviceName}`
67. Verifikasi row action `Delete` Show pada overlay unit Available
68. Tutup overlay dengan `Esc`
69. Ganti isi kotak search dengan Device Name `{Fixture.hardwareStock.p17.e[28].deviceName}`, tekan Enter
70. Klik `(⋯)` pada baris unit Waiting for Approval `{Fixture.hardwareStock.p17.e[28].deviceName}`
71. Verifikasi row action `Hardware Log` Show pada overlay unit Waiting for Approval
72. Verifikasi row action `Delete` Hidden pada overlay unit Waiting for Approval
73. Tutup overlay dengan `Esc`
74. Verifikasi Stock List, Stock Detail, icon Download, `[Event Log]`, dan `Hardware Log` Show
75. Verifikasi menu `Hardware > Stock` tampil di sidebar
76. Verifikasi menu `Approvals > Hardware Stock` Hidden di sidebar

### Blok 4: Total Control (TC-AC-ACHS-67)

77. Logout, lalu login sebagai Total Control (Pre-setup No 1)
78. Klik menu Hardware > Stock di sidebar
79. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`
80. Verifikasi row action `Add Stock` Show pada overlay Stock List
81. Tutup overlay dengan `Esc`
82. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
83. Verifikasi tombol `[Add Stock]` Show di toolbar Tab Available
84. Ketik Search Device Name `{Fixture.hardwareStock.p17.e[10].deviceName}`, tekan Enter
85. Klik `(⋯)` pada baris unit Available `{Fixture.hardwareStock.p17.e[10].deviceName}`
86. Verifikasi row action `Delete` Show pada overlay unit Available
87. Tutup overlay dengan `Esc`
88. Verifikasi Stock List, Stock Detail, icon Download, `[Event Log]`, dan `Hardware Log` Show
89. Verifikasi menu `Approvals > Hardware Stock` Show di sidebar
90. Klik menu Approvals > Hardware Stock di sidebar
91. Verifikasi row action `Review` Show di Tab Active
92. Klik Tab `History`
93. Verifikasi row action `Detail` Show di Tab History

### Blok 5: Default User (TC-AC-ACHS-68)

94. Logout, lalu login sebagai Default User (Pre-setup No 2)
95. Klik menu Hardware > Stock di sidebar
96. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`
97. Verifikasi row action `Add Stock` Show pada overlay Stock List
98. Tutup overlay dengan `Esc`
99. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
100. Verifikasi tombol `[Add Stock]` Show di toolbar Tab Available
101. Ketik Search Device Name `{Fixture.hardwareStock.p17.e[10].deviceName}`, tekan Enter
102. Klik `(⋯)` pada baris unit Available `{Fixture.hardwareStock.p17.e[10].deviceName}`
103. Verifikasi row action `Delete` Show pada overlay unit Available
104. Tutup overlay dengan `Esc`
105. Verifikasi menu `Approvals > Hardware Stock` Show di sidebar
106. Klik menu Approvals > Hardware Stock di sidebar
107. Verifikasi row action `Review` Show di Tab Active

### Blok 6: Additional Approver dengan capability Create (TC-AC-ACHS-69)

108. Logout, lalu login sebagai Additional Approver dengan capability Create (Pre-setup No 6)
109. Klik menu Hardware > Stock di sidebar
110. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`
111. Verifikasi row action `Add Stock` Show pada overlay Stock List
112. Tutup overlay dengan `Esc`
113. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
114. Ketik Search Device Name `{Fixture.hardwareStock.p17.e[10].deviceName}`, tekan Enter
115. Klik `(⋯)` pada baris unit Available `{Fixture.hardwareStock.p17.e[10].deviceName}`
116. Verifikasi row action `Hardware Log` Show pada overlay unit Available
117. Verifikasi row action `Delete` Hidden pada overlay unit Available
118. Tutup overlay dengan `Esc`
119. Verifikasi menu `Approvals > Hardware Stock` Show di sidebar
120. Klik menu Approvals > Hardware Stock di sidebar
121. Verifikasi row action `Review` Show di Tab Active

### Blok 7: Additional Approver tanpa capability Manage hardware stock (TC-AC-ACHS-70)

122. Logout, lalu login sebagai Additional Approver tanpa capability Manage hardware stock (Pre-setup No 7)
123. Verifikasi sidebar Admin Console tampil dengan sedikitnya satu item menu
124. Verifikasi menu `Hardware > Stock` tidak muncul di sidebar
125. Verifikasi menu `Approvals > Hardware Stock` Show di sidebar
126. Klik menu Approvals > Hardware Stock di sidebar
127. Klik `[Review]` pada baris pertama Tab Active
128. Verifikasi row action `Review` Show dan dialog Detail Approval terbuka
129. Verifikasi radio Approve dan Reject aktif
130. Pilih radio `Approve`
131. Klik `[Cancel]` pada dialog Detail Approval

### Blok 8: Distributor Pre-setup No 10, Local Registration aktif (TC-AC-ACHS-71)

132. Logout, lalu login sebagai Distributor (Pre-setup No 10)
133. Klik menu Hardware > Stock di sidebar
134. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`
135. Verifikasi row action `Add Stock` Show pada baris SKU dalam scope
136. Tutup overlay dengan `Esc`
137. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`, klik row action `Detail`
138. Verifikasi tombol `[Add Stock]` Show di toolbar Tab Available
139. Ketik Search Serial Number `{Fixture.hardwareStock.p27.fx[1].serialNumber}`, tekan Enter
140. Klik `(⋯)` pada baris unit Available milik Distributor Pre-setup No 10
141. Verifikasi row action `Hardware Log` Show pada overlay unit milik sendiri
142. Verifikasi row action `Delete` Show pada overlay unit Available milik sendiri
143. Tutup overlay dengan `Esc`
144. Verifikasi icon `[Event Log]` Show di toolbar Tab Available
145. Verifikasi menu `Approvals > Hardware Stock` Hidden di sidebar

### Blok 9: Distributor Pre-setup No 12, Local Registration nonaktif (TC-AC-ACHS-72)

146. Logout, lalu login sebagai Distributor (Pre-setup No 12)
147. Klik menu Hardware > Stock di sidebar
148. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`
149. Verifikasi overlay Stock List hanya berisi `Detail` (row action `Add Stock` Hidden)
150. Tutup overlay dengan `Esc`
151. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`, klik row action `Detail`
152. Verifikasi tombol `[Add Stock]` Hidden di toolbar Tab Available
153. Verifikasi Stock Detail stok Local Registration yang sudah ada dapat dibaca: sedikitnya satu baris unit tampil
154. Klik `(⋯)` pada baris unit Available milik Distributor Pre-setup No 12
155. Verifikasi row action `Hardware Log` Show pada overlay unit milik sendiri
156. Verifikasi row action `Delete` tetap Show pada overlay unit Available milik sendiri
157. Tutup overlay dengan `Esc`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 197). Tidak ada TC hanya-BE di spec ini.
- Spec Role Matrix varian A (matriks visibilitas per role, tanpa kata Positif atau Negatif pada title). Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (langkah 43, 58, 77, 94, 108, 122, 132, 146) dan tiap blok mengasersi himpunan elemen yang berbeda sesuai Expected TC role itu; bagian sesudah tiap ganti akun tetap bermakna walau blok sebelumnya gagal keras. Role Matrix negatif sidebar dan direct URL ada di spec 021.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): `Esc` untuk menutup overlay dan menu, `(←)` pada kotak Search, klik menu sidebar untuk membuka surface yang sudah dibuka TC lain (mereset Search, Sort, dan Filter), dan Search Device Name `{Fixture.hardwareStock.p17.e[10].deviceName}` atau `{Fixture.hardwareStock.p17.e[28].deviceName}` serta Serial Number `{Fixture.hardwareStock.p27.fx[1].serialNumber}` untuk menemukan baris unit target (R-16). Klik `[Cancel]` pada dialog Detail Approval (blok 7) dan `[Close]` (blok 1) berasal dari TC.
- Spec di atas smell 35 langkah (157 langkah). Alasan: seluruh blok adalah matriks visibilitas elemen modul yang sama (Stock List, Stock Detail, Approvals) pada role berbeda, tiap blok berdiri sendiri, dan memecahnya menambah login, hook, dan cleanup per role tanpa pemisah nyata (bagian 3a).
- Temuan untuk QA:
  - TC-69 Expected b ("`Delete` Hidden") tidak punya langkah membuka Stock Detail pada Langkah Uji; spec menambah pembukaan Stock Detail dan overlay unit Available pada blok 6. Expected e ("Hak Approve/Reject berasal dari tier Additional Approver") tidak punya langkah observasi dan tidak diasersi (Post Condition tanpa langkah observasi, S-01).
  - TC-71 dan TC-72 mengacu "unit Available milik sendiri" pada SKU `{Fixture.hardwareStock.p16.a[3].sku}`. Pre-setup No 27 memberi unit SKU itu hanya kepada Distributor No 10 (5 unit) dan Distributor No 11 (3 unit); Distributor No 12 hanya memiliki `{Fixture.hardwareStock.p17.e[28].deviceName}` yang berstatus Waiting for Approval. Blok 9 mensyaratkan unit Available milik Distributor No 12 yang tidak ada pada Pre-setup; disediakan tim FE/BE. Bila tidak ada, baris SKU FX9600 mungkin tidak tampil bagi Distributor ini.
  - TC-64 langkah 2 sampai 5 mengamati overlay dan toolbar tetapi tidak menyebut membuka Tab History; Expected e (`Detail` Tab History Show) diamati pada langkah menu Approvals sesudahnya.
  - TC-197 Expected b ("Approval Note teks aktual atau `—`") tidak menyebut baris History yang dibuka; spec memakai baris `{Fixture.hardwareStock.p22.d[2].matchedIdentifier}`.
  - TC-73 Expected tidak menyebut kriteria "berfungsi" per kontrol; spec memakai efek yang dapat diamati (hasil tersaring, indikator sort, overlay terbuka, menu Download tampil).
  - TC-70 mensyaratkan akun Pre-setup No 7 yang tidak memiliki menu Hardware > Stock sehingga hook `beforeEach` suite (membuka Stock List) tidak berlaku untuk blok ini; blok dimulai dari halaman yang terbuka sesudah login.
  - Password akun selain Total Control memakai nama env `AC_<ROLE>_PASSWORD` yang belum terdaftar; diminta dari tim FE.
  - Population Stock dan Approvals tidak ditulis literal: spec merujuk Pre-setup lewat tabel Parameter Pre-setup di Prerequisites sehingga tidak memerlukan pengecualian S-12. Email akun aktor dirujuk lewat kunci `account.*` pada tabel Parameter Pre-setup (kredensial login).
  - Perbandingan kata kunci Search terhadap substring TC (S-12): Search Brand `Zebra` (TC-73) dan Brand penuh `Zebra`: hasil sama (SKU TC52, FX9600, RFD40). Search Device Name unit dan Serial Number (langkah 6, 50, 65, 84, 101, 114, 139) adalah Search penghubung, bukan penggantian substring TC; nilai penuh masing-masing hanya cocok dengan satu unit. Tidak ada perbedaan hasil.
