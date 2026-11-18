---
id: TC-FA-BORROW-BE-076-approval-aturan-server
title: "Approval per aset: approver snapshot, mode Any one dan All, self-approval guard, fallback, dan keputusan sekaligus"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
owner: BE
sourceRules: ["BORROW-LOGIC-06a", "BORROW-LOGIC-06b", "BORROW-LOGIC-06c", "BORROW-LOGIC-06d", "BORROW-LOGIC-06e", "BORROW-LOGIC-06f", "BORROW-LOGIC-06g", "BORROW-LOGIC-06h", "BORROW-LOGIC-06i", "BORROW-LOGIC-06j", "BORROW-LOGIC-06k", "BORROW-LOGIC-06l", "BORROW-LOGIC-06m", "BORROW-LOGIC-06n", "BORROW-LOGIC-06o", "BORROW-LOGIC-06p", "BORROW-LOGIC-06q", "BORROW-LOGIC-07a", "BORROW-LOGIC-07b", "BORROW-LOGIC-07c", "BORROW-LOGIC-07d", "BORROW-LOGIC-07e", "BORROW-LOGIC-07f", "BORROW-LOGIC-07g", "BORROW-LOGIC-07h", "BORROW-LOGIC-07i", "BORROW-LOGIC-07j", "BORROW-LOGIC-07k", "BORROW-LOGIC-07l", "V-BRW-15", "EC-BRW-08", "EC-BRW-09", "EC-BRW-10", "EC-BRW-109", "EC-BRW-110", "EC-BRW-13", "EC-BRW-133", "EC-BRW-70", "F-BORROW-04.k1", "F-BORROW-04.k2", "F-BORROW-04.k3", "F-BORROW-04.k4", "F-BORROW-04.k5", "F-BORROW-04.k8", "§2.2#r2", "§9.2#b25", "§9.2#b27", "§9.2#b30", "§9.2#r34", "§9.2#r35", "§9.2#p25", "§9.2#p27", "§9.2#p28", "§9.2#r45", "§9.3#b2", "§10#r5"]
smoke: []
dependsOn: []
trace:
  "BORROW-LOGIC-06a": 12
  "BORROW-LOGIC-06b": 9
  "BORROW-LOGIC-06c": [58, 59]
  "BORROW-LOGIC-06d": 10
  "BORROW-LOGIC-06e": 11
  "BORROW-LOGIC-06f": 19
  "BORROW-LOGIC-06g": 19
  "BORROW-LOGIC-06h": [60, 61]
  "BORROW-LOGIC-06i": 60
  "BORROW-LOGIC-06j": 59
  "BORROW-LOGIC-06k": 11
  "BORROW-LOGIC-06l": 13
  "BORROW-LOGIC-06m": [13, 14]
  "BORROW-LOGIC-06n": 37
  "BORROW-LOGIC-06o": 37
  "BORROW-LOGIC-06p": 39
  "BORROW-LOGIC-06q": 40
  "BORROW-LOGIC-07a": 16
  "BORROW-LOGIC-07b": [47, 48]
  "BORROW-LOGIC-07c": 47
  "BORROW-LOGIC-07d": 15
  "BORROW-LOGIC-07e": [23, 32]
  "BORROW-LOGIC-07f": 27
  "BORROW-LOGIC-07g": 25
  "BORROW-LOGIC-07h": 27
  "BORROW-LOGIC-07i": [24, 29]
  "BORROW-LOGIC-07j": 34
  "BORROW-LOGIC-07k": [2, 7]
  "BORROW-LOGIC-07l": [5, 6]
  "V-BRW-15": 5
  "EC-BRW-08": 47
  "EC-BRW-09": [2, 5, 6]
  "EC-BRW-10": 50
  "EC-BRW-109": 62
  "EC-BRW-110": 63
  "EC-BRW-13": 54
  "EC-BRW-133": 60
  "EC-BRW-70": 56
  "F-BORROW-04.k1": [9, 10, 11]
  "F-BORROW-04.k2": [5, 50]
  "F-BORROW-04.k3": 47
  "F-BORROW-04.k4": [2, 3]
  "F-BORROW-04.k5": [40, 41, 43]
  "F-BORROW-04.k8": [54, 56]
  "§2.2#r2": 40
  "§9.2#b25": [44, 61]
  "§9.2#b27": 17
  "§9.2#b30": 39
  "§9.2#r34": [23, 25, 32]
  "§9.2#r35": [24, 29, 34]
  "§9.2#p25": 35
  "§9.2#p27": [54, 56]
  "§9.2#p28": 21
  "§9.2#r45": [21, 35]
  "§9.3#b2": [16, 42]
  "§10#r5": 12
