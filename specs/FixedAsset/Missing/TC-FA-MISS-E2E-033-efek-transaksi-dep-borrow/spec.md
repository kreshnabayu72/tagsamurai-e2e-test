---
id: TC-FA-MISS-E2E-033-efek-transaksi-dep-borrow
title: "Efek Missing pada Borrow: baris ditutup saat Report admin dan Confirm, baris tetap terbuka berbadge Reported Missing saat laporan pemegang, badge hilang saat Reject dan Found"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r39", "§1.2#r40", "§1.2#r41", "§1.2#r45", "§1.2#r46", "§1.2#r51", "§1.2#r55", "§1.2#r68", "§1.2#r67", "§9.2#b10", "§9.2#b11", "§9.2#b13", "§9.2#b26", "§9.2#b33", "§9.4.2#r3", "§9.4.2#r5", "§9.4.2#r6", "§9.4.2#r7", "§9.4.2#r16", "§9.4.3#b2", "§9.4.4#r12", "§9.4.4#r19", "§9.7#r1", "§9.7#r3", "§9.7#r4", "§9.7#r8", "§8.1#r9", "§11#r3", "§11#r18", "§3#p2", "§4.2.3#p2", "§2.1#b1", "§4.8#b1", "§2.1#b2", "§4.2.4#r15", "§9.4.1#r8", "§9.4.1#r13", "§9.7#r2"]
smoke: []
dependsOn: ["Borrow: halaman Borrow > aksi Report Missing", "Borrow: baris Waiting for handover dan Borrowed"]
trace:
  "§1.2#r39": [10, 22]
  "§1.2#r40": [10, 16]
  "§1.2#r41": [10]
  "§1.2#r45": [10]
  "§1.2#r46": [10, 16]
  "§1.2#r51": [16]
  "§1.2#r55": [32, 33, 45, 108]
  "§1.2#r68": [84, 88]
  "§1.2#r67": [89, 98]
  "§9.2#b10": [10]
  "§9.2#b11": [33]
  "§9.2#b13": [89]
  "§9.2#b26": [76, 77]
  "§9.2#b33": [40, 45, 55]
  "§9.4.2#r3": [16]
  "§9.4.2#r5": [76, 77]
  "§9.4.2#r6": [33, 45, 46]
  "§9.4.2#r7": [58, 59]
  "§9.4.2#r16": [89]
  "§9.4.3#b2": [32]
  "§9.4.4#r12": [76]
  "§9.4.4#r19": [40, 65]
  "§9.7#r1": [10]
  "§9.7#r3": [55, 58, 59]
  "§9.7#r4": [73, 76, 77]
  "§9.7#r8": [81, 82]
  "§8.1#r9": [41, 65]
  "§11#r3": [5, 10]
  "§11#r18": [3]
  "§3#p2": [9, 10, 21]
  "§4.2.3#p2": [5]
  "§2.1#b1": [21, 104]
  "§4.8#b1": [3, 104]
  "§2.1#b2": [3, 104]
  "§4.2.4#r15": [6]
  "§9.4.1#r8": [10, 16, 92, 93, 95]
  "§9.4.1#r13": [84, 89]
  "§9.7#r2": [25, 27, 29]
anchor: [97, 102]
coverage:
  web: automated
---

# Efek Missing pada Borrow: baris ditutup saat Report admin dan Confirm, baris tetap terbuka berbadge Reported Missing saat laporan pemegang, badge hilang saat Reject dan Found

