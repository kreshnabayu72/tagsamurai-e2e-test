---
id: TC-FA-MYASSET-UI-104-tabel-borrowed-tampilan-sel
title: "Tabel Borrowed: format sel, nilai kosong, hover, badge Status, dan tooltip progres approval"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r7", "§1.2#r37", "§1.2#r38", "§1.2#r85", "§1.2#r89", "§4.1#p5", "§4.1b#r1", "§4.1b#r2", "§4.1b#r3", "§4.1b#r4", "§4.1b#r5", "§4.1b#r6", "§4.1b#r7", "§4.1b#r8", "§4.1b#r9", "§4.1b#r12", "§4.1b#r13", "§4.1b#r14", "§4.1b#r15", "§4.1b#r16", "§4.1b#r17", "§4.1b#r18", "§4.4#r13", "§4.4#r50", "§5#r9", "§9.4.2#r29", "EB-TBL-12"]
smoke: []
dependsOn: []
trace:
  "§1.2#r7": 3
  "§1.2#r37": 60
  "§1.2#r38": [12, 63]
  "§1.2#r85": [54, 57]
  "§1.2#r89": [55, 58]
  "§4.1#p5": [15, 24]
  "§4.1b#r1": [5, 19]
  "§4.1b#r2": [6, 81]
  "§4.1b#r3": 7
  "§4.1b#r4": [8, 20, 82, 84]
  "§4.1b#r5": [9, 21, 85, 87]
  "§4.1b#r6": [10, 75, 77, 78, 80]
  "§4.1b#r7": [11, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 98]
  "§4.1b#r8": [33, 34]
  "§4.1b#r9": [35, 88, 90]
  "§4.1b#r12": [12, 60, 62, 63, 92, 93]
  "§4.1b#r13": 13
  "§4.1b#r14": [14, 23]
  "§4.1b#r15": [16, 25, 64, 96]
  "§4.1b#r16": [17, 22]
  "§4.1b#r17": [36, 37, 38]
  "§4.1b#r18": [39, 104]
  "§4.4#r13": [68, 70]
  "§4.4#r50": 68
  "§5#r9": 3
  "§9.4.2#r29": 57
  "EB-TBL-12": [6, 39, 92, 93, 94]
anchor: [67]
coverage:
  web: automated
---

# Tabel Borrowed: format sel, nilai kosong, hover, badge Status, dan tooltip progres approval

