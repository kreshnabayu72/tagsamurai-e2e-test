---
id: TC-FA-BORROW-BE-084-authz-cakupan-dan-pemisahan-peran
title: "Server menolak aksi di luar cakupan Group, pemrosesan transaksi sendiri tanpa syarat, dan aksi tulis tanpa hak"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["BORROW-LOGIC-15a", "BORROW-LOGIC-15b", "BORROW-LOGIC-15c", "BORROW-LOGIC-15d", "BORROW-LOGIC-15e", "BORROW-LOGIC-15f", "BORROW-LOGIC-15g", "BORROW-LOGIC-15h", "BORROW-LOGIC-15i", "BORROW-LOGIC-18a", "BORROW-LOGIC-18b", "BORROW-LOGIC-18c", "BORROW-LOGIC-18d", "BORROW-LOGIC-18e", "BORROW-LOGIC-18f", "BORROW-LOGIC-18g", "BORROW-LOGIC-18h", "BORROW-LOGIC-18i", "BORROW-LOGIC-18j", "BORROW-LOGIC-18k", "BORROW-LOGIC-18l", "BORROW-LOGIC-18m", "BORROW-LOGIC-18n", "FI-BRW-119", "FI-BRW-120", "FI-BRW-121", "FI-BRW-122", "§2.2#r1", "§2.2#p1", "§9.3#b1", "§9.3#b3", "§9.4.3#b5", "EB-AKS-3@submit-borrow", "EB-AKS-3@approve-reject", "EB-AKS-3@handover", "EB-AKS-3@return", "EB-AKS-3@extend", "EB-AKS-3@cancel-borrow", "EB-AKS-3@delete-draft"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-15a": [2, 3]
  "BORROW-LOGIC-15b": [5, 7, 9, 15, 17]
  "BORROW-LOGIC-15c": [35, 38]
  "BORROW-LOGIC-15d": [36]
  "BORROW-LOGIC-15e": [56, 58]
  "BORROW-LOGIC-15f": [60, 70]
  "BORROW-LOGIC-15g": [62, 64, 66]
  "BORROW-LOGIC-15h": [74, 83]
  "BORROW-LOGIC-15i": [40, 42, 44, 46, 48, 50, 52, 54]
  "BORROW-LOGIC-18a": [74, 83, 87]
  "BORROW-LOGIC-18b": [89, 91]
  "BORROW-LOGIC-18c": [70, 74, 79]
  "BORROW-LOGIC-18d": [72, 81]
  "BORROW-LOGIC-18e": [70]
  "BORROW-LOGIC-18f": [75]
  "BORROW-LOGIC-18g": [77, 84, 85]
  "BORROW-LOGIC-18h": [93]
  "BORROW-LOGIC-18i": [94, 96]
  "BORROW-LOGIC-18j": [98]
  "BORROW-LOGIC-18k": [99]
  "BORROW-LOGIC-18l": [101]
  "BORROW-LOGIC-18m": [5, 70, 79]
  "BORROW-LOGIC-18n": [76]
  "FI-BRW-119": [7]
  "FI-BRW-120": [8]
  "FI-BRW-121": [72, 81, 83, 91]
  "FI-BRW-122": [77, 84, 85]
  "§2.2#r1": [2]
  "§2.2#p1": [11, 13, 15]
  "§9.3#b1": [31, 33]
  "§9.3#b3": [62, 64, 68]
  "§9.4.3#b5": [62, 64, 66]
  "EB-AKS-3@submit-borrow": [17]
  "EB-AKS-3@approve-reject": [19]
  "EB-AKS-3@handover": [21]
  "EB-AKS-3@return": [23]
  "EB-AKS-3@extend": [25]
  "EB-AKS-3@cancel-borrow": [27]
  "EB-AKS-3@delete-draft": [29]
---

# Server menolak aksi di luar cakupan Group, pemrosesan transaksi sendiri tanpa syarat, dan aksi tulis tanpa hak

## Prerequisites
- Aktor: `Agus Pratama {runId}` (Asset Admin, Group `Head Office {runId}`); `Hendra Kusuma {runId}` (Asset Admin, Group `Branch Surabaya {runId}`); `Sinta Maharani {runId}` (Asset Admin, Group `Head Office {runId}`, PIC `Tari Wulandari {runId}`); `Siti Aminah {runId}` (Group Manager); `Wulan Sari {runId}` (Total Control); `Bambang Hartono {runId}` dan `Candra Wijaya {runId}` (Approver); `Nina Rahma {runId}` (Monitoring & Report); `Oscar Wijaya {runId}` (Read Only); `Dewi Lestari {runId}` dan `Bagus Santoso {runId}` (Borrower ber-akun).
- Data:
  - DU-084-1: Group asal aset: Name `Head Office {runId}`
  - DU-084-2: Group di luar cakupan Hendra dan Agus: Name `Branch Surabaya {runId}`
  - DU-084-3: User akun login: Name `Agus Pratama {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin`, Group penugasan `Head Office {runId}`
  - DU-084-4: User akun login: Name `Hendra Kusuma {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin`, Group penugasan `Branch Surabaya {runId}`
  - DU-084-5: User akun login: Name `Sinta Maharani {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin`, Group penugasan `Head Office {runId}`
  - DU-084-6: User akun login: Name `Siti Aminah {runId}`, Status `Active`, Activation Status `Activated`, Role `Group Manager`, Group binaan `Head Office {runId}`
  - DU-084-7: User akun login: Name `Wulan Sari {runId}`, Status `Active`, Activation Status `Activated`, Role `Total Control`, Scope `Seluruh client`
  - DU-084-8: User akun login: Name `Bambang Hartono {runId}`, Status `Active`, Activation Status `Activated`, Role `Approver`, Group penugasan `Head Office {runId}`
  - DU-084-9: User akun login: Name `Candra Wijaya {runId}`, Status `Active`, Activation Status `Activated`, Role `Approver`, Group penugasan `Head Office {runId}`
  - DU-084-10: User akun login: Name `Nina Rahma {runId}`, Status `Active`, Activation Status `Activated`, Role `Monitoring & Report`, Group penugasan `Head Office {runId}`
  - DU-084-11: User akun login: Name `Oscar Wijaya {runId}`, Status `Active`, Activation Status `Activated`, Role `Read Only`, Scope `Seluruh client`
  - DU-084-12: User akun login: Name `Dewi Lestari {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-084-13: User akun login: Name `Bagus Santoso {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-084-14: Karyawan tanpa akun login: Name `Tari Wulandari {runId}`, Status `Active`, Division `Finance`, PIC `Sinta Maharani {runId}`
  - DU-084-15: Aset self-service di Head Office: Asset Name `Kamera Canon EOS 90D {runId}`, Group `Head Office {runId}`, Category `Camera`, TAG `Ber-tag`, Custody `Available`, Self service `ON`, Max duration `7`, Allowed borrower `Semua karyawan`, Nilai aset `Rp 18.000.000`, Tanggal pembelian `T0 - 400 hari`
  - DU-084-16: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Laptop Dell Latitude 5440 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Approval`, Pengaju `Agus Pratama {runId}`, Approver snapshot `Bambang Hartono {runId}`
  - DU-084-17: Pinjaman berjalan: Borrower `Bagus Santoso {runId}`, Aset `Proyektor Epson EB-X49 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Approval`, Pengaju `Siti Aminah {runId}`, Approver snapshot `Bambang Hartono {runId}`
  - DU-084-18: Pinjaman berjalan: Borrower `Wulan Sari {runId}`, Aset `Printer Epson L3250 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Approval`, Pengaju `Agus Pratama {runId}`, Approver snapshot `Bambang Hartono {runId}`
  - DU-084-19: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Server Dell PowerEdge R450 {runId} (approver Bambang Hartono {runId}) dan Switch Cisco Catalyst 9200 {runId} (approver Candra Wijaya {runId})`, Group `Head Office {runId}`, Status baris `Waiting for Approval`, Pengaju `Agus Pratama {runId}`
  - DU-084-20: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Tablet Samsung Galaxy Tab S9 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`
  - DU-084-21: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Lensa Canon RF 24-70 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`
  - DU-084-22: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Speaker JBL PartyBox 310 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Due date `T0 + 3 hari`
  - DU-084-23: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Monitor LG UltraFine 27 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Max extensions `2`
  - DU-084-24: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Handycam Sony FDR-AX43 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Due date `T0 + 3 hari`, Laporan kerusakan aktif `Waiting for Confirmation`
  - DU-084-25: Pinjaman berjalan: Borrower `Agus Pratama {runId}`, Aset `Pengeras Suara Yamaha {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`, Pengaju `Agus Pratama {runId}`
  - DU-084-26: Pinjaman berjalan: Borrower `Agus Pratama {runId}`, Aset `Mesin Bor Pasir Makita {runId}`, Group `Branch Surabaya {runId}`, Status baris `Waiting for Handover`, Pengaju `Hendra Kusuma {runId}`
  - DU-084-27: Pinjaman berjalan: Borrower `Tari Wulandari {runId}`, Aset `Mikrofon Shure SM58 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`, PIC `Sinta Maharani {runId}`
  - DU-084-28: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Gerinda Bosch GWS 060 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`, Due date `T0 + 3 hari`
  - DU-084-29: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Bor Listrik Bosch GSB 13 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`, Due date `T0 + 3 hari`
  - DU-084-30: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Tripod Manfrotto MT055 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`, Due date `T0 + 3 hari`, Max extensions `2`
  - DU-084-31: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Kamera DJI Osmo Pocket 3 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`, Due date `T0 + 3 hari`
  - DU-084-32: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Drone DJI Mavic 3 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`, Due date `T0 + 3 hari`
  - DU-084-33: Pinjaman berjalan: Borrower `Bagus Santoso {runId}`, Aset `Headset Logitech H390 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`, Due date `T0 + 3 hari`
  - DU-084-34: Aset butuh approval: Asset Name `Genset Honda EU22i {runId}`, Group `Head Office {runId}`, Category `Tools`, TAG `Ber-tag`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Bambang Hartono {runId}`, Max duration `7`
  - DU-084-35: Aset di Group lain: Asset Name `Gergaji Mesin Stihl MS 170 {runId}`, Group `Branch Surabaya {runId}`, Category `Tools`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`
- Kondisi:
  - T0 adalah waktu permintaan dikirim.
  - Aset pada pinjaman berjalan memakai aturan efektif yang mengizinkan pinjaman; aset `Kamera Canon EOS 90D {runId}` memenuhi Allowed borrower bagi `Dewi Lestari {runId}`.
  - Draft milik `Agus Pratama {runId}` yang memuat `Genset Honda EU22i {runId}` tersimpan.
  - Akun Agus, Hendra, Sinta, Siti, Wulan, Bambang, Candra, Nina, Oscar, dan Dewi aktif dan kredensialnya tersedia untuk fase 2.

## Test Steps

### Baca BRW dan Borrow Log dibatasi pada Group dalam cakupan role
1. Agus, Nina, Oscar, dan Hendra membuka daftar BRW atas aset Group `Head Office {runId}`
2. Verifikasi BRW, baris, Approval, dan Borrow Log atas aset `Head Office {runId}` terlihat oleh `Agus Pratama {runId}`, `Nina Rahma {runId}` (Monitoring & Report), dan `Oscar Wijaya {runId}` (Read Only) karena dalam cakupan Group aset
3. Verifikasi BRW dan Borrow Log yang sama tidak terlihat oleh `Hendra Kusuma {runId}` yang cakupannya hanya `Branch Surabaya {runId}`

### Aksi lintas Group ditolak server
4. Hendra mengirim Handover langsung ke server atas baris `Tablet Samsung Galaxy Tab S9 {runId}` di Group `Head Office {runId}`
5. Verifikasi Handover ditolak karena aksi lintas Group dan baris tetap `Waiting for Handover`
6. Hendra mengirim Return langsung ke server atas baris `Speaker JBL PartyBox 310 {runId}` di Group `Head Office {runId}`
7. Verifikasi Return ditolak karena `Hendra Kusuma {runId}` tidak punya cakupan Group asal aset
8. Verifikasi penolakan memuat pesan `Error, return this asset to Head Office {runId}.`
9. Verifikasi baris `Speaker JBL PartyBox 310 {runId}` tetap `Borrowed`

### Memilih aset ke form mengikuti cakupan pemilihan
10. Agus membuka dialog Select Asset pada form Borrow
11. Verifikasi `Gergaji Mesin Stihl MS 170 {runId}` di Group `Branch Surabaya {runId}` tidak dimuat sama sekali di daftar pilihan Agus
12. Agus memindai TAG `Gergaji Mesin Stihl MS 170 {runId}` pada form Borrow
13. Verifikasi pesan `This asset belongs to Branch Surabaya {runId}.` diberikan, aset tidak ditambahkan, dan identitas, foto, serta atribut aset tidak ditampilkan
14. Agus mengirim aset `Gergaji Mesin Stihl MS 170 {runId}` langsung ke server sebagai baris pengajuan
15. Verifikasi server menolak aset di luar cakupan pemilihan walau dikirim lewat jalur lain

### Server menolak aksi tulis tanpa capability walau UI dilewati
16. Oscar mengirim Submit langsung ke server dengan Borrower `Dewi Lestari {runId}` atas `Genset Honda EU22i {runId}`
17. Verifikasi Submit oleh Oscar ditolak dan tidak ada BRW yang dibuat
18. Nina mengirim Approve langsung ke server atas aset `Laptop Dell Latitude 5440 {runId}` pada pengajuan `Dewi Lestari {runId}`
19. Verifikasi Approve ditolak dan baris tetap `Waiting for Approval`
20. Oscar mengirim Handover langsung ke server atas baris `Lensa Canon RF 24-70 {runId}`
21. Verifikasi Handover ditolak dan baris tetap `Waiting for Handover`
22. Oscar mengirim Return langsung ke server atas baris `Monitor LG UltraFine 27 {runId}`
23. Verifikasi Return ditolak dan baris tetap `Borrowed`
24. Oscar mengirim Extend langsung ke server atas baris `Monitor LG UltraFine 27 {runId}`
25. Verifikasi Extend ditolak dan Due date baris tidak berubah
26. Nina mengirim Cancel Borrow langsung ke server atas baris `Lensa Canon RF 24-70 {runId}`
27. Verifikasi Cancel Borrow ditolak dan baris tetap `Waiting for Handover`
28. Oscar mengirim Delete langsung ke server atas Draft milik `Agus Pratama {runId}` yang memuat `Genset Honda EU22i {runId}`
29. Verifikasi Delete Draft ditolak dan Draft tetap ada

### Peran menentukan aksi yang diizinkan
30. Bambang mengirim Submit langsung ke server dengan Borrower `Dewi Lestari {runId}` atas `Genset Honda EU22i {runId}`
31. Verifikasi Submit ditolak karena Approver bukan Aktor Borrow dan tidak berhak Create, Draft, Handover, Return, atau Report Missing
32. Dewi mengirim Handover langsung ke server atas baris `Lensa Canon RF 24-70 {runId}` miliknya
33. Verifikasi Handover ditolak karena Borrower tidak berhak Handover, yang milik Aktor Borrow

### Pengecualian self-service: Borrower melihat dan meminjam aset di luar cakupan role
34. Dewi membuka daftar aset self-service
35. Verifikasi `Kamera Canon EOS 90D {runId}` yang ber-Self service `ON` dan memenuhi Allowed borrower terlihat oleh `Dewi Lestari {runId}` walau di luar cakupan role-nya
36. Verifikasi data aset yang terlihat Dewi terbatas pada kolom versi self-service, tanpa nilai aset `Rp 18.000.000` dan tanpa tanggal pembelian
37. Dewi mengirim Borrow Now atas `Kamera Canon EOS 90D {runId}` dengan scan TAG, Duration `2` Days, dan Purpose `Dokumentasi rapat`
38. Verifikasi Borrow Now atas aset di luar cakupan role Dewi diterima
39. Dewi mengirim Cancel Borrow langsung ke server atas baris `Kamera Canon EOS 90D {runId}` miliknya
40. Verifikasi Cancel Borrow ditolak karena aksi itu tidak termasuk aksi yang tersedia bagi pinjaman self-service
41. Dewi mengirim Handover langsung ke server atas baris `Kamera Canon EOS 90D {runId}` miliknya
42. Verifikasi Handover ditolak karena tidak termasuk aksi yang tersedia bagi pinjaman self-service
43. Dewi mengirim Return atas baris `Headset Logitech H390 {runId}` milik `Bagus Santoso {runId}`
44. Verifikasi Return atas pinjaman milik orang lain ditolak karena aksi self-service hanya atas pinjamannya sendiri
45. Dewi mengajukan Extend atas baris `Tripod Manfrotto MT055 {runId}` miliknya dengan Extend by `1` dan Reason `Dipakai sampai akhir pekan`
46. Verifikasi Extend atas pinjamannya sendiri diterima
47. Dewi mengirim Cancel Extension atas baris `Tripod Manfrotto MT055 {runId}` miliknya
48. Verifikasi Cancel Extension atas pinjamannya sendiri diterima
49. Dewi mengirim Report Damaged atas baris `Drone DJI Mavic 3 {runId}` miliknya dengan satu foto dan What happened `Baling-baling patah`
50. Verifikasi Report Damaged atas pinjamannya sendiri diterima
51. Dewi mengirim Cancel Damage Report atas laporan `Drone DJI Mavic 3 {runId}` yang ia ajukan
52. Verifikasi Cancel Damage Report atas laporannya sendiri diterima
53. Dewi mengirim Report Missing atas baris `Gerinda Bosch GWS 060 {runId}` miliknya dengan What happened `Gerinda hilang dari loker`
54. Verifikasi Report Missing atas pinjamannya sendiri diterima

### Return self-service di Group asal tanpa cek radius lokasi
55. Dewi menjalankan Return atas `Kamera DJI Osmo Pocket 3 {runId}` di Group asal `Head Office {runId}` dengan scan TAG
56. Verifikasi Return self-service di Group asal diterima tanpa pengecekan radius lokasi dan baris menjadi `Returned`
57. Dewi menjalankan Return atas `Bor Listrik Bosch GSB 13 {runId}` di Group `Branch Surabaya {runId}` dengan scan TAG
58. Verifikasi Return di Group yang bukan Group asal ditolak dengan pesan `Error, return this asset to Head Office {runId}.`

### Tombol disabled bukan satu-satunya penjaga
59. Dewi mengirim Extend langsung ke server atas baris `Handycam Sony FDR-AX43 {runId}` yang punya laporan kerusakan aktif
60. Verifikasi Extend ditolak walau tombolnya sudah Disabled, dan Due date baris tidak berubah

### Pengaju, Borrower, dan approver di luar snapshot tidak memutuskan aset
61. Siti mengirim Approve atas aset `Proyektor Epson EB-X49 {runId}` pada pengajuan yang ia ajukan sendiri untuk `Bagus Santoso {runId}`
62. Verifikasi Approve oleh pengaju ditolak dan baris tetap `Waiting for Approval`
63. Wulan mengirim Approve atas aset `Printer Epson L3250 {runId}` pada pengajuan dengan Borrower dirinya sendiri
64. Verifikasi Approve oleh Borrower ditolak dan baris tetap `Waiting for Approval`
65. Dewi mengirim Approve atas aset `Laptop Dell Latitude 5440 {runId}` pada pengajuan dengan Borrower dirinya sendiri
66. Verifikasi Approve oleh Borrower ditolak karena Borrower tidak pernah memutuskan aset atas transaksinya sendiri
67. Bambang mengirim Approve atas aset `Switch Cisco Catalyst 9200 {runId}` yang approver-nya `Candra Wijaya {runId}`
68. Verifikasi Approve atas aset yang bukan miliknya ditolak server dan baris tetap `Waiting for Approval`

### Aktor Borrow sebagai Borrower memproses Handover dan Return sendiri dengan syarat pemrosesan sendiri
69. Agus mengirim Handover atas `Pengeras Suara Yamaha {runId}` pinjamannya sendiri tanpa scan TAG
70. Verifikasi Handover tanpa scan TAG ditolak server, karena tanpa scan tidak ada bukti fisik
71. Agus mengirim Handover atas `Pengeras Suara Yamaha {runId}` pinjamannya sendiri dengan `I Can't Scan the TAG`
72. Verifikasi `I Can't Scan the TAG` tidak tersedia pada pemrosesan sendiri dan Handover ditolak
73. Agus mengirim Handover atas `Pengeras Suara Yamaha {runId}` pinjamannya sendiri dengan scan TAG
74. Verifikasi Handover diterima dan baris menjadi `Borrowed`, karena Aktor Borrow yang menjadi Borrower boleh menjadi pemberi atas pinjamannya sendiri
75. Verifikasi konfirmasi serah terima selesai otomatis saat Agus menyelesaikan Handover, tanpa sesi `D-BRW-19` dan tanpa `D-BRW-20`
76. Verifikasi konfirmasi serah terima yang selesai otomatis ditandai `Confirmed (self)`
77. Verifikasi node Handed over di Borrow Log memuat penanda `Self-processed`
78. Agus mengirim Return atas `Pengeras Suara Yamaha {runId}` pinjamannya sendiri tanpa scan TAG
79. Verifikasi Return tanpa scan TAG ditolak server
80. Agus mengirim Return atas `Pengeras Suara Yamaha {runId}` pinjamannya sendiri dengan `I Can't Scan the TAG`
81. Verifikasi `I Can't Scan the TAG` tidak tersedia pada Return yang diterima Aktor yang juga Borrower, dan Return ditolak
82. Agus mengirim Return atas `Pengeras Suara Yamaha {runId}` pinjamannya sendiri dengan scan TAG
83. Verifikasi Return diterima dan baris menjadi `Returned`, karena Aktor Borrow yang menjadi Borrower boleh menjadi penerima atas pinjamannya sendiri
84. Verifikasi node Returned di Borrow Log memuat penanda `Self-processed`
85. Verifikasi baris dengan penanda `Self-processed` dapat difilter auditor
86. Agus mengirim Handover atas `Mesin Bor Pasir Makita {runId}` pinjamannya sendiri di Group `Branch Surabaya {runId}` dengan scan TAG
87. Verifikasi Handover ditolak karena Group asal aset di luar cakupan Agus, dan baris tetap `Waiting for Handover`

### PIC yang adalah Aktor Borrow memproses Handover dan Return atas pinjaman karyawan yang diwakilinya
88. Sinta mengirim Handover atas `Mikrofon Shure SM58 {runId}` milik `Tari Wulandari {runId}` dengan scan TAG
89. Verifikasi Handover diterima dan baris menjadi `Borrowed`, karena Aktor Borrow yang menjadi PIC Borrower tanpa akun diperlakukan sama dengan Borrower
90. Sinta mengirim Return atas `Mikrofon Shure SM58 {runId}` milik `Tari Wulandari {runId}` dengan scan TAG
91. Verifikasi Return diterima dan baris menjadi `Returned`, karena PIC boleh menjadi penerima atas pinjaman karyawan yang diwakilinya

### Aktor Borrow mengajukan BRW untuk dirinya sendiri tunduk pada self-approval guard
92. Agus mengirim Submit dengan Borrower dirinya sendiri, `Agus Pratama {runId}`, atas `Genset Honda EU22i {runId}` dengan Duration `2` Days dan Purpose `Cadangan listrik rapat`
93. Verifikasi pengajuan atas nama `Agus Pratama {runId}` sendiri diterima
94. Verifikasi `Agus Pratama {runId}` tidak ada di daftar approver aset itu, sedangkan `Bambang Hartono {runId}` ada
95. Agus mengirim Approve atas aset `Genset Honda EU22i {runId}` pada pengajuannya sendiri
96. Verifikasi Approve oleh Agus ditolak karena approval tetap tunduk pada self-approval guard

### Return self-service oleh Borrower mengirim notifikasi Review tanpa menahan proses
97. Dewi menjalankan Return atas `Gerinda Bosch GWS 060 {runId}` dengan scan TAG
98. Verifikasi notifikasi `borrow_returned` varian Review dikirim ke Aktor Borrow Group asal `Head Office {runId}`, beserta pasangan foto handover dan return
99. Verifikasi baris menjadi `Returned` tanpa menunggu Review, karena Review tidak menahan proses
100. Agus membuat Damage Report atas `Gerinda Bosch GWS 060 {runId}` dari detail aset setelah menemukan kerusakan
101. Verifikasi Damage Report oleh Aktor Borrow atas aset itu diterima

