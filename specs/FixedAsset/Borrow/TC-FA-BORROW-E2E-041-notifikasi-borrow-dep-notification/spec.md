---
id: TC-FA-BORROW-E2E-041-notifikasi-borrow-dep-notification
title: "Peristiwa Borrow memicu notifikasi ke penerima menurut katalog event"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["F-BORROW-16", "§9.2#b22", "§9.2#b23", "§9.8#p1", "§9.8#r1", "§9.8#r2", "§9.8#r3", "§9.8#r4", "§9.8#r5", "§9.8#r6", "§9.8#r7", "§9.8#r8", "§9.8#r9", "§9.8#r10", "§9.8#r11", "§9.8#r12", "§9.8#r13", "§9.8#r14", "§9.8#r15", "§9.8#r16", "§9.8#p2", "§9.8#p3"]
smoke: []
dependsOn: ["Notification: katalog event Borrow"]
trace:
  "F-BORROW-16": [11, 142]
  "§9.2#b22": [36, 153, 157]
  "§9.2#b23": [78, 80, 82, 166, 176]
  "§9.8#p1": [81, 82, 142]
  "§9.8#r1": [11, 21, 146, 149]
  "§9.8#r2": [25]
  "§9.8#r3": [34, 35]
  "§9.8#r4": [41, 42, 46, 50, 255, 259]
  "§9.8#r5": [54, 57, 58, 61]
  "§9.8#r6": [65, 66]
  "§9.8#r7": [142]
  "§9.8#r8": [142]
  "§9.8#r9": [70]
  "§9.8#r10": [86]
  "§9.8#r11": [90, 270]
  "§9.8#r12": [94, 97, 101, 225, 229, 233, 237]
  "§9.8#r13": [105]
  "§9.8#r14": [109, 112]
  "§9.8#r15": [119, 122, 241, 244, 247, 251]
  "§9.8#r16": [134, 137, 141]
  "§9.8#p2": [126, 130, 180, 184]
  "§9.8#p3": [14, 17, 28, 89, 115, 125, 187, 190, 194, 197, 201, 204, 208, 211, 216, 220, 221, 263, 266]
anchor: [45, 49, 175, 228, 236, 269]
coverage:
  web: automated
---

# Peristiwa Borrow memicu notifikasi ke penerima menurut katalog event

