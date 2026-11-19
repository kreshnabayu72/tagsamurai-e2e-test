---
id: TC-FA-BORROW-E2E-021-handover-scan-foto-sebagian
title: "Halaman Handover memverifikasi aset lewat scan TAG atau I Can't Scan the TAG, foto, dan handover sebagian"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-BRW-55", "FI-BRW-56", "FI-BRW-57", "FI-BRW-58", "FI-BRW-59", "FI-BRW-60", "FI-BRW-61", "FI-BRW-62", "FI-BRW-63", "FI-BRW-64", "FI-BRW-65", "FI-BRW-66", "FI-BRW-67", "FI-BRW-68", "FI-BRW-69", "FI-BRW-70", "FLD-BRW-07", "FLD-BRW-20", "FLD-BRW-21", "V-BRW-28", "V-BRW-29", "V-BRW-30", "V-BRW-31", "§4.2.5#p1", "§4.2.5#p2", "§4.4#r10", "§4.4#r11"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-55": 71
  "FI-BRW-56": 95
  "FI-BRW-57": 92
  "FI-BRW-58": 93
  "FI-BRW-59": [50, 52, 54, 55]
  "FI-BRW-60": 57
  "FI-BRW-61": 57
  "FI-BRW-62": 59
  "FI-BRW-63": 61
  "FI-BRW-64": 64
  "FI-BRW-65": 65
  "FI-BRW-66": [97, 107, 109]
  "FI-BRW-67": [66, 122]
  "FI-BRW-68": 71
  "FI-BRW-69": 65
  "FI-BRW-70": 101
  "FLD-BRW-07": 74
  "FLD-BRW-20": 68
  "FLD-BRW-21": [74, 76, 89]
  "V-BRW-28": [50, 52, 54]
  "V-BRW-29": 57
  "V-BRW-30": 68
  "V-BRW-31": [74, 89]
  "§4.2.5#p1": [8, 9, 115]
  "§4.2.5#p2": [6, 7, 10, 11, 12, 13, 14, 16, 18, 20, 21, 26, 27, 32, 33, 38, 39, 44, 45, 72, 78, 80, 82, 84, 86, 128, 129, 130, 131]
  "§4.4#r10": 50
  "§4.4#r11": 52
anchor: []
coverage:
  web: automated
---

