---
id: TC-FA-ASSIGN-UI-118-tabel-transactions-setup-column
title: "Tabel Transactions: mekanik Setup Column"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-KOL-1@tabel-transactions", "EB-KOL-3"]
smoke: []
dependsOn: []
trace:
  "EB-KOL-1@tabel-transactions": [4, 5, 6, 7, 8, 9, 10, 11, 17, 18, 19, 22, 25, 31, 38, 40, 42, 52, 54, 55, 65, 66, 72, 73, 76, 82, 83, 86, 91, 93, 95]
  "EB-KOL-3": [101]
coverage:
  web: automated
---

# Tabel Transactions: mekanik Setup Column

## Prerequisites
- Aktor: Aktor Assignment.
- Layar awal: Transactions > Assignment, tab Transactions.
- Komponen: Tabel Transactions
- Data:
  - DU-118-1: Assignment `ASG-2026-0071`, Status `Waiting for Handover`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `3`, Requested By `Rina W`, Request Date `09 Nov 2026, 19:00`, Last Updated `09 Nov 2026, 20:40`.
  - DU-118-2: Assignment `ASG-2026-0070`, Status `Waiting for Approval`, Group `Head Office`, Assignee `Sari D`, Assignee Type `Employee`, Total Asset `2`, Requested By `Agus P`, Request Date `09 Nov 2026, 14:00`, Last Updated `09 Nov 2026, 14:00`.
- Kondisi:
  - K1: daftar Tabel Transactions berisi DU-118-1 dan DU-118-2, dan pengaturan kolom masih bawaan.

## Test Steps

### Anatomi modal Setup Column
1. Tampilkan Tabel Transactions dengan kondisi K1
2. Klik header kolom aksi baris
3. Klik `Setup Column...`
4. Verifikasi modal dengan judul `Setup Column` tampil
5. Verifikasi deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.` tampil pada modal
6. Verifikasi tombol `[✕]` tampil pada modal
7. Verifikasi tombol `[Reset to Default]` tampil pada footer modal
8. Verifikasi tombol `[Save]` tampil pada footer modal
9. Verifikasi tombol `[Cancel]` tidak tampil pada footer modal
10. Verifikasi daftar kolom memuat `Transaction ID`, `Status`, `Group`, `Assignee`, `Assignee Type`, `Total Asset`, `Requested By`, `Request Date`, dan `Last Updated`
11. Verifikasi kolom aksi baris tidak ada pada daftar kolom

### Menyembunyikan dan menampilkan kolom lewat modal
12. Tampilkan Tabel Transactions dengan kondisi K1
13. Klik header kolom aksi baris
14. Klik `Setup Column...`
15. Hilangkan centang kolom `Status` pada daftar kolom
16. Klik `[Save]`
17. Verifikasi modal Setup Column tertutup
18. Verifikasi tabel memuat kolom `Transaction ID`
19. Verifikasi tabel tidak memuat kolom `Status`
20. Klik header kolom aksi baris
21. Klik `Setup Column...`
22. Verifikasi kolom `Status` tidak tercentang pada daftar kolom
23. Centang kolom `Status` pada daftar kolom
24. Klik `[Save]`
25. Verifikasi tabel memuat kolom `Status`

### Mengubah urutan kolom lewat modal
26. Tampilkan Tabel Transactions dengan kondisi K1
27. Klik header kolom aksi baris
28. Klik `Setup Column...`
29. Seret kolom `Last Updated` ke atas kolom `Transaction ID` pada daftar kolom
30. Klik `[Save]`
31. Verifikasi kolom `Last Updated` berada sebelum kolom `Transaction ID` pada tabel

### Batas pin dan ikon pin yang disabled
32. Tampilkan Tabel Transactions dengan kondisi K1
33. Klik header kolom aksi baris
34. Klik `Setup Column...`
35. Klik ikon pin pada kolom `Transaction ID`
36. Klik ikon pin pada kolom `Status`
37. Klik ikon pin pada kolom `Group`
38. Verifikasi ikon pin pada kolom `Assignee` disabled
39. Arahkan kursor ke ikon pin pada kolom `Assignee`
40. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
41. Klik ikon pin pada kolom `Group` untuk melepas pin
42. Verifikasi ikon pin pada kolom `Assignee` aktif

### Reset to Default mengembalikan konfigurasi bawaan sesudah Save
43. Tampilkan Tabel Transactions dengan kondisi K1
44. Klik header kolom aksi baris
45. Klik `Setup Column...`
46. Hilangkan centang kolom `Status` pada daftar kolom
47. Seret kolom `Last Updated` ke atas kolom `Transaction ID` pada daftar kolom
48. Klik `[Save]`
49. Klik header kolom aksi baris
50. Klik `Setup Column...`
51. Klik `[Reset to Default]`
52. Verifikasi kolom `Status` tercentang pada daftar kolom
53. Klik `[Save]`
54. Verifikasi tabel memuat kolom `Status`
55. Verifikasi kolom `Transaction ID` berada sebelum kolom `Last Updated` pada tabel

### Reset to Default belum permanen sebelum Save
56. Tampilkan Tabel Transactions dengan kondisi K1
57. Klik header kolom aksi baris
58. Klik `Setup Column...`
59. Hilangkan centang kolom `Status` pada daftar kolom
60. Klik `[Save]`
61. Klik header kolom aksi baris
62. Klik `Setup Column...`
63. Klik `[Reset to Default]`
64. Klik `[✕]` pada modal
65. Verifikasi tabel memuat kolom `Transaction ID`
66. Verifikasi tabel tidak memuat kolom `Status`

### Menutup modal dengan klik `[✕]` membuang perubahan
67. Tampilkan Tabel Transactions dengan kondisi K1
68. Klik header kolom aksi baris
69. Klik `Setup Column...`
70. Hilangkan centang kolom `Status` pada daftar kolom
71. Klik `[✕]` pada modal
72. Verifikasi modal Setup Column tertutup
73. Verifikasi tabel masih memuat kolom `Status`
74. Klik header kolom aksi baris
75. Klik `Setup Column...`
76. Verifikasi kolom `Status` tercentang pada daftar kolom

### Menutup modal dengan Esc membuang perubahan
77. Tampilkan Tabel Transactions dengan kondisi K1
78. Klik header kolom aksi baris
79. Klik `Setup Column...`
80. Hilangkan centang kolom `Status` pada daftar kolom
81. Tekan Esc
82. Verifikasi modal Setup Column tertutup
83. Verifikasi tabel masih memuat kolom `Status`
84. Klik header kolom aksi baris
85. Klik `Setup Column...`
86. Verifikasi kolom `Status` tercentang pada daftar kolom

### Kolom visible terakhir tidak bisa disembunyikan
87. Tampilkan Tabel Transactions dengan kondisi K1
88. Klik header kolom aksi baris
89. Klik `Setup Column...`
90. Hilangkan centang semua kolom pada daftar kolom kecuali `Transaction ID`
91. Verifikasi centang kolom `Transaction ID` disabled
92. Arahkan kursor ke centang kolom `Transaction ID`
93. Verifikasi tooltip `At least one column must remain visible.` tampil
94. Centang kolom `Status` pada daftar kolom
95. Verifikasi centang kolom `Transaction ID` aktif

### Konfigurasi kolom Tabel Transactions tersimpan
96. Tampilkan Tabel Transactions dengan kondisi K1
97. Klik header kolom aksi baris
98. Klik `Setup Column...`
99. Hilangkan centang kolom `Group` pada daftar kolom
100. Klik `[Save]`
101. Verifikasi tabel Transactions tidak memuat kolom `Group`
