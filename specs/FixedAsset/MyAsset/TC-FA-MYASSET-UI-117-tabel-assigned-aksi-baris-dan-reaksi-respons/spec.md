---
id: TC-FA-MYASSET-UI-117-tabel-assigned-aksi-baris-dan-reaksi-respons
title: "Tabel Assigned: aksi baris menurut keadaan baris dan toast atas respons aksi laporan"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ACT-MYA-01.<aksi>.<huruf>,ACT-MYA-02.<aksi>.<huruf>,ACT-MYA-04.<aksi>.<huruf>", "T-MYA-04", "§1.2#r29", "§1.2#r78", "§1.2#r79", "§1.2#r80", "§1.2#r83", "§1.2#r84", "§4.4#r51", "§7.3#r12", "§7.3#r15", "§9.4.2#r64", "§9.4.3#b10", "§1.2#r86", "§4.3#r9"]
smoke: []
dependsOn: []
trace:
  "ACT-MYA-01.<aksi>.<huruf>,ACT-MYA-02.<aksi>.<huruf>,ACT-MYA-04.<aksi>.<huruf>": [3, 4, 9, 10, 15, 16, 21, 22, 27, 28, 33, 34, 48, 67, 72, 77, 82, 87, 92, 108, 109, 113, 114]
  "T-MYA-04": [3, 4, 9, 10, 15, 16, 21, 22, 27, 28, 33, 34, 67, 72, 77, 82, 87, 92, 108, 109, 113, 114]
  "§1.2#r29": [3, 4, 9, 10, 15, 16, 21, 22, 27, 28, 33, 34]
  "§1.2#r78": [5, 11, 17, 23, 29, 35]
  "§1.2#r79": [15, 16, 21, 22, 27, 28, 33, 34]
  "§1.2#r80": [3, 4, 9, 10]
  "§1.2#r83": [5, 11, 17, 23, 29, 35]
  "§1.2#r84": [5, 11, 17, 23, 29, 35]
  "§4.4#r51": 40
  "§7.3#r12": 48
  "§7.3#r15": [55, 62]
  "§9.4.2#r64": [21, 22, 27, 28]
  "§9.4.3#b10": [5, 11, 17, 23, 29, 35]
  "§1.2#r86": [96, 100, 104]
  "§4.3#r9": [96, 100, 104]
anchor: [95, 99, 103]
coverage:
  web: automated
---

# Tabel Assigned: aksi baris menurut keadaan baris dan toast atas respons aksi laporan

## Prerequisites
- Aktor: Budi Santoso, pengguna yang login sebagai Assignee dan PIC Division atas baris yang tampil.
- Layar awal: halaman My Asset, tab Assigned.
- Komponen: Tabel Assigned (T-MYA-04)
- Data:
  - DU-117-1: Baris Assigned Name `Laptop Dell Latitude 5420 - 21`, Asset ID `LPT-2026-0021`, Status `Waiting for Handover`, Assigned To `Me`, Transaction ID `ASG-2026-0071`, Assigned Date kosong, Assigned By kosong.
  - DU-117-2: Baris Assigned Name `Laptop Dell Latitude 5420 - 22`, Asset ID `LPT-2026-0022`, Status `Waiting for Approval`, Assigned To `Me`, Transaction ID `ASG-2026-0073`, Assigned Date kosong, Assigned By kosong.
  - DU-117-3: Baris Assigned Name `Laptop Dell Latitude 5420 - 1`, Asset ID `LPT-2026-0001`, Status `Assigned`, Assigned To `Me`, Transaction ID `ASG-2026-0031`, Assigned Date `12/10/26, 10:00`, Assigned By `Rina W`.
  - DU-117-4: Baris Assigned Name `Printer HP M404 - 2`, Asset ID `PRN-2026-0002`, Status `Assigned · Reported Damaged`, Assigned To `Finance`, Transaction ID `ASG-2026-0069`, Assigned Date `06/11/26, 09:20`, Assigned By `Agus P`.
  - DU-117-5: Baris Assigned Name `Monitor Dell 24" - 5`, Asset ID `MON-2026-0005`, Status `Assigned · Damaged`, Assigned To `Me`, Transaction ID `ASG-2026-0016`, Assigned Date `22/08/26, 11:00`, Assigned By `Rina W`.
  - DU-117-6: Baris Assigned Name `Monitor Dell 24" - 4`, Asset ID `MON-2026-0004`, Status `Assigned · Reported Missing`, Assigned To `Me`, Transaction ID `ASG-2026-0015`, Assigned Date `20/08/26, 09:30`, Assigned By `Rina W`.
  - DU-117-8: Baris Assigned Name `Printer HP M404 - 3`, Asset ID `PRN-2026-0003`, Status `Assigned · Reported Damaged`, Assigned To `Finance`, Transaction ID `ASG-2026-0074`, Assigned Date `10/11/26, 08:40`, Assigned By `Agus P`, laporan Damaged diajukan pelapor lain.
  - DU-117-9: Baris Assigned Name `Monitor Dell 24" - 6`, Asset ID `MON-2026-0006`, Status `Assigned · Reported Missing`, Assigned To `Finance`, Transaction ID `ASG-2026-0075`, Assigned Date `10/11/26, 08:50`, Assigned By `Agus P`, laporan Missing diajukan pelapor lain.
