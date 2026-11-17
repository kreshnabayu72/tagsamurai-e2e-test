---
id: TC-FA-DAMAGED-E2E-030-report-damaged-satu-aset-dep-asset
title: "Report Damaged satu aset dari Asset List / Asset Detail oleh Pelapor admin membuat record Damaged, banner Asset Detail, dan status global Damaged"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-01, §4.1#r5, §4.1#r10, §4.2.3#p1, §4.2.3#p2, §4.2.3#b1, §4.4#r3, TS-DMG-01, S-DMG-18, S-DMG-19, §4.2.2#p1, §8.2#b1, §Aturan Logika Modul#r13, §Aturan Logika Modul#r14, §Aturan Logika Modul#r42, §Aturan Logika Modul#r44, §Aturan Logika Modul#r48, §Aturan Logika Modul#r25, §9.7#r1, §3#p2, EC-DMG-04, §9.4.4#r2, F-DMG-01, §4.8#r2, §2.1#r2, §9.6#r1, T-DMG-01, EB-FB-1@report-damaged, EB-FRM-1@report-damaged]
smoke: [EB-FB-1@report-damaged, EB-FRM-1@report-damaged]
dependsOn:
  - "Asset: Asset List dan Asset Detail (tombol Report Damaged, banner Damaged)"
trace:
  D-DMG-01: [13, 42]
  §4.1#r5: [10, 13]
  §4.1#r10: [23, 26, 42]
  §4.2.3#p1: [10, 41]
  §4.2.3#p2: [4, 5, 6, 37]
  §4.2.3#b1: [50, 53]
  §4.4#r3: [10, 41]
  TS-DMG-01: [10, 41]
  S-DMG-18: [57, 58]
  S-DMG-19: [23, 24, 42, 63, 64, 65, 70, 74]
  §4.2.2#p1: 26
  §8.2#b1: 31
  §Aturan Logika Modul#r13: 47
  §Aturan Logika Modul#r14: [47, 59, 66]
  §Aturan Logika Modul#r42: 14
  §Aturan Logika Modul#r44: [27, 28]
  §Aturan Logika Modul#r48: 15
  §Aturan Logika Modul#r25: [21, 43]
  §9.7#r1: [21, 43]
  §3#p2: [14, 21]
  EC-DMG-04: [50, 53]
  §9.4.4#r2: [50, 53]
  F-DMG-01: [10, 41]
  §4.8#r2: [2, 35]
  §2.1#r2: [2, 35]
  §9.6#r1: [10, 31]
  T-DMG-01: [14, 15, 16, 17, 18]
  EB-FB-1@report-damaged: 10
  EB-FRM-1@report-damaged: [13, 31]
anchor: [46, 49, 52]
coverage:
  web: automated
---

# Report Damaged satu aset dari Asset List / Asset Detail oleh Pelapor admin membuat record Damaged, banner Asset Detail, dan status global Damaged

## Prerequisites
- Aktor: Total Control (Pelapor admin).
- Layar awal: halaman Assets, tab Assets (Asset List).
- Data:
  - DU-030-1: aset `Projector Epson EB-X06 {runId}`, Group `Head Office`, status global `Normal`, tanpa record Damage, ada di entitas aktor (dilaporkan dari Asset List).
  - DU-030-2: aset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, status global `Normal`, tanpa record Damage, ada di entitas aktor (dilaporkan dari Asset Detail).
  - DU-030-5: aset `Monitor Dell P2422H {runId}`, Group `Head Office`, status global `Damaged`, sudah punya record Damage berjalan berstatus `Damaged` yang dilaporkan pemegang pada `T0 − 5 hari, pukul 09:10` (Reported Date), di-Confirm pada `T0 − 2 hari, pukul 10:30`, dan node terbarunya tercatat pada `T0 − 1 hari, pukul 16:40`, ada di entitas aktor.
  - DU-030-8: aset `Headset Logitech H390 {runId}`, Group `Head Office`, status global `Damaged`, sudah punya record Damage berjalan berstatus `Waiting for Confirmation` yang dilaporkan pemegang pada `T0 − 3 hari, pukul 09:15`, ada di entitas aktor.
  - DU-030-9: aset `Laptop Lenovo ThinkPad E14 {runId}`, Group `Head Office`, status global `Damaged`, sudah punya record Damage berjalan berstatus `Reported Disposal`, ada di entitas aktor.
  - DU-030-10: aset `Keyboard Logitech K380 {runId}`, Group `Head Office`, status global `Damaged`, sudah punya record Damage berjalan berstatus `In Disposal Process`, ada di entitas aktor.
  - DU-030-6: aset `Scanner Fujitsu fi-7160 {runId}`, Group `Head Office`, status `Disposed`, ada di entitas aktor.
  - DU-030-7: aset `Drill Bosch GSB {runId}`, Group `Head Office`, status `Missing`, tanpa record Damage, ada di entitas aktor.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps

