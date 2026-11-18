---
id: TC-FA-DAMAGED-BE-206-missing-bersamaan-server
title: "Server menahan dan melepas Damage record saat aset dilaporkan Missing, ditemukan, laporan Missing ditutup, atau Missing → Disposed, menolak aksi pada record berpenanda Missing, dan menangani Report Missing atas record Disposal"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r65", "§Aturan Logika Modul#r66", "§Aturan Logika Modul#r67", "§Aturan Logika Modul#r68", "§Aturan Logika Modul#r69", "§Aturan Logika Modul#r70", "§Aturan Logika Modul#r71", "§Aturan Logika Modul#r72", "§Aturan Logika Modul#r73", "§Aturan Logika Modul#r74", "§Aturan Logika Modul#r75", "§Aturan Logika Modul#r76", "§Aturan Logika Modul#r78", "V-DMG-02", "§9.2#b25", "§9.2#b26", "§9.2#b27", "§9.6#r10", "EC-DMG-11", "EC-DMG-12", "EC-DMG-33", "EC-DMG-34", "§9.4.4#r30", "§9.4.4#r31", "§9.4.4#r32", "§9.4.4#r33", "§9.7#r4", "§9.7#r15", "§9.7#r16", "F-DMG-10"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r65": 3
  "§Aturan Logika Modul#r66": [18, 20]
  "§Aturan Logika Modul#r67": 4
  "§Aturan Logika Modul#r68": 5
  "§Aturan Logika Modul#r69": [29, 54]
  "§Aturan Logika Modul#r70": [5, 56]
  "§Aturan Logika Modul#r71": [31, 35]
  "§Aturan Logika Modul#r72": [10, 12, 16]
  "§Aturan Logika Modul#r73": [22, 25, 74, 76]
  "§Aturan Logika Modul#r74": [37, 41]
  "§Aturan Logika Modul#r75": [38, 39]
  "§Aturan Logika Modul#r76": [45, 72]
  "§Aturan Logika Modul#r78": [48, 50]
  V-DMG-02: [10, 12, 14, 58, 60]
  "§9.2#b25": [3, 6, 38]
  "§9.2#b26": [48, 50, 52]
  "§9.2#b27": [22, 25, 27, 58, 60]
  "§9.6#r10": [6, 8, 32, 46, 62, 64, 66, 68, 70, 72]
  EC-DMG-11: [3, 5, 29]
  EC-DMG-12: 38
  EC-DMG-33: [31, 32, 35]
  EC-DMG-34: [45, 72]
  "§9.4.4#r30": [3, 6, 16]
  "§9.4.4#r31": [37, 38, 41]
  "§9.4.4#r32": [31, 32, 35]
  "§9.4.4#r33": [45, 46]
  "§9.7#r4": [37, 39, 43]
  "§9.7#r15": [5, 31]
  "§9.7#r16": 45
  F-DMG-10: 3
---

# Server menahan dan melepas Damage record saat aset dilaporkan Missing, ditemukan, laporan Missing ditutup, atau Missing → Disposed, menolak aksi pada record berpenanda Missing, dan menangani Report Missing atas record Disposal

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged.
  - Aktor Missing `Hendra Saputra {runId}`, yang menjalankan Mark as Found dan memutuskan laporan hilang.
  - Aktor pelepasan aset `Maya Puspita {runId}`, Asset Admin sub-tab Disposal.
  - Pelapor umum `Budi Santoso {runId}`, pemegang aset, tanpa role Damaged.
