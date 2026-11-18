---
id: TC-FA-BORROW-BE-093-sinkron-lintas-modul
title: "Efek lintas modul tiap aksi: Custody, snapshot, Draft, Damaged, Missing, Report TAG, offboarding, dan notifikasi"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§9.7#p1", "§9.7#r1", "§9.7#r2", "§9.7#r3", "§9.7#r4", "§9.7#r5", "§9.7#r6", "§9.7#r7", "§9.7#r8", "§9.7#r9", "§9.7#r10", "§9.7#r11", "§9.7#r12", "§9.7#r13", "§9.7#r14", "§9.7#r15", "§9.7#r16", "§9.7#r17", "§9.7#r18", "§9.7#r19", "§9.7#r20", "§9.7#r21", "§9.7#r22", "§9.7#r23"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§9.7#p1": [4, 5, 25, 26, 36]
  "§9.7#r1": [2, 3]
  "§9.7#r2": [20, 24]
  "§9.7#r3": [20, 21, 22, 23]
  "§9.7#r4": [40, 41, 42]
  "§9.7#r5": [16, 35, 38]
  "§9.7#r6": 86
  "§9.7#r7": [46, 47, 48, 53, 54]
  "§9.7#r8": [56, 57, 62]
  "§9.7#r9": [59, 60]
  "§9.7#r10": [12, 15]
  "§9.7#r11": [28, 29]
  "§9.7#r12": [80, 81, 82]
  "§9.7#r13": [32, 33]
  "§9.7#r14": 5
  "§9.7#r15": [64, 65, 67, 68]
  "§9.7#r16": [70, 71]
  "§9.7#r17": [73, 75]
  "§9.7#r18": [77, 78]
  "§9.7#r19": [84, 85]
  "§9.7#r20": 7
  "§9.7#r21": 8
  "§9.7#r22": [9, 10]
  "§9.7#r23": 6
---

# Efek lintas modul tiap aksi: Custody, snapshot, Draft, Damaged, Missing, Report TAG, offboarding, dan notifikasi

## Prerequisites
- Aktor:
  - Asset Admin DU-093-20, Group penugasan Head Office (pelaku utama).
  - Approver DU-093-21, Group penugasan Head Office, eligible untuk aset Head Office.
  - Borrower DU-093-22 dan Borrower DU-093-23, punya akun login.
  - Aktor yang berhak atas laporan kehilangan DU-093-24, Asset Admin dengan hak Aktor Missing pada Group Head Office.
  - Total Control, cakupan seluruh client.
