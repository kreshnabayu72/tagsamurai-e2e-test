---
id: TC-FA-FATR-UI-125-area-audit-maintenance-geolocation
title: "Area utama: field tab Audit, Maintenance, dan Geolocation"
layer: ui-client
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r4", "§4.1#r5", "§4.1#r6", "§4.1#r44", "§4.1#r45", "§4.1#r46", "§4.1#r47", "§Aturan Logika Modul#r107", "§Aturan Logika Modul#r108", "§Aturan Logika Modul#r116", "§Aturan Logika Modul#r117", "§Aturan Logika Modul#r120", "§Aturan Logika Modul#r122", "§4.1#r225", "§4.1#p39", "§4.1#r187", "§4.1#r192", "§4.1#r221", "§4.1#r229", "§4.1#r230", "§4.1#r231", "§4.1#r237", "§4.1#r238", "§4.1#r242", "§9.4.2#r71", "§9.2#b566", "FLD-42"]
smoke: []
dependsOn: []
trace:
  "§4.1#r4": [2, 3]
  "§4.1#r5": [28, 30, 45]
  "§4.1#r6": [50, 51]
  "§4.1#r44": [50, 51]
  "§4.1#r45": [25, 26, 61, 62]
  "§4.1#r46": [2, 3, 79, 80, 81, 82]
  "§4.1#r47": [28, 29, 30]
  "§Aturan Logika Modul#r107": [52, 53]
  "§Aturan Logika Modul#r108": [60, 61, 62]
  "§Aturan Logika Modul#r116": [5, 8, 11, 14]
  "§Aturan Logika Modul#r117": [25, 26, 75, 76, 77]
  "§Aturan Logika Modul#r120": 29
  "§Aturan Logika Modul#r122": [30, 43]
  "§4.1#r225": [5, 7, 19, 22]
  "§4.1#p39": [25, 26]
  "§4.1#r187": [8, 10]
  "§4.1#r192": [11, 13]
  "§4.1#r221": [14, 16]
  "§4.1#r229": [31, 33, 85, 88]
  "§4.1#r230": [34, 36]
  "§4.1#r231": [37, 39]
  "§4.1#r237": [55, 56, 58]
  "§4.1#r238": 54
  "§4.1#r242": [68, 69, 70, 71]
  "§9.4.2#r71": [45, 46, 47, 48]
  "§9.2#b566": [45, 46, 47]
  "FLD-42": [29, 91]
anchor: [24, 41, 64, 65, 66, 73, 74]
coverage:
  web: automated
---

# Area utama: field tab Audit, Maintenance, dan Geolocation

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-125-1: Pengaturan Company default tab Audit pada All categories: Grace period `3`, Require approval `ON`, Approval type `Any one approver`, Send email notifications `OFF`.
  - DU-125-2: Pengaturan Company default tab Maintenance pada All categories: Reminder before due `3`, Photo after `ON`, Require approval to close `OFF`.
  - DU-125-3: Pengaturan Category leaf `Machinery` tab Maintenance: semua field Inherit, Company default memakai DU-125-2.
  - DU-125-4: Pengaturan Company default tab Geolocation: Require location Audit `ON`, Require location Maintenance `ON`.
  - DU-125-5: Pengaturan Company default tab Geolocation: Require location Audit `OFF`, Require location Maintenance `OFF`.
  - DU-125-6: Nilai Grace period yang diisi: `5`.
  - DU-125-7: Nilai Grace period di bawah batas yang diisi: `-1`.
  - DU-125-8: Pengaturan Company default tab Audit pada All categories: Grace period `7`, Require approval `ON`, Approval type `All approvers (AND)`, Send email notifications `ON`.
  - DU-125-9: Pengaturan Company default tab Maintenance pada All categories: Reminder before due `7`, Photo after `OFF`, Require approval to close `ON`.
  - DU-125-10: Nilai Reminder before due yang diisi: `4`.
  - DU-125-11: Nilai Reminder before due di bawah batas yang diisi: `-1`.
