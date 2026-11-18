---
id: TC-FA-BORROW-UI-057-tabel-history-konfigurasi
title: "Tabel History By Transaction dan By Asset: konfigurasi kolom dan rentang awal"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1k#p3", "§4.1k#p4", "§4.1k#r1", "§4.1k#r2", "§4.1k#r3", "§4.1k#r4", "§4.1k#r5", "§4.1k#r6", "§4.1k#r7", "§4.1k#r8", "§4.1k#r9", "§4.1k#p7", "§4.1k#r16", "§4.1k#r17", "§4.1k#r18", "§4.1k#r19", "§4.1k#r20", "§4.1k#r21", "§4.1k#r22", "§4.1k#r23", "§4.1k#r24", "§4.1k#r25", "§4.1k#r26", "§4.1k#r27", "§4.1k#r28", "§4.1k#r29", "§4.1k#r30", "§4.1k#r31", "§4.1k#r32", "§4.1k#r33", "§4.1k#r34", "§4.1k#r35", "EB-TBL-1@tabel-history", "EB-TBL-2@tabel-history", "EB-TBL-4@tabel-history", "EB-TBL-12"]
smoke: []
dependsOn: []
trace:
  "§4.1k#p3": [25, 27, 80, 82]
  "§4.1k#p4": 30
  "§4.1k#r1": [29, 32, 33, 62]
  "§4.1k#r2": [29, 34, 35, 37, 38, 39, 62, 70]
  "§4.1k#r3": [29, 40, 42, 43, 62, 71, 72]
  "§4.1k#r4": [29, 45, 47, 48, 62, 73]
  "§4.1k#r5": [29, 49, 51, 52, 62, 74]
  "§4.1k#r6": [63, 65, 66, 67, 75]
  "§4.1k#r7": [29, 53, 55, 56, 62, 76]
  "§4.1k#r8": [29, 57, 59, 62, 77]
  "§4.1k#r9": [29, 58, 59, 62, 78]
  "§4.1k#p7": 85
  "§4.1k#r16": [84, 87, 88, 89, 134, 186]
  "§4.1k#r17": [84, 90, 91, 134, 170]
  "§4.1k#r18": [84, 92, 93, 134, 186]
  "§4.1k#r19": [84, 94, 96, 97, 134, 171]
  "§4.1k#r20": [84, 98, 100, 101, 134, 172]
  "§4.1k#r21": [84, 103, 104, 134, 173, 174]
  "§4.1k#r22": [84, 105, 106, 107, 108, 109, 110, 134, 175, 185]
  "§4.1k#r23": [135, 137, 138, 176]
  "§4.1k#r24": [135, 139, 141, 142, 177]
  "§4.1k#r25": [84, 112, 113, 134, 186]
  "§4.1k#r26": [84, 114, 116, 117, 134, 178]
  "§4.1k#r27": [84, 118, 120, 121, 134, 179]
  "§4.1k#r28": [84, 122, 123, 124, 125, 126, 127, 134, 180]
  "§4.1k#r29": [84, 128, 129, 134, 181]
  "§4.1k#r30": [135, 143, 145, 146, 147, 148, 186]
  "§4.1k#r31": [135, 149, 151, 153, 186]
  "§4.1k#r32": [135, 154, 156, 158, 186]
  "§4.1k#r33": [135, 159, 160, 162, 163, 182]
  "§4.1k#r34": [135, 164, 166, 167, 186]
  "§4.1k#r35": [84, 130, 131, 134, 183]
  "EB-TBL-1@tabel-history": [2, 3, 7, 8, 10, 11, 12, 14, 15, 19, 20, 22, 23]
  "EB-TBL-2@tabel-history": [56, 88, 97, 101, 121, 127, 129, 138, 147, 148, 153, 158, 167]
  "EB-TBL-4@tabel-history": [45, 47, 53, 55, 114, 116]
  "EB-TBL-12": [190, 191, 192]
anchor: []
coverage:
  web: automated
