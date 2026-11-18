---
id: TC-FA-FATR-UI-066-area-plan
title: "Area utama: tampilan field dan tab bergerbang plan"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules:
  - §Aturan Logika Modul#r77
  - §Aturan Logika Modul#r78
  - §Aturan Logika Modul#r79
  - §Aturan Logika Modul#r81
  - §Aturan Logika Modul#r85
  - §Aturan Logika Modul#r88
  - §Aturan Logika Modul#r90
  - §Aturan Logika Modul#r92
  - §Aturan Logika Modul#r106
  - §4.1#r63
  - §4.1#r65
  - AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f
  - §4.1#r256
  - §4.3#r12
  - §4.3#r13
  - §4.3#r14
  - §4.3#r18
  - §4.3#r33
  - §4.3#r34
  - §4.3#r35
  - §4.3#r36
  - §4.3#r37
  - §4.3#p2
  - §7#r20
  - §7#r21
  - §9.2#b2
  - §9.2#b4
  - §9.4.2#r16
  - §9.4.2#r99
  - §9.4.4#r2
  - §9.4.4#r20
  - §9.10.1#b3
  - §9.10.1#b6
  - §9.10.1#p11
  - §9.10.1#p13
  - §9.10.2#b3
  - §9.10.4#b1
  - §9.4.2#r19
smoke: []
dependsOn: []
trace:
  §Aturan Logika Modul#r77: [5, 6, 7, 8, 29, 30, 79, 80, 83, 111, 112, 114, 116]
  §Aturan Logika Modul#r78: 14
  §Aturan Logika Modul#r79: [5, 6, 7, 8, 29]
  §Aturan Logika Modul#r81: 13
  §Aturan Logika Modul#r85: [35, 36]
  §Aturan Logika Modul#r88: [35, 36]
  §Aturan Logika Modul#r90: 41
  §Aturan Logika Modul#r92: [48, 49, 50]
  §Aturan Logika Modul#r106: [53, 56]
  §4.1#r63: [10, 38, 40]
  §4.1#r65: [10, 38, 40]
  AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f: [3]
  §4.1#r256: 32
  §4.3#r12: [35, 36, 38, 40, 44, 94, 100, 101, 102]
  §4.3#r13: [46, 49, 53, 55]
  §4.3#r14: [60, 63, 67, 69]
  §4.3#r18: [28, 32]
  §4.3#r33: [10]
  §4.3#r34: [26, 98]
  §4.3#r35: [5, 6, 7, 8]
  §4.3#r36: [3, 74, 76]
  §4.3#r37: [18, 19, 106, 107, 108, 109]
  §4.3#p2: [19, 20, 22, 23, 86, 87, 88, 91, 92, 93]
  §7#r20: [2, 16, 74, 76, 78, 82]
  §7#r21: 72
  §9.2#b2: [47, 50, 52, 58, 61, 64, 66, 70]
  §9.2#b4: [32, 33]
  §9.4.2#r16: [46, 49, 53, 55]
  §9.4.2#r99: 12
  §9.4.4#r2: [46, 53]
  §9.4.4#r20: 12
  §9.10.1#b3: 5
  §9.10.1#b6: 4
  §9.10.1#p11: 5
  §9.10.1#p13: 4
  §9.10.2#b3: [35, 36]
  §9.10.4#b1: [60, 63, 67, 69]
  §9.4.2#r19: 72
anchor: [25, 43, 85, 90, 96, 97, 104, 105]
coverage:
  web: automated
