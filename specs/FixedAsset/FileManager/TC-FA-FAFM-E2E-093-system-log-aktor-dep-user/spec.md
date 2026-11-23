---
id: TC-FA-FAFM-E2E-093-system-log-aktor-dep-user
title: "System Log di Detail User aktor memuat entri Delete dan Permanently Delete"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§8.2#p1"]
smoke: []
dependsOn: ["User: Detail User > Tab System Log"]
trace:
  "§8.2#p1": [13, 14, 16]
anchor: []
coverage:
  web: automated
---

# System Log di Detail User aktor memuat entri Delete dan Permanently Delete

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-093-1: Aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, ada di entitas aktor, memiliki foto aktif DU-093-2.
  - DU-093-2: File `syslog-{runId}.jpg`, Category `Asset Photo`, aktif, foto aset DU-093-1.
  - DU-093-3: File `syslog-purge-{runId}.png`, sudah dihapus permanen oleh auto-purge sebelum spec dijalankan, dengan Modified By `System` di Activity Log.

## Test Steps

### Delete dan Permanently Delete manual masuk System Log aktor, aktor System tidak
1. Klik tab `Asset Photo`
2. Ketik Search `syslog-{runId}.jpg`, tekan Enter
3. Klik aksi Delete pada baris file `syslog-{runId}.jpg`
4. Klik `[Delete]` pada dialog Delete File
5. Klik tombol Recycle Bin pada header kartu Storage Usage
6. Ketik Search `syslog-{runId}.jpg`, tekan Enter
7. Klik aksi Permanently Delete pada baris file `syslog-{runId}.jpg`
8. Klik `[Permanently Delete]` pada dialog Permanently Delete File
9. Tutup modal Recycle Bin
10. Buka Detail User milik aktor
11. Klik tab `System Log`
12. Ketik Search `syslog-{runId}.jpg`, tekan Enter
13. Verifikasi entri System Log dengan object `File Manager`, Field `File Name`, Name `syslog-{runId}.jpg`, dan Action `Delete` tampil
14. Verifikasi entri System Log dengan Name `syslog-{runId}.jpg` dan Action `Permanently Delete` tampil
15. Ganti isi kotak Search dengan `syslog-purge-{runId}.png`, tekan Enter
16. Verifikasi tidak ada entri System Log dengan Name `syslog-purge-{runId}.png`
