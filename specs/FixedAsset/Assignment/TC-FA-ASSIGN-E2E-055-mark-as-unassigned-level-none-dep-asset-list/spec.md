---
id: TC-FA-ASSIGN-E2E-055-mark-as-unassigned-level-none-dep-asset-list
title: "Mark as Unassigned pada level None dari Asset List dan Asset Detail"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [TS-ASG-35, "§4.8#r13", EC-ASG-101, EC-ASG-102, EC-ASG-103, EC-ASG-104, EC-ASG-110, EC-ASG-111, "§9.6#r13"]
smoke: []
dependsOn: ["Asset List: aksi baris dan bulk Mark as Unassigned"]
trace:
  TS-ASG-35: [8, 37, 48, 63]
  "§4.8#r13": [4, 34, 52, 55, 84, 87, 91, 95]
  EC-ASG-101: [6, 8, 9, 12, 80]
  EC-ASG-102: [21, 30]
  EC-ASG-103: [45, 46, 49]
  EC-ASG-104: 2
  EC-ASG-110: [52, 53, 55, 84, 85, 87]
  EC-ASG-111: [61, 64, 69, 70]
  "§9.6#r13": [8, 12, 21, 38, 48, 49, 80]
anchor: []
coverage:
  web: automated
---

# Mark as Unassigned pada level None dari Asset List dan Asset Detail

## Prerequisites
- Aktor: Aktor Assignment (Total Control `Fajar Nugroho {runId}`, DU-055-2); pada blok terakhir juga Group Manager `Rudi Hartono {runId}` (DU-055-19) dan Asset Admin `Dewi Anggraini {runId}` (DU-055-20).
- Layar awal: Asset List.
- Data:
  - DU-055-1: Spec ini memakai entitas khusus `Entitas Wind-down {runId}` yang tidak dipakai spec lain, dengan Feature Suite Assignment level `None`.
  - DU-055-2: Karyawan `Fajar Nugroho {runId}`, role Total Control, Status `Active`.
  - DU-055-3: Karyawan `Sari Dewi {runId}`, Status `Active`, Assignee aset DU-055-5, DU-055-6, DU-055-7, DU-055-8, DU-055-21, dan DU-055-22.
  - DU-055-4: Karyawan `Budi Santoso {runId}`, Status `Active`, Assignee aset DU-055-9, DU-055-10, dan DU-055-14.
  - DU-055-5: Aset `Laptop Asus Vivobook 14 {runId}`, Custody `Assigned` kepada `Sari Dewi {runId}`.
  - DU-055-6: Aset `Kamera Sony ZV-E10 {runId}`, Custody `Assigned` kepada `Sari Dewi {runId}`.
  - DU-055-7: Aset `Drone DJI Mini 3 {runId}`, Custody `Assigned` kepada `Sari Dewi {runId}`.
  - DU-055-8: Aset `Handheld Zebra TC21 {runId}`, Custody `Assigned` kepada `Sari Dewi {runId}`.
  - DU-055-9: Aset `Proyektor BenQ MH535 {runId}`, Custody `Assigned` kepada `Budi Santoso {runId}`.
  - DU-055-10: Aset `Speaker JBL Charge 5 {runId}`, Custody `Assigned` kepada `Budi Santoso {runId}`.
  - DU-055-11: Aset `Printer Canon G3010 {runId}`, Custody `Available`.
  - DU-055-12: Aset `Laptop Dell XPS 13 {runId}`, Custody `Assigned` kepada `Fajar Nugroho {runId}`.
  - DU-055-13: Aset `Tablet Lenovo Tab M10 {runId}`, Custody `Assigned` kepada `Fajar Nugroho {runId}`.
  - DU-055-14: Aset `Monitor LG 27UL500 {runId}`, Custody `Assigned` kepada `Budi Santoso {runId}`.
  - DU-055-15: Division `Tim Gudang {runId}` dengan PIC `Fajar Nugroho {runId}`.
  - DU-055-16: Aset `Forklift Toyota 8FD {runId}`, Custody `Assigned` kepada Division `Tim Gudang {runId}`.
  - DU-055-17: Aset `Scanner Epson DS-530 {runId}`, Custody `Assigned` kepada `Sari Dewi {runId}`.
  - DU-055-18: Group `Gudang Pusat {runId}`.
  - DU-055-19: Karyawan `Rudi Hartono {runId}`, role Group Manager dengan Group binaan `Gudang Pusat {runId}`, Status `Active`.
  - DU-055-20: Karyawan `Dewi Anggraini {runId}`, role Asset Admin dengan cakupan Group `Gudang Pusat {runId}`, Status `Active`.
  - DU-055-21: Aset `Rak Server Dell R740 {runId}`, Group `Gudang Pusat {runId}`, Custody `Assigned` kepada `Sari Dewi {runId}`.
  - DU-055-22: Aset `Switch Cisco CBS350 {runId}`, Group `Gudang Pusat {runId}`, Custody `Assigned` kepada `Sari Dewi {runId}`.
