---
id: TC-FA-DAMAGED-E2E-037-report-missing-dep-missing
title: "Report Missing dari tab Damaged atas record Damaged menahan record dengan penanda Missing: hanya Damage Log tersedia, checkbox Disabled, dan node Asset reported missing"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, "§4.1#r8", "§4.2.4#p11", "§4.2.4#r6", "§4.4#r8", S-DMG-04, V-DMG-02, S-DMG-02, "§8.1#r10", "§8.3#r3", "§Aturan Logika Modul#r66", "§Aturan Logika Modul#r68", "§Aturan Logika Modul#r69", "§Aturan Logika Modul#r70", "§Aturan Logika Modul#r71", "§Aturan Logika Modul#r73", "§9.4.2#r11", "§9.4.2#r22", "§9.4.4#r31", "§9.7#r15", "§9.1#r8", "§2.1#r7", "§4.8#r5", "§9.2#b25", "§4.1#p3"]
smoke: []
dependsOn: ["Missing: dialog Report Missing (D-MIS-01)"]
trace:
  T-DMG-01: [5, 14, 21]
  "§4.1#r8": 7
  "§4.2.4#p11": [9, 10]
  "§4.2.4#r6": 7
  "§4.4#r8": [7, 11]
  S-DMG-04: [18, 19, 20]
  V-DMG-02: [18, 19, 20, 21]
  S-DMG-02: [11, 23]
  "§8.1#r10": [25, 26]
  "§8.3#r3": [25, 26]
  "§Aturan Logika Modul#r66": 9
  "§Aturan Logika Modul#r68": 29
  "§Aturan Logika Modul#r69": [11, 17]
  "§Aturan Logika Modul#r70": 23
  "§Aturan Logika Modul#r71": 11
  "§Aturan Logika Modul#r73": [17, 18, 19, 20]
  "§9.4.2#r11": [11, 17, 18, 19, 20]
  "§9.4.2#r22": [7, 9, 11]
  "§9.4.4#r31": 25
  "§9.7#r15": [11, 12]
  "§9.1#r8": [11, 17]
  "§2.1#r7": [5, 9]
  "§4.8#r5": [5, 14]
  "§9.2#b25": [25, 26]
  "§4.1#p3": [2, 11, 22, 23]
anchor: []
coverage:
  web: automated
---

# Report Missing dari tab Damaged atas record Damaged menahan record dengan penanda Missing: hanya Damage Log tersedia, checkbox Disabled, dan node Asset reported missing

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Damaged > Active.
- Data:
  - DU-037-1: Damage record `Camera Canon EOS {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, What happened `Lensa retak setelah jatuh dari rak penyimpanan`, Damaged Photo `kamera-lensa-retak.jpg`, tanpa penanda Missing.
  - DU-037-2: Damage record `Drill Bosch GSB {runId}`, Group `Warehouse`, Status `Damaged`, Source `Manual`, dengan penanda `Reported Missing`.
  - DU-037-3: Damage record `Projector Epson EB-X06 {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, tanpa penanda Missing.
- Kondisi:
  - Laporan Missing pemegang atas `Drill Bosch GSB {runId}` masih Waiting for Confirmation.

## Test Steps

### Report Missing atas record Damaged membuka dialog Report Missing dan menahan record
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Camera Canon EOS {runId}` berstatus `Damaged` tanpa penanda Missing
3. Catat jumlah pada badge tab Damaged
4. Buka menu ⋯ pada baris `Camera Canon EOS {runId}`
5. Verifikasi menu memuat aksi `Report Missing`
6. Klik `Report Missing`
7. Verifikasi dialog Report Missing terbuka dengan aset `Camera Canon EOS {runId}`, What happened `Lensa retak setelah jatuh dari rak penyimpanan`, dan Damaged Photo `kamera-lensa-retak.jpg` sudah terisi
8. Kirim dialog Report Missing
9. Verifikasi toast `Success, asset has been reported missing.` tampil
10. Verifikasi dialog Report Missing tertutup dan tampilan kembali ke sub-tab Active
11. Verifikasi baris `Camera Canon EOS {runId}` tetap berstatus `Damaged` dan memuat penanda `Missing` di samping badge status
12. Verifikasi jumlah pada badge tab Damaged berkurang `1` dari jumlah yang dicatat

### Selama ditahan hanya Damage Log yang tersedia
13. Buka menu ⋯ pada baris `Projector Epson EB-X06 {runId}`
14. Verifikasi menu memuat aksi `Mark as Repaired` dan `Report Missing`
15. Tutup menu ⋯
16. Buka menu ⋯ pada baris `Camera Canon EOS {runId}`
17. Verifikasi menu memuat aksi `Damage Log`
18. Verifikasi aksi `Mark as Repaired` Hidden pada menu baris `Camera Canon EOS {runId}`
19. Verifikasi aksi `Report Missing` Hidden pada menu baris `Camera Canon EOS {runId}`
20. Verifikasi aksi `Report Disposal` Hidden pada menu baris `Camera Canon EOS {runId}`
21. Verifikasi checkbox baris `Camera Canon EOS {runId}` Disabled

### Penanda Reported Missing pada record awal
22. Verifikasi baris `Drill Bosch GSB {runId}` berstatus `Damaged`
23. Verifikasi baris `Drill Bosch GSB {runId}` memuat penanda `Reported Missing` di samping badge status

### Node Asset reported missing di Damage Log
24. Klik nama aset `Camera Canon EOS {runId}` di kolom Name
25. Verifikasi dialog Damage Log memuat node `Asset reported missing` dengan pelaku `System`
26. Verifikasi baris detail node `Asset reported missing` menyatakan record ditahan
27. Tutup dialog Damage Log

### Status global aset Damaged + Missing
28. Buka Asset Detail aset `Camera Canon EOS {runId}`
29. Verifikasi status global aset `Damaged + Missing`
