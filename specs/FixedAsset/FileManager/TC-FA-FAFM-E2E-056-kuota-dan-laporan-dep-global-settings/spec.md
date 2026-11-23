---
id: TC-FA-FAFM-E2E-056-kuota-dan-laporan-dep-global-settings
title: "Kuota dan pemakaian Global Settings File Manager tercermin di kartu Storage Usage"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ARS-08c, DIM-02b, F-FAFM-06c, F-FAFM-06i, FAFM-LOGIC-06d, FAFM-LOGIC-06g, SUC-03a, SUC-04a, SUC-06e, SYN-02e, SYN-03e, SYN-09d, SYN-10a, SYN-10b, SYN-10c, SYN-10d, SYN-10e]
smoke: []
dependsOn: ["Global Settings: File Manager"]
trace:
  ARS-08c: 3
  DIM-02b: [5, 6]
  F-FAFM-06c: [5, 6, 12]
  F-FAFM-06i: [3, 31, 34, 38]
  FAFM-LOGIC-06d: [3, 7, 31, 32, 34, 35, 38, 39]
  FAFM-LOGIC-06g: [5, 6, 41]
  SUC-03a: [2, 5]
  SUC-04a: [2, 6]
  SUC-06e: [3, 7]
  SYN-02e: [3, 22, 24]
  SYN-03e: [3, 31, 34, 38]
  SYN-09d: 3
  SYN-10a: 16
  SYN-10b: 12
  SYN-10c: [9, 13]
  SYN-10d: [8, 14]
  SYN-10e: [12, 13, 14]
anchor: [13]
coverage:
  web: automated
---

# Kuota dan pemakaian Global Settings File Manager tercermin di kartu Storage Usage

## Prerequisites
- Aktor: Total Control.
- Layar awal: Global Settings > File Manager.
- Data:
  - DU-056-1: Entitas khusus `Entitas Storage {runId}` yang tidak dipakai spec lain; memiliki satu subscription Paid berstatus Active, Total Used `50.4 GB`, Storage Quota `50.0 GB`, pemakaian Fixed Asset `48.8 GB`, dan pemakaian Fixed Asset itu sudah dilaporkan ke Global Settings.
  - DU-056-3: Aset `Forklift Gudang {runId}`, Group `Head Office`, ada di entitas DU-056-1.
  - DU-056-4: File `arsip-recycle-{runId}.jpg`, Category `Asset Photo`, Size `2.0 GB`, ada di Recycle Bin, milik aset DU-056-3, sudah termasuk dalam pemakaian Fixed Asset `48.8 GB` yang dilaporkan.
  - DU-056-5: File `aktif-delete-{runId}.jpg`, Category `Asset Photo`, Size `1.0 GB`, aktif, milik aset DU-056-3, sudah termasuk dalam pemakaian Fixed Asset `48.8 GB` yang dilaporkan.
  - Nilai turunan: sesudah file DU-056-4 dihapus permanen, Fixed Asset di kartu File Manager `46.8 GB`, dari `48.8 GB` dikurangi Size DU-056-4 `2.0 GB`; sesudah laporan berkala berikutnya, Total Used `48.4 GB`, dari `50.4 GB` dikurangi `2.0 GB`.
  - DU-056-2: Top-up kuota Storage sebesar `25.0 GB` pada entitas DU-056-1, sehingga Storage Quota menjadi `75.0 GB` dan label ProgressBar menjadi `67%`.

## Test Steps

### Kartu Storage Usage Global Settings dan File Manager menampilkan angka yang sama
1. Buka Global Settings > File Manager
2. Verifikasi kartu Storage Usage Global Settings menampilkan Total Used `50.4 GB` dan Storage Quota `50.0 GB`
3. Verifikasi pemakaian aplikasi Fixed Asset pada kartu Storage Usage Global Settings menampilkan `48.8 GB`
4. Buka Fixed Asset > Settings > File Manager
5. Verifikasi kartu Storage Usage menampilkan Total Used `50.4 GB`
6. Verifikasi kartu Storage Usage menampilkan Storage Quota `50.0 GB`
7. Verifikasi kartu Storage Usage menampilkan `Fixed Asset 48.8 GB`

### Total Used mencapai kuota menampilkan Alert dan ProgressBar penuh
8. Verifikasi Alert `Storage is full. New uploads are blocked until storage is freed or the quota is increased.` tampil pada kartu Storage Usage
9. Verifikasi ProgressBar kartu Storage Usage menampilkan `100%` dengan severity danger dan bar penuh

### Top-up kuota tercermin pada pembacaan kartu berikutnya
10. Tambah kuota Storage client sebesar `25.0 GB` lewat top-up
11. Muat ulang halaman
12. Verifikasi kartu Storage Usage menampilkan Storage Quota `75.0 GB`
13. Verifikasi ProgressBar kartu Storage Usage menampilkan `67%` dengan severity default
14. Verifikasi tidak ada Alert Storage penuh pada kartu Storage Usage
15. Buka Global Settings > File Manager
16. Verifikasi kartu Storage Usage Global Settings menampilkan Storage Quota `75.0 GB`

### Delete memindahkan byte antar komponen tanpa mengubah total pemakaian dan laporan
17. Buka Fixed Asset > Settings > File Manager
18. Klik tab `Asset Photo`
19. Ketik Search `aktif-delete-{runId}.jpg`, tekan Enter
20. Klik aksi Delete pada baris file `aktif-delete-{runId}.jpg`
21. Klik `[Delete]` pada dialog Delete File
22. Verifikasi kartu Storage Usage menampilkan `Fixed Asset 48.8 GB`
23. Buka Global Settings > File Manager
24. Verifikasi pemakaian aplikasi Fixed Asset pada kartu Storage Usage Global Settings menampilkan `48.8 GB`

### Permanently Delete menurunkan Fixed Asset di kartu File Manager sedangkan laporan Global Settings tertinggal sampai laporan berikutnya
25. Buka Fixed Asset > Settings > File Manager
26. Klik tombol Recycle Bin pada header kartu Storage Usage
27. Ketik Search `arsip-recycle-{runId}.jpg`, tekan Enter
28. Buka aksi baris `arsip-recycle-{runId}.jpg`
29. Klik `Permanently Delete`
30. Klik `[Permanently Delete]` pada dialog `Permanently Delete File`
31. Verifikasi kartu Storage Usage menampilkan `Fixed Asset 46.8 GB`
32. Verifikasi kartu Storage Usage menampilkan Total Used `50.4 GB`
33. Buka Global Settings > File Manager
34. Verifikasi pemakaian aplikasi Fixed Asset pada kartu Storage Usage Global Settings masih menampilkan `48.8 GB`
35. Verifikasi kartu Storage Usage Global Settings masih menampilkan Total Used `50.4 GB`

### Laporan berkala berikutnya menurunkan pemakaian Fixed Asset di Global Settings dan Total Used
36. Laporan berkala pemakaian Fixed Asset ke Global Settings berjalan
37. Muat ulang halaman
38. Verifikasi pemakaian aplikasi Fixed Asset pada kartu Storage Usage Global Settings menampilkan `46.8 GB`
39. Verifikasi kartu Storage Usage Global Settings menampilkan Total Used `48.4 GB`
40. Buka Fixed Asset > Settings > File Manager
41. Verifikasi kartu Storage Usage menampilkan Total Used `48.4 GB`
