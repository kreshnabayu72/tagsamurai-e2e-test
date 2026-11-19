---
id: TC-FA-BORROW-E2E-033-gating-monitoring-read-only
title: "Monitoring & Report dan Read Only hanya membaca dan Download tanpa aksi tulis"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§2.1#r13", "§2.1#r14", "§2.1#r15", "§2.1#r16", "§2.1#r17", "§2.1#r18", "§4.1l#p4", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17", "§4.8#r18", EB-AKS-4]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [9, 14, 58, 63]
  "§2.1#r2": [12, 61]
  "§2.1#r3": [5, 7, 56]
  "§2.1#r4": [5, 7, 56]
  "§2.1#r5": [17, 73]
  "§2.1#r6": [2, 53]
  "§2.1#r7": [15, 64]
  "§2.1#r8": [16]
  "§2.1#r9": [20]
  "§2.1#r10": [34, 83]
  "§2.1#r11": [24]
  "§2.1#r12": [27]
  "§2.1#r13": [37, 86]
  "§2.1#r14": [21, 32, 81]
  "§2.1#r15": [50]
  "§2.1#r16": [33, 82]
  "§2.1#r17": [11, 60]
  "§2.1#r18": [9, 10, 58, 59]
  "§4.1l#p4": [5, 7, 56]
  "§4.8#r1": [1, 4, 52, 55]
  "§4.8#r2": [5, 7, 56]
  "§4.8#r3": [32, 33, 81, 82]
  "§4.8#r4": [12, 40, 45, 46, 61, 89, 94, 95]
  "§4.8#r5": [5]
  "§4.8#r6": [5]
  "§4.8#r7": [17, 73]
  "§4.8#r8": [15, 21, 33, 64, 76, 81, 82]
  "§4.8#r9": [50]
  "§4.8#r10": [16]
  "§4.8#r11": [20]
  "§4.8#r12": [24]
  "§4.8#r13": [27]
  "§4.8#r14": [37, 86]
  "§4.8#r15": [34, 83]
  "§4.8#r16": [2, 53]
  "§4.8#r17": [2]
  "§4.8#r18": [11, 60]
  EB-AKS-4: [58, 65, 66, 67, 68]
anchor: [19, 23, 26, 31, 36, 39, 44, 49, 72, 75, 80, 85, 88, 93]
coverage:
  web: automated
---

# Monitoring & Report dan Read Only hanya membaca dan Download tanpa aksi tulis

