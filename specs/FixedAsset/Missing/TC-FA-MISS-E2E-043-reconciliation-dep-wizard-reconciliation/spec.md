---
id: TC-FA-MISS-E2E-043-reconciliation-dep-wizard-reconciliation
title: "Record Missing dari Wizard Reconciliation dengan Source Reconciliation"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.3#b4", "§11#r11", "§4.1a#p11"]
smoke: []
dependsOn: ["Wizard Reconciliation: langkah aset tidak ditemukan > Report Missing"]
trace:
  "§4.2.3#b4": [5, 10, 12, 14, 19, 26, 31, 34]
  "§11#r11": [11, 17]
  "§4.1a#p11": [11]
anchor: [33]
coverage:
  web: automated
---

# Record Missing dari Wizard Reconciliation dengan Source Reconciliation

## Prerequisites
- Aktor: pemilik Wizard Reconciliation `Maya Putri {runId}`. Aktor lain: Total Control `Rina W`.
- Layar awal: Wizard Reconciliation.
- Data:
  - DU-043-1: Rekonsiliasi `Rekonsiliasi Gudang {runId}` milik `Maya Putri {runId}` yang memuat aset tidak ditemukan `Hand Pallet Truck {runId}`.
  - DU-043-2: Asset `Hand Pallet Truck {runId}`, Group `Warehouse`, tanpa record Missing.
  - DU-043-3: Pengguna `Maya Putri {runId}`, pemilik Wizard Reconciliation yang melapor sebagai Pelapor admin.
  - DU-043-4: Pengguna `Rina W`, Total Control.
  - DU-043-5: What happened `Hand pallet truck tidak ditemukan saat rekonsiliasi gudang`.
  - DU-043-6: Asset `Forklift Mini {runId}`, Group `Warehouse`, tanpa record Missing, juga tercantum sebagai aset tidak ditemukan pada `Rekonsiliasi Gudang {runId}`.
  - DU-043-7: What happened `Forklift mini tidak ditemukan saat rekonsiliasi gudang`.
- Kondisi:
  - Akun `Maya Putri {runId}` dan `Rina W` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Report Missing dari langkah aset tidak ditemukan
1. Buka langkah aset tidak ditemukan pada `Rekonsiliasi Gudang {runId}`
2. Klik `Report Missing` pada aset `Hand Pallet Truck {runId}`
3. Isi What happened `Hand pallet truck tidak ditemukan saat rekonsiliasi gudang`
4. Klik `[Report Missing]` pada dialog
5. Verifikasi toast `Success, asset has been reported missing.` tampil

### Record Missing bersumber Reconciliation
6. Masuk sebagai `Rina W`
7. Buka halaman `Assets`
8. Klik tab `Missing`
9. Ketik Search `Hand Pallet Truck {runId}`, tekan Enter
10. Verifikasi baris `Hand Pallet Truck {runId}` berstatus `Missing`
11. Verifikasi kolom Source pada baris itu `Reconciliation`
12. Verifikasi kolom Reported By pada baris itu `Maya Putri {runId}`
13. Klik `Hand Pallet Truck {runId}` pada kolom Name
14. Verifikasi dialog Missing Log memuat node `Reported missing by` oleh `Maya Putri {runId}` dengan What happened `Hand pallet truck tidak ditemukan saat rekonsiliasi gudang`
15. Tutup dialog Missing Log dengan `✕`
16. Buka menu `⋯` pada baris `Hand Pallet Truck {runId}`
17. Verifikasi aksi `Report Disposal` tampil pada menu

### Notifikasi missing_reported atas record Source Reconciliation
18. Buka daftar notifikasi
19. Verifikasi notifikasi event `missing_reported` atas `Hand Pallet Truck {runId}` tampil di daftar notifikasi

### Aset yang sudah punya record berjalan dilewati pada laporan Reconciliation
20. Masuk sebagai `Maya Putri {runId}`
21. Buka langkah aset tidak ditemukan pada `Rekonsiliasi Gudang {runId}`
22. Pilih aset `Hand Pallet Truck {runId}` dan `Forklift Mini {runId}`
23. Klik `Report Missing`
24. Isi What happened `Forklift mini tidak ditemukan saat rekonsiliasi gudang`
25. Klik `[Report Missing]` pada dialog
26. Verifikasi toast `Success, asset has been reported missing. Some items were skipped.` tampil
27. Masuk sebagai `Rina W`
28. Buka halaman `Assets`
29. Klik tab `Missing`
30. Ketik Search `Forklift Mini {runId}`, tekan Enter
31. Verifikasi baris `Forklift Mini {runId}` berstatus `Missing` dengan kolom Source `Reconciliation`
32. Ganti isi kotak search dengan `Hand Pallet Truck {runId}`, tekan Enter
33. Verifikasi baris `Hand Pallet Truck {runId}` tampil di sub-tab Active
34. Verifikasi hanya satu baris `Hand Pallet Truck {runId}` tampil di sub-tab Active, sehingga tidak ada record baru untuk aset yang sudah punya record berjalan
