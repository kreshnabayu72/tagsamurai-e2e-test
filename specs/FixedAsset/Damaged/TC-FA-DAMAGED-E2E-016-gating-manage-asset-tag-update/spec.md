---
id: TC-FA-DAMAGED-E2E-016-gating-manage-asset-tag-update
title: "Pemegang Manage asset & TAG (Update) menjalankan aksi tulis pada aset Group Update dan descendant, mengikuti kolom Read di Group lain, dan kehilangan aksi saat capability dicabut"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§2.1#r1, §2.1#r2, §2.1#r3, §2.1#r4, §2.1#r5, §2.1#r6, §2.1#r7, §2.1#r8, §2.1#r9, §2.1#r10, §2.1#r11, §4.8#r1, §4.8#r2, §4.8#r3, §4.8#r4, §4.8#r5, §4.8#r6, §4.8#r7, §4.8#r10, §4.8#r11, §4.8#r12, §4.8#r13, §2#b2, §2#b3, §2#b5, §2.1#b9, §2.1#b6, S-DMG-01, S-DMG-06, S-DMG-09, T-DMG-01, §9.3#b1, EB-AKS-5@confirm, EB-AKS-6, D-DISP-15]
smoke: []
dependsOn: []
trace:
  §2.1#r1: [1, 2, 10, 16, 38, 40]
  §2.1#r2: [13, 45]
  §2.1#r3: 45
  §2.1#r4: [20, 54]
  §2.1#r5: 21
  §2.1#r6: 11
  §2.1#r7: 12
  §2.1#r8: 13
  §2.1#r9: [17, 74, 78]
  §2.1#r10: 28
  §2.1#r11: [5, 6, 7]
  §4.8#r1: [1, 2]
  §4.8#r2: [45, 47]
  §4.8#r3: 45
  §4.8#r4: 45
  §4.8#r5: [11, 12, 25]
  §4.8#r6: [20, 54]
  §4.8#r7: 21
  §4.8#r10: 13
  §4.8#r11: [17, 74, 78]
  §4.8#r12: 34
  §4.8#r13: [27, 28]
  §2#b2: 5
  §2#b3: [11, 12, 20, 45, 47, 54]
  §2#b5: 3
  §2.1#b9: [7, 8, 24, 25]
  §2.1#b6: [13, 17, 74, 78]
  S-DMG-01: 3
  S-DMG-06: 17
  S-DMG-09: [33, 34]
  T-DMG-01: [5, 38]
  §9.3#b1: [30, 54]
  EB-AKS-5@confirm: [54, 55]
  EB-AKS-6: [62, 63, 66, 67]
  D-DISP-15: [13, 17, 74, 78]
anchor: [72, 77]
coverage:
  web: automated
---

# Pemegang Manage asset & TAG (Update) menjalankan aksi tulis pada aset Group Update dan descendant, mengikuti kolom Read di Group lain, dan kehilangan aksi saat capability dicabut

