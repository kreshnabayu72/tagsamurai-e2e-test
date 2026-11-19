---
id: TC-FA-FASVC-UI-053-form-validasi-alamat-dan-catatan
title: "Form: Country, Province, City, Postal Code, Address Line, dan Notes"
layer: ui-client
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["V-FASVC-11", "V-FASVC-23", "V-FASVC-24", "V-FASVC-25", "V-FASVC-28", "V-FASVC-29", "V-FASVC-33", "FLD-FASVC-06", "FLD-FASVC-07", "FLD-FASVC-08", "FLD-FASVC-09", "FLD-FASVC-10", "FLD-FASVC-17", "EC-FASVC-43", "EC-FASVC-44", "F-FASVC-02.k15", "EB-FRM-4@province-state", "EB-FRM-4@city", "EB-FRM-4@postal-code", "EB-FRM-4@address-line", "EB-FRM-4@notes", "EB-FRM-8@country", "EB-FRM-8@city"]
smoke: []
dependsOn: []
trace:
  "V-FASVC-11": [88, 89, 91, 93, 94, 96, 97, 100, 101, 103, 105, 106, 108, 109, 168, 169, 170, 175, 176, 177, 192, 193, 208, 209, 284, 285, 287, 289, 290, 292, 293, 296, 297, 299, 301, 302, 304, 305, 365, 366, 367, 373, 374, 375, 386, 387, 398, 399]
  "V-FASVC-23": [45, 48, 49, 241, 244, 245]
  "V-FASVC-24": [76, 77, 79, 81, 82, 84, 85, 148, 149, 151, 152, 155, 156, 159, 160, 163, 191, 207, 272, 273, 275, 277, 278, 280, 281, 344, 345, 347, 348, 351, 352, 355, 356, 359, 385, 397]
  "V-FASVC-25": [26, 27, 228, 229, 416, 417, 418, 421, 422]
  "V-FASVC-28": [64, 65, 67, 69, 70, 72, 73, 130, 131, 133, 134, 137, 138, 141, 142, 145, 190, 206, 260, 261, 263, 265, 266, 268, 269, 326, 327, 329, 330, 333, 334, 337, 338, 341, 384, 396]
  "V-FASVC-29": [52, 53, 55, 57, 58, 60, 61, 112, 113, 115, 116, 119, 120, 123, 124, 127, 189, 205, 248, 249, 251, 253, 254, 256, 257, 308, 309, 311, 312, 315, 316, 319, 320, 323, 383, 395]
  "V-FASVC-33": [16, 222]
  "FLD-FASVC-06": [5, 14, 16, 19, 26, 37, 211, 220, 222, 225, 228, 235]
  "FLD-FASVC-07": [6, 52, 53, 55, 57, 58, 60, 61, 112, 113, 115, 116, 119, 120, 123, 124, 127, 189, 205, 212, 248, 249, 251, 253, 254, 256, 257, 308, 309, 311, 312, 315, 316, 319, 320, 323, 383, 395]
  "FLD-FASVC-08": [5, 45, 64, 65, 67, 69, 70, 72, 73, 130, 131, 133, 134, 137, 138, 141, 142, 145, 190, 206, 213, 241, 260, 261, 263, 265, 266, 268, 269, 326, 327, 329, 330, 333, 334, 337, 338, 341, 384, 396, 405, 408]
  "FLD-FASVC-09": [2, 6, 76, 77, 79, 81, 82, 84, 85, 148, 149, 151, 152, 155, 156, 159, 160, 163, 191, 207, 214, 272, 273, 275, 277, 278, 280, 281, 344, 345, 347, 348, 351, 352, 355, 356, 359, 385, 397]
  "FLD-FASVC-10": [3, 6, 88, 89, 91, 93, 94, 96, 97, 168, 169, 170, 192, 208, 215, 284, 285, 287, 289, 290, 292, 293, 365, 366, 367, 386, 398]
  "FLD-FASVC-17": [4, 6, 100, 101, 103, 105, 106, 108, 109, 175, 176, 177, 193, 209, 216, 296, 297, 299, 301, 302, 304, 305, 373, 374, 375, 387, 399]
  "EC-FASVC-43": [405, 408, 409]
  "EC-FASVC-44": [37, 38, 39, 235, 236, 237]
  "F-FASVC-02.k15": [37, 38, 235, 236, 408]
  "EB-FRM-4@province-state": [52, 53, 55, 57, 58, 60, 61, 112, 113, 115, 116, 119, 120, 123, 124, 127, 189, 205, 248, 249, 251, 253, 254, 256, 257, 308, 309, 311, 312, 315, 316, 319, 320, 323, 383, 395]
  "EB-FRM-4@city": [64, 65, 67, 69, 70, 72, 73, 130, 131, 133, 134, 137, 138, 141, 142, 145, 190, 206, 260, 261, 263, 265, 266, 268, 269, 326, 327, 329, 330, 333, 334, 337, 338, 341, 384, 396]
  "EB-FRM-4@postal-code": [76, 77, 79, 81, 82, 84, 85, 148, 149, 151, 152, 155, 156, 159, 160, 163, 191, 207, 272, 273, 275, 277, 278, 280, 281, 344, 345, 347, 348, 351, 352, 355, 356, 359, 385, 397]
  "EB-FRM-4@address-line": [88, 89, 91, 93, 94, 96, 97, 168, 169, 170, 192, 208, 284, 285, 287, 289, 290, 292, 293, 365, 366, 367, 386, 398]
  "EB-FRM-4@notes": [100, 101, 103, 105, 106, 108, 109, 175, 176, 177, 193, 209, 296, 297, 299, 301, 302, 304, 305, 373, 374, 375, 387, 399]
  "EB-FRM-8@country": [16, 19, 26, 222, 225, 228]
  "EB-FRM-8@city": [45, 48, 64, 65, 67, 69, 70, 72, 73, 130, 131, 133, 134, 137, 138, 141, 142, 145, 190, 206, 241, 244, 260, 261, 263, 265, 266, 268, 269, 326, 327, 329, 330, 333, 334, 337, 338, 341, 384, 396]
