---
id: TC-FA-FASVC-UI-065-pemilih-service-center-tampilan
title: "Select Service Center: Opsi, Pencarian, Pesan Kosong, dan Link Add service center"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.4#b1", "§4.2.4#b2", "§4.2.4#b3", "§4.2.4#b6", "§4.4#r10", "§4.1#r9", "EC-FASVC-26", "F-FASVC-05.k4"]
smoke: []
dependsOn: []
trace:
  "§4.2.4#b1": [5, 6, 7, 11, 13, 62]
  "§4.2.4#b2": [25, 26, 30, 31, 35, 36, 40, 41, 45, 46, 50, 52]
  "§4.2.4#b3": [6, 7, 8, 11, 12, 13, 14, 15, 18, 19, 20, 21, 25, 30, 35, 40, 45, 52, 60, 61, 62, 63, 67, 69, 74, 75, 93, 94, 96, 98, 100, 103, 104]
  "§4.2.4#b6": [56, 57, 58, 70]
  "§4.4#r10": [78, 79, 81, 82, 85, 86]
  "§4.1#r9": [2]
  "EC-FASVC-26": [85, 86, 88, 89]
  "F-FASVC-05.k4": [85, 86, 88, 89]
anchor: []
coverage:
  web: automated
---
# Select Service Center: Opsi, Pencarian, Pesan Kosong, dan Link Add service center

## Prerequisites
- Aktor: Total Control (membuka pemilih dari form Schedule Maintenance Routine di modul pemanggil) dan pengguna tanpa hak Create Service Center; tiap kondisi menyebut aktor yang dipakai.
- Layar awal: form modul pemanggil dengan komponen Select Service Center (kondisi K1, K3, K5) atau dialog `Select Service Center` untuk konteks banyak aset (K2, K4, K6).
- Komponen: Select Service Center
- Data:
  - DU-065-1: Service Center `Bengkel Maju Motor`, ID `sc-4101`, City `Bandung`, Company phone `+62 2250003333`, Specialization kosong, Brands `Daikin, LG, Panasonic`.
  - DU-065-2: Service Center `CV Genset Prima`, ID `sc-4102`, City `Surabaya`, Company phone `+62 3150002222`, Specialization `Generator`, Brands kosong, Contact person `Rina Wijaya` dengan Phone `+62 8120004444` dan Email `rina@gensetprima.co.id`.
  - DU-065-3: Service Center `PT Sejuk Abadi Teknik`, ID `sc-4103`, City `Jakarta Selatan`, Company phone `+62 2150001234`, Specialization `AC, Generator, Refrigeration`, Brands kosong.
  - DU-065-4: Service Center `Servis Pendingin Nusantara`, ID `sc-4104`, City `Semarang`, tanpa Company phone, Specialization `AC`, Brands `Panasonic`, Contact person `Dewi Anggraini` dengan Phone `+62 8130005555`.
  - DU-065-5: Service Center `Teknik Mandiri Utama`, ID `sc-4105`, City `Surabaya`, Company phone `+62 3150006666`, Specialization kosong, Brands `LG`.
  - DU-065-6: Aset pemanggil satu aset: Group `Branch Surabaya`, Category `AC`, Brand `Daikin`.
  - DU-065-8: Service Center `Bengkel Sinar Teknik`, ID `sc-4108`, City `Medan`, Company phone `+62 6150007777`, Specialization kosong, Brands kosong, tiga contact person: `Andi Pratama` Phone `+62 8140001111`, `Siti Nurhaliza` Phone `+62 8150002222`, dan `Bayu Kurniawan` Phone `+62 8160003333`.
  - DU-065-9: Kata kunci Search contact person kedua dan ketiga: nama `Siti` dan `Bayu`, telepon `8150002222` dan `8160003333`.
  - DU-065-7: Kata kunci Search di pemilih: `Genset`, `Semarang`, `Dewi`, `3150002222`, `8130005555`, dan `rina@gensetprima.co.id`.
- Kondisi:
  - K1: aktor Total Control; pemilih memuat DU-065-1 sampai DU-065-5 (hasil `FASVC-LOGIC-04` untuk aset pemanggil); pencarian mencari Name, City, nama contact person, Company phone, dan telepon contact person, dan tidak email.
  - K2: aktor Total Control; dialog banyak aset memuat DU-065-1 sampai DU-065-5; pilihan tunggal.
  - K3: aktor Total Control (berhak Create); aset pemanggil DU-065-6; pemilih tanpa hasil.
  - K4: aktor Total Control (berhak Create); dialog banyak aset tanpa Service Center yang mencakup semua aset.
  - K5: aktor tanpa hak Create Service Center; aset pemanggil DU-065-6; pemilih tanpa hasil.
  - K6: aktor tanpa hak Create Service Center; dialog banyak aset tanpa Service Center yang mencakup semua aset.
  - K7: aktor Total Control; pemilih memuat DU-065-5 dan DU-065-8; pencarian mencari nama dan telepon semua contact person.

