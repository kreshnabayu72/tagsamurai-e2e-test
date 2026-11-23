---
id: TC-FA-DAMAGED-E2E-017-gating-read-only
title: "Read Only melihat sub-tab Active dan History seluruh client dengan toolbar aktif, Download, tanpa badge jumlah tab, tanpa aksi tulis, dan tanpa kolom nilai finansial"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§2.1#r1, §2.1#r2, §2.1#r3, §2.1#r4, §2.1#r5, §2.1#r6, §2.1#r7, §2.1#r8, §2.1#r9, §2.1#r10, §2.1#r11, §4.8#r1, §4.8#r2, §4.8#r3, §4.8#r4, §4.8#r5, §4.8#r6, §4.8#r7, §4.8#r10, §4.8#r11, §4.8#r12, §4.8#r13, §2#b3, S-DMG-01, S-DMG-09, §9.11#b1, §5#r8, T-DMG-01, EB-AKS-4, §9.3#b1, §9.4.3#b6]
smoke: []
dependsOn: []
trace:
  §2.1#r1: [1, 2, 9, 13, 18, 36, 38]
  §2.1#r2: [44, 47]
  §2.1#r3: 7
  §2.1#r4: 14
  §2.1#r5: 15
  §2.1#r6: 10
  §2.1#r7: 10
  §2.1#r8: 10
  §2.1#r9: 19
  §2.1#r10: 22
  §2.1#r11: [5, 6]
  §4.8#r1: [1, 2]
  §4.8#r2: [44, 47]
  §4.8#r3: 44
  §4.8#r4: 7
  §4.8#r5: 10
  §4.8#r6: 14
  §4.8#r7: 15
  §4.8#r10: 10
  §4.8#r11: 19
  §4.8#r12: 29
  §4.8#r13: [21, 22]
  §2#b3: [10, 14, 44, 47]
  S-DMG-01: 3
  S-DMG-09: [28, 29]
  §9.11#b1: 29
  §5#r8: 29
  T-DMG-01: [5, 36, 43]
  EB-AKS-4: [5, 24, 28, 31, 33, 51, 53, 54, 58, 59]
  §9.3#b1: 10
  §9.4.3#b6: 66
anchor: [46, 65]
coverage:
  web: automated
---

# Read Only melihat sub-tab Active dan History seluruh client dengan toolbar aktif, Download, tanpa badge jumlah tab, tanpa aksi tulis, dan tanpa kolom nilai finansial

## Prerequisites
- Aktor: Read Only (DU-017-8).
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-017-1: Damage record aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office {runId}` (DU-017-6), status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pelapor umum DU-017-9.
  - DU-017-2: Damage record aset `Toyota Avanza {runId}` di Group `Branch Surabaya {runId}` (DU-017-7), status `Damaged`, Source `Manual`, dilaporkan DU-017-9.
  - DU-017-3: Damage record aset `Printer HP LaserJet M404 {runId}` di Group `Head Office {runId}`, status `Reported Disposal`, Source `Audit`, dilaporkan DU-017-9.
  - DU-017-4: Damage record aset `Drill Bosch GSB {runId}` di Group `Head Office {runId}`, status `Repaired`, Source `Manual`, dilaporkan DU-017-9.
  - DU-017-5: Damage record aset `Handheld Scanner Zebra TC21 {runId}` di Group `Head Office {runId}`, status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan DU-017-8 sebagai pelapor umum dari My Asset.
  - DU-017-6: Group `Head Office {runId}`.
  - DU-017-7: Group `Branch Surabaya {runId}`.
  - DU-017-8: User `Rina Wijaya {runId}`, role Read Only, tanpa hak Manage accounting; cakupan: seluruh client.
  - DU-017-9: User `Dewi Anggraeni {runId}`, pelapor umum tanpa hak Aktor Damaged; cakupan: aset yang ia pegang.
  - DU-017-10: Aset `Tablet Samsung Tab A8 {runId}` di Group `Head Office {runId}`, tanpa record Damaged berjalan.

## Test Steps

### Tab Damaged tanpa badge dan cakupan seluruh client
1. Verifikasi tab `Damaged` tampil pada halaman Assets
2. Verifikasi sub-tab `Active` dan `History` tampil
3. Verifikasi badge jumlah tidak tampil pada tab `Damaged`
4. Ketik Search `{runId}`, tekan Enter
5. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` di Group `Head Office {runId}` tampil di tabel
6. Verifikasi baris `Toyota Avanza {runId}` di Group `Branch Surabaya {runId}` tampil di tabel
7. Verifikasi baris `Handheld Scanner Zebra TC21 {runId}` laporan aktor sebagai pelapor umum tampil dengan status `Waiting for Confirmation` dan Source `Reported by holder`