## Prerequisites
- Aktor: Aktor Borrow `Agus Pratama {runId}` (Asset Admin pada Group `Head Office`) yang melakukan aksi di halaman Borrow dan menerima notifikasi Aktor Borrow; ia bukan Borrower maupun PIC pada BRW di spec ini. Penerima yang diamati bergantian: Approver `Budi Santoso {runId}` (DU-041-4), Borrower `Hendra Kusuma {runId}` (DU-041-1), PIC `Rudi Hartono {runId}` (DU-041-3), pengaju `Lina Sari {runId}` (DU-041-5), dan penerima laporan `Siti Rahma {runId}` (DU-041-6). Borrower tanpa akun login `Joko Susilo {runId}` (DU-041-2) menerima email Borrower. Penerima tambahan: Approver kedua `Wati Rahayu {runId}` (DU-041-32), Aktor Borrow pemegang hak Aktor Damaged `Dian Anggraini {runId}` (DU-041-33), dan Borrower tanpa akun dan tanpa Email `Wawan Setiawan {runId}` (DU-041-38).
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-041-1: karyawan `Hendra Kusuma {runId}` dengan akun login, Email `hendra.kusuma{runId}@example.com`, Status `Active`.
  - DU-041-2: karyawan tanpa akun login `Joko Susilo {runId}`, Email `joko.susilo{runId}@example.com`, PIC `Rudi Hartono {runId}` (aktif), Status `Active`.
  - DU-041-3: karyawan `Rudi Hartono {runId}`, Email `rudi.hartono{runId}@example.com`, Asset Admin pada Group `Head Office`, Status `Active`.
  - DU-041-4: karyawan `Budi Santoso {runId}`, Approver pada Group `Head Office`, Status `Active`.
  - DU-041-5: karyawan `Lina Sari {runId}`, Asset Admin pada Group `Head Office`, Status `Active`.
  - DU-041-6: karyawan `Siti Rahma {runId}`, Group Manager pada Group `Head Office`, Status `Active`.
  - DU-041-7: Draft Borrower `Hendra Kusuma {runId}` berisi aset `Laptop Dell XPS {runId}`, Approval `Needs approval`, Duration `2 days`, Purpose `Rapat evaluasi bulanan`.
  - DU-041-8: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Proyektor Epson EB-W06 {runId}`, Approval Extend `Needs approval`, Due date T0 + 1 hari.
  - DU-041-9: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Meja Lipat Informa {runId}`, Self service `OFF` pada snapshot baris, Due date T0 + 2 hari.
  - DU-041-10: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Monitor LG UltraWide {runId}`; Approver `Budi Santoso {runId}` eligible.
  - DU-041-11: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Keyboard Logitech MX Keys {runId}`; Approver `Budi Santoso {runId}` eligible.
  - DU-041-12: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Mouse Logitech MX Master {runId}`; Approver `Budi Santoso {runId}` eligible.
  - DU-041-13: Draft Borrower `Hendra Kusuma {runId}` berisi aset `Webcam Logitech C920 {runId}`, Approval `Auto-approve`, Duration `1 days`, Purpose `Rekaman rapat`.
  - DU-041-14: BRW `Borrowed` Borrower `Hendra Kusuma {runId}` dengan tiga pengajuan Extension yang menunggu approval `Budi Santoso {runId}` untuk aset `Tablet Lenovo Tab P11 {runId}`, `Speaker Bose S1 Pro {runId}`, dan `Printer HP LaserJet Pro {runId}`.
  - DU-041-15: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, aset `Scanner Canon DR-C225 {runId}`, satu hari sebelum batas Transaction timeout.
  - DU-041-16: BRW `Waiting for Handover` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, aset `Shredder Fellowes 99Ci {runId}`, satu hari sebelum batas pengambilan.
  - DU-041-17: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, aset `Drone DJI Mini 4 {runId}`, melewati batas Transaction timeout.
  - DU-041-18: BRW `Waiting for Handover` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, aset `Genset Honda EU22i {runId}`, melewati batas pengambilan.
  - DU-041-21: BRW `Waiting for Handover` Borrower `Joko Susilo {runId}`, PIC `Rudi Hartono {runId}`, Requested By `Agus Pratama {runId}`, aset `Kamera Sony A7C {runId}`.
  - DU-041-22: BRW `Waiting for Handover` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, Photo at start OFF, aset `Handycam Sony FDR {runId}`.
  - DU-041-23: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, aset `Lampu Studio Godox {runId}`; Approver `Budi Santoso {runId}` belum bertindak.
  - DU-041-24: BRW `Waiting for Handover` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Tripod Manfrotto {runId}`.
  - DU-041-25: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Mikrofon Shure SM58 {runId}`, baris Days dengan Due date T0 + 1 hari.
  - DU-041-26: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Radio Handy Motorola {runId}`, Due date T0 - 1 hari.
  - DU-041-27: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Kursi Ergonomis Ergotrend {runId}`, Due date T0 + 3 hari.
  - DU-041-28: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Meja Kerja Lipat {runId}`, Due date T0 + 3 hari.
  - DU-041-29: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, Photo at end OFF, aset `Handheld Zebra TC21 {runId}`.
  - DU-041-30: BRW pinjaman self-service `Borrowed` Borrower `Hendra Kusuma {runId}`, Photo at end ON, aset `Tas Kamera Lowepro {runId}`.
  - DU-041-31: isian Extend: Extend By `2`, Reason `Proyek belum selesai`.
  - DU-041-32: karyawan `Wati Rahayu {runId}`, Approver pada Group `Head Office`, Status `Active`.
  - DU-041-33: karyawan `Dian Anggraini {runId}`, Asset Admin dengan hak Aktor Damaged pada Group `Head Office`, Status `Active`.
  - DU-041-34: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Pemotong Kertas Krisbow {runId}`; Approver `Budi Santoso {runId}` eligible.
  - DU-041-35: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Laminator Fellowes {runId}`; Approver `Budi Santoso {runId}` eligible.
  - DU-041-36: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Stapler Max HD {runId}`; Approver `Budi Santoso {runId}` eligible.
  - DU-041-37: BRW `Waiting for Handover` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, berisi dua baris aset `Proyektor Optoma {runId}` dan `Layar Proyektor Screenpro {runId}`.
  - DU-041-38: karyawan tanpa akun login `Wawan Setiawan {runId}`, tanpa Email, PIC `Rudi Hartono {runId}` (aktif), Status `Active`.
  - DU-041-39: BRW `Waiting for Handover` Borrower `Wawan Setiawan {runId}`, PIC `Rudi Hartono {runId}`, Requested By `Agus Pratama {runId}`, aset `Kabel Roll Uticon {runId}`.
  - DU-041-40: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Radio Panggil Icom {runId}`.
  - DU-041-41: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, aset `Rak Besi Lion {runId}`; Approver `Budi Santoso {runId}` belum bertindak.
  - DU-041-42: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Mesin Fotokopi Ricoh {runId}`, Self service `OFF` pada snapshot baris, Due date T0 + 2 hari.
  - DU-041-43: BRW `Waiting for Handover` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, Photo at start OFF, aset `Kipas Angin Cosmos {runId}`.
  - DU-041-44: BRW `Overdue` Borrower `Hendra Kusuma {runId}`, aset `Sepeda Listrik Selis {runId}`, Due date T0 - 1 hari, Approval Extend `Auto-approve`.
  - DU-041-45: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Mesin Kopi Delonghi {runId}`.
  - DU-041-46: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Dispenser Sharp {runId}`.
  - DU-041-47: Draft Borrower `Hendra Kusuma {runId}` berisi aset `Meja Rapat Olympic {runId}` (Approver `Budi Santoso {runId}`) dan aset `Kursi Rapat Chitose {runId}` (Approver `Budi Santoso {runId}` dan `Wati Rahayu {runId}`), Approval `Needs approval`, Duration `2 days`, Purpose `Rapat evaluasi bulanan`.
  - DU-041-48: BRW `Waiting for Handover` Borrower tanpa akun `Joko Susilo {runId}`, PIC `Rudi Hartono {runId}`, Requested By `Agus Pratama {runId}`, aset `Gerobak Sorong Krisbow {runId}`.
  - DU-041-49: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, berisi aset `Whiteboard Sakura {runId}` (sudah disetujui `Wati Rahayu {runId}`) dan aset `Proyektor Viewsonic {runId}` (Approver `Budi Santoso {runId}` belum bertindak).
  - DU-041-50: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Lemari Arsip Brother {runId}`.
  - DU-041-51: BRW `Borrowed` Borrower tanpa akun `Joko Susilo {runId}`, PIC `Rudi Hartono {runId}`, aset `Genset Yanmar YDG {runId}`.
  - DU-041-52: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Mesin Pemotong Rumput Honda {runId}`.
  - DU-041-53: BRW `Extension Request` Borrower `Hendra Kusuma {runId}`, aset `Genset Kipor {runId}`, Extend By `2 days`, Reason `Proyek belum selesai`, menunggu review.
  - DU-041-54: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Pompa Air Shimizu {runId}`, Extension menunggu approval `Budi Santoso {runId}`.
  - DU-041-55: isian penolakan review Extend: Approval Note `Kebutuhan proyek belum mendesak`.
  - DU-041-56: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Proyektor BenQ MX550 {runId}`, Self service `OFF` pada snapshot baris, Due date T0 + 2 hari.
- Kondisi:
  - Switch Send email notifications untuk Borrow bernilai ON.

## Test Steps

### Submit dan Extend yang butuh approval memicu borrow_waiting_approval ke Approver
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Klik tab `Drafts` pada halaman Borrow
4. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
5. Klik menu ⋯ pada Draft milik Borrower `Hendra Kusuma {runId}` berisi DU-041-7
6. Klik `Edit`
7. Klik `[Submit]`
8. Klik `[Submit]` pada dialog `Submit Borrow`
9. Masuk sebagai `Budi Santoso {runId}`
10. Klik ikon notifikasi pada navbar
11. Verifikasi notifikasi bertipe `borrow_waiting_approval` varian `Borrow` diterima Approver `Budi Santoso {runId}` untuk BRW hasil Submit DU-041-7
12. Klik `[Detail]` pada notifikasi `borrow_waiting_approval`
13. Tinggalkan halaman keputusan tanpa memutuskan
14. Verifikasi notifikasi `borrow_waiting_approval` tetap Unread karena Approver belum memutuskan
15. Approver `Budi Santoso {runId}` menyetujui aset `Laptop Dell XPS {runId}` pada pengajuan BRW hasil Submit DU-041-7
16. Muat ulang halaman
17. Verifikasi notifikasi `borrow_waiting_approval` berubah menjadi Read karena Approver tidak punya lagi aset yang belum diputuskan di pengajuan itu
18. Aktor Borrow `Agus Pratama {runId}` mengajukan Extend aset `Proyektor Epson EB-W06 {runId}` pada BRW DU-041-8 dengan Extend By `2` dan Reason `Proyek belum selesai`
19. Masuk sebagai `Budi Santoso {runId}`
20. Klik ikon notifikasi pada navbar
21. Verifikasi notifikasi bertipe `borrow_waiting_approval` varian `Extension` diterima Approver `Budi Santoso {runId}` untuk aset `Proyektor Epson EB-W06 {runId}`

### Extend dari Borrower menunggu review memicu borrow_extension_review ke Aktor Borrow
22. Borrower `Hendra Kusuma {runId}` mengajukan Extend aset `Meja Lipat Informa {runId}` pada BRW DU-041-9 dengan Extend By `2` dan Reason `Proyek belum selesai`
23. Masuk sebagai `Agus Pratama {runId}`
24. Klik ikon notifikasi pada navbar
25. Verifikasi notifikasi bertipe `borrow_extension_review` diterima Aktor Borrow `Agus Pratama {runId}` untuk aset `Meja Lipat Informa {runId}`
26. Aktor Borrow `Agus Pratama {runId}` mengirim Review Extension Request untuk aset `Meja Lipat Informa {runId}`
27. Muat ulang halaman
28. Verifikasi notifikasi `borrow_extension_review` berubah menjadi Read karena Review Extension Request sudah dikirim

### Keputusan approval memicu borrow_resolved ke Borrower dan digabung per Borrower
29. Approver `Budi Santoso {runId}` menyetujui aset `Monitor LG UltraWide {runId}` pada BRW DU-041-10 dan aset `Keyboard Logitech MX Keys {runId}` pada BRW DU-041-11 pada hari yang sama
30. Approver `Budi Santoso {runId}` menolak aset `Mouse Logitech MX Master {runId}` pada BRW DU-041-12
31. Aktor Borrow `Agus Pratama {runId}` men-Submit Draft DU-041-13 yang Auto-approve
32. Masuk sebagai `Hendra Kusuma {runId}`
33. Klik ikon notifikasi pada navbar
34. Verifikasi notifikasi bertipe `borrow_resolved` varian `Approved` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Webcam Logitech C920 {runId}` yang Auto-approved
35. Verifikasi notifikasi bertipe `borrow_resolved` varian `Rejected` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Mouse Logitech MX Master {runId}`
36. Verifikasi BRW DU-041-10 dan BRW DU-041-11 yang disetujui pada hari yang sama digabung dalam satu notifikasi `borrow_resolved` untuk Borrower `Hendra Kusuma {runId}`

### Keputusan dan penutupan Extension memicu borrow_extension_resolved
37. Approver `Budi Santoso {runId}` menyetujui Extension aset `Tablet Lenovo Tab P11 {runId}` dan menolak Extension aset `Speaker Bose S1 Pro {runId}` pada BRW DU-041-14
38. Aktor Borrow `Agus Pratama {runId}` membatalkan Extension aset `Printer HP LaserJet Pro {runId}` pada BRW DU-041-14 lewat `Cancel Extension`
39. Masuk sebagai `Hendra Kusuma {runId}`
40. Klik ikon notifikasi pada navbar
41. Verifikasi notifikasi bertipe `borrow_extension_resolved` varian `Approved` diterima untuk aset `Tablet Lenovo Tab P11 {runId}`
42. Verifikasi notifikasi bertipe `borrow_extension_resolved` varian `Rejected` diterima untuk aset `Speaker Bose S1 Pro {runId}`
43. Masuk sebagai `Budi Santoso {runId}`
44. Klik ikon notifikasi pada navbar
45. Verifikasi notifikasi `borrow_extension_resolved` untuk aset `Tablet Lenovo Tab P11 {runId}` diterima Approver `Budi Santoso {runId}` sebagai hasil keputusannya sendiri
46. Verifikasi notifikasi bertipe `borrow_extension_resolved` varian `Canceled` diterima Approver `Budi Santoso {runId}` untuk aset `Printer HP LaserJet Pro {runId}` karena ia belum bertindak
47. Masuk sebagai `Agus Pratama {runId}`
48. Klik ikon notifikasi pada navbar
49. Verifikasi notifikasi `borrow_extension_review` untuk aset `Meja Lipat Informa {runId}` tetap tampil di daftar notifikasi `Agus Pratama {runId}`
50. Verifikasi tidak ada notifikasi tambahan untuk Aktor Borrow pengaju `Agus Pratama {runId}` atas pembatalan Extension aset `Printer HP LaserJet Pro {runId}`

### Peringatan Transaction timeout 1 hari lagi memicu borrow_almost_timeout
51. Job peringatan Transaction timeout 1 hari lagi berjalan untuk BRW DU-041-15 dan BRW DU-041-16
52. Masuk sebagai `Budi Santoso {runId}`
53. Klik ikon notifikasi pada navbar
54. Verifikasi notifikasi bertipe `borrow_almost_timeout` varian `Approver` diterima Approver `Budi Santoso {runId}` untuk BRW DU-041-15
55. Masuk sebagai `Lina Sari {runId}`
56. Klik ikon notifikasi pada navbar
57. Verifikasi notifikasi bertipe `borrow_almost_timeout` varian `Requester` diterima pengaju `Lina Sari {runId}` untuk BRW DU-041-15
58. Verifikasi notifikasi bertipe `borrow_almost_timeout` varian `PIC admin` diterima pengaju `Lina Sari {runId}` untuk pengingat batas pengambilan BRW DU-041-16
59. Masuk sebagai `Hendra Kusuma {runId}`
60. Klik ikon notifikasi pada navbar
61. Verifikasi Borrower `Hendra Kusuma {runId}` tidak menerima pengingat batas pengambilan untuk BRW DU-041-16

### Penutupan Canceled oleh sistem memicu borrow_auto_canceled
62. Job Transaction timeout berjalan untuk BRW DU-041-17 dan BRW DU-041-18
63. Masuk sebagai `Lina Sari {runId}`
64. Klik ikon notifikasi pada navbar
65. Verifikasi notifikasi bertipe `borrow_auto_canceled` varian `Approval timeout` diterima pengaju `Lina Sari {runId}` untuk BRW DU-041-17
66. Verifikasi notifikasi bertipe `borrow_auto_canceled` varian `Not picked up` diterima pengaju `Lina Sari {runId}` untuk BRW DU-041-18

### Baris menjadi Waiting for Handover dan Remind Borrower mengirim ulang borrow_ready_pickup
67. Aktor Borrow `Agus Pratama {runId}` menyetujui BRW DU-041-21 sehingga barisnya menjadi Waiting for Handover
68. Masuk sebagai `Rudi Hartono {runId}`
69. Klik ikon notifikasi pada navbar
70. Verifikasi notifikasi bertipe `borrow_ready_pickup` untuk Borrower tanpa akun `Joko Susilo {runId}` diterima PIC `Rudi Hartono {runId}` dan memuat Group tempat ambil, Duration, dan batas pengambilan
71. Aktor Borrow `Agus Pratama {runId}` klik `Transactions` pada sidebar
72. Klik `Borrow`
73. Ketik Search `Joko Susilo {runId}`, tekan Enter
74. Klik menu ⋯ pada baris BRW milik DU-041-21
75. Klik `Remind Borrower`
76. Masuk sebagai `Rudi Hartono {runId}`
77. Klik ikon notifikasi pada navbar
78. Verifikasi notifikasi `borrow_ready_pickup` kedua diterima PIC `Rudi Hartono {runId}` sebagai notifikasi terpisah yang tidak digabung dengan notifikasi lain
79. Buka Borrow Detail BRW milik DU-041-21 pada layar Aktor Borrow `Agus Pratama {runId}`
80. Verifikasi baris aset `Kamera Sony A7C {runId}` tetap `Waiting for Handover` dengan batas pengambilan yang sama dan Borrow Log aset itu tidak memuat node untuk Remind Borrower
81. Verifikasi email `borrow_ready_pickup` diterima PIC `Rudi Hartono {runId}` dengan Subject `[Title] · [Transaction ID]`, Body `Hi [Full Name],` berisi `Rudi Hartono {runId}`, tombol `[View Details]`, dan teks `On behalf of [Borrower Name]: you're receiving this because you're the PIC for [Borrower Name], who doesn't have a TAG Samurai account.` dengan [Borrower Name] berisi `Joko Susilo {runId}`
82. Verifikasi email `borrow_ready_pickup` juga diterima Borrower tanpa akun `Joko Susilo {runId}` pada `joko.susilo{runId}@example.com` dengan teks `You're receiving this email because email notifications are turned on for [Transaction Type] transactions in your company.` dengan [Transaction Type] berisi `Borrow`

