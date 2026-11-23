---
id: TC-FA-FAFM-UI-081-tabel-files-filter-panel
title: "Tabel Files: mekanik Filter Panel"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["TBL-03d", "EB-SRC-6@filter-group-tabel-files", "EB-FLT-2@tabel-files", "EB-FLT-6@tabel-files"]
smoke: []
dependsOn: []
trace:
  "TBL-03d": [2, 4, 5, 6, 33, 34, 35, 36, 37, 38, 43, 44, 46, 47, 48, 49, 51, 52]
  "EB-SRC-6@filter-group-tabel-files": [88, 89, 90, 92, 93, 94, 96, 97, 98]
  "EB-FLT-2@tabel-files": [8, 10, 11, 13, 14, 18, 19, 21, 22, 27, 28, 30, 31, 33, 34, 35, 36, 37, 56, 57, 61, 62, 63, 65, 69]
  "EB-FLT-6@tabel-files": [74, 75, 78, 79, 80, 81, 82, 83, 84]
anchor: []
coverage:
  web: automated
---

# Tabel Files: mekanik Filter Panel

## Prerequisites
- Aktor: Total Control.
- Layar awal: Tabel File Manager tab Files.
- Komponen: Tabel File Manager tab Files.
- Data:
  - DU-081-1: `laptop-front.jpg`, JPG, Source Asset Photo, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `820.4 KB`, Uploaded By `Budi S`, Upload Date `02/11/26 14:30`.
  - DU-081-2: `loading-dock.jpeg`, JPEG, Source Asset Photo, Asset `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Group `Head Office`, Size `1.1 MB`, Uploaded By `Rina A`, Upload Date `04/11/26 08:15`.
  - DU-081-3: `monitor-lg-front.png`, PNG, Source Asset Photo, Asset `Monitor LG 24 - 7`, Asset ID `MON-2026-0007`, Group `Branch Bandung`, Size `640.0 KB`, Uploaded By `Dodi P`, Upload Date `05/11/26 09:00`.
  - DU-081-4: `printer-hp-side.jpg`, JPG, Source Asset Photo, Asset `Printer HP M404 - 1`, Asset ID `PRN-2026-0001`, Group `Branch Bandung`, Size `700.0 KB`, Uploaded By `Rina A`, Upload Date `06/11/26 10:30`.
  - DU-081-5: `scanner-epson-top.png`, PNG, Source Asset Photo, Asset `Scanner Epson DS-530 - 3`, Asset ID `SCN-2026-0003`, Group `Branch Surabaya`, Size `512.0 KB`, Uploaded By `Budi S`, Upload Date `07/11/26 11:00`.
  - DU-081-6: `router-cisco-front.jpeg`, JPEG, Source Asset Photo, Asset `Router Cisco ISR 4331 - 2`, Asset ID `RTR-2026-0002`, Group `Branch Surabaya`, Size `905.0 KB`, Uploaded By `Dodi P`, Upload Date `08/11/26 13:45`.
  - DU-081-7: akun tanpa satu pun file aktif.
- Kondisi:
  - K1: tab `Asset Photo` aktif; tabel berisi DU-081-1 sampai DU-081-6; Filter Panel belum pernah dibuka dan belum ada filter ter-Apply; opsi filter diisi dari nilai pada tabel; tree Group berisi `Head Office`, `Branch Bandung`, dan `Branch Surabaya` sebagai tiga node sejajar, tanpa hubungan induk dan anak.
  - K2: tab `Asset Photo` aktif; tabel kosong sesuai DU-081-7; Filter Panel belum pernah dibuka.

## Test Steps

### Membuka Filter Panel dan menutupnya tanpa Apply
1. Tampilkan Tabel File Manager tab Files dengan kondisi K1
2. Verifikasi ikon Filter tampil
3. Klik ikon Filter
4. Verifikasi Filter Panel terbuka dengan field `File Format`
5. Verifikasi tombol `[Clear Field]` tampil
6. Verifikasi tombol `[Apply]` tampil
7. Pilih `JPG` pada field `File Format`
8. Verifikasi chip `JPG` tampil pada field `File Format`
9. Klik ikon Filter untuk menutup panel
10. Verifikasi tabel tetap memuat baris `laptop-front.jpg` setelah panel ditutup
11. Verifikasi baris `monitor-lg-front.png` tampil
12. Klik ikon Filter untuk membuka panel kembali
13. Verifikasi placeholder `All formats` tampil pada field `File Format`
14. Verifikasi indikator filter aktif tidak tampil pada ikon Filter

### Uncheck opsi pada dropdown
15. Tampilkan Tabel File Manager tab Files dengan kondisi K1
16. Klik ikon Filter
17. Pilih `JPG` dan `PNG` pada field `File Format`
18. Verifikasi chip `JPG` tampil pada field `File Format`
19. Verifikasi chip `PNG` tampil pada field `File Format`
20. Hapus centang opsi `PNG` pada dropdown field `File Format`
21. Verifikasi chip `JPG` tetap tampil pada field `File Format`
22. Verifikasi chip `PNG` tidak tampil pada field `File Format`

### Hapus chip lalu Apply menyaring dengan opsi tersisa
23. Tampilkan Tabel File Manager tab Files dengan kondisi K1
24. Klik ikon Filter
25. Pilih `JPG` dan `PNG` pada field `File Format`
26. Klik ✕ pada chip `PNG` di field `File Format`
27. Verifikasi chip `JPG` tetap tampil pada field `File Format`
28. Verifikasi chip `PNG` tidak tampil pada field `File Format`
29. Buka dropdown field `File Format`
30. Verifikasi opsi `JPG` tercentang
31. Verifikasi opsi `PNG` tidak tercentang
32. Klik `[Apply]`
33. Verifikasi baris `laptop-front.jpg` tampil setelah `[Apply]`
34. Verifikasi baris `printer-hp-side.jpg` tampil
35. Verifikasi baris `monitor-lg-front.png` tidak tampil
36. Verifikasi baris `loading-dock.jpeg` tidak tampil
37. Verifikasi indikator filter aktif tampil pada ikon Filter
38. Verifikasi Filter Panel tetap tampil setelah `[Apply]`

### Clear Field mengosongkan field tanpa mengubah tabel
39. Tampilkan Tabel File Manager tab Files dengan kondisi K1
40. Klik ikon Filter
41. Pilih `JPG` pada field `File Format`
42. Klik `[Apply]`
43. Verifikasi hasil `[Apply]` memuat baris `laptop-front.jpg`
44. Verifikasi baris `monitor-lg-front.png` tidak tampil
45. Klik `[Clear Field]`
46. Verifikasi placeholder `All formats` tampil pada field `File Format`
47. Verifikasi Filter Panel tetap tampil setelah `[Clear Field]`
48. Verifikasi baris `laptop-front.jpg` masih tampil
49. Verifikasi baris `monitor-lg-front.png` masih tidak tampil
50. Klik `[Apply]`
51. Verifikasi baris `monitor-lg-front.png` tampil
52. Verifikasi indikator filter aktif tidak tampil pada ikon Filter

### Chip meluap diringkas menjadi +N more
53. Tampilkan Tabel File Manager tab Files dengan kondisi K1
54. Klik ikon Filter
55. Pilih `Laptop Dell Latitude 5420`, `Monitor LG 24`, `Printer HP M404`, `Scanner Epson DS-530`, dan `Router Cisco ISR 4331` pada field `Asset`
56. Verifikasi chip ringkasan `+N more` tampil pada field `Asset`
57. Verifikasi jumlah chip yang tampil ditambah N pada chip ringkasan sama dengan 5

### Search di dalam dropdown dan sumber opsi kosong
58. Tampilkan Tabel File Manager tab Files dengan kondisi K1
59. Klik ikon Filter
60. Buka dropdown field `File Format`
61. Verifikasi opsi `JPG` tampil
62. Verifikasi opsi `JPEG` tampil
63. Verifikasi opsi `PNG` tampil
64. Ketik `PDF` pada kotak cari di dalam dropdown
65. Verifikasi teks `No results found` tampil di dalam dropdown
66. Tampilkan Tabel File Manager tab Files dengan kondisi K2
67. Klik ikon Filter
68. Buka dropdown field `File Format`
69. Verifikasi teks `No options available` tampil di dalam dropdown

### Menyembunyikan kolom tidak menghapus field filter dan filter ter-Apply
70. Tampilkan Tabel File Manager tab Files dengan kondisi K1
71. Klik ikon Filter
72. Pilih `JPG` pada field `File Format`
73. Klik `[Apply]`
74. Verifikasi tabel memuat baris `laptop-front.jpg` sebelum kolom disembunyikan
75. Verifikasi baris `monitor-lg-front.png` tidak tampil
76. Klik trigger `Column Visibility` pada header kolom Actions
77. Hapus centang kolom `File Format` pada panel Column Visibility
78. Verifikasi header kolom `File Name` masih tampil setelah kolom `File Format` disembunyikan
79. Verifikasi header kolom `File Format` tidak tampil pada tabel
80. Verifikasi baris `laptop-front.jpg` tetap tampil
81. Verifikasi baris `monitor-lg-front.png` tetap tidak tampil
82. Verifikasi indikator filter aktif tetap tampil pada ikon Filter
83. Verifikasi field `File Format` tetap tampil pada Filter Panel
84. Verifikasi chip `JPG` tetap tampil pada field `File Format`

### Pencarian tree Group menyaring saat mengetik dan Enter tidak mengubah hasil
85. Tampilkan Tabel File Manager tab Files dengan kondisi K1
86. Klik ikon Filter
87. Buka field `Group`
88. Verifikasi node `Head Office` tampil pada tree Group
89. Verifikasi node `Branch Bandung` tampil pada tree Group
90. Verifikasi node `Branch Surabaya` tampil pada tree Group
91. Ketik `Bandung` pada kotak pencarian tree Group
92. Verifikasi node `Branch Bandung` tampil pada tree Group[^drift-1]
93. Verifikasi node `Head Office` tidak tampil pada tree Group[^drift-1]
94. Verifikasi node `Branch Surabaya` tidak tampil pada tree Group[^drift-1]
95. Tekan Enter
96. Verifikasi node `Branch Bandung` tetap tampil pada tree Group[^drift-1]
97. Verifikasi node `Head Office` tetap tidak tampil pada tree Group[^drift-1]
98. Verifikasi node `Branch Surabaya` tetap tidak tampil pada tree Group[^drift-1]

[^drift-1]: Drift PRD/foundation vs kontrak komponen. PRD unit EB-SRC-6 (foundation `prd-conventions.md` §31.3): pencarian tree berjalan saat Enter, bukan real-time. Kontrak `TreeSelect#9`: kotak cari di dalam dialog tree picker menyaring node menurut label saat diketik dan Enter tidak melakukan apa-apa (juga `Tree#15`: filterKeyword menyaring saat mengetik). Diasersi: kontrak, karena field Group di Filter Panel bertipe Tree picker multi-select (TreeSelect); aturan Enter §31.3 milik pencarian tree Sidebar Group (SB-7).
