---
id: TC-FA-FAFM-E2E-050-disposal-document-dep-disposal
title: "Disposal Document dan aset Disposed"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02e, ARS-01c, DIM-14a, DIM-14b, DIM-14d, DIM-14e, DIM-14f, F-FAFM-07c, FAFM-LOGIC-02c, FAFM-LOGIC-02e, FAFM-LOGIC-02f, SRC-10, SYN-01b, SYN-01e, SYN-01h]
smoke: []
dependsOn: ["Disposal: halaman Execute dan dokumen Disposal"]
trace:
  ACT-02e: [15, 19]
  ARS-01c: 19
  DIM-14a: 19
  DIM-14b: 20
  DIM-14d: 19
  DIM-14e: 43
  DIM-14f: [15, 20]
  F-FAFM-07c: [31, 38]
  FAFM-LOGIC-02c: [15, 19]
  FAFM-LOGIC-02e: 19
  FAFM-LOGIC-02f: 20
  SRC-10: [3, 6, 16, 34, 40]
  SYN-01b: 19
  SYN-01e: 19
  SYN-01h: 22
anchor: []
coverage:
  web: automated
---

# Disposal Document dan aset Disposed

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-050-1: Aset `Printer HP M404 {runId}`, Status `Active`, Group `Branch Bandung`, ada di entitas aktor, memiliki satu transaksi Disposal yang belum Execute.
  - DU-050-2: Transaksi Disposal aset DU-050-1 yang belum Execute, dengan field Disposal Document berisi file DU-050-3.
  - DU-050-3: File `dsp-pending-{runId}.pdf`, Source `Disposal Document`, Reference ID transaksi DU-050-2, aktif.
  - DU-050-4: Aset `Monitor LG 24 {runId}`, Status `Active`, Group `Head Office`, ada di entitas aktor, memiliki satu transaksi Disposal yang siap Execute.
  - DU-050-5: File `dsp-auction-{runId}.pdf`, Source `Disposal Document`, Reference ID transaksi Disposal aset DU-050-4, dipilih di halaman Execute transaksi aset DU-050-4.

## Test Steps

### Disposal Document transaksi yang belum Execute terdaftar di tab Disposal
1. Klik tab `Disposal`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris file `dsp-pending-{runId}.pdf` milik aset `Printer HP M404 {runId}` tampil di tab `Disposal`
4. Catat Reference baris file `dsp-pending-{runId}.pdf`
5. Buka transaksi Disposal aset `Printer HP M404 {runId}`
6. Verifikasi ID transaksi Disposal yang dibuka sama dengan Reference yang dicatat dari baris file `dsp-pending-{runId}.pdf`
7. Catat Status transaksi Disposal

### Delete Disposal Document pada transaksi yang belum Execute
8. Buka Settings > File Manager
9. Klik tab `Disposal`
10. Ketik Search `dsp-pending-{runId}.pdf`, tekan Enter
11. Klik aksi Delete pada baris file `dsp-pending-{runId}.pdf`
12. Klik `[Delete]` pada dialog Delete File
13. Klik tombol Recycle Bin pada header kartu Storage Usage
14. Ketik Search `dsp-pending-{runId}.pdf`, tekan Enter
15. Verifikasi baris file `dsp-pending-{runId}.pdf` tampil di Recycle Bin
16. Verifikasi baris file `dsp-pending-{runId}.pdf` menampilkan Source `Disposal Document` di Recycle Bin
17. Tutup modal Recycle Bin
18. Buka transaksi Disposal aset `Printer HP M404 {runId}`
19. Verifikasi field Disposal Document pada transaksi Disposal menampilkan `—`
20. Verifikasi Status transaksi Disposal sama dengan nilai yang dicatat pada langkah 7
21. Buka Changelog transaksi Disposal aset `Printer HP M404 {runId}`
22. Verifikasi entri dengan Action `Edit`, Old Value `dsp-pending-{runId}.pdf`, dan New Value `—` tampil
23. Tutup Changelog transaksi Disposal

### Execute Disposal menjadikan aset Disposed tampil di tab Asset Data dengan ukuran filenya
24. Buka halaman Execute transaksi Disposal aset `Monitor LG 24 {runId}`
25. Pilih file `dsp-auction-{runId}.pdf` pada field Disposal Document
26. Execute transaksi Disposal
27. Konfirmasi Execute transaksi Disposal
28. Buka Settings > File Manager
29. Klik tab `Disposed & Unmanaged Assets`
30. Ketik Search `Monitor LG 24 {runId}`, tekan Enter
31. Verifikasi baris aset `Monitor LG 24 {runId}` tampil dengan Status `Disposed`
32. Klik tab `Disposal`
33. Ketik Search `dsp-auction-{runId}.pdf`, tekan Enter
34. Verifikasi baris file `dsp-auction-{runId}.pdf` milik aset `Monitor LG 24 {runId}` tampil di tab `Disposal`
35. Catat Reference baris file `dsp-auction-{runId}.pdf`
36. Catat nilai Size baris file `dsp-auction-{runId}.pdf`
37. Klik tab `Disposed & Unmanaged Assets`
38. Verifikasi nilai Files Size baris aset `Monitor LG 24 {runId}` sama dengan nilai Size yang dicatat pada langkah 36
39. Buka transaksi Disposal aset `Monitor LG 24 {runId}`
40. Verifikasi ID transaksi Disposal yang dibuka sama dengan Reference yang dicatat dari baris file `dsp-auction-{runId}.pdf`

### Execute tanpa Disposal Document tidak berhasil karena kewajiban unggah tetap berlaku
41. Buka halaman Execute transaksi Disposal aset `Printer HP M404 {runId}`
42. Execute transaksi Disposal tanpa memilih file pada field Disposal Document
43. Verifikasi transaksi Disposal aset `Printer HP M404 {runId}` tidak berhasil di-Execute dan Status aset tetap `Active`