### Handover memicu borrow_confirmation_required lalu borrow_handover_completed
83. Aktor Borrow `Agus Pratama {runId}` memulai Hand Over BRW DU-041-22 dan menekan `[Request Confirmation]`
84. Masuk sebagai `Hendra Kusuma {runId}`
85. Klik ikon notifikasi pada navbar
86. Verifikasi notifikasi bertipe `borrow_confirmation_required` diterima Borrower `Hendra Kusuma {runId}` untuk BRW DU-041-22
87. Borrower `Hendra Kusuma {runId}` menyelesaikan konfirmasi handover aset `Handycam Sony FDR {runId}`
88. Muat ulang halaman
89. Verifikasi notifikasi `borrow_confirmation_required` berubah menjadi Read karena Borrower menyelesaikan konfirmasi
90. Verifikasi notifikasi bertipe `borrow_handover_completed` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Handycam Sony FDR {runId}`

### Cancel Borrow memicu borrow_canceled ke pihak yang bukan pelakunya
91. Aktor Borrow `Agus Pratama {runId}` membatalkan BRW DU-041-23 lewat `Cancel Borrow`
92. Masuk sebagai `Hendra Kusuma {runId}`
93. Klik ikon notifikasi pada navbar
94. Verifikasi notifikasi bertipe `borrow_canceled` diterima Borrower `Hendra Kusuma {runId}` karena bukan pelaku pembatalan BRW DU-041-23
95. Masuk sebagai `Budi Santoso {runId}`
96. Klik ikon notifikasi pada navbar
97. Verifikasi notifikasi bertipe `borrow_canceled` diterima Approver `Budi Santoso {runId}` yang belum bertindak untuk BRW DU-041-23
98. Borrower `Hendra Kusuma {runId}` membatalkan baris aset `Tripod Manfrotto {runId}` pada BRW DU-041-24 atas pinjamannya sendiri
99. Masuk sebagai `Agus Pratama {runId}`
100. Klik ikon notifikasi pada navbar
101. Verifikasi notifikasi bertipe `borrow_canceled` diterima Aktor Borrow Group asal `Agus Pratama {runId}` karena Borrower yang membatalkan BRW DU-041-24

### Job Due date dan Overdue memicu borrow_due_soon dan borrow_overdue
102. Job harian Due date reminders berjalan pukul 00:00 zona waktu penyewa untuk baris Days pada BRW DU-041-25
103. Masuk sebagai `Hendra Kusuma {runId}`
104. Klik ikon notifikasi pada navbar
105. Verifikasi notifikasi bertipe `borrow_due_soon` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Mikrofon Shure SM58 {runId}`
106. Baris aset `Radio Handy Motorola {runId}` pada BRW DU-041-26 menjadi Overdue pada H+1
107. Masuk sebagai `Hendra Kusuma {runId}`
108. Klik ikon notifikasi pada navbar
109. Verifikasi notifikasi bertipe `borrow_overdue` varian Borrower diterima Borrower `Hendra Kusuma {runId}` untuk aset `Radio Handy Motorola {runId}`
110. Masuk sebagai `Agus Pratama {runId}`
111. Klik ikon notifikasi pada navbar
112. Verifikasi notifikasi bertipe `borrow_overdue` varian Aktor Borrow diterima `Agus Pratama {runId}` untuk aset `Radio Handy Motorola {runId}`
113. Return aset `Radio Handy Motorola {runId}` diselesaikan Aktor Borrow `Agus Pratama {runId}`
114. Muat ulang halaman
115. Verifikasi notifikasi `borrow_overdue` varian Aktor Borrow berubah menjadi Read karena baris itu dikembalikan

