---
id: TC-FA-ASTL-E2E-042-laporan-damaged-dep-damaged
title: "Laporan Damaged tercermin di daftar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-11d", "§9.7#r1"]
smoke: []
dependsOn: ["Damaged: laporan Damaged"]
trace:
  "ASTL-LOGIC-11d": [10, 13]
  "§9.7#r1": [4, 5]
anchor: [2]
coverage:
  web: automated
---

# Laporan Damaged tercermin di daftar

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-042-1: aset `Proyektor X2 {runId} - 1`, Group `IT`, managed, Custody `Available`, Condition `Normal`, satu garansi `Service warranty {runId}` sampai `T0 + 60 hari`.

## Test Steps

### Laporan Damaged tercermin di daftar
1. Ketik Search `Proyektor X2 {runId}`, tekan Enter
2. Verifikasi baris `Proyektor X2 {runId} - 1` menampilkan `Available`
3. Pada modul Damaged, Hendra Saputra membuat laporan Damaged atas aset `Proyektor X2 {runId} - 1`, tanpa memuat ulang halaman Fixed Asset > Assets
4. Verifikasi badge Status baris `Proyektor X2 {runId} - 1` berubah menjadi `Damaged` dan `Available` tidak lagi tampil
5. Verifikasi angka kartu `Issues` menjadi `1` karena Search hanya memuat aset ini

### Garansi di modul Damaged sama dengan daftar
6. Buka Setup Column
7. Centang `Warranty Expiry`
8. Tutup Setup Column
9. Arahkan kursor ke sel `Warranty Expiry` baris `Proyektor X2 {runId} - 1`
10. Verifikasi sel `Warranty Expiry` baris `Proyektor X2 {runId} - 1` menampilkan `T0 + 60 hari` dalam Date Format `dd/MM/yy` dan hover memuat `Service warranty {runId}`
11. Buka laporan Damaged atas aset `Proyektor X2 {runId} - 1` pada modul Damaged
12. Arahkan kursor ke garansi aset pada laporan Damaged
13. Verifikasi laporan Damaged menampilkan garansi `Service warranty {runId}` sampai `T0 + 60 hari` dengan nilai dan hover yang sama seperti kolom `Warranty Expiry` di daftar
