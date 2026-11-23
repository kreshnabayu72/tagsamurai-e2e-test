---
id: TC-FA-MISS-E2E-042-stock-opname-dep-audit
title: "Report Missing dari Task Detail Audit oleh pelapor dengan hak Aktor Missing (Total Control, Group Manager) langsung Missing tanpa aksi Cancel my report, dan item Audited dengan badge Reported Missing bertautan ke Missing Log"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.3#b4", "§9.4.2#r15", "§2#b2", "§2.1#b1", "§11#r9", "§9.2#b51", "§3#p2", "§1.2#r71", "§4.8#r8", "§9.4.2#r37", "§1.2#r57", "§4.8#r2"]
smoke: []
dependsOn: ["Audit: Task Detail Audit > Report Missing", "Audit: item Audited"]
trace:
  "§4.2.3#b4": [12, 13, 15, 24, 31, 32, 34, 48, 55, 58]
  "§9.4.2#r15": [36, 38, 40]
  "§2#b2": [11, 30]
  "§2.1#b1": [11, 30]
  "§11#r9": [6]
  "§9.2#b51": [36, 40]
  "§3#p2": [6, 11]
  "§1.2#r71": [11, 30]
  "§4.8#r8": [7, 25]
  "§9.4.2#r37": [11, 30]
  "§1.2#r57": [7, 25]
  "§4.8#r2": [6, 24]
anchor: [2, 53]
coverage:
  web: automated
---

# Report Missing dari Task Detail Audit oleh pelapor dengan hak Aktor Missing (Total Control, Group Manager) langsung Missing tanpa aksi Cancel my report, dan item Audited dengan badge Reported Missing bertautan ke Missing Log