anchor: []
coverage:
  web: automated
---

# Form: Country, Province, City, Postal Code, Address Line, dan Notes

## Prerequisites
- Aktor: Total Control.
- Layar awal: dialog Create / Edit Service Center yang ditampilkan menurut kondisi di bawah.
- Komponen: Dialog Create / Edit Service Center
- Data:
  - DU-053-1: pohon Group cakupan Total Control: root `All groups`, anak `Head Office`.
  - DU-053-2: daftar negara `Indonesia`, `Malaysia`, dan `Singapore`; Negara company pada General Settings `Indonesia`.
  - DU-053-3: Service Center untuk Edit: Name `PT Alamat Servis Terpadu`, Service type `Routine`, Available to `Head Office`, Country `Indonesia`, Province / State `Jawa Barat`, City `Bandung`, Postal code `40115`, Address line `Jl. Asia Afrika No. 12`, Notes `Rekanan resmi servis pendingin`, Company email `cs@alamatservis-terpadu.co.id`.
  - DU-053-4: saran City dari Service Center lain: `Jakarta Selatan` dan `Jakarta Barat`.
  - Nilai tiap field pada langkah tercatat di entri data DU-053-5 dan seterusnya.
- Kondisi:
  - K1: dialog Create dibuka oleh Total Control; pohon Group DU-053-1 dan daftar negara DU-053-2; permintaan simpan dijawab sukses.
  - K2: seperti K1, dan permintaan simpan ditolak karena Country di luar daftar negara.
  - K3: dialog Edit untuk Service Center DU-053-3 dibuka oleh Total Control; pohon Group DU-053-1 dan daftar negara DU-053-2; permintaan simpan dijawab sukses.
  - K4: seperti K3, dan permintaan simpan ditolak karena Country di luar daftar negara.
  - K5: seperti K1, dan saran City DU-053-4 tersedia.

## Test Steps

### Nilai awal field alamat dan catatan (Create)
1. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
2. Verifikasi field `Postal code` menampilkan placeholder `Enter postal code`
3. Verifikasi field `Address line` menampilkan placeholder `Enter address line`
4. Verifikasi field `Notes` menampilkan placeholder `Enter notes`
5. Verifikasi field `Country` ditandai wajib dan field `City` ditandai wajib
6. Verifikasi field `Province / State`, `Postal code`, `Address line`, dan `Notes` tidak ditandai wajib

### Country dikosongkan ditolak saat Save (Create)
7. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
8. Isi Name `Bengkel Alamat Servis {runId}`
9. Centang checkbox `Routine`
10. Isi City `Cirebon`
11. Isi Company email `ops@alamatservis-cirebon.co.id`
12. Klik field `Country`
13. Klik opsi `Indonesia` yang sedang terpilih untuk mengosongkannya
14. Verifikasi field `Country` menampilkan placeholder `Select country`
15. Klik `[Submit]`
16. Verifikasi field `Country` ditandai tidak valid dengan pesan `Country must not be empty`
17. Klik field `Country`
18. Klik opsi `Malaysia`
19. Verifikasi field `Country` menampilkan `Malaysia`

### Country di luar daftar ditolak server saat Save (Create)
20. Tampilkan Dialog Create / Edit Service Center dengan kondisi K2
21. Isi Name `Bengkel Alamat Servis {runId}`
22. Centang checkbox `Routine`
23. Isi City `Cirebon`
24. Isi Company email `ops@alamatservis-cirebon.co.id`
25. Klik `[Submit]`
26. Verifikasi field `Country` ditandai tidak valid dengan pesan `Select a valid country`
27. Verifikasi dialog Create masih terbuka

### Vendor di luar negeri: Country diubah (Create)
28. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
29. Isi Name `Bengkel Alamat Servis {runId}`
30. Centang checkbox `Routine`
31. Isi City `Cirebon`
32. Isi Company email `ops@alamatservis-cirebon.co.id`
33. Klik field `Country`
34. Klik opsi `Malaysia`
35. Ganti isi City dengan `Johor Bahru`
36. Klik `[Submit]`
37. Verifikasi Country pada permintaan simpan adalah `Malaysia`
38. Verifikasi City pada permintaan simpan adalah `Johor Bahru`
39. Verifikasi dialog Create tertutup

