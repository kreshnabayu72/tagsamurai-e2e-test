---
id: TC-FA-ASTL-E2E-027-gating-group-manager
title: "Gating UI untuk Group Manager"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-10c", "ASTL-LOGIC-10d", "ASTL-LOGIC-10g", "ASTL-LOGIC-10n", "ASTL-LOGIC-10o", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§2#r1", "§2#r2", "§2#r3", "§2#r4", "§2#r5", "§2#r6", "§2#r7", "§2#r8", "§2#r9", "§2#r10", "§2#r11", "§2#r12", "§2#r13", "§2#r14", "§2#r15", "§2#r16", "§2#p3", "§9.11#r1", "§9.11#r2", "§9.11#r3", "§9.11#r4", "§9.11#r5", "§9.11#r6", "§9.11#r7"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-10c": 37
  "ASTL-LOGIC-10d": [40, 41, 42, 43]
  "ASTL-LOGIC-10g": [37, 38, 39, 40, 41, 42, 43]
  "ASTL-LOGIC-10n": 32
  "ASTL-LOGIC-10o": 33
  "§4.8#r1": [4, 5, 9, 20]
  "§4.8#r2": [10, 26, 69, 70, 73, 74, 78, 83]
  "§4.8#r3": 11
  "§4.8#r4": 12
  "§4.8#r5": [13, 55]
  "§4.8#r6": [21, 60]
  "§4.8#r7": [15, 60, 91, 95]
  "§4.8#r8": 16
  "§4.8#r9": 14
  "§4.8#r10": 24
  "§4.8#r11": 27
  "§4.8#r12": [17, 28]
  "§4.8#r13": [6, 7]
  "§4.8#r14": [37, 38, 39, 40, 41, 42, 43]
  "§2#r1": [13, 14, 15, 21]
  "§2#r2": 37
  "§2#r3": [17, 28, 40, 41, 42, 43]
  "§2#r4": [11, 37, 38, 39]
  "§2#r5": [2, 3, 4, 5, 7, 9, 13, 15, 20, 37]
  "§2#r6": [2, 3, 4, 5, 7, 9, 13, 15, 20, 37]
  "§2#r7": [2, 3, 4, 5, 7, 9, 13, 15, 20, 21, 37]
  "§2#r8": [2, 3, 4, 5, 7, 9, 13, 15, 20, 37]
  "§2#r9": [2, 3, 4, 5, 7, 9, 13, 15, 20, 37]
  "§2#r10": [2, 3, 4, 5, 7, 9, 13, 15, 20, 37]
  "§2#r11": [2, 3, 4, 5, 7, 9, 13, 15, 20, 37]
  "§2#r12": [2, 3, 4, 5, 7, 9, 13, 15, 20, 37]
  "§2#r13": [2, 3, 4, 5, 7, 9, 13, 15, 20, 37]
  "§2#r14": [2, 3, 4, 5, 7, 9, 13, 15, 20, 37]
  "§2#r15": [2, 3, 4, 5, 7, 9, 13, 15, 20, 37]
  "§2#r16": [2, 3, 4, 5, 7, 9, 13, 15, 20, 37]
  "§2#p3": [2, 3, 7, 13, 15, 21]
  "§9.11#r1": [2, 3, 7, 64]
  "§9.11#r2": 37
  "§9.11#r3": [33, 40, 41, 42, 43]
  "§9.11#r4": 34
  "§9.11#r5": [38, 39]
  "§9.11#r6": 47
  "§9.11#r7": 50
anchor: [45, 49]
coverage:
  web: automated
---

# Gating UI untuk Group Manager

