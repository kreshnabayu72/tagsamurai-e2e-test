---
id: TC-FA-FATR-UI-061-area-transfer
title: "Area utama: field tab Transfer"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules:
  - §4.1#r66
  - §4.1#r135
  - §4.1#r136
  - §4.1#r138
  - §4.1#r137
  - §4.1#r139
  - §4.1#r171
  - §4.1#r173
  - §4.1#r187
  - §4.1#r192
  - §4.1#r189
  - §4.1#r191
  - §4.1#r193
  - §4.1#r206
  - §4.1#r209
  - §4.1#r221
  - §9.2#b423
smoke: []
dependsOn: []
trace:
  §4.1#r66: [2, 4, 76]
  §4.1#r135: [6, 8, 42, 46, 78]
  §4.1#r136: [10, 12, 80]
  §4.1#r138: [15, 17, 43, 47, 84]
  §4.1#r137: [14, 19, 72, 82]
  §4.1#r139: 20
  §4.1#r171: [22, 60, 64, 86]
  §4.1#r173: [23, 61, 65, 88]
  §4.1#r187: [25, 56, 58, 90]
  §4.1#r192: [26, 28, 68, 70, 92]
  §4.1#r189: [30, 33, 62, 66, 94]
  §4.1#r191: [31, 50, 53, 96]
  §4.1#r193: [34, 36, 51, 54, 98]
  §4.1#r206: 36
  §4.1#r209: [39, 73, 100]
  §4.1#r221: [40, 44, 48, 102]
  §9.2#b423: [22, 23]
anchor: []
coverage:
  web: automated
---

# Area utama: field tab Transfer

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-061-1: Pengaturan Company default tab Transfer pada All categories: Allow Transfer `Allow`, Destination scope `Any Group`, Change Cost Center with Group `Never`, In-transit overdue after `7`, Destination quota check `ON`, Photo at start `ON`, Photo at end `ON`, Require approval `ON`, Approval type `Any one approver`, Auto-approve `ON`, Auto-approve when destination in same parent Group `ON`, Approval scope `Both`, Transaction timeout `7`, Send email notifications `OFF`.
  - DU-061-2: Pengaturan Category leaf `Machinery`: semua field Inherit, Change Cost Center with Group Company default `Never`.
  - DU-061-3: Pengaturan Company default tab Transfer pada All categories yang berbeda dari nilai awal: Destination scope `Within same parent Group`, Destination quota check `OFF`, Send email notifications `ON`.
  - DU-061-4: Pengaturan Company default tab Transfer pada All categories yang berbeda dari nilai awal: Require approval `ON`, Auto-approve `ON`, Auto-approve when destination in same parent Group `OFF`, Approval scope `Origin only`, Approval type `All approvers (AND)`.
  - DU-061-6: Pengaturan Company default tab Transfer pada All categories yang berbeda dari nilai awal: Photo at start `OFF`, Photo at end `OFF`, Require approval `ON`, Auto-approve `OFF`.
  - DU-061-5: Pengaturan Company default tab Transfer pada All categories yang berbeda dari nilai awal: Require approval `OFF`.
- Kondisi:
  - K1: node All categories terpilih, tab Transfer aktif, Approval Workflow tersedia di plan, nilai Company default memakai DU-061-1.
  - K2: node Category leaf `Machinery` terpilih, tab Transfer aktif, nilai memakai DU-061-2.
  - K3: node All categories terpilih, tab Transfer aktif, nilai Company default memakai DU-061-3.
  - K4: node All categories terpilih, tab Transfer aktif, Approval Workflow tersedia di plan, nilai Company default memakai DU-061-4.
  - K5: node All categories terpilih, tab Transfer aktif, nilai Company default memakai DU-061-5.
  - K6: node All categories terpilih, tab Transfer aktif, nilai Company default memakai DU-061-6.

## Test Steps

