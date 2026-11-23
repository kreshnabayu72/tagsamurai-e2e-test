---
id: TC-FA-DAMAGED-BE-213-foto-bukti-file-manager-server
title: "Server mencatat Damaged Photo dan After photo sebagai bukti sekali kirim dengan Source Damaged Photo dan Repair Photo yang hanya ditulis modul ini, tanpa aksi yang mengganti atau mengosongkannya, dan penghapusan file lewat File Manager tidak diblokir serta tidak mengubah status record, status global aset, penanda, atau hasil Mark as Repaired"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r91", "§Aturan Logika Modul#r92", "§Aturan Logika Modul#r96", EC-DMG-40, "§9.4.4#r17", "§9.2#b22", FLD-DMG-04, "§9.4.1#r14", "§9.9#p4", "§9.7#r18"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r91": [3, 5, 7, 9, 11, 13, 15, 16, 41]
  "§Aturan Logika Modul#r92": [18, 19, 21, 43, 44, 46, 47, 49, 51]
  "§Aturan Logika Modul#r96": [24, 25, 27, 28, 30, 31, 33, 34, 37, 39, 60, 61]
  EC-DMG-40: [24, 25, 27, 28, 30, 31, 33, 34, 35, 39, 60, 61]
  "§9.4.4#r17": 35
  "§9.2#b22": [24, 27, 30, 33]
  FLD-DMG-04: [15, 16, 46]
  "§9.4.1#r14": [24, 25, 27, 28, 30, 31, 33, 34]
  "§9.9#p4": [54, 57, 59]
  "§9.7#r18": [25, 28, 31, 34, 63, 65, 67]
---

# Server mencatat Damaged Photo dan After photo sebagai bukti sekali kirim dengan Source Damaged Photo dan Repair Photo yang hanya ditulis modul ini, tanpa aksi yang mengganti atau mengosongkannya, dan penghapusan file lewat File Manager tidak diblokir serta tidak mengubah status record, status global aset, penanda, atau hasil Mark as Repaired

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged.
  - Pemegang Manage asset & TAG (Update) `Rina Wulandari {runId}`, Aktor Damaged pada Group `Head Office {runId}`.
  - Pelapor umum `Budi Santoso {runId}`, pemegang aset, tanpa role Damaged.
  - Aktor peminjaman `Yoga Tanuwijaya {runId}`, Aktor penugasan `Dewi Anggraini {runId}`, dan Aktor penemuan aset `Hendra Saputra {runId}`.
  - Staff Auditor `Sinta Marlina {runId}`, pelapor dari Task Detail Audit, tanpa hak Aktor Damaged pada Group aset.
