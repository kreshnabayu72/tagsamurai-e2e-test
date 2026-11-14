---
id: TC-FA-FACO-UI-141-dialog-blok-dep-asset-class
title: "Dialog blok dan konfirmasi campuran untuk akun yang dipakai Asset Class"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules:
  - D-03
  - D-04
  - D-06
  - D-09
  - D-12
smoke: []
dependsOn:
  - "Asset Class: pemakaian akun pada field akun Asset Class (Used By)"
trace:
  D-03: [26, 27, 28, 29, 30, 31, 32]
  D-04: [3, 4, 5, 7, 10, 17, 18, 19]
  D-06: [37, 38, 39, 44]
  D-09: [51, 52, 53, 54, 55, 56, 57]
  D-12: [64, 65, 66]
coverage:
  web: automated
---

# Dialog blok dan konfirmasi campuran untuk akun yang dipakai Asset Class

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-141-1: Akun, Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Account Function `Depreciation Expense`, Status `Active`, Used By `0`, Last Used in Journal `—`.
  - DU-141-2: Akun, Account Code `5-6002`, Account Name `Depreciation Expense – Warehouse`, Account Function `Depreciation Expense`, Status `Active`, Used By `1`, Last Used in Journal `—`.
  - DU-141-3: Akun, Account Code `5-6003`, Account Name `Depreciation Expense – Branch`, Account Function `Depreciation Expense`, Status `Active`, Used By `2`, Last Used in Journal `—`.
- Kondisi:
  - K1: tabel berisi DU-141-1 sampai DU-141-3, semuanya Active

## Test Steps

### Deactivate akun yang dipakai satu Asset Class diblokir
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Klik Switch Status pada baris `5-6002`
3. Verifikasi dialog berjudul `Cannot Deactivate Account` tampil
4. Verifikasi kalimat `This account is used by 1 Asset Class and cannot be deactivated.` tampil
5. Verifikasi tombol `[OK]` tampil pada dialog
6. Klik `[OK]`
7. Verifikasi dialog `Cannot Deactivate Account` tidak tampil lagi

### Deactivate akun yang dipakai dua Asset Class diblokir
8. Tampilkan Tab Chart of Accounts dengan kondisi K1
9. Klik Switch Status pada baris `5-6003`
10. Verifikasi kalimat `This account is used by 2 Asset Classes and cannot be deactivated.` tampil
11. Klik `[OK]`

### Bulk Deactivate yang seluruh akunnya diblokir
12. Tampilkan Tab Chart of Accounts dengan kondisi K1
13. Centang baris `5-6002`
14. Centang baris `5-6003`
15. Klik `Bulk Action`
16. Klik `Deactivate`
17. Verifikasi dialog berjudul `Cannot Deactivate Accounts` tampil
18. Verifikasi akun yang diblokir diberi anotasi `(still in use)`
19. Verifikasi kalimat `These accounts are in use and cannot be deactivated.` tampil
20. Klik `[OK]`

### Bulk Deactivate campuran meminta konfirmasi
21. Tampilkan Tab Chart of Accounts dengan kondisi K1
22. Centang baris `5-6001`
23. Centang baris `5-6002`
24. Klik `Bulk Action`
25. Klik `Deactivate`
26. Verifikasi dialog berjudul `Deactivate Accounts` tampil
27. Verifikasi kalimat `The following will be deactivated:` tampil
28. Verifikasi kalimat `The following are still in use and will be skipped:` tampil
29. Verifikasi akun yang dilewati diberi anotasi `(still in use)`
30. Verifikasi kalimat `Are you sure you want to continue?` tampil
31. Verifikasi tombol `[Cancel]` tampil pada dialog
32. Verifikasi tombol `[Continue]` tampil pada dialog
33. Klik `[Cancel]`

### Delete akun yang dipakai satu Asset Class diblokir
34. Tampilkan Tab Chart of Accounts dengan kondisi K1
35. Klik `⋯` pada baris `5-6002`
36. Klik `Delete`
37. Verifikasi dialog berjudul `Cannot Delete Account` tampil
38. Verifikasi kalimat `This account is used by 1 Asset Class and cannot be deleted.` tampil
39. Verifikasi tombol `[OK]` tampil pada dialog
40. Klik `[OK]`

### Delete akun yang dipakai dua Asset Class diblokir
41. Tampilkan Tab Chart of Accounts dengan kondisi K1
42. Klik `⋯` pada baris `5-6003`
43. Klik `Delete`
44. Verifikasi kalimat `This account is used by 2 Asset Classes and cannot be deleted.` tampil
45. Klik `[OK]`

### Bulk Delete campuran meminta konfirmasi
46. Tampilkan Tab Chart of Accounts dengan kondisi K1
47. Centang baris `5-6001`
48. Centang baris `5-6002`
49. Klik `Bulk Action`
50. Klik `Delete`
51. Verifikasi dialog berjudul `Delete Accounts` tampil
52. Verifikasi kalimat `The following will be deleted:` tampil
53. Verifikasi kalimat `The following will be skipped:` tampil
54. Verifikasi akun yang dilewati karena dipakai Asset Class diberi anotasi `(still in use)`
55. Verifikasi kalimat `Are you sure you want to continue?` tampil
56. Verifikasi tombol `[Cancel]` tampil pada dialog
57. Verifikasi tombol `[Continue]` tampil pada dialog
58. Klik `[Cancel]`

### Bulk Delete yang seluruh akunnya diblokir
59. Tampilkan Tab Chart of Accounts dengan kondisi K1
60. Centang baris `5-6002`
61. Centang baris `5-6003`
62. Klik `Bulk Action`
63. Klik `Delete`
64. Verifikasi dialog berjudul `Cannot Delete Accounts` tampil
65. Verifikasi kalimat `The following are in use and cannot be deleted:` tampil
66. Verifikasi tombol `[OK]` tampil pada dialog
67. Klik `[OK]`
