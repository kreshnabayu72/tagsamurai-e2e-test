---
id: TC-FA-FAREG-E2E-042-draft-select-all
title: "Sub tab Draft: Select All lintas halaman"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["EB-BLK-2@tabel-draft"]
smoke: []
dependsOn: []
trace:
  "EB-BLK-2@tabel-draft": [2, 4, 6, 8]
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
2. Verifikasi tombol `Select All (25 records)` tampil di atas tabel sub tab Draft
3. Klik `Select All (25 records)`
4. Verifikasi tombol berubah menjadi `Unselect All`
5. Pindah ke halaman 3 pada paginasi tabel
6. Verifikasi baris `Gudang Select 25 {runId}` pada halaman 3 tercentang

### Uncheck satu baris mengembalikan tombol Select All
7. Hilangkan centang baris `Gudang Select 25 {runId}`
8. Verifikasi tombol `Select All (25 records)` tampil kembali dengan jumlah tetap `25`
