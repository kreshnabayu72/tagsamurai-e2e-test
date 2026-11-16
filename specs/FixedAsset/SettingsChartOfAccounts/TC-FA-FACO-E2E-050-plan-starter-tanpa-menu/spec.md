---
id: TC-FA-FACO-E2E-050-plan-starter-tanpa-menu
title: "Plan Starter (level None) tidak menyediakan Chart of Accounts dan data akun tidak dapat dilihat atau diekspor"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.4.2#r29", "§9.10#r1", "§9.10#b3"]
smoke: []
dependsOn: []
trace:
  "§9.4.2#r29": [4, 7, 10, 11]
  "§9.10#r1": [4, 7]
  "§9.10#b3": [10, 11]
anchor: [3, 6, 9]
coverage:
  web: automated
---

# Plan Starter (level None) tidak menyediakan Chart of Accounts dan data akun tidak dapat dilihat atau diekspor

## Prerequisites
- Aktor: Default User (Total Control permanen) pada entitas khusus berplan Starter yang tidak dipakai spec lain.
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-050-1: Entitas `Client Starter {runId}` dengan plan Starter, level fitur Chart of Accounts `None`.
  - DU-050-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, sudah ada di entitas `Client Starter {runId}`.

## Test Steps

### Menu Accounting tidak tersedia di plan Starter
1. Masuk sebagai Default User entitas `Client Starter {runId}`
2. Buka menu `Settings` di sidebar
3. Verifikasi menu `Settings` tampil di sidebar
4. Verifikasi menu `Accounting` Disabled dengan chip `Upgrade`
5. Klik menu `Accounting`
6. Verifikasi menu `Settings` tetap tampil di sidebar
7. Verifikasi halaman Accounting tidak terbuka dan tab `Chart of Accounts` tidak tampil

### Data akun tidak dapat dilihat atau diekspor selama menu Accounting tidak tersedia
8. Buka halaman Chart of Accounts lewat alamat langsung
9. Verifikasi menu `Settings` tampil di sidebar
10. Verifikasi tabel Account List tidak tampil sehingga akun Account Code `5-6001-{runId}` tidak dapat dilihat
11. Verifikasi kontrol `Download` untuk Account List tidak tersedia sehingga data akun tidak dapat diekspor
