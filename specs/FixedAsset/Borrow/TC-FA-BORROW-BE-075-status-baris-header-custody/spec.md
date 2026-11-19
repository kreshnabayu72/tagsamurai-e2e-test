---
id: TC-FA-BORROW-BE-075-status-baris-header-custody
title: "Status baris, status header turunan, Custody aset, dan pemisahan status transaksi dari status global aset"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["BORROW-LOGIC-04a", "BORROW-LOGIC-04b", "BORROW-LOGIC-04c", "BORROW-LOGIC-04d", "BORROW-LOGIC-04e", "BORROW-LOGIC-04f", "BORROW-LOGIC-04g", "BORROW-LOGIC-21a", "BORROW-LOGIC-21b", "BORROW-LOGIC-21c", "BORROW-LOGIC-21d", "BORROW-LOGIC-21e", "BORROW-LOGIC-21f", "BORROW-LOGIC-21g", "BORROW-LOGIC-21h", "BORROW-LOGIC-21i", "BORROW-LOGIC-21j", "BORROW-LOGIC-21k", "BORROW-LOGIC-21l", "BORROW-LOGIC-21m", "BORROW-LOGIC-21n", "§9.2#p3", "§9.2#r1", "§9.2#r2", "§9.2#r3", "§9.2#r4", "§9.2#r5", "§9.2#r6", "§9.2#r7", "§9.2#r8", "§9.2#p4", "§9.2#p5", "§9.2#p6", "§9.2#r11", "§9.2#r12", "§9.2#r13", "§9.2#r14", "§9.2#r15", "§9.2#r16", "§9.2#r17", "§9.2#r18", "§9.2#r19", "§9.2#b2", "§9.2#b3", "§9.2#b4", "§9.2#r20", "§9.2#r21", "§9.2#r22", "§9.2#r23", "§9.2#r24", "§9.2#r25", "§9.2#r26", "§9.2#r27", "§9.2#r28", "§9.2#p7", "§9.4.3#b1"]
smoke: []
dependsOn: []
trace:
  "BORROW-LOGIC-04a": [1, 17, 19]
  "BORROW-LOGIC-04b": 21
  "BORROW-LOGIC-04c": 21
  "BORROW-LOGIC-04d": [26, 42]
  "BORROW-LOGIC-04e": [33, 35, 37, 39]
  "BORROW-LOGIC-04f": [23, 29]
  "BORROW-LOGIC-04g": 24
  "BORROW-LOGIC-21a": 61
  "BORROW-LOGIC-21b": 44
  "BORROW-LOGIC-21c": 44
  "BORROW-LOGIC-21d": 46
  "BORROW-LOGIC-21e": 46
  "BORROW-LOGIC-21f": [44, 54]
  "BORROW-LOGIC-21g": [45, 48]
  "BORROW-LOGIC-21h": [48, 56]
  "BORROW-LOGIC-21i": 50
  "BORROW-LOGIC-21j": 52
  "BORROW-LOGIC-21k": 58
  "BORROW-LOGIC-21l": 62
  "BORROW-LOGIC-21m": [45, 54]
  "BORROW-LOGIC-21n": 60
  "§9.2#p3": 40
  "§9.2#r1": 1
  "§9.2#r2": 21
  "§9.2#r3": 21
  "§9.2#r4": 26
  "§9.2#r5": 31
  "§9.2#r6": 33
  "§9.2#r7": 37
  "§9.2#r8": [35, 39]
  "§9.2#p4": 48
  "§9.2#p5": 27
  "§9.2#p6": [40, 63, 64, 65]
  "§9.2#r11": 1
  "§9.2#r12": [12, 63, 64, 66]
  "§9.2#r13": 2
  "§9.2#r14": [4, 65]
  "§9.2#r15": [13, 67]
  "§9.2#r16": 5
  "§9.2#r17": 9
  "§9.2#r18": 10
  "§9.2#r19": 11
  "§9.2#b2": [6, 7, 66, 67]
  "§9.2#b3": [12, 13, 14, 66, 67]
  "§9.2#b4": 15
  "§9.2#r20": 2
  "§9.2#r21": 3
  "§9.2#r22": 4
  "§9.2#r23": 5
  "§9.2#r24": 6
  "§9.2#r25": 7
  "§9.2#r26": 8
  "§9.2#r27": 9
  "§9.2#r28": 10
  "§9.2#p7": 9
  "§9.4.3#b1": 40
