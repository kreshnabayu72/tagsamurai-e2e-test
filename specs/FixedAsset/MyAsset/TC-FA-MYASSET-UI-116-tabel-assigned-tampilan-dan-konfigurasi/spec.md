---
id: TC-FA-MYASSET-UI-116-tabel-assigned-tampilan-dan-konfigurasi
title: "Tabel Assigned: format sel, Assigned To, badge Status, konfigurasi toolbar, dan state data"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-15", "T-MYA-04", "§1.2#r7", "§1.2#r45", "§1.2#r85", "§4.1#p2", "§4.4#r50", "§5#r1", "§5#r3", "§5#r9", "§5#r10", "§7.1#r3", "§9.4.2#r59", "EB-TBL-1@tabel-assigned", "EB-FLT-6@tabel-assigned"]
smoke: []
dependsOn: []
trace:
  "FI-15": 7
  "T-MYA-04": [2, 3, 4, 6, 9, 10, 11, 12, 13, 14, 17, 19, 20, 22, 24, 25, 26, 28, 29, 30, 31, 33, 34, 35, 36, 38, 40, 42, 43, 45, 47, 48, 53, 54, 56, 57, 58, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 79, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 110]
  "§1.2#r7": 4
  "§1.2#r45": [19, 20, 22]
  "§1.2#r85": 17
  "§4.1#p2": [57, 58, 59, 60]
  "§4.4#r50": 6
  "§5#r1": [47, 48, 49]
  "§5#r3": 51
  "§5#r9": 4
  "§5#r10": [53, 56]
  "§7.1#r3": [112, 113, 121, 122, 129, 130]
  "§9.4.2#r59": [12, 13]
  "EB-TBL-1@tabel-assigned": [112, 114, 115, 116, 118, 121, 123, 125, 129, 132, 133, 134, 135]
  "EB-FLT-6@tabel-assigned": [74, 140, 141, 145, 146, 147, 148, 149]
coverage:
  web: automated
---

# Tabel Assigned: format sel, Assigned To, badge Status, konfigurasi toolbar, dan state data