---
# Tabel History By Transaction dan By Asset: konfigurasi kolom dan rentang awal

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman `Transactions > Borrow`, tab History.
- Komponen: Tabel History
- Data:
  - DU-057-1: BRW selesai Returned dengan satu baris Rejected: Transaction ID `BRW-2026-0140`, Status `Returned`, Group `Head Office`, Hierarki Group `Head Office`, Borrower `Andi Pratama`, Borrower tampil `Andi P`, Total Asset `3`, Requested By `Rina Wijaya`, Requested By tampil `Rina W`, Source `Admin`, Request Date `20/10/26, 09:00`, Last Updated `25/10/26, 16:30`, Rincian baris `2 Returned, 1 Rejected`, Aset `Laptop Dell Latitude 5420 - 5 (Returned); Camera Sony A7 IV - 2 (Returned · Damaged); Projector Epson EB-X06 - 5 (Rejected)`, Nama pembuat `Rina Wijaya`.
  - DU-057-2: BRW Rejected dari pinjaman self-service: Transaction ID `BRW-2026-0141`, Status `Rejected`, Group `Branch Surabaya`, Hierarki Group `Head Office > Branch Surabaya`, Borrower `Dewi Lestari`, Borrower tampil `Dewi L`, Total Asset `2`, Requested By `kosong`, Requested By tampil `—`, Source `Self-service`, Request Date `21/10/26, 10:00`, Last Updated `21/10/26, 15:00`.
  - DU-057-3: BRW Canceled atas nama Borrower tanpa akun login dengan PIC: Transaction ID `BRW-2026-0142`, Status `Canceled`, Group `Head Office`, Hierarki Group `Head Office`, Borrower `Wawan Setiadi`, Borrower tampil `Wawan S`, Total Asset `1`, Requested By `Rina Wijaya`, Requested By tampil `Rina W`, Source `Self-service`, Request Date `22/10/26, 08:00`, Last Updated `22/10/26, 08:20`, PIC `Rina Wijaya`.
  - DU-057-4: Baris Returned terlambat dua hari dengan kolom curated terisi: Name `Laptop Dell Latitude 5420 - 5`, Asset ID `LPT-2026-0005`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Returned`, Transaction ID `BRW-2026-0140`, Borrower `Andi Pratama`, Borrower tampil `Andi P`, Handed Over At `21/10/26, 09:30`, Returned At `24/10/26, 17:00`, Extensions `1 / 1`, Last Updated `24/10/26, 17:00`, Due Date `22/10/26`, Keterlambatan `late 2 days`, TAG `RFID`, Category `Laptop`, Hierarki Category `IT Equipment > Laptop`, Reason `kosong`, Handover Photo `ada`, Return Photo `ada`, Source `Admin`, Nama pembuat `Rina Wijaya`, Purpose `Kunjungan lapangan`, Handed Over By `Agus Prasetyo`.
  - DU-057-5: Baris Returned dengan penanda Damaged, tepat waktu, tanpa foto: Name `Camera Sony A7 IV - 2`, Asset ID `CAM-2026-0002`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Status `Returned + Damaged`, Transaction ID `BRW-2026-0140`, Borrower `Andi Pratama`, Borrower tampil `Andi P`, Handed Over At `21/10/26, 09:35`, Returned At `25/10/26, 16:30`, Extensions `0 / 2`, Last Updated `25/10/26, 16:30`, Due Date `25/10/26`, TAG `Non TAG`, Reason `kosong`, Handover Photo `kosong`, Return Photo `kosong`, Source `Self-service`, Purpose `kosong`.
  - DU-057-6: Baris satuan jam Returned terlambat 3 jam: Name `Handheld Scanner Zebra - 5`, Asset ID `HHS-2026-0005`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Status `Returned`, Transaction ID `BRW-2026-0143`, Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Handed Over At `24/10/26, 08:00`, Returned At `24/10/26, 12:20`, Extensions `0 / 2`, Last Updated `24/10/26, 12:20`, Due Date `24/10/26, 10:00`, Keterlambatan `late 3 hours`.
  - DU-057-7: Baris satuan jam Returned terlambat 1 jam: Name `Handheld Scanner Zebra - 6`, Asset ID `HHS-2026-0006`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Status `Returned`, Transaction ID `BRW-2026-0143`, Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Handed Over At `24/10/26, 08:00`, Returned At `24/10/26, 10:40`, Extensions `0 / 2`, Last Updated `24/10/26, 10:40`, Due Date `24/10/26, 10:00`, Keterlambatan `late 1 hour`.
  - DU-057-8: Baris Rejected dengan alasan Reject: Name `Projector Epson EB-X06 - 5`, Asset ID `PRJ-2026-0005`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Status `Rejected`, Transaction ID `BRW-2026-0140`, Borrower `Andi Pratama`, Borrower tampil `Andi P`, Handed Over At `kosong`, Returned At `kosong`, Extensions `0 / 2`, Last Updated `21/10/26, 11:00`, Reason `Aset sedang menunggu perbaikan dan belum boleh dipinjamkan sampai pemeriksaan ulang oleh Asset Admin selesai`.
  - DU-057-9: Baris Canceled otomatis oleh sistem: Name `Toyota Avanza - 7`, Asset ID `VEH-2026-0007`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Status `Canceled`, Transaction ID `BRW-2026-0142`, Borrower `Wawan Setiadi`, Borrower tampil `Wawan S`, Handed Over At `kosong`, Returned At `kosong`, Extensions `0 / 2`, Last Updated `22/10/26, 08:20`, Reason `Not picked up`.
  - DU-057-10: Baris Canceled manual tanpa Reason: Name `Toyota Avanza - 8`, Asset ID `VEH-2026-0008`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Status `Canceled`, Transaction ID `BRW-2026-0142`, Borrower `Wawan Setiadi`, Borrower tampil `Wawan S`, Handed Over At `kosong`, Returned At `kosong`, Extensions `0 / 2`, Last Updated `22/10/26, 08:20`, Reason `kosong`.
  - DU-057-11: Baris Returned dengan penanda Missing: Name `Laptop Dell Latitude 5420 - 6`, Asset ID `LPT-2026-0006`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Status `Returned + Missing`, Transaction ID `BRW-2026-0144`, Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Handed Over At `20/10/26, 09:00`, Returned At `23/10/26, 15:00`, Extensions `0 / 2`, Last Updated `23/10/26, 15:00`, Due Date `23/10/26`.
  - DU-057-12: Kata kunci tanpa hasil yang diketik pada tabel: Search tanpa hasil `Tidak Ada`.
- Kondisi:
  - K1: tabel By Transaction dimuat berisi DU-057-1 sampai DU-057-3; Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.
  - K2: tabel By Transaction dimuat tanpa data sama sekali.
  - K3: memuat tabel By Transaction gagal karena error server.
  - K4: seperti K1; pencarian `Tidak Ada` dijawab tanpa baris.
  - K5: tabel By Asset dimuat berisi DU-057-4 sampai DU-057-11; Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`; jatah Extend maksimum aset bernilai `2`.
  - K6: tabel By Asset dimuat tanpa data sama sekali.
  - K7: memuat tabel By Asset gagal karena error server.
  - K8: seperti K5; pencarian `Tidak Ada` dijawab tanpa baris.
  - K9: seperti K5; bahasa aktif pengguna adalah bahasa selain English.

