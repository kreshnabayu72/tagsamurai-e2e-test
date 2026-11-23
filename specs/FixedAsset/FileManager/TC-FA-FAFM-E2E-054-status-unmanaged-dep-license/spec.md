---
id: TC-FA-FAFM-E2E-054-status-unmanaged-dep-license
title: "Aset Unmanaged karena lisensi masuk dan keluar tab Asset Data"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [DIM-02c, EC-18, F-FAFM-07.k1, F-FAFM-07.k3, F-FAFM-07c, F-FAFM-07i, SYN-08a, SYN-08b, SYN-08c]
smoke: []
dependsOn: ["License: status Unmanaged aset"]
trace:
  DIM-02c: [3, 13, 17]
  EC-18: [8, 13, 17]
  F-FAFM-07.k1: 13
  F-FAFM-07.k3: 23
  F-FAFM-07c: 14
  F-FAFM-07i: [23, 26]
  SYN-08a: [13, 23]
  SYN-08b: 13
  SYN-08c: [13, 23]
anchor: [7, 22]
coverage:
  web: automated
---

# Aset Unmanaged karena lisensi masuk dan keluar tab Asset Data

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-054-1: Aset `Scanner Epson DS-530 {runId}`, Status `Active`, Group `Branch Bandung`, ada di entitas aktor, memiliki satu file aktif DU-054-2.
  - DU-054-2: File `unmanaged-scan-{runId}.jpg`, Category `Asset Photo`, aktif, milik aset DU-054-1.
  - DU-054-3: Aset `Monitor LG 24 {runId}`, Status `Unmanaged`, Group `Head Office`, ada di entitas aktor.

## Test Steps

### Aset Active belum tampil di tab Asset Data
1. Klik tab `Asset Photo`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris file `unmanaged-scan-{runId}.jpg` tampil dengan Asset `Scanner Epson DS-530 {runId}`
4. Catat nilai Size baris file `unmanaged-scan-{runId}.jpg`
5. Klik tab `Disposed & Unmanaged Assets`
6. Ketik Search `{runId}`, tekan Enter
7. Verifikasi baris aset `Monitor LG 24 {runId}` tampil dengan Status `Unmanaged`
8. Verifikasi tidak ada baris aset `Scanner Epson DS-530 {runId}`

### Aset menjadi Unmanaged karena lisensi tampil di tab Asset Data dengan ukurannya
9. Ubah status lisensi aset `Scanner Epson DS-530 {runId}` menjadi Unmanaged
10. Muat ulang halaman
11. Klik tab `Disposed & Unmanaged Assets`
12. Ketik Search `Scanner Epson DS-530 {runId}`, tekan Enter
13. Verifikasi baris aset `Scanner Epson DS-530 {runId}` tampil dengan Status `Unmanaged`
14. Verifikasi nilai Files Size baris aset `Scanner Epson DS-530 {runId}` sama dengan nilai Size yang dicatat pada langkah 4
15. Klik tab `Asset Photo`
16. Ketik Search `unmanaged-scan-{runId}.jpg`, tekan Enter
17. Verifikasi baris file `unmanaged-scan-{runId}.jpg` tetap tampil dengan Asset `Scanner Epson DS-530 {runId}`

### Aset kembali Active keluar dari tab Asset Data
18. Ubah status lisensi aset `Scanner Epson DS-530 {runId}` menjadi Active
19. Muat ulang halaman
20. Klik tab `Disposed & Unmanaged Assets`
21. Ketik Search `{runId}`, tekan Enter
22. Verifikasi baris aset `Monitor LG 24 {runId}` tampil dengan Status `Unmanaged`
23. Verifikasi tidak ada baris aset `Scanner Epson DS-530 {runId}`
24. Klik tab `Asset Photo`
25. Ketik Search `unmanaged-scan-{runId}.jpg`, tekan Enter
26. Verifikasi baris file `unmanaged-scan-{runId}.jpg` tampil dengan Asset `Scanner Epson DS-530 {runId}`
