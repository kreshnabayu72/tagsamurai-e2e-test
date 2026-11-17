---
id: TC-FA-MYASSET-UI-114-tabel-history-tampilan-sel
title: "Tabel History: format sel, caption late, Holder, badge Type, dan aksi baris menurut jenis transaksi"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-15", "§1.2#r7", "§1.2#r37", "§1.2#r38", "§1.2#r45", "§1.2#r81", "§4.1#p5", "§4.1c#r1", "§4.1c#r2", "§4.1c#r3", "§4.1c#r4", "§4.1c#r5", "§4.1c#r6", "§4.1c#r7", "§4.1c#r8", "§4.1c#r9", "§4.1c#r10", "§4.1c#r11", "§4.1c#r12", "§4.1c#r13", "§4.1c#r14", "§4.1c#r15", "§4.1c#r16", "§4.1c#r17", "§4.1c#p3", "§4.1c#r18", "§4.1c#r19", "§4.1c#p7", "§4.3#r6", "§4.4#r50", "§4.4#r51", "§5#r9", "§9.2#b12", "§9.2#b13", "§9.2#r20", "§9.2#r21"]
smoke: []
dependsOn: []
trace:
  "FI-15": 9
  "§1.2#r7": 6
  "§1.2#r37": [42, 44]
  "§1.2#r38": [18, 40, 41]
  "§1.2#r45": [40, 45, 47]
  "§1.2#r81": [69, 70]
  "§4.1#p5": [22, 54]
  "§4.1c#r1": [4, 98]
  "§4.1c#r2": [3, 75]
  "§4.1c#r3": 5
  "§4.1c#r4": [77, 83, 99]
  "§4.1c#r5": [79, 83, 100]
  "§4.1c#r6": [19, 81]
  "§4.1c#r7": [12, 13, 14, 15, 16, 49, 50, 51, 52, 105]
  "§4.1c#r8": [18, 40, 42, 44, 45, 47]
  "§4.1c#r9": [84, 101]
  "§4.1c#r10": [85, 87]
  "§4.1c#r11": [21, 53]
  "§4.1c#r12": [20, 55]
  "§4.1c#r13": [24, 25, 56, 59]
  "§4.1c#r14": [26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 57, 58, 112, 113]
  "§4.1c#r15": [88, 90, 102]
  "§4.1c#r16": [92, 94, 103, 107, 109]
  "§4.1c#r17": 96
  "§4.1c#p3": [62, 63, 69, 70]
  "§4.1c#r18": 62
  "§4.1c#r19": 69
  "§4.1c#p7": [62, 63, 69]
  "§4.3#r6": [29, 30, 32, 33]
  "§4.4#r50": 8
  "§4.4#r51": [65, 72]
  "§5#r9": 6
  "§9.2#b12": [56, 57, 69]
  "§9.2#b13": [29, 30, 31, 32, 33, 34, 35, 113]
  "§9.2#r20": [12, 13, 14, 15, 16, 49, 50, 51, 52, 105]
  "§9.2#r21": 10
anchor: [2]
coverage:
  web: automated
---

# Tabel History: format sel, caption late, Holder, badge Type, dan aksi baris menurut jenis transaksi

