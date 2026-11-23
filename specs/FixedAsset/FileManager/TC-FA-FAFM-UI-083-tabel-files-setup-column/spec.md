---
id: TC-FA-FAFM-UI-083-tabel-files-setup-column
title: "Tabel Files: Column Visibility dan Setup Column"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["INV-07a", "INV-07b", "INV-07c", "INV-07d", "INV-08a", "INV-08b", "INV-08c", "EB-KOL-1@tabel-files", "EB-KOL-3"]
smoke: []
dependsOn: []
trace:
  "INV-07a": [4, 5]
  "INV-07b": [4]
  "INV-07c": [2, 8, 9, 11, 15]
  "INV-07d": [6]
  "INV-08a": [19]
  "INV-08b": [19, 20]
  "INV-08c": [26, 32, 33, 38, 44, 51, 125, 127, 133]
  "EB-KOL-1@tabel-files": [19, 21, 22, 23, 24, 25, 26, 32, 33, 38, 44, 51, 53, 55, 61, 62, 67, 68, 70, 71, 77, 80, 83, 93, 94, 96, 107, 108, 110, 125, 127, 133]
  "EB-KOL-3": [114, 115, 117, 118, 119]
anchor: []
coverage:
  web: automated
---

# Tabel Files: Column Visibility dan Setup Column

## Prerequisites
- Aktor: Total Control.
- Layar awal: Tabel File Manager tab Files.
- Komponen: Tabel File Manager tab Files.
- Data:
  - DU-083-1: `laptop-front.jpg`, JPG, Source Asset Photo, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `820.4 KB`, Uploaded By `Budi S`, Upload Date `02/11/26 14:30`.
  - DU-083-2: `monitor-lg-front.png`, PNG, Source Asset Photo, Asset `Monitor LG 24 - 7`, Asset ID `MON-2026-0007`, Group `Branch Bandung`, Size `640.0 KB`, Uploaded By `Dodi P`, Upload Date `05/11/26 09:00`.
  - DU-083-3: aset Asset Data `Printer HP M404 - 1`, Asset ID `PRN-2026-0001`, Group `Branch Bandung`, Status `Disposed`, Data & Log Size `1.2 MB`, Files Size `5.8 MB`, Total Size `7.0 MB`.
- Kondisi:
  - K1: tab `Asset Photo` aktif; tabel berisi DU-083-1 dan DU-083-2; semua kolom data pada kondisi default (kolom `File Name`, `File Format`, `Asset`, `Asset ID`, `Group`, `Size`, `Uploaded By`, `Upload Date` tampil); belum ada konfigurasi kolom tersimpan.
  - K2: sama dengan K1; tab `Disposed & Unmanaged Assets` berisi DU-083-3 dengan kolom default.
  - K3: sama dengan K1; lebar tampilan sempit sehingga tabel Files dapat digulir horizontal.

## Test Steps

### Panel Column Visibility: show/hide langsung diterapkan
1. Tampilkan Tabel File Manager tab Files dengan kondisi K1
2. Verifikasi header kolom `Asset ID` tampil pada tabel
3. Klik trigger `Column Visibility` pada header kolom Actions
4. Verifikasi panel dropdown Column Visibility tampil
5. Verifikasi panel memuat checkbox untuk kolom `File Name`
6. Verifikasi item `Setup Column...` tampil pada panel
7. Hapus centang kolom `Asset ID` pada panel Column Visibility
8. Verifikasi header kolom `File Name` masih tampil pada tabel
9. Verifikasi header kolom `Asset ID` tidak tampil pada tabel tanpa langkah penyimpanan
10. Centang kembali kolom `Asset ID` pada panel Column Visibility
11. Verifikasi header kolom `Asset ID` tampil kembali pada tabel

### Panel Column Visibility: reorder langsung diterapkan
12. Tampilkan Tabel File Manager tab Files dengan kondisi K1
13. Klik trigger `Column Visibility` pada header kolom Actions
14. Seret kolom `Group` ke posisi di atas kolom `File Format` pada panel Column Visibility
15. Verifikasi header kolom `Group` tampil sebelum header kolom `File Format` pada tabel

