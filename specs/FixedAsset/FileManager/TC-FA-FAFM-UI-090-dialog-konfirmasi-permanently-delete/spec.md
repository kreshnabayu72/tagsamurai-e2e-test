---
id: TC-FA-FAFM-UI-090-dialog-konfirmasi-permanently-delete
title: "Dialog konfirmasi Permanently Delete single dan bulk: isi, tutup, Saving, dan reaksi gagal"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ACT-05c", "ACT-06b", "ARS-02c", "ARS-02d", "D-03", "D-04", "INV-06a", "INV-06b", "S-23", "T-09", "T-10", "V-05", "V-07", "§4.4#b4", "§4.4#b14", "EB-FB-1@permanently-delete-file", "EB-FB-2@permanently-delete-file", "EB-ERR-1@permanently-delete-file"]
smoke: []
dependsOn: []
trace:
  "ACT-05c": 4
  "ACT-06b": 12
  "ARS-02c": 55
  "ARS-02d": 57
  "D-03": [4, 5, 6, 7, 93, 94]
  "D-04": [12, 13, 15, 16, 17]
  "INV-06a": [8, 18]
  "INV-06b": [4, 12]
  "S-23": [23, 24, 25, 34, 49, 63, 87, 88, 89]
  "T-09": [49, 96]
  "T-10": 63
  "V-05": [49, 96]
  "V-07": 63
  "§4.4#b4": [4, 12]
  "§4.4#b14": [23, 24, 25, 30, 32, 33]
  "EB-FB-1@permanently-delete-file": [39, 44, 49, 57, 63, 96, 101]
  "EB-FB-2@permanently-delete-file": [25, 34, 89]
  "EB-ERR-1@permanently-delete-file": [50, 51, 52, 53, 55, 57, 58, 64, 65, 66, 67, 69, 70, 75, 76, 77, 78, 79, 81, 82]
coverage:
  web: automated
---

# Dialog konfirmasi Permanently Delete single dan bulk: isi, tutup, Saving, dan reaksi gagal

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager, dialog Recycle Bin terbuka.
- Komponen: Dialog konfirmasi Permanently Delete File
- Data:
  - DU-090-1: File di Recycle Bin `laptop-old.png`, Source `Asset Photo`, Asset `Laptop Dell Latitude 5420 - 4`.
  - DU-090-2: File di Recycle Bin `damage-01.jpg`, Source `Damaged Photo`, Asset `Toyota Avanza - 2`.
  - DU-090-3: File di Recycle Bin `calibration-cert.pdf`, Source `Attachment`, Asset `Laptop Dell Latitude 5420 - 9`.
  - DU-090-4: 7 file di Recycle Bin `arsip-1.jpg` sampai `arsip-7.jpg`, Source `Asset Photo`, Asset `Toyota Avanza - 1` sampai `Toyota Avanza - 7`.
- Kondisi:
  - K1: Recycle Bin berisi tepat 10 baris, yaitu DU-090-1 sampai DU-090-4.
  - K2: seperti K1, dan Permanently Delete atas `laptop-old.png` berhasil.
  - K3: seperti K1, dan Permanently Delete atas seluruh 10 file terpilih berhasil.
  - K4: seperti K1, dan Permanently Delete atas `laptop-old.png` gagal karena error server pada percobaan pertama, lalu berhasil pada percobaan berikutnya.
  - K5: seperti K1, dan Permanently Delete atas seluruh 10 file terpilih gagal karena error server pada percobaan pertama, lalu berhasil pada percobaan berikutnya.
  - K6: seperti K1, dan Permanently Delete atas `laptop-old.png` gagal karena timeout pada percobaan pertama, lalu berhasil pada percobaan berikutnya.
  - K7: seperti K1, dan Permanently Delete atas `laptop-old.png` yang dipilih lewat Bulk Action Bar gagal karena error server.
  - K8: seperti K1, dan Permanently Delete atas seluruh 10 file terpilih berhasil untuk sebagian file (minimal satu file terhapus) dan gagal karena error server untuk file lainnya.

## Test Steps

### Dialog Permanently Delete single memuat judul, bullet, peringatan, tombol, dan severity
1. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K1
2. Klik `⋯` pada baris `laptop-old.png`
3. Klik `Permanently Delete`
4. Verifikasi dialog konfirmasi `Permanently Delete File` tampil
5. Verifikasi bullet `laptop-old.png` tampil pada body dialog
6. Verifikasi body dialog memuat `Are you sure you want to permanently delete it? This action cannot be undone.`
7. Verifikasi tombol `[Cancel]` dan `[Permanently Delete]` tampil pada footer dialog
8. Verifikasi dialog konfirmasi `Permanently Delete File` memiliki severity `danger`

### Dialog Permanently Delete bulk memuat seluruh nama dalam daftar yang bisa digulir
9. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K1
10. Centang checkbox header tabel
11. Klik `Permanently Delete` pada Bulk Action Bar
12. Verifikasi dialog konfirmasi `Permanently Delete Files` tampil
13. Verifikasi bullet `laptop-old.png` tampil pada body dialog
14. Gulir daftar bullet sampai dasar
15. Verifikasi bullet `arsip-7.jpg` tampil pada body dialog
16. Verifikasi body dialog memuat `Are you sure you want to permanently delete them? This action cannot be undone.`
17. Verifikasi tombol `[Cancel]` dan `[Permanently Delete]` tampil pada footer dialog
18. Verifikasi dialog konfirmasi `Permanently Delete Files` memiliki severity `danger`

### Cancel menutup dialog tanpa mutasi dan tanpa toast
19. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K1
20. Klik `⋯` pada baris `laptop-old.png`
21. Klik `Permanently Delete`
22. Klik `[Cancel]`
23. Verifikasi baris `laptop-old.png` tetap tampil pada tabel
24. Verifikasi dialog konfirmasi `Permanently Delete File` tidak tampil
25. Verifikasi tidak ada toast yang tampil

