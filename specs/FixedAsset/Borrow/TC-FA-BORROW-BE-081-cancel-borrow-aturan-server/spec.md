---
id: TC-FA-BORROW-BE-081-cancel-borrow-aturan-server
title: "Cancel Borrow per baris atau BRW, Cancel saat sesi Handover, dan hasil Save as Draft to edit"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["EC-BRW-148", "EC-BRW-149", "EC-BRW-150", "EC-BRW-151", "EC-BRW-152", "EC-BRW-69", "EC-BRW-72", "EC-BRW-92", "EC-BRW-93", "EC-BRW-94", "F-BORROW-10.k6", "F-BORROW-10.k7", "V-BRW-37"]
smoke: []
dependsOn: []
owner: BE
trace:
  "EC-BRW-148": [2, 3, 4, 5, 6, 7]
  "EC-BRW-149": [10, 12, 14, 15, 16]
  "EC-BRW-150": [19, 20, 21]
  "EC-BRW-151": [26, 31, 35]
  "EC-BRW-152": [38, 39, 40]
  "EC-BRW-69": [24, 28, 31, 35]
  "EC-BRW-72": [42, 45]
  "EC-BRW-92": [48, 49, 50]
  "EC-BRW-93": [54, 56]
  "EC-BRW-94": [58, 59, 60]
  "F-BORROW-10.k6": [24, 31, 35]
  "F-BORROW-10.k7": [10, 12, 14, 16, 19, 20, 21]
  "V-BRW-37": [24, 26]
---

# Cancel Borrow per baris atau BRW, Cancel saat sesi Handover, dan hasil Save as Draft to edit

## Prerequisites
- Aktor: Asset Admin `Agus Pratama {runId}` dengan Group penugasan `Head Office {runId}` (DU-081-1); Borrower `Rina Wijaya {runId}` (DU-081-2); Asset Admin kedua `Tika Rahma {runId}` (DU-081-3); Approver `Sari Dewi {runId}` (DU-081-4); Total Control `Dewi Lestari {runId}` (DU-081-5); Borrower lain `Joko Susilo {runId}` (DU-081-6).
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
