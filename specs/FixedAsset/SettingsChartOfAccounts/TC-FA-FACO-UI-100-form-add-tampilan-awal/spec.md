---
id: TC-FA-FACO-UI-100-form-add-tampilan-awal
title: "Form Add Account: tampilan awal, opsi Account Function, dan popover penjelasan"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [FACO-LOGIC-01a, FACO-LOGIC-07d, §4.1.2#r1, §4.1.2#r2, §4.1.2#r3, §4.1.2#p2, §4.2b#p1, §4.2b#p3, §4.2b#r4, §4.2b#r5, §4.2b#r6, §4.2b#r7, §4.2b#r8, §4.2b#r9, §4.2b#r10, §4.5#b4, §9.5#r6, §9.5#r10, EB-FRM-7@form-add-account]
smoke: []
dependsOn: []
trace:
  FACO-LOGIC-01a: 38
  FACO-LOGIC-07d: 19
  §4.1.2#r1: [9, 10]
  §4.1.2#r2: 12
  §4.1.2#r3: [14, 15, 43]
  §4.1.2#p2: [16, 17, 18]
  §4.2b#p1: [3, 4, 5, 6, 7, 18]
  §4.2b#p3: [47, 55, 57, 58]
  §4.2b#r4: 48
  §4.2b#r5: 49
  §4.2b#r6: 50
  §4.2b#r7: 51
  §4.2b#r8: 52
  §4.2b#r9: 53
  §4.2b#r10: 54
  §4.5#b4: [23, 24, 25]
  §9.5#r6: [8, 11, 13]
  §9.5#r10: [38, 39, 41]
  EB-FRM-7@form-add-account: [22, 23, 24, 25, 26, 27, 29, 30, 32, 34]
anchor: []
coverage:
  web: automated
---

# Form Add Account: tampilan awal, opsi Account Function, dan popover penjelasan

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Modal Add Account.
- Data:
  - DU-100-1: opsi Account Function `Asset Cost`, `Accumulated Depreciation`, `Depreciation Expense`, `Gain on Disposal`, `Loss on Disposal`, `Capitalization Offset`, `Disposal Proceeds`.
- Kondisi:
  - K1: form Add Account baru dibuka dari toolbar, belum ada isian, dan Account Function memuat opsi DU-100-1.

## Test Steps

### Tampilan awal form Add Account dari toolbar
1. Tampilkan Modal Add Account dengan kondisi K1
2. Klik `[+ Account]`
3. Verifikasi judul `Add Account` tampil pada modal
4. Verifikasi tombol `✕` tampil pada header modal
5. Verifikasi label `Account Code` bertanda wajib
6. Verifikasi label `Account Name` bertanda wajib
7. Verifikasi label `Account Function` bertanda wajib
8. Verifikasi field `Account Code` kosong
9. Verifikasi placeholder `Enter account code` tampil pada field `Account Code`
10. Verifikasi teks bantuan `Letters, numbers, hyphens, underscores, and dots only (e.g. 1-1001)` tampil untuk field `Account Code`
11. Verifikasi field `Account Name` kosong
12. Verifikasi placeholder `Enter account name` tampil pada field `Account Name`
13. Verifikasi field `Account Function` belum terpilih
14. Verifikasi placeholder `Select account function` tampil pada field `Account Function`
15. Verifikasi label `Account Function` memiliki ikon `[ℹ]`
16. Verifikasi tombol `[Clear Field]` tampil
17. Verifikasi tombol `[Submit]` tampil
18. Verifikasi checkbox `Stay on this form after submitting` tampil
19. Verifikasi form tidak memiliki input `Last Used in Journal`

### Aksesibilitas field dan fokus modal
20. Tampilkan Modal Add Account dengan kondisi K1
21. Klik `[+ Account]`
22. Verifikasi fokus berada di dalam modal Add Account
23. Verifikasi field `Account Code` memiliki `aria-required`
24. Verifikasi field `Account Name` memiliki `aria-required`
25. Verifikasi field `Account Function` memiliki `aria-required`
26. Verifikasi ikon `[ℹ]` memiliki label aksesibel
27. Verifikasi tombol `✕` memiliki label aksesibel `Close dialog`
28. Klik `[Submit]` pada form yang belum diisi
29. Verifikasi field `Account Name` memiliki `aria-describedby` yang menunjuk caption error `Account name must not be empty`
30. Verifikasi field `Account Function` memiliki `aria-describedby` yang menunjuk caption error `Account function must not be empty`
31. Tekan Tab berulang kali sampai elemen interaktif terakhir di modal terlewati
32. Verifikasi fokus tetap berada di dalam modal Add Account
33. Klik `✕` pada form yang belum diubah
34. Verifikasi fokus kembali ke tombol `[+ Account]`

### Opsi Account Function
35. Tampilkan Modal Add Account dengan kondisi K1
36. Klik `[+ Account]`
37. Klik field `Account Function`
38. Verifikasi dropdown `Account Function` memuat tepat tujuh opsi: `Asset Cost`, `Accumulated Depreciation`, `Depreciation Expense`, `Gain on Disposal`, `Loss on Disposal`, `Capitalization Offset`, `Disposal Proceeds`
39. Verifikasi dropdown `Account Function` tidak memuat opsi kosong
40. Arahkan kursor ke opsi `Asset Cost`
41. Verifikasi tidak ada tooltip yang tampil untuk opsi `Asset Cost`
42. Klik opsi `Asset Cost`
43. Verifikasi field `Account Function` menampilkan `Asset Cost` sebagai nilai terpilih

### Popover penjelasan Account Function
44. Tampilkan Modal Add Account dengan kondisi K1
45. Klik `[+ Account]`
46. Klik ikon `[ℹ]` pada label `Account Function`
47. Verifikasi popover penjelasan Account Function terbuka
48. Verifikasi popover memuat penjelasan `Where the asset's acquisition cost is recorded on the balance sheet.` untuk `Asset Cost`
49. Verifikasi popover memuat penjelasan `Reduces the asset's value on the balance sheet; increases every month.` untuk `Accumulated Depreciation`
50. Verifikasi popover memuat penjelasan `Monthly depreciation expense on the income statement.` untuk `Depreciation Expense`
51. Verifikasi popover memuat penjelasan `Gain when an asset is sold above its book value.` untuk `Gain on Disposal`
52. Verifikasi popover memuat penjelasan `Loss on disposal, write-off, lost assets, and the value of replaced components.` untuk `Loss on Disposal`
53. Verifikasi popover memuat penjelasan `The account where the cost is currently recorded, before FAMS moves it to the asset.` untuk `Capitalization Offset`
54. Verifikasi popover memuat penjelasan `Clearing account for the proceeds of assets that are sold, scrapped, or traded in.` untuk `Disposal Proceeds`
55. Verifikasi field `Account Function` tetap belum terpilih sesudah ikon `[ℹ]` diklik
56. Tekan `Esc`
57. Verifikasi popover penjelasan Account Function tertutup
58. Verifikasi modal Add Account tetap terbuka
