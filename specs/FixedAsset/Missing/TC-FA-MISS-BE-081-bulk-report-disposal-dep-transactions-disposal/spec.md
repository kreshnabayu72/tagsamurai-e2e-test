---
id: TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal
title: "Server: Bulk Report Disposal memproses hanya record Missing yang berhak dan bukan Last holder, cek satu Group atas record yang diproses, satu node per record diproses"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§4.1a#p9", "§6#r11", "§6#r12", "§6#r13", "§9.2#b17", "§9.4.2#r21", "§9.4.4#r4", "§9.6#r10", "§8#r6", "§9.1#r5", "§2.1#r9", "§2.1#r10", "§4.8#r9", "EB-BLK-3", "EB-AKS-3@bulk-report-disposal", "§9.2#b32", "§9.2#b33", "§9.4.4#r18", "§9.4.4#r19", "§9.4.2#r3", "§8.1#r15"]
smoke: []
dependsOn: ["Transactions Disposal: Disposal Report"]
trace:
  "§4.1a#p9": [3, 4, 5, 14, 21, 22]
  "§6#r11": 17
  "§6#r12": [3, 4, 5, 22]
  "§6#r13": [12, 14]
  "§9.2#b17": [17, 22]
  "§9.4.2#r21": 17
  "§9.4.4#r4": 18
  "§9.6#r10": [6, 7, 8]
  "§8#r6": [6, 7, 12, 23]
  "§9.1#r5": 3
  "§2.1#r9": [3, 21, 25, 27, 29, 31, 33]
  "§2.1#r10": [35, 37, 39, 41, 43, 45, 49]
  "§4.8#r9": [5, 10, 27, 29, 37, 41]
  "EB-BLK-3": [10, 12]
  "EB-AKS-3@bulk-report-disposal": [29, 31, 33, 49]
  "§9.2#b32": [52, 55]
  "§9.2#b33": [57, 59, 62, 64]
  "§9.4.4#r18": [53, 55]
  "§9.4.4#r19": [57, 59, 60]
  "§9.4.2#r3": [52, 57]
  "§8.1#r15": [6, 21, 25, 27]
---

# Server: Bulk Report Disposal memproses hanya record Missing yang berhak dan bukan Last holder, cek satu Group atas record yang diproses, satu node per record diproses

## Prerequisites
- Aktor:
  - Aktor Missing A: Total Control, cakupan seluruh client, juga Aktor Disposal dan Pelapor admin.
  - Group Manager: Group binaan `Head Office` beserta sub-group, tanpa Group binaan `Warehouse`.
  - Staf Pengelola: Manage asset & TAG dengan Update pada Group `Head Office`.
  - Staf Accounting: Manage accounting dengan Read dan Update.
  - Pengguna Read Only: Read Only tanpa hak Report Disposal.
  - Pengguna View asset value: View asset value tanpa hak Report Disposal.
  - Pemegang: pemegang aset tanpa hak Report Disposal.
