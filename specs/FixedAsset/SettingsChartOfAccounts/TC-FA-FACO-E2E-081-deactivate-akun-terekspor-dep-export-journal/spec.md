---
id: TC-FA-FACO-E2E-081-deactivate-akun-terekspor-dep-export-journal
title: "Akun terekspor dinonaktifkan dan tetap tersimpan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [C-01, D-05, FACO-LOGIC-03a, "§9.7#r24"]
smoke: []
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal"]
trace:
  C-01: [4, 12, 14]
  D-05: [10, 11, 12]
  FACO-LOGIC-03a: [4, 12, 14]
  "§9.7#r24": 7
coverage:
  web: automated
---

# Akun terekspor dinonaktifkan dan tetap tersimpan

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - M0 adalah bulan saat spec dijalankan. Periode ditulis dengan format `MMM YYYY`.
  - DU-081-1: Account Code `DXA1-{runId}`, Account Name `Retired Fleet Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, Last Used in Journal `M0 − 2 bulan`, ada di entitas aktor.
  - Label akun pada bullet dialog adalah `DXA1-{runId} – Retired Fleet Cost {runId}`, dari Account Code `DXA1-{runId}` dan Account Name `Retired Fleet Cost {runId}`.

## Test Steps

### Akun terekspor yang Active dinonaktifkan lalu Delete tetap ditolak tanpa saran Deactivate
1. Ketik Search `DXA1-{runId}`, tekan Enter
2. Klik switch Status pada baris `DXA1-{runId}`
3. Klik `[Deactivate]` pada dialog konfirmasi
4. Verifikasi Status baris `DXA1-{runId}` menjadi `Inactive`
5. Muat ulang halaman
6. Ketik Search `DXA1-{runId}`, tekan Enter
7. Verifikasi Last Used in Journal baris `DXA1-{runId}` tetap bernilai periode `M0 − 2 bulan` yang ditulis `MMM YYYY`, yaitu tidak berubah sesudah Deactivate
8. Klik `⋯` pada baris `DXA1-{runId}`
9. Klik `Delete`
10. Verifikasi dialog `Cannot Delete Account` tampil dengan bullet `DXA1-{runId} – Retired Fleet Cost {runId}`
11. Verifikasi `[Month Year]` pada kalimat pertama dialog berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY`
12. Verifikasi kalimat saran `Deactivate it instead.` tidak tampil, karena akun sudah Inactive
13. Klik `[OK]`
14. Verifikasi baris `DXA1-{runId}` masih tampil di tabel dengan Status `Inactive`
