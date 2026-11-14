---
id: TC-FA-FACO-E2E-045-gating-delete
title: "Manage accounting huruf Delete hanya menambah aksi Delete"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§2.1#r3", "§2.1#r8", "§[F-FACO-05] Delete Account#p1", "EB-AKS-5@delete-account", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12"]
smoke: []
dependsOn: []
trace:
  "§2.1#r3": [15, 37]
  "§2.1#r8": [37, 41, 48, 50]
  "§[F-FACO-05] Delete Account#p1": 37
  "EB-AKS-5@delete-account": [35, 37, 41, 46, 48, 50]
  "§4.8#r1": 2
  "§4.8#r2": [6, 7, 8, 9]
  "§4.8#r3": 10
  "§4.8#r4": [11, 13]
  "§4.8#r5": 15
  "§4.8#r6": [16, 18]
  "§4.8#r7": [19, 22]
  "§4.8#r8": 25
  "§4.8#r9": 24
  "§4.8#r10": 28
  "§4.8#r11": 31
  "§4.8#r12": 30
anchor: [5, 40, 49]
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
  - DU-045-4: akun Account Code `1-1001-{runId}`, Account Name `Fixed Assets – Equipment {runId}`, Account Function `Asset Cost`, Status Active, Used By `3`, belum pernah diekspor.
  - DU-045-5: akun Account Code `6-3101-{runId}`, Account Name `Repairs & Maintenance Expense {runId}`, Account Function `Capitalization Offset`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-045-6: akun Account Code `6-3102-{runId}`, Account Name `Disposal Proceeds Clearing {runId}`, Account Function `Disposal Proceeds`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-045-7: akun Account Code `4-7201-{runId}`, Account Name `Loss on Disposal – Vehicles {runId}`, Account Function `Loss on Disposal`, Status Active, Used By `0`, belum pernah diekspor.

## Test Steps

### Menu dan alat baca tampil
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

### Link Used By membuka popup
11. Verifikasi angka Used By `3` pada baris Account Code `1-1001-{runId}` dapat diklik
12. Klik angka Used By `3` pada baris Account Code `1-1001-{runId}`
13. Verifikasi popup `Used By` tampil
14. Klik ikon close pada popup `Used By`

### Huruf Delete menambah kolom Checkbox, bulk Delete, dan row action Delete
15. Verifikasi tombol `+ Account` tidak dirender di toolbar
16. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Disabled
17. Arahkan kursor ke Switch Status pada baris Account Code `5-6001-{runId}`
18. Verifikasi alasan `You don't have permission to edit.` tersampaikan pada Switch Status yang Disabled
19. Verifikasi kolom Checkbox tampil di tabel
20. Centang baris Account Code `5-6001-{runId}`
21. Centang baris Account Code `4-7001-{runId}`
22. Verifikasi Bulk Action Bar tampil dengan counter `2 Accounts selected`
23. Klik `Bulk Action`
24. Verifikasi aksi bulk `Delete` tampil
25. Verifikasi aksi bulk `Activate` dan `Deactivate` tidak ada pada daftar aksi
26. Tekan Esc untuk menutup daftar aksi bulk
27. Klik ikon `×` pada Bulk Action Bar
28. Verifikasi ikon `⋯` tampil pada baris Account Code `5-6001-{runId}`
29. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
30. Verifikasi row action `Delete` tampil
31. Verifikasi row action `Edit` tidak dirender
32. Tekan Esc untuk menutup menu aksi baris

### Delete single dijalankan sampai sukses
33. Klik ikon `⋯` pada baris Account Code `6-3101-{runId}`
34. Klik `Delete`
35. Verifikasi dialog `Delete Account` tampil dengan teks `This action cannot be undone. Are you sure you want to delete it?`
36. Klik `[Delete]`
37. Verifikasi toast `Success, account has been deleted.` tampil
38. Muat ulang halaman
39. Ketik Search `{runId}`, tekan Enter
40. Verifikasi baris Account Code `5-6001-{runId}` tampil
41. Verifikasi baris Account Code `6-3101-{runId}` tidak ada di tabel

### Bulk Delete dijalankan sampai sukses
42. Centang baris Account Code `6-3102-{runId}`
43. Centang baris Account Code `4-7201-{runId}`
44. Klik `Bulk Action`
45. Klik `Delete`
46. Verifikasi dialog `Delete Accounts` tampil dengan teks `This action cannot be undone. Are you sure you want to delete them?`
47. Klik `[Delete]`
48. Verifikasi toast `Success, account has been deleted.` tampil
49. Verifikasi baris Account Code `1-1001-{runId}` tampil
50. Verifikasi baris Account Code `6-3102-{runId}` dan `4-7201-{runId}` tidak ada di tabel