- Data:
  - DU-213-1: User `Agus Pratama {runId}`, Total Control, Aktor Damaged, cakupan seluruh client.
  - DU-213-2: User `Rina Wulandari {runId}`, Manage asset & TAG (Update), Aktor Damaged, cakupan Group `Head Office {runId}` beserta descendant.
  - DU-213-3: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang.
  - DU-213-4: User `Yoga Tanuwijaya {runId}`, Aktor Borrow, cakupan Group `Head Office {runId}`.
  - DU-213-5: User `Dewi Anggraini {runId}`, Aktor Assignment, cakupan Group `Head Office {runId}`.
  - DU-213-6: User `Hendra Saputra {runId}`, Aktor Missing, cakupan Group `Head Office {runId}`.
  - DU-213-7: User `Sinta Marlina {runId}`, Staff Auditor, pelapor dari Task Detail Audit, tanpa hak Aktor Damaged, cakupan Group `Head Office {runId}`.
  - DU-213-8: Group `Head Office {runId}`.
  - DU-213-9: Aset `Laptop Dell Latitude 5420 - 401 {runId}`, Group `Head Office {runId}`, `Normal`, tanpa TAG, tanpa record berjalan.
  - DU-213-10: Aset `Tablet Samsung Tab A8 - 402 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-213-11: Aset `Monitor Dell P2422H - 403 {runId}`, Group `Head Office {runId}`, item sesi Audit berjalan milik `Sinta Marlina {runId}`, `Normal`, tanpa record berjalan.
  - DU-213-12: Aset `Projector Epson EB-X06 - 404 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-213-13: Aset `Tablet Samsung Tab A8 - 405 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-213-14: Aset `Camera Canon EOS - 406 {runId}`, Group `Head Office {runId}`, `Missing` tanpa record Damaged.
  - DU-213-15: Aset `Printer HP LaserJet M404 - 407 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged` dengan Damaged Photo `layar-retak.jpg`.
  - DU-213-16: Aset `Camera Canon EOS - 408 {runId}`, Group `Head Office {runId}`, `Missing` dengan record `Damaged` ditahan penanda `Missing` dan Damaged Photo `layar-retak.jpg`.
  - DU-213-17: What happened `Layar retak setelah terjatuh dari meja {runId}`, Damaged Photo `layar-retak.jpg`.
  - DU-213-18: Description `Engsel longgar saat dikembalikan {runId}`, foto Return `foto-return.jpg`.
  - DU-213-19: Description `Layar tergores saat dikembalikan {runId}`, foto Unassign `foto-unassign.jpg`.
  - DU-213-20: Note `Ditemukan rusak di ruang arsip {runId}`, Damaged Photo `ditemukan-rusak.jpg`.
  - DU-213-21: Repair note `Komponen rusak sudah diganti {runId}`, After photo `sesudah-perbaikan.jpg`.
  - DU-213-22: Reason `Foto yang dikirim bukan foto aset ini {runId}`.
  - DU-213-23: Aset `Tablet Samsung Tab A8 - 409 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-213-24: Aset `Laptop Dell Latitude 5420 - 410 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}` dengan Damaged Photo `layar-retak.jpg`.
  - DU-213-25: Aset `Printer HP LaserJet M404 - 411 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged` dengan Damaged Photo `layar-retak.jpg`.
  - DU-213-26: Aset `Camera Canon EOS - 412 {runId}`, Group `Head Office {runId}`, punya record `Damaged` dengan Damaged Photo `layar-retak.jpg`.
  - DU-213-27: Aset `Scanner Fujitsu fi-7160 - 413 {runId}`, Group `Head Office {runId}`, punya record `Damaged` dengan Damaged Photo `layar-retak.jpg`.
  - DU-213-28: What happened `Terakhir terlihat di gudang lantai dua {runId}`, Damaged Photo `terakhir-terlihat.jpg`.
  - DU-213-29: Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`.
  - DU-213-30: Aset `Printer HP LaserJet M404 - 414 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged`.
  - DU-213-31: Aset `Laptop Dell Latitude 5420 - 415 {runId}`, Group `Head Office {runId}`, `Normal`, tanpa TAG, tanpa record berjalan.
  - DU-213-32: Repair note dikosongkan, After photo `sesudah-perbaikan.jpg`.
  - DU-213-33: What happened dikosongkan, Damaged Photo `layar-retak.jpg`.
- Kondisi:
  - After photo required bernilai `OFF`.

## Test Steps
### Damaged Photo dan After photo tercatat di File Manager sebagai Source Damaged Photo dan Repair Photo yang ditulis modul ini
1. Catat jumlah berkas `File Manager` dengan Source `Damaged Photo` dan Source `Repair Photo` milik aset uji
2. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 401 {runId}` dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
3. Verifikasi `File Manager` memuat berkas baru `layar-retak.jpg` dengan Source `Damaged Photo` yang ditulis modul Damaged
4. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged dari `My Asset` atas `Tablet Samsung Tab A8 - 402 {runId}` dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
5. Verifikasi `File Manager` memuat berkas baru `layar-retak.jpg` dengan Source `Damaged Photo` dari laporan pemegang aset
6. Staff Auditor `Sinta Marlina {runId}` mengirim Report Damaged dari Task Detail Audit atas `Monitor Dell P2422H - 403 {runId}` dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
7. Verifikasi `File Manager` memuat berkas baru `layar-retak.jpg` dengan Source `Damaged Photo` dari laporan Task Detail Audit
8. Aktor peminjaman `Yoga Tanuwijaya {runId}` mengirim Report Damaged dari halaman Return Borrow atas `Projector Epson EB-X06 - 404 {runId}` dengan Description `Engsel longgar saat dikembalikan {runId}` dan foto Return `foto-return.jpg`
9. Verifikasi `File Manager` memuat berkas baru `foto-return.jpg` dengan Source `Damaged Photo` dari laporan halaman peminjaman
10. Aktor penugasan `Dewi Anggraini {runId}` melakukan Unassign berstatus `Unassigned` bermarker `Damaged` atas `Tablet Samsung Tab A8 - 405 {runId}` dengan Description `Layar tergores saat dikembalikan {runId}` dan foto Unassign `foto-unassign.jpg`
11. Verifikasi `File Manager` memuat berkas baru `foto-unassign.jpg` dengan Source `Damaged Photo` dari Unassign bermarker `Damaged`
12. Aktor penemuan aset `Hendra Saputra {runId}` menjalankan Mark as Found Damaged atas `Camera Canon EOS - 406 {runId}` dengan Note `Ditemukan rusak di ruang arsip {runId}` dan Damaged Photo `ditemukan-rusak.jpg`
13. Verifikasi `File Manager` memuat berkas baru `ditemukan-rusak.jpg` dengan Source `Damaged Photo` dari Mark as Found Damaged
14. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 407 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}` dan After photo `sesudah-perbaikan.jpg`
15. Verifikasi `File Manager` memuat berkas baru `sesudah-perbaikan.jpg` dengan Source `Repair Photo`
16. Verifikasi berkas Source `Damaged Photo` bertambah tepat enam dan berkas Source `Repair Photo` bertambah tepat satu dari yang dicatat, seluruhnya ditulis oleh Submit modul Damaged tanpa penulis lain

### Damaged Photo dan After photo adalah bukti sekali kirim yang tidak diganti atau dikosongkan aksi lain
17. Total Control `Agus Pratama {runId}` melakukan Confirm atas laporan `Tablet Samsung Tab A8 - 402 {runId}`
18. Verifikasi Damaged Photo `layar-retak.jpg` pada node `Reported damaged by` `Tablet Samsung Tab A8 - 402 {runId}` tetap sama dan berkas Source `Damaged Photo` di `File Manager` tidak diganti maupun dikosongkan
19. Verifikasi auto-transition `File Manager` tidak dipicu oleh Confirm itu sehingga Source berkas tetap `Damaged Photo`
20. Total Control `Agus Pratama {runId}` melakukan Reject atas laporan `Projector Epson EB-X06 - 404 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
21. Verifikasi foto Return `foto-return.jpg` pada node `Reported damaged by` tetap sama dan berkas Source `Damaged Photo` di `File Manager` tidak diganti maupun dikosongkan oleh Reject itu

