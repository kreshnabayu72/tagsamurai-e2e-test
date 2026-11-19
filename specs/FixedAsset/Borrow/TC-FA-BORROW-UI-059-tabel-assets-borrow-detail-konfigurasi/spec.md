---
id: TC-FA-BORROW-UI-059-tabel-assets-borrow-detail-konfigurasi
title: "Tabel Assets pada Borrow Detail: konfigurasi kolom, nilai kosong, dan aksi baris"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1c#p2", "§4.1c#r1", "§4.1c#r2", "§4.1c#r3", "§4.1c#r4", "§4.1c#r5", "§4.1c#r6", "§4.1c#r7", "§4.1c#r8", "§4.1c#r9", "§4.1c#r10", "§4.1c#r11", "§4.1c#r12", "§4.1c#r13", "§4.1c#r14", "§4.1c#r15", "§4.1c#r16", "§4.1c#r17", "§4.1c#r18", "§4.1c#r19"]
smoke: []
dependsOn: []
trace:
  "§4.1c#p2": [2, 4]
  "§4.1c#r1": [6, 7, 9, 10, 23, 74, 121]
  "§4.1c#r2": [6, 11, 12, 74, 108, 124, 148]
  "§4.1c#r3": [6, 13, 14, 74, 121]
  "§4.1c#r4": [6, 15, 17, 18, 74, 109, 125]
  "§4.1c#r5": [6, 19, 21, 22, 74, 110, 126]
  "§4.1c#r6": [6, 25, 26, 27, 28, 29, 30, 31, 33, 35, 37, 74, 111, 127, 152, 153]
  "§4.1c#r7": [75, 77, 78, 112, 128, 138, 166]
  "§4.1c#r8": [75, 79, 81, 82, 113, 114, 139]
  "§4.1c#r9": [6, 39, 40, 41, 42, 43, 45, 74, 115, 130]
  "§4.1c#r10": [75, 83, 84, 116, 131]
  "§4.1c#r11": [75, 85, 86, 87, 88, 117, 132, 157, 158, 159]
  "§4.1c#r12": [6, 46, 47, 48, 74, 121, 173]
  "§4.1c#r13": [75, 89, 90, 118, 133, 143]
  "§4.1c#r14": [6, 49, 50, 51, 52, 53, 54, 55, 56, 58, 60, 74, 119, 146, 161, 162]
  "§4.1c#r15": [75, 91, 93, 94, 95, 96, 121, 170, 171]
  "§4.1c#r16": [6, 62, 64, 66, 74, 121, 149]
  "§4.1c#r17": [6, 67, 69, 71, 74, 121, 150]
  "§4.1c#r18": [75, 97, 99, 100, 121]
  "§4.1c#r19": [75, 102, 103, 104, 105, 120, 129]
anchor: []
coverage:
  web: automated