## Prerequisites
- Aktor: Monitoring & Report (cakupan Group penugasan `Head Office {runId}`), lalu Read Only (cakupan seluruh client) pada langkah «Masuk sebagai Read Only».
- Layar awal: halaman utama aplikasi Fixed Asset.
- Data:
  - DU-033-1: User `Nina Rahayu {runId}`, role Monitoring & Report, Group penugasan `Head Office {runId}`, aktif.
  - DU-033-2: User `Tomi Wijaya {runId}`, role Read Only, cakupan seluruh client, aktif.
  - DU-033-3: User `Rina Wulandari {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif.
  - DU-033-4: Karyawan `Rudi Hartono {runId}`, aktif, Home Group `Head Office {runId}`.
  - DU-033-5: Karyawan `Dewi Lestari {runId}`, aktif, Home Group `Branch Surabaya {runId}`.
  - DU-033-6: Group `Head Office {runId}`, penugasan `Nina Rahayu {runId}`.
  - DU-033-7: Group `Branch Surabaya {runId}`, bukan penugasan `Nina Rahayu {runId}`.
  - DU-033-8: Aset `Laptop Lenovo T14 {runId}`, Group `Head Office {runId}`, status Available.
  - DU-033-9: BRW berstatus Waiting for Handover, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Duration `3 days`, Purpose `Kunjungan klien`, Requested By `Rina Wulandari {runId}`.
  - DU-033-10: BRW berstatus Borrowed, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Toyota Avanza {runId}`, Duration `5 days`, Purpose `Survei lokasi`, Requested By `Rina Wulandari {runId}`.
  - DU-033-11: BRW berstatus Extension Approval (Extend menunggu approval), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Projector Epson EB-X06 {runId}`, Duration `4 days`, Purpose `Presentasi vendor`, Requested By `Rina Wulandari {runId}`.
  - DU-033-12: BRW berstatus Extension Request (pengajuan Extend dari My Asset menunggu review), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Printer Canon G3010 {runId}`, Duration `4 days`, Purpose `Cetak dokumen audit`, Requested By `Rina Wulandari {runId}`.
  - DU-033-13: BRW berstatus Borrowed dengan Damage Report Waiting for Confirmation yang dilaporkan `Rina Wulandari {runId}`, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Excavator Komatsu PC200 {runId}`, Duration `6 days`, Purpose `Pekerjaan galian`, Requested By `Rina Wulandari {runId}`.
  - DU-033-14: BRW berstatus Borrowed, Group `Branch Surabaya {runId}`, Borrower `Dewi Lestari {runId}`, aset `Genset Perkins 20 kVA {runId}`, Duration `7 days`, Purpose `Cadangan listrik`, Requested By `Rina Wulandari {runId}`.
  - DU-033-15: Draft milik Borrower `Rudi Hartono {runId}`, berisi aset `Scanner Epson DS-530 {runId}` (Group `Head Office {runId}`), Total Asset `1`, Modified By `Rina Wulandari {runId}`.
- Kondisi:
  - Level Feature Suite Borrowing entitas aktor bernilai `Full`.
  - Akun `Tomi Wijaya {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Monitoring & Report: menu Borrow tampil dan menu Approvals > Borrow tidak tampil
1. Verifikasi menu `Transactions > Borrow` tampil di sidebar
2. Verifikasi menu `Approvals > Borrow` tidak tampil di sidebar
3. Klik menu `Transactions > Borrow`
4. Verifikasi tab `Transactions`, `Borrowed Assets`, dan `History` tampil
5. Verifikasi tab `Drafts` tidak tampil

### Monitoring & Report: URL ke tab Drafts menampilkan tab Transactions
6. Buka URL halaman Borrow dengan `?tab=drafts` secara langsung
7. Verifikasi tab `Transactions` yang tampil sebagai gantinya

### Monitoring & Report: tab Transactions hanya membaca dan Download
8. Ketik Search `{runId}`, tekan Enter
9. Verifikasi BRW milik DU-033-9 dengan Group `Head Office {runId}` tampil di tabel
10. Verifikasi BRW milik DU-033-14 dengan Group `Branch Surabaya {runId}` tidak tampil di tabel
11. Verifikasi `Download` tampil di toolbar tab `Transactions`
12. Verifikasi tombol `[+ Borrow]` tidak tampil di toolbar tab `Transactions`
13. Buka menu ⋯ pada baris BRW milik DU-033-9
14. Verifikasi aksi `Detail` tampil dan aktif
15. Verifikasi aksi `Hand Over` tidak tampil
16. Verifikasi aksi `Remind Borrower` tidak tampil
17. Verifikasi aksi `Cancel Borrow` tidak tampil
18. Buka menu ⋯ pada baris BRW milik DU-033-10
19. Verifikasi aksi `Detail` tampil pada baris BRW yang Borrowed
20. Verifikasi aksi `Request Extension` tidak tampil
21. Verifikasi aksi `Return` tidak tampil
22. Buka menu ⋯ pada baris BRW milik DU-033-11
23. Verifikasi aksi `Detail` tampil pada baris BRW dengan Extension Approval
24. Verifikasi aksi `Cancel Extension` tidak tampil
25. Buka menu ⋯ pada baris BRW milik DU-033-12
26. Verifikasi aksi `Detail` tampil pada baris BRW dengan Extension Request
27. Verifikasi aksi `Review` tidak tampil

### Monitoring & Report: tab Borrowed Assets hanya membaca
28. Klik tab `Borrowed Assets`
29. Ketik Search `{runId}`, tekan Enter
30. Buka menu ⋯ pada baris aset `Toyota Avanza {runId}`
31. Verifikasi aksi `Borrow Log` tampil pada baris aset yang Borrowed
32. Verifikasi aksi `Return` tidak tampil pada baris aset yang Borrowed
33. Verifikasi aksi `Report Missing` tidak tampil
34. Verifikasi aksi `Report Damaged` tidak tampil
35. Buka menu ⋯ pada baris aset `Excavator Komatsu PC200 {runId}`
36. Verifikasi aksi `Borrow Log` tampil pada baris aset dengan Damage Report
37. Verifikasi aksi `Cancel Damage Report` tidak tampil

### Monitoring & Report: Quick Action tanpa item Borrow
38. Buka menu Quick Action pada navbar
39. Verifikasi menu Quick Action terbuka untuk Monitoring & Report
40. Verifikasi item `Borrow` tidak tampil di menu Quick Action untuk Monitoring & Report

### Monitoring & Report: tabel aset tanpa aksi Borrow dan Mark as Returned
41. Klik menu `Assets > All`
42. Ketik Search `{runId}`, tekan Enter
43. Buka menu ⋯ pada baris aset `Laptop Lenovo T14 {runId}`
44. Verifikasi aset `Laptop Lenovo T14 {runId}` berstatus `Available` tampil di tabel aset
45. Verifikasi aksi `Borrow` tidak tampil
46. Verifikasi aksi `Add to Borrow Draft` tidak tampil
47. Ganti isi kotak search dengan `Toyota Avanza {runId}`, tekan Enter
48. Buka menu ⋯ pada baris aset `Toyota Avanza {runId}`
49. Verifikasi aset `Toyota Avanza {runId}` berstatus `Borrowed` tampil di tabel aset
50. Verifikasi aksi `Mark as Returned` tidak tampil karena level Feature Suite Borrowing bukan `None`

### Read Only: menu dan tab Borrow
51. Masuk sebagai Read Only `Tomi Wijaya {runId}`
52. Verifikasi menu `Transactions > Borrow` tampil di sidebar untuk Read Only
53. Verifikasi menu `Approvals > Borrow` tidak tampil di sidebar untuk Read Only
54. Klik menu `Transactions > Borrow`
55. Verifikasi tab `Transactions`, `Borrowed Assets`, dan `History` tampil untuk Read Only
56. Verifikasi tab `Drafts` tidak tampil untuk Read Only

### Read Only: cakupan seluruh client, hanya membaca dan Download
57. Ketik Search `{runId}`, tekan Enter
58. Verifikasi BRW milik DU-033-9 dengan Group `Head Office {runId}` tampil di tabel untuk Read Only
59. Verifikasi BRW milik DU-033-14 dengan Group `Branch Surabaya {runId}` tampil di tabel untuk Read Only
60. Verifikasi `Download` tampil di toolbar tab `Transactions` untuk Read Only
61. Verifikasi tombol `[+ Borrow]` tidak tampil di toolbar tab `Transactions` untuk Read Only
62. Buka menu ⋯ pada baris BRW milik DU-033-9
63. Verifikasi aksi `Detail` tampil dan aktif untuk Read Only
64. Verifikasi aksi `Hand Over` tidak tampil untuk Read Only

### Read Only: Search, Filter, Sort, Pagination, dan Setup Column tampil dan aktif
65. Verifikasi tombol `Filter` tampil dan aktif di toolbar tab `Transactions`
66. Verifikasi kontrol sort pada header kolom `Transaction ID` tampil dan aktif
67. Verifikasi paginasi `Table pagination` tampil dan aktif
68. Verifikasi tombol `Column Visibility` tampil dan aktif di header tabel

### Read Only: aksi tulis baris BRW dan baris aset tidak tampil
69. Klik tab `Transactions`
70. Ketik Search `{runId}`, tekan Enter
71. Buka menu ⋯ pada baris BRW milik DU-033-9
72. Verifikasi aksi `Detail` tampil pada baris BRW yang Waiting for Handover untuk Read Only
73. Verifikasi aksi `Cancel Borrow` tidak tampil untuk Read Only
74. Buka menu ⋯ pada baris BRW milik DU-033-10
75. Verifikasi aksi `Detail` tampil pada baris BRW yang Borrowed untuk Read Only
76. Verifikasi aksi `Return` tidak tampil pada baris BRW untuk Read Only
77. Klik tab `Borrowed Assets`
78. Ketik Search `{runId}`, tekan Enter
79. Buka menu ⋯ pada baris aset `Toyota Avanza {runId}`
80. Verifikasi aksi `Borrow Log` tampil pada baris aset yang Borrowed untuk Read Only
81. Verifikasi aksi `Return` tidak tampil pada baris aset yang Borrowed untuk Read Only
82. Verifikasi aksi `Report Missing` tidak tampil untuk Read Only
83. Verifikasi aksi `Report Damaged` tidak tampil untuk Read Only
84. Buka menu ⋯ pada baris aset `Excavator Komatsu PC200 {runId}`
85. Verifikasi aksi `Borrow Log` tampil pada baris aset dengan Damage Report untuk Read Only
86. Verifikasi aksi `Cancel Damage Report` tidak tampil untuk Read Only

### Read Only: Quick Action dan Asset List tanpa aksi Borrow
87. Buka menu Quick Action pada navbar
88. Verifikasi menu Quick Action terbuka untuk Read Only
89. Verifikasi item `Borrow` tidak tampil di menu Quick Action untuk Read Only
90. Klik menu `Assets > All`
91. Ketik Search `{runId}`, tekan Enter
92. Buka menu ⋯ pada baris aset `Laptop Lenovo T14 {runId}`
93. Verifikasi baris aset `Laptop Lenovo T14 {runId}` tampil di tabel aset untuk Read Only
94. Verifikasi aksi `Borrow` tidak tampil untuk Read Only
95. Verifikasi aksi `Add to Borrow Draft` tidak tampil untuk Read Only
