---
id: TC-FA-FASVC-UI-049-form-tampilan-awal-dan-default
title: "Form Create dan Edit: Struktur, Helper, Trigger Tree, dan Nilai Awal"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#p1", "§4.2.2#p1", "§4.2.2#b1", "§4.2.2#b2", "§4.2.2#b3", "§4.2.2#b4", "§4.2.2#b5", "§4.2.2#b6", "§4.2.2#b7", "§4.2.2#b8", "§4.2.2#b9", "§4.2.2#b10", "§4.2.2#b11", "§4.2.2#p2", "§4.2.2#p3", "§9.5#r6", "§9.5#r7", "§9.5#r8", "§9.5#r9", "§4.1#r5", "FI-FASVC-01", "FI-FASVC-03", "FI-FASVC-08", "FI-FASVC-09", "FI-FASVC-10", "S-FASVC-09", "FASVC-LOGIC-02f", "FASVC-LOGIC-02g", "FASVC-LOGIC-02h", "FASVC-LOGIC-02i", "FASVC-LOGIC-02j", "FASVC-LOGIC-02k", "§4.4#r2"]
smoke: []
dependsOn: []
trace:
  "§4.1#p1": [3, 4, 5, 6, 7, 8, 9, 11, 14, 15, 24, 26, 28]
  "§4.2.2#p1": [2, 3, 4, 5, 6, 7, 11, 14, 15, 24, 26, 28, 29, 116, 117]
  "§4.2.2#b1": [3, 4, 5, 6, 7]
  "§4.2.2#b2": [18, 42, 43, 44, 85, 111]
  "§4.2.2#b3": [40, 41, 45, 50, 80, 84, 105, 110, 134]
  "§4.2.2#b4": [20, 25]
  "§4.2.2#b5": [30, 32]
  "§4.2.2#b6": [115]
  "§4.2.2#b7": [61, 67, 73, 92, 98]
  "§4.2.2#b8": [21]
  "§4.2.2#b9": [126, 127]
  "§4.2.2#b10": [29]
  "§4.2.2#b11": [35, 36]
  "§4.2.2#p2": [47, 52, 53, 55]
  "§4.2.2#p3": [90, 92, 93]
  "§9.5#r6": [47, 50, 52]
  "§9.5#r7": [40, 41]
  "§9.5#r8": [21, 22]
  "§9.5#r9": [38, 39, 141]
  "§4.1#r5": [2, 113]
  FI-FASVC-01: [30, 129]
  FI-FASVC-03: [32, 144, 145]
  FI-FASVC-08: [115]
  FI-FASVC-09: [61, 62, 64, 67, 73, 92, 95]
  FI-FASVC-10: [21]
  S-FASVC-09: [119, 123]
  FASVC-LOGIC-02f: [8, 67]
  FASVC-LOGIC-02g: [61, 64, 73, 137, 138]
  FASVC-LOGIC-02h: [47, 50, 52]
  FASVC-LOGIC-02i: [9, 98, 110]
  FASVC-LOGIC-02j: [40, 42]
  FASVC-LOGIC-02k: [92, 95]
  "§4.4#r2": [53, 55, 61, 64, 92, 95]
anchor: [114, 122]
coverage:
  web: automated
---

# Form Create dan Edit: Struktur, Helper, Trigger Tree, dan Nilai Awal

