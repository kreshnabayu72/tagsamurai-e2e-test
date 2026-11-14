---
id: TC-FA-FACO-UI-110-form-edit-tampilan-awal-dan-kunci
title: "Form Edit Account: tampilan awal dan field terkunci"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [ST-10, §4.1.1#b4, §4.1.2#r1, §4.1.2#r3, §4.1.2#p2, §4.2b#p1, §4.2b#r1, §4.2b#r2, §4.5#b5, §7.2#b1, EB-FRM-7@form-edit-account, EB-TBL-5@field-terkunci-edit]
smoke: []
dependsOn: []
trace:
  ST-10: [17, 18, 33]
  §4.1.1#b4: [21, 24]
  §4.1.2#r1: [8, 17, 32]
  §4.1.2#r3: [9, 18, 33]
  §4.1.2#p2: [10, 11, 12]
  §4.2b#p1: [4, 5, 6, 7, 13, 55, 56, 58, 59]
  §4.2b#r1: 20
  §4.2b#r2: 23
  §4.5#b5: 26
  §7.2#b1: 28
  EB-FRM-7@form-edit-account: [37, 38, 39, 40, 41, 42, 44, 46, 52]
  EB-TBL-5@field-terkunci-edit: [17, 18, 20, 23]
anchor: []
coverage:
  web: automated
---

# Form Edit Account: tampilan awal dan field terkunci

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Modal Edit Account.
- Data:
  - DU-110-1: akun dengan Account Code `1-1001`, Account Name `Fixed Assets – Equipment`, Account Function `Asset Cost`, Used By `3`, Last Used in Journal `Oct 2026`.
  - DU-110-2: akun dengan Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`.
  - DU-110-3: akun dengan Account Code `5-6002`, Account Name `Depreciation Expense – Warehouse`, Account Function `Depreciation Expense`, Used By `1`, Last Used in Journal `—`.
- Kondisi:
  - K1: form Edit Account dibuka untuk akun DU-110-1, yang Last Used in Journal-nya terisi.
  - K2: form Edit Account dibuka untuk akun DU-110-2, yang Last Used in Journal-nya kosong dan Used By bernilai `0`.
  - K3: form Edit Account dibuka untuk akun DU-110-3, yang Last Used in Journal-nya kosong dan Used By bernilai `1`.

## Test Steps

### Tampilan awal form Edit untuk akun yang belum terkunci
1. Tampilkan Modal Edit Account dengan kondisi K2
2. Klik `⋯` pada baris akun `5-6001`
3. Klik `Edit`
4. Verifikasi judul `Edit Account` tampil pada modal
5. Verifikasi field `Account Code` berisi `5-6001`
6. Verifikasi field `Account Name` berisi `Depreciation Expense – Admin`
7. Verifikasi field `Account Function` menampilkan `Depreciation Expense`
8. Verifikasi field `Account Code` dapat diubah karena Last Used in Journal kosong
9. Verifikasi field `Account Function` dapat diubah karena Last Used in Journal kosong dan Used By bernilai `0`
10. Verifikasi tombol `[Clear Field]` tampil pada modal Edit Account
11. Verifikasi tombol `[Save]` tampil pada modal Edit Account
12. Verifikasi tombol `[Submit]` tidak tampil pada modal Edit Account
13. Verifikasi checkbox `Stay on this form after submitting` tidak tampil pada modal Edit Account

### Field terkunci pada akun yang pernah diekspor
14. Tampilkan Modal Edit Account dengan kondisi K1
15. Klik `⋯` pada baris akun `1-1001`
16. Klik `Edit`
17. Verifikasi field `Account Code` Disabled dengan nilai tersimpan `1-1001`
18. Verifikasi field `Account Function` Disabled dengan nilai tersimpan `Asset Cost`
19. Arahkan kursor ke field `Account Code` yang Disabled
20. Verifikasi alasan `Account Code can't be changed because this account was used in a journal in Oct 2026. Create a new account if needed.` tersampaikan pada field `Account Code` yang Disabled
21. Verifikasi periode pada alasan field `Account Code` ditulis `Oct 2026` dengan format `MMM YYYY`
22. Arahkan kursor ke field `Account Function` yang Disabled
23. Verifikasi alasan `Account Function can't be changed because this account was used in a journal in Oct 2026.` tersampaikan pada field `Account Function` yang Disabled
24. Verifikasi periode pada alasan field `Account Function` ditulis `Oct 2026` dengan format `MMM YYYY`
25. Tekan Tab dari header modal sampai fokus berpindah ke field `Account Name`
26. Verifikasi field `Account Code` yang Disabled tidak menerima fokus sehingga alasannya hanya tersampaikan lewat hover[^drift-1]
27. Klik field `Account Code` yang Disabled
28. Verifikasi tidak ada dialog blok yang tampil sesudah field `Account Code` yang Disabled diklik

### Account Function terkunci karena akun sudah dipakai
29. Tampilkan Modal Edit Account dengan kondisi K3
30. Klik `⋯` pada baris akun `5-6002`
31. Klik `Edit`
32. Verifikasi field `Account Code` dapat diubah walau Used By bernilai `1`
33. Verifikasi field `Account Function` Disabled karena Used By bernilai `1`

### Aksesibilitas form Edit
34. Tampilkan Modal Edit Account dengan kondisi K2
35. Klik `⋯` pada baris akun `5-6001`
36. Klik `Edit`
37. Verifikasi fokus berada di dalam modal Edit Account
38. Verifikasi field `Account Code` memiliki `aria-required` pada modal Edit Account
39. Verifikasi field `Account Name` memiliki `aria-required` pada modal Edit Account
40. Verifikasi field `Account Function` memiliki `aria-required` pada modal Edit Account
41. Verifikasi ikon `[ℹ]` pada label `Account Function` memiliki label aksesibel pada modal Edit Account
42. Verifikasi tombol `✕` memiliki label aksesibel `Close dialog` pada modal Edit Account
43. Tekan Tab berulang kali sampai elemen interaktif terakhir di modal Edit Account terlewati
44. Verifikasi fokus tetap berada di dalam modal Edit Account sesudah Tab melewati elemen terakhir
45. Klik `✕` pada form yang belum diubah
46. Verifikasi fokus kembali ke tombol `⋯` pada baris akun `5-6001`, pemicu menu `Edit` yang membuka modal Edit Account

### Caption error terhubung ke field pada form Edit
47. Tampilkan Modal Edit Account dengan kondisi K2
48. Klik `⋯` pada baris akun `5-6001`
49. Klik `Edit`
50. Kosongkan field `Account Name`
51. Klik `[Save]`
52. Verifikasi field `Account Name` memiliki `aria-describedby` yang menunjuk caption `Account name must not be empty` pada modal Edit Account

### Popover penjelasan Account Function pada form Edit
53. Tampilkan Modal Edit Account dengan kondisi K2
54. Klik ikon `[ℹ]` pada label `Account Function`
55. Verifikasi popover penjelasan Account Function terbuka pada modal Edit Account
56. Verifikasi field `Account Function` tetap menampilkan `Depreciation Expense` sesudah ikon `[ℹ]` diklik
57. Tekan `Esc`
58. Verifikasi popover penjelasan Account Function pada modal Edit Account tertutup sesudah `Esc`
59. Verifikasi modal Edit Account tetap terbuka

[^drift-1]: Drift PRD vs kontrak komponen. PRD §4.5: «Tooltip 🔖 dapat diakses lewat keyboard focus.» Kontrak `Tooltip#38`: «A disabled control cannot be focused, so its tooltip opens on hover only.» Diasersi: kontrak, karena field `Account Code` yang Disabled tidak bisa menerima fokus keyboard (SB-7).
