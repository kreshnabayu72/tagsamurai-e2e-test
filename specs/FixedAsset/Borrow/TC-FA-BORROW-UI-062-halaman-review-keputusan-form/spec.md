---
id: TC-FA-BORROW-UI-062-halaman-review-keputusan-form
title: "Halaman Review Approval: toggle Approve dan Reject, Approve Duration, Approval Note, dan kontrol tersembunyi"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-BRW-198", "FI-BRW-199", "FI-BRW-200", "FI-BRW-201", "FI-BRW-202", "FI-BRW-203", "FI-BRW-204", "FI-BRW-205", "FLD-BRW-13", "FLD-BRW-16", "FLD-BRW-17", "V-BRW-26", "V-BRW-27", "§4.1g#p2", "§4.1g#r1", "§4.1g#r2", "§4.1g#r3", "§4.1g#r4", "§4.1g#r5", "§4.1g#r6", "§4.1g#r7", "§4.1g#r8", "§4.1g#r9", "§4.1g#r10", "§4.1g#r11", "§4.1g#r12", "§4.1g#r13", "§4.1g#r14", "§4.1g#r15", "§4.1g#p4", "EB-FRM-4@form-review-approval", "EB-ERR-1@approve-reject"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-198": [86, 92, 93, 110, 115]
  "FI-BRW-199": 115
  "FI-BRW-200": [83, 123, 124]
  "FI-BRW-201": [80, 84, 125]
  "FI-BRW-202": 89
  "FI-BRW-203": 88
  "FI-BRW-204": 86
  "FI-BRW-205": 90
  "FLD-BRW-13": [119, 120]
  "FLD-BRW-16": [97, 100, 106]
  "FLD-BRW-17": [87, 93, 110, 113]
  "V-BRW-26": [97, 100, 103, 106]
  "V-BRW-27": [110, 113]
  "§4.1g#p2": [79, 80, 81]
  "§4.1g#r1": [2, 3, 4, 6, 38, 48]
  "§4.1g#r2": [2, 7, 38, 50]
  "§4.1g#r3": [2, 8, 38, 52]
  "§4.1g#r4": [2, 9, 10, 38, 54]
  "§4.1g#r5": [2, 11, 12, 38, 56]
  "§4.1g#r6": [39, 42, 43]
  "§4.1g#r7": [39, 45]
  "§4.1g#r8": [2, 13, 38, 58]
  "§4.1g#r9": [2, 14, 15, 38, 60]
  "§4.1g#r10": [26, 27, 66, 69]
  "§4.1g#r11": [26, 28, 66, 71]
  "§4.1g#r12": [26, 29, 30, 31, 32, 66, 73]
  "§4.1g#r13": [26, 33, 66, 75]
  "§4.1g#r14": [26, 34, 35, 66, 77]
  "§4.1g#r15": [2, 16, 17, 18, 19, 21, 23, 24, 38, 62]
  "§4.1g#p4": [40, 63]
  "EB-FRM-4@form-review-approval": [103, 106]
  "EB-ERR-1@approve-reject": [128, 130, 131, 132, 134, 138, 139, 141]
anchor: [46, 67]
coverage:
  web: automated
---

# Halaman Review Approval: toggle Approve dan Reject, Approve Duration, Approval Note, dan kontrol tersembunyi

