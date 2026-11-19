---
id: TC-FA-FASVC-UI-056-form-lampiran-unggah
title: "Form: Lampiran: Upload Satu File, Ukuran, Tipe, Gagal, Retry, dan Submit Menunggu Unggahan"
layer: ui-client
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: ["V-FASVC-12", "V-FASVC-37", "V-FASVC-38", "FLD-FASVC-18", "S-FASVC-07", "S-FASVC-10", "FI-FASVC-05", "TS-FASVC-06", "EC-FASVC-21a", "EC-FASVC-21b", "EC-FASVC-21c", "EC-FASVC-22", "EC-FASVC-41", "F-FASVC-07.k1", "F-FASVC-07.k2", "F-FASVC-07.k3", "§4.3#p1", "§4.4#r3", "§6#p1"]
smoke: []
dependsOn: []
trace:
  "V-FASVC-12": [17]
  "V-FASVC-37": [102, 103]
  "V-FASVC-38": [112, 113]
  "FLD-FASVC-18": [2, 4, 10, 13, 17, 89, 94]
  "S-FASVC-07": [5, 6, 8, 48, 50, 63, 90, 92]
  "S-FASVC-10": [32, 33, 35, 36, 38, 45, 60, 62, 72, 74, 75, 77, 84, 118, 119, 121, 123]
  "FI-FASVC-05": [33, 36, 75, 77, 118, 119, 123]
  "TS-FASVC-06": [46, 122]
  "EC-FASVC-21a": [17, 18]
  "EC-FASVC-21b": [23, 25]
  "EC-FASVC-21c": [19, 21]
  "EC-FASVC-22": [33, 45, 47, 60, 62, 65, 72, 75, 77, 118, 119, 123, 128]
  "EC-FASVC-41": [5, 6, 90]
  "F-FASVC-07.k1": [17, 18, 25]
  "F-FASVC-07.k2": [45, 46, 84, 86, 87]
  "F-FASVC-07.k3": [5, 90]
  "§4.3#p1": [47, 48, 50, 51, 53, 86, 87, 121, 123, 127, 128, 130, 131]
  "§4.4#r3": [32, 35, 45, 60, 62, 72, 74, 118, 119, 123]
  "§6#p1": [102, 103, 104, 112, 113, 114]
anchor: []
coverage:
  web: automated
---

# Form: Lampiran: Upload Satu File, Ukuran, Tipe, Gagal, Retry, dan Submit Menunggu Unggahan

## Prerequisites
- Aktor: Total Control.
- Layar awal: dialog Create / Edit Service Center yang ditampilkan menurut kondisi di bawah.
- Komponen: Dialog Create / Edit Service Center
- Data:
  - DU-056-1: pohon Group cakupan Total Control: root `All groups`, anak `Head Office`.
  - DU-056-2: Service Center untuk Edit: Name `PT Lampiran Servis Mandiri`, Service type `Routine`, Available to `Head Office`, Country `Indonesia`, City `Bandung`, Company email `admin@lampiranservis-mandiri.co.id`, Attachments `dokumen-kontrak-edit.pdf` (400 KB).
  - Nama dan ukuran berkas pada langkah tercatat di entri data DU-056-3 dan seterusnya.
- Kondisi:
  - K1: dialog Create dibuka oleh Total Control; pohon Group DU-056-1; unggahan berkas dijawab sukses; permintaan simpan dijawab sukses.
  - K2: seperti K1, dan jawaban unggahan ditahan sampai langkah menjawabnya.
  - K3: seperti K1, dan unggahan berkas pertama gagal karena jaringan; unggahan berikutnya, termasuk Retry, dijawab sukses.
  - K4: seperti K1, dan unggahan berkas pertama gagal karena jaringan; unggahan berikutnya (Retry) ditahan sampai langkah menjawabnya.
  - K5: dialog Edit untuk Service Center DU-056-2 dibuka oleh Total Control; pohon Group DU-056-1; unggahan dan permintaan simpan dijawab sukses.
  - K6: seperti K1, dan permintaan simpan ditolak karena tipe berkas bukan PDF, JPG, atau PNG.
  - K7: seperti K1, dan permintaan simpan ditolak karena berkas lebih dari 1.
  - K8: seperti K5, dan jawaban unggahan ditahan sampai langkah menjawabnya.
  - K9: seperti K5, dan unggahan berkas pertama gagal karena jaringan.

## Test Steps

### Pilih berkas PDF, JPG, dan PNG diterima dan batas 1 file
1. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
2. Verifikasi field `Attachments` tidak memiliki baris file
3. Pilih berkas `kontrak-servis.pdf` (500 KB) pada kontrol unggah `Attachments`
4. Verifikasi baris file `kontrak-servis.pdf` tampil pada field `Attachments`
5. Verifikasi kontrol unggah `Attachments` diganti teks `Up to 1 file.`
6. Verifikasi kontrol unggah `Attachments` tidak berstatus disabled karena diganti teks
7. Klik ikon hapus pada baris file `kontrak-servis.pdf`
8. Verifikasi kontrol unggah `Attachments` tampil kembali
9. Pilih berkas `foto-bengkel.jpg` (300 KB) pada kontrol unggah `Attachments`
10. Verifikasi baris file `foto-bengkel.jpg` tampil pada field `Attachments`
11. Klik ikon hapus pada baris file `foto-bengkel.jpg`
12. Pilih berkas `denah-lokasi.png` (200 KB) pada kontrol unggah `Attachments`
13. Verifikasi baris file `denah-lokasi.png` tampil pada field `Attachments`

