---
id: TC-FA-ASTL-UI-054-tabel-all-assets-tampilan-sel
title: "Tampilan sel dan kolom tabel All Assets"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-04g", "ASTL-LOGIC-09d", "ASTL-LOGIC-09e", "ASTL-LOGIC-10i", "ASTL-LOGIC-11c", "ASTL-LOGIC-11f", "ASTL-LOGIC-11g", "ASTL-LOGIC-11h", "ASTL-LOGIC-11i", "ASTL-LOGIC-11j", "ASTL-LOGIC-11k", "ASTL-LOGIC-12l", "ASTL-LOGIC-12o", "ASTL-LOGIC-12p", "ASTL-LOGIC-12q", "S-09", "S-20", "S-21", "S-22", "S-23", "S-24", "S-28", "S-38", "EC-14", "EC-25", "FLD-01", "FLD-02", "FLD-03", "FLD-04", "FLD-05", "FLD-06", "FLD-07", "FLD-08", "FLD-09", "FLD-10", "FLD-11", "FLD-12", "FLD-13", "FLD-14", "FLD-15", "FLD-16", "FLD-17", "FLD-18", "FLD-19", "FLD-20", "FLD-21", "FLD-22", "FLD-23", "FLD-24", "FLD-25", "FLD-26", "§9.4.3#p2", "§4.1a#p1", "§4.5#b1", "§4.5#b2", "§4.5#b3", "§5#r1", "§7.1#b2", "EB-TBL-2@kolom-division", "EB-TBL-2@kolom-alias-name", "EB-TBL-2@kolom-last-scanned", "EB-TBL-2@kolom-tag", "EB-TBL-3@kolom-labels", "EB-TBL-4@kolom-modified-by", "EB-TBL-8@tabel-all-assets", "EB-XM-1"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-04g": [55, 57, 61, 63]
  "ASTL-LOGIC-09d": 31
  "ASTL-LOGIC-09e": 33
  "ASTL-LOGIC-10i": [89, 91]
  "ASTL-LOGIC-11c": 104
  "ASTL-LOGIC-11f": [105, 106]
  "ASTL-LOGIC-11g": 107
  "ASTL-LOGIC-11h": [107, 108, 109]
  "ASTL-LOGIC-11i": [107, 148, 149]
  "ASTL-LOGIC-11j": [110, 111]
  "ASTL-LOGIC-11k": [112, 113]
  "ASTL-LOGIC-12l": [95, 97, 136, 139]
  "ASTL-LOGIC-12o": [80, 81]
  "ASTL-LOGIC-12p": [99, 136, 139]
  "ASTL-LOGIC-12q": 77
  "S-09": [72, 84, 85, 86, 113]
  "S-20": 106
  "S-21": 107
  "S-22": [91, 93]
  "S-23": 95
  "S-24": [97, 136, 139]
  "S-28": [55, 57]
  "S-38": 102
  "EC-14": [71, 97, 136, 137, 139]
  "EC-25": [91, 95]
  "FLD-01": [23, 24, 25]
  "FLD-02": 26
  "FLD-03": [27, 28]
  "FLD-04": 29
  "FLD-05": [31, 32]
  "FLD-06": [35, 37, 124, 125]
  "FLD-07": [38, 39, 127, 128]
  "FLD-08": 40
  "FLD-09": [41, 43]
  "FLD-10": [44, 46]
  "FLD-11": [47, 48]
  "FLD-12": [50, 53, 59, 130]
  "FLD-13": [21, 65]
  "FLD-14": 66
  "FLD-15": [67, 68]
  "FLD-16": [70, 71, 72]
  "FLD-17": [73, 74, 75]
  "FLD-18": [77, 78]
  "FLD-19": [77, 78, 132]
  "FLD-20": [82, 85]
  "FLD-21": [83, 86]
  "FLD-22": 104
  "FLD-23": [115, 116, 133, 134]
  "FLD-24": 117
  "FLD-25": 120
  "FLD-26": 87
  "§9.4.3#p2": [33, 122]
  "§4.1a#p1": [2, 13, 14, 154]
  "§4.5#b1": [18, 19, 156, 158, 160]
  "§4.5#b2": [20, 21]
  "§4.5#b3": [5, 7, 9, 11, 162, 163, 165, 166, 167]
  "§5#r1": [2, 3]
  "§7.1#b2": 39
  "EB-TBL-2@kolom-division": 48
  "EB-TBL-2@kolom-alias-name": 28
  "EB-TBL-2@kolom-last-scanned": 68
  "EB-TBL-2@kolom-tag": 32
  "EB-TBL-3@kolom-labels": [50, 51, 52, 53]
  "EB-TBL-4@kolom-modified-by": [117, 119]
  "EB-TBL-8@tabel-all-assets": 121
  "EB-XM-1": [66, 82, 120, 141, 142, 143, 146, 151]
