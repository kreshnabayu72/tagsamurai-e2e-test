---
id: TC-FA-FATR-E2E-010-override-bulk
title: "Bulk Delete override"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#p49, §6#r30, §6#r31, §7#r7, D-07, §9.2#b117, §9.2#b190, §9.4.2#r79, §9.4.2#r117, §9.4.2#r118, §9.4.2#r119, §9.4.2#r120, §9.4.4#r26, §9.6#r28, EB-BLK-2@tabel-overrides, EB-BLK-3, EB-EDG-2, §9.2#b162, §9.6#r29]
smoke: [§9.2#b162, §9.6#r29]
dependsOn: []
trace:
  §4.1#p49: [11, 12, 19, 20, 21, 22, 27, 29, 30, 35, 37, 38, 43, 45, 46, 61, 63, 64, 65, 66, 74, 78, 92, 93, 94]
  §6#r30: 79
  §6#r31: 76
  §7#r7: [76, 92]
  D-07: [76, 77]
  §9.2#b117: [76, 92]
  §9.2#b190: 76
  §9.4.2#r79: 76
  §9.4.2#r117: 93
  §9.4.2#r118: [90, 94]
  §9.4.2#r119: 92
  §9.4.2#r120: [98, 99]
  §9.4.4#r26: [93, 94]
  §9.6#r28: 92
  EB-BLK-2@tabel-overrides: [52, 54, 56]
  EB-BLK-3: [19, 22]
  EB-EDG-2: [9, 17, 98]
  §9.2#b162: 93
  §9.6#r29: 94
anchor: [5, 69, 85]
coverage:
  web: automated
---

# Bulk Delete override

## Prerequisites
- Aktor: Total Control; lalu `Andi {runId}`, user dengan Group Role Manage asset & TAG (Read + Update) pada Group `Proyek Bekasi {runId}` beserta turunannya.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-010-1: Category leaf `Laptop {runId}`, ada di entitas aktor.
  - DU-010-2: Category leaf `Machinery {runId}`, ada di entitas aktor.
  - DU-010-3, DU-010-4, dan DU-010-5: Group tingkat atas `Gudang Alfa {runId}`, `Gudang Beta {runId}`, dan `Gudang Gamma {runId}`.
  - DU-010-6: 12 Group tingkat atas `Cabang {n} {runId}` dengan n dari 1 sampai 12.
  - DU-010-7, DU-010-8, dan DU-010-9: Group tingkat atas `Proyek Bekasi {runId}`, `Proyek Guard {runId}`, dan `Proyek Plain {runId}`.
  - DU-010-10, DU-010-11, DU-010-12, dan DU-010-13: Asset Name `Excavator PC200 {runId}`, `Toyota Avanza {runId}`, `Crane LTM1100 {runId}`, dan `Dozer D65 {runId}`, berurutan, masing-masing ber-Category `Laptop {runId}`.
  - DU-010-14: Asset Name `Forklift FL25 {runId}`, ber-Category `Machinery {runId}`.
  - DU-010-15, DU-010-16, dan DU-010-17: aset `Dozer D65 {runId} - 1`, `Dozer D65 {runId} - 2`, dan `Dozer D65 {runId} - 3`, ber-Group `Proyek Plain {runId}`.
  - DU-010-18: aset `Forklift FL25 {runId} - 1`, ber-Group `Proyek Guard {runId}` dan Category `Machinery {runId}`.
  - DU-010-19, DU-010-20, dan DU-010-21: override Group `Gudang Alfa {runId}`, `Gudang Beta {runId}`, dan `Gudang Gamma {runId}` di Category `Laptop {runId}` transaksi `Borrow`, masing-masing Overridden `Max duration (7 days)`.
  - DU-010-22: override Asset Name `Excavator PC200 {runId}` dan DU-010-23: override Asset `Dozer D65 {runId} - 1`, di Category `Laptop {runId}` transaksi `Borrow`, masing-masing Overridden `Max duration (9 days)`.
  - DU-010-24 dan DU-010-25: override Asset Name `Toyota Avanza {runId}` dan `Crane LTM1100 {runId}` di Category `Laptop {runId}` transaksi `Borrow`, masing-masing Overridden `Max duration (9 days)`.
  - DU-010-26 dan DU-010-27: override Asset `Dozer D65 {runId} - 2` dan `Dozer D65 {runId} - 3` di Category `Laptop {runId}` transaksi `Borrow`, masing-masing Overridden `Max duration (9 days)`.
  - DU-010-28: 12 override Group `Cabang {n} {runId}` di Category `Machinery {runId}` transaksi `Borrow`, masing-masing Overridden `Max duration (7 days)`, dibuat berurutan dari n=1 sampai n=12 sesudah DU-10-29.
  - DU-010-29: override Group `Proyek Bekasi {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max duration (20 days)`, dibuat paling awal.
  - DU-010-30: override Group `Proyek Guard {runId}` di Category `Machinery {runId}` transaksi `Assign`, Overridden `Allowed assignee: Division (ON)`.
  - DU-010-31: override Group `Proyek Guard {runId}` di All categories transaksi `Assign`, Overridden `Allowed assignee: Employee (OFF), Allowed assignee: Division (OFF)`.
  - DU-010-32: override Group `Proyek Plain {runId}` di Category `Machinery {runId}` transaksi `Assign`, Overridden `Recipient acceptance (Optional)`.
  - DU-010-33: user `Andi {runId}`, Group Role Manage asset & TAG (Read + Update), cakupan Group `Proyek Bekasi {runId}` beserta turunannya.
- Kondisi:
  - Allow Assign bukan Deny untuk aset `Forklift FL25 {runId} - 1`.
  - Akun `Andi {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Bulk Delete satu override memakai bentuk tunggal
1. Ketik Search Sidebar Category Tree `Laptop {runId}`, tekan Enter
2. Klik node `Laptop {runId}` di Sidebar Category Tree
3. Klik tab `Borrow`
4. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
5. Verifikasi baris dengan Target `Gudang Alfa {runId}` tampil di tabel Overrides
6. Centang baris `Gudang Alfa {runId}`
7. Klik `Bulk Action` pada toolbar tabel Overrides
8. Klik `Delete`
9. Verifikasi dialog `Delete Override` terbuka dalam bentuk tunggal untuk satu override `Gudang Alfa {runId}`
10. Klik `[Delete]`
11. Verifikasi toast `Success, override has been deleted.` tampil
12. Verifikasi tidak ada baris dengan Target `Gudang Alfa {runId}` di tabel Overrides

### Bulk Delete dua override Group sekaligus dengan konfirmasi klik ganda
13. Centang baris `Gudang Beta {runId}`
14. Centang baris `Gudang Gamma {runId}`
15. Klik `Bulk Action` pada toolbar tabel Overrides
16. Klik `Delete`
17. Verifikasi dialog `Delete Overrides` terbuka untuk dua override
18. Klik ganda `[Delete]`
19. Verifikasi toast `Success, override has been deleted.` tampil sekali untuk kedua override
20. Verifikasi tidak ada baris dengan Target `Gudang Beta {runId}` di tabel Overrides
21. Verifikasi tidak ada baris dengan Target `Gudang Gamma {runId}` di tabel Overrides
22. Verifikasi tabel Overrides hasil Search `{runId}` memuat `6` baris, setiap override terpilih terhapus tepat sekali

### Bulk Delete seleksi campuran `Asset Name` dan `Asset`
23. Centang baris `Excavator PC200 {runId}`
24. Centang baris dengan Target `Dozer D65 {runId} - 1`
25. Klik `Bulk Action` pada toolbar tabel Overrides
26. Klik `Delete`
27. Verifikasi dialog `Delete Overrides` terbuka untuk override `Asset Name` dan override `Asset`
28. Klik `[Delete]`
29. Verifikasi toast `Success, override has been deleted.` tampil untuk seleksi campuran `Asset Name` dan `Asset`
30. Verifikasi tabel Overrides hasil Search `{runId}` memuat `4` baris

### Bulk Delete seleksi seragam `Asset Name`
31. Centang baris `Toyota Avanza {runId}`
32. Centang baris `Crane LTM1100 {runId}`
33. Klik `Bulk Action` pada toolbar tabel Overrides
34. Klik `Delete`
35. Verifikasi dialog `Delete Overrides` terbuka untuk dua override `Asset Name`
36. Klik `[Delete]`
37. Verifikasi toast `Success, override has been deleted.` tampil untuk seleksi seragam `Asset Name`
38. Verifikasi tabel Overrides hasil Search `{runId}` memuat `2` baris

### Bulk Delete seleksi seragam `Asset`
39. Centang baris dengan Target `Dozer D65 {runId} - 2`
40. Centang baris dengan Target `Dozer D65 {runId} - 3`
41. Klik `Bulk Action` pada toolbar tabel Overrides
42. Klik `Delete`
43. Verifikasi dialog `Delete Overrides` terbuka untuk dua override `Asset`
44. Klik `[Delete]`
45. Verifikasi toast `Success, override has been deleted.` tampil untuk seleksi seragam `Asset`
46. Verifikasi `No results found` tampil di tabel Overrides

### Select All memilih lintas halaman
47. Ganti isi kotak Search Sidebar Category Tree dengan `Machinery {runId}`, tekan Enter
48. Klik node `Machinery {runId}` di Sidebar Category Tree
49. Klik tab `Borrow`
50. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
51. Centang baris `Cabang 12 {runId}`
52. Verifikasi tombol `Select All (13 records)` tampil[^drift-1]
53. Klik `Select All (13 records)`
54. Verifikasi tombol berubah menjadi `Unselect All (13 records)`[^drift-2]
55. Hapus centang baris `Cabang 12 {runId}`
56. Verifikasi tombol kembali menjadi `Select All (13 records)`
57. Klik ikon `×` pada Bulk Action Bar

### Bulk Delete memilih satu halaman penuh
58. Centang checkbox header tabel Overrides, memilih baris `Cabang 12 {runId}` sampai `Cabang 3 {runId}` di halaman 1
59. Klik `Bulk Action` pada toolbar tabel Overrides
60. Klik `Delete`
61. Verifikasi dialog `Delete Overrides` terbuka untuk sepuluh override halaman 1
62. Klik `[Delete]`
63. Verifikasi toast `Success, override has been deleted.` tampil untuk seleksi satu halaman penuh
64. Verifikasi tabel Overrides hasil Search `{runId}` memuat `3` baris
65. Verifikasi baris dengan Target `Cabang 1 {runId}` tampil di tabel Overrides
66. Verifikasi baris dengan Target `Cabang 2 {runId}` tampil di tabel Overrides

### Bulk Delete dengan baris yang ditolak guard Allowed assignee dilewati
67. Klik tab `Assign`
68. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
69. Verifikasi baris dengan Target `Proyek Guard {runId}` dan Overridden `Allowed assignee: Division (ON)` tampil di tabel Overrides
70. Centang baris dengan Target `Proyek Guard {runId}` dan Overridden `Allowed assignee: Division (ON)`
71. Centang baris `Proyek Plain {runId}`
72. Klik `Bulk Action` pada toolbar tabel Overrides
73. Klik `Delete`
74. Verifikasi dialog `Delete Overrides` terbuka untuk dua override
75. Klik `[Delete]`
76. Verifikasi toast `Success, override has been deleted. Some items were skipped.` tampil
77. Verifikasi dialog `Cannot Delete Overrides` tidak tampil
78. Verifikasi tidak ada baris dengan Target `Proyek Plain {runId}` di tabel Overrides
79. Verifikasi baris dengan Target `Proyek Guard {runId}` dan Overridden `Allowed assignee: Division (ON)` tetap tampil di tabel Overrides

### Bulk Delete seleksi campuran dalam dan luar scope
80. Masuk sebagai `Andi {runId}`
81. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
82. Klik node `Machinery {runId}` di Sidebar Category Tree
83. Klik tab `Borrow`
84. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
85. Verifikasi baris dengan Target `Proyek Bekasi {runId}` dan Overridden `Max duration (20 days)` tampil di tabel Overrides
86. Centang baris `Proyek Bekasi {runId}`
87. Centang baris `Cabang 1 {runId}`
88. Klik `Bulk Action` pada toolbar tabel Overrides
89. Klik `Delete`
90. Verifikasi paragraf `Some overrides are outside your scope and will be skipped:` tampil pada dialog `Delete Overrides`
91. Klik `[Delete]`
92. Verifikasi toast `Success, override has been deleted. Some items were skipped.` tampil
93. Verifikasi tidak ada baris dengan Target `Proyek Bekasi {runId}` di tabel Overrides
94. Verifikasi baris dengan Target `Cabang 1 {runId}` tetap tampil di tabel Overrides

### Bulk Delete seleksi yang seluruhnya di luar scope tidak bisa dijalankan
95. Centang baris `Cabang 1 {runId}`
96. Centang baris `Cabang 2 {runId}`
97. Klik `Bulk Action` pada toolbar tabel Overrides
98. Verifikasi menu `Delete` disabled
99. Verifikasi alasan `This override is outside your scope.` tersampaikan pada menu `Delete` yang disabled

[^drift-1]: Drift PRD dan foundation vs kontrak komponen. PRD §4.1 (tabel Overrides): bulk delete memakai komponen `BulkActionButton` menurut `prd-conventions.md` §8, foundation `prd-conventions.md` §8: «Web: selalu tampil (tidak perlu pilih dulu)». Kontrak `BulkActionButton#9`: tombol select-all muncul bila seleksi tidak kosong, dan `BulkActionButton#1`: tanpa seleksi tidak ada bar yang dirender. Diasersi: kontrak, sehingga satu baris dicentang lebih dulu (SB-7).
[^drift-2]: Drift PRD dan foundation vs kontrak komponen. PRD §4.1 (tabel Overrides): bulk delete memakai komponen `BulkActionButton` menurut `prd-conventions.md` §8, foundation `prd-conventions.md` §8: tombol berubah menjadi `"Unselect All"`. Kontrak `BulkActionButton#11` dan `BulkActionButton#60`: bila seluruh N terpilih teksnya `Unselect All (N records)`. Diasersi: kontrak (SB-7).
