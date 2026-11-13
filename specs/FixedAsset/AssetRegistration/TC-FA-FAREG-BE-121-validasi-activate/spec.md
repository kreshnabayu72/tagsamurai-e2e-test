---
id: TC-FA-FAREG-BE-121-validasi-activate
title: "Validasi Activate: Tingkat 2, Skip pairing, dan transaksi tunggal"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [F-FAREG-05.k2, FAREG-LOGIC-01d, FAREG-LOGIC-01e, FAREG-LOGIC-01i, FAREG-LOGIC-01n, FAREG-LOGIC-01o, FAREG-LOGIC-01p, FAREG-LOGIC-04k, FAREG-LOGIC-04l, FAREG-LOGIC-09a, FAREG-LOGIC-11a, FAREG-LOGIC-11c, FAREG-LOGIC-15h, FLD-REG-09, V-REG-03, V-REG-11, V-REG-12, V-REG-13, "§6#b1", "§9.4.2#r12", "§9.4.3#b10", "§9.6#r3", "§9.9#r2", "§9.9#r3", "§9.9#r4", "§9.9#r8", "§9.9#r9", "§9.9#r10", "§9.9#r11", EB-ERR-4]
smoke: []
dependsOn: []
trace:
  F-FAREG-05.k2: [8, 9, 46, 47]
  FAREG-LOGIC-01d: [3, 4, 5]
  FAREG-LOGIC-01e: [30, 31]
  FAREG-LOGIC-01i: [8, 9]
  FAREG-LOGIC-01n: [14, 15, 16, 26, 46, 47, 48]
  FAREG-LOGIC-01o: [10, 11, 38, 52, 54, 55]
  FAREG-LOGIC-01p: [40, 42, 51]
  FAREG-LOGIC-04k: [23]
  FAREG-LOGIC-04l: [24]
  FAREG-LOGIC-09a: [27]
  FAREG-LOGIC-11a: [56, 57, 58, 59, 68]
  FAREG-LOGIC-11c: [3, 4, 5, 6, 7]
  FAREG-LOGIC-15h: [28, 56, 66, 67]
  FLD-REG-09: [14, 25, 63, 64]
  V-REG-03: [6]
  V-REG-11: [18]
  V-REG-12: [20]
  V-REG-13: [14]
  "§6#b1": [27, 29]
  "§9.4.2#r12": [27]
  "§9.4.3#b10": [27]
  "§9.6#r3": [8, 34, 35, 36, 60]
  "§9.9#r2": [3]
  "§9.9#r3": [4]
  "§9.9#r4": [5]
  "§9.9#r8": [6]
  "§9.9#r9": [18]
  "§9.9#r10": [20]
  "§9.9#r11": [7]
  EB-ERR-4: [11, 21]
owner: BE
---

# Validasi Activate: Tingkat 2, Skip pairing, dan transaksi tunggal

