---
id: TC-FA-FATR-BE-102-timeout-assign-dep-assign
title: "Transaction timeout dan versi setting pada transaksi Assign"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r5", "§Aturan Logika Modul#r31", "§Aturan Logika Modul#r40", "§9.2#b128", "§9.2#b140", "§9.2#b201", "§9.2#b203", "§9.2#b205", "§9.2#b206", "§9.2#b207", "§9.2#b208", "§9.2#b213", "§9.2#b214", "§9.2#b217", "§9.2#b218", "§9.2#b219", "§9.2#b221", "§9.2#b225", "§9.2#b259", "§9.2#b260", "§9.2#b261", "§9.2#b262", "§9.2#b263", "§9.2#b264", "§9.2#b265", "§9.2#b283", "§9.2#b289", "§9.2#b293", "§9.2#b300", "§9.2#b383", "§9.2#b395", "§9.2#b396", "§9.2#b436", "§9.2#b438", "§9.4.1#r11", "§9.4.2#r46", "§9.4.2#r135", "§9.4.2#r137", "§9.4.2#r147", "§9.4.2#r150", "§9.4.2#r151", "§9.4.3#b10", "§9.4.4#r37", "§9.6#r5", "§9.7#r2", "§9.7#r11", "§9.7#r22", "§9.7#r31", "§9.10.1#b8", "§11#r23", "§9.2#b444", "§Aturan Logika Modul#r76"]
smoke: []
dependsOn:
  - "Assign: pengajuan, handover, Reassign, dan Unassign"
owner: BE
trace:
  "§Aturan Logika Modul#r5": [9, 11, 13]
  "§Aturan Logika Modul#r31": 61
  "§Aturan Logika Modul#r40": 14
  "§9.2#b128": 19
  "§9.2#b140": 11
  "§9.2#b201": 90
  "§9.2#b203": 48
  "§9.2#b205": 61
  "§9.2#b206": 61
  "§9.2#b207": [68, 72, 75]
  "§9.2#b208": 69
  "§9.2#b213": 35
  "§9.2#b214": [44, 45]
  "§9.2#b217": 89
  "§9.2#b218": [35, 44]
  "§9.2#b219": 44
  "§9.2#b221": [38, 48]
  "§9.2#b225": 55
  "§9.2#b259": 89
  "§9.2#b260": [38, 48]
  "§9.2#b261": 40
  "§9.2#b262": 48
  "§9.2#b263": [51, 97, 98]
  "§9.2#b264": [5, 32]
  "§9.2#b265": 4
  "§9.2#b283": 89
  "§9.2#b289": 90
  "§9.2#b293": 39
  "§9.2#b300": [84, 88]
  "§9.2#b383": 9
  "§9.2#b395": 35
  "§9.2#b396": 38
  "§9.2#b436": 11
  "§9.2#b438": 61
  "§9.4.1#r11": 16
  "§9.4.2#r46": [89, 90]
  "§9.4.2#r135": 11
  "§9.4.2#r137": 61
  "§9.4.2#r147": 38
  "§9.4.2#r150": 89
  "§9.4.2#r151": [41, 49]
  "§9.4.3#b10": 14
  "§9.4.4#r37": [42, 43]
  "§9.6#r5": 53
  "§9.7#r2": [61, 69]
  "§9.7#r11": 9
  "§9.7#r22": 38
  "§9.7#r31": [42, 50]
  "§9.10.1#b8": 23
  "§11#r23": [5, 32, 40, 89]
  "§9.2#b444": [38, 48]
  "§Aturan Logika Modul#r76": 23
---

# Transaction timeout dan versi setting pada transaksi Assign

