---
id: TC-FA-ASSIGN-BE-221-konkurensi-idempotensi-dan-penolakan-server
title: "Konkurensi, idempotensi aksi, dan penolakan server tanpa perubahan data"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.6#r1", "§9.6#r2", "§9.6#r3", "§9.6#r4", "§9.6#r5", "§9.6#r6", "§9.6#r7", "§9.6#r8", "§9.6#r9", "§9.6#r10", "§9.6#r11", "§9.6#r12", "EB-CON-1", "EB-CON-3", "EB-EDG-1", "EB-ERR-3", "EB-ERR-4", "EC-ASG-10", "EC-ASG-47", "EC-ASG-48", "EC-ASG-85", "EC-ASG-49", "F-ASSIGN-03.k5"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§9.6#r1": 46
  "§9.6#r2": [3, 50]
  "§9.6#r3": [38, 52, 57]
  "§9.6#r4": 31
  "§9.6#r5": [56, 61]
  "§9.6#r6": 34
  "§9.6#r7": 44
  "§9.6#r8": 36
  "§9.6#r9": 25
  "§9.6#r10": 27
  "§9.6#r11": 22
  "§9.6#r12": 40
  "EB-CON-1": 42
  "EB-CON-3": [19, 48]
  "EB-EDG-1": [19, 22, 36, 48]
  "EB-ERR-3": 13
  "EB-ERR-4": [3, 19]
  "EC-ASG-10": [2, 3]
  "EC-ASG-47": [6, 9]
  "EC-ASG-48": 13
  "EC-ASG-85": 19
  "EC-ASG-49": 16
  "F-ASSIGN-03.k5": 2
---

