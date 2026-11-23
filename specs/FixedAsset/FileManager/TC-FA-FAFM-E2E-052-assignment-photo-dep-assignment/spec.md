---
id: TC-FA-FAFM-E2E-052-assignment-photo-dep-assignment
title: "Handover Photo dan Return Photo pada transaksi Assignment"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02e, ARS-01c, DIM-14a, DIM-14b, FAFM-LOGIC-02c, FAFM-LOGIC-02e, FAFM-LOGIC-02f, SRC-11, SRC-12, SYN-01b, SYN-01e, SYN-01h]
smoke: []
dependsOn: ["Assignment: foto awal dan akhir transaksi"]
trace:
  ACT-02e: [18, 22]
  ARS-01c: 22
  DIM-14a: 22
  DIM-14b: 23
  FAFM-LOGIC-02c: [18, 22]
  FAFM-LOGIC-02e: 22
  FAFM-LOGIC-02f: 23
  SRC-11: [3, 8]
  SRC-12: [4, 9]
  SYN-01b: 22
  SYN-01e: 22
  SYN-01h: 25
anchor: [21]
coverage:
  web: automated
---

# Handover Photo dan Return Photo pada transaksi Assignment

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-052-1: Aset `Projector Epson EB-X49 {runId}`, Group `Head Office`, ada di entitas aktor, memiliki satu transaksi Assignment yang sudah memuat Handover Photo dan Return Photo.
  - DU-052-2: File `asg-handover-{runId}.jpg`, Source `Handover Photo`, Reference ID transaksi Assignment aset DU-052-1, aktif, Handover Photo transaksi Assignment aset DU-052-1.
  - DU-052-3: File `asg-return-{runId}.jpg`, Source `Return Photo`, Reference ID transaksi Assignment aset DU-052-1, aktif, Return Photo transaksi Assignment aset DU-052-1.

## Test Steps

### Handover Photo dan Return Photo terdaftar di tab Assignment
1. Klik tab `Assignment`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris file `asg-handover-{runId}.jpg` tampil dengan Source `Handover Photo`
4. Verifikasi baris file `asg-return-{runId}.jpg` tampil dengan Source `Return Photo`
5. Catat Reference baris file `asg-handover-{runId}.jpg`
6. Catat Reference baris file `asg-return-{runId}.jpg`
7. Buka transaksi Assignment aset `Projector Epson EB-X49 {runId}`
8. Verifikasi ID transaksi Assignment yang dibuka sama dengan Reference yang dicatat dari baris file `asg-handover-{runId}.jpg`
9. Verifikasi ID transaksi Assignment yang dibuka sama dengan Reference yang dicatat dari baris file `asg-return-{runId}.jpg`
10. Catat Status transaksi Assignment

### Delete Return Photo mengosongkan field tanpa mengubah transaksi
11. Buka Settings > File Manager
12. Klik tab `Assignment`
13. Ketik Search `asg-return-{runId}.jpg`, tekan Enter
14. Klik aksi Delete pada baris file `asg-return-{runId}.jpg`
15. Klik `[Delete]` pada dialog Delete File
16. Klik tombol Recycle Bin pada header kartu Storage Usage
17. Ketik Search `asg-return-{runId}.jpg`, tekan Enter
18. Verifikasi baris file `asg-return-{runId}.jpg` tampil di Recycle Bin
19. Tutup modal Recycle Bin
20. Buka transaksi Assignment aset `Projector Epson EB-X49 {runId}`
21. Verifikasi field Handover Photo pada transaksi Assignment tetap menampilkan file `asg-handover-{runId}.jpg`
22. Verifikasi field Return Photo pada transaksi Assignment menampilkan `—`
23. Verifikasi Status transaksi Assignment sama dengan nilai yang dicatat pada langkah 10
24. Buka Changelog transaksi Assignment aset `Projector Epson EB-X49 {runId}`
25. Verifikasi entri dengan Action `Edit`, Old Value `asg-return-{runId}.jpg`, dan New Value `—` tampil
26. Tutup Changelog transaksi Assignment
