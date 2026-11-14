---
id: TC-FA-FATR-E2E-014-overrides-sort
title: "Sort tabel Overrides"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [§4.1#r239, §4.1#r241, §4.1#r242, §4.1#r244, §4.1#r240, §4.1#r243, §5#r4, §9.5#r8, EB-SRT-1, EB-SRT-3@tabel-overrides]
smoke: [EB-SRT-1, EB-SRT-3@tabel-overrides]
dependsOn: []
trace:
  §4.1#r239: [21, 23, 25]
  §4.1#r241: [28, 30]
  §4.1#r242: [32, 34]
  §4.1#r244: [36, 38]
  §4.1#r240: [12, 14, 16]
  §4.1#r243: [8, 10]
  §5#r4: [3, 4]
  §9.5#r8: [4, 19]
  EB-SRT-1: [8, 10, 12, 14]
  EB-SRT-3@tabel-overrides: [19]
anchor: []
coverage:
  web: automated
---

# Sort tabel Overrides

## Prerequisites
- Aktor: Total Control `Rina Wulandari` pada entitas khusus `Entitas Sort Overrides {runId}` (DU-014-1), yang tidak dipakai spec lain.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-014-1: entitas khusus `Entitas Sort Overrides {runId}` dengan aktor bernama Rina Wulandari, Total Control.
  - DU-014-2: Category leaf `Laptop {runId}`.
  - DU-014-3: Category leaf `Machinery {runId}`.
  - DU-014-4: Group tingkat atas `anggur Timur {runId}`.
  - DU-014-5: Group tingkat atas `Apel Barat {runId}`.
  - DU-014-6: Group tingkat atas `Cakra Utara {runId}`.
  - DU-014-7: Group tingkat atas `Zeta Selatan {runId}`.
  - DU-014-8: Group tingkat atas `Bima Tengah {runId}`.
  - DU-014-9: Group tingkat atas `Dharma Pusat {runId}`.
  - DU-014-10: Group tingkat atas `Gudang Kota {runId}`.
  - DU-014-11: Group tingkat atas `Cendana Raya {runId}`.
  - DU-014-12: Group tingkat atas `Mawar Putih {runId}`.
  - DU-014-13: Group tingkat atas `Flamboyan Asri {runId}`.
  - DU-014-14: Asset Name `Excavator PC200 {runId}`, Code `EXC14-{runId}`, Category `Laptop {runId}`, UoM `Unit`.
  - DU-014-15: Asset Name `Toyota Avanza {runId}`, Code `AVZ14-{runId}`, Category `Laptop {runId}`, UoM `Unit`.
  - DU-014-16: user `Budi Santoso`, Total Control, tampil di kolom Created By sebagai `Budi S`.
  - DU-014-17: user `Budi Hartono`, Total Control, tampil di kolom Created By sebagai `Budi H`.
  - DU-014-18: override Group `anggur Timur {runId}` di Category `Laptop {runId}` transaksi `Borrow`, Overridden `Max duration (5 days)`, dibuat oleh `Budi Santoso`, dibuat paling awal.
  - DU-014-19: override Group `Apel Barat {runId}` di Category `Laptop {runId}` transaksi `Borrow`, Overridden `Max duration (6 days)`, dibuat oleh `Budi Santoso`, dibuat berurutan sesudah DU-014-18.
  - DU-014-20: override Group `Cakra Utara {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max duration (7 days)`, dibuat oleh `Budi Santoso`, dibuat berurutan sesudah DU-014-19.
  - DU-014-21: override Asset Name `Excavator PC200 {runId}` di Category `Laptop {runId}` transaksi `Borrow`, Overridden `Max duration (8 days)`, dibuat oleh `Budi Santoso`, dibuat berurutan sesudah DU-014-20.
  - DU-014-22: override Group `Zeta Selatan {runId}` di Category `Laptop {runId}` transaksi `Borrow`, Overridden `Max duration (9 days)`, dibuat oleh `Budi Santoso`, dibuat berurutan sesudah DU-014-21.
  - DU-014-23: override Group `Bima Tengah {runId}` di Category `Laptop {runId}` transaksi `Borrow`, Overridden `Max duration (10 days)`, dibuat oleh `Budi Santoso`, dibuat berurutan sesudah DU-014-22.
  - DU-014-24: override Group `Dharma Pusat {runId}` di Category `Laptop {runId}` transaksi `Borrow`, Overridden `Allow Borrow (Deny)`, dibuat oleh `Budi Santoso`, dibuat berurutan sesudah DU-014-23.
  - DU-014-25: override Asset Name `Toyota Avanza {runId}` di Category `Laptop {runId}` transaksi `Borrow`, Overridden `Max duration (11 days)`, dibuat oleh `Budi Hartono`, dibuat berurutan sesudah DU-014-24.
  - DU-014-26: override Group `Gudang Kota {runId}` di Category `Laptop {runId}` transaksi `Borrow`, Overridden `Max duration (12 days)`, dibuat oleh `Budi Santoso`, dibuat berurutan sesudah DU-014-25.
  - DU-014-27: override Group `Cendana Raya {runId}` di Category `Laptop {runId}` transaksi `Borrow`, Overridden `Max extensions (2)`, dibuat oleh `Budi Santoso`, dibuat berurutan sesudah DU-014-26.
  - DU-014-28: override Group `Mawar Putih {runId}` di All categories transaksi `Borrow`, Overridden `Max duration (14 days)`, dibuat oleh `Rina Wulandari`, dibuat berurutan sesudah DU-014-27.
  - DU-014-29: override Group `Flamboyan Asri {runId}` di Category `Laptop {runId}` transaksi `Borrow`, Overridden `Max duration (15 days)`, dibuat oleh `Budi Santoso`, dibuat berurutan sesudah DU-014-28.
- Kondisi:
  - Ukuran halaman tabel Overrides bernilai `10`.
  - Kolom `Category` tabel Overrides tidak ditampilkan (bawaan) untuk `Rina Wulandari`.
  - Setiap override dibuat berurutan dengan jarak waktu yang membuat Created At masing-masing berbeda.

## Test Steps

### Urutan awal tabel Overrides adalah Created At Newest First
1. Klik node `All categories` di Sidebar Category Tree
2. Klik tab `Borrow`
3. Verifikasi laporan paginasi `Showing 1 to 10 of 12` tampil di bawah tabel Overrides
4. Verifikasi urutan lima baris pertama menurut Target: `Flamboyan Asri {runId}`, `Mawar Putih {runId}`, `Cendana Raya {runId}`, `Gudang Kota {runId}`, `Toyota Avanza {runId}` sebagai Newest First
5. Klik header kolom Actions pada tabel Overrides
6. Centang kolom `Category`

### Sort kolom Created At mengikuti Oldest First lalu Newest First
7. Klik header kolom Created At pada tabel Overrides
8. Verifikasi urutan tiga baris pertama menurut Target: `anggur Timur {runId}`, `Apel Barat {runId}`, `Cakra Utara {runId}` sebagai Oldest First
9. Klik header kolom Created At pada tabel Overrides
10. Verifikasi urutan tiga baris pertama menurut Target: `Flamboyan Asri {runId}`, `Mawar Putih {runId}`, `Cendana Raya {runId}` sebagai Newest First

### Sort kolom Target tanpa membedakan huruf besar dan kecil, lintas halaman, dan kembali ke bawaan pada klik ketiga
11. Klik header kolom Target pada tabel Overrides
12. Verifikasi urutan empat baris pertama menurut Target: `anggur Timur {runId}`, `Apel Barat {runId}`, `Bima Tengah {runId}`, `Cakra Utara {runId}` secara ascending
13. Klik header kolom Target pada tabel Overrides
14. Verifikasi urutan tiga baris pertama menurut Target: `Zeta Selatan {runId}`, `Toyota Avanza {runId}`, `Mawar Putih {runId}` secara descending
15. Klik tombol `Next Page` pada paginasi tabel Overrides
16. Verifikasi laporan paginasi `Showing 11 to 12 of 12` tampil dengan urutan baris halaman 2 menurut Target: `Apel Barat {runId}`, `anggur Timur {runId}` secara descending
17. Klik tombol `Previous Page` pada paginasi tabel Overrides
18. Klik header kolom Target pada tabel Overrides
19. Verifikasi urutan tiga baris pertama menurut Target: `Flamboyan Asri {runId}`, `Mawar Putih {runId}`, `Cendana Raya {runId}` kembali ke urutan bawaan Created At Newest First

### Sort kolom Scope
20. Klik header kolom Scope pada tabel Overrides
21. Verifikasi dua baris pertama adalah baris `Excavator PC200 {runId}` dan baris `Toyota Avanza {runId}` dengan Scope `Asset Name` secara ascending
22. Klik header kolom Scope pada tabel Overrides
23. Verifikasi baris pertama memiliki Scope `Group` secara descending
24. Klik tombol `Next Page` pada paginasi tabel Overrides
25. Verifikasi dua baris halaman 2 adalah baris `Excavator PC200 {runId}` dan baris `Toyota Avanza {runId}` dengan Scope `Asset Name` secara descending
26. Klik tombol `Previous Page` pada paginasi tabel Overrides

### Sort kolom Overridden menurut nama field pertama
27. Klik header kolom Overridden pada tabel Overrides
28. Verifikasi baris pertama memiliki Target `Dharma Pusat {runId}` dan Overridden `Allow Borrow (Deny)` secara ascending menurut nama field pertama
29. Klik header kolom Overridden pada tabel Overrides
30. Verifikasi baris pertama memiliki Target `Cendana Raya {runId}` dan Overridden `Max extensions (2)` secara descending menurut nama field pertama

### Sort kolom Created By memakai nama yang tampil
31. Klik header kolom Created By pada tabel Overrides
32. Verifikasi baris pertama memiliki Target `Toyota Avanza {runId}` dan Created By `Budi H` secara ascending
33. Klik header kolom Created By pada tabel Overrides
34. Verifikasi baris pertama memiliki Target `Mawar Putih {runId}` dan Created By `Rina W` secara descending

### Sort kolom Category
35. Klik header kolom Category pada tabel Overrides
36. Verifikasi baris pertama memiliki Target `Mawar Putih {runId}` dan Category `All categories` secara ascending
37. Klik header kolom Category pada tabel Overrides
38. Verifikasi baris pertama memiliki Target `Cakra Utara {runId}` dan Category `Machinery {runId}` secara descending
39. Klik header kolom Actions pada tabel Overrides
40. Hapus centang kolom `Category`