---
# Area utama: tampilan field dan tab bergerbang plan

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-066-1: Pengaturan Company default tab Borrow pada All categories: Require approval tersimpan `ON`, Auto-approve tersimpan `ON`, Auto-approve when duration ≤ tersimpan `3`, Approval type tersimpan `All approvers (AND)`, Self service `OFF`, Max duration `30`.
  - DU-066-2: Pengaturan Company default tab Borrow pada All categories: Require approval tersimpan `ON`, Auto-approve tersimpan `OFF`, Approval type tersimpan `All approvers (AND)`.
  - DU-066-3: Pengaturan Category leaf `Machinery` tab Borrow: semua field Inherit, Company default Require approval `ON` dan Self service `OFF`.
  - DU-066-4: Pengaturan Company default tab Transfer pada All categories: Require approval tersimpan `ON`, Auto-approve when destination in same parent Group tersimpan `ON`, Approval scope tersimpan `Origin only`, Approval type tersimpan `All approvers (AND)`, Auto-approve tersimpan `ON`, In-transit overdue after `10`.
  - DU-066-5: Pengaturan Company default tab Borrow pada All categories: Duration unit tersimpan `Hours`, Self service tersimpan `ON`, Max duration `30`.
  - DU-066-6: Pengaturan Category leaf `Machinery` tab Borrow: semua field Inherit.
  - DU-066-7: Pengaturan Company default tab Borrow pada All categories: Self service `ON`, Auto-approve tersimpan `ON`, Auto-approve when duration ≤ tersimpan `3`.
  - DU-066-8: Pengaturan Company default tab Transfer pada All categories: Require approval tersimpan `OFF`, Auto-approve tersimpan `ON`, Auto-approve when destination in same parent Group tersimpan `ON`, Approval type tersimpan `All approvers (AND)`, Approval scope tersimpan `Origin only`.
  - DU-066-9: Pengaturan Category leaf `Machinery` tab Borrow: Require approval bernilai sendiri tersimpan `ON`, Approval type bernilai sendiri tersimpan `All approvers (AND)`.
  - DU-066-10: Pengaturan Category leaf `Machinery` tab Borrow: Self service bernilai sendiri tersimpan `ON`, Duration unit bernilai sendiri tersimpan `Hours`.
  - DU-066-11: Pengaturan Company default tab Disposal pada All categories: Require approval tersimpan `ON`, Approval type tersimpan `All approvers (AND)`.
  - DU-066-12: Pengaturan Company default tab Borrow pada All categories: Self service tersimpan `ON`, Require approval tersimpan `ON`, Auto-approve tersimpan `ON`, Auto-approve when duration ≤ tersimpan `5`, Approval type tersimpan `All approvers (AND)`.
  - DU-066-13: Pengaturan Company default tab Assign pada All categories: Require approval tersimpan `ON`, Approval type tersimpan `All approvers (AND)`.
- Kondisi:
  - K1: node All categories terpilih, tab Borrow aktif, Approval Workflow tidak tersedia di plan, level Feature Suite Borrowing Full, tidak ada Approver ditugaskan untuk Borrow di Group mana pun, level Feature Suite Assignment bukan None, nilai memakai DU-066-1.
  - K2: node All categories terpilih, tab Borrow aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-2.
  - K3: node Category leaf `Machinery` terpilih, tab Borrow aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-3.
  - K4: node All categories terpilih, tab Transfer aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-4.
  - K5: node All categories terpilih, tab Borrow aktif, level Feature Suite Borrowing Basic, nilai memakai DU-066-5.
  - K6: node Category leaf `Machinery` terpilih, tab Borrow aktif, level Feature Suite Borrowing Basic, nilai memakai DU-066-6.
  - K7: node All categories terpilih, level Feature Suite Borrowing None dan Assignment None, tab Transfer aktif.
  - K8: node All categories terpilih, level Feature Suite Transfer None dan Disposal None, tab Borrow aktif.
  - K9: node All categories terpilih, tab Borrow aktif, Approval Workflow tersedia di plan, level Feature Suite Borrowing Full, nilai memakai DU-066-7.
  - K10: node All categories terpilih, tab Borrow aktif, Approval Workflow tersedia di plan, Require approval bernilai `ON`, tidak ada Approver ditugaskan untuk Borrow di Group mana pun.
  - K11: node All categories terpilih, tab Transfer aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-8.
  - K12: node All categories terpilih, tab Borrow aktif, level Feature Suite Borrowing Basic, Approval Workflow tersedia di plan, Approver ditugaskan untuk Borrow di Group, nilai memakai DU-066-5.
  - K13: node Category leaf `Machinery` terpilih, tab Borrow aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-9.
  - K14: node Category leaf `Machinery` terpilih, tab Borrow aktif, level Feature Suite Borrowing Basic, nilai memakai DU-066-10.
  - K15: node All categories terpilih, tab Disposal aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-11.
  - K16: node All categories terpilih, tab Borrow aktif, Approval Workflow tidak tersedia di plan, level Feature Suite Borrowing Full, nilai memakai DU-066-12.
  - K17: node All categories terpilih, tab Assign aktif, Approval Workflow tidak tersedia di plan, level Feature Suite Assignment bukan None, nilai memakai DU-066-13.