### Penghapusan berkas lewat File Manager tidak diblokir dan tidak mengubah status record, status global aset, penanda, atau hasil Mark as Repaired
22. Catat status record, status global aset, penanda, dan jumlah event `damaged_*` untuk `Laptop Dell Latitude 5420 - 401 {runId}`, `Monitor Dell P2422H - 403 {runId}`, `Camera Canon EOS - 408 {runId}`, dan `Printer HP LaserJet M404 - 407 {runId}`
23. Total Control `Agus Pratama {runId}` menghapus berkas Damaged Photo laporan `Laptop Dell Latitude 5420 - 401 {runId}` dari `File Manager`
24. Verifikasi penghapusan berkas itu tidak diblokir dan berkasnya terhapus
25. Verifikasi record `Laptop Dell Latitude 5420 - 401 {runId}` tetap `Damaged` dan status global aset tetap sama dengan yang dicatat
26. Total Control `Agus Pratama {runId}` menghapus berkas Damaged Photo laporan `Monitor Dell P2422H - 403 {runId}` dari `File Manager`
27. Verifikasi penghapusan berkas itu tidak diblokir dan berkasnya terhapus
28. Verifikasi record `Monitor Dell P2422H - 403 {runId}` tetap `Waiting for Confirmation`, status global aset tidak berubah, dan penanda `Damage reported` tetap ada
29. Total Control `Agus Pratama {runId}` menghapus berkas Damaged Photo laporan `Camera Canon EOS - 408 {runId}` dari `File Manager`
30. Verifikasi penghapusan berkas itu tidak diblokir dan berkasnya terhapus
31. Verifikasi record `Camera Canon EOS - 408 {runId}` tetap `Damaged` ditahan penanda `Missing`, dan status global aset serta penanda `Missing` tidak berubah
32. Total Control `Agus Pratama {runId}` menghapus berkas After photo milik Mark as Repaired `Printer HP LaserJet M404 - 407 {runId}` dari `File Manager`
33. Verifikasi penghapusan berkas itu tidak diblokir dan berkasnya terhapus
34. Verifikasi record `Printer HP LaserJet M404 - 407 {runId}` tetap `Repaired`, status global aset tetap sama, dan hasil Mark as Repaired (Repair note, Resolved By, dan Resolved Date) tidak berubah
35. Verifikasi keempat penghapusan berkas itu tidak memicu event `damaged_*`