## Prerequisites
- Aktor: Budi Santoso, pengguna yang login sebagai Assignee dan PIC Division atas baris yang tampil.
- Layar awal: halaman My Asset, tab Assigned.
- Komponen: Tabel Assigned (T-MYA-04)
- Data:
  - DU-116-1: Baris Assigned Photo `foto-LPT-2026-0021.jpg`, Name `Laptop Dell Latitude 5420 - 21`, Asset ID `LPT-2026-0021`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Waiting for Handover`, Assigned To `Me`, TAG `Non TAG`, Category `Laptop`, Transaction ID `ASG-2026-0071`, Assigned Date kosong, Assigned By kosong.
  - DU-116-2: Baris Assigned Photo `foto-LPT-2026-0022.jpg`, Name `Laptop Dell Latitude 5420 - 22`, Asset ID `LPT-2026-0022`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Waiting for Approval`, Assigned To `Me`, TAG `Non TAG`, Category `Laptop`, Transaction ID `ASG-2026-0073`, Assigned Date kosong, Assigned By kosong, Approved `1`, Required `2`.
  - DU-116-3: Baris Assigned Photo `foto-PRN-2026-0002.jpg`, Name `Printer HP M404 - 2`, Asset ID `PRN-2026-0002`, Brand `HP`, Model/Type `M404`, Group `Branch Surabaya`, Status `Assigned · Reported Damaged`, Assigned To `Finance`, TAG `Non TAG`, Category `Printer`, Transaction ID `ASG-2026-0069`, Assigned Date `06/11/26, 09:20`, Assigned By `Agus P`, Assigned By Full Name `Agus Prasetyo`, Assigned To Tooltip `PIC: Budi Santoso`.
  - DU-116-4: Baris Assigned Photo `foto-LPT-2026-0001.jpg`, Name `Laptop Dell Latitude 5420 - 1`, Asset ID `LPT-2026-0001`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Assigned`, Assigned To `Me`, TAG `Non TAG`, Category `Laptop`, Transaction ID `ASG-2026-0031`, Assigned Date `12/10/26, 10:00`, Assigned By `Rina W`, Assigned By Full Name `Rina Wulandari`.
  - DU-116-5: Baris Assigned Photo `foto-MON-2026-0004.jpg`, Name `Monitor Dell 24" - 4`, Asset ID `MON-2026-0004`, Brand `Dell`, Model/Type `P2422H`, Group `Head Office`, Status `Assigned · Reported Missing`, Assigned To `Me`, TAG `Non TAG`, Category `Monitor`, Transaction ID `ASG-2026-0015`, Assigned Date `20/08/26, 09:30`, Assigned By `Rina W`, Assigned By Full Name `Rina Wulandari`.
  - DU-116-6: Baris Assigned Photo `foto-MON-2026-0005.jpg`, Name `Monitor Dell 24" - 5`, Asset ID `MON-2026-0005`, Brand `Dell`, Model/Type `P2422H`, Group `Head Office`, Status `Assigned · Damaged`, Assigned To `Me`, TAG `Non TAG`, Category `Monitor`, Transaction ID `ASG-2026-0016`, Assigned Date `22/08/26, 11:00`, Assigned By `Rina W`, Assigned By Full Name `Rina Wulandari`.
  - DU-116-7: Baris Assigned Photo kosong, Name `Laptop Dell Latitude 5420 Edisi Khusus Kantor Pengadaan dan Manajemen Vendor Regional Jakarta - 31`, Asset ID `LPT-2026-0031`, Brand kosong, Model/Type kosong, Group `Head Office`, Status `Assigned`, Assigned To `Me`, TAG `Non TAG`, Category `Laptop`, Transaction ID `ASG-2026-0032`, Assigned Date `14/10/26, 10:00`, Assigned By `Rina W`, Assigned By Full Name `Rina Wulandari`.
  - DU-116-8: Baris Assigned Photo `foto-MIC-2026-0007.jpg`, Name `Meeting Mic Set - 7`, Asset ID `MIC-2026-0007`, Brand `Dell Technologies Indonesia Authorized Distributor`, Model/Type `Latitude 5420 Rugged Extreme Edition`, Group `Pengadaan`, Status `Assigned`, Assigned To `Me`, TAG `QR Code` dan `RFID`, Category `Audio Visual`, Transaction ID `ASG-2026-0033`, Assigned Date `16/10/26, 10:00`, Assigned By `Rina W`, Assigned By Full Name `Rina Wulandari`, hierarki Group `Head Office` lalu `Pengadaan`, hierarki Category `Peralatan Kantor` lalu `Audio Visual`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K1: tabel Assigned memuat DU-116-1 sampai DU-116-6, dengan konfigurasi kolom bawaan.
  - K2: tabel Assigned memuat DU-116-7 dan DU-116-8, dengan kolom TAG dan Category ditampilkan.
  - K3: tabel Assigned belum memiliki satu pun baris, dan tidak ada Search maupun Filter aktif.
  - K4: tabel Assigned memuat DU-116-4; respons untuk Search `Kamera Drone DJI` dan untuk Filter Status `Waiting for Approval` tidak memuat baris.
  - K5: memuat tabel Assigned gagal karena error server.
  - K6: tabel Assigned memuat DU-116-4 dan DU-116-1; respons untuk Filter Status `Assigned` hanya memuat DU-116-4.

## Test Steps

### Identitas aset, Name tanpa tautan, dan kolom yang tidak ada pada tabel Assigned
1. Tampilkan Tabel Assigned dengan kondisi K1
2. Verifikasi baris `Laptop Dell Latitude 5420 - 1` menampilkan Name `Laptop Dell Latitude 5420 - 1` dan Asset ID `LPT-2026-0001`
3. Verifikasi baris yang sama menampilkan foto utama aset pada kolom Photo
4. Verifikasi header kolom `Photo`, `Name`, `Asset ID`, `Brand`, dan `Model/Type` tampil sebagai blok identitas aset
5. Klik Name `Laptop Dell Latitude 5420 - 1`
6. Verifikasi Name bukan tautan: klik tidak membuka dialog dan tidak berpindah halaman
7. Verifikasi kotak centang baris dan bulk action tidak tampil pada tabel

