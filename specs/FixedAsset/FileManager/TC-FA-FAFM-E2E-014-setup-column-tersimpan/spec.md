---
id: TC-FA-FAFM-E2E-014-setup-column-tersimpan
title: "Konfigurasi Setup Column tersimpan per user dan per tabel"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.4#b15", "EB-KOL-2@tabel-files"]
smoke: []
dependsOn: []
trace:
  "§4.4#b15": [31, 38, 42, 49, 50, 112, 113, 115, 137, 139, 143]
  "EB-KOL-2@tabel-files": [2, 6, 7, 10, 11, 13, 19, 24, 25, 28, 29, 31, 35, 38, 46, 49, 54, 55, 58, 62, 63, 70, 73, 76, 80, 83, 90, 93, 96, 99, 119, 120, 123, 126, 127, 130, 131, 133, 134]
anchor: [2, 6, 10, 13, 19, 24, 28, 31, 38, 42, 49, 54, 58, 62, 95, 98, 103, 108]
coverage:
  web: automated
---

# Konfigurasi Setup Column tersimpan per user dan per tabel

## Prerequisites
- Aktor: Total Control, user `Gita Maharani {runId}` (tampil `Gita M`), akun aktif dengan kredensial disediakan fase 2. Aktor kedua: Total Control lain `Hendra Wijaya {runId}` (tampil `Hendra W`) di entitas yang sama, belum pernah mengubah konfigurasi kolom.
- Layar awal: halaman Settings > File Manager.
- Data:
  - User `Gita Maharani {runId}` (DU-014-1) dan `Hendra Wijaya {runId}` (DU-014-2) ada di entitas aktor; keduanya belum punya konfigurasi kolom tersimpan.
  - Aset `Kompresor Udara {runId}` dan Group `Gudang Barat {runId}` ada di entitas aktor.
  - DU-014-4: File File Name `rencana-kerja-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Kompresor Udara {runId}`, Group `Gudang Barat {runId}`, Size `100.0 KB`, Uploaded By `Gita M`; tab `Asset Documents`.
  - DU-014-5: Aset `Bor Tangan Afkir {runId}` berstatus `Disposed` di Group `Gudang Barat {runId}`, sehingga tab `Disposed & Unmanaged Assets` memuat baris.
  - DU-014-6: File File Name `lama-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Asset `Kompresor Udara {runId}`, Group `Gudang Barat {runId}`, Size `100.0 KB`; sudah di-soft-delete dan berada di Recycle Bin.
  - DU-014-7: Entri Changelog Date `T0 − 2 hari, pukul 09:00`, Action `Delete`, File Name `lama-{runId}.pdf`, Field `File Name`, Old Value `lama-{runId}.pdf`, New Value `—`, Modified By `Gita M`.
  - DU-014-9: File File Name `sortir-a-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Kompresor Udara {runId}`, Group `Gudang Barat {runId}`, Size `100.0 KB`; sudah di-soft-delete dan berada di Recycle Bin, Deleted Date `T0 − 1 hari`.
  - DU-014-10: File File Name `sortir-b-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Kompresor Udara {runId}`, Group `Gudang Barat {runId}`, Size `100.0 KB`; sudah di-soft-delete dan berada di Recycle Bin, Deleted Date `T0 − 1 hari`, lebih akhir daripada DU-014-9.
  - DU-014-11: Entri Changelog Action `Delete`, File Name `sortir-a-{runId}.pdf`, Field `File Name`, Old Value `sortir-a-{runId}.pdf`, New Value `—`, Modified By `Gita M`, Date `T0 − 1 hari`.
  - DU-014-12: Entri Changelog Action `Delete`, File Name `sortir-b-{runId}.pdf`, Field `File Name`, Old Value `sortir-b-{runId}.pdf`, New Value `—`, Modified By `Gita M`, Date `T0 − 1 hari`, lebih akhir daripada DU-014-11.
  - DU-014-13: sembilan file `massal-{n}-{runId}.pdf` untuk n dari 1 sampai 9, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Kompresor Udara {runId}`, Group `Gudang Barat {runId}`, Size `100.0 KB`; sudah di-soft-delete dan berada di Recycle Bin, Deleted Date `T0 − 4 hari`.
  - DU-014-19: sembilan entri Changelog Action `Delete`, File Name `massal-{n}-{runId}.pdf`, Field `File Name`, Old Value `massal-{n}-{runId}.pdf`, New Value `—`, Modified By `Gita M`, Date `T0 − 4 hari`, untuk n dari 1 sampai 9.
  - DU-014-20: File File Name `foto-aset-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Kompresor Udara {runId}`, Group `Gudang Barat {runId}`, Size `100.0 KB`, Uploaded By `Gita M`; tab `Asset Photo`.
  - DU-014-21: File File Name `kerusakan-{runId}.jpg`, File Format `JPG`, Source `Damaged Photo`, Asset `Kompresor Udara {runId}`, Group `Gudang Barat {runId}`, Size `100.0 KB`, Uploaded By `Gita M`; tab `Damaged`.
  - Urutan dari paling lama ke paling baru untuk Recycle Bin dan Changelog: DU-014-6 dan DU-014-7, lalu DU-014-9 dan DU-014-11, lalu DU-014-10 dan DU-014-12.
  - Himpunan entri Changelog ber-runId seluruhnya berjumlah 12: DU-014-7, DU-014-11, DU-014-12, dan sembilan entri DU-014-19; sembilan entri DU-014-19 lebih lama daripada semua entri lain.
