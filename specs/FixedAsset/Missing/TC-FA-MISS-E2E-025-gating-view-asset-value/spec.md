---
id: TC-FA-MISS-E2E-025-gating-view-asset-value
title: "Gating View asset value: tab, Missing Log, kolom nilai finansial pada Group di-assign, tanpa aksi tulis"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§4.8#r1", "§4.8#r2", "§4.8#r5", "§4.8#r6", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§9.11#r1", "§9.11#r2", "§9.11#b1", "§2.1#b7", "§4.8#b2", "§2.1#b6"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [3, 9, 13]
  "§2.1#r2": 49
  "§2.1#r5": 17
  "§2.1#r6": 23
  "§2.1#r7": 18
  "§2.1#r9": 19
  "§2.1#r10": 27
  "§2.1#r11": 31
  "§2.1#r12": [5, 6, 7]
  "§4.8#r1": [1, 3]
  "§4.8#r2": 49
  "§4.8#r5": 17
  "§4.8#r6": [18, 23, 55]
  "§4.8#r8": [19, 27]
  "§4.8#r9": [38, 39, 40]
  "§4.8#r10": 33
  "§4.8#r11": 31
  "§9.11#r1": [7, 9]
  "§9.11#r2": [39, 62, 63, 64]
  "§9.11#b1": 43
  "§2.1#b7": [38, 39, 40]
  "§4.8#b2": [3, 9, 31]
  "§2.1#b6": [3, 9, 17, 19, 38, 39, 40]
anchor: [16, 22, 26, 29, 47, 54]
coverage:
  web: automated
---

# Gating View asset value: tab, Missing Log, kolom nilai finansial pada Group di-assign, tanpa aksi tulis