---
# Tabel Assets pada Borrow Detail: konfigurasi kolom, nilai kosong, dan aksi baris

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Borrow Detail, tab Assets.
- Komponen: Tabel Assets Borrow Detail
- Data:
  - DU-059-1: Baris Waiting for Handover tanpa approval: Name `Laptop Dell Latitude 5420 - 7`, Asset ID `LPT-2026-0007`, Brand `kosong`, Model/Type `kosong`, Status `Waiting for Handover`, Due Date `kosong`, Duration `3 days`, Extensions `0 / 1`, Approval `Auto-approved`, Handover Photo `kosong`, Return Photo `kosong`, Foto utama `kosong`, Handed Over At `kosong`, Returned At `kosong`, Handed Over By `kosong`, Purpose `kosong`, TAG `Non TAG`, Category `Laptop`, Hierarki Category `IT Equipment > Laptop`.
  - DU-059-2: Baris Waiting for Approval dengan Any one approver: Name `Laptop Dell Latitude 5420 - 8`, Asset ID `LPT-2026-0008`, Brand `kosong`, Model/Type `kosong`, Status `Waiting for Approval`, Due Date `kosong`, Duration `3 days`, Extensions `0 / 1`, Approval `Waiting`, Handover Photo `kosong`, Return Photo `kosong`, Approval type `Any one approver`, Approver `Rina Wijaya ⏳`.
  - DU-059-3: Baris Waiting for Approval dengan All approvers dan Max extensions 0: Name `Excavator PC200 - 3`, Asset ID `EXC-2026-0009`, Brand `kosong`, Model/Type `kosong`, Status `Waiting for Approval`, Due Date `kosong`, Duration `3 days`, Extensions `0 / 0`, Approval `Waiting`, Handover Photo `kosong`, Return Photo `kosong`, Approval type `All approvers`, Approver 1 `Agus Prasetyo ✓`, Approver 2 `Rina Wijaya ⏳`, Progres approval `(1 of 2 approved)`.
  - DU-059-4: Baris Borrowed hasil Borrow Now dengan foto handover: Name `Laptop Dell Latitude 5420 - 2`, Asset ID `LPT-2026-0002`, Brand `kosong`, Model/Type `kosong`, Status `Borrowed`, Due Date `10/11/26`, Duration `4 days`, Extensions `0 / 1`, Approval `Self-service`, Handover Photo `ada`, Return Photo `kosong`, Waktu masuk status `07/11/26, 09:10`.
  - DU-059-5: Baris Extension Request yang belum diteruskan ke approval: Name `Projector Epson EB-X06 - 3`, Asset ID `PRJ-2026-0003`, Brand `kosong`, Model/Type `kosong`, Status `Extension Request`, Due Date `12/11/26`, Duration `5 days`, Extensions `0 / 1`, Approval `kosong`, Handover Photo `ada`, Return Photo `kosong`.
  - DU-059-6: Baris Borrowed dengan Reported Damaged: Name `Toyota Avanza - 4`, Asset ID `VEH-2026-0004`, Brand `kosong`, Model/Type `kosong`, Status `Borrowed + Reported Damaged`, Due Date `11/11/26`, Duration `4 days`, Extensions `0 / 1`, Approval `Not required`, Handover Photo `ada`, Return Photo `kosong`.
  - DU-059-7: Baris Borrowed dengan Reported Missing tanpa foto handover: Name `Toyota Avanza - 5`, Asset ID `VEH-2026-0005`, Brand `kosong`, Model/Type `kosong`, Status `Borrowed + Reported Missing`, Due Date `11/11/26`, Duration `4 days`, Extensions `0 / 1`, Approval `Not required`, Handover Photo `kosong`, Return Photo `kosong`, Pelapor Missing `Dewi Lestari`, Tanggal lapor Missing `08/11/26`.
  - DU-059-8: Baris Overdue: Name `Laptop Dell Latitude 5420 - 3`, Asset ID `LPT-2026-0003`, Brand `kosong`, Model/Type `kosong`, Status `Overdue`, Due Date `06/11/26`, Duration `6 days`, Extensions `0 / 1`, Approval `Not required`, Handover Photo `ada`, Return Photo `kosong`.
  - DU-059-9: Baris Returned dengan penanda Damaged, Due date hasil Extend, terlambat satu hari: Name `Laptop Dell Latitude 5420 - 45`, Asset ID `LPT-2026-0045`, Brand `kosong`, Model/Type `kosong`, Status `Returned + Damaged`, Due Date `05/11/26`, Duration `5 days`, Extensions `1 / 1`, Approval `Not required`, Handover Photo `ada`, Return Photo `ada`, Due date asal `04/11/26`, Handed Over At `01/11/26, 10:00`, Returned At `06/11/26, 16:00`, Keterlambatan `late 1 day`, Handed Over By `Agus Prasetyo`, Handed Over By tampil `Agus P`, Purpose `Presentasi proposal pengadaan jaringan kepada klien di Surabaya`, TAG `RFID`, Category `Laptop`, Hierarki Category `IT Equipment > Laptop`.
  - DU-059-10: Baris Returned satuan jam terlambat dua jam: Name `Meeting Mic Set - 1`, Asset ID `MIC-2026-0001`, Brand `Shure`, Model/Type `MXW`, Status `Returned`, Due Date `03/11/26, 17:05`, Duration `3 hours`, Extensions `0 / 1`, Approval `Self-service`, Handover Photo `ada`, Return Photo `ada`, Foto utama `ada`, Handed Over At `03/11/26, 14:05`, Returned At `03/11/26, 19:00`, Keterlambatan `late 2 hours`, Handed Over By `Self-service`, Purpose `Kunjungan lapangan`.
  - DU-059-11: Baris Canceled otomatis oleh sistem: Name `Camera Sony A7 - 1`, Asset ID `CAM-2026-0001`, Brand `kosong`, Model/Type `kosong`, Status `Canceled (Not picked up)`, Due Date `kosong`, Duration `3 days`, Extensions `0 / 1`, Approval `Approved`, Handover Photo `kosong`, Return Photo `kosong`, Reason `Not picked up`.
  - DU-059-12: Baris Rejected dengan alasan Reject: Name `Camera Sony A7 - 44`, Asset ID `CAM-2026-0044`, Brand `kosong`, Model/Type `kosong`, Status `Rejected`, Due Date `kosong`, Duration `6 days`, Extensions `0 / 1`, Approval `Rejected`, Handover Photo `kosong`, Return Photo `kosong`, Approval type `Any one approver`, Approver `Rina Wijaya ✕`, Reason `Aset sedang menunggu perbaikan dan belum boleh dipinjamkan sampai pemeriksaan ulang oleh Asset Admin selesai`.
  - DU-059-13: Baris Canceled manual sebelum approver memutuskan: Name `Camera Sony A7 - 2`, Asset ID `CAM-2026-0002`, Brand `kosong`, Model/Type `kosong`, Status `Canceled`, Due Date `kosong`, Duration `3 days`, Extensions `0 / 1`, Approval `kosong`, Handover Photo `kosong`, Return Photo `kosong`, Reason `kosong`.
  - DU-059-14: Baris Returned satuan jam terlambat satu jam: Name `Meeting Mic Set - 2`, Asset ID `MIC-2026-0002`, Brand `Shure`, Model/Type `MXW`, Status `Returned`, Due Date `03/11/26, 17:05`, Duration `3 hours`, Extensions `0 / 1`, Approval `Self-service`, Handover Photo `ada`, Return Photo `ada`, Handed Over At `03/11/26, 14:05`, Returned At `03/11/26, 18:00`, Keterlambatan `late 1 hour`.
  - DU-059-15: Baris Returned satuan jam tepat waktu: Name `Meeting Mic Set - 3`, Asset ID `MIC-2026-0003`, Brand `Shure`, Model/Type `MXW`, Status `Returned`, Due Date `03/11/26, 17:05`, Duration `3 hours`, Extensions `0 / 1`, Approval `Self-service`, Handover Photo `ada`, Return Photo `ada`, Handed Over At `03/11/26, 14:05`, Returned At `03/11/26, 16:40`.
  - DU-059-16: Baris Canceled otomatis karena Borrower dinonaktifkan: Name `Camera Sony A7 - 3`, Asset ID `CAM-2026-0003`, Brand `kosong`, Model/Type `kosong`, Status `Canceled (Borrower deactivated)`, Due Date `kosong`, Duration `3 days`, Extensions `0 / 1`, Approval `kosong`, Handover Photo `kosong`, Return Photo `kosong`, Reason `Borrower deactivated`.
  - DU-059-17: Baris Canceled otomatis karena aset dilaporkan hilang: Name `Camera Sony A7 - 4`, Asset ID `CAM-2026-0004`, Brand `kosong`, Model/Type `kosong`, Status `Canceled (Asset reported missing)`, Due Date `kosong`, Duration `3 days`, Extensions `0 / 1`, Approval `kosong`, Handover Photo `kosong`, Return Photo `kosong`, Reason `Asset reported missing`.
  - DU-059-18: Baris Overdue dengan pengajuan Extend: Name `Projector Epson EB-X06 - 9`, Asset ID `PRJ-2026-0009`, Brand `kosong`, Model/Type `kosong`, Status `Overdue + Extension Request`, Due Date `05/11/26`, Duration `5 days`, Extensions `0 / 1`, Approval `kosong`, Handover Photo `ada`, Return Photo `kosong`.
  - DU-059-19: Baris Overdue dengan pengajuan Extend yang sudah diteruskan ke approval: Name `Projector Epson EB-X06 - 10`, Asset ID `PRJ-2026-0010`, Brand `kosong`, Model/Type `kosong`, Status `Overdue + Extension Approval`, Due Date `05/11/26`, Duration `5 days`, Extensions `0 / 1`, Approval `Waiting`, Handover Photo `ada`, Return Photo `kosong`.
  - DU-059-20: Baris Borrowed dengan dua TAG Type: Name `Laptop Dell Latitude 5420 - 46`, Asset ID `LPT-2026-0046`, Brand `kosong`, Model/Type `kosong`, Status `Borrowed`, Due Date `10/11/26`, Duration `4 days`, Extensions `0 / 1`, Approval `Not required`, Handover Photo `ada`, Return Photo `kosong`, TAG `RFID` dan `QR`, Category `Laptop`, Hierarki Category `IT Equipment > Laptop`.
