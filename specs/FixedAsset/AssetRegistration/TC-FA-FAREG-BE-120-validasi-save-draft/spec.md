---
id: TC-FA-FAREG-BE-120-validasi-save-draft
title: "Validasi Save draft dan autosave"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: [F-FAREG-01.k1, FAREG-LOGIC-01c, FAREG-LOGIC-01q, FAREG-LOGIC-03q, FAREG-LOGIC-03t, FAREG-LOGIC-03w, FAREG-LOGIC-10g, FAREG-LOGIC-17b, FLD-REG-02, V-REG-01, V-REG-10, "§9.2#p3", "§9.4.2#r4", "§9.4.3#b1", "§9.5#r10", "§9.6#r1", "§9.6#r2", "§9.9#r5", "§9.9#r6"]
smoke: []
dependsOn: []
trace:
  F-FAREG-01.k1: [15, 16, 33, 34]
  FAREG-LOGIC-01c: [9, 10, 22, 26, 27]
  FAREG-LOGIC-01q: [36, 37]
  FAREG-LOGIC-03q: [15, 20, 33]
  FAREG-LOGIC-03t: [29, 30]
  FAREG-LOGIC-03w: [13, 15, 20, 33]
  FAREG-LOGIC-10g: [59, 60, 61, 63, 65, 67, 69, 71]
  FAREG-LOGIC-17b: [47, 48]
  FLD-REG-02: [50, 51, 52]
  V-REG-01: [3]
  V-REG-10: [7, 13, 15]
  "§9.2#p3": [7, 23, 24]
  "§9.4.2#r4": [15, 33]
  "§9.4.3#b1": [22, 26]
  "§9.5#r10": [50, 51, 52, 54, 56]
  "§9.6#r1": [41, 42]
  "§9.6#r2": [44, 45]
  "§9.9#r5": [4]
  "§9.9#r6": [7, 13, 18, 20]
owner: BE
---

# Validasi Save draft dan autosave

