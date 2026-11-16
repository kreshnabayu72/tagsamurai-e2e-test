---
id: TC-FA-MISS-UI-053-tabel-history-tampilan-awal
title: "Tabel History: tampilan awal, kolom default, Duration, Resolved By System, empty state, dan tanpa Bulk"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1b#r1, §4.1b#r2, §4.1b#r3, §4.1b#r4, §4.1b#r5, §4.1b#r6, §4.1b#r7, §4.1b#r8, §4.1b#r9, §4.1b#r10, §4.1b#r11, §4.1b#r12, §4.1b#r13, §4.1b#r14, §4.1b#r15, §4.1b#r16, §4.1b#r17, §4.1b#r18, §4.1b#r19, §4.1b#r20, §4.1b#r21, §4.1b#r22, §4.1b#r23, §4.1b#r24, §4.1b#r25, §4.1b#r26, §4.1b#r27, §4.1b#p1, §4.1b#p3, §7.1#r2, §5#r5, §4.1#r2, §4.3#r7, EB-TBL-1@tabel-history, EB-TBL-2@tabel-history, EB-TBL-4@tabel-history]
smoke: []
dependsOn: []
trace:
  §4.1b#r1: [9, 12, 13, 111, 136]
  §4.1b#r2: [9, 14, 111, 119]
  §4.1b#r3: [9, 15, 111]
  §4.1b#r4: [10, 53, 64, 88]
  §4.1b#r5: [10, 54, 65, 89]
  §4.1b#r6: [10, 55, 66, 90]
  §4.1b#r7: [10, 56, 58, 67, 91]
  §4.1b#r8: [9, 16, 47, 49, 92]
  §4.1b#r9: [9, 17, 34, 39, 41, 93]
  §4.1b#r10: [9, 18, 43, 94]
  §4.1b#r11: [9, 19, 21, 22, 23, 35, 45, 51, 95, 139, 140]
  §4.1b#r12: [9, 24, 26, 46, 96, 137]
  §4.1b#r13: [9, 27, 97]
  §4.1b#r14: [9, 28, 37, 40, 98]
  §4.1b#r15: [9, 29, 31, 36, 42, 99]
  §4.1b#r16: [9, 32, 38, 100]
  §4.1b#r17: [10, 59, 68, 111]
  §4.1b#r18: [10, 60, 69, 101]
  §4.1b#r19: [10, 61, 70, 102]
  §4.1b#r20: [10, 62, 71, 103]
  §4.1b#r21: [10, 63, 72, 104]
  §4.1b#r22: [10, 74, 105]
  §4.1b#r23: [10, 75, 77, 106]
  §4.1b#r24: [10, 76, 78, 107, 142, 144, 146]
  §4.1b#r25: [10, 79, 82, 108]
  §4.1b#r26: [10, 80, 83, 109]
  §4.1b#r27: [10, 81, 84, 110]
  §4.1b#p1: [2, 3, 4, 5, 45, 46, 91, 92]
  §4.1b#p3: [115, 116]
  §7.1#r2: [121, 122, 126, 127]
  §5#r5: [5, 6]
  §4.1#r2: [2, 7, 87]
  §4.3#r7: [121, 126, 130]
  EB-TBL-1@tabel-history: [121, 122, 126, 127, 128, 130, 131, 132, 134]
  EB-TBL-2@tabel-history: [35, 64, 77]
  EB-TBL-4@tabel-history: [19, 21, 24, 29, 42, 51]
anchor: []
coverage:
  web: automated
---

# Tabel History: tampilan awal, kolom default, Duration, Resolved By System, empty state, dan tanpa Bulk

