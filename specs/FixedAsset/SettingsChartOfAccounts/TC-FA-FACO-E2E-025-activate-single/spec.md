---
id: TC-FA-FACO-E2E-025-activate-single
title: "Activate satu akun Inactive lewat Switch Status"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["D-14", "F-FACO-03", "FACO-LOGIC-02e", "§[F-FACO-03] Activate Account#p1", "L-03", "T-04"]
smoke: ["L-03", "T-04"]
dependsOn: []
trace:
  "D-14": [4, 7]
  "F-FACO-03": [7, 10]
  "FACO-LOGIC-02e": 7
  "§[F-FACO-03] Activate Account#p1": [6, 7, 13, 14]
  "L-03": [13, 14]
  "T-04": 6
anchor: [2]
coverage:
  web: automated
  android: automated
---

# Activate satu akun Inactive lewat Switch Status

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-025-1: akun Inactive dengan Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Used By `0`, Last Used in Journal `—`; Account Label `4-7001-{runId} – Gain on Disposal {runId}`.

## Test Steps

### Activate akun Inactive lewat Switch Status
1. Ketik Search `4-7001-{runId}`, tekan Enter
2. Verifikasi Switch Status pada baris `4-7001-{runId}` berstatus Inactive
3. Klik Switch Status pada baris `4-7001-{runId}`
4. Verifikasi bullet `4-7001-{runId} – Gain on Disposal {runId}` tampil pada dialog konfirmasi
5. Klik `[Activate]`
6. Verifikasi toast `Success, account has been activated.` tampil
7. Verifikasi Switch Status pada baris `4-7001-{runId}` berstatus Active
8. Muat ulang halaman
9. Ketik Search `4-7001-{runId}`, tekan Enter
10. Verifikasi Switch Status pada baris `4-7001-{runId}` tetap berstatus Active

### Satu entri Changelog untuk perubahan Status
11. Klik ikon Changelog
12. Ketik Search `4-7001-{runId}`, tekan Enter
13. Verifikasi tepat satu baris Changelog dengan Action `Edit` dan Field `Status`
14. Verifikasi baris itu memuat Old Value `Inactive` dan New Value `Active`
15. Klik `✕` pada modal Changelog
