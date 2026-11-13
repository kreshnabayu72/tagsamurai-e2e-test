---
id: TC-FA-FAREG-UI-017-form-tab-asset-tampilan
title: "Form Register Asset: tab Asset, tabel Asset per Item, badge, dan kartu filter"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FAREG-04", "F-FAREG-15", "FAREG-LOGIC-04b", "FAREG-LOGIC-11e", "FAREG-LOGIC-17a", "FLD-REG-06", "S-REG-06", "§4.1#b21", "§4.1#b22", "§4.1#b23", "§4.1#b24", "§4.1#b28", "§4.1#p28", "§4.1#r98", "§4.1#r99", "§4.1#r100", "§4.1#r102", "§4.1#r103", "§4.1#r104", "§4.1#r105", "§4.4#r9", "§4.5#p1", "§9.9#r7"]
smoke: []
dependsOn: []
trace:
  "F-FAREG-04": [37, 40, 114]
  "F-FAREG-15": [13, 19, 20]
  "FAREG-LOGIC-04b": [20, 77, 90, 93, 91]
  "FAREG-LOGIC-11e": [36, 37, 38, 97, 99, 111, 112, 113, 114, 118]
  "FAREG-LOGIC-17a": [13, 22]
  "FLD-REG-06": [27, 28]
  "S-REG-06": [80, 81, 85, 86]
  "§4.1#b21": 3
  "§4.1#b22": [3, 4, 5, 6, 7, 73]
  "§4.1#b23": [9, 10]
  "§4.1#b24": [43, 44, 45, 46]
  "§4.1#b28": 66
  "§4.1#p28": [3, 30, 32, 48, 49, 51, 54, 55, 59, 60, 61, 62, 64]
  "§4.1#r98": 9
  "§4.1#r99": [11, 12]
  "§4.1#r100": [13, 19, 20, 22, 102]
  "§4.1#r102": [14, 15]
  "§4.1#r103": [16, 27]
  "§4.1#r104": [36, 37, 38, 40, 112, 114, 118]
  "§4.1#r105": 17
  "§4.4#r9": 42
  "§4.5#p1": [36, 73, 70, 107]
  "§9.9#r7": 27
anchor: [68, 72, 101]
coverage:
  web: automated
---

# Form Register Asset: tab Asset, tabel Asset per Item, badge, dan kartu filter

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-017-1: Item `Laptop Dell Latitude 5440`, TAG Type `RFID`, Quantity `3`, Custom field per aset `Serial Number` (teks, wajib); aset `Laptop Dell Latitude 5440 - 1` ber-Serial Number `SN-LDL-0001`, Tag `RFID-000201` Verified, Photo `2`, Condition `Normal`, Status `✓ Ready`; aset `Laptop Dell Latitude 5440 - 2` tanpa Serial Number dan tanpa Tag, Photo `1`, Condition `Normal`, kekurangan `Serial Number` dan `Tag` sehingga Status `Serial Number` dengan `+1`; aset `Laptop Dell Latitude 5440 - 3` ber-Serial Number `SN-LDL-0003`, tanpa Tag, tanpa Photo, Condition `Normal`, kekurangan `Tag` saja.
  - DU-017-2: Item `Kursi Kerja Ergonomis`, TAG Type `QR`, Quantity `2`, tanpa Custom field per aset; aset `Kursi Kerja Ergonomis - 1` ber-Tag `QR-000301` dan aset `Kursi Kerja Ergonomis - 2` ber-Tag `QR-000302`, keduanya Condition `Normal` dan Ready.
  - DU-017-3: Item `Printer Epson L3250`, TAG Type `RFID`, Quantity `2`, Custom field per aset `Tanggal Garansi` (tanggal) dan `Jenis Tinta` (pilihan, placeholder `Select Jenis Tinta`); aset `Printer Epson L3250 - 1` ber-Tag `RFID-000401`, Tanggal Garansi `15/11/2026`, Jenis Tinta `Black`, Condition `Normal`, Ready; aset `Printer Epson L3250 - 2` tanpa Tag, tanpa Tanggal Garansi, tanpa Jenis Tinta, Condition `Normal`, kekurangan `Tag`.
  - DU-017-4: Item `Meja Lipat Aluminium`, TAG Type `Non-TAG`, Quantity `1`; aset `Meja Lipat Aluminium - 1`.
  - DU-017-5: Item `Laptop Dell Latitude 5440` dengan 12 aset bernama `Laptop Dell Latitude 5440 - 1` sampai `Laptop Dell Latitude 5440 - 12`.
  - DU-017-8: Custom field `Catatan Lokasi`, Scope `General`, teks, tidak wajib, Value Type Specific (Nilai per aset), berlaku bagi semua Asset Name.
  - DU-017-9: Item `Laptop Dell Latitude 5440` tanpa Brand dan tanpa Model, TAG Type `RFID`, Quantity `1`, Custom field per aset `Serial Number` (teks, wajib); aset `Laptop Dell Latitude 5440 - 1` tanpa Serial Number dan tanpa Tag, Condition `Normal`, kekurangan berurutan `Brand`, `Model`, `Serial Number`, `Tag`.
  - DU-017-10: Item `Kursi Kerja Ergonomis` dengan Brand `Ergotec` dan Model `ErgoMesh 200`, TAG Type `QR`, Quantity `1`; aset `Kursi Kerja Ergonomis - 1` tanpa Tag, Condition `Damaged` dan Damage note kosong, kekurangan berurutan `Damage note`, `Tag`.
  - DU-017-11: Item `Kursi Kerja Ergonomis` dengan Brand `Ergotec` dan Model `ErgoMesh 200`, TAG Type `QR`, Quantity `2`, tanpa Custom field per aset; aset `Kursi Kerja Ergonomis - 1` ber-Tag `Skipped`, Condition `Normal`, Tingkat 2 lain lengkap sehingga Status `✓ Ready`; aset `Kursi Kerja Ergonomis - 2` ber-Tag `Unverified` dan Condition `Normal`, kekurangan `Tag` saja.
  - DU-017-12: Item `Laptop Dell Latitude 5440` dengan Brand `Dell` dan Model `Latitude 5440`, TAG Type `RFID`, Quantity `1`, Custom field per aset `Serial Number` (teks, wajib); aset `Laptop Dell Latitude 5440 - 1` tanpa Serial Number, ber-Tag `RFID-000501` Verified, Condition `Damaged` dan Damage note kosong, kekurangan berurutan `Serial Number`, `Damage note` sehingga Status `Serial Number` dengan `+1`.