## Prerequisites
- Aktor: Total Control (Aktor Missing), berhak melihat nilai finansial.
- Layar awal: Assets > Missing > History.
- Komponen: Halaman Missing sub-tab History (tabel T-MIS-02)
- Data:
  - DU-053-1: Record History Found, diselesaikan Rina Wulandari. Name `Laptop Dell Latitude 5420 - 9`; Asset ID `LPT-2026-0009`; Group `Head Office`; Hierarki Group `Head Office`; Status `Found`; Source `Borrow`; Last Holder `Sari Dewanti`; Last Holder tampil `Sari D`; Last Holder Division `Finance`; Last Holder Employee ID `EMP-0207`; Reported By `Rina Wulandari`; Reported By tampil `Rina W`; Reported Date `2026-10-12T09:00:00Z`; Reported Date tampil `12/10/26, 09:00`; Duration `6`; Duration tampil `6 days`; Resolved By `Rina Wulandari`; Resolved By tampil `Rina W`; Resolved Date `2026-10-18T14:10:00Z`; Resolved Date tampil `18/10/26, 14:10`; Photo `laptop-dell-9.jpg`.
  - DU-053-2: Record History Disposed, diselesaikan System, tanpa Last Holder. Name `Drill Bosch GSB - 4`; Asset ID `DRL-2026-0004`; Group `Warehouse`; Hierarki Group `Warehouse`; Status `Disposed`; Source `Manual`; Last Holder `null`; Last Holder tampil `—`; Reported By `Agus Prasetyo`; Reported By tampil `Agus P`; Reported Date `2026-08-01T08:00:00Z`; Reported Date tampil `01/08/26, 08:00`; Duration `62`; Duration tampil `62 days`; Resolved By `System`; Resolved By tampil `System`; Resolved Date `2026-10-02T00:00:00Z`; Resolved Date tampil `02/10/26, 00:00`; Photo `drill-bosch-4.jpg`.
  - DU-053-3: Record History Rejected dengan Duration satu hari. Name `Camera Canon EOS - 1`; Asset ID `CAM-2026-0001`; Group `Head Office`; Hierarki Group `Head Office`; Status `Rejected`; Source `Reported by holder`; Last Holder `Budi Santoso`; Last Holder tampil `Budi S`; Reported By `Budi Santoso`; Reported By tampil `Budi S`; Reported Date `2026-11-05T08:30:00Z`; Reported Date tampil `05/11/26, 08:30`; Duration `1`; Duration tampil `1 day`; Resolved By `Rina Wulandari`; Resolved By tampil `Rina W`; Resolved Date `2026-11-06T09:15:00Z`; Resolved Date tampil `06/11/26, 09:15`; Photo `camera-canon-1.jpg`.
  - DU-053-4: Record History Canceled oleh pelapor. Name `Scanner Zebra DS2208 - 2`; Asset ID `SCN-2026-0002`; Group `Warehouse`; Hierarki Group `Warehouse`; Status `Canceled`; Source `Reported by holder`; Last Holder `Joko Susanto`; Last Holder tampil `Joko S`; Reported By `Joko Susanto`; Reported By tampil `Joko S`; Reported Date `2026-11-03T13:00:00Z`; Reported Date tampil `03/11/26, 13:00`; Duration `1`; Duration tampil `1 day`; Resolved By `Joko Susanto`; Resolved By tampil `Joko S`; Resolved Date `2026-11-04T08:20:00Z`; Resolved Date tampil `04/11/26, 08:20`; Photo `scanner-zebra-2.jpg`.
  - DU-053-5: Record History Found dengan pengguna yang kemudian dihapus. Name `Tablet Samsung Galaxy Tab A8 - 3`; Asset ID `TAB-2026-0003`; Group `Finance Room`; Hierarki Group `Head Office > Finance Room`; Status `Found`; Source `Transfer`; Last Holder `Maya Kusuma`; Last Holder tampil `Maya K`; Status akun Maya Kusuma `dihapus sesudah record selesai`; Reported By `Maya Kusuma`; Reported By tampil `Maya K`; Reported Date `2026-10-20T10:00:00Z`; Reported Date tampil `20/10/26, 10:00`; Duration `3`; Duration tampil `3 days`; Resolved By `Rina Wulandari`; Resolved By tampil `Rina W`; Resolved Date `2026-10-23T15:45:00Z`; Resolved Date tampil `23/10/26, 15:45`; Photo `tablet-samsung-3.jpg`.
  - DU-053-6: Record History dengan seluruh kolom Curated terisi. Name `Mobile Printer Zebra ZQ320 - 5`; Asset ID `PRN-2026-0205`; Group `Head Office`; Status `Found`; Brand `Zebra Technologies`; Model/Type `Mobile Printer ZQ320`; TAG `BLE, QR`; Category `Mobile Printer`; Hierarki Category `Hardware > Printer > Mobile Printer`; Alias Name `Printer Lapangan`; Measurement `Unit`; Division `Operations`; Labels `Portable, Priority`; Asset Class `Electronic Equipment`; Register Date `2024-06-01`; Register Date tampil `01/06/24`; Purchase Date `2024-05-20`; Purchase Date tampil `20/05/24`; Daftar garansi `Garansi Pabrik — 2026-12-05 | Garansi Layanan Purna Jual — 2027-04-18 | Garansi Baterai — 2027-09-30`; Warranty Expiry (Warranty until terdekat) `2026-12-05`; Warranty Expiry tampil `05/12/26`; Hover daftar garansi `Garansi Pabrik — 05/12/26 | Garansi Layanan Purna Jual — 18/04/27 | Garansi Baterai — 30/09/27`; Purchase Cost `4500000`; Asset Value (Commercial) `3200000`; Asset Value (Fiscal) `2800000`.
  - DU-053-7: Record History dengan kolom Curated kosong. Name `Lemari Arsip Besi - 2`; Asset ID `FRN-2026-0302`; Group `Head Office`; Status `Found`; Brand `null`; Model/Type `null`; TAG `null`; Category `Furniture`; Hierarki Category `Furniture`; Alias Name `null`; Measurement `null`; Division `null`; Labels `null`; Asset Class `null`; Register Date `2025-02-14`; Register Date tampil `14/02/25`; Purchase Date `null`; Warranty Expiry `null`; Purchase Cost `null`; Asset Value (Commercial) `null`; Asset Value (Fiscal) `null`.
  - DU-053-8: Kata kunci Search tanpa hasil. Kata kunci Search `ZZZ-TIDAK-ADA`.
  - DU-053-9: Record History Found tanpa foto, dilaporkan PIC atas nama pemegang tanpa akun. Name `Forklift Toyota 8FD - 6`; Asset ID `FLK-2026-0006`; Group `Warehouse`; Hierarki Group `Warehouse`; Status `Found`; Source `Reported by holder`; Last Holder `Joko Susanto`; Last Holder tampil `Joko S`; Last Holder hover PIC `PIC: Rudi Hartono`; Reported By `Rudi Hartono (PIC) atas nama Joko Susanto`; Reported By tampil `Rudi H (on behalf of Joko S)`; Reported Date `2026-10-25T07:15:00Z`; Reported Date tampil `25/10/26, 07:15`; Duration `2`; Duration tampil `2 days`; Resolved By `Rina Wulandari`; Resolved By tampil `Rina W`; Resolved Date `2026-10-27T10:30:00Z`; Resolved Date tampil `27/10/26, 10:30`; Photo `tanpa foto (avatar inisial)`.
  - DU-053-10: Record History Found dengan tiga garansi yang urutan daftarnya tidak dimulai dari garansi terdekat. Name `Generator Honda EU22i - 4`; Asset ID `GEN-2026-0104`; Group `Warehouse`; Status `Found`; Register Date `2025-04-11`; Register Date tampil `11/04/25`; Purchase Date `2025-04-01`; Purchase Date tampil `01/04/25`; Daftar garansi `Garansi Mesin — 2028-04-01 | Garansi Aki — 2027-01-15 | Garansi Servis — 2026-12-12`; Warranty Expiry (Warranty until terdekat) `2026-12-12`; Warranty Expiry tampil `12/12/26`; Hover daftar garansi `Garansi Mesin — 01/04/28 | Garansi Aki — 15/01/27 | Garansi Servis — 12/12/26`; Purchase Cost `18500000`; Asset Value (Commercial) `16200000`; Asset Value (Fiscal) `14800000`.