- Kondisi:
  - Aktor pertama dan aktor kedua memakai browser yang berbeda dengan sesi login masing-masing.

## Test Steps

### Konfigurasi kolom default sebelum ada preferensi tersimpan
1. Klik tab `Asset Documents`
2. Verifikasi header kolom `File Name`, `Reference`, dan `Group` tampil

### Kolom yang disembunyikan lewat panel Column Visibility tersimpan langsung dan bertahan setelah muat ulang
3. Klik header kolom `Actions` (`⋯`) pada tabel
4. Hilangkan centang kolom `Group` pada panel Column Visibility
5. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
6. Verifikasi header kolom `File Name` tampil di tab `Asset Documents`
7. Verifikasi header kolom `Group` tidak ada lagi di tabel tab `Asset Documents`
8. Muat ulang halaman dengan F5
9. Klik tab `Asset Documents`
10. Verifikasi header kolom `Reference` tampil sesudah muat ulang
11. Verifikasi header kolom `Group` tidak ada di tabel sesudah muat ulang

### Konfigurasi tersimpan per tabel dan tidak memengaruhi tabel lain
12. Klik tab `Disposed & Unmanaged Assets`
13. Verifikasi header kolom `Group` tampil pada tabel tab `Disposed & Unmanaged Assets`

### Setup Column modal membuang perubahan bila ditutup tanpa Save dan menyimpannya bila Save
14. Klik tab `Asset Documents`
15. Klik header kolom `Actions` (`⋯`) pada tabel
16. Klik `Setup Column...` pada panel Column Visibility
17. Hilangkan centang kolom `Reference` pada modal `Setup Column`
18. Klik `[✕]` pada modal `Setup Column`
19. Verifikasi header kolom `Reference` tampil di tabel sesudah modal `Setup Column` ditutup tanpa Save
20. Klik header kolom `Actions` (`⋯`) pada tabel
21. Klik `Setup Column...` pada panel Column Visibility
22. Hilangkan centang kolom `Reference` pada modal `Setup Column`
23. Klik `[Save]` pada modal `Setup Column`
24. Verifikasi header kolom `File Name` tampil sesudah Save
25. Verifikasi header kolom `Reference` tidak ada lagi di tabel
26. Muat ulang halaman dengan F5
27. Klik tab `Asset Documents`
28. Verifikasi header kolom `File Name` tampil sesudah muat ulang
29. Verifikasi header kolom `Reference` dan `Group` tidak ada di tabel sesudah muat ulang

