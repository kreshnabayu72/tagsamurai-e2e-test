---
id: TC-FA-FACO-E2E-092-akun-hasil-import-dep-import
title: "Akun hasil Import menjalani Edit dan Delete seperti akun manual"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§11.1#r6", EB-XM-3]
smoke: []
dependsOn: ["Import: import akun dari berkas"]
trace:
  "§11.1#r6": 3
  EB-XM-3: [8, 9, 12, 16, 18, 19, 22]
anchor: [2]
coverage:
  web: automated
---
# Akun hasil Import menjalani Edit dan Delete seperti akun manual

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-092-1: Account Code `IMP1-{runId}`, Account Name `Imported Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, belum pernah diekspor, dibuat oleh Import dari berkas, ada di entitas aktor.
  - DU-092-2: Account Code `IMP2-{runId}`, Account Name `Imported Surplus {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, belum pernah diekspor, dibuat oleh Import dari berkas, ada di entitas aktor.
  - DU-092-3: Account Name baru untuk DU-092-1, yaitu `Imported Cost Revised {runId}`.
  - Label akun pada bullet dialog dibentuk dari Account Code dan Account Name:
    - DU-092-2: `IMP2-{runId} – Imported Surplus {runId}`, dari Account Code `IMP2-{runId}` dan Account Name `Imported Surplus {runId}`.
  - Ketiga data DU-092-1 sampai DU-092-3 adalah seluruh akun milik spec ini.

## Test Steps

### Akun hasil Import menjalani Edit dengan hasil yang sama seperti akun manual
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `IMP1-{runId}` dan `IMP2-{runId}` tampil
3. Verifikasi toolbar tab Chart of Accounts memuat ikon `Search`, `Filter`, `Download`, dan `Changelog` serta tombol `[+ Account]`, tanpa kontrol upload atau import berkas
4. Klik `⋯` pada baris `IMP1-{runId}`
5. Klik `Edit`
6. Ganti isi field Account Name dengan `Imported Cost Revised {runId}`
7. Klik `[Save]`
8. Verifikasi toast `Success, account has been updated.` tampil
9. Verifikasi baris `IMP1-{runId}` menampilkan Account Name `Imported Cost Revised {runId}`
10. Klik ikon `Changelog` di toolbar
11. Ketik Search `IMP1-{runId}`, tekan Enter
12. Verifikasi baris Changelog dengan Action `Edit`, Account Code `IMP1-{runId}`, Field `Account Name`, Old Value `Imported Cost {runId}`, dan New Value `Imported Cost Revised {runId}` tampil
13. Klik `✕` pada modal Changelog

### Akun hasil Import menjalani Delete dengan hasil yang sama seperti akun manual
14. Klik `⋯` pada baris `IMP2-{runId}`
15. Klik `Delete`
16. Verifikasi dialog `Delete Account` tampil dengan bullet `IMP2-{runId} – Imported Surplus {runId}`
17. Klik `[Delete]` pada dialog konfirmasi
18. Verifikasi toast `Success, account has been deleted.` tampil
19. Verifikasi baris `IMP2-{runId}` tidak tampil
20. Klik ikon `Changelog` di toolbar
21. Ketik Search `IMP2-{runId}`, tekan Enter
22. Verifikasi baris Changelog dengan Action `Delete`, Account Code `IMP2-{runId}`, Field `Account Code`, Old Value `IMP2-{runId}`, dan New Value `—` tampil
23. Klik `✕` pada modal Changelog
