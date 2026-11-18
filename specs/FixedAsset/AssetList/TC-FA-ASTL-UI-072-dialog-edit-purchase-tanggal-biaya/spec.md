---
id: TC-FA-ASTL-UI-072-dialog-edit-purchase-tanggal-biaya
title: "Validasi Purchase Date, Purchase Cost, dan Reference Price"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-21b", "ASTL-LOGIC-21e", "ASTL-LOGIC-21a", "ASTL-LOGIC-21i", "FI-02", "V-09", "V-12", "V-16", "S-25", "S-26", "EC-39", "EC-40", "EC-47", "FLD-27", "FLD-28", "FLD-29", "§4.1i#b2", "§4.1i#b8", "§9.9#r1", "§9.9#r2", "§9.9#r3"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-21b": [14, 16, 22, 23, 25, 77, 78]
  "ASTL-LOGIC-21e": [28, 30, 37]
  "ASTL-LOGIC-21a": [8, 11]
  "ASTL-LOGIC-21i": [53, 57, 62, 67]
  "FI-02": [53, 57, 62, 67]
  "V-09": [8, 11, 82]
  "V-12": [53, 57]
  "V-16": [40, 42, 45, 49, 85]
  "S-25": [14, 16]
  "S-26": [28, 30]
  "EC-39": [14, 19]
  "EC-40": [28, 33, 35, 37]
  "EC-47": [53, 57]
  "FLD-27": [2, 14]
  "FLD-28": [3, 28]
  "FLD-29": [4]
  "§4.1i#b2": [53, 69, 70, 72, 74, 95, 101]
  "§4.1i#b8": [14, 28]
  "§9.9#r1": [2, 8, 11]
  "§9.9#r2": [40, 42, 49, 88, 90]
  "§9.9#r3": [45, 53, 57, 98, 101]
anchor: []
coverage:
  web: automated
---
# Validasi Purchase Date, Purchase Cost, dan Reference Price

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Edit Purchase
- Data:
  - DU-072-1: Aset `Kursi Kerja - 2`, Asset ID `AST-0073`, Group `GA`, Purchase `Pending` dengan seluruh field Purchase kosong, tidak berjejak Posted.
  - DU-072-2: Aset `Meja Rapat - 3`, Asset ID `AST-0052`, Group `GA`, Purchase `Complete`, tidak berjejak Posted, Additional costs `Instalasi` `250.000,00`.
  - DU-072-3: Aset `Meja Rapat - 4`, Asset ID `AST-0053`, Group `GA`, Purchase `Complete`, tidak berjejak Posted, Additional costs `Bea masuk` `9.999.999.999.999,99`.
  - DU-072-4: Aset `Server Rack - 2`, Asset ID `AST-0041`, Group `IT`, Purchase `Complete`, berjejak Posted.
  - DU-072-5: Aset `Printer Laser - 3`, Asset ID `AST-0033`, Group `IT`, Purchase `Complete`, tidak berjejak Posted, Reference Price tersimpan Currency `JPY` jumlah `150.000,00`.
  - DU-072-6: Tanggal masa depan `19/11/26`.
  - DU-072-7: Tanggal hari ini `18/11/26`.
  - DU-072-8: Tanggal sebelum First Accounting Period `15/12/25`.
  - DU-072-9: Tanggal di bulan First Accounting Period `15/01/26`.
  - DU-072-10: Purchase Cost `0`.
  - DU-072-11: Purchase Cost `18.500.000,00`.
  - DU-072-12: Purchase Cost tepat di batas `1234567890123,45` (15 digit termasuk 2 digit desimal).
  - DU-072-13: Purchase Cost satu di atas batas `12345678901234,56` (16 digit termasuk 2 digit desimal).
  - DU-072-14: Reference Price Currency `USD` dan jumlah `1.150,00`.
  - DU-072-15: Reference Price jumlah satu di atas batas `12345678901234,56` (16 digit termasuk 2 digit desimal).
  - DU-072-16: Purchase Cost `100,00`.
  - DU-072-17: Reference Price jumlah tepat di batas `1234567890123,45` (15 digit termasuk 2 digit desimal).
  - DU-072-18: Purchase Cost dengan tiga digit desimal `1,234`, yang diharapkan tersimpan di field `1,23`.
  - DU-072-19: Purchase Cost bertanda minus `-50`, yang diharapkan tersimpan di field `50`.
  - DU-072-20: Jumlah Reference Price bertanda minus `-50`.
