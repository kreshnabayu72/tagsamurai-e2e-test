---
id: TC-FA-ASTL-UI-061-menu-aksi-tooltip
title: "Menu aksi baris dan Bulk Action: tooltip Disabled"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-15d", "ASTL-LOGIC-15r", "ASTL-LOGIC-17l", "ASTL-LOGIC-17n", "ASTL-LOGIC-19b", "ASTL-LOGIC-19c", "S-14", "S-15", "S-16", "S-18", "S-19", "S-27", "S-29", "S-30", "S-32", "S-33", "S-34", "S-35", "EC-22", "EC-45", "§4.5#b4"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-15d": [58, 60, 131]
  "ASTL-LOGIC-15r": [77, 79]
  "ASTL-LOGIC-17l": [3, 5, 7, 9, 11, 13, 15, 17, 19, 45, 47]
  "ASTL-LOGIC-17n": [39, 41, 98, 100, 106, 108]
  "ASTL-LOGIC-19b": [39, 41, 51, 53, 98, 100, 102, 106, 108]
  "ASTL-LOGIC-19c": [58, 60, 65, 67, 73, 84, 129, 131]
  "S-14": 79
  "S-15": 89
  "S-16": [3, 5]
  "S-18": [7, 9]
  "S-19": [11, 13]
  "S-27": [22, 24]
  "S-29": [29, 31]
  "S-30": [33, 35]
  "S-32": [39, 41, 47, 53, 67, 98, 100, 102, 106, 108]
  "S-33": [60, 131]
  "S-34": [15, 17]
  "S-35": [134, 136, 138, 140, 142, 144, 147, 149, 151, 153]
  "EC-22": [87, 89]
  "EC-45": [22, 24, 26]
  "§4.5#b4": [92, 94, 114, 117, 120, 124]
anchor: []
coverage:
  web: automated
---
# Menu aksi baris dan Bulk Action: tooltip Disabled

## Prerequisites
- Aktor: Total Control; pada kondisi K6 aktor hanya memegang hak Manage purchase.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Menu Aksi All Assets
- Data:
  - DU-061-1: Aset berjejak penyusutan Posted: Name `Aset Posted 1`, Status `Available`, Lisensi `Unmanaged`.
  - DU-061-2: Aset berdisposal Executed yang jurnal pelepasannya belum Posted: Name `Aset Disposal 1`, Status `Disposed`.
  - DU-061-3: Aset dengan record Missing berjalan: Name `Aset Missing 1`, Status `Missing`, Lisensi `Unmanaged`.
  - DU-061-4: Aset berdisposal Reported atau DSP aktif: Name `Aset Disposal Aktif 1`, Status `In Disposal Process`, Lisensi `Unmanaged`.
  - DU-061-5: Aset dengan Custody Borrowed: Name `Aset Dipinjam 1`, Status `Borrowed`.
  - DU-061-6: Aset dengan Custody Assigned: Name `Aset Ditugaskan 1`, Status `Assigned`.
  - DU-061-8: Aset dengan Activity Lock In Audit: Name `Aset Audit 1`, Status `In Audit`, Lisensi `Unmanaged`.
  - DU-061-9: Aset dengan Activity Lock Under Maintenance: Name `Aset Servis 1`, Status `Under Maintenance`, Lisensi `Unmanaged`.
  - DU-061-10: Aset Unmanaged dengan Custody Borrowed: Name `Aset Lepas 1`, Status `Borrowed`, Lisensi `Unmanaged`.
  - DU-061-11: Aset Unmanaged di group GA: Name `Aset Unmanaged A1`, Status `Available`, Group `GA`, Lisensi `Unmanaged`.
  - DU-061-12: Aset Unmanaged di group GB: Name `Aset Unmanaged B1`, Status `Available`, Group `GB`, Lisensi `Unmanaged`.
  - DU-061-13: Aset managed di group GA: Name `Aset Managed A1`, Status `Available`, Group `GA`, Lisensi `Managed`.
  - DU-061-14: Aset berstatus Disposed: Name `Aset Disposed 1`, Status `Disposed`.
  - DU-061-18: Aset dengan Custody In Borrow Process: Name `Aset Proses Pinjam 1`, Status `In Borrow Process`.
  - DU-061-19: Aset dengan Custody In Assignment Process: Name `Aset Proses Tugas 1`, Status `In Assignment Process`.
  - DU-061-17: Aset dengan Custody In Transfer Process dengan baris Transfer In Transit: Name `Aset Proses 3`, Status `In Transfer Process`, baris Transfer `In Transit`.
  - DU-061-15: Jeda Manage group `GA` berakhir `15/06/26, 10:30`; tooltip yang diharapkan `Manage is available again on 15/06/26, 10:30.`, dari tanggal dan waktu itu.
