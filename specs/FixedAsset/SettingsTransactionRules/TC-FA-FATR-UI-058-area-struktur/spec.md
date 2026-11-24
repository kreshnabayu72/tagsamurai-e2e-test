---
id: TC-FA-FATR-UI-058-area-struktur
title: "Area utama: struktur tab, bagian, dan baris field"
layer: ui-client
priority: High
caseType: Positive
status: ready-for-automation
sourceRules:
  - §Aturan Logika Modul#r10
  - §Aturan Logika Modul#r68
  - §Aturan Logika Modul#r94
  - §Aturan Logika Modul#r95
  - §Aturan Logika Modul#r96
  - §Aturan Logika Modul#r97
  - §Aturan Logika Modul#r98
  - §Aturan Logika Modul#r99
  - §Aturan Logika Modul#r100
  - §Aturan Logika Modul#r101
  - §4.1#r2
  - §4.1#r3
  - §4.1#r29
  - §4.1#r30
  - §4.1#r31
  - §4.1#r32
  - §4.1#r33
  - §4.1#r34
  - §4.1#r35
  - §4.1#r36
  - §4.1#r37
  - §4.1#r38
  - §4.1#r39
  - §4.1#r40
  - §4.1#r41
  - §4.1#r42
  - §4.1#r43
  - §4.1#r48
  - §4.1#r49
  - §4.1#r50
  - §4.1#r52
  - §4.1#r61
  - §4.1#r212
  - §4.1#r222
  - §4.2#b2
  - §4.3#r1
  - §4.3#r3
  - §4.3#r4
  - §4.3#r15
  - §4.5#b2
  - AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f
  - §9.2#b193
  - §9.2#b194
  - §9.2#b195
  - §9.2#b196
  - §9.2#b202
  - §9.5#r4
  - §10#b3
  - §9.5#r11
  - §9.2#b355
smoke: []
dependsOn: []
trace:
  §Aturan Logika Modul#r10: [2, 24, 25, 55]
  §Aturan Logika Modul#r68: 55
  §Aturan Logika Modul#r94: [49, 52]
  §Aturan Logika Modul#r95: [49, 52]
  §Aturan Logika Modul#r96: [48, 51]
  §Aturan Logika Modul#r97: 51
  §Aturan Logika Modul#r98: [48, 70, 73, 76]
  §Aturan Logika Modul#r99: 38
  §Aturan Logika Modul#r100: [16, 19]
  §Aturan Logika Modul#r101: 17
  §4.1#r2: 4
  §4.1#r3: [16, 17, 18]
  §4.1#r29: [6, 8, 10, 12]
  §4.1#r30: [6, 8, 10, 13]
  §4.1#r31: 13
  §4.1#r32: [2, 38]
  §4.1#r33: [16, 17]
  §4.1#r34: 18
  §4.1#r35: 55
  §4.1#r36: 54
  §4.1#r37: [16, 27, 51]
  §4.1#r38: 34
  §4.1#r39: 31
  §4.1#r40: [41, 57]
  §4.1#r41: 30
  §4.1#r42: [39, 67]
  §4.1#r43: 40
  §4.1#r48: 42
  §4.1#r49: 42
  §4.1#r50: 44
  §4.1#r52: 39
  §4.1#r61: 35
  §4.1#r212: [22, 49]
  §4.1#r222: 24
  §4.2#b2: [2, 3, 37, 38, 62, 64, 92, 93, 95]
  §4.3#r1: [29, 30]
  §4.3#r3: [54, 55]
  §4.3#r4: [48, 49, 51, 52, 70, 71, 73, 74, 76, 77]
  §4.3#r15: [2, 38]
  §4.5#b2: 34
  AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f: [34, 35, 46]
  §9.2#b193: 21
  §9.2#b194: [22, 48]
  §9.2#b195: [23, 49]
  §9.2#b196: 49
  §9.2#b202: 22
  §9.5#r4: 39
  §10#b3: [60, 81, 84, 87, 90]
  §9.5#r11: [62, 64]
  §9.2#b355: [42, 44]
