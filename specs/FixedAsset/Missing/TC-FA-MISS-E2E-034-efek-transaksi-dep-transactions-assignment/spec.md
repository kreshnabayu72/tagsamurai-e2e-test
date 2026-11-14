---
id: TC-FA-MISS-E2E-034-efek-transaksi-dep-transactions-assignment
title: "Efek Missing pada Assignment: baris Assigned ditutup, permintaan menunggu dibatalkan, pintu masuk Report Missing"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r42", "§9.4.2#r4", "§11#r5", "§4.2.3#p2", "§9.7#r1", "§9.2#b32", "§4.2.3#b5"]
smoke: []
dependsOn: ["Transactions Assignment: halaman Assignment > aksi Report Missing", "Transactions Assignment: Draft"]
trace:
  "§1.2#r42": [8]
  "§9.4.2#r4": [18, 19, 21, 48, 50]
  "§11#r5": [3, 8, 15, 36]
  "§4.2.3#p2": [12]
  "§9.7#r1": [8, 15, 36, 57, 60]
  "§9.2#b32": [24]
  "§4.2.3#b5": [5, 12, 29, 43]
anchor: [28, 42, 47]
coverage:
  web: automated
---

# Efek Missing pada Assignment: baris Assigned ditutup, permintaan menunggu dibatalkan, pintu masuk Report Missing