## Prerequisites
- Aktor: Budi Santoso, pengguna yang login sebagai Borrower, Assignee, dan PIC atas baris yang tampil.
- Layar awal: halaman My Asset, tab History.
- Komponen: Tabel History (T-MYA-03)
- Data:
  - DU-114-1: Baris History Name `Laptop Dell Latitude 5420 - 12`, Asset ID `LPT-2026-0012`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Returned`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0151`, Handed Over At `01/11/26, 09:00`, Closed At `08/11/26, 11:00`, Due Date `06/11/26`, Satuan `Days`, Photo `foto-LPT-2026-0012.jpg`.
  - DU-114-2: Baris History Name `Projector Epson EB-X06 - 5`, Asset ID `PRJ-2026-0005`, Brand `Epson`, Model/Type `EB-X06`, Group `Head Office`, Status `Returned`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0158`, Handed Over At `05/11/26, 09:00`, Closed At `08/11/26, 10:00`, Due Date `07/11/26`, Satuan `Days`, Photo `foto-PRJ-2026-0005.jpg`.
  - DU-114-3: Baris History Name `Projector Epson EB-X06 - 6`, Asset ID `PRJ-2026-0006`, Brand `Epson`, Model/Type `EB-X06`, Group `Head Office`, Status `Returned`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0159`, Handed Over At `05/11/26, 09:00`, Closed At `08/11/26, 09:15`, Due Date `08/11/26`, Satuan `Days`, Photo `foto-PRJ-2026-0006.jpg`.
  - DU-114-4: Baris History Name `Meeting Mic Set - 2`, Asset ID `MIC-2026-0002`, Brand `Shure`, Model/Type `SM58`, Group `Head Office`, Status `Returned`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0156`, Handed Over At `08/11/26, 08:00`, Closed At `08/11/26, 12:30`, Due Date `08/11/26, 11:00`, Satuan `Hours`, Photo `foto-MIC-2026-0002.jpg`.
  - DU-114-5: Baris History Name `Meeting Mic Set - 4`, Asset ID `MIC-2026-0004`, Brand `Shure`, Model/Type `SM58`, Group `Head Office`, Status `Returned`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0160`, Handed Over At `08/11/26, 06:00`, Closed At `08/11/26, 14:10`, Due Date `08/11/26, 09:00`, Satuan `Hours`, Photo `foto-MIC-2026-0004.jpg`.
  - DU-114-6: Baris History Name `Meeting Mic Set - 6`, Asset ID `MIC-2026-0006`, Brand `Shure`, Model/Type `SM58`, Group `Head Office`, Status `Returned`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0161`, Handed Over At `08/11/26, 06:00`, Closed At `08/11/26, 09:40`, Due Date `08/11/26, 09:00`, Satuan `Hours`, Photo `foto-MIC-2026-0006.jpg`.
  - DU-114-7: Baris History Name `Meeting Mic Set - 3`, Asset ID `MIC-2026-0003`, Brand `Shure`, Model/Type `SM58`, Group `Head Office`, Status `Returned · Missing`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0155`, Handed Over At `03/11/26, 10:00`, Closed At `07/11/26, 13:30`, Due Date `06/11/26`, Satuan `Days`, Photo `foto-MIC-2026-0003.jpg`.
  - DU-114-8: Baris History Name `Laptop Dell Latitude 5420 - 44`, Asset ID `LPT-2026-0044`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Returned · Damaged`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0140`, Handed Over At `30/10/26, 09:00`, Closed At `05/11/26, 16:00`, Due Date `02/11/26`, Satuan `Days`, Photo `foto-LPT-2026-0044.jpg`.
  - DU-114-9: Baris History Name `Laptop Dell Latitude 5420 - 6`, Asset ID `LPT-2026-0006`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Canceled`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0140`, Handed Over At kosong, Closed At `04/11/26, 14:10`, Photo `foto-LPT-2026-0006.jpg`.
  - DU-114-10: Baris History Name `Excavator PC200 - 2`, Asset ID `EXC-2026-0008`, Brand `Caterpillar`, Model/Type `PC200`, Group `Head Office`, Status `Rejected`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0146`, Handed Over At kosong, Closed At `31/10/26, 11:30`, Photo `foto-EXC-2026-0008.jpg`.
  - DU-114-11: Baris History Name `Toyota Avanza - 6`, Asset ID `VEH-2026-0006`, Brand `Toyota`, Model/Type `Avanza`, Group `Head Office`, Status `Unassigned · Missing`, Holder `Me`, Type `Assignment`, Transaction ID `ASG-2026-0012`, Handed Over At `15/09/26, 10:00`, Closed At `02/11/26, 14:00`, Photo `foto-VEH-2026-0006.jpg`.
  - DU-114-12: Baris History Name `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Brand `Epson`, Model/Type `EB-X06`, Group `Head Office`, Status `Unassigned`, Holder `Me`, Type `Assignment`, Transaction ID `ASG-2026-0009`, Handed Over At `03/07/26, 10:00`, Closed At `30/10/26, 15:20`, Photo `foto-PRJ-2026-0002.jpg`.
  - DU-114-13: Baris History Name `Printer HP M404 - 1`, Asset ID `PRN-2026-0001`, Brand `HP`, Model/Type `M404`, Group `Branch Surabaya`, Status `Unassigned`, Holder `Finance`, Type `Assignment`, Transaction ID `ASG-2026-0013`, Handed Over At `01/08/26, 10:00`, Closed At `28/10/26, 16:00`, Photo `foto-PRN-2026-0001.jpg`, tooltip Holder `PIC: Budi Santoso`.
  - DU-114-14: Baris History Name `Toyota Avanza - 5`, Asset ID `VEH-2026-0005`, Brand `Toyota`, Model/Type `Avanza`, Group `Head Office`, Status `Rejected`, Holder `Me`, Type `Assignment`, Transaction ID `ASG-2026-0011`, Handed Over At kosong, Closed At `21/09/26, 13:15`, Photo `foto-VEH-2026-0005.jpg`.
  - DU-114-15: Baris History Name `Laptop Dell Latitude 5420 - 5`, Asset ID `LPT-2026-0005`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Canceled`, Holder `Me`, Type `Assignment`, Transaction ID `ASG-2026-0010`, Handed Over At kosong, Closed At `06/09/26, 08:45`, Photo `foto-LPT-2026-0005.jpg`.
  - DU-114-16: Baris History Name `Tablet Samsung Galaxy Tab A9 - 3`, Asset ID `TAB-2026-0003`, Brand `Samsung`, Model/Type `Galaxy Tab A9`, Group `Head Office`, Status `Returned`, Holder `Budi S`, Type `Borrow`, Transaction ID `BRW-2026-0162`, Handed Over At `03/11/26, 09:30`, Closed At `06/11/26, 15:00`, Due Date `07/11/26`, Satuan `Days`, Photo `foto-TAB-2026-0003.jpg`, tooltip Holder `Budi Setiawan · PIC: Budi Santoso`.
  - DU-114-17: Baris History Name `Laptop Dell Latitude 5420 Edisi Khusus Kantor Pengadaan dan Manajemen Vendor Regional Jakarta - 7`, Asset ID `LPT-2026-0007`, Brand `Dell Technologies Indonesia Authorized Distributor`, Model/Type `Latitude 5420 Rugged Extreme Edition`, Group `Regional Procurement and Vendor Management Office Jakarta`, Status `Returned`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0170`, Handed Over At `02/11/26, 09:00`, Closed At `05/11/26, 10:00`, Due Date `06/11/26`, Satuan `Days`, Photo `foto-LPT-2026-0007.jpg`, hierarki Group `Head Office` lalu `Regional Procurement and Vendor Management Office Jakarta`.
  - DU-114-18: Baris History Name `Meeting Mic Set - 5`, Asset ID `MIC-2026-0005`, Brand `Shure`, Model/Type `SM58`, Group `Pengadaan`, Status `Returned`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0171`, Handed Over At `04/11/26, 09:00`, Closed At `06/11/26, 09:30`, Due Date `07/11/26`, Satuan `Days`, Photo `foto-MIC-2026-0005.jpg`, hierarki Group `Head Office` lalu `Pengadaan`, TAG `QR Code` dan `RFID`, Category `Audio Visual`, hierarki Category `Peralatan Kantor` lalu `Audio Visual`, Handover Photo `handover-MIC-2026-0005.jpg`, Return Photo `return-MIC-2026-0005.jpg`, Purpose `Rapat koordinasi vendor pengadaan peralatan audio visual untuk seluruh kantor cabang wilayah Jawa Timur`.
  - DU-114-19: Baris History Name `Laptop Dell Latitude 5420 - 15`, Asset ID `LPT-2026-0015`, Brand kosong, Model/Type kosong, Group `Head Office`, Status `Returned`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0172`, Handed Over At `04/11/26, 09:00`, Closed At `06/11/26, 09:45`, Due Date `07/11/26`, Satuan `Days`, Photo kosong, TAG `Non TAG`, Category `Laptop`, Handover Photo kosong, Return Photo kosong, Purpose `Keperluan operasional kantor`.
  - DU-114-20: Baris History Name `Toyota Avanza - 7`, Asset ID `VEH-2026-0007`, Brand `Toyota`, Model/Type `Avanza`, Group `Head Office`, Status `Unassigned · Damaged`, Holder `Me`, Type `Assignment`, Transaction ID `ASG-2026-0014`, Handed Over At `10/08/26, 10:00`, Closed At `29/10/26, 11:00`, Photo `foto-VEH-2026-0007.jpg`.
  - DU-114-21: Baris History Name `Toyota Avanza - 8`, Asset ID `VEH-2026-0008`, Brand `Toyota`, Model/Type `Avanza`, Group `Head Office`, Status `Unassigned`, Holder `Me`, Type `Assignment`, Transaction ID `ASG-2026-0015`, Handed Over At `12/08/26, 10:00`, Closed At `27/10/26, 14:30`, Photo `foto-VEH-2026-0008.jpg`, Return Photo (foto Unassign) `unassign-VEH-2026-0008.jpg`.
  - DU-114-22: Baris History Name `Laptop Dell Latitude 5420 - 31`, Asset ID `LPT-2026-0031`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Returned`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0173`, Handed Over At `04/11/26, 09:00`, Closed At `08/11/26, 00:10` menurut Time Zone General Settings (waktu yang sama di UTC adalah `07/11/26, 17:10`), Due Date `06/11/26`, Satuan `Days`, Photo `foto-LPT-2026-0031.jpg`; selisih hari kalender dari Due Date menurut Time Zone General Settings adalah 2 hari (`late 2 days`), sedangkan menurut UTC hanya 1 hari.
  - Caption late dihitung dari Due Date dan Closed At: DU-114-1 selisih 2 hari kalender (`late 2 days`), DU-114-2 selisih 1 hari (`late 1 day`), DU-114-8 selisih 3 hari (`late 3 days`), DU-114-4 selisih 1 jam penuh (`late 1 hour`), DU-114-5 selisih 5 jam penuh (`late 5 hours`).
