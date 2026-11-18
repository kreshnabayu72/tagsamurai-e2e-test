---
id: TC-FA-MYASSET-BE-206-extension-aturan-server-dep-borrow
title: "Aturan server pengajuan Extend dari My Asset dan penarikannya"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r64", "§1.2#r66", "§1.2#r67", "§4.1b#r17", "§4.1b#r48", "§4.1b#r54", "§9.2#b8", "§9.4.2#r7", "§9.4.2#r44", "§9.6#r3", "§9.6#r4", "§9.7#r15", "EB-CON-3", "EB-EDG-1"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§1.2#r64": [6, 8, 10, 11]
  "§1.2#r66": 12
  "§1.2#r67": 14
  "§4.1b#r17": [2, 3, 4, 11, 20]
  "§4.1b#r48": [52, 54, 79, 82, 84]
  "§4.1b#r54": [58, 61, 88, 91, 94, 107, 110]
  "§9.2#b8": [23, 25, 31, 33, 35, 73]
  "§9.4.2#r7": 48
  "§9.4.2#r44": [39, 41]
  "§9.6#r3": [6, 14, 16, 64, 65, 67, 68, 70, 103]
  "§9.6#r4": [23, 27, 33, 39, 73, 75]
  "§9.7#r15": [45, 47, 48]
  "EB-CON-3": [39, 48]
  "EB-EDG-1": [14, 16, 27, 65, 97, 99, 101]
owner: BE
---

# Aturan server pengajuan Extend dari My Asset dan penarikannya

## Prerequisites
- Aktor: Maya (Borrower yang mengajukan dan menarik Extend), Gita (Aktor Borrow Group `Head Office` yang meninjau pengajuan, meneruskannya ke approval, dan mengembalikan aset), dan Dewi (Aktor Missing Group `Head Office` yang menolak laporan aset hilang).
- Data:
  - DU-206-1: User `Maya Anggraini {runId}`, role Read Only, cakupan Group `Head Office` beserta Group di bawahnya, Borrower pada DU-206-3 sampai DU-206-12, DU-206-21 sampai DU-206-26, dan DU-206-32.
  - DU-206-2: User `Gita Permata {runId}`, role Asset Admin, cakupan Group `Head Office` beserta Group di bawahnya, Aktor Borrow Group `Head Office`.
  - DU-206-3: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 61 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati.
  - DU-206-4: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 62 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati.
  - DU-206-5: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 63 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati.
  - DU-206-6: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 64 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati, Extend yang diteruskan Aktor Borrow memerlukan approval.
  - DU-206-7: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 65 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati.
  - DU-206-8: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 66 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati.
  - DU-206-9: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 67 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati.
  - DU-206-10: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 68 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati.
  - DU-206-11: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 69 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `0`, Extensions `0 / 0`, Due date satuan Days belum terlewati.
  - DU-206-12: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 70 {runId}`, Group `Head Office`, status `Waiting for Approval`, Max extensions `2`, Extensions `0 / 2`.
  - DU-206-21: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 96 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati.
  - DU-206-22: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 97 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati.
  - DU-206-23: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 98 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati.
  - DU-206-24: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 99 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati, Extend yang diteruskan Aktor Borrow memerlukan approval.
  - DU-206-25: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 100 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati, Extend yang diteruskan Aktor Borrow memerlukan approval.
  - DU-206-26: Pinjaman Maya melalui Borrow an Asset self-service, aset `Laptop Dell Latitude 5420 - 101 {runId}`, Group `Head Office`, status `Borrowed`, Due date belum terlewati.
  - DU-206-32: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 102 {runId}`, Group `Head Office`, status `Borrowed`, Max extensions `2`, Extensions `0 / 2`, Due date satuan Days belum terlewati.
  - DU-206-33: User `Dewi Lestari {runId}`, memegang hak Aktor Missing pada Group `Head Office`, cakupan Group `Head Office` beserta Group di bawahnya.

## Test Steps

### Kolom Extensions menghitung hanya Extend yang berlaku
1. Maya meminta data tab Borrowed dan mencatat Due Date baris aset `Laptop Dell Latitude 5420 - 61 {runId}`
2. Verifikasi baris aset `Laptop Dell Latitude 5420 - 69 {runId}` memiliki Extensions `0 / 0`
3. Verifikasi baris aset `Laptop Dell Latitude 5420 - 70 {runId}` memiliki Extensions `0 / 2`
4. Verifikasi baris aset `Laptop Dell Latitude 5420 - 61 {runId}` memiliki Extensions `0 / 2`

