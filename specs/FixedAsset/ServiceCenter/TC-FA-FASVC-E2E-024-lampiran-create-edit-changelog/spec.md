---
id: TC-FA-FASVC-E2E-024-lampiran-create-edit-changelog
title: "Lampiran: Tersimpan Saat Submit, Diganti dan Dihapus Saat Save, Entri Attachment di Changelog"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FASVC-07.k2", "RS-FASVC-06", "§9.6#p2", "§9.6#p3", "§9.7#r14"]
smoke: []
dependsOn: []
trace:
  "F-FASVC-07.k2": [54, 63, 64, 71]
  "RS-FASVC-06": [100, 113, 119, 120]
  "§9.6#p2": [9, 12, 13, 21, 24, 35, 38, 87, 118, 119]
  "§9.6#p3": 95
  "§9.7#r14": [12, 54, 71, 118, 119]
anchor: [50, 53, 67, 70, 86, 98, 105, 111]
coverage:
  web: automated
---
# Lampiran: Tersimpan Saat Submit, Diganti dan Dihapus Saat Save, Entri Attachment di Changelog

## Prerequisites
- Aktor: Total Control.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-024-1: Service Center `Lampiran Awal {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Segamat {runId}`, Company phone `+60 7555110101`, tanpa Attachments.
- Kondisi: unggahan berkas `foto-jaringan.jpg` gagal di tengah karena jaringan terputus.

## Test Steps

### Create dengan lampiran PDF 1 MB tepat dilampirkan saat Submit
1. Klik `[+ Service Center]`
2. Isi Name `Lampiran Baru {runId}`
3. Centang Service type `Routine`
4. Isi City `Seremban {runId}`
5. Isi Company phone dengan Dial Code `+60` dan nomor `6555070707`
6. Unggah berkas `brosur-1mb.pdf` (ukuran tepat 1 MB) pada Attachments
7. Klik `[Submit]`
8. Ketik Search `Lampiran Baru {runId}`, tekan Enter
9. Verifikasi baris `Lampiran Baru {runId}` tampil di tabel
10. Klik `[Changelog]`
11. Ketik Search `Lampiran Baru {runId}`, tekan Enter
12. Verifikasi tabel Changelog memuat tepat satu baris dengan Action `Attachment added`, Field `Attachments`, Old Value `—`, dan New Value nama berkas yang diunggah pada langkah 6
13. Verifikasi tabel Changelog memuat baris dengan Action `Created`, Field `Name`, dan New Value `Lampiran Baru {runId}`
14. Klik ikon close pada modal `Changelog: Service Center`

### Unggah lalu batal membuang berkas dan tidak menulis entri
15. Klik `(←)` pada kotak Search
16. Klik `[+ Service Center]`
17. Isi Name `Lampiran Batal {runId}`
18. Unggah berkas `foto-bengkel.jpg` (di bawah 1 MB) pada Attachments
19. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
20. Ketik Search `Lampiran Batal {runId}`, tekan Enter
21. Verifikasi tabel menampilkan empty state `No results found`
22. Klik `[Changelog]`
23. Ketik Search `Lampiran Batal {runId}`, tekan Enter
24. Verifikasi tabel Changelog menampilkan empty state `No results found`
25. Klik ikon close pada modal `Changelog: Service Center`

### Berkas valid dengan field lain tidak valid tidak membuat record
26. Klik `(←)` pada kotak Search
27. Klik `[+ Service Center]`
28. Isi Name `Lampiran Invalid {runId}`
29. Centang Service type `Routine`
30. Isi Company phone dengan Dial Code `+60` dan nomor `6555080808`
31. Unggah berkas `denah-lokasi.png` (di bawah 1 MB) pada Attachments
32. Klik `[Submit]` dengan City dibiarkan kosong
33. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
34. Ketik Search `Lampiran Invalid {runId}`, tekan Enter
35. Verifikasi tabel menampilkan empty state `No results found`
36. Klik `[Changelog]`
37. Ketik Search `Lampiran Invalid {runId}`, tekan Enter
38. Verifikasi tabel Changelog menampilkan empty state `No results found`
39. Klik ikon close pada modal `Changelog: Service Center`

### Berkas yang ditolak tidak dilampirkan
40. Klik `(←)` pada kotak Search
41. Klik `[+ Service Center]`
42. Isi Name `Lampiran Tolak {runId}`
43. Centang Service type `Routine`
44. Isi City `Kuantan {runId}`
45. Isi Company phone dengan Dial Code `+60` dan nomor `6555120202`
46. Unggah berkas `kontrak-vendor.docx` pada Attachments
47. Unggah berkas `katalog-lebih-1mb.pdf` (1 byte di atas 1 MB) pada Attachments
48. Klik `[Submit]`
49. Ketik Search `Lampiran Tolak {runId}`, tekan Enter
50. Verifikasi baris `Lampiran Tolak {runId}` tampil di tabel
51. Klik `[Changelog]`
52. Ketik Search `Lampiran Tolak {runId}`, tekan Enter
53. Verifikasi tabel Changelog memuat baris dengan Action `Created`, Field `Name`, dan New Value `Lampiran Tolak {runId}`
54. Verifikasi baris dengan Action `Attachment added` tidak tampil pada hasil Search `Lampiran Tolak {runId}`
55. Klik ikon close pada modal `Changelog: Service Center`

