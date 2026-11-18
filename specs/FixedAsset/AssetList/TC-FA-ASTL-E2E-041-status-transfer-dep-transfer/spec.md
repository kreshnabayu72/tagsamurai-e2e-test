---
id: TC-FA-ASTL-E2E-041-status-transfer-dep-transfer
title: "Status Transfer dan pintasan Transfer"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.7#r1"]
smoke: []
dependsOn: ["Transfer: transaksi Transfer"]
trace:
  "§9.7#r1": [4, 5]
anchor: [2]
coverage:
  web: automated
---

# Status Transfer dan pintasan Transfer

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-041-1: aset `Server Rack {runId} - 1`, Group `IT`, managed, Custody `Available`.

## Test Steps

### Status Transfer tercermin di daftar
1. Ketik Search `Server Rack {runId}`, tekan Enter
2. Verifikasi baris `Server Rack {runId} - 1` menampilkan `Available`
3. Pada modul Transfer, Hendra Saputra mengajukan Transfer aset `Server Rack {runId} - 1` ke group lain, tanpa memuat ulang halaman Fixed Asset > Assets
4. Verifikasi badge Status baris `Server Rack {runId} - 1` berubah menjadi `In Transfer Process` dan `Available` tidak lagi tampil
5. Verifikasi angka kartu `In Transaction` menjadi `1` karena Search hanya memuat aset ini
