---
id: TC-FA-FACO-E2E-054-gating-link-used-by-create-dep-asset-class
title: "Manage accounting huruf Create melihat link Used By dan membuka popup Used By"
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

# Manage accounting huruf Create melihat link Used By dan membuka popup Used By

## Prerequisites
- Aktor: User `Rudi Hartono {runId}` (Manage accounting huruf Read dan Create).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-054-1: User `Rudi Hartono {runId}` dengan Global Role Manage accounting huruf Read dan Create (Read baseline terkunci), scope seluruh client.
  - DU-054-2: Account Code `CRU-{runId}`, Account Name `Fixed Assets – Machinery {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 2 Asset Class (DU-054-3, DU-054-4).
  - DU-054-3: Asset Class `Production Machinery {runId}`; Asset Cost `CRU-{runId}`.
  - DU-054-4: Asset Class `Packaging Machinery {runId}`; Asset Cost `CRU-{runId}`.

## Test Steps

### Link Used By tampil dan popup Used By terbuka
1. Buka halaman Settings > Accounting
2. Klik tab `Chart of Accounts`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi angka Used By `2` pada baris `CRU-{runId}` dapat diklik
5. Klik angka Used By `2` pada baris `CRU-{runId}`
6. Verifikasi popup `Used By` tampil
7. Klik ikon close pada popup `Used By`