### Tabel di modal Recycle Bin dan Changelog tidak menyimpan konfigurasi kolom dan kembali ke default saat dibuka lagi
30. Klik `Recycle Bin` pada header kartu `Storage Usage`
31. Verifikasi header kolom `Asset` tampil di modal `Recycle Bin`
32. Klik header kolom `Actions` (`⋯`) pada tabel
33. Hilangkan centang kolom `Asset` pada panel Column Visibility
34. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
35. Verifikasi header kolom `Asset` tidak ada lagi di modal `Recycle Bin`
36. Tutup modal `Recycle Bin`
37. Klik `Recycle Bin` pada header kartu `Storage Usage`
38. Verifikasi header kolom `Asset` tampil kembali di modal `Recycle Bin`
39. Tutup modal `Recycle Bin`
40. Klik `Changelog` pada header kartu `Storage Usage`
41. Ketik Search `lama-{runId}`, tekan Enter
42. Verifikasi entri File Name `lama-{runId}.pdf` tampil di modal `Changelog`
43. Klik header kolom `Actions` (`⋯`) pada tabel
44. Hilangkan centang kolom `Old Value` pada panel Column Visibility
45. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
46. Verifikasi header kolom `Old Value` tidak ada lagi di modal `Changelog`
47. Tutup modal `Changelog`
48. Klik `Changelog` pada header kartu `Storage Usage`
49. Verifikasi header kolom `Old Value` tampil kembali di modal `Changelog`
50. Verifikasi kotak Search pada modal `Changelog` kosong
51. Tutup modal `Changelog`

### Konfigurasi bertahan di browser lain untuk user yang sama
52. Aktor pertama login di browser lain dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
53. Klik tab `Asset Documents`
54. Verifikasi header kolom `File Name` tampil di browser lain
55. Verifikasi header kolom `Reference` dan `Group` tidak ada di tabel browser lain

### User lain tetap melihat kolom default
56. Aktor kedua login di browser lain dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
57. Klik tab `Asset Documents`
58. Verifikasi header kolom `File Name`, `Reference`, dan `Group` tampil bagi aktor kedua

### Konfigurasi bertahan setelah logout lalu login lagi
59. Aktor pertama logout dari browser awal
60. Aktor pertama login kembali dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
61. Klik tab `Asset Documents`
62. Verifikasi header kolom `File Name` tampil sesudah login kembali
63. Verifikasi header kolom `Reference` dan `Group` tidak ada di tabel sesudah login kembali

### Urutan kolom dan pin tersimpan lewat Setup Column
64. Klik tab `Asset Documents`
65. Klik header kolom `Actions` (`⋯`) pada tabel
66. Klik `Setup Column...` pada panel Column Visibility
67. Pindahkan kolom `Size` ke posisi sebelum kolom `File Format` pada modal `Setup Column`
68. Klik ikon pin pada kolom `File Name` pada modal `Setup Column`
69. Klik `[Save]` pada modal `Setup Column`
70. Verifikasi tiga kolom pertama dari kiri pada header tabel berurutan: `File Name`, `Size`, `File Format`
71. Muat ulang halaman dengan F5
72. Klik tab `Asset Documents`
73. Verifikasi tiga kolom pertama dari kiri pada header tabel berurutan: `File Name`, `Size`, `File Format` sesudah muat ulang
74. Klik header kolom `Actions` (`⋯`) pada tabel
75. Klik `Setup Column...` pada panel Column Visibility
76. Verifikasi kolom `File Name` ter-pin pada modal `Setup Column`
77. Klik `[✕]` pada modal `Setup Column`
78. Aktor pertama login di browser lain dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
79. Klik tab `Asset Documents`
80. Verifikasi tiga kolom pertama dari kiri pada header tabel berurutan: `File Name`, `Size`, `File Format` di browser lain
81. Klik header kolom `Actions` (`⋯`) pada tabel
82. Klik `Setup Column...` pada panel Column Visibility
83. Verifikasi kolom `File Name` ter-pin pada modal `Setup Column` di browser lain
84. Klik `[✕]` pada modal `Setup Column`

### Kolom tambahan Curated tersimpan lewat Setup Column
85. Klik tab `Disposed & Unmanaged Assets`
86. Klik header kolom `Actions` (`⋯`) pada tabel
87. Klik `Setup Column...` pada panel Column Visibility
88. Centang kolom `Division` pada modal `Setup Column`
89. Klik `[Save]` pada modal `Setup Column`
90. Verifikasi header kolom `Division` tampil di tabel tab `Disposed & Unmanaged Assets`
91. Muat ulang halaman dengan F5
92. Klik tab `Disposed & Unmanaged Assets`
93. Verifikasi header kolom `Division` tampil di tabel sesudah muat ulang