## Test Steps

### By Transaction kosong alami
1. Tampilkan Tabel History By Transaction dengan kondisi K2
2. Verifikasi judul `No finished borrows yet` tampil pada tabel History By Transaction
3. Verifikasi deskripsi `Returned, rejected, and canceled borrows will appear here.` tampil pada tabel History By Transaction

### By Transaction kosong akibat pencarian tanpa hasil
4. Tampilkan Tabel History By Transaction dengan kondisi K4
5. Klik ikon Search pada toolbar By Transaction
6. Ketik Search `Tidak Ada`, tekan Enter
7. Verifikasi judul `No results found` tampil pada tabel History By Transaction
8. Verifikasi deskripsi `Try adjusting your search or filter.` tampil pada tabel History By Transaction

### By Transaction gagal muat bukan empty state
9. Tampilkan Tabel History By Transaction dengan kondisi K3
10. Verifikasi pesan `Unable to load this data.` tampil pada tabel History By Transaction
11. Verifikasi tombol `[Try Again]` tampil pada tabel History By Transaction
12. Verifikasi judul `No finished borrows yet` tidak tampil karena gagal muat bukan empty state

### By Asset kosong alami
13. Tampilkan Tabel History By Asset dengan kondisi K6
14. Verifikasi judul `No finished borrows yet` tampil pada tabel History By Asset
15. Verifikasi deskripsi `Returned, rejected, and canceled borrows will appear here.` tampil pada tabel History By Asset

