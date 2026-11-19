---
id: TC-FA-BORROW-E2E-005-tab-borrowed-assets-by-asset
title: "Tab Borrowed Assets By Asset menampilkan baris Borrowed dan Overdue dengan urutan awal, Remaining, dan aksi baris"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1j#p1", "§4.1j#p2", "§4.1j#r1", "§4.1j#r2", "§4.1j#r3", "§4.1j#r4", "§4.1j#r5", "§4.1j#r6", "§4.1j#r7", "§4.1j#r8", "§4.1j#r9", "§4.1j#r10", "§4.1j#r11", "§4.1j#r12", "§4.1j#r13", "§4.1j#r14", "§4.1j#r15", "§4.1j#r16", "§4.1j#r17", "§4.1j#r18", "§4.1j#p5", "§4.1j#r19", "§4.1j#r20", "§4.1j#r21", "§4.1j#r22", "§4.1j#r23", "§4.1j#r24", "§4.1j#r25", "§4.1j#r26", "§9.5#r4", "§9.5#r5", "EB-SRC-5@tabel-borrowed-assets"]
smoke: []
dependsOn: []
trace:
  "§4.1j#p1": [2, 4, 5, 100, 102]
  "§4.1j#p2": [7, 8]
  "§4.1j#r1": [12]
  "§4.1j#r2": [13, 51, 111, 112, 113, 117, 119, 191, 192, 228, 229, 328, 329, 331, 332]
  "§4.1j#r3": [14, 121, 123, 191, 192]
  "§4.1j#r4": [15, 51, 55, 125, 127, 206, 207]
  "§4.1j#r5": [16, 51, 129, 131, 209, 210, 234, 235]
  "§4.1j#r6": [17, 18, 51, 133, 135, 212, 213, 240, 241]
  "§4.1j#r7": [19, 20, 21, 22, 51, 137, 139, 215, 216, 246, 247]
  "§4.1j#r8": [33, 35, 51, 141, 143, 252, 253]
  "§4.1j#r9": [37, 51, 145, 147, 218, 219, 258, 259]
  "§4.1j#r10": [23, 24, 51, 149, 151, 264, 265]
  "§4.1j#r11": [6, 10, 25, 153, 155, 185, 186]
  "§4.1j#r12": [26, 106, 157, 159, 188, 189]
  "§4.1j#r13": [27, 28, 51, 59, 161, 163, 194, 195, 290, 291]
  "§4.1j#r14": [39, 51, 165, 167, 270, 271]
  "§4.1j#r15": [41, 51, 169, 171, 221, 222, 277, 278]
  "§4.1j#r16": [43, 44, 51, 173, 175, 197, 198, 281, 284, 285]
  "§4.1j#r17": [46, 177, 179, 203, 204]
  "§4.1j#r18": [48, 49, 51, 181, 183, 197, 198, 200, 201, 296, 297]
  "§4.1j#p5": [61]
  "§4.1j#r19": [61, 64, 75]
  "§4.1j#r20": [61, 75, 86]
  "§4.1j#r21": [90, 93, 95]
  "§4.1j#r22": [61, 76, 82]
  "§4.1j#r23": [61, 68, 76]
  "§4.1j#r24": [61, 72, 75]
  "§4.1j#r25": [62, 75, 78]
  "§4.1j#r26": [98, 306, 307, 310, 315, 321, 324]
  "§9.5#r4": [2, 100, 104]
  "§9.5#r5": [6, 9, 10]
  "EB-SRC-5@tabel-borrowed-assets": [30, 33]
anchor: [115]
coverage:
  web: automated
---

# Tab Borrowed Assets By Asset menampilkan baris Borrowed dan Overdue dengan urutan awal, Remaining, dan aksi baris