### Badge Status dan badge tambahan laporan
8. Tampilkan Tabel Assigned dengan kondisi K1
9. Verifikasi baris `Laptop Dell Latitude 5420 - 21` menampilkan Status `Waiting for Handover`
10. Verifikasi baris `Laptop Dell Latitude 5420 - 22` menampilkan Status `Waiting for Approval`
11. Verifikasi baris `Laptop Dell Latitude 5420 - 1` menampilkan Status `Assigned`
12. Verifikasi baris `Printer HP M404 - 2` menampilkan Status `Assigned` dengan badge tambahan `Reported Damaged`
13. Verifikasi baris `Monitor Dell 24" - 5` menampilkan Status `Assigned` dengan badge tambahan `Damaged`
14. Verifikasi baris `Monitor Dell 24" - 4` menampilkan Status `Assigned` dengan badge tambahan `Reported Missing`

### Tooltip progres approval pada badge Waiting for Approval
15. Tampilkan Tabel Assigned dengan kondisi K1
16. Arahkan kursor ke badge `Waiting for Approval` pada baris `Laptop Dell Latitude 5420 - 22`
17. Verifikasi tooltip `Approval: 1 of 2 approved` tampil

### Assigned To: Me untuk aset pribadi dan nama Division
18. Tampilkan Tabel Assigned dengan kondisi K1
19. Verifikasi baris `Laptop Dell Latitude 5420 - 1` menampilkan Assigned To `Me`
20. Verifikasi baris `Printer HP M404 - 2` menampilkan Assigned To `Finance`
21. Arahkan kursor ke Assigned To `Finance`
22. Verifikasi tooltip `PIC: Budi Santoso` tampil

### Format Transaction ID, Assigned Date, dan Assigned By serta nilai kosongnya
23. Tampilkan Tabel Assigned dengan kondisi K1
24. Verifikasi baris `Laptop Dell Latitude 5420 - 1` menampilkan Transaction ID `ASG-2026-0031`
25. Verifikasi baris yang sama menampilkan Assigned Date `12/10/26, 10:00`
26. Verifikasi baris yang sama menampilkan Assigned By `Rina W`
27. Arahkan kursor ke Assigned By `Rina W`
28. Verifikasi tooltip nama lengkap `Rina Wulandari` tampil
29. Verifikasi baris `Laptop Dell Latitude 5420 - 21` menampilkan Assigned Date `—`
30. Verifikasi baris yang sama menampilkan Assigned By `—`
31. Verifikasi baris `Printer HP M404 - 2` menampilkan Assigned Date `06/11/26, 09:20` dan Assigned By `Agus P`

### Teks panjang, nilai kosong, dan kolom curated TAG dan Category
32. Tampilkan Tabel Assigned dengan kondisi K2
33. Verifikasi Name `Laptop Dell Latitude 5420 Edisi Khusus Kantor Pengadaan dan Manajemen Vendor Regional Jakarta - 31` tampil utuh tanpa dipotong
34. Verifikasi baris itu menampilkan placeholder gambar standar pada kolom Photo
35. Verifikasi baris itu menampilkan Brand `—` dan Model/Type `—`
36. Verifikasi baris itu menampilkan TAG `—` karena aset `Non TAG`
37. Arahkan kursor ke badge Brand `Dell Technologies Indonesia Authorized Distributor`
38. Verifikasi tooltip nama Brand penuh `Dell Technologies Indonesia Authorized Distributor` tampil
39. Arahkan kursor ke badge Model/Type `Latitude 5420 Rugged Extreme Edition`
40. Verifikasi tooltip nama Model penuh `Latitude 5420 Rugged Extreme Edition` tampil
41. Arahkan kursor ke badge Group `Pengadaan`
42. Verifikasi tooltip memuat hierarki lengkap Group, yaitu `Head Office` dan `Pengadaan`
43. Verifikasi sel TAG baris `Meeting Mic Set - 7` menampilkan dua ikon, satu untuk setiap TAG Type `QR Code` dan `RFID`
44. Arahkan kursor ke badge Category `Audio Visual`
45. Verifikasi tooltip memuat hierarki lengkap Category, yaitu `Peralatan Kantor` dan `Audio Visual`

