---
id: TC-FA-DAMAGED-E2E-044-record-kembali-damaged-dari-tab-reported-dep-disposal
title: "Decline Report atau Cancel Report di tab Reported mengembalikan record ke Damaged dengan node Disposal report declined by / canceled by"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r20", "§Aturan Logika Modul#r63", "§8.1#r14", "§8.1#r15", "§8.3#r4", "§9.4.2#r14", "§9.4.4#r26", "§9.7#r11"]
smoke: []
dependsOn:
  - "Disposal: tab Reported (Decline, Cancel Report)"
trace:
  "§Aturan Logika Modul#r63": [5, 25]
  "§Aturan Logika Modul#r20": [11, 14, 31, 34]
  "§9.4.2#r14": [11, 17, 31, 37]
  "§9.4.4#r26": [11, 17, 31, 37]
  "§9.7#r11": [11, 12, 14, 31, 32, 34]
  "§8.1#r14": [17, 18, 19]
  "§8.3#r4": [17, 37]
  "§8.1#r15": [37, 38, 39]
anchor: []
coverage:
  web: automated
---

# Decline Report atau Cancel Report di tab Reported mengembalikan record ke Damaged dengan node Disposal report declined by / canceled by

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Damaged > Active.
- Data:
  - DU-044-1: Damage record `Printer HP LaserJet M404 {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
  - DU-044-2: Damage record `Monitor Dell P2422H {runId}`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`.
  - DU-044-3: Input Decline Report atas `Printer HP LaserJet M404 {runId}`: Reason `Aset masih dapat diperbaiki oleh teknisi internal`.
  - DU-044-4: Input Cancel Report atas `Monitor Dell P2422H {runId}`: Reason `Pelaporan dibatalkan karena monitor sudah diperbaiki`.
- Kondisi:
  - Level Feature Suite Disposal bernilai `Basic`.

## Test Steps

### Decline Report di tab Reported mengembalikan record ke Damaged
1. Catat jumlah pada badge tab Damaged
2. Buka Transactions > Disposal, tab Reported
3. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
4. Buka menu ⋯ pada Disposal Report aset `Printer HP LaserJet M404 {runId}` di tab Reported
5. Verifikasi menu Disposal Report aset `Printer HP LaserJet M404 {runId}` memuat aksi `Decline`
6. Klik `Decline`
7. Isi Reason `Aset masih dapat diperbaiki oleh teknisi internal`
8. Kirim dialog Decline Report
9. Buka Assets > Damaged > Active
10. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
11. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Damaged`
12. Verifikasi jumlah pada badge tab Damaged bertambah `1` dari jumlah yang dicatat
13. Buka menu ⋯ pada baris `Printer HP LaserJet M404 {runId}`
14. Verifikasi menu baris `Printer HP LaserJet M404 {runId}` memuat aksi `Mark as Repaired`
15. Tutup menu ⋯
16. Klik nama aset `Printer HP LaserJet M404 {runId}` di kolom Name
17. Verifikasi dialog Damage Log memuat node `Disposal report declined by` dengan pelaku aktor yang menjalankan Decline
18. Verifikasi baris detail node `Disposal report declined by` memuat Reason `Aset masih dapat diperbaiki oleh teknisi internal`
19. Verifikasi baris detail node `Disposal report declined by` memuat `Report ID` dan `Back to Damaged`
20. Tutup dialog Damage Log

### Cancel Report di tab Reported mengembalikan record ke Damaged
21. Catat jumlah pada badge tab Damaged
22. Buka Transactions > Disposal, tab Reported
23. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
24. Buka menu ⋯ pada Disposal Report aset `Monitor Dell P2422H {runId}` di tab Reported
25. Verifikasi menu Disposal Report aset `Monitor Dell P2422H {runId}` memuat aksi `Cancel Report`
26. Klik `Cancel Report`
27. Isi Reason `Pelaporan dibatalkan karena monitor sudah diperbaiki`
28. Kirim dialog Cancel Report
29. Buka Assets > Damaged > Active
30. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
31. Verifikasi baris `Monitor Dell P2422H {runId}` berstatus `Damaged`
32. Verifikasi jumlah pada badge tab Damaged bertambah `1` dari jumlah yang dicatat
33. Buka menu ⋯ pada baris `Monitor Dell P2422H {runId}`
34. Verifikasi menu baris `Monitor Dell P2422H {runId}` memuat aksi `Mark as Repaired`
35. Tutup menu ⋯
36. Klik nama aset `Monitor Dell P2422H {runId}` di kolom Name
37. Verifikasi dialog Damage Log memuat node `Disposal report canceled by` dengan pelaku aktor yang menjalankan Cancel Report
38. Verifikasi baris detail node `Disposal report canceled by` memuat Reason `Pelaporan dibatalkan karena monitor sudah diperbaiki`
39. Verifikasi baris detail node `Disposal report canceled by` memuat `Report ID` dan `Back to Damaged`
40. Tutup dialog Damage Log
