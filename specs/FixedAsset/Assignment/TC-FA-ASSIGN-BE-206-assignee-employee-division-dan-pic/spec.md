---
id: TC-FA-ASSIGN-BE-206-assignee-employee-division-dan-pic
title: "Aturan Assignee Employee dan Division serta PIC"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["V-ASG-10", "V-ASG-11", "F-ASSIGN-03.k2", "EC-ASG-07", "EC-ASG-46", "§10#r4", "§10#r5", "ASSIGN-LOGIC-06a", "ASSIGN-LOGIC-06b", "ASSIGN-LOGIC-06d", "ASSIGN-LOGIC-06e", "ASSIGN-LOGIC-06f", "ASSIGN-LOGIC-06g", "ASSIGN-LOGIC-06h", "ASSIGN-LOGIC-06i", "ASSIGN-LOGIC-06j", "ASSIGN-LOGIC-06l"]
smoke: []
dependsOn: []
trace:
  "V-ASG-10": [15, 19]
  "V-ASG-11": 4
  "F-ASSIGN-03.k2": [2, 4, 15, 21, 27, 29]
  "EC-ASG-07": [21, 22, 23]
  "EC-ASG-46": [15, 16, 17]
  "§10#r4": [5, 7]
  "§10#r5": 37
  "ASSIGN-LOGIC-06a": [21, 22, 25]
  "ASSIGN-LOGIC-06b": 21
  "ASSIGN-LOGIC-06d": [2, 11]
  "ASSIGN-LOGIC-06e": [4, 5]
  "ASSIGN-LOGIC-06f": 11
  "ASSIGN-LOGIC-06g": [27, 35]
  "ASSIGN-LOGIC-06h": [29, 31, 33, 35, 37]
  "ASSIGN-LOGIC-06i": [39, 42, 43]
  "ASSIGN-LOGIC-06j": [46, 48]
  "ASSIGN-LOGIC-06l": [52, 53, 54]
owner: BE
---

