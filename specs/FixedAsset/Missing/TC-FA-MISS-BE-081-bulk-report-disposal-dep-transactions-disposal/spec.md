---
id: TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal
title: "Server: Bulk Report Disposal memproses hanya record Missing yang berhak dan bukan Last holder, cek satu Group atas record yang diproses, satu node per record diproses"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [§4.1a#p9, §6#r11, §6#r12, §6#r13, §9.2#b17, §9.4.2#r21, §9.4.4#r4, §9.6#r10, §8#r6, §9.1#r5, §2.1#r9, §2.1#r10, §4.8#r9, EB-BLK-3, EB-AKS-3@bulk-report-disposal, §9.2#b32, §9.2#b33, §9.4.4#r18, §9.4.4#r19, §9.4.2#r3]
smoke: []
dependsOn: ["Transactions Disposal: Disposal Report"]
trace:
  §4.1a#p9: [7, 8, 9, 12]
  §6#r11: [9, 15]
  §6#r12: [7, 8]
  §6#r13: [12, 13]
  §9.2#b17: [15, 16]
  §9.4.2#r21: [15, 16]
  §9.4.4#r4: 15
  §9.6#r10: [3, 5, 8]
  §8#r6: [4, 10]
  §9.1#r5: 3
  §2.1#r9: [18, 20, 40, 42]
  §2.1#r10: [22, 24, 26, 28]
  §4.8#r9: [18, 20, 22, 24, 26, 28, 40, 42]
  EB-BLK-3: [3, 4]
  EB-AKS-3@bulk-report-disposal: 18
  §9.2#b32: 30
  §9.2#b33: [32, 34, 36, 37]
  §9.4.4#r18: [30, 38]
  §9.4.4#r19: [32, 34, 37, 38]
  §9.4.2#r3: [30, 32]
---

# Server: Bulk Report Disposal memproses hanya record Missing yang berhak dan bukan Last holder, cek satu Group atas record yang diproses, satu node per record diproses

## Prerequisites
- Aktor: Rina W, Total Control dengan cakupan seluruh client dan Aktor Disposal; pengguna lain pada entri data DU-081-1 sampai DU-081-5 dengan peran dan cakupan seperti tercatat di entri; approver dan job sistem hanya sebagai pemicu keadaan.
- Data:
  - DU-081-1: User Name `Maya Anggraini {runId}`, Peran `Group Manager dan Aktor Disposal`, Cakupan `Group Head Office beserta sub-group`.
  - DU-081-2: User Name `Dewi Anindita {runId}`, Peran `Manage asset & TAG dengan Update pada Head Office`, Cakupan `Head Office beserta descendant`.
  - DU-081-3: User Name `Eko Wibowo {runId}`, Peran `Accounting dengan Manage accounting Read dan Update`, Cakupan `seluruh client`.
  - DU-081-4: User Name `Fajar Nugroho {runId}`, Peran `Read Only`, Cakupan `seluruh client`.
  - DU-081-5: User Name `Joko Susilo {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Cakupan `aset yang ia pegang`.
  - DU-081-6: Asset Name `Laptop Dell Latitude 5420 {runId}`, Asset ID `FA081-001`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-081-7: Asset Name `Hand Pallet Truck {runId}`, Asset ID `FA081-002`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-081-8: Asset Name `Projector Epson EB-X06 {runId}`, Asset ID `FA081-003`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-081-9: Asset Name `Camera Canon EOS {runId}`, Asset ID `FA081-004`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-081-10: Asset Name `Printer HP LaserJet M404 {runId}`, Asset ID `FA081-005`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`.
  - DU-081-11: Asset Name `Monitor LG 27UL500 {runId}`, Asset ID `FA081-006`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Maya Anggraini {runId}`, Last holder `Maya Anggraini {runId}`.
  - DU-081-12: Asset Name `Toyota Innova {runId}`, Asset ID `FA081-007`, Group aset `Warehouse`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-081-13: Asset Name `Drill Bosch GSB {runId}`, Asset ID `FA081-008`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-081-14: Asset Name `Genset Honda EU22 {runId}`, Asset ID `FA081-009`, Group aset `Warehouse`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-081-15: Asset Name `Kursi Ergonomis {runId}`, Asset ID `FA081-010`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-081-16: Asset Name `Meja Kerja Kayu {runId}`, Asset ID `FA081-011`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-081-17: Asset Name `Papan Tulis {runId}`, Asset ID `FA081-012`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`.
  - DU-081-18: Asset Name `Tablet Samsung Tab A8 {runId}`, Asset ID `FA081-013`, Group aset `Finance Room`, Record berjalan `Reported Disposal, dilaporkan Eko Wibowo {runId}`.
  - DU-081-19: Asset Name `Kamera Sony A7 {runId}`, Asset ID `FA081-014`, Group aset `Finance Room`, Record berjalan `Reported Disposal, dilaporkan Rina W`.
  - DU-081-20: Asset Name `Scanner Zebra DS2208 {runId}`, Asset ID `FA081-015`, Group aset `Finance Room`, Record berjalan `Reported Disposal, dilaporkan Rina W`.
  - DU-081-21: Asset Name `Rak Besi Gudang {runId}`, Asset ID `FA081-016`, Group aset `Warehouse`, Record berjalan `Reported Disposal, dilaporkan Rina W`.
  - DU-081-22: Asset Name `Brankas Besi {runId}`, Asset ID `FA081-017`, Group aset `Finance Room`, Record berjalan `tidak ada`, Disposal Report `Reported`.
  - DU-081-23: Asset Name `Dispenser Air Galon {runId}`, Asset ID `FA081-019`, Group aset `Finance Room`, Record berjalan `tidak ada`, Baris Disposal `Sell, Waiting for Execution`.
  - DU-081-24: Asset Name `Lemari Arsip Besi {runId}`, Asset ID `FA081-018`, Group aset `Finance Room`, Record berjalan `tidak ada`, Baris Disposal `Sell, Waiting for Approval`, Draft Disposal `ada`.
- Kondisi:
  - Long missing after bernilai `30`

## Test Steps
### Bulk Report Disposal atas record Missing satu Group memproses setiap record sekali
1. Rina W menjalankan Bulk Report Disposal atas `Laptop Dell Latitude 5420 {runId}`, `Hand Pallet Truck {runId}`, dan `Projector Epson EB-X06 {runId}` dengan satu Reason `Aset tidak ditemukan setelah pencarian dua pekan`
2. Rina W mengirim konfirmasi Bulk Report Disposal yang sama sekali lagi secara beruntun
3. Verifikasi ketiga record berstatus `Reported Disposal` dan masing-masing punya tepat satu Disposal Report dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan` yang sama, walau konfirmasi dikirim dua kali
4. Verifikasi masing-masing record memuat tepat satu node `Disposal reported by` dan satu entri log per record, tanpa pasangan ganda dari konfirmasi kedua
5. Verifikasi hasil sukses penuh tidak memuat kalimat dilewati

### Record yang bukan Missing, Last holder, atau di luar hak Group dilewati
6. `Maya Anggraini {runId}` menjalankan Bulk Report Disposal atas `Camera Canon EOS {runId}`, `Printer HP LaserJet M404 {runId}`, `Monitor LG 27UL500 {runId}`, dan `Toyota Innova {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
7. Verifikasi hanya `Camera Canon EOS {runId}` yang diproses dan berstatus `Reported Disposal`, sedangkan `Printer HP LaserJet M404 {runId}` (bukan `Missing`), `Monitor LG 27UL500 {runId}` (`Maya Anggraini {runId}` adalah Last holder), dan `Toyota Innova {runId}` (di luar hak Group `Warehouse`) dilewati dan tetap pada status semula
8. Verifikasi hasil memuat pesan `Success, disposal report has been created. Some items were skipped.`
9. Verifikasi cek satu Group hanya menghitung `Camera Canon EOS {runId}` yang diproses, sehingga `Toyota Innova {runId}` di Group lain tidak menggagalkan seleksi
10. Verifikasi hanya `Camera Canon EOS {runId}` yang memuat node `Disposal reported by`, sedangkan record yang dilewati tanpa node

### Semua record terpilih dilewati tidak membuat Disposal Report
11. `Maya Anggraini {runId}` menjalankan Bulk Report Disposal atas `Printer HP LaserJet M404 {runId}` dan `Monitor LG 27UL500 {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
12. Verifikasi permintaan itu ditolak dengan pesan `None of the selected records can be reported for disposal.`, tanpa pesan sukses
13. Verifikasi `Printer HP LaserJet M404 {runId}` dan `Monitor LG 27UL500 {runId}` tidak mendapat Disposal Report maupun node baru dan tetap pada status semula

### Seleksi lintas Group ditolak seluruhnya
14. Rina W menjalankan Bulk Report Disposal atas `Drill Bosch GSB {runId}` di Group `Finance Room` dan `Genset Honda EU22 {runId}` di Group `Warehouse` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
15. Verifikasi permintaan itu ditolak dengan pesan `Selected assets come from more than one group. Select assets from one group.`, dan tidak ada Disposal Report yang dibuat untuk `Drill Bosch GSB {runId}` maupun `Genset Honda EU22 {runId}`
16. Verifikasi `Drill Bosch GSB {runId}` dan `Genset Honda EU22 {runId}` tetap berstatus `Missing` tanpa node baru

### Aktor tanpa hak Report Disposal ditolak walau UI dilewati
17. `Fajar Nugroho {runId}` dan `Joko Susilo {runId}` masing-masing menjalankan Bulk Report Disposal atas `Kursi Ergonomis {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
18. Verifikasi kedua permintaan itu ditolak dan record `Kursi Ergonomis {runId}` tetap `Missing`

### Accounting melaporkan hanya aset Missing dan membatalkan hanya laporan miliknya
19. `Eko Wibowo {runId}` menjalankan Bulk Report Disposal atas `Meja Kerja Kayu {runId}` dan `Papan Tulis {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
20. Verifikasi `Meja Kerja Kayu {runId}` berstatus `Reported Disposal` dan `Papan Tulis {runId}` yang berstatus `Waiting for Confirmation` dilewati, karena Accounting hanya boleh melaporkan aset Missing
21. `Eko Wibowo {runId}` menjalankan Cancel Disposal Report atas record `Tablet Samsung Tab A8 {runId}` yang dilaporkan `Eko Wibowo {runId}`
22. Verifikasi record `Tablet Samsung Tab A8 {runId}` kembali berstatus `Missing` karena laporan itu milik `Eko Wibowo {runId}`
23. `Eko Wibowo {runId}` menjalankan Cancel Disposal Report atas record `Kamera Sony A7 {runId}` yang dilaporkan Rina W
24. Verifikasi permintaan itu ditolak karena bukan laporan milik `Eko Wibowo {runId}`, dan record `Kamera Sony A7 {runId}` tetap `Reported Disposal`

### Group Manager membatalkan Disposal Report hanya di Group binaan
25. `Maya Anggraini {runId}` menjalankan Cancel Disposal Report atas record `Scanner Zebra DS2208 {runId}` di Group `Finance Room`
26. Verifikasi record `Scanner Zebra DS2208 {runId}` kembali berstatus `Missing` karena Group `Finance Room` adalah Group binaan `Maya Anggraini {runId}`
27. `Maya Anggraini {runId}` menjalankan Cancel Disposal Report atas record `Rak Besi Gudang {runId}` di Group `Warehouse`
28. Verifikasi permintaan itu ditolak karena Group `Warehouse` bukan Group binaan, dan record `Rak Besi Gudang {runId}` tetap `Reported Disposal`

### Report Missing atas aset dengan Report atau baris Disposal berjalan membatalkannya oleh System
29. Rina W mengirim Report Missing atas `Brankas Besi {runId}` yang punya Disposal Report `Reported` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
30. Verifikasi Disposal Report `Brankas Besi {runId}` menjadi `Canceled` oleh `System` dengan alasan `Asset reported missing`, dan aset mendapat record Missing baru
31. Rina W mengirim Report Missing atas `Lemari Arsip Besi {runId}` yang punya baris Disposal Sell berstatus Waiting for Approval dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
32. Verifikasi baris Disposal `Lemari Arsip Besi {runId}` menjadi `Canceled` oleh `System` dengan alasan `Asset reported missing`, dan aset mendapat record Missing baru
33. Rina W mengirim Report Missing atas `Dispenser Air Galon {runId}` yang punya baris Disposal Sell berstatus Waiting for Execution dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
34. Verifikasi baris Disposal `Dispenser Air Galon {runId}` menjadi `Canceled` oleh `System` dengan alasan `Asset reported missing`, dan aset mendapat record Missing baru
35. Rina W mengirim Report Missing atas `Kamera Sony A7 {runId}` yang berstatus `Reported Disposal` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
36. Verifikasi permintaan itu ditolak dengan keterangan `Already reported missing` karena aset sudah punya record berjalan `Reported Disposal`, dan tidak ada record Missing kedua
37. Verifikasi Draft Disposal aset `Lemari Arsip Besi {runId}` tidak berubah dan aset ditandai ⚠
38. Verifikasi pembatalan oleh `System` pada `Brankas Besi {runId}` dan `Lemari Arsip Besi {runId}` tidak mengirim event `missing_*` selain `missing_reported` untuk laporan baru

### Manage asset & TAG dengan Update melaporkan disposal aset Missing hanya di Group yang ia pegang Update
39. `Dewi Anindita {runId}` menjalankan Bulk Report Disposal atas `Kursi Ergonomis {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
40. Verifikasi permintaan itu diterima dan record `Kursi Ergonomis {runId}` berstatus `Reported Disposal`
41. `Dewi Anindita {runId}` menjalankan Bulk Report Disposal atas `Toyota Innova {runId}` di Group `Warehouse` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
42. Verifikasi permintaan itu ditolak dengan pesan `None of the selected records can be reported for disposal.` karena Group `Warehouse` di luar hak Update `Dewi Anindita {runId}`, dan record `Toyota Innova {runId}` tetap `Missing`