## Prerequisites
- Aktor: Rina (Manage asset & TAG, Group terkelola `Gudang Surabaya {runId}`); Dewi (Manage asset & TAG, Group terkelola `Gudang Surabaya {runId}`); Hana T (Total Control, mengubah master Asset Name).
- Data:
  - DU-121-1: Group `Gudang Surabaya {runId}`, Assignable, di entitas aktor.
  - DU-121-2: Asset Name `Meja Kerja {runId}`, Category `Furnitur`, Brand `Olympic`, Model `OL-121`, TAG Type `Non-TAG`, tanpa Asset Class, dengan Custom field kelompok Purchase wajib `Nomor Invoice`.
  - DU-121-3: Asset Name `Kursi Kantor {runId}`, Category `Furnitur`, Brand `Chitose`, Model `Orion`, TAG Type `Non-TAG`.
  - DU-121-4: Asset Name `Lemari Arsip {runId}`, Category `Furnitur`, Brand `Alba`, Model `AR-12`, TAG Type `Non-TAG`.
  - DU-121-5: Asset Name `Rak Besi {runId}`, Category `Furnitur`, Brand `Krisbow`, Model `RB-4`, TAG Type `Non-TAG`, dengan Custom field Specific Asset Name wajib `Material`.
  - DU-121-6: Asset Name `Bangku Lab {runId}`, Category `Furnitur`, Brand `Lab Pro`, Model `BL-1`, TAG Type `Non-TAG`.
  - DU-121-7: Asset Name `Laptop {runId}`, Category `IT Equipment`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`.
  - DU-121-8: Asset Name `Pot Bunga {runId}`, Category `Furnitur`, TAG Type `Non-TAG`, tanpa Brand terkait di master.
  - DU-121-9: batch Draft milik Rina, Group `Gudang Surabaya {runId}`, enam Item: Item 1 `Meja Kerja {runId}` Brand `Olympic` Model `OL-121` Quantity `2` lengkap; Item 2 tanpa Asset Name Quantity `1`; Item 3 `Kursi Kantor {runId}` tanpa Brand dan Model Quantity `1`; Item 4 `Lemari Arsip {runId}` Brand `Alba` tanpa Model Quantity `1`; Item 5 `Rak Besi {runId}` Brand `Krisbow` Model `RB-4` dengan Material kosong Quantity `1`; Item 6 `Bangku Lab {runId}` Brand `Lab Pro` Model `BL-1` Condition `Damaged` tanpa Damage note Quantity `1`.
  - DU-121-10: batch Draft milik Rina, Group `Gudang Surabaya {runId}`, Item 1 `Laptop {runId}` Brand `Dell` Model `Latitude 5440` Quantity `3` dengan aset pertama ber-Tag RFID `E280-1210-0001 {runId}` dan dua aset lain belum ber-Tag, Item 2 `Meja Kerja {runId}` Brand `Olympic` Model `OL-121` Quantity `1`, Tingkat 3 kosong.
  - DU-121-20: Asset Name `Perangkat Ukur {runId}`, Category `Peralatan Lapangan`, Brand `Leica`, Model `TS16`, TAG Type `RFID` dan `NFC` (dua slot Tag).
  - DU-121-21: Asset Name `Rak Warna {runId}`, Category `Furnitur`, Brand `Krisbow`, Model `RW-1`, TAG Type `Non-TAG`, dengan Custom field Specific Asset Name opsional `Warna` (tidak wajib).
  - DU-121-22: Tag RFID `E280-1210-0201 {runId}`, status `Available`.
  - DU-121-23: batch Draft milik Rina, Group `Gudang Surabaya {runId}`, satu Item `Perangkat Ukur {runId}` Brand `Leica` Model `TS16` Quantity `1`, Tingkat 2 lengkap selain Tag; slot RFID terverifikasi dengan Tag `E280-1210-0201 {runId}` dan slot NFC kosong.
  - DU-121-24: batch Draft milik Rina, Group `Gudang Surabaya {runId}`, empat Item Quantity `1`: Item 1 `Meja Kerja {runId}` Brand `Olympic` Model `OL-121` dengan Alias Name `Meja Rapat {runId}`, Photo dan Asset labels kosong, Custom field Purchase `Nomor Invoice` kosong; Item 2 `Rak Warna {runId}` Brand `Krisbow` Model `RW-1` dengan Alias Name, Photo, Asset labels, dan `Warna` kosong; Item 3 `Laptop {runId}` Brand `Dell` Model `Latitude 5440` tanpa Tag dengan Alias Name, Photo, dan Asset labels kosong; Item 4 `Rak Besi {runId}` Brand `Krisbow` Model `RB-4` dengan `Material` `Baja` dan Alias Name `Rak Gudang {runId}`, Photo dan Asset labels kosong.
  - DU-121-25: batch Draft milik Rina, Group `Gudang Surabaya {runId}`, satu Item `Kursi Kantor {runId}` Brand `Chitose` Model `Orion` Quantity `1`, Tingkat 2 lengkap.
- Kondisi:
  - Approval Workflow tidak aktif untuk `Gudang Surabaya {runId}`.
  - Kuota tenant dan kuota Group `Gudang Surabaya {runId}` mencukupi untuk seluruh aset yang diaktifkan spec ini.

## Test Steps

### Activate ditolak seluruhnya bila ada aset belum memenuhi Tingkat 2
1. Rina mencatat jumlah pengajuan miliknya
2. Rina mengirim Submit atas batch DU-121-9 dengan Alias Name `Meja Eksekutif {runId}` ditambahkan pada Item `Meja Kerja {runId}`
3. Verifikasi Submit ditolak server dengan pesan `Asset Name must not be empty`
4. Verifikasi Submit ditolak server dengan pesan `Brand must not be empty`
5. Verifikasi Submit ditolak server dengan pesan `Model must not be empty`
6. Verifikasi Submit ditolak server dengan pesan `Damage note must not be empty`
7. Verifikasi Submit ditolak server dengan pesan `Material must not be empty`
8. Verifikasi seluruh aset batch tetap Draft, termasuk aset `Meja Kerja {runId}` yang sudah lengkap
9. Verifikasi jumlah pengajuan milik Rina sama dengan catatan langkah 1
10. Verifikasi Alias Name `Meja Eksekutif {runId}` tidak tersimpan pada batch
11. Verifikasi seluruh data batch sama dengan keadaan sebelum Submit

### Skip pairing menentukan Activate aset yang hanya kurang Tag
12. Rina mencatat jumlah pengajuan miliknya
13. Rina mengirim Activate atas batch DU-121-10 dengan Skip pairing tidak dicentang
14. Verifikasi Activate ditolak server dengan pesan `Choose to submit without pairing, or pair the TAGs first.`
15. Verifikasi seluruh aset batch tetap Draft, termasuk aset `Laptop {runId}` yang sudah ber-Tag
16. Verifikasi jumlah pengajuan milik Rina sama dengan catatan langkah 12
17. Rina mengirim Activate atas batch DU-121-10 dengan Skip pairing dicentang tanpa memilih Reason
18. Verifikasi Activate ditolak server dengan pesan `You must pick a reason`
19. Rina mengirim Activate atas batch DU-121-10 dengan Skip pairing dicentang, Reason `Other`, tanpa Note
20. Verifikasi Activate ditolak server dengan pesan `Note must not be empty`
21. Verifikasi seluruh aset batch tetap Draft sesudah kedua penolakan Skip pairing
22. Rina mengirim Activate atas batch DU-121-10 dengan Skip pairing dicentang dan Reason `TAG not yet available`
23. Verifikasi Activate diterima untuk aset yang hanya kurang Tag
24. Verifikasi kedua aset `Laptop {runId}` tanpa Tag tercatat `Not Paired Yet`
25. Verifikasi aset `Meja Kerja {runId}` bertipe `Non-TAG` diterima tanpa Tag dan tanpa Skip pairing
26. Verifikasi seluruh aset batch berstatus Active dalam satu transaksi
27. Verifikasi aset `Meja Kerja {runId}` berstatus Active walau Asset Name tanpa Asset Class
28. Verifikasi aset `Meja Kerja {runId}` berstatus Active walau Custom field kelompok Purchase `Nomor Invoice` kosong
29. Verifikasi hasil Activate tidak memuat peringatan Asset Class
30. Verifikasi Activate diterima walau Alias Name, Foto, dan Asset labels kosong
31. Verifikasi skor kelengkapan aset `Meja Kerja {runId}` kurang dari `100`

### Activate kedua atas batch yang sudah Active ditolak
32. Rina mencatat Asset Code aset batch DU-121-10 dan kuota Used Group `Gudang Surabaya {runId}`
33. Rina mengirim Activate sekali lagi atas batch DU-121-10 dengan Skip pairing dicentang dan Reason `TAG not yet available`
34. Verifikasi Activate kedua ditolak server karena batch tidak lagi berstatus Draft
35. Verifikasi Asset Code aset batch sama dengan catatan langkah 32
36. Verifikasi kuota Used Group sama dengan catatan langkah 32

### Submit dari form baru menyimpan lalu mengaktifkan
37. Rina mengirim Submit dari form baru dengan Group `Gudang Surabaya {runId}`, Asset Name `Kursi Kantor {runId}`, Brand `Chitose`, Model `Orion`, Quantity `2`
38. Verifikasi batch Draft tercipta lalu kedua aset `Kursi Kantor {runId}` berstatus Active dalam satu transaksi

### Asset Name tanpa Brand di master memblokir Activate
39. Rina mengirim Save draft dengan Group `Gudang Surabaya {runId}`, Asset Name `Pot Bunga {runId}`, Quantity `1`
40. Verifikasi Save draft Item `Pot Bunga {runId}` tanpa Brand di master berhasil
41. Rina mengirim Activate atas batch Draft dari langkah 39
42. Verifikasi Activate ditolak server

### Tag direbut sesi lain menolak seluruh Submit
43. Rina mencatat jumlah batch Draft dan jumlah pengajuan miliknya
44. Dewi mengirim Save draft dari form baru dengan Group `Gudang Surabaya {runId}`, Asset Name `Laptop {runId}`, Quantity `1`, Tag RFID `E280-1210-0102 {runId}` sehingga Tag itu Reserved atas aset Dewi
45. Rina mengirim Submit dari form baru dengan Group `Gudang Surabaya {runId}`, Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, Quantity `2`, Tag RFID aset 1 `E280-1210-0101 {runId}`, Tag RFID aset 2 `E280-1210-0102 {runId}`
46. Verifikasi Submit ditolak server untuk Tag `E280-1210-0102 {runId}` dengan pesan `E280-1210-0102 {runId} is no longer available. Scan another TAG.`
47. Verifikasi jumlah batch Draft dan jumlah pengajuan milik Rina sama dengan catatan langkah 43
48. Verifikasi Tag `E280-1210-0101 {runId}` tidak Reserved atas aset milik Rina

### Activate menerima aset sesudah master Brand dilengkapi
49. Hana T menambahkan Brand `Terracotta` dengan Model `TC-1` pada Asset Name `Pot Bunga {runId}`
50. Rina mengirim Activate atas batch Draft dari langkah 39 dengan Brand `Terracotta` dan Model `TC-1`
51. Verifikasi Activate diterima dan aset `Pot Bunga {runId}` berstatus Active

### Submit dari form baru mencatat Draft created
52. Verifikasi Registration Log batch dari langkah 37 memuat entri `Draft created by Rina` dengan Total Asset `2`

### Submit atas batch yang ada menyimpan perubahan form sebelum mengaktifkan
53. Rina mengirim Submit atas batch DU-121-25 dengan Quantity Item `Kursi Kantor {runId}` diubah menjadi `3` dan belum tersimpan
54. Verifikasi Quantity Item `Kursi Kantor {runId}` batch DU-121-25 tersimpan `3`
55. Verifikasi ketiga aset `Kursi Kantor {runId}` batch DU-121-25 berstatus Active dalam satu transaksi

### Skor kelengkapan dihitung dari field yang berlaku
56. Verifikasi skor kelengkapan aset `Meja Kerja {runId}` batch DU-121-24 adalah `75`, dari 6 field terisi dari 8 field yang berlaku, tanpa Custom field Purchase `Nomor Invoice` dan tanpa Custom field Specific Asset Name milik Asset Name lain dalam hitungan
57. Verifikasi skor kelengkapan aset `Rak Warna {runId}` batch DU-121-24 adalah `56`, dari 5 field terisi dari 9 field yang berlaku, dengan Custom field Specific Asset Name opsional `Warna` yang kosong dalam hitungan
58. Verifikasi skor kelengkapan aset `Laptop {runId}` batch DU-121-24 adalah `56`, dari 5 field terisi dari 9 field yang berlaku, dengan slot Tag RFID `Unverified` dihitung kosong
59. Verifikasi skor kelengkapan aset kedua `Laptop {runId}` batch DU-121-10 adalah `67`, dari 6 field terisi dari 9 field yang berlaku, dengan slot Tag RFID `Skipped` dihitung terisi

### Activate mengalokasikan Asset Code
60. Verifikasi setiap aset batch DU-121-10 memiliki Asset Code yang dialokasikan saat Activate pada langkah 22

### Activate ditolak bila sebagian slot Tag belum terverifikasi
61. Rina mencatat jumlah pengajuan miliknya
62. Rina mengirim Activate atas batch DU-121-23 dengan Skip pairing tidak dicentang
63. Verifikasi Activate ditolak server karena slot Tag NFC belum terverifikasi
64. Verifikasi aset batch DU-121-23 tetap Draft dan jumlah pengajuan milik Rina sama dengan catatan langkah 61

### Custom field Purchase tidak ditampilkan di form registrasi
65. Rina meminta data batch DU-121-24 lewat form registrasi
66. Verifikasi respons form memuat Asset Name `Meja Kerja {runId}`, Brand `Olympic`, dan Model `OL-121` untuk aset itu
67. Verifikasi respons form untuk aset `Meja Kerja {runId}` tidak memuat Custom field kelompok Purchase `Nomor Invoice`

### Skor kelengkapan menghitung Custom field wajib milik Asset Name
68. Verifikasi skor kelengkapan aset `Rak Besi {runId}` batch DU-121-24 adalah `78`, dari 7 field terisi dari 9 field yang berlaku, dengan Custom field Specific Asset Name wajib `Material` yang terisi dalam hitungan