### Aksi tulis tidak tersedia pada menu baris
8. Klik `⋯` pada baris `Toyota Avanza {runId}`
9. Verifikasi item `Damage Log` tampil pada menu baris
10. Verifikasi item `Mark as Repaired`, `Report Missing`, dan `Report Disposal` tidak tampil pada menu baris
11. Tekan Esc untuk menutup menu baris
12. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
13. Verifikasi item `Damage Log` tampil pada menu baris
14. Verifikasi item `Review` tidak tampil pada menu baris
15. Verifikasi item `Cancel Report` tidak tampil pada menu baris
16. Tekan Esc untuk menutup menu baris
17. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
18. Verifikasi item `Damage Log` tampil pada menu baris
19. Verifikasi item `Cancel Disposal Report` tidak tampil pada menu baris
20. Tekan Esc untuk menutup menu baris

### Toolbar aktif dan kolom nilai finansial tidak tersedia
21. Verifikasi tombol `Search by Scan` tampil di dalam kotak Search
22. Verifikasi tombol Download tampil pada toolbar
23. Klik ikon Filter pada toolbar
24. Verifikasi Filter Panel terbuka
25. Klik ikon Filter pada toolbar
26. Klik header kolom Actions `⋯`
27. Klik `Setup Column...`
28. Verifikasi Setup Column terbuka dan kolom `Group` tersedia
29. Verifikasi kolom `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)` tidak tersedia di Setup Column
30. Tekan Esc untuk menutup Setup Column
31. Verifikasi kontrol paginasi tampil di bawah tabel

### Sort kolom tersedia bagi Read Only
32. Klik ikon sort pada header kolom `Name`
33. Verifikasi baris pada tabel berurutan menaik menurut nama aset: `Handheld Scanner Zebra TC21 {runId}`, `Laptop Dell Latitude 5420 {runId}`, `Printer HP LaserJet M404 {runId}`, `Toyota Avanza {runId}`

### History dan Damage Log terbuka
34. Klik sub-tab `History`
35. Ketik Search `Drill Bosch GSB {runId}`, tekan Enter
36. Verifikasi baris `Drill Bosch GSB {runId}` tampil di tabel History dengan status `Repaired`
37. Klik nama aset `Drill Bosch GSB {runId}` pada kolom Name
38. Verifikasi dialog `Damage Log` terbuka untuk aset `Drill Bosch GSB {runId}`
39. Klik `✕` pada dialog `Damage Log`

### Report Damaged tidak tersedia di Asset List
40. Klik tab `Assets`
41. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
42. Centang baris aset `Tablet Samsung Tab A8 {runId}`
43. Verifikasi baris aset `Tablet Samsung Tab A8 {runId}` tampil di tabel Assets
44. Verifikasi tombol `[Report Damaged]` tidak tampil untuk aset `Tablet Samsung Tab A8 {runId}`

### Report Damaged tidak tersedia di Asset Detail
45. Klik nama aset `Tablet Samsung Tab A8 {runId}` untuk membuka Asset Detail
46. Verifikasi Asset Detail aset `Tablet Samsung Tab A8 {runId}` tampil
47. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) pada Asset Detail aset itu

### Pagination dapat dipakai Read Only
48. Klik tab `Damaged`
49. Klik sub-tab `Active`
50. Ketik Search `{runId}`, tekan Enter
51. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` di Group `Head Office {runId}` tampil di tabel
52. Ubah ukuran halaman menjadi `25`
53. Verifikasi ukuran halaman tabel menjadi `25`
54. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tetap tampil di tabel

### Filter menyempitkan hasil tabel
55. Klik ikon Filter pada toolbar
56. Pada Filter Panel, pilih Group `Branch Surabaya {runId}`
57. Klik `[Apply]`
58. Verifikasi baris `Toyota Avanza {runId}` di Group `Branch Surabaya {runId}` tampil di tabel
59. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tidak tampil di tabel

### Pelapor tanpa hak Aktor Damaged tidak melihat Review atas laporannya sendiri
60. Klik ikon Filter pada toolbar
61. Pada Filter Panel, ganti pilihan Group menjadi `Head Office {runId}`
62. Klik `[Apply]`
63. Ganti isi kotak search dengan `Handheld Scanner Zebra TC21 {runId}`, tekan Enter
64. Klik `⋯` pada baris `Handheld Scanner Zebra TC21 {runId}`
65. Verifikasi item `Damage Log` tampil pada menu baris
66. Verifikasi item `Review` tidak tampil pada menu baris laporan buatan aktor sendiri
