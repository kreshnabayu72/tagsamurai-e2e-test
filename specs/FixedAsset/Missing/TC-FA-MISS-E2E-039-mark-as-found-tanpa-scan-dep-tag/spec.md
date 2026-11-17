---
id: TC-FA-MISS-E2E-039-mark-as-found-tanpa-scan-dep-tag
title: "Mark as Found lewat I Can't Scan the TAG: dialog Report TAG, badge TAG Reported, Manual identification, dan toast marked as found"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r73", "§1.2#r74", "§1.2#r75", "§1.2#r76", "§1.2#r77", "§1.2#r78", "§1.2#r82", "§1.2#r83", "§1.2#r29", "§1.2#r65", "§4.2.4#r1", "§4.2.4#r2", "§4.2.4#r3", "§4.2.4#r17", "§4.2.4#p2", "§9.4.2#r9", "§9.4.2#r23", "§9.4.4#r10", "§4.3#r8", "§9.2#r5", "§9.9#r2", "§8.1#r14", "§8.2#b3", "§11#r11", "§3#p8", "§9.2#b24"]
smoke: []
dependsOn: ["Tag: dialog Report TAG (identifikasi manual)", "Tag: TAG Log"]
trace:
  "§1.2#r73": [6]
  "§1.2#r74": [8]
  "§1.2#r75": [12]
  "§1.2#r76": [16, 19]
  "§1.2#r77": [16]
  "§1.2#r78": [43, 45]
  "§1.2#r82": [19]
  "§1.2#r83": [26]
  "§1.2#r29": [19]
  "§1.2#r65": [19]
  "§4.2.4#r1": [8]
  "§4.2.4#r2": [12, 13, 37]
  "§4.2.4#r3": [39, 45]
  "§4.2.4#r17": [11, 12]
  "§4.2.4#p2": [4, 40]
  "§9.4.2#r9": [26]
  "§9.4.2#r23": [19]
  "§9.4.4#r10": [26]
  "§4.3#r8": [12, 39]
  "§9.2#r5": [19, 24]
  "§9.9#r2": [33]
  "§8.1#r14": [26]
  "§8.2#b3": [18, 46]
  "§11#r11": [18]
  "§3#p8": [16, 24]
  "§9.2#b24": [26]
anchor: []
coverage:
  web: automated
---

# Mark as Found lewat I Can't Scan the TAG: dialog Report TAG, badge TAG Reported, Manual identification, dan toast marked as found

## Prerequisites
- Aktor: Total Control `Rina W`, yang juga Aktor Missing.
- Layar awal: Assets > Missing > Active.
- Data:
  - DU-039-1: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Finance Room`, ber-TAG QR, dengan record Missing berstatus `Missing`.
  - DU-039-2: Asset `Hand Pallet Truck {runId}`, Group `Warehouse`, ber-TAG QR, dengan record Missing berstatus `Missing`.
  - DU-039-3: Reason Report TAG `TAG QR rusak terkena air`, Note `Ditemukan di laci meja kerja`.
  - DU-039-4: Reason Report TAG `TAG QR tergores sehingga tidak terbaca`, Note `Ditemukan di rak gudang belakang`.
  - DU-039-5: Pengguna `Rina W`, Total Control.
- Kondisi:
  - Akun `Rina W` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Mark as Found tanpa scan TAG lewat I Can't Scan the TAG
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
3. Klik `Mark as Found`
4. Verifikasi dialog `Mark as Found` memuat isian `Scan TAG`, `Found at`, `Asset Status`, `Photo`, dan `Note`
5. Klik `[Mark as Found]` pada dialog tanpa memverifikasi Scan TAG
6. Verifikasi caption `Scan TAG must not be empty` tampil di bawah isian Scan TAG
7. Klik `I Can't Scan the TAG`
8. Verifikasi dialog Report TAG varian identifikasi manual terbuka
9. Isi Reason Report TAG `TAG QR rusak terkena air`
10. Kirim dialog Report TAG
11. Verifikasi dialog `Mark as Found` terbuka kembali
12. Verifikasi badge `TAG Reported` tampil pada isian Scan TAG
13. Verifikasi tombol `[Scan TAG]` tetap aktif
14. Isi Note `Ditemukan di laci meja kerja`
15. Klik `[Mark as Found]` pada dialog
16. Verifikasi toast `Success, asset has been marked as found.` tampil
17. Buka TAG Log milik aset `Laptop Dell Latitude 5420 {runId}`
18. Verifikasi TAG Log memuat entri Report TAG dari jalur `I Can't Scan the TAG`
19. Verifikasi aset `Laptop Dell Latitude 5420 {runId}` tetap bertagging `Tag Reported` dan status global aset bukan `Available`
20. Buka halaman `Assets`
21. Klik tab `Missing`
22. Klik sub-tab `History`
23. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
24. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berstatus `Found`
25. Klik `Laptop Dell Latitude 5420 {runId}` pada kolom Name
26. Verifikasi dialog Missing Log memuat node `Marked as found by` oleh `Rina W` dengan Manual identification tercatat dan Asset Status `Normal`
27. Tutup dialog Missing Log dengan `✕`

### Scan berhasil sesudah Report TAG membatalkan Report TAG
28. Klik sub-tab `Active`
29. Ketik Search `Hand Pallet Truck {runId}`, tekan Enter
30. Buka menu `⋯` pada baris `Hand Pallet Truck {runId}`
31. Klik `Mark as Found`
32. Pindai TAG milik aset `Laptop Dell Latitude 5420 {runId}` melalui `[Scan TAG]`
33. Verifikasi pesan `This TAG doesn't belong to [Asset Name].` tampil dengan nama aset `Hand Pallet Truck {runId}`
34. Klik `I Can't Scan the TAG`
35. Isi Reason Report TAG `TAG QR tergores sehingga tidak terbaca`
36. Kirim dialog Report TAG
37. Verifikasi badge `TAG Reported` tampil pada isian Scan TAG
38. Pindai TAG milik aset `Hand Pallet Truck {runId}` melalui `[Scan TAG]`
39. Verifikasi badge `Verified` tampil pada isian Scan TAG
40. Verifikasi tautan `I Can't Scan the TAG` tidak tampil lagi pada isian Scan TAG
41. Isi Note `Ditemukan di rak gudang belakang`
42. Klik `[Mark as Found]` pada dialog
43. Verifikasi toast `Success, [Asset Name] is available again.` tampil dengan nama aset `Hand Pallet Truck {runId}`
44. Buka TAG Log milik aset `Hand Pallet Truck {runId}`
45. Verifikasi Report TAG aset `Hand Pallet Truck {runId}` berstatus `Canceled`
46. Verifikasi TAG Log milik aset `Hand Pallet Truck {runId}` tidak memuat entri untuk aksi Mark as Found
