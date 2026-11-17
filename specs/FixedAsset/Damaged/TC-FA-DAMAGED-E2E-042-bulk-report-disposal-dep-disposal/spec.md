---
id: TC-FA-DAMAGED-E2E-042-bulk-report-disposal-dep-disposal
title: "Bulk Report Disposal satu Group memakai satu Reason untuk semua, melewati record yang tidak lagi Damaged dengan toast Some items were skipped, dan memblok D-DMG-13 bila semua dilewati"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, D-DMG-13, "§4.2.4#p10", D-DISP-13, "§4.2.4#r10", "§4.4#r13", V-DMG-09, TS-DMG-09, "§6#p2", "§8.3#b2", EC-DMG-35, "§9.4.4#r11", TS-DISP-15, EB-BLK-3, EB-EDG-2, "§9.2#b23", S-DMG-08]
smoke: []
dependsOn: ["Disposal: dialog Report Disposal (D-DISP-13) untuk bulk"]
trace:
  T-DMG-01: 4
  S-DMG-08: [4, 69, 71]
  EB-EDG-2: [6, 9, 10]
  "§4.4#r13": 16
  D-DISP-13: [16, 24, 28]
  "§9.2#b23": [16, 20, 21]
  TS-DISP-15: [19, 23, 53, 58, 61]
  "§8.3#b2": [23, 27, 41, 44]
  EB-BLK-3: [19, 23, 27, 61]
  V-DMG-09: [37, 38, 39]
  TS-DMG-09: 37
  "§6#p2": [37, 53, 59]
  EC-DMG-35: [37, 38, 39, 44]
  "§9.4.4#r11": [41, 44]
  D-DMG-13: [53, 54, 55, 56]
  "§4.2.4#p10": [53, 55]
  "§4.2.4#r10": [53, 54, 55, 58, 61]
anchor: []
coverage:
  web: automated
---

# Bulk Report Disposal satu Group memakai satu Reason untuk semua, melewati record yang tidak lagi Damaged dengan toast Some items were skipped, dan memblok D-DMG-13 bila semua dilewati

