---
id: TC-FA-MISS-E2E-047-mark-as-found-storage-penuh-dep-file-manager
title: "Mark as Found saat Storage penuh: Photo / Damaged Photo baru ditolak dengan toast Error, dialog dan isian tetap, tanpa perubahan record; tanpa Photo tidak ditolak"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§1.2#r124", "§1.2#r126", "§1.2#r127", "§1.2#r128", "§4.2.4#p4", "§6#r16", "§7.3#r14", "§7.3#p1", "§9.2#b29", "§9.4.2#r34", "§9.4.4#r15", "§10#r8", "§11#r14", "§9.4.1#r2", "§9.9#p4", "§9.6#r4"]
smoke: []
dependsOn: ["File Manager: Storage Usage", "Damaged: Damage Log"]
trace:
  "§1.2#r124": [79, 83]
  "§1.2#r126": [9, 36, 69]
  "§1.2#r127": [31, 36, 65, 69, 90]
  "§1.2#r128": [13, 14, 15, 19, 22, 25, 40, 41, 42, 46, 48, 50, 72, 76, 79]
  "§4.2.4#p4": [7, 11, 13, 34, 38, 40]
  "§6#r16": [9, 11, 12, 13, 17, 36, 38, 39, 40, 44, 69, 71, 72, 74]
  "§7.3#r14": [9, 11, 17, 36, 38, 44, 69, 71, 74]
  "§7.3#p1": [9, 36, 69]
  "§9.2#b29": [9, 36, 58, 59, 69]
  "§9.4.2#r34": [9, 11, 19, 22, 36, 46, 48, 50, 69, 76, 90]
  "§9.4.4#r15": [22, 48, 79]
  "§10#r8": [36, 69]
  "§11#r14": [9, 83]
  "§9.4.1#r2": [9, 36, 69]
  "§9.9#p4": [9, 12, 36, 39, 69]
  "§9.6#r4": [9, 90]
anchor: [2, 21, 78, 82]
coverage:
  web: automated
---

# Mark as Found saat Storage penuh: Photo / Damaged Photo baru ditolak dengan toast Error, dialog dan isian tetap, tanpa perubahan record; tanpa Photo tidak ditolak

## Prerequisites
- Aktor: Total Control `Rina Wulandari {runId}` pada Client `Klien Storage Penuh {runId}`, Aktor Missing, bukan Last Holder record di bawah.
- Layar awal: halaman Missing, sub-tab Active.
- Data:
  - DU-047-1: Client, Name `Klien Storage Penuh {runId}`, kuota Storage `50.0 GB`, usage ledger Storage `51.2 GB`; entitas khusus yang tidak dipakai spec lain.
  - DU-047-2: Missing record, Name `Camera DSLR Canon R6 {runId}`, aset tanpa TAG, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`, Condition `Normal`, dengan node `Reported missing by Rina Wulandari {runId}`.
  - DU-047-3: Missing record, Name `Laptop Dell Latitude 5420 {runId}`, aset tanpa TAG, Group `Finance Room {runId}`, Status `Missing`, Source `Borrow`, Last Holder `Dian Kusuma {runId}`, Condition sebelum laporan `Normal`, dengan satu baris transaksi Borrow yang sudah tertutup.
  - DU-047-4: Missing record, Name `Printer HP LaserJet M404 {runId}`, aset tanpa TAG, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`, Condition sebelum laporan `Damaged`, dengan satu Damage record yang ditahan (aset tampil `Damaged + Missing`).
  - DU-047-5: Photo `foto-ditemukan {runId}.png`, format PNG, ukuran di bawah 1 MB.
  - DU-047-6: Damaged Photo `foto-kerusakan-laptop {runId}.png` dan Note `Layar retak dan engsel patah saat ditemukan`, untuk DU-047-3.
  - DU-047-7: Damaged Photo `foto-kerusakan-printer {runId}.png` dan Note `Rumah printer retak sejak sebelum hilang`, untuk DU-047-4.
  - DU-047-8: pengguna `Rina Wulandari {runId}`, Role Total Control, cakupan seluruh client.
  - DU-047-9: pengguna `Dian Kusuma {runId}`, tanpa Group Role, pemegang terakhir DU-047-3.
  - Pohon Group pada entitas: `Finance Room {runId}` adalah node terbawah.
