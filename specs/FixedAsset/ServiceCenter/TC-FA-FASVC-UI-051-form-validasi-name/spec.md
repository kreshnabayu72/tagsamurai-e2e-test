---
id: TC-FA-FASVC-UI-051-form-validasi-name
title: "Form: Validasi Name: Wajib, Unik, Maks 120, Karakter, dan Emoji"
layer: ui-client
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["V-FASVC-01", "V-FASVC-02", "V-FASVC-03", "V-FASVC-36", "FLD-FASVC-01", "EC-FASVC-01", "EC-FASVC-20a", "EC-FASVC-20b", "EC-FASVC-20c", "F-FASVC-02.k2", "F-FASVC-02.k9", "FASVC-LOGIC-02a", "FASVC-LOGIC-02b", "EB-FRM-4@name", "EB-FRM-8@name", "§4.4#r1"]
smoke: []
dependsOn: []
trace:
  "V-FASVC-01": [7, 8, 11, 99, 100, 103]
  "V-FASVC-02": [74, 77, 80, 83, 84, 91, 92, 163, 166, 169, 172, 173, 177, 178]
  "V-FASVC-03": [15, 16, 18, 27, 28, 30, 31, 33, 35, 36, 38, 107, 108, 110, 119, 120, 122, 123, 125, 127, 128, 130]
  "V-FASVC-36": [48, 49, 52, 53, 56, 141, 142, 146, 147, 151]
  "FLD-FASVC-01": [2, 3, 4, 7, 15, 18, 23, 63, 70, 74, 91, 94, 95, 99, 107, 110, 115, 155, 159, 163, 177]
  "EC-FASVC-01": [74, 77, 80, 163, 166, 169]
  "EC-FASVC-20a": [41, 42, 44, 45, 133, 134, 136, 137]
  "EC-FASVC-20b": [35, 36, 38, 127, 128, 130]
  "EC-FASVC-20c": [48, 49, 52, 53, 56, 141, 142, 146, 147, 151]
  "F-FASVC-02.k2": [74, 77, 80, 163, 166, 169]
  "F-FASVC-02.k9": [41, 42, 44, 45, 48, 52, 56, 133, 134, 136, 137, 141, 146, 151]
  "FASVC-LOGIC-02a": [74, 77, 80, 83, 84, 163, 166, 169, 172, 173]
  "FASVC-LOGIC-02b": [11, 12, 103, 104]
  "EB-FRM-4@name": [15, 16, 18, 20, 21, 24, 27, 28, 30, 31, 33, 107, 108, 110, 112, 113, 116, 119, 120, 122, 123, 125]
  "EB-FRM-8@name": [2, 3, 4, 7, 11, 15, 16, 18, 23, 27, 28, 30, 35, 41, 44, 48, 52, 56, 63, 70, 74, 77, 80, 91, 94, 95, 99, 103, 107, 108, 110, 115, 119, 120, 122, 127, 133, 136, 141, 146, 151, 155, 159, 163, 166, 169, 177]
  "§4.4#r1": [18, 20, 21, 33, 74, 110, 112, 113, 125, 163]
anchor: []
coverage:
  web: automated
---

# Form: Validasi Name: Wajib, Unik, Maks 120, Karakter, dan Emoji

## Prerequisites
- Aktor: Total Control.
- Layar awal: dialog Create / Edit Service Center yang ditampilkan menurut kondisi di bawah.
- Komponen: Dialog Create / Edit Service Center
- Data:
  - DU-051-1: pohon Group cakupan Total Control: root `All groups`, anak `Head Office`.
  - DU-051-2: Negara company pada General Settings `Indonesia`.
  - DU-051-3: Service Center untuk Edit: Name `CV Sinar Teknik Utama`, Service type `Repair`, Available to `Head Office`, Country `Indonesia`, City `Bogor`, Company email `admin@sinarteknik-utama.co.id`, field lain kosong.
  - Name pembanding keunikan: Service Center lain ber-Name `Finance Pusat` sudah ada di entitas aktor.