- Data:
  - DU-093-5: Asset, aset BRW pertama untuk Submit, handover per aset, Extend, Overdue, dan Return; Asset Name `Laptop Dell Latitude 5440 {runId}`; Group `Head Office`.
  - DU-093-6: Asset, aset BRW pertama yang tidak dicentang lalu di-Cancel; Asset Name `Monitor Samsung S27 {runId}`; Group `Head Office`.
  - DU-093-7: Asset, aset yang ditolak approver; Asset Name `Proyektor Epson EB-FH06 {runId}`; Group `Head Office`.
  - DU-093-8: Asset, aset Borrow Now self-service; Asset Name `Kamera Sony A7C {runId}`; Group `Head Office`.
  - DU-093-9: Asset, aset untuk Cancel dengan Save as Draft to edit; Asset Name `Tablet Samsung Galaxy Tab S9 {runId}`; Group `Head Office`.
  - DU-093-10: Asset, aset untuk timeout Not picked up; Asset Name `Printer Canon G3010 {runId}`; Group `Head Office`.
  - DU-093-11: Asset, aset untuk Save Draft dan Delete Draft; Asset Name `Speaker JBL PartyBox 310 {runId}`; Group `Head Office`.
  - DU-093-12: Asset, aset yang ditambahkan lewat Add to Borrow Draft; Asset Name `Drone DJI Mavic 3 {runId}`; Group `Head Office`.
  - DU-093-13: Asset, aset Borrowed dengan laporan kerusakan; Asset Name `Laptop Lenovo ThinkPad L14 {runId}`; Group `Head Office`.
  - DU-093-14: Asset, aset Borrowed dengan laporan kehilangan oleh Borrower; Asset Name `Mikrofon Rode Wireless GO II {runId}`; Group `Head Office`.
  - DU-093-15: Asset, aset Borrowed dengan laporan kehilangan oleh Aktor yang berhak; Asset Name `Scanner Epson V600 {runId}`; Group `Head Office`.
  - DU-093-16: Asset, aset Waiting for Handover untuk Report TAG; Asset Name `Gimbal Zhiyun Crane 4 {runId}`; Group `Head Office`.
  - DU-093-17: Asset, aset Borrowed dengan Extension yang dibatalkan; Asset Name `Laptop HP ZBook Firefly {runId}`; Group `Head Office`.
  - DU-093-18: Asset, aset Waiting for Approval milik Borrower yang dinonaktifkan; Asset Name `Kamera Fujifilm X-S20 {runId}`; Group `Head Office`.
  - DU-093-19: Asset, aset Borrowed milik Borrower yang dinonaktifkan; Asset Name `Monitor Dell P2723QE {runId}`; Group `Head Office`.
  - DU-093-20: User, Asset Admin pelaku utama; Name `Rina Marlina {runId}`; Role `Asset Admin`.
  - DU-093-21: User, Approver; Name `Benny Gunawan {runId}`; Role `Approver`.
  - DU-093-22: User, Borrower pertama yang punya akun login; Name `Citra Dewanti {runId}`.
  - DU-093-23: User, Borrower kedua yang punya akun login dan akan dinonaktifkan; Name `Eko Prasetyo {runId}`.
  - DU-093-24: User, Asset Admin dengan hak Aktor Missing; Name `Fitri Handayani {runId}`; Role `Asset Admin`.
  - DU-093-25: Parameter pengajuan sinkron, Duration dan Purpose pengajuan; Duration `4 Day(s)`; Purpose `Pemakaian operasional {runId}`.
  - DU-093-26: Parameter Extension sinkron, Durasi Extension yang diajukan; Extend duration `2 Day(s)`.
  - DU-093-27: Reason penolakan sinkron, Reason saat approver menolak aset; Reason `Aset sedang dipesan untuk kegiatan lain {runId}`.
  - DU-093-28: Deskripsi kerusakan sinkron, Description laporan kerusakan; Description `Layar retak di pojok kiri bawah {runId}`.
  - DU-093-29: Reason kehilangan sinkron, Reason laporan kehilangan; Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`.
- Kondisi:
  - Level Borrowing entitas suite adalah Full dan Approval Workflow aktif.
  - Baris aset DU-093-13, DU-093-14, dan DU-093-17 berstatus `Borrowed` untuk Borrower DU-093-22, masing-masing dalam BRW sendiri.
  - Aset DU-093-13 dan aset DU-093-17 punya Extension yang menunggu approval dan Due date lebih dari 3 hari lagi.
  - Baris aset DU-093-15 berstatus `Borrowed` untuk Borrower DU-093-22 dan Group Head Office.
  - Baris aset DU-093-16 berstatus `Waiting for Handover` untuk Borrower DU-093-22.
  - Baris aset DU-093-18 berstatus `Waiting for Approval` dan baris aset DU-093-19 berstatus `Borrowed` untuk Borrower DU-093-23.
  - Transaction Settings entitas suite tidak diubah selama spec ini berjalan.

## Test Steps

### Submit mengunci Custody, membentuk snapshot, dan menulis log serta notifikasi
1. Asset Admin DU-093-20 mengajukan BRW untuk aset DU-093-5 dan aset DU-093-6 atas nama Borrower DU-093-22 dengan Duration `4 Day(s)` dan Purpose `Pemakaian operasional {runId}`
2. Verifikasi Custody aset DU-093-5 dan aset DU-093-6 berubah menjadi `In Borrow Process`
3. Verifikasi aset DU-093-5 tidak layak untuk transaksi lain selama Custody `In Borrow Process`
4. Verifikasi status baris aset DU-093-5 bernilai `Waiting for Approval` dan disimpan sebagai milik modul Borrow
5. Verifikasi aturan efektif dan data Borrower tersimpan ke baris aset DU-093-5 sebagai snapshot saat Submit
6. Verifikasi batas Transaction timeout baris aset DU-093-5 dihitung dari aturan efektif yang berlaku saat Submit
7. Verifikasi event notifikasi Submit untuk aset DU-093-5 terbentuk dalam 60 detik
8. Verifikasi Transaction log aset DU-093-5 memuat satu baris dengan Status `Waiting for Approval`
9. Verifikasi Transaction admin log Asset Admin DU-093-20 memuat entri Submit
10. Verifikasi log pengguna Borrower DU-093-22 memuat peristiwa Submit yang sama

### Approve membuat baris siap diambil dan Reject melepas Custody
11. Approver DU-093-21 menyetujui aset DU-093-5 dan aset DU-093-6
12. Verifikasi status baris aset DU-093-5 dan aset DU-093-6 berubah menjadi `Waiting for Handover`
13. Asset Admin DU-093-20 mengajukan BRW untuk aset DU-093-7 atas nama Borrower DU-093-22 dengan Duration `4 Day(s)` dan Purpose `Pemakaian operasional {runId}`
14. Approver DU-093-21 menolak aset DU-093-7 dengan Reason `Aset sedang dipesan untuk kegiatan lain {runId}`
15. Verifikasi status baris aset DU-093-7 berubah menjadi `Rejected`
16. Verifikasi Custody aset DU-093-7 kembali `Available` dan aset DU-093-7 muncul lagi di pool aset yang tersedia

### Handover per aset hanya mengikat aset yang dicentang Borrower
17. Asset Admin DU-093-20 memulai handover aset DU-093-5 dan aset DU-093-6 kepada Borrower DU-093-22 dengan Condition `Normal`
18. Borrower DU-093-22 mencentang hanya aset DU-093-5 dan membiarkan aset DU-093-6 tidak tercentang
19. Borrower DU-093-22 mengonfirmasi handover
20. Verifikasi baris aset DU-093-5 berstatus `Borrowed` dan Custody aset DU-093-5 berubah menjadi `Borrowed`
21. Verifikasi baris aset DU-093-6 tetap `Waiting for Handover` dengan keterangan `Not received`
22. Verifikasi Task `Confirm Handover` milik Borrower DU-093-22 hilang sesudah konfirmasi
23. Verifikasi Due date hanya ditetapkan untuk aset DU-093-5 dan tidak untuk aset DU-093-6
24. Verifikasi Held by pada aset DU-093-5 bernilai `until [Date]` sesuai Due date
25. Verifikasi status header BRW diturunkan dari status baris dan tidak disimpan sendiri
26. Verifikasi Custody aset DU-093-5 tercermin di daftar aset dan detail aset sebagai `Borrowed`

### Extend yang berlaku menggeser Due date dan Held by
27. Asset Admin DU-093-20 menjalankan Extend aset DU-093-5 dengan Extend duration `2 Day(s)`
28. Verifikasi Due date baris aset DU-093-5 berubah menjadi Due date baru sesudah Extend
29. Verifikasi Held by pada aset DU-093-5 mengikuti Due date baru dengan `until [Date]`

### Baris Overdue menandai aset dan memunculkan Needs attention
30. Waktu berlalu sampai 1 hari sesudah Due date aset DU-093-5
31. Job Overdue berjalan
32. Verifikasi baris aset DU-093-5 berpenanda `Overdue`
33. Verifikasi aset DU-093-5 tampil dengan Needs attention `Borrow overdue` dan aksi `Return`

### Return melepas Custody dan header mengikuti baris
34. Asset Admin DU-093-20 menerima kembali aset DU-093-5 dengan Condition `Normal`
35. Verifikasi Custody aset DU-093-5 kembali `Available` dan aset DU-093-5 muncul lagi di pool aset yang tersedia
36. Verifikasi status header BRW berubah mengikuti status baris sesudah Return

### Cancel baris menunggu melepas Custody
37. Asset Admin DU-093-20 menjalankan Cancel Borrow atas baris aset DU-093-6
38. Verifikasi baris aset DU-093-6 berstatus `Canceled` dan Custody aset DU-093-6 kembali `Available`

### Borrow Now langsung Borrowed tanpa tahap handover
39. Borrower DU-093-22 meminjam aset DU-093-8 lewat `Borrow Now` self-service dengan Duration `4 Day(s)` dan Purpose `Pemakaian operasional {runId}`
40. Verifikasi baris aset DU-093-8 langsung `Borrowed` tanpa tahap `Waiting for Handover` dan Source `Self-service`
41. Verifikasi Custody aset DU-093-8 berubah menjadi `Borrowed`
42. Verifikasi aset DU-093-8 tampil di Held by dan di tab Borrowed milik Borrower DU-093-22

### Cancel dengan Save as Draft to edit membentuk Draft baru
43. Asset Admin DU-093-20 mengajukan BRW untuk aset DU-093-9 atas nama Borrower DU-093-22 dengan Duration `4 Day(s)` dan Purpose `Pemakaian operasional {runId}`
44. Approver DU-093-21 menyetujui aset DU-093-9
45. Asset Admin DU-093-20 menjalankan Cancel Borrow atas baris aset DU-093-9 dengan opsi `Save as Draft to edit`
46. Verifikasi Draft baru berisi aset DU-093-9 terbentuk tanpa nomor BRW dengan Origin `Restored`
47. Verifikasi Custody aset DU-093-9 dilepas ke `Available` seperti Cancel biasa
48. Verifikasi BRW asal aset DU-093-9 tetap `Canceled` di tab History

### Timeout Not picked up membentuk Draft baru oleh sistem
49. Asset Admin DU-093-20 mengajukan BRW untuk aset DU-093-10 atas nama Borrower DU-093-22 dengan Duration `4 Day(s)` dan Purpose `Pemakaian operasional {runId}`
50. Approver DU-093-21 menyetujui aset DU-093-10
51. Waktu berlalu sampai batas `Not picked up` aset DU-093-10 terlewati
52. Job Transaction timeout berjalan
53. Verifikasi Draft baru berisi aset DU-093-10 terbentuk tanpa nomor BRW dengan Origin `Restored by system`
54. Verifikasi Custody aset DU-093-10 dilepas ke `Available`

### Save Draft, Add to Borrow Draft, dan Delete Draft tidak mengunci aset
55. Asset Admin DU-093-20 menyimpan Draft berisi aset DU-093-11 untuk Borrower DU-093-22
56. Verifikasi Draft berisi aset DU-093-11 tersimpan dengan Last Updated dan Modified By terisi
57. Verifikasi Custody aset DU-093-11 tidak berubah dari `Available` sesudah Save Draft
58. Asset Admin DU-093-20 menjalankan `Add to Borrow Draft` untuk aset DU-093-11 dan aset DU-093-12 ke Draft Borrower DU-093-22
59. Verifikasi Total Asset Draft bertambah satu dan aset DU-093-11 yang sudah ada dilewati, dengan Modified By dan Last Updated terbarui
60. Verifikasi Custody aset DU-093-12 tidak berubah dari `Available` sesudah Add to Borrow Draft
61. Asset Admin DU-093-20 menghapus Draft berisi aset DU-093-11 dan aset DU-093-12
62. Verifikasi Draft terhapus dan Custody aset DU-093-11 dan aset DU-093-12 tidak berubah dari `Available`

### Report Damaged saat dipinjam
63. Borrower DU-093-22 melaporkan kerusakan aset DU-093-13 dengan Description `Layar retak di pojok kiri bawah {runId}`
64. Verifikasi record laporan untuk aset DU-093-13 berstatus `Waiting for Confirmation` dan Condition aset DU-093-13 berubah menjadi `Damaged`
65. Verifikasi baris aset DU-093-13 tetap `Borrowed` dengan badge `Reported Damaged`
66. Asset Admin DU-093-20 menjalankan Extend aset DU-093-13 dengan Extend duration `2 Day(s)`
67. Verifikasi Extend aset DU-093-13 ditolak karena ada laporan kerusakan
68. Verifikasi Extension aset DU-093-13 yang menunggu otomatis `Canceled` dengan alasan `Damage reported`
69. Asset Admin DU-093-20 menerima kembali aset DU-093-13 dengan Condition `Normal`
70. Verifikasi penanda `Damaged` aset DU-093-13 mengikuti record laporan kerusakan sampai final
71. Verifikasi Return aset DU-093-13 tidak membuat laporan kerusakan baru

### Report Missing oleh Borrower dan oleh Aktor yang berhak
72. Borrower DU-093-22 melaporkan kehilangan aset DU-093-14 dengan Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`
73. Verifikasi Condition aset DU-093-14 berubah menjadi `Missing` dan baris aset DU-093-14 tetap `Borrowed` dengan badge `Reported Missing`
74. Aktor yang berhak atas laporan kehilangan DU-093-24 melaporkan kehilangan aset DU-093-15 dengan Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`
75. Verifikasi baris aset DU-093-15 ditutup `Returned` dengan penanda `Missing`

### Report TAG lewat identifikasi manual
76. Asset Admin DU-093-20 menjalankan `I Can't Scan the TAG` saat menyerahkan aset DU-093-16
77. Verifikasi laporan TAG aset DU-093-16 masuk ke antrean Reported TAGs
78. Verifikasi Borrow Log aset DU-093-16 memuat node `TAG reported by [Reporter]`

### Cancel Extension membatalkan pengajuan tanpa mengubah Due date
79. Asset Admin DU-093-20 menjalankan Cancel Extension atas Extension aset DU-093-17
80. Verifikasi Extension aset DU-093-17 berstatus `Canceled`
81. Verifikasi Due date dan jumlah Extend aset DU-093-17 tidak berubah dan status baris kembali diturunkan dari baris
82. Verifikasi pengajuan Extension aset DU-093-17 hilang dari antrean Active approver yang tidak punya aset tersisa

### Borrower dinonaktifkan membatalkan baris menunggu dan menahan exit clearance
83. Total Control menonaktifkan Borrower Borrower DU-093-23
84. Verifikasi baris aset DU-093-18 yang menunggu ditutup `Canceled` dan daftar Return Borrower DU-093-23 memuat aset DU-093-19
85. Verifikasi exit clearance Borrower DU-093-23 tertahan selama aset DU-093-19 belum dikembalikan

### Aturan sinkron downgrade ke None dan Mark as Returned
86. Verifikasi downgrade ke None di T-0 menutup baris menunggu sebagai `Canceled` oleh `System`, melepas Custody menjadi `Available`, dan menghapus Draft tanpa Draft baru serta tidak dipulihkan saat rollback atau upgrade
