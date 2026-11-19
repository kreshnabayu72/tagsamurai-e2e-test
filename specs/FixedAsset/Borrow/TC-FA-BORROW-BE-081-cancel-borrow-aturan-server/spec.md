---
id: TC-FA-BORROW-BE-081-cancel-borrow-aturan-server
title: "Cancel Borrow per baris atau BRW, Cancel saat sesi Handover, dan hasil Save as Draft to edit"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["EC-BRW-148", "EC-BRW-149", "EC-BRW-150", "EC-BRW-151", "EC-BRW-152", "EC-BRW-69", "EC-BRW-72", "EC-BRW-92", "EC-BRW-93", "EC-BRW-94", "F-BORROW-10.k6", "F-BORROW-10.k7", "V-BRW-37"]
smoke: []
dependsOn: []
owner: BE
trace:
  "EC-BRW-148": [2, 3, 4, 5, 6, 7]
  "EC-BRW-149": [10, 12, 14, 15, 16, 63, 64]
  "EC-BRW-150": [19, 20, 21]
  "EC-BRW-151": [26, 31, 35, 71, 73, 77]
  "EC-BRW-152": [38, 39, 40]
  "EC-BRW-69": [24, 28, 31, 35, 71, 73, 77, 78, 81, 83, 87, 88, 90, 91]
  "EC-BRW-72": [42, 45]
  "EC-BRW-92": [48, 49, 50]
  "EC-BRW-93": [54, 56]
  "EC-BRW-94": [58, 59, 60]
  "F-BORROW-10.k6": [24, 31, 35, 71, 73, 77]
  "F-BORROW-10.k7": [10, 12, 14, 16, 19, 20, 21, 63, 64, 67, 68]
  "V-BRW-37": [24, 26]
---

# Cancel Borrow per baris atau BRW, Cancel saat sesi Handover, dan hasil Save as Draft to edit

