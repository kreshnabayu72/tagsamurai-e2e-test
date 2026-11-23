---
id: TC-FA-FAFM-E2E-055-retensi-recycle-bin-dep-lifecycle-settings
title: "Durasi retensi Lifecycle Settings tercermin di Recycle Bin"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [SYN-11a, SYN-11b, SYN-11c, SYN-11e, SYN-11g]
smoke: []
dependsOn: ["Plans & Licensing: Lifecycle Settings"]
trace:
  SYN-11a: 19
  SYN-11b: [6, 19, 29]
  SYN-11c: [8, 21]
  SYN-11e: [19, 29]
  SYN-11g: 22
anchor: []
coverage:
  web: automated
---

# Durasi retensi Lifecycle Settings tercermin di Recycle Bin

## Prerequisites
- Aktor: Total Control; aktor lain yang memicu perubahan: operator Admin Console, pemegang akses Plans & Licensing > Lifecycle Settings tab Recycle Bin, akun aktif dengan kredensial disediakan fase 2.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-055-1: Setting durasi retensi Recycle Bin di Plans & Licensing > Lifecycle Settings bernilai `30 hari` (nilai awal).
  - DU-055-2: Nilai durasi retensi pengganti `45 hari`, yang tampil sebagai `45 days` pada Auto-Purge In dan Info Recycle Bin.
  - DU-055-3: Aset `Printer HP M404 {runId}`, Group `Head Office`, ada di entitas aktor, memiliki dua file aktif DU-055-4 dan DU-055-5.
  - DU-055-4: File `retensi-before-{runId}.jpg`, Category `Asset Photo`, aktif, di-Delete sebelum durasi retensi diubah.
  - DU-055-5: File `retensi-after-{runId}.jpg`, Category `Asset Photo`, aktif, di-Delete sesudah durasi retensi diubah.

## Test Steps

### Info dan Auto-Purge In memakai durasi retensi awal
1. Klik tab `Asset Photo`
2. Ketik Search `retensi-before-{runId}.jpg`, tekan Enter
3. Klik aksi Delete pada baris file `retensi-before-{runId}.jpg`
4. Klik `[Delete]` pada dialog Delete File
5. Klik tombol Recycle Bin pada header kartu Storage Usage
6. Verifikasi Info Recycle Bin menampilkan `Files are permanently deleted after 30 days.`
7. Ketik Search `retensi-before-{runId}.jpg`, tekan Enter
8. Verifikasi baris file `retensi-before-{runId}.jpg` tampil dengan Auto-Purge In `30 days`
9. Tutup modal Recycle Bin

### Durasi retensi yang diubah tercermin pada pembukaan modal berikutnya
10. Operator Admin Console membuka Plans & Licensing > Lifecycle Settings, tab Recycle Bin
11. Operator Admin Console mengubah durasi retensi Recycle Bin menjadi `45` hari
12. Operator Admin Console menyimpan perubahan Lifecycle Settings
13. Buka Settings > File Manager
14. Klik tab `Asset Photo`
15. Ketik Search `retensi-after-{runId}.jpg`, tekan Enter
16. Klik aksi Delete pada baris file `retensi-after-{runId}.jpg`
17. Klik `[Delete]` pada dialog Delete File
18. Klik tombol Recycle Bin pada header kartu Storage Usage
19. Verifikasi Info Recycle Bin menampilkan `Files are permanently deleted after 45 days.`
20. Ketik Search `{runId}`, tekan Enter
21. Verifikasi baris file `retensi-after-{runId}.jpg` tampil dengan Auto-Purge In `45 days`
22. Verifikasi baris file `retensi-before-{runId}.jpg` tampil
23. Tutup modal Recycle Bin

### Durasi retensi dikembalikan ke nilai awal
24. Operator Admin Console membuka Plans & Licensing > Lifecycle Settings, tab Recycle Bin
25. Operator Admin Console mengubah durasi retensi Recycle Bin menjadi `30` hari
26. Operator Admin Console menyimpan perubahan Lifecycle Settings
27. Buka Settings > File Manager
28. Klik tombol Recycle Bin pada header kartu Storage Usage
29. Verifikasi Info Recycle Bin menampilkan `Files are permanently deleted after 30 days.`
30. Tutup modal Recycle Bin
