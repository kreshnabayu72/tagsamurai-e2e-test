---
id: TC-FA-BORROW-UI-056-tabel-borrowed-assets-konfigurasi
title: "Tabel Borrowed Assets By Asset dan By Borrower: konfigurasi kolom, Remaining, Due Date, dan bulk Return"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1j#p3", "§4.1j#p4", "§4.1j#r1", "§4.1j#r2", "§4.1j#r3", "§4.1j#r4", "§4.1j#r5", "§4.1j#r6", "§4.1j#r7", "§4.1j#r8", "§4.1j#r9", "§4.1j#r10", "§4.1j#r11", "§4.1j#r12", "§4.1j#r13", "§4.1j#r14", "§4.1j#r15", "§4.1j#r16", "§4.1j#r17", "§4.1j#r18", "§4.1j#p7", "§4.1j#r34", "§4.1j#r35", "§4.1j#r36", "§4.3#r6", "EB-TBL-1@tabel-borrowed-assets", "EB-TBL-2@tabel-borrowed-assets", "EB-TBL-3@tabel-borrowed-assets", "EB-TBL-4@tabel-borrowed-assets", "EB-KOL-3"]
smoke: []
dependsOn: []
trace:
  "§4.1j#p3": [25, 27, 197, 198, 208, 209]
  "§4.1j#p4": 30
  "§4.1j#r1": [29, 32, 33, 34, 95]
  "§4.1j#r2": [29, 35, 36, 95, 124]
  "§4.1j#r3": [29, 37, 38, 95, 137]
  "§4.1j#r4": [29, 40, 41, 43, 44, 95, 125]
  "§4.1j#r5": [29, 45, 46, 48, 49, 95, 126]
  "§4.1j#r6": [29, 50, 52, 53, 95, 127]
  "§4.1j#r7": [29, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 95, 128]
  "§4.1j#r8": [96, 97, 99, 100, 129, 204]
  "§4.1j#r9": [96, 101, 102, 104, 105, 130, 205]
  "§4.1j#r10": [29, 66, 67, 68, 69, 71, 72, 95, 131]
  "§4.1j#r11": [29, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 95, 137]
  "§4.1j#r12": [29, 87, 88, 95, 137]
  "§4.1j#r13": [29, 89, 91, 92, 95, 132]
  "§4.1j#r14": [96, 106, 108, 133, 177, 178]
  "§4.1j#r15": [96, 109, 110, 134]
  "§4.1j#r16": [96, 111, 112, 114, 115, 135, 185]
  "§4.1j#r17": [96, 117, 118, 137, 179, 180]
  "§4.1j#r18": [96, 119, 120, 121, 136, 189, 191]
  "§4.1j#p7": [140, 141, 142, 144]
  "§4.1j#r34": [139, 147, 149, 150, 163]
  "§4.1j#r35": [151, 152, 153, 154, 155, 157, 158, 164, 194]
  "§4.1j#r36": [139, 159, 160, 165]
  "§4.3#r6": [68, 69]
  "EB-TBL-1@tabel-borrowed-assets": [2, 3, 7, 8, 10, 11, 12, 14, 15, 19, 20, 22, 23]
  "EB-TBL-2@tabel-borrowed-assets": [33, 44, 49, 100, 110]
  "EB-TBL-3@tabel-borrowed-assets": [151, 153, 154, 155]
  "EB-TBL-4@tabel-borrowed-assets": [89, 91, 147, 149, 189, 191]
  "EB-KOL-3": [170, 172]
anchor: [169]
coverage:
  web: automated
