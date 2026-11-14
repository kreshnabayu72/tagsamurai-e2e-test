---
id: TC-FA-FACO-E2E-079-bulk-delete-terekspor-dep-export-journal
title: "Bulk Delete atas akun yang pernah diekspor"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [D-09, D-12, "§[F-FACO-05] Delete Account#r6", "§9.4.2#r21", T-06]
smoke: [T-06]
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal"]
trace:
  D-09: [25, 26, 31, 32]
  D-12: [11, 13, 14]
  "§[F-FACO-05] Delete Account#r6": [11, 13, 14, 17]
  "§9.4.2#r21": [11, 17]
  T-06: 28
anchor: [6]
coverage:
  web: automated
---

# Bulk Delete atas akun yang pernah diekspor

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - M0 adalah bulan saat spec dijalankan. Periode ditulis dengan format `MMM YYYY`.
  - DU-079-1: Account Code `BDX1-{runId}`, Account Name `Plant Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, Last Used in Journal `M0 − 2 bulan`, ada di entitas aktor.
  - DU-079-2: Account Code `BDX2-{runId}`, Account Name `Tooling Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, Last Used in Journal `M0 − 3 bulan`, ada di entitas aktor.
  - DU-079-3: Account Code `BDX3-{runId}`, Account Name `Fixture Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, Last Used in Journal `M0 − 4 bulan`, ada di entitas aktor.
  - DU-079-4: Account Code `BDF1-{runId}`, Account Name `Scaffolding Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - Label akun pada bullet dialog dibentuk dari Account Code dan Account Name:
    - DU-079-1: `BDX1-{runId} – Plant Cost {runId}`, dari Account Code `BDX1-{runId}` dan Account Name `Plant Cost {runId}`.
    - DU-079-2: `BDX2-{runId} – Tooling Cost {runId}`, dari Account Code `BDX2-{runId}` dan Account Name `Tooling Cost {runId}`.
    - DU-079-3: `BDX3-{runId} – Fixture Cost {runId}`, dari Account Code `BDX3-{runId}` dan Account Name `Fixture Cost {runId}`.
    - DU-079-4: `BDF1-{runId} – Scaffolding Cost {runId}`, dari Account Code `BDF1-{runId}` dan Account Name `Scaffolding Cost {runId}`.
  - Keempat akun DU-079-1 sampai DU-079-4 adalah seluruh akun milik spec ini.

## Test Steps

### Bulk Delete atas akun yang semuanya pernah diekspor ditolak tanpa mengubah data
1. Klik ikon `Changelog` di toolbar
2. Ketik Search `{runId}`, tekan Enter
3. Catat jumlah baris hasil Search di modal Changelog
4. Klik `✕` pada modal Changelog
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi baris `BDX1-{runId}`, `BDX2-{runId}`, `BDX3-{runId}`, dan `BDF1-{runId}` tampil
7. Centang baris `BDX1-{runId}`
8. Centang baris `BDX2-{runId}`
9. Klik `Bulk Action`
10. Klik `Delete`
11. Verifikasi dialog `Cannot Delete Accounts` tampil dengan kelompok `The following were last used in a journal and cannot be deleted:` yang memuat bullet `BDX1-{runId} – Plant Cost {runId}` dan bullet `BDX2-{runId} – Tooling Cost {runId}`
12. Klik `[OK]`
13. Verifikasi baris `BDX1-{runId}` masih tampil
14. Verifikasi baris `BDX2-{runId}` masih tampil
15. Klik ikon `Changelog` di toolbar
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi jumlah baris hasil Search di modal Changelog sama dengan jumlah yang dicatat pada langkah 3, yaitu tidak ada entri log baru
18. Klik `✕` pada modal Changelog

### Bulk Delete campuran menghapus akun yang lolos dan melewati akun yang pernah diekspor
19. Hapus centang baris `BDX1-{runId}`
20. Hapus centang baris `BDX2-{runId}`
21. Centang baris `BDX3-{runId}`
22. Centang baris `BDF1-{runId}`
23. Klik `Bulk Action`
24. Klik `Delete`
25. Verifikasi dialog `Delete Accounts` tampil dengan kelompok `The following will be deleted:` yang memuat bullet `BDF1-{runId} – Scaffolding Cost {runId}`
26. Verifikasi dialog `Delete Accounts` memuat kelompok `The following will be skipped:` dengan bullet `BDX3-{runId} – Fixture Cost {runId}` beranotasi `(last used in a journal)`
27. Klik `[Continue]`
28. Verifikasi toast `Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company).` tampil
29. Muat ulang halaman
30. Ketik Search `{runId}`, tekan Enter
31. Verifikasi baris `BDX3-{runId}` masih tampil
32. Verifikasi baris `BDF1-{runId}` tidak tampil
