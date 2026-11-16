---
id: TC-FA-FATR-UI-066-area-plan
title: "Area utama: tampilan field dan tab bergerbang plan"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules:
  - §Aturan Logika Modul#r75
  - §Aturan Logika Modul#r76
  - §Aturan Logika Modul#r77
  - §Aturan Logika Modul#r79
  - §Aturan Logika Modul#r83
  - §Aturan Logika Modul#r86
  - §Aturan Logika Modul#r88
  - §Aturan Logika Modul#r90
  - §Aturan Logika Modul#r103
  - §Aturan Logika Modul#r105
  - §Aturan Logika Modul#r106
  - §Aturan Logika Modul#r108
  - §Aturan Logika Modul#r110
  - §4.1#r54
  - §4.1#r229
  - §4.3#r12
  - §4.3#r13
  - §4.3#r14
  - §4.3#r15
  - §4.3#r19
  - §4.3#r29
  - §4.3#r30
  - §4.3#r31
  - §4.3#r32
  - §4.3#r33
  - §4.3#p2
  - §7#r20
  - §7#r21
  - §9.2#b2
  - §9.2#b4
  - §9.4.2#r16
  - §9.4.2#r91
  - §9.4.4#r2
  - §9.4.4#r20
  - §9.10.1#b3
  - §9.10.1#b6
  - §9.10.1#p11
  - §9.10.1#p13
  - §9.10.2#b3
  - §9.10.3#b3
  - §9.10.4#b1
smoke: []
dependsOn: []
trace:
  §Aturan Logika Modul#r75: [5, 6, 7, 8, 29, 30, 88, 89, 92]
  §Aturan Logika Modul#r76: 14
  §Aturan Logika Modul#r77: [5, 6, 7, 8, 29]
  §Aturan Logika Modul#r79: 13
  §Aturan Logika Modul#r83: [35, 36]
  §Aturan Logika Modul#r86: [35, 36]
  §Aturan Logika Modul#r88: 41
  §Aturan Logika Modul#r90: [55, 61]
  §Aturan Logika Modul#r103: 46
  §Aturan Logika Modul#r105: 49
  §Aturan Logika Modul#r106: 46
  §Aturan Logika Modul#r108: 50
  §Aturan Logika Modul#r110: [62, 67]
  §4.1#r54: [10, 38, 40, 48]
  §4.1#r229: 32
  §4.3#r12: [35, 36, 38, 40, 44, 103, 116, 117, 118]
  §4.3#r13: [46, 48, 53, 106, 109, 110]
  §4.3#r14: [55, 57, 58, 62, 64, 65]
  §4.3#r15: [69, 71, 72, 75, 76, 78, 79]
  §4.3#r19: [28, 32]
  §4.3#r29: 10
  §4.3#r30: [26, 114]
  §4.3#r31: [5, 6, 7, 8]
  §4.3#r32: [3, 83, 85]
  §4.3#r33: [18, 19]
  §4.3#p2: [19, 20, 22, 23, 95, 96, 97, 100, 101, 102]
  §7#r20: [2, 16, 83, 85, 87, 91]
  §7#r21: 81
  §9.2#b2: [55, 60, 61, 67]
  §9.2#b4: [32, 33]
  §9.4.2#r16: [55, 57, 58, 62, 64, 65]
  §9.4.2#r91: 12
  §9.4.4#r2: [55, 62]
  §9.4.4#r20: 12
  §9.10.1#b3: 5
  §9.10.1#b6: 4
  §9.10.1#p11: 5
  §9.10.1#p13: 4
  §9.10.2#b3: [35, 36]
  §9.10.3#b3: 46
  §9.10.4#b1: [69, 71, 72, 74, 75, 76, 78, 79]