### City kosong dan hanya spasi ditolak saat Save (Create)
40. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
41. Isi Name `Bengkel Alamat Servis {runId}`
42. Centang checkbox `Routine`
43. Isi Company email `ops@alamatservis-cirebon.co.id`
44. Klik `[Submit]` dengan field `City` kosong
45. Verifikasi field `City` ditandai tidak valid dengan pesan `City must not be empty`
46. Ganti isi City dengan `   `
47. Klik `[Submit]`
48. Verifikasi field `City` ditandai tidak valid dengan pesan `City must not be empty`
49. Verifikasi tidak ada permintaan simpan yang terkirim

### Batas 120 karakter pada Province / State (Create)
50. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
51. Isi Province / State `Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa` (120 karakter)
52. Verifikasi field `Province / State` berisi `Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa` (120 karakter)
53. Verifikasi pesan `Max. 120 characters` tidak tampil
54. Ganti isi Province / State dengan `Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawai` (121 karakter)
55. Verifikasi field `Province / State` ditandai tidak valid dengan pesan `Max. 120 characters`
56. Ganti isi Province / State dengan `Jawa  Barat  Wilayah  Pegunungan  Tengah  Kabupaten  Perbukitan  Jawa  Barat  Wilayah  Pegunungan  Tengah  Kabupaten  Pe` (120 karakter)
57. Verifikasi field `Province / State` berisi `Jawa  Barat  Wilayah  Pegunungan  Tengah  Kabupaten  Perbukitan  Jawa  Barat  Wilayah  Pegunungan  Tengah  Kabupaten  Pe` (120 karakter)
58. Verifikasi pesan `Max. 120 characters` tidak tampil
59. Ganti isi Province / State dengan `  Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa  ` (124 karakter)
60. Verifikasi field `Province / State` berisi `  Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa  ` (124 karakter)
61. Verifikasi pesan `Max. 120 characters` tidak tampil

### Batas 120 karakter pada City (Create)
62. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
63. Isi City `Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawa` (120 karakter)
64. Verifikasi field `City` berisi `Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawa` (120 karakter)
65. Verifikasi pesan `Max. 120 characters` tidak tampil
66. Ganti isi City dengan `Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawai` (121 karakter)
67. Verifikasi field `City` ditandai tidak valid dengan pesan `Max. 120 characters`
68. Ganti isi City dengan `Kota  Bandung  Raya  Kawasan  Industri  Selatan  Pusat  Kota  Bandung  Raya  Kawasan  Industri  Selatan  Pusat  Kota  Ba` (120 karakter)
69. Verifikasi field `City` berisi `Kota  Bandung  Raya  Kawasan  Industri  Selatan  Pusat  Kota  Bandung  Raya  Kawasan  Industri  Selatan  Pusat  Kota  Ba` (120 karakter)
70. Verifikasi pesan `Max. 120 characters` tidak tampil
71. Ganti isi City dengan `  Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawa  ` (124 karakter)
72. Verifikasi field `City` berisi `  Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawa  ` (124 karakter)
73. Verifikasi pesan `Max. 120 characters` tidak tampil

### Batas 120 karakter pada Postal code (Create)
74. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
75. Isi Postal code `40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119a` (120 karakter)
76. Verifikasi field `Postal code` berisi `40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119a` (120 karakter)
77. Verifikasi pesan `Max. 120 characters` tidak tampil
78. Ganti isi Postal code dengan `40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119ai` (121 karakter)
79. Verifikasi field `Postal code` ditandai tidak valid dengan pesan `Max. 120 characters`
80. Ganti isi Postal code dengan `40115  40116  40117  40118  40119  40115  40116  40117  40118  40119  40115  40116  40117  40118  40119  40115  40116  4` (120 karakter)
81. Verifikasi field `Postal code` berisi `40115  40116  40117  40118  40119  40115  40116  40117  40118  40119  40115  40116  40117  40118  40119  40115  40116  4` (120 karakter)
82. Verifikasi pesan `Max. 120 characters` tidak tampil
83. Ganti isi Postal code dengan `  40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119a  ` (124 karakter)
84. Verifikasi field `Postal code` berisi `  40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119a  ` (124 karakter)
85. Verifikasi pesan `Max. 120 characters` tidak tampil

### Batas 360 karakter pada Address line (Create)
86. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
87. Isi Address line `Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia` (360 karakter)
88. Verifikasi field `Address line` berisi `Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia` (360 karakter)
89. Verifikasi pesan `Max. 360 characters` tidak tampil
90. Ganti isi Address line dengan `Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asiai` (361 karakter)
91. Verifikasi field `Address line` ditandai tidak valid dengan pesan `Max. 360 characters`
92. Ganti isi Address line dengan `Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Serv` (360 karakter)
93. Verifikasi field `Address line` berisi `Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Serv` (360 karakter)
94. Verifikasi pesan `Max. 360 characters` tidak tampil
95. Ganti isi Address line dengan `  Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia  ` (364 karakter)
96. Verifikasi field `Address line` berisi `  Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia  ` (364 karakter)
97. Verifikasi pesan `Max. 360 characters` tidak tampil

