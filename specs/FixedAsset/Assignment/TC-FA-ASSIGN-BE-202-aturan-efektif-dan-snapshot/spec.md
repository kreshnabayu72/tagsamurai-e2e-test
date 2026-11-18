---
id: TC-FA-ASSIGN-BE-202-aturan-efektif-dan-snapshot
title: "Aturan efektif per aset, snapshot saat Submit, dan perubahan setting"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EC-ASG-37", "EC-ASG-58", "EC-ASG-59", "EC-ASG-60", "EC-ASG-61", "EC-ASG-62", "§9.4.3#b10", "§9.4.3#b11", "§9.7#r22", "ASSIGN-LOGIC-02a", "ASSIGN-LOGIC-02b", "ASSIGN-LOGIC-02c", "ASSIGN-LOGIC-02d", "ASSIGN-LOGIC-02e", "ASSIGN-LOGIC-02f", "ASSIGN-LOGIC-02g", "ASSIGN-LOGIC-02h"]
smoke: []
dependsOn: []
trace:
  "EC-ASG-37": [17, 19]
  "EC-ASG-58": [36, 38, 40, 43]
  "EC-ASG-59": [47, 49, 52, 54]
  "EC-ASG-60": [61, 62, 63, 64, 65, 66, 81, 82, 83, 84]
  "EC-ASG-61": [32, 33, 34]
  "EC-ASG-62": [28, 29, 30]
  "§9.4.3#b10": [17, 24]
  "§9.4.3#b11": [62, 63]
  "§9.7#r22": [17, 24, 38, 47, 61]
  "ASSIGN-LOGIC-02a": [5, 6, 7, 8, 9, 74]
  "ASSIGN-LOGIC-02b": [10, 11, 68, 69, 71]
  "ASSIGN-LOGIC-02c": 12
  "ASSIGN-LOGIC-02d": 2
  "ASSIGN-LOGIC-02e": [21, 24]
  "ASSIGN-LOGIC-02f": [61, 62, 77, 81, 82]
  "ASSIGN-LOGIC-02g": [14, 15]
  "ASSIGN-LOGIC-02h": [2, 3, 66]
owner: BE
---

