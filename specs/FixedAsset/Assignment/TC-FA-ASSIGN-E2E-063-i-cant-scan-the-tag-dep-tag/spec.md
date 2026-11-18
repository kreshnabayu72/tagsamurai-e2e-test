---
id: TC-FA-ASSIGN-E2E-063-i-cant-scan-the-tag-dep-tag
title: "I Can't Scan the TAG saat Handover dan Unassign"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [FI-ASG-25, FI-ASG-26, FI-ASG-27, FI-ASG-28, FI-ASG-29, FI-ASG-30, FI-ASG-31, FI-ASG-32, FI-ASG-33, FI-ASG-68, FI-ASG-69, EC-ASG-26, EC-ASG-72, F-ASSIGN-06.k7, F-ASSIGN-07.k4, "§9.7#r16", V-ASG-07]
smoke: []
dependsOn: ["Tag: Report TAG dan Replace TAG"]
trace:
  FI-ASG-25: 7
  FI-ASG-26: 6
  FI-ASG-27: 10
  FI-ASG-28: 10
  FI-ASG-29: [15, 18, 83, 86]
  FI-ASG-30: [20, 22]
  FI-ASG-31: [39, 42]
  FI-ASG-32: [29, 32]
  FI-ASG-33: 34
  FI-ASG-68: [53, 62, 63, 64, 68, 98, 101, 105]
  FI-ASG-69: 55
  EC-ASG-26: [53, 55]
  EC-ASG-72: [10, 15, 20, 22, 29, 34, 39]
  F-ASSIGN-06.k7: 34
  F-ASSIGN-07.k4: [53, 55, 62]
  "§9.7#r16": 67
  V-ASG-07: 112
anchor: [82, 85, 104]
coverage:
  web: manual
---
# I Can't Scan the TAG saat Handover dan Unassign

