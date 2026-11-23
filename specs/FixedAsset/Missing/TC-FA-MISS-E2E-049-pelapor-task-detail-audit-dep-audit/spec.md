---
id: TC-FA-MISS-E2E-049-pelapor-task-detail-audit-dep-audit
title: "Pelapor dari Task Detail Audit tanpa hak Aktor Missing (Asset Admin sub-tab Audit atau Staff Auditor) melapor: record Waiting for Confirmation Source Audit dengan status global aset langsung Missing, lalu Cancel my report membatalkan laporan, status global aset dihitung ulang, dan baris Audit kembali Pending"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r71", "§2.1#b5", "§4.8#r8", "§9.2#b37", "§9.4.2#r37", "§9.4.2#r38", "§9.4.4#r23", "§1.2#r57", "§3#p4", "§4.2.4#p8", "§7.2#r18", "§2.1#b1", "§2.1#b2", "§4.8#b1", "§2#b2", "§2.1#r8", "§9.3#b1", "§9.2#r1", "§11#r9", "§8.2#p5", "§1.2#r58", "§4.8#r2", "§8.1#r7"]
smoke: []
dependsOn: ["Audit: Task Detail Audit (Report Missing, Cancel my report)"]
trace:
  "§1.2#r71": [10, 19, 32, 70, 71, 76, 80]
  "§2.1#b5": [5, 27, 40]
  "§4.8#r8": [5, 23, 27, 59, 63]
  "§9.2#b37": [40, 47, 54]
  "§9.4.2#r37": [10, 11, 19, 32, 33, 77, 81]
  "§9.4.2#r38": [23, 38, 41, 47, 54]
  "§9.4.4#r23": [49]
  "§1.2#r57": [40, 47, 87]
  "§3#p4": [19, 47, 54]
  "§4.2.4#p8": [38]
  "§7.2#r18": [38, 40, 87]
  "§2.1#b1": [10, 32]
  "§2.1#b2": [10, 32]
  "§4.8#b1": [10, 32]
  "§2#b2": [10, 12, 34, 78, 82]
  "§2.1#r8": [5, 40]
  "§9.3#b1": [5, 23, 40]
  "§9.2#r1": [10, 32]
  "§11#r9": [10, 32]
  "§8.2#p5": [14]
  "§1.2#r58": [92]
  "§4.8#r2": [5, 27, 70]
  "§8.1#r7": [14]
anchor: [22, 58, 62]
coverage:
  web: automated
---

# Pelapor dari Task Detail Audit tanpa hak Aktor Missing (Asset Admin sub-tab Audit atau Staff Auditor) melapor: record Waiting for Confirmation Source Audit dengan status global aset langsung Missing, lalu Cancel my report membatalkan laporan, status global aset dihitung ulang, dan baris Audit kembali Pending

## Prerequisites
- Aktor: Asset Admin sub-tab Audit `Lia Kartika {runId}` tanpa hak Aktor Missing pada Group `Warehouse`. Aktor lain: Staff Auditor `Bayu Saputra {runId}` tanpa hak Aktor Missing pada Group `Warehouse`, dan Total Control `Rina W`.
- Layar awal: Audit.
- Data:
  - DU-049-1: Task Audit `Audit Gudang Barat {runId}` yang memuat dua item berstatus `Not found`: `Rak Server APC {runId}` dan `Meja Kerja Lipat {runId}`.
  - DU-049-2: Asset `Rak Server APC {runId}`, Group `Warehouse`, Asset Status `Normal`, tidak dipegang siapa pun, tanpa record Missing.
  - DU-049-3: Asset `Meja Kerja Lipat {runId}`, Group `Warehouse`, Asset Status `Normal`, tidak dipegang siapa pun, tanpa record Missing.
  - DU-049-4: Pengguna `Lia Kartika {runId}`, Asset Admin sub-tab Audit tanpa hak Aktor Missing pada Group `Warehouse`.
  - DU-049-5: Pengguna `Bayu Saputra {runId}`, Staff Auditor tanpa hak Aktor Missing pada Group `Warehouse`.
  - DU-049-6: Pengguna `Rina W`, Total Control.
  - DU-049-7: What happened `Rak server tidak ada di ruang server saat penghitungan fisik`.
  - DU-049-8: What happened `Meja kerja lipat tidak ada di area gudang barat saat penghitungan fisik`.
  - DU-049-9: Task Audit `Audit Gudang Timur {runId}` yang memuat dua item berstatus `Not found`: `Kabinet Arsip Besi {runId}` dan `Lemari Display Kaca {runId}`.
  - DU-049-10: Asset `Kabinet Arsip Besi {runId}`, Group `Warehouse`, Asset Status `Normal`, Tagging `Tag Reported`, tidak dipegang siapa pun, tanpa record Missing.
  - DU-049-11: Asset `Lemari Display Kaca {runId}`, Group `Warehouse`, Asset Status `Normal`, tidak dipegang siapa pun, tanpa record Missing.
  - DU-049-12: What happened `Kabinet dan lemari display tidak ada di area gudang timur saat penghitungan fisik`.
