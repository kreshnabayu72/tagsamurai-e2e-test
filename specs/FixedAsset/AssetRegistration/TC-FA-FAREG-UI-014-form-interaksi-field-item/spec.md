---
id: TC-FA-FAREG-UI-014-form-interaksi-field-item
title: "Form Register Asset: interaksi Category, Asset Name, Brand, Model, dan TAG Type"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FAREG-LOGIC-01k", "FAREG-LOGIC-01l", "FAREG-LOGIC-01m", "FAREG-LOGIC-01p", "FAREG-LOGIC-04a", "FI-REG-01", "FI-REG-02", "FI-REG-03", "FI-REG-04", "FI-REG-05", "FI-REG-06", "FLD-REG-02", "FLD-REG-03", "FLD-REG-04", "S-REG-09", "S-REG-10", "§4.1#b16", "§4.1#b17", "§4.1#b18", "§4.1#p45", "§9.9#r1", "EB-TBL-5@form-register-asset"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-01k": [12, 17]
  "FAREG-LOGIC-01l": [33, 34, 37, 38]
  "FAREG-LOGIC-01m": [10, 14]
  "FAREG-LOGIC-01p": [75, 77, 78, 82, 85, 87]
  "FAREG-LOGIC-04a": [31, 39, 62]
  "FI-REG-01": [47, 48, 56]
  "FI-REG-02": [68, 69, 70, 71]
  "FI-REG-03": 61
  "FI-REG-04": [37, 38]
  "FI-REG-05": 33
  "FI-REG-06": [6, 31, 39]
  "FLD-REG-02": [41, 59, 97, 98]
  "FLD-REG-03": [2, 12, 102, 103]
  "FLD-REG-04": [4, 16, 17, 18, 108, 109]
  "S-REG-09": 3
  "S-REG-10": 5
  "§4.1#b16": [31, 39]
  "§4.1#b17": [25, 26]
  "§4.1#b18": 41
  "§4.1#p45": [45, 52]
  "§9.9#r1": [52, 54, 56, 91, 94]
  "EB-TBL-5@form-register-asset": [3, 5]
anchor: [90, 93]
coverage:
  web: automated
---

# Form Register Asset: interaksi Category, Asset Name, Brand, Model, dan TAG Type

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-014-1: Asset Name `Laptop Dell Latitude 5440`, Category `Elektronik > Komputer > Laptop`, TAG Type `RFID`, Brand `Dell` dengan Model `Latitude 5440` dan `Inspiron 15 3530`, Brand `Lenovo` dengan Model `ThinkPad T14`.
  - DU-014-2: Asset Name `Kursi Kerja Ergonomis`, Category `Furnitur > Kursi`, TAG Type `QR`, Brand `Ergotec`, Model `ErgoMesh 200`.
  - DU-014-3: Asset Name `Printer Epson L3250`, Category `Elektronik > Periferal > Printer`, TAG Type `RFID` dan `NFC`, Brand `Epson`, Model `L3250`.
  - DU-014-4: Asset Name `Rak Besi Gudang`, Category `Furnitur > Rak`, TAG Type `QR`, tanpa Brand terkait, dengan Custom field Per asset `Serial Number`.
- Kondisi:
  - K1: form `Register Asset` baru tanpa draft tersimpan; tabel Item berisi satu Item kosong; master Asset Name, Brand, Model, dan Category berisi DU-014-1 sampai DU-014-4.

## Test Steps
### Brand dan Model Disabled sampai induk dipilih
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Verifikasi `Brand` berstatus Disabled selama Asset Name belum dipilih
3. Verifikasi tooltip `Select asset name first.` tampil saat pointer berada di `Brand`
4. Verifikasi `Model` berstatus Disabled selama Brand belum dipilih
5. Verifikasi tooltip `Select brand first.` tampil saat pointer berada di `Model`
6. Verifikasi TAG Type bernilai `—` sebelum Asset Name dipilih