## Prerequisites
- Aktor: Total Control `Rina W`, pemegang hak Aktor Missing. Aktor lain: Group Manager `Dewi Lestari {runId}` atas Group `Warehouse`, juga pemegang hak Aktor Missing.
- Layar awal: Audit.
- Data:
  - DU-042-1: Task Audit `Audit Gudang Utama {runId}` yang memuat tiga item berstatus `Not found`: `Laptop Dell Latitude 5420 {runId}`, `Printer HP LaserJet M404 {runId}`, dan `Projector Epson EB-X06 {runId}`.
  - DU-042-2: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Warehouse`, tanpa record Missing.
  - DU-042-3: Asset `Printer HP LaserJet M404 {runId}`, Group `Warehouse`, tanpa record Missing.
  - DU-042-4: Asset `Projector Epson EB-X06 {runId}`, Group `Warehouse`, sudah punya satu record Missing berjalan.
  - DU-042-5: Task Audit `Audit Gudang Cabang {runId}` dengan item `Toyota Innova {runId}` berstatus `Audited` karena terbaca di sesi Audit ini, dengan badge `Reported Missing`.
  - DU-042-6: Asset `Toyota Innova {runId}`, Group `Branch Surabaya`, dengan record Missing berstatus `Missing`.
  - DU-042-7: Pengguna `Dewi Lestari {runId}`, Group Manager atas Group `Warehouse`.
  - DU-042-8: Pengguna `Rina W`, Total Control.
  - DU-042-9: What happened `Laptop tidak ada di rak saat penghitungan fisik`.
  - DU-042-10: What happened `Printer dan proyektor tidak ada di rak saat penghitungan fisik`.
  - DU-042-11: Task Audit `Audit Gudang Pusat {runId}` yang memuat dua item berstatus `Not found`: `Kursi Rapat Lipat {runId}` dan `Lemari Arsip Besi {runId}`.
  - DU-042-12: Asset `Kursi Rapat Lipat {runId}`, Group `Warehouse`, dalam cakupan Group pelapor `Dewi Lestari {runId}`, tanpa record Missing.
  - DU-042-13: Asset `Lemari Arsip Besi {runId}`, Group `Branch Medan`, di luar cakupan Group pelapor `Dewi Lestari {runId}`, tanpa record Missing.
  - DU-042-14: What happened `Kursi dan lemari tidak ada di ruang penyimpanan saat penghitungan fisik`.
- Kondisi:
  - Akun `Rina W` dan `Dewi Lestari {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Total Control melapor satu item Not found dari Task Detail Audit
1. Buka Task Detail Audit `Audit Gudang Utama {runId}`
2. Verifikasi item `Laptop Dell Latitude 5420 {runId}` berstatus `Not found`
3. Klik `Report Missing` pada item `Laptop Dell Latitude 5420 {runId}`
4. Isi What happened `Laptop tidak ada di rak saat penghitungan fisik`
5. Klik `[Report Missing]` pada dialog
6. Verifikasi toast `Success, asset has been reported missing.` tampil
7. Verifikasi item `Laptop Dell Latitude 5420 {runId}` tidak menyediakan aksi `Cancel my report` di Task Detail Audit

### Record Total Control langsung Missing di tab Missing
8. Buka halaman `Assets`
9. Klik tab `Missing`
10. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
11. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berstatus `Missing`
12. Verifikasi kolom Source pada baris itu `Audit`
13. Verifikasi kolom Reported By pada baris itu `Rina W`
14. Klik `Laptop Dell Latitude 5420 {runId}` pada kolom Name
15. Verifikasi dialog Missing Log memuat node `Reported missing by` oleh `Rina W` dengan What happened `Laptop tidak ada di rak saat penghitungan fisik`
16. Tutup dialog Missing Log dengan `✕`

### Group Manager Bulk Report Missing melewati aset yang sudah punya record berjalan
17. Masuk sebagai `Dewi Lestari {runId}`
18. Buka Task Detail Audit `Audit Gudang Utama {runId}`
19. Centang item `Printer HP LaserJet M404 {runId}`
20. Centang item `Projector Epson EB-X06 {runId}`
21. Klik `Bulk Report Missing`
22. Isi What happened `Printer dan proyektor tidak ada di rak saat penghitungan fisik`
23. Klik `[Report Missing]` pada dialog
24. Verifikasi toast `Success, asset has been reported missing. Some items were skipped.` tampil
25. Verifikasi item `Printer HP LaserJet M404 {runId}` tidak menyediakan aksi `Cancel my report` di Task Detail Audit

### Record Group Manager langsung Missing di tab Missing
26. Masuk sebagai `Rina W`
27. Buka halaman `Assets`
28. Klik tab `Missing`
29. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
30. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Missing`
31. Verifikasi kolom Source pada baris itu `Audit`
32. Verifikasi kolom Reported By pada baris itu `Dewi Lestari {runId}`
33. Ganti isi kotak search dengan `Projector Epson EB-X06 {runId}`, tekan Enter
34. Verifikasi hasil Search `Projector Epson EB-X06 {runId}` hanya satu baris

### Item Audited dengan badge Reported Missing bertautan ke Missing Log
35. Buka Task Detail Audit `Audit Gudang Cabang {runId}`
36. Verifikasi item `Toyota Innova {runId}` berstatus `Audited` dengan badge `Reported Missing`
37. Klik badge `Reported Missing` pada item `Toyota Innova {runId}`
38. Verifikasi dialog Missing Log record `Toyota Innova {runId}` terbuka
39. Tutup dialog Missing Log dengan `✕`
40. Verifikasi item `Toyota Innova {runId}` tidak menyediakan aksi `Mark as Found` di layar Audit

### Group Manager Bulk Report Missing melewati aset di luar cakupan pelapor
41. Masuk sebagai `Dewi Lestari {runId}`
42. Buka Task Detail Audit `Audit Gudang Pusat {runId}`
43. Centang item `Kursi Rapat Lipat {runId}`
44. Centang item `Lemari Arsip Besi {runId}`
45. Klik `Bulk Report Missing`
46. Isi What happened `Kursi dan lemari tidak ada di ruang penyimpanan saat penghitungan fisik`
47. Klik `[Report Missing]` pada dialog
48. Verifikasi toast `Success, asset has been reported missing. Some items were skipped.` tampil
49. Masuk sebagai `Rina W`
50. Buka halaman `Assets`
51. Klik tab `Missing`
52. Ketik Search `Kursi Rapat Lipat {runId}`, tekan Enter
53. Verifikasi baris `Kursi Rapat Lipat {runId}` berstatus `Missing`
54. Ganti isi kotak search dengan `Lemari Arsip Besi {runId}`, tekan Enter
55. Verifikasi baris `Lemari Arsip Besi {runId}` tidak tampil di tab Missing

### Notifikasi missing_reported ke Aktor Missing atas record Source Audit dari Pelapor admin
56. Masuk sebagai `Rina W`
57. Buka daftar notifikasi
58. Verifikasi notifikasi event `missing_reported` atas `Printer HP LaserJet M404 {runId}` tampil di daftar notifikasi