- Kondisi:
  - K1: node All categories terpilih, tab Audit aktif, nilai Company default memakai DU-125-1; plan menyediakan Approval Workflow dan addon Audit aktif.
  - K2: node All categories terpilih, tab Maintenance aktif, nilai Company default memakai DU-125-2; plan menyediakan Approval Workflow dan addon Maintenance aktif.
  - K3: node Category leaf `Machinery` terpilih, tab Maintenance aktif, semua field Inherit memakai DU-125-3; addon Maintenance aktif.
  - K4: node All categories terpilih, tab Geolocation aktif, nilai Company default memakai DU-125-5; addon Audit dan addon Maintenance aktif.
  - K5: node All categories terpilih, tab Geolocation aktif, nilai Company default memakai DU-125-4; addon Audit dan addon Maintenance aktif.
  - K6: node All categories terpilih, tab Borrow aktif.
  - K7: node Category leaf `Machinery` terpilih, tab Geolocation aktif, nilai Company default memakai DU-125-4; addon Audit dan addon Maintenance aktif.
  - K8: node Category leaf `Machinery` terpilih, tab Audit aktif, nilai Company default memakai DU-125-8; plan menyediakan Approval Workflow dan addon Audit aktif.
  - K9: node All categories terpilih, tab Maintenance aktif, nilai Company default memakai DU-125-9; plan menyediakan Approval Workflow dan addon Maintenance aktif.

## Test Steps

### Tab Audit memuat bagian Limits, Approval, dan Notifications saja
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi tab `Audit` memuat bagian `Limits`, `Approval`, dan `Notifications`
3. Verifikasi tab `Audit` tidak memuat bagian `Eligibility`, `Evidence`, `Reminders`, dan `Overrides`

### Field tab Audit dan teks bantunya
4. Tampilkan Area utama dengan kondisi K1
5. Verifikasi `Grace period` bernilai `3`
6. Arahkan pointer ke label `Grace period`
7. Verifikasi teks bantu `Extra days after an audit task's duration ends before it becomes overdue.` tersampaikan pada label `Grace period`
8. Verifikasi `Require approval` bernilai `ON`
9. Arahkan pointer ke label `Require approval`
10. Verifikasi teks bantu `Requires approval before the transaction proceeds.` tersampaikan pada label `Require approval`
11. Verifikasi `Approval type` bernilai `Any one approver`
12. Arahkan pointer ke label `Approval type`
13. Verifikasi teks bantu `Whether one approver or all approvers must approve.` tersampaikan pada label `Approval type`
14. Verifikasi `Send email notifications` bernilai `OFF`
15. Arahkan pointer ke label `Send email notifications`
16. Verifikasi teks bantu `Also sends this transaction's notifications by email.` tersampaikan pada label `Send email notifications`

### Grace period menerima angka bulat dan tidak menerima nilai di bawah 0
17. Tampilkan Area utama dengan kondisi K1
18. Isi `Grace period` `5`
19. Verifikasi `Grace period` bernilai `5`
20. Isi `Grace period` `-1`
21. Pindahkan fokus dari kontrol `Grace period`
22. Verifikasi `Grace period` bernilai `0`

### Tab Audit tanpa Inherit, Set own value, dan Reset to inherit
23. Tampilkan Area utama dengan kondisi K1
24. Verifikasi `Grace period` bernilai `3` tampil sebagai kontrol bernilai sendiri
25. Verifikasi tab `Audit` tanpa tombol `Set own value` dan tanpa tombol `Reset to inherit` pada baris field mana pun
26. Verifikasi tab `Audit` tidak menampilkan teks `Inherit` pada field mana pun

### Tab Maintenance memuat bagian Routine dan field-nya
27. Tampilkan Area utama dengan kondisi K2
28. Verifikasi tab `Maintenance` memuat bagian `Routine`
29. Verifikasi bagian `Routine` memuat `Reminder before due`, `Photo after`, `Require approval to close`, dan `Require scan to start`
30. Verifikasi tab `Maintenance` tidak memuat bagian `Overrides`
31. Verifikasi `Reminder before due` bernilai `3`
32. Arahkan pointer ke label `Reminder before due`
33. Verifikasi teks bantu `Days before a routine maintenance due date to send a reminder.` tersampaikan pada label `Reminder before due`
34. Verifikasi `Photo after` bernilai `ON`
35. Arahkan pointer ke label `Photo after`
36. Verifikasi teks bantu `Requires a photo of the finished work to complete routine maintenance.` tersampaikan pada label `Photo after`
37. Verifikasi `Require approval to close` bernilai `OFF`
38. Arahkan pointer ke label `Require approval to close`
39. Verifikasi teks bantu `Requires approval before completed routine maintenance is closed.` tersampaikan pada label `Require approval to close`

### Tab transaksi memuat tombol Override
40. Tampilkan Area utama dengan kondisi K6
41. Verifikasi tab `Borrow` memuat tombol `[+ Override]`

### Maintenance tidak tersedia sebagai transaksi override
42. Tampilkan Area utama dengan kondisi K2
43. Verifikasi tab `Maintenance` tidak memuat tombol `[+ Override]`

