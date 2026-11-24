---
id: TC-FA-FATR-UI-062-area-disposal-dm
title: "Area utama: field tab Disposal dan tab Damaged & Missing"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules:
  - §4.1#r66
  - §4.1#r153
  - §4.1#r154
  - §4.1#r155
  - §4.1#r166
  - §4.1#r172
  - §4.1#r187
  - §4.1#r192
  - §4.1#r209
  - §4.1#r221
  - §9.2#b71
  - §9.2#b85
  - §9.2#b424
  - §9.2#b425
  - §9.4.2#r9
  - §9.4.4#r19
  - §4.1#r189
  - §9.2#b423
  - FLD-43
smoke: []
dependsOn: []
trace:
  §4.1#r66: [2, 4, 57]
  §4.1#r153: [6, 33, 36, 41, 59]
  §4.1#r154: [7, 37, 42, 61]
  §4.1#r155: [8, 38, 43, 63]
  §4.1#r166: [28, 74]
  §4.1#r172: [29, 76]
  §4.1#r187: [19, 46, 48, 65]
  §4.1#r192: [20, 22, 50, 52, 67]
  §4.1#r209: [25, 54, 69]
  §4.1#r221: [26, 39, 44, 71]
  §9.2#b71: [15, 16]
  §9.2#b85: 30
  §9.2#b424: [10, 11]
  §9.2#b425: 29
  §9.4.2#r9: [15, 16]
  §9.4.4#r19: 17
  §4.1#r189: 80
  §9.2#b423: [11, 83]
  FLD-43: [85, 87, 89, 91]
anchor: [13, 78, 79, 82]
coverage:
  web: automated
---

# Area utama: field tab Disposal dan tab Damaged & Missing

## Prerequisites
- Aktor: Total Control (cakupan semua Group).
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-062-1: Pengaturan Company default tab Disposal pada All categories: Allow Disposal `Allow`, Allowed disposal types `Sell`, `Scrap`, `Donate`, `Trade-in`, Min asset age warning `12`, Max deviation from book value `30`, Max price drop from approved price `10`, Require approval `ON`, Approval type `Any one approver`, Transaction timeout `7`, Send email notifications `OFF`.
  - DU-062-2: Pengaturan Company default tab Damaged & Missing pada All categories: Long missing after `30`, After photo required `OFF`.
  - DU-062-3: Pengaturan Company default tab Disposal dengan Allowed disposal types hanya `Sell`.
  - DU-062-4: Pengaturan Company default tab Disposal pada All categories yang berbeda dari nilai awal: Allowed disposal types hanya `Sell`, Min asset age warning `24`, Max deviation from book value `50`, Max price drop from approved price `50`, Send email notifications `ON`.
  - DU-062-5: Pengaturan Company default tab Disposal pada All categories yang berbeda dari nilai awal: Require approval `OFF`.
  - DU-062-6: Pengaturan Company default tab Disposal pada All categories yang berbeda dari nilai awal: Require approval `ON`, Approval type `All approvers (AND)`.
  - DU-062-7: Pengaturan Company default tab Damaged & Missing pada All categories yang berbeda dari nilai awal: Long missing after `14`, After photo required `ON`.
- Kondisi:
  - K1: node All categories terpilih, tab Disposal aktif, nilai Company default memakai DU-062-1.
  - K2: node All categories terpilih, tab Damaged & Missing aktif, nilai Company default memakai DU-062-2.
  - K3: node All categories terpilih, tab Disposal aktif, Allowed disposal types hanya `Sell` memakai DU-062-3.
  - K4: node All categories terpilih, tab Disposal aktif, nilai Company default memakai DU-062-4.
  - K5: node All categories terpilih, tab Disposal aktif, nilai Company default memakai DU-062-5.
  - K6: node All categories terpilih, tab Disposal aktif, nilai Company default memakai DU-062-6.
  - K7: node All categories terpilih, tab Damaged & Missing aktif, nilai Company default memakai DU-062-7.

## Test Steps