anchor: [59]
coverage:
  web: automated
---
# Tampilan sel dan kolom tabel All Assets

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Tabel All Assets
- Data:
  - DU-054-1: Aset dengan seluruh kolom terisi: Photo `foto utama terpasang`, Name `Laptop Dell - 1`, Alias Name `Laptop Direksi`, Asset ID `AST-0101`, TAG `NFC, QR`, Brand `Dell`, Model / Type `Latitude 5440`, Measurement `Unit`, Category `Laptop`, Category hierarki `Elektronik > Laptop`, Group `GA`, Group hierarki `Kantor Pusat > GA`, Division `Finance`, Labels `Aset IT (bawaan), Audit 2026, Garansi (bawaan), Prioritas`, Status `Available`, Register Date `10/01/26`, Last Scanned `02/06/26`, Asset Class `Peralatan Kantor`, Tax Depreciation Class `Kelompok 1`, Asset Value (Commercial) `Rp 12.500.000,00`, Asset Value (Fiscal) `Rp 11.000.000,00`, Purchase Date `05/01/26`, Purchase Cost `Rp 15.000.000,00`, Reference Price `IDR 14.500.000,00`, Warranty Expiry `—`, Nomor Seri `SN-4471`, Modified By `John L (nama lengkap John Lennon)`, Last Updated `12/06/26, 09:42`.
  - DU-054-2: Aset belum dilengkapi (Not Paired Yet, tanpa data pembelian): Photo `tanpa foto`, Name `Printer Laser - 1`, Alias Name `kosong`, Asset ID `AST-0031`, TAG `kosong`, Brand `Epson`, Model / Type `No Model`, Measurement `Unit`, Category `Printer`, Group `GA`, Division `kosong`, Labels `kosong`, Status `Not Paired Yet`, Register Date `11/01/26`, Last Scanned `kosong`, Asset Class `kosong`, Tax Depreciation Class `kosong`, Asset Value (Commercial) `Pending`, Asset Value (Fiscal) `Pending`, Purchase Date `Pending`, Purchase Cost `Pending`, Warranty Expiry `—`, Nomor Seri `kosong`, Modified By `Budi`, Last Updated `13/06/26, 10:15`.
  - DU-054-3: Aset dengan empat garansi pada hari ini 15/06/26: Name `Server Rack - 1`, Asset ID `AST-0202`, Status `Available`, Garansi `Garansi Unit 14/06/26; Garansi Baterai 15/06/26; Garansi Panel 15/07/26; Garansi Layanan 16/07/26`, Hover diharapkan `Garansi Unit — 14/06/26 | Garansi Baterai — 15/06/26 | Garansi Panel — 15/07/26 | Garansi Layanan — 16/07/26`.
  - DU-054-4: Aset yang gerbang nilainya tidak berhak dibaca aktor: Name `Kursi Kerja - 1`, Asset ID `AST-0072`, Status `Available`, Asset Class `No access`, Tax Depreciation Class `No access`, Asset Value (Commercial) `No access`, Purchase Date `No access`, Purchase Cost `No access`, Warranty Expiry `No access`.
  - DU-054-5: Aset bernama berisi markup: Name `<b>Meja Rapat</b> - 1`, Asset ID `AST-0303`, Status `Available`.
  - DU-054-6: Aset tanpa Asset Class dengan Purchase Cost terisi: Name `Mesin Fotokopi - 1`, Asset ID `AST-0404`, Status `Available`, Labels `Audit 2026, Prioritas`, Asset Class `kosong`, Tax Depreciation Class `kosong`, Asset Value (Commercial) `Pending`, Purchase Cost `Rp 8.000.000,00`, Reference Price `IDR 7.500.000,00`, Tooltip Purchase Cost diharapkan `Reference price: IDR 7.500.000,00`.
  - DU-054-7: Aset berpredikat Asset Value tidak terbaca: Name `Proyektor - 1`, Asset ID `AST-0505`, Status `Available`, Labels `Prioritas`, Asset Class `Peralatan Kantor`, Purchase Cost `Rp 6.000.000,00`, Asset Value (Commercial) `Pending`.
  - DU-054-8: Aset dengan nama panjang pada Group dan Category: Name `Sensor Gudang - 1`, Asset ID `AST-0606`, Status `Available`, Group `Jakarta Selatan Distribution Center`, Group hierarki `Region Jawa > Jakarta Selatan Distribution Center`, Category `Environmental Monitoring`, Category hierarki `Sensors > Environmental Monitoring`.
  - DU-054-9: Aset tanpa Brand dan tanpa Model / Type: Name `Kabel Roll - 1`, Asset ID `AST-0707`, Status `Available`, Brand `kosong`, Model / Type `kosong`.
  - DU-054-10: Aset tanpa Asset Class dengan Purchase Cost terisi dan predikat Asset Value tidak terbaca (periode Posted terakhir): Name `Scanner - 1`, Asset ID `AST-0808`, Status `Available`, Asset Class `kosong`, Purchase Cost `Rp 4.000.000,00`, Asset Value (Commercial) `Pending`.
  - DU-054-11: Aset Disposed tanpa Asset Class dengan Purchase Cost terisi, nilai Disposal belum Posted terbaca, dan jurnal pelepasan sudah Posted: Name `Genset - 1`, Asset ID `AST-0909`, Status `Disposed`, Asset Class `kosong`, Purchase Cost `Rp 9.000.000,00`, Asset Value (Commercial) `Pending`.
  - DU-054-12: Aset yang Asset Name-nya di luar Scope custom field Nomor Seri (field hanya berlaku pada Asset Name `Laptop`): Name `Meja Kerja - 1`, Asset ID `AST-1010`, Status `Available`, Nomor Seri `kosong`.
