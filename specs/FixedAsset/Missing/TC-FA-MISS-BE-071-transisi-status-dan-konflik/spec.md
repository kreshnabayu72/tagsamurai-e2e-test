---
id: TC-FA-MISS-BE-071-transisi-status-dan-konflik
title: "Server: tabel transisi status record, aksi atas status yang sudah berubah ditolak tanpa efek ganda, idempotensi per aksi, record selesai tidak dibuka ulang"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§1.2#r18", "§1.2#r19", "§1.2#r20", "§1.2#r21", "§1.2#r22", "§1.2#r23", "§1.2#r104", "§1.2#r105", "§1.2#r62", "§1.2#r63", "§1.2#r102", "§1.2#r103", "§1.2#r67", "§1.2#r59", "§9.2#r1", "§9.2#r2", "§9.2#r3", "§9.2#r4", "§9.2#r5", "§9.2#r6", "§9.2#r7", "§9.2#r8", "§9.2#p2", "§6#r2", "§6#r3", "§6#r10", "§9.2#b20", "§9.4.2#r28", "§9.4.2#r22", "§9.4.2#r12", "§9.4.3#b4", "§9.4.3#b5", "§9.6#r2", "§9.6#r3", "§9.6#r4", "§9.6#r5", "§9.6#r7", "§9.6#p2", "§9.4.4#r7", "§9.4.4#r17", "§9.4.4#r22", "§9.4.1#r7", "§9.2#b36", "§10#r4", "§10#r5", "EB-CON-3", "EB-EDG-1", "§4.2.4#p14", "§9.2#b30", "§9.2#b31", "§9.2#b37", "§9.4.2#r38", "§3#p4", "§9.4.2#r11", "§1.2#r71", "§9.4.2#r37", "§8.1#r16", "§8.1#r17", "§3#p8", "§9.8#p2", "§11#r11"]
smoke: []
dependsOn: []
trace:
  "§1.2#r18": [2, 23, 48, 58, 89]
  "§1.2#r19": 8
  "§1.2#r20": 14
  "§1.2#r21": [32, 38, 44]
  "§1.2#r22": [50, 52, 54, 56]
  "§1.2#r23": 85
  "§1.2#r104": [64, 66, 68, 70, 72]
  "§1.2#r105": [74, 75]
  "§1.2#r62": 112
  "§1.2#r63": 113
  "§1.2#r102": [81, 83]
  "§1.2#r103": [48, 50]
  "§1.2#r67": [135, 137]
  "§1.2#r59": [98, 100, 103]
  "§9.2#r1": [2, 8, 14, 20]
  "§9.2#r2": [23, 26]
  "§9.2#r3": [23, 48, 50]
  "§9.2#r4": [48, 50, 58]
  "§9.2#r5": [26, 27]
  "§9.2#r6": 58
  "§9.2#r7": [8, 9]
  "§9.2#r8": [14, 15]
  "§9.2#p2": [85, 89]
  "§6#r2": [36, 77, 79]
  "§6#r3": [81, 83, 106]
  "§6#r10": [92, 95]
  "§9.2#b20": [92, 95, 98, 103, 106]
  "§9.4.2#r28": [18, 92, 95, 98, 103, 106]
  "§9.4.2#r22": 112
  "§9.4.2#r12": [36, 42]
  "§9.4.3#b4": [64, 68, 72]
  "§9.4.3#b5": [113, 117]
  "§9.6#r2": [2, 3, 6]
  "§9.6#r3": [9, 12]
  "§9.6#r4": 30
  "§9.6#r5": [108, 110]
  "§9.6#r7": [14, 15, 18]
  "§9.6#p2": 110
  "§9.4.4#r7": [92, 106]
  "§9.4.4#r17": [40, 42]
  "§9.4.4#r22": 113
  "§9.4.1#r7": [20, 21]
  "§9.2#b36": 112
  "§10#r4": [116, 117]
  "§10#r5": [62, 75, 87]
  "EB-CON-3": [92, 95, 98, 103, 106]
  "EB-EDG-1": [6, 64, 68, 72]
  "§4.2.4#p14": [60, 92]
  "§9.2#b30": [23, 48, 50]
  "§9.2#b31": [85, 132, 133]
  "§9.2#b37": [126, 128]
  "§9.4.2#r38": [126, 128, 130]
  "§3#p4": [2, 8, 14, 20, 126]
  "§9.4.2#r11": [32, 33, 50]
  "§1.2#r71": [119, 120, 122, 124]
  "§9.4.2#r37": [119, 122, 124]
  "§8.1#r16": 33
  "§8.1#r17": [39, 45]
  "§3#p8": [48, 58]
  "§9.8#p2": [24, 34, 40, 46]
  "§11#r11": [132, 133]
