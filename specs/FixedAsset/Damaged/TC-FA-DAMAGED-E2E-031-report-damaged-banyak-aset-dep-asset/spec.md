---
id: TC-FA-DAMAGED-E2E-031-report-damaged-banyak-aset-dep-asset
title: "Report Damaged Assets dari Asset List membuat satu record per aset, mengeluarkan aset tidak layak dengan keterangan, dan memblok D-DMG-12 bila semua tidak layak"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-01, D-DMG-12, §4.2.3#p2, §4.2.3#b2, §4.2.3#b3, §4.2.3#b4, §4.2.3#b5, §4.2.3#b6, §4.2.4#p10, FI-DMG-06, FI-DMG-07, TS-DMG-10, V-DMG-10, §Aturan Logika Modul#r16, §Aturan Logika Modul#r17, §8.3#b1, S-DMG-21, EC-DMG-01, EC-DMG-02, EC-DMG-05, §9.4.4#r1, §9.4.4#r5, F-DMG-01, §4.8#r2, EB-FB-2@dialog-blok-report-damaged]
smoke: [EB-FB-2@dialog-blok-report-damaged]
dependsOn:
  - "Asset: Asset List (Report Damaged banyak aset)"
trace:
  D-DMG-01: [34, 35]
  D-DMG-12: [51, 52]
  §4.2.3#p2: [5, 11, 12, 18, 20, 64, 82, 98, 99]
  §4.2.3#b2: [22, 23, 54, 55]
  §4.2.3#b3: 27
  §4.2.3#b4: 25
  §4.2.3#b5: 24
  §4.2.3#b6: [18, 19, 51, 57, 70, 71, 89, 90]
  §4.2.4#p10: [53, 54, 55, 56]
  FI-DMG-06: [26, 39, 44]
  FI-DMG-07: [27, 41, 45]
  TS-DMG-10: 70
  V-DMG-10: [71, 72, 89, 91, 92]
  §Aturan Logika Modul#r16: [20, 53]
  §Aturan Logika Modul#r17: [34, 35]
  §8.3#b1: [37, 40]
  S-DMG-21: [71, 72, 76]
  EC-DMG-01: [20, 53]
  EC-DMG-02: [21, 36]
  EC-DMG-05: [71, 72, 77]
  §9.4.4#r1: [20, 21, 36]
  §9.4.4#r5: [40, 77]
  F-DMG-01: [34, 35]
  §4.8#r2: 3
  EB-FB-2@dialog-blok-report-damaged: 58
coverage:
  web: automated
---

# Report Damaged Assets dari Asset List membuat satu record per aset, mengeluarkan aset tidak layak dengan keterangan, dan memblok D-DMG-12 bila semua tidak layak