### Konfigurasi kolom berlaku bersama untuk semua tab Kategori
94. Klik tab `Damaged`
95. Verifikasi header kolom `File Name` tampil di tab `Damaged`
96. Verifikasi header kolom `Group` dan `Reference` tidak ada di tabel tab `Damaged`
97. Klik tab `Asset Photo`
98. Verifikasi header kolom `File Name` tampil di tab `Asset Photo`
99. Verifikasi header kolom `Group` tidak ada di tabel tab `Asset Photo`

### Sort, Filter, dan Rows per page modal Changelog kembali ke default saat dibuka lagi
100. Klik `Changelog` pada header kartu `Storage Usage`
101. Ketik Search `{runId}`, tekan Enter
102. Klik ikon sort pada header kolom `File Name`
103. Verifikasi entri pertama modal `Changelog` memuat File Name `lama-{runId}.pdf`
104. Klik ikon Filter
105. Pilih Action `Delete` pada panel Filter
106. Klik `[Apply]`
107. Pilih `Rows per page` `25` pada Pagination
108. Verifikasi `Rows per page` modal `Changelog` bernilai `25`
109. Tutup modal `Changelog`
110. Klik `Changelog` pada header kartu `Storage Usage`
111. Ketik Search `{runId}`, tekan Enter
112. Verifikasi entri pertama modal `Changelog` memuat File Name `sortir-b-{runId}.pdf`
113. Verifikasi `Rows per page` modal `Changelog` bernilai `10`
114. Klik ikon Filter
115. Verifikasi field `Action` pada panel Filter modal `Changelog` kosong dengan placeholder `All actions`
116. Tutup modal `Changelog`

### Urutan, pin, dan kolom tersembunyi berlaku di tab Kategori lain sesudah muat ulang dan di browser lain
117. Muat ulang halaman dengan F5
118. Klik tab `Damaged`
119. Verifikasi tiga kolom pertama dari kiri pada header tabel berurutan: `File Name`, `Size`, `File Format` di tab `Damaged` sesudah muat ulang
120. Verifikasi header kolom `Group` dan `Reference` tidak ada di tabel tab `Damaged` sesudah muat ulang
121. Klik header kolom `Actions` (`⋯`) pada tabel
122. Klik `Setup Column...` pada panel Column Visibility
123. Verifikasi kolom `File Name` ter-pin pada modal `Setup Column` di tab `Damaged`
124. Klik `[✕]` pada modal `Setup Column`
125. Klik tab `Asset Photo`
126. Verifikasi tiga kolom pertama dari kiri pada header tabel berurutan: `File Name`, `Size`, `File Format` di tab `Asset Photo`
127. Verifikasi header kolom `Group` tidak ada di tabel tab `Asset Photo` sesudah muat ulang
128. Aktor pertama login di browser lain dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
129. Klik tab `Damaged`
130. Verifikasi tiga kolom pertama dari kiri pada header tabel berurutan: `File Name`, `Size`, `File Format` di tab `Damaged` di browser lain
131. Verifikasi header kolom `Group` dan `Reference` tidak ada di tabel tab `Damaged` di browser lain
132. Klik tab `Asset Photo`
133. Verifikasi tiga kolom pertama dari kiri pada header tabel berurutan: `File Name`, `Size`, `File Format` di tab `Asset Photo` di browser lain
134. Verifikasi header kolom `Group` tidak ada di tabel tab `Asset Photo` di browser lain

### Halaman aktif modal Changelog kembali ke halaman 1 saat dibuka lagi
135. Klik `Changelog` pada header kartu `Storage Usage`
136. Ketik Search `{runId}`, tekan Enter
137. Verifikasi Pagination modal `Changelog` menampilkan total `12` baris dalam `2` halaman
138. Klik halaman `2` pada Pagination
139. Verifikasi halaman 2 aktif pada Pagination modal `Changelog`
140. Tutup modal `Changelog`
141. Klik `Changelog` pada header kartu `Storage Usage`
142. Ketik Search `{runId}`, tekan Enter
143. Verifikasi halaman 1 aktif pada Pagination modal `Changelog`
144. Tutup modal `Changelog`
