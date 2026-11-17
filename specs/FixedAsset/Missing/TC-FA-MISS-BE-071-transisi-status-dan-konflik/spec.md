---
id: TC-FA-MISS-BE-071-transisi-status-dan-konflik
title: "Server: tabel transisi status record, aksi atas status yang sudah berubah ditolak tanpa efek ganda, idempotensi per aksi, dan record selesai tidak dibuka ulang"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [§1.2#r17, §1.2#r18, §1.2#r19, §1.2#r20, §1.2#r21, §1.2#r22, §1.2#r101, §1.2#r102, §1.2#r61, §1.2#r62, §1.2#r99, §1.2#r100, §1.2#r66, §1.2#r58, §9.2#r1, §9.2#r2, §9.2#r3, §9.2#r4, §9.2#r5, §9.2#r6, §9.2#r7, §9.2#r8, §9.2#p2, §6#r2, §6#r3, §6#r10, §9.2#b20, §9.4.2#r28, §9.4.2#r22, §9.4.2#r12, §9.4.3#b4, §9.4.3#b5, §9.6#r2, §9.6#r3, §9.6#r4, §9.6#r5, §9.6#r7, §9.6#p2, §9.4.4#r7, §9.4.4#r15, §9.4.4#r20, §9.4.1#r7, §9.2#b34, §10#r4, §10#r5, EB-CON-3, EB-EDG-1, §4.2.4#p13, §9.2#b28, §9.2#b29]
smoke: []
dependsOn: []
trace:
  §1.2#r17: [2, 11, 19, 47, 53]
  §1.2#r18: 25
  §1.2#r19: 29
  §1.2#r20: [15, 65]
  §1.2#r21: [57, 59, 61, 63]
  §1.2#r22: 2
  §1.2#r101: [67, 69, 71]
  §1.2#r102: 23
  §1.2#r61: 75
  §1.2#r62: 76
  §1.2#r99: [15, 49]
  §1.2#r100: 47
  §1.2#r66: [81, 83]
  §1.2#r58: [4, 44]
  §9.2#r1: [2, 33]
  §9.2#r2: [2, 57, 65]
  §9.2#r3: 11
  §9.2#r4: [47, 57]
  §9.2#r5: 19
  §9.2#r6: [53, 73]
  §9.2#r7: 25
  §9.2#r8: 29
  §9.2#p2: [2, 67]
  §6#r2: [13, 51]
  §6#r3: 49
  §6#r10: [6, 35]
  §9.2#b20: [35, 38, 41, 55]
  §9.4.2#r28: [35, 38, 41, 44, 49, 55]
  §9.4.2#r22: [75, 76]
  §9.4.2#r12: [13, 19, 51]
  §9.4.3#b4: [67, 69, 71]
  §9.4.3#b5: [75, 77]
  §9.6#r2: [2, 6, 96]
  §9.6#r3: [25, 27]
  §9.6#r4: [19, 21]
  §9.6#r5: 9
  §9.6#r7: [29, 31, 44]
  §9.6#p2: [35, 38]
  §9.4.4#r7: [35, 41]
  §9.4.4#r15: [16, 17]
  §9.4.4#r20: 76
  §9.4.1#r7: 33
  §9.2#b34: 75
  §10#r4: [53, 77]
  §10#r5: [85, 86]
  EB-CON-3: [35, 38, 41, 44, 49]
  EB-EDG-1: [67, 69, 71, 73, 88, 90, 92, 94]
  §4.2.4#p13: [35, 55]
  §9.2#b28: [11, 15, 57, 65]
  §9.2#b29: [15, 49, 79]
---

# Server: tabel transisi status record, aksi atas status yang sudah berubah ditolak tanpa efek ganda, idempotensi per aksi, dan record selesai tidak dibuka ulang

## Prerequisites
- Aktor: Rina W, Total Control dengan cakupan seluruh client dan Aktor Disposal; `Bambang Wijaya {runId}` (DU-071-1), Total Control dengan cakupan seluruh client dan Aktor Disposal; `Joko Susilo {runId}` (DU-071-2), pemegang tanpa hak Aktor Missing; approver Disposal dan job sistem hanya sebagai pemicu keadaan.
- Data:
  - DU-071-1: User Name `Bambang Wijaya {runId}`, Peran `Total Control`.
  - DU-071-2: User Name `Joko Susilo {runId}`, Peran `pemegang tanpa hak Aktor Missing`.
  - DU-071-3: Asset Name `Hand Pallet Truck {runId}`, Asset ID `FA071-001`, Condition `Normal`, TAG `tanpa TAG`, Pemegang `Joko Susilo {runId}`, Record berjalan `Waiting for Confirmation`, Pelapor `Joko Susilo {runId}`.
  - DU-071-4: Asset Name `Laptop Dell Latitude 5420 {runId}`, Asset ID `FA071-002`, Condition `Normal`, TAG `tanpa TAG`, Pemegang `Joko Susilo {runId}`, Record berjalan `Waiting for Confirmation`, Pelapor `Joko Susilo {runId}`.
  - DU-071-5: Asset Name `Scanner Zebra DS2208 {runId}`, Asset ID `FA071-003`, Condition `Normal`, TAG `tanpa TAG`, Pemegang `Joko Susilo {runId}`, Record berjalan `Waiting for Confirmation`, Pelapor `Joko Susilo {runId}`.
  - DU-071-6: Asset Name `Printer HP LaserJet M404 {runId}`, Asset ID `FA071-004`, Condition `Normal`, TAG `tanpa TAG`, Pemegang `Joko Susilo {runId}`, Record berjalan `Waiting for Confirmation`, Pelapor `Joko Susilo {runId}`.
  - DU-071-7: Asset Name `Camera Canon EOS {runId}`, Asset ID `FA071-005`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `Missing`.
  - DU-071-8: Asset Name `Monitor LG 27UL500 {runId}`, Asset ID `FA071-006`, Condition `Normal`, TAG `tanpa TAG`, Pemegang `Joko Susilo {runId}`, Record berjalan `Waiting for Confirmation`, Pelapor `Joko Susilo {runId}`.
  - DU-071-9: Asset Name `Projector Epson EB-X06 {runId}`, Asset ID `FA071-007`, Condition `Normal`, TAG `tanpa TAG`, Pemegang `Joko Susilo {runId}`, Record berjalan `Waiting for Confirmation`, Pelapor `Joko Susilo {runId}`.
  - DU-071-10: Asset Name `Toyota Innova {runId}`, Asset ID `FA071-008`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `Reported Disposal`.
  - DU-071-11: Asset Name `Mesin Fotokopi Ricoh {runId}`, Asset ID `FA071-009`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `In Disposal Process`.
  - DU-071-12: Asset Name `Drill Bosch GSB {runId}`, Asset ID `FA071-010`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `In Disposal Process`.
  - DU-071-13: Asset Name `Genset Honda EU22 {runId}`, Asset ID `FA071-011`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `In Disposal Process`.
  - DU-071-14: Asset Name `Tablet Samsung Tab A8 {runId}`, Asset ID `FA071-012`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `In Disposal Process`.
  - DU-071-15: Asset Name `Kamera Sony A7 {runId}`, Asset ID `FA071-013`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `In Disposal Process`.
  - DU-071-16: Asset Name `Laptop Lenovo ThinkPad T14 {runId}`, Asset ID `FA071-014`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `Reported Disposal`.
  - DU-071-17: Asset Name `Hand Truck Gudang {runId}`, Asset ID `FA071-015`, Condition `Normal`, TAG `tanpa TAG`, Pemegang `Joko Susilo {runId}`, Record berjalan `Waiting for Confirmation, dilaporkan T0 − 90 hari`.
  - DU-071-18: Asset Name `Kursi Ergonomis {runId}`, Asset ID `FA071-016`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `Missing, dilaporkan T0 − 45 hari`.
  - DU-071-19: Asset Name `Brankas Besi {runId}`, Asset ID `FA071-017`, Condition `Normal`, TAG `tanpa TAG`, Pemegang `Joko Susilo {runId}`, Record berjalan `Waiting for Confirmation`, Pelapor `Joko Susilo {runId}`, Condition tersimpan `Damaged, tidak lagi dapat dipulihkan`.
  - DU-071-20: Asset Name `Papan Tulis {runId}`, Asset ID `FA071-018`, Condition `Normal`, TAG `tanpa TAG`, Pemegang `Joko Susilo {runId}`, Record berjalan `Waiting for Confirmation`, Pelapor `Joko Susilo {runId}`, Condition tersimpan `Damaged, tidak lagi dapat dipulihkan`.
  - DU-071-21: Asset Name `Meja Kerja Kayu {runId}`, Asset ID `FA071-019`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `Found`.
  - DU-071-22: Asset Name `Rak Besi Gudang {runId}`, Asset ID `FA071-020`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `Disposed`.
  - DU-071-23: Asset Name `Lemari Arsip Besi {runId}`, Asset ID `FA071-021`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `Rejected`.
  - DU-071-24: Asset Name `Kipas Angin Standing {runId}`, Asset ID `FA071-022`, Condition `Normal`, TAG `tanpa TAG`, Record berjalan `Canceled`.
  - DU-071-30: Asset Name `Kulkas Pendingin {runId}`, Asset ID `FA071-023`, Condition `Normal`, TAG `tanpa TAG`, Pemegang `Joko Susilo {runId}`, Record berjalan `Waiting for Confirmation`, Pelapor `Joko Susilo {runId}`.
- Kondisi:
  - Long missing after bernilai `30`

## Test Steps
### Record melewati Waiting for Confirmation, Missing, Reported Disposal, dan Found
1. Rina W menjalankan Confirm atas record `Hand Pallet Truck {runId}` yang berstatus `Waiting for Confirmation`
2. Verifikasi record `Hand Pallet Truck {runId}` berstatus `Missing` dan status global aset Missing
3. Rina W menjalankan Reject atas record `Hand Pallet Truck {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
4. Verifikasi aksi itu ditolak dengan `D-MIS-06`, record `Hand Pallet Truck {runId}` tetap `Missing`, dan tidak berubah menjadi `Rejected`
5. Rina W mengirim ulang Confirm atas record `Hand Pallet Truck {runId}`
6. Verifikasi pengiriman ulang itu ditolak dengan `D-MIS-06`, record `Hand Pallet Truck {runId}` tetap `Missing`, dan node `Report confirmed by` tetap satu
7. Rina W menjalankan Add Update atas record `Hand Pallet Truck {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
8. Rina W menjalankan Add Update atas record `Hand Pallet Truck {runId}` dengan Update `Pencarian di gudang lantai dua belum membuahkan hasil`
9. Verifikasi record `Hand Pallet Truck {runId}` memuat dua node `Update added by` yang terpisah, satu per Submit, dan statusnya tetap `Missing`
10. Rina W menjalankan Report Disposal atas record `Hand Pallet Truck {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
11. Verifikasi record `Hand Pallet Truck {runId}` berstatus `Reported Disposal` dengan Condition aset `Reported Disposal` dan Custody `Available`
12. Rina W menjalankan Mark as Found atas record `Hand Pallet Truck {runId}` yang berstatus `Reported Disposal`
13. Verifikasi aksi itu ditolak dengan `D-MIS-06` dan record `Hand Pallet Truck {runId}` tetap `Reported Disposal`
14. Rina W menjalankan Cancel Disposal Report atas record `Hand Pallet Truck {runId}`
15. Verifikasi record `Hand Pallet Truck {runId}` kembali berstatus `Missing` dengan Condition aset `Missing`
16. Verifikasi record `Hand Pallet Truck {runId}` memuat node `Disposal report canceled by` dengan Back to Missing `Yes`
17. Verifikasi transisi Cancel Disposal Report itu tidak mengirim event `missing_*`
18. Rina W menjalankan Mark as Found atas record `Hand Pallet Truck {runId}` dengan Found at default Group aset dan Asset Status `Normal`
19. Verifikasi record `Hand Pallet Truck {runId}` berstatus `Found` dan status global aset menjadi Normal lalu Available
20. Rina W mengirim ulang Mark as Found atas record `Hand Pallet Truck {runId}`
21. Verifikasi pengiriman ulang itu ditolak dengan `D-MIS-06`, record `Hand Pallet Truck {runId}` tetap `Found`, dan node `Marked as found by` tetap satu
22. Rina W mengirim Report Missing atas `Hand Pallet Truck {runId}` dengan What happened `Aset hilang lagi sesudah pemeriksaan bulanan`
23. Verifikasi aset `Hand Pallet Truck {runId}` mendapat record baru berstatus `Missing` dan record `Found` sebelumnya tetap berstatus `Found`

### Laporan pemegang yang ditolak selesai sebagai Rejected
24. Rina W menjalankan Reject atas record `Laptop Dell Latitude 5420 {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
25. Verifikasi record `Laptop Dell Latitude 5420 {runId}` berstatus `Rejected` dan status global aset kembali seperti sebelum laporan, tidak lagi Missing
26. Rina W mengirim ulang Reject atas record `Laptop Dell Latitude 5420 {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
27. Verifikasi pengiriman ulang itu ditolak dengan `D-MIS-06` dan record `Laptop Dell Latitude 5420 {runId}` tetap `Rejected`

### Laporan pemegang yang dibatalkan pelapornya selesai sebagai Canceled
28. `Joko Susilo {runId}` menjalankan Cancel Report atas record `Scanner Zebra DS2208 {runId}`
29. Verifikasi record `Scanner Zebra DS2208 {runId}` berstatus `Canceled` dan status global aset kembali seperti sebelum laporan, tidak lagi Missing
30. `Joko Susilo {runId}` mengirim ulang Cancel Report atas record `Scanner Zebra DS2208 {runId}`
31. Verifikasi pengiriman ulang itu ditolak dengan `D-MIS-06` dan record `Scanner Zebra DS2208 {runId}` tetap `Canceled`

### Mark as Found oleh admin lain mendahului Confirm
32. `Bambang Wijaya {runId}` menjalankan Mark as Found atas record `Printer HP LaserJet M404 {runId}` dengan Found at default Group aset dan Asset Status `Normal`
33. Verifikasi record `Printer HP LaserJet M404 {runId}` berstatus `Found` langsung dari `Waiting for Confirmation`
34. Rina W menjalankan Confirm atas record `Printer HP LaserJet M404 {runId}` dari tampilan yang masih memuat status lama
35. Verifikasi aksi itu ditolak dengan `D-MIS-06` yang menyebut `Bambang Wijaya {runId}` sebagai pengubah, record `Printer HP LaserJet M404 {runId}` tetap `Found`, dan tidak ada node `Report confirmed by`

### Mark as Found oleh admin lain mendahului Add Update
36. `Bambang Wijaya {runId}` menjalankan Mark as Found atas record `Camera Canon EOS {runId}` dengan Found at default Group aset dan Asset Status `Normal`
37. Rina W menjalankan Add Update atas record `Camera Canon EOS {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil` dari tampilan yang masih memuat status lama
38. Verifikasi aksi itu ditolak dengan `D-MIS-06` yang menyebut `Bambang Wijaya {runId}` sebagai pengubah, record `Camera Canon EOS {runId}` tetap `Found`, dan tidak ada node `Update added by` baru

### Confirm oleh admin lain mendahului Reject
39. `Bambang Wijaya {runId}` menjalankan Confirm atas record `Monitor LG 27UL500 {runId}`
40. Rina W menjalankan Reject atas record `Monitor LG 27UL500 {runId}` dengan Reason `Aset masih dipakai di meja pemegang` dari tampilan yang masih memuat status lama
41. Verifikasi aksi itu ditolak dengan `D-MIS-06` yang menyebut `Bambang Wijaya {runId}` sebagai pengubah, record `Monitor LG 27UL500 {runId}` tetap `Missing`, dan tidak berubah menjadi `Rejected`

### Confirm mendahului Cancel Report pelapor
42. Rina W menjalankan Confirm atas record `Projector Epson EB-X06 {runId}`
43. `Joko Susilo {runId}` menjalankan Cancel Report atas record `Projector Epson EB-X06 {runId}` dari tampilan yang masih memuat status lama
44. Verifikasi aksi itu ditolak dengan `D-MIS-06` yang menyebut Rina W sebagai pengubah, record `Projector Epson EB-X06 {runId}` tetap `Missing`, dan status global aset tetap Missing

### Dispose mendahului Cancel Disposal Report
45. `Bambang Wijaya {runId}` menjalankan Dispose atas laporan disposal `Toyota Innova {runId}` dengan jenis `Lost`
46. `Bambang Wijaya {runId}` menjalankan Submit Request atas laporan disposal `Toyota Innova {runId}`
47. Verifikasi record `Toyota Innova {runId}` berstatus `In Disposal Process` dengan Condition aset `In Disposal Process` dan Custody `Available`
48. Rina W menjalankan Cancel Disposal Report atas record `Toyota Innova {runId}` dari tampilan yang masih memuat status lama
49. Verifikasi aksi itu ditolak dengan `D-MIS-06` yang menyebut `Bambang Wijaya {runId}` sebagai pengubah dan record `Toyota Innova {runId}` tetap `In Disposal Process`
50. Rina W menjalankan Mark as Found atas record `Toyota Innova {runId}` yang berstatus `In Disposal Process`
51. Verifikasi aksi itu ditolak dengan `D-MIS-06` dan record `Toyota Innova {runId}` tetap `In Disposal Process`

### Disposal Executed oleh System menutup record sebagai Disposed
52. Disposal Executed untuk aset `Mesin Fotokopi Ricoh {runId}`
53. Verifikasi record `Mesin Fotokopi Ricoh {runId}` berstatus `Disposed` dan Lifecycle aset menjadi `Disposed`
54. Rina W menjalankan Mark as Found atas record `Mesin Fotokopi Ricoh {runId}` dari tampilan yang masih memuat status lama
55. Verifikasi aksi itu ditolak dengan `D-MIS-06` yang menyebut `System` sebagai pengubah dan record `Mesin Fotokopi Ricoh {runId}` tetap `Disposed`

### Baris Disposal yang tidak jadi dieksekusi mengembalikan record ke Missing
56. Approver Disposal menolak baris Disposal aset `Drill Bosch GSB {runId}`
57. Verifikasi record `Drill Bosch GSB {runId}` kembali berstatus `Missing` dengan Condition aset `Missing`
58. Pembuat membatalkan baris Disposal aset `Genset Honda EU22 {runId}`
59. Verifikasi record `Genset Honda EU22 {runId}` kembali berstatus `Missing` dengan Condition aset `Missing`
60. Baris Disposal aset `Tablet Samsung Tab A8 {runId}` dihapus dari daftar Disposal
61. Verifikasi record `Tablet Samsung Tab A8 {runId}` kembali berstatus `Missing` dengan Condition aset `Missing`
62. Baris Disposal aset `Kamera Sony A7 {runId}` melewati Transaction timeout
63. Verifikasi record `Kamera Sony A7 {runId}` kembali berstatus `Missing` dengan Condition aset `Missing`
64. Aktor Disposal menjalankan Decline Report atas laporan disposal `Laptop Lenovo ThinkPad T14 {runId}`
65. Verifikasi record `Laptop Lenovo ThinkPad T14 {runId}` kembali berstatus `Missing` dengan Condition aset `Missing`

### Record selesai tidak dibuka ulang
66. Rina W menjalankan Confirm atas record `Meja Kerja Kayu {runId}` yang berstatus `Found`
67. Verifikasi aksi itu ditolak dengan `D-MIS-06` dan record `Meja Kerja Kayu {runId}` tetap `Found`
68. Rina W menjalankan Confirm atas record `Lemari Arsip Besi {runId}` yang berstatus `Rejected`
69. Verifikasi aksi itu ditolak dengan `D-MIS-06` dan record `Lemari Arsip Besi {runId}` tetap `Rejected`
70. Rina W menjalankan Confirm atas record `Kipas Angin Standing {runId}` yang berstatus `Canceled`
71. Verifikasi aksi itu ditolak dengan `D-MIS-06` dan record `Kipas Angin Standing {runId}` tetap `Canceled`
72. Rina W menjalankan Mark as Found atas record `Rak Besi Gudang {runId}` yang berstatus `Disposed`
73. Verifikasi aksi itu ditolak dengan `D-MIS-06` dan record `Rak Besi Gudang {runId}` tetap `Disposed`

### Laporan pemegang tidak punya batas tunggu dan tidak ditutup otomatis
74. Job Long missing harian berjalan
75. Verifikasi record `Hand Truck Gudang {runId}` yang dilaporkan T0 − 90 hari tetap berstatus `Waiting for Confirmation` dan tidak dibatalkan otomatis
76. Verifikasi record `Hand Truck Gudang {runId}` tidak mendapat notifikasi, node, atau penanda tambahan selama menunggu
77. Verifikasi record `Kursi Ergonomis {runId}` yang dilaporkan T0 − 45 hari tetap berstatus `Missing` dan tidak ditutup otomatis

### Report Disposal hanya untuk record Missing
78. Rina W menjalankan Report Disposal atas record `Hand Truck Gudang {runId}` yang berstatus `Waiting for Confirmation` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
79. Verifikasi aksi itu ditolak dan record `Hand Truck Gudang {runId}` tetap `Waiting for Confirmation` tanpa Disposal Report

### Condition tersimpan yang tidak lagi dapat dipulihkan menolak Reject dan Cancel Report
80. Rina W menjalankan Reject atas record `Brankas Besi {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
81. Verifikasi aksi itu ditolak dengan `D-MIS-06`, record `Brankas Besi {runId}` tetap `Waiting for Confirmation`, dan status global aset tetap Missing
82. `Joko Susilo {runId}` menjalankan Cancel Report atas record `Papan Tulis {runId}`
83. Verifikasi aksi itu ditolak dengan `D-MIS-06`, record `Papan Tulis {runId}` tetap `Waiting for Confirmation`, dan status global aset tetap Missing

### Missing record tidak dapat dihapus pengguna
84. Rina W menghapus record `Kursi Ergonomis {runId}`
85. Verifikasi penghapusan itu ditolak dan record `Kursi Ergonomis {runId}` tetap ada berstatus `Missing`
86. Verifikasi record `Meja Kerja Kayu {runId}` yang berstatus `Found` tetap tersedia sebagai riwayat selama asetnya ada

### Aksi tulis atas record yang asetnya sudah dihapus ditolak tanpa efek
87. Rina W menjalankan Delete Asset Data atas aset `Rak Besi Gudang {runId}` yang berstatus Disposed
88. Verifikasi aset `Rak Besi Gudang {runId}` terhapus bersama record `Disposed` miliknya
89. Rina W menjalankan Confirm atas record `Rak Besi Gudang {runId}` dari tampilan yang masih memuat record itu
90. Verifikasi aksi itu ditolak tanpa efek dan tidak ada record, node, atau aset `Rak Besi Gudang {runId}` yang tercipta atau berubah
91. Rina W menjalankan Add Update atas record `Rak Besi Gudang {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil` dari tampilan yang masih memuat record itu
92. Verifikasi aksi itu ditolak tanpa efek dan tidak ada node `Update added by` yang tercatat untuk `Rak Besi Gudang {runId}`
93. Rina W menjalankan Mark as Found atas record `Rak Besi Gudang {runId}` dari tampilan yang masih memuat record itu
94. Verifikasi aksi itu ditolak tanpa efek dan tidak ada node `Marked as found by` yang tercatat untuk `Rak Besi Gudang {runId}`

### Confirm mencatat status record dan status global aset bersama
95. Rina W menjalankan Confirm atas record `Kulkas Pendingin {runId}`
96. Verifikasi aksi itu atomik: record `Missing` dan status global aset Missing tercatat bersama, tanpa salah satunya saja