## Test Steps

### Approval Workflow tidak tersedia: alert dan field bergerbang
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil di bagian `Approval`
3. Verifikasi chip `Upgrade` tampil pada alert itu
4. Verifikasi alert `No one is assigned as Approver for this transaction in any Group. Approval goes to the Group Manager or Total Control.` tidak ada
5. Verifikasi kontrol `Require approval` tampil disabled dan nilai tersimpan `ON` dipertahankan
6. Verifikasi `Auto-approve` disabled dengan nilai tersimpan `ON`
7. Verifikasi `Auto-approve when duration ≤` disabled dengan nilai tersimpan `3`
8. Verifikasi `Approval type` disabled dengan nilai tersimpan `All approvers (AND)`
9. Arahkan kursor ke kontrol `Require approval` yang disabled
10. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada kontrol `Require approval` yang disabled
11. Klik kontrol `Require approval` yang disabled
12. Verifikasi `Require approval` tetap bernilai `ON` setelah diklik
13. Verifikasi `Max duration` bernilai `30` dan aktif
14. Verifikasi `Self service` bernilai `OFF` dan aktif
15. Klik tab `Assign`
16. Verifikasi alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil di bagian `Approval` pada tab `Assign`

### Field Approval bersyarat mengikuti nilai tersimpan induknya
17. Tampilkan Area utama dengan kondisi K2
18. Verifikasi `Auto-approve` disabled dengan nilai tersimpan `OFF`
19. Verifikasi field `Auto-approve when duration ≤` tidak dirender
20. Verifikasi `Approval type` disabled dengan nilai tersimpan `All approvers (AND)`

### Self service ON menyembunyikan Auto-approve when duration ≤
21. Tampilkan Area utama dengan kondisi K9
22. Verifikasi `Self service` bernilai `ON` pada level Feature Suite Borrowing Full
23. Verifikasi `Auto-approve when duration ≤` ikut tersembunyi saat `Self service` bernilai `ON`

### Field bergerbang Approval Workflow di Category
24. Tampilkan Area utama dengan kondisi K3
25. Verifikasi bagian `Approval` tampil pada Category leaf `Machinery`
26. Verifikasi tombol `Set own value` dan tombol `Reset to inherit` tidak ada pada `Require approval` dan `Approval type`

### Reset to Default tidak menyentuh field bergerbang Approval scope
27. Tampilkan Area utama dengan kondisi K4
28. Verifikasi tombol `Reset to Default` aktif untuk role berhak
29. Verifikasi `Approval scope` disabled dengan nilai tersimpan `Origin only`
30. Verifikasi `Auto-approve when destination in same parent Group` disabled dengan nilai tersimpan `ON`
31. Klik `Reset to Default`
32. Verifikasi `Approval scope` tetap bernilai `Origin only`
33. Verifikasi `In-transit overdue after` kembali ke nilai awal `7`