### Item Setup Column... membuka dialog Setup Column
16. Tampilkan Tabel File Manager tab Files dengan kondisi K1
17. Klik trigger `Column Visibility` pada header kolom Actions
18. Klik item `Setup Column...` pada panel Column Visibility
19. Verifikasi dialog dengan judul `Setup Column` tampil
20. Verifikasi panel dropdown Column Visibility tertutup
21. Verifikasi deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.` tampil di dialog
22. Verifikasi ikon tutup `[✕]` tampil di dialog
23. Verifikasi tombol `[Reset to Default]` tampil di footer dialog
24. Verifikasi tombol `[Save]` tampil di footer dialog
25. Verifikasi footer dialog tidak memuat tombol `[Cancel]`
26. Verifikasi dialog memuat checkbox, handle seret, dan ikon pin untuk kolom `File Name`

### Dialog: hide dan show kolom berlaku setelah Save
27. Tampilkan Tabel File Manager tab Files dengan kondisi K1
28. Klik trigger `Column Visibility` pada header kolom Actions
29. Klik item `Setup Column...` pada panel Column Visibility
30. Hapus centang kolom `Uploaded By` di dialog Setup Column
31. Klik `[Save]`
32. Verifikasi header kolom `File Name` tampil pada tabel setelah dialog tertutup
33. Verifikasi header kolom `Uploaded By` tidak tampil pada tabel
34. Klik trigger `Column Visibility` pada header kolom Actions
35. Klik item `Setup Column...` pada panel Column Visibility
36. Centang kembali kolom `Uploaded By` di dialog Setup Column
37. Klik `[Save]`
38. Verifikasi header kolom `Uploaded By` tampil kembali pada tabel

### Dialog: reorder kolom berlaku setelah Save
39. Tampilkan Tabel File Manager tab Files dengan kondisi K1
40. Klik trigger `Column Visibility` pada header kolom Actions
41. Klik item `Setup Column...` pada panel Column Visibility
42. Seret kolom `Group` ke posisi di atas kolom `File Format` di dialog Setup Column
43. Klik `[Save]`
44. Verifikasi header kolom `Group` tampil sebelum header kolom `File Format` pada tabel setelah Save

### Dialog: pin dan batas tiga kolom
45. Tampilkan Tabel File Manager tab Files dengan kondisi K1
46. Klik trigger `Column Visibility` pada header kolom Actions
47. Klik item `Setup Column...` pada panel Column Visibility
48. Klik ikon pin kolom `File Name` di dialog Setup Column
49. Klik ikon pin kolom `File Format` di dialog Setup Column
50. Klik ikon pin kolom `Asset` di dialog Setup Column
51. Verifikasi ikon pin kolom `Group` tidak dapat diklik
52. Arahkan kursor ke ikon pin kolom `Group`
53. Verifikasi teks `Maximum 3 columns can be pinned at once. Unpin another column first.` tersampaikan pada ikon pin kolom `Group`
54. Klik ikon pin kolom `File Format` di dialog Setup Column untuk melepas pin
55. Verifikasi ikon pin kolom `Group` dapat diklik kembali

### Dialog: Reset to Default mengembalikan ke default modul
56. Tampilkan Tabel File Manager tab Files dengan kondisi K1
57. Klik trigger `Column Visibility` pada header kolom Actions
58. Klik item `Setup Column...` pada panel Column Visibility
59. Hapus centang kolom `Uploaded By` di dialog Setup Column
60. Klik `[Save]`
61. Verifikasi header kolom `Upload Date` tampil pada tabel setelah Save
62. Verifikasi header kolom `Uploaded By` tidak tampil pada tabel setelah Save
63. Klik trigger `Column Visibility` pada header kolom Actions
64. Klik item `Setup Column...` pada panel Column Visibility
65. Hapus centang kolom `Size` di dialog Setup Column
66. Klik `[Reset to Default]`
67. Verifikasi checkbox kolom `Size` tercentang di dialog Setup Column
68. Verifikasi checkbox kolom `Uploaded By` tercentang di dialog Setup Column
69. Klik `[Save]`
70. Verifikasi header kolom `Size` tampil pada tabel setelah reset disimpan
71. Verifikasi header kolom `Uploaded By` tampil pada tabel setelah reset disimpan

### Dialog: menutup tanpa Save membuang perubahan
72. Tampilkan Tabel File Manager tab Files dengan kondisi K1
73. Klik trigger `Column Visibility` pada header kolom Actions
74. Klik item `Setup Column...` pada panel Column Visibility
75. Hapus centang kolom `Asset` di dialog Setup Column
76. Klik ikon tutup `[✕]` di dialog Setup Column
77. Verifikasi header kolom `Asset` masih tampil pada tabel setelah dialog ditutup dengan `[✕]`
78. Klik trigger `Column Visibility` pada header kolom Actions
79. Klik item `Setup Column...` pada panel Column Visibility
80. Verifikasi checkbox kolom `Asset` tercentang saat dialog dibuka kembali
81. Hapus centang kolom `Asset` di dialog Setup Column
82. Tekan Esc
83. Verifikasi header kolom `Asset` masih tampil pada tabel setelah dialog ditutup dengan Esc

### Kolom terakhir tidak bisa disembunyikan: panel Column Visibility
84. Tampilkan Tabel File Manager tab Files dengan kondisi K1
85. Klik trigger `Column Visibility` pada header kolom Actions
86. Hapus centang kolom `File Format` pada panel Column Visibility
87. Hapus centang kolom `Asset` pada panel Column Visibility
88. Hapus centang kolom `Asset ID` pada panel Column Visibility
89. Hapus centang kolom `Group` pada panel Column Visibility
90. Hapus centang kolom `Size` pada panel Column Visibility
91. Hapus centang kolom `Uploaded By` pada panel Column Visibility
92. Hapus centang kolom `Upload Date` pada panel Column Visibility
93. Verifikasi header kolom `File Name` tampil sebagai satu-satunya kolom pada tabel
94. Verifikasi checkbox kolom `File Name` pada panel tidak dapat diubah
95. Arahkan kursor ke checkbox kolom `File Name` pada panel Column Visibility
96. Verifikasi teks `At least one column must remain visible.` tersampaikan pada checkbox kolom `File Name`

### Kolom terakhir tidak bisa disembunyikan: dialog Setup Column
97. Tampilkan Tabel File Manager tab Files dengan kondisi K1
98. Klik trigger `Column Visibility` pada header kolom Actions
99. Klik item `Setup Column...` pada panel Column Visibility
100. Hapus centang kolom `File Format` di dialog Setup Column
101. Hapus centang kolom `Asset` di dialog Setup Column
102. Hapus centang kolom `Asset ID` di dialog Setup Column
103. Hapus centang kolom `Group` di dialog Setup Column
104. Hapus centang kolom `Size` di dialog Setup Column
105. Hapus centang kolom `Uploaded By` di dialog Setup Column
106. Hapus centang kolom `Upload Date` di dialog Setup Column
107. Verifikasi checkbox kolom `File Name` tercentang di dialog Setup Column
108. Verifikasi checkbox kolom `File Name` di dialog tidak dapat diubah
109. Arahkan kursor ke checkbox kolom `File Name` di dialog Setup Column
110. Verifikasi teks `At least one column must remain visible.` tersampaikan pada checkbox kolom `File Name` di dialog

### Konfigurasi kolom satu tabel tidak mengubah tabel lain
111. Tampilkan Tabel File Manager tab Files dengan kondisi K2
112. Klik trigger `Column Visibility` pada header kolom Actions
113. Hapus centang kolom `Asset ID` pada panel Column Visibility
114. Verifikasi header kolom `Size` tampil pada tabel Files
115. Verifikasi header kolom `Asset ID` tidak tampil pada tabel Files
116. Klik tab `Disposed & Unmanaged Assets`
117. Verifikasi header kolom `Name` pada tabel Asset Data tidak berubah
118. Verifikasi header kolom `Asset ID` tampil pada tabel Asset Data
119. Verifikasi header kolom `Total Size` tampil pada tabel Asset Data

### Dialog: kolom yang di-pin beku di kiri tabel setelah Save, dan kembali tidak beku setelah unpin
120. Tampilkan Tabel File Manager tab Files dengan kondisi K3
121. Klik trigger `Column Visibility` pada header kolom Actions
122. Klik item `Setup Column...` pada panel Column Visibility
123. Klik ikon pin kolom `Asset` di dialog Setup Column
124. Klik `[Save]`
125. Verifikasi header kolom `Asset` tampil beku di sisi kiri tabel setelah Save
126. Gulir tabel Files secara horizontal
127. Verifikasi header kolom `Asset` tetap terlihat di sisi kiri tabel saat tabel digulir
128. Klik trigger `Column Visibility` pada header kolom Actions
129. Klik item `Setup Column...` pada panel Column Visibility
130. Klik ikon pin kolom `Asset` di dialog Setup Column untuk melepas pin
131. Klik `[Save]`
132. Gulir tabel Files secara horizontal
133. Verifikasi header kolom `Asset` ikut bergeser saat tabel digulir setelah pin dilepas