- Kondisi:
  - K1: form `Edit` draft tersimpan dengan Item DU-017-1, DU-017-2, dan DU-017-3; format tanggal General Settings `DD/MM/YYYY`; kartu filter berjumlah `All` 7, `Needs data` 3, `Ready` 4.
  - K2: form `Edit` draft tersimpan dengan Item DU-017-4 dan DU-017-2.
  - K3: form `Register Asset` baru tanpa Asset Name yang dipilih.
  - K4: form `Edit` draft tersimpan dengan Item DU-017-2 saja.
  - K5: form `Edit` draft tersimpan dengan Item DU-017-5.
  - K6: form `Edit` draft tersimpan dengan Item DU-017-1 dan DU-017-2; master Custom field DU-017-8.
  - K7: form `Edit` draft tersimpan dengan Item DU-017-9 dan DU-017-10.
  - K8: sama dengan K1; lebar viewport sempit.
  - K9: form `Edit` draft tersimpan dengan Item DU-017-11 dan DU-017-12.

## Test Steps
### Accordion per Item, badge, dan kolom tabel aset
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Klik tab `Asset`
3. Verifikasi aset dikelompokkan per Item dengan judul Item `Laptop Dell Latitude 5440`, `Kursi Kerja Ergonomis`, dan `Printer Epson L3250`
4. Verifikasi judul Item `Laptop Dell Latitude 5440` memuat badge `Incomplete`
5. Verifikasi judul Item `Kursi Kerja Ergonomis` memuat badge `Complete`
6. Verifikasi tooltip `2 assets still need data.` tampil saat pointer berada di badge `Incomplete` Item `Laptop Dell Latitude 5440`
7. Verifikasi tooltip `1 asset still needs data.` tampil saat pointer berada di badge `Incomplete` Item `Printer Epson L3250`
8. Klik judul Item `Laptop Dell Latitude 5440`
9. Verifikasi kolom `#` menampilkan nomor urut `1`, `2`, dan `3` pada tabel Item `Laptop Dell Latitude 5440`
10. Verifikasi tabel aset tidak memiliki checkbox
11. Verifikasi kolom `Name` menampilkan `Laptop Dell Latitude 5440 - 1`
12. Verifikasi kolom `Name` terisi pada `Laptop Dell Latitude 5440 - 2` dan `Laptop Dell Latitude 5440 - 3`
13. Verifikasi kolom `Serial Number` pada `Laptop Dell Latitude 5440 - 2` menampilkan placeholder `Enter value`
14. Verifikasi kolom `Photo` pada `Laptop Dell Latitude 5440 - 1` menampilkan `2`
15. Verifikasi kolom `Photo` pada `Laptop Dell Latitude 5440 - 3` menampilkan `—`
16. Verifikasi kolom `Condition` pada `Laptop Dell Latitude 5440 - 1` menampilkan `Normal` tanpa placeholder
17. Verifikasi row option (titik tiga) pada `Laptop Dell Latitude 5440 - 1` memuat `Detail`
18. Klik judul Item `Printer Epson L3250`
19. Verifikasi kolom `Tanggal Garansi` pada `Printer Epson L3250 - 2` menampilkan placeholder `Select date`
20. Verifikasi kolom `Jenis Tinta` pada `Printer Epson L3250 - 2` menampilkan placeholder `Select Jenis Tinta`
21. Klik judul Item `Kursi Kerja Ergonomis`
22. Verifikasi tabel Item `Kursi Kerja Ergonomis` tidak memiliki kolom Custom field per aset