## Prerequisites
- Aktor: Aktor Borrow tanpa Manage asset & TAG (Update) `Maya Putri {runId}`. Aktor lain: Total Control `Rina W`, pemegang `Joko Santoso {runId}` tanpa hak Aktor Missing, dan pengguna `Hendra Gunawan {runId}` yang bisa melihat halaman Borrow tanpa hak Aktor Borrow dan tanpa hak Aktor Missing.
- Layar awal: Borrow.
- Data:
  - DU-033-1: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Finance Room`, dengan baris Borrow berstatus `Borrowed` untuk peminjam `Joko Santoso {runId}`, tanpa record Missing.
  - DU-033-2: Asset `Hand Pallet Truck {runId}`, Group `Warehouse`, dengan baris Borrow berstatus `Waiting for handover` untuk peminjam `Joko Santoso {runId}`, tanpa record Missing.
  - DU-033-3: Asset `Scanner Zebra DS2208 {runId}`, Group `Warehouse`, dengan baris Borrow berstatus `Overdue` untuk peminjam `Joko Santoso {runId}` dan record Missing `Waiting for Confirmation` yang dilaporkan `Joko Santoso {runId}`.
  - DU-033-4: Asset `Monitor LG 27UL500 {runId}`, Group `Head Office`, dengan baris Borrow berstatus `Borrowed` untuk peminjam `Joko Santoso {runId}` dan record Missing `Waiting for Confirmation` yang dilaporkan `Joko Santoso {runId}`.
  - DU-033-5: Asset `Projector Epson EB-X06 {runId}`, Group `Head Office`, tanpa TAG, dengan baris Borrow berstatus `Borrowed` untuk peminjam `Joko Santoso {runId}` dan record Missing `Waiting for Confirmation` yang dilaporkan `Joko Santoso {runId}`.
  - DU-033-6: Asset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, dengan baris Borrow berstatus `Borrowed` untuk peminjam `Tono Wibowo {runId}` yang sudah dinonaktifkan dan record Missing `Waiting for Confirmation` yang dilaporkan `Tono Wibowo {runId}`.
  - DU-033-7: Asset `Camera Canon EOS {runId}`, Group `Head Office`, dengan baris Borrow berstatus `Borrowed` untuk peminjam `Joko Santoso {runId}` dan record Missing `Waiting for Confirmation` yang dilaporkan `Joko Santoso {runId}`.
  - DU-033-8: Pengguna `Maya Putri {runId}`, Aktor Borrow tanpa Manage asset & TAG (Update).
  - DU-033-9: Pengguna `Joko Santoso {runId}`, pemegang tanpa hak Aktor Missing.
  - DU-033-10: Pengguna `Tono Wibowo {runId}`, pemegang yang sudah dinonaktifkan.
  - DU-033-11: What happened `Laptop tidak dikembalikan dan tidak ditemukan di lokasi peminjam`.
  - DU-033-12: What happened `Hand pallet truck tidak diserahkan dan hilang dari gudang`.
  - DU-033-13: Reason `Aset masih dipakai di lapangan`.
  - DU-033-14: Note `Ditemukan di mobil operasional`.
  - DU-033-15: Asset `Tablet Samsung Galaxy Tab S8 {runId}`, Group `Head Office`, tercantum dalam Draft Borrow `Draft Peminjaman Tablet {runId}`, tanpa pemegang, tanpa record Missing.
  - DU-033-16: What happened `Tablet tidak ada di ruang rapat setelah sesi pelatihan`.
  - DU-033-17: Asset `Keyboard Logitech MX Keys {runId}`, Group `Head Office`, dengan baris Borrow berstatus `Borrowed` untuk peminjam `Tono Wibowo {runId}` yang sudah dinonaktifkan, tanpa record Missing.
  - DU-033-18: Pengguna `Hendra Gunawan {runId}`, bisa melihat halaman Borrow, tanpa hak Aktor Borrow dan tanpa hak Aktor Missing.
- Kondisi:
  - Akun `Maya Putri {runId}`, `Joko Santoso {runId}`, `Hendra Gunawan {runId}`, dan `Rina W` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Aktor Borrow melaporkan baris Borrowed sebagai Pelapor admin
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
3. Verifikasi aksi `Report Missing` tampil pada menu
4. Klik `Report Missing`
5. Verifikasi kotak dampak memuat baris `Laptop Dell Latitude 5420 {runId}` diikuti `in`, nomor transaksi Borrow milik DU-033-1, dan `will be closed as missing.`
6. Verifikasi kotak dampak memuat baris pemegang `Joko Santoso {runId}` diikuti `and the asset admins will be notified.`
7. Isi What happened `Laptop tidak dikembalikan dan tidak ditemukan di lokasi peminjam`
8. Klik `[Report Missing]` pada dialog
9. Verifikasi toast `Success, asset has been reported missing.` tampil
10. Verifikasi baris Borrow `Laptop Dell Latitude 5420 {runId}` ditutup sebagai `Returned` dengan marker `Missing`

### Baris Waiting for handover dibatalkan oleh sistem
11. Ganti isi kotak search dengan `Hand Pallet Truck {runId}`, tekan Enter
12. Buka menu `⋯` pada baris `Hand Pallet Truck {runId}`
13. Klik `Report Missing`
14. Isi What happened `Hand pallet truck tidak diserahkan dan hilang dari gudang`
15. Klik `[Report Missing]` pada dialog
16. Verifikasi baris Borrow `Hand Pallet Truck {runId}` berstatus `Canceled` dengan alasan `Asset reported missing` oleh `System`

### Laporan Aktor Borrow langsung berstatus Missing dengan Last holder
17. Masuk sebagai `Rina W`
18. Buka halaman `Assets`
19. Klik tab `Missing`
20. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
21. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berstatus `Missing`
22. Verifikasi kolom Last Holder pada baris itu `Joko Santoso {runId}`

### Laporan pemegang menampilkan badge Reported Missing di baris Borrow
23. Buka halaman `Borrow`
24. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
25. Verifikasi badge `Reported Missing` tampil pada baris Borrow `Scanner Zebra DS2208 {runId}`
26. Ganti isi kotak search dengan `Monitor LG 27UL500 {runId}`, tekan Enter
27. Verifikasi badge `Reported Missing` tampil pada baris Borrow `Monitor LG 27UL500 {runId}`
28. Ganti isi kotak search dengan `Projector Epson EB-X06 {runId}`, tekan Enter
29. Verifikasi badge `Reported Missing` tampil pada baris Borrow `Projector Epson EB-X06 {runId}`

### Laporan pemegang atas baris Overdue tidak menutup baris sampai Confirm
30. Buka halaman `Borrow`
31. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
32. Verifikasi baris Borrow `Scanner Zebra DS2208 {runId}` tetap berstatus `Overdue`
33. Verifikasi pengingat Overdue pada baris `Scanner Zebra DS2208 {runId}` berjalan seperti biasa, tidak dijeda
34. Buka halaman `Assets`
35. Klik tab `Missing`
36. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
37. Buka menu `⋯` pada baris `Scanner Zebra DS2208 {runId}`
38. Klik `Review`
39. Klik `[Confirm]` pada dialog Missing Log
40. Verifikasi toast `Success, report has been confirmed.` tampil
41. Verifikasi dialog Missing Log memuat node `Report confirmed by` oleh `Rina W` dengan Closed lines yang memuat nomor transaksi Borrow milik DU-033-3
42. Tutup dialog Missing Log dengan `✕`
43. Buka halaman `Borrow`
44. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
45. Verifikasi baris Borrow `Scanner Zebra DS2208 {runId}` ditutup sebagai `Returned` dengan marker `Missing`
46. Verifikasi keterlambatan pada baris Borrow `Scanner Zebra DS2208 {runId}` tetap tercatat

### Reject laporan pemegang menghilangkan badge Reported Missing dan baris tetap terbuka
47. Buka halaman `Assets`
48. Klik tab `Missing`
49. Ketik Search `Monitor LG 27UL500 {runId}`, tekan Enter
50. Buka menu `⋯` pada baris `Monitor LG 27UL500 {runId}`
51. Klik `Review`
52. Klik `[Reject]` pada dialog Missing Log
53. Isi Reason `Aset masih dipakai di lapangan`
54. Klik `[Reject]` pada dialog Reject Report
55. Verifikasi toast `Success, report has been rejected.` tampil
56. Buka halaman `Borrow`
57. Ketik Search `Monitor LG 27UL500 {runId}`, tekan Enter
58. Verifikasi baris Borrow `Monitor LG 27UL500 {runId}` tetap berstatus `Borrowed`
59. Verifikasi badge `Reported Missing` tidak tampil pada baris Borrow `Monitor LG 27UL500 {runId}`
60. Buka halaman `Assets`
61. Klik tab `Missing`
62. Klik sub-tab `History`
63. Ketik Search `Monitor LG 27UL500 {runId}`, tekan Enter
64. Klik `Monitor LG 27UL500 {runId}` pada kolom Name
65. Verifikasi dialog Missing Log memuat node `Report rejected by` oleh `Rina W` dengan Reason `Aset masih dipakai di lapangan`
66. Tutup dialog Missing Log dengan `✕`

### Mark as Found atas laporan pemegang menghilangkan badge Reported Missing
67. Klik sub-tab `Active`
68. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
69. Buka menu `⋯` pada baris `Projector Epson EB-X06 {runId}`
70. Klik `Mark as Found`
71. Isi Note `Ditemukan di mobil operasional`
72. Klik `[Mark as Found]` pada dialog
73. Verifikasi toast `Success, asset has been marked as found.` tampil
74. Buka halaman `Borrow`
75. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
76. Verifikasi baris Borrow `Projector Epson EB-X06 {runId}` tetap berstatus `Borrowed`
77. Verifikasi badge `Reported Missing` tidak tampil pada baris Borrow `Projector Epson EB-X06 {runId}`

### Cancel Report oleh pelapor memulihkan pengingat baris
78. `Joko Santoso {runId}` membatalkan laporannya atas `Camera Canon EOS {runId}` lewat Cancel Report
79. Buka halaman `Borrow`
80. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
81. Verifikasi baris Borrow `Camera Canon EOS {runId}` tetap berstatus `Borrowed`
82. Verifikasi pengingat pada baris Borrow `Camera Canon EOS {runId}` berjalan lagi

### Laporan atas pemegang yang dinonaktifkan tidak menutup baris
83. Ganti isi kotak search dengan `Printer HP LaserJet M404 {runId}`, tekan Enter
84. Verifikasi baris Borrow `Printer HP LaserJet M404 {runId}` tetap berstatus `Borrowed`
85. Buka halaman `Assets`
86. Klik tab `Missing`
87. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
88. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Waiting for Confirmation`
89. Verifikasi kolom Last Holder pada baris itu `Tono Wibowo {runId}`

