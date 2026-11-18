---
id: TC-FA-ASTL-E2E-026-gating-read-only
title: "Gating UI untuk Read Only"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-10f", "ASTL-LOGIC-10n", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§2#r1", "§2#r2", "§2#r3", "§2#r4", "§2#r5", "§2#r6", "§2#r7", "§2#r8", "§2#r9", "§2#r10", "§2#r11", "§2#r12", "§2#r13", "§2#r14", "§2#r15", "§2#r16", "§2#p3", "§9.11#r1", "§9.11#r2", "§9.11#r3", "§9.11#r4", "§9.11#r5", "§9.11#r6", "§9.11#r7", "EB-AKS-4"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-10f": [31, 32, 33, 34, 35, 36, 37]
  "ASTL-LOGIC-10n": 26
  "§4.8#r1": [4, 5, 9, 20, 61]
  "§4.8#r2": [10, 78, 79, 82, 83]
  "§4.8#r3": 11
  "§4.8#r4": 12
  "§4.8#r5": 13
  "§4.8#r6": 21
  "§4.8#r7": 15
  "§4.8#r8": [16, 21, 62]
  "§4.8#r9": [5, 14]
  "§4.8#r10": 23
  "§4.8#r11": 24
  "§4.8#r12": [17, 24]
  "§4.8#r13": [6, 7]
  "§4.8#r14": [31, 32, 33, 34, 35, 36, 37]
  "§2#r1": [13, 14, 15, 21]
  "§2#r2": 31
  "§2#r3": [17, 24, 34, 35, 36, 37]
  "§2#r4": [11, 31, 32, 33]
  "§2#r5": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r6": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r7": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r8": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r9": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r10": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r11": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r12": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r13": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r14": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r15": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r16": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#p3": [2, 3, 7, 13, 15]
  "§9.11#r1": [2, 3, 7]
  "§9.11#r2": 31
  "§9.11#r3": [27, 34, 35, 36, 37]
  "§9.11#r4": 28
  "§9.11#r5": [32, 33]
  "§9.11#r6": 40
  "§9.11#r7": 42
  "EB-AKS-4": [45, 46, 48, 50, 52, 54, 55, 57, 69, 70, 74, 89]
anchor: []
coverage:
  web: automated
---

# Gating UI untuk Read Only

