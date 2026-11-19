---
id: TC-FA-BORROW-E2E-018-approvals-borrow-antrean
title: "Menu Approvals > Borrow menampilkan antrean Active dan History per pengajuan approval, dan Detail read-only"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["F-BORROW-14", "FI-BRW-213", "FI-BRW-214", "FI-BRW-215", "§4.1f#p1", "§4.1f#r1", "§4.1f#r2", "§4.1f#r3", "§4.1f#r4", "§4.1f#r5", "§4.1f#r6", "§4.1f#r7", "§4.1f#r11", "§4.1f#r12", "§4.1f#r13", "§4.1f#r14", "§4.1f#r15", "§4.1f#r16", "§4.1f#r17", "§4.1f#r18", "§4.1f#r19", "§4.1f#p7", "§4.1f#r22", "§4.1f#r23", "§4.1f#r24", "§4.1f#p8", "§4.2.10#p1", "§4.2.10#b1", "§4.2.10#b2", "§4.2.10#b3", "§9.5#r2", "§9.5#r8"]
smoke: []
dependsOn: []
trace:
  "F-BORROW-14": 4
  "FI-BRW-213": [166, 168, 260, 269]
  "FI-BRW-214": 169
  "FI-BRW-215": 171
  "§4.1f#p1": [7, 11, 97, 250, 251]
  "§4.1f#r1": [14, 21, 44, 242]
  "§4.1f#r2": [10, 23, 42, 49, 50]
  "§4.1f#r3": [15, 25, 38, 55, 56]
  "§4.1f#r4": [16, 27, 35, 36, 61, 62, 246]
  "§4.1f#r5": [17, 29, 67, 68, 238]
  "§4.1f#r6": [18, 31, 40, 73, 74, 248]
  "§4.1f#r7": [13, 19, 33, 79, 80]
  "§4.1f#r11": [97, 128, 213, 216]
  "§4.1f#r12": [98, 107, 126, 133, 134]
  "§4.1f#r13": [97, 109, 139, 140, 181, 183]
  "§4.1f#r14": [99, 111, 185, 201, 202]
  "§4.1f#r15": [100, 113, 123, 124, 195, 196, 221]
  "§4.1f#r16": [101, 115, 145, 146, 190]
  "§4.1f#r17": [102, 117, 188, 207, 208, 223]
  "§4.1f#r18": [103, 119, 151, 152]
  "§4.1f#r19": [104, 105, 121, 157, 158]
  "§4.1f#p7": 86
  "§4.1f#r22": [86, 87, 89]
  "§4.1f#r23": [164, 166, 167, 227, 228, 259, 268]
  "§4.1f#r24": [9, 94, 178, 234, 277, 280]
  "§4.1f#p8": [8, 94, 236]
  "§4.2.10#p1": 2
  "§4.2.10#b1": [5, 12]
  "§4.2.10#b2": [93, 95, 96, 227, 228, 259, 268]
  "§4.2.10#b3": [9, 44, 128, 179, 181, 185, 188, 190, 238]
  "§9.5#r2": 4
  "§9.5#r8": [13, 105]
anchor: [187, 249]
coverage:
  web: automated
---

# Menu Approvals > Borrow menampilkan antrean Active dan History per pengajuan approval, dan Detail read-only

