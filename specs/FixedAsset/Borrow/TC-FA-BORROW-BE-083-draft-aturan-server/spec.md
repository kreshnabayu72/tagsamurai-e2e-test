---
id: TC-FA-BORROW-BE-083-draft-aturan-server
title: "Draft bersama: cakupan Group, Draft tanpa aset, optimistic lock, dan hasil saat pembuat dinonaktifkan"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["BORROW-LOGIC-14a", "BORROW-LOGIC-14b", "BORROW-LOGIC-14c", "BORROW-LOGIC-14d", "BORROW-LOGIC-14e", "BORROW-LOGIC-14f", "BORROW-LOGIC-14g", "BORROW-LOGIC-14h", "BORROW-LOGIC-14i", "BORROW-LOGIC-14j", "BORROW-LOGIC-14k", "BORROW-LOGIC-14l", "BORROW-LOGIC-14m", "BORROW-LOGIC-14n", "BORROW-LOGIC-14o", "BORROW-LOGIC-14p", "BORROW-LOGIC-14q", "BORROW-LOGIC-14r", "BORROW-LOGIC-14s", "BORROW-LOGIC-14t", "BORROW-LOGIC-14u", "BORROW-LOGIC-14v", "EC-BRW-114", "EC-BRW-140", "EC-BRW-32", "EC-BRW-74", "EC-BRW-75", "EC-BRW-76", "EC-BRW-77", "EC-BRW-79", "EC-BRW-90", "F-BORROW-01.k1", "F-BORROW-01.k2", "F-BORROW-01.k3", "F-BORROW-01.k4", "F-BORROW-01.k5", "F-BORROW-01.k6", "§2.2#r4", "§9.2#b73", "§9.2#b78", "§9.4.3#b2", "§9.4.3#b3", "EB-CON-1"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-14a": [4]
  "BORROW-LOGIC-14b": [7, 8]
  "BORROW-LOGIC-14c": [9]
  "BORROW-LOGIC-14d": [6]
  "BORROW-LOGIC-14e": [28]
  "BORROW-LOGIC-14f": [5]
  "BORROW-LOGIC-14g": [28]
  "BORROW-LOGIC-14h": [15, 21, 132]
  "BORROW-LOGIC-14i": [17, 19, 24]
  "BORROW-LOGIC-14j": [36, 41, 43, 135, 136]
  "BORROW-LOGIC-14k": [22]
  "BORROW-LOGIC-14l": [30, 32, 121, 123, 125]
  "BORROW-LOGIC-14m": [32]
  "BORROW-LOGIC-14n": [34, 36, 43, 45]
  "BORROW-LOGIC-14o": [48, 50, 54]
  "BORROW-LOGIC-14p": [58]
  "BORROW-LOGIC-14q": [62, 63]
  "BORROW-LOGIC-14r": [60]
  "BORROW-LOGIC-14s": [55]
  "BORROW-LOGIC-14t": [56]
  "BORROW-LOGIC-14u": [39, 132, 133]
  "BORROW-LOGIC-14v": [97, 100]
  "EC-BRW-114": [65, 67, 68, 127, 129, 130]
  "EC-BRW-140": [111, 113, 115, 117, 119]
  "EC-BRW-32": [70, 71, 74]
  "EC-BRW-74": [79, 81, 83, 85, 87]
  "EC-BRW-75": [48, 50, 51, 52]
  "EC-BRW-76": [30, 34, 36, 38, 132]
  "EC-BRW-77": [91, 92]
  "EC-BRW-79": [94, 96, 97, 98, 100, 101]
  "EC-BRW-90": [104, 105]
  "F-BORROW-01.k1": [28, 41, 91]
  "F-BORROW-01.k2": [48, 50, 52]
  "F-BORROW-01.k3": [11, 12, 13]
  "F-BORROW-01.k4": [65, 70, 72, 77, 127]
  "F-BORROW-01.k5": [117, 119]
  "F-BORROW-01.k6": [94, 96, 97, 100, 101, 109]
  "§2.2#r4": [21, 26]
  "§9.2#b73": [2, 7, 8]
  "§9.2#b78": [108, 109]
  "§9.4.3#b2": [8]
  "§9.4.3#b3": [72]
  "EB-CON-1": [51]
---

# Draft bersama: cakupan Group, Draft tanpa aset, optimistic lock, dan hasil saat pembuat dinonaktifkan

## Prerequisites
- Aktor: `Agus Pratama {runId}` (Asset Admin, Group `Head Office {runId}`); `Hendra Kusuma {runId}` (Asset Admin, Group `Head Office {runId}` dan `Branch Surabaya {runId}`); `Putri Ayu {runId}` (Asset Admin, Group `Branch Surabaya {runId}`); `Siti Aminah {runId}` (Group Manager Group `Head Office {runId}`); `Wulan Sari {runId}` (Total Control); `Nina Rahma {runId}` (Monitoring & Report); `Oscar Wijaya {runId}` (Read Only).
- Data:
  - DU-083-1: Group asal aset: Name `Head Office {runId}`
  - DU-083-2: Group di luar cakupan sebagian Aktor: Name `Branch Surabaya {runId}`
  - DU-083-3: User akun login: Name `Agus Pratama {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin`, Group penugasan `Head Office {runId}`
  - DU-083-4: User akun login: Name `Hendra Kusuma {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin`, Group penugasan `Head Office {runId} dan Branch Surabaya {runId}`
  - DU-083-5: User akun login: Name `Siti Aminah {runId}`, Status `Active`, Activation Status `Activated`, Role `Group Manager`, Group binaan `Head Office {runId}`
  - DU-083-6: User akun login: Name `Wulan Sari {runId}`, Status `Active`, Activation Status `Activated`, Role `Total Control`, Scope `Seluruh client`
  - DU-083-7: User akun login: Name `Nina Rahma {runId}`, Status `Active`, Activation Status `Activated`, Role `Monitoring & Report`, Group penugasan `Head Office {runId}`
  - DU-083-8: User akun login: Name `Oscar Wijaya {runId}`, Status `Active`, Activation Status `Activated`, Role `Read Only`, Scope `Seluruh client`
  - DU-083-9: User akun login: Name `Joko Santoso {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin`, Group penugasan `Head Office {runId}`
  - DU-083-10: User akun login: Name `Yuli Astuti {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin`, Group penugasan `Head Office {runId}`
  - DU-083-11: User akun login: Name `Dewi Lestari {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-083-12: User akun login: Name `Bagus Santoso {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-083-13: User akun login: Name `Hana Permata {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-083-14: User akun login: Name `Fajar Nugroho {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-083-15: User akun login: Name `Rina Kusuma {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow, PIC`, Division `Marketing`
  - DU-083-16: Karyawan tanpa akun login: Name `Gita Anggraini {runId}`, Status `Active`, Division `Finance`, PIC `Rina Kusuma {runId}`
  - DU-083-17: Aset tersedia: Asset Name `Genset Honda EU22i {runId}`, Group `Head Office {runId}`, Category `Tools`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `OFF`, Satuan `Days`, Require approval `OFF`
  - DU-083-18: Aset tersedia: Asset Name `Scanner Fujitsu fi-8170 {runId}`, Group `Head Office {runId}`, Category `Scanner`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `OFF`, Satuan `Days`, Allow Borrow `Allow`
  - DU-083-19: Aset tersedia: Asset Name `Kursi Lipat Chitose {runId}`, Group `Head Office {runId}`, Category `Furniture`, TAG `Non TAG`, Custody `Available`, Condition `Normal`, Self service `OFF`, Satuan `Days`, Lifecycle `Disposed`
  - DU-083-20: Aset tersedia: Asset Name `Papan Info Akrilik {runId}`, Group `Head Office {runId}`, Category `Furniture`, TAG `Non TAG`, Custody `Available`, Condition `Normal`, Self service `OFF`, Satuan `Days`, Deleted `Ya`
  - DU-083-21: Aset tersedia: Asset Name `Mikrofon Shure SM58 {runId}`, Group `Head Office {runId}`, Category `Audio`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `OFF`, Satuan `Days`, Allowed borrower `Division Marketing`
  - DU-083-22: Pinjaman Overdue milik Borrower: Borrower `Bagus Santoso {runId}`, Aset `Kamera Fujifilm X-T4 {runId}`, Asset Code `AST-0412 {runId}`, Group `Head Office {runId}`, Status baris `Overdue`, Due date `T0 - 3 hari`, Block new borrow when overdue `ON`
  - DU-083-23: Draft tersimpan: Pembuat `Wulan Sari {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Monitor Dell P2422H {runId}, Proyektor ViewSonic PA503S {runId}; Branch Surabaya: Kamera Sony ZV-E10 {runId}, Tripod Benro T980 {runId}`, Duration dan Purpose `terisi pada keempat baris`
  - DU-083-24: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Dewi Lestari {runId}`, Aset `(tanpa aset)`, Group `—`
  - DU-083-25: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Laptop Asus ExpertBook B1 {runId}, Mouse Logitech MX Master 3 {runId}`
  - DU-083-26: Draft tersimpan: Pembuat `Siti Aminah {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Genset Honda EU22i {runId}`, Duration `2`, Purpose `Cadangan listrik rapat`
  - DU-083-27: Draft tersimpan: Pembuat `Siti Aminah {runId}`, Borrower `Hana Permata {runId}`, Aset `Head Office: Genset Honda EU22i {runId}`, Duration `2`, Purpose `Pendukung acara bazar`
  - DU-083-28: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Kabel HDMI Ugreen 5 m {runId}`
  - DU-083-29: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Scanner Fujitsu fi-8170 {runId}`, Duration `2`, Purpose `Pemindaian arsip`
  - DU-083-30: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Kursi Lipat Chitose {runId}, Papan Info Akrilik {runId}`, Duration `2`, Purpose `Acara pameran`
  - DU-083-31: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Bagus Santoso {runId}`, Aset `Head Office: Lensa Sigma 24-70 {runId}`, Duration `2`, Purpose `Liputan acara`
  - DU-083-32: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Mikrofon Shure SM58 {runId}`, Duration `2`, Purpose `Rekaman siniar`
  - DU-083-33: Draft tersimpan: Pembuat `Hendra Kusuma {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Bor Listrik Bosch GSB 13 {runId}; Branch Surabaya: Mesin Bor Pasir Makita {runId}`, Duration dan Purpose `terisi pada kedua baris`
  - DU-083-34: Draft tersimpan: Pembuat `Joko Santoso {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Handycam Sony FDR-AX43 {runId}`
  - DU-083-35: Draft tersimpan: Pembuat `Joko Santoso {runId}`, Borrower `Dewi Lestari {runId}`, Aset `(tanpa aset)`
  - DU-083-36: Draft tersimpan: Pembuat `Yuli Astuti {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Speaker JBL PartyBox 310 {runId}`
  - DU-083-37: Draft tersimpan: Pembuat `Yuli Astuti {runId}`, Borrower `Dewi Lestari {runId}`, Aset `(tanpa aset)`
  - DU-083-38: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Gita Anggraini {runId}`, Aset `Head Office: Printer Epson L3250 {runId}`, Duration `2`, Purpose `Pencetakan laporan`
  - DU-083-39: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Fajar Nugroho {runId}`, Aset `Head Office: Proyektor Epson EB-X49 {runId}`, Duration `2`, Purpose `Presentasi mingguan`
  - DU-083-40: Draft tersimpan: Pembuat `Sistem`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Lampu Studio Godox SL60 {runId}`, Origin `Restored by system`
  - DU-083-41: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Mixer Yamaha MG10 {runId}`, Origin `Restored`
  - DU-083-42: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Tablet Samsung Galaxy Tab S9 {runId}`, Origin `New`
  - DU-083-45: Aset tersedia: Asset Name `Dispenser Sanken HWD-77 {runId}`, Group `Head Office {runId}`, Category `Appliance`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `OFF`, Satuan `Days`, Require approval `OFF`
  - DU-083-46: User akun login: Name `Putri Ayu {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin`, Group penugasan `Branch Surabaya {runId}`
  - DU-083-47: Aset tersedia: Asset Name `Webcam Logitech C920 {runId}`, Group `Head Office {runId}`, Category `Electronics`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `OFF`, Satuan `Days`, Allow Borrow `Allow`
  - DU-083-48: Draft tersimpan: Pembuat `Wulan Sari {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Gerinda Tangan Bosch GWS 060 {runId}; Branch Surabaya: Kompresor Udara Ingco {runId}`, Duration dan Purpose `terisi pada kedua baris`
  - DU-083-49: Aset di Group lain: Asset Name `Bor Tangan Hitachi DV16V {runId}`, Group `Branch Surabaya {runId}`, Category `Tools`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `OFF`, Satuan `Days`
  - DU-083-50: Category: Name `Peralatan Studio {runId}`, Allow Borrow `Allow`
  - DU-083-51: Aset tersedia: Asset Name `Softbox Godox 60 cm {runId}`, Group `Head Office {runId}`, Category `Peralatan Studio {runId}`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `OFF`, Satuan `Days`
  - DU-083-52: Draft tersimpan: Pembuat `Agus Pratama {runId}`, Borrower `Dewi Lestari {runId}`, Aset `Head Office: Softbox Godox 60 cm {runId}`, Duration `2`, Purpose `Pemotretan katalog`
  - DU-083-53: Draft tersimpan: Pembuat `Hendra Kusuma {runId}`, Borrower `Dewi Lestari {runId}`, Aset `(tanpa aset)`, Group `—`
- Kondisi:
  - T0 adalah waktu permintaan dikirim.
  - Sesudah disimpan, Allow Borrow `Scanner Fujitsu fi-8170 {runId}` bernilai Deny pada override aset, `Kursi Lipat Chitose {runId}` berstatus Lifecycle Disposed, dan `Papan Info Akrilik {runId}` sudah dihapus.
  - Block new borrow when overdue bernilai `ON` pada aset di Draft `Bagus Santoso {runId}`.
  - Akun Agus, Hendra, Putri, Siti, Wulan, Nina, Oscar, Joko, dan Yuli aktif dan kredensialnya tersedia untuk fase 2.
  - Sesudah disimpan, Allow Borrow Category `Peralatan Studio {runId}` bernilai Deny.

## Test Steps

### Save Draft memerlukan Borrower dan tidak mengunci aset
1. Agus mengirim Save Draft tanpa Borrower atas `Dispenser Sanken HWD-77 {runId}`
2. Verifikasi Save Draft ditolak dengan pesan `You must pick a borrower`
3. Agus mengirim Save Draft dengan Borrower `Dewi Lestari {runId}` atas `Dispenser Sanken HWD-77 {runId}` dengan Duration dan Purpose dikosongkan
4. Verifikasi pengajuan tersimpan sebagai Draft, yaitu pengajuan yang disimpan tetapi belum di-Submit
5. Verifikasi Draft tersimpan walau Duration dan Purpose kosong
6. Verifikasi Draft hanya memuat satu Borrower, yaitu `Dewi Lestari {runId}`
7. Verifikasi Draft belum punya nomor BRW dan belum punya snapshot aturan efektif
8. Verifikasi Custody `Dispenser Sanken HWD-77 {runId}` tetap `Available`, karena Draft tidak mengunci aset
9. Verifikasi tidak ada fitur Prelist: pengajuan yang disimpan hanya berbentuk Draft

### Add to Borrow Draft ke Draft yang sudah ada bersifat idempoten
10. Agus mengirim Add to Borrow Draft atas `Kabel HDMI Ugreen 5 m {runId}` dan `Webcam Logitech C920 {runId}` ke Draft `Dewi Lestari {runId}` yang sudah memuat `Kabel HDMI Ugreen 5 m {runId}`
11. Verifikasi aset yang sudah ada dilewati: Draft tetap memuat tepat satu baris `Kabel HDMI Ugreen 5 m {runId}`
12. Verifikasi aset baru `Webcam Logitech C920 {runId}` masuk dengan Duration dan Purpose kosong
13. Verifikasi Draft lain milik `Dewi Lestari {runId}` tidak berubah

### Draft tanpa aset hanya terlihat dan dapat diubah pembuatnya
14. Wulan membuka tab Drafts
15. Verifikasi Draft tanpa aset buatan `Agus Pratama {runId}` tidak terlihat oleh `Wulan Sari {runId}`
16. Wulan mengirim Edit atas Draft tanpa aset buatan `Agus Pratama {runId}`
17. Verifikasi Edit ditolak karena Draft tanpa aset hanya dapat di-Edit pembuatnya
18. Wulan mengirim Delete atas Draft tanpa aset buatan `Agus Pratama {runId}`
19. Verifikasi Delete ditolak karena Draft tanpa aset hanya dapat di-Delete pembuatnya
20. Agus membuka tab Drafts
21. Verifikasi Draft tanpa aset terlihat oleh pembuatnya `Agus Pratama {runId}` selama ia Aktor Borrow
22. Verifikasi kolom Group Draft tanpa aset bernilai `—`
23. Agus mengubah Note Draft tanpa aset menjadi `Draft persiapan acara`
24. Verifikasi perubahan Note oleh pembuat diterima

### Draft tidak terlihat oleh Monitoring & Report dan Read Only
25. Nina dan Oscar membuka tab Drafts
26. Verifikasi Draft yang memuat aset Group `Head Office {runId}` tidak terlihat oleh `Nina Rahma {runId}` (Monitoring & Report) maupun `Oscar Wijaya {runId}` (Read Only)

### Cakupan Group menentukan siapa melihat, mengubah, Submit, dan Delete Draft multi-Group
27. Agus dan Hendra membuka tab Drafts
28. Verifikasi Draft `Dewi Lestari {runId}` yang memuat aset `Head Office {runId}` dan `Branch Surabaya {runId}` terlihat oleh `Agus Pratama {runId}` dan `Hendra Kusuma {runId}`, bukan hanya oleh pembuatnya `Wulan Sari {runId}`
29. Agus mengubah Duration `2` dan Purpose `Presentasi vendor` baris `Monitor Dell P2422H {runId}`
30. Verifikasi perubahan baris `Monitor Dell P2422H {runId}` yang dalam cakupan Agus tersimpan
31. Agus mengubah Purpose baris `Kamera Sony ZV-E10 {runId}` yang di luar cakupannya
32. Verifikasi perubahan baris di luar cakupan ditolak dan baris itu hanya terbaca nama aset `Kamera Sony ZV-E10 {runId}` dan Group `Branch Surabaya {runId}`
33. Agus mengirim Submit atas Draft itu
34. Verifikasi Submit ditolak karena sebagian aset di luar cakupan Group Agus, dan tidak ada BRW yang dibuat
35. Agus mengirim Delete atas Draft itu
36. Verifikasi Delete ditolak karena sebagian aset di luar cakupan Group Agus, dan Draft tetap ada
37. Agus mengirim Bulk Delete atas Draft `Dewi Lestari {runId}` multi-Group dan Draft tanpa aset buatannya
38. Verifikasi Draft multi-Group yang tidak memenuhi syarat dilewati dan tetap ada
39. Verifikasi Draft tanpa aset buatan `Agus Pratama {runId}` ikut terhapus karena memenuhi syarat bagi pembuatnya
40. Putri mengubah Purpose baris `Kamera Sony ZV-E10 {runId}` pada Draft multi-Group
41. Verifikasi Edit oleh Aktor yang cakupannya meliputi minimal satu Group di Draft diterima untuk barisnya sendiri
42. Putri mengirim Delete atas Draft multi-Group
43. Verifikasi Delete oleh Aktor yang cakupannya tidak meliputi semua Group di Draft ditolak
44. Wulan mengirim Delete atas Draft multi-Group
45. Verifikasi Delete oleh Aktor yang cakupannya meliputi semua Group di Draft diterima dan Draft terhapus

### Perubahan bersamaan atas Draft dijaga versi
46. Agus dan Siti membuka Draft `Dewi Lestari {runId}` yang memuat `Laptop Asus ExpertBook B1 {runId}` dan `Mouse Logitech MX Master 3 {runId}`
47. Agus menyimpan Purpose `Dukungan pelatihan` pada baris `Laptop Asus ExpertBook B1 {runId}`
48. Verifikasi penyimpan pertama berhasil
49. Siti menyimpan Purpose `Sewa untuk audit internal` pada baris `Mouse Logitech MX Master 3 {runId}` dari versi Draft yang ia buka sebelum penyimpanan Agus
50. Verifikasi penyimpan kedua ditolak karena versi Draft sudah berubah dan mendapat `D-BRW-13`
51. Verifikasi perubahan Agus tidak tertimpa: Purpose baris `Laptop Asus ExpertBook B1 {runId}` tetap `Dukungan pelatihan`, bukan last-write-wins
52. Verifikasi sesudah Reload, Draft memuat Purpose `Dukungan pelatihan` dari Agus sehingga penyimpan kedua melanjutkan dari versi terbaru
53. Siti mengulang penyimpanan Purpose `Sewa untuk audit internal` pada baris `Mouse Logitech MX Master 3 {runId}` setelah memuat ulang
54. Verifikasi penyimpanan Siti setelah memuat ulang diterima
55. Verifikasi Transaction admin log mencatat pembuat `Agus Pratama {runId}` dan pengubah `Siti Aminah {runId}`
56. Verifikasi Draft tampil dengan Modified By `Siti Aminah {runId}` dan Last Updated sama dengan waktu perubahan terakhir

### Satu aset di beberapa Draft dan kelayakan dievaluasi ulang saat Submit
57. Agus membuka tab Drafts
58. Verifikasi `Genset Honda EU22i {runId}` berada di dua Draft sekaligus, milik `Dewi Lestari {runId}` dan milik `Hana Permata {runId}`
59. Agus mengirim Submit atas Draft `Dewi Lestari {runId}` yang memuat `Genset Honda EU22i {runId}` dan dibuat `Siti Aminah {runId}`
60. Verifikasi Submit diterima dan pengaju yang tercatat di Requested By adalah `Agus Pratama {runId}`, bukan pembuat Draft `Siti Aminah {runId}`
61. Siti mengirim Submit atas Draft `Hana Permata {runId}` yang memuat `Genset Honda EU22i {runId}`
62. Verifikasi Submit ditolak dengan alasan `This asset is already in another transaction.` karena kelayakan dievaluasi ulang saat Submit
63. Verifikasi Draft `Hana Permata {runId}` tetap tersimpan

### Baris Draft yang tidak layak ditandai, bukan dihapus diam-diam
64. Agus membuka Draft `Dewi Lestari {runId}` yang memuat `Scanner Fujitsu fi-8170 {runId}` setelah Allow Borrow aset itu menjadi Deny
65. Verifikasi baris `Scanner Fujitsu fi-8170 {runId}` ditandai dengan `This asset can no longer be borrowed.` dan `Remove from List`
66. Agus mengirim Submit atas Draft yang memuat `Scanner Fujitsu fi-8170 {runId}`
67. Verifikasi Submit diblokir sampai baris dikeluarkan dan tidak ada BRW yang dibuat
68. Verifikasi Draft tetap tersimpan
69. Agus membuka Draft `Dewi Lestari {runId}` yang memuat `Kursi Lipat Chitose {runId}` dan `Papan Info Akrilik {runId}`
70. Verifikasi baris `Kursi Lipat Chitose {runId}` yang Disposed ditandai `This asset can no longer be borrowed.` dengan alasan `This asset is Disposed and can't be borrowed.`
71. Verifikasi baris `Kursi Lipat Chitose {runId}` menyediakan `Remove from List`
72. Verifikasi baris aset Deleted `Papan Info Akrilik {runId}` tetap ada di Draft dengan alasan `This asset has been deleted.`, tidak dihapus diam-diam
73. Agus mengirim Submit atas Draft yang memuat `Kursi Lipat Chitose {runId}` dan `Papan Info Akrilik {runId}`
74. Verifikasi Submit diblokir dan tidak ada BRW yang dibuat
75. Agus menutup Draft yang memuat `Kursi Lipat Chitose {runId}`
76. Agus membuka kembali Draft yang memuat `Kursi Lipat Chitose {runId}`
77. Verifikasi tanda tidak layak pada baris `Kursi Lipat Chitose {runId}` dievaluasi dan tampil lagi pada pembukaan berikutnya

### Draft dengan Borrower yang diblokir tetap dapat diedit
78. Agus membuka Draft `Bagus Santoso {runId}` yang memuat `Lensa Sigma 24-70 {runId}`
79. Verifikasi Borrower ditandai dengan pesan yang memuat nama `Bagus Santoso {runId}`, kode aset `AST-0412 {runId}`, dan Due date baris Overdue, diakhiri `Return it first.`
80. Agus mengubah Purpose Draft `Bagus Santoso {runId}` menjadi `Liputan acara tahunan`
81. Verifikasi Draft tetap dapat diedit walau Borrower diblokir
82. Agus mengirim Submit atas Draft `Bagus Santoso {runId}`
83. Verifikasi Submit diblokir dan tidak ada BRW yang dibuat
84. Agus membuka Draft `Dewi Lestari {runId}` yang memuat `Mikrofon Shure SM58 {runId}`
85. Verifikasi baris `Mikrofon Shure SM58 {runId}` ditandai dengan alasan `Dewi Lestari {runId} can't borrow assets from Head Office {runId}.`
86. Agus mengirim Submit atas Draft yang memuat `Mikrofon Shure SM58 {runId}`
87. Verifikasi Submit diblokir karena Allowed borrower tidak terpenuhi

### Cakupan Group Aktor dicabut saat Draft terbuka
88. Hendra membuka Draft `Dewi Lestari {runId}` yang memuat `Bor Listrik Bosch GSB 13 {runId}` dan `Mesin Bor Pasir Makita {runId}`
89. Cakupan `Branch Surabaya {runId}` milik `Hendra Kusuma {runId}` dicabut saat Draft masih terbuka
90. Hendra menyimpan Purpose `Survei lokasi pabrik` pada baris `Bor Listrik Bosch GSB 13 {runId}` dan baris `Mesin Bor Pasir Makita {runId}` dalam satu penyimpanan
91. Verifikasi penyimpanan baris `Mesin Bor Pasir Makita {runId}` yang di luar cakupan ditolak server
92. Verifikasi perubahan baris `Bor Listrik Bosch GSB 13 {runId}` yang masih dalam cakupan tetap tersimpan

### Pembuat Draft dinonaktifkan atau kehilangan peran Aktor Borrow
93. `Joko Santoso {runId}` dinonaktifkan
94. Verifikasi Draft berisi aset buatan `Joko Santoso {runId}` tetap ada
95. Agus melanjutkan Draft buatan `Joko Santoso {runId}` dengan mengubah Purpose baris `Handycam Sony FDR-AX43 {runId}`
96. Verifikasi Draft berisi aset itu dapat dilanjutkan Aktor lain dalam cakupan
97. Verifikasi Draft tanpa aset buatan `Joko Santoso {runId}` ikut dihapus tanpa status akhir
98. Verifikasi Draft yang terhapus itu tidak memiliki status `Canceled`, karena Draft tidak memiliki status akhir
99. `Yuli Astuti {runId}` kehilangan peran Aktor Borrow
100. Verifikasi Draft tanpa aset buatan `Yuli Astuti {runId}` ikut dihapus tanpa status akhir
101. Verifikasi Draft berisi aset buatan `Yuli Astuti {runId}` tetap ada dan dapat dilanjutkan Aktor lain dalam cakupan

### Borrower di Draft kehilangan PIC atau dinonaktifkan sebelum Submit
102. PIC `Gita Anggraini {runId}` dikosongkan di Users sebelum Submit
103. Agus mengirim Submit atas Draft `Gita Anggraini {runId}` yang memuat `Printer Epson L3250 {runId}`
104. Verifikasi Submit diblokir dengan pesan `Gita Anggraini {runId} has no login account and no PIC. Set a PIC in Users first.`
105. Verifikasi Draft `Gita Anggraini {runId}` tetap tersimpan
106. `Fajar Nugroho {runId}` dinonaktifkan
107. Agus mengirim Submit atas Draft `Fajar Nugroho {runId}` yang memuat `Proyektor Epson EB-X49 {runId}`
108. Verifikasi Submit gagal dengan pesan `Fajar Nugroho {runId} is no longer active. Pick another borrower.` pada field Borrower
109. Verifikasi baris aset `Proyektor Epson EB-X49 {runId}` tidak berubah dan Draft tetap tersimpan

### Draft hasil restore tidak punya timeout dan dapat difilter menurut Origin
110. Agus menyaring tab Drafts dengan Origin `Restored by system`
111. Verifikasi Draft yang memuat `Lampu Studio Godox SL60 {runId}` tampil, sedangkan Draft dengan Origin `Restored` dan `New` tidak tampil
112. Agus menyaring tab Drafts dengan Origin `Restored`
113. Verifikasi Draft yang memuat `Mixer Yamaha MG10 {runId}` tampil, sedangkan Draft dengan Origin `Restored by system` dan `New` tidak tampil
114. Agus menyaring tab Drafts dengan Origin `New`
115. Verifikasi Draft yang memuat `Tablet Samsung Galaxy Tab S9 {runId}` tampil, sedangkan Draft dengan Origin `Restored by system` dan `Restored` tidak tampil
116. Job Transaction timeout berjalan
117. Verifikasi ketiga Draft tetap ada karena Draft tidak memiliki Transaction timeout dan tidak pernah dihapus otomatis
118. Agus mengirim Bulk Delete atas ketiga Draft
119. Verifikasi ketiga Draft terhapus lewat Delete manual

### Aktor hanya dapat menambah dan mengeluarkan baris aset dalam cakupannya
120. Agus menambahkan `Bor Tangan Hitachi DV16V {runId}` yang berada di Group `Branch Surabaya {runId}` ke Draft yang memuat `Gerinda Tangan Bosch GWS 060 {runId}` dan `Kompresor Udara Ingco {runId}`
121. Verifikasi penambahan baris aset di luar cakupan ditolak dan Draft tidak memuat `Bor Tangan Hitachi DV16V {runId}`
122. Agus mengeluarkan baris `Kompresor Udara Ingco {runId}` yang di luar cakupannya dari Draft itu
123. Verifikasi pengeluaran baris di luar cakupan ditolak dan baris `Kompresor Udara Ingco {runId}` tetap ada di Draft
124. Agus mengeluarkan baris `Gerinda Tangan Bosch GWS 060 {runId}` yang dalam cakupannya dari Draft itu
125. Verifikasi pengeluaran baris dalam cakupan diterima: Draft tidak lagi memuat `Gerinda Tangan Bosch GWS 060 {runId}` dan tetap memuat `Kompresor Udara Ingco {runId}`

### Baris Draft ditandai tidak layak bila Allow Borrow Category diubah menjadi Deny
126. Agus membuka Draft `Dewi Lestari {runId}` yang memuat `Softbox Godox 60 cm {runId}` setelah Allow Borrow Category `Peralatan Studio {runId}` menjadi Deny
127. Verifikasi baris `Softbox Godox 60 cm {runId}` ditandai dengan `This asset can no longer be borrowed.` dan `Remove from List`
128. Agus mengirim Submit atas Draft yang memuat `Softbox Godox 60 cm {runId}`
129. Verifikasi Submit diblokir sampai baris dikeluarkan dan tidak ada BRW yang dibuat
130. Verifikasi Draft tetap tersimpan

### Draft tanpa aset milik orang lain dilewati pada Bulk Delete
131. Agus mengirim Bulk Delete atas Draft tanpa aset buatan `Hendra Kusuma {runId}` dan Draft `Dewi Lestari {runId}` yang memuat `Kabel HDMI Ugreen 5 m {runId}`
132. Verifikasi Draft tanpa aset buatan `Hendra Kusuma {runId}` dilewati dan tetap ada, karena Draft tanpa aset hanya memenuhi syarat bagi pembuatnya dan Agus bukan pembuatnya
133. Verifikasi Draft `Dewi Lestari {runId}` yang memuat `Kabel HDMI Ugreen 5 m {runId}` dan seluruh asetnya dalam cakupan Group Agus terhapus

### Edit atas Draft berisi aset ditolak bagi Aktor yang cakupannya tidak meliputi satu Group pun di Draft
134. Putri mengubah Purpose baris `Laptop Asus ExpertBook B1 {runId}` menjadi `Perubahan oleh Putri` pada Draft `Dewi Lestari {runId}` yang memuat `Laptop Asus ExpertBook B1 {runId}` dan `Mouse Logitech MX Master 3 {runId}`
135. Verifikasi Edit ditolak karena cakupan Group Putri (`Branch Surabaya {runId}`) tidak meliputi satu Group pun di Draft yang sudah memuat aset, yang hanya memuat aset Group `Head Office {runId}`
136. Verifikasi Purpose baris `Laptop Asus ExpertBook B1 {runId}` tetap `Dukungan pelatihan`
