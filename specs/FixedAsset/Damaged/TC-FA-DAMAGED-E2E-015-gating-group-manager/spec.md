---
id: TC-FA-DAMAGED-E2E-015-gating-group-manager
title: "Group Manager hanya melihat record Group binaan dan sub-group, dengan aksi tulis dan Cancel Disposal Report atas Group binaan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§2.1#r1, §2.1#r2, §2.1#r3, §2.1#r4, §2.1#r5, §2.1#r6, §2.1#r7, §2.1#r8, §2.1#r9, §2.1#r10, §2.1#r11, §4.8#r1, §4.8#r2, §4.8#r3, §4.8#r4, §4.8#r5, §4.8#r6, §4.8#r7, §4.8#r10, §4.8#r11, §4.8#r12, §4.8#r13, §2#b2, §2#b5, S-DMG-01, S-DMG-09, §9.11#r2, T-DMG-01, §9.3#b1]
smoke: []
dependsOn: []
trace:
  §2.1#r1: [1, 2, 10, 33, 35]
  §2.1#r2: [13, 40]
  §2.1#r3: 40
  §2.1#r4: 19
  §2.1#r5: 20
  §2.1#r6: [11, 48]
  §2.1#r7: 12
  §2.1#r8: 13
  §2.1#r9: [16, 61]
  §2.1#r10: 23
  §2.1#r11: [6, 7, 8]
  §4.8#r1: [1, 2]
  §4.8#r2: [40, 53]
  §4.8#r3: 40
  §4.8#r4: 40
  §4.8#r5: [11, 12, 48]
  §4.8#r6: 19
  §4.8#r7: 20
  §4.8#r10: 13
  §4.8#r11: [16, 58, 61]
  §4.8#r12: 29
  §4.8#r13: [22, 23]
  §2#b2: [6, 8]
  §2#b5: [3, 48]
  S-DMG-01: [3, 4]
  S-DMG-09: [28, 29]
  §9.11#r2: 29
  T-DMG-01: [6, 33]
  §9.3#b1: [25, 48, 49]
anchor: [57, 59]
coverage:
  web: automated
---

# Group Manager hanya melihat record Group binaan dan sub-group, dengan aksi tulis dan Cancel Disposal Report atas Group binaan

## Prerequisites
- Aktor: Group Manager (DU-015-10), dengan Group binaan `Head Office {runId}`.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-015-1: Damage record aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office {runId}` (DU-015-7), status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pelapor umum DU-015-11.
  - DU-015-2: Damage record aset `Projector Epson EB-X06 {runId}` tanpa TAG di Group `Sub Head Office {runId}` (DU-015-8, sub-group dari `Head Office {runId}`), status `Damaged`, Source `Manual`, dilaporkan DU-015-10.
  - DU-015-3: Damage record aset `Printer HP LaserJet M404 {runId}` di Group `Head Office {runId}`, status `Reported Disposal`, Source `Audit`, dilaporkan DU-015-10.
  - DU-015-4: Damage record aset `Toyota Avanza {runId}` di Group `Branch Surabaya {runId}` (DU-015-9, di luar Group binaan), status `Damaged`, Source `Manual`, dilaporkan DU-015-10.
  - DU-015-5: Damage record aset `Drill Bosch GSB {runId}` di Group `Head Office {runId}`, status `Repaired`, Source `Manual`, dilaporkan DU-015-10.
  - DU-015-6: Aset `Tablet Samsung Tab A8 {runId}` di Group `Head Office {runId}`, tanpa record Damaged berjalan.
  - DU-015-7: Group `Head Office {runId}`.
  - DU-015-8: Group `Sub Head Office {runId}`, sub-group dari `Head Office {runId}`.
  - DU-015-9: Group `Branch Surabaya {runId}`.
  - DU-015-10: User `Rina Wijaya {runId}`, role Group Manager dengan Group binaan `Head Office {runId}`, tanpa hak Manage accounting; cakupan: Group binaan beserta sub-group.
  - DU-015-11: User `Dewi Anggraeni {runId}`, pelapor umum tanpa hak Aktor Damaged; cakupan: aset yang ia pegang.
  - DU-015-13: Damage record aset `Forklift Toyota 8FD {runId}` di Group `Branch Surabaya {runId}` (DU-015-9, di luar Group binaan), status `Reported Disposal`, Source `Manual`, dilaporkan DU-015-10.
  - DU-015-14: Damage record aset `Monitor Dell P2422H {runId}` di Group `Head Office {runId}`, status `Reported Disposal`, Source `Manual`, dilaporkan DU-015-15.
  - DU-015-15: User `Agus Pratama {runId}`, role Total Control; cakupan: seluruh Group.
  - Badge jumlah pada tab `Damaged` bernilai `2`, dari DU-015-1 (`Waiting for Confirmation`) dan DU-015-2 (`Damaged` tanpa penanda Missing) di Group binaan beserta sub-group; DU-015-3 dan DU-015-14 (`Reported Disposal`) dan DU-015-5 (`Repaired`) tidak dihitung, dan DU-015-4 di luar Group binaan tidak dihitung.
- Kondisi: After photo required bernilai `OFF`.

## Test Steps

### Tab Damaged, badge, dan cakupan Group binaan beserta sub-group
1. Verifikasi tab `Damaged` tampil pada halaman Assets
2. Verifikasi sub-tab `Active` dan `History` tampil
3. Verifikasi badge jumlah record tampil pada tab `Damaged`
4. Verifikasi badge jumlah pada tab `Damaged` bernilai `2`, dari record Group binaan beserta sub-group saja
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` di Group binaan `Head Office {runId}` tampil di tabel
7. Verifikasi baris `Projector Epson EB-X06 {runId}` di sub-group `Sub Head Office {runId}` tampil di tabel
8. Verifikasi baris `Toyota Avanza {runId}` di Group `Branch Surabaya {runId}` tidak tampil di tabel