## Prerequisites
- Aktor: Asset Admin `Agus Pratama {runId}` dengan Group penugasan `Head Office {runId}` (DU-081-1); Borrower `Rina Wijaya {runId}` (DU-081-2); Asset Admin kedua `Tika Rahma {runId}` (DU-081-3); Approver `Sari Dewi {runId}` (DU-081-4); Total Control `Dewi Lestari {runId}` (DU-081-5); Borrower lain `Joko Susilo {runId}` (DU-081-6); karyawan aktif tanpa akun login `Budi Santoso {runId}` dengan PIC `Agus Pratama {runId}` (DU-081-22); Borrower `Lukman Hakim {runId}` (DU-081-28).
- Data:
  - DU-081-1: Pengguna, Asset Admin Group asal: Name `Agus Pratama {runId}`, Role `Asset Admin`, Group penugasan `Head Office {runId}`.
  - DU-081-2: Pengguna, Borrower dengan akun login: Name `Rina Wijaya {runId}`, Role `Karyawan aktif dengan akun login`, Group `Head Office {runId}`.
  - DU-081-3: Pengguna, Asset Admin kedua: Name `Tika Rahma {runId}`, Role `Asset Admin`, Group penugasan `Head Office {runId}`.
  - DU-081-4: Pengguna, Approver aset: Name `Sari Dewi {runId}`, Role `Approver`, Group penugasan `Head Office {runId}`.
  - DU-081-5: Pengguna, Total Control yang tidak punya cakupan Group BRW itu: Name `Dewi Lestari {runId}`, Role `Total Control`, Cakupan Group untuk menyimpan Draft `tidak termasuk Head Office {runId}`.
  - DU-081-6: Pengguna, Borrower lain yang mengambil aset dalam transaksi lain: Name `Joko Susilo {runId}`, Role `Karyawan aktif dengan akun login`, Group `Head Office {runId}`.
  - DU-081-7: Baris Borrow, Baris Waiting for Approval yang dibatalkan Borrower: BRW `BRW 1 bersama DU-081-8 dan DU-081-9`, Borrower `Rina Wijaya {runId}`, Asset Name `Laptop Dell Latitude {runId}`, Category `Laptop`, Duration `3 Days`, Status baris `Waiting for Approval`.
  - DU-081-8: Baris Borrow, Baris Waiting for Handover yang dibatalkan Borrower: BRW `BRW 1 bersama DU-081-7 dan DU-081-9`, Borrower `Rina Wijaya {runId}`, Asset Name `Proyektor Epson {runId}`, Category `Proyektor`, Duration `3 Days`, Status baris `Waiting for Handover`.
  - DU-081-9: Baris Borrow, Baris lain BRW yang sama yang tidak dibatalkan: BRW `BRW 1 bersama DU-081-7 dan DU-081-8`, Borrower `Rina Wijaya {runId}`, Asset Name `Kursi Lipat Rapat {runId}`, Category `Furnitur`, Duration `3 Days`, Status baris `Waiting for Handover`.
  - DU-081-10: Baris Borrow, Baris Waiting for Handover yang dibatalkan Borrower lalu diaksi Asset Admin: BRW `BRW 2`, Borrower `Rina Wijaya {runId}`, Asset Name `Monitor Samsung {runId}`, Category `Monitor`, Duration `3 Days`, Status baris `Waiting for Handover`.
  - DU-081-11: Baris Borrow, Baris Waiting for Handover yang dibatalkan Asset Admin sebelum Borrower mengonfirmasi: BRW `BRW 3`, Borrower `Rina Wijaya {runId}`, Asset Name `Tripod Kamera {runId}`, Category `Aksesori Kamera`, Duration `3 Days`, Status baris `Waiting for Handover`.
  - DU-081-12: Baris Borrow, Baris Waiting for Handover dalam sesi Handover yang berakhir dengan Cancel Request: BRW `BRW 4`, Borrower `Rina Wijaya {runId}`, Asset Name `Speaker Portable JBL {runId}`, Category `Audio`, Duration `3 Days`, Status baris `Waiting for Handover`, TAG `sudah terverifikasi di Handover`.
  - DU-081-13: Baris Borrow, Baris Waiting for Handover dalam sesi Handover yang berakhir karena jendela habis: BRW `BRW 5`, Borrower `Rina Wijaya {runId}`, Asset Name `Mikrofon Wireless Shure {runId}`, Category `Audio`, Duration `3 Days`, Status baris `Waiting for Handover`, TAG `sudah terverifikasi di Handover`.
  - DU-081-14: Baris Borrow, Baris Waiting for Approval yang dibatalkan Borrower saat approver membuka Review: BRW `BRW 6`, Borrower `Rina Wijaya {runId}`, Asset Name `Walkie Talkie Motorola {runId}`, Category `Peralatan Komunikasi`, Duration `3 Days`, Status baris `Waiting for Approval`, Approver `Sari Dewi {runId}`.
  - DU-081-15: Baris Borrow, Baris Waiting for Handover yang akan dibatalkan per baris: BRW `BRW 7 bersama DU-081-16`, Borrower `Rina Wijaya {runId}`, Asset Name `Printer Warna Epson {runId}`, Category `Printer`, Duration `3 Days`, Status baris `Waiting for Handover`.
  - DU-081-16: Baris Borrow, Baris Returned yang tersisa dalam BRW: BRW `BRW 7 bersama DU-081-15`, Borrower `Rina Wijaya {runId}`, Asset Name `Mesin Bor Listrik {runId}`, Category `Peralatan Lapangan`, Duration `3 Days`, Status baris `Returned`.
  - DU-081-17: Baris Borrow, Baris Waiting for Handover pertama dari BRW yang semuanya akan dibatalkan: BRW `BRW 8 bersama DU-081-18`, Borrower `Rina Wijaya {runId}`, Asset Name `Server Rack Mini {runId}`, Category `Perangkat Jaringan`, Duration `3 Days`, Status baris `Waiting for Handover`.
  - DU-081-18: Baris Borrow, Baris Waiting for Handover kedua dari BRW yang semuanya akan dibatalkan: BRW `BRW 8 bersama DU-081-17`, Borrower `Rina Wijaya {runId}`, Asset Name `Router Cisco {runId}`, Category `Perangkat Jaringan`, Duration `3 Days`, Status baris `Waiting for Handover`.
  - DU-081-19: Baris Borrow, Baris Waiting for Approval yang dibatalkan dengan Save as Draft to edit saat approver membuka Review: BRW `BRW 9`, Borrower `Rina Wijaya {runId}`, Asset Name `Kamera Canon EOS {runId}`, Category `Kamera`, Duration `3 Days`, Status baris `Waiting for Approval`, Approver `Sari Dewi {runId}`, Purpose `Dokumentasi acara`, Note `Untuk acara kantor`.
  - DU-081-20: Baris Borrow, Baris Waiting for Approval yang dibatalkan dengan Save as Draft to edit lalu asetnya diambil transaksi lain: BRW `BRW 10`, Borrower `Rina Wijaya {runId}`, Asset Name `Lensa Sigma {runId}`, Category `Kamera`, Duration `3 Days`, Status baris `Waiting for Approval`, Purpose `Dokumentasi acara`, Note `Untuk acara kantor`.
  - DU-081-21: Baris Borrow, Baris Waiting for Approval yang dibatalkan Total Control tanpa cakupan Group BRW itu: BRW `BRW 11`, Borrower `Rina Wijaya {runId}`, Asset Name `Gimbal DJI {runId}`, Category `Kamera`, Duration `3 Days`, Status baris `Waiting for Approval`.
  - DU-081-22: Pengguna, Borrower tanpa akun login dengan PIC Asset Admin: Name `Budi Santoso {runId}`, Role `Karyawan aktif tanpa akun login`, PIC `Agus Pratama {runId}`.
  - DU-081-23: Baris Borrow, Baris Waiting for Handover milik Borrower tanpa akun yang dibatalkan PIC: BRW `BRW 12`, Borrower `Budi Santoso {runId}`, PIC `Agus Pratama {runId}`, Asset Name `Genset Portable {runId}`, Category `Peralatan Lapangan`, Duration `3 Days`, Status baris `Waiting for Handover`.
  - DU-081-24: Baris Borrow, Baris Waiting for Handover yang dibatalkan Aktor Borrow lalu diaksi Aktor Borrow lain: BRW `BRW 13`, Borrower `Rina Wijaya {runId}`, Asset Name `Tripod Mini {runId}`, Category `Aksesori Kamera`, Duration `3 Days`, Status baris `Waiting for Handover`.
  - DU-081-25: Baris Borrow, Baris Waiting for Handover ber-tag yang diterima dalam handover sebagian: BRW `BRW 14 bersama DU-081-26`, Borrower `Rina Wijaya {runId}`, Asset Name `Kabel Ekstensi A {runId}`, Category `Perkakas`, Duration `3 Days`, Status baris `Waiting for Handover`, Photo at start `OFF`.
  - DU-081-26: Baris Borrow, Baris Waiting for Handover ber-tag yang tidak diterima dalam handover sebagian lalu dibatalkan Borrower: BRW `BRW 14 bersama DU-081-25`, Borrower `Rina Wijaya {runId}`, Asset Name `Kabel Ekstensi B {runId}`, Category `Perkakas`, Duration `3 Days`, Status baris `Waiting for Handover`, Photo at start `OFF`.
  - DU-081-27: Baris Borrow, Baris Waiting for Handover ber-tag yang sesinya berakhir karena jendela habis lalu dibatalkan Borrower: BRW `BRW 15`, Borrower `Rina Wijaya {runId}`, Asset Name `Kabel Ekstensi C {runId}`, Category `Perkakas`, Duration `3 Days`, Status baris `Waiting for Handover`, Photo at start `OFF`.
  - DU-081-28: Pengguna, Borrower dengan akun login yang dinonaktifkan selama sesi Handover: Name `Lukman Hakim {runId}`, Role `Karyawan aktif dengan akun login`, Group `Head Office {runId}`.
  - DU-081-29: Baris Borrow, Baris Waiting for Handover ber-tag yang Borrower-nya dinonaktifkan selama sesi Handover: BRW `BRW 16`, Borrower `Lukman Hakim {runId}`, Asset Name `Scanner Canon {runId}`, Category `Scanner`, Duration `3 Days`, Status baris `Waiting for Handover`, Photo at start `OFF`, TAG `QR ter-pair`.
  - DU-081-30: Baris Borrow, Baris Waiting for Handover ber-tag yang asetnya dikunci dan dipindah Group selama sesi Handover: BRW `BRW 17`, Borrower `Rina Wijaya {runId}`, Asset Name `Mixer Audio Behringer {runId}`, Category `Audio`, Duration `3 Days`, Status baris `Waiting for Handover`, Photo at start `OFF`, TAG `QR ter-pair`, Group aset `Head Office {runId}`, Group tujuan pindah `Branch Surabaya {runId}`, Activity Lock aset `belum ada`.
