---
id: TC-FA-FAREG-UI-018-form-panel-samping-aset
title: "Form Register Asset: panel samping aset dan Apply to all"
layer: ui-client
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FAREG-14", "FAREG-LOGIC-16a", "FAREG-LOGIC-16b", "FI-REG-08", "FI-REG-09", "FI-REG-10", "FI-REG-11", "FI-REG-12", "FI-REG-13", "FI-REG-14", "FLD-REG-07", "FLD-REG-10", "FLD-REG-11", "FLD-REG-12", "FLD-REG-13", "T-REG-12", "T-REG-13", "T-REG-16", "§4.1#b25", "§4.1#b26", "§4.1#b27", "§4.1#b29", "§9.6#r15", "§9.9#r15", "§9.9#r16", "EB-FB-1@apply-to-all"]
smoke: []
dependsOn: []
trace:
  "F-FAREG-14": 44
  "FAREG-LOGIC-16a": 44
  "FAREG-LOGIC-16b": 44
  "FI-REG-08": [4, 7, 11, 95, 112]
  "FI-REG-09": [9, 97]
  "FI-REG-10": [11, 100]
  "FI-REG-11": [36, 37]
  "FI-REG-12": 34
  "FI-REG-13": [66, 67, 68, 69, 73, 75, 76, 106, 108]
  "FI-REG-14": 70
  "FLD-REG-07": [34, 37, 38]
  "FLD-REG-10": [18, 19, 62, 56, 59]
  "FLD-REG-11": [25, 47, 51]
  "FLD-REG-12": [23, 44]
  "FLD-REG-13": [20, 21, 22, 29, 108]
  "T-REG-12": 82
  "T-REG-13": 89
  "T-REG-16": [73, 106]
  "§4.1#b25": [13, 14, 114, 115]
  "§4.1#b26": [7, 18, 20, 23, 25, 36]
  "§4.1#b27": [66, 67, 68, 69, 70]
  "§4.1#b29": 26
  "§9.6#r15": [73, 82, 83, 89, 90]
  "§9.9#r15": 24
  "§9.9#r16": [20, 22]
  "EB-FB-1@apply-to-all": [73, 82]
anchor: [3, 28, 33, 50, 61]
coverage:
  web: automated
---

# Form Register Asset: panel samping aset dan Apply to all

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-018-1: Item `Laptop Dell Latitude 5440` dengan Quantity `3`; aset `Laptop Dell Latitude 5440 - 1`, `Laptop Dell Latitude 5440 - 2`, dan `Laptop Dell Latitude 5440 - 3`, semuanya Condition `Normal` dan belum berfoto.
  - DU-018-2: Item `Kursi Kerja Ergonomis` dengan Quantity `1`; aset `Kursi Kerja Ergonomis - 1`, Condition `Normal`.
  - DU-018-3: master Custom field `Warna` (Scope General, opsional) dan `Kapasitas RAM` (Scope Specific Asset Name `Laptop Dell Latitude 5440`, wajib).
  - DU-018-4: master Asset Label `Aset IT`, `Kantor Pusat`, dan `Garansi Aktif`.
  - DU-018-8: Item `Printer Epson L3250` dengan Quantity `25`; aset `Printer Epson L3250 - 1` sampai `Printer Epson L3250 - 25`, semuanya Condition `Normal`.
  - DU-018-9: Custom field `Warna` diisi `Hitam`.
- Kondisi:
  - K1: form `Edit` draft tersimpan dengan Item DU-018-1 dan DU-018-2; master Custom field DU-018-3; master Asset Label DU-018-4.
  - K2: sama dengan K1; Apply to all gagal karena error server.
  - K3: sama dengan K1; Apply to all gagal karena gangguan jaringan.
  - K4: form `Edit` draft tersimpan dengan Item DU-018-1, DU-018-2, dan DU-018-8; master Custom field DU-018-3; master Asset Label DU-018-4; tinggi viewport pendek sehingga tabel aset dan isi panel samping aset melebihi tinggi viewport.
  - K5: sama dengan K4; form dibuka dalam mode `Detail` (read-only).