### Klik backdrop tidak menutup dan Esc menutup tanpa menghapus
26. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K1
27. Klik `⋯` pada baris `laptop-old.png`
28. Klik `Permanently Delete`
29. Klik backdrop di luar dialog
30. Verifikasi dialog konfirmasi `Permanently Delete File` tetap tampil
31. Tekan Esc
32. Verifikasi baris `laptop-old.png` tetap tampil pada tabel
33. Verifikasi dialog konfirmasi `Permanently Delete File` tidak tampil
34. Verifikasi tidak ada toast yang tampil setelah dialog ditutup dengan Esc

### Permanently Delete single berhasil menampilkan toast sukses
35. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K2
36. Klik `⋯` pada baris `laptop-old.png`
37. Klik `Permanently Delete`
38. Klik `[Permanently Delete]`
39. Verifikasi toast `Success, laptop-old.png has been permanently deleted.` tampil

### Permanently Delete bulk berhasil menampilkan toast sukses
40. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K3
41. Centang checkbox header tabel
42. Klik `Permanently Delete` pada Bulk Action Bar
43. Klik `[Permanently Delete]`
44. Verifikasi toast `Success, file has been permanently deleted.` tampil

### Permanently Delete single gagal karena error server mempertahankan dialog dan bisa diulang
45. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K4
46. Klik `⋯` pada baris `laptop-old.png`
47. Klik `Permanently Delete`
48. Klik `[Permanently Delete]`
49. Verifikasi toast `Error, failed to permanently delete laptop-old.png.` tampil
50. Verifikasi dialog konfirmasi `Permanently Delete File` masih tampil
51. Verifikasi bullet `laptop-old.png` masih tampil pada body dialog
52. Verifikasi tombol `[Permanently Delete]` bisa diklik lagi
53. Verifikasi toast `Error, failed to permanently delete laptop-old.png.` tidak memiliki tombol `[Try Again]`
54. Waktu berlalu sampai 10 detik sejak toast tampil
55. Verifikasi toast `Error, failed to permanently delete laptop-old.png.` masih tampil
56. Klik `[Permanently Delete]`
57. Verifikasi toast `Success, laptop-old.png has been permanently deleted.` tampil
58. Verifikasi hanya satu toast `Success, laptop-old.png has been permanently deleted.` tampil

### Permanently Delete bulk gagal seluruhnya mempertahankan dialog
59. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K5
60. Centang checkbox header tabel
61. Klik `Permanently Delete` pada Bulk Action Bar
62. Klik `[Permanently Delete]`
63. Verifikasi toast `Error, failed to permanently delete file.` tampil
64. Verifikasi dialog konfirmasi `Permanently Delete Files` masih tampil
65. Verifikasi bullet `laptop-old.png` masih tampil pada body dialog
66. Verifikasi tombol `[Permanently Delete]` bisa diklik lagi
67. Verifikasi toast `Error, failed to permanently delete file.` tidak memiliki tombol `[Try Again]`
68. Klik `[Permanently Delete]`
69. Verifikasi toast `Success, file has been permanently deleted.` tampil
70. Verifikasi hanya satu toast `Success, file has been permanently deleted.` tampil

### Permanently Delete gagal karena timeout mempertahankan dialog
71. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K6
72. Klik `⋯` pada baris `laptop-old.png`
73. Klik `Permanently Delete`
74. Klik `[Permanently Delete]`
75. Verifikasi toast `Connection problem. Please try again.` tampil setelah Permanently Delete gagal
76. Verifikasi dialog konfirmasi `Permanently Delete File` masih tampil
77. Verifikasi bullet `laptop-old.png` masih tampil pada body dialog
78. Verifikasi tombol `[Permanently Delete]` bisa diklik lagi
79. Verifikasi toast `Connection problem. Please try again.` setelah Permanently Delete gagal tidak memiliki tombol `[Try Again]`
80. Klik `[Permanently Delete]`
81. Verifikasi toast `Success, laptop-old.png has been permanently deleted.` tampil
82. Verifikasi hanya satu toast `Success, laptop-old.png has been permanently deleted.` tampil

### Cancel pada dialog bulk menutup dialog tanpa mutasi dan tanpa toast
83. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K1
84. Centang checkbox header tabel
85. Klik `Permanently Delete` pada Bulk Action Bar
86. Klik `[Cancel]`
87. Verifikasi checkbox baris `laptop-old.png` masih tercentang
88. Verifikasi dialog konfirmasi `Permanently Delete Files` tidak tampil
89. Verifikasi tidak ada toast yang tampil setelah Cancel pada dialog bulk

### Bulk dengan satu file terpilih memakai dialog single dan kegagalannya menyebut nama file
90. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K7
91. Centang checkbox baris `laptop-old.png`
92. Klik `Permanently Delete` pada Bulk Action Bar
93. Verifikasi dialog konfirmasi `Permanently Delete File` tampil
94. Verifikasi body dialog memuat `Are you sure you want to permanently delete it? This action cannot be undone.`
95. Klik `[Permanently Delete]`
96. Verifikasi toast `Error, failed to permanently delete laptop-old.png.` tampil

### Permanently Delete bulk sebagian file gagal dan sebagian berhasil menampilkan toast parsial
97. Tampilkan Dialog konfirmasi Permanently Delete File dengan kondisi K8
98. Centang checkbox header tabel
99. Klik `Permanently Delete` pada Bulk Action Bar
100. Klik `[Permanently Delete]`
101. Verifikasi toast `Success, file has been permanently deleted. Some items were skipped.` tampil
