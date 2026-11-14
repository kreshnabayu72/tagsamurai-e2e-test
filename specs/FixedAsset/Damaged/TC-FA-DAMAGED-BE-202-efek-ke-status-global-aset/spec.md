---
id: TC-FA-DAMAGED-BE-202-efek-ke-status-global-aset
title: "Efek Damage record ke status global aset: Damaged saat record Damaged, laporan pemegang vs scan selama Waiting for Confirmation, hitung ulang saat Reject/Cancel, Normal atau TAG Reported saat Repaired, dan transaksi berjalan tidak berubah"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r24", "§Aturan Logika Modul#r25", "§Aturan Logika Modul#r26", "§Aturan Logika Modul#r27", "§Aturan Logika Modul#r28", "§Aturan Logika Modul#r29", "§Aturan Logika Modul#r30", "§Aturan Logika Modul#r31", "§Aturan Logika Modul#r32", "§Aturan Logika Modul#r33", "§Aturan Logika Modul#r34", "§Aturan Logika Modul#r36", "§Aturan Logika Modul#r37", "§Aturan Logika Modul#r38", "§Aturan Logika Modul#r39", "§Aturan Logika Modul#r40", "§Aturan Logika Modul#r41", "§Aturan Logika Modul#r59", "§Aturan Logika Modul#r60", "§9.2#b8", "§9.4.3#b2", "§9.4.3#b3", "§9.4.2#r3", "§9.4.2#r9", "§9.4.2#r10", "§9.4.2#r21", "§9.4.4#r3", "§9.4.4#r20", "§9.4.4#r21", "§9.4.4#r23", "§9.7#r1", "§9.7#r2", "§9.7#r5", "§9.7#r6", "§9.7#r7", "§9.7#r9", "§9.4.1#r3", "§9.4.1#r8", "§9.4.1#r5"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r24": 8
  "§Aturan Logika Modul#r25": [2, 14]
  "§Aturan Logika Modul#r26": [3, 9]
  "§Aturan Logika Modul#r27": [8, 11]
  "§Aturan Logika Modul#r28": 8
  "§Aturan Logika Modul#r29": [11, 12]
  "§Aturan Logika Modul#r30": 14
  "§Aturan Logika Modul#r31": [40, 49]
  "§Aturan Logika Modul#r32": [20, 25, 30, 56, 59]
  "§Aturan Logika Modul#r33": [35, 38]
  "§Aturan Logika Modul#r34": [23, 28, 33]
  "§Aturan Logika Modul#r36": 3
  "§Aturan Logika Modul#r37": [4, 6]
  "§Aturan Logika Modul#r38": [40, 44]
  "§Aturan Logika Modul#r39": [41, 45]
  "§Aturan Logika Modul#r40": 42
  "§Aturan Logika Modul#r41": [51, 53]
  "§Aturan Logika Modul#r59": [40, 44, 49]
  "§Aturan Logika Modul#r60": 47
  "§9.2#b8": [8, 9, 12, 14]
  "§9.4.3#b2": [4, 6]
  "§9.4.3#b3": [8, 11]
  "§9.4.2#r3": [4, 6]
  "§9.4.2#r9": [40, 41]
  "§9.4.2#r10": [44, 45]
  "§9.4.2#r21": 47
  "§9.4.4#r3": [4, 6]
  "§9.4.4#r20": [40, 62]
  "§9.4.4#r21": 44
  "§9.4.4#r23": 47
  "§9.7#r1": 2
  "§9.7#r2": [8, 11]
  "§9.7#r5": [14, 15, 17]
  "§9.7#r6": [20, 25, 35]
  "§9.7#r7": [30, 38]
  "§9.7#r9": [40, 44, 47, 49, 61]
  "§9.4.1#r3": [2, 40]
  "§9.4.1#r8": [4, 23, 28, 33, 51]
  "§9.4.1#r5": 49
---

# Efek Damage record ke status global aset: Damaged saat record Damaged, laporan pemegang vs scan selama Waiting for Confirmation, hitung ulang saat Reject/Cancel, Normal atau TAG Reported saat Repaired, dan transaksi berjalan tidak berubah

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged yang melapor, memutuskan Confirm dan Reject, dan menjalankan Mark as Repaired.
  - Aktor peminjaman `Yoga Tanuwijaya {runId}` dan Aktor penugasan `Dewi Anggraini {runId}`, tanpa hak Update Manage asset & TAG.
  - Aktor pemindahan aset `Tono Riyadi {runId}`.
  - Pelapor umum `Budi Santoso {runId}`, pemegang aset, tanpa role Damaged.
  - Pelapor umum `Dedi Kurniawan {runId}`, pengguna aktif yang memindai TAG, tanpa role Damaged.