### Eligibility dan Limits Transfer
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi `Allow Transfer` bernilai `Allow`
3. Buka daftar pilihan `Allow Transfer`
4. Verifikasi pilihan `Allow Transfer` adalah `Allow` dan `Deny`
5. Tutup daftar pilihan dengan Escape
6. Verifikasi `Destination scope` bernilai `Any Group`
7. Buka daftar pilihan `Destination scope`
8. Verifikasi pilihan `Destination scope` adalah `Within same parent Group` dan `Any Group`
9. Tutup daftar pilihan dengan Escape
10. Verifikasi `Change Cost Center with Group` bernilai `Never`
11. Buka daftar pilihan `Change Cost Center with Group`
12. Verifikasi pilihan `Change Cost Center with Group` adalah `Never` dan `Always`
13. Tutup daftar pilihan dengan Escape
14. Verifikasi `In-transit overdue after` bernilai `7`
15. Verifikasi `Destination quota check` bernilai `ON`
16. Matikan `Destination quota check`
17. Verifikasi `Destination quota check` bernilai `OFF`

### Change Cost Center with Group hanya di All categories
18. Tampilkan Area utama dengan kondisi K2
19. Verifikasi tab `Transfer` memuat field `In-transit overdue after` dengan tombol `Set own value`
20. Verifikasi `Change Cost Center with Group` di Category leaf `Machinery` tidak punya kontrol dan tidak punya tombol `Set own value`

### Evidence Transfer
21. Tampilkan Area utama dengan kondisi K1
22. Verifikasi `Photo at start` bernilai `ON` pada bagian `Evidence`
23. Verifikasi `Photo at end` bernilai `ON` pada bagian `Evidence`

### Approval Transfer
24. Tampilkan Area utama dengan kondisi K1
25. Verifikasi `Require approval` bernilai `ON`
26. Verifikasi `Approval type` bernilai `Any one approver`
27. Buka daftar pilihan `Approval type`
28. Verifikasi pilihan `Approval type` adalah `Any one approver` dan `All approvers (AND)`
29. Tutup daftar pilihan dengan Escape
30. Verifikasi `Auto-approve` bernilai `ON`
31. Verifikasi `Auto-approve when destination in same parent Group` bernilai `ON`
32. Matikan `Auto-approve`
33. Verifikasi `Auto-approve` bernilai `OFF`
34. Verifikasi `Approval scope` bernilai `Both`
35. Buka daftar pilihan `Approval scope`
36. Verifikasi pilihan `Approval scope` adalah `Origin only`, `Destination only`, dan `Both`
37. Tutup daftar pilihan dengan Escape

### Reminders dan Notifications Transfer
38. Tampilkan Area utama dengan kondisi K1
39. Verifikasi `Transaction timeout` bernilai `7`
40. Verifikasi `Send email notifications` bernilai `OFF`

### Reset to Default mengembalikan Destination dan Notifications Transfer ke nilai awal
41. Tampilkan Area utama dengan kondisi K3
42. Verifikasi `Destination scope` bernilai `Within same parent Group`
43. Verifikasi `Destination quota check` bernilai `OFF`
44. Verifikasi `Send email notifications` bernilai `ON`
45. Klik `Reset to Default`
46. Verifikasi `Destination scope` kembali ke nilai awal `Any Group`
47. Verifikasi `Destination quota check` kembali ke nilai awal `ON`
48. Verifikasi `Send email notifications` kembali ke nilai awal `OFF`

### Reset to Default mengembalikan Approval scope Transfer ke nilai awal
49. Tampilkan Area utama dengan kondisi K4
50. Verifikasi `Auto-approve when destination in same parent Group` bernilai `OFF`
51. Verifikasi `Approval scope` tampil dengan nilai `Origin only` sebelum Reset to Default
52. Klik `Reset to Default`
53. Verifikasi `Auto-approve when destination in same parent Group` kembali ke nilai awal `ON`
54. Verifikasi `Approval scope` kembali ke nilai awal `Both`

### Reset to Default mengembalikan Require approval Transfer ke nilai awal
55. Tampilkan Area utama dengan kondisi K5
56. Verifikasi `Require approval` bernilai `OFF`
57. Klik `Reset to Default`
58. Verifikasi `Require approval` kembali ke nilai awal `ON`

