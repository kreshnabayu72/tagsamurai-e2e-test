---
id: TC-FA-DAMAGED-E2E-032-efek-repaired-di-asset-dep-asset
title: "Setelah Mark as Repaired, Asset Detail menampilkan status global Normal tanpa banner Damaged dan Transaction log memuat Repaired"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§Aturan Logika Modul#r31, §Aturan Logika Modul#r56, §Aturan Logika Modul#r40, §9.7#r9, §8.2#b1, §4.1#r10]
smoke: []
dependsOn:
  - "Asset: Asset Detail (status global aset, banner Damaged, Transaction log)"
trace:
  §Aturan Logika Modul#r31: [13, 14]
  §Aturan Logika Modul#r56: 13
  §Aturan Logika Modul#r40: 14
  §9.7#r9: [13, 20]
  §8.2#b1: 16
  §4.1#r10: 14
anchor: [3, 4]
coverage:
  web: automated
---

# Setelah Mark as Repaired, Asset Detail menampilkan status global Normal tanpa banner Damaged dan Transaction log memuat Repaired

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Assets, tab Assets (Asset List).
- Data:
  - DU-032-1: aset `Genset Honda EU22i {runId}`, Group `Head Office`, tanpa TAG, status global `Damaged`, sudah punya record Damage berjalan berstatus `Damaged`.
  - DU-032-2: Repair note `Mesin diservis dan busi diganti` untuk Mark as Repaired atas `Genset Honda EU22i {runId}`.
- Kondisi:
  - After photo required bernilai `OFF`.

## Test Steps

### Efek Mark as Repaired di Asset Detail dan History
1. Ketik Search `Genset Honda EU22i {runId}`, tekan Enter
2. Klik nama aset `Genset Honda EU22i {runId}` untuk membuka Asset Detail
3. Verifikasi status global aset `Damaged` sebelum perbaikan pada Asset Detail aset ini
4. Verifikasi banner `Damaged since [Date].` tampil pada Asset Detail
5. Buka tab `Damaged` pada halaman Assets
6. Ketik Search `Genset Honda EU22i {runId}`, tekan Enter
7. Klik aksi `Mark as Repaired` pada baris `Genset Honda EU22i {runId}`
8. Isi `Repair note` dengan `Mesin diservis dan busi diganti`
9. Klik `[Mark as Repaired]` pada footer dialog
10. Buka tab `Assets` pada halaman Assets
11. Ganti isi kotak search dengan `Genset Honda EU22i {runId}`, tekan Enter
12. Klik nama aset `Genset Honda EU22i {runId}` untuk membuka Asset Detail
13. Verifikasi status global aset `Normal` tampil pada Asset Detail
14. Verifikasi banner `Damaged since [Date].` tidak tampil pada Asset Detail
15. Buka Transaction log pada Asset Detail
16. Verifikasi entri `Repaired` tampil
17. Buka tab `Damaged` pada halaman Assets
18. Buka sub-tab `History`
19. Ketik Search `Genset Honda EU22i {runId}`, tekan Enter
20. Verifikasi baris `Genset Honda EU22i {runId}` tampil dengan Status `Repaired`