### By Asset kosong akibat pencarian tanpa hasil
16. Tampilkan Tabel History By Asset dengan kondisi K8
17. Klik ikon Search pada toolbar By Asset
18. Ketik Search `Tidak Ada`, tekan Enter
19. Verifikasi judul `No results found` tampil pada tabel History By Asset
20. Verifikasi deskripsi `Try adjusting your search or filter.` tampil pada tabel History By Asset

### By Asset gagal muat bukan empty state
21. Tampilkan Tabel History By Asset dengan kondisi K7
22. Verifikasi pesan `Unable to load this data.` tampil pada tabel History By Asset
23. Verifikasi tombol `[Try Again]` tampil pada tabel History By Asset

### By Transaction: tanpa checkbox, kolom Actions, dan urutan kolom
24. Tampilkan Tabel History By Transaction dengan kondisi K1
25. Verifikasi tabel History By Transaction tidak memiliki kolom Checkbox maupun bar Bulk Action
26. Klik `⋯` pada baris `BRW-2026-0140`
27. Verifikasi menu baris tabel History By Transaction memuat aksi `Detail`
28. Tekan Esc
29. Verifikasi urutan kolom data dari kiri ke kanan: `Transaction ID`, `Status`, `Group`, `Borrower`, `Total Asset`, `Requested By`, `Request Date`, `Last Updated` pada tabel History By Transaction
30. Verifikasi Transaction ID `BRW-2026-0140` tampil pada satu baris saja, satu baris untuk satu BRW selesai

### By Transaction: Transaction ID, Status, dan Group
31. Tampilkan Tabel History By Transaction dengan kondisi K1
32. Verifikasi Transaction ID `BRW-2026-0140` tampil sebagai tautan
33. Verifikasi setiap baris tabel History By Transaction memuat Transaction ID
34. Verifikasi baris `BRW-2026-0140` memuat badge status header `Returned`
35. Verifikasi baris `BRW-2026-0140` tidak memuat badge penanda `Damaged` maupun `Missing`
36. Arahkan kursor ke badge status baris `BRW-2026-0140`
37. Verifikasi rincian baris `Returned` dan `Rejected` tampil
38. Verifikasi baris `BRW-2026-0141` memuat badge status `Rejected` dan baris `BRW-2026-0142` memuat badge status `Canceled`
39. Verifikasi setiap baris tabel History By Transaction memuat badge status
40. Verifikasi badge Group `Head Office` baris `BRW-2026-0140` memakai severity `primary`
41. Arahkan kursor ke badge Group baris `BRW-2026-0141`
42. Verifikasi hierarki `Head Office > Branch Surabaya` tampil pada tooltip Group tabel History By Transaction
43. Verifikasi setiap baris tabel History By Transaction memuat badge Group

