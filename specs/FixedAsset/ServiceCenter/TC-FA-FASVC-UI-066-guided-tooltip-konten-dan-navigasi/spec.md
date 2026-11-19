---
id: TC-FA-FASVC-UI-066-guided-tooltip-konten-dan-navigasi
title: "Guided Tooltip: Tiga Step, Navigasi, Replay, dan Step Dilewati"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.7#r1", "§4.7#r2", "§4.7#r3", "§4.7#p1", "EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "§4.7#r1": [3, 4, 5, 6]
  "§4.7#r2": [11, 12, 13, 14]
  "§4.7#r3": [19, 20, 21, 22]
  "§4.7#p1": [81, 82, 83, 85, 86, 87, 89, 90, 92, 93, 94, 96, 98, 99, 100, 101, 103, 104, 105, 106, 108, 109, 110, 112, 113, 114, 116, 117, 118]
  "EB-TBL-10": [2, 3, 7, 8, 11, 15, 19, 23, 24, 29, 30, 32, 33, 38, 39, 42, 43, 46, 47, 50, 51, 54, 56, 59, 60, 62, 63, 66, 67, 68, 72, 73, 79]
anchor: []
coverage:
  web: automated
---
# Guided Tooltip: Tiga Step, Navigasi, Replay, dan Step Dilewati

## Prerequisites
- Aktor: Total Control, Read Only (tanpa hak Create), dan Monitoring & Report (tanpa hak Create); tiap kondisi menyebut aktor yang dipakai.
- Layar awal: Add-ons > Service Center, halaman daftar Service Center.
- Komponen: Guided Tooltip fams-service-center-list
- Data:
  - DU-066-1: Service Center `CV Genset Prima`, Service Type `Routine`, Specialization `Generator`, Available To `Branch Surabaya`, City `Surabaya`, Brands `All brands`, Usage `24`, Status `Active`, Modified By `Rina W`.
  - DU-066-2: Flag `guided_tooltip_seen_fams-service-center-list` milik aktor: belum disetel (kunjungan pertama).
  - DU-066-3: Flag `guided_tooltip_seen_fams-service-center-list` milik aktor: sudah disetel `true`.
  - DU-066-4: Lebar jendela browser setelah diubah: `800` px.
- Kondisi:
  - K1: aktor Total Control; daftar memuat DU-066-1; flag memakai DU-066-2; penyetelan flag berhasil.
  - K2: aktor Total Control; daftar memuat DU-066-1; flag memakai DU-066-3.
  - K3: aktor Read Only; daftar memuat DU-066-1; flag memakai DU-066-2.
  - K4: aktor Total Control; daftar memuat DU-066-1; flag memakai DU-066-2; konfigurasi kolom tersimpan milik aktor menyembunyikan kolom `Available To`.
  - K5: aktor Total Control; daftar memuat DU-066-1; flag memakai DU-066-2; konfigurasi kolom tersimpan milik aktor menyembunyikan kolom `Usage`.
  - K6: aktor Total Control; daftar memuat DU-066-1; flag memakai DU-066-2; konfigurasi kolom tersimpan milik aktor menyembunyikan kolom `Available To` dan `Usage`.
  - K7: aktor Read Only; daftar memuat DU-066-1; flag memakai DU-066-2; konfigurasi kolom tersimpan milik aktor menyembunyikan kolom `Available To`.
  - K8: aktor Monitoring & Report; daftar memuat DU-066-1; flag memakai DU-066-2.

## Test Steps

### Kunjungan pertama membuka Guided Tooltip otomatis di Step 1 dengan konten tombol tambah
1. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K1
2. Verifikasi Guided Tooltip tampil otomatis
3. Verifikasi `Step 1 of 3` tampil
4. Verifikasi judul `Add your vendors` tampil
5. Verifikasi deskripsi `Save the vendors and technicians who maintain or repair your assets.` tampil
6. Verifikasi tombol `+ Service Center` ditandai sebagai elemen yang disorot
7. Verifikasi tombol `[Skip]` dan `[Next]` tampil di Guided Tooltip
8. Verifikasi tombol `[Back]` tidak tampil di Step 1

### Next ke Step 2 dengan konten kolom Available To
9. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K1
10. Klik `[Next]`
11. Verifikasi `Step 2 of 3` tampil
12. Verifikasi judul `Choose where they work` tampil
13. Verifikasi deskripsi `A service center only appears when assigning work in the groups it is available to.` tampil
14. Verifikasi kolom `Available To` ditandai sebagai elemen yang disorot
15. Verifikasi tombol `[Back]`, `[Skip]`, dan `[Next]` tampil di Guided Tooltip

### Next ke Step 3 dengan konten kolom Usage dan tombol Done
16. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K1
17. Klik `[Next]`
18. Klik `[Next]`
19. Verifikasi `Step 3 of 3` tampil
20. Verifikasi judul `See where it's used` tampil
21. Verifikasi deskripsi `Open the Usage tab to see schedules, tasks, and repairs that refer to it.` tampil
22. Verifikasi kolom `Usage` ditandai sebagai elemen yang disorot
23. Verifikasi tombol `[Done]` tampil menggantikan `[Next]`
24. Verifikasi tombol `[Next]` tidak tampil di Step 3

