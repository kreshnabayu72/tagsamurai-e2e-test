---
id: TC-FA-MISS-E2E-023-gating-accounting
title: "Gating Accounting: read-only tab dan Missing Log, kolom finansial Show, Report Disposal tersedia, aksi lain Hidden"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§4.8#r1", "§4.8#r2", "§4.8#r5", "§4.8#r6", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§9.11#r1", "§9.11#r2", "§9.11#b1", "§2.1#b8", "§4.8#b2", "§2#b4", "§2.1#b6"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [3, 8, 12]
  "§2.1#r2": [56, 72]
  "§2.1#r5": 17
  "§2.1#r6": [22, 26]
  "§2.1#r7": 18
  "§2.1#r9": 16
  "§2.1#r10": [29, 33]
  "§2.1#r11": 38
  "§2.1#r12": [5, 6]
  "§4.8#r1": [1, 3]
  "§4.8#r2": [56, 72]
  "§4.8#r5": 17
  "§4.8#r6": [18, 22, 26]
  "§4.8#r9": [16, 29, 33, 34]
  "§4.8#r10": [45, 46, 47]
  "§4.8#r11": 40
  "§4.8#r12": 38
  "§9.11#r1": 8
  "§9.11#r2": [46, 64, 65, 66]
  "§9.11#b1": 50
  "§2.1#b8": [45, 46, 47]
  "§4.8#b2": 38
  "§2#b4": [16, 45]
  "§2.1#b6": [16, 34]
anchor: [15, 21, 25, 32, 36, 54, 71]
coverage:
  web: automated
---

# Gating Accounting: read-only tab dan Missing Log, kolom finansial Show, Report Disposal tersedia, aksi lain Hidden