## Prerequisites
- Aktor: Rina W, Approver (Role Transaksi `Approver`) pada Group `Head Office` dan `Branch Surabaya`; lalu Total Control `Tia Kusumo {runId}` dan Group Manager `Gani Permana {runId}`, dan kembali sebagai Rina W, pada langkah «Masuk sebagai».
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-018-1: pengajuan approval tipe `Borrow` di antrean Active Rina W, Group `Head Office`, Borrower `Budi Santoso {runId}`, Total Asset `2` (satu aset menunggu keputusan Rina W, satu aset lain berstatus Auto-approved dan tetap dihitung), Requested By `Agus Pratama {runId}`, Request Date T0 − 3 hari, pukul 09:05.
  - DU-018-2: pengajuan tipe `Borrow` di Active, Group `Head Office`, Borrower `Rudi Hartono {runId}`, Total Asset `1`, Requested By `Agus Pratama {runId}`, Request Date T0 − 2 hari, pukul 09:20.
  - DU-018-3: pengajuan tipe `Extension` di Active, Group `Branch Surabaya`, Borrower `Dewi Lestari {runId}`, Total Asset `10`, Requested By `Lina Setiawati {runId}`, Request Date T0 − 1 hari, pukul 07:45.
  - Transaction ID DU-018-3 lebih kecil daripada DU-018-1, dan DU-018-1 lebih kecil daripada DU-018-2 (BRW milik DU-018-3 dibuat paling awal).
  - Nilai tampil kolom Borrower dan Requested By adalah nama depan dan inisial nama belakang, dengan nama lengkap pada hover: `Budi S` dari `Budi Santoso {runId}`, `Rudi H` dari `Rudi Hartono {runId}`, `Dewi L` dari `Dewi Lestari {runId}`, `Hendra K` dari `Hendra Kusuma {runId}`, `Sari D` dari `Sari Dewi {runId}`, `Agus P` dari `Agus Pratama {runId}`, dan `Lina S` dari `Lina Setiawati {runId}`.
  - DU-018-4: pengajuan di History Rina W, status `Approved`, tipe `Borrow`, Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Total Asset `2`, Requested By `Agus Pratama {runId}`, Request Date T0 − 10 hari, pukul 10:00, Decided Date T0 − 10 hari, pukul 11:00.
  - DU-018-5: pengajuan di History, status `Rejected`, tipe `Borrow`, Group `Head Office`, Borrower `Budi Santoso {runId}`, Total Asset `10`, Requested By `Agus Pratama {runId}`, Request Date T0 − 12 hari, pukul 09:10, Decided Date T0 − 11 hari, pukul 11:30.
  - DU-018-6: pengajuan di History, status `Partially Approved`, tipe `Borrow`, Group `Branch Surabaya`, Borrower `Sari Dewi {runId}`, Total Asset `3`, Requested By `Lina Setiawati {runId}`, Request Date T0 − 8 hari, pukul 14:30, Decided Date T0 − 7 hari, pukul 09:40. Asetnya DU-018-10 (mode Any one approver, diputuskan Rina W `Approved`), DU-018-11 (satu approver, diputuskan Rina W `Rejected`), dan DU-018-12 (mode All approvers, Rina W `Approved`, `Wawan Setiawan {runId}` belum memutuskan).
  - DU-018-7: pengajuan di History, status `Approved`, tipe `Extension`, Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Total Asset `1`, Requested By `Lina Setiawati {runId}`, Request Date T0 − 5 hari, pukul 08:00, Decided Date T0 − 4 hari, pukul 10:15. Transaction ID-nya sama dengan DU-018-4 (BRW yang sama). Asetnya `Printer Canon G3010 {runId}` dengan keputusan `Approved`.
  - Transaction ID DU-018-5 lebih kecil daripada DU-018-6, dan DU-018-6 lebih kecil daripada DU-018-4 (BRW milik DU-018-5 dibuat paling awal, lalu DU-018-6, lalu DU-018-4).
  - DU-018-8: pengajuan `Borrow` menunggu approval dengan Borrower `Rina W` sendiri, Group `Head Office`, Requested By `Agus Pratama {runId}`; approver asetnya menurut konfigurasi approver Group `Head Office` adalah Rina W dan `Wawan Setiawan {runId}`.
  - DU-018-9: pengajuan `Borrow` dengan Borrower `Maya Anggraini {runId}`, Group `Head Office`, Requested By `Agus Pratama {runId}`; asetnya mode Any one approver dengan approver Rina W dan `Wawan Setiawan {runId}`, dan `Wawan Setiawan {runId}` sudah memutuskan `Approved`.
  - Aset DU-018-10: `Laptop Dell Latitude {runId}`, aset DU-018-11: `Proyektor Epson {runId}`, aset DU-018-12: `Kamera Sony Alpha {runId}`.
  - DU-018-19: User `Wawan Setiawan {runId}`, Role Transaksi `Approver` pada Group `Head Office` dan `Branch Surabaya`, aktif.
  - DU-018-13: pengajuan `Borrow` menunggu approval dengan Requested By `Rina W`, Group `Head Office`, Borrower `Yusuf Hidayat {runId}`, Total Asset `1`; approver asetnya menurut konfigurasi adalah Rina W dan `Wawan Setiawan {runId}`.
  - DU-018-14: pengajuan `Borrow` menunggu approval dengan Borrower karyawan tanpa akun login `Joko Susilo {runId}` yang PIC-nya Rina W, Group `Head Office`, Requested By `Agus Pratama {runId}`, Total Asset `1`; approver asetnya menurut konfigurasi adalah Rina W dan `Wawan Setiawan {runId}`.
  - DU-018-15: User `Tia Kusumo {runId}`, role Total Control, cakupan seluruh client, aktif.
  - DU-018-16: User `Gani Permana {runId}`, role Group Manager, Group binaan `Head Office`, aktif.
  - DU-018-17: pengajuan di History `Tia Kusumo {runId}`, status `Approved`, tipe `Borrow`, Group `Head Office`, Borrower `Citra Dewanti {runId}`, Total Asset `1`, Requested By `Agus Pratama {runId}`, Request Date T0 − 6 hari, pukul 09:00, Decided Date T0 − 6 hari, pukul 10:30; asetnya `Mesin Fotokopi Ricoh {runId}`; approval pengajuan ini sudah dirutekan ulang kepada `Tia Kusumo {runId}` dan diputuskan olehnya `Approved`.
  - DU-018-18: pengajuan di History `Gani Permana {runId}`, status `Approved`, tipe `Borrow`, Group `Head Office`, Borrower `Dodi Prakoso {runId}`, Total Asset `1`, Requested By `Agus Pratama {runId}`, Request Date T0 − 9 hari, pukul 13:00, Decided Date T0 − 9 hari, pukul 14:00; asetnya `Meja Rapat Oval {runId}`; approval pengajuan ini sudah dirutekan ulang kepada `Gani Permana {runId}` dan diputuskan olehnya `Approved`.
