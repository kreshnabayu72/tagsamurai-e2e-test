---
id: TC-FA-FACO-E2E-024-deactivate-single
title: "Deactivate satu akun yang lolos guard lewat Switch Status"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["D-01", "F-FACO-04", "§4.2f#b1", "§[F-FACO-04] Deactivate Account#b3", "L-03", "T-05"]
smoke: ["L-03", "T-05"]
dependsOn: []
trace:
  "D-01": [4, 7]
  "F-FACO-04": [7, 10]
  "§4.2f#b1": 4
  "§[F-FACO-04] Deactivate Account#b3": [6, 7, 10, 13, 14]
  "L-03": [13, 14]
  "T-05": 6
anchor: [2]
coverage:
  web: automated
  android: automated
---

# Deactivate satu akun yang lolos guard lewat Switch Status

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-024-1: akun Active dengan Account Code `5-6001-{runId}`, Account Name `Depreciation Expense Admin {runId}`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`; Account Label `5-6001-{runId} – Depreciation Expense Admin {runId}`.

## Test Steps

### Deactivate akun yang lolos guard lewat Switch Status
1. Ketik Search `5-6001-{runId}`, tekan Enter
2. Verifikasi Switch Status pada baris `5-6001-{runId}` berstatus Active
3. Klik Switch Status pada baris `5-6001-{runId}`
4. Verifikasi bullet `5-6001-{runId} – Depreciation Expense Admin {runId}` tampil pada dialog konfirmasi
5. Klik `[Deactivate]`
6. Verifikasi toast `Success, account has been deactivated.` tampil
7. Verifikasi Switch Status pada baris `5-6001-{runId}` berstatus Inactive
8. Muat ulang halaman
9. Ketik Search `5-6001-{runId}`, tekan Enter
10. Verifikasi Switch Status pada baris `5-6001-{runId}` tetap berstatus Inactive

### Satu entri Changelog untuk perubahan Status
11. Klik ikon Changelog
12. Ketik Search `5-6001-{runId}`, tekan Enter
13. Verifikasi tepat satu baris Changelog dengan Action `Edit` dan Field `Status`
14. Verifikasi baris itu memuat Old Value `Active` dan New Value `Inactive`
15. Klik `✕` pada modal Changelog
