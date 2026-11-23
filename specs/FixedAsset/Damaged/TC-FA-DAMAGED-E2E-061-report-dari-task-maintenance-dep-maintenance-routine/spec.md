---
id: TC-FA-DAMAGED-E2E-061-report-dari-task-maintenance-dep-maintenance-routine
title: "Pelapor dari Task Maintenance tanpa hak Aktor Damaged melapor rusak: What happened terisi dari indicator out of standard dan dapat diedit, record Waiting for Confirmation Source Maintenance dengan penanda Damage reported tanpa mengubah status global aset, Damage Log dapat dibuka pelapor, dan Cancel my report membatalkan laporan tanpa mengubah task"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.4.2#r38", "§9.4.2#r39", "§9.4.2#r41", "§9.4.2#r42", "§2.1#b5", "§2.1#b3", "§4.8#r9", "§4.2.4#r15", "§3#p5", "§Aturan Logika Modul#r32", "§Aturan Logika Modul#r58", "§Aturan Logika Modul#r47", "§Aturan Logika Modul#r55", "§4.2.4#p8", "EC-DMG-22", "§2#b7", "§2#b6", "FI-DMG-05", "§2.1#b1", "§2.1#b2", "§3#p2", "§9.11#r1", "§2.1#r2", "§2.1#r5", "§4.2.3#p1", "§4.8#r3", "§9.4.3#b6"]
smoke: []
dependsOn:
  - "Maintenance Routine: Task Maintenance (tombol Report Damaged, indicator out of standard, Cancel my report, penanda Damage reported)"
trace:
  "§9.4.2#r38": [20]
  "§9.4.2#r39": [6, 7, 9, 15, 20, 66]
  "§9.4.2#r41": [39, 40, 41, 45, 51, 52, 76]
  "§9.4.2#r42": [30, 31]
  "§2.1#b5": [33, 63, 76]
  "§2.1#b3": [25, 26, 27, 33, 63]
  "§4.8#r9": [33, 63, 76]
  "§4.2.4#r15": [35, 39]
  "§3#p5": [13, 30, 31]
  "§Aturan Logika Modul#r32": [30, 31]
  "§Aturan Logika Modul#r58": [6, 7, 9]
  "§Aturan Logika Modul#r47": [12, 20]
  "§Aturan Logika Modul#r55": [33, 39, 45, 47]
  "§4.2.4#p8": [35, 36, 37]
  "EC-DMG-22": [15]
  "§2#b7": [20, 22, 66, 68]
  "§2#b6": [20, 75, 79]
  "FI-DMG-05": [6, 9, 16]
  "§2.1#b1": [3, 20, 55, 66, 79]
  "§2.1#b2": [15, 20, 62, 66, 79]
  "§3#p2": [5, 21, 67, 80]
  "§9.11#r1": [15]
  "§2.1#r2": [79]
  "§2.1#r5": [33, 63]
  "§4.2.3#p1": [5, 57, 61]
  "§4.8#r3": [82]
  "§9.4.3#b6": [27, 88]
anchor: [24, 87]
coverage:
  web: automated
---

# Pelapor dari Task Maintenance tanpa hak Aktor Damaged melapor rusak: What happened terisi dari indicator out of standard dan dapat diedit, record Waiting for Confirmation Source Maintenance dengan penanda Damage reported tanpa mengubah status global aset, Damage Log dapat dibuka pelapor, dan Cancel my report membatalkan laporan tanpa mengubah task

## Prerequisites
- Aktor: Staff Executor `Rina Kusuma {runId}` (DU-061-3), tanpa hak Aktor Damaged pada Group aset (tanpa hak Update Manage asset & TAG), sehingga pelapor umum, yang juga memegang role Read Only. Untuk kelompok Asset Admin Maintenance Routine: Asset Admin `Dewi Anggraini {runId}` (DU-061-4), tanpa hak Aktor Damaged pada Group aset. Untuk kelompok Pelapor admin: Aktor Damaged dengan role Total Control.
- Layar awal: halaman Task Maintenance `Perawatan Rutin Genset {runId}`.
- Data:
  - DU-061-1: Task Maintenance Name `Perawatan Rutin Genset {runId}` untuk Group `Head Office`, berstatus `In Progress`, dikerjakan `Rina Kusuma {runId}`, berisi aset Name `Genset Perkins 40kVA {runId}`, aset Name `Kompresor Udara Atlas Copco {runId}`, dan aset Name `Pompa Hidran Ebara {runId}`, ketiganya Group `Head Office`, tanpa TAG, status global `Normal`, dan belum punya record Damage; aset `Genset Perkins 40kVA {runId}` memiliki indicator out of standard bernama `Tekanan Oli` bernilai `1,2 bar`.
  - DU-061-4: User `Dewi Anggraini {runId}`, Asset Admin Maintenance Routine (bukan pelaksana Task Maintenance DU-061-1), role Read Only pada Group `Head Office`, tanpa hak Update Manage asset & TAG pada Group aset; cakupan: Group `Head Office`.
  - DU-061-3: User `Rina Kusuma {runId}`, Staff Executor pada Task Maintenance DU-061-1, role Read Only pada Group `Head Office`, tanpa hak Update Manage asset & TAG pada Group aset; cakupan: Group `Head Office`.