- Data:
  - DU-206-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-206-2: User `Hendra Saputra {runId}`, Aktor Missing, cakupan Group `Head Office {runId}`.
  - DU-206-3: User `Maya Puspita {runId}`, Asset Admin sub-tab Disposal, cakupan Group `Head Office {runId}`.
  - DU-206-4: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang.
  - DU-206-5: Group `Head Office {runId}`.
  - DU-206-6: Aset `Camera Canon EOS - 61 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, tanpa transaksi berjalan.
  - DU-206-7: Aset `Laptop Dell Latitude 5420 - 62 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, tanpa transaksi berjalan.
  - DU-206-8: Aset `Tablet Samsung Tab A8 - 63 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-206-9: Aset `Drill Bosch GSB - 64 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, dipegang `Budi Santoso {runId}`.
  - DU-206-10: Aset `Printer HP LaserJet M404 - 65 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, dipegang `Budi Santoso {runId}`.
  - DU-206-11: Aset `Projector Epson EB-X06 - 66 {runId}`, Group `Head Office {runId}`, `Missing` dengan Condition sebelumnya Damaged, punya record `Damaged` yang ditahan penanda `Missing`.
  - DU-206-12: Aset `Monitor Dell P2422H - 67 {runId}`, Group `Head Office {runId}`, `Missing` dengan Condition sebelumnya Damaged, punya record `Damaged` yang ditahan penanda `Missing`.
  - DU-206-13: Aset `Forklift Toyota 8FD - 68 {runId}`, Group `Head Office {runId}`, `Missing` dengan Condition sebelumnya Damaged, punya record `Damaged` yang ditahan penanda `Missing`.
  - DU-206-14: Aset `Scanner Fujitsu fi-7160 - 69 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-206-15: Aset `Office Chair Ergo - 70 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal`.
  - DU-206-16: Aset `Office Chair Ergo - 71 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan baris jenis selain Write-off.
  - DU-206-17: Aset `Handheld Scanner Zebra TC21 - 72 {runId}`, Group `Head Office {runId}`, tanpa record Damaged, ada laporan hilang dari pemegang `Budi Santoso {runId}` yang masih `Waiting for Confirmation`.
  - DU-206-18: Aset `Office Chair Ergo - 74 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal`.
  - DU-206-19: Aset `Toyota Avanza - 73 {runId}`, Group `Head Office {runId}`, `Missing` tanpa record Damaged.
  - DU-206-20: What happened `Terakhir terlihat di gudang lantai dua {runId}`, Damaged Photo `terakhir-terlihat.jpg`.
  - DU-206-21: Note `Ditemukan rusak di ruang arsip {runId}`, Damaged Photo `ditemukan-rusak.jpg`.
  - DU-206-22: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-206-23: What happened `Casing retak setelah terbentur {runId}`, Damaged Photo `casing-retak.jpg`.
  - DU-206-24: Aset `Drill Bosch GSB - 75 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, dipegang `Budi Santoso {runId}`.
  - DU-206-25: Aset `Handheld Scanner Zebra TC21 - 76 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`, dipegang `Budi Santoso {runId}`.
  - DU-206-26: Reason `Foto yang dikirim bukan foto aset ini {runId}`.

## Test Steps

### Report Missing atas record Damaged dari tab Damaged menahan record
1. Catat jumlah node Damage Log record `Camera Canon EOS - 61 {runId}`
2. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Camera Canon EOS - 61 {runId}` dari tab Damaged dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
3. Verifikasi aset dengan record berjalan dapat dilaporkan hilang dari tab Damaged
4. Verifikasi Condition aset menjadi `Missing` dengan Condition sebelumnya `Damaged` tersimpan, sehingga status global aset menjadi `Damaged + Missing`
5. Verifikasi record tetap berstatus `Damaged` dan diberi penanda `Missing`
6. Verifikasi Damage Log record bertambah satu node `Asset reported missing` dengan pelaku `System`
7. Event `Asset reported missing` atas `Camera Canon EOS - 61 {runId}` dikirim ulang dengan identitas event yang sama
8. Verifikasi node `Asset reported missing` tidak bertambah dan status record serta status global aset tidak berubah, karena event dengan identitas sama diproses sekali

### Selama ditahan hanya Damage Log yang tersedia
9. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Camera Canon EOS - 61 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
10. Verifikasi Mark as Repaired ditolak karena record berpenanda `Missing` dan record tetap `Damaged`
11. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Camera Canon EOS - 61 {runId}`
12. Verifikasi Report Disposal ditolak karena record berpenanda `Missing`
13. Total Control `Agus Pratama {runId}` menjalankan Report Missing sekali lagi atas `Camera Canon EOS - 61 {runId}` dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
14. Verifikasi Report Missing kedua ditolak karena record berpenanda `Missing`
15. Total Control `Agus Pratama {runId}` membuka Damage Log `Camera Canon EOS - 61 {runId}`
16. Verifikasi Damage Log tetap dapat dibaca dan jumlah node tetap bertambah hanya satu dari jumlah yang dicatat, karena penolakan tidak menulis node

### Report Missing dari Asset List hanya bila tanpa transaksi berjalan
17. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Laptop Dell Latitude 5420 - 62 {runId}` dari Asset List dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
18. Verifikasi aset dengan record berjalan dan tanpa transaksi berjalan dapat dilaporkan hilang dari Asset List dan record `Damaged` ditahan
19. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Tablet Samsung Tab A8 - 63 {runId}` yang sedang dipinjam dari Asset List dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
20. Verifikasi permintaan ditolak karena ada transaksi berjalan dan record tidak ditahan