---
# Tabel Borrowed Assets By Asset dan By Borrower: konfigurasi kolom, Remaining, Due Date, dan bulk Return

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman `Transactions > Borrow`, tab Borrowed Assets.
- Komponen: Tabel Borrowed Assets
- Data:
  - DU-056-1: Baris Overdue dengan kolom curated terisi: Name `Laptop Dell Latitude 5420 - 3`, Asset ID `LPT-2026-0003`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Hierarki Group `Head Office`, Status `Overdue`, Due Date `06/11/26`, Remaining `3 days overdue`, Transaction ID `BRW-2026-0149`, Borrower `Andi Pratama`, Borrower tampil `Andi P`, Employee ID `10250`, Due date asal `04/11/26`, TAG `RFID`, Category `Laptop`, Hierarki Category `IT Equipment > Laptop`, Handed Over At `01/11/26, 10:00`, Handed Over By `Agus Prasetyo` (tampil `Agus P`), Extensions `1 / 1`, Source `Admin`, Nama pembuat `Rina Wijaya`, Purpose `Presentasi proposal pengadaan jaringan kepada klien di Surabaya`.
  - DU-056-2: Baris Borrowed sisa satu hari, Brand dan Model kosong: Name `Laptop Dell Latitude 5420 - 2`, Asset ID `LPT-2026-0002`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Hierarki Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Transaction ID `BRW-2026-0147`, Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Employee ID `10231`, TAG `Non TAG`, Category `Laptop`, Hierarki Category `IT Equipment > Laptop`, Handed Over At `07/11/26, 09:10`, Handed Over By `Self-service`, Extensions `0 / 2`, Source `Self-service`, Purpose `Kunjungan lapangan`.
  - DU-056-3: Baris Extension Approval: Name `Toyota Avanza - 2`, Asset ID `VEH-2026-0002`, Brand `kosong`, Model/Type `kosong`, Group `Branch Surabaya`, Hierarki Group `Head Office > Branch Surabaya`, Status `Extension Approval`, Due Date `11/11/26`, Remaining `Due in 2 days`, Transaction ID `BRW-2026-0150`, Borrower `Dewi Lestari`, Borrower tampil `Dewi L`, Employee ID `20318`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-4: Baris Borrowed dalam BRW yang sama dengan Extension Approval: Name `Toyota Avanza - 3`, Asset ID `VEH-2026-0003`, Brand `kosong`, Model/Type `kosong`, Group `Branch Surabaya`, Hierarki Group `Head Office > Branch Surabaya`, Status `Borrowed`, Due Date `11/11/26`, Remaining `Due in 2 days`, Transaction ID `BRW-2026-0150`, Borrower `Dewi Lestari`, Borrower tampil `Dewi L`, Employee ID `20318`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-5: Baris Extension Request: Name `Projector Epson EB-X06 - 3`, Asset ID `PRJ-2026-0003`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Hierarki Group `Head Office`, Status `Extension Request`, Due Date `12/11/26`, Remaining `Due in 3 days`, Transaction ID `BRW-2026-0161`, Borrower `Rudi Hartono`, Borrower tampil `Rudi H`, Employee ID `10262`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-6: Baris Borrowed dengan Reported Damaged: Name `Toyota Avanza - 4`, Asset ID `VEH-2026-0004`, Brand `kosong`, Model/Type `kosong`, Group `Branch Surabaya`, Hierarki Group `Head Office > Branch Surabaya`, Status `Borrowed + Reported Damaged`, Due Date `11/11/26`, Remaining `Due in 2 days`, Transaction ID `BRW-2026-0166`, Borrower `Dewi Lestari`, Borrower tampil `Dewi L`, Employee ID `20318`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-7: Baris Borrowed dengan Reported Missing: Name `Toyota Avanza - 5`, Asset ID `VEH-2026-0005`, Brand `kosong`, Model/Type `kosong`, Group `Branch Surabaya`, Hierarki Group `Head Office > Branch Surabaya`, Status `Borrowed + Reported Missing`, Due Date `11/11/26`, Remaining `Due in 2 days`, Transaction ID `BRW-2026-0166`, Borrower `Dewi Lestari`, Borrower tampil `Dewi L`, Employee ID `20318`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-8: Baris Borrowed dengan record Damaged: Name `Toyota Avanza - 6`, Asset ID `VEH-2026-0006`, Brand `kosong`, Model/Type `kosong`, Group `Branch Surabaya`, Hierarki Group `Head Office > Branch Surabaya`, Status `Borrowed + Damaged`, Due Date `11/11/26`, Remaining `Due in 2 days`, Transaction ID `BRW-2026-0166`, Borrower `Dewi Lestari`, Borrower tampil `Dewi L`, Employee ID `20318`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-9: Baris Overdue dengan pengajuan Extend: Name `Projector Epson EB-X06 - 9`, Asset ID `PRJ-2026-0009`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Hierarki Group `Head Office`, Status `Overdue + Extension Request`, Due Date `05/11/26`, Remaining `4 days overdue`, Transaction ID `BRW-2026-0163`, Borrower `Rudi Hartono`, Borrower tampil `Rudi H`, Employee ID `10262`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-10: Baris Borrowed jatuh tempo hari ini tanpa foto: Name `Camera Sony A7 IV - 1`, Asset ID `CAM-2026-0001`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Hierarki Group `Head Office`, Status `Borrowed`, Due Date `09/11/26`, Remaining `Due today`, Transaction ID `BRW-2026-0168`, Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Employee ID `10231`, Foto `kosong`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-11: Baris satuan jam sisa 3 jam: Name `Handheld Scanner Zebra - 1`, Asset ID `HHS-2026-0001`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Hierarki Group `Head Office`, Status `Borrowed`, Due Date `09/11/26, 23:10`, Remaining `Due in 3 hours`, Transaction ID `BRW-2026-0169`, Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Employee ID `10231`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-12: Baris satuan jam sisa 1 jam: Name `Handheld Scanner Zebra - 2`, Asset ID `HHS-2026-0002`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Hierarki Group `Head Office`, Status `Borrowed`, Due Date `09/11/26, 21:00`, Remaining `Due in 1 hour`, Transaction ID `BRW-2026-0169`, Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Employee ID `10231`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-13: Baris satuan jam terlambat 2 jam: Name `Handheld Scanner Zebra - 3`, Asset ID `HHS-2026-0003`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Hierarki Group `Head Office`, Status `Overdue`, Due Date `09/11/26, 19:10`, Remaining `2 hours overdue`, Transaction ID `BRW-2026-0169`, Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Employee ID `10231`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-14: Baris satuan jam terlambat 1 jam: Name `Handheld Scanner Zebra - 4`, Asset ID `HHS-2026-0004`, Brand `kosong`, Model/Type `kosong`, Group `Head Office`, Hierarki Group `Head Office`, Status `Overdue`, Due Date `09/11/26, 19:45`, Remaining `1 hour overdue`, Transaction ID `BRW-2026-0169`, Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Employee ID `10231`, Handed Over At `05/11/26, 09:00`, Purpose `Kebutuhan operasional harian`.
  - DU-056-15: Borrower dengan aset terbanyak: Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Employee ID `10231`, Group `Head Office`, Total Asset `6`.
  - DU-056-16: Borrower dengan Total Asset sama di Group cabang: Borrower `Dewi Lestari`, Borrower tampil `Dewi L`, Employee ID `20318`, Group `Branch Surabaya`, Total Asset `6`.
  - DU-056-17: Borrower Group cabang: Borrower `Maya Putri`, Borrower tampil `Maya P`, Employee ID `20325`, Group `Branch Surabaya`, Total Asset `4`.
  - DU-056-18: Borrower Group Head Office: Borrower `Rudi Hartono`, Borrower tampil `Rudi H`, Employee ID `10262`, Group `Head Office`, Total Asset `4`.
  - DU-056-19: Borrower dengan aset paling sedikit: Borrower `Andi Pratama`, Borrower tampil `Andi P`, Employee ID `10250`, Group `Head Office`, Total Asset `1`.
  - DU-056-20: Borrower dengan tiga Group, urutan penugasan tidak alfabetis: Borrower `Sari Dewi`, Borrower tampil `Sari D`, Employee ID `10270`, Group `Head Office`, Total Asset `3`, Group 2 `Branch Surabaya`, Group 3 `Branch Bandung`.
  - DU-056-21: Borrower dengan dua Group, urutan penugasan tidak alfabetis: Borrower `Agus Prasetyo`, Borrower tampil `Agus P`, Employee ID `10290`, Group `Head Office`, Total Asset `2`, Group 2 `Branch Surabaya`.
  - DU-056-22: Borrower dengan seluruh Group master data: Borrower `Siti Nurbaya`, Borrower tampil `Siti N`, Employee ID `10280`, Group `All Groups`, Total Asset `8`.
  - DU-056-23: Kata kunci tanpa hasil yang diketik pada tabel: Search tanpa hasil `Tidak Ada`.
