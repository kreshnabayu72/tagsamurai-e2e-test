---
id: TC-FA-FACO-E2E-027-bulk-activate
title: "Bulk Activate hanya memproses akun Inactive pada seleksi campuran"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["D-15", "F-FACO-03", "§4.1.1#p4", "§[F-FACO-03] Activate Account#p1", "EB-BLK-7", "T-04"]
smoke: ["T-04"]
dependsOn: []
trace:
  "D-15": [7, 11]
  "F-FACO-03": 11
  "§4.1.1#p4": [8, 11, 16]
  "§[F-FACO-03] Activate Account#p1": [10, 11, 14, 15]
  "EB-BLK-7": [8, 11, 16]
  "T-04": 10
anchor: [2]
coverage:
  web: automated
---

# Bulk Activate hanya memproses akun Inactive pada seleksi campuran

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-027-1: akun Inactive dengan Account Code `RA1-{runId}`, Account Name `Reaktivasi Peralatan Kantor {runId}`, Account Function `Asset Cost`, Used By `0`, Last Used in Journal `—`; Account Label `RA1-{runId} – Reaktivasi Peralatan Kantor {runId}`.
  - DU-027-2: akun Inactive dengan Account Code `RA2-{runId}`, Account Name `Reaktivasi Kendaraan Operasional {runId}`, Account Function `Asset Cost`, Used By `0`, Last Used in Journal `—`; Account Label `RA2-{runId} – Reaktivasi Kendaraan Operasional {runId}`.
  - DU-027-3: akun Active dengan Account Code `RA3-{runId}`, Account Name `Peralatan Gudang Aktif {runId}`, Account Function `Asset Cost`, Used By `0`, Last Used in Journal `—`; Account Label `RA3-{runId} – Peralatan Gudang Aktif {runId}`.

## Test Steps

### Bulk Activate pada seleksi berisi akun Inactive dan akun Active
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `RA1-{runId}`, `RA2-{runId}`, dan `RA3-{runId}` tampil
3. Centang baris `RA1-{runId}`
4. Klik `Select All (3 records)`
5. Klik `Bulk Action`
6. Klik `Activate`
7. Verifikasi dialog memuat bullet `RA1-{runId} – Reaktivasi Peralatan Kantor {runId}` dan bullet `RA2-{runId} – Reaktivasi Kendaraan Operasional {runId}`
8. Verifikasi dialog tidak memuat bullet `RA3-{runId} – Peralatan Gudang Aktif {runId}`
9. Klik `[Activate]`
10. Verifikasi toast `Success, account has been activated.` tampil
11. Verifikasi Switch Status pada baris `RA1-{runId}` dan baris `RA2-{runId}` berstatus Active

### Entri Changelog hanya untuk akun yang diproses
12. Klik ikon Changelog pada toolbar
13. Ketik Search `{runId}`, tekan Enter
14. Verifikasi setiap akun `RA1-{runId}` dan `RA2-{runId}` memiliki tepat satu baris Changelog dengan Action `Edit` dan Field `Status`
15. Verifikasi baris-baris Field `Status` itu memuat Old Value `Inactive` dan New Value `Active`
16. Verifikasi tidak ada baris Changelog dengan Account Code `RA3-{runId}` dan Field `Status`
17. Klik `✕` pada modal Changelog