## Prerequisites
- Aktor: Total Control (K1, K3, K4) dan Asset Admin dengan cakupan Group `Branch Surabaya` (K2).
- Layar awal: dialog Create / Edit Service Center yang ditampilkan menurut kondisi di bawah.
- Komponen: Dialog Create / Edit Service Center
- Data:
  - DU-049-1: pohon Group cakupan Total Control: root `All groups`, anak `Head Office`, tiga cucu `Branch Surabaya`, `Branch Malang`, dan `Branch Medan` (leaf bersarang di bawah `Head Office`), serta leaf `Warehouse Bandung` langsung di bawah root `All groups`.
  - DU-049-2: pohon Group cakupan Asset Admin `Branch Surabaya`: `Head Office` sebagai ancestor yang tidak dapat dipilih, dan `Branch Surabaya` sebagai Group yang dapat dipilih.
  - DU-049-3: pohon Category: `Cooling` dengan anak `AC` dan `Refrigeration`, serta `Power` dengan anak `Generator` dan `UPS`.
  - DU-049-4: master Brand: `Daikin` (Active), `Panasonic` (Active), dan `LG` (Inactive).
  - DU-049-5: Service Center untuk Edit: Name `PT Sejuk Abadi Teknik`, Service type `Routine` dan `Repair`, Available to `Branch Surabaya`, Specialization `AC` dan `Refrigeration`, Brands `Daikin` dan `LG`, Country `Indonesia`, Province / State `Jawa Timur`, City `Surabaya`, Postal code `60175`, Address line `Jl. Basuki Rahmat No. 45`, Company phone dengan Dial Code `+62` dan nomor `315550123`, Company email `cs@sejukabadi.co.id`, Contact persons 0 baris, Notes `Vendor AC dan pendingin untuk Branch Surabaya`, Attachments `kontrak-sejuk-abadi.pdf`.
  - DU-049-6: Negara company pada General Settings: `Indonesia`.
  - DU-049-7: Service Center untuk Edit dengan induk terpilih: Name `CV Teknik Dingin Nusantara`, Service type `Routine`, Available to `Head Office` (induk saja), Specialization kosong, Brands kosong, Country `Indonesia`, Province / State `Jawa Barat`, City `Bandung`, Postal code `40115`, Address line `Jl. Asia Afrika No. 10`, Company phone dengan Dial Code `+62` dan nomor `225550188`, Company email `cs@tekniknusantara.co.id`, Contact persons 0 baris, Notes `Vendor pendingin untuk seluruh cabang Head Office`, Attachments kosong.
  - DU-049-8: pohon Group cakupan Total Control sesudah Group baru dibuat: root `All groups`, anak `Head Office`, dan empat cucu `Branch Surabaya`, `Branch Malang`, `Branch Medan`, dan `Branch Bekasi`; `Branch Bekasi` dibuat sesudah DU-049-7 disimpan.
  - DU-049-9: Negara company pada General Settings: `Malaysia`.
- Kondisi:
  - K1: dialog Create dibuka oleh Total Control; pohon Group DU-049-1, pohon Category DU-049-3, master Brand DU-049-4, dan Negara company DU-049-6.
  - K2: dialog Create dibuka oleh Asset Admin dengan cakupan Group `Branch Surabaya`; pohon Group DU-049-2, pohon Category DU-049-3, master Brand DU-049-4, dan Negara company DU-049-6.
  - K3: dialog Edit untuk Service Center DU-049-5 dibuka oleh Total Control; pohon Group DU-049-1, pohon Category DU-049-3, dan master Brand DU-049-4.
  - K4: dialog Edit untuk Service Center DU-049-5 dibuka oleh Total Control, dan permintaan simpan dijawab sukses tanpa perubahan nilai.
  - K5: dialog Edit untuk Service Center DU-049-7 dibuka oleh Total Control; pohon Group DU-049-8, pohon Category DU-049-3, dan master Brand DU-049-4.
  - K6: dialog Create dibuka oleh Total Control; pohon Group DU-049-1, pohon Category DU-049-3, master Brand DU-049-4, dan Negara company DU-049-9.

## Test Steps

### Struktur dialog Create dan pengelompokan field
1. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
2. Verifikasi judul dialog `Add Service Center`
3. Verifikasi section `General` memuat field `Name` dan field `Service type`
4. Verifikasi section `Coverage` memuat field `Available to`, field `Specialization`, dan field `Brands`
5. Verifikasi section `Address` memuat field `Country`, field `Province / State`, field `City`, field `Postal code`, dan field `Address line`
6. Verifikasi section `Contact` memuat field `Company phone`, field `Company email`, dan field `Contact persons`
7. Verifikasi section `Other` memuat field `Notes` dan field `Attachments`
8. Verifikasi field `Name`, field `Service type`, field `Available to`, field `Country`, dan field `City` ditandai wajib
9. Verifikasi field `Specialization` dan field `Brands` tidak ditandai wajib

### Pilihan Service type dan pencarian Brands
10. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
11. Verifikasi field `Service type` memuat checkbox `Routine` dan checkbox `Repair`, keduanya belum tercentang
12. Klik field `Brands`
13. Ketik `dai` pada kotak pencarian daftar Brands
14. Verifikasi opsi `Daikin` tampil pada daftar Brands
15. Verifikasi opsi `Panasonic` tidak tampil pada daftar Brands
16. Klik opsi `Daikin`
17. Tekan `Esc` untuk menutup daftar Brands
18. Verifikasi helper `Leave empty if they work on all brands.` tetap tampil pada field `Brands`

