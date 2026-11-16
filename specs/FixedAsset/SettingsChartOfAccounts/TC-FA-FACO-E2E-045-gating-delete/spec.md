---
id: TC-FA-FACO-E2E-045-gating-delete
title: "Manage accounting huruf Delete hanya menambah aksi Delete"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r3", "§2.1#r8", "§[F-FACO-05] Delete Account#p1", "EB-AKS-5@delete-account", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12"]
smoke: []
dependsOn: []
trace:
  "§2.1#r3": [11, 33]
  "§2.1#r8": [33, 37, 44, 46]
  "§[F-FACO-05] Delete Account#p1": 33
  "EB-AKS-5@delete-account": [31, 33, 37, 42, 44, 46]
  "§4.8#r1": 2
  "§4.8#r2": [6, 7, 8, 9]
  "§4.8#r3": 10
  "§4.8#r5": 11
  "§4.8#r6": [12, 14]
  "§4.8#r7": [15, 18]
  "§4.8#r8": 21
  "§4.8#r9": 20
  "§4.8#r10": 24
  "§4.8#r11": 27
  "§4.8#r12": 26
anchor: [5, 36, 45]
coverage:
  web: automated
---

# Manage accounting huruf Delete hanya menambah aksi Delete

## Prerequisites
- Aktor: User `Agus Salim {runId}` (Manage accounting huruf Read dan Delete).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-045-1: User `Agus Salim {runId}` dengan Global Role Manage accounting huruf Read dan Delete (Read baseline terkunci), scope seluruh client.
  - DU-045-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-045-3: akun Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-045-5: akun Account Code `6-3101-{runId}`, Account Name `Repairs & Maintenance Expense {runId}`, Account Function `Capitalization Offset`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-045-6: akun Account Code `6-3102-{runId}`, Account Name `Disposal Proceeds Clearing {runId}`, Account Function `Disposal Proceeds`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-045-7: akun Account Code `4-7201-{runId}`, Account Name `Loss on Disposal – Vehicles {runId}`, Account Function `Loss on Disposal`, Status Active, Used By `0`, belum pernah diekspor.

## Test Steps

### Tab dan alat baca tampil
1. Buka halaman Settings > Accounting
2. Verifikasi tab `Chart of Accounts` tampil pada tab bar halaman Accounting
3. Klik tab `Chart of Accounts`
4. Ketik Search `{runId}`, tekan Enter
5. Verifikasi baris dengan Account Code `5-6001-{runId}` tampil di tabel
6. Verifikasi kontrol `Search` tampil di toolbar
7. Verifikasi kontrol `Filter` tampil di toolbar
8. Verifikasi kontrol `Download` tampil di toolbar
9. Verifikasi kontrol `Changelog` tampil di toolbar
10. Verifikasi ikon `⋯` pada header kolom Actions tampil

### Huruf Delete menambah kolom Checkbox, bulk Delete, dan row action Delete
11. Verifikasi tombol `+ Account` tidak dirender di toolbar
12. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Disabled
13. Arahkan kursor ke Switch Status pada baris Account Code `5-6001-{runId}`
14. Verifikasi alasan `You don't have permission to edit.` tersampaikan pada Switch Status yang Disabled
15. Verifikasi kolom Checkbox tampil di tabel
16. Centang baris Account Code `5-6001-{runId}`
17. Centang baris Account Code `4-7001-{runId}`
18. Verifikasi Bulk Action Bar tampil dengan counter `2 Accounts selected`
19. Klik `Bulk Action`
20. Verifikasi aksi bulk `Delete` tampil
21. Verifikasi aksi bulk `Activate` dan `Deactivate` tidak ada pada daftar aksi
22. Tekan Esc untuk menutup daftar aksi bulk
23. Klik ikon `×` pada Bulk Action Bar
24. Verifikasi ikon `⋯` tampil pada baris Account Code `5-6001-{runId}`
25. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
26. Verifikasi row action `Delete` tampil
27. Verifikasi row action `Edit` tidak dirender
28. Tekan Esc untuk menutup menu aksi baris

### Delete single dijalankan sampai sukses
29. Klik ikon `⋯` pada baris Account Code `6-3101-{runId}`
30. Klik `Delete`
31. Verifikasi dialog `Delete Account` tampil dengan teks `This action cannot be undone. Are you sure you want to delete it?`
32. Klik `[Delete]`
33. Verifikasi toast `Success, account has been deleted.` tampil
34. Muat ulang halaman
35. Ketik Search `{runId}`, tekan Enter
36. Verifikasi baris Account Code `5-6001-{runId}` tampil
37. Verifikasi baris Account Code `6-3101-{runId}` tidak ada di tabel

### Bulk Delete dijalankan sampai sukses
38. Centang baris Account Code `6-3102-{runId}`
39. Centang baris Account Code `4-7201-{runId}`
40. Klik `Bulk Action`
41. Klik `Delete`
42. Verifikasi dialog `Delete Accounts` tampil dengan teks `This action cannot be undone. Are you sure you want to delete them?`
43. Klik `[Delete]`
44. Verifikasi toast `Success, account has been deleted.` tampil
45. Verifikasi baris Account Code `4-7001-{runId}` tampil
46. Verifikasi baris Account Code `6-3102-{runId}` dan `4-7201-{runId}` tidak ada di tabel
