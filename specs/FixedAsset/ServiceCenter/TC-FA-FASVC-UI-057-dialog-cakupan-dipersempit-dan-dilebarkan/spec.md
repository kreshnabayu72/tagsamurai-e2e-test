---
id: TC-FA-FASVC-UI-057-dialog-cakupan-dipersempit-dan-dilebarkan
title: "Dialog Narrow Coverage dan Widen Coverage: Total Hitungan, Rincian Nama per Field, dan Urutan"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["D-FASVC-03", "D-FASVC-08", "DO-FASVC-02", "DO-FASVC-03", "EC-FASVC-10a", "EC-FASVC-51", "F-FASVC-02.k6", "F-FASVC-02.k13", "FASVC-LOGIC-07e", "FASVC-LOGIC-07f", "FASVC-LOGIC-07g", "§4.2.5#p2", "§4.2.5#p5", "§4.4#r5", "§4.4#r6"]
smoke: []
dependsOn: []
trace:
  "D-FASVC-03": [6, 7, 8, 9, 10, 12, 22, 23, 24, 25, 26, 112, 113, 114, 115]
  "D-FASVC-08": [40, 41, 42, 43, 44, 45, 50, 51, 52]
  "DO-FASVC-02": [6]
  "DO-FASVC-03": [40, 50]
  "EC-FASVC-10a": [6]
  "EC-FASVC-51": [40, 50]
  "F-FASVC-02.k6": [6]
  "F-FASVC-02.k13": [40, 50]
  "FASVC-LOGIC-07e": [9, 10, 23, 24, 25, 26]
  "FASVC-LOGIC-07f": [43, 51]
  "FASVC-LOGIC-07g": [40, 50]
  "§4.2.5#p2": [9, 10, 11, 23, 24, 25, 26, 33, 99, 113, 114, 115]
  "§4.2.5#p5": [62, 63, 65, 67, 68, 69, 70, 81, 82, 83, 84, 85, 97, 98]
  "§4.4#r5": [9, 10, 23, 24, 25, 26]
  "§4.4#r6": [40, 43, 50, 51]
anchor: [32]
coverage:
  web: automated
---
# Dialog Narrow Coverage dan Widen Coverage: Total Hitungan, Rincian Nama per Field, dan Urutan

## Prerequisites
- Aktor: Total Control.
- Layar awal: Dialog Edit Service Center di Add-ons > Service Center, terbuka untuk DU-057-1.
- Komponen: Dialog konfirmasi Narrow Coverage dan Widen Coverage
- Data:
  - DU-057-1: Service Center `CV Genset Prima`, Service type `Routine`, Available to `Branch Surabaya` dan `Branch Malang`, Specialization `AC` dan `Refrigeration`, Brands `Daikin` dan `LG`.
  - DU-057-2: Hitungan dampak penyempitan: `2` Schedule aktif dan `3` Task terbuka terdampak.
  - DU-057-3: Hitungan dampak penyempitan: `4` Schedule aktif dan `5` Task terbuka terdampak.
  - DU-057-4: Hitungan dampak penyempitan: `0` Schedule aktif dan `0` Task terbuka terdampak.
  - DU-057-5: Service Center `PT Servis Terpadu Nusantara`, Service type `Routine`, Available to `Branch Surabaya, Branch Malang, Branch Bandung`, Specialization `AC, Generator, Refrigeration`, Brands `Daikin, LG, Panasonic`.
- Kondisi:
  - K1: Edit DU-057-1 terbuka dan respons hitungan dampak memakai DU-057-2.
  - K2: Edit DU-057-1 terbuka dan respons hitungan dampak memakai DU-057-3.
  - K3: Edit DU-057-1 terbuka dan respons hitungan dampak memakai DU-057-4; simpan berhasil.
  - K4: Edit DU-057-1 terbuka dan respons hitungan dampak memakai DU-057-4.
  - K5: Edit DU-057-1 terbuka dan respons hitungan dampak memakai DU-057-4.
  - K6: Edit DU-057-1 terbuka, respons hitungan dampak memakai DU-057-2, dan simpan berhasil.
  - K7: Edit DU-057-5 terbuka dan respons hitungan dampak memakai DU-057-3.

## Test Steps

