---
id: TC-FA-MISS-E2E-044-log-admin-dep-settings-user
title: "Transaction admin log di User Detail mencatat Report Missing, Confirm, Reject, Add Update, Mark as Found; Cancel Report pemegang tidak masuk"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§8.2#b2", "§8#r10", "§9.6#r1", "§9.6#r2", "§9.6#r3", "§9.6#r4", "§9.6#r5", "§11#r15", "§9.2#b21", "§8#r6", "EB-LOG-1", "§8.2#p14", "§8.2#p15", "§8.2#p16", "§8.2#p17", "§8.2#p18", "§8.2#p21", "§8.2#p22", "§8.2#p23", "§8.2#p24", "§8.2#p25", "§8.2#p26", "§8.2#p27", "§9.6#r7"]
smoke: []
dependsOn: ["Settings User: Detail User > Transaction admin log"]
trace:
  "§8.2#b2": [5, 17, 25, 26, 32, 34, 40, 46, 47, 48, 54]
  "§8#r10": [19]
  "§9.6#r1": [5, 9, 10]
  "§9.6#r2": [6]
  "§9.6#r3": [7]
  "§9.6#r4": [8]
  "§9.6#r5": [15]
  "§11#r15": [5]
  "§9.2#b21": [9, 10, 11]
  "§8#r6": [9, 10, 11]
  "EB-LOG-1": [15]
  "§8.2#p14": [60]
  "§8.2#p15": [5, 6, 7, 8, 9, 10, 32, 40, 46, 47]
  "§8.2#p16": [5, 32, 40, 46]
  "§8.2#p17": [32, 40, 46, 47, 48]
  "§8.2#p18": [32, 40, 46, 62]
  "§8.2#p21": [32, 40, 46]
  "§8.2#p22": [47]
  "§8.2#p23": [6]
  "§8.2#p24": [7]
  "§8.2#p25": [15]
  "§8.2#p26": [8]
  "§8.2#p27": [17, 32, 34, 40, 54]
  "§9.6#r7": [26, 47]
anchor: [25]
coverage:
  web: automated
---

# Transaction admin log di User Detail mencatat Report Missing, Confirm, Reject, Add Update, Mark as Found; Cancel Report pemegang tidak masuk