### Isi dan urutan toolbar
46. Tampilkan Tabel Assigned dengan kondisi K1
47. Verifikasi toolbar memuat ikon Search, ikon Filter, dan ikon Download
48. Verifikasi urutan ikon toolbar dari kiri ke kanan adalah Search, Filter, Download
49. Verifikasi tombol `Borrow an Asset` tidak tampil di toolbar
50. Klik ikon Search
51. Verifikasi kotak Search menampilkan placeholder `Search asset name, asset ID...`

### Kolom tampil awal, urutan kolom, dan status Hideable atau Curated
52. Tampilkan Tabel Assigned dengan kondisi K1
53. Verifikasi header kolom tampil berurutan dari kiri ke kanan: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Assigned To`, `Transaction ID`, `Assigned Date`, `Assigned By`
54. Verifikasi header kolom `TAG`, `Category` tidak tampil
55. Klik header kolom Actions `⋯`
56. Verifikasi panel Column Visibility memuat daftar kolom berurutan: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Assigned To`, `TAG`, `Category`, `Transaction ID`, `Assigned Date`, `Assigned By`
57. Verifikasi kotak centang kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Assigned To`, `Transaction ID`, `Assigned Date`, `Assigned By` tercentang (Hideable)
58. Verifikasi kotak centang kolom `TAG`, `Category` tidak tercentang (Curated)
59. Verifikasi semua kotak centang aktif sehingga tidak ada kolom yang terkunci tampil
60. Verifikasi daftar tidak memuat baris untuk kolom Checkbox maupun kolom Actions
61. Tutup panel Column Visibility dengan menekan `Escape`

### Field Filter tiap kolom: label dan placeholder
62. Tampilkan Tabel Assigned dengan kondisi K1
63. Klik ikon Filter
64. Verifikasi Filter Panel memuat field `Asset Name` dengan placeholder `All asset names`
65. Verifikasi Filter Panel memuat field `Brand` dengan placeholder `All brands`
66. Verifikasi Filter Panel memuat field `Model/Type` dengan placeholder `All models`
67. Verifikasi Filter Panel memuat field `Group` dengan placeholder `All groups`
68. Verifikasi Filter Panel memuat field `Status` dengan placeholder `All statuses`
69. Verifikasi Filter Panel memuat field `Assigned To` dengan placeholder `All assignees`
70. Verifikasi Filter Panel memuat field `TAG` dengan placeholder `All TAGs`
71. Verifikasi Filter Panel memuat field `Category` dengan placeholder `All categories`
72. Verifikasi Filter Panel memuat field `Assigned Date` dengan placeholder `Select date`
73. Verifikasi Filter Panel memuat field `Assigned By` dengan placeholder `All users`
74. Verifikasi Filter Panel memuat field untuk kolom TAG dan Category walaupun kedua kolom itu tidak tampil di tabel
75. Verifikasi Filter Panel tidak memuat field untuk kolom `Photo`, `Asset ID`, dan `Transaction ID`

### Tipe field Filter: multi-select searchable dan date range picker
76. Tampilkan Tabel Assigned dengan kondisi K1
77. Klik ikon Filter
78. Klik field `Status`
79. Verifikasi daftar opsi field `Status` memiliki kotak pencarian
80. Pilih `Assigned` dan `Waiting for Approval` pada field `Status`
81. Verifikasi field `Status` menampilkan `Assigned` dan `Waiting for Approval` sebagai pilihan terpilih sekaligus
82. Tutup daftar opsi field `Status` dengan menekan `Escape`
83. Klik field `Asset Name`
84. Verifikasi daftar opsi field `Asset Name` memiliki kotak pencarian
85. Tutup daftar opsi field `Asset Name` dengan menekan `Escape`
86. Klik field `Brand`
87. Verifikasi daftar opsi field `Brand` memiliki kotak pencarian
88. Tutup daftar opsi field `Brand` dengan menekan `Escape`
89. Klik field `Model/Type`
90. Verifikasi daftar opsi field `Model/Type` memiliki kotak pencarian
91. Tutup daftar opsi field `Model/Type` dengan menekan `Escape`
92. Klik field `Group`
93. Verifikasi daftar opsi field `Group` memiliki kotak pencarian
94. Tutup daftar opsi field `Group` dengan menekan `Escape`
95. Klik field `Assigned To`
96. Verifikasi daftar opsi field `Assigned To` memiliki kotak pencarian
97. Tutup daftar opsi field `Assigned To` dengan menekan `Escape`
98. Klik field `TAG`
99. Verifikasi daftar opsi field `TAG` memiliki kotak pencarian
100. Tutup daftar opsi field `TAG` dengan menekan `Escape`
101. Klik field `Category`
102. Verifikasi daftar opsi field `Category` memiliki kotak pencarian
103. Tutup daftar opsi field `Category` dengan menekan `Escape`
104. Klik field `Assigned By`
105. Verifikasi daftar opsi field `Assigned By` memiliki kotak pencarian
106. Tutup daftar opsi field `Assigned By` dengan menekan `Escape`
107. Klik field `Assigned Date`
108. Verifikasi panel pemilih tanggal terbuka untuk field `Assigned Date`
109. Pilih hari pertama yang tampil sebagai awal dan hari ketiga yang tampil sebagai akhir
110. Verifikasi field `Assigned Date` menampilkan satu rentang tanggal dari awal sampai akhir yang dipilih

### Empty state tab Assigned belum ada data
111. Tampilkan Tabel Assigned dengan kondisi K3
112. Verifikasi `No assets are assigned to you` tampil
113. Verifikasi `Assets assigned to you will appear here.` tampil
114. Verifikasi `No results found` tidak tampil
115. Verifikasi `Unable to load this data.` tidak tampil
116. Verifikasi empty state tidak memuat tombol aksi

### Empty state tab Assigned akibat Search dan Filter
117. Tampilkan Tabel Assigned dengan kondisi K4
118. Verifikasi baris `Laptop Dell Latitude 5420 - 1` tampil
119. Klik ikon Search
120. Ketik Search `Kamera Drone DJI`, tekan Enter
121. Verifikasi `No results found` tampil
122. Verifikasi `Try adjusting your search or filter.` tampil
123. Verifikasi `No assets are assigned to you` tidak tampil
124. Klik `(←)` pada kotak Search
125. Verifikasi baris `Laptop Dell Latitude 5420 - 1` tampil kembali
126. Klik ikon Filter
127. Pilih `Waiting for Approval` pada field `Status`
128. Klik `[Apply]`
129. Verifikasi `No results found` tampil
130. Verifikasi `Try adjusting your search or filter.` tampil

### Gagal muat tab Assigned
131. Tampilkan Tabel Assigned dengan kondisi K5
132. Verifikasi `Unable to load this data.` tampil
133. Verifikasi tombol `[Try Again]` tampil
134. Verifikasi `No assets are assigned to you` tidak tampil
135. Verifikasi `No results found` tidak tampil

### Menyembunyikan kolom tidak menghapus field Filter dan tidak membatalkan filter ter-Apply
136. Tampilkan Tabel Assigned dengan kondisi K6
137. Klik ikon Filter
138. Pilih `Assigned` pada field `Status`
139. Klik `[Apply]`
140. Verifikasi baris `Laptop Dell Latitude 5420 - 1` tampil
141. Verifikasi ikon Filter menampilkan titik penanda filter ter-Apply
142. Klik header kolom Actions `⋯`
143. Hilangkan centang kolom `Status` pada panel Column Visibility
144. Tutup panel Column Visibility dengan menekan `Escape`
145. Verifikasi header kolom `Name` tampil
146. Verifikasi header kolom `Status` tidak tampil
147. Verifikasi Filter Panel masih memuat field `Status` dengan pilihan `Assigned`
148. Verifikasi ikon Filter masih menampilkan titik penanda filter ter-Apply
149. Verifikasi baris `Laptop Dell Latitude 5420 - 1` tetap tampil