- Kondisi:
  - Semua kondisi: tanggal hari ini bernilai `18/11/26`, Date Format bernilai `dd/MM/yy`, dan lisensi akuntansi aktif dengan First Accounting Period Januari 2026, kecuali K2 dan K8.
  - K1: satu aset terpilih, DU-072-1; simpan berhasil.
  - K2: satu aset terpilih, DU-072-1; lisensi akuntansi tidak aktif; simpan berhasil.
  - K3: satu aset terpilih, DU-072-2; simpan berhasil.
  - K4: satu aset terpilih, DU-072-3; simpan ditolak validasi klien.
  - K5: satu aset terpilih, DU-072-5; addon Currency tidak aktif.
  - K6: satu aset terpilih, DU-072-4; daftar mata uang addon Currency yang aktif adalah `USD` dan `EUR`.
  - K7: satu aset terpilih, DU-072-5; addon Currency aktif; simpan berhasil.
  - K8: satu aset terpilih, DU-072-1; lisensi akuntansi aktif tetapi First Accounting Period belum ditetapkan.
  - K9: Bulk, seleksi DU-072-1 dan DU-072-2.

## Test Steps

### Isi awal field Purchase Date, Purchase Cost, dan Reference Price
1. Tampilkan Dialog Edit Purchase dengan kondisi K1
2. Verifikasi field berlabel `Purchase Date` kosong dengan placeholder `Select date`
3. Verifikasi field berlabel `Purchase Cost` kosong dengan placeholder `Enter purchase cost`
4. Verifikasi field berlabel `Reference Price` kosong dengan placeholder `Select currency` dan `Enter amount`

### Purchase Date tidak boleh setelah hari ini
5. Tampilkan Dialog Edit Purchase dengan kondisi K1
6. Pilih Purchase Date `19/11/26`
7. Klik `[Save]`
8. Verifikasi alert inline `Purchase date cannot be in the future` tampil dan dialog `Edit Purchase` tetap terbuka
9. Pilih Purchase Date `18/11/26`
10. Klik `[Save]`
11. Verifikasi dialog `Edit Purchase` tertutup

### Purchase Date sebelum First Accounting Period diizinkan dengan helper text
12. Tampilkan Dialog Edit Purchase dengan kondisi K1
13. Pilih Purchase Date `15/12/25`
14. Verifikasi helper text `Depreciation for earlier periods will be caught up.` tampil di bawah Purchase Date
15. Pilih Purchase Date `15/01/26`
16. Verifikasi helper text `Depreciation for earlier periods will be caught up.` tidak tampil
17. Pilih Purchase Date `15/12/25`
18. Klik `[Save]`
19. Verifikasi dialog `Edit Purchase` tertutup

### Tanpa lisensi akuntansi Purchase Date tidak dibatasi
20. Tampilkan Dialog Edit Purchase dengan kondisi K2
21. Pilih Purchase Date `15/12/25`
22. Verifikasi field Purchase Date berisi `15/12/25`
23. Verifikasi helper text `Depreciation for earlier periods will be caught up.` tidak tampil
24. Klik `[Save]`
25. Verifikasi dialog `Edit Purchase` tertutup

### Purchase Cost 0 tanpa Additional costs
26. Tampilkan Dialog Edit Purchase dengan kondisi K1
27. Isi Purchase Cost `0`
28. Verifikasi helper text `Asset value will be 0 and the asset will not be depreciated.` tampil di bawah Purchase Cost
29. Isi Purchase Cost `18.500.000,00`
30. Verifikasi helper text `Asset value will be 0 and the asset will not be depreciated.` tidak tampil
31. Isi Purchase Cost `0`
32. Klik `[Save]`
33. Verifikasi dialog `Edit Purchase` tertutup

### Purchase Cost 0 dengan Additional costs lebih dari 0
34. Tampilkan Dialog Edit Purchase dengan kondisi K3
35. Verifikasi bagian Additional costs memuat baris `Instalasi` dengan jumlah `250.000,00`
36. Isi Purchase Cost `0`
37. Verifikasi helper text `Asset value will be 0 and the asset will not be depreciated.` tidak tampil

### Batas 15 digit pada Purchase Cost
38. Tampilkan Dialog Edit Purchase dengan kondisi K1
39. Isi Purchase Cost `1234567890123,45`
40. Verifikasi field Purchase Cost menerima nilai tanpa pesan `Max. 15 characters`
41. Isi Purchase Cost `12345678901234,56`
42. Verifikasi pesan `Max. 15 characters` tampil di bawah field Purchase Cost

### Batas 15 digit pada jumlah Reference Price
43. Tampilkan Dialog Edit Purchase dengan kondisi K1
44. Isi jumlah Reference Price `12345678901234,56`
45. Verifikasi pesan `Max. 15 characters` tampil di bawah jumlah Reference Price

