---
id: TC-FA-FATR-UI-064-area-validasi
title: "Area utama: validasi field sebelum Save"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - §4.1#r115
  - §4.1#r202
  - §6#r1
  - §6#r2
  - §6#r8
  - §6#r9
  - §6#r13
  - §6#r14
  - §6#r15
  - §6#r16
  - §6#r17
  - §6#r19
  - §6#r20
  - §6#r21
  - §6#r22
  - §6#r34
  - §6#r38
  - §9.2#r9
  - §9.2#b31
  - §9.2#b44
  - §9.2#b68
  - §9.2#b69
  - §9.2#b70
  - §9.2#b198
  - §9.2#b209
  - §9.2#b298
  - §9.2#b299
  - §9.4.2#r7
  - §9.4.2#r48
  - §9.4.4#r18
  - §9.9#r1
  - §9.9#r2
  - §9.9#r3
  - §9.9#r4
  - §9.9#r5
  - §9.9#r6
  - §9.9#r7
  - §9.9#r8
  - §9.9#r9
  - §9.9#r10
  - §9.9#r11
  - §9.9#r12
smoke: []
dependsOn: []
trace:
  §4.1#r115: [90, 91]
  §4.1#r202: 24
  §6#r1: 81
  §6#r2: [90, 92]
  §6#r8: [8, 42, 49, 60, 61, 75]
  §6#r9: [21, 52, 65, 66]
  §6#r13: [119, 127]
  §6#r14: 81
  §6#r15: 80
  §6#r16: 84
  §6#r17: 119
  §6#r19: [120, 122]
  §6#r20: [119, 127]
  §6#r21: [116, 125]
  §6#r22: [90, 91]
  §6#r34: 90
  §6#r38: [90, 92]
  §9.2#r9: [119, 120, 122]
  §9.2#b31: [110, 113]
  §9.2#b44: [98, 103]
  §9.2#b68: [8, 9, 10, 11, 12, 42, 49, 60, 61, 75]
  §9.2#b69: [21, 22, 23, 24, 52, 65, 66]
  §9.2#b70: [13, 26]
  §9.2#b198: 24
  §9.2#b209: 24
  §9.2#b298: 24
  §9.2#b299: 26
  §9.4.2#r7: [12, 13]
  §9.4.2#r48: [24, 26]
  §9.4.4#r18: 13
  §9.9#r1: [8, 21, 29]
  §9.9#r2: [9, 25, 31]
  §9.9#r3: [10, 22, 33]
  §9.9#r4: [42, 44]
  §9.9#r5: [49, 52, 54]
  §9.9#r6: [60, 65, 68]
  §9.9#r7: [61, 66, 70]
  §9.9#r8: [11, 23, 35]
  §9.9#r9: [12, 24, 37]
  §9.9#r10: [75, 77]
  §9.9#r11: [80, 81]
  §9.9#r12: [90, 91, 98]
anchor: [83, 112, 115, 124]
coverage:
  web: automated
---

# Area utama: validasi field sebelum Save

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-064-1: Pengaturan Company default pada All categories: Max duration `14` dengan Duration unit `Days`, Max extensions `1`, Max assets per borrower (concurrent) `3`, Auto-approve when duration ≤ `3`, Transaction timeout `7`, Require approval Borrow `ON`, Auto-approve Borrow `ON`, Max assets per assignee (concurrent) `0`, Allowed assignee: Employee `ON`, Allowed assignee: Division `ON`, In-transit overdue after `7`, Min asset age warning `12`, Max deviation from book value `30`, Long missing after `30`, Allow Assign `Allow`.
  - DU-064-2: Field angka yang dikosongkan: nilai kosong.
  - DU-064-3: Field angka yang diisi nilai nol: `0`.
  - DU-064-4: Masukan campur huruf dan angka `1a2`, nilai tampil `12` dari masukan itu.
  - DU-064-5: Pengaturan Company default tab Disposal pada All categories dengan Allowed disposal types hanya `Sell`.
  - DU-064-6: Allowed assignee: Employee `OFF` dan Allowed assignee: Division `OFF`.
  - DU-064-7: Pengaturan Category leaf `Machinery` tab Assign: Allow Assign bernilai sendiri `Allow`, Allowed assignee: Employee `ON` dan Allowed assignee: Division `ON` bernilai sendiri.
  - DU-064-8: Pengaturan Category leaf `Machinery` tab Borrow: semua field Inherit, Company default Max duration `14` dengan Duration unit `Days`.
  - DU-064-9: Nilai Max duration `400` yang dicoba untuk Duration unit `Days`.
  - DU-064-10: Pengaturan Category leaf `Machinery` tab Borrow: semua field Inherit, Company default Duration unit `Hours` dengan Max duration `9000`.