### Back kembali ke step sebelumnya
25. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K1
26. Klik `[Next]`
27. Klik `[Next]`
28. Klik `[Back]`
29. Verifikasi `Step 2 of 3` tampil
30. Verifikasi judul `Choose where they work` tampil
31. Klik `[Back]`
32. Verifikasi `Step 1 of 3` tampil
33. Verifikasi judul `Add your vendors` tampil

### Done pada Step 3 menutup Guided Tooltip dan menyetel flag
34. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K1
35. Klik `[Next]`
36. Klik `[Next]`
37. Klik `[Done]`
38. Verifikasi Guided Tooltip tertutup
39. Verifikasi permintaan menyetel flag `guided_tooltip_seen_fams-service-center-list` terkirim satu kali

### Skip menutup Guided Tooltip dan menyetel flag
40. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K1
41. Klik `[Skip]`
42. Verifikasi Guided Tooltip tertutup
43. Verifikasi permintaan menyetel flag `guided_tooltip_seen_fams-service-center-list` terkirim satu kali

### Klik overlay setara Skip
44. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K1
45. Klik overlay gelap di luar Guided Tooltip
46. Verifikasi Guided Tooltip tertutup
47. Verifikasi permintaan menyetel flag `guided_tooltip_seen_fams-service-center-list` terkirim satu kali

### Keyboard: Esc setara Skip
48. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K1
49. Tekan Esc
50. Verifikasi Guided Tooltip tertutup
51. Verifikasi permintaan menyetel flag `guided_tooltip_seen_fams-service-center-list` terkirim satu kali

### Keyboard: panah kanan Next dan panah kiri Back
52. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K1
53. Tekan panah kanan
54. Verifikasi `Step 2 of 3` tampil
55. Tekan panah kiri
56. Verifikasi `Step 1 of 3` tampil

### Ubah ukuran jendela menutup tanpa menyetel flag
57. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K1
58. Ubah lebar jendela browser menjadi `800` px
59. Verifikasi Guided Tooltip tertutup
60. Verifikasi permintaan menyetel flag belum terkirim

### Kunjungan berikutnya tidak membuka Guided Tooltip otomatis
61. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K2
62. Verifikasi tabel Service Center tampil
63. Verifikasi Guided Tooltip tidak tampil

### Tombol tanya memutar ulang dari Step 1 tanpa mereset flag
64. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K2
65. Klik tombol bantuan `?` (icon question-mark)
66. Verifikasi Guided Tooltip tampil
67. Verifikasi `Step 1 of 3` tampil
68. Verifikasi judul `Add your vendors` tampil
69. Klik `[Next]`
70. Klik `[Next]`
71. Klik `[Done]`
72. Verifikasi Guided Tooltip tertutup
73. Verifikasi permintaan mereset flag tidak terkirim

### Tombol tanya memutar ulang dari Step 1 setelah keluar di step tengah
74. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K2
75. Klik tombol bantuan `?` (icon question-mark)
76. Klik `[Next]`
77. Klik `[Skip]`
78. Klik tombol bantuan `?` (icon question-mark)
79. Verifikasi `Step 1 of 3` tampil

### Role tanpa hak Create melewati Step 1 dan penomoran menyesuaikan
80. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K3
81. Verifikasi `Step 1 of 2` tampil
82. Verifikasi judul `Choose where they work` tampil
83. Verifikasi judul `Add your vendors` tidak tampil
84. Klik `[Next]`
85. Verifikasi `Step 2 of 2` tampil
86. Verifikasi judul `See where it's used` tampil
87. Verifikasi tombol `[Done]` tampil menggantikan `[Next]`

### Kolom Available To disembunyikan melewati Step 2
88. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K4
89. Verifikasi `Step 1 of 2` tampil
90. Verifikasi judul `Add your vendors` tampil
91. Klik `[Next]`
92. Verifikasi `Step 2 of 2` tampil
93. Verifikasi judul `See where it's used` tampil
94. Verifikasi judul `Choose where they work` tidak tampil

### Kolom Usage disembunyikan melewati Step 3
95. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K5
96. Verifikasi `Step 1 of 2` tampil
97. Klik `[Next]`
98. Verifikasi `Step 2 of 2` tampil
99. Verifikasi judul `Choose where they work` tampil
100. Verifikasi tombol `[Done]` tampil menggantikan `[Next]`
101. Verifikasi judul `See where it's used` tidak tampil

### Kolom Available To dan Usage disembunyikan menyisakan satu step
102. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K6
103. Verifikasi `Step 1 of 1` tampil
104. Verifikasi judul `Add your vendors` tampil
105. Verifikasi tombol `[Done]` tampil
106. Verifikasi tombol `[Back]` tidak tampil

### Role tanpa hak Create dan kolom Available To disembunyikan menyisakan step Usage
107. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K7
108. Verifikasi `Step 1 of 1` tampil
109. Verifikasi judul `See where it's used` tampil
110. Verifikasi tombol `[Done]` tampil

### Monitoring & Report tanpa hak Create melewati Step 1 dan penomoran menyesuaikan
111. Tampilkan Guided Tooltip fams-service-center-list dengan kondisi K8
112. Verifikasi `Step 1 of 2` tampil
113. Verifikasi judul `Choose where they work` tampil
114. Verifikasi judul `Add your vendors` tidak tampil
115. Klik `[Next]`
116. Verifikasi `Step 2 of 2` tampil
117. Verifikasi judul `See where it's used` tampil
118. Verifikasi tombol `[Done]` tampil menggantikan `[Next]`