## Prerequisites
- Aktor: pemegang `View asset value` (Group Role, tanpa hak tulis) pada Group `Head Office {runId}` beserta descendant `Finance Room {runId}`.
- Layar awal: halaman Assets.
- Data:
  - DU-025-1: Missing record, Name `Laptop Dell Latitude 5420 {runId} - 22`, Asset ID `LPT-0022 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-025-2: Missing record, Name `Hand Pallet Truck {runId} - 3`, Asset ID `HPT-0003 {runId}`, Group `Warehouse {runId}` (di luar Group di-assign), Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-025-3: Missing record, Name `Monitor LG 27UL500 {runId} - 11`, Asset ID `MON-0011 {runId}`, Group `Head Office {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari Dewi {runId}` (pemegang aset tanpa hak Aktor Missing).
  - DU-025-4: Missing record, Name `Projector Epson EB-X06 {runId} - 7`, Asset ID `PRJ-0007 {runId}`, Group `Head Office {runId}`, Status `Reported Disposal`, Source `Stock opname`, Last Holder `—`.
  - DU-025-5: Missing record, Name `Camera Canon EOS {runId} - 1`, Asset ID `CAM-0001 {runId}`, Group `Finance Room {runId}`, Status `Found`, Source `Borrow`, Last Holder `—`.
  - DU-025-6: Asset, Name `Scanner Zebra DS2208 {runId} - 2`, Asset ID `SCN-0002 {runId}`, Group `Finance Room {runId}`, Status `Available`, tanpa record Missing berjalan.

## Test Steps

### Tab Missing dan sub-tab tampil untuk pemegang View asset value
1. Verifikasi tab `Missing` tampil pada halaman Assets
2. Klik tab `Missing`
3. Verifikasi sub-tab `Active` dan `History` tampil
4. Ketik Search `{runId}`, tekan Enter

### Cakupan Group di-assign dan Missing Log
5. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 22` dengan Group `Finance Room {runId}` tampil
6. Verifikasi baris `Monitor LG 27UL500 {runId} - 11` dengan Group `Head Office {runId}` tampil
7. Verifikasi baris `Hand Pallet Truck {runId} - 3` dengan Group `Warehouse {runId}` tidak tampil
8. Klik nama `Laptop Dell Latitude 5420 {runId} - 22`
9. Verifikasi dialog `Missing Log` untuk record `Laptop Dell Latitude 5420 {runId} - 22` terbuka
10. Klik `✕` pada dialog Missing Log
11. Klik sub-tab `History`
12. Ketik Search `{runId}`, tekan Enter
13. Verifikasi baris `Camera Canon EOS {runId} - 1` dengan Status `Found` tampil
14. Klik sub-tab `Active`

### Record Missing: semua aksi tulis tidak tampil
15. Klik menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId} - 22`
16. Verifikasi aksi `Missing Log` tampil
17. Verifikasi aksi `Add Update` tidak tampil
18. Verifikasi aksi `Mark as Found` tidak tampil
19. Verifikasi aksi `Report Disposal` tidak tampil
20. Tekan `Esc`

### Laporan pemegang dan Reported Disposal: Review dan Cancel Disposal Report tidak tampil
21. Klik menu ⋯ pada baris `Monitor LG 27UL500 {runId} - 11`
22. Verifikasi aksi `Missing Log` tampil
23. Verifikasi aksi `Review` tidak tampil
24. Tekan `Esc`
25. Klik menu ⋯ pada baris `Projector Epson EB-X06 {runId} - 7`
26. Verifikasi aksi `Missing Log` tampil
27. Verifikasi aksi `Cancel Disposal Report` tidak tampil
28. Tekan `Esc`

### Toolbar tab Active: Download tampil, Scan Found Asset tidak tampil
29. Verifikasi tombol `Download` tampil di toolbar tab Active
30. Klik `Download`
31. Verifikasi opsi `Download as CSV` dan `Download as XLSX` tampil
32. Tekan `Esc`
33. Verifikasi tombol `Scan Found Asset` tidak tampil di toolbar tab Active

### Kolom nilai finansial tersedia pada Group di-assign
34. Klik tombol `Column Visibility` pada header tabel
35. Centang `Purchase Cost`
36. Centang `Asset Value (Commercial)`
37. Centang `Asset Value (Fiscal)`
38. Verifikasi header kolom `Purchase Cost` tampil di tabel
39. Verifikasi header kolom `Asset Value (Commercial)` tampil di tabel
40. Verifikasi header kolom `Asset Value (Fiscal)` tampil di tabel
41. Tekan `Esc`
42. Klik `Filter`
43. Verifikasi Filter Panel memuat field `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
44. Klik `Filter`

### Report Missing tidak tampil dari daftar aset
45. Klik tab `Assets`
46. Ketik Search `{runId}`, tekan Enter
47. Verifikasi baris `Scanner Zebra DS2208 {runId} - 2` tampil
48. Klik menu ⋯ pada baris `Scanner Zebra DS2208 {runId} - 2`
49. Verifikasi aksi `Report Missing` tidak tampil
50. Tekan `Esc`
51. Klik tab `Missing`

### View asset value: footer Reject dan Confirm tidak tampil pada laporan pemegang
52. Ketik Search `{runId}`, tekan Enter
53. Klik nama `Monitor LG 27UL500 {runId} - 11`
54. Verifikasi dialog `Missing Log` untuk record `Monitor LG 27UL500 {runId} - 11` terbuka
55. Verifikasi tombol `[Reject]` dan `[Confirm]` tidak tampil pada footer dialog Missing Log
56. Klik `✕` pada dialog Missing Log

### View asset value: kolom nilai finansial tab History tersedia
57. Klik sub-tab `History`
58. Klik tombol `Column Visibility` pada header tabel
59. Centang `Purchase Cost`
60. Centang `Asset Value (Commercial)`
61. Centang `Asset Value (Fiscal)`
62. Verifikasi header kolom `Purchase Cost` tampil di tabel
63. Verifikasi header kolom `Asset Value (Commercial)` tampil di tabel
64. Verifikasi header kolom `Asset Value (Fiscal)` tampil di tabel
65. Tekan `Esc`