- Kondisi:
  - K1: tabel memuat DU-061-1 sampai DU-061-6 dan DU-061-8 sampai DU-061-10, DU-061-14, DU-061-17 sampai DU-061-19, dan Total Control memegang hak atas seluruh aset itu.
  - K2: tabel memuat DU-061-11 sampai DU-061-13, dan tidak ada jeda Manage pada group mana pun.
  - K3: tabel memuat DU-061-11, DU-061-13, dan DU-061-15 berlaku untuk group `GA`.
  - K4: tabel memuat DU-061-5.
  - K5: tabel memuat DU-061-1, DU-061-10, dan DU-061-13.
  - K6: aktor hanya memegang hak Manage purchase sehingga tidak ada aksi Bulk yang ditawarkan baginya pada aset Disposed, dan tabel memuat DU-061-14.
  - K7: tabel memuat DU-061-11 dan DU-061-12, dan DU-061-15 berlaku untuk group `GA`.

## Test Steps

### Tooltip blokir Delete Asset Data pada baris
1. Tampilkan Menu Aksi All Assets dengan kondisi K1
2. Klik `⋯` pada baris `Aset Posted 1`
3. Verifikasi aksi `Delete Asset Data` tampil Disabled
4. Arahkan pointer ke aksi `Delete Asset Data`
5. Verifikasi tooltip `Asset has posted depreciation or journal entries. Use Disposal.` tampil
6. Klik `⋯` pada baris `Aset Disposal 1`
7. Verifikasi aksi `Delete Asset Data` tampil Disabled
8. Arahkan pointer ke aksi `Delete Asset Data`
9. Verifikasi tooltip `Asset has a disposal that is not posted yet.` tampil
10. Klik `⋯` pada baris `Aset Missing 1`
11. Verifikasi aksi `Delete Asset Data` tampil Disabled
12. Arahkan pointer ke aksi `Delete Asset Data`
13. Verifikasi tooltip `Asset has an ongoing missing record. Complete or close the record first.` tampil
14. Klik `⋯` pada baris `Aset Disposal Aktif 1`
15. Verifikasi aksi `Delete Asset Data` tampil Disabled
16. Arahkan pointer ke aksi `Delete Asset Data`
17. Verifikasi tooltip `Asset has an open disposal report or request. Cancel or complete it first.` tampil
18. Klik `⋯` pada baris `Aset Lepas 1`
19. Verifikasi aksi `Delete Asset Data` tidak ditawarkan pada menu baris

### Tooltip aksi Report Missing untuk baris Transfer In Transit
20. Tampilkan Menu Aksi All Assets dengan kondisi K1
21. Klik `⋯` pada baris `Aset Proses 3`
22. Verifikasi aksi `Report Missing` tampil Disabled
23. Arahkan pointer ke aksi `Report Missing`
24. Verifikasi tooltip `This asset is in transfer. Report it missing from Transfer.` tampil
25. Klik `⋯` pada baris `Aset Dipinjam 1`
26. Verifikasi aksi `Report Missing` tampil aktif, tidak Disabled

### Tooltip aksi yang diblok Activity Lock
27. Tampilkan Menu Aksi All Assets dengan kondisi K1
28. Klik `⋯` pada baris `Aset Audit 1`
29. Verifikasi aksi `Delete Asset Data` tampil Disabled
30. Arahkan pointer ke aksi `Delete Asset Data`
31. Verifikasi tooltip `Asset is in audit. Complete or cancel the audit to continue.` tampil
32. Klik `⋯` pada baris `Aset Servis 1`
33. Verifikasi aksi `Delete Asset Data` tampil Disabled
34. Arahkan pointer ke aksi `Delete Asset Data`
35. Verifikasi tooltip `Asset is under maintenance. Complete the maintenance task to continue.` tampil

