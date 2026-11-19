---
id: TC-FA-ASSIGN-E2E-065-pemetaan-transaction-settings-dep-settings-transaction-rules
title: "Perubahan Transaction Settings tab Assign dan efeknya"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.12#p1", "§9.12#p2", "§9.12#r1", "§9.12#r2", "§9.12#r3", "§9.12#r4", "§9.12#r5", "§9.12#r6", "§9.12#r7", "§9.12#r8", EC-ASG-113]
smoke: []
dependsOn: ["Settings Transaction Rules: tab Assign"]
trace:
  "§9.12#p1": 19
  "§9.12#p2": 1
  "§9.12#r1": 19
  "§9.12#r2": [48, 61, 64]
  "§9.12#r3": 23
  "§9.12#r4": [34, 47]
  "§9.12#r5": [31, 32, 46]
  "§9.12#r6": [35, 47]
  "§9.12#r7": [72, 76]
  "§9.12#r8": [11, 41, 86]
  EC-ASG-113: 12
anchor: [18, 40]
coverage:
  web: automated
---
# Perubahan Transaction Settings tab Assign dan efeknya

## Prerequisites
- Aktor: Total Control `Fajar Nugroho {runId}` (DU-065-2) yang mengubah Transaction Settings dan memakai Assignment; Approver `Anton Pratama {runId}` (DU-065-3).
- Layar awal: Settings > Transaction Settings, tab `Assign`.
- Data:
  - DU-065-1: Spec ini memakai entitas khusus `Entitas Setting Assign {runId}` yang tidak dipakai spec lain; nilai awal tab `Assign`: `Allow Assign` `Allow`, `Allowed assignee: Employee` `ON`, `Allowed assignee: Division` `ON`, `Max assets per assignee` `0`, `Need recipient confirmation` `Yes`, `Photo at start` `OFF`, `Photo at end` `OFF`, `Require approval` `OFF`, `Send email notifications` `ON`.
  - DU-065-2: Karyawan `Fajar Nugroho {runId}`, role Total Control, Status `Active`.
  - DU-065-3: Karyawan `Anton Pratama {runId}`, role Approver, Group penugasan `Head Office`, Status `Active`.
  - DU-065-4: Karyawan `Budi Santoso {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, memegang satu aset `Assigned` (DU-065-8).
  - DU-065-5: Karyawan `Citra Lestari {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, tanpa penugasan aktif.
  - DU-065-6: Aset `Laptop Asus Zenbook {runId}`, Category `Laptop {runId}`, Group `Head Office`, Custody `Available`.
  - DU-065-7: Aset `Monitor Samsung 24 {runId}`, Category `Monitor {runId}`, Group `Head Office`, Custody `Available`.
  - DU-065-8: ASG `Assigned` untuk Assignee `Budi Santoso {runId}` berisi aset `Kamera Sony A6000 {runId}`.
  - DU-065-9: Draft Assignee `Citra Lestari {runId}` berisi aset `Webcam Logitech C920 {runId}`, Purpose `Rapat daring`, dibuat sebelum batas Transaction timeout terlewati.
  - DU-065-10: ASG `Waiting for Handover` untuk Assignee `Rina Wijaya {runId}` berisi aset `Speaker JBL Flip 6 {runId}`, batas Transaction timeout sudah terlewati.
  - DU-065-11: Karyawan `Rina Wijaya {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login.
  - DU-065-12: Purpose `Pemakaian tim desain` untuk ASG baru milik `Citra Lestari {runId}`.
  - DU-065-13: Division `Divisi Desain {runId}` dengan satu anggota ber-akun login `Citra Lestari {runId}`, tanpa penugasan aktif.
  - DU-065-14: Aset `Proyektor Epson EB-X06 {runId}`, Category `Proyektor {runId}`, Group `Head Office`, Custody `Available`.
  - DU-065-15: Aset `Scanner Canon LiDE 300 {runId}`, Category `Scanner {runId}`, Group `Head Office`, Custody `Available`.

## Test Steps

### Tab Assign tampil dan nilai diubah di Transaction Settings
1. Verifikasi tab `Assign` tampil di Transaction Settings pada entitas level `Full`
2. Ubah `Allow Assign` untuk Category `Laptop {runId}` menjadi `Deny`
3. Ubah `Allowed assignee: Division` menjadi `OFF`
4. Ubah `Max assets per assignee` menjadi `1`
5. Ubah `Need recipient confirmation` menjadi `No`
6. Ubah `Photo at start` menjadi `ON`
7. Ubah `Photo at end` menjadi `ON`
8. Ubah `Require approval` menjadi `ON`
9. Ubah `Send email notifications` menjadi `OFF`
10. Simpan perubahan Transaction Settings
11. Verifikasi `Send email notifications` tersimpan `OFF`
12. Verifikasi `Allowed assignee: Division` tersimpan `OFF` dan `Allowed assignee: Employee` tetap `ON` pada level `Full`

### Allow Assign Deny menyaring aset di Select Asset
13. Buka halaman Transactions > Assignment
14. Klik `[+ Assign]`
15. Klik `Employee` pada overlay `Assign to`
16. Klik `[+ Asset]`
17. Ketik Search `{runId}`, tekan Enter
18. Verifikasi aset `Monitor Samsung 24 {runId}` tampil di dialog Select Asset
19. Verifikasi aset `Laptop Asus Zenbook {runId}` tidak tampil di dialog Select Asset karena Allow Assign efektif Deny

### Max assets per assignee memblokir Assignee yang sudah penuh
20. Tutup dialog Select Asset
21. Klik `[Select Assignee]`
22. Ketik Search `Budi Santoso {runId}`, tekan Enter
23. Verifikasi baris `Budi Santoso {runId}` berstatus `Blocked` dengan alasan `[Assignee] can hold up to 1 asset at a time.` dan jumlah `1`
24. Ganti isi kotak search dengan `Citra Lestari {runId}`, tekan Enter
25. Pilih baris `Citra Lestari {runId}`
26. Klik `[Select]`

### Need recipient confirmation, Require approval, dan bukti foto tercermin di Select Asset dan form
27. Klik `[+ Asset]`
28. Ketik Search `Monitor Samsung 24 {runId}`, tekan Enter
29. Pilih baris aset `Monitor Samsung 24 {runId}`
30. Arahkan pointer ke sel Approval Rule baris aset `Monitor Samsung 24 {runId}`
31. Verifikasi hover sel Approval Rule memuat `Need recipient confirmation`
32. Verifikasi hover sel Approval Rule memuat bukti foto yang diminta `Photo at start` dan `Photo at end`
33. Klik `[Select]`
34. Verifikasi kolom Confirmation Rule baris aset `Monitor Samsung 24 {runId}` bernilai `No`
35. Verifikasi kolom Approval Rule baris aset `Monitor Samsung 24 {runId}` bernilai `Needs approval`
36. Isi Purpose baris aset `Monitor Samsung 24 {runId}` dengan `Pemakaian tim desain`
37. Klik `[Submit]`
38. Klik `[Submit]` pada dialog `Submit Assignment`

### Send email notifications OFF tidak mengirim email event Assignment
39. Approver `Anton Pratama {runId}` membuka daftar notifikasinya
40. Verifikasi notifikasi `assignment_waiting_approval` untuk pengajuan `Citra Lestari {runId}` tercatat
41. Verifikasi tidak ada email notifikasi untuk pengajuan `Citra Lestari {runId}` di kotak masuk Approver `Anton Pratama {runId}` dalam 5 detik sejak notifikasi in-app tercatat

### Photo at start, Photo at end, dan Allowed assignee tercermin di dialog Transaction Rules
42. Total Control `Fajar Nugroho {runId}` membuka tab Transactions di halaman Transactions > Assignment
43. Ketik Search `Citra Lestari {runId}`, tekan Enter
44. Buka Assignment Detail ASG milik Assignee `Citra Lestari {runId}`
45. Klik aksi `Transaction Rules` pada baris aset `Monitor Samsung 24 {runId}`
46. Verifikasi dialog `Transaction Rules` memuat `Photo at start` `ON` dan `Photo at end` `ON` untuk aset `Monitor Samsung 24 {runId}`
47. Verifikasi dialog `Transaction Rules` memuat `Need recipient confirmation` `No` dan Approval `Needs approval` untuk aset `Monitor Samsung 24 {runId}`
48. Verifikasi dialog `Transaction Rules` memuat `Allowed assignee` yang hanya mengizinkan Employee untuk aset `Monitor Samsung 24 {runId}`
49. Tutup dialog `Transaction Rules`

### Allowed assignee Division OFF menandai aset untuk Assignee Division
50. Buka halaman Transactions > Assignment
51. Klik `[+ Assign]`
52. Klik `Division` pada overlay `Assign to`
53. Klik `[+ Asset]`
54. Ketik Search `Proyektor Epson EB-X06 {runId}`, tekan Enter
55. Pilih baris aset `Proyektor Epson EB-X06 {runId}`
56. Klik `[Select]`
57. Klik `[Select Assignee]`
58. Ketik Search `Divisi Desain {runId}`, tekan Enter
59. Pilih baris `Divisi Desain {runId}`
60. Klik `[Select]`
61. Verifikasi ikon ⚠ pada baris aset `Proyektor Epson EB-X06 {runId}` membawa alasan `This asset can't be assigned to a division.`
62. Klik `[+ Asset]`
63. Ketik Search `Scanner Canon LiDE 300 {runId}`, tekan Enter
64. Verifikasi baris aset `Scanner Canon LiDE 300 {runId}` di dialog Select Asset berstatus Eligibility `Not ready` dengan alasan `This asset can't be assigned to a division.`
65. Klik `[Cancel]` pada dialog Select Asset
66. Klik `[Cancel]` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Transaction timeout berlaku untuk baris Waiting for Handover dan tidak untuk Draft
67. Job penutupan otomatis Transaction timeout berjalan
68. Buka tab History di halaman Transactions > Assignment
69. Buka sub-tab By Asset
70. Ketik Search `Speaker JBL Flip 6 {runId}`, tekan Enter
71. Klik aksi `Assignment Log` pada baris aset `Speaker JBL Flip 6 {runId}`
72. Verifikasi node `Canceled by [Actor]` dengan pelaku `System` dan Reason `Not handed over` tampil untuk aset `Speaker JBL Flip 6 {runId}`
73. Tutup dialog `Assignment Log`
74. Buka tab Drafts di halaman Transactions > Assignment
75. Ketik Search `Webcam Logitech C920 {runId}`, tekan Enter
76. Verifikasi Draft untuk aset `Webcam Logitech C920 {runId}` tetap tampil di tab Drafts setelah batas Transaction timeout terlewati

### Send email notifications ON mengirim email event Assignment
77. Total Control `Fajar Nugroho {runId}` membuka Settings > Transaction Settings, tab `Assign`
78. Ubah `Send email notifications` menjadi `ON`
79. Simpan perubahan Transaction Settings
80. Buka tab Transactions di halaman Transactions > Assignment
81. Ketik Search `Citra Lestari {runId}`, tekan Enter
82. Klik `⋯` pada baris ASG milik Assignee `Citra Lestari {runId}`
83. Klik `Cancel Assignment`
84. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
85. Approver `Anton Pratama {runId}` membuka daftar notifikasinya
86. Verifikasi email notifikasi event `assignment_canceled` untuk ASG milik `Citra Lestari {runId}` diterima di kotak masuk Approver `Anton Pratama {runId}`