- Data:
  - DU-081-1: Missing record berstatus `Missing`, Source `Manual`, aset `Laptop HP ProBook 450 {runId}` di Group `Head Office`, bukan Last holder Aktor Missing A.
  - DU-081-2: Missing record berstatus `Missing`, Source `Manual`, aset `Monitor Dell U2723QE {runId}` di Group `Head Office`, bukan Last holder Aktor Missing A.
  - DU-081-3: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Kamera Sony Alpha A7 {runId}` di Group `Head Office`, Disposal Report berstatus `Reported`.
  - DU-081-4: Missing record berstatus `Missing`, Source `Manual`, aset `Printer Brother HL-L2375 {runId}` di Group `Head Office`, Last holder Aktor Missing A.
  - DU-081-5: Missing record berstatus `Missing`, Source `Manual`, aset `Tablet Lenovo Tab M10 {runId}` di Group `Head Office`.
  - DU-081-6: Missing record berstatus `Missing`, Source `Manual`, aset `Rak Server APC NetShelter {runId}` di Group `Warehouse`.
  - DU-081-7: Missing record berstatus `Missing`, Source `Manual`, aset `Mikrofon Shure SM58 {runId}` di Group `Head Office`.
  - DU-081-8: Missing record berstatus `Missing`, Source `Manual`, aset `Forklift Hyster H2.5 {runId}` di Group `Warehouse`.
  - DU-081-9: Missing record berstatus `Missing`, Source `Manual`, aset `Proyektor Epson EB-X49 {runId}` di Group `Head Office`.
  - DU-081-10: Missing record berstatus `Missing`, Source `Manual`, aset `Router Mikrotik RB4011 {runId}` di Group `Head Office`, tidak dalam transaksi.
  - DU-081-11: Missing record berstatus `Missing`, Source `Manual`, aset `Switch TP-Link TL-SG3428 {runId}` di Group `Head Office`.
  - DU-081-12: Missing record berstatus `Missing`, Source `Manual`, aset `Genset Cummins C20D5 {runId}` di Group `Head Office`.
  - DU-081-13: Missing record berstatus `Missing`, Source `Manual`, aset `Dispenser Cosmos CWD-1100 {runId}` di Group `Head Office`.
  - DU-081-14: aset `Mesin Fotokopi Ricoh MP2014 {runId}` di Group `Head Office`, belum punya record Missing berjalan, dengan Disposal Report berstatus `Reported` Source `Manual`.
  - DU-081-15: aset `Laptop Asus ExpertBook B1 {runId}` di Group `Head Office`, belum punya record Missing berjalan, dengan Disposal Report berstatus `Reported` Source `Damaged`.
  - DU-081-16: aset `Lemari Besi Lion {runId}` di Group `Head Office`, belum punya record Missing berjalan, dengan satu baris Disposal berjenis Sell `Waiting for Approval` dan satu baris Disposal `Draft`.
  - DU-081-17: aset `Kursi Kantor Chitose {runId}` di Group `Head Office`, belum punya record Missing berjalan, dengan satu baris Disposal berjenis Sell `Waiting for Execution`.
  - DU-081-18: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Mobil Toyota Avanza {runId}` di Group `Head Office`, Disposal Report berstatus `Reported`.
  - DU-081-19: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `Mesin Bubut Krisbow {runId}` di Group `Head Office`, baris Disposal Write-off `Waiting for Approval`.
  - DU-081-20: Reason `Aset tidak pernah ditemukan sejak inventaris tahunan`, dipakai Aktor Missing A.
  - DU-081-21: Reason `Aset hilang sejak pindah kantor cabang`, dipakai Group Manager.
  - DU-081-22: Reason `Aset sudah tidak layak dicari lagi`, dipakai Staf Pengelola.
  - DU-081-23: Reason `Aset diusulkan dihapus dari pembukuan`, dipakai Staf Accounting.
  - DU-081-24: Reason `Percobaan tanpa hak akses`, dipakai pengguna tanpa hak Report Disposal.
  - DU-081-25: What happened `Aset tidak ditemukan di ruang penyimpanan setelah renovasi`, dipakai Aktor Missing A.
- Kondisi:
  - Tidak satu pun aktor selain Aktor Missing A menjadi Last holder record di Data.
  - Jumlah notifikasi `missing_*`, jumlah node Missing Log, jumlah entri Activity Log dan System Log, serta jumlah Disposal Report dicatat sebelum aksi pertama atas record terkait.
  - Cakupan Group Aktor Missing A meliputi `Head Office` dan `Warehouse`.

## Test Steps

