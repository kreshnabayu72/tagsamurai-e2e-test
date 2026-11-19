---
id: TC-FA-BORROW-UI-058-tabel-approvals-borrow-konfigurasi
title: "Tabel Approvals > Borrow Active dan History: konfigurasi kolom dan state"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1f#p2", "§4.1f#r1", "§4.1f#r2", "§4.1f#r3", "§4.1f#r4", "§4.1f#r5", "§4.1f#r6", "§4.1f#r7", "§4.1f#r11", "§4.1f#r12", "§4.1f#r13", "§4.1f#r14", "§4.1f#r15", "§4.1f#r16", "§4.1f#r17", "§4.1f#r18", "§4.1f#r19", "EB-TBL-1@tabel-approvals", "EB-TBL-2@tabel-approvals", "EB-TBL-4@tabel-approvals"]
smoke: []
dependsOn: []
trace:
  "§4.1f#p2": [25, 27, 64, 66]
  "§4.1f#r1": [29, 31, 32, 33, 52, 62]
  "§4.1f#r2": [29, 34, 35, 52, 55]
  "§4.1f#r3": [29, 36, 38, 49, 52, 56, 57]
  "§4.1f#r4": [29, 40, 42, 49, 52, 58]
  "§4.1f#r5": [29, 43, 49, 52, 59]
  "§4.1f#r6": [29, 44, 46, 48, 52, 60]
  "§4.1f#r7": [29, 47, 48, 52, 61]
  "§4.1f#r11": [68, 70, 71, 72, 95, 107]
  "§4.1f#r12": [68, 73, 74, 75, 76, 95, 98]
  "§4.1f#r13": [68, 77, 95, 99]
  "§4.1f#r14": [68, 78, 80, 92, 95, 100, 101]
  "§4.1f#r15": [68, 82, 84, 92, 95, 102]
  "§4.1f#r16": [68, 85, 92, 95, 103]
  "§4.1f#r17": [68, 86, 88, 92, 95, 104]
  "§4.1f#r18": [68, 89, 92, 95, 105]
  "§4.1f#r19": [68, 90, 91, 92, 95, 106]
  "EB-TBL-1@tabel-approvals": [2, 3, 7, 8, 10, 11, 12, 14, 15, 19, 20, 22, 23]
  "EB-TBL-2@tabel-approvals": [33, 49, 72, 92]
  "EB-TBL-4@tabel-approvals": [40, 42, 44, 46, 82, 84, 86, 88]
anchor: []
coverage:
  web: automated
---
# Tabel Approvals > Borrow Active dan History: konfigurasi kolom dan state

## Prerequisites
- Aktor: Approver.
- Layar awal: halaman `Approvals > Borrow`, tab Active.
- Komponen: Tabel Approvals Borrow
- Data:
  - DU-058-1: Pengajuan Borrow dengan dua aset: Transaction ID `BRW-2026-0153`, Type `Borrow`, Group `Head Office`, Hierarki Group `Head Office`, Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Total Asset `2`, Requested By `Agus Prasetyo`, Requested By tampil `Agus P`, Request Date `09/11/26, 09:05`.
  - DU-058-2: Pengajuan Borrow dengan satu aset: Transaction ID `BRW-2026-0154`, Type `Borrow`, Group `Head Office`, Hierarki Group `Head Office`, Borrower `Rudi Hartono`, Borrower tampil `Rudi H`, Total Asset `1`, Requested By `Agus Prasetyo`, Requested By tampil `Agus P`, Request Date `09/11/26, 09:20`.
  - DU-058-3: Pengajuan Extension pada Group cabang: Transaction ID `BRW-2026-0150`, Type `Extension`, Group `Branch Surabaya`, Hierarki Group `Head Office > Branch Surabaya`, Borrower `Dewi Lestari`, Borrower tampil `Dewi L`, Total Asset `1`, Requested By `Dewi Lestari`, Requested By tampil `Dewi L`, Request Date `09/11/26, 07:45`.
  - DU-058-4: Pengajuan Borrow yang semua asetnya ditolak: Transaction ID `BRW-2026-0146`, Status `Rejected`, Type `Borrow`, Group `Head Office`, Hierarki Group `Head Office`, Borrower `Budi Setiawan`, Borrower tampil `Budi S`, Total Asset `1`, Requested By `Agus Prasetyo`, Requested By tampil `Agus P`, Request Date `30/10/26, 09:10`, Decided Date `31/10/26, 11:30`.
  - DU-058-5: Pengajuan Borrow yang semua asetnya disetujui: Transaction ID `BRW-2026-0151`, Status `Approved`, Type `Borrow`, Group `Head Office`, Hierarki Group `Head Office`, Borrower `Sari Dewi`, Borrower tampil `Sari D`, Total Asset `2`, Requested By `Agus Prasetyo`, Requested By tampil `Agus P`, Request Date `08/11/26, 10:00`, Decided Date `08/11/26, 11:00`.
  - DU-058-6: Pengajuan Extension yang sebagian disetujui: Transaction ID `BRW-2026-0155`, Status `Partially Approved`, Type `Extension`, Group `Branch Surabaya`, Hierarki Group `Head Office > Branch Surabaya`, Borrower `Maya Putri`, Borrower tampil `Maya P`, Total Asset `3`, Requested By `Rina Wijaya`, Requested By tampil `Rina W`, Request Date `05/11/26, 09:00`, Decided Date `06/11/26, 14:00`.
  - DU-058-7: Kata kunci tanpa hasil yang diketik pada tabel: Search tanpa hasil `Tidak Ada`.
