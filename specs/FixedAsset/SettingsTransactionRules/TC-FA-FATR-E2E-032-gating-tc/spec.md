---
id: TC-FA-FATR-E2E-032-gating-tc
title: "Gating Total Control dan Default User"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [§2#r4, §2#r5, §2#p2, §4.1#r262, §4.8#r1, §4.8#r2, §4.8#r3, §4.8#r4, §4.8#r5, §4.8#r6, §4.8#r7, §4.8#r8, §4.8#r9, §4.8#r10, §4.8#r11, §4.8#r12, §9.11#r1, §9.11#r5, §9.11#r8, §10#b4]
smoke: [§9.11#r5, §9.11#r8, §10#b4]
dependsOn: []
trace:
  §2#r4: [21, 100]
  §2#r5: [7, 26, 42, 53, 64]
  §2#p2: [84, 86, 87, 89, 92, 93, 95, 97, 100, 101, 104, 105, 106, 116, 118]
  §4.1#r262: [67, 70, 73, 118]
  §4.8#r1: [2, 4, 84, 86]
  §4.8#r2: [5, 7, 87]
  §4.8#r3: [9, 89]
  §4.8#r4: [15, 95]
  §4.8#r5: [12, 16, 92]
  §4.8#r6: [13, 93]
  §4.8#r7: [18, 97]
  §4.8#r8: [27, 101]
  §4.8#r9: [30, 104]
  §4.8#r10: [31, 105]
  §4.8#r11: [32, 106]
  §4.8#r12: [67, 70, 73, 79, 118]
  §9.11#r1: [21, 100]
  §9.11#r5: 42
  §9.11#r8: 64
  §10#b4: [21, 26]
anchor: []
coverage:
  web: automated
---
# Gating Total Control dan Default User

## Prerequisites
- Aktor: Total Control `Tari Kusuma {runId}` dan Default User `Dedi Pratama {runId}`.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-032-1: User `Tari Kusuma {runId}`, tingkat akses Total Control, tanpa batas cakupan Group, ada di entitas aktor.
  - DU-032-2: User `Dedi Pratama {runId}`, Default User, tanpa batas cakupan Group, ada di entitas aktor.
  - DU-032-3: Category leaf `Mobil Operasional {runId}` di bawah Category induk `Kendaraan {runId}`, semua field transaksi Inherit.
  - DU-032-4: Category leaf `Truk Operasional {runId}` di bawah Category induk `Kendaraan {runId}`, semua field transaksi Inherit.
  - DU-032-5: Group `Proyek Karawang {runId}`, ada di entitas aktor.
  - DU-032-6: Group `Workshop Bekasi {runId}`, ada di entitas aktor.
  - DU-032-7: Asset Name `Toyota Hilux {runId}`, aktif.
  - DU-032-8: Aset `Toyota Hilux - 1 {runId}` dengan Asset Name DU-032-7 dan Category `Mobil Operasional {runId}`, status bukan Disposed.
- Kondisi:
  - Akun `Tari Kusuma {runId}` dan `Dedi Pratama {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Total Control melihat halaman, header, dan pohon kategori
1. Ketik Search Sidebar Category Tree `Mobil Operasional {runId}`, tekan Enter
2. Verifikasi Sidebar Category Tree menampilkan `All categories` dan Category `Mobil Operasional {runId}`
3. Klik Category `Mobil Operasional {runId}`
4. Verifikasi tab `Borrow`, `Assign`, `Transfer`, dan `Disposal` tampil
5. Verifikasi tombol `[Export rules]` tampil dan aktif
6. Klik `[Export rules]`
7. Verifikasi berkas aturan terunduh langsung tanpa dialog
8. Klik ikon `Changelog` pada header halaman
9. Verifikasi dialog `Changelog: Transaction Settings` tampil
10. Klik `✕` pada dialog Changelog

### Total Control mengubah dan menyimpan setting Category
11. Klik tab `Borrow`
12. Verifikasi tombol `[Set own value]` tampil pada field `Max duration`
13. Verifikasi tombol `[Reset to Default]` tampil dan aktif
14. Klik `[Set own value]` pada field `Max duration`
15. Verifikasi kontrol field `Max duration` aktif
16. Verifikasi tombol `[Reset to inherit]` tampil pada field `Max duration`
17. Ganti isi field `Max duration` dengan `21`
18. Verifikasi tombol `[Save]` tampil dan aktif
19. Klik `[Save]`
20. Klik `[Save]` pada dialog Save Changes
21. Verifikasi toast `Success, settings have been saved.` tampil
22. Muat ulang halaman
23. Ketik Search Sidebar Category Tree `Mobil Operasional {runId}`, tekan Enter
24. Klik Category `Mobil Operasional {runId}`
25. Klik tab `Borrow`
26. Verifikasi field `Max duration` bernilai `21`

### Total Control melihat opsi Scope dan menambah override Group
27. Verifikasi tombol `[+ Override]` tampil dan aktif
28. Klik `[+ Override]`
29. Klik pilihan Scope
30. Verifikasi opsi Scope `Group` tampil dan aktif
31. Verifikasi opsi Scope `Asset Name` tampil dan aktif
32. Verifikasi opsi Scope `Asset` tampil dan aktif
33. Pilih Scope `Group`
34. Klik `[Select Group]`
35. Ketik Search `Proyek Karawang {runId}`, tekan Enter
36. Centang Group `Proyek Karawang {runId}`
37. Klik `[Select]`
38. Pilih Field `Max duration`
39. Isi Value `30`
40. Klik `[Submit]`
41. Ketik Search tabel Overrides `Proyek Karawang {runId}`, tekan Enter
42. Verifikasi baris dengan Scope `Group`, Target `Proyek Karawang {runId}`, dan Overridden `Max duration (30 days)` tampil

### Total Control menambah override Asset Name
43. Klik `[+ Override]`
44. Pilih Scope `Asset Name`
45. Klik `[Select Asset Name]`
46. Ketik Search `Toyota Hilux {runId}`, tekan Enter
47. Centang baris `Toyota Hilux {runId}`
48. Klik `[Select]`
49. Pilih Field `Max duration`
50. Isi Value `10`
51. Klik `[Submit]`
52. Ganti isi kotak search tabel Overrides dengan `Toyota Hilux {runId}`, tekan Enter
53. Verifikasi baris dengan Scope `Asset Name`, Target `Toyota Hilux {runId}`, dan Overridden `Max duration (10 days)` tampil

### Total Control menambah override Asset
54. Klik `[+ Override]`
55. Pilih Scope `Asset`
56. Klik `[Select Asset]`
57. Ketik Search `Toyota Hilux - 1 {runId}`, tekan Enter
58. Centang baris `Toyota Hilux - 1 {runId}`
59. Klik `[Select]`
60. Pilih Field `Max duration`
61. Isi Value `30`
62. Klik `[Submit]`
63. Ganti isi kotak search tabel Overrides dengan `Toyota Hilux - 1 {runId}`, tekan Enter
64. Verifikasi baris dengan Scope `Asset`, Target berisi `Toyota Hilux - 1 {runId}`, dan Overridden `Max duration (30 days)` tampil

### Total Control dapat menghapus override semua scope
65. Ganti isi kotak search tabel Overrides dengan `{runId}`, tekan Enter
66. Klik menu `⋯` pada baris `Proyek Karawang {runId}`
67. Verifikasi item `Delete` aktif untuk baris override Group
68. Tekan Esc untuk menutup menu baris
69. Klik menu `⋯` pada baris `Toyota Hilux {runId}`
70. Verifikasi item `Delete` aktif untuk baris override Asset Name
71. Tekan Esc untuk menutup menu baris
72. Klik menu `⋯` pada baris `Toyota Hilux - 1 {runId}`
73. Verifikasi item `Delete` aktif untuk baris override dengan Scope `Asset`
74. Tekan Esc untuk menutup menu baris
75. Centang baris `Proyek Karawang {runId}`
76. Centang baris `Toyota Hilux {runId}`
77. Centang baris `Toyota Hilux - 1 {runId}`
78. Klik tombol aksi bulk pada toolbar tabel Overrides
79. Verifikasi aksi bulk `Delete` aktif
80. Tekan Esc untuk menutup menu aksi bulk

### Default User melihat halaman, header, dan pohon kategori
81. Keluar dari akun `Tari Kusuma {runId}`
82. Masuk sebagai `Dedi Pratama {runId}`
83. Ketik Search Sidebar Category Tree `Truk Operasional {runId}`, tekan Enter
84. Verifikasi Sidebar Category Tree menampilkan `All categories` dan Category `Truk Operasional {runId}`
85. Klik Category `Truk Operasional {runId}`
86. Verifikasi tab `Borrow`, `Assign`, `Transfer`, dan `Disposal` tampil
87. Verifikasi tombol `[Export rules]` tampil dan aktif
88. Klik ikon `Changelog` pada header halaman
89. Verifikasi dialog `Changelog: Transaction Settings` tampil
90. Klik `✕` pada dialog Changelog

### Default User mengubah dan menyimpan setting Category
91. Klik tab `Borrow`
92. Verifikasi tombol `[Set own value]` tampil pada field `Max duration`
93. Verifikasi tombol `[Reset to Default]` tampil dan aktif
94. Klik `[Set own value]` pada field `Max duration`
95. Verifikasi kontrol field `Max duration` aktif
96. Ganti isi field `Max duration` dengan `28`
97. Verifikasi tombol `[Save]` tampil dan aktif
98. Klik `[Save]`
99. Klik `[Save]` pada dialog Save Changes
100. Verifikasi toast `Success, settings have been saved.` tampil

### Default User menambah override Group dan memeriksa menu baris
101. Verifikasi tombol `[+ Override]` tampil dan aktif
102. Klik `[+ Override]`
103. Klik pilihan Scope
104. Verifikasi opsi Scope `Group` tampil dan aktif
105. Verifikasi opsi Scope `Asset Name` tampil dan aktif
106. Verifikasi opsi Scope `Asset` tampil dan aktif
107. Pilih Scope `Group`
108. Klik `[Select Group]`
109. Ketik Search `Workshop Bekasi {runId}`, tekan Enter
110. Centang Group `Workshop Bekasi {runId}`
111. Klik `[Select]`
112. Pilih Field `Max duration`
113. Isi Value `30`
114. Klik `[Submit]`
115. Ketik Search tabel Overrides `Workshop Bekasi {runId}`, tekan Enter
116. Verifikasi baris dengan Scope `Group`, Target `Workshop Bekasi {runId}`, dan Overridden `Max duration (30 days)` tampil
117. Klik menu `⋯` pada baris `Workshop Bekasi {runId}`
118. Verifikasi item `Delete` aktif untuk baris override Group
119. Tekan Esc untuk menutup menu baris
