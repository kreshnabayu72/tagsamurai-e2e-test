---
id: TC-FA-DAMAGED-E2E-052-unassign-accept-with-damage-dep-assignment
title: "Unassign bermarker Damaged membuat record Damaged Source Assign return dari Description dan foto Unassign; laporan Waiting for Confirmation atas aset ditugaskan ditautkan tanpa Damage Report kedua dan tetap diputuskan Aktor Damaged, marker Unassigned mengikuti hasilnya"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r50", "§Aturan Logika Modul#r57", "§9.2#b7", "§8.3#r2", "§8.1#r7", "§Aturan Logika Modul#r36", "§Aturan Logika Modul#r44", "§9.7#r3", "T-DMG-01", "§2#b6", "§3#p2", "§4.2.3#p1", "§Aturan Logika Modul#r52", "§Aturan Logika Modul#r49"]
smoke: []
dependsOn:
  - "Assignment: Unassign (status Unassigned bermarker Damaged, form D-ASG-17)"
trace:
  "§Aturan Logika Modul#r50": [20, 21, 40, 41, 42, 71, 73]
  "§Aturan Logika Modul#r57": [35, 38, 44, 46, 49, 50, 53, 56, 58, 61, 67, 68, 71, 84, 89, 90, 94, 95]
  "§9.2#b7": [20, 21]
  "§8.3#r2": [19]
  "§8.1#r7": [19, 20, 21]
  "§Aturan Logika Modul#r36": [35, 38]
  "§Aturan Logika Modul#r44": [10, 35, 49]
  "§9.7#r3": [14, 17, 25, 27]
  "T-DMG-01": [14, 15, 16, 38, 46]
  "§2#b6": [14]
  "§3#p2": [9, 11, 14, 25]
  "§4.2.3#p1": [9]
  "§Aturan Logika Modul#r52": [15]
  "§Aturan Logika Modul#r49": [20, 21, 42]
anchor: []
coverage:
  web: automated
---

# Unassign bermarker Damaged membuat record Damaged Source Assign return dari Description dan foto Unassign; laporan Waiting for Confirmation atas aset ditugaskan ditautkan tanpa Damage Report kedua dan tetap diputuskan Aktor Damaged, marker Unassigned mengikuti hasilnya

## Prerequisites
- Aktor: Total Control, yang bertindak sebagai Aktor Assignment dan sebagai Aktor Damaged.
- Layar awal: halaman Assets, tab `Damaged`.
- Data:
  - DU-052-1: aset Name `Webcam Logitech C920 {runId}`, Group `Head Office`, tanpa TAG, sedang ditugaskan kepada `Citra Maharani {runId}` lewat baris Assignment berstatus `Assigned`, belum punya record Damage.
  - DU-052-2: aset Name `Tablet Lenovo Tab M10 {runId}`, Group `Head Office`, tanpa TAG, sedang ditugaskan kepada `Dani Ramadhan {runId}` lewat baris Assignment berstatus `Assigned`, dengan record `Waiting for Confirmation` Source `Reported by holder` dari laporan pemegang dengan What happened `Layar tablet muncul bintik hitam dan sentuhan lambat`.
  - DU-052-5: aset Name `Monitor Dell P2422H {runId}`, Group `Head Office`, tanpa TAG, sedang ditugaskan kepada `Eka Pratama {runId}` lewat baris Assignment berstatus `Assigned`, dengan record `Waiting for Confirmation` Source `Reported by holder` dari laporan pemegang dengan What happened `Panel monitor berkedip dan muncul garis vertikal`.
  - DU-052-6: aset Name `Printer Epson L3250 {runId}`, Group `Head Office`, tanpa TAG, sedang ditugaskan kepada `Fajar Nugroho {runId}` lewat baris Assignment berstatus `Assigned`, dengan record `Waiting for Confirmation` Source `Reported by holder` dari laporan pemegang dengan What happened `Hasil cetak bergaris dan tinta bocor`.

## Test Steps

