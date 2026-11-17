---
id: TC-FA-FATR-UI-059-area-borrow
title: "Area utama: field tab Borrow"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules:
  - §4.1#r66
  - §4.1#r67
  - §4.1#r68
  - §4.1#r69
  - §4.1#r70
  - §4.1#r71
  - §4.1#r72
  - §4.1#r98
  - §4.1#r171
  - §4.1#r173
  - §4.1#r187
  - §4.1#r192
  - §4.1#r188
  - §4.1#r190
  - §4.1#r189
  - §4.1#r209
  - §4.1#r210
  - §4.1#r221
  - §9.2#b400
  - §9.2#b423
  - §9.4.2#r8
  - §9.4.1#r11
smoke: []
dependsOn: []
trace:
  §4.1#r66: [2, 4, 104]
  §4.1#r67: [6, 8, 98, 106]
  §4.1#r68: [10, 23, 108]
  §4.1#r69: [11, 110]
  §4.1#r70: [12, 67, 74, 101, 112]
  §4.1#r71: [13, 15, 68, 75, 114]
  §4.1#r72: [17, 19, 69, 76, 116]
  §4.1#r98: [24, 25]
  §4.1#r171: [45, 70, 77, 118]
  §4.1#r173: [46, 71, 78, 120]
  §4.1#r187: [48, 88, 90, 122]
  §4.1#r192: [49, 51, 81, 84, 124]
  §4.1#r188: [53, 92, 94, 126]
  §4.1#r190: [21, 55, 58, 86, 96, 98, 130]
  §4.1#r189: [54, 57, 82, 85, 128]
  §4.1#r209: [60, 100, 132]
  §4.1#r210: [61, 63, 72, 79, 134]
  §4.1#r221: [65, 136]
  §9.2#b400: [29, 31, 37, 39]
  §9.2#b423: [45, 46]
  §9.4.2#r8: [29, 31, 32, 37, 39, 40, 43]
  §9.4.1#r11: [31, 39]
anchor: [28, 36, 42, 57]
coverage:
  web: automated
---

# Area utama: field tab Borrow

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-059-1: Pengaturan Company default tab Borrow pada All categories: Allow Borrow `Allow`, Duration unit `Days`, Max duration `14`, Max extensions `1`, Max assets per borrower (concurrent) `3`, Allowed borrower `Employee in any Group`, Block new borrow when overdue `ON`, Photo at start `ON`, Photo at end `ON`, Require approval `ON`, Approval type `Any one approver`, Self service `OFF`, Auto-approve `ON`, Auto-approve when duration ≤ `3`, Transaction timeout `7`, Due date reminders `D-3, D-1, D-day`, Send email notifications `ON`.
  - DU-059-2: Nilai Max duration yang dicoba: `365` dan `366` untuk Duration unit `Days`, `8760` dan `8761` untuk Duration unit `Hours`.
  - DU-059-3: Pengaturan Category leaf `Machinery`: semua field Inherit, Max duration Company default `400` dengan Duration unit `Days`.
  - DU-059-4: Pengaturan Company default tab Borrow pada All categories yang berbeda dari nilai awal: Max assets per borrower (concurrent) `5`, Allowed borrower `Same Group only`, Block new borrow when overdue `OFF`, Photo at start `OFF`, Photo at end `OFF`, Due date reminders `D-day only`.
  - DU-059-5: Pengaturan Company default tab Borrow pada All categories yang berbeda dari nilai awal: Require approval `ON`, Approval type `All approvers (AND)`, Self service `OFF`, Auto-approve `OFF`, Auto-approve when duration ≤ tersimpan `5`.
  - DU-059-6: Pengaturan Company default tab Borrow pada All categories yang berbeda dari nilai awal: Require approval `OFF`, Self service `OFF`.
  - DU-059-7: Pengaturan Company default tab Borrow pada All categories yang berbeda dari nilai awal: Self service `ON`.