- Kondisi:
  - K1: tabel By Asset dimuat berisi DU-056-1 sampai DU-056-14; waktu sekarang `09/11/26, 20:30`; Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`; jatah Extend maksimum aset DU-056-2 bernilai `2`.
  - K2: tabel By Asset dimuat tanpa data sama sekali.
  - K3: memuat tabel By Asset gagal karena error server.
  - K4: seperti K1; pencarian `Tidak Ada` dijawab tanpa baris.
  - K5: tabel By Borrower dimuat berisi DU-056-15 sampai DU-056-22.
  - K6: tabel By Borrower dimuat tanpa data sama sekali.
  - K7: memuat tabel By Borrower gagal karena error server.
  - K8: seperti K5; pencarian `Tidak Ada` dijawab tanpa baris.

## Test Steps

### By Asset kosong alami
1. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K2
2. Verifikasi judul `No assets are out right now` tampil pada tabel By Asset
3. Verifikasi deskripsi `Borrowed assets will appear here after handover.` tampil pada tabel By Asset

### By Asset kosong akibat pencarian tanpa hasil
4. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K4
5. Klik ikon Search pada toolbar By Asset
6. Ketik Search `Tidak Ada`, tekan Enter
7. Verifikasi judul `No results found` tampil pada tabel By Asset
8. Verifikasi deskripsi `Try adjusting your search or filter.` tampil pada tabel By Asset

### By Asset gagal muat bukan empty state
9. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K3
10. Verifikasi pesan `Unable to load this data.` tampil pada tabel By Asset
11. Verifikasi tombol `[Try Again]` tampil pada tabel By Asset
12. Verifikasi judul `No assets are out right now` tidak tampil karena gagal muat bukan empty state

### By Borrower kosong alami
13. Tampilkan Tabel Borrowed Assets By Borrower dengan kondisi K6
14. Verifikasi judul `No assets are out right now` tampil pada tabel By Borrower
15. Verifikasi deskripsi `Borrowed assets will appear here after handover.` tampil pada tabel By Borrower

### By Borrower kosong akibat pencarian tanpa hasil
16. Tampilkan Tabel Borrowed Assets By Borrower dengan kondisi K8
17. Klik ikon Search pada toolbar By Borrower
18. Ketik Search `Tidak Ada`, tekan Enter
19. Verifikasi judul `No results found` tampil pada tabel By Borrower
20. Verifikasi deskripsi `Try adjusting your search or filter.` tampil pada tabel By Borrower

### By Borrower gagal muat bukan empty state
21. Tampilkan Tabel Borrowed Assets By Borrower dengan kondisi K7
22. Verifikasi pesan `Unable to load this data.` tampil pada tabel By Borrower
23. Verifikasi tombol `[Try Again]` tampil pada tabel By Borrower

### By Asset: kolom pertama, Actions, dan urutan kolom
24. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
25. Verifikasi kolom pertama tabel By Asset adalah kolom Checkbox
26. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 3`
27. Verifikasi urutan aksi pada menu baris: `Borrow Log`, `Return`, `Request Extension`, `Report Damaged`, dan `Report Missing`
28. Tekan Esc
29. Verifikasi urutan kolom data dari kiri ke kanan sesudah Checkbox: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Due Date`, `Remaining`, `Transaction ID`, `Borrower`
30. Verifikasi baris `Toyota Avanza - 2` dan baris `Toyota Avanza - 3` sama-sama memuat Transaction ID `BRW-2026-0150`, satu baris untuk tiap aset

### By Asset: Photo, Name, dan Asset ID
31. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
32. Verifikasi baris `Laptop Dell Latitude 5420 - 3` menampilkan foto utama aset
33. Verifikasi baris `Camera Sony A7 IV - 1` menampilkan placeholder gambar standar
34. Verifikasi header kolom `Photo` tidak memiliki ikon sort
35. Verifikasi Name `Laptop Dell Latitude 5420 - 3` tampil pada baris pertama dengan format nama aset dan increment
36. Verifikasi setiap baris tabel By Asset memuat Name
37. Verifikasi Asset ID `LPT-2026-0003` tampil pada baris `Laptop Dell Latitude 5420 - 3`
38. Verifikasi setiap baris tabel By Asset memuat Asset ID

### By Asset: Brand, Model/Type, dan Group
39. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
40. Verifikasi Brand baris `Laptop Dell Latitude 5420 - 3` tampil sebagai badge `Dell`
41. Verifikasi badge Brand `Dell` memakai severity `dark`
42. Arahkan kursor ke badge Brand baris `Laptop Dell Latitude 5420 - 3`
43. Verifikasi nama Brand penuh `Dell` tampil
44. Verifikasi Brand baris `Laptop Dell Latitude 5420 - 2` tampil `—`
45. Verifikasi Model/Type baris `Laptop Dell Latitude 5420 - 3` tampil sebagai badge `Latitude 5420`
46. Verifikasi badge Model/Type `Latitude 5420` memakai severity `dark`
47. Arahkan kursor ke badge Model/Type baris `Laptop Dell Latitude 5420 - 3`
48. Verifikasi nama Model penuh `Latitude 5420` tampil
49. Verifikasi Model/Type baris `Laptop Dell Latitude 5420 - 2` tampil `—`
50. Verifikasi badge Group `Head Office` baris `Laptop Dell Latitude 5420 - 3` memakai severity `primary`
51. Arahkan kursor ke badge Group baris `Toyota Avanza - 2`
52. Verifikasi hierarki `Head Office > Branch Surabaya` tampil
53. Verifikasi setiap baris tabel By Asset memuat badge Group

### By Asset: badge Status
54. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
55. Verifikasi baris `Toyota Avanza - 3` memuat badge status `Borrowed`
56. Verifikasi baris `Toyota Avanza - 2` memuat badge status `Extension Approval` dan tidak memuat badge `Borrowed`
57. Verifikasi baris `Projector Epson EB-X06 - 3` memuat badge status `Extension Request`
58. Verifikasi baris `Laptop Dell Latitude 5420 - 3` memuat badge status `Overdue`
59. Verifikasi baris `Projector Epson EB-X06 - 9` memuat dua badge status `Overdue` dan `Extension Request`
60. Verifikasi baris `Toyota Avanza - 4` memuat badge `Borrowed` dan badge `Reported Damaged`
61. Verifikasi badge `Reported Damaged` memakai severity `danger`
62. Verifikasi baris `Toyota Avanza - 5` memuat badge `Reported Missing` dengan severity `danger`
63. Verifikasi baris `Toyota Avanza - 6` memuat badge `Damaged` dengan severity `danger`
64. Verifikasi setiap baris tabel By Asset memuat badge status

### By Asset: Due Date dan Remaining
65. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
66. Verifikasi Due Date baris `Laptop Dell Latitude 5420 - 3` tampil `06/11/26`
67. Verifikasi Due Date baris `Handheld Scanner Zebra - 1` tampil `09/11/26, 23:10` lengkap dengan jam
68. Verifikasi Due Date baris `Laptop Dell Latitude 5420 - 3` memakai severity `danger` karena Overdue
69. Verifikasi Due Date baris `Laptop Dell Latitude 5420 - 2` memakai severity `warning` karena sisa tidak lebih dari satu hari
70. Arahkan kursor ke Due Date baris `Laptop Dell Latitude 5420 - 3`
71. Verifikasi due date asal `04/11/26` tampil
72. Verifikasi setiap baris tabel By Asset memuat Due Date
73. Verifikasi Remaining baris `Laptop Dell Latitude 5420 - 3` tampil `3 days overdue`
74. Verifikasi Remaining baris `Laptop Dell Latitude 5420 - 2` tampil `Due in 1 day`
75. Verifikasi Remaining baris `Toyota Avanza - 3` tampil `Due in 2 days`
76. Verifikasi Remaining baris `Camera Sony A7 IV - 1` tampil `Due today`
77. Verifikasi Remaining baris `Handheld Scanner Zebra - 1` tampil `Due in 3 hours`
78. Verifikasi Remaining baris `Handheld Scanner Zebra - 2` tampil `Due in 1 hour`
79. Verifikasi Remaining baris `Handheld Scanner Zebra - 3` tampil `2 hours overdue`
80. Verifikasi Remaining baris `Handheld Scanner Zebra - 4` tampil `1 hour overdue`
81. Verifikasi Remaining baris `Laptop Dell Latitude 5420 - 3` memakai severity `danger`
82. Verifikasi Remaining baris `Laptop Dell Latitude 5420 - 2` memakai severity `warning`
83. Verifikasi Remaining baris `Handheld Scanner Zebra - 1` memakai severity `warning`
84. Verifikasi Remaining baris `Toyota Avanza - 3` tidak memakai severity `warning` maupun `danger`
85. Verifikasi setiap baris tabel By Asset memuat Remaining

### By Asset: Transaction ID dan Borrower
86. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
87. Verifikasi Transaction ID `BRW-2026-0149` baris `Laptop Dell Latitude 5420 - 3` tampil sebagai tautan
88. Verifikasi setiap baris tabel By Asset memuat Transaction ID
89. Verifikasi Borrower baris `Laptop Dell Latitude 5420 - 3` tampil `Andi P`
90. Arahkan kursor ke Borrower baris `Laptop Dell Latitude 5420 - 3`
91. Verifikasi nama lengkap `Andi Pratama` dan Employee ID `10250` tampil
92. Verifikasi setiap baris tabel By Asset memuat Borrower

### By Asset: toggle Setup Column
93. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
94. Klik header kolom Actions `⋯`
95. Verifikasi checkbox `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Due Date`, `Remaining`, `Transaction ID`, dan `Borrower` tercentang dan enabled
96. Verifikasi checkbox `TAG`, `Category`, `Handed Over At`, `Extensions`, `Source`, `Purpose`, dan `Handed Over By` tidak tercentang dan enabled
97. Verifikasi kolom `TAG`, `Category`, `Handed Over At`, `Extensions`, `Source`, `Purpose`, dan `Handed Over By` tidak tampil pada tabel By Asset
98. Centang kolom `TAG`, `Category`, `Handed Over At`, `Extensions`, `Source`, `Purpose`, dan `Handed Over By` pada daftar Column Visibility
99. Verifikasi baris `Laptop Dell Latitude 5420 - 3` menampilkan satu ikon TAG dengan label `RFID`
100. Verifikasi TAG baris `Laptop Dell Latitude 5420 - 2` tampil `—` karena `Non TAG`
101. Verifikasi badge Category `Laptop` baris `Laptop Dell Latitude 5420 - 3` tampil
102. Verifikasi badge Category `Laptop` memakai severity `primary`
103. Arahkan kursor ke badge Category baris `Laptop Dell Latitude 5420 - 3`
104. Verifikasi hierarki `IT Equipment > Laptop` tampil
105. Verifikasi setiap baris tabel By Asset memuat Category
106. Verifikasi Handed Over At baris `Laptop Dell Latitude 5420 - 3` tampil `01/11/26, 10:00`
107. Arahkan kursor ke Handed Over At baris `Laptop Dell Latitude 5420 - 3`
108. Verifikasi pemberi handover `Agus Prasetyo` tampil
109. Verifikasi Extensions baris `Laptop Dell Latitude 5420 - 3` tampil `1 / 1`
110. Verifikasi Extensions baris `Laptop Dell Latitude 5420 - 2` tampil `0 / 2`
111. Verifikasi badge Source `Admin` baris `Laptop Dell Latitude 5420 - 3` memakai severity `dark`
112. Verifikasi badge Source `Self-service` baris `Laptop Dell Latitude 5420 - 2` memakai severity `primary`
113. Arahkan kursor ke badge Source `Admin` baris `Laptop Dell Latitude 5420 - 3`
114. Verifikasi nama pembuat `Rina Wijaya` tampil pada tooltip badge Source
115. Verifikasi setiap baris tabel By Asset memuat badge Source
116. Arahkan kursor ke Purpose baris `Laptop Dell Latitude 5420 - 3`
117. Verifikasi teks penuh `Presentasi proposal pengadaan jaringan kepada klien di Surabaya` tampil
118. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 2` tampil `Kunjungan lapangan`
119. Verifikasi Handed Over By baris `Laptop Dell Latitude 5420 - 2` tampil `Self-service`
120. Verifikasi Handed Over By baris `Laptop Dell Latitude 5420 - 3` menampilkan nama pemberi handover
121. Verifikasi kolom `Handed Over By` menjadi kolom data terakhir sebelum Actions