- Kondisi:
  - Akun `Lia Kartika {runId}`, `Bayu Saputra {runId}`, dan `Rina W` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Asset Admin sub-tab Audit melapor dari Task Detail Audit
1. Buka Task Detail Audit `Audit Gudang Barat {runId}`
2. Klik `Report Missing` pada item `Rak Server APC {runId}`
3. Isi What happened `Rak server tidak ada di ruang server saat penghitungan fisik`
4. Klik `[Report Missing]` pada dialog
5. Verifikasi aksi `Cancel my report` tampil pada item `Rak Server APC {runId}`

### Laporan Asset Admin berstatus Waiting for Confirmation dan status global aset langsung Missing
6. Masuk sebagai `Rina W`
7. Buka halaman `Assets`
8. Klik tab `Missing`
9. Ketik Search `Rak Server APC {runId}`, tekan Enter
10. Verifikasi baris `Rak Server APC {runId}` berstatus `Waiting for Confirmation`
11. Verifikasi kolom Source pada baris itu `Audit`
12. Verifikasi kolom Reported By pada baris itu `Lia Kartika {runId}`
13. Klik `Rak Server APC {runId}` pada kolom Name
14. Verifikasi dialog Missing Log memuat node `Reported missing by` oleh `Lia Kartika {runId}` dengan What happened `Rak server tidak ada di ruang server saat penghitungan fisik` dan status `Waiting for Confirmation`
15. Tutup dialog Missing Log dengan `✕`
16. Klik tab `Assets`
17. Ketik Search `Rak Server APC {runId}`, tekan Enter
18. Klik `Rak Server APC {runId}` pada kolom Name
19. Verifikasi Asset Status pada Asset Detail `Missing`

### Staff Auditor melapor dan tidak memiliki aksi atas laporan pelapor lain
20. Masuk sebagai `Bayu Saputra {runId}`
21. Buka Task Detail Audit `Audit Gudang Barat {runId}`
22. Verifikasi item `Meja Kerja Lipat {runId}` berstatus `Not found`
23. Verifikasi aksi `Cancel my report` tidak tampil pada item `Rak Server APC {runId}` bagi `Bayu Saputra {runId}`, karena laporan itu milik pelapor lain
24. Klik `Report Missing` pada item `Meja Kerja Lipat {runId}`
25. Isi What happened `Meja kerja lipat tidak ada di area gudang barat saat penghitungan fisik`
26. Klik `[Report Missing]` pada dialog
27. Verifikasi aksi `Cancel my report` tampil pada item `Meja Kerja Lipat {runId}`

### Laporan Staff Auditor berstatus Waiting for Confirmation
28. Masuk sebagai `Rina W`
29. Buka halaman `Assets`
30. Klik tab `Missing`
31. Ketik Search `Meja Kerja Lipat {runId}`, tekan Enter
32. Verifikasi baris `Meja Kerja Lipat {runId}` berstatus `Waiting for Confirmation`
33. Verifikasi kolom Source pada baris itu `Audit`
34. Verifikasi kolom Reported By pada baris itu `Bayu Saputra {runId}`

### Asset Admin membatalkan laporannya lewat Cancel my report
35. Masuk sebagai `Lia Kartika {runId}`
36. Buka Task Detail Audit `Audit Gudang Barat {runId}`
37. Klik `Cancel my report` pada item `Rak Server APC {runId}`
38. Verifikasi dialog `Cancel Report` memuat bullet `Rak Server APC {runId}` dan pertanyaan `Are you sure you want to cancel it?`
39. Klik `[Cancel Report]` pada dialog
40. Verifikasi toast `Success, report has been canceled.` tampil
41. Verifikasi baris Audit `Rak Server APC {runId}` kembali `Pending`

