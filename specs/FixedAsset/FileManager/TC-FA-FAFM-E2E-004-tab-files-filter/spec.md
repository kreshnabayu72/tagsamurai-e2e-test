---
id: TC-FA-FAFM-E2E-004-tab-files-filter
title: "Filter tab Files: opsi dan hasil saringan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-FAFM-01", "TBL-03a", "TBL-08a", "TBL-08b", "§4.4#b6", "EB-FLT-1@tabel-files", "EB-FLT-3", "EB-FLT-4@tabel-files", "EB-FLT-7"]
smoke: []
dependsOn: []
trace:
  "T-FAFM-01": [4, 49, 50, 65, 91, 95, 103, 104, 107, 110, 115, 116, 119, 120, 125, 132]
  "TBL-03a": [4, 5, 6]
  "TBL-08a": [8, 10, 17, 18, 21, 22, 25, 26, 29]
  "TBL-08b": [11, 14]
  "§4.4#b6": [8]
  "EB-FLT-1@tabel-files": [8, 9, 14, 18, 22, 26, 30, 33, 34, 36, 38, 40, 43]
  "EB-FLT-3": [53, 54, 59, 60]
  "EB-FLT-4@tabel-files": [67, 68, 70, 74, 78, 83, 86, 146, 152, 163]
  "EB-FLT-7": [173, 176, 179, 180, 181]
anchor: [4, 8, 17, 21, 25, 29, 36, 49, 65, 103, 115, 131, 139, 142, 145, 151, 160, 169, 175]
coverage:
  web: automated
---

# Filter tab Files: opsi dan hasil saringan