### Tooltip Bulk Delete Asset Data dan aksi transaksi
36. Tampilkan Menu Aksi All Assets dengan kondisi K5
37. Centang baris `Aset Posted 1`
38. Klik `Bulk Action`
39. Verifikasi aksi `Delete Asset Data` tampil Disabled
40. Arahkan pointer ke aksi `Delete Asset Data`
41. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil
42. Hapus centang baris `Aset Posted 1`
43. Centang baris `Aset Lepas 1`
44. Klik `Bulk Action`
45. Verifikasi aksi `Delete Asset Data` tampil Disabled
46. Arahkan pointer ke aksi `Delete Asset Data`
47. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil

### Aksi transaksi Bulk Disabled bagi aset yang tidak memenuhi syarat
48. Tampilkan Menu Aksi All Assets dengan kondisi K4
49. Centang baris `Aset Dipinjam 1`
50. Klik `Bulk Action`
51. Verifikasi aksi `Borrow`, `Assign`, `Transfer`, `Add to Borrow Draft`, `Add to Assignment Draft`, dan `Add to Transfer Draft` tampil Disabled
52. Arahkan pointer ke aksi `Borrow`
53. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil

### Manage Disabled bila seleksi berasal dari lebih dari satu group
54. Tampilkan Menu Aksi All Assets dengan kondisi K2
55. Centang baris `Aset Unmanaged A1`
56. Centang baris `Aset Unmanaged B1`
57. Klik `Bulk Action`
58. Verifikasi aksi `Manage` tampil Disabled
59. Arahkan pointer ke aksi `Manage`
60. Verifikasi tooltip `Select assets from a single group to manage them.` tampil

### Manage Disabled bila seleksi memuat aset yang bukan Unmanaged
61. Tampilkan Menu Aksi All Assets dengan kondisi K2
62. Centang baris `Aset Unmanaged A1`
63. Centang baris `Aset Managed A1`
64. Klik `Bulk Action`
65. Verifikasi aksi `Manage` tampil Disabled
66. Arahkan pointer ke aksi `Manage`
67. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil

### Urutan tooltip Manage saat beberapa penyebab berlaku
68. Tampilkan Menu Aksi All Assets dengan kondisi K2
69. Centang baris `Aset Unmanaged B1`
70. Centang baris `Aset Managed A1`
71. Klik `Bulk Action`
72. Arahkan pointer ke aksi `Manage`
73. Verifikasi tooltip `Select assets from a single group to manage them.` tampil, bukan `Some selected assets are not eligible for this action. Check the Status column for the cause.`

### Manage Disabled selama jeda antar aksi Manage
74. Tampilkan Menu Aksi All Assets dengan kondisi K3
75. Centang baris `Aset Unmanaged A1`
76. Klik `Bulk Action`
77. Verifikasi aksi `Manage` tampil Disabled
78. Arahkan pointer ke aksi `Manage`
79. Verifikasi tooltip `Manage is available again on 15/06/26, 10:30.` tampil
80. Hapus centang baris `Aset Unmanaged A1`
81. Centang baris `Aset Managed A1`
82. Centang baris `Aset Unmanaged A1`
83. Arahkan pointer ke aksi `Manage`
84. Verifikasi tooltip `Manage is available again on 15/06/26, 10:30.` tampil, bukan `Some selected assets are not eligible for this action. Check the Status column for the cause.`

### Tombol Bulk Action Disabled bila tidak ada aksi yang memenuhi syarat
85. Tampilkan Menu Aksi All Assets dengan kondisi K6
86. Centang baris `Aset Disposed 1`
87. Verifikasi tombol `Bulk Action` tampil Disabled
88. Arahkan pointer ke tombol `Bulk Action`
89. Verifikasi tooltip `No action is available for the selected assets.` tampil