### Bulk Report Disposal campuran memproses record Missing yang berhak dan melewati record lain
1. Catat jumlah node record DU-081-1, DU-081-2, DU-081-3, dan DU-081-4, jumlah Disposal Report aset DU-081-1 sampai DU-081-4 di Transactions Disposal, jumlah entri Activity Log dan System Log Aktor Missing A, dan jumlah notifikasi `missing_*` untuk keempat record sebelum aksi
2. Aktor Missing A melakukan Bulk Report Disposal atas record DU-081-1, DU-081-2, DU-081-3, dan DU-081-4 yang semuanya di Group `Head Office` dengan Reason `Aset tidak pernah ditemukan sejak inventaris tahunan`
3. Verifikasi record DU-081-1 dan DU-081-2 menjadi `Reported Disposal` dan masing-masing mendapat satu Disposal Report berstatus `Reported` di Transactions Disposal
4. Verifikasi record DU-081-3 dilewati karena statusnya sudah bukan `Missing`: status tetap `Reported Disposal`, tanpa Disposal Report tambahan dan tanpa node baru
5. Verifikasi record DU-081-4 dilewati karena Aktor Missing A adalah Last holder-nya: status tetap `Missing`, tanpa Disposal Report dan tanpa node
6. Verifikasi record DU-081-1 dan DU-081-2 masing-masing memuat satu node `Disposal reported by` dengan Reason `Aset tidak pernah ditemukan sejak inventaris tahunan` dan tanpa Report ID, sedangkan record DU-081-3 dan DU-081-4 tidak mendapat node
7. Verifikasi Activity Log dan System Log Aktor Missing A masing-masing bertambah dua entri, satu per record yang diproses, tanpa entri untuk record DU-081-3 dan DU-081-4
8. Verifikasi Bulk Report Disposal tidak memicu notifikasi `missing_*` baru untuk keempat record dibanding sebelum aksi

### Penolakan Report Disposal satu record konsisten dengan record yang dilewati pada Bulk
9. Aktor Missing A melakukan Report Disposal atas record DU-081-4 dengan Reason `Aset tidak pernah ditemukan sejak inventaris tahunan`
10. Verifikasi Report Disposal atas record DU-081-4 ditolak dengan pesan `You were holding this asset. Ask another admin.`, status record tetap `Missing`, dan tidak ada Disposal Report baru, sama dengan perlakuan record itu pada Bulk

### Konfirmasi ulang Bulk memproses setiap record sekali dan semua dilewati tidak menulis apa pun
11. Aktor Missing A melakukan Bulk Report Disposal atas record DU-081-1 dan DU-081-2 sekali lagi dengan Reason `Aset tidak pernah ditemukan sejak inventaris tahunan`
12. Verifikasi pengulangan itu melewati kedua record karena sudah `Reported Disposal`: tetap satu Disposal Report dan satu node `Disposal reported by` per record, dan entri Activity Log serta System Log tidak bertambah
13. Aktor Missing A melakukan Bulk Report Disposal atas record DU-081-3 dan DU-081-4 dengan Reason `Aset tidak pernah ditemukan sejak inventaris tahunan`
14. Verifikasi semua record terpilih dilewati: tidak ada Disposal Report baru, tidak ada node baru, tidak ada entri Activity Log atau System Log baru, dan status kedua record tidak berubah

### Seleksi lintas Group ditolak seluruhnya
15. Catat jumlah node record DU-081-5 dan DU-081-6, jumlah Disposal Report aset DU-081-5 dan DU-081-6, jumlah entri Activity Log dan System Log Aktor Missing A, dan jumlah notifikasi `missing_*` untuk kedua record sebelum aksi
16. Aktor Missing A melakukan Bulk Report Disposal atas record DU-081-5 di Group `Head Office` dan record DU-081-6 di Group `Warehouse` dengan Reason `Aset tidak pernah ditemukan sejak inventaris tahunan`
17. Verifikasi Bulk itu ditolak seluruhnya karena record yang akan diproses berasal dari lebih dari satu Group: kedua record tetap `Missing`, tanpa Disposal Report dan tanpa node
18. Verifikasi penolakan itu tidak menambah entri Activity Log atau System Log dan tidak memicu notifikasi `missing_*` baru

