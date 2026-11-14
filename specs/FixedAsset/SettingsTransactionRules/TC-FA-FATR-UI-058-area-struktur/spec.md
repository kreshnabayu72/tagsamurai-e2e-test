---
id: TC-FA-FATR-UI-058-area-struktur
title: "Area utama: struktur tab, bagian, dan baris field"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - §Aturan Logika Modul#r10
  - §Aturan Logika Modul#r66
  - §Aturan Logika Modul#r92
  - §Aturan Logika Modul#r93
  - §Aturan Logika Modul#r94
  - §Aturan Logika Modul#r95
  - §Aturan Logika Modul#r96
  - §Aturan Logika Modul#r97
  - §Aturan Logika Modul#r98
  - §Aturan Logika Modul#r99
  - §4.1#r2
  - §4.1#r3
  - §4.1#r26
  - §4.1#r27
  - §4.1#r28
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
  - §4.1#r44
  - §4.1#r45
  - §4.1#r52
  - §4.1#r53
  - §4.1#r203
  - §4.1#r213
  - §4.2#b2
  - §4.3#r1
  - §4.3#r3
  - §4.3#r4
  - §4.3#r16
  - §4.5#b2
  - AU-BAGIAN-asampaiAU-BAGIAN-o,AU-NILAI-asampaiAU-NILAI-j,AU-TOOLTIP-asampaiAU-TOOLTIP-d
  - §9.2#b193
  - §9.2#b194
  - §9.2#b195
  - §9.2#b196
  - §9.2#b202
  - §9.5#r4
  - §10#b3
smoke: []
dependsOn: []
trace:
  §Aturan Logika Modul#r10: [2, 24, 25, 58]
  §Aturan Logika Modul#r66: 58
  §Aturan Logika Modul#r92: [52, 55]
  §Aturan Logika Modul#r93: [52, 55]
  §Aturan Logika Modul#r94: [51, 54]
  §Aturan Logika Modul#r95: 54
  §Aturan Logika Modul#r96: [51, 73, 76, 79]
  §Aturan Logika Modul#r97: 41
  §Aturan Logika Modul#r98: 16
  §Aturan Logika Modul#r99: 17
  §4.1#r2: 4
  §4.1#r3: [16, 17, 18]
  §4.1#r26: [6, 8, 10, 12]
  §4.1#r27: [6, 8, 10, 13]
  §4.1#r28: 13
  §4.1#r29: [2, 41]
  §4.1#r30: [16, 17]
  §4.1#r31: 18
  §4.1#r32: 58
  §4.1#r33: 57
  §4.1#r34: [16, 27, 54]
  §4.1#r35: 34
  §4.1#r36: 31
  §4.1#r37: [44, 60]
  §4.1#r38: 30
  §4.1#r39: [42, 70]
  §4.1#r40: 43
  §4.1#r41: 45
  §4.1#r42: 45
  §4.1#r43: 47
  §4.1#r44: 19
  §4.1#r45: 42
  §4.1#r52: 36
  §4.1#r53: 38
  §4.1#r203: [22, 52]
  §4.1#r213: 24
  §4.2#b2: [2, 3, 40, 41, 65, 67]
  §4.3#r1: [29, 30]
  §4.3#r3: [57, 58]
  §4.3#r4: [51, 52, 54, 55, 73, 74, 76, 77, 79, 80]
  §4.3#r16: [2, 41]
  §4.5#b2: 34
  AU-BAGIAN-asampaiAU-BAGIAN-o,AU-NILAI-asampaiAU-NILAI-j,AU-TOOLTIP-asampaiAU-TOOLTIP-d: [35, 38, 49]
  §9.2#b193: 21
  §9.2#b194: [22, 51]
  §9.2#b195: [23, 52]
  §9.2#b196: 52
  §9.2#b202: 22
  §9.5#r4: 42
  §10#b3: [63, 84, 87, 90, 93]
anchor: [62, 69, 83, 86, 89, 92]
coverage:
  web: automated
---

# Area utama: struktur tab, bagian, dan baris field

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-058-1: Pengaturan Company default pada All categories: Duration unit `Days`, Max duration `14`, Max extensions `0`, Max assets per assignee (concurrent) `0`, Allowed disposal types `Write-off` dipilih lebih dulu lalu `Sell`, Long missing after `0`, Transaction timeout `7`, Change Cost Center with Group `Never`, Send email notifications `ON`.
  - DU-058-2: Pengaturan Category leaf `Machinery`: Max duration bernilai sendiri `21`, semua field lain Inherit.
- Kondisi:
  - K1: node All categories terpilih, semua tab transaksi tersedia di plan, nilai Company default memakai DU-058-1.
  - K2: node Category leaf `Machinery` terpilih, semua field Inherit, nilai Company default memakai DU-058-1.
  - K3: node Category leaf `Machinery` terpilih, Max duration pada tab Borrow bernilai sendiri sesuai DU-058-2.
  - K4: node All categories terpilih, level Feature Suite Borrowing None dan level Assignment, Transfer, serta Disposal tidak None, nilai Company default memakai DU-058-1.
  - K5: node All categories terpilih, level Feature Suite Borrowing None dan Assignment None, level Transfer dan Disposal tidak None, nilai Company default memakai DU-058-1.

## Test Steps

### Urutan tab dan tab awal di All categories
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi tab tampil berurutan `Borrow`, `Assign`, `Transfer`, `Disposal`, `Damaged & Missing`
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
34. Verifikasi teks bantuan label `Duration unit` tersampaikan
35. Verifikasi teks bantuan label `Duration unit` menjelaskan bahwa field itu menentukan satuan Max duration dan Auto-approve duration
36. Verifikasi teks bantuan label `Duration unit` berbahasa Inggris dan berupa satu kalimat ringkas
37. Pindahkan fokus keyboard ke bantuan label `Allowed borrower`
38. Verifikasi teks bantuan label `Allowed borrower` berupa satu kalimat yang menjelaskan fungsi field itu

