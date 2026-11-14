---
id: TC-FA-MISS-E2E-042-stock-opname-dep-audit
title: "Report Missing dari sesi Stock Opname dan item Audited dengan badge Reported Missing bertautan ke Missing Log"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.3#b4", "§9.4.2#r15", "§2#b2", "§2.1#b1", "§11#r9", "§9.2#b47", "§3#p2"]
smoke: []
dependsOn: ["Audit: sesi Stock Opname > Report Missing", "Audit: item Audited"]
trace:
  "§4.2.3#b4": [12, 18, 19, 21, 24, 38, 45]
  "§9.4.2#r15": [27, 29]
  "§2#b2": [17]
  "§2.1#b1": [17]
  "§11#r9": [2]
  "§9.2#b47": [27, 31]
  "§3#p2": [6, 17]
anchor: [43]
coverage:
  web: automated
---

# Report Missing dari sesi Stock Opname dan item Audited dengan badge Reported Missing bertautan ke Missing Log

## Prerequisites
- Aktor: pemilik sesi Stock Opname `Maya Putri {runId}` tanpa Manage asset & TAG (Update). Aktor lain: Total Control `Rina W`.
- Layar awal: Stock Opname.
- Data:
  - DU-042-1: Sesi Stock Opname `SO Gudang Utama {runId}` milik `Maya Putri {runId}` yang memuat tiga item berstatus `Not found`: `Laptop Dell Latitude 5420 {runId}`, `Printer HP LaserJet M404 {runId}`, dan `Projector Epson EB-X06 {runId}`.
  - DU-042-2: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Warehouse`, tanpa record Missing.
  - DU-042-3: Asset `Printer HP LaserJet M404 {runId}`, Group `Warehouse`, tanpa record Missing.
  - DU-042-4: Asset `Projector Epson EB-X06 {runId}`, Group `Warehouse`, sudah punya satu record Missing berjalan.
  - DU-042-5: Sesi Stock Opname `SO Gudang Cabang {runId}` milik `Maya Putri {runId}` dengan item `Toyota Innova {runId}` berstatus `Audited` karena terbaca di sesi ini, dengan badge `Reported Missing`.
  - DU-042-6: Asset `Toyota Innova {runId}`, Group `Branch Surabaya`, dengan record Missing berstatus `Missing`.
  - DU-042-7: Pengguna `Maya Putri {runId}`, pemilik sesi Stock Opname tanpa Manage asset & TAG (Update).
  - DU-042-8: Pengguna `Rina W`, Total Control.
  - DU-042-9: What happened `Laptop tidak ada di rak saat penghitungan fisik`.
  - DU-042-10: What happened `Printer dan proyektor tidak ada di rak saat penghitungan fisik`.
  - DU-042-11: Sesi Stock Opname `SO Gudang Pusat {runId}` milik `Maya Putri {runId}` yang memuat dua item berstatus `Not found`: `Kursi Rapat Lipat {runId}` dan `Lemari Arsip Besi {runId}`.
  - DU-042-12: Asset `Kursi Rapat Lipat {runId}`, Group `Warehouse`, dalam cakupan Group pelapor `Maya Putri {runId}`, tanpa record Missing.
  - DU-042-13: Asset `Lemari Arsip Besi {runId}`, Group `Branch Medan`, di luar cakupan Group pelapor `Maya Putri {runId}`, tanpa record Missing.
  - DU-042-14: What happened `Kursi dan lemari tidak ada di ruang penyimpanan saat penghitungan fisik`.
- Kondisi:
  - Akun `Maya Putri {runId}` dan `Rina W` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Report Missing satu item Not found dari sesi Stock Opname
1. Buka sesi Stock Opname `SO Gudang Utama {runId}`
2. Verifikasi item `Laptop Dell Latitude 5420 {runId}` berstatus `Not found`
3. Klik `Report Missing` pada item `Laptop Dell Latitude 5420 {runId}`
4. Isi What happened `Laptop tidak ada di rak saat penghitungan fisik`
5. Klik `[Report Missing]` pada dialog
6. Verifikasi toast `Success, asset has been reported missing.` tampil

### Bulk Report Missing melewati aset yang sudah punya record berjalan
7. Centang item `Printer HP LaserJet M404 {runId}`
8. Centang item `Projector Epson EB-X06 {runId}`
9. Klik `Bulk Report Missing`
10. Isi What happened `Printer dan proyektor tidak ada di rak saat penghitungan fisik`
11. Klik `[Report Missing]` pada dialog
12. Verifikasi toast `Success, asset has been reported missing. Some items were skipped.` tampil

### Record dari sesi Stock Opname di tab Missing
13. Masuk sebagai `Rina W`
14. Buka halaman `Assets`
15. Klik tab `Missing`
16. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
17. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berstatus `Missing`
18. Verifikasi kolom Source pada baris itu `Stock opname`
19. Verifikasi kolom Reported By pada baris itu `Maya Putri {runId}`
20. Klik `Laptop Dell Latitude 5420 {runId}` pada kolom Name
21. Verifikasi dialog Missing Log memuat node `Reported missing by` oleh `Maya Putri {runId}` dengan What happened `Laptop tidak ada di rak saat penghitungan fisik`
22. Tutup dialog Missing Log dengan `✕`
23. Ganti isi kotak search dengan `Projector Epson EB-X06 {runId}`, tekan Enter
24. Verifikasi hasil Search `Projector Epson EB-X06 {runId}` hanya satu baris

### Item Audited dengan badge Reported Missing bertautan ke Missing Log
25. Masuk sebagai `Maya Putri {runId}`
26. Buka sesi Stock Opname `SO Gudang Cabang {runId}`
27. Verifikasi item `Toyota Innova {runId}` berstatus `Audited` dengan badge `Reported Missing`
28. Klik badge `Reported Missing` pada item `Toyota Innova {runId}`
29. Verifikasi dialog Missing Log record `Toyota Innova {runId}` terbuka
30. Tutup dialog Missing Log dengan `✕`
31. Verifikasi item `Toyota Innova {runId}` tidak menyediakan aksi `Mark as Found` di layar Stock Opname

### Bulk Report Missing melewati aset di luar cakupan pelapor
32. Buka sesi Stock Opname `SO Gudang Pusat {runId}`
33. Centang item `Kursi Rapat Lipat {runId}`
34. Centang item `Lemari Arsip Besi {runId}`
35. Klik `Bulk Report Missing`
36. Isi What happened `Kursi dan lemari tidak ada di ruang penyimpanan saat penghitungan fisik`
37. Klik `[Report Missing]` pada dialog
38. Verifikasi toast `Success, asset has been reported missing. Some items were skipped.` tampil
39. Masuk sebagai `Rina W`
40. Buka halaman `Assets`
41. Klik tab `Missing`
42. Ketik Search `Kursi Rapat Lipat {runId}`, tekan Enter
43. Verifikasi baris `Kursi Rapat Lipat {runId}` berstatus `Missing`
44. Ganti isi kotak search dengan `Lemari Arsip Besi {runId}`, tekan Enter
45. Verifikasi baris `Lemari Arsip Besi {runId}` tidak tampil di tab Missing
