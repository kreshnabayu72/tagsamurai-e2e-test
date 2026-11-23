---
id: TC-FA-FAFM-UI-089-dialog-konfirmasi-delete
title: "Dialog konfirmasi Delete single dan bulk: isi, tutup, Saving, dan reaksi gagal"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ACT-02d", "ACT-04b", "ARS-01e", "ARS-01f", "ARS-01j", "D-01", "D-02", "EC-10", "F-FAFM-02e", "INV-04a", "INV-04b", "S-16", "S-21", "T-04", "T-05", "V-04", "V-06", "§4.4#b4", "§4.4#b14", "§4.5#b3", "§6#p5", "EB-FB-1@delete-file", "EB-FB-2@delete-file", "EB-FB-4", "EB-ERR-1@delete-file", "EB-ERR-2@delete-file"]
smoke: []
dependsOn: []
trace:
  "ACT-02d": 4
  "ACT-04b": 13
  "ARS-01e": 71
  "ARS-01f": 73
  "ARS-01j": [99, 100]
  "D-01": [4, 5, 6, 7, 8]
  "D-02": [13, 14, 16, 17, 18, 19]
  "EC-10": [99, 100]
  "F-FAFM-02e": [4, 13]
  "INV-04a": [4, 9, 13, 20]
  "INV-04b": [4, 13]
  "S-16": 99
  "S-21": [30, 31, 32, 40, 65, 79]
  "T-04": [65, 110]
  "T-05": 79
  "V-04": [65, 110]
  "V-06": 79
  "§4.4#b4": [4, 13]
  "§4.4#b14": [31, 32, 37, 39, 40]
  "§4.5#b3": [45, 47]
  "§6#p5": [6, 17, 24, 25]
  "EB-FB-1@delete-file": [52, 60, 65, 79, 105, 110]
  "EB-FB-2@delete-file": 32
  "EB-FB-4": [55, 71]
  "EB-ERR-1@delete-file": [66, 67, 68, 69, 73, 74, 80, 81, 82, 84, 85, 90, 91, 92, 93, 94, 115, 116, 121, 123, 124]
  "EB-ERR-2@delete-file": [39, 45, 47, 100]
anchor: [39, 54]
coverage:
  web: automated
---

# Dialog konfirmasi Delete single dan bulk: isi, tutup, Saving, dan reaksi gagal

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager, tab `Asset Photo`.
- Komponen: Dialog konfirmasi Delete File
- Data:
  - DU-089-1: File `laptop-front.jpg`, Source `Asset Photo`, Asset `Laptop Dell Latitude 5420 - 4`.
  - DU-089-2: File `monitor-lg-24.jpg`, Source `Asset Photo`, Asset `Monitor LG 24 - 7`.
  - DU-089-3: File `printer-hp-m404.jpg`, Source `Asset Photo`, Asset `Printer HP M404 - 1`.
  - DU-089-4: 7 file `inventaris-1.jpg` sampai `inventaris-7.jpg`, Source `Asset Photo`, Asset `Toyota Avanza - 1` sampai `Toyota Avanza - 7`.
- Kondisi:
  - K1: tab `Asset Photo` berisi tepat 10 baris, yaitu DU-089-1 sampai DU-089-4.
  - K2: seperti K1, dan Delete atas `laptop-front.jpg` berhasil.
  - K3: seperti K1, dan Delete atas seluruh 10 file terpilih berhasil.
  - K4: seperti K1, dan Delete atas `laptop-front.jpg` gagal karena error server pada percobaan pertama, lalu berhasil pada percobaan berikutnya.
  - K5: seperti K1, dan Delete atas seluruh 10 file terpilih gagal karena error server pada percobaan pertama, lalu berhasil pada percobaan berikutnya.
  - K6: seperti K1, dan Delete atas `laptop-front.jpg` gagal karena timeout pada percobaan pertama, lalu berhasil pada percobaan berikutnya.
  - K7: seperti K1, dan Delete atas `laptop-front.jpg` berhasil dengan respons yang selesai setelah 2 detik.
  - K8: seperti K1, dan Delete atas seluruh 10 file terpilih berhasil untuk sebagian file (minimal satu file terhapus) dan gagal karena error server untuk file lainnya.
  - K9: seperti K1, dan Delete atas `laptop-front.jpg` yang dipilih lewat Bulk Action Bar gagal karena error server.

## Test Steps

