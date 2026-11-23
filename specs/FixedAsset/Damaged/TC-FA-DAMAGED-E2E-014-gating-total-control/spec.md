---
id: TC-FA-DAMAGED-E2E-014-gating-total-control
title: "Total Control melihat sub-tab Active, History, badge jumlah tab, kolom nilai finansial, seluruh aksi tulis, dan menjalankan Confirm"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§2.1#r1, §2.1#r2, §2.1#r3, §2.1#r4, §2.1#r5, §2.1#r6, §2.1#r7, §2.1#r8, §2.1#r9, §2.1#r10, §2.1#r11, §4.8#r1, §4.8#r2, §4.8#r3, §4.8#r4, §4.8#r5, §4.8#r6, §4.8#r7, §4.8#r10, §4.8#r11, §4.8#r12, §4.8#r13, §2#b2, §2#b3, §2#b5, S-DMG-01, S-DMG-09, §9.11#r2, §5#r8, T-DMG-01, §9.3#b1]
smoke: []
dependsOn: []
trace:
  §2.1#r1: [1, 2, 8, 31, 33]
  §2.1#r2: [11, 38]
  §2.1#r3: 38
  §2.1#r4: [17, 45]
  §2.1#r5: 18
  §2.1#r6: 9
  §2.1#r7: 10
  §2.1#r8: 11
  §2.1#r9: 14
  §2.1#r10: 21
  §2.1#r11: [5, 6]
  §4.8#r1: [1, 2]
  §4.8#r2: 38
  §4.8#r3: 38
  §4.8#r4: 38
  §4.8#r5: [9, 10]
  §4.8#r6: [17, 45]
  §4.8#r7: 18
  §4.8#r10: 11
  §4.8#r11: [14, 49, 51]
  §4.8#r12: 27
  §4.8#r13: [20, 21]
  §2#b2: [5, 6]
  §2#b3: [9, 10, 17, 38, 45]
  §2#b5: [17, 45]
  S-DMG-01: 3
  S-DMG-09: 27
  §9.11#r2: 27
  §5#r8: 27
  T-DMG-01: [5, 31]
  §9.3#b1: [23, 45, 46]
anchor: []
coverage:
  web: automated
---

# Total Control melihat sub-tab Active, History, badge jumlah tab, kolom nilai finansial, seluruh aksi tulis, dan menjalankan Confirm