## Prerequisites
- Aktor: Borrower (Budi Santoso, pengguna yang membuka halaman My Asset miliknya; untuk K2 juga PIC Borrower atas nama Borrower tanpa akun `Agus Pratama`).
- Layar awal: Halaman My Asset > tab Borrowed
- Komponen: Tabel Borrowed (T-MYA-02)
- Data:
  - DU-104-1: respons tiruan, satu baris tabel Borrowed: Photo `laptop-dell-9.jpg`, Name `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Overdue`, TAG `RFID`, Category `Laptop`, Due Date `06/11/26`, Remaining `3 days overdue`, Borrower `Me`, Transaction ID `BRW-2026-0148`, Source `Admin`, Duration `4 days`, Handed Over At `03/11/26, 09:00`, Extensions `1 / 2`, Purpose `Presentasi klien kuartal keempat`.
  - DU-104-2: respons tiruan, satu baris tabel Borrowed: Photo `null`, Name `Meeting Mic Set - 2`, Asset ID `MIC-2026-0002`, Brand `null`, Model/Type `null`, Group `Head Office`, Status `Borrowed`, TAG `Non TAG`, Category `Audio`, Due Date `09/11/26, 21:50`, Remaining `Due in 1 hour`, Borrower `Me`, Transaction ID `BRW-2026-0156`, Source `Self-service`, Duration `3 hours`, Handed Over At `09/11/26, 18:50`, Extensions `0 / 0`, Purpose `Rapat koordinasi tim`.
  - DU-104-3: respons tiruan, satu baris tabel Borrowed: Photo `projector-epson-eb-x06.jpg`, Name `Projector Epson EB-X06 - 12`, Asset ID `PRJ-2026-0012`, Brand `Epson`, Model/Type `EB-X06`, Group `Head Office`, Status `Waiting for Handover`, TAG `QR`, Category `Projector`, Due Date `null`, Remaining `—`, Borrower `Me`, Transaction ID `BRW-2026-0152`, Source `Admin`, Duration `3 days`, Handed Over At `null`, Extensions `0 / 2`, Purpose `Presentasi vendor`.
  - DU-104-4: respons tiruan, satu baris tabel Borrowed: Photo `laptop-dell-8.jpg`, Name `Laptop Dell Latitude 5420 - 8`, Asset ID `LPT-2026-0008`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Waiting for Approval`, TAG `Non TAG`, Category `Laptop`, Due Date `null`, Remaining `—`, Borrower `Me`, Transaction ID `BRW-2026-0153`, Source `Admin`, Duration `3 days`, Handed Over At `null`, Extensions `0 / 2`, Purpose `Kunjungan cabang`, Approved `1`, Required `2`, Approver yang sudah menyetujui `Rina Wijaya`.
  - DU-104-5: respons tiruan, satu baris tabel Borrowed: Photo `laptop-dell-10.jpg`, Name `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Extension Approval`, TAG `Non TAG`, Category `Laptop`, Due Date `11/11/26`, Remaining `Due in 2 days`, Borrower `Me`, Transaction ID `BRW-2026-0149`, Source `Admin`, Duration `5 days`, Handed Over At `07/11/26, 09:00`, Extensions `0 / 2`, Purpose `Proyek audit`, Approved `0`, Required `1`, Approver yang berhak `Dewi Anggraini`.
  - DU-104-6: respons tiruan, satu baris tabel Borrowed: Photo `laptop-dell-51.jpg`, Name `Laptop Dell Latitude 5420 - 51`, Asset ID `LPT-2026-0051`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Extension Request`, TAG `Non TAG`, Category `Laptop`, Due Date `11/11/26`, Remaining `Due in 2 days`, Borrower `Me`, Transaction ID `BRW-2026-0164`, Source `Admin`, Duration `5 days`, Handed Over At `07/11/26, 09:00`, Extensions `0 / 2`, Purpose `Pelatihan karyawan baru`.
  - DU-104-7: respons tiruan, satu baris tabel Borrowed: Photo `laptop-dell-54.jpg`, Name `Laptop Dell Latitude 5420 - 54`, Asset ID `LPT-2026-0054`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Borrowed + Reported Damaged`, TAG `Non TAG`, Category `Laptop`, Due Date `12/11/26`, Remaining `Due in 3 days`, Borrower `Me`, Transaction ID `BRW-2026-0164`, Source `Admin`, Duration `6 days`, Handed Over At `07/11/26, 09:00`, Extensions `0 / 2`, Purpose `Pelatihan karyawan baru`.
  - DU-104-8: respons tiruan, satu baris tabel Borrowed: Photo `laptop-dell-11.jpg`, Name `Laptop Dell Latitude 5420 - 11`, Asset ID `LPT-2026-0011`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Borrowed + Reported Missing`, TAG `Non TAG`, Category `Laptop`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-0150`, Source `Admin`, Duration `4 days`, Handed Over At `07/11/26, 09:00`, Extensions `0 / 2`, Purpose `Audit lapangan`.
  - DU-104-9: respons tiruan, satu baris tabel Borrowed: Photo `camera-sony-a7-3.jpg`, Name `Camera Sony A7 - 3`, Asset ID `CAM-2026-0003`, Brand `Sony`, Model/Type `A7 III`, Group `Head Office`, Status `Borrowed + Damaged`, TAG `NFC`, Category `Camera`, Due Date `13/11/26`, Remaining `Due in 4 days`, Borrower `Me`, Transaction ID `BRW-2026-0158`, Source `Admin`, Duration `7 days`, Handed Over At `06/11/26, 10:00`, Extensions `0 / 2`, Purpose `Dokumentasi acara kantor`.
  - DU-104-10: respons tiruan, satu baris tabel Borrowed: Photo `tablet-samsung-galaxy-tab-4.jpg`, Name `Tablet Samsung Galaxy Tab - 4`, Asset ID `TAB-2026-0004`, Brand `Samsung`, Model/Type `Galaxy Tab S9`, Group `Head Office`, Status `Borrowed`, TAG `Non TAG`, Category `Tablet`, Due Date `11/11/26`, Remaining `Due in 2 days`, Borrower `Agus Pratama`, Transaction ID `BRW-2026-0160`, Source `Admin`, Duration `1 day`, Handed Over At `08/11/26, 09:00`, Extensions `0 / 2`, Purpose `Survei pelanggan`, PIC `Budi Santoso`.
  - DU-104-11: respons tiruan, satu baris tabel Borrowed: Photo `scanner-zebra-tc21-1.jpg`, Name `Scanner Zebra TC21 - 1`, Asset ID `SCN-2026-0001`, Brand `Zebra Technologies`, Model/Type `Handheld Reader Pro`, Group `Jakarta Barat Warehouse 1`, Status `Borrowed`, TAG `RFID`, Category `Environmental Monitoring`, Due Date `12/11/26`, Remaining `Due in 3 days`, Borrower `Me`, Transaction ID `BRW-2026-0170`, Source `Admin`, Duration `5 days`, Handed Over At `07/11/26, 09:00`, Extensions `0 / 2`, Purpose `Inventarisasi gudang`, Group (hierarki) `Region Jawa > Jakarta Barat Warehouse 1`, Category (hierarki) `Sensors > Environmental Monitoring`.
  - DU-104-12: respons tiruan, satu baris tabel Borrowed: Photo `regional-procurement-1.jpg`, Name `Regional Procurement and Vendor Management Office Jakarta - 1`, Asset ID `RPV-2026-0001`, Brand `Zebra Technologies`, Model/Type `Handheld Reader Pro`, Group `Jakarta Barat Warehouse 12`, Status `Borrowed`, TAG `RFID`, Category `Environmental Monitoring`, Due Date `12/11/26`, Remaining `Due in 3 days`, Borrower `Me`, Transaction ID `BRW-2026-0171`, Source `Admin`, Duration `5 days`, Handed Over At `07/11/26, 09:00`, Extensions `0 / 2`, Purpose `Pengadaan perangkat kantor regional`, Group (hierarki) `Region Jawa > Jakarta Cluster > Jakarta Barat Warehouse 12`.
  - DU-104-13: respons tiruan, satu baris tabel Borrowed: Photo `headset-jabra-evolve-5.jpg`, Name `Headset Jabra Evolve - 5`, Asset ID `HDS-2026-0005`, Brand `Jabra`, Model/Type `Evolve 40`, Group `Head Office`, Status `Borrowed`, TAG `Non TAG`, Category `Audio`, Due Date `09/11/26, 19:50`, Remaining `Due in 1 hour`, Borrower `Me`, Transaction ID `BRW-2026-0172`, Source `Self-service`, Duration `1 hour`, Handed Over At `09/11/26, 18:50`, Extensions `0 / 0`, Purpose `Panggilan konferensi singkat`.
  - DU-104-14: respons tiruan, satu baris tabel Borrowed: Photo `camera-sony-a7-5.jpg`, Name `Camera Sony A7 - 5`, Asset ID `CAM-2026-0005`, Brand `Sony`, Model/Type `A7 III`, Group `Head Office`, Status `Borrowed + Damaged + Reported Missing`, TAG `NFC`, Category `Camera`, Due Date `13/11/26`, Remaining `Due in 4 days`, Borrower `Me`, Transaction ID `BRW-2026-0173`, Source `Admin`, Duration `7 days`, Handed Over At `06/11/26, 10:00`, Extensions `0 / 2`, Purpose `Liputan acara cabang`.
  - DU-104-15: respons tiruan, satu baris tabel Borrowed: Photo `scanner-zebra-tc21-6.jpg`, Name `Scanner Zebra TC21 - 6`, Asset ID `SCN-2026-0006`, Brand `Zebra Technologies`, Model/Type `Handheld Reader Pro`, Group `Head Office`, Status `Borrowed`, TAG `RFID`, Category `Environmental Monitoring`, Due Date `12/11/26`, Remaining `Due in 3 days`, Borrower `Me`, Transaction ID `BRW-2026-0174`, Source `Admin`, Duration `5 days`, Handed Over At `07/11/26, 09:00`, Extensions `0 / 2`, Purpose `Pemindaian inventaris seluruh gudang regional Jawa Barat selama triwulan keempat beserta rekonsiliasi hasilnya`.
  - Nama pada Borrower yang diharapkan untuk DU-104-10 adalah `Agus P`, dari Full Name `Agus Pratama`; tooltip yang diharapkan `Agus Pratama · PIC: Budi Santoso`, dari Full Name `Agus Pratama` dan PIC `Budi Santoso`.
  - Badge Group yang diharapkan untuk DU-104-12 adalah `Jakarta Bara..Warehouse 12`, dari Group `Jakarta Barat Warehouse 12`.
- Kondisi:
  - K1: tabel Borrowed berisi DU-104-1 sampai DU-104-9 dan DU-104-14, dengan kolom bawaan tampil.
  - K2: tabel Borrowed berisi DU-104-1, DU-104-10, dan DU-104-13, dengan kolom bawaan tampil.
  - K3: tabel Borrowed berisi DU-104-11 dan DU-104-12, dengan kolom bawaan tampil.
  - K4: tabel Borrowed berisi DU-104-1 dan DU-104-10, dengan kolom bawaan tampil dan bahasa antarmuka aktif adalah bahasa selain bahasa bawaan.
  - K5: tabel Borrowed berisi DU-104-15, dengan kolom bawaan tampil.
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.

## Test Steps

### Blok identitas aset tidak memiliki kolom Always visible
1. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
2. Klik `⋯` pada header kolom Actions (Column Visibility)
3. Verifikasi kolom `Photo`, `Name`, `Asset ID`, `Brand`, dan `Model/Type` tercentang dan aktif (enabled), sehingga semuanya Hideable

### Format sel baris Overdue milik sendiri dari Admin
4. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
5. Verifikasi sel Photo baris `Laptop Dell Latitude 5420 - 9` menampilkan foto `laptop-dell-9.jpg`
6. Verifikasi sel Name baris `Laptop Dell Latitude 5420 - 9` tampil persis `Laptop Dell Latitude 5420 - 9`
7. Verifikasi sel Asset ID baris `Laptop Dell Latitude 5420 - 9` berisi `LPT-2026-0009`
8. Verifikasi sel Brand baris `Laptop Dell Latitude 5420 - 9` menampilkan badge `Dell`
9. Verifikasi sel Model/Type baris `Laptop Dell Latitude 5420 - 9` menampilkan badge `Latitude 5420`
10. Verifikasi sel Group baris `Laptop Dell Latitude 5420 - 9` menampilkan badge `Head Office`
11. Verifikasi sel Status baris `Laptop Dell Latitude 5420 - 9` menampilkan badge `Overdue`
12. Verifikasi sel Borrower baris `Laptop Dell Latitude 5420 - 9` berisi `Me`
13. Verifikasi sel Transaction ID baris `Laptop Dell Latitude 5420 - 9` berisi `BRW-2026-0148`
14. Verifikasi sel Source baris `Laptop Dell Latitude 5420 - 9` menampilkan badge `Admin`
15. Verifikasi badge Source `Admin` pada baris `Laptop Dell Latitude 5420 - 9` bersaverity `secondary`
16. Verifikasi sel Duration baris `Laptop Dell Latitude 5420 - 9` berisi `4 days`
17. Verifikasi sel Handed Over At baris `Laptop Dell Latitude 5420 - 9` berisi `03/11/26, 09:00`

### Nilai kosong pada baris tanpa foto, tanpa Brand dan Model, dan belum diserahkan
18. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
19. Verifikasi sel Photo baris `Meeting Mic Set - 2` menampilkan placeholder gambar standar
20. Verifikasi sel Brand baris `Meeting Mic Set - 2` menampilkan `—`
21. Verifikasi sel Model/Type baris `Meeting Mic Set - 2` menampilkan `—`
22. Verifikasi sel Handed Over At baris `Projector Epson EB-X06 - 12` menampilkan `—`
23. Verifikasi sel Source baris `Meeting Mic Set - 2` menampilkan badge `Self-service`
24. Verifikasi badge Source `Self-service` pada baris `Meeting Mic Set - 2` bersaverity `info`
25. Verifikasi sel Duration baris `Meeting Mic Set - 2` berisi `3 hours`

### Kolom TAG, Category, Extensions, dan Purpose sesudah dicentang
26. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
27. Klik `⋯` pada header kolom Actions (Column Visibility)
28. Centang kolom `TAG`
29. Centang kolom `Category`
30. Centang kolom `Extensions`
31. Centang kolom `Purpose`
32. Tutup popover Column Visibility
33. Verifikasi sel TAG baris `Laptop Dell Latitude 5420 - 9` menampilkan satu ikon berlabel `RFID`
34. Verifikasi sel TAG baris `Meeting Mic Set - 2` menampilkan `—`
35. Verifikasi sel Category baris `Laptop Dell Latitude 5420 - 9` menampilkan badge `Laptop`
36. Verifikasi sel Extensions baris `Laptop Dell Latitude 5420 - 9` berisi `1 / 2`
37. Verifikasi sel Extensions baris `Meeting Mic Set - 2` berisi `0 / 0`
38. Verifikasi sel Extensions baris `Projector Epson EB-X06 - 12` berisi `0 / 2`
39. Verifikasi sel Purpose baris `Laptop Dell Latitude 5420 - 9` berisi `Presentasi klien kuartal keempat` persis seperti data

### Badge Status menurut nilai status baris
40. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
41. Verifikasi sel Status baris `Laptop Dell Latitude 5420 - 8` menampilkan badge `Waiting for Approval`
42. Verifikasi sel Status baris `Projector Epson EB-X06 - 12` menampilkan badge `Waiting for Handover`
43. Verifikasi sel Status baris `Meeting Mic Set - 2` menampilkan badge `Borrowed`
44. Verifikasi sel Status baris `Laptop Dell Latitude 5420 - 51` menampilkan badge `Extension Request`
45. Verifikasi sel Status baris `Laptop Dell Latitude 5420 - 10` menampilkan badge `Extension Approval`
46. Verifikasi sel Status baris `Laptop Dell Latitude 5420 - 54` menampilkan badge `Borrowed` dan badge `Reported Damaged`
47. Verifikasi badge `Reported Damaged` pada baris `Laptop Dell Latitude 5420 - 54` bersaverity `danger`
48. Verifikasi sel Status baris `Laptop Dell Latitude 5420 - 11` menampilkan badge `Borrowed` dan badge `Reported Missing`
49. Verifikasi badge `Reported Missing` pada baris `Laptop Dell Latitude 5420 - 11` bersaverity `danger`
50. Verifikasi sel Status baris `Camera Sony A7 - 3` menampilkan badge `Borrowed` dan badge `Damaged`
51. Verifikasi badge `Damaged` pada baris `Camera Sony A7 - 3` bersaverity `danger`

### Tooltip progres approval tanpa nama approver
52. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
53. Arahkan kursor ke badge `Waiting for Approval` pada baris `Laptop Dell Latitude 5420 - 8`
54. Verifikasi tooltip badge itu berisi `Approval: 1 of 2 approved`
55. Verifikasi tooltip badge itu tidak memuat nama approver `Rina Wijaya`
56. Arahkan kursor ke badge `Extension Approval` pada baris `Laptop Dell Latitude 5420 - 10`
57. Verifikasi tooltip badge itu berisi `Approval: 0 of 1 approved`
58. Verifikasi tooltip badge itu tidak memuat nama approver `Dewi Anggraini`

### Kolom Borrower untuk Borrower tanpa akun dan baris milik sendiri
59. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K2
60. Verifikasi sel Borrower baris `Tablet Samsung Galaxy Tab - 4` berisi `Agus P`, yaitu nama depan dan inisial nama belakang
61. Arahkan kursor ke sel Borrower baris `Tablet Samsung Galaxy Tab - 4`
62. Verifikasi tooltip sel itu berisi `Agus Pratama · PIC: Budi Santoso`
63. Verifikasi sel Borrower baris `Laptop Dell Latitude 5420 - 9` berisi `Me`
64. Verifikasi sel Duration baris `Tablet Samsung Galaxy Tab - 4` berisi `1 day`

### Name bukan tautan dan riwayat dibuka lewat Borrow Log
65. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
66. Klik sel Name baris `Laptop Dell Latitude 5420 - 9`
67. Verifikasi baris `Laptop Dell Latitude 5420 - 9` masih tampil di Tabel Borrowed
68. Verifikasi tidak ada dialog atau halaman lain yang terbuka
69. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 9`
70. Verifikasi aksi `Borrow Log` tersedia di menu baris

