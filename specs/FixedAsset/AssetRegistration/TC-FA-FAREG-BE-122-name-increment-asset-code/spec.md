---
id: TC-FA-FAREG-BE-122-name-increment-asset-code
title: "Name sementara, increment, dan Asset Code"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [FAREG-LOGIC-03b, FAREG-LOGIC-03e, FAREG-LOGIC-03f, FAREG-LOGIC-03g, FAREG-LOGIC-03h, FAREG-LOGIC-03i, FAREG-LOGIC-03r, FAREG-LOGIC-03s, FAREG-LOGIC-03v, "§9.4.3#b3"]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-03b: [2, 8, 47]
  FAREG-LOGIC-03e: [5, 7]
  FAREG-LOGIC-03f: [12, 14, 15, 19, 22]
  FAREG-LOGIC-03g: [40, 41]
  FAREG-LOGIC-03h: [23, 24, 25, 51, 52, 58, 59]
  FAREG-LOGIC-03i: [26, 36, 37, 40]
  FAREG-LOGIC-03r: [10, 17, 21, 42, 76]
  FAREG-LOGIC-03s: [24, 25, 28, 29, 30, 32, 52, 53, 54, 60, 61, 62, 64, 65, 67, 68, 70, 71]
  FAREG-LOGIC-03v: [73, 74, 75]
  "§9.4.3#b3": [19, 22, 32, 40, 41]
owner: BE
---

# Name sementara, increment, dan Asset Code

## Prerequisites
- Aktor: Rina (Manage asset & TAG, Group terkelola `Gudang Malang {runId}` dan `Gudang Tanpa Divisi {runId}`, pengaju); Dewi (Manage asset & TAG, Group terkelola `Gudang Malang {runId}`); Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Malang {runId}` dan `Gudang Tanpa Divisi {runId}`, bukan pengaju, approver).
- Data:
  - DU-122-1: Group `Gudang Malang {runId}`, Assignable, di entitas aktor.
  - DU-122-2: Asset Name `Meja Kerja {runId}`, Category `Furnitur`, Brand `Olympic`, Model `OL-122` dan `OL-123`, TAG Type `Non-TAG`.
  - DU-122-3: Asset Name `Kursi Kantor {runId}`, Category `Furnitur`, Brand `Chitose`, Model `Orion`, TAG Type `Non-TAG`.
  - DU-122-4: Asset Name `Lemari Arsip {runId}`, Category `Furnitur`, Brand `Alba`, Model `AR-12`, TAG Type `Non-TAG`.
  - DU-122-5: Asset Name `Rak Besi {runId}`, Category `Furnitur`, Brand `Krisbow`, Model `RB-4`, TAG Type `Non-TAG`.
  - DU-122-6: batch Draft milik Dewi, Group `Gudang Malang {runId}`, satu aset `Meja Kerja {runId}` Brand `Olympic` Model `OL-122`, Tingkat 2 lengkap.
  - DU-122-7: batch Draft milik Rina, Group `Gudang Malang {runId}`, empat Item dengan Tingkat 2 lengkap: `Meja Kerja {runId}` Brand `Olympic` Model `OL-122` Quantity `3`; `Kursi Kantor {runId}` Brand `Chitose` Model `Orion` Quantity `1`; `Lemari Arsip {runId}` Brand `Alba` Model `AR-12` Quantity `1`; `Rak Besi {runId}` Brand `Krisbow` Model `RB-4` Quantity `1`.
  - DU-122-8: batch Draft milik Rina, Group `Gudang Malang {runId}`, satu aset `Meja Kerja {runId}` Brand `Olympic` Model `OL-122`, Tingkat 2 lengkap.
  - DU-122-15: batch Draft milik Rina, Group `Gudang Malang {runId}`, satu aset `Lemari Arsip {runId}` Brand `Alba` Model `AR-12`, Tingkat 2 lengkap.
  - DU-122-16: Asset Name `Laptop {runId}`, Category `IT Equipment`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID` (satu slot Tag).
  - DU-122-17: Asset Name `Server Mini {runId}`, Category `IT Equipment`, Brand `HPE`, Model `ML30`, TAG Type `RFID` (satu slot Tag).
  - DU-122-18: Group `Gudang Tanpa Divisi {runId}`, Assignable, tanpa Division Code, dengan toggle `Require Approval for Registration` ON, di entitas aktor.
  - DU-122-19: Asset Name `Kursi Tanpa Akun {runId}`, Category `Furnitur`, Brand `Chitose`, Model `Orion`, TAG Type `Non-TAG`, tanpa Account Code.
  - DU-122-20: batch Draft milik Rina, Group `Gudang Malang {runId}`, satu aset `Laptop {runId}` Brand `Dell` Model `Latitude 5440` Quantity `1` ber-Tag RFID `E280-1220-0001 {runId}`, Tingkat 2 lengkap.
  - DU-122-21: Tag RFID `E280-1220-0001 {runId}`, status `Reserved` atas aset batch DU-122-20.
  - DU-122-22: batch Draft milik Rina, Group `Gudang Malang {runId}`, dua Item dengan Tingkat 2 lengkap: Item 1 `Laptop {runId}` Brand `Dell` Model `Latitude 5440` Quantity `2` dengan aset pertama ber-Tag RFID `E280-1220-0002 {runId}` dan aset kedua ber-Tag RFID `E280-1220-0003 {runId}`; Item 2 `Server Mini {runId}` Brand `HPE` Model `ML30` Quantity `1` ber-Tag RFID `E280-1220-0004 {runId}`.
  - DU-122-23: Tag RFID `E280-1220-0002 {runId}`, status `Reserved` atas aset pertama Item `Laptop {runId}` batch DU-122-22.
  - DU-122-24: Tag RFID `E280-1220-0003 {runId}`, status `Reserved` atas aset kedua Item `Laptop {runId}` batch DU-122-22.
  - DU-122-25: Tag RFID `E280-1220-0004 {runId}`, status `Reserved` atas aset Item `Server Mini {runId}` batch DU-122-22.