### Unassign bermarker Damaged atas aset tanpa record membuat record Damaged Source Assign return
1. Catat jumlah pada badge tab `Damaged` sebagai jumlah awal
2. Buka halaman Assignment
3. Ketik Search `Webcam Logitech C920 {runId}`, tekan Enter
4. Klik `Unassign` pada baris Assignment aset `Webcam Logitech C920 {runId}`
5. Tandai aset rusak pada form Unassign
6. Isi Description `Lensa webcam tergores dan gambar buram`
7. Pilih foto Unassign `webcam-lensa-tergores.jpg`
8. Submit form Unassign
9. Verifikasi dialog `Report Damaged` tidak tampil
10. Verifikasi baris Assignment aset `Webcam Logitech C920 {runId}` berstatus `Unassigned`
11. Verifikasi baris Assignment aset `Webcam Logitech C920 {runId}` memuat penanda `Damaged`
12. Buka halaman Assets, tab `Damaged`
13. Ketik Search `Webcam Logitech C920 {runId}`, tekan Enter
14. Verifikasi baris aset `Webcam Logitech C920 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`, tanpa Confirm
15. Verifikasi kolom Source pada baris itu `Assign return`
16. Verifikasi kolom Last Holder pada baris itu terisi nama pemegang saat Unassign, dalam bentuk nama depan dan inisial nama belakang
17. Verifikasi badge tab `Damaged` bertambah satu dari jumlah awal
18. Klik nama aset pada baris aset `Webcam Logitech C920 {runId}`
19. Verifikasi node `Reported damaged by [Reporter Name]` tampil atas nama Aktor Assignment yang melakukan Unassign
20. Verifikasi baris detail What happened pada node itu `Lensa webcam tergores dan gambar buram`
21. Verifikasi baris detail Damaged Photo pada node itu memuat foto Unassign `webcam-lensa-tergores.jpg`
22. Tutup dialog Damage Log

### Status global aset Damaged sejak Unassign bermarker Damaged
23. Buka halaman Assets, tab `Assets`
24. Ketik Search `Webcam Logitech C920 {runId}`, tekan Enter
25. Verifikasi status global aset `Damaged` pada baris `Webcam Logitech C920 {runId}`
26. Klik nama aset pada baris aset `Webcam Logitech C920 {runId}` untuk membuka Asset Detail
27. Verifikasi status global aset `Damaged` tampil pada Asset Detail

### Unassign atas aset ber-record Waiting for Confirmation menautkan laporan tanpa Damage Report kedua
28. Buka halaman Assignment
29. Ketik Search `Tablet Lenovo Tab M10 {runId}`, tekan Enter
30. Klik `Unassign` pada baris Assignment aset `Tablet Lenovo Tab M10 {runId}`
31. Tandai aset rusak pada form Unassign
32. Isi Description `Layar tablet bintik hitam seperti yang dilaporkan pemegang`
33. Pilih foto Unassign `tablet-layar-bintik.jpg`
34. Submit form Unassign
35. Verifikasi baris Assignment aset `Tablet Lenovo Tab M10 {runId}` berstatus `Unassigned`
36. Buka halaman Assets, tab `Damaged`
37. Ketik Search `Tablet Lenovo Tab M10 {runId}`, tekan Enter
38. Verifikasi tepat satu baris aset `Tablet Lenovo Tab M10 {runId}` tampil di sub-tab `Active` dengan Status `Waiting for Confirmation`
39. Klik nama aset pada baris aset `Tablet Lenovo Tab M10 {runId}`
40. Verifikasi timeline dialog Damage Log memuat tepat satu node, yaitu `Reported damaged by [Reporter Name]`
41. Verifikasi baris detail What happened pada node itu tetap `Layar tablet muncul bintik hitam dan sentuhan lambat`
42. Verifikasi dialog Damage Log memuat foto Unassign `tablet-layar-bintik.jpg` sebagai Damaged Photo record itu

