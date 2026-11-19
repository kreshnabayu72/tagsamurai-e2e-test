---
id: TC-FA-DAMAGED-BE-202-efek-ke-status-global-aset
title: "Efek Damage record ke status global aset: Damaged saat record Damaged, laporan pemegang vs scan selama Waiting for Confirmation, hitung ulang saat Reject/Cancel, Normal atau TAG Reported saat Repaired, dan transaksi berjalan tidak berubah, serta Condition tidak berubah dan record tetap Active selama aset In Transfer Process"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r24", "§Aturan Logika Modul#r25", "§Aturan Logika Modul#r26", "§Aturan Logika Modul#r27", "§Aturan Logika Modul#r28", "§Aturan Logika Modul#r29", "§Aturan Logika Modul#r30", "§Aturan Logika Modul#r31", "§Aturan Logika Modul#r32", "§Aturan Logika Modul#r33", "§Aturan Logika Modul#r34", "§Aturan Logika Modul#r36", "§Aturan Logika Modul#r38", "§Aturan Logika Modul#r39", "§Aturan Logika Modul#r40", "§Aturan Logika Modul#r41", "§Aturan Logika Modul#r42", "§Aturan Logika Modul#r58", "§Aturan Logika Modul#r59", "§9.2#b8", "§9.4.3#b2", "§9.4.3#b3", "EC-DMG-03", "EC-DMG-09", "EC-DMG-10", "EC-DMG-25", "§9.4.4#r3", "§9.4.4#r19", "§9.4.4#r20", "§9.4.4#r22", "§9.7#r1", "§9.7#r2", "§9.7#r5", "§9.7#r6", "§9.7#r7", "§9.7#r9", "§9.4.1#r3", "§9.4.1#r8", "§9.4.1#r5", "§Aturan Logika Modul#r43", "§9.4.2#r33"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r24": 8
  "§Aturan Logika Modul#r25": [2, 14]
  "§Aturan Logika Modul#r26": [3, 9]
  "§Aturan Logika Modul#r27": [8, 11]
  "§Aturan Logika Modul#r28": [8, 65, 67]
  "§Aturan Logika Modul#r29": [11, 12]
  "§Aturan Logika Modul#r30": 14
  "§Aturan Logika Modul#r31": [40, 50]
  "§Aturan Logika Modul#r32": [20, 25, 30, 57, 60]
  "§Aturan Logika Modul#r33": [35, 38]
  "§Aturan Logika Modul#r34": [23, 28, 33]
  "§Aturan Logika Modul#r36": 3
  "§Aturan Logika Modul#r38": [4, 6]
  "§Aturan Logika Modul#r39": [40, 44]
  "§Aturan Logika Modul#r40": [41, 45]
  "§Aturan Logika Modul#r41": [42, 46]
  "§Aturan Logika Modul#r42": [52, 54]
  "§Aturan Logika Modul#r58": [40, 44, 50]
  "§Aturan Logika Modul#r59": 48
  "§9.2#b8": [8, 9, 12, 14]
  "§9.4.3#b2": [4, 6]
  "§9.4.3#b3": 11
  EC-DMG-03: [4, 6]
  EC-DMG-09: [40, 41]
  EC-DMG-10: [44, 45]
  EC-DMG-25: 48
  "§9.4.4#r3": [4, 6]
  "§9.4.4#r19": [40, 63]
  "§9.4.4#r20": [44, 70]
  "§9.4.4#r22": 48
  "§9.7#r1": 2
  "§9.7#r2": [8, 11, 65, 67]
  "§9.7#r5": [14, 15, 17]
  "§9.7#r6": [20, 25, 35]
  "§9.7#r7": [30, 38]
  "§9.7#r9": [40, 44, 48, 50, 62, 69]
  "§9.4.1#r3": [2, 40]
  "§9.4.1#r8": [4, 23, 28, 33, 52, 72, 74, 75, 77, 79, 82, 85, 88, 91]
  "§9.4.1#r5": 50
  "§Aturan Logika Modul#r43": [72, 74, 75, 77, 79, 82, 85, 88, 91]
  "§9.4.2#r33": [72, 74, 75, 77, 79, 82, 85, 88, 91]
---