- Kondisi:
  - K1: Date Format bernilai `DD/MM/YY`, Time Format bernilai `HH:mm`, dan Time Zone bernilai `UTC`; daftar History berisi DU-053-1 sampai DU-053-5; kolom yang tampil adalah kolom bawaan tabel
  - K2: preferensi kolom tersimpan menampilkan hanya kolom `Name`, `Brand`, `Model/Type`, `TAG`, `Category`, `Group`, `Alias Name`, `Measurement`, `Division`, `Labels`, dan `Asset Class`; daftar History berisi DU-053-6 dan DU-053-7
  - K3: Date Format bernilai `DD/MM/YY`, Time Format bernilai `HH:mm`, dan Time Zone bernilai `UTC`; preferensi kolom tersimpan menampilkan hanya kolom `Name`, `Register Date`, `Purchase Date`, `Warranty Expiry`, `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`; aktor berhak melihat nilai finansial; daftar History berisi DU-053-6, DU-053-7, dan DU-053-10
  - K4: daftar History kosong tanpa Search dan Filter
  - K5: daftar History berisi DU-053-1 sampai DU-053-5; pencarian `ZZZ-TIDAK-ADA` (DU-053-8) dijawab daftar kosong
  - K6: memuat daftar History gagal karena error server pada percobaan pertama, lalu berhasil berisi DU-053-1 sampai DU-053-5 pada percobaan kedua
  - K7: Date Format bernilai `DD/MM/YY`, Time Format bernilai `HH:mm`, dan Time Zone bernilai `UTC`; daftar History berisi DU-053-9; kolom yang tampil adalah kolom bawaan tabel

