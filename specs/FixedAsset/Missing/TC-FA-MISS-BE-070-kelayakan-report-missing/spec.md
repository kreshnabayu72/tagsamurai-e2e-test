---
id: TC-FA-MISS-BE-070-kelayakan-report-missing
title: "Server: kelayakan Report Missing per aset, satu record berjalan, atomik per aset, dan race dua laporan"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [§1.2#r12, §1.2#r13, §1.2#r14, §1.2#r16, §1.2#r40, §1.2#r46, §1.2#r47, §1.2#r48, §1.2#r49, §1.2#r54, §1.2#r55, §1.2#r64, §1.2#r26, §1.2#r28, §9.2#b1, §9.2#b2, §9.2#b3, §9.2#b5, §9.2#b8, §9.2#b9, §9.2#b10, §9.2#b11, §9.2#b12, §9.2#b14, §9.2#b15, §9.4.2#r2, §9.4.2#r16, §9.4.3#b3, §9.4.1#r6, §9.4.1#r3, §9.6#r1, §6#r14, §4.2.3#b1, §10#r2, §10#r6, §9.4.4#r1, §9.4.4#r2, §9.4.4#r3, EB-CON-3, EB-EDG-1, EB-EDG-3, EB-ERR-4, §1.2#r71, §9.4.2#r37, §9.2#b33]
smoke: []
dependsOn: []
trace:
  §1.2#r12: 3
  §1.2#r13: 2
  §1.2#r14: [19, 20, 33, 35, 36, 37]
  §1.2#r16: [48, 49]
  §1.2#r40: [6, 17]
  §1.2#r46: 17
  §1.2#r47: 32
  §1.2#r48: 14
  §1.2#r49: [15, 16, 93, 95, 97]
  §1.2#r54: [22, 23, 24]
  §1.2#r55: [26, 27]
  §1.2#r64: [10, 11]
  §1.2#r26: 5
  §1.2#r28: 10
  §9.2#b1: [17, 39]
  §9.2#b2: [19, 32, 41, 44, 84, 87]
  §9.2#b3: [33, 38, 39, 41, 44]
  §9.2#b5: 32
  §9.2#b8: 17
  §9.2#b9: [5, 6, 7, 8, 9, 24]
  §9.2#b10: 4
  §9.2#b11: [26, 27, 28]
  §9.2#b12: 54
  §9.2#b14: [13, 29]
  §9.2#b15: 47
  §9.4.2#r2: [47, 50]
  §9.4.2#r16: [53, 54, 55]
  §9.4.3#b3: [19, 34]
  §9.4.1#r6: 47
  §9.4.1#r3: [35, 36, 37]
  §9.6#r1: [17, 19]
  §6#r14: 50
  §4.2.3#b1: [33, 38, 41, 44]
  §10#r2: 19
  §10#r6: [57, 59, 61, 63, 65, 67, 69, 71, 72, 74, 75, 76, 77, 79, 81, 82]
  §9.4.4#r1: [19, 33]
  §9.4.4#r2: [12, 30]
  §9.4.4#r3: [47, 48]
  EB-CON-3: 47
  EB-EDG-1: 38
  EB-EDG-3: [57, 69, 71, 74, 75, 79, 81, 82]
  EB-ERR-4: [20, 34, 38, 42, 45]
  §1.2#r71: [84, 85, 89, 91]
  §9.4.2#r37: [84, 85]
  §9.2#b33: [36, 37, 99, 101]
---

# Server: kelayakan Report Missing per aset, satu record berjalan, atomik per aset, dan race dua laporan

## Prerequisites
- Aktor: Rina W, Total Control dengan cakupan seluruh client; Andi P, Group Manager Head Office dengan Group binaan Head Office beserta sub-group `Finance Room` dan `Server Room`, sedangkan Group `Warehouse` bukan Group binaannya; `Joko Susilo {runId}`, pemegang tanpa hak Aktor Missing (DU-070-17); `Sari Dewi {runId}`, pemegang tanpa hak Aktor Missing (DU-070-18); `Hendra Kusuma {runId}`, Staff Auditor tanpa hak Aktor Missing (DU-070-30).
- Data:
  - DU-070-1: Asset Name `Laptop Dell Latitude 5420 {runId}`, Asset ID `FA070-001`, Group `Finance Room`, Condition `Normal`, Pemegang `Joko Susilo {runId}`, Scan terakhir `Lobby reader pada T0 − 2 hari, pukul 09:00`.
  - DU-070-2: Asset Name `Hand Pallet Truck {runId}`, Asset ID `FA070-002`, Group `Finance Room`, Condition `Normal`, Pemegang `tidak ada`, Scan terakhir `belum pernah terpindai`, Transaksi lain berjalan `Work Order berjalan, jadwal maintenance, dan item sesi pemeriksaan aset berjalan`, Activity Lock `In Audit`.
  - DU-070-3: Asset Name `Projector Epson EB-X06 {runId}`, Asset ID `FA070-003`, Group `Server Room`, Condition `Damaged`, Pemegang `tidak ada`.
  - DU-070-4: Asset Name `Monitor LG 27UL500 {runId}`, Asset ID `FA070-004`, Group `Finance Room`, Condition `Normal`, Pemegang `tidak ada`, Activity Lock `Under Maintenance`.
  - DU-070-5: Asset Name `Laptop Lenovo ThinkPad T14 {runId}`, Asset ID `FA070-005`, Group `Finance Room`, Condition `Normal`, Pemegang `Andi P`.
  - DU-070-6: Asset Name `Scanner Zebra DS2208 {runId}`, Asset ID `FA070-006`, Group `Warehouse`, Condition `Normal`, Pemegang `Joko Susilo {runId}`.
  - DU-070-7: Asset Name `Drill Bosch GSB {runId}`, Asset ID `FA070-007`, Group `Warehouse`, Condition `Normal`, Pemegang `tidak ada`.
  - DU-070-8: Asset Name `Camera Canon EOS {runId}`, Asset ID `FA070-008`, Group `Finance Room`, Condition `Normal`, Record berjalan `Missing`, What happened record `Kamera tidak ada di lemari penyimpanan`, Pelapor record `Rina W`.
  - DU-070-9: Asset Name `Printer HP LaserJet M404 {runId}`, Asset ID `FA070-009`, Group `Finance Room`, Condition `Normal`, Record berjalan `Waiting for Confirmation`.
  - DU-070-10: Asset Name `Toyota Innova {runId}`, Asset ID `FA070-010`, Group `Server Room`, Condition `Normal`, Record berjalan `Reported Disposal`.
  - DU-070-11: Asset Name `Mesin Fotokopi Ricoh {runId}`, Asset ID `FA070-011`, Group `Server Room`, Condition `Normal`, Record berjalan `In Disposal Process`.
  - DU-070-12: Asset Name `Meja Kerja Kayu {runId}`, Asset ID `FA070-012`, Group `Finance Room`, Condition `Normal`, Lifecycle `Disposed`, Record History `Disposed`.
  - DU-070-13: Asset Name `Hand Truck Gudang {runId}`, Asset ID `FA070-013`, Group `Warehouse`, Condition `Normal`, Pemegang `tidak ada`.
  - DU-070-14: Asset Name `Tablet Samsung Tab A8 {runId}`, Asset ID `FA070-014`, Group `Finance Room`, Condition `Normal`, Pemegang `Andi P`.
  - DU-070-15: Asset Name `Kamera Sony A7 {runId}`, Asset ID `FA070-015`, Group `Finance Room`, Condition `Normal`, Pemegang `Sari Dewi {runId}`.
  - DU-070-16: Asset Name `Genset Honda EU22 {runId}`, Asset ID `FA070-016`, Group `Finance Room`, Condition `Normal`, Pemegang `tidak ada`.
  - DU-070-17: User Name `Joko Susilo {runId}`, Peran `pemegang tanpa hak Aktor Missing`.
  - DU-070-18: User Name `Sari Dewi {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Status `Active`.
  - DU-070-19: Asset Name `Kursi Ergonomis {runId}`, Asset ID `FA070-019`, Group `Finance Room`, Condition `Normal`, Lifecycle `Unmanaged`.
  - DU-070-20: Group Name `Ruang Arsip {runId}`.
  - DU-070-21: Asset Name `Brankas Besi {runId}`, Asset ID `FA070-021`, Group `Ruang Arsip {runId}`, Condition `Normal`, Record berjalan `Missing`.
  - DU-070-22: Group Name `Lantai Dua {runId}`.
  - DU-070-23: Asset Name `Papan Tulis {runId}`, Asset ID `FA070-023`, Group `Finance Room`, Condition `Normal`, Record History `Found, Found at Lantai Dua {runId}`.
  - DU-070-26: Category Name `Perabot Arsip {runId}`.
  - DU-070-27: Asset Name `Lemari Arsip Baja {runId}`, Asset ID `FA070-027`, Group `Finance Room`, Category `Perabot Arsip {runId}`, Condition `Normal`, Record berjalan `Missing`.
  - DU-070-28: Category Name `Peralatan Gudang {runId}`.
  - DU-070-29: Asset Name `Rak Besi Gudang {runId}`, Asset ID `FA070-029`, Group `Finance Room`, Category `Perabot Arsip {runId}`, Condition `Normal`, Record History `Found, Category Peralatan Gudang {runId}` yang tersimpan saat record selesai.
  - DU-070-31: Sesi Audit `Audit Ruang Server {runId}` dengan pemilik `Hendra Kusuma {runId}`, memuat aset DU-070-32, DU-070-33, dan DU-070-34.
  - DU-070-32: Asset Name `Rak Server Dell {runId}`, Asset ID `FA070-032`, Group `Server Room`, Condition `Normal`, Pemegang `tidak ada`, termasuk dalam sesi Audit `Audit Ruang Server {runId}`.
  - DU-070-33: Asset Name `Switch Cisco Catalyst {runId}`, Asset ID `FA070-033`, Group `Finance Room`, Condition `Normal`, Pemegang `tidak ada`, termasuk dalam sesi Audit `Audit Ruang Server {runId}`.
  - DU-070-34: Asset Name `UPS APC Smart {runId}`, Asset ID `FA070-034`, Group `Finance Room`, Condition `Normal`, Pemegang `tidak ada`, termasuk dalam sesi Audit `Audit Ruang Server {runId}`.
  - DU-070-35: Asset Name `Proyektor BenQ MW550 {runId}`, Asset ID `FA070-035`, Group `Finance Room`, Condition `Normal`, Pemegang `tidak ada`, tidak termasuk dalam sesi Audit `Audit Ruang Server {runId}`.
  - DU-070-37: Asset Name `Generator Perkins 20kVA {runId}`, Asset ID `FA070-037`, Group `Finance Room`, Condition `Normal`, Pemegang `tidak ada`, Baris Disposal `Waiting for Approval` berjenis `Sell`, tanpa record Missing.
  - DU-070-38: Asset Name `Kompresor Udara Swan {runId}`, Asset ID `FA070-038`, Group `Finance Room`, Condition `Normal`, Pemegang `tidak ada`, tercantum dalam Draft Disposal berjenis `Scrap`, tanpa record Missing.
  - DU-070-36: Asset Name `Kabinet Besi Arsip {runId}`, Asset ID `FA070-036`, Group `Finance Room`, Condition `Normal`, Pemegang `tidak ada`, Record berjalan `Missing`, Activity Lock `In Audit`, Baris sesi pemeriksaan aset `sudah final`.

## Test Steps
### Satu laporan banyak aset menghasilkan satu record per aset
1. Rina W mengirim Report Missing atas `Laptop Dell Latitude 5420 {runId}`, `Hand Pallet Truck {runId}`, `Projector Epson EB-X06 {runId}`, dan `Monitor LG 27UL500 {runId}` dalam satu laporan dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
2. Verifikasi keempat aset masing-masing punya tepat satu record berjalan, sehingga satu laporan menghasilkan empat record
3. Verifikasi setiap record memuat aset yang dilaporkan dan waktu lapor
4. Verifikasi setiap record langsung berstatus `Missing` dan efek Pelapor admin dijalankan tanpa melalui `Waiting for Confirmation`
5. Verifikasi status global keempat aset menjadi Missing
6. Verifikasi record `Laptop Dell Latitude 5420 {runId}` mencatat `Joko Susilo {runId}` sebagai Last holder
7. Verifikasi record `Hand Pallet Truck {runId}` tidak memiliki Last holder
8. Verifikasi Last seen record `Laptop Dell Latitude 5420 {runId}` memuat waktu scan terakhir sebelum laporan dan pemindai `Lobby reader`
9. Verifikasi Last seen record `Hand Pallet Truck {runId}` bernilai `Unknown`
10. Verifikasi record `Projector Epson EB-X06 {runId}` menyimpan Condition sebelum laporan `Damaged`
11. Verifikasi record `Laptop Dell Latitude 5420 {runId}` menyimpan Condition sebelum laporan `Normal`
12. Verifikasi setiap record memuat node `Reported missing by` atas nama Rina W dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
13. Verifikasi setiap record menyimpan Source sesuai titik masuk laporan Pelapor admin, tanpa nomor transaksi
14. Verifikasi Work Order berjalan, jadwal maintenance, dan item sesi pemeriksaan aset milik `Hand Pallet Truck {runId}` tidak berubah, tidak ditutup, dan tidak dijeda
15. Verifikasi Activity Lock `In Audit` milik `Hand Pallet Truck {runId}` tetap ada di atas Condition Missing
16. Verifikasi Activity Lock `Under Maintenance` milik `Monitor LG 27UL500 {runId}` tetap ada di atas Condition Missing
17. Verifikasi untuk setiap aset dalam laporan itu, status global Missing hanya ada bersama tepat satu record berjalan dan sebaliknya, sehingga tidak ada record tanpa efek dan tidak ada efek tanpa record

### Laporan ulang atas aset yang sudah dilaporkan ditolak
18. Rina W mengirim ulang Report Missing atas `Laptop Dell Latitude 5420 {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
19. Verifikasi aset `Laptop Dell Latitude 5420 {runId}` ditolak dengan keterangan `Already reported missing` beserta tautan ke record yang sudah ada
20. Verifikasi aset `Laptop Dell Latitude 5420 {runId}` tetap punya tepat satu record berjalan dan record itu tidak berubah

### Pemegang dengan hak Aktor Missing melapor sebagai Pelapor admin
21. Andi P mengirim Report Missing atas `Laptop Lenovo ThinkPad T14 {runId}` yang ia pegang dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
22. Verifikasi record `Laptop Lenovo ThinkPad T14 {runId}` langsung berstatus `Missing` tanpa menunggu Confirm
23. Verifikasi aset `Laptop Lenovo ThinkPad T14 {runId}` tidak punya record berstatus `Waiting for Confirmation`
24. Verifikasi record `Laptop Lenovo ThinkPad T14 {runId}` mencatat Andi P sebagai Last holder

### Laporan pemegang tanpa hak Aktor Missing menunggu konfirmasi
25. `Joko Susilo {runId}` mengirim Report Missing atas `Scanner Zebra DS2208 {runId}` yang ia pegang dengan What happened `Terakhir terlihat di pantry lantai dua`
26. Verifikasi record `Scanner Zebra DS2208 {runId}` berstatus `Waiting for Confirmation`
27. Verifikasi status global aset `Scanner Zebra DS2208 {runId}` menjadi Missing sebelum Aktor Missing memutuskan
28. Verifikasi record `Scanner Zebra DS2208 {runId}` mencatat `Joko Susilo {runId}` sebagai Last holder
29. Verifikasi record laporan pemegang menyimpan Source sesuai titik masuk laporan pemegang, tanpa nomor transaksi
30. Verifikasi record `Scanner Zebra DS2208 {runId}` memuat node `Reported missing by` atas nama `Joko Susilo {runId}` dengan What happened `Terakhir terlihat di pantry lantai dua`

### Satu laporan campuran hanya membuat record untuk aset yang layak
31. Rina W mengirim Report Missing atas `Drill Bosch GSB {runId}`, `Camera Canon EOS {runId}`, `Printer HP LaserJet M404 {runId}`, `Toyota Innova {runId}`, `Mesin Fotokopi Ricoh {runId}`, dan `Meja Kerja Kayu {runId}` dalam satu laporan dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
32. Verifikasi aset `Drill Bosch GSB {runId}` mendapat record `Missing` walau aset lain dalam laporan itu ditolak
33. Verifikasi aset `Camera Canon EOS {runId}` ditolak dengan keterangan `Already reported missing` beserta tautan ke record berjalan yang ada
34. Verifikasi aset `Camera Canon EOS {runId}` tetap punya tepat satu record berjalan dengan What happened `Kamera tidak ada di lemari penyimpanan` yang tidak berubah
35. Verifikasi aset `Printer HP LaserJet M404 {runId}` dengan record `Waiting for Confirmation` ditolak dengan keterangan `Already reported missing` dan tetap punya tepat satu record berjalan
36. Verifikasi aset `Toyota Innova {runId}` dengan record `Reported Disposal` ditolak dengan keterangan `Already reported missing` dan tetap punya tepat satu record berjalan
37. Verifikasi aset `Mesin Fotokopi Ricoh {runId}` dengan record `In Disposal Process` ditolak dengan keterangan `Already reported missing` dan tetap punya tepat satu record berjalan
38. Verifikasi aset `Meja Kerja Kayu {runId}` ditolak dengan keterangan `Disposed`, tidak mendapat record baru, dan status globalnya tetap `Disposed`
39. Verifikasi laporan itu hanya menambah satu record berjalan baru, sebanyak aset yang diterima, dan tidak membuat record untuk aset yang ditolak

### Aset di luar cakupan Group pelapor ditolak
40. Andi P mengirim Report Missing atas `Hand Truck Gudang {runId}` yang berada di Group `Warehouse` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
41. Verifikasi aset `Hand Truck Gudang {runId}` ditolak dengan keterangan `Outside your group` dan tidak mendapat record
42. Verifikasi status global aset `Hand Truck Gudang {runId}` tetap seperti sebelum laporan

### Aset yang tidak lagi dipegang pelapor ditolak
43. `Joko Susilo {runId}` mengirim Report Missing atas `Tablet Samsung Tab A8 {runId}` yang dipegang Andi P dengan What happened `Terakhir terlihat di pantry lantai dua`
44. Verifikasi aset `Tablet Samsung Tab A8 {runId}` ditolak dengan keterangan `No longer held by you` dan tidak mendapat record
45. Verifikasi status global aset `Tablet Samsung Tab A8 {runId}` tetap seperti sebelum laporan

### Dua laporan serentak atas aset yang sama menghasilkan satu record
46. Rina W dan Andi P mengirim Report Missing atas `Genset Honda EU22 {runId}` pada saat yang sama, masing-masing dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
47. Verifikasi tepat satu dari dua permintaan menghasilkan record dan permintaan yang lain ditolak
48. Verifikasi aset `Genset Honda EU22 {runId}` hanya punya satu record berjalan dan hanya satu node `Reported missing by`, sehingga laporan yang ditolak tidak membuat record maupun node
49. Verifikasi penolakan memuat tautan ke record yang sudah ada
50. Verifikasi penolakan memuat pesan `[Asset Name] was just reported missing by [User Name].` dengan `[Asset Name]` berisi nama aset `Genset Honda EU22 {runId}` dan `[User Name]` berisi pelapor yang sama dengan Reported By pada record yang tersimpan

### Last holder yang dinonaktifkan tetap tercatat
51. Rina W mengirim Report Missing atas `Kamera Sony A7 {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
52. `Sari Dewi {runId}` dinonaktifkan
53. Verifikasi record `Kamera Sony A7 {runId}` tetap ada dan berstatus `Missing`
54. Verifikasi record `Kamera Sony A7 {runId}` tetap mencatat `Sari Dewi {runId}` sebagai Last holder
55. Verifikasi `Kamera Sony A7 {runId}` tidak masuk Return list offboarding `Sari Dewi {runId}`

### Penghapusan data aset dan Group yang dirujuk record
56. Rina W menjalankan Delete Asset Data atas `Camera Canon EOS {runId}`
57. Verifikasi penghapusan `Camera Canon EOS {runId}` ditolak, aset dan record `Missing`-nya tetap ada
58. Rina W menjalankan Delete Asset Data atas `Printer HP LaserJet M404 {runId}`
59. Verifikasi penghapusan `Printer HP LaserJet M404 {runId}` ditolak, aset dan record `Waiting for Confirmation`-nya tetap ada
60. Rina W menjalankan Delete Asset Data atas `Toyota Innova {runId}`
61. Verifikasi penghapusan `Toyota Innova {runId}` ditolak, aset dan record `Reported Disposal`-nya tetap ada
62. Rina W menjalankan Delete Asset Data atas `Mesin Fotokopi Ricoh {runId}`
63. Verifikasi penghapusan `Mesin Fotokopi Ricoh {runId}` ditolak, aset dan record `In Disposal Process`-nya tetap ada
64. Rina W menjalankan Delete Asset Data atas seleksi `Kursi Ergonomis {runId}` dan `Camera Canon EOS {runId}` sekaligus
65. Verifikasi seluruh seleksi ditolak dan `Kursi Ergonomis {runId}` tetap ada walau aset itu tanpa record berjalan
66. Rina W menjalankan Delete Asset Data atas `Meja Kerja Kayu {runId}`
67. Verifikasi `Meja Kerja Kayu {runId}` terhapus dan record History `Disposed` miliknya ikut terhapus permanen
68. Rina W menghapus Group `Ruang Arsip {runId}`
69. Verifikasi penghapusan Group `Ruang Arsip {runId}` ditolak karena `Brankas Besi {runId}` masih punya record berjalan, dan Group itu tetap ada
70. Rina W menghapus Group `Lantai Dua {runId}`
71. Verifikasi Group `Lantai Dua {runId}` terhapus karena hanya dirujuk record History `Papan Tulis {runId}` sebagai Found at
72. Verifikasi record History `Papan Tulis {runId}` tetap memuat Found at `Lantai Dua {runId}` yang tersimpan saat record selesai

### Aset Unmanaged tanpa record berjalan boleh dihapus beserta riwayatnya
73. Rina W menjalankan Delete Asset Data atas `Kursi Ergonomis {runId}` saja
74. Verifikasi `Kursi Ergonomis {runId}` terhapus walau berstatus Unmanaged karena tidak punya record berjalan
75. Verifikasi record History `Found` milik `Kursi Ergonomis {runId}` ikut terhapus permanen
76. Verifikasi riwayat transaksi aset `Kursi Ergonomis {runId}` ikut terhapus permanen
77. Verifikasi riwayat transaksi aset `Meja Kerja Kayu {runId}` ikut terhapus permanen bersama record History `Disposed` miliknya

### Penghapusan Category yang dirujuk record
78. Rina W menghapus Category `Perabot Arsip {runId}`
79. Verifikasi penghapusan Category `Perabot Arsip {runId}` ditolak karena `Lemari Arsip Baja {runId}` masih punya record berjalan, dan Category itu tetap ada
80. Rina W menghapus Category `Peralatan Gudang {runId}`
81. Verifikasi Category `Peralatan Gudang {runId}` terhapus karena hanya dirujuk record History `Rak Besi Gudang {runId}`
82. Verifikasi record History `Rak Besi Gudang {runId}` tetap memuat Category `Peralatan Gudang {runId}` yang tersimpan saat record selesai

### Pelapor dari Task Detail Audit
83. `Hendra Kusuma {runId}` mengirim Report Missing atas `Rak Server Dell {runId}` dari Task Detail Audit sesi `Audit Ruang Server {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
84. Verifikasi record `Rak Server Dell {runId}` berstatus `Waiting for Confirmation` dengan Source `Audit`
85. Verifikasi status global aset `Rak Server Dell {runId}` langsung menjadi Missing sebelum Aktor Missing memutuskan
86. `Hendra Kusuma {runId}` mengirim Report Missing atas `Proyektor BenQ MW550 {runId}` yang berada di luar cakupan sesi `Audit Ruang Server {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
87. Verifikasi aset `Proyektor BenQ MW550 {runId}` ditolak dan tidak mendapat record
88. Rina W mengirim Report Missing atas `Switch Cisco Catalyst {runId}` dari Task Detail Audit sesi `Audit Ruang Server {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
89. Verifikasi record `Switch Cisco Catalyst {runId}` langsung berstatus `Missing` dengan Source `Audit`
90. Andi P mengirim Report Missing atas `UPS APC Smart {runId}` dari Task Detail Audit sesi `Audit Ruang Server {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
91. Verifikasi record `UPS APC Smart {runId}` langsung berstatus `Missing` dengan Source `Audit`

### Mark as Found tidak dibatasi Activity Lock dan tidak mengubah baris pemeriksaan aset yang sudah final
92. Rina W mengirim Mark as Found atas record `Hand Pallet Truck {runId}` dengan Found at default Group aset dan Asset Status `Normal`
93. Verifikasi Mark as Found atas `Hand Pallet Truck {runId}` tidak ditolak oleh Activity Lock `In Audit` miliknya dan record berubah menjadi `Found`
94. Rina W mengirim Mark as Found atas record `Monitor LG 27UL500 {runId}` dengan Found at default Group aset dan Asset Status `Normal`
95. Verifikasi Mark as Found atas `Monitor LG 27UL500 {runId}` tidak ditolak oleh Activity Lock `Under Maintenance` miliknya dan record berubah menjadi `Found`
96. Rina W mengirim Mark as Found atas record `Kabinet Besi Arsip {runId}` dengan Found at default Group aset dan Asset Status `Normal`
97. Verifikasi Mark as Found atas `Kabinet Besi Arsip {runId}` diterima dan baris sesi pemeriksaan aset miliknya yang sudah final tidak berubah

### Report Missing atas aset dengan baris Disposal berjalan
98. Rina W mengirim Report Missing atas `Generator Perkins 20kVA {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
99. Verifikasi baris Disposal berjenis `Sell` atas `Generator Perkins 20kVA {runId}` berstatus `Canceled` oleh `System` dengan alasan `Asset reported missing`
100. Rina W mengirim Report Missing atas `Kompresor Udara Swan {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
101. Verifikasi Draft Disposal yang memuat `Kompresor Udara Swan {runId}` tidak berubah dan aset `Kompresor Udara Swan {runId}` ditandai ⚠
