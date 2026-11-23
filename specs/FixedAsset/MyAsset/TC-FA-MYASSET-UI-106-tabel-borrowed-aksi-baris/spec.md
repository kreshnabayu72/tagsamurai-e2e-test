---
id: TC-FA-MYASSET-UI-106-tabel-borrowed-aksi-baris
title: "Tabel Borrowed: aksi baris yang tampil menurut keadaan baris"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r29", "§1.2#r31", "§1.2#r32", "§1.2#r33", "§1.2#r36", "§4.1b#p3", "§4.1b#r19", "§4.1b#r28", "§4.1b#r29", "§4.1b#r30", "§4.1b#r31", "§4.1b#r35", "§4.1b#r36", "§4.1b#r37", "§4.1b#r38", "§4.1b#r40", "§4.1b#r41", "§4.1b#r42", "§4.1b#r47", "§4.1b#r49", "§4.1b#r50", "§4.1b#r56", "§4.1b#r57", "§4.1b#r60", "§4.1b#r67", "§4.1b#r68", "§4.1b#r75", "§4.1b#p5", "§4.3#r7", "§4.4#r51", "§9.4.2#r45", "§9.4.2#r47", "§9.4.2#r55", "§9.4.2#r91", "§9.4.3#b3", "§9.4.3#b4", "§9.4.3#b7"]
smoke: []
dependsOn: []
trace:
  "§1.2#r29": [3, 11]
  "§1.2#r31": [4, 8]
  "§1.2#r32": [3, 7]
  "§1.2#r33": [13, 20]
  "§1.2#r36": [34, 35, 36, 40, 43, 45, 46, 63, 66, 69, 79, 82, 83]
  "§4.1b#p3": [11, 16]
  "§4.1b#r19": [3, 7, 11, 16]
  "§4.1b#r28": [3, 16, 23]
  "§4.1b#r29": [12, 16, 23]
  "§4.1b#r30": 56
  "§4.1b#r31": [16, 72]
  "§4.1b#r35": [3, 11, 19]
  "§4.1b#r36": [35, 45, 63, 66, 69]
  "§4.1b#r37": [49, 50]
  "§4.1b#r38": [27, 31]
  "§4.1b#r40": [3, 11, 19]
  "§4.1b#r41": [36, 46, 63, 66, 69]
  "§4.1b#r42": [49, 51]
  "§4.1b#r47": [36, 46]
  "§4.1b#r49": [3, 11, 19]
  "§4.1b#r50": [37, 43, 49, 52, 63, 66, 69]
  "§4.1b#r56": [7, 26, 30, 75]
  "§4.1b#r57": [26, 30, 75]
  "§4.1b#r60": [34, 40]
  "§4.1b#r67": [44, 60]
  "§4.1b#r68": [49, 55, 59]
  "§4.1b#r75": [3, 7]
  "§4.1b#p5": [3, 7]
  "§4.3#r7": [27, 30, 76, 87, 91, 95, 99]
  "§4.4#r51": [3, 11]
  "§9.4.2#r45": [27, 31]
  "§9.4.2#r47": [26, 30]
  "§9.4.2#r55": 19
  "§9.4.2#r91": [19, 23]
  "§9.4.3#b3": [4, 8]
  "§9.4.3#b4": [13, 20]
  "§9.4.3#b7": 12
anchor: [81, 86, 90, 94, 98]
coverage:
  web: automated
---

# Tabel Borrowed: aksi baris yang tampil menurut keadaan baris