### Aktor Damaged memutuskan laporan dan marker Unassigned mengikuti hasilnya
43. Klik `[Confirm]` pada footer dialog Damage Log
44. Verifikasi node `Report confirmed by [Admin Name]` tampil di dialog Damage Log
45. Tutup dialog Damage Log
46. Verifikasi Status baris aset `Tablet Lenovo Tab M10 {runId}` `Damaged`
47. Buka halaman Assignment
48. Ketik Search `Tablet Lenovo Tab M10 {runId}`, tekan Enter
49. Verifikasi baris Assignment aset `Tablet Lenovo Tab M10 {runId}` tetap berstatus `Unassigned`
50. Verifikasi baris Assignment aset `Tablet Lenovo Tab M10 {runId}` memuat penanda `Damaged`

### Keputusan Aktor Damaged sebelum Unassign: aset tetap Assigned dan marker mengikuti record yang sudah diputuskan
51. Buka halaman Assets, tab `Damaged`
52. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
53. Verifikasi baris aset `Monitor Dell P2422H {runId}` tampil di sub-tab `Active` dengan Status `Waiting for Confirmation`
54. Klik nama aset pada baris aset `Monitor Dell P2422H {runId}`
55. Klik `[Confirm]` pada footer dialog Damage Log
56. Verifikasi node `Report confirmed by [Admin Name]` tampil di dialog Damage Log
57. Tutup dialog Damage Log
58. Verifikasi Status baris aset `Monitor Dell P2422H {runId}` `Damaged`
59. Buka halaman Assignment
60. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
61. Verifikasi baris Assignment aset `Monitor Dell P2422H {runId}` masih berstatus `Assigned`
62. Klik `Unassign` pada baris Assignment aset `Monitor Dell P2422H {runId}`
63. Tandai aset rusak pada form Unassign
64. Isi Description `Panel monitor berkedip seperti yang dilaporkan pemegang`
65. Pilih foto Unassign `monitor-panel-berkedip.jpg`
66. Submit form Unassign
67. Verifikasi baris Assignment aset `Monitor Dell P2422H {runId}` berstatus `Unassigned`
68. Verifikasi baris Assignment aset `Monitor Dell P2422H {runId}` memuat penanda `Damaged`
69. Buka halaman Assets, tab `Damaged`
70. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
71. Verifikasi tepat satu baris aset `Monitor Dell P2422H {runId}` tampil di sub-tab `Active` dengan Status `Damaged`
72. Klik nama aset pada baris aset `Monitor Dell P2422H {runId}`
73. Verifikasi timeline dialog Damage Log memuat tepat satu node `Reported damaged by [Reporter Name]`
74. Tutup dialog Damage Log

### Keputusan Aktor Damaged sesudah Unassign: Reject laporan memutuskan record dan marker mengikuti hasilnya
75. Buka halaman Assignment
76. Ketik Search `Printer Epson L3250 {runId}`, tekan Enter
77. Klik `Unassign` pada baris Assignment aset `Printer Epson L3250 {runId}`
78. Tandai aset rusak pada form Unassign
79. Isi Description `Hasil cetak bergaris seperti yang dilaporkan pemegang`
80. Pilih foto Unassign `printer-hasil-cetak-bergaris.jpg`
81. Submit form Unassign
82. Buka halaman Assets, tab `Damaged`
83. Ketik Search `Printer Epson L3250 {runId}`, tekan Enter
84. Verifikasi baris aset `Printer Epson L3250 {runId}` tampil di sub-tab `Active` dengan Status `Waiting for Confirmation`
85. Klik nama aset pada baris aset `Printer Epson L3250 {runId}`
86. Klik `[Reject]` pada footer dialog Damage Log
87. Isi Reason `Kerusakan tidak terbukti setelah pengecekan teknisi`
88. Klik `[Reject]` pada dialog `Reject Report`
89. Verifikasi badge status record pada dialog Damage Log `Rejected`
90. Verifikasi node `Report rejected by [Admin Name]` tampil di dialog Damage Log
91. Tutup dialog Damage Log
92. Buka halaman Assignment
93. Ketik Search `Printer Epson L3250 {runId}`, tekan Enter
94. Verifikasi baris Assignment aset `Printer Epson L3250 {runId}` tetap berstatus `Unassigned`
95. Verifikasi baris Assignment aset `Printer Epson L3250 {runId}` tidak memuat penanda `Damaged`