### By Asset: field dan placeholder Filter Panel
122. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
123. Klik ikon Filter pada toolbar By Asset
124. Verifikasi placeholder `All asset names` tampil pada field `Asset Name`
125. Verifikasi placeholder `All brands` tampil pada field `Brand`
126. Verifikasi placeholder `All models` tampil pada field `Model/Type`
127. Verifikasi placeholder `All groups` tampil pada field `Group` di Filter Panel By Asset
128. Verifikasi placeholder `All statuses` tampil pada field `Status` di Filter Panel By Asset
129. Verifikasi placeholder `All tags` tampil pada field `TAG`
130. Verifikasi placeholder `All categories` tampil pada field `Category`
131. Verifikasi placeholder `Select date` tampil pada field `Due Date`
132. Verifikasi placeholder `All borrowers` tampil pada field `Borrower` di Filter Panel By Asset
133. Verifikasi placeholder `Select date` tampil pada field `Handed Over At`
134. Verifikasi input pertama field `Extensions` memakai placeholder `Min` dan input kedua memakai placeholder `Max`
135. Verifikasi placeholder `All sources` tampil pada field `Source` di Filter Panel By Asset
136. Verifikasi placeholder `All users` tampil pada field `Handed Over By`
137. Verifikasi Filter Panel tidak memuat field `Asset ID`, `Remaining`, `Transaction ID`, maupun `Purpose`

