---
id: TC-FA-MYASSET-UI-103-tabel-task-tampilan-dan-konfigurasi
title: "Tabel Task: nilai dan format kolom, penanda PIC Division, aksi baris, konfigurasi toolbar, dan state data"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FI-15, T-MYA-01, "§1.2#r40", "§1.2#r47", "§1.2#r71", "§4.1#p2", "§5#r1", "§5#r3", "§7.1#r1", "§9.4.3#b11", "EB-TBL-1@tabel-task", "EB-FLT-6@tabel-task"]
smoke: []
dependsOn: []
trace:
  FI-15: [46, 47]
  T-MYA-01: [2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16, 17, 18, 19, 21, 23, 25, 27, 29, 35, 38, 41, 54, 55, 59, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 103, 105, 106, 108, 110, 111]
  "§1.2#r40": 34
  "§1.2#r47": [31, 33]
  "§1.2#r71": [39, 42]
  "§4.1#p2": [2, 6, 7, 54, 55, 56]
  "§5#r1": 49
  "§5#r3": 51
  "§7.1#r1": [86, 87, 92, 93]
  "§9.4.3#b11": [39, 42]
  "EB-TBL-1@tabel-task": [88, 94, 96, 97, 98, 100, 101]
  "EB-FLT-6@tabel-task": [82, 84]
anchor: [45, 58, 77, 81]
coverage:
  web: automated
---

# Tabel Task: nilai dan format kolom, penanda PIC Division, aksi baris, konfigurasi toolbar, dan state data

## Prerequisites
- Aktor: Borrower, Assignee, PIC Borrower, dan PIC Division `Finance` (satu pengguna memegang keempat posisi itu).
- Layar awal: Halaman My Asset, tab Task.
- Komponen: Tabel Task (T-MYA-01)
- Data:
  - DU-103-1: Task Borrow: Transaction ID `BRW-2026-0152`, Task `Confirm Handover`, Group `Head Office`, Total Asset `6`, Handed Over By `Rina Wulandari`, Expires At `2026-11-09 20:41`.
  - DU-103-2: Task Assignment: Transaction ID `ASG-2026-0071`, Task `Confirm Handover`, Group `Jakarta Selatan Distribution Center` dengan hierarki `Region Jawa > Jakarta Selatan Distribution Center`, Total Asset `3`, Handed Over By `Alexander Graham Bell`, Expires At `2026-11-09 20:43`.
  - DU-103-3: Task Assignment atas nama Division `Finance`: Transaction ID `ASG-2026-0072`, Task `Confirm Handover`, Group `Head Office`, Total Asset `2`, Handed Over By `Buzzlightyear Sumardi`, Expires At `2026-11-09 20:48`.
  - DU-103-4: Task Borrow atas nama Borrower tanpa akun yang PIC-nya pengguna: Transaction ID `BRW-2026-0158`, Task `Confirm Handover`, Group `Head Office`, Total Asset `4`, Handed Over By `Budi`, Expires At `2026-11-09 21:05`.
  - DU-103-5: Task Borrow: Transaction ID `BRW-2026-0159`, Task `Confirm Handover`, Group `Head Office`, Total Asset `5`, Handed Over By `Dewi Anggraini`, Expires At `2026-11-09 21:10`.
  - DU-103-6: Task Borrow: Transaction ID `BRW-2026-0160`, Task `Confirm Handover`, Group `Head Office`, Total Asset `1`, Handed Over By `Dewi Anggreni`, Expires At `2026-11-09 21:15`.
  - DU-103-7: Task Borrow dari aksi sistem: Transaction ID `BRW-2026-0161`, Task `Confirm Handover`, Group `Head Office`, Total Asset `7`, Handed Over By `System`, Expires At `2026-11-09 21:20`.
  - DU-103-8: pengguna tanpa Task aktif (`0`).
  - DU-103-9: kata kunci Search `BRW-9999` yang tidak cocok dengan Task mana pun.
  - DU-103-10: Task Borrow yang diserahkan Aktor yang sudah dinonaktifkan, dengan nama tercatat saat aksi: Transaction ID `BRW-2026-0162`, Task `Confirm Handover`, Group `Head Office`, Total Asset `2`, Handed Over By `Agus Pratama`, Expires At `2026-11-09 21:25`.
  - DU-103-11: Task Borrow yang diserahkan Aktor yang sudah dihapus, dengan nama tercatat saat aksi: Transaction ID `BRW-2026-0163`, Task `Confirm Handover`, Group `Head Office`, Total Asset `3`, Handed Over By `Maya Kusuma`, Expires At `2026-11-09 21:30`.
  - Nilai tampil turunan: Handed Over By `Rina W` dari `Rina Wulandari`; Handed Over By `Agus P` dari `Agus Pratama`; Handed Over By `Maya K` dari `Maya Kusuma`; Expires At `09/11/26, 20:41` dari `2026-11-09 20:41` dengan Date Format `dd/MM/yy` dan Time Format `24 jam`; Group `Jakarta Sela..ution Center` dari `Jakarta Selatan Distribution Center`.
