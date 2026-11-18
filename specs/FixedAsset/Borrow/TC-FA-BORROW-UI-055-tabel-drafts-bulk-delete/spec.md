---
id: TC-FA-BORROW-UI-055-tabel-drafts-bulk-delete
title: "Tabel Drafts: konfigurasi kolom dan mekanik bulk Delete dengan bar seleksi, batas seleksi, dan reaksi gagal"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1l#p3", "§4.1l#r1", "§4.1l#r2", "§4.1l#r3", "§4.1l#r4", "§4.1l#r5", "§4.1l#r6", "§4.1l#p8", "§4.1l#p10", "§5#r6", "EB-TBL-1@tabel-drafts", "EB-TBL-2@tabel-drafts", "EB-TBL-4@tabel-drafts", "EB-BLK-1@tabel-drafts", "EB-BLK-4", "EB-BLK-6"]
smoke: []
dependsOn: []
trace:
  "§4.1l#p3": [14, 16]
  "§4.1l#r1": [18, 20, 22, 23, 24, 25, 26, 59, 71]
  "§4.1l#r2": [28, 29, 31, 32, 60, 61, 72]
  "§4.1l#r3": [34, 35, 37, 38, 62, 72]
  "§4.1l#r4": [40, 41, 42, 44, 45, 63, 72]
  "§4.1l#r5": [46, 48, 49, 50, 64, 72]
  "§4.1l#r6": [18, 51, 53, 55, 56, 65, 72]
  "§4.1l#p8": [63, 67]
  "§4.1l#p10": 70
  "§5#r6": 92
  "EB-TBL-1@tabel-drafts": [2, 3, 7, 8, 10, 11, 12]
  "EB-TBL-2@tabel-drafts": [32, 38]
  "EB-TBL-4@tabel-drafts": [20, 22, 46, 48]
  "EB-BLK-1@tabel-drafts": [75, 76, 78, 79, 81, 83, 85, 87, 94, 95, 97, 104, 105]
  "EB-BLK-4": [112, 113, 120, 121]
  "EB-BLK-6": [125, 126, 129]
anchor: [74]
coverage:
  web: automated
---
# Tabel Drafts: konfigurasi kolom dan mekanik bulk Delete dengan bar seleksi, batas seleksi, dan reaksi gagal

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman `Transactions > Borrow`, tab Drafts.
- Komponen: Tabel Drafts
- Data:
  - DU-055-1: Draft Borrower `Budi Setiawan` (tampil `Budi S`), Group `Head Office`, Total Asset `2`, Origin `New`, Modified By `Rina Wijaya` (tampil `Rina W`), Last Updated `09/11/26, 08:01`.
  - DU-055-2: Draft Borrower `Rudi Hartono` (tampil `Rudi H`), Group `Branch Surabaya`, Total Asset `1 ⚠` dengan aset `Camera Sony A7 IV - 1` yang Duration-nya belum diisi, Origin `Restored` dengan baris kedua Borrower `Restored from BRW-2026-0152`, Modified By `Agus Prasetyo` (tampil `Agus P`), Last Updated `08/11/26, 14:20`.
  - DU-055-3: Draft Borrower `Sari Dewi` (tampil `Sari D`), Group `Head Office` dan `Branch Surabaya`, Total Asset `4`, Origin `Restored by system` dengan baris kedua Borrower `Restored from BRW-2026-0153`, Modified By `System`, Last Updated `08/11/26, 09:45`.
  - DU-055-4: Draft Borrower `Andi Pratama` (tampil `Andi P`), Group `Head Office`, Total Asset `2 ⚠`, Origin `New`, Modified By `Rina Wijaya`, Last Updated `30/09/26, 16:10`.
  - DU-055-5: Draft Borrower `Maya Putri` (tampil `Maya P`), Group `Head Office`, `Branch Surabaya`, dan `Branch Bandung`, Total Asset `3`, Origin `New`, Modified By `Rina Wijaya`, Last Updated `07/11/26, 10:00`.
  - DU-055-6: Draft tanpa aset Borrower `Siti Nurbaya` (tampil `Siti N`), Group kosong, Total Asset `0`, Origin `New`, Modified By `Rina Wijaya`, Last Updated `09/11/26, 07:00`.
  - DU-055-7: 12 Draft Borrower `Peminjam{n} Pratama` (tampil `Peminjam{n} P`), Group `Head Office`, Total Asset `1`, Origin `New`.
  - DU-055-8: 1.500 Draft Borrower `Peminjam{n} Pratama` (tampil `Peminjam{n} P`), Group `Head Office`, Total Asset `1`, Origin `New`.
  - DU-055-9: kata kunci tanpa hasil `Tidak Ada` dan nomor halaman `101`.
