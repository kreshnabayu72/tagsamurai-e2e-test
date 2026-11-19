---
id: TC-FA-MYASSET-BE-212-aksi-tulis-menurut-state-entitas-dan-plan-dep-borrow
title: "Aksi tulis My Asset saat entitas Suspended atau Expired"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.4.1#r1", "§9.4.2#r81", "§9.4.2#r83", "EB-AKS-7"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
owner: BE
trace:
  "§9.4.1#r1": [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 34, 35, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 65, 66, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 93, 94]
  "§9.4.2#r81": [2, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 38, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92]
  "§9.4.2#r83": [34, 65, 93]
  "EB-AKS-7": [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 34, 35, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 65, 66, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 93, 94]
---

# Aksi tulis My Asset saat entitas Suspended atau Expired

## Prerequisites
- Aktor: Borrower dan Assignee Dewi (DU-212-2) dan operator Admin Console (DU-212-3) yang mengubah Status entitas.
- Data:
  - DU-212-1: Client: Name `PT Sinar Mandiri Utama {runId}`, Status `Active`, Plan `Full`.
  - DU-212-2: User: Name `Dewi Lestari {runId}`, Peran `Borrower dan Assignee di entitas PT Sinar Mandiri Utama {runId}, tanpa hak lain`.
  - DU-212-3: User: Name `Yusuf Maulana {runId}`, Peran `operator Admin Console yang mengubah Status entitas`.
  - DU-212-4: Pinjaman: Name `Laptop Lenovo ThinkPad T14 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Laporan `belum ada Damage Report`.
  - DU-212-5: Pinjaman: Name `Laptop Dell Latitude 5420 {runId}`, Status `Waiting for Handover`, Borrower `Dewi Lestari {runId}`, Sesi Handover `aktif, menunggu konfirmasi Dewi Lestari {runId}`.
  - DU-212-6: Pinjaman: Name `Monitor Dell 24 Inci {runId}`, Status `Waiting for Approval`, Borrower `Dewi Lestari {runId}`.
  - DU-212-7: Pinjaman: Name `Kamera Canon EOS 200D {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`.
  - DU-212-8: Pinjaman: Name `Drone DJI Mini 3 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Extension `menunggu review`.
  - DU-212-9: Pinjaman: Name `Printer HP M404 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`.
  - DU-212-10: Pinjaman: Name `Proyektor Epson EB-X06 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`.
  - DU-212-11: Pinjaman: Name `Tablet Samsung Galaxy Tab A9 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Damage Report `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-212-12: Pinjaman: Name `Scanner Canon LiDE 300 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Missing `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-212-13: Pinjaman: Name `Laptop HP ProBook 450 {runId}`, Status `Borrowed`, Borrower `Dewi Lestari {runId}`, Source `Self-service`.
  - DU-212-14: Aset: Name `Laptop Asus ZenBook 14 {runId}`, Status `Available`, Source `Self-service`.
  - DU-212-15: Penugasan: Name `Keyboard Logitech MX Keys {runId}`, Status `Waiting for Handover`, Assignee `Dewi Lestari {runId}`, Sesi Handover `aktif, menunggu konfirmasi Dewi Lestari {runId}`.
  - DU-212-16: Penugasan: Name `Monitor LG 27 Inci {runId}`, Status `Assigned`, Assignee `Dewi Lestari {runId}`.
  - DU-212-17: Penugasan: Name `Mouse Logitech MX Master 3 {runId}`, Status `Assigned`, Assignee `Dewi Lestari {runId}`.
  - DU-212-18: Penugasan: Name `Scanner Epson DS-530 {runId}`, Status `Assigned`, Assignee `Dewi Lestari {runId}`, Damage Report `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
  - DU-212-19: Penugasan: Name `Headset Jabra Evolve2 {runId}`, Status `Assigned`, Assignee `Dewi Lestari {runId}`, Missing `Waiting for Confirmation, dilaporkan Dewi Lestari {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus `PT Sinar Mandiri Utama {runId}` (DU-212-1) yang tidak dipakai spec lain; entitas itu berstatus `Active` dengan plan `Full` sebelum langkah pertama.
  - Setiap baris di Data milik entitas itu dan sudah berada pada statusnya sebelum langkah pertama.
  - Sesi Handover DU-212-5 dan DU-212-15 masih menunggu konfirmasi, belum melewati jendela konfirmasi, pada langkah Confirm Handover di blok Entitas Suspended, yang berjalan sebelum waktu dimajukan, sehingga penolakannya karena Status entitas, bukan karena jendela habis.
  - Job sistem terjadwal tidak diblokir oleh Status entitas: perubahan yang dilakukan job selama waktu dimajukan bukan bagian dari asersi tidak ada perubahan data, yang dibandingkan dengan keadaan yang dicatat sesudah waktu dimajukan dan sebelum aksi pertama blok.

## Test Steps

### Entitas Active: aksi tulis diterima sebagai pembanding
1. Dewi mengirim Report Damaged atas pinjaman `Laptop Lenovo ThinkPad T14 {runId}` dengan Damaged Photo `laptop-layar-retak.jpg` dan What happened `Layar laptop retak setelah terjatuh dari meja`
2. Verifikasi aksi diterima dan Damage Report atas `Laptop Lenovo ThinkPad T14 {runId}` dibuat dengan status `Waiting for Confirmation` selama entitas berstatus `Active`

### Entitas Suspended: setiap aksi tulis ditolak server tanpa perubahan data
3. Operator mengubah Status entitas `PT Sinar Mandiri Utama {runId}` menjadi `Suspended`
4. Dewi mengirim Confirm Handover atas pinjaman `Laptop Dell Latitude 5420 {runId}` dengan aset itu tercentang
5. Verifikasi server menolak Confirm Handover atas pinjaman `Laptop Dell Latitude 5420 {runId}` selama Status entitas `Suspended`
6. Dewi mengirim Cancel Borrow atas pinjaman `Monitor Dell 24 Inci {runId}`
7. Verifikasi server menolak Cancel Borrow atas pinjaman `Monitor Dell 24 Inci {runId}` selama Status entitas `Suspended`
8. Dewi mengajukan Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` dengan Reason `Proyek audit lapangan belum selesai`
9. Verifikasi server menolak Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` selama Status entitas `Suspended`
10. Dewi mengirim Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}`
11. Verifikasi server menolak Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}` selama Status entitas `Suspended`
12. Dewi mengirim Report Damaged atas pinjaman `Printer HP M404 {runId}` dengan Damaged Photo `printer-roller-aus.jpg` dan What happened `Roller printer aus`
13. Verifikasi server menolak Report Damaged atas pinjaman `Printer HP M404 {runId}` selama Status entitas `Suspended`
14. Dewi mengirim Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}`
15. Verifikasi server menolak Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}` selama Status entitas `Suspended`
16. Dewi mengirim Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}`
17. Verifikasi server menolak Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}` selama Status entitas `Suspended`
18. Dewi mengirim Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}`
19. Verifikasi server menolak Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}` selama Status entitas `Suspended`
20. Dewi melakukan Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}`
21. Verifikasi server menolak Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}` selama Status entitas `Suspended`
22. Dewi melakukan Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}`
23. Verifikasi server menolak Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}` selama Status entitas `Suspended`
24. Dewi mengirim Confirm atas penugasan `Keyboard Logitech MX Keys {runId}` dengan aset itu tercentang
25. Verifikasi server menolak Confirm Handover penugasan atas penugasan `Keyboard Logitech MX Keys {runId}` selama Status entitas `Suspended`
26. Dewi mengirim Report Damaged atas penugasan `Monitor LG 27 Inci {runId}` dengan Damaged Photo `monitor-panel-bergaris.jpg` dan What happened `Panel monitor bergaris`
27. Verifikasi server menolak Report Damaged penugasan atas penugasan `Monitor LG 27 Inci {runId}` selama Status entitas `Suspended`
28. Dewi mengirim Report Missing atas penugasan `Mouse Logitech MX Master 3 {runId}`
29. Verifikasi server menolak Report Missing penugasan atas penugasan `Mouse Logitech MX Master 3 {runId}` selama Status entitas `Suspended`
30. Dewi mengirim Cancel Damage Report atas penugasan `Scanner Epson DS-530 {runId}`
31. Verifikasi server menolak Cancel Damage Report penugasan atas penugasan `Scanner Epson DS-530 {runId}` selama Status entitas `Suspended`
32. Dewi mengirim Cancel Missing Report atas penugasan `Headset Jabra Evolve2 {runId}`
33. Verifikasi server menolak Cancel Missing Report penugasan atas penugasan `Headset Jabra Evolve2 {runId}` selama Status entitas `Suspended`
34. Verifikasi tidak ada perubahan data: setiap baris yang diuji masih berstatus seperti sebelum aksi, dan tidak ada record laporan, pengajuan, atau serah terima baru
35. Verifikasi seluruh baris yang diuji tetap terbaca oleh Dewi

