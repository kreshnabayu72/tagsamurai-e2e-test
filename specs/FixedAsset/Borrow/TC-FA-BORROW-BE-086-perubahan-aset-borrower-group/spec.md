---
id: TC-FA-BORROW-BE-086-perubahan-aset-borrower-group
title: "Perubahan aset, tag, Borrower, Group, dan lock aktivitas saat transaksi berjalan"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: ["BORROW-LOGIC-16am", "BORROW-LOGIC-16an", "BORROW-LOGIC-16ao", "BORROW-LOGIC-16ap", "BORROW-LOGIC-16aq", "BORROW-LOGIC-16ar", "BORROW-LOGIC-16as", "BORROW-LOGIC-16av", "BORROW-LOGIC-16aw", "BORROW-LOGIC-16bg", "BORROW-LOGIC-16bm", "BORROW-LOGIC-16bn", "BORROW-LOGIC-16o", "BORROW-LOGIC-16p", "BORROW-LOGIC-16q", "BORROW-LOGIC-16v", "EC-BRW-01", "EC-BRW-160", "EC-BRW-36", "F-BORROW-12.k2", "F-BORROW-12.k3", "F-BORROW-12.k4", "F-BORROW-12.k5", "F-BORROW-12.k6", "F-BORROW-12.k7", "§9.2#r52", "§9.2#r54", "§9.2#r55", "§9.2#r57", "§9.2#r58", "§9.2#r59", "EB-EDG-3"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-16am": [3]
  "BORROW-LOGIC-16an": [5, 6]
  "BORROW-LOGIC-16ao": [8]
  "BORROW-LOGIC-16ap": [11]
  "BORROW-LOGIC-16aq": [18]
  "BORROW-LOGIC-16ar": [20]
  "BORROW-LOGIC-16as": [22, 24]
  "BORROW-LOGIC-16av": [26, 28]
  "BORROW-LOGIC-16aw": [30]
  "BORROW-LOGIC-16bg": [34]
  "BORROW-LOGIC-16bm": [9]
  "BORROW-LOGIC-16bn": [10]
  "BORROW-LOGIC-16o": [36]
  "BORROW-LOGIC-16p": [38]
  "BORROW-LOGIC-16q": [39]
  "BORROW-LOGIC-16v": [32]
  "EC-BRW-01": [5, 6, 8, 9, 10, 11, 14]
  "EC-BRW-160": [59]
  "EC-BRW-36": [53, 55, 57]
  "F-BORROW-12.k2": [3]
  "F-BORROW-12.k3": [42, 45]
  "F-BORROW-12.k4": [5, 11, 12, 16]
  "F-BORROW-12.k5": [47, 49, 51]
  "F-BORROW-12.k6": [53, 55, 57]
  "F-BORROW-12.k7": [59]
  "§9.2#r52": [3]
  "§9.2#r54": [42, 45]
  "§9.2#r55": [5, 12, 16]
  "§9.2#r57": [47, 49, 51]
  "§9.2#r58": [53, 55, 57]
  "§9.2#r59": [59]
  "EB-EDG-3": [60]
---

# Perubahan aset, tag, Borrower, Group, dan lock aktivitas saat transaksi berjalan

## Prerequisites
- Aktor: `Agus Pratama {runId}` (Asset Admin, pengaju, Group `Head Office {runId}`); `Sinta Maharani {runId}` (Asset Admin, Aktor Borrow Group `Head Office {runId}`); `Maya Putri {runId}` (Aktor Damaged); `Rudi Hartono {runId}` (Aktor Missing); `Dewi Lestari {runId}` (Borrower ber-akun).
- Data:
  - DU-086-1: Group asal aset: Name `Head Office {runId}`
  - DU-086-2: Group punya baris aktif: Name `Gudang Cabang {runId}`
  - DU-086-3: Group hanya punya Draft berisi asetnya: Name `Gudang Arsip {runId}`
  - DU-086-4: User akun login: Name `Agus Pratama {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin, pengaju`, Group penugasan `Head Office {runId}`
  - DU-086-5: User akun login: Name `Sinta Maharani {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin, Aktor Borrow Group aset`, Group penugasan `Head Office {runId}`
  - DU-086-6: User akun login: Name `Maya Putri {runId}`, Status `Active`, Activation Status `Activated`, Role `Aktor Damaged`, Group penugasan `Head Office {runId}`
  - DU-086-7: User akun login: Name `Rudi Hartono {runId}`, Status `Active`, Activation Status `Activated`, Role `Aktor Missing`, Group penugasan `Head Office {runId}`
  - DU-086-8: User akun login: Name `Dewi Lestari {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-086-9: User akun login: Name `Fajar Nugroho {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-086-10: User akun login: Name `Rina Kusuma {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow, PIC`, Division `Marketing`
  - DU-086-11: User akun login: Name `Maya Putri PIC pengganti {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow, PIC`, Division `Marketing`
  - DU-086-12: Karyawan tanpa akun login: Name `Ayu Lestari {runId}`, Status `Active`, Division `Finance`, PIC `Rina Kusuma {runId}`
  - DU-086-13: Karyawan tanpa akun login: Name `Bima Prakoso {runId}`, Status `Active`, Division `Finance`, PIC `Rina Kusuma {runId}`
  - DU-086-14: Karyawan tanpa akun login: Name `Cici Paramitha {runId}`, Status `Active`, Division `Finance`, PIC `Rina Kusuma {runId}`
  - DU-086-15: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Kamera Fujifilm X-T30 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Tag lama `RFID-A1B2 {runId}`, Tag baru `RFID-C3D4 {runId}`, Due date `T0 + 3 hari`
  - DU-086-16: Pinjaman berjalan: Borrower `Fajar Nugroho {runId}`, Aset `Laptop Dell Latitude 5440 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Approval`, Pengaju `Agus Pratama {runId}`
  - DU-086-17: Pinjaman berjalan: Borrower `Fajar Nugroho {runId}`, Aset `Printer Epson L3250 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`, Pengaju `Agus Pratama {runId}`
  - DU-086-18: Pinjaman berjalan: Borrower `Fajar Nugroho {runId}`, Aset `Proyektor Epson EB-X49 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Pengaju `Agus Pratama {runId}`, Due date `T0 + 1 hari`
  - DU-086-19: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Fajar Nugroho {runId}`, Aset `Head Office: Speaker JBL PartyBox 310 {runId}`, Duration `2`, Purpose `Acara pelatihan`
  - DU-086-20: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Tablet Samsung Galaxy Tab S9 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Lifecycle aset `Unmanaged`
  - DU-086-21: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Lensa Canon RF 24-70 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`, Lifecycle aset `Unmanaged`
  - DU-086-22: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Kompresor Ingersoll Rand 2475 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Activity Lock `In Audit`, Max extensions `2`
  - DU-086-23: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Genset Honda EU22i {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Activity Lock `Under Maintenance`, Max extensions `2`
  - DU-086-24: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Bor Listrik Bosch GSB 13 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Due date `T0 - 1 hari`, Activity Lock `In Audit`
  - DU-086-25: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Drone DJI Mavic 3 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Condition `Normal`
  - DU-086-26: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Gimbal DJI RS 3 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Extension `menunggu approval`, Max extensions `2`
  - DU-086-27: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Bagus Santoso {runId}`, Aset `Head Office: Gimbal DJI RS 3 {runId}`, Duration `2`, Purpose `Liputan konser`
  - DU-086-28: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Headset Logitech H390 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Allowed borrower sebelum diubah `Division Finance`, Max assets per borrower sebelum diubah `3`, Max extensions `2`
  - DU-086-29: Aset tersedia untuk pengajuan berikutnya: Asset Name `Mikrofon Shure SM58 {runId}`, Group `Head Office {runId}`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Allowed borrower `Division Finance`, Max assets per borrower `3`
  - DU-086-30: Pinjaman berjalan: Borrower `Ayu Lestari {runId}`, Aset `Kursi Ergonomis Ergotec {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, PIC `Rina Kusuma {runId}`, Due date `T0 + 1 hari`
  - DU-086-31: Pinjaman berjalan: Borrower `Bima Prakoso {runId}`, Aset `Meja Rapat Kayu Jati {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, PIC `Rina Kusuma {runId}`, Due date `T0 + 1 hari`
  - DU-086-32: Pinjaman berjalan: Borrower `Cici Paramitha {runId}`, Aset `Papan Tulis Magnetik {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, PIC `Rina Kusuma {runId}`, Due date `T0 + 1 hari`
  - DU-086-33: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Rak Besi Heavy Duty {runId}`, Group `Gudang Cabang {runId}`, Status baris `Borrowed`, Due date `T0 + 3 hari`
  - DU-086-34: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Gudang Arsip: Lemari Arsip Besi {runId}`, Duration `2`, Purpose `Penataan arsip`
  - DU-086-35: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Scanner Fujitsu fi-8170 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Due date `T0 + 3 hari`
- Kondisi:
  - T0 adalah waktu permintaan dikirim.
  - Aset `Gimbal DJI RS 3 {runId}`, `Lensa Canon RF 24-70 {runId}`, dan `Tablet Samsung Galaxy Tab S9 {runId}` berstatus seperti disebut di entri datanya sebelum langkah dimulai.
  - Akun Agus, Sinta, Maya, Rudi, dan Dewi aktif dan kredensialnya tersedia untuk fase 2.

## Test Steps

### Tag diganti saat dipinjam
1. Tag `Kamera Fujifilm X-T30 {runId}` diganti dari `RFID-A1B2 {runId}` menjadi `RFID-C3D4 {runId}` saat barisnya `Borrowed`
2. Dewi menjalankan Return atas `Kamera Fujifilm X-T30 {runId}` dengan scan tag baru `RFID-C3D4 {runId}`
3. Verifikasi Return memakai tag baru diterima dan baris menjadi `Returned`

### Borrower dinonaktifkan: baris menunggu ditutup, Draft tidak diubah, Borrowed masuk Return list
4. `Fajar Nugroho {runId}` dinonaktifkan
5. Verifikasi baris `Laptop Dell Latitude 5440 {runId}` yang `Waiting for Approval` atas nama `Fajar Nugroho {runId}` otomatis `Canceled`
6. Verifikasi baris `Printer Epson L3250 {runId}` yang `Waiting for Handover` atas nama `Fajar Nugroho {runId}` otomatis `Canceled`
7. Agus mengirim Submit atas Draft `Fajar Nugroho {runId}` yang memuat `Speaker JBL PartyBox 310 {runId}`
8. Verifikasi Submit atas Draft Borrower yang nonaktif gagal, dan field Borrower menampilkan `Fajar Nugroho {runId} is no longer active. Pick another borrower.`
9. Verifikasi baris aset `Speaker JBL PartyBox 310 {runId}` pada Draft tidak berubah
10. Verifikasi Draft atas nama `Fajar Nugroho {runId}` tetap tersimpan
11. Verifikasi baris `Proyektor Epson EB-X49 {runId}` yang `Borrowed` masuk Return list offboarding
12. Verifikasi exit clearance `Fajar Nugroho {runId}` tertahan selama baris `Proyektor Epson EB-X49 {runId}` belum `Returned`
13. Job pengingat Due date harian berjalan
14. Verifikasi notifikasi yang ditujukan ke Borrower dialihkan ke pengaju `Agus Pratama {runId}` dan Aktor Borrow Group aset `Sinta Maharani {runId}`
15. Sinta menjalankan Return atas `Proyektor Epson EB-X49 {runId}` dengan scan TAG
16. Verifikasi baris `Proyektor Epson EB-X49 {runId}` menjadi `Returned` dan exit clearance tidak lagi tertahan oleh baris itu

### Aset Unmanaged saat dipinjam
17. Dewi menjalankan Return atas `Tablet Samsung Galaxy Tab S9 {runId}` yang Unmanaged dengan scan TAG
18. Verifikasi Return tetap diterima untuk menyelesaikan transaksi berjalan dan baris menjadi `Returned`
19. Dewi mengajukan Extend atas `Tablet Samsung Galaxy Tab S9 {runId}` yang Unmanaged dengan Extend by `1` dan Reason `Perlu satu hari lagi`
20. Verifikasi Extend tidak ditawarkan dan ditolak dengan alasan `This asset is Unmanaged and can't be extended.`
21. Sinta menyelesaikan Handover atas `Lensa Canon RF 24-70 {runId}` yang Unmanaged
22. Verifikasi Handover atas aset Unmanaged ditolak dan baris tetap `Waiting for Handover` sampai timeout
23. Sinta mengirim Cancel Borrow atas `Lensa Canon RF 24-70 {runId}` yang Unmanaged
24. Verifikasi Cancel Borrow tetap diterima dan baris menjadi `Canceled`

### Activity Lock saat dipinjam tidak menawarkan Extend dan tidak menghentikan Overdue
25. Dewi mengajukan Extend atas `Kompresor Ingersoll Rand 2475 {runId}` yang Activity Lock-nya `In Audit` dengan Extend by `1` dan Reason `Dipakai sampai akhir pekan`
26. Verifikasi Extend tidak ditawarkan dan ditolak dengan alasan `This asset is In Audit and can't be extended.`
27. Dewi mengajukan Extend atas `Genset Honda EU22i {runId}` yang Activity Lock-nya `Under Maintenance` dengan Extend by `1` dan Reason `Acara berlanjut`
28. Verifikasi Extend tidak ditawarkan dan ditolak dengan alasan `This asset is Under Maintenance and can't be extended.`
29. Waktu berlalu melewati pukul 00:00 pada H+1 sesudah Due date baris `Bor Listrik Bosch GSB 13 {runId}` menurut Time Zone General Settings penyewa
30. Verifikasi baris `Bor Listrik Bosch GSB 13 {runId}` berstatus `Overdue` walau aset masih `In Audit`, karena Overdue tetap dihitung

### Laporan Damaged: status baris tetap Borrowed dan Mark as Repaired memulihkan Condition
31. Dewi mengirim Report Damaged atas `Drone DJI Mavic 3 {runId}` dengan satu foto dan What happened `Baling-baling patah`
32. Verifikasi status baris `Drone DJI Mavic 3 {runId}` tetap `Borrowed` sampai Return
33. Maya menjalankan Mark as Repaired atas `Drone DJI Mavic 3 {runId}`
34. Verifikasi status global aset kembali ke Condition sebelumnya, yaitu `Normal`

### Aset dilaporkan hilang oleh Aktor Missing menutup Extension dan menandai Draft
35. Rudi mengirim Report Missing atas `Gimbal DJI RS 3 {runId}` yang punya pengajuan Extension menunggu
36. Verifikasi pengajuan Extension yang menunggu pada baris yang ditutup ikut `Canceled` dengan alasan `Asset reported missing`
37. Agus membuka Draft `Bagus Santoso {runId}` yang memuat `Gimbal DJI RS 3 {runId}`
38. Verifikasi Draft yang memuat aset itu tidak diubah
39. Verifikasi aset `Gimbal DJI RS 3 {runId}` ditandai tidak layak dengan `This asset can no longer be borrowed.` dan alasan `This asset is Missing and can't be borrowed.`

### Perubahan Allowed borrower dan Max assets tidak memengaruhi pinjaman berjalan
40. Allowed borrower `Headset Logitech H390 {runId}` diubah menjadi `Division Marketing` dan Max assets per borrower menjadi `1` saat barisnya `Borrowed`
41. Dewi mengajukan Extend atas `Headset Logitech H390 {runId}` dengan Extend by `1` dan Reason `Proyek belum selesai`
42. Verifikasi pinjaman berjalan tidak terpengaruh: Extend atas baris `Headset Logitech H390 {runId}` tetap diterima menurut snapshot
43. Allowed borrower `Mikrofon Shure SM58 {runId}` diubah menjadi `Division Marketing`
44. Dewi mengirim Submit dengan Borrower `Dewi Lestari {runId}` atas `Mikrofon Shure SM58 {runId}` dengan Duration `2` Days dan Purpose `Rekaman siniar`
45. Verifikasi pengajuan berikutnya memakai aturan baru dan ditolak dengan alasan `Dewi Lestari {runId} can't borrow assets from Head Office {runId}.`

### PIC dikosongkan, diganti, atau Borrower dibuatkan akun tidak menghentikan pinjaman
46. PIC `Ayu Lestari {runId}` dikosongkan di Users saat barisnya `Borrowed`
47. Verifikasi pinjaman `Kursi Ergonomis Ergotec {runId}` tidak dihentikan dan tetap `Borrowed`
48. PIC `Bima Prakoso {runId}` diganti menjadi `Maya Putri PIC pengganti {runId}` di Users saat barisnya `Borrowed`
49. Verifikasi pinjaman `Meja Rapat Kayu Jati {runId}` tidak dihentikan dan tampil serta ditujukan ke `Maya Putri PIC pengganti {runId}` sebagai PIC saat ini
50. `Cici Paramitha {runId}` dibuatkan akun login di Users saat barisnya `Borrowed`
51. Verifikasi pinjaman `Papan Tulis Magnetik {runId}` tidak dihentikan dan tampil serta ditujukan ke akun `Cici Paramitha {runId}` saat ini

### Penghapusan Group ditolak selama ada baris aktif dan Draft dibiarkan
52. Sinta mengirim penghapusan Group `Gudang Cabang {runId}` yang punya baris aktif `Rak Besi Heavy Duty {runId}`
53. Verifikasi penghapusan Group ditolak sampai semua baris aktif selesai dan baris tetap `Borrowed`
54. Sinta mengirim penghapusan Group `Gudang Arsip {runId}` yang hanya punya Draft berisi `Lemari Arsip Besi {runId}`
55. Verifikasi Draft atas nama `Dewi Lestari {runId}` dibiarkan tidak berubah dan tetap tersimpan
56. Agus membuka Draft `Dewi Lestari {runId}` yang memuat `Lemari Arsip Besi {runId}`
57. Verifikasi aset `Lemari Arsip Besi {runId}` ditandai saat Draft dibuka

### Penghapusan aset yang sedang dipinjam ditolak
58. Sinta mengirim penghapusan aset `Scanner Fujitsu fi-8170 {runId}` yang sedang `Borrowed`
59. Verifikasi penghapusan ditolak selama ada transaksi berjalan karena Custody aset bukan `Available`
60. Verifikasi nasib data dependen saat induknya dihapus mengikuti PRD: baris `Scanner Fujitsu fi-8170 {runId}` tetap `Borrowed` dan tidak ikut terhapus

