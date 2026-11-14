---
id: TC-FA-FACO-E2E-086-bulk-delete-default-company-dep-preferences
title: "Bulk Delete campuran melewati akun default company"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [D-09, T-06]
smoke: [T-06]
dependsOn: ["Settings > Accounting > Preferences: akun default company"]
trace:
  D-09: [7, 8, 9, 14, 15]
  T-06: 11
anchor: [2]
coverage:
  web: automated
---
# Bulk Delete campuran melewati akun default company

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-086-1: Account Code `DDM1-{runId}`, Account Name `Offset Default {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, belum pernah diekspor, ada di entitas aktor.
  - DU-086-2: Account Code `DDM2-{runId}`, Account Name `Surplus Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, belum pernah diekspor, bukan nilai default company, ada di entitas aktor.
  - Label akun pada bullet dialog dibentuk dari Account Code dan Account Name:
    - DU-086-1: `DDM1-{runId} – Offset Default {runId}`, dari Account Code `DDM1-{runId}` dan Account Name `Offset Default {runId}`.
    - DU-086-2: `DDM2-{runId} – Surplus Cost {runId}`, dari Account Code `DDM2-{runId}` dan Account Name `Surplus Cost {runId}`.
  - Kedua akun DU-086-1 dan DU-086-2 adalah seluruh akun milik spec ini.
- Kondisi: Settings > Accounting > Preferences menyimpan akun DU-086-1 sebagai nilai `Default Capitalization Offset` untuk entitas aktor.

## Test Steps

### Bulk Delete campuran melewati akun default company dan menghapus akun yang lolos
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `DDM1-{runId}` dan `DDM2-{runId}` tampil
3. Centang baris `DDM1-{runId}`
4. Centang baris `DDM2-{runId}`
5. Klik `Bulk Action`
6. Klik `Delete`
7. Verifikasi dialog `Delete Accounts` tampil dengan kelompok `The following will be deleted:` yang memuat bullet `DDM2-{runId} – Surplus Cost {runId}`
8. Verifikasi dialog memuat kelompok `The following are default company accounts and will be skipped:` dengan bullet `DDM1-{runId} – Offset Default {runId}` yang diikuti kalimat `This account is the default company account for Default Capitalization Offset in Settings > Accounting > Preferences. Change the default there before deleting it.`
9. Verifikasi `[Setting Name]` pada kalimat itu berisi `Default Capitalization Offset`
10. Klik `[Continue]`
11. Verifikasi toast `Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company).` tampil

### Sesudah muat ulang akun default company masih ada dan akun yang lolos terhapus
12. Muat ulang halaman
13. Ketik Search `{runId}`, tekan Enter
14. Verifikasi baris `DDM1-{runId}` masih tampil di tabel
15. Verifikasi baris `DDM2-{runId}` tidak tampil di tabel