### Unggah gagal di tengah karena jaringan
56. Klik `(←)` pada kotak Search
57. Klik `[+ Service Center]`
58. Isi Name `Lampiran Jaringan {runId}`
59. Centang Service type `Routine`
60. Isi City `Taiping {runId}`
61. Isi Company phone dengan Dial Code `+60` dan nomor `6555130303`
62. Unggah berkas `foto-jaringan.jpg` pada Attachments
63. Verifikasi baris file `foto-jaringan.jpg` berstatus `Failed` dengan aksi `Retry`
64. Verifikasi toast `Error, failed to upload foto-jaringan.jpg.` tampil
65. Klik `[Submit]`
66. Ketik Search `Lampiran Jaringan {runId}`, tekan Enter
67. Verifikasi baris `Lampiran Jaringan {runId}` tampil di tabel
68. Klik `[Changelog]`
69. Ketik Search `Lampiran Jaringan {runId}`, tekan Enter
70. Verifikasi tabel Changelog memuat baris dengan Action `Created`, Field `Name`, dan New Value `Lampiran Jaringan {runId}`
71. Verifikasi baris dengan Action `Attachment added` tidak tampil pada hasil Search `Lampiran Jaringan {runId}`
72. Klik ikon close pada modal `Changelog: Service Center`

### Edit: unggah lalu batal dan field lain tidak valid tidak mengubah lampiran
73. Ganti isi kotak search dengan `Lampiran Awal {runId}`, tekan Enter
74. Klik `⋯` pada baris `Lampiran Awal {runId}`
75. Klik `Edit`
76. Unggah berkas `foto-cabang.jpg` (di bawah 1 MB) pada Attachments
77. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
78. Klik `⋯` pada baris `Lampiran Awal {runId}`
79. Klik `Edit`
80. Unggah berkas `peta-cabang.png` (di bawah 1 MB) pada Attachments
81. Kosongkan City
82. Klik `[Save]`
83. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
84. Klik `[Changelog]`
85. Ketik Search `Lampiran Awal {runId}`, tekan Enter
86. Verifikasi tabel Changelog memuat baris dengan Action `Created`, Field `Name`, dan New Value `Lampiran Awal {runId}`
87. Verifikasi baris dengan Action `Attachment added` tidak tampil pada hasil Search `Lampiran Awal {runId}`
88. Klik ikon close pada modal `Changelog: Service Center`

### Edit menambah PDF 1 MB, berkas yang ditolak tidak ikut
89. Klik `⋯` pada baris `Lampiran Awal {runId}`
90. Klik `Edit`
91. Unggah berkas `kontrak-vendor.docx` pada Attachments
92. Unggah berkas `katalog-lebih-1mb.pdf` (1 byte di atas 1 MB) pada Attachments
93. Unggah berkas `brosur-1mb.pdf` (ukuran tepat 1 MB) pada Attachments
94. Klik `[Save]`
95. Verifikasi toast `Success, Lampiran Awal {runId} has been updated.` tampil

### Edit mengganti berkas PDF dengan JPG lalu dengan PNG
96. Klik `⋯` pada baris `Lampiran Awal {runId}`
97. Klik `Edit`
98. Verifikasi baris file `brosur-1mb.pdf` tampil di Attachments
99. Hapus berkas pada baris file `brosur-1mb.pdf` lewat ikon hapus
100. Verifikasi baris file `brosur-1mb.pdf` tidak tampil di Attachments
101. Unggah berkas `foto-bengkel.jpg` (di bawah 1 MB) pada Attachments
102. Klik `[Save]`
103. Klik `⋯` pada baris `Lampiran Awal {runId}`
104. Klik `Edit`
105. Verifikasi baris file `foto-bengkel.jpg` tampil di Attachments
106. Hapus berkas pada baris file `foto-bengkel.jpg` lewat ikon hapus
107. Unggah berkas `denah-lokasi.png` (di bawah 1 MB) pada Attachments
108. Klik `[Save]`

### Edit menghapus lampiran
109. Klik `⋯` pada baris `Lampiran Awal {runId}`
110. Klik `Edit`
111. Verifikasi baris file `denah-lokasi.png` tampil di Attachments
112. Hapus berkas pada baris file `denah-lokasi.png` lewat ikon hapus
113. Verifikasi baris file `denah-lokasi.png` tidak tampil di Attachments
114. Klik `[Save]`

### Changelog mencatat setiap penambahan dan penghapusan lampiran saat Save
115. Klik `[Changelog]`
116. Ketik Search `Lampiran Awal {runId}`, tekan Enter
117. Pilih `50` baris per halaman pada tabel Changelog
118. Verifikasi tabel Changelog memuat tepat tiga baris dengan Action `Attachment added`, Field `Attachments`, dan Old Value `—`
119. Verifikasi tabel Changelog memuat tepat tiga baris dengan Action `Attachment removed`, Field `Attachments`, dan New Value `—`
120. Verifikasi setiap baris Action `Attachment removed` mencatat Old Value nama berkas yang diganti atau dihapus pada Edit sebelumnya
121. Klik ikon close pada modal `Changelog: Service Center`
