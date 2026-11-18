---
id: TC-FA-ASTL-UI-060-bar-bulk
title: "Bar Bulk dan seleksi baris"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["S-47", "EC-16", "§4.4#b3", "§4.4#b5", "§4.4#b6", "§5#r5", "EB-BLK-1@tabel-all-assets", "EB-BLK-4", "EB-BLK-6"]
smoke: []
dependsOn: []
trace:
  "S-47": 5
  "EC-16": [54, 56, 61, 62]
  "§4.4#b3": 8
  "§4.4#b5": [14, 16, 18, 22]
  "§4.4#b6": 33
  "§5#r5": [5, 53]
  "EB-BLK-1@tabel-all-assets": [3, 5, 6, 9, 11, 28, 33]
  "EB-BLK-4": [40, 41, 48]
  "EB-BLK-6": [51, 53, 54, 56, 57, 61, 62, 63]
anchor: [2]
coverage:
  web: automated
---
# Bar Bulk dan seleksi baris

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Bar Bulk All Assets
- Data:
  - DU-060-1: Tiga aset: Name `Aset Seleksi 1` sampai `Aset Seleksi 3`, Status `Available`.
  - DU-060-2: Pengaturan: Selection Limit `5`.
  - DU-060-3: Enam aset: Name `Aset Batas 1` sampai `Aset Batas 6`, Status `Available`.
  - DU-060-4: Dua belas aset hasil Search: Name `Aset Tersaring 1` sampai `Aset Tersaring 12`, Status `Available`.
  - DU-060-5: Dua belas aset untuk dua halaman: Name `Aset Halaman 1` sampai `Aset Halaman 12`, Status `Available`, ukuran halaman `10`.
  - DU-060-6: Label manual: Label `Prioritas`.
- Kondisi:
  - K1: tabel memuat DU-060-1, Selection Limit bernilai `1000`, dan simpan Add Label berhasil.
  - K2: Selection Limit bernilai `5` (DU-060-2) dan tabel memuat DU-060-3.
  - K3: Selection Limit bernilai `5` (DU-060-2), dan Search menghasilkan DU-060-4 sebanyak 12 baris.
  - K4: Selection Limit bernilai `1000` dan tabel memuat DU-060-5.
  - K5: tabel memuat DU-060-1, Selection Limit bernilai `1000`, dan simpan Add Label gagal karena timeout.
  - K6: tabel memuat DU-060-1, Selection Limit bernilai `1000`, dan simpan Add Label gagal karena error server.

## Test Steps

### Bar Bulk, penghitung, dan header checkbox
1. Tampilkan Bar Bulk All Assets dengan kondisi K1
2. Verifikasi tabel memuat `Aset Seleksi 1`, `Aset Seleksi 2`, dan `Aset Seleksi 3`
3. Verifikasi bar Bulk belum tampil
4. Centang baris `Aset Seleksi 1`
5. Verifikasi bar Bulk tampil dengan tombol `Bulk Action`, teks `1 asset selected`, tombol `Select All (3 records)`, dan ikon `×`
6. Verifikasi checkbox header berstatus indeterminate
7. Klik checkbox header
8. Verifikasi `Aset Seleksi 1`, `Aset Seleksi 2`, dan `Aset Seleksi 3` tercentang
9. Verifikasi teks bar Bulk menjadi `3 assets selected` dan tombol menjadi `Unselect All`
10. Klik `×` pada bar Bulk
11. Verifikasi bar Bulk hilang dan tidak ada baris yang tercentang

### Seleksi bertahan saat pindah halaman, sort, dan filter
12. Tampilkan Bar Bulk All Assets dengan kondisi K4
13. Centang baris `Aset Halaman 1`
14. Verifikasi teks bar Bulk `1 asset selected`
15. Klik halaman 2
16. Verifikasi teks bar Bulk tetap `1 asset selected`
17. Klik header kolom Name
18. Verifikasi teks bar Bulk tetap `1 asset selected`
19. Klik ikon Filter
20. Pilih `Available` pada field Status
21. Klik `[Apply]`
22. Verifikasi teks bar Bulk tetap `1 asset selected`

### Batal pada dialog tidak mereset dan aksi tersimpan mereset seleksi
23. Tampilkan Bar Bulk All Assets dengan kondisi K1
24. Centang baris `Aset Seleksi 1`
25. Klik `Bulk Action`
26. Klik `Add Label`
27. Klik `[Cancel]` pada dialog Add Label
28. Verifikasi teks bar Bulk tetap `1 asset selected`
29. Klik `Bulk Action`
30. Klik `Add Label`
31. Pilih label `Prioritas`
32. Klik `[Apply]` pada dialog Add Label
33. Verifikasi bar Bulk hilang dan tidak ada baris yang tercentang

### Bulk gagal karena timeout atau error server
34. Tampilkan Bar Bulk All Assets dengan kondisi K5
35. Centang baris `Aset Seleksi 1`
36. Klik `Bulk Action`
37. Klik `Add Label`
38. Pilih label `Prioritas`
39. Klik `[Apply]` pada dialog Add Label
40. Verifikasi toast `Connection problem. Please try again.` tampil
41. Verifikasi bar Bulk dan seleksi `1 asset selected` dipertahankan

### Bulk gagal karena error server
42. Tampilkan Bar Bulk All Assets dengan kondisi K6
43. Centang baris `Aset Seleksi 1`
44. Klik `Bulk Action`
45. Klik `Add Label`
46. Pilih label `Prioritas`
47. Klik `[Apply]` pada dialog Add Label
48. Verifikasi toast error tampil dan bar Bulk dengan seleksi `1 asset selected` dipertahankan

### Seleksi dibatasi Selection Limit
49. Tampilkan Bar Bulk All Assets dengan kondisi K2
50. Centang baris `Aset Batas 1`, `Aset Batas 2`, `Aset Batas 3`, dan `Aset Batas 4`
51. Verifikasi teks bar Bulk `4 assets selected` dan checkbox `Aset Batas 5` masih dapat dicentang
52. Centang baris `Aset Batas 5`
53. Verifikasi teks bar Bulk `5 assets selected`
54. Verifikasi checkbox baris `Aset Batas 6` disabled
55. Arahkan pointer ke checkbox baris `Aset Batas 6`
56. Verifikasi tooltip `You've reached the maximum selection of 5 rows.` tampil
57. Verifikasi `Aset Batas 1` sampai `Aset Batas 5` tetap tercentang

### Select All dipotong ke batas dengan toast
58. Tampilkan Bar Bulk All Assets dengan kondisi K3
59. Centang baris `Aset Tersaring 1`
60. Klik `Select All (12 records)`
61. Verifikasi teks bar Bulk `5 assets selected`
62. Verifikasi toast `Error, only the first 5 of 12 rows were selected. Narrow your filter to include the rest.` tampil
63. Verifikasi bar Bulk tetap tampil
