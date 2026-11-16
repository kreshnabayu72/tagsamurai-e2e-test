---
id: TC-FA-FATR-UI-059-area-borrow
title: "Area utama: field tab Borrow"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules:
  - §4.1#r55
  - §4.1#r56
  - §4.1#r57
  - §4.1#r58
  - §4.1#r59
  - §4.1#r60
  - §4.1#r61
  - §4.1#r87
  - §4.1#r161
  - §4.1#r163
  - §4.1#r179
  - §4.1#r184
  - §4.1#r180
  - §4.1#r182
  - §4.1#r181
  - §4.1#r200
  - §4.1#r201
  - §4.1#r212
  - §9.2#b400
  - §9.2#b424
  - §9.4.2#r8
smoke: []
dependsOn: []
trace:
  §4.1#r55: [2, 4]
  §4.1#r56: [6, 8]
  §4.1#r57: [10, 23]
  §4.1#r58: 11
  §4.1#r59: [12, 67, 74]
  §4.1#r60: [13, 15, 68, 75]
  §4.1#r61: [17, 19, 69, 76]
  §4.1#r87: [24, 25]
  §4.1#r161: [45, 70, 77]
  §4.1#r163: [46, 71, 78]
  §4.1#r179: [48, 88, 90]
  §4.1#r184: [49, 51, 81, 84]
  §4.1#r180: [53, 92, 94]
  §4.1#r182: [21, 55, 58, 86]
  §4.1#r181: [54, 57, 82, 85]
  §4.1#r200: 60
  §4.1#r201: [61, 63, 72, 79]
  §4.1#r212: 65
  §9.2#b400: [29, 31, 37, 39]
  §9.2#b424: [45, 46]
  §9.4.2#r8: [29, 31, 32, 37, 39, 40, 43]
anchor: [28, 36, 42, 57]
coverage:
  web: automated
---

# Area utama: field tab Borrow

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-059-1: Pengaturan Company default tab Borrow pada All categories: Allow Borrow `Allow`, Duration unit `Days`, Max duration `14`, Max extensions `1`, Max assets per borrower (concurrent) `3`, Allowed borrower `Employee in any Group`, Block new borrow when overdue `ON`, Photo at start `ON`, Photo at end `ON`, Require approval `ON`, Approval type `Any one approver`, Self service `OFF`, Auto-approve `ON`, Auto-approve when duration ≤ `3`, Transaction timeout `7`, Due date reminders `D-3, D-1, D-day`, Send email notifications `ON`.
  - DU-059-2: Nilai Max duration yang dicoba: `365` dan `366` untuk Duration unit `Days`, `8760` dan `8761` untuk Duration unit `Hours`.
  - DU-059-3: Pengaturan Category leaf `Machinery`: semua field Inherit, Max duration Company default `400` dengan Duration unit `Days`.
  - DU-059-4: Pengaturan Company default tab Borrow pada All categories yang berbeda dari nilai awal: Max assets per borrower (concurrent) `5`, Allowed borrower `Same Group only`, Block new borrow when overdue `OFF`, Photo at start `OFF`, Photo at end `OFF`, Due date reminders `D-day only`.
  - DU-059-5: Pengaturan Company default tab Borrow pada All categories yang berbeda dari nilai awal: Require approval `ON`, Approval type `All approvers (AND)`, Self service `OFF`, Auto-approve `OFF`, Auto-approve when duration ≤ tersimpan `5`.
  - DU-059-6: Pengaturan Company default tab Borrow pada All categories yang berbeda dari nilai awal: Require approval `OFF`, Self service `OFF`.
  - DU-059-7: Pengaturan Company default tab Borrow pada All categories yang berbeda dari nilai awal: Self service `ON`.
- Kondisi:
  - K1: node All categories terpilih, tab Borrow aktif, nilai Company default memakai DU-059-1.
  - K2: node Category leaf `Machinery` terpilih, tab Borrow aktif, nilai memakai DU-059-3.
  - K3: node All categories terpilih, tab Borrow aktif, nilai memakai DU-059-4.
  - K4: node All categories terpilih, tab Borrow aktif, nilai memakai DU-059-5.
  - K5: node All categories terpilih, tab Borrow aktif, nilai memakai DU-059-6.
  - K6: node All categories terpilih, tab Borrow aktif, nilai memakai DU-059-7.

## Test Steps

### Eligibility dan Limits Borrow
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi `Allow Borrow` bernilai `Allow`
3. Buka daftar pilihan `Allow Borrow`
4. Verifikasi pilihan `Allow Borrow` adalah `Allow` dan `Deny`
5. Tutup daftar pilihan dengan Escape
6. Verifikasi `Duration unit` bernilai `Days`
7. Buka daftar pilihan `Duration unit`
8. Verifikasi pilihan `Duration unit` adalah `Days` dan `Hours`
9. Tutup daftar pilihan dengan Escape
10. Verifikasi `Max duration` bernilai `14`
11. Verifikasi `Max extensions` bernilai `1`
12. Verifikasi `Max assets per borrower (concurrent)` bernilai `3`
13. Verifikasi `Allowed borrower` bernilai `Employee in any Group`
14. Buka daftar pilihan `Allowed borrower`
15. Verifikasi pilihan `Allowed borrower` adalah `Same Group only`, `Same Division only`, dan `Employee in any Group`
16. Tutup daftar pilihan dengan Escape
17. Verifikasi `Block new borrow when overdue` bernilai `ON`
18. Matikan `Block new borrow when overdue`
19. Verifikasi `Block new borrow when overdue` bernilai `OFF`

