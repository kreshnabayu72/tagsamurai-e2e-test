---
id: TC-FA-MISS-BE-073-validasi-field
title: "Server: validasi What happened, Reason, Update, Note, Damaged Photo, Found at, dan Scan TAG"
layer: be-e2e
priority: High
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [§9.9#r1, §9.9#r2, §9.9#r3, §9.9#r4, §9.9#r5, §9.9#r6, §9.9#r7, §9.9#r8, §9.9#p3, §9.9#p4, §9.2#b65, §9.4.2#r32, §9.4.4#r29, §6#r4, §6#p1, §1.2#r89, EB-FRM-4@report-missing, EB-FRM-4@reject-report, EB-FRM-4@add-update, EB-FRM-4@mark-as-found, EB-FRM-10@found-at]
smoke: []
dependsOn: []
trace:
  §9.9#r1: [2, 4, 6, 8]
  §9.9#r2: [26, 28, 30, 32, 34, 38]
  §9.9#r3: [40, 42, 44, 47, 49, 51]
  §9.9#r4: [53, 55, 61]
  §9.9#r5: [36, 38, 53, 57, 59, 63]
  §9.9#r6: [55, 59, 63]
  §9.9#r7: [10, 12, 14, 16]
  §9.9#r8: [18, 20, 22, 24]
  §9.9#p3: [26, 34, 36, 38]
  §9.9#p4: 59
  §9.2#b65: [18, 20, 22]
  §9.4.2#r32: [18, 22]
  §9.4.4#r29: [18, 22]
  §6#r4: [28, 30, 32]
  §6#p1: 28
  §1.2#r89: 63
  EB-FRM-4@report-missing: [2, 6, 8]
  EB-FRM-4@reject-report: [10, 14, 16]
  EB-FRM-4@add-update: [22, 24]
  EB-FRM-4@mark-as-found: [36, 57, 59]
  EB-FRM-10@found-at: 47
---

# Server: validasi What happened, Reason, Update, Note, Damaged Photo, Found at, dan Scan TAG

## Prerequisites
- Aktor: Rina W, Total Control dengan cakupan seluruh client; `Maya Anggraini {runId}` (DU-073-1), Group Manager dengan Group binaan Head Office beserta sub-group; `Joko Susilo {runId}` (DU-073-2), pemegang tanpa hak Aktor Missing.
- Data:
  - DU-073-1: User Name `Maya Anggraini {runId}`, Peran `Group Manager`, Cakupan `Group Head Office beserta sub-group`.
  - DU-073-2: User Name `Joko Susilo {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Cakupan `aset yang ia pegang`.
  - DU-073-3: Asset Name `Drill Bosch GSB {runId}`, Asset ID `FA073-001`, Group aset `Finance Room`, Condition `Normal`, Record berjalan `tidak ada`.
  - DU-073-4: Asset Name `Printer HP LaserJet M404 {runId}`, Asset ID `FA073-002`, Group aset `Finance Room`, Condition `Normal`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`.
  - DU-073-5: Asset Name `Camera Canon EOS {runId}`, Asset ID `FA073-003`, Group aset `Finance Room`, Condition `Normal`, Record berjalan `Missing, dilaporkan Rina W`.
  - DU-073-6: Asset Name `Laptop Dell Latitude 5420 {runId}`, Asset ID `FA073-004`, Group aset `Finance Room`, Condition `Normal`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `QR-073-0001`, TAG yang sudah diganti `QR-073-0003`.
  - DU-073-7: Asset Name `Hand Pallet Truck {runId}`, Asset ID `FA073-005`, Group aset `Finance Room`, Condition `Normal`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `tidak ada`.
  - DU-073-8: Asset Name `Monitor LG 27UL500 {runId}`, Asset ID `FA073-006`, Group aset `Head Office`, Condition `Normal`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `tidak ada`.
  - DU-073-9: Asset Name `Projector Epson EB-X06 {runId}`, Asset ID `FA073-007`, Group aset `Finance Room`, Condition `Normal`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `tidak ada`.
  - DU-073-10: Asset Name `Toyota Innova {runId}`, Asset ID `FA073-008`, Group aset `Finance Room`, Condition `Damaged`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `tidak ada`, Damage record `ditahan`.
  - DU-073-11: TAG TAG `QR-073-0002`, Terpasang pada `Mesin Fotokopi Ricoh {runId}`.
  - DU-073-12: TAG TAG `QR-073-0001`, Terpasang pada `Laptop Dell Latitude 5420 {runId}`.
  - DU-073-13: TAG TAG `QR-073-9999`, Terpasang pada `tidak ada`.
  - DU-073-14: TAG TAG `8991234567890`, Terpasang pada `bukan TAG Tag Samurai`.
  - DU-073-15: TAG TAG `QR-073-0003`, Terpasang pada `sudah diganti pada Laptop Dell Latitude 5420 {runId}`.
  - DU-073-16: Group Name `Lantai Tiga {runId}`.
  - DU-073-17: Berkas Berkas `foto-kerusakan-073.png`, Format `PNG`, Ukuran `2 MB`.

## Test Steps
### What happened wajib terisi dan maksimal 360 karakter
1. Rina W mengirim Report Missing atas `Drill Bosch GSB {runId}` dengan What happened dikosongkan
2. Verifikasi permintaan itu ditolak server dengan pesan `What happened must not be empty` dan `Drill Bosch GSB {runId}` tidak mendapat record
3. Rina W mengirim Report Missing atas `Drill Bosch GSB {runId}` dengan What happened yang hanya berisi spasi
4. Verifikasi permintaan itu ditolak dengan pesan `What happened must not be empty` karena spasi di tepi dibuang sebelum dihitung, dan `Drill Bosch GSB {runId}` tidak mendapat record
5. Rina W mengirim Report Missing atas `Drill Bosch GSB {runId}` dengan What happened `Laporan kehilangan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudan` (361 karakter)
6. Verifikasi permintaan itu ditolak dengan pesan `Max. 360 characters` dan `Drill Bosch GSB {runId}` tidak mendapat record
7. Rina W mengirim Report Missing atas `Drill Bosch GSB {runId}` dengan What happened `Laporan kehilangan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, guda` (360 karakter)
8. Verifikasi permintaan itu diterima, `Drill Bosch GSB {runId}` mendapat record `Missing`, dan What happened tersimpan utuh sepanjang 360 karakter

### Reason Reject wajib terisi dan maksimal 360 karakter
9. Rina W mengirim Reject atas record `Printer HP LaserJet M404 {runId}` dengan Reason dikosongkan
10. Verifikasi permintaan itu ditolak dengan pesan `Reason must not be empty` dan record `Printer HP LaserJet M404 {runId}` tetap `Waiting for Confirmation`
11. Rina W mengirim Reject atas record `Printer HP LaserJet M404 {runId}` dengan Reason yang hanya berisi spasi
12. Verifikasi permintaan itu ditolak dengan pesan `Reason must not be empty` dan record `Printer HP LaserJet M404 {runId}` tetap `Waiting for Confirmation`
13. Rina W mengirim Reject atas record `Printer HP LaserJet M404 {runId}` dengan Reason `Alasan penolakan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang,` (361 karakter)
14. Verifikasi permintaan itu ditolak dengan pesan `Max. 360 characters` dan record `Printer HP LaserJet M404 {runId}` tetap `Waiting for Confirmation`
15. Rina W mengirim Reject atas record `Printer HP LaserJet M404 {runId}` dengan Reason `Alasan penolakan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang` (360 karakter)
16. Verifikasi permintaan itu diterima dan record `Printer HP LaserJet M404 {runId}` berstatus `Rejected` dengan Reason tersimpan utuh sepanjang 360 karakter

### Update wajib terisi dan maksimal 360 karakter
17. Rina W mengirim Add Update atas record `Camera Canon EOS {runId}` dengan Update dikosongkan
18. Verifikasi permintaan itu ditolak dengan pesan `Update must not be empty` dan record `Camera Canon EOS {runId}` tidak mendapat node `Update added by`
19. Rina W mengirim Add Update atas record `Camera Canon EOS {runId}` dengan Update yang hanya berisi spasi
20. Verifikasi permintaan itu ditolak dengan pesan `Update must not be empty` dan record `Camera Canon EOS {runId}` tidak mendapat node `Update added by`
21. Rina W mengirim Add Update atas record `Camera Canon EOS {runId}` dengan Update `Catatan pencarian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang` (361 karakter)
22. Verifikasi permintaan itu ditolak dengan pesan `Max. 360 characters` dan record `Camera Canon EOS {runId}` tidak mendapat node `Update added by`
23. Rina W mengirim Add Update atas record `Camera Canon EOS {runId}` dengan Update `Catatan pencarian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudan` (360 karakter)
24. Verifikasi permintaan itu diterima dan record `Camera Canon EOS {runId}` mendapat tepat satu node `Update added by` dengan Update tersimpan utuh sepanjang 360 karakter

### Scan TAG wajib untuk aset ber-TAG dan harus TAG milik aset
25. Rina W mengirim Mark as Found atas record `Laptop Dell Latitude 5420 {runId}` dengan Asset Status `Normal` tanpa verifikasi Scan TAG
26. Verifikasi permintaan itu ditolak dengan pesan `Scan TAG must not be empty` dan record `Laptop Dell Latitude 5420 {runId}` tetap `Missing`
27. Rina W mengirim Mark as Found atas record `Laptop Dell Latitude 5420 {runId}` dengan Scan TAG `QR-073-0002` milik aset lain
28. Verifikasi permintaan itu ditolak dengan pesan `This TAG doesn't belong to [Asset Name].` untuk `Laptop Dell Latitude 5420 {runId}` dan record tetap `Missing`
29. Rina W mengirim Mark as Found atas record `Laptop Dell Latitude 5420 {runId}` dengan Scan TAG `QR-073-9999` yang tidak terdaftar
30. Verifikasi permintaan itu ditolak dengan pesan `This TAG doesn't belong to [Asset Name].` untuk `Laptop Dell Latitude 5420 {runId}` dan record tetap `Missing`
31. Rina W mengirim Mark as Found atas record `Laptop Dell Latitude 5420 {runId}` dengan Scan TAG `8991234567890` yang bukan TAG Tag Samurai
32. Verifikasi permintaan itu ditolak dengan pesan `This TAG doesn't belong to [Asset Name].` untuk `Laptop Dell Latitude 5420 {runId}` dan record tetap `Missing`
33. Rina W mengirim Mark as Found atas record `Laptop Dell Latitude 5420 {runId}` dengan Scan TAG `QR-073-0003` yang sudah diganti
34. Verifikasi permintaan itu ditolak dengan pesan `This TAG doesn't belong to [Asset Name].` untuk `Laptop Dell Latitude 5420 {runId}` karena TAG yang sudah diganti tidak dihitung, dan record tetap `Missing`
35. Rina W mengirim Mark as Found atas record `Laptop Dell Latitude 5420 {runId}` dengan Scan TAG `QR-073-0001`, Asset Status `Normal`, dan Note `Catatan kerusakan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang` (361 karakter)
36. Verifikasi permintaan itu ditolak dengan pesan `Max. 360 characters` walau TAG terverifikasi, dan record `Laptop Dell Latitude 5420 {runId}` tetap `Missing`
37. Rina W mengirim Mark as Found atas record `Laptop Dell Latitude 5420 {runId}` dengan Scan TAG `QR-073-0001`, Asset Status `Normal`, dan Note dikosongkan
38. Verifikasi permintaan itu diterima karena Note opsional pada Asset Status `Normal`, dan record `Laptop Dell Latitude 5420 {runId}` berstatus `Found`

### Found at wajib terisi, dalam cakupan aktor, dan hanya node terbawah
39. Rina W mengirim Mark as Found atas record `Hand Pallet Truck {runId}` dengan Found at dikosongkan dan Asset Status `Normal`
40. Verifikasi permintaan itu ditolak dengan pesan `Found at must not be empty` dan record `Hand Pallet Truck {runId}` tetap `Missing`
41. `Maya Anggraini {runId}` mengirim Mark as Found atas record `Hand Pallet Truck {runId}` dengan Found at `Warehouse` dan Asset Status `Normal`
42. Verifikasi permintaan itu ditolak karena Group `Warehouse` di luar cakupan `Maya Anggraini {runId}`, dan record `Hand Pallet Truck {runId}` tetap `Missing`
43. Rina W mengirim Mark as Found atas record `Hand Pallet Truck {runId}` dengan Found at `Head Office` dan Asset Status `Normal`
44. Verifikasi permintaan itu ditolak karena Group `Head Office` bukan node terbawah dan bukan Group aset, dan record `Hand Pallet Truck {runId}` tetap `Missing`
45. Group `Lantai Tiga {runId}` dihapus oleh aktor lain
46. Rina W mengirim Mark as Found atas record `Hand Pallet Truck {runId}` dengan Found at `Lantai Tiga {runId}` dan Asset Status `Normal`
47. Verifikasi permintaan itu ditolak dengan pesan `This found at no longer exists. Please select another.`, dan record `Hand Pallet Truck {runId}` tetap `Missing`
48. Rina W mengirim Mark as Found atas record `Hand Pallet Truck {runId}` dengan Found at `Server Room` dan Asset Status `Normal`
49. Verifikasi permintaan itu diterima, record `Hand Pallet Truck {runId}` berstatus `Found`, dan Group aset tetap `Finance Room` karena Found at hanya data
50. Rina W mengirim Mark as Found atas record `Monitor LG 27UL500 {runId}` dengan Found at `Head Office` yang merupakan Group aset itu sendiri dan Asset Status `Normal`
51. Verifikasi permintaan itu diterima dan record `Monitor LG 27UL500 {runId}` berstatus `Found`, karena Group aset selalu dapat dipilih walau bukan node terbawah

### Asset Status Damaged mewajibkan Damaged Photo dan Note
52. Rina W mengirim Mark as Found atas record `Projector Epson EB-X06 {runId}` dengan Asset Status `Damaged`, Damaged Photo diisi, dan Note dikosongkan
53. Verifikasi permintaan itu ditolak dengan pesan `Note must not be empty` dan record `Projector Epson EB-X06 {runId}` tetap `Missing`
54. Rina W mengirim Mark as Found atas record `Projector Epson EB-X06 {runId}` dengan Asset Status `Damaged`, Note `Layar retak dan bodi penyok pada sisi kiri`, dan Damaged Photo dikosongkan
55. Verifikasi permintaan itu ditolak dengan pesan `Damaged photo must not be empty` dan record `Projector Epson EB-X06 {runId}` tetap `Missing`
56. Rina W mengirim Mark as Found atas record `Projector Epson EB-X06 {runId}` dengan Asset Status `Damaged`, Damaged Photo, dan Note `Catatan kerusakan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang` (361 karakter)
57. Verifikasi permintaan itu ditolak dengan pesan `Max. 360 characters` dan record `Projector Epson EB-X06 {runId}` tetap `Missing`
58. Rina W mengirim Mark as Found atas record `Projector Epson EB-X06 {runId}` dengan Asset Status `Damaged`, Damaged Photo `foto-kerusakan-073.png` (PNG, 2 MB), dan Note `Catatan kerusakan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudan` (360 karakter)
59. Verifikasi permintaan itu diterima tanpa pesan ukuran berkas, record `Projector Epson EB-X06 {runId}` berstatus `Found`, dan Damaged Photo tersimpan dengan ukuran maksimal 1 MB

### Asal Damaged + Missing mengunci Asset Status dan mewajibkan Damaged Photo dan Note
60. Rina W mengirim Mark as Found atas record `Toyota Innova {runId}` dengan Asset Status `Normal`
61. Verifikasi permintaan itu ditolak karena Asset Status terisi `Damaged` dan tidak dapat diubah, dan record `Toyota Innova {runId}` tetap `Missing`
62. Rina W mengirim Mark as Found atas record `Toyota Innova {runId}` dengan Asset Status `Damaged`, tanpa Damaged Photo dan tanpa Note
63. Verifikasi permintaan itu ditolak karena Damaged Photo dan Note tetap wajib untuk asal `Damaged + Missing`, dan record `Toyota Innova {runId}` tetap `Missing`