- Kondisi:
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`; semua tanggal pada data ditulis menurut Time Zone General Settings yang sama.
  - K1: tabel History memuat baris pinjaman DU-114-1 sampai DU-114-10.
  - K2: tabel History memuat baris penugasan DU-114-11 sampai DU-114-15 dan DU-114-20, serta baris pinjaman Borrower tanpa akun DU-114-16.
  - K3: tabel History memuat DU-114-17.
  - K4: tabel History memuat DU-114-18, DU-114-19, dan baris penugasan DU-114-21, dengan kolom TAG, Category, Handover Photo, Return Photo, dan Purpose ditampilkan.
  - K5: tabel History memuat DU-114-22.

## Test Steps

### Identitas aset, Name tanpa tautan, dan kolom yang tidak ada pada tabel History
1. Tampilkan Tabel History dengan kondisi K1
2. Verifikasi header kolom `Status`, `Holder`, `Type`, `Transaction ID`, `Handed Over At`, dan `Closed At` tampil
3. Verifikasi baris DU-114-1 menampilkan Name `Laptop Dell Latitude 5420 - 12`
4. Verifikasi baris yang sama menampilkan foto utama aset pada kolom Photo
5. Verifikasi baris yang sama menampilkan Asset ID `LPT-2026-0012`
6. Verifikasi header kolom `Photo`, `Name`, `Asset ID`, `Brand`, dan `Model/Type` tampil sebagai blok identitas aset
7. Klik Name `Laptop Dell Latitude 5420 - 12`
8. Verifikasi Name bukan tautan: klik tidak membuka dialog dan tidak berpindah halaman
9. Verifikasi kotak centang baris dan bulk action tidak tampil pada tabel
10. Verifikasi kolom `Reason` tidak tampil pada tabel

### Status akhir dan marker pada kolom Status baris pinjaman
11. Tampilkan Tabel History dengan kondisi K1
12. Verifikasi baris `Laptop Dell Latitude 5420 - 12` menampilkan Status `Returned`
13. Verifikasi baris `Meeting Mic Set - 3` menampilkan Status `Returned` dengan badge kedua `Missing`
14. Verifikasi baris `Laptop Dell Latitude 5420 - 44` menampilkan Status `Returned` dengan badge kedua `Damaged`
15. Verifikasi baris `Laptop Dell Latitude 5420 - 6` menampilkan Status `Canceled`
16. Verifikasi baris `Excavator PC200 - 2` menampilkan Status `Rejected`

### Holder, Group, Transaction ID, dan Type pada baris pinjaman
17. Tampilkan Tabel History dengan kondisi K1
18. Verifikasi baris `Laptop Dell Latitude 5420 - 12` menampilkan Holder `Me`
19. Verifikasi baris yang sama menampilkan Group `Head Office`
20. Verifikasi baris yang sama menampilkan Transaction ID `BRW-2026-0151`
21. Verifikasi baris yang sama menampilkan Type `Borrow`
22. Verifikasi badge Type `Borrow` bertoken `secondary`

### Format Handed Over At dan Closed At serta nilai kosongnya
23. Tampilkan Tabel History dengan kondisi K1
24. Verifikasi baris `Laptop Dell Latitude 5420 - 12` menampilkan Handed Over At `01/11/26, 09:00`
25. Verifikasi baris `Laptop Dell Latitude 5420 - 6` menampilkan Handed Over At `—`
26. Verifikasi baris yang sama menampilkan Closed At `04/11/26, 14:10`

### Caption late pada Closed At menurut satuan pinjaman
27. Tampilkan Tabel History dengan kondisi K1
28. Verifikasi baris `Laptop Dell Latitude 5420 - 12` menampilkan Closed At `08/11/26, 11:00`
29. Verifikasi di bawah Closed At baris itu tampil caption `late 2 days`
30. Verifikasi baris `Projector Epson EB-X06 - 5` menampilkan caption `late 1 day` di bawah Closed At `08/11/26, 10:00`
31. Verifikasi baris `Laptop Dell Latitude 5420 - 44` menampilkan caption `late 3 days` di bawah Closed At `05/11/26, 16:00`
32. Verifikasi baris `Meeting Mic Set - 2` menampilkan caption `late 1 hour` di bawah Closed At `08/11/26, 12:30`
33. Verifikasi baris `Meeting Mic Set - 4` menampilkan caption `late 5 hours` di bawah Closed At `08/11/26, 14:10`
34. Verifikasi baris `Projector Epson EB-X06 - 6` menampilkan Closed At `08/11/26, 09:15` tanpa caption late karena selisih hari kalender 0
35. Verifikasi baris `Meeting Mic Set - 6` menampilkan Closed At `08/11/26, 09:40` tanpa caption late karena terlambat kurang dari 1 jam
36. Verifikasi baris `Meeting Mic Set - 3` menampilkan Closed At `07/11/26, 13:30` tanpa caption late karena bermarker `Missing`
37. Verifikasi baris `Laptop Dell Latitude 5420 - 6` tanpa caption late karena berstatus `Canceled`
38. Verifikasi baris `Excavator PC200 - 2` tanpa caption late karena berstatus `Rejected`

### Holder pengguna sendiri, Borrower tanpa akun, dan Division
39. Tampilkan Tabel History dengan kondisi K2
40. Verifikasi baris `Projector Epson EB-X06 - 2` menampilkan Holder `Me`
41. Verifikasi baris `Toyota Avanza - 6` menampilkan Holder `Me`
42. Verifikasi baris `Tablet Samsung Galaxy Tab A9 - 3` menampilkan Holder `Budi S`
43. Arahkan kursor ke Holder `Budi S`
44. Verifikasi tooltip `Budi Setiawan · PIC: Budi Santoso` tampil
45. Verifikasi baris `Printer HP M404 - 1` menampilkan Holder `Finance`
46. Arahkan kursor ke Holder `Finance`
47. Verifikasi tooltip `PIC: Budi Santoso` tampil

### Status, Type, Transaction ID, dan tanggal pada baris penugasan
48. Tampilkan Tabel History dengan kondisi K2
49. Verifikasi baris `Projector Epson EB-X06 - 2` menampilkan Status `Unassigned`
50. Verifikasi baris `Toyota Avanza - 6` menampilkan Status `Unassigned` dengan badge kedua `Missing`
51. Verifikasi baris `Toyota Avanza - 5` menampilkan Status `Rejected`
52. Verifikasi baris `Laptop Dell Latitude 5420 - 5` menampilkan Status `Canceled`
53. Verifikasi baris `Projector Epson EB-X06 - 2` menampilkan Type `Assignment`
54. Verifikasi badge Type `Assignment` bertoken `info`
55. Verifikasi baris yang sama menampilkan Transaction ID `ASG-2026-0009`
56. Verifikasi baris yang sama menampilkan Assigned Date `03/07/26, 10:00` pada kolom Handed Over At
57. Verifikasi baris yang sama menampilkan waktu penutupan `30/10/26, 15:20` pada kolom Closed At
58. Verifikasi baris yang sama tidak menampilkan caption late di bawah Closed At
59. Verifikasi baris `Laptop Dell Latitude 5420 - 5` menampilkan Handed Over At `—`

### Aksi baris pinjaman: Borrow Log
60. Tampilkan Tabel History dengan kondisi K1
61. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 - 12`
62. Verifikasi menu memuat aksi `Borrow Log`
63. Verifikasi menu tidak memuat aksi `Assignment Log`
64. Klik `Borrow Log`
65. Verifikasi dialog Borrow Log terbuka untuk aset `Laptop Dell Latitude 5420 - 12`
66. Tutup dialog dengan menekan `Escape`

