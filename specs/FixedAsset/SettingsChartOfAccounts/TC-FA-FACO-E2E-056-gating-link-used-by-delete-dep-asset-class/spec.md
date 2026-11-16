---
id: TC-FA-FACO-E2E-056-gating-link-used-by-delete-dep-asset-class
title: "Manage accounting huruf Delete melihat link Used By dan membuka popup Used By"
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

# Manage accounting huruf Delete melihat link Used By dan membuka popup Used By

## Prerequisites
- Aktor: User `Agus Salim {runId}` (Manage accounting huruf Read dan Delete).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-056-1: User `Agus Salim {runId}` dengan Global Role Manage accounting huruf Read dan Delete (Read baseline terkunci), scope seluruh client.
  - DU-056-2: Account Code `DLU-{runId}`, Account Name `Fixed Assets – Furniture {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 2 Asset Class (DU-056-3, DU-056-4).
  - DU-056-3: Asset Class `Meeting Furniture {runId}`; Asset Cost `DLU-{runId}`.
  - DU-056-4: Asset Class `Staff Furniture {runId}`; Asset Cost `DLU-{runId}`.

## Test Steps

### Link Used By tampil dan popup Used By terbuka
1. Buka halaman Settings > Accounting
2. Klik tab `Chart of Accounts`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi angka Used By `2` pada baris `DLU-{runId}` dapat diklik
5. Klik angka Used By `2` pada baris `DLU-{runId}`
6. Verifikasi popup `Used By` tampil
7. Klik ikon close pada popup `Used By`
