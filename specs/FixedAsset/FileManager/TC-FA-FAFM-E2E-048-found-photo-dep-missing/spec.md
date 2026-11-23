---
id: TC-FA-FAFM-E2E-048-found-photo-dep-missing
title: "Found Photo pada record Missing"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02e, ARS-01c, DIM-14a, DIM-14b, FAFM-LOGIC-02c, FAFM-LOGIC-02e, FAFM-LOGIC-02f, SRC-07, SYN-01b, SYN-01e, SYN-01h]
smoke: []
dependsOn: ["Missing: Mark as Found"]
trace:
  ACT-02e: [16, 20]
  ARS-01c: 20
  DIM-14a: 20
  DIM-14b: 21
  FAFM-LOGIC-02c: [16, 20]
  FAFM-LOGIC-02e: 20
  FAFM-LOGIC-02f: 21
  SRC-07: [3, 7, 17]
  SYN-01b: 20
  SYN-01e: 20
  SYN-01h: 23
anchor: [6]
coverage:
  web: automated
---

# Found Photo pada record Missing

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-048-1: Aset `MacBook Pro 14 {runId}`, Group `Head Office`, ada di entitas aktor, memiliki satu record Missing yang sudah selesai Mark as Found.
  - DU-048-2: Record Missing milik aset DU-048-1, dengan field Found Photo berisi file DU-048-3.
  - DU-048-3: File `found-{runId}.jpg`, Source `Found Photo`, Reference ID record Missing milik DU-048-2, aktif.

## Test Steps

### Found Photo terdaftar di tab Missing dan sama dengan file di record
1. Klik tab `Missing`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris file `found-{runId}.jpg` milik aset `MacBook Pro 14 {runId}` tampil
4. Catat Reference baris file `found-{runId}.jpg`
5. Buka record Missing aset `MacBook Pro 14 {runId}`
6. Verifikasi field Found Photo pada record Missing menampilkan file `found-{runId}.jpg`
7. Verifikasi ID record Missing yang dibuka sama dengan Reference yang dicatat dari baris file `found-{runId}.jpg`
8. Catat Status record Missing

### Delete Found Photo mengosongkan field tanpa mengubah record Missing
9. Buka Settings > File Manager
10. Klik tab `Missing`
11. Ketik Search `found-{runId}.jpg`, tekan Enter
12. Klik aksi Delete pada baris file `found-{runId}.jpg`
13. Klik `[Delete]` pada dialog Delete File
14. Klik tombol Recycle Bin pada header kartu Storage Usage
15. Ketik Search `found-{runId}.jpg`, tekan Enter
16. Verifikasi baris file `found-{runId}.jpg` tampil di Recycle Bin
17. Verifikasi baris file `found-{runId}.jpg` menampilkan Source `Found Photo`
18. Tutup modal Recycle Bin
19. Buka record Missing aset `MacBook Pro 14 {runId}`
20. Verifikasi field Found Photo pada record Missing menampilkan `—`
21. Verifikasi Status record Missing sama dengan nilai yang dicatat pada langkah 8
22. Buka Changelog record Missing aset `MacBook Pro 14 {runId}`
23. Verifikasi entri dengan Action `Edit`, Old Value `found-{runId}.jpg`, dan New Value `—` tampil
24. Tutup Changelog record Missing
