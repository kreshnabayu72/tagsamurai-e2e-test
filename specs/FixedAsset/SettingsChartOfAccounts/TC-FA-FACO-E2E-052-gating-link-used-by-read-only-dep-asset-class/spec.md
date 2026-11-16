---
id: TC-FA-FACO-E2E-052-gating-link-used-by-read-only-dep-asset-class
title: "Read Only melihat link Used By dan membuka popup Used By"
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

# Read Only melihat link Used By dan membuka popup Used By

## Prerequisites
- Aktor: User `Hendra Kusuma {runId}` (Read Only).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-052-1: User `Hendra Kusuma {runId}` dengan access level Read Only, scope seluruh client.
  - DU-052-2: Account Code `ROU-{runId}`, Account Name `Fixed Assets – Vehicles {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 2 Asset Class (DU-052-3, DU-052-4).
  - DU-052-3: Asset Class `Light Vehicles {runId}`; Asset Cost `ROU-{runId}`.
  - DU-052-4: Asset Class `Heavy Vehicles {runId}`; Asset Cost `ROU-{runId}`.

## Test Steps

### Link Used By tampil dan popup Used By terbuka
1. Buka halaman Settings > Accounting
2. Klik tab `Chart of Accounts`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi angka Used By `2` pada baris `ROU-{runId}` dapat diklik
5. Klik angka Used By `2` pada baris `ROU-{runId}`
6. Verifikasi popup `Used By` tampil
7. Klik ikon close pada popup `Used By`