### Dialog Delete single memuat judul, bullet, dampak, dan tombol
1. Tampilkan Dialog konfirmasi Delete File dengan kondisi K1
2. Klik `⋯` pada baris `laptop-front.jpg`
3. Klik `Delete`
4. Verifikasi dialog konfirmasi `Delete File` tampil
5. Verifikasi bullet `laptop-front.jpg` tampil pada body dialog
6. Verifikasi body dialog memuat `The file will be removed from the record that uses it and moved to the recycle bin.`
7. Verifikasi body dialog memuat `Are you sure you want to delete it?`
8. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil pada footer dialog
9. Verifikasi dialog konfirmasi `Delete File` memiliki severity `danger`

### Dialog Delete bulk memuat seluruh nama dalam daftar yang bisa digulir
10. Tampilkan Dialog konfirmasi Delete File dengan kondisi K1
11. Centang checkbox header tabel
12. Klik `Delete` pada Bulk Action Bar
13. Verifikasi dialog konfirmasi `Delete Files` tampil
14. Verifikasi bullet `laptop-front.jpg` tampil pada body dialog
15. Gulir daftar bullet sampai dasar
16. Verifikasi bullet `inventaris-7.jpg` tampil pada body dialog
17. Verifikasi body dialog memuat `The files will be removed from the records that use them and moved to the recycle bin.`
18. Verifikasi body dialog memuat `Are you sure you want to delete them?`
19. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil pada footer dialog
20. Verifikasi dialog konfirmasi `Delete Files` memiliki severity `danger`

### Bulk dengan satu file terpilih memakai dialog single
21. Tampilkan Dialog konfirmasi Delete File dengan kondisi K1
22. Centang checkbox baris `laptop-front.jpg`
23. Klik `Delete` pada Bulk Action Bar
24. Verifikasi dialog konfirmasi `Delete File` tampil
25. Verifikasi body dialog memuat `Are you sure you want to delete it?`

### Cancel menutup dialog tanpa mutasi dan tanpa toast
26. Tampilkan Dialog konfirmasi Delete File dengan kondisi K1
27. Klik `⋯` pada baris `laptop-front.jpg`
28. Klik `Delete`
29. Klik `[Cancel]`
30. Verifikasi baris `laptop-front.jpg` tetap tampil pada tabel
31. Verifikasi dialog konfirmasi `Delete File` tidak tampil
32. Verifikasi tidak ada toast yang tampil

### Klik backdrop tidak menutup dan Esc menutup tanpa menghapus
33. Tampilkan Dialog konfirmasi Delete File dengan kondisi K1
34. Klik `⋯` pada baris `laptop-front.jpg`
35. Klik `Delete`
36. Klik backdrop di luar dialog
37. Verifikasi dialog konfirmasi `Delete File` tetap tampil
38. Tekan Esc
39. Verifikasi baris `laptop-front.jpg` tetap tampil pada tabel
40. Verifikasi dialog konfirmasi `Delete File` tidak tampil

### Fokus terkunci di dialog dan kembali ke pemicu
41. Tampilkan Dialog konfirmasi Delete File dengan kondisi K1
42. Klik `⋯` pada baris `laptop-front.jpg`
43. Klik `Delete`
44. Tekan Tab tiga kali
45. Verifikasi fokus tetap berada di dalam dialog konfirmasi `Delete File`
46. Klik `[Cancel]`
47. Verifikasi fokus kembali ke pemicu dialog konfirmasi `Delete File`

### Delete single berhasil menampilkan toast yang hilang sendiri
48. Tampilkan Dialog konfirmasi Delete File dengan kondisi K2
49. Klik `⋯` pada baris `laptop-front.jpg`
50. Klik `Delete`
51. Klik `[Delete]`
52. Verifikasi toast `Success, laptop-front.jpg has been deleted.` tampil
53. Waktu berlalu sampai 5 detik sejak toast tampil
54. Verifikasi baris `monitor-lg-24.jpg` tampil pada tabel
55. Verifikasi toast `Success, laptop-front.jpg has been deleted.` tidak tampil

### Delete bulk berhasil menampilkan toast sukses
56. Tampilkan Dialog konfirmasi Delete File dengan kondisi K3
57. Centang checkbox header tabel
58. Klik `Delete` pada Bulk Action Bar
59. Klik `[Delete]`
60. Verifikasi toast `Success, file has been deleted.` tampil