# Konkurensi, idempotensi aksi, dan penolakan server tanpa perubahan data

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` dan `Agus Pratama {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); Approver `Mira Handayani {runId}`; Assignee Employee dan PIC ber-akun login seperti di entri data.
- Data:
  - DU-221-1: User, Aktor Assignment pertama: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-221-2: User, Aktor Assignment kedua: Nama `Agus Pratama {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-221-3: User, Approver Group: Nama `Mira Handayani {runId}`, Role `Approver`, Cakupan Group `Head Office {runId}`.
  - DU-221-4: Asset, Aset Available yang diajukan dua Aktor untuk dua Assignee hampir bersamaan: Nama `Laptop HP ProBook {runId}`, Custody `Available`, Assignee Rina `Budi Santoso {runId}`, Assignee Agus `Citra Dewi {runId}`, Group `Head Office {runId}`.
  - DU-221-5: Draft, Draft A berisi aset yang akan lebih dulu di-Submit: Assignee `Dedi Prasetyo {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Proyektor Epson EB {runId}`, Group aset 1 `Head Office {runId}`, Aset 2 `Speaker Aktif {runId}`, Group aset 2 `Head Office {runId}`.
  - DU-221-6: Draft, Draft B berisi aset yang sama dengan Draft A: Assignee `Eko Wijaya {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Proyektor Epson EB {runId}`, Group aset 1 `Head Office {runId}`, Aset 2 `Kipas Meja {runId}`, Group aset 2 `Head Office {runId}`.
  - DU-221-7: Asset, Aset di form yang terbuka lama dan diambil ASG lain sebelum Submit: Nama `Printer Canon LBP {runId}`, Custody `Available`, Assignee form Rina `Fani Rahmawati {runId}`, Assignee ASG lain `Gani Mahendra {runId}`, Group `Head Office {runId}`.
  - DU-221-8: Draft, Draft yang asetnya masuk tiga transaksi lain: Assignee `Hana Permatasari {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Mobil Toyota Avanza {runId}`, Group aset 1 `Head Office {runId}`, Aset 2 `Meja Kerja Kayu {runId}`, Group aset 2 `Head Office {runId}`, Aset 3 `Genset Cummins C {runId}`, Group aset 3 `Head Office {runId}`, Transaksi lain aset 1 `Borrow`, Transaksi lain aset 2 `Transfer`, Transaksi lain aset 3 `Disposal`.
  - DU-221-9: Assignment, ASG dengan baris Waiting for Handover yang dibatalkan Aktor lain: Assignee `Indra Kusuma {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kamera Canon EOS {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`.
  - DU-221-10: Assignment, ASG dengan baris untuk Complete Handover berulang: Assignee `Gita Lestari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Monitor Dell P2422 {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`.
  - DU-221-11: Assignment, ASG dengan baris untuk Request Confirmation, Cancel Request, dan Confirm berulang: Assignee `Joko Susilo {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Mouse Logitech {runId}`, Baris 2 `Keyboard Logitech {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`.
  - DU-221-12: Assignment, ASG dengan baris Assigned untuk Unassign dan Cancel berulang: Assignee `Kiki Amelia {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kamera Sony Alpha {runId}`, Status baris `Assigned`.
  - DU-221-13: Assignment, ASG dengan baris Waiting for Approval untuk keputusan berulang: Assignee `Lina Hartati {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Speaker JBL {runId}`, Status baris `Waiting for Approval`, Approver `Mira Handayani {runId}`.
  - DU-221-14: Assignment, ASG dengan baris Waiting for Handover untuk Remind Assignee berulang dan Cancel berulang: Assignee `Mario Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Printer HP LaserJet {runId}`, Baris 2 `Scanner Fujitsu {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`.
  - DU-221-15: Assignment, ASG Division untuk Change PIC berulang dan bersamaan: Assignee `Operasional {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Perkins {runId}`, Status baris `Waiting for Handover`, PIC `Indah Permata {runId}`, PIC dari Rina `Joko Susilo {runId}`, PIC dari Agus `Wati Susanti {runId}`.
  - DU-221-16: Draft, Draft untuk Save Draft tanpa perubahan dan Delete berulang: Assignee `Novi Andriani {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Rak Gudang Besi {runId}`, Group aset 1 `Head Office {runId}`.
  - DU-221-17: Asset, Aset Available untuk Submit dengan kunci idempotensi yang sama: Nama `Kursi Staff {runId}`, Custody `Available`, Assignee `Oscar Pratama {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Require approval `ON`, Approver `Mira Handayani {runId}`.
  - DU-221-18: Assignment, ASG dengan baris Waiting for Approval untuk Reject berulang: Assignee `Pandu Wijaya {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kulkas Polytron {runId}`, Status baris `Waiting for Approval`, Approver `Mira Handayani {runId}`.
  - DU-221-19: Assignment, ASG dengan baris untuk Confirm on This Device pada sesi baru: Assignee `Qori Ramadhan {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Webcam Logitech {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`.
  - DU-221-20: Assignment, ASG dengan dua baris untuk Confirm on This Device berulang: Assignee `Ratna Wulandari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Mesin Cuci LG {runId}`, Baris 2 `Kulkas Samsung {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`.
- Kondisi:
  - Jendela konfirmasi Handover bernilai `15 menit`.

## Test Steps

### Dua Submit bersamaan atas aset yang sama
1. Rina menekan `[Submit]` untuk aset `Laptop HP ProBook {runId}` bagi `Budi Santoso {runId}` dan Agus menekan `[Submit]` untuk aset yang sama bagi `Citra Dewi {runId}` pada DU-221-4 hampir bersamaan
2. Verifikasi tepat satu Submit yang dikomit dan aset `Laptop HP ProBook {runId}` berada di tepat satu ASG
3. Verifikasi Submit yang kedua ditolak dengan pesan `This asset is already in [Transaction ID].` dan tidak ada data berubah oleh penolakan itu

### Aset Draft A di-Submit lebih dulu dari Draft B
4. Rina menekan `[Submit]` pada Draft A untuk `Dedi Prasetyo {runId}` pada DU-221-5
5. Rina membuka Draft B untuk `Eko Wijaya {runId}` pada DU-221-6
6. Verifikasi baris `Proyektor Epson EB {runId}` di Draft B ditandai tidak layak dengan `Remove from List` dan baris lain tetap ada
7. Rina mengeluarkan baris `Proyektor Epson EB {runId}` dari Draft B
8. Rina menekan `[Submit]` pada Draft B
9. Verifikasi baris lain `Kipas Meja {runId}` di Draft B berhasil diajukan setelah baris yang bermasalah dikeluarkan

### Form terbuka lama dan aset diambil ASG lain
10. Rina membuka form Assignment Request untuk `Fani Rahmawati {runId}` berisi `Printer Canon LBP {runId}` pada DU-221-7
11. Agus mengajukan `Printer Canon LBP {runId}` untuk `Gani Mahendra {runId}` lebih dulu
12. Rina menekan `[Submit]` pada form yang terbuka lama
13. Verifikasi kelayakan dicek ulang saat Submit, baris `Printer Canon LBP {runId}` ditandai, dan Submit ditolak sampai baris dikeluarkan

### Aset di Draft masuk transaksi lain
14. Aset `Mobil Toyota Avanza {runId}` masuk `Borrow`, aset `Meja Kerja Kayu {runId}` masuk `Transfer`, dan aset `Genset Cummins C {runId}` masuk `Disposal` pada DU-221-8 sebelum Draft di-Submit
15. Rina menekan `[Submit]` pada Draft `Hana Permatasari {runId}`
16. Verifikasi baris `Mobil Toyota Avanza {runId}`, `Meja Kerja Kayu {runId}`, dan `Genset Cummins C {runId}` masing-masing ditandai tidak layak dan Submit diblokir sampai ketiga baris dikeluarkan

### Aksi atas baris yang sudah dibatalkan Aktor lain
17. Agus membatalkan baris `Kamera Canon EOS {runId}` pada DU-221-9
18. Rina mengirim Cancel Assignment, Handover, dan Remind Assignee atas baris `Kamera Canon EOS {runId}` yang sudah dibatalkan
19. Verifikasi ketiga aksi ditolak server dan baris `Kamera Canon EOS {runId}` tidak berubah oleh percobaan itu

### Idempotensi Handover, sesi, dan Confirm
20. Rina memverifikasi tag baris `Monitor Dell P2422 {runId}` pada DU-221-10
21. Rina menekan `[Complete Handover]` untuk baris `Monitor Dell P2422 {runId}` dua kali
22. Verifikasi baris `Monitor Dell P2422 {runId}` berstatus `Assigned` dan pengulangan pada baris yang sudah `Assigned` diabaikan
23. Rina memverifikasi tag baris `Mouse Logitech {runId}` pada DU-221-11
24. Rina menekan `[Request Confirmation]` dua kali untuk ASG yang sama
25. Verifikasi pengulangan memakai satu sesi aktif yang sama dan sesi beserta Task terbentuk atomik
26. Rina menekan `[Cancel Request]` dua kali
27. Verifikasi sesi yang sudah batal tidak menambah log dan semua aset sesi tetap `Waiting for Handover`
28. Rina memverifikasi tag baris `Keyboard Logitech {runId}`
29. Rina menekan `[Request Confirmation]` untuk baris `Keyboard Logitech {runId}`
30. Assignee `Joko Susilo {runId}` menekan Confirm dua kali pada sesi yang sama
31. Verifikasi satu handover terjadi dan semua baris tercentang `Assigned` secara atomik beserta Custody

### Idempotensi Unassign dan Cancel
32. Rina memverifikasi tag baris `Kamera Sony Alpha {runId}` pada DU-221-12
33. Rina menekan `[Submit]` pada halaman Unassign dua kali untuk Assignee `Kiki Amelia {runId}`
34. Verifikasi baris `Kamera Sony Alpha {runId}` berstatus `Unassigned` sekali dan Custody `Available` secara atomik per ASG
35. Rina membatalkan baris `Scanner Fujitsu {runId}` pada DU-221-14 dua kali
36. Verifikasi baris `Scanner Fujitsu {runId}` berstatus `Canceled` sekali beserta Custody `Available`

### Keputusan approval dan Remind Assignee berulang
37. Mira menyetujui baris `Speaker JBL {runId}` pada DU-221-13 dua kali
38. Verifikasi keputusan per approver per aset tercatat sekali dan baris berstatus `Waiting for Handover` dengan Custody `In Assignment Process` serta notifikasi keputusan terkirim sekali secara atomik
39. Rina mengirim Remind Assignee untuk baris `Printer HP LaserJet {runId}` pada DU-221-14 dua kali
40. Verifikasi tiap panggilan mengirim ulang notifikasi `assignment_ready_handover` tanpa mengubah status baris dan tanpa node log

### Change PIC berulang dan bersamaan
41. Rina mengganti PIC ASG DU-221-15 menjadi `Joko Susilo {runId}` dan Agus mengganti PIC ASG yang sama menjadi `Wati Susanti {runId}` hampir bersamaan
42. Verifikasi kedua penggantian PIC berhasil tanpa dialog konflik dan PIC akhir berasal dari penyimpanan terakhir
43. Rina mengganti PIC ASG DU-221-15 menjadi PIC akhir yang sama sekali lagi
44. Verifikasi pengulangan tidak mengubah PIC

### Save Draft, Delete Draft, dan Submit idempoten
45. Rina menekan `[Save Draft]` pada Draft `Novi Andriani {runId}` pada DU-221-16 tanpa perubahan
46. Verifikasi Save berhasil tanpa menaikkan versi dan tanpa log baru
47. Rina dan Agus menghapus Draft `Novi Andriani {runId}` hampir bersamaan
48. Verifikasi Draft terhapus sekali dan penghapusan yang sudah terhapus adalah no-op tanpa error
49. Rina menekan `[Submit]` untuk aset `Kursi Staff {runId}` pada DU-221-17 dua kali dengan kunci idempotensi yang sama
50. Verifikasi hanya satu ASG terbentuk dan baris, Custody, snapshot, serta pengajuan approval tercatat atomik

### Reject berulang
51. Mira menolak baris `Kulkas Polytron {runId}` pada DU-221-18 dua kali
52. Verifikasi keputusan per approver per aset tercatat sekali, baris `Kulkas Polytron {runId}` berstatus `Rejected`, dan Custody `Available` secara atomik

### Confirm on This Device berulang pada sesi baru
53. Rina memverifikasi tag baris `Webcam Logitech {runId}` pada DU-221-19
54. Rina menekan `[Request Confirmation]` untuk baris `Webcam Logitech {runId}`
55. Rina memakai `Confirm on This Device` dua kali pada sesi baru itu
56. Verifikasi baris `Webcam Logitech {runId}` berstatus `Assigned` sekali dan satu handover tercatat di Assignment Log, Transaction log aset, dan Transaction admin log

### Notifikasi keputusan pada Reject berulang terkirim sekali
57. Verifikasi notifikasi keputusan atas penolakan baris `Kulkas Polytron {runId}` pada DU-221-18 terkirim sekali walau Mira menolak dua kali

### Confirm on This Device berulang pada sesi dengan dua baris
58. Rina memverifikasi tag baris `Mesin Cuci LG {runId}` dan `Kulkas Samsung {runId}` pada DU-221-20
59. Rina menekan `[Request Confirmation]`
60. Rina memakai `Confirm on This Device` dua kali pada sesi itu dengan pernyataan dicentang dan kedua aset dicentang
61. Verifikasi kedua baris `Mesin Cuci LG {runId}` dan `Kulkas Samsung {runId}` berstatus `Assigned` sekali dan Custody tiap aset `Assigned` secara atomik