- Data:
  - DU-202-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-202-2: User `Yoga Tanuwijaya {runId}`, Aktor Borrow, cakupan Group `Head Office {runId}`.
  - DU-202-3: User `Dewi Anggraini {runId}`, Aktor Assignment, cakupan Group `Head Office {runId}`.
  - DU-202-4: User `Tono Riyadi {runId}`, Aktor Transfer, cakupan Group `Head Office {runId}` dan Group `Branch Surabaya {runId}`.
  - DU-202-5: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang.
  - DU-202-6: User `Dedi Kurniawan {runId}`, pelapor umum, pemindai TAG, cakupan aset yang ia pindai.
  - DU-202-7: Group `Head Office {runId}`.
  - DU-202-8: Group `Branch Surabaya {runId}`.
  - DU-202-9: Aset `Laptop Dell Latitude 5420 - 2 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-10: Aset `Tablet Samsung Tab A8 - 5 {runId}`, Group `Head Office {runId}`, TAG `QR`, status global `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-11: Aset `Camera Canon EOS - 2 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-12: Aset `Office Chair Ergo - 12 {runId}`, Group `Head Office {runId}`, TAG `QR`, status global `Normal`, tanpa record berjalan.
  - DU-202-13: Aset `Printer HP LaserJet M404 - 3 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-14: Aset `Monitor Dell P2422H - 3 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-15: Aset `Laptop Dell Latitude 5420 - 7 {runId}`, Group `Head Office {runId}`, TAG `QR`, status global `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-16: Aset `Scanner Fujitsu fi-7160 - 3 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `Normal`, tanpa record berjalan.
  - DU-202-17: Aset `Handheld Scanner Zebra TC21 - 3 {runId}`, Group `Head Office {runId}`, TAG `QR`, status global `Normal`, tanpa record berjalan.
  - DU-202-18: Aset `Forklift Toyota 8FD - 3 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-202-19: Aset `Drill Bosch GSB - 3 {runId}`, Group `Head Office {runId}`, TAG `QR`, status global `Assigned` kepada `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-202-20: Aset `Toyota Avanza - 4 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `TAG Reported`, punya record `Damaged`.
  - DU-202-21: Aset `Projector Epson EB-X06 - 3 {runId}`, Group `Head Office {runId}`, TAG tanpa TAG, status global `Damaged`, punya record `Damaged`, tidak dipegang.
  - DU-202-22: Aset `Monitor Dell P2422H - 9 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-202-23: Aset `Handheld Scanner Zebra TC21 - 5 {runId}`, Group `Head Office {runId}`, TAG `QR`, status global `Assigned` kepada `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-202-24: What happened `Layar retak setelah terjatuh {runId}`, Damaged Photo `layar-retak.jpg`.
  - DU-202-25: Reason `Foto yang dikirim bukan foto aset ini {runId}`.
  - DU-202-26: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-202-27: Aset `Projector Epson EB-X06 - 8 {runId}`, Group `Head Office {runId}`, TAG `QR`, status global `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-28: Aset `Monitor Dell P2422H - 10 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `TAG Reported`, dipegang `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-29: Aset `Forklift Toyota 8FD - 5 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`.
- Kondisi:
  - After photo required bernilai `OFF`.

## Test Steps

### Laporan Pelapor admin atas aset yang dipegang mengubah status global menjadi Damaged tanpa mengubah Group, pemegang, TAG, dan baris transaksi
1. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 2 {runId}` yang sedang ditugaskan kepada `Budi Santoso {runId}` dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
2. Verifikasi record yang dibuat berstatus `Damaged` dan status global aset menjadi `Damaged`
3. Verifikasi Group `Head Office {runId}`, pemegang `Budi Santoso {runId}`, dan TAG `RFID` aset itu tidak berubah
4. Verifikasi baris penugasan aset itu tidak ditutup dan tidak diubah, dan aset tetap di tangan `Budi Santoso {runId}`
5. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Tablet Samsung Tab A8 - 5 {runId}` yang sedang dipinjam oleh `Budi Santoso {runId}` dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
6. Verifikasi status global aset menjadi `Damaged`, baris peminjaman tidak ditutup dan tidak diubah, dan pemegang `Budi Santoso {runId}` tidak berubah

### Laporan pelapor umum selama Waiting for Confirmation: efek ke aset mengikuti Source
7. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Camera Canon EOS - 2 {runId}` yang ia pegang dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
8. Verifikasi record berstatus `Waiting for Confirmation` sedangkan status global aset langsung menjadi `Damaged`
9. Verifikasi Group, pemegang `Budi Santoso {runId}`, dan TAG `RFID` aset itu tidak berubah
10. Pelapor umum `Dedi Kurniawan {runId}` mengirim Report Damaged atas `Office Chair Ergo - 12 {runId}` dari hasil scan TAG di mobile dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
11. Verifikasi record berstatus `Waiting for Confirmation` dan status global aset tetap `Normal`
12. Verifikasi aset itu diberi penanda `Damage reported`

