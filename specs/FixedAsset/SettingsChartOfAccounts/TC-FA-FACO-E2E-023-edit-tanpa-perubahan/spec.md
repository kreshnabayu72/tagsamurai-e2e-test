---
id: TC-FA-FACO-E2E-023-edit-tanpa-perubahan
title: "Save Edit Account tanpa perubahan nilai tidak mengubah data dan tidak menulis log"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§[F-FACO-02] Edit Account#r6", "§[F-FACO-02] Edit Account#r7", "§9.4.2#r7", "EB-FB-3@form-edit-account", "T-03"]
smoke: ["T-03"]
dependsOn: []
trace:
  "§[F-FACO-02] Edit Account#r6": [11, 12]
  "§[F-FACO-02] Edit Account#r7": 16
  "§9.4.2#r7": [10, 11, 12, 16]
  "EB-FB-3@form-edit-account": 16
  "T-03": 10
anchor: [6]
coverage:
  web: automated
  android: automated
---

# Save Edit Account tanpa perubahan nilai tidak mengubah data dan tidak menulis log

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-023-1: akun Active dengan Account Code `5-6003-{runId}`, Account Name `Depreciation Expense Workshop {runId}`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`.

## Test Steps

### Save Edit Account tanpa perubahan nilai
1. Klik ikon Changelog
2. Ketik Search `5-6003-{runId}`, tekan Enter
3. Catat jumlah baris Changelog yang tampil untuk Account Code `5-6003-{runId}`
4. Klik `✕` pada modal Changelog
5. Ketik Search `5-6003-{runId}`, tekan Enter
6. Verifikasi baris `5-6003-{runId}` tampil dengan Account Name `Depreciation Expense Workshop {runId}`
7. Klik `⋯` pada baris `5-6003-{runId}`
8. Klik `Edit`
9. Klik `[Save]` tanpa mengubah nilai field apa pun
10. Verifikasi toast `No changes to save.` tampil
11. Verifikasi Account Name pada baris `5-6003-{runId}` tetap `Depreciation Expense Workshop {runId}`
12. Verifikasi Account Function pada baris `5-6003-{runId}` tetap `Depreciation Expense`

### Tidak ada entri log baru
13. Klik ikon Changelog
14. Ketik Search `5-6003-{runId}`, tekan Enter
15. Catat jumlah baris Changelog yang tampil untuk Account Code `5-6003-{runId}`
16. Verifikasi jumlah baris Changelog itu sama dengan jumlah yang dicatat sebelum Save
17. Klik `✕` pada modal Changelog
