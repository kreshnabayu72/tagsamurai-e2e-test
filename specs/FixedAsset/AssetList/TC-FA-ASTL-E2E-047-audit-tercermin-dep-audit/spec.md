---
id: TC-FA-ASTL-E2E-047-audit-tercermin-dep-audit
title: "Audit tercermin di daftar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.7#r6"]
smoke: []
dependsOn: ["Audit: sesi Audit"]
trace:
  "§9.7#r6": [7, 9, 11]
anchor: [5]
coverage:
  web: automated
---

# Audit tercermin di daftar

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client; Auditor sesi Audit memicu perubahan state.
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-047-1: aset `Genset 20kVA {runId} - 1`, dicari dengan `Genset 20kVA {runId}`, Group `IT`, Custody `Available`, belum pernah dipindai pada Audit, ada di entitas aktor.

## Test Steps

### Sesi Audit dan pemindaian tercermin di daftar
1. Ketik Search `Genset 20kVA {runId}`, tekan Enter
2. Buka Setup Column
3. Centang `Last Scanned`
4. Tutup Setup Column
5. Verifikasi baris `Genset 20kVA {runId} - 1` menampilkan `Available` dan kolom `Last Scanned` bernilai `—`
6. Auditor memulai sesi Audit yang memuat aset `Genset 20kVA {runId} - 1`, tanpa memuat ulang halaman
7. Verifikasi badge `In Audit` tampil pada baris `Genset 20kVA {runId} - 1`
8. Buka menu `⋯` baris `Genset 20kVA {runId} - 1`
9. Verifikasi aksi `Edit` tampil `Disabled` dengan tooltip `Asset is in audit. Complete or cancel the audit to continue.`
10. Auditor memindai aset `Genset 20kVA {runId} - 1` pada sesi Audit, tanpa memuat ulang halaman
11. Verifikasi kolom `Last Scanned` baris `Genset 20kVA {runId} - 1` tidak lagi `—` dan memuat tanggal pindai terbaru dalam Date Format `dd/MM/yy`