### Report Damaged satu aset dari Asset List
1. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
2. Verifikasi aksi `Report Damaged` tersedia untuk baris `Projector Epson EB-X06 {runId}`
3. Klik `[Report Damaged]` pada baris `Projector Epson EB-X06 {runId}`
4. Verifikasi dialog berjudul `Report Damaged` tampil dengan blok aset `Projector Epson EB-X06 {runId}`
5. Verifikasi field `What happened` tampil pada dialog
6. Verifikasi field `Damaged Photo` tampil pada dialog
7. Isi `What happened` dengan `Layar proyektor retak dan tidak menampilkan gambar`
8. Unggah foto `proyektor-retak.jpg` pada `Damaged Photo`
9. Klik `[Report Damaged]` pada footer dialog
10. Verifikasi toast `Success, asset has been reported damaged.` tampil

### Record Damaged tercatat di sub-tab Active tab Damaged
11. Buka tab `Damaged` pada halaman Assets
12. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
13. Verifikasi tepat satu baris `Projector Epson EB-X06 {runId}` tampil di sub-tab `Active`
14. Verifikasi Status baris itu `Damaged`
15. Verifikasi Source baris itu `Manual`
16. Verifikasi Days Damaged baris itu `0 days`
17. Verifikasi Last Holder baris itu `—`
18. Verifikasi Reported Date baris itu tampil dalam Date Format `dd/MM/yy` dan Time Format `24h`

### Status global aset menjadi Damaged di Asset List
19. Buka tab `Assets` pada halaman Assets
20. Ganti isi kotak search dengan `Projector Epson EB-X06 {runId}`, tekan Enter
21. Verifikasi status global aset `Damaged` pada baris `Projector Epson EB-X06 {runId}`

### Banner, Damage Log, dan Transaction log di Asset Detail
22. Klik nama aset `Projector Epson EB-X06 {runId}` untuk membuka Asset Detail
23. Verifikasi banner `Damaged since [Date].` tampil
24. Verifikasi `[Date]` pada banner adalah tanggal Reported Date record dalam Date Format `dd/MM/yy`
25. Klik `[View]` pada banner
26. Verifikasi dialog `Damage Log` record aset itu tampil
27. Verifikasi `What happened` `Layar proyektor retak dan tidak menampilkan gambar` tampil pada node `Reported damaged by`
28. Verifikasi `Damaged Photo` tampil pada node `Reported damaged by`
29. Klik `✕` pada dialog Damage Log
30. Buka Transaction log pada Asset Detail
31. Verifikasi tepat satu entri `Reported damaged` tampil