### Batas 360 karakter pada Notes (Create)
98. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
99. Isi Notes `Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekan` (360 karakter)
100. Verifikasi field `Notes` berisi `Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekan` (360 karakter)
101. Verifikasi pesan `Max. 360 characters` tidak tampil
102. Ganti isi Notes dengan `Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekani` (361 karakter)
103. Verifikasi field `Notes` ditandai tidak valid dengan pesan `Max. 360 characters`
104. Ganti isi Notes dengan `Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  r` (360 karakter)
105. Verifikasi field `Notes` berisi `Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  r` (360 karakter)
106. Verifikasi pesan `Max. 360 characters` tidak tampil
107. Ganti isi Notes dengan `  Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekan  ` (364 karakter)
108. Verifikasi field `Notes` berisi `  Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekan  ` (364 karakter)
109. Verifikasi pesan `Max. 360 characters` tidak tampil

### Karakter yang diizinkan dan emoji diblok pada Province / State (Create)
110. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
111. Isi Province / State `Jawa Barat 西爪哇`
112. Verifikasi field `Province / State` berisi `Jawa Barat 西爪哇`
113. Verifikasi pesan `Province / State contains invalid characters` tidak tampil
114. Ganti isi Province / State dengan `D.I. Yogyakarta (DIY) / Kulon-Progo`
115. Verifikasi field `Province / State` berisi `D.I. Yogyakarta (DIY) / Kulon-Progo`
116. Verifikasi pesan `Province / State contains invalid characters` tidak tampil
117. Hapus seluruh isi field `Province / State`
118. Ketik `Banten🔥 Raya` di field `Province / State`
119. Verifikasi field `Province / State` berisi `Banten Raya`
120. Verifikasi pesan `Province / State contains invalid characters` tidak tampil
121. Hapus seluruh isi field `Province / State`
122. Tempel `Jambi📎 Utara` ke field `Province / State`
123. Verifikasi field `Province / State` berisi `Jambi Utara`
124. Verifikasi pesan `Province / State contains invalid characters` tidak tampil
125. Hapus seluruh isi field `Province / State`
126. Lepas teks `Riau🔍 Timur` ke field `Province / State` dengan drag-drop
127. Verifikasi field `Province / State` ditandai tidak valid dengan pesan `Province / State contains invalid characters`

### Karakter yang diizinkan dan emoji diblok pada City (Create)
128. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
129. Isi City `Bandung 万隆`
130. Verifikasi field `City` berisi `Bandung 万隆`
131. Verifikasi pesan `City contains invalid characters` tidak tampil
132. Ganti isi City dengan `Kota Baru #2 & Sekitarnya`
133. Verifikasi field `City` berisi `Kota Baru #2 & Sekitarnya`
134. Verifikasi pesan `City contains invalid characters` tidak tampil
135. Hapus seluruh isi field `City`
136. Ketik `Bogor📍 Kota` di field `City`
137. Verifikasi field `City` berisi `Bogor Kota`
138. Verifikasi pesan `City contains invalid characters` tidak tampil
139. Hapus seluruh isi field `City`
140. Tempel `Garut📌 Kota` ke field `City`
141. Verifikasi field `City` berisi `Garut Kota`
142. Verifikasi pesan `City contains invalid characters` tidak tampil
143. Hapus seluruh isi field `City`
144. Lepas teks `Cimahi🔍 Selatan` ke field `City` dengan drag-drop
145. Verifikasi field `City` ditandai tidak valid dengan pesan `City contains invalid characters`

### Karakter yang diizinkan dan emoji diblok pada Postal code (Create)
146. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
147. Isi Postal code `Ж-40115`
148. Verifikasi field `Postal code` berisi `Ж-40115`
149. Verifikasi pesan `Postal code contains invalid characters` tidak tampil
150. Ganti isi Postal code dengan `40115-A/2 (#3)`
151. Verifikasi field `Postal code` berisi `40115-A/2 (#3)`
152. Verifikasi pesan `Postal code contains invalid characters` tidak tampil
153. Hapus seluruh isi field `Postal code`
154. Ketik `40📊115` di field `Postal code`
155. Verifikasi field `Postal code` berisi `40115`
156. Verifikasi pesan `Postal code contains invalid characters` tidak tampil
157. Hapus seluruh isi field `Postal code`
158. Tempel `61📎254` ke field `Postal code`
159. Verifikasi field `Postal code` berisi `61254`
160. Verifikasi pesan `Postal code contains invalid characters` tidak tampil
161. Hapus seluruh isi field `Postal code`
162. Lepas teks `17🔍510` ke field `Postal code` dengan drag-drop
163. Verifikasi field `Postal code` ditandai tidak valid dengan pesan `Postal code contains invalid characters`