### Confirm laporan scan mengubah status global menjadi Damaged dan menghapus penanda
13. Total Control `Agus Pratama {runId}` melakukan Confirm atas laporan `Office Chair Ergo - 12 {runId}`
14. Verifikasi record menjadi `Damaged` dan status global aset menjadi `Damaged`
15. Verifikasi penanda `Damage reported` pada aset itu dihapus
16. Total Control `Agus Pratama {runId}` melakukan Confirm atas laporan `Camera Canon EOS - 2 {runId}`
17. Verifikasi record menjadi `Damaged` dan status global aset tetap `Damaged` karena laporan pemegang sudah mengubahnya

### Reject laporan pemegang menghitung ulang status global dari state aset terkini
18. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Printer HP LaserJet M404 - 3 {runId}` yang ia pegang dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
19. Total Control `Agus Pratama {runId}` melakukan Reject atas laporan `Printer HP LaserJet M404 - 3 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
20. Verifikasi record menjadi `Rejected` dan status global aset dihitung ulang menjadi `Assigned` karena aset masih dipegang `Budi Santoso {runId}`
21. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Monitor Dell P2422H - 3 {runId}` yang ia pegang dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
22. Aktor penugasan `Dewi Anggraini {runId}` melakukan Unassign atas `Monitor Dell P2422H - 3 {runId}` selagi record masih `Waiting for Confirmation`
23. Verifikasi Unassign tetap berlaku dan record tetap `Waiting for Confirmation`
24. Total Control `Agus Pratama {runId}` melakukan Reject atas laporan `Monitor Dell P2422H - 3 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
25. Verifikasi status global aset dihitung ulang dari state aset terkini menjadi `Normal`, bukan dipulihkan ke `Assigned` saat laporan

### Cancel Report laporan pemegang menghitung ulang status global dari state aset terkini
26. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 7 {runId}` yang ia pinjam dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
27. Aktor peminjaman `Yoga Tanuwijaya {runId}` menyelesaikan Return `Laptop Dell Latitude 5420 - 7 {runId}` selagi record masih `Waiting for Confirmation`
28. Verifikasi Return tetap berlaku dan record tetap `Waiting for Confirmation`
29. Pelapor umum `Budi Santoso {runId}` membatalkan laporannya lewat Cancel Report atas `Laptop Dell Latitude 5420 - 7 {runId}`
30. Verifikasi record menjadi `Canceled` dan status global aset dihitung ulang dari state aset terkini menjadi `Normal`

### Laporan scan yang di-Reject atau di-Cancel menghapus penanda tanpa mengubah status global
31. Pelapor umum `Dedi Kurniawan {runId}` mengirim Report Damaged atas `Scanner Fujitsu fi-7160 - 3 {runId}` dari hasil scan TAG di mobile dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
32. Aktor pemindahan aset `Tono Riyadi {runId}` memindahkan `Scanner Fujitsu fi-7160 - 3 {runId}` ke Group `Branch Surabaya {runId}` dan aset diterima selagi record masih `Waiting for Confirmation`
33. Verifikasi pemindahan tetap berlaku, Group aset menjadi `Branch Surabaya {runId}`, dan record tetap `Waiting for Confirmation`
34. Total Control `Agus Pratama {runId}` melakukan Reject atas laporan `Scanner Fujitsu fi-7160 - 3 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
35. Verifikasi penanda `Damage reported` pada aset itu dihapus dan status global aset tetap `Normal`
36. Pelapor umum `Dedi Kurniawan {runId}` mengirim Report Damaged atas `Handheld Scanner Zebra TC21 - 3 {runId}` dari hasil scan TAG di mobile dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
37. Pelapor umum `Dedi Kurniawan {runId}` membatalkan laporannya lewat Cancel Report atas `Handheld Scanner Zebra TC21 - 3 {runId}`
38. Verifikasi record menjadi `Canceled`, penanda `Damage reported` pada aset itu dihapus, dan status global aset tetap `Normal`

