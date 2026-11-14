---
id: TC-FA-FACO-E2E-047-capability-dicabut
title: "Capability Update dicabut saat halaman terbuka"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["EB-AKS-6"]
smoke: []
dependsOn: []
trace:
  "EB-AKS-6": [9, 10, 11, 12]
anchor: [4, 5]
coverage:
  web: automated
---

# Capability Update dicabut saat halaman terbuka

## Prerequisites
- Aktor: User `Wulan Sari {runId}` (Manage accounting huruf Read dan Update); aktor pemicu pencabutan adalah Total Control lain.
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-047-1: User `Wulan Sari {runId}` dengan Global Role Manage accounting huruf Read dan Update (Read baseline terkunci), scope seluruh client.
  - DU-047-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.

## Test Steps

### Aksi ditolak dan elemen aksi tersembunyi setelah capability Update dicabut
1. Buka halaman Settings > Accounting
2. Klik tab `Chart of Accounts`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi baris Account Code `5-6001-{runId}` tampil di tabel
5. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Enabled
6. Aktor pemicu mencabut huruf Update milik `Wulan Sari {runId}`
7. Klik Switch Status pada baris Account Code `5-6001-{runId}`
8. Klik `[Deactivate]` pada dialog `Deactivate Account`
9. Verifikasi toast `You don't have permission to do this.` tampil
10. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` tetap Active
11. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Disabled
12. Verifikasi ikon `⋯` tidak dirender pada baris Account Code `5-6001-{runId}`