- Kondisi:
  - Akun `Tia Kusumo {runId}` dan `Gani Permana {runId}` aktif, dan kredensialnya disediakan fase 2.

## Test Steps

### Menu Approvals memuat Borrow dan antrean Active menjadi tab awal
1. Klik `Approvals` pada sidebar
2. Verifikasi item `Borrow` tampil sebagai anak `Approvals`
3. Klik `Borrow`
4. Verifikasi breadcrumb `Approvals > Borrow > Active` dan tab `Active` terpilih
5. Verifikasi tab `Active` menampilkan badge jumlah pengajuan dengan angka minimal `3`

### Antrean Active memuat satu baris per pengajuan milik approver
6. Ketik Search `{runId}`, tekan Enter
7. Verifikasi tabel Active memuat baris DU-018-1, DU-018-2, dan DU-018-3
8. Verifikasi Search dan Filter tampil pada toolbar tab `Active`
9. Verifikasi `Download` tidak tampil pada toolbar tab `Active`
10. Verifikasi baris DU-018-1 dan DU-018-2 bertipe `Borrow` dan baris DU-018-3 bertipe `Extension`, satu baris per pengajuan
11. Verifikasi tidak ada baris dengan Borrower `Rina W` di tabel Active
12. Verifikasi tidak ada baris dengan Borrower `Maya Anggraini {runId}` di tabel Active
13. Verifikasi urutan awal baris dari atas ke bawah adalah DU-018-1, DU-018-2, DU-018-3 (Request Date terlama di atas)