### Aksi dapat dijalankan dengan keyboard
90. Tampilkan Menu Aksi All Assets dengan kondisi K1
91. Tekan Tab sampai fokus pada tombol `⋯` baris `Aset Posted 1`
92. Verifikasi fokus terlihat pada tombol `⋯`
93. Tekan Enter
94. Verifikasi menu aksi baris terbuka

### Bulk Action Disabled bagi aset yang terkunci Activity Lock
95. Tampilkan Menu Aksi All Assets dengan kondisi K1
96. Centang baris `Aset Audit 1`
97. Klik `Bulk Action`
98. Verifikasi aksi `Delete Asset Data` dan `Borrow` tampil Disabled
99. Arahkan pointer ke aksi `Delete Asset Data`
100. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil
101. Arahkan pointer ke aksi `Borrow`
102. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil
103. Hapus centang baris `Aset Audit 1`
104. Centang baris `Aset Servis 1`
105. Klik `Bulk Action`
106. Verifikasi aksi `Delete Asset Data` dan `Borrow` tampil Disabled
107. Arahkan pointer ke aksi `Delete Asset Data`
108. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil

### Aksi dijalankan dengan keyboard
109. Tampilkan Menu Aksi All Assets dengan kondisi K1
110. Tekan Tab sampai fokus pada tombol `⋯` baris `Aset Posted 1`
111. Tekan Enter
112. Tekan panah bawah sampai fokus pada item menu pertama yang tidak Disabled
113. Tekan Enter
114. Verifikasi aksi item itu dijalankan dan menu aksi tertutup
115. Tekan Tab sampai fokus pada checkbox baris `Aset Posted 1`
116. Tekan Spasi
117. Verifikasi baris `Aset Posted 1` tercentang dan fokus terlihat pada checkbox
118. Tekan Tab sampai fokus pada tombol `Bulk Action`
119. Tekan Enter
120. Verifikasi menu Bulk Action terbuka dan fokus terlihat pada tombol `Bulk Action`
121. Tekan Escape
122. Tekan Tab sampai fokus pada checkbox `Select All`
123. Tekan Spasi
124. Verifikasi seluruh baris pada halaman tercentang

### Urutan tooltip Manage: beberapa group didahulukan atas jeda
125. Tampilkan Menu Aksi All Assets dengan kondisi K7
126. Centang baris `Aset Unmanaged A1`
127. Centang baris `Aset Unmanaged B1`
128. Klik `Bulk Action`
129. Verifikasi aksi `Manage` tampil Disabled
130. Arahkan pointer ke aksi `Manage`
131. Verifikasi tooltip `Select assets from a single group to manage them.` tampil, bukan `Manage is available again on 15/06/26, 10:30.`

### Tooltip Report Disposal Disabled menurut Custody
132. Tampilkan Menu Aksi All Assets dengan kondisi K1
133. Klik `⋯` pada baris `Aset Dipinjam 1`
134. Verifikasi aksi `Report Disposal` tampil Disabled
135. Arahkan pointer ke aksi `Report Disposal`
136. Verifikasi tooltip `This asset is in borrow process.` tampil
137. Klik `⋯` pada baris `Aset Ditugaskan 1`
138. Verifikasi aksi `Report Disposal` tampil Disabled
139. Arahkan pointer ke aksi `Report Disposal`
140. Verifikasi tooltip `This asset is in assignment process.` tampil
141. Klik `⋯` pada baris `Aset Proses 3`
142. Verifikasi aksi `Report Disposal` tampil Disabled
143. Arahkan pointer ke aksi `Report Disposal`
144. Verifikasi tooltip `This asset is in transfer.` tampil

### Tooltip Report Disposal Disabled untuk Custody dalam proses
145. Tampilkan Menu Aksi All Assets dengan kondisi K1
146. Klik `⋯` pada baris `Aset Proses Pinjam 1`
147. Verifikasi aksi `Report Disposal` tampil Disabled
148. Arahkan pointer ke aksi `Report Disposal`
149. Verifikasi tooltip `This asset is in borrow process.` tampil
150. Klik `⋯` pada baris `Aset Proses Tugas 1`
151. Verifikasi aksi `Report Disposal` tampil Disabled
152. Arahkan pointer ke aksi `Report Disposal`
153. Verifikasi tooltip `This asset is in assignment process.` tampil