# Aturan Assignee Employee dan Division serta PIC

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Grup Assignee {runId}`, sebagai pengaju dan pemberi handover. Pengelola karyawan pada langkah yang menyebutnya. Assignee dan PIC bertindak sebagai dirinya sendiri pada langkah konfirmasi.
- Data:
  - DU-206-1: Category CE beserta Asset Name, Category `Kategori Employee Saja {runId}`, Asset Name `Nama Employee Saja {runId}`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `OFF`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Require approval `OFF`.
  - DU-206-2: Category CB beserta Asset Name, Category `Kategori Dua Tipe {runId}`, Asset Name `Nama Dua Tipe {runId}`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `ON`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Require approval `OFF`.
  - DU-206-3: Category CK beserta Asset Name, Category `Kategori Konfirmasi {runId}`, Asset Name `Nama Konfirmasi {runId}`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `ON`, Override Category Max assets per assignee `0`, Override Category Need recipient confirmation `Yes`, Override Category Photo at start `OFF`, Override Category Require approval `OFF`.
  - DU-206-4: Category CM beserta Asset Name, Category `Kategori Batas Satu {runId}`, Asset Name `Nama Batas Satu {runId}`, Override Category Allowed assignee Employee `ON`, Override Category Allowed assignee Division `ON`, Override Category Max assets per assignee `1`, Override Category Need recipient confirmation `No`, Override Category Photo at start `OFF`, Override Category Require approval `OFF`.
  - DU-206-5: Group aset, Group `Grup Assignee {runId}`.
  - DU-206-6: Division Assignee, Division `Gudang {runId}`.
  - DU-206-7: Division lain, Division `Finance {runId}`.
  - DU-206-8: Assignee Employee dengan akun login, Name `Budi Santoso {runId}`, Status `Aktif`, Akun login `Ada`, Tipe Assignee `Employee`.
  - DU-206-9: Assignee Employee yang akan dinonaktifkan, Name `Eko Nugroho {runId}`, Status `Aktif`, Akun login `Ada`, Tipe Assignee `Employee`.
  - DU-206-10: Karyawan Division Gudang tanpa akun login, Name `Dewi Tanpa Akun {runId}`, Status `Aktif`, Akun login `Tidak ada`, Division `Gudang {runId}`.
  - DU-206-11: Karyawan Division Finance ber-akun login, Name `Rudi Hartono {runId}`, Status `Aktif`, Akun login `Ada`, Division `Finance {runId}`.
  - DU-206-12: PIC ber-akun login Division Gudang, Name `Joko Prasetyo {runId}`, Status `Aktif`, Akun login `Ada`, Division `Gudang {runId}`.
  - DU-206-13: PIC kedua ber-akun login Division Gudang, Name `Wati Susanti {runId}`, Status `Aktif`, Akun login `Ada`, Division `Gudang {runId}`.
  - DU-206-14: PIC ber-akun login yang akan dinonaktifkan, Name `Hadi Santoso {runId}`, Status `Aktif`, Akun login `Ada`, Division `Gudang {runId}`.
  - DU-206-15: PIC ber-akun login yang akan pindah Division, Name `Yuni Lestari {runId}`, Status `Aktif`, Akun login `Ada`, Division `Gudang {runId}`.
  - DU-206-16: Aset Aset Employee Saja, Name `Aset Employee Saja {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Employee Saja {runId}`, Asset Name `Nama Employee Saja {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-17: Aset Aset Dua Tipe, Name `Aset Dua Tipe {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Dua Tipe {runId}`, Asset Name `Nama Dua Tipe {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-18: Aset Aset Draft Eko, Name `Aset Draft Eko {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Dua Tipe {runId}`, Asset Name `Nama Dua Tipe {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-19: Aset Aset Akun Login, Name `Aset Akun Login {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Dua Tipe {runId}`, Asset Name `Nama Dua Tipe {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-20: Aset Aset PIC Satu, Name `Aset PIC Satu {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Dua Tipe {runId}`, Asset Name `Nama Dua Tipe {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-21: Aset Aset PIC Dua, Name `Aset PIC Dua {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Dua Tipe {runId}`, Asset Name `Nama Dua Tipe {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-22: Aset Aset Konfirmasi PIC, Name `Aset Konfirmasi PIC {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Konfirmasi {runId}`, Asset Name `Nama Konfirmasi {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-23: Aset Aset Konfirmasi Assignee, Name `Aset Konfirmasi Assignee {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Konfirmasi {runId}`, Asset Name `Nama Konfirmasi {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-24: Aset Aset Batas Satu, Name `Aset Batas Satu {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Batas Satu {runId}`, Asset Name `Nama Batas Satu {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-25: Aset Aset Batas Dua, Name `Aset Batas Dua {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Batas Satu {runId}`, Asset Name `Nama Batas Satu {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-26: Aset Aset Batas Joko, Name `Aset Batas Joko {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Batas Satu {runId}`, Asset Name `Nama Batas Satu {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-27: Aset Aset PIC Nonaktif, Name `Aset PIC Nonaktif {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Dua Tipe {runId}`, Asset Name `Nama Dua Tipe {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-28: Aset Aset PIC Pindah, Name `Aset PIC Pindah {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Dua Tipe {runId}`, Asset Name `Nama Dua Tipe {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-29: Aset Aset Tanpa Akun, Name `Aset Tanpa Akun {runId}`, Group `Grup Assignee {runId}`, Category `Kategori Dua Tipe {runId}`, Asset Name `Nama Dua Tipe {runId}`, TAG `Non TAG`, Custody `Available`, Condition `Normal`.
  - DU-206-30: Input pengajuan untuk Assignee Employee, Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Purpose `Daily work`.
  - DU-206-31: Input pengajuan untuk Assignee Division, Assignee `Gudang {runId}`, Tipe Assignee `Division`, Purpose `Daily work`.
  - DU-206-32: PIC nonaktif Division Gudang, Name `Bambang Wijaya {runId}`, Status `Nonaktif`, Akun login `Ada`, Division `Gudang {runId}`.
- Kondisi:
  - Level Feature Suite Assignment pada plan adalah `Full`.
  - Setiap aset berada di Custody `Available` dan tidak berada di ASG aktif maupun Draft mana pun.

## Test Steps

### Assignee Employee wajib karyawan aktif dengan akun login
1. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Akun Login {runId}` dan Purpose `Daily work`
2. Verifikasi baris aset `Aset Akun Login {runId}` berstatus `Waiting for Handover`, karena Assignee Employee aktif dengan akun login memenuhi pemeriksaan Assignee
3. Aktor Assignment mengajukan Submit untuk Assignee `Dewi Tanpa Akun {runId}` dengan aset `Aset Tanpa Akun {runId}` dan Purpose `Daily work`
4. Verifikasi Submit atas Assignee tanpa akun login ditolak dengan pesan `[Name] has no login account. Only employees who can sign in can be assignees.` untuk karyawan `Dewi Tanpa Akun {runId}`
5. Verifikasi tidak ada ASG yang dibuat untuk Assignee `Dewi Tanpa Akun {runId}` dan Custody aset `Aset Tanpa Akun {runId}` tetap `Available`
6. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Tanpa Akun {runId}` dan Purpose `Daily work`
7. Verifikasi aset `Aset Tanpa Akun {runId}` dapat ditugaskan lewat Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}`, walau karyawan `Dewi Tanpa Akun {runId}` tanpa akun login tidak dapat menjadi Assignee sendiri

### Akun login diperlukan agar Assignee dapat mengonfirmasi dan melihat My Asset
8. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Konfirmasi Assignee {runId}` dan Purpose `Daily work`
9. Aktor Assignment menekan `Request Confirmation` untuk aset `Aset Konfirmasi Assignee {runId}`
10. Assignee `Budi Santoso {runId}` mengonfirmasi penerimaan aset `Aset Konfirmasi Assignee {runId}`
11. Verifikasi baris aset `Aset Konfirmasi Assignee {runId}` berstatus `Assigned` dan aset tampil di `My Asset` milik Assignee `Budi Santoso {runId}`

### Assignee harus masih aktif saat Submit
12. Aktor Assignment menyimpan Draft untuk Assignee `Eko Nugroho {runId}` dengan aset `Aset Draft Eko {runId}` dan Purpose `Daily work`
13. Pengelola karyawan menonaktifkan karyawan `Eko Nugroho {runId}`
14. Aktor Assignment mengajukan Submit atas Draft tersebut
15. Verifikasi Submit ditolak dengan pesan `[Name] is no longer active. Pick another assignee.` dengan Name `Eko Nugroho {runId}`
16. Verifikasi baris aset `Aset Draft Eko {runId}` tidak berubah dan Custody tetap `Available`
17. Verifikasi Draft yang memuat aset `Aset Draft Eko {runId}` tetap tersimpan
18. Aktor Assignment membuka kembali Draft tersebut
19. Verifikasi Draft yang dibuka kembali menampilkan alasan `[Name] is no longer active. Pick another assignee.` dengan Name `Eko Nugroho {runId}` pada Assignee

### Allowed assignee per aset menentukan tipe Assignee yang layak
20. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Employee Saja {runId}` (hanya tipe `Employee` diizinkan) dan `Aset Dua Tipe {runId}` (tipe `Employee` dan `Division` diizinkan)
21. Verifikasi aset `Aset Employee Saja {runId}` tidak layak dengan pesan `This asset can't be assigned to a division.`, karena aset yang tidak mengizinkan tipe Assignee terpilih tidak layak untuk form itu
22. Verifikasi aset `Aset Dua Tipe {runId}` layak dan tidak termasuk dalam baris bermasalah
23. Verifikasi form campuran dievaluasi per aset, sehingga hanya aset `Aset Employee Saja {runId}` yang bermasalah untuk Assignee Division
24. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Employee Saja {runId}` dan `Aset Dua Tipe {runId}` dan Purpose `Daily work`
25. Verifikasi kedua baris berstatus `Waiting for Handover`, karena tipe Assignee `Employee` diizinkan oleh kedua aset

### Division wajib PIC aktif ber-akun login dari Division yang sama
26. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` tanpa memilih PIC dengan aset `Aset PIC Satu {runId}`
27. Verifikasi Submit Assignee Division tanpa PIC ditolak dengan pesan `You must pick a PIC`, karena PIC wajib untuk Assignee Division
28. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Rudi Hartono {runId}` dan aset `Aset PIC Satu {runId}`
29. Verifikasi Submit ditolak dengan pesan `[Name] isn't an active member of [Division].` dengan Name `Rudi Hartono {runId}` dan Assignee Division `Gudang {runId}`
30. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Dewi Tanpa Akun {runId}` dan aset `Aset PIC Satu {runId}`
31. Verifikasi Submit ditolak dengan pesan `[Name] isn't an active member of [Division].` dengan Name `Dewi Tanpa Akun {runId}` dan Assignee Division `Gudang {runId}`, karena PIC wajib ber-akun login walau ia anggota `Gudang {runId}`
32. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Bambang Wijaya {runId}` dan aset `Aset PIC Satu {runId}`
33. Verifikasi Submit ditolak dengan pesan `[Name] isn't an active member of [Division].` dengan Name `Bambang Wijaya {runId}` dan Assignee Division `Gudang {runId}`, karena PIC wajib berstatus aktif walau ia anggota `Gudang {runId}`
34. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset PIC Satu {runId}`
35. Verifikasi ASG terbentuk dengan Assignee Division `Gudang {runId}` dan PIC `Joko Prasetyo {runId}` untuk aset `Aset PIC Satu {runId}`
36. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Wati Susanti {runId}` dan aset `Aset PIC Dua {runId}`
37. Verifikasi ASG kedua untuk Assignee Division `Gudang {runId}` memiliki PIC `Wati Susanti {runId}` sedangkan ASG pertama tetap memiliki PIC `Joko Prasetyo {runId}`, karena PIC dipilih per transaksi dan master `Division` tidak menyimpan PIC

### PIC menerima notifikasi, mengonfirmasi handover, dan melihat aset di My Asset
38. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Konfirmasi PIC {runId}`
39. Verifikasi PIC `Joko Prasetyo {runId}` menerima notifikasi untuk ASG tersebut
40. Aktor Assignment menekan `Request Confirmation` untuk aset `Aset Konfirmasi PIC {runId}`
41. PIC `Joko Prasetyo {runId}` mengonfirmasi penerimaan aset `Aset Konfirmasi PIC {runId}` saat handover
42. Verifikasi baris aset `Aset Konfirmasi PIC {runId}` berstatus `Assigned`, karena PIC mengonfirmasi saat handover
43. Verifikasi PIC `Joko Prasetyo {runId}` melihat aset `Aset Konfirmasi PIC {runId}` di `My Asset` dengan penanda `On behalf of [Division]` dengan Assignee Division `Gudang {runId}`

### Max assets per assignee dihitung untuk Assignee, bukan untuk PIC
44. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Batas Satu {runId}`
45. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Joko Prasetyo {runId}` dan aset `Aset Batas Dua {runId}`
46. Verifikasi Submit ditolak dengan pesan `[Assignee] can hold up to 1 asset at a time.` dengan Assignee `Gudang {runId}`, karena batas dihitung untuk Assignee Division
47. Aktor Assignment mengajukan Submit untuk Assignee `Joko Prasetyo {runId}` dengan aset `Aset Batas Joko {runId}` dan Purpose `Daily work`
48. Verifikasi baris aset `Aset Batas Joko {runId}` berstatus `Waiting for Handover`, karena baris Assignee Division `Gudang {runId}` tidak dihitung untuk `Joko Prasetyo {runId}` sebagai PIC

### PIC dinonaktifkan atau pindah Division
49. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Hadi Santoso {runId}` dan aset `Aset PIC Nonaktif {runId}`
50. Aktor Assignment mengajukan Submit untuk Assignee Division `Gudang {runId}` dengan PIC `Yuni Lestari {runId}` dan aset `Aset PIC Pindah {runId}`
51. Pengelola karyawan menonaktifkan karyawan `Hadi Santoso {runId}` dan memindahkan karyawan `Yuni Lestari {runId}` ke `Division` `Finance {runId}`
52. Verifikasi baris aktif aset `Aset PIC Nonaktif {runId}` dan `Aset PIC Pindah {runId}` diberi penanda `No PIC`
53. Verifikasi notifikasi untuk PIC `Hadi Santoso {runId}` dan `Yuni Lestari {runId}` dialihkan ke Aktor Assignment Group asal
54. Verifikasi Aktor Assignment mendapat tugas `Change PIC` untuk kedua ASG tersebut