### Isi kolom tabel Active sesuai data
14. Verifikasi kolom Transaction ID baris DU-018-1 berformat `BRW-YYYY-NNNN` dan memiliki tombol copy
15. Verifikasi kolom Group baris DU-018-1 `Head Office` dan baris DU-018-3 `Branch Surabaya`
16. Verifikasi kolom Borrower baris DU-018-1 `Budi S`, baris DU-018-2 `Rudi H`, dan baris DU-018-3 `Dewi L`
17. Verifikasi kolom Total Asset baris DU-018-1 `2` (termasuk aset yang berstatus Auto-approved), baris DU-018-2 `1`, dan baris DU-018-3 `10`
18. Verifikasi kolom Requested By baris DU-018-1 `Agus P` dan baris DU-018-3 `Lina S`
19. Verifikasi kolom Request Date baris DU-018-1 menampilkan tanggal dan waktu Request Date milik DU-018-1 menurut format General Settings

### Sort tabel Active
20. Urutkan kolom `Transaction ID` secara Alphabetical (A–Z)
21. Verifikasi urutan natural Transaction ID dari atas ke bawah adalah DU-018-3, DU-018-1, DU-018-2
22. Urutkan kolom `Type` secara Alphabetical (A–Z)
23. Verifikasi baris DU-018-3 berada di bawah baris DU-018-1 dan DU-018-2
24. Urutkan kolom `Group` secara Alphabetical (A–Z)
25. Verifikasi baris DU-018-3 berada di atas baris DU-018-1 dan DU-018-2
26. Urutkan kolom `Borrower` secara Alphabetical (A–Z)
27. Verifikasi urutan dari atas ke bawah adalah DU-018-1, DU-018-3, DU-018-2
28. Urutkan kolom `Total Asset` secara Numeric
29. Verifikasi urutan dari atas ke bawah adalah DU-018-2, DU-018-1, DU-018-3 (Total Asset `10` di bawah `2`, urutan numerik, bukan urutan huruf)
30. Urutkan kolom `Requested By` secara Alphabetical (A–Z)
31. Verifikasi baris DU-018-3 berada di bawah baris DU-018-1 dan DU-018-2
32. Urutkan kolom `Request Date` dengan `Newest First`
33. Verifikasi urutan dari atas ke bawah adalah DU-018-3, DU-018-2, DU-018-1

### Search tabel Active mencari kolom Searchable
34. Ganti isi kotak search dengan `Dewi Lestari {runId}`, tekan Enter
35. Verifikasi baris DU-018-3 tampil
36. Verifikasi baris DU-018-1 dan DU-018-2 tidak tampil
37. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
38. Verifikasi baris DU-018-3 tampil
39. Ganti isi kotak search dengan `Lina Setiawati {runId}`, tekan Enter
40. Verifikasi baris DU-018-3 tampil
41. Ganti isi kotak search dengan `Extension`, tekan Enter
42. Verifikasi baris DU-018-3 tampil
43. Ganti isi kotak search dengan Transaction ID milik DU-018-1, tekan Enter
44. Verifikasi baris DU-018-1 tampil
45. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Filter tabel Active menyaring per kolom
46. Klik ikon Filter
47. Pada field `Type` pilih `Extension`
48. Klik `[Apply]`
49. Verifikasi baris DU-018-3 tampil
50. Verifikasi baris DU-018-1 dan DU-018-2 tidak tampil
51. Klik `[Clear Field]`
52. Klik `[Apply]`
53. Pada field `Group` pilih `Branch Surabaya`
54. Klik `[Apply]`
55. Verifikasi baris DU-018-3 tampil
56. Verifikasi baris DU-018-1 dan DU-018-2 tidak tampil
57. Klik `[Clear Field]`
58. Klik `[Apply]`
59. Pada field `Borrower` pilih `Rudi Hartono {runId}`
60. Klik `[Apply]`
61. Verifikasi baris DU-018-2 tampil
62. Verifikasi baris DU-018-1 dan DU-018-3 tidak tampil
63. Klik `[Clear Field]`
64. Klik `[Apply]`
65. Isi field `Total Asset` dengan Min `2` dan Max `10`
66. Klik `[Apply]`
67. Verifikasi baris DU-018-1 dan DU-018-3 tampil
68. Verifikasi baris DU-018-2 tidak tampil
69. Klik `[Clear Field]`
70. Klik `[Apply]`
71. Pada field `Requested By` pilih `Lina Setiawati {runId}`
72. Klik `[Apply]`
73. Verifikasi baris DU-018-3 tampil
74. Verifikasi baris DU-018-1 dan DU-018-2 tidak tampil
75. Klik `[Clear Field]`
76. Klik `[Apply]`
77. Pada field `Request Date` pilih rentang dari T0 − 3 hari sampai T0 − 2 hari
78. Klik `[Apply]`
79. Verifikasi baris DU-018-1 dan DU-018-2 tampil
80. Verifikasi baris DU-018-3 tidak tampil
81. Klik `[Clear Field]`
82. Klik `[Apply]`
83. Klik ikon Filter