anchor: [59, 66, 80, 83, 86, 89]
coverage:
  web: automated
---

# Area utama: struktur tab, bagian, dan baris field

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-058-1: Pengaturan Company default pada All categories: Duration unit `Days`, Max duration `14`, Max extensions `0`, Max assets per assignee (concurrent) `0`, Allowed disposal types `Trade-in` dipilih lebih dulu lalu `Sell`, Long missing after `0`, Transaction timeout `7`, Change Cost Center with Group `Never`, Send email notifications `ON`, Allowed borrower `Employee in any Group`.
  - DU-058-2: Pengaturan Category leaf `Machinery`: Max duration bernilai sendiri `21`, semua field lain Inherit.
- Kondisi:
  - K1: node All categories terpilih, semua tab transaksi tersedia di plan, addon Audit dan addon Maintenance aktif, nilai Company default memakai DU-058-1.
  - K2: node Category leaf `Machinery` terpilih, semua field Inherit, nilai Company default memakai DU-058-1.
  - K3: node Category leaf `Machinery` terpilih, Max duration pada tab Borrow bernilai sendiri sesuai DU-058-2.
  - K4: node All categories terpilih, level Feature Suite Borrowing None dan level Assignment, Transfer, serta Disposal tidak None, nilai Company default memakai DU-058-1.
  - K5: node All categories terpilih, level Feature Suite Borrowing None dan Assignment None, level Transfer dan Disposal tidak None, nilai Company default memakai DU-058-1.
  - K6: node All categories terpilih, level Feature Suite Borrowing, Assignment, Transfer, dan Disposal None, addon Audit dan addon Maintenance tidak aktif, nilai Company default memakai DU-058-1.
  - K7: node Category leaf `Machinery` terpilih, level Feature Suite Borrowing, Assignment, Transfer, dan Disposal None, addon Audit tidak aktif dan addon Maintenance aktif, semua field Inherit, nilai Company default memakai DU-058-1.

## Test Steps

### Urutan tab dan tab awal di All categories
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi tab tampil berurutan `Borrow`, `Assign`, `Transfer`, `Disposal`, `Damaged & Missing`, `Audit`, `Maintenance`, `Geolocation`
3. Verifikasi tab `Borrow` aktif sebagai tab awal
4. Verifikasi tab `Borrow` memuat bagian `Overrides`, tombol `Reset to Default`, dan tombol `Save`

### Bagian tiap transaksi di All categories
5. Tampilkan Area utama dengan kondisi K1
6. Verifikasi tab `Borrow` memuat bagian `Eligibility`, `Limits`, `Evidence`, `Approval`, `Reminders`, dan `Notifications`
7. Klik tab `Assign`
8. Verifikasi tab `Assign` memuat bagian `Eligibility`, `Limits`, `Evidence`, `Approval`, `Reminders`, dan `Notifications`
9. Klik tab `Transfer`
10. Verifikasi tab `Transfer` memuat bagian `Eligibility`, `Limits`, `Evidence`, `Approval`, `Reminders`, dan `Notifications`
11. Klik tab `Disposal`
12. Verifikasi tab `Disposal` memuat bagian `Eligibility`, `Limits`, `Approval`, `Reminders`, dan `Notifications`
13. Verifikasi bagian `Evidence` tidak ada pada tab `Disposal`

### Tab Damaged & Missing di All categories
14. Tampilkan Area utama dengan kondisi K1
15. Klik tab `Damaged & Missing`
16. Verifikasi tab `Damaged & Missing` memuat bagian `Limits` dengan field `Long missing after`
17. Verifikasi tab `Damaged & Missing` memuat bagian `Evidence` dengan field `After photo required`
18. Verifikasi tab `Damaged & Missing` tidak memuat bagian `Eligibility`, `Approval`, `Reminders`, `Notifications`, dan `Overrides`
19. Verifikasi `Long missing after` bernilai `0` tampil sebagai kontrol bernilai sendiri tanpa teks `Inherit`

