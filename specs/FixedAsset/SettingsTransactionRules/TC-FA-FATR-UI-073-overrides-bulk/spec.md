---
id: TC-FA-FATR-UI-073-overrides-bulk
title: "Tabel Overrides: seleksi baris dan menu bulk Delete"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#p49, §4.1#r354, §4.1#r355, §4.1#r356, §4.1#r357, §4.3#r20, §5#r5, §9.2#b159, §9.4.2#r120, §9.4.2#r121, §9.5#r15, EB-TBL-5@menu-bulk-delete, EB-BLK-1@tabel-overrides, EB-BLK-4]
smoke: []
dependsOn: []
trace:
  §4.1#p49: [3, 7, 8, 12, 13, 26, 27, 29, 32]
  §4.1#r354: 56
  §4.1#r355: [62, 64]
  §4.1#r356: 66
  §4.1#r357: [7, 10, 60]
  §4.3#r20: [7, 12]
  §5#r5: [12, 13]
  §9.2#b159: [62, 64, 70, 72]
  §9.4.2#r120: 62
  §9.4.2#r121: 66
  §9.5#r15: 4
  EB-TBL-5@menu-bulk-delete: [64, 72]
  EB-BLK-1@tabel-overrides: [7, 10, 16, 18, 19, 21, 22, 26, 37, 39, 41, 47, 51]
  EB-BLK-4: [78, 79, 85, 86]
anchor: [2]
coverage:
  web: automated
---

# Tabel Overrides: seleksi baris dan menu bulk Delete

## Prerequisites
- Aktor: Manage asset & TAG (Read + Update) pada Group `Proyek Karawang`. K5 memakai aktor Read Only.
- Layar awal: Settings > Transaction Settings, bagian `Overrides` pada Category dan transaksi terpilih.
- Komponen: Tabel Overrides
- Data:
  - DU-073-1: 12 override (volume) di dalam cakupan Group aktor, Scope `Group`, Target `Workshop {n}`, Overridden `Max duration (30 days)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-15 14:05`.
  - DU-073-2: override di luar cakupan Group aktor, Scope `Group`, Target `Proyek Bekasi`, Overridden `Auto-approve (OFF)`, Category `Vehicle > Pool car`, Created By `Siti Nurbaya`, Created At `2026-06-03 10:00`.
  - DU-073-3: override di luar cakupan Group aktor, Scope `Group`, Target `Proyek Cikarang`, Overridden `Max extensions (2)`, Category `Machinery`, Created By `Alexander Graham Bell`, Created At `2026-06-02 13:10`.
- Kondisi:
  - K1: tabel berisi 14 baris dengan urutan DU-073-2, DU-073-3, lalu DU-073-1 (Target `Workshop 1` sampai `Workshop 12`); ukuran halaman bawaan 10, sehingga halaman 1 memuat DU-073-2, DU-073-3, dan `Workshop 1` sampai `Workshop 8`, dan halaman 2 memuat `Workshop 9` sampai `Workshop 12`.
  - K2: sama dengan K1; permintaan Delete diterima server.
  - K3: sama dengan K1; permintaan Delete gagal karena error server.
  - K4: sama dengan K1; permintaan Delete tidak mendapat respons (timeout).
  - K5: sama dengan K1; aktor Read Only.

## Test Steps

### Default tanpa seleksi
1. Tampilkan Tabel Overrides dengan kondisi K1
2. Verifikasi tabel menampilkan baris Target `Proyek Bekasi`
3. Verifikasi setiap baris tabel memiliki checkbox dan header tabel memiliki checkbox
4. Verifikasi tidak ada baris yang tercentang dan bar bulk tidak tampil

### Bar bulk, counter tunggal dan jamak, dan aksi Delete sebagai satu-satunya aksi
5. Tampilkan Tabel Overrides dengan kondisi K1
6. Centang baris `Workshop 1`
7. Verifikasi bar bulk menampilkan `1 Override selected`
8. Verifikasi bar bulk memuat tombol `Select All (14 records)`
9. Centang baris `Workshop 2`
10. Verifikasi bar bulk menampilkan `2 Overrides selected`
11. Klik `[Bulk Action]`
12. Verifikasi menu bulk hanya memuat satu aksi, `Delete`
13. Verifikasi menu bulk tidak memuat `Edit`