### Row action Review pada tab Active membuka halaman Review
84. Ganti isi kotak search dengan `Budi Santoso {runId}`, tekan Enter
85. Klik menu ⋯ pada baris DU-018-1
86. Verifikasi menu ⋯ baris DU-018-1 memuat `Review`
87. Verifikasi menu ⋯ baris DU-018-1 tidak memuat `Approve` dan `Reject`
88. Klik `Review`
89. Verifikasi breadcrumb `Approvals > Borrow > Active > Review`
90. Klik `Borrow` pada sidebar

### Antrean History memuat satu baris per pengajuan yang sudah diputuskan
91. Klik tab `History`
92. Ketik Search `{runId}`, tekan Enter
93. Verifikasi breadcrumb `Approvals > Borrow > History`
94. Verifikasi Search, Filter, dan `Download` tampil pada toolbar tab `History`
95. Verifikasi tabel History memuat baris DU-018-4, DU-018-5, DU-018-6, dan DU-018-7
96. Verifikasi tidak ada baris dengan Borrower `Maya Anggraini {runId}` di tabel History
97. Verifikasi baris DU-018-4 dan baris DU-018-7 memiliki Transaction ID yang sama, tampil sebagai dua baris terpisah bertipe `Borrow` dan `Extension`
98. Verifikasi kolom Status baris DU-018-4 `Approved`, baris DU-018-5 `Rejected`, baris DU-018-6 `Partially Approved`, dan baris DU-018-7 `Approved`
99. Verifikasi kolom Group baris DU-018-4 `Head Office` dan baris DU-018-6 `Branch Surabaya`
100. Verifikasi kolom Borrower baris DU-018-4 `Hendra K` dan baris DU-018-6 `Sari D`
101. Verifikasi kolom Total Asset baris DU-018-4 `2`, baris DU-018-5 `10`, baris DU-018-6 `3`, dan baris DU-018-7 `1`
102. Verifikasi kolom Requested By baris DU-018-4 `Agus P` dan baris DU-018-6 `Lina S`
103. Verifikasi kolom Request Date baris DU-018-4 menampilkan tanggal dan waktu Request Date milik DU-018-4 menurut format General Settings
104. Verifikasi kolom Decided Date baris DU-018-4 menampilkan tanggal dan waktu Decided Date milik DU-018-4 menurut format General Settings
105. Verifikasi urutan awal dari atas ke bawah adalah DU-018-7, DU-018-6, DU-018-4, DU-018-5 (Decided Date terbaru di atas)

### Sort tabel History
106. Urutkan kolom `Status` secara Alphabetical by label
107. Verifikasi baris DU-018-6 berada di bawah baris DU-018-4 dan DU-018-7 dan di atas baris DU-018-5
108. Urutkan kolom `Type` secara Alphabetical (A–Z)
109. Verifikasi baris DU-018-7 berada di bawah baris DU-018-4, DU-018-5, dan DU-018-6
110. Urutkan kolom `Group` secara Alphabetical (A–Z)
111. Verifikasi baris DU-018-6 berada di atas baris DU-018-4, DU-018-5, dan DU-018-7
112. Urutkan kolom `Borrower` secara Alphabetical (A–Z)
113. Verifikasi baris DU-018-5 berada di atas baris DU-018-4 dan DU-018-7 dan baris DU-018-6 berada di bawah keduanya
114. Urutkan kolom `Total Asset` secara Numeric
115. Verifikasi urutan dari atas ke bawah adalah DU-018-7, DU-018-4, DU-018-6, DU-018-5 (Total Asset `10` di bawah `3`, urutan numerik, bukan urutan huruf)
116. Urutkan kolom `Requested By` secara Alphabetical (A–Z)
117. Verifikasi baris DU-018-6 dan DU-018-7 berada di bawah baris DU-018-4 dan DU-018-5
118. Urutkan kolom `Request Date` dengan `Oldest First`
119. Verifikasi urutan dari atas ke bawah adalah DU-018-5, DU-018-4, DU-018-6, DU-018-7
120. Urutkan kolom `Decided Date` dengan `Oldest First`
121. Verifikasi urutan dari atas ke bawah adalah DU-018-5, DU-018-4, DU-018-6, DU-018-7