# Halaman Handover memverifikasi aset lewat scan TAG atau I Can't Scan the TAG, foto, dan handover sebagian

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office`; ia bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-021-1: BRW `Waiting for Handover` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, Note `Peminjaman untuk acara kantor`, Photo at start ON pada semua barisnya. Barisnya adalah aset DU-021-2, DU-021-3, DU-021-4, dan DU-021-5 berstatus `Waiting for Handover`, dan aset DU-021-6 berstatus `Borrowed`.
  - DU-021-2: aset `Laptop Asus Zenbook {runId}`, Brand `Asus`, Model/Type `Zenbook 14`, TAG `RFID`, Category `Laptop`, Duration `3 / 7 days`, Purpose `Presentasi klien`.
  - DU-021-3: aset `Proyektor BenQ {runId}`, Brand `BenQ`, Model/Type `MW535`, TAG `QR`, Category `Proyektor`, Duration `2 / 7 days`, Purpose `Rapat divisi`.
  - DU-021-4: aset `Kamera Canon EOS {runId}`, Brand `Canon`, Model/Type `EOS 90D`, TAG `NFC`, Category `Kamera`, Duration `4 / 7 days`, Purpose `Dokumentasi acara`.
  - DU-021-5: aset `Speaker JBL {runId}`, Brand `JBL`, Model/Type `PartyBox 310`, TAG `RFID` yang tidak terbaca saat dipindai, Category `Audio`, Duration `1 / 3 days`, Purpose `Acara gathering`; Note laporan TAG yang dicoba `TAG tidak terbaca di lokasi serah terima`.
  - DU-021-6: aset `Headset Logitech {runId}` pada BRW yang sama dengan status `Borrowed`.
  - DU-021-7: aset `Genset Honda {runId}` pada BRW lain berstatus `Waiting for Approval` dengan approver `Rina W`.
  - DU-021-8: aset `Router Cisco {runId}` milik Group `Branch Surabaya`, di luar Group Aktor.
  - DU-021-9: aset `Printer HP {runId}` berstatus tersedia dan tidak berada di BRW DU-021-1; Asset ID-nya milik entri ini.
  - Asset ID aset DU-021-2 sampai DU-021-9 dibentuk sistem dan menjadi milik entri aset masing-masing.
  - DU-021-10: BRW `Waiting for Handover` Group `Head Office`, Borrower `Wulan Sari {runId}`, Requested By `Agus Pratama {runId}`, dengan satu baris aset DU-021-11.
  - DU-021-11: aset `Mouse Logitech MX {runId}`, TAG `RFID` dengan laporan TAG terbuka berjenis `Unreadable`, status baris `Waiting for Handover`; batas pengambilan baris itu sudah terlewati saat job Transaction timeout berjalan.
  - Setelah Replace TAG selesai, aset DU-021-5 memiliki TAG pengganti `RFID` yang terbaca saat dipindai.
  - DU-021-12: BRW `Waiting for Handover` Group `Head Office`, Borrower `Intan Permata {runId}`, Requested By `Agus Pratama {runId}`, Photo at start OFF pada barisnya, dengan satu baris aset DU-021-13.
  - DU-021-13: aset `Kursi Lipat Chitose {runId}`, Brand `Chitose`, Model/Type `Y-50`, TAG `Non TAG`, Category `Furnitur`, Duration `2 / 7 days`, Purpose `Acara gathering`, status baris `Waiting for Handover`.

## Test Steps

### Halaman Handover hanya memuat baris Waiting for Handover
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
4. Klik menu ⋯ pada baris BRW milik DU-021-1
5. Klik `Hand Over`
6. Verifikasi header transaksi memuat Transaction ID milik DU-021-1, Requested By `Agus Pratama {runId}`, Borrower `Hendra Kusuma {runId}`, Group `Head Office`, Note `Peminjaman untuk acara kantor`, dan Last Updated
7. Verifikasi header transaksi memuat tombol `[Copy]` untuk Transaction ID milik DU-021-1 dan badge status header `Waiting for Handover`
8. Verifikasi tabel Handover memuat aset DU-021-2, DU-021-3, DU-021-4, dan DU-021-5
9. Verifikasi tabel Handover tidak memuat aset DU-021-6 yang berstatus `Borrowed`
10. Verifikasi toolbar Handover memuat Search, Filter, dan tombol `[Verify Asset]`
11. Verifikasi kolom Verification baris DU-021-2 `Unverified`
12. Verifikasi baris DU-021-2 menampilkan Name `Laptop Asus Zenbook {runId}`, Asset ID milik DU-021-2, Brand `Asus`, Model/Type `Zenbook 14`, TAG `RFID`, Duration `3 / 7 days`, dan Purpose `Presentasi klien`
13. Verifikasi kolom Handover Photo baris DU-021-2 kosong dan menyediakan tombol ambil foto
14. Verifikasi teks bantu `Scanned assets are ready. Ask [Borrower] to confirm.` tidak tampil sebelum ada aset yang discan
15. Urutkan kolom `Duration` dengan `Shortest First`
16. Verifikasi urutan dari atas ke bawah adalah DU-021-5, DU-021-3, DU-021-2, DU-021-4
17. Urutkan kolom `Purpose` secara Alphabetical (A–Z)
18. Verifikasi urutan dari atas ke bawah adalah DU-021-5, DU-021-4, DU-021-2, DU-021-3
19. Ketik Search `Kamera Canon EOS {runId}`, tekan Enter
20. Verifikasi baris DU-021-4 tampil
21. Verifikasi baris DU-021-2, DU-021-3, dan DU-021-5 tidak tampil
22. Klik `(←)` pada kotak Search
23. Klik ikon Filter
24. Pada field `Brand` pilih `Canon`
25. Klik `[Apply]`
26. Verifikasi baris DU-021-4 tampil
27. Verifikasi baris DU-021-2, DU-021-3, dan DU-021-5 tidak tampil
28. Klik `[Clear Field]`
29. Klik `[Apply]`
30. Klik ikon Filter

### Search Asset ID dan Filter Category serta Brand dengan beberapa pilihan
31. Ketik Search Asset ID milik DU-021-3, tekan Enter
32. Verifikasi baris DU-021-3 tampil
33. Verifikasi baris DU-021-2, DU-021-4, dan DU-021-5 tidak tampil
34. Klik `(←)` pada kotak Search
35. Klik ikon Filter
36. Pada field `Category` pilih `Laptop`
37. Klik `[Apply]`
38. Verifikasi baris DU-021-2 tampil
39. Verifikasi baris DU-021-3, DU-021-4, dan DU-021-5 tidak tampil
40. Klik `[Clear Field]`
41. Klik `[Apply]`
42. Pada field `Brand` pilih `Asus` dan `BenQ`
43. Klik `[Apply]`
44. Verifikasi baris DU-021-2 dan DU-021-3 tampil
45. Verifikasi baris DU-021-4 dan DU-021-5 tidak tampil
46. Klik `[Clear Field]`
47. Klik `[Apply]`
48. Klik ikon Filter

### Scan ditolak untuk TAG yang bukan baris BRW ini
49. Scan TAG aset DU-021-9 lewat `[Verify Asset]`
50. Verifikasi toast `Error, this TAG belongs to [Asset Code], not in this borrow.` tampil dengan [Asset Code] berisi Asset ID milik DU-021-9
51. Scan TAG aset DU-021-7 lewat `[Verify Asset]`
52. Verifikasi toast `Error, this asset is still waiting for approval from [Names].` tampil dengan [Names] berisi `Rina W`
53. Scan TAG aset DU-021-8 lewat `[Verify Asset]`
54. Verifikasi toast `Error, this asset belongs to [Group].` tampil dengan [Group] berisi `Branch Surabaya`
55. Verifikasi kolom Verification baris DU-021-2, DU-021-3, DU-021-4, dan DU-021-5 tidak berubah dan tidak ada yang `Verified`

### Aset ber-tag yang tagnya tidak terbaca dilaporkan lewat I Can't Scan the TAG
56. Scan TAG aset DU-021-5 lewat `[Verify Asset]`
57. Verifikasi toast `Error, this TAG can't be read. Report the TAG and use another asset.` tampil dan handover aset DU-021-5 tidak dapat dimulai tanpa identifikasi manual
58. Klik menu ⋯ pada baris DU-021-5
59. Verifikasi menu ⋯ baris DU-021-5 memuat `I Can't Scan the TAG`
60. Klik `I Can't Scan the TAG`
61. Verifikasi dialog Report TAG biasa tampil dengan Report Type `Unreadable`, bukan varian identifikasi manual
62. Isi Note laporan dengan `TAG tidak terbaca di lokasi serah terima`
63. Klik tombol kirim laporan pada dialog Report TAG
64. Verifikasi kolom Verification baris DU-021-5 menampilkan teks `TAG reported. Replace the TAG to hand over.`
65. Verifikasi baris DU-021-5 nonaktif untuk Verify, foto, dan Request Confirmation, tanpa pilihan identifikasi manual untuk Aktor ini
66. Verifikasi baris DU-021-5 tetap tampil di daftar Handover sebagai `Waiting for Handover`