### Karakter bebas pada Address line (Create)
164. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
165. Ketik `Ruko Blok A 🏠 No. 7 & 8` di field `Address line`
166. Tekan `Enter` pada field `Address line`
167. Ketik `Lantai 2 #05 😊 (belakang)` di field `Address line`
168. Verifikasi field `Address line` berisi dua baris `Ruko Blok A 🏠 No. 7 & 8` dan `Lantai 2 #05 😊 (belakang)`
169. Verifikasi pesan `Address line contains invalid characters` tidak tampil
170. Verifikasi dialog Create tidak menampilkan error pada field `Address line`

### Karakter bebas pada Notes (Create)
171. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
172. Ketik `Rekanan 🔥 resmi` di field `Notes`
173. Tekan `Enter` pada field `Notes`
174. Ketik `Garansi 1 tahun + servis gratis!` di field `Notes`
175. Verifikasi field `Notes` berisi dua baris `Rekanan 🔥 resmi` dan `Garansi 1 tahun + servis gratis!`
176. Verifikasi pesan `Notes contains invalid characters` tidak tampil
177. Verifikasi dialog Create tidak menampilkan error pada field `Notes`

### Spasi tepi pada field alamat dan catatan dibuang saat Save (Create)
178. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
179. Isi Name `Bengkel Alamat Servis {runId}`
180. Centang checkbox `Routine`
181. Isi City `Cirebon`
182. Isi Company email `ops@alamatservis-cirebon.co.id`
183. Isi Province / State `  Jawa Tengah  `
184. Isi City `  Semarang  `
185. Isi Postal code `  50132  `
186. Isi Address line `  Jl. Pemuda No. 21  `
187. Isi Notes `  Rekanan resmi servis kompresor  `
188. Klik `[Submit]`
189. Verifikasi Province / State pada permintaan simpan adalah `Jawa Tengah`
190. Verifikasi City pada permintaan simpan adalah `Semarang`
191. Verifikasi Postal code pada permintaan simpan adalah `50132`
192. Verifikasi Address line pada permintaan simpan adalah `Jl. Pemuda No. 21`
193. Verifikasi Notes pada permintaan simpan adalah `Rekanan resmi servis kompresor`

### Spasi tengah pada field alamat dan catatan tidak diubah saat Save (Create)
194. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
195. Isi Name `Bengkel Alamat Servis {runId}`
196. Centang checkbox `Routine`
197. Isi City `Cirebon`
198. Isi Company email `ops@alamatservis-cirebon.co.id`
199. Isi Province / State `Jawa  Timur Selatan`
200. Isi City `Kota  Batu Raya`
201. Isi Postal code `65  311 A`
202. Isi Address line `Jl.  Ijen No. 8  Blok C`
203. Isi Notes `Rekanan  resmi servis  AC`
204. Klik `[Submit]`
205. Verifikasi Province / State pada permintaan simpan adalah `Jawa  Timur Selatan`
206. Verifikasi City pada permintaan simpan adalah `Kota  Batu Raya`
207. Verifikasi Postal code pada permintaan simpan adalah `65  311 A`
208. Verifikasi Address line pada permintaan simpan adalah `Jl.  Ijen No. 8  Blok C`
209. Verifikasi Notes pada permintaan simpan adalah `Rekanan  resmi servis  AC`

### Nilai awal field alamat dan catatan (Edit)
210. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
211. Verifikasi field `Country` menampilkan `Indonesia`
212. Verifikasi field `Province / State` berisi `Jawa Barat`
213. Verifikasi field `City` berisi `Bandung`
214. Verifikasi field `Postal code` berisi `40115`
215. Verifikasi field `Address line` berisi `Jl. Asia Afrika No. 12`
216. Verifikasi field `Notes` berisi `Rekanan resmi servis pendingin`

### Country dikosongkan ditolak saat Save (Edit)
217. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
218. Klik field `Country`
219. Klik opsi `Indonesia` yang sedang terpilih untuk mengosongkannya
220. Verifikasi field `Country` menampilkan placeholder `Select country`
221. Klik `[Save]`
222. Verifikasi field `Country` ditandai tidak valid dengan pesan `Country must not be empty`
223. Klik field `Country`
224. Klik opsi `Malaysia`
225. Verifikasi field `Country` menampilkan `Malaysia`

### Country di luar daftar ditolak server saat Save (Edit)
226. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
227. Klik `[Save]`
228. Verifikasi field `Country` ditandai tidak valid dengan pesan `Select a valid country`
229. Verifikasi dialog Edit masih terbuka

### Vendor di luar negeri: Country diubah (Edit)
230. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
231. Klik field `Country`
232. Klik opsi `Malaysia`
233. Ganti isi City dengan `Johor Bahru`
234. Klik `[Save]`
235. Verifikasi Country pada permintaan simpan adalah `Malaysia`
236. Verifikasi City pada permintaan simpan adalah `Johor Bahru`
237. Verifikasi dialog Edit tertutup

