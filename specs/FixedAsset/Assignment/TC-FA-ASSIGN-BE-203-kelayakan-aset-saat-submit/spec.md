---
id: TC-FA-ASSIGN-BE-203-kelayakan-aset-saat-submit
title: "Kelayakan aset: status, tag, Allow Assign, dan Allowed assignee"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["V-ASG-01", "V-ASG-06", "V-ASG-08", "V-ASG-30", "V-ASG-31", "V-ASG-32", "V-ASG-33", "V-ASG-34", "V-ASG-35", "V-ASG-36", "F-ASSIGN-03.k1", "EC-ASG-94", "§9.2#b4", "§9.2#b5", "§9.2#b6", "§9.2#b7", "§9.2#b8", "§9.2#p19", "§9.4.3#b3", "§10#r9", "ASSIGN-LOGIC-03a", "ASSIGN-LOGIC-03b", "ASSIGN-LOGIC-03c", "ASSIGN-LOGIC-03e"]
smoke: []
dependsOn: []
trace:
  "V-ASG-01": [16, 17]
  "V-ASG-06": [23, 24, 25]
  "V-ASG-08": [26, 27, 29, 35, 45]
  "V-ASG-30": 21
  "V-ASG-31": [16, 17, 18, 22]
  "V-ASG-32": 19
  "V-ASG-33": 20
  "V-ASG-34": [23, 24]
  "V-ASG-35": 25
  "V-ASG-36": [26, 27, 45]
  "F-ASSIGN-03.k1": [15, 29, 30, 41, 56]
  "EC-ASG-94": 38
  "§9.2#b4": [15, 28, 29]
  "§9.2#b5": [27, 47, 49, 54, 55, 65, 66]
  "§9.2#b6": [55, 58]
  "§9.2#b7": [54, 58, 68, 70, 72]
  "§9.2#b8": [59, 60, 75, 77, 79, 81, 85, 87]
  "§9.2#p19": [54, 55, 58, 63]
  "§9.4.3#b3": 33
  "§10#r9": 31
  "ASSIGN-LOGIC-03a": [16, 22, 23, 25]
  "ASSIGN-LOGIC-03b": [33, 38]
  "ASSIGN-LOGIC-03c": [15, 28]
  "ASSIGN-LOGIC-03e": [29, 30, 41, 42, 43]
owner: BE
---

