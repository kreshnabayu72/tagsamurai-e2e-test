---
id: TC-FA-ASSIGN-UI-106-dialog-select-assignee
title: "Dialog Select Assignee: sub-tab Employees dan Divisions, status Blocked"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-ASG-05, "§4.1#r7", S-ASG-05, S-ASG-22, S-ASG-23, FI-ASG-07, EC-ASG-06, EC-ASG-45, "EB-TBL-9@select-assignee"]
smoke: []
dependsOn: []
trace:
  T-ASG-05: [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 23, 24, 26, 28, 29, 31, 34, 36, 37, 39, 47, 48, 49, 50, 51, 52, 58, 71, 72, 74, 75, 77, 78, 95, 96, 97, 98, 99, 100, 101, 102, 106, 107, 109, 111, 114, 116, 118, 122, 124, 125]
  "§4.1#r7": 3
  S-ASG-05: [65, 66, 68, 69]
  S-ASG-22: [80, 81, 88, 89]
  S-ASG-23: [84, 85, 91, 92]
  FI-ASG-07: [54, 56]
  EC-ASG-06: 53
  EC-ASG-45: [20, 21]
  "EB-TBL-9@select-assignee": [41, 43, 44, 62, 63]
anchor: [19]
coverage:
  web: automated
---
# Dialog Select Assignee: sub-tab Employees dan Divisions, status Blocked

## Prerequisites
- Aktor: Asset Admin pada Group `Head Office`, yaitu karyawan DU-106-10.
- Layar awal: form Assignment Request dengan dialog Select Assignee dibuka dari tombol `[Select Assignee]`.
- Komponen: Dialog Select Assignee
- Data:
  - DU-106-1: Karyawan `Budi Santoso`, Email `budi.santoso@example.com`, Position `Staff`, Division `IT`, Home Group `Head Office`, Status `Active`, Activation Status `Activated`, Active Assignments `9 assets`, Eligibility `Can be assigned`.
  - DU-106-2: Karyawan `Joko Susilo`, Email `joko.susilo@example.com`, Position `Operator`, Division `Warehouse`, Home Group `—`, Status `Active`, Active Assignments `0 assets`, tanpa akun login sehingga Activation Status tidak dinyatakan, Eligibility `Blocked` dengan alasan `No login account. Only employees who can sign in can be assignees.`.
  - DU-106-3: Karyawan `Sari Dewi`, Email `sari.dewi@example.com`, Position `Analyst`, Division `Finance`, Home Group `Head Office`, Status `Active`, Activation Status `Activated`, Active Assignments `4 assets`, Eligibility `Can be assigned`.
  - DU-106-4: Karyawan `Budi Setiawan`, Email `budi.setiawan@example.com`, Position `Analyst`, Division `Finance`, Home Group `Branch Surabaya`, Status `Active`, Activation Status `Activated`, Active Assignments `2 assets`, Eligibility `Can be assigned`.
  - DU-106-5: Division `Field Survey`, Code `FSV`, Users `6`, Eligibility `Can be assigned`.
  - DU-106-6: Division `Finance`, Code `FIN`, Users `4`, Eligibility `Can be assigned`.
  - DU-106-7: Division `Security`, Code `SEC`, Users `0`, Eligibility `Blocked` dengan alasan `No member can sign in, so no one can be the PIC.`.
  - DU-106-8: Karyawan `Rina Wulandari`, Email `rina.wulandari@example.com`, Position `Analyst`, Division `Finance`, Home Group `Head Office`, Status `Active`, Activation Status `Activated`, Active Assignments `5 assets`, Eligibility `Blocked` karena batas Max assets per assignee tercapai.
  - DU-106-9: Karyawan `Wahyu Pratama`, Email `wahyu.pratama@example.com`, Position `Operator`, Division `Warehouse`, Home Group `Branch Surabaya`, Status `Active`, Activation Status `Activated`, Active Assignments `1 asset`, Eligibility `Can be assigned`.
  - DU-106-10: Karyawan `Dewi Lestari`, Email `dewi.lestari@example.com`, Position `Operations Officer`, Division `Operations`, Home Group `Head Office`, Status `Active`, Activation Status `Activated`, Active Assignments `3 assets`, Eligibility `Can be assigned`.
  - DU-106-12: Karyawan `Rudi Hartono`, Email `rudi.hartono@example.com`, Position `Staff`, Division `Logistics`, Home Group `Floor 1` dengan hierarki lengkap `Head Office > Floor 1`, Status `Active`, Activation Status `Activated`, Active Assignments `1 asset` dengan aset yang sedang ditugaskan `Laptop Dell Latitude 5420 - 10`, Eligibility `Can be assigned`.
  - DU-106-11: Kata kunci Search `Tanpa Hasil` yang tidak cocok dengan baris mana pun.