### Opsi bertingkat Asset Name, Brand, dan Model tanpa auto-pilih
7. Tampilkan Halaman `Register Asset` dengan kondisi K1
8. Buka dropdown `Asset Name`
9. Pilih `Laptop Dell Latitude 5440`
10. Verifikasi `Brand` tidak Disabled dan masih menampilkan placeholder `Select brand`
11. Buka dropdown `Brand`
12. Verifikasi opsi `Dell` dan `Lenovo` tampil di dropdown `Brand`
13. Pilih `Dell`
14. Verifikasi `Model` tidak Disabled dan masih menampilkan placeholder `Select model`
15. Buka dropdown `Model`
16. Verifikasi opsi `No Model` berada paling atas di dropdown `Model`
17. Verifikasi opsi `Latitude 5440` dan `Inspiron 15 3530` tampil di dropdown `Model`
18. Verifikasi opsi `ThinkPad T14` tidak tampil di dropdown `Model`

### Satu Item adalah satu kombinasi Asset Name, Brand, dan Model
19. Tampilkan Halaman `Register Asset` dengan kondisi K1
20. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name` Item pertama
21. Pilih `Dell` di dropdown `Brand` Item pertama
22. Pilih `Latitude 5440` di dropdown `Model` Item pertama
23. Klik `[+ Asset Name]`
24. Pilih `Kursi Kerja Ergonomis` di dropdown `Asset Name` Item kedua
25. Verifikasi Item pertama tetap berisi `Laptop Dell Latitude 5440`, `Dell`, dan `Latitude 5440`
26. Verifikasi Item kedua berisi `Kursi Kerja Ergonomis` dengan Brand dan Model masih kosong

### Mengganti induk mengosongkan anak dan TAG Type mengikuti Asset Name
27. Tampilkan Halaman `Register Asset` dengan kondisi K1
28. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name`
29. Pilih `Dell` di dropdown `Brand`
30. Pilih `Latitude 5440` di dropdown `Model`
31. Verifikasi `TAG Type` menampilkan ikon `RFID`
32. Ganti Brand menjadi `Lenovo`
33. Verifikasi `Model` menampilkan placeholder `Select model`
34. Verifikasi `Asset Name` tetap `Laptop Dell Latitude 5440`
35. Pilih `ThinkPad T14` di dropdown `Model`
36. Ganti Asset Name menjadi `Printer Epson L3250`
37. Verifikasi `Brand` menampilkan placeholder `Select brand`
38. Verifikasi `Model` menampilkan placeholder `Select model`
39. Verifikasi `TAG Type` menampilkan ikon `RFID` dan ikon `NFC`

### Category menyaring Asset Name dan hanya node terbawah dapat dipilih
40. Tampilkan Halaman `Register Asset` dengan kondisi K1
41. Verifikasi kolom `Category` berada sebelum kolom `Asset Name`
42. Buka pemilih `Category`
43. Klik node `Laptop`
44. Klik `[Select]`
45. Verifikasi `Category` menampilkan badge berisi label node `Laptop`[^drift-1]
46. Buka dropdown `Asset Name`
47. Verifikasi opsi `Laptop Dell Latitude 5440` tampil di dropdown `Asset Name`
48. Verifikasi opsi `Kursi Kerja Ergonomis` tidak tampil di dropdown `Asset Name`
49. Buka pemilih `Category`
50. Klik node induk `Elektronik`
51. Klik `[Select]`
52. Verifikasi `Category` tetap menampilkan badge berisi label node `Laptop`[^drift-1]
53. Kosongkan `Category`
54. Verifikasi `Category` menampilkan placeholder `Select category`
55. Buka dropdown `Asset Name`
56. Verifikasi opsi `Kursi Kerja Ergonomis` tampil kembali di dropdown `Asset Name`