### Aksi baris penugasan: hanya Assignment Log
67. Tampilkan Tabel History dengan kondisi K2
68. Klik menu `⋯` pada baris `Projector Epson EB-X06 - 2`
69. Verifikasi menu memuat aksi `Assignment Log`
70. Verifikasi menu tidak memuat aksi `Borrow Log`
71. Klik `Assignment Log`
72. Verifikasi dialog Assignment Log terbuka untuk aset `Projector Epson EB-X06 - 2`
73. Tutup dialog dengan menekan `Escape`

### Teks panjang tidak dipotong dan tooltip nama penuh
74. Tampilkan Tabel History dengan kondisi K3
75. Verifikasi Name `Laptop Dell Latitude 5420 Edisi Khusus Kantor Pengadaan dan Manajemen Vendor Regional Jakarta - 7` tampil utuh tanpa dipotong
76. Arahkan kursor ke badge Brand `Dell Technologies Indonesia Authorized Distributor`
77. Verifikasi tooltip nama Brand penuh `Dell Technologies Indonesia Authorized Distributor` tampil
78. Arahkan kursor ke badge Model/Type `Latitude 5420 Rugged Extreme Edition`
79. Verifikasi tooltip nama Model penuh `Latitude 5420 Rugged Extreme Edition` tampil
80. Arahkan kursor ke badge Group `Regional Procurement and Vendor Management Office Jakarta`
81. Verifikasi tooltip memuat hierarki lengkap Group, yaitu `Head Office` dan `Regional Procurement and Vendor Management Office Jakarta`