## Test Steps
### Panel samping hanya tampil sesudah pemicu, ditutup, dan dibuka kembali
1. Tampilkan Halaman `Register Asset` dengan kondisi K4
2. Klik tab `Asset`
3. Verifikasi `Laptop Dell Latitude 5440 - 1` terdaftar di tabel aset
4. Verifikasi panel samping aset tidak tampil sebelum pemicu
5. Klik row option (titik tiga) pada `Laptop Dell Latitude 5440 - 1`
6. Klik `Detail`
7. Verifikasi panel samping aset tampil dengan judul `Laptop Dell Latitude 5440 - 1`
8. Klik `Close`
9. Verifikasi panel samping aset tertutup
10. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
11. Verifikasi panel samping aset tampil kembali dengan judul `Laptop Dell Latitude 5440 - 1`
12. Gulir tabel aset ke bawah
13. Verifikasi panel samping aset tetap terlihat saat tabel digulir
14. Verifikasi isi panel samping aset dapat digulir sendiri

### Isi panel samping: Photo, Custom fields, Asset labels, dan Alias Name
15. Tampilkan Halaman `Register Asset` dengan kondisi K1
16. Klik tab `Asset`
17. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
18. Verifikasi panel memuat area `Add photo`
19. Verifikasi bagian Photo tidak menampilkan pesan error walau belum berfoto
20. Verifikasi bagian `Custom fields` memuat field `Warna` dan `Kapasitas RAM`
21. Verifikasi field `Kapasitas RAM` bertanda wajib
22. Verifikasi field `Warna` tidak bertanda wajib
23. Verifikasi bagian Asset labels menampilkan placeholder `Select asset labels`
24. Verifikasi bagian Asset labels tidak bertanda wajib
25. Verifikasi bagian Alias Name memuat input dengan placeholder `Enter alias name` dan tombol `+ Add alias name`
26. Verifikasi panel tidak memuat bagian `Attachments`
27. Klik kolom `Name` pada `Kursi Kerja Ergonomis - 1`
28. Verifikasi panel `Kursi Kerja Ergonomis - 1` memuat field `Warna`
29. Verifikasi field `Kapasitas RAM` tidak tampil pada panel `Kursi Kerja Ergonomis - 1`

### Damage note tampil dan wajib hanya bila Condition Damaged
30. Tampilkan Halaman `Register Asset` dengan kondisi K1
31. Klik tab `Asset`
32. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
33. Verifikasi bagian Asset labels tampil pada panel `Laptop Dell Latitude 5440 - 1`
34. Verifikasi `Damage note` tidak tampil saat Condition `Normal`
35. Ganti sel `Condition` pada `Laptop Dell Latitude 5440 - 1` menjadi `Damaged`
36. Verifikasi `Damage note` tampil sebagai field pertama di panel
37. Verifikasi `Damage note` bertanda wajib
38. Verifikasi `Damage note` menampilkan placeholder `Enter damage note`