## Test Steps

### Toolbar History dan tabel tanpa Bulk
1. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K1
2. Verifikasi tombol Search, Filter, dan Download tampil pada toolbar tab History
3. Verifikasi tombol `[Scan Found Asset]` tidak tampil pada toolbar tab History
4. Verifikasi tidak ada kartu ringkasan jumlah record di atas tabel
5. Verifikasi kolom Checkbox tidak tampil pada tabel History
6. Verifikasi bulk bar tidak tampil pada tab History
7. Verifikasi kolom Actions tampil pada setiap baris tabel History

### Kolom bawaan dan kolom Curated tabel History
8. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K1
9. Verifikasi kolom tabel History tampil berurutan `Photo`, `Name`, `Asset ID`, `Group`, `Status`, `Source`, `Last Holder`, `Reported By`, `Reported Date`, `Duration`, `Resolved By`, `Resolved Date`
10. Verifikasi kolom `Brand`, `Model/Type`, `TAG`, `Category`, `Alias Name`, `Measurement`, `Division`, `Labels`, `Asset Class`, `Register Date`, `Purchase Date`, `Warranty Expiry`, `Purchase Cost`, `Asset Value (Commercial)`, `Asset Value (Fiscal)` tidak tampil

### Baris Found Laptop Dell Latitude 5420 - 9
11. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K1
12. Verifikasi foto aset tampil pada baris `Laptop Dell Latitude 5420 - 9`
13. Verifikasi header `Photo` tidak memiliki ikon sort
14. Verifikasi Name `Laptop Dell Latitude 5420 - 9` tampil sebagai tautan teks
15. Verifikasi Asset ID `LPT-2026-0009` tampil pada baris `Laptop Dell Latitude 5420 - 9`
16. Verifikasi Group `Head Office` tampil pada baris `Laptop Dell Latitude 5420 - 9`
17. Verifikasi Status `Found` tampil pada baris `Laptop Dell Latitude 5420 - 9`
18. Verifikasi Source `Borrow` tampil tanpa nomor transaksi pada baris `Laptop Dell Latitude 5420 - 9`
19. Verifikasi Last Holder `Sari D` tampil pada baris `Laptop Dell Latitude 5420 - 9`
20. Arahkan kursor ke Last Holder `Sari D` pada baris `Laptop Dell Latitude 5420 - 9`
21. Verifikasi nama lengkap `Sari Dewanti` tampil
22. Verifikasi Division pemegang `Finance` tampil
23. Verifikasi Employee ID `EMP-0207` tampil
24. Verifikasi Reported By `Rina W` tampil pada baris `Laptop Dell Latitude 5420 - 9`
25. Arahkan kursor ke Reported By `Rina W` pada baris `Laptop Dell Latitude 5420 - 9`
26. Verifikasi nama lengkap `Rina Wulandari` tampil
27. Verifikasi Reported Date `12/10/26, 09:00` tampil pada baris `Laptop Dell Latitude 5420 - 9`
28. Verifikasi Duration `6 days` tampil pada baris `Laptop Dell Latitude 5420 - 9`
29. Verifikasi Resolved By `Rina W` tampil pada baris `Laptop Dell Latitude 5420 - 9`
30. Arahkan kursor ke Resolved By `Rina W` pada baris `Laptop Dell Latitude 5420 - 9`
31. Verifikasi nama lengkap `Rina Wulandari` tampil
32. Verifikasi Resolved Date `18/10/26, 14:10` tampil pada baris `Laptop Dell Latitude 5420 - 9`

