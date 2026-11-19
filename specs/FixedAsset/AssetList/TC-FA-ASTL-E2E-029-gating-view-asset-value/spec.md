---
id: TC-FA-ASTL-E2E-029-gating-view-asset-value
title: "Gating UI untuk View asset value"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-10c", "ASTL-LOGIC-10k", "ASTL-LOGIC-10l", "ASTL-LOGIC-10n", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§2#r1", "§2#r2", "§2#r3", "§2#r4", "§2#r5", "§2#r6", "§2#r7", "§2#r8", "§2#r9", "§2#r10", "§2#r11", "§2#r12", "§2#r13", "§2#r14", "§2#r15", "§2#r16", "§2#p3", "§9.11#r1", "§9.11#r2", "§9.11#r3", "§9.11#r4", "§9.11#r5", "§9.11#r6", "§9.11#r7"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-10c": [31, 47, 48, 49]
  "ASTL-LOGIC-10k": [32, 33, 34, 35]
  "ASTL-LOGIC-10l": 35
  "ASTL-LOGIC-10n": 26
  "§4.8#r1": [4, 5, 9, 20]
  "§4.8#r2": [10, 53, 54, 57, 58]
  "§4.8#r3": 11
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
  "§9.11#r3": [27, 34, 35]
  "§9.11#r4": 28
  "§9.11#r5": [32, 33]
  "§9.11#r6": 40
  "§9.11#r7": 43
anchor: [37, 39, 42]
coverage:
  web: automated
---

# Gating UI untuk View asset value