anchor: [25, 43, 52, 94, 99, 105, 108, 112, 113]
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
  - DU-066-3: Pengaturan Category leaf `Machinery` tab Borrow: semua field Inherit.
  - DU-066-4: Pengaturan Company default tab Transfer pada All categories: Require approval tersimpan `ON`, Auto-approve when destination in same parent Group tersimpan `ON`, Approval scope tersimpan `Origin only`, Auto-approve tersimpan `ON`, In-transit overdue after `10`.
  - DU-066-5: Pengaturan Company default tab Borrow pada All categories: Duration unit tersimpan `Hours`, Self service tersimpan `ON`, Max duration `30`.
  - DU-066-6: Pengaturan Category leaf `Machinery` tab Borrow: semua field Inherit.
  - DU-066-7: Pengaturan Company default tab Assign pada All categories: Direct handover between holders tersimpan `Deny`, Allowed assignee: Division `ON`, Max assets per assignee (concurrent) `5`.
  - DU-066-9: Pengaturan Company default tab Borrow pada All categories: Self service `ON`, Auto-approve tersimpan `ON`, Auto-approve when duration ≤ tersimpan `3`.
  - DU-066-8: Pengaturan Category leaf `Machinery` tab Assign: semua field Inherit.
  - DU-066-10: Pengaturan Company default tab Transfer pada All categories: Require approval tersimpan `OFF`, Auto-approve tersimpan `ON`, Auto-approve when destination in same parent Group tersimpan `ON`, Approval type tersimpan `All approvers (AND)`, Approval scope tersimpan `Origin only`.
  - DU-066-11: Pengaturan Category leaf `Machinery` tab Assign: Direct handover between holders bernilai sendiri tersimpan `Deny`.
  - DU-066-12: Pengaturan Category leaf `Machinery` tab Borrow: Require approval bernilai sendiri tersimpan `ON`, Approval type bernilai sendiri tersimpan `All approvers (AND)`.
  - DU-066-14: Pengaturan Category leaf `Machinery` tab Borrow: Self service bernilai sendiri tersimpan `ON`, Duration unit bernilai sendiri tersimpan `Hours`.
  - DU-066-13: Pengaturan Company default tab Disposal pada All categories: Require approval tersimpan `ON`.
- Kondisi:
  - K1: node All categories terpilih, tab Borrow aktif, Approval Workflow tidak tersedia di plan, level Feature Suite Borrowing Full, tidak ada Approver ditugaskan untuk Borrow di Group mana pun, nilai memakai DU-066-1.
  - K2: node All categories terpilih, tab Borrow aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-2.
  - K3: node Category leaf `Machinery` terpilih, tab Borrow aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-3.
  - K4: node All categories terpilih, tab Transfer aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-4.
  - K5: node All categories terpilih, tab Borrow aktif, level Feature Suite Borrowing Basic, nilai memakai DU-066-5.
  - K6: node Category leaf `Machinery` terpilih, tab Borrow aktif, level Feature Suite Borrowing Basic, nilai memakai DU-066-6.
  - K7: node All categories terpilih, tab Assign aktif, level Feature Suite Assignment Basic, nilai memakai DU-066-7.
  - K8: node Category leaf `Machinery` terpilih, tab Assign aktif, level Feature Suite Assignment Basic, nilai memakai DU-066-8.
  - K9: node All categories terpilih, level Feature Suite Borrowing None dan Assignment None, tab Transfer aktif.
  - K10: node All categories terpilih, level Feature Suite Transfer None dan Disposal None, tab Borrow aktif.
  - K12: node All categories terpilih, tab Borrow aktif, Approval Workflow tersedia di plan, level Feature Suite Borrowing Full, nilai memakai DU-066-9.
  - K11: node All categories terpilih, tab Borrow aktif, Approval Workflow tersedia di plan, Require approval bernilai `ON`, tidak ada Approver ditugaskan untuk Borrow di Group mana pun.
  - K13: node All categories terpilih, tab Transfer aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-10.
  - K14: node All categories terpilih, tab Borrow aktif, level Feature Suite Borrowing Basic, Approval Workflow tersedia di plan, Approver ditugaskan untuk Borrow di Group, nilai memakai DU-066-5.
  - K15: node All categories terpilih, tab Assign aktif, level Feature Suite Assignment Basic, Approval Workflow tersedia di plan, Approver ditugaskan untuk Assign di Group, nilai memakai DU-066-7.
  - K16: node Category leaf `Machinery` terpilih, tab Assign aktif, level Feature Suite Assignment Basic, nilai memakai DU-066-11.
  - K17: node Category leaf `Machinery` terpilih, tab Borrow aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-12.
  - K18: node Category leaf `Machinery` terpilih, tab Borrow aktif, level Feature Suite Borrowing Basic, nilai memakai DU-066-14.
  - K18: node All categories terpilih, tab Disposal aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-066-13.

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
10. Verifikasi alasan `Requires Approval Workflow on your plan` tersampaikan pada kontrol `Require approval` yang disabled
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
21. Tampilkan Area utama dengan kondisi K12
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
38. Verifikasi alasan `Available on plans with full Borrowing` tersampaikan pada kontrol `Duration unit` yang disabled
39. Arahkan kursor ke kontrol `Self service` yang disabled
40. Verifikasi alasan `Available on plans with full Borrowing` tersampaikan pada kontrol `Self service` yang disabled
41. Verifikasi `Max duration` bernilai `30` dan aktif