## Prerequisites
- Aktor: Approver `Rina W`, approver dari aset yang dimilikinya di pengajuan.
- Layar awal: Halaman Review Approval
- Komponen: Halaman Review Approval
- Data:
  - DU-062-2: baris milik Approver, pengajuan Borrow, Photo `laptop-dell.jpg`, Name `Laptop Dell Latitude 5420 - 8`, Asset ID `LPT-2026-0008`, Brand `Dell`, Model/Type `Latitude 5420`, TAG `RFID`, Category `Laptop`, Duration `3 / 3 days`, Purpose `Demo aplikasi ke klien`, Approval Rule `Any one approver · Waiting`, durasi diminta `3` days.
  - DU-062-3: baris milik Approver, pengajuan Borrow, tanpa foto, Name `Excavator PC200 - 3`, Asset ID `EXC-2026-0009`, Brand `—`, Model/Type `—`, TAG `Non TAG`, Category `Alat Berat`, Duration `3 / 7 days`, Purpose `—`, Approval Rule `All approvers · 0 of 2 approved`, durasi diminta `3` days.
  - DU-062-4: baris milik Approver, pengajuan Borrow, Photo `excavator.jpg`, Name `Excavator PC200 - 1`, Asset ID `EXC-2026-0007`, Brand `—`, Model/Type `—`, TAG `Non TAG`, Category `Alat Berat`, Duration `2 / 7 days`, Purpose `Pengerjaan jalan akses proyek`, Approval Rule `Rina W (You) · Waiting`, durasi diminta `2` days.
  - DU-062-5: baris milik approver lain, pengajuan Borrow, Photo `genset.jpg`, Name `Genset Honda EU20i - 1`, Asset ID `GEN-2026-0001`, Brand `Honda`, Model/Type `EU20i`, TAG `RFID`, Category `Genset`, Duration `2 / 7 days`, Purpose `Cadangan listrik acara kantor`, Approval Rule `Agus P · Waiting`.
  - DU-062-6: baris milik Approver, pengajuan Extension, Name `Toyota Avanza - 2`, Asset ID `VEH-2026-0002`, Brand `Toyota`, Model/Type `Avanza`, Category `Kendaraan`, Current Due Date `11/11/2026`, Extensions `0 / 1`, Extend By `3 days`, New Due Date `14/11/2026`, Reason `Proyek lapangan belum selesai`, Approval Rule `Any one approver · Waiting`.
  - DU-062-7: baris milik Approver, pengajuan Extension, Name `Toyota Hilux - 1`, Asset ID `VEH-2026-0003`, Brand `Toyota`, Model/Type `Hilux`, Category `Kendaraan`, Current Due Date `12/11/2026`, Extensions `0 / 1`, Extend By `1 day`, New Due Date `13/11/2026`, Reason `—`, Approval Rule `Any one approver · Waiting`.
  - DU-062-8: baris yang sudah diputuskan, Name `Printer Epson L3110 - 1`, Asset ID `PRT-2026-0001`, Approval Rule `Approved`.
  - DU-062-9: baris yang sudah diputuskan, Name `Printer Epson L3110 - 2`, Asset ID `PRT-2026-0002`, Approval Rule `Rejected`.
  - DU-062-10: baris milik Approver, pengajuan Extension, Name `Genset Honda EU20i - 2`, Asset ID `GEN-2026-0002`, Brand `Honda`, Model/Type `EU20i`, Category `Genset`, Extend By `1 hour`, Approval Rule `Any one approver · Waiting`.
  - DU-062-11: baris milik Approver, pengajuan Extension, Name `Forklift Toyota 8FD - 1`, Asset ID `FRK-2026-0001`, Brand `Toyota`, Model/Type `8FD`, Category `Alat Berat`, Extend By `2 hours`, Approval Rule `Any one approver · Waiting`.
- Kondisi:
  - K1: pengajuan tipe Borrow, tabel berisi DU-062-2, DU-062-3, DU-062-4, dan DU-062-5.
  - K2: pengajuan tipe Extension, Date Format bernilai `DD/MM/YYYY`, tabel berisi DU-062-6, DU-062-7, DU-062-10, dan DU-062-11.
  - K3: pengajuan tipe Borrow, tabel berisi DU-062-8 dan DU-062-9.
  - K4: pengajuan tipe Borrow, tabel berisi DU-062-2, Submit pertama dijawab error server, Submit berikutnya berhasil.
  - K5: pengajuan tipe Borrow, tabel berisi DU-062-2, Submit pertama tidak mendapat respons karena koneksi putus, Submit berikutnya berhasil.

## Test Steps

