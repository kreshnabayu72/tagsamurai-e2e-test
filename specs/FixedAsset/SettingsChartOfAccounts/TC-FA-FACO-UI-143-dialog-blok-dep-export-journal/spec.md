---
id: TC-FA-FACO-UI-143-dialog-blok-dep-export-journal
title: "Dialog blok Delete untuk akun yang pernah diekspor"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules:
  - D-05
  - D-09
  - D-12
smoke: []
dependsOn:
  - "Export Journal: export jurnal yang mengisi Last Used in Journal"
  - "Asset Class: pemakaian akun pada field akun Asset Class (Used By)"
trace:
  D-05: [4, 5, 6, 7, 12, 13, 14, 19, 20, 21, 26, 27]
  D-09: [34, 35, 36]
  D-12: [43, 44]
coverage:
  web: automated
---

# Dialog blok Delete untuk akun yang pernah diekspor

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-143-1: Akun, Account Code `6-2001`, Account Name `Repairs & Maintenance Expense`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `Aug 2026`.
  - DU-143-2: Akun, Account Code `1-1001`, Account Name `Fixed Assets – Equipment`, Account Function `Asset Cost`, Status `Active`, Used By `3`, Last Used in Journal `Oct 2026`.
  - DU-143-3: Akun, Account Code `1-2002`, Account Name `Accumulated Depreciation – Vehicles`, Account Function `Accumulated Depreciation`, Status `Active`, Used By `1`, Last Used in Journal `Sep 2026`.
  - DU-143-4: Akun, Account Code `1-1002`, Account Name `Equipment – Legacy Code`, Account Function `Asset Cost`, Status `Inactive`, Used By `0`, Last Used in Journal `Mar 2025`.
  - DU-143-5: Akun, Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Account Function `Depreciation Expense`, Status `Active`, Used By `0`, Last Used in Journal `—`.
  - Kalimat Guard 1 yang diharapkan untuk DU-143-1: `This account was last used in a journal in Aug 2026. Deleting it may break historical records.`, dari Last Used in Journal `Aug 2026`
  - Kalimat Guard 1 yang diharapkan untuk DU-143-2: `This account was last used in a journal in Oct 2026. Deleting it may break historical records.`, dari Last Used in Journal `Oct 2026`
  - Kalimat Guard 1 yang diharapkan untuk DU-143-3: `This account was last used in a journal in Sep 2026. Deleting it may break historical records.`, dari Last Used in Journal `Sep 2026`
  - Kalimat Guard 1 yang diharapkan untuk DU-143-4: `This account was last used in a journal in Mar 2025. Deleting it may break historical records.`, dari Last Used in Journal `Mar 2025`
- Kondisi:
  - K1: tabel berisi DU-143-1 sampai DU-143-5

## Test Steps

### Delete akun terekspor yang Active dan tidak diblokir menyarankan Deactivate
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Klik `⋯` pada baris `6-2001`
3. Klik `Delete`
4. Verifikasi dialog berjudul `Cannot Delete Account` tampil
5. Verifikasi kalimat `This account was last used in a journal in Aug 2026. Deleting it may break historical records.` tampil
6. Verifikasi kalimat `Deactivate it instead.` tampil
7. Verifikasi tombol `[OK]` tampil pada dialog
8. Klik `[OK]`

### Delete akun terekspor yang dipakai beberapa Asset Class
9. Tampilkan Tab Chart of Accounts dengan kondisi K1
10. Klik `⋯` pada baris `1-1001`
11. Klik `Delete`
12. Verifikasi kalimat `This account was last used in a journal in Oct 2026. Deleting it may break historical records.` tampil
13. Verifikasi kalimat `This account is used by 3 Asset Classes and cannot be deleted.` tampil
14. Verifikasi kalimat `Deactivate it instead.` tidak tampil
15. Klik `[OK]`

### Delete akun terekspor yang dipakai satu Asset Class
16. Tampilkan Tab Chart of Accounts dengan kondisi K1
17. Klik `⋯` pada baris `1-2002`
18. Klik `Delete`
19. Verifikasi kalimat `This account was last used in a journal in Sep 2026. Deleting it may break historical records.` tampil
20. Verifikasi kalimat `This account is used by 1 Asset Class and cannot be deleted.` tampil
21. Verifikasi kalimat `Deactivate it instead.` tidak tampil
22. Klik `[OK]`

### Delete akun terekspor yang sudah Inactive tanpa baris ketiga
23. Tampilkan Tab Chart of Accounts dengan kondisi K1
24. Klik `⋯` pada baris `1-1002`
25. Klik `Delete`
26. Verifikasi kalimat `This account was last used in a journal in Mar 2025. Deleting it may break historical records.` tampil
27. Verifikasi kalimat `Deactivate it instead.` tidak tampil
28. Klik `[OK]`

### Bulk Delete campuran melewati akun terekspor
29. Tampilkan Tab Chart of Accounts dengan kondisi K1
30. Centang baris `5-6001`
31. Centang baris `6-2001`
32. Klik `Bulk Action`
33. Klik `Delete`
34. Verifikasi dialog berjudul `Delete Accounts` tampil
35. Verifikasi kalimat `The following will be skipped:` tampil
36. Verifikasi akun yang dilewati karena terekspor diberi anotasi `(last used in a journal)`
37. Klik `[Cancel]`

### Bulk Delete yang seluruh akunnya terekspor
38. Tampilkan Tab Chart of Accounts dengan kondisi K1
39. Centang baris `6-2001`
40. Centang baris `1-1002`
41. Klik `Bulk Action`
42. Klik `Delete`
43. Verifikasi dialog berjudul `Cannot Delete Accounts` tampil
44. Verifikasi kalimat `The following were last used in a journal and cannot be deleted:` tampil
45. Klik `[OK]`