### By Borrower: kolom pertama, tanpa checkbox, dan row action
138. Tampilkan Tabel Borrowed Assets By Borrower dengan kondisi K5
139. Verifikasi urutan kolom data dari kiri ke kanan: `Borrower`, `Group`, `Total Asset`
140. Verifikasi tabel By Borrower tidak memiliki kolom Checkbox maupun bar Bulk Action
141. Verifikasi tabel By Borrower datar tanpa kontrol expand pada baris `Budi S`
142. Verifikasi tombol `Search by Scan` tidak tampil pada toolbar By Borrower
143. Klik `⋯` pada baris `Budi S`
144. Verifikasi menu baris memuat aksi `Detail`
145. Tekan Esc

### By Borrower: Borrower, Group, dan Total Asset
146. Tampilkan Tabel Borrowed Assets By Borrower dengan kondisi K5
147. Verifikasi Borrower baris `Budi S` tampil `Budi S` dengan Employee ID `10231` di baris kedua
148. Arahkan kursor ke Borrower baris `Budi S`
149. Verifikasi nama lengkap `Budi Setiawan` tampil pada tooltip Borrower baris `Budi S`
150. Verifikasi setiap baris tabel By Borrower memuat Borrower
151. Verifikasi baris `Dewi L` memuat satu badge Group `Branch Surabaya`
152. Verifikasi badge Group `Branch Surabaya` baris `Dewi L` memakai severity `primary`
153. Verifikasi baris `Agus P` memuat dua badge Group berurutan `Branch Surabaya` lalu `Head Office`
154. Verifikasi baris `Sari D` memuat dua badge Group `Branch Bandung` dan `Branch Surabaya` dan chip `+1 more`
155. Verifikasi baris `Siti N` memuat badge tunggal `All Groups`
156. Arahkan kursor ke badge Group baris `Dewi L`
157. Verifikasi hierarki `Head Office > Branch Surabaya` tampil
158. Verifikasi setiap baris tabel By Borrower memuat Group
159. Verifikasi Total Asset baris `Budi S` tampil `6` sebagai angka bulat
160. Verifikasi setiap baris tabel By Borrower memuat Total Asset