- Kondisi:
  - K1: node All categories terpilih, tab Borrow aktif, nilai Company default memakai DU-064-1.
  - K2: node All categories terpilih, tab Disposal aktif, Allowed disposal types hanya `Sell` memakai DU-064-5, field lain memakai DU-064-1.
  - K3: node Category leaf `Machinery` terpilih, tab Assign aktif, nilai memakai DU-064-7.
  - K4: node Category leaf `Machinery` terpilih, tab Borrow aktif, nilai memakai DU-064-8.
  - K5: node Category leaf `Machinery` terpilih, tab Borrow aktif, nilai memakai DU-064-10.

## Test Steps

### Field angka tab Borrow dikosongkan
1. Tampilkan Area utama dengan kondisi K1
2. Kosongkan `Max duration`
3. Kosongkan `Max extensions`
4. Kosongkan `Max assets per borrower (concurrent)`
5. Kosongkan `Auto-approve when duration ≤`
6. Kosongkan `Transaction timeout`
7. Klik `Save`
8. Verifikasi pesan `You must enter a value` tampil di bawah kontrol `Max duration`
9. Verifikasi pesan `You must enter a value` tampil di bawah kontrol `Max extensions`
10. Verifikasi pesan `You must enter a value` tampil di bawah kontrol `Max assets per borrower (concurrent)`
11. Verifikasi pesan `You must enter a value` tampil di bawah kontrol `Auto-approve when duration ≤`
12. Verifikasi pesan `You must enter a value` tampil di bawah kontrol `Transaction timeout`
13. Verifikasi dialog `Save Changes` tidak tampil dan Save tidak diproses

### Field angka tab Borrow bernilai 0
14. Tampilkan Area utama dengan kondisi K1
15. Ganti `Max duration` menjadi `0`
16. Ganti `Max extensions` menjadi `0`
17. Ganti `Max assets per borrower (concurrent)` menjadi `0`
18. Ganti `Auto-approve when duration ≤` menjadi `0`
19. Ganti `Transaction timeout` menjadi `0`
20. Klik `Save`
21. Verifikasi pesan `Value must be at least 1` tampil di bawah kontrol `Max duration`
22. Verifikasi pesan `Value must be at least 1` tampil di bawah kontrol `Max assets per borrower (concurrent)`
23. Verifikasi pesan `Value must be at least 1` tampil di bawah kontrol `Auto-approve when duration ≤`
24. Verifikasi pesan `Value must be at least 1` tampil di bawah kontrol `Transaction timeout`
25. Verifikasi `Max extensions` bernilai `0` dan tidak ada pesan di bawah kontrolnya
26. Verifikasi dialog `Save Changes` tidak tampil dan Save tidak diproses

### Masukan field angka tab Borrow hanya digit
27. Tampilkan Area utama dengan kondisi K1
28. Ganti `Max duration` dengan `1a2`
29. Verifikasi `Max duration` bernilai `12`
30. Ganti `Max extensions` dengan `1a2`
31. Verifikasi `Max extensions` bernilai `12`
32. Ganti `Max assets per borrower (concurrent)` dengan `1a2`
33. Verifikasi `Max assets per borrower (concurrent)` bernilai `12`
34. Ganti `Auto-approve when duration ≤` dengan `1a2`
35. Verifikasi `Auto-approve when duration ≤` bernilai `12`
36. Ganti `Transaction timeout` dengan `1a2`
37. Verifikasi `Transaction timeout` bernilai `12`

### Max assets per assignee (concurrent) di tab Assign
38. Tampilkan Area utama dengan kondisi K1
39. Klik tab `Assign`
40. Kosongkan `Max assets per assignee (concurrent)`
41. Klik `Save`
42. Verifikasi pesan `You must enter a value` tampil di bawah kontrol `Max assets per assignee (concurrent)`
43. Ganti `Max assets per assignee (concurrent)` dengan `1a2`
44. Verifikasi `Max assets per assignee (concurrent)` bernilai `12`

### In-transit overdue after di tab Transfer
45. Tampilkan Area utama dengan kondisi K1
46. Klik tab `Transfer`
47. Kosongkan `In-transit overdue after`
48. Klik `Save`
49. Verifikasi pesan `You must enter a value` tampil di bawah kontrol `In-transit overdue after`
50. Ganti `In-transit overdue after` menjadi `0`
51. Klik `Save`
52. Verifikasi pesan `Value must be at least 1` tampil di bawah kontrol `In-transit overdue after`
53. Ganti `In-transit overdue after` dengan `1a2`
54. Verifikasi `In-transit overdue after` bernilai `12`