### By Transaction: Borrower, Total Asset, Requested By, dan tanggal
44. Tampilkan Tabel History By Transaction dengan kondisi K1
45. Verifikasi Borrower baris `BRW-2026-0140` tampil `Andi P`
46. Arahkan kursor ke Borrower baris `BRW-2026-0140`
47. Verifikasi nama lengkap `Andi Pratama` tampil pada tooltip Borrower tabel History By Transaction
48. Verifikasi setiap baris tabel History By Transaction memuat Borrower
49. Verifikasi Total Asset baris `BRW-2026-0140` bernilai `3` sebagai angka bulat
50. Arahkan kursor ke Total Asset baris `BRW-2026-0140`
51. Verifikasi baris `Laptop Dell Latitude 5420 - 5` berstatus `Returned`, `Camera Sony A7 IV - 2` berstatus `Returned · Damaged`, dan `Projector Epson EB-X06 - 5` berstatus `Rejected` tampil
52. Verifikasi setiap baris tabel History By Transaction memuat Total Asset
53. Verifikasi Requested By baris `BRW-2026-0140` tampil `Rina W`
54. Arahkan kursor ke Requested By baris `BRW-2026-0140`
55. Verifikasi nama lengkap `Rina Wijaya` tampil pada tooltip Requested By
56. Verifikasi Requested By baris `BRW-2026-0141` tampil `—`
57. Verifikasi Request Date baris `BRW-2026-0140` tampil `20/10/26, 09:00`
58. Verifikasi Last Updated baris `BRW-2026-0140` tampil `25/10/26, 16:30`
59. Verifikasi setiap baris tabel History By Transaction memuat Request Date dan Last Updated

### By Transaction: toggle Setup Column dan kolom Source
60. Tampilkan Tabel History By Transaction dengan kondisi K1
61. Klik header kolom Actions `⋯`
62. Verifikasi checkbox `Transaction ID`, `Status`, `Group`, `Borrower`, `Total Asset`, `Requested By`, `Request Date`, dan `Last Updated` tercentang dan enabled pada tabel History By Transaction
63. Verifikasi checkbox `Source` tidak tercentang dan enabled pada tabel History By Transaction
64. Centang kolom `Source` pada daftar Column Visibility
65. Verifikasi badge Source `Admin` memakai severity `dark` pada baris `BRW-2026-0140`
66. Verifikasi badge Source `Self-service` memakai severity `primary` pada baris `BRW-2026-0141`
67. Verifikasi setiap baris tabel History By Transaction memuat badge Source

### By Transaction: field dan placeholder Filter Panel
68. Tampilkan Tabel History By Transaction dengan kondisi K1
69. Klik ikon Filter pada toolbar By Transaction
70. Verifikasi placeholder `All statuses` tampil pada field `Status` di Filter Panel History By Transaction
71. Verifikasi field `Group` di Filter Panel History By Transaction berupa dropdown multi-pilih dengan kotak cari, bukan pemilih tree
72. Verifikasi placeholder `All groups` tampil pada field `Group` di Filter Panel History By Transaction
73. Verifikasi placeholder `All borrowers` tampil pada field `Borrower` di Filter Panel History By Transaction
74. Verifikasi input pertama field `Total Asset` di Filter Panel History By Transaction memakai placeholder `Min` dan input kedua memakai placeholder `Max`
75. Verifikasi placeholder `All sources` tampil pada field `Source` di Filter Panel History By Transaction
76. Verifikasi placeholder `All users` tampil pada field `Requested By` di Filter Panel History By Transaction
77. Verifikasi placeholder `Select date` tampil pada field `Request Date` di Filter Panel History By Transaction
78. Verifikasi placeholder `Select date` tampil pada field `Last Updated` di Filter Panel History By Transaction

### By Asset: tanpa checkbox, kolom Actions, dan urutan kolom
79. Tampilkan Tabel History By Asset dengan kondisi K5
80. Verifikasi tabel History By Asset tidak memiliki kolom Checkbox maupun bar Bulk Action
81. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 5`
82. Verifikasi menu baris tabel History By Asset memuat aksi `Borrow Log`
83. Tekan Esc
84. Verifikasi urutan kolom data dari kiri ke kanan: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Transaction ID`, `Borrower`, `Handed Over At`, `Returned At`, `Extensions`, `Last Updated`
85. Verifikasi baris `Laptop Dell Latitude 5420 - 5` dan baris `Camera Sony A7 IV - 2` sama-sama memuat Transaction ID `BRW-2026-0140`, satu baris untuk tiap aset yang selesai

