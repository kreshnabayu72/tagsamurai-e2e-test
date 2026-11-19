---
id: TC-FA-BORROW-E2E-042-transaction-log-aset-dep-asset-detail
title: "Transaction log aset di Asset Detail memuat peristiwa Borrow lintas transaksi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§8.1a#p1", "§8.1a#r1", "§8.1a#r2", "§8.1a#r3", "§8.1a#r4", "§8.1a#r5", "§8.1a#r6", "§8.1a#r7", "§8.1a#r8", "§8.1a#r9", "§8.1a#r10", "§8.1a#r11", "§8.1a#r12", "§8.1a#r13", "§8.1a#r14", "§8.1a#r15", "§8.1a#r16", "§8.1a#r17", "§8.1a#r18", "§8.1a#r19", "§8.1a#p4"]
smoke: []
dependsOn: ["Asset Detail: Transaction log"]
trace:
  "§8.1a#p1": [4, 19]
  "§8.1a#r1": 5
  "§8.1a#r2": 6
  "§8.1a#r3": [7, 8, 9, 10, 11, 12, 13]
  "§8.1a#r4": 14
  "§8.1a#r5": [15, 67, 69]
  "§8.1a#r6": [16, 33]
  "§8.1a#r7": [17, 34]
  "§8.1a#r8": [7, 31]
  "§8.1a#r9": 8
  "§8.1a#r10": 32
  "§8.1a#r11": 39
  "§8.1a#r12": 9
  "§8.1a#r13": [10, 54]
  "§8.1a#r14": [11, 55, 62]
  "§8.1a#r15": 12
  "§8.1a#r16": [44, 75]
  "§8.1a#r17": 49
  "§8.1a#r18": [13, 63]
  "§8.1a#r19": [57, 81, 87]
  "§8.1a#p4": [22, 26]
anchor: [56, 74, 80, 86]
coverage:
  web: automated
---