### Kontak awal dan baris contact person
19. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
20. Verifikasi tombol `[+ Contact person]` tampil pada field `Contact persons`
21. Verifikasi field `Contact persons` tidak memiliki baris contact person
22. Verifikasi field `Company phone` menampilkan placeholder `Enter phone number` dan field `Company email` menampilkan placeholder `Enter email`
23. Klik `[+ Contact person]`
24. Verifikasi baris contact person memuat kolom `Primary`, kolom `Name`, kolom `Phone`, dan kolom `Email`
25. Verifikasi baris contact person memiliki tombol hapus baris
26. Verifikasi kolom `Name` pada baris contact person ditandai wajib

### Footer, tanpa Cancel, dan klik di luar dialog
27. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
28. Verifikasi footer dialog memuat `[Clear Field]` dan `[Submit]`
29. Verifikasi checkbox `Stay on this form after submitting` tampil di footer dialog
30. Verifikasi dialog tidak memiliki tombol `[Cancel]`
31. Klik area di luar dialog
32. Verifikasi dialog Create tetap terbuka

### Menutup dialog Create tanpa perubahan
33. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
34. Klik `✕` pada dialog
35. Verifikasi dialog Create tertutup
36. Verifikasi dialog `Unsaved Changes` tidak tampil

### Nilai awal Create bagi Total Control
37. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
38. Verifikasi field `Country` menampilkan `Indonesia`
39. Verifikasi field `Province / State` menampilkan placeholder `Enter province / state` dan field `City` menampilkan placeholder `Enter city`
40. Verifikasi trigger field `Specialization` menampilkan placeholder `Select categories`
41. Verifikasi trigger field `Brands` menampilkan placeholder `Select brands`
42. Verifikasi helper `Leave empty if they work on all categories.` tampil pada field `Specialization`
43. Verifikasi helper `Leave empty if they work on all brands.` tampil pada field `Brands`
44. Verifikasi helper `Groups that can assign work to this service center.` tampil pada field `Available to`
45. Verifikasi tidak ada keterangan `All groups` di bawah field `Available to`
46. Klik trigger field `Available to`
47. Verifikasi checkbox `All groups`, `Head Office`, `Branch Surabaya`, dan `Branch Malang` tercentang
48. Klik `[Cancel]` pada dialog pilihan Available to

### Nilai awal Create bagi Asset Admin dengan cakupan satu Group
49. Tampilkan Dialog Create / Edit Service Center dengan kondisi K2
50. Verifikasi trigger field `Available to` menampilkan `1 group selected`
51. Klik trigger field `Available to`
52. Verifikasi checkbox `Branch Surabaya` tercentang
53. Verifikasi node `Head Office` tampil greyed-out dengan checkbox disabled sehingga tidak dapat dipilih
54. Klik checkbox `Head Office`
55. Verifikasi checkbox `Head Office` tetap tidak tercentang
56. Klik `[Cancel]` pada dialog pilihan Available to

### Memilih dan melepas parent di Available to mencakup seluruh descendant
57. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
58. Klik trigger field `Available to`
59. Klik checkbox `All groups` untuk melepas seluruh pilihan
60. Klik checkbox `Head Office`
61. Verifikasi checkbox `Branch Surabaya`, `Branch Malang`, dan `Branch Medan` tercentang
62. Verifikasi checkbox `Warehouse Bandung` tidak tercentang
63. Klik checkbox `Head Office` untuk melepasnya
64. Verifikasi checkbox `Branch Surabaya`, `Branch Malang`, dan `Branch Medan` tidak tercentang
65. Klik checkbox `Warehouse Bandung`
66. Klik checkbox `Branch Surabaya`
67. Verifikasi checkbox `Warehouse Bandung` dan `Branch Surabaya` tercentang bersamaan
68. Klik `[Cancel]` pada dialog pilihan Available to

### Memilih All groups mencakup seluruh Group di pohon
69. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
70. Klik trigger field `Available to`
71. Klik checkbox `All groups` untuk melepas seluruh pilihan
72. Klik checkbox `All groups` untuk memilihnya
73. Verifikasi checkbox `Head Office`, `Branch Surabaya`, `Branch Malang`, `Branch Medan`, dan `Warehouse Bandung` tercentang
74. Klik `[Cancel]` pada dialog pilihan Available to