### Entitas kembali Active: aksi tulis diterima sebagai pembanding
36. Operator mengubah Status entitas `PT Sinar Mandiri Utama {runId}` kembali menjadi `Active`
37. Dewi mengirim Cancel Damage Report atas pinjaman `Laptop Lenovo ThinkPad T14 {runId}`
38. Verifikasi aksi diterima dan Damage Report atas `Laptop Lenovo ThinkPad T14 {runId}` tidak lagi berstatus `Waiting for Confirmation` selama entitas berstatus `Active`

### Entitas Expired: setiap aksi tulis ditolak server tanpa perubahan data
39. Waktu berlalu sampai T-0 subscription entitas `PT Sinar Mandiri Utama {runId}` sehingga Status menjadi `Expired`
40. Catat status setiap baris yang diuji serta jumlah record laporan, pengajuan, dan serah terima sesudah waktu dimajukan dan sebelum aksi pertama blok ini
41. Dewi mengajukan Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` dengan Reason `Proyek audit lapangan belum selesai`
42. Verifikasi server menolak Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` selama Status entitas `Expired`
43. Dewi mengirim Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}`
44. Verifikasi server menolak Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}` selama Status entitas `Expired`
45. Dewi mengirim Report Damaged atas pinjaman `Printer HP M404 {runId}` dengan Damaged Photo `printer-roller-aus.jpg` dan What happened `Roller printer aus`
46. Verifikasi server menolak Report Damaged atas pinjaman `Printer HP M404 {runId}` selama Status entitas `Expired`
47. Dewi mengirim Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}`
48. Verifikasi server menolak Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}` selama Status entitas `Expired`
49. Dewi mengirim Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}`
50. Verifikasi server menolak Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}` selama Status entitas `Expired`
51. Dewi mengirim Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}`
52. Verifikasi server menolak Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}` selama Status entitas `Expired`
53. Dewi melakukan Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}`
54. Verifikasi server menolak Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}` selama Status entitas `Expired`
55. Dewi melakukan Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}`
56. Verifikasi server menolak Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}` selama Status entitas `Expired`
57. Dewi mengirim Report Damaged atas penugasan `Monitor LG 27 Inci {runId}` dengan Damaged Photo `monitor-panel-bergaris.jpg` dan What happened `Panel monitor bergaris`
58. Verifikasi server menolak Report Damaged penugasan atas penugasan `Monitor LG 27 Inci {runId}` selama Status entitas `Expired`
59. Dewi mengirim Report Missing atas penugasan `Mouse Logitech MX Master 3 {runId}`
60. Verifikasi server menolak Report Missing penugasan atas penugasan `Mouse Logitech MX Master 3 {runId}` selama Status entitas `Expired`
61. Dewi mengirim Cancel Damage Report atas penugasan `Scanner Epson DS-530 {runId}`
62. Verifikasi server menolak Cancel Damage Report penugasan atas penugasan `Scanner Epson DS-530 {runId}` selama Status entitas `Expired`
63. Dewi mengirim Cancel Missing Report atas penugasan `Headset Jabra Evolve2 {runId}`
64. Verifikasi server menolak Cancel Missing Report penugasan atas penugasan `Headset Jabra Evolve2 {runId}` selama Status entitas `Expired`
65. Verifikasi tidak ada perubahan data akibat aksi blok ini: setiap baris yang diuji masih berstatus seperti yang dicatat pada langkah 40, dan tidak ada record laporan, pengajuan, atau serah terima baru dibanding yang dicatat pada langkah 40
66. Verifikasi seluruh baris yang diuji tetap terbaca oleh Dewi