- Kondisi:
  - K1: dialog Create dibuka oleh Total Control; pohon Group DU-051-1 dan Negara company DU-051-2; pemeriksaan keunikan Name dijawab tidak dipakai; permintaan simpan dijawab sukses.
  - K2: seperti K1, dan pemeriksaan keunikan Name dijawab sudah dipakai bila Name, setelah spasi tepi dibuang dan tanpa membedakan huruf besar-kecil, sama dengan `Finance Pusat`.
  - K3: seperti K1, dan permintaan simpan ditolak karena Name sudah dipakai (kesalahan pada field Name).
  - K4: dialog Edit untuk Service Center DU-051-3 dibuka oleh Total Control; pohon Group DU-051-1 dan Negara company DU-051-2; pemeriksaan keunikan Name dijawab tidak dipakai; permintaan simpan dijawab sukses.
  - K5: seperti K4, dan pemeriksaan keunikan Name dijawab sudah dipakai bila Name, setelah spasi tepi dibuang dan tanpa membedakan huruf besar-kecil, sama dengan `Finance Pusat`.
  - K6: seperti K4, dan permintaan simpan ditolak karena Name sudah dipakai (kesalahan pada field Name).

## Test Steps

### Tampilan awal field Name (Create)
1. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
2. Verifikasi field `Name` menampilkan placeholder `Enter name`
3. Verifikasi field `Name` ditandai wajib
4. Verifikasi tidak ada pesan error di bawah field `Name` sebelum ada aksi

### Name kosong dan hanya spasi ditolak saat Save (Create)
5. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
6. Klik `[Submit]` dengan field `Name` kosong
7. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name must not be empty`
8. Verifikasi tidak ada permintaan simpan yang terkirim
9. Isi Name dengan `   ` (3 spasi)
10. Klik `[Submit]`
11. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name must not be empty`
12. Verifikasi tidak ada permintaan simpan yang terkirim

### Batas 120 karakter pada Name (Create)
13. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
14. Isi Name `Pusat Servis Peralatan Industri dan Kelistrikan Modern Wilayah Jawa Barat Divisi Pendingin Udara dan Genset Cabang Utama` (120 karakter)
15. Verifikasi field `Name` berisi `Pusat Servis Peralatan Industri dan Kelistrikan Modern Wilayah Jawa Barat Divisi Pendingin Udara dan Genset Cabang Utama` (120 karakter)
16. Verifikasi pesan `Max. 120 characters` tidak tampil
17. Ganti isi Name dengan `Pusat Servis Peralatan Industri dan Kelistrikan Modern Wilayah Jawa Barat Divisi Pendingin Udara dan Genset Cabang Utamai` (121 karakter)
18. Verifikasi field `Name` ditandai tidak valid dengan pesan `Max. 120 characters`
19. Ganti isi Name dengan `Pusat Servis Peralatan Industri dan Kelistrikan Modern Wilayah Jawa Barat Divisi Pendingin Udara dan Genset Cabang Utama` (120 karakter)
20. Verifikasi field `Name` berisi `Pusat Servis Peralatan Industri dan Kelistrikan Modern Wilayah Jawa Barat Divisi Pendingin Udara dan Genset Cabang Utama` (120 karakter)
21. Verifikasi pesan `Max. 120 characters` tidak tampil
22. Ganti isi Name dengan `Z`
23. Verifikasi field `Name` berisi `Z`
24. Verifikasi pesan `Max. 120 characters` tidak tampil