### Eligibility dan Limits Disposal
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi `Allow Disposal` bernilai `Allow`
3. Buka daftar pilihan `Allow Disposal`
4. Verifikasi pilihan `Allow Disposal` adalah `Allow` dan `Deny`
5. Tutup daftar pilihan dengan Escape
6. Verifikasi `Allowed disposal types` terpilih `Sell`, `Scrap`, `Donate`, dan `Trade-in`
7. Verifikasi `Min asset age warning` bernilai `12`
8. Verifikasi `Max deviation from book value` bernilai `30`

### Evidence tidak ada di Disposal
9. Tampilkan Area utama dengan kondisi K1
10. Verifikasi tab `Disposal` memuat bagian `Limits` dan `Approval`
11. Verifikasi tab `Disposal` tidak memuat setting `Photo at start`, `Photo at end`, dan `After photo required`

### Pilihan terakhir Allowed disposal types tidak dapat dihapus
12. Tampilkan Area utama dengan kondisi K3
13. Verifikasi `Allowed disposal types` terpilih `Sell`
14. Hapus pilihan `Sell` pada `Allowed disposal types`
15. Verifikasi `Sell` tetap terpilih pada `Allowed disposal types`
16. Verifikasi pesan `At least one disposal type must be selected` tampil di bawah kontrol `Allowed disposal types`
17. Verifikasi tidak ada permintaan Save yang terkirim akibat penghapusan itu

### Approval Disposal
18. Tampilkan Area utama dengan kondisi K1
19. Verifikasi `Require approval` bernilai `ON`
20. Verifikasi `Approval type` bernilai `Any one approver`
21. Buka daftar pilihan `Approval type`
22. Verifikasi pilihan `Approval type` adalah `Any one approver` dan `All approvers (AND)`
23. Tutup daftar pilihan dengan Escape

### Reminders dan Notifications Disposal
24. Tampilkan Area utama dengan kondisi K1
25. Verifikasi `Transaction timeout` bernilai `7`
26. Verifikasi `Send email notifications` bernilai `OFF`

### Tab Damaged & Missing
27. Tampilkan Area utama dengan kondisi K2
28. Verifikasi `Long missing after` bernilai `30`
29. Verifikasi `After photo required` bernilai `OFF`
30. Verifikasi tab `Damaged & Missing` tidak memuat bagian `Overrides`

### Daftar pilihan Allowed disposal types
31. Tampilkan Area utama dengan kondisi K1
32. Buka daftar pilihan `Allowed disposal types`
33. Verifikasi pilihan `Allowed disposal types` adalah `Sell`, `Scrap`, `Donate`, dan `Trade-in`
34. Tutup daftar pilihan dengan Escape

### Reset to Default mengembalikan Limits dan Notifications Disposal ke nilai awal
35. Tampilkan Area utama dengan kondisi K4
36. Verifikasi `Allowed disposal types` tampil dengan pilihan `Sell` saja sebelum Reset to Default
37. Verifikasi `Min asset age warning` bernilai `24`
38. Verifikasi `Max deviation from book value` bernilai `50`
39. Verifikasi `Send email notifications` bernilai `ON`
40. Klik `Reset to Default`
41. Verifikasi `Allowed disposal types` kembali ke nilai awal terpilih `Sell`, `Scrap`, `Donate`, dan `Trade-in`
42. Verifikasi `Min asset age warning` kembali ke nilai awal `12`
43. Verifikasi `Max deviation from book value` kembali ke nilai awal `30`
44. Verifikasi `Send email notifications` kembali ke nilai awal `OFF`

### Reset to Default mengembalikan Require approval Disposal ke nilai awal
45. Tampilkan Area utama dengan kondisi K5
46. Verifikasi `Require approval` bernilai `OFF`
47. Klik `Reset to Default`
48. Verifikasi `Require approval` kembali ke nilai awal `ON`

### Reset to Default mengembalikan Approval type Disposal ke nilai awal
49. Tampilkan Area utama dengan kondisi K6
50. Verifikasi `Approval type` bernilai `All approvers (AND)`
51. Klik `Reset to Default`
52. Verifikasi `Approval type` kembali ke nilai awal `Any one approver`