### Baris Disposed, Rejected, dan Canceled
33. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K1
34. Verifikasi Status `Disposed` tampil pada baris `Drill Bosch GSB - 4`
35. Verifikasi Last Holder `—` tampil pada baris `Drill Bosch GSB - 4`
36. Verifikasi Resolved By `System` tampil pada baris `Drill Bosch GSB - 4`
37. Verifikasi Duration `62 days` tampil pada baris `Drill Bosch GSB - 4`
38. Verifikasi Resolved Date `02/10/26, 00:00` tampil pada baris `Drill Bosch GSB - 4`
39. Verifikasi Status `Rejected` tampil pada baris `Camera Canon EOS - 1`
40. Verifikasi Duration `1 day` dalam bentuk tunggal pada baris `Camera Canon EOS - 1`
41. Verifikasi Status `Canceled` tampil pada baris `Scanner Zebra DS2208 - 2`
42. Verifikasi Resolved By `Joko S` tampil pada baris `Scanner Zebra DS2208 - 2`
43. Verifikasi Source `Reported by holder` tampil pada baris `Scanner Zebra DS2208 - 2`

### Pengguna yang kemudian dihapus tetap tampil pada Last Holder, Reported By, dan Group
44. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K1
45. Verifikasi Last Holder `Maya K` tetap tampil pada baris `Tablet Samsung Galaxy Tab A8 - 3`
46. Verifikasi Reported By `Maya K` tetap tampil pada baris `Tablet Samsung Galaxy Tab A8 - 3`
47. Verifikasi Group `Finance Room` tampil pada baris `Tablet Samsung Galaxy Tab A8 - 3`
48. Arahkan kursor ke badge Group `Finance Room`
49. Verifikasi hierarki lengkap `Head Office > Finance Room` tampil
50. Arahkan kursor ke Last Holder `Maya K` pada baris `Tablet Samsung Galaxy Tab A8 - 3`
51. Verifikasi nama lengkap `Maya Kusuma` tampil

### Kolom Curated Brand sampai Asset Class
52. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K2
53. Verifikasi Brand `Zebra Technologies` tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
54. Verifikasi Model/Type `Mobile Printer ZQ320` tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
55. Verifikasi dua ikon TAG berlabel `BLE` dan `QR` tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
56. Verifikasi Category `Mobile Printer` tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
57. Arahkan kursor ke badge Category `Mobile Printer`
58. Verifikasi hierarki lengkap `Hardware > Printer > Mobile Printer` tampil
59. Verifikasi Alias Name `Printer Lapangan` tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
60. Verifikasi Measurement `Unit` tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
61. Verifikasi Division `Operations` tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
62. Verifikasi dua badge Labels `Portable` dan `Priority` tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
63. Verifikasi Asset Class `Electronic Equipment` tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
64. Verifikasi Brand `—` tampil pada baris `Lemari Arsip Besi - 2`
65. Verifikasi Model/Type `—` tampil pada baris `Lemari Arsip Besi - 2`
66. Verifikasi TAG `—` tampil pada baris `Lemari Arsip Besi - 2`
67. Verifikasi Category `Furniture` tampil, tidak kosong, pada baris `Lemari Arsip Besi - 2`
68. Verifikasi Alias Name `—` tampil pada baris `Lemari Arsip Besi - 2`
69. Verifikasi Measurement `—` tampil pada baris `Lemari Arsip Besi - 2`
70. Verifikasi Division `—` tampil pada baris `Lemari Arsip Besi - 2`
71. Verifikasi Labels `—` tampil pada baris `Lemari Arsip Besi - 2`
72. Verifikasi Asset Class `—` tampil pada baris `Lemari Arsip Besi - 2`

