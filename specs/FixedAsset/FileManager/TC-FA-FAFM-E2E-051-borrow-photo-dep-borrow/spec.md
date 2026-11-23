---
id: TC-FA-FAFM-E2E-051-borrow-photo-dep-borrow
title: "Handover Photo dan Return Photo pada transaksi Borrow"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02e, ARS-01c, DIM-14a, DIM-14b, DIM-14d, DIM-14e, DIM-14f, FAFM-LOGIC-02c, FAFM-LOGIC-02e, FAFM-LOGIC-02f, SRC-11, SRC-12, SYN-01b, SYN-01e, SYN-01h]
smoke: []
dependsOn: ["Borrow: foto awal dan akhir transaksi"]
trace:
  ACT-02e: [19, 22]
  ARS-01c: 22
  DIM-14a: 22
  DIM-14b: 23
  DIM-14d: 22
  DIM-14e: 29
  DIM-14f: [19, 23]
  FAFM-LOGIC-02c: [19, 22]
  FAFM-LOGIC-02e: 22
  FAFM-LOGIC-02f: 23
  SRC-11: [3, 8]
  SRC-12: [4, 11]
  SYN-01b: 22
  SYN-01e: 22
  SYN-01h: 25
anchor: []
coverage:
  web: automated
---

# Handover Photo dan Return Photo pada transaksi Borrow

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-051-1: Aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, ada di entitas aktor, memiliki satu transaksi Borrow yang sudah Handover dan belum Return.
  - DU-051-2: Transaksi Borrow aset DU-051-1 yang belum Return, dengan field Handover Photo berisi file DU-051-3.
  - DU-051-3: File `handover-{runId}.jpg`, Source `Handover Photo`, Reference ID transaksi DU-051-2, aktif.
  - DU-051-4: Aset `Camera Canon EOS R6 {runId}`, Group `Head Office`, ada di entitas aktor, memiliki satu transaksi Borrow yang sudah Return.
  - DU-051-5: File `return-{runId}.jpg`, Source `Return Photo`, Reference ID transaksi Borrow aset DU-051-4, aktif, Return Photo transaksi Borrow aset DU-051-4.

## Test Steps

### Handover Photo dan Return Photo terdaftar di tab Borrow
1. Klik tab `Borrow`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris file `handover-{runId}.jpg` tampil dengan Source `Handover Photo`
4. Verifikasi baris file `return-{runId}.jpg` tampil dengan Source `Return Photo`
5. Catat Reference baris file `handover-{runId}.jpg`
6. Catat Reference baris file `return-{runId}.jpg`
7. Buka transaksi Borrow aset `Laptop Dell Latitude 5420 {runId}`
8. Verifikasi ID transaksi Borrow yang dibuka sama dengan Reference yang dicatat dari baris file `handover-{runId}.jpg`
9. Catat Status transaksi Borrow
10. Buka transaksi Borrow aset `Camera Canon EOS R6 {runId}`
11. Verifikasi ID transaksi Borrow yang dibuka sama dengan Reference yang dicatat dari baris file `return-{runId}.jpg`

### Delete Handover Photo pada transaksi yang belum Return
12. Buka Settings > File Manager
13. Klik tab `Borrow`
14. Ketik Search `handover-{runId}.jpg`, tekan Enter
15. Klik aksi Delete pada baris file `handover-{runId}.jpg`
16. Klik `[Delete]` pada dialog Delete File
17. Klik tombol Recycle Bin pada header kartu Storage Usage
18. Ketik Search `handover-{runId}.jpg`, tekan Enter
19. Verifikasi baris file `handover-{runId}.jpg` tampil di Recycle Bin
20. Tutup modal Recycle Bin
21. Buka transaksi Borrow aset `Laptop Dell Latitude 5420 {runId}`
22. Verifikasi field Handover Photo pada transaksi Borrow menampilkan `—`
23. Verifikasi Status transaksi Borrow sama dengan nilai yang dicatat pada langkah 9
24. Buka Changelog transaksi Borrow aset `Laptop Dell Latitude 5420 {runId}`
25. Verifikasi entri dengan Action `Edit`, Old Value `handover-{runId}.jpg`, dan New Value `—` tampil
26. Tutup Changelog transaksi Borrow

### Return tanpa foto yang diwajibkan tidak berhasil karena kewajiban unggah tetap berlaku
27. Buka transaksi Borrow aset `Laptop Dell Latitude 5420 {runId}`
28. Lakukan Return pada transaksi Borrow aset `Laptop Dell Latitude 5420 {runId}` tanpa mengunggah foto
29. Verifikasi Return transaksi Borrow aset `Laptop Dell Latitude 5420 {runId}` tidak berhasil karena kewajiban unggah foto belum terpenuhi
