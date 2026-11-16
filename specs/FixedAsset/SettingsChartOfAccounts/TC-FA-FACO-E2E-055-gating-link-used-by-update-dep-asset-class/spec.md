---
id: TC-FA-FACO-E2E-055-gating-link-used-by-update-dep-asset-class
title: "Manage accounting huruf Update melihat link Used By dan membuka popup Used By"
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

# Manage accounting huruf Update melihat link Used By dan membuka popup Used By

## Prerequisites
- Aktor: User `Dewi Anggraini {runId}` (Manage accounting huruf Read dan Update).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-055-1: User `Dewi Anggraini {runId}` dengan Global Role Manage accounting huruf Read dan Update (Read baseline terkunci), scope seluruh client.
  - DU-055-2: Account Code `UPU-{runId}`, Account Name `Fixed Assets – Equipment {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 2 Asset Class (DU-055-3, DU-055-4).
  - DU-055-3: Asset Class `Office Equipment {runId}`; Asset Cost `UPU-{runId}`.
  - DU-055-4: Asset Class `Laboratory Equipment {runId}`; Asset Cost `UPU-{runId}`.

## Test Steps

### Link Used By tampil dan popup Used By terbuka
1. Buka halaman Settings > Accounting
2. Klik tab `Chart of Accounts`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi angka Used By `2` pada baris `UPU-{runId}` dapat diklik
5. Klik angka Used By `2` pada baris `UPU-{runId}`
6. Verifikasi popup `Used By` tampil
7. Klik ikon close pada popup `Used By`