### Condition dan Custom field per aset dapat diedit
23. Tampilkan Halaman `Register Asset` dengan kondisi K1
24. Klik tab `Asset`
25. Klik judul Item `Laptop Dell Latitude 5440`
26. Klik sel `Condition` pada `Laptop Dell Latitude 5440 - 1`
27. Verifikasi opsi `Normal` dan `Damaged` tampil di dropdown `Condition`
28. Verifikasi opsi `Missing` tidak tampil di dropdown `Condition`
29. Klik `Damaged`
30. Verifikasi sel `Condition` pada `Laptop Dell Latitude 5440 - 1` menampilkan `Damaged`
31. Ganti isi sel `Serial Number` pada `Laptop Dell Latitude 5440 - 2` dengan `SN-LDL-0002`
32. Verifikasi sel `Serial Number` pada `Laptop Dell Latitude 5440 - 2` menampilkan `SN-LDL-0002`

### Kolom Status, daftar kekurangan, dan kartu filter
33. Tampilkan Halaman `Register Asset` dengan kondisi K1
34. Klik tab `Asset`
35. Klik judul Item `Laptop Dell Latitude 5440`
36. Verifikasi Status `Laptop Dell Latitude 5440 - 1` menampilkan teks `✓ Ready`
37. Verifikasi Status `Laptop Dell Latitude 5440 - 2` menampilkan kekurangan pertama `Serial Number` dan `+1`
38. Verifikasi Status `Laptop Dell Latitude 5440 - 3` menampilkan `Tag` tanpa `+N`
39. Arahkan pointer ke Status `Laptop Dell Latitude 5440 - 2`
40. Verifikasi daftar kekurangan lengkap `Serial Number` dan `Tag` tampil pada hover Status
41. Klik `+1` pada Status `Laptop Dell Latitude 5440 - 2`
42. Verifikasi popover daftar kekurangan lengkap memuat `Serial Number` dan `Tag`
43. Verifikasi kartu filter `All`, `Needs data`, dan `Ready` tampil
44. Verifikasi kartu `All` menampilkan jumlah `7`
45. Verifikasi kartu `Needs data` menampilkan jumlah `3`
46. Verifikasi kartu `Ready` menampilkan jumlah `4`
47. Klik kartu `Needs data`
48. Verifikasi tabel Item `Laptop Dell Latitude 5440` memuat `Laptop Dell Latitude 5440 - 2` dan `Laptop Dell Latitude 5440 - 3`
49. Verifikasi `Laptop Dell Latitude 5440 - 1` tidak tampil di tabel
50. Klik judul Item `Printer Epson L3250`
51. Verifikasi tabel Item `Printer Epson L3250` memuat `Printer Epson L3250 - 2`
52. Klik kartu `Ready`
53. Klik judul Item `Laptop Dell Latitude 5440`
54. Verifikasi tabel memuat `Laptop Dell Latitude 5440 - 1`
55. Verifikasi `Laptop Dell Latitude 5440 - 2` tidak tampil di tabel

### Tabel aset memakai paginasi tanpa colvis, Search, filter, dan sort
56. Tampilkan Halaman `Register Asset` dengan kondisi K5
57. Klik tab `Asset`
58. Klik judul Item `Laptop Dell Latitude 5440`
59. Verifikasi paginasi menawarkan `10`, `25`, `50`, dan `100`
60. Verifikasi kontrol column visibility tidak tampil pada tabel aset
61. Verifikasi kotak Search tidak tampil pada tabel aset
62. Verifikasi filter selain kartu filter tidak tampil pada tabel aset
63. Klik header kolom `Name`
64. Verifikasi urutan aset tetap `Laptop Dell Latitude 5440 - 1`, `Laptop Dell Latitude 5440 - 2`, `Laptop Dell Latitude 5440 - 3` dari atas