- Kondisi:
  - K1: tabel memuat DU-054-1 sampai DU-054-12, seluruh kolom Curated tampil, Date Format bernilai `dd/MM/yy`, Time Format bernilai `24h`, dan tanggal hari ini menurut Time Zone General Settings adalah `15/06/26`.
  - K2: seperti K1, tetapi Date Format bernilai `dd MMM yy` dan Time Format bernilai `12h`; tampilan diharapkan untuk DU-054-1: Register Date `10 Jan 26`, Purchase Date `05 Jan 26`, Last Updated `12 Jun 26, 09:42 AM`.
  - K3: seperti K1, tetapi Time Zone General Settings adalah `Asia/Jakarta` (UTC+7) dan waktu sistem `14/06/26, 16:00` UTC sehingga hari ini menurut Time Zone adalah `14/06/26`, dan Last Updated DU-054-1 tersimpan `12/06/26, 02:42` UTC.
  - K4: seperti K3, tetapi Time Zone General Settings adalah `Asia/Jayapura` (UTC+9) sehingga hari ini menurut Time Zone adalah `15/06/26`, dan Last Updated DU-054-1 tampil `12/06/26, 11:42`.
  - K5: seperti K1, dengan lebar layar lebar.
  - K6: seperti K1, dengan lebar layar menengah.
  - K7: seperti K1, dengan lebar layar sempit.

## Test Steps

### Toolbar dan tooltip ikon
1. Tampilkan Tabel All Assets dengan kondisi K1
2. Verifikasi toolbar memuat Search, Filter, Download, Changelog, lalu `Print Label` berurutan dari kiri ke kanan
3. Verifikasi toolbar tidak memuat tombol Scan maupun tombol Register
4. Arahkan pointer ke ikon Search
5. Verifikasi tooltip `Search` tampil
6. Arahkan pointer ke ikon Filter
7. Verifikasi tooltip `Filter` tampil
8. Arahkan pointer ke ikon Download
9. Verifikasi tooltip `Download` tampil
10. Arahkan pointer ke ikon Changelog
11. Verifikasi tooltip `Changelog` tampil
12. Klik ikon Search
13. Verifikasi kotak Search berplaceholder `Search asset name, asset ID...`
14. Verifikasi Search berada di sisi kanan toolbar
15. Klik `(←)` pada kotak Search

