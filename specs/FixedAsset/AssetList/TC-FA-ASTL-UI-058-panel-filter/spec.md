---
id: TC-FA-ASTL-UI-058-panel-filter
title: "Mekanik Panel Filter"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-14m", "FI-27", "§4.1c#p1", "§4.1c#b3", "EB-FLT-2@tabel-all-assets"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-14m": 5
  "FI-27": [66, 68, 69]
  "§4.1c#p1": [3, 4, 12, 13, 18, 19]
  "§4.1c#b3": [66, 68]
  "EB-FLT-2@tabel-all-assets": [10, 14, 15, 27, 29, 35, 36, 38, 39, 41, 45, 47, 51, 58, 60, 61, 73]
anchor: [24, 56]
coverage:
  web: automated
---
# Mekanik Panel Filter

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Panel Filter All Assets
- Data:
  - DU-058-1: Aset pertama: Name `Laptop Dell - 1`, Brand `Dell`, Status `Available`, Category `Laptop` di bawah node `Elektronik`.
  - DU-058-2: Aset kedua: Name `Printer Laser - 1`, Brand `Epson`, Status `Not Paired Yet`, Category `Printer` di bawah node `Elektronik`.
  - DU-058-3: Aset ketiga: Name `Kursi Kerja - 1`, Brand `Ikea`, Status `Available`, Category `Kursi` di bawah node `Furnitur`.
- Kondisi:
  - K1: tabel memuat DU-058-1 sampai DU-058-3, dan opsi Brand serta Status mengikuti nilai pada ketiga data itu.
  - K2: tabel tidak memuat satu pun baris sehingga sumber opsi Brand kosong.
  - K3: tabel memuat aset dengan sedikitnya delapan nilai Brand berbeda, sehingga chip seluruh opsi terpilih melebihi lebar field Brand.

## Test Steps

### Panel dibuka dari ikon Filter dan Filter Group tidak ada
1. Tampilkan Panel Filter All Assets dengan kondisi K1
2. Klik ikon Filter
3. Verifikasi panel Filter terbuka dengan field `Brand` berplaceholder `All brands`
4. Verifikasi panel memuat tombol `[Clear Field]` lalu `[Apply]`
5. Verifikasi panel tidak memuat field Group

### Opsi dalam satu field digabung OR dan antar field digabung AND
6. Tampilkan Panel Filter All Assets dengan kondisi K1
7. Klik ikon Filter
8. Pilih `Dell` pada field Brand
9. Pilih `Epson` pada field Brand
10. Verifikasi field Brand menampilkan chip `Dell` dan chip `Epson`
11. Klik `[Apply]`
12. Verifikasi tabel memuat `Laptop Dell - 1` dan `Printer Laser - 1`
13. Verifikasi `Kursi Kerja - 1` tidak tampil di tabel
14. Verifikasi ikon Filter menampilkan indikator titik
15. Verifikasi panel Filter tetap terbuka
16. Pilih `Available` pada field Status
17. Klik `[Apply]`
18. Verifikasi tabel memuat `Laptop Dell - 1`
19. Verifikasi `Printer Laser - 1` tidak tampil di tabel

### Menutup panel tanpa Apply membuang draft
20. Tampilkan Panel Filter All Assets dengan kondisi K1
21. Klik ikon Filter
22. Pilih `Dell` pada field Brand
23. Klik `[Apply]`
24. Verifikasi tabel memuat `Laptop Dell - 1`
25. Pilih `Ikea` pada field Brand
26. Klik ikon Filter
27. Verifikasi tabel tetap memuat `Laptop Dell - 1` dan tidak memuat `Kursi Kerja - 1`
28. Klik ikon Filter
29. Verifikasi field Brand hanya menampilkan chip `Dell`

### Menghapus chip dan menghapus centang opsi
30. Tampilkan Panel Filter All Assets dengan kondisi K1
31. Klik ikon Filter
32. Pilih `Dell` pada field Brand
33. Pilih `Epson` pada field Brand
34. Klik `✕` pada chip `Epson`
35. Verifikasi chip `Epson` hilang dari field Brand
36. Verifikasi opsi `Epson` tidak tercentang pada dropdown Brand
37. Klik `[Apply]`
38. Verifikasi tabel memuat `Laptop Dell - 1`
39. Verifikasi `Printer Laser - 1` tidak tampil di tabel
40. Hapus centang opsi `Dell` pada dropdown Brand
41. Verifikasi chip `Dell` hilang dari field Brand

### Pencarian di dalam dropdown dan sumber opsi kosong
42. Tampilkan Panel Filter All Assets dengan kondisi K1
43. Klik ikon Filter
44. Buka dropdown Brand
45. Verifikasi dropdown Brand memuat opsi `Dell`, `Epson`, dan `Ikea`
46. Ketik `Zzz` pada kotak cari dropdown Brand
47. Verifikasi dropdown Brand menampilkan `No results found`
48. Tampilkan Panel Filter All Assets dengan kondisi K2
49. Klik ikon Filter
50. Buka dropdown Brand
51. Verifikasi dropdown Brand menampilkan `No options available`

### Clear Field hanya mengosongkan panel
52. Tampilkan Panel Filter All Assets dengan kondisi K1
53. Klik ikon Filter
54. Pilih `Dell` pada field Brand
55. Klik `[Apply]`
56. Verifikasi tabel memuat `Laptop Dell - 1`
57. Klik `[Clear Field]`
58. Verifikasi field Brand kosong dan tabel masih tersaring pada `Laptop Dell - 1`
59. Klik `[Apply]`
60. Verifikasi tabel memuat `Laptop Dell - 1`, `Printer Laser - 1`, dan `Kursi Kerja - 1`
61. Verifikasi ikon Filter tidak lagi menampilkan indikator titik

### Memilih node Category menyertakan seluruh turunannya
62. Tampilkan Panel Filter All Assets dengan kondisi K1
63. Klik ikon Filter
64. Buka field Category
65. Pilih node `Elektronik` pada field Category
66. Verifikasi node `Laptop` dan `Printer` ikut terpilih
67. Klik `[Apply]`
68. Verifikasi tabel memuat `Laptop Dell - 1` dan `Printer Laser - 1`
69. Verifikasi `Kursi Kerja - 1` tidak tampil di tabel

### Chip yang melebihi lebar field menjadi +N more
70. Tampilkan Panel Filter All Assets dengan kondisi K3
71. Klik ikon Filter
72. Pilih seluruh opsi pada field Brand satu per satu
73. Verifikasi field Brand hanya menampilkan chip yang muat dan sisanya diringkas sebagai `+N more`, dengan N sama dengan jumlah opsi terpilih yang tidak tertampung