# Efek Damage record ke status global aset: Damaged saat record Damaged, laporan pemegang vs scan selama Waiting for Confirmation, hitung ulang saat Reject/Cancel, Normal atau TAG Reported saat Repaired, dan transaksi berjalan tidak berubah, serta Condition tidak berubah dan record tetap Active selama aset In Transfer Process

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged yang melapor, memutuskan Confirm dan Reject, dan menjalankan Mark as Repaired.
  - Aktor peminjaman `Yoga Tanuwijaya {runId}` dan Aktor penugasan `Dewi Anggraini {runId}`, tanpa hak Update Manage asset & TAG.
  - Aktor pemindahan aset `Tono Riyadi {runId}`, yang juga mengakhiri Transfer.
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
  - DU-202-20: Aset `Toyota Avanza - 4 {runId}`, Group `Head Office {runId}`, TAG `RFID`, berstatus global `TAG Reported` sebelum dilaporkan rusak, lalu punya record `Damaged` sehingga status global `Damaged`.
  - DU-202-21: Aset `Projector Epson EB-X06 - 3 {runId}`, Group `Head Office {runId}`, TAG tanpa TAG, status global `Damaged`, punya record `Damaged`, tidak dipegang.
  - DU-202-22: Aset `Monitor Dell P2422H - 9 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-202-23: Aset `Handheld Scanner Zebra TC21 - 5 {runId}`, Group `Head Office {runId}`, TAG `QR`, status global `Assigned` kepada `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-202-24: What happened `Layar retak setelah terjatuh {runId}`, Damaged Photo `layar-retak.jpg`.
  - DU-202-25: Reason `Foto yang dikirim bukan foto aset ini {runId}`.
  - DU-202-26: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-202-27: Aset `Projector Epson EB-X06 - 8 {runId}`, Group `Head Office {runId}`, TAG `QR`, status global `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-28: Aset `Monitor Dell P2422H - 10 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `TAG Reported`, dipegang `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-29: Aset `Forklift Toyota 8FD - 5 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-202-30: Aset `Tablet Samsung Tab A8 - 7 {runId}`, Group `Head Office {runId}`, TAG `QR`, status global `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-31: Aset `Camera Canon EOS - 7 {runId}`, Group `Head Office {runId}`, TAG `RFID`, status global `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-202-32: Aset `Drill Bosch GSB - 5 {runId}`, Group `Head Office {runId}`, TAG `QR`, status global `Assigned` kepada `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-202-33: Aset `Pickup Toyota Hilux - 1 {runId}`, Group `Head Office {runId}`, tanpa TAG, status global `Damaged`, punya record `Damaged`, Custody `In Transfer Process` dengan baris Transfer `Waiting for Approval` menuju `Branch Surabaya {runId}`.
  - DU-202-34: Aset `Pickup Toyota Hilux - 2 {runId}`, Group `Head Office {runId}`, tanpa TAG, status global `Damaged`, punya record `Damaged`, Custody `In Transfer Process` dengan baris Transfer `In Transit` menuju `Branch Surabaya {runId}`.
  - DU-202-35: Aset `Pickup Toyota Hilux - 3 {runId}`, Group `Head Office {runId}`, tanpa TAG, status global `Damaged`, punya record `Damaged`, Custody `In Transfer Process` dengan baris Transfer `In Transit` menuju `Branch Surabaya {runId}`.
  - DU-202-36: Aset `Pickup Toyota Hilux - 4 {runId}`, Group `Head Office {runId}`, tanpa TAG, status global `Damaged`, punya record `Damaged`, Custody `In Transfer Process` dengan baris Transfer `In Transit` menuju `Branch Surabaya {runId}`.
  - DU-202-37: Aset `Pickup Toyota Hilux - 5 {runId}`, Group `Head Office {runId}`, tanpa TAG, status global `Damaged`, punya record `Damaged`, Custody `In Transfer Process` dengan baris Transfer `Waiting for Approval` menuju `Branch Surabaya {runId}`.
  - DU-202-38: Aset `Pickup Toyota Hilux - 6 {runId}`, Group `Head Office {runId}`, tanpa TAG, status global `Damaged`, punya record `Damaged`, Custody `In Transfer Process` dengan baris Transfer `Waiting for Approval` menuju `Branch Surabaya {runId}`.
  - DU-202-39: Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`.
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
46. Verifikasi penanda `Damaged` pada baris penugasan hilang bersama record

### Hasil Mark as Repaired menurut keadaan aset: TAG Reported dipertahankan, aset tanpa TAG menjadi Normal
47. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Toyota Avanza - 4 {runId}` yang sebelum dilaporkan rusak berstatus `TAG Reported`, dengan identifikasi manual dan Repair note `Komponen rusak sudah diganti {runId}`
48. Verifikasi record menjadi `Repaired` dan status global aset menjadi `TAG Reported`, bukan `Normal`
49. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 3 {runId}` yang tidak memiliki TAG dengan Repair note `Komponen rusak sudah diganti {runId}`
50. Verifikasi record menjadi `Repaired` tanpa permintaan Scan TAG, status global aset menjadi `Normal`, dan penanda Damaged pada aset hilang

### Return dan Unassign atas aset ber-record Damaged berjalan biasa dengan status Returned dan Unassigned
51. Aktor peminjaman `Yoga Tanuwijaya {runId}` menyelesaikan Return atas `Monitor Dell P2422H - 9 {runId}`
52. Verifikasi Return selesai biasa dengan status `Returned` dan record tetap `Damaged` tanpa record baru
53. Aktor penugasan `Dewi Anggraini {runId}` melakukan Unassign atas `Handheld Scanner Zebra TC21 - 5 {runId}`
54. Verifikasi Unassign selesai biasa dengan status `Unassigned` dan record tetap `Damaged` tanpa record baru