- Kondisi:
  - K1: level Full; form belum memuat aset; sub-tab `Employees` aktif; daftar berisi DU-106-1 sampai DU-106-4, DU-106-8, DU-106-9, dan DU-106-10.
  - K2: seperti K1; daftar sub-tab `Divisions` berisi DU-106-5 sampai DU-106-7.
  - K3: level Full; semua aset di form tidak mengizinkan tipe Division; daftar berisi DU-106-1.
  - K4: level Full; semua aset di form tidak mengizinkan tipe Employee; daftar `Divisions` berisi DU-106-5.
  - K5: dialog dibuka dari form dengan Assignee Type `Employee` yang dipilih di overlay Assign to; daftar berisi DU-106-1 sampai DU-106-4.
  - K6: dialog dibuka dari form dengan Assignee Type `Division` yang dipilih di overlay Assign to; daftar berisi DU-106-5 sampai DU-106-7.
  - K7: level Basic; daftar berisi DU-106-1 sampai DU-106-4.
  - K8: tidak ada karyawan yang bisa menjadi Assignee; daftar `Employees` kosong.
  - K9: tidak ada Division yang bisa menjadi Assignee; daftar `Divisions` kosong.
  - K11: level Full; form belum memuat aset; sub-tab `Employees` aktif; daftar berisi DU-106-12.
  - K10: seperti K1; Search DU-106-11 tidak menemukan baris mana pun pada sub-tab `Employees` maupun `Divisions`.

## Test Steps

### Sub-tab Employees: toolbar, kolom, dan isi baris
1. Tampilkan Dialog Select Assignee dengan kondisi K1
2. Verifikasi sub-tab `Employees` dan `Divisions` tampil karena form belum memuat aset
3. Verifikasi toolbar dialog Select Assignee memuat Search dan Filter
4. Verifikasi kotak Search dialog Select Assignee memuat placeholder `Search name or email...`
5. Verifikasi kolom `Name`, `Email`, `Position`, `Division`, `Home Group`, `Status`, `Active Assignments`, dan `Eligibility` tampil
6. Verifikasi kolom `Activation Status`, `Temporary User`, `Temporary Until`, dan `TAG` tidak tampil
7. Verifikasi baris `Budi Santoso` menampilkan Email `budi.santoso@example.com`
8. Verifikasi baris `Budi Santoso` menampilkan Position `Staff`
9. Verifikasi baris `Budi Santoso` menampilkan kolom `Division` bernilai `IT`
10. Verifikasi baris `Budi Santoso` menampilkan Home Group `Head Office`
11. Verifikasi baris `Budi Santoso` menampilkan Active Assignments `9 assets`
12. Verifikasi baris `Budi Santoso` menampilkan Eligibility `Can be assigned`
13. Verifikasi baris `Joko Susilo` menampilkan Home Group `—`
14. Verifikasi baris `Joko Susilo` menampilkan Active Assignments `0 assets`
15. Verifikasi baris `Wahyu Pratama` menampilkan Active Assignments `1 asset`
16. Verifikasi baris `Sari Dewi` dan `Budi Setiawan` tampil sebagai dua baris terpisah dengan Email berbeda

### Hanya karyawan Active dan Activated yang menjadi kandidat
17. Tampilkan Dialog Select Assignee dengan kondisi K1
18. Centang `Activation Status` pada Setup Column
19. Verifikasi baris `Budi Santoso` tampil bersama kolom `Activation Status`
20. Verifikasi setiap baris menampilkan Status `Active`
21. Verifikasi baris `Budi Santoso`, `Sari Dewi`, `Budi Setiawan`, `Rina Wulandari`, `Wahyu Pratama`, dan `Dewi Lestari` menampilkan Activation Status `Activated`

### Karyawan tanpa akun login tampil Blocked dan tidak bisa dipilih
22. Tampilkan Dialog Select Assignee dengan kondisi K1
23. Verifikasi baris `Joko Susilo` menampilkan Eligibility `Blocked`
24. Verifikasi pilihan baris `Joko Susilo` disabled dan alasan `No login account. Only employees who can sign in can be assignees.` tersampaikan padanya
25. Klik pilihan baris `Joko Susilo`
26. Verifikasi baris `Joko Susilo` tidak terpilih

