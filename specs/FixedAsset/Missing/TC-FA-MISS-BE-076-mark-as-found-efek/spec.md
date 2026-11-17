---
id: TC-FA-MISS-BE-076-mark-as-found-efek
title: "Server: hasil Mark as Found per Asset Status, asal Damaged + Missing, TAG Reported, Found at hanya data, pemulihan Condition pada Reject dan Cancel"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [§1.2#r36, §1.2#r37, §1.2#r38, §1.2#r28, §1.2#r29, §1.2#r30, §1.2#r32, §1.2#r33, §1.2#r49, §1.2#r50, §1.2#r57, §1.2#r64, §1.2#r65, §1.2#r66, §1.2#r68, §1.2#r76, §1.2#r78, §1.2#r80, §1.2#r81, §1.2#r82, §1.2#r83, §1.2#r84, §1.2#r85, §1.2#r87, §1.2#r88, §1.2#r89, §1.2#r90, §1.2#r91, §1.2#r92, §9.2#b24, §9.2#b25, §9.2#b26, §9.4.2#r5, §9.4.2#r8, §9.4.2#r10, §9.4.2#r23, §9.4.2#r33, §9.4.2#r7, §9.4.4#r10, §9.4.4#r11, §9.4.4#r12, §9.6#r4, §9.7#r3, §9.7#r4, §9.7#r8, §9.2#r5, §9.2#r7, §9.2#r8, §7.3#r8, §9.4.3#b2, §9.2#b33, §9.4.4#r19, §9.5#r8, §9.9#r3, §4.2.4#p6]
smoke: []
dependsOn: []
trace:
  §1.2#r36: [5, 32]
  §1.2#r37: [6, 17, 22]
  §1.2#r38: 6
  §1.2#r28: 36
  §1.2#r29: 21
  §1.2#r30: 3
  §1.2#r32: 2
  §1.2#r33: 2
  §1.2#r49: [10, 44]
  §1.2#r50: [10, 44]
  §1.2#r57: 51
  §1.2#r64: [47, 52]
  §1.2#r65: 48
  §1.2#r66: 54
  §1.2#r68: [13, 16]
  §1.2#r76: 21
  §1.2#r78: 30
  §1.2#r80: 38
  §1.2#r81: 5
  §1.2#r82: [21, 26]
  §1.2#r83: [22, 26]
  §1.2#r84: [33, 34, 40]
  §1.2#r85: 33
  §1.2#r87: 41
  §1.2#r88: 42
  §1.2#r89: 8
  §1.2#r90: 7
  §1.2#r91: 7
  §1.2#r92: 7
  §9.2#b24: [9, 23]
  §9.2#b25: [5, 35, 40]
  §9.2#b26: [15, 16]
  §9.4.2#r5: [15, 16]
  §9.4.2#r8: [7, 8]
  §9.4.2#r10: [32, 33]
  §9.4.2#r23: 21
  §9.4.2#r33: [38, 40, 43]
  §9.4.2#r7: [46, 49]
  §9.4.4#r10: [23, 26]
  §9.4.4#r11: [8, 12, 32]
  §9.4.4#r12: 16
  §9.6#r4: [11, 35]
  §9.7#r3: [46, 49]
  §9.7#r4: [12, 16]
  §9.7#r8: 51
  §9.2#r5: [5, 17, 21, 32]
  §9.2#r7: 46
  §9.2#r8: 51
  §7.3#r8: [6, 17, 22, 34, 43]
  §9.4.3#b2: 13
  §9.2#b33: [49, 56]
  §9.4.4#r19: [49, 56]
  §9.5#r8: 18
  §9.9#r3: [7, 58]
  §4.2.4#p6: [58, 60]
---

# Server: hasil Mark as Found per Asset Status, asal Damaged + Missing, TAG Reported, Found at hanya data, pemulihan Condition pada Reject dan Cancel

## Prerequisites
- Aktor: Rina W, Total Control dengan cakupan seluruh client; `Maya Anggraini {runId}` (DU-076-1), Group Manager dengan Group binaan Head Office beserta sub-group; `Joko Susilo {runId}` (DU-076-2), pemegang tanpa hak Aktor Missing; `Sari Dewi {runId}` (DU-076-3), pemegang tanpa hak Aktor Missing yang sudah dinonaktifkan.
- Data:
  - DU-076-1: User Name `Maya Anggraini {runId}`, Peran `Group Manager`, Cakupan `Group Head Office beserta sub-group`.
  - DU-076-2: User Name `Joko Susilo {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Cakupan `aset yang ia pegang`.
  - DU-076-3: User Name `Sari Dewi {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Cakupan `aset yang ia pegang`, Status `dinonaktifkan`.
  - DU-076-4: Asset Name `Laptop Dell Latitude 5420 {runId}`, Asset ID `FA076-001`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, Condition sebelum laporan `Normal`, TAG terpasang `QR-076-0001`, Work Order `berjalan`.
  - DU-076-5: Asset Name `Hand Pallet Truck {runId}`, Asset ID `FA076-002`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Sari Dewi {runId}`, Pemegang `Sari Dewi {runId}`, Baris transaksi `terbuka` dengan badge `Reported Missing`, TAG terpasang `tidak ada`.
  - DU-076-6: Asset Name `Projector Epson EB-X06 {runId}`, Asset ID `FA076-003`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, Condition sebelum laporan `Normal`, TAG terpasang `QR-076-0002`.
  - DU-076-7: Asset Name `Printer HP LaserJet M404 {runId}`, Asset ID `FA076-004`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, Condition sebelum laporan `Normal`, TAG terpasang `QR-076-0003`.
  - DU-076-8: Asset Name `Monitor LG 27UL500 {runId}`, Asset ID `FA076-005`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, Condition sebelum laporan `Normal`, TAG terpasang `QR-076-0004`.
  - DU-076-9: Asset Name `Toyota Innova {runId}`, Asset ID `FA076-006`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, Condition sebelum laporan `Normal`, TAG terpasang `tidak ada`.
  - DU-076-10: Asset Name `Genset Honda EU22 {runId}`, Asset ID `FA076-007`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, Condition sebelum laporan `Damaged`, TAG terpasang `tidak ada`, Damage record `berjalan dan ditahan`, Work Order `berjalan`.
  - DU-076-11: Asset Name `Tablet Samsung Tab A8 {runId}`, Asset ID `FA076-008`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`, Baris transaksi `terbuka` dengan badge `Reported Missing`, Condition sebelum laporan `Damaged`, Damage record `berjalan dan ditahan`, Tagging `Tag Reported`, Activity Lock `In Audit`.
  - DU-076-12: Asset Name `Kamera Sony A7 {runId}`, Asset ID `FA076-009`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`, Condition sebelum laporan `Damaged`, Damage record `berjalan dan ditahan`.
  - DU-076-13: Asset Name `Brankas Besi {runId}`, Asset ID `FA076-010`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`, Condition sebelum laporan `Damaged, tidak lagi dapat dipulihkan`.
  - DU-076-14: Asset Name `Scanner Zebra DS2208 {runId}`, Asset ID `FA076-011`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`, Condition sebelum laporan `Normal`.
  - DU-076-15: Asset Name `Kursi Ergonomis {runId}`, Asset ID `FA076-012`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, Condition sebelum laporan `Normal`, TAG terpasang `tidak ada`.
  - DU-076-16: Berkas Berkas `foto-kerusakan-076.png`, Format `PNG`, Ukuran `800 KB`.

## Test Steps
### Aset Missing tidak layak untuk transaksi baru dan Group serta TAG tidak berubah
1. Rina W membuat transaksi baru atas aset `Kursi Ergonomis {runId}` yang berstatus global Missing
2. Verifikasi permintaan itu ditolak karena aset berstatus global Missing, dan tidak ada transaksi baru yang tercatat atas `Kursi Ergonomis {runId}`
3. Verifikasi record `Laptop Dell Latitude 5420 {runId}` berstatus `Missing` dan Group serta TAG aset tidak berubah karena dilaporkan

### Mark as Found Normal mengembalikan aset Available di Group aset dan Found at hanya data
4. Rina W mengirim Mark as Found atas record `Laptop Dell Latitude 5420 {runId}` dengan Scan TAG `QR-076-0001` terverifikasi, Found at `Server Room`, Asset Status `Normal`, dan Note dikosongkan
5. Verifikasi record `Laptop Dell Latitude 5420 {runId}` berstatus `Found` dan status global aset menjadi Normal lalu Available
6. Verifikasi hasil sukses memuat pesan `Success, [Asset Name] is available again.` dengan nama aset `Laptop Dell Latitude 5420 {runId}`
7. Verifikasi Group aset `Laptop Dell Latitude 5420 {runId}` tetap `Finance Room` dan aset tidak dipindahkan ke `Server Room`
8. Verifikasi Found at `Server Room` tercatat di Missing Log dan di Resolution record sebagai tempat aset ditemukan
9. Verifikasi node `Marked as found by` memuat waktu yang sama dengan waktu Submit
10. Verifikasi tidak ada Damage Report baru dan Work Order `Laptop Dell Latitude 5420 {runId}` tidak berubah oleh Mark as Found
11. Verifikasi aksi itu atomik: record `Found` dan status global aset tercatat bersama, tanpa salah satunya saja
12. Verifikasi event `missing_resolved` dikirim untuk record `Laptop Dell Latitude 5420 {runId}`

### Ditemukan dari Waiting for Confirmation menjaga baris transaksi pemegang tetap terbuka
13. Verifikasi baris transaksi aset `Hand Pallet Truck {runId}` tetap terbuka selama record berstatus `Waiting for Confirmation` walau pemegangnya sudah dinonaktifkan
14. Rina W mengirim Mark as Found atas record `Hand Pallet Truck {runId}` dengan Found at default Group aset dan Asset Status `Normal`
15. Verifikasi record `Hand Pallet Truck {runId}` berstatus `Found` langsung dari `Waiting for Confirmation`
16. Verifikasi baris transaksi aset `Hand Pallet Truck {runId}` tetap terbuka dan badge `Reported Missing` hilang
17. Verifikasi status global aset `Hand Pallet Truck {runId}` bukan Available karena baris transaksi masih terbuka, dan hasil sukses memuat pesan `Success, asset has been marked as found.`
18. Verifikasi Found at tersimpan sebagai Group aset karena Found at tidak diubah dari bawaan

### Ditemukan lewat I Can't Scan the TAG menambah Tagging Tag Reported tanpa menjadi Available
19. Rina W menyimpan Report TAG identifikasi manual atas aset `Projector Epson EB-X06 {runId}` lewat `I Can't Scan the TAG`
20. Rina W mengirim Mark as Found atas record `Projector Epson EB-X06 {runId}` dengan Asset Status `Normal`
21. Verifikasi record `Projector Epson EB-X06 {runId}` berstatus `Found`, Tagging `Tag Reported` tetap sebagai overlay terpisah, dan status global aset bukan Available
22. Verifikasi Condition aset `Projector Epson EB-X06 {runId}` mengikuti Asset Status `Normal` tanpa nama status baru, dan hasil sukses memuat pesan `Success, asset has been marked as found.`
23. Verifikasi node `Marked as found by` mencatat Manual identification
24. Rina W menyimpan Report TAG identifikasi manual atas aset `Printer HP LaserJet M404 {runId}` lewat `I Can't Scan the TAG`
25. Rina W mengirim Mark as Found atas record `Printer HP LaserJet M404 {runId}` dengan Asset Status `Damaged`, Damaged Photo `foto-kerusakan-076.png`, dan Note `Layar retak dan bodi penyok pada sisi kiri`
26. Verifikasi record `Printer HP LaserJet M404 {runId}` berstatus `Found`, Tagging `Tag Reported` tetap, dan Condition aset mengikuti Asset Status `Damaged`

### Scan berhasil sebelum Submit membatalkan Report TAG dan hasilnya Available
27. Rina W menyimpan Report TAG identifikasi manual atas aset `Monitor LG 27UL500 {runId}` lewat `I Can't Scan the TAG`
28. Rina W memindai TAG `QR-076-0004` milik `Monitor LG 27UL500 {runId}` sebelum Submit
29. Rina W mengirim Mark as Found atas record `Monitor LG 27UL500 {runId}` dengan Asset Status `Normal`
30. Verifikasi Report TAG atas `Monitor LG 27UL500 {runId}` berstatus Canceled otomatis dan status global aset menjadi Available

### Ditemukan rusak membuat Damage Report dari Damaged Photo dan Note
31. Rina W mengirim Mark as Found atas record `Toyota Innova {runId}` dengan Asset Status `Damaged`, Damaged Photo `foto-kerusakan-076.png`, dan Note `Layar retak dan bodi penyok pada sisi kiri`
32. Verifikasi status global aset `Toyota Innova {runId}` menjadi `Damaged` lalu Available, dan record berstatus `Found`
33. Verifikasi Damage Report baru dengan Source `Missing Asset` dibuat dengan Damaged Photo dan Note itu serta tautan ke Missing Log record `Toyota Innova {runId}`
34. Verifikasi hasil sukses memuat pesan `Success, [Asset Name] is available again. A damage report has been created.`
35. Verifikasi record `Found`, status global aset, dan Damage Report tercatat bersama, tanpa salah satunya saja

### Asal Damaged + Missing memakai Damage record yang ditahan
36. Verifikasi aset `Genset Honda EU22 {runId}` yang dilaporkan dengan Condition sebelum laporan `Damaged` tampil `Damaged + Missing` dan Damage record-nya ditahan
37. Rina W mengirim Mark as Found atas record `Genset Honda EU22 {runId}` dengan Asset Status `Normal`
38. Verifikasi permintaan itu ditolak karena Asset Status terisi `Damaged` dan tidak dapat diubah, dan record `Genset Honda EU22 {runId}` tetap `Missing`
39. Rina W mengirim Mark as Found atas record `Genset Honda EU22 {runId}` dengan Asset Status `Damaged`, Damaged Photo `foto-kerusakan-076.png`, dan Note `Layar retak dan bodi penyok pada sisi kiri`
40. Verifikasi record `Genset Honda EU22 {runId}` berstatus `Found` tanpa Damage Report baru
41. Verifikasi Damaged Photo dan Note tersimpan sebagai node baru pada Damage record yang ditahan
42. Verifikasi Damaged Photo dan Note juga tercatat di node `Marked as found by`
43. Verifikasi hasil sukses memuat pesan `Success, [Asset Name] is available again.` tanpa kalimat damage report
44. Verifikasi record lain aset `Genset Honda EU22 {runId}` selain Damage record yang ditahan, termasuk Work Order, tidak berubah

### Reject dan Cancel Report memulihkan Condition dan status global aset
45. Rina W mengirim Reject atas record `Tablet Samsung Tab A8 {runId}` dengan Reason `Aset terlihat di ruang kerja pemegang`
46. Verifikasi record `Tablet Samsung Tab A8 {runId}` berstatus `Rejected` dan status global aset kembali seperti sebelum laporan, dan badge `Reported Missing` pada baris transaksi aset hilang
47. Verifikasi Condition aset `Tablet Samsung Tab A8 {runId}` dipulihkan menjadi `Damaged` dan Damage record aktif kembali
48. Verifikasi Tagging `Tag Reported`, Activity Lock `In Audit`, dan Custody aset `Tablet Samsung Tab A8 {runId}` tidak berubah oleh Reject
49. Verifikasi `Joko Susilo {runId}` menerima notifikasi `missing_holder_resolved` berisi Reason itu, dan node `Report rejected by` memuat Reason yang sama
50. `Joko Susilo {runId}` mengirim Cancel Report atas record `Kamera Sony A7 {runId}`
51. Verifikasi record `Kamera Sony A7 {runId}` berstatus `Canceled` dan status global aset kembali seperti sebelum laporan
52. Verifikasi Condition aset `Kamera Sony A7 {runId}` dipulihkan menjadi `Damaged` dan Damage record aktif kembali

### Condition tersimpan yang tidak dapat dipulihkan menolak Reject
53. Rina W mengirim Reject atas record `Brankas Besi {runId}` dengan Reason `Aset masih tercatat di gudang cabang`
54. Verifikasi permintaan itu ditolak dengan `D-MIS-06` tanpa efek ganda, record `Brankas Besi {runId}` tetap `Waiting for Confirmation`, dan Reason tidak tercatat

### Confirm laporan pemegang memberi tahu pemegang
55. Rina W menjalankan Confirm atas record `Scanner Zebra DS2208 {runId}`
56. Verifikasi record `Scanner Zebra DS2208 {runId}` berstatus `Missing` dan `Joko Susilo {runId}` menerima notifikasi `missing_holder_resolved`

### Opsi Found at mengikuti cakupan aktor
57. `Maya Anggraini {runId}` meminta opsi Found at untuk record `Kursi Ergonomis {runId}` yang Group-nya `Finance Room`
58. Verifikasi opsi itu memuat `Finance Room` sebagai Group aset default dan `Server Room` yang dapat dipilih, `Head Office` sebagai induk yang tidak dapat dipilih, dan tidak memuat `Warehouse`
59. Rina W meminta opsi Found at untuk record `Kursi Ergonomis {runId}`
60. Verifikasi opsi itu memuat `Warehouse` karena Total Control melihat seluruh Group