### Record Waiting for Confirmation belum dapat dilaporkan hilang
21. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Scanner Fujitsu fi-7160 - 69 {runId}` dari Asset List dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
22. Verifikasi permintaan ditolak karena record masih `Waiting for Confirmation` dan tanpa penanda
23. Total Control `Agus Pratama {runId}` melakukan Confirm atas laporan `Scanner Fujitsu fi-7160 - 69 {runId}`
24. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Scanner Fujitsu fi-7160 - 69 {runId}` dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
25. Verifikasi Report Missing diterima setelah record di-Confirm dan record `Damaged` ditahan
26. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Handheld Scanner Zebra TC21 - 72 {runId}` yang punya laporan hilang `Waiting for Confirmation` dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
27. Verifikasi laporan ditolak karena aset yang sedang dilaporkan hilang tidak dapat dilaporkan rusak dan tidak ada Damage record

### Laporan hilang dari pemegang: penanda Reported Missing, lalu ditutup
28. Pelapor umum `Budi Santoso {runId}` melaporkan hilang `Drill Bosch GSB - 64 {runId}` yang ia pegang dari halaman aset yang dipegangnya
29. Verifikasi record `Damaged` ditahan dengan penanda `Reported Missing` selama laporan hilang masih `Waiting for Confirmation`
30. Aktor penemuan aset `Hendra Saputra {runId}` melakukan Reject atas laporan hilang `Drill Bosch GSB - 64 {runId}`
31. Verifikasi penanda dihapus dan record `Damaged` aktif kembali
32. Verifikasi Damage Log record memuat node `Missing report closed` dengan pelaku `System`
33. Pelapor umum `Budi Santoso {runId}` melaporkan hilang `Printer HP LaserJet M404 - 65 {runId}` yang ia pegang
34. Pelapor umum `Budi Santoso {runId}` melakukan Cancel Report atas laporan hilang `Printer HP LaserJet M404 - 65 {runId}`
35. Verifikasi penanda dihapus, record `Damaged` aktif kembali, dan node `Missing report closed` tercatat

### Aset ditemukan: penanda hilang dan record aktif kembali tanpa record baru
36. Aktor penemuan aset `Hendra Saputra {runId}` menjalankan Mark as Found Damaged atas `Projector Epson EB-X06 - 66 {runId}` dengan Note `Ditemukan rusak di ruang arsip {runId}` dan Damaged Photo `ditemukan-rusak.jpg`
37. Verifikasi penanda `Missing` dihapus dan record `Damaged` yang sama aktif kembali
38. Verifikasi server menambah node `Asset found` ke record yang ada dan tidak membuat record baru
39. Verifikasi status global aset menjadi `Damaged` dan node `Asset found` memuat Note dan Damaged Photo dari dialog tanpa menimpa What happened record
40. Aktor penemuan aset `Hendra Saputra {runId}` menjalankan Mark as Found atas `Monitor Dell P2422H - 67 {runId}` tanpa kerusakan
41. Verifikasi penanda `Missing` dihapus dan record `Damaged` aktif kembali
42. Aktor penemuan aset `Hendra Saputra {runId}` menjalankan Mark as Found Damaged atas `Toyota Avanza - 73 {runId}` yang tidak punya Damage record dengan Note `Ditemukan rusak di ruang arsip {runId}` dan Damaged Photo `ditemukan-rusak.jpg`
43. Verifikasi server membuat record `Damaged` baru dan status global aset menjadi `Damaged`

### Missing menjadi Disposed menyelesaikan record sebagai Disposed
44. Aktor pelepasan aset `Maya Puspita {runId}` menyelesaikan pelepasan aset `Forklift Toyota 8FD - 68 {runId}` yang berstatus `Missing`
45. Verifikasi record ikut selesai `Disposed` dan pindah dari record berjalan ke History
46. Verifikasi Damage Log record memuat node `Disposed` dengan pelaku `System`

### Report Missing atas record yang sedang dalam proses pelepasan aset
47. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Office Chair Ergo - 70 {runId}` yang record-nya `Reported Disposal` dari Asset List dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
48. Verifikasi laporan pelepasan aset ditutup oleh `System` dengan alasan `Asset reported missing`, record kembali `Damaged`, lalu ditahan dengan penanda `Missing`
49. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Office Chair Ergo - 71 {runId}` yang record-nya `In Disposal Process` dari Asset List dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
50. Verifikasi baris pelepasan aset ditutup oleh `System` dengan alasan `Asset reported missing`, record kembali `Damaged`, lalu ditahan dengan penanda `Missing`
51. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Office Chair Ergo - 74 {runId}` yang record-nya `Reported Disposal` dari tab Damaged
52. Verifikasi aksi Report Missing dari tab Damaged ditolak untuk record selain `Damaged`