### Field angka tab Disposal
55. Tampilkan Area utama dengan kondisi K1
56. Klik tab `Disposal`
57. Kosongkan `Min asset age warning`
58. Kosongkan `Max deviation from book value`
59. Klik `Save`
60. Verifikasi pesan `You must enter a value` tampil di bawah kontrol `Min asset age warning`
61. Verifikasi pesan `You must enter a value` tampil di bawah kontrol `Max deviation from book value`
62. Ganti `Min asset age warning` menjadi `0`
63. Ganti `Max deviation from book value` menjadi `0`
64. Klik `Save`
65. Verifikasi pesan `Value must be at least 1` tampil di bawah kontrol `Min asset age warning`
66. Verifikasi pesan `Value must be at least 1` tampil di bawah kontrol `Max deviation from book value`
67. Ganti `Min asset age warning` dengan `1a2`
68. Verifikasi `Min asset age warning` menyimpan digit dari masukan itu sebagai `12`
69. Ganti `Max deviation from book value` dengan `1a2`
70. Verifikasi `Max deviation from book value` bernilai `12`

### Long missing after di tab Damaged & Missing
71. Tampilkan Area utama dengan kondisi K1
72. Klik tab `Damaged & Missing`
73. Kosongkan `Long missing after`
74. Klik `Save`
75. Verifikasi pesan `You must enter a value` tampil di bawah kontrol `Long missing after`
76. Ganti `Long missing after` dengan `1a2`
77. Verifikasi `Long missing after` bernilai `12`

### Pilihan terakhir Allowed disposal types
78. Tampilkan Area utama dengan kondisi K2
79. Hapus pilihan `Sell` pada `Allowed disposal types`
80. Verifikasi pilihan terakhir `Sell` tetap terpilih pada `Allowed disposal types` setelah penghapusan dicoba
81. Verifikasi pesan `At least one disposal type must be selected` tampil tepat di bawah kontrol `Allowed disposal types` tanpa Save diklik
82. Pilih `Scrap` pada `Allowed disposal types`
83. Verifikasi `Allowed disposal types` terpilih `Sell` dan `Scrap`
84. Verifikasi pesan `At least one disposal type must be selected` tidak ada

### Allowed assignee keduanya OFF pada Save
85. Tampilkan Area utama dengan kondisi K1
86. Klik tab `Assign`
87. Matikan `Allowed assignee: Employee`
88. Matikan `Allowed assignee: Division`
89. Klik `Save`
90. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol `Allowed assignee: Employee`
91. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol `Allowed assignee: Division`
92. Verifikasi dialog `Save Changes` tidak tampil

### Guard Allowed assignee tidak dievaluasi saat Allow Assign Deny
93. Tampilkan Area utama dengan kondisi K3
94. Matikan `Allowed assignee: Employee`
95. Matikan `Allowed assignee: Division`
96. Pilih `Deny` pada `Allow Assign`
97. Klik `Save`
98. Verifikasi dialog `Save Changes` tampil

### Field tersembunyi tidak divalidasi
99. Tampilkan Area utama dengan kondisi K1
100. Kosongkan `Auto-approve when duration ≤`
101. Matikan `Require approval`
102. Klik `Save`
103. Verifikasi dialog `Save Changes` tampil

### Draft tidak valid di tab lain
104. Tampilkan Area utama dengan kondisi K1
105. Klik tab `Transfer`
106. Ganti `In-transit overdue after` menjadi `0`
107. Klik tab `Borrow`
108. Klik `Save`
109. Klik tab `Transfer`
110. Verifikasi pesan `Value must be at least 1` tampil di bawah kontrol `In-transit overdue after`
111. Klik tab `Borrow`
112. Verifikasi `Transaction timeout` pada tab `Borrow` bernilai `7`
113. Verifikasi dialog `Save Changes` tidak tampil

### Peringatan Max duration di halaman Settings untuk nilai sendiri
114. Tampilkan Area utama dengan kondisi K4
115. Verifikasi `Max duration` pada Category `Machinery` masih menampilkan `Inherit — 14 days (from Company default)` sebelum Set own value
116. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tidak ada
117. Klik `Set own value` pada `Max duration`
118. Ganti `Max duration` menjadi `400`
119. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tampil di bagian `Limits`
120. Verifikasi tombol `Save` aktif
121. Klik `Save`
122. Verifikasi dialog `Save Changes` tampil

### Peringatan tidak tampil untuk nilai warisan dan tampil saat Duration unit menjadi nilai sendiri
123. Tampilkan Area utama dengan kondisi K5
124. Verifikasi `Max duration` menampilkan `Inherit — 9000 hours (from Company default)`
125. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tidak ada pada nilai warisan
126. Klik `Set own value` pada `Duration unit`
127. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tampil di bagian `Limits`
