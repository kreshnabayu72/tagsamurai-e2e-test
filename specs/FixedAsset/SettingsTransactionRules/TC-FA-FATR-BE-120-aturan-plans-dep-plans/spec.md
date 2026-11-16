---
id: TC-FA-FATR-BE-120-aturan-plans-dep-plans
title: "Perubahan plan terhadap setting tersimpan"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§8.1#r5", "§9.2#b557", "§9.2#b559", "§9.2#b561", "§9.4.2#r54", "§9.4.3#b8", "§9.4.4#r55", "§9.4.4#r57", "§9.4.4#r59", "§9.8#r15", "§9.10.1#r7", "§9.10.2#r8", "§9.10.3#r8", "§9.10.4#b3", "§11#r2"]
smoke: []
dependsOn:
  - "Admin Console: Plans & Features"
trace:
  "§9.10.1#r7": [1, 30]
  "§11#r2": [1, 8, 16, 24, 30]
  "§9.10.2#r8": [2, 30]
  "§9.10.3#r8": [3, 30]
  "§9.2#b557": 7
  "§9.4.4#r55": [7, 10, 11]
  "§8.1#r5": [7, 15, 23, 31]
  "§9.4.3#b8": [7, 11, 15, 19, 23, 27]
  "§9.8#r15": [7, 15, 23, 31]
  "§9.4.2#r54": [8, 10, 16, 18, 24, 26]
  "§9.2#b559": 15
  "§9.4.4#r57": [15, 18, 19]
  "§9.2#b561": 23
  "§9.4.4#r59": [23, 26, 27]
  "§9.10.4#b3": [33, 35, 37, 39, 41, 44]
---

# Perubahan plan terhadap setting tersimpan

## Prerequisites
- Aktor: Total Control. Operator di luar tenant, hanya untuk mengubah plan entitas.
- Data:
  - DU-120-1: entitas khusus `Entitas Plan Transaksi {runId}`, plan `Paid (rank 2)`, tidak dipakai spec lain; semua data di bawah ada di entitas ini.
  - DU-120-2: Group `Grup Dasar {n} {runId}`, 3 Group yang lebih lama.
  - DU-120-3: Group `Grup Excess {runId}`, dibuat sesudah Group dasar.
  - DU-120-4: Category `Kategori Dasar {n} {runId}`, 20 Category yang lebih lama.
  - DU-120-5: Category `Kategori Excess {runId}`, dibuat sesudah Category dasar.
  - DU-120-6: Asset Name `Nama Aset Dasar {n} {runId}`, 50 Asset Name yang lebih lama.
  - DU-120-7: Asset Name `Nama Aset Excess {runId}`, dibuat sesudah Asset Name dasar.
  - DU-120-8: aset `Aset Excess Unit 1 {runId}` ber-Asset Name `Nama Aset Excess {runId}`, di Category `Kategori Dasar 1 {runId}` yang Max duration-nya mewarisi Company default `14`, dan di Group `Grup Dasar 1 {runId}`.
  - DU-120-9: Require approval bernilai `ON`.
  - DU-120-10: Self service bernilai `ON`.
  - DU-120-11: Direct handover between holders bernilai `Allow`.
  - DU-120-12: Max duration `9` untuk Category `Kategori Excess {runId}`.
  - DU-120-13: override transaksi pinjam All categories, target Group `Grup Excess {runId}`, Max duration `5`.
  - DU-120-14: override transaksi pinjam All categories, target Asset Name `Nama Aset Excess {runId}`, Max duration `5`.
  - DU-120-15: pengajuan pinjam selama `10` Days.
- Kondisi:
  - Max duration bernilai `14` di Company default untuk transaksi pinjam.
  - Entitas memakai plan khusus miliknya sendiri, tidak dipakai entitas lain, sehingga perubahan Approval Workflow dan level Feature Suite pada plan itu hanya mengubah entitas ini.
  - Plan `Paid (rank 2)` memakai nilai default plan awal, dan plan `Paid (rank 1)` juga memakai nilai default plan awal.

## Test Steps

### Halaman membaca nilai default plan awal Paid (rank 2)
1. Verifikasi pada plan `Paid (rank 2)` Approval Workflow tersedia, sesuai nilai default plan awal yang dibaca halaman dari plan entitas
2. Verifikasi pada plan `Paid (rank 2)` level Feature Suite Borrowing adalah `Full`, sesuai nilai default plan awal, sehingga Self service dan Duration unit Hours tersedia
3. Verifikasi pada plan `Paid (rank 2)` level Feature Suite Assignment adalah `Full`, sesuai nilai default plan awal, sehingga Direct handover between holders tersedia