# Kelayakan aset: status, tag, Allow Assign, dan Allowed assignee

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Grup Kelayakan {runId}` dan `Grup Kelayakan B {runId}`, sebagai pengaju dan pemberi handover. Pengelola aset menghapus aset, melaporkan Condition, mengganti status TAG, dan melepas aset lewat Disposal pada langkah yang menyebutnya. Aktor pemicu lain: Pengelola Transaction Settings (mengubah nilai setting) dan Approver `Agus Pratama {runId}` (memutuskan pengajuan).
- Data:
  - DU-203-1: Category CN beserta Asset Name, Category `Kategori Normal {runId}`, Asset Name `Nama Normal {runId}`, Override Category Max assets per assignee `0`.
  - DU-203-2: Category CD beserta Asset Name, Category `Kategori Izin Deny {runId}`, Asset Name `Nama Izin Deny {runId}`, Override Category Allow Assign `Allow`, Override Category Allowed assignee Employee `ON`, Override Category Max assets per assignee `0`.
  - DU-203-3: Category CE beserta Asset Name, Category `Kategori Employee OFF {runId}`, Asset Name `Nama Employee OFF {runId}`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `ON`, Override Category Max assets per assignee `0`.
  - DU-203-4: Category CV beserta Asset Name, Category `Kategori Division OFF {runId}`, Asset Name `Nama Division OFF {runId}`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `OFF`, Override Category Max assets per assignee `0`.
  - DU-203-5: Category CO beserta Asset Name, Category `Kategori Assignee OFF {runId}`, Asset Name `Nama Assignee OFF {runId}`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `OFF`, Override Category Max assets per assignee `0`.
  - DU-203-6: Category CL beserta Asset Name, Category `Kategori Laptop {runId}`, Asset Name `Nama Laptop {runId}`, Override Category Max assets per assignee `2`, Override Category Allowed assignee Division `ON`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`.
  - DU-203-7: Category CP beserta Asset Name, Category `Kategori Projector {runId}`, Asset Name `Nama Projector {runId}`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`.
  - DU-203-8: Asset Name dengan override Allow Assign, Asset Name `Nama Deny {runId}`, Category `Kategori Normal {runId}`, Override Asset Name Allow Assign `Allow`.
  - DU-203-9: Asset Name dengan override Allow Assign pada Category yang mengizinkan Allow Assign, Asset Name `Nama Deny Izin {runId}`, Category `Kategori Izin Deny {runId}`, Override Asset Name Allow Assign `Allow`.
  - DU-203-10: Assignee Employee dengan akun login, Name `Budi Santoso {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`.
  - DU-203-11: Assignee Employee kedua dengan akun login, Name `Tono Hartono {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`.
  - DU-203-12: Assignee Employee untuk pemeriksaan batas, Name `Sari Dewi {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`.
  - DU-203-13: Karyawan PIC yang juga Assignee Employee, Name `Joko Prasetyo {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`, Division `Gudang {runId}`.
  - DU-203-14: Karyawan tanpa akun login, Name `Dewi Tanpa Akun {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Tidak ada`.
  - DU-203-15: Pemegang hak Manage asset & TAG pada Group aset, Name `Lina Marlina {runId}`, Capability `Manage asset & TAG`, Group `Grup Kelayakan {runId}`, Status `Aktif`.
  - DU-203-16: Division Assignee dengan PIC, Division `Gudang {runId}`, PIC `Joko Prasetyo {runId}`.
  - DU-203-17: Aset Aset Layak Satu, Name `Aset Layak Satu {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Normal {runId}`, Asset Name `Nama Normal {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-18: Aset Aset Layak Dua, Name `Aset Layak Dua {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Normal {runId}`, Asset Name `Nama Normal {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-19: Aset Aset Rusak, Name `Aset Rusak {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Normal {runId}`, Asset Name `Nama Normal {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`, Override Asset Allow Assign `Allow`.
  - DU-203-20: Aset Aset TAG Ganti, Name `Aset TAG Ganti {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Normal {runId}`, Asset Name `Nama Normal {runId}`, TAG `Terpasang`, Custody `Available`, Condition `Normal`, Override Asset Allow Assign `Allow`.
  - DU-203-21: Aset Aset Transaksi Lain, Name `Aset Transaksi Lain {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Normal {runId}`, Asset Name `Nama Normal {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-22: Aset Aset Dihapus, Name `Aset Dihapus {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Normal {runId}`, Asset Name `Nama Normal {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-23: Aset Aset Urutan Satu, Name `Aset Urutan Satu {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Normal {runId}`, Asset Name `Nama Deny {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-24: Aset Aset Urutan Dua, Name `Aset Urutan Dua {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Izin Deny {runId}`, Asset Name `Nama Deny Izin {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-25: Aset Aset Izin dan Assignee, Name `Aset Izin dan Assignee {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Izin Deny {runId}`, Asset Name `Nama Izin Deny {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-26: Aset Aset Tanpa Employee, Name `Aset Tanpa Employee {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Employee OFF {runId}`, Asset Name `Nama Employee OFF {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-27: Aset Aset Tanpa Assignee, Name `Aset Tanpa Assignee {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Assignee OFF {runId}`, Asset Name `Nama Assignee OFF {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-28: Aset Aset Tanpa Division, Name `Aset Tanpa Division {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Division OFF {runId}`, Asset Name `Nama Division OFF {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-29: Aset Aset Laptop 1, Name `Aset Laptop 1 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Laptop {runId}`, Asset Name `Nama Laptop {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-30: Aset Aset Laptop 2, Name `Aset Laptop 2 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Laptop {runId}`, Asset Name `Nama Laptop {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-31: Aset Aset Laptop 3, Name `Aset Laptop 3 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Laptop {runId}`, Asset Name `Nama Laptop {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-32: Aset Aset Laptop 4, Name `Aset Laptop 4 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Laptop {runId}`, Asset Name `Nama Laptop {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-33: Aset Aset Laptop 5, Name `Aset Laptop 5 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Laptop {runId}`, Asset Name `Nama Laptop {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-34: Aset Aset Laptop 6, Name `Aset Laptop 6 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Laptop {runId}`, Asset Name `Nama Laptop {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-35: Aset Aset Laptop 7, Name `Aset Laptop 7 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Laptop {runId}`, Asset Name `Nama Laptop {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-36: Aset Aset Projector 1, Name `Aset Projector 1 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Projector {runId}`, Asset Name `Nama Projector {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-37: Aset Aset Projector 2, Name `Aset Projector 2 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Projector {runId}`, Asset Name `Nama Projector {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-38: Aset Aset Projector 3, Name `Aset Projector 3 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Projector {runId}`, Asset Name `Nama Projector {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-39: Input pengajuan untuk Assignee Employee, Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Note `Penugasan uji kelayakan {runId}`, Purpose `Daily work`.
  - DU-203-40: Group kedua untuk pengajuan multi-Group, Group `Grup Kelayakan B {runId}`.
  - DU-203-41: Assignee Employee untuk pengajuan multi-Group dan override di bawah Category, Name `Maya Anggraini {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`.
  - DU-203-42: Assignee Employee untuk pemeriksaan baris aktif, Name `Hendra Kusuma {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`.
  - DU-203-43: Approver pada Group aset, Name `Agus Pratama {runId}`, Role Transaksi `Approver`, Group `Grup Kelayakan {runId}`, Status `Aktif`.
  - DU-203-44: Category CM beserta Asset Name tanpa override, Category `Kategori Monitor {runId}`, Asset Name `Nama Monitor Standar {runId}`, tanpa override Max assets per assignee.
  - DU-203-45: Asset Name dengan override Max assets per assignee, Asset Name `Nama Monitor Terbatas {runId}`, Category `Kategori Monitor {runId}`, Override Asset Name Max assets per assignee `2`.
  - DU-203-46: Category CK dengan approval, Category `Kategori Kamera {runId}`, Asset Name `Nama Kamera {runId}`, Override Category Max assets per assignee `2`, Override Category Require approval `ON`, Override Category Approval type `Any one`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Photo at end `OFF`.
  - DU-203-47: Aset Aset Hilang, Name `Aset Hilang {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Normal {runId}`, Asset Name `Nama Normal {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-48: Aset Aset Disposed, Name `Aset Disposed {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Normal {runId}`, Asset Name `Nama Normal {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`, Lifecycle `Active`.
  - DU-203-49: Aset Aset Projector 4, Name `Aset Projector 4 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Projector {runId}`, Asset Name `Nama Projector {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-50: Aset Aset Projector 5, Name `Aset Projector 5 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Projector {runId}`, Asset Name `Nama Projector {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-51: Aset Aset Projector 6, Name `Aset Projector 6 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Projector {runId}`, Asset Name `Nama Projector {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-52: Aset Aset Projector 7, Name `Aset Projector 7 {runId}`, Group `Grup Kelayakan B {runId}`, Category `Kategori Projector {runId}`, Asset Name `Nama Projector {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-53: Aset Aset Projector 8, Name `Aset Projector 8 {runId}`, Group `Grup Kelayakan B {runId}`, Category `Kategori Projector {runId}`, Asset Name `Nama Projector {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-54: Aset Aset Projector 9, Name `Aset Projector 9 {runId}`, Group `Grup Kelayakan B {runId}`, Category `Kategori Projector {runId}`, Asset Name `Nama Projector {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-55: Aset Aset Monitor Standar 1, Name `Aset Monitor Standar 1 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Monitor {runId}`, Asset Name `Nama Monitor Standar {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-56: Aset Aset Monitor Terbatas 1, Name `Aset Monitor Terbatas 1 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Monitor {runId}`, Asset Name `Nama Monitor Terbatas {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-57: Aset Aset Monitor Terbatas 2, Name `Aset Monitor Terbatas 2 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Monitor {runId}`, Asset Name `Nama Monitor Terbatas {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-58: Aset Aset Kamera 1, Name `Aset Kamera 1 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Kamera {runId}`, Asset Name `Nama Kamera {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-59: Aset Aset Kamera 2, Name `Aset Kamera 2 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Kamera {runId}`, Asset Name `Nama Kamera {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-60: Aset Aset Kamera 3, Name `Aset Kamera 3 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Kamera {runId}`, Asset Name `Nama Kamera {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-61: Aset Aset Kamera 4, Name `Aset Kamera 4 {runId}`, Group `Grup Kelayakan {runId}`, Category `Kategori Kamera {runId}`, Asset Name `Nama Kamera {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-203-62: Approval Note Reject, Approval Note `Aset sedang dipakai tim lain {runId}`.
  - DU-203-63: Keadaan sesudah berubah setelah Draft disimpan: Condition `Aset Rusak {runId}` `Damaged`, TAG `Aset TAG Ganti {runId}` `Perlu diganti`, Condition `Aset Hilang {runId}` `Missing`, Lifecycle `Aset Disposed {runId}` `Disposed`, Condition `Aset Urutan Satu {runId}` `Damaged`, Override Asset Name `Nama Deny {runId}` Allow Assign `Deny`, Override Asset Name `Nama Deny Izin {runId}` Allow Assign `Deny`, Category `Kategori Izin Deny {runId}` Allow Assign `Deny` dan Allowed assignee Employee `OFF`, Category `Kategori Employee OFF {runId}` Allowed assignee Employee `OFF`, Category `Kategori Assignee OFF {runId}` Allowed assignee Employee `OFF`.
- Kondisi:
  - Level Feature Suite Assignment pada plan adalah `Full`.
  - Company default: Require approval bernilai `OFF`, Allow Assign bernilai `Allow`, Allowed assignee Employee bernilai `ON`, dan Max assets per assignee bernilai `5`.
  - Setiap aset berada di Custody `Available` kecuali yang disebut lain di Data, dan tidak berada di ASG aktif maupun Draft mana pun.

## Test Steps

### Semua baris bermasalah dievaluasi sekaligus pada Submit
1. Aktor Assignment menyimpan Draft untuk Assignee `Budi Santoso {runId}` dengan Note `Penugasan uji kelayakan {runId}` dan Purpose `Daily work`, memuat aset `Aset Layak Satu {runId}`, `Aset Rusak {runId}`, `Aset TAG Ganti {runId}`, `Aset Hilang {runId}`, `Aset Disposed {runId}`, `Aset Transaksi Lain {runId}`, `Aset Urutan Satu {runId}`, `Aset Urutan Dua {runId}`, `Aset Izin dan Assignee {runId}`, `Aset Tanpa Employee {runId}`, `Aset Tanpa Assignee {runId}`, `Aset Dihapus {runId}`, yang semuanya layak pada saat dimasukkan
2. Aktor Assignment mengajukan Submit untuk Assignee `Tono Hartono {runId}` dengan aset `Aset Transaksi Lain {runId}`
3. Pengelola aset menghapus aset `Aset Dihapus {runId}`
4. Pengelola aset melaporkan Condition aset `Aset Rusak {runId}` menjadi `Damaged` setelah aset masuk Draft
5. Pengelola aset menandai TAG aset `Aset TAG Ganti {runId}` menjadi `Perlu diganti` setelah aset masuk Draft
6. Pengelola aset melaporkan Condition aset `Aset Hilang {runId}` menjadi `Missing` setelah aset masuk Draft
7. Pengelola aset melepas aset `Aset Disposed {runId}` lewat Disposal sehingga Lifecycle-nya menjadi `Disposed` setelah aset masuk Draft
8. Pengelola aset melaporkan Condition aset `Aset Urutan Satu {runId}` menjadi `Damaged` setelah aset masuk Draft
9. Pengelola Transaction Settings mengubah override Asset Name `Nama Deny {runId}`: Allow Assign dari `Allow` menjadi `Deny`
10. Pengelola Transaction Settings mengubah override Asset Name `Nama Deny Izin {runId}`: Allow Assign dari `Allow` menjadi `Deny`
11. Pengelola Transaction Settings mengubah Category `Kategori Izin Deny {runId}`: Allow Assign dari `Allow` menjadi `Deny` dan Allowed assignee Employee dari `ON` menjadi `OFF`
12. Pengelola Transaction Settings mengubah Category `Kategori Employee OFF {runId}`: Allowed assignee Employee dari `ON` menjadi `OFF`
13. Pengelola Transaction Settings mengubah Category `Kategori Assignee OFF {runId}`: Allowed assignee Employee dari `ON` menjadi `OFF`
14. Aktor Assignment mengajukan Submit atas Draft tersebut
15. Verifikasi Submit ditolak seluruhnya dan semua baris bermasalah dilaporkan sekaligus dalam satu hasil, bukan hanya baris pertama yang gagal
16. Verifikasi baris `Aset Rusak {runId}` ditolak dengan pesan `This asset is Damaged and can't be assigned.`, karena Custody `Available`, Condition `Normal`, tag lengkap, dan tanpa Activity Lock adalah syarat status aset
17. Verifikasi baris `Aset Hilang {runId}` ditolak dengan pesan `This asset is Missing and can't be assigned.`
18. Verifikasi baris `Aset Disposed {runId}` ditolak dengan pesan `This asset is Disposed and can't be assigned.`
19. Verifikasi baris `Aset TAG Ganti {runId}` ditolak dengan pesan `This asset can't be assigned until its TAG is replaced.`
20. Verifikasi baris `Aset Transaksi Lain {runId}` ditolak dengan pesan `This asset is already in another transaction.`
21. Verifikasi baris `Aset Dihapus {runId}` ditolak dengan pesan `This asset has been deleted.`
22. Verifikasi baris `Aset Urutan Satu {runId}` ditolak dengan pesan `This asset is Damaged and can't be assigned.`, karena aturan tetap dievaluasi lebih dulu daripada Deny pada override
23. Verifikasi baris `Aset Urutan Dua {runId}` ditolak dengan pesan `Can't be assigned: this asset is not available for assignment. Contact [Name] (Manage asset & TAG).`, karena Deny pada override dievaluasi lebih dulu daripada Allow Assign
24. Verifikasi pesan baris `Aset Urutan Dua {runId}` menyebut [Name] pemegang hak Manage asset & TAG pada Group aset, yaitu `Lina Marlina {runId}`
25. Verifikasi baris `Aset Izin dan Assignee {runId}` ditolak dengan pesan `Assigning isn't allowed for [Category].` dengan Category `Kategori Izin Deny {runId}`, karena Allow Assign dievaluasi lebih dulu daripada Allowed assignee
26. Verifikasi baris `Aset Tanpa Employee {runId}` ditolak dengan pesan `This asset can't be assigned to an employee.`
27. Verifikasi baris `Aset Tanpa Assignee {runId}` ditolak dengan pesan `This asset can't be assigned to an employee or a division.`
28. Verifikasi setiap baris dievaluasi dengan aturan efektif asetnya sendiri sehingga baris `Aset Layak Satu {runId}` lolos evaluasi, sedangkan baris lain gagal karena sebab yang berbeda
29. Verifikasi baris `Aset Layak Satu {runId}` yang layak tidak diproses karena baris lain bermasalah: tidak ada ASG yang dibuat dan Custody aset tetap `Available`
30. Verifikasi tidak ada entri Assignment Log baru yang tercatat untuk aset `Aset Layak Satu {runId}`
31. Verifikasi aset `Aset Rusak {runId}` dan `Aset TAG Ganti {runId}` tetap ditolak walau override Asset Allow Assign bernilai `Allow`, karena aturan tetap sistem tidak dapat dimatikan

### Draft yang asetnya tidak layak tetap tersimpan dan dievaluasi ulang
32. Aktor Assignment membuka kembali Draft tersebut
33. Verifikasi baris `Aset Rusak {runId}`, `Aset TAG Ganti {runId}`, dan `Aset Transaksi Lain {runId}` tetap ada di Draft dan ditandai tidak layak, karena kelayakan dievaluasi ulang saat Draft dibuka dan tidak ada baris yang dihapus diam-diam
34. Aktor Assignment mengganti Assignee Draft tersebut menjadi Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}`
35. Verifikasi baris `Aset Tanpa Employee {runId}` tidak lagi ditolak oleh Allowed assignee, karena kelayakan dinilai ulang saat Assignee diganti dan tipe Assignee yang diizinkan aset itu terpenuhi
36. Aktor Assignment mengganti Assignee Draft tersebut kembali menjadi `Budi Santoso {runId}`

### Submit langsung ke server dievaluasi identik
37. Aktor Assignment mengirim Submit langsung ke server tanpa melalui form untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Rusak {runId}`
38. Verifikasi Submit ditolak dengan pesan `This asset is Damaged and can't be assigned.` dan tidak ada ASG yang dibuat, identik dengan evaluasi lewat form

### Baris layak diproses setelah aset bermasalah dikeluarkan
39. Aktor Assignment mengeluarkan semua aset bermasalah dari Draft sehingga Draft hanya memuat aset `Aset Layak Satu {runId}`
40. Aktor Assignment menambahkan aset `Aset Layak Dua {runId}` ke Draft dan mengajukan Submit atas Draft tersebut
41. Verifikasi terbentuk ASG untuk Assignee `Budi Santoso {runId}` dengan satu baris untuk aset `Aset Layak Satu {runId}` dan satu baris untuk aset `Aset Layak Dua {runId}`
42. Verifikasi Custody aset `Aset Layak Satu {runId}` dan `Aset Layak Dua {runId}` berubah menjadi `In Assignment Process`
43. Verifikasi Assignment Log memuat node `Requested` untuk aset `Aset Layak Satu {runId}`

### Allowed assignee Division dan pemeriksaan Assignee
44. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Tanpa Division {runId}`
45. Verifikasi Submit ditolak dengan pesan `This asset can't be assigned to a division.`
46. Aktor Assignment mengajukan Submit untuk Assignee `Dewi Tanpa Akun {runId}` dengan aset `Aset Tanpa Division {runId}`
47. Verifikasi Submit ditolak dengan pesan `[Name] has no login account. Only employees who can sign in can be assignees.` untuk karyawan tanpa akun login
48. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` tanpa memilih PIC dengan aset `Aset Laptop 7 {runId}`
49. Verifikasi Submit ditolak dengan pesan `You must pick a PIC`

### Max assets per assignee dihitung per nilai efektif tiap baris
50. Aktor Assignment mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Aset Laptop 1 {runId}`, `Aset Projector 1 {runId}`, dan `Aset Projector 2 {runId}`
51. Aktor Assignment menyelesaikan handover aset `Aset Projector 1 {runId}` tanpa konfirmasi Assignee
52. Aktor Assignment menyimpan Draft untuk Assignee `Sari Dewi {runId}` dengan aset `Aset Laptop 4 {runId}` dan Purpose `Daily work`
53. Aktor Assignment mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Aset Laptop 2 {runId}`, `Aset Laptop 3 {runId}`, dan `Aset Projector 3 {runId}`
54. Verifikasi baris `Aset Laptop 2 {runId}` dan `Aset Laptop 3 {runId}` ditolak dengan pesan `[Assignee] can hold up to 2 assets at a time.` dengan Assignee `Sari Dewi {runId}`, karena nilai efektif Category 2 dibandingkan dengan 1 baris aktif di Category itu ditambah 2 baris baru
55. Verifikasi baris `Aset Projector 3 {runId}` ditolak dengan pesan `[Assignee] can hold up to 5 assets at a time.` dengan Assignee `Sari Dewi {runId}`, karena nilai efektif Company default 5 dibandingkan dengan 3 baris aktif di semua Category ditambah 3 baris baru dalam pengajuan
56. Verifikasi tidak ada ASG yang dibuat dari pengajuan tersebut
57. Aktor Assignment mengajukan Submit untuk Assignee `Sari Dewi {runId}` dengan aset `Aset Laptop 2 {runId}` dan `Aset Projector 3 {runId}`
58. Verifikasi baris `Aset Laptop 2 {runId}` dan `Aset Projector 3 {runId}` lolos dan berstatus `Waiting for Handover`, karena nilai Category 2 tidak dijumlahkan dengan Company default 5
59. Verifikasi baris aktif Sari dihitung dari baris `Waiting for Approval`, `Waiting for Handover`, dan `Assigned` (baris `Aset Projector 1 {runId}` yang `Assigned` ikut dihitung), sedangkan Draft aset `Aset Laptop 4 {runId}` tidak dihitung
60. Verifikasi pengajuan yang lolos tetap sah karena Draft yang memuat aset `Aset Laptop 4 {runId}` tidak menambah jumlah baris aktif
61. Aktor Assignment mengajukan Submit untuk Assignee `Joko Prasetyo {runId}` dengan aset `Aset Laptop 5 {runId}` dan `Aset Laptop 6 {runId}`
62. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Laptop 7 {runId}`
63. Verifikasi baris `Aset Laptop 7 {runId}` lolos dan berstatus `Waiting for Handover`, karena batas Max assets per assignee dibandingkan dengan Assignee Division, bukan dengan PIC yang sudah memegang 2 baris aktif

### Max assets per assignee dihitung atas seluruh pengajuan multi-Group
64. Aktor Assignment mengajukan Submit untuk Assignee `Maya Anggraini {runId}` dengan aset `Aset Projector 4 {runId}`, `Aset Projector 5 {runId}`, dan `Aset Projector 6 {runId}` dari Group `Grup Kelayakan {runId}`, serta `Aset Projector 7 {runId}`, `Aset Projector 8 {runId}`, dan `Aset Projector 9 {runId}` dari Group `Grup Kelayakan B {runId}`
65. Verifikasi seluruh aset pengajuan ditolak dengan pesan `[Assignee] can hold up to 5 assets at a time.` dengan Assignee `Maya Anggraini {runId}`, karena nilai efektif Company default 5 dibandingkan dengan jumlah seluruh pengajuan (6 aset), walau tiap Group asal hanya memuat 3 aset
66. Verifikasi tidak ada ASG yang dibuat untuk Group `Grup Kelayakan {runId}` maupun `Grup Kelayakan B {runId}`, dan Custody keenam aset tetap `Available`

### Max assets per assignee dari override di bawah Category dihitung per Category
67. Aktor Assignment mengajukan Submit untuk Assignee `Maya Anggraini {runId}` dengan aset `Aset Monitor Standar 1 {runId}`
68. Verifikasi baris `Aset Monitor Standar 1 {runId}` berstatus `Waiting for Handover`
69. Aktor Assignment mengajukan Submit untuk Assignee `Maya Anggraini {runId}` dengan aset `Aset Monitor Terbatas 1 {runId}` dan `Aset Monitor Terbatas 2 {runId}`
70. Verifikasi kedua aset ditolak dengan pesan `[Assignee] can hold up to 2 assets at a time.` dengan Assignee `Maya Anggraini {runId}`, karena nilai efektif `2` dari override Asset Name `Nama Monitor Terbatas {runId}` dibandingkan dengan seluruh baris aktif Assignee di Category `Kategori Monitor {runId}` (1 baris aktif ditambah 2 baris baru), bukan hanya dengan baris di Asset Name itu
71. Aktor Assignment mengajukan Submit untuk Assignee `Maya Anggraini {runId}` dengan aset `Aset Monitor Terbatas 1 {runId}`
72. Verifikasi baris `Aset Monitor Terbatas 1 {runId}` lolos dan berstatus `Waiting for Handover`, karena 1 baris aktif di Category ditambah 1 baris baru sama dengan batas `2`

### Baris Waiting for Approval dihitung sebagai baris aktif, baris Rejected dan Unassigned tidak
73. Aktor Assignment mengajukan Submit untuk Assignee `Hendra Kusuma {runId}` dengan aset `Aset Kamera 1 {runId}`
74. Aktor Assignment mengajukan Submit untuk Assignee `Hendra Kusuma {runId}` dengan aset `Aset Kamera 2 {runId}`
75. Verifikasi baris `Aset Kamera 1 {runId}` dan `Aset Kamera 2 {runId}` berstatus `Waiting for Approval`
76. Aktor Assignment mengajukan Submit untuk Assignee `Hendra Kusuma {runId}` dengan aset `Aset Kamera 3 {runId}`
77. Verifikasi Submit ditolak dengan pesan `[Assignee] can hold up to 2 assets at a time.` dengan Assignee `Hendra Kusuma {runId}`, karena dua baris `Waiting for Approval` dihitung sebagai baris aktif
78. Approver `Agus Pratama {runId}` melakukan Reject atas aset `Aset Kamera 1 {runId}` dengan Approval Note `Aset sedang dipakai tim lain {runId}`
79. Verifikasi baris `Aset Kamera 1 {runId}` berstatus `Rejected`
80. Aktor Assignment mengajukan Submit untuk Assignee `Hendra Kusuma {runId}` dengan aset `Aset Kamera 3 {runId}`
81. Verifikasi baris `Aset Kamera 3 {runId}` lolos dan berstatus `Waiting for Approval`, karena baris `Rejected` tidak dihitung sebagai baris aktif
82. Approver `Agus Pratama {runId}` melakukan Approve atas aset `Aset Kamera 2 {runId}`
83. Aktor Assignment menyelesaikan handover aset `Aset Kamera 2 {runId}` tanpa konfirmasi Assignee
84. Aktor Assignment melakukan Unassign atas aset `Aset Kamera 2 {runId}`
85. Verifikasi baris `Aset Kamera 2 {runId}` berstatus `Unassigned`
86. Aktor Assignment mengajukan Submit untuk Assignee `Hendra Kusuma {runId}` dengan aset `Aset Kamera 4 {runId}`
87. Verifikasi baris `Aset Kamera 4 {runId}` lolos dan berstatus `Waiting for Approval`, karena baris `Unassigned` tidak dihitung sebagai baris aktif
