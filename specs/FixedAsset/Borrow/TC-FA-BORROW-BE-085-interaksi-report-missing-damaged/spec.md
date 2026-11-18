---
id: TC-FA-BORROW-BE-085-interaksi-report-missing-damaged
title: "Interaksi Borrow dengan laporan Damaged dan Missing saat dipinjam dan sesudah Return"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: ["BORROW-LOGIC-16aa", "BORROW-LOGIC-16ab", "BORROW-LOGIC-16ac", "BORROW-LOGIC-16ad", "BORROW-LOGIC-16ae", "BORROW-LOGIC-16af", "BORROW-LOGIC-16ag", "BORROW-LOGIC-16ah", "BORROW-LOGIC-16ai", "BORROW-LOGIC-16aj", "BORROW-LOGIC-16ak", "BORROW-LOGIC-16al", "BORROW-LOGIC-16at", "BORROW-LOGIC-16au", "BORROW-LOGIC-16ax", "BORROW-LOGIC-16ay", "BORROW-LOGIC-16az", "BORROW-LOGIC-16ba", "BORROW-LOGIC-16bb", "BORROW-LOGIC-16bc", "BORROW-LOGIC-16bd", "BORROW-LOGIC-16be", "BORROW-LOGIC-16bf", "BORROW-LOGIC-16bh", "BORROW-LOGIC-16bi", "BORROW-LOGIC-16bj", "BORROW-LOGIC-16bk", "BORROW-LOGIC-16bl", "BORROW-LOGIC-16c", "BORROW-LOGIC-16d", "BORROW-LOGIC-16e", "BORROW-LOGIC-16f", "BORROW-LOGIC-16g", "BORROW-LOGIC-16h", "BORROW-LOGIC-16i", "BORROW-LOGIC-16j", "BORROW-LOGIC-16k", "BORROW-LOGIC-16l", "BORROW-LOGIC-16m", "BORROW-LOGIC-16n", "BORROW-LOGIC-16r", "BORROW-LOGIC-16s", "BORROW-LOGIC-16t", "BORROW-LOGIC-16u", "BORROW-LOGIC-16w", "BORROW-LOGIC-16x", "BORROW-LOGIC-16y", "BORROW-LOGIC-16z", "EC-BRW-153", "F-BORROW-12.k1", "V-BRW-39", "§9.2#r48", "§9.2#r49", "§9.2#r50", "§9.2#r56"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-16aa": [50, 52]
  "BORROW-LOGIC-16ab": [50, 69]
  "BORROW-LOGIC-16ac": [38]
  "BORROW-LOGIC-16ad": [52, 74]
  "BORROW-LOGIC-16ae": [70]
  "BORROW-LOGIC-16af": [71]
  "BORROW-LOGIC-16ag": [78]
  "BORROW-LOGIC-16ah": [80]
  "BORROW-LOGIC-16ai": [79]
  "BORROW-LOGIC-16aj": [82]
  "BORROW-LOGIC-16ak": [83]
  "BORROW-LOGIC-16al": [88]
  "BORROW-LOGIC-16at": [90, 92, 94]
  "BORROW-LOGIC-16au": [95]
  "BORROW-LOGIC-16ax": [2, 3]
  "BORROW-LOGIC-16ay": [9]
  "BORROW-LOGIC-16az": [12]
  "BORROW-LOGIC-16ba": [15]
  "BORROW-LOGIC-16bb": [24, 28]
  "BORROW-LOGIC-16bc": [35]
  "BORROW-LOGIC-16bd": [34]
  "BORROW-LOGIC-16be": [39, 48]
  "BORROW-LOGIC-16bf": [41]
  "BORROW-LOGIC-16bh": [62]
  "BORROW-LOGIC-16bi": [66]
  "BORROW-LOGIC-16bj": [57, 75]
  "BORROW-LOGIC-16bk": [85]
  "BORROW-LOGIC-16bl": [86]
  "BORROW-LOGIC-16c": [3]
  "BORROW-LOGIC-16d": [4]
  "BORROW-LOGIC-16e": [7]
  "BORROW-LOGIC-16f": [8]
  "BORROW-LOGIC-16g": [14]
  "BORROW-LOGIC-16h": [23, 28]
  "BORROW-LOGIC-16i": [31]
  "BORROW-LOGIC-16j": [32]
  "BORROW-LOGIC-16k": [36]
  "BORROW-LOGIC-16l": [17]
  "BORROW-LOGIC-16m": [26]
  "BORROW-LOGIC-16n": [19, 21]
  "BORROW-LOGIC-16r": [38, 45]
  "BORROW-LOGIC-16s": [40]
  "BORROW-LOGIC-16t": [38, 45]
  "BORROW-LOGIC-16u": [47]
  "BORROW-LOGIC-16w": [57]
  "BORROW-LOGIC-16x": [55, 59]
  "BORROW-LOGIC-16y": [43, 64]
  "BORROW-LOGIC-16z": [61]
  "EC-BRW-153": [7, 8, 9, 12]
  "F-BORROW-12.k1": [7]
  "V-BRW-39": [88]
  "§9.2#r48": [2, 5, 14]
  "§9.2#r49": [43]
  "§9.2#r50": [69, 70, 72]
  "§9.2#r56": [38, 39, 76]
---

# Interaksi Borrow dengan laporan Damaged dan Missing saat dipinjam dan sesudah Return

## Prerequisites
- Aktor: `Agus Pratama {runId}` (Aktor Borrow, Asset Admin dengan hak Aktor Missing); `Sinta Maharani {runId}` (Aktor Borrow tanpa hak Aktor Missing dan tanpa hak Aktor Damaged); `Maya Putri {runId}` (Aktor Damaged); `Rudi Hartono {runId}` (Aktor Missing); `Dewi Lestari {runId}` dan `Bagus Santoso {runId}` (Borrower ber-akun); `Rina Kusuma {runId}` (PIC).
- Data:
  - DU-085-1: Group asal aset: Name `Head Office {runId}`
  - DU-085-2: User akun login: Name `Agus Pratama {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin dengan hak Aktor Missing`, Group penugasan `Head Office {runId}`
  - DU-085-3: User akun login: Name `Sinta Maharani {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin tanpa hak Aktor Missing dan tanpa hak Aktor Damaged`, Group penugasan `Head Office {runId}`
  - DU-085-4: User akun login: Name `Maya Putri {runId}`, Status `Active`, Activation Status `Activated`, Role `Aktor Damaged`, Group penugasan `Head Office {runId}`
  - DU-085-5: User akun login: Name `Rudi Hartono {runId}`, Status `Active`, Activation Status `Activated`, Role `Aktor Missing`, Group penugasan `Head Office {runId}`
  - DU-085-6: User akun login: Name `Dewi Lestari {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-085-7: User akun login: Name `Bagus Santoso {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-085-8: User akun login: Name `Rina Kusuma {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow, PIC`, Division `Marketing`
  - DU-085-9: Karyawan tanpa akun login: Name `Gita Anggraini {runId}`, Status `Active`, Division `Finance`, PIC `Rina Kusuma {runId}`
  - DU-085-10: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Laptop Dell Latitude 5440 {runId} dan Mouse Logitech MX Master 3 {runId} dalam satu BRW`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`
  - DU-085-11: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Proyektor Epson EB-X49 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`
  - DU-085-12: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Kamera Canon EOS 90D {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Waiting for Handover`
  - DU-085-13: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Printer Epson L3250 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Waiting for Approval`, Approver snapshot `Siti Aminah {runId}`
  - DU-085-14: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Speaker JBL PartyBox 310 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`
  - DU-085-15: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Monitor LG UltraFine 27 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Overdue`, Due date `T0 - 1 hari`, Notifikasi borrow_overdue varian Borrower `belum pernah dikirim`
  - DU-085-16: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Tripod Manfrotto MT055 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Extension `menunggu approval`, Max extensions `2`
  - DU-085-17: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Tablet Samsung Galaxy Tab S9 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`
  - DU-085-18: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Drone DJI Mavic 3 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Max extensions `2`
  - DU-085-19: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Handycam Sony FDR-AX43 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`
  - DU-085-20: Pinjaman berjalan: Borrower `Bagus Santoso {runId}`, Aset `Gimbal DJI RS 3 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`
  - DU-085-21: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Headset Logitech H390 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Laporan Missing `Waiting for Confirmation dari Dewi Lestari {runId}`
  - DU-085-22: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Kompresor Ingersoll Rand 2475 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Activity Lock `In Audit`
  - DU-085-23: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Genset Honda EU22i {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Activity Lock `Under Maintenance`
  - DU-085-24: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Bor Listrik Bosch GSB 13 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Activity Lock `In Audit`
  - DU-085-25: Pinjaman berjalan: Borrower `Gita Anggraini {runId}`, Aset `Kursi Gaming Secretlab Titan {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Status baris `Borrowed`, Due date `T0 + 3 hari`, PIC `Rina Kusuma {runId}`
  - DU-085-26: Aset sudah Missing dengan baris Returned: Asset Name `Gergaji Mesin Stihl MS 170 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Custody `Available`, Condition `Missing`, Status baris terakhir `Returned dengan penanda Missing`
- Kondisi:
  - T0 adalah waktu permintaan dikirim.
  - Aset pada pinjaman berjalan memakai aturan efektif yang mengizinkan Extend; `Monitor LG UltraFine 27 {runId}` sudah Overdue sejak T0 - 1 hari dan Due date reminders D-3 / D-1 / D-day sudah lewat.
  - Akun Agus, Sinta, Maya, Rudi, Dewi, Bagus, dan Rina aktif dan kredensialnya tersedia untuk fase 2.

## Test Steps

### Report Missing oleh pelapor admin menutup baris dan tidak memengaruhi baris lain
1. Agus mengirim Report Missing atas `Laptop Dell Latitude 5440 {runId}` dengan What happened `Laptop hilang dari ruang rapat`
2. Verifikasi laporan `Missing` dari Pelapor admin langsung berstatus `Missing` tanpa review
3. Verifikasi baris `Laptop Dell Latitude 5440 {runId}` pada saat itu juga ditutup `Returned` dengan penanda `Missing` tanpa scan, dan status global aset menjadi `Missing`
4. Verifikasi baris `Mouse Logitech MX Master 3 {runId}` pada BRW yang sama tidak terpengaruh dan tetap `Borrowed`
5. Verifikasi notifikasi laporan dikirim ke pemegang hak Manage asset & TAG

### Aset ditemukan tetapi masih dipegang Borrower dicatat lewat BRW baru
6. Rudi menjalankan Mark as Found atas `Laptop Dell Latitude 5440 {runId}` yang ternyata masih dipegang `Dewi Lestari {runId}`
7. Verifikasi Custody aset menjadi `Available` padahal aset ada di tangan Borrower
8. Verifikasi baris lama tetap `Returned` dengan penanda `Missing`
9. Verifikasi Borrow Detail BRW asal menampilkan kepada Aktor Borrow Alert `This asset was found. If Dewi Lestari {runId} still holds it, create a new borrow to record it.`
10. Agus mengirim Submit dengan Borrower `Dewi Lestari {runId}` atas `Laptop Dell Latitude 5440 {runId}` dengan Duration `2` Days dan Purpose `Pencatatan ulang aset ditemukan`
11. Agus menyelesaikan Hand Over atas BRW baru itu
12. Verifikasi BRW baru diterima dan mencatat aset yang masih dipegang Borrower lewat `[Submit]` lalu Hand Over

### Report Missing oleh Aktor Borrow tanpa hak Aktor Missing menunggu konfirmasi
13. Sinta mengirim Report Missing atas `Proyektor Epson EB-X49 {runId}` dengan What happened `Proyektor hilang saat pindah ruangan`
14. Verifikasi record laporan berstatus `Waiting for Confirmation` yang diputuskan Aktor Missing
15. Verifikasi status baris tetap Borrowed dan badge `Reported Missing` muncul pada baris itu
16. Rudi mengonfirmasi laporan `Missing` atas `Proyektor Epson EB-X49 {runId}`
17. Verifikasi baris ditutup `Returned` dengan penanda `Missing` setelah Aktor Missing mengonfirmasi

### Permintaan yang belum diserahkan dibatalkan sistem saat aset dilaporkan hilang
18. Rudi mengirim Report Missing atas `Kamera Canon EOS 90D {runId}` yang barisnya `Waiting for Handover`
19. Verifikasi baris `Kamera Canon EOS 90D {runId}` menjadi `Canceled` oleh `System` dengan alasan `Asset reported missing`
20. Rudi mengirim Report Missing atas `Printer Epson L3250 {runId}` yang barisnya `Waiting for Approval`
21. Verifikasi baris `Printer Epson L3250 {runId}` menjadi `Canceled` oleh `System` dengan alasan `Asset reported missing`

### Report Missing oleh Borrower atau PIC mengubah status global tetapi tidak status baris
22. Dewi mengirim Report Missing atas `Speaker JBL PartyBox 310 {runId}` dengan What happened `Speaker tertinggal di mobil dinas`
23. Verifikasi record laporan berstatus `Waiting for Confirmation` dan status global aset langsung `Missing`
24. Verifikasi status baris tetap Borrowed dan badge `Reported Missing` tampil di sampingnya
25. Dewi mengirim Cancel Missing Report atas laporan `Speaker JBL PartyBox 310 {runId}`
26. Verifikasi badge `Reported Missing` hilang dan baris tetap Borrowed
27. Rina mengirim Report Missing atas `Kursi Gaming Secretlab Titan {runId}` atas nama `Gita Anggraini {runId}` dengan What happened `Kursi tidak ditemukan di gudang`
28. Verifikasi laporan dari PIC diterima: record `Waiting for Confirmation`, status global aset `Missing`, dan status baris tetap Borrowed dengan badge `Reported Missing`

### Notifikasi pengingat selama laporan Missing menunggu dan sesudah ditolak
29. Dewi mengirim Report Missing atas `Monitor LG UltraFine 27 {runId}` yang barisnya sudah Overdue dengan What happened `Monitor tidak ditemukan di meja kerja`
30. Job pengingat harian dan Overdue berjalan
31. Verifikasi `borrow_due_soon` dan `borrow_overdue` varian Borrower tidak dikirim ke `Dewi Lestari {runId}` selama laporan menunggu konfirmasi
32. Verifikasi status Overdue tetap dihitung dan `borrow_overdue` varian Aktor Borrow tetap dikirim
33. Rudi menolak laporan `Missing` atas `Monitor LG UltraFine 27 {runId}` dengan Approval note `Aset masih di tangan Borrower`
34. Verifikasi `borrow_overdue` varian Borrower dikirim saat laporan ditolak karena baris sudah Overdue dan belum pernah dikirim
35. Verifikasi ambang Due date yang sudah lewat tidak dikirim mundur
36. Verifikasi pengingat ke Borrower berjalan lagi sesudah laporan ditolak

### Report Damaged saat dipinjam menjadikan status global Damaged dan memblokir Extend
37. Dewi mengirim Report Damaged atas `Tripod Manfrotto MT055 {runId}` yang punya pengajuan Extend menunggu, dengan satu foto dan What happened `Kaki tripod patah`
38. Verifikasi record laporan Borrower berstatus `Waiting for Confirmation` dan status global aset langsung `Damaged`
39. Verifikasi status baris tetap Borrowed dan badge `Reported Damaged` tampil selama record `Waiting for Confirmation`
40. Verifikasi notifikasi `borrow_damage_reported` dikirim ke Aktor Borrow Group asal dan Aktor Damaged Group aset
41. Verifikasi pengajuan Extend yang menunggu otomatis `Canceled` oleh `System` dengan alasan `Damage reported` tanpa dipulihkan setelahnya
42. Dewi mengajukan Extend atas `Tripod Manfrotto MT055 {runId}` dengan Extend by `1` dan Reason `Proyek belum selesai`
43. Verifikasi Extend diblokir dengan alasan `This asset has a damage report. Return it first.` selama laporan aktif
44. Sinta mengirim Report Damaged atas `Tablet Samsung Galaxy Tab S9 {runId}` dari Borrow Detail dengan satu foto dan What happened `Layar tablet retak`
45. Verifikasi record laporan Aktor Borrow tanpa hak Aktor Damaged berstatus `Waiting for Confirmation` dan status global aset langsung `Damaged`
46. Maya mengirim Report Damaged atas `Drone DJI Mavic 3 {runId}` dengan satu foto dan What happened `Baling-baling patah`
47. Verifikasi laporan Pelapor admin yang punya hak Aktor Damaged langsung berstatus `Damaged`
48. Verifikasi badge `Reported Damaged` tampil pada baris `Drone DJI Mavic 3 {runId}` untuk laporan yang dilaporkan Pelapor admin

### Keputusan laporan Damaged dan pembatalan oleh pelapor
49. Sinta mengirim Confirm atas laporan `Tablet Samsung Galaxy Tab S9 {runId}`
50. Verifikasi Aktor Borrow tidak dapat memutuskan laporan: Confirm oleh Sinta ditolak
51. Maya mengonfirmasi laporan `Tablet Samsung Galaxy Tab S9 {runId}` lewat menu `Damaged`
52. Verifikasi Confirm oleh Aktor Damaged menetapkan laporan menjadi `Damaged`, kapan saja
53. Bagus mengirim Report Damaged atas `Gimbal DJI RS 3 {runId}` dengan satu foto dan What happened `Motor gimbal rusak`
54. Sinta mengirim Cancel Damage Report atas laporan Bagus untuk `Gimbal DJI RS 3 {runId}`
55. Verifikasi laporan pelapor lain tidak dapat dibatalkan Aktor Borrow dan Cancel oleh Sinta ditolak
56. Bagus mengirim Cancel Damage Report atas laporannya sendiri untuk `Gimbal DJI RS 3 {runId}`
57. Verifikasi laporan dapat ditarik pelapornya sendiri dan badge `Reported Damaged` hilang
58. Maya mengirim Cancel Damage Report atas record `Damaged` untuk `Drone DJI Mavic 3 {runId}`
59. Verifikasi laporan yang sudah `Damaged` tidak dapat dibatalkan

### Mark as Repaired selama aset Borrowed memulihkan Extend dan penanda
60. Maya menjalankan Mark as Repaired atas `Drone DJI Mavic 3 {runId}` selama aset masih Borrowed
61. Verifikasi Mark as Repaired diterima selama aset Borrowed
62. Verifikasi badge `Damaged` pada baris `Drone DJI Mavic 3 {runId}` hilang
63. Dewi mengajukan Extend atas `Drone DJI Mavic 3 {runId}` dengan Extend by `1` dan Reason `Dipakai sampai akhir pekan`
64. Verifikasi Extend tersedia lagi dan permintaan diterima sesudah aset Repaired
65. Dewi menjalankan Return atas `Drone DJI Mavic 3 {runId}` dengan scan TAG
66. Verifikasi baris tetap Borrowed sampai Return lalu menjadi `Returned` tanpa penanda `Damaged`

### Return tidak menunggu keputusan laporan dan penanda Damaged mengikuti record
67. Dewi mengirim Report Damaged atas `Handycam Sony FDR-AX43 {runId}` dengan satu foto dan What happened `Lensa handycam tergores`
68. Dewi menjalankan Return atas `Handycam Sony FDR-AX43 {runId}` dengan scan TAG sementara laporan `Waiting for Confirmation`
69. Verifikasi Return tidak diblokir dan tidak menunggu keputusan laporan
70. Verifikasi baris menjadi `Returned` dengan penanda `Damaged` tanpa badge `Reported Damaged` di samping `Returned`
71. Verifikasi penanda `Damaged` menautkan ke record laporan yang sama dan tidak membuat record baru
72. Verifikasi penanda `Damaged` pada baris menyertakan foto Return
73. Maya menolak laporan `Handycam Sony FDR-AX43 {runId}` dengan Approval note `Aset masih di tangan Borrower`
74. Verifikasi Reject mengembalikan status aset seperti sebelum laporan
75. Verifikasi penanda `Damaged` pada baris `Returned` hilang karena record di-Reject, satu-satunya cara penanda itu hilang
76. Verifikasi pelepasan aset (Disposal) atas aset `Handycam Sony FDR-AX43 {runId}` yang Borrowed dan dilaporkan rusak menunggu Return

### Aset Missing ter-scan hanya dicatat sebagai deteksi
77. Agus memindai TAG `Headset Logitech H390 {runId}` pada halaman Return, sementara laporan `Missing` dari `Dewi Lestari {runId}` masih `Waiting for Confirmation`
78. Verifikasi scan hanya dicatat sebagai deteksi dan status `Missing` tidak berubah
79. Verifikasi scan itu tidak menemukan aset secara otomatis
80. Verifikasi baris tetap dapat di-Return dan daftar Return menandainya dengan badge `Reported Missing` bertautan ke Missing Log
81. Rudi mengirim Confirm atas laporan `Missing` `Headset Logitech H390 {runId}` sesudah deteksi scan
82. Verifikasi Confirm pada record itu Disabled dan ditolak setelah ada deteksi scan
83. Verifikasi baris tidak ditutup `Missing` padahal aset sudah di tangan admin
84. Agus menjalankan Return atas `Headset Logitech H390 {runId}` dengan scan TAG
85. Verifikasi Custody aset kembali `Available` di Group asal `Head Office {runId}`
86. Verifikasi record `Missing` tetap menunggu Aktor Missing, yaitu Reject atau Mark as Found, untuk memulihkan Condition
87. Agus memindai TAG `Gergaji Mesin Stihl MS 170 {runId}` pada form Borrow
88. Verifikasi scan ditolak dengan Dialog Blok `[OK]` berisi `Gergaji Mesin Stihl MS 170 {runId} is reported missing.`

### Activity Lock tidak menghalangi Return, Report Missing, dan Report Damaged
89. Dewi menjalankan Return atas `Kompresor Ingersoll Rand 2475 {runId}` yang Activity Lock-nya `In Audit` dengan scan TAG
90. Verifikasi Return diterima dan baris menjadi `Returned` walau aset `In Audit`
91. Agus mengirim Report Missing atas `Genset Honda EU22i {runId}` yang Activity Lock-nya `Under Maintenance` dengan What happened `Genset tidak ditemukan di basement`
92. Verifikasi Report Missing diterima walau aset `Under Maintenance`
93. Dewi mengirim Report Damaged atas `Bor Listrik Bosch GSB 13 {runId}` yang Activity Lock-nya `In Audit` dengan satu foto dan What happened `Mata bor patah`
94. Verifikasi Report Damaged diterima walau aset `In Audit`
95. Verifikasi Activity Lock `In Audit` pada `Bor Listrik Bosch GSB 13 {runId}` tidak dijeda oleh laporan, karena laporan tidak menjeda Stock Opname maupun Work Order

