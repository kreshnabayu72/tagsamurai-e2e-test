---
id: TC-FA-BORROW-BE-090-mark-as-returned-level-none
title: "Mark as Returned pada level None: pelaku, pemisahan peran, bulk, dan hasil Returned, Missing, atau Damaged"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["BORROW-LOGIC-22aa", "BORROW-LOGIC-22b", "BORROW-LOGIC-22c", "BORROW-LOGIC-22d", "BORROW-LOGIC-22e", "BORROW-LOGIC-22f", "BORROW-LOGIC-22g", "BORROW-LOGIC-22h", "BORROW-LOGIC-22i", "BORROW-LOGIC-22j", "BORROW-LOGIC-22k", "BORROW-LOGIC-22l", "BORROW-LOGIC-22m", "BORROW-LOGIC-22n", "BORROW-LOGIC-22o", "BORROW-LOGIC-22p", "BORROW-LOGIC-22q", "BORROW-LOGIC-22r", "BORROW-LOGIC-22s", "BORROW-LOGIC-22t", "BORROW-LOGIC-22u", "BORROW-LOGIC-22v", "BORROW-LOGIC-22w", "BORROW-LOGIC-22x", "BORROW-LOGIC-22y", "BORROW-LOGIC-22z", "EC-BRW-170", "EC-BRW-171", "EC-BRW-172", "EC-BRW-173", "EC-BRW-175", "EC-BRW-178", "EC-BRW-179"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-22aa": [66, 67]
  "BORROW-LOGIC-22b": 12
  "BORROW-LOGIC-22c": [10, 15, 26]
  "BORROW-LOGIC-22d": 13
  "BORROW-LOGIC-22e": [24, 27, 31, 36]
  "BORROW-LOGIC-22f": 38
  "BORROW-LOGIC-22g": [50, 54]
  "BORROW-LOGIC-22h": [73, 75]
  "BORROW-LOGIC-22i": 39
  "BORROW-LOGIC-22j": 49
  "BORROW-LOGIC-22k": [65, 67]
  "BORROW-LOGIC-22l": [50, 54]
  "BORROW-LOGIC-22m": [17, 18]
  "BORROW-LOGIC-22n": 19
  "BORROW-LOGIC-22o": [29, 33]
  "BORROW-LOGIC-22p": 61
  "BORROW-LOGIC-22q": [64, 65, 70]
  "BORROW-LOGIC-22r": [62, 63]
  "BORROW-LOGIC-22s": 42
  "BORROW-LOGIC-22t": 44
  "BORROW-LOGIC-22u": [21, 22]
  "BORROW-LOGIC-22v": 20
  "BORROW-LOGIC-22w": 40
  "BORROW-LOGIC-22x": [52, 53]
  "BORROW-LOGIC-22y": 58
  "BORROW-LOGIC-22z": [30, 34]
  "EC-BRW-170": [19, 21, 22, 23, 26]
  "EC-BRW-171": [29, 30, 33, 34]
  "EC-BRW-172": [63, 64, 66, 71]
  "EC-BRW-173": [38, 42]
  "EC-BRW-175": [46, 47]
  "EC-BRW-178": [49, 50, 52, 54, 55, 73, 75]
  "EC-BRW-179": [58, 67, 68, 70]
---

# Mark as Returned pada level None: pelaku, pemisahan peran, bulk, dan hasil Returned, Missing, atau Damaged

## Prerequisites
- Aktor:
  - Principal, operator di luar tenant yang mengubah plan entitas DU-090-1.
  - Total Control entitas DU-090-1, cakupan seluruh client.
  - Group Manager DU-090-2, Group binaan Head Office.
  - Asset Admin DU-090-3, Group penugasan Head Office (pengaju dan pelaksana utama).
  - Asset Admin DU-090-4, Group penugasan Head Office (juga Borrower aset DU-090-12 dan PIC Borrower DU-090-7).
  - Asset Admin DU-090-5, Group penugasan Branch Surabaya saja.
  - Borrower DU-090-6, punya akun login.
  - Borrower DU-090-7, tanpa akun login, dengan PIC Asset Admin DU-090-4.
- Data:
  - DU-090-1: Entitas, Entitas khusus spec ini dengan plan yang diubah Principal; Entity Name `Entitas Wind-down Borrow {runId}`.
  - DU-090-2: User, Group Manager Head Office; Name `Sri Wahyuni {runId}`; Role `Group Manager`.
  - DU-090-3: User, Asset Admin pelaksana utama, Group penugasan Head Office; Name `Arif Setiawan {runId}`; Role `Asset Admin`.
  - DU-090-4: User, Asset Admin yang juga Borrower dan PIC, Group penugasan Head Office; Name `Maya Anggraini {runId}`; Role `Asset Admin`.
  - DU-090-5: User, Asset Admin Group penugasan Branch Surabaya saja; Name `Yoga Pratama {runId}`; Role `Asset Admin`.
  - DU-090-6: User, Borrower yang punya akun login; Name `Bagas Nugroho {runId}`.
  - DU-090-7: User, Borrower tanpa akun login dengan PIC Asset Admin DU-090-4; Name `Wulan Safitri {runId}`; PIC `Maya Anggraini {runId}`.
  - DU-090-8: Asset, aset Borrowed yang diselesaikan dengan hasil Returned tanpa Reason; Asset Name `Laptop Lenovo ThinkPad X1 Carbon {runId}`; Group `Head Office`.
  - DU-090-9: Asset, aset Overdue yang diselesaikan Total Control dengan hasil Returned; Asset Name `Proyektor Epson EB-L200F {runId}`; Group `Head Office`.
  - DU-090-10: Asset, aset Borrowed yang diselesaikan dengan hasil Missing; Asset Name `Tablet Samsung Galaxy Tab S9 {runId}`; Group `Head Office`.
  - DU-090-11: Asset, aset Borrowed yang diselesaikan dengan hasil Damaged; Asset Name `Kamera Canon EOS R50 {runId}`; Group `Head Office`.
  - DU-090-12: Asset, aset Borrowed milik Aktor sendiri sebagai Borrower; Asset Name `Laptop Asus Zenbook 14 {runId}`; Group `Head Office`.
  - DU-090-13: Asset, aset Borrowed yang dikelola Aktor sebagai PIC Borrower; Asset Name `Monitor LG UltraFine 27UP850 {runId}`; Group `Head Office`.
  - DU-090-14: Asset, aset Borrowed untuk uji Borrower, aset terkunci, dan bulk; Asset Name `Speaker Sony SRS-XB43 {runId}`; Group `Head Office`.
  - DU-090-15: Asset, aset Borrowed untuk uji Report dari halaman Borrow dan bulk; Asset Name `Mikrofon Rode NT-USB {runId}`; Group `Head Office`.
  - DU-090-16: Asset, aset Available pertama yang dilewati karena bukan Borrowed; Asset Name `Printer Brother HL-L3270CDW {runId}`; Group `Head Office`.
  - DU-090-17: Asset, aset Available kedua yang dilewati karena bukan Borrowed; Asset Name `Scanner Epson DS-530 {runId}`; Group `Head Office`.
  - DU-090-18: Parameter pengajuan wind-down, Duration dan Purpose pengajuan satuan Days; Duration `4 Day(s)`; Purpose `Pemakaian proyek {runId}`.
  - DU-090-19: Reason hasil Returned, Reason saat hasil Returned; Reason `Aset diselesaikan karena plan turun ke None {runId}`.
  - DU-090-20: Reason hasil Missing, Reason saat hasil Missing; Reason `Aset tidak ditemukan saat inventaris {runId}`.
  - DU-090-21: Reason hasil Damaged, Reason saat hasil Damaged; Reason `Layar retak di pojok kiri bawah {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus DU-090-1 yang tidak dipakai spec lain.
  - Plan entitas DU-090-1 awalnya berada di slot `paid_1` dan Approval Workflow tidak aktif.
  - Seluruh aset DU-090 berstatus `Available` dan tidak dipakai transaksi lain sebelum spec dimulai.

## Test Steps

### Mark as Returned ditolak pada level Basic dan hanya untuk aset Borrowed
1. Asset Admin DU-090-3 mengajukan BRW untuk aset DU-090-8, DU-090-9, DU-090-10, DU-090-11, DU-090-14, dan DU-090-15 atas nama Borrower DU-090-6 dengan Duration `4 Day(s)` dan Purpose `Pemakaian proyek {runId}`
2. Asset Admin DU-090-3 mengajukan BRW untuk aset DU-090-12 atas nama Asset Admin DU-090-4 sebagai Borrower dengan Duration `4 Day(s)` dan Purpose `Pemakaian proyek {runId}`
3. Asset Admin DU-090-3 mengajukan BRW untuk aset DU-090-13 atas nama Borrower DU-090-7 dengan PIC Asset Admin DU-090-4 dengan Duration `4 Day(s)` dan Purpose `Pemakaian proyek {runId}`
4. Asset Admin DU-090-3 menyerahkan aset DU-090-8, DU-090-9, DU-090-10, DU-090-11, DU-090-14, dan DU-090-15 kepada Borrower DU-090-6 dengan Condition `Normal`
5. Asset Admin DU-090-3 menyerahkan aset DU-090-12 kepada Asset Admin DU-090-4 dengan Condition `Normal`
6. Asset Admin DU-090-3 menyerahkan aset DU-090-13 kepada PIC Asset Admin DU-090-4 dengan Condition `Normal`
7. Waktu berlalu sampai 1 hari sesudah Due date aset DU-090-9
8. Job Overdue berjalan
9. Asset Admin DU-090-3 menjalankan Mark as Returned pada aset DU-090-8 pada level Basic
10. Verifikasi Mark as Returned ditolak pada level Basic dan baris aset DU-090-8 tetap `Borrowed`
11. Principal menurunkan plan entitas DU-090-1 ke slot `free` dan downgrade berlaku di T-0
12. Verifikasi tidak ada aksi Cancel wind-down karena baris menunggu sudah ditutup otomatis di T-0
13. Verifikasi Mark as Returned tersedia sebagai aksi baris dan aksi bulk di daftar aset serta sebagai aksi di header detail aset
14. Asset Admin DU-090-3 menjalankan Mark as Returned pada aset DU-090-16 yang berstatus `Available`
15. Verifikasi Mark as Returned ditolak untuk aset DU-090-16 karena Custody bukan `Borrowed`

### Hasil Returned oleh Asset Admin tanpa Reason dan tanpa scan atau foto
16. Asset Admin DU-090-3 menjalankan Mark as Returned pada aset DU-090-8 dengan pilihan hasil `Returned` tanpa Reason
17. Verifikasi dialog Mark as Returned memuat pilihan hasil `Returned`, `Missing`, dan `Damaged` dengan default `Returned`
18. Verifikasi Reason pada dialog Mark as Returned bersifat opsional dan permintaan tanpa Reason diterima
19. Verifikasi baris aset DU-090-8 berstatus `Returned` dan Custody aset DU-090-8 `Available`
20. Verifikasi Mark as Returned diproses tanpa scan TAG dan tanpa foto
21. Verifikasi node `Returned by [Actor]` untuk aset DU-090-8 tercatat dengan penanda `Plan change`
22. Verifikasi notifikasi Mark as Returned dikirim ke Borrower DU-090-6
23. Verifikasi toast `Success, asset has been marked as returned.` tampil
24. Verifikasi Mark as Returned oleh Asset Admin dalam cakupan Group aset DU-090-8 diterima

### Hasil Returned oleh Total Control untuk aset Overdue
25. Total Control menjalankan Mark as Returned pada aset DU-090-9 yang berstatus `Overdue` dengan pilihan hasil `Returned` dan Reason `Aset diselesaikan karena plan turun ke None {runId}`
26. Verifikasi baris aset DU-090-9 berstatus `Returned` dan Custody aset DU-090-9 `Available`
27. Verifikasi Mark as Returned oleh Total Control atas aset DU-090-9 diterima

### Hasil Missing oleh Group Manager
28. Group Manager DU-090-2 menjalankan Mark as Returned pada aset DU-090-10 dengan pilihan hasil `Missing` dan Reason `Aset tidak ditemukan saat inventaris {runId}`
29. Verifikasi baris aset DU-090-10 ditutup `Returned` dengan penanda `Missing`
30. Verifikasi laporan kehilangan untuk aset DU-090-10 dibuat mengikuti aturan laporan kehilangan saat dipinjam
31. Verifikasi Mark as Returned oleh Group Manager atas aset DU-090-10 diterima

### Hasil Damaged oleh Asset Admin
32. Asset Admin DU-090-3 menjalankan Mark as Returned pada aset DU-090-11 dengan pilihan hasil `Damaged` dan Reason `Layar retak di pojok kiri bawah {runId}`
33. Verifikasi baris aset DU-090-11 ditutup `Returned` dengan penanda `Damaged`
34. Verifikasi laporan kerusakan untuk aset DU-090-11 dibuat mengikuti aturan laporan kerusakan saat dipinjam

### Aktor di luar cakupan Group ditolak
35. Asset Admin DU-090-5 menjalankan Mark as Returned pada aset DU-090-14
36. Verifikasi Mark as Returned ditolak untuk Asset Admin di luar cakupan Group aset DU-090-14 dan baris aset DU-090-14 tetap `Borrowed`

### Borrower tidak dapat mengembalikan sendiri dan aset Borrowed tetap terkunci
37. Borrower DU-090-6 mengembalikan aset DU-090-14 sendiri
38. Verifikasi Return sendiri oleh Borrower atas aset DU-090-14 ditolak dan baris tetap `Borrowed`
39. Verifikasi Mark as Returned tidak punya scan sehingga Borrower atau PIC tidak dapat me-Mark as Returned asetnya sendiri
40. Verifikasi pemrosesan sendiri oleh Borrower atau PIC hanya sah dengan scan TAG karena tanpa scan tidak ada bukti fisik
41. Asset Admin DU-090-3 menjalankan Assign, Transfer, dan Dispose pada aset DU-090-14
42. Verifikasi Assign, Transfer, dan Dispose atas aset DU-090-14 yang masih `Borrowed` ditolak
43. Asset Admin DU-090-3 menjalankan Report Missing dan Report Damaged dari halaman Borrow atas aset DU-090-15
44. Verifikasi Report Missing dan Report Damaged atas aset DU-090-15 dari halaman Borrow ditolak dan hanya tersedia lewat hasil Mark as Returned
45. Asset Admin DU-090-3 mengajukan BRW baru untuk aset DU-090-16 atas nama Borrower DU-090-6 dengan Duration `4 Day(s)` dan Purpose `Pemakaian proyek {runId}`
46. Verifikasi aksi Borrow atas transaksi baru lewat API pada level None ditolak dengan kode galat `PLAN_FEATURE_UNAVAILABLE`
47. Verifikasi riwayat Borrow aset DU-090-8 tetap terbaca, Mark as Returned tetap diizinkan, dan job sistem tetap berjalan

### Pemisahan peran Aktor yang menjadi Borrower atau PIC
48. Asset Admin DU-090-4 menjalankan Mark as Returned pada aset DU-090-12 yang ia pinjam sendiri
49. Verifikasi aksi Mark as Returned aset DU-090-12 untuk Asset Admin DU-090-4 sebagai Borrower Disabled dengan alasan `You can't return your own borrowed asset.` tersampaikan pada aksi baris dan aksi header
50. Verifikasi Mark as Returned aset DU-090-12 oleh Asset Admin DU-090-4 sebagai Borrower ditolak server walau permintaan dikirim langsung
51. Asset Admin DU-090-4 menjalankan Mark as Returned pada aset DU-090-13 yang ia kelola sebagai PIC
52. Verifikasi aksi baris Mark as Returned aset DU-090-13 untuk Asset Admin DU-090-4 sebagai PIC Disabled dengan alasan `You're the PIC for this borrow. Ask another admin.` tersampaikan
53. Verifikasi aksi header Mark as Returned aset DU-090-13 untuk Asset Admin DU-090-4 sebagai PIC Disabled dengan alasan `You're the PIC for this borrow. Ask another admin.` tersampaikan
54. Verifikasi Mark as Returned aset DU-090-13 oleh Asset Admin DU-090-4 sebagai PIC Borrower ditolak server
55. Verifikasi baris aset DU-090-12 dan aset DU-090-13 dan Custody keduanya tidak berubah sesudah penolakan

### Bulk seluruhnya milik Aktor sendiri tidak membuka dialog
56. Asset Admin DU-090-4 memilih aset DU-090-12 dan aset DU-090-13
57. Asset Admin DU-090-4 menjalankan bulk Mark as Returned
58. Verifikasi dialog `D-BRW-25` tidak terbuka dan toast danger `Error, you can't return your own borrowed assets.` tampil

### Bulk campuran melewati aset bukan Borrowed dan aset milik sendiri
59. Asset Admin DU-090-4 memilih aset DU-090-12, DU-090-13, DU-090-14, DU-090-15, DU-090-16, dan DU-090-17
60. Asset Admin DU-090-4 menjalankan bulk Mark as Returned
61. Verifikasi bulk Mark as Returned tersedia karena sedikitnya satu aset terpilih berstatus `Borrowed`
62. Verifikasi dialog `D-BRW-25` memuat daftar aset Borrowed yang diproses, yaitu aset DU-090-14 dan aset DU-090-15, tanpa pilihan hasil
63. Verifikasi bulk hanya menghasilkan `Returned`, sedangkan hasil kehilangan atau kerusakan hanya lewat aksi per aset
64. Verifikasi aset DU-090-16 dan aset DU-090-17 yang bukan Borrowed dilewati
65. Verifikasi aset DU-090-12 dan aset DU-090-13 milik Asset Admin DU-090-4 sebagai Borrower atau PIC dilewati
66. Verifikasi dialog menampilkan `{N} assets skipped because they aren't borrowed.` dengan N bernilai 2
67. Verifikasi dialog menampilkan `{N} assets skipped because they're yours.` dengan N bernilai 2
68. Verifikasi caption aset bukan Borrowed tampil bersama caption aset milik sendiri pada dialog yang sama
69. Asset Admin DU-090-4 mengonfirmasi bulk Mark as Returned
70. Verifikasi hanya aset DU-090-14 dan aset DU-090-15 yang menjadi `Returned` sedangkan aset DU-090-12 dan aset DU-090-13 tidak berubah
71. Verifikasi toast `Success, [N] assets have been marked as returned.` tampil dengan N bernilai 2

### Aktor Borrow lain memproses aset milik Aktor
72. Asset Admin DU-090-3 menjalankan Mark as Returned pada aset DU-090-12 dengan pilihan hasil `Returned`
73. Verifikasi baris aset DU-090-12 berstatus `Returned` setelah diproses Aktor Borrow lain
74. Asset Admin DU-090-3 menjalankan Mark as Returned pada aset DU-090-13 dengan pilihan hasil `Returned`
75. Verifikasi baris aset DU-090-13 berstatus `Returned` setelah diproses Aktor Borrow lain