### Gulir horizontal dan badge status
16. Tampilkan Tabel All Assets dengan kondisi K1
17. Gulir tabel ke kanan sampai kolom Last Updated terlihat
18. Verifikasi tabel menggulir horizontal
19. Verifikasi kolom Checkbox dan kolom Actions tetap terlihat
20. Verifikasi badge status baris `Laptop Dell - 1` membawa teks `Available`
21. Verifikasi badge status baris `Printer Laser - 1` membawa teks `Not Paired Yet`

### Kolom Photo, Name, Alias Name, dan Asset ID
22. Tampilkan Tabel All Assets dengan kondisi K1
23. Verifikasi baris `Laptop Dell - 1` menampilkan foto utama aset pada kolom Photo
24. Verifikasi baris `Printer Laser - 1` menampilkan gambar placeholder generik pada kolom Photo
25. Verifikasi kolom Photo tidak memiliki ikon sort
26. Verifikasi baris `Laptop Dell - 1` menampilkan nama `Laptop Dell - 1` sebagai tautan pada kolom Name
27. Verifikasi baris `Laptop Dell - 1` menampilkan `Laptop Direksi` pada kolom Alias Name
28. Verifikasi baris `Printer Laser - 1` menampilkan `—` pada kolom Alias Name
29. Verifikasi baris `Laptop Dell - 1` menampilkan `AST-0101` pada kolom Asset ID

### Kolom TAG dan Tag Code
30. Tampilkan Tabel All Assets dengan kondisi K1
31. Verifikasi baris `Laptop Dell - 1` menampilkan ikon `NFC` dan `QR` pada kolom TAG
32. Verifikasi baris `Printer Laser - 1` menampilkan `—` pada kolom TAG
33. Verifikasi tabel tidak memiliki kolom Tag Code

### Kolom Brand, Model / Type, Measurement, Category, Group, dan Division
34. Tampilkan Tabel All Assets dengan kondisi K1
35. Verifikasi baris `Laptop Dell - 1` menampilkan badge `Dell` pada kolom Brand
36. Arahkan pointer ke badge `Dell` baris `Laptop Dell - 1`
37. Verifikasi tooltip `Dell` tampil
38. Verifikasi baris `Laptop Dell - 1` menampilkan badge `Latitude 5440` pada kolom Model / Type
39. Verifikasi baris `Printer Laser - 1` menampilkan badge `No Model` pada kolom Model / Type
40. Verifikasi baris `Laptop Dell - 1` menampilkan `Unit` pada kolom Measurement
41. Verifikasi baris `Sensor Gudang - 1` menampilkan badge `Environmental Monitoring` pada kolom Category
42. Arahkan pointer ke badge `Environmental Monitoring` baris `Sensor Gudang - 1`
43. Verifikasi tooltip `Sensors > Environmental Monitoring` tampil
44. Verifikasi baris `Sensor Gudang - 1` menampilkan badge `Jakarta Sela..ution Center` pada kolom Group
45. Arahkan pointer ke badge `Jakarta Sela..ution Center`
46. Verifikasi tooltip `Region Jawa > Jakarta Selatan Distribution Center` tampil
47. Verifikasi baris `Laptop Dell - 1` menampilkan `Finance` pada kolom Division
48. Verifikasi baris `Printer Laser - 1` menampilkan `—` pada kolom Division