### Satuan Transaction timeout tab Disposal
53. Tampilkan Area utama dengan kondisi K1
54. Verifikasi addon `Transaction timeout` menunjukkan satuan `days`

### Teks bantuan label field tab Disposal
55. Tampilkan Area utama dengan kondisi K1
56. Pindahkan fokus keyboard ke bantuan label `Allow Disposal`
57. Verifikasi teks bantuan label `Allow Disposal` tersampaikan berbunyi `Whether this transaction can be made for assets in this category.`
58. Pindahkan fokus keyboard ke bantuan label `Allowed disposal types`
59. Verifikasi teks bantuan label `Allowed disposal types` tersampaikan berbunyi `Disposal types that can be used for assets in this category.`
60. Pindahkan fokus keyboard ke bantuan label `Min asset age warning`
61. Verifikasi teks bantuan label `Min asset age warning` tersampaikan berbunyi `Shows a warning when disposing of an asset younger than this age.`
62. Pindahkan fokus keyboard ke bantuan label `Max deviation from book value`
63. Verifikasi teks bantuan label `Max deviation from book value` tersampaikan berbunyi `A sale price below book value by more than this percentage shows a warning and requires a reason.`
64. Pindahkan fokus keyboard ke bantuan label `Require approval`
65. Verifikasi teks bantuan label `Require approval` tersampaikan berbunyi `Requires approval before the transaction proceeds.`
66. Pindahkan fokus keyboard ke bantuan label `Approval type`
67. Verifikasi teks bantuan label `Approval type` tersampaikan berbunyi `Whether one approver or all approvers must approve.`
68. Pindahkan fokus keyboard ke bantuan label `Transaction timeout`
69. Verifikasi teks bantuan label `Transaction timeout` tersampaikan berbunyi `Days a transaction can wait at a step before it is closed automatically.`
70. Pindahkan fokus keyboard ke bantuan label `Send email notifications`
71. Verifikasi teks bantuan label `Send email notifications` tersampaikan berbunyi `Also sends this transaction's notifications by email.`

### Teks bantuan label field tab Damaged & Missing
72. Tampilkan Area utama dengan kondisi K2
73. Pindahkan fokus keyboard ke bantuan label `Long missing after`
74. Verifikasi teks bantuan label `Long missing after` tersampaikan berbunyi `Days missing before an asset is flagged as long missing; 0 turns this off.`
75. Pindahkan fokus keyboard ke bantuan label `After photo required`
76. Verifikasi teks bantuan label `After photo required` tersampaikan berbunyi `Requires an after photo when marking a damaged asset as repaired.`

### Auto-approve tidak ada di tab Disposal
77. Tampilkan Area utama dengan kondisi K6
78. Verifikasi `Require approval` pada tab `Disposal` bernilai `ON`
79. Verifikasi `Approval type` pada tab `Disposal` bernilai `All approvers (AND)`
80. Verifikasi setting `Auto-approve` tidak ada pada tab `Disposal` karena tidak dirender

### Photo at start dan Photo at end tidak ada di tab Damaged & Missing
81. Tampilkan Area utama dengan kondisi K7
82. Verifikasi `After photo required` pada tab `Damaged & Missing` bernilai `ON`
83. Verifikasi setting `Photo at start` dan `Photo at end` tidak ada pada tab `Damaged & Missing`

### Max price drop from approved price pada tab Disposal
84. Tampilkan Area utama dengan kondisi K1
85. Verifikasi `Max price drop from approved price` bernilai `10`
86. Pindahkan fokus keyboard ke bantuan label `Max price drop from approved price`
87. Verifikasi teks bantuan label `Max price drop from approved price` tersampaikan berbunyi `A final price lower than the approved price by more than this percentage needs approval again before execution.`

### Reset to Default mengembalikan Max price drop from approved price ke nilai awal
88. Tampilkan Area utama dengan kondisi K4
89. Verifikasi `Max price drop from approved price` bernilai `50`
90. Klik `Reset to Default`
91. Verifikasi `Max price drop from approved price` kembali ke nilai awal `10`
