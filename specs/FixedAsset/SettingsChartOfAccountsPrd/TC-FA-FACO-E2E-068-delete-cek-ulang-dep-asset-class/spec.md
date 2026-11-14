---
id: TC-FA-FACO-E2E-068-delete-cek-ulang-dep-asset-class
title: "Akun menjadi dipakai antara dialog Delete dibuka dan Confirm"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["§7.3#b3", "§7.3#b6", "§7.3#b7", "§[F-FACO-05] Delete Account#r15", "§[F-FACO-05] Delete Account#r16", "§9.4.2#r22"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  "§7.3#b3": [6, 9]
  "§7.3#b6": [18, 19, 20, 21, 24, 26]
  "§7.3#b7": [35, 36, 37, 39, 40, 43, 45]
  "§[F-FACO-05] Delete Account#r15": [6, 7, 8, 9, 11]
  "§[F-FACO-05] Delete Account#r16": [18, 19, 20, 21, 24, 26]
  "§9.4.2#r22": [6, 11, 35]
anchor: []
coverage:
  web: automated
---

# Akun menjadi dipakai antara dialog Delete dibuka dan Confirm

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-068-1: Account Code `RDA-{runId}`, Account Name `Cabang Medan {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, belum dipakai Asset Class saat dialog dibuka, bukan nilai default company.
  - DU-068-2: Account Code `RDB-{runId}`, Account Name `Cabang Padang {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class, bukan nilai default company.
  - DU-068-3: Account Code `RDC-{runId}`, Account Name `Cabang Pekanbaru {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, belum dipakai Asset Class saat dialog dibuka, bukan nilai default company.
  - DU-068-4: Account Code `RDD-{runId}`, Account Name `Cabang Jambi {runId}`, Account Function `Gain on Disposal`, Status Active, Last Used in Journal `—`, belum dipakai Asset Class saat dialog dibuka, bukan nilai default company.
  - DU-068-5: Account Code `RDE-{runId}`, Account Name `Cabang Batam {runId}`, Account Function `Loss on Disposal`, Status Active, Last Used in Journal `—`, belum dipakai Asset Class saat dialog dibuka, bukan nilai default company.
  - DU-068-6: Asset Class `Armada Cabang {runId}`, belum memakai akun DU-068-1 sampai DU-068-5.
  - Account Label yang diharapkan untuk DU-068-4 adalah `RDD-{runId} – Cabang Jambi {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-068-5 adalah `RDE-{runId} – Cabang Batam {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-068-1 adalah `RDA-{runId} – Cabang Medan {runId}`, dari Account Code dan Account Name.

## Test Steps

### Single: akun menjadi dipakai antara dialog Delete dibuka dan Confirm
1. Ketik Search `{runId}`, tekan Enter
2. Klik `⋯` pada baris `RDA-{runId}`
3. Klik `Delete`
4. Asset Class `Armada Cabang {runId}` memakai akun `RDA-{runId}` pada field Asset Cost
5. Klik `[Delete]` pada dialog
6. Verifikasi dialog `Cannot Delete Account` tampil
7. Verifikasi dialog memuat bullet `RDA-{runId} – Cabang Medan {runId}`
8. Verifikasi dialog memuat kalimat `This account is used by 1 Asset Class and cannot be deleted.`
9. Verifikasi tidak ada toast yang tampil
10. Klik `[OK]`
11. Verifikasi baris `RDA-{runId}` tetap ada di tabel

### Bulk: sebagian akun menjadi dipakai tetap diproses sebagian
12. Centang baris `RDB-{runId}`
13. Centang baris `RDC-{runId}`
14. Klik `Bulk Action`
15. Pilih `Delete`
16. Asset Class `Armada Cabang {runId}` memakai akun `RDC-{runId}` pada field Depreciation Expense
17. Klik `[Delete]` pada dialog
18. Verifikasi toast `Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company).` tampil
19. Verifikasi baris `RDC-{runId}` tetap ada di tabel
20. Verifikasi baris `RDB-{runId}` tidak ada lagi di tabel
21. Verifikasi dialog `Cannot Delete Accounts` tidak tampil
22. Klik ikon Changelog
23. Ketik Search `RDB-{runId}` pada Changelog, tekan Enter
24. Verifikasi Changelog memuat entri Action `Delete` untuk Account Code `RDB-{runId}`
25. Ganti isi Search Changelog dengan `RDC-{runId}`, tekan Enter
26. Verifikasi Changelog tidak memuat entri Action `Delete` untuk Account Code `RDC-{runId}`
27. Klik `✕` pada Changelog

### Bulk: seluruh akun menjadi dipakai ditolak seluruhnya
28. Centang baris `RDD-{runId}`
29. Centang baris `RDE-{runId}`
30. Klik `Bulk Action`
31. Pilih `Delete`
32. Asset Class `Armada Cabang {runId}` memakai akun `RDD-{runId}` pada field Gain on Disposal
33. Asset Class `Armada Cabang {runId}` memakai akun `RDE-{runId}` pada field Loss on Disposal
34. Klik `[Delete]` pada dialog
35. Verifikasi dialog `Cannot Delete Accounts` tampil
36. Verifikasi dialog memuat bullet `RDD-{runId} – Cabang Jambi {runId}` pada kelompok `The following are in use and cannot be deleted:`
37. Verifikasi dialog memuat bullet `RDE-{runId} – Cabang Batam {runId}` pada kelompok `The following are in use and cannot be deleted:`
38. Klik `[OK]`
39. Verifikasi baris `RDD-{runId}` tetap ada di tabel
40. Verifikasi baris `RDE-{runId}` tetap ada di tabel
41. Klik ikon Changelog
42. Ketik Search `RDD-{runId}` pada Changelog, tekan Enter
43. Verifikasi Changelog tidak memuat entri Action `Delete` untuk Account Code `RDD-{runId}`
44. Ganti isi Search Changelog dengan `RDE-{runId}`, tekan Enter
45. Verifikasi Changelog tidak memuat entri Action `Delete` untuk Account Code `RDE-{runId}`
46. Klik `✕` pada Changelog
47. Klik `×` pada Bulk Action bar
