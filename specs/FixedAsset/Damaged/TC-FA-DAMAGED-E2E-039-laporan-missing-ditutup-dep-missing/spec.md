---
id: TC-FA-DAMAGED-E2E-039-laporan-missing-ditutup-dep-missing
title: "Reject atau Cancel Report laporan Missing menghapus penanda, mengaktifkan record kembali, dan menambah node Missing report closed"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r69", "§8.1#r11", "§8.3#r3", EC-DMG-33, "§9.4.4#r32", "§9.7#r15"]
smoke: []
dependsOn: ["Missing: Reject dan Cancel Report laporan Missing"]
trace:
  "§Aturan Logika Modul#r69": [9, 10, 13, 25, 26, 29]
  "§8.1#r11": [16, 17, 32]
  "§8.3#r3": [16, 32]
  EC-DMG-33: [10, 13, 16, 26, 32]
  "§9.4.4#r32": [16, 32]
  "§9.7#r15": [9, 10, 11, 20, 25, 26, 27]
anchor: [2]
coverage:
  web: automated
---

# Reject atau Cancel Report laporan Missing menghapus penanda, mengaktifkan record kembali, dan menambah node Missing report closed

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Damaged > Active.
- Data:
  - DU-039-1: Damage record `Camera Canon EOS {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, berpenanda `Reported Missing`.
  - DU-039-2: Damage record `Drill Bosch GSB {runId}`, Group `Warehouse`, Status `Damaged`, Source `Manual`, berpenanda `Reported Missing`.
  - DU-039-3: Input Reject laporan Missing atas `Camera Canon EOS {runId}`: Reason `Aset masih berada di gudang pusat`.
- Kondisi:
  - Laporan Missing pemegang atas `Camera Canon EOS {runId}` dan `Drill Bosch GSB {runId}` masih Waiting for Confirmation.

## Test Steps

### Reject laporan Missing menghapus penanda dan mengaktifkan record kembali
1. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
2. Verifikasi baris `Camera Canon EOS {runId}` berstatus `Damaged` dengan penanda `Reported Missing`
3. Catat jumlah pada badge tab Damaged
4. Buka tab Missing
5. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
6. Reject laporan Missing atas aset `Camera Canon EOS {runId}` dengan Reason `Aset masih berada di gudang pusat`
7. Buka tab Damaged, sub-tab Active
8. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
9. Verifikasi baris `Camera Canon EOS {runId}` berstatus `Damaged`
10. Verifikasi baris `Camera Canon EOS {runId}` tidak memuat penanda Missing
11. Verifikasi jumlah pada badge tab Damaged bertambah `1` dari jumlah yang dicatat
12. Buka menu ⋯ pada baris `Camera Canon EOS {runId}`
13. Verifikasi menu baris `Camera Canon EOS {runId}` memuat aksi `Mark as Repaired`
14. Tutup menu ⋯
15. Klik nama aset `Camera Canon EOS {runId}` di kolom Name
16. Verifikasi dialog Damage Log memuat node `Missing report closed` dengan pelaku `System`
17. Verifikasi baris detail node `Missing report closed` menyatakan penanda Missing hilang dan record aktif kembali
18. Tutup dialog Damage Log

### Cancel Report oleh pemegang menghapus penanda dan mengaktifkan record kembali
19. Ganti isi kotak search dengan `Drill Bosch GSB {runId}`, tekan Enter
20. Verifikasi baris `Drill Bosch GSB {runId}` berstatus `Damaged` dengan penanda `Reported Missing`
21. Catat jumlah pada badge tab Damaged
22. Pemegang aset `Drill Bosch GSB {runId}` membatalkan laporan Missing dengan Cancel Report
23. Muat ulang halaman
24. Ketik Search `Drill Bosch GSB {runId}`, tekan Enter
25. Verifikasi baris `Drill Bosch GSB {runId}` berstatus `Damaged`
26. Verifikasi baris `Drill Bosch GSB {runId}` tidak memuat penanda Missing
27. Verifikasi jumlah pada badge tab Damaged bertambah `1` dari jumlah yang dicatat
28. Buka menu ⋯ pada baris `Drill Bosch GSB {runId}`
29. Verifikasi menu baris `Drill Bosch GSB {runId}` memuat aksi `Mark as Repaired`
30. Tutup menu ⋯
31. Klik nama aset `Drill Bosch GSB {runId}` di kolom Name
32. Verifikasi dialog Damage Log memuat node `Missing report closed` dengan pelaku `System`
33. Tutup dialog Damage Log