### Pengajuan Extend menunggu review dan pengajuan kedua ditolak
5. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 61 {runId}` dengan Reason `Perpanjangan untuk penyelesaian audit proyek`
6. Verifikasi pengajuan Extend diterima server sebagai pengajuan yang menunggu review
7. Gita meminta daftar pengajuan Extend yang menunggu review Aktor Borrow Group `Head Office`
8. Verifikasi daftar memuat pengajuan Extend untuk baris aset `Laptop Dell Latitude 5420 - 61 {runId}` milik Maya
9. Maya meminta data tab Borrowed
10. Verifikasi baris aset `Laptop Dell Latitude 5420 - 61 {runId}` berstatus `Extension Request`
11. Verifikasi baris aset `Laptop Dell Latitude 5420 - 61 {runId}` tetap memiliki Extensions `0 / 2`, karena pengajuan yang menunggu tidak dihitung
12. Verifikasi Due Date baris aset `Laptop Dell Latitude 5420 - 61 {runId}` sama dengan Due Date pada langkah 1
13. Maya mengajukan Extend kedua untuk baris aset `Laptop Dell Latitude 5420 - 61 {runId}` dengan Reason `Perpanjangan untuk penyelesaian audit proyek`
14. Verifikasi pengajuan kedua ditolak server karena pengajuan sebelumnya masih menunggu
15. Gita meminta daftar pengajuan Extend yang menunggu review Aktor Borrow Group `Head Office`
16. Verifikasi daftar memuat satu pengajuan Extend untuk baris aset `Laptop Dell Latitude 5420 - 61 {runId}`

### Pengajuan yang disetujui Aktor Borrow dihitung sebagai Extend yang berlaku
17. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 62 {runId}` dengan Reason `Perpanjangan untuk pelatihan operator`
18. Gita menyetujui pengajuan Extend baris aset `Laptop Dell Latitude 5420 - 62 {runId}`
19. Maya meminta data tab Borrowed
20. Verifikasi baris aset `Laptop Dell Latitude 5420 - 62 {runId}` memiliki Extensions `1 / 2`, karena Extend sudah berlaku

### Penarikan pengajuan yang menunggu review diterima dan penarikan ulang ditolak
21. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 63 {runId}` dengan Reason `Perpanjangan untuk kegiatan inventarisasi`
22. Maya menarik pengajuan Extend baris aset `Laptop Dell Latitude 5420 - 63 {runId}` lewat Cancel Extension Request
23. Verifikasi penarikan pengajuan yang menunggu review diterima server
24. Maya meminta data tab Borrowed
25. Verifikasi baris aset `Laptop Dell Latitude 5420 - 63 {runId}` kembali berstatus `Borrowed`
26. Maya menarik pengajuan Extend baris aset `Laptop Dell Latitude 5420 - 63 {runId}` lewat Cancel Extension Request sekali lagi
27. Verifikasi penarikan kedua ditolak server karena pengajuan sudah ditutup

### Penarikan pengajuan yang menunggu approval diterima
28. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 64 {runId}` dengan Reason `Perpanjangan untuk persiapan peluncuran produk`
29. Gita meneruskan pengajuan Extend baris aset `Laptop Dell Latitude 5420 - 64 {runId}` ke approval
30. Maya meminta data tab Borrowed
31. Verifikasi baris aset `Laptop Dell Latitude 5420 - 64 {runId}` berstatus `Extension Approval`
32. Maya menarik pengajuan Extend baris aset `Laptop Dell Latitude 5420 - 64 {runId}` lewat Cancel Extension Request
33. Verifikasi penarikan pengajuan yang menunggu approval diterima server
34. Maya meminta data tab Borrowed
35. Verifikasi baris aset `Laptop Dell Latitude 5420 - 64 {runId}` kembali berstatus `Borrowed`

