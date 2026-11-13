---
id: TC-FA-FAREG-UI-004-draft-mekanik-search-sort-paginasi
title: "Sub tab Draft: siklus kotak Search, indikator sort, dan paginasi"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§5#r2", "§5#r3", "EB-SRC-4@tabel-draft", "EB-SRT-3@tabel-draft", "EB-TBL-7@tabel-draft"]
smoke: []
dependsOn: []
trace:
  "§5#r2": [44, 45, 46, 49, 51, 52, 55, 58, 61, 63, 66, 68, 71, 76, 87, 90, 91, 92]
  "§5#r3": [5, 7, 8]
  EB-SRC-4@tabel-draft: [3, 5, 7, 8, 15, 17, 22, 24, 25]
  EB-SRT-3@tabel-draft: [28, 30, 33, 38, 39, 42]
  EB-TBL-7@tabel-draft: [57, 73, 78, 80, 82, 84]
anchor: [14, 21, 32, 36, 41]
coverage:
  web: automated
---

# Sub tab Draft: siklus kotak Search, indikator sort, dan paginasi

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Komponen: Sub tab `Draft` (TBL-REG-01)
- Data:
  - DU-004-1: 11 batch Draft Group `Gudang Cabang {n}` (n = 1 sampai 11), Origin `—`, Total Asset `3`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-09T08:15:00Z`.
  - DU-004-2: 10 batch Draft Group `Gudang Pusat {n}` (n = 1 sampai 10), Origin `—`, Total Asset `4`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-08T10:00:00Z`.
  - DU-004-3: 26 batch Draft Group `Gudang Regional {n}` (n = 1 sampai 26), Origin `—`, Total Asset `2`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-07T09:30:00Z`.
  - DU-004-4: 101 batch Draft Group `Gudang Wilayah {n}` (n = 1 sampai 101), Origin `—`, Total Asset `1`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-06T09:00:00Z`.
  - DU-004-5: 12 batch Draft Group `Gudang Kota {n}` (n = 1 sampai 12), Origin `—`, Total Asset `5`, Progress `20%`, Requested By `Siti Nurbaya`, Last Updated `2026-11-05T13:20:00Z`.
  - DU-004-6: 3 batch Draft Group `Kantor Kota {n}` (n = 1 sampai 3), Origin `—`, Total Asset `7`, Progress `40%`, Requested By `Siti Nurbaya`, Last Updated `2026-11-04T15:10:00Z`.
  - DU-004-7: kata kunci Search `Gudang Kota`.
  - DU-004-8: nomor halaman `0` yang diketik pada input nomor halaman.
  - DU-004-9: nomor halaman `-1` yang diketik pada input nomor halaman.
  - DU-004-10: nomor halaman `3`, yaitu nomor setelah halaman terakhir pada daftar DU-004-1, yang diketik pada input nomor halaman.
  - DU-004-11: nomor halaman `abc` yang diketik pada input nomor halaman.
  - DU-004-12: batch Draft Group `Gudang Utara`, Origin `—`, Total Asset `6`, Progress `10%`, Requested By `Budi Santoso`, Last Updated `2026-11-03T08:00:00Z`.
  - DU-004-13: batch Draft Group `Kantor Selatan`, Origin `—`, Total Asset `9`, Progress `30%`, Requested By `Budi Santoso`, Last Updated `2026-11-02T08:00:00Z`.
- Kondisi:
  - K1: daftar berisi DU-004-1.
  - K2: daftar berisi DU-004-2.
  - K3: daftar berisi DU-004-3.
  - K4: daftar berisi DU-004-4.
  - K5: daftar berisi DU-004-5 dan DU-004-6; pencarian dengan kata kunci DU-004-7 hanya menghasilkan DU-004-5.
  - K6: daftar berisi DU-004-12 dan DU-004-13; pencarian `Gudang Utara` hanya menghasilkan DU-004-12; kotak Search kosong menghasilkan DU-004-12 dan DU-004-13.

## Test Steps

### Ikon Search membuka kotak berfokus dan pencarian hanya berjalan saat Enter
1. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K6
2. Klik ikon Search pada toolbar
3. Verifikasi kotak Search terbuka dan terfokus
4. Ketik Search `Gudang Utara` tanpa menekan Enter
5. Verifikasi baris `Kantor Selatan` masih tampil
6. Tekan Enter
7. Verifikasi baris `Gudang Utara` tampil
8. Verifikasi baris `Kantor Selatan` tidak tampil

