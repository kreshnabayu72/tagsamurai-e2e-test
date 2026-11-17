---
id: TC-FA-MYASSET-BE-215-filter-opsi-dan-hasil-dep-borrow
title: "Filter My Asset: opsi tiap field dan hasil saringan di keempat tabel"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["T-MYA-01", "T-MYA-04", "§4.1b#r2", "§4.1b#r4", "§4.1b#r5", "§4.1b#r6", "§4.1b#r7", "§4.1b#r8", "§4.1b#r9", "§4.1b#r10", "§4.1b#r12", "§4.1b#r14", "§4.1b#r16", "§4.1b#r17", "§4.1c#r2", "§4.1c#r4", "§4.1c#r5", "§4.1c#r6", "§4.1c#r7", "§4.1c#r8", "§4.1c#r9", "§4.1c#r10", "§4.1c#r11", "§4.1c#r13", "§4.1c#r14", "EB-FLT-3"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
owner: BE
trace:
  "T-MYA-01": [154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182]
  "T-MYA-04": [108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152]
  "§4.1b#r2": [2, 20]
  "§4.1b#r4": [4, 22, 40]
  "§4.1b#r5": [6, 24]
  "§4.1b#r6": [8, 26]
  "§4.1b#r7": [10, 28, 38, 186, 189, 193]
  "§4.1b#r8": [12, 30]
  "§4.1b#r9": [14, 32]
  "§4.1b#r10": [46, 48, 50]
  "§4.1b#r12": [16, 34]
  "§4.1b#r14": [18, 36, 42]
  "§4.1b#r16": [52, 54]
  "§4.1b#r17": 56
  "§4.1c#r2": [58, 76]
  "§4.1c#r4": [60, 78]
  "§4.1c#r5": [62, 80]
  "§4.1c#r6": [64, 82]
  "§4.1c#r7": [66, 84, 86, 191]
  "§4.1c#r8": [68, 88]
  "§4.1c#r9": [70, 90]
  "§4.1c#r10": [72, 92]
  "§4.1c#r11": [74, 94, 96]
  "§4.1c#r13": [100, 102]
  "§4.1c#r14": [104, 106]
  "EB-FLT-3": [38, 40, 42, 44, 96, 98, 146, 148, 166, 168]
---

# Filter My Asset: opsi tiap field dan hasil saringan di keempat tabel

## Prerequisites
- Aktor: Borrower dan Assignee, yaitu pengguna ber-akun login `Rina Wulandari {runId}` (DU-215-1) yang membuka My Asset dan tidak punya baris lain selain DU-215-2 sampai DU-215-21. Aktor Borrow dan Aktor Assignment menyerahkan aset ke Aktor, masing-masing dengan hak atas Group aset yang diserahkannya; Aktor Borrow `Budi Santoso {runId}`, Aktor Assignment `Agus Pratama {runId}` dan `Siti Rahmawati {runId}`. Borrower tanpa akun `Hendra Wijaya {runId}` dan Division `Divisi Keuangan {runId}` memakai Aktor sebagai PIC.
- Data:
  - DU-215-1: Aktor pemegang semua baris di bawah, tanpa baris lain di My Asset: Name `Rina Wulandari {runId}`, Posisi `Borrower dan Assignee`.
  - DU-215-2: pinjaman Admin Borrowed, Brand dan Model yang dipakai dua baris: Name `Laptop Operasional {runId}`, Brand `Dell`, Model/Type `Latitude 5440`, Group `Ruang IT`, Status `Borrowed`, TAG `RFID`, Category `Komputer`, Borrower `Me`, Source `Admin`, Duration `3 days`, Due Date `T0 + 3 hari`, Handed Over At `T0`.
  - DU-215-3: pinjaman self-service Waiting for Approval, satu-satunya pembawa status itu: Name `Proyektor Rapat {runId}`, Brand `Epson`, Model/Type `EB-X500`, Group `Ruang Rapat`, Status `Waiting for Approval`, TAG `NFC`, Category `Elektronik`, Borrower `Me`, Source `Self-service`, Duration `3 days`, Due Date `—`, Handed Over At `—`.
  - DU-215-4: pinjaman Admin Waiting for Handover atas nama Borrower tanpa akun yang PIC-nya Aktor, tanpa TAG: Name `Kamera Dokumentasi {runId}`, Brand `Canon`, Model/Type `EOS R50`, Group `Studio`, Status `Waiting for Handover`, TAG `—`, Category `Fotografi`, Borrower `Hendra Wijaya {runId}`, Source `Admin`, Duration `3 days`, Due Date `—`, Handed Over At `—`.
  - DU-215-5: pinjaman self-service Borrowed dengan Brand, Model, Group, dan TAG yang sama dengan DU-215-2: Name `Laptop Staf {runId}`, Brand `Dell`, Model/Type `Latitude 5440`, Group `Ruang IT`, Status `Borrowed`, TAG `RFID`, Category `Komputer`, Borrower `Me`, Source `Self-service`, Duration `2 days`, Due Date `T0 + 2 hari`, Handed Over At `T0`.
  - DU-215-6: pinjaman Admin dengan pengajuan Extend yang menunggu review, tanpa Brand dan Model: Name `Meja Lipat {runId}`, Brand `—`, Model/Type `—`, Group `Gudang Utama`, Status `Extension Request`, TAG `BLE`, Category `Furnitur`, Borrower `Me`, Source `Admin`, Duration `7 days`, Due Date `T0 + 7 hari`, Handed Over At `T0`.
  - DU-215-7: pinjaman self-service dengan pengajuan Extend yang menunggu approval: Name `Pengeras Suara {runId}`, Brand `JBL`, Model/Type `EON715`, Group `Ruang Rekam`, Status `Extension Approval`, TAG `NFC`, Category `Audio`, Borrower `Me`, Source `Self-service`, Duration `5 days`, Due Date `T0 + 5 hari`, Handed Over At `T0`.
  - DU-215-8: pinjaman Admin atas aset baru dengan Duration jam yang kemudian melewati Due date: Name `Server Rack {runId}`, Brand `Dell`, Model/Type `PowerEdge R250`, Group `Ruang Server`, Status `Overdue`, TAG `RFID`, Category `Komputer`, Borrower `Me`, Source `Admin`, Duration `2 hours`.
  - DU-215-9: Brand yang ada di master tetapi tidak dipakai baris tab mana pun: Name `Acer {runId}`.
  - DU-215-10: pinjaman Returned milik Aktor, status dan Brand yang tidak ada di tab Borrowed: Name `Mikrofon Studio {runId}`, Brand `Shure`, Model/Type `SM58`, Group `Ruang Rekam`, Status `Returned`, Holder `Me`, TAG `RFID`, Category `Audio`, Type `Borrow`, Handed Over At `T0`, Closed At `T0`.
  - DU-215-11: penugasan Unassigned atas nama Division yang PIC-nya Aktor: Name `Monitor Kerja {runId}`, Brand `Samsung`, Model/Type `S24C`, Group `Ruang Finance`, Status `Unassigned`, Holder `Divisi Keuangan {runId}`, TAG `NFC`, Category `Peripheral`, Type `Assignment`, Handed Over At `T0`, Closed At `T0`.
  - DU-215-12: pinjaman Rejected atas nama Borrower tanpa akun, tidak pernah diserahkan: Name `Printer Kantor {runId}`, Brand `Brother`, Model/Type `HL-L2320`, Group `Ruang Arsip`, Status `Rejected`, Holder `Hendra Wijaya {runId}`, TAG `—`, Category `Perangkat Cetak`, Type `Borrow`, Handed Over At `—`, Closed At `T0`.
  - DU-215-13: pinjaman Returned kedua atas aset bernama sama dengan DU-215-10: Name `Mikrofon Studio {runId}`, Brand `Shure`, Model/Type `SM58`, Group `Ruang Rekam`, Status `Returned`, Holder `Me`, TAG `RFID`, Category `Audio`, Type `Borrow`, Handed Over At `T0`, Closed At `T0`.
  - DU-215-14: pinjaman Returned dengan marker Damaged milik Aktor: Name `Speaker Aktif {runId}`, Brand `JBL`, Model/Type `EON715`, Group `Ruang Rekam`, Status `Returned · Damaged`, Holder `Me`, TAG `BLE`, Category `Audio`, Type `Borrow`, Handed Over At `T0`, Closed At `T0`.
  - DU-215-15: penugasan Assigned milik Aktor: Name `Notebook Staf {runId}`, Brand `Lenovo`, Model/Type `T14`, Group `Ruang Staf`, Status `Assigned`, Assigned To `Me`, TAG `RFID`, Category `Laptop`, Assigned Date `T0`, Assigned By `Siti Rahmawati {runId}`.
  - DU-215-16: penugasan Waiting for Handover atas nama Division yang PIC-nya Aktor: Name `Meja Rapat Besar {runId}`, Brand `Informa`, Model/Type `Oval 200`, Group `Ruang Direksi`, Status `Waiting for Handover`, Assigned To `Divisi Keuangan {runId}`, TAG `NFC`, Category `Furnitur`, Assigned Date `—`, Assigned By `—`.
  - DU-215-17: penugasan Assigned dengan laporan Damaged menunggu konfirmasi, tanpa TAG: Name `Dispenser Air {runId}`, Brand `Sanken`, Model/Type `HWD-770`, Group `Ruang Pantry`, Status `Assigned · Reported Damaged`, Assigned To `Me`, TAG `—`, Category `Elektronik`, Assigned Date `T0`, Assigned By `Agus Pratama {runId}`.
  - DU-215-18: Task Confirm Handover pinjaman dengan Total Asset terkecil: Transaction ID `nomor BRW milik DU-215-18`, Task `Confirm Handover`, Group `Ruang IT`, Total Asset `2`, Handed Over By `Budi Santoso {runId}`, Expires At `T0 + 1 hari`.
  - DU-215-19: Task Confirm Handover pinjaman dengan Total Asset di tengah rentang: Transaction ID `nomor BRW milik DU-215-19`, Task `Confirm Handover`, Group `Ruang Direksi`, Total Asset `5`, Handed Over By `Agus Pratama {runId}`, Expires At `T0 + 1 hari`.
  - DU-215-20: Task Confirm Handover pinjaman dengan Total Asset terbesar: Transaction ID `nomor BRW milik DU-215-20`, Task `Confirm Handover`, Group `Ruang IT`, Total Asset `9`, Handed Over By `Budi Santoso {runId}`, Expires At `T0 + 1 hari`.
  - DU-215-21: pinjaman Admin Borrowed dengan laporan Damaged dari Borrower yang menunggu konfirmasi, Brand, Model, Group, dan TAG sama dengan DU-215-2: Name `Laptop Cadangan {runId}`, Brand `Dell`, Model/Type `Latitude 5440`, Group `Ruang IT`, Status `Borrowed · Reported Damaged`, TAG `RFID`, Category `Komputer`, Borrower `Me`, Source `Admin`, Duration `10 days`, Due Date `T0 + 10 hari`, Handed Over At `T0`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`
  - T0 adalah tanggal run dan seluruh pinjaman serta penugasan di atas diserahkan atau ditutup pada T0
  - Kolom `TAG` dan `Category` tampil pada tabel yang difilter

## Test Steps

### Opsi filter tab Borrowed dipopulasi dari baris tab Borrowed saja
1. Aktor meminta opsi filter `Asset Name` tab Borrowed
2. Verifikasi opsi `Asset Name` memuat `Kamera Dokumentasi {runId}`, `Laptop Operasional {runId}`, `Laptop Cadangan {runId}`, `Laptop Staf {runId}`, `Meja Lipat {runId}`, `Pengeras Suara {runId}`, dan `Proyektor Rapat {runId}`, masing-masing satu kali
3. Aktor meminta opsi filter `Brand` tab Borrowed
4. Verifikasi opsi `Brand` memuat `Canon`, `Dell`, `Epson`, dan `JBL`, masing-masing satu kali, tidak memuat `Acer {runId}` yang ada di master tetapi tidak dipakai baris mana pun, dan tidak memuat `Shure` yang hanya dipakai baris tab History
5. Aktor meminta opsi filter `Model/Type` tab Borrowed
6. Verifikasi opsi `Model/Type` memuat `EB-X500`, `EON715`, `EOS R50`, dan `Latitude 5440`, masing-masing satu kali
7. Aktor meminta opsi filter `Group` tab Borrowed
8. Verifikasi opsi `Group` memuat `Gudang Utama`, `Ruang IT`, `Ruang Rapat`, `Ruang Rekam`, dan `Studio`, masing-masing satu kali
9. Aktor meminta opsi filter `Status` tab Borrowed
10. Verifikasi opsi `Status` memuat `Borrowed`, `Borrowed · Reported Damaged`, `Extension Approval`, `Extension Request`, `Waiting for Approval`, dan `Waiting for Handover`, masing-masing satu kali, dengan `Borrowed` dan `Borrowed · Reported Damaged` sebagai dua opsi terpisah, tidak memuat `Overdue` karena belum ada baris Overdue, dan tidak memuat `Returned` yang hanya dipakai baris tab History
11. Aktor meminta opsi filter `TAG` tab Borrowed
12. Verifikasi opsi `TAG` memuat `BLE`, `NFC`, dan `RFID`, masing-masing satu kali
13. Aktor meminta opsi filter `Category` tab Borrowed
14. Verifikasi opsi `Category` memuat `Audio`, `Elektronik`, `Fotografi`, `Furnitur`, dan `Komputer`, masing-masing satu kali
15. Aktor meminta opsi filter `Borrower` tab Borrowed
16. Verifikasi opsi `Borrower` memuat `Hendra Wijaya {runId}` (User), dan `Me`, masing-masing satu kali
17. Aktor meminta opsi filter `Source` tab Borrowed
18. Verifikasi opsi `Source` memuat `Admin`, dan `Self-service`, masing-masing satu kali

### Hasil filter tab Borrowed per field
19. Aktor meminta daftar tab Borrowed dengan filter `Asset Name` bernilai `Laptop Operasional {runId}`
20. Verifikasi hasil memuat baris DU-215-2 dan tidak memuat baris DU-215-3, DU-215-4, DU-215-5, DU-215-6, DU-215-7
21. Aktor meminta daftar tab Borrowed dengan filter `Brand` bernilai `Dell`
22. Verifikasi hasil memuat baris DU-215-2, DU-215-5, DU-215-21 dan tidak memuat baris DU-215-3, DU-215-4, DU-215-6, DU-215-7
23. Aktor meminta daftar tab Borrowed dengan filter `Model/Type` bernilai `EB-X500`
24. Verifikasi hasil memuat baris DU-215-3 dan tidak memuat baris DU-215-2, DU-215-4, DU-215-5, DU-215-6, DU-215-7
25. Aktor meminta daftar tab Borrowed dengan filter `Group` bernilai `Ruang IT`
26. Verifikasi hasil memuat baris DU-215-2, DU-215-5, DU-215-21 dan tidak memuat baris DU-215-3, DU-215-4, DU-215-6, DU-215-7
27. Aktor meminta daftar tab Borrowed dengan filter `Status` bernilai `Borrowed`
28. Verifikasi hasil memuat baris DU-215-2, DU-215-5 dan tidak memuat baris DU-215-3, DU-215-4, DU-215-6, DU-215-7, DU-215-21
29. Aktor meminta daftar tab Borrowed dengan filter `TAG` bernilai `NFC`
30. Verifikasi hasil memuat baris DU-215-3, DU-215-7 dan tidak memuat baris DU-215-2, DU-215-4, DU-215-5, DU-215-6
31. Aktor meminta daftar tab Borrowed dengan filter `Category` bernilai `Fotografi`
32. Verifikasi hasil memuat baris DU-215-4 dan tidak memuat baris DU-215-2, DU-215-3, DU-215-5, DU-215-6, DU-215-7
33. Aktor meminta daftar tab Borrowed dengan filter `Borrower` bernilai `Hendra Wijaya {runId}` (User)
34. Verifikasi hasil memuat baris DU-215-4 dan tidak memuat baris DU-215-2, DU-215-3, DU-215-5, DU-215-6, DU-215-7
35. Aktor meminta daftar tab Borrowed dengan filter `Source` bernilai `Self-service`
36. Verifikasi hasil memuat baris DU-215-3, DU-215-5, DU-215-7 dan tidak memuat baris DU-215-2, DU-215-4, DU-215-6

### Filter satu field memakai OR dan antar-field memakai AND di tab Borrowed
37. Aktor meminta daftar tab Borrowed dengan filter `Status` bernilai `Waiting for Approval`, dan `Waiting for Handover`
38. Verifikasi hasil memuat baris DU-215-3, DU-215-4 dan tidak memuat baris DU-215-2, DU-215-5, DU-215-6, DU-215-7
39. Aktor meminta daftar tab Borrowed dengan filter `Brand` bernilai `Dell`, dan `Epson`
40. Verifikasi hasil memuat baris DU-215-2, DU-215-3, DU-215-5, DU-215-21 dan tidak memuat baris DU-215-4, DU-215-6, DU-215-7
41. Aktor meminta daftar tab Borrowed dengan filter `Brand` bernilai `Dell` dan filter `Source` bernilai `Self-service`
42. Verifikasi hasil memuat baris DU-215-5 dan tidak memuat baris DU-215-2, DU-215-3, DU-215-4, DU-215-6, DU-215-7
43. Aktor meminta daftar tab Borrowed dengan filter `Brand` bernilai `Dell` dan filter `Status` bernilai `Waiting for Approval`
44. Verifikasi hasil saringan tidak memuat baris apa pun dari tab Borrowed

### Filter rentang tanggal tab Borrowed
45. Aktor meminta daftar tab Borrowed dengan filter `Due Date` dari T0 + 2 hari sampai T0 + 3 hari
46. Verifikasi hasil memuat baris DU-215-2, DU-215-5 dan tidak memuat baris DU-215-3, DU-215-4, DU-215-6, DU-215-7
47. Aktor meminta daftar tab Borrowed dengan filter `Due Date` dari T0 + 4 hari sampai T0 + 6 hari
48. Verifikasi hasil memuat baris DU-215-7 dan tidak memuat baris DU-215-2, DU-215-3, DU-215-4, DU-215-5, DU-215-6
49. Aktor meminta daftar tab Borrowed dengan filter `Due Date` dari T0 + 8 hari sampai T0 + 9 hari
50. Verifikasi hasil saringan tidak memuat baris apa pun dari tab Borrowed
51. Aktor meminta daftar tab Borrowed dengan filter `Handed Over At` dari T0 sampai T0
52. Verifikasi hasil memuat baris DU-215-2, DU-215-5, DU-215-6, DU-215-7, DU-215-21 dan tidak memuat baris DU-215-3, DU-215-4
53. Aktor meminta daftar tab Borrowed dengan filter `Handed Over At` dari T0 − 7 hari sampai T0 − 1 hari
54. Verifikasi hasil saringan tidak memuat baris apa pun dari tab Borrowed
55. Aktor meminta daftar tab Borrowed dan membaca kolom `Extensions` baris DU-215-2
56. Verifikasi nilai kolom `Extensions` baris DU-215-2 berupa `[terpakai] / [maks]`, dan hasil filter kolom ini tidak diasersi karena angka yang dipakai belum ditetapkan

### Opsi filter tab History dipopulasi dari baris tab History saja
57. Aktor meminta opsi filter `Asset Name` tab History
58. Verifikasi opsi `Asset Name` memuat `Mikrofon Studio {runId}`, `Monitor Kerja {runId}`, `Printer Kantor {runId}`, dan `Speaker Aktif {runId}`, masing-masing satu kali
59. Aktor meminta opsi filter `Brand` tab History
60. Verifikasi opsi `Brand` memuat `Brother`, `JBL`, `Samsung`, dan `Shure`, masing-masing satu kali, dan tidak memuat `Dell` yang hanya dipakai baris tab Borrowed
61. Aktor meminta opsi filter `Model/Type` tab History
62. Verifikasi opsi `Model/Type` memuat `EON715`, `HL-L2320`, `S24C`, dan `SM58`, masing-masing satu kali
63. Aktor meminta opsi filter `Group` tab History
64. Verifikasi opsi `Group` memuat `Ruang Arsip`, `Ruang Finance`, dan `Ruang Rekam`, masing-masing satu kali
65. Aktor meminta opsi filter `Status` tab History
66. Verifikasi opsi `Status` memuat `Rejected`, `Returned`, `Returned · Damaged`, dan `Unassigned`, masing-masing satu kali, dan tidak memuat `Borrowed`, `Waiting for Approval`, maupun `Overdue` yang hanya dipakai baris tab Borrowed, dengan `Returned` dan `Returned · Damaged` sebagai dua opsi terpisah
67. Aktor meminta opsi filter `Holder` tab History
68. Verifikasi opsi `Holder` memuat `Divisi Keuangan {runId}` (Division), `Hendra Wijaya {runId}` (User), dan `Me`, masing-masing satu kali
69. Aktor meminta opsi filter `TAG` tab History
70. Verifikasi opsi `TAG` memuat `BLE`, `NFC`, dan `RFID`, masing-masing satu kali
71. Aktor meminta opsi filter `Category` tab History
72. Verifikasi opsi `Category` memuat `Audio`, `Perangkat Cetak`, dan `Peripheral`, masing-masing satu kali
73. Aktor meminta opsi filter `Type` tab History
74. Verifikasi opsi `Type` memuat `Assignment`, dan `Borrow`, masing-masing satu kali

### Hasil filter tab History per field
75. Aktor meminta daftar tab History dengan filter `Asset Name` bernilai `Mikrofon Studio {runId}`
76. Verifikasi hasil memuat baris DU-215-10, DU-215-13 dan tidak memuat baris DU-215-11, DU-215-12, DU-215-14
77. Aktor meminta daftar tab History dengan filter `Brand` bernilai `Shure`
78. Verifikasi hasil memuat baris DU-215-10, DU-215-13 dan tidak memuat baris DU-215-11, DU-215-12, DU-215-14
79. Aktor meminta daftar tab History dengan filter `Model/Type` bernilai `HL-L2320`
80. Verifikasi hasil memuat baris DU-215-12 dan tidak memuat baris DU-215-10, DU-215-11, DU-215-13, DU-215-14
81. Aktor meminta daftar tab History dengan filter `Group` bernilai `Ruang Rekam`
82. Verifikasi hasil memuat baris DU-215-10, DU-215-13, DU-215-14 dan tidak memuat baris DU-215-11, DU-215-12
83. Aktor meminta daftar tab History dengan filter `Status` bernilai `Returned`
84. Verifikasi hasil memuat baris DU-215-10, DU-215-13 dan tidak memuat baris DU-215-11, DU-215-12, DU-215-14
85. Aktor meminta daftar tab History dengan filter `Status` bernilai `Returned · Damaged`
86. Verifikasi hasil memuat baris DU-215-14 dan tidak memuat baris DU-215-10, DU-215-11, DU-215-12, DU-215-13
87. Aktor meminta daftar tab History dengan filter `Holder` bernilai `Divisi Keuangan {runId}` (Division)
88. Verifikasi hasil memuat baris DU-215-11 dan tidak memuat baris DU-215-10, DU-215-12, DU-215-13, DU-215-14
89. Aktor meminta daftar tab History dengan filter `TAG` bernilai `BLE`
90. Verifikasi hasil memuat baris DU-215-14 dan tidak memuat baris DU-215-10, DU-215-11, DU-215-12, DU-215-13
91. Aktor meminta daftar tab History dengan filter `Category` bernilai `Audio`
92. Verifikasi hasil memuat baris DU-215-10, DU-215-13, DU-215-14 dan tidak memuat baris DU-215-11, DU-215-12
93. Aktor meminta daftar tab History dengan filter `Type` bernilai `Assignment`
94. Verifikasi hasil memuat baris DU-215-11 dan tidak memuat baris DU-215-10, DU-215-12, DU-215-13, DU-215-14

### Filter satu field memakai OR dan antar-field memakai AND di tab History
95. Aktor meminta daftar tab History dengan filter `Type` bernilai `Assignment`, dan `Borrow` dan filter `Status` bernilai `Rejected`, dan `Unassigned`
96. Verifikasi hasil memuat baris DU-215-11, DU-215-12 dan tidak memuat baris DU-215-10, DU-215-13, DU-215-14
97. Aktor meminta daftar tab History dengan filter `Brand` bernilai `Shure` dan filter `Status` bernilai `Returned` dan filter `Holder` bernilai `Me`
98. Verifikasi hasil memuat baris DU-215-10, DU-215-13 dan tidak memuat baris DU-215-11, DU-215-12, DU-215-14

### Filter rentang tanggal tab History
99. Aktor meminta daftar tab History dengan filter `Handed Over At` dari T0 sampai T0
100. Verifikasi hasil memuat baris DU-215-10, DU-215-11, DU-215-13, DU-215-14 dan tidak memuat baris DU-215-12
101. Aktor meminta daftar tab History dengan filter `Handed Over At` dari T0 − 30 hari sampai T0 − 1 hari
102. Verifikasi hasil saringan tidak memuat baris apa pun dari tab History
103. Aktor meminta daftar tab History dengan filter `Closed At` dari T0 sampai T0
104. Verifikasi hasil memuat baris DU-215-10, DU-215-11, DU-215-12, DU-215-13, DU-215-14
105. Aktor meminta daftar tab History dengan filter `Closed At` dari T0 − 30 hari sampai T0 − 1 hari
106. Verifikasi hasil saringan tidak memuat baris apa pun dari tab History

### Opsi filter tab Assigned dipopulasi dari baris tab Assigned saja
107. Aktor meminta opsi filter `Asset Name` tab Assigned
108. Verifikasi opsi `Asset Name` memuat `Dispenser Air {runId}`, `Meja Rapat Besar {runId}`, dan `Notebook Staf {runId}`, masing-masing satu kali
109. Aktor meminta opsi filter `Brand` tab Assigned
110. Verifikasi opsi `Brand` memuat `Informa`, `Lenovo`, dan `Sanken`, masing-masing satu kali
111. Aktor meminta opsi filter `Model/Type` tab Assigned
112. Verifikasi opsi `Model/Type` memuat `HWD-770`, `Oval 200`, dan `T14`, masing-masing satu kali
113. Aktor meminta opsi filter `Group` tab Assigned
114. Verifikasi opsi `Group` memuat `Ruang Direksi`, `Ruang Pantry`, dan `Ruang Staf`, masing-masing satu kali
115. Aktor meminta opsi filter `Status` tab Assigned
116. Verifikasi opsi `Status` memuat `Assigned`, `Assigned · Reported Damaged`, dan `Waiting for Handover`, masing-masing satu kali, dan `Assigned` serta `Assigned · Reported Damaged` tampil sebagai dua opsi terpisah
117. Aktor meminta opsi filter `Assigned To` tab Assigned
118. Verifikasi opsi `Assigned To` memuat `Divisi Keuangan {runId}` (Division), dan `Me`, masing-masing satu kali
119. Aktor meminta opsi filter `TAG` tab Assigned
120. Verifikasi opsi `TAG` memuat `NFC`, dan `RFID`, masing-masing satu kali
121. Aktor meminta opsi filter `Category` tab Assigned
122. Verifikasi opsi `Category` memuat `Elektronik`, `Furnitur`, dan `Laptop`, masing-masing satu kali
123. Aktor meminta opsi filter `Assigned By` tab Assigned
124. Verifikasi opsi `Assigned By` memuat `Agus Pratama {runId}`, dan `Siti Rahmawati {runId}`, masing-masing satu kali

### Hasil filter tab Assigned per field
125. Aktor meminta daftar tab Assigned dengan filter `Asset Name` bernilai `Notebook Staf {runId}`
126. Verifikasi hasil memuat baris DU-215-15 dan tidak memuat baris DU-215-16, DU-215-17
127. Aktor meminta daftar tab Assigned dengan filter `Brand` bernilai `Informa`
128. Verifikasi hasil memuat baris DU-215-16 dan tidak memuat baris DU-215-15, DU-215-17
129. Aktor meminta daftar tab Assigned dengan filter `Model/Type` bernilai `HWD-770`
130. Verifikasi hasil memuat baris DU-215-17 dan tidak memuat baris DU-215-15, DU-215-16
131. Aktor meminta daftar tab Assigned dengan filter `Group` bernilai `Ruang Staf`
132. Verifikasi hasil memuat baris DU-215-15 dan tidak memuat baris DU-215-16, DU-215-17
133. Aktor meminta daftar tab Assigned dengan filter `Status` bernilai `Assigned`
134. Verifikasi hasil memuat baris DU-215-15 dan tidak memuat baris DU-215-16, DU-215-17
135. Aktor meminta daftar tab Assigned dengan filter `Status` bernilai `Assigned · Reported Damaged`
136. Verifikasi hasil memuat baris DU-215-17 dan tidak memuat baris DU-215-15, DU-215-16
137. Aktor meminta daftar tab Assigned dengan filter `Assigned To` bernilai `Divisi Keuangan {runId}` (Division)
138. Verifikasi hasil memuat baris DU-215-16 dan tidak memuat baris DU-215-15, DU-215-17
139. Aktor meminta daftar tab Assigned dengan filter `TAG` bernilai `RFID`
140. Verifikasi hasil memuat baris DU-215-15 dan tidak memuat baris DU-215-16, DU-215-17
141. Aktor meminta daftar tab Assigned dengan filter `Category` bernilai `Furnitur`
142. Verifikasi hasil memuat baris DU-215-16 dan tidak memuat baris DU-215-15, DU-215-17
143. Aktor meminta daftar tab Assigned dengan filter `Assigned By` bernilai `Agus Pratama {runId}`
144. Verifikasi hasil memuat baris DU-215-17 dan tidak memuat baris DU-215-15, DU-215-16

### Filter satu field memakai OR dan antar-field memakai AND di tab Assigned
145. Aktor meminta daftar tab Assigned dengan filter `Assigned To` bernilai `Me`, dan `Divisi Keuangan {runId}` (Division) dan filter `Category` bernilai `Elektronik`
146. Verifikasi hasil memuat baris DU-215-17 dan tidak memuat baris DU-215-15, DU-215-16
147. Aktor meminta daftar tab Assigned dengan filter `Status` bernilai `Assigned`, dan `Waiting for Handover` dan filter `Assigned To` bernilai `Me`
148. Verifikasi hasil memuat baris DU-215-15 dan tidak memuat baris DU-215-16, DU-215-17

### Filter rentang tanggal tab Assigned
149. Aktor meminta daftar tab Assigned dengan filter `Assigned Date` dari T0 sampai T0
150. Verifikasi hasil memuat baris DU-215-15, DU-215-17 dan tidak memuat baris DU-215-16
151. Aktor meminta daftar tab Assigned dengan filter `Assigned Date` dari T0 − 30 hari sampai T0 − 1 hari
152. Verifikasi hasil saringan tidak memuat baris apa pun dari tab Assigned

### Opsi dan hasil filter tab Task per field
153. Aktor meminta opsi filter `Task` tab Task
154. Verifikasi opsi `Task` memuat `Confirm Handover`, masing-masing satu kali
155. Aktor meminta opsi filter `Group` tab Task
156. Verifikasi opsi `Group` memuat `Ruang Direksi`, dan `Ruang IT`, masing-masing satu kali, dan `Ruang IT` yang dipakai dua baris hanya tampil satu kali
157. Aktor meminta opsi filter `Handed Over By` tab Task
158. Verifikasi opsi `Handed Over By` memuat `Agus Pratama {runId}`, dan `Budi Santoso {runId}`, masing-masing satu kali
159. Aktor meminta daftar tab Task dengan filter `Task` bernilai `Confirm Handover`
160. Verifikasi hasil memuat baris DU-215-18, DU-215-19, DU-215-20
161. Aktor meminta daftar tab Task dengan filter `Group` bernilai `Ruang IT`
162. Verifikasi hasil memuat baris DU-215-18, DU-215-20 dan tidak memuat baris DU-215-19
163. Aktor meminta daftar tab Task dengan filter `Handed Over By` bernilai `Agus Pratama {runId}`
164. Verifikasi hasil memuat baris DU-215-19 dan tidak memuat baris DU-215-18, DU-215-20
165. Aktor meminta daftar tab Task dengan filter `Group` bernilai `Ruang IT` dan filter `Handed Over By` bernilai `Budi Santoso {runId}`
166. Verifikasi hasil memuat baris DU-215-18, DU-215-20 dan tidak memuat baris DU-215-19
167. Aktor meminta daftar tab Task dengan filter `Group` bernilai `Ruang Direksi`, dan `Ruang IT` dan filter `Handed Over By` bernilai `Agus Pratama {runId}`
168. Verifikasi hasil memuat baris DU-215-19 dan tidak memuat baris DU-215-18, DU-215-20
169. Aktor meminta daftar tab Task dengan filter `Expires At` dari T0 sampai T0 + 30 hari
170. Verifikasi hasil memuat baris DU-215-18, DU-215-19, DU-215-20
171. Aktor meminta daftar tab Task dengan filter `Expires At` dari T0 − 30 hari sampai T0 − 1 hari
172. Verifikasi hasil saringan tidak memuat baris apa pun dari tab Task

### Filter rentang Total Asset tab Task inklusif di kedua ujung dan boleh hanya satu ujung
173. Aktor meminta daftar tab Task dengan filter `Total Asset` dengan Min 5 dan Max 8
174. Verifikasi hasil memuat baris DU-215-19 dan tidak memuat baris DU-215-18, DU-215-20
175. Aktor meminta daftar tab Task dengan filter `Total Asset` dengan Min 3 dan Max 5
176. Verifikasi hasil memuat baris DU-215-19 dan tidak memuat baris DU-215-18, DU-215-20
177. Aktor meminta daftar tab Task dengan filter `Total Asset` hanya dengan Min 5
178. Verifikasi hasil memuat baris DU-215-19, DU-215-20 dan tidak memuat baris DU-215-18
179. Aktor meminta daftar tab Task dengan filter `Total Asset` hanya dengan Max 5
180. Verifikasi hasil memuat baris DU-215-18, DU-215-19 dan tidak memuat baris DU-215-20
181. Aktor meminta daftar tab Task dengan filter `Total Asset` dengan Min 10 dan Max 20
182. Verifikasi hasil saringan tidak memuat baris apa pun dari tab Task

### Opsi Status tab Borrowed mengikuti perubahan data: nilai baru muncul dan nilai tanpa pembawa hilang
183. Aktor Borrow membuat pinjaman Admin atas `Server Rack {runId}` dengan Duration `2 hours` untuk Aktor, dan Aktor mengonfirmasi Handover
184. Waktu berlalu sampai Due date pinjaman DU-215-8 terlewati
185. Aktor meminta opsi filter `Status` tab Borrowed
186. Verifikasi opsi `Status` memuat `Borrowed`, `Borrowed · Reported Damaged`, `Extension Approval`, `Extension Request`, `Overdue`, `Waiting for Approval`, dan `Waiting for Handover`, masing-masing satu kali, dengan `Overdue` sebagai opsi baru dan keenam status `Waiting for Approval`, `Waiting for Handover`, `Borrowed`, `Overdue`, `Extension Request`, dan `Extension Approval` masing-masing memiliki baris
187. Aktor membatalkan pinjaman DU-215-3 lewat aksi Cancel Borrow
188. Aktor meminta opsi filter `Status` tab Borrowed
189. Verifikasi opsi `Status` memuat `Borrowed`, `Borrowed · Reported Damaged`, `Extension Approval`, `Extension Request`, `Overdue`, dan `Waiting for Handover`, masing-masing satu kali, dan tidak lagi memuat `Waiting for Approval` karena pembawa terakhirnya sudah pindah ke tab History
190. Aktor meminta opsi filter `Status` tab History
191. Verifikasi opsi `Status` memuat `Canceled`, `Rejected`, `Returned`, `Returned · Damaged`, dan `Unassigned`, masing-masing satu kali, dengan `Canceled` sebagai opsi baru dari DU-215-3

### Filter Status memakai kombinasi badge yang sama persis di tab Borrowed
192. Aktor meminta daftar tab Borrowed dengan filter `Status` bernilai `Borrowed · Reported Damaged`
193. Verifikasi hasil memuat baris DU-215-21 dan tidak memuat baris DU-215-2, DU-215-5, DU-215-7