### Penarikan pengajuan yang sudah ditinjau Aktor Borrow ditolak
36. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 65 {runId}` dengan Reason `Perpanjangan untuk pengujian lapangan`
37. Gita menolak pengajuan Extend baris aset `Laptop Dell Latitude 5420 - 65 {runId}`
38. Maya menarik pengajuan Extend baris aset `Laptop Dell Latitude 5420 - 65 {runId}` lewat Cancel Extension Request
39. Verifikasi penarikan ditolak server karena pengajuan sudah ditutup oleh review Aktor Borrow
40. Maya meminta data tab Borrowed
41. Verifikasi baris aset `Laptop Dell Latitude 5420 - 65 {runId}` berstatus `Borrowed` tanpa pengajuan Extend yang menunggu

### Return oleh Aktor Borrow menutup pengajuan Extend yang menunggu
42. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 66 {runId}` dengan Reason `Perpanjangan untuk keperluan survei`
43. Gita mengembalikan aset baris `Laptop Dell Latitude 5420 - 66 {runId}` sebagai Return oleh Aktor Borrow
44. Maya meminta data tab History
45. Verifikasi baris aset `Laptop Dell Latitude 5420 - 66 {runId}` berstatus `Returned`
46. Gita meminta daftar pengajuan Extend yang menunggu review Aktor Borrow Group `Head Office`
47. Verifikasi daftar memuat pengajuan Extend untuk baris aset `Laptop Dell Latitude 5420 - 61 {runId}`
48. Verifikasi daftar tidak memuat pengajuan Extend untuk baris aset `Laptop Dell Latitude 5420 - 66 {runId}`, karena pengajuan itu ditutup otomatis saat Return

### Laporan kerusakan menutup pengajuan Extend yang menunggu
49. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 67 {runId}` dengan Reason `Perpanjangan untuk acara pameran`
50. Maya mengirim laporan kerusakan atas baris aset `Laptop Dell Latitude 5420 - 67 {runId}`
51. Gita meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 67 {runId}`
52. Verifikasi Borrow Log memuat penutupan pengajuan Extend oleh `System` dengan alasan `Damage reported`
53. Maya meminta data tab Borrowed
54. Verifikasi baris aset `Laptop Dell Latitude 5420 - 67 {runId}` tidak lagi berstatus `Extension Request`

### Laporan aset hilang menutup pengajuan Extend dan pengajuan tidak dipulihkan
55. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 68 {runId}` dengan Reason `Perpanjangan untuk acara peluncuran`
56. Maya mengirim laporan aset hilang atas baris aset `Laptop Dell Latitude 5420 - 68 {runId}`
57. Gita meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 68 {runId}`
58. Verifikasi Borrow Log memuat penutupan pengajuan Extend oleh `System` dengan alasan `Asset reported missing`
59. Maya membatalkan laporan aset hilang atas baris aset `Laptop Dell Latitude 5420 - 68 {runId}`
60. Maya meminta data tab Borrowed
61. Verifikasi baris aset `Laptop Dell Latitude 5420 - 68 {runId}` tidak berstatus `Extension Request`, karena pengajuan tidak dipulihkan sesudah laporan dibatalkan

