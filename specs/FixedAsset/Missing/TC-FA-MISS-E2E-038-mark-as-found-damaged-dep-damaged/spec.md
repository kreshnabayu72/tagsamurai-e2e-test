---
id: TC-FA-MISS-E2E-038-mark-as-found-damaged-dep-damaged
title: "Mark as Found dengan Asset Status Damaged dan asal Damaged + Missing: Damage Report, Damage record ditahan, toast varian"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r27", "§1.2#r28", "§1.2#r49", "§1.2#r50", "§1.2#r63", "§1.2#r64", "§1.2#r80", "§1.2#r84", "§1.2#r85", "§1.2#r86", "§1.2#r87", "§1.2#r88", "§9.4.2#r10", "§9.4.2#r33", "§9.4.2#r7", "§4.2.4#r5", "§4.2.4#r7", "§4.2.4#r8", "§9.9#r4", "§9.9#r5", "§9.9#r6", "§7.3#r8", "§9.7#r4", "§4.1b#p5", "§8.1#r14", "§11#r12", "§9.4.4#r11"]
smoke: []
dependsOn: ["Damaged: Damage Report", "Damaged: Damage Log"]
trace:
  "§1.2#r27": [28]
  "§1.2#r28": [28, 55]
  "§1.2#r49": [28]
  "§1.2#r50": [44]
  "§1.2#r63": [66]
  "§1.2#r64": [65]
  "§1.2#r80": [34]
  "§1.2#r84": [15, 44]
  "§1.2#r85": [16]
  "§1.2#r86": [37, 38]
  "§1.2#r87": [45]
  "§1.2#r88": [51]
  "§9.4.2#r10": [8, 9, 15, 16, 17]
  "§9.4.2#r33": [34, 42, 44]
  "§9.4.2#r7": [65, 66]
  "§4.2.4#r5": [34]
  "§4.2.4#r7": [5, 35]
  "§4.2.4#r8": [6]
  "§9.9#r4": [34]
  "§9.9#r5": [9, 38]
  "§9.9#r6": [8, 37]
  "§7.3#r8": [13, 42]
  "§9.7#r4": [15, 44]
  "§4.1b#p5": [23]
  "§8.1#r14": [23, 51]
  "§11#r12": [15]
  "§9.4.4#r11": [23]
anchor: []
coverage:
  web: automated
---

# Mark as Found dengan Asset Status Damaged dan asal Damaged + Missing: Damage Report, Damage record ditahan, toast varian