### Toggle Approval Workflow bukan perubahan Settings
4. Total Control menyimpan Require approval bernilai `ON` untuk transaksi pinjam di All categories
5. Catat jumlah entri Changelog Transaction Settings
6. Operator mengubah toggle Approval Workflow pada plan entitas menjadi `No`
7. Verifikasi Changelog Transaction Settings tidak bertambah oleh perubahan toggle Approval Workflow
8. Verifikasi nilai efektif Require approval adalah `OFF` selama Approval Workflow `No`, sedangkan nilai tersimpan `ON` dipertahankan
9. Operator mengubah toggle Approval Workflow pada plan entitas kembali menjadi `Yes`
10. Verifikasi nilai tersimpan Require approval `ON` langsung berlaku lagi saat Approval Workflow kembali tersedia
11. Verifikasi Changelog Transaction Settings tetap tidak bertambah sesudah toggle Approval Workflow kembali `Yes`

### Level Feature Suite Borrowing bukan perubahan Settings
12. Total Control menyimpan Self service bernilai `ON` untuk transaksi pinjam di All categories
13. Catat jumlah entri Changelog Transaction Settings
14. Operator mengubah level Feature Suite Borrowing pada plan entitas menjadi `Basic`
15. Verifikasi Changelog Transaction Settings tidak bertambah oleh perubahan level Feature Suite Borrowing
16. Verifikasi nilai efektif Self service adalah `OFF` pada level `Basic`, sedangkan nilai tersimpan `ON` dipertahankan
17. Operator mengubah level Feature Suite Borrowing pada plan entitas kembali menjadi `Full`
18. Verifikasi nilai tersimpan Self service `ON` langsung berlaku lagi saat level kembali `Full`
19. Verifikasi Changelog Transaction Settings tetap tidak bertambah sesudah level Borrowing kembali `Full`

### Level Feature Suite Assignment bukan perubahan Settings
20. Total Control menyimpan Direct handover between holders bernilai `Allow` untuk transaksi serah terima aset di All categories
21. Catat jumlah entri Changelog Transaction Settings
22. Operator mengubah level Feature Suite Assignment pada plan entitas menjadi `Basic`
23. Verifikasi Changelog Transaction Settings tidak bertambah oleh perubahan level Feature Suite Assignment
24. Verifikasi nilai efektif Direct handover between holders adalah `Deny` pada level `Basic`, sedangkan nilai tersimpan `Allow` dipertahankan
25. Operator mengubah level Feature Suite Assignment pada plan entitas kembali menjadi `Full`
26. Verifikasi nilai tersimpan Direct handover between holders `Allow` langsung berlaku lagi saat level kembali `Full`
27. Verifikasi Changelog Transaction Settings tetap tidak bertambah sesudah level Assignment kembali `Full`

### Plan turun ke Paid (rank 1) dan status excess pada masa Grace tidak membatasi setting dan override
28. Catat jumlah entri Changelog Transaction Settings
29. Operator menurunkan plan entitas ke `Paid (rank 1)`, sehingga Group `Grup Excess {runId}`, Category `Kategori Excess {runId}`, dan Asset Name `Nama Aset Excess {runId}` berstatus excess pada masa Grace
30. Verifikasi pada plan `Paid (rank 1)` Approval Workflow tidak tersedia, level Borrowing `Basic`, dan level Assignment `Basic`, sesuai nilai default plan awal
31. Verifikasi Changelog Transaction Settings tidak bertambah oleh penurunan plan
32. Total Control menyimpan Max duration bernilai `9` untuk Category `Kategori Excess {runId}`
33. Verifikasi Save Max duration `9` untuk Category excess `Kategori Excess {runId}` diterima karena Save tidak memeriksa status excess
34. Total Control menambah override pada transaksi pinjam All categories dengan target Group excess `Grup Excess {runId}`, field `Max duration` bernilai `5`
35. Verifikasi Add override dengan target Group excess `Grup Excess {runId}` diterima karena Add override tidak memeriksa status excess
36. Total Control menambah override pada transaksi pinjam All categories dengan target Asset Name excess `Nama Aset Excess {runId}`, field `Max duration` bernilai `5`
37. Verifikasi Add override dengan target Asset Name excess `Nama Aset Excess {runId}` diterima karena Add override tidak memeriksa status excess
38. Total Control mengajukan peminjaman aset `Aset Excess Unit 1 {runId}` selama `10` Days selagi Asset Name `Nama Aset Excess {runId}` berstatus excess
39. Verifikasi pengajuan selama `10` Days ditolak karena override Asset Name excess dengan Max duration `5` dievaluasi seperti biasa
40. Total Control menghapus override target Group excess `Grup Excess {runId}`
41. Verifikasi Delete override dengan target Group excess `Grup Excess {runId}` berhasil karena Delete tidak memeriksa status excess
42. Operator menaikkan plan entitas kembali ke `Paid (rank 2)`, sehingga status excess dilepas
43. Total Control mengajukan peminjaman aset `Aset Excess Unit 1 {runId}` selama `10` Days sesudah status excess dilepas
44. Verifikasi pengajuan selama `10` Days tetap ditolak oleh override Asset Name `Nama Aset Excess {runId}` dengan Max duration `5`, sehingga evaluasi tidak berubah saat status excess dilepas