- Kondisi:
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K1: tabel Assigned memuat DU-117-1 sampai DU-117-6.
  - K2: tabel Assigned memuat DU-117-3; Report Damaged pada baris `Laptop Dell Latitude 5420 - 1` dijawab sukses.
  - K3: tabel Assigned memuat DU-117-3; Report Damaged pada baris `Laptop Dell Latitude 5420 - 1` dijawab error server.
  - K4: tabel Assigned memuat DU-117-3; Report Damaged pada baris `Laptop Dell Latitude 5420 - 1` gagal karena koneksi putus.
  - K5: tabel Assigned memuat DU-117-3; Report Missing pada baris `Laptop Dell Latitude 5420 - 1` dijawab sukses.
  - K6: tabel Assigned memuat DU-117-3; Report Missing pada baris `Laptop Dell Latitude 5420 - 1` dijawab error server.
  - K7: tabel Assigned memuat DU-117-4; Cancel Damage Report pada baris `Printer HP M404 - 2` dijawab sukses.
  - K8: tabel Assigned memuat DU-117-4; Cancel Damage Report pada baris `Printer HP M404 - 2` dijawab error server.
  - K9: tabel Assigned memuat DU-117-6; Cancel Missing Report pada baris `Monitor Dell 24" - 4` dijawab sukses.
  - K10: tabel Assigned memuat DU-117-6; Cancel Missing Report pada baris `Monitor Dell 24" - 4` dijawab error server.
  - K11: tabel Assigned memuat DU-117-3, DU-117-4, dan DU-117-6, dan respons menyatakan level Feature Suite Assignment `None`.
  - K12: tabel Assigned memuat DU-117-8 dan DU-117-9; laporan pada kedua baris diajukan oleh PIC Division sebelumnya, bukan Budi Santoso, yang menjadi PIC Division Finance sesudah Change PIC.

## Test Steps

### Menu baris Waiting for Approval hanya berisi Assignment Log
1. Tampilkan Tabel Assigned dengan kondisi K1
2. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 - 22`
3. Verifikasi menu memuat aksi `Assignment Log`
4. Verifikasi menu tidak memuat aksi `Report Damaged`, `Report Missing`, `Cancel Damage Report`, `Cancel Missing Report`
5. Verifikasi menu tidak memuat aksi `Unassign` maupun permintaan Unassign
6. Tutup menu dengan menekan `Escape`

### Menu baris Waiting for Handover hanya berisi Assignment Log
7. Tampilkan Tabel Assigned dengan kondisi K1
8. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 - 21`
9. Verifikasi menu memuat aksi `Assignment Log`
10. Verifikasi menu tidak memuat aksi `Report Damaged`, `Report Missing`, `Cancel Damage Report`, `Cancel Missing Report`
11. Verifikasi menu tidak memuat aksi `Unassign` maupun permintaan Unassign
12. Tutup menu dengan menekan `Escape`

