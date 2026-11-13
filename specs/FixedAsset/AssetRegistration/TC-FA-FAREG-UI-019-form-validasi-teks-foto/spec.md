---
id: TC-FA-FAREG-UI-019-form-validasi-teks-foto
title: "Form Register Asset: batas karakter, karakter Alias Name, dan format Photo"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FAREG-LOGIC-01s", "V-REG-18", "§9.9#r8", "§9.9#r13", "§9.9#r14", "EB-FRM-4@alias-name", "EB-FRM-4@damage-note", "EB-FRM-8@edit-draft"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-01s": [7, 9, 21, 29, 35, 40, 46, 52, 63, 64, 65, 71, 74, 80]
  "V-REG-18": [7, 9, 12, 15, 27, 29, 32]
  "§9.9#r8": [7, 9, 18]
  "§9.9#r13": [52, 55, 61, 63]
  "§9.9#r14": [27, 29, 32, 35]
  "EB-FRM-4@alias-name": [27, 29]
  "EB-FRM-4@damage-note": [7, 9]
  "EB-FRM-8@edit-draft": [9, 29]
anchor: [6, 11, 14, 17, 20, 26, 31, 34, 39, 51, 54, 60, 70, 73, 79]
coverage:
  web: automated
---

# Form Register Asset: batas karakter, karakter Alias Name, dan format Photo

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-019-1: Item `Laptop Dell Latitude 5440` dengan Quantity `3`; aset `Laptop Dell Latitude 5440 - 1`, `Laptop Dell Latitude 5440 - 2`, dan `Laptop Dell Latitude 5440 - 3`, Condition `Normal`.
- Kondisi:
  - K1: form `Edit` draft tersimpan dengan Item DU-019-1; tab `Asset` memuat aset itu.

## Test Steps
### Damage note: batas 120 karakter diterima dan 121 ditolak
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Klik tab `Asset`
3. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
4. Ganti sel `Condition` pada `Laptop Dell Latitude 5440 - 1` menjadi `Damaged`
5. Ganti isi `Damage note` dengan `Layar retak di pojok kanan atas, engsel kiri longgar, dan baterai menggembung sehingga aset belum layak dipakai. Kode 01` (120 karakter)
6. Verifikasi `Damage note` menampilkan `Layar retak di pojok kanan atas, engsel kiri longgar, dan baterai menggembung sehingga aset belum layak dipakai. Kode 01`
7. Verifikasi tidak ada pesan error di bawah `Damage note`
8. Ganti isi `Damage note` dengan `Layar retak di pojok kanan atas, engsel kiri longgar, dan baterai menggembung sehingga aset belum layak dipakai. Kode 012` (121 karakter)
9. Verifikasi pesan `Max. 120 characters` tampil di bawah `Damage note` pada form Edit
10. Ganti isi `Damage note` dengan `Layar  retak  di  pojok  kanan  atas,  engsel  kiri  longgar,  baterai  menggembung,  aset  belum  layak  dipakai.  Kode` (120 karakter)
11. Verifikasi `Damage note` menampilkan `Layar  retak  di  pojok  kanan  atas,  engsel  kiri  longgar,  baterai  menggembung,  aset  belum  layak  dipakai.  Kode`
12. Verifikasi tidak ada pesan error di bawah `Damage note`
13. Ganti isi `Damage note` dengan `Kantor Cabang Medan Élan 𝒜 layar retak, engsel kiri longgar, dan baterai menggembung sehingga aset belum layak dipakai.0` (120 karakter)
14. Verifikasi `Damage note` menampilkan `Kantor Cabang Medan Élan 𝒜 layar retak, engsel kiri longgar, dan baterai menggembung sehingga aset belum layak dipakai.0`
15. Verifikasi tidak ada pesan error di bawah `Damage note`
16. Ganti isi `Damage note` dengan `R` (1 karakter)
17. Verifikasi `Damage note` menampilkan `R`
18. Verifikasi tidak ada pesan error di bawah `Damage note`
19. Ganti isi `Damage note` dengan `Retak <layar> & "bodi" 100% #1 @gudang` (38 karakter)
20. Verifikasi `Damage note` menampilkan `Retak <layar> & "bodi" 100% #1 @gudang`
21. Verifikasi tidak ada pesan error di bawah `Damage note`

