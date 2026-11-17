---
id: TC-FA-FATR-BE-109-aturan-damaged-dep-damaged
title: "After photo required pada Damaged"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§4.1#r177", "§4.1#r178", "§4.1#r179", "§4.1#r180", "§9.2#b272", "§9.2#b425", "§9.7#r34", "§11#r16", "§4.1#r172"]
smoke: []
dependsOn: ["Damaged: Mark as Repaired"]
trace:
  "§4.1#r178": 2
  "§4.1#r177": [5, 6, 8]
  "§11#r16": 5
  "§4.1#r179": 10
  "§9.2#b425": 10
  "§4.1#r180": 11
  "§9.2#b272": [14, 15, 18, 19]
  "§9.7#r34": [14, 15, 18, 19]
  "§4.1#r172": [2, 5, 8]
---

# After photo required pada Damaged

## Prerequisites
- Aktor: Total Control.
- Data:
  - DU-109-1: entitas khusus `Entitas Aset Rusak {runId}`, tidak dipakai spec lain; semua data di bawah ada di entitas ini.
  - DU-109-2: aset `Genset Portabel {runId}`, Condition `Damaged`, ada record Damaged aktif.
  - DU-109-3: aset `Forklift Listrik {runId}`, Condition `Damaged`, ada record Damaged aktif.
  - DU-109-4: aset `Kompresor Angin {runId}`, Condition `Normal`, belum punya record Damaged.
  - DU-109-5: aset `Mesin Bubut {runId}`, Condition `Damaged`, ada record Damaged aktif, dengan Disposal Source `Manual` berstatus Waiting for Approval yang diajukan atas aset itu.
  - DU-109-6: berkas After photo `forklift-sesudah-perbaikan.jpg`.
  - DU-109-7: berkas Damaged Photo `kompresor-rusak.jpg`.
  - DU-109-8: aset `Pompa Celup {runId}`, sebelum dilaporkan Condition `Damaged` dengan record Damaged aktif; sudah dilaporkan lewat Disposal Report berstatus `Proceeded`, dan Disposal yang berasal dari Disposal Report itu berstatus Waiting for Approval.
- Kondisi:
  - After photo required bernilai `OFF`.
  - Transaction timeout bernilai `1` (days).

## Test Steps

### After photo required OFF: Mark as Repaired tanpa After photo diterima
1. Kirim Mark as Repaired untuk record Damaged aset `Genset Portabel {runId}` tanpa After photo
2. Verifikasi Mark as Repaired tanpa After photo diterima saat After photo required `OFF`

### After photo required ON: Mark as Repaired tanpa After photo ditolak
3. Total Control menyimpan After photo required bernilai `ON` di All categories
4. Kirim Mark as Repaired untuk record Damaged aset `Forklift Listrik {runId}` tanpa After photo
5. Verifikasi Mark as Repaired tanpa After photo ditolak karena After photo wajib sesuai nilai After photo required yang baru disimpan `ON`
6. Verifikasi record Damaged aset `Forklift Listrik {runId}` tetap aktif dan Condition tetap `Damaged`
7. Kirim Mark as Repaired untuk record Damaged aset `Forklift Listrik {runId}` dengan After photo `forklift-sesudah-perbaikan.jpg`
8. Verifikasi Mark as Repaired dengan After photo `forklift-sesudah-perbaikan.jpg` diterima

### After photo required tidak berlaku untuk pelaporan Damaged
9. Kirim laporan Damaged untuk aset `Kompresor Angin {runId}` dengan Damaged Photo `kompresor-rusak.jpg` tanpa After photo
10. Verifikasi laporan Damaged diterima tanpa After photo saat After photo required `ON`
11. Verifikasi Damaged Photo `kompresor-rusak.jpg` tersimpan pada laporan sebagaimana dikirim, tidak ditentukan oleh After photo required

### Disposal yang kena Transaction timeout mengembalikan Condition dan record Damaged
12. Waktu berlalu sampai batas Transaction timeout `1` (days) terlewati sejak transaksi pelepasan aset (Source `Manual`) atas aset `Mesin Bubut {runId}` diajukan
13. Job Transaction timeout berjalan
14. Verifikasi Condition aset `Mesin Bubut {runId}` kembali ke `Damaged`, nilai sebelum pelepasan aset diajukan
15. Verifikasi record Damaged aset `Mesin Bubut {runId}` kembali ke nilai sebelum pelepasan aset diajukan

### Pelepasan aset dari laporan pelepasan aset yang kena Transaction timeout mengembalikan Condition dan record Damaged
16. Waktu berlalu sampai batas Transaction timeout `1` (days) terlewati sejak transaksi pelepasan aset yang berasal dari laporan pelepasan aset atas aset `Pompa Celup {runId}` diajukan
17. Job Transaction timeout berjalan
18. Verifikasi Condition aset `Pompa Celup {runId}` kembali ke `Damaged`, nilai sebelum aset dilaporkan
19. Verifikasi record Damaged aset `Pompa Celup {runId}` kembali ke nilai sebelum aset dilaporkan