---

# Server: tabel transisi status record, aksi atas status yang sudah berubah ditolak tanpa efek ganda, idempotensi per aksi, record selesai tidak dibuka ulang

## Prerequisites
- Aktor:
  - Aktor Missing A: Total Control, cakupan seluruh client, bukan Last holder satu pun record di Data.
  - Aktor Missing B: Total Control lain, cakupan seluruh client, bukan Last holder satu pun record di Data.
  - Aktor Disposal: Total Control A yang sama dengan Aktor Missing A, memutuskan Report dan Request Disposal.
  - Pemegang: Borrower atau Assignee aset tanpa hak Aktor Missing pada Group aset; pemegang yang sama melapor dan membatalkan laporannya sendiri.
  - Pelapor sesi: Asset Admin sub-tab Audit tanpa hak Aktor Missing pada Group aset.
  - Staff Auditor: tanpa hak Aktor Missing pada Group aset.
- Data:
  - DU-071-1: Missing record berstatus `Waiting for Confirmation`, Source `Reported by holder`, aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office`, dipegang Borrower lewat baris Borrow terbuka, status global aset `Missing`.
  - DU-071-2: Missing record berstatus `Waiting for Confirmation`, Source `Reported by holder`, aset `Monitor LG 27UL500 {runId}` di Group `Head Office`, dipegang Borrower lewat baris Borrow terbuka, status global aset `Missing`.
  - DU-071-3: Missing record berstatus `Waiting for Confirmation`, Source `Reported by holder`, aset `Hand Pallet Truck {runId}` di Group `Head Office`, dipegang Assignee lewat baris Assignment terbuka, status global aset `Missing`.
  - DU-071-4: Missing record berstatus `Waiting for Confirmation`, Source `Reported by holder`, aset `Camera Canon EOS {runId}` di Group `Head Office`, dipegang Borrower lewat baris Borrow terbuka, tanpa TAG, status global aset `Missing`.
  - DU-071-5: Missing record berstatus `Missing`, Source `Manual`, aset `Projector Epson EB-X06 {runId}` di Group `Head Office`.
  - DU-071-6: Missing record berstatus `Missing`, Source `Manual`, aset `Scanner Zebra DS2208 {runId}` di Group `Head Office`, tanpa TAG.
  - DU-071-7: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Drill Bosch GSB {runId}` di Group `Head Office`, Disposal Report berstatus `Reported`.
  - DU-071-8: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Forklift Toyota 8FD {runId}` di Group `Head Office`, tanpa TAG, Disposal Report berstatus `Reported`.
  - DU-071-9: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Router Cisco ISR {runId}` di Group `Head Office`, Disposal Report berstatus `Reported` dilaporkan Aktor Missing A.
  - DU-071-10: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Handheld Zebra TC21 {runId}` di Group `Head Office`, Disposal Report berstatus `Reported`.
  - DU-071-11: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `Generator Honda EU20 {runId}` di Group `Head Office`, baris Disposal Write-off `Waiting for Approval`.
  - DU-071-12: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `Kursi Ergonomis Ergotec {runId}` di Group `Head Office`, baris Disposal Write-off `Waiting for Approval`.
  - DU-071-13: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `Meja Rapat Informa {runId}` di Group `Head Office`, baris Disposal Write-off `Waiting for Approval`.
  - DU-071-14: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `AC Daikin FTV35 {runId}` di Group `Head Office`, baris Disposal Write-off `Waiting for Approval`.
  - DU-071-15: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `Server Dell PowerEdge R450 {runId}` di Group `Head Office`, baris Disposal Write-off `Waiting for Execution`.
  - DU-071-16: Missing record berstatus `Found`, Source `Borrow`, aset `Barcode Printer Zebra ZD230 {runId}` di Group `Head Office`, status global aset `Normal`.
  - DU-071-17: Missing record berstatus `Rejected`, Source `Reported by holder`, aset `Mesin Fotokopi Fuji Xerox {runId}` di Group `Head Office`.
  - DU-071-18: Missing record berstatus `Canceled`, Source `Reported by holder`, aset `Tablet Samsung Galaxy Tab A8 {runId}` di Group `Head Office`.
  - DU-071-19: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Proyektor BenQ MW550 {runId}` di Group `Head Office`.
  - DU-071-20: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `UPS APC Smart 1500 {runId}` di Group `Head Office`.
  - DU-071-21: Missing record berstatus `Missing`, Source `Transfer`, aset `Switch Cisco Catalyst 2960 {runId}` di Group `Head Office`.
  - DU-071-22: Missing record berstatus `Waiting for Confirmation`, Source `Reported by holder`, aset `Kamera CCTV Hikvision {runId}` di Group `Head Office`.
  - DU-071-23: Missing record berstatus `Missing`, Source `Manual`, aset `Timbangan Digital Ohaus {runId}` di Group `Head Office`, tanpa TAG.
  - DU-071-24: Missing record berstatus `Waiting for Confirmation`, Source `Reported by holder`, aset `Mixer Audio Yamaha MG10 {runId}` di Group `Head Office`, tanpa TAG.
  - DU-071-25: Missing record berstatus `Waiting for Confirmation`, Source `Reported by holder`, aset `Radio Handy Motorola {runId}` di Group `Head Office`, tanpa TAG.
  - DU-071-26: Missing record berstatus `Waiting for Confirmation`, Source `Reported by holder`, aset `Laptop HP ProBook 450 {runId}` di Group `Head Office`.
  - DU-071-27: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Monitor Dell P2422H {runId}` di Group `Head Office`, Disposal Report berstatus `Reported`.
  - DU-071-28: Missing record berstatus `Missing`, Source `Manual`, aset `Keyboard Logitech MX {runId}` di Group `Head Office`.
  - DU-071-29: Missing record berstatus `Waiting for Confirmation`, Source `Reported by holder`, aset `Telepon IP Yealink T46 {runId}` di Group `Head Office`.
  - DU-071-30: Missing record berstatus `Missing`, Source `Manual`, aset `Trolley Besi Gudang {runId}` di Group `Head Office`.
  - DU-071-31: aset `Kompresor Swan 2HP {runId}` di Group `Head Office`, dipegang Borrower lewat baris Borrow terbuka, belum punya record berjalan.
  - DU-071-32: aset `Genset Perkins 20kVA {runId}` di Group `Head Office`, belum punya record berjalan.
  - DU-071-33: Missing record berstatus `Waiting for Confirmation`, Source `Audit`, aset `Lemari Arsip Brother {runId}` di Group `Head Office`, dilaporkan Pelapor sesi dari Task Detail sesi pemeriksaan, baris sesi pemeriksaan `Not found`.
  - DU-071-34: Missing record berstatus `Missing`, Source `Audit`, aset `Laptop Asus ExpertBook B1 {runId}` di Group `Head Office`, dilaporkan Pelapor sesi lalu di-Confirm Aktor Missing.
  - DU-071-35: Missing record berstatus `Missing`, Source `Audit`, aset `Printer Epson L3250 {runId}` di Group `Head Office`, dilaporkan Group Manager dari Task Detail sesi pemeriksaan sehingga langsung `Missing`.
  - DU-071-36: Missing record berstatus `Missing`, Source `Reconciliation`, aset `Dispenser Sharp {runId}` di Group `Head Office`.
  - DU-071-37: Missing record berstatus `Waiting for Confirmation`, Source `Reported by holder`, aset `Telepon IP Cisco 7841 {runId}` di Group `Head Office`, Condition aset sebelum laporan sudah tidak dapat dipulihkan.
  - DU-071-38: Missing record berstatus `Disposed`, Source `Manual`, aset `Lampu Sorot Philips {runId}` di Group `Head Office`, aset berstatus Disposed.
  - DU-071-39: Reason Reject `Aset masih dipegang peminjam`, dipakai Aktor Missing A dan B.
  - DU-071-40: Update `Pencarian di gudang sudah dilakukan tim operasional`.
  - DU-071-41: Update `Pencarian di lobi sudah dilakukan tim keamanan`.
  - DU-071-42: What happened `Aset hilang saat dipindahkan antar ruangan`.
  - DU-071-43: Reason Report Disposal `Aset tidak ditemukan setelah pencarian`.
  - DU-071-44: Reason Decline Report `Aset masih dalam proses pencarian`.
- Kondisi:
  - Long missing after bernilai `30`.
  - Jumlah event `missing_*`, jumlah node Missing Log, dan nilai `Last Updated` setiap record di Data dicatat sebelum aksi pertama atas record itu.
  - Cakupan Group Aktor Missing A dan B meliputi `Head Office`.

## Test Steps

### Confirm laporan pemegang membawa record ke Missing dan diulang tanpa efek tambahan
1. Aktor Missing A melakukan Confirm atas record DU-071-1
2. Verifikasi status record DU-071-1 menjadi `Missing`
3. Verifikasi baris transaksi aset DU-071-1 ditutup dalam transaksi atomik yang sama dengan Confirm, menjadi baris `Returned` bermarker `Missing`
4. Catat jumlah node Missing Log, jumlah notifikasi `missing_holder_resolved`, dan nilai `Last Updated` record DU-071-1 sesudah Confirm pertama
5. Aktor Missing A melakukan Confirm atas record DU-071-1 sekali lagi
6. Verifikasi pengulangan Confirm tidak menambah efek: status tetap `Missing`, jumlah node `Report confirmed by` tetap satu, notifikasi `missing_holder_resolved` tidak bertambah, dan `Last Updated` sama dengan sesudah Confirm pertama

### Reject laporan pemegang membawa record ke Rejected dan diulang tanpa efek tambahan
7. Aktor Missing A melakukan Reject atas record DU-071-2 dengan Reason `Aset masih dipegang peminjam`
8. Verifikasi status record DU-071-2 menjadi `Rejected`
9. Verifikasi status global aset DU-071-2 dihitung ulang dari state aset terkini menjadi `Borrowed` karena aset masih dipegang
10. Catat jumlah node Missing Log, jumlah notifikasi `missing_holder_resolved`, dan nilai `Last Updated` record DU-071-2 sesudah Reject pertama
11. Aktor Missing A melakukan Reject atas record DU-071-2 sekali lagi dengan Reason `Aset masih dipegang peminjam`
12. Verifikasi pengulangan Reject tidak menambah efek: status tetap `Rejected`, jumlah node `Report rejected by` tetap satu, notifikasi `missing_holder_resolved` tidak bertambah, dan `Last Updated` sama dengan sesudah Reject pertama

### Cancel Report pelapor membawa record ke Canceled dan diulang ditolak tanpa efek ganda
13. Pemegang aset DU-071-3 melakukan Cancel Report atas laporannya sendiri
14. Verifikasi status record DU-071-3 menjadi `Canceled`
15. Verifikasi status global aset DU-071-3 dihitung ulang dari state aset terkini menjadi `Assigned` karena aset masih dipegang, dan bukan disalin dari status saat laporan dibuat
16. Catat jumlah node Missing Log dan nilai `Last Updated` record DU-071-3 sesudah Cancel Report pertama
17. Pemegang aset DU-071-3 melakukan Cancel Report sekali lagi
18. Verifikasi pengulangan Cancel Report ditolak karena status record sudah berubah, tanpa efek ganda: status tetap `Canceled`, jumlah node `Report canceled by` tetap satu, dan `Last Updated` sama dengan sesudah Cancel Report pertama

### Mark as Found dari Waiting for Confirmation
19. Aktor Missing A melakukan Mark as Found atas record DU-071-4 dengan Found at `Head Office` dan Asset Status `Normal`
20. Verifikasi status record DU-071-4 menjadi `Found`
21. Verifikasi baris transaksi aset DU-071-4 tetap terbuka dan status global aset DU-071-4 bukan `Available`

### Missing keluar ke Reported Disposal atau Found
22. Aktor Missing A melakukan Report Disposal atas record DU-071-5 dengan Reason `Aset tidak ditemukan setelah pencarian`
23. Verifikasi status record DU-071-5 menjadi `Reported Disposal` dengan Condition `Reported Disposal` dan Custody `Available`
24. Verifikasi Report Disposal atas record DU-071-5 tidak memicu event `missing_*` baru dibanding sebelum aksi
25. Aktor Missing A melakukan Mark as Found atas record DU-071-6 dengan Found at `Head Office` dan Asset Status `Normal`
26. Verifikasi status record DU-071-6 menjadi `Found`
27. Verifikasi aset DU-071-6 berstatus `Normal` lalu kembali `Available` di Group aset
28. Catat jumlah node Missing Log, jumlah notifikasi `missing_resolved`, dan nilai `Last Updated` record DU-071-6 sesudah Mark as Found pertama
29. Aktor Missing A melakukan Mark as Found atas record DU-071-6 sekali lagi dengan Found at `Head Office` dan Asset Status `Normal`
30. Verifikasi pengulangan Mark as Found tidak menambah efek: status tetap `Found`, jumlah node `Marked as found by` tetap satu, notifikasi `missing_resolved` tidak bertambah, dan `Last Updated` sama dengan sesudah Mark as Found pertama

### Decline Report mengembalikan Reported Disposal ke Missing
31. Aktor Disposal melakukan Decline atas Disposal Report record DU-071-7 dengan Reason `Aset masih dalam proses pencarian`
32. Verifikasi status record DU-071-7 kembali `Missing`
33. Verifikasi node `Disposal report declined by` pada record DU-071-7 memuat Reason `Aset masih dalam proses pencarian` dan Back to Missing `Yes`
34. Verifikasi Decline Report atas record DU-071-7 tidak memicu event `missing_*` baru dibanding sebelum aksi

### Cancel Disposal Report dan Cancel Report di tab Reported mengembalikan ke Missing
35. Aktor Missing A melakukan Mark as Found atas record DU-071-8 yang berstatus `Reported Disposal`
36. Verifikasi Mark as Found ditolak server: status record DU-071-8 tetap `Reported Disposal` dan tidak ada node `Marked as found by`
37. Aktor Missing A melakukan Cancel Disposal Report atas record DU-071-8
38. Verifikasi status record DU-071-8 kembali `Missing`
39. Verifikasi node `Disposal report canceled by` pada record DU-071-8 memuat Back to Missing `Yes`
40. Verifikasi Cancel Disposal Report atas record DU-071-8 tidak memicu event `missing_*` baru dibanding sebelum aksi
41. Aktor Missing A melakukan Mark as Found atas record DU-071-8 dengan Found at `Head Office` dan Asset Status `Normal`
42. Verifikasi Mark as Found diterima sesudah Cancel Disposal Report: status record DU-071-8 menjadi `Found`
43. Aktor Missing A melakukan Cancel Report atas Disposal Report record DU-071-9 di tab Reported
44. Verifikasi status record DU-071-9 kembali `Missing`
45. Verifikasi node `Disposal report canceled by` pada record DU-071-9 memuat Back to Missing `Yes`
46. Verifikasi Cancel Report atas Disposal Report record DU-071-9 tidak memicu event `missing_*` baru dibanding sebelum aksi

### Dispose dan Submit Request membawa Reported Disposal ke In Disposal Process
47. Aktor Disposal melakukan Dispose dengan Submit Request jenis Write-off atas Report record DU-071-10
48. Verifikasi status record DU-071-10 menjadi `In Disposal Process` dengan Condition `In Disposal Process` dan Custody `Available`, mengikuti Report dan baris Disposal

### Baris Disposal gagal mengembalikan In Disposal Process ke Reported Disposal
49. Baris Disposal Write-off record DU-071-11 ditolak approver
50. Verifikasi status record DU-071-11 kembali `Reported Disposal` dan Report kembali `Reported`, bukan `Missing`
51. Baris Disposal Write-off record DU-071-12 dibatalkan
52. Verifikasi status record DU-071-12 kembali `Reported Disposal` dan Report kembali `Reported`
53. Baris Disposal Write-off record DU-071-13 dihapus
54. Verifikasi status record DU-071-13 kembali `Reported Disposal` dan Report kembali `Reported`
55. Baris Disposal Write-off record DU-071-14 melewati Transaction timeout
56. Verifikasi status record DU-071-14 kembali `Reported Disposal` dan Report kembali `Reported`

### Disposal Executed membawa record ke Disposed dan aksi sesudahnya ditolak
57. Disposal Executed atas baris Disposal Write-off record DU-071-15
58. Verifikasi status record DU-071-15 menjadi `Disposed` dengan Lifecycle `Disposed`
59. Aktor Missing A melakukan Mark as Found atas record DU-071-15 yang sudah `Disposed`
60. Verifikasi Mark as Found ditolak tanpa efek ganda: status record DU-071-15 tetap `Disposed`, dan respons konflik menyebut aktor pengubah `System`

### Record Disposed ikut terhapus bersama aset
61. Aktor Missing A melakukan Delete Asset Data atas aset record DU-071-38
62. Verifikasi record `Disposed` DU-071-38 ikut terhapus permanen bersama aset, tidak lagi ada di riwayat

### Record Found, Rejected, dan Canceled tidak dibuka ulang
63. Aktor Missing A melakukan Confirm atas record DU-071-16 yang berstatus `Found`
64. Verifikasi Confirm ditolak: status record DU-071-16 tetap `Found`
65. Aktor Missing A melakukan Add Update atas record DU-071-16 dengan Update `Pencarian di gudang sudah dilakukan tim operasional`
66. Verifikasi Add Update ditolak karena record sudah selesai: status record DU-071-16 tetap `Found` dan tidak ada node `Update added by`
67. Aktor Missing A melakukan Confirm atas record DU-071-17 yang berstatus `Rejected`
68. Verifikasi Confirm ditolak: status record DU-071-17 tetap `Rejected`
69. Aktor Missing A melakukan Mark as Found atas record DU-071-17 dengan Found at `Head Office` dan Asset Status `Normal`
70. Verifikasi Mark as Found ditolak: status record DU-071-17 tetap `Rejected`
71. Aktor Missing A melakukan Reject atas record DU-071-18 yang berstatus `Canceled` dengan Reason `Aset masih dipegang peminjam`
72. Verifikasi Reject ditolak: status record DU-071-18 tetap `Canceled`
73. Pelapor admin Aktor Missing A melakukan Report Missing atas aset record DU-071-16 dengan What happened `Aset hilang saat dipindahkan antar ruangan`
74. Verifikasi aset DU-071-16 yang hilang lagi mendapat record baru berstatus `Missing`, terpisah dari record DU-071-16
75. Verifikasi record DU-071-16 tidak dibuka ulang: status tetap `Found` dan tetap tampil sebagai riwayat di tab History

### Transisi yang tidak ada di tabel status record ditolak
76. Aktor Missing A melakukan Mark as Found atas record DU-071-19 yang berstatus `Reported Disposal` lewat permintaan basi
77. Verifikasi Mark as Found ditolak server: status record DU-071-19 tetap `Reported Disposal` dan tidak ada node `Marked as found by`
78. Aktor Missing A melakukan Mark as Found atas record DU-071-20 yang berstatus `In Disposal Process` lewat permintaan basi
79. Verifikasi Mark as Found ditolak server: status record DU-071-20 tetap `In Disposal Process` dan tidak ada node `Marked as found by`
80. Aktor Missing A melakukan Cancel Disposal Report atas record DU-071-20 yang berstatus `In Disposal Process`
81. Verifikasi Cancel Disposal Report ditolak karena hanya tersedia pada record `Reported Disposal`: status record DU-071-20 tetap `In Disposal Process`
82. Aktor Missing A melakukan Cancel Disposal Report atas record DU-071-21 yang berstatus `Missing`
83. Verifikasi Cancel Disposal Report ditolak karena hanya tersedia pada record `Reported Disposal`: status record DU-071-21 tetap `Missing`
84. Aktor Disposal melakukan Dispose atas aset record DU-071-21 dengan memilih jenis Write-off, tanpa Report Disposal lebih dulu
85. Verifikasi Dispose ditolak karena aset Missing hanya masuk Disposal lewat Report Disposal: status record DU-071-21 tetap `Missing`, tanpa transisi ke `In Disposal Process`
86. Aktor Missing A mencoba menghapus record DU-071-21
87. Verifikasi server menolak penghapusan: record DU-071-21 tetap ada berstatus `Missing`, karena Missing record tidak dapat dihapus pengguna dan dikoreksi lewat Cancel Report, Reject, atau Mark as Found
88. Aktor Missing A melakukan Report Disposal atas record DU-071-22 yang berstatus `Waiting for Confirmation` dengan Reason `Aset tidak ditemukan setelah pencarian`
89. Verifikasi Report Disposal ditolak karena status record bukan `Missing`: status record DU-071-22 tetap `Waiting for Confirmation`

### Aksi atas record yang sudah diubah pihak lain ditolak tanpa efek ganda
90. Aktor Missing A melakukan Mark as Found atas record DU-071-23 dengan Found at `Head Office` dan Asset Status `Normal`
91. Aktor Missing B melakukan Add Update atas record DU-071-23 dengan Update `Pencarian di lobi sudah dilakukan tim keamanan`
92. Verifikasi Add Update ditolak karena status record sudah diubah pihak lain, tanpa efek ganda: status record DU-071-23 tetap `Found`, tidak ada node `Update added by`, dan respons konflik menyebut Aktor Missing A sebagai pengubah
93. Aktor Missing A melakukan Mark as Found atas record DU-071-24 dengan Found at `Head Office` dan Asset Status `Normal`
94. Aktor Missing B melakukan Confirm atas record DU-071-24
95. Verifikasi Confirm ditolak karena status record sudah diubah pihak lain, tanpa efek ganda: status record DU-071-24 tetap `Found` dan tidak ada node `Report confirmed by`
96. Aktor Missing A melakukan Confirm atas record DU-071-25 lewat Review
97. Aktor Missing B melakukan Reject atas record DU-071-25 dengan Reason `Aset masih dipegang peminjam`
98. Verifikasi Reject ditolak karena status record sudah diubah pihak lain, tanpa efek ganda: status record DU-071-25 tetap `Missing` dan tidak ada node `Report rejected by`
99. Aktor Missing A melakukan Mark as Found atas record DU-071-25 dengan Found at `Head Office` dan Asset Status `Normal`
100. Verifikasi koreksi sesudah Confirm hanya lewat Mark as Found oleh Aktor Missing: status record DU-071-25 menjadi `Found`
101. Aktor Missing A melakukan Confirm atas record DU-071-26 lewat Review
102. Pemegang aset DU-071-26 melakukan Cancel Report atas laporannya
103. Verifikasi Cancel Report ditolak karena record sudah bukan `Waiting for Confirmation`, tanpa efek ganda: status record DU-071-26 tetap `Missing` dan tidak ada node `Report canceled by`
104. Aktor Disposal melakukan Dispose dengan Submit Request jenis Write-off atas Report record DU-071-27
105. Aktor Missing B melakukan Cancel Disposal Report atas record DU-071-27
106. Verifikasi Cancel Disposal Report ditolak karena status record sudah diubah pihak lain, tanpa efek ganda: status record DU-071-27 tetap `In Disposal Process` dan tidak ada node `Disposal report canceled by`

### Add Update tidak idempotent: tiap Submit membuat node baru
107. Aktor Missing A melakukan Add Update atas record DU-071-28 dengan Update `Pencarian di gudang sudah dilakukan tim operasional`
108. Verifikasi jumlah node `Update added by` pada record DU-071-28 bertambah satu
109. Aktor Missing A melakukan Add Update atas record DU-071-28 sekali lagi dengan Update `Pencarian di gudang sudah dilakukan tim operasional`
110. Verifikasi jumlah node `Update added by` bertambah satu lagi karena tiap Submit membuat node baru, sedangkan status record DU-071-28 tetap `Missing` karena Add Update hanya menambah node dan tidak mengubah status

### Tanpa batas tunggu, tanpa penutupan otomatis, Long missing hanya penanda
111. Waktu berlalu sampai 45 hari sejak laporan record DU-071-29 dibuat
112. Verifikasi record DU-071-29 tetap `Waiting for Confirmation` tanpa batas tunggu
113. Verifikasi record DU-071-29 tidak dibatalkan otomatis, tidak menerima notifikasi baru dibanding sebelum aksi, dan tidak mendapat penanda `Long missing`
114. Waktu berlalu sampai 31 hari sejak laporan record DU-071-30 dibuat
115. Job Long missing harian berjalan
116. Verifikasi record DU-071-30 mendapat penanda `Long missing` dan satu notifikasi `missing_long`
117. Verifikasi record DU-071-30 tetap `Missing` dan tidak ditutup otomatis

### Laporan dari Task Detail Audit tanpa hak Aktor Missing menunggu Confirm
118. Pelapor sesi melakukan Report Missing atas aset DU-071-31 dari Task Detail sesi pemeriksaan dengan What happened `Aset hilang saat dipindahkan antar ruangan`
119. Verifikasi record untuk aset DU-071-31 berstatus `Waiting for Confirmation` dan status global aset langsung `Missing`
120. Verifikasi baris transaksi aset DU-071-31 belum ditutup sebelum Confirm
121. Aktor Missing A melakukan Confirm atas record aset DU-071-31
122. Verifikasi status record aset DU-071-31 menjadi `Missing` dan baris transaksi aset DU-071-31 ditutup menjadi baris `Returned` bermarker `Missing`
123. Staff Auditor melakukan Report Missing atas aset DU-071-32 dari Task Detail sesi pemeriksaan dengan What happened `Aset hilang saat dipindahkan antar ruangan`
124. Verifikasi record untuk aset DU-071-32 berstatus `Waiting for Confirmation` dan status global aset langsung `Missing`
125. Pelapor sesi melakukan Cancel my report atas record DU-071-33 dari Task Detail sesi pemeriksaan
126. Verifikasi record DU-071-33 menjadi `Canceled`, status global aset dihitung ulang dari state aset terkini, dan baris sesi pemeriksaan kembali `Pending`
127. Pelapor sesi melakukan Cancel my report atas record DU-071-34 yang sudah diputuskan Aktor Missing
128. Verifikasi Cancel my report ditolak tanpa efek ganda: status record DU-071-34 tetap `Missing` dan tidak ada node `Report canceled by`
129. Pelapor sesi melakukan Cancel my report atas record DU-071-35 yang langsung `Missing`
130. Verifikasi Cancel my report ditolak karena pelapor yang langsung `Missing` tidak memiliki aksi ini: status record DU-071-35 tetap `Missing`

### Write-off hanya lewat Report Disposal atas record Missing dari Reconciliation
131. Aktor Missing A melakukan Report Disposal atas record DU-071-36 dengan Reason `Aset tidak ditemukan setelah pencarian`
132. Verifikasi status record DU-071-36 menjadi `Reported Disposal`
133. Verifikasi Disposal Report dari record DU-071-36 bukan Source `Reconciliation`, karena Disposal tidak punya Source `Reconciliation`

### Condition tersimpan yang tidak dapat dipulihkan menolak Reject dan Cancel Report
134. Aktor Missing A melakukan Reject atas record DU-071-37 dengan Reason `Aset masih dipegang peminjam`
135. Verifikasi Reject ditolak tanpa efek ganda: status record DU-071-37 tetap `Waiting for Confirmation`, status global aset tidak berubah, dan tidak ada node `Report rejected by`
136. Pemegang aset DU-071-37 melakukan Cancel Report atas laporannya
137. Verifikasi Cancel Report ditolak tanpa efek ganda: status record DU-071-37 tetap `Waiting for Confirmation`, status global aset tidak berubah, dan tidak ada node `Report canceled by`