- Kondisi:
  - Level Feature Suite Borrowing bernilai `Full`.
  - Dialog `Save as Draft to edit` hanya tersedia untuk Asset Admin, Group Manager, dan Total Control dan hanya bila BRW belum punya baris `Borrowed` atau `Overdue`.

## Test Steps

### Borrower membatalkan baris Waiting for Approval atau Waiting for Handover
1. Borrower membatalkan baris `Laptop Dell Latitude {runId}` yang `Waiting for Approval` dan baris `Proyektor Epson {runId}` yang `Waiting for Handover` pada BRW 1
2. Verifikasi baris dibatalkan menjadi `Canceled` dengan node `Canceled by [Borrower]` tanpa Reason
3. Verifikasi Custody aset kembali `Available`
4. Verifikasi baris yang dibatalkan pindah ke tab History Borrower
5. Verifikasi baris lain BRW 1 yaitu `Kursi Lipat Rapat {runId}` tidak berubah
6. Verifikasi toast `Success, borrow has been canceled.` dikembalikan
7. Verifikasi Aktor Borrow Group asal menerima `borrow_canceled` varian Aktor Borrow

### Aksi Aktor Borrow pada baris yang sudah dibatalkan Borrower atau Aktor Borrow lain
8. Borrower membatalkan baris `Monitor Samsung {runId}` yang `Waiting for Handover`
9. Asset Admin `Agus Pratama {runId}` mengirim Cancel Borrow atas baris `Monitor Samsung {runId}`
10. Verifikasi server menolak Cancel Borrow itu dan Aktor Borrow melihat dialog `D-BRW-22` `Borrow Already Canceled`
11. Asset Admin `Agus Pratama {runId}` mengirim Hand Over atas baris `Monitor Samsung {runId}`
12. Verifikasi server menolak Hand Over itu dengan dialog `D-BRW-22`
13. Asset Admin `Agus Pratama {runId}` mengirim Remind Borrower atas baris `Monitor Samsung {runId}`
14. Verifikasi server menolak Remind Borrower itu dengan dialog `D-BRW-22`
15. Verifikasi `[OK]` pada dialog memuat ulang tabel dan baris tampil `Canceled` di tab History
16. Verifikasi baris `Monitor Samsung {runId}` tidak berubah oleh ketiga percobaan itu
17. Asset Admin `Agus Pratama {runId}` membatalkan baris `Tripod Kamera {runId}` yang `Waiting for Handover`
18. Borrower mengonfirmasi dialog `D-BRW-01` untuk membatalkan baris `Tripod Kamera {runId}` setelah Asset Admin membatalkannya
19. Verifikasi server menolak pembatalan Borrower itu
20. Verifikasi Borrower melihat dialog `Borrow Already Canceled` (`D-MYA-03`)
21. Verifikasi baris `Tripod Kamera {runId}` tidak berubah oleh percobaan Borrower itu

