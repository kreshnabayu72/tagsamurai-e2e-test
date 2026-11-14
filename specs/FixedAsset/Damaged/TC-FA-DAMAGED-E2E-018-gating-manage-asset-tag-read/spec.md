---
id: TC-FA-DAMAGED-E2E-018-gating-manage-asset-tag-read
title: "Pemegang Manage asset & TAG (Read) hanya melihat record Group penugasan dan descendant, dan tautan Damage Log record di luar cakupan ditolak 403"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§2.1#r1, §2.1#r2, §2.1#r3, §2.1#r4, §2.1#r5, §2.1#r6, §2.1#r7, §2.1#r8, §2.1#r9, §2.1#r10, §2.1#r11, §4.8#r1, §4.8#r2, §4.8#r3, §4.8#r4, §4.8#r5, §4.8#r6, §4.8#r7, §4.8#r8, §4.8#r9, §4.8#r10, §4.8#r11, §2#b2, S-DMG-01, S-DMG-09, §9.11#r1, §9.11#b1, §7.1#p1, §9.3#b2, §9.4.2#r19, §9.4.4#r15, T-DMG-01, §9.2#b19]
smoke: []
dependsOn: []
trace:
  §2.1#r1: [1, 2, 10, 14, 19, 30, 32]
  §2.1#r2: 38
  §2.1#r3: 8
  §2.1#r4: 15
  §2.1#r5: 16
  §2.1#r6: 11
  §2.1#r7: 11
  §2.1#r8: 11
  §2.1#r9: 20
  §2.1#r10: 23
  §2.1#r11: [5, 6, 7]
  §4.8#r1: [1, 2]
  §4.8#r2: 38
  §4.8#r3: 38
  §4.8#r4: 8
  §4.8#r5: 11
  §4.8#r6: 15
  §4.8#r7: 16
  §4.8#r8: 11
  §4.8#r9: 20
  §4.8#r10: 26
  §4.8#r11: [22, 23]
  §2#b2: [5, 7]
  S-DMG-01: 3
  S-DMG-09: [25, 26]
  §9.11#r1: [5, 6, 7, 32]
  §9.11#b1: 26
  §7.1#p1: 43
  §9.3#b2: [40, 43]
  §9.4.2#r19: [43, 44]
  §9.4.4#r15: [43, 44]
  T-DMG-01: [5, 30, 37]
  §9.2#b19: [40, 43]
anchor: []
coverage:
  web: automated
---

# Pemegang Manage asset & TAG (Read) hanya melihat record Group penugasan dan descendant, dan tautan Damage Log record di luar cakupan ditolak 403

## Prerequisites
- Aktor: pemegang Manage asset & TAG dengan Read pada Group `Head Office {runId}` (DU-018-9).
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-018-1: Damage record aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office {runId}` (DU-018-7), status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pelapor umum DU-018-10.
  - DU-018-2: Damage record aset `Projector Epson EB-X06 {runId}` di Group `Sub Head Office {runId}` (DU-018-8, descendant `Head Office {runId}`), status `Damaged`, Source `Manual`, dilaporkan DU-018-10.
  - DU-018-3: Damage record aset `Printer HP LaserJet M404 {runId}` di Group `Head Office {runId}`, status `Reported Disposal`, Source `Stock opname`, dilaporkan DU-018-10.
  - DU-018-4: Damage record aset `Toyota Avanza {runId}` di Group `Branch Surabaya {runId}` (di luar Group penugasan), status `Damaged`, Source `Manual`, dilaporkan DU-018-10.
  - DU-018-5: Damage record aset `Drill Bosch GSB {runId}` di Group `Head Office {runId}`, status `Repaired`, Source `Manual`, dilaporkan DU-018-10.
  - DU-018-6: Damage record aset `Handheld Scanner Zebra TC21 {runId}` di Group `Head Office {runId}`, status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan DU-018-9 sebagai pelapor umum dari My Asset.
  - DU-018-7: Group `Head Office {runId}`.
  - DU-018-8: Group `Sub Head Office {runId}`, descendant dari `Head Office {runId}`.
  - DU-018-11: Group `Branch Surabaya {runId}`.
  - DU-018-9: User `Rina Wijaya {runId}`, pemegang Manage asset & TAG dengan Read pada Group `Head Office {runId}`, tanpa hak Manage accounting; cakupan: Group penugasan beserta descendant.
  - DU-018-10: User `Dewi Anggraeni {runId}`, pelapor umum tanpa hak Aktor Damaged; cakupan: aset yang ia pegang.
  - DU-018-12: Aset `Tablet Samsung Tab A8 {runId}` di Group `Head Office {runId}`, tanpa record Damaged berjalan.

## Test Steps

### Tab Damaged tanpa badge dan cakupan Group penugasan beserta descendant
1. Verifikasi tab `Damaged` tampil pada halaman Assets
2. Verifikasi sub-tab `Active` dan `History` tampil
3. Verifikasi badge jumlah tidak tampil pada tab `Damaged`
4. Ketik Search `{runId}`, tekan Enter
5. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` di Group penugasan `Head Office {runId}` tampil di tabel
6. Verifikasi baris `Projector Epson EB-X06 {runId}` di Group descendant `Sub Head Office {runId}` tampil di tabel
7. Verifikasi baris `Toyota Avanza {runId}` di Group `Branch Surabaya {runId}` tidak tampil di tabel
8. Verifikasi baris `Handheld Scanner Zebra TC21 {runId}` laporan aktor sebagai pelapor umum tampil dengan status `Waiting for Confirmation` dan Source `Reported by holder`