### Kolom Curated tanggal dan nilai finansial
73. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K3
74. Verifikasi Register Date `01/06/24` tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
75. Verifikasi Purchase Date `20/05/24` tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
76. Verifikasi Warranty Expiry `05/12/26`, Warranty until terdekat dari tiga garansi aset, tampil pada baris `Mobile Printer Zebra ZQ320 - 5`
77. Verifikasi Purchase Date `—` tampil pada baris `Lemari Arsip Besi - 2`
78. Verifikasi Warranty Expiry `—` tampil pada baris `Lemari Arsip Besi - 2`
79. Verifikasi Purchase Cost tampil sebagai nilai mata uang Company dari `4500000` pada baris `Mobile Printer Zebra ZQ320 - 5`
80. Verifikasi Asset Value (Commercial) tampil sebagai nilai mata uang Company dari `3200000` pada baris `Mobile Printer Zebra ZQ320 - 5`
81. Verifikasi Asset Value (Fiscal) tampil sebagai nilai mata uang Company dari `2800000` pada baris `Mobile Printer Zebra ZQ320 - 5`
82. Verifikasi Purchase Cost `—` tampil pada baris `Lemari Arsip Besi - 2`
83. Verifikasi Asset Value (Commercial) `—` tampil pada baris `Lemari Arsip Besi - 2`
84. Verifikasi Asset Value (Fiscal) `—` tampil pada baris `Lemari Arsip Besi - 2`

### Filter Panel tabel History: label, tipe, dan placeholder setiap field
85. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K1
86. Klik tombol Filter
87. Verifikasi panel Filter tabel History terbuka
88. Verifikasi field filter `Brand` pada tabel History berupa multi-select searchable dengan placeholder `All brands`
89. Verifikasi field filter `Model/Type` pada tabel History berupa multi-select searchable dengan placeholder `All models`
90. Verifikasi field filter `TAG` pada tabel History berupa multi-select searchable dengan placeholder `All tags`
91. Verifikasi field filter `Category` pada tabel History berupa multi-select searchable dengan placeholder `All categories`
92. Verifikasi field filter `Group` pada tabel History berupa multi-select searchable dengan placeholder `All groups`
93. Verifikasi field filter `Status` pada tabel History berupa multi-select searchable dengan placeholder `All statuses`
94. Verifikasi field filter `Source` pada tabel History berupa multi-select searchable dengan placeholder `All sources`
95. Verifikasi field filter `Last Holder` pada tabel History berupa multi-select searchable dengan placeholder `All users`
96. Verifikasi field filter `Reported By` pada tabel History berupa multi-select searchable dengan placeholder `All users`
97. Verifikasi field filter `Reported Date` pada tabel History berupa date range picker dengan placeholder `Select date`
98. Verifikasi field filter `Duration` pada tabel History berupa rentang dengan placeholder `Min` dan `Max`
99. Verifikasi field filter `Resolved By` pada tabel History berupa multi-select searchable dengan placeholder `All users`
100. Verifikasi field filter `Resolved Date` pada tabel History berupa date range picker dengan placeholder `Select date`
101. Verifikasi field filter `Measurement` pada tabel History berupa multi-select searchable dengan placeholder `All measurements`
102. Verifikasi field filter `Division` pada tabel History berupa multi-select searchable dengan placeholder `All divisions`
103. Verifikasi field filter `Label` pada tabel History berupa multi-select searchable dengan placeholder `All labels`
104. Verifikasi field filter `Asset Class` pada tabel History berupa multi-select searchable dengan placeholder `All asset classes`
105. Verifikasi field filter `Register Date` pada tabel History berupa date range picker dengan placeholder `Select date`
106. Verifikasi field filter `Purchase Date` pada tabel History berupa date range picker dengan placeholder `Select date`
107. Verifikasi field filter `Warranty Expiry` pada tabel History berupa date range picker dengan placeholder `Select date`
108. Verifikasi field filter `Purchase Cost` pada tabel History berupa rentang dengan placeholder `Min` dan `Max`
109. Verifikasi field filter `Asset Value (Commercial)` pada tabel History berupa rentang dengan placeholder `Min` dan `Max`
110. Verifikasi field filter `Asset Value (Fiscal)` pada tabel History berupa rentang dengan placeholder `Min` dan `Max`
111. Verifikasi tidak ada field filter tabel History untuk `Photo`, `Name`, `Asset ID`, dan `Alias Name`
112. Klik tombol Filter