## Prerequisites
- Aktor: Borrower (Budi Santoso, pengguna yang membuka halaman My Asset miliknya; untuk K3 juga PIC Borrower atas nama Borrower tanpa akun `Agus Pratama`).
- Layar awal: Halaman My Asset > tab Borrowed
- Komponen: Tabel Borrowed (T-MYA-02)
- Data:
  - DU-106-1: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 8`, Asset ID `LPT-2026-0008`, Status `Waiting for Approval`, Source `Admin`, Borrower `Me`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-2: respons tiruan, satu baris tabel Borrowed: Name `Projector Epson EB-X06 - 12`, Asset ID `PRJ-2026-0012`, Status `Waiting for Handover`, Source `Admin`, Borrower `Me`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-3: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 3`, Asset ID `LPT-2026-0003`, Status `Borrowed`, Source `Admin`, Borrower `Me`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-4: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 2`, Asset ID `MIC-2026-0002`, Status `Borrowed`, Source `Self-service`, Borrower `Me`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-5: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Status `Overdue`, Source `Admin`, Borrower `Me`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `null`, Duration `4 days`.
  - DU-106-6: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 8`, Asset ID `MIC-2026-0008`, Status `Overdue`, Source `Self-service`, Borrower `Me`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `null`, Duration `3 hours`.
  - DU-106-7: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 51`, Asset ID `LPT-2026-0051`, Status `Extension Request`, Source `Admin`, Borrower `Me`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `menunggu review`.
  - DU-106-8: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Status `Extension Approval`, Source `Admin`, Borrower `Me`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `menunggu approval`.
  - DU-106-9: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 54`, Asset ID `LPT-2026-0054`, Status `Borrowed + Reported Damaged`, Source `Admin`, Borrower `Me`, Damage Report `Waiting for Confirmation`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-10: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 5`, Asset ID `MIC-2026-0005`, Status `Borrowed + Reported Damaged`, Source `Self-service`, Borrower `Me`, Damage Report `Waiting for Confirmation`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-11: respons tiruan, satu baris tabel Borrowed: Name `Camera Sony A7 - 3`, Asset ID `CAM-2026-0003`, Status `Borrowed + Damaged`, Source `Admin`, Borrower `Me`, Damage Report `Damaged`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-12: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 12`, Asset ID `LPT-2026-0012`, Status `Borrowed + Reported Missing`, Source `Admin`, Borrower `Me`, Damage Report `null`, Laporan Missing `Waiting for Confirmation`, Pengajuan Extend `null`.
  - DU-106-13: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 6`, Asset ID `MIC-2026-0006`, Status `Borrowed + Reported Missing`, Source `Self-service`, Borrower `Me`, Damage Report `null`, Laporan Missing `Waiting for Confirmation`, Pengajuan Extend `null`.
  - DU-106-14: respons tiruan, satu baris tabel Borrowed: Name `Camera Sony A7 - 4`, Asset ID `CAM-2026-0004`, Status `Borrowed + Damaged + Reported Missing`, Source `Admin`, Borrower `Me`, Damage Report `Damaged`, Laporan Missing `Waiting for Confirmation`, Pengajuan Extend `null`.
  - DU-106-15: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 15`, Asset ID `LPT-2026-0015`, Status `Borrowed`, Source `Admin`, Borrower `Me`, Damage Report `Rejected`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-16: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 16`, Asset ID `LPT-2026-0016`, Status `Borrowed`, Source `Admin`, Borrower `Me`, Damage Report `Canceled`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-17: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 17`, Asset ID `LPT-2026-0017`, Status `Borrowed`, Source `Admin`, Borrower `Me`, Damage Report `Repaired`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-18: respons tiruan, satu baris tabel Borrowed: Name `Tablet Samsung Galaxy Tab - 4`, Asset ID `TAB-2026-0004`, Status `Borrowed`, Source `Self-service`, Borrower `Agus Pratama`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `null`, PIC `Budi Santoso`.
  - DU-106-19: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 53`, Asset ID `LPT-2026-0053`, Status `Overdue + Extension Request`, Source `Admin`, Borrower `Me`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `menunggu review`, Duration `6 days`.
  - DU-106-20: respons tiruan, satu baris tabel Borrowed: Name `Tablet Samsung Galaxy Tab - 7`, Asset ID `TAB-2026-0007`, Status `Borrowed + Damaged`, Source `Self-service`, Borrower `Me`, Damage Report `Damaged`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-21: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 18`, Asset ID `LPT-2026-0018`, Status `Borrowed`, Source `Admin`, Borrower `Me`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `null`.
  - DU-106-22: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 19`, Asset ID `LPT-2026-0019`, Status `Overdue`, Source `Admin`, Borrower `Me`, Damage Report `null`, Laporan Missing `null`, Pengajuan Extend `null`, Duration `2 days`.
- Kondisi:
  - K1: tabel Borrowed berisi DU-106-1 sampai DU-106-8 dan DU-106-19.
  - K2: tabel Borrowed berisi DU-106-9 sampai DU-106-14 dan DU-106-20.
  - K3: tabel Borrowed berisi DU-106-15 sampai DU-106-18.
  - K4: tabel Borrowed berisi DU-106-21 dan DU-106-22, dan respons menyatakan level Borrowing `Basic`.
  - K5: tabel Borrowed berisi DU-106-21 dan DU-106-22, dan respons menyatakan level Borrowing `None`.

## Test Steps

### Baris Waiting for Approval dan Waiting for Handover hanya memiliki Borrow Log dan Cancel Borrow
1. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
2. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 8`
3. Verifikasi menu baris memuat tepat `Borrow Log` dan `Cancel Borrow`, dalam urutan itu
4. Verifikasi menu baris tidak memuat `Review`
5. Tekan Esc untuk menutup menu baris
6. Klik `⋯` pada baris `Projector Epson EB-X06 - 12`
7. Verifikasi menu baris memuat tepat `Borrow Log` dan `Cancel Borrow`, dalam urutan itu
8. Verifikasi menu baris tidak memuat `Hand over`