### Duration unit diubah tanpa konversi angka
20. Tampilkan Area utama dengan kondisi K1
21. Verifikasi `Auto-approve when duration ≤` bernilai `3`
22. Pilih `Hours` pada `Duration unit`
23. Verifikasi addon `Max duration` menunjukkan satuan yang sama dengan Duration unit `Hours`
24. Verifikasi `Max duration` tetap bernilai `14`
25. Verifikasi `Auto-approve when duration ≤` tetap bernilai `3`

### Peringatan Max duration lebih dari 1 tahun dalam Days
26. Tampilkan Area utama dengan kondisi K1
27. Ganti Max duration menjadi `365`
28. Verifikasi `Max duration` bernilai `365`
29. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tidak ada di bagian `Limits`
30. Ganti Max duration menjadi `366`
31. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tampil di bagian `Limits`
32. Verifikasi tombol `Save` aktif

### Peringatan Max duration lebih dari 1 tahun dalam Hours
33. Tampilkan Area utama dengan kondisi K1
34. Pilih `Hours` pada `Duration unit`
35. Ganti Max duration menjadi `8760`
36. Verifikasi `Max duration` bernilai `8760`
37. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tidak ada di bagian `Limits`
38. Ganti Max duration menjadi `8761`
39. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tampil di bagian `Limits`
40. Verifikasi tombol `Save` aktif

### Peringatan tidak tampil untuk nilai warisan
41. Tampilkan Area utama dengan kondisi K2
42. Verifikasi `Max duration` menampilkan `Inherit — 400 days (from Company default)`
43. Verifikasi peringatan `Max duration exceeds 1 year in total. You can still save.` tidak ada di bagian `Limits`

### Evidence Borrow
44. Tampilkan Area utama dengan kondisi K1
45. Verifikasi `Photo at start` bernilai `ON` pada bagian `Evidence`
46. Verifikasi `Photo at end` bernilai `ON` pada bagian `Evidence`

### Approval Borrow
47. Tampilkan Area utama dengan kondisi K1
48. Verifikasi `Require approval` bernilai `ON`
49. Verifikasi `Approval type` bernilai `Any one approver`
50. Buka daftar pilihan `Approval type`
51. Verifikasi pilihan `Approval type` adalah `Any one approver` dan `All approvers (AND)`
52. Tutup daftar pilihan dengan Escape
53. Verifikasi `Self service` bernilai `OFF`
54. Verifikasi `Auto-approve` bernilai `ON`
55. Verifikasi `Auto-approve when duration ≤` tampil dengan nilai `3`
56. Matikan `Auto-approve`
57. Verifikasi `Auto-approve` bernilai `OFF`
58. Verifikasi `Auto-approve when duration ≤` tidak ada

### Reminders dan Notifications Borrow
59. Tampilkan Area utama dengan kondisi K1
60. Verifikasi `Transaction timeout` bernilai `7`
61. Verifikasi `Due date reminders` bernilai `D-3, D-1, D-day`
62. Buka daftar pilihan `Due date reminders`
63. Verifikasi pilihan `Due date reminders` adalah `D-3, D-1, D-day`, `D-1, D-day`, dan `D-day only`
64. Tutup daftar pilihan dengan Escape
65. Verifikasi `Send email notifications` bernilai `ON`

### Reset to Default mengembalikan Limits, Evidence, dan Reminders Borrow ke nilai awal
66. Tampilkan Area utama dengan kondisi K3
67. Verifikasi `Max assets per borrower (concurrent)` bernilai `5`
68. Verifikasi `Allowed borrower` bernilai `Same Group only`
69. Verifikasi `Block new borrow when overdue` bernilai `OFF`
70. Verifikasi `Photo at start` bernilai `OFF` pada bagian `Evidence`
71. Verifikasi `Photo at end` bernilai `OFF` pada bagian `Evidence`
72. Verifikasi `Due date reminders` bernilai `D-day only`
73. Klik `Reset to Default`
74. Verifikasi `Max assets per borrower (concurrent)` kembali ke nilai awal `3`
75. Verifikasi `Allowed borrower` kembali ke nilai awal `Employee in any Group`
76. Verifikasi `Block new borrow when overdue` kembali ke nilai awal `ON`
77. Verifikasi `Photo at start` kembali ke nilai awal `ON` pada bagian `Evidence`
78. Verifikasi `Photo at end` kembali ke nilai awal `ON` pada bagian `Evidence`
79. Verifikasi `Due date reminders` kembali ke nilai awal `D-3, D-1, D-day`

### Reset to Default mengembalikan Approval type dan Auto-approve Borrow ke nilai awal
80. Tampilkan Area utama dengan kondisi K4
81. Verifikasi `Approval type` bernilai `All approvers (AND)`
82. Verifikasi `Auto-approve` bernilai `OFF`
83. Klik `Reset to Default`
84. Verifikasi `Approval type` kembali ke nilai awal `Any one approver`
85. Verifikasi `Auto-approve` kembali ke nilai awal `ON`
86. Verifikasi `Auto-approve when duration ≤` tampil dengan nilai awal `3`

### Reset to Default mengembalikan Require approval Borrow ke nilai awal
87. Tampilkan Area utama dengan kondisi K5
88. Verifikasi `Require approval` bernilai `OFF`
89. Klik `Reset to Default`
90. Verifikasi `Require approval` kembali ke nilai awal `ON`

### Reset to Default mengembalikan Self service Borrow ke nilai awal
91. Tampilkan Area utama dengan kondisi K6
92. Verifikasi `Self service` tampil dengan nilai `ON` sebelum Reset to Default
93. Klik `Reset to Default`
94. Verifikasi `Self service` kembali ke nilai awal `OFF`