### Level Borrowing Basic menonaktifkan Self service dan Duration unit
34. Tampilkan Area utama dengan kondisi K5
35. Verifikasi kontrol `Duration unit` tampil disabled dan nilai tersimpan `Hours` dipertahankan
36. Verifikasi `Self service` disabled dengan nilai tersimpan `ON`
37. Arahkan kursor ke kontrol `Duration unit` yang disabled
38. Verifikasi alasan `Available on plans with full Borrowing.` tersampaikan pada kontrol `Duration unit` yang disabled
39. Arahkan kursor ke kontrol `Self service` yang disabled
40. Verifikasi alasan `Available on plans with full Borrowing.` tersampaikan pada kontrol `Self service` yang disabled
41. Verifikasi `Max duration` bernilai `30` dan aktif

### Level Borrowing Basic di Category
42. Tampilkan Area utama dengan kondisi K6
43. Verifikasi bagian `Limits` tampil pada Category leaf `Machinery`
44. Verifikasi tombol `Set own value` dan tombol `Reset to inherit` tidak ada pada `Self service` dan `Duration unit`

### Tab Borrow dan tab Assign tidak tampil pada level None
45. Tampilkan Area utama dengan kondisi K7
46. Verifikasi tab `Borrow` tidak tampil pada daftar tab
47. Verifikasi tab `Transfer` aktif
48. Buka langsung URL Transaction Settings dengan tab `Borrow`
49. Verifikasi tab `Borrow` tetap tidak tampil pada daftar tab
50. Verifikasi tab `Borrow` tidak menjadi tab aktif
51. Tampilkan Area utama dengan kondisi K7
52. Verifikasi tab `Transfer` tetap aktif
53. Verifikasi tab `Assign` tidak tampil pada daftar tab
54. Buka langsung URL Transaction Settings dengan tab `Assign`
55. Verifikasi tab `Assign` tetap tidak tampil pada daftar tab
56. Verifikasi tab `Assign` tidak menjadi tab aktif
57. Tampilkan Area utama dengan kondisi K7
58. Verifikasi tab `Transfer` tetap aktif

### Tab Transfer dan tab Disposal tidak tampil pada level None
59. Tampilkan Area utama dengan kondisi K8
60. Verifikasi tab `Transfer` tidak tampil pada daftar tab
61. Verifikasi tab `Borrow` aktif
62. Buka langsung URL Transaction Settings dengan tab `Transfer`
63. Verifikasi tab `Transfer` tetap tidak tampil pada daftar tab
64. Verifikasi tab `Transfer` tidak menjadi tab aktif
65. Tampilkan Area utama dengan kondisi K8
66. Verifikasi tab `Borrow` tetap aktif
67. Verifikasi tab `Disposal` tidak tampil pada daftar tab
68. Buka langsung URL Transaction Settings dengan tab `Disposal`
69. Verifikasi tab `Disposal` tetap tidak tampil pada daftar tab
70. Verifikasi tab `Disposal` tidak menjadi tab aktif

### Alert tidak ada Approver saat Approval Workflow tersedia
71. Tampilkan Area utama dengan kondisi K10
72. Verifikasi alert `No one is assigned as Approver for this transaction in any Group. Approval goes to the Group Manager or Total Control.` tampil dengan severity warning di bagian `Approval`

### Alert Approval Workflow bersifat info pada tab Borrow dan Assign
73. Tampilkan Area utama dengan kondisi K1
74. Verifikasi alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil dengan severity info di bagian `Approval` pada tab `Borrow`
75. Klik tab `Assign`
76. Verifikasi alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil dengan severity info di bagian `Approval` pada tab `Assign`

### Field Approval bergerbang pada tab Transfer dan Disposal
77. Tampilkan Area utama dengan kondisi K4
78. Verifikasi alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil dengan severity info di bagian `Approval` pada tab `Transfer`
79. Verifikasi `Require approval` disabled dengan nilai tersimpan `ON` pada tab `Transfer`
80. Verifikasi `Auto-approve` disabled dengan nilai tersimpan `ON` pada tab `Transfer`
81. Tampilkan Area utama dengan kondisi K15
82. Verifikasi alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil dengan severity info di bagian `Approval` pada tab `Disposal`
83. Verifikasi `Require approval` disabled dengan nilai tersimpan `ON` pada tab `Disposal`

