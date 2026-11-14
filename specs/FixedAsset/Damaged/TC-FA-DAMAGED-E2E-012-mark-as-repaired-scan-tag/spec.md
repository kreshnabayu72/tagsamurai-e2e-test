---
id: TC-FA-DAMAGED-E2E-012-mark-as-repaired-scan-tag
title: "Mark as Repaired atas aset ber-TAG mewajibkan Scan TAG: belum dipindai ditolak saat Submit, TAG aset lain ditolak saat scan, TAG milik aset lolos"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, D-DMG-02, §4.2.4#p2, FI-DMG-08, §9.9#r3, §9.4.4#r24, §8.1#r12, V-DMG-04, V-DMG-03]
smoke: [V-DMG-04, V-DMG-03]
dependsOn: []
trace:
  T-DMG-01: [2, 4, 45]
  D-DMG-02: [6, 23, 31, 40, 42, 45]
  §4.2.4#p2: 6
  FI-DMG-08: [6, 9, 10]
  §9.9#r3: [9, 13, 15, 23, 31, 40]
  §9.4.4#r24: 47
  §8.1#r12: 47
  V-DMG-04: 9
  V-DMG-03: [13, 15]
anchor: []
coverage:
  web: manual
---

# Mark as Repaired atas aset ber-TAG mewajibkan Scan TAG: belum dipindai ditolak saat Submit, TAG aset lain ditolak saat scan, TAG milik aset lolos

## Prerequisites
- Aktor: Total Control (DU-012-9).
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-012-1: Damage record aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office`, status `Damaged`, Source `Manual`, TAG RFID `RFID-{runId}-A` (DU-012-4), dilaporkan DU-012-9 dengan What happened `Layar laptop retak dan menampilkan garis`.
  - DU-012-2: Damage record aset `Tablet Samsung Tab A8 {runId}` di Group `Head Office`, status `Damaged`, Source `Manual`, TAG QR `QR-{runId}-B` (DU-012-5), dilaporkan DU-012-9.
  - DU-012-3: Damage record aset `Handheld Scanner Zebra TC21 {runId}` di Group `Head Office`, status `Damaged`, Source `Manual`, TAG NFC `NFC-{runId}-C` (DU-012-6), dilaporkan DU-012-9.
  - DU-012-4: TAG RFID `RFID-{runId}-A` terpasang pada aset `Laptop Dell Latitude 5420 {runId}`.
  - DU-012-5: TAG QR `QR-{runId}-B` terpasang pada aset `Tablet Samsung Tab A8 {runId}`.
  - DU-012-6: TAG NFC `NFC-{runId}-C` terpasang pada aset `Handheld Scanner Zebra TC21 {runId}`.
  - DU-012-7: TAG RFID `RFID-{runId}-U` terpasang pada user DU-012-8.
  - DU-012-8: User `Sinta Maharani {runId}`, pemegang TAG DU-012-7, tanpa hak Aktor Damaged; cakupan: aset yang ia pegang.
  - DU-012-9: User `Agus Pratama {runId}`, role Total Control; cakupan: seluruh client.
- Kondisi: Perangkat pemindai TAG tersedia untuk memindai TAG DU-012-4 sampai DU-012-7.

## Test Steps

### Submit tanpa Scan TAG ditolak dan TAG bukan milik aset ditolak saat scan
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` tampil di tabel dengan status `Damaged`
3. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
4. Verifikasi item `Mark as Repaired` tampil pada menu baris
5. Klik `Mark as Repaired`
6. Verifikasi dialog `Mark as Repaired` terbuka untuk aset `Laptop Dell Latitude 5420 {runId}` dengan field `Scan TAG*`
7. Isi Repair note `Layar laptop diganti baru dan unit sudah diuji menyala normal`
8. Klik `[Mark as Repaired]` pada dialog `Mark as Repaired`
9. Verifikasi pesan `Scan TAG must not be empty` tampil pada field Scan TAG
10. Verifikasi dialog `Mark as Repaired` tetap terbuka
11. Klik `[Scan TAG]`
12. Pindai TAG `QR-{runId}-B` yang terpasang pada aset `Tablet Samsung Tab A8 {runId}`
13. Verifikasi pesan `This TAG doesn't belong to [Asset Name].` tampil dengan `[Asset Name]` berisi nama aset `Laptop Dell Latitude 5420 {runId}`
14. Pindai TAG `RFID-{runId}-U` yang terpasang pada user `Sinta Maharani {runId}`
15. Verifikasi pesan `This TAG doesn't belong to [Asset Name].` tampil dengan `[Asset Name]` berisi nama aset `Laptop Dell Latitude 5420 {runId}` untuk TAG milik user lain
16. Klik `✕` pada dialog `Mark as Repaired`
17. Klik `[Leave]` pada dialog Unsaved Changes

### TAG QR dan NFC milik aset terverifikasi saat dipindai
18. Ganti isi kotak search dengan `Tablet Samsung Tab A8 {runId}`, tekan Enter
19. Klik `⋯` pada baris `Tablet Samsung Tab A8 {runId}`
20. Klik `Mark as Repaired`
21. Klik `[Scan TAG]`
22. Pindai TAG `QR-{runId}-B` milik aset `Tablet Samsung Tab A8 {runId}`
23. Verifikasi badge Verification pada field Scan TAG menyatakan TAG terverifikasi
24. Klik `✕` pada dialog `Mark as Repaired`
25. Klik `[Leave]` pada dialog Unsaved Changes
26. Ganti isi kotak search dengan `Handheld Scanner Zebra TC21 {runId}`, tekan Enter
27. Klik `⋯` pada baris `Handheld Scanner Zebra TC21 {runId}`
28. Klik `Mark as Repaired`
29. Klik `[Scan TAG]`
30. Pindai TAG `NFC-{runId}-C` milik aset `Handheld Scanner Zebra TC21 {runId}`
31. Verifikasi badge Verification pada field Scan TAG menyatakan TAG terverifikasi untuk TAG NFC
32. Klik `✕` pada dialog `Mark as Repaired`
33. Klik `[Leave]` pada dialog Unsaved Changes

### TAG milik aset lolos dan record menjadi Repaired
34. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
35. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
36. Klik `Mark as Repaired`
37. Isi Repair note `Layar laptop diganti baru dan unit sudah diuji menyala normal`
38. Klik `[Scan TAG]`
39. Pindai TAG `RFID-{runId}-A` milik aset `Laptop Dell Latitude 5420 {runId}`
40. Verifikasi badge Verification pada field Scan TAG menyatakan TAG terverifikasi untuk TAG RFID
41. Klik `[Mark as Repaired]` pada dialog `Mark as Repaired`
42. Verifikasi dialog `Mark as Repaired` tidak lagi tampil
43. Klik sub-tab `History`
44. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
45. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` tampil di tabel History dengan status `Repaired`
46. Klik nama aset `Laptop Dell Latitude 5420 {runId}` pada kolom Name
47. Verifikasi timeline memuat tepat satu node `Marked as repaired by` dengan aktor yang sedang masuk sebagai pelaku
48. Klik `✕` pada dialog `Damage Log`