### Spasi tepi, spasi tengah, dan karakter Unicode dalam hitungan panjang Name (Create)
25. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
26. Isi Name `  Bengkel Resmi Layanan Perawatan Mesin Produksi dan Instalasi Listrik Gedung Perkantoran Wilayah Jawa Tengah Divisi Utama  ` (124 karakter)
27. Verifikasi field `Name` berisi `  Bengkel Resmi Layanan Perawatan Mesin Produksi dan Instalasi Listrik Gedung Perkantoran Wilayah Jawa Tengah Divisi Utama  ` (124 karakter)
28. Verifikasi pesan `Max. 120 characters` tidak tampil
29. Ganti isi Name dengan `Layanan  Teknik  Perawatan  Kompresor  dan  Pendingin  Ruangan  Industri  Makanan  Minuman  Wilayah  Jawa  Timur  Cabang` (120 karakter)
30. Verifikasi field `Name` berisi `Layanan  Teknik  Perawatan  Kompresor  dan  Pendingin  Ruangan  Industri  Makanan  Minuman  Wilayah  Jawa  Timur  Cabang` (120 karakter)
31. Verifikasi pesan `Max. 120 characters` tidak tampil
32. Ketik `x` di akhir field `Name`
33. Verifikasi field `Name` ditandai tidak valid dengan pesan `Max. 120 characters`
34. Ganti isi Name dengan `Kantor Cabang Medan Élan 𝒜 Pusat Layanan Kalibrasi Alat Ukur Presisi dan Pengujian Peralatan Laboratorium Sumatera Utara` (120 karakter)
35. Verifikasi field `Name` berisi `Kantor Cabang Medan Élan 𝒜 Pusat Layanan Kalibrasi Alat Ukur Presisi dan Pengujian Peralatan Laboratorium Sumatera Utara` (120 karakter)
36. Verifikasi pesan `Max. 120 characters` tidak tampil
37. Ketik `x` di akhir field `Name`
38. Verifikasi field `Name` ditandai tidak valid dengan pesan `Max. 120 characters`

### Karakter non-Latin dan simbol diterima pada Name (Create)
39. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
40. Isi Name `Ångström Servis 山田`
41. Verifikasi field `Name` berisi `Ångström Servis 山田`
42. Verifikasi pesan `Name contains invalid characters` tidak tampil
43. Ganti isi Name dengan `PT Servis & Kalibrasi (Cabang #2)`
44. Verifikasi field `Name` berisi `PT Servis & Kalibrasi (Cabang #2)`
45. Verifikasi pesan `Name contains invalid characters` tidak tampil

### Emoji yang diketik diblok di input Name (Create)
46. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
47. Ketik `Finance📊 Team` di field `Name`
48. Verifikasi field `Name` berisi `Finance Team`
49. Verifikasi pesan `Name contains invalid characters` tidak tampil

### Emoji yang ditempel diblok di input Name (Create)
50. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
51. Tempel `Legal📎 Team` ke field `Name`
52. Verifikasi field `Name` berisi `Legal Team`
53. Verifikasi pesan `Name contains invalid characters` tidak tampil

### Emoji yang lolos blok input memunculkan pesan pada Name (Create)
54. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
55. Lepas teks `Audit🔍 Unit` ke field `Name` dengan drag-drop
56. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name contains invalid characters`

### Spasi tepi pada Name dibuang saat Save (Create)
57. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
58. Centang checkbox `Routine`
59. Isi City `Pontianak`
60. Isi Company email `info@teknikpendingin-nusantara.co.id`
61. Isi Name `  Teknik Pendingin Nusantara  `
62. Klik `[Submit]`
63. Verifikasi Name pada permintaan simpan adalah `Teknik Pendingin Nusantara`

### Spasi tengah ganda pada Name tidak diubah saat Save (Create)
64. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
65. Centang checkbox `Routine`
66. Isi City `Pontianak`
67. Isi Company email `info@teknikpendingin-nusantara.co.id`
68. Isi Name `Teknik  Pendingin  Nusantara`
69. Klik `[Submit]`
70. Verifikasi Name pada permintaan simpan adalah `Teknik  Pendingin  Nusantara`

### Name yang sudah dipakai ditolak saat mengetik (Create)
71. Tampilkan Dialog Create / Edit Service Center dengan kondisi K2
72. Ketik Name `Finance Pusat`
73. Waktu berlalu sampai 1 detik sejak berhenti mengetik
74. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name already exists` tanpa klik `[Submit]`
75. Ganti isi Name dengan `finance pusat`
76. Waktu berlalu sampai 1 detik sejak berhenti mengetik
77. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name already exists`
78. Ganti isi Name dengan `  Finance Pusat  `
79. Waktu berlalu sampai 1 detik sejak berhenti mengetik
80. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name already exists`
81. Ganti isi Name dengan `Finance Pusat Baru`
82. Waktu berlalu sampai 1 detik sejak berhenti mengetik
83. Verifikasi field `Name` berisi `Finance Pusat Baru`
84. Verifikasi pesan `Name already exists` tidak tampil