## Prerequisites
- Aktor: Total Control (DU-014-9).
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-014-1: Damage record aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office {runId}` (DU-014-7), status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pelapor umum DU-014-10.
  - DU-014-2: Damage record aset `Toyota Avanza {runId}` di Group `Branch Surabaya {runId}` (DU-014-8), status `Damaged`, Source `Manual`, dilaporkan DU-014-9.
  - DU-014-3: Damage record aset `Printer HP LaserJet M404 {runId}` di Group `Head Office {runId}`, status `Reported Disposal`, Source `Audit`, dilaporkan DU-014-9.
  - DU-014-4: Damage record aset `Projector Epson EB-X06 {runId}` di Group `Head Office {runId}`, status `Damaged`, Source `Manual`, dilaporkan DU-014-9.
  - DU-014-5: Damage record aset `Drill Bosch GSB {runId}` di Group `Branch Surabaya {runId}`, status `Repaired`, Source `Manual`, dilaporkan DU-014-9.
  - DU-014-6: Aset `Tablet Samsung Tab A8 {runId}` di Group `Head Office {runId}`, tanpa record Damaged berjalan.
  - DU-014-7: Group `Head Office {runId}`.
  - DU-014-8: Group `Branch Surabaya {runId}`.
  - DU-014-9: User `Agus Pratama {runId}`, role Total Control; cakupan: seluruh client.
  - DU-014-10: User `Dewi Anggraeni {runId}`, pelapor umum tanpa hak Aktor Damaged; cakupan: aset yang ia pegang.
  - DU-014-11: Damage record aset `Forklift Toyota 8FD {runId}` di Group `Head Office {runId}`, status `Reported Disposal`, Source `Manual`, dilaporkan DU-014-12.
  - DU-014-12: User `Hendra Kusuma {runId}`, role Total Control; cakupan: seluruh client; aktor lain yang melaporkan DU-014-11, bukan aktor spec ini.

## Test Steps

### Tab Damaged, sub-tab, badge, dan cakupan seluruh client
1. Verifikasi tab `Damaged` tampil pada halaman Assets
2. Verifikasi sub-tab `Active` dan `History` tampil
3. Verifikasi badge jumlah record tampil pada tab `Damaged`
4. Ketik Search `{runId}`, tekan Enter
5. Verifikasi baris `Projector Epson EB-X06 {runId}` di Group `Head Office {runId}` tampil di tabel
6. Verifikasi baris `Toyota Avanza {runId}` di Group `Branch Surabaya {runId}` tampil di tabel

### Seluruh aksi tulis tersedia pada menu baris
7. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
8. Verifikasi item `Damage Log` tampil pada menu baris
9. Verifikasi item `Mark as Repaired` tampil pada menu baris
10. Verifikasi item `Report Missing` tampil pada menu baris
11. Verifikasi item `Report Disposal` tampil pada menu baris
12. Tekan Esc untuk menutup menu baris
13. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
14. Verifikasi item `Cancel Disposal Report` tampil pada menu baris
15. Tekan Esc untuk menutup menu baris
16. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
17. Verifikasi item `Review` tampil dan aktif pada menu baris
18. Verifikasi item `Cancel Report` tidak tampil pada menu baris
19. Tekan Esc untuk menutup menu baris

### Toolbar dan bulk tersedia
20. Verifikasi tombol `Search by Scan` tampil di dalam kotak Search
21. Verifikasi tombol Download tampil pada toolbar
22. Centang baris `Projector Epson EB-X06 {runId}`
23. Verifikasi bar bulk tampil dengan tombol `Bulk Action`
24. Klik ikon `×` pada bar bulk

### Kolom nilai finansial tersedia
25. Klik header kolom Actions `⋯`
26. Klik `Setup Column...`
27. Verifikasi kolom `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)` tersedia di Setup Column
28. Tekan Esc untuk menutup Setup Column

### History dan Damage Log terbuka
29. Klik sub-tab `History`
30. Ketik Search `Drill Bosch GSB {runId}`, tekan Enter
31. Verifikasi baris `Drill Bosch GSB {runId}` tampil di tabel History dengan status `Repaired`
32. Klik nama aset `Drill Bosch GSB {runId}` pada kolom Name
33. Verifikasi dialog `Damage Log` terbuka untuk aset `Drill Bosch GSB {runId}`
34. Klik `✕` pada dialog `Damage Log`

### Report Damaged tersedia di Asset List
35. Klik tab `Assets`
36. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
37. Centang baris aset `Tablet Samsung Tab A8 {runId}`
38. Verifikasi tombol `[Report Damaged]` tampil untuk aset `Tablet Samsung Tab A8 {runId}`

### Confirm sebagai aksi tulis yang dijalankan
39. Klik tab `Damaged`
40. Klik sub-tab `Active`
41. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
42. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
43. Klik `Review`
44. Klik `[Confirm]`
45. Verifikasi toast `Success, report has been confirmed.` tampil
46. Verifikasi badge status record pada dialog `Damage Log` `Damaged`
47. Klik `✕` pada dialog `Damage Log`

### Cancel Disposal Report tersedia atas laporan yang dilaporkan aktor lain
48. Ganti isi kotak search dengan `Forklift Toyota 8FD {runId}`, tekan Enter
49. Verifikasi baris aset `Forklift Toyota 8FD {runId}` tampil di tabel dengan status `Reported Disposal`
50. Klik `⋯` pada baris `Forklift Toyota 8FD {runId}`
51. Verifikasi item `Cancel Disposal Report` tampil pada menu baris
52. Tekan Esc untuk menutup menu baris
