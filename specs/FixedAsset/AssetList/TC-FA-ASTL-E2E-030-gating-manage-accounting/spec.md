---
id: TC-FA-ASTL-E2E-030-gating-manage-accounting
title: "Gating UI untuk Manage accounting"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-10c", "ASTL-LOGIC-10e", "ASTL-LOGIC-10n", "ASTL-LOGIC-10p", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§2#r1", "§2#r2", "§2#r3", "§2#r4", "§2#r5", "§2#r6", "§2#r7", "§2#r8", "§2#r9", "§2#r10", "§2#r11", "§2#r12", "§2#r13", "§2#r14", "§2#r15", "§2#r16", "§2#p3", "§9.11#r1", "§9.11#r2", "§9.11#r3", "§9.11#r4", "§9.11#r5", "§9.11#r6", "§9.11#r7"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-10c": [31, 45]
  "ASTL-LOGIC-10e": [32, 33]
  "ASTL-LOGIC-10n": 26
  "ASTL-LOGIC-10p": [28, 61]
  "§4.8#r1": [4, 5, 9, 20]
  "§4.8#r2": [10, 65, 66, 69, 70, 74, 79]
  "§4.8#r3": [11, 47, 48, 54, 55]
  "§4.8#r4": 12
  "§4.8#r5": 13
  "§4.8#r6": 21
  "§4.8#r7": 15
  "§4.8#r8": 16
  "§4.8#r9": 14
  "§4.8#r10": 23
  "§4.8#r11": 24
  "§4.8#r12": [17, 24]
  "§4.8#r13": [6, 7]
  "§4.8#r14": [31, 32, 33, 34, 35]
  "§2#r1": [13, 14, 15, 21]
  "§2#r2": 31
  "§2#r3": [17, 24, 34, 35]
  "§2#r4": [11, 31, 32, 33, 45, 55]
  "§2#r5": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r6": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r7": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r8": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r9": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r10": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r11": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r12": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r13": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31, 48, 55, 61]
  "§2#r14": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r15": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#r16": [2, 3, 4, 5, 7, 9, 13, 15, 20, 31]
  "§2#p3": [2, 3, 7, 13, 15]
  "§9.11#r1": [2, 3, 7]
  "§9.11#r2": 31
  "§9.11#r3": [27, 34, 35]
  "§9.11#r4": 28
  "§9.11#r5": [32, 33]
  "§9.11#r6": 40
  "§9.11#r7": 42
anchor: [37, 39]
coverage:
  web: automated
---

# Gating UI untuk Manage accounting