### Cancel saat sesi Handover berjalan ditolak dan dapat diulang sesudahnya
22. Asset Admin `Agus Pratama {runId}` mengirim Request Confirmation untuk baris `Speaker Portable JBL {runId}`
23. Asset Admin `Tika Rahma {runId}` mengirim Cancel Borrow atas baris `Speaker Portable JBL {runId}` selama sesi Handover berjalan
24. Verifikasi Cancel ditolak dengan Dialog Blok `[OK]` berisi `Handover is in progress for this asset.`
25. Borrower membatalkan baris `Speaker Portable JBL {runId}` selama sesi Handover berjalan
26. Verifikasi pembatalan Borrower ditolak dengan `Handover is in progress for this asset.`
27. Aset `Speaker Portable JBL {runId}` dijadikan Unmanaged selama sesi Handover berjalan
28. Verifikasi operasi sistem atas baris di dalam sesi ditunda sampai sesi selesai, dibatalkan, atau jendela habis
29. Asset Admin `Agus Pratama {runId}` menekan `Cancel Request` pada `D-BRW-19`
30. Borrower membatalkan baris `Speaker Portable JBL {runId}` yang masih `Waiting for Handover`
31. Verifikasi Cancel dapat diulang sesudah `Cancel Request` dan baris menjadi `Canceled`
32. Asset Admin `Agus Pratama {runId}` mengirim Request Confirmation untuk baris `Mikrofon Wireless Shure {runId}`
33. Waktu berlalu 15 menit sejak permintaan konfirmasi `Mikrofon Wireless Shure {runId}` dikirim
34. Asset Admin `Tika Rahma {runId}` mengirim Cancel Borrow atas baris `Mikrofon Wireless Shure {runId}` yang masih `Waiting for Handover`
35. Verifikasi Cancel dapat diulang sesudah jendela konfirmasi habis dan baris menjadi `Canceled`

