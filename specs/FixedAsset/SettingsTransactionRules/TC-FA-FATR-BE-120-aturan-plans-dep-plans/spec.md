---
id: TC-FA-FATR-BE-120-aturan-plans-dep-plans
title: "Perubahan plan terhadap setting tersimpan"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§8.1#r5", "§9.2#b556", "§9.2#b558", "§9.2#b559", "§9.4.2#r54", "§9.4.3#b8", "§9.4.4#r55", "§9.4.4#r57", "§9.4.4#r58", "§9.8#r15", "§9.10.1#r7", "§9.10.2#r8", "§9.10.3#r7", "§9.10.4#b3", "§11#r2", "§9.10.1#b9", "§9.10.2#b7", "§9.10.3#b2"]
smoke: []
dependsOn:
  - "Admin Console: Plans & Features"
trace:
  "§9.10.1#r7": [1, 27]
  "§11#r2": [1, 8, 16, 27]
  "§9.10.2#r8": [2, 27]
  "§9.10.3#r7": [3, 27]
  "§9.2#b556": 7
  "§9.4.4#r55": [7, 10, 11]
  "§8.1#r5": [7, 15, 22, 28]
  "§9.4.3#b8": [7, 11, 15, 19, 22, 24]
  "§9.8#r15": [7, 15, 22, 28]
  "§9.4.2#r54": [8, 10, 16, 18]
  "§9.2#b558": 15
  "§9.4.4#r57": [15, 18, 19]
  "§9.2#b559": 22
  "§9.4.4#r58": [22, 24]
  "§9.10.4#b3": [30, 32, 34, 36, 38, 41]
  "§9.10.1#b9": [7, 10, 11]
  "§9.10.2#b7": [15, 18, 19]
  "§9.10.3#b2": [22, 24]
---

# Perubahan plan terhadap setting tersimpan

## Prerequisites
- Aktor: Total Control. Operator di luar tenant, hanya untuk mengubah plan entitas.
- Data:
  - DU-120-1: entitas khusus `Entitas Plan Transaksi {runId}`, tidak dipakai spec lain; semua data di bawah ada di entitas ini. Entitas memakai plan kustom DU-120-15 pada awal spec.
  - DU-120-15: plan kustom `Plan Rank 2 {runId}`, salinan default plan awal `Paid (rank 2)` (Approval Workflow `Yes`, Borrowing `Full`, Assignment `Full`), dipakai entitas DU-120-1 saja.
  - DU-120-16: plan kustom `Plan Rank 1 {runId}`, salinan default plan awal `Paid (rank 1)` (Approval Workflow `No`, Borrowing `Basic`, Assignment `Basic`), dipakai entitas DU-120-1 saja saat plan diturunkan.
  - DU-120-2: Group `Grup Dasar {n} {runId}`, 3 Group yang lebih lama.
  - DU-120-3: Group `Grup Excess {runId}`, dibuat sesudah Group dasar.
  - DU-120-4: Category `Kategori Dasar {n} {runId}`, 20 Category yang lebih lama.
  - DU-120-5: Category `Kategori Excess {runId}`, dibuat sesudah Category dasar.
  - DU-120-6: Asset Name `Nama Aset Dasar {n} {runId}`, 50 Asset Name yang lebih lama.
  - DU-120-7: Asset Name `Nama Aset Excess {runId}`, dibuat sesudah Asset Name dasar.
  - DU-120-8: aset `Aset Excess Unit 1 {runId}` ber-Asset Name `Nama Aset Excess {runId}`, di Category `Kategori Dasar 1 {runId}` yang Max duration-nya mewarisi Company default `14`, dan di Group `Grup Dasar 1 {runId}`.
  - DU-120-9: Require approval bernilai `ON`.
  - DU-120-10: Self service bernilai `ON`.
  - DU-120-14: pengajuan pinjam selama `10` Days.
- Kondisi:
  - Max duration bernilai `14` di Company default untuk transaksi pinjam.
  - Entitas memakai plan kustom `Plan Rank 2 {runId}` miliknya sendiri, tidak dipakai entitas lain dan bukan slot `Paid (rank 2)` bersama, sehingga perubahan Approval Workflow dan level Feature Suite pada plan itu hanya mengubah entitas ini.
  - Nilai `Plan Rank 2 {runId}` sama dengan default plan awal `Paid (rank 2)`, dan nilai `Plan Rank 1 {runId}` sama dengan default plan awal `Paid (rank 1)`.

## Test Steps