## Prerequisites
- Aktor: Total Control `Admin Borrow {runId}` (DU-005-1), cakupan seluruh client; aktor lain pada kasus Download: Monitoring & Report `Monitor Borrow {runId}` (DU-005-12) dan Read Only `Viewer Borrow {runId}` (DU-005-13), keduanya cakupan seluruh client.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-005-1: User `Admin Borrow {runId}`, role Total Control, cakupan seluruh client; pelapor Damage Report pada DU-005-8.
  - Pengaju seluruh BRW: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`), tampil `Agus P`. Peminjam, Group, dan status baris tiap aset ada di entri DU-005-2 sampai DU-005-8. BRW pemilik DU-005-7 dibuat lebih dulu daripada BRW pemilik DU-005-4.
  - DU-005-2: aset `Laptop Dell Latitude {runId}`, Brand `Dell`, Model/Type `Latitude 5440`, Category `Laptop`, TAG RFID, Group `Head Office`, Borrower `Andi Pratama` (tampil `Andi P`), status baris Overdue, Due Date `T0 − 3 hari`, Remaining `3 days overdue`, Handed Over At `T0 − 5 hari`, Extensions `0 / 3`, Source `Admin`, Purpose `Presentasi klien`, Handed Over By `Agus P`.
  - DU-005-3: aset `Monitor LG 24MK {runId}` dalam BRW yang sama dengan DU-005-2, Brand `LG`, Model/Type `24MK600M`, Category `Monitor`, TAG QR, Group `Head Office`, Borrower `Andi P`, status baris Overdue, Due Date `T0 − 2 hari`, Remaining `2 days overdue`, Handed Over At `T0 − 4 hari`, Purpose `Presentasi klien`.
  - DU-005-4: aset `Proyektor Epson EB-X06 {runId}`, Brand `Epson`, Model/Type `EB-X06`, Category `Proyektor`, TAG RFID, Group `Head Office`, Borrower `Budi Santoso` (tampil `Budi S`), status baris Borrowed, Due Date `T0 + 2 hari`, Remaining `Due in 2 days`, Handed Over At `T0 − 3 hari`, Extensions `0 / 3`, Purpose `Rapat divisi`, alias `Proyektor Rapat {runId}`, kode TAG `E2003412DF6B-{runId}`.
  - DU-005-14: kata kunci Search alias dan kode TAG milik DU-005-4, diketik langkah.
  - DU-005-5: aset `Kamera Sony A6400 {runId}`, Brand `Sony`, Model/Type `A6400`, Category `Kamera`, TAG NFC, Group `Branch Surabaya`, Borrower `Maya Putri` (tampil `Maya P`), status baris Borrowed, Due Date `T0`, Remaining `Due today`, Extensions `2 / 3`.
  - DU-005-6: aset `Kabel HDMI Premium {runId}` dalam BRW yang sama dengan DU-005-5, Brand `Ugreen`, Model/Type `HD104`, Category `Kabel`, Non TAG, Group `Branch Surabaya`, Borrower `Maya P`, status baris Borrowed, Due Date `T0`, Remaining `Due today`, Extensions `1 / 3`.
  - DU-005-7: aset `Tablet Samsung Tab A9 {runId}`, Brand `Samsung`, Model/Type `Tab A9`, Category `Tablet`, TAG RFID, Group `Head Office`, Borrower `Dewi Lestari` (tampil `Dewi L`), status baris Borrowed dengan pengajuan Extend yang menunggu approval (tampil `Extension Approval`), Due Date `T0 + 2 hari`, Remaining `Due in 2 days`.
  - DU-005-8: aset `Speaker JBL Charge 5 {runId}`, Brand `JBL`, Model/Type `Charge 5`, Category `Speaker`, TAG QR, Group `Head Office`, Borrower `Budi S`, status baris Borrowed dengan Damage Report berstatus Waiting for Confirmation yang dilaporkan `Admin Borrow {runId}` (tampil badge `Reported Damaged`), Due Date `T0 + 6 hari`, Remaining `Due in 6 days`.
  - DU-005-11: aset `Headset Logitech H390 {runId}`, Brand `Logitech`, Model/Type `H390`, Category `Aksesoris Audio`, TAG QR, Group `Head Office`, Borrower `Lina Marlina` (tampil `Lina M`), BRW Self-service yang dibuat Borrower sendiri, status baris Borrowed, Due Date `T0 + 4 hari`, Remaining `Due in 4 days`, Handed Over At `T0 − 1 hari`, Extensions `0 / 3`, Source `Self-service`, Purpose `Kerja jarak jauh`, Handed Over By `Self-service`.
  - DU-005-12: User `Monitor Borrow {runId}`, role Monitoring & Report, cakupan seluruh client.
  - DU-005-13: User `Viewer Borrow {runId}`, role Read Only, cakupan seluruh client.
  - DU-005-9: aset `Printer Epson L3250 {runId}` pada BRW Borrower `Citra Dewi` berstatus Waiting for Handover.
  - DU-005-10: aset `Scanner Canon LiDE 400 {runId}` pada BRW Borrower `Hendra Wijaya` berstatus Returned.
- Kondisi:
  - Akun `Monitor Borrow {runId}` dan `Viewer Borrow {runId}` aktif dan kredensialnya disediakan fase 2.
  - Date Format dan Time Format di General Settings entitas berlaku untuk tampilan Due Date dan Handed Over At.
  - Max extensions efektif seluruh aset pada spec ini bernilai `3`.

## Test Steps

### Tab Borrowed Assets hanya memuat aset yang sedang dipinjam
1. Klik tab `Borrowed Assets`
2. Verifikasi sub-tab `By Asset` aktif
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi hasil Search memuat 8 baris dengan aset `Laptop Dell Latitude {runId}`, `Monitor LG 24MK {runId}`, `Proyektor Epson EB-X06 {runId}`, `Kamera Sony A6400 {runId}`, `Kabel HDMI Premium {runId}`, `Tablet Samsung Tab A9 {runId}`, `Speaker JBL Charge 5 {runId}`, dan `Headset Logitech H390 {runId}`
5. Verifikasi aset `Printer Epson L3250 {runId}` (Waiting for Handover) dan `Scanner Canon LiDE 400 {runId}` (Returned) tidak tampil

### Urutan awal By Asset
6. Verifikasi `Laptop Dell Latitude {runId}` (`3 days overdue`) tampil sebelum `Monitor LG 24MK {runId}` (`2 days overdue`), dan keduanya tampil sebelum semua baris lain
7. Verifikasi `Kabel HDMI Premium {runId}` tampil sebelum `Kamera Sony A6400 {runId}`, karena Due Date dan Transaction ID sama sehingga diurutkan menurut nama aset
8. Verifikasi `Tablet Samsung Tab A9 {runId}` tampil sebelum `Proyektor Epson EB-X06 {runId}`, karena Due Date sama dan Transaction ID aset pertama lebih kecil, walaupun menurut abjad nama aset `Proyektor Epson EB-X06 {runId}` lebih dulu
9. Verifikasi `Speaker JBL Charge 5 {runId}` (`Due in 6 days`) tampil paling akhir, karena Due Date-nya paling jauh
10. Verifikasi `Kamera Sony A6400 {runId}` dan `Kabel HDMI Premium {runId}` (Due Date `T0`) tampil sebelum `Tablet Samsung Tab A9 {runId}` dan `Proyektor Epson EB-X06 {runId}` (Due Date `T0 + 2 hari`)

### Isi kolom yang tampil sejak awal
11. Klik header kolom `Photo`
12. Verifikasi urutan baris tidak berubah karena kolom `Photo` tidak dapat diurutkan
13. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Name yang memuat nama aset tersebut
14. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Asset ID milik DU-005-2
15. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Brand `Dell`, baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Brand `Epson`, dan baris aset `Kamera Sony A6400 {runId}` menampilkan Brand `Sony`
16. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Model/Type `Latitude 5440`, baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Model/Type `EB-X06`, dan baris aset `Kamera Sony A6400 {runId}` menampilkan Model/Type `A6400`
17. Verifikasi baris aset `Laptop Dell Latitude {runId}`, `Proyektor Epson EB-X06 {runId}`, `Tablet Samsung Tab A9 {runId}`, dan `Speaker JBL Charge 5 {runId}` menampilkan Group `Head Office`
18. Verifikasi baris aset `Kamera Sony A6400 {runId}` dan `Kabel HDMI Premium {runId}` menampilkan Group `Branch Surabaya`
19. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan status `Overdue`
20. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` menampilkan status `Borrowed`
21. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` menampilkan status `Extension Approval`
22. Verifikasi baris aset `Speaker JBL Charge 5 {runId}` menampilkan status `Borrowed` dan badge `Reported Damaged`
23. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Due Date `T0 − 3 hari` sesuai Date Format General Settings
24. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Due Date `T0 + 2 hari` sesuai Date Format General Settings
25. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Remaining `3 days overdue`, baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Remaining `Due in 2 days`, dan baris aset `Kamera Sony A6400 {runId}` menampilkan Remaining `Due today`
26. Verifikasi Transaction ID pada setiap baris aset berupa tautan yang dapat diklik
27. Verifikasi baris aset `Laptop Dell Latitude {runId}` dan `Monitor LG 24MK {runId}` menampilkan Borrower `Andi P`
28. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` dan `Speaker JBL Charge 5 {runId}` menampilkan Borrower `Budi S`

