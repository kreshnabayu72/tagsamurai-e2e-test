---
id: TC-FA-FAFM-E2E-013-state-tabel-bertahan
title: "State tab dan tabel bertahan setelah muat ulang dan pindah tab"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.4#b7", "EB-TBL-6@tabel-files"]
smoke: []
dependsOn: []
trace:
  "§4.4#b7": [4, 6, 8, 10, 15, 16, 18, 19, 20, 22, 23]
  "EB-TBL-6@tabel-files": [10, 18, 19, 22, 23, 26, 27, 28, 30, 31, 34, 36, 40, 43, 44, 46, 49, 52, 56, 60, 63, 64, 67, 68, 81, 83, 87, 89, 92, 104, 106, 109, 111, 116, 118, 121, 123, 136, 137, 139]
anchor: [4, 6, 15, 22, 26, 30, 34, 43, 49, 56, 63, 67, 77, 98, 101, 127, 132]
coverage:
  web: automated
---

# State tab dan tabel bertahan setelah muat ulang dan pindah tab

## Prerequisites
- Aktor: Total Control, user `Fajar Nugroho {runId}` (tampil `Fajar N`), akun aktif dengan kredensial disediakan fase 2.
- Layar awal: halaman Settings > File Manager.
- Data:
  - Aset `Pompa Hidran {runId}` dan Group `Gudang Timur {runId}` ada di entitas aktor; semua file di bawah milik aset itu.
  - DU-013-1: sepuluh file tab `Asset Documents` dengan File Name `berkas-{n}-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Pompa Hidran {runId}`, Group `Gudang Timur {runId}`, Size `100.0 KB`, Uploaded By `Fajar N`.
  - DU-013-2: file tab `Asset Documents` `berkas-k-{runId}.pdf` dan DU-013-3: file `berkas-l-{runId}.pdf`, masing-masing File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Pompa Hidran {runId}`, Group `Gudang Timur {runId}`, Size `100.0 KB`, Uploaded By `Fajar N`.
  - DU-013-4: file tab `Asset Photo` `foto-a-{runId}.jpg` (File Format `JPG`) dan DU-013-5: file `foto-b-{runId}.png` (File Format `PNG`), Source `Asset Photo`, Asset `Pompa Hidran {runId}`, Group `Gudang Timur {runId}`, Size `100.0 KB`, Uploaded By `Fajar N`.
  - DU-013-6: file `lama-a-{runId}.pdf` dan DU-013-7: file `lama-b-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Asset `Pompa Hidran {runId}`, Group `Gudang Timur {runId}`, Size `100.0 KB`; keduanya sudah di-soft-delete dan berada di Recycle Bin.
  - Urutan pembuatan dari paling lama ke paling baru: DU-013-1, DU-013-2, lalu DU-013-3. DU-013-6 di-soft-delete lebih dulu daripada DU-013-7.
  - Himpunan file ber-runId di tab `Asset Documents` seluruhnya berjumlah 12: DU-013-1 sampai DU-013-3.
- Kondisi:
  - Rows per page tabel bernilai default `10`.

## Test Steps

### State Search, sort, dan halaman tab Asset Documents bertahan saat pindah ke tab lain dan kembali
1. Klik tab `Asset Documents`
2. Ketik Search `{runId}`, tekan Enter
3. Klik ikon sort pada header kolom `File Name`
4. Verifikasi Pagination menampilkan total `12` baris dalam `2` halaman
5. Klik halaman `2` pada Pagination
6. Verifikasi halaman 2 memuat dua baris dari atas ke bawah: `berkas-k-{runId}.pdf`, `berkas-l-{runId}.pdf`
7. Centang baris `berkas-k-{runId}.pdf`
8. Verifikasi penghitung seleksi `1 File selected` tampil pada tab `Asset Documents`
9. Klik tab `Asset Photo`
10. Verifikasi kotak Search pada tab `Asset Photo` kosong
11. Ketik Search `{runId}`, tekan Enter
12. Klik ikon Filter
13. Pilih File Format `JPG` pada panel Filter
14. Klik `[Apply]`
15. Verifikasi baris `foto-a-{runId}.jpg` tampil
16. Verifikasi baris `foto-b-{runId}.png` tidak tampil
17. Klik tab `Asset Documents`
18. Verifikasi kotak Search pada tab `Asset Documents` berisi `{runId}`
19. Verifikasi halaman 2 aktif dan memuat dua baris dari atas ke bawah: `berkas-k-{runId}.pdf`, `berkas-l-{runId}.pdf`
20. Verifikasi teks seleksi `1 File selected` tidak tampil dan tidak ada baris yang tercentang
21. Klik tab `Asset Photo`
22. Verifikasi baris `foto-a-{runId}.jpg` tampil
23. Verifikasi baris `foto-b-{runId}.png` tidak tampil