### Request Confirmation memerlukan minimal satu aset terverifikasi dan foto per aset
67. Klik `[Request Confirmation]`
68. Verifikasi pesan `Verify at least one asset with Verify Asset.` tampil di atas tombol `[Request Confirmation]`
69. Scan TAG aset DU-021-2 lewat `[Verify Asset]`
70. Scan TAG aset DU-021-3 lewat `[Verify Asset]`
71. Verifikasi kolom Verification baris DU-021-2 dan DU-021-3 `Verified` dan baris DU-021-4 tetap `Unverified`, sehingga aset lain tetap dapat diserahkan
72. Verifikasi teks bantu `Scanned assets are ready. Ask [Borrower] to confirm.` tampil
73. Klik `[Request Confirmation]`
74. Verifikasi pesan `2 assets need a handover photo.` tampil di atas tombol `[Request Confirmation]`
75. Ambil foto pada kolom Handover Photo baris DU-021-2
76. Verifikasi kolom Handover Photo baris DU-021-2 menampilkan thumbnail foto
77. Klik thumbnail foto pada kolom Handover Photo baris DU-021-2
78. Verifikasi pratinjau foto ukuran penuh tampil
79. Tutup pratinjau foto
80. Verifikasi ikon Edit dan ikon Delete tampil di samping thumbnail pada kolom Handover Photo baris DU-021-2
81. Klik ikon Edit pada kolom Handover Photo baris DU-021-2
82. Verifikasi dialog `Adjust photo` tampil
83. Klik `Cancel` pada dialog `Adjust photo`
84. Verifikasi kolom Handover Photo baris DU-021-2 tetap menampilkan thumbnail foto sebelumnya
85. Klik ikon Delete pada kolom Handover Photo baris DU-021-2
86. Verifikasi kolom Handover Photo baris DU-021-2 kosong dan menyediakan tombol ambil foto
87. Ambil foto pada kolom Handover Photo baris DU-021-2
88. Klik `[Request Confirmation]`
89. Verifikasi pesan `1 asset needs a handover photo.` tampil di atas tombol `[Request Confirmation]`
90. Ambil foto pada kolom Handover Photo baris DU-021-3

