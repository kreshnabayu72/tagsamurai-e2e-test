---
id: TC-FA-DAMAGED-E2E-026-search-by-scan
title: "Search by Scan sub-tab Active mengisi Search tabel dengan Asset ID hasil pindai tanpa mini detail dan dengan filter aktif tetap berlaku"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-10, §4.1#r3, §4.1#p2, §4.2.1#b3, §4.4#r2, §5#r1, §9.1#r2]
smoke: []
dependsOn: []
trace:
  D-DMG-10: [4, 9, 10, 12, 30, 35, 36, 37]
  §4.1#r3: [4, 10, 30]
  §4.1#p2: [9, 10, 12, 24, 25, 26, 36, 37]
  §4.2.1#b3: [2, 9, 10, 16, 24, 25, 26]
  §4.4#r2: [4, 9, 10, 11, 16, 17]
  §5#r1: [2, 40, 41]
  §9.1#r2: [2, 11, 26]
anchor: []
coverage:
  web: manual
---

# Search by Scan sub-tab Active mengisi Search tabel dengan Asset ID hasil pindai tanpa mini detail dan dengan filter aktif tetap berlaku

## Prerequisites
- Aktor: Total Control (DU-026-10).
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-026-1: Damage record aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office {runId}` (DU-026-8), status `Damaged`, Source `Manual`, TAG RFID `RFID-{runId}-A` (DU-026-4), dilaporkan DU-026-10.
  - DU-026-2: Damage record aset `Tablet Samsung Tab A8 {runId}` di Group `Head Office {runId}`, status `Damaged`, Source `Manual`, TAG QR `QR-{runId}-B` (DU-026-5), dilaporkan DU-026-10.
  - DU-026-3: Damage record aset `Projector Epson EB-X06 {runId}` di Group `Warehouse {runId}` (DU-026-9), status `Damaged`, Source `Manual`, TAG RFID `RFID-{runId}-C` (DU-026-6), dilaporkan DU-026-10.
  - DU-026-4: TAG RFID `RFID-{runId}-A` terpasang pada aset `Laptop Dell Latitude 5420 {runId}`.
  - DU-026-5: TAG QR `QR-{runId}-B` terpasang pada aset `Tablet Samsung Tab A8 {runId}`.
  - DU-026-6: TAG RFID `RFID-{runId}-C` terpasang pada aset `Projector Epson EB-X06 {runId}`.
  - DU-026-7: TAG RFID `RFID-{runId}-N` terdaftar di perusahaan tetapi belum terpasang pada aset mana pun.
  - DU-026-8: Group `Head Office {runId}`.
  - DU-026-9: Group `Warehouse {runId}`.
  - DU-026-10: User `Agus Pratama {runId}`, role Total Control; cakupan: seluruh client.
  - DU-026-11: TAG RFID `RFID-{runId}-X` yang tidak terdaftar di perusahaan.
- Kondisi:
  - Perangkat pemindai TAG tersedia untuk memindai TAG DU-026-4 sampai DU-026-7 dan DU-026-11.
  - Plan entitas aktor bukan Starter, sehingga tipe TAG `RFID` terbuka untuk dipilih.

## Test Steps

### Search by Scan tersedia di toolbar sub-tab Active dan menawarkan pilihan tipe TAG
1. Klik ikon Search pada toolbar sub-tab Active
2. Verifikasi tombol `Search by Scan` tampil di dalam kotak Search sub-tab Active
3. Klik `Search by Scan`
4. Verifikasi overlay `Search by Scan` terbuka dengan pilihan `RFID` dan `QR`
5. Tekan Esc untuk menutup overlay

### Pindai TAG RFID milik aset mengisi Search dengan Asset ID tanpa mini detail
6. Klik `Search by Scan`
7. Pilih `RFID`
8. Pindai TAG `RFID-{runId}-A` milik aset `Laptop Dell Latitude 5420 {runId}`
9. Verifikasi overlay `Search by Scan` tertutup
10. Verifikasi kotak Search berisi Asset ID milik aset `Laptop Dell Latitude 5420 {runId}`
11. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` tampil di tabel
12. Verifikasi mini detail aset tidak tampil

### Pindai TAG QR milik aset mengisi Search dengan Asset ID
13. Klik `Search by Scan`
14. Pilih `QR`
15. Pindai TAG `QR-{runId}-B` milik aset `Tablet Samsung Tab A8 {runId}`
16. Verifikasi kotak Search berisi Asset ID milik aset `Tablet Samsung Tab A8 {runId}`
17. Verifikasi baris aset `Tablet Samsung Tab A8 {runId}` tampil di tabel

### Filter yang aktif tetap berlaku atas hasil pindai
18. Klik ikon Filter pada toolbar
19. Pada Filter Panel, pilih Group `Head Office {runId}`
20. Klik `[Apply]`
21. Klik `Search by Scan`
22. Pilih `RFID`
23. Pindai TAG `RFID-{runId}-C` milik aset `Projector Epson EB-X06 {runId}` di Group `Warehouse {runId}`
24. Verifikasi kotak Search berisi Asset ID milik aset `Projector Epson EB-X06 {runId}`
25. Verifikasi saringan Group `Head Office {runId}` masih aktif
26. Verifikasi sub-tab Active menampilkan `No results found` karena aset `Projector Epson EB-X06 {runId}` berada di luar saringan Group

### TAG tidak terdaftar ditolak dan TAG belum terpasang tidak menampilkan mini detail aset
27. Klik `Search by Scan`
28. Pilih `RFID`
29. Pindai TAG `RFID-{runId}-X` yang tidak terdaftar di perusahaan
30. Verifikasi error `Not recognize` tampil pada overlay `Search by Scan`
31. Tekan Esc untuk menutup overlay
32. Klik `Search by Scan`
33. Pilih `RFID`
34. Pindai TAG `RFID-{runId}-N` yang belum terpasang pada aset
35. Verifikasi tab `Damaged` sub-tab `Active` tetap tampil sesudah pemindaian TAG yang belum terpasang
36. Verifikasi mini detail aset tidak tampil pada hasil pindai TAG yang belum terpasang
37. Verifikasi Info TAG tidak tampil pada hasil pindai TAG yang belum terpasang

### History tidak menyediakan Search by Scan
38. Klik sub-tab `History`
39. Klik ikon Search pada toolbar sub-tab History
40. Verifikasi kotak Search tampil di toolbar sub-tab History
41. Verifikasi tombol `Search by Scan` tidak tampil di dalam kotak Search sub-tab History
