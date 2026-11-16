---
id: TC-FA-FACO-UI-144-dialog-blok-dep-preferences
title: "Dialog blok Delete untuk akun default company"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules:
  - D-06
  - D-09
  - D-12
smoke: []
dependsOn:
  - "Settings > Accounting > Preferences: akun default company"
  - "Asset Class: pemakaian akun pada field akun Asset Class (Used By)"
trace:
  D-06: [4, 5, 6, 11, 12]
  D-09: [21, 22, 23, 24, 25, 26, 27]
  D-12: [35, 36, 37, 38, 39, 40, 41]
coverage:
  web: automated
---

# Dialog blok Delete untuk akun default company

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-144-1: Akun, Account Code `4-7003`, Account Name `Gain on Disposal – Machinery`, Account Function `Gain on Disposal`, Status `Active`, Used By `0`, Last Used in Journal `—`, Setting default company `Default Gain on Disposal`.
  - DU-144-2: Akun, Account Code `4-7004`, Account Name `Gain and Loss on Disposal – Vehicles`, Account Function `Loss on Disposal`, Status `Active`, Used By `2`, Last Used in Journal `—`, Setting default company `Default Gain on Disposal, Default Loss on Disposal`.
  - DU-144-3: Akun, Account Code `6-2003`, Account Name `Capitalization Offset – Repairs`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `—`, Setting default company `Default Capitalization Offset`.
  - DU-144-4: Akun, Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Account Function `Depreciation Expense`, Status `Active`, Used By `0`, Last Used in Journal `—`.
  - Setting default company diurutkan mengikuti urutan setting pada tab Preferences: `Default Gain on Disposal` mendahului `Default Loss on Disposal`
- Kondisi:
  - K1: tabel berisi DU-144-1 sampai DU-144-4

## Test Steps

### Delete akun default company diblokir
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Klik `⋯` pada baris `4-7003`
3. Klik `Delete`
4. Verifikasi dialog berjudul `Cannot Delete Account` tampil
5. Verifikasi kalimat `This account is the default company account for Default Gain on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it.` tampil
6. Verifikasi tombol `[OK]` tampil pada dialog
7. Klik `[OK]`

### Delete akun yang sekaligus dipakai Asset Class dan default company
8. Tampilkan Tab Chart of Accounts dengan kondisi K1
9. Klik `⋯` pada baris `4-7004`
10. Klik `Delete`
11. Verifikasi dialog berjudul `Cannot Delete Account` tampil
12. Verifikasi kalimat pemakaian Asset Class `This account is used by 2 Asset Classes and cannot be deleted.` tampil lebih dahulu, lalu kalimat default company `This account is the default company account for Default Gain on Disposal, Default Loss on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it.`
13. Klik `[OK]`

### Bulk Delete campuran melewati akun default company
14. Tampilkan Tab Chart of Accounts dengan kondisi K1
15. Centang baris `5-6001`
16. Centang baris `4-7003`
17. Centang baris `6-2003`
18. Centang baris `4-7004`
19. Klik `Bulk Action`
20. Klik `Delete`
21. Verifikasi dialog berjudul `Delete Accounts` tampil
22. Verifikasi kalimat `The following are default company accounts and will be skipped:` tampil
23. Verifikasi bullet akun `4-7003` diikuti kalimat `This account is the default company account for Default Gain on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it.`
24. Verifikasi bullet akun `6-2003` diikuti kalimat `This account is the default company account for Default Capitalization Offset in Settings > Accounting > Preferences. Change the default there before deleting it.`
25. Verifikasi akun `4-7004` memuat kalimat pemakaian Asset Class `This account is used by 2 Asset Classes and cannot be deleted.` lebih dahulu, lalu kalimat default company `This account is the default company account for Default Gain on Disposal, Default Loss on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it.`
26. Verifikasi akun `4-7004` tampil pada kelompok `The following will be skipped:` beranotasi `(still in use)`
27. Verifikasi akun `4-7004` tidak tampil pada kelompok `The following are default company accounts and will be skipped:`
28. Klik `[Cancel]`

### Bulk Delete yang seluruh akunnya diblokir termasuk akun default company
29. Tampilkan Tab Chart of Accounts dengan kondisi K1
30. Centang baris `4-7003`
31. Centang baris `6-2003`
32. Centang baris `4-7004`
33. Klik `Bulk Action`
34. Klik `Delete`
35. Verifikasi dialog berjudul `Cannot Delete Accounts` tampil
36. Verifikasi kalimat `The following are default company accounts and cannot be deleted:` tampil
37. Verifikasi bullet akun `4-7003` diikuti kalimat `This account is the default company account for Default Gain on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it.`
38. Verifikasi bullet akun `6-2003` diikuti kalimat `This account is the default company account for Default Capitalization Offset in Settings > Accounting > Preferences. Change the default there before deleting it.`
39. Verifikasi kalimat `The following are in use and cannot be deleted:` tampil
40. Verifikasi akun `4-7004` memuat kalimat pemakaian Asset Class `This account is used by 2 Asset Classes and cannot be deleted.` lebih dahulu, lalu kalimat default company `This account is the default company account for Default Gain on Disposal, Default Loss on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it.`
41. Verifikasi tombol `[OK]` tampil pada dialog
42. Klik `[OK]`
