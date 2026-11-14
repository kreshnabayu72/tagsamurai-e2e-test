---
id: TC-FA-MISS-UI-052-bulk-report-disposal-klien
title: "Bulk bar tab Active: seleksi, counter, tombol Report Disposal aktif selama ada seleksi, dialog blok Cannot Report Disposal, toast skipped, dan kegagalan 5xx"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-BLK-1@tabel-active, EB-BLK-4, §4.1a#p8, §4.1a#p9, §4.2.4#p9, §7.2#r5, §7.3#r13, §6#r11, §6#r13, §4.4#r12, §4.1#r9, §5#r5]
smoke: []
dependsOn: []
trace:
  EB-BLK-1@tabel-active: [2, 3, 5, 6, 7, 9, 11, 12, 15, 16, 18, 20, 22, 30, 31, 45, 47, 58, 68, 76, 77]
  EB-BLK-4: [83, 84, 85, 91, 92, 93]
  §4.1a#p8: [35, 36]
  §4.1a#p9: [35, 40, 65, 66, 75]
  §4.2.4#p9: [54, 55, 65]
  §7.2#r5: [53, 54, 55, 64]
  §7.3#r13: 75
  §6#r11: [53, 54]
  §6#r13: [64, 65, 66]
  §4.4#r12: [53, 54, 64, 65]
  §4.1#r9: [53, 55, 57, 64]
  §5#r5: 35
anchor: []
coverage:
  web: automated
---

# Bulk bar tab Active: seleksi, counter, tombol Report Disposal aktif selama ada seleksi, dialog blok Cannot Report Disposal, toast skipped, dan kegagalan 5xx

## Prerequisites
- Aktor: Group Manager (Aktor Missing) dengan hak Report Disposal.
- Layar awal: Assets > Missing > Active.
- Komponen: Halaman Missing sub-tab Active (tabel T-MIS-01)
- Data:
  - DU-052-1: Dua belas record Missing satu Group. Name `Aset Bulk {n}`; Asset ID `BLK-2026-{n}`; Group `Head Office`; Status `Missing`; Source `Manual`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
  - DU-052-2: Record Missing di Group Warehouse hasil filter. Name `Aset Gudang Hilang - 1`; Asset ID `WHS-2026-0001`; Group `Warehouse`; Status `Missing`; Source `Manual`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
  - DU-052-3: Record Missing di Group Head Office. Name `Aset Head Office - 1`; Asset ID `HOF-2026-0001`; Group `Head Office`; Status `Missing`; Source `Manual`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
  - DU-052-4: Dua record Missing yang seluruhnya dilewati. Name `Aset Semua Dilewati {n}`; Asset ID `SDL-2026-{n}`; Group `Head Office`; Status `Missing`; Source `Manual`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
  - DU-052-5: Tiga record Missing yang sebagian dilewati. Name `Aset Sebagian Dilewati {n}`; Asset ID `SBD-2026-{n}`; Group `Head Office`; Status `Missing`; Source `Manual`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
  - DU-052-6: Dua record Missing untuk kegagalan server. Name `Aset Gagal Bulk {n}`; Asset ID `GGL-2026-{n}`; Group `Head Office`; Status `Missing`; Source `Manual`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
  - DU-052-7: Record Waiting for Confirmation. Name `Aset Menunggu Konfirmasi - 1`; Asset ID `WFC-2026-0001`; Group `Head Office`; Status `Waiting for Confirmation`; Source `Reported by holder`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
- Kondisi:
  - K1: daftar Active berisi DU-052-1 (12 record) dengan ukuran halaman bawaan; filter `Group` bernilai `Warehouse` dijawab daftar berisi DU-052-2
  - K2: daftar Active berisi DU-052-3; Report Disposal atas seleksi membuka dialog Report Disposal
  - K3: daftar Active berisi DU-052-2 dan DU-052-3; Report Disposal atas seleksi dijawab blokir karena aset terpilih berasal dari lebih dari satu Group
  - K4: daftar Active berisi DU-052-4 (2 record); Report Disposal atas seleksi dijawab bahwa seluruh record terpilih dilewati
  - K5: daftar Active berisi DU-052-5 (3 record); Report Disposal atas seleksi dijawab bahwa sebagian record dilewati
  - K6: daftar Active berisi DU-052-6 (2 record); Report Disposal atas seleksi dijawab error server
  - K7: daftar Active berisi DU-052-6 (2 record); Report Disposal atas seleksi tidak dijawab sampai melewati batas waktu
  - K8: daftar Active berisi DU-052-3 dan DU-052-7

## Test Steps

### Seleksi baris: bar, counter, checkbox header, dan pembersihan
1. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
2. Verifikasi baris `Aset Bulk 1` tampil pada tabel
3. Verifikasi bulk bar tidak tampil sebelum ada baris terpilih
4. Centang baris `Aset Bulk 1`
5. Verifikasi bulk bar tampil
6. Verifikasi counter seleksi menampilkan jumlah `1` dalam bentuk tunggal
7. Verifikasi checkbox header berstatus indeterminate
8. Centang baris `Aset Bulk 2`
9. Verifikasi counter seleksi menampilkan jumlah `2` dalam bentuk jamak
10. Klik `×` pada bulk bar
11. Verifikasi baris `Aset Bulk 1` tidak lagi tercentang
12. Verifikasi bulk bar tidak tampil sesudah seleksi dibersihkan

