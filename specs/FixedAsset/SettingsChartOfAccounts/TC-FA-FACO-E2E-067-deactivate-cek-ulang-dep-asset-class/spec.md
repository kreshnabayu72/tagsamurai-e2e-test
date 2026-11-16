---
id: TC-FA-FACO-E2E-067-deactivate-cek-ulang-dep-asset-class
title: "Akun menjadi dipakai antara dialog Deactivate dibuka dan Confirm"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§7.3#b3", "§7.3#b6", "§7.3#b7", "§[F-FACO-04] Deactivate Account#r7", "§[F-FACO-04] Deactivate Account#r8", "§9.4.2#r12"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  "§7.3#b3": [5, 7]
  "§7.3#b6": [16, 17, 18, 19, 22, 24]
  "§7.3#b7": [33, 34, 35, 37, 38, 41, 43]
  "§[F-FACO-04] Deactivate Account#r7": [5, 6, 7, 9]
  "§[F-FACO-04] Deactivate Account#r8": [16, 17, 18, 19, 22, 24]
  "§9.4.2#r12": [5, 9, 33]
anchor: []
coverage:
  web: automated
---

# Akun menjadi dipakai antara dialog Deactivate dibuka dan Confirm

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-067-1: Account Code `RCA-{runId}`, Account Name `Lini Produksi A {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, belum dipakai Asset Class saat dialog dibuka.
  - DU-067-2: Account Code `RCB-{runId}`, Account Name `Lini Produksi B {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-067-3: Account Code `RCC-{runId}`, Account Name `Lini Produksi C {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, belum dipakai Asset Class saat dialog dibuka.
  - DU-067-4: Account Code `RCD-{runId}`, Account Name `Lini Produksi D {runId}`, Account Function `Gain on Disposal`, Status Active, Last Used in Journal `—`, belum dipakai Asset Class saat dialog dibuka.
  - DU-067-5: Account Code `RCE-{runId}`, Account Name `Lini Produksi E {runId}`, Account Function `Loss on Disposal`, Status Active, Last Used in Journal `—`, belum dipakai Asset Class saat dialog dibuka.
  - DU-067-6: Asset Class `Armada Perakitan {runId}`, belum memakai akun DU-067-1 sampai DU-067-5.
  - Account Label yang diharapkan untuk DU-067-1 adalah `RCA-{runId} – Lini Produksi A {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-067-4 adalah `RCD-{runId} – Lini Produksi D {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-067-5 adalah `RCE-{runId} – Lini Produksi E {runId}`, dari Account Code dan Account Name.
  - Bullet beranotasi yang diharapkan untuk DU-067-4 adalah `RCD-{runId} – Lini Produksi D {runId} (still in use)`, dari Account Label dan anotasi untuk akun yang dipakai Asset Class.
  - Bullet beranotasi yang diharapkan untuk DU-067-5 adalah `RCE-{runId} – Lini Produksi E {runId} (still in use)`, dari Account Label dan anotasi untuk akun yang dipakai Asset Class.

## Test Steps

### Single: akun menjadi dipakai antara dialog Deactivate dibuka dan Confirm
1. Ketik Search `{runId}`, tekan Enter
2. Klik switch Status baris `RCA-{runId}`
3. Asset Class `Armada Perakitan {runId}` memakai akun `RCA-{runId}` pada field Asset Cost
4. Klik `[Deactivate]` pada dialog
5. Verifikasi dialog `Cannot Deactivate Account` tampil
6. Verifikasi dialog memuat bullet `RCA-{runId} – Lini Produksi A {runId}`
7. Verifikasi tidak ada toast yang tampil
8. Klik `[OK]`
9. Verifikasi switch Status baris `RCA-{runId}` tetap Active

### Bulk: sebagian akun menjadi dipakai tetap diproses sebagian
10. Centang baris `RCB-{runId}`
11. Centang baris `RCC-{runId}`
12. Klik `Bulk Action`
13. Pilih `Deactivate`
14. Asset Class `Armada Perakitan {runId}` memakai akun `RCC-{runId}` pada field Depreciation Expense
15. Klik `[Deactivate]` pada dialog
16. Verifikasi toast `Success, account has been deactivated. Some items were skipped (still in use).` tampil
17. Verifikasi switch Status baris `RCB-{runId}` Inactive
18. Verifikasi switch Status baris `RCC-{runId}` tetap Active
19. Verifikasi dialog `Cannot Deactivate Accounts` tidak tampil
20. Klik ikon Changelog
21. Ketik Search `RCB-{runId}` pada Changelog, tekan Enter
22. Verifikasi Changelog memuat entri Field `Status` dengan Old Value `Active` dan New Value `Inactive` untuk `RCB-{runId}`
23. Ganti isi Search Changelog dengan `RCC-{runId}`, tekan Enter
24. Verifikasi Changelog tidak memuat entri Field `Status` untuk `RCC-{runId}`
25. Klik `✕` pada Changelog

### Bulk: seluruh akun menjadi dipakai ditolak seluruhnya
26. Centang baris `RCD-{runId}`
27. Centang baris `RCE-{runId}`
28. Klik `Bulk Action`
29. Pilih `Deactivate`
30. Asset Class `Armada Perakitan {runId}` memakai akun `RCD-{runId}` pada field Gain on Disposal
31. Asset Class `Armada Perakitan {runId}` memakai akun `RCE-{runId}` pada field Loss on Disposal
32. Klik `[Deactivate]` pada dialog
33. Verifikasi dialog `Cannot Deactivate Accounts` tampil
34. Verifikasi dialog memuat bullet `RCD-{runId} – Lini Produksi D {runId} (still in use)`
35. Verifikasi dialog memuat bullet `RCE-{runId} – Lini Produksi E {runId} (still in use)`
36. Klik `[OK]`
37. Verifikasi switch Status baris `RCD-{runId}` tetap Active
38. Verifikasi switch Status baris `RCE-{runId}` tetap Active
39. Klik ikon Changelog
40. Ketik Search `RCD-{runId}` pada Changelog, tekan Enter
41. Verifikasi Changelog tidak memuat entri Field `Status` untuk `RCD-{runId}`
42. Ganti isi Search Changelog dengan `RCE-{runId}`, tekan Enter
43. Verifikasi Changelog tidak memuat entri Field `Status` untuk `RCE-{runId}`
44. Klik `✕` pada Changelog
45. Klik `×` pada Bulk Action bar