### Menu baris Assigned tanpa laporan
13. Tampilkan Tabel Assigned dengan kondisi K1
14. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 - 1`
15. Verifikasi menu memuat aksi `Assignment Log`, `Report Damaged`, `Report Missing` dengan urutan itu
16. Verifikasi menu tidak memuat aksi `Cancel Damage Report`, `Cancel Missing Report`
17. Verifikasi menu tidak memuat aksi `Unassign` maupun permintaan Unassign
18. Tutup menu dengan menekan `Escape`

### Menu baris Assigned dengan Damage Report menunggu konfirmasi
19. Tampilkan Tabel Assigned dengan kondisi K1
20. Klik menu `⋯` pada baris `Printer HP M404 - 2`
21. Verifikasi menu memuat aksi `Assignment Log`, `Cancel Damage Report` dengan urutan itu
22. Verifikasi menu tidak memuat aksi `Report Damaged`, `Report Missing`, `Cancel Missing Report`
23. Verifikasi menu tidak memuat aksi `Unassign` maupun permintaan Unassign
24. Tutup menu dengan menekan `Escape`

### Menu baris Assigned dengan record Damaged
25. Tampilkan Tabel Assigned dengan kondisi K1
26. Klik menu `⋯` pada baris `Monitor Dell 24" - 5`
27. Verifikasi menu memuat aksi `Assignment Log`, `Report Missing` dengan urutan itu
28. Verifikasi menu tidak memuat aksi `Report Damaged`, `Cancel Damage Report`, `Cancel Missing Report`
29. Verifikasi menu tidak memuat aksi `Unassign` maupun permintaan Unassign
30. Tutup menu dengan menekan `Escape`

### Menu baris Assigned dengan laporan Missing menunggu konfirmasi
31. Tampilkan Tabel Assigned dengan kondisi K1
32. Klik menu `⋯` pada baris `Monitor Dell 24" - 4`
33. Verifikasi menu memuat aksi `Assignment Log`, `Cancel Missing Report` dengan urutan itu
34. Verifikasi menu tidak memuat aksi `Report Damaged`, `Report Missing`, `Cancel Damage Report`
35. Verifikasi menu tidak memuat aksi `Unassign` maupun permintaan Unassign
36. Tutup menu dengan menekan `Escape`

### Riwayat per aset dibuka lewat Assignment Log
37. Tampilkan Tabel Assigned dengan kondisi K1
38. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 - 1`
39. Klik `Assignment Log`
40. Verifikasi dialog Assignment Log terbuka untuk aset `Laptop Dell Latitude 5420 - 1`
41. Tutup dialog dengan menekan `Escape`

### Toast sukses atas respons Report Damaged berhasil
42. Tampilkan Tabel Assigned dengan kondisi K2
43. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 - 1`
44. Klik `Report Damaged`
45. Unggah Damaged Photo `foto-kerusakan-laptop-1.jpg`
46. Isi What happened dengan `Layar retak setelah terjatuh dari meja kerja`
47. Klik `[Report Damaged]`
48. Verifikasi toast sukses tampil

### Toast error atas respons Report Damaged gagal karena error server
49. Tampilkan Tabel Assigned dengan kondisi K3
50. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 - 1`
51. Klik `Report Damaged`
52. Unggah Damaged Photo `foto-kerusakan-laptop-1.jpg`
53. Isi What happened dengan `Layar retak setelah terjatuh dari meja kerja`
54. Klik `[Report Damaged]`
55. Verifikasi toast error `Error, failed to send report.` tampil

### Toast error atas respons Report Damaged gagal karena koneksi putus
56. Tampilkan Tabel Assigned dengan kondisi K4
57. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 - 1`
58. Klik `Report Damaged`
59. Unggah Damaged Photo `foto-kerusakan-laptop-1.jpg`
60. Isi What happened dengan `Layar retak setelah terjatuh dari meja kerja`
61. Klik `[Report Damaged]`
62. Verifikasi toast error `Connection problem. Please try again.` tampil

### Toast sukses atas respons Report Missing berhasil
63. Tampilkan Tabel Assigned dengan kondisi K5
64. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 - 1`
65. Klik `Report Missing`
66. Klik `[Report Missing]`
67. Verifikasi toast sukses tampil untuk Report Missing

### Toast error atas respons Report Missing gagal karena error server
68. Tampilkan Tabel Assigned dengan kondisi K6
69. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 - 1`
70. Klik `Report Missing`
71. Klik `[Report Missing]`
72. Verifikasi toast error `Error, failed to send report.` tampil untuk Report Missing