### Asset Name berupa dropdown master dan mengisi Category otomatis
57. Tampilkan Halaman `Register Asset` dengan kondisi K1
58. Ketik `Meja Tidak Terdaftar` pada dropdown `Asset Name`
59. Verifikasi `Meja Tidak Terdaftar` tidak menjadi nilai `Asset Name`
60. Pilih `Kursi Kerja Ergonomis` di dropdown `Asset Name`
61. Verifikasi `Category` terisi otomatis dengan badge berisi label node `Kursi`[^drift-1]
62. Verifikasi `TAG Type` menampilkan ikon `QR`
63. Pilih `Ergotec` di dropdown `Brand`
64. Pilih `ErgoMesh 200` di dropdown `Model`
65. Buka pemilih `Category`
66. Klik node `Laptop`
67. Klik `[Select]`
68. Verifikasi `Category` menampilkan badge berisi label node `Laptop`[^drift-1]
69. Verifikasi `Asset Name` menampilkan placeholder `Select asset name`
70. Verifikasi `Brand` menampilkan placeholder `Select brand`
71. Verifikasi `Model` menampilkan placeholder `Select model`

### Asset Name tanpa Brand terkait dan Category terisi kembali
72. Tampilkan Halaman `Register Asset` dengan kondisi K1
73. Pilih `Rak Besi Gudang` di dropdown `Asset Name`
74. Buka dropdown `Brand`
75. Verifikasi dropdown `Brand` menampilkan `No brand available`
76. Kosongkan `Category`
77. Verifikasi `Category` terisi kembali dengan badge berisi label node `Rak`[^drift-1]
78. Verifikasi `Asset Name` tetap `Rak Besi Gudang`

### Definisi Custom field Asset Name tidak berubah saat Category dikosongkan
79. Tampilkan Halaman `Register Asset` dengan kondisi K1
80. Pilih `Rak Besi Gudang` di dropdown `Asset Name`
81. Klik tab `Asset`
82. Verifikasi Item `Rak Besi Gudang` memuat kolom Custom field `Serial Number`
83. Klik tab `General Information`
84. Kosongkan `Category`
85. Verifikasi `Category` terisi kembali dengan badge berisi label node `Rak`[^drift-1]
86. Klik tab `Asset`
87. Verifikasi Item `Rak Besi Gudang` tetap memuat kolom Custom field `Serial Number`

### Category kosong tidak diperiksa saat Submit dan Save draft
88. Tampilkan Halaman `Register Asset` dengan kondisi K1
89. Klik `[Submit]`
90. Verifikasi pesan `Asset Name must not be empty` tampil di bawah sel `Asset Name`
91. Verifikasi tidak ada pesan error di bawah sel `Category`
92. Klik `[Save draft]`
93. Verifikasi field `Group` menampilkan pesan `Group must not be empty`
94. Verifikasi tidak ada pesan error di bawah sel `Category`

### Dropdown Asset Name dapat dicari dengan mengetik
95. Tampilkan Halaman `Register Asset` dengan kondisi K1
96. Ketik `Kursi` pada dropdown `Asset Name`
97. Verifikasi opsi `Kursi Kerja Ergonomis` tampil di dropdown `Asset Name`
98. Verifikasi opsi `Laptop Dell Latitude 5440`, `Printer Epson L3250`, dan `Rak Besi Gudang` tidak tampil di dropdown `Asset Name`

### Dropdown Brand dapat dicari dengan mengetik
99. Tampilkan Halaman `Register Asset` dengan kondisi K1
100. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name`
101. Ketik `Len` pada dropdown `Brand`
102. Verifikasi opsi `Lenovo` tampil di dropdown `Brand`
103. Verifikasi opsi `Dell` tidak tampil di dropdown `Brand`

### Dropdown Model dapat dicari dengan mengetik
104. Tampilkan Halaman `Register Asset` dengan kondisi K1
105. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name`
106. Pilih `Dell` di dropdown `Brand`
107. Ketik `Insp` pada dropdown `Model`
108. Verifikasi opsi `Inspiron 15 3530` tampil di dropdown `Model`
109. Verifikasi opsi `No Model` dan `Latitude 5440` tidak tampil di dropdown `Model`

[^drift-1]: Drift PRD vs kontrak komponen. PRD §4.1 tabel Item, baris Category (`TreeSelect`): format tampil `Path penuh`. Kontrak `TreeSelect#6`: mode single dengan node yang sudah dipilih menampilkan badge berisi LABEL node (bukan key). Diasersi: kontrak, yaitu badge berisi label node (`Laptop`, `Kursi`, `Rak`) dan bukan path penuh.