### Search tabel History mencari kolom Searchable
122. Ganti isi kotak search dengan `Sari Dewi {runId}`, tekan Enter
123. Verifikasi baris DU-018-6 tampil
124. Verifikasi baris DU-018-4, DU-018-5, dan DU-018-7 tidak tampil
125. Ganti isi kotak search dengan `Partially Approved`, tekan Enter
126. Verifikasi baris DU-018-6 tampil
127. Ganti isi kotak search dengan Transaction ID milik DU-018-4, tekan Enter
128. Verifikasi baris DU-018-4 dan baris DU-018-7 tampil
129. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Filter tabel History menyaring per kolom
130. Klik ikon Filter
131. Pada field `Status` pilih `Partially Approved`
132. Klik `[Apply]`
133. Verifikasi baris DU-018-6 tampil
134. Verifikasi baris DU-018-4, DU-018-5, dan DU-018-7 tidak tampil
135. Klik `[Clear Field]`
136. Klik `[Apply]`
137. Pada field `Type` pilih `Extension`
138. Klik `[Apply]`
139. Verifikasi baris DU-018-7 tampil
140. Verifikasi baris DU-018-4, DU-018-5, dan DU-018-6 tidak tampil
141. Klik `[Clear Field]`
142. Klik `[Apply]`
143. Isi field `Total Asset` dengan Min `3` dan Max `10`
144. Klik `[Apply]`
145. Verifikasi baris DU-018-5 dan DU-018-6 tampil
146. Verifikasi baris DU-018-4 dan DU-018-7 tidak tampil
147. Klik `[Clear Field]`
148. Klik `[Apply]`
149. Pada field `Request Date` pilih rentang dari T0 − 12 hari sampai T0 − 10 hari
150. Klik `[Apply]`
151. Verifikasi baris DU-018-4 dan DU-018-5 tampil
152. Verifikasi baris DU-018-6 dan DU-018-7 tidak tampil
153. Klik `[Clear Field]`
154. Klik `[Apply]`
155. Pada field `Decided Date` pilih rentang dari T0 − 7 hari sampai T0 − 4 hari
156. Klik `[Apply]`
157. Verifikasi baris DU-018-6 dan DU-018-7 tampil
158. Verifikasi baris DU-018-4 dan DU-018-5 tidak tampil
159. Klik `[Clear Field]`
160. Klik `[Apply]`
161. Klik ikon Filter

### Detail read-only dari tab History
162. Ganti isi kotak search dengan `Sari Dewi {runId}`, tekan Enter
163. Klik menu ⋯ pada baris DU-018-6
164. Verifikasi menu ⋯ baris DU-018-6 memuat `Detail`
165. Klik `Detail`
166. Verifikasi breadcrumb `Approvals > Borrow > History > Detail`
167. Verifikasi tabel aset memuat aset DU-018-10, DU-018-11, dan DU-018-12 dari pengajuan baris DU-018-6
168. Verifikasi halaman tidak memuat toggle `Approval`, kontrol `Approve Duration` dan `Approval Note` yang dapat diisi, toolbar bulk, dan footer keputusan
169. Verifikasi keputusan aset DU-018-10 `Approved`, aset DU-018-11 `Rejected`, dan aset DU-018-12 `Waiting`
170. Klik sel `Approval Rule` aset DU-018-12
171. Verifikasi dialog `Approval Progress` menampilkan Rina W `Approved` dan `Wawan Setiawan {runId}` `Waiting for Approval`

