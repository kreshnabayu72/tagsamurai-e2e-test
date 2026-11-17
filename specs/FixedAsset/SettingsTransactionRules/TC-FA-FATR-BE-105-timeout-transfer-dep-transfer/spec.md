---
id: TC-FA-FATR-BE-105-timeout-transfer-dep-transfer
title: "Transaction timeout dan versi setting pada transaksi Transfer"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§Aturan Logika Modul#r5", "§Aturan Logika Modul#r30", "§Aturan Logika Modul#r31", "§Aturan Logika Modul#r40", "§9.2#b128", "§9.2#b140", "§9.2#b201", "§9.2#b203", "§9.2#b205", "§9.2#b206", "§9.2#b207", "§9.2#b208", "§9.2#b213", "§9.2#b215", "§9.2#b217", "§9.2#b218", "§9.2#b219", "§9.2#b221", "§9.2#b225", "§9.2#b275", "§9.2#b276", "§9.2#b277", "§9.2#b278", "§9.2#b279", "§9.2#b280", "§9.2#b284", "§9.2#b290", "§9.2#b293", "§9.2#b300", "§9.2#b383", "§9.2#b395", "§9.2#b396", "§9.2#b436", "§9.2#b438", "§9.2#b418", "§9.4.2#r46", "§9.4.2#r135", "§9.4.2#r137", "§9.4.2#r147", "§9.4.2#r150", "§9.4.2#r151", "§9.4.3#b10", "§9.4.4#r37", "§9.6#r5", "§9.7#r2", "§9.7#r11", "§9.7#r22", "§9.7#r31", "§9.10.1#b8", "§11#r21", "§11#r5", "§9.2#b444", "§9.4.3#b9", "§Aturan Logika Modul#r76"]
smoke: []
dependsOn:
  - "Transfer: pengajuan, Send, dan Receive"
trace:
  "§Aturan Logika Modul#r5": [61, 64, 66, 68]
  "§Aturan Logika Modul#r30": 40
  "§Aturan Logika Modul#r31": 49
  "§Aturan Logika Modul#r40": 64
  "§9.2#b128": 76
  "§9.2#b140": [64, 70]
  "§9.2#b201": 9
  "§9.2#b203": [9, 10]
  "§9.2#b205": 49
  "§9.2#b206": 49
  "§9.2#b207": [52, 56, 59]
  "§9.2#b208": 53
  "§9.2#b213": 9
  "§9.2#b215": 10
  "§9.2#b217": 11
  "§9.2#b218": [16, 27, 28]
  "§9.2#b219": [16, 28, 35]
  "§9.2#b221": [23, 24]
  "§9.2#b225": 37
  "§9.2#b275": 29
  "§9.2#b276": [23, 24]
  "§9.2#b277": [23, 24, 35]
  "§9.2#b278": [12, 30, 40]
  "§9.2#b279": 40
  "§9.2#b280": [27, 28, 35, 89, 92, 95, 96]
  "§9.2#b284": 29
  "§9.2#b290": 30
  "§9.2#b293": [23, 24, 25]
  "§9.2#b300": [84, 98, 102]
  "§9.2#b383": [61, 66, 79]
  "§9.2#b395": 20
  "§9.2#b396": [23, 24, 59]
  "§9.2#b436": [64, 70]
  "§9.2#b438": 49
  "§9.2#b418": 40
  "§9.4.2#r46": [29, 30]
  "§9.4.2#r135": 64
  "§9.4.2#r137": 49
  "§9.4.2#r147": [23, 24]
  "§9.4.2#r150": 29
  "§9.4.2#r151": [23, 24]
  "§9.4.3#b10": 64
  "§9.4.4#r37": [23, 24, 25, 26]
  "§9.6#r5": 32
  "§9.7#r2": [49, 52, 53]
  "§9.7#r11": 66
  "§9.7#r22": [23, 24, 35]
  "§9.7#r31": [25, 26]
  "§9.10.1#b8": 79
  "§11#r21": [23, 24, 29]
  "§11#r5": [23, 24, 25]
  "§9.2#b444": [23, 24, 35]
  "§9.4.3#b9": [29, 30, 40]
  "§Aturan Logika Modul#r76": 79
anchor: []
---

# Transaction timeout dan versi setting pada transaksi Transfer

