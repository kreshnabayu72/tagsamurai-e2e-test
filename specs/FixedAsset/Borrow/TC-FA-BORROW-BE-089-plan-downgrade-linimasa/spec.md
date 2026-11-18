---
id: TC-FA-BORROW-BE-089-plan-downgrade-linimasa
title: "Downgrade level plan di T-0: auto-cancel baris menunggu, penghapusan Draft, dan pemulihan"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["BORROW-LOGIC-19h", "BORROW-LOGIC-19j", "BORROW-LOGIC-19n", "BORROW-LOGIC-19r", "BORROW-LOGIC-19w", "BORROW-LOGIC-19x", "EC-BRW-166", "EC-BRW-167", "EC-BRW-168", "EC-BRW-169", "EC-BRW-174", "§9.11#p10", "§9.11#r36", "§9.11#r37", "§9.11#r38", "§9.11#r39", "§9.11#r40", "§9.11#r41", "§9.11#r42", "§9.11#r43", "§9.11#r44", "§9.11#p13"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-19h": [70, 71, 73]
  "BORROW-LOGIC-19j": [61, 62]
  "BORROW-LOGIC-19n": 65
  "BORROW-LOGIC-19r": [17, 59]
  "BORROW-LOGIC-19w": 63
  "BORROW-LOGIC-19x": [73, 75]
  "EC-BRW-166": [61, 62, 63, 64, 65]
  "EC-BRW-167": [66, 67, 68]
  "EC-BRW-168": [17, 18, 19, 59]
  "EC-BRW-169": [35, 36, 38]
  "EC-BRW-174": [25, 27]
  "§9.11#p10": 21
  "§9.11#r36": [15, 56, 57]
  "§9.11#r37": [17, 59]
  "§9.11#r38": 60
  "§9.11#r39": [35, 36, 38, 39]
  "§9.11#r40": [17, 59]
  "§9.11#r41": [23, 25, 31]
  "§9.11#r42": [29, 30]
  "§9.11#r43": [27, 33]
  "§9.11#r44": 20
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
  - DU-089-14: Parameter pengajuan downgrade, Duration dan Purpose pengajuan satuan Days; Duration `4 Day(s)`; Purpose `Penugasan lapangan {runId}`.
  - DU-089-15: Parameter pengajuan downgrade jam, Duration dan Purpose pengajuan satuan Hours; Duration `6 Hour(s)`; Purpose `Penugasan lapangan {runId}`.
  - DU-089-16: Parameter Extension downgrade, Durasi Extension satuan Days; Extend duration `2 Day(s)`.
  - DU-089-17: Parameter Extension downgrade jam, Durasi Extension satuan Hours; Extend duration `2 Hour(s)`.
  - DU-089-18: Transaction Settings downgrade, Nilai Transaction Settings yang disimpan sebelum downgrade; Self service `ON`; Duration unit `Hours`.
  - DU-089-19: Reason Mark as Returned downgrade, Reason saat Mark as Returned; Reason `Plan entitas turun ke None {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus DU-089-1 yang tidak dipakai spec lain.
  - Plan entitas DU-089-1 awalnya berada di slot `paid_2`.
  - Approval Workflow aktif pada slot `paid_2` dan tidak aktif pada slot `paid_1` dan `free`.
  - Seluruh aset DU-089 berstatus `Available` dan tidak dipakai transaksi lain sebelum spec dimulai.

## Test Steps

### Langkah Borrow pada wizard rekonsiliasi di T-30 sebelum turun ke Basic
1. Asset Admin DU-089-2 menyimpan Draft berisi aset DU-089-5 untuk Borrower DU-089-4
2. Borrower DU-089-4 meminjam aset DU-089-6 lewat `Borrow Now` self-service dengan Duration `4 Day(s)` dan Purpose `Penugasan lapangan {runId}`
3. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-7 atas nama Borrower DU-089-4 dengan Duration `6 Hour(s)` dan Purpose `Penugasan lapangan {runId}`
4. Approver DU-089-3 menyetujui aset DU-089-7
5. Asset Admin DU-089-2 menyerahkan aset DU-089-7 kepada Borrower DU-089-4 dengan Condition `Normal`
6. Borrower DU-089-4 mengonfirmasi handover aset DU-089-7
7. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-8 atas nama Borrower DU-089-4 dengan Duration `4 Day(s)` dan Purpose `Penugasan lapangan {runId}`
8. Approver DU-089-3 menyetujui aset DU-089-8
9. Asset Admin DU-089-2 menyerahkan aset DU-089-8 kepada Borrower DU-089-4 dengan Condition `Normal`
10. Borrower DU-089-4 mengonfirmasi handover aset DU-089-8
11. Borrower DU-089-4 mengajukan Request Extension dari halaman pinjamannya untuk aset DU-089-8 dengan Extend duration `2 Day(s)`
12. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-9 atas nama Borrower DU-089-4 dengan Duration `4 Day(s)` dan Purpose `Penugasan lapangan {runId}`
13. Total Control menyimpan Transaction Settings Borrow dengan Self service `ON` dan Duration unit `Hours`
14. Waktu berlalu sampai T-30 sebelum downgrade ke Basic
15. Verifikasi langkah Borrow pada wizard rekonsiliasi plan memuat daftar Draft yang akan terdampak turun ke Basic

### Downgrade Full ke Basic di T-0 menghapus Draft dan menutup approval yang dicabut
16. Principal menurunkan plan entitas DU-089-1 ke slot `paid_1` dan downgrade berlaku di T-0
17. Verifikasi Draft berisi aset DU-089-5 dihapus tanpa status akhir
18. Verifikasi penghapusan Draft tidak menghasilkan notifikasi
19. Verifikasi `Add to Borrow Draft` dan tab Drafts tidak tampil pada level Basic
20. Verifikasi baris aset DU-089-9 berstatus `Waiting for Approval` ditutup otomatis oleh sistem dengan log `Canceled by system (subscription downgraded — approval no longer available at [new plan])` karena Approval Workflow dicabut plan baru
21. Verifikasi auto-cancel pengajuan Waiting for Approval saat Approval Workflow dicabut dimiliki aturan plan, dan downgrade level Feature Suite Borrowing dimiliki Borrow
22. Verifikasi perubahan plan tidak tercatat di Changelog Transaction Settings

### Pinjaman lama tetap berjalan pada level Basic
23. Verifikasi baris self-service aset DU-089-6 tetap berstatus `Borrowed` sesudah downgrade
24. Borrower DU-089-4 mengembalikan aset DU-089-6 sendiri
25. Verifikasi Return sendiri oleh Borrower atas baris self-service lama aset DU-089-6 diterima
26. Borrower DU-089-4 mengajukan Request Extension dari halaman pinjamannya untuk aset DU-089-7 dengan Extend duration `2 Day(s)`
27. Verifikasi Request Extension baru oleh Borrower ditolak dan tidak ada pengajuan Extension baru
28. Asset Admin DU-089-2 menjalankan Extend aset DU-089-7 dengan Extend duration `2 Hour(s)`
29. Verifikasi Extend aset DU-089-7 tetap dalam jam dan Due date bertambah 2 jam
30. Verifikasi baris aset DU-089-7 memakai snapshot satuan Hours sampai selesai
31. Verifikasi pinjaman self-service berjalan tidak bisa di-Extend oleh Borrower dan Extend dilakukan Aktor Borrow
32. Asset Admin DU-089-2 menerapkan Extension dari Request Extension aset DU-089-8 yang menunggu review
33. Verifikasi Request Extension aset DU-089-8 yang menunggu review tetap diproses sesudah downgrade

### Upgrade kembali ke Full tidak memulihkan yang sudah dihapus atau dibatalkan
34. Principal menaikkan plan entitas DU-089-1 kembali ke slot `paid_2` pada masa Grace
35. Verifikasi Draft berisi aset DU-089-5 yang sudah dihapus tidak dipulihkan
36. Verifikasi baris aset DU-089-9 yang dibatalkan otomatis tetap berstatus `Canceled` dan tidak dipulihkan
37. Asset Admin DU-089-2 mengajukan ulang BRW untuk aset DU-089-9 atas nama Borrower DU-089-4 dengan Duration `4 Day(s)` dan Purpose `Penugasan lapangan {runId}`
38. Verifikasi pengajuan ulang aset DU-089-9 diterima dan baris baru berstatus `Waiting for Approval`
39. Verifikasi nilai Transaction Settings Self service `ON` dan Duration unit `Hours` langsung berlaku sesudah upgrade

### Baris disiapkan pada level Full sebelum downgrade ke None
40. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-10 atas nama Borrower DU-089-4 dengan Duration `4 Day(s)` dan Purpose `Penugasan lapangan {runId}`
41. Approver DU-089-3 menyetujui aset DU-089-10
42. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-11 atas nama Borrower DU-089-4 dengan Duration `4 Day(s)` dan Purpose `Penugasan lapangan {runId}`
43. Approver DU-089-3 menyetujui aset DU-089-11
44. Asset Admin DU-089-2 menyerahkan aset DU-089-11 kepada Borrower DU-089-4 dengan Condition `Normal`
45. Borrower DU-089-4 mengonfirmasi handover aset DU-089-11
46. Asset Admin DU-089-2 mengajukan Extend aset DU-089-11 dengan Extend duration `2 Day(s)` yang menunggu approval
47. Due date aset DU-089-11 dicatat sebagai Due date sebelum downgrade
48. Asset Admin DU-089-2 mengajukan BRW untuk aset DU-089-12 atas nama Borrower DU-089-4 dengan Duration `4 Day(s)` dan Purpose `Penugasan lapangan {runId}`
49. Approver DU-089-3 menyetujui aset DU-089-12
50. Asset Admin DU-089-2 menyerahkan aset DU-089-12 kepada Borrower DU-089-4 dengan Condition `Normal`
51. Borrower DU-089-4 mengonfirmasi handover aset DU-089-12
52. Waktu berlalu sampai 1 hari sesudah Due date aset DU-089-12
53. Job Overdue berjalan
54. Asset Admin DU-089-2 menyimpan Draft berisi aset DU-089-13 untuk Borrower DU-089-4
55. Waktu berlalu sampai T-30 sebelum downgrade ke None
56. Verifikasi langkah Borrow pada wizard rekonsiliasi plan memuat daftar BRW In Borrow Process dan Borrowed yang akan terdampak turun ke None
57. Verifikasi konten langkah Borrow untuk wizard rekonsiliasi plan disiapkan Borrow dalam bentuk siap dipasang, sementara wizard dimiliki modul wizard

### Downgrade Full ke None di T-0 menutup baris menunggu dan menghapus Draft
58. Principal menurunkan plan entitas DU-089-1 ke slot `free` dan downgrade berlaku di T-0
59. Verifikasi Draft berisi aset DU-089-13 dihapus tanpa status akhir pada downgrade ke None
60. Verifikasi baris aset DU-089-9 dan aset DU-089-10 berstatus `Waiting for Approval` dan `Waiting for Handover` ditutup otomatis di T-0
61. Verifikasi baris aset DU-089-9 dan aset DU-089-10 ditutup `Canceled` oleh `System` dengan alasan `Borrowing not available on plan`
62. Verifikasi tidak ada Draft baru berisi aset DU-089-9 maupun aset DU-089-10
63. Verifikasi Custody aset DU-089-9 dan aset DU-089-10 kembali `Available`
64. Verifikasi node `Canceled by [Actor]` untuk aset DU-089-10 tercatat dengan pelaku `System`
65. Verifikasi notifikasi auto-cancel dikirim sekali ke pengaju dan ke Borrower
66. Verifikasi Extension aset DU-089-11 yang menunggu ikut `Canceled` dengan alasan `Borrowing not available on plan`
67. Verifikasi Due date aset DU-089-11 sama dengan Due date yang dicatat sebelum downgrade
68. Verifikasi baris aset DU-089-11 tetap `Borrowed` dan baris aset DU-089-12 tetap `Overdue`

### Baris Borrowed dan Overdue diselesaikan lewat Mark as Returned pada level None
69. Job Overdue berjalan
70. Verifikasi job sistem tetap berjalan pada level None dan baris aset DU-089-12 tetap `Overdue`
71. Verifikasi riwayat Borrow aset DU-089-11 tetap terbaca di Transaction log aset dan Transaction admin log
72. Asset Admin DU-089-2 menjalankan Mark as Returned pada aset DU-089-11 dengan Outcome `Returned` dan Reason `Plan entitas turun ke None {runId}`
73. Verifikasi baris aset DU-089-11 berstatus `Returned` sesudah Mark as Returned
74. Asset Admin DU-089-2 menjalankan Mark as Returned pada aset DU-089-12 dengan Outcome `Returned` dan Reason `Plan entitas turun ke None {runId}`
75. Verifikasi baris aset DU-089-12 berstatus `Returned` sesudah Mark as Returned
