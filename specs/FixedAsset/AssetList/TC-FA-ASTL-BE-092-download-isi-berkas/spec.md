---
id: TC-FA-ASTL-BE-092-download-isi-berkas
title: "Isi berkas Download"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-10t, ASTL-LOGIC-10u, ASTL-LOGIC-10v, ASTL-LOGIC-11m, EC-15, "§9.2#p4", EB-DL-4, EB-DL-5]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-10t: [5, 6]
  ASTL-LOGIC-10u: 7
  ASTL-LOGIC-10v: [3, 4]
  ASTL-LOGIC-11m: 10
  EC-15: 27
  "§9.2#p4": [5, 9, 18]
  EB-DL-4: [3, 4, 8, 11, 12, 13, 14, 16, 21, 24]
  EB-DL-5: 27
anchor: []
---

# Isi berkas Download

## Prerequisites
- Aktor: pemegang Manage purchase (Rina), pemegang Manage asset & TAG dengan Read (Budi).
- Data:
  - DU-092-1: User, pemegang Manage purchase di IT dan Read di GA: Name `Rina Maharani {runId}`, Role `Manage purchase pada IT {runId}, Manage asset & TAG (Read) pada GA {runId}`.
  - DU-092-2: User, pemegang Manage asset & TAG Read di IT tanpa kapabilitas lain: Name `Budi Santoso {runId}`, Role `Manage asset & TAG (Read) pada IT {runId}`.
  - DU-092-3: Group, group IT di bawah Head Office dan group GA: Name `Head Office {runId}`, Anak `IT {runId}`, Group lain `GA {runId}`.
  - DU-092-4: Asset, aset lengkap dengan garansi ganda dan empat label: Name `Laptop Pro 16 - 1 {runId}`, Group `Head Office {runId} > IT {runId}`, Purchase Date `T0 - 30 hari`, Purchase Cost `Rp 18.500.000,00`, Warranty 1 `Garansi Pabrik {runId} berakhir T0 + 200 hari`, Warranty 2 `Garansi Tambahan {runId} berakhir T0 + 400 hari`, Label 1 `Prioritas {runId}`, Label 2 `Inventaris Kantor {runId}`, Label 3 `Garansi {runId}`, Label 4 `Cadangan {runId}`, Foto `ada`, Nomor PO `PO-2025-001`, Kode Anggaran `AGR-77`.
  - DU-092-5: Asset, aset kedua dengan Purchase Cost lebih kecil untuk sort: Name `Laptop Pro 16 - 2 {runId}`, Group `Head Office {runId} > IT {runId}`, Purchase Date `T0 - 20 hari`, Purchase Cost `Rp 9.000.000,00`.
  - DU-092-6: Asset, aset dengan data Purchase belum diisi: Name `Switch Jaringan - 1 {runId}`, Group `Head Office {runId} > IT {runId}`, Status Purchase `Pending`, Warranty Expiry `kosong`.
  - DU-092-7: Asset, aset di group tanpa hak Purchase bagi Rina: Name `Meja Rapat - 1 {runId}`, Group `GA {runId}`, Purchase Date `T0 - 10 hari`, Purchase Cost `Rp 4.000.000,00`.
  - DU-092-8: Asset, volume aset untuk Download lebih dari 5.000 baris: Name `Aset Volume {n} {runId}`, Group `Head Office {runId} > IT {runId}`, Lifecycle `Active`, Jumlah baris volume `5001`.
  - DU-092-11: Setup Column, kolom yang tampil bagi Rina: `Name`, `Group`, `Purchase Date`, `Purchase Cost`, `Asset Value`, `Warranty`, `Warranty Expiry`, `Labels`, `Nomor PO`, dan `Kode Anggaran`.
  - DU-092-12: Setup Column, kolom yang tampil bagi Budi: `Name`, `Group`, `Nomor PO`, dan `Kode Anggaran`.
  - DU-092-13: Custom field, dua kolom custom field: `Nomor PO` di grup Purchasing dan `Kode Anggaran` di grup Accounting; Rina memegang Manage purchase pada `IT {runId}` tetapi tidak memegang Manage accounting, Budi tidak memegang keduanya.
