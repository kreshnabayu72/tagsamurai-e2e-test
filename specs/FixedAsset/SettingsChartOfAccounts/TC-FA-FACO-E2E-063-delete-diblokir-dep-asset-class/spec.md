---
id: TC-FA-FACO-E2E-063-delete-diblokir-dep-asset-class
title: "Delete akun yang dipakai Asset Class ditolak Guard 2"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [D-06, D-12, FACO-LOGIC-03b, "§3.8#r4", "§[F-FACO-05] Delete Account#r2", "§[F-FACO-05] Delete Account#r6", "§9.4.2#r17", "§9.4.2#r21"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  D-06: [5, 6, 7, 12]
  D-12: [23, 24, 25]
  FACO-LOGIC-03b: [5, 7, 9, 12, 14]
  "§3.8#r4": [3, 5]
  "§[F-FACO-05] Delete Account#r2": [5, 7, 9, 14]
  "§[F-FACO-05] Delete Account#r6": [23, 27, 28, 31]
  "§9.4.2#r17": [5, 9]
  "§9.4.2#r21": [23, 31]
anchor: []
coverage:
  web: automated
---

# Delete akun yang dipakai Asset Class ditolak Guard 2

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-063-1: Account Code `DLX-{runId}`, Account Name `Mesin Cetak {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-063-3), bukan nilai default company.
  - DU-063-2: Account Code `DLY-{runId}`, Account Name `Mesin Potong {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, dipakai 2 Asset Class (DU-063-3, DU-063-4), bukan nilai default company.
  - DU-063-3: Asset Class `Heavy Equipment {runId}`; Asset Cost `DLX-{runId}`, Accumulated Depreciation `DLY-{runId}`.
  - DU-063-4: Asset Class `Office Equipment {runId}`; Accumulated Depreciation `DLY-{runId}`.
  - Account Label yang diharapkan untuk DU-063-1 adalah `DLX-{runId} – Mesin Cetak {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-063-2 adalah `DLY-{runId} – Mesin Potong {runId}`, dari Account Code dan Account Name.

## Test Steps

### Delete akun yang dipakai 1 Asset Class ditolak Guard 2
1. Ketik Search `{runId}`, tekan Enter
2. Klik `⋯` pada baris `DLX-{runId}`
3. Verifikasi item `Delete` pada menu baris `DLX-{runId}` Enabled
4. Klik `Delete`
5. Verifikasi dialog `Cannot Delete Account` tampil
6. Verifikasi dialog memuat bullet `DLX-{runId} – Mesin Cetak {runId}`
7. Verifikasi dialog memuat kalimat `This account is used by 1 Asset Class and cannot be deleted.`
8. Klik `[OK]`
9. Verifikasi baris `DLX-{runId}` tetap ada di tabel

### Delete akun yang dipakai 2 Asset Class ditolak Guard 2
10. Klik `⋯` pada baris `DLY-{runId}`
11. Klik `Delete`
12. Verifikasi dialog memuat kalimat `This account is used by 2 Asset Classes and cannot be deleted.`
13. Klik `[OK]`
14. Verifikasi baris `DLY-{runId}` tetap ada di tabel

### Bulk Delete seluruh akun yang dipakai ditolak
15. Klik ikon Changelog
16. Ketik Search `{runId}` pada Changelog, tekan Enter
17. Catat jumlah entri Changelog yang tampil
18. Klik `✕` pada Changelog
19. Centang baris `DLX-{runId}`
20. Centang baris `DLY-{runId}`
21. Klik `Bulk Action`
22. Pilih `Delete`
23. Verifikasi dialog `Cannot Delete Accounts` tampil
24. Verifikasi dialog memuat bullet `DLX-{runId} – Mesin Cetak {runId}` pada kelompok `The following are in use and cannot be deleted:`
25. Verifikasi dialog memuat bullet `DLY-{runId} – Mesin Potong {runId}` pada kelompok `The following are in use and cannot be deleted:`
26. Klik `[OK]`
27. Verifikasi baris `DLX-{runId}` tetap ada di tabel
28. Verifikasi baris `DLY-{runId}` tetap ada di tabel
29. Klik ikon Changelog
30. Ketik Search `{runId}` pada Changelog, tekan Enter
31. Verifikasi jumlah entri Changelog sama dengan jumlah yang dicatat
32. Klik `✕` pada Changelog
33. Klik `×` pada Bulk Action bar