### Badge Group, Brand, Model/Type, dan Category dengan hover dan nama panjang
71. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K3
72. Klik `⋯` pada header kolom Actions (Column Visibility)
73. Centang kolom `Category`
74. Tutup popover Column Visibility
75. Verifikasi sel Group baris `Scanner Zebra TC21 - 1` menampilkan badge `Jakarta Barat Warehouse 1` utuh (25 karakter)
76. Arahkan kursor ke badge Group baris `Scanner Zebra TC21 - 1`
77. Verifikasi tooltip badge itu berisi `Region Jawa > Jakarta Barat Warehouse 1`
78. Verifikasi sel Group baris `Regional Procurement and Vendor Management Office Jakarta - 1` menampilkan badge `Jakarta Bara..Warehouse 12`, dari Group `Jakarta Barat Warehouse 12` (26 karakter)
79. Arahkan kursor ke badge Group baris `Regional Procurement and Vendor Management Office Jakarta - 1`
80. Verifikasi tooltip badge itu berisi `Region Jawa > Jakarta Cluster > Jakarta Barat Warehouse 12`
81. Verifikasi sel Name baris `Regional Procurement and Vendor Management Office Jakarta - 1` menampilkan `Regional Procurement and Vendor Management Office Jakarta - 1` utuh tanpa dipotong
82. Verifikasi sel Brand baris `Scanner Zebra TC21 - 1` menampilkan badge `Zebra Technologies`
83. Arahkan kursor ke badge Brand baris `Scanner Zebra TC21 - 1`
84. Verifikasi tooltip badge itu berisi `Zebra Technologies`
85. Verifikasi sel Model/Type baris `Scanner Zebra TC21 - 1` menampilkan badge `Handheld Reader Pro`
86. Arahkan kursor ke badge Model/Type baris `Scanner Zebra TC21 - 1`
87. Verifikasi tooltip badge itu berisi `Handheld Reader Pro`
88. Verifikasi sel Category baris `Scanner Zebra TC21 - 1` menampilkan badge `Environmental Monitoring`
89. Arahkan kursor ke badge Category baris `Scanner Zebra TC21 - 1`
90. Verifikasi tooltip badge itu berisi `Sensors > Environmental Monitoring`

