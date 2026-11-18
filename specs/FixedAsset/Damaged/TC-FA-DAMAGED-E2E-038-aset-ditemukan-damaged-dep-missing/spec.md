---
id: TC-FA-DAMAGED-E2E-038-aset-ditemukan-damaged-dep-missing
title: "Mark as Found Damaged menambah node Asset found ke record yang ditahan tanpa record baru, dan membuat record Source Missing asset bagi aset tanpa record"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r74", "§Aturan Logika Modul#r75", "§Aturan Logika Modul#r49", "§8.1#r10", "§8.3#p2", "§8.3#r2", "§9.7#r4", EC-DMG-12, "§9.4.4#r31", "§9.2#b25"]
smoke: []
dependsOn: ["Missing: Mark as Found (Damaged)"]
trace:
  "§Aturan Logika Modul#r74": [11, 12, 16]
  "§Aturan Logika Modul#r75": [14, 23]
  "§Aturan Logika Modul#r49": [20, 21, 41, 42]
  "§8.1#r10": [19, 20, 22]
  "§8.3#p2": [20, 23, 24, 37, 40, 41]
  "§8.3#r2": 40
  "§9.7#r4": [11, 12, 13, 19, 37, 38]
  EC-DMG-12: [14, 19, 23]
  "§9.4.4#r31": 19
  "§9.2#b25": [12, 19]
anchor: []
coverage:
  web: automated
---

# Mark as Found Damaged menambah node Asset found ke record yang ditahan tanpa record baru, dan membuat record Source Missing asset bagi aset tanpa record

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Missing.
- Data:
  - DU-038-1: Damage record `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, What happened `Layar laptop retak dan tidak menyala`, Damaged Photo `laptop-layar-retak.jpg`, berpenanda `Missing`; aset berstatus Missing.
  - DU-038-2: Aset `Tablet Samsung Tab A8 {runId}`, Group `Head Office`, berstatus Missing, tanpa Damage record.
  - DU-038-3: Input Mark as Found untuk `Laptop Dell Latitude 5420 {runId}`: kondisi `Damaged`, Note `Ditemukan di gudang dengan bodi penyok`, Damaged Photo `laptop-ditemukan-penyok.jpg`.
  - DU-038-4: Input Mark as Found untuk `Tablet Samsung Tab A8 {runId}`: kondisi `Damaged`, Note `Ditemukan di ruang rapat dengan layar pecah`, Damaged Photo `tablet-ditemukan-pecah.jpg`.

## Test Steps

### Mark as Found Damaged atas aset dengan record yang ditahan menambah node tanpa record baru
1. Catat jumlah pada badge tab Damaged
2. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
3. Buka menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId}`
4. Klik `Mark as Found`
5. Pilih kondisi aset saat ditemukan `Damaged`
6. Isi Note `Ditemukan di gudang dengan bodi penyok`
7. Pilih Damaged Photo `laptop-ditemukan-penyok.jpg`
8. Kirim dialog Mark as Found
9. Buka tab Damaged, sub-tab Active
10. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
11. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berstatus `Damaged`
12. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tidak memuat penanda `Missing`
13. Verifikasi jumlah pada badge tab Damaged bertambah `1` dari jumlah yang dicatat
14. Verifikasi hasil Search memuat tepat `1` baris `Laptop Dell Latitude 5420 {runId}`
15. Buka menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId}`
16. Verifikasi menu baris `Laptop Dell Latitude 5420 {runId}` memuat aksi `Mark as Repaired`
17. Tutup menu ⋯
18. Klik nama aset `Laptop Dell Latitude 5420 {runId}` di kolom Name
19. Verifikasi dialog Damage Log memuat node `Asset found` dengan pelaku `System`
20. Verifikasi baris detail node `Asset found` memuat Note `Ditemukan di gudang dengan bodi penyok`
21. Verifikasi baris detail node `Asset found` memuat Damaged Photo `laptop-ditemukan-penyok.jpg`
22. Verifikasi baris detail node `Asset found` menyatakan record aktif kembali
23. Verifikasi dialog Damage Log memuat tepat `1` node `Reported damaged by`
24. Verifikasi What happened pada node `Reported damaged by` tetap `Layar laptop retak dan tidak menyala`
25. Tutup dialog Damage Log

### Mark as Found Damaged atas aset tanpa Damage record membuat record baru
26. Catat jumlah pada badge tab Damaged
27. Buka tab Missing
28. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
29. Buka menu ⋯ pada baris `Tablet Samsung Tab A8 {runId}`
30. Klik `Mark as Found`
31. Pilih kondisi aset saat ditemukan `Damaged`
32. Isi Note `Ditemukan di ruang rapat dengan layar pecah`
33. Pilih Damaged Photo `tablet-ditemukan-pecah.jpg`
34. Kirim dialog Mark as Found
35. Buka tab Damaged, sub-tab Active
36. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
37. Verifikasi baris `Tablet Samsung Tab A8 {runId}` tampil dengan Status `Damaged` dan Source `Missing asset`
38. Verifikasi jumlah pada badge tab Damaged bertambah `1` dari jumlah yang dicatat
39. Klik nama aset `Tablet Samsung Tab A8 {runId}` di kolom Name
40. Verifikasi dialog Damage Log memuat node `Reported damaged by` dengan pelaku aktor yang menjalankan Mark as Found
41. Verifikasi What happened pada node `Reported damaged by` adalah `Ditemukan di ruang rapat dengan layar pecah`
42. Verifikasi Damaged Photo pada node `Reported damaged by` adalah `tablet-ditemukan-pecah.jpg`
43. Tutup dialog Damage Log