### Cek satu Group hanya menghitung record yang diproses
19. Catat jumlah node record DU-081-7 dan DU-081-8, jumlah Disposal Report kedua aset, serta jumlah entri Activity Log dan System Log Group Manager sebelum aksi
20. Group Manager dengan Group binaan `Head Office` melakukan Bulk Report Disposal atas record DU-081-7 di Group `Head Office` dan record DU-081-8 di Group `Warehouse` dengan Reason `Aset hilang sejak pindah kantor cabang`
21. Verifikasi record DU-081-7 menjadi `Reported Disposal` dengan satu Disposal Report berstatus `Reported` dan satu node `Disposal reported by` yang memuat Reason `Aset hilang sejak pindah kantor cabang`
22. Verifikasi record DU-081-8 dilewati karena Group `Warehouse` di luar hak Report Disposal Group Manager: status tetap `Missing`, tanpa Disposal Report dan tanpa node, dan seleksi tidak ditolak sebagai lintas Group karena cek Group hanya menghitung record yang diproses
23. Verifikasi Activity Log dan System Log Group Manager masing-masing bertambah satu entri, untuk record DU-081-7 saja

### Hak Report Disposal per aktor pada Bulk
24. Staf Pengelola dengan Manage asset & TAG (Update) pada Group `Head Office` melakukan Bulk Report Disposal atas record DU-081-9 dengan Reason `Aset sudah tidak layak dicari lagi`
25. Verifikasi record DU-081-9 menjadi `Reported Disposal` dengan satu Disposal Report berstatus `Reported` dan satu node `Disposal reported by` yang memuat Reason `Aset sudah tidak layak dicari lagi`
26. Staf Accounting dengan Manage accounting Read dan Update melakukan Bulk Report Disposal atas record DU-081-10 dengan Reason `Aset diusulkan dihapus dari pembukuan`
27. Verifikasi record DU-081-10 menjadi `Reported Disposal` dengan satu Disposal Report berstatus `Reported` karena aset Missing tidak dalam transaksi, dan satu node `Disposal reported by` yang memuat Reason `Aset diusulkan dihapus dari pembukuan`
28. Pengguna Read Only melakukan Bulk Report Disposal atas record DU-081-11 dengan Reason `Percobaan tanpa hak akses`
29. Verifikasi Bulk itu ditolak server walau antarmuka dilewati: record DU-081-11 tetap `Missing`, tanpa Disposal Report, tanpa node, dan tanpa entri log baru
30. Pengguna dengan View asset value melakukan Bulk Report Disposal atas record DU-081-12 dengan Reason `Percobaan tanpa hak akses`
31. Verifikasi Bulk itu ditolak server: record DU-081-12 tetap `Missing`, tanpa Disposal Report, tanpa node, dan tanpa entri log baru
32. Pemegang melakukan Bulk Report Disposal atas record DU-081-13 dengan Reason `Percobaan tanpa hak akses`
33. Verifikasi Bulk itu ditolak server: record DU-081-13 tetap `Missing`, tanpa Disposal Report, tanpa node, dan tanpa entri log baru

### Cancel Disposal Report hanya oleh yang berhak atas laporan itu
34. Staf Pengelola melakukan Cancel Disposal Report atas record DU-081-1 yang Report-nya dibuat Aktor Missing A
35. Verifikasi Cancel Disposal Report ditolak karena bukan laporan miliknya: record DU-081-1 tetap `Reported Disposal` dan Disposal Report tetap `Reported`
36. Staf Pengelola melakukan Cancel Disposal Report atas record DU-081-9 yang Report-nya dibuat Staf Pengelola
37. Verifikasi record DU-081-9 kembali `Missing` karena laporan miliknya sendiri
38. Staf Accounting melakukan Cancel Disposal Report atas record DU-081-2 yang Report-nya dibuat Aktor Missing A
39. Verifikasi Cancel Disposal Report ditolak karena bukan laporan miliknya: record DU-081-2 tetap `Reported Disposal`
40. Staf Accounting melakukan Cancel Disposal Report atas record DU-081-10 yang Report-nya dibuat Staf Accounting
41. Verifikasi record DU-081-10 kembali `Missing` karena laporan miliknya sendiri
42. Group Manager melakukan Cancel Disposal Report atas record DU-081-2 di Group binaannya yang Report-nya dibuat Aktor Missing A
43. Verifikasi record DU-081-2 kembali `Missing` karena Group Manager berhak atas Group binaan
44. Aktor Missing A melakukan Cancel Disposal Report atas record DU-081-7 yang Report-nya dibuat Group Manager
45. Verifikasi record DU-081-7 kembali `Missing` karena Total Control berhak atas semua laporan
46. Pengguna Read Only melakukan Cancel Disposal Report atas record DU-081-1
47. Pengguna dengan View asset value melakukan Cancel Disposal Report atas record DU-081-1
48. Pemegang melakukan Cancel Disposal Report atas record DU-081-1
49. Verifikasi ketiga permintaan itu ditolak server dan record DU-081-1 tetap `Reported Disposal` dengan Disposal Report tetap `Reported`