## Prerequisites
- Aktor: pemegang Manage asset & TAG dengan Update pada Group `Head Office` dan Read pada Group `Branch Surabaya`. Admin B (Total Control) hanya memicu laporan lain.
- Layar awal: halaman Assets, tab Assets (Asset List).
- Data:
  - DU-031-1: aset `Meja Kerja Staff {runId}`, Group `Head Office`, status global `Normal`, tanpa record Damage.
  - DU-031-2: 8 aset `Kursi Rapat Eksekutif Ruang Pertemuan Utama Lantai Tiga Gedung Timur {runId} {n}` (`{n}` 1 sampai 8), Group `Head Office`, status global `Normal`, tanpa record Damage; kata kunci Search `Kursi Rapat Eksekutif Ruang Pertemuan Utama Lantai Tiga Gedung Timur {runId}`.
  - DU-031-3: aset `Laptop Staf {runId} Layak 1`, Group `Head Office`, status global `Normal`, tanpa record Damage; kata kunci Search `Laptop Staf {runId}`.
  - DU-031-4: aset `Laptop Staf {runId} Layak 2`, Group `Head Office`, status global `Normal`, tanpa record Damage.
  - DU-031-5: aset `Laptop Staf {runId} Berjalan`, Group `Head Office`, status global `Damaged`, record Damage berjalan berstatus `Damaged`.
  - DU-031-6: aset `Laptop Staf {runId} Waiting`, Group `Head Office`, record Damage berjalan berstatus `Waiting for Confirmation`.
  - DU-031-7: aset `Laptop Staf {runId} Disposed`, Group `Head Office`, status `Disposed`.
  - DU-031-8: aset `Laptop Staf {runId} Missing`, Group `Head Office`, status `Missing`, tanpa record Damage.
  - DU-031-9: aset `Laptop Staf {runId} Luar Cakupan`, Group `Branch Surabaya` (aktor hanya memegang Read), status global `Normal`, tanpa record Damage.
  - DU-031-10: aset `Monitor Arsip {runId} Berjalan`, Group `Head Office`, record Damage berjalan berstatus `Damaged`; kata kunci Search `Monitor Arsip {runId}`.
  - DU-031-11: aset `Monitor Arsip {runId} Disposed`, Group `Head Office`, status `Disposed`.
  - DU-031-12: aset `Monitor Arsip {runId} Missing`, Group `Head Office`, status `Missing`, tanpa record Damage.
  - DU-031-13: aset `Scanner Gudang {runId} Satu`, Group `Head Office`, status global `Normal`, tanpa record Damage; kata kunci Search `Scanner Gudang {runId}`.
  - DU-031-14: aset `Scanner Gudang {runId} Dua`, Group `Head Office`, status global `Normal`, tanpa record Damage.
  - DU-031-15: aset `Printer Gudang {runId} Satu`, Group `Head Office`, status global `Normal`, tanpa record Damage; kata kunci Search `Printer Gudang {runId}`.
  - DU-031-16: aset `Printer Gudang {runId} Dua`, Group `Head Office`, status global `Normal`, tanpa record Damage.
  - DU-031-17: isian laporan laptop: What happened `Genangan air merusak casing laptop`, foto `laptop-layak-1.jpg` untuk `Laptop Staf {runId} Layak 1`, foto `laptop-layak-2.jpg` untuk `Laptop Staf {runId} Layak 2`.
  - DU-031-18: isian laporan scanner: What happened `Casing scanner retak setelah terjatuh`, foto `scanner-satu.jpg` untuk `Scanner Gudang {runId} Satu`, foto `scanner-dua.jpg` untuk `Scanner Gudang {runId} Dua`.
  - DU-031-19: isian laporan printer: What happened `Roller printer gudang aus`, foto `printer-satu.jpg` untuk `Printer Gudang {runId} Satu`, foto `printer-dua.jpg` untuk `Printer Gudang {runId} Dua`.
  - DU-031-20: laporan Admin B atas `Scanner Gudang {runId} Dua`: What happened `Kabel daya scanner terbakar`, foto `scanner-kabel-terbakar.jpg`.
  - DU-031-21: laporan Admin B atas `Printer Gudang {runId} Satu`: What happened `Panel printer gudang mati total`, foto `printer-panel-mati.jpg`.
  - DU-031-22: laporan Admin B atas `Printer Gudang {runId} Dua`: What happened `Tray kertas printer gudang patah`, foto `printer-tray-patah.jpg`.

## Test Steps

### Satu aset terpilih membuka dialog berjudul tunggal
1. Ketik Search `Meja Kerja Staff {runId}`, tekan Enter
2. Centang baris `Meja Kerja Staff {runId}`
3. Verifikasi aksi `Report Damaged` tersedia untuk aset terpilih
4. Klik `[Report Damaged]` untuk aset terpilih
5. Verifikasi dialog berjudul `Report Damaged` tampil dengan satu blok aset `Meja Kerja Staff {runId}`
6. Klik `✕` pada dialog (form belum diubah)
7. Klik `×` pada bar seleksi

### Daftar aset di dialog tidak diringkas
8. Ganti isi kotak search dengan `Kursi Rapat Eksekutif Ruang Pertemuan Utama Lantai Tiga Gedung Timur {runId}`, tekan Enter
9. Centang checkbox header pada kolom Checkbox
10. Klik `[Report Damaged]` untuk aset terpilih
11. Verifikasi dialog berjudul `Report Damaged Assets` tampil
12. Verifikasi seluruh 8 aset `Kursi Rapat Eksekutif Ruang Pertemuan Utama Lantai Tiga Gedung Timur {runId} {n}` tampil sebagai blok di daftar dialog tanpa diringkas
13. Klik `✕` pada dialog (form belum diubah)
14. Klik `×` pada bar seleksi