- Kondisi:
  - K1: tabel dimuat berisi DU-055-1 sampai DU-055-6; waktu sekarang `09/11/26, 20:30`; Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.
  - K2: tabel dimuat tanpa data sama sekali.
  - K3: memuat tabel gagal karena error server.
  - K4: seperti K1; pencarian `Tidak Ada` dijawab tanpa baris.
  - K5: tabel dimuat berisi 12 baris DU-055-7; ukuran halaman bawaan 10 baris.
  - K6: seperti K5; Bulk Delete dikonfirmasi dan dijawab sukses untuk semua Draft terpilih.
  - K7: seperti K5; Bulk Delete dikonfirmasi dan dijawab gagal karena error server.
  - K8: seperti K5; Bulk Delete dikonfirmasi dan dijawab gagal karena koneksi terputus.
  - K9: Selection Limit bernilai `1000`; tabel dimuat dengan total 1.500 baris DU-055-8.

## Test Steps

### Kosong alami
1. Tampilkan Tabel Drafts dengan kondisi K2
2. Verifikasi judul `No drafts` tampil pada tabel Drafts
3. Verifikasi deskripsi `Saved drafts from you and your team will appear here.` tampil pada tabel Drafts

### Kosong akibat pencarian tanpa hasil
4. Tampilkan Tabel Drafts dengan kondisi K4
5. Klik ikon Search pada toolbar
6. Ketik Search `Tidak Ada`, tekan Enter
7. Verifikasi judul `No results found` tampil pada tabel Drafts
8. Verifikasi deskripsi `Try adjusting your search or filter.` tampil pada tabel Drafts

### Gagal muat bukan empty state
9. Tampilkan Tabel Drafts dengan kondisi K3
10. Verifikasi pesan `Unable to load this data.` tampil pada tabel Drafts
11. Verifikasi tombol `[Try Again]` tampil pada tabel Drafts
12. Verifikasi judul `No drafts` tidak tampil karena gagal muat bukan empty state

### Kolom pertama, kolom Actions, dan urutan kolom
13. Tampilkan Tabel Drafts dengan kondisi K1
14. Verifikasi kolom pertama tabel adalah kolom Checkbox
15. Klik `⋯` pada baris `Andi P`
16. Verifikasi menu baris memuat aksi `Edit` dan `Delete`
17. Tekan Esc
18. Verifikasi urutan kolom data dari kiri ke kanan sesudah Checkbox: `Borrower`, `Group`, `Total Asset`, `Origin`, `Modified By`, `Last Updated`

### Borrower dan nama user
19. Tampilkan Tabel Drafts dengan kondisi K1
20. Verifikasi Borrower baris `Andi P` tampil sebagai tautan
21. Arahkan kursor ke Borrower baris `Andi P`
22. Verifikasi nama lengkap `Andi Pratama` tampil pada tooltip Borrower baris `Andi P`
23. Verifikasi baris `Sari D` memuat baris kedua `Restored from BRW-2026-0153` pada kolom Borrower
24. Verifikasi baris `Rudi H` memuat baris kedua `Restored from BRW-2026-0152` pada kolom Borrower
25. Verifikasi baris `Andi P` tidak memuat baris kedua `Restored from` pada kolom Borrower
26. Verifikasi setiap baris tabel Drafts memuat Borrower