### Download pada tab History mengunduh baris yang tampil
172. Klik `Approvals` pada sidebar
173. Klik `Borrow`
174. Klik tab `History`
175. Ketik Search `Sari Dewi {runId}`, tekan Enter
176. Klik `Download`
177. Pilih unduhan format CSV
178. Verifikasi berkas CSV memuat baris DU-018-6
179. Verifikasi berkas CSV tidak memuat baris DU-018-4

### Search tabel History mencari kolom Type, Group, Requested By, dan Total Asset
180. Ganti isi kotak search dengan `Extension`, tekan Enter
181. Verifikasi baris DU-018-7 tampil
182. Ganti isi kotak search dengan `Borrow`, tekan Enter
183. Verifikasi baris DU-018-4 dan baris DU-018-5 tampil
184. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
185. Verifikasi baris DU-018-6 tampil
186. Ganti isi kotak search dengan `Lina Setiawati {runId}`, tekan Enter
187. Verifikasi baris DU-018-6 dan baris DU-018-7 tampil
188. Verifikasi baris DU-018-4 dan baris DU-018-5 tidak tampil
189. Ganti isi kotak search dengan `10`, tekan Enter
190. Verifikasi baris DU-018-5 tampil
191. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Filter tabel History menyaring Borrower, Group, dan Requested By
192. Klik ikon Filter
193. Pada field `Borrower` pilih `Sari Dewi {runId}`
194. Klik `[Apply]`
195. Verifikasi baris DU-018-6 tampil
196. Verifikasi baris DU-018-4, DU-018-5, dan DU-018-7 tidak tampil
197. Klik `[Clear Field]`
198. Klik `[Apply]`
199. Pada field `Group` pilih `Branch Surabaya`
200. Klik `[Apply]`
201. Verifikasi baris DU-018-6 tampil
202. Verifikasi baris DU-018-4, DU-018-5, dan DU-018-7 tidak tampil
203. Klik `[Clear Field]`
204. Klik `[Apply]`
205. Pada field `Requested By` pilih `Lina Setiawati {runId}`
206. Klik `[Apply]`
207. Verifikasi baris DU-018-6 dan DU-018-7 tampil
208. Verifikasi baris DU-018-4 dan DU-018-5 tidak tampil
209. Klik `[Clear Field]`
210. Klik `[Apply]`
211. Klik ikon Filter

### Sort Transaction ID di History dan tautan Transaction ID membuka Detail read-only
212. Urutkan kolom `Transaction ID` secara Alphabetical (A–Z)
213. Verifikasi baris DU-018-5 berada di atas baris DU-018-6, dan baris DU-018-6 berada di atas baris DU-018-4 dan DU-018-7
214. Ganti isi kotak search dengan `Sari Dewi {runId}`, tekan Enter
215. Klik tautan Transaction ID pada baris DU-018-6
216. Verifikasi breadcrumb `Approvals > Borrow > History > Detail`
217. Klik `Borrow` pada sidebar
218. Klik tab `History`

### Nama Borrower dan Requested By di History tampil singkat dengan nama lengkap pada hover
219. Ketik Search `{runId}`, tekan Enter
220. Arahkan kursor ke sel Borrower baris DU-018-6
221. Verifikasi nama lengkap `Sari Dewi {runId}` tersampaikan pada hover sel Borrower
222. Arahkan kursor ke sel Requested By baris DU-018-6
223. Verifikasi nama lengkap `Lina Setiawati {runId}` tersampaikan pada hover sel Requested By

### Detail read-only untuk pengajuan Extension
224. Ganti isi kotak search dengan `Hendra Kusuma {runId}`, tekan Enter
225. Klik menu ⋯ pada baris DU-018-7
226. Klik `Detail`
227. Verifikasi breadcrumb `Approvals > Borrow > History > Detail`
228. Verifikasi tabel aset memuat aset `Printer Canon G3010 {runId}` dari pengajuan Extension baris DU-018-7
229. Klik `Borrow` pada sidebar
230. Klik tab `History`

