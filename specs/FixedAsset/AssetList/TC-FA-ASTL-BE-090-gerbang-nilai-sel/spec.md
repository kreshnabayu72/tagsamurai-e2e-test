---
id: TC-FA-ASTL-BE-090-gerbang-nilai-sel
title: "Gerbang nilai sel sensitif"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-10a, ASTL-LOGIC-10b, ASTL-LOGIC-10m, ASTL-LOGIC-10q, ASTL-LOGIC-10r, ASTL-LOGIC-10s, EC-26, EC-13, F-ASTL-06.k1, F-ASTL-09, "§9.4.3#p2", "§9.3#r7"]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-10a: [2, 3, 7, 32, 33, 35]
  ASTL-LOGIC-10b: [2, 3, 4, 7, 32, 33, 35]
  ASTL-LOGIC-10m: [5, 9]
  ASTL-LOGIC-10q: [12, 14]
  ASTL-LOGIC-10r: [16, 18]
  ASTL-LOGIC-10s: [20, 22, 24, 26, 28]
  EC-26: 8
  EC-13: [14, 18, 22, 26, 30]
  F-ASTL-06.k1: 30
  F-ASTL-09: [2, 3]
  "§9.4.3#p2": [5, 9]
  "§9.3#r7": [5, 9, 30, 33, 35]
anchor: []
---

# Gerbang nilai sel sensitif

## Prerequisites
- Aktor: pemegang Manage purchase (Rina), pemegang Manage asset & TAG dengan Read (Budi).
- Data:
  - DU-090-1: User, pemegang Manage purchase di IT dan Read di GA: Name `Rina Maharani {runId}`, Role `Manage purchase pada IT {runId}, Manage asset & TAG (Read) pada GA {runId}`.
  - DU-090-2: User, pemegang Manage asset & TAG Read di IT tanpa kapabilitas lain: Name `Budi Santoso {runId}`, Role `Manage asset & TAG (Read) pada IT {runId}`.
  - DU-090-3: Group, dua group tanpa induk: Name `IT {runId}`, Group lain `GA {runId}`.
  - DU-090-4: Asset, aset dengan data Purchase lengkap dan garansi: Name `Laptop Pro 16 - 1 {runId}`, Group `IT {runId}`, Purchase Date `T0 - 30 hari`, Purchase Cost `Rp 18.500.000,00`, Warranty Expiry `T0 + 200 hari`, Asset Class `Peralatan Kantor`, Tax Depreciation Class `Kelompok 2`, Nomor PO `PO-2025-0417`, Kode Anggaran `ANG-2025-11`.
  - DU-090-5: Asset, aset kedua dengan Purchase Cost berbeda untuk sort: Name `Laptop Pro 16 - 2 {runId}`, Group `IT {runId}`, Purchase Date `T0 - 20 hari`, Purchase Cost `Rp 9.000.000,00`, Asset Class `Peralatan Kantor`.
  - DU-090-6: Asset, aset dengan data Purchase belum diisi: Name `Switch Jaringan - 1 {runId}`, Group `IT {runId}`, Status Purchase `Pending`, Asset Class `Peralatan Jaringan`.
  - DU-090-7: Asset, aset di group tanpa hak Purchase bagi Rina: Name `Meja Rapat - 1 {runId}`, Group `GA {runId}`, Purchase Date `T0 - 10 hari`, Purchase Cost `Rp 4.000.000,00`, Nomor PO `PO-2025-0502`, Kode Anggaran `ANG-2025-12`.
  - DU-090-9: Custom field, dua kolom custom field tampil di Setup Column Rina dan Budi: `Nomor PO` grup Purchasing dan `Kode Anggaran` grup Accounting; Rina tidak memegang Manage accounting.
- Kondisi: Date Format bernilai `dd/MM/yy`.

## Test Steps

### Pemegang Manage purchase membaca sel Purchase, sel lain tanpa hak No access
1. Rina meminta daftar aset
2. Verifikasi baris `Laptop Pro 16 - 1 {runId}` menampilkan Purchase Date `T0 - 30 hari`, Purchase Cost `Rp 18.500.000,00`, dan Warranty Expiry `T0 + 200 hari` karena Rina berhak atas group `IT {runId}`
3. Verifikasi baris `Laptop Pro 16 - 1 {runId}` menampilkan Asset Value dan Tax Depreciation Class `No access` karena Rina tidak memegang `View asset value` maupun `Manage accounting`
4. Verifikasi baris `Switch Jaringan - 1 {runId}` menampilkan Purchase Date dan Purchase Cost `Pending` karena Rina berhak dan data Purchase belum diisi
5. Verifikasi baris `Meja Rapat - 1 {runId}` di group `GA {runId}` menampilkan Purchase Date dan Purchase Cost `No access`, dan respons tidak memuat nilai `Rp 4.000.000,00`