### Kolom Labels dan tooltip label bawaan
49. Tampilkan Tabel All Assets dengan kondisi K1
50. Verifikasi baris `Printer Laser - 1` menampilkan `—` pada kolom Labels
51. Verifikasi baris `Proyektor - 1` menampilkan satu badge `Prioritas` pada kolom Labels
52. Verifikasi baris `Mesin Fotokopi - 1` menampilkan dua badge `Audit 2026` dan `Prioritas` tanpa chip `+N more`
53. Verifikasi baris `Laptop Dell - 1` menampilkan badge `Aset IT` lalu `Audit 2026`, diikuti chip `+2 more`
54. Arahkan pointer ke badge `Aset IT` baris `Laptop Dell - 1`
55. Verifikasi tooltip `Default label from the Asset Name template. It cannot be removed here.` tampil
56. Arahkan pointer ke badge `Audit 2026` baris `Laptop Dell - 1`
57. Verifikasi tidak ada tooltip `Default label from the Asset Name template. It cannot be removed here.` pada badge `Audit 2026`
58. Klik chip `+2 more` baris `Laptop Dell - 1`
59. Verifikasi popover memuat seluruh label baris `Laptop Dell - 1`: `Aset IT`, `Audit 2026`, `Garansi`, dan `Prioritas`
60. Arahkan pointer ke label `Garansi` di popover
61. Verifikasi tooltip `Default label from the Asset Name template. It cannot be removed here.` tampil pada label `Garansi`
62. Arahkan pointer ke label `Prioritas` di popover
63. Verifikasi tidak ada tooltip `Default label from the Asset Name template. It cannot be removed here.` pada label `Prioritas`

### Kolom Status, Register Date, dan Last Scanned
64. Tampilkan Tabel All Assets dengan kondisi K1
65. Verifikasi baris `Laptop Dell - 1` menampilkan badge status `Available`
66. Verifikasi baris `Laptop Dell - 1` menampilkan `10/01/26` pada kolom Register Date
67. Verifikasi baris `Laptop Dell - 1` menampilkan `02/06/26` pada kolom Last Scanned
68. Verifikasi baris `Printer Laser - 1` menampilkan `—` pada kolom Last Scanned

### Kolom kelas aset dan kelas penyusutan pajak
69. Tampilkan Tabel All Assets dengan kondisi K1
70. Verifikasi baris `Laptop Dell - 1` menampilkan `Peralatan Kantor` pada kolom kelas aset
71. Verifikasi baris `Mesin Fotokopi - 1` menampilkan `—` pada kolom kelas aset
72. Verifikasi baris `Kursi Kerja - 1` menampilkan `No access` pada kolom kelas aset
73. Verifikasi baris `Laptop Dell - 1` menampilkan `Kelompok 1` pada kolom kelas penyusutan pajak
74. Verifikasi baris `Mesin Fotokopi - 1` menampilkan `—` pada kolom kelas penyusutan pajak
75. Verifikasi baris `Kursi Kerja - 1` menampilkan `No access` pada kolom kelas penyusutan pajak

### Kolom Asset Value, Purchase Date, dan Purchase Cost
76. Tampilkan Tabel All Assets dengan kondisi K1
77. Verifikasi baris `Laptop Dell - 1` menampilkan `Rp 12.500.000,00` pada kolom Asset Value (Commercial)
78. Verifikasi baris `Laptop Dell - 1` menampilkan `Rp 11.000.000,00` pada kolom Asset Value (Fiscal)
79. Arahkan pointer ke nilai `Rp 12.500.000,00`
80. Verifikasi sel bernilai tidak memiliki tooltip
81. Verifikasi tabel tidak memiliki kolom metode penyusutan, masa manfaat, maupun periode
82. Verifikasi baris `Laptop Dell - 1` menampilkan `05/01/26` pada kolom Purchase Date
83. Verifikasi baris `Laptop Dell - 1` menampilkan `Rp 15.000.000,00` pada kolom Purchase Cost
84. Verifikasi baris `Kursi Kerja - 1` menampilkan `No access` pada kolom Asset Value (Commercial)
85. Verifikasi baris `Kursi Kerja - 1` menampilkan `No access` pada kolom Purchase Date
86. Verifikasi baris `Kursi Kerja - 1` menampilkan `No access` pada kolom Purchase Cost
87. Verifikasi tabel tidak memiliki kolom Purchase Status

### Sel Pending dan tooltip alasannya
88. Tampilkan Tabel All Assets dengan kondisi K1
89. Verifikasi baris `Printer Laser - 1` menampilkan `Pending` pada kolom Purchase Date
90. Arahkan pointer ke sel `Pending` Purchase Date baris `Printer Laser - 1`
91. Verifikasi tooltip `Purchase data has not been set.` tampil
92. Arahkan pointer ke sel `Pending` Purchase Cost baris `Printer Laser - 1`
93. Verifikasi tooltip `Purchase data has not been set.` tampil pada Purchase Cost
94. Arahkan pointer ke sel `Pending` Asset Value baris `Printer Laser - 1`
95. Verifikasi tooltip `Purchase cost has not been set.` tampil walau kelas aset juga belum ada
96. Arahkan pointer ke sel `Pending` Asset Value baris `Mesin Fotokopi - 1`
97. Verifikasi tooltip `Asset class has not been set.` tampil
98. Arahkan pointer ke sel `Pending` Asset Value baris `Proyektor - 1`
99. Verifikasi sel `Pending` baris `Proyektor - 1` tidak memiliki tooltip

