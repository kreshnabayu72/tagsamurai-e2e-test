---
id: TC-FA-FACO-E2E-031-status-usang-idempotent
title: "Activate atau Deactivate atas akun yang sudah berstatus target tidak mengubah data"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§7.3#b5", "§[F-FACO-03] Activate Account#r2", "§[F-FACO-03] Activate Account#r3", "§[F-FACO-04] Deactivate Account#r3", "§9.4.2#r10", "§9.4.2#r13"]
smoke: []
dependsOn: []
trace:
  "§7.3#b5": [7, 15]
  "§[F-FACO-03] Activate Account#r2": [7, 10]
  "§[F-FACO-03] Activate Account#r3": 7
  "§[F-FACO-04] Deactivate Account#r3": [15, 18]
  "§9.4.2#r10": [7, 10]
  "§9.4.2#r13": [15, 18]
anchor: [2, 3]
coverage:
  web: automated
---

# Activate atau Deactivate atas akun yang sudah berstatus target tidak mengubah data

## Prerequisites
- Aktor: Total Control. Aktor lain yang memicu perubahan status: Admin B, Total Control, seluruh client.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-031-1: akun Inactive dengan Account Code `4-7004-{runId}`, Account Name `Gain on Disposal Cabang Barat {runId}`, Account Function `Gain on Disposal`, Used By `0`, Last Used in Journal `—`; diaktifkan Admin B setelah aktor membuka dialog konfirmasi Activate dan sebelum aktor mengonfirmasinya.
  - DU-031-2: akun Active dengan Account Code `5-6011-{runId}`, Account Name `Depreciation Expense Cabang Barat {runId}`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`; dinonaktifkan Admin B setelah aktor membuka dialog konfirmasi Deactivate dan sebelum aktor mengonfirmasinya.

## Test Steps

### Activate atas akun yang sudah Active
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi Switch Status pada baris `4-7004-{runId}` berstatus Inactive
3. Verifikasi Switch Status pada baris `5-6011-{runId}` berstatus Active
4. Klik Switch Status pada baris `4-7004-{runId}`, sehingga dialog konfirmasi Activate terbuka
5. Admin B mengaktifkan akun `4-7004-{runId}`
6. Klik `[Activate]`
7. Verifikasi Switch Status pada baris `4-7004-{runId}` berstatus Active
8. Klik ikon Changelog pada toolbar
9. Ketik Search `4-7004-{runId}`, tekan Enter
10. Verifikasi tepat satu baris Changelog dengan Field `Status`
11. Klik `✕` pada modal Changelog

### Deactivate atas akun yang sudah Inactive
12. Klik Switch Status pada baris `5-6011-{runId}`, sehingga dialog konfirmasi Deactivate terbuka
13. Admin B menonaktifkan akun `5-6011-{runId}`
14. Klik `[Deactivate]`
15. Verifikasi Switch Status pada baris `5-6011-{runId}` berstatus Inactive
16. Klik ikon Changelog pada toolbar
17. Ketik Search `5-6011-{runId}`, tekan Enter
18. Verifikasi tepat satu baris Changelog dengan Field `Status`
19. Klik `✕` pada modal Changelog