## Prerequisites
- Aktor: `Anita Kusuma {runId}`, pemegang role View asset value dengan cakupan Group `IT {runId}` beserta descendant.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-029-1: User, Name `Anita Kusuma {runId}`, Role `View asset value`, Cakupan `Group IT {runId} beserta descendant`
  - DU-029-2: Group, Name `IT {runId}`, Anak `IT Support {runId}`
  - DU-029-3: Group, Name `Cabang Bandung {runId}`
  - DU-029-4: Asset, Name `Laptop Pro 16 {runId}`, Group `IT {runId}`, Status `Available`, TAG `RFID` berstatus `Paired`, Asset Class `Peralatan IT {runId}`, Tax Depreciation Class `Kelompok 1 {runId}`, Purchase Date `T0 − 30 hari`, Purchase Cost `18500000`, Warranty Until `T0 + 200 hari`
  - DU-029-5: Asset, Name `Kursi Kerja {runId}`, Group `IT {runId}`, Status `Available`
  - DU-029-6: Asset, Name `Kamera Mirrorless {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-029-7: Asset, Name `Printer Laser {runId}`, Group `Cabang Bandung {runId}`, Status `Available`
  - DU-029-8: Custom Field, Name `Nomor PO {runId}`, Group `Purchasing`
  - DU-029-9: Custom Field, Name `Kode Anggaran {runId}`, Group `Accounting`
  - DU-029-10: Asset, Name `Monitor Ultrawide {runId}`, Group `IT Support {runId}`, Status `Available`
  - DU-029-11: Asset, Name `Proyektor Pinjam {runId}`, Group `IT {runId}`, Status `Borrowed`
  - DU-029-12: Asset, Name `Laptop Tugas {runId}`, Group `IT {runId}`, Status `Assigned`
  - Nama baris yang diharapkan untuk Asset Name `Laptop Pro 16 {runId}` adalah `Laptop Pro 16 {runId} - 1`, dari Asset Name `Laptop Pro 16 {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kursi Kerja {runId}` adalah `Kursi Kerja {runId} - 1`, dari Asset Name `Kursi Kerja {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kamera Mirrorless {runId}` adalah `Kamera Mirrorless {runId} - 1`, dari Asset Name `Kamera Mirrorless {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Printer Laser {runId}` adalah `Printer Laser {runId} - 1`, dari Asset Name `Printer Laser {runId}`.
  - Purchase Cost yang diharapkan untuk Purchase Cost `18500000` adalah `Rp 18.500.000,00`, dari Purchase Cost `18500000`.
  - Nama baris yang diharapkan untuk Asset Name `Monitor Ultrawide {runId}` adalah `Monitor Ultrawide {runId} - 1`, dari Asset Name `Monitor Ultrawide {runId}`.
  - Kursi Kerja {runId} tidak memiliki Purchase Information dan Asset Name-nya tanpa Asset Class; Kamera Mirrorless {runId} adalah aset Unmanaged.
  - Aset `Laptop Pro 16 {runId}` dan `Kursi Kerja {runId}` tercatat di group `IT {runId}`; `Monitor Ultrawide {runId}` tercatat di group `IT Support {runId}`, descendant dari `IT {runId}`; user hanya mengakses group yang sesuai cakupannya.
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
3. Verifikasi baris `Printer Laser {runId} - 1` tidak tampil di tabel
4. Verifikasi tabel dan kartu status `All` tampil
5. Verifikasi ikon `Changelog` dan tombol `Download` tampil di toolbar
6. Verifikasi Sidebar Group tampil dengan node `All Groups`
7. Verifikasi Sidebar Group memuat node `IT {runId}` dan tidak memuat node `Cabang Bandung {runId}`

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
21. Verifikasi aksi `Manage` tidak dirender (Hidden)
22. Tekan Esc

### Checkbox baris, Bar Bulk, dan aksi Bulk
23. Verifikasi checkbox baris dan Bar Bulk tidak dirender (Hidden)
24. Verifikasi aksi Bulk `Print Label`, `Add Label`, `Remove Label`, dan `Edit Purchase` tidak dapat dipilih karena Bar Bulk tidak dirender (Hidden)

### Setup Column dan sel kolom bergerbang
25. Buka Setup Column
26. Verifikasi kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` tersedia di Setup Column
27. Verifikasi kolom custom field Purchasing `Nomor PO {runId}` tidak tersedia di Setup Column
28. Verifikasi kolom custom field Accounting `Kode Anggaran {runId}` tidak tersedia di Setup Column
29. Tampilkan kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry`
30. Tutup Setup Column
31. Verifikasi sel `Asset Value (Commercial)` baris `Kursi Kerja {runId} - 1` menampilkan `Pending`
32. Verifikasi sel `Asset Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
33. Verifikasi sel `Tax Depreciation Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
34. Verifikasi sel `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
35. Verifikasi sel `Purchase Date` dan `Purchase Cost` baris `Kursi Kerja {runId} - 1` menampilkan `No access`, bukan `Pending`

### Dokumen Purchase dan data Accounting di Asset Detail
36. Klik Name `Laptop Pro 16 {runId} - 1`
37. Verifikasi halaman detail aset `Laptop Pro 16 {runId} - 1` terbuka bagi `Anita Kusuma {runId}`
38. Buka tab `Documents`
39. Verifikasi tab `Documents` terbuka bagi `Anita Kusuma {runId}`
40. Verifikasi kelompok Purchase pada tab `Documents` tidak tampil
41. Buka tab `Accounting`
42. Verifikasi tab `Accounting` terbuka bagi `Anita Kusuma {runId}`
43. Verifikasi data tab `Accounting` (peringatan fisik vs buku, Depreciation, Acquisition & Value changes, Journals) tidak tampil
44. Muat ulang halaman
45. Ketik Search `{runId}`, tekan Enter

### Cakupan group meliputi descendant
46. Ketik Search `Monitor Ultrawide {runId}`, tekan Enter
47. Verifikasi baris `Monitor Ultrawide {runId} - 1` tampil di tabel
48. Verifikasi sel `Asset Value (Commercial)` baris `Monitor Ultrawide {runId} - 1` menampilkan `Pending`
49. Verifikasi Sidebar Group memuat node `IT Support {runId}` di bawah `IT {runId}`

### Mark as Returned dan Mark as Unassigned pada aset Borrowed dan Assigned
50. Muat ulang halaman
51. Ketik Search `{runId}`, tekan Enter
52. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
53. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
54. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
55. Tekan Esc
56. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
57. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Assigned`
58. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
59. Tekan Esc