- Kondisi:
  - Akun Group Manager dan Asset Admin aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Mark as Unassigned satu aset dengan hasil Unassigned
1. Ketik Search `Laptop Asus Vivobook 14 {runId}`, tekan Enter
2. Verifikasi baris `Laptop Asus Vivobook 14 {runId}` memiliki Custody `Assigned` sebelum diproses
3. Klik `⋯` pada baris `Laptop Asus Vivobook 14 {runId}`
4. Verifikasi opsi `Mark as Unassigned` tampil dan aktif pada baris aset Assigned
5. Klik `Mark as Unassigned`
6. Verifikasi dialog `Mark as Unassigned` memuat Assignee `Sari Dewi {runId}` dan pilihan hasil `Unassigned`, `Missing`, dan `Damaged` dengan `Unassigned` terpilih bawaan
7. Klik `[Mark as Unassigned]` pada dialog
8. Verifikasi toast `Success, asset has been marked as unassigned.`
9. Verifikasi baris `Laptop Asus Vivobook 14 {runId}` memiliki Custody `Available`
10. Buka halaman detail aset `Laptop Asus Vivobook 14 {runId}`
11. Buka tab `Transaction log`
12. Verifikasi baris log terbaru berstatus `Unassigned` untuk Assignee `Sari Dewi {runId}`

### Mark as Unassigned dengan hasil Missing
13. Buka halaman Asset List
14. Ketik Search `Kamera Sony ZV-E10 {runId}`, tekan Enter
15. Klik `⋯` pada baris `Kamera Sony ZV-E10 {runId}`
16. Klik `Mark as Unassigned`
17. Pilih hasil `Missing` pada dialog `Mark as Unassigned`
18. Klik `[Mark as Unassigned]` pada dialog
19. Buka halaman detail aset `Kamera Sony ZV-E10 {runId}`
20. Buka tab `Transaction log`
21. Verifikasi baris log terbaru berstatus `Unassigned` dengan marker `Missing`

### Mark as Unassigned dengan hasil Damaged
22. Buka halaman Asset List
23. Ketik Search `Drone DJI Mini 3 {runId}`, tekan Enter
24. Klik `⋯` pada baris `Drone DJI Mini 3 {runId}`
25. Klik `Mark as Unassigned`
26. Pilih hasil `Damaged` pada dialog `Mark as Unassigned`
27. Klik `[Mark as Unassigned]` pada dialog
28. Buka halaman detail aset `Drone DJI Mini 3 {runId}`
29. Buka tab `Transaction log`
30. Verifikasi baris log terbaru berstatus `Unassigned` dengan marker `Damaged`

### Mark as Unassigned dari header halaman detail aset
31. Buka halaman Asset List
32. Ketik Search `Handheld Zebra TC21 {runId}`, tekan Enter
33. Buka halaman detail aset `Handheld Zebra TC21 {runId}`
34. Verifikasi tombol `Mark as Unassigned` tampil dan aktif di header halaman detail aset
35. Klik `Mark as Unassigned` di header halaman detail aset
36. Klik `[Mark as Unassigned]` pada dialog
37. Verifikasi toast `Success, asset has been marked as unassigned.` tampil setelah aksi dari header halaman detail aset
38. Verifikasi Custody aset `Handheld Zebra TC21 {runId}` menjadi `Available`

### Bulk Mark as Unassigned melewati aset yang bukan Assigned
39. Buka halaman Asset List
40. Ketik Search `{runId}`, tekan Enter
41. Centang baris `Proyektor BenQ MH535 {runId}`
42. Centang baris `Speaker JBL Charge 5 {runId}`
43. Centang baris `Printer Canon G3010 {runId}`
44. Klik `Mark as Unassigned` pada menu aksi bulk
45. Verifikasi dialog memuat `{N} assets skipped because they aren't assigned.` dengan `{N}` bernilai `1`
46. Verifikasi dialog bulk tidak menyediakan pilihan hasil `Missing` dan `Damaged`
47. Klik `[Mark as Unassigned]` pada dialog
48. Verifikasi toast `Success, 2 assets have been marked as unassigned.`
49. Verifikasi baris `Printer Canon G3010 {runId}` tetap memiliki Custody `Available`