### Aset tidak layak dikeluarkan dari dialog dan aset layak dilaporkan
15. Ganti isi kotak search dengan `Laptop Staf {runId}`, tekan Enter
16. Centang checkbox header pada kolom Checkbox
17. Klik `[Report Damaged]` untuk aset terpilih
18. Verifikasi dialog berjudul `Report Damaged Assets` tampil
19. Verifikasi dialog hanya memuat blok aset `Laptop Staf {runId} Layak 1` dan `Laptop Staf {runId} Layak 2`
20. Verifikasi keterangan `Already reported damaged` tampil untuk aset `Laptop Staf {runId} Berjalan`
21. Verifikasi keterangan `Already reported damaged` tampil untuk aset `Laptop Staf {runId} Waiting`
22. Verifikasi keterangan `Can't be reported damaged` tampil untuk aset `Laptop Staf {runId} Disposed`
23. Verifikasi keterangan `Can't be reported damaged` tampil untuk aset `Laptop Staf {runId} Missing`
24. Verifikasi keterangan `Can't be reported damaged` tampil untuk aset `Laptop Staf {runId} Luar Cakupan`
25. Verifikasi kotak dampak `The assets will be marked Damaged.` tampil
26. Verifikasi hanya ada satu isian `What happened` untuk seluruh aset
27. Verifikasi satu `Damaged Photo` tampil di setiap blok aset `Laptop Staf {runId} Layak 1` dan `Laptop Staf {runId} Layak 2`
28. Isi `What happened` dengan `Genangan air merusak casing laptop`
29. Unggah foto `laptop-layak-1.jpg` pada `Damaged Photo` blok aset `Laptop Staf {runId} Layak 1`
30. Unggah foto `laptop-layak-2.jpg` pada `Damaged Photo` blok aset `Laptop Staf {runId} Layak 2`
31. Klik `[Report Damaged]` pada footer dialog

### Satu record per aset layak tercatat di tab Damaged dan Damage Log
32. Buka tab `Damaged` pada halaman Assets
33. Ketik Search `Laptop Staf {runId}`, tekan Enter
34. Verifikasi baris `Laptop Staf {runId} Layak 1` tampil dengan Status `Damaged`
35. Verifikasi baris `Laptop Staf {runId} Layak 2` tampil dengan Status `Damaged`
36. Verifikasi baris `Laptop Staf {runId} Waiting` tampil dengan Status `Waiting for Confirmation`
37. Verifikasi tidak ada baris untuk aset `Laptop Staf {runId} Disposed`, `Laptop Staf {runId} Missing`, dan `Laptop Staf {runId} Luar Cakupan`
38. Klik nama aset `Laptop Staf {runId} Layak 1` untuk membuka dialog Damage Log
39. Verifikasi `What happened` `Genangan air merusak casing laptop` tampil pada node `Reported damaged by`
40. Verifikasi tepat satu node `Reported damaged by` tampil
41. Verifikasi `Damaged Photo` milik aset `Laptop Staf {runId} Layak 1` tampil pada node `Reported damaged by`
42. Klik `✕` pada dialog Damage Log
43. Klik nama aset `Laptop Staf {runId} Layak 2` untuk membuka dialog Damage Log
44. Verifikasi `What happened` `Genangan air merusak casing laptop` tampil pada node `Reported damaged by`
45. Verifikasi `Damaged Photo` milik aset `Laptop Staf {runId} Layak 2` tampil pada node `Reported damaged by`
46. Klik `✕` pada dialog Damage Log

### Semua aset terpilih tidak layak memblok dengan Cannot Report Damaged
47. Buka tab `Assets` pada halaman Assets
48. Ganti isi kotak search dengan `Monitor Arsip {runId}`, tekan Enter
49. Centang checkbox header pada kolom Checkbox
50. Klik `[Report Damaged]` untuk aset terpilih
51. Verifikasi dialog `Cannot Report Damaged` tampil
52. Verifikasi pesan `None of the selected assets can be reported damaged.` tampil
53. Verifikasi keterangan `Already reported damaged` tampil untuk aset `Monitor Arsip {runId} Berjalan`
54. Verifikasi keterangan `Can't be reported damaged` tampil untuk aset `Monitor Arsip {runId} Disposed`
55. Verifikasi keterangan `Can't be reported damaged` tampil untuk aset `Monitor Arsip {runId} Missing`
56. Verifikasi tombol `[OK]` tampil pada dialog
57. Verifikasi dialog `Report Damaged` tidak dibuka untuk seleksi itu
58. Verifikasi toast `Success, asset has been reported damaged.` tidak tampil
59. Klik `[OK]`
60. Klik `×` pada bar seleksi