## Prerequisites
- Aktor: `Tomi Wijaya {runId}`, pemegang role Group Manager dengan cakupan Group `IT {runId}` beserta descendant.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-027-1: User, Name `Tomi Wijaya {runId}`, Role `Group Manager`, Cakupan `Group IT {runId} beserta descendant`
  - DU-027-2: Group, Name `IT {runId}`
  - DU-027-3: Group, Name `Cabang Bandung {runId}`
  - DU-027-4: Asset, Name `Laptop Pro 16 {runId}`, Group `IT {runId}`, Status `Available`, TAG `RFID` berstatus `Paired`, Asset Class `Peralatan IT {runId}`, Tax Depreciation Class `Kelompok 1 {runId}`, Purchase Date `T0 − 30 hari`, Purchase Cost `18500000`, Warranty Until `T0 + 200 hari`
  - DU-027-5: Asset, Name `Kursi Kerja {runId}`, Group `IT {runId}`, Status `Available`
  - DU-027-6: Asset, Name `Kamera Mirrorless {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-027-7: Asset, Name `Printer Laser {runId}`, Group `Cabang Bandung {runId}`, Status `Available`
  - DU-027-8: Custom Field, Name `Nomor PO {runId}`, Group `Purchasing`
  - DU-027-9: Custom Field, Name `Kode Anggaran {runId}`, Group `Accounting`
  - DU-027-10: Asset, Name `Proyektor Pinjam {runId}`, Group `IT {runId}`, Status `Borrowed`
  - DU-027-11: Asset, Name `Laptop Tugas {runId}`, Group `IT {runId}`, Status `Assigned`
  - DU-027-12: Asset, Name `Kamera Cabang {runId}`, Group `Cabang Bandung {runId}`, Status `Available`, License `Unmanaged`
  - DU-027-13: User role tambahan, Name `Tomi Wijaya {runId}`, Role `Manage asset & TAG` (Read + Update), Cakupan `Group Cabang Bandung {runId}`; baru diberikan di langkah 86 dan tidak berlaku sebelum langkah itu
  - Nama baris yang diharapkan untuk Asset Name `Laptop Pro 16 {runId}` adalah `Laptop Pro 16 {runId} - 1`, dari Asset Name `Laptop Pro 16 {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kursi Kerja {runId}` adalah `Kursi Kerja {runId} - 1`, dari Asset Name `Kursi Kerja {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kamera Mirrorless {runId}` adalah `Kamera Mirrorless {runId} - 1`, dari Asset Name `Kamera Mirrorless {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Printer Laser {runId}` adalah `Printer Laser {runId} - 1`, dari Asset Name `Printer Laser {runId}`.
  - Purchase Cost yang diharapkan untuk Purchase Cost `18500000` adalah `Rp 18.500.000,00`, dari Purchase Cost `18500000`.
  - Kursi Kerja {runId} tidak memiliki Purchase Information dan Asset Name-nya tanpa Asset Class; Kamera Mirrorless {runId} adalah aset Unmanaged.
  - Aset `Laptop Pro 16 {runId}` dan `Kursi Kerja {runId}` tercatat di group `IT {runId}`; user hanya mengakses group yang sesuai cakupannya.
  - Nama baris yang diharapkan untuk Asset Name `Proyektor Pinjam {runId}` adalah `Proyektor Pinjam {runId} - 1`, dari Asset Name `Proyektor Pinjam {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Laptop Tugas {runId}` adalah `Laptop Tugas {runId} - 1`, dari Asset Name `Laptop Tugas {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kamera Cabang {runId}` adalah `Kamera Cabang {runId} - 1`, dari Asset Name `Kamera Cabang {runId}`.
  - `Proyektor Pinjam {runId}` sedang dipinjam (Custody `Borrowed`) dan `Laptop Tugas {runId}` sedang ditugaskan (Custody `Assigned`).
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Lisensi `FA-7` aktif pada entitas.
  - Feature Suite Borrow, Assignment, dan Transfer berada di level `Full`.

## Test Steps

### Tabel, kartu, dan cakupan group tampil sesuai hak
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Pro 16 {runId} - 1`, `Kursi Kerja {runId} - 1`, dan `Kamera Mirrorless {runId} - 1` tampil di tabel
3. Verifikasi baris `Printer Laser {runId} - 1` tidak tampil di tabel
4. Verifikasi tabel dan kartu status `All` tampil
5. Verifikasi ikon `Changelog` dan tombol `Download` tampil di toolbar
6. Verifikasi Sidebar Group tampil dengan node `All Groups`
7. Verifikasi Sidebar Group memuat node `IT {runId}` dan tidak memuat node `Cabang Bandung {runId}`

### Aksi baris pada aset Available
8. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
9. Verifikasi aksi `Detail` tampil
10. Verifikasi aksi `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tampil
11. Verifikasi aksi `Report Disposal` tampil
12. Verifikasi aksi `Report Damage` dan `Report Missing` tampil
13. Verifikasi aksi `Edit` dan `Replace TAG` tampil
14. Verifikasi aksi `Print Label` tampil
15. Verifikasi aksi `Delete Asset Data` tidak dirender (Hidden) pada aset managed yang belum Disposed
16. Verifikasi aksi `Report TAG` tidak dirender (Hidden)
17. Verifikasi aksi `Edit Purchase` tampil
18. Tekan Esc

### Aksi Manage pada aset Unmanaged
19. Klik `⋯` pada baris `Kamera Mirrorless {runId} - 1`
20. Verifikasi aksi `Detail` tampil
21. Verifikasi aksi `Manage` dan `Delete Asset Data` tampil
22. Tekan Esc

### Checkbox baris, Bar Bulk, dan aksi Bulk
23. Centang baris `Laptop Pro 16 {runId} - 1`
24. Verifikasi checkbox baris dan Bar Bulk tampil
25. Klik tombol Bulk Action
26. Verifikasi aksi Bulk `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tampil
27. Verifikasi aksi Bulk `Print Label`, `Add Label`, dan `Remove Label` tampil
28. Verifikasi aksi Bulk `Edit Purchase` tampil
29. Tekan Esc
30. Klik `×` pada Bar Bulk

### Setup Column dan sel kolom bergerbang
31. Buka Setup Column
32. Verifikasi kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` tersedia di Setup Column
33. Verifikasi kolom custom field Purchasing `Nomor PO {runId}` tersedia di Setup Column
34. Verifikasi kolom custom field Accounting `Kode Anggaran {runId}` tidak tersedia di Setup Column
35. Tampilkan kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry`
36. Tutup Setup Column
37. Verifikasi sel `Asset Value (Commercial)` baris `Kursi Kerja {runId} - 1` menampilkan `Pending`
38. Verifikasi sel `Asset Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
39. Verifikasi sel `Tax Depreciation Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
40. Verifikasi sel `Purchase Date` baris `Laptop Pro 16 {runId} - 1` menampilkan tanggal `T0 − 30 hari` dalam format `dd/MM/yy`
41. Verifikasi sel `Purchase Cost` baris `Laptop Pro 16 {runId} - 1` menampilkan `Rp 18.500.000,00`
42. Verifikasi sel `Purchase Date` dan `Purchase Cost` baris `Kursi Kerja {runId} - 1` menampilkan `Pending`
43. Verifikasi sel `Warranty Expiry` baris `Laptop Pro 16 {runId} - 1` menampilkan tanggal `T0 + 200 hari` dalam format `dd/MM/yy`

### Dokumen Purchase dan data Accounting di Asset Detail
44. Klik Name `Laptop Pro 16 {runId} - 1`
45. Verifikasi halaman detail aset `Laptop Pro 16 {runId} - 1` terbuka bagi `Tomi Wijaya {runId}`
46. Buka tab `Documents`
47. Verifikasi kelompok Purchase pada tab `Documents` tampil
48. Buka tab `Accounting`
49. Verifikasi tab `Accounting` terbuka bagi `Tomi Wijaya {runId}`
50. Verifikasi data tab `Accounting` (peringatan fisik vs buku, Depreciation, Acquisition & Value changes, Journals) tidak tampil

### Aksi Bulk Batch Replace TAG, Manage, dan Delete Asset Data
51. Muat ulang halaman
52. Ketik Search `{runId}`, tekan Enter
53. Centang baris `Laptop Pro 16 {runId} - 1`
54. Klik tombol Bulk Action
55. Verifikasi aksi Bulk `Batch Replace TAG` tampil
56. Tekan Esc
57. Klik `×` pada Bar Bulk
58. Centang baris `Kamera Mirrorless {runId} - 1`
59. Klik tombol Bulk Action
60. Verifikasi aksi Bulk `Manage` dan `Delete Asset Data` tampil
61. Tekan Esc
62. Klik `×` pada Bar Bulk

### Changelog dibatasi cakupan group
63. Klik ikon `Changelog`
64. Verifikasi modal Changelog tidak memuat entri aset `Printer Laser {runId} - 1` di luar cakupan group
65. Tekan Esc

### Mark as Returned dan Mark as Unassigned pada aset Borrowed dan Assigned
66. Muat ulang halaman
67. Ketik Search `{runId}`, tekan Enter
68. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
69. Verifikasi aksi `Mark as Returned` tampil pada aset berstatus `Borrowed`
70. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
71. Tekan Esc
72. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
73. Verifikasi aksi `Mark as Unassigned` tampil pada aset berstatus `Assigned`
74. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
75. Tekan Esc
76. Centang baris `Proyektor Pinjam {runId} - 1`
77. Klik tombol Bulk Action
78. Verifikasi aksi Bulk `Mark as Returned` tampil untuk aset berstatus `Borrowed`
79. Tekan Esc
80. Klik `×` pada Bar Bulk
81. Centang baris `Laptop Tugas {runId} - 1`
82. Klik tombol Bulk Action
83. Verifikasi aksi Bulk `Mark as Unassigned` tampil untuk aset berstatus `Assigned`
84. Tekan Esc
85. Klik `×` pada Bar Bulk

### Seleksi campuran lintas group tidak menawarkan aksi Bulk di luar hak
86. Admin menambahkan hak `Manage asset & TAG` (Read + Update) untuk `Tomi Wijaya {runId}` pada group `Cabang Bandung {runId}`, tanpa mengubah hak `Group Manager` pada group `IT {runId}`
87. Muat ulang halaman
88. Ketik Search `{runId}`, tekan Enter
89. Centang baris `Kamera Mirrorless {runId} - 1`
90. Klik tombol Bulk Action
91. Verifikasi aksi Bulk `Delete Asset Data` tampil untuk seleksi yang seluruhnya berada di group `IT {runId}`
92. Tekan Esc
93. Centang baris `Kamera Cabang {runId} - 1`
94. Klik tombol Bulk Action
95. Verifikasi aksi Bulk `Delete Asset Data` tidak dirender (Hidden) karena sebagian aset terpilih berada di group `Cabang Bandung {runId}` yang di luar hak Delete
96. Tekan Esc
97. Klik `×` pada Bar Bulk