- Kondisi:
  - K1: Date Format bernilai `dd/MM/yy`, Time Format bernilai `24 jam`; Task berisi DU-103-1 sampai DU-103-7.
  - K2: Task berisi DU-103-8, yaitu daftar kosong.
  - K3: Task berisi DU-103-1; pencarian DU-103-9 dijawab tanpa baris.
  - K4: memuat daftar Task gagal karena error server pada permintaan pertama; permintaan ulang dijawab dengan DU-103-1.
  - K5: Task berisi DU-103-1 dan DU-103-3.
  - K6: Task berisi DU-103-10 dan DU-103-11; Aktor penyerah DU-103-10 sudah dinonaktifkan dan Aktor penyerah DU-103-11 sudah dihapus, dan nama yang dikirim respons adalah nama yang tercatat saat aksi.

## Test Steps

### Nilai dan format sel pada baris Task
1. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K1
2. Verifikasi header kolom `Transaction ID`, `Task`, `Group`, `Total Asset`, `Handed Over By`, dan `Expires At` tampil
3. Verifikasi sel Task baris `BRW-2026-0152` menampilkan badge `Confirm Handover`
4. Verifikasi sel Group baris `BRW-2026-0152` menampilkan `Head Office`
5. Verifikasi sel Total Asset baris `BRW-2026-0152` menampilkan `6`
6. Verifikasi sel Handed Over By baris `BRW-2026-0152` menampilkan `Rina W`, dari `Rina Wulandari`
7. Verifikasi sel Expires At baris `BRW-2026-0152` menampilkan `09/11/26, 20:41`, dari `2026-11-09 20:41` dengan Date Format `dd/MM/yy` dan Time Format `24 jam`
8. Verifikasi sel Task baris `ASG-2026-0071` menampilkan badge `Confirm Handover`

### Group bernama panjang dipotong dan hierarkinya tampil di tooltip
9. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K1
10. Verifikasi sel Group baris `ASG-2026-0071` menampilkan `Jakarta Sela..ution Center`, dari `Jakarta Selatan Distribution Center` (35 karakter)
11. Arahkan kursor ke sel Group baris `ASG-2026-0071`
12. Verifikasi tooltip `Region Jawa > Jakarta Selatan Distribution Center` tampil

### Nama user tampil singkat dengan tooltip nama lengkap
13. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K1
14. Verifikasi sel Handed Over By baris `ASG-2026-0071` menampilkan `Alexander G`, dari `Alexander Graham Bell`
15. Verifikasi sel Handed Over By baris `ASG-2026-0072` menampilkan `Buzzlightyear S`, dari `Buzzlightyear Sumardi`
16. Verifikasi sel Handed Over By baris `BRW-2026-0158` menampilkan `Budi`, dari `Budi`
17. Verifikasi sel Handed Over By baris `BRW-2026-0159` menampilkan `Dewi A`, dari `Dewi Anggraini`
18. Verifikasi sel Handed Over By baris `BRW-2026-0160` menampilkan `Dewi A`, dari `Dewi Anggreni`
19. Verifikasi sel Handed Over By baris `BRW-2026-0161` menampilkan `System`
20. Arahkan kursor ke sel Handed Over By baris `ASG-2026-0071`
21. Verifikasi tooltip `Alexander Graham Bell` tampil
22. Arahkan kursor ke sel Handed Over By baris `ASG-2026-0072`
23. Verifikasi tooltip `Buzzlightyear Sumardi` tampil
24. Arahkan kursor ke sel Handed Over By baris `BRW-2026-0158`
25. Verifikasi tooltip `Budi` tampil
26. Arahkan kursor ke sel Handed Over By baris `BRW-2026-0159`
27. Verifikasi tooltip `Dewi Anggraini` tampil
28. Arahkan kursor ke sel Handed Over By baris `BRW-2026-0160`
29. Verifikasi tooltip `Dewi Anggreni` tampil

### Penanda atas nama Division pada sel Transaction ID
30. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K1
31. Verifikasi sel Transaction ID baris `ASG-2026-0072` menampilkan penanda atas nama Division berupa ikon dan `Finance`
32. Arahkan kursor ke penanda `Finance` pada baris `ASG-2026-0072`
33. Verifikasi tooltip `On behalf of: Finance` tampil
34. Verifikasi sel Transaction ID baris `BRW-2026-0158` tidak menampilkan penanda atas nama
35. Verifikasi sel Transaction ID baris `BRW-2026-0152` berupa teks biasa, bukan tautan

### Confirm hanya tersedia di dialog Confirm Handover
36. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K1
37. Klik menu `⋯` pada baris `ASG-2026-0071`
38. Verifikasi aksi `Confirm Handover` tampil pada menu baris
39. Verifikasi aksi `Confirm` tidak tampil pada menu baris
40. Klik `Confirm Handover`
41. Verifikasi dialog `Confirm Handover` tampil
42. Verifikasi tombol `[Confirm]` tampil pada dialog
43. Klik `[Cancel]`