### Group dan nilai kosong
27. Tampilkan Tabel Drafts dengan kondisi K1
28. Verifikasi baris `Sari D` memuat badge Group `Head Office` dan `Branch Surabaya`
29. Verifikasi baris `Maya P` memuat dua badge Group dan chip `+1 more`
30. Arahkan kursor ke Group baris `Maya P`
31. Verifikasi daftar Group `Head Office`, `Branch Surabaya`, dan `Branch Bandung` tampil
32. Verifikasi Group baris `Siti N` tampil `—`

### Total Asset
33. Tampilkan Tabel Drafts dengan kondisi K1
34. Verifikasi Total Asset baris `Andi P` tampil `2 ⚠`
35. Verifikasi Total Asset baris `Budi S` tampil `2` tanpa `⚠`
36. Arahkan kursor ke Total Asset baris `Rudi H`
37. Verifikasi aset `Camera Sony A7 IV - 1` tampil beserta keterangan isian Duration yang kurang
38. Verifikasi Total Asset baris `Siti N` tampil `0`

### Origin, Modified By, dan Last Updated
39. Tampilkan Tabel Drafts dengan kondisi K1
40. Verifikasi Origin baris `Budi S` tampil `New`
41. Verifikasi Origin baris `Rudi H` tampil `Restored`
42. Verifikasi Origin baris `Sari D` tampil `Restored by system`
43. Arahkan kursor ke badge Origin baris `Rudi H`
44. Verifikasi nomor BRW asal `BRW-2026-0152` tampil pada tooltip Origin
45. Verifikasi setiap baris tabel memuat Origin
46. Verifikasi Modified By baris `Budi S` tampil `Rina W`
47. Arahkan kursor ke Modified By baris `Budi S`
48. Verifikasi nama lengkap `Rina Wijaya` tampil pada tooltip Modified By baris `Budi S`
49. Verifikasi Modified By baris `Sari D` tampil `System`
50. Verifikasi setiap baris tabel memuat Modified By
51. Verifikasi Last Updated baris `Budi S` tampil `09/11/26, 08:01`
52. Arahkan kursor ke Last Updated baris `Rudi H`
53. Verifikasi teks `1 day ago` tampil
54. Arahkan kursor ke Last Updated baris `Andi P`
55. Verifikasi teks `40 days ago` tampil
56. Verifikasi setiap baris tabel memuat Last Updated

### Field dan placeholder Filter Panel
57. Tampilkan Tabel Drafts dengan kondisi K1
58. Klik ikon Filter pada toolbar
59. Verifikasi placeholder `All borrowers` tampil pada field `Borrower` di Filter Panel Drafts
60. Verifikasi placeholder `All groups` tampil pada field `Group` di Filter Panel Drafts
61. Verifikasi field `Group` di Filter Panel Drafts berupa pemilih tree multi-pilih
62. Verifikasi input pertama field `Total Asset` di Filter Panel Drafts memakai placeholder `Min` dan input kedua memakai placeholder `Max`
63. Verifikasi placeholder `All origins` tampil pada field `Origin`
64. Verifikasi placeholder `All users` tampil pada field `Modified By`
65. Verifikasi placeholder `Select date` tampil pada field `Last Updated` di Filter Panel Drafts
66. Klik field `Origin`
67. Verifikasi opsi `New`, `Restored`, dan `Restored by system` tampil pada field `Origin`

### Column Visibility pada panel cepat
68. Tampilkan Tabel Drafts dengan kondisi K1
69. Klik header kolom Actions `⋯`
70. Verifikasi daftar kolom tabel tampil pada panel Column Visibility
71. Verifikasi checkbox `Borrower` tercentang dan enabled[^drift-1]
72. Verifikasi checkbox `Group`, `Total Asset`, `Origin`, `Modified By`, dan `Last Updated` tercentang dan enabled