- Kondisi:
  - Usage ledger Storage `Klien Storage Penuh {runId}` bernilai `51.2 GB` dengan kuota Storage `50.0 GB`, sehingga Storage penuh.
  - Date Format bernilai `DD/MM/YY`
  - Time Format bernilai `HH:mm`

## Test Steps

### Storage penuh menolak Mark as Found Normal dengan Photo baru
1. Ketik Search `Camera DSLR Canon R6 {runId}`, tekan Enter
2. Verifikasi Status baris `Camera DSLR Canon R6 {runId}` menampilkan `Missing`
3. Klik `⋯` pada baris `Camera DSLR Canon R6 {runId}`
4. Klik `Mark as Found`
5. Pilih Asset Status `Normal`
6. Pilih berkas `foto-ditemukan {runId}.png` pada Photo
7. Verifikasi tombol `[Mark as Found]` pada dialog tidak Disabled
8. Klik `[Mark as Found]` pada dialog
9. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (51.2 GB of 50.0 GB used).` tampil
10. Waktu berlalu sampai 5 detik sejak toast tampil tanpa menutup toast
11. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (51.2 GB of 50.0 GB used).` masih tampil
12. Verifikasi field Photo tidak menampilkan pesan error inline
13. Verifikasi dialog `Mark as Found` tetap terbuka
14. Verifikasi Photo `foto-ditemukan {runId}.png` masih terpilih pada dialog
15. Verifikasi Asset Status tetap `Normal`
16. Klik `Close Button` pada toast Error
17. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (51.2 GB of 50.0 GB used).` tidak tampil lagi
18. Klik `[Cancel]` pada dialog `Mark as Found`
19. Verifikasi Status baris `Camera DSLR Canon R6 {runId}` tetap `Missing` di sub-tab Active
20. Klik nama `Camera DSLR Canon R6 {runId}` pada kolom Name
21. Verifikasi dialog Missing Log memuat node `Reported missing by Rina Wulandari {runId}`
22. Verifikasi dialog Missing Log tidak memuat node `Marked as found by`
23. Klik `✕` pada dialog Missing Log
24. Buka Asset Detail aset `Camera DSLR Canon R6 {runId}`
25. Verifikasi banner `Reported missing on [Date].` tampil sehingga status global aset tetap Missing

### Damaged Photo wajib tidak dikecualikan dari blokir Storage penuh
26. Buka tab `Missing` di halaman `Assets`
27. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
28. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
29. Klik `Mark as Found`
30. Pilih Asset Status `Damaged`
31. Verifikasi label `Damaged Photo` tampil pada isian foto
32. Pilih berkas `foto-kerusakan-laptop {runId}.png` pada Damaged Photo
33. Isi Note `Layar retak dan engsel patah saat ditemukan`
34. Verifikasi tombol `[Mark as Found]` pada dialog tidak Disabled
35. Klik `[Mark as Found]` pada dialog
36. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (51.2 GB of 50.0 GB used).` tampil
37. Waktu berlalu sampai 5 detik sejak toast tampil tanpa menutup toast
38. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (51.2 GB of 50.0 GB used).` masih tampil
39. Verifikasi field Damaged Photo tidak menampilkan pesan error inline
40. Verifikasi dialog `Mark as Found` tetap terbuka
41. Verifikasi Damaged Photo `foto-kerusakan-laptop {runId}.png` masih terpilih pada dialog
42. Verifikasi Note tetap `Layar retak dan engsel patah saat ditemukan`
43. Klik `Close Button` pada toast Error
44. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (51.2 GB of 50.0 GB used).` tidak tampil lagi
45. Klik `[Cancel]` pada dialog `Mark as Found`
46. Verifikasi Status baris `Laptop Dell Latitude 5420 {runId}` tetap `Missing` di sub-tab Active
47. Buka Damage Log milik aset `Laptop Dell Latitude 5420 {runId}`
48. Verifikasi Damage Log tidak memuat Damage Report dengan Source `Missing Asset`
49. Buka Asset Detail aset `Laptop Dell Latitude 5420 {runId}`
50. Verifikasi baris transaksi aset `Laptop Dell Latitude 5420 {runId}` tetap tertutup

