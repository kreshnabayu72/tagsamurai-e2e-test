---
id: TC-FA-FACO-E2E-065-edit-function-terkunci-dep-asset-class
title: "Account Function terkunci selama akun dipakai Asset Class"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [C-03, FACO-LOGIC-04b, "§4.2b#r3", "§[F-FACO-02] Edit Account#r2", "§9.4.2#r6"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  C-03: [4, 11]
  FACO-LOGIC-04b: [4, 11]
  "§4.2b#r3": [7, 13]
  "§[F-FACO-02] Edit Account#r2": [4, 11]
  "§9.4.2#r6": [4, 5, 7, 11, 13]
anchor: []
coverage:
  web: automated
---

# Account Function terkunci selama akun dipakai Asset Class

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-065-1: Account Code `LKA-{runId}`, Account Name `Mesin Las {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-065-3).
  - DU-065-2: Account Code `LKB-{runId}`, Account Name `Mesin Bor {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, dipakai 2 Asset Class (DU-065-3, DU-065-4).
  - DU-065-3: Asset Class `Heavy Equipment {runId}`; Asset Cost `LKA-{runId}`, Accumulated Depreciation `LKB-{runId}`.
  - DU-065-4: Asset Class `Office Equipment {runId}`; Accumulated Depreciation `LKB-{runId}`.

## Test Steps

### Account Function terkunci karena dipakai 1 Asset Class
1. Ketik Search `{runId}`, tekan Enter
2. Klik `⋯` pada baris `LKA-{runId}`
3. Klik `Edit`
4. Verifikasi field Account Function Disabled
5. Verifikasi field Account Function berisi nilai tersimpan `Asset Cost`
6. Arahkan kursor ke field Account Function
7. Verifikasi alasan `Account Function can't be changed because this account is used by 1 Asset Class.` tersampaikan pada field Account Function yang Disabled
8. Klik `✕` pada form, form belum diubah

### Account Function terkunci karena dipakai 2 Asset Class
9. Klik `⋯` pada baris `LKB-{runId}`
10. Klik `Edit`
11. Verifikasi field Account Function Disabled
12. Arahkan kursor ke field Account Function
13. Verifikasi alasan `Account Function can't be changed because this account is used by 2 Asset Classes.` tersampaikan pada field Account Function yang Disabled
14. Klik `✕` pada form, form belum diubah