### Level Borrowing Basic di Category
42. Tampilkan Area utama dengan kondisi K6
43. Verifikasi bagian `Limits` tampil pada Category leaf `Machinery`
44. Verifikasi tombol `Set own value` dan tombol `Reset to inherit` tidak ada pada `Self service` dan `Duration unit`

### Level Assignment Basic menonaktifkan Direct handover between holders
45. Tampilkan Area utama dengan kondisi K7
46. Verifikasi kontrol `Direct handover between holders` tampil disabled dan nilai tersimpan `Deny` dipertahankan
47. Arahkan kursor ke kontrol `Direct handover between holders` yang disabled
48. Verifikasi alasan `Available on plans with full Assignment` tersampaikan pada kontrol `Direct handover between holders` yang disabled
49. Verifikasi `Allowed assignee: Division` bernilai `ON` dan aktif
50. Verifikasi `Max assets per assignee (concurrent)` bernilai `5` dan aktif

### Level Assignment Basic di Category
51. Tampilkan Area utama dengan kondisi K8
52. Verifikasi bagian `Limits` tampil pada Category leaf `Machinery`
53. Verifikasi tombol `Set own value` dan tombol `Reset to inherit` tidak ada pada `Direct handover between holders`

### Tab Borrow dan Assign tidak dapat dibuka pada level None
54. Tampilkan Area utama dengan kondisi K9
55. Verifikasi tab `Borrow` disabled
56. Arahkan kursor ke tab `Borrow` yang disabled
57. Verifikasi alasan `Not available on your current plan` tersampaikan pada tab `Borrow` yang disabled
58. Verifikasi chip `Upgrade` tampil pada tab `Borrow`
59. Klik tab `Borrow`
60. Verifikasi tab `Transfer` tetap aktif
61. Verifikasi tab `Borrow` tidak aktif
62. Verifikasi tab `Assign` disabled
63. Arahkan kursor ke tab `Assign` yang disabled
64. Verifikasi alasan `Not available on your current plan` tersampaikan pada tab `Assign` yang disabled
65. Verifikasi chip `Upgrade` tampil pada tab `Assign`
66. Klik tab `Assign`
67. Verifikasi tab `Assign` tidak aktif

### Tab Transfer dan Disposal tidak dapat dibuka pada level None
68. Tampilkan Area utama dengan kondisi K10
69. Verifikasi tab `Transfer` disabled
70. Arahkan kursor ke tab `Transfer` yang disabled
71. Verifikasi alasan `Not available on your current plan` tersampaikan pada tab `Transfer` yang disabled
72. Verifikasi chip `Upgrade` tampil pada tab `Transfer`
73. Klik tab `Transfer`
74. Verifikasi tab `Borrow` tetap aktif
75. Verifikasi tab `Transfer` tidak aktif
76. Verifikasi tab `Disposal` disabled
77. Arahkan kursor ke tab `Disposal` yang disabled
78. Verifikasi alasan `Not available on your current plan` tersampaikan pada tab `Disposal` yang disabled
79. Verifikasi chip `Upgrade` tampil pada tab `Disposal`

### Alert tidak ada Approver saat Approval Workflow tersedia
80. Tampilkan Area utama dengan kondisi K11
81. Verifikasi alert `No one is assigned as Approver for this transaction in any Group. Approval goes to the Group Manager or Total Control.` tampil di bagian `Approval`