### Baris Borrowed dari Admin dan dari self-service
9. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
10. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 3`
11. Verifikasi menu baris memuat tepat `Borrow Log`, `Request Extension`, `Report Damaged`, dan `Report Missing`, dalam urutan itu
12. Verifikasi menu baris tidak memuat `Return`
13. Verifikasi menu baris tidak memuat `Cancel Borrow`
14. Tekan Esc untuk menutup menu baris
15. Klik `⋯` pada baris `Meeting Mic Set - 2`
16. Verifikasi menu baris memuat tepat `Borrow Log`, `Return`, `Request Extension`, `Report Damaged`, dan `Report Missing`, dalam urutan itu

### Baris Overdue tetap memiliki Request Extension
17. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
18. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 9`
19. Verifikasi menu baris Overdue berdurasi `4 days` (satuan Days) memuat tepat `Borrow Log`, `Request Extension`, `Report Damaged`, dan `Report Missing`, dalam urutan itu
20. Verifikasi menu baris tidak memuat `Cancel Borrow`
21. Tekan Esc untuk menutup menu baris
22. Klik `⋯` pada baris `Meeting Mic Set - 8`
23. Verifikasi menu baris Overdue berdurasi `3 hours` (satuan Hours) memuat tepat `Borrow Log`, `Return`, `Request Extension`, `Report Damaged`, dan `Report Missing`, dalam urutan itu

### Baris dengan pengajuan Extend yang menunggu memiliki Cancel Extension Request
24. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
25. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 51`
26. Verifikasi menu baris memuat tepat `Borrow Log`, `Report Damaged`, `Report Missing`, dan `Cancel Extension Request`, dalam urutan itu
27. Verifikasi menu baris tidak memuat `Request Extension`
28. Tekan Esc untuk menutup menu baris
29. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 10`
30. Verifikasi menu baris memuat tepat `Borrow Log`, `Report Damaged`, `Report Missing`, dan `Cancel Extension Request`, dalam urutan itu
31. Verifikasi menu baris tidak memuat `Request Extension`

### Baris dengan Damage Report menunggu konfirmasi memiliki Cancel Damage Report
32. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K2
33. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 54`
34. Verifikasi menu baris memuat tepat `Borrow Log` dan `Cancel Damage Report`, dalam urutan itu
35. Verifikasi menu baris tidak memuat `Request Extension`
36. Verifikasi menu baris tidak memuat `Report Damaged`
37. Verifikasi menu baris tidak memuat `Report Missing`
38. Tekan Esc untuk menutup menu baris
39. Klik `⋯` pada baris `Meeting Mic Set - 5`
40. Verifikasi menu baris memuat tepat `Borrow Log`, `Return`, dan `Cancel Damage Report`, dalam urutan itu

### Baris yang record Damage Report-nya sudah Damaged
41. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K2
42. Klik `⋯` pada baris `Camera Sony A7 - 3`
43. Verifikasi menu baris memuat tepat `Borrow Log` dan `Report Missing`, dalam urutan itu
44. Verifikasi menu baris tidak memuat `Cancel Damage Report`
45. Verifikasi menu baris tidak memuat `Request Extension`
46. Verifikasi menu baris tidak memuat `Report Damaged`

### Baris dengan laporan Missing menunggu konfirmasi memiliki Cancel Missing Report
47. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K2
48. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 12`
49. Verifikasi menu baris memuat tepat `Borrow Log` dan `Cancel Missing Report`, dalam urutan itu
50. Verifikasi menu baris tidak memuat `Request Extension`
51. Verifikasi menu baris tidak memuat `Report Damaged`
52. Verifikasi menu baris tidak memuat `Report Missing`
53. Tekan Esc untuk menutup menu baris
54. Klik `⋯` pada baris `Meeting Mic Set - 6`
55. Verifikasi menu baris memuat tepat `Borrow Log` dan `Cancel Missing Report`, dalam urutan itu
56. Verifikasi menu baris tidak memuat `Return`
57. Tekan Esc untuk menutup menu baris
58. Klik `⋯` pada baris `Camera Sony A7 - 4`
59. Verifikasi menu baris memuat tepat `Borrow Log` dan `Cancel Missing Report`, dalam urutan itu
60. Verifikasi menu baris tidak memuat `Cancel Damage Report`

