---
id: TC-FA-FAREG-E2E-041-draft-filter
title: "Sub tab Draft: opsi dan hasil Filter"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r22", "§4.1#r23", "§4.1#r24", "§4.1#r25", "§4.1#r26", "§4.1#r27", "§9.5#r11", "EB-FLT-1@tabel-draft", "EB-FLT-4@tabel-draft", "EB-FLT-3"]
smoke: ["EB-FLT-3"]
dependsOn: []
trace:
  "§4.1#r22": [2, 7, 12]
  "§4.1#r23": [2]
  "§4.1#r24": [2, 18, 23, 28, 53]
  "§4.1#r25": [2]
  "§4.1#r26": [2, 33, 36, 53]
  "§4.1#r27": [2, 41, 46]
  "§9.5#r11": [4]
  "EB-FLT-1@tabel-draft": [4, 129]
  "EB-FLT-3": [36, 53]
  "EB-FLT-4@tabel-draft": [57, 61, 64, 65, 69, 70, 76, 83, 85, 92, 93, 99, 106, 111, 118, 125]
coverage:
  web: automated
---

# Sub tab Draft: opsi dan hasil Filter

## Prerequisites
- Aktor: Total Control `Maya L`, belum memiliki batch Draft sebelum spec mulai.
- Layar awal: Assets > Registration > Draft.
- Data:
  - DU-041-1: Batch Draft dengan Group `Gudang Cawang {runId}`, Origin `—`, Total Asset `5`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`.
  - DU-041-2: Batch Draft dengan Group `Gudang Pancoran {runId}`, Origin `—`, Total Asset `15`, Progress `0%`, Requested By `Budi S`, Last Updated `T0 − 2 hari`.
  - DU-041-3: Batch Draft dengan Group `Gudang Kuningan {runId}`, Origin `—`, Total Asset `20`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − 3 hari`.
  - DU-041-4: Batch Draft dengan Group `Gudang Pasar Minggu {runId}`, Origin `—`, Total Asset `30`, Progress `0%`, Requested By `Siti N`, Last Updated `T0 − 4 hari`.
  - DU-041-5: Batch Draft dengan Group `Gudang Ciputat {runId}`, Origin `—`, Total Asset `31`, Progress `0%`, Requested By `Budi S`, Last Updated `T0 − 5 hari`.
  - DU-041-6: Batch Draft dengan Group `Gudang Bintaro {runId}`, Origin `—`, Total Asset `8`, Progress `0%`, Requested By `Siti N`, Last Updated `T0 − 6 hari`.
  - DU-041-7: Batch Draft dengan Group `Gudang Kramat {runId}`, Origin `—`, Total Asset `40`, Progress `0%`, Requested By `Dewi A`, Last Updated `T0 − 7 hari`.
  - DU-041-8: Batch Draft dengan Group `Gudang Senen {runId}`, Origin `—`, Total Asset `45`, Progress `0%`, Requested By `Dewi A`, Last Updated `T0 − 8 hari`.
  - DU-041-9: Group `Gudang Cikini {runId}` yang dapat dipilih (Assignable) di entitas aktor.
  - DU-041-10: Group `Gudang Setiabudi {runId}` yang dapat dipilih (Assignable) di entitas aktor.
  - DU-041-11: Pengguna aktif `Wulan T` (nama singkat `Wulan T`) dengan role Manage asset & TAG, tidak memiliki batch Draft.
  - Rina W, Budi S, Siti N, dan Dewi A adalah pengguna aktif dengan role Manage asset & TAG pada Group batch masing-masing.

## Test Steps

### Panel Filter memuat field kolom yang Filterable
1. Klik ikon Filter
2. Verifikasi panel Filter memuat field `Group`, `Total Asset`, `Requested By`, dan `Last Updated` dan tidak memuat field `Origin` maupun `Progress`

### Opsi filter Requested By berasal dari nilai tabel Draft
3. Klik field `Requested By` pada panel Filter
4. Verifikasi opsi berisi nilai DISTINCT kolom Requested By pada tabel yang sedang tampil: daftar opsi memuat `Rina W`, `Budi S`, `Siti N`, dan `Dewi A` dan tidak memuat `Wulan T` maupun `Maya L`[^drift-1]