### Laporan kerusakan dan kehilangan saat dipinjam memicu borrow_damage_reported dan event modul lain
116. Borrower `Hendra Kusuma {runId}` mengirim laporan kerusakan aset `Kursi Ergonomis Ergotrend {runId}` pada BRW DU-041-27
117. Masuk sebagai `Agus Pratama {runId}`
118. Klik ikon notifikasi pada navbar
119. Verifikasi notifikasi bertipe `borrow_damage_reported` varian Aktor Borrow diterima `Agus Pratama {runId}` untuk aset `Kursi Ergonomis Ergotrend {runId}`
120. Masuk sebagai `Siti Rahma {runId}`
121. Klik ikon notifikasi pada navbar
122. Verifikasi notifikasi bertipe `borrow_damage_reported` varian Aktor penerima laporan dengan status Waiting for Confirmation diterima `Siti Rahma {runId}`
123. Aktor penerima laporan `Siti Rahma {runId}` mengonfirmasi laporan kerusakan aset `Kursi Ergonomis Ergotrend {runId}`
124. Muat ulang halaman
125. Verifikasi notifikasi `borrow_damage_reported` varian Aktor penerima laporan berubah menjadi Read karena laporan sudah dikonfirmasi
126. Verifikasi notifikasi bertipe `damaged_review_resolved` untuk aset `Kursi Ergonomis Ergotrend {runId}` diterima pelapor `Hendra Kusuma {runId}` sesudah laporannya dikonfirmasi, sebagai event milik modul laporan kerusakan
127. Borrower `Hendra Kusuma {runId}` mengirim laporan kehilangan aset `Meja Kerja Lipat {runId}` pada BRW DU-041-28
128. Masuk sebagai `Siti Rahma {runId}`
129. Klik ikon notifikasi pada navbar
130. Verifikasi notifikasi bertipe `missing_holder_reported` diterima `Siti Rahma {runId}` untuk aset `Meja Kerja Lipat {runId}` sebagai event milik modul laporan kehilangan