### Seleksi baris, bar, dan counter
73. Tampilkan Tabel Drafts dengan kondisi K5
74. Verifikasi baris `Peminjam1 P` tampil pada tabel
75. Verifikasi checkbox header tidak tercentang
76. Verifikasi bar Bulk Action tidak tampil sebelum ada baris tercentang
77. Centang baris `Peminjam1 P`
78. Verifikasi bar Bulk Action tampil dengan counter `1 Draft selected`
79. Verifikasi checkbox header berstatus indeterminate
80. Centang baris `Peminjam2 P`
81. Verifikasi counter `2 Drafts selected` tampil pada bar
82. Klik checkbox header
83. Verifikasi counter `10 Drafts selected` tampil pada bar
84. Klik halaman 2 pada paginasi
85. Verifikasi counter `10 Drafts selected` tetap tampil pada bar
86. Klik `✕` pada bar
87. Verifikasi bar Bulk Action tidak tampil sebelum ada baris tercentang

### Cancel dialog Bulk Delete tidak memproses apa pun
88. Tampilkan Tabel Drafts dengan kondisi K5
89. Centang baris `Peminjam1 P`
90. Centang baris `Peminjam2 P`
91. Klik `Bulk Action` pada bar
92. Verifikasi menu memuat aksi `Delete`
93. Klik `Delete`
94. Verifikasi judul `Delete Drafts` tampil pada dialog
95. Verifikasi pertanyaan `Are you sure you want to delete them?` tampil pada dialog
96. Klik `[Go Back]`
97. Verifikasi counter `2 Drafts selected` tetap tampil pada bar sesudah dialog ditutup

### Seleksi bersih sesudah Bulk Delete selesai
98. Tampilkan Tabel Drafts dengan kondisi K6
99. Centang baris `Peminjam1 P`
100. Centang baris `Peminjam2 P`
101. Klik `Bulk Action` pada bar
102. Klik `Delete`
103. Klik `[Delete]`
104. Verifikasi toast `Success, draft has been deleted.` tampil
105. Verifikasi bar Bulk Action tidak tampil sesudah aksi selesai

### Bulk Delete gagal karena error server
106. Tampilkan Tabel Drafts dengan kondisi K7
107. Centang baris `Peminjam1 P`
108. Centang baris `Peminjam2 P`
109. Klik `Bulk Action` pada bar
110. Klik `Delete`
111. Klik `[Delete]`
112. Verifikasi toast `Error, failed to delete draft.` tampil
113. Verifikasi bar Bulk Action tetap tampil dengan counter `2 Drafts selected`

### Bulk Delete gagal karena koneksi terputus
114. Tampilkan Tabel Drafts dengan kondisi K8
115. Centang baris `Peminjam1 P`
116. Centang baris `Peminjam2 P`
117. Klik `Bulk Action` pada bar
118. Klik `Delete`
119. Klik `[Delete]`
120. Verifikasi toast `Connection problem. Please try again.` tampil sesudah Bulk Delete gagal
121. Verifikasi bar Bulk Action tetap tampil dengan counter `2 Drafts selected`

### Select All dipotong ke Selection Limit
122. Tampilkan Tabel Drafts dengan kondisi K9
123. Centang baris `Peminjam1 P`
124. Klik `Select All (1500 records)`
125. Verifikasi toast `Error, only the first 1000 of 1500 rows were selected. Narrow your filter to include the rest.` tampil
126. Verifikasi counter `1000 Drafts selected` tampil pada bar
127. Isi nomor halaman dengan `101`, tekan Enter
128. Arahkan kursor ke checkbox salah satu baris pada halaman 101
129. Verifikasi checkbox baris itu disabled dengan tooltip `You've reached the maximum selection of 1000 rows.`

[^drift-1]: Drift PRD vs foundation. PRD §4.1l (T-BRW-20 Setup Column, kolom Borrower): Toggle `☐ Always visible (checked, disabled)`. foundation `prd-conventions.md` §9.3: tidak ada kolom Locked, semua kolom data Hideable (`☑ Hideable (checked, enabled)`), dan satu-satunya guard adalah kolom visible terakhir. Diasersi: foundation, karena Setup Column adalah pola bersama (SB-4).
