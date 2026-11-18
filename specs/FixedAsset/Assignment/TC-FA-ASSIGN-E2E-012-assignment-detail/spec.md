---
id: TC-FA-ASSIGN-E2E-012-assignment-detail
title: "Assignment Detail: header ASG, tabel Assets, dan salin Transaction ID"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-ASG-03, "§4.1#r9", "§4.2.4#p1", "§4.2.4#p2", TS-ASG-17]
smoke: []
dependsOn: []
trace:
  T-ASG-03: [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 37, 40, 45, 56, 58, 60, 62, 64, 65, 66, 68, 69, 71, 75, 83, 84, 85, 86, 87, 88, 89, 91, 93, 95, 97, 98]
  "§4.1#r9": 18
  "§4.2.4#p1": [3, 4, 5, 6, 9, 10, 11, 12, 14, 15, 17, 20, 21, 49, 50, 76, 79]
  "§4.2.4#p2": [11, 12, 42, 51, 52]
  TS-ASG-17: 8
coverage:
  web: automated
---

# Assignment Detail: header ASG, tabel Assets, dan salin Transaction ID

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}`.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-012-1: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini dan bukan Assignee maupun PIC.
  - DU-012-2: Group `Head Office {runId}`.
  - DU-012-3: User `Agus Prasetyo {runId}`, role Asset Admin pada Group `Head Office {runId}`; ia pengaju ketiga ASG.
  - DU-012-4: User `Budi Santoso {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Budi S`, dari `Budi Santoso {runId}`.
  - DU-012-5: Division `Finance {runId}` dengan PIC aktif `Dewi Anggraini {runId}` dan anggota aktif ber-akun login `Joko Santoso {runId}` yang memenuhi syarat sebagai PIC pengganti; keduanya tanpa akses menu Assignment.
  - DU-012-6: ASG berstatus `Waiting for Handover` untuk Assignee Division `Finance {runId}` di Group `Head Office {runId}` dengan Note `Peminjaman alat untuk audit {runId}`, dengan lima baris: `Laptop Dell Latitude 5420 {runId}` `Waiting for Handover` tanpa approval, `Toyota Avanza {runId}` `Waiting for Approval` dengan approver, `Printer HP M404 {runId}` `Assigned` dengan `Reported Damaged` dan konfirmasi `Accepted on phone`, `Tablet Samsung Tab S8 {runId}` `Unassigned` dengan marker `Missing` dan konfirmasi `Confirmed on admin device`, serta `Excavator PC200 {runId}` `Rejected`.
  - DU-012-7: ASG berstatus `Assigned` untuk Assignee DU-012-4 dengan satu aset `Monitor LG 24 {runId}` berstatus `Assigned`; seluruh barisnya Assigned.
  - DU-012-8: User `Rina Wijaya {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Rina W`, dari `Rina Wijaya {runId}`; Assignee ASG DU-012-9 dan pemegang semua asetnya.
  - DU-012-9: ASG untuk Assignee DU-012-8 di Group `Head Office {runId}`, diajukan DU-012-3, dengan tujuh baris DU-012-11 sampai DU-012-17.
  - DU-012-10: General Settings entitas suite: Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - DU-012-11: Aset `Camera Canon EOS R {runId}` `Assigned` dengan `Reported Missing` yang dilaporkan DU-012-8, konfirmasi `Accepted on phone`, foto handover tersedia, ber-TAG QR, Category `Peralatan Dokumentasi {runId}`, Purpose `Dokumentasi audit {runId}`, diserahkan oleh DU-012-3.
  - DU-012-12: Aset `Laptop HP ProBook {runId}` `Assigned` dengan record `Damaged`.
  - DU-012-13: Aset `Mouse Logitech M170 {runId}` `Assigned` dengan approval `Approved` oleh DU-012-18, konfirmasi `Not required`, tanpa foto handover.
  - DU-012-14: Aset `Keyboard Logitech K380 {runId}` `Waiting for Approval` dengan approval type `All approvers`: DU-012-18 sudah menyetujui dan `Indra Gunawan {runId}` masih menunggu.
  - DU-012-15: Aset `Webcam Logitech C920 {runId}` `Waiting for Approval`; spec ini membatalkannya lewat `Agus Prasetyo {runId}`.
  - DU-012-16: Aset `Tablet Lenovo M10 {runId}` `Unassigned` dengan foto unassign tersedia.
  - DU-012-17: Aset `Printer Canon G3010 {runId}` `Rejected` dengan Reason `Anggaran belum disetujui`.
  - DU-012-18: User approver `Hana Pratama {runId}` dan `Indra Gunawan {runId}`, karyawan aktif tanpa akses menu Assignment.

## Test Steps

### Buka Assignment Detail dan header ASG
1. Ketik Search `Finance {runId}`, tekan Enter
2. Klik tautan Transaction ID pada baris `Finance {runId}`
3. Verifikasi Breadcrumb memuat `Transactions`, `Assignment`, `Transactions`, dan `Detail`
4. Verifikasi baris judul memuat Transaction ID berformat `ASG-YYYY-NNNN` dan badge status header `Waiting for Handover`
5. Verifikasi baris judul tidak memuat badge `No PIC` karena Assignee punya PIC aktif
6. Verifikasi baris judul tidak memuat ringkasan jumlah baris per status
7. Klik tombol salin di samping Transaction ID
8. Verifikasi toast `Success, Transaction ID has been copied.` tampil
9. Verifikasi baris info memuat `Assignee` dengan nilai `Finance {runId}`, `PIC` dengan nilai `Dewi Anggraini {runId}`, dan `Group` dengan nilai `Head Office {runId}`
10. Verifikasi `Note` memuat `Peminjaman alat untuk audit {runId}`
11. Verifikasi `Requested By` memuat Request Date dalam format Date Format `dd/MM/yy`
12. Verifikasi `Last Updated` memuat Date Time dalam format Date Format `dd/MM/yy` dan Time Format `24 jam`
13. Arahkan kursor ke nilai `Requested By`
14. Verifikasi nama lengkap `Agus Prasetyo {runId}` tampil
15. Verifikasi header tidak memuat Purpose
16. Arahkan kursor ke nilai `PIC`
17. Verifikasi tooltip PIC memuat nama lengkap `Dewi Anggraini {runId}`

### Toolbar dan kolom tabel Assets
18. Verifikasi toolbar tabel Assets memuat `Search by Scan`, Search, `Filter`, dan `Download` tanpa menu `⋯`[^drift-1]
19. Klik `Search`
20. Verifikasi kotak Search memuat placeholder `Search asset name or ID...`
21. Verifikasi tabel Assets tampil tanpa tab dan tanpa judul `Assets`
22. Verifikasi header kolom tabel tampil berurutan: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Status`, `Handed Over At`, `Confirmation`, `Approval`, `Handover Photo`, `Unassign Photo`
23. Verifikasi kolom `TAG`, `Category`, `Unassigned At`, `Reason`, `Purpose`, dan `Handed Over By` tidak tampil secara awal
24. Verifikasi tabel memuat tepat 5 baris dan urutan awal menurut Name A-Z: `Excavator PC200 {runId}`, `Laptop Dell Latitude 5420 {runId}`, `Printer HP M404 {runId}`, `Tablet Samsung Tab S8 {runId}`, `Toyota Avanza {runId}`

### Isi baris tabel Assets
25. Verifikasi kolom `Name` kelima baris berformat `[Asset Name] - [Increment]`
26. Verifikasi kolom `Status` baris `Laptop Dell Latitude 5420 {runId}` menampilkan `Waiting for Handover` dan baris `Toyota Avanza {runId}` menampilkan `Waiting for Approval`
27. Verifikasi kolom `Status` baris `Printer HP M404 {runId}` menampilkan `Assigned` dengan badge `Reported Damaged`
28. Verifikasi kolom `Status` baris `Tablet Samsung Tab S8 {runId}` menampilkan `Unassigned` dengan badge kedua `Missing`
29. Verifikasi kolom `Status` baris `Excavator PC200 {runId}` menampilkan `Rejected`
30. Verifikasi kolom `Confirmation` menampilkan `Accepted on phone` pada baris `Printer HP M404 {runId}`, `Confirmed on admin device` pada baris `Tablet Samsung Tab S8 {runId}`, dan `—` pada baris yang belum diserahkan
31. Verifikasi kolom `Approval` menampilkan `Not required` pada baris `Laptop Dell Latitude 5420 {runId}`, `Waiting` pada baris `Toyota Avanza {runId}`, dan `Rejected` pada baris `Excavator PC200 {runId}`
32. Verifikasi kolom `Handed Over At` terisi pada baris `Printer HP M404 {runId}` dan `Tablet Samsung Tab S8 {runId}`, dan menampilkan `—` pada baris yang belum diserahkan
33. Verifikasi kolom `Brand` dan `Model/Type` kelima baris menampilkan `—`
34. Arahkan kursor ke kolom `Status` baris `Toyota Avanza {runId}`
35. Verifikasi waktu baris masuk ke status `Waiting for Approval` tampil

### Aksi baris dan aksi di bawah tabel
36. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
37. Verifikasi menu aksi baris memuat `Assignment Log`, `Transaction Rules`, `Hand Over`, `Remind Assignee`, dan `Cancel Assignment`
38. Tutup menu aksi baris
39. Klik `⋯` pada baris `Printer HP M404 {runId}`
40. Verifikasi menu aksi baris memuat `Assignment Log`, `Transaction Rules`, `Unassign`, dan `Report Missing`, tanpa `Report Damaged`
41. Tutup menu aksi baris
42. Verifikasi aksi di bawah tabel memuat `[Cancel Assignment]`, `[Change PIC]`, `[Unassign]`, dan `[Hand Over]` karena semuanya memenuhi syarat
43. Klik `Download`[^drift-1]
44. Klik `Download as CSV`
45. Verifikasi berkas `Assignment-Detail-Assets.csv` terunduh

### Aksi di bawah tabel hanya yang memenuhi syarat
46. Kembali ke halaman sebelumnya
47. Ganti isi kotak search dengan `Budi Santoso {runId}`, tekan Enter
48. Klik tautan Transaction ID pada baris `Budi S`
49. Verifikasi baris info memuat `Assignee` dengan nilai `Budi S`
50. Verifikasi baris info tidak memuat `PIC` karena Assignee `Budi S` berjenis Employee
51. Verifikasi aksi di bawah tabel memuat `[Unassign]`
52. Verifikasi aksi di bawah tabel tidak memuat `[Hand Over]`, `[Cancel Assignment]`, dan `[Change PIC]` karena tidak ada baris yang memenuhi syaratnya

### Status Reported Missing dan Damaged pada tabel Assets
53. Kembali ke halaman sebelumnya
54. Ganti isi kotak search dengan `Rina Wijaya {runId}`, tekan Enter
55. Klik tautan Transaction ID pada baris `Rina W`
56. Verifikasi kolom `Status` baris `Camera Canon EOS R {runId}` menampilkan `Assigned` dengan badge `Reported Missing`
57. Arahkan kursor ke badge `Reported Missing` baris `Camera Canon EOS R {runId}`
58. Verifikasi hover memuat `Reported missing by` dengan nama pelapor `Rina Wijaya {runId}`, tanggal laporan dalam Date Format `dd/MM/yy`, dan teks `Confirm or reject it in Missing.`
59. Klik badge `Reported Missing` baris `Camera Canon EOS R {runId}`
60. Verifikasi dialog Missing Log untuk aset `Camera Canon EOS R {runId}` terbuka
61. Tutup dialog Missing Log
62. Verifikasi kolom `Status` baris `Laptop HP ProBook {runId}` menampilkan `Assigned` dengan badge `Damaged`
63. Arahkan kursor ke kolom `Status` baris `Laptop HP ProBook {runId}`
64. Verifikasi waktu baris masuk ke status `Assigned` tampil

### Kolom Approval dan Confirmation pada tabel Assets
65. Verifikasi kolom `Approval` baris `Mouse Logitech M170 {runId}` menampilkan `Approved`
66. Verifikasi kolom `Confirmation` baris `Mouse Logitech M170 {runId}` menampilkan `Not required`
67. Arahkan kursor ke kolom `Approval` baris `Keyboard Logitech K380 {runId}`
68. Verifikasi hover memuat approval type `All approvers`, approver `Hana Pratama {runId}` sudah menyetujui, dan approver `Indra Gunawan {runId}` masih menunggu
69. Verifikasi hover memuat progres `(1 of 2 approved)`
70. Arahkan kursor ke kolom `Confirmation` baris `Camera Canon EOS R {runId}`
71. Verifikasi hover memuat waktu konfirmasi dan teks pernyataan konfirmasi `Accepted on phone`
72. Catat nilai `Last Updated` pada header
73. Aktor `Agus Prasetyo {runId}` melakukan Cancel Assignment pada baris `Webcam Logitech C920 {runId}` sampai berhasil
74. Muat ulang halaman
75. Verifikasi kolom `Approval` baris `Webcam Logitech C920 {runId}` menampilkan `Canceled`
76. Verifikasi nilai `Last Updated` berubah menjadi waktu peristiwa Cancel yang baru
77. Klik `⋯` pada baris `Webcam Logitech C920 {runId}`
78. Klik `Assignment Log`
79. Verifikasi waktu entri terbaru pada dialog Assignment Log sama dengan nilai `Last Updated` pada header
80. Tutup dialog Assignment Log

### Kolom tersembunyi, Reason, dan foto pada tabel Assets
81. Klik header kolom `Actions`
82. Beri centang kolom `TAG`, `Category`, `Unassigned At`, `Reason`, `Purpose`, dan `Handed Over By` pada panel Column Visibility
83. Verifikasi kolom `TAG` baris `Camera Canon EOS R {runId}` menampilkan ikon TAG tipe QR
84. Verifikasi kolom `Category` baris `Camera Canon EOS R {runId}` menampilkan `Peralatan Dokumentasi {runId}`
85. Verifikasi kolom `Purpose` baris `Camera Canon EOS R {runId}` menampilkan `Dokumentasi audit {runId}`
86. Verifikasi kolom `Handed Over By` baris `Camera Canon EOS R {runId}` menampilkan `Agus Prasetyo {runId}`
87. Verifikasi kolom `Unassigned At` baris `Tablet Lenovo M10 {runId}` terisi tanggal dan baris `Camera Canon EOS R {runId}` menampilkan `—`
88. Verifikasi kolom `Reason` baris `Printer Canon G3010 {runId}` menampilkan `Anggaran belum disetujui`
89. Verifikasi kolom `Handover Photo` baris `Camera Canon EOS R {runId}` menampilkan thumbnail dan baris `Mouse Logitech M170 {runId}` menampilkan `—`
90. Klik thumbnail kolom `Handover Photo` baris `Camera Canon EOS R {runId}`
91. Verifikasi pratinjau foto handover aset `Camera Canon EOS R {runId}` terbuka
92. Tutup pratinjau foto
93. Verifikasi kolom `Unassign Photo` baris `Tablet Lenovo M10 {runId}` menampilkan thumbnail

### Hover Handed Over At pada tabel Assets
94. Arahkan kursor ke kolom `Handed Over At` baris `Camera Canon EOS R {runId}`
95. Verifikasi `Agus Prasetyo {runId}` tampil sebagai pihak yang menyerahkan aset `Camera Canon EOS R {runId}` pada hover `Handed Over At`

### Field filter dan placeholder tabel Assets
96. Klik `Filter`
97. Verifikasi field filter `Name`, `Brand`, `Model/Type`, `Status`, `TAG`, `Category`, `Handed Over At`, `Unassigned At`, `Confirmation`, `Approval`, dan `Handed Over By` tampil
98. Verifikasi placeholder `All asset names`, `All brands`, `All models`, `All statuses`, `All tags`, `All categories`, `All confirmations`, `All approvals`, dan `All users` tampil pada field dropdown masing-masing, serta field `Handed Over At` dan `Unassigned At` memuat placeholder `Select date`
99. Klik `Filter`

[^drift-1]: Drift PRD vs foundation. PRD §5 Global Table Rules baris Download dan §4.2.4: nama dan tooltip tombol toolbar adalah `Export`, bukan `Download`. foundation `prd-conventions.md` §9.1: icon toolbar bernama `Download` dengan tooltip `Download`, dan modul tidak menulis ulang teks tooltip itu. Diasersi: foundation, karena tombol unduh di toolbar tabel adalah pola bersama (SB-4).