### Asset labels multi-pilih dan Alias Name berulang tidak unik
39. Tampilkan Halaman `Register Asset` dengan kondisi K1
40. Klik tab `Asset`
41. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
42. Pilih Asset label `Aset IT` pada bagian Asset labels
43. Pilih Asset label `Kantor Pusat` pada bagian Asset labels
44. Verifikasi bagian Asset labels menampilkan `Aset IT` dan `Kantor Pusat` terpilih bersamaan
45. Ketik Alias Name `Notebook Direksi A` pada input `Enter alias name`
46. Klik `+ Add alias name`
47. Verifikasi panel memuat dua input Alias Name
48. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 2`
49. Ketik Alias Name `Notebook Direksi A` pada input `Enter alias name`
50. Verifikasi input Alias Name `Laptop Dell Latitude 5440 - 2` menampilkan `Notebook Direksi A`
51. Verifikasi tidak ada pesan error pada Alias Name yang sama dengan Alias Name aset lain

### Photo maksimum dua foto per aset
52. Tampilkan Halaman `Register Asset` dengan kondisi K1
53. Klik tab `Asset`
54. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
55. Pilih berkas `laptop-1.jpg` pada area `Add photo`
56. Verifikasi dialog `Adjust photo` tampil dengan tombol `Apply`
57. Klik `Apply`
58. Pilih berkas `laptop-2.jpg` pada area `Add photo`
59. Verifikasi dialog `Adjust photo` tampil dengan tombol `Apply`
60. Klik `Apply`
61. Verifikasi panel menampilkan dua foto aset `Laptop Dell Latitude 5440 - 1`
62. Verifikasi area `Add photo` untuk foto ketiga tidak tampil pada aset `Laptop Dell Latitude 5440 - 1`

### Apply to all per data, bukan sekaligus, dan tidak ada untuk Tag dan Condition
63. Tampilkan Halaman `Register Asset` dengan kondisi K1
64. Klik tab `Asset`
65. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
66. Verifikasi tautan `Apply to all` tampil pada header bagian Photo
67. Verifikasi tautan `Apply to all` tampil pada header bagian `Custom fields`
68. Verifikasi tautan `Apply to all` tampil pada header bagian Asset labels
69. Verifikasi tautan `Apply to all` tampil pada header bagian Alias Name
70. Verifikasi kolom TAG dan kolom `Condition` pada tabel tidak memiliki `Apply to all`
71. Pilih Asset label `Aset IT` pada bagian Asset labels
72. Klik `Apply to all` pada header bagian Asset labels
73. Verifikasi toast `Success, the value has been applied to all assets in the item.` tampil
74. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 2`
75. Verifikasi bagian Asset labels `Laptop Dell Latitude 5440 - 2` menampilkan `Aset IT`
76. Verifikasi bagian Photo `Laptop Dell Latitude 5440 - 2` tidak berubah dan belum berfoto

### Apply to all gagal karena error server
77. Tampilkan Halaman `Register Asset` dengan kondisi K2
78. Klik tab `Asset`
79. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
80. Pilih Asset label `Aset IT` pada bagian Asset labels
81. Klik `Apply to all` pada header bagian Asset labels
82. Verifikasi toast Error dengan awalan `Error, failed to` tampil
83. Verifikasi panel samping aset `Laptop Dell Latitude 5440 - 1` tetap terbuka

### Apply to all gagal karena gangguan jaringan
84. Tampilkan Halaman `Register Asset` dengan kondisi K3
85. Klik tab `Asset`
86. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
87. Pilih Asset label `Aset IT` pada bagian Asset labels
88. Klik `Apply to all` pada header bagian Asset labels
89. Verifikasi toast Error `Connection problem. Please try again.` tampil
90. Verifikasi panel samping aset `Laptop Dell Latitude 5440 - 1` tetap terbuka

### Panel samping aset dibuka kembali lewat row option Detail sesudah ditutup
91. Tampilkan Halaman `Register Asset` dengan kondisi K1
92. Klik tab `Asset`
93. Klik row option (titik tiga) pada `Laptop Dell Latitude 5440 - 1`
94. Klik `Detail`
95. Verifikasi panel samping aset tampil dengan judul `Laptop Dell Latitude 5440 - 1`
96. Klik `Close`
97. Verifikasi panel samping aset tertutup
98. Klik row option (titik tiga) pada `Laptop Dell Latitude 5440 - 1`
99. Klik `Detail`
100. Verifikasi panel samping aset tampil kembali dengan judul `Laptop Dell Latitude 5440 - 1`

### Apply to all pada Custom fields diterapkan ke semua aset Item
101. Tampilkan Halaman `Register Asset` dengan kondisi K1
102. Klik tab `Asset`
103. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
104. Ganti isi field `Warna` dengan `Hitam`
105. Klik `Apply to all` pada header bagian `Custom fields`
106. Verifikasi toast `Success, the value has been applied to all assets in the item.` tampil
107. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 2`
108. Verifikasi field `Warna` pada panel `Laptop Dell Latitude 5440 - 2` menampilkan `Hitam`

### Panel samping aset tetap terlihat dan punya scroll sendiri pada mode Detail read-only
109. Tampilkan Halaman `Register Asset` dengan kondisi K5
110. Klik tab `Asset`
111. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
112. Verifikasi panel samping aset tampil dengan judul `Laptop Dell Latitude 5440 - 1`
113. Gulir tabel aset ke bawah
114. Verifikasi panel samping aset tetap terlihat saat tabel digulir
115. Verifikasi isi panel samping aset dapat digulir sendiri
