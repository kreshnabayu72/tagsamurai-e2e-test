---
id: TC-FA-ASSIGN-E2E-002-transactions-search
title: "Search pada tab Transactions"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.1#p2", "§5#r2", "§5#r4", "EB-SRC-2@tabel-transactions", "EB-SRC-3@tabel-transactions", EB-SRC-1]
smoke: []
dependsOn: []
trace:
  "§4.2.1#p2": [1, 3, 10, 14, 18, 22, 26, 80, 82]
  "§5#r2": [4, 6, 11, 15, 19, 23, 88, 89, 90, 95, 96, 102, 103, 108, 109, 117, 118, 119]
  "§5#r4": [29, 31, 33, 37, 49, 51, 72, 74, 76, 78]
  "EB-SRC-2@tabel-transactions": [35, 43, 65, 70]
  "EB-SRC-3@tabel-transactions": [53, 54, 56, 60, 62, 63]
  EB-SRC-1: [29, 39, 41, 45, 47, 67]
anchor: [58, 113]
coverage:
  web: automated
---

# Search pada tab Transactions

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}`.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-002-1: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-002-2: Group `Head Office {runId}` dan Group `Branch Surabaya {runId}`.
  - DU-002-3: User `Agus Prasetyo {runId}`, role Asset Admin pada Group `Head Office {runId}` dan `Branch Surabaya {runId}`; ia pengaju semua ASG DU-002-9 sampai DU-002-14, sehingga kolom `Requested By` seragam.
  - DU-002-4: User `Budi Santoso {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Budi S`, dari `Budi Santoso {runId}`.
  - DU-002-5: User `Sari Dewi {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Sari D`, dari `Sari Dewi {runId}`.
  - DU-002-6: User `Dewi Anggraini {runId}`, karyawan aktif tanpa akses menu Assignment; PIC aktif keempat Division DU-002-7 dan DU-002-8.
  - DU-002-7: Division `Gudang Pusat {runId}` dan Division `Pusat {runId}`, nama yang satu memuat nama yang lain.
  - DU-002-8: Division `Surabaya Selatan {runId}` dan Division `Head Office Room {runId}`.
  - DU-002-9: ASG berstatus `Waiting for Handover` untuk Assignee DU-002-4, Group `Head Office {runId}`, aset `Switch Cisco 100% {runId}` beralias `Sw-Lobi-A1 {runId}` dan ber-TAG QR, Total Asset `1`; Asset ID dan kode TAG aset itu dibentuk server dan menjadi milik aset itu.
  - DU-002-10: ASG berstatus `Waiting for Approval` untuk Assignee DU-002-5, Group `Head Office {runId}`, aset `Switch Cisco 100X {runId}`, Total Asset `1`.
  - DU-002-11: ASG berstatus `Assigned` untuk Assignee Division `Gudang Pusat {runId}`, Group `Branch Surabaya {runId}`, aset `Printer Zebra ZD220 {runId}` ber-TAG QR, Total Asset `1`.
  - DU-002-12: ASG berstatus `Assigned` untuk Assignee Division `Pusat {runId}`, Group `Head Office {runId}`, aset `Kamera CCTV Hikvision {runId}` ber-TAG QR, Total Asset `1`.
  - DU-002-13: ASG berstatus `Waiting for Approval` untuk Assignee Division `Surabaya Selatan {runId}`, Group `Head Office {runId}`, aset `Tablet Samsung Tab A8 {runId}` (ber-TAG QR), `Tablet Samsung Tab A9 {runId}`, dan `Tablet Samsung Tab S9 {runId}`, Total Asset `3`.
  - DU-002-32: Draft untuk Assignee DU-002-5, Group `Head Office {runId}`, dengan aset `Mouse Logitech M331 {runId}` yang ber-TAG QR; Draft tidak bernomor.
  - DU-002-14: ASG berstatus `Waiting for Handover` untuk Assignee Division `Head Office Room {runId}`, Group `Head Office {runId}`, aset `Heater Panasonic {runId}`, Total Asset `1`.

## Test Steps

### Placeholder Search dan tombol Search by Scan di tiap tab
1. Verifikasi tab `Drafts` dan tab `Assigned Assets` masing-masing memuat badge angka, dan halaman Assignment tidak memuat kartu ringkas
2. Klik `Search` pada toolbar tab `Transactions`
3. Verifikasi kotak Search memuat placeholder `Search transaction ID, asset, or assignee...`
4. Verifikasi toolbar memuat tombol `Search by Scan` tepat di kiri tombol Search
5. Klik `Search by Scan`
6. Verifikasi dialog Search by Scan menawarkan tipe TAG `RFID`, `QR`, dan `NFC`
7. Tutup dialog Search by Scan
8. Klik tab `Assigned Assets`
9. Klik `Search` pada toolbar sub-tab `By Asset`
10. Verifikasi kotak Search memuat placeholder `Search transaction ID, asset, or assignee...` pada sub-tab `By Asset`
11. Verifikasi tombol `Search by Scan` tampil pada sub-tab `By Asset`
12. Klik sub-tab `By Assignee`
13. Klik `Search` pada toolbar sub-tab `By Assignee`
14. Verifikasi kotak Search memuat placeholder `Search assignee or asset...` pada sub-tab `By Assignee`
15. Verifikasi tombol `Search by Scan` tampil pada sub-tab `By Assignee`
16. Klik tab `Drafts`
17. Klik `Search` pada toolbar tab `Drafts`
18. Verifikasi kotak Search memuat placeholder `Search assignee or asset...` pada tab `Drafts`
19. Verifikasi tombol `Search by Scan` tampil pada tab `Drafts`
20. Klik tab `History`
21. Klik `Search` pada toolbar sub-tab `By Transaction`
22. Verifikasi kotak Search memuat placeholder `Search transaction ID, asset, or assignee...` pada sub-tab `By Transaction`
23. Verifikasi tombol `Search by Scan` tidak tampil pada tab `History`
24. Klik sub-tab `By Asset`
25. Klik `Search` pada toolbar sub-tab `By Asset`
26. Verifikasi kotak Search memuat placeholder `Search transaction ID, asset, or assignee...` pada sub-tab `By Asset`

### Pencarian per kelas kolom
27. Klik tab `Transactions`
28. Ganti isi kotak search dengan `Agus Prasetyo {runId}`, tekan Enter
29. Verifikasi tabel memuat tepat 6 baris, yaitu baris untuk Assignee `Budi S`, `Sari D`, `Gudang Pusat {runId}`, `Pusat {runId}`, `Surabaya Selatan {runId}`, dan `Head Office Room {runId}` karena kolom `Requested By` seragam
30. Ganti isi kotak search dengan Transaction ID milik DU-002-9 yang tampil pada baris `Budi S`, tekan Enter
31. Verifikasi baris `Budi S` tampil
32. Ganti isi kotak search dengan `Budi Santoso {runId}`, tekan Enter
33. Verifikasi baris `Budi S` tampil
34. Ganti isi kotak search dengan `Waiting for Approval`, tekan Enter
35. Verifikasi baris `Sari D` tampil
36. Ganti isi kotak search dengan `3`, tekan Enter
37. Verifikasi baris `Surabaya Selatan {runId}` tampil

### Kecocokan substring, huruf besar kecil, dan lintas kolom
38. Ganti isi kotak search dengan `abaya Sel`, tekan Enter
39. Verifikasi baris `Surabaya Selatan {runId}` tampil karena kata kunci cocok di tengah teks
40. Ganti isi kotak search dengan `surabaya selatan {runId}`, tekan Enter
41. Verifikasi baris `Surabaya Selatan {runId}` tampil walau huruf besar dan kecilnya berbeda
42. Ganti isi kotak search dengan `Surabaya`, tekan Enter
43. Verifikasi baris `Gudang Pusat {runId}` tampil karena cocok di kolom `Group` dan baris `Surabaya Selatan {runId}` tampil karena cocok di kolom `Assignee`
44. Ganti isi kotak search dengan `Pusat {runId}`, tekan Enter
45. Verifikasi baris `Pusat {runId}` dan baris `Gudang Pusat {runId}` tampil karena nilai yang satu memuat nilai yang lain
46. Ganti isi kotak search dengan `Head Room {runId}`, tekan Enter
47. Verifikasi baris `Head Office Room {runId}` tampil karena setiap kata kunci `Head`, `Room`, dan `{runId}` ada pada baris itu walau tidak bersebelahan[^drift-1]

### Trigger Enter dan normalisasi spasi
48. Ganti isi kotak search dengan `Budi Santoso {runId}` tanpa menekan Enter
49. Verifikasi tabel masih menampilkan hasil Search sebelumnya, yaitu baris `Head Office Room {runId}`, karena tabel belum berubah sebelum Enter
50. Tekan Enter
51. Verifikasi baris `Budi S` tampil
52. Ganti isi kotak search dengan `Surabaya Selatan {runId}` yang diawali dan diakhiri satu spasi, tekan Enter
53. Verifikasi baris `Surabaya Selatan {runId}` tampil walau kata kunci diawali dan diakhiri spasi
54. Verifikasi kotak Search tetap memuat spasi di awal dan akhir kata kunci yang diketik
55. Ganti isi kotak search dengan `Surabaya  Selatan {runId}` dengan dua spasi di antara `Surabaya` dan `Selatan`, tekan Enter
56. Verifikasi baris `Surabaya Selatan {runId}` tampil karena setiap kata kunci `Surabaya`, `Selatan`, dan `{runId}` ada pada baris itu walau dipisah dua spasi[^drift-1]
57. Ganti isi kotak search dengan `Surabaya Selatan {runId}`, tekan Enter
58. Verifikasi tabel memuat tepat satu baris, yaitu baris `Surabaya Selatan {runId}`
59. Ganti isi kotak search dengan tiga spasi, tekan Enter
60. Verifikasi tabel memuat lebih dari satu baris karena kata kunci yang hanya berisi spasi diperlakukan sebagai kotak search kosong

### Karakter pola dan kolom yang tidak dicari
61. Ganti isi kotak search dengan `100% {runId}`, tekan Enter
62. Verifikasi baris `Budi S` tampil karena `%` dicari sebagai teks
63. Verifikasi baris `Sari D` tidak tampil karena `%` tidak diperlakukan sebagai wildcard
64. Ganti isi kotak search dengan teks Request Date milik DU-002-13 yang tampil pada baris `Surabaya Selatan {runId}`, tekan Enter
65. Verifikasi pesan `No results found` tampil karena nilai tanggal tidak dicari
66. Ganti isi kotak search dengan `{runId} tidakada`, tekan Enter
67. Verifikasi pesan `No results found` tampil

### Kolom tersembunyi tetap dicari
68. Klik header kolom `Actions`
69. Hilangkan centang kolom `Group` pada panel Column Visibility
70. Verifikasi kolom `Group` tidak tampil di tabel
71. Ganti isi kotak search dengan `Branch Surabaya {runId}`, tekan Enter
72. Verifikasi pesan `No results found` tampil karena kolom `Group` yang disembunyikan tidak ikut dicari

### Search mencakup Asset ID, alias, dan kode TAG aset
73. Ganti isi kotak search dengan Asset ID milik aset `Switch Cisco 100% {runId}`, tekan Enter
74. Verifikasi baris `Budi S` tampil karena Asset ID aset ikut dicari
75. Ganti isi kotak search dengan alias aset `Switch Cisco 100% {runId}`, yaitu `Sw-Lobi-A1 {runId}`, tekan Enter
76. Verifikasi baris `Budi S` tampil karena alias aset ikut dicari
77. Ganti isi kotak search dengan kode TAG milik aset `Switch Cisco 100% {runId}`, tekan Enter
78. Verifikasi baris `Budi S` tampil karena kode TAG aset ikut dicari

### Badge angka tab Assigned Assets dan Drafts sesuai jumlah barisnya
79. Klik tab `Assigned Assets`
80. Verifikasi angka pada badge tab `Assigned Assets` sama dengan jumlah total baris yang dilaporkan paginator sub-tab `By Asset`
81. Klik tab `Drafts`
82. Verifikasi angka pada badge tab `Drafts` sama dengan jumlah total baris yang dilaporkan paginator tab `Drafts`

### Hasil Search by Scan mengisi Search dengan Asset ID di tiap tabel
83. Klik tab `Transactions`
84. Ganti isi kotak search dengan `{runId}`, tekan Enter
85. Klik `Search by Scan`
86. Pilih tipe TAG `QR`
87. Scan TAG milik aset `Switch Cisco 100% {runId}`
88. Verifikasi dialog Search by Scan tertutup
89. Verifikasi kotak Search berisi Asset ID milik aset `Switch Cisco 100% {runId}`
90. Verifikasi baris `Budi S` tampil di tab `Transactions`
91. Klik tab `Drafts`
92. Klik `Search by Scan`
93. Pilih tipe TAG `QR`
94. Scan TAG milik aset `Mouse Logitech M331 {runId}`
95. Verifikasi kotak Search berisi Asset ID milik aset `Mouse Logitech M331 {runId}`
96. Verifikasi Draft untuk Assignee `Sari D` tampil di tab `Drafts`
97. Klik tab `Assigned Assets`
98. Klik sub-tab `By Asset`
99. Klik `Search by Scan`
100. Pilih tipe TAG `QR`
101. Scan TAG milik aset `Printer Zebra ZD220 {runId}`
102. Verifikasi kotak Search berisi Asset ID milik aset `Printer Zebra ZD220 {runId}`
103. Verifikasi baris aset `Printer Zebra ZD220 {runId}` tampil di sub-tab `By Asset`
104. Klik sub-tab `By Assignee`
105. Klik `Search by Scan`
106. Pilih tipe TAG `QR`
107. Scan TAG milik aset `Kamera CCTV Hikvision {runId}`
108. Verifikasi kotak Search berisi Asset ID milik aset `Kamera CCTV Hikvision {runId}`
109. Verifikasi baris Assignee `Pusat {runId}` tampil di sub-tab `By Assignee`
110. Klik tab `Transactions`
111. Ganti isi kotak search dengan `Surabaya Selatan {runId}`, tekan Enter
112. Klik tautan Transaction ID pada baris `Surabaya Selatan {runId}`
113. Verifikasi tabel Assets memuat aset `Tablet Samsung Tab A8 {runId}`, `Tablet Samsung Tab A9 {runId}`, dan `Tablet Samsung Tab S9 {runId}`
114. Klik `Search by Scan` pada tabel Assets
115. Pilih tipe TAG `QR`
116. Scan TAG milik aset `Tablet Samsung Tab A8 {runId}`
117. Verifikasi kotak Search tabel Assets berisi Asset ID milik aset `Tablet Samsung Tab A8 {runId}`
118. Verifikasi baris aset `Tablet Samsung Tab A8 {runId}` tampil di tabel Assets
119. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` tidak tampil di tabel Assets

[^drift-1]: Drift foundation vs kontrak komponen. PRD §5 Search: pencocokan mengikuti `prd-conventions.md` §9.1b dan §9.16. foundation `prd-conventions.md` §9.16: kata kunci dicocokkan sebagai substring, bukan per kata, dan query tidak dipecah menjadi beberapa kata. Kontrak `SearchButton#5`: baris cocok bila setiap kata query (dipisah spasi) muncul di nilai baris, urutan bebas dan boleh di kolom berbeda. Diasersi: kontrak, karena foundation meminta mekanik yang tidak bisa terjadi bersama butir `Does` komponen (SB-7).
