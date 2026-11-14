---
id: TC-FA-FACO-E2E-050-plan-starter-tanpa-menu
title: "Plan Starter (level None) tidak menyediakan Chart of Accounts"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["§9.4.2#r29", "§9.10#r1"]
smoke: []
dependsOn: []
trace:
  "§9.4.2#r29": [4, 7]
  "§9.10#r1": [4, 7]
anchor: [3, 6]
coverage:
  web: automated
---

# Plan Starter (level None) tidak menyediakan Chart of Accounts

## Prerequisites
- Aktor: Default User (Total Control permanen) pada entitas khusus berplan Starter yang tidak dipakai spec lain.
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-050-1: Entitas `Client Starter {runId}` dengan plan Starter, level fitur Chart of Accounts `None`.

## Test Steps

### Menu Accounting tidak tersedia di plan Starter
1. Masuk sebagai Default User entitas `Client Starter {runId}`
2. Buka menu `Settings` di sidebar
3. Verifikasi menu `Settings` tampil di sidebar
4. Verifikasi menu `Accounting` Disabled dengan chip `Upgrade`
5. Klik menu `Accounting`
6. Verifikasi menu `Settings` tetap tampil di sidebar
7. Verifikasi halaman Accounting tidak terbuka dan tab `Chart of Accounts` tidak tampil
