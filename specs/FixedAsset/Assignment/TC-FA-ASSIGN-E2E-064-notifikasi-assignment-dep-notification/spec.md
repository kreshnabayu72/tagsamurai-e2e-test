---
id: TC-FA-ASSIGN-E2E-064-notifikasi-assignment-dep-notification
title: "Notifikasi event Assignment"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.8#p1", "§9.8#p2", "§9.8#r1", "§9.8#r2", "§9.8#r3", "§9.8#r4", "§9.8#r5", "§9.8#r6", "§9.8#r7", "§9.8#r8", "§9.8#r9", "§9.8#r10", "§9.8#r11", "§9.8#r12", "§9.8#r13", "§9.8#r14", F-ASSIGN-12, "§9.7#r19", EC-ASG-95, FI-ASG-87, "§9.10#r27", "§9.10#r28", "§9.10#p7"]
smoke: []
dependsOn: ["Notification: katalog notifikasi Assignment"]
trace:
  "§9.8#p1": [7, 43, 87, 196, 198]
  "§9.8#p2": [10, 12, 35, 84, 90, 116, 134, 156, 170, 180, 193]
  "§9.8#r1": [7, 111, 125]
  "§9.8#r2": [14, 118, 144]
  "§9.8#r3": [16, 21, 214]
  "§9.8#r4": [28, 153, 167]
  "§9.8#r5": 43
  "§9.8#r6": 52
  "§9.8#r7": 60
  "§9.8#r8": [67, 135, 137]
  "§9.8#r9": 70
  "§9.8#r10": [73, 75, 196, 201, 203]
  "§9.8#r11": 103
  "§9.8#r12": [82, 178, 188]
  "§9.8#r13": 87
  "§9.8#r14": 92
  F-ASSIGN-12: 7
  "§9.7#r19": 7
  EC-ASG-95: [94, 98, 100, 206, 212]
  FI-ASG-87: 52
  "§9.10#r27": 104
  "§9.10#r28": 103
  "§9.10#p7": 102
anchor: [205]
coverage:
  web: automated
---
# Notifikasi event Assignment

