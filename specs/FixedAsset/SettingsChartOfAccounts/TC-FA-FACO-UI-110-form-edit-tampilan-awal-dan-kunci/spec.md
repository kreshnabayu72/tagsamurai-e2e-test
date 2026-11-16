---
id: TC-FA-FACO-UI-110-form-edit-tampilan-awal-dan-kunci
title: "Form Edit Account: tampilan awal dan field terkunci"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ST-10, §4.1.1#b3, §4.1.2#r1, §4.1.2#r3, §4.1.2#p2, §4.2b#p1, §4.2b#r1, §4.2b#r2, §4.5#b5, §7.2#b1, EB-FRM-7@form-edit-account, EB-TBL-5@field-terkunci-edit, FACO-LOGIC-07d]
smoke: []
dependsOn: []
trace:
  ST-10: [13, 14, 27]
  §4.1.1#b3: [17, 20]
  §4.1.2#r1: [6, 13, 26]
  §4.1.2#r3: [7, 14, 27]
  §4.1.2#p2: [8, 9, 10]
  §4.2b#p1: [2, 3, 4, 5, 11, 45, 46, 48, 49]
  §4.2b#r1: 16
  §4.2b#r2: 19
  §4.5#b5: [22, 52]
  §7.2#b1: 24
  EB-FRM-7@form-edit-account: [29, 30, 31, 32, 33, 34, 36, 38, 42]
  EB-TBL-5@field-terkunci-edit: [13, 14, 16, 19]
  FACO-LOGIC-07d: 55
anchor: [54]
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
2. Verifikasi judul `Edit Account` tampil pada modal
3. Verifikasi field `Account Code` berisi `5-6001`
4. Verifikasi field `Account Name` berisi `Depreciation Expense – Admin`
5. Verifikasi field `Account Function` menampilkan `Depreciation Expense`
6. Verifikasi field `Account Code` dapat diubah karena Last Used in Journal kosong
7. Verifikasi field `Account Function` dapat diubah karena Last Used in Journal kosong dan Used By bernilai `0`
8. Verifikasi tombol `[Clear Field]` tampil pada modal Edit Account
9. Verifikasi tombol `[Save]` tampil pada modal Edit Account
10. Verifikasi tombol `[Submit]` tidak tampil pada modal Edit Account
11. Verifikasi checkbox `Stay on this form after submitting` tidak tampil pada modal Edit Account

### Field terkunci pada akun yang pernah diekspor
12. Tampilkan Modal Edit Account dengan kondisi K1
13. Verifikasi field `Account Code` Disabled dengan nilai tersimpan `1-1001`
14. Verifikasi field `Account Function` Disabled dengan nilai tersimpan `Asset Cost`
15. Arahkan kursor ke field `Account Code` yang Disabled
16. Verifikasi alasan `Account Code can't be changed because this account was used in a journal in Oct 2026. Create a new account if needed.` tersampaikan pada field `Account Code` yang Disabled
17. Verifikasi periode pada alasan field `Account Code` ditulis `Oct 2026` dengan format `MMM YYYY`
18. Arahkan kursor ke field `Account Function` yang Disabled
19. Verifikasi alasan `Account Function can't be changed because this account was used in a journal in Oct 2026.` tersampaikan pada field `Account Function` yang Disabled
20. Verifikasi periode pada alasan field `Account Function` ditulis `Oct 2026` dengan format `MMM YYYY`
21. Tekan Tab dari header modal sampai fokus berpindah ke field `Account Name`
22. Verifikasi field `Account Code` yang Disabled tidak menerima fokus sehingga alasannya hanya tersampaikan lewat hover
23. Klik field `Account Code` yang Disabled
24. Verifikasi tidak ada dialog blok yang tampil sesudah field `Account Code` yang Disabled diklik

### Account Function terkunci karena akun sudah dipakai
25. Tampilkan Modal Edit Account dengan kondisi K3
26. Verifikasi field `Account Code` dapat diubah walau Used By bernilai `1`
27. Verifikasi field `Account Function` Disabled karena Used By bernilai `1`

### Aksesibilitas form Edit
28. Tampilkan Modal Edit Account dengan kondisi K2
29. Verifikasi fokus berada di dalam modal Edit Account
30. Verifikasi field `Account Code` memiliki `aria-required` pada modal Edit Account
31. Verifikasi field `Account Name` memiliki `aria-required` pada modal Edit Account
32. Verifikasi field `Account Function` memiliki `aria-required` pada modal Edit Account
33. Verifikasi ikon `[ℹ]` pada label `Account Function` memiliki label aksesibel pada modal Edit Account
34. Verifikasi tombol `✕` memiliki label aksesibel `Close dialog` pada modal Edit Account
35. Tekan Tab berulang kali sampai elemen interaktif terakhir di modal Edit Account terlewati
36. Verifikasi fokus tetap berada di dalam modal Edit Account sesudah Tab melewati elemen terakhir
37. Klik `✕` pada form yang belum diubah
38. Verifikasi fokus kembali ke pemicu yang membuka modal Edit Account

### Caption error terhubung ke field pada form Edit
39. Tampilkan Modal Edit Account dengan kondisi K2
40. Kosongkan field `Account Name`
41. Klik `[Save]`
42. Verifikasi field `Account Name` memiliki `aria-describedby` yang menunjuk caption `Account name must not be empty` pada modal Edit Account

### Popover penjelasan Account Function pada form Edit
43. Tampilkan Modal Edit Account dengan kondisi K2
44. Klik ikon `[ℹ]` pada label `Account Function`
45. Verifikasi popover penjelasan Account Function terbuka pada modal Edit Account
46. Verifikasi field `Account Function` tetap menampilkan `Depreciation Expense` sesudah ikon `[ℹ]` diklik
47. Tekan `Esc`
48. Verifikasi popover penjelasan Account Function pada modal Edit Account tertutup sesudah `Esc`
49. Verifikasi modal Edit Account tetap terbuka

### Account Function yang Disabled tidak dapat difokus keyboard
50. Tampilkan Modal Edit Account dengan kondisi K1
51. Tekan Tab sampai fokus melewati field `Account Name`
52. Verifikasi field `Account Function` yang Disabled tidak menerima fokus sehingga alasannya hanya tersampaikan lewat hover

### Form Edit tidak punya input Last Used in Journal
53. Tampilkan Modal Edit Account dengan kondisi K1
54. Verifikasi field `Account Name` berisi `Fixed Assets – Equipment` pada modal Edit Account
55. Verifikasi input untuk mengisi Last Used in Journal tidak tampil pada modal Edit Account walau akun sudah punya Last Used in Journal `Oct 2026`