## Prerequisites
- Aktor: `Maya Purnama {runId}`, pemegang role Manage accounting (Read + Update) dengan cakupan Seluruh client.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-030-1: User, Name `Maya Purnama {runId}`, Role `Manage accounting`, Cakupan `Seluruh client`
  - DU-030-2: Group, Name `IT {runId}`
  - DU-030-3: Group, Name `Cabang Bandung {runId}`
  - DU-030-4: Asset, Name `Laptop Pro 16 {runId}`, Group `IT {runId}`, Status `Available`, TAG `RFID` berstatus `Paired`, Asset Class `Peralatan IT {runId}`, Tax Depreciation Class `Kelompok 1 {runId}`, Purchase Date `T0 − 30 hari`, Purchase Cost `18500000`, Warranty Until `T0 + 200 hari`, `Kode Anggaran {runId}` bernilai `AGR-2026-01`
  - DU-030-5: Asset, Name `Kursi Kerja {runId}`, Group `IT {runId}`, Status `Available`
  - DU-030-6: Asset, Name `Kamera Mirrorless {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-030-7: Asset, Name `Printer Laser {runId}`, Group `Cabang Bandung {runId}`, Status `Available`
  - DU-030-8: Custom Field, Name `Nomor PO {runId}`, Group `Purchasing`
  - DU-030-9: Custom Field, Name `Kode Anggaran {runId}`, Group `Accounting`
  - DU-030-10: Asset, Name `Proyektor Rapat {runId}`, Group `IT {runId}`, Status `Borrowed`
  - DU-030-11: Asset, Name `Proyektor Pinjam {runId}`, Group `IT {runId}`, Status `Borrowed`
  - DU-030-12: Asset, Name `Laptop Tugas {runId}`, Group `IT {runId}`, Status `Assigned`
  - Nama baris yang diharapkan untuk Asset Name `Laptop Pro 16 {runId}` adalah `Laptop Pro 16 {runId} - 1`, dari Asset Name `Laptop Pro 16 {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kursi Kerja {runId}` adalah `Kursi Kerja {runId} - 1`, dari Asset Name `Kursi Kerja {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kamera Mirrorless {runId}` adalah `Kamera Mirrorless {runId} - 1`, dari Asset Name `Kamera Mirrorless {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Printer Laser {runId}` adalah `Printer Laser {runId} - 1`, dari Asset Name `Printer Laser {runId}`.
  - Purchase Cost yang diharapkan untuk Purchase Cost `18500000` adalah `Rp 18.500.000,00`, dari Purchase Cost `18500000`.
  - Kursi Kerja {runId} tidak memiliki Purchase Information dan Asset Name-nya tanpa Asset Class; Kamera Mirrorless {runId} adalah aset Unmanaged.
  - Aset `Laptop Pro 16 {runId}` dan `Kursi Kerja {runId}` tercatat di group `IT {runId}`; user hanya mengakses group yang sesuai cakupannya.
  - Nama baris yang diharapkan untuk Asset Name `Proyektor Rapat {runId}` adalah `Proyektor Rapat {runId} - 1`, dari Asset Name `Proyektor Rapat {runId}`.
  - `Proyektor Rapat {runId}` sedang dalam transaksi (Custody `Borrowed`).
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
5. Verifikasi ikon `Changelog` dan tombol `Download` tampil di toolbar
6. Verifikasi Sidebar Group tampil dengan node `All Groups`
7. Verifikasi Sidebar Group memuat node `IT {runId}` dan `Cabang Bandung {runId}`

### Aksi baris pada aset Available
8. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
9. Verifikasi aksi `Detail` tampil
10. Verifikasi aksi `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tidak dirender (Hidden)
11. Verifikasi aksi `Report Disposal` tampil
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
21. Verifikasi aksi `Manage` tidak dirender (Hidden)
22. Tekan Esc

### Checkbox baris, Bar Bulk, dan aksi Bulk
23. Verifikasi checkbox baris dan Bar Bulk tidak dirender (Hidden)
24. Verifikasi aksi Bulk `Print Label`, `Add Label`, `Remove Label`, dan `Edit Purchase` tidak dapat dipilih karena Bar Bulk tidak dirender (Hidden)

### Setup Column dan sel kolom bergerbang
25. Buka Setup Column
26. Verifikasi kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` tersedia di Setup Column
27. Verifikasi kolom custom field Purchasing `Nomor PO {runId}` tidak tersedia di Setup Column
28. Verifikasi kolom custom field Accounting `Kode Anggaran {runId}` tersedia di Setup Column
29. Tampilkan kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry`
30. Tutup Setup Column
31. Verifikasi sel `Asset Value (Commercial)` baris `Kursi Kerja {runId} - 1` menampilkan `Pending`
32. Verifikasi sel `Asset Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `Peralatan IT {runId}`
33. Verifikasi sel `Tax Depreciation Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `Kelompok 1 {runId}`
34. Verifikasi sel `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
35. Verifikasi sel `Purchase Date` dan `Purchase Cost` baris `Kursi Kerja {runId} - 1` menampilkan `No access`, bukan `Pending`

### Dokumen Purchase dan data Accounting di Asset Detail
36. Klik Name `Laptop Pro 16 {runId} - 1`
37. Verifikasi halaman detail aset `Laptop Pro 16 {runId} - 1` terbuka bagi `Maya Purnama {runId}`
38. Buka tab `Documents`
39. Verifikasi tab `Documents` terbuka bagi `Maya Purnama {runId}`
40. Verifikasi kelompok Purchase pada tab `Documents` tidak tampil
41. Buka tab `Accounting`
42. Verifikasi data tab `Accounting` (peringatan fisik vs buku, Depreciation, Acquisition & Value changes, Journals) tampil
43. Muat ulang halaman
44. Ketik Search `{runId}`, tekan Enter

### Hak Asset Value berlaku client-wide
45. Verifikasi sel `Asset Value (Commercial)` baris `Printer Laser {runId} - 1` di group `Cabang Bandung {runId}` menampilkan `Pending`

### Report Disposal tidak ditawarkan pada aset dalam transaksi
46. Klik `⋯` pada baris `Proyektor Rapat {runId} - 1`
47. Verifikasi aksi `Detail` tampil
48. Verifikasi aksi `Report Disposal` tidak dirender (Hidden) pada aset berstatus `Borrowed`
49. Tekan Esc

### Hak diubah menjadi Manage accounting (Read)
50. Admin mengubah hak `Maya Purnama {runId}` menjadi `Manage accounting` (Read)
51. Muat ulang halaman
52. Ketik Search `{runId}`, tekan Enter
53. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
54. Verifikasi aksi `Detail` tampil
55. Verifikasi aksi `Report Disposal` tidak dirender (Hidden)
56. Tekan Esc

### Nilai sel custom field Accounting tampil bagi pemegang hak
57. Ketik Search `{runId}`, tekan Enter
58. Buka Setup Column
59. Tampilkan kolom custom field Accounting `Kode Anggaran {runId}`
60. Tutup Setup Column
61. Verifikasi sel `Kode Anggaran {runId}` baris `Laptop Pro 16 {runId} - 1` menampilkan `AGR-2026-01`

### Mark as Returned dan Mark as Unassigned pada aset Borrowed dan Assigned
62. Muat ulang halaman
63. Ketik Search `{runId}`, tekan Enter
64. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
65. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
66. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
67. Tekan Esc
68. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
69. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Assigned`
70. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
71. Tekan Esc
72. Centang baris `Proyektor Pinjam {runId} - 1`
73. Klik tombol Bulk Action
74. Verifikasi aksi Bulk `Mark as Returned` tidak dirender (Hidden) untuk aset berstatus `Borrowed`
75. Tekan Esc
76. Klik `×` pada Bar Bulk
77. Centang baris `Laptop Tugas {runId} - 1`
78. Klik tombol Bulk Action
79. Verifikasi aksi Bulk `Mark as Unassigned` tidak dirender (Hidden) untuk aset berstatus `Assigned`
80. Tekan Esc
81. Klik `×` pada Bar Bulk