- Kondisi:
  - K1: tabel Active dimuat berisi DU-058-1 sampai DU-058-3; Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.
  - K2: tabel Active dimuat tanpa data sama sekali.
  - K3: memuat tabel Active gagal karena error server.
  - K4: seperti K1; pencarian `Tidak Ada` dijawab tanpa baris.
  - K5: tabel History dimuat berisi DU-058-4 sampai DU-058-6; Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.
  - K6: tabel History dimuat tanpa data sama sekali.
  - K7: memuat tabel History gagal karena error server.
  - K8: seperti K5; pencarian `Tidak Ada` dijawab tanpa baris.

## Test Steps

### Active kosong alami
1. Tampilkan Tabel Approvals Borrow Active dengan kondisi K2
2. Verifikasi judul `No pending approvals` tampil pada tabel Active
3. Verifikasi deskripsi `You have no pending approval requests at this moment.` tampil pada tabel Active

### Active kosong akibat pencarian tanpa hasil
4. Tampilkan Tabel Approvals Borrow Active dengan kondisi K4
5. Klik ikon Search pada toolbar Active
6. Ketik Search `Tidak Ada`, tekan Enter
7. Verifikasi judul `No results found` tampil pada tabel Active
8. Verifikasi deskripsi `Try adjusting your search or filter.` tampil pada tabel Active

### Active gagal muat bukan empty state
9. Tampilkan Tabel Approvals Borrow Active dengan kondisi K3
10. Verifikasi pesan `Unable to load this data.` tampil pada tabel Active
11. Verifikasi tombol `[Try Again]` tampil pada tabel Active
12. Verifikasi judul `No pending approvals` tidak tampil karena gagal muat bukan empty state

### History kosong alami
13. Tampilkan Tabel Approvals Borrow History dengan kondisi K6
14. Verifikasi judul `No history yet` tampil pada tabel History
15. Verifikasi deskripsi `Decided or closed borrows will appear here.` tampil pada tabel History

### History kosong akibat pencarian tanpa hasil
16. Tampilkan Tabel Approvals Borrow History dengan kondisi K8
17. Klik ikon Search pada toolbar History
18. Ketik Search `Tidak Ada`, tekan Enter
19. Verifikasi judul `No results found` tampil pada tabel History
20. Verifikasi deskripsi `Try adjusting your search or filter.` tampil pada tabel History

### History gagal muat bukan empty state
21. Tampilkan Tabel Approvals Borrow History dengan kondisi K7
22. Verifikasi pesan `Unable to load this data.` tampil pada tabel History
23. Verifikasi tombol `[Try Again]` tampil pada tabel History

### Active: tanpa checkbox, kolom Actions, dan urutan kolom
24. Tampilkan Tabel Approvals Borrow Active dengan kondisi K1
25. Verifikasi tabel Active tidak memiliki kolom Checkbox maupun bar Bulk Action
26. Klik `⋯` pada baris `BRW-2026-0153` di tabel Active
27. Verifikasi menu baris tabel Active memuat aksi `Review`
28. Tekan Esc
29. Verifikasi urutan kolom data tabel Active dari kiri ke kanan: `Transaction ID`, `Type`, `Group`, `Borrower`, `Total Asset`, `Requested By`, `Request Date`