### Handover sebagian: aset yang belum discan tetap Waiting for Handover
91. Klik `[Request Confirmation]`
92. Verifikasi popup `Waiting for Confirmation` tampil dengan pesan `1 asset will stay Waiting for Handover.`
93. Verifikasi daftar aset sesi konfirmasi memuat aset DU-021-2 dan DU-021-3 saja, tanpa aset DU-021-4
94. Klik `[Cancel Request]`
95. Verifikasi aset DU-021-2, DU-021-3, DU-021-4, dan DU-021-5 tetap `Waiting for Handover` sesudah permintaan dibatalkan

### Replace TAG selesai mengembalikan baris ke Unverified
96. Replace TAG aset DU-021-5 selesai dan laporan TAG terbuka ditutup `Replaced`
97. Verifikasi kolom Verification baris DU-021-5 kembali `Unverified` tanpa memuat ulang halaman
98. Buka Borrow Detail BRW milik DU-021-1 dari tabel Transactions
99. Klik menu ⋯ pada baris aset DU-021-5
100. Klik `Borrow Log`
101. Verifikasi Borrow Log aset DU-021-5 memuat node `TAG reported by [Reporter]` dengan daftar TAG yang dilaporkan

### Halaman Handover dibuka ulang sesudah Replace TAG dan aset discan dengan TAG pengganti
102. Klik `Transactions` pada sidebar
103. Klik `Borrow`
104. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
105. Klik menu ⋯ pada baris BRW milik DU-021-1
106. Klik `Hand Over`
107. Verifikasi kolom Verification baris DU-021-5 `Unverified` sesudah halaman Handover dibuka ulang
108. Scan TAG pengganti aset DU-021-5 lewat `[Verify Asset]`
109. Verifikasi kolom Verification baris DU-021-5 `Verified`

### Halaman Handover dibuka dari tombol Hand Over di Borrow Detail
110. Klik `Transactions` pada sidebar
111. Klik `Borrow`
112. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
113. Buka Borrow Detail BRW milik DU-021-1 dari tabel Transactions
114. Klik `Hand Over`
115. Verifikasi halaman Handover BRW milik DU-021-1 terbuka dengan tabel Handover memuat aset DU-021-2, DU-021-3, dan DU-021-4

### Baris dengan TAG dilaporkan tetap kena batas pengambilan
116. Klik `Transactions` pada sidebar
117. Klik `Borrow`
118. Job Transaction timeout berjalan sesudah batas pengambilan baris DU-021-11 terlewati
119. Klik tab `History`
120. Ketik Search `Wulan Sari {runId}`, tekan Enter
121. Buka Borrow Detail BRW milik DU-021-10 dari tabel History
122. Verifikasi baris aset DU-021-11 berstatus `Canceled (Not picked up)` walau TAG-nya dilaporkan

### Aset Non TAG dan Photo at start OFF pada halaman Handover
123. Klik `Transactions` pada sidebar
124. Klik `Borrow`
125. Ketik Search `Intan Permata {runId}`, tekan Enter
126. Klik menu ⋯ pada baris BRW milik DU-021-12
127. Klik `Hand Over`
128. Verifikasi kolom Verification baris DU-021-13 `Non TAG`
129. Verifikasi kolom Photo tampil pada tabel Handover dan baris DU-021-13 menampilkan Name `Kursi Lipat Chitose {runId}`
130. Verifikasi kolom Handover Photo tidak tampil pada tabel Handover karena Photo at start OFF
131. Verifikasi footer halaman Handover memuat `[Cancel]` dan tidak memuat `[Clear Field]`