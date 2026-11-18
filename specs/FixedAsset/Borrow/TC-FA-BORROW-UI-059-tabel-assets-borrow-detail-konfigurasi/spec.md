---
id: TC-FA-BORROW-UI-059-tabel-assets-borrow-detail-konfigurasi
title: "Tabel Assets pada Borrow Detail: konfigurasi kolom, nilai kosong, dan aksi baris"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1c#p2", "§4.1c#r1", "§4.1c#r2", "§4.1c#r3", "§4.1c#r4", "§4.1c#r5", "§4.1c#r6", "§4.1c#r7", "§4.1c#r8", "§4.1c#r9", "§4.1c#r10", "§4.1c#r11", "§4.1c#r12", "§4.1c#r13", "§4.1c#r14", "§4.1c#r15", "§4.1c#r16", "§4.1c#r17", "§4.1c#r18", "§4.1c#r19"]
smoke: []
dependsOn: []
trace:
  "§4.1c#p2": [2, 4]
  "§4.1c#r1": [6, 7, 9, 10, 23, 75, 122]
  "§4.1c#r2": [6, 11, 12, 75, 109]
  "§4.1c#r3": [6, 13, 14, 75, 122]
  "§4.1c#r4": [6, 15, 17, 18, 75, 110]
  "§4.1c#r5": [6, 19, 21, 22, 75, 111]
  "§4.1c#r6": [6, 25, 26, 27, 28, 29, 30, 31, 33, 35, 37, 75, 112]
  "§4.1c#r7": [76, 78, 79, 113]
  "§4.1c#r8": [76, 80, 82, 83, 114, 115]
  "§4.1c#r9": [6, 40, 41, 42, 43, 44, 46, 75, 116]
  "§4.1c#r10": [76, 84, 85, 117]
  "§4.1c#r11": [76, 86, 87, 88, 89, 118]
  "§4.1c#r12": [6, 47, 48, 49, 75, 122]
  "§4.1c#r13": [76, 90, 91, 119]
  "§4.1c#r14": [6, 50, 51, 52, 53, 54, 55, 56, 57, 59, 61, 75, 120]
  "§4.1c#r15": [76, 92, 94, 95, 96, 97, 122]
  "§4.1c#r16": [6, 63, 65, 67, 75, 122]
  "§4.1c#r17": [6, 68, 70, 72, 75, 122]
  "§4.1c#r18": [76, 98, 100, 101, 122]
  "§4.1c#r19": [76, 103, 104, 105, 106, 121]
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
  - DU-059-10: Baris Returned satuan jam terlambat dua jam: Name `Meeting Mic Set - 1`, Asset ID `MIC-2026-0001`, Brand `Shure`, Model/Type `MXW`, Status `Returned`, Due Date `03/11/26, 17:05`, Duration `3 hours`, Extensions `0 / 1`, Approval `Self-service`, Handover Photo `ada`, Return Photo `ada`, Handed Over At `03/11/26, 14:05`, Returned At `03/11/26, 19:00`, Keterlambatan `late 2 hours`, Handed Over By `Self-service`, Purpose `Kunjungan lapangan`.
  - DU-059-11: Baris Canceled otomatis oleh sistem: Name `Camera Sony A7 - 1`, Asset ID `CAM-2026-0001`, Brand `kosong`, Model/Type `kosong`, Status `Canceled (Not picked up)`, Due Date `kosong`, Duration `3 days`, Extensions `0 / 1`, Approval `Approved`, Handover Photo `kosong`, Return Photo `kosong`, Reason `Not picked up`.
  - DU-059-12: Baris Rejected dengan alasan Reject: Name `Camera Sony A7 - 44`, Asset ID `CAM-2026-0044`, Brand `kosong`, Model/Type `kosong`, Status `Rejected`, Due Date `kosong`, Duration `6 days`, Extensions `0 / 1`, Approval `Rejected`, Handover Photo `kosong`, Return Photo `kosong`, Reason `Aset sedang menunggu perbaikan dan belum boleh dipinjamkan sampai pemeriksaan ulang oleh Asset Admin selesai`.
  - DU-059-13: Baris Canceled manual sebelum approver memutuskan: Name `Camera Sony A7 - 2`, Asset ID `CAM-2026-0002`, Brand `kosong`, Model/Type `kosong`, Status `Canceled`, Due Date `kosong`, Duration `3 days`, Extensions `0 / 1`, Approval `kosong`, Handover Photo `kosong`, Return Photo `kosong`, Reason `kosong`.
- Kondisi:
  - K1: tabel dimuat berisi DU-059-1 sampai DU-059-13; Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.

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
9. Verifikasi baris `Laptop Dell Latitude 5420 - 7` menampilkan foto utama aset
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
37. Verifikasi dialog Missing Log record itu tampil
38. Tekan Esc

