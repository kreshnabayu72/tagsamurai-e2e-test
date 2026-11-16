---
id: TC-FA-FACO-E2E-053-gating-link-used-by-read-dep-asset-class
title: "Manage accounting huruf Read melihat link Used By dan membuka popup Used By"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.8#r4"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  "§4.8#r4": [4, 6]
anchor: []
coverage:
  web: automated
---

# Manage accounting huruf Read melihat link Used By dan membuka popup Used By

## Prerequisites
- Aktor: User `Maya Lestari {runId}` (Manage accounting huruf Read saja).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-053-1: User `Maya Lestari {runId}` dengan Global Role Manage accounting huruf Read saja, scope seluruh client.
  - DU-053-2: Account Code `RDU-{runId}`, Account Name `Fixed Assets – Buildings {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 2 Asset Class (DU-053-3, DU-053-4).
  - DU-053-3: Asset Class `Office Buildings {runId}`; Asset Cost `RDU-{runId}`.
  - DU-053-4: Asset Class `Warehouse Buildings {runId}`; Asset Cost `RDU-{runId}`.

## Test Steps

### Link Used By tampil dan popup Used By terbuka
1. Buka halaman Settings > Accounting
2. Klik tab `Chart of Accounts`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi angka Used By `2` pada baris `RDU-{runId}` dapat diklik
5. Klik angka Used By `2` pada baris `RDU-{runId}`
6. Verifikasi popup `Used By` tampil
7. Klik ikon close pada popup `Used By`