### Menu aksi baris History dan tautan Name
113. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K1
114. Klik `⋯` pada baris `Drill Bosch GSB - 4`
115. Verifikasi opsi `Missing Log` tampil pada menu aksi baris tabel History
116. Verifikasi tidak ada opsi `Report Disposal` pada menu aksi baris record Disposed
117. Tekan Esc
118. Klik Name `Laptop Dell Latitude 5420 - 9`
119. Verifikasi dialog `Missing Log` terbuka

### Empty state tabel History belum ada data
120. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K4
121. Verifikasi `No resolved records yet` tampil
122. Verifikasi `Found, disposed, rejected, and canceled reports will appear here.` tampil

### Empty state tabel History kosong akibat pencarian
123. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K5
124. Klik tombol Search
125. Ketik Search `ZZZ-TIDAK-ADA`, tekan Enter
126. Verifikasi `No results found` tampil
127. Verifikasi `Try adjusting your search or filter.` tampil pada tabel History
128. Verifikasi `No resolved records yet` tidak tampil

### Gagal muat tabel History
129. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K6
130. Verifikasi `Unable to load this data.` tampil
131. Verifikasi tombol `[Try Again]` tampil pada tabel History
132. Verifikasi `No resolved records yet` tidak tampil
133. Klik tombol `[Try Again]`
134. Verifikasi baris `Laptop Dell Latitude 5420 - 9` tampil

### Avatar inisial, PIC pada Last Holder, dan laporan atas nama pada tabel History
135. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K7
136. Verifikasi avatar inisial tampil pada baris `Forklift Toyota 8FD - 6` karena belum ada foto
137. Verifikasi Reported By `Rudi H (on behalf of Joko S)` tampil pada baris `Forklift Toyota 8FD - 6`
138. Arahkan kursor ke Last Holder `Joko S` pada baris `Forklift Toyota 8FD - 6`
139. Verifikasi nama lengkap `Joko Susanto` tampil pada hover Last Holder baris `Forklift Toyota 8FD - 6`
140. Verifikasi `PIC: Rudi Hartono` tampil pada hover Last Holder baris `Forklift Toyota 8FD - 6`

### Warranty Expiry: Warranty until terdekat dan daftar seluruh garansi saat hover
141. Tampilkan Halaman Missing sub-tab History (tabel T-MIS-02) dengan kondisi K3
142. Verifikasi Warranty Expiry `12/12/26`, Warranty until terdekat dari tiga garansi aset, tampil pada baris `Generator Honda EU22i - 4`
143. Arahkan kursor ke Warranty Expiry `12/12/26` pada baris `Generator Honda EU22i - 4`
144. Verifikasi daftar seluruh garansi memuat tiga entri `Garansi Mesin — 01/04/28`, `Garansi Aki — 15/01/27`, dan `Garansi Servis — 12/12/26`
145. Arahkan kursor ke Warranty Expiry `05/12/26` pada baris `Mobile Printer Zebra ZQ320 - 5`
146. Verifikasi daftar seluruh garansi memuat tiga entri `Garansi Pabrik — 05/12/26`, `Garansi Layanan Purna Jual — 18/04/27`, dan `Garansi Baterai — 30/09/27`