### By Borrower: field dan placeholder Filter Panel
161. Tampilkan Tabel Borrowed Assets By Borrower dengan kondisi K5
162. Klik ikon Filter pada toolbar By Borrower
163. Verifikasi placeholder `All borrowers` tampil pada field `Borrower` di Filter Panel By Borrower
164. Verifikasi placeholder `All groups` tampil pada field `Group` di Filter Panel By Borrower
165. Verifikasi input pertama field `Total Asset` di Filter Panel By Borrower memakai placeholder `Min` dan input kedua memakai placeholder `Max`

### Konfigurasi kolom satu tabel tidak mengubah tabel lain
166. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
167. Klik header kolom Actions `⋯`
168. Hilangkan centang kolom `Group` pada daftar Column Visibility
169. Verifikasi kolom `Name` tampil pada tabel By Asset
170. Verifikasi kolom `Group` tidak tampil pada tabel By Asset sesudah dihilangkan
171. Tampilkan Tabel Borrowed Assets By Borrower dengan kondisi K5
172. Verifikasi kolom `Group` tampil pada tabel By Borrower

### By Asset: Handed Over At dan Purpose tidak pernah kosong
173. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
174. Klik header kolom Actions `⋯`
175. Centang kolom `Handed Over At`
176. Centang kolom `Purpose`
177. Verifikasi Handed Over At baris `Toyota Avanza - 2` tampil `05/11/26, 09:00`
178. Verifikasi setiap baris tabel By Asset memuat Handed Over At
179. Verifikasi Purpose baris `Toyota Avanza - 2` tampil `Kebutuhan operasional harian`
180. Verifikasi setiap baris tabel By Asset memuat Purpose

