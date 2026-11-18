---
id: TC-FA-DAMAGED-E2E-013-bulk-seleksi-lintas-group
title: "Seleksi bulk sub-tab Active: checkbox Disabled pada baris bukan Damaged atau berpenanda Missing, Select All lintas halaman, dan seleksi lintas Group diblok D-DMG-07"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, D-DMG-07, §4.2.4#p6, §4.2.4#r9, §4.4#r13, V-DMG-08, V-DMG-02, S-DMG-08, §6#p2, §9.2#b12, EC-DMG-21, §9.4.4#r10, §5#r5, EB-BLK-2@tabel-active, F-DMG-02, EB-FB-2@dialog-blok-disposal]
smoke: [EB-FB-2@dialog-blok-disposal]
dependsOn: []
trace:
  T-DMG-01: [5, 6, 8, 9, 11, 12, 14, 15, 18, 21, 22, 24, 25, 32, 35, 38, 40, 41, 44, 50, 59, 60, 62, 78]
  D-DMG-07: [67, 68, 69, 73]
  §4.2.4#p6: [68, 69]
  §4.2.4#r9: 67
  §4.4#r13: [67, 70]
  V-DMG-08: [67, 68]
  V-DMG-02: [15, 17, 18, 20, 21, 22]
  S-DMG-08: [64, 67]
  §6#p2: [70, 73, 82, 83, 84, 86, 87]
  §9.2#b12: [64, 67]
  EC-DMG-21: [67, 70, 74]
  §9.4.4#r10: 74
  §5#r5: 65
  EB-BLK-2@tabel-active: [25, 27, 28, 45, 47, 48, 50, 53, 55]
  F-DMG-02: [65, 67]
  EB-FB-2@dialog-blok-disposal: [67, 71]
anchor: []
coverage:
  web: automated
---

# Seleksi bulk sub-tab Active: checkbox Disabled pada baris bukan Damaged atau berpenanda Missing, Select All lintas halaman, dan seleksi lintas Group diblok D-DMG-07