### Kolom curated: TAG, Category, foto, dan Purpose
82. Tampilkan Tabel History dengan kondisi K4
83. Verifikasi baris `Meeting Mic Set - 5` menampilkan Brand `Shure` dan Model/Type `SM58`
84. Verifikasi sel TAG baris itu menampilkan dua ikon, satu untuk setiap TAG Type `QR Code` dan `RFID`
85. Verifikasi baris itu menampilkan Category `Audio Visual`
86. Arahkan kursor ke badge Category `Audio Visual`
87. Verifikasi tooltip memuat hierarki lengkap Category, yaitu `Peralatan Kantor` dan `Audio Visual`
88. Verifikasi baris itu menampilkan thumbnail pada kolom Handover Photo
89. Klik thumbnail Handover Photo
90. Verifikasi pratinjau foto `handover-MIC-2026-0005.jpg` terbuka
91. Tutup pratinjau dengan menekan `Escape`
92. Verifikasi baris itu menampilkan thumbnail pada kolom Return Photo
93. Klik thumbnail Return Photo
94. Verifikasi pratinjau foto `return-MIC-2026-0005.jpg` terbuka
95. Tutup pratinjau dengan menekan `Escape`
96. Verifikasi baris itu menampilkan Purpose `Rapat koordinasi vendor pengadaan peralatan audio visual untuk seluruh kantor cabang wilayah Jawa Timur`

