---
id: TC-FA-FATR-UI-073-overrides-bulk
title: "Tabel Overrides: seleksi baris dan menu bulk Delete"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#p56, §4.1#r380, §4.1#r381, §4.1#r382, §4.1#r383, §4.3#r19, §5#r5, §9.2#b159, §9.4.2#r128, §9.4.2#r129, §9.5#r15, EB-TBL-5@menu-bulk-delete, EB-BLK-1@tabel-overrides, EB-BLK-4, EB-FB-1@delete-override, EB-BLK-2@tabel-overrides]
smoke: []
dependsOn: []
trace:
  §4.1#p56: [3, 7, 8, 12, 13, 26, 27, 29, 32]
  §4.1#r380: 56
  §4.1#r381: [62, 64]
  §4.1#r382: 66
  §4.1#r383: [7, 10, 60]
  §4.3#r19: [7, 12]
  §5#r5: [12, 13]
  §9.2#b159: [62, 64, 69, 70]
  §9.4.2#r128: 62
  §9.4.2#r129: 66
  §9.5#r15: 4
  EB-TBL-5@menu-bulk-delete: [62, 64]
  EB-BLK-1@tabel-overrides: [7, 10, 16, 18, 19, 21, 22, 26, 37, 39, 41, 47, 51]
  EB-BLK-4: [76, 77, 83, 84]
  EB-FB-1@delete-override: [76, 83]
  EB-BLK-2@tabel-overrides: [8, 26, 27, 29]
anchor: [2, 68]
coverage:
  web: automated
---

# Tabel Overrides: seleksi baris dan menu bulk Delete

## Prerequisites
- Aktor: Manage asset & TAG (Read + Update) pada Group `Proyek Karawang`. K5 memakai aktor Read Only.
- Layar awal: Settings > Transaction Settings, bagian `Overrides` pada Category dan transaksi terpilih.
- Komponen: Tabel Overrides
- Data:
  - DU-073-1: 12 override (volume) di dalam cakupan Group aktor, Scope `Group`, Target `Workshop {n}`, Overridden `Max duration (30 days)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-15 14:05` untuk `Workshop 1`, lalu mundur satu menit untuk tiap nomor berikutnya (`Workshop 12` pada `2026-06-15 13:54`).
  - DU-073-2: override di luar cakupan Group aktor, Scope `Group`, Target `Proyek Bekasi`, Overridden `Auto-approve (OFF)`, Category `Vehicle > Pool car`, Created By `Siti Nurbaya`, Created At `2026-06-20 10:00`.
  - DU-073-3: override di luar cakupan Group aktor, Scope `Group`, Target `Proyek Cikarang`, Overridden `Max extensions (2)`, Category `Machinery`, Created By `Alexander Graham Bell`, Created At `2026-06-19 13:10`.
- Kondisi:
  - K1: tabel berisi 14 baris dengan urutan bawaan Created At terbaru lebih dulu: DU-073-2 (`2026-06-20 10:00`), DU-073-3 (`2026-06-19 13:10`), lalu DU-073-1 (Target `Workshop 1` sampai `Workshop 12`, `2026-06-15 14:05` mundur ke `2026-06-15 13:54`); ukuran halaman bawaan 10, sehingga halaman 1 memuat DU-073-2, DU-073-3, dan `Workshop 1` sampai `Workshop 8`, dan halaman 2 memuat `Workshop 9` sampai `Workshop 12`.
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

### Aktor Read Only tanpa kolom checkbox dan bar bulk
67. Tampilkan Tabel Overrides dengan kondisi K5
68. Verifikasi tabel menampilkan baris Target `Workshop 1`
69. Verifikasi tidak ada kolom checkbox seleksi pada tabel, baik pada baris maupun pada header[^drift-1]
70. Verifikasi bar bulk dan tombol `[Bulk Action]` tidak tampil pada toolbar tabel[^drift-1]

### Bulk Delete gagal karena error server
71. Tampilkan Tabel Overrides dengan kondisi K3
72. Centang baris `Workshop 1`
73. Klik `[Bulk Action]`
74. Klik `Delete`
75. Klik `[Delete]` pada dialog
76. Verifikasi toast error `Error, failed to delete override.` tampil
77. Verifikasi bar bulk tetap menampilkan `1 Override selected`

### Bulk Delete tanpa respons
78. Tampilkan Tabel Overrides dengan kondisi K4
79. Centang baris `Workshop 1`
80. Klik `[Bulk Action]`
81. Klik `Delete`
82. Klik `[Delete]` pada dialog
83. Verifikasi toast error `Connection problem. Please try again.` tampil
84. Verifikasi bar bulk tetap menampilkan `1 Override selected`

[^drift-1]: Drift PRD vs foundation. PRD §4.8 (UI Visibility per Role, baris Delete untuk baris dan bulk): Read Only `Disabled 🔖` dengan tooltip alasan di luar cakupan role; PRD §4.1: tabel punya checkbox per baris dan checkbox header untuk bulk delete. Foundation `entity-isolation.md` §18.4 (Aturan kolom 3): kolom checkbox bulk select Hidden untuk aktor yang tidak punya write access sama sekali (mis. Read Only), dan bulk action bar Hidden total, bukan hanya checkbox-nya. Diasersi: foundation, karena UI visibility per capability adalah pola bersama (SB-4).