### Require approval tersimpan OFF menyembunyikan field Approval saat bergerbang
84. Tampilkan Area utama dengan kondisi K11
85. Verifikasi `Require approval` disabled dengan nilai tersimpan `OFF` pada tab `Transfer`
86. Verifikasi `Auto-approve` tidak ada pada tab `Transfer`
87. Verifikasi `Auto-approve when destination in same parent Group` tidak ada pada tab `Transfer`
88. Verifikasi `Approval type` tidak ada pada tab `Transfer`

### Self service tersimpan ON pada level Borrowing Basic menyembunyikan field Approval tanpa alert
89. Tampilkan Area utama dengan kondisi K12
90. Verifikasi `Self service` tampil disabled dengan nilai tersimpan `ON` pada tab `Borrow`
91. Verifikasi `Require approval` tidak ada pada tab `Borrow`
92. Verifikasi `Auto-approve` tidak ada pada tab `Borrow`
93. Verifikasi `Approval type` tidak dirender pada tab `Borrow`
94. Verifikasi tidak ada alert pada tab `Borrow` akibat level Feature Suite Borrowing Basic

### Field Approval bernilai sendiri di Category saat Approval Workflow tidak tersedia
95. Tampilkan Area utama dengan kondisi K13
96. Verifikasi `Require approval` tampil disabled dengan nilai tersimpan `ON` pada Category leaf `Machinery`
97. Verifikasi `Approval type` tampil disabled dengan nilai tersimpan `All approvers (AND)` pada Category leaf `Machinery`
98. Verifikasi tombol `Set own value` dan tombol `Reset to inherit` tidak ada pada `Require approval` dan `Approval type`

### Self service dan Duration unit bernilai sendiri di Category saat level Borrowing Basic
99. Tampilkan Area utama dengan kondisi K14
100. Verifikasi `Self service` tampil disabled dengan nilai tersimpan `ON` pada Category leaf `Machinery`
101. Verifikasi `Duration unit` tampil disabled dengan nilai tersimpan `Hours` pada Category leaf `Machinery`
102. Verifikasi tombol `Set own value` dan tombol `Reset to inherit` tidak ada pada `Self service` dan `Duration unit`

### Self service tersimpan ON menyembunyikan field Approval saat Approval Workflow tidak tersedia
103. Tampilkan Area utama dengan kondisi K16
104. Verifikasi alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil di bagian `Approval`
105. Verifikasi `Self service` bernilai `ON` dan aktif
106. Verifikasi `Require approval` tidak ada
107. Verifikasi `Auto-approve` tidak ada
108. Verifikasi `Approval type` tidak ada
109. Verifikasi `Auto-approve when duration ≤` tidak ada

### Require approval dan Approval type tab Assign disabled saat Approval Workflow tidak tersedia
110. Tampilkan Area utama dengan kondisi K17
111. Verifikasi `Require approval` disabled dengan nilai tersimpan `ON` pada tab `Assign`
112. Verifikasi `Approval type` disabled dengan nilai tersimpan `All approvers (AND)` pada tab `Assign`

### Approval type tab Transfer disabled saat Approval Workflow tidak tersedia
113. Tampilkan Area utama dengan kondisi K4
114. Verifikasi `Approval type` disabled dengan nilai tersimpan `All approvers (AND)` pada tab `Transfer`

### Approval type tab Disposal disabled saat Approval Workflow tidak tersedia
115. Tampilkan Area utama dengan kondisi K15
116. Verifikasi `Approval type` disabled dengan nilai tersimpan `All approvers (AND)` pada tab `Disposal`