### Field khusus All categories di All categories
20. Tampilkan Area utama dengan kondisi K1
21. Verifikasi tab `Borrow` memuat satu field `Transaction timeout` pada bagian `Reminders`
22. Verifikasi `Transaction timeout` tampil sebagai kontrol bernilai sendiri `7`
23. Verifikasi `Transaction timeout` tanpa tombol `Set own value` dan tanpa tombol `Reset to inherit`
24. Verifikasi `Send email notifications` pada bagian `Notifications` tampil sebagai switch bernilai `ON`
25. Verifikasi `Send email notifications` tanpa tombol `Set own value` dan tanpa tombol `Reset to inherit`
26. Klik tab `Transfer`
27. Verifikasi `Change Cost Center with Group` bernilai `Never` tampil sebagai kontrol bernilai sendiri tanpa tombol `Set own value` dan tanpa tombol `Reset to inherit`

### Company default tanpa Inherit
28. Tampilkan Area utama dengan kondisi K1
29. Verifikasi `Max duration` tampil sebagai kontrol bernilai sendiri `14`
30. Verifikasi tombol `Set own value` dan tombol `Reset to inherit` tidak ada pada baris field mana pun di bagian `Limits`
31. Verifikasi setiap baris field di bagian `Limits` memuat satu kontrol bernilai sendiri

### Teks bantuan label field
32. Tampilkan Area utama dengan kondisi K1
33. Pindahkan fokus keyboard ke bantuan label `Duration unit`
34. Verifikasi teks bantuan label `Duration unit` tersampaikan berbunyi `Unit used for Max duration and Auto-approve when duration ≤.`
35. Verifikasi teks bantuan label `Duration unit` berbahasa Inggris dan berupa satu kalimat ringkas

### Teks Inherit pada Category
36. Tampilkan Area utama dengan kondisi K2
37. Verifikasi tab `Borrow`, `Assign`, `Transfer`, dan `Disposal` tampil
38. Verifikasi tab `Damaged & Missing` tidak ada
39. Verifikasi `Max duration` menampilkan `Inherit — 14 days (from Company default)`
40. Verifikasi sumber pada teks Inherit `Max duration` berisi `Company default`
41. Verifikasi tombol `Set own value` tampil pada baris `Max duration`
42. Verifikasi `Max extensions` menampilkan `Inherit — No extension (from Company default)`
43. Klik tab `Assign`
44. Verifikasi `Max assets per assignee (concurrent)` menampilkan `Inherit — Unlimited (from Company default)`
45. Klik tab `Disposal`
46. Verifikasi pada teks Inherit `Allowed disposal types`, `Sell` tampil sebelum `Trade-in`

### Field khusus All categories pada Category
47. Tampilkan Area utama dengan kondisi K2
48. Verifikasi `Transaction timeout` menampilkan `Set in All categories: 7 days`
49. Verifikasi `Transaction timeout` tanpa kontrol, tanpa tombol `Set own value`, dan tanpa tombol `Reset to inherit`
50. Klik tab `Transfer`
51. Verifikasi `Change Cost Center with Group` menampilkan `Set in All categories: Never`
52. Verifikasi `Change Cost Center with Group` tanpa kontrol dan tanpa tombol `Set own value`

### Bagian Notifications pada Category
53. Tampilkan Area utama dengan kondisi K2
54. Verifikasi bagian `Notifications` menampilkan keterangan `Notification settings are set in All categories.`
55. Verifikasi bagian `Notifications` tidak memuat switch `Send email notifications` dan tidak memuat tombol `Set own value`

### Tombol Reset to inherit pada Category dengan nilai sendiri
56. Tampilkan Area utama dengan kondisi K3
57. Verifikasi `Max duration` bernilai `21` dengan tombol `Reset to inherit`

