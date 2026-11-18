---
id: TC-FA-ASTL-E2E-043-laporan-missing-dep-missing
title: "Laporan Missing tercermin di daftar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-11d", "ASTL-LOGIC-17l", "§9.7#r1"]
smoke: []
dependsOn: ["Missing: laporan Missing"]
trace:
  "ASTL-LOGIC-11d": [10, 13]
  "ASTL-LOGIC-17l": 18
  "§9.7#r1": [4, 5]
anchor: [2, 16]
coverage:
  web: automated
---

# Laporan Missing tercermin di daftar

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-043-1: aset `Meja Rapat {runId} - 1`, Group `GA`, managed, Custody `Available`, Condition `Normal`, satu garansi `Frame warranty {runId}` sampai `T0 + 45 hari`.
  - DU-043-2: aset `Scanner Gudang {runId} - 1`, Group `Cabang Medan`, Unmanaged, Custody `Available`, dengan record Missing berjalan berstatus `Missing`.

## Test Steps

### Laporan Missing tercermin di daftar
1. Ketik Search `Meja Rapat {runId}`, tekan Enter
2. Verifikasi baris `Meja Rapat {runId} - 1` menampilkan `Available` sebelum laporan Missing
3. Pada modul Missing, Hendra Saputra membuat laporan Missing atas aset `Meja Rapat {runId} - 1`, tanpa memuat ulang halaman Fixed Asset > Assets
4. Verifikasi badge Status baris `Meja Rapat {runId} - 1` berubah menjadi `Missing` dan `Available` tidak lagi tampil
5. Verifikasi angka kartu `Issues` menjadi `1` karena Search hanya memuat aset ini

### Garansi di modul Missing sama dengan daftar
6. Buka Setup Column
7. Centang `Warranty Expiry`
8. Tutup Setup Column
9. Arahkan kursor ke sel `Warranty Expiry` baris `Meja Rapat {runId} - 1`
10. Verifikasi sel `Warranty Expiry` baris `Meja Rapat {runId} - 1` menampilkan `T0 + 45 hari` dalam Date Format `dd/MM/yy` dan hover memuat `Frame warranty {runId}`
11. Buka laporan Missing atas aset `Meja Rapat {runId} - 1` pada modul Missing
12. Arahkan kursor ke garansi aset pada laporan Missing
13. Verifikasi laporan Missing menampilkan garansi `Frame warranty {runId}` sampai `T0 + 45 hari` dengan nilai dan hover yang sama seperti kolom `Warranty Expiry` di daftar

### Delete Asset Data diblok record Missing berjalan
14. Ketik Search `Scanner Gudang {runId}`, tekan Enter
15. Buka menu `⋯` baris `Scanner Gudang {runId} - 1`
16. Verifikasi menu aksi baris `Scanner Gudang {runId} - 1` memuat `Detail`
17. Arahkan kursor ke aksi `Delete Asset Data`
18. Verifikasi aksi `Delete Asset Data` tampil `Disabled` dengan tooltip `Asset has an ongoing missing record. Complete or close the record first.`
