---
id: TC-FA-FAFM-E2E-049-maintenance-photo-dep-maintenance-routine
title: "Maintenance Before Photo dan After Photo pada task"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02e, ARS-01c, DIM-14a, DIM-14b, FAFM-LOGIC-02c, FAFM-LOGIC-02e, FAFM-LOGIC-02f, SRC-08, SRC-09, SYN-01b, SYN-01e, SYN-01h]
smoke: []
dependsOn: ["Maintenance Routine: foto Before dan After pada task"]
trace:
  ACT-02e: [18, 22]
  ARS-01c: 22
  DIM-14a: 22
  DIM-14b: 23
  FAFM-LOGIC-02c: [18, 22]
  FAFM-LOGIC-02e: 22
  FAFM-LOGIC-02f: 23
  SRC-08: [3, 8]
  SRC-09: [4, 9]
  SYN-01b: 22
  SYN-01e: 22
  SYN-01h: 25
anchor: [21]
coverage:
  web: automated
---

# Maintenance Before Photo dan After Photo pada task

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-049-1: Aset `Printer HP M404 {runId}`, Group `Branch Bandung`, ada di entitas aktor, memiliki satu task yang sudah memuat Before photo dan After photo.
  - DU-049-2: File `maint-before-{runId}.jpg`, Source `Maintenance Before Photo`, Reference ID task milik aset DU-049-1, aktif, Before photo task aset DU-049-1.
  - DU-049-3: File `maint-after-{runId}.jpg`, Source `Maintenance After Photo`, Reference ID task milik aset DU-049-1, aktif, After photo task aset DU-049-1.

## Test Steps

### Before photo dan After photo task terdaftar di tab Maintenance
1. Klik tab `Maintenance`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris file `maint-before-{runId}.jpg` tampil dengan Source `Maintenance Before Photo`
4. Verifikasi baris file `maint-after-{runId}.jpg` tampil dengan Source `Maintenance After Photo`
5. Catat Reference baris file `maint-before-{runId}.jpg`
6. Catat Reference baris file `maint-after-{runId}.jpg`
7. Buka task aset `Printer HP M404 {runId}`
8. Verifikasi ID task yang dibuka sama dengan Reference yang dicatat dari baris file `maint-before-{runId}.jpg`
9. Verifikasi ID task yang dibuka sama dengan Reference yang dicatat dari baris file `maint-after-{runId}.jpg`
10. Catat Status task

### Delete Before photo mengosongkan field tanpa mengubah task
11. Buka Settings > File Manager
12. Klik tab `Maintenance`
13. Ketik Search `maint-before-{runId}.jpg`, tekan Enter
14. Klik aksi Delete pada baris file `maint-before-{runId}.jpg`
15. Klik `[Delete]` pada dialog Delete File
16. Klik tombol Recycle Bin pada header kartu Storage Usage
17. Ketik Search `maint-before-{runId}.jpg`, tekan Enter
18. Verifikasi baris file `maint-before-{runId}.jpg` tampil di Recycle Bin
19. Tutup modal Recycle Bin
20. Buka task aset `Printer HP M404 {runId}`
21. Verifikasi After photo task tetap menampilkan file `maint-after-{runId}.jpg`
22. Verifikasi Before photo task menampilkan `—`
23. Verifikasi Status task sama dengan nilai yang dicatat pada langkah 10
24. Buka Changelog task aset `Printer HP M404 {runId}`
25. Verifikasi entri dengan Action `Edit`, Old Value `maint-before-{runId}.jpg`, dan New Value `—` tampil
26. Tutup Changelog task