### By Asset: Photo, Name, Asset ID, Brand, dan Model/Type
86. Tampilkan Tabel History By Asset dengan kondisi K5
87. Verifikasi baris `Laptop Dell Latitude 5420 - 5` menampilkan foto utama aset
88. Verifikasi baris `Handheld Scanner Zebra - 5` menampilkan placeholder gambar standar
89. Verifikasi header kolom `Photo` pada tabel History By Asset tidak memiliki ikon sort
90. Verifikasi Name `Laptop Dell Latitude 5420 - 5` tampil dengan format nama aset dan increment
91. Verifikasi setiap baris tabel History By Asset memuat Name
92. Verifikasi Asset ID `LPT-2026-0005` tampil pada baris `Laptop Dell Latitude 5420 - 5`
93. Verifikasi setiap baris tabel History By Asset memuat Asset ID
94. Verifikasi Brand baris `Laptop Dell Latitude 5420 - 5` tampil sebagai badge `Dell` dengan severity `dark`
95. Arahkan kursor ke badge Brand baris `Laptop Dell Latitude 5420 - 5`
96. Verifikasi nama Brand penuh `Dell` tampil pada tooltip Brand
97. Verifikasi Brand baris `Camera Sony A7 IV - 2` tampil `—`
98. Verifikasi Model/Type baris `Laptop Dell Latitude 5420 - 5` tampil sebagai badge `Latitude 5420` dengan severity `dark`
99. Arahkan kursor ke badge Model/Type baris `Laptop Dell Latitude 5420 - 5`
100. Verifikasi nama Model penuh `Latitude 5420` tampil pada tooltip Model/Type
101. Verifikasi Model/Type baris `Camera Sony A7 IV - 2` tampil `—`

### By Asset: Group dan Status
102. Tampilkan Tabel History By Asset dengan kondisi K5
103. Verifikasi badge Group `Head Office` baris `Laptop Dell Latitude 5420 - 5` memakai severity `primary` pada tabel History By Asset
104. Verifikasi setiap baris tabel History By Asset memuat badge Group
105. Verifikasi baris `Laptop Dell Latitude 5420 - 5` memuat badge status `Returned` tanpa badge kedua
106. Verifikasi baris `Camera Sony A7 IV - 2` memuat badge status `Returned` dan badge kedua `Damaged`
107. Verifikasi baris `Laptop Dell Latitude 5420 - 6` memuat badge status `Returned` dan badge kedua `Missing`
108. Verifikasi baris `Projector Epson EB-X06 - 5` memuat badge status `Rejected`
109. Verifikasi baris `Toyota Avanza - 7` memuat badge status `Canceled`
110. Verifikasi setiap baris tabel History By Asset memuat badge status