### Category leaf tanpa nilai sendiri menampilkan Inherit pada tab Maintenance
44. Tampilkan Area utama dengan kondisi K3
45. Verifikasi `Reminder before due` menampilkan teks Inherit dengan nilai `3` dan sumber `Company default`
46. Verifikasi `Photo after` menampilkan teks Inherit dengan sumber `Company default`
47. Verifikasi `Require approval to close` menampilkan teks Inherit dengan sumber `Company default`
48. Verifikasi tab `Maintenance` tidak memuat bagian `Overrides`

### Tab Geolocation memuat bagian Location capture dan baris Require location
49. Tampilkan Area utama dengan kondisi K4
50. Verifikasi tab `Geolocation` memuat bagian `Location capture`
51. Verifikasi tab `Geolocation` tidak memuat bagian `Eligibility`, `Limits`, `Evidence`, `Approval`, `Reminders`, `Notifications`, dan `Overrides`
52. Verifikasi bagian `Location capture` memuat baris `Audit` dan baris `Maintenance`
53. Verifikasi bagian `Location capture` tidak memuat baris `Borrow`, `Assign`, `Transfer`, dan `Disposal`
54. Verifikasi baris `Audit` dan baris `Maintenance` masing-masing berupa switch berlabel nama transaksinya
55. Verifikasi baris `Audit` pada Require location bernilai `OFF`
56. Verifikasi baris `Maintenance` pada Require location bernilai `OFF`
57. Arahkan pointer ke label `Require location`
58. Verifikasi teks bantu `Requires the device location to be recorded before the transaction can be submitted.` tersampaikan pada label `Require location`

### Tab Geolocation tanpa nilai per Category, Inherit, Set own value, dan Reset to inherit
59. Tampilkan Area utama dengan kondisi K7
60. Verifikasi baris `Audit` pada Require location bernilai `ON` sebagai nilai Company default pada node Category `Machinery`
61. Verifikasi tab `Geolocation` tanpa tombol `Set own value` dan tanpa tombol `Reset to inherit` pada baris mana pun
62. Verifikasi tab `Geolocation` tidak menampilkan teks `Inherit` pada baris mana pun

### Reset to Default di tab Geolocation mengembalikan Require location semua transaksi ke OFF sebagai draft
63. Tampilkan Area utama dengan kondisi K5
64. Verifikasi baris `Audit` pada Require location bernilai `ON`
65. Verifikasi baris `Maintenance` pada Require location bernilai `ON`
66. Verifikasi tombol `Save` disabled karena belum ada perubahan
67. Klik `Reset to Default`
68. Verifikasi baris `Audit` pada Require location bernilai `OFF`
69. Verifikasi baris `Maintenance` pada Require location bernilai `OFF`
70. Verifikasi tombol `Save` aktif karena perubahan masuk draft
71. Verifikasi tidak ada permintaan Save yang terkirim akibat Reset to Default

### Tab Audit di Category leaf sama dengan Company default tanpa Inherit
72. Tampilkan Area utama dengan kondisi K8
73. Verifikasi `Grace period` bernilai `7` sebagai nilai Company default pada node Category `Machinery`
74. Verifikasi `Approval type` bernilai `All approvers (AND)` sebagai nilai Company default pada node Category `Machinery`
75. Verifikasi tab `Audit` tanpa tombol `Set own value` dan tanpa tombol `Reset to inherit` pada baris field mana pun
76. Verifikasi tab `Audit` tidak menampilkan teks `Inherit` pada field mana pun
77. Verifikasi tab `Audit` tidak memuat bagian `Overrides`

### Field tab Audit berada di bagiannya
78. Tampilkan Area utama dengan kondisi K8
79. Verifikasi bagian `Limits` memuat `Grace period`
80. Verifikasi bagian `Approval` memuat `Require approval`
81. Verifikasi bagian `Approval` memuat `Approval type`
82. Verifikasi bagian `Notifications` memuat `Send email notifications`

### Reminder before due menerima angka bulat dan tidak menerima nilai di bawah 0
83. Tampilkan Area utama dengan kondisi K9
84. Isi `Reminder before due` `4`
85. Verifikasi `Reminder before due` bernilai `4`
86. Isi `Reminder before due` `-1`
87. Pindahkan fokus dari kontrol `Reminder before due`
88. Verifikasi `Reminder before due` bernilai `0`

### Tooltip Require scan to start
89. Tampilkan Area utama dengan kondisi K2
90. Arahkan pointer ke label `Require scan to start`
91. Verifikasi teks bantu `Requires scanning the asset's TAG before routine maintenance can start.` tersampaikan pada label `Require scan to start`