### State tiap tab bertahan setelah muat ulang halaman
24. Klik tab `Asset Documents`
25. Muat ulang halaman dengan F5
26. Verifikasi tab `Asset Documents` aktif
27. Verifikasi kotak Search berisi `{runId}`
28. Verifikasi halaman 2 aktif dan memuat dua baris dari atas ke bawah: `berkas-k-{runId}.pdf`, `berkas-l-{runId}.pdf`
29. Klik tab `Asset Photo`
30. Verifikasi baris `foto-a-{runId}.jpg` tampil
31. Verifikasi baris `foto-b-{runId}.png` tidak tampil
32. Klik tab `Asset Documents`
33. Pilih `Rows per page` `25` pada Pagination
34. Verifikasi seluruh `12` baris tampil dalam satu halaman
35. Muat ulang halaman dengan F5
36. Verifikasi `Rows per page` bernilai `25` dan `12` baris tampil dalam satu halaman

### State bertahan saat kembali lewat sidebar dan direset saat menu File Manager diklik di halaman itu
37. Buka halaman beranda Fixed Asset
38. Buka File Manager lewat grup `Settings` di sidebar Fixed Asset
39. Klik tab `Asset Documents`
40. Verifikasi kotak Search berisi `{runId}` dan `Rows per page` bernilai `25`
41. Klik menu `File Manager` pada grup `Settings` di sidebar Fixed Asset saat halaman File Manager sedang terbuka
42. Klik tab `Asset Documents`
43. Verifikasi `Rows per page` bernilai `10`
44. Verifikasi kotak Search pada tab `Asset Documents` kosong
45. Klik tab `Asset Photo`
46. Verifikasi kotak Search pada tab `Asset Photo` kosong

### Tab browser baru mulai dari state default
47. Klik tab `Asset Documents`
48. Ketik Search `{runId}`, tekan Enter
49. Verifikasi kotak Search berisi `{runId}`
50. Buka File Manager di tab browser baru lewat grup `Settings` di sidebar Fixed Asset
51. Klik tab `Asset Documents`
52. Verifikasi kotak Search pada tab `Asset Documents` di tab browser baru kosong
53. Tutup tab browser baru

### State dikosongkan setelah logout lalu login lagi
54. Klik tab `Asset Documents`
55. Ketik Search `{runId}`, tekan Enter
56. Verifikasi kotak Search berisi `{runId}` sebelum logout
57. Logout dari akun aktor
58. Login kembali sebagai aktor dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
59. Klik tab `Asset Documents`
60. Verifikasi kotak Search pada tab `Asset Documents` kosong sesudah login kembali

### State modal Recycle Bin kembali ke default saat dibuka lagi
61. Klik `Recycle Bin` pada header kartu `Storage Usage`
62. Ketik Search `lama-a-{runId}`, tekan Enter
63. Verifikasi baris `lama-a-{runId}.pdf` tampil di modal `Recycle Bin`
64. Verifikasi baris `lama-b-{runId}.pdf` tidak tampil di modal `Recycle Bin`
65. Tutup modal `Recycle Bin`
66. Klik `Recycle Bin` pada header kartu `Storage Usage`
67. Verifikasi baris `lama-a-{runId}.pdf` dan `lama-b-{runId}.pdf` tampil di modal `Recycle Bin`
68. Verifikasi kotak Search pada modal `Recycle Bin` kosong
69. Tutup modal `Recycle Bin`

### Sort, Filter, dan halaman bertahan saat kembali lewat sidebar
70. Klik tab `Asset Documents`
71. Ketik Search `{runId}`, tekan Enter
72. Klik ikon Filter
73. Pilih File Format `PDF` pada panel Filter
74. Klik `[Apply]`
75. Klik ikon sort pada header kolom `File Name`
76. Klik halaman `2` pada Pagination
77. Verifikasi halaman 2 aktif dan memuat dua baris dari atas ke bawah: `berkas-k-{runId}.pdf`, `berkas-l-{runId}.pdf`
78. Buka halaman beranda Fixed Asset
79. Buka File Manager lewat grup `Settings` di sidebar Fixed Asset
80. Klik tab `Asset Documents`
81. Verifikasi halaman 2 aktif dan memuat dua baris dari atas ke bawah: `berkas-k-{runId}.pdf`, `berkas-l-{runId}.pdf`
82. Klik ikon Filter
83. Verifikasi field `File Format` pada panel Filter berisi `PDF`
84. Klik ikon Filter