## Prerequisites
- Aktor: `Dewi Lestari {runId}`, pemegang role Read Only dengan cakupan Seluruh client.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-026-1: User, Name `Dewi Lestari {runId}`, Role `Read Only`, Cakupan `Seluruh client`
  - DU-026-2: Group, Name `IT {runId}`
  - DU-026-3: Group, Name `Cabang Bandung {runId}`
  - DU-026-4: Asset, Name `Laptop Pro 16 {runId}`, Group `IT {runId}`, Status `Available`, TAG `RFID` berstatus `Paired`, Asset Class `Peralatan IT {runId}`, Tax Depreciation Class `Kelompok 1 {runId}`, Purchase Date `T0 − 30 hari`, Purchase Cost `18500000`, Warranty Until `T0 + 200 hari`
  - DU-026-5: Asset, Name `Kursi Kerja {runId}`, Group `IT {runId}`, Status `Available`
  - DU-026-6: Asset, Name `Kamera Mirrorless {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-026-7: Asset, Name `Printer Laser {runId}`, Group `Cabang Bandung {runId}`, Status `Available`
  - DU-026-8: Custom Field, Name `Nomor PO {runId}`, Group `Purchasing`
  - DU-026-9: Custom Field, Name `Kode Anggaran {runId}`, Group `Accounting`
  - DU-026-10: Asset, Name `Proyektor Pinjam {runId}`, Group `IT {runId}`, Status `Borrowed`
  - DU-026-11: Asset, Name `Laptop Tugas {runId}`, Group `IT {runId}`, Status `Assigned`
  - Nama baris yang diharapkan untuk Asset Name `Laptop Pro 16 {runId}` adalah `Laptop Pro 16 {runId} - 1`, dari Asset Name `Laptop Pro 16 {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kursi Kerja {runId}` adalah `Kursi Kerja {runId} - 1`, dari Asset Name `Kursi Kerja {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kamera Mirrorless {runId}` adalah `Kamera Mirrorless {runId} - 1`, dari Asset Name `Kamera Mirrorless {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Printer Laser {runId}` adalah `Printer Laser {runId} - 1`, dari Asset Name `Printer Laser {runId}`.
  - Purchase Cost yang diharapkan untuk Purchase Cost `18500000` adalah `Rp 18.500.000,00`, dari Purchase Cost `18500000`.
  - Kursi Kerja {runId} tidak memiliki Purchase Information dan Asset Name-nya tanpa Asset Class; Kamera Mirrorless {runId} adalah aset Unmanaged.
  - Aset `Laptop Pro 16 {runId}` dan `Kursi Kerja {runId}` tercatat di group `IT {runId}`; user hanya mengakses group yang sesuai cakupannya.
  - Nama baris yang diharapkan untuk Asset Name `Proyektor Pinjam {runId}` adalah `Proyektor Pinjam {runId} - 1`, dari Asset Name `Proyektor Pinjam {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Laptop Tugas {runId}` adalah `Laptop Tugas {runId} - 1`, dari Asset Name `Laptop Tugas {runId}`.
  - `Proyektor Pinjam {runId}` sedang dipinjam (Custody `Borrowed`) dan `Laptop Tugas {runId}` sedang ditugaskan (Custody `Assigned`).
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Lisensi `FA-7` aktif pada entitas.
  - Feature Suite Borrow, Assignment, dan Transfer berada di level `Full`.

## Test Steps

### Tabel, kartu, dan cakupan group tampil sesuai hak
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Pro 16 {runId} - 1`, `Kursi Kerja {runId} - 1`, dan `Kamera Mirrorless {runId} - 1` tampil di tabel
3. Verifikasi baris `Printer Laser {runId} - 1` di group `Cabang Bandung {runId}` tampil di tabel
4. Verifikasi tabel dan kartu status `All` tampil
5. Verifikasi ikon `Changelog` dan tombol `Download` tampil di toolbar, dan tombol `Print Label` tidak dirender (Hidden)
6. Verifikasi Sidebar Group tampil dengan node `All Groups`
7. Verifikasi Sidebar Group memuat node `IT {runId}` dan `Cabang Bandung {runId}`

### Aksi baris pada aset Available
8. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
9. Verifikasi aksi `Detail` tampil
10. Verifikasi aksi `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tidak dirender (Hidden)
11. Verifikasi aksi `Report Disposal` tidak dirender (Hidden)
12. Verifikasi aksi `Report Damage` dan `Report Missing` tidak dirender (Hidden)
13. Verifikasi aksi `Edit` dan `Replace TAG` tidak dirender (Hidden)
14. Verifikasi aksi `Print Label` tidak dirender (Hidden)
15. Verifikasi aksi `Delete Asset Data` tidak dirender (Hidden)
16. Verifikasi aksi `Report TAG` tampil
17. Verifikasi aksi `Edit Purchase` tidak dirender (Hidden)
18. Tekan Esc

### Aksi Manage pada aset Unmanaged
19. Klik `⋯` pada baris `Kamera Mirrorless {runId} - 1`
20. Verifikasi aksi `Detail` tampil
21. Verifikasi aksi `Manage` dan `Report TAG` tidak dirender (Hidden) pada aset Unmanaged
22. Tekan Esc

### Checkbox baris, Bar Bulk, dan aksi Bulk
23. Verifikasi checkbox baris dan Bar Bulk tidak dirender (Hidden)
24. Verifikasi aksi Bulk `Print Label`, `Add Label`, `Remove Label`, dan `Edit Purchase` tidak dapat dipilih karena Bar Bulk tidak dirender (Hidden)

### Setup Column dan sel kolom bergerbang
25. Buka Setup Column
26. Verifikasi kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` tersedia di Setup Column
27. Verifikasi kolom custom field Purchasing `Nomor PO {runId}` tersedia di Setup Column
28. Verifikasi kolom custom field Accounting `Kode Anggaran {runId}` tersedia di Setup Column
29. Tampilkan kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry`
30. Tutup Setup Column
31. Verifikasi sel `Asset Value (Commercial)` baris `Kursi Kerja {runId} - 1` menampilkan `Pending`
32. Verifikasi sel `Asset Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `Peralatan IT {runId}`
33. Verifikasi sel `Tax Depreciation Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `Kelompok 1 {runId}`
34. Verifikasi sel `Purchase Date` baris `Laptop Pro 16 {runId} - 1` menampilkan tanggal `T0 − 30 hari` dalam format `dd/MM/yy`
35. Verifikasi sel `Purchase Cost` baris `Laptop Pro 16 {runId} - 1` menampilkan `Rp 18.500.000,00`
36. Verifikasi sel `Purchase Date` dan `Purchase Cost` baris `Kursi Kerja {runId} - 1` menampilkan `Pending`
37. Verifikasi sel `Warranty Expiry` baris `Laptop Pro 16 {runId} - 1` menampilkan tanggal `T0 + 200 hari` dalam format `dd/MM/yy`

### Dokumen Purchase dan data Accounting di Asset Detail
38. Klik Name `Laptop Pro 16 {runId} - 1`
39. Buka tab `Documents`
40. Verifikasi kelompok Purchase pada tab `Documents` tampil
41. Buka tab `Accounting`
42. Verifikasi data tab `Accounting` (peringatan fisik vs buku, Depreciation, Acquisition & Value changes, Journals) tampil

### Search, Filter, Sort, Pagination, dan Setup Column aktif
43. Muat ulang halaman
44. Ketik Search `Kursi Kerja {runId}`, tekan Enter
45. Verifikasi baris `Kursi Kerja {runId} - 1` tampil sesudah Search
46. Verifikasi baris `Laptop Pro 16 {runId} - 1` tidak tampil sesudah Search
47. Ganti isi kotak search dengan `{runId}`, tekan Enter
48. Verifikasi baris `Laptop Pro 16 {runId} - 1` dan `Kursi Kerja {runId} - 1` tampil sesudah Search diganti
49. Klik tombol Filter
50. Verifikasi panel Filter terbuka
51. Klik tombol Filter
52. Verifikasi baris `Laptop Pro 16 {runId} - 1` tampil sebelum baris `Printer Laser {runId} - 1` pada urutan Name A–Z
53. Klik header kolom `Name`
54. Verifikasi baris `Printer Laser {runId} - 1` tampil sebelum baris `Laptop Pro 16 {runId} - 1` pada urutan Name Z–A
55. Verifikasi Pagination tampil di bawah tabel
56. Buka Setup Column
57. Verifikasi Setup Column terbuka dan kolom `Alias Name` dapat dipilih

### Report TAG hanya ditawarkan untuk aset managed dengan TAG Paired
58. Muat ulang halaman
59. Ketik Search `{runId}`, tekan Enter
60. Klik `⋯` pada baris `Kursi Kerja {runId} - 1`
61. Verifikasi aksi `Detail` tampil
62. Verifikasi aksi `Report TAG` tidak dirender (Hidden) pada aset tanpa TAG Paired
63. Tekan Esc

### Filter dan Pagination dipakai
64. Muat ulang halaman
65. Ketik Search `{runId}`, tekan Enter
66. Klik ikon Filter
67. Pilih Status `Unmanaged` pada Filter Panel
68. Klik `[Apply]`
69. Verifikasi baris `Kamera Mirrorless {runId} - 1` tampil sebagai hasil Filter
70. Verifikasi laporan halaman menampilkan `Showing 1 to 1 of 1` dan tombol `Next Page` tidak aktif

### Setup Column dipakai
71. Buka Setup Column
72. Tampilkan kolom `Alias Name`
73. Tutup Setup Column
74. Verifikasi kolom `Alias Name` tampil sebagai header tabel

### Mark as Returned dan Mark as Unassigned pada aset Borrowed dan Assigned
75. Muat ulang halaman
76. Ketik Search `{runId}`, tekan Enter
77. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
78. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
79. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
80. Tekan Esc
81. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
82. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Assigned`
83. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
84. Tekan Esc

### Pagination dipakai mengganti ukuran halaman
85. Muat ulang halaman
86. Ketik Search `{runId}`, tekan Enter
87. Klik dropdown `Rows per page`
88. Pilih ukuran halaman `25`
89. Verifikasi dropdown `Rows per page` menampilkan `25` dan laporan halaman menampilkan `Showing 1 to 6 of 6`
