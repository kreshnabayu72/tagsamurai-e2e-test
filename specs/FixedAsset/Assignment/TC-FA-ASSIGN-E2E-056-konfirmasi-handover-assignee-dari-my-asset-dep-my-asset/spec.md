---
id: TC-FA-ASSIGN-E2E-056-konfirmasi-handover-assignee-dari-my-asset-dep-my-asset
title: "Assignee atau PIC mengonfirmasi handover dari My Asset"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [F-ASSIGN-11, "§4.1h#p1", "§4.1h#r1", "§4.1h#r2", "§4.1h#r3", "§4.1h#r4", "§4.1h#r5", "§4.1#r20", FI-ASG-34, FI-ASG-35, FI-ASG-36, TS-ASG-31, DO-ASG-07, EC-ASG-108]
smoke: []
dependsOn: ["My Asset: tab Task, Assigned, History, dan dialog Confirm Handover"]
trace:
  F-ASSIGN-11: [11, 23]
  "§4.1h#p1": 11
  "§4.1h#r1": [11, 21, 73, 85]
  "§4.1h#r2": 13
  "§4.1h#r3": [23, 24, 57, 88, 89]
  "§4.1h#r4": [29, 30, 31, 103, 104]
  "§4.1h#r5": [26, 27, 94, 95, 100, 101]
  "§4.1#r20": 11
  FI-ASG-34: [14, 15]
  FI-ASG-35: 17
  FI-ASG-36: 53
  TS-ASG-31: [20, 43]
  DO-ASG-07: 71
  EC-ASG-108: 29
anchor: [66, 82, 90, 96]
coverage:
  web: automated
---
# Assignee atau PIC mengonfirmasi handover dari My Asset