## Prerequisites
- Aktor: Rina (DU-105-1), pengaju Transfer; Hendra (DU-105-2), penerima Transfer; Joko (DU-105-3), Approver; Wulan (DU-105-4), admin Transaction Settings; dan Operator platform yang mengubah plan client dan status entitas.
- Data:
  - DU-105-1: User: Name `Rina Pengaju {runId}`, Role `Aktor Transfer`, Cakupan Transfer `Group Gudang Timeout {runId}, Gudang Timur {runId}`.
  - DU-105-2: User: Name `Hendra Penerima {runId}`, Role `Aktor Transfer`, Cakupan Transfer `Group Gudang Penerima {runId}, Gudang Barat {runId}`.
  - DU-105-3: User: Name `Joko Approver {runId}`, Role Transaksi `Approver Transfer pada Group Gudang Timeout {runId}`, Status `Active`.
  - DU-105-4: User: Name `Wulan Pengelola {runId}`, Access Level `Total Control`, Cakupan `seluruh client`.
  - DU-105-5: Group: Name `Gudang Timeout {runId}`, Group induk `root client`.
  - DU-105-6: Group: Name `Gudang Penerima {runId}`, Group induk `root client`.
  - DU-105-7: Group: Name `Regional Barat {runId}`, Group induk `root client`.
  - DU-105-8: Group: Name `Gudang Barat {runId}`, Group induk `Regional Barat {runId}`.
  - DU-105-9: Group: Name `Gudang Timur {runId}`, Group induk `root client`.
  - DU-105-10: Asset: Name `Peti Kemas Timeout A {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-105-11: Asset: Name `Peti Kemas Timeout B {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval OFF`.
  - DU-105-12: Asset: Name `Peti Kemas Draft {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval OFF`.
  - DU-105-13: Asset: Name `Peti Kemas Transit {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval OFF`.
  - DU-105-14: Asset: Name `Peti Kemas Timeout E {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-105-15: Asset: Name `Peti Kemas Timeout G {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-105-16: Asset: Name `Peti Kemas Hitung Ulang {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-105-17: Asset: Name `Mesin Versi 1 {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval OFF`.
  - DU-105-18: Asset: Name `Mesin Versi 2 {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval OFF`.
  - DU-105-19: Asset: Name `Mesin Versi 3 {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-105-20: Asset: Name `Mesin Suspend {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval OFF`.
  - DU-105-21: Asset: Name `Mesin Dinamis {runId}`, Group `Gudang Timur {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval OFF`.
  - DU-105-22: Asset: Name `Peti Kemas Campur A {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval OFF`.
  - DU-105-23: Asset: Name `Peti Kemas Campur B {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-105-24: Asset: Name `Mesin Kedaluwarsa {runId}`, Group `Gudang Timeout {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`, Override aset `Require approval OFF`.
- Kondisi:
  - Spec ini memakai entitas khusus yang tidak dipakai spec lain, karena mengubah setting entitas, plan client, dan status entitas.
  - Pada awal spec nilai di All categories: Allow Transfer `Allow`, Transaction timeout `7`, In-transit overdue after `7`, Photo at start `ON`, Photo at end `ON`, dan Approval Workflow tersedia di plan client.
  - Rina, Hendra, dan Joko memiliki akun aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Transaction timeout 2 hari: baris Waiting for Approval dan Waiting for Send ditutup oleh System, Draft dan In Transit tidak
1. Wulan menyimpan Transaction timeout `2` hari di All categories
2. Rina dan Joko masing-masing mencatat jumlah entri System Log miliknya
3. Rina mengajukan Transfer aset `Peti Kemas Timeout A {runId}` ke Group `Gudang Penerima {runId}`
4. Rina mengajukan Transfer aset `Peti Kemas Timeout B {runId}` ke Group `Gudang Penerima {runId}`
5. Rina menyimpan Draft Transfer untuk aset `Peti Kemas Draft {runId}` ke Group `Gudang Penerima {runId}`
6. Rina mengajukan Transfer aset `Peti Kemas Transit {runId}` ke Group `Gudang Penerima {runId}`
7. Rina melakukan Send atas baris Transfer aset `Peti Kemas Transit {runId}` dengan scan tag dan 1 foto
8. Rina mengajukan Transfer aset `Peti Kemas Timeout E {runId}` ke Group `Gudang Penerima {runId}`
9. Verifikasi baris Transfer aset `Peti Kemas Timeout A {runId}` berstatus `Waiting for Approval`, karena nilai efektif Require approval `ON` pada aset itu
10. Verifikasi baris Transfer aset `Peti Kemas Timeout B {runId}` berstatus `Waiting for Send`, karena nilai efektif Require approval `OFF` pada aset itu
11. Verifikasi Draft Transfer untuk aset `Peti Kemas Draft {runId}` berstatus `Draft`
12. Verifikasi baris Transfer aset `Peti Kemas Transit {runId}` berstatus `In Transit`
13. Waktu berlalu sampai 25 jam sejak baris Transfer aset `Peti Kemas Timeout A {runId}` masuk `Waiting for Approval`
14. Rina mengajukan Transfer aset `Peti Kemas Timeout G {runId}` ke Group `Gudang Penerima {runId}`
15. Joko menyetujui permintaan approval atas baris Transfer aset `Peti Kemas Timeout E {runId}`
16. Verifikasi baris Transfer aset `Peti Kemas Timeout E {runId}` berstatus `Waiting for Send`, dan hitungan batasnya dimulai sejak masuk status itu
17. Wulan menyimpan In-transit overdue after `14` di All categories
18. Waktu berlalu sampai 47 jam sejak baris Transfer aset `Peti Kemas Timeout A {runId}` masuk `Waiting for Approval`
19. Job timeout berjalan
20. Verifikasi baris Transfer aset `Peti Kemas Timeout A {runId}` masih berstatus `Waiting for Approval` dan baris Transfer aset `Peti Kemas Timeout B {runId}` masih berstatus `Waiting for Send`, karena Transaction timeout `2` hari adalah 48 jam sejak masuk status itu
21. Waktu berlalu sampai 49 jam sejak baris Transfer aset `Peti Kemas Timeout A {runId}` masuk `Waiting for Approval`
22. Job timeout berjalan
23. Verifikasi baris Transfer aset `Peti Kemas Timeout A {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)`, bukan `Expired`, karena batas Transaction timeout tercapai
24. Verifikasi baris Transfer aset `Peti Kemas Timeout B {runId}` berstatus `Canceled` dengan Note `Not sent`, bukan `Expired`, karena batas pengiriman dihitung sejak baris masuk `Waiting for Send`
25. Verifikasi log transaksi baris Transfer aset `Peti Kemas Timeout A {runId}` dan baris Transfer aset `Peti Kemas Timeout B {runId}` masing-masing mencatat penutupan dengan Modified By `System`
26. Verifikasi jumlah entri System Log Rina dan Joko tidak bertambah, karena penutupan oleh sistem tidak tercatat di System Log
27. Verifikasi baris Transfer aset `Peti Kemas Timeout G {runId}` masih berstatus `Waiting for Approval`, karena timeout dihitung per baris sejak baris itu masuk status tersebut
28. Verifikasi baris Transfer aset `Peti Kemas Timeout E {runId}` masih berstatus `Waiting for Send`, karena hitungan `Waiting for Send` dimulai sejak baris masuk status itu, bukan sejak diajukan
29. Verifikasi Draft Transfer untuk aset `Peti Kemas Draft {runId}` tetap berstatus `Draft`, tidak pernah ditutup otomatis
30. Verifikasi baris Transfer aset `Peti Kemas Transit {runId}` tetap berstatus `In Transit`, tidak pernah ditutup otomatis
31. Job timeout berjalan lagi
32. Verifikasi baris Transfer aset `Peti Kemas Timeout A {runId}` tetap berstatus `Canceled` dengan tepat satu entri log penutupan, karena transaksi yang sudah ditutup tidak diproses lagi
33. Waktu berlalu sampai 74 jam sejak baris Transfer aset `Peti Kemas Timeout A {runId}` masuk `Waiting for Approval`
34. Job timeout berjalan
35. Verifikasi baris Transfer aset `Peti Kemas Timeout E {runId}` berstatus `Canceled` dengan Note `Not sent` dan baris Transfer aset `Peti Kemas Timeout G {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)`, masing-masing sesudah 48 jam sejak masuk status menunggunya
36. Rina mengajukan ulang Transfer aset `Peti Kemas Timeout A {runId}` ke Group `Gudang Penerima {runId}`
37. Verifikasi pengajuan ulang diterima dan baris Transfer baru untuk aset `Peti Kemas Timeout A {runId}` berstatus `Waiting for Approval`

### Baris In Transit tidak pernah ditutup otomatis dan hanya diberi penanda In-transit overdue menurut snapshot
38. Waktu berlalu sampai 9 hari sejak baris Transfer aset `Peti Kemas Transit {runId}` masuk `In Transit`
39. Job timeout berjalan
40. Verifikasi baris Transfer aset `Peti Kemas Transit {runId}` masih berstatus `In Transit` dan ditandai In-transit overdue menurut ambang `7` yang di-snapshot saat diajukan, bukan ambang `14` yang disimpan sesudahnya

### Perubahan Transaction timeout dihitung ulang untuk baris yang sedang menunggu
41. Wulan menyimpan Transaction timeout `3` hari di All categories
42. Rina mengajukan Transfer aset `Peti Kemas Hitung Ulang {runId}` ke Group `Gudang Penerima {runId}`
43. Rina mencatat jumlah notifikasi `*_almost_timeout` yang ia terima
44. Waktu berlalu sampai 12 jam sejak baris Transfer aset `Peti Kemas Hitung Ulang {runId}` masuk `Waiting for Approval`
45. Wulan menyimpan Transaction timeout `5` hari di All categories
46. Job penghitungan ulang batas timeout berjalan
47. Waktu berlalu sampai 84 jam sejak baris Transfer aset `Peti Kemas Hitung Ulang {runId}` masuk `Waiting for Approval`
48. Job timeout berjalan
49. Verifikasi baris Transfer aset `Peti Kemas Hitung Ulang {runId}` masih berstatus `Waiting for Approval`, karena batasnya dihitung ulang dari saat baris masuk status itu ditambah nilai baru `5` hari dan batas lama sudah terlewati
50. Wulan menyimpan Transaction timeout `1` hari di All categories
51. Job penghitungan ulang batas timeout berjalan
52. Verifikasi baris Transfer aset `Peti Kemas Hitung Ulang {runId}` tidak ditutup seketika dan batasnya disetel ke waktu Save ditambah 24 jam, karena batas hasil hitung ulang jatuh sebelum waktu Save
53. Verifikasi Rina menerima notifikasi peringatan `*_almost_timeout` baru atas baris itu, karena sisa waktu ke batas baru 24 jam atau kurang
54. Waktu berlalu sampai 107 jam sejak baris Transfer aset `Peti Kemas Hitung Ulang {runId}` masuk `Waiting for Approval`
55. Job timeout berjalan
56. Verifikasi baris Transfer aset `Peti Kemas Hitung Ulang {runId}` masih berstatus `Waiting for Approval`
57. Waktu berlalu sampai 109 jam sejak baris Transfer aset `Peti Kemas Hitung Ulang {runId}` masuk `Waiting for Approval`
58. Job timeout berjalan
59. Verifikasi baris Transfer aset `Peti Kemas Hitung Ulang {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)` sesudah batas yang disetel Save ditambah 24 jam

### Transaksi berjalan memakai versi setting saat diajukan dan transaksi baru memakai versi baru
60. Rina mengajukan Transfer aset `Mesin Versi 1 {runId}` ke Group `Gudang Penerima {runId}`
61. Verifikasi baris Transfer aset `Mesin Versi 1 {runId}` mencatat versi setting yang dipakai saat pengajuan
62. Wulan menyimpan Photo at start `OFF` di All categories
63. Rina melakukan Send atas baris Transfer aset `Mesin Versi 1 {runId}` dengan scan tag, tanpa foto
64. Verifikasi Send ditolak karena baris itu memakai versi setting saat diajukan, yaitu Photo at start `ON`, dan baris tetap berstatus `Waiting for Send`, tidak dibatalkan atau diubah aturannya
65. Rina mengajukan Transfer aset `Mesin Versi 2 {runId}` ke Group `Gudang Penerima {runId}`
66. Verifikasi baris Transfer aset `Mesin Versi 2 {runId}` mencatat versi setting yang satu lebih tinggi daripada baris `Mesin Versi 1 {runId}`, karena satu Save Changes terjadi di antara kedua pengajuan
67. Rina melakukan Send atas baris Transfer aset `Mesin Versi 2 {runId}` dengan scan tag, tanpa foto
68. Verifikasi Send diterima dan baris Transfer aset `Mesin Versi 2 {runId}` berstatus `In Transit`, karena transaksi baru memakai aturan yang berlaku saat diajukan
69. Rina melakukan Send atas baris Transfer aset `Mesin Versi 1 {runId}` dengan scan tag dan 1 foto
70. Verifikasi Send diterima dan baris Transfer aset `Mesin Versi 1 {runId}` berstatus `In Transit`, sehingga transaksi berjalan selesai dengan aturan lama

### Cakupan override Group dievaluasi dinamis terhadap data saat ini
71. Wulan menambah override Group untuk Group `Regional Barat {runId}` di All categories dengan Allow Transfer `Deny`
72. Rina mengajukan Transfer aset `Mesin Dinamis {runId}` dari Group `Gudang Timur {runId}` ke Group `Gudang Barat {runId}`
73. Rina melakukan Send atas baris Transfer aset `Mesin Dinamis {runId}` dengan scan tag, tanpa foto
74. Hendra melakukan Receive atas baris Transfer aset `Mesin Dinamis {runId}` dengan scan tag dan 1 foto
75. Hendra mengajukan Transfer aset `Mesin Dinamis {runId}` dari Group `Gudang Barat {runId}` ke Group `Gudang Timur {runId}`
76. Verifikasi pengajuan ditolak dan tidak ada baris Transfer baru untuk aset `Mesin Dinamis {runId}`, karena aset itu kini berada di Group dalam cakupan override Deny, dan cakupan dievaluasi terhadap data saat ini, bukan saat override dibuat

### Transaksi yang diajukan saat Approval Workflow tidak tersedia tercatat tanpa langkah approval
77. Operator platform menonaktifkan Approval Workflow pada plan client
78. Rina mengajukan Transfer aset `Mesin Versi 3 {runId}` ke Group `Gudang Penerima {runId}`
79. Verifikasi baris Transfer aset `Mesin Versi 3 {runId}` berstatus `Waiting for Send` tanpa langkah approval, dan mencatat versi setting yang dipakai saat pengajuan

### Entitas Suspended: job timeout tanpa aktor tetap berjalan
80. Rina mengajukan Transfer aset `Mesin Suspend {runId}` ke Group `Gudang Penerima {runId}`
81. Operator platform mengubah status entitas menjadi `Suspended`
82. Waktu berlalu sampai 25 jam sejak baris Transfer aset `Mesin Suspend {runId}` masuk `Waiting for Send`
83. Job timeout berjalan
84. Verifikasi baris Transfer aset `Mesin Suspend {runId}` berstatus `Canceled` dengan Note `Not sent` dan Modified By `System`, walau entitas berstatus `Suspended`

### Timeout dihitung per baris pada satu Transfer yang barisnya masuk status menunggu pada waktu berbeda
85. Operator platform mengubah status entitas menjadi `Active`
86. Operator platform mengaktifkan Approval Workflow pada plan client
87. Wulan menyimpan Transaction timeout `2` hari di All categories
88. Rina mengajukan satu Transfer berisi aset `Peti Kemas Campur A {runId}` dan `Peti Kemas Campur B {runId}` ke Group `Gudang Penerima {runId}`
89. Verifikasi baris Transfer aset `Peti Kemas Campur A {runId}` berstatus `Waiting for Send` dan baris Transfer aset `Peti Kemas Campur B {runId}` berstatus `Waiting for Approval`, karena nilai efektif Require approval aset A `OFF` dan aset B `ON`
90. Waktu berlalu sampai 30 jam sejak baris Transfer aset `Peti Kemas Campur B {runId}` masuk `Waiting for Approval`
91. Joko menyetujui permintaan approval atas baris Transfer aset `Peti Kemas Campur B {runId}`
92. Verifikasi baris Transfer aset `Peti Kemas Campur B {runId}` berstatus `Waiting for Send`
93. Waktu berlalu sampai 49 jam sejak baris Transfer aset `Peti Kemas Campur A {runId}` masuk `Waiting for Send`
94. Job timeout berjalan
95. Verifikasi baris Transfer aset `Peti Kemas Campur A {runId}` berstatus `Canceled` dengan Note `Not sent`
96. Verifikasi baris Transfer aset `Peti Kemas Campur B {runId}`, pada Transfer yang sama, masih berstatus `Waiting for Send`, karena timeout dihitung per baris sejak baris itu masuk status tersebut

### Entitas Expired: job timeout tanpa aktor tetap berjalan
97. Rina mengajukan Transfer aset `Mesin Kedaluwarsa {runId}` ke Group `Gudang Penerima {runId}`
98. Verifikasi baris Transfer aset `Mesin Kedaluwarsa {runId}` berstatus `Waiting for Send`
99. Operator platform mengubah status entitas menjadi `Expired`
100. Waktu berlalu sampai 49 jam sejak baris Transfer aset `Mesin Kedaluwarsa {runId}` masuk `Waiting for Send`
101. Job timeout berjalan
102. Verifikasi baris Transfer aset `Mesin Kedaluwarsa {runId}` berstatus `Canceled` dengan Note `Not sent` dan Modified By `System`, walau entitas berstatus `Expired`