## Prerequisites
- Aktor: Rina (Manage asset & TAG, Group terkelola `Gudang Cikarang {runId}` dan `Gudang Bekasi {runId}`); Siti (Manage asset & TAG, Group terkelola `Gudang Cikarang {runId}` saja); Dewi (Group Manager, Group binaan `Gudang Bekasi {runId}`).
- Data:
  - DU-120-1: Group `Gudang Cikarang {runId}`, Assignable, di entitas aktor.
  - DU-120-2: Group `Gudang Bekasi {runId}`, Assignable, di entitas aktor.
  - DU-120-3: Asset Name `Laptop {runId}`, Category `IT Equipment` (node terbawah), Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`, status `Active`, Custom field `Serial Number` bertipe Specific dan tidak wajib.
  - DU-120-4: Asset Name `Printer Lama {runId}`, Category `IT Equipment`, Brand `HP`, Model `LaserJet Pro`, status `Inactive`.
  - DU-120-5: Asset Name `Mesin CNC {runId}`, Category `Mesin Produksi`, Brand `Haas`, Model `VF-2`, berstatus Locked dari Registrasi Aset.
  - DU-120-6: Asset Name `Meja Kerja {runId}`, Category `Furnitur`, Brand `Olympic`, Model `OL-120`, TAG Type `Non-TAG`, status `Active`.
  - DU-120-7: Asset Name `Kursi Kantor {runId}`, Category `Furnitur`, Brand `Chitose`, Model `Orion`, TAG Type `Non-TAG`, status `Active`.
  - DU-120-8: batch Draft milik Rina, Group `Gudang Cikarang {runId}`, satu aset `Laptop {runId}` ber-Tag RFID `E280-1200-0001 {runId}` berstatus `To be Returned` dengan Return Group `Gudang Cikarang {runId}`, Quantity `1`, Owner `Rina`.
  - DU-120-9: batch Draft kembalian milik Rina, Group `Gudang Cikarang {runId}`, Asset Name `Meja Kerja {runId}`, Quantity `2`, Asset Code aset `MJK-2026-0001`, Origin `REG-20261108-00011`.
- Kondisi:
  - Register Asset Bulk Limit bernilai `100`.
  - Approval Workflow tidak aktif untuk `Gudang Cikarang {runId}`.

## Test Steps

### Save draft tanpa Group ditolak
1. Rina mencatat jumlah batch Draft miliknya
2. Rina mengirim Save draft tanpa Group dengan satu Item Asset Name `Laptop {runId}`, Quantity `1`
3. Verifikasi Save draft ditolak server dengan pesan `Group must not be empty`
4. Verifikasi jumlah batch Draft milik Rina sama dengan catatan langkah 1

### Quantity nol dan Damage note terlalu panjang ditolak
5. Rina mencatat jumlah batch Draft miliknya
6. Rina mengirim Save draft dengan Group `Gudang Cikarang {runId}`, Asset Name `Laptop {runId}`, Quantity `0`
7. Verifikasi Save draft ditolak server dengan pesan `Quantity must be between 1 and 100`
8. Rina mengirim Save draft dengan Group `Gudang Cikarang {runId}`, Asset Name `Laptop {runId}`, Condition `Damaged`, Damage note `Layar retak di sudut kiri atas dan engsel penutup patah sehingga laptop tidak layak dipakai bekerja di lapangan saat ini.` (121 karakter)
9. Verifikasi Save draft ditolak server dengan pesan `Max. 120 characters`
10. Verifikasi jumlah batch Draft milik Rina sama dengan catatan langkah 5

### Register Asset Bulk Limit dievaluasi pada Save draft
11. Rina mencatat jumlah batch Draft miliknya
12. Rina mengirim Save draft dengan Group `Gudang Cikarang {runId}`, Asset Name `Laptop {runId}`, Quantity `101`
13. Verifikasi Save draft ditolak server dengan pesan `Quantity must be between 1 and 100`
14. Rina mengirim Save draft dengan Group `Gudang Cikarang {runId}`, Item 1 Asset Name `Laptop {runId}` Quantity `60`, Item 2 Asset Name `Meja Kerja {runId}` Quantity `41`
15. Verifikasi Save draft ditolak server dengan pesan `For more than 100 assets, use Import.`
16. Verifikasi jumlah batch Draft milik Rina sama dengan catatan langkah 11
17. Rina mengirim Save draft dengan Group `Gudang Cikarang {runId}`, Asset Name `Laptop {runId}`, Quantity `99`
18. Verifikasi Save draft berhasil dan Quantity tersimpan `99`
19. Rina mengirim Save draft dengan Group `Gudang Cikarang {runId}`, Asset Name `Laptop {runId}`, Quantity `100`
20. Verifikasi Save draft berhasil dan Quantity tersimpan `100`

### Save draft tidak diblokir field Tingkat 2 dan 3 yang kosong
21. Rina mengirim Save draft dengan Group `Gudang Cikarang {runId}` dan satu Item tanpa Asset Name, Brand, Model, Alias Name, dan Foto, tanpa mengisi Quantity dan Condition
22. Verifikasi Save draft berhasil dan batch Draft Group `Gudang Cikarang {runId}` tersimpan
23. Verifikasi Quantity Item tersimpan `1`
24. Verifikasi Condition Item tersimpan `Normal`
25. Rina mengirim Save draft dengan Group `Gudang Cikarang {runId}`, Asset Name `Laptop {runId}`, Condition `Damaged`, tanpa Damage note
26. Verifikasi Save draft berhasil
27. Verifikasi Condition aset tersimpan `Damaged` tanpa Damage note

### Item tanpa Asset Name tidak dihitung ke Bulk Limit
28. Rina mengirim Save draft dengan Group `Gudang Cikarang {runId}`, Item 1 tanpa Asset Name Quantity `100`, Item 2 Asset Name `Laptop {runId}` Quantity `100`
29. Verifikasi Save draft berhasil walau jumlah Quantity kedua Item melebihi Register Asset Bulk Limit
30. Verifikasi baris Item tanpa Asset Name tersimpan dengan Quantity `100`

### Submit melebihi Bulk Limit ditolak
31. Rina mencatat jumlah batch Draft dan jumlah pengajuan miliknya
32. Rina mengirim Submit dengan Group `Gudang Cikarang {runId}`, Item 1 Asset Name `Meja Kerja {runId}` Brand `Olympic` Model `OL-120` Quantity `70`, Item 2 Asset Name `Kursi Kantor {runId}` Brand `Chitose` Model `Orion` Quantity `31`
33. Verifikasi Submit ditolak server dengan pesan `For more than 100 assets, use Import.`
34. Verifikasi jumlah batch Draft dan jumlah pengajuan milik Rina sama dengan catatan langkah 31

### Autosave menjalankan pemeriksaan yang sama dengan Save draft
35. Rina mengirim autosave atas batch Draft dari langkah 19 dengan Quantity `101`
36. Verifikasi autosave ditolak server dengan pemeriksaan Bulk Limit yang sama dengan Save draft
37. Verifikasi Quantity batch Draft dari langkah 19 tetap `100`

### Save draft menambah batch pada setiap pengiriman dan autosave tidak
38. Rina mencatat jumlah batch Draft miliknya
39. Rina mengirim Save draft dari form baru dengan Group `Gudang Cikarang {runId}`, Asset Name `Laptop {runId}`, Quantity `1`
40. Rina mengirim Save draft dari form baru lain dengan Group `Gudang Cikarang {runId}`, Asset Name `Laptop {runId}`, Quantity `1`
41. Verifikasi jumlah batch Draft milik Rina bertambah dua dari catatan langkah 38
42. Verifikasi aset batch kedua memakai nomor increment sementara lebih besar daripada aset batch pertama
43. Rina mengirim autosave dengan isi yang sama atas batch pertama dua kali berturut-turut
44. Verifikasi jumlah batch Draft milik Rina tetap bertambah dua dari catatan langkah 38
45. Verifikasi isi batch pertama sama dengan isi sebelum autosave

### Nilai Custom field per aset tidak harus unik
46. Rina mengirim Save draft dengan Group `Gudang Cikarang {runId}`, Asset Name `Laptop {runId}`, Quantity `2`, Serial Number kedua aset `SN-LAP {runId}`
47. Verifikasi Save draft berhasil
48. Verifikasi kedua aset tersimpan dengan Serial Number `SN-LAP {runId}`

### Opsi selector hanya dari master Asset Name aktif
49. Rina meminta opsi Asset Name untuk form registrasi
50. Verifikasi opsi memuat `Laptop {runId}` yang terikat Category node terbawah `IT Equipment`
51. Verifikasi opsi tidak memuat `Printer Lama {runId}`
52. Verifikasi opsi tidak memuat `Mesin CNC {runId}`
53. Rina meminta opsi Brand untuk Asset Name `Laptop {runId}`
54. Verifikasi opsi Brand memuat `Dell`
55. Rina meminta opsi Model untuk Brand `Dell`
56. Verifikasi opsi Model memuat `Latitude 5440`

### Penggantian Group draft melepas Tag dan memindahkan hak ubah
57. Rina membuka batch Draft `Gudang Cikarang {runId}` yang berisi aset `Laptop {runId}` ber-Tag `E280-1200-0001 {runId}` hingga memegang kunci sesinya
58. Rina mengirim Save draft atas batch itu dengan Group diganti menjadi `Gudang Bekasi {runId}`
59. Verifikasi slot Tag RFID aset itu `Unverified`
60. Verifikasi Tag `E280-1200-0001 {runId}` tidak lagi terpasang pada aset itu
61. Verifikasi hasil Save draft memuat peringatan bahwa Tag dilepas
62. Siti mengirim Save draft atas batch itu dengan Alias Name `Laptop Rapat {runId}`
63. Verifikasi Save draft dari Siti ditolak tanpa mutasi dengan pesan `You don't have permission to do this.`
64. Siti meminta Take over kunci sesi batch itu
65. Verifikasi Take over dari Siti ditolak dan kunci sesi tetap dipegang Rina
66. Dewi meminta Take over kunci sesi batch itu
67. Verifikasi kunci sesi batch itu dipegang Dewi
68. Dewi mengirim Save draft atas batch itu dengan Alias Name `Laptop Direksi {runId}`
69. Verifikasi Save draft dari Dewi berhasil

### Group batch kembalian tidak dapat diganti
70. Rina mengirim permintaan mengganti Group batch Draft kembalian dengan Asset Code `MJK-2026-0001` menjadi `Gudang Bekasi {runId}`
71. Verifikasi Group batch kembalian tetap `Gudang Cikarang {runId}`