### Tombol batal sebelum Enter tidak mereset dan Enter dengan kotak kosong mereset
9. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K6
10. Klik ikon Search pada toolbar
11. Ketik Search `Gudang Utara`, tekan Enter
12. Ganti isi kotak Search dengan `Kantor Selatan` tanpa menekan Enter
13. Klik `✕` pada kotak Search
14. Verifikasi baris `Gudang Utara` tampil
15. Verifikasi baris `Kantor Selatan` tidak tampil
16. Tekan Enter
17. Verifikasi baris `Kantor Selatan` tampil kembali

### Tombol panah kembali menutup kotak sekaligus mereset
18. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K6
19. Klik ikon Search pada toolbar
20. Ketik Search `Gudang Utara`, tekan Enter
21. Verifikasi baris `Gudang Utara` tampil
22. Verifikasi baris `Kantor Selatan` tidak tampil
23. Klik `(←)` pada kotak Search
24. Verifikasi kotak Search tertutup
25. Verifikasi baris `Kantor Selatan` tampil kembali

### Indikator sort mengikuti siklus tiga klik
26. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
27. Klik ikon sort kolom `Group`
28. Verifikasi kolom `Group` menampilkan indikator `↑`
29. Klik ikon sort kolom `Group`
30. Verifikasi kolom `Group` menampilkan indikator `↓`
31. Klik ikon sort kolom `Group`
32. Verifikasi header kolom `Group` memiliki ikon sort
33. Verifikasi indikator sort kolom `Group` tidak tampil

### Klik kolom lain memindahkan indikator sort
34. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
35. Klik ikon sort kolom `Group`
36. Verifikasi kolom `Group` menampilkan indikator `↑`
37. Klik ikon sort kolom `Total Asset`
38. Verifikasi kolom `Total Asset` menampilkan indikator `↑`
39. Verifikasi indikator sort kolom `Group` tidak tampil

### Kolom Actions tidak punya ikon sort
40. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
41. Verifikasi header kolom `Group` memiliki ikon sort
42. Verifikasi ikon sort pada header kolom Actions `⋯` tidak tampil

### Paginasi default 10 baris dan pilihan ukuran halaman
43. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
44. Verifikasi halaman `1` menampilkan `10` baris
45. Verifikasi pilihan ukuran halaman `10`, `25`, `50`, dan `100` tersedia
46. Verifikasi pilihan ukuran halaman `All` tidak tersedia

### Halaman terakhir berisi satu baris
47. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
48. Klik halaman `2`
49. Verifikasi halaman `2` menampilkan `1` baris

### Jumlah baris tepat satu halaman tidak membentuk halaman kedua
50. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
51. Verifikasi halaman `1` menampilkan `10` baris
52. Verifikasi halaman `2` tidak tersedia

### Ganti ukuran halaman kembali ke halaman 1
53. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
54. Klik halaman `2`
55. Verifikasi halaman aktif `2`
56. Pilih ukuran halaman `25`
57. Verifikasi halaman aktif `1`
58. Verifikasi halaman `1` menampilkan `11` baris

### Ukuran halaman 25 dengan 26 batch
59. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K3
60. Pilih ukuran halaman `25`
61. Verifikasi halaman `1` menampilkan `25` baris
62. Klik halaman `2`
63. Verifikasi halaman `2` menampilkan `1` baris

### Ukuran halaman 100 dengan 101 batch
64. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K4
65. Pilih ukuran halaman `100`
66. Verifikasi halaman `1` menampilkan `100` baris
67. Klik halaman `2`
68. Verifikasi halaman `2` menampilkan `1` baris

### Ganti sort tetap di halaman sekarang
69. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
70. Klik halaman `2`
71. Verifikasi halaman aktif `2`
72. Klik ikon sort kolom `Group`
73. Verifikasi halaman aktif `2`

### Nomor halaman tidak valid diabaikan
74. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
75. Klik halaman `2`
76. Verifikasi halaman aktif `2`
77. Ketik nomor halaman `0`, tekan Enter
78. Verifikasi halaman aktif `2`
79. Ketik nomor halaman `-1`, tekan Enter
80. Verifikasi halaman aktif `2`
81. Ketik nomor halaman `3`, tekan Enter
82. Verifikasi halaman aktif `2`
83. Ketik nomor halaman `abc`, tekan Enter
84. Verifikasi halaman aktif `2`

### Search dengan hasil lebih dari satu halaman kembali ke halaman 1
85. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K5
86. Klik halaman `2`
87. Verifikasi halaman aktif `2`
88. Klik ikon Search pada toolbar
89. Ketik Search `Gudang Kota`, tekan Enter
90. Verifikasi halaman aktif `1`
91. Verifikasi halaman `1` menampilkan `10` baris
92. Verifikasi halaman `2` tersedia