### Berkas di atas 1 MB ditolak saat unggah
14. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
15. Isi Name `Bengkel Lampiran Servis {runId}`
16. Pilih berkas `katalog-besar.pdf` (11 MB) pada kontrol unggah `Attachments`
17. Verifikasi pesan `File size must not exceed 1 MB.` tampil di bawah field `Attachments`
18. Verifikasi field `Attachments` tidak memiliki baris file
19. Verifikasi field `Name` masih berisi `Bengkel Lampiran Servis {runId}`
20. Pilih berkas `kontrak-servis.pdf` (500 KB) pada kontrol unggah `Attachments`
21. Verifikasi baris file `kontrak-servis.pdf` tampil pada field `Attachments`

### Berkas berformat DOCX tidak dapat dipilih
22. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
23. Verifikasi kontrol unggah `Attachments` tampil
24. Pilih berkas `laporan-servis.docx` (200 KB) pada kontrol unggah `Attachments`
25. Verifikasi field `Attachments` tidak memiliki baris file

### Progres per file dan Submit menunggu unggahan selesai
26. Tampilkan Dialog Create / Edit Service Center dengan kondisi K2
27. Isi Name `Bengkel Lampiran Servis {runId}`
28. Centang checkbox `Routine`
29. Isi City `Pekanbaru`
30. Isi Company email `admin@lampiranservis-pekanbaru.co.id`
31. Pilih berkas `kontrak-servis.pdf` (500 KB) pada kontrol unggah `Attachments`
32. Verifikasi baris file `kontrak-servis.pdf` menampilkan progres unggah
33. Verifikasi `[Submit]` disabled dengan spinner selama unggahan berjalan
34. Jawaban unggahan `kontrak-servis.pdf` dikirim sukses
35. Verifikasi baris file `kontrak-servis.pdf` tampil tanpa `Failed` dan tanpa `Retry`
36. Verifikasi `[Submit]` dapat diklik
37. Klik `[Submit]`
38. Verifikasi dialog Create tertutup

### Unggah gagal menampilkan Failed dan Retry, dan baris Failed tidak dihitung terhadap batas
39. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
40. Isi Name `Bengkel Lampiran Servis {runId}`
41. Centang checkbox `Routine`
42. Isi City `Pekanbaru`
43. Isi Company email `admin@lampiranservis-pekanbaru.co.id`
44. Pilih berkas `kontrak-gagal.pdf` (400 KB) pada kontrol unggah `Attachments`
45. Verifikasi baris file `kontrak-gagal.pdf` menampilkan `Failed` dan tombol `Retry`
46. Verifikasi toast error `Error, failed to upload kontrak-gagal.pdf.` tampil
47. Verifikasi `[Submit]` dapat diklik
48. Verifikasi kontrol unggah `Attachments` masih tampil
49. Pilih berkas `kontrak-ulang.pdf` (300 KB) pada kontrol unggah `Attachments`
50. Verifikasi baris file `kontrak-ulang.pdf` tampil pada field `Attachments`
51. Verifikasi baris file `kontrak-gagal.pdf` masih menampilkan `Failed` dan tombol `Retry`
52. Klik ikon hapus pada baris file `kontrak-gagal.pdf`
53. Verifikasi baris file `kontrak-gagal.pdf` tidak lagi tampil dan baris file `kontrak-ulang.pdf` masih tampil

### Retry berhasil sesudah unggah gagal
54. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
55. Isi Name `Bengkel Lampiran Servis {runId}`
56. Centang checkbox `Routine`
57. Isi City `Pekanbaru`
58. Isi Company email `admin@lampiranservis-pekanbaru.co.id`
59. Pilih berkas `kontrak-gagal.pdf` (400 KB) pada kontrol unggah `Attachments`
60. Verifikasi baris file `kontrak-gagal.pdf` menampilkan `Failed` dan tombol `Retry`
61. Klik `Retry` pada baris file `kontrak-gagal.pdf`
62. Verifikasi baris file `kontrak-gagal.pdf` tampil tanpa `Failed` dan tanpa `Retry`
63. Verifikasi kontrol unggah `Attachments` diganti teks `Up to 1 file.`
64. Klik `[Submit]`
65. Verifikasi dialog Create tertutup