- Kondisi:
  - Approval Workflow aktif untuk `Gudang Malang {runId}` dengan toggle `Require Approval for Registration` ON.
  - Kuota tenant dan kuota Group `Gudang Malang {runId}` mencukupi untuk seluruh aset yang diajukan spec ini.
  - Pola Asset Code memuat segmen Division Code dan Account Code.

## Test Steps

### Name sementara berurutan dan bergeser saat aset lain Submit lebih dulu
1. Rina mengirim Save draft dengan Group `Gudang Malang {runId}`, Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-122`, Quantity `2`
2. Verifikasi kedua aset batch bernama sementara berformat Asset Name - increment dengan Asset Name `Meja Kerja {runId}` dan nomor increment berurutan
3. Rina mencatat nomor increment sementara kedua aset
4. Dewi mengirim Submit atas batch DU-122-6
5. Verifikasi aset batch DU-122-6 berstatus Waiting for Approval
6. Rina membuka ulang batch Draft dari langkah 1
7. Verifikasi nomor increment sementara kedua aset lebih besar daripada catatan langkah 3
8. Verifikasi nomor increment sementara kedua aset tetap berurutan dan lebih besar daripada nomor increment aset batch DU-122-6 yang sudah Waiting for Approval

### Mengganti Asset Name pada Draft menghitung ulang Name sementara
9. Rina mengirim Save draft atas batch Draft dari langkah 1 dengan Asset Name diganti menjadi `Kursi Kantor {runId}`, Brand `Chitose`, Model `Orion`
10. Verifikasi Name sementara kedua aset kini memakai Asset Name `Kursi Kantor {runId}` dengan nomor increment berurutan

### Asset Code dan increment dialokasikan saat Activate dan terkunci sejak Waiting for Approval
11. Rina membuka batch DU-122-7
12. Verifikasi keenam aset batch DU-122-7 belum memiliki Asset Code
13. Rina mengirim Submit atas batch DU-122-7
14. Verifikasi keenam aset berstatus Waiting for Approval
15. Verifikasi setiap aset memiliki Asset Code dan nomor increment yang sudah teralokasi
16. Rina mencatat Asset Code, nomor increment, dan Name keenam aset
17. Verifikasi nomor increment pada Name dan nomor Asset Code tersimpan sebagai dua nilai terpisah pada setiap aset
18. Budi menyimpan koreksi Model aset `Meja Kerja {runId}` pertama menjadi `OL-123`
19. Verifikasi Asset Code dan nomor increment keenam aset sama dengan catatan langkah 16

### Keputusan campuran mempertahankan atau membuang increment
20. Budi mengirim keputusan: aset `Meja Kerja {runId}` pertama `Approve`; aset `Meja Kerja {runId}` kedua dan ketiga, aset `Kursi Kantor {runId}`, dan aset `Lemari Arsip {runId}` `Return to Draft` dengan Reason `Warna meja tidak cocok`; aset `Rak Besi {runId}` `Reject` dengan Reason `Rak berkarat di sisi kanan`
21. Verifikasi aset `Meja Kerja {runId}` yang di-Approve berstatus Active dengan Name sama dengan catatan langkah 16
22. Verifikasi Asset Code dan nomor increment aset yang di-Approve sama dengan catatan langkah 16 walau Model berubah menjadi `OL-123`
23. Verifikasi keempat aset Return to Draft berada di satu batch Draft baru milik Rina
24. Verifikasi Name Draft keempat aset memakai nomor increment yang sama dengan catatan langkah 16
25. Verifikasi Asset Code dan nomor increment keempat aset Return to Draft sama dengan catatan langkah 16
26. Verifikasi Asset Code aset `Rak Besi {runId}` yang di-Reject berstatus `Voided`

### Quantity turun pada aset ber-Asset Code memvoid kodenya
27. Rina menurunkan Quantity Item `Meja Kerja {runId}` pada batch Draft baru dari `2` menjadi `1`
28. Verifikasi aset `Meja Kerja {runId}` dengan nomor increment terbesar dihapus dari batch
29. Verifikasi Asset Code aset yang dihapus berstatus `Voided`
30. Verifikasi aset `Meja Kerja {runId}` yang tersisa tetap memiliki Asset Code dan nomor increment sama dengan catatan langkah 16

### Submit ulang aset kembalian memakai kode yang sama
31. Rina mengirim Submit atas batch Draft baru yang berisi tiga aset tersisa
32. Verifikasi Asset Code dan nomor increment ketiga aset sama dengan catatan langkah 16 tanpa alokasi baru

### Pembatalan dengan aset dibuang tidak memakai ulang increment
33. Rina mengirim Submit atas batch DU-122-8
34. Rina mencatat Asset Code dan nomor increment aset batch DU-122-8
35. Rina membatalkan pengajuan batch DU-122-8 dengan `Save as Draft to edit` tidak dicentang
36. Verifikasi aset batch DU-122-8 dibuang
37. Verifikasi Asset Code aset yang dibuang berstatus `Voided`

### Increment tidak pernah dipakai ulang
38. Rina mengirim Save draft dengan Group `Gudang Malang {runId}`, Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-122`, Quantity `1`
39. Rina mengirim Submit atas batch Draft dari langkah 38
40. Verifikasi nomor increment aset itu tidak sama dengan nomor increment aset yang di-Reject, yang di-Voided oleh Quantity turun, maupun yang dibuang lewat Cancel
41. Verifikasi nomor increment aset itu lebih besar daripada seluruh nomor increment yang tercatat di langkah 16 dan langkah 34