### By Asset: keterangan badge Source Self-service
181. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
182. Klik header kolom Actions `⋯`
183. Centang kolom `Source`
184. Arahkan kursor ke badge Source `Self-service` baris `Laptop Dell Latitude 5420 - 2`
185. Verifikasi keterangan bahwa BRW dipinjam sendiri oleh Borrower tampil pada tooltip badge Source

### By Asset: Handed Over By tampil singkat dengan nama lengkap saat hover
186. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
187. Klik header kolom Actions `⋯`
188. Centang kolom `Handed Over By`
189. Verifikasi Handed Over By baris `Laptop Dell Latitude 5420 - 3` tampil `Agus P`
190. Arahkan kursor ke Handed Over By baris `Laptop Dell Latitude 5420 - 3`
191. Verifikasi nama lengkap `Agus Prasetyo` tampil

### By Borrower: chip +N more membuka daftar semua Group
192. Tampilkan Tabel Borrowed Assets By Borrower dengan kondisi K5
193. Klik chip `+1 more` pada baris `Sari D`
194. Verifikasi daftar semua Group `Branch Bandung`, `Branch Surabaya`, dan `Head Office` tampil pada popover

### By Asset: menu baris tidak memuat aksi Detail
195. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
196. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 3`
197. Verifikasi menu baris memuat aksi `Borrow Log`
198. Verifikasi menu baris tidak memuat aksi `Detail` karena transaksinya dibuka lewat tautan Transaction ID
199. Tekan Esc

### By Asset: posisi kolom TAG dan Category saat ditampilkan
200. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
201. Klik header kolom Actions `⋯`
202. Centang kolom `TAG` pada daftar Column Visibility
203. Centang kolom `Category` pada daftar Column Visibility
204. Verifikasi kolom `TAG` tampil tepat setelah kolom `Status` pada tabel By Asset
205. Verifikasi kolom `Category` tampil tepat setelah kolom `TAG` pada tabel By Asset

### By Asset: severity aksi baris
206. Tampilkan Tabel Borrowed Assets By Asset dengan kondisi K1
207. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 3`
208. Verifikasi aksi `Borrow Log`, `Return`, dan `Request Extension` memakai severity `dark`
209. Verifikasi aksi `Report Damaged` dan `Report Missing` memakai severity `danger`
210. Tekan Esc