### Approver membuka Review saat pengajuan dibatalkan Borrower
36. Approver `Sari Dewi {runId}` membuka Review pengajuan baris `Walkie Talkie Motorola {runId}`
37. Borrower membatalkan baris `Walkie Talkie Motorola {runId}` yang `Waiting for Approval`
38. Verifikasi approver melihat `D-BRW-09` varian `Borrow Canceled` dengan teks `This borrow was canceled by [Name].`
39. Verifikasi keputusan approver atas Review baris `Walkie Talkie Motorola {runId}` yang belum dikirim dibuang
40. Verifikasi approver item approval yang belum bertindak menerima `borrow_canceled` untuk baris `Waiting for Approval`

### Cancel baris terakhir per baris menghitung ulang status header
41. Asset Admin `Agus Pratama {runId}` membatalkan baris `Printer Warna Epson {runId}` per baris pada BRW 7 yang tersisa baris `Returned`
42. Verifikasi status header BRW 7 dihitung ulang menjadi `Returned` dan BRW pindah ke tab History
43. Asset Admin `Agus Pratama {runId}` membatalkan baris `Server Rack Mini {runId}` per baris pada BRW 8
44. Asset Admin `Agus Pratama {runId}` membatalkan baris `Router Cisco {runId}` per baris pada BRW 8
45. Verifikasi status header BRW 8 dihitung ulang menjadi `Canceled` saat semua baris `Canceled` dan BRW pindah ke tab History

### Cancel dengan Save as Draft to edit
46. Approver `Sari Dewi {runId}` membuka Review BRW 9 yang memuat `Kamera Canon EOS {runId}`
47. Asset Admin `Agus Pratama {runId}` membatalkan BRW 9 dengan `Save as Draft to edit` dicentang
48. Verifikasi approver melihat `D-BRW-09` varian `Borrow Canceled` saat BRW 9 dibatalkan
49. Verifikasi keputusan approver atas BRW 9 yang belum dikirim dibuang
50. Verifikasi Draft baru tidak masuk antrean Approvals sampai di-Submit ulang
51. Asset Admin `Agus Pratama {runId}` membatalkan BRW 10 dengan `Save as Draft to edit` dicentang
52. Borrower `Joko Susilo {runId}` meminjam aset `Lensa Sigma {runId}` lewat transaksi lain sebelum Draft di-Submit ulang
53. Asset Admin `Agus Pratama {runId}` membuka Draft hasil Cancel BRW 10
54. Verifikasi Draft tidak mengunci aset dan baris `Lensa Sigma {runId}` ditandai dengan copy umum `This asset can no longer be borrowed.`
55. Asset Admin `Agus Pratama {runId}` mengirim Submit atas Draft hasil Cancel BRW 10
56. Verifikasi Submit diblokir sampai baris `Lensa Sigma {runId}` dikeluarkan
57. Total Control `Dewi Lestari {runId}` yang tidak punya cakupan Group BRW 11 membatalkan BRW 11
58. Verifikasi Cancel tetap boleh sesuai hak Cancel
59. Verifikasi tidak ada Draft baru yang dibuat karena Aktor tidak punya cakupan Group BRW 11
60. Verifikasi checkbox `Save as Draft to edit` disabled dengan alasan `You don't manage [Group], so this borrow can't be saved as a draft.`

### Aktor Borrow mengirim aksi pada baris yang dibatalkan PIC atas nama Borrower tanpa akun
61. PIC `Agus Pratama {runId}` membatalkan baris `Genset Portable {runId}` atas nama Borrower `Budi Santoso {runId}`
62. Asset Admin `Tika Rahma {runId}` mengirim Cancel Borrow atas baris `Genset Portable {runId}`
63. Verifikasi server menolak Cancel Borrow itu dan Aktor Borrow melihat dialog `D-BRW-22` atas nama PIC: `[PIC] already canceled this borrow on behalf of [Borrower].`
64. Verifikasi baris `Genset Portable {runId}` tidak berubah oleh percobaan itu