### Increment sekuensial lintas Asset Name dan batch, dan dasar hitung aset Active
42. Verifikasi nomor increment keenam aset batch DU-122-7 sama dengan catatan langkah 16, berbeda satu sama lain, dan semuanya lebih besar daripada nomor increment aset batch DU-122-6 lintas Asset Name `Meja Kerja {runId}`, `Kursi Kantor {runId}`, `Lemari Arsip {runId}`, dan `Rak Besi {runId}`
43. Rina mengirim Submit atas batch DU-122-15
44. Budi mengirim keputusan `Approve` untuk aset batch DU-122-15
45. Rina mencatat nomor increment aset batch DU-122-15 yang Active
46. Rina mengirim Save draft dengan Group `Gudang Malang {runId}`, Asset Name `Kursi Kantor {runId}`, Brand `Chitose`, Model `Orion`, Quantity `1`
47. Verifikasi nomor increment sementara aset batch Draft dari langkah 46 lebih besar daripada catatan langkah 45

### Pembatalan dengan Save as Draft to edit mempertahankan kode, increment, dan Tag Reserved
48. Rina mengirim Submit atas batch DU-122-20
49. Rina mencatat Asset Code dan nomor increment aset batch DU-122-20
50. Rina membatalkan pengajuan batch DU-122-20 dengan `Save as Draft to edit` dicentang
51. Verifikasi aset batch DU-122-20 kembali ke batch Draft baru milik Rina
52. Verifikasi Asset Code dan nomor increment aset sama dengan catatan langkah 49
53. Verifikasi Name Draft aset memakai nomor increment yang sama dengan catatan langkah 49
54. Verifikasi Tag `E280-1220-0001 {runId}` tetap `Reserved` atas aset itu