### Bahasa antarmuka lain: label sistem mengikuti bahasa, nama data tetap persis
91. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K4
92. Verifikasi sel Borrower baris `Laptop Dell Latitude 5420 - 9` menampilkan label sistem `Me` dalam bahasa antarmuka aktif
93. Verifikasi sel Borrower baris `Tablet Samsung Galaxy Tab - 4` tetap berisi `Agus P` persis seperti data, tanpa diterjemahkan
94. Verifikasi sel Name baris `Laptop Dell Latitude 5420 - 9` tetap tampil persis `Laptop Dell Latitude 5420 - 9`

### Duration satuan jam bentuk tunggal
95. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K2
96. Verifikasi sel Duration baris `Headset Jabra Evolve - 5` berisi `1 hour`

### Dua badge tambahan pada kolom Status tampil berurutan
97. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
98. Verifikasi sel Status baris `Camera Sony A7 - 5` menampilkan badge `Borrowed`, `Damaged`, dan `Reported Missing` berurutan dalam urutan itu

### Tooltip teks penuh pada sel Purpose
99. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K5
100. Klik `⋯` pada header kolom Actions (Column Visibility)
101. Centang kolom `Purpose`
102. Tutup popover Column Visibility
103. Arahkan kursor ke sel Purpose baris `Scanner Zebra TC21 - 6`
104. Verifikasi tooltip sel itu berisi teks penuh `Pemindaian inventaris seluruh gudang regional Jawa Barat selama triwulan keempat beserta rekonsiliasi hasilnya`