### Aset dalam Draft Borrow ditandai tidak tersedia tanpa mengubah Draft
90. Rina W melaporkan `Tablet Samsung Galaxy Tab S8 {runId}` hilang lewat Report Missing dengan What happened `Tablet tidak ada di ruang rapat setelah sesi pelatihan`
91. Buka Draft Borrow `Draft Peminjaman Tablet {runId}`
92. Verifikasi `Tablet Samsung Galaxy Tab S8 {runId}` ditandai ⚠ unavailable di Draft
93. Verifikasi `Tablet Samsung Galaxy Tab S8 {runId}` tetap tercantum di Draft
94. Klik `[Submit]` pada Draft
95. Verifikasi Submit Draft diblokir sampai aset `Tablet Samsung Galaxy Tab S8 {runId}` dikeluarkan

### Aset milik pemegang yang dinonaktifkan dengan laporan Waiting for Confirmation tidak masuk Return list offboarding
96. Buka Return list offboarding `Tono Wibowo {runId}`
97. Verifikasi `Keyboard Logitech MX Keys {runId}` masuk Return list offboarding `Tono Wibowo {runId}`
98. Verifikasi `Printer HP LaserJet M404 {runId}` tidak masuk Return list offboarding `Tono Wibowo {runId}`

### Pengguna tanpa hak aksi transaksi tidak melihat Report Missing di halaman Borrow
99. Masuk sebagai `Hendra Gunawan {runId}`
100. Buka halaman `Borrow`
101. Ketik Search `Keyboard Logitech MX Keys {runId}`, tekan Enter
102. Verifikasi baris Borrow `Keyboard Logitech MX Keys {runId}` tampil
103. Buka menu `⋯` pada baris `Keyboard Logitech MX Keys {runId}`
104. Verifikasi aksi `Report Missing` tidak tampil pada menu

### Pengingat baris Borrow berjalan seperti biasa sesudah Reject
105. Masuk sebagai `Rina W`
106. Buka halaman `Borrow`
107. Ketik Search `Monitor LG 27UL500 {runId}`, tekan Enter
108. Verifikasi pengingat pada baris Borrow `Monitor LG 27UL500 {runId}` berjalan seperti biasa sesudah laporan pemegang ditolak