- Kondisi:
  - K1: node All categories terpilih, tab Borrow aktif, Approval Workflow tersedia di plan, level Feature Suite Borrowing `Full`, nilai Company default memakai DU-059-1.
  - K2: node Category leaf `Machinery` terpilih, tab Borrow aktif, nilai memakai DU-059-3.
  - K3: node All categories terpilih, tab Borrow aktif, nilai memakai DU-059-4.
  - K4: node All categories terpilih, tab Borrow aktif, nilai memakai DU-059-5.
  - K5: node All categories terpilih, tab Borrow aktif, nilai memakai DU-059-6.
  - K6: node All categories terpilih, tab Borrow aktif, nilai memakai DU-059-7.

## Test Steps

### Eligibility dan Limits Borrow
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi `Allow Borrow` bernilai `Allow`
3. Buka daftar pilihan `Allow Borrow`
4. Verifikasi pilihan `Allow Borrow` adalah `Allow` dan `Deny`
5. Tutup daftar pilihan dengan Escape
6. Verifikasi `Duration unit` bernilai `Days`
7. Buka daftar pilihan `Duration unit`
8. Verifikasi pilihan `Duration unit` adalah `Days` dan `Hours`
9. Tutup daftar pilihan dengan Escape
10. Verifikasi `Max duration` bernilai `14`
11. Verifikasi `Max extensions` bernilai `1`
12. Verifikasi `Max assets per borrower (concurrent)` bernilai `3`
13. Verifikasi `Allowed borrower` bernilai `Employee in any Group`
14. Buka daftar pilihan `Allowed borrower`
15. Verifikasi pilihan `Allowed borrower` adalah `Same Group only`, `Same Division only`, dan `Employee in any Group`
16. Tutup daftar pilihan dengan Escape
17. Verifikasi `Block new borrow when overdue` bernilai `ON`
18. Matikan `Block new borrow when overdue`
19. Verifikasi `Block new borrow when overdue` bernilai `OFF`

### Duration unit diubah tanpa konversi angka
20. Tampilkan Area utama dengan kondisi K1
21. Verifikasi `Auto-approve when duration ≤` bernilai `3`
22. Pilih `Hours` pada `Duration unit`
23. Verifikasi addon `Max duration` menunjukkan satuan yang sama dengan Duration unit `Hours`
24. Verifikasi `Max duration` tetap bernilai `14`
25. Verifikasi `Auto-approve when duration ≤` tetap bernilai `3`

### Peringatan Max duration lebih dari 1 tahun dalam Days
26. Tampilkan Area utama dengan kondisi K1
27. Ganti Max duration menjadi `365`
28. Verifikasi `Max duration` bernilai `365`
29. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tidak ada di bagian `Limits`
30. Ganti Max duration menjadi `366`
31. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tampil di bagian `Limits`
32. Verifikasi tombol `Save` aktif

### Peringatan Max duration lebih dari 1 tahun dalam Hours
33. Tampilkan Area utama dengan kondisi K1
34. Pilih `Hours` pada `Duration unit`
35. Ganti Max duration menjadi `8760`
36. Verifikasi `Max duration` bernilai `8760`
37. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tidak ada di bagian `Limits`
38. Ganti Max duration menjadi `8761`
39. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tampil di bagian `Limits`
40. Verifikasi tombol `Save` aktif

### Peringatan tidak tampil untuk nilai warisan
41. Tampilkan Area utama dengan kondisi K2
42. Verifikasi `Max duration` menampilkan `Inherit — 400 days (from Company default)`
43. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tidak ada di bagian `Limits`

### Evidence Borrow
44. Tampilkan Area utama dengan kondisi K1
45. Verifikasi `Photo at start` bernilai `ON` pada bagian `Evidence`
46. Verifikasi `Photo at end` bernilai `ON` pada bagian `Evidence`