### By Asset: Transaction ID, Borrower, dan tanggal
111. Tampilkan Tabel History By Asset dengan kondisi K5
112. Verifikasi Transaction ID `BRW-2026-0140` baris `Laptop Dell Latitude 5420 - 5` tampil sebagai tautan
113. Verifikasi setiap baris tabel History By Asset memuat Transaction ID
114. Verifikasi Borrower baris `Laptop Dell Latitude 5420 - 5` tampil `Andi P`
115. Arahkan kursor ke Borrower baris `Laptop Dell Latitude 5420 - 5`
116. Verifikasi nama lengkap `Andi Pratama` tampil pada tooltip Borrower tabel History By Asset
117. Verifikasi setiap baris tabel History By Asset memuat Borrower
118. Verifikasi Handed Over At baris `Laptop Dell Latitude 5420 - 5` tampil `21/10/26, 09:30`
119. Arahkan kursor ke Handed Over At baris `Laptop Dell Latitude 5420 - 5`
120. Verifikasi pemberi handover `Agus Prasetyo` tampil pada tooltip Handed Over At tabel History By Asset
121. Verifikasi Handed Over At baris `Projector Epson EB-X06 - 5` tampil `—` karena tidak pernah diserahkan
122. Verifikasi Returned At baris `Laptop Dell Latitude 5420 - 5` tampil `24/10/26, 17:00`
123. Verifikasi penanda `late 2 days` tampil pada Returned At baris `Laptop Dell Latitude 5420 - 5` dengan severity `danger`
124. Verifikasi penanda `late 3 hours` tampil pada Returned At baris `Handheld Scanner Zebra - 5`
125. Verifikasi penanda `late 1 hour` tampil pada Returned At baris `Handheld Scanner Zebra - 6`
126. Verifikasi Returned At baris `Camera Sony A7 IV - 2` tidak memuat penanda `late` karena dikembalikan pada Due date
127. Verifikasi Returned At baris `Projector Epson EB-X06 - 5` dan baris `Toyota Avanza - 7` tampil `—`
128. Verifikasi Extensions baris `Laptop Dell Latitude 5420 - 5` tampil `1 / 1`
129. Verifikasi Extensions baris `Camera Sony A7 IV - 2` tampil `0 / 2`
130. Verifikasi Last Updated baris `Laptop Dell Latitude 5420 - 5` tampil `24/10/26, 17:00`
131. Verifikasi kolom `Last Updated` menjadi kolom data terakhir sebelum Actions pada tabel History By Asset

