---
id: TC-FA-MYASSET-BE-207-laporan-damaged-missing-aturan-server-dep-borrow
title: "Aturan server laporan Damaged dan Missing dari My Asset beserta pembatalannya"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["ACT-MYA-01.<aksi>.<huruf>,ACT-MYA-02.<aksi>.<huruf>,ACT-MYA-04.<aksi>.<huruf>", "T-MYA-04", "§1.2#r36", "§1.2#r55", "§4.1b#r60", "§4.1b#r62", "§4.1b#r63", "§4.1b#r68", "§4.1b#r70", "§4.1b#r71", "§9.2#r10", "§9.2#r11", "§9.2#r13", "§9.2#r15", "§9.2#r18", "§9.2#r29", "§9.2#r30", "§9.2#r31", "§9.4.2#r62", "§9.4.2#r65", "§9.4.3#b6", "§9.6#r5", "§9.6#r8", "§9.6#r9", "EB-EDG-1"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment", "Damaged: keputusan Damage Report oleh Aktor Damaged", "Missing: keputusan laporan Missing oleh Aktor Missing"]
owner: BE
trace:
  "ACT-MYA-01.<aksi>.<huruf>,ACT-MYA-02.<aksi>.<huruf>,ACT-MYA-04.<aksi>.<huruf>": [7, 9, 13, 24, 26, 39, 49, 61, 63, 65, 67, 68, 70, 83, 86, 103, 105, 107, 109, 110, 113, 114, 126, 129, 137, 140]
  "T-MYA-04": [70, 75, 103, 105, 107, 109, 110, 113, 114]
  "§1.2#r36": [9, 11, 22, 28, 30, 32, 34, 73, 89, 91, 93, 95, 97, 99, 101]
  "§1.2#r55": [83, 84, 86, 87, 117, 119, 121, 123, 126, 127, 129, 130, 132, 134, 137, 138, 140, 141]
  "§4.1b#r60": [13, 83, 126, 127, 137, 138]
  "§4.1b#r62": 13
  "§4.1b#r63": 14
  "§4.1b#r68": [49, 86, 129, 130, 140, 141]
  "§4.1b#r70": 49
  "§4.1b#r71": 50
  "§9.2#r10": [39, 58]
  "§9.2#r11": [58, 59]
  "§9.2#r13": [41, 47]
  "§9.2#r15": 2
  "§9.2#r18": [36, 37]
  "§9.2#r29": 71
  "§9.2#r30": [75, 79, 80]
  "§9.2#r31": 77
  "§9.4.2#r62": 77
  "§9.4.2#r65": 71
  "§9.4.3#b6": [40, 58, 59]
  "§9.6#r5": [42, 43, 45]
  "§9.6#r8": [3, 4, 5, 7]
  "§9.6#r9": [15, 16, 19, 20, 51, 52, 55, 56, 111, 115]
  "EB-EDG-1": [7, 19, 20, 45, 55, 56, 103, 107]
---

# Aturan server laporan Damaged dan Missing dari My Asset beserta pembatalannya

## Prerequisites
- Aktor: Borrower dan Assignee Dewi (DU-207-1), Aktor Damaged Hendra (DU-207-2), Aktor Missing Maya (DU-207-3), Aktor Borrow dan Aktor Assignment Rina (DU-207-4), pemegang yang juga memegang hak Aktor Missing Agus (DU-207-5), PIC Division lama Budi (DU-207-6) dan PIC Division baru Siti (DU-207-7), PIC Borrower lama Wulan (DU-207-44) dan PIC Borrower baru Yoga (DU-207-45), serta admin Bambang (DU-207-46) yang mengelola karyawan dan akun login.
- Data:
  - DU-207-1: User: Name `Dewi Lestari {runId}`, Peran `Borrower dan Assignee tanpa hak Aktor Damaged dan Aktor Missing`.
  - DU-207-2: User: Name `Hendra Wijaya {runId}`, Peran `Aktor Damaged pada Group Head Office`.
  - DU-207-3: User: Name `Maya Anggraini {runId}`, Peran `Aktor Missing pada Group Head Office`.
  - DU-207-4: User: Name `Rina Wulandari {runId}`, Peran `Aktor Borrow dan Aktor Assignment pada Group Head Office`.
  - DU-207-5: User: Name `Agus Pratama {runId}`, Peran `Borrower dan Assignee yang juga memegang hak Aktor Missing pada Group Head Office`.
  - DU-207-6: User: Name `Budi Santoso {runId}`, Peran `PIC Division Finance tanpa hak Aktor Damaged dan Aktor Missing`.
  - DU-207-7: User: Name `Siti Nurhaliza {runId}`, Peran `pengganti PIC Division Finance tanpa hak Aktor Damaged dan Aktor Missing`.
  - DU-207-8: Division: Name `Finance {runId}`, PIC `Budi Santoso {runId}`.
  - DU-207-9: Pinjaman: Name `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Laporan `belum ada Damage Report dan belum ada laporan Missing`.
  - DU-207-10: Pinjaman: Name `Laptop Lenovo ThinkPad T14 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-207-11: Pinjaman: Name `Printer Epson L3250 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-207-12: Pinjaman: Name `Proyektor Epson EB-X06 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-207-13: Pinjaman: Name `Tablet Samsung Galaxy Tab A9 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-207-14: Pinjaman: Name `Kamera Canon EOS 200D {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Condition `Good`, Laporan `belum ada laporan Missing`.
  - DU-207-15: Pinjaman: Name `Drone DJI Mini 3 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Condition sebelum laporan `Good`, Condition saat ini bukan `Good` karena Missing record `Waiting for Confirmation` sudah mengubahnya, Missing `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-207-16: Pinjaman: Name `Laptop HP ProBook 450 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Agus Pratama {runId}`, Laporan `belum ada laporan Missing`.
  - DU-207-17: Penugasan: Name `Monitor Dell 24 Inci {runId}`, Group `Head Office`, Status `Assigned`, Assignee `Dewi Lestari {runId}`, Laporan `belum ada Damage Report dan belum ada laporan Missing`.
  - DU-207-18: Penugasan: Name `Monitor LG 27 Inci {runId}`, Group `Head Office`, Status `Assigned`, Assignee `Dewi Lestari {runId}`, Condition sebelum laporan `Good`, Condition saat ini bukan `Good` karena Missing record `Waiting for Confirmation` sudah mengubahnya, Missing `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-207-19: Penugasan: Name `Keyboard Logitech MX Keys {runId}`, Group `Head Office`, Status `Waiting for Handover`, Assignee `Dewi Lestari {runId}`.
  - DU-207-20: Penugasan: Name `Scanner Canon LiDE 300 {runId}`, Group `Head Office`, Status `Assigned`, Assignee `Dewi Lestari {runId}`, Laporan `belum ada Damage Report dan belum ada laporan Missing`.
  - DU-207-21: Penugasan: Name `Mouse Logitech MX Master 3 {runId}`, Group `Head Office`, Status `Assigned`, Assignee `Agus Pratama {runId}`, Laporan `belum ada Damage Report dan belum ada laporan Missing`.
  - DU-207-22: Penugasan: Assigned To `Finance {runId}`, PIC `Budi Santoso {runId}`, Aset 1 `Printer HP M404 {runId}`, Status Aset 1 `Assigned`, Damage Report Aset 1 `Waiting for Confirmation, dilaporkan Budi Santoso {runId}`, Aset 2 `Scanner Epson DS-530 {runId}`, Status Aset 2 `Assigned`, Missing Aset 2 `Waiting for Confirmation, dilaporkan Budi Santoso {runId}`.
  - DU-207-34: Pinjaman: Name `Speaker JBL Charge 5 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Damaged, dilaporkan Dewi Lestari {runId}, dikonfirmasi Hendra Wijaya {runId}`.
  - DU-207-35: Pinjaman: Name `Webcam Logitech C920 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Rejected, dilaporkan Dewi Lestari {runId}, ditolak Hendra Wijaya {runId}`.
  - DU-207-36: Pinjaman: Name `Headset Jabra Evolve 40 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Canceled, dilaporkan dan dibatalkan Dewi Lestari {runId}`.
  - DU-207-37: Pinjaman: Name `Mikrofon Shure SM58 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Repaired, dilaporkan Dewi Lestari {runId}`.
  - DU-207-38: Pinjaman: Name `Power Bank Anker PowerCore 20000 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Rejected, dilaporkan Dewi Lestari {runId}, ditolak Hendra Wijaya {runId}`, Laporan Missing `belum ada`.
  - DU-207-39: Pinjaman: Name `Smartwatch Samsung Galaxy Watch 6 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Canceled, dilaporkan dan dibatalkan Dewi Lestari {runId}`, Laporan Missing `belum ada`.
  - DU-207-40: Pinjaman: Name `Router TP-Link Archer C6 {runId}`, Group `Head Office`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Repaired, dilaporkan Dewi Lestari {runId}`, Laporan Missing `belum ada`.
  - DU-207-41: Extension Request: Reason `Kegiatan pelatihan lapangan diperpanjang satu pekan`.
  - DU-207-42: Extension Request: Reason `Pelatihan lapangan baru berakhir minggu depan`.
  - DU-207-43: Damage Report: Damaged Photo `monitor-penyangga-patah.jpg`, What happened `Kaki penyangga monitor patah, dilaporkan lagi`.
  - DU-207-44: User: Name `Wulan Prasetyo {runId}`, Peran `PIC Borrower tanpa hak Aktor Damaged dan Aktor Missing`.
  - DU-207-45: User: Name `Yoga Permana {runId}`, Peran `pengganti PIC Borrower tanpa hak Aktor Damaged dan Aktor Missing`.
  - DU-207-46: User: Name `Bambang Hartono {runId}`, Peran `admin yang mengelola karyawan dan akun login`.
  - DU-207-47: Karyawan: Name `Gunawan Setiadi {runId}`, Akun login `tidak ada`, PIC `Wulan Prasetyo {runId}`.
  - DU-207-48: Karyawan: Name `Lestari Wibowo {runId}`, Akun login `tidak ada`, PIC `Wulan Prasetyo {runId}`.
  - DU-207-49: Pinjaman: Name `Mesin Laminasi GBC {runId}`, Status `Borrowed`, Borrower `Gunawan Setiadi {runId}`, Laporan `belum ada Damage Report dan belum ada laporan Missing`.
  - DU-207-50: Pinjaman: Name `Hard Disk Eksternal WD 2TB {runId}`, Status `Borrowed`, Borrower `Gunawan Setiadi {runId}`, Laporan `belum ada Damage Report dan belum ada laporan Missing`.
  - DU-207-51: Pinjaman: Name `Speaker Konferensi Jabra 410 {runId}`, Status `Borrowed`, Borrower `Lestari Wibowo {runId}`, Laporan `belum ada Damage Report dan belum ada laporan Missing`.
  - DU-207-52: Pinjaman: Name `Alat Ukur Fluke 117 {runId}`, Status `Borrowed`, Borrower `Lestari Wibowo {runId}`, Laporan `belum ada Damage Report dan belum ada laporan Missing`.
  - DU-207-53: Damage Report: Damaged Photo `mesin-laminasi-roller-aus.jpg`, What happened `Roller mesin laminasi aus dan menggulung kertas`.
  - DU-207-54: Damage Report: Damaged Photo `speaker-konferensi-kabel-putus.jpg`, What happened `Kabel speaker konferensi putus dekat konektor`.
  - DU-207-55: Akun: Name `Lestari Wibowo {runId}`, Email `lestari.wibowo.{runId}@example.com`.

## Test Steps

### Report Damaged pada pinjaman dibuat, laporan ganda dan Report Missing atau Extend ditolak
1. Dewi mengirim Report Damaged atas pinjaman `Laptop Dell Latitude 5420 {runId}` dengan Damaged Photo `laptop-layar-retak.jpg` dan What happened `Layar laptop retak setelah terjatuh dari meja`
2. Verifikasi Damage Report atas aset `Laptop Dell Latitude 5420 {runId}` dibuat dengan status `Waiting for Confirmation`
3. Verifikasi laporan Damaged tercatat di Damaged log
4. Verifikasi laporan Damaged tercatat di Borrow Log pinjaman itu
5. Verifikasi status global aset sudah mengikuti Damage Report yang baru dibuat
6. Dewi mengirim Report Damaged kedua atas pinjaman yang sama dengan Damaged Photo `laptop-layar-retak.jpg` dan What happened `Layar laptop retak, dilaporkan lagi`
7. Verifikasi laporan ganda ditolak server dan aset tetap hanya punya satu Damage Report `Waiting for Confirmation`
8. Dewi mengirim Report Missing atas pinjaman yang sama
9. Verifikasi Report Missing ditolak server selama Damage Report `Waiting for Confirmation` dan tidak ada Missing record yang dibuat
10. Dewi mengajukan Extend atas pinjaman yang sama dengan Reason `Proyek audit lapangan belum selesai`
11. Verifikasi pengajuan Extend ditolak server selama Damage Report `Waiting for Confirmation`

### Cancel Damage Report oleh pelapor: laporan Canceled, status global dihitung ulang, tidak diproses ulang
12. Dewi mengirim Cancel Damage Report atas laporan Damaged pada `Laptop Lenovo ThinkPad T14 {runId}`
13. Verifikasi laporan Damaged pada aset itu menjadi `Canceled` karena dibatalkan pelapornya sendiri
14. Verifikasi status global aset dihitung ulang sesudah pembatalan
15. Verifikasi pembatalan tercatat di Damaged log
16. Verifikasi pembatalan tercatat di Borrow Log pinjaman itu
17. Catat jumlah entri pembatalan laporan di Damaged log untuk aset itu
18. Dewi mengirim Cancel Damage Report kedua atas laporan yang sama
19. Verifikasi laporan itu tetap `Canceled` dan tidak diproses ulang
20. Verifikasi jumlah entri pembatalan di Damaged log sama dengan jumlah yang dicatat
21. Dewi mengirim Report Damaged baru atas aset yang sama dengan Damaged Photo `laptop-keyboard-rusak.jpg` dan What happened `Beberapa tombol keyboard tidak berfungsi`
22. Verifikasi Damage Report baru diterima sesudah laporan sebelumnya `Canceled`, dengan status `Waiting for Confirmation`

### Keputusan Damage Report mengubah laporan yang diterima: Damaged dan Rejected
23. Hendra mengonfirmasi Damage Report pada `Printer Epson L3250 {runId}`
24. Verifikasi record Damage Report itu menjadi `Damaged`
25. Dewi mengirim Cancel Damage Report atas laporan itu
26. Verifikasi Cancel Damage Report ditolak server karena record sudah `Damaged`
27. Dewi mengirim Report Damaged atas aset yang sama dengan Damaged Photo `printer-roller-aus.jpg` dan What happened `Roller printer aus`
28. Verifikasi Report Damaged ditolak server selama record `Damaged`
29. Dewi mengirim Report Missing atas pinjaman `Printer Epson L3250 {runId}`
30. Verifikasi Missing record `Waiting for Confirmation` dibuat sesudah Damage Report menjadi `Damaged`
31. Hendra menolak Damage Report pada `Proyektor Epson EB-X06 {runId}`
32. Verifikasi record Damage Report itu menjadi `Rejected`
33. Dewi mengirim Report Damaged atas aset yang sama dengan Damaged Photo `proyektor-lensa-buram.jpg` dan What happened `Lensa proyektor buram`
34. Verifikasi Damage Report baru diterima sesudah `Rejected`, dengan status `Waiting for Confirmation`

### Return pinjaman yang punya Damage Report meninggalkan marker Damaged
35. Rina melakukan Return atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}`
36. Verifikasi baris pinjaman itu menjadi `Returned` bermarker `Damaged`
37. Verifikasi marker `Damaged` pada baris `Returned` tertaut ke Damage Report yang dilaporkan Dewi

### Report Missing pinjaman oleh pemegang tanpa hak Aktor Missing
38. Dewi mengirim Report Missing atas pinjaman `Kamera Canon EOS 200D {runId}`
39. Verifikasi Missing record dibuat dengan status `Waiting for Confirmation`
40. Verifikasi baris pinjaman tetap `Borrowed` dan tidak ditutup sebelum Aktor Missing mengonfirmasi
41. Verifikasi pengingat atas baris itu dijeda selama laporan Missing menunggu keputusan
42. Verifikasi laporan Missing tercatat di Missing log
43. Verifikasi Condition aset berubah dari `Good` bersama pembuatan Missing record
44. Dewi mengirim Report Missing kedua atas pinjaman yang sama
45. Verifikasi laporan Missing ganda ditolak server dan aset tetap hanya punya satu Missing record `Waiting for Confirmation`
46. Maya menolak laporan Missing pada pinjaman itu
47. Verifikasi pengingat atas baris itu berjalan lagi sesudah Aktor Missing menolak laporan

### Cancel Missing Report oleh pelapor memulihkan Condition aset
48. Dewi mengirim Cancel Missing Report atas laporan Missing pada `Drone DJI Mini 3 {runId}`
49. Verifikasi laporan Missing pada aset itu menjadi `Canceled`
50. Verifikasi Condition aset kembali ke `Good`, nilai sebelum laporan, dari Condition yang sebelumnya berubah oleh Missing record
51. Verifikasi pembatalan tercatat di Missing log
52. Verifikasi pembatalan tercatat di Borrow Log pinjaman itu
53. Catat jumlah entri pembatalan laporan di Missing log untuk aset itu
54. Dewi mengirim Cancel Missing Report kedua atas laporan yang sama
55. Verifikasi laporan itu tetap `Canceled` dan tidak diproses ulang
56. Verifikasi jumlah entri pembatalan di Missing log sama dengan jumlah yang dicatat

### Report Missing pinjaman oleh pemegang dengan hak Aktor Missing
57. Agus mengirim Report Missing atas pinjaman `Laptop HP ProBook 450 {runId}`
58. Verifikasi record Missing langsung berstatus `Missing`, tanpa melewati `Waiting for Confirmation`
59. Verifikasi baris pinjaman ditutup `Returned` bermarker `Missing` dan baris berpindah ke tab History

### Report Damaged pada baris Assigned: syarat, kelengkapan, dan hasil
60. Dewi mengirim Report Damaged atas `Keyboard Logitech MX Keys {runId}` dengan Damaged Photo `keyboard-tombol-lepas.jpg` dan What happened `Tombol keyboard lepas`
61. Verifikasi Report Damaged ditolak server karena baris belum berstatus `Assigned`
62. Dewi mengirim Report Damaged atas `Monitor LG 27 Inci {runId}` dengan Damaged Photo `monitor-panel-bergaris.jpg` dan What happened `Panel monitor bergaris`
63. Verifikasi Report Damaged ditolak server karena baris itu sudah punya laporan Missing
64. Dewi mengirim Report Damaged atas `Monitor Dell 24 Inci {runId}` dengan What happened `Kaki penyangga monitor patah`, tanpa Damaged Photo
65. Verifikasi Report Damaged ditolak server karena Damaged Photo wajib
66. Dewi mengirim Report Damaged atas `Monitor Dell 24 Inci {runId}` dengan Damaged Photo `monitor-penyangga-patah.jpg`, tanpa What happened
67. Verifikasi Report Damaged ditolak server karena What happened wajib
68. Verifikasi aset `Monitor Dell 24 Inci {runId}` belum punya Damage Report sesudah dua penolakan itu
69. Dewi mengirim Report Damaged atas `Monitor Dell 24 Inci {runId}` dengan Damaged Photo `monitor-penyangga-patah.jpg` dan What happened `Kaki penyangga monitor patah`
70. Verifikasi Damage Report dibuat dengan status `Waiting for Confirmation` dan Source `Assigned asset`
71. Verifikasi baris tetap `Assigned` dan aset tetap dipegang Dewi
72. Dewi mengirim Report Missing atas `Monitor Dell 24 Inci {runId}`
73. Verifikasi Report Missing ditolak server selama Damage Report `Waiting for Confirmation`

### Report Missing pada baris Assigned dibuat dan dikonfirmasi
74. Dewi mengirim Report Missing atas `Scanner Canon LiDE 300 {runId}`
75. Verifikasi Missing record dibuat dengan status `Waiting for Confirmation` dan baris tetap `Assigned`
76. Maya mengonfirmasi laporan Missing pada aset itu
77. Verifikasi baris keluar dari penugasan aktif dengan status `Unassigned` bermarker `Missing`
78. Agus mengirim Report Missing atas `Mouse Logitech MX Master 3 {runId}`
79. Verifikasi record Missing langsung berstatus `Missing`, tanpa melewati `Waiting for Confirmation`
80. Verifikasi baris penugasan ditutup dan baris berpindah ke tab History

### Pelapor tercatat: pemegang baru tidak membatalkan laporan PIC lama
81. Rina mengubah PIC penugasan Division `Finance {runId}` dari Budi menjadi Siti lewat Change PIC
82. Siti mengirim Cancel Damage Report atas laporan Damaged pada `Printer HP M404 {runId}`
83. Verifikasi Cancel Damage Report ditolak server karena Siti bukan pelapor tercatat
84. Verifikasi laporan Damaged itu tetap `Waiting for Confirmation` dan menunggu keputusan Aktor Damaged
85. Siti mengirim Cancel Missing Report atas laporan Missing pada `Scanner Epson DS-530 {runId}`
86. Verifikasi Cancel Missing Report ditolak server karena Siti bukan pelapor tercatat
87. Verifikasi laporan Missing itu tetap `Waiting for Confirmation` dan menunggu keputusan Aktor Missing

### Extend ditolak selama Damage Report Damaged dan diterima lagi sesudah Rejected, Canceled, atau Repaired
88. Dewi mengajukan Extend atas pinjaman `Speaker JBL Charge 5 {runId}` dengan Reason `Kegiatan pelatihan lapangan diperpanjang satu pekan`
89. Verifikasi pengajuan Extend ditolak server selama Damage Report `Damaged` dan tidak ada pengajuan Extend yang dibuat
90. Dewi mengajukan Extend atas pinjaman `Webcam Logitech C920 {runId}` dengan Reason `Pelatihan lapangan baru berakhir minggu depan`
91. Verifikasi pengajuan Extend diterima server sesudah Damage Report `Rejected`
92. Dewi mengajukan Extend atas pinjaman `Headset Jabra Evolve 40 {runId}` dengan Reason `Pelatihan lapangan baru berakhir minggu depan`
93. Verifikasi pengajuan Extend diterima server sesudah Damage Report `Canceled`
94. Dewi mengajukan Extend atas pinjaman `Mikrofon Shure SM58 {runId}` dengan Reason `Pelatihan lapangan baru berakhir minggu depan`
95. Verifikasi pengajuan Extend diterima server sesudah Damage Report `Repaired`

### Report Missing diterima lagi sesudah Damage Report Rejected, Canceled, atau Repaired
96. Dewi mengirim Report Missing atas pinjaman `Power Bank Anker PowerCore 20000 {runId}`
97. Verifikasi Missing record dibuat dengan status `Waiting for Confirmation` sesudah Damage Report `Rejected`
98. Dewi mengirim Report Missing atas pinjaman `Smartwatch Samsung Galaxy Watch 6 {runId}`
99. Verifikasi Missing record dibuat dengan status `Waiting for Confirmation` sesudah Damage Report `Canceled`
100. Dewi mengirim Report Missing atas pinjaman `Router TP-Link Archer C6 {runId}`
101. Verifikasi Missing record dibuat dengan status `Waiting for Confirmation` sesudah Damage Report `Repaired`

### Laporan ganda pada baris Assigned, serta Report Missing pada baris belum Assigned atau yang sudah punya laporan Missing, ditolak
102. Dewi mengirim Report Damaged kedua atas `Monitor Dell 24 Inci {runId}` dengan Damaged Photo `monitor-penyangga-patah.jpg` dan What happened `Kaki penyangga monitor patah, dilaporkan lagi`
103. Verifikasi Report Damaged ganda ditolak server karena baris itu sudah punya Damage Report dan aset tetap hanya punya satu Damage Report `Waiting for Confirmation`
104. Dewi mengirim Report Missing atas `Keyboard Logitech MX Keys {runId}`
105. Verifikasi Report Missing ditolak server karena baris belum berstatus `Assigned` dan tidak ada Missing record yang dibuat
106. Dewi mengirim Report Missing kedua atas `Monitor LG 27 Inci {runId}`
107. Verifikasi Report Missing ganda ditolak server dan aset tetap hanya punya satu Missing record `Waiting for Confirmation`

### Cancel Damage Report oleh pelapor pada baris Assigned: laporan Canceled dan status global dihitung ulang
108. Dewi mengirim Cancel Damage Report atas laporan Damaged pada `Monitor Dell 24 Inci {runId}`
109. Verifikasi laporan Damaged pada aset itu menjadi `Canceled` karena dibatalkan pelapornya sendiri
110. Verifikasi status global aset dihitung ulang sesudah pembatalan
111. Verifikasi pembatalan laporan Damaged tercatat di Assignment Log penugasan itu

### Cancel Missing Report oleh pelapor pada baris Assigned memulihkan Condition aset
112. Dewi mengirim Cancel Missing Report atas laporan Missing pada `Monitor LG 27 Inci {runId}`
113. Verifikasi laporan Missing pada aset itu menjadi `Canceled`
114. Verifikasi Condition aset kembali ke `Good`, nilai sebelum laporan, dari Condition yang sebelumnya berubah oleh Missing record
115. Verifikasi pembatalan laporan Missing tercatat di Assignment Log penugasan itu

### Laporan PIC lama diputuskan Aktor Damaged dan Aktor Missing sesudah pergantian PIC
116. Hendra mengonfirmasi Damage Report pada `Printer HP M404 {runId}`
117. Verifikasi record Damage Report itu menjadi `Damaged` walau PIC pelapornya sudah diganti
118. Maya mengonfirmasi laporan Missing pada `Scanner Epson DS-530 {runId}`
119. Verifikasi record Missing itu dikonfirmasi menjadi `Missing` walau PIC pelapornya sudah diganti

### PIC Borrower diganti: PIC baru tidak membatalkan laporan PIC lama atas nama Borrower tanpa akun
120. Wulan mengirim Report Damaged atas nama Gunawan untuk pinjaman `Mesin Laminasi GBC {runId}` dengan Damaged Photo `mesin-laminasi-roller-aus.jpg` dan What happened `Roller mesin laminasi aus dan menggulung kertas`
121. Verifikasi Damage Report atas `Mesin Laminasi GBC {runId}` dibuat dengan status `Waiting for Confirmation` dan pelapor tercatat `Wulan Prasetyo {runId}`
122. Wulan mengirim Report Missing atas nama Gunawan untuk pinjaman `Hard Disk Eksternal WD 2TB {runId}`
123. Verifikasi Missing record atas `Hard Disk Eksternal WD 2TB {runId}` dibuat dengan status `Waiting for Confirmation` dan pelapor tercatat `Wulan Prasetyo {runId}`
124. Bambang mengganti PIC Borrower `Gunawan Setiadi {runId}` dari Wulan menjadi Yoga
125. Yoga mengirim Cancel Damage Report atas laporan Damaged pada `Mesin Laminasi GBC {runId}`
126. Verifikasi Cancel Damage Report ditolak server karena Yoga bukan pelapor tercatat
127. Verifikasi laporan Damaged pada `Mesin Laminasi GBC {runId}` tetap `Waiting for Confirmation` dan menunggu keputusan Aktor Damaged
128. Yoga mengirim Cancel Missing Report atas laporan Missing pada `Hard Disk Eksternal WD 2TB {runId}`
129. Verifikasi Cancel Missing Report ditolak server karena Yoga bukan pelapor tercatat
130. Verifikasi laporan Missing pada `Hard Disk Eksternal WD 2TB {runId}` tetap `Waiting for Confirmation` dan menunggu keputusan Aktor Missing

### Borrower dibuatkan akun: Borrower tidak membatalkan laporan PIC lama
131. Wulan mengirim Report Damaged atas nama Lestari untuk pinjaman `Speaker Konferensi Jabra 410 {runId}` dengan Damaged Photo `speaker-konferensi-kabel-putus.jpg` dan What happened `Kabel speaker konferensi putus dekat konektor`
132. Verifikasi Damage Report atas `Speaker Konferensi Jabra 410 {runId}` dibuat dengan status `Waiting for Confirmation` dan pelapor tercatat `Wulan Prasetyo {runId}`
133. Wulan mengirim Report Missing atas nama Lestari untuk pinjaman `Alat Ukur Fluke 117 {runId}`
134. Verifikasi Missing record atas `Alat Ukur Fluke 117 {runId}` dibuat dengan status `Waiting for Confirmation` dan pelapor tercatat `Wulan Prasetyo {runId}`
135. Bambang membuatkan akun login untuk Borrower `Lestari Wibowo {runId}` dengan Email `lestari.wibowo.{runId}@example.com`
136. Lestari mengirim Cancel Damage Report atas laporan Damaged pada `Speaker Konferensi Jabra 410 {runId}`
137. Verifikasi Cancel Damage Report ditolak server karena Lestari bukan pelapor tercatat
138. Verifikasi laporan Damaged pada `Speaker Konferensi Jabra 410 {runId}` tetap `Waiting for Confirmation` dan menunggu keputusan Aktor Damaged
139. Lestari mengirim Cancel Missing Report atas laporan Missing pada `Alat Ukur Fluke 117 {runId}`
140. Verifikasi Cancel Missing Report ditolak server karena Lestari bukan pelapor tercatat
141. Verifikasi laporan Missing pada `Alat Ukur Fluke 117 {runId}` tetap `Waiting for Confirmation` dan menunggu keputusan Aktor Missing