### Approval Borrow
47. Tampilkan Area utama dengan kondisi K1
48. Verifikasi `Require approval` bernilai `ON`
49. Verifikasi `Approval type` bernilai `Any one approver`
50. Buka daftar pilihan `Approval type`
51. Verifikasi pilihan `Approval type` adalah `Any one approver` dan `All approvers (AND)`
52. Tutup daftar pilihan dengan Escape
53. Verifikasi `Self service` bernilai `OFF`
54. Verifikasi `Auto-approve` bernilai `ON`
55. Verifikasi `Auto-approve when duration ≤` tampil dengan nilai `3`
56. Matikan `Auto-approve`
57. Verifikasi `Auto-approve` bernilai `OFF`
58. Verifikasi `Auto-approve when duration ≤` tidak ada

### Reminders dan Notifications Borrow
59. Tampilkan Area utama dengan kondisi K1
60. Verifikasi `Transaction timeout` bernilai `7`
61. Verifikasi `Due date reminders` bernilai `D-3, D-1, D-day`
62. Buka daftar pilihan `Due date reminders`
63. Verifikasi pilihan `Due date reminders` adalah `D-3, D-1, D-day`, `D-1, D-day`, dan `D-day only`
64. Tutup daftar pilihan dengan Escape
65. Verifikasi `Send email notifications` bernilai `ON`

### Reset to Default mengembalikan Limits, Evidence, dan Reminders Borrow ke nilai awal
66. Tampilkan Area utama dengan kondisi K3
67. Verifikasi `Max assets per borrower (concurrent)` bernilai `5`
68. Verifikasi `Allowed borrower` bernilai `Same Group only`
69. Verifikasi `Block new borrow when overdue` bernilai `OFF`
70. Verifikasi `Photo at start` bernilai `OFF` pada bagian `Evidence`
71. Verifikasi `Photo at end` bernilai `OFF` pada bagian `Evidence`
72. Verifikasi `Due date reminders` bernilai `D-day only`
73. Klik `Reset to Default`
74. Verifikasi `Max assets per borrower (concurrent)` kembali ke nilai awal `3`
75. Verifikasi `Allowed borrower` kembali ke nilai awal `Employee in any Group`
76. Verifikasi `Block new borrow when overdue` kembali ke nilai awal `ON`
77. Verifikasi `Photo at start` kembali ke nilai awal `ON` pada bagian `Evidence`
78. Verifikasi `Photo at end` kembali ke nilai awal `ON` pada bagian `Evidence`
79. Verifikasi `Due date reminders` kembali ke nilai awal `D-3, D-1, D-day`

### Reset to Default mengembalikan Approval type dan Auto-approve Borrow ke nilai awal
80. Tampilkan Area utama dengan kondisi K4
81. Verifikasi `Approval type` bernilai `All approvers (AND)`
82. Verifikasi `Auto-approve` bernilai `OFF`
83. Klik `Reset to Default`
84. Verifikasi `Approval type` kembali ke nilai awal `Any one approver`
85. Verifikasi `Auto-approve` kembali ke nilai awal `ON`
86. Verifikasi `Auto-approve when duration ≤` tampil dengan nilai awal `3`

### Reset to Default mengembalikan Require approval Borrow ke nilai awal
87. Tampilkan Area utama dengan kondisi K5
88. Verifikasi `Require approval` bernilai `OFF`
89. Klik `Reset to Default`
90. Verifikasi `Require approval` kembali ke nilai awal `ON`

### Reset to Default mengembalikan Self service Borrow ke nilai awal
91. Tampilkan Area utama dengan kondisi K6
92. Verifikasi `Self service` tampil dengan nilai `ON` sebelum Reset to Default
93. Klik `Reset to Default`
94. Verifikasi `Self service` kembali ke nilai awal `OFF`

### Satuan addon Auto-approve when duration ≤ mengikuti Duration unit
95. Tampilkan Area utama dengan kondisi K1
96. Verifikasi addon `Auto-approve when duration ≤` menunjukkan satuan yang sama dengan Duration unit `Days`
97. Pilih `Hours` pada `Duration unit`
98. Verifikasi addon `Auto-approve when duration ≤` menunjukkan satuan yang sama dengan Duration unit `Hours`

