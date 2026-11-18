---
id: TC-FA-ASSIGN-E2E-054-add-to-assignment-draft-dari-asset-list-dep-asset-list
title: "Add to Assignment Draft dari Asset List"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-ASG-02, "§4.1#r5", TS-ASG-02, EC-ASG-66, "§9.6#r14"]
smoke: []
dependsOn: ["Asset List: aksi Add to Assignment Draft"]
trace:
  T-ASG-02: [8, 10, 13, 22, 23, 24, 25, 26, 27, 28, 30, 35, 37, 64, 66, 67, 103, 105, 107, 109, 110, 115, 116, 119, 120, 130, 131, 132, 143, 145, 149, 150]
  "§4.1#r5": [7, 21]
  TS-ASG-02: [32, 49, 61, 76, 92, 95]
  EC-ASG-66: [21, 76, 79, 130]
  "§9.6#r14": [49, 52]
anchor: []
coverage:
  web: automated
---

# Add to Assignment Draft dari Asset List

## Prerequisites
- Aktor:
  - Aktor A: Aktor Assignment (Total Control).
  - Aktor B: Asset Admin dengan cakupan Group `Head Office {runId}`, dipakai pada blok terakhir.
- Layar awal: Asset List.
- Data:
  - DU-054-1: Karyawan `Rina Wijaya {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, punya dua Draft yang bisa diedit (DU-054-4 dan DU-054-5).
  - DU-054-2: Karyawan `Hendra Kusuma {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, punya satu Draft yang bisa diedit (DU-054-6).
  - DU-054-3: Karyawan `Maya Putri {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, belum punya Draft.
  - DU-054-4: Draft Assignee `Rina Wijaya {runId}`, Group `Head Office {runId}`, berisi aset `Proyektor Epson EB-X49 {runId}` dengan Purpose `Presentasi klien`, Total Asset `1`; dibuat lebih dulu daripada DU-054-5.
  - DU-054-5: Draft Assignee `Rina Wijaya {runId}`, Group `Branch Surabaya {runId}`, berisi aset `Kamera Canon EOS 200D {runId}` dan `Tripod Manfrotto 190 {runId}` dengan Purpose `Dokumentasi acara`, Total Asset `2`; dibuat sesudah DU-054-4.
  - DU-054-6: Draft Assignee `Hendra Kusuma {runId}`, Group `Head Office {runId}`, berisi aset `Router TP-Link Archer C6 {runId}` dengan Purpose `Jaringan kantor`, Total Asset `1`.
  - DU-054-7: Aset `Scanner Epson DS-530 {runId}`, Custody `Available`, Condition `Normal`, Group `Head Office {runId}`.
  - DU-054-8: Aset `Tablet Samsung Galaxy Tab S9 {runId}`, Custody `Available`, Condition `Normal`, Group `Head Office {runId}`.
  - DU-054-9: Aset `Mouse Logitech MX Master 3 {runId}`, Custody `Available`, Condition `Normal`, Group `Head Office {runId}`.
  - DU-054-10: Aset `Headset Jabra Evolve2 65 {runId}`, Custody `Available`, Condition `Normal`, Group `Head Office {runId}`.
  - DU-054-11: Aset `Speaker Bluetooth JBL Flip 6 {runId}`, Custody `Available`, Condition `Normal`, Group `Head Office {runId}`.
  - DU-054-12: Aset `Webcam Logitech C920 {runId}`, Custody `Available`, Condition `Normal`, Group `Head Office {runId}`.
  - DU-054-13: Aktor B `Tono Prasetyo {runId}`, Asset Admin, cakupan Group `Head Office {runId}`.
  - DU-054-14: Group `Head Office {runId}`, milik spec ini, berisi aset DU-054-7 sampai DU-054-12.
  - DU-054-15: Group `Branch Surabaya {runId}`, milik spec ini, bukan bagian cakupan Aktor B.
- Kondisi:
  - Akun Aktor B aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Dialog Add to Assignment Draft untuk Assignee dengan satu Draft, Cancel tidak mengubah data
1. Ketik Search `Scanner Epson DS-530 {runId}`, tekan Enter
2. Klik `⋯` pada baris `Scanner Epson DS-530 {runId}`
3. Klik `Add to Assignment Draft`
4. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
5. Pilih baris `Hendra Kusuma {runId}`
6. Klik `[Select]`
7. Verifikasi dialog `Add to Assignment Draft` tampil
8. Verifikasi subjudul dialog `[Assignee] has 1 draft you can edit.` dengan Assignee `Hendra Kusuma {runId}`
9. Klik `[Cancel]`
10. Verifikasi dialog `Add to Assignment Draft` tertutup dan baris `Scanner Epson DS-530 {runId}` tampil di Asset List
11. Buka tab Drafts di halaman Transactions > Assignment
12. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
13. Verifikasi Draft `Hendra Kusuma {runId}` tetap memiliki Total Asset `1`

### Dialog untuk Assignee dengan beberapa Draft memuat kolom dan tombol aksi
14. Buka halaman Asset List
15. Ketik Search `Scanner Epson DS-530 {runId}`, tekan Enter
16. Klik `⋯` pada baris `Scanner Epson DS-530 {runId}`
17. Klik `Add to Assignment Draft`
18. Ketik Search `Rina Wijaya {runId}`, tekan Enter
19. Pilih baris `Rina Wijaya {runId}`
20. Klik `[Select]`
21. Verifikasi dialog `Add to Assignment Draft` tampil dengan daftar Draft untuk Assignee `Rina Wijaya {runId}`
22. Verifikasi subjudul dialog `[Assignee] has [N] drafts you can edit.` dengan Assignee `Rina Wijaya {runId}` dan jumlah `2`
23. Verifikasi kolom `Group`, `Total Asset`, `Modified By`, dan `Last Updated` tampil pada tabel dialog
24. Verifikasi kolom `Assignee` tidak tampil pada tabel dialog
25. Verifikasi kotak Search dialog memakai placeholder `Search group or modified by...`
26. Verifikasi baris pertama tabel dialog dengan Group `Branch Surabaya {runId}` karena Draft terbaru tampil dulu menurut `Last Updated`
27. Verifikasi tombol `[New Draft]` dan `[Cancel]` tampil di footer dialog
28. Verifikasi tombol `[Add to Assignment Draft]` disabled sebelum Draft dipilih

### Add ke Draft terpilih menambahkan aset dan mewarisi Purpose baris terakhir
29. Pilih baris Draft dengan Group `Head Office {runId}`
30. Verifikasi tombol `[Add to Assignment Draft]` aktif setelah Draft dipilih
31. Klik `[Add to Assignment Draft]`
32. Verifikasi toast `Success, 1 asset has been added to the draft.` tampil setelah Draft terpilih ditambahkan
33. Buka tab Drafts di halaman Transactions > Assignment
34. Ketik Search `Rina Wijaya {runId}`, tekan Enter
35. Verifikasi Draft `Rina Wijaya {runId}` dengan Group `Head Office {runId}` memiliki Total Asset `2`
36. Klik ikon `Edit` pada baris Draft `Rina Wijaya {runId}` dengan Group `Head Office {runId}`
37. Verifikasi aset `Scanner Epson DS-530 {runId}` ada di tabel aset Draft dengan Purpose `Presentasi klien`
38. Klik `[Cancel]` pada form Draft yang belum diubah

### Aset yang sudah ada di Draft dilewati dan Draft tidak bertambah dua kali
39. Buka halaman Asset List
40. Ketik Search `{runId}`, tekan Enter
41. Centang baris `Scanner Epson DS-530 {runId}`
42. Centang baris `Tablet Samsung Galaxy Tab S9 {runId}`
43. Klik `Add to Assignment Draft` pada menu aksi bulk
44. Ketik Search `Rina Wijaya {runId}`, tekan Enter
45. Pilih baris `Rina Wijaya {runId}`
46. Klik `[Select]`
47. Pilih baris Draft dengan Group `Head Office {runId}`
48. Klik `[Add to Assignment Draft]`
49. Verifikasi toast memuat `Success, 1 asset has been added to the draft.` dan `1 was already in it.`
50. Buka tab Drafts di halaman Transactions > Assignment
51. Ketik Search `Rina Wijaya {runId}`, tekan Enter
52. Verifikasi Draft `Rina Wijaya {runId}` dengan Group `Head Office {runId}` memiliki Total Asset `3`

### New Draft membuat Draft baru berisi aset terpilih dengan Purpose kosong
53. Buka halaman Asset List
54. Ketik Search `Mouse Logitech MX Master 3 {runId}`, tekan Enter
55. Klik `⋯` pada baris `Mouse Logitech MX Master 3 {runId}`
56. Klik `Add to Assignment Draft`
57. Ketik Search `Rina Wijaya {runId}`, tekan Enter
58. Pilih baris `Rina Wijaya {runId}`
59. Klik `[Select]`
60. Klik `[New Draft]`
61. Verifikasi toast `Success, 1 asset has been added to the draft.` muncul setelah Draft baru dibuat
62. Buka tab Drafts di halaman Transactions > Assignment
63. Ketik Search `Rina Wijaya {runId}`, tekan Enter
64. Verifikasi tab Drafts memuat tiga Draft untuk Assignee `Rina Wijaya {runId}`
65. Klik ikon `Edit` pada baris Draft `Rina Wijaya {runId}` dengan Group `Head Office {runId}` dan Total Asset `1`
66. Verifikasi aset `Mouse Logitech MX Master 3 {runId}` ada di tabel aset Draft baru
67. Verifikasi Purpose pada baris aset `Mouse Logitech MX Master 3 {runId}` kosong dengan placeholder `Enter purpose`
68. Klik `[Cancel]` pada form Draft yang belum diubah

### Assignee tanpa Draft yang bisa diedit langsung dibuatkan Draft baru
69. Buka halaman Asset List
70. Ketik Search `Headset Jabra Evolve2 65 {runId}`, tekan Enter
71. Klik `⋯` pada baris `Headset Jabra Evolve2 65 {runId}`
72. Klik `Add to Assignment Draft`
73. Ketik Search `Maya Putri {runId}`, tekan Enter
74. Pilih baris `Maya Putri {runId}`
75. Klik `[Select]`
76. Verifikasi toast `Success, 1 asset has been added to the draft.` tampil tanpa dialog `Add to Assignment Draft`
77. Buka tab Drafts di halaman Transactions > Assignment
78. Ketik Search `Maya Putri {runId}`, tekan Enter
79. Verifikasi Draft untuk Assignee `Maya Putri {runId}` tampil dengan Total Asset `1`

### Add ke Draft dengan dua aset baru dan dua aset yang sudah ada memakai bentuk jamak pada toast
80. Buka halaman Asset List
81. Ketik Search `{runId}`, tekan Enter
82. Centang baris `Scanner Epson DS-530 {runId}`
83. Centang baris `Tablet Samsung Galaxy Tab S9 {runId}`
84. Centang baris `Speaker Bluetooth JBL Flip 6 {runId}`
85. Centang baris `Webcam Logitech C920 {runId}`
86. Klik `Add to Assignment Draft` pada menu aksi bulk
87. Ketik Search `Rina Wijaya {runId}`, tekan Enter
88. Pilih baris `Rina Wijaya {runId}`
89. Klik `[Select]`
90. Pilih baris Draft dengan Group `Head Office {runId}` dan Total Asset `3`
91. Klik `[Add to Assignment Draft]`
92. Verifikasi toast memuat `Success, 2 assets have been added to the draft.` dan `2 were already in it.`
93. Buka tab Drafts di halaman Transactions > Assignment
94. Ketik Search `Rina Wijaya {runId}`, tekan Enter
95. Verifikasi Draft `Rina Wijaya {runId}` dengan Group `Head Office {runId}` memiliki Total Asset `5`

### Dialog Add to Assignment Draft: urutan Total Asset, Search Group, Filter, dan satu Draft terpilih
96. Buka halaman Asset List
97. Ketik Search `Mouse Logitech MX Master 3 {runId}`, tekan Enter
98. Klik `⋯` pada baris `Mouse Logitech MX Master 3 {runId}`
99. Klik `Add to Assignment Draft`
100. Ketik Search `Rina Wijaya {runId}`, tekan Enter
101. Pilih baris `Rina Wijaya {runId}`
102. Klik `[Select]`
103. Verifikasi subjudul dialog `[Assignee] has [N] drafts you can edit.` dengan Assignee `Rina Wijaya {runId}` dan jumlah `3`
104. Klik header kolom `Total Asset`
105. Verifikasi kolom `Total Asset` terurut dari kecil ke besar: Draft Group `Head Office {runId}` (`1`), Draft Group `Branch Surabaya {runId}` (`2`), Draft Group `Head Office {runId}` (`5`)
106. Klik header kolom `Total Asset` sekali lagi
107. Verifikasi kolom `Total Asset` terurut dari besar ke kecil: Draft Group `Head Office {runId}` (`5`), Draft Group `Branch Surabaya {runId}` (`2`), Draft Group `Head Office {runId}` (`1`)
108. Ketik Search `Branch Surabaya {runId}`, tekan Enter
109. Verifikasi Draft Group `Branch Surabaya {runId}` tampil pada tabel dialog
110. Verifikasi kedua Draft Group `Head Office {runId}` tidak tampil karena Group-nya tidak cocok dengan Search
111. Klik `(←)` pada kotak Search
112. Klik `Filter`
113. Isi `Min` dengan `2` dan `Max` dengan `5` pada field `Total Asset`
114. Klik `[Apply]`
115. Verifikasi Draft Group `Branch Surabaya {runId}` dengan Total Asset `2` dan Draft Group `Head Office {runId}` dengan Total Asset `5` tampil karena Total Asset-nya dalam rentang
116. Verifikasi Draft Group `Head Office {runId}` dengan Total Asset `1` tidak tampil karena di luar rentang
117. Pilih baris Draft Group `Branch Surabaya {runId}`
118. Pilih baris Draft Group `Head Office {runId}` dengan Total Asset `5`
119. Verifikasi baris Draft Group `Head Office {runId}` dengan Total Asset `5` terpilih
120. Verifikasi baris Draft Group `Branch Surabaya {runId}` tidak lagi terpilih karena dialog single-select
121. Klik `[Cancel]`

### Draft di luar cakupan Group aktor tidak dihitung pada dialog
122. Masuk sebagai Aktor B
123. Buka halaman Asset List
124. Ketik Search `Mouse Logitech MX Master 3 {runId}`, tekan Enter
125. Klik `⋯` pada baris `Mouse Logitech MX Master 3 {runId}`
126. Klik `Add to Assignment Draft`
127. Ketik Search `Rina Wijaya {runId}`, tekan Enter
128. Pilih baris `Rina Wijaya {runId}`
129. Klik `[Select]`
130. Verifikasi subjudul dialog `[Assignee] has [N] drafts you can edit.` dengan Assignee `Rina Wijaya {runId}` dan jumlah `2`
131. Verifikasi kedua Draft Group `Head Office {runId}` tampil pada tabel dialog
132. Verifikasi Draft Group `Branch Surabaya {runId}` tidak tampil karena di luar cakupan Aktor B
133. Klik `[Cancel]`

### Dialog Add to Assignment Draft: urutan Group dan saringan Group
134. Masuk sebagai Aktor A
135. Buka halaman Asset List
136. Ketik Search `Mouse Logitech MX Master 3 {runId}`, tekan Enter
137. Klik `⋯` pada baris `Mouse Logitech MX Master 3 {runId}`
138. Klik `Add to Assignment Draft`
139. Ketik Search `Rina Wijaya {runId}`, tekan Enter
140. Pilih baris `Rina Wijaya {runId}`
141. Klik `[Select]`
142. Klik header kolom `Group`
143. Verifikasi baris pertama tabel dialog adalah Draft Group `Branch Surabaya {runId}` karena Group terurut A-Z
144. Klik header kolom `Group` sekali lagi
145. Verifikasi baris terakhir tabel dialog adalah Draft Group `Branch Surabaya {runId}` karena Group terurut Z-A
146. Klik `Filter`
147. Pilih Group `Branch Surabaya {runId}` pada field `Group`
148. Klik `[Apply]`
149. Verifikasi Draft Group `Branch Surabaya {runId}` dengan Total Asset `2` tampil karena Group-nya sesuai saringan
150. Verifikasi kedua Draft Group `Head Office {runId}` tidak tampil karena Group-nya tidak sesuai saringan
151. Klik `[Cancel]`