- Kondisi:
  - K1: tabel dimuat berisi DU-059-1 sampai DU-059-13; Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.
  - K2: tabel dimuat berisi DU-059-14 sampai DU-059-20; Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.
  - K3: seperti K1; bahasa aktif pengguna adalah bahasa selain English.

## Test Steps

### Tanpa checkbox, kolom Actions, dan urutan kolom awal
1. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
2. Verifikasi tabel Assets Borrow Detail tidak memiliki kolom Checkbox
3. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 7`
4. Verifikasi menu baris memuat aksi `Borrow Log`, `Transaction Rules`, `Hand Over`, `Remind Borrower`, dan `Cancel Borrow`
5. Tekan Esc
6. Verifikasi urutan kolom data dari kiri ke kanan: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Status`, `Due Date`, `Duration`, `Approval`, `Handover Photo`, `Return Photo`
7. Verifikasi tabel Assets Borrow Detail tidak memiliki kolom `Transaction ID`, `Group`, maupun `Borrower`

### Photo, Name, Asset ID, Brand, dan Model/Type
8. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
9. Verifikasi baris `Meeting Mic Set - 1` menampilkan foto utama aset
10. Verifikasi header kolom `Photo` pada tabel Assets Borrow Detail tidak memiliki ikon sort
11. Verifikasi Name `Laptop Dell Latitude 5420 - 7` tampil dengan format nama aset dan increment
12. Verifikasi setiap baris tabel Assets Borrow Detail memuat Name
13. Verifikasi Asset ID `LPT-2026-0007` tampil pada baris `Laptop Dell Latitude 5420 - 7`
14. Verifikasi setiap baris tabel Assets Borrow Detail memuat Asset ID
15. Verifikasi Brand baris `Meeting Mic Set - 1` tampil sebagai badge `Shure` dengan severity `dark`
16. Arahkan kursor ke badge Brand baris `Meeting Mic Set - 1`
17. Verifikasi nama Brand penuh `Shure` tampil pada tooltip Brand tabel Assets Borrow Detail
18. Verifikasi Brand baris `Laptop Dell Latitude 5420 - 7` tampil `—`
19. Verifikasi Model/Type baris `Meeting Mic Set - 1` tampil sebagai badge `MXW` dengan severity `dark`
20. Arahkan kursor ke badge Model/Type baris `Meeting Mic Set - 1`
21. Verifikasi nama Model penuh `MXW` tampil pada tooltip Model/Type tabel Assets Borrow Detail
22. Verifikasi Model/Type baris `Laptop Dell Latitude 5420 - 7` tampil `—`
23. Verifikasi baris `Laptop Dell Latitude 5420 - 7` menampilkan placeholder gambar standar karena foto utama aset tidak ada

