---
id: TC-FA-FAREG-E2E-042-draft-select-all
title: "Sub tab Draft: Select All lintas halaman"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-BLK-2@tabel-draft"]
smoke: []
dependsOn: []
trace:
  "EB-BLK-2@tabel-draft": [3, 5, 7, 9]
coverage:
  web: automated
---

# Sub tab Draft: Select All lintas halaman

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Data:
  - DU-042-1: 25 batch Draft dengan Group `Gudang Select {n} {runId}` (n = 1 sampai 25), Origin `—`, Total Asset `3`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − {n} menit`.
  - Rina W adalah pengguna aktif dengan role Manage asset & TAG pada Group batch.
- Kondisi: ukuran halaman tabel 10 baris per halaman.

## Test Steps

### Select All memilih seluruh baris yang cocok lintas halaman
1. Ketik Search `{runId}`, tekan Enter
2. Centang baris `Gudang Select 1 {runId}`
3. Verifikasi tombol `Select All (25 records)` tampil di bar seleksi tabel sub tab Draft
4. Klik `Select All (25 records)`
5. Verifikasi tombol berubah menjadi `Unselect All`
6. Pindah ke halaman 3 pada paginasi tabel
7. Verifikasi baris `Gudang Select 25 {runId}` pada halaman 3 tercentang

### Uncheck satu baris mengembalikan tombol Select All
8. Hilangkan centang baris `Gudang Select 25 {runId}`
9. Verifikasi tombol `Select All (25 records)` tampil kembali dengan jumlah tetap `25`