### Return to Draft mempertahankan Tag Reserved
55. Rina mengirim Submit atas batch DU-122-22
56. Rina mencatat Asset Code dan nomor increment ketiga aset batch DU-122-22
57. Budi mengirim keputusan `Return to Draft` untuk ketiga aset batch DU-122-22 dengan Reason `Foto belum jelas`
58. Verifikasi ketiga aset berada di satu batch Draft baru milik Rina
59. Verifikasi Asset Code dan nomor increment ketiga aset sama dengan catatan langkah 56
60. Verifikasi Tag `E280-1220-0002 {runId}` tetap `Reserved` atas aset pertama Item `Laptop {runId}`
61. Verifikasi Tag `E280-1220-0003 {runId}` tetap `Reserved` atas aset kedua Item `Laptop {runId}`
62. Verifikasi Tag `E280-1220-0004 {runId}` tetap `Reserved` atas aset Item `Server Mini {runId}`

### Quantity turun, Remove Item, dan Delete pada aset ber-Tag memvoid kode dan melepas Tag
63. Rina menurunkan Quantity Item `Laptop {runId}` pada batch Draft dari langkah 58 dari `2` menjadi `1`
64. Verifikasi Asset Code aset kedua Item `Laptop {runId}` berstatus `Voided`
65. Verifikasi Tag `E280-1220-0003 {runId}` berstatus `Available`
66. Rina menghapus Item `Server Mini {runId}` dari batch Draft itu dengan Remove Item
67. Verifikasi Asset Code aset Item `Server Mini {runId}` berstatus `Voided`
68. Verifikasi Tag `E280-1220-0004 {runId}` berstatus `Available`
69. Rina menghapus batch Draft itu dengan Delete
70. Verifikasi Asset Code aset pertama Item `Laptop {runId}` berstatus `Voided`
71. Verifikasi Tag `E280-1220-0002 {runId}` berstatus `Available`

### Segmen Asset Code yang tidak tersedia memakai 0000
72. Rina mengirim Submit dengan Group `Gudang Tanpa Divisi {runId}`, Asset Name `Kursi Tanpa Akun {runId}`, Brand `Chitose`, Model `Orion`, Quantity `1`
73. Verifikasi Submit diterima dan aset berstatus Waiting for Approval
74. Verifikasi Asset Code aset memuat `0000` pada segmen Division Code
75. Verifikasi Asset Code aset memuat `0000` pada segmen Account Code

### Increment sekuensial lintas Group
76. Verifikasi nomor increment aset dari langkah 72 pada Group `Gudang Tanpa Divisi {runId}` lebih besar daripada seluruh nomor increment yang tercatat di langkah 16 pada Group `Gudang Malang {runId}`