### Active: Transaction ID, Type, dan Group
30. Tampilkan Tabel Approvals Borrow Active dengan kondisi K1
31. Verifikasi Transaction ID `BRW-2026-0153` pada tabel Active tampil sebagai tautan
32. Verifikasi tombol salin tampil di samping Transaction ID `BRW-2026-0153` pada tabel Active
33. Verifikasi setiap baris tabel Active memuat Transaction ID
34. Verifikasi baris `BRW-2026-0153` pada tabel Active memuat badge Type `Borrow` dengan severity `dark`
35. Verifikasi baris `BRW-2026-0150` pada tabel Active memuat badge Type `Extension` dengan severity `dark`
36. Verifikasi badge Group `Head Office` baris `BRW-2026-0153` pada tabel Active memakai severity `primary`
37. Arahkan kursor ke badge Group baris `BRW-2026-0150` pada tabel Active
38. Verifikasi hierarki `Head Office > Branch Surabaya` tampil pada tooltip Group tabel Active

### Active: Borrower, Total Asset, Requested By, dan Request Date
39. Tampilkan Tabel Approvals Borrow Active dengan kondisi K1
40. Verifikasi Borrower baris `BRW-2026-0153` pada tabel Active tampil `Budi S`
41. Arahkan kursor ke Borrower baris `BRW-2026-0153` pada tabel Active
42. Verifikasi nama lengkap `Budi Setiawan` tampil pada tooltip Borrower tabel Active
43. Verifikasi Total Asset baris `BRW-2026-0153` pada tabel Active bernilai `2` sebagai angka bulat
44. Verifikasi Requested By baris `BRW-2026-0153` pada tabel Active tampil `Agus P`
45. Arahkan kursor ke Requested By baris `BRW-2026-0153` pada tabel Active
46. Verifikasi nama lengkap `Agus Prasetyo` tampil pada tooltip Requested By tabel Active
47. Verifikasi Request Date baris `BRW-2026-0153` pada tabel Active tampil `09/11/26, 09:05`
48. Verifikasi kolom `Request Date` menjadi kolom data terakhir sebelum Actions dan `Requested By` kolom data kedua dari akhir pada tabel Active
49. Verifikasi setiap baris tabel Active memuat nilai pada kolom Group, Borrower, Total Asset, Requested By, dan Request Date

### Active: toggle Setup Column
50. Tampilkan Tabel Approvals Borrow Active dengan kondisi K1
51. Klik header kolom Actions `⋯` pada tabel Active
52. Verifikasi checkbox `Transaction ID`, `Type`, `Group`, `Borrower`, `Total Asset`, `Requested By`, dan `Request Date` tercentang dan enabled pada tabel Active

### Active: field dan placeholder Filter Panel
53. Tampilkan Tabel Approvals Borrow Active dengan kondisi K1
54. Klik ikon Filter pada toolbar Active
55. Verifikasi placeholder `All types` tampil pada field `Type` di Filter Panel Active
56. Verifikasi field `Group` di Filter Panel Active berupa pemilih tree multi-pilih
57. Verifikasi placeholder `All groups` tampil pada field `Group` di Filter Panel Active
58. Verifikasi placeholder `All borrowers` tampil pada field `Borrower` di Filter Panel Active
59. Verifikasi input pertama field `Total Asset` di Filter Panel Active memakai placeholder `Min` dan input kedua memakai placeholder `Max`
60. Verifikasi placeholder `All users` tampil pada field `Requested By` di Filter Panel Active
61. Verifikasi placeholder `Select date` tampil pada field `Request Date` di Filter Panel Active
62. Verifikasi Filter Panel Active tidak memuat field `Transaction ID`

### History: tanpa checkbox, kolom Actions, dan urutan kolom
63. Tampilkan Tabel Approvals Borrow History dengan kondisi K5
64. Verifikasi tabel History tidak memiliki kolom Checkbox maupun bar Bulk Action
65. Klik `⋯` pada baris `BRW-2026-0146` di tabel History
66. Verifikasi menu baris tabel History memuat aksi `Detail`
67. Tekan Esc
68. Verifikasi urutan kolom data tabel History dari kiri ke kanan: `Transaction ID`, `Status`, `Type`, `Group`, `Borrower`, `Total Asset`, `Requested By`, `Request Date`, `Decided Date`