### Narrow Coverage menyebut hitungan dan rincian Groups saja
1. Tampilkan Dialog konfirmasi Narrow Coverage dan Widen Coverage dengan kondisi K1
2. Klik trigger field `Available to`
3. Klik checkbox `Branch Malang` untuk melepas pilihannya
4. Klik `[Select]` pada dialog pilihan Available to
5. Klik `[Save]`
6. Verifikasi dialog `Narrow Coverage` tampil
7. Verifikasi tombol `[Cancel]` dan `[Save]` tampil di dialog
8. Verifikasi isi dialog memuat `• CV Genset Prima`
9. Verifikasi isi dialog memuat `It will no longer appear for assets outside its new coverage. 2 active schedules and 3 open tasks keep using it; their next tasks for those assets will wait for assignment.`
10. Verifikasi rincian `Groups removed: Branch Malang` tampil
11. Verifikasi rincian `Categories removed` dan `Brands removed` tidak tampil
12. Verifikasi pertanyaan `Are you sure you want to save the changes?` tampil

### Narrow Coverage merinci setiap field yang dipersempit
13. Tampilkan Dialog konfirmasi Narrow Coverage dan Widen Coverage dengan kondisi K2
14. Klik trigger field `Available to`
15. Klik checkbox `Branch Malang` untuk melepas pilihannya
16. Klik `[Select]` pada dialog pilihan Available to
17. Klik trigger field `Specialization`
18. Klik checkbox `Refrigeration` untuk melepas pilihannya
19. Klik `[Select]` pada dialog pilihan Specialization
20. Hapus pilihan `LG` pada Brands
21. Klik `[Save]`
22. Verifikasi dialog `Narrow Coverage` tampil
23. Verifikasi isi dialog memuat `It will no longer appear for assets outside its new coverage. 4 active schedules and 5 open tasks keep using it; their next tasks for those assets will wait for assignment.`
24. Verifikasi rincian `Groups removed: Branch Malang` tampil
25. Verifikasi rincian `Categories removed: Refrigeration` tampil
26. Verifikasi rincian `Brands removed: LG` tampil

### Dialog Narrow Coverage tidak tampil bila hitungan terdampak 0
27. Tampilkan Dialog konfirmasi Narrow Coverage dan Widen Coverage dengan kondisi K3
28. Klik trigger field `Specialization`
29. Klik checkbox `Refrigeration` untuk melepas pilihannya
30. Klik `[Select]` pada dialog pilihan Specialization
31. Klik `[Save]`
32. Verifikasi toast `Success, CV Genset Prima has been updated.` tampil
33. Verifikasi dialog `Narrow Coverage` tidak tampil

### Widen Coverage saat Specialization dikosongkan
34. Tampilkan Dialog konfirmasi Narrow Coverage dan Widen Coverage dengan kondisi K4
35. Klik trigger field `Specialization`
36. Klik checkbox `AC` untuk melepas pilihannya
37. Klik checkbox `Refrigeration` untuk melepas pilihannya
38. Klik `[Select]` pada dialog pilihan Specialization
39. Klik `[Save]`
40. Verifikasi dialog `Widen Coverage` tampil
41. Verifikasi tombol `[Cancel]` dan `[Save]` tampil di dialog
42. Verifikasi isi dialog memuat `• CV Genset Prima`
43. Verifikasi isi dialog memuat `Leaving Specialization empty means it works on all categories.`
44. Verifikasi isi dialog tidak memuat `Leaving Brands empty means it works on all brands.`
45. Verifikasi pertanyaan `Are you sure you want to save the changes?` tampil

### Widen Coverage saat Brands dikosongkan
46. Tampilkan Dialog konfirmasi Narrow Coverage dan Widen Coverage dengan kondisi K5
47. Hapus pilihan `Daikin` pada Brands
48. Hapus pilihan `LG` pada Brands
49. Klik `[Save]`
50. Verifikasi dialog `Widen Coverage` tampil
51. Verifikasi isi dialog memuat `Leaving Brands empty means it works on all brands.`
52. Verifikasi isi dialog tidak memuat `Leaving Specialization empty means it works on all categories.`