## Prerequisites
- Aktor: Admin `Budi Santoso {runId}` (Total Control entitas khusus; mengubah setting dan menjalankan Handover dan Unassign); `Tia Anggraini {runId}` (pengaju Assign, bukan Group Manager dan bukan Total Control); `Wawan Hidayat {runId}` (Approver Level 1 untuk Group `Gudang Utama {runId}`); Operator platform (hanya mengubah Approval Workflow pada plan entitas dan status entitas).
- Data:
  - DU-102-1: Entitas: Name `Entitas Timeout Assign {runId}`; entitas khusus spec ini, tidak dipakai spec lain.
  - DU-102-2: Group: Name `Gudang Utama {runId}`; Group untuk pengujian timeout, Require approval ON dari Company default.
  - DU-102-3: Group: Name `Gudang Surabaya {runId}`; Group untuk pengujian versi setting dan kuota.
  - DU-102-4: User: Name `Budi Santoso {runId}`, Role `Total Control entitas`; Admin pengubah setting dan pelaksana Handover dan Unassign.
  - DU-102-5: User: Name `Tia Anggraini {runId}`, Role `Pengaju Assign`; Pengaju Assign yang bukan Group Manager dan bukan Total Control.
  - DU-102-6: User: Name `Wawan Hidayat {runId}`, Role Transaksi `Approver`, Group `Gudang Utama {runId}`; Approver untuk Group di atas.
  - DU-102-7: Employee: Name `Bayu Saputra {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee yang aktif dan punya akun login.
  - DU-102-8: Employee: Name `Putri Handayani {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee yang aktif dan punya akun login.
  - DU-102-10: Employee: Name `Rina Kusuma {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee yang aktif dan punya akun login.
  - DU-102-11: Employee: Name `Maya Puspita {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee yang aktif dan punya akun login.
  - DU-102-12: Setting Assign Entitas Timeout: Require approval `ON`, Approval type `Any one approver`, Transaction timeout `7`, Need recipient confirmation `Yes`, Photo at start `ON`, Photo at end `ON`, Allowed assignee: Employee `ON`; keadaan awal Company default tab Assign.
  - DU-102-13: Asset: Name `Laptop Lenovo IdeaPad 5 {runId}`, Group `Gudang Surabaya {runId}`; aset milik spec ini.
  - DU-102-14: Asset: Name `Laptop HP Pavilion 14 {runId}`, Group `Gudang Surabaya {runId}`; aset milik spec ini.
  - DU-102-15: Asset: Name `Laptop Acer Aspire Lite {runId}`, Group `Gudang Utama {runId}`; aset milik spec ini.
  - DU-102-16: Asset: Name `Monitor Dell P2723QE {runId}`, Group `Gudang Utama {runId}`; aset milik spec ini.
  - DU-102-17: Asset: Name `Monitor LG 27UP550 {runId}`, Group `Gudang Utama {runId}`; aset milik spec ini.
  - DU-102-18: Asset: Name `Monitor Samsung S27 {runId}`, Group `Gudang Utama {runId}`; aset milik spec ini.
  - DU-102-19: Asset: Name `Tablet Lenovo Tab M10 {runId}`, Group `Gudang Utama {runId}`; aset milik spec ini.
  - DU-102-20: Asset: Name `Tablet Samsung Galaxy Tab A8 {runId}`, Group `Gudang Utama {runId}`; aset milik spec ini.
  - DU-102-21: Asset: Name `Proyektor Epson EB-E01 {runId}`, Group `Gudang Utama {runId}`; aset milik spec ini.
  - DU-102-22: Asset: Name `Proyektor BenQ MS560 {runId}`, Group `Gudang Utama {runId}`; aset milik spec ini.
  - DU-102-23: Asset: Name `Kamera Canon EOS 200D {runId}`, Group `Gudang Utama {runId}`; aset milik spec ini.
  - DU-102-24: Asset: Name `Handphone Samsung Galaxy S23 {runId}`, Group `Gudang Surabaya {runId}`, Status `Assigned`, Pemegang `Rina Kusuma {runId}`; aset milik spec ini.
  - DU-102-25: Asset: Name `Handphone Xiaomi 13T {runId}`, Group `Gudang Surabaya {runId}`; aset milik spec ini.
  - DU-102-33: Plan entitas: Approval Workflow `Tersedia`; keadaan plan entitas.
  - DU-102-36: Group: Name `Gudang Malang {runId}`; Group untuk pengujian batas serah terima per baris.
  - DU-102-37: Asset: Name `Printer Epson L121 {runId}`, Group `Gudang Malang {runId}`; aset milik spec ini.
  - DU-102-38: Asset: Name `Printer Canon E470 {runId}`, Group `Gudang Malang {runId}`; aset milik spec ini.
  - DU-102-31: Asset: Name `Laptop Asus Vivobook Go {runId}`, Group `Gudang Surabaya {runId}`; aset milik spec ini, didaftarkan ke Group sesudah override Group untuk Group itu dibuat.
  - Spec ini memakai entitas khusus (DU-102-1) yang tidak dipakai spec lain; semua data di atas berada di entitas itu.
- Kondisi:
  - Company default tab Assign pada keadaan awal sesuai data di atas: Require approval bernilai `ON`, Approval type bernilai `Any one approver`, Transaction timeout bernilai `7` hari, Need recipient confirmation bernilai `Yes`, Photo at start bernilai `ON`, Photo at end bernilai `ON`, Allowed assignee: Employee bernilai `ON`
  - Approval Workflow tersedia pada plan entitas, Level Feature Suite Assignment bernilai `Full`, dan status entitas aktif
  - Employee assignee `Rina Kusuma {runId}` memegang aset `Handphone Samsung Galaxy S23 {runId}` berstatus Assigned di Group `Gudang Surabaya {runId}`
  - Aset `Laptop Lenovo IdeaPad 5 {runId}` dan `Laptop HP Pavilion 14 {runId}` sudah ada di Group `Gudang Surabaya {runId}` sebelum override Group untuk Group itu dibuat

## Test Steps
### Transaksi memakai versi setting saat diajukan dan mencatat versinya
1. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Surabaya {runId}` untuk transaksi Assign dengan Require approval `OFF` dan Max assets per assignee (concurrent) `1`
2. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop Lenovo IdeaPad 5 {runId}` kepada `Bayu Saputra {runId}`
3. Admin `Budi Santoso {runId}` menyelesaikan Handover aset `Laptop Lenovo IdeaPad 5 {runId}` dengan satu foto dan akseptasi Assignee pada saat handover
4. Verifikasi akseptasi Assignee terjadi saat Handover: baris Assign aset `Laptop Lenovo IdeaPad 5 {runId}` langsung berstatus `Assigned` tanpa langkah akseptasi terpisah sesudahnya
5. Verifikasi baris Assign tidak pernah berstatus `Waiting acceptance`, karena Assign tidak memiliki status itu
6. Admin `Budi Santoso {runId}` menyimpan Company default Assign dengan Photo at end `OFF`
7. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop HP Pavilion 14 {runId}` kepada `Putri Handayani {runId}`
8. Admin `Budi Santoso {runId}` menyelesaikan Handover aset `Laptop HP Pavilion 14 {runId}` dengan satu foto dan akseptasi Assignee pada saat handover
9. Verifikasi versi setting yang tercatat pada transaksi aset `Laptop HP Pavilion 14 {runId}` satu lebih besar daripada versi pada transaksi aset `Laptop Lenovo IdeaPad 5 {runId}`, karena hasil evaluasi menyimpan versi yang berlaku saat diajukan
10. Admin `Budi Santoso {runId}` menyelesaikan Unassign aset `Laptop Lenovo IdeaPad 5 {runId}` dari `Bayu Saputra {runId}` tanpa foto
11. Verifikasi Unassign ditolak karena transaksi aset `Laptop Lenovo IdeaPad 5 {runId}` berjalan memakai versi setting saat diajukan, yaitu Photo at end `ON`
12. Admin `Budi Santoso {runId}` menyelesaikan Unassign aset `Laptop HP Pavilion 14 {runId}` dari `Putri Handayani {runId}` tanpa foto
13. Verifikasi Unassign diterima karena transaksi yang diajukan sesudah Save memakai aturan yang berlaku saat itu, yaitu Photo at end `OFF`
14. Verifikasi transaksi aset `Laptop Lenovo IdeaPad 5 {runId}` tidak dibatalkan otomatis dan tetap berstatus `Assigned`, dengan aturannya tidak diubah karena Settings berubah

### Kuota Max assets per assignee ditegakkan saat evaluasi
15. `Tia Anggraini {runId}` mengajukan Assign aset `Handphone Xiaomi 13T {runId}` kepada `Rina Kusuma {runId}`
16. Verifikasi pengajuan aset `Handphone Xiaomi 13T {runId}` ditolak karena `Rina Kusuma {runId}` sudah memegang aset `Handphone Samsung Galaxy S23 {runId}` dan batas Max assets per assignee (concurrent) `1` ditegakkan saat evaluasi pengajuan

### Cakupan override dievaluasi dinamis
17. Admin `Budi Santoso {runId}` mendaftarkan aset `Laptop Asus Vivobook Go {runId}` ke Group `Gudang Surabaya {runId}` sesudah override Group untuk Group itu dibuat
18. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop Asus Vivobook Go {runId}` kepada `Maya Puspita {runId}`
19. Verifikasi pengajuan aset `Laptop Asus Vivobook Go {runId}` langsung berstatus `Waiting for Handover`, karena cakupan override Group dievaluasi terhadap data saat ini pada evaluasi transaksi baru dan bukan snapshot saat override dibuat

### Transaksi yang diajukan saat Approval Workflow tidak tersedia tercatat tanpa langkah approval
20. Operator platform mengubah Approval Workflow pada plan entitas menjadi tidak tersedia
21. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop Acer Aspire Lite {runId}` kepada `Bayu Saputra {runId}`
22. Operator platform mengubah Approval Workflow pada plan entitas menjadi tersedia
23. Verifikasi transaksi aset `Laptop Acer Aspire Lite {runId}` yang diajukan saat Approval Workflow tidak tersedia tercatat tanpa langkah approval, yaitu `Waiting for Handover`, dan tetap demikian sesudah Approval Workflow tersedia

### Batas Transaction timeout, status yang berlaku, dan hasil Canceled oleh System
24. `Tia Anggraini {runId}` mengajukan Assign aset `Monitor Dell P2723QE {runId}` kepada `Bayu Saputra {runId}`
25. `Tia Anggraini {runId}` mengajukan Assign aset `Monitor LG 27UP550 {runId}` kepada `Bayu Saputra {runId}`
26. `Tia Anggraini {runId}` mengajukan Assign aset `Monitor Samsung S27 {runId}` kepada `Bayu Saputra {runId}`
27. Admin `Budi Santoso {runId}` menyimpan Draft Assign aset `Kamera Canon EOS 200D {runId}` untuk `Bayu Saputra {runId}`
28. Waktu berlalu 3 hari sejak ketiga transaksi diajukan
29. `Wawan Hidayat {runId}` menyetujui pengajuan Assign aset `Monitor LG 27UP550 {runId}`
30. Waktu berlalu sampai 6 hari sejak ketiga transaksi diajukan
31. `Wawan Hidayat {runId}` menyetujui pengajuan Assign aset `Monitor Samsung S27 {runId}`
32. Verifikasi setelah persetujuan, aset `Monitor Samsung S27 {runId}` langsung berstatus `Waiting for Handover` dan bukan `Waiting acceptance`
33. Waktu berlalu sampai 6 hari 23 jam sejak ketiga transaksi diajukan
34. Background job pengecekan Transaction timeout berjalan
35. Verifikasi transaksi aset `Monitor Dell P2723QE {runId}` masih `Waiting for Approval`, karena Transaction timeout `7` hari berarti 7 × 24 jam sejak transaksi masuk status itu dan batasnya belum tercapai
36. Waktu berlalu sampai 7 hari 1 jam sejak ketiga transaksi diajukan
37. Background job pengecekan Transaction timeout berjalan
38. Verifikasi transaksi aset `Monitor Dell P2723QE {runId}` ditutup saat batas Transaction timeout tercapai, dan berstatus `Canceled`
39. Verifikasi transaksi aset `Monitor Dell P2723QE {runId}` ditutup oleh `System` karena melewati batas di status yang berlaku
40. Verifikasi transaksi aset `Monitor Dell P2723QE {runId}` berstatus `Canceled` dan bukan `Expired`
41. Verifikasi Note penutupan transaksi aset `Monitor Dell P2723QE {runId}` adalah `Timed out (Waiting for Approval)`
42. Verifikasi log transaksi aset `Monitor Dell P2723QE {runId}` tercatat dengan Modified By `System`
43. Verifikasi penutupan itu tidak menambah entri System Log atas nama aktor, karena aksi sistem tanpa user aktor hanya tercatat di log transaksi
44. Verifikasi transaksi aset `Monitor LG 27UP550 {runId}` masih `Waiting for Handover`, karena hitungan batas serah terima dimulai lagi sejak transaksi masuk status itu dan bukan sejak diajukan
45. Verifikasi transaksi aset `Monitor Samsung S27 {runId}` masih `Waiting for Handover`
46. Waktu berlalu sampai 10 hari 1 jam sejak ketiga transaksi diajukan
47. Background job pengecekan Transaction timeout berjalan
48. Verifikasi transaksi aset `Monitor LG 27UP550 {runId}` berstatus `Canceled` karena batas serah terima dari status `Waiting for Handover` terlewati
49. Verifikasi Note penutupan transaksi aset `Monitor LG 27UP550 {runId}` adalah `Not handed over`
50. Verifikasi log transaksi aset `Monitor LG 27UP550 {runId}` tercatat dengan Modified By `System`
51. Verifikasi transaksi aset `Monitor Samsung S27 {runId}` masih `Waiting for Handover`, karena batas serah terima dihitung per baris sejak baris itu masuk status
52. Background job pengecekan Transaction timeout berjalan
53. Verifikasi transaksi aset `Monitor Dell P2723QE {runId}` yang sudah ditutup tidak diproses lagi: statusnya tetap `Canceled` dan tidak ada entri log transaksi baru
54. `Tia Anggraini {runId}` mengajukan Assign aset `Monitor Dell P2723QE {runId}` kepada `Bayu Saputra {runId}`
55. Verifikasi transaksi aset `Monitor Dell P2723QE {runId}` yang sebelumnya ditutup timeout dapat diajukan ulang dan berstatus `Waiting for Approval`

### Nilai Transaction timeout dihitung ulang dari saat transaksi masuk status
56. `Tia Anggraini {runId}` mengajukan Assign aset `Proyektor Epson EB-E01 {runId}` kepada `Bayu Saputra {runId}`
57. Admin `Budi Santoso {runId}` menyimpan Company default Assign dengan Transaction timeout `3`
58. Job batch penghitungan ulang batas Transaction timeout berjalan
59. Waktu berlalu sampai 3 hari 1 jam sejak transaksi aset `Proyektor Epson EB-E01 {runId}` diajukan
60. Background job pengecekan Transaction timeout berjalan
61. Verifikasi transaksi aset `Proyektor Epson EB-E01 {runId}` berstatus `Canceled` karena batas dihitung ulang dari saat transaksi masuk status itu ditambah nilai baru `3` hari, bukan nilai lama `7` hari

### Batas yang jatuh sebelum waktu Save disetel ke waktu Save ditambah 24 jam
62. Admin `Budi Santoso {runId}` menyimpan Company default Assign dengan Transaction timeout `7`
63. `Tia Anggraini {runId}` mengajukan Assign aset `Proyektor BenQ MS560 {runId}` kepada `Bayu Saputra {runId}`
64. Waktu berlalu 5 hari sejak transaksi aset `Proyektor BenQ MS560 {runId}` diajukan
65. Admin `Budi Santoso {runId}` menyimpan Company default Assign dengan Transaction timeout `2`
66. Job batch penghitungan ulang batas Transaction timeout berjalan
67. Background job pengecekan Transaction timeout berjalan
68. Verifikasi transaksi aset `Proyektor BenQ MS560 {runId}` tidak langsung ditutup walau batas baru jatuh sebelum waktu Save, karena batas disetel ke waktu Save ditambah 24 jam
69. Verifikasi peringatan 1 hari sebelum batas (event `*_almost_timeout`) dikirim ulang untuk transaksi aset `Proyektor BenQ MS560 {runId}` karena sisa waktu ke batas baru 24 jam atau kurang
70. Waktu berlalu 23 jam sejak Save
71. Background job pengecekan Transaction timeout berjalan
72. Verifikasi transaksi aset `Proyektor BenQ MS560 {runId}` masih `Waiting for Approval` sampai batas Save ditambah 24 jam
73. Waktu berlalu sampai 1 hari 1 jam sejak Save
74. Background job pengecekan Transaction timeout berjalan
75. Verifikasi transaksi aset `Proyektor BenQ MS560 {runId}` berstatus `Canceled` setelah batas Save ditambah 24 jam terlewati

### Timeout tetap berjalan saat entitas Suspended atau Expired
76. Admin `Budi Santoso {runId}` menyimpan Company default Assign dengan Transaction timeout `7`
77. `Tia Anggraini {runId}` mengajukan Assign aset `Tablet Lenovo Tab M10 {runId}` kepada `Putri Handayani {runId}`
78. Waktu berlalu 5 hari sejak transaksi aset `Tablet Lenovo Tab M10 {runId}` diajukan
79. `Tia Anggraini {runId}` mengajukan Assign aset `Tablet Samsung Galaxy Tab A8 {runId}` kepada `Putri Handayani {runId}`
80. Waktu berlalu 1 hari sejak transaksi aset `Tablet Samsung Galaxy Tab A8 {runId}` diajukan
81. Operator platform mengubah status entitas menjadi `Suspended`
82. Waktu berlalu sampai 7 hari 1 jam sejak transaksi aset `Tablet Lenovo Tab M10 {runId}` diajukan
83. Background job pengecekan Transaction timeout berjalan
84. Verifikasi transaksi aset `Tablet Lenovo Tab M10 {runId}` tetap ditutup oleh `System` dan berstatus `Canceled` saat entitas `Suspended`, karena job timeout tanpa aktor tetap berjalan
85. Operator platform mengubah status entitas menjadi `Expired`
86. Waktu berlalu sampai 7 hari 1 jam sejak transaksi aset `Tablet Samsung Galaxy Tab A8 {runId}` diajukan
87. Background job pengecekan Transaction timeout berjalan
88. Verifikasi transaksi aset `Tablet Samsung Galaxy Tab A8 {runId}` tetap ditutup oleh `System` dan berstatus `Canceled` saat entitas `Expired`, karena job timeout tanpa aktor tetap berjalan

### Draft dan status Assigned tidak pernah ditutup otomatis
89. Verifikasi Draft Assign aset `Kamera Canon EOS 200D {runId}` tetap Draft sesudah seluruh waktu berlalu, karena Draft tidak memiliki timeout
90. Verifikasi transaksi aset `Handphone Samsung Galaxy S23 {runId}` tetap berstatus `Assigned` dan tidak pernah ditutup otomatis oleh timeout

### Batas serah terima dihitung per baris pada satu pengajuan berisi dua baris
91. Operator platform mengembalikan status entitas menjadi `Aktif`
92. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Malang {runId}` untuk transaksi Assign dengan Require approval `OFF`
93. `Tia Anggraini {runId}` mengajukan satu pengajuan Assign berisi dua baris, aset `Printer Epson L121 {runId}` dan aset `Printer Canon E470 {runId}`, kepada `Bayu Saputra {runId}`
94. Admin `Budi Santoso {runId}` menyelesaikan Handover baris aset `Printer Epson L121 {runId}` dengan satu foto dan akseptasi Assignee pada saat handover
95. Waktu berlalu sampai 7 hari 1 jam sejak pengajuan itu diajukan
96. Background job pengecekan Transaction timeout berjalan
97. Verifikasi baris aset `Printer Canon E470 {runId}` berstatus `Canceled` dengan Note `Not handed over`, karena batas serah terima dihitung per baris dan baris itu belum diserahterimakan
98. Verifikasi baris aset `Printer Epson L121 {runId}` tetap berstatus `Assigned` dan tidak ditutup oleh timeout, walau berasal dari pengajuan yang sama