### Entitas Expired pada Grace Period: setiap aksi tulis ditolak server tanpa perubahan data
67. Waktu berlalu sampai hari ke-15 sesudah T-0, dalam Grace Period, sehingga Status entitas `PT Sinar Mandiri Utama {runId}` menjadi `Expired (Grace)`
68. Catat status setiap baris yang diuji serta jumlah record laporan, pengajuan, dan serah terima sesudah waktu dimajukan dan sebelum aksi pertama blok ini
69. Dewi mengajukan Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` dengan Reason `Proyek audit lapangan belum selesai`
70. Verifikasi server menolak Request Extension atas pinjaman `Kamera Canon EOS 200D {runId}` selama Status entitas `Expired (Grace)`
71. Dewi mengirim Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}`
72. Verifikasi server menolak Cancel Extension Request atas pinjaman `Drone DJI Mini 3 {runId}` selama Status entitas `Expired (Grace)`
73. Dewi mengirim Report Damaged atas pinjaman `Printer HP M404 {runId}` dengan Damaged Photo `printer-roller-aus.jpg` dan What happened `Roller printer aus`
74. Verifikasi server menolak Report Damaged atas pinjaman `Printer HP M404 {runId}` selama Status entitas `Expired (Grace)`
75. Dewi mengirim Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}`
76. Verifikasi server menolak Report Missing atas pinjaman `Proyektor Epson EB-X06 {runId}` selama Status entitas `Expired (Grace)`
77. Dewi mengirim Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}`
78. Verifikasi server menolak Cancel Damage Report atas pinjaman `Tablet Samsung Galaxy Tab A9 {runId}` selama Status entitas `Expired (Grace)`
79. Dewi mengirim Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}`
80. Verifikasi server menolak Cancel Missing Report atas pinjaman `Scanner Canon LiDE 300 {runId}` selama Status entitas `Expired (Grace)`
81. Dewi melakukan Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}`
82. Verifikasi server menolak Return atas pinjaman self-service `Laptop HP ProBook 450 {runId}` selama Status entitas `Expired (Grace)`
83. Dewi melakukan Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}`
84. Verifikasi server menolak Borrow Now atas aset self-service `Laptop Asus ZenBook 14 {runId}` selama Status entitas `Expired (Grace)`
85. Dewi mengirim Report Damaged atas penugasan `Monitor LG 27 Inci {runId}` dengan Damaged Photo `monitor-panel-bergaris.jpg` dan What happened `Panel monitor bergaris`
86. Verifikasi server menolak Report Damaged penugasan atas penugasan `Monitor LG 27 Inci {runId}` selama Status entitas `Expired (Grace)`
87. Dewi mengirim Report Missing atas penugasan `Mouse Logitech MX Master 3 {runId}`
88. Verifikasi server menolak Report Missing penugasan atas penugasan `Mouse Logitech MX Master 3 {runId}` selama Status entitas `Expired (Grace)`
89. Dewi mengirim Cancel Damage Report atas penugasan `Scanner Epson DS-530 {runId}`
90. Verifikasi server menolak Cancel Damage Report penugasan atas penugasan `Scanner Epson DS-530 {runId}` selama Status entitas `Expired (Grace)`
91. Dewi mengirim Cancel Missing Report atas penugasan `Headset Jabra Evolve2 {runId}`
92. Verifikasi server menolak Cancel Missing Report penugasan atas penugasan `Headset Jabra Evolve2 {runId}` selama Status entitas `Expired (Grace)`
93. Verifikasi tidak ada perubahan data akibat aksi blok ini: setiap baris yang diuji masih berstatus seperti yang dicatat pada langkah 68, dan tidak ada record laporan, pengajuan, atau serah terima baru dibanding yang dicatat pada langkah 68
94. Verifikasi seluruh baris yang diuji tetap terbaca oleh Dewi
