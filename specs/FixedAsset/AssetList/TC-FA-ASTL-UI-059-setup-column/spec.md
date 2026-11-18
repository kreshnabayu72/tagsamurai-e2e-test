---
id: TC-FA-ASTL-UI-059-setup-column
title: "Mekanik Setup Column"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EC-43", "EB-FLT-6@tabel-all-assets", "EB-KOL-1@tabel-all-assets", "EB-KOL-3"]
smoke: []
dependsOn: []
trace:
  "EC-43": [76, 78, 79, 80, 81]
  "EB-FLT-6@tabel-all-assets": [71, 72, 73]
  "EB-KOL-1@tabel-all-assets": [3, 5, 6, 7, 8, 13, 15, 16, 21, 23, 28, 30, 37, 39, 41, 44, 48, 50, 52, 56, 58]
  "EB-KOL-3": [60, 61]
anchor: [66, 75]
coverage:
  web: automated
---
# Mekanik Setup Column

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Setup Column All Assets
- Data:
  - DU-059-1: Aset pertama: Name `Laptop Dell - 1`, Asset ID `AST-0101`, Brand `Dell`, Model / Type `Latitude 5440`, Status `Available`.
  - DU-059-2: Aset kedua: Name `Printer Laser - 1`, Asset ID `AST-0031`, Brand `Epson`, Model / Type `No Model`, Status `Not Paired Yet`.
- Kondisi:
  - K1: tabel memuat DU-059-1 dan DU-059-2 dengan konfigurasi kolom bawaan, dan konfigurasi tersimpan di akun user.
  - K2: konfigurasi kolom yang tersimpan di akun user menyembunyikan kolom Brand.
  - K3: konfigurasi kolom yang tersimpan di akun user hanya menampilkan kolom Name.
  - K4: tabel lain pada aplikasi memiliki konfigurasi tersimpan yang menyembunyikan kolom Name, sedangkan konfigurasi All Assets bawaan.
  - K5: konfigurasi tersimpan memuat kolom custom field `Nomor Seri` yang sudah dihapus, dan filter tersimpan memuat label `Prioritas` serta Category `Meja Lama` yang sudah dihapus.
  - K6: tabel memuat DU-059-1 dan DU-059-2, dan filter Brand `Dell` hanya menjawab DU-059-1.

## Test Steps

### Anatomi modal Setup Column
1. Tampilkan Setup Column All Assets dengan kondisi K1
2. Klik header kolom Actions `⋯`
3. Verifikasi panel cepat memuat butir `Setup Column...`
4. Klik `Setup Column...`
5. Verifikasi modal berjudul `Setup Column` dengan deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.`
6. Verifikasi modal memuat ikon tutup `✕`
7. Verifikasi footer modal memuat `[Reset to Default]` dan `[Save]`
8. Verifikasi footer modal tidak memuat tombol `[Cancel]`

### Sembunyikan kolom dan simpan
9. Tampilkan Setup Column All Assets dengan kondisi K1
10. Klik header kolom Actions `⋯`
11. Klik `Setup Column...`
12. Hapus centang kolom `Brand` pada modal
13. Verifikasi tabel di balik modal tidak menampilkan kolom Brand sebagai pratinjau
14. Klik `[Save]`
15. Verifikasi modal tertutup dan tabel tidak menampilkan kolom Brand
16. Verifikasi konfigurasi kolom tersimpan di akun user

### Menutup modal tanpa Save membuang perubahan
17. Tampilkan Setup Column All Assets dengan kondisi K1
18. Klik header kolom Actions `⋯`
19. Klik `Setup Column...`
20. Hapus centang kolom `Model / Type` pada modal
21. Verifikasi tabel di balik modal tidak menampilkan kolom Model / Type sebagai pratinjau
22. Klik `✕` pada modal
23. Verifikasi tabel menampilkan kolom Model / Type kembali

### Urutan kolom diubah dengan seret
24. Tampilkan Setup Column All Assets dengan kondisi K1
25. Klik header kolom Actions `⋯`
26. Klik `Setup Column...`
27. Seret kolom `Brand` ke atas kolom `Name` pada modal
28. Verifikasi tabel di balik modal menampilkan kolom Brand sebelum kolom Name
29. Klik `[Save]`
30. Verifikasi tabel menampilkan kolom Brand sebelum kolom Name

### Batas pin tiga kolom
31. Tampilkan Setup Column All Assets dengan kondisi K1
32. Klik header kolom Actions `⋯`
33. Klik `Setup Column...`
34. Klik pin pada kolom `Name`
35. Klik pin pada kolom `Asset ID`
36. Klik pin pada kolom `Brand`
37. Verifikasi ikon pin kolom `Status` disabled
38. Arahkan pointer ke ikon pin kolom `Status`
39. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
40. Klik pin pada kolom `Brand` untuk melepasnya
41. Verifikasi ikon pin kolom `Status` kembali aktif
42. Klik `[Save]`
43. Gulir tabel ke kanan
44. Verifikasi kolom `Name` dan `Asset ID` tetap terlihat

### Reset to Default dan pratinjau yang dibuang
45. Tampilkan Setup Column All Assets dengan kondisi K2
46. Klik header kolom Actions `⋯`
47. Klik `Setup Column...`
48. Verifikasi kolom `Brand` tidak tercentang pada modal
49. Klik `[Reset to Default]`
50. Verifikasi kolom `Brand` tercentang pada modal
51. Klik `✕` pada modal
52. Verifikasi tabel tetap tidak menampilkan kolom Brand

### Kolom terakhir tidak bisa disembunyikan
53. Tampilkan Setup Column All Assets dengan kondisi K3
54. Klik header kolom Actions `⋯`
55. Klik `Setup Column...`
56. Verifikasi kolom `Name` tercentang dan checkbox-nya disabled
57. Arahkan pointer ke checkbox kolom `Name`
58. Verifikasi tooltip `At least one column must remain visible.` tampil

### Konfigurasi satu tabel tidak mengubah tabel lain
59. Tampilkan Setup Column All Assets dengan kondisi K4
60. Verifikasi tabel All Assets menampilkan kolom Name
61. Verifikasi tabel All Assets menampilkan kolom Brand

### Menyembunyikan kolom tidak menghapus filternya
62. Tampilkan Setup Column All Assets dengan kondisi K6
63. Klik ikon Filter
64. Pilih `Dell` pada field Brand
65. Klik `[Apply]`
66. Verifikasi tabel memuat `Laptop Dell - 1`
67. Klik header kolom Actions `⋯`
68. Klik `Setup Column...`
69. Hapus centang kolom `Brand` pada modal
70. Klik `[Save]`
71. Verifikasi `Printer Laser - 1` tidak tampil di tabel
72. Verifikasi field Brand tetap ada pada panel Filter
73. Verifikasi filter Brand `Dell` tetap ter-Apply

### Rujukan yang sudah dihapus dibuang diam-diam
74. Tampilkan Setup Column All Assets dengan kondisi K5
75. Verifikasi baris `Laptop Dell - 1` tampil pada tabel
76. Verifikasi tabel tidak menampilkan kolom `Nomor Seri`
77. Klik ikon Filter
78. Verifikasi nilai filter label `Prioritas` tidak tampil pada panel Filter
79. Verifikasi nilai filter Category `Meja Lama` tidak tampil pada panel Filter
80. Verifikasi tidak ada pesan error
81. Verifikasi tidak ada toast yang tampil