### Search tidak mencocokkan kolom TAG yang tersembunyi dan mencocokkannya lagi saat ditampilkan
29. Ganti isi kotak search dengan `NFC`, tekan Enter
30. Verifikasi baris aset `Kamera Sony A6400 {runId}` tidak tampil karena kolom `TAG` tersembunyi
31. Klik header kolom Actions `⋯`
32. Centang `TAG` pada panel Column Visibility
33. Verifikasi baris aset `Kamera Sony A6400 {runId}` tampil dengan ikon TAG `NFC`
34. Ganti isi kotak search dengan `{runId}`, tekan Enter
35. Verifikasi baris aset `Kabel HDMI Premium {runId}` menampilkan `—` pada kolom `TAG`

### Isi kolom tambahan yang ditampilkan lewat Column Visibility
36. Centang `Category` pada panel Column Visibility
37. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Category `Laptop`
38. Centang `Handed Over At` pada panel Column Visibility
39. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Handed Over At `T0 − 5 hari` sesuai Date Format General Settings
40. Centang `Extensions` pada panel Column Visibility
41. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Extensions `0 / 3`
42. Centang `Source` pada panel Column Visibility
43. Verifikasi baris aset `Headset Logitech H390 {runId}` menampilkan Source `Self-service`
44. Verifikasi setiap baris selain `Headset Logitech H390 {runId}` menampilkan Source `Admin`
45. Centang `Purpose` pada panel Column Visibility
46. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Purpose `Presentasi klien` dan baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Purpose `Rapat divisi`
47. Centang `Handed Over By` pada panel Column Visibility
48. Verifikasi baris aset `Headset Logitech H390 {runId}` menampilkan Handed Over By `Self-service`
49. Verifikasi setiap baris selain `Headset Logitech H390 {runId}` menampilkan Handed Over By `Agus P`