## Prerequisites
- Aktor: Aktor Assignment (Asset Admin `Dewi Lestari {runId}`, DU-063-1); Total Control `Fajar Nugroho {runId}` (DU-063-2) dan Group Manager `Rina Wijaya {runId}` (DU-063-9) sebagai aktor lain pada satu blok; Aktor Tag (DU-063-4) yang menyelesaikan Replace TAG.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-063-1: Karyawan `Dewi Lestari {runId}`, role Asset Admin, Group penugasan `Head Office`, Status `Active`.
  - DU-063-2: Karyawan `Fajar Nugroho {runId}`, role Total Control, Status `Active`.
  - DU-063-3: Karyawan `Budi Santoso {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee DU-063-5 dan DU-063-6.
  - DU-063-4: Karyawan `Maya Putri {runId}`, Status `Active`, pemegang hak Replace TAG pada Group `Head Office`.
  - DU-063-5: ASG `Waiting for Handover` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, Confirmation Rule `No`, Photo at start `OFF`, berisi aset `Laptop MSI Modern 14 {runId}` dengan TAG `QR-LPT-0014-{runId}` yang tidak terbaca (TAG pengganti `QR-LPT-0015-{runId}`) dan aset `Monitor HP E24 {runId}` dengan TAG `QR-MON-0021-{runId}` yang terbaca.
  - DU-063-6: ASG `Assigned` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, Photo at end `OFF`, berisi aset `Printer Canon G2020 {runId}` dengan dua TAG: `QR-PRN-0033-{runId}` yang rusak dan `RFID-PRN-0033-{runId}`.
  - DU-063-7: Aset `Scanner Zebra DS2208 {runId}`, Group `Head Office`, Custody `Available`, dengan TAG `QR-SCN-0040-{runId}` yang dilaporkan tidak terbaca dan belum diganti.
  - DU-063-8: Foto Unassign `foto-unassign-printer.jpg` untuk aset `Printer Canon G2020 {runId}`.
  - DU-063-9: Karyawan `Rina Wijaya {runId}`, role Group Manager, Group `Head Office`, Status `Active`.
  - DU-063-10: Karyawan `Citra Dewi {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee DU-063-12.
  - DU-063-11: Karyawan `Dimas Prasetyo {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee DU-063-13.
  - DU-063-12: ASG `Waiting for Handover` untuk Assignee `Citra Dewi {runId}`, Group `Head Office`, Confirmation Rule `Yes`, Photo at start `ON`, berisi aset `Kamera Mirrorless Canon EOS R50 {runId}` dengan TAG `QR-CAM-0050-{runId}` dan aset `Tablet Samsung Galaxy Tab S9 {runId}` dengan TAG `QR-TAB-0061-{runId}` yang terbaca.
  - DU-063-13: ASG `Assigned` untuk Assignee `Dimas Prasetyo {runId}`, Group `Head Office`, Photo at end `OFF`, berisi aset `Proyektor Epson EB-X06 {runId}` dengan TAG `QR-PRJ-0071-{runId}`.
  - DU-063-14 sampai DU-063-17: isian laporan TAG yang dibuat langkah (TAG, Report Type, dan Note).
- Kondisi:
  - Perangkat pindai TAG tersedia di sesi Aktor Assignment.

## Test Steps

### Scan TAG yang tidak terbaca ditolak dan Handover tidak dapat dimulai untuk aset itu
1. Ketik Search `Budi Santoso {runId}`, tekan Enter
2. Klik `⋯` pada baris ASG milik Assignee `Budi Santoso {runId}`
3. Klik `Hand Over`
4. Klik `[Verify Asset]`
5. Pindai TAG `QR-LPT-0014-{runId}` aset `Laptop MSI Modern 14 {runId}` yang tidak terbaca
6. Verifikasi toast `Error, this TAG can't be read. Report the TAG and use another asset.` tampil
7. Verifikasi baris aset `Laptop MSI Modern 14 {runId}` tetap `Unverified` sehingga Handover aset itu tidak dapat dimulai

### I Can't Scan the TAG membuka Dialog Report TAG biasa dan menonaktifkan baris
8. Klik `⋯` pada baris aset `Laptop MSI Modern 14 {runId}`
9. Klik `I Can't Scan the TAG`
10. Verifikasi Dialog Report TAG biasa tampil dengan pilihan Tag, Report Type bawaan `Unreadable`, dan Note
11. Centang TAG `QR-LPT-0014-{runId}`
12. Pilih Report Type `Unreadable`
13. Isi Note `TAG QR pada laptop tergores dan tidak terbaca`
14. Kirim dialog `Report TAG`
15. Verifikasi kolom Verification baris aset `Laptop MSI Modern 14 {runId}` menampilkan `TAG reported. Replace the TAG to hand over.`
16. Klik `[Verify Asset]`
17. Pindai TAG `QR-LPT-0014-{runId}` aset `Laptop MSI Modern 14 {runId}`
18. Verifikasi baris aset `Laptop MSI Modern 14 {runId}` tidak berstatus `Verified` setelah TAG dipindai

### Total Control dan Group Manager tidak dapat melewati laporan TAG
19. Total Control `Fajar Nugroho {runId}`: Buka halaman Hand Over untuk ASG milik Assignee `Budi Santoso {runId}`
20. Verifikasi baris aset `Laptop MSI Modern 14 {runId}` tetap nonaktif dengan teks `TAG reported. Replace the TAG to hand over.` untuk Total Control
21. Group Manager `Rina Wijaya {runId}`: Buka halaman Hand Over untuk ASG milik Assignee `Budi Santoso {runId}`
22. Verifikasi baris aset `Laptop MSI Modern 14 {runId}` tetap nonaktif dengan teks `TAG reported. Replace the TAG to hand over.` untuk Group Manager

### Aset lain di ASG yang sama tetap dapat diserahkan
23. Aktor Assignment `Dewi Lestari {runId}`: Buka halaman Hand Over untuk ASG milik Assignee `Budi Santoso {runId}`
24. Klik `[Verify Asset]`
25. Pindai TAG `QR-MON-0021-{runId}` aset `Monitor HP E24 {runId}`
26. Klik `[Complete Handover]`
27. Buka tab Assigned Assets di halaman Transactions > Assignment
28. Ketik Search `Monitor HP E24 {runId}`, tekan Enter
29. Verifikasi baris aset `Monitor HP E24 {runId}` berstatus `Assigned`
30. Buka tab Transactions di halaman Transactions > Assignment
31. Ketik Search `Laptop MSI Modern 14 {runId}`, tekan Enter
32. Verifikasi baris aset `Laptop MSI Modern 14 {runId}` tetap berstatus `Waiting for Handover`

### Assignment Log mencatat TAG yang dilaporkan
33. Klik aksi `Assignment Log` pada baris aset `Laptop MSI Modern 14 {runId}`
34. Verifikasi node `TAG reported by [Reporter]` dengan pelaku `Dewi Lestari {runId}` memuat daftar TAG `QR-LPT-0014-{runId}`
35. Tutup dialog `Assignment Log`

### Replace TAG mengembalikan baris ke Unverified dan dapat dipindai dengan TAG pengganti
36. Klik `⋯` pada baris ASG milik Assignee `Budi Santoso {runId}`
37. Klik `Hand Over`
38. Aktor Tag `Maya Putri {runId}`: Selesaikan Replace TAG aset `Laptop MSI Modern 14 {runId}` dengan TAG pengganti `QR-LPT-0015-{runId}`
39. Verifikasi baris aset `Laptop MSI Modern 14 {runId}` kembali `Unverified` tanpa membuka ulang halaman
40. Klik `[Verify Asset]`
41. Pindai TAG pengganti `QR-LPT-0015-{runId}` aset `Laptop MSI Modern 14 {runId}`
42. Verifikasi baris aset `Laptop MSI Modern 14 {runId}` berstatus `Verified`

### Unassign dengan identifikasi manual mewajibkan foto dan melaporkan hanya TAG tercentang
43. Buka tab Assigned Assets di halaman Transactions > Assignment
44. Ketik Search `Printer Canon G2020 {runId}`, tekan Enter
45. Klik `⋯` pada baris aset `Printer Canon G2020 {runId}`
46. Klik `Unassign`
47. Klik `⋯` pada baris aset `Printer Canon G2020 {runId}` di halaman Unassign
48. Klik `I Can't Scan the TAG`
49. Centang hanya TAG `QR-PRN-0033-{runId}`
50. Pilih Report Type `Unreadable`
51. Isi Note `TAG QR printer rusak, TAG RFID tidak dilaporkan`
52. Kirim dialog `Report TAG` varian identifikasi manual
53. Verifikasi baris aset `Printer Canon G2020 {runId}` berstatus `TAG Reported` dan tetap dapat dipindai
54. Klik `[Submit]` tanpa Unassign Photo
55. Verifikasi pesan `1 asset needs an unassign photo.` tampil di atas tombol meskipun Photo at end `OFF`
56. Unggah Unassign Photo `foto-unassign-printer.jpg` untuk aset `Printer Canon G2020 {runId}`
57. Klik `[Submit]`
58. Buka tab History di halaman Transactions > Assignment
59. Buka sub-tab By Asset
60. Ketik Search `Printer Canon G2020 {runId}`, tekan Enter
61. Klik aksi `Assignment Log` pada baris aset `Printer Canon G2020 {runId}`
62. Verifikasi node `TAG reported by [Reporter]` memuat daftar TAG `QR-PRN-0033-{runId}` tampil di Assignment Log
63. Verifikasi node `TAG reported by [Reporter]` memuat Report Type `Unreadable`
64. Verifikasi node `TAG reported by [Reporter]` tidak memuat TAG `RFID-PRN-0033-{runId}`
65. Tutup dialog `Assignment Log`
66. Buka antrean Reported TAGs
67. Verifikasi TAG `QR-PRN-0033-{runId}` tampil di antrean Reported TAGs
68. Verifikasi TAG `RFID-PRN-0033-{runId}` tidak tampil di antrean Reported TAGs

### Baris dengan laporan TAG nonaktif untuk foto dan Request Confirmation
69. Buka halaman Transactions > Assignment
70. Ketik Search `Citra Dewi {runId}`, tekan Enter
71. Klik `⋯` pada baris ASG milik Assignee `Citra Dewi {runId}`
72. Klik `Hand Over`
73. Klik `[Verify Asset]`
74. Pindai TAG `QR-TAB-0061-{runId}` aset `Tablet Samsung Galaxy Tab S9 {runId}`
75. Ambil foto untuk baris aset `Tablet Samsung Galaxy Tab S9 {runId}`
76. Klik `⋯` pada baris aset `Kamera Mirrorless Canon EOS R50 {runId}`
77. Klik `I Can't Scan the TAG`
78. Centang TAG `QR-CAM-0050-{runId}`
79. Pilih Report Type `Unreadable`
80. Isi Note `TAG QR pada kamera terkelupas`
81. Kirim dialog `Report TAG`
82. Verifikasi kolom Handover Photo baris aset `Tablet Samsung Galaxy Tab S9 {runId}` memuat foto yang diambil
83. Verifikasi baris aset `Kamera Mirrorless Canon EOS R50 {runId}` nonaktif untuk foto sehingga foto tidak dapat diambil untuk baris itu
84. Klik `[Request Confirmation]`
85. Verifikasi popup `Waiting for Confirmation` memuat aset `Tablet Samsung Galaxy Tab S9 {runId}`
86. Verifikasi popup `Waiting for Confirmation` tidak memuat aset `Kamera Mirrorless Canon EOS R50 {runId}`
87. Klik `[Cancel Request]`

### Scan berhasil membatalkan Report TAG dari identifikasi manual
88. Buka tab Assigned Assets di halaman Transactions > Assignment
89. Ketik Search `Proyektor Epson EB-X06 {runId}`, tekan Enter
90. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}`
91. Klik `Unassign`
92. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}` di halaman Unassign
93. Klik `I Can't Scan the TAG`
94. Centang TAG `QR-PRJ-0071-{runId}`
95. Pilih Report Type `Unreadable`
96. Isi Note `TAG QR proyektor terkelupas`
97. Kirim dialog `Report TAG` varian identifikasi manual
98. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` berstatus `TAG Reported`
99. Klik `[Verify Asset]`
100. Pindai TAG `QR-PRJ-0071-{runId}` aset `Proyektor Epson EB-X06 {runId}`
101. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` berstatus `Verified`
102. Klik `[Cancel]` pada halaman Unassign, lalu klik `[Leave]` pada dialog Unsaved Changes
103. Buka antrean Reported TAGs
104. Verifikasi TAG `QR-PRN-0033-{runId}` tampil di antrean Reported TAGs
105. Verifikasi TAG `QR-PRJ-0071-{runId}` tidak tampil di antrean Reported TAGs

### Aset dengan TAG yang belum diganti tidak dapat dipilih untuk Assign
106. Buka halaman Transactions > Assignment
107. Klik `[+ Assign]`
108. Klik `Employee` pada overlay `Assign to`
109. Klik `[+ Asset]`
110. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
111. Pilih baris aset `Scanner Zebra DS2208 {runId}`
112. Verifikasi pesan `This asset can't be assigned until its TAG is replaced.` dan tombol `[Report TAG]` tampil untuk aset `Scanner Zebra DS2208 {runId}`