## Prerequisites
- Aktor: Aktor Assignment tanpa Manage asset & TAG (Update) `Nina Aulia {runId}`. Aktor lain: Total Control `Rina W`.
- Layar awal: Assignment.
- Data:
  - DU-034-1: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Finance Room`, dengan baris Assignment berstatus `Assigned` untuk penerima `Joko Santoso {runId}`, tanpa record Missing.
  - DU-034-2: Asset `Hand Pallet Truck {runId}`, Group `Warehouse`, dengan satu baris Assignment berstatus `Waiting for Handover` yang menunggu, tanpa pemegang, tanpa record Missing.
  - DU-034-3: Asset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, tanpa pemegang, tanpa record Missing, tercantum dalam Draft Assignment `Draft Penugasan Printer {runId}` bersama aset `Mouse Logitech MX Master 3 {runId}`.
  - DU-034-4: Asset `Monitor LG 27UL500 {runId}`, Group `Head Office`, dengan baris Assignment berstatus `Assigned` untuk penerima `Joko Santoso {runId}` dan record Missing `Waiting for Confirmation` yang dilaporkan `Joko Santoso {runId}`.
  - DU-034-5: Pengguna `Nina Aulia {runId}`, Aktor Assignment tanpa Manage asset & TAG (Update).
  - DU-034-6: Pengguna `Joko Santoso {runId}`, pemegang tanpa hak Aktor Missing.
  - DU-034-7: What happened `Laptop tidak ada di meja penerima setelah pindah ruangan`.
  - DU-034-8: What happened `Hand pallet truck hilang dari gudang sebelum diserahkan`.
  - DU-034-9: What happened `Printer tidak ada di ruang cetak setelah renovasi`.
  - DU-034-10: Asset `Tablet Samsung Galaxy Tab S8 {runId}`, Group `Head Office`, dengan baris Assignment berstatus `Assigned` untuk penerima `Joko Santoso {runId}`, tanpa record Missing.
  - DU-034-11: Asset `Scanner Zebra DS2208 {runId}`, Group `Warehouse`, tanpa pemegang, tanpa record Missing, tercantum dalam Draft Assignment `Draft Penugasan Scanner {runId}`.
  - DU-034-12: Asset `Camera Canon EOS {runId}`, Group `Head Office`, dengan satu baris Assignment berstatus `Waiting for Approval`, tanpa pemegang, tanpa record Missing.
  - DU-034-13: Asset `Mouse Logitech MX Master 3 {runId}`, Group `Head Office`, tanpa pemegang, tanpa record Missing, tercantum dalam Draft Assignment `Draft Penugasan Printer {runId}`.
  - DU-034-14: What happened `Kamera tidak ada di ruang arsip sebelum permintaan disetujui`.
- Kondisi:
  - Akun `Nina Aulia {runId}` dan `Rina W` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Report Missing atas baris Assigned menutup baris
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
3. Verifikasi aksi `Report Missing` tampil pada menu
4. Klik `Report Missing`
5. Verifikasi kotak dampak memuat baris pemegang `Joko Santoso {runId}` diikuti `and the asset admins will be notified.`
6. Isi What happened `Laptop tidak ada di meja penerima setelah pindah ruangan`
7. Klik `[Report Missing]` pada dialog
8. Verifikasi baris Assignment `Laptop Dell Latitude 5420 {runId}` tidak lagi berstatus `Assigned`

### Report Missing atas aset dengan permintaan menunggu membatalkan permintaan itu
9. Ganti isi kotak search dengan `Hand Pallet Truck {runId}`, tekan Enter
10. Buka menu `⋯` pada baris `Hand Pallet Truck {runId}`
11. Klik `Report Missing`
12. Verifikasi kotak dampak memuat baris `The asset admins will be notified.`
13. Isi What happened `Hand pallet truck hilang dari gudang sebelum diserahkan`
14. Klik `[Report Missing]` pada dialog
15. Verifikasi baris Assignment `Hand Pallet Truck {runId}` berstatus `Canceled`

### Aset dalam Draft ditandai tidak tersedia tanpa mengubah Draft
16. Rina W melaporkan `Printer HP LaserJet M404 {runId}` hilang lewat Report Missing dengan What happened `Printer tidak ada di ruang cetak setelah renovasi`
17. Buka Draft Assignment `Draft Penugasan Printer {runId}`
18. Verifikasi `Printer HP LaserJet M404 {runId}` ditandai ⚠ unavailable di Draft
19. Verifikasi `Printer HP LaserJet M404 {runId}` tetap tercantum di Draft
20. Klik `[Submit]` pada Draft
21. Verifikasi Submit Draft diblokir sampai aset `Printer HP LaserJet M404 {runId}` dikeluarkan

### Laporan pemegang tidak menutup baris Assigned
22. Ganti isi kotak search dengan `Monitor LG 27UL500 {runId}`, tekan Enter
23. Klik tab `Assigned`
24. Verifikasi baris Assignment `Monitor LG 27UL500 {runId}` tetap berstatus `Assigned`

### Kotak dampak tidak mempratinjau efek baris Assignment
25. Ganti isi kotak search dengan `Tablet Samsung Galaxy Tab S8 {runId}`, tekan Enter
26. Buka menu `⋯` pada baris `Tablet Samsung Galaxy Tab S8 {runId}`
27. Klik `Report Missing`
28. Verifikasi kotak dampak memuat baris pemegang `Joko Santoso {runId}` diikuti `and the asset admins will be notified.`
29. Verifikasi baris pratinjau penutupan baris Assignment `Assigned` tidak tampil pada kotak dampak
30. Klik `[Cancel]` pada dialog

### Report Missing atas aset dengan permintaan Waiting for Approval membatalkan permintaan itu
31. Ganti isi kotak search dengan `Camera Canon EOS {runId}`, tekan Enter
32. Buka menu `⋯` pada baris `Camera Canon EOS {runId}`
33. Klik `Report Missing`
34. Isi What happened `Kamera tidak ada di ruang arsip sebelum permintaan disetujui`
35. Klik `[Report Missing]` pada dialog
36. Verifikasi baris Assignment `Camera Canon EOS {runId}` berstatus `Canceled`

### Kotak dampak tidak mempratinjau Draft Assignment
37. Masuk sebagai `Rina W`
38. Buka halaman `Assets`
39. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
40. Buka menu `⋯` pada baris `Scanner Zebra DS2208 {runId}`
41. Klik `Report Missing`
42. Verifikasi kotak dampak memuat baris `The asset admins will be notified.`
43. Verifikasi baris pratinjau efek Draft Assignment `Draft Penugasan Scanner {runId}` tidak tampil pada kotak dampak
44. Klik `[Cancel]` pada dialog

### Submit Draft berhasil sesudah aset yang dilaporkan hilang dikeluarkan
45. Buka Draft Assignment `Draft Penugasan Printer {runId}`
46. Keluarkan `Printer HP LaserJet M404 {runId}` dari Draft
47. Verifikasi `Mouse Logitech MX Master 3 {runId}` tetap tercantum di Draft
48. Verifikasi `Printer HP LaserJet M404 {runId}` tidak tampil lagi di Draft
49. Klik `[Submit]` pada Draft
50. Verifikasi Submit Draft berhasil tanpa blokir

### Confirm laporan pemegang menutup baris Assigned
51. Buka halaman `Assets`
52. Klik tab `Missing`
53. Ketik Search `Monitor LG 27UL500 {runId}`, tekan Enter
54. Buka menu `⋯` pada baris `Monitor LG 27UL500 {runId}`
55. Klik `Review`
56. Klik `[Confirm]` pada dialog Missing Log
57. Verifikasi toast `Success, report has been confirmed.` tampil
58. Buka halaman `Assignment`
59. Ketik Search `Monitor LG 27UL500 {runId}`, tekan Enter
60. Verifikasi baris Assignment `Monitor LG 27UL500 {runId}` tidak lagi berstatus `Assigned`