### Aturan tetap sistem
58. Tampilkan Area utama dengan kondisi K1
59. Verifikasi bagian `Eligibility` pada tab `Borrow` memuat field `Allow Borrow`
60. Verifikasi tidak ada kontrol untuk kelayakan status aset, kondisi aset, satu transaksi aktif per aset, hak role, scan tag, Handover Note PDF, atau dokumen wajib pada tab `Borrow`

### Tab awal mengikuti tab pertama yang tersedia
61. Tampilkan Area utama dengan kondisi K4
62. Verifikasi tab `Assign` aktif sebagai tab awal
63. Tampilkan Area utama dengan kondisi K5
64. Verifikasi tab `Transfer` aktif sebagai tab awal

### Baris Inherit tanpa kontrol input
65. Tampilkan Area utama dengan kondisi K2
66. Verifikasi tombol `Set own value` tampil pada baris `Max duration`
67. Verifikasi tidak ada kontrol input pada baris `Max duration`

### Transaction timeout di tab Assign, Transfer, dan Disposal pada Category
68. Tampilkan Area utama dengan kondisi K2
69. Klik tab `Assign`
70. Verifikasi `Transaction timeout` menampilkan `Set in All categories: 7 days`
71. Verifikasi `Transaction timeout` tanpa kontrol, tanpa tombol `Set own value`, dan tanpa tombol `Reset to inherit`
72. Klik tab `Transfer`
73. Verifikasi `Transaction timeout` menampilkan `Set in All categories: 7 days`
74. Verifikasi `Transaction timeout` tanpa kontrol, tanpa tombol `Set own value`, dan tanpa tombol `Reset to inherit`
75. Klik tab `Disposal`
76. Verifikasi `Transaction timeout` menampilkan `Set in All categories: 7 days`
77. Verifikasi `Transaction timeout` tanpa kontrol, tanpa tombol `Set own value`, dan tanpa tombol `Reset to inherit`

### Aturan tetap sistem pada tab transaksi lain
78. Tampilkan Area utama dengan kondisi K1
79. Klik tab `Assign`
80. Verifikasi bagian `Eligibility` pada tab `Assign` memuat field `Allow Assign`
81. Verifikasi tidak ada kontrol untuk kelayakan status aset, kondisi aset, satu transaksi aktif per aset, hak role, scan tag, Handover Note PDF, atau dokumen wajib pada tab `Assign`
82. Klik tab `Transfer`
83. Verifikasi bagian `Eligibility` pada tab `Transfer` memuat field `Allow Transfer`
84. Verifikasi tidak ada kontrol untuk kelayakan status aset, kondisi aset, satu transaksi aktif per aset, hak role, scan tag, Handover Note PDF, atau dokumen wajib pada tab `Transfer`
85. Klik tab `Disposal`
86. Verifikasi bagian `Eligibility` pada tab `Disposal` memuat field `Allow Disposal`
87. Verifikasi tidak ada kontrol untuk kelayakan status aset, kondisi aset, satu transaksi aktif per aset, hak role, scan tag, Handover Note PDF, atau dokumen wajib pada tab `Disposal`
88. Klik tab `Damaged & Missing`
89. Verifikasi bagian `Limits` pada tab `Damaged & Missing` memuat field `Long missing after`
90. Verifikasi tidak ada kontrol untuk kelayakan status aset, kondisi aset, satu transaksi aktif per aset, hak role, scan tag, Handover Note PDF, atau dokumen wajib pada tab `Damaged & Missing`

### Tab awal bila tab transaksi dan tab addon tidak tersedia
91. Tampilkan Area utama dengan kondisi K6
92. Verifikasi tab `Damaged & Missing` aktif sebagai tab awal
93. Verifikasi tab `Geolocation` tidak ada di daftar tab
94. Tampilkan Area utama dengan kondisi K7
95. Verifikasi tab `Maintenance` aktif sebagai tab awal