## Prerequisites
- Aktor: Total Control `Rina W`, yang juga Aktor Missing.
- Layar awal: Assets > Missing > Active.
- Data:
  - DU-038-1: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Finance Room`, tanpa TAG, dengan Condition sebelum laporan `Normal` dan record Missing berstatus `Missing`.
  - DU-038-2: Asset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, tanpa TAG, dengan Condition sebelum laporan `Damaged`, record Missing berstatus `Missing`, dan satu Damage record yang ditahan.
  - DU-038-3: Asset `Monitor LG 27UL500 {runId}`, Group `Head Office`, dengan Condition sebelum laporan `Damaged`, satu Damage record yang ditahan, dan record Missing berstatus `Waiting for Confirmation` yang dilaporkan pemegang `Joko Santoso {runId}`.
  - DU-038-4: Pengguna `Joko Santoso {runId}`, pemegang tanpa hak Aktor Missing.
  - DU-038-5: Damaged Photo `foto-kerusakan-laptop.png`, Note `Layar retak dan engsel patah saat ditemukan`.
  - DU-038-6: Damaged Photo `foto-kerusakan-printer.png`, Note `Rumah printer retak sejak sebelum hilang`.
  - DU-038-7: Reason `Monitor masih dipakai dalam kondisi rusak`.
  - DU-038-8: Pengguna `Rina W`, Total Control.
- Kondisi:
  - Akun `Rina W` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Mark as Found dengan Asset Status Damaged membuat Damage Report
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
3. Klik `Mark as Found`
4. Pilih Asset Status `Damaged`
5. Verifikasi label `Damaged Photo` tampil pada isian foto
6. Verifikasi placeholder `Enter damage description` tampil pada Note
7. Klik `[Mark as Found]` pada dialog tanpa mengisi Damaged Photo dan Note
8. Verifikasi caption `Damaged photo must not be empty` tampil di bawah Damaged Photo
9. Verifikasi caption `Note must not be empty` tampil di bawah Note
10. Pilih berkas `foto-kerusakan-laptop.png` pada Damaged Photo
11. Isi Note `Layar retak dan engsel patah saat ditemukan`
12. Klik `[Mark as Found]` pada dialog
13. Verifikasi toast `Success, [Asset Name] is available again. A damage report has been created.` tampil dengan nama aset `Laptop Dell Latitude 5420 {runId}`
14. Buka Damage Log milik aset `Laptop Dell Latitude 5420 {runId}`
15. Verifikasi Damage Report baru dengan Source `Missing Asset` tampil di Damage Log
16. Verifikasi Damage Report itu memuat foto `foto-kerusakan-laptop.png` dan Note `Layar retak dan engsel patah saat ditemukan`
17. Verifikasi Damage Report itu memuat tautan ke Missing Log record
18. Buka halaman `Assets`
19. Klik tab `Missing`
20. Klik sub-tab `History`
21. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
22. Klik `Laptop Dell Latitude 5420 {runId}` pada kolom Name
23. Verifikasi dialog Missing Log memuat node `Marked as found by` oleh `Rina W` dengan Found at Group aset, Asset Status `Damaged`, Note `Layar retak dan engsel patah saat ditemukan`, Damaged Photo `foto-kerusakan-laptop.png`, dan tautan ke Damage Log
24. Tutup dialog Missing Log dengan `✕`

### Mark as Found atas aset asal Damaged + Missing memakai Damage record yang ditahan
25. Klik sub-tab `Active`
26. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
27. Buka Damage Log milik aset `Printer HP LaserJet M404 {runId}`
28. Verifikasi Damage record milik `Printer HP LaserJet M404 {runId}` ditahan selama record Missing berjalan dan aset tampil `Damaged + Missing`
29. Buka halaman `Assets`
30. Klik tab `Missing`
31. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
32. Buka menu `⋯` pada baris `Printer HP LaserJet M404 {runId}`
33. Klik `Mark as Found`
34. Verifikasi Asset Status terisi `Damaged` dan disabled sehingga tidak dapat diubah
35. Verifikasi label `Damaged Photo` tampil pada isian foto
36. Klik `[Mark as Found]` pada dialog tanpa mengisi Damaged Photo dan Note
37. Verifikasi caption `Damaged photo must not be empty` tampil di bawah Damaged Photo
38. Verifikasi caption `Note must not be empty` tampil di bawah Note
39. Pilih berkas `foto-kerusakan-printer.png` pada Damaged Photo
40. Isi Note `Rumah printer retak sejak sebelum hilang`
41. Klik `[Mark as Found]` pada dialog
42. Verifikasi toast `Success, [Asset Name] is available again.` tampil dengan nama aset `Printer HP LaserJet M404 {runId}`
43. Buka Damage Log milik aset `Printer HP LaserJet M404 {runId}`
44. Verifikasi Damage Log hanya memuat Damage record yang ditahan itu dan tidak memuat Damage Report baru
45. Verifikasi Damage record itu memuat node baru dengan foto `foto-kerusakan-printer.png` dan Note `Rumah printer retak sejak sebelum hilang`
46. Buka halaman `Assets`
47. Klik tab `Missing`
48. Klik sub-tab `History`
49. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
50. Klik `Printer HP LaserJet M404 {runId}` pada kolom Name
51. Verifikasi dialog Missing Log memuat node `Marked as found by` dengan Damaged Photo `foto-kerusakan-printer.png` dan Note `Rumah printer retak sejak sebelum hilang`

### Reject laporan pemegang memulihkan Condition Damaged
52. Klik sub-tab `Active`
53. Ketik Search `Monitor LG 27UL500 {runId}`, tekan Enter
54. Buka Damage Log milik aset `Monitor LG 27UL500 {runId}`
55. Verifikasi Damage record milik `Monitor LG 27UL500 {runId}` ditahan selama record `Waiting for Confirmation` berjalan dan aset tampil `Damaged + Missing`
56. Buka halaman `Assets`
57. Klik tab `Missing`
58. Ketik Search `Monitor LG 27UL500 {runId}`, tekan Enter
59. Buka menu `⋯` pada baris `Monitor LG 27UL500 {runId}`
60. Klik `Review`
61. Klik `[Reject]` pada dialog Missing Log
62. Isi Reason `Monitor masih dipakai dalam kondisi rusak`
63. Klik `[Reject]` pada dialog Reject Report
64. Buka Damage Log milik aset `Monitor LG 27UL500 {runId}`
65. Verifikasi Damage record milik `Monitor LG 27UL500 {runId}` aktif kembali
66. Verifikasi Asset Status `Monitor LG 27UL500 {runId}` kembali `Damaged`