### Sort, Filter, dan halaman direset saat menu File Manager diklik di halaman itu
85. Klik menu `File Manager` pada grup `Settings` di sidebar Fixed Asset saat halaman File Manager sedang terbuka
86. Klik tab `Asset Documents`
87. Verifikasi halaman 1 aktif pada Pagination
88. Klik ikon Filter
89. Verifikasi field `File Format` pada panel Filter kosong dengan placeholder `All formats`
90. Klik ikon Filter
91. Ketik Search `{runId}`, tekan Enter
92. Verifikasi baris pertama halaman 1 adalah `berkas-l-{runId}.pdf`

### Tab browser baru mulai dari Sort, Filter, halaman, dan Rows per page default
93. Klik ikon Filter
94. Pilih File Format `PDF` pada panel Filter
95. Klik `[Apply]`
96. Klik ikon sort pada header kolom `File Name`
97. Klik halaman `2` pada Pagination
98. Verifikasi halaman 2 aktif dan memuat dua baris dari atas ke bawah: `berkas-k-{runId}.pdf`, `berkas-l-{runId}.pdf`
99. Klik tab `Asset Photo`
100. Pilih `Rows per page` `25` pada Pagination
101. Verifikasi `Rows per page` bernilai `25` pada tab `Asset Photo`
102. Buka File Manager di tab browser baru lewat grup `Settings` di sidebar Fixed Asset
103. Klik tab `Asset Documents`
104. Verifikasi halaman 1 aktif pada Pagination di tab browser baru
105. Klik ikon Filter
106. Verifikasi field `File Format` pada panel Filter kosong dengan placeholder `All formats`
107. Klik ikon Filter
108. Ketik Search `{runId}`, tekan Enter
109. Verifikasi baris pertama halaman 1 adalah `berkas-l-{runId}.pdf`
110. Klik tab `Asset Photo`
111. Verifikasi `Rows per page` pada tab `Asset Photo` di tab browser baru bernilai `10`
112. Tutup tab browser baru

### Login kembali mulai dari Sort, Filter, halaman, dan Rows per page default
113. Logout dari akun aktor
114. Login kembali sebagai aktor dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
115. Klik tab `Asset Documents`
116. Verifikasi halaman 1 aktif pada Pagination sesudah login kembali
117. Klik ikon Filter
118. Verifikasi field `File Format` pada panel Filter kosong dengan placeholder `All formats`
119. Klik ikon Filter
120. Ketik Search `{runId}`, tekan Enter
121. Verifikasi baris pertama halaman 1 adalah `berkas-l-{runId}.pdf`
122. Klik tab `Asset Photo`
123. Verifikasi `Rows per page` pada tab `Asset Photo` bernilai `10` sesudah login kembali

### Sort, Filter, dan Rows per page modal Recycle Bin kembali ke default saat dibuka lagi
124. Klik `Recycle Bin` pada header kartu `Storage Usage`
125. Ketik Search `{runId}`, tekan Enter
126. Klik ikon sort pada header kolom `File Name`
127. Verifikasi baris pertama modal `Recycle Bin` adalah `lama-a-{runId}.pdf`
128. Klik ikon Filter
129. Pilih File Format `PDF` pada panel Filter
130. Klik `[Apply]`
131. Pilih `Rows per page` `25` pada Pagination
132. Verifikasi `Rows per page` modal `Recycle Bin` bernilai `25`
133. Tutup modal `Recycle Bin`
134. Klik `Recycle Bin` pada header kartu `Storage Usage`
135. Ketik Search `{runId}`, tekan Enter
136. Verifikasi baris pertama modal `Recycle Bin` adalah `lama-b-{runId}.pdf`
137. Verifikasi `Rows per page` modal `Recycle Bin` bernilai `10`
138. Klik ikon Filter
139. Verifikasi field `File Format` pada panel Filter modal `Recycle Bin` kosong dengan placeholder `All formats`
140. Tutup modal `Recycle Bin`