### Filter Panel memuat field kolom yang filterable
50. Klik `Filter`
51. Verifikasi Filter Panel memuat field `Asset Name`, `Brand`, `Model/Type`, `Group`, `Status`, `TAG`, `Category`, `Due Date`, `Handed Over At`, `Extensions`, `Source`, `Borrower`, dan `Handed Over By`
52. Klik field `Brand`
53. Pilih opsi `Epson`
54. Klik `[Apply]`
55. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tampil dan baris aset `Laptop Dell Latitude {runId}` tidak tampil
56. Klik `[Clear Field]`
57. Klik `[Apply]`

### Sort kolom Borrower
58. Klik header kolom `Borrower`
59. Verifikasi kolom Borrower dari atas ke bawah berurutan `Andi P`, `Andi P`, `Budi S`, `Budi S`, `Dewi L`, `Lina M`, `Maya P`, lalu `Maya P`

### Aksi baris pada aset Borrowed tanpa Damage Report
60. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}`
61. Verifikasi menu baris memuat `Borrow Log`, `Return`, `Request Extension`, `Report Damaged`, dan `Report Missing`
62. Verifikasi menu baris tidak memuat `Cancel Damage Report`
63. Klik `Borrow Log`
64. Verifikasi dialog Borrow Log terbuka untuk aset `Proyektor Epson EB-X06 {runId}`
65. Tutup dialog Borrow Log
66. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}`
67. Klik `Report Damaged`
68. Verifikasi dialog `Report Damaged` terbuka
69. Tutup dialog `Report Damaged` tanpa menyimpan
70. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}`
71. Klik `Report Missing`
72. Verifikasi dialog `Report Missing` terbuka
73. Tutup dialog `Report Missing` tanpa menyimpan

### Aksi baris pada aset yang sudah dilaporkan rusak oleh aktor
74. Klik `⋯` pada baris aset `Speaker JBL Charge 5 {runId}`
75. Verifikasi menu baris memuat `Borrow Log`, `Return`, `Report Missing`, dan `Cancel Damage Report`
76. Verifikasi menu baris tidak memuat `Request Extension` dan `Report Damaged`
77. Klik `Cancel Damage Report`
78. Verifikasi dialog Cancel Damage Report terbuka untuk aset `Speaker JBL Charge 5 {runId}`
79. Tutup dialog Cancel Damage Report tanpa mengonfirmasi

### Request Extension dan Return per aset membuka halaman dengan aset itu saja
80. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}`
81. Klik `Request Extension`
82. Verifikasi halaman `Extension Request` terbuka dengan baris aset `Proyektor Epson EB-X06 {runId}` saja
83. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb
84. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}`
85. Klik `Return`
86. Verifikasi halaman `Return Asset` terbuka dengan Borrower `Budi S` dan aset `Proyektor Epson EB-X06 {runId}` saja
87. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb

### Bulk Return hanya untuk aset satu Borrower
88. Centang baris aset `Laptop Dell Latitude {runId}`
89. Centang baris aset `Proyektor Epson EB-X06 {runId}`
90. Verifikasi aksi bulk `Return` disabled dengan tooltip `Select assets of one borrower only.`
91. Hapus centang baris aset `Proyektor Epson EB-X06 {runId}`
92. Centang baris aset `Monitor LG 24MK {runId}`
93. Verifikasi aksi bulk `Return` aktif
94. Klik aksi bulk `Return`
95. Verifikasi halaman `Return Asset` terbuka dengan Borrower `Andi P` dan aset `Laptop Dell Latitude {runId}` serta `Monitor LG 24MK {runId}`
96. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb

### Download di toolbar
97. Klik `Download`
98. Verifikasi `Download` pada toolbar menawarkan `Download as CSV` dan `Download as XLSX`

### Pilihan sub-tab tersimpan di URL
99. Tutup popover `Download`
100. Verifikasi alamat halaman memuat `view=asset`
101. Klik sub-tab `By Borrower`
102. Verifikasi alamat halaman memuat `view=borrower`
103. Klik sub-tab `By Asset`
104. Verifikasi alamat halaman memuat `view=asset` dan sub-tab `By Asset` aktif

### Klik Transaction ID membuka Borrow Detail
105. Klik Transaction ID baris aset `Proyektor Epson EB-X06 {runId}`
106. Verifikasi halaman Borrow Detail terbuka dengan Transaction ID milik DU-005-4
107. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb

### Search by Scan menampilkan baris aset itu
108. Klik `Search by Scan`
109. Pilih tipe TAG `RFID`
110. Scan TAG aset `Laptop Dell Latitude {runId}`
111. Verifikasi dialog tertutup dan kotak Search terisi Asset ID aset `Laptop Dell Latitude {runId}`
112. Verifikasi baris aset `Laptop Dell Latitude {runId}` tampil
113. Verifikasi baris aset `Monitor LG 24MK {runId}` tidak tampil

### Sort kolom lewat klik header
114. Ganti isi kotak search dengan `{runId}`, tekan Enter
115. Verifikasi hasil Search memuat 8 baris milik spec ini
116. Klik header kolom `Name`
117. Verifikasi baris aset `Headset Logitech H390 {runId}` tampil paling atas
118. Klik header kolom `Name`
119. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` tampil paling atas
120. Klik header kolom `Asset ID`
121. Verifikasi kolom Asset ID dari atas ke bawah berurutan alfabetis menaik
122. Klik header kolom `Asset ID`
123. Verifikasi kolom Asset ID dari atas ke bawah berurutan alfabetis menurun
124. Klik header kolom `Brand`
125. Verifikasi baris aset `Laptop Dell Latitude {runId}` (Brand `Dell`) tampil paling atas
126. Klik header kolom `Brand`
127. Verifikasi baris aset `Kabel HDMI Premium {runId}` (Brand `Ugreen`) tampil paling atas
128. Klik header kolom `Model/Type`
129. Verifikasi baris aset `Monitor LG 24MK {runId}` (Model/Type `24MK600M`) tampil paling atas
130. Klik header kolom `Model/Type`
131. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` (Model/Type `Tab A9`) tampil paling atas
132. Klik header kolom `Group`
133. Verifikasi baris aset `Kamera Sony A6400 {runId}` dan `Kabel HDMI Premium {runId}` (Group `Branch Surabaya`) tampil di dua baris teratas
134. Klik header kolom `Group`
135. Verifikasi baris aset `Kamera Sony A6400 {runId}` dan `Kabel HDMI Premium {runId}` (Group `Branch Surabaya`) tampil di dua baris terbawah
136. Klik header kolom `Status`
137. Verifikasi baris aset `Laptop Dell Latitude {runId}` dan `Monitor LG 24MK {runId}` (status `Overdue`) tampil di dua baris terbawah
138. Klik header kolom `Status`
139. Verifikasi baris aset `Laptop Dell Latitude {runId}` dan `Monitor LG 24MK {runId}` (status `Overdue`) tampil di dua baris teratas
140. Klik header kolom `TAG`
141. Verifikasi baris aset `Kamera Sony A6400 {runId}` (TAG `NFC`) tampil paling atas, disusul `Kabel HDMI Premium {runId}` (Non TAG)
142. Klik header kolom `TAG`
143. Verifikasi baris aset `Kamera Sony A6400 {runId}` (TAG `NFC`) tampil paling bawah, tepat di bawah `Kabel HDMI Premium {runId}` (Non TAG)
144. Klik header kolom `Category`
145. Verifikasi baris aset `Headset Logitech H390 {runId}` (Category `Aksesoris Audio`) tampil paling atas
146. Klik header kolom `Category`
147. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` (Category `Tablet`) tampil paling atas
148. Klik header kolom `Due Date`
149. Verifikasi baris aset `Laptop Dell Latitude {runId}` (Due Date `T0 − 3 hari`) tampil paling atas
150. Klik header kolom `Due Date`
151. Verifikasi baris aset `Speaker JBL Charge 5 {runId}` (Due Date `T0 + 6 hari`) tampil paling atas
152. Klik header kolom `Remaining`
153. Verifikasi baris aset `Laptop Dell Latitude {runId}` (Remaining `3 days overdue`) tampil paling atas
154. Klik header kolom `Remaining`
155. Verifikasi baris aset `Speaker JBL Charge 5 {runId}` (Remaining `Due in 6 days`) tampil paling atas
156. Klik header kolom `Transaction ID`
157. Verifikasi kolom Transaction ID dari atas ke bawah berurutan alfabetis natural menaik
158. Klik header kolom `Transaction ID`
159. Verifikasi kolom Transaction ID dari atas ke bawah berurutan alfabetis natural menurun
160. Klik header kolom `Borrower`
161. Verifikasi kolom Borrower dari atas ke bawah berurutan menaik, dengan `Andi P` di baris pertama
162. Klik header kolom `Borrower`
163. Verifikasi kolom Borrower dari atas ke bawah berurutan menurun, dengan `Maya P` di baris pertama
164. Klik header kolom `Handed Over At`
165. Verifikasi baris aset `Laptop Dell Latitude {runId}` (Handed Over At `T0 − 5 hari`) tampil paling atas
166. Klik header kolom `Handed Over At`
167. Verifikasi baris aset `Speaker JBL Charge 5 {runId}` dan `Headset Logitech H390 {runId}` (Handed Over At `T0 − 1 hari`) tampil di dua baris teratas
168. Klik header kolom `Extensions`
169. Verifikasi baris aset `Kamera Sony A6400 {runId}` (Extensions `2 / 3`) tampil paling bawah, tepat di bawah `Kabel HDMI Premium {runId}` (Extensions `1 / 3`)
170. Klik header kolom `Extensions`
171. Verifikasi baris aset `Kamera Sony A6400 {runId}` (Extensions `2 / 3`) tampil paling atas, disusul `Kabel HDMI Premium {runId}` (Extensions `1 / 3`)
172. Klik header kolom `Source`
173. Verifikasi baris aset `Headset Logitech H390 {runId}` (Source `Self-service`) tampil paling bawah
174. Klik header kolom `Source`
175. Verifikasi baris aset `Headset Logitech H390 {runId}` (Source `Self-service`) tampil paling atas
176. Klik header kolom `Purpose`
177. Verifikasi baris aset `Speaker JBL Charge 5 {runId}` (Purpose `Acara kantor`) tampil paling atas
178. Klik header kolom `Purpose`
179. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` (Purpose `Survei lapangan`) tampil paling atas
180. Klik header kolom `Handed Over By`
181. Verifikasi baris aset `Headset Logitech H390 {runId}` (Handed Over By `Self-service`) tampil paling bawah
182. Klik header kolom `Handed Over By`
183. Verifikasi baris aset `Headset Logitech H390 {runId}` (Handed Over By `Self-service`) tampil paling atas

### Search mencocokkan nilai kolom yang tampil
184. Ganti isi kotak search dengan `3 days overdue`, tekan Enter
185. Verifikasi baris aset `Laptop Dell Latitude {runId}` tampil
186. Verifikasi baris aset `Monitor LG 24MK {runId}` tidak tampil
187. Ganti isi kotak search dengan Transaction ID milik DU-005-4, tekan Enter
188. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tampil
189. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` tidak tampil
190. Ganti isi kotak search dengan Asset ID milik DU-005-2, tekan Enter
191. Verifikasi baris aset `Laptop Dell Latitude {runId}` tampil
192. Verifikasi baris aset `Monitor LG 24MK {runId}` tidak tampil
193. Ganti isi kotak search dengan `Dewi Lestari`, tekan Enter
194. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` tampil
195. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tidak tampil
196. Ganti isi kotak search dengan `Self-service`, tekan Enter
197. Verifikasi baris aset `Headset Logitech H390 {runId}` tampil
198. Verifikasi baris aset `Laptop Dell Latitude {runId}` tidak tampil
199. Ganti isi kotak search dengan `Agus P`, tekan Enter
200. Verifikasi baris aset `Laptop Dell Latitude {runId}` tampil
201. Verifikasi baris aset `Headset Logitech H390 {runId}` tidak tampil
202. Ganti isi kotak search dengan `Survei lapangan`, tekan Enter
203. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` tampil
204. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tidak tampil
205. Ganti isi kotak search dengan `Ugreen`, tekan Enter
206. Verifikasi baris aset `Kabel HDMI Premium {runId}` tampil
207. Verifikasi baris aset `Laptop Dell Latitude {runId}` tidak tampil
208. Ganti isi kotak search dengan `24MK600M`, tekan Enter
209. Verifikasi baris aset `Monitor LG 24MK {runId}` tampil
210. Verifikasi baris aset `Laptop Dell Latitude {runId}` tidak tampil
211. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
212. Verifikasi baris aset `Kamera Sony A6400 {runId}` tampil
213. Verifikasi baris aset `Laptop Dell Latitude {runId}` tidak tampil
214. Ganti isi kotak search dengan `Overdue`, tekan Enter
215. Verifikasi baris aset `Laptop Dell Latitude {runId}` tampil
216. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tidak tampil
217. Ganti isi kotak search dengan `Aksesoris Audio`, tekan Enter
218. Verifikasi baris aset `Headset Logitech H390 {runId}` tampil
219. Verifikasi baris aset `Speaker JBL Charge 5 {runId}` tidak tampil
220. Ganti isi kotak search dengan `2 / 3`, tekan Enter
221. Verifikasi baris aset `Kamera Sony A6400 {runId}` tampil
222. Verifikasi baris aset `Kabel HDMI Premium {runId}` tidak tampil
223. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Filter Panel menerapkan saringan per field
224. Klik `Filter`
225. Klik field `Asset Name`
226. Pilih opsi `Kamera Sony A6400 {runId}`
227. Klik `[Apply]`
228. Verifikasi baris aset `Kamera Sony A6400 {runId}` tampil
229. Verifikasi baris aset `Laptop Dell Latitude {runId}` tidak tampil
230. Klik `[Clear Field]`
231. Klik field `Model/Type`
232. Pilih opsi `Tab A9`
233. Klik `[Apply]`
234. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` tampil
235. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tidak tampil
236. Klik `[Clear Field]`
237. Klik field `Group`
238. Pilih node `Branch Surabaya`
239. Klik `[Apply]`
240. Verifikasi baris aset `Kamera Sony A6400 {runId}` tampil
241. Verifikasi baris aset `Laptop Dell Latitude {runId}` tidak tampil
242. Klik `[Clear Field]`
243. Klik field `Status`
244. Pilih opsi `Extension Approval`
245. Klik `[Apply]`
246. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` tampil
247. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tidak tampil
248. Klik `[Clear Field]`
249. Klik field `TAG`
250. Pilih opsi `NFC`
251. Klik `[Apply]`
252. Verifikasi baris aset `Kamera Sony A6400 {runId}` tampil
253. Verifikasi baris aset `Laptop Dell Latitude {runId}` tidak tampil
254. Klik `[Clear Field]`
255. Klik field `Category`
256. Pilih node `Kamera`
257. Klik `[Apply]`
258. Verifikasi baris aset `Kamera Sony A6400 {runId}` tampil
259. Verifikasi baris aset `Laptop Dell Latitude {runId}` tidak tampil
260. Klik `[Clear Field]`
261. Klik field `Due Date`
262. Pilih rentang tanggal dari `T0 + 1 hari` sampai `T0 + 3 hari`
263. Klik `[Apply]`
264. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tampil
265. Verifikasi baris aset `Laptop Dell Latitude {runId}` tidak tampil
266. Klik `[Clear Field]`
267. Klik field `Handed Over At`
268. Pilih rentang tanggal dari `T0 − 5 hari` sampai `T0 − 4 hari`
269. Klik `[Apply]`
270. Verifikasi baris aset `Laptop Dell Latitude {runId}` tampil
271. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tidak tampil
272. Klik `[Clear Field]`
273. Klik field `Extensions`
274. Isi `Min` dengan `1`
275. Isi `Max` dengan `2`
276. Klik `[Apply]`
277. Verifikasi baris aset `Kabel HDMI Premium {runId}` dan `Kamera Sony A6400 {runId}` tampil
278. Verifikasi baris aset `Laptop Dell Latitude {runId}` tidak tampil
279. Klik `[Clear Field]`
280. Klik field `Source`
281. Verifikasi opsi `Admin` dan `Self-service` tersedia pada field `Source`
282. Pilih opsi `Self-service`
283. Klik `[Apply]`
284. Verifikasi baris aset `Headset Logitech H390 {runId}` tampil
285. Verifikasi baris aset `Laptop Dell Latitude {runId}` tidak tampil
286. Klik `[Clear Field]`
287. Klik field `Borrower`
288. Pilih opsi `Dewi L`
289. Klik `[Apply]`
290. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` tampil
291. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tidak tampil
292. Klik `[Clear Field]`
293. Klik field `Handed Over By`
294. Pilih opsi `Agus P`
295. Klik `[Apply]`
296. Verifikasi baris aset `Laptop Dell Latitude {runId}` tampil
297. Verifikasi baris aset `Headset Logitech H390 {runId}` tidak tampil
298. Klik `[Clear Field]`
299. Klik `[Apply]`

### Download memakai nama berkas Borrowed-Assets, filter, dan kolom yang tampil
300. Klik field `Asset Name`
301. Pilih opsi `Laptop Dell Latitude {runId}`
302. Pilih opsi `Kamera Sony A6400 {runId}`
303. Klik `[Apply]`
304. Klik `Download`
305. Pilih `Download as CSV`
306. Verifikasi berkas terunduh dengan nama `Borrowed-Assets` dan ekstensi `.csv`
307. Verifikasi berkas memuat 2 baris data
308. Klik `Download`
309. Pilih `Download as XLSX`
310. Verifikasi berkas terunduh dengan nama `Borrowed-Assets` dan ekstensi `.xlsx`
311. Klik header kolom Actions `⋯`
312. Hapus centang `Purpose` pada panel Column Visibility
313. Klik `Download`
314. Pilih `Download as CSV`
315. Verifikasi berkas memuat 2 baris data tanpa kolom `Purpose`
316. Centang `Purpose` pada panel Column Visibility
317. Klik `[Clear Field]`
318. Klik `[Apply]`

### Download tersedia untuk Monitoring & Report dan Read Only
319. Masuk sebagai `Monitor Borrow {runId}`
320. Klik tab `Borrowed Assets`
321. Verifikasi tombol `Download` tampil di toolbar tabel
322. Masuk sebagai `Viewer Borrow {runId}`
323. Klik tab `Borrowed Assets`
324. Verifikasi tombol `Download` tampil di toolbar tabel

### Search mencakup alias aset dan kode TAG
325. Masuk sebagai `Admin Borrow {runId}`
326. Klik tab `Borrowed Assets`
327. Ketik Search `Proyektor Rapat {runId}`, tekan Enter
328. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tampil
329. Verifikasi baris aset `Monitor LG 24MK {runId}` tidak tampil
330. Ganti isi kotak search dengan `E2003412DF6B-{runId}`, tekan Enter
331. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tampil
332. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` tidak tampil
