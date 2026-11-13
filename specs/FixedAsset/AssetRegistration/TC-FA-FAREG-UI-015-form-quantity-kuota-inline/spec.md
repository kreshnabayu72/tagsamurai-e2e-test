---
id: TC-FA-FAREG-UI-015-form-quantity-kuota-inline
title: "Form Register Asset: validasi Quantity, pesan kuota, dan Remaining Quota"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["FAREG-LOGIC-05g", "FAREG-LOGIC-05m", "FI-REG-23", "FI-REG-24", "FLD-REG-05", "V-REG-10", "V-REG-17", "§4.2.1#b3", "§9.5#r1", "§9.9#r6"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-05g": [20, 37, 40, 46, 53, 55, 56]
  "FAREG-LOGIC-05m": [20, 24, 28, 37, 40, 43, 69, 70, 71, 72]
  "FI-REG-23": [34, 35, 39, 42]
  "FI-REG-24": [32, 48]
  "FLD-REG-05": [2, 4]
  "V-REG-10": [8, 11, 15, 16, 79]
  "V-REG-17": [20, 24, 28, 37, 40, 43, 53, 55]
  "§4.2.1#b3": [79, 80]
  "§9.5#r1": [2, 8]
  "§9.9#r6": [11, 15, 83]
anchor: [7, 31, 45, 47]
coverage:
  web: automated
---

# Form Register Asset: validasi Quantity, pesan kuota, dan Remaining Quota

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-015-1: sisa kuota tenant `500`.
  - DU-015-2: sisa kuota tenant `20`.
  - DU-015-3: sisa kuota tenant `1`.
  - DU-015-4: sisa kuota tenant `0`.
  - DU-015-5: sisa kuota tenant `10`.
  - DU-015-6: sisa kuota tenant `5`.
  - DU-015-7: Group `Gudang 2` dengan batas, sisa kuota Group `8`.
  - DU-015-8: Group `Gudang 3` dengan batas, sisa kuota Group `1`.
  - DU-015-9: Group `Gudang 4` dengan batas, sisa kuota Group `0`.
  - DU-015-10: Group `Gudang 5` tanpa batas.
  - DU-015-11: Group `Gudang 6` dengan batas, sisa kuota Group `3`.
  - DU-015-21: master Asset Name `Laptop Dell Latitude 5440`.
  - DU-015-22: master Asset Name `Kursi Kerja Ergonomis`.
  - DU-015-23: master Asset Name `Printer Epson L3250`.
  - DU-015-24: master Asset Name `Meja Kerja Lipat`.
- Kondisi:
  - K1: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item yang Asset Name-nya belum dipilih; master Asset Name memuat DU-015-21 sampai DU-015-24; sisa kuota tenant DU-015-1.
  - K2: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item yang Asset Name-nya belum dipilih; master Asset Name memuat DU-015-21 sampai DU-015-24; sisa kuota tenant DU-015-2; Group belum dipilih.
  - K3: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item yang Asset Name-nya belum dipilih; master Asset Name memuat DU-015-21 sampai DU-015-24; sisa kuota tenant DU-015-3; Group belum dipilih.
  - K4: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item yang Asset Name-nya belum dipilih; master Asset Name memuat DU-015-21 sampai DU-015-24; sisa kuota tenant DU-015-4; Group belum dipilih.
  - K5: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item yang Asset Name-nya belum dipilih; master Asset Name memuat DU-015-21 sampai DU-015-24; sisa kuota tenant DU-015-1; pohon Group memuat DU-015-7 sampai DU-015-10.
  - K6: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item yang Asset Name-nya belum dipilih; master Asset Name memuat DU-015-21 sampai DU-015-24; sisa kuota tenant DU-015-6; pohon Group memuat DU-015-11.
  - K7: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item yang Asset Name-nya belum dipilih; master Asset Name memuat DU-015-21 sampai DU-015-24; sisa kuota tenant DU-015-5; Group belum dipilih.

## Test Steps
### Quantity di dalam rentang dan nilai awal
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Verifikasi sel `Quantity` Item pertama menampilkan nilai awal `1`
3. Klik `[+ Asset Name]`
4. Verifikasi sel `Quantity` Item kedua menampilkan nilai awal `1`
5. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name` Item pertama
6. Ganti isi sel `Quantity` Item pertama dengan `100`
7. Verifikasi sel `Quantity` Item pertama menampilkan `100`
8. Verifikasi tidak ada pesan error di bawah sel `Quantity` Item pertama

### Quantity di bawah rentang dijepit ke batas bawah
9. Tampilkan Halaman `Register Asset` dengan kondisi K1
10. Ganti isi sel `Quantity` Item pertama dengan `0`, tekan Enter
11. Verifikasi sel `Quantity` Item pertama menampilkan `1`, yaitu nilai `0` yang diketik dijepit ke batas bawah[^drift-1]

### Quantity melebihi Register Asset Bulk Limit dijepit ke batas atas
12. Tampilkan Halaman `Register Asset` dengan kondisi K1
13. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name` Item pertama
14. Ganti isi sel `Quantity` Item pertama dengan `101`, tekan Enter
15. Verifikasi sel `Quantity` Item pertama menampilkan `100`, yaitu nilai `101` yang diketik dijepit ke batas atas[^drift-1]
16. Verifikasi tidak ada pesan rentang di bawah sel `Quantity` Item pertama[^drift-1]

### Pesan kuota tenant: banyak, satu, dan nol
17. Tampilkan Halaman `Register Asset` dengan kondisi K2
18. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name` Item pertama
19. Ganti isi sel `Quantity` Item pertama dengan `25`
20. Verifikasi pesan `Only 20 more assets can be added on your plan. Reduce the quantity.` tampil di bawah sel `Quantity`
21. Tampilkan Halaman `Register Asset` dengan kondisi K3
22. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name` Item pertama
23. Ganti isi sel `Quantity` Item pertama dengan `2`
24. Verifikasi pesan `Only 1 more asset can be added on your plan. Reduce the quantity.` tampil di bawah sel `Quantity`
25. Tampilkan Halaman `Register Asset` dengan kondisi K4
26. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name` Item pertama
27. Ganti isi sel `Quantity` Item pertama dengan `3`
28. Verifikasi pesan `No more assets can be added on your plan.` tampil di bawah sel `Quantity`

### Remaining Quota dan pesan kuota Group berubah langsung saat Group berubah
29. Tampilkan Halaman `Register Asset` dengan kondisi K5
30. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name` Item pertama
31. Verifikasi `Group` masih menampilkan `Select group`
32. Verifikasi `Remaining Quota` tidak tampil sebelum Group dipilih
33. Pilih Group `Gudang 2`
34. Verifikasi `Remaining Quota: 8` tampil di samping field `Group`
35. Verifikasi `Remaining Quota: 500` tidak tampil
36. Ganti isi sel `Quantity` Item pertama dengan `9`
37. Verifikasi pesan `Only 8 more assets can be added to Gudang 2. Reduce the quantity.` tampil di bawah sel `Quantity`
38. Pilih Group `Gudang 3`
39. Verifikasi `Remaining Quota: 1` tampil di samping field `Group`
40. Verifikasi pesan `Only 1 more asset can be added to Gudang 3. Reduce the quantity.` tampil di bawah sel `Quantity`
41. Pilih Group `Gudang 4`
42. Verifikasi `Remaining Quota: 0` tampil di samping field `Group`
43. Verifikasi pesan `No more assets can be added to Gudang 4.` tampil di bawah sel `Quantity`
44. Pilih Group `Gudang 5`
45. Verifikasi `Group` menampilkan `Gudang 5`
46. Verifikasi pesan kuota Group tidak tampil di bawah sel `Quantity`
47. Verifikasi sel `Quantity` Item pertama tetap menampilkan `9`
48. Verifikasi `Remaining Quota` tidak tampil untuk Group tanpa batas

### Sisa kuota tenant dibandingkan lebih dulu dari sisa kuota Group
49. Tampilkan Halaman `Register Asset` dengan kondisi K6
50. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name` Item pertama
51. Pilih Group `Gudang 6`
52. Ganti isi sel `Quantity` Item pertama dengan `4`
53. Verifikasi pesan `Only 3 more assets can be added to Gudang 6. Reduce the quantity.` tampil di bawah sel `Quantity`
54. Ganti isi sel `Quantity` Item pertama dengan `6`
55. Verifikasi pesan `Only 5 more assets can be added on your plan. Reduce the quantity.` tampil di bawah sel `Quantity`
56. Verifikasi pesan kuota Group tidak tampil bersamaan dengan pesan kuota tenant

### Error kuota ditandai pada Item pertama yang melampaui dan semua Item sesudahnya
57. Tampilkan Halaman `Register Asset` dengan kondisi K7
58. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name` Item pertama
59. Ganti isi sel `Quantity` Item pertama dengan `4`
60. Klik `[+ Asset Name]`
61. Pilih `Kursi Kerja Ergonomis` di dropdown `Asset Name` Item kedua
62. Ganti isi sel `Quantity` Item kedua dengan `4`
63. Klik `[+ Asset Name]`
64. Pilih `Printer Epson L3250` di dropdown `Asset Name` Item ketiga
65. Ganti isi sel `Quantity` Item ketiga dengan `4`
66. Klik `[+ Asset Name]`
67. Pilih `Meja Kerja Lipat` di dropdown `Asset Name` Item keempat
68. Ganti isi sel `Quantity` Item keempat dengan `1`
69. Verifikasi pesan kuota tampil di bawah sel `Quantity` Item ketiga
70. Verifikasi pesan kuota tampil di bawah sel `Quantity` Item keempat
71. Verifikasi pesan kuota tidak tampil di bawah sel `Quantity` Item pertama
72. Verifikasi pesan kuota tidak tampil di bawah sel `Quantity` Item kedua

### Total Quantity dua Item melebihi Register Asset Bulk Limit
73. Tampilkan Halaman `Register Asset` dengan kondisi K1
74. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name` Item pertama
75. Ganti isi sel `Quantity` Item pertama dengan `60`
76. Klik `[+ Asset Name]`
77. Pilih `Kursi Kerja Ergonomis` di dropdown `Asset Name` Item kedua
78. Ganti isi sel `Quantity` Item kedua dengan `41`
79. Verifikasi pesan `For more than 100 assets, use Import.` tampil di bawah sel `Quantity` Item kedua
80. Verifikasi pesan di bawah sel `Quantity` Item kedua memuat tautan `Import`

### Quantity hanya menerima angka
81. Tampilkan Halaman `Register Asset` dengan kondisi K1
82. Ganti isi sel `Quantity` Item pertama dengan `5x`
83. Verifikasi sel `Quantity` Item pertama menampilkan `5`

[^drift-1]: Drift PRD vs kontrak komponen. PRD V-REG-10 dan §9.9 baris Quantity: nilai di luar rentang 1 sampai [Max] memunculkan pesan `Quantity must be between 1 and [Max]` dengan timing Langsung. Kontrak `NumberInput#1`: `min` dan `max` adalah rentang, dan saat blur atau Enter nilai dijepit ke batas terdekat (`-7` menjadi `0`, di atas `max` menjadi `max`). Kontrak `NumberInput#15`: tidak ada pesan rentang dan tidak ada keadaan invalid untuk nilai di luar `min`/`max`, hanya dijepit. Diasersi: kontrak, yaitu `0` dijepit menjadi `1` dan `101` dijepit menjadi `100` tanpa pesan rentang.
