---
id: TC-FA-FAFM-E2E-058-log-modul-sumber-dep-activity-log
title: "Entri Activity Log modul sumber dan aktor System"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ARS-01m, SYN-03i, "§8.1#b1", "§8.3#p1"]
smoke: []
dependsOn: ["Activity Log: log aset dan log modul sumber"]
trace:
  ARS-01m: 6
  SYN-03i: 36
  "§8.1#b1": [6, 7, 8, 9]
  "§8.3#p1": [13, 30, 31, 33, 34]
anchor: []
coverage:
  web: automated
---

# Entri Activity Log modul sumber dan aktor System

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-058-1: Aset `Printer HP M404 {runId}`, Group `Head Office`, ada di entitas aktor, memiliki foto aktif DU-058-2.
  - DU-058-2: File `log-single-{runId}.jpg`, Category `Asset Photo`, aktif, foto aset DU-058-1.
  - DU-058-3: Aset `Monitor LG 24 {runId}`, Group `Head Office`, ada di entitas aktor, memiliki foto aktif DU-058-4.
  - DU-058-4: File `log-bulk-a-{runId}.jpg`, Category `Asset Photo`, aktif, foto aset DU-058-3.
  - DU-058-5: Aset `Scanner Epson DS-530 {runId}`, Group `Head Office`, ada di entitas aktor, memiliki foto aktif DU-058-6.
  - DU-058-6: File `log-bulk-b-{runId}.jpg`, Category `Asset Photo`, aktif, foto aset DU-058-5.
  - DU-058-7: File `log-purge-{runId}.png`, sudah dihapus permanen oleh auto-purge sebelum spec dijalankan, sehingga Activity Log memuat entri dengan Modified By `System`.

## Test Steps

### Delete file yang dirujuk menulis entri pengosongan di log modul sumber
1. Klik tab `Asset Photo`
2. Ketik Search `log-single-{runId}.jpg`, tekan Enter
3. Klik aksi Delete pada baris file `log-single-{runId}.jpg`
4. Klik `[Delete]` pada dialog Delete File
5. Buka Changelog aset `Printer HP M404 {runId}`
6. Verifikasi entri dengan Action `Edit` dan Old Value `log-single-{runId}.jpg` tampil
7. Verifikasi entri tersebut menampilkan New Value `—`
8. Verifikasi entri tersebut menampilkan Modified By pengguna aktor
9. Verifikasi entri tersebut menampilkan Field `Photo`
10. Tutup Changelog aset

### Activity Log mencatat Delete satu file
11. Buka Activity Log
12. Ketik Search `log-single-{runId}.jpg`, tekan Enter
13. Verifikasi hasil Search memuat tepat satu entri Activity Log dengan object `File Manager`, Field `File Name`, Name `log-single-{runId}.jpg`, Action `Delete`, dan Modified By pengguna aktor tampil

### Bulk Delete dan bulk Permanently Delete menulis satu entri per file
14. Buka Settings > File Manager
15. Klik tab `Asset Photo`
16. Ketik Search `{runId}`, tekan Enter
17. Centang baris file `log-bulk-a-{runId}.jpg`
18. Centang baris file `log-bulk-b-{runId}.jpg`
19. Klik aksi bulk Delete
20. Klik `[Delete]` pada dialog Delete Files
21. Klik tombol Recycle Bin pada header kartu Storage Usage
22. Ketik Search `{runId}`, tekan Enter
23. Centang baris file `log-bulk-a-{runId}.jpg`
24. Centang baris file `log-bulk-b-{runId}.jpg`
25. Klik aksi bulk Permanently Delete
26. Klik `[Permanently Delete]` pada dialog Permanently Delete Files
27. Tutup modal Recycle Bin
28. Buka Activity Log
29. Ketik Search `log-bulk-a-{runId}.jpg`, tekan Enter
30. Verifikasi hasil Search memuat tepat satu entri Activity Log dengan Name `log-bulk-a-{runId}.jpg` dan Action `Delete`
31. Verifikasi hasil Search memuat tepat satu entri Activity Log dengan Name `log-bulk-a-{runId}.jpg` dan Action `Permanently Delete`
32. Ganti isi kotak Search dengan `log-bulk-b-{runId}.jpg`, tekan Enter
33. Verifikasi hasil Search memuat tepat satu entri Activity Log dengan Name `log-bulk-b-{runId}.jpg` dan Action `Delete`
34. Verifikasi hasil Search memuat tepat satu entri Activity Log dengan Name `log-bulk-b-{runId}.jpg` dan Action `Permanently Delete`

### Auto-purge ditulis dengan aktor System
35. Ganti isi kotak Search dengan `log-purge-{runId}.png`, tekan Enter
36. Verifikasi entri Activity Log dengan Name `log-purge-{runId}.png`, Action `Permanently Delete`, dan Modified By `System` tampil
