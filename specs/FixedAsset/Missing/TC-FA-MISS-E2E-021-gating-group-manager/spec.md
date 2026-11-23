---
id: TC-FA-MISS-E2E-021-gating-group-manager
title: "Gating Group Manager: cakupan Group binaan dan sub-group, aksi tulis, kolom finansial sesuai hak"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§4.8#r1", "§4.8#r2", "§4.8#r5", "§4.8#r6", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§9.11#r1", "§9.11#r2", "§9.11#b1", "§2.1#b8", "§4.8#b2", "§2#b1"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [3, 10, 14]
  "§2.1#r2": 45
  "§2.1#r5": [17, 53]
  "§2.1#r6": [27, 28]
  "§2.1#r7": 18
  "§2.1#r9": 19
  "§2.1#r10": 22
  "§2.1#r11": 32
  "§2.1#r12": [5, 6, 7, 8]
  "§4.8#r1": [1, 3]
  "§4.8#r2": 45
  "§4.8#r5": 17
  "§4.8#r6": [18, 25]
  "§4.8#r9": [19, 22]
  "§4.8#r10": [36, 40, 60, 61, 62, 65]
  "§4.8#r11": 30
  "§4.8#r12": 32
  "§9.11#r1": [8, 10]
  "§9.11#r2": [36, 72, 73, 74, 81]
  "§9.11#b1": [36, 40]
  "§2.1#b8": [36, 40, 60, 61, 62, 65]
  "§4.8#b2": 32
  "§2#b1": 18
anchor: [35, 39, 80]
coverage:
  web: automated
---

# Gating Group Manager: cakupan Group binaan dan sub-group, aksi tulis, kolom finansial sesuai hak