### Pemanggil tanpa hak tidak diberi tahu bahwa data belum diisi
6. Budi meminta daftar aset
7. Verifikasi baris `Laptop Pro 16 - 1 {runId}` menampilkan Asset Value, Tax Depreciation Class, Purchase Date, Purchase Cost, dan Warranty Expiry `No access`
8. Verifikasi baris `Switch Jaringan - 1 {runId}` menampilkan Purchase Date dan Purchase Cost `No access`, bukan `Pending`
9. Verifikasi respons untuk Budi tidak memuat nilai `Rp 18.500.000,00` maupun `Rp 9.000.000,00` pada sel mana pun

### Sort menempatkan No access paling akhir dan Pending tepat sebelumnya
10. Rina mencari `{runId}`
11. Rina mengurutkan kolom Purchase Cost secara ascending
12. Verifikasi urutan baris adalah `Laptop Pro 16 - 2 {runId}`, `Laptop Pro 16 - 1 {runId}`, `Switch Jaringan - 1 {runId}` yang `Pending`, lalu `Meja Rapat - 1 {runId}` yang `No access`
13. Rina mengurutkan kolom Purchase Cost secara descending
14. Verifikasi urutan baris adalah `Laptop Pro 16 - 1 {runId}`, `Laptop Pro 16 - 2 {runId}`, `Switch Jaringan - 1 {runId}` yang `Pending`, lalu `Meja Rapat - 1 {runId}` yang `No access`, sehingga `No access` tetap paling akhir pada kedua arah

### Filter tidak mencocokkan baris No access dan Pending
15. Rina memfilter kolom Purchase Cost dari `5000000.00` sampai `20000000.00`
16. Verifikasi hasil filter memuat `Laptop Pro 16 - 1 {runId}` dan `Laptop Pro 16 - 2 {runId}`, dan tidak memuat `Switch Jaringan - 1 {runId}` yang `Pending` maupun `Meja Rapat - 1 {runId}` yang `No access`
17. Rina memfilter kolom Asset Value dari `0.00` sampai `100000000.00`
18. Verifikasi hasil filter tidak memuat `Laptop Pro 16 - 1 {runId}` karena sel Asset Value Rina `No access`

### Search tidak mencocokkan sel No access dan Pending
19. Rina mencari `18.500.000`
20. Verifikasi hasil pencarian memuat `Laptop Pro 16 - 1 {runId}` lewat sel Purchase Cost yang berhak dibaca Rina
21. Rina mencari `4.000.000,00`
22. Verifikasi hasil pencarian tidak memuat `Meja Rapat - 1 {runId}` karena sel Purchase Cost-nya `No access`
23. Rina mencari `Pending`
24. Verifikasi hasil pencarian tidak memuat `Switch Jaringan - 1 {runId}` karena sel `Pending` tidak cocok dengan teksnya
25. Rina mencari `No access`
26. Verifikasi hasil pencarian tidak memuat `Meja Rapat - 1 {runId}` karena sel `No access` tidak cocok dengan teksnya
27. Budi mencari `18.500.000`
28. Verifikasi hasil pencarian tidak memuat `Laptop Pro 16 - 1 {runId}` karena sel Purchase Cost Budi `No access`

### Download tidak membocorkan nilai sel No access
29. Rina mengunduh daftar aset
30. Verifikasi isi berkas Download tidak memuat nilai `Rp 4.000.000,00` milik sel `No access` pada `Meja Rapat - 1 {runId}` dan tidak memuat nilai Asset Value apa pun

### Kolom custom field Purchasing dan Accounting mengikuti hak
31. Rina meminta daftar aset dengan kolom `Nomor PO` dan `Kode Anggaran` tampil
32. Verifikasi baris `Laptop Pro 16 - 1 {runId}` menampilkan `Nomor PO` `PO-2025-0417` karena Rina memegang Manage purchase pada `IT {runId}`, dan `Kode Anggaran` `No access` karena Rina tidak memegang Manage accounting
33. Verifikasi baris `Meja Rapat - 1 {runId}` menampilkan `Nomor PO` dan `Kode Anggaran` `No access`, dan respons untuk Rina tidak memuat nilai `PO-2025-0502`, `ANG-2025-12`, maupun `ANG-2025-11`
34. Budi meminta daftar aset dengan kolom `Nomor PO` dan `Kode Anggaran` tampil
35. Verifikasi baris `Laptop Pro 16 - 1 {runId}` menampilkan `Nomor PO` dan `Kode Anggaran` `No access`, dan respons untuk Budi tidak memuat nilai `PO-2025-0417` maupun `ANG-2025-11`