### Field invalid didahulukan dari cek Storage penuh
51. Buka tab `Missing` di halaman `Assets`
52. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
53. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
54. Klik `Mark as Found`
55. Pilih Asset Status `Damaged`
56. Pilih berkas `foto-kerusakan-laptop {runId}.png` pada Damaged Photo
57. Klik `[Mark as Found]` pada dialog tanpa mengisi Note
58. Verifikasi caption `Note must not be empty` tampil pada field Note
59. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (51.2 GB of 50.0 GB used).` tidak tampil
60. Klik `[Cancel]` pada dialog `Mark as Found`

### Asal Damaged + Missing: tidak ada node baru pada Damage record yang ditahan
61. Buka tab `Missing` di halaman `Assets`
62. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
63. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
64. Klik `Mark as Found`
65. Verifikasi Asset Status terisi `Damaged` dan Disabled
66. Pilih berkas `foto-kerusakan-printer {runId}.png` pada Damaged Photo
67. Isi Note `Rumah printer retak sejak sebelum hilang`
68. Klik `[Mark as Found]` pada dialog
69. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (51.2 GB of 50.0 GB used).` tampil
70. Waktu berlalu sampai 5 detik sejak toast tampil tanpa menutup toast
71. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (51.2 GB of 50.0 GB used).` masih tampil
72. Verifikasi dialog `Mark as Found` tetap terbuka dengan Damaged Photo `foto-kerusakan-printer {runId}.png` dan Note `Rumah printer retak sejak sebelum hilang` tidak direset
73. Klik `Close Button` pada toast Error
74. Verifikasi toast Error `Error, failed to mark asset as found. Storage is full (51.2 GB of 50.0 GB used).` tidak tampil lagi
75. Klik `[Cancel]` pada dialog `Mark as Found`
76. Verifikasi Status baris `Printer HP LaserJet M404 {runId}` tetap `Missing` di sub-tab Active
77. Buka Damage Log milik aset `Printer HP LaserJet M404 {runId}`
78. Verifikasi Damage Log memuat Damage record yang ditahan
79. Verifikasi Damage Log tanpa node baru dengan foto `foto-kerusakan-printer {runId}.png`

### Submit yang ditolak tidak menulis berkas ke File Manager
80. Buka halaman `Settings > File Manager`
81. Ketik Search `{runId}`, tekan Enter
82. Verifikasi kartu `Storage Usage` tampil
83. Verifikasi tidak ada berkas dengan Source `Found Photo` atau `Damaged Photo` untuk aset `Camera DSLR Canon R6 {runId}`, `Laptop Dell Latitude 5420 {runId}`, dan `Printer HP LaserJet M404 {runId}`

### Mark as Found Normal tanpa Photo tidak dicek saat Storage penuh
84. Buka tab `Missing` di halaman `Assets`
85. Ketik Search `Camera DSLR Canon R6 {runId}`, tekan Enter
86. Klik `⋯` pada baris `Camera DSLR Canon R6 {runId}`
87. Klik `Mark as Found`
88. Pilih Asset Status `Normal`
89. Klik `[Mark as Found]` pada dialog tanpa memilih Photo
90. Verifikasi toast `Success, [Asset Name] is available again.` tampil dengan Asset Name record `Camera DSLR Canon R6 {runId}`