### Delete single gagal karena error server mempertahankan dialog dan bisa diulang
61. Tampilkan Dialog konfirmasi Delete File dengan kondisi K4
62. Klik `⋯` pada baris `laptop-front.jpg`
63. Klik `Delete`
64. Klik `[Delete]`
65. Verifikasi toast `Error, failed to delete laptop-front.jpg.` tampil
66. Verifikasi dialog konfirmasi `Delete File` masih tampil
67. Verifikasi bullet `laptop-front.jpg` masih tampil pada body dialog
68. Verifikasi tombol `[Delete]` bisa diklik lagi
69. Verifikasi toast `Error, failed to delete laptop-front.jpg.` tidak memiliki tombol `[Try Again]`
70. Waktu berlalu sampai 10 detik sejak toast tampil
71. Verifikasi toast `Error, failed to delete laptop-front.jpg.` masih tampil
72. Klik `[Delete]`
73. Verifikasi toast `Success, laptop-front.jpg has been deleted.` tampil
74. Verifikasi hanya satu toast `Success, laptop-front.jpg has been deleted.` tampil

### Delete bulk gagal seluruhnya mempertahankan dialog
75. Tampilkan Dialog konfirmasi Delete File dengan kondisi K5
76. Centang checkbox header tabel
77. Klik `Delete` pada Bulk Action Bar
78. Klik `[Delete]`
79. Verifikasi toast `Error, failed to delete file.` tampil
80. Verifikasi dialog konfirmasi `Delete Files` masih tampil
81. Verifikasi bullet `laptop-front.jpg` masih tampil pada body dialog
82. Verifikasi tombol `[Delete]` bisa diklik lagi
83. Klik `[Delete]`
84. Verifikasi toast `Success, file has been deleted.` tampil
85. Verifikasi hanya satu toast `Success, file has been deleted.` tampil

### Delete gagal karena timeout mempertahankan dialog
86. Tampilkan Dialog konfirmasi Delete File dengan kondisi K6
87. Klik `⋯` pada baris `laptop-front.jpg`
88. Klik `Delete`
89. Klik `[Delete]`
90. Verifikasi toast `Connection problem. Please try again.` tampil
91. Verifikasi dialog konfirmasi `Delete File` masih tampil
92. Verifikasi bullet `laptop-front.jpg` masih tampil pada body dialog
93. Verifikasi tombol `[Delete]` bisa diklik lagi
94. Verifikasi toast `Connection problem. Please try again.` setelah Delete gagal tidak memiliki tombol `[Try Again]`

### Klik ganda pada Delete tidak mengirim dua kali
95. Tampilkan Dialog konfirmasi Delete File dengan kondisi K7
96. Klik `⋯` pada baris `laptop-front.jpg`
97. Klik `Delete`
98. Klik ganda `[Delete]`
99. Verifikasi `[Delete]` tidak bisa diklik selama permintaan berjalan
100. Verifikasi hanya satu toast `Success, laptop-front.jpg has been deleted.` tampil

### Delete bulk sebagian file gagal dan sebagian berhasil menampilkan toast parsial
101. Tampilkan Dialog konfirmasi Delete File dengan kondisi K8
102. Centang checkbox header tabel
103. Klik `Delete` pada Bulk Action Bar
104. Klik `[Delete]`
105. Verifikasi toast `Success, file has been deleted. Some items were skipped.` tampil

### Delete bulk dengan satu file terpilih gagal menyebut nama file
106. Tampilkan Dialog konfirmasi Delete File dengan kondisi K9
107. Centang checkbox baris `laptop-front.jpg`
108. Klik `Delete` pada Bulk Action Bar
109. Klik `[Delete]`
110. Verifikasi toast `Error, failed to delete laptop-front.jpg.` tampil

### Delete bulk gagal karena error server menampilkan toast tanpa tombol aksi
111. Tampilkan Dialog konfirmasi Delete File dengan kondisi K5
112. Centang checkbox header tabel
113. Klik `Delete` pada Bulk Action Bar
114. Klik `[Delete]`
115. Verifikasi toast `Error, failed to delete file.` tampil
116. Verifikasi toast `Error, failed to delete file.` tidak memiliki tombol `[Try Again]`

### Delete gagal karena timeout bisa diulang sampai berhasil
117. Tampilkan Dialog konfirmasi Delete File dengan kondisi K6
118. Klik `⋯` pada baris `laptop-front.jpg`
119. Klik `Delete`
120. Klik `[Delete]`
121. Verifikasi tombol `[Delete]` bisa diklik lagi
122. Klik `[Delete]`
123. Verifikasi toast `Success, laptop-front.jpg has been deleted.` tampil
124. Verifikasi hanya satu toast `Success, laptop-front.jpg has been deleted.` tampil