### History: Transaction ID, Status, Type, dan Group
69. Tampilkan Tabel Approvals Borrow History dengan kondisi K5
70. Verifikasi Transaction ID `BRW-2026-0146` pada tabel History tampil sebagai tautan
71. Verifikasi tombol salin tampil di samping Transaction ID `BRW-2026-0146` pada tabel History
72. Verifikasi setiap baris tabel History memuat Transaction ID
73. Verifikasi baris `BRW-2026-0151` memuat badge Status `Approved` dengan severity `success`
74. Verifikasi baris `BRW-2026-0155` memuat badge Status `Partially Approved` dengan severity `warning`
75. Verifikasi baris `BRW-2026-0146` memuat badge Status `Rejected` dengan severity `danger`
76. Verifikasi setiap baris tabel History memuat badge Status
77. Verifikasi baris `BRW-2026-0146` pada tabel History memuat badge Type `Borrow` dan baris `BRW-2026-0155` memuat badge Type `Extension`
78. Verifikasi badge Group `Head Office` baris `BRW-2026-0146` pada tabel History memakai severity `primary`
79. Arahkan kursor ke badge Group baris `BRW-2026-0155` pada tabel History
80. Verifikasi hierarki `Head Office > Branch Surabaya` tampil pada tooltip Group tabel History

### History: Borrower, Total Asset, Requested By, dan tanggal
81. Tampilkan Tabel Approvals Borrow History dengan kondisi K5
82. Verifikasi Borrower baris `BRW-2026-0146` pada tabel History tampil `Budi S`
83. Arahkan kursor ke Borrower baris `BRW-2026-0146` pada tabel History
84. Verifikasi nama lengkap `Budi Setiawan` tampil pada tooltip Borrower tabel History
85. Verifikasi Total Asset baris `BRW-2026-0151` pada tabel History bernilai `2` sebagai angka bulat
86. Verifikasi Requested By baris `BRW-2026-0155` pada tabel History tampil `Rina W`
87. Arahkan kursor ke Requested By baris `BRW-2026-0155` pada tabel History
88. Verifikasi nama lengkap `Rina Wijaya` tampil pada tooltip Requested By tabel History
89. Verifikasi Request Date baris `BRW-2026-0146` pada tabel History tampil `30/10/26, 09:10`
90. Verifikasi Decided Date baris `BRW-2026-0146` pada tabel History tampil `31/10/26, 11:30`
91. Verifikasi kolom `Decided Date` menjadi kolom data terakhir sebelum Actions pada tabel History
92. Verifikasi setiap baris tabel History memuat nilai pada kolom Group, Borrower, Total Asset, Requested By, Request Date, dan Decided Date

### History: toggle Setup Column
93. Tampilkan Tabel Approvals Borrow History dengan kondisi K5
94. Klik header kolom Actions `⋯` pada tabel History
95. Verifikasi checkbox `Transaction ID`, `Status`, `Type`, `Group`, `Borrower`, `Total Asset`, `Requested By`, `Request Date`, dan `Decided Date` tercentang dan enabled pada tabel History

### History: field dan placeholder Filter Panel
96. Tampilkan Tabel Approvals Borrow History dengan kondisi K5
97. Klik ikon Filter pada toolbar History
98. Verifikasi placeholder `All statuses` tampil pada field `Status` di Filter Panel History
99. Verifikasi placeholder `All types` tampil pada field `Type` di Filter Panel History
100. Verifikasi field `Group` di Filter Panel History berupa dropdown multi-pilih dengan kotak cari, bukan pemilih tree
101. Verifikasi placeholder `All groups` tampil pada field `Group` di Filter Panel History
102. Verifikasi placeholder `All borrowers` tampil pada field `Borrower` di Filter Panel History
103. Verifikasi input pertama field `Total Asset` di Filter Panel History memakai placeholder `Min` dan input kedua memakai placeholder `Max`
104. Verifikasi placeholder `All users` tampil pada field `Requested By` di Filter Panel History
105. Verifikasi placeholder `Select date` tampil pada field `Request Date` di Filter Panel History
106. Verifikasi placeholder `Select date` tampil pada field `Decided Date` di Filter Panel History
107. Verifikasi Filter Panel History tidak memuat field `Transaction ID`