### Aktor Borrow mengirim aksi pada baris yang dibatalkan Aktor Borrow lain
65. Asset Admin `Tika Rahma {runId}` membatalkan baris `Tripod Mini {runId}` yang `Waiting for Handover`
66. Asset Admin `Agus Pratama {runId}` mengirim Hand Over atas baris `Tripod Mini {runId}`
67. Verifikasi server menolak Hand Over itu dan Aktor Borrow melihat dialog `D-BRW-22` `Borrow Already Canceled`
68. Verifikasi baris `Tripod Mini {runId}` tidak berubah oleh percobaan itu

### Cancel Borrower dapat diulang sesudah sesi Handover sebagian selesai
69. Asset Admin `Agus Pratama {runId}` memverifikasi `Kabel Ekstensi A {runId}` dan `Kabel Ekstensi B {runId}` dengan scan tag dan mengirim Request Confirmation untuk keduanya
70. Borrower menekan Accept dengan menghapus centang `Kabel Ekstensi B {runId}`
71. Verifikasi `Kabel Ekstensi A {runId}` menjadi `Borrowed` dan `Kabel Ekstensi B {runId}` tetap `Waiting for Handover` dengan keterangan `Not received` karena sesi selesai
72. Borrower membatalkan baris `Kabel Ekstensi B {runId}` yang masih `Waiting for Handover`
73. Verifikasi Cancel dapat diulang sesudah sesi selesai dan baris `Kabel Ekstensi B {runId}` menjadi `Canceled`

### Cancel Borrower dapat diulang sesudah jendela konfirmasi habis
74. Asset Admin `Agus Pratama {runId}` memverifikasi `Kabel Ekstensi C {runId}` dengan scan tag dan mengirim Request Confirmation
75. Waktu berlalu 15 menit sejak permintaan konfirmasi `Kabel Ekstensi C {runId}` dikirim
76. Borrower membatalkan baris `Kabel Ekstensi C {runId}` yang masih `Waiting for Handover`
77. Verifikasi Cancel oleh Borrower dapat diulang sesudah jendela konfirmasi habis dan baris `Kabel Ekstensi C {runId}` menjadi `Canceled`

### Operasi Unmanaged yang ditunda dijalankan sesudah sesi berakhir
78. Verifikasi operasi Unmanaged atas `Speaker Portable JBL {runId}` yang ditunda selama sesi Handover dijalankan sesudah sesi dibatalkan: aset berstatus `Unmanaged`

### Penonaktifan Borrower ditunda selama sesi Handover dan diterapkan sesudah Cancel Request
79. Asset Admin `Agus Pratama {runId}` memverifikasi `Scanner Canon {runId}` dengan scan tag dan mengirim Request Confirmation
80. Borrower `Lukman Hakim {runId}` dinonaktifkan selama sesi Handover berjalan
81. Verifikasi baris `Scanner Canon {runId}` tetap `Waiting for Handover` selama sesi Handover berjalan karena penonaktifan Borrower ditunda
82. Asset Admin `Agus Pratama {runId}` menekan `Cancel Request` pada `D-BRW-19`
83. Verifikasi penonaktifan Borrower yang ditunda diterapkan sesudah sesi dibatalkan: baris `Scanner Canon {runId}` menjadi `Canceled`

### Aset dikunci dan pindah Group ditunda selama sesi Handover dan diterapkan sesudah Cancel Request
84. Asset Admin `Agus Pratama {runId}` memverifikasi `Mixer Audio Behringer {runId}` dengan scan tag dan mengirim Request Confirmation
85. Aset `Mixer Audio Behringer {runId}` dikunci dengan Activity Lock `Under Maintenance` selama sesi Handover berjalan
86. Aset `Mixer Audio Behringer {runId}` dipindahkan ke Group `Branch Surabaya {runId}` selama sesi Handover berjalan
87. Verifikasi baris `Mixer Audio Behringer {runId}` tetap `Waiting for Handover` selama sesi Handover berjalan dan Activity Lock `Under Maintenance` belum diterapkan pada asetnya
88. Verifikasi pindah Group belum diterapkan selama sesi Handover berjalan: aset `Mixer Audio Behringer {runId}` masih di Group `Head Office {runId}`
89. Asset Admin `Agus Pratama {runId}` menekan `Cancel Request` pada `D-BRW-19`
90. Verifikasi Activity Lock `Under Maintenance` yang ditunda diterapkan pada aset `Mixer Audio Behringer {runId}` sesudah sesi dibatalkan
91. Verifikasi pindah Group yang ditunda diterapkan sesudah sesi dibatalkan: aset `Mixer Audio Behringer {runId}` berada di Group `Branch Surabaya {runId}`
