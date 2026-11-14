---
id: TC-FA-DAMAGED-UI-107-tab-damaged-sub-tab-breadcrumb-guided-tooltip
title: "Tab Damaged: breadcrumb, pergantian sub-tab dengan state masing-masing, konfigurasi kolom per tabel tidak saling mengubah, dan Guided Tooltip tiga langkah"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.1#p1", "§4.2.1#b4", "§4.4#r1", "§9.5#r1", "§4.7#r1", "§4.7#r2", "§4.7#r3", EB-TBL-10, EB-TBL-11, EB-KOL-3]
smoke: []
dependsOn: []
trace:
  "§4.2.1#p1": [2, 6, 7, 17, 20]
  "§4.2.1#b4": [8, 10]
  "§4.4#r1": [16, 18, 21, 24, 25, 27, 29, 30, 32, 33, 35, 36, 37, 90, 91, 93, 95, 96, 99, 101, 103]
  "§9.5#r1": [12, 13]
  "§4.7#r1": [51, 52, 105]
  "§4.7#r2": [57, 58, 107]
  "§4.7#r3": [61, 62, 109]
  EB-TBL-10: [50, 53, 54, 56, 60, 63, 65, 68, 69, 71, 73, 75, 77, 78, 80, 82, 84, 85]
  EB-TBL-11: [3, 4, 5]
  EB-KOL-3: [41, 43, 46, 48]
anchor: []
coverage:
  web: automated
---

# Tab Damaged: breadcrumb, pergantian sub-tab dengan state masing-masing, konfigurasi kolom per tabel tidak saling mengubah, dan Guided Tooltip tiga langkah

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Assets, tab `Damaged`, sub-tab `Active`.
- Komponen: Tab Damaged (sub-tab Active dan History)
- Data:
  - DU-107-1: Record sub-tab Active `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Group `Head Office`, Status `Damaged`, Source `Borrow return`, Reported By `Rina Wijaya`.
  - DU-107-2: Record sub-tab Active `Camera Canon EOS - 3`, Asset ID `CAM-2026-0003`, Group `Head Office`, Status `Damaged`, Source `Manual`, Reported By `Agus Prasetyo`.
  - DU-107-3: Record sub-tab History `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Group `Head Office`, Status `Repaired`, Source `Borrow return`, Reported By `Rina Wijaya`, Resolved By `Rina Wijaya`.
  - DU-107-4: Record sub-tab History `Toyota Avanza - 1`, Asset ID `VEH-2026-0001`, Group `Branch Surabaya`, Status `Repaired`, Source `Manual`, Reported By `Agus Prasetyo`, Resolved By `Agus Prasetyo`.
  - DU-107-6: 12 record sub-tab Active `Pallet Jack Manual - {n}` (n = 1 sampai 12), Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-107-7: 12 record sub-tab History `Hand Truck Steel - {n}` (n = 1 sampai 12), Group `Head Office`, Status `Repaired`, Source `Manual`.
- Kondisi:
  - K1: sub-tab Active memuat DU-107-1 dan DU-107-2, sub-tab History memuat DU-107-3 dan DU-107-4; flag `guided_tooltip_seen_fa-damaged` untuk aktor belum tersimpan.
  - K2: seperti K1; flag `guided_tooltip_seen_fa-damaged` untuk aktor sudah tersimpan.
  - K3: sub-tab Active memuat 12 record pada DU-107-6, sub-tab History memuat 12 record pada DU-107-7, dengan ukuran halaman bawaan; flag `guided_tooltip_seen_fa-damaged` untuk aktor sudah tersimpan.

## Test Steps

### Breadcrumb dan struktur halaman tab Damaged
1. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K2
2. Verifikasi breadcrumb memuat segmen `Assets`, `Damaged`, dan `Active` berurutan
3. Verifikasi segmen pertama `Assets` tampil sebagai teks statis, bukan tautan
4. Verifikasi segmen terakhir `Active` tampil sebagai teks statis, bukan tautan
5. Verifikasi segmen tengah `Damaged` tampil sebagai tautan
6. Verifikasi tab halaman `Assets`, `Registration`, `Damaged`, dan `Missing` tampil berurutan
7. Verifikasi sub-tab `Active` dan `History` tampil
8. Verifikasi sidebar Group tidak dirender
9. Klik ikon Filter
10. Verifikasi field `Group` tampil pada Filter Panel dengan placeholder `All groups`

### Sub-tab awal adalah Active
11. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K2
12. Verifikasi sub-tab `Active` terpilih
13. Verifikasi baris `Projector Epson EB-X06 - 2` tampil

### Pergantian sub-tab memperbarui breadcrumb dan isi tabel
14. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K2
15. Klik sub-tab `History`
16. Verifikasi sub-tab `History` terpilih
17. Verifikasi segmen terakhir breadcrumb `History` tampil
18. Verifikasi baris `Laptop Dell Latitude 5420 - 9` tampil
19. Klik sub-tab `Active`
20. Verifikasi segmen terakhir breadcrumb `Active` tampil
21. Verifikasi baris `Projector Epson EB-X06 - 2` tampil