### Aksi tulis tidak tersedia pada menu baris
9. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
10. Verifikasi item `Damage Log` tampil pada menu baris
11. Verifikasi item `Mark as Repaired`, `Report Missing`, dan `Report Disposal` tidak tampil pada menu baris
12. Tekan Esc untuk menutup menu baris
13. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
14. Verifikasi item `Damage Log` tampil pada menu baris
15. Verifikasi item `Review` tidak tampil pada menu baris
16. Verifikasi item `Cancel Report` tidak tampil pada menu baris
17. Tekan Esc untuk menutup menu baris
18. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
19. Verifikasi item `Damage Log` tampil pada menu baris
20. Verifikasi item `Cancel Disposal Report` tidak tampil pada menu baris
21. Tekan Esc untuk menutup menu baris

### Toolbar dan kolom nilai finansial tidak tersedia
22. Verifikasi tombol `Search by Scan` tampil di dalam kotak Search
23. Verifikasi tombol Download tampil pada toolbar
24. Klik tombol Setup Column pada toolbar
25. Verifikasi kolom `Group` tersedia di Setup Column
26. Verifikasi kolom `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)` tidak tersedia di Setup Column
27. Tekan Esc untuk menutup Setup Column

### History dan Damage Log terbuka
28. Klik sub-tab `History`
29. Ketik Search `Drill Bosch GSB {runId}`, tekan Enter
30. Verifikasi baris `Drill Bosch GSB {runId}` tampil di tabel History dengan status `Repaired`
31. Klik nama aset `Drill Bosch GSB {runId}` pada kolom Name
32. Verifikasi dialog `Damage Log` terbuka untuk aset `Drill Bosch GSB {runId}`
33. Klik `✕` pada dialog `Damage Log`

### Report Damaged tidak tersedia di Asset List
34. Klik tab `Assets`
35. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
36. Centang baris aset `Tablet Samsung Tab A8 {runId}`
37. Verifikasi baris aset `Tablet Samsung Tab A8 {runId}` tampil di tabel Assets
38. Verifikasi tombol `[Report Damaged]` tidak tampil untuk aset `Tablet Samsung Tab A8 {runId}`

### Tautan Damage Log di luar cakupan ditolak
39. Buka tautan Damage Log langsung untuk record aset `Projector Epson EB-X06 {runId}`
40. Verifikasi dialog `Damage Log` terbuka untuk aset `Projector Epson EB-X06 {runId}` dari tautan langsung
41. Klik `✕` pada dialog `Damage Log`
42. Buka tautan Damage Log langsung untuk record aset `Toyota Avanza {runId}`
43. Verifikasi halaman menampilkan state akses ditolak `403`
44. Verifikasi dialog `Damage Log` untuk aset `Toyota Avanza {runId}` tidak tampil