# Transaction log aset di Asset Detail memuat peristiwa Borrow lintas transaksi

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office` dan Group `Branch Surabaya`; ia hanya membaca Transaction log aset dan bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: daftar aset (Assets > All).
- Data:
  - DU-042-1: aset `Kamera Sony ZV-1 {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}` (punya akun login), tanpa PIC, dengan satu BRW (DU-042-8) yang riwayatnya berurutan dari paling awal: Requested, Approved, Handed over (scan lewat Handheld Reader `Handheld Zebra RFD40 {runId}`), Extension requested, Extended, Overdue, lalu Returned (scan lewat reader yang sama); tujuh baris log.
  - DU-042-2: aset `Proyektor Epson EB-X49 {runId}`, Group `Head Office`, Borrower karyawan tanpa akun login `Nico Prasetyo {runId}` dengan PIC `Rina Wijaya {runId}`, dengan satu BRW (DU-042-9) yang riwayatnya Requested, Approval rerouted, lalu Rejected; tiga baris log.
  - DU-042-3: aset `Gimbal DJI RS 3 {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`, dengan satu BRW (DU-042-10) yang riwayatnya Requested, Approved, lalu Canceled; tiga baris log.
  - DU-042-4: aset `Mikrofon Rode VideoMic {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`, dengan satu BRW (DU-042-11) yang riwayatnya Requested, Approved, Handed over, lalu Reported missing oleh Aktor Borrow yang memegang hak Aktor Missing; empat baris log.
  - DU-042-5: aset `Tablet Samsung Tab S9 {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`, dengan satu BRW (DU-042-12) yang riwayatnya Requested, Approved, Handed over, Extension requested, Extension forwarded, Extension rejected, Extension requested, Extension canceled, lalu Returned; di sela riwayat itu terjadi Damage reported, Damage report canceled, laporan kehilangan oleh Borrower, pembatalan laporan kehilangan, TAG reported, dan Handover not confirmed; sembilan baris log.
  - DU-042-6: aset `Printer Epson L5290 {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`, dengan satu BRW (DU-042-13) yang riwayatnya Requested, Approved, Handed over, Overdue, Extension requested, Extension rejected sesudah Due date, lalu Returned dengan penanda Damaged; tujuh baris log.
  - DU-042-7: aset `Speaker Bose S1 Pro {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`, dengan satu BRW (DU-042-14) yang riwayatnya Requested, Approved, Handed over, Reported missing oleh Borrower, lalu Missing confirmed oleh Aktor Missing; empat baris log.
  - DU-042-8: BRW `Returned` milik DU-042-1, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-9: BRW `Rejected` milik DU-042-2, Group `Head Office`, Borrower `Nico Prasetyo {runId}`, PIC `Rina Wijaya {runId}`.
  - DU-042-10: BRW `Canceled` milik DU-042-3, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-11: BRW `Returned` milik DU-042-4 dengan penanda `Missing`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-12: BRW `Returned` milik DU-042-5, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-13: BRW `Returned` milik DU-042-6 dengan penanda `Damaged`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-14: BRW `Returned` milik DU-042-7 dengan penanda `Missing`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-15: aset `Drone DJI Mavic 3 {runId}`, Group saat peristiwa `Head Office`, dipindah ke Group `Branch Surabaya` sesudah BRW DU-042-16 selesai; riwayat BRW itu Requested, Approved, Handed over, lalu Returned; empat baris log.
  - DU-042-16: BRW `Returned` milik DU-042-15, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-17: aset `Handycam Panasonic HC {runId}`, Group `Head Office`, dengan satu BRW (DU-042-18) yang riwayatnya Requested, Approved, Handed over, lalu laporan kehilangan oleh Aktor Borrow tanpa hak Aktor Missing sehingga laporan `Waiting for Confirmation` dan baris tetap Borrowed; tiga baris log.
  - DU-042-18: BRW `Borrowed` milik DU-042-17, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-19: aset `Walkie Talkie Motorola {runId}`, Group `Head Office`, dengan satu BRW (DU-042-20) yang riwayatnya Requested, Approved, Handed over, laporan kehilangan oleh Borrower, lalu Missing report rejected oleh Aktor Missing; tiga baris log.
  - DU-042-20: BRW `Borrowed` milik DU-042-19, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-21: aset `Radio Handy Icom {runId}`, Group `Head Office`, dengan satu BRW (DU-042-22) yang riwayatnya Requested, Approved, Handed over, lalu laporan kehilangan oleh PIC; tiga baris log.
  - DU-042-22: BRW `Borrowed` milik DU-042-21, Group `Head Office`, Borrower karyawan tanpa akun login `Nico Prasetyo {runId}`, PIC `Rina Wijaya {runId}`.
- Kondisi:
  - Date Format dan Time Format di General Settings entitas berlaku untuk tampilan tanggal dan waktu.

## Test Steps

### Kolom dan baris log satu aset dengan riwayat lengkap dari Requested sampai Returned
1. Ketik Search `Kamera Sony ZV-1 {runId}`, tekan Enter
2. Buka Asset Detail aset `Kamera Sony ZV-1 {runId}`
3. Klik tab `Transaction log`
4. Verifikasi log memuat tepat tujuh baris, satu per perubahan status baris aset pada BRW milik DU-042-8
5. Verifikasi kolom `Date` menampilkan waktu peristiwa dengan format Date Format dan Time Format General Settings
6. Verifikasi kolom `Transaction ID` memuat nomor BRW milik DU-042-8 sebagai tautan pada ketujuh baris
7. Verifikasi peristiwa Requested tercatat sebagai baris dengan Status `Waiting for Approval`
8. Verifikasi peristiwa Approved tercatat sebagai baris dengan Status `Waiting for Handover`
9. Verifikasi peristiwa Handed over tercatat sebagai baris dengan Status `Borrowed`
10. Verifikasi peristiwa Extension requested tercatat sebagai baris dengan Status `Extension Request`
11. Verifikasi peristiwa Extended tercatat sebagai baris dengan Status `Borrowed`
12. Verifikasi peristiwa Overdue tercatat sebagai baris dengan Status `Overdue`
13. Verifikasi peristiwa Returned tercatat sebagai baris dengan Status `Returned`
14. Verifikasi kolom `Reader name` berisi `Handheld Zebra RFD40 {runId}` pada baris Handed over dan baris Returned, serta `—` pada baris lain
15. Verifikasi kolom `Group` berisi `Head Office` pada ketujuh baris
16. Verifikasi kolom `PIC` berisi `—` pada ketujuh baris karena Borrower punya akun login
17. Verifikasi kolom `Borrower` berisi `Oscar Wijaya {runId}` pada ketujuh baris

### Klik Transaction ID membuka Borrow Detail dan log aset memuat peristiwa yang sama dengan Borrow Log
18. Klik Transaction ID BRW milik DU-042-8 pada baris dengan Status `Returned`
19. Verifikasi Borrow Detail BRW milik DU-042-8 terbuka
20. Klik menu ⋯ pada baris aset `Kamera Sony ZV-1 {runId}`
21. Klik `Borrow Log`
22. Verifikasi Borrow Log aset `Kamera Sony ZV-1 {runId}` memuat node `Handed over by [Giver]` dan node `Returned to [Receiver]` untuk peristiwa yang sama dengan baris Status `Borrowed` dan `Returned` di Transaction log aset
23. Tutup dialog Borrow Log
24. Klik tab `History` pada halaman Borrow
25. Ketik Search `Oscar Wijaya {runId}`, tekan Enter
26. Verifikasi BRW milik DU-042-8 tampil di tab `History` sebagai riwayat tingkat BRW

### Borrower tanpa akun login menampilkan PIC, dan Approval rerouted serta Rejected
27. Buka daftar aset lewat sidebar `Assets` > `All`
28. Ketik Search `Proyektor Epson EB-X49 {runId}`, tekan Enter
29. Buka Asset Detail aset `Proyektor Epson EB-X49 {runId}`
30. Klik tab `Transaction log`
31. Verifikasi peristiwa Requested dan Approval rerouted masing-masing tercatat sebagai baris dengan Status `Waiting for Approval`
32. Verifikasi peristiwa Rejected tercatat sebagai baris dengan Status `Rejected`
33. Verifikasi kolom `PIC` berisi `Rina Wijaya {runId}` pada ketiga baris karena Borrower tidak punya akun login
34. Verifikasi kolom `Borrower` berisi `Nico Prasetyo {runId}` pada ketiga baris

### Peristiwa Canceled tercatat sebagai Status Canceled
35. Buka daftar aset lewat sidebar `Assets` > `All`
36. Ketik Search `Gimbal DJI RS 3 {runId}`, tekan Enter
37. Buka Asset Detail aset `Gimbal DJI RS 3 {runId}`
38. Klik tab `Transaction log`
39. Verifikasi peristiwa Canceled tercatat sebagai baris dengan Status `Canceled`

### Report Missing oleh Aktor Borrow dan Missing confirmed menutup baris Returned dengan penanda Missing
40. Buka daftar aset lewat sidebar `Assets` > `All`
41. Ketik Search `Mikrofon Rode VideoMic {runId}`, tekan Enter
42. Buka Asset Detail aset `Mikrofon Rode VideoMic {runId}`
43. Klik tab `Transaction log`
44. Verifikasi peristiwa laporan kehilangan oleh Aktor Borrow tercatat sebagai baris dengan Status `Returned` dan penanda `Missing`
45. Buka daftar aset lewat sidebar `Assets` > `All`
46. Ketik Search `Speaker Bose S1 Pro {runId}`, tekan Enter
47. Buka Asset Detail aset `Speaker Bose S1 Pro {runId}`
48. Klik tab `Transaction log`
49. Verifikasi peristiwa konfirmasi laporan kehilangan tercatat sebagai baris dengan Status `Returned` dan penanda `Missing`

### Extension forwarded, rejected, dan canceled serta peristiwa yang tidak membentuk baris
50. Buka daftar aset lewat sidebar `Assets` > `All`
51. Ketik Search `Tablet Samsung Tab S9 {runId}`, tekan Enter
52. Buka Asset Detail aset `Tablet Samsung Tab S9 {runId}`
53. Klik tab `Transaction log`
54. Verifikasi peristiwa Extension forwarded tercatat sebagai baris dengan Status `Extension Approval`
55. Verifikasi peristiwa Extension rejected dan Extension canceled masing-masing tercatat sebagai baris dengan Status `Borrowed`
56. Verifikasi log memuat baris Status `Extension Approval` dan baris Status `Returned` untuk BRW milik DU-042-12
57. Verifikasi tidak ada baris tambahan di log yang memuat tepat sembilan baris untuk Damage reported, Damage report canceled, laporan kehilangan oleh Borrower, pembatalan laporan kehilangan, TAG reported, dan Handover not confirmed

### Extension rejected sesudah Due date berstatus Overdue dan Returned membawa penanda Damaged
58. Buka daftar aset lewat sidebar `Assets` > `All`
59. Ketik Search `Printer Epson L5290 {runId}`, tekan Enter
60. Buka Asset Detail aset `Printer Epson L5290 {runId}`
61. Klik tab `Transaction log`
62. Verifikasi peristiwa Extension rejected sesudah Due date tercatat sebagai baris dengan Status `Overdue`
63. Verifikasi peristiwa Returned tercatat sebagai baris dengan Status `Returned` dan penanda `Damaged`

### Group pada baris log adalah Group asal aset saat peristiwa, bukan Group aset sekarang
64. Buka daftar aset lewat sidebar `Assets` > `All`
65. Ketik Search `Drone DJI Mavic 3 {runId}`, tekan Enter
66. Buka Asset Detail aset `Drone DJI Mavic 3 {runId}`
67. Verifikasi Asset Detail menampilkan Group aset `Branch Surabaya` sesudah dipindah
68. Klik tab `Transaction log`
69. Verifikasi kolom `Group` berisi `Head Office` pada keempat baris log BRW milik DU-042-16 karena itu Group asal aset saat peristiwa, bukan Group aset sekarang

### Laporan kehilangan oleh Aktor Borrow tanpa hak Aktor Missing tidak membentuk baris
70. Buka daftar aset lewat sidebar `Assets` > `All`
71. Ketik Search `Handycam Panasonic HC {runId}`, tekan Enter
72. Buka Asset Detail aset `Handycam Panasonic HC {runId}`
73. Klik tab `Transaction log`
74. Verifikasi log memuat baris Handed over dengan Status `Borrowed` untuk BRW milik DU-042-18
75. Verifikasi tidak ada baris tambahan di log selain tiga baris Requested, Approved, dan Handed over untuk laporan kehilangan oleh Aktor Borrow tanpa hak Aktor Missing karena status baris tetap `Borrowed`

### Missing report rejected dan laporan kehilangan oleh PIC tidak membentuk baris
76. Buka daftar aset lewat sidebar `Assets` > `All`
77. Ketik Search `Walkie Talkie Motorola {runId}`, tekan Enter
78. Buka Asset Detail aset `Walkie Talkie Motorola {runId}`
79. Klik tab `Transaction log`
80. Verifikasi log memuat baris Handed over dengan Status `Borrowed` untuk BRW milik DU-042-20
81. Verifikasi tidak ada baris tambahan di log selain tiga baris Requested, Approved, dan Handed over untuk laporan kehilangan oleh Borrower maupun penolakan laporan itu oleh Aktor Missing
82. Buka daftar aset lewat sidebar `Assets` > `All`
83. Ketik Search `Radio Handy Icom {runId}`, tekan Enter
84. Buka Asset Detail aset `Radio Handy Icom {runId}`
85. Klik tab `Transaction log`
86. Verifikasi log memuat baris Handed over dengan Status `Borrowed` untuk BRW milik DU-042-22
87. Verifikasi tidak ada baris tambahan di log selain tiga baris Requested, Approved, dan Handed over untuk laporan kehilangan oleh PIC `Rina Wijaya {runId}`