### State Search dan sort tiap sub-tab dipulihkan
22. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K2
23. Ketik Search `Camera`, tekan Enter
24. Verifikasi baris `Camera Canon EOS - 3` tampil
25. Verifikasi baris `Projector Epson EB-X06 - 2` tidak tampil
26. Klik header kolom `Name`
27. Verifikasi indikator `↑` aktif pada header kolom `Name`
28. Klik sub-tab `History`
29. Verifikasi baris `Laptop Dell Latitude 5420 - 9` dan `Toyota Avanza - 1` tampil tanpa dipengaruhi Search sub-tab Active
30. Verifikasi indikator sort pada header kolom `Name` tidak aktif
31. Ketik Search `Laptop`, tekan Enter
32. Verifikasi baris `Laptop Dell Latitude 5420 - 9` tampil
33. Verifikasi baris `Toyota Avanza - 1` tidak tampil
34. Klik sub-tab `Active`
35. Verifikasi baris `Camera Canon EOS - 3` tampil
36. Verifikasi baris `Projector Epson EB-X06 - 2` tidak tampil sesuai Search `Camera` yang dipulihkan
37. Verifikasi indikator `↑` aktif pada header kolom `Name`

### Konfigurasi kolom satu tabel tidak mengubah tabel lain
38. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K2
39. Klik header kolom Actions (`⋯`)
40. Hapus centang `Source` pada daftar kolom
41. Verifikasi header kolom `Source` tidak dirender pada sub-tab Active
42. Klik sub-tab `History`
43. Verifikasi header kolom `Source` tampil pada sub-tab History
44. Klik header kolom Actions (`⋯`)
45. Hapus centang `Reported By` pada daftar kolom
46. Verifikasi header kolom `Reported By` tidak dirender pada sub-tab History
47. Klik sub-tab `Active`
48. Verifikasi header kolom `Reported By` tampil pada sub-tab Active

### Guided Tooltip terbuka otomatis dan menjalani tiga langkah
49. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K1
50. Verifikasi Guided Tooltip terbuka otomatis dengan progres `Step 1 of 3`
51. Verifikasi judul `Focus on what needs action` tampil
52. Verifikasi deskripsi `Narrow down the list to the records that need your attention.` tampil
53. Verifikasi tombol `Skip` dan `Next` tampil
54. Verifikasi tombol `Back` tidak tampil pada langkah pertama
55. Klik `Next`
56. Verifikasi progres `Step 2 of 3` tampil
57. Verifikasi judul `Track damaged assets` tampil
58. Verifikasi deskripsi `Every asset stays here until its report is resolved.` tampil
59. Klik `Next`
60. Verifikasi progres `Step 3 of 3` tampil
61. Verifikasi judul `Review closed records` tampil
62. Verifikasi deskripsi `Closed records stay here for reference.` tampil
63. Verifikasi tombol `Done` tampil menggantikan `Next`
64. Klik `Back`
65. Verifikasi progres `Step 2 of 3` tampil
66. Klik `Next`
67. Klik `Done`
68. Verifikasi Guided Tooltip tertutup
69. Verifikasi sub-tab `Active` tetap terpilih sesudah tur selesai

### Skip menutup Guided Tooltip
70. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K1
71. Verifikasi Guided Tooltip terbuka otomatis dengan progres `Step 1 of 3`
72. Klik `Skip`
73. Verifikasi Guided Tooltip tertutup

### Guided Tooltip tidak terbuka lagi dan diputar ulang lewat tombol bantuan
74. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K2
75. Verifikasi Guided Tooltip tidak terbuka otomatis
76. Klik `[?]` di sebelah kanan breadcrumb
77. Verifikasi Guided Tooltip terbuka dengan progres `Step 1 of 3`
78. Verifikasi flag `guided_tooltip_seen_fa-damaged` untuk aktor tetap tersimpan
79. Klik `Skip`
80. Verifikasi Guided Tooltip tertutup

### Keluar tanpa selesai tidak menyetel flag
81. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K1
82. Verifikasi Guided Tooltip terbuka otomatis dengan progres `Step 1 of 3`
83. Ubah ukuran jendela
84. Verifikasi Guided Tooltip tertutup
85. Verifikasi flag `guided_tooltip_seen_fa-damaged` untuk aktor belum tersimpan

### Filter tiap sub-tab dipulihkan
86. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K2
87. Klik ikon Filter
88. Pilih opsi `Manual` pada field `Source`
89. Klik `[Apply]`
90. Verifikasi baris `Camera Canon EOS - 3` tampil
91. Verifikasi baris `Projector Epson EB-X06 - 2` tidak tampil
92. Klik sub-tab `History`
93. Verifikasi baris `Laptop Dell Latitude 5420 - 9` dan `Toyota Avanza - 1` tampil tanpa dipengaruhi Filter sub-tab Active
94. Klik sub-tab `Active`
95. Verifikasi baris `Camera Canon EOS - 3` tampil
96. Verifikasi baris `Projector Epson EB-X06 - 2` tidak tampil sesuai Filter `Source` yang dipulihkan

### Halaman paginasi tiap sub-tab dipulihkan
97. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K3
98. Klik tombol halaman `2`
99. Verifikasi laporan `Showing 11 to 12 of 12` tampil
100. Klik sub-tab `History`
101. Verifikasi laporan `Showing 1 to 10 of 12` tampil
102. Klik sub-tab `Active`
103. Verifikasi laporan `Showing 11 to 12 of 12` tampil

### Guided Tooltip menyorot elemen target tiap langkah
104. Tampilkan Tab Damaged (sub-tab Active dan History) dengan kondisi K1
105. Verifikasi Guided Tooltip pada langkah pertama menyorot `Ikon Filter di toolbar`
106. Klik `Next`
107. Verifikasi Guided Tooltip pada langkah kedua menyorot `Sub-tab Active`
108. Klik `Next`
109. Verifikasi Guided Tooltip pada langkah ketiga menyorot `Sub-tab History`