### Checkbox header, indeterminate, dan seleksi bertahan saat pindah halaman
14. Tampilkan Tabel Overrides dengan kondisi K1
15. Centang baris `Workshop 1`
16. Verifikasi checkbox header berstatus indeterminate
17. Klik checkbox header
18. Verifikasi seluruh baris pada halaman 1 tercentang dan checkbox header tercentang
19. Verifikasi bar bulk menampilkan `10 Overrides selected`
20. Klik halaman `2`
21. Verifikasi bar bulk tetap menampilkan `10 Overrides selected` pada halaman 2
22. Verifikasi checkbox header tidak tercentang pada halaman 2

### Select All dan Unselect All
23. Tampilkan Tabel Overrides dengan kondisi K1
24. Centang baris `Workshop 1`
25. Klik `[Select All (14 records)]`
26. Verifikasi bar bulk menampilkan `14 Overrides selected`
27. Verifikasi bar bulk memuat tombol `Unselect All (14 records)`
28. Hilangkan centang baris `Workshop 1`
29. Verifikasi bar bulk kembali memuat tombol `Select All (14 records)`
30. Klik `[Select All (14 records)]`
31. Klik `[Unselect All (14 records)]`
32. Verifikasi bar bulk tidak tampil dan tidak ada baris yang tercentang

### Ikon × membersihkan seluruh seleksi
33. Tampilkan Tabel Overrides dengan kondisi K1
34. Centang baris `Workshop 1`
35. Klik halaman `2`
36. Centang baris `Workshop 9`
37. Verifikasi bar bulk menampilkan `2 Overrides selected` dari dua halaman
38. Klik `×` pada bar bulk
39. Verifikasi bar bulk tidak tampil
40. Klik halaman `1`
41. Verifikasi tidak ada baris yang tercentang pada halaman 1

### Cancel dialog tidak memproses dan seleksi bersih sesudah aksi selesai
42. Tampilkan Tabel Overrides dengan kondisi K2
43. Centang baris `Workshop 1`
44. Klik `[Bulk Action]`
45. Klik `Delete`
46. Klik `[Cancel]` pada dialog
47. Verifikasi bar bulk tetap menampilkan `1 Override selected` dan permintaan Delete tidak dikirim
48. Klik `[Bulk Action]`
49. Klik `Delete`
50. Klik `[Delete]` pada dialog
51. Verifikasi bar bulk tidak tampil dan tidak ada baris yang tercentang sesudah aksi selesai

### Seleksi campuran: menu bulk Delete tetap aktif
52. Tampilkan Tabel Overrides dengan kondisi K1
53. Centang baris `Proyek Bekasi`
54. Centang baris `Workshop 1`
55. Klik `[Bulk Action]`
56. Verifikasi `Delete` pada menu bulk aktif

### Tidak ada baris terpilih yang boleh dihapus
57. Tampilkan Tabel Overrides dengan kondisi K1
58. Centang baris `Proyek Bekasi`
59. Centang baris `Proyek Cikarang`
60. Verifikasi bar bulk menampilkan `2 Overrides selected`
61. Klik `[Bulk Action]`
62. Verifikasi `Delete` pada menu bulk disabled
63. Arahkan kursor ke `Delete` pada menu bulk
64. Verifikasi alasan `This override is outside your scope.` tersampaikan pada `Delete`
65. Klik `Delete` pada menu bulk
66. Verifikasi tidak ada dialog yang tampil

### Aktor tanpa hak menghapus
67. Tampilkan Tabel Overrides dengan kondisi K5
68. Centang baris `Workshop 1`
69. Klik `[Bulk Action]`
70. Verifikasi `Delete` pada menu bulk disabled
71. Arahkan kursor ke `Delete` pada menu bulk
72. Verifikasi alasan `This override is outside your scope.` tersampaikan pada `Delete`

### Bulk Delete gagal karena error server
73. Tampilkan Tabel Overrides dengan kondisi K3
74. Centang baris `Workshop 1`
75. Klik `[Bulk Action]`
76. Klik `Delete`
77. Klik `[Delete]` pada dialog
78. Verifikasi toast error `Error, failed to delete override.` tampil
79. Verifikasi bar bulk tetap menampilkan `1 Override selected`

### Bulk Delete tanpa respons
80. Tampilkan Tabel Overrides dengan kondisi K4
81. Centang baris `Workshop 1`
82. Klik `[Bulk Action]`
83. Klik `Delete`
84. Klik `[Delete]` pada dialog
85. Verifikasi toast error `Connection problem. Please try again.` tampil
86. Verifikasi bar bulk tetap menampilkan `1 Override selected`