### Mark as Repaired atas aset yang sedang dipinjam atau ditugaskan tidak menunggu Return atau Unassign
39. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Forklift Toyota 8FD - 3 {runId}` yang sedang dipinjam dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
40. Verifikasi record menjadi `Repaired` tanpa menunggu Return dan status global aset menjadi `Normal`
41. Verifikasi baris peminjaman tetap `Borrowed` dan pemegang `Budi Santoso {runId}` tidak berubah
42. Verifikasi penanda `Damaged` pada baris peminjaman hilang bersama record
43. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Drill Bosch GSB - 3 {runId}` yang sedang ditugaskan dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
44. Verifikasi record menjadi `Repaired` tanpa menunggu Unassign dan status global aset menjadi `Normal`
45. Verifikasi baris penugasan tetap `Assigned` dan pemegang `Budi Santoso {runId}` tidak berubah

### Hasil Mark as Repaired menurut keadaan aset: TAG Reported dipertahankan, aset tanpa TAG menjadi Normal
46. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Toyota Avanza - 4 {runId}` yang berstatus `TAG Reported` dengan identifikasi manual dan Repair note `Komponen rusak sudah diganti {runId}`
47. Verifikasi record menjadi `Repaired` dan status global aset menjadi `TAG Reported`, bukan `Normal`
48. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 3 {runId}` yang tidak memiliki TAG dengan Repair note `Komponen rusak sudah diganti {runId}`
49. Verifikasi record menjadi `Repaired` tanpa permintaan Scan TAG, status global aset menjadi `Normal`, dan penanda Damaged pada aset hilang

### Return dan Unassign atas aset ber-record Damaged berjalan sebagai Accept biasa
50. Aktor peminjaman `Yoga Tanuwijaya {runId}` menyelesaikan Return dengan Accept atas `Monitor Dell P2422H - 9 {runId}`
51. Verifikasi Return selesai sebagai Accept biasa dan record tetap `Damaged` tanpa record baru
52. Aktor penugasan `Dewi Anggraini {runId}` melakukan Unassign dengan Accept atas `Handheld Scanner Zebra TC21 - 5 {runId}`
53. Verifikasi Unassign selesai sebagai Accept biasa dan record tetap `Damaged` tanpa record baru

### Reject dan Cancel Report laporan pemegang menghitung ulang status global menjadi Borrowed atau TAG Reported
54. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Projector Epson EB-X06 - 8 {runId}` yang ia pinjam dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
55. Total Control `Agus Pratama {runId}` melakukan Reject atas laporan `Projector Epson EB-X06 - 8 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
56. Verifikasi record menjadi `Rejected` dan status global aset dihitung ulang menjadi `Borrowed` karena aset masih dipinjam `Budi Santoso {runId}`
57. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Monitor Dell P2422H - 10 {runId}` yang berstatus `TAG Reported` dan ia pegang dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
58. Pelapor umum `Budi Santoso {runId}` membatalkan laporannya lewat Cancel Report atas `Monitor Dell P2422H - 10 {runId}`
59. Verifikasi record menjadi `Canceled` dan status global aset dihitung ulang dari state aset terkini menjadi `TAG Reported`

### Mark as Repaired atas aset yang sedang dipinjam memicu tepat satu event damaged_resolved
60. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Forklift Toyota 8FD - 5 {runId}` yang sedang dipinjam dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
61. Verifikasi record menjadi `Repaired` dan baris peminjaman tetap `Borrowed`
62. Verifikasi tepat satu event `damaged_resolved` dikirim untuk record itu