---

# Status baris, status header turunan, Custody aset, dan pemisahan status transaksi dari status global aset

## Prerequisites
- Aktor: Aktor Borrow (Asset Admin) yang cakupannya meliputi `Head Office {runId}`.
  - Approver `Rina Wijaya {runId}` (DU-075-4), hanya untuk keputusan Reject.
  - Borrower `Citra Dewi {runId}` (DU-075-3), hanya untuk Borrow Now atas dirinya sendiri.
  - Aktor yang berwenang mengonfirmasi laporan kerusakan dan laporan kehilangan dalam cakupan `Head Office {runId}`, hanya untuk konfirmasi laporan.
- Data:
  - DU-075-1: Group, Group asal aset: Name `Head Office {runId}`.
  - DU-075-2: User, Borrower karyawan aktif dengan akun login: Name `Budi Santoso {runId}`, Group `Head Office {runId}`, Status `Aktif`.
  - DU-075-3: User, Borrower kedua karyawan aktif dengan akun login: Name `Citra Dewi {runId}`, Group `Head Office {runId}`, Status `Aktif`.
  - DU-075-4: User, Approver aset yang butuh approval: Name `Rina Wijaya {runId}`, Role `Approver`, Cakupan `Head Office {runId}`.
  - DU-075-5: Asset, Aset yang dipinjam: Name `Laptop Dell Latitude {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`, Duration unit `Hours`.
  - DU-075-6: Asset, Aset yang dipinjam: Name `Projector Epson EB {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`.
  - DU-075-7: Asset, Aset yang dipinjam: Name `Excavator Komatsu {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approver `Rina Wijaya {runId}`, Approval type `Any one`.
  - DU-075-8: Asset, Aset yang dipinjam: Name `Genset Honda {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approver `Rina Wijaya {runId}`, Approval type `Any one`.
  - DU-075-9: Asset, Aset yang dipinjam: Name `Camera Canon EOS {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`.
  - DU-075-10: Asset, Aset yang dipinjam: Name `Meeting Mic Set {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Self service `ON`.
  - DU-075-11: Asset, Aset yang dipinjam: Name `Tablet Samsung {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Borrowed`, baris pinjamannya ada di DU-075-28.
  - DU-075-12: Asset, Aset yang dipinjam: Name `Speaker JBL {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Borrowed`, baris pinjamannya ada di DU-075-28.
  - DU-075-13: Asset, Aset yang dipinjam: Name `Monitor LG UltraWide {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, baris pinjamannya yang sudah Returned ada di DU-075-29.
  - DU-075-14: Draft, Draft Eko yang memuat aset yang sama dengan pengajuan Citra: Borrower `Eko Prasetyo {runId}`, Aset 1 `Camera Canon EOS {runId}`, Duration `2`, Unit `Days`, Purpose `Survei`.
  - DU-075-15: BRW, BRW awal dengan satu baris Waiting for Handover dan satu Waiting for Approval: Borrower `Budi Santoso {runId}`, Aset 1 `Printer HP LaserJet {runId}`, Status 1 `Waiting for Handover`, Aset 2 `Scanner Epson {runId}`, Status 2 `Waiting for Approval`.
  - DU-075-16: BRW, BRW awal dengan satu baris Borrowed dan satu Waiting for Handover: Borrower `Budi Santoso {runId}`, Aset 1 `Kamera Sony {runId}`, Status 1 `Borrowed`, Aset 2 `Bor Listrik Makita {runId}`, Status 2 `Waiting for Handover`.
  - DU-075-17: BRW, BRW awal dengan satu baris Borrowed dan satu Waiting for Approval: Borrower `Budi Santoso {runId}`, Aset 1 `Forklift Toyota {runId}`, Status 1 `Borrowed`, Aset 2 `Pompa Air Honda {runId}`, Status 2 `Waiting for Approval`.
  - DU-075-18: BRW, BRW awal dengan dua baris Borrowed dan satu Returned: Borrower `Budi Santoso {runId}`, Aset 1 `Laptop Asus Vivobook {runId}`, Status 1 `Borrowed`, Aset 2 `Laptop Acer Swift {runId}`, Status 2 `Borrowed`, Aset 3 `Laptop Lenovo ThinkPad {runId}`, Status 3 `Returned`.
  - DU-075-19: BRW, BRW awal dengan satu baris Overdue dan satu Waiting for Approval: Borrower `Budi Santoso {runId}`, Aset 1 `Projector Optoma {runId}`, Status 1 `Overdue`, Aset 2 `Projector Sony {runId}`, Status 2 `Waiting for Approval`.
  - DU-075-20: BRW, BRW awal dengan satu baris Borrowed dan satu Overdue: Borrower `Budi Santoso {runId}`, Aset 1 `Tablet Lenovo {runId}`, Status 1 `Borrowed`, Aset 2 `Tablet Xiaomi Pad {runId}`, Status 2 `Overdue`.
  - DU-075-21: BRW, BRW awal dengan dua baris Overdue: Borrower `Budi Santoso {runId}`, Aset 1 `Mesin Fotokopi Ricoh {runId}`, Status 1 `Overdue`, Aset 2 `Mesin Cuci Sharp {runId}`, Status 2 `Overdue`.
  - DU-075-22: BRW, BRW awal dengan satu baris Returned dan satu Canceled: Borrower `Budi Santoso {runId}`, Aset 1 `Meja Rapat Oval {runId}`, Status 1 `Returned`, Aset 2 `Kursi Ergonomis {runId}`, Status 2 `Canceled`.
  - DU-075-23: BRW, BRW awal dengan satu baris Rejected dan satu Canceled: Borrower `Budi Santoso {runId}`, Aset 1 `Kipas Angin Cosmos {runId}`, Status 1 `Rejected`, Aset 2 `Pompa Celup Shimizu {runId}`, Status 2 `Canceled`.
  - DU-075-24: BRW, BRW awal dengan seluruh baris Canceled: Borrower `Budi Santoso {runId}`, Aset 1 `Lensa Sigma {runId}`, Status 1 `Canceled`, Aset 2 `Tripod Manfrotto {runId}`, Status 2 `Canceled`.
  - DU-075-25: BRW, BRW awal dengan baris Borrowed yang punya pengajuan Extend menunggu review: Borrower `Budi Santoso {runId}`, Aset 1 `Monitor Dell {runId}`, Status 1 `Borrowed`.
  - DU-075-26: BRW, BRW awal dengan baris Borrowed yang punya pengajuan Extend menunggu approval: Borrower `Budi Santoso {runId}`, Aset 1 `Laptop Toshiba Dynabook {runId}`, Status 1 `Borrowed`.
  - DU-075-27: BRW, BRW awal dengan baris Overdue yang punya pengajuan Extend menunggu approval: Borrower `Budi Santoso {runId}`, Aset 1 `Laptop MSI Modern {runId}`, Status 1 `Overdue`.
  - DU-075-28: BRW, BRW awal Citra dengan dua baris Borrowed: Borrower `Citra Dewi {runId}`, Aset 1 `Tablet Samsung {runId}`, Status 1 `Borrowed`, Aset 2 `Speaker JBL {runId}`, Status 2 `Borrowed`.
  - DU-075-29: BRW, BRW awal Citra dengan satu baris Returned: Borrower `Citra Dewi {runId}`, Aset 1 `Monitor LG UltraWide {runId}`, Status 1 `Returned`.
  - DU-075-30: User, Borrower ketiga karyawan aktif dengan akun login tanpa pinjaman lain: Name `Eko Prasetyo {runId}`, Group `Head Office {runId}`, Status `Aktif`.
  - DU-075-31: BRW, BRW awal dengan baris Borrowed yang punya pengajuan Extend menunggu review dan satu Waiting for Handover: Borrower `Budi Santoso {runId}`, Aset 1 `Printer Brother {runId}`, Status 1 `Borrowed`, Aset 2 `Scanner Canon {runId}`, Status 2 `Waiting for Handover`.
  - DU-075-32: BRW, BRW awal dengan baris Borrowed yang punya pengajuan Extend menunggu review dan satu Waiting for Approval: Borrower `Budi Santoso {runId}`, Aset 1 `Proyektor Acer {runId}`, Status 1 `Borrowed`, Aset 2 `Mesin Label Brother {runId}`, Status 2 `Waiting for Approval`.
  - DU-075-33: BRW, BRW awal dengan baris Borrowed yang punya pengajuan Extend menunggu approval dan satu Waiting for Approval: Borrower `Budi Santoso {runId}`, Aset 1 `Monitor Samsung {runId}`, Status 1 `Borrowed`, Aset 2 `Mesin Absensi Fingerprint {runId}`, Status 2 `Waiting for Approval`.
  - DU-075-34: BRW, BRW awal dengan baris Overdue yang punya pengajuan Extend menunggu review: Borrower `Budi Santoso {runId}`, Aset 1 `Laptop HP Elitebook {runId}`, Status 1 `Overdue`.
- Kondisi:
  - Transaction timeout Company default, Max assets per borrower Company default `5`, dan Time Zone penyewa berlaku sebagai nilai lingkungan.
  - `Eko Prasetyo {runId}` dan `Citra Dewi {runId}` tidak punya baris `Overdue`.
  - Aset `Tablet Samsung {runId}` dan `Speaker JBL {runId}` sedang dipinjam `Citra Dewi {runId}` dengan baris Borrowed (DU-075-28), dan baris `Monitor LG UltraWide {runId}` milik `Citra Dewi {runId}` sudah Returned (DU-075-29).

## Test Steps

### Status header diturunkan dari status baris
1. Verifikasi header Draft atas nama `Eko Prasetyo {runId}` berstatus `Draft` dan Custody aset di dalamnya tetap `Available` karena Draft tidak terkunci
2. Verifikasi BRW dengan satu baris `Waiting for Handover` dan satu baris `Waiting for Approval` berstatus header `Waiting for Handover`
3. Verifikasi BRW dengan satu baris `Borrowed` dan satu baris `Waiting for Handover` berstatus header `Waiting for Handover`
4. Verifikasi BRW dengan satu baris `Borrowed` dan satu baris `Waiting for Approval` berstatus header `Waiting for Approval`
5. Verifikasi BRW dengan dua baris `Borrowed` dan satu baris `Returned` berstatus header `Borrowed`
6. Verifikasi BRW dengan satu baris `Overdue` dan satu baris `Waiting for Approval` berstatus header `Waiting for Approval` dengan penanda `Overdue`
7. Verifikasi BRW dengan satu baris `Borrowed` dan satu baris `Overdue` berstatus header `Borrowed` dengan penanda `Overdue`
8. Verifikasi BRW dengan dua baris `Overdue` berstatus header `Borrowed` dengan penanda `Overdue`
9. Verifikasi BRW dengan satu baris `Returned` dan satu baris `Canceled` berstatus header `Returned` dan baris `Canceled` tetap tampil di Detail
10. Verifikasi BRW dengan satu baris `Rejected` dan satu baris `Canceled` berstatus header `Rejected`
11. Verifikasi BRW yang seluruh barisnya `Canceled` berstatus header `Canceled`
12. Verifikasi BRW dengan baris `Borrowed` yang punya pengajuan Extend menunggu review berstatus header `Extension Request` dan status baris tetap `Borrowed`
13. Verifikasi BRW dengan baris `Borrowed` yang punya pengajuan Extend menunggu approval berstatus header `Extension Approval`
14. Verifikasi baris `Overdue` yang punya pengajuan Extend menunggu approval tampil dengan dua badge, `Overdue` dan `Extension Approval`
15. Verifikasi tidak ada status header `Partially approved`, `Closed`, maupun `Expired` pada seluruh BRW di atas

### Draft tidak mengunci aset
16. Aktor Borrow mengirim Submit untuk Borrower `Citra Dewi {runId}` dengan aset `Camera Canon EOS {runId}`
17. Verifikasi Submit berhasil walaupun aset `Camera Canon EOS {runId}` sudah ada di Draft atas nama `Eko Prasetyo {runId}`, karena Draft tidak mengunci aset
18. Aktor Borrow mengirim Submit atas Draft atas nama `Eko Prasetyo {runId}` yang memuat aset `Camera Canon EOS {runId}`
19. Verifikasi kelayakan dievaluasi ulang saat Submit dan Submit ditolak karena aset `Camera Canon EOS {runId}` sudah berada di transaksi aktif lain

### Custody mengikuti status baris sepanjang siklus
20. Aktor Borrow mengirim Submit untuk Borrower `Eko Prasetyo {runId}` dengan aset `Laptop Dell Latitude {runId}`, `Projector Epson EB {runId}`, `Excavator Komatsu {runId}`, dan `Genset Honda {runId}`
21. Verifikasi Custody tiap baris menjadi `In Borrow Process`, sebagai bagian status global aset, baik baris `Waiting for Handover` maupun baris `Waiting for Approval`
22. Aktor Borrow mengirim Submit untuk Borrower `Citra Dewi {runId}` dengan aset `Excavator Komatsu {runId}`
23. Verifikasi Submit ditolak dengan `This asset is already in [BRW No.].` karena aset yang `In Borrow Process` tidak boleh masuk Borrow lain
24. Verifikasi pengajuan tidak menerima periode mulai, aset terkunci sejak Submit, dan tidak ada reservasi per periode
25. Aktor Borrow menyelesaikan Handover baris `Laptop Dell Latitude {runId}`
26. Verifikasi baris `Laptop Dell Latitude {runId}` berstatus `Borrowed` dan Custody aset menjadi `Borrowed`
27. Verifikasi Due date baris `Laptop Dell Latitude {runId}` disimpan per baris sebagai waktu handover ditambah Duration
28. Aktor Borrow mengirim Submit untuk Borrower `Citra Dewi {runId}` dengan aset `Laptop Dell Latitude {runId}`
29. Verifikasi Submit ditolak karena aset yang `Borrowed` tidak boleh masuk Borrow lain
30. Waktu berlalu sampai Due date baris `Laptop Dell Latitude {runId}` terlewati
31. Verifikasi baris `Laptop Dell Latitude {runId}` berstatus `Overdue` dan Custody tetap `Borrowed` dengan penanda Overdue
32. Aktor Borrow menyelesaikan Return baris `Laptop Dell Latitude {runId}`
33. Verifikasi baris `Laptop Dell Latitude {runId}` berstatus `Returned`, Custody aset kembali `Available`, dan Condition tidak berubah
34. Aktor Borrow membatalkan baris `Projector Epson EB {runId}` lewat Cancel Borrow per baris
35. Verifikasi baris `Projector Epson EB {runId}` berstatus `Canceled` dan Custody aset kembali `Available`
36. Approver `Rina Wijaya {runId}` menolak baris `Excavator Komatsu {runId}` dengan Approval note
37. Verifikasi baris `Excavator Komatsu {runId}` berstatus `Rejected` dan Custody aset kembali `Available`
38. Waktu berlalu sampai Transaction timeout baris `Genset Honda {runId}` terlewati
39. Verifikasi baris `Genset Honda {runId}` ditutup sistem dengan status `Canceled` alasan `Timed out (Waiting for Approval)`, Custody aset kembali `Available`, dan aset dikembalikan ke Draft baru
40. Verifikasi status header BRW itu dihitung ulang dari baris dan tidak diubah langsung
41. Borrower `Citra Dewi {runId}` mengirim Borrow Now untuk dirinya sendiri dengan aset `Meeting Mic Set {runId}`
42. Verifikasi baris `Meeting Mic Set {runId}` langsung berstatus `Borrowed` tanpa melewati `Waiting for Handover` dan Custody aset menjadi `Borrowed`

### Status transaksi dan status global aset berdiri sendiri
43. Aktor Borrow membuat laporan kerusakan atas aset `Tablet Samsung {runId}` dari Detail BRW milik `Citra Dewi {runId}` (DU-075-28) dan laporan menunggu konfirmasi
44. Verifikasi status global aset `Tablet Samsung {runId}` menjadi Condition `Damaged` seketika, tampil sebagai status aset dan bukan di kolom `Status` baris Borrow
45. Verifikasi baris `Tablet Samsung {runId}` tetap berstatus `Borrowed` dan hanya mendapat badge `Reported Damaged`
46. Verifikasi Borrow hanya mengubah Custody: Custody aset `Tablet Samsung {runId}` tetap `Borrowed` dan Condition `Damaged` diubah oleh laporan kerusakan, bukan oleh Borrow
47. Aktor Borrow menyelesaikan Return baris `Tablet Samsung {runId}`
48. Verifikasi baris `Tablet Samsung {runId}` berstatus `Returned` dan badge `Damaged` dipasang saat baris menjadi `Returned`
49. Aktor yang berwenang atas laporan kerusakan mengonfirmasi record kerusakan aset `Tablet Samsung {runId}` sampai final
50. Verifikasi badge `Damaged` pada baris `Tablet Samsung {runId}` mengikuti record sampai record itu final
51. Aset `Tablet Samsung {runId}` selesai di-repair
52. Verifikasi badge `Damaged` pada baris `Tablet Samsung {runId}` tidak berubah sesudah aset di-repair
53. Aktor Borrow membuat laporan kehilangan atas aset `Speaker JBL {runId}` dari Detail BRW milik `Citra Dewi {runId}` (DU-075-28) dan laporan menunggu konfirmasi
54. Verifikasi status global aset `Speaker JBL {runId}` menjadi Condition `Missing` seketika, sedangkan baris tetap `Borrowed` dengan badge `Reported Missing`
55. Aktor yang berwenang atas laporan kehilangan mengonfirmasi laporan aset `Speaker JBL {runId}`
56. Verifikasi baris `Speaker JBL {runId}` berstatus `Returned` dengan badge `Missing`, Custody aset `Available`, dan Condition aset `Missing`
57. Aset `Speaker JBL {runId}` ditemukan
58. Verifikasi badge `Missing` pada baris `Speaker JBL {runId}` tidak berubah sesudah aset ditemukan
59. Aktor yang berwenang atas laporan kerusakan membuat record kerusakan atas aset `Monitor LG UltraWide {runId}` sesudah baris `Monitor LG UltraWide {runId}` berstatus `Returned`
60. Verifikasi baris `Monitor LG UltraWide {runId}` tidak mendapat penanda `Damaged`
61. Verifikasi kolom `Status` baris Borrow hanya memuat status baris dan dimiliki Borrow
62. Verifikasi Condition aset hanya tampil sebagai rujukan di transaksi dan status global aset tidak diturunkan dari status baris

### Header Extension Request menang atas baris yang menunggu tindakan lain
63. Verifikasi BRW (DU-075-31) dengan baris `Borrowed` yang punya pengajuan Extend menunggu review dan baris `Waiting for Handover` berstatus header `Extension Request`, bukan `Waiting for Handover`
64. Verifikasi BRW (DU-075-32) dengan baris `Borrowed` yang punya pengajuan Extend menunggu review dan baris `Waiting for Approval` berstatus header `Extension Request`, bukan `Waiting for Approval`
65. Verifikasi BRW (DU-075-33) dengan baris `Borrowed` yang punya pengajuan Extend menunggu approval dan baris `Waiting for Approval` berstatus header `Waiting for Approval`, bukan `Extension Approval`

### Header baris Overdue yang punya pengajuan Extend
66. Verifikasi BRW (DU-075-34) dengan baris `Overdue` yang punya pengajuan Extend menunggu review berstatus header `Extension Request` dengan penanda `Overdue`
67. Verifikasi BRW (DU-075-27) dengan baris `Overdue` yang punya pengajuan Extend menunggu approval berstatus header `Extension Approval` dengan penanda `Overdue`