### Filter Group: cocok dan tidak cocok
5. Pilih Group `Gudang Kuningan {runId}` pada field `Group`
6. Klik `[Apply]`
7. Verifikasi tabel sub tab Draft memuat baris `Gudang Kuningan {runId}` dan tidak memuat baris `Gudang Cawang {runId}`
8. Klik `[Clear Field]`
9. Klik `[Apply]`
10. Pilih Group `Gudang Setiabudi {runId}` pada field `Group`
11. Klik `[Apply]`
12. Verifikasi `No results found` tampil
13. Klik `[Clear Field]`
14. Klik `[Apply]`

### Filter Total Asset: batas Min dan Max
15. Isi Min `15` pada field `Total Asset`
16. Isi Max `30` pada field `Total Asset`
17. Klik `[Apply]`
18. Verifikasi tabel sub tab Draft memuat baris `Gudang Pancoran {runId}`, `Gudang Kuningan {runId}`, `Gudang Pasar Minggu {runId}` dan tidak memuat baris `Gudang Cawang {runId}`, `Gudang Ciputat {runId}`, `Gudang Bintaro {runId}`; baris bernilai tepat `15` dan tepat `30` ikut tampil
19. Klik `[Clear Field]`
20. Klik `[Apply]`
21. Isi Min `20` pada field `Total Asset`
22. Klik `[Apply]`
23. Verifikasi tabel sub tab Draft memuat baris `Gudang Kuningan {runId}`, `Gudang Pasar Minggu {runId}`, `Gudang Ciputat {runId}` dan tidak memuat baris `Gudang Cawang {runId}`, `Gudang Pancoran {runId}`, `Gudang Bintaro {runId}`; hanya Min yang diisi
24. Klik `[Clear Field]`
25. Klik `[Apply]`
26. Isi Max `15` pada field `Total Asset`
27. Klik `[Apply]`
28. Verifikasi tabel sub tab Draft memuat baris `Gudang Cawang {runId}`, `Gudang Pancoran {runId}`, `Gudang Bintaro {runId}` dan tidak memuat baris `Gudang Kuningan {runId}`, `Gudang Pasar Minggu {runId}`, `Gudang Ciputat {runId}`; hanya Max yang diisi
29. Klik `[Clear Field]`
30. Klik `[Apply]`

### Filter Requested By: satu opsi lalu dua opsi
31. Pilih opsi `Rina W` pada field `Requested By`
32. Klik `[Apply]`
33. Verifikasi tabel sub tab Draft memuat baris `Gudang Cawang {runId}`, `Gudang Kuningan {runId}` dan tidak memuat baris `Gudang Pancoran {runId}`, `Gudang Pasar Minggu {runId}`
34. Pilih opsi `Siti N` pada field `Requested By`
35. Klik `[Apply]`
36. Verifikasi tabel sub tab Draft memuat baris `Gudang Cawang {runId}`, `Gudang Kuningan {runId}`, `Gudang Pasar Minggu {runId}`, `Gudang Bintaro {runId}` dan tidak memuat baris `Gudang Pancoran {runId}`, `Gudang Ciputat {runId}`; dua opsi dalam satu field berlaku OR
37. Klik `[Clear Field]`
38. Klik `[Apply]`

### Filter Last Updated: rentang tanggal
39. Pilih rentang tanggal `T0 − 4 hari` sampai `T0 − 2 hari` pada field `Last Updated`
40. Klik `[Apply]`
41. Verifikasi tabel sub tab Draft memuat baris `Gudang Pancoran {runId}`, `Gudang Kuningan {runId}`, `Gudang Pasar Minggu {runId}` dan tidak memuat baris `Gudang Cawang {runId}`, `Gudang Ciputat {runId}`; baris pada tanggal awal dan tanggal akhir rentang ikut tampil
42. Klik `[Clear Field]`
43. Klik `[Apply]`
44. Pilih rentang tanggal `T0 − 3 hari` sampai `T0 − 3 hari` pada field `Last Updated`
45. Klik `[Apply]`
46. Verifikasi tabel sub tab Draft memuat baris `Gudang Kuningan {runId}` dan tidak memuat baris `Gudang Pancoran {runId}`, `Gudang Pasar Minggu {runId}`; Start Date sama dengan End Date
47. Klik `[Clear Field]`
48. Klik `[Apply]`