### Alert Approval Workflow bersifat info pada tab Borrow dan Assign
82. Tampilkan Area utama dengan kondisi K1
83. Verifikasi alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil dengan severity info di bagian `Approval` pada tab `Borrow`
84. Klik tab `Assign`
85. Verifikasi alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil dengan severity info di bagian `Approval` pada tab `Assign`

### Field Approval bergerbang pada tab Transfer dan Disposal
86. Tampilkan Area utama dengan kondisi K4
87. Verifikasi alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil dengan severity info di bagian `Approval` pada tab `Transfer`
88. Verifikasi `Require approval` disabled dengan nilai tersimpan `ON` pada tab `Transfer`
89. Verifikasi `Auto-approve` disabled dengan nilai tersimpan `ON` pada tab `Transfer`
90. Tampilkan Area utama dengan kondisi K18
91. Verifikasi alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil dengan severity info di bagian `Approval` pada tab `Disposal`
92. Verifikasi `Require approval` disabled dengan nilai tersimpan `ON` pada tab `Disposal`

### Require approval tersimpan OFF menyembunyikan field Approval saat bergerbang
93. Tampilkan Area utama dengan kondisi K13
94. Verifikasi `Require approval` disabled dengan nilai tersimpan `OFF` pada tab `Transfer`
95. Verifikasi `Auto-approve` tidak ada pada tab `Transfer`
96. Verifikasi `Auto-approve when destination in same parent Group` tidak ada pada tab `Transfer`
97. Verifikasi `Approval type` tidak ada pada tab `Transfer`

### Self service tersimpan ON pada level Borrowing Basic menyembunyikan field Approval tanpa alert
98. Tampilkan Area utama dengan kondisi K14
99. Verifikasi `Self service` tampil disabled dengan nilai tersimpan `ON` pada tab `Borrow`
100. Verifikasi `Require approval` tidak ada pada tab `Borrow`
101. Verifikasi `Auto-approve` tidak ada pada tab `Borrow`
102. Verifikasi `Approval type` tidak dirender pada tab `Borrow`
103. Verifikasi tidak ada alert pada tab `Borrow` akibat level Feature Suite Borrowing Basic

### Level Assignment Basic tanpa alert pada tab Assign
104. Tampilkan Area utama dengan kondisi K15
105. Verifikasi `Direct handover between holders` tampil disabled dengan nilai tersimpan `Deny` pada tab `Assign`
106. Verifikasi tidak ada alert pada tab `Assign` akibat level Feature Suite Assignment Basic

### Direct handover between holders bernilai sendiri di Category saat level Assignment Basic
107. Tampilkan Area utama dengan kondisi K16
108. Verifikasi `Direct handover between holders` tampil disabled dengan nilai tersimpan `Deny` pada Category leaf `Machinery`
109. Verifikasi tombol `Set own value` tidak ada pada `Direct handover between holders`
110. Verifikasi tombol `Reset to inherit` tidak ada pada `Direct handover between holders`

### Field Approval bernilai sendiri di Category saat Approval Workflow tidak tersedia
111. Tampilkan Area utama dengan kondisi K17
112. Verifikasi `Require approval` tampil disabled dengan nilai tersimpan `ON` pada Category leaf `Machinery`
113. Verifikasi `Approval type` tampil disabled dengan nilai tersimpan `All approvers (AND)` pada Category leaf `Machinery`
114. Verifikasi tombol `Set own value` dan tombol `Reset to inherit` tidak ada pada `Require approval` dan `Approval type`

### Self service dan Duration unit bernilai sendiri di Category saat level Borrowing Basic
115. Tampilkan Area utama dengan kondisi K18
116. Verifikasi `Self service` tampil disabled dengan nilai tersimpan `ON` pada Category leaf `Machinery`
117. Verifikasi `Duration unit` tampil disabled dengan nilai tersimpan `Hours` pada Category leaf `Machinery`
118. Verifikasi tombol `Set own value` dan tombol `Reset to inherit` tidak ada pada `Self service` dan `Duration unit`