### Batas Max assets per assignee tercapai membuat baris Blocked
27. Tampilkan Dialog Select Assignee dengan kondisi K1
28. Verifikasi baris `Rina Wulandari` menampilkan Eligibility `Blocked`
29. Verifikasi pilihan baris `Rina Wulandari` disabled dan alasan batas Max assets per assignee tersampaikan padanya
30. Klik pilihan baris `Rina Wulandari`
31. Verifikasi baris `Rina Wulandari` tidak terpilih

### Single-select: memilih baris baru melepas baris sebelumnya, termasuk Aktor sendiri
32. Tampilkan Dialog Select Assignee dengan kondisi K1
33. Pilih baris `Budi Santoso`
34. Verifikasi baris `Budi Santoso` terpilih
35. Pilih baris `Sari Dewi`
36. Verifikasi baris `Sari Dewi` terpilih
37. Verifikasi baris `Budi Santoso` tidak lagi terpilih
38. Pilih baris `Dewi Lestari`
39. Verifikasi baris `Dewi Lestari` terpilih karena Aktor boleh memilih dirinya sendiri sebagai Assignee

### Konfirmasi tanpa pilihan pada sub-tab Employees
40. Tampilkan Dialog Select Assignee dengan kondisi K1
41. Verifikasi tombol konfirmasi dialog enabled
42. Klik tombol konfirmasi dialog
43. Verifikasi pesan error inline `You must pick a user` tampil di atas tombol footer
44. Verifikasi dialog Select Assignee tetap terbuka karena pilihan tidak dikirim

### Sub-tab Divisions: kolom, isi baris, dan Division tanpa anggota ber-akun login
45. Tampilkan Dialog Select Assignee dengan kondisi K2
46. Klik sub-tab `Divisions`
47. Verifikasi kotak Search memuat placeholder `Search division...`
48. Verifikasi kolom `Division`, `Code`, `Users`, dan `Eligibility` tampil
49. Verifikasi baris `Finance` menampilkan Code `FIN`
50. Verifikasi baris `Finance` menampilkan Users `4`
51. Verifikasi baris `Finance` menampilkan Eligibility `Can be assigned`
52. Verifikasi baris `Security` menampilkan Users `0`
53. Verifikasi baris `Security` menampilkan Eligibility `Blocked`
54. Verifikasi pilihan baris `Security` disabled dan alasan `No member can sign in, so no one can be the PIC.` tersampaikan padanya
55. Klik pilihan baris `Security`
56. Verifikasi baris `Security` tidak terpilih
57. Pilih baris `Finance`
58. Verifikasi baris `Finance` terpilih

### Konfirmasi tanpa pilihan pada sub-tab Divisions
59. Tampilkan Dialog Select Assignee dengan kondisi K2
60. Klik sub-tab `Divisions`
61. Klik tombol konfirmasi dialog
62. Verifikasi pesan error inline `You must pick an item` tampil di atas tombol footer[^drift-1]
63. Verifikasi dialog Select Assignee tetap terbuka karena pilihan tidak dikirim

### Sub-tab Divisions yang tidak diizinkan semua aset konteks disembunyikan
64. Tampilkan Dialog Select Assignee dengan kondisi K3
65. Verifikasi sub-tab `Employees` tampil
66. Verifikasi sub-tab `Divisions` tidak tampil

### Sub-tab Employees yang tidak diizinkan semua aset konteks disembunyikan
67. Tampilkan Dialog Select Assignee dengan kondisi K4
68. Verifikasi sub-tab `Divisions` tampil
69. Verifikasi sub-tab `Employees` tidak tampil

### Assignee Type Employee sudah dipilih: tanpa sub-tab
70. Tampilkan Dialog Select Assignee dengan kondisi K5
71. Verifikasi baris `Budi Santoso` tampil
72. Verifikasi sub-tab `Employees` dan `Divisions` tidak tampil

### Assignee Type Division sudah dipilih: tanpa sub-tab
73. Tampilkan Dialog Select Assignee dengan kondisi K6
74. Verifikasi baris `Finance` tampil
75. Verifikasi sub-tab `Employees` dan `Divisions` tidak tampil

### Level Basic: hanya Employees tanpa sub-tab
76. Tampilkan Dialog Select Assignee dengan kondisi K7
77. Verifikasi baris `Budi Santoso` tampil
78. Verifikasi sub-tab `Employees` dan `Divisions` tidak tampil

### Empty state sub-tab Employees
79. Tampilkan Dialog Select Assignee dengan kondisi K8
80. Verifikasi empty state memuat judul `No employees available`
81. Verifikasi empty state memuat teks `There are no employees who can sign in.`

