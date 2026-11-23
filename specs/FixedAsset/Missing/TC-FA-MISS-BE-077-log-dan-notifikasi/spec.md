---
id: TC-FA-MISS-BE-077-log-dan-notifikasi
title: "Server: satu node dan satu entri log per item, aktor System tanpa System Log, Cancel Report tanpa Transaction admin log, dan event per aksi"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [§8#r1, §8#r2, §8#r3, §8#r4, §8#r5, §8#r6, §8#r7, §8#r8, §8#r9, §8#r10, §8#r11, §8#p2, §8.1#p2, §8.2#b1, §8.2#b2, §8.2#b3, §9.2#b21, §9.4.4#r16, §9.4.4#r18, §9.4.4#r19, §9.8#p1, §9.8#r1, §9.8#r2, §9.8#r3, §9.8#r4, §9.8#r5, §9.8#r6, §9.8#r7, §9.8#p2, §9.8#p3, §9.6#r1, §9.6#r2, §9.6#r3, §9.6#r4, §9.6#r5, §9.6#r7, §9.6#r8, §9.6#r9, §9.6#r10, §9.6#r11, §9.5#r7, §9.7#p1, §9.7#r1, §9.7#r2, §9.7#r3, §9.7#r4, §9.7#r5, §9.7#r6, §9.7#r7, §9.7#r8, §9.7#r9, §9.7#r10, EB-LOG-1, §4.1a#r27, §4.1a#r28, §9.4.1#r8, §9.4.1#r10, §9.4.1#r9, §9.4.1#r2, §1.2#r115, §9.4.4#r23, §1.2#r72, §9.2#b38, §9.4.2#r39, §9.4.4#r24, §8.2#p4, §8.2#p5, §8.2#p6, §8.2#p7, §8.2#p8, §8.2#p9, §8.2#p10, §8.2#p14, §8.2#p15, §8.2#p16, §8.2#p17, §8.2#p18, §8.2#p21, §8.2#p22, §8.2#p23, §8.2#p24, §8.2#p25, §8.2#p26, §8.2#p27, §8.1#r12, §3#p4, §1.2#r61, §3#p8, §9.4.2#r11]
smoke: []
dependsOn: []
trace:
  §8#r1: 3
  §8#r2: 3
  §8#r3: 3
  §8#r4: [6, 14, 17, 19, 23, 28, 32, 36]
  §8#r5: [55, 58]
  §8#r6: [3, 4, 5, 30, 71, 72]
  §8#r7: [14, 74]
  §8#r8: [55, 56]
  §8#r9: [58, 59]
  §8#r10: [63, 64]
  §8#r11: [39, 42, 44, 45]
  §8#p2: [45, 74]
  §8.1#p2: [47, 49, 50, 52, 91]
  §8.2#b1: [7, 14, 20, 29, 33, 75, 106, 107]
  §8.2#b2: [7, 14, 20, 24, 29, 33, 37, 42, 102]
  §8.2#b3: 74
  §9.2#b21: [4, 71, 72]
  §9.4.4#r16: [39, 44]
  §9.4.4#r18: [49, 50, 53]
  §9.4.4#r19: [52, 53]
  §9.8#p1: 8
  §9.8#r1: 8
  §9.8#r2: [12, 94]
  §9.8#r3: [15, 21]
  §9.8#r4: 55
  §9.8#r5: [65, 67, 69, 88, 90]
  §9.8#r6: [58, 61]
  §9.8#r7: [34, 44]
  §9.8#p2: [36, 39, 42, 44, 47, 53, 79, 81, 83, 85]
  §9.8#p3: [16, 129, 130, 131, 132]
  §9.6#r1: [3, 6, 7]
  §9.6#r2: [14, 17]
  §9.6#r3: [19, 20]
  §9.6#r4: [32, 33]
  §9.6#r5: [28, 29]
  §9.6#r7: [23, 24, 25]
  §9.6#r8: [63, 65, 67, 69]
  §9.6#r9: [36, 37, 42]
  §9.6#r10: [71, 72]
  §9.6#r11: [58, 61]
  §9.5#r7: [67, 69, 88, 90]
  §9.7#p1: 10
  §9.7#r1: [7, 8]
  §9.7#r2: [12, 94]
  §9.7#r3: [21, 127]
  §9.7#r4: 34
  §9.7#r5: [36, 44, 47]
  §9.7#r6: 55
  §9.7#r7: 58
  §9.7#r8: [25, 128]
  §9.7#r9: 28
  §9.7#r10: [63, 65]
  EB-LOG-1: [5, 30]
  §4.1a#r27: [56, 59]
  §4.1a#r28: [56, 59]
  §9.4.1#r8: 8
  §9.4.1#r10: 74
  §9.4.1#r9: [3, 4]
  §9.4.1#r2: 9
  §1.2#r115: 58
  §9.4.4#r23: [98]
  §1.2#r72: [94]
  §9.2#b38: [94]
  §9.4.2#r39: [94]
  §9.4.4#r24: [93, 94]
  §8.2#p4: [107]
  §8.2#p5: [95]
  §8.2#p6: [108]
  §8.2#p7: [109]
  §8.2#p8: [110]
  §8.2#p9: [111]
  §8.2#p10: [112, 113, 114, 115, 116, 117, 118, 119, 120, 121]
  §8.2#p14: [104]
  §8.2#p15: [102]
  §8.2#p16: [103]
  §8.2#p17: [102]
  §8.2#p18: [105, 134, 135]
  §8.2#p21: [96, 102]
  §8.2#p22: [99]
  §8.2#p23: [122]
  §8.2#p24: [123]
  §8.2#p25: [102, 124]
  §8.2#p26: [125]
  §8.2#p27: [24, 126]
  §8.1#r12: [63, 91]
  §3#p4: [14, 19, 23, 127]
  §1.2#r61: [19, 127]
  §3#p8: [32, 36, 39, 42, 44, 47]
  §9.4.2#r11: [39, 47]
---

# Server: satu node dan satu entri log per item, aktor System tanpa System Log, Cancel Report tanpa Transaction admin log, dan event per aksi

## Prerequisites
- Aktor: Rina W, Total Control dengan cakupan seluruh client sebagai Aktor Missing dan Aktor Disposal; `Joko Susilo {runId}` (DU-077-1), pemegang tanpa hak Aktor Missing; `Agus Pratama {runId}` (DU-077-2) dan `Budi Hartono {runId}` (DU-077-3), pengguna terautentikasi tanpa hak Aktor Missing sebagai penemu; `Sabrina Putri {runId}` (DU-077-36), Staff Auditor tanpa hak Aktor Missing; approver Disposal dan job sistem hanya sebagai pemicu keadaan.
- Data:
  - DU-077-1: User Name `Joko Susilo {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Cakupan `aset yang ia pegang`.
  - DU-077-2: User Name `Agus Pratama {runId}`, Peran `pengguna terautentikasi tanpa hak Aktor Missing`, Cakupan `tanpa cakupan Group`.
  - DU-077-3: User Name `Budi Hartono {runId}`, Peran `pengguna terautentikasi tanpa hak Aktor Missing`, Cakupan `tanpa cakupan Group`.
  - DU-077-4: Asset Name `Laptop Dell Latitude 5420 {runId}`, Asset ID `FA077-001`, Group aset `Finance Room`, Record berjalan `tidak ada`.
  - DU-077-5: Asset Name `Hand Pallet Truck {runId}`, Asset ID `FA077-002`, Group aset `Finance Room`, Record berjalan `tidak ada`.
  - DU-077-6: Asset Name `Drill Bosch GSB {runId}`, Asset ID `FA077-003`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-077-7: Asset Name `Camera Canon EOS {runId}`, Asset ID `FA077-004`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-077-8: Asset Name `Scanner Zebra DS2208 {runId}`, Asset ID `FA077-005`, Group aset `Finance Room`, Record berjalan `tidak ada`, Pemegang `Joko Susilo {runId}`.
  - DU-077-9: Asset Name `Printer HP LaserJet M404 {runId}`, Asset ID `FA077-006`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`, Transaksi pemegang `Borrow`.
  - DU-077-10: Asset Name `Monitor LG 27UL500 {runId}`, Asset ID `FA077-007`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`, Transaksi pemegang `Borrow`.
  - DU-077-11: Asset Name `Projector Epson EB-X06 {runId}`, Asset ID `FA077-008`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-077-12: Asset Name `Toyota Innova {runId}`, Asset ID `FA077-009`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `tidak ada`.
  - DU-077-13: Asset Name `Genset Honda EU22 {runId}`, Asset ID `FA077-010`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-077-14: Asset Name `Tablet Samsung Tab A8 {runId}`, Asset ID `FA077-011`, Group aset `Finance Room`, Record berjalan `In Disposal Process, dilaporkan Rina W`. Disposal No. dibentuk server saat Disposal Executed dan menjadi milik DU-077-14.
  - DU-077-15: Asset Name `Kamera Sony A7 {runId}`, Asset ID `FA077-012`, Group aset `Finance Room`, Record berjalan `In Disposal Process, dilaporkan Rina W`.
  - DU-077-16: Asset Name `Brankas Besi {runId}`, Asset ID `FA077-013`, Group aset `Finance Room`, Record berjalan `tidak ada`, Disposal Report `Reported`.
  - DU-077-17: Asset Name `Kursi Ergonomis {runId}`, Asset ID `FA077-014`, Group aset `Finance Room`, Record berjalan `tidak ada`, Baris Disposal `Sell, Waiting for Approval`.
  - DU-077-18: Asset Name `Meja Rapat Kayu {runId}`, Asset ID `FA077-018`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`.
  - DU-077-19: Asset Name `Meja Kerja Kayu {runId}`, Asset ID `FA077-015`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `QR-077-0001`.
  - DU-077-20: Asset Name `Papan Tulis {runId}`, Asset ID `FA077-016`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, Reported Date `T0 − 30 hari, pukul 09:00`.
  - DU-077-21: Asset Name `Rak Besi Gudang {runId}`, Asset ID `FA077-017`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `QR-077-0002`.
  - DU-077-22: Berkas Berkas `foto-penemuan-077.jpg`, Format `JPG`, Ukuran `600 KB`.
  - DU-077-23: Lokasi Latitude `-6.200000`, Longitude `106.816667`.
  - DU-077-28: Asset Name `Lemari Arsip Besi {runId}`, Asset ID `FA077-019`, Group aset `Finance Room`, Record berjalan `Reported Disposal, dilaporkan Rina W`.
  - DU-077-29: Asset Name `Kipas Angin Standing {runId}`, Asset ID `FA077-020`, Group aset `Finance Room`, Record berjalan `In Disposal Process, dilaporkan Rina W`.
  - DU-077-30: Asset Name `Mesin Fotokopi Ricoh {runId}`, Asset ID `FA077-021`, Group aset `Finance Room`, Record berjalan `In Disposal Process, dilaporkan Rina W`.
  - DU-077-31: Asset Name `Mesin Cuci Industri {runId}`, Asset ID `FA077-022`, Group aset `Finance Room`, Record berjalan `In Disposal Process, dilaporkan Rina W`.
  - DU-077-36: User Name `Sabrina Putri {runId}`, Peran `Staff Auditor tanpa hak Aktor Missing`, Cakupan `aset dalam sesinya sendiri`.
  - DU-077-37: Sesi Audit `Audit Gudang {runId}` milik `Sabrina Putri {runId}`, memuat aset DU-077-38 dan DU-077-39.
  - DU-077-38: Asset Name `Kabinet Server {runId}`, Asset ID `FA077-023`, Group aset `Finance Room`, Record berjalan `tidak ada`, termasuk dalam sesi Audit `Audit Gudang {runId}`.
  - DU-077-39: Asset Name `Meja Resepsionis {runId}`, Asset ID `FA077-024`, Group aset `Finance Room`, Record berjalan `tidak ada`, termasuk dalam sesi Audit `Audit Gudang {runId}`.
- Kondisi:
  - Long missing after bernilai `30`
  - Date Format bernilai `DD/MM/YY`
  - Time Format bernilai `HH:mm`

## Test Steps
### Report Missing banyak aset menulis satu record, satu node, dan satu entri log per aset yang diproses
1. Catat jumlah entri Activity Log dan System Log Rina W, serta jumlah node record `Camera Canon EOS {runId}`, sebelum laporan
2. Rina W mengirim Report Missing atas `Laptop Dell Latitude 5420 {runId}`, `Hand Pallet Truck {runId}`, dan `Drill Bosch GSB {runId}` dalam satu laporan dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
3. Verifikasi `Laptop Dell Latitude 5420 {runId}` dan `Hand Pallet Truck {runId}` masing-masing mendapat satu record dan satu node `Reported missing by`, sedangkan `Drill Bosch GSB {runId}` tidak mendapat record maupun node baru
4. Verifikasi Activity Log dan System Log Rina W masing-masing bertambah dua entri, satu per aset yang diproses, dan tidak ada entri untuk `Drill Bosch GSB {runId}` yang dilewati
5. Verifikasi record `Camera Canon EOS {runId}` yang tidak terlibat tidak mendapat node atau entri log baru
6. Verifikasi node `Reported missing by` pada `Laptop Dell Latitude 5420 {runId}` dan `Hand Pallet Truck {runId}` atas nama Rina W memuat What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
7. Verifikasi Transaction log aset memuat `Reported missing` untuk `Laptop Dell Latitude 5420 {runId}` dan `Hand Pallet Truck {runId}`, dan Transaction admin log Rina W sub-tab Missing memuat Report Missing oleh Pelapor admin dengan Activity `Reported missing`, Name aset, Source yang sama dengan Source record itu, dan Group aset saat tindakan
8. Verifikasi Aktor Missing Group aset menerima event `missing_reported` untuk setiap record yang dibuat
9. Verifikasi laporan itu tidak ditolak karena plan, karena Report Missing tersedia di semua plan
10. Verifikasi status record dan status global aset terbaca konsisten dari sumber masing-masing, sehingga tampilan turunan banner aset dan status laporan pemegang hanya menurunkan data itu

### Laporan pemegang dan Confirm menulis log dan event milik pemegang
11. `Joko Susilo {runId}` mengirim Report Missing atas `Scanner Zebra DS2208 {runId}` yang ia pegang dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
12. Verifikasi Aktor Missing Group aset menerima event `missing_holder_reported` dan tidak menerima event `missing_reported` untuk record `Scanner Zebra DS2208 {runId}`
13. Rina W menjalankan Confirm atas record `Scanner Zebra DS2208 {runId}`
14. Verifikasi record `Scanner Zebra DS2208 {runId}` memuat node `Report confirmed by` atas nama Rina W, Transaction log aset memuat `Report confirmed`, dan Transaction admin log Rina W memuat Confirm
15. Verifikasi `Joko Susilo {runId}` menerima event `missing_holder_resolved` untuk record `Scanner Zebra DS2208 {runId}`
16. Verifikasi notifikasi `missing_holder_reported` untuk record `Scanner Zebra DS2208 {runId}` ditandai selesai otomatis setelah Confirm
17. Verifikasi System Log Rina W memuat Confirm sebagai aktor, sedangkan target aksi adalah record yang dipegang `Joko Susilo {runId}`

### Reject menulis node dengan Reason dan event ke pemegang
18. Rina W mengirim Reject atas record `Printer HP LaserJet M404 {runId}` dengan Reason `Aset terlihat di ruang kerja pemegang`
19. Verifikasi record `Printer HP LaserJet M404 {runId}` memuat node `Report rejected by` atas nama Rina W dengan Reason `Aset terlihat di ruang kerja pemegang`
20. Verifikasi Transaction log aset memuat `Report rejected` dan Transaction admin log Rina W memuat Reject
21. Verifikasi `Joko Susilo {runId}` menerima event `missing_holder_resolved` untuk record `Printer HP LaserJet M404 {runId}`

### Cancel Report oleh pemegang tidak masuk Transaction admin log
22. `Joko Susilo {runId}` mengirim Cancel Report atas record `Monitor LG 27UL500 {runId}`
23. Verifikasi record `Monitor LG 27UL500 {runId}` memuat node `Report canceled by` atas nama `Joko Susilo {runId}`
24. Verifikasi Transaction admin log tidak memuat Cancel Report oleh `Joko Susilo {runId}` sebagai pemegang, karena riwayatnya hanya di Missing Log dan User Log
25. Verifikasi status record dan status global aset `Monitor LG 27UL500 {runId}` berubah bersama dan tidak ada event `missing_*` yang dikirim

### Add Update menulis node dan Transaction admin log tanpa Transaction log aset
26. Catat jumlah entri Transaction log aset `Projector Epson EB-X06 {runId}` dan jumlah entri log record `Camera Canon EOS {runId}` sebelum Add Update
27. Rina W mengirim Add Update atas record `Projector Epson EB-X06 {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
28. Verifikasi record `Projector Epson EB-X06 {runId}` memuat node `Update added by` atas nama Rina W dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
29. Verifikasi Transaction admin log Rina W memuat Add Update dan Transaction log aset `Projector Epson EB-X06 {runId}` tidak bertambah
30. Verifikasi record `Camera Canon EOS {runId}` tetap tanpa node atau entri log baru

### Mark as Found menulis node, log aset, dan event missing_resolved
31. Rina W mengirim Mark as Found atas record `Toyota Innova {runId}` dengan Found at default Group aset dan Asset Status `Normal`
32. Verifikasi record `Toyota Innova {runId}` memuat node `Marked as found by` atas nama Rina W
33. Verifikasi Transaction log aset memuat `Marked as found` dan Transaction admin log Rina W memuat Mark as Found
34. Verifikasi event `missing_resolved` dikirim untuk record `Toyota Innova {runId}` dan status global aset berubah bersama record

### Peristiwa Disposal menulis node Missing Log tanpa event missing
35. Rina W menjalankan Report Disposal atas record `Genset Honda EU22 {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
36. Verifikasi record `Genset Honda EU22 {runId}` memuat node `Disposal reported by` dengan Report ID dan Reason `Aset tidak ditemukan setelah pencarian dua pekan`, dan tidak ada event `missing_*` yang dikirim untuk transisi itu
37. Verifikasi Transaction admin log Rina W memuat Report Disposal pada sub-tab Disposal
38. Aktor Disposal menjalankan Decline Report atas laporan disposal `Genset Honda EU22 {runId}`
39. Verifikasi record `Genset Honda EU22 {runId}` memuat node `Disposal report declined by` dengan Back to Missing `Yes` dan tidak ada event `missing_*` untuk Decline
40. Rina W menjalankan Report Disposal atas record `Genset Honda EU22 {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
41. Rina W menjalankan Cancel Disposal Report atas record `Genset Honda EU22 {runId}`
42. Verifikasi record `Genset Honda EU22 {runId}` memuat node `Disposal report canceled by` dengan Back to Missing `Yes`, dan Transaction admin log Rina W memuat Cancel Disposal Report pada sub-tab Disposal
43. Disposal Executed untuk aset `Tablet Samsung Tab A8 {runId}`
44. Verifikasi record `Tablet Samsung Tab A8 {runId}` memuat node `Disposed` atas nama `System` dengan Disposal No. milik DU-077-14, dan event `missing_resolved` dikirim
45. Verifikasi Activity Log mencatat peristiwa itu dengan Modified By `System` dan System Log tidak mendapat entri aktor, karena tidak ada pengguna aktor
46. Baris Disposal aset `Kamera Sony A7 {runId}` ditolak approver Disposal
47. Verifikasi record `Kamera Sony A7 {runId}` kembali `Missing` dan tidak ada event `missing_*` untuk transisi itu, sedangkan node log mengikuti peristiwa Disposal yang sama

### Report Missing atas aset dengan Report atau baris Disposal berjalan tidak menulis node Disposal di Missing Log
48. Rina W mengirim Report Missing atas `Brankas Besi {runId}` yang punya Disposal Report `Reported` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
49. Verifikasi Report Disposal `Brankas Besi {runId}` menjadi Canceled oleh `System` dengan alasan `Asset reported missing` di log Report Disposal
50. Verifikasi Missing Log record `Brankas Besi {runId}` dimulai dari node `Reported missing by` dan tidak memuat node apa pun untuk pembatalan Report itu
51. Rina W mengirim Report Missing atas `Kursi Ergonomis {runId}` yang punya baris Disposal Sell berstatus Waiting for Approval dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
52. Verifikasi baris Disposal `Kursi Ergonomis {runId}` menjadi Canceled oleh `System` dengan alasan `Asset reported missing`, dan Missing Log record baru hanya memuat node `Reported missing by`
53. Verifikasi pembatalan oleh `System` itu tidak mengirim event `missing_*` selain `missing_reported` milik laporan baru

### Jalur non-form scan, job, dan I found it dicatat dengan aktor yang benar
54. `Agus Pratama {runId}` memindai TAG `QR-077-0001` milik `Meja Kerja Kayu {runId}`
55. Verifikasi record `Meja Kerja Kayu {runId}` memuat node `Detected by scan` dan Aktor Missing menerima event `missing_detected`
56. Verifikasi Modified By dan Last Updated record `Meja Kerja Kayu {runId}` diperbarui oleh `System`, tanpa System Log atas nama pengguna
57. Job Long missing harian berjalan
58. Verifikasi record `Papan Tulis {runId}` memuat node `Long missing` atas nama `System` dan Activity Log dengan Modified By `System`, tanpa System Log
59. Verifikasi Modified By dan Last Updated record `Papan Tulis {runId}` diperbarui oleh `System`
60. Job Long missing harian berjalan lagi pada hari berikutnya
61. Verifikasi record `Papan Tulis {runId}` tidak menerima event `missing_long` baru dan tetap memuat satu node `Long missing`
62. `Agus Pratama {runId}` mengirim I found it atas record `Rak Besi Gudang {runId}` dengan Photo `foto-penemuan-077.jpg` dan lokasi perangkat Latitude `-6.200000` Longitude `106.816667`
63. Verifikasi record `Rak Besi Gudang {runId}` memuat node `Reported found by` atas nama `Agus Pratama {runId}` dengan Location dan Photo
64. Verifikasi Activity Log dan System Log `Agus Pratama {runId}` masing-masing memuat satu entri untuk pengiriman itu
65. Verifikasi Aktor Missing menerima event `missing_found_reported` satu kali dan status record serta status global aset tidak berubah
66. `Agus Pratama {runId}` mengirim lagi I found it atas record `Rak Besi Gudang {runId}` dalam jendela 1 jam
67. Verifikasi record `Rak Besi Gudang {runId}` mendapat node `Reported found by` kedua tanpa event `missing_found_reported` baru untuk `Agus Pratama {runId}`
68. `Budi Hartono {runId}` mengirim I found it atas record `Rak Besi Gudang {runId}` tanpa izin lokasi
69. Verifikasi node `Reported found by` atas nama `Budi Hartono {runId}` memuat Location `—` dan Aktor Missing menerima event `missing_found_reported` untuk `Budi Hartono {runId}`

### Bulk Report Disposal menulis satu node per record yang diproses
70. Rina W menjalankan Bulk Report Disposal atas `Laptop Dell Latitude 5420 {runId}`, `Hand Pallet Truck {runId}`, dan `Meja Rapat Kayu {runId}` dalam satu Group dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
71. Verifikasi `Laptop Dell Latitude 5420 {runId}` dan `Hand Pallet Truck {runId}` masing-masing memuat satu node `Disposal reported by`, sedangkan `Meja Rapat Kayu {runId}` yang berstatus `Waiting for Confirmation` dilewati tanpa node
72. Verifikasi Activity Log dan System Log Rina W bertambah satu entri per record yang diproses dan tidak ada entri untuk `Meja Rapat Kayu {runId}`

### Download dan aksi tanpa catatan tidak menulis log
73. Rina W meminta Download daftar sub-tab Active
74. Verifikasi tidak ada entri log baru yang dicatat karena Download tidak dicatat dan tidak ada modal Changelog

### Disposal Executed menulis entri Disposed di Transaction log aset
75. Verifikasi Transaction log aset `Tablet Samsung Tab A8 {runId}` memuat entri `Disposed`

### Transisi Disposal lain tidak mengirim event missing
76. Catat jumlah event `missing_*` atas record `Lemari Arsip Besi {runId}`, `Kipas Angin Standing {runId}`, `Mesin Fotokopi Ricoh {runId}`, dan `Mesin Cuci Industri {runId}` sebelum transisi
77. Aktor Disposal menjalankan Dispose atas laporan disposal `Lemari Arsip Besi {runId}` dengan jenis `Write-off`
78. Aktor Disposal menjalankan Submit Request atas laporan disposal `Lemari Arsip Besi {runId}`
79. Verifikasi record `Lemari Arsip Besi {runId}` berstatus `In Disposal Process` tanpa event `missing_*` baru untuk transisi Submit Request
80. Pembuat membatalkan baris Disposal aset `Kipas Angin Standing {runId}`
81. Verifikasi record `Kipas Angin Standing {runId}` kembali `Missing` tanpa event `missing_*` baru untuk baris yang dibatalkan
82. Baris Disposal aset `Mesin Fotokopi Ricoh {runId}` dihapus dari daftar Disposal
83. Verifikasi record `Mesin Fotokopi Ricoh {runId}` kembali `Missing` tanpa event `missing_*` baru untuk baris yang dihapus
84. Baris Disposal aset `Mesin Cuci Industri {runId}` melewati Transaction timeout
85. Verifikasi record `Mesin Cuci Industri {runId}` kembali `Missing` tanpa event `missing_*` baru untuk timeout

### Notifikasi I found it kembali terkirim sesudah jendela 1 jam dan berlaku per record
86. Waktu berlalu sampai 70 menit sejak I found it pertama `Agus Pratama {runId}` atas record `Rak Besi Gudang {runId}`
87. `Agus Pratama {runId}` mengirim lagi I found it atas record `Rak Besi Gudang {runId}`
88. Verifikasi record `Rak Besi Gudang {runId}` mendapat node `Reported found by` baru atas nama `Agus Pratama {runId}` dan Aktor Missing menerima event `missing_found_reported` baru untuk `Agus Pratama {runId}`, karena jendela 1 jam sejak notifikasi pertamanya sudah berakhir
89. `Agus Pratama {runId}` mengirim I found it atas record `Meja Kerja Kayu {runId}` dalam 1 jam sesudah pengiriman pada record `Rak Besi Gudang {runId}`
90. Verifikasi Aktor Missing menerima event `missing_found_reported` untuk `Agus Pratama {runId}` atas record `Meja Kerja Kayu {runId}`, karena jendela 1 jam dihitung per pengguna per record

### Node Reported found by memuat koordinat lokasi penemu
91. Verifikasi node `Reported found by` pertama atas nama `Agus Pratama {runId}` pada record `Rak Besi Gudang {runId}` memuat Location dengan Latitude `-6.200000` dan Longitude `106.816667`

### Pelapor Audit menunggu konfirmasi dan notifikasinya sama dengan laporan pemegang
92. `Sabrina Putri {runId}` mengirim Report Missing atas `Kabinet Server {runId}` dari Task Detail sesi `Audit Gudang {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
93. Verifikasi record `Kabinet Server {runId}` berstatus `Waiting for Confirmation` dengan Source `Audit` dan memuat node `Reported missing by` atas nama `Sabrina Putri {runId}`
94. Verifikasi Aktor Missing Group aset menerima event `missing_holder_reported` dan tidak menerima event `missing_reported` untuk record `Kabinet Server {runId}`
95. Verifikasi baris `Reported missing` pada Transaction log aset `Kabinet Server {runId}` memuat Status `Waiting for Confirmation`
96. Verifikasi Transaction admin log `Sabrina Putri {runId}` sub-tab Missing memuat baris Activity `Reported missing` untuk `Kabinet Server {runId}` dengan Source `Audit`

### Pelapor Audit membatalkan laporannya tanpa notifikasi tambahan
97. `Sabrina Putri {runId}` mengirim Cancel Report atas record `Kabinet Server {runId}` dari Task Detail sesi `Audit Gudang {runId}`
98. Verifikasi record `Kabinet Server {runId}` memuat node `Report canceled by` atas nama `Sabrina Putri {runId}` dan pembatalan itu tidak mengirim notifikasi tambahan
99. Verifikasi Transaction admin log `Sabrina Putri {runId}` sub-tab Missing memuat baris Activity `Report canceled` untuk `Kabinet Server {runId}`

### Satu baris Transaction admin log per tindakan atas satu aset
100. Rina W mengirim Report Missing atas `Meja Resepsionis {runId}` dari Task Detail sesi `Audit Gudang {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
101. Rina W mengirim Add Update atas record `Meja Resepsionis {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
102. Verifikasi Transaction admin log Rina W sub-tab Missing memuat tepat satu baris Activity `Reported missing` dan tepat satu baris Activity `Update added` untuk `Meja Resepsionis {runId}`, tanpa akhiran `by [Pelaku]` dan dengan Source `Audit` yang sama pada kedua baris
103. Verifikasi Name kedua baris itu memuat `Meja Resepsionis {runId}` diikuti tanda hubung dan Increment yang terisi
104. Verifikasi Date kedua baris itu memuat waktu tindakan dengan format `DD/MM/YY` dan `HH:mm`
105. Verifikasi Group kedua baris itu `Finance Room`, Group aset saat tindakan dieksekusi

### Transaction log aset memuat Date, Status, dan User per peristiwa status
106. Verifikasi Transaction log aset `Laptop Dell Latitude 5420 {runId}` memuat kolom Date, Status, dan User, dan tidak memuat kolom Transaction ID, Reader name, Group, maupun Requested by
107. Verifikasi baris `Reported missing` pada Transaction log aset `Laptop Dell Latitude 5420 {runId}` memuat Status `Missing` dan User Rina W
108. Verifikasi baris `Report confirmed` pada Transaction log aset `Scanner Zebra DS2208 {runId}` memuat Status `Missing`
109. Verifikasi baris `Report rejected` pada Transaction log aset `Printer HP LaserJet M404 {runId}` memuat Status `Rejected`
110. Verifikasi baris `Marked as found` pada Transaction log aset `Toyota Innova {runId}` memuat Status `Found`
111. Verifikasi baris `Disposed` pada Transaction log aset `Tablet Samsung Tab A8 {runId}` memuat Status `Disposed`

### Node selain peristiwa status tidak membentuk baris Transaction log aset
112. Verifikasi Transaction log aset `Meja Kerja Kayu {runId}` memuat baris `Reported missing`
113. Verifikasi Transaction log aset `Meja Kerja Kayu {runId}` tidak memuat baris `Detected by scan`
114. Verifikasi Transaction log aset `Papan Tulis {runId}` memuat baris `Reported missing`
115. Verifikasi Transaction log aset `Papan Tulis {runId}` tidak memuat baris `Long missing`
116. Verifikasi Transaction log aset `Rak Besi Gudang {runId}` memuat baris `Reported missing`
117. Verifikasi Transaction log aset `Rak Besi Gudang {runId}` tidak memuat baris `Reported found by`
118. Verifikasi Transaction log aset `Genset Honda EU22 {runId}` memuat baris `Reported missing`
119. Verifikasi Transaction log aset `Genset Honda EU22 {runId}` tidak memuat baris `Disposal reported by`, `Disposal report declined by`, maupun `Disposal report canceled by`
120. Verifikasi Transaction log aset `Monitor LG 27UL500 {runId}` memuat baris `Reported missing`
121. Verifikasi Transaction log aset `Monitor LG 27UL500 {runId}` tidak memuat baris `Report canceled by`

### Activity Transaction admin log per aksi Aktor Missing
122. Verifikasi Transaction admin log Rina W memuat baris Activity `Report confirmed` untuk `Scanner Zebra DS2208 {runId}`
123. Verifikasi Transaction admin log Rina W memuat baris Activity `Report rejected` untuk `Printer HP LaserJet M404 {runId}`
124. Verifikasi Transaction admin log Rina W memuat baris Activity `Update added` untuk `Projector Epson EB-X06 {runId}`
125. Verifikasi Transaction admin log Rina W memuat baris Activity `Marked as found` untuk `Toyota Innova {runId}`

### Laporan dari My Asset tidak masuk Transaction admin log
126. Verifikasi Transaction admin log `Joko Susilo {runId}` tidak memuat Report Missing atas `Scanner Zebra DS2208 {runId}` yang dikirim `Joko Susilo {runId}` sebagai pemegang

### Reject dan Cancel Report menghitung ulang status global aset
127. Verifikasi status global aset `Printer HP LaserJet M404 {runId}` dihitung ulang dari state aset terkini menjadi `Borrowed` karena aset masih dipegang `Joko Susilo {runId}`
128. Verifikasi status global aset `Monitor LG 27UL500 {runId}` dihitung ulang dari state aset terkini menjadi `Borrowed` karena aset masih dipegang `Joko Susilo {runId}`

### Sinyal task selesai saat laporan diputuskan atau record keluar dari Waiting for Confirmation atau Missing
129. Verifikasi notifikasi `missing_holder_reported` untuk record `Printer HP LaserJet M404 {runId}` ditandai selesai otomatis setelah Reject pada langkah 18
130. Verifikasi notifikasi `missing_holder_reported` untuk record `Monitor LG 27UL500 {runId}` ditandai selesai otomatis setelah Cancel Report pada langkah 22
131. Verifikasi notifikasi `missing_reported` untuk record `Toyota Innova {runId}` ditandai selesai otomatis setelah Mark as Found pada langkah 31
132. Verifikasi notifikasi `missing_reported` untuk record `Tablet Samsung Tab A8 {runId}` ditandai selesai otomatis setelah Disposal Executed pada langkah 43

### Group pada Transaction admin log adalah snapshot saat tindakan dieksekusi
133. Group aset `Meja Resepsionis {runId}` dipindah ke Group `Warehouse`
134. Verifikasi Group aset `Meja Resepsionis {runId}` kini `Warehouse`
135. Verifikasi Group baris Activity `Reported missing` dan `Update added` untuk `Meja Resepsionis {runId}` pada Transaction admin log Rina W tetap `Finance Room`, bukan `Warehouse`