### Aksi tulis tersedia pada menu baris Group binaan
9. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
10. Verifikasi item `Damage Log` tampil pada menu baris
11. Verifikasi item `Mark as Repaired` tampil pada menu baris
12. Verifikasi item `Report Missing` tampil pada menu baris
13. Verifikasi item `Report Disposal` tampil pada menu baris
14. Tekan Esc untuk menutup menu baris
15. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
16. Verifikasi item `Cancel Disposal Report` tampil pada menu baris atas Group binaan
17. Tekan Esc untuk menutup menu baris
18. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
19. Verifikasi item `Review` tampil dan aktif pada menu baris
20. Verifikasi item `Cancel Report` tidak tampil pada menu baris
21. Tekan Esc untuk menutup menu baris

### Toolbar dan bulk tersedia
22. Verifikasi tombol `Search by Scan` tampil di dalam kotak Search
23. Verifikasi tombol Download tampil pada toolbar
24. Centang baris `Projector Epson EB-X06 {runId}`
25. Verifikasi bar bulk tampil dengan tombol `Bulk Action`
26. Klik ikon `×` pada bar bulk

### Kolom nilai finansial tidak tersedia tanpa hak
27. Klik tombol Setup Column pada toolbar
28. Verifikasi kolom `Group` tersedia di Setup Column
29. Verifikasi kolom `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)` tidak tersedia di Setup Column
30. Tekan Esc untuk menutup Setup Column

### History dan Damage Log terbuka
31. Klik sub-tab `History`
32. Ketik Search `Drill Bosch GSB {runId}`, tekan Enter
33. Verifikasi baris `Drill Bosch GSB {runId}` tampil di tabel History dengan status `Repaired`
34. Klik nama aset `Drill Bosch GSB {runId}` pada kolom Name
35. Verifikasi dialog `Damage Log` terbuka untuk aset `Drill Bosch GSB {runId}`
36. Klik `✕` pada dialog `Damage Log`

### Report Damaged tersedia di Asset List
37. Klik tab `Assets`
38. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
39. Centang baris aset `Tablet Samsung Tab A8 {runId}`
40. Verifikasi tombol `[Report Damaged]` tampil untuk aset `Tablet Samsung Tab A8 {runId}`

### Mark as Repaired sebagai aksi tulis yang dijalankan
41. Klik tab `Damaged`
42. Klik sub-tab `Active`
43. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
44. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
45. Klik `Mark as Repaired`
46. Isi Repair note `Lampu proyektor diganti dan unit sudah diuji menyala normal`
47. Klik `[Mark as Repaired]` pada dialog `Mark as Repaired`
48. Verifikasi toast `Success, [Asset Name] has been marked as repaired.` tampil dengan `[Asset Name]` berisi nama aset `Projector Epson EB-X06 {runId}`
49. Verifikasi sub-tab Active menampilkan `No results found` untuk Search `Projector Epson EB-X06 {runId}`

### Report Damaged tersedia di Asset Detail
50. Klik tab `Assets`
51. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
52. Klik nama aset `Tablet Samsung Tab A8 {runId}` untuk membuka Asset Detail
53. Verifikasi aksi `Report Damaged` tersedia pada Asset Detail

### Reported Disposal di luar Group binaan tidak tampil
54. Klik tab `Damaged`
55. Klik sub-tab `Active`
56. Ketik Search `{runId}`, tekan Enter
57. Verifikasi baris `Printer HP LaserJet M404 {runId}` di Group binaan `Head Office {runId}` tampil di tabel dengan status `Reported Disposal`
58. Verifikasi baris `Forklift Toyota 8FD {runId}` di Group `Branch Surabaya {runId}` tidak tampil di tabel

### Cancel Disposal Report tampil untuk laporan aktor lain di Group binaan
59. Verifikasi baris `Monitor Dell P2422H {runId}` di Group binaan `Head Office {runId}` tampil di tabel dengan status `Reported Disposal`, dilaporkan `Agus Pratama {runId}`
60. Klik `⋯` pada baris `Monitor Dell P2422H {runId}`
61. Verifikasi item `Cancel Disposal Report` tampil pada menu baris atas laporan yang dilaporkan `Agus Pratama {runId}`, bukan oleh Group Manager sendiri
62. Tekan Esc untuk menutup menu baris