## Prerequisites
- Aktor: Total Control `Rina W`. Aktor lain yang memicu perubahan: Total Control `Dewi Anggraini {runId}` sebagai Aktor Missing.
- Layar awal: Daftar pengguna.
- Data:
  - DU-044-1: Pengguna `Dewi Anggraini {runId}`, Total Control, yang di Transaction admin log-nya sudah tercatat entri-entri pada DU-044-3 sampai DU-044-8 dan DU-044-11.
  - DU-044-2: Pengguna `Joko Santoso {runId}`, pemegang tanpa hak Aktor Missing, yang membatalkan laporannya atas `Laptop Lenovo ThinkPad T14 {runId}` lewat Cancel Report.
  - DU-044-3: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Finance Room`, dengan entri Report Missing oleh `Dewi Anggraini {runId}` di Transaction admin log.
  - DU-044-4: Asset `Scanner Zebra DS2208 {runId}`, Group `Warehouse`, dengan entri Confirm oleh `Dewi Anggraini {runId}` di Transaction admin log.
  - DU-044-5: Asset `Camera Canon EOS {runId}`, Group `Head Office`, dengan entri Reject oleh `Dewi Anggraini {runId}` di Transaction admin log.
  - DU-044-6: Asset `Projector Epson EB-X06 {runId}`, Group `Head Office`, dengan entri Mark as Found oleh `Dewi Anggraini {runId}` di Transaction admin log.
  - DU-044-7: Asset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, dengan satu entri Report Missing oleh `Dewi Anggraini {runId}` dari satu laporan banyak aset.
  - DU-044-8: Asset `Monitor LG 27UL500 {runId}`, Group `Head Office`, dengan satu entri Report Missing oleh `Dewi Anggraini {runId}` dari laporan banyak aset yang sama.
  - DU-044-9: Asset `Server Dell PowerEdge {runId}`, Group `Head Office`, yang sudah punya record Missing berjalan sehingga dilewati laporan banyak aset yang sama dan tanpa entri Report Missing.
  - DU-044-10: Asset `Laptop Lenovo ThinkPad T14 {runId}`, Group `Head Office`, dengan record Missing berstatus `Canceled` yang dibatalkan `Joko Santoso {runId}`.
  - DU-044-11: Asset `Hand Pallet Truck {runId}`, Group `Warehouse`, dengan record Missing berstatus `Missing` dan satu entri Add Update di Transaction admin log `Dewi Anggraini {runId}`.
  - DU-044-12: Asset `Drill Bosch GSB {runId}`, Group `Warehouse`, dengan record Missing berstatus `Reported Disposal` yang dilaporkan `Dewi Anggraini {runId}`.
  - DU-044-13: Asset `Handheld Honeywell CT60 {runId}`, Group `Warehouse`, dengan record Missing berstatus `Missing` yang punya node `Reported found by` dari `Dewi Anggraini {runId}` lewat `I found it`.
  - DU-044-14: Pengguna `Rina W`, Total Control.
  - DU-044-15: Update `Catatan penelusuran hari ini`.
  - DU-044-16: Pengguna `Budi Hartono {runId}`, Aktor Borrow tanpa Manage asset & TAG (Update), yang di Transaction admin log-nya sudah tercatat entri Report Missing atas DU-044-17.
  - DU-044-17: Asset `Proyektor BenQ MW535 {runId}`, Group `Head Office`, dengan satu entri Report Missing oleh `Budi Hartono {runId}` yang dilaporkan dari halaman transaksi Borrow.
  - DU-044-18: Pengguna `Sari Wulandari {runId}`, Group Manager atas Group `Warehouse` pemegang hak Aktor Missing, yang melapor dari Task Detail Audit dan di Transaction admin log-nya sudah tercatat entri Report Missing atas DU-044-19.
  - DU-044-19: Asset `Barcode Scanner Honeywell 1900 {runId}`, Group `Warehouse`, dengan satu entri Report Missing oleh `Sari Wulandari {runId}` yang dilaporkan dari Task Detail Audit.
  - DU-044-20: Pengguna `Lia Kartika {runId}`, Asset Admin sub-tab Audit tanpa hak Aktor Missing pada Group `Warehouse`, pelapor umum yang melapor dari Task Detail Audit lalu membatalkan laporannya lewat `Cancel my report` atas DU-044-21.
  - DU-044-21: Asset `Rak Server APC {runId}`, Group `Warehouse`, dengan record Missing Source `Audit` berstatus `Canceled` yang dibatalkan `Lia Kartika {runId}` dari Task Detail Audit.
  - DU-044-22: Pengguna `Hadi Pratama {runId}`, pemegang aset dengan hak Aktor Missing (Pelapor admin) yang melapor dari My Asset atas DU-044-23.
  - DU-044-23: Asset `Kamera Nikon D850 {runId}`, Group `Head Office`, dipegang `Hadi Pratama {runId}`, dengan record Missing dari laporannya lewat My Asset.
- Kondisi:
  - Akun `Rina W` dan `Dewi Anggraini {runId}` aktif dan kredensialnya disediakan fase 2.
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.

## Test Steps

### Transaction admin log mencatat aksi Aktor Missing
1. Ketik Search `Dewi Anggraini {runId}`, tekan Enter
2. Klik `Dewi Anggraini {runId}` pada kolom Name
3. Buka Transaction admin log pada User Detail
4. Klik sub-tab `Missing` pada Transaction admin log
5. Verifikasi entri Activity `Reported missing` atas `Laptop Dell Latitude 5420 {runId} - 1` tampil di Transaction admin log
6. Verifikasi entri Activity `Report confirmed` atas `Scanner Zebra DS2208 {runId} - 1` tampil di Transaction admin log
7. Verifikasi entri Activity `Report rejected` atas `Camera Canon EOS {runId} - 1` tampil di Transaction admin log
8. Verifikasi entri Activity `Marked as found` atas `Projector Epson EB-X06 {runId} - 1` tampil di Transaction admin log

### Report Missing banyak aset menulis satu entri per item yang diproses
9. Verifikasi entri Activity `Reported missing` atas `Printer HP LaserJet M404 {runId} - 1` tampil tepat satu kali di Transaction admin log
10. Verifikasi entri Activity `Reported missing` atas `Monitor LG 27UL500 {runId} - 1` tampil tepat satu kali di Transaction admin log
11. Verifikasi tidak ada entri Activity `Reported missing` atas `Server Dell PowerEdge {runId}` di Transaction admin log

### Add Update menambah satu entri
12. Catat jumlah entri Activity `Update added` atas `Hand Pallet Truck {runId} - 1` di Transaction admin log
13. `Dewi Anggraini {runId}` menambah Update `Catatan penelusuran hari ini` pada record `Hand Pallet Truck {runId}` lewat Add Update
14. Muat ulang halaman
15. Verifikasi jumlah entri Activity `Update added` atas `Hand Pallet Truck {runId} - 1` bertambah satu dari jumlah yang dicatat

### Report Disposal dan jalur I found it tercatat di log yang dinyatakan
16. Klik sub-tab `Disposal` pada Transaction admin log
17. Verifikasi entri Report Disposal atas `Drill Bosch GSB {runId}` tampil di sub-tab Disposal
18. Klik tab `Activity Log` pada User Detail
19. Verifikasi entri aksi `I found it` atas `Handheld Honeywell CT60 {runId}` tampil di Activity Log

### Cancel Report pemegang tidak masuk Transaction admin log
20. Buka daftar pengguna
21. Ketik Search `Joko Santoso {runId}`, tekan Enter
22. Klik `Joko Santoso {runId}` pada kolom Name
23. Buka Transaction admin log pada User Detail
24. Klik sub-tab `Missing` pada Transaction admin log
25. Verifikasi kolom Transaction admin log sub-tab `Missing` berurutan `Date`, `Activity`, `Name`, `Source`, `Group`
26. Verifikasi tidak ada entri Cancel Report atas `Laptop Lenovo ThinkPad T14 {runId}` di Transaction admin log

### Report Missing oleh Pelapor admin dari halaman transaksi dan dari Task Detail Audit tercatat di log pelapornya
27. Buka daftar pengguna
28. Ketik Search `Budi Hartono {runId}`, tekan Enter
29. Klik `Budi Hartono {runId}` pada kolom Name
30. Buka Transaction admin log pada User Detail
31. Klik sub-tab `Missing` pada Transaction admin log
32. Verifikasi entri Activity `Reported missing` atas `Proyektor BenQ MW535 {runId} - 1` dengan Source `Borrow` dan Group `Head Office` tampil di Transaction admin log
33. Klik sub-tab `Borrow` pada Transaction admin log
34. Verifikasi sub-tab `Borrow` tidak memuat baris Report Missing atas `Proyektor BenQ MW535 {runId} - 1`
35. Buka daftar pengguna
36. Ketik Search `Sari Wulandari {runId}`, tekan Enter
37. Klik `Sari Wulandari {runId}` pada kolom Name
38. Buka Transaction admin log pada User Detail
39. Klik sub-tab `Missing` pada Transaction admin log
40. Verifikasi entri Activity `Reported missing` atas `Barcode Scanner Honeywell 1900 {runId} - 1` dengan Source `Audit` dan Group `Warehouse` tampil di Transaction admin log

### Pelapor umum dan Cancel Report dari Task Detail Audit tercatat, aksi dari layar pemegang tidak
41. Buka daftar pengguna
42. Ketik Search `Lia Kartika {runId}`, tekan Enter
43. Klik `Lia Kartika {runId}` pada kolom Name
44. Buka Transaction admin log pada User Detail
45. Klik sub-tab `Missing` pada Transaction admin log
46. Verifikasi entri Activity `Reported missing` atas `Rak Server APC {runId} - 1` dengan Source `Audit` dan Group `Warehouse` tampil walau `Lia Kartika {runId}` pelapor umum
47. Verifikasi entri Activity `Report canceled` atas `Rak Server APC {runId} - 1` dengan Source `Audit` dan Group `Warehouse` tampil dari Cancel Report di Task Detail Audit
48. Verifikasi baris `Reported missing` dan `Report canceled` atas `Rak Server APC {runId} - 1` memakai Source yang sama
49. Buka daftar pengguna
50. Ketik Search `Hadi Pratama {runId}`, tekan Enter
51. Klik `Hadi Pratama {runId}` pada kolom Name
52. Buka Transaction admin log pada User Detail
53. Klik sub-tab `Missing` pada Transaction admin log
54. Verifikasi tidak ada baris untuk aset `Kamera Nikon D850 {runId}` di Transaction admin log walau `Hadi Pratama {runId}` adalah Pelapor admin, karena Report Missing dari layar pemegang aset hanya masuk Missing Log dan User Log

### Kolom Date memakai format General Settings
55. Buka daftar pengguna
56. Ketik Search `Dewi Anggraini {runId}`, tekan Enter
57. Klik `Dewi Anggraini {runId}` pada kolom Name
58. Buka Transaction admin log pada User Detail
59. Klik sub-tab `Missing` pada Transaction admin log
60. Verifikasi kolom Date baris `Laptop Dell Latitude 5420 {runId} - 1` memakai format tanggal `DD/MM/YY` dan format waktu `HH:mm`

### Kolom Group menampilkan hierarki grup saat hover
61. Arahkan kursor ke badge Group pada baris `Laptop Dell Latitude 5420 {runId} - 1`
62. Verifikasi hover pada badge Group memuat hierarki grup dari Group `Finance Room`