### City kosong dan hanya spasi ditolak saat Save (Edit)
238. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
239. Hapus seluruh isi field `City`
240. Klik `[Save]`
241. Verifikasi field `City` ditandai tidak valid dengan pesan `City must not be empty`
242. Ganti isi City dengan `   `
243. Klik `[Save]`
244. Verifikasi field `City` ditandai tidak valid dengan pesan `City must not be empty`
245. Verifikasi tidak ada permintaan simpan yang terkirim

### Batas 120 karakter pada Province / State (Edit)
246. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
247. Ganti isi Province / State dengan `Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa` (120 karakter)
248. Verifikasi field `Province / State` berisi `Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa` (120 karakter)
249. Verifikasi pesan `Max. 120 characters` tidak tampil
250. Ganti isi Province / State dengan `Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawai` (121 karakter)
251. Verifikasi field `Province / State` ditandai tidak valid dengan pesan `Max. 120 characters`
252. Ganti isi Province / State dengan `Jawa  Barat  Wilayah  Pegunungan  Tengah  Kabupaten  Perbukitan  Jawa  Barat  Wilayah  Pegunungan  Tengah  Kabupaten  Pe` (120 karakter)
253. Verifikasi field `Province / State` berisi `Jawa  Barat  Wilayah  Pegunungan  Tengah  Kabupaten  Perbukitan  Jawa  Barat  Wilayah  Pegunungan  Tengah  Kabupaten  Pe` (120 karakter)
254. Verifikasi pesan `Max. 120 characters` tidak tampil
255. Ganti isi Province / State dengan `  Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa  ` (124 karakter)
256. Verifikasi field `Province / State` berisi `  Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa Barat Wilayah Pegunungan Tengah Kabupaten Perbukitan Jawa  ` (124 karakter)
257. Verifikasi pesan `Max. 120 characters` tidak tampil

### Batas 120 karakter pada City (Edit)
258. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
259. Ganti isi City dengan `Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawa` (120 karakter)
260. Verifikasi field `City` berisi `Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawa` (120 karakter)
261. Verifikasi pesan `Max. 120 characters` tidak tampil
262. Ganti isi City dengan `Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawai` (121 karakter)
263. Verifikasi field `City` ditandai tidak valid dengan pesan `Max. 120 characters`
264. Ganti isi City dengan `Kota  Bandung  Raya  Kawasan  Industri  Selatan  Pusat  Kota  Bandung  Raya  Kawasan  Industri  Selatan  Pusat  Kota  Ba` (120 karakter)
265. Verifikasi field `City` berisi `Kota  Bandung  Raya  Kawasan  Industri  Selatan  Pusat  Kota  Bandung  Raya  Kawasan  Industri  Selatan  Pusat  Kota  Ba` (120 karakter)
266. Verifikasi pesan `Max. 120 characters` tidak tampil
267. Ganti isi City dengan `  Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawa  ` (124 karakter)
268. Verifikasi field `City` berisi `  Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawasan Industri Selatan Pusat Kota Bandung Raya Kawa  ` (124 karakter)
269. Verifikasi pesan `Max. 120 characters` tidak tampil

### Batas 120 karakter pada Postal code (Edit)
270. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
271. Ganti isi Postal code dengan `40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119a` (120 karakter)
272. Verifikasi field `Postal code` berisi `40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119a` (120 karakter)
273. Verifikasi pesan `Max. 120 characters` tidak tampil
274. Ganti isi Postal code dengan `40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119ai` (121 karakter)
275. Verifikasi field `Postal code` ditandai tidak valid dengan pesan `Max. 120 characters`
276. Ganti isi Postal code dengan `40115  40116  40117  40118  40119  40115  40116  40117  40118  40119  40115  40116  40117  40118  40119  40115  40116  4` (120 karakter)
277. Verifikasi field `Postal code` berisi `40115  40116  40117  40118  40119  40115  40116  40117  40118  40119  40115  40116  40117  40118  40119  40115  40116  4` (120 karakter)
278. Verifikasi pesan `Max. 120 characters` tidak tampil
279. Ganti isi Postal code dengan `  40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119a  ` (124 karakter)
280. Verifikasi field `Postal code` berisi `  40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119 40115 40116 40117 40118 40119a  ` (124 karakter)
281. Verifikasi pesan `Max. 120 characters` tidak tampil

### Batas 360 karakter pada Address line (Edit)
282. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
283. Ganti isi Address line dengan `Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia` (360 karakter)
284. Verifikasi field `Address line` berisi `Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia` (360 karakter)
285. Verifikasi pesan `Max. 360 characters` tidak tampil
286. Ganti isi Address line dengan `Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asiai` (361 karakter)
287. Verifikasi field `Address line` ditandai tidak valid dengan pesan `Max. 360 characters`
288. Ganti isi Address line dengan `Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Serv` (360 karakter)
289. Verifikasi field `Address line` berisi `Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Servis  Lantai  Blok  Kawasan  Pergudangan  Jalan  Asia  Afrika  Nomor  Gedung  Serv` (360 karakter)
290. Verifikasi pesan `Max. 360 characters` tidak tampil
291. Ganti isi Address line dengan `  Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia  ` (364 karakter)
292. Verifikasi field `Address line` berisi `  Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia Afrika Nomor Gedung Servis Lantai Blok Kawasan Pergudangan Jalan Asia  ` (364 karakter)
293. Verifikasi pesan `Max. 360 characters` tidak tampil