## Test Steps

### Report Damaged dari Task Maintenance: What happened terisi dari indicator out of standard dan dapat diedit
1. Buka Task Maintenance `Perawatan Rutin Genset {runId}` untuk aset `Genset Perkins 40kVA {runId}`
2. Catat status Task Maintenance sebagai status awal
3. Verifikasi tombol `Report Damaged` tampil pada Task Maintenance
4. Klik `Report Damaged` pada Task Maintenance
5. Verifikasi dialog `Report Damaged` tampil
6. Verifikasi field What happened terisi dengan nama indicator `Tekanan Oli`
7. Verifikasi field What happened terisi dengan nilai indicator `1,2 bar`
8. Ganti isi What happened dengan `Tekanan oli di bawah standar dan oli merembes dari seal pompa`
9. Verifikasi field What happened berisi `Tekanan oli di bawah standar dan oli merembes dari seal pompa`
10. Pilih Damaged Photo `genset-oli-merembes.jpg`
11. Klik `[Report Damaged]`
12. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil

### Damage Log terbuka dari penanda Damage reported di Task Maintenance
13. Verifikasi penanda `Damage reported` tampil pada Task Maintenance
14. Klik penanda `Damage reported`
15. Verifikasi dialog `Damage Log` tampil
16. Verifikasi node `Reported damaged by [Reporter Name]` memuat baris detail What happened `Tekanan oli di bawah standar dan oli merembes dari seal pompa`
17. Tutup dialog Damage Log

### Record Waiting for Confirmation Source Maintenance di tab Damaged dan tanpa aksi tulis bagi pelapor
18. Buka halaman Assets, tab `Damaged`
19. Ketik Search `{runId}`, tekan Enter
20. Verifikasi baris aset `Genset Perkins 40kVA {runId}` tampil di sub-tab `Active` dengan Status `Waiting for Confirmation`
21. Verifikasi kolom Source pada baris itu `Maintenance`
22. Verifikasi kolom Reported By pada baris itu memuat nama Staff Executor `Rina Kusuma {runId}`, dalam bentuk nama depan dan inisial nama belakang
23. Klik `⋯` pada baris aset `Genset Perkins 40kVA {runId}`
24. Verifikasi aksi `Damage Log` tampil pada menu baris
25. Verifikasi aksi `Mark as Repaired` tidak tampil pada menu baris
26. Verifikasi aksi `Report Missing` tidak tampil pada menu baris
27. Verifikasi aksi `Review` tidak tampil pada menu baris

### Status global aset tetap dan hanya diberi penanda Damage reported
28. Buka halaman Assets, tab `Assets`
29. Ketik Search `Genset Perkins 40kVA {runId}`, tekan Enter
30. Verifikasi status global aset `Normal` pada baris `Genset Perkins 40kVA {runId}`
31. Verifikasi baris `Genset Perkins 40kVA {runId}` memuat penanda `Damage reported`

### Cancel my report dari Task Maintenance membatalkan laporan tanpa mengubah task
32. Buka Task Maintenance `Perawatan Rutin Genset {runId}` untuk aset `Genset Perkins 40kVA {runId}`
33. Verifikasi aksi `Cancel my report` tampil pada Task Maintenance
34. Klik `Cancel my report` pada Task Maintenance
35. Verifikasi dialog `Cancel Report` tampil dengan butir `Genset Perkins 40kVA {runId}`
36. Verifikasi dialog memuat pertanyaan `Are you sure you want to cancel it?`
37. Verifikasi dialog memuat tombol `[Go Back]` dan `[Cancel Report]`
38. Klik `[Cancel Report]` pada dialog
39. Verifikasi toast `Success, report has been canceled.` tampil
40. Verifikasi penanda `Damage reported` tidak tampil lagi pada Task Maintenance
41. Verifikasi status Task Maintenance sama dengan status awal yang dicatat