### Record Canceled dan status global aset dihitung ulang
42. Masuk sebagai `Rina W`
43. Buka halaman `Assets`
44. Klik tab `Missing`
45. Klik sub-tab `History`
46. Ketik Search `Rak Server APC {runId}`, tekan Enter
47. Verifikasi baris `Rak Server APC {runId}` berstatus `Canceled`
48. Klik `Rak Server APC {runId}` pada kolom Name
49. Verifikasi dialog Missing Log memuat node `Report canceled by` oleh `Lia Kartika {runId}`
50. Tutup dialog Missing Log dengan `✕`
51. Klik tab `Assets`
52. Ketik Search `Rak Server APC {runId}`, tekan Enter
53. Klik `Rak Server APC {runId}` pada kolom Name
54. Verifikasi Asset Status pada Asset Detail `Normal`

### Cancel my report tidak tampil sesudah laporan bukan lagi Waiting for Confirmation
55. Rina W melakukan Confirm atas laporan `Meja Kerja Lipat {runId}`
56. Masuk sebagai `Lia Kartika {runId}`
57. Buka Task Detail Audit `Audit Gudang Barat {runId}`
58. Verifikasi baris Audit `Rak Server APC {runId}` `Pending`
59. Verifikasi aksi `Cancel my report` tidak tampil pada item `Rak Server APC {runId}` sesudah laporannya Canceled
60. Masuk sebagai `Bayu Saputra {runId}`
61. Buka Task Detail Audit `Audit Gudang Barat {runId}`
62. Verifikasi baris Audit `Rak Server APC {runId}` `Pending`
63. Verifikasi aksi `Cancel my report` tidak tampil pada item `Meja Kerja Lipat {runId}` sesudah laporannya dikonfirmasi

### Staff Auditor melapor lewat Bulk Report Missing
64. Buka Task Detail Audit `Audit Gudang Timur {runId}`
65. Centang item `Kabinet Arsip Besi {runId}`
66. Centang item `Lemari Display Kaca {runId}`
67. Klik `Bulk Report Missing`
68. Isi What happened `Kabinet dan lemari display tidak ada di area gudang timur saat penghitungan fisik`
69. Klik `[Report Missing]` pada dialog
70. Verifikasi aksi `Cancel my report` tampil pada item `Kabinet Arsip Besi {runId}`
71. Verifikasi aksi `Cancel my report` tampil pada item `Lemari Display Kaca {runId}`
72. Masuk sebagai `Rina W`
73. Buka halaman `Assets`
74. Klik tab `Missing`
75. Ketik Search `Kabinet Arsip Besi {runId}`, tekan Enter
76. Verifikasi baris `Kabinet Arsip Besi {runId}` berstatus `Waiting for Confirmation`
77. Verifikasi kolom Source pada baris itu `Audit`
78. Verifikasi kolom Reported By pada baris itu `Bayu Saputra {runId}`
79. Ganti isi kotak search dengan `Lemari Display Kaca {runId}`, tekan Enter
80. Verifikasi baris `Lemari Display Kaca {runId}` berstatus `Waiting for Confirmation`
81. Verifikasi kolom Source pada baris itu `Audit`
82. Verifikasi kolom Reported By pada baris itu `Bayu Saputra {runId}`

### Status global aset bertagging Tag Reported dihitung ulang sesudah Cancel my report
83. Masuk sebagai `Bayu Saputra {runId}`
84. Buka Task Detail Audit `Audit Gudang Timur {runId}`
85. Klik `Cancel my report` pada item `Kabinet Arsip Besi {runId}`
86. Klik `[Cancel Report]` pada dialog
87. Verifikasi toast `Success, report has been canceled.` tampil
88. Masuk sebagai `Rina W`
89. Buka halaman `Assets`
90. Ketik Search `Kabinet Arsip Besi {runId}`, tekan Enter
91. Klik `Kabinet Arsip Besi {runId}` pada kolom Name
92. Verifikasi Asset Status pada Asset Detail `TAG Reported`