### Status dan badge penanda
24. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
25. Verifikasi baris `Laptop Dell Latitude 5420 - 2` memuat badge status `Borrowed`
26. Verifikasi baris `Projector Epson EB-X06 - 3` memuat badge status `Extension Request` dan tidak memuat badge `Borrowed`
27. Verifikasi baris `Laptop Dell Latitude 5420 - 3` memuat badge status `Overdue` pada tabel Assets Borrow Detail
28. Verifikasi setiap baris tabel Assets Borrow Detail memuat badge status
29. Verifikasi baris `Toyota Avanza - 4` memuat badge `Borrowed` dan badge `Reported Damaged` dengan severity `danger`
30. Verifikasi baris `Toyota Avanza - 5` memuat badge `Borrowed` dan badge `Reported Missing` dengan severity `danger`
31. Verifikasi baris `Laptop Dell Latitude 5420 - 45` memuat badge status `Returned` dan badge `Damaged` dengan severity `danger`
32. Arahkan kursor ke badge status baris `Laptop Dell Latitude 5420 - 2`
33. Verifikasi waktu masuk status `07/11/26, 09:10` tampil pada tooltip Status
34. Arahkan kursor ke badge `Reported Missing` baris `Toyota Avanza - 5`
35. Verifikasi tooltip `Reported missing by Dewi Lestari on 08/11/26. Confirm or reject it in Missing.` tampil
36. Klik badge `Reported Missing` baris `Toyota Avanza - 5`
37. Verifikasi klik badge itu memicu pembukaan dialog Missing Log untuk record laporan baris `Toyota Avanza - 5`