### Empty state sub-tab Divisions
82. Tampilkan Dialog Select Assignee dengan kondisi K9
83. Klik sub-tab `Divisions`
84. Verifikasi empty state memuat judul `No divisions available`
85. Verifikasi empty state memuat teks `There are no divisions to assign to.`

### Empty state akibat Search tanpa hasil
86. Tampilkan Dialog Select Assignee dengan kondisi K10
87. Ketik Search `Tanpa Hasil`, tekan Enter
88. Verifikasi empty state sub-tab Employees memuat judul `No results found`
89. Verifikasi empty state sub-tab Employees memuat teks `Try adjusting your search or filter.`
90. Klik sub-tab `Divisions`
91. Verifikasi empty state sub-tab Divisions memuat judul `No results found`
92. Verifikasi empty state sub-tab Divisions memuat teks `Try adjusting your search or filter.`

### Filter Panel sub-tab Employees memuat field menurut kolom yang dapat difilter
93. Tampilkan Dialog Select Assignee dengan kondisi K1
94. Klik ikon Filter
95. Verifikasi Filter Panel dialog Select Assignee memuat field `Position` dengan placeholder `All positions`
96. Verifikasi Filter Panel dialog Select Assignee memuat field `Division` dengan placeholder `All divisions`
97. Verifikasi Filter Panel dialog Select Assignee memuat field `Home Group` dengan placeholder `All home groups`
98. Verifikasi Filter Panel dialog Select Assignee memuat field rentang `Active Assignments` dengan placeholder `Min` dan `Max`
99. Verifikasi Filter Panel dialog Select Assignee memuat field `Eligibility` dengan placeholder `All eligibility`
100. Verifikasi Filter Panel dialog Select Assignee memuat field `Activation Status` dengan placeholder `All statuses`
101. Verifikasi Filter Panel dialog Select Assignee memuat field `Temporary User` dengan placeholder `All options`
102. Verifikasi Filter Panel dialog Select Assignee memuat field `Temporary Until` dengan placeholder `Select date`

### Filter Panel sub-tab Divisions memuat field menurut kolom yang dapat difilter
103. Tampilkan Dialog Select Assignee dengan kondisi K2
104. Klik sub-tab `Divisions`
105. Klik ikon Filter
106. Verifikasi Filter Panel dialog Select Assignee memuat field rentang `Users` dengan placeholder `Min` dan `Max`
107. Verifikasi Filter Panel dialog Select Assignee memuat field `Eligibility` dengan placeholder `All eligibility`

### Kolom yang dapat diurutkan pada kedua sub-tab
108. Tampilkan Dialog Select Assignee dengan kondisi K1
109. Verifikasi header kolom `Name`, `Email`, `Position`, `Division`, `Home Group`, `Status`, `Active Assignments`, dan `Eligibility` dapat diurutkan
110. Klik sub-tab `Divisions`
111. Verifikasi header kolom `Division`, `Code`, `Users`, dan `Eligibility` dapat diurutkan

### Hover Home Group dan Active Assignments
112. Tampilkan Dialog Select Assignee dengan kondisi K11
113. Arahkan kursor ke badge Home Group pada baris `Rudi Hartono`
114. Verifikasi hover Home Group menyampaikan hierarki lengkap `Head Office > Floor 1`
115. Arahkan kursor ke Active Assignments pada baris `Rudi Hartono`
116. Verifikasi hover Active Assignments menyampaikan daftar aset yang sedang ditugaskan `Laptop Dell Latitude 5420 - 10`

### Avatar pada kolom Name
117. Tampilkan Dialog Select Assignee dengan kondisi K1
118. Verifikasi baris `Budi Santoso` menampilkan avatar bersama nama lengkap `Budi Santoso` pada kolom `Name`

### Setup Column sub-tab Divisions
119. Tampilkan Dialog Select Assignee dengan kondisi K2
120. Klik sub-tab `Divisions`
121. Buka Setup Column
122. Verifikasi kolom `Division`, `Code`, `Users`, dan `Eligibility` masing-masing dapat disembunyikan lewat Setup Column
123. Hapus centang `Users` pada Setup Column
124. Verifikasi kolom `Division`, `Code`, dan `Eligibility` tetap tampil
125. Verifikasi kolom `Users` tidak tampil

[^drift-1]: Drift PRD vs foundation. PRD §4.1e (T-ASG-05): tidak menetapkan copy error konfirmasi tanpa pilihan untuk sub-tab Divisions. foundation `prd-conventions.md` §37.2: pemilihan Item atau generik memakai `You must pick an item`. Diasersi: foundation, karena error konfirmasi picker adalah pola bersama (SB-4).