## Prerequisites
- Aktor: Total Control, user `Wulan Sari {runId}` (tampil `Wulan S`), akun aktif dengan kredensial disediakan fase 2; aktor lain yang hanya memicu perubahan: Total Control, user `Rudi Hartono {runId}` (tampil `Rudi H`).
- Layar awal: halaman Settings > File Manager.
- Data:
  - Aset `Aset Filter {runId}`, `Printer Lama {runId}`, `Aset Hilang {runId}`, dan delapan aset `Aset Panjang {n} Untuk Uji Overflow Chip {runId}` ada di entitas aktor, semuanya di Group `Grup Filter {runId}` kecuali dinyatakan lain.
  - Semua file di bawah memakai Source Attachment atau Custom Field Document sehingga tampil di tab `Asset Documents`; Reference `Kartu Filter {runId}` adalah nama custom field.
  - Baris tanggal memakai waktu unggah relatif terhadap waktu run T0; tanggal absolut ditentukan fase 2.
  - DU-004-1: File File Name `aa-pdf-att-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-2: File File Name `bb-jpg-cfd-{runId}.jpg`, File Format `JPG`, Source `Custom Field Document`, Reference `Kartu Filter {runId}`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-3: File File Name `ab-pdf-cfd-{runId}.pdf`, File Format `PDF`, Source `Custom Field Document`, Reference `Kartu Filter {runId}`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-4: File File Name `nn-jpg-att-{runId}.jpg`, File Format `JPG`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-5: File File Name `or-png-att-{runId}.png`, File Format `PNG`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-6: File File Name `laporan-sf-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-7: File File Name `laporan-sf-{runId}.jpg`, File Format `JPG`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-8: File File Name `gambar-sf-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-9: File File Name `gambar-sf-{runId}.png`, File Format `PNG`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-10: File File Name `sz100-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-11: File File Name `sz200-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `200.0 KB`, Uploaded By `Wulan S`.
  - DU-004-12: File File Name `sz300-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `300.0 KB`, Uploaded By `Wulan S`.
  - DU-004-13: File File Name `sz400-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `400.0 KB`, Uploaded By `Wulan S`.
  - DU-004-14: File File Name `dt10-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`, Upload Date `T0 − 10 hari, pukul 11:20`.
  - DU-004-15: File File Name `dt07-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`, Upload Date `T0 − 7 hari, pukul 11:20`.
  - DU-004-16: File File Name `dt06-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`, Upload Date `T0 − 6 hari, pukul 11:20`.
  - DU-004-17: File File Name `dt05-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`, Upload Date `T0 − 5 hari, pukul 11:20`.
  - DU-004-18: File File Name `dt02-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`, Upload Date `T0 − 2 hari, pukul 11:20`.
  - DU-004-19: File File Name `dt01-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`, Upload Date `T0 − 1 hari, pukul 11:20`.
  - DU-004-20: File File Name `dmg-lain-{runId}.jpg`, File Format `JPG`, Source `Damaged Photo`, Asset `Aset Filter {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-21: File File Name `rename-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Printer Lama {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-22: File File Name `overflow-{n}-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Panjang {n} Untuk Uji Overflow Chip {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`.
  - DU-004-23: Group Group `Grup Kosong {runId}`.
  - DU-004-24: User Nama Lengkap `Pengunggah Kosong {runId}`.
  - DU-004-39: File File Name `hilang-opsi-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Aset Hilang {runId}`, Group `Grup Filter {runId}`, Size `100.0 KB`, Uploaded By `Wulan S`; satu-satunya file ber-Asset `Aset Hilang {runId}`.
  - Urutan pembuatan: DU-004-6 dibuat lebih dulu daripada DU-004-8.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.

## Test Steps

### Panel Filter memuat field menurut kolom filterable
1. Klik tab `Asset Documents`
2. Pilih ukuran halaman `100` pada Pagination
3. Klik ikon Filter
4. Verifikasi panel Filter tampil dengan field `File Format`, `Source`, `Asset`, `Group`, `Size (KB)`, `Uploaded By`, dan `Upload Date`
5. Verifikasi placeholder field berturut-turut: `All formats`, `All sources`, `All assets`, `All groups`, `Min` dan `Max`, `All users`, `Select date`
6. Verifikasi tidak ada field filter untuk `File Name`, `Reference`, dan `Asset ID`

### Opsi File Format berasal dari nilai di tabel
7. Buka dropdown field `File Format`
8. Verifikasi opsi `PDF`, `JPG`, dan `PNG` tampil
9. Verifikasi opsi `PDF` tampil satu kali walaupun banyak baris ber-File Format `PDF`
10. Verifikasi tidak ada opsi kosong di daftar `File Format`
11. Verifikasi opsi `ODT` tidak tampil karena belum ada file berformat itu
12. Pengguna lain `Rudi Hartono {runId}` menambahkan file `baru-opsi-{runId}.odt` ke aset `Aset Filter {runId}`
13. Tutup dropdown field `File Format`, lalu buka lagi
14. Verifikasi opsi `ODT` tampil sebagai opsi baru tanpa memuat ulang halaman
15. Tutup dropdown field `File Format`

### Opsi Source, Group, Uploaded By, dan Asset hanya dari data tabel
16. Buka dropdown field `Source`
17. Verifikasi opsi `Attachment` dan `Custom Field Document` tampil
18. Verifikasi opsi `Damaged Photo` tidak tampil karena hanya ada di tab `Damaged`
19. Tutup dropdown field `Source`
20. Buka pemilih Tree field `Group`
21. Verifikasi opsi `Grup Filter {runId}` tampil
22. Verifikasi opsi `Grup Kosong {runId}` tidak tampil karena tidak punya file
23. Tutup pemilih Tree field `Group`
24. Buka dropdown field `Uploaded By`
25. Verifikasi opsi `Wulan Sari {runId}` tampil dengan nama lengkap
26. Verifikasi opsi `Pengunggah Kosong {runId}` tidak tampil karena tidak punya file
27. Tutup dropdown field `Uploaded By`
28. Buka dropdown field `Asset`
29. Verifikasi opsi `Aset Filter {runId}` tampil sebagai nama aset tanpa `- [Increment]`
30. Verifikasi opsi `Printer Lama {runId}` tampil
31. Pengguna lain `Rudi Hartono {runId}` mengubah nama aset `Printer Lama {runId}` menjadi `Printer Baru {runId}`
32. Tutup dropdown field `Asset`, lalu buka lagi
33. Verifikasi opsi `Printer Baru {runId}` tampil
34. Verifikasi opsi `Printer Lama {runId}` tidak tampil

### Pencarian di dalam dropdown opsi dan chip yang meluap
35. Ketik `aset panjang` di kotak cari dropdown field `Asset`
36. Verifikasi opsi `Aset Panjang 3 Untuk Uji Overflow Chip {runId}` tampil
37. Ganti isi kotak cari dropdown dengan `Panjang 3`
38. Verifikasi opsi `Aset Panjang 3 Untuk Uji Overflow Chip {runId}` tampil
39. Ganti isi kotak cari dropdown dengan `zzqx-{runId}`
40. Verifikasi `No results found` tampil di dropdown
41. Kosongkan kotak cari dropdown
42. Pilih delapan opsi Asset dari `Aset Panjang 1 Untuk Uji Overflow Chip {runId}` sampai `Aset Panjang 8 Untuk Uji Overflow Chip {runId}`
43. Verifikasi field `Asset` menampilkan ringkasan chip `+N more`
44. Tutup dropdown field `Asset`
45. Klik `[Clear Field]`

### Filter File Format, AND antar-field, dan OR dalam satu field
46. Pilih Asset `Aset Filter {runId}` dan Group `Grup Filter {runId}` pada panel Filter
47. Pilih File Format `JPG`
48. Klik `[Apply]`
49. Verifikasi baris `bb-jpg-cfd-{runId}.jpg` tampil
50. Verifikasi baris `aa-pdf-att-{runId}.pdf` tidak tampil
51. Pilih File Format `PDF` dan `JPG`
52. Klik `[Apply]`
53. Verifikasi baris `aa-pdf-att-{runId}.pdf` dan `bb-jpg-cfd-{runId}.jpg` tampil
54. Verifikasi baris `or-png-att-{runId}.png` tidak tampil
55. Klik `[Clear Field]`
56. Pilih Asset `Aset Filter {runId}` dan Group `Grup Filter {runId}` pada panel Filter
57. Pilih File Format `PDF` dan Source `Custom Field Document`
58. Klik `[Apply]`
59. Verifikasi baris `ab-pdf-cfd-{runId}.pdf` tampil
60. Verifikasi baris `aa-pdf-att-{runId}.pdf`, `bb-jpg-cfd-{runId}.jpg`, dan `nn-jpg-att-{runId}.jpg` tidak tampil

### Irisan Search dan Filter serta pemulihan dari empty state
61. Klik `[Clear Field]`
62. Pilih Asset `Aset Filter {runId}` dan Group `Grup Filter {runId}` pada panel Filter
63. Pilih File Format `PDF`
64. Klik `[Apply]`
65. Verifikasi baris `laporan-sf-{runId}.pdf` dan `gambar-sf-{runId}.pdf` tampil
66. Ketik Search `laporan-sf-{runId}`, tekan Enter
67. Verifikasi baris `laporan-sf-{runId}.pdf` tampil
68. Verifikasi baris `gambar-sf-{runId}.pdf` dan `laporan-sf-{runId}.jpg` tidak tampil
69. Klik `(←)` pada kotak Search
70. Verifikasi baris `gambar-sf-{runId}.pdf` tampil dan filter `File Format` tetap `PDF`
71. Klik `[Clear Field]`
72. Klik `[Apply]`
73. Ketik Search `laporan-sf-{runId}`, tekan Enter
74. Verifikasi baris `laporan-sf-{runId}.pdf` dan `laporan-sf-{runId}.jpg` tampil
75. Pilih Asset `Aset Filter {runId}` dan Group `Grup Filter {runId}` pada panel Filter
76. Pilih File Format `PDF`
77. Klik `[Apply]`
78. Verifikasi hasil sama dengan menerapkan Filter lebih dulu: baris `laporan-sf-{runId}.pdf` tampil dan `laporan-sf-{runId}.jpg` tidak tampil
79. Klik `[Clear Field]`
80. Pilih Asset `Aset Filter {runId}` dan Group `Grup Filter {runId}` pada panel Filter
81. Pilih File Format `PNG`
82. Klik `[Apply]`
83. Verifikasi `No results found` tampil karena Search dan Filter masing-masing punya hasil tetapi irisannya kosong
84. Klik `[Clear Field]`
85. Klik `[Apply]`
86. Verifikasi baris `laporan-sf-{runId}.pdf` dan `laporan-sf-{runId}.jpg` tampil kembali dan Search tetap `laporan-sf-{runId}`
87. Klik `(←)` pada kotak Search

### Filter bertahan saat kolom disembunyikan
88. Pilih Asset `Aset Filter {runId}` dan Group `Grup Filter {runId}` pada panel Filter
89. Pilih File Format `PDF`
90. Klik `[Apply]`
91. Verifikasi baris `gambar-sf-{runId}.pdf` tampil dan `gambar-sf-{runId}.png` tidak tampil
92. Klik header kolom `Actions` (`⋯`) pada tabel
93. Hilangkan centang kolom `File Format` pada panel Column Visibility
94. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
95. Verifikasi field `File Format` tetap ada di panel Filter dan baris `gambar-sf-{runId}.pdf` tetap tampil
96. Klik header kolom `Actions` (`⋯`) pada tabel
97. Centang kolom `File Format` pada panel Column Visibility
98. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility

### Filter Size dengan batas inklusif dan salah satu batas kosong
99. Klik `[Clear Field]`
100. Pilih Asset `Aset Filter {runId}` dan Group `Grup Filter {runId}` pada panel Filter
101. Isi Size Min `200` dan Max `300`
102. Klik `[Apply]`
103. Verifikasi baris `sz200-{runId}.pdf` dan `sz300-{runId}.pdf` tampil
104. Verifikasi baris `sz100-{runId}.pdf` dan `sz400-{runId}.pdf` tidak tampil
105. Isi Size hanya Min `300` dengan Max kosong
106. Klik `[Apply]`
107. Verifikasi baris `sz300-{runId}.pdf` dan `sz400-{runId}.pdf` tampil dan `sz200-{runId}.pdf` tidak tampil
108. Isi Size hanya Max `200` dengan Min kosong
109. Klik `[Apply]`
110. Verifikasi baris `sz100-{runId}.pdf` dan `sz200-{runId}.pdf` tampil dan `sz300-{runId}.pdf` tidak tampil

### Filter Upload Date dengan rentang inklusif
111. Klik `[Clear Field]`
112. Pilih Asset `Aset Filter {runId}` dan Group `Grup Filter {runId}` pada panel Filter
113. Pilih rentang tanggal dari T0 − 6 hari sampai T0 − 2 hari pada field `Upload Date`
114. Klik `[Apply]`
115. Verifikasi baris `dt06-{runId}.pdf`, `dt05-{runId}.pdf`, dan `dt02-{runId}.pdf` tampil
116. Verifikasi baris `dt07-{runId}.pdf`, `dt01-{runId}.pdf`, dan `dt10-{runId}.pdf` tidak tampil
117. Pilih rentang tanggal dari T0 − 5 hari sampai T0 − 5 hari pada field `Upload Date`
118. Klik `[Apply]`
119. Verifikasi baris `dt05-{runId}.pdf` tampil
120. Verifikasi baris `dt06-{runId}.pdf` dan `dt02-{runId}.pdf` tidak tampil
121. Klik `[Clear Field]`
122. Klik `[Apply]`

### Nama aset pada baris mengikuti perubahan nama aset
123. Pilih Asset `Printer Baru {runId}` dan Group `Grup Filter {runId}` pada panel Filter
124. Klik `[Apply]`
125. Verifikasi Asset baris `rename-{runId}.pdf` tampil sebagai `[Asset Name] - [Increment]` dari aset `Printer Baru {runId}`
126. Klik `[Clear Field]`
127. Klik `[Apply]`

### Filter Uploaded By memilih pengunggah
128. Pilih Asset `Aset Filter {runId}` dan Group `Grup Filter {runId}` pada panel Filter
129. Pilih Uploaded By `Wulan Sari {runId}`
130. Klik `[Apply]`
131. Verifikasi baris `aa-pdf-att-{runId}.pdf` tampil
132. Verifikasi baris `baru-opsi-{runId}.odt` tidak tampil karena diunggah `Rudi H`
133. Klik `[Clear Field]`
134. Klik `[Apply]`

### Sort aktif bertahan saat Clear Filter dan Clear Search
135. Pilih Asset `Aset Filter {runId}` dan Group `Grup Filter {runId}` pada panel Filter
136. Pilih File Format `PDF`
137. Klik `[Apply]`
138. Ketik Search `sf-{runId}`, tekan Enter
139. Verifikasi baris `gambar-sf-{runId}.pdf` dan `laporan-sf-{runId}.pdf` tampil
140. Klik ikon sort pada header kolom `File Name`
141. Klik ikon sort pada header kolom `File Name` sekali lagi
142. Verifikasi urutan baris dari atas ke bawah: `laporan-sf-{runId}.pdf`, `gambar-sf-{runId}.pdf`
143. Klik `[Clear Field]`
144. Klik `[Apply]`
145. Verifikasi baris `laporan-sf-{runId}.jpg` dan `gambar-sf-{runId}.png` tampil
146. Verifikasi urutan baris tetap dari atas ke bawah: `laporan-sf-{runId}.pdf`, `gambar-sf-{runId}.pdf`
147. Pilih Asset `Aset Filter {runId}` dan Group `Grup Filter {runId}` pada panel Filter
148. Pilih File Format `PDF`
149. Klik `[Apply]`
150. Klik `(←)` pada kotak Search
151. Verifikasi baris `aa-pdf-att-{runId}.pdf` tampil dan baris `or-png-att-{runId}.png` tidak tampil
152. Verifikasi urutan baris tetap dari atas ke bawah: `laporan-sf-{runId}.pdf`, `gambar-sf-{runId}.pdf`
153. Klik ikon sort pada header kolom `File Name` untuk ketiga kalinya
154. Klik `[Clear Field]`
155. Klik `[Apply]`

### Record yang diubah sehingga tidak cocok tidak tampil
156. Pilih Group `Grup Filter {runId}` pada panel Filter
157. Pilih File Format `PDF`
158. Klik `[Apply]`
159. Ketik Search `Printer Baru {runId}`, tekan Enter
160. Verifikasi baris `rename-{runId}.pdf` tampil
161. Pengguna lain `Rudi Hartono {runId}` mengubah nama aset `Printer Baru {runId}` menjadi `Printer Akhir {runId}`
162. Ganti isi kotak search dengan `Printer Baru {runId}`, tekan Enter
163. Verifikasi baris `rename-{runId}.pdf` tidak tampil
164. Klik `(←)` pada kotak Search
165. Klik `[Clear Field]`
166. Klik `[Apply]`

### Nilai filter yang opsinya sudah dihapus aktor lain dibersihkan saat Apply
167. Pilih Asset `Aset Hilang {runId}` dan Group `Grup Filter {runId}` pada panel Filter
168. Klik `[Apply]`
169. Verifikasi baris `hilang-opsi-{runId}.pdf` tampil
170. Pengguna lain `Rudi Hartono {runId}` menghapus file `hilang-opsi-{runId}.pdf`
171. Klik ikon Filter untuk menutup panel Filter
172. Klik ikon Filter untuk membuka panel Filter
173. Verifikasi field `Asset` tetap mencantumkan `Aset Hilang {runId}`
174. Buka dropdown field `Asset`
175. Verifikasi opsi `Aset Filter {runId}` tampil
176. Verifikasi opsi `Aset Hilang {runId}` tidak tampil karena tidak ada lagi file dengan Asset itu
177. Tutup dropdown field `Asset`
178. Klik `[Apply]`
179. Verifikasi field `Asset` tidak lagi mencantumkan `Aset Hilang {runId}`
180. Verifikasi baris `aa-pdf-att-{runId}.pdf` tampil sesuai kriteria Group yang tersisa
181. Verifikasi tidak ada pesan error yang tampil
182. Klik `[Clear Field]`
183. Klik `[Apply]`
