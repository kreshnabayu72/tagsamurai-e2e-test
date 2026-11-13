---
id: TC-FA-FAREG-BE-124-validasi-scan-tag
title: "Validasi scan Tag per status dan tipe"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: [F-FAREG-02.k1, V-REG-05, V-REG-06, V-REG-07, V-REG-08, V-REG-09, "§9.4.2#r28", "§9.4.2#r32", "§9.4.2#r33", "§9.4.2#r34", "§9.4.2#r35", "§9.4.2#r36", "§9.4.2#r37", "§9.4.2#r38", "§9.4.2#r39", "§9.4.2#r40", "§9.4.2#r41", "§9.9#r12"]
smoke: []
dependsOn: []
trace:
  F-FAREG-02.k1: [17, 19, 21, 23, 25, 27, 29, 36]
  V-REG-05: [10, 12, 14]
  V-REG-06: [17, 19, 21, 23, 25, 27, 29, 47]
  V-REG-07: [32, 34]
  V-REG-08: [38]
  V-REG-09: [36]
  "§9.4.2#r28": [17, 19, 30]
  "§9.4.2#r32": [38, 39]
  "§9.4.2#r33": [10, 12, 14, 15]
  "§9.4.2#r34": [17, 30]
  "§9.4.2#r35": [19]
  "§9.4.2#r36": [21, 23, 25, 27]
  "§9.4.2#r37": [44, 47]
  "§9.4.2#r38": [29]
  "§9.4.2#r39": [32, 34]
  "§9.4.2#r40": [36]
  "§9.4.2#r41": [41, 42]
  "§9.9#r12": [2, 4, 6, 8]
owner: BE
---

# Validasi scan Tag per status dan tipe

## Prerequisites
- Aktor: Rina (Manage asset & TAG, Group terkelola `Gudang Makassar {runId}` saja); Dewi (Manage asset & TAG, Group terkelola `Gudang Manado {runId}` saja).
- Data:
  - DU-124-1: Group `Gudang Makassar {runId}`, Assignable, di entitas aktor.
  - DU-124-2: Group `Gudang Manado {runId}`, Assignable, di entitas aktor.
  - DU-124-3: Asset Name `Perangkat Survei {runId}`, Category `Peralatan Lapangan`, Brand `Trimble`, Model `R12i`, TAG Type `RFID`, `QR`, dan `NFC` (tiga slot Tag).
  - DU-124-4: Asset Name `Laptop {runId}`, Category `IT Equipment`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`.
  - DU-124-5: batch Draft milik Rina, Group `Gudang Makassar {runId}`, satu Item `Perangkat Survei {runId}` Quantity `2`, seluruh slot Tag kedua aset kosong.
  - DU-124-6: batch Draft milik Dewi, Group `Gudang Manado {runId}`, satu Item `Laptop {runId}` Quantity `1`, slot Tag RFID kosong.
  - DU-124-7: Tag RFID `E280-1240-0001 {runId}`, status `Available`.
  - DU-124-8: Tag QR `QR-1240-0001 {runId}`, status `Available`.
  - DU-124-9: Tag NFC `NFC-1240-0001 {runId}`, status `Available`.
  - DU-124-10: Tag RFID `E280-1240-0002 {runId}`, status `Available`.
  - DU-124-11: Tag RFID `E280-1240-0003 {runId}`, status `To be Returned`, Return Group `Gudang Makassar {runId}`.
  - DU-124-12: Tag RFID `E280-1240-0011 {runId}`, status `Paired` di aset Active `Server Rack Lama {runId}`.
  - DU-124-13: Tag RFID `E280-1240-0012 {runId}`, status `Reserved` oleh batch Draft Dewi.
  - DU-124-14: Tag RFID `E280-1240-0013 {runId}`, status `Retired`.
  - DU-124-15: Tag RFID `E280-1240-0014 {runId}`, status `Damaged`.
  - DU-124-16: Tag RFID `E280-1240-0015 {runId}`, status `Missing`.
  - DU-124-17: Tag RFID `E280-1240-0016 {runId}`, status `Waiting for Approval`.
  - DU-124-18: Tag RFID `E280-1240-0017 {runId}`, status `To be Returned`, Return Group `Gudang Manado {runId}`.
  - DU-124-19: Tag user `USR-1240-0001 {runId}`, status `Paired` pada pengguna `Agus Pratama`.
  - DU-124-20: Tag produk lain `SUP-1240-0001 {runId}` milik produk `Supply Asset`.
- Kondisi:
  - Approval Workflow tidak aktif untuk `Gudang Makassar {runId}`.

## Test Steps

### Tag Available per jenis diterima dan tersimpan
1. Rina memindai Tag RFID `E280-1240-0001 {runId}` pada slot RFID aset pertama batch DU-124-5
2. Verifikasi pemindaian diterima dan slot RFID aset pertama berstatus `Verified`
3. Rina memindai Tag QR `QR-1240-0001 {runId}` pada slot QR aset pertama batch DU-124-5
4. Verifikasi pemindaian diterima dan slot QR aset pertama berstatus `Verified`
5. Rina memindai Tag NFC `NFC-1240-0001 {runId}` pada slot NFC aset pertama batch DU-124-5
6. Verifikasi pemindaian diterima dan slot NFC aset pertama berstatus `Verified`
7. Rina mengirim Save draft atas batch DU-124-5
8. Verifikasi ketiga slot Tag aset pertama tetap `Verified` sesudah Save draft

### Tag tidak dikenal ditolak
9. Rina memindai Tag RFID `E280-1240-9999 {runId}` yang tidak terdaftar di registri Global pada slot RFID aset kedua batch DU-124-5
10. Verifikasi pemindaian ditolak dengan pesan `Error, can't recognize TAG.`
11. Rina memindai kode barcode `8991234567890` yang bukan TAG Samurai pada slot RFID aset kedua batch DU-124-5
12. Verifikasi pemindaian ditolak dengan pesan `Error, can't recognize TAG.`
13. Rina memindai Tag QR `QR-1240-0099 {runId}` yang belum diaktivasi di Global pada slot QR aset kedua batch DU-124-5
14. Verifikasi pemindaian ditolak dengan pesan `Error, can't recognize TAG.`
15. Verifikasi slot RFID dan slot QR aset kedua berstatus `Unverified`