- Kondisi: Date Format bernilai `dd/MM/yy`.

## Test Steps

### Sel dalam berkas mengikuti hak pemanggil
1. Rina mencari `{runId}`
2. Rina mengunduh daftar aset sebagai CSV
3. Verifikasi baris `Laptop Pro 16 - 1 {runId}` pada berkas CSV menulis Purchase Cost `18500000` sebagai nilai numerik asli, tanpa simbol mata uang dan tanpa pemisah ribuan
4. Verifikasi baris `Laptop Pro 16 - 1 {runId}` menulis Purchase Date `T0 - 30 hari` dalam Date Format `dd/MM/yy`
5. Verifikasi baris `Laptop Pro 16 - 1 {runId}` menulis Asset Value `No access`, karena Rina tidak memegang `View asset value`
6. Verifikasi baris `Meja Rapat - 1 {runId}` menulis Purchase Date dan Purchase Cost `No access`, bukan nilai aslinya
7. Verifikasi sel Purchase Date dan Purchase Cost baris `Switch Jaringan - 1 {runId}` kosong, bukan `-` dan bukan `Pending`
8. Verifikasi sel Warranty Expiry baris `Switch Jaringan - 1 {runId}` yang tidak berisi nilai ditulis `-`
9. Verifikasi kolom custom field Purchasing `Nomor PO` ikut dengan nilai `PO-2025-001` pada baris `Laptop Pro 16 - 1 {runId}`, dan kolom custom field Accounting `Kode Anggaran` tidak ikut karena Rina tidak berhak

### Isi sel per tipe kolom
10. Verifikasi sel Garansi baris `Laptop Pro 16 - 1 {runId}` menulis seluruh garansi dalam satu sel: `Garansi Pabrik {runId} (T0 + 200 hari); Garansi Tambahan {runId} (T0 + 400 hari)` tanpa warna
11. Verifikasi sel label baris `Laptop Pro 16 - 1 {runId}` menulis seluruh empat label `Prioritas {runId}, Inventaris Kantor {runId}, Garansi {runId}, Cadangan {runId}` dipisah `", "` tanpa terpotong menjadi `+N more`
12. Verifikasi sel Group baris `Laptop Pro 16 - 1 {runId}` menulis hierarki penuh dari root `Head Office {runId} > IT {runId}`
13. Verifikasi berkas tidak memuat kolom foto
14. Verifikasi berkas CSV berenkode UTF-8 dengan BOM
15. Rina mengunduh daftar aset sebagai XLSX
16. Verifikasi berkas XLSX berisi satu sheet bernama `Sheet1`

### Kolom bergerbang tanpa hak tidak ikut
17. Budi mengunduh daftar aset
18. Verifikasi berkas Budi tidak memuat kolom custom field Purchasing `Nomor PO` maupun kolom custom field Accounting `Kode Anggaran`

### Urutan baris mengikuti sort aktif
19. Rina mengurutkan kolom Purchase Cost secara ascending
20. Rina mengunduh daftar aset
21. Verifikasi urutan baris berkas sama dengan urutan sort aktif: `Laptop Pro 16 - 2 {runId}` sebelum `Laptop Pro 16 - 1 {runId}`

### Nol baris menghasilkan berkas berisi header saja
22. Rina mencari `Zebra Tidak Ada {runId}`
23. Rina mengunduh daftar aset
24. Verifikasi berkas hanya berisi baris header kolom yang visible, tanpa baris data

### Download lebih dari 5.000 baris tetap utuh
25. Rina mencari `Aset Volume {runId}`
26. Rina mengunduh daftar aset sebagai CSV
27. Verifikasi berkas memuat seluruh `5001` baris data aset volume tanpa terpotong dan tanpa job di latar belakang