## Prerequisites
- Aktor: Aktor Assignment (Asset Admin `Dewi Lestari {runId}`, DU-056-1) di sesi Admin; Assignee `Budi Santoso {runId}` (DU-056-2), `Sari Dewi {runId}` (DU-056-3), `Rina Wijaya {runId}` (DU-056-4), `Maya Putri {runId}` (DU-056-5), PIC Division `Hendra Kusuma {runId}` (DU-056-6), dan Assignee `Dian Pratama {runId}` (DU-056-16), masing-masing di sesinya sendiri.
- Layar awal: Transactions > Assignment (sesi Admin).
- Data:
  - DU-056-1: Karyawan `Dewi Lestari {runId}`, role Asset Admin, Group penugasan `Head Office`, Status `Active`.
  - DU-056-2: Karyawan `Budi Santoso {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login.
  - DU-056-3: Karyawan `Sari Dewi {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login.
  - DU-056-4: Karyawan `Rina Wijaya {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login.
  - DU-056-5: Karyawan `Maya Putri {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login.
  - DU-056-6: Karyawan `Hendra Kusuma {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, anggota Division `Finance {runId}`.
  - DU-056-7: Division `Finance {runId}` dengan PIC `Hendra Kusuma {runId}`.
  - DU-056-8: ASG `Waiting for Handover` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, Confirmation Rule `Yes`, Photo at start `OFF`, berisi aset `Laptop HP ProBook 450 {runId}` dan `Monitor Dell U2723 {runId}` dengan Purpose `Kerja harian`.
  - DU-056-9: ASG `Waiting for Handover` untuk Assignee `Sari Dewi {runId}`, Confirmation Rule `Yes`, Photo at start `OFF`, berisi aset `Tablet Samsung Galaxy Tab A9 {runId}` dengan Purpose `Survei lapangan`.
  - DU-056-10: ASG `Waiting for Handover` untuk Assignee Division `Finance {runId}` dengan PIC `Hendra Kusuma {runId}`, Confirmation Rule `Yes`, Photo at start `OFF`, berisi aset `Proyektor Epson EB-X49 {runId}` dengan Purpose `Presentasi laporan`.
  - DU-056-11: ASG `Waiting for Handover` untuk Assignee `Rina Wijaya {runId}`, Confirmation Rule `Yes`, Photo at start `OFF`, berisi aset `Printer HP LaserJet Pro {runId}` dengan Purpose `Cetak dokumen`.
  - DU-056-12: ASG `Waiting for Handover` untuk Assignee `Maya Putri {runId}`, Confirmation Rule `Yes`, Photo at start `OFF`, berisi aset `Scanner Fujitsu iX1300 {runId}` dengan Purpose `Arsip digital`.
  - DU-056-13: Riwayat penugasan Assignee `Budi Santoso {runId}` berstatus `Unassigned` untuk aset `Router Mikrotik hAP {runId}`.
  - DU-056-14: Riwayat penugasan Assignee `Budi Santoso {runId}` berstatus `Canceled` dengan reason `Not handed over` untuk aset `Switch TP-Link 8 Port {runId}`.
  - DU-056-15: Riwayat penugasan Assignee `Budi Santoso {runId}` berstatus `Rejected` dengan reason `Anggaran belum disetujui` untuk aset `Headset Logitech H390 {runId}`.
  - DU-056-16: Karyawan `Dian Pratama {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login.
  - DU-056-17: ASG `Waiting for Approval` untuk Assignee `Dian Pratama {runId}`, Group `Head Office`, berisi aset Category `Vehicle` `Mobil Toyota Avanza {runId}` dengan Purpose `Operasional kantor`.
  - DU-056-18: ASG `Waiting for Handover` untuk Assignee `Dian Pratama {runId}`, Group `Head Office`, Confirmation Rule `Yes`, Photo at start `OFF`, berisi aset `Mouse Logitech MX Master 3 {runId}` dengan Purpose `Desain grafis`.
  - DU-056-19: ASG `Assigned` untuk Assignee `Dian Pratama {runId}`, Group `Head Office`, berisi aset `Kamera Sony ZV-E10 {runId}` dengan Purpose `Dokumentasi kegiatan`; laporan Damaged milik `Dian Pratama {runId}` berstatus `Waiting for Confirmation` dengan What happened `Lensa tergores di bagian depan`.
  - DU-056-20: ASG `Assigned` untuk Assignee `Dian Pratama {runId}`, Group `Head Office`, berisi aset `Speaker Bluetooth JBL Flip 6 {runId}` dengan Purpose `Acara kantor`; laporan Missing milik `Dian Pratama {runId}` berstatus `Waiting for Confirmation` dengan Reason `Hilang saat kunjungan lapangan`.
  - DU-056-21: Riwayat penugasan Assignee `Dian Pratama {runId}` berstatus `Unassigned` dengan marker `Damaged` untuk aset `Drone DJI Mini 3 {runId}`.
  - DU-056-22: Riwayat penugasan Assignee `Dian Pratama {runId}` berstatus `Unassigned` dengan marker `Missing` untuk aset `Power Bank Anker 20000 {runId}`.
- Kondisi:
  - Akun semua Assignee dan PIC aktif dan kredensialnya disediakan fase 2.
  - Jendela konfirmasi Handover bernilai `15 menit`.

## Test Steps

### Task Confirm Handover muncul saat Request Confirmation
1. Admin: Ketik Search `Budi Santoso {runId}`, tekan Enter
2. Admin: Klik `⋯` pada baris ASG milik Assignee `Budi Santoso {runId}`
3. Admin: Klik `Hand Over`
4. Admin: Klik `[Verify Asset]`
5. Admin: Pindai TAG aset `Laptop HP ProBook 450 {runId}`
6. Admin: Klik `[Verify Asset]`
7. Admin: Pindai TAG aset `Monitor Dell U2723 {runId}`
8. Admin: Klik `[Request Confirmation]`
9. Assignee `Budi Santoso {runId}`: Buka My Asset lewat menu Profile
10. Assignee `Budi Santoso {runId}`: Buka tab `Task`
11. Verifikasi Task `Confirm Handover` tampil di tab `Task` untuk penugasan aset `Laptop HP ProBook 450 {runId}` dan `Monitor Dell U2723 {runId}`

### Dialog Confirm Handover dan pernyataan tanggung jawab
12. Assignee `Budi Santoso {runId}`: Klik Task `Confirm Handover`
13. Verifikasi dialog Confirm Handover memuat checklist aset `Laptop HP ProBook 450 {runId}` dan `Monitor Dell U2723 {runId}` beserta pernyataan tanggung jawab dan tombol `[Confirm]`
14. Verifikasi pernyataan tanggung jawab `I acknowledge receipt of these assets and accept responsibility for them.` tampil
15. Verifikasi tombol `[Confirm]` aktif sebelum pernyataan dicentang
16. Assignee `Budi Santoso {runId}`: Klik `[Confirm]` tanpa mencentang pernyataan
17. Verifikasi pesan `Check the statement to confirm.` tampil dan dialog Confirm Handover tetap terbuka

### Confirm menyerahkan semua aset sesi dan Task hilang
18. Assignee `Budi Santoso {runId}`: Centang pernyataan tanggung jawab
19. Assignee `Budi Santoso {runId}`: Klik `[Confirm]`
20. Verifikasi toast `Success, 2 assets have been handed over.`
21. Verifikasi Task `Confirm Handover` tidak tampil di tab `Task` setelah Confirm

### Tab Assigned menampilkan aset yang baru diserahkan dan aksi Assignee
22. Assignee `Budi Santoso {runId}`: Buka tab `Assigned`
23. Verifikasi baris `Laptop HP ProBook 450 {runId}` dan `Monitor Dell U2723 {runId}` tampil berstatus `Assigned`
24. Verifikasi baris `Router Mikrotik hAP {runId}` yang sudah `Unassigned` tidak tampil di tab `Assigned`
25. Assignee `Budi Santoso {runId}`: Klik `⋯` pada baris `Laptop HP ProBook 450 {runId}`
26. Verifikasi aksi `Report Damaged` dan `Report Missing` tersedia untuk baris `Laptop HP ProBook 450 {runId}`
27. Verifikasi aksi `Unassign`, `Cancel Assignment`, dan permintaan Unassign tidak tersedia untuk baris `Laptop HP ProBook 450 {runId}`

### Tab History menampilkan riwayat penugasan
28. Assignee `Budi Santoso {runId}`: Buka tab `History`
29. Verifikasi baris `Router Mikrotik hAP {runId}` tampil berstatus `Unassigned` dengan Type `Assignment`
30. Verifikasi baris `Switch TP-Link 8 Port {runId}` tampil berstatus `Canceled` dengan Type `Assignment` dan reason `Not handed over`
31. Verifikasi baris `Headset Logitech H390 {runId}` tampil berstatus `Rejected` dengan Type `Assignment` dan reason `Anggaran belum disetujui`

### Assignee dengan satu aset menerima toast bentuk tunggal
32. Admin: Ketik Search `Sari Dewi {runId}`, tekan Enter
33. Admin: Klik `⋯` pada baris ASG milik Assignee `Sari Dewi {runId}`
34. Admin: Klik `Hand Over`
35. Admin: Klik `[Verify Asset]`
36. Admin: Pindai TAG aset `Tablet Samsung Galaxy Tab A9 {runId}`
37. Admin: Klik `[Request Confirmation]`
38. Assignee `Sari Dewi {runId}`: Buka My Asset lewat menu Profile
39. Assignee `Sari Dewi {runId}`: Buka tab `Task`
40. Assignee `Sari Dewi {runId}`: Klik Task `Confirm Handover`
41. Assignee `Sari Dewi {runId}`: Centang pernyataan tanggung jawab
42. Assignee `Sari Dewi {runId}`: Klik `[Confirm]`
43. Verifikasi toast `Success, 1 asset has been handed over.`

### PIC Division mengonfirmasi atas nama Division
44. Admin: Ketik Search `Finance {runId}`, tekan Enter
45. Admin: Klik `⋯` pada baris ASG milik Assignee `Finance {runId}`
46. Admin: Klik `Hand Over`
47. Admin: Klik `[Verify Asset]`
48. Admin: Pindai TAG aset `Proyektor Epson EB-X49 {runId}`
49. Admin: Klik `[Request Confirmation]`
50. PIC `Hendra Kusuma {runId}`: Buka My Asset lewat menu Profile
51. PIC `Hendra Kusuma {runId}`: Buka tab `Task`
52. PIC `Hendra Kusuma {runId}`: Klik Task `Confirm Handover`
53. Verifikasi pernyataan tanggung jawab `I acknowledge receipt of these assets on behalf of [Division] and accept responsibility for them.` tampil dengan nama `Finance {runId}`
54. PIC `Hendra Kusuma {runId}`: Centang pernyataan tanggung jawab
55. PIC `Hendra Kusuma {runId}`: Klik `[Confirm]`
56. PIC `Hendra Kusuma {runId}`: Buka tab `Assigned`
57. Verifikasi baris `Proyektor Epson EB-X49 {runId}` tampil berstatus `Assigned` dengan penanda atas nama `Finance {runId}`

### Cancel Request menutup Task dan Confirm yang tertunda ditolak
58. Admin: Ketik Search `Rina Wijaya {runId}`, tekan Enter
59. Admin: Klik `⋯` pada baris ASG milik Assignee `Rina Wijaya {runId}`
60. Admin: Klik `Hand Over`
61. Admin: Klik `[Verify Asset]`
62. Admin: Pindai TAG aset `Printer HP LaserJet Pro {runId}`
63. Admin: Klik `[Request Confirmation]`
64. Assignee `Rina Wijaya {runId}`: Buka My Asset lewat menu Profile
65. Assignee `Rina Wijaya {runId}`: Buka tab `Task`
66. Verifikasi Task `Confirm Handover` tampil di tab `Task` untuk aset `Printer HP LaserJet Pro {runId}` selama sesi berjalan
67. Assignee `Rina Wijaya {runId}`: Klik Task `Confirm Handover`
68. Assignee `Rina Wijaya {runId}`: Centang pernyataan tanggung jawab
69. Admin: Klik `[Cancel Request]` pada popup `Waiting for Confirmation`
70. Assignee `Rina Wijaya {runId}`: Klik `[Confirm]` pada dialog Confirm Handover yang masih terbuka
71. Verifikasi dialog `Handover No Longer Available` tampil
72. Assignee `Rina Wijaya {runId}`: Tutup dialog `Handover No Longer Available`
73. Verifikasi Task `Confirm Handover` tidak tampil di tab `Task` setelah Admin menekan `[Cancel Request]`

### Task hilang saat jendela konfirmasi habis
74. Admin: Ketik Search `Maya Putri {runId}`, tekan Enter
75. Admin: Klik `⋯` pada baris ASG milik Assignee `Maya Putri {runId}`
76. Admin: Klik `Hand Over`
77. Admin: Klik `[Verify Asset]`
78. Admin: Pindai TAG aset `Scanner Fujitsu iX1300 {runId}`
79. Admin: Klik `[Request Confirmation]`
80. Assignee `Maya Putri {runId}`: Buka My Asset lewat menu Profile
81. Assignee `Maya Putri {runId}`: Buka tab `Task`
82. Verifikasi Task `Confirm Handover` tampil di tab `Task` untuk aset `Scanner Fujitsu iX1300 {runId}` selama jendela konfirmasi berjalan
83. Waktu berlalu sampai jendela konfirmasi `15 menit` habis sejak `[Request Confirmation]` ditekan
84. Assignee `Maya Putri {runId}`: Muat ulang halaman
85. Verifikasi Task `Confirm Handover` tidak tampil di tab `Task` setelah jendela konfirmasi habis

### Baris penugasan aktif tampil dengan status per baris
86. Assignee `Dian Pratama {runId}`: Buka My Asset lewat menu Profile
87. Assignee `Dian Pratama {runId}`: Buka tab `Assigned`
88. Verifikasi baris `Mobil Toyota Avanza {runId}` tampil berstatus `Waiting for Approval`
89. Verifikasi baris `Mouse Logitech MX Master 3 {runId}` tampil berstatus `Waiting for Handover`

### Assignee membatalkan laporan Damaged miliknya
90. Verifikasi baris `Kamera Sony ZV-E10 {runId}` memuat badge `Reported Damaged`
91. Assignee `Dian Pratama {runId}`: Klik `⋯` pada baris `Kamera Sony ZV-E10 {runId}`
92. Assignee `Dian Pratama {runId}`: Klik `Cancel Damage Report`
93. Assignee `Dian Pratama {runId}`: Konfirmasi pembatalan pada dialog Cancel Damage Report
94. Verifikasi badge `Reported Damaged` tidak tampil pada baris `Kamera Sony ZV-E10 {runId}`
95. Verifikasi baris `Kamera Sony ZV-E10 {runId}` tetap berstatus `Assigned`

### Assignee membatalkan laporan Missing miliknya
96. Verifikasi baris `Speaker Bluetooth JBL Flip 6 {runId}` memuat badge `Reported Missing`
97. Assignee `Dian Pratama {runId}`: Klik `⋯` pada baris `Speaker Bluetooth JBL Flip 6 {runId}`
98. Assignee `Dian Pratama {runId}`: Klik `Cancel Missing Report`
99. Assignee `Dian Pratama {runId}`: Konfirmasi pembatalan pada dialog Cancel Missing Report
100. Verifikasi badge `Reported Missing` tidak tampil pada baris `Speaker Bluetooth JBL Flip 6 {runId}`
101. Verifikasi baris `Speaker Bluetooth JBL Flip 6 {runId}` tetap berstatus `Assigned`

### Riwayat Unassigned bermarker Damaged atau Missing
102. Assignee `Dian Pratama {runId}`: Buka tab `History`
103. Verifikasi baris `Drone DJI Mini 3 {runId}` tampil berstatus `Unassigned` dengan marker `Damaged`
104. Verifikasi baris `Power Bank Anker 20000 {runId}` tampil berstatus `Unassigned` dengan marker `Missing`