## Prerequisites
- Aktor: Total Control; `Admin B {runId}` (Total Control, seluruh client) hanya memicu perubahan state.
- Layar awal: Assets > Damaged > Active.
- Data:
  - DU-042-1: Damage record `Monitor Dell P2422H {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-2: `2` Damage record `Printer HP LaserJet {runId} - 1` dan `Printer HP LaserJet {runId} - 2`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-3: `6` Damage record `Proyektor Epson EB-X06 {runId} - 1` sampai `Proyektor Epson EB-X06 {runId} - 6`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-4: `8` Damage record `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 1` sampai `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 8`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-5: Damage record `Forklift Toyota 8FD {runId}`, Group `Warehouse`, Status `Damaged`, Source `Manual`.
  - DU-042-6: Damage record `Scanner Fujitsu fi-7160 {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-7: User `Admin B {runId}`, role Total Control, cakupan seluruh client.
  - DU-042-8: Input Reason bulk atas `Monitor Dell P2422H {runId}`: Reason `Monitor tidak menyala dan tidak layak diperbaiki`.
  - DU-042-9: Input Reason bulk atas `Printer HP LaserJet {runId} - 1` dan `Printer HP LaserJet {runId} - 2`: Reason `Printer satu Group sudah tidak layak pakai`.
  - DU-042-10: Input Reason bulk atas `Proyektor Epson EB-X06 {runId} - 1` sampai `- 6`: Reason `Proyektor satu Group sudah tidak layak pakai`.
  - DU-042-11: Input Reason bulk atas record `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara`: Reason `Panel listrik sudah tidak layak pakai`.
  - DU-042-12: Input Reason `Admin B {runId}` atas record `Proyektor Epson EB-X06 {runId} - 3` sampai `- 6` dan seluruh record `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara`: Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`.
- Kondisi:
  - Level Feature Suite Disposal bernilai `Basic`.
  - Selection Limit bernilai `1000`.

## Test Steps

### Bulk Report Disposal atas satu record memakai bentuk tunggal
1. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
2. Centang baris `Monitor Dell P2422H {runId}`
3. Klik `Bulk Action`
4. Verifikasi `Report Disposal` tersedia dan aktif pada daftar aksi bulk
5. Klik `Report Disposal`
6. Verifikasi dialog Report Disposal terbuka untuk `1` record `Monitor Dell P2422H {runId}` dalam bentuk tunggal yang sama dengan Report Disposal satu aset
7. Isi Reason `Monitor tidak menyala dan tidak layak diperbaiki`
8. Kirim dialog Report Disposal
9. Verifikasi toast sukses Report Disposal tampil
10. Verifikasi baris `Monitor Dell P2422H {runId}` berstatus `Reported Disposal`

### Bulk Report Disposal satu Group memakai satu Reason untuk semua record
11. Ganti isi kotak search dengan `Printer HP LaserJet {runId}`, tekan Enter
12. Centang baris `Printer HP LaserJet {runId} - 1`
13. Centang baris `Printer HP LaserJet {runId} - 2`
14. Klik `Bulk Action`
15. Klik `Report Disposal`
16. Verifikasi dialog Report Disposal terbuka dengan satu isian `Reason` untuk kedua record
17. Isi Reason `Printer satu Group sudah tidak layak pakai`
18. Kirim dialog Report Disposal dengan dua klik berturut-turut
19. Verifikasi tepat `1` toast sukses Report Disposal tampil
20. Verifikasi baris `Printer HP LaserJet {runId} - 1` berstatus `Reported Disposal`
21. Verifikasi baris `Printer HP LaserJet {runId} - 2` berstatus `Reported Disposal`
22. Klik nama aset `Printer HP LaserJet {runId} - 1` di kolom Name
23. Verifikasi dialog Damage Log record `Printer HP LaserJet {runId} - 1` memuat tepat `1` node `Disposal reported by`
24. Verifikasi baris detail node `Disposal reported by` memuat Reason `Printer satu Group sudah tidak layak pakai`
25. Tutup dialog Damage Log
26. Klik nama aset `Printer HP LaserJet {runId} - 2` di kolom Name
27. Verifikasi dialog Damage Log record `Printer HP LaserJet {runId} - 2` memuat tepat `1` node `Disposal reported by`
28. Verifikasi baris detail node `Disposal reported by` record `Printer HP LaserJet {runId} - 2` memuat Reason `Printer satu Group sudah tidak layak pakai`
29. Tutup dialog Damage Log

### Record yang tidak lagi Damaged saat Submit dilewati dan sisanya dilaporkan
30. Ganti isi kotak search dengan `Proyektor Epson EB-X06 {runId}`, tekan Enter
31. Klik tombol Select All
32. Klik `Bulk Action`
33. Klik `Report Disposal`
34. `Admin B {runId}` menjalankan Report Disposal atas record `Proyektor Epson EB-X06 {runId} - 3`, `Proyektor Epson EB-X06 {runId} - 4`, `Proyektor Epson EB-X06 {runId} - 5`, dan `Proyektor Epson EB-X06 {runId} - 6` dengan Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`
35. Isi Reason `Proyektor satu Group sudah tidak layak pakai`
36. Kirim dialog Report Disposal
37. Verifikasi toast `Success, asset has been reported for disposal. Some items were skipped.` tampil
38. Verifikasi baris `Proyektor Epson EB-X06 {runId} - 1` berstatus `Reported Disposal`
39. Verifikasi baris `Proyektor Epson EB-X06 {runId} - 2` berstatus `Reported Disposal`
40. Klik nama aset `Proyektor Epson EB-X06 {runId} - 1` di kolom Name
41. Verifikasi dialog Damage Log record `Proyektor Epson EB-X06 {runId} - 1` memuat tepat `1` node `Disposal reported by` dengan pelaku aktor yang menjalankan bulk
42. Tutup dialog Damage Log
43. Klik nama aset `Proyektor Epson EB-X06 {runId} - 3` di kolom Name
44. Verifikasi dialog Damage Log record `Proyektor Epson EB-X06 {runId} - 3` memuat tepat `1` node `Disposal reported by` dengan pelaku `Admin B {runId}`
45. Tutup dialog Damage Log

### Semua record dilewati memunculkan dialog blok Cannot Report Disposal
46. Ganti isi kotak search dengan `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara`, tekan Enter
47. Klik tombol Select All
48. Klik `Bulk Action`
49. Klik `Report Disposal`
50. `Admin B {runId}` menjalankan Report Disposal atas seluruh `8` record `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara` dengan Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`
51. Isi Reason `Panel listrik sudah tidak layak pakai`
52. Kirim dialog Report Disposal
53. Verifikasi dialog blok `Cannot Report Disposal` tampil
54. Verifikasi isi dialog `None of the selected records can be reported for disposal.`
55. Verifikasi daftar dialog memuat bullet `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 1` sampai `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 8`, masing-masing dengan keterangan per record, tanpa diringkas
56. Verifikasi daftar dialog dapat digulir sampai bullet terakhir `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 8`
57. Klik `OK`
58. Verifikasi bulk action bar masih tampil dengan jumlah terpilih `8`
59. Verifikasi baris `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 1` sampai `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 8` pada tabel berstatus `Reported Disposal` sesudah tabel dimuat ulang
60. Klik nama aset `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 1` di kolom Name
61. Verifikasi dialog Damage Log record `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 1` memuat tepat `1` node `Disposal reported by` dengan pelaku `Admin B {runId}`
62. Tutup dialog Damage Log
63. Klik `×` pada bulk action bar

### Seleksi lintas Group diblok sebelum dialog Report Disposal dibuka
64. Ganti isi kotak search dengan `{runId}`, tekan Enter
65. Centang baris `Forklift Toyota 8FD {runId}`
66. Centang baris `Scanner Fujitsu fi-7160 {runId}`
67. Klik `Bulk Action`
68. Klik `Report Disposal`
69. Verifikasi dialog blok `Selected assets come from more than one group. Select assets from one group.` tampil dengan bullet `Forklift Toyota 8FD {runId}` dan `Scanner Fujitsu fi-7160 {runId}`
70. Klik `OK`
71. Verifikasi baris `Forklift Toyota 8FD {runId}` tetap berstatus `Damaged`
72. Klik `×` pada bulk action bar
