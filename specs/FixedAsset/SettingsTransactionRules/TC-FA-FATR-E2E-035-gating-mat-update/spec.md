---
id: TC-FA-FATR-E2E-035-gating-mat-update
title: "Gating Manage asset & TAG (Read + Update) dan Group Manager"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§2#r2, §2#r4, §2#r8, §2#p2, §2#p4, §2#p7, §2#p8, §2#p9, §4.1#r289, §4.3#r5, §4.8#r1, §4.8#r2, §4.8#r3, §4.8#r4, §4.8#r5, §4.8#r6, §4.8#r7, §4.8#r8, §4.8#r9, §4.8#r10, §4.8#r11, §4.8#r12, §4.8#p2, §9.4.2#r23, §9.4.2#r30, §9.4.4#r24, §9.4.4#r25, §9.11#r2, EB-AKS-5@add-override, EB-AKS-5@delete-override, §4.1#r288, §9.3#b1, §9.11#r6, §9.11#r9]
smoke: [§9.3#b1, §9.11#r6, §9.11#r9]
dependsOn: []
trace:
  §2#r2: [4, 7, 9, 37]
  §2#r4: [104, 106, 110, 121, 129, 131, 139]
  §2#r8: [2, 7, 12, 17, 21, 22, 23, 55]
  §2#p2: [104, 105, 106, 109, 110, 111, 121, 123, 129, 131, 139]
  §2#p4: [4, 37]
  §2#p7: [37, 48]
  §2#p8: [63, 74]
  §2#p9: [22, 29]
  §4.1#r289: [84, 89]
  §4.3#r5: [12, 13, 14, 15]
  §4.8#r1: [2, 4]
  §4.8#r2: [5, 7]
  §4.8#r3: 9
  §4.8#r4: [12, 104]
  §4.8#r5: [13, 15]
  §4.8#r6: 16
  §4.8#r7: [17, 105]
  §4.8#r8: [18, 106]
  §4.8#r9: [21, 109]
  §4.8#r10: [22, 110]
  §4.8#r11: [23, 111]
  §4.8#r12: [77, 84, 89, 93, 95, 96, 98, 123, 147, 150, 154, 158]
  §4.8#p2: [86, 91, 152]
  §9.4.2#r23: 22
  §9.4.2#r30: [84, 86, 152]
  §9.4.4#r24: 22
  §9.4.4#r25: 84
  §9.11#r2: [84, 89, 150]
  EB-AKS-5@add-override: [37, 48, 63]
  EB-AKS-5@delete-override: 82
  §9.3#b1: [22, 29]
  §9.11#r6: 48
  §9.11#r9: [55, 63, 147]
  §4.1#r288: [77, 123, 147]
anchor: [27, 53, 81]
coverage:
  web: automated
---
# Gating Manage asset & TAG (Read + Update) dan Group Manager

## Prerequisites
- Aktor: pemegang Group Role Manage asset & TAG (Read, Update) `Andi Prasetyo {runId}` dan Group Manager `Gita Maharani {runId}`.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-035-1: User `Andi Prasetyo {runId}`, Group Role Manage asset & TAG (Read, Update) pada Group `Proyek Karawang {runId}` beserta Group turunannya, tanpa Global Role Manage transaction settings, bukan Total Control, ada di entitas aktor.
  - DU-035-2: User `Gita Maharani {runId}`, Group Manager pada Group `Gudang Pusat {runId}` beserta Group turunannya, tanpa Global Role Manage transaction settings, bukan Total Control, ada di entitas aktor.
  - DU-035-3: Group `Proyek Karawang {runId}`.
  - DU-035-4: Group `Workshop {runId}`, Group turunan dari `Proyek Karawang {runId}`.
  - DU-035-5: Group `Proyek Bekasi {runId}`, di luar cakupan `Andi Prasetyo {runId}` dan `Gita Maharani {runId}`.
  - DU-035-6: Group `Gudang Pusat {runId}`.
  - DU-035-7: Category leaf `Alat Angkat {runId}` di bawah Category induk `Peralatan {runId}`; pada tab Borrow, field `Max duration` bernilai sendiri `15` dan field `Max extensions` Inherit, dibuat oleh aktor lain.
  - DU-035-8: Asset Name `Crane Tadano {runId}`, aktif.
  - DU-035-9: Aset `Crane Tadano - 1 {runId}` di Group `Proyek Karawang {runId}`, Asset Name DU-035-8, Category `Alat Angkat {runId}`, status bukan Disposed.
  - DU-035-10: Aset `Crane Tadano - 2 {runId}` di Group `Workshop {runId}`, Asset Name DU-035-8, Category `Alat Angkat {runId}`, status bukan Disposed.
  - DU-035-11: Aset `Crane Tadano - 3 {runId}` di Group `Proyek Bekasi {runId}`, Asset Name DU-035-8, Category `Alat Angkat {runId}`, status bukan Disposed.
  - DU-035-12: override pada tab Borrow Category `Alat Angkat {runId}` dengan Scope `Group`, Target `Proyek Bekasi {runId}`, Overridden `Max duration (30 days)`, dibuat oleh aktor lain.
  - DU-035-13: override pada tab Borrow Category `Alat Angkat {runId}` dengan Scope `Asset Name`, Target `Crane Tadano {runId}`, Overridden `Max duration (10 days)`, dibuat oleh aktor lain.
  - DU-035-19: Group `Gudang Timur {runId}`, Group turunan dari `Gudang Pusat {runId}`.
  - DU-035-20: override pada tab Borrow Category `Alat Angkat {runId}` dengan Scope `Asset`, Target `Crane Tadano - 3 {runId}`, Overridden `Max duration (30 days)`, dibuat oleh aktor lain.
- Kondisi:
  - Akun `Andi Prasetyo {runId}` dan `Gita Maharani {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Pemegang Manage asset & TAG (Read + Update) melihat halaman dan header
1. Ketik Search Sidebar Category Tree `Alat Angkat {runId}`, tekan Enter
2. Verifikasi Sidebar Category Tree menampilkan `All categories` dan Category `Alat Angkat {runId}`
3. Klik Category `Alat Angkat {runId}`
4. Verifikasi tab `Borrow`, `Assign`, `Transfer`, dan `Disposal` tampil
5. Verifikasi tombol `[Export rules]` tampil dan aktif
6. Klik `[Export rules]`
7. Verifikasi berkas aturan terunduh langsung tanpa dialog
8. Klik ikon `Changelog` pada header halaman
9. Verifikasi dialog `Changelog: Transaction Settings` tampil
10. Klik `✕` pada dialog Changelog

### Kontrol field disabled dan tombol Set own value serta Reset to inherit tidak dirender
11. Klik tab `Borrow`
12. Verifikasi kontrol field `Max duration` disabled dengan nilai `15`
13. Verifikasi tombol `[Reset to inherit]` tidak dirender pada field `Max duration`
14. Verifikasi field `Max extensions` menampilkan teks `Inherit` beserta sumbernya
15. Verifikasi tombol `[Set own value]` tidak dirender pada field `Max extensions`
16. Verifikasi tombol `[Reset to Default]` tampil dan disabled
17. Verifikasi tombol `[Save]` tampil dan disabled

### Opsi Scope di Dialog Add override sesuai cakupan Group
18. Verifikasi tombol `[+ Override]` tampil dan aktif
19. Klik `[+ Override]`
20. Klik pilihan Scope
21. Verifikasi opsi Scope `Group` tampil dan aktif
22. Verifikasi opsi Scope `Asset Name` disabled
23. Verifikasi opsi Scope `Asset` tampil dan aktif
24. Pilih Scope `Group`
25. Klik `[Select Group]`
26. Ketik Search `Proyek Karawang {runId}`, tekan Enter
27. Verifikasi Group `Proyek Karawang {runId}` tampil di dialog Select Group
28. Ganti isi kotak search dengan `Proyek Bekasi {runId}`, tekan Enter
29. Verifikasi `No results found` tampil di dialog Select Group

### Pemegang Group Role menambah override Group Proyek Karawang
30. Ganti isi kotak search dengan `Proyek Karawang {runId}`, tekan Enter
31. Centang Group `Proyek Karawang {runId}`
32. Klik `[Select]`
33. Pilih Field `Max duration`
34. Isi Value `30`
35. Klik `[Submit]`
36. Ketik Search tabel Overrides `Proyek Karawang {runId}`, tekan Enter
37. Verifikasi baris dengan Scope `Group`, Target `Proyek Karawang {runId}`, dan Overridden `Max duration (30 days)` tampil

### Pemegang Group Role menambah override Group turunan Workshop
38. Klik `[+ Override]`
39. Pilih Scope `Group`
40. Klik `[Select Group]`
41. Ketik Search `Workshop {runId}`, tekan Enter
42. Centang Group `Workshop {runId}`
43. Klik `[Select]`
44. Pilih Field `Max duration`
45. Isi Value `20`
46. Klik `[Submit]`
47. Ganti isi kotak search tabel Overrides dengan `Workshop {runId}`, tekan Enter
48. Verifikasi baris dengan Scope `Group`, Target `Workshop {runId}`, dan Overridden `Max duration (20 days)` tampil

### Pemegang Group Role menambah override Asset hanya untuk aset di Group-nya
49. Klik `[+ Override]`
50. Pilih Scope `Asset`
51. Klik `[Select Asset]`
52. Ketik Search `Crane Tadano - 1 {runId}`, tekan Enter
53. Verifikasi aset `Crane Tadano - 1 {runId}` tampil di dialog Select Asset
54. Ganti isi kotak search dengan `Crane Tadano - 3 {runId}`, tekan Enter
55. Verifikasi `No results found` tampil di dialog Select Asset
56. Ganti isi kotak search dengan `Crane Tadano - 1 {runId}`, tekan Enter
57. Centang baris `Crane Tadano - 1 {runId}`
58. Klik `[Select]`
59. Pilih Field `Max duration`
60. Isi Value `30`
61. Klik `[Submit]`
62. Ketik Search tabel Overrides `Crane Tadano - 1 {runId}`, tekan Enter
63. Verifikasi baris dengan Scope `Asset`, Target berisi `Crane Tadano - 1 {runId}`, dan Overridden `Max duration (30 days)` tampil

### Pemegang Group Role menambah override Asset untuk aset di Group turunan
64. Klik `[+ Override]`
65. Pilih Scope `Asset`
66. Klik `[Select Asset]`
67. Ketik Search `Crane Tadano - 2 {runId}`, tekan Enter
68. Centang baris `Crane Tadano - 2 {runId}`
69. Klik `[Select]`
70. Pilih Field `Max duration`
71. Isi Value `30`
72. Klik `[Submit]`
73. Ganti isi kotak search tabel Overrides dengan `Crane Tadano - 2 {runId}`, tekan Enter
74. Verifikasi baris dengan Scope `Asset`, Target berisi `Crane Tadano - 2 {runId}`, dan Overridden `Max duration (30 days)` tampil

### Pemegang Group Role menghapus override Group turunan di cakupannya
75. Ganti isi kotak search tabel Overrides dengan `{runId}`, tekan Enter
76. Klik menu `⋯` pada baris `Workshop {runId}`
77. Verifikasi item `Delete` aktif untuk baris override dengan Scope `Group` di dalam cakupan
78. Klik item `Delete`
79. Klik `[Delete]` pada dialog Delete Override
80. Ganti isi kotak search tabel Overrides dengan `{runId}`, tekan Enter
81. Verifikasi baris dengan Scope `Group` dan Target `Proyek Karawang {runId}` tampil
82. Verifikasi baris dengan Scope `Group` dan Target `Workshop {runId}` tidak tampil di tabel Overrides

### Delete override dan checkbox seleksi di luar cakupan Group disabled dengan alasan
83. Klik menu `⋯` pada baris `Proyek Bekasi {runId}`
84. Verifikasi item `Delete` disabled untuk baris override dengan Scope `Group` di luar cakupan
85. Arahkan kursor ke item `Delete`
86. Verifikasi alasan `This override is outside your scope.` tersampaikan pada item `Delete` yang disabled
87. Tekan Esc untuk menutup menu baris
88. Klik menu `⋯` pada baris `Crane Tadano {runId}`
89. Verifikasi item `Delete` disabled untuk baris override dengan Scope `Asset Name`
90. Arahkan kursor ke item `Delete`
91. Verifikasi alasan `This override is outside your scope.` tersampaikan pada item `Delete` yang disabled
92. Tekan Esc untuk menutup menu baris
93. Verifikasi checkbox seleksi pada baris `Proyek Bekasi {runId}` disabled[^drift-1]
94. Arahkan kursor ke checkbox seleksi pada baris `Proyek Bekasi {runId}`
95. Verifikasi alasan `You don't have permission to do this.` tersampaikan pada checkbox seleksi yang disabled[^drift-1]
96. Verifikasi checkbox seleksi pada baris `Crane Tadano {runId}` disabled[^drift-1]
97. Arahkan kursor ke checkbox seleksi pada baris `Crane Tadano {runId}`
98. Verifikasi alasan `You don't have permission to do this.` tersampaikan pada checkbox seleksi yang disabled[^drift-1]

### Group Manager mengikuti hak Manage asset & TAG pada Group penugasannya
99. Keluar dari akun `Andi Prasetyo {runId}`
100. Masuk sebagai `Gita Maharani {runId}`
101. Ketik Search Sidebar Category Tree `Alat Angkat {runId}`, tekan Enter
102. Klik Category `Alat Angkat {runId}`
103. Klik tab `Borrow`
104. Verifikasi kontrol field `Max duration` disabled dengan nilai `15`
105. Verifikasi tombol `[Save]` tampil dan disabled
106. Verifikasi tombol `[+ Override]` tampil dan aktif
107. Klik `[+ Override]`
108. Klik pilihan Scope
109. Verifikasi opsi Scope `Group` tampil dan aktif
110. Verifikasi opsi Scope `Asset Name` disabled
111. Verifikasi opsi Scope `Asset` tampil dan aktif
112. Pilih Scope `Group`
113. Klik `[Select Group]`
114. Ketik Search `Gudang Pusat {runId}`, tekan Enter
115. Centang Group `Gudang Pusat {runId}`
116. Klik `[Select]`
117. Pilih Field `Max duration`
118. Isi Value `25`
119. Klik `[Submit]`
120. Ketik Search tabel Overrides `Gudang Pusat {runId}`, tekan Enter
121. Verifikasi baris dengan Scope `Group`, Target `Gudang Pusat {runId}`, dan Overridden `Max duration (25 days)` tampil
122. Klik menu `⋯` pada baris `Gudang Pusat {runId}`
123. Verifikasi item `Delete` aktif untuk baris override dengan Scope `Group` di dalam cakupan
124. Tekan Esc untuk menutup menu baris

### Group Manager memilih Group hanya dalam subtree penugasannya
125. Klik `[+ Override]`
126. Pilih Scope `Group`
127. Klik `[Select Group]`
128. Ketik Search `Gudang Timur {runId}`, tekan Enter
129. Verifikasi Group `Gudang Timur {runId}` tampil di dialog Select Group
130. Ganti isi kotak search dengan `Proyek Bekasi {runId}`, tekan Enter
131. Verifikasi `No results found` tampil di dialog Select Group
132. Ganti isi kotak search dengan `Gudang Timur {runId}`, tekan Enter
133. Centang Group `Gudang Timur {runId}`
134. Klik `[Select]`
135. Pilih Field `Max duration`
136. Isi Value `18`
137. Klik `[Submit]`
138. Ketik Search tabel Overrides `Gudang Timur {runId}`, tekan Enter
139. Verifikasi baris dengan Scope `Group`, Target `Gudang Timur {runId}`, dan Overridden `Max duration (18 days)` tampil

### Pemegang Group Role: Delete override Asset aktif di Group-nya dan disabled di luar Group
140. Keluar dari akun `Gita Maharani {runId}`
141. Masuk sebagai `Andi Prasetyo {runId}`
142. Ketik Search Sidebar Category Tree `Alat Angkat {runId}`, tekan Enter
143. Klik Category `Alat Angkat {runId}`
144. Klik tab `Borrow`
145. Ketik Search tabel Overrides `{runId}`, tekan Enter
146. Klik menu `⋯` pada baris `Crane Tadano - 1 {runId}`
147. Verifikasi item `Delete` aktif untuk baris override dengan Scope `Asset` di Group pengguna
148. Tekan Esc untuk menutup menu baris
149. Klik menu `⋯` pada baris `Crane Tadano - 3 {runId}`
150. Verifikasi item `Delete` disabled untuk baris override dengan Scope `Asset` di luar Group pengguna
151. Arahkan kursor ke item `Delete`
152. Verifikasi alasan `This override is outside your scope.` tersampaikan pada item `Delete` yang disabled
153. Tekan Esc untuk menutup menu baris
154. Verifikasi checkbox seleksi pada baris `Crane Tadano - 3 {runId}` disabled[^drift-1]
155. Centang baris `Proyek Karawang {runId}`
156. Centang baris `Crane Tadano - 1 {runId}`
157. Klik tombol aksi bulk pada toolbar tabel Overrides
158. Verifikasi aksi bulk `Delete` aktif
159. Tekan Esc untuk menutup menu aksi bulk

[^drift-1]: Drift PRD vs foundation. PRD §4.8 (sel Delete baris dan bulk) dan §4.1 DO-15: baris di luar hak dapat dicentang lalu aksi bulk `Delete` disabled dengan tooltip tersendiri. foundation `functions/entity-isolation.md` §18.4 Aturan kolom 4: checkbox seleksi pada baris yang capability tulisnya tidak cukup Disabled 🔖 dengan tooltip `You don't have permission to do this.`, sehingga baris itu tidak bisa dicentang. Diasersi: foundation, karena checkbox seleksi tabel adalah pola bersama (SB-4).