## Prerequisites
- Aktor: pemegang Manage asset & TAG dengan Update pada Group `Head Office {runId}` dan Read pada Group `Branch Surabaya {runId}` (DU-016-11); `Agus Pratama {runId}` (DU-016-12) hanya memicu perubahan capability; di akhir spec aktor berganti ke pemegang Manage asset & TAG dengan Update pada Group `Head Office {runId}` tanpa Asset Admin sub-tab Disposal yang melaporkan Report Disposal sendiri, `Maya Puspita {runId}` (DU-016-16).
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-016-1: Damage record aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office {runId}` (DU-016-8), status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pelapor umum DU-016-13.
  - DU-016-2: Damage record aset `Projector Epson EB-X06 {runId}` di Group `Sub Head Office {runId}` (DU-016-9, descendant `Head Office {runId}`), status `Damaged`, Source `Manual`, dilaporkan DU-016-12.
  - DU-016-3: Damage record aset `Printer HP LaserJet M404 {runId}` di Group `Head Office {runId}`, status `Reported Disposal`, Source `Audit`, dilaporkan DU-016-12.
  - DU-016-4: Damage record aset `Toyota Avanza {runId}` di Group `Branch Surabaya {runId}` (DU-016-10), status `Damaged`, Source `Manual`, dilaporkan DU-016-12.
  - DU-016-5: Damage record aset `Drill Bosch GSB {runId}` di Group `Head Office {runId}`, status `Repaired`, Source `Manual`, dilaporkan DU-016-12.
  - DU-016-6: Aset `Tablet Samsung Tab A8 {runId}` di Group `Head Office {runId}`, tanpa record Damaged berjalan.
  - DU-016-7: Damage record aset `Handheld Scanner Zebra TC21 {runId}` di Group `Head Office {runId}`, status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pelapor umum DU-016-13.
  - DU-016-8: Group `Head Office {runId}`.
  - DU-016-9: Group `Sub Head Office {runId}`, descendant dari `Head Office {runId}`.
  - DU-016-10: Group `Branch Surabaya {runId}`.
  - DU-016-11: User `Rina Wijaya {runId}`, pemegang Manage asset & TAG dengan Update pada Group `Head Office {runId}` dan Read pada Group `Branch Surabaya {runId}`, tanpa hak Manage accounting dan tanpa Asset Admin sub-tab Disposal; cakupan: Group Update beserta descendant, ditambah Group Read. Pencabutan di akhir spec hanya mencabut Update pada Group `Head Office {runId}`; Read pada Group `Head Office {runId}` tetap dimiliki.
  - DU-016-12: User `Agus Pratama {runId}`, role Total Control; cakupan: seluruh client.
  - DU-016-13: User `Dewi Anggraeni {runId}`, pelapor umum tanpa hak Aktor Damaged; cakupan: aset yang ia pegang.
  - DU-016-14: Group `Gudang Bandung {runId}`, tanpa Update maupun Read bagi DU-016-11.
  - DU-016-15: Damage record aset `Forklift Toyota 8FD {runId}` di Group `Gudang Bandung {runId}` (DU-016-14), status `Damaged`, Source `Manual`, dilaporkan DU-016-12.
  - DU-016-16: User `Maya Puspita {runId}`, pemegang Manage asset & TAG dengan Update pada Group `Head Office {runId}`, tanpa Asset Admin sub-tab Disposal dan tanpa hak Manage accounting; cakupan: Group Update beserta descendant.
  - DU-016-17: Damage record aset `Scanner Brother ADS-2200 {runId}` di Group `Head Office {runId}`, status `Reported Disposal`, Source `Manual`, dilaporkan DU-016-16.
- Kondisi:
  - Level Feature Suite Disposal bernilai `Full`.

## Test Steps

### Tab Damaged, badge, dan cakupan Group Update, descendant, serta Group Read
1. Verifikasi tab `Damaged` tampil pada halaman Assets
2. Verifikasi sub-tab `Active` dan `History` tampil
3. Verifikasi badge jumlah record tampil pada tab `Damaged`
4. Ketik Search `{runId}`, tekan Enter
5. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` di Group Update `Head Office {runId}` tampil di tabel
6. Verifikasi baris `Projector Epson EB-X06 {runId}` di Group descendant `Sub Head Office {runId}` tampil di tabel
7. Verifikasi baris `Toyota Avanza {runId}` di Group Read `Branch Surabaya {runId}` tampil di tabel
8. Verifikasi baris `Forklift Toyota 8FD {runId}` di Group `Gudang Bandung {runId}` tanpa Update maupun Read tidak tampil di tabel

### Aksi tulis tersedia pada menu baris Group Update
9. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
10. Verifikasi item `Damage Log` tampil pada menu baris
11. Verifikasi item `Mark as Repaired` tampil pada menu baris
12. Verifikasi item `Report Missing` tampil pada menu baris
13. Verifikasi item `Report Disposal` tampil pada menu baris karena hak melapor Report Disposal mengikuti Pelapor Report, termasuk pemegang Update atas aset Damaged
14. Tekan Esc untuk menutup menu baris
15. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
16. Verifikasi item `Damage Log` tampil pada menu baris
17. Verifikasi item `Cancel Disposal Report` tidak tampil pada menu baris laporan yang dilaporkan `Agus Pratama {runId}`, karena hak Cancel Disposal Report pemegang Update hanya atas laporan miliknya
18. Tekan Esc untuk menutup menu baris
19. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
20. Verifikasi item `Review` tampil dan aktif pada menu baris
21. Verifikasi item `Cancel Report` tidak tampil pada menu baris
22. Tekan Esc untuk menutup menu baris