---

# Approval per aset: approver snapshot, mode Any one dan All, self-approval guard, fallback, dan keputusan sekaligus

## Prerequisites
- Aktor: Aktor Borrow `Dian Permata {runId}`, Asset Admin dengan cakupan `Head Office {runId}` dan satu-satunya Total Control, sebagai pengaju.
  - Approver `Rina Wijaya {runId}`, `Sari Wulandari {runId}`, `Tono Prasetyo {runId}`, dan `Agus Salim {runId}` (pemegang Role Transaksi Approver pada `Head Office {runId}`), serta Group Manager `Gita Pramesti {runId}`, masing-masing hanya untuk keputusan atau pengamatan yang disebut di langkah.
- Data:
  - DU-076-1: Group, Group asal aset dengan Group Manager Gita: Name `Head Office {runId}`, Group Manager `Gita Pramesti {runId}`.
  - DU-076-2: Group, Group turunan Head Office; approver diwarisi dari Group induk: Name `Head Office Gudang {runId}`, Group induk `Head Office {runId}`.
  - DU-076-3: Group, Group asal tanpa approver lain dan tanpa Group Manager lain: Name `Gudang Terpencil {runId}`, Approver `Dian Permata {runId}`, Group Manager `Dian Permata {runId}`.
  - DU-076-4: User, Borrower yang juga pemegang Role Transaksi Approver pada Group Head Office: Name `Budi Santoso {runId}`, Group `Head Office {runId}`, Role `Approver`, Status `Aktif`.
  - DU-076-5: User, Aktor Borrow pengaju, Asset Admin, dan Total Control: Name `Dian Permata {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`, Total Control `ya`.
  - DU-076-6: User, Pemegang Role Approver pada Group Head Office: Name `Rina Wijaya {runId}`, Role `Approver`, Cakupan `Head Office {runId}`, Status `Aktif`.
  - DU-076-7: User, Pemegang Role Approver pada Group Head Office: Name `Sari Wulandari {runId}`, Role `Approver`, Cakupan `Head Office {runId}`, Status `Aktif`.
  - DU-076-8: User, Pemegang Role Approver pada Group Head Office: Name `Tono Prasetyo {runId}`, Role `Approver`, Cakupan `Head Office {runId}`, Status `Aktif`.
  - DU-076-9: User, Pemegang Role Group Manager pada Group Head Office: Name `Gita Pramesti {runId}`, Role `Group Manager`, Cakupan `Head Office {runId}`, Status `Aktif`.
  - DU-076-10: User, Approver yang kemudian dinonaktifkan: Name `Agus Salim {runId}`, Role `Approver`, Cakupan `Head Office {runId}`, Status `Aktif`.
  - DU-076-11: Asset, Aset yang dipinjam: Name `Laptop Dell Latitude {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId} dan Sari Wulandari {runId}`.
  - DU-076-12: Asset, Aset yang dipinjam: Name `Laptop HP ProBook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId} dan Sari Wulandari {runId}`.
  - DU-076-13: Asset, Aset yang dipinjam: Name `Excavator Komatsu {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `All`, Approver `Rina Wijaya {runId} dan Sari Wulandari {runId}`.
  - DU-076-14: Asset, Aset yang dipinjam: Name `Bulldozer Caterpillar {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `All`, Approver `Rina Wijaya {runId} dan Sari Wulandari {runId}`.
  - DU-076-15: Asset, Aset yang dipinjam: Name `Genset Honda {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Tono Prasetyo {runId}`.
  - DU-076-16: Asset, Aset yang dipinjam: Name `Projector Epson EB {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Auto-approve `sampai 3 hari`, Approver `Tono Prasetyo {runId}`.
  - DU-076-17: Asset, Aset yang dipinjam: Name `Camera Canon EOS {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Auto-approve `sampai 3 hari`, Approver `Tono Prasetyo {runId}`, Approval type `Any one`.
  - DU-076-18: Asset, Aset yang dipinjam: Name `Forklift Toyota {runId}`, Group asal `Head Office Gudang {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `diwarisi dari Group induk: Tono Prasetyo {runId}`.
  - DU-076-19: Asset, Aset yang dipinjam: Name `Mesin Bor Bosch {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Agus Salim {runId}`.
  - DU-076-20: Asset, Aset yang dipinjam: Name `Printer HP LaserJet {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Budi Santoso {runId}`.
  - DU-076-21: Asset, Aset yang dipinjam: Name `Scanner Epson {runId}`, Group asal `Gudang Terpencil {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Dian Permata {runId}`.
  - DU-076-22: Asset, Aset yang dipinjam: Name `Monitor Dell {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`, Status baris `Borrowed`.
  - DU-076-23: Asset, Aset yang dipinjam: Name `Monitor LG UltraWide {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`, Status baris `Borrowed`.
  - DU-076-24: Asset, Aset yang dipinjam: Name `Tablet Samsung {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`.
  - DU-076-25: Asset, Aset yang dipinjam: Name `Speaker JBL {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`.
  - DU-076-26: Asset, Aset yang dipinjam: Name `Kamera Sony {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`.
  - DU-076-27: BRW, BRW awal Budi pertama dengan baris Monitor Dell Borrowed: Borrower `Budi Santoso {runId}`, Aset 1 `Monitor Dell {runId}`, Status 1 `Borrowed`.
  - DU-076-28: BRW, BRW awal Budi kedua dengan baris Monitor LG UltraWide Borrowed: Borrower `Budi Santoso {runId}`, Aset 1 `Monitor LG UltraWide {runId}`, Status 1 `Borrowed`.
  - DU-076-29: BRW, BRW awal dengan satu pengajuan Borrow dan dua pengajuan Extension yang semuanya sudah diputuskan Rina: Borrower `Budi Santoso {runId}`, Pengajuan 1 `Borrow`, Pengajuan 2 `Extension`, Pengajuan 3 `Extension`, Approver `Rina Wijaya {runId}`, Keputusan `Approved`.
  - DU-076-30: BRW, BRW awal dengan dua aset yang diputuskan Rina dan Sari, untuk melihat progres approval: Borrower `Budi Santoso {runId}`, Aset 1 `Laptop Dell Latitude {runId}`, Keputusan Sari `Approved`, Approval Note Sari `Disetujui untuk proyek gudang`, Approve Duration Sari `3`.
- Kondisi:
  - Daftar approver tiap aset di entri data menjadi snapshot saat Submit.
  - Transaction timeout Company default berlaku sebagai nilai lingkungan.
  - `Dian Permata {runId}` adalah satu-satunya Total Control entitas aktor, dan Group Manager `Gudang Terpencil {runId}` adalah `Dian Permata {runId}`.

## Test Steps

### Self-approval guard dan fallback
1. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Printer HP LaserJet {runId}`
2. Verifikasi `Budi Santoso {runId}` dikeluarkan dari daftar approver aset `Printer HP LaserJet {runId}` karena Borrower, dan daftar yang kosong dirutekan ke fallback Group Manager `Gita Pramesti {runId}`
3. Verifikasi pada mode All, pengaju dan Borrower yang dikeluarkan tidak dihitung sebagai suara yang dibutuhkan, dan satu orang tidak dihitung dua kali pada satu aset
4. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Scanner Epson {runId}`
5. Verifikasi Submit ditolak dengan `There is no eligible approver for [Asset Name]. Ask someone else to submit this borrow.` karena daftar approver dan seluruh fallback habis oleh self-approval guard
6. Verifikasi tidak ada BRW yang dibuat untuk aset `Scanner Epson {runId}`
7. Verifikasi pengaju `Dian Permata {runId}` dan Borrower dikeluarkan dari daftar approver tiap aset di transaksi itu

### Pengajuan approval per Transaction ID dan aturan per aset
8. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Laptop Dell Latitude {runId}`, `Excavator Komatsu {runId}`, `Genset Honda {runId}`, `Projector Epson EB {runId}`, `Camera Canon EOS {runId}`, dan `Forklift Toyota {runId}`, Duration `2` Days untuk `Projector Epson EB {runId}` dan Duration `5` Days untuk aset lain
9. Verifikasi baris Waiting for Approval hasil Submit itu masuk satu pengajuan approval tipe `Borrow` per Transaction ID
10. Verifikasi ID pengajuan yang tampil adalah Transaction ID BRW itu
11. Verifikasi pengajuan tidak dipecah menurut himpunan approver atau Approval type walaupun aset di dalamnya punya Approval type `Any one`, `All`, dan satu approver
12. Verifikasi approval satu level tanpa rantai approval
13. Verifikasi baris `Projector Epson EB {runId}` berstatus `Waiting for Handover` dan dicatat Auto-approved beserta aturan dan versi setting karena Duration baris itu memenuhi Auto-approve
14. Verifikasi baris `Camera Canon EOS {runId}` berstatus `Waiting for Approval` karena Duration baris itu melebihi batas Auto-approve, sehingga Auto-approve dinilai per baris
15. Verifikasi daftar approver di-snapshot per baris saat Submit
16. Verifikasi approver tiap baris adalah pemegang Role Transaksi `Approver` pada Group aset, dan baris `Forklift Toyota {runId}` di Group turunan `Head Office Gudang {runId}` memuat `Tono Prasetyo {runId}` dari Group ancestor
17. Verifikasi plan tanpa Approval Workflow ditandai Require approval efektif OFF dan semua baris langsung `Waiting for Handover` saat Submit

### Mode Any one, All, dan satu approver
18. Approver `Rina Wijaya {runId}` mengirim keputusan Approve hanya untuk aset `Laptop Dell Latitude {runId}` tanpa memutuskan aset `Excavator Komatsu {runId}` yang juga miliknya dalam pengajuan itu
19. Verifikasi keputusan sebagian ditolak karena seluruh aset milik approver diputuskan sekaligus dalam satu Submit
20. Approver `Rina Wijaya {runId}` mengirim keputusan Reject untuk aset `Laptop Dell Latitude {runId}` tanpa Approval note
21. Verifikasi Reject ditolak dengan `Approval note must not be empty` karena Reject wajib disertai Approval note
22. Approver `Rina Wijaya {runId}` mengirim keputusan Approve untuk aset `Laptop Dell Latitude {runId}` dan `Excavator Komatsu {runId}` dalam satu Submit
23. Verifikasi aset `Laptop Dell Latitude {runId}` berstatus `Waiting for Handover` karena keputusan pertama Approve pada mode Any one
24. Verifikasi aset `Excavator Komatsu {runId}` tetap `Waiting for Approval` karena mode All butuh semua approver snapshot
25. Verifikasi aset `Laptop Dell Latitude {runId}` keluar dari Active approver `Sari Wulandari {runId}` dan tidak tercatat di Active maupun History-nya, tanpa notifikasi
26. Approver `Sari Wulandari {runId}` mengirim keputusan Reject atas aset `Laptop Dell Latitude {runId}` sesudah keputusan `Rina Wijaya {runId}` masuk lebih dulu
27. Verifikasi keputusan itu ditolak dengan `You can no longer approve this request because it has already been done by another approver.` dan tidak tersimpan
28. Approver `Sari Wulandari {runId}` mengirim keputusan Approve untuk aset `Excavator Komatsu {runId}`
29. Verifikasi aset `Excavator Komatsu {runId}` berstatus `Waiting for Handover` karena semua approver snapshot menyetujui
30. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Laptop HP ProBook {runId}` dan `Bulldozer Caterpillar {runId}`
31. Approver `Sari Wulandari {runId}` mengirim keputusan Reject dengan Approval note `Tidak sesuai kebutuhan` untuk aset `Laptop HP ProBook {runId}` lebih dulu, dan Approve untuk aset `Bulldozer Caterpillar {runId}`
32. Verifikasi aset `Laptop HP ProBook {runId}` berstatus `Rejected` karena keputusan pertama Reject pada mode Any one menolak aset itu
33. Approver `Rina Wijaya {runId}` mengirim keputusan Reject dengan Approval note `Tidak sesuai kebutuhan` untuk aset `Bulldozer Caterpillar {runId}`
34. Verifikasi aset `Bulldozer Caterpillar {runId}` langsung berstatus `Rejected` karena satu penolakan pada mode All menolak aset itu
35. Verifikasi Reject melepas Custody aset `Bulldozer Caterpillar {runId}` dan tidak memengaruhi aset lain, dan baris yang ditolak dapat diajukan ulang sebagai BRW baru

### Keputusan per aset, Bulk, dan keterlihatan pengajuan
36. Approver `Rina Wijaya {runId}` mengirim keputusan Approve atas aset `Genset Honda {runId}` yang approver-nya `Tono Prasetyo {runId}`
37. Verifikasi keputusan ditolak karena approver hanya memutuskan aset yang approver-nya dia dan belum ia putuskan
38. Approver `Rina Wijaya {runId}` mengirim Bulk Approve atas aset `Genset Honda {runId}`, `Camera Canon EOS {runId}`, dan `Forklift Toyota {runId}`
39. Verifikasi Bulk Approve hanya berlaku untuk aset terpilih milik approver itu, dan satu persetujuan berlaku untuk satu aset
40. Verifikasi pengajuan muncul di Active bagi `Tono Prasetyo {runId}` karena ia approver dari paling sedikit satu aset yang belum ia putuskan
41. Verifikasi pengajuan tidak muncul di Active bagi `Agus Salim {runId}` yang bukan approver aset mana pun di dalamnya
42. Verifikasi Group Manager `Gita Pramesti {runId}` di luar daftar snapshot tidak dapat memutuskan aset sebelum pengajuan dirutekan ulang
43. Verifikasi aset milik approver lain tampil read-only `Not your approval`
44. Verifikasi status pengajuan `Partially Approved` sesudah sebagian aset diputuskan dan `Approved` sesudah seluruh asetnya diputuskan

### Approver Reroute dan snapshot approver
45. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Mesin Bor Bosch {runId}`
46. Aktor Admin menonaktifkan Approver `Agus Salim {runId}` saat pengajuan masih menunggu
47. Verifikasi pengajuan dirutekan ke Group Manager `Gita Pramesti {runId}` dengan log node `Approval rerouted` alasan `Approver removed`
48. Verifikasi snapshot approver tidak ditulis ulang dan keputusan pertama penerima fallback final
49. Aktor Admin mengubah Approval type override Asset baris `Mesin Bor Bosch {runId}` dari Any one menjadi All saat pengajuan menunggu
50. Verifikasi aset `Mesin Bor Bosch {runId}` memakai snapshot saat Submit

### Pengajuan dibatalkan atau ditutup sistem saat Review terbuka
51. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Tablet Samsung {runId}` dan `Speaker JBL {runId}`
52. Aktor Borrow membatalkan pengajuan `Borrow` saat Review approver `Rina Wijaya {runId}` terbuka
53. Approver `Rina Wijaya {runId}` mengirim keputusan Approve atas aset `Tablet Samsung {runId}`
54. Verifikasi keputusan ditolak dengan `This borrow was canceled by [Name].` dan tidak tersimpan
55. Waktu berlalu sampai Transaction timeout pengajuan `Borrow` terlewati saat Review approver `Rina Wijaya {runId}` terbuka
56. Verifikasi keputusan `Rina Wijaya {runId}` atas aset `Speaker JBL {runId}` ditolak dengan `This borrow was canceled automatically ([Reason]).` dan tidak tersimpan

### History per pengajuan dan Extension per Submit Extend
57. Aktor Borrow mengirim Submit Extend untuk Borrower `Budi Santoso {runId}` atas aset `Monitor Dell {runId}` dan `Monitor LG UltraWide {runId}` dari dua BRW berbeda
58. Verifikasi Submit Extend itu menghasilkan satu pengajuan tipe `Extension` per BRW
59. Verifikasi satu Transaction ID dapat punya beberapa pengajuan Extension yang dibedakan Request Date
60. Verifikasi History Approvals approver `Rina Wijaya {runId}` memuat tiga entri ber-Transaction ID sama dengan Type `Borrow`, `Extension`, dan `Extension`, dibedakan Request Date dan Decided Date, tidak digabung
61. Verifikasi hanya pengajuan yang sudah diputuskan approver itu yang masuk History
62. Verifikasi keputusan baru dari History untuk pengajuan yang sudah ditutup ditolak dan keputusan tiap aset tampil sebagai hasil
63. Verifikasi progres approval aset milik approver lain hanya memuat status dan waktu keputusan, tanpa Approval Note dan Approve Duration approver lain