### Kewajiban foto hanya dievaluasi saat Submit, tidak saat membaca record
36. Total Control `Agus Pratama {runId}` melakukan Confirm atas laporan `Monitor Dell P2422H - 403 {runId}` yang Damaged Photo-nya sudah dihapus dari `File Manager`
37. Verifikasi Confirm diterima tanpa kewajiban foto dan record menjadi `Damaged`
38. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 401 {runId}` yang Damaged Photo-nya sudah dihapus dengan Repair note `Komponen rusak sudah diganti {runId}` dan tanpa After photo
39. Verifikasi Mark as Repaired diterima dan record menjadi `Repaired`, karena kewajiban foto hanya berlaku saat Submit

### Report Damaged dari halaman transaksi penugasan menulis berkas Source Damaged Photo
40. Aktor penugasan `Dewi Anggraini {runId}` mengirim Report Damaged dari halaman transaksi penugasan atas `Tablet Samsung Tab A8 - 409 {runId}` yang sedang ditugaskan dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
41. Verifikasi `File Manager` memuat berkas baru `layar-retak.jpg` dengan Source `Damaged Photo` dari laporan halaman transaksi penugasan

### Cancel Report dan Mark as Repaired tidak mengganti atau mengosongkan Damaged Photo
42. Pelapor umum `Budi Santoso {runId}` membatalkan laporannya lewat Cancel Report atas `Laptop Dell Latitude 5420 - 410 {runId}`
43. Verifikasi record `Laptop Dell Latitude 5420 - 410 {runId}` menjadi `Canceled`, Damaged Photo `layar-retak.jpg` pada node `Reported damaged by` tetap sama, dan berkas Source `Damaged Photo` di `File Manager` tidak diganti maupun dikosongkan
44. Verifikasi auto-transition `File Manager` tidak dipicu oleh Cancel Report itu sehingga Source berkas tetap `Damaged Photo`
45. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 411 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}` dan After photo `sesudah-perbaikan.jpg`
46. Verifikasi Damaged Photo `layar-retak.jpg` pada node `Reported damaged by` `Printer HP LaserJet M404 - 411 {runId}` tetap sama dan berkas Source `Damaged Photo` di `File Manager` tidak diganti maupun dikosongkan, sedangkan After photo `sesudah-perbaikan.jpg` tercatat sebagai berkas terpisah dengan Source `Repair Photo`
47. Verifikasi auto-transition `File Manager` tidak dipicu oleh Mark as Repaired itu sehingga Source berkas Damaged Photo tetap `Damaged Photo`

### Transisi Missing dan Disposal tidak mengganti atau mengosongkan Damaged Photo
48. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Camera Canon EOS - 412 {runId}` dari tab Damaged dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
49. Verifikasi record `Camera Canon EOS - 412 {runId}` tetap `Damaged` ditahan penanda `Missing`, Damaged Photo `layar-retak.jpg` pada node `Reported damaged by` tetap sama, dan berkas Source `Damaged Photo` milik laporan semula tidak diganti maupun dikosongkan
50. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Scanner Fujitsu fi-7160 - 413 {runId}` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
51. Verifikasi record `Scanner Fujitsu fi-7160 - 413 {runId}` menjadi `Reported Disposal`, Damaged Photo `layar-retak.jpg` pada node `Reported damaged by` tetap sama, berkas Source `Damaged Photo` tidak diganti maupun dikosongkan, dan auto-transition `File Manager` tidak dipicu