### Name yang ditolak saat Save ditandai tidak valid (Create)
85. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
86. Centang checkbox `Routine`
87. Isi City `Pontianak`
88. Isi Company email `info@teknikpendingin-nusantara.co.id`
89. Isi Name `Finance Pusat`
90. Klik `[Submit]`
91. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name already exists`
92. Verifikasi dialog Create masih terbuka

### Tampilan awal field Name (Edit)
93. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
94. Verifikasi field `Name` terisi nilai tersimpan `CV Sinar Teknik Utama`
95. Verifikasi field `Name` ditandai wajib

### Name kosong dan hanya spasi ditolak saat Save (Edit)
96. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
97. Hapus seluruh isi field `Name`
98. Klik `[Save]`
99. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name must not be empty`
100. Verifikasi tidak ada permintaan simpan yang terkirim
101. Ganti isi Name dengan `   ` (3 spasi)
102. Klik `[Save]`
103. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name must not be empty`
104. Verifikasi tidak ada permintaan simpan yang terkirim

### Batas 120 karakter pada Name (Edit)
105. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
106. Ganti isi Name dengan `Pusat Servis Peralatan Industri dan Kelistrikan Modern Wilayah Jawa Barat Divisi Pendingin Udara dan Genset Cabang Utama` (120 karakter)
107. Verifikasi field `Name` berisi `Pusat Servis Peralatan Industri dan Kelistrikan Modern Wilayah Jawa Barat Divisi Pendingin Udara dan Genset Cabang Utama` (120 karakter)
108. Verifikasi pesan `Max. 120 characters` tidak tampil
109. Ganti isi Name dengan `Pusat Servis Peralatan Industri dan Kelistrikan Modern Wilayah Jawa Barat Divisi Pendingin Udara dan Genset Cabang Utamai` (121 karakter)
110. Verifikasi field `Name` ditandai tidak valid dengan pesan `Max. 120 characters`
111. Ganti isi Name dengan `Pusat Servis Peralatan Industri dan Kelistrikan Modern Wilayah Jawa Barat Divisi Pendingin Udara dan Genset Cabang Utama` (120 karakter)
112. Verifikasi field `Name` berisi `Pusat Servis Peralatan Industri dan Kelistrikan Modern Wilayah Jawa Barat Divisi Pendingin Udara dan Genset Cabang Utama` (120 karakter)
113. Verifikasi pesan `Max. 120 characters` tidak tampil
114. Ganti isi Name dengan `Z`
115. Verifikasi field `Name` berisi `Z`
116. Verifikasi pesan `Max. 120 characters` tidak tampil

### Spasi tepi, spasi tengah, dan karakter Unicode dalam hitungan panjang Name (Edit)
117. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
118. Ganti isi Name dengan `  Bengkel Resmi Layanan Perawatan Mesin Produksi dan Instalasi Listrik Gedung Perkantoran Wilayah Jawa Tengah Divisi Utama  ` (124 karakter)
119. Verifikasi field `Name` berisi `  Bengkel Resmi Layanan Perawatan Mesin Produksi dan Instalasi Listrik Gedung Perkantoran Wilayah Jawa Tengah Divisi Utama  ` (124 karakter)
120. Verifikasi pesan `Max. 120 characters` tidak tampil
121. Ganti isi Name dengan `Layanan  Teknik  Perawatan  Kompresor  dan  Pendingin  Ruangan  Industri  Makanan  Minuman  Wilayah  Jawa  Timur  Cabang` (120 karakter)
122. Verifikasi field `Name` berisi `Layanan  Teknik  Perawatan  Kompresor  dan  Pendingin  Ruangan  Industri  Makanan  Minuman  Wilayah  Jawa  Timur  Cabang` (120 karakter)
123. Verifikasi pesan `Max. 120 characters` tidak tampil
124. Ketik `x` di akhir field `Name`
125. Verifikasi field `Name` ditandai tidak valid dengan pesan `Max. 120 characters`
126. Ganti isi Name dengan `Kantor Cabang Medan Élan 𝒜 Pusat Layanan Kalibrasi Alat Ukur Presisi dan Pengujian Peralatan Laboratorium Sumatera Utara` (120 karakter)
127. Verifikasi field `Name` berisi `Kantor Cabang Medan Élan 𝒜 Pusat Layanan Kalibrasi Alat Ukur Presisi dan Pengujian Peralatan Laboratorium Sumatera Utara` (120 karakter)
128. Verifikasi pesan `Max. 120 characters` tidak tampil
129. Ketik `x` di akhir field `Name`
130. Verifikasi field `Name` ditandai tidak valid dengan pesan `Max. 120 characters`

### Karakter non-Latin dan simbol diterima pada Name (Edit)
131. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
132. Ganti isi Name dengan `Ångström Servis 山田`
133. Verifikasi field `Name` berisi `Ångström Servis 山田`
134. Verifikasi pesan `Name contains invalid characters` tidak tampil
135. Ganti isi Name dengan `PT Servis & Kalibrasi (Cabang #2)`
136. Verifikasi field `Name` berisi `PT Servis & Kalibrasi (Cabang #2)`
137. Verifikasi pesan `Name contains invalid characters` tidak tampil

### Emoji yang diketik diblok di input Name (Edit)
138. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
139. Hapus seluruh isi field `Name`
140. Ketik `Finance📊 Team` di field `Name`
141. Verifikasi field `Name` berisi `Finance Team`
142. Verifikasi pesan `Name contains invalid characters` tidak tampil

### Emoji yang ditempel diblok di input Name (Edit)
143. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
144. Hapus seluruh isi field `Name`
145. Tempel `Legal📎 Team` ke field `Name`
146. Verifikasi field `Name` berisi `Legal Team`
147. Verifikasi pesan `Name contains invalid characters` tidak tampil

### Emoji yang lolos blok input memunculkan pesan pada Name (Edit)
148. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
149. Hapus seluruh isi field `Name`
150. Lepas teks `Audit🔍 Unit` ke field `Name` dengan drag-drop
151. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name contains invalid characters`

### Spasi tepi pada Name dibuang saat Save (Edit)
152. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
153. Ganti isi Name dengan `  Teknik Pendingin Nusantara  `
154. Klik `[Save]`
155. Verifikasi Name pada permintaan simpan adalah `Teknik Pendingin Nusantara`

### Spasi tengah ganda pada Name tidak diubah saat Save (Edit)
156. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
157. Ganti isi Name dengan `Teknik  Pendingin  Nusantara`
158. Klik `[Save]`
159. Verifikasi Name pada permintaan simpan adalah `Teknik  Pendingin  Nusantara`

### Name yang sudah dipakai ditolak saat mengetik (Edit)
160. Tampilkan Dialog Create / Edit Service Center dengan kondisi K5
161. Ganti isi Name dengan `Finance Pusat`
162. Waktu berlalu sampai 1 detik sejak berhenti mengetik
163. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name already exists` tanpa klik `[Save]`
164. Ganti isi Name dengan `finance pusat`
165. Waktu berlalu sampai 1 detik sejak berhenti mengetik
166. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name already exists`
167. Ganti isi Name dengan `  Finance Pusat  `
168. Waktu berlalu sampai 1 detik sejak berhenti mengetik
169. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name already exists`
170. Ganti isi Name dengan `Finance Pusat Baru`
171. Waktu berlalu sampai 1 detik sejak berhenti mengetik
172. Verifikasi field `Name` berisi `Finance Pusat Baru`
173. Verifikasi pesan `Name already exists` tidak tampil

### Name yang ditolak saat Save ditandai tidak valid (Edit)
174. Tampilkan Dialog Create / Edit Service Center dengan kondisi K6
175. Ganti isi Name dengan `Finance Pusat`
176. Klik `[Save]`
177. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name already exists`
178. Verifikasi dialog Edit masih terbuka