### Cancel pada Widen Coverage membatalkan seluruh Save
53. Tampilkan Dialog konfirmasi Narrow Coverage dan Widen Coverage dengan kondisi K6
54. Klik trigger field `Available to`
55. Klik checkbox `Branch Malang` untuk melepas pilihannya
56. Klik `[Select]` pada dialog pilihan Available to
57. Klik trigger field `Specialization`
58. Klik checkbox `AC` untuk melepas pilihannya
59. Klik checkbox `Refrigeration` untuk melepas pilihannya
60. Klik `[Select]` pada dialog pilihan Specialization
61. Klik `[Save]`
62. Verifikasi dialog `Narrow Coverage` tampil
63. Verifikasi dialog `Widen Coverage` belum tampil
64. Klik `[Save]` pada dialog `Narrow Coverage`
65. Verifikasi dialog `Widen Coverage` tampil
66. Klik `[Cancel]` pada dialog `Widen Coverage`
67. Verifikasi dialog `Edit Service Center` tetap terbuka
68. Verifikasi Available to menampilkan `1 group selected`
69. Verifikasi Specialization menampilkan `Select categories`
70. Verifikasi permintaan simpan belum terkirim

### Cancel pada Narrow Coverage membatalkan seluruh Save
71. Tampilkan Dialog konfirmasi Narrow Coverage dan Widen Coverage dengan kondisi K6
72. Klik trigger field `Available to`
73. Klik checkbox `Branch Malang` untuk melepas pilihannya
74. Klik `[Select]` pada dialog pilihan Available to
75. Klik trigger field `Specialization`
76. Klik checkbox `AC` untuk melepas pilihannya
77. Klik checkbox `Refrigeration` untuk melepas pilihannya
78. Klik `[Select]` pada dialog pilihan Specialization
79. Klik `[Save]`
80. Klik `[Cancel]` pada dialog `Narrow Coverage`
81. Verifikasi dialog `Edit Service Center` tetap terbuka
82. Verifikasi Available to menampilkan `1 group selected`
83. Verifikasi Specialization menampilkan `Select categories`
84. Verifikasi dialog `Widen Coverage` tidak tampil
85. Verifikasi permintaan simpan belum terkirim

### Perubahan tersimpan setelah kedua dialog dikonfirmasi
86. Tampilkan Dialog konfirmasi Narrow Coverage dan Widen Coverage dengan kondisi K6
87. Klik trigger field `Available to`
88. Klik checkbox `Branch Malang` untuk melepas pilihannya
89. Klik `[Select]` pada dialog pilihan Available to
90. Klik trigger field `Specialization`
91. Klik checkbox `AC` untuk melepas pilihannya
92. Klik checkbox `Refrigeration` untuk melepas pilihannya
93. Klik `[Select]` pada dialog pilihan Specialization
94. Klik `[Save]`
95. Klik `[Save]` pada dialog `Narrow Coverage`
96. Klik `[Save]` pada dialog `Widen Coverage`
97. Verifikasi permintaan simpan terkirim satu kali
98. Verifikasi toast `Success, CV Genset Prima has been updated.` tampil
99. Verifikasi dialog `Narrow Coverage` tidak tampil lagi sesudah penyimpanan berhasil

### Rincian beberapa nilai dipisah koma dan spasi
100. Tampilkan Dialog konfirmasi Narrow Coverage dan Widen Coverage dengan kondisi K7
101. Klik trigger field `Available to`
102. Klik checkbox `Branch Malang` untuk melepas pilihannya
103. Klik checkbox `Branch Bandung` untuk melepas pilihannya
104. Klik `[Select]` pada dialog pilihan Available to
105. Klik trigger field `Specialization`
106. Klik checkbox `Generator` untuk melepas pilihannya
107. Klik checkbox `Refrigeration` untuk melepas pilihannya
108. Klik `[Select]` pada dialog pilihan Specialization
109. Hapus pilihan `LG` pada Brands
110. Hapus pilihan `Panasonic` pada Brands
111. Klik `[Save]`
112. Verifikasi dialog `Narrow Coverage` tampil
113. Verifikasi rincian `Groups removed` memuat `Branch Malang` dan `Branch Bandung` dipisahkan koma dan spasi
114. Verifikasi rincian `Categories removed` memuat `Generator` dan `Refrigeration` dipisahkan koma dan spasi
115. Verifikasi rincian `Brands removed` memuat `LG` dan `Panasonic` dipisahkan koma dan spasi