### Pengajuan Extend untuk beberapa baris diproses atomik per baris
62. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 96 {runId}` dengan Reason `Perpanjangan untuk pelatihan tim regional`
63. Maya mengajukan Extend sekaligus untuk baris aset `Laptop Dell Latitude 5420 - 96 {runId}` dan baris aset `Laptop Dell Latitude 5420 - 97 {runId}` dengan Reason `Perpanjangan untuk pelatihan lanjutan tim regional`
64. Verifikasi pengajuan untuk baris aset `Laptop Dell Latitude 5420 - 97 {runId}` diterima server sebagai pengajuan yang menunggu review
65. Verifikasi pengajuan untuk baris aset `Laptop Dell Latitude 5420 - 96 {runId}` ditolak server karena pengajuan sebelumnya masih menunggu
66. Maya meminta data tab Borrowed
67. Verifikasi baris aset `Laptop Dell Latitude 5420 - 97 {runId}` berstatus `Extension Request`
68. Verifikasi baris aset `Laptop Dell Latitude 5420 - 96 {runId}` tetap berstatus `Extension Request`
69. Gita meminta daftar pengajuan Extend yang menunggu review Aktor Borrow Group `Head Office`
70. Verifikasi daftar memuat satu pengajuan Extend untuk baris aset `Laptop Dell Latitude 5420 - 96 {runId}` dan satu pengajuan Extend untuk baris aset `Laptop Dell Latitude 5420 - 97 {runId}`

### Penarikan pengajuan Extend tercatat di Borrow Log
71. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 98 {runId}` dengan Reason `Perpanjangan untuk kegiatan bakti sosial`
72. Maya menarik pengajuan Extend baris aset `Laptop Dell Latitude 5420 - 98 {runId}` lewat Cancel Extension Request
73. Verifikasi penarikan pengajuan yang menunggu review diterima server
74. Gita meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 98 {runId}`
75. Verifikasi Borrow Log memuat satu node penarikan pengajuan Extend dengan Activity `Extension canceled`

### Laporan kerusakan menutup pengajuan Extend yang menunggu approval
76. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 99 {runId}` dengan Reason `Perpanjangan untuk proyek renovasi kantor`
77. Gita meneruskan pengajuan Extend baris aset `Laptop Dell Latitude 5420 - 99 {runId}` ke approval
78. Maya meminta data tab Borrowed
79. Verifikasi baris aset `Laptop Dell Latitude 5420 - 99 {runId}` berstatus `Extension Approval`
80. Maya mengirim laporan kerusakan atas baris aset `Laptop Dell Latitude 5420 - 99 {runId}`
81. Gita meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 99 {runId}`
82. Verifikasi Borrow Log memuat penutupan pengajuan Extend oleh `System` dengan alasan `Damage reported`
83. Maya meminta data tab Borrowed
84. Verifikasi baris aset `Laptop Dell Latitude 5420 - 99 {runId}` tidak lagi berstatus `Extension Approval`

### Laporan aset hilang menutup pengajuan Extend yang menunggu approval dan pengajuan tidak dipulihkan
85. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 100 {runId}` dengan Reason `Perpanjangan untuk acara pelatihan nasional`
86. Gita meneruskan pengajuan Extend baris aset `Laptop Dell Latitude 5420 - 100 {runId}` ke approval
87. Maya meminta data tab Borrowed
88. Verifikasi baris aset `Laptop Dell Latitude 5420 - 100 {runId}` berstatus `Extension Approval`
89. Maya mengirim laporan aset hilang atas baris aset `Laptop Dell Latitude 5420 - 100 {runId}`
90. Gita meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 100 {runId}`
91. Verifikasi Borrow Log memuat penutupan pengajuan Extend oleh `System` dengan alasan `Asset reported missing`
92. Maya membatalkan laporan aset hilang atas baris aset `Laptop Dell Latitude 5420 - 100 {runId}`
93. Maya meminta data tab Borrowed
94. Verifikasi baris aset `Laptop Dell Latitude 5420 - 100 {runId}` tidak berstatus `Extension Approval`, karena pengajuan tidak dipulihkan sesudah laporan dibatalkan

### Return kedua atas pinjaman self-service yang sudah Returned tidak diproses ulang
95. Maya mengembalikan aset baris `Laptop Dell Latitude 5420 - 101 {runId}` lewat Return pinjaman self-service
96. Maya meminta data tab History
97. Verifikasi baris aset `Laptop Dell Latitude 5420 - 101 {runId}` berstatus `Returned`
98. Maya mengirim Return kedua untuk baris aset `Laptop Dell Latitude 5420 - 101 {runId}` yang sudah `Returned`
99. Verifikasi Return kedua tidak diproses ulang oleh server
100. Maya meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 101 {runId}`
101. Verifikasi Borrow Log tetap memuat satu node `Returned via self-service`

### Pengajuan Extend yang berhasil tercatat di Borrow Log
102. Gita meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 97 {runId}`
103. Verifikasi Borrow Log memuat satu node `Extension requested`

### Laporan aset hilang ditolak Aktor Missing dan pengajuan Extend tidak dipulihkan
104. Maya mengajukan Extend untuk baris aset `Laptop Dell Latitude 5420 - 102 {runId}` dengan Reason `Perpanjangan untuk kegiatan studi banding`
105. Maya mengirim laporan aset hilang atas baris aset `Laptop Dell Latitude 5420 - 102 {runId}`
106. Gita meminta Borrow Log baris aset `Laptop Dell Latitude 5420 - 102 {runId}`
107. Verifikasi Borrow Log memuat penutupan pengajuan Extend oleh `System` dengan alasan `Asset reported missing`
108. Dewi menolak laporan aset hilang atas baris aset `Laptop Dell Latitude 5420 - 102 {runId}`
109. Maya meminta data tab Borrowed
110. Verifikasi baris aset `Laptop Dell Latitude 5420 - 102 {runId}` tidak berstatus `Extension Request`, karena pengajuan tidak dipulihkan sesudah laporan ditolak