### Return memicu borrow_returned ke Borrower, pengaju, dan Review
131. Aktor Borrow `Agus Pratama {runId}` menerima Return aset `Handheld Zebra TC21 {runId}` pada BRW DU-041-29
132. Masuk sebagai `Hendra Kusuma {runId}`
133. Klik ikon notifikasi pada navbar
134. Verifikasi notifikasi bertipe `borrow_returned` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Handheld Zebra TC21 {runId}`
135. Masuk sebagai `Lina Sari {runId}`
136. Klik ikon notifikasi pada navbar
137. Verifikasi notifikasi bertipe `borrow_returned` diterima pengaju `Lina Sari {runId}` karena berbeda dari pelaku Return dan Borrower
138. Borrower `Hendra Kusuma {runId}` mengembalikan sendiri aset `Tas Kamera Lowepro {runId}` pada BRW self-service DU-041-30 dengan foto return
139. Masuk sebagai `Agus Pratama {runId}`
140. Klik ikon notifikasi pada navbar
141. Verifikasi notifikasi `Review` bertipe `borrow_returned` diterima Aktor Borrow Group asal `Agus Pratama {runId}` dan memuat foto handover dan foto return
142. Verifikasi katalog event, penerima, Title, Body, dan path setiap notifikasi di atas mengikuti katalog event modul Notification dan bukan didefinisikan ulang oleh Borrow

### borrow_waiting_approval dikirim sekali per pengajuan ke setiap approver dari minimal satu aset
143. Aktor Borrow `Agus Pratama {runId}` men-Submit Draft DU-041-47
144. Masuk sebagai `Budi Santoso {runId}`
145. Klik ikon notifikasi pada navbar
146. Verifikasi Approver `Budi Santoso {runId}` menerima satu notifikasi `borrow_waiting_approval` untuk seluruh pengajuan BRW hasil Submit DU-041-47 yang memuat aset `Meja Rapat Olympic {runId}` dan aset `Kursi Rapat Chitose {runId}`, bukan satu notifikasi per aset
147. Masuk sebagai `Wati Rahayu {runId}`
148. Klik ikon notifikasi pada navbar
149. Verifikasi notifikasi `borrow_waiting_approval` untuk pengajuan BRW hasil Submit DU-041-47 diterima Approver `Wati Rahayu {runId}` karena ia approver dari aset `Kursi Rapat Chitose {runId}`

### borrow_ready_pickup digabung per Borrower pada hari yang sama dan tidak digabung pada hari berbeda
150. Approver `Budi Santoso {runId}` menyetujui aset `Pemotong Kertas Krisbow {runId}` pada BRW DU-041-34 dan aset `Laminator Fellowes {runId}` pada BRW DU-041-35 pada hari yang sama
151. Masuk sebagai `Hendra Kusuma {runId}`
152. Klik ikon notifikasi pada navbar
153. Verifikasi BRW DU-041-34 dan BRW DU-041-35 yang siap diambil pada hari yang sama digabung dalam satu notifikasi `borrow_ready_pickup` untuk Borrower `Hendra Kusuma {runId}`
154. Waktu berlalu sampai hari berikutnya
155. Approver `Budi Santoso {runId}` menyetujui aset `Stapler Max HD {runId}` pada BRW DU-041-36
156. Muat ulang halaman
157. Verifikasi notifikasi `borrow_ready_pickup` untuk aset `Stapler Max HD {runId}` berdiri sendiri dan tidak digabung dengan notifikasi `borrow_ready_pickup` pada hari sebelumnya

### Remind Borrower mengirim ulang borrow_ready_pickup ke Borrower dengan akun untuk beberapa baris
158. Masuk sebagai `Agus Pratama {runId}`
159. Klik `Transactions` pada sidebar
160. Klik `Borrow`
161. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
162. Klik menu ⋯ pada baris BRW milik DU-041-37
163. Klik `Remind Borrower`
164. Masuk sebagai `Hendra Kusuma {runId}`
165. Klik ikon notifikasi pada navbar
166. Verifikasi notifikasi `borrow_ready_pickup` untuk BRW DU-041-37 dengan baris aset `Proyektor Optoma {runId}` dan `Layar Proyektor Screenpro {runId}` diterima langsung oleh Borrower `Hendra Kusuma {runId}` sebagai notifikasi terpisah yang tidak digabung dengan notifikasi lain

### Remind Borrower untuk Borrower tanpa akun dan tanpa Email hanya mengirim ke PIC
167. Masuk sebagai `Agus Pratama {runId}`
168. Klik `Transactions` pada sidebar
169. Klik `Borrow`
170. Ketik Search `Wawan Setiawan {runId}`, tekan Enter
171. Klik menu ⋯ pada baris BRW milik DU-041-39
172. Klik `Remind Borrower`
173. Masuk sebagai `Rudi Hartono {runId}`
174. Klik ikon notifikasi pada navbar
175. Verifikasi notifikasi `borrow_ready_pickup` untuk Borrower tanpa akun `Wawan Setiawan {runId}` diterima PIC `Rudi Hartono {runId}`
176. Verifikasi tidak ada email `borrow_ready_pickup` untuk Borrower tanpa akun `Wawan Setiawan {runId}` dalam 5 detik karena ia tidak punya Email

### Laporan kehilangan oleh Aktor Borrow dan hasil laporan Borrower memicu event modul laporan kehilangan
177. Aktor Borrow `Agus Pratama {runId}` mengirim laporan kehilangan aset `Radio Panggil Icom {runId}` pada BRW DU-041-40
178. Masuk sebagai `Siti Rahma {runId}`
179. Klik ikon notifikasi pada navbar
180. Verifikasi notifikasi bertipe `missing_reported` diterima `Siti Rahma {runId}` untuk aset `Radio Panggil Icom {runId}` sebagai event milik modul laporan kehilangan
181. Aktor penerima laporan `Siti Rahma {runId}` menolak laporan kehilangan aset `Meja Kerja Lipat {runId}` pada BRW DU-041-28
182. Masuk sebagai `Hendra Kusuma {runId}`
183. Klik ikon notifikasi pada navbar
184. Verifikasi notifikasi bertipe `missing_holder_resolved` diterima pelapor `Hendra Kusuma {runId}` untuk aset `Meja Kerja Lipat {runId}` sebagai event milik modul laporan kehilangan

### borrow_waiting_approval berubah Read saat pengajuan dibatalkan
185. Masuk sebagai `Budi Santoso {runId}`
186. Klik ikon notifikasi pada navbar
187. Verifikasi notifikasi `borrow_waiting_approval` untuk BRW DU-041-41 berstatus Unread karena Approver belum memutuskan
188. Aktor Borrow `Agus Pratama {runId}` membatalkan BRW DU-041-41 lewat `Cancel Borrow`
189. Muat ulang halaman
190. Verifikasi notifikasi `borrow_waiting_approval` untuk BRW DU-041-41 berubah menjadi Read karena pengajuan dibatalkan

### borrow_extension_review berubah Read saat Aktor Borrow lain mengirim review
191. Borrower `Hendra Kusuma {runId}` mengajukan Extend aset `Mesin Fotokopi Ricoh {runId}` pada BRW DU-041-42 dengan Extend By `2` dan Reason `Proyek belum selesai`
192. Masuk sebagai `Agus Pratama {runId}`
193. Klik ikon notifikasi pada navbar
194. Verifikasi notifikasi `borrow_extension_review` untuk aset `Mesin Fotokopi Ricoh {runId}` berstatus Unread di daftar `Agus Pratama {runId}`
195. Aktor Borrow `Lina Sari {runId}` mengirim Review Extension Request untuk aset `Mesin Fotokopi Ricoh {runId}`
196. Muat ulang halaman
197. Verifikasi notifikasi `borrow_extension_review` untuk aset `Mesin Fotokopi Ricoh {runId}` berubah menjadi Read di daftar `Agus Pratama {runId}` karena review dikirim Aktor Borrow lain

### borrow_confirmation_required berubah Read saat handover dibatalkan
198. Aktor Borrow `Agus Pratama {runId}` memulai Hand Over BRW DU-041-43 dan menekan `[Request Confirmation]`
199. Masuk sebagai `Hendra Kusuma {runId}`
200. Klik ikon notifikasi pada navbar
201. Verifikasi notifikasi `borrow_confirmation_required` untuk BRW DU-041-43 berstatus Unread karena Borrower belum mengonfirmasi
202. Aktor Borrow `Agus Pratama {runId}` menekan `[Cancel Request]` pada popup `Waiting for Confirmation`
203. Muat ulang halaman
204. Verifikasi notifikasi `borrow_confirmation_required` untuk BRW DU-041-43 berubah menjadi Read karena handover dibatalkan

### borrow_overdue varian Aktor Borrow berubah Read saat baris di-Extend
205. Baris aset `Sepeda Listrik Selis {runId}` pada BRW DU-041-44 menjadi Overdue pada H+1
206. Masuk sebagai `Agus Pratama {runId}`
207. Klik ikon notifikasi pada navbar
208. Verifikasi notifikasi `borrow_overdue` varian Aktor Borrow untuk aset `Sepeda Listrik Selis {runId}` berstatus Unread
209. Aktor Borrow `Agus Pratama {runId}` mengajukan Extend aset `Sepeda Listrik Selis {runId}` pada BRW DU-041-44 dengan Extend By `2` dan Reason `Proyek belum selesai` sehingga langsung berlaku
210. Muat ulang halaman
211. Verifikasi notifikasi `borrow_overdue` varian Aktor Borrow untuk aset `Sepeda Listrik Selis {runId}` berubah menjadi Read karena baris itu di-Extend

### borrow_damage_reported berubah Read saat laporan ditolak atau dibatalkan pelapor
212. Borrower `Hendra Kusuma {runId}` mengirim laporan kerusakan aset `Mesin Kopi Delonghi {runId}` pada BRW DU-041-45
213. Borrower `Hendra Kusuma {runId}` mengirim laporan kerusakan aset `Dispenser Sharp {runId}` pada BRW DU-041-46
214. Masuk sebagai `Siti Rahma {runId}`
215. Klik ikon notifikasi pada navbar
216. Verifikasi notifikasi `borrow_damage_reported` varian Aktor penerima laporan untuk aset `Mesin Kopi Delonghi {runId}` dan aset `Dispenser Sharp {runId}` berstatus Unread
217. Aktor penerima laporan `Siti Rahma {runId}` menolak laporan kerusakan aset `Mesin Kopi Delonghi {runId}`
218. Borrower `Hendra Kusuma {runId}` membatalkan laporan kerusakan aset `Dispenser Sharp {runId}` lewat `Cancel Damage Report`
219. Muat ulang halaman
220. Verifikasi notifikasi `borrow_damage_reported` varian Aktor penerima laporan untuk aset `Mesin Kopi Delonghi {runId}` berubah menjadi Read karena laporan ditolak
221. Verifikasi notifikasi `borrow_damage_reported` varian Aktor penerima laporan untuk aset `Dispenser Sharp {runId}` berubah menjadi Read karena laporan dibatalkan pelapor

### borrow_canceled ke Aktor Borrow Group asal saat PIC yang membatalkan
222. PIC `Rudi Hartono {runId}` membatalkan baris aset `Gerobak Sorong Krisbow {runId}` pada BRW DU-041-48 atas nama Borrower tanpa akun `Joko Susilo {runId}` dari halaman pinjamannya
223. Masuk sebagai `Agus Pratama {runId}`
224. Klik ikon notifikasi pada navbar
225. Verifikasi notifikasi bertipe `borrow_canceled` untuk BRW DU-041-48 diterima Aktor Borrow Group asal `Agus Pratama {runId}` karena PIC `Rudi Hartono {runId}` yang membatalkan

### Borrower pelaku pembatalan tidak menerima borrow_canceled
226. Masuk sebagai `Hendra Kusuma {runId}`
227. Klik ikon notifikasi pada navbar
228. Verifikasi notifikasi bertipe `borrow_canceled` untuk BRW DU-041-23 tampil di daftar notifikasi `Hendra Kusuma {runId}` karena ia bukan pelakunya
229. Verifikasi tidak ada notifikasi bertipe `borrow_canceled` untuk BRW DU-041-24 di daftar notifikasi `Hendra Kusuma {runId}` karena ia pelaku pembatalan

### Approver yang sudah bertindak tidak menerima borrow_canceled
230. Aktor Borrow `Agus Pratama {runId}` membatalkan BRW DU-041-49 lewat `Cancel Borrow`
231. Masuk sebagai `Budi Santoso {runId}`
232. Klik ikon notifikasi pada navbar
233. Verifikasi notifikasi bertipe `borrow_canceled` untuk BRW DU-041-49 diterima Approver `Budi Santoso {runId}` yang belum bertindak
234. Masuk sebagai `Wati Rahayu {runId}`
235. Klik ikon notifikasi pada navbar
236. Verifikasi notifikasi `borrow_waiting_approval` untuk pengajuan BRW hasil Submit DU-041-47 tampil di daftar notifikasi Approver `Wati Rahayu {runId}`
237. Verifikasi tidak ada notifikasi bertipe `borrow_canceled` untuk BRW DU-041-49 di daftar notifikasi Approver `Wati Rahayu {runId}` karena ia sudah bertindak

### borrow_damage_reported ke penerima menurut jalur pelapor
238. Aktor Borrow `Dian Anggraini {runId}` pemegang hak penerima laporan kerusakan mengirim laporan kerusakan aset `Lemari Arsip Brother {runId}` pada BRW DU-041-50 yang langsung terkonfirmasi tanpa menunggu konfirmasi
239. Masuk sebagai `Siti Rahma {runId}`
240. Klik ikon notifikasi pada navbar
241. Verifikasi notifikasi bertipe `borrow_damage_reported` varian Aktor penerima laporan untuk laporan yang langsung terkonfirmasi diterima `Siti Rahma {runId}` untuk aset `Lemari Arsip Brother {runId}`
242. PIC `Rudi Hartono {runId}` mengirim laporan kerusakan aset `Genset Yanmar YDG {runId}` pada BRW DU-041-51 atas nama Borrower tanpa akun `Joko Susilo {runId}` dari halaman pinjamannya
243. Muat ulang halaman
244. Verifikasi notifikasi bertipe `borrow_damage_reported` varian Aktor penerima laporan dengan status Waiting for Confirmation diterima `Siti Rahma {runId}` untuk aset `Genset Yanmar YDG {runId}` yang dilaporkan PIC
245. Masuk sebagai `Agus Pratama {runId}`
246. Klik ikon notifikasi pada navbar
247. Verifikasi notifikasi bertipe `borrow_damage_reported` varian Aktor Borrow diterima `Agus Pratama {runId}` untuk aset `Genset Yanmar YDG {runId}` yang dilaporkan PIC
248. Aktor Borrow `Agus Pratama {runId}` mengirim laporan kerusakan aset `Mesin Pemotong Rumput Honda {runId}` pada BRW DU-041-52 dari Borrow Detail
249. Masuk sebagai `Lina Sari {runId}`
250. Klik ikon notifikasi pada navbar
251. Verifikasi notifikasi bertipe `borrow_damage_reported` varian Aktor Borrow diterima Aktor Borrow `Lina Sari {runId}` untuk aset `Mesin Pemotong Rumput Honda {runId}` yang dilaporkan Aktor Borrow

### borrow_extension_resolved Rejected dari review My Asset dan Canceled otomatis karena laporan kehilangan
252. Aktor Borrow `Agus Pratama {runId}` menolak pengajuan Extend aset `Genset Kipor {runId}` pada BRW DU-041-53 lewat Review Extension Request dengan Approval Note `Kebutuhan proyek belum mendesak`
253. Masuk sebagai `Hendra Kusuma {runId}`
254. Klik ikon notifikasi pada navbar
255. Verifikasi notifikasi bertipe `borrow_extension_resolved` varian `Rejected` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Genset Kipor {runId}` dari hasil review pengajuan Extend yang diajukan Borrower sendiri
256. Borrower `Hendra Kusuma {runId}` mengirim laporan kehilangan aset `Pompa Air Shimizu {runId}` pada BRW DU-041-54 saat Extension aset itu menunggu approval
257. Masuk sebagai `Budi Santoso {runId}`
258. Klik ikon notifikasi pada navbar
259. Verifikasi notifikasi bertipe `borrow_extension_resolved` varian `Canceled` diterima Approver `Budi Santoso {runId}` untuk aset `Pompa Air Shimizu {runId}` karena Extension otomatis Canceled oleh laporan kehilangan dan ia belum bertindak

