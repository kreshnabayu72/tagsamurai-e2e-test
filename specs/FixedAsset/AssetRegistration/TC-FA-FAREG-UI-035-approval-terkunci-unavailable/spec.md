---
id: TC-FA-FAREG-UI-035-approval-terkunci-unavailable
title: "Halaman Approval: pengajuan sendiri terkunci dan aset Unavailable"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [S-REG-13, S-REG-17, S-REG-24, S-REG-29, §4.1#r8, §4.1#r9, §4.2.4#b6, §4.2.4#b7, §4.2.4#b9, §4.8#r22, §4.8#r27, EB-TBL-5@halaman-approval, FAREG-LOGIC-20m]
smoke: []
dependsOn: []
trace:
  S-REG-13: [2, 3, 9, 23, 84]
  S-REG-17: [13, 15, 18]
  S-REG-24: [31, 32, 45, 52, 53, 60]
  S-REG-29: [27, 34, 36, 40, 49, 55, 58, 62, 63, 65, 73, 76]
  §4.1#r8: [2, 25]
  §4.1#r9: [32, 45, 53, 60, 68, 69, 33, 46, 54, 61, 79, 80]
  §4.2.4#b6: [2, 3, 6]
  §4.2.4#b7: [13, 18, 19, 20, 21]
  §4.2.4#b9: [30, 31, 34, 37, 38, 43, 44, 47, 52, 55, 56, 73, 74]
  §4.8#r22: [3, 5, 23, 84]
  §4.8#r27: [6, 11, 13, 18, 24]
  EB-TBL-5@halaman-approval: [9, 11, 15, 36, 84]
  FAREG-LOGIC-20m: [2, 13, 23, 24, 25]
anchor: [71]
coverage:
  web: automated
---
# Halaman Approval: pengajuan sendiri terkunci dan aset Unavailable

## Prerequisites
- Aktor: Hadi K (role Manage asset & TAG dengan capability Update pada Group `Gudang 1`) pada K1, yang juga pengaju pengajuan DU-035-1; Dewi A (approver, role Group Manager, cakupan Group binaan + sub-group termasuk Gudang 1, Gudang 3, dan Gudang 4), bukan pengaju pengajuan, pada K2 sampai K10.
- Layar awal: Halaman Approval pengajuan. Pengajuan sendiri (K1) tidak masuk antrean Active sehingga halamannya dibuka lewat alamat langsung; pengajuan lain (K2 sampai K10) dibuka dari antrean Approvals tab Active.
- Komponen: Halaman Approval
- Data:
  - DU-035-1: pengajuan Registration ID `REG-20261111-00014`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Hadi K`, Total Asset `3`.
  - DU-035-2: aset Name `Laptop - 128`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason; di panel koreksi: Custom field `Serial Number` bernilai `SN-128-0001`.
  - DU-035-3: aset Name `Laptop - 129`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Skipped`, Condition `Damaged`, Corrections `1`, Decision `Approve`, tanpa Reason.
  - DU-035-4: aset Name `Office Desk - 12`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 1`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-5: pengajuan Registration ID `REG-20261109-00003`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `5`.
  - DU-035-6: aset Name `Laptop - 129`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Skipped`, Condition `Damaged`, Corrections `1`, Decision awal `Approve`, tanpa Reason.
  - DU-035-7: aset Name `Laptop - 130`, Category `Computers`, Brand `Dell`, Model `Latitude 5450`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-8: aset Name `Laptop - 131`, Category `Computers`, Brand `Dell`, Model `Latitude 5450`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-9: aset Name `Office Desk - 12`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 1`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision awal `Approve`, tanpa Reason.
  - DU-035-10: pengajuan Registration ID `REG-20261110-00012`, Status `Waiting for Approval`, Group `Gudang 3`, Requested By `Siti N`, Total Asset `2`.
  - DU-035-11: aset Name `Monitor - 21`, Category `Computers`, Brand `Samsung`, Model `U28`, Group `Gudang 3`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-12: aset Name `Monitor - 22`, Category `Computers`, Brand `Samsung`, Model `U28`, Group `Gudang 4`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-13: aset Name `Monitor - 23`, Category `Computers`, Brand `Samsung`, Model `U28`, Group `Gudang 4`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-14: aset Name `Monitor - 24`, Category `Computers`, Brand `Samsung`, Model `U28`, Group `Gudang 3`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision awal `Approve`, tanpa Reason.
  - DU-035-15: pengajuan Registration ID `REG-20261112-00015`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `3`.
  - DU-035-16: aset Name `Monitor - 25`, Category `Computers`, Brand `Samsung`, Model `S24`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-17: pengajuan Registration ID `REG-20261113-00016`, Status `Waiting for Approval`, Group `Gudang 4`, Requested By `Siti N`, Total Asset `2`.
  - DU-035-18: aset Name `Monitor - 26`, Category `Computers`, Brand `Samsung`, Model `S24`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-19: pengajuan Registration ID `REG-20261114-00017`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `4`.
  - DU-035-20: aset Name `Monitor - 30`, Category `Computers`, Brand `Dell`, Model `P2422H`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - Teks Alert yang diharapkan: `1 asset uses master data that is no longer available. Correct it, return it to Draft, or reject it before deciding.` (satu aset Brand atau Model tidak tersedia), `2 assets use master data that is no longer available. Correct them, return them to Draft, or reject them before deciding.` (dua aset), `1 asset uses master data that is no longer available. Return it to Draft or reject it before deciding.` (satu aset Asset Name atau Group tidak tersedia), dan `2 assets use master data that is no longer available. Return them to Draft or reject them before deciding.` (dua aset), dari template `[N] assets use master data that is no longer available.` dengan N sesuai jumlah aset. Pada K11, baris Alert pertama menghitung DU-035-2 dan DU-035-20 (Brand tidak tersedia), dan baris Alert kedua menghitung DU-035-16, DU-035-18, dan DU-035-20 (Asset Name tidak tersedia, termasuk DU-035-20 yang Brand-nya juga tidak tersedia).
- Kondisi:
  - K1: pengajuan DU-035-1 milik Hadi K berisi aset DU-035-2 dan DU-035-3 dalam grup Accordion `Laptop` dan DU-035-4 dalam grup Accordion `Office Desk`, dengan Decision awal `Approve`.
  - K2: pengajuan DU-035-5 milik Rina W berisi aset DU-035-2, DU-035-6, DU-035-7, dan DU-035-8 dalam grup Accordion `Laptop` dan DU-035-9 dalam grup Accordion `Office Desk`, dan approver berhak memutuskan.
  - K3: pengajuan DU-035-10 milik Siti N berisi aset DU-035-11 dan DU-035-14 dalam grup Accordion `Monitor`, dan approver berhak memutuskan.
  - K4: pengajuan DU-035-15 milik Rina W berisi aset DU-035-2 dalam grup Accordion `Laptop` serta DU-035-16 dan DU-035-18 dalam grup Accordion `Monitor`, dan approver berhak memutuskan.
  - K5: seperti K2, dan sesudah halaman Approval terbuka, respons master menyatakan Model `Latitude 5440` tidak lagi tersedia.
  - K6: seperti K2, dan sesudah halaman Approval terbuka, respons master menyatakan Model `Latitude 5450` tidak lagi tersedia.
  - K7: seperti K3, dan sesudah halaman Approval terbuka, respons master menyatakan Group `Gudang 3` tidak lagi tersedia.
  - K8: pengajuan DU-035-17 milik Siti N berisi aset DU-035-12 dan DU-035-13 dalam grup Accordion `Monitor`, approver berhak memutuskan, dan sesudah halaman Approval terbuka, respons master menyatakan Group `Gudang 4` tidak lagi tersedia.
  - K9: seperti K4, dan sesudah halaman Approval terbuka, respons master menyatakan Model `Latitude 5440` dan Asset Name `Monitor` tidak lagi tersedia.
  - K10: seperti K2, dan sesudah halaman Approval terbuka, respons master menyatakan Brand `Dell` tidak lagi tersedia.
  - K11: pengajuan DU-035-19 milik Rina W berisi aset DU-035-2 dalam grup Accordion `Laptop` serta DU-035-16, DU-035-18, dan DU-035-20 dalam grup Accordion `Monitor`, approver berhak memutuskan, dan sesudah halaman Approval terbuka, respons master menyatakan Brand `Dell` dan Asset Name `Monitor` tidak lagi tersedia.

## Test Steps

### Pengajuan sendiri: notice dan kontrol keputusan disabled
1. Tampilkan Halaman Approval dengan kondisi K1
2. Verifikasi notice `You cannot decide a registration you submitted.` tampil di atas tabel aset
3. Verifikasi Decision pada setiap baris aset disabled
4. Centang baris `Laptop - 128` pada grup `Laptop`
5. Verifikasi Bulk Action pada grup `Laptop` disabled
6. Verifikasi `[Submit]` disabled

### Alasan disabled tampil saat hover
7. Tampilkan Halaman Approval dengan kondisi K1
8. Arahkan kursor ke Decision pada baris `Laptop - 128`
9. Verifikasi tooltip `You cannot decide a registration you submitted.` tampil
10. Arahkan kursor ke `[Submit]`
11. Verifikasi tooltip alasan tampil pada `[Submit]` yang disabled
12. Klik row option (titik tiga) pada baris `Laptop - 128`
13. Verifikasi pilihan `Edit` disabled
14. Arahkan kursor ke pilihan `Edit`
15. Verifikasi tooltip `You cannot decide a registration you submitted.` tampil

### Link Name tetap aktif dan membuka panel view-only
16. Tampilkan Halaman Approval dengan kondisi K1
17. Klik nama `Laptop - 128`
18. Verifikasi panel koreksi terbuka
19. Verifikasi field `Brand`, `Model`, `Condition`, dan `Serial Number` pada panel nonaktif
20. Verifikasi panel tidak memuat tombol `[Clear Field]`
21. Verifikasi panel tidak memuat tombol `[Save correction]`

### Pengajuan bukan milik approver tidak terkunci
22. Tampilkan Halaman Approval dengan kondisi K2
23. Verifikasi Decision pada baris `Laptop - 128` aktif
24. Verifikasi `[Submit]` aktif
25. Verifikasi notice `You cannot decide a registration you submitted.` tidak tampil

### Satu aset Brand atau Model tidak tersedia
26. Tampilkan Halaman Approval dengan kondisi K5
27. Verifikasi Decision pada baris `Laptop - 128` aktif
28. Pilih Decision `Return to Draft` pada baris `Laptop - 129`
29. Respons master menyatakan Model `Latitude 5440` tidak lagi tersedia (kondisi K5)
30. Verifikasi Badge Model pada baris `Laptop - 128` menampilkan `Unavailable`
31. Verifikasi Alert Warning tampil tanpa muat ulang halaman
32. Verifikasi Alert memuat `1 asset uses master data that is no longer available. Correct it, return it to Draft, or reject it before deciding.`
33. Verifikasi Alert tidak memuat salinan `1 asset uses master data that is no longer available. Return it to Draft or reject it before deciding.`
34. Verifikasi Decision pada baris `Laptop - 128` disabled
35. Arahkan kursor ke Decision pada baris `Laptop - 128`
36. Verifikasi tooltip `This asset uses master data that is no longer available.` tampil
37. Verifikasi Badge Model pada baris `Laptop - 129` tidak menampilkan `Unavailable`
38. Verifikasi Decision pada baris `Laptop - 129` dengan Decision `Return to Draft` aktif

### Dua aset Brand atau Model tidak tersedia
39. Tampilkan Halaman Approval dengan kondisi K6
40. Verifikasi Decision pada baris `Laptop - 130` aktif
41. Pilih Decision `Reject` pada baris `Office Desk - 12`
42. Respons master menyatakan Model `Latitude 5450` tidak lagi tersedia (kondisi K6)
43. Verifikasi Badge Model pada baris `Laptop - 130` menampilkan `Unavailable`
44. Verifikasi Badge Model pada baris `Laptop - 131` menampilkan `Unavailable`
45. Verifikasi Alert memuat `2 assets use master data that is no longer available. Correct them, return them to Draft, or reject them before deciding.`
46. Verifikasi Alert tidak memuat salinan `2 assets use master data that is no longer available. Return them to Draft or reject them before deciding.`
47. Verifikasi Decision pada baris `Office Desk - 12` dengan Decision `Reject` aktif

### Satu aset Asset Name atau Group tidak tersedia
48. Tampilkan Halaman Approval dengan kondisi K7
49. Verifikasi Decision pada baris `Monitor - 21` aktif
50. Pilih Decision `Reject` pada baris `Monitor - 24`
51. Respons master menyatakan Group `Gudang 3` tidak lagi tersedia (kondisi K7)
52. Verifikasi Alert Warning tampil tanpa muat ulang halaman
53. Verifikasi Alert memuat `1 asset uses master data that is no longer available. Return it to Draft or reject it before deciding.`
54. Verifikasi Alert tidak memuat salinan `1 asset uses master data that is no longer available. Correct it, return it to Draft, or reject it before deciding.`
55. Verifikasi Decision pada baris `Monitor - 21` disabled
56. Verifikasi Decision pada baris `Monitor - 24` dengan Decision `Reject` aktif

### Dua aset Asset Name atau Group tidak tersedia
57. Tampilkan Halaman Approval dengan kondisi K8
58. Verifikasi Decision pada baris `Monitor - 22` aktif
59. Respons master menyatakan Group `Gudang 4` tidak lagi tersedia (kondisi K8)
60. Verifikasi Alert memuat `2 assets use master data that is no longer available. Return them to Draft or reject them before deciding.`
61. Verifikasi Alert tidak memuat salinan `2 assets use master data that is no longer available. Correct them, return them to Draft, or reject them before deciding.`
62. Verifikasi Decision pada baris `Monitor - 22` disabled
63. Verifikasi Decision pada baris `Monitor - 23` disabled

### Dua jenis aset tidak tersedia tampil sebagai dua baris Alert
64. Tampilkan Halaman Approval dengan kondisi K9
65. Verifikasi Decision pada baris `Laptop - 128` aktif
66. Respons master menyatakan Model `Latitude 5440` tidak lagi tersedia (kondisi K9)
67. Respons master menyatakan Asset Name `Monitor` tidak lagi tersedia (kondisi K9)
68. Verifikasi baris Alert pertama `1 asset uses master data that is no longer available. Correct it, return it to Draft, or reject it before deciding.`
69. Verifikasi baris Alert kedua `2 assets use master data that is no longer available. Return them to Draft or reject them before deciding.`

### Brand tidak tersedia menandai baris Unavailable
70. Tampilkan Halaman Approval dengan kondisi K10
71. Verifikasi Decision pada baris `Laptop - 128` aktif
72. Respons master menyatakan Brand `Dell` tidak lagi tersedia (kondisi K10)
73. Verifikasi Badge Brand pada baris `Laptop - 128` menampilkan `Unavailable`
74. Verifikasi `Unavailable` tidak tampil pada Badge Brand baris `Office Desk - 12`

### Aset yang Brand dan Asset Name-nya sama-sama tidak tersedia terhitung di kedua baris Alert
75. Tampilkan Halaman Approval dengan kondisi K11
76. Verifikasi Decision pada baris `Laptop - 128` aktif
77. Respons master menyatakan Brand `Dell` tidak lagi tersedia (kondisi K11)
78. Respons master menyatakan Asset Name `Monitor` tidak lagi tersedia (kondisi K11)
79. Verifikasi baris Alert pertama `2 assets use master data that is no longer available. Correct them, return them to Draft, or reject them before deciding.`
80. Verifikasi baris Alert kedua `3 assets use master data that is no longer available. Return them to Draft or reject them before deciding.`

### Alasan disabled pada Bulk Action tampil saat hover
81. Tampilkan Halaman Approval dengan kondisi K1
82. Centang baris `Laptop - 128` pada grup `Laptop`
83. Arahkan kursor ke Bulk Action pada grup `Laptop`
84. Verifikasi alasan `You cannot decide a registration you submitted.` tersampaikan pada Bulk Action grup `Laptop` yang disabled
