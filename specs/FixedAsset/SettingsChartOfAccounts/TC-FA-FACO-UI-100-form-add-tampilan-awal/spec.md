---
id: TC-FA-FACO-UI-100-form-add-tampilan-awal
title: "Form Add Account: tampilan awal, opsi Account Function, dan popover penjelasan"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FACO-LOGIC-01a, FACO-LOGIC-07d, §4.1.2#r1, §4.1.2#r2, §4.1.2#r3, §4.1.2#p2, §4.2b#p1, §4.2b#p3, §4.2b#r4, §4.2b#r5, §4.2b#r6, §4.2b#r7, §4.2b#r8, §4.2b#r9, §4.2b#r10, §4.5#b4, §9.5#r6, §9.5#r10, EB-FRM-7@form-add-account]
smoke: []
dependsOn: []
trace:
  FACO-LOGIC-01a: 35
  FACO-LOGIC-07d: 18
  §4.1.2#r1: [8, 9]
  §4.1.2#r2: 11
  §4.1.2#r3: [13, 14, 40]
  §4.1.2#p2: [15, 16, 17]
  §4.2b#p1: [2, 3, 4, 5, 6, 17]
  §4.2b#p3: [43, 51, 53, 54]
  §4.2b#r4: 44
  §4.2b#r5: 45
  §4.2b#r6: 46
  §4.2b#r7: 47
  §4.2b#r8: 48
  §4.2b#r9: 49
  §4.2b#r10: 50
  §4.5#b4: [21, 22, 23]
  §9.5#r6: [7, 10, 12]
  §9.5#r10: [35, 36, 38]
  EB-FRM-7@form-add-account: [20, 21, 22, 23, 24, 25, 27, 28, 30, 32]
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
2. Verifikasi judul `Add Account` tampil pada modal
3. Verifikasi tombol `✕` tampil pada header modal
4. Verifikasi label `Account Code` bertanda wajib
5. Verifikasi label `Account Name` bertanda wajib
6. Verifikasi label `Account Function` bertanda wajib
7. Verifikasi field `Account Code` kosong
8. Verifikasi placeholder `Enter account code` tampil pada field `Account Code`
9. Verifikasi teks bantuan `Letters, numbers, hyphens, underscores, and dots only (e.g. 1-1001)` tampil untuk field `Account Code`
10. Verifikasi field `Account Name` kosong
11. Verifikasi placeholder `Enter account name` tampil pada field `Account Name`
12. Verifikasi field `Account Function` belum terpilih
13. Verifikasi placeholder `Select account function` tampil pada field `Account Function`
14. Verifikasi label `Account Function` memiliki ikon `[ℹ]`
15. Verifikasi tombol `[Clear Field]` tampil
16. Verifikasi tombol `[Submit]` tampil
17. Verifikasi checkbox `Stay on this form after submitting` tampil
18. Verifikasi form tidak memiliki input `Last Used in Journal`

### Aksesibilitas field dan fokus modal
19. Tampilkan Modal Add Account dengan kondisi K1
20. Verifikasi fokus berada di dalam modal Add Account
21. Verifikasi field `Account Code` memiliki `aria-required`
22. Verifikasi field `Account Name` memiliki `aria-required`
23. Verifikasi field `Account Function` memiliki `aria-required`
24. Verifikasi ikon `[ℹ]` memiliki label aksesibel
25. Verifikasi tombol `✕` memiliki label aksesibel `Close dialog`
26. Klik `[Submit]` pada form yang belum diisi
27. Verifikasi field `Account Name` memiliki `aria-describedby` yang menunjuk caption error `Account name must not be empty`
28. Verifikasi field `Account Function` memiliki `aria-describedby` yang menunjuk caption error `Account function must not be empty`
29. Tekan Tab berulang kali sampai elemen interaktif terakhir di modal terlewati
30. Verifikasi fokus tetap berada di dalam modal Add Account
31. Klik `✕` pada form yang belum diubah
32. Verifikasi fokus kembali ke pemicu yang membuka form Add Account

### Opsi Account Function
33. Tampilkan Modal Add Account dengan kondisi K1
34. Klik field `Account Function`
35. Verifikasi dropdown `Account Function` memuat tepat tujuh opsi: `Asset Cost`, `Accumulated Depreciation`, `Depreciation Expense`, `Gain on Disposal`, `Loss on Disposal`, `Capitalization Offset`, `Disposal Proceeds`
36. Verifikasi dropdown `Account Function` tidak memuat opsi kosong
37. Arahkan kursor ke opsi `Asset Cost`
38. Verifikasi tidak ada tooltip yang tampil untuk opsi `Asset Cost`
39. Klik opsi `Asset Cost`
40. Verifikasi field `Account Function` menampilkan `Asset Cost` sebagai nilai terpilih

### Popover penjelasan Account Function
41. Tampilkan Modal Add Account dengan kondisi K1
42. Klik ikon `[ℹ]` pada label `Account Function`
43. Verifikasi popover penjelasan Account Function terbuka
44. Verifikasi popover memuat penjelasan `Where the asset's acquisition cost is recorded on the balance sheet.` untuk `Asset Cost`
45. Verifikasi popover memuat penjelasan `Reduces the asset's value on the balance sheet; increases every month.` untuk `Accumulated Depreciation`
46. Verifikasi popover memuat penjelasan `Monthly depreciation expense on the income statement.` untuk `Depreciation Expense`
47. Verifikasi popover memuat penjelasan `Gain when an asset is sold above its book value.` untuk `Gain on Disposal`
48. Verifikasi popover memuat penjelasan `Loss on disposal, write-off, lost assets, and the value of replaced components.` untuk `Loss on Disposal`
49. Verifikasi popover memuat penjelasan `The account where the cost is currently recorded, before FAMS moves it to the asset.` untuk `Capitalization Offset`
50. Verifikasi popover memuat penjelasan `Clearing account for the proceeds of assets that are sold, scrapped, or traded in.` untuk `Disposal Proceeds`
51. Verifikasi field `Account Function` tetap belum terpilih sesudah ikon `[ℹ]` diklik
52. Tekan `Esc`
53. Verifikasi popover penjelasan Account Function tertutup
54. Verifikasi modal Add Account tetap terbuka