### Isi sel kolom data tabel Borrow
1. Tampilkan Halaman Review Approval dengan kondisi K1
2. Verifikasi tabel menampilkan kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Duration`, `Purpose`, dan `Approval Rule`
3. Verifikasi kolom Photo baris `Laptop Dell Latitude 5420 - 8` menampilkan foto aset
4. Verifikasi kolom Photo baris `Excavator PC200 - 3` menampilkan placeholder gambar standar
5. Klik foto baris `Laptop Dell Latitude 5420 - 8`
6. Verifikasi pratinjau foto aset `Laptop Dell Latitude 5420 - 8` dalam ukuran penuh tampil
7. Verifikasi kolom Name baris pertama menampilkan `Laptop Dell Latitude 5420 - 8`
8. Verifikasi kolom Asset ID baris `Laptop Dell Latitude 5420 - 8` menampilkan `LPT-2026-0008`
9. Verifikasi kolom Brand baris `Laptop Dell Latitude 5420 - 8` menampilkan `Dell`
10. Verifikasi kolom Brand baris `Excavator PC200 - 3` menampilkan `—`
11. Verifikasi kolom Model/Type baris `Laptop Dell Latitude 5420 - 8` menampilkan `Latitude 5420`
12. Verifikasi kolom Model/Type baris `Excavator PC200 - 3` menampilkan `—`
13. Verifikasi kolom Duration baris `Laptop Dell Latitude 5420 - 8` menampilkan `3 / 3 days`
14. Verifikasi kolom Purpose baris `Laptop Dell Latitude 5420 - 8` menampilkan `Demo aplikasi ke klien`
15. Verifikasi kolom Purpose baris `Excavator PC200 - 3` menampilkan `—`
16. Verifikasi kolom Approval Rule baris `Laptop Dell Latitude 5420 - 8` menampilkan `Any one approver · Waiting`
17. Verifikasi kolom Approval Rule baris `Excavator PC200 - 3` menampilkan `All approvers · 0 of 2 approved`
18. Verifikasi kolom Approval Rule baris `Excavator PC200 - 1` menampilkan `Rina W (You) · Waiting`
19. Verifikasi kolom Approval Rule baris `Genset Honda EU20i - 1` menampilkan `Agus P · Waiting`
20. Klik Approval Rule baris `Laptop Dell Latitude 5420 - 8`
21. Verifikasi dialog `Approval Progress` tampil

### Isi sel Approval Rule sesudah diputuskan
22. Tampilkan Halaman Review Approval dengan kondisi K3
23. Verifikasi kolom Approval Rule baris `Printer Epson L3110 - 1` menampilkan `Approved`
24. Verifikasi kolom Approval Rule baris `Printer Epson L3110 - 2` menampilkan `Rejected`

### Isi sel kolom data tabel Extension
25. Tampilkan Halaman Review Approval dengan kondisi K2
26. Verifikasi tabel menampilkan kolom `Current Due Date`, `Extensions`, `Extend By`, `New Due Date`, dan `Reason`
27. Verifikasi kolom Current Due Date baris `Toyota Avanza - 2` menampilkan `11/11/2026`
28. Verifikasi kolom Extensions baris `Toyota Avanza - 2` menampilkan `0 / 1`
29. Verifikasi kolom Extend By baris `Toyota Avanza - 2` menampilkan `3 days`
30. Verifikasi kolom Extend By baris `Toyota Hilux - 1` menampilkan `1 day`
31. Verifikasi kolom Extend By baris `Genset Honda EU20i - 2` menampilkan `1 hour`
32. Verifikasi kolom Extend By baris `Forklift Toyota 8FD - 1` menampilkan `2 hours`
33. Verifikasi kolom New Due Date baris `Toyota Avanza - 2` menampilkan `14/11/2026`
34. Verifikasi kolom Reason baris `Toyota Avanza - 2` menampilkan `Proyek lapangan belum selesai`
35. Verifikasi kolom Reason baris `Toyota Hilux - 1` menampilkan `—`

### Setup Column kolom data tabel Borrow
36. Tampilkan Halaman Review Approval dengan kondisi K1
37. Klik header kolom Actions (⋯)
38. Verifikasi panel Column Visibility mencentang `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Duration`, `Purpose`, dan `Approval Rule`
39. Verifikasi panel Column Visibility tidak mencentang `TAG` dan `Category`
40. Verifikasi panel Column Visibility tidak memuat `Approval`, `Approve Duration`, dan `Approval Note` sebagai kolom
41. Centang `TAG` pada panel Column Visibility
42. Verifikasi kolom TAG baris `Laptop Dell Latitude 5420 - 8` menampilkan ikon TAG
43. Verifikasi kolom TAG baris `Excavator PC200 - 3` menampilkan `—`
44. Centang `Category` pada panel Column Visibility
45. Verifikasi kolom Category baris `Laptop Dell Latitude 5420 - 8` menampilkan `Laptop`
46. Verifikasi tabel menampilkan kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `TAG`, `Category`, `Duration`, `Purpose`, dan `Approval Rule`
47. Hilangkan centang `Photo` pada panel Column Visibility
48. Verifikasi kolom `Photo` tidak tampil di tabel
49. Hilangkan centang `Name` pada panel Column Visibility
50. Verifikasi kolom `Name` tidak tampil di tabel
51. Hilangkan centang `Asset ID` pada panel Column Visibility
52. Verifikasi kolom `Asset ID` tidak tampil di tabel
53. Hilangkan centang `Brand` pada panel Column Visibility
54. Verifikasi kolom `Brand` tidak tampil di tabel
55. Hilangkan centang `Model/Type` pada panel Column Visibility
56. Verifikasi kolom `Model/Type` tidak tampil di tabel
57. Hilangkan centang `Duration` pada panel Column Visibility
58. Verifikasi kolom `Duration` tidak tampil di tabel
59. Hilangkan centang `Purpose` pada panel Column Visibility
60. Verifikasi kolom `Purpose` tidak tampil di tabel
61. Hilangkan centang `Approval Rule` pada panel Column Visibility
62. Verifikasi kolom `Approval Rule` tidak tampil di tabel
63. Verifikasi kontrol `Approval`, `Approve Duration`, dan `Approval Note` tetap tampil di kolom paling kanan dengan urutan itu

### Setup Column kolom data tabel Extension
64. Tampilkan Halaman Review Approval dengan kondisi K2
65. Klik header kolom Actions (⋯)
66. Verifikasi panel Column Visibility mencentang `Current Due Date`, `Extensions`, `Extend By`, `New Due Date`, dan `Reason`
67. Verifikasi tabel menampilkan kolom `Current Due Date`, `Extensions`, `Extend By`, `New Due Date`, dan `Reason` sebelum disembunyikan
68. Hilangkan centang `Current Due Date` pada panel Column Visibility
69. Verifikasi kolom `Current Due Date` tidak tampil di tabel
70. Hilangkan centang `Extensions` pada panel Column Visibility
71. Verifikasi kolom `Extensions` tidak tampil di tabel
72. Hilangkan centang `Extend By` pada panel Column Visibility
73. Verifikasi kolom `Extend By` tidak tampil di tabel
74. Hilangkan centang `New Due Date` pada panel Column Visibility
75. Verifikasi kolom `New Due Date` tidak tampil di tabel
76. Hilangkan centang `Reason` pada panel Column Visibility
77. Verifikasi kolom `Reason` tidak tampil di tabel

### Kolom checkbox dan Actions, serta pemilihan baris
78. Tampilkan Halaman Review Approval dengan kondisi K1
79. Verifikasi checkbox baris `Laptop Dell Latitude 5420 - 8` dapat dicentang
80. Verifikasi checkbox baris `Genset Honda EU20i - 1` disabled
81. Verifikasi kolom Actions baris `Laptop Dell Latitude 5420 - 8` kosong, tanpa row action
82. Centang checkbox header tabel
83. Verifikasi baris `Laptop Dell Latitude 5420 - 8`, `Excavator PC200 - 3`, dan `Excavator PC200 - 1` terpilih
84. Verifikasi baris `Genset Honda EU20i - 1` tidak terpilih

### Keputusan per aset dan baris milik approver lain
85. Tampilkan Halaman Review Approval dengan kondisi K1
86. Verifikasi toggle Approval baris `Laptop Dell Latitude 5420 - 8`, `Excavator PC200 - 3`, dan `Excavator PC200 - 1` berlabel `Approve`
87. Verifikasi Approve Duration baris `Laptop Dell Latitude 5420 - 8` terisi `3`, sama dengan durasi diminta
88. Verifikasi baris `Genset Honda EU20i - 1` menampilkan keterangan `Not your approval`
89. Verifikasi kontrol Approval, Approve Duration, dan Approval Note baris `Genset Honda EU20i - 1` read-only
90. Verifikasi footer hanya memiliki satu tombol `[Submit]` untuk seluruh keputusan, tanpa tombol Submit pada baris
91. Klik toggle Approval baris `Laptop Dell Latitude 5420 - 8`
92. Verifikasi toggle Approval baris `Laptop Dell Latitude 5420 - 8` berlabel `Reject`
93. Verifikasi Approve Duration baris `Laptop Dell Latitude 5420 - 8` tidak dapat diisi selama `Reject`

### Approval Note wajib saat Reject
94. Tampilkan Halaman Review Approval dengan kondisi K1
95. Klik toggle Approval baris `Laptop Dell Latitude 5420 - 8`
96. Klik `[Submit]`
97. Verifikasi pesan `Approval note must not be empty` tampil di bawah input Approval Note baris `Laptop Dell Latitude 5420 - 8`
98. Isi Approval Note baris `Laptop Dell Latitude 5420 - 8` hanya dengan spasi
99. Klik `[Submit]`
100. Verifikasi pesan `Approval note must not be empty` tampil di bawah input Approval Note baris `Laptop Dell Latitude 5420 - 8` yang hanya berisi spasi
101. Ganti isi Approval Note baris `Laptop Dell Latitude 5420 - 8` dengan `Permintaan ditolak karena aset sudah dijadwalkan untuk inventarisasi kantor cabang pada periode yang sama dan belum bisa` (120 karakter)
102. Klik `[Submit]`
103. Verifikasi dialog `Submit Approval` tampil karena Approval Note tepat di batas diterima
104. Klik `[Cancel]` pada dialog `Submit Approval`
105. Ganti isi Approval Note baris `Laptop Dell Latitude 5420 - 8` dengan `Permintaan ditolak karena aset sudah dijadwalkan untuk inventarisasi kantor cabang pada periode yang sama dan belum bisa.` (121 karakter)
106. Verifikasi pesan `Max. 120 characters` tampil di bawah input Approval Note baris `Laptop Dell Latitude 5420 - 8`

### Approve Duration melewati durasi diminta, negatif, dan nol
107. Tampilkan Halaman Review Approval dengan kondisi K1
108. Isi Approve Duration baris `Laptop Dell Latitude 5420 - 8` dengan `5`
109. Pindahkan fokus dari input Approve Duration baris `Laptop Dell Latitude 5420 - 8`
110. Verifikasi Approve Duration baris `Laptop Dell Latitude 5420 - 8` menjadi `3`, sama dengan durasi diminta[^drift-1]
111. Ganti isi Approve Duration baris `Laptop Dell Latitude 5420 - 8` dengan `-2`
112. Pindahkan fokus dari input Approve Duration baris `Laptop Dell Latitude 5420 - 8`
113. Verifikasi Approve Duration baris `Laptop Dell Latitude 5420 - 8` menjadi `0`[^drift-2]
114. Klik `[Submit]`
115. Verifikasi pesan `Approval note must not be empty` tampil di bawah input Approval Note baris `Laptop Dell Latitude 5420 - 8` karena Approve Duration `0` dihitung Reject

### Bulk action Approve dan Reject
116. Tampilkan Halaman Review Approval dengan kondisi K1
117. Centang checkbox header tabel
118. Pilih `Reject` pada bulk action
119. Verifikasi pesan `Approval note must not be empty` tampil di bawah input note bulk action
120. Verifikasi tombol terapkan bulk action disabled selama note kosong
121. Isi Approval note bulk action dengan `Aset sedang dipakai proyek lain pada periode yang sama`
122. Klik tombol terapkan bulk action
123. Verifikasi toggle Approval baris `Laptop Dell Latitude 5420 - 8`, `Excavator PC200 - 3`, dan `Excavator PC200 - 1` berlabel `Reject`
124. Verifikasi Approval Note baris `Laptop Dell Latitude 5420 - 8` terisi `Aset sedang dipakai proyek lain pada periode yang sama`
125. Verifikasi baris `Genset Honda EU20i - 1` tetap menampilkan keterangan `Not your approval`

### Submit keputusan gagal karena error server lalu diulang
126. Tampilkan Halaman Review Approval dengan kondisi K4
127. Klik `[Submit]`
128. Verifikasi dialog `Submit Approval` tampil sebagai konfirmasi sebelum Submit dikirim
129. Klik `[Submit]` pada dialog `Submit Approval`
130. Verifikasi toast `Error, failed to approve borrow.` tampil
131. Verifikasi toast error keputusan Approval tidak menampilkan tombol aksi `[Try Again]`
132. Verifikasi dialog `Submit Approval` tetap terbuka, toggle Approval baris `Laptop Dell Latitude 5420 - 8` tetap `Approve`, dan tombol `[Submit]` pada dialog aktif lagi
133. Klik `[Submit]` pada dialog `Submit Approval`
134. Verifikasi toast `Success, borrow has been approved.` tampil sesudah Submit diulang

### Submit keputusan gagal karena koneksi putus lalu diulang
135. Tampilkan Halaman Review Approval dengan kondisi K5
136. Klik `[Submit]`
137. Klik `[Submit]` pada dialog `Submit Approval`
138. Verifikasi toast `Connection problem. Please try again.` tampil setelah Submit tidak mendapat respons
139. Verifikasi dialog `Submit Approval` tetap terbuka dan tombol `[Submit]` pada dialog aktif lagi setelah gangguan koneksi
140. Klik `[Submit]` pada dialog `Submit Approval`
141. Verifikasi toast `Success, borrow has been approved.` tampil sesudah koneksi pulih

[^drift-1]: Drift PRD vs kontrak komponen. PRD §4.2.9 (kontrol keputusan T-BRW-08), V-BRW-27, dan FLD-BRW-17: Approve Duration yang melebihi durasi diminta ditolak dengan caption `Max. [Requested] [Unit]` di bawah input. Kontrak `NumberInput#1`: `min` dan `max` adalah rentang, bukan filter ketik; nilai di luar rentang dijepit ke batas terdekat saat blur atau Enter. Kontrak `NumberInput#15`: tidak ada pesan rentang dan tidak ada state invalid untuk nilai di luar `min`/`max`. Diasersi: kontrak, nilai dijepit ke durasi diminta tanpa caption (SB-7).

[^drift-2]: Drift PRD vs kontrak komponen. PRD FLD-BRW-17 dan V-BRW-27: angka negatif tidak dapat diketik pada Approve Duration. Kontrak `NumberInput#1`: nilai di luar rentang tetap tampil seperti diketik (`-7` dengan `min` 0 tampil `-7`) dan baru dijepit ke batas terdekat saat blur. Kontrak `NumberInput#2`: tanda minus yang diketik tetap tampil selama mengetik. Diasersi: kontrak, `-2` diterima saat diketik lalu dijepit menjadi `0` saat fokus dipindahkan (SB-7).