## Prerequisites
- Aktor: Aktor Assignment (Asset Admin `Dewi Lestari {runId}`, DU-064-1) sebagai pelaku utama dan pengaju; Asset Admin Group `Branch Surabaya` `Lina Marlina {runId}` (DU-064-2); Approver `Anton Pratama {runId}` (DU-064-3); Aktor Damaged `Nina Kartika {runId}` (DU-064-4); Admin pengguna (Total Control `Fajar Nugroho {runId}`, DU-064-5), yang juga pengaju ASG DU-064-36; serta Assignee dan PIC yang masing-masing membaca notifikasinya di sesinya sendiri.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-064-1: Karyawan `Dewi Lestari {runId}`, role Asset Admin, Group penugasan `Head Office`, Status `Active`.
  - DU-064-2: Karyawan `Lina Marlina {runId}`, role Asset Admin, Group penugasan `Branch Surabaya`, Status `Active`.
  - DU-064-3: Karyawan `Anton Pratama {runId}`, role Approver, Group penugasan `Head Office`, Status `Active`.
  - DU-064-4: Karyawan `Nina Kartika {runId}`, pemegang hak keputusan menu Damaged pada Group `Head Office`, Status `Active`.
  - DU-064-5: Karyawan `Fajar Nugroho {runId}`, role Total Control, Status `Active`.
  - DU-064-6: Karyawan `Budi Santoso {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee ASG DU-064-12, DU-064-17, dan DU-064-18.
  - DU-064-7: Karyawan `Rina Wijaya {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee ASG DU-064-14, DU-064-19, dan DU-064-38.
  - DU-064-8: Karyawan `Maya Putri {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee ASG DU-064-15.
  - DU-064-9: Karyawan `Tono Hartono {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee ASG DU-064-16 dan DU-064-37.
  - DU-064-10: Karyawan `Hendra Kusuma {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, anggota Division `Finance {runId}` dan `Operasional {runId}`, PIC Division `Finance {runId}`.
  - DU-064-11: Karyawan `Gita Maharani {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, PIC Division `Operasional {runId}`.
  - DU-064-12: Draft Assignee `Budi Santoso {runId}`, Group `Head Office`, berisi aset `Laptop Dell Latitude 7440 {runId}` dengan Purpose `Kerja harian`; approval dari `Anton Pratama {runId}`, Need recipient confirmation `Yes`, Photo at start `OFF`, Photo at end `OFF`.
  - DU-064-13: ASG `Waiting for Handover` untuk Assignee Division `Finance {runId}` dengan PIC `Hendra Kusuma {runId}`, Confirmation Rule `No`, berisi aset `Printer Brother MFC {runId}`.
  - DU-064-14: ASG `Waiting for Handover` untuk Assignee `Rina Wijaya {runId}` berisi aset `Tablet iPad 10 {runId}`.
  - DU-064-15: ASG `Waiting for Handover` untuk Assignee `Maya Putri {runId}` berisi aset `Kamera Canon M50 II {runId}`, Group `Head Office`, pengaju `Dewi Lestari {runId}`, Transaction timeout tinggal 1 hari.
  - DU-064-16: ASG `Waiting for Handover` untuk Assignee `Tono Hartono {runId}` berisi aset `Mouse Logitech M331 {runId}`, Group `Head Office`, pengaju `Dewi Lestari {runId}`, Transaction timeout sudah terlewati.
  - DU-064-17: ASG `Assigned` untuk Assignee `Budi Santoso {runId}` berisi aset `Headphone Sony WH-1000XM5 {runId}`, Group `Head Office`, pengaju `Dewi Lestari {runId}`, dengan laporan Missing `Waiting for Confirmation` milik pelapor `Budi Santoso {runId}`; Transaction timeout baris itu sudah terlewati.
  - DU-064-18: ASG `Assigned` untuk Assignee `Budi Santoso {runId}` berisi aset `Proyektor Epson EB-X49 {runId}`, tanpa laporan.
  - DU-064-19: ASG `Assigned` untuk Assignee `Rina Wijaya {runId}` berisi aset `Server Rack HP {runId}` dari Group `Head Office`, TAG terbaca.
  - DU-064-20: ASG `Assigned` untuk Assignee Division `Operasional {runId}` dengan PIC `Gita Maharani {runId}` berisi aset `Meja Standing Desk {runId}` dari Group `Head Office`, pengaju `Dewi Lestari {runId}`.
  - DU-064-21: Karyawan `Sinta Anggraini {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee Draft DU-064-22.
  - DU-064-22: Draft Assignee `Sinta Anggraini {runId}`, Group `Head Office`, berisi dua aset, `Monitor LG 27UL500 {runId}` dan `Keyboard Logitech K380 {runId}`, dengan Purpose `Kerja harian`; approval dari `Anton Pratama {runId}` untuk kedua aset, Need recipient confirmation `Yes`.
  - DU-064-24: Karyawan `Wulan Sari {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee Draft DU-064-25.
  - DU-064-25: Draft Assignee `Wulan Sari {runId}`, Group `Head Office`, berisi aset `Webcam Logitech C920 {runId}` dengan Purpose `Rapat daring`; approval dari `Anton Pratama {runId}`.
  - DU-064-26: Karyawan `Yusuf Hakim {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee Draft DU-064-27 serta ASG DU-064-31 dan DU-064-32.
  - DU-064-27: Draft Assignee `Yusuf Hakim {runId}`, Group `Head Office`, berisi aset `Printer Epson L3250 {runId}` dengan Purpose `Cetak dokumen`; Require approval `OFF` untuk aset itu.
  - DU-064-28: Karyawan `Dimas Prakoso {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee ASG DU-064-29 dan DU-064-30.
  - DU-064-29: ASG `Waiting for Handover` untuk Assignee `Dimas Prakoso {runId}` berisi aset `Scanner Epson DS-530 {runId}`, Group `Head Office`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-064-30: ASG `Waiting for Handover` untuk Assignee `Dimas Prakoso {runId}` berisi aset `Proyektor BenQ MH535 {runId}`, Group `Head Office`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-064-31: ASG `Assigned` untuk Assignee `Yusuf Hakim {runId}` berisi aset `Kursi Ergonomis Ergotec {runId}`, Group `Head Office`, tanpa laporan.
  - DU-064-32: ASG `Assigned` untuk Assignee `Yusuf Hakim {runId}` berisi aset `Router Mikrotik RB4011 {runId}`, Group `Head Office`, tanpa laporan.
  - DU-064-35: Karyawan `Okta Permana {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee ASG DU-064-36.
  - DU-064-36: ASG `Waiting for Handover` untuk Assignee `Okta Permana {runId}` berisi aset `Monitor Dell P2422H {runId}`, Group `Head Office`, pengaju `Fajar Nugroho {runId}`.
  - DU-064-38: ASG `Assigned` untuk Assignee `Rina Wijaya {runId}` berisi aset `Lemari Arsip Besi {runId}` dari Group `Branch Surabaya`, tanpa laporan.
  - DU-064-37: ASG `Waiting for Approval` untuk Assignee `Tono Hartono {runId}` berisi aset `Speaker JBL Flip 6 {runId}`, Group `Head Office`, pengaju `Dewi Lestari {runId}`, approval dari `Anton Pratama {runId}`, Transaction timeout sudah terlewati.
- Kondisi:
  - Akun semua Assignee, PIC, dan aktor aktif dan kredensialnya disediakan fase 2.
  - Level Feature Suite Assignment pada entitas ini `Full`.

## Test Steps

### Submit dengan baris Waiting for Approval mengirim notifikasi ke Approver
1. Dewi Lestari: Buka tab Drafts di halaman Transactions > Assignment
2. Dewi Lestari: Ketik Search `Laptop Dell Latitude 7440 {runId}`, tekan Enter
3. Dewi Lestari: Klik ikon `Edit` pada baris Draft untuk aset `Laptop Dell Latitude 7440 {runId}`
4. Dewi Lestari: Klik `[Submit]`
5. Dewi Lestari: Klik `[Submit]` pada dialog `Submit Assignment`
6. Anton Pratama: Buka daftar notifikasi lewat ikon Bell di navbar
7. Verifikasi notifikasi permintaan approval untuk aset `Laptop Dell Latitude 7440 {runId}` tampil di daftar notifikasi `Anton Pratama {runId}` berstatus `Unread`
8. Anton Pratama: Klik `[Detail]` pada notifikasi itu
9. Anton Pratama: Keluar dari halaman Approvals > Assignment tanpa memutuskan
10. Verifikasi notifikasi permintaan approval untuk aset `Laptop Dell Latitude 7440 {runId}` tetap `Unread` karena keputusan belum diambil

### Keputusan approval mengirim notifikasi ke Assignee dan menyelesaikan task approver
11. Anton Pratama: Setujui (Approve) aset `Laptop Dell Latitude 7440 {runId}` di halaman Approvals > Assignment
12. Verifikasi notifikasi permintaan approval untuk aset `Laptop Dell Latitude 7440 {runId}` berstatus `Read` di daftar notifikasi `Anton Pratama {runId}`
13. Budi Santoso: Buka daftar notifikasi lewat ikon Bell di navbar
14. Verifikasi notifikasi hasil keputusan approval untuk aset `Laptop Dell Latitude 7440 {runId}` tampil di daftar notifikasi Assignee `Budi Santoso {runId}`

### Baris Waiting for Handover mengirim notifikasi ke Assignee dan dikirim ulang lewat Remind Assignee
15. Budi Santoso: Buka daftar notifikasi lewat ikon Bell di navbar
16. Verifikasi tepat satu notifikasi siap diserahkan untuk aset `Laptop Dell Latitude 7440 {runId}` tampil di daftar notifikasi `Budi Santoso {runId}` sebelum `Remind Assignee`
17. Dewi Lestari: Buka tab Transactions di halaman Transactions > Assignment
18. Dewi Lestari: Ketik Search `Budi Santoso {runId}`, tekan Enter
19. Dewi Lestari: Klik `⋯` pada baris ASG Waiting for Handover untuk aset `Laptop Dell Latitude 7440 {runId}`
20. Dewi Lestari: Klik `Remind Assignee`
21. Verifikasi daftar notifikasi `Budi Santoso {runId}` yang dimuat ulang memuat dua notifikasi siap diserahkan untuk aset `Laptop Dell Latitude 7440 {runId}`, bertambah satu dari jumlah satu sebelum `Remind Assignee`

### Sesi Handover menunggu konfirmasi mengirim notifikasi ke Assignee dan selesai saat Confirm
22. Dewi Lestari: Klik `⋯` pada baris ASG Waiting for Handover untuk aset `Laptop Dell Latitude 7440 {runId}`
23. Dewi Lestari: Klik `Hand Over`
24. Dewi Lestari: Klik `[Verify Asset]`
25. Dewi Lestari: Pindai TAG aset `Laptop Dell Latitude 7440 {runId}`
26. Dewi Lestari: Klik `[Request Confirmation]`
27. Budi Santoso: Buka daftar notifikasi lewat ikon Bell di navbar
28. Verifikasi notifikasi permintaan konfirmasi handover untuk aset `Laptop Dell Latitude 7440 {runId}` tampil di daftar notifikasi `Budi Santoso {runId}` berstatus `Unread`
29. Budi Santoso: Buka My Asset lewat menu Profile
30. Budi Santoso: Buka tab `Task`
31. Budi Santoso: Klik Task `Confirm Handover`
32. Budi Santoso: Centang pernyataan tanggung jawab
33. Budi Santoso: Klik `[Confirm]`
34. Budi Santoso: Buka daftar notifikasi lewat ikon Bell di navbar
35. Verifikasi notifikasi permintaan konfirmasi handover untuk aset `Laptop Dell Latitude 7440 {runId}` berstatus `Read` setelah Confirm

### Handover selesai tanpa konfirmasi mengirim notifikasi ke PIC Division
36. Dewi Lestari: Ketik Search `Finance {runId}`, tekan Enter
37. Dewi Lestari: Klik `⋯` pada baris ASG milik Assignee `Finance {runId}`
38. Dewi Lestari: Klik `Hand Over`
39. Dewi Lestari: Klik `[Verify Asset]`
40. Dewi Lestari: Pindai TAG aset `Printer Brother MFC {runId}`
41. Dewi Lestari: Klik `[Complete Handover]`
42. Hendra Kusuma: Buka daftar notifikasi lewat ikon Bell di navbar
43. Verifikasi notifikasi handover selesai untuk aset `Printer Brother MFC {runId}` tampil di daftar notifikasi PIC `Hendra Kusuma {runId}` sebagai penerima atas nama `Finance {runId}`

### Unassign selesai mengirim notifikasi ke Assignee
44. Dewi Lestari: Buka tab Assigned Assets di halaman Transactions > Assignment
45. Dewi Lestari: Ketik Search `Laptop Dell Latitude 7440 {runId}`, tekan Enter
46. Dewi Lestari: Klik `⋯` pada baris aset `Laptop Dell Latitude 7440 {runId}`
47. Dewi Lestari: Klik `Unassign`
48. Dewi Lestari: Klik `[Verify Asset]`
49. Dewi Lestari: Pindai TAG aset `Laptop Dell Latitude 7440 {runId}`
50. Dewi Lestari: Klik `[Submit]`
51. Budi Santoso: Buka daftar notifikasi lewat ikon Bell di navbar
52. Verifikasi notifikasi Unassign selesai untuk aset `Laptop Dell Latitude 7440 {runId}` tampil di daftar notifikasi `Budi Santoso {runId}`

### Unassign oleh Aktor di luar Group asal ditolak dan mengirim notifikasi jemput ke Aktor Group asal
53. Lina Marlina: Buka tab Assigned Assets di halaman Transactions > Assignment
54. Lina Marlina: Ketik Search `Lemari Arsip Besi {runId}`, tekan Enter
55. Lina Marlina: Klik `⋯` pada baris aset `Lemari Arsip Besi {runId}`
56. Lina Marlina: Klik `Unassign`
57. Lina Marlina: Klik `[Verify Asset]`
58. Lina Marlina: Pindai TAG aset `Server Rack HP {runId}`
59. Dewi Lestari: Buka daftar notifikasi lewat ikon Bell di navbar
60. Verifikasi notifikasi permintaan menerima kembali aset `Server Rack HP {runId}` tampil di daftar notifikasi `Dewi Lestari {runId}`

### Cancel Assignment mengirim notifikasi ke Assignee
61. Dewi Lestari: Buka tab Transactions di halaman Transactions > Assignment
62. Dewi Lestari: Ketik Search `Rina Wijaya {runId}`, tekan Enter
63. Dewi Lestari: Klik `⋯` pada baris ASG untuk aset `Tablet iPad 10 {runId}`
64. Dewi Lestari: Klik `Cancel Assignment`
65. Dewi Lestari: Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
66. Rina Wijaya: Buka daftar notifikasi lewat ikon Bell di navbar
67. Verifikasi notifikasi pembatalan penugasan aset `Tablet iPad 10 {runId}` tampil di daftar notifikasi `Rina Wijaya {runId}`

### Batas Transaction timeout 1 hari lagi mengirim notifikasi peringatan ke Aktor Assignment dan pengaju
68. Job pengingat Transaction timeout 1 hari lagi berjalan
69. Dewi Lestari: Buka daftar notifikasi lewat ikon Bell di navbar
70. Verifikasi notifikasi peringatan batas serah terima untuk aset `Kamera Canon M50 II {runId}` tampil di daftar notifikasi `Dewi Lestari {runId}` sebagai Aktor Assignment dan pengaju

### Penutupan otomatis oleh sistem mengirim notifikasi ke Assignee dan pengaju
71. Job penutupan otomatis Transaction timeout berjalan
72. Tono Hartono: Buka daftar notifikasi lewat ikon Bell di navbar
73. Verifikasi notifikasi penutupan otomatis untuk aset `Mouse Logitech M331 {runId}` tampil di daftar notifikasi `Tono Hartono {runId}`
74. Dewi Lestari: Buka daftar notifikasi lewat ikon Bell di navbar
75. Verifikasi notifikasi penutupan otomatis untuk aset `Mouse Logitech M331 {runId}` tampil di daftar notifikasi pengaju `Dewi Lestari {runId}`

### Report Damaged saat ditugaskan mengirim notifikasi dan selesai saat laporan di-Confirm
76. Dewi Lestari: Buka tab Assigned Assets di halaman Transactions > Assignment
77. Dewi Lestari: Ketik Search `Proyektor Epson EB-X49 {runId}`, tekan Enter
78. Dewi Lestari: Klik `⋯` pada baris aset `Proyektor Epson EB-X49 {runId}`
79. Dewi Lestari: Klik `Report Damaged`
80. Dewi Lestari: Lengkapi dan kirim dialog `Report Damaged` untuk aset `Proyektor Epson EB-X49 {runId}`
81. Nina Kartika: Buka daftar notifikasi lewat ikon Bell di navbar
82. Verifikasi notifikasi laporan kerusakan untuk aset `Proyektor Epson EB-X49 {runId}` tampil di daftar notifikasi `Nina Kartika {runId}` sebagai pemegang hak keputusan laporan kerusakan berstatus `Unread`
83. Nina Kartika: Konfirmasi (Confirm) laporan kerusakan aset `Proyektor Epson EB-X49 {runId}` di halaman keputusan laporan kerusakan
84. Verifikasi notifikasi laporan kerusakan untuk aset `Proyektor Epson EB-X49 {runId}` berstatus `Read` setelah laporan di-Confirm

### PIC menjadi tidak aktif mengirim notifikasi dan selesai saat Change PIC
85. Admin pengguna `Fajar Nugroho {runId}`: Nonaktifkan karyawan `Gita Maharani {runId}`
86. Dewi Lestari: Buka daftar notifikasi lewat ikon Bell di navbar
87. Verifikasi notifikasi PIC tidak aktif untuk `Operasional {runId}` tampil di daftar notifikasi `Dewi Lestari {runId}` sebagai Aktor Assignment Group aset `Head Office`, berstatus `Unread`
88. Dewi Lestari: Klik `Change PIC` pada ASG Assignee `Operasional {runId}`
89. Dewi Lestari: Pilih PIC `Hendra Kusuma {runId}`
90. Verifikasi notifikasi PIC tidak aktif untuk `Operasional {runId}` berstatus `Read` setelah Change PIC
91. Hendra Kusuma: Buka daftar notifikasi lewat ikon Bell di navbar
92. Verifikasi notifikasi PIC baru untuk aset `Meja Standing Desk {runId}` tampil di daftar notifikasi `Hendra Kusuma {runId}`

### Laporan Missing Assignee yang menunggu konfirmasi tidak menutup baris saat timeout
93. Budi Santoso: Buka daftar notifikasi lewat ikon Bell di navbar
94. Verifikasi jumlah notifikasi `Budi Santoso {runId}` untuk aset `Headphone Sony WH-1000XM5 {runId}` adalah nol, padahal batas Transaction timeout baris itu sudah terlewati dan job penutupan otomatis sudah berjalan
95. Job penutupan otomatis Transaction timeout berjalan lagi
96. Dewi Lestari: Buka tab Assigned Assets di halaman Transactions > Assignment
97. Dewi Lestari: Ketik Search `Headphone Sony WH-1000XM5 {runId}`, tekan Enter
98. Verifikasi baris aset `Headphone Sony WH-1000XM5 {runId}` tetap berstatus `Assigned` dengan badge `Reported Missing`
99. Budi Santoso: Buka daftar notifikasi lewat ikon Bell di navbar
100. Verifikasi jumlah notifikasi `Budi Santoso {runId}` untuk aset `Headphone Sony WH-1000XM5 {runId}` tetap nol setelah job timeout

### Pada level Full tidak ada notifikasi varian level None
101. Budi Santoso: Buka daftar notifikasi lewat ikon Bell di navbar
102. Verifikasi daftar notifikasi `Budi Santoso {runId}` memuat notifikasi Assignment untuk aset `Laptop Dell Latitude 7440 {runId}` pada entitas level `Full`
103. Verifikasi daftar notifikasi `Budi Santoso {runId}` tidak memuat notifikasi varian `Plan change`
104. Verifikasi daftar notifikasi `Tono Hartono {runId}` tidak memuat notifikasi varian `Not available on plan`

### Pengajuan dengan dua aset mengirim satu notifikasi ke Approver dan Reject menyelesaikan task approver
105. Dewi Lestari: Buka tab Drafts di halaman Transactions > Assignment
106. Dewi Lestari: Ketik Search `Sinta Anggraini {runId}`, tekan Enter
107. Dewi Lestari: Klik ikon `Edit` pada baris Draft untuk Assignee `Sinta Anggraini {runId}`
108. Dewi Lestari: Klik `[Submit]`
109. Dewi Lestari: Klik `[Submit]` pada dialog `Submit Assignment`
110. Anton Pratama: Buka daftar notifikasi lewat ikon Bell di navbar
111. Verifikasi daftar notifikasi `Anton Pratama {runId}` memuat tepat satu notifikasi permintaan approval untuk pengajuan Assignee `Sinta Anggraini {runId}` yang mencakup aset `Monitor LG 27UL500 {runId}` dan `Keyboard Logitech K380 {runId}`, berstatus `Unread`
112. Anton Pratama: Tolak (Reject) aset `Monitor LG 27UL500 {runId}` di halaman Approvals > Assignment dengan Approval Note `Aset belum dibutuhkan bulan ini`
113. Anton Pratama: Tolak (Reject) aset `Keyboard Logitech K380 {runId}` di halaman Approvals > Assignment dengan Approval Note `Aset belum dibutuhkan bulan ini`
114. Anton Pratama: Klik `[Submit]`
115. Anton Pratama: Klik `[Submit]` pada dialog `Submit Approval`
116. Verifikasi notifikasi permintaan approval untuk pengajuan Assignee `Sinta Anggraini {runId}` berstatus `Read` di daftar notifikasi `Anton Pratama {runId}` setelah seluruh asetnya diputuskan
117. Sinta Anggraini: Buka daftar notifikasi lewat ikon Bell di navbar
118. Verifikasi notifikasi hasil keputusan approval berupa penolakan untuk aset `Monitor LG 27UL500 {runId}` tampil di daftar notifikasi Assignee `Sinta Anggraini {runId}`

### Pembatalan baris Waiting for Approval mengirim notifikasi ke Assignee dan Approver
119. Dewi Lestari: Buka tab Drafts di halaman Transactions > Assignment
120. Dewi Lestari: Ketik Search `Wulan Sari {runId}`, tekan Enter
121. Dewi Lestari: Klik ikon `Edit` pada baris Draft untuk Assignee `Wulan Sari {runId}`
122. Dewi Lestari: Klik `[Submit]`
123. Dewi Lestari: Klik `[Submit]` pada dialog `Submit Assignment`
124. Anton Pratama: Buka daftar notifikasi lewat ikon Bell di navbar
125. Verifikasi notifikasi permintaan approval untuk aset `Webcam Logitech C920 {runId}` tampil di daftar notifikasi `Anton Pratama {runId}` berstatus `Unread`
126. Dewi Lestari: Buka tab Transactions di halaman Transactions > Assignment
127. Dewi Lestari: Ketik Search `Wulan Sari {runId}`, tekan Enter
128. Dewi Lestari: Klik `⋯` pada baris ASG untuk aset `Webcam Logitech C920 {runId}`
129. Dewi Lestari: Klik `Detail`
130. Dewi Lestari: Klik `⋯` pada baris aset `Webcam Logitech C920 {runId}` di tabel aset Assignment Detail
131. Dewi Lestari: Klik `Cancel Assignment`
132. Dewi Lestari: Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
133. Anton Pratama: Buka daftar notifikasi lewat ikon Bell di navbar
134. Verifikasi notifikasi permintaan approval untuk aset `Webcam Logitech C920 {runId}` berstatus `Read` di daftar notifikasi `Anton Pratama {runId}` setelah baris dibatalkan
135. Verifikasi notifikasi pembatalan penugasan aset `Webcam Logitech C920 {runId}` tampil di daftar notifikasi approver `Anton Pratama {runId}`
136. Wulan Sari: Buka daftar notifikasi lewat ikon Bell di navbar
137. Verifikasi notifikasi pembatalan penugasan aset `Webcam Logitech C920 {runId}` tampil di daftar notifikasi Assignee `Wulan Sari {runId}`

### Pengajuan tanpa approval langsung mengirim notifikasi hasil ke Assignee
138. Dewi Lestari: Buka tab Drafts di halaman Transactions > Assignment
139. Dewi Lestari: Ketik Search `Yusuf Hakim {runId}`, tekan Enter
140. Dewi Lestari: Klik ikon `Edit` pada baris Draft untuk Assignee `Yusuf Hakim {runId}`
141. Dewi Lestari: Klik `[Submit]`
142. Dewi Lestari: Klik `[Submit]` pada dialog `Submit Assignment`
143. Yusuf Hakim: Buka daftar notifikasi lewat ikon Bell di navbar
144. Verifikasi notifikasi hasil pengajuan tanpa approval untuk aset `Printer Epson L3250 {runId}` tampil di daftar notifikasi Assignee `Yusuf Hakim {runId}`

### Sesi konfirmasi yang dibatalkan admin menyelesaikan notifikasi permintaan konfirmasi
145. Dewi Lestari: Buka tab Transactions di halaman Transactions > Assignment
146. Dewi Lestari: Ketik Search `Dimas Prakoso {runId}`, tekan Enter
147. Dewi Lestari: Klik `⋯` pada baris ASG untuk aset `Scanner Epson DS-530 {runId}`
148. Dewi Lestari: Klik `Hand Over`
149. Dewi Lestari: Klik `[Verify Asset]`
150. Dewi Lestari: Pindai TAG aset `Scanner Epson DS-530 {runId}`
151. Dewi Lestari: Klik `[Request Confirmation]`
152. Dimas Prakoso: Buka daftar notifikasi lewat ikon Bell di navbar
153. Verifikasi notifikasi permintaan konfirmasi handover untuk aset `Scanner Epson DS-530 {runId}` tampil di daftar notifikasi `Dimas Prakoso {runId}` berstatus `Unread`
154. Dewi Lestari: Klik `[Cancel Request]` pada popup `Waiting for Confirmation`
155. Dimas Prakoso: Buka daftar notifikasi lewat ikon Bell di navbar
156. Verifikasi notifikasi permintaan konfirmasi handover untuk aset `Scanner Epson DS-530 {runId}` berstatus `Read` setelah sesi dibatalkan
157. Dewi Lestari: Klik `[Cancel]` pada halaman Hand Over
158. Dewi Lestari: Klik `[Leave]` pada dialog Unsaved Changes

### Jendela konfirmasi yang habis menyelesaikan notifikasi permintaan konfirmasi
159. Dewi Lestari: Buka tab Transactions di halaman Transactions > Assignment
160. Dewi Lestari: Ketik Search `Dimas Prakoso {runId}`, tekan Enter
161. Dewi Lestari: Klik `⋯` pada baris ASG untuk aset `Proyektor BenQ MH535 {runId}`
162. Dewi Lestari: Klik `Hand Over`
163. Dewi Lestari: Klik `[Verify Asset]`
164. Dewi Lestari: Pindai TAG aset `Proyektor BenQ MH535 {runId}`
165. Dewi Lestari: Klik `[Request Confirmation]`
166. Dimas Prakoso: Buka daftar notifikasi lewat ikon Bell di navbar
167. Verifikasi notifikasi permintaan konfirmasi handover untuk aset `Proyektor BenQ MH535 {runId}` tampil di daftar notifikasi `Dimas Prakoso {runId}` berstatus `Unread`
168. Waktu berlalu sampai jendela konfirmasi `15 menit` habis sejak permintaan konfirmasi dikirim
169. Dimas Prakoso: Buka daftar notifikasi lewat ikon Bell di navbar
170. Verifikasi notifikasi permintaan konfirmasi handover untuk aset `Proyektor BenQ MH535 {runId}` berstatus `Read` setelah jendela konfirmasi habis

### Laporan kerusakan yang ditolak menyelesaikan notifikasi laporan kerusakan
171. Dewi Lestari: Buka tab Assigned Assets di halaman Transactions > Assignment
172. Dewi Lestari: Ketik Search `Kursi Ergonomis Ergotec {runId}`, tekan Enter
173. Dewi Lestari: Klik `⋯` pada baris aset `Kursi Ergonomis Ergotec {runId}`
174. Dewi Lestari: Klik `Report Damaged`
175. Dewi Lestari: Isi What happened `Sandaran kursi patah saat dipakai` dan unggah Photo `kerusakan-kursi.jpg`
176. Dewi Lestari: Kirim dialog `Report Damaged`
177. Nina Kartika: Buka daftar notifikasi lewat ikon Bell di navbar
178. Verifikasi notifikasi laporan kerusakan untuk aset `Kursi Ergonomis Ergotec {runId}` tampil di daftar notifikasi `Nina Kartika {runId}` berstatus `Unread`
179. Nina Kartika: Tolak (Reject) laporan kerusakan aset `Kursi Ergonomis Ergotec {runId}` di halaman keputusan laporan kerusakan
180. Verifikasi notifikasi laporan kerusakan untuk aset `Kursi Ergonomis Ergotec {runId}` berstatus `Read` setelah laporan di-Reject

### Laporan kerusakan yang dibatalkan pelapor menyelesaikan notifikasi laporan kerusakan
181. Dewi Lestari: Buka tab Assigned Assets di halaman Transactions > Assignment
182. Dewi Lestari: Ketik Search `Router Mikrotik RB4011 {runId}`, tekan Enter
183. Dewi Lestari: Klik `⋯` pada baris aset `Router Mikrotik RB4011 {runId}`
184. Dewi Lestari: Klik `Report Damaged`
185. Dewi Lestari: Isi What happened `Port LAN router tidak berfungsi` dan unggah Photo `kerusakan-router.jpg`
186. Dewi Lestari: Kirim dialog `Report Damaged`
187. Nina Kartika: Buka daftar notifikasi lewat ikon Bell di navbar
188. Verifikasi notifikasi laporan kerusakan untuk aset `Router Mikrotik RB4011 {runId}` tampil di daftar notifikasi `Nina Kartika {runId}` berstatus `Unread`
189. Dewi Lestari: Klik `⋯` pada baris aset `Router Mikrotik RB4011 {runId}`
190. Dewi Lestari: Klik `Cancel Damage Report`
191. Dewi Lestari: Konfirmasi pembatalan laporan kerusakan aset `Router Mikrotik RB4011 {runId}`
192. Nina Kartika: Buka daftar notifikasi lewat ikon Bell di navbar
193. Verifikasi notifikasi laporan kerusakan untuk aset `Router Mikrotik RB4011 {runId}` berstatus `Read` setelah laporan dibatalkan pelapor

### Assignee dinonaktifkan mengalihkan notifikasi ke pengaju dan Aktor Assignment Group aset
194. Admin pengguna `Fajar Nugroho {runId}`: Nonaktifkan karyawan `Okta Permana {runId}`
195. Fajar Nugroho: Buka daftar notifikasi lewat ikon Bell di navbar
196. Verifikasi notifikasi penutupan otomatis dengan alasan `Assignee deactivated` untuk aset `Monitor Dell P2422H {runId}` tampil di daftar notifikasi pengaju `Fajar Nugroho {runId}`
197. Dewi Lestari: Buka daftar notifikasi lewat ikon Bell di navbar
198. Verifikasi notifikasi penutupan otomatis dengan alasan `Assignee deactivated` untuk aset `Monitor Dell P2422H {runId}` tampil di daftar notifikasi `Dewi Lestari {runId}` sebagai Aktor Assignment Group aset `Head Office`

### Penutupan otomatis baris Waiting for Approval oleh timeout mengirim notifikasi ke Assignee dan pengaju
199. Job penutupan otomatis Transaction timeout berjalan
200. Tono Hartono: Buka daftar notifikasi lewat ikon Bell di navbar
201. Verifikasi notifikasi penutupan otomatis untuk aset `Speaker JBL Flip 6 {runId}` tampil di daftar notifikasi `Tono Hartono {runId}`
202. Dewi Lestari: Buka daftar notifikasi lewat ikon Bell di navbar
203. Verifikasi notifikasi penutupan otomatis untuk aset `Speaker JBL Flip 6 {runId}` tampil di daftar notifikasi pengaju `Dewi Lestari {runId}`

### Pengaju tidak menerima notifikasi tambahan dan laporan Missing yang dibatalkan tidak mengubah baris Assigned
204. Dewi Lestari: Buka daftar notifikasi lewat ikon Bell di navbar
205. Verifikasi daftar notifikasi `Dewi Lestari {runId}` memuat notifikasi penutupan otomatis untuk aset `Mouse Logitech M331 {runId}`
206. Verifikasi tidak ada notifikasi untuk aset `Headphone Sony WH-1000XM5 {runId}` di daftar notifikasi `Dewi Lestari {runId}` setelah job timeout
207. Budi Santoso: Buka My Asset lewat menu Profile
208. Budi Santoso: Klik `Cancel Missing Report` pada baris aset `Headphone Sony WH-1000XM5 {runId}`
209. Budi Santoso: Konfirmasi pembatalan laporan kehilangan aset `Headphone Sony WH-1000XM5 {runId}`
210. Dewi Lestari: Buka tab Assigned Assets di halaman Transactions > Assignment
211. Dewi Lestari: Ketik Search `Headphone Sony WH-1000XM5 {runId}`, tekan Enter
212. Verifikasi baris aset `Headphone Sony WH-1000XM5 {runId}` tetap berstatus `Assigned` tanpa badge `Reported Missing` setelah laporan dibatalkan

### Pengajuan tanpa approval langsung mengirim notifikasi siap diserahkan ke Assignee
213. Yusuf Hakim: Buka daftar notifikasi lewat ikon Bell di navbar
214. Verifikasi notifikasi siap diserahkan untuk aset `Printer Epson L3250 {runId}` tampil di daftar notifikasi Assignee `Yusuf Hakim {runId}`