### Dua field filter berlaku AND
49. Pilih opsi `Rina W` pada field `Requested By`
50. Isi Min `15` pada field `Total Asset`
51. Isi Max `30` pada field `Total Asset`
52. Klik `[Apply]`
53. Verifikasi tabel sub tab Draft memuat baris `Gudang Kuningan {runId}` dan tidak memuat baris `Gudang Cawang {runId}`, `Gudang Pancoran {runId}`, `Gudang Pasar Minggu {runId}`, `Gudang Ciputat {runId}`, `Gudang Bintaro {runId}`; hanya baris yang memenuhi kedua field yang tampil
54. Klik `[Clear Field]`
55. Klik `[Apply]`

### Search dan Filter beririsan
56. Ketik Search `Rina W`, tekan Enter
57. Verifikasi tabel sub tab Draft memuat baris `Gudang Cawang {runId}`, `Gudang Kuningan {runId}` dan tidak memuat baris `Gudang Pancoran {runId}`, `Gudang Pasar Minggu {runId}`; Search saja
58. Isi Min `15` pada field `Total Asset`
59. Isi Max `30` pada field `Total Asset`
60. Klik `[Apply]`
61. Verifikasi tabel sub tab Draft memuat baris `Gudang Kuningan {runId}` dan tidak memuat baris `Gudang Cawang {runId}`, `Gudang Pancoran {runId}`, `Gudang Pasar Minggu {runId}`; irisan Search lalu Filter
62. Klik ikon sort pada header kolom `Total Asset`
63. Klik `(←)` pada kotak Search
64. Verifikasi tabel sub tab Draft memuat baris `Gudang Pancoran {runId}`, `Gudang Kuningan {runId}`, `Gudang Pasar Minggu {runId}` dan tidak memuat baris `Gudang Cawang {runId}`; Filter tetap berlaku setelah Search dibersihkan
65. Verifikasi urutan baris kolom `Total Asset` naik tetap berlaku setelah Search dibersihkan: `Gudang Pancoran {runId}`, `Gudang Kuningan {runId}`, `Gudang Pasar Minggu {runId}`
66. Ketik Search `Rina W`, tekan Enter
67. Klik `[Clear Field]`
68. Klik `[Apply]`
69. Verifikasi tabel sub tab Draft memuat baris `Gudang Cawang {runId}`, `Gudang Kuningan {runId}` dan tidak memuat baris `Gudang Pancoran {runId}`, `Gudang Pasar Minggu {runId}`; Search tetap berlaku setelah Filter dibersihkan
70. Verifikasi urutan baris kolom `Total Asset` naik tetap berlaku setelah Filter dibersihkan: `Gudang Cawang {runId}`, `Gudang Kuningan {runId}`
71. Klik `(←)` pada kotak Search
72. Isi Min `15` pada field `Total Asset`
73. Isi Max `30` pada field `Total Asset`
74. Klik `[Apply]`
75. Ketik Search `Rina W`, tekan Enter
76. Verifikasi tabel sub tab Draft memuat baris `Gudang Kuningan {runId}` dan tidak memuat baris `Gudang Cawang {runId}`, `Gudang Pancoran {runId}`, `Gudang Pasar Minggu {runId}`; irisan Filter lalu Search sama dengan irisan Search lalu Filter
77. Klik `[Clear Field]`
78. Klik `[Apply]`
79. Klik `(←)` pada kotak Search

