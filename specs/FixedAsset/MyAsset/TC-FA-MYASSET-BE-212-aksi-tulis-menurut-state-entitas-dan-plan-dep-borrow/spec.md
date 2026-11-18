---
id: TC-FA-MYASSET-BE-212-aksi-tulis-menurut-state-entitas-dan-plan-dep-borrow
title: "Aksi tulis My Asset saat entitas Suspended atau Expired, dan Extend sesudah downgrade plan"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.4.1#r1", "§9.4.2#r79", "§9.4.2#r81", "§9.4.2#r83", "EB-AKS-7"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
owner: BE
trace:
  "§9.4.1#r1": [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 37, 38, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 66, 67, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 95, 96]
  "§9.4.2#r79": [2, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94]
  "§9.4.2#r81": [37, 66, 95]
  "§9.4.2#r83": 5
  "EB-AKS-7": [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 37, 38, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 66, 67, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 95, 96]
---

# Aksi tulis My Asset saat entitas Suspended atau Expired, dan Extend sesudah downgrade plan

## Prerequisites
- Aktor: Borrower dan Assignee Dewi (DU-212-2), Principal pemilik subscription (DU-212-3), dan operator Admin Console (DU-212-4) yang mengubah Status entitas.
- Data:
  - DU-212-1: Client: Name `PT Sinar Mandiri Utama {runId}`, Status `Active`, Plan `Full`.
  - DU-212-2: User: Name `Dewi Lestari {runId}`, Peran `Borrower dan Assignee di entitas PT Sinar Mandiri Utama {runId}, tanpa hak lain`.
  - DU-212-3: User: Name `Hartono Wibowo {runId}`, Peran `Principal yang mengelola plan entitas PT Sinar Mandiri Utama {runId}`.
  - DU-212-4: User: Name `Yusuf Maulana {runId}`, Peran `operator Admin Console yang mengubah Status entitas`.
  - DU-212-5: Pinjaman: Name `Laptop Lenovo ThinkPad T14 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Laporan `belum ada Damage Report`.
  - DU-212-6: Pinjaman: Name `Kamera Sony ZV-E10 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Extension `belum ada pengajuan`.
  - DU-212-7: Pinjaman: Name `Laptop Dell Latitude 5420 {runId}`, Status `Waiting for Handover`, Borrower `Dewi Lestari {runId}`, Sesi Handover `aktif, menunggu konfirmasi Dewi Lestari {runId}`.
  - DU-212-8: Pinjaman: Name `Monitor Dell 24 Inci {runId}`, Status `Waiting for Approval`, Borrower `Dewi Lestari {runId}`.
  - DU-212-9: Pinjaman: Name `Kamera Canon EOS 200D {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`.
  - DU-212-10: Pinjaman: Name `Drone DJI Mini 3 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Extension `menunggu review`.
  - DU-212-11: Pinjaman: Name `Printer HP M404 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`.
  - DU-212-12: Pinjaman: Name `Proyektor Epson EB-X06 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`.
  - DU-212-13: Pinjaman: Name `Tablet Samsung Galaxy Tab A9 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-212-14: Pinjaman: Name `Scanner Canon LiDE 300 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Missing `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-212-15: Pinjaman: Name `Laptop HP ProBook 450 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Source `Self-service`.
  - DU-212-16: Aset: Name `Laptop Asus ZenBook 14 {runId}`, Status `Available`, Source `Self-service`.
  - DU-212-17: Penugasan: Name `Keyboard Logitech MX Keys {runId}`, Status `Waiting for Handover`, Assignee `Dewi Lestari {runId}`, Sesi Handover `aktif, menunggu konfirmasi Dewi Lestari {runId}`.
  - DU-212-18: Penugasan: Name `Monitor LG 27 Inci {runId}`, Status `Assigned`, Assignee `Dewi Lestari {runId}`.
  - DU-212-19: Penugasan: Name `Mouse Logitech MX Master 3 {runId}`, Status `Assigned`, Assignee `Dewi Lestari {runId}`.
  - DU-212-20: Penugasan: Name `Scanner Epson DS-530 {runId}`, Status `Assigned`, Assignee `Dewi Lestari {runId}`, Damage Report `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-212-21: Penugasan: Name `Headset Jabra Evolve2 {runId}`, Status `Assigned`, Assignee `Dewi Lestari {runId}`, Missing `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus `PT Sinar Mandiri Utama {runId}` (DU-212-1) yang tidak dipakai spec lain; entitas itu berstatus `Active` dengan plan `Full` sebelum langkah pertama.
  - Plan sesudah downgrade masih memuat Borrowing dan Assignment.
  - Setiap baris di Data milik entitas itu dan sudah berada pada statusnya sebelum langkah pertama.

## Test Steps

### Entitas Active: aksi tulis diterima sebagai pembanding
1. Dewi mengirim Report Damaged atas pinjaman `Laptop Lenovo ThinkPad T14 {runId}` dengan Damaged Photo `laptop-layar-retak.jpg` dan What happened `Layar laptop retak setelah terjatuh dari meja`
2. Verifikasi aksi diterima dan Damage Report atas `Laptop Lenovo ThinkPad T14 {runId}` dibuat dengan status `Waiting for Confirmation` selama entitas berstatus `Active`

### Downgrade plan: Extend tetap berjalan
3. Principal men-downgrade plan entitas `PT Sinar Mandiri Utama {runId}` dari `Full` ke plan di bawahnya
4. Dewi mengajukan Request Extension atas pinjaman `Kamera Sony ZV-E10 {runId}` dengan Reason `Kegiatan dokumentasi proyek belum selesai`
5. Verifikasi pengajuan Extend atas `Kamera Sony ZV-E10 {runId}` diterima dan menunggu review Aktor Borrow sesudah downgrade

### Entitas Suspended: setiap aksi tulis ditolak server tanpa perubahan data
6. Operator mengubah Status entitas `PT Sinar Mandiri Utama {runId}` menjadi `Suspended`
7. Dewi mengirim Confirm Handover atas pinjaman `Laptop Dell Latitude 5420 {runId}` dengan aset itu tercentang
8. Verifikasi server menolak Confirm Handover atas pinjaman `Laptop Dell Latitude 5420 {runId}` selama Status entitas `Suspended`
9. Dewi mengirim Cancel Borrow atas pinjaman `Monitor Dell 24 Inci {runId}`
10. Verifikasi server menolak Cancel Borrow atas pinjaman `Monitor Dell 24 Inci {runId}` selama Status entitas `Suspended`
11. Dewi mengajukan Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` dengan Reason `Proyek audit lapangan belum selesai`
12. Verifikasi server menolak Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` selama Status entitas `Suspended`
13. Dewi mengirim Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}`
14. Verifikasi server menolak Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}` selama Status entitas `Suspended`
15. Dewi mengirim Report Damaged atas pinjaman `Printer HP M404 {runId}` dengan Damaged Photo `printer-roller-aus.jpg` dan What happened `Roller printer aus`
16. Verifikasi server menolak Report Damaged atas pinjaman `Printer HP M404 {runId}` selama Status entitas `Suspended`
17. Dewi mengirim Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}`
18. Verifikasi server menolak Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}` selama Status entitas `Suspended`
19. Dewi mengirim Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}`
20. Verifikasi server menolak Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}` selama Status entitas `Suspended`
21. Dewi mengirim Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}`
22. Verifikasi server menolak Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}` selama Status entitas `Suspended`
23. Dewi melakukan Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}`
24. Verifikasi server menolak Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}` selama Status entitas `Suspended`
25. Dewi melakukan Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}`
26. Verifikasi server menolak Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}` selama Status entitas `Suspended`
27. Dewi mengirim Confirm atas penugasan `Keyboard Logitech MX Keys {runId}` dengan aset itu tercentang
28. Verifikasi server menolak Confirm Handover penugasan atas penugasan `Keyboard Logitech MX Keys {runId}` selama Status entitas `Suspended`
29. Dewi mengirim Report Damaged atas penugasan `Monitor LG 27 Inci {runId}` dengan Damaged Photo `monitor-panel-bergaris.jpg` dan What happened `Panel monitor bergaris`
30. Verifikasi server menolak Report Damaged penugasan atas penugasan `Monitor LG 27 Inci {runId}` selama Status entitas `Suspended`
31. Dewi mengirim Report Missing atas penugasan `Mouse Logitech MX Master 3 {runId}`
32. Verifikasi server menolak Report Missing penugasan atas penugasan `Mouse Logitech MX Master 3 {runId}` selama Status entitas `Suspended`
33. Dewi mengirim Cancel Damage Report atas penugasan `Scanner Epson DS-530 {runId}`
34. Verifikasi server menolak Cancel Damage Report penugasan atas penugasan `Scanner Epson DS-530 {runId}` selama Status entitas `Suspended`
35. Dewi mengirim Cancel Missing Report atas penugasan `Headset Jabra Evolve2 {runId}`
36. Verifikasi server menolak Cancel Missing Report penugasan atas penugasan `Headset Jabra Evolve2 {runId}` selama Status entitas `Suspended`
37. Verifikasi tidak ada perubahan data: setiap baris yang diuji masih berstatus seperti sebelum aksi, dan tidak ada record laporan, pengajuan, atau serah terima baru
38. Verifikasi seluruh baris yang diuji tetap terbaca oleh Dewi

### Entitas Expired: setiap aksi tulis ditolak server tanpa perubahan data
39. Waktu berlalu sampai T-0 subscription entitas `PT Sinar Mandiri Utama {runId}` sehingga Status menjadi `Expired`
40. Dewi mengirim Cancel Borrow atas pinjaman `Monitor Dell 24 Inci {runId}`
41. Verifikasi server menolak Cancel Borrow atas pinjaman `Monitor Dell 24 Inci {runId}` selama Status entitas `Expired`
42. Dewi mengajukan Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` dengan Reason `Proyek audit lapangan belum selesai`
43. Verifikasi server menolak Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` selama Status entitas `Expired`
44. Dewi mengirim Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}`
45. Verifikasi server menolak Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}` selama Status entitas `Expired`
46. Dewi mengirim Report Damaged atas pinjaman `Printer HP M404 {runId}` dengan Damaged Photo `printer-roller-aus.jpg` dan What happened `Roller printer aus`
47. Verifikasi server menolak Report Damaged atas pinjaman `Printer HP M404 {runId}` selama Status entitas `Expired`
48. Dewi mengirim Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}`
49. Verifikasi server menolak Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}` selama Status entitas `Expired`
50. Dewi mengirim Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}`
51. Verifikasi server menolak Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}` selama Status entitas `Expired`
52. Dewi mengirim Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}`
53. Verifikasi server menolak Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}` selama Status entitas `Expired`
54. Dewi melakukan Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}`
55. Verifikasi server menolak Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}` selama Status entitas `Expired`
56. Dewi melakukan Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}`
57. Verifikasi server menolak Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}` selama Status entitas `Expired`
58. Dewi mengirim Report Damaged atas penugasan `Monitor LG 27 Inci {runId}` dengan Damaged Photo `monitor-panel-bergaris.jpg` dan What happened `Panel monitor bergaris`
59. Verifikasi server menolak Report Damaged penugasan atas penugasan `Monitor LG 27 Inci {runId}` selama Status entitas `Expired`
60. Dewi mengirim Report Missing atas penugasan `Mouse Logitech MX Master 3 {runId}`
61. Verifikasi server menolak Report Missing penugasan atas penugasan `Mouse Logitech MX Master 3 {runId}` selama Status entitas `Expired`
62. Dewi mengirim Cancel Damage Report atas penugasan `Scanner Epson DS-530 {runId}`
63. Verifikasi server menolak Cancel Damage Report penugasan atas penugasan `Scanner Epson DS-530 {runId}` selama Status entitas `Expired`
64. Dewi mengirim Cancel Missing Report atas penugasan `Headset Jabra Evolve2 {runId}`
65. Verifikasi server menolak Cancel Missing Report penugasan atas penugasan `Headset Jabra Evolve2 {runId}` selama Status entitas `Expired`
66. Verifikasi tidak ada perubahan data: setiap baris yang diuji masih berstatus seperti sebelum aksi, dan tidak ada record laporan, pengajuan, atau serah terima baru
67. Verifikasi seluruh baris yang diuji tetap terbaca oleh Dewi

### Entitas Expired pada Grace Period: setiap aksi tulis ditolak server tanpa perubahan data
68. Waktu berlalu sampai hari ke-15 sesudah T-0, dalam Grace Period, sehingga Status entitas `PT Sinar Mandiri Utama {runId}` menjadi `Expired (Grace)`
69. Dewi mengirim Cancel Borrow atas pinjaman `Monitor Dell 24 Inci {runId}`
70. Verifikasi server menolak Cancel Borrow atas pinjaman `Monitor Dell 24 Inci {runId}` selama Status entitas `Expired (Grace)`
71. Dewi mengajukan Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` dengan Reason `Proyek audit lapangan belum selesai`
72. Verifikasi server menolak Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` selama Status entitas `Expired (Grace)`
73. Dewi mengirim Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}`
74. Verifikasi server menolak Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}` selama Status entitas `Expired (Grace)`
75. Dewi mengirim Report Damaged atas pinjaman `Printer HP M404 {runId}` dengan Damaged Photo `printer-roller-aus.jpg` dan What happened `Roller printer aus`
76. Verifikasi server menolak Report Damaged atas pinjaman `Printer HP M404 {runId}` selama Status entitas `Expired (Grace)`
77. Dewi mengirim Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}`
78. Verifikasi server menolak Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}` selama Status entitas `Expired (Grace)`
79. Dewi mengirim Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}`
80. Verifikasi server menolak Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}` selama Status entitas `Expired (Grace)`
81. Dewi mengirim Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}`
82. Verifikasi server menolak Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}` selama Status entitas `Expired (Grace)`
83. Dewi melakukan Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}`
84. Verifikasi server menolak Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}` selama Status entitas `Expired (Grace)`
85. Dewi melakukan Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}`
86. Verifikasi server menolak Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}` selama Status entitas `Expired (Grace)`
87. Dewi mengirim Report Damaged atas penugasan `Monitor LG 27 Inci {runId}` dengan Damaged Photo `monitor-panel-bergaris.jpg` dan What happened `Panel monitor bergaris`
88. Verifikasi server menolak Report Damaged penugasan atas penugasan `Monitor LG 27 Inci {runId}` selama Status entitas `Expired (Grace)`
89. Dewi mengirim Report Missing atas penugasan `Mouse Logitech MX Master 3 {runId}`
90. Verifikasi server menolak Report Missing penugasan atas penugasan `Mouse Logitech MX Master 3 {runId}` selama Status entitas `Expired (Grace)`
91. Dewi mengirim Cancel Damage Report atas penugasan `Scanner Epson DS-530 {runId}`
92. Verifikasi server menolak Cancel Damage Report penugasan atas penugasan `Scanner Epson DS-530 {runId}` selama Status entitas `Expired (Grace)`
93. Dewi mengirim Cancel Missing Report atas penugasan `Headset Jabra Evolve2 {runId}`
94. Verifikasi server menolak Cancel Missing Report penugasan atas penugasan `Headset Jabra Evolve2 {runId}` selama Status entitas `Expired (Grace)`
95. Verifikasi tidak ada perubahan data: setiap baris yang diuji masih berstatus seperti sebelum aksi, dan tidak ada record laporan, pengajuan, atau serah terima baru
96. Verifikasi seluruh baris yang diuji tetap terbaca oleh Dewi