## Prerequisites
- Aktor: Accounting, yaitu pemegang Global Role `Manage accounting` (Read + Update), cakupan seluruh client.
- Layar awal: halaman Assets.
- Data:
  - DU-023-1: Missing record, Name `Laptop Dell Latitude 5420 {runId} - 22`, Asset ID `LPT-0022 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-023-2: Missing record, Name `Hand Pallet Truck {runId} - 3`, Asset ID `HPT-0003 {runId}`, Group `Warehouse {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-023-3: Missing record, Name `Monitor LG 27UL500 {runId} - 11`, Asset ID `MON-0011 {runId}`, Group `Head Office {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari Dewi {runId}` (pemegang aset tanpa hak Aktor Missing).
  - DU-023-4: Missing record, Name `Projector Epson EB-X06 {runId} - 7`, Asset ID `PRJ-0007 {runId}`, Group `Branch Surabaya {runId}`, Status `Reported Disposal`, Source `Audit`, Last Holder `—`, dilaporkan oleh aktor ini.
  - DU-023-5: Missing record, Name `Printer HP LaserJet M404 {runId} - 5`, Asset ID `PRN-0005 {runId}`, Group `Head Office {runId}`, Status `Reported Disposal`, Source `Manual`, Last Holder `—`, dilaporkan oleh pengguna lain.
  - DU-023-6: Missing record, Name `Camera Canon EOS {runId} - 1`, Asset ID `CAM-0001 {runId}`, Group `Head Office {runId}`, Status `Found`, Source `Borrow`, Last Holder `—`.
  - DU-023-7: Asset, Name `Scanner Zebra DS2208 {runId} - 2`, Asset ID `SCN-0002 {runId}`, Group `Warehouse {runId}`, Status `Available`, tanpa record Missing berjalan.

## Test Steps

### Tab Missing dan sub-tab tampil untuk Accounting
1. Verifikasi tab `Missing` tampil pada halaman Assets
2. Klik tab `Missing`
3. Verifikasi sub-tab `Active` dan `History` tampil
4. Ketik Search `{runId}`, tekan Enter

### Cakupan seluruh client dan Missing Log read-only
5. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 22` dengan Group `Finance Room {runId}` tampil
6. Verifikasi baris `Hand Pallet Truck {runId} - 3` dengan Group `Warehouse {runId}` tampil
7. Klik nama `Hand Pallet Truck {runId} - 3`
8. Verifikasi dialog `Missing Log` untuk record `Hand Pallet Truck {runId} - 3` terbuka
9. Klik `✕` pada dialog Missing Log
10. Klik sub-tab `History`
11. Ketik Search `{runId}`, tekan Enter
12. Verifikasi baris `Camera Canon EOS {runId} - 1` dengan Status `Found` tampil
13. Klik sub-tab `Active`

### Record Missing: Report Disposal tersedia, aksi tulis lain tidak tampil
14. Klik menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId} - 22`
15. Verifikasi aksi `Missing Log` tampil
16. Verifikasi aksi `Report Disposal` tampil
17. Verifikasi aksi `Add Update` tidak tampil
18. Verifikasi aksi `Mark as Found` tidak tampil
19. Tekan `Esc`

### Laporan pemegang: Review dan footer Confirm atau Reject tidak tampil
20. Klik menu ⋯ pada baris `Monitor LG 27UL500 {runId} - 11`
21. Verifikasi aksi `Missing Log` tampil
22. Verifikasi aksi `Review` tidak tampil
23. Tekan `Esc`
24. Klik nama `Monitor LG 27UL500 {runId} - 11`
25. Verifikasi dialog `Missing Log` untuk record `Monitor LG 27UL500 {runId} - 11` terbuka
26. Verifikasi tombol `[Reject]` dan `[Confirm]` tidak tampil pada footer dialog Missing Log
27. Klik `✕` pada dialog Missing Log

### Cancel Disposal Report hanya untuk laporan miliknya
28. Klik menu ⋯ pada baris `Projector Epson EB-X06 {runId} - 7`
29. Verifikasi aksi `Cancel Disposal Report` tampil
30. Tekan `Esc`
31. Klik menu ⋯ pada baris `Printer HP LaserJet M404 {runId} - 5`
32. Verifikasi aksi `Missing Log` tampil
33. Verifikasi aksi `Cancel Disposal Report` tidak tampil
34. Verifikasi aksi `Report Disposal` tidak tampil
35. Tekan `Esc`

### Toolbar tab Active: Download tampil, Scan Found Asset tidak tampil
36. Verifikasi tombol `Download` tampil di toolbar tab Active
37. Klik `Download`
38. Verifikasi opsi `Download as CSV` dan `Download as XLSX` tampil
39. Tekan `Esc`
40. Verifikasi tombol `Scan Found Asset` tidak tampil di toolbar tab Active

### Kolom nilai finansial tersedia
41. Klik tombol `Column Visibility` pada header tabel
42. Centang `Purchase Cost`
43. Centang `Asset Value (Commercial)`
44. Centang `Asset Value (Fiscal)`
45. Verifikasi header kolom `Purchase Cost` tampil di tabel
46. Verifikasi header kolom `Asset Value (Commercial)` tampil di tabel
47. Verifikasi header kolom `Asset Value (Fiscal)` tampil di tabel
48. Tekan `Esc`
49. Klik `Filter`
50. Verifikasi Filter Panel memuat field `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
51. Klik `Filter`

### Report Missing tidak tampil dari daftar aset
52. Klik tab `Assets`
53. Ketik Search `{runId}`, tekan Enter
54. Verifikasi baris `Scanner Zebra DS2208 {runId} - 2` tampil
55. Klik menu ⋯ pada baris `Scanner Zebra DS2208 {runId} - 2`
56. Verifikasi aksi `Report Missing` tidak tampil
57. Tekan `Esc`
58. Klik tab `Missing`

### Kolom nilai finansial tab History tersedia untuk Accounting
59. Klik sub-tab `History`
60. Klik tombol `Column Visibility` pada header tabel
61. Centang `Purchase Cost`
62. Centang `Asset Value (Commercial)`
63. Centang `Asset Value (Fiscal)`
64. Verifikasi header kolom `Purchase Cost` tampil di tabel
65. Verifikasi header kolom `Asset Value (Commercial)` tampil di tabel
66. Verifikasi header kolom `Asset Value (Fiscal)` tampil di tabel
67. Tekan `Esc`

### Report Missing tidak tampil pada Asset Detail
68. Klik tab `Assets`
69. Ketik Search `{runId}`, tekan Enter
70. Klik `Scanner Zebra DS2208 {runId} - 2` pada kolom Name
71. Verifikasi Asset Status pada Asset Detail `Available`
72. Verifikasi tombol `[Report Missing]` tidak tampil pada Asset Detail