### Report Missing menutup Report dan baris Disposal oleh System tanpa node di Missing Log
50. Catat jumlah entri Activity Log dan System Log Aktor Missing A, jumlah notifikasi `missing_reported`, dan status Disposal Report serta baris Disposal aset DU-081-14, DU-081-15, DU-081-16, dan DU-081-17 sebelum aksi
51. Aktor Missing A melakukan Report Missing atas aset DU-081-14 dengan What happened `Aset tidak ditemukan di ruang penyimpanan setelah renovasi`
52. Verifikasi Disposal Report aset DU-081-14 menjadi `Canceled` oleh `System` dengan alasan `Asset reported missing`
53. Verifikasi record Missing baru aset DU-081-14 dimulai dari node `Reported missing by` dan tidak memuat node apa pun dari penutupan Report itu, dan tidak ada notifikasi `missing_*` selain satu `missing_reported`
54. Aktor Missing A melakukan Report Missing atas aset DU-081-15 dengan What happened `Aset tidak ditemukan di ruang penyimpanan setelah renovasi`
55. Verifikasi Disposal Report aset DU-081-15 yang Source-nya `Damaged` menjadi `Canceled` oleh `System` dengan alasan `Asset reported missing`, dan record Missing baru dimulai dari node `Reported missing by` tanpa node dari penutupan itu
56. Aktor Missing A melakukan Report Missing atas aset DU-081-16 dengan What happened `Aset tidak ditemukan di ruang penyimpanan setelah renovasi`
57. Verifikasi baris Disposal berjenis Sell `Waiting for Approval` aset DU-081-16 menjadi `Canceled` oleh `System` dengan alasan `Asset reported missing`, baris `Draft` tidak diubah, dan aset ditandai ⚠
58. Aktor Missing A melakukan Report Missing atas aset DU-081-17 dengan What happened `Aset tidak ditemukan di ruang penyimpanan setelah renovasi`
59. Verifikasi baris Disposal berjenis Sell `Waiting for Execution` aset DU-081-17 menjadi `Canceled` oleh `System` dengan alasan `Asset reported missing`, dan record Missing baru dimulai dari node `Reported missing by` tanpa node dari penutupan baris itu
60. Verifikasi penutupan baris Disposal aset DU-081-16 dan DU-081-17 tidak memicu notifikasi `missing_*` selain satu `missing_reported` per Report Missing
61. Aktor Missing A melakukan Report Missing atas aset DU-081-18 yang record Missing-nya `Reported Disposal`
62. Verifikasi Report Missing atas aset DU-081-18 ditolak karena aset sudah punya record Missing berjalan: tidak ada record baru dan Disposal Report aset itu tetap `Reported`
63. Aktor Missing A melakukan Report Missing atas aset DU-081-19 yang record Missing-nya `In Disposal Process`
64. Verifikasi Report Missing atas aset DU-081-19 ditolak karena aset sudah punya record Missing berjalan: tidak ada record baru dan baris Disposal Write-off aset itu tetap `Waiting for Approval`