### Halaman membaca nilai default plan awal Paid (rank 2)
1. Verifikasi pada plan `Plan Rank 2 {runId}` Approval Workflow tersedia, sesuai nilai default plan awal `Paid (rank 2)` yang dibaca halaman dari plan entitas[^drift-1]
2. Verifikasi pada plan `Plan Rank 2 {runId}` level Feature Suite Borrowing adalah `Full`, sesuai nilai default plan awal `Paid (rank 2)`, sehingga Self service dan Duration unit Hours tersedia
3. Verifikasi pada plan `Plan Rank 2 {runId}` level Feature Suite Assignment adalah `Full`, sesuai nilai default plan awal `Paid (rank 2)`

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
20. Catat jumlah entri Changelog Transaction Settings
21. Operator mengubah level Feature Suite Assignment pada plan entitas menjadi `Basic`
22. Verifikasi Changelog Transaction Settings tidak bertambah oleh perubahan level Feature Suite Assignment
23. Operator mengubah level Feature Suite Assignment pada plan entitas kembali menjadi `Full`
24. Verifikasi Changelog Transaction Settings tetap tidak bertambah sesudah level Assignment kembali `Full`

### Plan turun ke Plan Rank 1 dan status excess pada masa Grace tidak membatasi setting dan override
25. Catat jumlah entri Changelog Transaction Settings
26. Operator menurunkan plan entitas ke plan kustom `Plan Rank 1 {runId}`, sehingga Group `Grup Excess {runId}`, Category `Kategori Excess {runId}`, dan Asset Name `Nama Aset Excess {runId}` berstatus excess pada masa Grace
27. Verifikasi pada plan `Plan Rank 1 {runId}` Approval Workflow tidak tersedia, level Borrowing `Basic`, dan level Assignment `Basic`, sesuai nilai default plan awal `Paid (rank 1)`[^drift-1]
28. Verifikasi Changelog Transaction Settings tidak bertambah oleh penurunan plan
29. Total Control menyimpan Max duration bernilai `9` untuk Category `Kategori Excess {runId}`
30. Verifikasi Save Max duration `9` untuk Category excess `Kategori Excess {runId}` diterima karena Save tidak memeriksa status excess
31. Total Control menambah override pada transaksi pinjam All categories dengan target Group excess `Grup Excess {runId}`, field `Max duration` bernilai `5`
32. Verifikasi Add override dengan target Group excess `Grup Excess {runId}` diterima karena Add override tidak memeriksa status excess
33. Total Control menambah override pada transaksi pinjam All categories dengan target Asset Name excess `Nama Aset Excess {runId}`, field `Max duration` bernilai `5`
34. Verifikasi Add override dengan target Asset Name excess `Nama Aset Excess {runId}` diterima karena Add override tidak memeriksa status excess
35. Total Control mengajukan peminjaman aset `Aset Excess Unit 1 {runId}` selama `10` Days selagi Asset Name `Nama Aset Excess {runId}` berstatus excess
36. Verifikasi pengajuan selama `10` Days ditolak karena override Asset Name excess dengan Max duration `5` dievaluasi seperti biasa
37. Total Control menghapus override target Group excess `Grup Excess {runId}`
38. Verifikasi Delete override dengan target Group excess `Grup Excess {runId}` berhasil karena Delete tidak memeriksa status excess
39. Operator menaikkan plan entitas kembali ke plan kustom `Plan Rank 2 {runId}`, sehingga status excess dilepas
40. Total Control mengajukan peminjaman aset `Aset Excess Unit 1 {runId}` selama `10` Days sesudah status excess dilepas
41. Verifikasi pengajuan selama `10` Days tetap ditolak oleh override Asset Name `Nama Aset Excess {runId}` dengan Max duration `5`, sehingga evaluasi tidak berubah saat status excess dilepas

[^drift-1]: Drift PRD vs foundation. PRD §9.10.1, §9.10.2, dan §9.10.3 (tabel level per plan): kolom plan memakai slot `free`, `paid_1`, `paid_2`, dan `paid_3`. foundation `plans.md` §2.2: kolom plan adalah slot `Free (rank 0)`, `Paid (rank 1)`, `Paid (rank 2)`, dan `Paid (rank 3)` dengan nilai default plan awal per slot (Approval Workflow: No, No, Yes, Yes; Borrowing dan Assignment: None, Basic, Full, Full). Diasersi: foundation, karena plan adalah pola bersama platform; `free`, `paid_1`, `paid_2`, dan `paid_3` dibaca sebagai slot rank 0 sampai 3 (SB-4).