## Test Steps

### Select Service Center berplaceholder Select service center
1. Tampilkan Select Service Center dengan kondisi K1
2. Verifikasi trigger Select Service Center berplaceholder `Select service center`

### Opsi pemilih berurutan Name A-Z dengan Name, City, dan Company phone
3. Tampilkan Select Service Center dengan kondisi K1
4. Klik Select Service Center
5. Verifikasi daftar opsi berurutan `Bengkel Maju Motor`, `CV Genset Prima`, `PT Sejuk Abadi Teknik`, `Servis Pendingin Nusantara`, dan `Teknik Mandiri Utama`
6. Verifikasi opsi `CV Genset Prima` menampilkan Name `CV Genset Prima`, City `Surabaya`, dan Company phone `+62 3150002222`
7. Verifikasi opsi `PT Sejuk Abadi Teknik` menampilkan Name `PT Sejuk Abadi Teknik`, City `Jakarta Selatan`, dan Company phone `+62 2150001234`
8. Verifikasi opsi `Servis Pendingin Nusantara` menampilkan Name `Servis Pendingin Nusantara`, City `Semarang`, dan Company phone `—`

### Opsi memuat badge Specialization dan Brands hanya bila diisi
9. Tampilkan Select Service Center dengan kondisi K1
10. Klik Select Service Center
11. Verifikasi opsi `CV Genset Prima` memuat badge `Generator`
12. Verifikasi opsi `CV Genset Prima` tidak memuat badge Brands
13. Verifikasi opsi `Servis Pendingin Nusantara` memuat badge `AC` dan `Panasonic`
14. Verifikasi opsi `Teknik Mandiri Utama` memuat badge `LG`
15. Verifikasi opsi `Teknik Mandiri Utama` tidak memuat badge Specialization

### Badge dibatasi dua lalu chip +N more
16. Tampilkan Select Service Center dengan kondisi K1
17. Klik Select Service Center
18. Verifikasi opsi `PT Sejuk Abadi Teknik` memuat badge `AC` dan `Generator` serta chip `+1 more`
19. Verifikasi badge `Refrigeration` tidak tampil di opsi `PT Sejuk Abadi Teknik`
20. Verifikasi opsi `Bengkel Maju Motor` memuat badge `Daikin` dan `LG` serta chip `+1 more`
21. Verifikasi badge `Panasonic` tidak tampil di opsi `Bengkel Maju Motor`

### Pencarian pemilih mencakup Name
22. Tampilkan Select Service Center dengan kondisi K1
23. Klik Select Service Center
24. Ketik `Genset` pada kotak cari
25. Verifikasi opsi `CV Genset Prima` tampil
26. Verifikasi opsi `Teknik Mandiri Utama` tidak tampil

### Pencarian pemilih mencakup City
27. Tampilkan Select Service Center dengan kondisi K1
28. Klik Select Service Center
29. Ketik `Semarang` pada kotak cari
30. Verifikasi opsi `Servis Pendingin Nusantara` tampil
31. Verifikasi opsi `CV Genset Prima` tidak tampil

### Pencarian pemilih mencakup nama contact person
32. Tampilkan Select Service Center dengan kondisi K1
33. Klik Select Service Center
34. Ketik `Dewi` pada kotak cari
35. Verifikasi opsi `Servis Pendingin Nusantara` tampil
36. Verifikasi opsi `CV Genset Prima` tidak tampil

### Pencarian pemilih mencakup Company phone
37. Tampilkan Select Service Center dengan kondisi K1
38. Klik Select Service Center
39. Ketik `3150002222` pada kotak cari
40. Verifikasi opsi `CV Genset Prima` tampil
41. Verifikasi opsi `Teknik Mandiri Utama` tidak tampil

### Pencarian pemilih mencakup telepon contact person
42. Tampilkan Select Service Center dengan kondisi K1
43. Klik Select Service Center
44. Ketik `8130005555` pada kotak cari
45. Verifikasi opsi `Servis Pendingin Nusantara` tampil
46. Verifikasi opsi `CV Genset Prima` tidak tampil

### Pencarian pemilih tidak mencakup email
47. Tampilkan Select Service Center dengan kondisi K1
48. Klik Select Service Center
49. Ketik `3150002222` pada kotak cari
50. Verifikasi opsi `CV Genset Prima` tampil
51. Ganti isi kotak cari dengan `rina@gensetprima.co.id`
52. Verifikasi `No results found.` tampil di panel