### Aset yang dilaporkan admin lain saat dialog terbuka dilewati sebagian
61. Ganti isi kotak search dengan `Scanner Gudang {runId}`, tekan Enter
62. Centang checkbox header pada kolom Checkbox
63. Klik `[Report Damaged]` untuk aset terpilih
64. Verifikasi dialog berjudul `Report Damaged Assets` tampil dengan blok aset `Scanner Gudang {runId} Satu` dan `Scanner Gudang {runId} Dua`
65. Admin B melaporkan aset `Scanner Gudang {runId} Dua` rusak dengan What happened `Kabel daya scanner terbakar` dan foto `scanner-kabel-terbakar.jpg`
66. Isi `What happened` dengan `Casing scanner retak setelah terjatuh`
67. Unggah foto `scanner-satu.jpg` pada `Damaged Photo` blok aset `Scanner Gudang {runId} Satu`
68. Unggah foto `scanner-dua.jpg` pada `Damaged Photo` blok aset `Scanner Gudang {runId} Dua`
69. Klik `[Report Damaged]` pada footer dialog
70. Verifikasi toast `Success, asset has been reported damaged. Some items were skipped.` tampil
71. Verifikasi dialog `Report Damaged Assets` tetap terbuka
72. Verifikasi keterangan `Already reported damaged` tampil untuk aset `Scanner Gudang {runId} Dua`
73. Klik `[Cancel]` pada footer dialog
74. Buka tab `Damaged` pada halaman Assets
75. Ganti isi kotak search dengan `Scanner Gudang {runId}`, tekan Enter
76. Verifikasi baris `Scanner Gudang {runId} Satu` tampil dengan Status `Damaged`
77. Verifikasi tepat satu baris `Scanner Gudang {runId} Dua` tampil

### Semua aset dilaporkan admin lain saat dialog terbuka tidak membuat laporan
78. Buka tab `Assets` pada halaman Assets
79. Ganti isi kotak search dengan `Printer Gudang {runId}`, tekan Enter
80. Centang checkbox header pada kolom Checkbox
81. Klik `[Report Damaged]` untuk aset terpilih
82. Verifikasi dialog berjudul `Report Damaged Assets` tampil dengan blok aset `Printer Gudang {runId} Satu` dan `Printer Gudang {runId} Dua`
83. Admin B melaporkan aset `Printer Gudang {runId} Satu` rusak dengan What happened `Panel printer gudang mati total` dan foto `printer-panel-mati.jpg`
84. Admin B melaporkan aset `Printer Gudang {runId} Dua` rusak dengan What happened `Tray kertas printer gudang patah` dan foto `printer-tray-patah.jpg`
85. Isi `What happened` dengan `Roller printer gudang aus`
86. Unggah foto `printer-satu.jpg` pada `Damaged Photo` blok aset `Printer Gudang {runId} Satu`
87. Unggah foto `printer-dua.jpg` pada `Damaged Photo` blok aset `Printer Gudang {runId} Dua`
88. Klik `[Report Damaged]` pada footer dialog
89. Verifikasi dialog `Report Damaged Assets` tetap terbuka
90. Verifikasi toast `Success, asset has been reported damaged.` tidak tampil
91. Verifikasi keterangan `Already reported damaged` tampil untuk aset `Printer Gudang {runId} Satu`
92. Verifikasi keterangan `Already reported damaged` tampil untuk aset `Printer Gudang {runId} Dua`
93. Klik `[Cancel]` pada footer dialog

### Daftar aset pada dialog dapat digulir
94. Klik `×` pada bar seleksi
95. Ganti isi kotak search dengan `Kursi Rapat Eksekutif Ruang Pertemuan Utama Lantai Tiga Gedung Timur {runId}`, tekan Enter
96. Centang checkbox header pada kolom Checkbox
97. Klik `[Report Damaged]` untuk aset terpilih
98. Verifikasi dialog berjudul `Report Damaged Assets` tampil
99. Verifikasi daftar blok aset pada dialog dapat digulir sampai blok aset `Kursi Rapat Eksekutif Ruang Pertemuan Utama Lantai Tiga Gedung Timur {runId} 8` terjangkau dan tampil
100. Klik `✕` pada dialog (form belum diubah)
101. Klik `×` pada bar seleksi