### Total Purchase Cost dan Additional costs melebihi 15 digit
46. Tampilkan Dialog Edit Purchase dengan kondisi K4
47. Isi Purchase Cost `100,00`
48. Klik `[Save]`
49. Verifikasi pesan `Max. 15 characters` tampil di bawah field Purchase Cost dan dialog `Edit Purchase` tetap terbuka

### Reference Price diisi sebagian ditolak
50. Tampilkan Dialog Edit Purchase dengan kondisi K1
51. Pilih Currency `USD` pada Reference Price
52. Klik `[Save]`
53. Verifikasi pesan `Select a currency and enter an amount, or leave both empty.` tampil di bawah field Reference Price dan dialog `Edit Purchase` tetap terbuka
54. Tampilkan Dialog Edit Purchase dengan kondisi K1
55. Isi jumlah Reference Price `1.150,00`
56. Klik `[Save]`
57. Verifikasi pesan `Select a currency and enter an amount, or leave both empty.` tampil di bawah field Reference Price dan dialog `Edit Purchase` tetap terbuka

### Reference Price diisi lengkap diterima
58. Tampilkan Dialog Edit Purchase dengan kondisi K1
59. Pilih Currency `USD` pada Reference Price
60. Isi jumlah Reference Price `1.150,00`
61. Klik `[Save]`
62. Verifikasi dialog `Edit Purchase` tertutup

### Reference Price dikosongkan bersama diterima
63. Tampilkan Dialog Edit Purchase dengan kondisi K7
64. Kosongkan pilihan Currency pada Reference Price
65. Kosongkan jumlah Reference Price
66. Klik `[Save]`
67. Verifikasi dialog `Edit Purchase` tertutup

### Reference Price saat addon Currency tidak aktif
68. Tampilkan Dialog Edit Purchase dengan kondisi K5
69. Verifikasi Reference Price tersimpan `JPY` dan `150.000,00` tampil
70. Verifikasi bagian Reference Price read-only

### Reference Price pada aset berjejak Posted dan daftar mata uang
71. Tampilkan Dialog Edit Purchase dengan kondisi K6
72. Verifikasi bagian Reference Price dapat diisi
73. Klik pilihan Currency pada Reference Price
74. Verifikasi pilihan Currency hanya `USD` dan `EUR`

### Purchase Date saat First Accounting Period belum ditetapkan
75. Tampilkan Dialog Edit Purchase dengan kondisi K8
76. Pilih Purchase Date `15/12/25`
77. Verifikasi field Purchase Date berisi `15/12/25`
78. Verifikasi helper text `Depreciation for earlier periods will be caught up.` tidak tampil

### Purchase Date masa depan pada Bulk
79. Tampilkan Dialog Edit Purchase dengan kondisi K9
80. Pilih Purchase Date `19/11/26`
81. Klik `[Save]`
82. Verifikasi alert inline `Purchase date cannot be in the future` tampil dan dialog `Edit Purchase` tetap terbuka

### Batas pas 15 digit pada jumlah Reference Price
83. Tampilkan Dialog Edit Purchase dengan kondisi K1
84. Isi jumlah Reference Price `1234567890123,45`
85. Verifikasi jumlah Reference Price menerima nilai tanpa pesan `Max. 15 characters`

### Digit desimal ketiga dan tanda minus diblok pada Purchase Cost
86. Tampilkan Dialog Edit Purchase dengan kondisi K1
87. Isi Purchase Cost `1,234`
88. Verifikasi field Purchase Cost berisi `1,23` karena digit desimal ketiga diblok
89. Isi Purchase Cost `-50`
90. Verifikasi field Purchase Cost berisi `50` karena tanda minus diblok

### Reference Price dikirim apa adanya tanpa konversi kurs
91. Tampilkan Dialog Edit Purchase dengan kondisi K1
92. Pilih Currency `USD` pada Reference Price
93. Isi jumlah Reference Price `1.150,00`
94. Klik `[Save]`
95. Verifikasi permintaan simpan memuat Reference Price Currency `USD` dan jumlah `1.150,00` apa adanya, tanpa konversi kurs

### Jumlah Reference Price negatif tidak diterima
96. Tampilkan Dialog Edit Purchase dengan kondisi K1
97. Pilih Currency `USD` pada Reference Price
98. Verifikasi Currency `USD` terpilih pada Reference Price
99. Isi jumlah Reference Price `-50`
100. Klik `[Save]`
101. Verifikasi tidak ada permintaan simpan yang memuat jumlah Reference Price negatif