### Trigger Available to menampilkan jumlah Group terpilih
75. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
76. Klik trigger field `Available to`
77. Klik checkbox `All groups` untuk melepas seluruh pilihan
78. Klik checkbox `Branch Surabaya`
79. Klik `[Select]` pada dialog pilihan Available to
80. Verifikasi trigger field `Available to` menampilkan `1 group selected`
81. Klik trigger field `Available to`
82. Klik checkbox `Branch Malang`
83. Klik `[Select]` pada dialog pilihan Available to
84. Verifikasi trigger field `Available to` menampilkan `2 groups selected`
85. Verifikasi helper `Groups that can assign work to this service center.` tetap tampil pada field `Available to`

### Memilih dan melepas parent di Specialization mencakup seluruh descendant
86. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
87. Klik trigger field `Specialization`
88. Perluas node `Cooling`
89. Perluas node `Power`
90. Verifikasi `AC` dan `Refrigeration` tampil di bawah `Cooling`, serta `Generator` dan `UPS` tampil di bawah `Power`
91. Klik checkbox `Cooling`
92. Verifikasi checkbox `AC` dan `Refrigeration` tercentang
93. Verifikasi checkbox `Generator` dan `UPS` tidak tercentang
94. Klik checkbox `Cooling` untuk melepasnya
95. Verifikasi checkbox `AC` dan `Refrigeration` tidak tercentang
96. Klik checkbox `AC`
97. Klik checkbox `Generator`
98. Verifikasi checkbox `AC` dan `Generator` tercentang bersamaan
99. Klik `[Cancel]` pada dialog pilihan Specialization

### Trigger Specialization menampilkan jumlah Category terpilih
100. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
101. Klik trigger field `Specialization`
102. Perluas node `Cooling`
103. Klik checkbox `AC`
104. Klik `[Select]` pada dialog pilihan Specialization
105. Verifikasi trigger field `Specialization` menampilkan `1 category selected`
106. Klik trigger field `Specialization`
107. Perluas node `Power`
108. Klik checkbox `Generator`
109. Klik `[Select]` pada dialog pilihan Specialization
110. Verifikasi trigger field `Specialization` menampilkan `2 categories selected`
111. Verifikasi helper `Leave empty if they work on all categories.` tetap tampil pada field `Specialization`

### Tampilan dialog Edit
112. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
113. Verifikasi judul dialog `Edit Service Center`
114. Verifikasi field `Name` tampil pada dialog Edit
115. Verifikasi tidak ada teks info di atas form pada dialog Edit
116. Verifikasi footer dialog Edit memuat `[Clear Field]` dan `[Save]`
117. Verifikasi checkbox `Stay on this form after submitting` tidak tampil pada dialog Edit

### Brand Inactive di master tetap tampil tetapi tidak dapat dipilih baru
118. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
119. Verifikasi chip `LG` pada field `Brands` tampil dengan badge `Inactive`
120. Klik `✕` pada chip `LG` di field `Brands`
121. Klik field `Brands`
122. Verifikasi opsi `Panasonic` tampil pada daftar Brands
123. Verifikasi tidak ada opsi `LG` yang dapat dipilih pada daftar Brands

### Edit tanpa perubahan
124. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
125. Klik `[Save]`
126. Verifikasi dialog Edit tertutup
127. Verifikasi toast info `No changes to save.` tampil

### Dialog Edit tidak memiliki tombol Cancel
128. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
129. Verifikasi dialog Edit tidak memiliki tombol `[Cancel]`

### Trigger Available to kosong menampilkan placeholder
130. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
131. Klik trigger field `Available to`
132. Klik checkbox `All groups` untuk melepas seluruh pilihan
133. Klik `[Select]` pada dialog pilihan Available to
134. Verifikasi trigger field `Available to` menampilkan placeholder `Select groups`

### Memilih parent mencakup descendant yang dibuat kemudian
135. Tampilkan Dialog Create / Edit Service Center dengan kondisi K5
136. Klik trigger field `Available to`
137. Verifikasi checkbox `Head Office` tercentang
138. Verifikasi checkbox `Branch Bekasi` tercentang
139. Klik `[Cancel]` pada dialog pilihan Available to

### Country awal mengikuti Negara company
140. Tampilkan Dialog Create / Edit Service Center dengan kondisi K6
141. Verifikasi field `Country` menampilkan `Malaysia`

### Klik di luar dialog Edit tidak menutup
142. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
143. Klik area di luar dialog Edit
144. Verifikasi dialog Edit tetap terbuka
145. Verifikasi dialog `Unsaved Changes` tidak tampil