### Memilih opsi menampilkan nama dan meneruskan ID Service Center
53. Tampilkan Select Service Center dengan kondisi K1
54. Klik Select Service Center
55. Klik opsi `CV Genset Prima`
56. Verifikasi trigger Select Service Center menampilkan `CV Genset Prima`
57. Verifikasi panel opsi tertutup
58. Verifikasi nilai terpilih yang diteruskan ke modul pemakai adalah ID Service Center `sc-4102`

### Dialog Select Service Center untuk konteks banyak aset
59. Tampilkan Select Service Center dengan kondisi K2
60. Verifikasi dialog berjudul `Select Service Center` tampil
61. Verifikasi kotak cari berplaceholder `Search service center...` tampil
62. Verifikasi daftar memuat `Bengkel Maju Motor`, `CV Genset Prima`, `PT Sejuk Abadi Teknik`, `Servis Pendingin Nusantara`, dan `Teknik Mandiri Utama`
63. Verifikasi tombol `[Cancel]` dan `[Select]` tampil di dialog

### Dialog banyak aset: pilihan tunggal dan Select meneruskan ID
64. Tampilkan Select Service Center dengan kondisi K2
65. Klik opsi `CV Genset Prima`
66. Klik opsi `PT Sejuk Abadi Teknik`
67. Verifikasi hanya opsi `PT Sejuk Abadi Teknik` yang terpilih
68. Klik `[Select]`
69. Verifikasi dialog `Select Service Center` tertutup
70. Verifikasi nilai terpilih yang diteruskan ke modul pemakai adalah ID Service Center `sc-4103`

### Dialog banyak aset: Cancel menutup tanpa memilih
71. Tampilkan Select Service Center dengan kondisi K2
72. Klik opsi `CV Genset Prima`
73. Klik `[Cancel]`
74. Verifikasi dialog `Select Service Center` tertutup
75. Verifikasi tidak ada Service Center yang diteruskan ke modul pemakai

### Pemilih tanpa hasil untuk satu aset menampilkan pesan kosong dan link bagi yang berhak Create
76. Tampilkan Select Service Center dengan kondisi K3
77. Klik Select Service Center
78. Verifikasi pesan `No service centers match this asset (Branch Surabaya · AC · Daikin).` tampil
79. Verifikasi link `Add service center` tampil

### Pemilih tanpa hasil untuk banyak aset menampilkan pesan kosong dan link bagi yang berhak Create
80. Tampilkan Select Service Center dengan kondisi K4
81. Verifikasi pesan `No service center covers every asset here. Split the schedule or widen a service center's coverage.` tampil
82. Verifikasi link `Add service center` tampil

### Pengguna tanpa hak Create membuka pemilih satu aset kosong: hanya pesan
83. Tampilkan Select Service Center dengan kondisi K5
84. Klik Select Service Center
85. Verifikasi pesan `No service centers match this asset (Branch Surabaya · AC · Daikin).` tampil
86. Verifikasi link `Add service center` tidak tampil

### Pengguna tanpa hak Create membuka pemilih banyak aset kosong: hanya pesan
87. Tampilkan Select Service Center dengan kondisi K6
88. Verifikasi pesan `No service center covers every asset here. Split the schedule or widen a service center's coverage.` tampil
89. Verifikasi link `Add service center` tidak tampil

### Pencarian pemilih mencakup semua contact person, bukan hanya yang pertama
90. Tampilkan Select Service Center dengan kondisi K7
91. Klik Select Service Center
92. Ketik `Siti` pada kotak cari
93. Verifikasi opsi `Bengkel Sinar Teknik` tampil
94. Verifikasi opsi `Teknik Mandiri Utama` tidak tampil
95. Ganti isi kotak cari dengan `Bayu`
96. Verifikasi opsi `Bengkel Sinar Teknik` tampil
97. Ganti isi kotak cari dengan `8150002222`
98. Verifikasi opsi `Bengkel Sinar Teknik` tampil
99. Ganti isi kotak cari dengan `8160003333`
100. Verifikasi opsi `Bengkel Sinar Teknik` tampil

### Dialog banyak aset menyaring daftar saat mengetik
101. Tampilkan Select Service Center dengan kondisi K2
102. Ketik `Genset` pada kotak cari `Search service center...` di dialog
103. Verifikasi daftar dialog memuat `CV Genset Prima`
104. Verifikasi `Teknik Mandiri Utama` tidak tampil di daftar dialog
