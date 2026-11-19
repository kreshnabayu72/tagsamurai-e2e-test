---
id: TC-FA-BORROW-BE-089-plan-downgrade-linimasa
title: "Downgrade level plan di T-0: auto-cancel baris menunggu, penghapusan Draft, dan pemulihan"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["BORROW-LOGIC-19h", "BORROW-LOGIC-19j", "BORROW-LOGIC-19n", "BORROW-LOGIC-19r", "BORROW-LOGIC-19w", "BORROW-LOGIC-19x", "EC-BRW-166", "EC-BRW-167", "EC-BRW-168", "EC-BRW-169", "EC-BRW-174", "§9.11#p10", "§9.11#r36", "§9.11#r37", "§9.11#r38", "§9.11#r39", "§9.11#r40", "§9.11#r41", "§9.11#r42", "§9.11#r43", "§9.11#r44", "§9.11#p13"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-19h": [81, 82, 84]
  "BORROW-LOGIC-19j": [71, 72]
  "BORROW-LOGIC-19n": 75
  "BORROW-LOGIC-19r": [18, 68]
  "BORROW-LOGIC-19w": 73
  "BORROW-LOGIC-19x": [84, 86]
  "EC-BRW-166": [71, 72, 73, 74, 75]
  "EC-BRW-167": [76, 77, 78]
  "EC-BRW-168": [18, 19, 20, 68, 69]
  "EC-BRW-169": [40, 41, 43, 88, 89, 90]
  "EC-BRW-174": [25, 29]
  "§9.11#p10": 21
  "§9.11#r36": [16, 65, 66]
  "§9.11#r37": [18, 68]
  "§9.11#r38": 70
  "§9.11#r39": [40, 41, 43, 44, 88, 89, 90]
  "§9.11#r40": [18, 68]
  "§9.11#r41": [23, 25, 27, 34, 36]
  "§9.11#r42": [31, 32]
  "§9.11#r43": [29, 38]
  "§9.11#r44": 21
  "§9.11#p13": 22
---

# Downgrade level plan di T-0: auto-cancel baris menunggu, penghapusan Draft, dan pemulihan

## Prerequisites
- Aktor:
  - Principal, operator di luar tenant yang mengubah plan entitas DU-089-1.
  - Total Control entitas DU-089-1, cakupan seluruh client (menyimpan Transaction Settings).
  - Asset Admin DU-089-2, Group penugasan Head Office.
  - Approver DU-089-3, Group penugasan Head Office, eligible untuk aset Head Office.
  - Borrower DU-089-4, punya akun login.
- Data:
  - DU-089-1: Entitas, Entitas khusus spec ini dengan plan yang diubah Principal; Entity Name `Entitas Downgrade Borrow {runId}`.
  - DU-089-2: User, Asset Admin pengaju, Group penugasan Head Office; Name `Dimas Prakoso {runId}`; Role `Asset Admin`.
  - DU-089-3: User, Approver, Group penugasan Head Office; Name `Ratna Kusuma {runId}`; Role `Approver`.
  - DU-089-4: User, Borrower yang punya akun login; Name `Fajar Ramadhan {runId}`.
  - DU-089-5: Asset, aset dalam Draft yang dihapus di T-0 saat turun ke Basic; Asset Name `Printer Epson EcoTank L5290 {runId}`; Group `Head Office`.
  - DU-089-6: Asset, aset pinjaman self-service dari masa Full; Asset Name `Kamera GoPro Hero 12 {runId}`; Group `Head Office`.
  - DU-089-7: Asset, aset baris bersatuan Hours yang berjalan; Asset Name `Laptop Asus ROG Zephyrus G14 {runId}`; Group `Head Office`.
  - DU-089-8: Asset, aset Borrowed dengan Request Extension menunggu review; Asset Name `Proyektor Optoma UHD38 {runId}`; Group `Head Office`.
  - DU-089-9: Asset, aset baris Waiting for Approval yang dibatalkan saat Approval Workflow dicabut lalu diajukan ulang; Asset Name `Monitor Dell UltraSharp U2723QE {runId}`; Group `Head Office`.
  - DU-089-10: Asset, aset baris Waiting for Handover saat downgrade ke None; Asset Name `Tablet Samsung Galaxy Tab S8 {runId}`; Group `Head Office`.
  - DU-089-11: Asset, aset Borrowed dengan Extension menunggu approval saat downgrade ke None; Asset Name `Kamera Fujifilm X-T30 {runId}`; Group `Head Office`.
  - DU-089-12: Asset, aset baris Overdue saat downgrade ke None; Asset Name `Speaker JBL Flip 6 {runId}`; Group `Head Office`.
  - DU-089-13: Asset, aset dalam Draft yang dihapus di T-0 saat turun ke None; Asset Name `Printer HP DeskJet 2720 {runId}`; Group `Head Office`.
  - DU-089-15: Parameter pengajuan downgrade jam, Duration dan Purpose pengajuan satuan Hours; Duration `6 Hour(s)`; Purpose `Penugasan lapangan {runId}`.
  - DU-089-17: Parameter Extension downgrade jam, Durasi Extension satuan Hours; Extend duration `2 Hour(s)`.
  - DU-089-18: Transaction Settings downgrade, Nilai Transaction Settings yang disimpan sebelum downgrade; Self service `ON`; Duration unit `Hours`.
  - DU-089-19: Reason Mark as Returned downgrade, Reason saat Mark as Returned; Reason `Plan entitas turun ke None {runId}`.
  - DU-089-20: Asset, aset Borrowed yang melewati Due date sesudah downgrade ke None; Asset Name `Walkie Talkie Motorola T82 {runId}`; Group `Head Office`.
  - DU-089-21: Asset, aset pinjaman self-service yang masih berjalan pada level Basic; Asset Name `Kamera Sony ZV-1 {runId}`; Group `Head Office`.
- Kondisi:
  - Spec ini memakai entitas khusus DU-089-1 yang tidak dipakai spec lain.
  - Plan entitas DU-089-1 awalnya berada di slot `paid_2`.
  - Approval Workflow aktif pada slot `paid_2` dan tidak aktif pada slot `paid_1` dan `free`.
  - Seluruh aset DU-089 berstatus `Available` dan tidak dipakai transaksi lain sebelum spec dimulai.

## Test Steps

### Langkah Borrow pada wizard rekonsiliasi di T-30 sebelum turun ke Basic
1. Total Control menyimpan Transaction Settings Borrow dengan Self service `ON` dan Duration unit `Hours`
2. Asset Admin DU-089-2 menyimpan Draft berisi aset DU-089-5 untuk Borrower DU-089-4
3. Borrower DU-089-4 meminjam aset DU-089-6 lewat `Borrow Now` self-service dengan Duration `6 Hour(s)` dan Purpose `Penugasan lapangan {runId}`
4. Borrower DU-089-4 meminjam aset DU-089-21 lewat `Borrow Now` self-service dengan Duration `6 Hour(s)` dan Purpose `Penugasan lapangan {runId}`
5. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-7 atas nama Borrower DU-089-4 dengan Duration `6 Hour(s)` dan Purpose `Penugasan lapangan {runId}`
6. Approver DU-089-3 menyetujui aset DU-089-7
7. Asset Admin DU-089-2 menyerahkan aset DU-089-7 kepada Borrower DU-089-4 dengan Condition `Normal`
8. Borrower DU-089-4 mengonfirmasi handover aset DU-089-7
9. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-8 atas nama Borrower DU-089-4 dengan Duration `6 Hour(s)` dan Purpose `Penugasan lapangan {runId}`
10. Approver DU-089-3 menyetujui aset DU-089-8
11. Asset Admin DU-089-2 menyerahkan aset DU-089-8 kepada Borrower DU-089-4 dengan Condition `Normal`
12. Borrower DU-089-4 mengonfirmasi handover aset DU-089-8
13. Borrower DU-089-4 mengajukan Request Extension dari halaman pinjamannya untuk aset DU-089-8 dengan Extend duration `2 Hour(s)`
14. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-9 atas nama Borrower DU-089-4 dengan Duration `6 Hour(s)` dan Purpose `Penugasan lapangan {runId}`
15. Waktu berlalu sampai T-30 sebelum downgrade ke Basic
16. Verifikasi langkah Borrow pada wizard rekonsiliasi plan memuat daftar Draft yang akan terdampak turun ke Basic

### Downgrade Full ke Basic di T-0 menghapus Draft dan menutup approval yang dicabut
17. Principal menurunkan plan entitas DU-089-1 ke slot `paid_1` dan downgrade berlaku di T-0
18. Verifikasi Draft berisi aset DU-089-5 dihapus tanpa status akhir
19. Verifikasi penghapusan Draft tidak menghasilkan notifikasi
20. Verifikasi `Add to Borrow Draft` dan tab Drafts tidak tampil pada level Basic
21. Verifikasi baris aset DU-089-9 berstatus `Waiting for Approval` ditutup otomatis oleh sistem dengan log `Canceled by system (subscription downgraded — approval no longer available at [new plan])` karena Approval Workflow dicabut plan baru
22. Verifikasi perubahan plan tidak tercatat di Changelog Transaction Settings

### Pinjaman lama tetap berjalan pada level Basic
23. Verifikasi baris self-service aset DU-089-6 tetap berstatus `Borrowed` sesudah downgrade
24. Borrower DU-089-4 mengembalikan aset DU-089-6 sendiri
25. Verifikasi Return sendiri oleh Borrower atas baris self-service lama aset DU-089-6 diterima
26. Borrower DU-089-4 menjalankan Return sendiri atas aset DU-089-7 yang bukan pinjaman self-service
27. Verifikasi Return sendiri oleh Borrower atas aset DU-089-7 yang bukan pinjaman self-service ditolak
28. Borrower DU-089-4 mengajukan Request Extension dari halaman pinjamannya untuk aset DU-089-7 dengan Extend duration `2 Hour(s)`
29. Verifikasi Request Extension baru oleh Borrower ditolak dan tidak ada pengajuan Extension baru
30. Asset Admin DU-089-2 menjalankan Extend aset DU-089-7 dengan Extend duration `2 Hour(s)`
31. Verifikasi Extend aset DU-089-7 tetap dalam jam dan Due date bertambah 2 jam
32. Verifikasi baris aset DU-089-7 memakai snapshot satuan Hours sampai selesai
33. Borrower DU-089-4 mengajukan Extend aset DU-089-21 dari halaman pinjamannya dengan Extend duration `2 Hour(s)`
34. Verifikasi pengajuan Extend oleh Borrower atas pinjaman self-service berjalan aset DU-089-21 ditolak
35. Asset Admin DU-089-2 menjalankan Extend aset DU-089-21 dengan Extend duration `2 Hour(s)`
36. Verifikasi Extend oleh Aktor Borrow atas pinjaman self-service aset DU-089-21 diterima dan Due date bertambah
37. Asset Admin DU-089-2 menerapkan Extension dari Request Extension aset DU-089-8 yang menunggu review
38. Verifikasi Request Extension aset DU-089-8 yang menunggu review tetap diproses sesudah downgrade

### Upgrade kembali ke Full tidak memulihkan yang sudah dihapus atau dibatalkan
39. Principal menaikkan plan entitas DU-089-1 kembali ke slot `paid_2` pada masa Grace
40. Verifikasi Draft berisi aset DU-089-5 yang sudah dihapus tidak dipulihkan
41. Verifikasi baris aset DU-089-9 yang dibatalkan otomatis tetap berstatus `Canceled` dan tidak dipulihkan
42. Asset Admin DU-089-2 mengajukan ulang BRW untuk aset DU-089-9 atas nama Borrower DU-089-4 dengan Duration `6 Hour(s)` dan Purpose `Penugasan lapangan {runId}`
43. Verifikasi pengajuan ulang aset DU-089-9 diterima dan baris baru berstatus `Waiting for Approval`
44. Verifikasi nilai Transaction Settings Self service `ON` dan Duration unit `Hours` langsung berlaku sesudah upgrade

### Baris disiapkan pada level Full sebelum downgrade ke None
45. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-10 atas nama Borrower DU-089-4 dengan Duration `6 Hour(s)` dan Purpose `Penugasan lapangan {runId}`
46. Approver DU-089-3 menyetujui aset DU-089-10
47. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-11 atas nama Borrower DU-089-4 dengan Duration `6 Hour(s)` dan Purpose `Penugasan lapangan {runId}`
48. Approver DU-089-3 menyetujui aset DU-089-11
49. Asset Admin DU-089-2 menyerahkan aset DU-089-11 kepada Borrower DU-089-4 dengan Condition `Normal`
50. Borrower DU-089-4 mengonfirmasi handover aset DU-089-11
51. Asset Admin DU-089-2 mengajukan Extend aset DU-089-11 dengan Extend duration `2 Hour(s)` yang menunggu approval
52. Due date aset DU-089-11 dicatat sebagai Due date sebelum downgrade
53. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-12 atas nama Borrower DU-089-4 dengan Duration `6 Hour(s)` dan Purpose `Penugasan lapangan {runId}`
54. Approver DU-089-3 menyetujui aset DU-089-12
55. Asset Admin DU-089-2 menyerahkan aset DU-089-12 kepada Borrower DU-089-4 dengan Condition `Normal`
56. Borrower DU-089-4 mengonfirmasi handover aset DU-089-12
57. Waktu berlalu sampai 1 hari sesudah Due date aset DU-089-12
58. Job Overdue berjalan
59. Asset Admin DU-089-2 menyimpan Draft berisi aset DU-089-13 untuk Borrower DU-089-4
60. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-20 atas nama Borrower DU-089-4 dengan Duration `6 Hour(s)` dan Purpose `Penugasan lapangan {runId}`
61. Approver DU-089-3 menyetujui aset DU-089-20
62. Asset Admin DU-089-2 menyerahkan aset DU-089-20 kepada Borrower DU-089-4 dengan Condition `Normal`
63. Borrower DU-089-4 mengonfirmasi handover aset DU-089-20
64. Waktu berlalu sampai T-30 sebelum downgrade ke None
65. Verifikasi langkah Borrow pada wizard rekonsiliasi plan memuat daftar BRW In Borrow Process dan Borrowed yang akan terdampak turun ke None
66. Verifikasi langkah Borrow pada wizard rekonsiliasi plan memuat daftar Draft yang akan terdampak turun ke None

### Downgrade Full ke None di T-0 menutup baris menunggu dan menghapus Draft
67. Principal menurunkan plan entitas DU-089-1 ke slot `free` dan downgrade berlaku di T-0
68. Verifikasi Draft berisi aset DU-089-13 dihapus tanpa status akhir pada downgrade ke None
69. Verifikasi penghapusan Draft berisi aset DU-089-13 tidak menghasilkan notifikasi
70. Verifikasi baris aset DU-089-9 dan aset DU-089-10 berstatus `Waiting for Approval` dan `Waiting for Handover` ditutup otomatis di T-0
71. Verifikasi baris aset DU-089-9 dan aset DU-089-10 ditutup `Canceled` oleh `System` dengan alasan `Borrowing not available on plan`
72. Verifikasi tidak ada Draft baru berisi aset DU-089-9 maupun aset DU-089-10
73. Verifikasi Custody aset DU-089-9 dan aset DU-089-10 kembali `Available`
74. Verifikasi node `Canceled by [Actor]` untuk aset DU-089-10 tercatat dengan pelaku `System`
75. Verifikasi notifikasi auto-cancel dikirim sekali ke pengaju dan ke Borrower
76. Verifikasi Extension aset DU-089-11 yang menunggu ikut `Canceled` dengan alasan `Borrowing not available on plan`
77. Verifikasi Due date aset DU-089-11 sama dengan Due date yang dicatat sebelum downgrade
78. Verifikasi baris aset DU-089-11 dan aset DU-089-20 tetap `Borrowed` dan baris aset DU-089-12 tetap `Overdue`

### Baris Borrowed dan Overdue diselesaikan lewat Mark as Returned pada level None
79. Waktu berlalu sampai 1 hari sesudah Due date aset DU-089-20
80. Job Overdue berjalan
81. Verifikasi job sistem tetap berjalan pada level None: baris aset DU-089-20 berubah menjadi `Overdue` dan baris aset DU-089-12 tetap `Overdue`
82. Verifikasi riwayat Borrow aset DU-089-11 tetap terbaca di Transaction log aset dan Transaction admin log
83. Asset Admin DU-089-2 menjalankan Mark as Returned pada aset DU-089-11 dengan Outcome `Returned` dan Reason `Plan entitas turun ke None {runId}`
84. Verifikasi baris aset DU-089-11 berstatus `Returned` sesudah Mark as Returned
85. Asset Admin DU-089-2 menjalankan Mark as Returned pada aset DU-089-12 dengan Outcome `Returned` dan Reason `Plan entitas turun ke None {runId}`
86. Verifikasi baris aset DU-089-12 berstatus `Returned` sesudah Mark as Returned

### Upgrade kembali dari level None tidak memulihkan yang sudah dihapus atau dibatalkan
87. Principal menaikkan plan entitas DU-089-1 kembali ke slot `paid_2` pada masa Grace
88. Verifikasi Draft berisi aset DU-089-13 yang sudah dihapus tidak dipulihkan
89. Verifikasi baris aset DU-089-9 dan aset DU-089-10 yang dibatalkan otomatis tetap berstatus `Canceled` dan tidak dipulihkan
90. Verifikasi Extension aset DU-089-11 yang dibatalkan otomatis tetap berstatus `Canceled` dan tidak dipulihkan