### Tag berstatus selain Available dan To be Returned dalam cakupan ditolak
16. Rina memindai Tag RFID `E280-1240-0011 {runId}` pada slot RFID aset kedua batch DU-124-5
17. Verifikasi pemindaian ditolak dengan pesan yang memuat Tag `E280-1240-0011 {runId}` dan status `Paired`
18. Rina memindai Tag RFID `E280-1240-0012 {runId}` pada slot RFID aset kedua batch DU-124-5
19. Verifikasi pemindaian ditolak dengan pesan yang memuat Tag `E280-1240-0012 {runId}` dan status `Reserved`
20. Rina memindai Tag RFID `E280-1240-0013 {runId}` pada slot RFID aset kedua batch DU-124-5
21. Verifikasi pemindaian ditolak dengan pesan yang memuat Tag `E280-1240-0013 {runId}` dan status `Retired`
22. Rina memindai Tag RFID `E280-1240-0014 {runId}` pada slot RFID aset kedua batch DU-124-5
23. Verifikasi pemindaian ditolak dengan pesan yang memuat Tag `E280-1240-0014 {runId}` dan status `Damaged`
24. Rina memindai Tag RFID `E280-1240-0015 {runId}` pada slot RFID aset kedua batch DU-124-5
25. Verifikasi pemindaian ditolak dengan pesan yang memuat Tag `E280-1240-0015 {runId}` dan status `Missing`
26. Rina memindai Tag RFID `E280-1240-0016 {runId}` pada slot RFID aset kedua batch DU-124-5
27. Verifikasi pemindaian ditolak dengan pesan yang memuat Tag `E280-1240-0016 {runId}` dan status `Waiting for Approval`
28. Rina memindai Tag RFID `E280-1240-0017 {runId}` dengan Return Group di luar cakupannya pada slot RFID aset kedua batch DU-124-5
29. Verifikasi pemindaian ditolak dengan pesan yang memuat Tag `E280-1240-0017 {runId}` dan status `To be Returned`
30. Verifikasi slot RFID aset kedua tetap berstatus `Unverified` sesudah ketujuh penolakan

### Tag user dan Tag produk lain ditolak
31. Rina memindai Tag user `USR-1240-0001 {runId}` pada slot RFID aset kedua batch DU-124-5
32. Verifikasi pemindaian ditolak dengan pesan `This is a user TAG. Scan an asset TAG.`
33. Rina memindai Tag produk lain `SUP-1240-0001 {runId}` pada slot RFID aset kedua batch DU-124-5
34. Verifikasi pemindaian ditolak dengan pesan `This TAG is used by Supply Asset`

### Tag duplikat di form dan Rescan Tag yang sama ditolak
35. Rina memindai Tag RFID `E280-1240-0001 {runId}` pada slot RFID aset kedua batch DU-124-5
36. Verifikasi pemindaian ditolak dengan pesan `This TAG has already been scanned`
37. Rina memindai ulang Tag RFID `E280-1240-0001 {runId}` pada slot RFID aset pertama batch DU-124-5
38. Verifikasi pemindaian ditolak dengan pesan `This TAG is the same as the current TAG`
39. Verifikasi slot RFID aset pertama tetap berstatus `Verified` dengan Tag `E280-1240-0001 {runId}`

### Tag bertipe lain dari slot ditolak
40. Rina memindai Tag RFID `E280-1240-0002 {runId}` pada slot QR aset kedua batch DU-124-5
41. Verifikasi pemindaian ditolak dengan pesan `This slot needs a QR TAG`
42. Verifikasi slot QR aset kedua tetap berstatus `Unverified`

### Tag To be Returned dengan Return Group dalam cakupan diterima
43. Rina memindai Tag RFID `E280-1240-0003 {runId}` pada slot RFID aset kedua batch DU-124-5
44. Verifikasi pemindaian diterima dan slot RFID aset kedua berstatus `Verified`
45. Rina mengirim Save draft atas batch DU-124-5
46. Dewi memindai Tag RFID `E280-1240-0003 {runId}` pada slot RFID aset pertama batch DU-124-6
47. Verifikasi pemindaian ditolak dengan pesan yang memuat Tag `E280-1240-0003 {runId}` dan status `Reserved`, bukan `To be Returned`