### Reset to Default mengembalikan Evidence dan Auto-approve Transfer ke nilai awal
59. Tampilkan Area utama dengan kondisi K6
60. Verifikasi `Photo at start` bernilai `OFF` pada bagian `Evidence`
61. Verifikasi `Photo at end` bernilai `OFF` pada bagian `Evidence`
62. Verifikasi `Auto-approve` bernilai `OFF`
63. Klik `Reset to Default`
64. Verifikasi `Photo at start` kembali ke nilai awal `ON` pada bagian `Evidence`
65. Verifikasi `Photo at end` kembali ke nilai awal `ON` pada bagian `Evidence`
66. Verifikasi `Auto-approve` kembali ke nilai awal `ON`

### Reset to Default mengembalikan Approval type Transfer ke nilai awal
67. Tampilkan Area utama dengan kondisi K4
68. Verifikasi `Approval type` bernilai `All approvers (AND)`
69. Klik `Reset to Default`
70. Verifikasi `Approval type` kembali ke nilai awal `Any one approver`

### Satuan field angka tab Transfer
71. Tampilkan Area utama dengan kondisi K1
72. Verifikasi addon `In-transit overdue after` menunjukkan satuan `days`
73. Verifikasi addon `Transaction timeout` menunjukkan satuan `days`

### Teks bantuan label field tab Transfer
74. Tampilkan Area utama dengan kondisi K1
75. Pindahkan fokus keyboard ke bantuan label `Allow Transfer`
76. Verifikasi teks bantuan label `Allow Transfer` tersampaikan berbunyi `Whether this transaction can be made for assets in this category.`
77. Pindahkan fokus keyboard ke bantuan label `Destination scope`
78. Verifikasi teks bantuan label `Destination scope` tersampaikan berbunyi `Which groups an asset can be transferred to.`
79. Pindahkan fokus keyboard ke bantuan label `Change Cost Center with Group`
80. Verifikasi teks bantuan label `Change Cost Center with Group` tersampaikan berbunyi `Whether the asset's cost center changes to the destination group's default cost center when the transfer is completed.`
81. Pindahkan fokus keyboard ke bantuan label `In-transit overdue after`
82. Verifikasi teks bantuan label `In-transit overdue after` tersampaikan berbunyi `Days in transit before a transfer is flagged as overdue.`
83. Pindahkan fokus keyboard ke bantuan label `Destination quota check`
84. Verifikasi teks bantuan label `Destination quota check` tersampaikan berbunyi `Checks the destination group's asset quota when a transfer is submitted and when it is completed.`
85. Pindahkan fokus keyboard ke bantuan label `Photo at start`
86. Verifikasi teks bantuan label `Photo at start` tersampaikan berbunyi `Requires a camera photo at the first step of the transaction.`
87. Pindahkan fokus keyboard ke bantuan label `Photo at end`
88. Verifikasi teks bantuan label `Photo at end` tersampaikan berbunyi `Requires a camera photo at the last step of the transaction.`
89. Pindahkan fokus keyboard ke bantuan label `Require approval`
90. Verifikasi teks bantuan label `Require approval` tersampaikan berbunyi `Requires approval before the transaction proceeds.`
91. Pindahkan fokus keyboard ke bantuan label `Approval type`
92. Verifikasi teks bantuan label `Approval type` tersampaikan berbunyi `Whether one approver or all approvers must approve.`
93. Pindahkan fokus keyboard ke bantuan label `Auto-approve`
94. Verifikasi teks bantuan label `Auto-approve` tersampaikan berbunyi `Approves requests automatically when the conditions below are met.`
95. Pindahkan fokus keyboard ke bantuan label `Auto-approve when destination in same parent Group`
96. Verifikasi teks bantuan label `Auto-approve when destination in same parent Group` tersampaikan berbunyi `Transfers to a group under the same parent are approved automatically.`
97. Pindahkan fokus keyboard ke bantuan label `Approval scope`
98. Verifikasi teks bantuan label `Approval scope` tersampaikan berbunyi `Which side of the transfer must approve: origin, destination, or both.`
99. Pindahkan fokus keyboard ke bantuan label `Transaction timeout`
100. Verifikasi teks bantuan label `Transaction timeout` tersampaikan berbunyi `Days a transaction can wait at a step before it is closed automatically.`
101. Pindahkan fokus keyboard ke bantuan label `Send email notifications`
102. Verifikasi teks bantuan label `Send email notifications` tersampaikan berbunyi `Also sends this transaction's notifications by email.`
