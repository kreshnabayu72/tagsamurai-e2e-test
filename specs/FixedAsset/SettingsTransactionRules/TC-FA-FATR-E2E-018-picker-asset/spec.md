---
id: TC-FA-FATR-E2E-018-picker-asset
title: "Dialog Select Asset menampilkan aset dari data nyata"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [§4.1#r390, §4.1#r391, §4.1#r392, §4.1#r393, §4.1#r394, §4.1#r395, §4.1#r396, §4.1#r397, §5#r3, §5#r4, D-05, §9.5#r10, §9.5#r25, §11#r14, EB-TBL-9@select-asset, EB-SRC-5@select-asset]
smoke: []
dependsOn: []
trace:
  §4.1#r390: [8, 21, 23, 27, 46]
  §4.1#r391: [9, 34, 49]
  §4.1#r392: [10, 37, 52, 53, 93, 94]
  §4.1#r393: [10, 55, 115, 117, 119, 124, 125]
  §4.1#r394: [11, 41, 57, 87, 88]
  §4.1#r395: [11, 44, 59, 99, 100]
  §4.1#r396: [12, 13, 29, 61, 81, 82]
  §4.1#r397: [12, 13, 32, 63, 105, 106]
  §5#r3: [46, 47, 49, 50, 52, 53, 55, 57, 59, 61, 63, 65, 81]
  §5#r4: 8
  D-05: [15, 16, 19, 115, 134, 135]
  §9.5#r10: 8
  §9.5#r25: [15, 19, 134, 135]
  §11#r14: 8
  EB-TBL-9@select-asset: [16, 135]
  EB-SRC-5@select-asset: [67, 71, 75]
anchor: [8, 18]
coverage:
  web: automated
---

# Dialog Select Asset menampilkan aset dari data nyata

## Prerequisites
- Aktor: Total Control; lalu `Andi {runId}`, user dengan Group Role Manage asset & TAG (Read + Update) pada Group `Proyek Karawang {runId}` beserta turunannya.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-018-1: Category leaf `Laptop {runId}`, ada di entitas aktor.
  - DU-018-2: Category leaf `Machinery {runId}`, ada di entitas aktor.
  - DU-018-3: Group tingkat atas `Proyek Karawang {runId}`.
  - DU-018-4: Group `Workshop {runId}`, turunan langsung dari `Proyek Karawang {runId}`.
  - DU-018-5: Group tingkat atas `Proyek Bekasi {runId}`.
  - DU-018-6: Brand `Dell {runId}`.
  - DU-018-7: Brand `Lenovo {runId}`.
  - DU-018-8: Model/Type `E5420 {runId}`.
  - DU-018-9: Model/Type `T14 Gen3 {runId}`.
  - DU-018-10: Label `Staff {runId}`.
  - DU-018-11: Label `Warranty {runId}`.
  - DU-018-12: Label `Loan {runId}`.
  - DU-018-13: Label `Zone {runId}`.
  - DU-018-14: Asset Name `Laptop Dell Latitude 5420 {runId}`, Code `LPT18-{runId}`, Category `Laptop {runId}`, UoM `Unit`.
  - DU-018-15: Asset Name `Laptop Lenovo ThinkPad T14 {runId}`, Code `TPD18-{runId}`, Category `Laptop {runId}`, UoM `Unit`.
  - DU-018-16: Asset Name `Excavator PC200 {runId}`, Code `EXC18-{runId}`, Category `Machinery {runId}`, UoM `Unit`.
  - DU-018-17: aset `Laptop Dell Latitude 5420 {runId} - 1`, Asset ID `LPT18-001-{runId}`, Group `Proyek Karawang {runId}`, Category `Laptop {runId}`, Brand `Dell {runId}`, Model/Type `E5420 {runId}`, Status `Available`, Labels `Staff {runId}`.
  - DU-018-18: aset `Laptop Dell Latitude 5420 {runId} - 2`, Asset ID `LPT18-002-{runId}`, Group `Proyek Karawang {runId}`, Category `Laptop {runId}`, Brand `Dell {runId}`, Model/Type `E5420 {runId}`, Status `Assigned`, Labels `Staff {runId}`, `Warranty {runId}`, dan `Loan {runId}`.
  - DU-018-19: aset `Laptop Dell Latitude 5420 {runId} - 3`, Asset ID `LPT18-003-{runId}`, Group `Proyek Karawang {runId}`, Category `Laptop {runId}`, Brand `Dell {runId}`, Model/Type `E5420 {runId}`, Status `Available`, Labels `Loan {runId}` dan `Zone {runId}`.
  - DU-018-20: aset `Laptop Dell Latitude 5420 {runId} - 4`, Asset ID `LPT18-004-{runId}`, Group `Proyek Karawang {runId}`, Category `Laptop {runId}`, Brand `Dell {runId}`, Model/Type `E5420 {runId}`, Status `Available`, Labels `Staff {runId}` dan `Warranty {runId}`.
  - DU-018-21: 3 aset `Laptop Dell Latitude 5420 {runId} - {n}` dengan n dari 5 sampai 7, Group `Proyek Karawang {runId}`, Category `Laptop {runId}`, Brand `Dell {runId}`, Model/Type `E5420 {runId}`, Status `Available`, tanpa Labels (tampil `—`).
  - DU-018-22: aset `Laptop Dell Latitude 5420 {runId} - 8`, Asset ID `LPT18-008-{runId}`, Group `Proyek Karawang {runId}`, Category `Laptop {runId}`, Brand `Dell {runId}`, Model/Type `E5420 {runId}`, Status `Available`, Labels tanpa Labels (tampil `—`).
  - DU-018-23: aset `Laptop Dell Latitude 5420 {runId} - 9`, Asset ID `LPT18-009-{runId}`, Group `Proyek Karawang {runId}`, Category `Laptop {runId}`, Brand `Dell {runId}`, Model/Type `E5420 {runId}`, Status `Available`, Labels tanpa Labels (tampil `—`).
  - DU-018-24: aset `Laptop Dell Latitude 5420 {runId} - 10`, Asset ID `LPT18-010-{runId}`, Group `Proyek Karawang {runId}`, Category `Laptop {runId}`, Brand `Dell {runId}`, Model/Type `E5420 {runId}`, Status `Available`, Labels tanpa Labels (tampil `—`).
  - DU-018-25: aset `Laptop Lenovo ThinkPad T14 {runId} - 1`, Asset ID `TPD18-001-{runId}`, Group `Workshop {runId}`, Category `Laptop {runId}`, Brand `Lenovo {runId}`, Model/Type `T14 Gen3 {runId}`, Status `Available`, Labels tanpa Labels (tampil `—`).
  - DU-018-26: aset `Laptop Lenovo ThinkPad T14 {runId} - 2`, Asset ID `TPD18-002-{runId}`, Group `Workshop {runId}`, Category `Laptop {runId}`, Brand `Lenovo {runId}`, Model/Type `T14 Gen3 {runId}`, Status `Disposed`, Labels tanpa Labels.
  - DU-018-27: aset `Laptop Lenovo ThinkPad T14 {runId} - 3`, Asset ID `TPD18-003-{runId}`, Group `Workshop {runId}`, Category `Laptop {runId}`, Brand `Lenovo {runId}`, Model/Type `T14 Gen3 {runId}`, Status `Available`, Labels tanpa Labels, sudah dihapus.
  - DU-018-28: aset `Laptop Lenovo ThinkPad T14 {runId} - 4`, Asset ID `TPD18-004-{runId}`, Group `Proyek Bekasi {runId}`, Category `Laptop {runId}`, Brand `Lenovo {runId}`, Model/Type `T14 Gen3 {runId}`, Status `Available`, Labels tanpa Labels.
  - DU-018-29: aset `Excavator PC200 {runId} - 1`, Asset ID `EXC18-001-{runId}`, Group `Proyek Karawang {runId}`, Category `Machinery {runId}`, Brand `Dell {runId}`, Model/Type `E5420 {runId}`, Status `Available`, Labels tanpa Labels.
  - DU-018-30: user `Andi {runId}`, Group Role Manage asset & TAG (Read + Update), cakupan Group `Proyek Karawang {runId}` beserta turunannya.
- Kondisi:
  - Kolom `Brand` dialog Select Asset ditampilkan (bawaan).
  - Ukuran halaman dialog Select Asset bernilai `10`.
  - Akun `Andi {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Dialog menampilkan aset aktif dalam Category terpilih dengan urutan awal Name A-Z
1. Ketik Search Sidebar Category Tree `Laptop {runId}`, tekan Enter
2. Klik node `Laptop {runId}` di Sidebar Category Tree
3. Klik tab `Borrow`
4. Klik `[+ Override]`
5. Pilih Scope `Asset`
6. Klik `[Select Asset]`
7. Ketik Search `Latitude 5420 {runId}` pada dialog Select Asset, tekan Enter
8. Verifikasi urutan baris dari atas ke bawah menurut Name: `Laptop Dell Latitude 5420 {runId} - 1`, `Laptop Dell Latitude 5420 {runId} - 2`, `Laptop Dell Latitude 5420 {runId} - 3` sebagai tiga baris pertama dan `Laptop Dell Latitude 5420 {runId} - 9`, `Laptop Dell Latitude 5420 {runId} - 10` sebagai dua baris terakhir
9. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` memiliki Asset ID `LPT18-001-{runId}`
10. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` memiliki Group `Proyek Karawang {runId}` dan Category `Laptop {runId}`
11. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` memiliki Brand `Dell {runId}` dan Model / Type `E5420 {runId}`
12. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` memiliki Status `Available` dan Labels `Staff {runId}`
13. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 2` memiliki Status `Assigned` dan Labels `Loan {runId}`, `Staff {runId}`, serta `+1 more`
14. Ganti isi kotak Search dengan `ThinkPad T14 {runId}`, tekan Enter
15. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` tampil di dialog Select Asset
16. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 2` dan baris `Laptop Lenovo ThinkPad T14 {runId} - 3` tidak tampil karena aset Disposed dan aset yang dihapus tidak ditampilkan
17. Ganti isi kotak Search dengan `Dell {runId}`, tekan Enter
18. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` tampil di dialog Select Asset
19. Verifikasi baris `Excavator PC200 {runId} - 1` tidak tampil karena Category `Machinery {runId}` bukan Category terpilih

### Urutan awal Name A-Z lintas nama aset dengan Increment numerik natural
20. Ganti isi kotak Search dengan `Laptop {runId}`, tekan Enter
21. Verifikasi baris terakhir halaman 1 adalah `Laptop Dell Latitude 5420 {runId} - 10` menurut Name A-Z dengan Increment numerik natural
22. Klik tombol `Next Page` pada paginasi dialog Select Asset
23. Verifikasi baris pertama halaman 2 adalah `Laptop Lenovo ThinkPad T14 {runId} - 1` sebagai nama aset sesudah `Laptop Dell Latitude 5420 {runId}` menurut Name A-Z

### Sort kolom Name, Status, Labels, Asset ID, Group, Brand, dan Model / Type
24. Ketik Search `Latitude 5420 {runId}` pada dialog Select Asset, tekan Enter
25. Klik header kolom Name pada dialog Select Asset
26. Klik header kolom Name pada dialog Select Asset
27. Verifikasi tiga baris pertama menurut Name: `Laptop Dell Latitude 5420 {runId} - 10`, `Laptop Dell Latitude 5420 {runId} - 9`, `Laptop Dell Latitude 5420 {runId} - 8` secara descending dengan Increment numerik natural
28. Klik header kolom Status pada dialog Select Asset
29. Verifikasi baris pertama adalah `Laptop Dell Latitude 5420 {runId} - 2` dengan Status `Assigned` secara ascending menurut label badge
30. Klik header kolom Labels pada dialog Select Asset
31. Klik header kolom Labels pada dialog Select Asset
32. Verifikasi tiga baris pertama menurut Name: `Laptop Dell Latitude 5420 {runId} - 2`, `Laptop Dell Latitude 5420 {runId} - 4`, `Laptop Dell Latitude 5420 {runId} - 3` menurut jumlah label lalu label pertama secara descending
33. Klik header kolom Asset ID pada dialog Select Asset
34. Verifikasi tiga baris pertama menurut Asset ID: `LPT18-001-{runId}`, `LPT18-002-{runId}`, `LPT18-003-{runId}` untuk `Laptop Dell Latitude 5420 {runId} - 1`, `Laptop Dell Latitude 5420 {runId} - 2`, `Laptop Dell Latitude 5420 {runId} - 3` secara ascending
35. Ganti isi kotak Search dengan `ThinkPad T14 {runId}`, tekan Enter
36. Klik header kolom Group pada dialog Select Asset
37. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 4` dengan Group `Proyek Bekasi {runId}` tampil di atas baris `Laptop Lenovo ThinkPad T14 {runId} - 1` dengan Group `Workshop {runId}` secara ascending menurut Group
38. Ganti isi kotak Search dengan `Laptop {runId}`, tekan Enter
39. Klik header kolom Brand pada dialog Select Asset
40. Klik header kolom Brand pada dialog Select Asset
41. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` dan baris `Laptop Lenovo ThinkPad T14 {runId} - 4` dengan Brand `Lenovo {runId}` tampil sebagai dua baris pertama secara descending menurut Brand
42. Klik header kolom Model / Type pada dialog Select Asset
43. Klik header kolom Model / Type pada dialog Select Asset
44. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` dan baris `Laptop Lenovo ThinkPad T14 {runId} - 4` dengan Model / Type `T14 Gen3 {runId}` tampil sebagai dua baris pertama secara descending menurut Model / Type

### Search mencari di semua kolom yang searchable
45. Ganti isi kotak Search dengan `Laptop Lenovo ThinkPad T14 {runId} - 1`, tekan Enter
46. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` tampil karena kolom Name ikut dicari
47. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` tidak tampil
48. Ganti isi kotak Search dengan `LPT18-001-{runId}`, tekan Enter
49. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` tampil karena kolom Asset ID ikut dicari
50. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 2` tidak tampil
51. Ganti isi kotak Search dengan `Workshop {runId}`, tekan Enter
52. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` tampil karena kolom Group ikut dicari
53. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` dan baris `Laptop Lenovo ThinkPad T14 {runId} - 4` tidak tampil
54. Ganti isi kotak Search dengan `Laptop {runId}`, tekan Enter
55. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` tampil karena kolom Category ikut dicari
56. Ganti isi kotak Search dengan `Lenovo {runId}`, tekan Enter
57. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` dan baris `Laptop Lenovo ThinkPad T14 {runId} - 4` tampil karena kolom Brand ikut dicari
58. Ganti isi kotak Search dengan `Gen3 {runId}`, tekan Enter
59. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` tampil karena kolom Model / Type ikut dicari
60. Ganti isi kotak Search dengan `Assigned`, tekan Enter
61. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 2` dengan Status `Assigned` tampil karena kolom Status ikut dicari
62. Ganti isi kotak Search dengan `Loan {runId}`, tekan Enter
63. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 2` dan baris `Laptop Dell Latitude 5420 {runId} - 3` tampil karena kolom Labels ikut dicari
64. Ganti isi kotak Search dengan `Zzqx {runId}`, tekan Enter
65. Verifikasi `No results found` tampil pada dialog Select Asset

### Search tidak lagi mencocokkan kolom yang disembunyikan
66. Ganti isi kotak Search dengan `Lenovo {runId}`, tekan Enter
67. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` tampil karena kolom Brand ikut dicari
68. Klik header kolom Actions pada dialog Select Asset
69. Hapus centang kolom `Brand`
70. Ganti isi kotak Search dengan `Lenovo {runId}` lagi, tekan Enter
71. Verifikasi `No results found` tampil pada dialog Select Asset karena kolom Brand disembunyikan
72. Klik header kolom Actions pada dialog Select Asset
73. Centang kolom `Brand`
74. Ganti isi kotak Search dengan `Lenovo {runId}` lagi, tekan Enter
75. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` tampil lagi karena kolom Brand ditampilkan

### Filter Status, Brand, Group, Model / Type, dan Label
76. Ganti isi kotak Search dengan `{runId}`, tekan Enter
77. Klik ikon filter pada toolbar dialog Select Asset
78. Klik field `Status` pada panel filter
79. Pilih opsi `Assigned`
80. Klik `[Apply]`
81. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 2` tampil karena Status `Assigned`
82. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` dan baris `Laptop Lenovo ThinkPad T14 {runId} - 1` tidak tampil
83. Klik `[Clear Field]`
84. Klik field `Brand` pada panel filter
85. Pilih opsi `Lenovo {runId}`
86. Klik `[Apply]`
87. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` dan baris `Laptop Lenovo ThinkPad T14 {runId} - 4` dengan Brand `Lenovo {runId}` tampil
88. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` tidak tampil
89. Klik `[Clear Field]`
90. Klik field `Group` pada panel filter
91. Pilih opsi `Workshop {runId}`
92. Klik `[Apply]`
93. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` dengan Group `Workshop {runId}` tampil
94. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` tidak tampil karena Group `Proyek Karawang {runId}` tersaring keluar
95. Klik `[Clear Field]`
96. Klik field `Model / Type` pada panel filter
97. Pilih opsi `T14 Gen3 {runId}`
98. Klik `[Apply]`
99. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` dengan Model / Type `T14 Gen3 {runId}` tampil
100. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` tidak tampil karena Model / Type `E5420 {runId}` tersaring keluar
101. Klik `[Clear Field]`
102. Klik field `Label` pada panel filter
103. Pilih opsi `Loan {runId}`
104. Klik `[Apply]`
105. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 2` dan baris `Laptop Dell Latitude 5420 {runId} - 3` tampil karena memiliki Labels `Loan {runId}`
106. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` tidak tampil karena tidak memiliki Labels `Loan {runId}`

### All categories menampilkan aset semua Category
107. Klik `[Cancel]` pada dialog Select Asset
108. Klik `✕` pada dialog, lalu klik `[Leave]` pada dialog Unsaved Changes
109. Klik node `All categories` di Sidebar Category Tree
110. Klik tab `Borrow`
111. Klik `[+ Override]`
112. Pilih Scope `Asset`
113. Klik `[Select Asset]`
114. Ketik Search `{runId}` pada dialog Select Asset, tekan Enter
115. Verifikasi baris `Excavator PC200 {runId} - 1` dengan Category `Machinery {runId}` dan baris `Laptop Dell Latitude 5420 {runId} - 1` dengan Category `Laptop {runId}` tampil
116. Klik header kolom Category pada dialog Select Asset
117. Verifikasi baris pertama memiliki Category `Laptop {runId}` secara ascending menurut Category
118. Klik header kolom Category pada dialog Select Asset
119. Verifikasi baris pertama adalah `Excavator PC200 {runId} - 1` dengan Category `Machinery {runId}` secara descending menurut Category
120. Klik ikon filter pada toolbar dialog Select Asset
121. Klik field `Category` pada panel filter
122. Pilih opsi `Machinery {runId}`
123. Klik `[Apply]`
124. Verifikasi baris `Excavator PC200 {runId} - 1` dengan Category `Machinery {runId}` tampil sesudah Filter Category dari All categories
125. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 1` tidak tampil karena Category `Laptop {runId}` tersaring keluar

### Manage asset & TAG hanya melihat aset dalam cakupan Group-nya
126. Masuk sebagai `Andi {runId}`
127. Ketik Search Sidebar Category Tree `Laptop {runId}`, tekan Enter
128. Klik node `Laptop {runId}` di Sidebar Category Tree
129. Klik tab `Borrow`
130. Klik `[+ Override]`
131. Pilih Scope `Asset`
132. Klik `[Select Asset]`
133. Ketik Search `ThinkPad T14 {runId}` pada dialog Select Asset, tekan Enter
134. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 1` dengan Group `Workshop {runId}` tampil untuk `Andi {runId}`
135. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 4` dengan Group `Proyek Bekasi {runId}` tidak tampil karena berada di luar cakupan `Andi {runId}`