### Teks Inherit pada Category
39. Tampilkan Area utama dengan kondisi K2
40. Verifikasi tab `Borrow`, `Assign`, `Transfer`, dan `Disposal` tampil
41. Verifikasi tab `Damaged & Missing` tidak ada
42. Verifikasi `Max duration` menampilkan `Inherit — 14 days (from Company default)`
43. Verifikasi sumber pada teks Inherit `Max duration` berisi `Company default`
44. Verifikasi tombol `Set own value` tampil pada baris `Max duration`
45. Verifikasi `Max extensions` menampilkan `Inherit — No extension (from Company default)`
46. Klik tab `Assign`
47. Verifikasi `Max assets per assignee (concurrent)` menampilkan `Inherit — Unlimited (from Company default)`
48. Klik tab `Disposal`
49. Verifikasi pada teks Inherit `Allowed disposal types`, `Sell` tampil sebelum `Write-off`

### Field khusus All categories pada Category
50. Tampilkan Area utama dengan kondisi K2
51. Verifikasi `Transaction timeout` menampilkan `Set in All categories: 7 days`
52. Verifikasi `Transaction timeout` tanpa kontrol, tanpa tombol `Set own value`, dan tanpa tombol `Reset to inherit`
53. Klik tab `Transfer`
54. Verifikasi `Change Cost Center with Group` menampilkan `Set in All categories: Never`
55. Verifikasi `Change Cost Center with Group` tanpa kontrol dan tanpa tombol `Set own value`

### Bagian Notifications pada Category
56. Tampilkan Area utama dengan kondisi K2
57. Verifikasi bagian `Notifications` menampilkan keterangan `Notification settings are set in All categories.`
58. Verifikasi bagian `Notifications` tidak memuat switch `Send email notifications` dan tidak memuat tombol `Set own value`

### Tombol Reset to inherit pada Category dengan nilai sendiri
59. Tampilkan Area utama dengan kondisi K3
60. Verifikasi `Max duration` bernilai `21` dengan tombol `Reset to inherit`

### Aturan tetap sistem
61. Tampilkan Area utama dengan kondisi K1
62. Verifikasi bagian `Eligibility` pada tab `Borrow` memuat field `Allow Borrow`
63. Verifikasi tidak ada kontrol untuk kelayakan status aset, kondisi aset, satu transaksi aktif per aset, hak role, scan tag, Handover Note PDF, atau dokumen wajib pada tab `Borrow`

### Tab awal mengikuti tab pertama yang tersedia
64. Tampilkan Area utama dengan kondisi K4
65. Verifikasi tab `Assign` aktif sebagai tab awal
66. Tampilkan Area utama dengan kondisi K5
67. Verifikasi tab `Transfer` aktif sebagai tab awal

### Baris Inherit tanpa kontrol input
68. Tampilkan Area utama dengan kondisi K2
69. Verifikasi tombol `Set own value` tampil pada baris `Max duration`
70. Verifikasi tidak ada kontrol input pada baris `Max duration`

### Transaction timeout di tab Assign, Transfer, dan Disposal pada Category
71. Tampilkan Area utama dengan kondisi K2
72. Klik tab `Assign`
73. Verifikasi `Transaction timeout` menampilkan `Set in All categories: 7 days`
74. Verifikasi `Transaction timeout` tanpa kontrol, tanpa tombol `Set own value`, dan tanpa tombol `Reset to inherit`
75. Klik tab `Transfer`
76. Verifikasi `Transaction timeout` menampilkan `Set in All categories: 7 days`
77. Verifikasi `Transaction timeout` tanpa kontrol, tanpa tombol `Set own value`, dan tanpa tombol `Reset to inherit`
78. Klik tab `Disposal`
79. Verifikasi `Transaction timeout` menampilkan `Set in All categories: 7 days`
80. Verifikasi `Transaction timeout` tanpa kontrol, tanpa tombol `Set own value`, dan tanpa tombol `Reset to inherit`

### Aturan tetap sistem pada tab transaksi lain
81. Tampilkan Area utama dengan kondisi K1
82. Klik tab `Assign`
83. Verifikasi bagian `Eligibility` pada tab `Assign` memuat field `Allow Assign`
84. Verifikasi tidak ada kontrol untuk kelayakan status aset, kondisi aset, satu transaksi aktif per aset, hak role, scan tag, Handover Note PDF, atau dokumen wajib pada tab `Assign`
85. Klik tab `Transfer`
86. Verifikasi bagian `Eligibility` pada tab `Transfer` memuat field `Allow Transfer`
87. Verifikasi tidak ada kontrol untuk kelayakan status aset, kondisi aset, satu transaksi aktif per aset, hak role, scan tag, Handover Note PDF, atau dokumen wajib pada tab `Transfer`
88. Klik tab `Disposal`
89. Verifikasi bagian `Eligibility` pada tab `Disposal` memuat field `Allow Disposal`
90. Verifikasi tidak ada kontrol untuk kelayakan status aset, kondisi aset, satu transaksi aktif per aset, hak role, scan tag, Handover Note PDF, atau dokumen wajib pada tab `Disposal`
91. Klik tab `Damaged & Missing`
92. Verifikasi bagian `Limits` pada tab `Damaged & Missing` memuat field `Long missing after`
93. Verifikasi tidak ada kontrol untuk kelayakan status aset, kondisi aset, satu transaksi aktif per aset, hak role, scan tag, Handover Note PDF, atau dokumen wajib pada tab `Damaged & Missing`