### borrow_extension_review berubah Read saat pengajuan Extend ditutup
260. Borrower `Hendra Kusuma {runId}` mengajukan Extend aset `Proyektor BenQ MX550 {runId}` pada BRW DU-041-56 dengan Extend By `2` dan Reason `Proyek belum selesai`
261. Masuk sebagai `Agus Pratama {runId}`
262. Klik ikon notifikasi pada navbar
263. Verifikasi notifikasi `borrow_extension_review` untuk aset `Proyektor BenQ MX550 {runId}` berstatus Unread di daftar `Agus Pratama {runId}` karena belum ada review yang dikirim
264. Borrower `Hendra Kusuma {runId}` membatalkan pengajuan Extend aset `Proyektor BenQ MX550 {runId}` lewat `Cancel Extension Request`
265. Muat ulang halaman
266. Verifikasi notifikasi `borrow_extension_review` untuk aset `Proyektor BenQ MX550 {runId}` berubah menjadi Read di daftar `Agus Pratama {runId}` karena pengajuannya ditutup

### borrow_handover_completed tidak dikirim untuk pinjaman self-service
267. Masuk sebagai `Hendra Kusuma {runId}`
268. Klik ikon notifikasi pada navbar
269. Verifikasi notifikasi bertipe `borrow_handover_completed` untuk aset `Handycam Sony FDR {runId}` tampil di daftar notifikasi `Hendra Kusuma {runId}`
270. Verifikasi tidak ada notifikasi bertipe `borrow_handover_completed` untuk aset `Tas Kamera Lowepro {runId}` pada BRW self-service DU-041-30 di daftar notifikasi `Hendra Kusuma {runId}` karena pinjaman self-service tidak memakai Handover
