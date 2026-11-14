---
id: TC-FA-MISS-E2E-020-gating-total-control
title: "Gating Total Control: seluruh sel matriks Show, kolom finansial, dan aksi allow representatif"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§4.8#r1", "§4.8#r2", "§4.8#r5", "§4.8#r6", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§9.11#r1", "§9.11#r2", "§9.11#b1", "§2.1#b7", "§4.8#b2", "§2#b1", "§2.1#b4", "§9.3#b1"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [3, 8, 12]
  "§2.1#r2": 46
  "§2.1#r5": [15, 54]
  "§2.1#r6": [25, 26]
  "§2.1#r7": 16
  "§2.1#r9": 17
  "§2.1#r10": 20
  "§2.1#r11": 30
  "§2.1#r12": [5, 6]
  "§4.8#r1": [1, 3]
  "§4.8#r2": 46
  "§4.8#r5": 15
  "§4.8#r6": [16, 23]
  "§4.8#r8": [17, 20]
  "§4.8#r9": [36, 37, 38]
  "§4.8#r10": 28
  "§4.8#r11": 30
  "§9.11#r1": 8
  "§9.11#r2": 37
  "§9.11#b1": 41
  "§2.1#b7": [36, 37, 38]
  "§4.8#b2": 30
  "§2#b1": 16
  "§2.1#b4": 1
  "§9.3#b1": [54, 56]
anchor: []
coverage:
  web: automated
---

# Gating Total Control: seluruh sel matriks Show, kolom finansial, dan aksi allow representatif

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Assets.
- Data:
  - DU-020-1: Missing record, Name `Laptop Dell Latitude 5420 {runId} - 22`, Asset ID `LPT-0022 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-020-2: Missing record, Name `Hand Pallet Truck {runId} - 3`, Asset ID `HPT-0003 {runId}`, Group `Warehouse {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-020-3: Missing record, Name `Monitor LG 27UL500 {runId} - 11`, Asset ID `MON-0011 {runId}`, Group `Head Office {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari Dewi {runId}` (pemegang aset tanpa hak Aktor Missing).
  - DU-020-4: Missing record, Name `Projector Epson EB-X06 {runId} - 7`, Asset ID `PRJ-0007 {runId}`, Group `Branch Surabaya {runId}`, Status `Reported Disposal`, Source `Stock opname`, Last Holder `—`.
  - DU-020-5: Missing record, Name `Camera Canon EOS {runId} - 1`, Asset ID `CAM-0001 {runId}`, Group `Head Office {runId}`, Status `Found`, Source `Borrow`, Last Holder `—`.
  - DU-020-6: Asset, Name `Scanner Zebra DS2208 {runId} - 2`, Asset ID `SCN-0002 {runId}`, Group `Warehouse {runId}`, Status `Available`, tanpa record Missing berjalan.

## Test Steps

### Tab Missing dan sub-tab tampil untuk Total Control
1. Verifikasi tab `Missing` tampil pada halaman Assets
2. Klik tab `Missing`
3. Verifikasi sub-tab `Active` dan `History` tampil
4. Ketik Search `{runId}`, tekan Enter

### Cakupan seluruh client dan Missing Log lintas Group
5. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 22` dengan Group `Finance Room {runId}` tampil
6. Verifikasi baris `Hand Pallet Truck {runId} - 3` dengan Group `Warehouse {runId}` tampil
7. Klik nama `Hand Pallet Truck {runId} - 3`
8. Verifikasi dialog `Missing Log` untuk record `Hand Pallet Truck {runId} - 3` terbuka
9. Klik `✕` pada dialog Missing Log
10. Klik sub-tab `History`
11. Ketik Search `{runId}`, tekan Enter
12. Verifikasi baris `Camera Canon EOS {runId} - 1` dengan Status `Found` tampil
13. Klik sub-tab `Active`

### Aksi baris dan Review tampil untuk Total Control
14. Klik menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId} - 22`
15. Verifikasi aksi `Add Update` tampil
16. Verifikasi aksi `Mark as Found` tampil
17. Verifikasi aksi `Report Disposal` tampil
18. Tekan `Esc`
19. Klik menu ⋯ pada baris `Projector Epson EB-X06 {runId} - 7`
20. Verifikasi aksi `Cancel Disposal Report` tampil
21. Tekan `Esc`
22. Klik menu ⋯ pada baris `Monitor LG 27UL500 {runId} - 11`
23. Verifikasi aksi `Review` tampil
24. Klik `Review`
25. Verifikasi tombol `[Reject]` pada footer dialog Missing Log tampil
26. Verifikasi tombol `[Confirm]` pada footer dialog Missing Log tampil
27. Klik `✕` pada dialog Missing Log

### Toolbar tab Active: Scan Found Asset dan Download
28. Verifikasi tombol `Scan Found Asset` tampil di toolbar tab Active
29. Klik `Download`
30. Verifikasi opsi `Download as CSV` dan `Download as XLSX` tampil
31. Tekan `Esc`

### Kolom nilai finansial tersedia
32. Klik tombol `Column Visibility` pada header tabel
33. Centang `Purchase Cost`
34. Centang `Asset Value (Commercial)`
35. Centang `Asset Value (Fiscal)`
36. Verifikasi header kolom `Purchase Cost` tampil di tabel
37. Verifikasi header kolom `Asset Value (Commercial)` tampil di tabel
38. Verifikasi header kolom `Asset Value (Fiscal)` tampil di tabel
39. Tekan `Esc`
40. Klik `Filter`
41. Verifikasi Filter Panel memuat field `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
42. Klik `Filter`

### Report Missing tersedia dari daftar aset
43. Klik tab `Assets`
44. Ketik Search `{runId}`, tekan Enter
45. Klik menu ⋯ pada baris `Scanner Zebra DS2208 {runId} - 2`
46. Verifikasi aksi `Report Missing` tampil
47. Tekan `Esc`
48. Klik tab `Missing`
49. Ketik Search `{runId}`, tekan Enter

### Add Update oleh Total Control tersimpan
50. Klik menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId} - 22`
51. Klik `Add Update`
52. Isi Update `Terakhir terlihat di lobi kantor pusat {runId}`
53. Klik `[Add Update]`
54. Verifikasi toast `Success, update has been added.` tampil
55. Klik nama `Laptop Dell Latitude 5420 {runId} - 22`
56. Verifikasi node `Update added by` dengan Update `Terakhir terlihat di lobi kantor pusat {runId}` tampil di dialog Missing Log