### Batas 360 karakter pada Notes (Edit)
294. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
295. Ganti isi Notes dengan `Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekan` (360 karakter)
296. Verifikasi field `Notes` berisi `Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekan` (360 karakter)
297. Verifikasi pesan `Max. 360 characters` tidak tampil
298. Ganti isi Notes dengan `Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekani` (361 karakter)
299. Verifikasi field `Notes` ditandai tidak valid dengan pesan `Max. 360 characters`
300. Ganti isi Notes dengan `Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  r` (360 karakter)
301. Verifikasi field `Notes` berisi `Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  ruangan  dan  genset  untuk  cabang  wilayah  Rekanan  resmi  servis  pendingin  r` (360 karakter)
302. Verifikasi pesan `Max. 360 characters` tidak tampil
303. Ganti isi Notes dengan `  Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekan  ` (364 karakter)
304. Verifikasi field `Notes` berisi `  Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekanan resmi servis pendingin ruangan dan genset untuk cabang wilayah Rekan  ` (364 karakter)
305. Verifikasi pesan `Max. 360 characters` tidak tampil

### Karakter yang diizinkan dan emoji diblok pada Province / State (Edit)
306. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
307. Ganti isi Province / State dengan `Jawa Barat 西爪哇`
308. Verifikasi field `Province / State` berisi `Jawa Barat 西爪哇`
309. Verifikasi pesan `Province / State contains invalid characters` tidak tampil
310. Ganti isi Province / State dengan `D.I. Yogyakarta (DIY) / Kulon-Progo`
311. Verifikasi field `Province / State` berisi `D.I. Yogyakarta (DIY) / Kulon-Progo`
312. Verifikasi pesan `Province / State contains invalid characters` tidak tampil
313. Hapus seluruh isi field `Province / State`
314. Ketik `Banten🔥 Raya` di field `Province / State`
315. Verifikasi field `Province / State` berisi `Banten Raya`
316. Verifikasi pesan `Province / State contains invalid characters` tidak tampil
317. Hapus seluruh isi field `Province / State`
318. Tempel `Jambi📎 Utara` ke field `Province / State`
319. Verifikasi field `Province / State` berisi `Jambi Utara`
320. Verifikasi pesan `Province / State contains invalid characters` tidak tampil
321. Hapus seluruh isi field `Province / State`
322. Lepas teks `Riau🔍 Timur` ke field `Province / State` dengan drag-drop
323. Verifikasi field `Province / State` ditandai tidak valid dengan pesan `Province / State contains invalid characters`

### Karakter yang diizinkan dan emoji diblok pada City (Edit)
324. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
325. Ganti isi City dengan `Bandung 万隆`
326. Verifikasi field `City` berisi `Bandung 万隆`
327. Verifikasi pesan `City contains invalid characters` tidak tampil
328. Ganti isi City dengan `Kota Baru #2 & Sekitarnya`
329. Verifikasi field `City` berisi `Kota Baru #2 & Sekitarnya`
330. Verifikasi pesan `City contains invalid characters` tidak tampil
331. Hapus seluruh isi field `City`
332. Ketik `Bogor📍 Kota` di field `City`
333. Verifikasi field `City` berisi `Bogor Kota`
334. Verifikasi pesan `City contains invalid characters` tidak tampil
335. Hapus seluruh isi field `City`
336. Tempel `Garut📌 Kota` ke field `City`
337. Verifikasi field `City` berisi `Garut Kota`
338. Verifikasi pesan `City contains invalid characters` tidak tampil
339. Hapus seluruh isi field `City`
340. Lepas teks `Cimahi🔍 Selatan` ke field `City` dengan drag-drop
341. Verifikasi field `City` ditandai tidak valid dengan pesan `City contains invalid characters`

### Karakter yang diizinkan dan emoji diblok pada Postal code (Edit)
342. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
343. Ganti isi Postal code dengan `Ж-40115`
344. Verifikasi field `Postal code` berisi `Ж-40115`
345. Verifikasi pesan `Postal code contains invalid characters` tidak tampil
346. Ganti isi Postal code dengan `40115-A/2 (#3)`
347. Verifikasi field `Postal code` berisi `40115-A/2 (#3)`
348. Verifikasi pesan `Postal code contains invalid characters` tidak tampil
349. Hapus seluruh isi field `Postal code`
350. Ketik `40📊115` di field `Postal code`
351. Verifikasi field `Postal code` berisi `40115`
352. Verifikasi pesan `Postal code contains invalid characters` tidak tampil
353. Hapus seluruh isi field `Postal code`
354. Tempel `61📎254` ke field `Postal code`
355. Verifikasi field `Postal code` berisi `61254`
356. Verifikasi pesan `Postal code contains invalid characters` tidak tampil
357. Hapus seluruh isi field `Postal code`
358. Lepas teks `17🔍510` ke field `Postal code` dengan drag-drop
359. Verifikasi field `Postal code` ditandai tidak valid dengan pesan `Postal code contains invalid characters`

