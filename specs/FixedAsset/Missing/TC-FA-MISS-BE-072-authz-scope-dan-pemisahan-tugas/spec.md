---
id: TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas
title: "Server: cakupan Group, capability per aksi, Last holder, kepemilikan pemegang, Missing Log di luar cakupan, dan filter atau sort kolom finansial ditolak"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [§9.3#b1, §9.3#b2, §9.2#b23, §9.4.2#r20, §9.4.4#r9, §9.4.4#r14, §9.11#r1, §9.11#r2, §9.11#b1, §6#r1, §6#r6, §2.1#r12, §2.1#p10, §2.1#p20, §9.4.1#r4, §9.4.3#b6, §9.2#b28, §2#b1, §2#b2, §2#b3, §2#b4, §2.1#b10, §7.1#p2, §2.2#p1, §1.2#r118, §1.2#r119, §1.2#r120, §1.2#r121, §1.2#r122, §1.2#r123, §1.2#r57, §1.2#r70, §1.2#r73, §1.2#r74, §1.2#r53, §9.4.2#r17, §9.4.2#r27, §2.1#r2, §2.1#r3, §2.1#r5, §2.1#r6, §2.1#r7, §2.1#r8, §2.1#r9, §2.1#r10, §2.1#r11, §2.1#r4, §2.1#b3, EB-AKS-3@report-missing, EB-AKS-3@confirm, EB-AKS-3@reject, EB-AKS-3@mark-as-found, EB-AKS-3@add-update, EB-AKS-3@cancel-report, EB-AKS-3@report-disposal, EB-AKS-3@cancel-disposal-report, EB-AKS-6, EB-AKS-2, §11#r17, §1.2#r71, §2.1#b5, §2.1#b6, §4.8#r12]
smoke: []
dependsOn: []
trace:
  §9.3#b1: [3, 38, 115, 116, 119, 140, 142, 152, 154, 160]
  §9.3#b2: [47, 49, 51, 53, 55, 57, 59]
  §9.2#b23: [47, 49, 61]
  §9.4.2#r20: [47, 51, 59]
  §9.4.4#r9: [47, 49]
  §9.4.4#r14: [79, 131]
  §9.11#r1: [29, 31, 32, 40, 42, 43, 45, 61]
  §9.11#r2: [63, 73, 75, 76]
  §9.11#b1: [63, 65, 67, 69, 71, 73]
  §6#r1: [79, 82]
  §6#r6: [121, 122]
  §2.1#r12: [29, 31, 32, 34, 40, 42, 43]
  §2.1#p10: [12, 38, 49, 162, 164, 166]
  §2.1#b6: [25, 27]
  §4.8#r12: 21
  §2.1#p20: 82
  §9.4.1#r4: [3, 29, 42, 43, 45, 79]
  §9.4.3#b6: [79, 82, 98]
  §9.2#b28: [79, 82, 84]
  §2#b1: [3, 137, 138]
  §2#b2: [3, 107, 109, 111, 156]
  §2#b3: [88, 113]
  §2#b4: 23
  §2.1#b10: [34, 36, 38]
  §7.1#p2: [47, 51, 55]
  §2.2#p1: 29
  §1.2#r118: [79, 86]
  §1.2#r119: 82
  §1.2#r120: [95, 98]
  §1.2#r121: [95, 98, 169]
  §1.2#r122: 90
  §1.2#r123: [93, 146]
  §1.2#r57: [93, 160]
  §1.2#r70: [103, 105]
  §1.2#r73: [93, 150]
  §1.2#r74: 101
  §1.2#r53: 88
  §9.4.2#r17: [79, 84, 86]
  §9.4.2#r27: 82
  §2.1#r2: [3, 107, 111, 156]
  §2.1#r3: [88, 113]
  §2.1#r5: 5
  §2.1#r6: [8, 152]
  §2.1#r7: 10
  §2.1#r8: [14, 93, 158, 160]
  §2.1#r9: [12, 23, 25, 162, 164]
  §2.1#r10: [19, 27]
  §2.1#r11: 21
  §2.1#r4: 115
  §2.1#b3: [115, 116, 117]
  EB-AKS-3@report-missing: [3, 109]
  EB-AKS-3@confirm: 8
  EB-AKS-3@reject: 8
  EB-AKS-3@mark-as-found: [10, 166]
  EB-AKS-3@add-update: [5, 125]
  EB-AKS-3@cancel-report: 14
  EB-AKS-3@report-disposal: 12
  EB-AKS-3@cancel-disposal-report: 19
  EB-AKS-6: 125
  EB-AKS-2: [45, 51]
  §11#r17: 75
  §1.2#r71: [111, 156]
  §2.1#b5: [158, 160]
---

# Server: cakupan Group, capability per aksi, Last holder, kepemilikan pemegang, Missing Log di luar cakupan, dan filter atau sort kolom finansial ditolak

## Prerequisites
- Aktor: `Hendra Pratama {runId}` (DU-072-1), `Maya Anggraini {runId}` (DU-072-2), `Dewi Anindita {runId}` (DU-072-3), `Eko Wibowo {runId}` (DU-072-4), `Fajar Nugroho {runId}` (DU-072-5), `Gita Lestari {runId}` (DU-072-6), `Hari Susanto {runId}` (DU-072-7), `Joko Susilo {runId}` (DU-072-8), `Indra Kusuma {runId}` (DU-072-9), `Andi Prasetyo {runId}` (DU-072-10), `Kartika Sari {runId}` (DU-072-11), `Wulan Sari {runId}` (DU-072-12), `Yoga Pratama {runId}` (DU-072-13), `Nanda Putri {runId}` (DU-072-14), `Rudi Hartono {runId}` (DU-072-15), `Taufik Ramadhan {runId}` (DU-072-16), `Lina Marlina {runId}` (DU-072-18), `Sinta Maharani {runId}` (DU-072-19), `Citra Dewi {runId}` (DU-072-48), dan `Bagus Setiawan {runId}` (DU-072-49), dengan peran dan cakupan seperti di Data; `Budi Santoso {runId}` (DU-072-17) hanya pemegang tanpa akun yang diwakili PIC.
- Data:
  - DU-072-1: User Name `Hendra Pratama {runId}`, Peran `Total Control`, Cakupan `seluruh client`.
  - DU-072-2: User Name `Maya Anggraini {runId}`, Peran `Group Manager`, Cakupan `Group Head Office beserta sub-group`.
  - DU-072-3: User Name `Dewi Anindita {runId}`, Peran `Manage asset & TAG dengan Update pada Head Office dan Read pada Warehouse`, Cakupan `Head Office beserta descendant untuk Update, Warehouse untuk Read`.
  - DU-072-4: User Name `Eko Wibowo {runId}`, Peran `Accounting dengan Manage accounting Read dan Update`, Cakupan `seluruh client`.
  - DU-072-5: User Name `Fajar Nugroho {runId}`, Peran `Read Only`, Cakupan `seluruh client`.
  - DU-072-6: User Name `Gita Lestari {runId}`, Peran `Manage asset & TAG dengan Read`, Cakupan `Head Office beserta descendant`.
  - DU-072-7: User Name `Hari Susanto {runId}`, Peran `View asset value`, Cakupan `Group Head Office beserta descendant`.
  - DU-072-8: User Name `Joko Susilo {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Cakupan `aset yang ia pegang`.
  - DU-072-9: User Name `Indra Kusuma {runId}`, Peran `tanpa capability apa pun di modul Missing`, Cakupan `tanpa cakupan`.
  - DU-072-10: User Name `Andi Prasetyo {runId}`, Peran `Group Manager`, Cakupan `Group Head Office beserta sub-group`.
  - DU-072-11: User Name `Kartika Sari {runId}`, Peran `Manage asset & TAG dengan Create dan Delete tanpa Update`, Cakupan `Head Office beserta descendant`.
  - DU-072-12: User Name `Wulan Sari {runId}`, Peran `Aktor transaksi tanpa Manage asset & TAG dengan Update`, Cakupan `aset dalam transaksinya sendiri`.
  - DU-072-13: User Name `Yoga Pratama {runId}`, Peran `Staff Auditor pemilik sesi Audit tanpa Manage asset & TAG dengan Update`, Cakupan `aset dalam sesinya sendiri`.
  - DU-072-14: User Name `Nanda Putri {runId}`, Peran `Manage asset & TAG dengan Update`, Cakupan `Head Office beserta descendant`.
  - DU-072-15: User Name `Rudi Hartono {runId}`, Peran `PIC tanpa hak Aktor Missing`, Cakupan `aset karyawan tanpa akun yang ia wakili`.
  - DU-072-16: User Name `Taufik Ramadhan {runId}`, Peran `PIC pengganti tanpa hak Aktor Missing`, Cakupan `aset karyawan tanpa akun yang ia wakili`.
  - DU-072-17: User Name `Budi Santoso {runId}`, Peran `karyawan tanpa akun`, Cakupan `tanpa akses`.
  - DU-072-18: User Name `Lina Marlina {runId}`, Peran `pemegang tanpa hak Aktor Missing yang dinonaktifkan`, Cakupan `aset yang ia pegang`.
  - DU-072-19: User Name `Sinta Maharani {runId}`, Peran `Group Manager yang juga PIC`, Cakupan `Group Head Office beserta sub-group dan aset karyawan tanpa akun yang ia wakili`.
  - DU-072-20: Sesi Sesi `tanpa token`.
  - DU-072-21: Asset Name `Laptop Dell Latitude 5420 {runId}`, Asset ID `FA072-001`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Hendra Pratama {runId}`, Purchase Cost `12500000`, Asset Value (Commercial) `9800000`, Asset Value (Fiscal) `9100000`.
  - DU-072-22: Asset Name `Drill Bosch GSB {runId}`, Asset ID `FA072-002`, Group aset `Finance Room`, Record berjalan `tidak ada`.
  - DU-072-23: Asset Name `Printer HP LaserJet M404 {runId}`, Asset ID `FA072-003`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`.
  - DU-072-24: Asset Name `Hand Pallet Truck {runId}`, Asset ID `FA072-004`, Group aset `Warehouse`, Record berjalan `Missing, dilaporkan Hendra Pratama {runId}`, TAG `QR-072-0001`.
  - DU-072-25: Asset Name `Projector Epson EB-X06 {runId}`, Asset ID `FA072-005`, Group aset `Server Room`, Record berjalan `Missing, dilaporkan Hendra Pratama {runId}`.
  - DU-072-26: Asset Name `Toyota Innova {runId}`, Asset ID `FA072-006`, Group aset `Finance Room`, Record berjalan `Reported Disposal, dilaporkan Hendra Pratama {runId}`.
  - DU-072-27: Asset Name `Mesin Fotokopi Ricoh {runId}`, Asset ID `FA072-007`, Group aset `Warehouse`, Record berjalan `Reported Disposal, dilaporkan Hendra Pratama {runId}`.
  - DU-072-28: Asset Name `Monitor LG 27UL500 {runId}`, Asset ID `FA072-008`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Hendra Pratama {runId}`.
  - DU-072-29: Asset Name `Camera Canon EOS {runId}`, Asset ID `FA072-009`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Andi Prasetyo {runId} sebelum ia memperoleh hak Aktor Missing`, Pemegang `Andi Prasetyo {runId}`.
  - DU-072-30: Asset Name `Genset Honda EU22 {runId}`, Asset ID `FA072-010`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Andi Prasetyo {runId}`, Pemegang `Andi Prasetyo {runId}`.
  - DU-072-31: Asset Name `Tablet Samsung Tab A8 {runId}`, Asset ID `FA072-011`, Group aset `Finance Room`, Record berjalan `tidak ada`, Transaksi `milik Wulan Sari {runId}`.
  - DU-072-32: Asset Name `Kamera Sony A7 {runId}`, Asset ID `FA072-012`, Group aset `Finance Room`, Record berjalan `tidak ada`.
  - DU-072-33: Asset Name `Scanner Zebra DS2208 {runId}`, Asset ID `FA072-013`, Group aset `Finance Room`, Record berjalan `tidak ada`, Sesi Audit `milik Yoga Pratama {runId}`.
  - DU-072-34: Asset Name `Kursi Ergonomis {runId}`, Asset ID `FA072-014`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Hendra Pratama {runId}`.
  - DU-072-35: Asset Name `Laptop Lenovo ThinkPad T14 {runId}`, Asset ID `FA072-015`, Group aset `Finance Room`, Record berjalan `tidak ada`, Pemegang `Budi Santoso {runId}`, PIC `Rudi Hartono {runId}`.
  - DU-072-36: Asset Name `Brankas Besi {runId}`, Asset ID `FA072-016`, Group aset `Finance Room`, Record berjalan `tidak ada`, Pemegang `Budi Santoso {runId}`, PIC `Sinta Maharani {runId}`.
  - DU-072-37: Asset Name `Papan Tulis {runId}`, Asset ID `FA072-017`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Lina Marlina {runId}`, Pemegang `Lina Marlina {runId}`.
  - DU-072-38: Record entitas lain Name `Meja Kerja Kayu {runId}`, Client `client lain`, Record berjalan `Missing`.
  - DU-072-39: Record terhapus Name `Rak Besi Gudang {runId}`, Asset ID `FA072-019`, Record `ikut terhapus bersama aset`.
  - DU-072-40: Record ID record `00000000-0000-0000-0000-000000000000`.
  - DU-072-45: Asset Name `Lemari Arsip Besi {runId}`, Asset ID `FA072-018`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Andi Prasetyo {runId} sebelum ia memperoleh hak Aktor Missing`, Pemegang `Andi Prasetyo {runId}`.
  - DU-072-46: Asset Name `Mesin Cuci Industri {runId}`, Asset ID `FA072-020`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Rudi Hartono {runId} atas nama Budi Santoso {runId}`, Pemegang `Budi Santoso {runId}`, PIC `Rudi Hartono {runId}`.
  - DU-072-47: Asset Name `Rak Display {runId}`, Asset ID `FA072-021`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Citra Dewi {runId} atas nama Budi Santoso {runId}`, Pemegang `Budi Santoso {runId}`, PIC `Citra Dewi {runId}`.
  - DU-072-48: User Name `Citra Dewi {runId}`, Peran `PIC tanpa hak Aktor Missing`, Cakupan `aset karyawan tanpa akun yang ia wakili`.
  - DU-072-49: User Name `Bagus Setiawan {runId}`, Peran `pengguna terautentikasi tanpa hubungan dengan client suite`, Cakupan `client lain`.
  - DU-072-51: Asset Name `Vacuum Cleaner Industri {runId}`, Asset ID `FA072-023`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Sinta Maharani {runId} atas nama Budi Santoso {runId}`, Pemegang `Budi Santoso {runId}`, PIC `Sinta Maharani {runId}`.
  - DU-072-50: Asset Name `Meja Rapat Kayu {runId}`, Asset ID `FA072-022`, Group aset `Finance Room`, Record berjalan `tidak ada`, Sesi Audit `milik Yoga Pratama {runId}`.

## Test Steps
### Aksi tulis ditolak bagi aktor tanpa capability walau UI dilewati
1. `Eko Wibowo {runId}`, `Fajar Nugroho {runId}`, `Gita Lestari {runId}`, `Hari Susanto {runId}`, `Kartika Sari {runId}`, dan `Indra Kusuma {runId}` masing-masing mengirim Report Missing atas `Drill Bosch GSB {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
2. Permintaan Report Missing atas aset yang sama dikirim tanpa token login
3. Verifikasi semua permintaan itu ditolak server karena aktornya tidak punya hak Pelapor admin, dan `Drill Bosch GSB {runId}` tidak mendapat record maupun perubahan status global
4. `Eko Wibowo {runId}`, `Fajar Nugroho {runId}`, `Gita Lestari {runId}`, `Hari Susanto {runId}`, dan `Joko Susilo {runId}` masing-masing mengirim Add Update atas record `Laptop Dell Latitude 5420 {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
5. Verifikasi semua permintaan itu ditolak dan record `Laptop Dell Latitude 5420 {runId}` tidak mendapat node `Update added by` baru
6. `Eko Wibowo {runId}`, `Fajar Nugroho {runId}`, `Gita Lestari {runId}`, `Hari Susanto {runId}`, dan `Joko Susilo {runId}` masing-masing mengirim Confirm atas record `Printer HP LaserJet M404 {runId}`
7. `Eko Wibowo {runId}`, `Fajar Nugroho {runId}`, `Gita Lestari {runId}`, `Hari Susanto {runId}`, dan `Joko Susilo {runId}` masing-masing mengirim Reject atas record `Printer HP LaserJet M404 {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
8. Verifikasi semua permintaan itu ditolak dan record `Printer HP LaserJet M404 {runId}` tetap `Waiting for Confirmation` dengan status global aset tetap Missing
9. `Eko Wibowo {runId}`, `Fajar Nugroho {runId}`, `Gita Lestari {runId}`, `Hari Susanto {runId}`, dan `Joko Susilo {runId}` masing-masing mengirim Mark as Found atas record `Laptop Dell Latitude 5420 {runId}`
10. Verifikasi semua permintaan itu ditolak dan record `Laptop Dell Latitude 5420 {runId}` tetap `Missing`
11. `Fajar Nugroho {runId}`, `Gita Lestari {runId}`, `Hari Susanto {runId}`, dan `Joko Susilo {runId}` masing-masing mengirim Report Disposal atas record `Laptop Dell Latitude 5420 {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
12. Verifikasi semua permintaan itu ditolak dan record `Laptop Dell Latitude 5420 {runId}` tetap `Missing` tanpa Disposal Report
13. `Hendra Pratama {runId}` dan `Dewi Anindita {runId}` masing-masing mengirim Cancel Report atas record `Printer HP LaserJet M404 {runId}` yang dilaporkan `Joko Susilo {runId}`
14. Verifikasi kedua permintaan itu ditolak karena bukan pelapor, dan record `Printer HP LaserJet M404 {runId}` tetap `Waiting for Confirmation`
15. `Fajar Nugroho {runId}`, `Gita Lestari {runId}`, `Hari Susanto {runId}`, dan `Joko Susilo {runId}` masing-masing mengirim Cancel Disposal Report atas record `Toyota Innova {runId}`
16. `Eko Wibowo {runId}` mengirim Cancel Disposal Report atas record `Toyota Innova {runId}` yang dilaporkan `Hendra Pratama {runId}`
17. `Dewi Anindita {runId}` mengirim Cancel Disposal Report atas record `Toyota Innova {runId}` yang dilaporkan `Hendra Pratama {runId}`
18. `Maya Anggraini {runId}` mengirim Cancel Disposal Report atas record `Mesin Fotokopi Ricoh {runId}` yang berada di Group `Warehouse`
19. Verifikasi semua permintaan itu ditolak, laporan milik orang lain tidak bisa dibatalkan Accounting maupun Manage asset & TAG, dan record `Toyota Innova {runId}` serta `Mesin Fotokopi Ricoh {runId}` tetap `Reported Disposal`
20. `Joko Susilo {runId}` meminta Download daftar record
21. Verifikasi permintaan itu ditolak dan tidak ada berkas yang dihasilkan

### Accounting melapor disposal aset Missing dan membatalkan laporannya sendiri
22. `Eko Wibowo {runId}` mengirim Report Disposal atas record `Monitor LG 27UL500 {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
23. Verifikasi record `Monitor LG 27UL500 {runId}` berstatus `Reported Disposal`
24. `Eko Wibowo {runId}` mengirim Report Disposal atas record `Printer HP LaserJet M404 {runId}` yang berstatus `Waiting for Confirmation` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
25. Verifikasi permintaan itu ditolak karena Report Disposal hanya melaporkan aset Missing, dan record `Printer HP LaserJet M404 {runId}` tetap `Waiting for Confirmation`
26. `Eko Wibowo {runId}` mengirim Cancel Disposal Report atas record `Monitor LG 27UL500 {runId}`
27. Verifikasi record `Monitor LG 27UL500 {runId}` kembali berstatus `Missing` karena laporan itu milik `Eko Wibowo {runId}`

### Daftar record mengikuti cakupan Group tiap peran
28. `Hendra Pratama {runId}` mengambil daftar sub-tab Active dengan Search `{runId}`
29. Verifikasi daftar itu memuat record `Laptop Dell Latitude 5420 {runId}`, `Projector Epson EB-X06 {runId}`, dan `Hand Pallet Truck {runId}` karena cakupan Total Control adalah seluruh client
30. `Maya Anggraini {runId}` mengambil daftar sub-tab Active dengan Search `{runId}`
31. Verifikasi daftar itu memuat record `Laptop Dell Latitude 5420 {runId}` di Group `Finance Room` dan `Projector Epson EB-X06 {runId}` di sub-group `Server Room`
32. Verifikasi daftar itu tidak memuat record `Hand Pallet Truck {runId}` di Group `Warehouse` karena di luar Group binaan
33. `Dewi Anindita {runId}` mengambil daftar sub-tab Active dengan Search `{runId}`
34. Verifikasi daftar itu memuat record `Laptop Dell Latitude 5420 {runId}` di Group `Finance Room` dan `Hand Pallet Truck {runId}` di Group `Warehouse` dalam satu tabel
35. `Dewi Anindita {runId}` mengirim Add Update atas record `Laptop Dell Latitude 5420 {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
36. Verifikasi permintaan itu diterima karena Update berlaku di Group `Finance Room` sebagai descendant Head Office
37. `Dewi Anindita {runId}` mengirim Add Update atas record `Hand Pallet Truck {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
38. Verifikasi permintaan itu ditolak karena di Group `Warehouse` `Dewi Anindita {runId}` hanya punya Read, dan record `Hand Pallet Truck {runId}` tidak mendapat node `Update added by` baru
39. `Eko Wibowo {runId}` dan `Fajar Nugroho {runId}` masing-masing mengambil daftar sub-tab Active dengan Search `{runId}`
40. Verifikasi kedua daftar itu memuat record `Laptop Dell Latitude 5420 {runId}`, `Projector Epson EB-X06 {runId}`, dan `Hand Pallet Truck {runId}` karena cakupan keduanya seluruh client
41. `Gita Lestari {runId}` dan `Hari Susanto {runId}` masing-masing mengambil daftar sub-tab Active dengan Search `{runId}`
42. Verifikasi kedua daftar itu memuat record `Laptop Dell Latitude 5420 {runId}` dan `Projector Epson EB-X06 {runId}` di Head Office beserta descendant
43. Verifikasi kedua daftar itu tidak memuat record `Hand Pallet Truck {runId}` di Group `Warehouse`
44. `Indra Kusuma {runId}` mengambil daftar sub-tab Active dengan Search `{runId}`
45. Verifikasi permintaan itu ditolak dan tidak ada record yang dikembalikan

### Missing Log di luar cakupan ditolak server
46. `Gita Lestari {runId}` membuka Missing Log record `Hand Pallet Truck {runId}` lewat tautan langsung
47. Verifikasi permintaan itu ditolak dan tidak ada isi Missing Log `Hand Pallet Truck {runId}` yang dikembalikan, karena `Gita Lestari {runId}` tidak punya cakupan Group `Warehouse`
48. `Maya Anggraini {runId}` membuka Missing Log record `Hand Pallet Truck {runId}` lewat tautan langsung
49. Verifikasi permintaan itu ditolak dan tidak ada isi Missing Log `Hand Pallet Truck {runId}` yang dikembalikan, karena Group `Warehouse` di luar Group binaan
50. `Indra Kusuma {runId}` membuka Missing Log record `Laptop Dell Latitude 5420 {runId}` lewat tautan langsung
51. Verifikasi permintaan itu ditolak karena aktornya tidak punya hak lihat, dan tidak ada isi Missing Log `Laptop Dell Latitude 5420 {runId}` yang dikembalikan
52. Permintaan membuka Missing Log record `Laptop Dell Latitude 5420 {runId}` dikirim tanpa token login
53. Verifikasi permintaan itu ditolak dan tidak ada isi Missing Log yang dikembalikan
54. `Hendra Pratama {runId}` membuka Missing Log dengan ID record `00000000-0000-0000-0000-000000000000`
55. Verifikasi permintaan itu ditolak karena record tidak ada, tanpa isi apa pun
56. `Hendra Pratama {runId}` membuka Missing Log record milik aset `Rak Besi Gudang {runId}` yang sudah dihapus
57. Verifikasi permintaan itu ditolak karena record sudah terhapus bersama asetnya
58. `Hendra Pratama {runId}` membuka Missing Log record milik client lain atas `Meja Kerja Kayu {runId}`
59. Verifikasi permintaan itu ditolak dan tidak ada isi record client lain yang dikembalikan
60. `Hari Susanto {runId}` membuka Missing Log record `Laptop Dell Latitude 5420 {runId}`
61. Verifikasi permintaan itu diterima secara read-only karena `Laptop Dell Latitude 5420 {runId}` berada di Group `Finance Room` dalam Group yang di-assign

### Kolom finansial tidak tersedia bagi peran tanpa hak lihat nilai finansial
62. `Maya Anggraini {runId}` mengambil daftar sub-tab Active dengan Search `{runId}`
63. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tidak memuat Purchase Cost, Asset Value (Commercial), maupun Asset Value (Fiscal)
64. `Maya Anggraini {runId}` meminta daftar yang difilter pada Purchase Cost dengan Min `10000000` dan Max `15000000`
65. Verifikasi permintaan itu ditolak server
66. `Maya Anggraini {runId}` meminta daftar yang diurutkan menurut Asset Value (Commercial)
67. Verifikasi permintaan itu ditolak server
68. `Maya Anggraini {runId}` mengambil daftar sub-tab Active dengan Search `12500000`
69. Verifikasi hasil pencarian itu tidak memuat record `Laptop Dell Latitude 5420 {runId}`, karena Search tidak mencocokkan nilai Purchase Cost
70. `Maya Anggraini {runId}` meminta Download daftar sub-tab Active
71. Verifikasi berkas yang dihasilkan tidak memuat kolom Purchase Cost, Asset Value (Commercial), maupun Asset Value (Fiscal)
72. `Fajar Nugroho {runId}` dan `Gita Lestari {runId}` masing-masing mengambil daftar sub-tab Active dengan Search `{runId}`
73. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` pada kedua daftar itu tidak memuat nilai finansial, karena keduanya tidak memegang View asset value
74. `Eko Wibowo {runId}` dan `Hari Susanto {runId}` masing-masing mengambil daftar sub-tab Active dengan Search `{runId}`
75. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` pada kedua daftar itu memuat Purchase Cost `12500000`, Asset Value (Commercial) `9800000`, dan Asset Value (Fiscal) `9100000`
76. Verifikasi daftar `Hari Susanto {runId}` tidak memuat record `Hand Pallet Truck {runId}`, karena Group `Warehouse` di luar Group yang di-assign

### Last holder tidak dapat memutuskan record dari pinjaman atau penugasannya sendiri
77. `Andi Prasetyo {runId}` mengirim Confirm atas record `Camera Canon EOS {runId}` yang ia pegang
78. `Andi Prasetyo {runId}` mengirim Reject atas record `Camera Canon EOS {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
79. Verifikasi kedua permintaan itu ditolak dengan pesan `You were holding this asset. Ask another admin.` dan record `Camera Canon EOS {runId}` tetap `Waiting for Confirmation`
80. `Andi Prasetyo {runId}` mengirim Mark as Found atas record `Genset Honda EU22 {runId}` yang ia laporkan sendiri sebagai Pelapor admin
81. `Andi Prasetyo {runId}` mengirim Report Disposal atas record `Genset Honda EU22 {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
82. Verifikasi kedua permintaan itu ditolak dengan pesan `You were holding this asset. Ask another admin.`, record `Genset Honda EU22 {runId}` tetap `Missing`, dan tidak ada Disposal Report
83. `Andi Prasetyo {runId}` mengirim Mark as Found atas record `Camera Canon EOS {runId}`
84. Verifikasi permintaan itu ditolak dengan pesan `You were holding this asset. Ask another admin.` dan record `Camera Canon EOS {runId}` tetap `Waiting for Confirmation`
85. `Hendra Pratama {runId}` mengirim Confirm atas record `Camera Canon EOS {runId}`
86. Verifikasi permintaan itu diterima karena `Hendra Pratama {runId}` bukan Last holder, dan record `Camera Canon EOS {runId}` berstatus `Missing`

### Pemegang tanpa akun: PIC menjadi Last holder dan dapat membatalkan laporan
87. `Rudi Hartono {runId}` mengirim Report Missing atas `Laptop Lenovo ThinkPad T14 {runId}` atas nama `Budi Santoso {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
88. Verifikasi record `Laptop Lenovo ThinkPad T14 {runId}` berstatus `Waiting for Confirmation` dan mencatat `Rudi Hartono {runId}` sebagai PIC yang melapor atas nama `Budi Santoso {runId}`
89. `Dewi Anindita {runId}` mengirim Cancel Report atas record `Laptop Lenovo ThinkPad T14 {runId}`
90. Verifikasi permintaan itu ditolak karena bukan pelapor atau PIC yang tercatat, dan record `Laptop Lenovo ThinkPad T14 {runId}` tetap `Waiting for Confirmation`
91. PIC aset `Laptop Lenovo ThinkPad T14 {runId}` diganti dari `Rudi Hartono {runId}` menjadi `Taufik Ramadhan {runId}`
92. `Taufik Ramadhan {runId}` mengirim Cancel Report atas record `Laptop Lenovo ThinkPad T14 {runId}`
93. Verifikasi permintaan itu diterima dan record `Laptop Lenovo ThinkPad T14 {runId}` berstatus `Canceled`
94. `Sinta Maharani {runId}` mengirim Report Missing atas `Brankas Besi {runId}` atas nama `Budi Santoso {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
95. Verifikasi record `Brankas Besi {runId}` langsung berstatus `Missing` dan mencatat `Sinta Maharani {runId}` sebagai Last holder
96. `Sinta Maharani {runId}` mengirim Mark as Found atas record `Brankas Besi {runId}`
97. `Sinta Maharani {runId}` mengirim Report Disposal atas record `Brankas Besi {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
98. Verifikasi kedua permintaan itu ditolak dengan pesan `You were holding this asset. Ask another admin.`, termasuk karena `Sinta Maharani {runId}` yang melapor atas nama `Budi Santoso {runId}`, dan record `Brankas Besi {runId}` tetap `Missing`
99. PIC aset `Brankas Besi {runId}` diganti dari `Sinta Maharani {runId}` menjadi `Taufik Ramadhan {runId}`
100. `Sinta Maharani {runId}` mengirim Mark as Found atas record `Brankas Besi {runId}`
101. Verifikasi permintaan itu tetap ditolak dengan pesan `You were holding this asset. Ask another admin.`, karena pemisahan tugas mengikuti PIC yang tercatat saat dilaporkan

### Pelapor yang dinonaktifkan tidak dapat membatalkan laporan
102. `Lina Marlina {runId}` mengirim Cancel Report atas record `Papan Tulis {runId}`
103. Verifikasi permintaan itu ditolak karena pelapor sudah dinonaktifkan, dan record `Papan Tulis {runId}` tetap `Waiting for Confirmation`
104. `Hendra Pratama {runId}` mengirim Confirm atas record `Papan Tulis {runId}`
105. Verifikasi record `Papan Tulis {runId}` berstatus `Missing` karena diputuskan Aktor Missing

### Aktor transaksi melapor dari cakupannya sendiri, dan pelapor dari Task Detail Audit menunggu konfirmasi
106. `Wulan Sari {runId}` mengirim Report Missing atas `Tablet Samsung Tab A8 {runId}` dari transaksinya sendiri dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
107. Verifikasi record `Tablet Samsung Tab A8 {runId}` langsung berstatus `Missing` walau `Wulan Sari {runId}` tidak punya Manage asset & TAG dengan Update
108. `Wulan Sari {runId}` mengirim Report Missing atas `Kamera Sony A7 {runId}` yang berada di luar transaksinya dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
109. Verifikasi permintaan itu ditolak dan `Kamera Sony A7 {runId}` tidak mendapat record
110. `Yoga Pratama {runId}` mengirim Report Missing atas `Scanner Zebra DS2208 {runId}` dari Task Detail sesinya sendiri dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
111. Verifikasi record `Scanner Zebra DS2208 {runId}` berstatus `Waiting for Confirmation` dengan Source `Audit` dan status global aset langsung Missing, karena `Yoga Pratama {runId}` tidak punya hak Aktor Missing
112. `Joko Susilo {runId}` mengirim Report Missing atas `Kamera Sony A7 {runId}` yang tidak ia pegang dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
113. Verifikasi permintaan itu ditolak karena pemegang hanya boleh melaporkan aset yang ia pegang, dan `Kamera Sony A7 {runId}` tidak mendapat record

### I found it tidak dibatasi cakupan Group dan tidak membuka data finansial
114. `Gita Lestari {runId}` mengirim I found it atas record `Hand Pallet Truck {runId}` yang berada di luar cakupannya
115. Verifikasi permintaan itu diterima walau `Hand Pallet Truck {runId}` berada di Group `Warehouse` di luar cakupan `Gita Lestari {runId}`
116. Verifikasi respons hanya memuat badge status record, Asset Name, dan Group, tanpa Purchase Cost, Asset Value (Commercial), maupun Asset Value (Fiscal)
117. Verifikasi status record `Hand Pallet Truck {runId}` tetap `Missing` dan status global aset tidak berubah
118. `Gita Lestari {runId}` mengirim I found it atas aset `Drill Bosch GSB {runId}` yang tidak punya record Missing berjalan
119. Verifikasi permintaan itu ditolak karena aset tidak punya record Missing berjalan

### Scan Found Asset di luar cakupan tidak mengungkap data aset
120. `Dewi Anindita {runId}` menjalankan Scan Found Asset dengan TAG `QR-072-0001`
121. Verifikasi permintaan itu ditolak dengan pesan `You don't have access to this asset.` tanpa nama aset dan tanpa data aset
122. Verifikasi scan itu tidak tercatat sebagai deteksi pada record `Hand Pallet Truck {runId}`

### Capability yang dicabut menolak aksi berikutnya
123. Hak Update pada Manage asset & TAG milik `Nanda Putri {runId}` dicabut
124. `Nanda Putri {runId}` mengirim Add Update atas record `Kursi Ergonomis {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
125. Verifikasi permintaan itu ditolak dan record `Kursi Ergonomis {runId}` tidak mendapat node `Update added by` baru

### Penolakan Last holder tidak menghasilkan event, notifikasi, maupun entri log
126. Catat jumlah event `missing_*`, notifikasi, dan entri log atas record `Lemari Arsip Besi {runId}` dan `Genset Honda EU22 {runId}` sebelum penolakan
127. `Andi Prasetyo {runId}` mengirim Confirm atas record `Lemari Arsip Besi {runId}`
128. `Andi Prasetyo {runId}` mengirim Reject atas record `Lemari Arsip Besi {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
129. `Andi Prasetyo {runId}` mengirim Mark as Found atas record `Genset Honda EU22 {runId}`
130. `Andi Prasetyo {runId}` mengirim Report Disposal atas record `Genset Honda EU22 {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
131. Verifikasi keempat permintaan itu ditolak tanpa event `missing_*`, tanpa notifikasi, dan tanpa entri log baru dibanding jumlah yang dicatat sebelumnya

### Create dan Delete tanpa Update tidak cukup untuk aksi tulis
132. `Kartika Sari {runId}` mengirim Add Update atas record `Laptop Dell Latitude 5420 {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
133. `Kartika Sari {runId}` mengirim Confirm atas record `Printer HP LaserJet M404 {runId}`
134. `Kartika Sari {runId}` mengirim Reject atas record `Printer HP LaserJet M404 {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
135. `Kartika Sari {runId}` mengirim Mark as Found atas record `Laptop Dell Latitude 5420 {runId}`
136. `Kartika Sari {runId}` mengirim Report Disposal atas record `Laptop Dell Latitude 5420 {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
137. Verifikasi kelima permintaan itu ditolak karena Create dan Delete pada Manage asset & TAG tidak berlaku dan seluruh aksi tulis memakai Update
138. Verifikasi record `Laptop Dell Latitude 5420 {runId}` tetap `Missing` tanpa Disposal Report dan tanpa node `Update added by` baru, serta record `Printer HP LaserJet M404 {runId}` tetap `Waiting for Confirmation`

### I found it ditolak tanpa token login dan dari client lain
139. Permintaan I found it atas record `Hand Pallet Truck {runId}` dikirim tanpa token login
140. Verifikasi permintaan itu ditolak dan tidak ada data record yang dikembalikan
141. `Bagus Setiawan {runId}` dari client lain mengirim I found it atas record `Hand Pallet Truck {runId}`
142. Verifikasi permintaan itu ditolak dan tidak ada data record yang dikembalikan

### PIC yang dinonaktifkan atau dihapus digantikan PIC pengganti untuk membatalkan laporan
143. `Rudi Hartono {runId}` dinonaktifkan
144. PIC aset `Mesin Cuci Industri {runId}` diganti dari `Rudi Hartono {runId}` menjadi `Taufik Ramadhan {runId}`
145. `Taufik Ramadhan {runId}` mengirim Cancel Report atas record `Mesin Cuci Industri {runId}`
146. Verifikasi permintaan itu diterima dan record `Mesin Cuci Industri {runId}` berstatus `Canceled`
147. `Citra Dewi {runId}` dihapus
148. PIC aset `Rak Display {runId}` diganti dari `Citra Dewi {runId}` menjadi `Taufik Ramadhan {runId}`
149. `Taufik Ramadhan {runId}` mengirim Cancel Report atas record `Rak Display {runId}`
150. Verifikasi permintaan itu diterima dan record `Rak Display {runId}` berstatus `Canceled`

### Pelapor dari Task Detail Audit hanya dapat Report Missing dan Cancel Report miliknya
151. `Yoga Pratama {runId}` mengirim Confirm atas record `Scanner Zebra DS2208 {runId}`
152. Verifikasi permintaan itu ditolak karena `Yoga Pratama {runId}` bukan Aktor Missing, dan record `Scanner Zebra DS2208 {runId}` tetap `Waiting for Confirmation`
153. `Yoga Pratama {runId}` mengirim Add Update atas record `Scanner Zebra DS2208 {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
154. Verifikasi permintaan itu ditolak dan record `Scanner Zebra DS2208 {runId}` tidak mendapat node `Update added by`
155. `Hendra Pratama {runId}` mengirim Report Missing atas `Meja Rapat Kayu {runId}` dari Task Detail sesi milik `Yoga Pratama {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
156. Verifikasi record `Meja Rapat Kayu {runId}` langsung berstatus `Missing` dengan Source `Audit`, tanpa melalui `Waiting for Confirmation`
157. `Hendra Pratama {runId}` mengirim Cancel Report atas record `Meja Rapat Kayu {runId}` yang ia laporkan langsung `Missing`
158. Verifikasi permintaan itu ditolak dan record `Meja Rapat Kayu {runId}` tetap `Missing`
159. `Yoga Pratama {runId}` mengirim Cancel Report atas record `Scanner Zebra DS2208 {runId}` dari Task Detail sesinya sendiri
160. Verifikasi permintaan itu diterima, record `Scanner Zebra DS2208 {runId}` berstatus `Canceled`, dan status global aset dihitung ulang dari state aset terkini

### Manage asset & TAG dengan Update melapor disposal hanya di Group yang ia pegang Update
161. `Dewi Anindita {runId}` mengirim Report Disposal atas record `Projector Epson EB-X06 {runId}` yang berada di Group `Server Room` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
162. Verifikasi permintaan itu diterima dan record `Projector Epson EB-X06 {runId}` berstatus `Reported Disposal`
163. `Dewi Anindita {runId}` mengirim Report Disposal atas record `Hand Pallet Truck {runId}` yang berada di Group `Warehouse` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
164. Verifikasi permintaan itu ditolak karena di Group `Warehouse` `Dewi Anindita {runId}` hanya punya Read, dan record `Hand Pallet Truck {runId}` tetap `Missing` tanpa Disposal Report
165. `Dewi Anindita {runId}` mengirim Mark as Found atas record `Hand Pallet Truck {runId}` yang berada di Group `Warehouse`
166. Verifikasi permintaan itu ditolak karena di Group `Warehouse` `Dewi Anindita {runId}` hanya punya Read, dan record `Hand Pallet Truck {runId}` tetap `Missing`

### PIC ditolak Confirm dan Reject atas laporan pemegang tanpa akun, termasuk yang ia laporkan sendiri
167. `Sinta Maharani {runId}` mengirim Confirm atas record `Vacuum Cleaner Industri {runId}` yang ia laporkan atas nama `Budi Santoso {runId}`
168. `Sinta Maharani {runId}` mengirim Reject atas record `Vacuum Cleaner Industri {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
169. Verifikasi kedua permintaan itu ditolak dengan pesan `You were holding this asset. Ask another admin.` dan record `Vacuum Cleaner Industri {runId}` tetap `Waiting for Confirmation`