### Aset milik Aktor sendiri tidak dapat di-Mark as Unassigned
50. Ketik Search `Laptop Dell XPS 13 {runId}`, tekan Enter
51. Klik `⋯` pada baris `Laptop Dell XPS 13 {runId}`
52. Verifikasi opsi `Mark as Unassigned` tampil dan disabled pada baris `Laptop Dell XPS 13 {runId}` dengan alasan `You can't hand over or receive your own assignment.` tersampaikan
53. Verifikasi baris `Laptop Dell XPS 13 {runId}` tetap memiliki Custody `Assigned`
54. Buka halaman detail aset `Laptop Dell XPS 13 {runId}`
55. Verifikasi tombol `Mark as Unassigned` tampil dan disabled di header halaman detail aset dengan alasan `You can't hand over or receive your own assignment.` tersampaikan

### Bulk campuran aset milik Aktor sendiri dan aset lain
56. Buka halaman Asset List
57. Ketik Search `{runId}`, tekan Enter
58. Centang baris `Laptop Dell XPS 13 {runId}`
59. Centang baris `Monitor LG 27UL500 {runId}`
60. Klik `Mark as Unassigned` pada menu aksi bulk
61. Verifikasi dialog memuat `{N} assets skipped because they're yours.` dengan `{N}` bernilai `1`
62. Klik `[Mark as Unassigned]` pada dialog
63. Verifikasi toast `Success, asset has been marked as unassigned.` tampil untuk aset yang diproses
64. Verifikasi baris `Monitor LG 27UL500 {runId}` memiliki Custody `Available` dan baris `Laptop Dell XPS 13 {runId}` tetap memiliki Custody `Assigned`

### Bulk dengan semua aset milik Aktor sendiri ditolak
65. Ketik Search `{runId}`, tekan Enter
66. Centang baris `Laptop Dell XPS 13 {runId}`
67. Centang baris `Tablet Lenovo Tab M10 {runId}`
68. Klik `Mark as Unassigned` pada menu aksi bulk
69. Verifikasi toast `Error, you can't hand over or receive your own assignment.` tampil tanpa dialog `Mark as Unassigned`
70. Verifikasi baris `Tablet Lenovo Tab M10 {runId}` tetap memiliki Custody `Assigned`

### Assignment Log mencatat Mark as Unassigned
71. Buka halaman Asset List
72. Ketik Search `Scanner Epson DS-530 {runId}`, tekan Enter
73. Klik `⋯` pada baris `Scanner Epson DS-530 {runId}`
74. Klik `Mark as Unassigned`
75. Klik `[Mark as Unassigned]` pada dialog
76. Buka halaman detail aset `Scanner Epson DS-530 {runId}`
77. Buka tab `Transaction log`
78. Klik Transaction ID pada baris log terbaru untuk membuka Assignment Detail
79. Klik row action `Assignment Log` pada baris aset `Scanner Epson DS-530 {runId}`
80. Verifikasi node Assignment Log berjudul `Unassigned by` dengan pelaku `Fajar Nugroho {runId}` tampil dengan penanda `Plan change` dan Outcome `Unassigned`

### Aset yang Aktor menjadi PIC Division-nya tidak dapat di-Mark as Unassigned
81. Buka halaman Asset List
82. Ketik Search `Forklift Toyota 8FD {runId}`, tekan Enter
83. Klik `⋯` pada baris `Forklift Toyota 8FD {runId}`
84. Verifikasi opsi `Mark as Unassigned` tampil dan disabled pada baris `Forklift Toyota 8FD {runId}` dengan alasan `You're the PIC for this division. Ask another admin.` tersampaikan
85. Verifikasi baris `Forklift Toyota 8FD {runId}` tetap memiliki Custody `Assigned`
86. Buka halaman detail aset `Forklift Toyota 8FD {runId}`
87. Verifikasi tombol `Mark as Unassigned` tampil dan disabled di header halaman detail aset dengan alasan `You're the PIC for this division. Ask another admin.` tersampaikan

### Mark as Unassigned tampil bagi Group Manager dan Asset Admin pada Group-nya
88. Group Manager `Rudi Hartono {runId}`: Buka halaman Asset List
89. Ketik Search `Rak Server Dell R740 {runId}`, tekan Enter
90. Klik `⋯` pada baris `Rak Server Dell R740 {runId}`
91. Verifikasi opsi `Mark as Unassigned` tampil dan aktif pada baris `Rak Server Dell R740 {runId}`
92. Asset Admin `Dewi Anggraini {runId}`: Buka halaman Asset List
93. Ketik Search `Switch Cisco CBS350 {runId}`, tekan Enter
94. Klik `⋯` pada baris `Switch Cisco CBS350 {runId}`
95. Verifikasi opsi `Mark as Unassigned` tampil dan aktif pada baris `Switch Cisco CBS350 {runId}`
