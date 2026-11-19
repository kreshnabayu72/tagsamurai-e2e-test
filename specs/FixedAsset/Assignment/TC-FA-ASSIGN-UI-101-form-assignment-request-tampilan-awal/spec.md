---
id: TC-FA-ASSIGN-UI-101-form-assignment-request-tampilan-awal
title: "Form Assignment Request: tampilan awal, tipe Assignee, dan Purpose per aset"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.3#p1", "§4.2.3#p2", "§4.2.3#p3", "§4.2.3#p4", "§4.2.3#b1", "§4.2.3#b2", "§4.2.3#b3", "§4.2.3#b4", "§4.2.3#b5", "§4.2.3#b6", "§4.2.3#b7", "§4.2.3#b8", "§4.2.3#b9", "§4.2.3#b10", "§4.2.3#b11", "§4.2.3#b12", "§4.2.3#b13", "§4.2.3#b14", "§4.2.3#b15", "§4.2.3#b16", "§4.2.3#b17", "§4.1#r6", "FI-ASG-01", "FI-ASG-02", "FI-ASG-03", "FI-ASG-04", "S-ASG-04", "S-ASG-03", "FLD-ASG-04", "FLD-ASG-05", "§4.4#r1", "§4.4#r2", "§9.5#r11", "§10#r3", "ASSIGN-LOGIC-01e", "ASSIGN-LOGIC-01f", "ASSIGN-LOGIC-01g", "ASSIGN-LOGIC-01n"]
smoke: []
dependsOn: []
trace:
  "§4.2.3#p1": [3, 4, 5, 6, 13, 14, 15, 16, 17, 18, 20, 21, 23, 26, 28, 29, 31, 33, 35, 37, 39, 40, 42, 45, 46, 47, 93, 96, 98, 107, 110, 112, 114, 116, 118, 119, 124, 127, 130, 137, 141, 173, 184, 211, 212, 215, 216, 221, 222, 225, 227, 229, 231, 236, 239, 242, 245, 248, 249, 251, 253]
  "§4.2.3#p2": [144, 189, 194, 198, 202, 206]
  "§4.2.3#p3": [52, 79]
  "§4.2.3#p4": 8
  "§4.2.3#b1": 145
  "§4.2.3#b2": [146, 195, 199, 203, 207, 208]
  "§4.2.3#b3": [10, 11, 156]
  "§4.2.3#b4": [12, 27, 90]
  "§4.2.3#b5": [79, 168, 174]
  "§4.2.3#b6": 102
  "§4.2.3#b7": [62, 63, 64]
  "§4.2.3#b8": 137
  "§4.2.3#b9": 141
  "§4.2.3#b10": [107, 108]
  "§4.2.3#b11": [65, 66, 146, 190, 191]
  "§4.2.3#b12": [149, 152]
  "§4.2.3#b13": [133, 134, 177, 256, 257, 260, 261]
  "§4.2.3#b14": [48, 49, 50]
  "§4.2.3#b15": 162
  "§4.2.3#b16": [159, 160]
  "§4.2.3#b17": 106
  "§4.1#r6": 8
  "FI-ASG-01": [61, 65, 66, 71]
  "FI-ASG-02": 79
  "FI-ASG-03": [84, 89, 168, 173, 174]
  "FI-ASG-04": [102, 103, 104]
  "S-ASG-04": [7, 62, 185, 186]
  "S-ASG-03": [137, 138]
  "FLD-ASG-04": [9, 178, 182]
  "FLD-ASG-05": 106
  "§4.4#r1": [29, 65]
  "§4.4#r2": [53, 65, 72, 73]
  "§9.5#r11": [79, 84, 102, 164, 168, 174]
  "§10#r3": 27
  "ASSIGN-LOGIC-01e": 27
  "ASSIGN-LOGIC-01f": [79, 90]
  "ASSIGN-LOGIC-01g": 12
  "ASSIGN-LOGIC-01n": [84, 102, 168, 174]
anchor: [2, 44, 54, 78, 92, 181]
coverage:
  web: automated
---

# Form Assignment Request: tampilan awal, tipe Assignee, dan Purpose per aset

