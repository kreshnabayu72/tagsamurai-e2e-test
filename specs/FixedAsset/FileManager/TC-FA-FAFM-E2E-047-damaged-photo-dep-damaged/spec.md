---
id: TC-FA-FAFM-E2E-047-damaged-photo-dep-damaged
title: "Damaged Photo dan Repair Photo pada record Damaged"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02e, ARS-01c, DIM-14a, DIM-14b, EC-02, FAFM-LOGIC-01e, FAFM-LOGIC-02c, FAFM-LOGIC-02e, FAFM-LOGIC-02f, SRC-05, SRC-06, SYN-01b, SYN-01e, SYN-01h, "§9.2#p25", "§9.2#p27", "§9.4.3#b8"]
smoke: []
dependsOn: ["Damaged: Report Damaged dan Mark as Repaired"]
trace:
  ACT-02e: [20, 24]
  ARS-01c: 24
  DIM-14a: 24
  DIM-14b: 25
  EC-02: [20, 24, 25]
  FAFM-LOGIC-01e: [8, 9, 24]
  FAFM-LOGIC-02c: [20, 24]
  FAFM-LOGIC-02e: 24
  FAFM-LOGIC-02f: 25
  SRC-05: [3, 10]
  SRC-06: [4, 11]
  SYN-01b: 24
  SYN-01e: 24
  SYN-01h: 27
  "§9.2#p25": 24
  "§9.2#p27": 25
  "§9.4.3#b8": 25
anchor: [23]
coverage:
  web: automated
---

# Damaged Photo dan Repair Photo pada record Damaged

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-047-1: Aset `Toyota Avanza {runId}`, Group `Fleet`, ada di entitas aktor, memiliki satu record Damaged yang sudah selesai Mark as Repaired.
  - DU-047-2: Record Damaged milik aset DU-047-1, dengan field Damaged Photo berisi file DU-047-3 dan field Repair Photo berisi file DU-047-4.
  - DU-047-3: File `damage-{runId}.jpg`, Source `Damaged Photo`, Size `900.0 KB`, Reference ID record DU-047-2, aktif.
  - DU-047-4: File `repair-{runId}.jpg`, Source `Repair Photo`, Size `880.0 KB`, Reference ID record DU-047-2, aktif.

## Test Steps

### Damaged Photo dan Repair Photo terdaftar di tab Damaged dan sama dengan file di record
1. Klik tab `Damaged`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris file `damage-{runId}.jpg` tampil dengan Source `Damaged Photo`
4. Verifikasi baris file `repair-{runId}.jpg` tampil dengan Source `Repair Photo`
5. Catat Reference baris file `damage-{runId}.jpg`
6. Catat Reference baris file `repair-{runId}.jpg`
7. Buka record Damaged aset `Toyota Avanza {runId}`
8. Verifikasi field Damaged Photo pada record Damaged menampilkan file `damage-{runId}.jpg`
9. Verifikasi field Repair Photo pada record Damaged menampilkan file `repair-{runId}.jpg`
10. Verifikasi ID record Damaged yang dibuka sama dengan Reference yang dicatat dari baris file `damage-{runId}.jpg`
11. Verifikasi ID record Damaged yang dibuka sama dengan Reference yang dicatat dari baris file `repair-{runId}.jpg`
12. Catat Status record Damaged

### Delete Damaged Photo tidak diblokir dan mengosongkan field tanpa mengubah record
13. Buka Settings > File Manager
14. Klik tab `Damaged`
15. Ketik Search `damage-{runId}.jpg`, tekan Enter
16. Klik aksi Delete pada baris file `damage-{runId}.jpg`
17. Klik `[Delete]` pada dialog Delete File
18. Klik tombol Recycle Bin pada header kartu Storage Usage
19. Ketik Search `damage-{runId}.jpg`, tekan Enter
20. Verifikasi baris file `damage-{runId}.jpg` tampil di Recycle Bin
21. Tutup modal Recycle Bin
22. Buka record Damaged aset `Toyota Avanza {runId}`
23. Verifikasi field Repair Photo pada record Damaged tetap menampilkan file `repair-{runId}.jpg`
24. Verifikasi field Damaged Photo pada record Damaged kosong dan tidak lagi menampilkan file `damage-{runId}.jpg`
25. Verifikasi Status record Damaged sama dengan nilai yang dicatat pada langkah 12
26. Buka Changelog record Damaged aset `Toyota Avanza {runId}`
27. Verifikasi entri dengan Action `Edit`, Old Value `damage-{runId}.jpg`, dan New Value `—` tampil
28. Tutup Changelog record Damaged