### Nilai kosong pada Photo, Brand, Model/Type, TAG, Handover Photo, dan Return Photo
97. Tampilkan Tabel History dengan kondisi K4
98. Verifikasi baris `Laptop Dell Latitude 5420 - 15` menampilkan placeholder gambar standar pada kolom Photo
99. Verifikasi baris yang sama menampilkan Brand `—`
100. Verifikasi baris yang sama menampilkan Model/Type `—`
101. Verifikasi baris yang sama menampilkan TAG `—` karena aset `Non TAG`
102. Verifikasi baris yang sama menampilkan Handover Photo `—`
103. Verifikasi baris yang sama menampilkan Return Photo `—`

### Status Unassigned dengan marker Damaged pada baris penugasan
104. Tampilkan Tabel History dengan kondisi K2
105. Verifikasi baris `Toyota Avanza - 7` menampilkan Status `Unassigned` dengan badge kedua `Damaged`

### Return Photo baris penugasan berisi foto Unassign
106. Tampilkan Tabel History dengan kondisi K4
107. Verifikasi baris `Toyota Avanza - 8` menampilkan thumbnail pada kolom Return Photo
108. Klik thumbnail Return Photo baris itu
109. Verifikasi pratinjau foto `unassign-VEH-2026-0008.jpg` terbuka
110. Tutup pratinjau dengan menekan `Escape`

### Caption late memakai selisih hari kalender menurut Time Zone General Settings
111. Tampilkan Tabel History dengan kondisi K5
112. Verifikasi baris `Laptop Dell Latitude 5420 - 31` menampilkan Closed At `08/11/26, 00:10`
113. Verifikasi di bawah Closed At baris itu tampil caption `late 2 days`