### Confirm laporan hilang pemegang mengubah penanda Reported Missing menjadi Missing
53. Pelapor umum `Budi Santoso {runId}` melaporkan hilang `Drill Bosch GSB - 75 {runId}` yang ia pegang dari halaman aset yang dipegangnya
54. Verifikasi record `Damaged` ditahan dengan penanda `Reported Missing` selama laporan hilang masih `Waiting for Confirmation`
55. Aktor penemuan aset `Hendra Saputra {runId}` melakukan Confirm atas laporan hilang `Drill Bosch GSB - 75 {runId}`
56. Verifikasi penanda berubah menjadi `Missing` dan record `Damaged` tetap ditahan

### Confirm dan Reject atas record berpenanda Missing ditolak server
57. Total Control `Agus Pratama {runId}` melakukan Confirm atas record `Camera Canon EOS - 61 {runId}` yang berpenanda `Missing`
58. Verifikasi Confirm ditolak dengan pesan `This asset is reported missing.` dan record tetap `Damaged` berpenanda `Missing`
59. Total Control `Agus Pratama {runId}` melakukan Reject atas record `Camera Canon EOS - 61 {runId}` yang berpenanda `Missing` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
60. Verifikasi Reject ditolak dengan pesan `This asset is reported missing.` dan record tetap `Damaged` berpenanda `Missing`

### Event Missing dan Disposal yang dikirim ulang diproses sekali
61. Event `Asset found` atas `Projector Epson EB-X06 - 66 {runId}` dikirim ulang dengan identitas event yang sama
62. Verifikasi node `Asset found` tidak bertambah dan status record serta status global aset tidak berubah, karena event dengan identitas sama diproses sekali
63. Event `Missing report closed` atas `Drill Bosch GSB - 64 {runId}` dikirim ulang dengan identitas event yang sama
64. Verifikasi node `Missing report closed` tidak bertambah dan status record serta status global aset tidak berubah, karena event dengan identitas sama diproses sekali
65. Event `Disposed` atas `Forklift Toyota 8FD - 68 {runId}` dikirim ulang dengan identitas event yang sama
66. Verifikasi node `Disposed` tidak bertambah dan status record serta status global aset tidak berubah, karena event dengan identitas sama diproses sekali

### Status global aset sesudah laporan hilang ditutup dan sesudah Missing menjadi Disposed
67. Total Control `Agus Pratama {runId}` membaca status global aset `Drill Bosch GSB - 64 {runId}` yang laporan hilangnya ditolak
68. Verifikasi status global aset kembali `Damaged` bersamaan dengan penghapusan penanda
69. Total Control `Agus Pratama {runId}` membaca status global aset `Printer HP LaserJet M404 - 65 {runId}` yang laporan hilangnya dibatalkan
70. Verifikasi status global aset kembali `Damaged` bersamaan dengan penghapusan penanda
71. Total Control `Agus Pratama {runId}` membaca status global aset `Forklift Toyota 8FD - 68 {runId}` yang sudah menjadi Disposed
72. Verifikasi status global aset menjadi Lifecycle `Disposed` bersamaan dengan record yang selesai `Disposed`

### Report Missing atas record Waiting for Confirmation ditolak di titik masuk tab Damaged dan halaman aset pemegang
73. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Handheld Scanner Zebra TC21 - 76 {runId}` yang record-nya `Waiting for Confirmation` dari tab Damaged dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
74. Verifikasi permintaan ditolak karena record masih `Waiting for Confirmation` dan tanpa penanda
75. Pelapor umum `Budi Santoso {runId}` melaporkan hilang `Handheld Scanner Zebra TC21 - 76 {runId}` yang ia pegang dari halaman aset yang dipegangnya
76. Verifikasi permintaan ditolak karena record masih `Waiting for Confirmation` dan tanpa penanda