### Record Canceled di sub-tab History dan status global aset tidak berubah
42. Buka halaman Assets, tab `Damaged`
43. Klik sub-tab `History`
44. Ketik Search `{runId}`, tekan Enter
45. Verifikasi baris aset `Genset Perkins 40kVA {runId}` tampil di sub-tab `History` dengan Status `Canceled`
46. Klik nama aset pada baris aset `Genset Perkins 40kVA {runId}`
47. Verifikasi node `Report canceled by [Reporter Name]` tampil di dialog Damage Log
48. Tutup dialog Damage Log
49. Buka halaman Assets, tab `Assets`
50. Ketik Search `Genset Perkins 40kVA {runId}`, tekan Enter
51. Verifikasi status global aset `Normal` pada baris `Genset Perkins 40kVA {runId}`
52. Verifikasi baris `Genset Perkins 40kVA {runId}` tidak memuat penanda `Damage reported`

### Asset Admin Maintenance Routine tanpa hak Aktor Damaged melapor sebagai pelapor umum
53. Masuk sebagai Asset Admin Maintenance Routine `Dewi Anggraini {runId}`
54. Buka Task Maintenance `Perawatan Rutin Genset {runId}` untuk aset `Kompresor Udara Atlas Copco {runId}`
55. Verifikasi tombol `Report Damaged` tampil pada Task Maintenance
56. Klik `Report Damaged` pada Task Maintenance
57. Verifikasi dialog `Report Damaged` tampil
58. Isi What happened `Kompresor tidak mencapai tekanan kerja dan terdengar berisik`
59. Pilih Damaged Photo `kompresor-berisik.jpg`
60. Klik `[Report Damaged]`
61. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil
62. Verifikasi penanda `Damage reported` tampil pada Task Maintenance
63. Verifikasi aksi `Cancel my report` tampil pada Task Maintenance
64. Buka halaman Assets, tab `Damaged`
65. Ketik Search `Kompresor Udara Atlas Copco {runId}`, tekan Enter
66. Verifikasi baris aset `Kompresor Udara Atlas Copco {runId}` tampil di sub-tab `Active` dengan Status `Waiting for Confirmation`
67. Verifikasi kolom Source pada baris itu `Maintenance`
68. Verifikasi kolom Reported By pada baris itu memuat nama Asset Admin `Dewi Anggraini {runId}`, dalam bentuk nama depan dan inisial nama belakang

### Pelapor admin dari Task Maintenance langsung Damaged dan tidak memakai Cancel my report
69. Masuk sebagai Aktor Damaged dengan role Total Control
70. Buka Task Maintenance `Perawatan Rutin Genset {runId}` untuk aset `Pompa Hidran Ebara {runId}`
71. Klik `Report Damaged` pada Task Maintenance
72. Isi What happened `Seal pompa bocor dan tekanan air turun`
73. Pilih Damaged Photo `pompa-seal-bocor.jpg`
74. Klik `[Report Damaged]`
75. Verifikasi toast `Success, asset has been reported damaged.` tampil
76. Verifikasi aksi `Cancel my report` tidak tampil pada Task Maintenance
77. Buka halaman Assets, tab `Damaged`
78. Ketik Search `Pompa Hidran Ebara {runId}`, tekan Enter
79. Verifikasi baris aset `Pompa Hidran Ebara {runId}` tampil di sub-tab `Active` dengan Status `Damaged`, tanpa Confirm
80. Verifikasi kolom Source pada baris itu `Maintenance`

### Tombol Report Damaged di Task Maintenance tampil bagi Total Control yang berhak atas sesi itu
81. Buka Task Maintenance `Perawatan Rutin Genset {runId}` untuk aset `Genset Perkins 40kVA {runId}`
82. Verifikasi tombol `Report Damaged` tampil pada Task Maintenance

### Damage Log record pelapor umum tidak menampilkan Confirm dan Reject
83. Masuk sebagai Asset Admin Maintenance Routine `Dewi Anggraini {runId}`
84. Buka halaman Assets, tab `Damaged`
85. Ketik Search `Kompresor Udara Atlas Copco {runId}`, tekan Enter
86. Klik nama aset pada baris aset `Kompresor Udara Atlas Copco {runId}`
87. Verifikasi dialog `Damage Log` aset `Kompresor Udara Atlas Copco {runId}` tampil dengan node `Reported damaged by [Reporter Name]`
88. Verifikasi tombol `[Confirm]` dan `[Reject]` tidak tampil pada dialog Damage Log bagi pelapor `Dewi Anggraini {runId}`
89. Tutup dialog Damage Log