## Prerequisites
- Aktor: Aktor Assignment.
- Layar awal: halaman Assignment Request pada level Full.
- Komponen: Form Assignment Request
- Data:
  - DU-101-1: Assignee Employee `Dewi Kartika`, Email `dewi.kartika@example.com`, Position `Staff`, Division `IT`, Home Group `Head Office`, Active Assignments `0 assets`.
  - DU-101-2: Assignee Division `Finance`, Code `FIN`, Users `4`.
  - DU-101-3: PIC `Sari Dewi`, Email `sari.dewi@example.com`, anggota aktif ber-akun login Division `Finance`.
  - DU-101-4: Aset `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`.
  - DU-101-5: Aset `Laptop Dell Latitude 5420 - 11`, Asset ID `LPT-2026-0011`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`.
  - DU-101-6: Aset `Toyota Avanza - 6`, Asset ID `VEH-2026-0006`, Group `Branch Surabaya`, Approval Rule `Needs approval`, Confirmation Rule `Yes`.
  - DU-101-7: Aset `Printer HP M404 - 3`, Asset ID `PRN-2026-0003`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `No`, tidak boleh ditugaskan ke Division.
  - DU-101-11: Draft tersimpan dengan Assignee `Dewi Kartika`, Note `Peminjaman untuk proyek kantor cabang`, aset DU-101-4 ber-Purpose `Operasional kantor pusat`, terakhir diubah oleh `Rina Wulandari`.
  - DU-101-12: 1 Draft lain milik `Dewi Kartika` yang bisa diedit.
  - DU-101-13: 2 Draft lain milik `Dewi Kartika` yang bisa diedit, dengan pola `Draft lain {n}`.
  - DU-101-14: Max assets per assignee efektif `5`.
  - DU-101-15: Max assets per assignee efektif `3`.
  - DU-101-16: Max assets per assignee efektif `0`.
  - DU-101-19: Teks blok Approval yang diharapkan, dari nama aset DU-101-4 dan DU-101-6: `No approval needed: Laptop Dell Latitude 5420 - 10.` dan `Needs approval: Toyota Avanza - 6.`.
  - DU-101-17: Aset `Excavator PC200 - 4`, Asset ID `EXC-2026-0010`, Group `Branch Bandung` yang berada di luar cakupan Aktor Assignment.
  - DU-101-20: Max assets per assignee efektif `5` dengan cakupan hitung Category yang sama, yaitu Category `Laptop`, untuk DU-101-4 dan DU-101-5 yang keduanya ber-Category `Laptop`.
  - DU-101-21: PIC `Budi Hartono`, Email `budi.hartono@example.com`, anggota aktif ber-akun login Division `Finance`.
  - DU-101-22: Aturan approval Group `Branch Surabaya` untuk DU-101-6: `No approval` saat aset ditambahkan, `Needs approval` saat Submit. Teks blok Approval yang diharapkan bila DU-101-6 tidak memerlukan approval: `No approval needed: Toyota Avanza - 6.`.
  - DU-101-23: Approver tunggal `Hendra Pratama` untuk Group `Branch Surabaya`.
  - DU-101-24: Dua approver `Hendra Pratama` dan `Maya Lestari` untuk Group `Branch Surabaya`, Approval type `Any one approver`.
  - DU-101-25: Dua approver `Hendra Pratama` dan `Maya Lestari` untuk Group `Branch Surabaya`, Approval type `All approvers`.
  - DU-101-26: Group `Branch Surabaya` dan ancestor-nya tanpa pemegang Role Transaksi `Approver`; hanya Total Control yang dapat memutuskan.
- Kondisi:
  - K1: form baru dibuka dari pilihan overlay `Employee`; Assignee belum dipilih dan tabel aset kosong.
  - K2: form dibuka tanpa overlay dari Asset List dengan aset DU-101-4; Assignee belum dipilih; dialog Select Assignee memuat DU-101-1 dan DU-101-2; Max assets per assignee bernilai DU-101-16.
  - K3: Assignee DU-101-1 sudah dipilih dan tidak memegang aset aktif lain; form berisi aset DU-101-4; Max assets per assignee bernilai DU-101-14 lintas Category.
  - K4: seperti K3, form berisi aset DU-101-4, DU-101-5, dan DU-101-6.
  - K5: seperti K4, Max assets per assignee bernilai DU-101-16 untuk ketiga aset.
  - K6: seperti K4, Max assets per assignee bernilai DU-101-14 untuk DU-101-4 dan DU-101-5, dan DU-101-15 untuk DU-101-6.
  - K7: Assignee DU-101-1 dipilih dan memiliki DU-101-12.
  - K8: Assignee DU-101-1 dipilih dan memiliki DU-101-13.
  - K9: Edit draft dibuka dengan DU-101-11.
  - K10: form dibuka tanpa overlay dengan aset DU-101-4 dan DU-101-7; Assignee DU-101-1 sudah dipilih; dialog Select Assignee memuat DU-101-1 dan DU-101-2; dialog Select User memuat DU-101-3; Max assets per assignee bernilai DU-101-16.
  - K11: Assignee DU-101-1 dipilih; tabel berisi aset DU-101-6, DU-101-5, dan DU-101-4 menurut urutan data itu; Max assets per assignee bernilai DU-101-16.
  - K12: Assignee DU-101-1 dipilih; tabel aset kosong; dialog Select Asset memuat DU-101-4, DU-101-5, dan DU-101-6; Max assets per assignee bernilai DU-101-16.
  - K13: Assignee DU-101-1 dipilih; tabel berisi DU-101-4 ber-Purpose `Operasional kantor pusat`, DU-101-5 dan DU-101-6 ber-Purpose `Survei lapangan Surabaya`; Max assets per assignee bernilai DU-101-16.
  - K14: Assignee DU-101-1 dipilih; hasil pindai tag adalah tag yang tidak dikenali.
  - K15: Assignee DU-101-1 dipilih; tabel berisi DU-101-4 dengan Purpose kosong; simpan draft berhasil.
  - K16: Assignee DU-101-1 dipilih; tabel berisi DU-101-4 ber-Purpose `Operasional kantor pusat` dan DU-101-7 yang tidak lagi layak untuk ditugaskan.
  - K17: Assignee DU-101-1 dipilih; tabel berisi DU-101-4 ber-Purpose `Operasional kantor pusat` dan DU-101-6 ber-Purpose `Survei lapangan Surabaya`, keduanya layak.
  - K18: Assignee DU-101-1 dipilih; tabel berisi DU-101-4 ber-Purpose `Operasional kantor pusat`; jumlah baris pada form melebihi Bulk Transaction Row Limit yang berlaku; simpan draft berhasil.
  - K19: Edit draft dibuka dengan DU-101-11; draft sudah diubah orang lain sejak dibuka, sehingga simpan ditolak karena versi draft berubah.
  - K20: Assignee DU-101-1 dipilih; tabel berisi DU-101-17.
  - K21: Assignee DU-101-1 dipilih; tabel berisi DU-101-4 ber-Purpose `Operasional kantor pusat` dan DU-101-5 ber-Purpose kosong; dialog Select Asset memuat DU-101-6; Max assets per assignee bernilai DU-101-16.
  - K22: Assignee DU-101-1 dipilih; tabel berisi DU-101-4 ber-Purpose `Operasional kantor pusat`; hasil pindai tag adalah tag DU-101-6 yang dikenali; Max assets per assignee bernilai DU-101-16.
  - K23: Assignee DU-101-1 dipilih; Note kosong; tabel berisi DU-101-4 dengan Purpose kosong; simpan draft berhasil.
  - K24: form baru dibuka dari pilihan overlay `Division`; Assignee belum dipilih.
  - K25: Assignee DU-101-1 dipilih; tabel berisi DU-101-6 ber-Purpose `Survei lapangan Surabaya` dengan aturan approval DU-101-22.
  - K26: Assignee DU-101-1 dipilih; tabel berisi DU-101-6 ber-Purpose `Survei lapangan Surabaya` dengan approver DU-101-23.
  - K27: Assignee DU-101-1 dipilih; tabel berisi DU-101-6 ber-Purpose `Survei lapangan Surabaya` dengan approver DU-101-24.
  - K28: Assignee DU-101-1 dipilih; tabel berisi DU-101-6 ber-Purpose `Survei lapangan Surabaya` dengan approver DU-101-25.
  - K29: Assignee DU-101-1 dipilih; tabel berisi DU-101-6 ber-Purpose `Survei lapangan Surabaya` dengan approver DU-101-26.
  - K30: Assignee DU-101-1 dipilih dan tidak memegang aset aktif lain; form berisi DU-101-4, DU-101-5, dan DU-101-6; Max assets per assignee bernilai DU-101-14 untuk ketiga aset, dengan cakupan hitung DU-101-20 untuk DU-101-4 dan DU-101-5 dan lintas Category untuk DU-101-6.
  - K31: Assignee DU-101-1 dipilih dan tidak memegang aset aktif lain; form berisi DU-101-4 dan DU-101-5; Max assets per assignee bernilai DU-101-20.
  - K32: Assignee DU-101-2 dipilih dan PIC DU-101-3 sudah dipilih; tabel berisi DU-101-4; dialog Select User memuat DU-101-3 dan DU-101-21.
  - K33: Assignee DU-101-1 dipilih; tabel aset kosong; simpan draft berhasil.
  - K34: Assignee DU-101-1 dipilih; tabel berisi DU-101-4 (Group `Head Office`) dan DU-101-6 (Group `Branch Surabaya`) dengan Purpose kosong; simpan draft berhasil.

## Test Steps

### Tampilan awal form baru dari overlay Employee
1. Tampilkan Form Assignment Request dengan kondisi K1
2. Verifikasi isian Assignee tampil
3. Verifikasi tidak ada badge `Draft`
4. Verifikasi badge `Employee` tampil pada Assignee Type
5. Verifikasi tombol `[Select Assignee]` tampil
6. Verifikasi field `Assignee` ditandai wajib
7. Verifikasi field PIC tidak tampil
8. Verifikasi isian Assignee, Note, tabel aset, serta aksi `[Cancel]`, `[Save Draft]`, dan `[Submit]` tampil
9. Verifikasi placeholder `Enter note` tampil pada Note
10. Verifikasi tidak ada tombol `[Clear Field]`
11. Verifikasi tidak ada checkbox `Stay on this form after submitting`
12. Verifikasi form tidak memuat isian `Duration` maupun `Due date`, kontrol `Extend`, dan penanda `Overdue`
13. Verifikasi placeholder `Search asset name or ID...` tampil pada Search aset
14. Verifikasi Filter Group tampil pada toolbar aset
15. Verifikasi tombol `[Add by Scan]` dan `[+ Asset]` tampil
16. Verifikasi header kolom `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Approval Rule`, `Confirmation Rule`, `Purpose`, dan `Action` tampil
17. Verifikasi `No assets added` tampil pada badan tabel
18. Verifikasi `Add the assets to assign to this assignee.` tampil pada badan tabel

### Memilih Assignee Employee tanpa overlay
19. Tampilkan Form Assignment Request dengan kondisi K2
20. Verifikasi tombol `[Select Assignee]` tampil
21. Verifikasi badge `Employee` dan `Division` tidak tampil
22. Klik `[Select Assignee]`
23. Verifikasi dialog Select Assignee memuat sub-tab `Employees` dan `Divisions`
24. Pilih Assignee `Dewi Kartika` pada dialog Select Assignee
25. Konfirmasi pilihan pada dialog Select Assignee
26. Verifikasi tombol Assignee menampilkan nama `Dewi Kartika`
27. Verifikasi form hanya memiliki satu isian Assignee
28. Verifikasi badge `Employee` tampil pada Assignee Type
29. Verifikasi teks bantu `1 asset assigned` tampil pada Assignee

### Teks bantu jumlah aset dengan batas Max assets per assignee
30. Tampilkan Form Assignment Request dengan kondisi K3
31. Verifikasi teks bantu `1 of 5 assigned` tampil pada Assignee
32. Tampilkan Form Assignment Request dengan kondisi K4
33. Verifikasi teks bantu `3 of 5 assigned` tampil pada Assignee
34. Tampilkan Form Assignment Request dengan kondisi K5
35. Verifikasi teks bantu `3 assets assigned` tampil pada Assignee
36. Tampilkan Form Assignment Request dengan kondisi K6
37. Verifikasi teks bantu `3 assets assigned` tampil pada Assignee

### Info Draft lain milik Assignee
38. Tampilkan Form Assignment Request dengan kondisi K7
39. Verifikasi `Dewi Kartika has 1 other draft.` tampil
40. Verifikasi tombol `[Open]` tampil
41. Tampilkan Form Assignment Request dengan kondisi K8
42. Verifikasi `Dewi Kartika has 2 other drafts.` tampil

### Edit draft membuka form dengan nilai tersimpan
43. Tampilkan Form Assignment Request dengan kondisi K9
44. Verifikasi isian Assignee tampil
45. Verifikasi teks `Last modified by` diikuti nama `Rina Wulandari` dan waktu perubahan terakhir draft tampil
46. Verifikasi tidak ada badge `Draft`
47. Verifikasi badge `Employee` tampil pada Assignee Type
48. Verifikasi Assignee `Dewi Kartika` terisi dengan nilai tersimpan
49. Verifikasi Note `Peminjaman untuk proyek kantor cabang` terisi dengan nilai tersimpan
50. Verifikasi Purpose `Operasional kantor pusat` terisi pada baris `Laptop Dell Latitude 5420 - 10`

### Mengganti tipe Assignee Employee dan Division
51. Tampilkan Form Assignment Request dengan kondisi K10
52. Verifikasi badge `Employee` tampil pada Assignee Type
53. Verifikasi field PIC tidak tampil
54. Verifikasi baris `Laptop Dell Latitude 5420 - 10` dan `Printer HP M404 - 3` tampil tanpa ikon ⚠
55. Klik tombol Assignee `Dewi Kartika`
56. Klik sub-tab `Divisions`
57. Pilih `Finance` pada sub-tab `Divisions`
58. Konfirmasi pilihan pada dialog Select Assignee
59. Pilih PIC `Sari Dewi` pada dialog Select User
60. Konfirmasi pilihan pada dialog Select User
61. Verifikasi badge `Division` tampil pada Assignee Type
62. Verifikasi field `PIC` tampil dan ditandai wajib
63. Verifikasi nama `Sari Dewi` tampil pada tombol PIC
64. Verifikasi `The PIC accepts the assets and receives notifications.` tampil pada PIC
65. Verifikasi baris `Printer HP M404 - 3` ditandai ikon ⚠
66. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tidak ditandai ikon ⚠
67. Klik tombol Assignee `Finance`
68. Klik sub-tab `Employees`
69. Pilih Assignee `Dewi Kartika` pada dialog Select Assignee
70. Konfirmasi pilihan pada dialog Select Assignee
71. Verifikasi badge `Employee` tampil pada Assignee Type
72. Verifikasi field PIC tidak tampil
73. Verifikasi baris `Printer HP M404 - 3` tidak ditandai ikon ⚠

### Purpose aset pertama kosong dan aset berikutnya mewarisi
74. Tampilkan Form Assignment Request dengan kondisi K12
75. Klik `[+ Asset]`
76. Centang aset `Laptop Dell Latitude 5420 - 10` pada dialog Select Asset
77. Klik `[Select]`
78. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tampil pada tabel aset
79. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 10` kosong dengan placeholder `Enter purpose`
80. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Operasional kantor pusat`
81. Klik `[+ Asset]`
82. Centang aset `Laptop Dell Latitude 5420 - 11` pada dialog Select Asset
83. Klik `[Select]`
84. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 11` berisi `Operasional kantor pusat`
85. Ganti Purpose baris `Laptop Dell Latitude 5420 - 11` dengan `Survei lapangan Surabaya`
86. Klik `[+ Asset]`
87. Centang aset `Toyota Avanza - 6` pada dialog Select Asset
88. Klik `[Select]`
89. Verifikasi Purpose baris `Toyota Avanza - 6` berisi `Survei lapangan Surabaya`
90. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 10` tetap `Operasional kantor pusat`

### Bulk Set Purpose menyamakan Purpose antar aset
91. Tampilkan Form Assignment Request dengan kondisi K13
92. Verifikasi baris `Laptop Dell Latitude 5420 - 10`, `Laptop Dell Latitude 5420 - 11`, dan `Toyota Avanza - 6` tampil
93. Verifikasi bar bulk tidak tampil sebelum ada baris yang dicentang
94. Centang baris `Laptop Dell Latitude 5420 - 10`
95. Centang baris `Toyota Avanza - 6`
96. Verifikasi bar bulk menampilkan `2 Assets selected`
97. Buka menu aksi pada bar bulk
98. Verifikasi menu aksi memuat `[Set Purpose]` dan `[Remove from List]`
99. Klik `[Set Purpose]`
100. Isi Purpose pada dialog Set Purpose dengan `Dinas luar kota`
101. Klik `[Apply to 2 assets]`
102. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 10` berisi `Dinas luar kota`
103. Verifikasi Purpose baris `Toyota Avanza - 6` berisi `Dinas luar kota`
104. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 11` tetap `Survei lapangan Surabaya`

### Isi baris tabel aset, sort Name, dan Remove from List
105. Tampilkan Form Assignment Request dengan kondisi K11
106. Verifikasi setiap aset tampil sebagai satu baris tabel
107. Verifikasi baris `Toyota Avanza - 6` menampilkan Asset ID `VEH-2026-0006`, Group `Branch Surabaya`, Approval Rule `Needs approval`, dan Confirmation Rule `Yes`
108. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Asset ID `LPT-2026-0010`, Group `Head Office`, Approval Rule `No approval`, dan Confirmation Rule `Yes`
109. Klik header `Name`
110. Verifikasi urutan baris: `Laptop Dell Latitude 5420 - 10`, `Laptop Dell Latitude 5420 - 11`, lalu `Toyota Avanza - 6`
111. Klik header `Name`
112. Verifikasi urutan baris: `Toyota Avanza - 6`, `Laptop Dell Latitude 5420 - 11`, lalu `Laptop Dell Latitude 5420 - 10`
113. Klik header `Purpose`
114. Verifikasi urutan baris tetap: `Toyota Avanza - 6`, `Laptop Dell Latitude 5420 - 11`, lalu `Laptop Dell Latitude 5420 - 10`
115. Klik ikon ⋯ pada baris `Laptop Dell Latitude 5420 - 11`
116. Verifikasi menu baris menyediakan `Remove from List`
117. Klik `Remove from List`
118. Verifikasi baris `Laptop Dell Latitude 5420 - 11` tidak lagi tampil dan baris `Toyota Avanza - 6` tetap tampil
119. Verifikasi tidak ada dialog konfirmasi yang tampil

### Bulk Remove from List mengeluarkan baris tercentang
120. Tampilkan Form Assignment Request dengan kondisi K11
121. Centang baris `Toyota Avanza - 6`
122. Buka menu aksi pada bar bulk
123. Klik `[Remove from List]`
124. Verifikasi baris `Toyota Avanza - 6` tidak lagi tampil dan baris `Laptop Dell Latitude 5420 - 10` tetap tampil

### Pindai tag yang tidak dikenali
125. Tampilkan Form Assignment Request dengan kondisi K14
126. Klik `[Add by Scan]`
127. Verifikasi overlay scan memuat pilihan `RFID`, `QR`, dan `NFC`
128. Pilih `QR` pada overlay scan
129. Pindai tag yang tidak dikenali
130. Verifikasi `Not recognized` tampil

### Save Draft hanya memerlukan Assignee
131. Tampilkan Form Assignment Request dengan kondisi K15
132. Klik `[Save Draft]`
133. Verifikasi toast `Success, assignment has been saved as draft.` tampil setelah Save Draft tanpa Purpose
134. Verifikasi tidak ada pesan error pada isian Purpose baris `Laptop Dell Latitude 5420 - 10`

### Submit gagal karena isian wajib kosong
135. Tampilkan Form Assignment Request dengan kondisi K15
136. Klik `[Submit]`
137. Verifikasi caption error `Please fill in all required fields.` tampil di atas tombol aksi
138. Verifikasi tidak ada dialog `Submit Assignment`

### Submit gagal karena ada aset tidak layak
139. Tampilkan Form Assignment Request dengan kondisi K16
140. Klik `[Submit]`
141. Verifikasi caption error `Remove the unavailable assets to continue.` tampil di atas tombol aksi

### Blok Approval pada dialog konfirmasi Submit
142. Tampilkan Form Assignment Request dengan kondisi K17
143. Klik `[Submit]`
144. Verifikasi dialog `Submit Assignment` tampil
145. Verifikasi `No approval needed: Laptop Dell Latitude 5420 - 10.` tampil pada blok Approval
146. Verifikasi `Needs approval: Toyota Avanza - 6.` tampil pada blok Approval

### Submit melebihi Bulk Transaction Row Limit
147. Tampilkan Form Assignment Request dengan kondisi K18
148. Klik `[Submit]`
149. Verifikasi dialog `Bulk Transaction Row Limit` tampil dengan tombol `[OK]`
150. Klik `[OK]`
151. Klik `[Save Draft]`
152. Verifikasi toast `Success, assignment has been saved as draft.` tampil tanpa dialog `Bulk Transaction Row Limit`

### Meninggalkan form kotor lewat Cancel
153. Tampilkan Form Assignment Request dengan kondisi K1
154. Isi Note dengan `Dipakai untuk kegiatan survei`
155. Klik `[Cancel]`
156. Verifikasi dialog `Unsaved Changes` tampil

### Draft diubah orang lain sejak dibuka
157. Tampilkan Form Assignment Request dengan kondisi K19
158. Klik `[Save Draft]`
159. Verifikasi dialog `Draft Changed` tampil dengan tombol `[Cancel]` dan `[Reload]`
160. Verifikasi `Reload to see the latest version; your unsaved changes will be lost.` tampil pada dialog

### Baris aset di luar cakupan pengguna
161. Tampilkan Form Assignment Request dengan kondisi K20
162. Verifikasi baris `Excavator PC200 - 4` menampilkan `Outside your groups`

### Purpose diwarisi dari baris terakhir yang terisi lewat dialog Select Asset
163. Tampilkan Form Assignment Request dengan kondisi K21
164. Verifikasi placeholder `Enter purpose` tampil pada Purpose baris `Laptop Dell Latitude 5420 - 11`
165. Klik `[+ Asset]`
166. Centang aset `Toyota Avanza - 6` pada dialog Select Asset
167. Klik `[Select]`
168. Verifikasi Purpose baris `Toyota Avanza - 6` berisi `Operasional kantor pusat`

### Purpose diwarisi dari baris terakhir yang terisi lewat pindai tag
169. Tampilkan Form Assignment Request dengan kondisi K22
170. Klik `[Add by Scan]`
171. Pilih `QR` pada overlay scan
172. Pindai tag aset `Toyota Avanza - 6`
173. Verifikasi baris `Toyota Avanza - 6` tampil pada tabel aset
174. Verifikasi Purpose baris `Toyota Avanza - 6` berisi `Operasional kantor pusat`

### Save Draft dengan Note kosong tidak menimbulkan error pada Note
175. Tampilkan Form Assignment Request dengan kondisi K23
176. Klik `[Save Draft]`
177. Verifikasi toast `Success, assignment has been saved as draft.` tampil untuk Save Draft ketika Note belum diisi
178. Verifikasi tidak ada pesan error pada isian Note

### Submit gagal dengan Note kosong tidak menimbulkan error pada Note
179. Tampilkan Form Assignment Request dengan kondisi K23
180. Klik `[Submit]`
181. Verifikasi caption error `Please fill in all required fields.` tampil di atas tombol aksi
182. Verifikasi tidak ada pesan error pada isian Note

### Field PIC disabled sampai Division dipilih
183. Tampilkan Form Assignment Request dengan kondisi K24
184. Verifikasi badge `Division` tampil pada Assignee Type
185. Verifikasi field `PIC` tampil
186. Verifikasi tombol `[Select PIC]` disabled

### Blok Approval dihitung dari kondisi saat Submit
187. Tampilkan Form Assignment Request dengan kondisi K25
188. Klik `[Submit]`
189. Verifikasi dialog `Submit Assignment` tampil
190. Verifikasi `Needs approval: Toyota Avanza - 6.` tampil pada blok Approval
191. Verifikasi `No approval needed: Toyota Avanza - 6.` tidak tampil pada blok Approval

### Blok Approval untuk aset dengan satu approver
192. Tampilkan Form Assignment Request dengan kondisi K26
193. Klik `[Submit]`
194. Verifikasi dialog `Submit Assignment` tampil
195. Verifikasi `Needs approval: Toyota Avanza - 6.` tampil pada blok Approval

### Blok Approval untuk aset dengan beberapa approver Any one approver
196. Tampilkan Form Assignment Request dengan kondisi K27
197. Klik `[Submit]`
198. Verifikasi dialog `Submit Assignment` tampil
199. Verifikasi `Needs approval: Toyota Avanza - 6.` tampil pada blok Approval

### Blok Approval untuk aset dengan beberapa approver All approvers
200. Tampilkan Form Assignment Request dengan kondisi K28
201. Klik `[Submit]`
202. Verifikasi dialog `Submit Assignment` tampil
203. Verifikasi `Needs approval: Toyota Avanza - 6.` tampil pada blok Approval

### Blok Approval untuk aset tanpa approver tetap Needs approval
204. Tampilkan Form Assignment Request dengan kondisi K29
205. Klik `[Submit]`
206. Verifikasi dialog `Submit Assignment` tampil
207. Verifikasi `Needs approval: Toyota Avanza - 6.` tampil pada blok Approval
208. Verifikasi `No approval needed: Toyota Avanza - 6.` tidak tampil pada blok Approval

### Search pada toolbar aset menyaring baris form
209. Tampilkan Form Assignment Request dengan kondisi K11
210. Ketik Search `Toyota Avanza - 6`, tekan Enter
211. Verifikasi baris `Toyota Avanza - 6` tampil pada tabel aset
212. Verifikasi baris `Laptop Dell Latitude 5420 - 10` dan `Laptop Dell Latitude 5420 - 11` tidak tampil pada tabel aset
213. Klik `(←)` pada kotak Search
214. Ketik Search `LPT-2026-0011`, tekan Enter
215. Verifikasi baris `Laptop Dell Latitude 5420 - 11` tampil pada tabel aset
216. Verifikasi baris `Laptop Dell Latitude 5420 - 10` dan `Toyota Avanza - 6` tidak tampil pada tabel aset

### Filter Group pada toolbar aset menyaring baris form
217. Tampilkan Form Assignment Request dengan kondisi K11
218. Buka Filter pada toolbar aset
219. Pilih `Branch Surabaya` pada Filter Group
220. Klik `[Apply]`
221. Verifikasi baris `Toyota Avanza - 6` tampil pada tabel aset
222. Verifikasi baris `Laptop Dell Latitude 5420 - 10` dan `Laptop Dell Latitude 5420 - 11` tidak tampil pada tabel aset
223. Pilih `Head Office` pada Filter Group
224. Klik `[Apply]`
225. Verifikasi baris `Laptop Dell Latitude 5420 - 10`, `Laptop Dell Latitude 5420 - 11`, dan `Toyota Avanza - 6` tampil pada tabel aset

### Kolom checkbox, Photo, pilih semua, dan bar bulk bentuk tunggal
226. Tampilkan Form Assignment Request dengan kondisi K11
227. Verifikasi kolom checkbox dengan pilih semua dan kolom `Photo` tampil pada header tabel aset
228. Centang baris `Toyota Avanza - 6`
229. Verifikasi bar bulk menampilkan `1 Asset selected`
230. Centang pilih semua pada header tabel aset
231. Verifikasi bar bulk menampilkan `3 Assets selected`

### Kolom opsional TAG dan Category lewat Setup Column
232. Tampilkan Form Assignment Request dengan kondisi K11
233. Buka Setup Column pada tabel aset
234. Centang kolom `TAG` pada Setup Column
235. Centang kolom `Category` pada Setup Column
236. Verifikasi header kolom `TAG` dan `Category` tampil pada tabel aset

### Open pada info satu Draft lain tidak menutup form
237. Tampilkan Form Assignment Request dengan kondisi K7
238. Klik `[Open]`
239. Verifikasi isian Assignee tetap tampil pada form

### Open pada info beberapa Draft lain tidak menutup form
240. Tampilkan Form Assignment Request dengan kondisi K8
241. Klik `[Open]`
242. Verifikasi isian Assignee tetap tampil pada form

### Mengganti PIC lewat tombol PIC
243. Tampilkan Form Assignment Request dengan kondisi K32
244. Klik tombol PIC `Sari Dewi`
245. Verifikasi dialog Select User tampil
246. Pilih PIC `Budi Hartono` pada dialog Select User
247. Konfirmasi pilihan pada dialog Select User
248. Verifikasi nama `Budi Hartono` tampil pada tombol PIC
249. Verifikasi nama `Sari Dewi` tidak tampil pada tombol PIC

### Teks bantu tanpa Max bila cakupan hitung aset berbeda
250. Tampilkan Form Assignment Request dengan kondisi K30
251. Verifikasi teks bantu `3 assets assigned` tampil pada Assignee

### Teks bantu dengan Max bila cakupan hitung Category yang sama
252. Tampilkan Form Assignment Request dengan kondisi K31
253. Verifikasi teks bantu `2 of 5 assigned` tampil pada Assignee

### Save Draft dengan tabel aset kosong
254. Tampilkan Form Assignment Request dengan kondisi K33
255. Klik `[Save Draft]`
256. Verifikasi toast `Success, assignment has been saved as draft.` tampil untuk Save Draft ketika belum ada aset pada tabel
257. Verifikasi tidak ada pesan error pada tabel aset

### Save Draft dengan aset dari dua Group
258. Tampilkan Form Assignment Request dengan kondisi K34
259. Klik `[Save Draft]`
260. Verifikasi toast `Success, assignment has been saved as draft.` tampil untuk Save Draft dengan aset dari dua Group
261. Verifikasi tidak ada dialog `Submit Assignment`