### Toast sukses atas respons Cancel Damage Report berhasil
73. Tampilkan Tabel Assigned dengan kondisi K7
74. Klik menu `⋯` pada baris `Printer HP M404 - 2`
75. Klik `Cancel Damage Report`
76. Klik tombol konfirmasi pada dialog `Cancel Report`
77. Verifikasi toast sukses tampil untuk Cancel Damage Report

### Toast error atas respons Cancel Damage Report gagal karena error server
78. Tampilkan Tabel Assigned dengan kondisi K8
79. Klik menu `⋯` pada baris `Printer HP M404 - 2`
80. Klik `Cancel Damage Report`
81. Klik tombol konfirmasi pada dialog `Cancel Report`
82. Verifikasi toast error `Error, failed to cancel report.` tampil untuk Cancel Damage Report

### Toast sukses atas respons Cancel Missing Report berhasil
83. Tampilkan Tabel Assigned dengan kondisi K9
84. Klik menu `⋯` pada baris `Monitor Dell 24" - 4`
85. Klik `Cancel Missing Report`
86. Klik tombol konfirmasi pada dialog `Cancel Report`
87. Verifikasi toast sukses tampil untuk Cancel Missing Report

### Toast error atas respons Cancel Missing Report gagal karena error server
88. Tampilkan Tabel Assigned dengan kondisi K10
89. Klik menu `⋯` pada baris `Monitor Dell 24" - 4`
90. Klik `Cancel Missing Report`
91. Klik tombol konfirmasi pada dialog `Cancel Report`
92. Verifikasi toast error `Error, failed to cancel report.` tampil untuk Cancel Missing Report

### Aksi laporan tidak tampil pada level Assignment None
93. Tampilkan Tabel Assigned dengan kondisi K11
94. Klik menu `⋯` pada baris `Laptop Dell Latitude 5420 - 1`
95. Verifikasi menu baris `Laptop Dell Latitude 5420 - 1` memuat aksi `Assignment Log`
96. Verifikasi aksi `Report Damaged`, `Report Missing`, `Cancel Damage Report`, dan `Cancel Missing Report` tidak tampil pada menu baris `Laptop Dell Latitude 5420 - 1` saat respons menyatakan level `None`
97. Tutup menu dengan menekan `Escape`
98. Klik menu `⋯` pada baris `Printer HP M404 - 2`
99. Verifikasi menu baris `Printer HP M404 - 2` memuat aksi `Assignment Log`
100. Verifikasi aksi `Report Damaged`, `Report Missing`, `Cancel Damage Report`, dan `Cancel Missing Report` tidak tampil pada menu baris `Printer HP M404 - 2` saat respons menyatakan level `None`
101. Tutup menu dengan menekan `Escape`
102. Klik menu `⋯` pada baris `Monitor Dell 24" - 4`
103. Verifikasi menu baris `Monitor Dell 24" - 4` memuat aksi `Assignment Log`
104. Verifikasi aksi `Report Damaged`, `Report Missing`, `Cancel Damage Report`, dan `Cancel Missing Report` tidak tampil pada menu baris `Monitor Dell 24" - 4` saat respons menyatakan level `None`
105. Tutup menu dengan menekan `Escape`

### Menu baris dengan Damage Report dari pelapor lain hanya berisi Assignment Log
106. Tampilkan Tabel Assigned dengan kondisi K12
107. Klik menu `⋯` pada baris `Printer HP M404 - 3`
108. Verifikasi menu memuat aksi `Assignment Log`
109. Verifikasi menu tidak memuat aksi `Report Damaged`, `Report Missing`, `Cancel Damage Report`, `Cancel Missing Report`
110. Tutup menu dengan menekan `Escape`

### Menu baris dengan laporan Missing dari pelapor lain hanya berisi Assignment Log
111. Tampilkan Tabel Assigned dengan kondisi K12
112. Klik menu `⋯` pada baris `Monitor Dell 24" - 6`
113. Verifikasi menu memuat aksi `Assignment Log`
114. Verifikasi menu tidak memuat aksi `Report Damaged`, `Report Missing`, `Cancel Damage Report`, `Cancel Missing Report`
115. Tutup menu dengan menekan `Escape`