### Submit menunggu selama Retry berjalan
66. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
67. Isi Name `Bengkel Lampiran Servis {runId}`
68. Centang checkbox `Routine`
69. Isi City `Pekanbaru`
70. Isi Company email `admin@lampiranservis-pekanbaru.co.id`
71. Pilih berkas `kontrak-gagal.pdf` (400 KB) pada kontrol unggah `Attachments`
72. Verifikasi baris file `kontrak-gagal.pdf` menampilkan `Failed` dan tombol `Retry`
73. Klik `Retry` pada baris file `kontrak-gagal.pdf`
74. Verifikasi baris file `kontrak-gagal.pdf` menampilkan progres unggah
75. Verifikasi `[Submit]` disabled dengan spinner selama unggahan berjalan
76. Jawaban unggahan `kontrak-gagal.pdf` dikirim sukses
77. Verifikasi `[Submit]` dapat diklik

### Berkas yang berstatus Failed tidak dilampirkan saat Submit
78. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
79. Isi Name `Bengkel Lampiran Servis {runId}`
80. Centang checkbox `Routine`
81. Isi City `Pekanbaru`
82. Isi Company email `admin@lampiranservis-pekanbaru.co.id`
83. Pilih berkas `kontrak-gagal.pdf` (400 KB) pada kontrol unggah `Attachments`
84. Verifikasi baris file `kontrak-gagal.pdf` menampilkan `Failed` dan tombol `Retry`
85. Klik `[Submit]`
86. Verifikasi dialog Create tertutup
87. Verifikasi permintaan simpan tidak memuat berkas `kontrak-gagal.pdf`

### Lampiran tersimpan pada dialog Edit dan dapat diganti
88. Tampilkan Dialog Create / Edit Service Center dengan kondisi K5
89. Verifikasi baris file `dokumen-kontrak-edit.pdf` tampil pada field `Attachments`
90. Verifikasi kontrol unggah `Attachments` diganti teks `Up to 1 file.`
91. Klik ikon hapus pada baris file `dokumen-kontrak-edit.pdf`
92. Verifikasi kontrol unggah `Attachments` tampil kembali
93. Pilih berkas `kontrak-baru.pdf` (300 KB) pada kontrol unggah `Attachments`
94. Verifikasi baris file `kontrak-baru.pdf` tampil pada field `Attachments`

### Tipe berkas tidak valid ditolak server saat Save
95. Tampilkan Dialog Create / Edit Service Center dengan kondisi K6
96. Isi Name `Bengkel Lampiran Servis {runId}`
97. Centang checkbox `Routine`
98. Isi City `Pekanbaru`
99. Isi Company email `admin@lampiranservis-pekanbaru.co.id`
100. Pilih berkas `kontrak-servis.pdf` (500 KB) pada kontrol unggah `Attachments`
101. Klik `[Submit]`
102. Verifikasi pesan `Select a PDF, JPG, or PNG file.` tampil di bawah field `Attachments`
103. Verifikasi dialog Create masih terbuka dengan field `Name` berisi `Bengkel Lampiran Servis {runId}`
104. Verifikasi baris file `kontrak-servis.pdf` tidak tampil pada field `Attachments`

### Lebih dari 1 berkas ditolak server saat Save
105. Tampilkan Dialog Create / Edit Service Center dengan kondisi K7
106. Isi Name `Bengkel Lampiran Servis {runId}`
107. Centang checkbox `Routine`
108. Isi City `Pekanbaru`
109. Isi Company email `admin@lampiranservis-pekanbaru.co.id`
110. Pilih berkas `kontrak-servis.pdf` (500 KB) pada kontrol unggah `Attachments`
111. Klik `[Submit]`
112. Verifikasi pesan `Up to 1 file.` tampil di bawah field `Attachments`
113. Verifikasi dialog Create masih terbuka dengan field `Name` berisi `Bengkel Lampiran Servis {runId}`
114. Verifikasi baris file `kontrak-servis.pdf` tidak tampil pada field `Attachments`

### Save menunggu unggahan berjalan selesai pada dialog Edit
115. Tampilkan Dialog Create / Edit Service Center dengan kondisi K8
116. Klik ikon hapus pada baris file `dokumen-kontrak-edit.pdf`
117. Pilih berkas `kontrak-baru.pdf` (300 KB) pada kontrol unggah `Attachments`
118. Verifikasi baris file `kontrak-baru.pdf` menampilkan progres unggah
119. Verifikasi `[Save]` disabled dengan spinner selama unggahan berjalan
120. Jawaban unggahan `kontrak-baru.pdf` dikirim sukses
121. Verifikasi baris file `kontrak-baru.pdf` tampil tanpa `Failed` dan tanpa `Retry`
122. Verifikasi tidak ada toast sukses unggahan yang tampil
123. Verifikasi `[Save]` dapat diklik

### Berkas yang berstatus Failed tidak dilampirkan saat Save pada dialog Edit
124. Tampilkan Dialog Create / Edit Service Center dengan kondisi K9
125. Klik ikon hapus pada baris file `dokumen-kontrak-edit.pdf`
126. Pilih berkas `kontrak-gagal.pdf` (400 KB) pada kontrol unggah `Attachments`
127. Verifikasi baris file `kontrak-gagal.pdf` menampilkan `Failed` dan tombol `Retry`
128. Verifikasi `[Save]` dapat diklik
129. Klik `[Save]`
130. Verifikasi dialog Edit tertutup
131. Verifikasi permintaan simpan tidak memuat berkas `kontrak-gagal.pdf`