# Aturan efektif per aset, snapshot saat Submit, dan perubahan setting

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Grup Aturan Biasa {runId}` dan `Grup Aturan ON {runId}`, sebagai pengaju, pemberi handover, dan penerima Unassign. Aktor pemicu: Pengelola Transaction Settings (mengubah nilai setting), Pengelola Role Transaksi (mengubah daftar Approver Group), dan Approver `Rina Wijaya {runId}` (memutuskan pengajuan).
- Data:
  - DU-202-1: Group tanpa override aturan, Group `Grup Aturan Biasa {runId}`, Approver `Rina Wijaya {runId}`.
  - DU-202-2: Group dengan override Require approval, Group `Grup Aturan ON {runId}`, Override Group Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`.
  - DU-202-3: Category tanpa override dengan Asset Name biasa, Category `Kategori Biasa {runId}`, Asset Name `Nama Biasa {runId}`.
  - DU-202-4: Category dengan override Require approval beserta Asset Name tanpa override, Category `Kategori Aturan {runId}`, Override Category Require approval `ON`, Approval type `Any one`, Asset Name `Nama Aturan {runId}`.
  - DU-202-5: Asset Name dengan override Require approval, Asset Name `Nama Aturan OFF {runId}`, Category `Kategori Aturan {runId}`, Override Asset Name Require approval `OFF`.
  - DU-202-6: Asset Name dengan override Allow Assign, Asset Name `Nama Deny {runId}`, Category `Kategori Biasa {runId}`, Override Asset Name Allow Assign `Deny`.
  - DU-202-7: Category dengan batas jumlah aset per Assignee, Category `Kategori Batas {runId}`, Asset Name `Nama Batas {runId}`, Max assets per assignee `5`.
  - DU-202-8: Category dengan Allow Assign, Category `Kategori Izin {runId}`, Asset Name `Nama Izin {runId}`, Allow Assign `Allow`.
  - DU-202-9: Category dengan Allowed assignee, Category `Kategori Assignee {runId}`, Asset Name `Nama Assignee {runId}`, Allowed assignee Employee `ON`, Allowed assignee Division `ON`.
  - DU-202-10: Category dengan Transaction timeout dan Require approval, Category `Kategori Timeout {runId}`, Asset Name `Nama Timeout {runId}`, Override Category Require approval `ON`, Approval type `Any one`, Transaction timeout `7 hari`.
  - DU-202-11: Assignee Employee dengan akun login, Name `Budi Santoso {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`.
  - DU-202-12: Assignee Employee kedua dengan akun login, Name `Tono Hartono {runId}`, Tipe Assignee `Employee`, Status `Aktif`, Akun login `Ada`.
  - DU-202-13: Approver pada Group aturan, Name `Rina Wijaya {runId}`, Role Transaksi `Approver`, Status `Aktif`.
  - DU-202-14: Approver yang belum ditugaskan pada Group aturan ON, Name `Agus Pratama {runId}`, Role Transaksi `Approver`, Status `Aktif`, Approver pada Group Aturan ON `Belum`.
  - DU-202-15: Aset Aset Dasar, Name `Aset Dasar {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Biasa {runId}`, Asset Name `Nama Biasa {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-16: Aset Aset Kategori, Name `Aset Kategori {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Aturan {runId}`, Asset Name `Nama Aturan {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-17: Aset Aset Nama OFF, Name `Aset Nama OFF {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Aturan {runId}`, Asset Name `Nama Aturan OFF {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-18: Aset Aset Grup ON, Name `Aset Grup ON {runId}`, Group `Grup Aturan ON {runId}`, Category `Kategori Aturan {runId}`, Asset Name `Nama Aturan OFF {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-19: Aset Aset Override OFF, Name `Aset Override OFF {runId}`, Group `Grup Aturan ON {runId}`, Category `Kategori Aturan {runId}`, Asset Name `Nama Aturan OFF {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`, Override Asset Require approval `OFF`.
  - DU-202-20: Aset Aset Deny, Name `Aset Deny {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Biasa {runId}`, Asset Name `Nama Deny {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`, Override Asset Allow Assign `Allow`.
  - DU-202-21: Aset Aset Konfirmasi, Name `Aset Konfirmasi {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Biasa {runId}`, Asset Name `Nama Biasa {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `Yes`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-22: Aset Aset Foto, Name `Aset Foto {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Biasa {runId}`, Asset Name `Nama Biasa {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-23: Aset Aset Batas Satu, Name `Aset Batas Satu {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Batas {runId}`, Asset Name `Nama Batas {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`.
  - DU-202-24: Aset Aset Batas Dua, Name `Aset Batas Dua {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Batas {runId}`, Asset Name `Nama Batas {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`.
  - DU-202-25: Aset Aset Batas Tiga, Name `Aset Batas Tiga {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Batas {runId}`, Asset Name `Nama Batas {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`.
  - DU-202-26: Aset Aset Izin Berjalan, Name `Aset Izin Berjalan {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Izin {runId}`, Asset Name `Nama Izin {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-27: Aset Aset Izin Baru, Name `Aset Izin Baru {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Izin {runId}`, Asset Name `Nama Izin {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-28: Aset Aset Assignee Berjalan, Name `Aset Assignee Berjalan {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Assignee {runId}`, Asset Name `Nama Assignee {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-29: Aset Aset Assignee Baru, Name `Aset Assignee Baru {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Assignee {runId}`, Asset Name `Nama Assignee {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-30: Aset Aset Timeout Lama, Name `Aset Timeout Lama {runId}`, Group `Grup Aturan ON {runId}`, Category `Kategori Timeout {runId}`, Asset Name `Nama Timeout {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-31: Aset Aset Timeout Baru, Name `Aset Timeout Baru {runId}`, Group `Grup Aturan ON {runId}`, Category `Kategori Timeout {runId}`, Asset Name `Nama Timeout {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-32: Aset Aset Timeout Draft, Name `Aset Timeout Draft {runId}`, Group `Grup Aturan ON {runId}`, Category `Kategori Timeout {runId}`, Asset Name `Nama Timeout {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-33: Input pengajuan untuk Assignee Budi, Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Note `Penugasan uji aturan {runId}`, Purpose `Daily work`.
  - DU-202-34: Input pengajuan untuk Assignee Tono, Assignee `Tono Hartono {runId}`, Tipe Assignee `Employee`, Purpose `Daily work`.
  - DU-202-35: Nilai setting dan data aset sesudah diubah, Need recipient confirmation Aset Konfirmasi `No`, Photo at end Aset Foto `ON`, Max assets per assignee Kategori Batas `1`, Allow Assign Kategori Izin `Deny`, Allowed assignee Employee Kategori Assignee `OFF`, Transaction timeout Kategori Timeout `3 hari`, Category Aset Kategori `Kategori Biasa {runId}`, Asset Name Aset Nama OFF `Nama Aturan {runId}`, Group Aset Grup ON `Grup Aturan Biasa {runId}`, Transaction timeout Kategori Serah Langsung `3 hari`, Transaction timeout Kategori Serah Approval `3 hari`.
  - DU-202-36: Category Dua Tipe, Category `Kategori Dua Tipe {runId}`, Asset Name `Nama Dua Tipe {runId}`, Allowed assignee Employee `ON`, Allowed assignee Division `ON`.
  - DU-202-37: Category Karyawan Saja, Category `Kategori Karyawan Saja {runId}`, Asset Name `Nama Karyawan Saja {runId}`, Allowed assignee Employee `ON`, Allowed assignee Division `OFF`.
  - DU-202-38: Category Serah Langsung, Category `Kategori Serah Langsung {runId}`, Asset Name `Nama Serah Langsung {runId}`, Require approval `OFF`, Transaction timeout `7 hari`.
  - DU-202-39: Category Serah Approval, Category `Kategori Serah Approval {runId}`, Asset Name `Nama Serah Approval {runId}`, Override Category Require approval `ON`, Approval type `Any one`, Transaction timeout `7 hari`.
  - DU-202-40: Aset Foto Awal ON, Name `Aset Foto Awal ON {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Biasa {runId}`, Asset Name `Nama Biasa {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `ON`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-41: Aset Foto Awal OFF, Name `Aset Foto Awal OFF {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Biasa {runId}`, Asset Name `Nama Biasa {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-42: Aset Dua Tipe, Name `Aset Dua Tipe {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Dua Tipe {runId}`, Asset Name `Nama Dua Tipe {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-43: Aset Karyawan Saja, Name `Aset Karyawan Saja {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Karyawan Saja {runId}`, Asset Name `Nama Karyawan Saja {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-44: Aset Serah Langsung, Name `Aset Serah Langsung {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Serah Langsung {runId}`, Asset Name `Nama Serah Langsung {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
  - DU-202-45: Aset Serah Approval, Name `Aset Serah Approval {runId}`, Group `Grup Aturan Biasa {runId}`, Category `Kategori Serah Approval {runId}`, Asset Name `Nama Serah Approval {runId}`, TAG `Non TAG`, Custody `Available`, Override Asset Need recipient confirmation `No`, Override Asset Photo at start `OFF`, Override Asset Photo at end `OFF`, Override Asset Max assets per assignee `0`.
- Kondisi:
  - Level Feature Suite Assignment pada plan adalah `Full`, dan Approval Workflow tersedia di plan.
  - Company default: Require approval bernilai `OFF`, Allow Assign bernilai `Allow`, Allowed assignee Employee bernilai `ON`, dan Max assets per assignee bernilai `5`.
  - Setiap aset berada di Custody `Available` dan tidak berada di ASG aktif maupun Draft mana pun.
  - Transaction timeout untuk Category `Kategori Timeout {runId}` bernilai `7 hari`.
  - Transaction timeout untuk Category `Kategori Serah Langsung {runId}` dan `Kategori Serah Approval {runId}` masing-masing bernilai `7 hari`.

## Test Steps

### Draft belum memiliki snapshot maupun timeout
1. Aktor Assignment menyimpan Draft untuk Assignee `Budi Santoso {runId}` dengan Note `Penugasan uji aturan {runId}` dan Purpose `Daily work`, memuat aset `Aset Dasar {runId}`, `Aset Kategori {runId}`, `Aset Nama OFF {runId}`, `Aset Grup ON {runId}`, `Aset Override OFF {runId}`, `Aset Konfirmasi {runId}`, `Aset Foto {runId}`
2. Verifikasi baris Draft belum memiliki snapshot aturan efektif, daftar approver, maupun Approval type
3. Verifikasi Draft tidak memiliki batas waktu Transaction timeout

### Aturan efektif tiap aset diselesaikan berlapis dan di-snapshot saat Submit
4. Aktor Assignment mengajukan Submit atas Draft tersebut sehingga terbentuk satu ASG per Group asal
5. Verifikasi baris `Aset Dasar {runId}` berstatus `Waiting for Handover` dengan Approval `Not required`, karena tanpa override nilai Company default Require approval `OFF` berlaku
6. Verifikasi baris `Aset Kategori {runId}` berstatus `Waiting for Approval`, karena override Category `ON` mengalahkan Company default
7. Verifikasi baris `Aset Nama OFF {runId}` berstatus `Waiting for Handover`, karena override Asset Name `OFF` mengalahkan override Category `ON`
8. Verifikasi baris `Aset Grup ON {runId}` berstatus `Waiting for Approval`, karena override Group `ON` mengalahkan override Asset Name `OFF`
9. Verifikasi baris `Aset Override OFF {runId}` berstatus `Waiting for Handover`, karena override Asset `OFF` mengalahkan override Group `ON`
10. Verifikasi satu ASG memuat baris `Aset Dasar {runId}` dengan Approval `Not required` dan baris `Aset Kategori {runId}` dengan Approval `Waiting`
11. Verifikasi satu ASG memuat baris `Aset Dasar {runId}` dengan Need recipient confirmation `No` dan baris `Aset Konfirmasi {runId}` dengan Need recipient confirmation `Yes`
12. Verifikasi setiap baris menyimpan snapshot berupa versi setting, nilai efektif, daftar approver, dan Approval type, dan baris `Aset Kategori {runId}` mencatat Approval type `Any one` dengan approver `Rina Wijaya {runId}`

### Deny pada override mengalahkan Allow
13. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Deny {runId}` yang override Asset Name-nya `Deny` dan override Asset-nya `Allow`
14. Verifikasi Submit ditolak dengan pesan `Can't be assigned: this asset is not available for assignment. Contact [Name] (Manage asset & TAG).`, karena Deny pada override selalu menang
15. Verifikasi tidak ada baris yang dibuat untuk aset `Aset Deny {runId}` dan Custody tetap `Available`

### Perubahan setting tidak memengaruhi baris yang sudah diajukan
16. Pengelola Transaction Settings mengubah override Asset `Aset Konfirmasi {runId}`: Need recipient confirmation dari `Yes` menjadi `No`
17. Verifikasi baris `Aset Konfirmasi {runId}` tetap memakai snapshot Need recipient confirmation `Yes` dan tidak memakai nilai terbaru
18. Aktor Assignment menyelesaikan handover aset `Aset Konfirmasi {runId}` tanpa konfirmasi Assignee
19. Verifikasi baris `Aset Konfirmasi {runId}` tetap `Waiting for Handover`, karena Need recipient confirmation `Yes` menurut snapshot menuntut konfirmasi Assignee
20. Aktor Assignment menyelesaikan handover aset `Aset Foto {runId}` tanpa konfirmasi Assignee
21. Verifikasi baris `Aset Foto {runId}` berstatus `Assigned`
22. Pengelola Transaction Settings mengubah override Asset `Aset Foto {runId}`: Photo at end dari `OFF` menjadi `ON`
23. Aktor Assignment melakukan Unassign atas aset `Aset Foto {runId}` tanpa foto Unassign
24. Verifikasi baris `Aset Foto {runId}` berstatus `Unassigned` tanpa foto Unassign, karena Unassign memakai snapshot baris itu dan perubahan setting tidak memengaruhi baris yang sudah Assigned

### Data aset berubah saat baris aktif
25. Aktor Assignment mengubah Category aset `Aset Kategori {runId}` menjadi `Kategori Biasa {runId}`
26. Aktor Assignment mengubah Asset Name aset `Aset Nama OFF {runId}` menjadi `Nama Aturan {runId}`
27. Aktor Assignment mengubah Group aset `Aset Grup ON {runId}` menjadi `Grup Aturan Biasa {runId}`
28. Verifikasi baris `Aset Kategori {runId}` tetap `Waiting for Approval` dengan approver `Rina Wijaya {runId}` menurut snapshot, walau Category barunya tidak mewajibkan approval
29. Verifikasi baris `Aset Nama OFF {runId}` tetap `Waiting for Handover` dengan Approval `Not required`, walau Asset Name barunya berada di Category yang mewajibkan approval
30. Verifikasi baris `Aset Grup ON {runId}` tetap `Waiting for Approval` dan Group asal ASG-nya tetap `Grup Aturan ON {runId}`

### Daftar Approver Group berubah saat pengajuan menunggu
31. Pengelola Role Transaksi menugaskan `Agus Pratama {runId}` sebagai `Approver` pada Group `Grup Aturan ON {runId}`
32. Verifikasi pengajuan yang memuat aset `Aset Grup ON {runId}` tampil di antrean Active milik approver `Rina Wijaya {runId}`
33. Verifikasi pengajuan yang memuat aset `Aset Grup ON {runId}` tidak tampil di antrean Active milik approver `Agus Pratama {runId}`, karena aset memakai snapshot approver
34. Verifikasi baris `Aset Grup ON {runId}` tetap memuat daftar approver snapshot yang hanya berisi `Rina Wijaya {runId}`

### Max assets per assignee diturunkan di bawah jumlah baris aktif
35. Aktor Assignment mengajukan Submit untuk Assignee `Tono Hartono {runId}` dengan aset `Aset Batas Satu {runId}`, `Aset Batas Dua {runId}`
36. Verifikasi baris `Aset Batas Satu {runId}`, `Aset Batas Dua {runId}` berstatus `Waiting for Handover`
37. Pengelola Transaction Settings mengubah Max assets per assignee pada Category `Kategori Batas {runId}` dari `5` menjadi `1`
38. Verifikasi baris `Aset Batas Satu {runId}`, `Aset Batas Dua {runId}` tetap `Waiting for Handover`, penugasan berjalan tidak terpengaruh
39. Aktor Assignment mengajukan Submit untuk Assignee `Tono Hartono {runId}` dengan aset `Aset Batas Tiga {runId}`
40. Verifikasi Submit ditolak dengan pesan `[Assignee] can hold up to 1 asset at a time.` dengan Assignee `Tono Hartono {runId}`
41. Pengaju melakukan Cancel Assignment pada baris `Aset Batas Satu {runId}`, `Aset Batas Dua {runId}`
42. Aktor Assignment mengajukan Submit untuk Assignee `Tono Hartono {runId}` dengan aset `Aset Batas Tiga {runId}`
43. Verifikasi baris `Aset Batas Tiga {runId}` berstatus `Waiting for Handover`, karena jumlah baris aktif Assignee sudah di bawah batas baru

### Allow Assign menjadi Deny dan Allowed assignee dipersempit setelah Submit
44. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Izin Berjalan {runId}`
45. Pengelola Transaction Settings mengubah Allow Assign pada Category `Kategori Izin {runId}` dari `Allow` menjadi `Deny`
46. Aktor Assignment menyelesaikan handover aset `Aset Izin Berjalan {runId}` tanpa konfirmasi Assignee
47. Verifikasi baris `Aset Izin Berjalan {runId}` berstatus `Assigned`, karena baris berjalan tetap mengikuti snapshot
48. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Izin Baru {runId}`
49. Verifikasi Submit ditolak dengan pesan `Assigning isn't allowed for [Category].` dengan Category `Kategori Izin {runId}`
50. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Assignee Berjalan {runId}`
51. Pengelola Transaction Settings mengubah Allowed assignee Employee pada Category `Kategori Assignee {runId}` dari `ON` menjadi `OFF`
52. Verifikasi baris `Aset Assignee Berjalan {runId}` tetap `Waiting for Handover`, karena baris berjalan tetap mengikuti snapshot
53. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Assignee Baru {runId}`
54. Verifikasi Submit ditolak dengan pesan `This asset can't be assigned to an employee.`

### Transaction timeout diubah saat baris sedang menunggu
55. Aktor Assignment menyimpan Draft untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Timeout Draft {runId}` dan Purpose `Daily work`
56. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Timeout Lama {runId}`
57. Waktu berlalu 4 hari
58. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Timeout Baru {runId}`
59. Waktu berlalu 1 hari
60. Pengelola Transaction Settings mengubah Transaction timeout pada Category `Kategori Timeout {runId}` dari `7 hari` menjadi `3 hari`
61. Verifikasi batas waktu baris `Aset Timeout Baru {runId}` adalah saat baris masuk `Waiting for Approval` ditambah `3 hari`
62. Verifikasi batas waktu baris `Aset Timeout Lama {runId}`, yang batas barunya jatuh sebelum waktu Save, disetel ke waktu Save ditambah `24 jam`
63. Verifikasi tidak ada baris yang sedang menunggu memiliki batas waktu sebelum waktu Save sesudah perhitungan ulang
64. Verifikasi peringatan `assignment_almost_timeout` dikirim ulang untuk baris `Aset Timeout Lama {runId}`, karena sisa waktu ke batas baru 24 jam atau kurang
65. Verifikasi peringatan `assignment_almost_timeout` tidak dikirim ulang untuk baris `Aset Timeout Baru {runId}`, karena sisa waktu ke batas baru lebih dari 24 jam
66. Verifikasi Draft yang memuat aset `Aset Timeout Draft {runId}` tetap tanpa batas waktu setelah Transaction timeout diubah

### Dua aset dalam satu ASG punya Photo at start dan Allowed assignee berbeda
67. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Foto Awal ON {runId}`, `Aset Foto Awal OFF {runId}`, `Aset Dua Tipe {runId}`, dan `Aset Karyawan Saja {runId}`
68. Verifikasi satu ASG memuat baris `Aset Foto Awal ON {runId}` dengan Photo at start `ON` dan baris `Aset Foto Awal OFF {runId}` dengan Photo at start `OFF`
69. Verifikasi satu ASG memuat baris `Aset Dua Tipe {runId}` dengan Allowed assignee Employee `ON` dan Assignee Division `ON`, dan baris `Aset Karyawan Saja {runId}` dengan Allowed assignee Employee `ON` dan Assignee Division `OFF`
70. Aktor Assignment menyelesaikan handover aset `Aset Foto Awal OFF {runId}` tanpa foto handover dan tanpa konfirmasi Assignee
71. Verifikasi baris `Aset Foto Awal OFF {runId}` berstatus `Assigned`, karena aset itu tidak mewajibkan Photo at start

### Transaction timeout diubah saat baris Waiting for Handover
72. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Serah Langsung {runId}`
73. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Aset Serah Approval {runId}`
74. Verifikasi baris `Aset Serah Langsung {runId}` berstatus `Waiting for Handover` dan baris `Aset Serah Approval {runId}` berstatus `Waiting for Approval`
75. Waktu berlalu 4 hari
76. Approver `Rina Wijaya {runId}` menyetujui aset `Aset Serah Approval {runId}`
77. Verifikasi baris `Aset Serah Approval {runId}` berstatus `Waiting for Handover`
78. Waktu berlalu 1 hari
79. Pengelola Transaction Settings mengubah Transaction timeout pada Category `Kategori Serah Langsung {runId}` dari `7 hari` menjadi `3 hari`
80. Pengelola Transaction Settings mengubah Transaction timeout pada Category `Kategori Serah Approval {runId}` dari `7 hari` menjadi `3 hari`
81. Verifikasi batas waktu baris `Aset Serah Langsung {runId}`, yang batas barunya jatuh sebelum waktu Save, disetel ke waktu Save ditambah `24 jam`
82. Verifikasi batas waktu baris `Aset Serah Approval {runId}` adalah saat baris masuk `Waiting for Handover` lewat Approve ditambah `3 hari`, bukan saat Submit ditambah `3 hari`
83. Verifikasi peringatan `assignment_almost_timeout` dikirim ulang untuk baris `Aset Serah Langsung {runId}`, karena sisa waktu ke batas baru 24 jam atau kurang
84. Verifikasi peringatan `assignment_almost_timeout` tidak dikirim ulang untuk baris `Aset Serah Approval {runId}`, karena sisa waktu ke batas baru lebih dari 24 jam