### Reject dan Cancel Report laporan pemegang menghitung ulang status global menjadi Borrowed atau TAG Reported
55. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Projector Epson EB-X06 - 8 {runId}` yang ia pinjam dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
56. Total Control `Agus Pratama {runId}` melakukan Reject atas laporan `Projector Epson EB-X06 - 8 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
57. Verifikasi record menjadi `Rejected` dan status global aset dihitung ulang menjadi `Borrowed` karena aset masih dipinjam `Budi Santoso {runId}`
58. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Monitor Dell P2422H - 10 {runId}` yang berstatus `TAG Reported` dan ia pegang dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
59. Pelapor umum `Budi Santoso {runId}` membatalkan laporannya lewat Cancel Report atas `Monitor Dell P2422H - 10 {runId}`
60. Verifikasi record menjadi `Canceled` dan status global aset dihitung ulang dari state aset terkini menjadi `TAG Reported`

### Mark as Repaired atas aset yang sedang dipinjam memicu tepat satu event damaged_resolved
61. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Forklift Toyota 8FD - 5 {runId}` yang sedang dipinjam dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
62. Verifikasi record menjadi `Repaired` dan baris peminjaman tetap `Borrowed`
63. Verifikasi tepat satu event `damaged_resolved` dikirim untuk record itu

### Laporan Aktor Borrow dan Aktor Assignment selama Waiting for Confirmation langsung mengubah status global menjadi Damaged
64. Aktor peminjaman `Yoga Tanuwijaya {runId}` mengirim Report Damaged atas `Tablet Samsung Tab A8 - 7 {runId}` yang sedang dipinjam dari halaman transaksi peminjaman dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
65. Verifikasi record berstatus `Waiting for Confirmation` sedangkan status global aset langsung menjadi `Damaged`
66. Aktor penugasan `Dewi Anggraini {runId}` mengirim Report Damaged atas `Camera Canon EOS - 7 {runId}` yang sedang ditugaskan dari halaman transaksi penugasan dengan What happened `Layar retak setelah terjatuh {runId}` dan Damaged Photo `layar-retak.jpg`
67. Verifikasi record berstatus `Waiting for Confirmation` sedangkan status global aset langsung menjadi `Damaged`

### Mark as Repaired atas aset yang sedang ditugaskan memicu tepat satu event damaged_resolved
68. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Drill Bosch GSB - 5 {runId}` yang sedang ditugaskan dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
69. Verifikasi record menjadi `Repaired` dan baris penugasan tetap `Assigned`
70. Verifikasi Mark as Repaired atas aset yang ditugaskan itu memicu tepat satu event `damaged_resolved`

### Selama Custody In Transfer Process Mark as Repaired dan Report Disposal ditolak server, Condition tidak berubah, dan record tetap Active
71. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Pickup Toyota Hilux - 1 {runId}` yang baris pemindahannya `Waiting for Approval` dengan Repair note `Komponen rusak sudah diganti {runId}`
72. Verifikasi Mark as Repaired itu ditolak server dan record tetap `Damaged`
73. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Pickup Toyota Hilux - 1 {runId}` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
74. Verifikasi Report Disposal itu ditolak server dan record tetap `Damaged`, bukan `Reported Disposal`
75. Verifikasi Condition aset `Pickup Toyota Hilux - 1 {runId}` tidak berubah dan record itu tetap record berjalan di sub-tab Active
76. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Pickup Toyota Hilux - 2 {runId}` yang baris pemindahannya `In Transit` dengan Repair note `Komponen rusak sudah diganti {runId}`
77. Verifikasi Mark as Repaired itu ditolak server dan record tetap `Damaged`, Condition aset tidak berubah, dan record tetap di sub-tab Active
78. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Pickup Toyota Hilux - 2 {runId}` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
79. Verifikasi Report Disposal itu ditolak server dan record tetap `Damaged`, bukan `Reported Disposal`

### Mark as Repaired aktif lagi setelah baris Transfer Completed, Returned to Origin, Rejected, atau Canceled
80. Aktor pemindahan aset `Tono Riyadi {runId}` menyelesaikan pemindahan atas `Pickup Toyota Hilux - 3 {runId}` sehingga baris pemindahan menjadi `Completed`
81. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Pickup Toyota Hilux - 3 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}`
82. Verifikasi Mark as Repaired itu diterima server dan record menjadi `Repaired`
83. Aktor pemindahan aset `Tono Riyadi {runId}` mengembalikan pemindahan atas `Pickup Toyota Hilux - 4 {runId}` ke asal sehingga baris pemindahan menjadi `Returned to Origin`
84. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Pickup Toyota Hilux - 4 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}`
85. Verifikasi Mark as Repaired itu diterima server dan record menjadi `Repaired`
86. Permintaan pemindahan atas `Pickup Toyota Hilux - 5 {runId}` ditolak pada tahap approval sehingga baris pemindahan menjadi `Rejected`
87. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Pickup Toyota Hilux - 5 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}`
88. Verifikasi Mark as Repaired itu diterima server dan record menjadi `Repaired`
89. Aktor pemindahan aset `Tono Riyadi {runId}` membatalkan pemindahan atas `Pickup Toyota Hilux - 6 {runId}` sehingga baris pemindahan menjadi `Canceled`
90. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Pickup Toyota Hilux - 6 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}`
91. Verifikasi Mark as Repaired itu diterima server dan record menjadi `Repaired`