### Group Read hanya menampilkan baca
23. Klik `⋯` pada baris `Toyota Avanza {runId}`
24. Verifikasi item `Damage Log` tampil pada menu baris Group Read
25. Verifikasi item `Mark as Repaired` dan `Report Missing` tidak tampil pada menu baris Group Read
26. Tekan Esc untuk menutup menu baris

### Toolbar dan bulk tersedia
27. Verifikasi tombol `Search by Scan` tampil di dalam kotak Search
28. Verifikasi tombol Download tampil pada toolbar
29. Centang baris `Projector Epson EB-X06 {runId}`
30. Verifikasi bar bulk tampil dengan tombol `Bulk Action`
31. Klik ikon `×` pada bar bulk

### Kolom nilai finansial tidak tersedia tanpa hak
32. Klik tombol Setup Column pada toolbar
33. Verifikasi kolom `Group` tersedia di Setup Column
34. Verifikasi kolom `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)` tidak tersedia di Setup Column
35. Tekan Esc untuk menutup Setup Column

### History dan Damage Log terbuka
36. Klik sub-tab `History`
37. Ketik Search `Drill Bosch GSB {runId}`, tekan Enter
38. Verifikasi baris `Drill Bosch GSB {runId}` tampil di tabel History dengan status `Repaired`
39. Klik nama aset `Drill Bosch GSB {runId}` pada kolom Name
40. Verifikasi dialog `Damage Log` terbuka untuk aset `Drill Bosch GSB {runId}`
41. Klik `✕` pada dialog `Damage Log`

### Report Damaged tersedia di Asset List
42. Klik tab `Assets`
43. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
44. Centang baris aset `Tablet Samsung Tab A8 {runId}`
45. Verifikasi tombol `[Report Damaged]` tampil untuk aset `Tablet Samsung Tab A8 {runId}`

### Report Damaged tersedia di Asset Detail
46. Klik nama aset `Tablet Samsung Tab A8 {runId}` untuk membuka Asset Detail
47. Verifikasi aksi `Report Damaged` tersedia pada Asset Detail

### Confirm dijalankan oleh pemegang Update
48. Klik tab `Damaged`
49. Klik sub-tab `Active`
50. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
51. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
52. Klik `Review`
53. Klik `[Confirm]`
54. Verifikasi toast `Success, report has been confirmed.` tampil
55. Verifikasi badge status record pada dialog `Damage Log` `Damaged`
56. Klik `✕` pada dialog `Damage Log`

### Capability dicabut saat halaman terbuka
57. Ganti isi kotak search dengan `Handheld Scanner Zebra TC21 {runId}`, tekan Enter
58. Klik `⋯` pada baris `Handheld Scanner Zebra TC21 {runId}`
59. Klik `Review`
60. Agus Pratama {runId} mencabut capability Update Manage asset & TAG dari aktor
61. Klik `[Confirm]`
62. Verifikasi toast `You don't have permission to do this.` tampil
63. Verifikasi badge status record pada dialog `Damage Log` tetap `Waiting for Confirmation`
64. Klik `✕` pada dialog `Damage Log`
65. Klik `⋯` pada baris `Handheld Scanner Zebra TC21 {runId}`
66. Verifikasi item `Damage Log` tampil pada menu baris
67. Verifikasi item `Review` tidak tampil pada menu baris

### Cancel Disposal Report tersedia bagi pemegang Update sebagai pelapor hanya pada laporan miliknya
68. Keluar dari aplikasi
69. Masuk sebagai Maya Puspita {runId} dari sesi browser baru
70. Klik tab `Damaged`
71. Ketik Search `{runId}`, tekan Enter
72. Verifikasi baris `Scanner Brother ADS-2200 {runId}` laporan `Maya Puspita {runId}` tampil di tabel dengan status `Reported Disposal`
73. Klik `⋯` pada baris `Scanner Brother ADS-2200 {runId}`
74. Verifikasi item `Cancel Disposal Report` tampil pada menu baris laporan milik aktor
75. Tekan Esc untuk menutup menu baris
76. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
77. Verifikasi item `Damage Log` tampil pada menu baris
78. Verifikasi item `Cancel Disposal Report` tidak tampil pada menu baris laporan yang dilaporkan `Agus Pratama {runId}`
79. Tekan Esc untuk menutup menu baris