### Request Extension, Report Damaged, dan Report Missing tampil lagi sesudah Damage Report ditutup
61. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K3
62. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 15`
63. Verifikasi menu baris memuat tepat `Borrow Log`, `Request Extension`, `Report Damaged`, dan `Report Missing`, dalam urutan itu
64. Tekan Esc untuk menutup menu baris
65. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 16`
66. Verifikasi menu baris memuat tepat `Borrow Log`, `Request Extension`, `Report Damaged`, dan `Report Missing`, dalam urutan itu
67. Tekan Esc untuk menutup menu baris
68. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 17`
69. Verifikasi menu baris memuat tepat `Borrow Log`, `Request Extension`, `Report Damaged`, dan `Report Missing`, dalam urutan itu

### Return tampil bagi PIC Borrower atas nama Borrower tanpa akun
70. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K3
71. Klik `⋯` pada baris `Tablet Samsung Galaxy Tab - 4`
72. Verifikasi menu baris memuat tepat `Borrow Log`, `Return`, `Request Extension`, `Report Damaged`, dan `Report Missing`, dalam urutan itu

### Baris Overdue dengan pengajuan Extend yang menunggu memiliki Cancel Extension Request
73. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
74. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 53`
75. Verifikasi menu baris Overdue dengan pengajuan Extend yang menunggu memuat tepat `Borrow Log`, `Report Damaged`, `Report Missing`, dan `Cancel Extension Request`, dalam urutan itu
76. Verifikasi menu baris tidak memuat `Request Extension`

### Return tetap tersedia pada pinjaman self-service yang record Damage Report-nya Damaged
77. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K2
78. Klik `⋯` pada baris `Tablet Samsung Galaxy Tab - 7`
79. Verifikasi menu baris memuat tepat `Borrow Log`, `Return`, dan `Report Missing`, dalam urutan itu

### Badge Reported Damaged dan Damaged hilang sesudah Damage Report Repaired
80. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K3
81. Verifikasi sel Status baris `Laptop Dell Latitude 5420 - 17` menampilkan badge `Borrowed`
82. Verifikasi badge `Reported Damaged` tidak tampil pada sel Status baris `Laptop Dell Latitude 5420 - 17`
83. Verifikasi badge `Damaged` tidak tampil pada sel Status baris `Laptop Dell Latitude 5420 - 17`

### Request Extension tidak tampil pada level Borrowing Basic
84. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K4
85. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 18`
86. Verifikasi menu baris memuat `Borrow Log`
87. Verifikasi `Request Extension` tidak tampil pada menu baris Borrowed di level Borrowing `Basic`
88. Tekan Esc untuk menutup menu baris
89. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 19`
90. Verifikasi menu baris memuat `Borrow Log`
91. Verifikasi `Request Extension` tidak tampil pada menu baris Overdue di level Borrowing `Basic`

### Request Extension tidak tampil pada level Borrowing None
92. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K5
93. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 18`
94. Verifikasi menu baris memuat `Borrow Log`
95. Verifikasi `Request Extension` tidak tampil pada menu baris Borrowed di level Borrowing `None`
96. Tekan Esc untuk menutup menu baris
97. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 19`
98. Verifikasi menu baris memuat `Borrow Log`
99. Verifikasi `Request Extension` tidak tampil pada menu baris Overdue di level Borrowing `None`