### Tooltip Reference Price dan penanda garansi
100. Tampilkan Tabel All Assets dengan kondisi K1
101. Arahkan pointer ke nilai Purchase Cost baris `Mesin Fotokopi - 1`
102. Verifikasi tooltip `Reference price: IDR 7.500.000,00` tampil
103. Arahkan pointer ke sel Warranty Expiry baris `Server Rack - 1`
104. Verifikasi hover memuat empat garansi `Garansi Unit — 14/06/26`, `Garansi Baterai — 15/06/26`, `Garansi Panel — 15/07/26`, dan `Garansi Layanan — 16/07/26` beserta penandanya masing-masing
105. Verifikasi garansi `Garansi Unit — 14/06/26` berwarna danger
106. Verifikasi garansi `Garansi Unit — 14/06/26` bertooltip `Warranty expired`
107. Verifikasi garansi `Garansi Baterai — 15/06/26` berwarna warning dengan tooltip `Warranty expires soon` dan masih berlaku pada tanggal habisnya
108. Verifikasi garansi `Garansi Panel — 15/07/26` berwarna warning dengan tooltip `Warranty expires soon`
109. Verifikasi garansi `Garansi Layanan — 16/07/26` tidak berwarna danger maupun warning dan tanpa tooltip penanda
110. Verifikasi setiap tanggal garansi tampil penuh
111. Verifikasi warna garansi disertai tooltip penandanya sehingga warna bukan satu-satunya penanda
112. Verifikasi baris `Laptop Dell - 1` menampilkan `—` pada kolom Warranty Expiry tanpa warna
113. Verifikasi baris `Kursi Kerja - 1` menampilkan `No access` pada kolom Warranty Expiry tanpa warna

### Custom field, Modified By, Last Updated, dan teks markup
114. Tampilkan Tabel All Assets dengan kondisi K1
115. Verifikasi baris `Laptop Dell - 1` menampilkan `SN-4471` pada kolom Nomor Seri
116. Verifikasi baris `Printer Laser - 1` menampilkan `—` pada kolom Nomor Seri
117. Verifikasi baris `Laptop Dell - 1` menampilkan `John L` pada kolom Modified By
118. Arahkan pointer ke `John L` baris `Laptop Dell - 1`
119. Verifikasi tooltip `John Lennon` tampil
120. Verifikasi baris `Laptop Dell - 1` menampilkan `12/06/26, 09:42` pada kolom Last Updated
121. Verifikasi baris `<b>Meja Rapat</b> - 1` menampilkan teks `<b>Meja Rapat</b> - 1` apa adanya
122. Verifikasi tidak ada teks `null`, `undefined`, maupun `Invalid Date` pada kolom tabel mana pun

### Nilai kosong Brand dan Model / Type, serta hover Model / Type dan Labels
123. Tampilkan Tabel All Assets dengan kondisi K1
124. Verifikasi baris `Kabel Roll - 1` menampilkan `—` pada kolom Brand
125. Verifikasi baris `Kabel Roll - 1` menampilkan `—` pada kolom Model / Type
126. Arahkan pointer ke badge `Latitude 5440` baris `Laptop Dell - 1`
127. Verifikasi tooltip `Latitude 5440` tampil sebagai nama Model / Type penuh
128. Verifikasi baris `Kabel Roll - 1` tidak menampilkan badge pada kolom Model / Type
129. Arahkan pointer ke sel Labels baris `Laptop Dell - 1`
130. Verifikasi hover memuat daftar penuh label `Aset IT`, `Audit 2026`, `Garansi`, dan `Prioritas`