## Prerequisites
- Aktor: Group Manager dengan Group binaan `Head Office {runId}`, yang punya sub-group `Finance Room {runId}` dan `Server Room {runId}`; tanpa hak `View asset value`; lalu Group Manager dengan Group binaan yang sama yang juga memegang `View asset value` pada Group `Head Office {runId}` beserta descendant.
- Layar awal: halaman Assets.
- Data:
  - DU-021-1: Missing record, Name `Laptop Lenovo ThinkPad T14 {runId} - 4`, Asset ID `LPT-0004 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-021-2: Missing record, Name `Hand Pallet Truck {runId} - 3`, Asset ID `HPT-0003 {runId}`, Group `Warehouse {runId}` (di luar Group binaan), Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-021-3: Missing record, Name `Monitor LG 27UL500 {runId} - 11`, Asset ID `MON-0011 {runId}`, Group `Server Room {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari Dewi {runId}` (pemegang aset tanpa hak Aktor Missing).
  - DU-021-4: Missing record, Name `Projector Epson EB-X06 {runId} - 7`, Asset ID `PRJ-0007 {runId}`, Group `Head Office {runId}`, Status `Reported Disposal`, Source `Audit`, Last Holder `—`.
  - DU-021-5: Missing record, Name `Camera Canon EOS {runId} - 1`, Asset ID `CAM-0001 {runId}`, Group `Finance Room {runId}`, Status `Found`, Source `Borrow`, Last Holder `—`.
  - DU-021-6: Asset, Name `Scanner Zebra DS2208 {runId} - 2`, Asset ID `SCN-0002 {runId}`, Group `Finance Room {runId}`, Status `Available`, tanpa record Missing berjalan.

## Test Steps

### Tab Missing dan sub-tab tampil untuk Group Manager
1. Verifikasi tab `Missing` tampil pada halaman Assets
2. Klik tab `Missing`
3. Verifikasi sub-tab `Active` dan `History` tampil
4. Ketik Search `{runId}`, tekan Enter

### Cakupan Group binaan dan sub-group
5. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 4` dengan Group `Finance Room {runId}` tampil
6. Verifikasi baris `Monitor LG 27UL500 {runId} - 11` dengan Group `Server Room {runId}` tampil
7. Verifikasi baris `Projector Epson EB-X06 {runId} - 7` dengan Group `Head Office {runId}` tampil
8. Verifikasi baris `Hand Pallet Truck {runId} - 3` dengan Group `Warehouse {runId}` tidak tampil
9. Klik nama `Laptop Lenovo ThinkPad T14 {runId} - 4`
10. Verifikasi dialog `Missing Log` untuk record `Laptop Lenovo ThinkPad T14 {runId} - 4` terbuka
11. Klik `✕` pada dialog Missing Log
12. Klik sub-tab `History`
13. Ketik Search `{runId}`, tekan Enter
14. Verifikasi baris `Camera Canon EOS {runId} - 1` dengan Status `Found` tampil
15. Klik sub-tab `Active`

### Aksi baris dan Review tampil untuk Group Manager
16. Klik menu ⋯ pada baris `Laptop Lenovo ThinkPad T14 {runId} - 4`
17. Verifikasi aksi `Add Update` tampil
18. Verifikasi aksi `Mark as Found` tampil
19. Verifikasi aksi `Report Disposal` tampil
20. Tekan `Esc`
21. Klik menu ⋯ pada baris `Projector Epson EB-X06 {runId} - 7`
22. Verifikasi aksi `Cancel Disposal Report` tampil
23. Tekan `Esc`
24. Klik menu ⋯ pada baris `Monitor LG 27UL500 {runId} - 11`
25. Verifikasi aksi `Review` tampil
26. Klik `Review`
27. Verifikasi tombol `[Reject]` pada footer dialog Missing Log tampil
28. Verifikasi tombol `[Confirm]` pada footer dialog Missing Log tampil
29. Klik `✕` pada dialog Missing Log

### Toolbar tab Active: Scan Found Asset dan Download
30. Verifikasi tombol `Scan Found Asset` tampil di toolbar tab Active
31. Klik `Download`
32. Verifikasi opsi `Download as CSV` dan `Download as XLSX` tampil
33. Tekan `Esc`

### Kolom nilai finansial tidak tersedia tanpa hak View asset value
34. Klik tombol `Column Visibility` pada header tabel
35. Verifikasi kolom `Brand` tersedia pada daftar Column Visibility
36. Verifikasi daftar Column Visibility tidak memuat `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
37. Tekan `Esc`
38. Klik `Filter`
39. Verifikasi field `Brand` tampil di Filter Panel
40. Verifikasi Filter Panel tidak memuat field `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
41. Klik `Filter`

### Report Missing tersedia dari daftar aset
42. Klik tab `Assets`
43. Ketik Search `{runId}`, tekan Enter
44. Klik menu ⋯ pada baris `Scanner Zebra DS2208 {runId} - 2`
45. Verifikasi aksi `Report Missing` tampil
46. Tekan `Esc`
47. Klik tab `Missing`
48. Ketik Search `{runId}`, tekan Enter

### Add Update oleh Group Manager tersimpan
49. Klik menu ⋯ pada baris `Laptop Lenovo ThinkPad T14 {runId} - 4`
50. Klik `Add Update`
51. Isi Update `Dicari di ruang keuangan lantai tiga {runId}`
52. Klik `[Add Update]`
53. Verifikasi toast `Success, update has been added.` tampil

### Group Manager yang juga memegang View asset value: kolom nilai finansial tersedia
54. Masuk sebagai Group Manager yang juga memegang `View asset value` pada Group `Head Office {runId}`
55. Klik tab `Missing`
56. Klik tombol `Column Visibility` pada header tabel
57. Centang `Purchase Cost`
58. Centang `Asset Value (Commercial)`
59. Centang `Asset Value (Fiscal)`
60. Verifikasi header kolom `Purchase Cost` tampil di tabel
61. Verifikasi header kolom `Asset Value (Commercial)` tampil di tabel
62. Verifikasi header kolom `Asset Value (Fiscal)` tampil di tabel
63. Tekan `Esc`
64. Klik `Filter`
65. Verifikasi Filter Panel memuat field `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
66. Klik `Filter`

### Group Manager yang juga memegang View asset value: kolom nilai finansial tab History tersedia
67. Klik sub-tab `History`
68. Klik tombol `Column Visibility` pada header tabel
69. Centang `Purchase Cost`
70. Centang `Asset Value (Commercial)`
71. Centang `Asset Value (Fiscal)`
72. Verifikasi header kolom `Purchase Cost` tampil di tabel
73. Verifikasi header kolom `Asset Value (Commercial)` tampil di tabel
74. Verifikasi header kolom `Asset Value (Fiscal)` tampil di tabel
75. Tekan `Esc`

### Group Manager tanpa View asset value: kolom nilai finansial tab History tidak tersedia
76. Masuk sebagai Group Manager dengan Group binaan `Head Office {runId}` tanpa hak `View asset value`
77. Klik tab `Missing`
78. Klik sub-tab `History`
79. Klik tombol `Column Visibility` pada header tabel
80. Verifikasi kolom `Brand` tersedia pada daftar Column Visibility
81. Verifikasi daftar Column Visibility tidak memuat `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
82. Tekan `Esc`