### Seleksi satu halaman penuh dan lintas halaman
13. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
14. Centang checkbox header
15. Verifikasi checkbox header berstatus checked
16. Verifikasi counter seleksi menampilkan jumlah `10`
17. Klik halaman `2`
18. Verifikasi counter seleksi tetap menampilkan jumlah `10` pada halaman `2`
19. Centang baris `Aset Bulk 11`
20. Verifikasi counter seleksi menampilkan jumlah `11`
21. Klik halaman `1`
22. Verifikasi baris `Aset Bulk 1` masih tercentang

### Seleksi bertahan saat baris tersaring keluar
23. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
24. Centang baris `Aset Bulk 1`
25. Centang baris `Aset Bulk 2`
26. Klik tombol Filter
27. Klik field `Group`
28. Centang node `Warehouse`
29. Klik tombol `[Apply]`
30. Verifikasi baris `Aset Gudang Hilang - 1` tampil sesudah filter
31. Verifikasi counter seleksi tetap menampilkan jumlah `2` walau baris terpilih tidak tampil

### Menu Bulk Action hanya memuat Report Disposal dan aktif selama ada seleksi
32. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K8
33. Centang baris `Aset Head Office - 1`
34. Klik `Bulk Action`
35. Verifikasi opsi `Report Disposal` tampil dan aktif pada menu Bulk Action
36. Verifikasi tidak ada opsi `Review`, `Confirm`, `Reject`, dan `Mark as Found` pada menu Bulk Action
37. Tekan Esc
38. Centang baris `Aset Menunggu Konfirmasi - 1`
39. Klik `Bulk Action`
40. Verifikasi opsi `Report Disposal` tetap aktif pada seleksi dengan status campuran

### Batalkan dialog tidak memproses apa pun
41. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K2
42. Centang baris `Aset Head Office - 1`
43. Klik `Bulk Action`
44. Klik `Report Disposal`
45. Verifikasi dialog Report Disposal terbuka
46. Tutup dialog Report Disposal tanpa mengirim
47. Verifikasi bulk bar masih tampil dengan counter seleksi `1`

### Dialog blok Cannot Report Disposal untuk aset lintas Group
48. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K3
49. Centang baris `Aset Gudang Hilang - 1`
50. Centang baris `Aset Head Office - 1`
51. Klik `Bulk Action`
52. Klik `Report Disposal`
53. Verifikasi dialog `Cannot Report Disposal` tampil
54. Verifikasi pesan `Selected assets come from more than one group. Select assets from one group.` tampil pada dialog
55. Verifikasi tombol `[OK]` tampil pada dialog
56. Klik `[OK]`
57. Verifikasi dialog `Cannot Report Disposal` tertutup
58. Verifikasi counter seleksi tetap menampilkan jumlah `2`

### Dialog blok Cannot Report Disposal saat semua record dilewati
59. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K4
60. Centang baris `Aset Semua Dilewati 1`
61. Centang baris `Aset Semua Dilewati 2`
62. Klik `Bulk Action`
63. Klik `Report Disposal`
64. Verifikasi dialog `Cannot Report Disposal` tampil
65. Verifikasi pesan `None of the selected records can be reported for disposal.` tampil pada dialog
66. Verifikasi tidak ada toast sukses yang tampil
67. Klik `[OK]`
68. Verifikasi counter seleksi tetap menampilkan jumlah `2` sesudah dialog ditutup

### Toast sebagian record dilewati dan seleksi bersih sesudah aksi selesai
69. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K5
70. Centang baris `Aset Sebagian Dilewati 1`
71. Centang baris `Aset Sebagian Dilewati 2`
72. Centang baris `Aset Sebagian Dilewati 3`
73. Klik `Bulk Action`
74. Klik `Report Disposal`
75. Verifikasi toast `Success, disposal report has been created. Some items were skipped.` tampil
76. Verifikasi bulk bar tidak tampil sesudah aksi selesai
77. Verifikasi baris `Aset Sebagian Dilewati 1` tidak tercentang

### Bulk gagal karena error server mempertahankan bar dan seleksi
78. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K6
79. Centang baris `Aset Gagal Bulk 1`
80. Centang baris `Aset Gagal Bulk 2`
81. Klik `Bulk Action`
82. Klik `Report Disposal`
83. Verifikasi toast error tampil
84. Verifikasi bulk bar masih tampil
85. Verifikasi counter seleksi tetap menampilkan jumlah `2`

### Bulk melewati batas waktu mempertahankan bar dan seleksi
86. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K7
87. Centang baris `Aset Gagal Bulk 1`
88. Centang baris `Aset Gagal Bulk 2`
89. Klik `Bulk Action`
90. Klik `Report Disposal`
91. Verifikasi toast `Connection problem. Please try again.` tampil
92. Verifikasi bulk bar masih tampil
93. Verifikasi counter seleksi tetap menampilkan jumlah `2`