### Download pada tab History mengunduh berkas XLSX
231. Ketik Search `Sari Dewi {runId}`, tekan Enter
232. Klik `Download`
233. Pilih unduhan format XLSX
234. Verifikasi berkas XLSX memuat baris DU-018-6
235. Klik `Borrow` pada sidebar

### Placeholder Search dan pencarian Total Asset di tab Active
236. Verifikasi kotak Search yang kosong memuat placeholder yang menyebut `Transaction ID` sebagai contoh
237. Ketik Search `10`, tekan Enter
238. Verifikasi baris DU-018-3 tampil
239. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Tautan Transaction ID pada tab Active membuka halaman Review
240. Ganti isi kotak search dengan `Budi Santoso {runId}`, tekan Enter
241. Klik tautan Transaction ID pada baris DU-018-1
242. Verifikasi breadcrumb `Approvals > Borrow > Active > Review`
243. Klik `Borrow` pada sidebar

### Nama Borrower dan Requested By di Active tampil singkat dengan nama lengkap pada hover
244. Ketik Search `{runId}`, tekan Enter
245. Arahkan kursor ke sel Borrower baris DU-018-1
246. Verifikasi nama lengkap `Budi Santoso {runId}` tersampaikan pada hover sel Borrower
247. Arahkan kursor ke sel Requested By baris DU-018-1
248. Verifikasi nama lengkap `Agus Pratama {runId}` tersampaikan pada hover sel Requested By

### Pengajuan yang diajukan atau dipinjam atas nama approver sendiri tidak masuk antrean Active
249. Verifikasi baris DU-018-1 tampil
250. Verifikasi tidak ada baris dengan Borrower `Yusuf Hidayat {runId}` di tabel Active, padahal pengajuannya diajukan oleh Rina W
251. Verifikasi tidak ada baris dengan Borrower `Joko Susilo {runId}` di tabel Active, padahal PIC-nya Rina W

### Detail read-only dibuka oleh Total Control
252. Masuk sebagai Total Control `Tia Kusumo {runId}`
253. Klik `Approvals` pada sidebar
254. Klik `Borrow`
255. Klik tab `History`
256. Ketik Search `Citra Dewanti {runId}`, tekan Enter
257. Klik menu ⋯ pada baris DU-018-17
258. Klik `Detail`
259. Verifikasi breadcrumb `Approvals > Borrow > History > Detail`
260. Verifikasi halaman tidak memuat toggle `Approval`, kontrol `Approve Duration` dan `Approval Note` yang dapat diisi, toolbar bulk, dan footer keputusan

### Detail read-only dibuka oleh Group Manager
261. Masuk sebagai Group Manager `Gani Permana {runId}`
262. Klik `Approvals` pada sidebar
263. Klik `Borrow`
264. Klik tab `History`
265. Ketik Search `Dodi Prakoso {runId}`, tekan Enter
266. Klik menu ⋯ pada baris DU-018-18
267. Klik `Detail`
268. Verifikasi breadcrumb `Approvals > Borrow > History > Detail`
269. Verifikasi halaman tidak memuat toggle `Approval`, kontrol `Approve Duration` dan `Approval Note` yang dapat diisi, toolbar bulk, dan footer keputusan

### Nama berkas unduhan tab History
270. Masuk sebagai Approver `Rina W`
271. Klik `Approvals` pada sidebar
272. Klik `Borrow`
273. Klik tab `History`
274. Ketik Search `Sari Dewi {runId}`, tekan Enter
275. Klik `Download`
276. Pilih unduhan format CSV
277. Verifikasi nama berkas unduhan CSV, tanpa ekstensi, adalah `Borrow-Approvals`
278. Klik `Download`
279. Pilih unduhan format XLSX
280. Verifikasi nama berkas unduhan XLSX, tanpa ekstensi, adalah `Borrow-Approvals`