### Foto dari submit Report Damaged yang gagal tidak pernah menjadi berkas permanen
52. Catat jumlah berkas `File Manager` dengan Source `Damaged Photo` milik aset `Scanner Fujitsu fi-7160 - 413 {runId}`
53. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Scanner Fujitsu fi-7160 - 413 {runId}` yang sudah punya record berjalan dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
54. Verifikasi laporan itu ditolak karena aset sudah punya record berjalan dan Damaged Photo `layar-retak.jpg` dari submit yang gagal tidak menjadi berkas permanen: jumlah berkas Source `Damaged Photo` milik aset itu di `File Manager` sama dengan yang dicatat

### Foto dari submit Mark as Repaired dan Report Damaged yang gagal validasi tidak pernah menjadi berkas permanen
55. Catat jumlah berkas `File Manager` dengan Source `Repair Photo` milik aset `Printer HP LaserJet M404 - 414 {runId}` dan Source `Damaged Photo` milik aset `Laptop Dell Latitude 5420 - 415 {runId}`
56. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 414 {runId}` dengan Repair note dikosongkan dan After photo `sesudah-perbaikan.jpg`
57. Verifikasi permintaan ditolak karena Repair note kosong, record tetap `Damaged`, dan After photo `sesudah-perbaikan.jpg` dari submit yang gagal tidak menjadi berkas permanen: jumlah berkas Source `Repair Photo` milik aset itu di `File Manager` sama dengan yang dicatat
58. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 415 {runId}` dengan What happened dikosongkan dan Damaged Photo `layar-retak.jpg`
59. Verifikasi permintaan ditolak karena What happened kosong, tidak ada record yang dibuat untuk aset itu, dan Damaged Photo `layar-retak.jpg` dari submit yang gagal tidak menjadi berkas permanen: jumlah berkas Source `Damaged Photo` milik aset itu di `File Manager` sama dengan yang dicatat

### Kolom Photo hanya mengikuti Damaged Photo pertama, sedangkan After photo hanya memengaruhi node Marked as repaired by
60. Verifikasi respons daftar record untuk `Laptop Dell Latitude 5420 - 401 {runId}` tidak lagi memuat Damaged Photo pada kolom Photo, karena Damaged Photo pertamanya sudah dihapus
61. Verifikasi respons daftar record untuk `Printer HP LaserJet M404 - 407 {runId}` tetap memuat Damaged Photo pertama `layar-retak.jpg` pada kolom Photo, karena yang dihapus hanya After photo dan After photo hanya memengaruhi node `Marked as repaired by`

### Rujukan foto pada node Damage Log kosong sesudah berkasnya dihapus lewat File Manager, termasuk pada respons untuk pelapor
62. Total Control `Agus Pratama {runId}` membuka Damage Log record `Printer HP LaserJet M404 - 407 {runId}` yang After photo-nya sudah dihapus dari `File Manager`
63. Verifikasi node `Marked as repaired by` tidak memuat rujukan After photo karena berkasnya sudah dihapus, sedangkan node `Reported damaged by` tetap memuat Damaged Photo `layar-retak.jpg`
64. Total Control `Agus Pratama {runId}` membuka Damage Log record `Laptop Dell Latitude 5420 - 401 {runId}` yang Damaged Photo-nya sudah dihapus dari `File Manager`
65. Verifikasi node `Reported damaged by` tidak memuat rujukan Damaged Photo karena berkasnya sudah dihapus
66. Staff Auditor `Sinta Marlina {runId}`, pelapor, membaca Damage Log laporannya `Monitor Dell P2422H - 403 {runId}` yang Damaged Photo-nya sudah dihapus dari `File Manager`, yaitu Damage Log My Asset pelapor
67. Verifikasi respons untuk pelapor itu tidak memuat rujukan Damaged Photo karena berkasnya sudah dihapus
