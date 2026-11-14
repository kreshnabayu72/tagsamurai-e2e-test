---
id: TC-FA-FACO-E2E-040-gating-total-control
title: "Total Control melihat dan menjalankan seluruh aksi Chart of Accounts"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§2.1#r1", "§2.2#r1", "§2.2#r2", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [31, 35, 39]
  "§2.2#r1": 31
  "§2.2#r2": [42, 45, 48, 50, 53]
  "§4.8#r1": 2
  "§4.8#r2": [5, 6, 7, 8]
  "§4.8#r3": 9
  "§4.8#r4": [10, 12]
  "§4.8#r5": 14
  "§4.8#r6": 15
  "§4.8#r7": [16, 19]
  "§4.8#r8": 22
  "§4.8#r9": 21
  "§4.8#r10": 25
  "§4.8#r11": 27
  "§4.8#r12": 28
anchor: []
coverage:
  web: automated
---

# Total Control melihat dan menjalankan seluruh aksi Chart of Accounts

## Prerequisites
- Aktor: User `Bagus Prasetyo {runId}` (Default User, Total Control permanen).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-040-1: User `Bagus Prasetyo {runId}` dengan access level Default User (Total Control permanen), scope seluruh client.
  - DU-040-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-040-3: akun Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-040-4: akun Account Code `1-1001-{runId}`, Account Name `Fixed Assets – Equipment {runId}`, Account Function `Asset Cost`, Status Active, Used By `3`, belum pernah diekspor.

## Test Steps

### Menu dan alat baca tampil
1. Buka halaman Settings > Accounting
2. Verifikasi tab `Chart of Accounts` tampil pada tab bar halaman Accounting
3. Klik tab `Chart of Accounts`
4. Ketik Search `{runId}`, tekan Enter
5. Verifikasi kontrol `Search` tampil di toolbar
6. Verifikasi kontrol `Filter` tampil di toolbar
7. Verifikasi kontrol `Download` tampil di toolbar
8. Verifikasi kontrol `Changelog` tampil di toolbar
9. Verifikasi ikon `⋯` pada header kolom Actions tampil

### Link Used By membuka popup
10. Verifikasi angka Used By `3` pada baris Account Code `1-1001-{runId}` dapat diklik
11. Klik angka Used By `3` pada baris Account Code `1-1001-{runId}`
12. Verifikasi popup `Used By` tampil
13. Klik ikon close pada popup `Used By`

### Seluruh elemen tulis tampil dan dapat dipakai
14. Verifikasi tombol `+ Account` tampil di toolbar
15. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Enabled
16. Verifikasi kolom Checkbox tampil di tabel
17. Centang baris Account Code `5-6001-{runId}`
18. Centang baris Account Code `4-7001-{runId}`
19. Verifikasi Bulk Action Bar tampil dengan counter `2 Accounts selected`
20. Klik `Bulk Action`
21. Verifikasi aksi bulk `Delete` tampil
22. Verifikasi aksi bulk `Activate` dan `Deactivate` tampil
23. Tekan Esc untuk menutup daftar aksi bulk
24. Klik ikon `×` pada Bulk Action Bar
25. Verifikasi ikon `⋯` tampil pada baris Account Code `5-6001-{runId}`
26. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
27. Verifikasi row action `Edit` tampil
28. Verifikasi row action `Delete` tampil
29. Tekan Esc untuk menutup menu aksi baris

### Aksi tulis dapat dijalankan dan guard bisnis tetap berlaku
30. Klik `+ Account`
31. Verifikasi modal `Add Account` terbuka
32. Klik `[✕]` pada modal; form belum diubah sehingga dialog Unsaved Changes tidak muncul
33. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
34. Klik `Edit`
35. Verifikasi modal `Edit Account` terbuka
36. Klik `[✕]` pada modal; form belum diubah sehingga dialog Unsaved Changes tidak muncul
37. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
38. Klik `Delete`
39. Verifikasi dialog `Delete Account` tampil dengan teks `This action cannot be undone. Are you sure you want to delete it?`
40. Klik `[Cancel]`
41. Klik Switch Status pada baris Account Code `5-6001-{runId}`
42. Verifikasi dialog `Deactivate Account` tampil dengan teks `Are you sure you want to deactivate it?`
43. Klik `[Cancel]`
44. Klik Switch Status pada baris Account Code `4-7001-{runId}`
45. Verifikasi dialog `Activate Account` tampil dengan teks `Are you sure you want to activate it?`
46. Klik `[Cancel]`
47. Klik Switch Status pada baris Account Code `1-1001-{runId}`
48. Verifikasi dialog `Cannot Deactivate Account` tampil dengan teks `This account is used by 3 Asset Classes and cannot be deactivated.`
49. Klik `[OK]`
50. Verifikasi Switch Status pada baris Account Code `1-1001-{runId}` tetap Active
51. Klik ikon `⋯` pada baris Account Code `1-1001-{runId}`
52. Klik `Delete`
53. Verifikasi dialog `Cannot Delete Account` tampil dengan teks `This account is used by 3 Asset Classes and cannot be deleted.`
54. Klik `[OK]`