## Prerequisites
- Aktor: Total Control (DU-013-10); `Admin B {runId}` (DU-013-13) hanya memicu perubahan state.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-013-1: 12 Damage record aset `Monitor Dell P2422H {n} {runId}` (n = 1 sampai 12) di Group `Head Office {runId}` (DU-013-8), semuanya berstatus `Damaged`, Source `Manual`, tanpa penanda, dilaporkan DU-013-10.
  - DU-013-2: Damage record aset `Printer HP LaserJet M404 {runId}` di Group `Warehouse {runId}` (DU-013-9), status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pelapor umum DU-013-11.
  - DU-013-3: Damage record aset `Scanner Fujitsu fi-7160 {runId}` di Group `Warehouse {runId}`, status `Reported Disposal`, Source `Stock opname`, dilaporkan DU-013-10.
  - DU-013-4: Damage record aset `Forklift Toyota 8FD {runId}` di Group `Warehouse {runId}`, status `In Disposal Process`, Source `Manual`, dilaporkan DU-013-10.
  - DU-013-5: Damage record aset `Camera Canon EOS {runId}` di Group `Warehouse {runId}`, status `Damaged` dengan penanda `Missing`, Source `Manual`, dilaporkan DU-013-10.
  - DU-013-6: Damage record aset `Drill Bosch GSB {runId}` di Group `Warehouse {runId}`, status `Damaged` dengan penanda `Reported Missing`, Source `Manual`, dilaporkan DU-013-10.
  - DU-013-7: Damage record aset `Toyota Avanza {runId}` di Group `Warehouse {runId}`, status `Damaged`, Source `Manual`, tanpa penanda, dilaporkan DU-013-10.
  - DU-013-8: Group `Head Office {runId}`.
  - DU-013-9: Group `Warehouse {runId}`.
  - DU-013-10: User `Agus Pratama {runId}`, role Total Control; cakupan: seluruh client.
  - DU-013-11: User `Dewi Anggraeni {runId}`, pelapor umum tanpa hak Aktor Damaged; cakupan: aset yang ia pegang.
  - DU-013-12: Damage record aset `Generator Honda EU20i {runId}` di Group `Warehouse {runId}` (DU-013-9), status `Damaged`, Source `Manual`, tanpa penanda, dilaporkan DU-013-10.
  - DU-013-13: User `Admin B {runId}`, role Total Control; cakupan: seluruh client.
  - DU-013-14: Input Reason Admin B atas record DU-013-12: Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`.
- Kondisi:
  - Selection Limit bernilai `1000`.
  - Level Feature Suite Disposal bernilai `Full`.

## Test Steps

### Checkbox Disabled pada baris bukan Damaged atau berpenanda Missing
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon Filter pada toolbar
3. Pada Filter Panel, pilih Group `Warehouse {runId}`
4. Klik `[Apply]`
5. Verifikasi baris `Toyota Avanza {runId}` tampil dengan status `Damaged` dan checkbox aktif
6. Verifikasi checkbox baris `Printer HP LaserJet M404 {runId}` Disabled
7. Arahkan kursor ke checkbox baris `Printer HP LaserJet M404 {runId}` yang Disabled
8. Verifikasi alasan `Only damaged records can be selected.` tersampaikan pada checkbox baris `Printer HP LaserJet M404 {runId}` yang Disabled
9. Verifikasi checkbox baris `Scanner Fujitsu fi-7160 {runId}` Disabled
10. Arahkan kursor ke checkbox baris `Scanner Fujitsu fi-7160 {runId}` yang Disabled
11. Verifikasi alasan `Only damaged records can be selected.` tersampaikan pada checkbox baris `Scanner Fujitsu fi-7160 {runId}` yang Disabled
12. Verifikasi checkbox baris `Forklift Toyota 8FD {runId}` Disabled
13. Arahkan kursor ke checkbox baris `Forklift Toyota 8FD {runId}` yang Disabled
14. Verifikasi alasan `Only damaged records can be selected.` tersampaikan pada checkbox baris `Forklift Toyota 8FD {runId}` yang Disabled
15. Verifikasi checkbox baris `Camera Canon EOS {runId}` Disabled
16. Arahkan kursor ke checkbox baris `Camera Canon EOS {runId}` yang Disabled
17. Verifikasi alasan `This asset is reported missing.` tersampaikan pada checkbox baris `Camera Canon EOS {runId}` yang Disabled
18. Verifikasi checkbox baris `Drill Bosch GSB {runId}` Disabled
19. Arahkan kursor ke checkbox baris `Drill Bosch GSB {runId}` yang Disabled
20. Verifikasi alasan `This asset is reported missing.` tersampaikan pada checkbox baris `Drill Bosch GSB {runId}` yang Disabled
21. Verifikasi checkbox baris `Printer HP LaserJet M404 {runId}` yang Disabled tidak dapat dicentang
22. Verifikasi bar bulk tidak tampil
23. Centang baris `Toyota Avanza {runId}`
24. Verifikasi counter seleksi pada bar bulk menampilkan jumlah `1`
25. Verifikasi tombol `Select All (2 records)` tampil pada bar bulk karena baris Disabled tidak dihitung dan hanya `Toyota Avanza {runId}` serta `Generator Honda EU20i {runId}` yang dapat dipilih
26. Klik ikon `×` pada bar bulk
27. Verifikasi baris `Toyota Avanza {runId}` tampil dengan checkbox tidak tercentang
28. Verifikasi bar bulk tidak tampil

### Seleksi satu baris dan banyak baris
29. Klik ikon Filter pada toolbar
30. Pada Filter Panel, ganti pilihan Group menjadi `Head Office {runId}`
31. Klik `[Apply]`
32. Verifikasi halaman pertama tabel memuat 10 baris
33. Ganti isi kotak search dengan `Monitor Dell P2422H 1 {runId}`, tekan Enter
34. Centang baris `Monitor Dell P2422H 1 {runId}`
35. Verifikasi counter seleksi pada bar bulk menampilkan jumlah `1`
36. Ganti isi kotak search dengan `Monitor Dell P2422H 2 {runId}`, tekan Enter
37. Centang baris `Monitor Dell P2422H 2 {runId}`
38. Verifikasi counter seleksi pada bar bulk menampilkan jumlah `2`
39. Klik ikon `×` pada bar bulk
40. Verifikasi baris `Monitor Dell P2422H 2 {runId}` tampil dengan checkbox tidak tercentang
41. Verifikasi bar bulk tidak tampil
42. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Header checkbox memilih baris halaman aktif dan Select All memilih lintas halaman
43. Centang checkbox header kolom Checkbox
44. Verifikasi counter seleksi pada bar bulk menampilkan jumlah `10`
45. Verifikasi tombol `Select All (12 records)` tampil pada bar bulk
46. Klik `Select All (12 records)`
47. Verifikasi counter seleksi pada bar bulk menampilkan jumlah `12`
48. Verifikasi tombol seleksi pada bar bulk berubah menjadi `Unselect All (N records)` dengan N bernilai `12`[^drift-1]
49. Klik `Next Page`
50. Verifikasi seluruh baris di halaman 2 tercentang
51. Ganti isi kotak search dengan `Monitor Dell P2422H 1 {runId}`, tekan Enter
52. Hapus centang baris `Monitor Dell P2422H 1 {runId}`
53. Verifikasi counter seleksi pada bar bulk menampilkan jumlah `11`
54. Ganti isi kotak search dengan `{runId}`, tekan Enter
55. Verifikasi tombol seleksi pada bar bulk kembali menjadi `Select All (12 records)`

### Seleksi bertahan saat filter berganti dan lintas Group diblok
56. Klik ikon Filter pada toolbar
57. Pada Filter Panel, ganti pilihan Group menjadi `Warehouse {runId}`
58. Klik `[Apply]`
59. Verifikasi baris `Toyota Avanza {runId}` tampil di tabel dengan status `Damaged`
60. Verifikasi counter seleksi pada bar bulk tetap menampilkan jumlah `11` walau baris terpilih tersaring keluar
61. Centang baris `Toyota Avanza {runId}`
62. Verifikasi counter seleksi pada bar bulk menampilkan jumlah `12`
63. Klik `Bulk Action`[^drift-2]
64. Verifikasi item `Report Disposal` tampil aktif pada menu `Bulk Action`
65. Verifikasi menu `Bulk Action` hanya memuat satu item, yaitu `Report Disposal`
66. Klik `Report Disposal`
67. Verifikasi dialog `Cannot Report Disposal` terbuka
68. Verifikasi dialog memuat pesan `Selected assets come from more than one group. Select assets from one group.`
69. Verifikasi daftar aset pada dialog memuat seluruh 12 aset terpilih tanpa diringkas, termasuk `Toyota Avanza {runId}`
70. Verifikasi dialog `D-DISP-13` tidak tampil
71. Verifikasi tidak ada toast yang tampil
72. Klik `[OK]` pada dialog `Cannot Report Disposal`
73. Verifikasi dialog `Cannot Report Disposal` tertutup dan bar bulk tetap menampilkan jumlah `12`
74. Verifikasi baris `Toyota Avanza {runId}` tetap berstatus `Damaged`

### Record terpilih yang berubah sebelum klik bulk dicek ulang dan diblok
75. Klik ikon `×` pada bar bulk
76. Ganti isi kotak search dengan `Generator Honda EU20i {runId}`, tekan Enter
77. Centang baris `Generator Honda EU20i {runId}`
78. Verifikasi counter seleksi pada bar bulk menampilkan jumlah `1`
79. `Admin B {runId}` menjalankan Report Disposal atas record `Generator Honda EU20i {runId}` dengan Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`
80. Klik `Bulk Action`[^drift-2]
81. Klik `Report Disposal`
82. Verifikasi dialog `Cannot Report Disposal` terbuka sebelum dialog Report Disposal dibuka
83. Verifikasi isi dialog `None of the selected records can be reported for disposal.`
84. Verifikasi dialog Report Disposal tidak terbuka
85. Klik `[OK]` pada dialog `Cannot Report Disposal`
86. Verifikasi bar bulk tetap menampilkan jumlah `1`
87. Verifikasi baris `Generator Honda EU20i {runId}` pada tabel yang dimuat ulang berstatus `Reported Disposal`

[^drift-1]: Drift foundation vs kontrak komponen. PRD §4.1a menyerahkan seleksi bulk pada `prd-conventions.md` §8. Foundation `prd-conventions.md` §8: «button berubah (toggle) menjadi "Unselect All"». Kontrak `BulkActionButton#41`: «Unselect All (N records)». Diasersi: kontrak, karena label tombol dirender komponen BulkActionButton (SB-7).

[^drift-2]: Drift PRD vs foundation. PRD §4.1a Bulk Action Bar: «| Report Disposal | Disposal | dark |» (aksi tampil sebagai item tabel Bulk Action Bar). Foundation `prd-conventions.md` §8: «Button "Bulk Action" (dropdown trigger) — klik membuka overlay berisi daftar aksi». Diasersi: foundation, karena bulk bar adalah pola bersama (SB-4).