### Tabel Task tanpa checkbox dan bulk action
44. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K1
45. Verifikasi header kolom `Transaction ID` tampil
46. Verifikasi tabel Task tidak memiliki checkbox pada baris maupun pada header
47. Verifikasi `Bulk Action` tidak tampil

### Toolbar dan placeholder Search
48. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K1
49. Verifikasi toolbar tab `Task` memuat ikon `Search`, `Filter`, dan `Download`
50. Klik ikon `Search`
51. Verifikasi kotak Search memuat placeholder `Search transaction ID, task...`

### Setup Column memuat enam kolom yang semuanya Hideable
52. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K1
53. Klik header kolom Actions `⋯`
54. Verifikasi daftar kolom memuat `Transaction ID`, `Task`, `Group`, `Total Asset`, `Handed Over By`, dan `Expires At` dalam keadaan tercentang
55. Verifikasi checkbox keenam kolom itu aktif
56. Verifikasi `Checkbox` dan `Actions` tidak ada dalam daftar kolom
57. Hilangkan centang kolom `Transaction ID`
58. Verifikasi header kolom `Task` tampil
59. Verifikasi header kolom `Transaction ID` tidak tampil

### Filter Panel memuat field untuk kolom yang bisa difilter
60. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K1
61. Klik `Filter` pada toolbar
62. Verifikasi field `Task` tampil dengan placeholder `All tasks`
63. Verifikasi field `Task` berjenis multi-select yang bisa dicari
64. Verifikasi field `Group` tampil dengan placeholder `All groups`
65. Verifikasi field `Group` berjenis multi-select yang bisa dicari
66. Verifikasi field `Total Asset` berjenis rentang angka
67. Verifikasi input rentang `Total Asset` memiliki placeholder `Min` dan `Max`
68. Verifikasi field `Handed Over By` tampil dengan placeholder `All users`
69. Verifikasi field `Handed Over By` berjenis multi-select yang bisa dicari
70. Verifikasi field `Expires At` tampil dengan placeholder `Select date`
71. Verifikasi field `Expires At` berjenis date range picker
72. Verifikasi field `Transaction ID` tidak tampil pada Filter Panel

### Menyembunyikan kolom tidak menghapus field dan saringan yang diterapkan
73. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K5
74. Klik `Filter` pada toolbar
75. Pilih `Confirm Handover` pada field `Task`
76. Klik `[Apply]`
77. Verifikasi ikon `Filter` pada toolbar tabel Task menandai ada saringan yang diterapkan
78. Klik `Filter` pada toolbar untuk menutup panel
79. Klik header kolom Actions `⋯`
80. Hilangkan centang kolom `Task`
81. Verifikasi header kolom `Task` tidak tampil
82. Verifikasi ikon `Filter` pada toolbar tabel Task tetap menandai ada saringan yang diterapkan
83. Klik `Filter` pada toolbar
84. Verifikasi field `Task` tetap tampil di Filter Panel dan berisi `Confirm Handover`

### Empty state saat belum ada Task
85. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K2
86. Verifikasi judul `No tasks` tampil
87. Verifikasi deskripsi `Handover confirmations appear here.` tampil
88. Verifikasi empty state tabel Task tidak memuat tombol aksi

### Empty state saat pencarian tidak menemukan hasil
89. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K3
90. Klik ikon `Search`
91. Ketik Search `BRW-9999`, tekan Enter
92. Verifikasi judul `No results found` tampil
93. Verifikasi deskripsi `Try adjusting your search or filter.` tampil
94. Verifikasi judul `No tasks` tidak tampil

### Gagal memuat daftar Task
95. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K4
96. Verifikasi pesan `Unable to load this data.` tampil
97. Verifikasi tabel Task menyediakan tombol `[Try Again]`
98. Verifikasi judul `No tasks` tidak tampil
99. Klik `[Try Again]`
100. Verifikasi baris `BRW-2026-0152` tampil
101. Verifikasi pesan `Unable to load this data.` tidak tampil

### Handed Over By tetap tampil dengan nama tercatat bila Aktor nonaktif atau dihapus
102. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K6
103. Verifikasi sel Handed Over By baris `BRW-2026-0162` menampilkan `Agus P`, dari `Agus Pratama`
104. Arahkan kursor ke sel Handed Over By baris `BRW-2026-0162`
105. Verifikasi tooltip `Agus Pratama` tampil
106. Verifikasi sel Handed Over By baris `BRW-2026-0163` menampilkan `Maya K`, dari `Maya Kusuma`
107. Arahkan kursor ke sel Handed Over By baris `BRW-2026-0163`
108. Verifikasi tooltip `Maya Kusuma` tampil

### Urutan kolom tabel Task
109. Tampilkan Tabel Task (T-MYA-01) dengan kondisi K1
110. Verifikasi urutan header kolom dari kiri ke kanan adalah `Transaction ID`, `Task`, `Group`, `Total Asset`, `Handed Over By`, `Expires At`
111. Verifikasi `Expires At` adalah kolom data terakhir sebelum kolom Actions