### Due Date, Duration, dan Approval
39. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
40. Verifikasi Due Date baris `Laptop Dell Latitude 5420 - 2` tampil `10/11/26`
41. Verifikasi Due Date baris `Meeting Mic Set - 1` tampil `03/11/26, 17:05` lengkap dengan jam
42. Verifikasi Due Date baris `Laptop Dell Latitude 5420 - 3` memakai severity `danger` karena Overdue pada tabel Assets Borrow Detail
43. Verifikasi Due Date baris `Laptop Dell Latitude 5420 - 7` tampil `—` karena belum handover
44. Verifikasi Due Date baris `Laptop Dell Latitude 5420 - 8` tampil `—` karena belum handover
45. Arahkan kursor ke Due Date baris `Laptop Dell Latitude 5420 - 45`
46. Verifikasi due date asal `04/11/26` tampil pada tooltip Due Date tabel Assets Borrow Detail
47. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 2` tampil `4 days`
48. Verifikasi Duration baris `Meeting Mic Set - 1` tampil `3 hours`
49. Verifikasi setiap baris tabel Assets Borrow Detail memuat Duration
50. Verifikasi Approval baris `Laptop Dell Latitude 5420 - 7` tampil `Auto-approved`
51. Verifikasi Approval baris `Laptop Dell Latitude 5420 - 8` tampil `Waiting`
52. Verifikasi Approval baris `Toyota Avanza - 4` tampil `Not required`
53. Verifikasi Approval baris `Laptop Dell Latitude 5420 - 2` tampil `Self-service`
54. Verifikasi Approval baris `Camera Sony A7 - 1` tampil `Approved`
55. Verifikasi Approval baris `Camera Sony A7 - 44` tampil `Rejected`
56. Verifikasi Approval baris `Projector Epson EB-X06 - 3` tampil `—` karena belum diteruskan ke approval
57. Verifikasi Approval baris `Camera Sony A7 - 2` tampil `—` karena ditutup Canceled sebelum approver memutuskan
58. Arahkan kursor ke Approval baris `Laptop Dell Latitude 5420 - 8`
59. Verifikasi Approval type `Any one approver` dan approver `Rina Wijaya ⏳` tampil
60. Arahkan kursor ke Approval baris `Excavator PC200 - 3`
61. Verifikasi Approval type `All approvers`, approver `Agus Prasetyo ✓`, approver `Rina Wijaya ⏳`, dan progres `(1 of 2 approved)` tampil

### Foto Handover dan Return
62. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
63. Verifikasi Handover Photo baris `Laptop Dell Latitude 5420 - 2` tampil sebagai thumbnail
64. Klik thumbnail Handover Photo baris `Laptop Dell Latitude 5420 - 2`
65. Verifikasi pratinjau foto handover tampil pada tabel Assets Borrow Detail
66. Tekan Esc
67. Verifikasi Handover Photo baris `Toyota Avanza - 5` tampil `—` karena foto tidak diminta
68. Verifikasi Return Photo baris `Laptop Dell Latitude 5420 - 45` tampil sebagai thumbnail
69. Klik thumbnail Return Photo baris `Laptop Dell Latitude 5420 - 45`
70. Verifikasi pratinjau foto return tampil pada tabel Assets Borrow Detail
71. Tekan Esc
72. Verifikasi Return Photo baris `Laptop Dell Latitude 5420 - 2` tampil `—` karena foto belum ada

### Toggle Setup Column dan kolom curated
73. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
74. Klik header kolom Actions `⋯`
75. Verifikasi checkbox `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Status`, `Due Date`, `Duration`, `Approval`, `Handover Photo`, dan `Return Photo` tercentang dan enabled pada tabel Assets Borrow Detail
76. Verifikasi checkbox `TAG`, `Category`, `Handed Over At`, `Returned At`, `Extensions`, `Reason`, `Purpose`, dan `Handed Over By` tidak tercentang dan enabled pada tabel Assets Borrow Detail
77. Centang kolom `TAG`, `Category`, `Handed Over At`, `Returned At`, `Extensions`, `Reason`, `Purpose`, dan `Handed Over By` pada daftar Column Visibility
78. Verifikasi baris `Laptop Dell Latitude 5420 - 45` menampilkan satu ikon TAG dengan label `RFID`
79. Verifikasi TAG baris `Laptop Dell Latitude 5420 - 7` tampil `—` karena `Non TAG`
80. Verifikasi badge Category `Laptop` baris `Laptop Dell Latitude 5420 - 45` tampil dengan severity `primary`
81. Arahkan kursor ke badge Category baris `Laptop Dell Latitude 5420 - 45`
82. Verifikasi hierarki `IT Equipment > Laptop` tampil pada tooltip Category tabel Assets Borrow Detail
83. Verifikasi setiap baris tabel Assets Borrow Detail memuat badge Category
84. Verifikasi Handed Over At baris `Laptop Dell Latitude 5420 - 45` tampil `01/11/26, 10:00`
85. Verifikasi Handed Over At baris `Laptop Dell Latitude 5420 - 7` tampil `—` karena belum diserahkan
86. Verifikasi Returned At baris `Laptop Dell Latitude 5420 - 45` tampil `06/11/26, 16:00`
87. Verifikasi penanda `late 1 day` dengan severity `danger` tampil pada Returned At baris `Laptop Dell Latitude 5420 - 45`
88. Verifikasi penanda `late 2 hours` tampil pada Returned At baris `Meeting Mic Set - 1`
89. Verifikasi Returned At baris `Laptop Dell Latitude 5420 - 7` tampil `—`
90. Verifikasi Extensions baris `Laptop Dell Latitude 5420 - 45` tampil `1 / 1`
91. Verifikasi Extensions baris `Laptop Dell Latitude 5420 - 7` tampil `0 / 1`
92. Verifikasi Reason baris `Camera Sony A7 - 44` tampil dalam satu baris
93. Arahkan kursor ke Reason baris `Camera Sony A7 - 44`
94. Verifikasi teks penuh `Aset sedang menunggu perbaikan dan belum boleh dipinjamkan sampai pemeriksaan ulang oleh Asset Admin selesai` tampil pada tooltip Reason tabel Assets Borrow Detail
95. Verifikasi Reason baris `Camera Sony A7 - 1` tampil `Not picked up`
96. Verifikasi Reason baris `Camera Sony A7 - 2` tampil `—` karena Cancel manual
97. Verifikasi Reason baris `Laptop Dell Latitude 5420 - 7` tampil `—` karena bukan Rejected maupun Canceled oleh System
98. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 45` tampil dalam satu baris
99. Arahkan kursor ke Purpose baris `Laptop Dell Latitude 5420 - 45`
100. Verifikasi teks penuh `Presentasi proposal pengadaan jaringan kepada klien di Surabaya` tampil pada tooltip Purpose tabel Assets Borrow Detail
101. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 7` tampil `—`
102. Arahkan kursor ke Handed Over By baris `Laptop Dell Latitude 5420 - 45`
103. Verifikasi nama lengkap `Agus Prasetyo` tampil pada tooltip Handed Over By
104. Verifikasi Handed Over By baris `Meeting Mic Set - 1` tampil `Self-service`
105. Verifikasi Handed Over By baris `Laptop Dell Latitude 5420 - 7` tampil `—` karena belum diserahkan
106. Verifikasi kolom `Handed Over By` menjadi kolom data terakhir sebelum Actions pada tabel Assets Borrow Detail

### Field dan placeholder Filter Panel
107. Tampilkan Tabel Assets Borrow Detail dengan kondisi K1
108. Klik ikon Filter pada toolbar tabel Assets Borrow Detail
109. Verifikasi placeholder `All asset names` tampil pada field `Asset Name` di Filter Panel Borrow Detail
110. Verifikasi placeholder `All brands` tampil pada field `Brand` di Filter Panel Borrow Detail
111. Verifikasi placeholder `All models` tampil pada field `Model/Type` di Filter Panel Borrow Detail
112. Verifikasi placeholder `All statuses` tampil pada field `Status` di Filter Panel Borrow Detail
113. Verifikasi placeholder `All tags` tampil pada field `TAG` di Filter Panel Borrow Detail
114. Verifikasi placeholder `All categories` tampil pada field `Category` di Filter Panel Borrow Detail
115. Verifikasi field `Category` di Filter Panel Borrow Detail berupa pemilih tree multi-pilih
116. Verifikasi placeholder `Select date` tampil pada field `Due Date` di Filter Panel Borrow Detail
117. Verifikasi placeholder `Select date` tampil pada field `Handed Over At` di Filter Panel Borrow Detail
118. Verifikasi placeholder `Select date` tampil pada field `Returned At` di Filter Panel Borrow Detail
119. Verifikasi input pertama field `Extensions` di Filter Panel Borrow Detail memakai placeholder `Min` dan input kedua memakai placeholder `Max`
120. Verifikasi placeholder `All approvals` tampil pada field `Approval` di Filter Panel Borrow Detail
121. Verifikasi placeholder `All users` tampil pada field `Handed Over By` di Filter Panel Borrow Detail
122. Verifikasi Filter Panel Borrow Detail tidak memuat field `Photo`, `Asset ID`, `Duration`, `Reason`, `Handover Photo`, `Return Photo`, maupun `Purpose`