### Accordion dapat dilipat dengan keyboard
65. Tampilkan Halaman `Register Asset` dengan kondisi K1
66. Verifikasi tabel General Information tidak memuat kolom `Condition`
67. Klik tab `Asset`
68. Verifikasi judul Item `Laptop Dell Latitude 5440` tampil sebelum dibuka
69. Tekan `Enter` pada judul Item `Laptop Dell Latitude 5440`
70. Verifikasi baris `Laptop Dell Latitude 5440 - 1` tampil karena Accordion dibuka
71. Tekan `Enter` pada judul Item `Laptop Dell Latitude 5440`
72. Verifikasi judul Item `Laptop Dell Latitude 5440` tetap tampil
73. Verifikasi baris `Laptop Dell Latitude 5440 - 1` tidak tampil karena Accordion dilipat

### Item TAG Type Non-TAG tidak memiliki slot Tag
74. Tampilkan Halaman `Register Asset` dengan kondisi K2
75. Klik tab `Asset`
76. Klik judul Item `Meja Lipat Aluminium`
77. Verifikasi kolom Tag pada `Meja Lipat Aluminium - 1` menampilkan `No tag`

### Empty state tab Asset dan hasil saring kosong
78. Tampilkan Halaman `Register Asset` dengan kondisi K3
79. Klik tab `Asset`
80. Verifikasi tab `Asset` menampilkan `No assets yet`
81. Verifikasi tab `Asset` menampilkan `Select an Asset Name in General Information to see the assets here.`
82. Tampilkan Halaman `Register Asset` dengan kondisi K4
83. Klik tab `Asset`
84. Klik kartu `Needs data`
85. Verifikasi tabel menampilkan `No results found`
86. Verifikasi tabel menampilkan `Try adjusting your search or filter.`

### Custom field Scope General tampil di semua Item dan Scope Specific hanya pada Asset Name-nya
87. Tampilkan Halaman `Register Asset` dengan kondisi K6
88. Klik tab `Asset`
89. Klik judul Item `Kursi Kerja Ergonomis`
90. Verifikasi tabel Item `Kursi Kerja Ergonomis` memuat kolom Custom field `Catatan Lokasi`
91. Verifikasi tabel Item `Kursi Kerja Ergonomis` tidak memuat kolom Custom field `Serial Number`
92. Klik judul Item `Laptop Dell Latitude 5440`
93. Verifikasi tabel Item `Laptop Dell Latitude 5440` memuat kolom Custom field `Catatan Lokasi` dan `Serial Number`

### Kekurangan pertama Status mengikuti urutan kolom
94. Tampilkan Halaman `Register Asset` dengan kondisi K7
95. Klik tab `Asset`
96. Klik judul Item `Laptop Dell Latitude 5440`
97. Verifikasi Status `Laptop Dell Latitude 5440 - 1` menampilkan kekurangan pertama `Brand` dan `+3`
98. Klik judul Item `Kursi Kerja Ergonomis`
99. Verifikasi Status `Kursi Kerja Ergonomis - 1` menampilkan kekurangan pertama `Damage note` dan `+1`

### Tabel Item tab General Information tanpa isian Custom field
100. Tampilkan Halaman `Register Asset` dengan kondisi K1
101. Verifikasi tabel Item memuat `Laptop Dell Latitude 5440`, `Kursi Kerja Ergonomis`, dan `Printer Epson L3250`
102. Verifikasi tidak ada kolom atau isian Custom field `Serial Number`, `Tanggal Garansi`, dan `Jenis Tinta` di tabel Item

### Panel samping aset turun di bawah form pada lebar sempit
103. Tampilkan Halaman `Register Asset` dengan kondisi K8
104. Klik tab `Asset`
105. Klik judul Item `Laptop Dell Latitude 5440`
106. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
107. Verifikasi panel samping aset `Laptop Dell Latitude 5440 - 1` berada di bawah form

### Aset ber-Tag Skipped dihitung terisi dan Tag Unverified tetap kekurangan
108. Tampilkan Halaman `Register Asset` dengan kondisi K9
109. Klik tab `Asset`
110. Klik judul Item `Kursi Kerja Ergonomis`
111. Verifikasi kolom Tag pada `Kursi Kerja Ergonomis - 1` menampilkan `Skipped`
112. Verifikasi Status `Kursi Kerja Ergonomis - 1` menampilkan teks `✓ Ready`
113. Verifikasi kolom Tag pada `Kursi Kerja Ergonomis - 2` menampilkan `Unverified`
114. Verifikasi Status `Kursi Kerja Ergonomis - 2` menampilkan `Tag` tanpa `+N`

### Custom field wajib mendahului Damage note pada kekurangan pertama Status
115. Tampilkan Halaman `Register Asset` dengan kondisi K9
116. Klik tab `Asset`
117. Klik judul Item `Laptop Dell Latitude 5440`
118. Verifikasi Status `Laptop Dell Latitude 5440 - 1` menampilkan kekurangan pertama `Serial Number` dan `+1`