### Due Date, Duration, dan Approval
38. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
39. Verifikasi Due Date baris `Laptop Dell Latitude 5420 - 2` tampil `10/11/26`
40. Verifikasi Due Date baris `Meeting Mic Set - 1` tampil `03/11/26, 17:05` lengkap dengan jam
41. Verifikasi Due Date baris `Laptop Dell Latitude 5420 - 3` memakai severity `danger` karena Overdue pada tabel Assets Borrow Detail
42. Verifikasi Due Date baris `Laptop Dell Latitude 5420 - 7` tampil `—` karena belum handover
43. Verifikasi Due Date baris `Laptop Dell Latitude 5420 - 8` tampil `—` karena belum handover
44. Arahkan kursor ke Due Date baris `Laptop Dell Latitude 5420 - 45`
45. Verifikasi due date asal `04/11/26` tampil pada tooltip Due Date tabel Assets Borrow Detail
46. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 2` tampil `4 days`
47. Verifikasi Duration baris `Meeting Mic Set - 1` tampil `3 hours`
48. Verifikasi setiap baris tabel Assets Borrow Detail memuat Duration
49. Verifikasi Approval baris `Laptop Dell Latitude 5420 - 7` tampil `Auto-approved`
50. Verifikasi Approval baris `Laptop Dell Latitude 5420 - 8` tampil `Waiting`
51. Verifikasi Approval baris `Toyota Avanza - 4` tampil `Not required`
52. Verifikasi Approval baris `Laptop Dell Latitude 5420 - 2` tampil `Self-service`
53. Verifikasi Approval baris `Camera Sony A7 - 1` tampil `Approved`
54. Verifikasi Approval baris `Camera Sony A7 - 44` tampil `Rejected`
55. Verifikasi Approval baris `Projector Epson EB-X06 - 3` tampil `—` karena belum diteruskan ke approval
56. Verifikasi Approval baris `Camera Sony A7 - 2` tampil `—` karena ditutup Canceled sebelum approver memutuskan
57. Arahkan kursor ke Approval baris `Laptop Dell Latitude 5420 - 8`
58. Verifikasi Approval type `Any one approver` dan approver `Rina Wijaya ⏳` tampil
59. Arahkan kursor ke Approval baris `Excavator PC200 - 3`
60. Verifikasi Approval type `All approvers`, approver `Agus Prasetyo ✓`, approver `Rina Wijaya ⏳`, dan progres `(1 of 2 approved)` tampil

### Foto Handover dan Return
61. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
62. Verifikasi Handover Photo baris `Laptop Dell Latitude 5420 - 2` tampil sebagai thumbnail
63. Klik thumbnail Handover Photo baris `Laptop Dell Latitude 5420 - 2`
64. Verifikasi pratinjau foto handover tampil pada tabel Assets Borrow Detail
65. Tekan Esc
66. Verifikasi Handover Photo baris `Toyota Avanza - 5` tampil `—` karena foto tidak diminta
67. Verifikasi Return Photo baris `Laptop Dell Latitude 5420 - 45` tampil sebagai thumbnail
68. Klik thumbnail Return Photo baris `Laptop Dell Latitude 5420 - 45`
69. Verifikasi pratinjau foto return tampil pada tabel Assets Borrow Detail
70. Tekan Esc
71. Verifikasi Return Photo baris `Laptop Dell Latitude 5420 - 2` tampil `—` karena foto belum ada

### Toggle Setup Column dan kolom curated
72. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
73. Klik header kolom Actions `⋯`
74. Verifikasi checkbox `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Status`, `Due Date`, `Duration`, `Approval`, `Handover Photo`, dan `Return Photo` tercentang dan enabled pada tabel Assets Borrow Detail
75. Verifikasi checkbox `TAG`, `Category`, `Handed Over At`, `Returned At`, `Extensions`, `Reason`, `Purpose`, dan `Handed Over By` tidak tercentang dan enabled pada tabel Assets Borrow Detail
76. Centang kolom `TAG`, `Category`, `Handed Over At`, `Returned At`, `Extensions`, `Reason`, `Purpose`, dan `Handed Over By` pada daftar Column Visibility
77. Verifikasi baris `Laptop Dell Latitude 5420 - 45` menampilkan satu ikon TAG dengan label `RFID`
78. Verifikasi TAG baris `Laptop Dell Latitude 5420 - 7` tampil `—` karena `Non TAG`
79. Verifikasi badge Category `Laptop` baris `Laptop Dell Latitude 5420 - 45` tampil dengan severity `primary`
80. Arahkan kursor ke badge Category baris `Laptop Dell Latitude 5420 - 45`
81. Verifikasi hierarki `IT Equipment > Laptop` tampil pada tooltip Category tabel Assets Borrow Detail
82. Verifikasi setiap baris tabel Assets Borrow Detail memuat badge Category
83. Verifikasi Handed Over At baris `Laptop Dell Latitude 5420 - 45` tampil `01/11/26, 10:00`
84. Verifikasi Handed Over At baris `Laptop Dell Latitude 5420 - 7` tampil `—` karena belum diserahkan
85. Verifikasi Returned At baris `Laptop Dell Latitude 5420 - 45` tampil `06/11/26, 16:00`
86. Verifikasi penanda `late 1 day` dengan severity `danger` tampil pada Returned At baris `Laptop Dell Latitude 5420 - 45`
87. Verifikasi penanda `late 2 hours` tampil pada Returned At baris `Meeting Mic Set - 1`
88. Verifikasi Returned At baris `Laptop Dell Latitude 5420 - 7` tampil `—`
89. Verifikasi Extensions baris `Laptop Dell Latitude 5420 - 45` tampil `1 / 1`
90. Verifikasi Extensions baris `Laptop Dell Latitude 5420 - 7` tampil `0 / 1`
91. Verifikasi Reason baris `Camera Sony A7 - 44` tampil dalam satu baris
92. Arahkan kursor ke Reason baris `Camera Sony A7 - 44`
93. Verifikasi teks penuh `Aset sedang menunggu perbaikan dan belum boleh dipinjamkan sampai pemeriksaan ulang oleh Asset Admin selesai` tampil pada tooltip Reason tabel Assets Borrow Detail
94. Verifikasi Reason baris `Camera Sony A7 - 1` tampil `Not picked up`
95. Verifikasi Reason baris `Camera Sony A7 - 2` tampil `—` karena Cancel manual
96. Verifikasi Reason baris `Laptop Dell Latitude 5420 - 7` tampil `—` karena bukan Rejected maupun Canceled oleh System
97. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 45` tampil dalam satu baris
98. Arahkan kursor ke Purpose baris `Laptop Dell Latitude 5420 - 45`
99. Verifikasi teks penuh `Presentasi proposal pengadaan jaringan kepada klien di Surabaya` tampil pada tooltip Purpose tabel Assets Borrow Detail
100. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 7` tampil `—`
101. Arahkan kursor ke Handed Over By baris `Laptop Dell Latitude 5420 - 45`
102. Verifikasi nama lengkap `Agus Prasetyo` tampil pada tooltip Handed Over By
103. Verifikasi Handed Over By baris `Meeting Mic Set - 1` tampil `Self-service`
104. Verifikasi Handed Over By baris `Laptop Dell Latitude 5420 - 7` tampil `—` karena belum diserahkan
105. Verifikasi kolom `Handed Over By` menjadi kolom data terakhir sebelum Actions pada tabel Assets Borrow Detail

### Field dan placeholder Filter Panel
106. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
107. Klik ikon Filter pada toolbar tabel Assets Borrow Detail
108. Verifikasi placeholder `All asset names` tampil pada field `Asset Name` di Filter Panel Borrow Detail
109. Verifikasi placeholder `All brands` tampil pada field `Brand` di Filter Panel Borrow Detail
110. Verifikasi placeholder `All models` tampil pada field `Model/Type` di Filter Panel Borrow Detail
111. Verifikasi placeholder `All statuses` tampil pada field `Status` di Filter Panel Borrow Detail
112. Verifikasi placeholder `All tags` tampil pada field `TAG` di Filter Panel Borrow Detail
113. Verifikasi placeholder `All categories` tampil pada field `Category` di Filter Panel Borrow Detail
114. Verifikasi field `Category` di Filter Panel Borrow Detail berupa pemilih tree multi-pilih
115. Verifikasi placeholder `Select date` tampil pada field `Due Date` di Filter Panel Borrow Detail
116. Verifikasi placeholder `Select date` tampil pada field `Handed Over At` di Filter Panel Borrow Detail
117. Verifikasi placeholder `Select date` tampil pada field `Returned At` di Filter Panel Borrow Detail
118. Verifikasi input pertama field `Extensions` di Filter Panel Borrow Detail memakai placeholder `Min` dan input kedua memakai placeholder `Max`
119. Verifikasi placeholder `All approvals` tampil pada field `Approval` di Filter Panel Borrow Detail
120. Verifikasi placeholder `All users` tampil pada field `Handed Over By` di Filter Panel Borrow Detail
121. Verifikasi Filter Panel Borrow Detail tidak memuat field `Photo`, `Asset ID`, `Duration`, `Reason`, `Handover Photo`, `Return Photo`, maupun `Purpose`

### Tipe field Filter Panel Borrow Detail
122. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
123. Klik ikon Filter pada toolbar tabel Assets Borrow Detail
124. Verifikasi field `Asset Name` di Filter Panel Borrow Detail berupa dropdown multi-pilih dengan kotak cari
125. Verifikasi field `Brand` di Filter Panel Borrow Detail berupa dropdown multi-pilih dengan kotak cari
126. Verifikasi field `Model/Type` di Filter Panel Borrow Detail berupa dropdown multi-pilih dengan kotak cari
127. Verifikasi field `Status` di Filter Panel Borrow Detail berupa dropdown multi-pilih dengan kotak cari
128. Verifikasi field `TAG` di Filter Panel Borrow Detail berupa dropdown multi-pilih dengan kotak cari
129. Verifikasi field `Handed Over By` di Filter Panel Borrow Detail berupa dropdown multi-pilih dengan kotak cari
130. Verifikasi field `Due Date` di Filter Panel Borrow Detail berupa pemilih rentang tanggal
131. Verifikasi field `Handed Over At` di Filter Panel Borrow Detail berupa pemilih rentang tanggal
132. Verifikasi field `Returned At` di Filter Panel Borrow Detail berupa pemilih rentang tanggal
133. Verifikasi field berlabel `Extensions` di Filter Panel Borrow Detail berupa rentang angka dengan input `Min` dan `Max`

### Posisi kolom TAG dan Category saat ditampilkan
134. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
135. Klik header kolom Actions `⋯`
136. Centang kolom `TAG` pada daftar Column Visibility
137. Centang kolom `Category` pada daftar Column Visibility
138. Verifikasi kolom `TAG` tampil tepat setelah kolom `Status` pada tabel Assets Borrow Detail
139. Verifikasi kolom `Category` tampil tepat setelah kolom `TAG` pada tabel Assets Borrow Detail

### Extensions pada aset dengan jatah Extend 0
140. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
141. Klik header kolom Actions `⋯`
142. Centang kolom `Extensions` pada daftar Column Visibility
143. Verifikasi Extensions baris `Excavator PC200 - 3` tampil `0 / 0`

### Rincian Approval pada baris Rejected
144. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
145. Arahkan kursor ke Approval baris `Camera Sony A7 - 44`
146. Verifikasi Approval type `Any one approver` dan approver `Rina Wijaya ✕` tampil

### Kolom foto Handover dan Return tidak bisa diurutkan
147. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
148. Verifikasi header kolom `Name` memiliki ikon sort
149. Verifikasi header kolom `Handover Photo` pada tabel Assets Borrow Detail tidak memiliki ikon sort
150. Verifikasi header kolom `Return Photo` pada tabel Assets Borrow Detail tidak memiliki ikon sort

### Status Overdue dengan pengajuan Extend
151. Tampilkan Tabel Assets Borrow Detail dengan kondisi K2
152. Verifikasi baris `Projector Epson EB-X06 - 9` memuat dua badge status `Overdue` dan `Extension Request` pada tabel Assets Borrow Detail
153. Verifikasi baris `Projector Epson EB-X06 - 10` memuat dua badge status `Overdue` dan `Extension Approval` pada tabel Assets Borrow Detail

### Returned At satuan jam: late satu jam dan tepat waktu
154. Tampilkan Tabel Assets Borrow Detail dengan kondisi K2
155. Klik header kolom Actions `⋯`
156. Centang kolom `Returned At` pada daftar Column Visibility
157. Verifikasi penanda `late 1 hour` tampil pada Returned At baris `Meeting Mic Set - 2`
158. Verifikasi Returned At baris `Meeting Mic Set - 3` tampil `03/11/26, 16:40`
159. Verifikasi Returned At baris `Meeting Mic Set - 3` tidak memuat penanda `late` karena dikembalikan sebelum Due Date

### Approval kosong pada baris Canceled karena Borrower dinonaktifkan dan Report Missing
160. Tampilkan Tabel Assets Borrow Detail dengan kondisi K2
161. Verifikasi Approval baris `Camera Sony A7 - 3` tampil `—` karena ditutup Canceled saat Borrower dinonaktifkan
162. Verifikasi Approval baris `Camera Sony A7 - 4` tampil `—` karena ditutup Canceled saat aset dilaporkan hilang

### Aset dengan lebih dari satu TAG Type
163. Tampilkan Tabel Assets Borrow Detail dengan kondisi K2
164. Klik header kolom Actions `⋯`
165. Centang kolom `TAG` pada daftar Column Visibility
166. Verifikasi baris `Laptop Dell Latitude 5420 - 46` menampilkan dua ikon TAG dengan label `RFID` dan `QR`

### Reason Reject verbatim dan alasan sistem mengikuti bahasa aktif
167. Tampilkan Tabel Assets Borrow Detail dengan kondisi K3
168. Klik header kolom Actions `⋯`
169. Centang kolom `Reason` pada daftar Column Visibility
170. Verifikasi Reason baris `Camera Sony A7 - 44` tampil persis `Aset sedang menunggu perbaikan dan belum boleh dipinjamkan sampai pemeriksaan ulang oleh Asset Admin selesai` seperti yang diinput
171. Verifikasi alasan sistem pada baris `Camera Sony A7 - 1` tampil dalam bahasa aktif

### Duration baris yang sudah di-Extend
172. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
173. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 45` tampil `5 days` termasuk perpanjangan sebagai Duration termasuk perpanjangan