### Irisan Search dan Filter kosong lalu dipulihkan
80. Ketik Search `Siti N`, tekan Enter
81. Pilih opsi `Rina W` pada field `Requested By`
82. Klik `[Apply]`
83. Verifikasi `No results found` tampil
84. Klik `(←)` pada kotak Search
85. Verifikasi tabel sub tab Draft memuat baris `Gudang Cawang {runId}`, `Gudang Kuningan {runId}` dan tidak memuat baris `Gudang Pancoran {runId}`, `Gudang Pasar Minggu {runId}`; baris pulih dari empty state setelah Search dilepas
86. Klik `[Clear Field]`
87. Klik `[Apply]`

### Saringan tetap berlaku saat kolom disembunyikan
88. Pilih opsi `Rina W` pada field `Requested By`
89. Klik `[Apply]`
90. Klik header kolom Actions `⋯`
91. Hilangkan centang `Requested By` pada panel Column Visibility
92. Verifikasi tabel sub tab Draft memuat baris `Gudang Cawang {runId}`, `Gudang Kuningan {runId}` dan tidak memuat baris `Gudang Pancoran {runId}`, `Gudang Pasar Minggu {runId}`; kolom `Requested By` disembunyikan
93. Verifikasi field `Requested By` masih ada di panel Filter
94. Centang kembali `Requested By` pada panel Column Visibility
95. Klik `[Clear Field]`
96. Klik `[Apply]`

### Group batch diubah keluar dari saringan Group
97. Pilih Group `Gudang Kramat {runId}` pada field `Group`
98. Klik `[Apply]`
99. Verifikasi tabel sub tab Draft memuat baris `Gudang Kramat {runId}`
100. Klik ikon `Edit` pada baris `Gudang Kramat {runId}`
101. Ganti Group menjadi `Gudang Cikini {runId}`
102. Klik `[Save draft]`
103. Klik `[Cancel]` pada form yang sudah tersimpan
104. Atur field `Group` pada panel Filter menjadi `Gudang Kramat {runId}`
105. Klik `[Apply]`
106. Verifikasi `No results found` tampil
107. Klik `[Clear Field]`
108. Klik `[Apply]`

### Group batch diubah masuk ke saringan Group
109. Pilih Group `Gudang Senen {runId}` pada field `Group`
110. Klik `[Apply]`
111. Verifikasi tabel sub tab Draft memuat baris `Gudang Senen {runId}`
112. Klik ikon `Edit` pada baris `Gudang Senen {runId}`
113. Ganti Group menjadi `Gudang Kramat {runId}`
114. Klik `[Save draft]`
115. Klik `[Cancel]` pada form yang sudah tersimpan
116. Atur field `Group` pada panel Filter menjadi `Gudang Kramat {runId}`
117. Klik `[Apply]`
118. Verifikasi tabel sub tab Draft memuat baris `Gudang Kramat {runId}`

### Batch baru yang tidak cocok dengan saringan aktif tidak tampil
119. Klik `[+ Register Asset]`
120. Pilih Group `Gudang Setiabudi {runId}` pada form
121. Klik `[Save draft]`
122. Klik `[Cancel]` pada form yang sudah tersimpan
123. Atur field `Group` pada panel Filter menjadi `Gudang Kramat {runId}`
124. Klik `[Apply]`
125. Verifikasi tabel sub tab Draft memuat baris `Gudang Kramat {runId}` dan tidak memuat baris `Gudang Setiabudi {runId}`
126. Klik `[Clear Field]`
127. Klik `[Apply]`

### Batch baru muncul sebagai opsi Requested By tanpa muat ulang
128. Klik field `Requested By` pada panel Filter
129. Verifikasi opsi berisi nilai DISTINCT kolom Requested By pada tabel yang sedang tampil: daftar opsi memuat `Maya L`[^drift-1]

[^drift-1]: Drift PRD vs foundation. PRD §9.5 baris Sumber filter Requested By: User aktif dalam scope Group. foundation `prd-conventions.md` §9.8 (Opsi dropdown filter): opsi diisi nilai DISTINCT kolom sumbernya dan cakupannya mengikuti baris tabel yang sedang tampil. Diasersi: foundation, karena Filter Panel adalah pola bersama (SB-4). Aturan bisnis PRD tentang scope Group tidak dihapus: baris tabel sudah dibatasi cakupan Group aktor.
