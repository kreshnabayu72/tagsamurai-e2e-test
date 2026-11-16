---
id: TC-FA-FATR-BE-119-aturan-accounting-dep-accounting
title: "Post Accounting pada Disposal tanpa approval"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§9.2#b531"]
smoke: []
dependsOn:
  - "Accounting: Post dan review Cost Center"
trace:
  "§9.2#b531": [3, 5]
---

# Post Accounting pada Disposal tanpa approval

## Prerequisites
- Aktor: Total Control sebagai pengaju. `Sari Wulandari {runId}` sebagai pelaksana Execute. `Hendra Saputra {runId}` sebagai pengguna Accounting.
- Data:
  - DU-119-1: Category `Peralatan Pabrik {runId} > Mesin Potong {runId}`, Require approval `OFF` untuk transaksi pelepasan aset.
  - DU-119-2: aset `Mesin Potong Unit 1 {runId}` di Category `Peralatan Pabrik {runId} > Mesin Potong {runId}`, dengan data akuntansi.
  - DU-119-3: user `Hendra Saputra {runId}`, Accounting, cakupan seluruh entitas.
  - DU-119-4: user `Sari Wulandari {runId}`, pelaksana Execute pelepasan aset, cakupan seluruh entitas.- Kondisi:
  - Accounting & Depreciation aktif pada paket entitas.

## Test Steps

### Pelepasan aset tanpa approval tetap di-Post oleh Accounting
1. Total Control mengajukan pelepasan aset `Mesin Potong Unit 1 {runId}` di Category `Peralatan Pabrik {runId} > Mesin Potong {runId}` yang Require approval-nya `OFF`, dengan jenis pelepasan `Scrap` dan Reason `Mesin potong rusak berat dan tidak ekonomis diperbaiki`
2. `Sari Wulandari {runId}` melakukan Execute atas pelepasan aset `Mesin Potong Unit 1 {runId}`
3. Verifikasi pelepasan aset `Mesin Potong Unit 1 {runId}` sesudah Execute berstatus Executed dan menunggu Post, walaupun Require approval `OFF`
4. `Hendra Saputra {runId}` melakukan Post atas pelepasan aset `Mesin Potong Unit 1 {runId}`
5. Verifikasi Post oleh pengguna Accounting `Hendra Saputra {runId}` atas pelepasan aset `Mesin Potong Unit 1 {runId}` diterima walaupun Require approval `OFF`