### Satuan field angka tab Borrow
99. Tampilkan Area utama dengan kondisi K1
100. Verifikasi addon `Transaction timeout` menunjukkan satuan `days`
101. Verifikasi addon `Max assets per borrower (concurrent)` menunjukkan satuan `assets`

### Teks bantuan label field tab Borrow
102. Tampilkan Area utama dengan kondisi K1
103. Pindahkan fokus keyboard ke bantuan label `Allow Borrow`
104. Verifikasi teks bantuan label `Allow Borrow` tersampaikan berbunyi `Whether this transaction can be made for assets in this category.`
105. Pindahkan fokus keyboard ke bantuan label `Duration unit`
106. Verifikasi teks bantuan label `Duration unit` tersampaikan berbunyi `Unit used for Max duration and Auto-approve when duration ≤.`
107. Pindahkan fokus keyboard ke bantuan label `Max duration`
108. Verifikasi teks bantuan label `Max duration` tersampaikan berbunyi `Longest total borrow time from handover, including all extensions.`
109. Pindahkan fokus keyboard ke bantuan label `Max extensions`
110. Verifikasi teks bantuan label `Max extensions` tersampaikan berbunyi `How many times the due date can be extended; 0 means no extension.`
111. Pindahkan fokus keyboard ke bantuan label `Max assets per borrower (concurrent)`
112. Verifikasi teks bantuan label `Max assets per borrower (concurrent)` tersampaikan berbunyi `Maximum number of assets one borrower can hold at the same time.`
113. Pindahkan fokus keyboard ke bantuan label `Allowed borrower`
114. Verifikasi teks bantuan label `Allowed borrower` tersampaikan berbunyi `Who can borrow assets, based on the asset's origin group.`
115. Pindahkan fokus keyboard ke bantuan label `Block new borrow when overdue`
116. Verifikasi teks bantuan label `Block new borrow when overdue` tersampaikan berbunyi `Prevents a borrower with an overdue borrow from borrowing again until it is returned.`
117. Pindahkan fokus keyboard ke bantuan label `Photo at start`
118. Verifikasi teks bantuan label `Photo at start` tersampaikan berbunyi `Requires a camera photo at the first step of the transaction.`
119. Pindahkan fokus keyboard ke bantuan label `Photo at end`
120. Verifikasi teks bantuan label `Photo at end` tersampaikan berbunyi `Requires a camera photo at the last step of the transaction.`
121. Pindahkan fokus keyboard ke bantuan label `Require approval`
122. Verifikasi teks bantuan label `Require approval` tersampaikan berbunyi `Requires approval before the transaction proceeds.`
123. Pindahkan fokus keyboard ke bantuan label `Approval type`
124. Verifikasi teks bantuan label `Approval type` tersampaikan berbunyi `Whether one approver or all approvers must approve.`
125. Pindahkan fokus keyboard ke bantuan label `Self service`
126. Verifikasi teks bantuan label `Self service` tersampaikan berbunyi `Lets users borrow assets themselves without an admin or approval.`
127. Pindahkan fokus keyboard ke bantuan label `Auto-approve`
128. Verifikasi teks bantuan label `Auto-approve` tersampaikan berbunyi `Approves requests automatically when the conditions below are met.`
129. Pindahkan fokus keyboard ke bantuan label `Auto-approve when duration ≤`
130. Verifikasi teks bantuan label `Auto-approve when duration ≤` tersampaikan berbunyi `Borrow requests up to this duration are approved automatically.`
131. Pindahkan fokus keyboard ke bantuan label `Transaction timeout`
132. Verifikasi teks bantuan label `Transaction timeout` tersampaikan berbunyi `Days a transaction can wait at a step before it is closed automatically.`
133. Pindahkan fokus keyboard ke bantuan label `Due date reminders`
134. Verifikasi teks bantuan label `Due date reminders` tersampaikan berbunyi `When borrowers are reminded before the due date.`
135. Pindahkan fokus keyboard ke bantuan label `Send email notifications`
136. Verifikasi teks bantuan label `Send email notifications` tersampaikan berbunyi `Also sends this transaction's notifications by email.`