### Karakter bebas pada Address line (Edit)
360. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
361. Hapus seluruh isi field `Address line`
362. Ketik `Ruko Blok A 🏠 No. 7 & 8` di field `Address line`
363. Tekan `Enter` pada field `Address line`
364. Ketik `Lantai 2 #05 😊 (belakang)` di field `Address line`
365. Verifikasi field `Address line` berisi dua baris `Ruko Blok A 🏠 No. 7 & 8` dan `Lantai 2 #05 😊 (belakang)`
366. Verifikasi pesan `Address line contains invalid characters` tidak tampil
367. Verifikasi dialog Edit tidak menampilkan error pada field `Address line`

### Karakter bebas pada Notes (Edit)
368. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
369. Hapus seluruh isi field `Notes`
370. Ketik `Rekanan 🔥 resmi` di field `Notes`
371. Tekan `Enter` pada field `Notes`
372. Ketik `Garansi 1 tahun + servis gratis!` di field `Notes`
373. Verifikasi field `Notes` berisi dua baris `Rekanan 🔥 resmi` dan `Garansi 1 tahun + servis gratis!`
374. Verifikasi pesan `Notes contains invalid characters` tidak tampil
375. Verifikasi dialog Edit tidak menampilkan error pada field `Notes`

### Spasi tepi pada field alamat dan catatan dibuang saat Save (Edit)
376. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
377. Ganti isi Province / State dengan `  Jawa Tengah  `
378. Ganti isi City dengan `  Semarang  `
379. Ganti isi Postal code dengan `  50132  `
380. Ganti isi Address line dengan `  Jl. Pemuda No. 21  `
381. Ganti isi Notes dengan `  Rekanan resmi servis kompresor  `
382. Klik `[Save]`
383. Verifikasi Province / State pada permintaan simpan adalah `Jawa Tengah`
384. Verifikasi City pada permintaan simpan adalah `Semarang`
385. Verifikasi Postal code pada permintaan simpan adalah `50132`
386. Verifikasi Address line pada permintaan simpan adalah `Jl. Pemuda No. 21`
387. Verifikasi Notes pada permintaan simpan adalah `Rekanan resmi servis kompresor`

### Spasi tengah pada field alamat dan catatan tidak diubah saat Save (Edit)
388. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
389. Ganti isi Province / State dengan `Jawa  Timur Selatan`
390. Ganti isi City dengan `Kota  Batu Raya`
391. Ganti isi Postal code dengan `65  311 A`
392. Ganti isi Address line dengan `Jl.  Ijen No. 8  Blok C`
393. Ganti isi Notes dengan `Rekanan  resmi servis  AC`
394. Klik `[Save]`
395. Verifikasi Province / State pada permintaan simpan adalah `Jawa  Timur Selatan`
396. Verifikasi City pada permintaan simpan adalah `Kota  Batu Raya`
397. Verifikasi Postal code pada permintaan simpan adalah `65  311 A`
398. Verifikasi Address line pada permintaan simpan adalah `Jl.  Ijen No. 8  Blok C`
399. Verifikasi Notes pada permintaan simpan adalah `Rekanan  resmi servis  AC`

### City ditulis berbeda diterima apa adanya dengan saran autocomplete
400. Tampilkan Dialog Create / Edit Service Center dengan kondisi K5
401. Isi Name `Bengkel Alamat Servis {runId}`
402. Centang checkbox `Routine`
403. Isi Company email `ops@alamatservis-cirebon.co.id`
404. Ketik `Jakarta` di field `City`
405. Verifikasi saran `Jakarta Selatan` tampil pada field `City`
406. Ganti isi City dengan `Jaksel`
407. Klik `[Submit]`
408. Verifikasi City pada permintaan simpan adalah `Jaksel`
409. Verifikasi dialog Create tertutup

### Country di luar daftar ditolak server: isian terjaga (Create)
410. Tampilkan Dialog Create / Edit Service Center dengan kondisi K2
411. Isi Name `Bengkel Alamat Servis {runId}`
412. Centang checkbox `Routine`
413. Isi City `Cirebon`
414. Isi Company email `ops@alamatservis-cirebon.co.id`
415. Klik `[Submit]`
416. Verifikasi field `Country` ditandai tidak valid dengan pesan `Select a valid country`
417. Verifikasi field `Name` berisi `Bengkel Alamat Servis {runId}` dan field `City` berisi `Cirebon`
418. Verifikasi checkbox `Routine` tercentang

### Country di luar daftar ditolak server: isian terjaga (Edit)
419. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
420. Klik `[Save]`
421. Verifikasi field `Country` ditandai tidak valid dengan pesan `Select a valid country`
422. Verifikasi field `Name` berisi `PT Alamat Servis Terpadu` dan field `City` berisi `Bandung`