### Report Damaged satu aset dari Asset Detail
32. Buka tab `Assets` pada halaman Assets
33. Ganti isi kotak search dengan `Printer HP LaserJet M404 {runId}`, tekan Enter
34. Klik nama aset `Printer HP LaserJet M404 {runId}` untuk membuka Asset Detail
35. Verifikasi aksi `Report Damaged` tersedia pada Asset Detail
36. Klik `[Report Damaged]` pada Asset Detail
37. Verifikasi dialog berjudul `Report Damaged` tampil dengan blok aset `Printer HP LaserJet M404 {runId}`
38. Isi `What happened` dengan `Kertas macet dan roller printer patah`
39. Unggah foto `printer-roller-patah.jpg` pada `Damaged Photo`
40. Klik `[Report Damaged]` pada footer dialog
41. Verifikasi toast `Success, asset has been reported damaged.` tampil
42. Verifikasi banner `Damaged since [Date].` tampil pada Asset Detail aset itu
43. Verifikasi status global aset `Damaged` tampil pada Asset Detail

### Aksi Report Damaged tidak ditawarkan untuk aset yang sudah punya record berjalan
44. Buka tab `Assets` pada halaman Assets
45. Ganti isi kotak search dengan `Monitor Dell P2422H {runId}`, tekan Enter
46. Verifikasi baris `Monitor Dell P2422H {runId}` tampil
47. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) untuk baris `Monitor Dell P2422H {runId}`

### Aksi Report Damaged tidak ditawarkan untuk aset Disposed
48. Ganti isi kotak search dengan `Scanner Fujitsu fi-7160 {runId}`, tekan Enter
49. Verifikasi baris `Scanner Fujitsu fi-7160 {runId}` tampil
50. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) untuk baris `Scanner Fujitsu fi-7160 {runId}`

### Aksi Report Damaged tidak ditawarkan untuk aset Missing
51. Ganti isi kotak search dengan `Drill Bosch GSB {runId}`, tekan Enter
52. Verifikasi baris `Drill Bosch GSB {runId}` tampil
53. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) untuk baris `Drill Bosch GSB {runId}`

### Banner Waiting for Confirmation di Asset Detail
54. Buka tab `Assets` pada halaman Assets
55. Ganti isi kotak search dengan `Headset Logitech H390 {runId}`, tekan Enter
56. Klik nama aset `Headset Logitech H390 {runId}` untuk membuka Asset Detail
57. Verifikasi banner `Damage reported on [Date]. Waiting for review.` tampil
58. Verifikasi `[Date]` pada banner adalah tanggal Reported Date record, yaitu `T0 − 3 hari`, dalam Date Format `dd/MM/yy`
59. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) pada Asset Detail aset itu

### Tanggal banner Damaged mengikuti Reported Date
60. Buka tab `Assets` pada halaman Assets
61. Ganti isi kotak search dengan `Monitor Dell P2422H {runId}`, tekan Enter
62. Klik nama aset `Monitor Dell P2422H {runId}` untuk membuka Asset Detail
63. Verifikasi banner `Damaged since [Date].` tampil
64. Verifikasi `[Date]` pada banner adalah tanggal Reported Date record, yaitu `T0 − 5 hari`, dalam Date Format `dd/MM/yy`
65. Verifikasi `[Date]` pada banner bukan tanggal Confirm `T0 − 2 hari` dan bukan tanggal node terbaru `T0 − 1 hari`
66. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) pada Asset Detail aset itu

### Banner Damaged untuk record Reported Disposal dan In Disposal Process
67. Buka tab `Assets` pada halaman Assets
68. Ganti isi kotak search dengan `Laptop Lenovo ThinkPad E14 {runId}`, tekan Enter
69. Klik nama aset `Laptop Lenovo ThinkPad E14 {runId}` untuk membuka Asset Detail
70. Verifikasi banner `Damaged since [Date].` tampil pada Asset Detail aset ber-record `Reported Disposal`
71. Buka tab `Assets` pada halaman Assets
72. Ganti isi kotak search dengan `Keyboard Logitech K380 {runId}`, tekan Enter
73. Klik nama aset `Keyboard Logitech K380 {runId}` untuk membuka Asset Detail
74. Verifikasi banner `Damaged since [Date].` tampil pada Asset Detail aset ber-record `In Disposal Process`