### Alias Name: batas 120 karakter, emoji diblok, Alias kosong diabaikan, dan jumlah tidak dibatasi
22. Tampilkan Halaman `Register Asset` dengan kondisi K1
23. Klik tab `Asset`
24. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
25. Ganti isi input Alias Name dengan `Laptop Direksi Lantai Tiga untuk Rapat Dewan Komisaris dan Tamu Kehormatan Kantor Pusat Jakarta Selatan. Kode 0123456789` (120 karakter)
26. Verifikasi input Alias Name menampilkan `Laptop Direksi Lantai Tiga untuk Rapat Dewan Komisaris dan Tamu Kehormatan Kantor Pusat Jakarta Selatan. Kode 0123456789`
27. Verifikasi tidak ada pesan error di bawah input Alias Name
28. Ganti isi input Alias Name dengan `Laptop Direksi Lantai Tiga untuk Rapat Dewan Komisaris dan Tamu Kehormatan Kantor Pusat Jakarta Selatan. Kode 01234567890` (121 karakter)
29. Verifikasi pesan `Max. 120 characters` tampil di bawah input Alias Name pada form Edit
30. Ganti isi input Alias Name dengan `Laptop  Direksi  Lantai  Tiga  untuk  Rapat  Dewan  Komisaris  dan  Tamu  Kehormatan  Kantor  Pusat  Jakarta.  Kode 0123` (120 karakter)
31. Verifikasi input Alias Name menampilkan `Laptop  Direksi  Lantai  Tiga  untuk  Rapat  Dewan  Komisaris  dan  Tamu  Kehormatan  Kantor  Pusat  Jakarta.  Kode 0123`
32. Verifikasi tidak ada pesan error di bawah input Alias Name yang berspasi ganda di tengah
33. Ketik Alias Name `Laptop Panel Rapat 😊`
34. Verifikasi input Alias Name menampilkan `Laptop Panel Rapat`
35. Verifikasi input Alias Name tidak memuat emoji `😊`
36. Klik `+ Add alias name`
37. Ketik Alias Name `Notebook Direksi B` pada input Alias Name kedua
38. Kosongkan input Alias Name kedua
39. Verifikasi input Alias Name pertama masih tampil
40. Verifikasi input Alias Name kedua tidak tampil lagi
41. Klik `+ Add alias name`
42. Klik `+ Add alias name`
43. Klik `+ Add alias name`
44. Klik `+ Add alias name`
45. Klik `+ Add alias name`
46. Verifikasi tombol `+ Add alias name` masih tampil sesudah enam input Alias Name

### Photo: format PNG dan JPG diterima
47. Tampilkan Halaman `Register Asset` dengan kondisi K1
48. Klik tab `Asset`
49. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
50. Pilih berkas `foto-aset.png` pada area `Add photo`
51. Verifikasi foto `foto-aset.png` tampil pada aset `Laptop Dell Latitude 5440 - 1`
52. Verifikasi tidak ada pesan error format pada bagian Photo
53. Pilih berkas `foto-aset.jpg` pada area `Add photo`
54. Verifikasi foto `foto-aset.jpg` tampil pada aset `Laptop Dell Latitude 5440 - 1`
55. Verifikasi tidak ada pesan error format pada bagian Photo setelah `foto-aset.jpg`

### Photo: format JPEG diterima dan format tidak didukung ditolak
56. Tampilkan Halaman `Register Asset` dengan kondisi K1
57. Klik tab `Asset`
58. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
59. Pilih berkas `foto-aset.jpeg` pada area `Add photo`
60. Verifikasi foto `foto-aset.jpeg` tampil pada aset `Laptop Dell Latitude 5440 - 1`
61. Verifikasi tidak ada pesan error format pada bagian Photo setelah `foto-aset.jpeg`
62. Pilih berkas `dokumen-aset.pdf` pada area `Add photo`
63. Verifikasi pesan `Unsupported format. Please upload JPG, PNG, or JPEG.` tampil pada bagian Photo
64. Verifikasi foto `dokumen-aset.pdf` tidak tampil pada aset `Laptop Dell Latitude 5440 - 1`
65. Verifikasi foto `foto-aset.jpeg` masih tampil pada aset `Laptop Dell Latitude 5440 - 1`

### Photo: ukuran di bawah dan tepat 1 MB diterima tanpa pesan error ukuran
66. Tampilkan Halaman `Register Asset` dengan kondisi K1
67. Klik tab `Asset`
68. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
69. Pilih berkas `foto-kecil.jpg` (500 KB) pada area `Add photo`
70. Verifikasi foto `foto-kecil.jpg` tampil pada aset `Laptop Dell Latitude 5440 - 1`
71. Verifikasi tidak ada pesan error ukuran pada bagian Photo setelah `foto-kecil.jpg`
72. Pilih berkas `foto-satu-mb.jpg` (1 MB) pada area `Add photo`
73. Verifikasi foto `foto-satu-mb.jpg` tampil pada aset `Laptop Dell Latitude 5440 - 1`
74. Verifikasi tidak ada pesan error ukuran pada bagian Photo setelah `foto-satu-mb.jpg`

### Photo: ukuran di atas 1 MB diperkecil otomatis tanpa pesan error ukuran
75. Tampilkan Halaman `Register Asset` dengan kondisi K1
76. Klik tab `Asset`
77. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
78. Pilih berkas `foto-besar.jpg` (3 MB) pada area `Add photo`
79. Verifikasi foto `foto-besar.jpg` tampil pada aset `Laptop Dell Latitude 5440 - 1`
80. Verifikasi tidak ada pesan error ukuran pada bagian Photo setelah `foto-besar.jpg`
