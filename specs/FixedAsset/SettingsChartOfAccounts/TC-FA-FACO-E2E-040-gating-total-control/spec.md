---
id: TC-FA-FACO-E2E-040-gating-total-control
title: "Total Control melihat dan menjalankan seluruh aksi Chart of Accounts"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.2#r1", "§2.2#r2", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [27, 31, 35]
  "§2.2#r1": 27
  "§2.2#r2": [38, 41]
  "§4.8#r1": 2
  "§4.8#r2": [5, 6, 7, 8]
  "§4.8#r3": 9
  "§4.8#r5": 10
  "§4.8#r6": 11
  "§4.8#r7": [12, 15]
  "§4.8#r8": 18
  "§4.8#r9": 17
  "§4.8#r10": 21
  "§4.8#r11": 23
  "§4.8#r12": 24
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

## Test Steps

### Tab dan alat baca tampil
1. Buka halaman Settings > Accounting
2. Verifikasi tab `Chart of Accounts` tampil pada tab bar halaman Accounting
3. Klik tab `Chart of Accounts`
4. Ketik Search `{runId}`, tekan Enter
5. Verifikasi kontrol `Search` tampil di toolbar
6. Verifikasi kontrol `Filter` tampil di toolbar
7. Verifikasi kontrol `Download` tampil di toolbar
8. Verifikasi kontrol `Changelog` tampil di toolbar
9. Verifikasi ikon `⋯` pada header kolom Actions tampil

### Seluruh elemen tulis tampil dan dapat dipakai
10. Verifikasi tombol `+ Account` tampil di toolbar
11. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Enabled
12. Verifikasi kolom Checkbox tampil di tabel
13. Centang baris Account Code `5-6001-{runId}`
14. Centang baris Account Code `4-7001-{runId}`
15. Verifikasi Bulk Action Bar tampil dengan counter `2 Accounts selected`
16. Klik `Bulk Action`
17. Verifikasi aksi bulk `Delete` tampil
18. Verifikasi aksi bulk `Activate` dan `Deactivate` tampil
19. Tekan Esc untuk menutup daftar aksi bulk
20. Klik ikon `×` pada Bulk Action Bar
21. Verifikasi ikon `⋯` tampil pada baris Account Code `5-6001-{runId}`
22. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
23. Verifikasi row action `Edit` tampil
24. Verifikasi row action `Delete` tampil
25. Tekan Esc untuk menutup menu aksi baris

### Aksi tulis dapat dijalankan
26. Klik `+ Account`
27. Verifikasi modal `Add Account` terbuka
28. Klik `[✕]` pada modal; form belum diubah sehingga dialog Unsaved Changes tidak muncul
29. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
30. Klik `Edit`
31. Verifikasi modal `Edit Account` terbuka
32. Klik `[✕]` pada modal; form belum diubah sehingga dialog Unsaved Changes tidak muncul
33. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
34. Klik `Delete`
35. Verifikasi dialog `Delete Account` tampil dengan teks `This action cannot be undone. Are you sure you want to delete it?`
36. Klik `[Cancel]`
37. Klik Switch Status pada baris Account Code `5-6001-{runId}`
38. Verifikasi dialog `Deactivate Account` tampil dengan teks `Are you sure you want to deactivate it?`
39. Klik `[Cancel]`
40. Klik Switch Status pada baris Account Code `4-7001-{runId}`
41. Verifikasi dialog `Activate Account` tampil dengan teks `Are you sure you want to activate it?`
42. Klik `[Cancel]`