### Pending Asset Value (Fiscal) dan custom field di luar Scope
131. Arahkan pointer ke sel `Pending` Asset Value (Fiscal) baris `Printer Laser - 1`
132. Verifikasi tooltip `Purchase cost has not been set.` tampil pada kolom Asset Value (Fiscal)
133. Verifikasi baris `Meja Kerja - 1` menampilkan `—` pada kolom Nomor Seri karena Asset Name-nya di luar Scope field
134. Verifikasi baris `Laptop Dell - 1` tetap menampilkan `SN-4471` pada kolom Nomor Seri

### Presedensi tooltip Asset Class atas Pending tanpa tooltip dan Rp 0,00
135. Arahkan pointer ke sel `Pending` Asset Value baris `Scanner - 1`
136. Verifikasi tooltip `Asset class has not been set.` tampil walau predikat Asset Value tidak terbaca
137. Verifikasi sel `Pending` baris `Scanner - 1` bertooltip, berbeda dengan sel `Pending` baris `Proyektor - 1` yang tanpa tooltip
138. Arahkan pointer ke sel Asset Value baris `Genset - 1`
139. Verifikasi baris `Genset - 1` menampilkan `Pending` dengan tooltip `Asset class has not been set.` dan bukan `Rp 0,00`

### Date Format, Time Format, dan Time Zone lain
140. Tampilkan Tabel All Assets dengan kondisi K2
141. Verifikasi baris `Laptop Dell - 1` menampilkan `10 Jan 26` pada kolom Register Date
142. Verifikasi baris `Laptop Dell - 1` menampilkan `12 Jun 26, 09:42 AM` pada kolom Last Updated
143. Verifikasi baris `Laptop Dell - 1` menampilkan `05 Jan 26` pada kolom Purchase Date
144. Arahkan pointer ke sel Warranty Expiry baris `Server Rack - 1` dan verifikasi garansi `Garansi Unit — 14 Jun 26` tampil dalam Date Format yang sama
145. Tampilkan Tabel All Assets dengan kondisi K3
146. Verifikasi baris `Laptop Dell - 1` menampilkan `12/06/26, 09:42` pada kolom Last Updated menurut Time Zone `Asia/Jakarta`
147. Arahkan pointer ke sel Warranty Expiry baris `Server Rack - 1`
148. Verifikasi garansi `Garansi Unit — 14/06/26` berwarna warning dengan tooltip `Warranty expires soon` dan masih berlaku, karena hari ini menurut Time Zone adalah `14/06/26`
149. Verifikasi garansi `Garansi Baterai — 15/06/26` berwarna warning dengan tooltip `Warranty expires soon`
150. Tampilkan Tabel All Assets dengan kondisi K4
151. Verifikasi baris `Laptop Dell - 1` menampilkan `12/06/26, 11:42` pada kolom Last Updated menurut Time Zone `Asia/Jayapura`
152. Arahkan pointer ke sel Warranty Expiry baris `Server Rack - 1` dan verifikasi garansi `Garansi Unit — 14/06/26` berwarna danger dengan tooltip `Warranty expired`

### Bulk Action di sisi kiri toolbar setelah baris terpilih
153. Centang baris `Laptop Dell - 1`
154. Verifikasi Bulk Action tampil di sisi kiri toolbar

### Grid responsif baris kartu
155. Tampilkan Tabel All Assets dengan kondisi K5
156. Verifikasi kelima kartu status tampil dalam satu baris
157. Tampilkan Tabel All Assets dengan kondisi K6
158. Verifikasi baris kartu status tersusun dalam tiga kolom
159. Tampilkan Tabel All Assets dengan kondisi K7
160. Verifikasi baris kartu status tersusun dalam dua kolom

### Label aksesibel dan tooltip tombol ikon
161. Tampilkan Tabel All Assets dengan kondisi K1
162. Verifikasi tombol ikon Search, Filter, Download, dan Changelog masing-masing memiliki label aksesibel `Search`, `Filter`, `Download`, dan `Changelog`
163. Verifikasi tombol ikon Actions pada baris `Laptop Dell - 1` memiliki label aksesibel `Actions`
164. Arahkan pointer ke tombol ikon Actions baris `Laptop Dell - 1`
165. Verifikasi tooltip `Actions` tampil
166. Verifikasi setiap tombol ikon pada toolbar dan baris memiliki label aksesibel yang tidak kosong
167. Verifikasi tooltip tombol ikon Search, Filter, Download, Changelog, dan Actions sama dengan label aksesibelnya