### By Asset: toggle Setup Column dan kolom curated
132. Tampilkan Tabel History By Asset dengan kondisi K5
133. Klik header kolom Actions `⋯`
134. Verifikasi checkbox `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Transaction ID`, `Borrower`, `Handed Over At`, `Returned At`, `Extensions`, dan `Last Updated` tercentang dan enabled pada tabel History By Asset
135. Verifikasi checkbox `TAG`, `Category`, `Reason`, `Handover Photo`, `Return Photo`, `Source`, dan `Purpose` tidak tercentang dan enabled pada tabel History By Asset
136. Centang kolom `TAG`, `Category`, `Reason`, `Handover Photo`, `Return Photo`, `Source`, dan `Purpose` pada daftar Column Visibility
137. Verifikasi baris `Laptop Dell Latitude 5420 - 5` menampilkan satu ikon TAG dengan label `RFID`
138. Verifikasi TAG baris `Camera Sony A7 IV - 2` tampil `—` karena `Non TAG`
139. Verifikasi badge Category `Laptop` baris `Laptop Dell Latitude 5420 - 5` tampil dengan severity `primary`
140. Arahkan kursor ke badge Category baris `Laptop Dell Latitude 5420 - 5`
141. Verifikasi hierarki `IT Equipment > Laptop` tampil pada tooltip Category tabel History By Asset
142. Verifikasi setiap baris tabel History By Asset memuat Category
143. Verifikasi Reason baris `Projector Epson EB-X06 - 5` tampil dalam satu baris
144. Arahkan kursor ke Reason baris `Projector Epson EB-X06 - 5`
145. Verifikasi teks penuh `Aset sedang menunggu perbaikan dan belum boleh dipinjamkan sampai pemeriksaan ulang oleh Asset Admin selesai` tampil
146. Verifikasi Reason baris `Toyota Avanza - 7` tampil `Not picked up`
147. Verifikasi Reason baris `Laptop Dell Latitude 5420 - 5` tampil `—` karena Returned
148. Verifikasi Reason baris `Toyota Avanza - 8` tampil `—` karena Cancel manual
149. Verifikasi Handover Photo baris `Laptop Dell Latitude 5420 - 5` tampil sebagai thumbnail
150. Klik thumbnail Handover Photo baris `Laptop Dell Latitude 5420 - 5`
151. Verifikasi pratinjau foto handover tampil
152. Tekan Esc
153. Verifikasi Handover Photo baris `Camera Sony A7 IV - 2` tampil `—` karena foto tidak ada
154. Verifikasi Return Photo baris `Laptop Dell Latitude 5420 - 5` tampil sebagai thumbnail
155. Klik thumbnail Return Photo baris `Laptop Dell Latitude 5420 - 5`
156. Verifikasi pratinjau foto return tampil
157. Tekan Esc
158. Verifikasi Return Photo baris `Camera Sony A7 IV - 2` tampil `—` karena foto tidak ada
159. Verifikasi badge Source `Admin` baris `Laptop Dell Latitude 5420 - 5` memakai severity `dark` pada tabel History By Asset
160. Verifikasi badge Source `Self-service` baris `Camera Sony A7 IV - 2` memakai severity `primary` pada tabel History By Asset
161. Arahkan kursor ke badge Source `Admin` baris `Laptop Dell Latitude 5420 - 5`
162. Verifikasi nama pembuat `Rina Wijaya` tampil pada tooltip Source tabel History By Asset
163. Verifikasi setiap baris tabel History By Asset memuat badge Source
164. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 5` tampil `Kunjungan lapangan` dalam satu baris
165. Arahkan kursor ke Purpose baris `Laptop Dell Latitude 5420 - 5`
166. Verifikasi teks penuh Purpose `Kunjungan lapangan` tampil
167. Verifikasi Purpose baris `Camera Sony A7 IV - 2` tampil `—`

### By Asset: field dan placeholder Filter Panel
168. Tampilkan Tabel History By Asset dengan kondisi K5
169. Klik ikon Filter pada toolbar By Asset
170. Verifikasi placeholder `All asset names` tampil pada field `Asset Name` di Filter Panel History By Asset
171. Verifikasi placeholder `All brands` tampil pada field `Brand` di Filter Panel History By Asset
172. Verifikasi placeholder `All models` tampil pada field `Model/Type` di Filter Panel History By Asset
173. Verifikasi placeholder `All groups` tampil pada field `Group` di Filter Panel History By Asset
174. Verifikasi field `Group` di Filter Panel History By Asset berupa dropdown multi-pilih dengan kotak cari, bukan pemilih tree
175. Verifikasi placeholder `All statuses` tampil pada field `Status` di Filter Panel History By Asset
176. Verifikasi placeholder `All tags` tampil pada field `TAG` di Filter Panel History By Asset
177. Verifikasi placeholder `All categories` tampil pada field `Category` di Filter Panel History By Asset
178. Verifikasi placeholder `All borrowers` tampil pada field `Borrower` di Filter Panel History By Asset
179. Verifikasi placeholder `Select date` tampil pada field `Handed Over At` di Filter Panel History By Asset
180. Verifikasi placeholder `Select date` tampil pada field `Returned At` di Filter Panel History By Asset
181. Verifikasi input pertama field `Extensions` di Filter Panel History By Asset memakai placeholder `Min` dan input kedua memakai placeholder `Max`
182. Verifikasi placeholder `All sources` tampil pada field `Source` di Filter Panel History By Asset
183. Verifikasi placeholder `Select date` tampil pada field `Last Updated` di Filter Panel History By Asset
184. Klik field `Status` pada Filter Panel History By Asset
185. Verifikasi opsi `Returned`, `Returned · Damaged`, `Returned · Missing`, `Rejected`, dan `Canceled` tampil pada field `Status`
186. Verifikasi Filter Panel History By Asset tidak memuat field `Photo`, `Asset ID`, `Transaction ID`, `Reason`, `Handover Photo`, `Return Photo`, maupun `Purpose`

### Kolom Verbatim dan Translatable mengikuti bahasa aktif
187. Tampilkan Tabel History By Asset dengan kondisi K9
188. Klik header kolom Actions `⋯`
189. Centang kolom `Reason` pada daftar Column Visibility
190. Verifikasi Reason Reject baris `Projector Epson EB-X06 - 5` tampil persis `Aset sedang menunggu perbaikan dan belum boleh dipinjamkan sampai pemeriksaan ulang oleh Asset Admin selesai` seperti yang diinput
191. Verifikasi Name `Projector Epson EB-X06 - 5` tampil persis seperti yang diinput
192. Verifikasi alasan sistem pada baris `Toyota Avanza - 7` tampil dalam bahasa aktif
