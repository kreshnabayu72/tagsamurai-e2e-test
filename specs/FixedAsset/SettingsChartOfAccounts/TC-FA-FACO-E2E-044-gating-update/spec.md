---
id: TC-FA-FACO-E2E-044-gating-update
title: "Manage accounting huruf Update menjalankan Edit, Activate, dan Deactivate"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r3", "§2.1#r7", "§[F-FACO-02] Edit Account#p1", "§[F-FACO-04] Deactivate Account#p1", "EB-AKS-5@edit-account", "EB-AKS-5@activate-account", "EB-AKS-5@deactivate-account", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12"]
smoke: []
dependsOn: []
trace:
  "§2.1#r3": 31
  "§2.1#r7": [31, 34, 38, 43, 51, 59]
  "§[F-FACO-02] Edit Account#p1": 31
  "§[F-FACO-04] Deactivate Account#p1": [41, 43, 57]
  "EB-AKS-5@edit-account": [31, 34]
  "EB-AKS-5@activate-account": [36, 38, 39, 49, 51, 52]
  "EB-AKS-5@deactivate-account": [41, 43, 44, 57, 59, 60]
  "§4.8#r1": 2
  "§4.8#r2": [6, 7, 8, 9]
  "§4.8#r3": 10
  "§4.8#r5": 11
  "§4.8#r6": 12
  "§4.8#r7": [13, 16]
  "§4.8#r8": 18
  "§4.8#r9": 19
  "§4.8#r10": 22
  "§4.8#r11": 24
  "§4.8#r12": 25
anchor: [5]
coverage:
  web: automated
---

# Manage accounting huruf Update menjalankan Edit, Activate, dan Deactivate

## Prerequisites
- Aktor: User `Dewi Anggraini {runId}` (Manage accounting huruf Read dan Update).
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-044-1: User `Dewi Anggraini {runId}` dengan Global Role Manage accounting huruf Read dan Update (Read baseline terkunci), scope seluruh client.
  - DU-044-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-044-3: akun Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-044-5: akun Account Code `4-7101-{runId}`, Account Name `Loss on Disposal {runId}`, Account Function `Loss on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-044-6: akun Account Code `5-6101-{runId}`, Account Name `Depreciation Expense – Warehouse {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-044-7: akun Account Code `2-1101-{runId}`, Account Name `Accumulated Depreciation – Vehicles {runId}`, Account Function `Accumulated Depreciation`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-044-8: akun Account Code `2-1102-{runId}`, Account Name `Accumulated Depreciation – Office {runId}`, Account Function `Accumulated Depreciation`, Status Inactive, Used By `0`, belum pernah diekspor.

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

### Huruf Update menambah Switch Status, bulk Activate dan Deactivate, serta Edit
11. Verifikasi tombol `+ Account` tidak dirender di toolbar
12. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Enabled
13. Verifikasi kolom Checkbox tampil di tabel
14. Centang baris Account Code `5-6001-{runId}`
15. Centang baris Account Code `4-7001-{runId}`
16. Verifikasi Bulk Action Bar tampil dengan counter `2 Accounts selected`
17. Klik `Bulk Action`
18. Verifikasi aksi bulk `Activate` dan `Deactivate` tampil
19. Verifikasi aksi bulk `Delete` tidak ada pada daftar aksi
20. Tekan Esc untuk menutup daftar aksi bulk
21. Klik ikon `×` pada Bulk Action Bar
22. Verifikasi ikon `⋯` tampil pada baris Account Code `5-6001-{runId}`
23. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
24. Verifikasi row action `Edit` tampil
25. Verifikasi row action `Delete` tidak dirender
26. Tekan Esc untuk menutup menu aksi baris

### Edit Account dijalankan sampai sukses
27. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
28. Klik `Edit`
29. Ganti Account Name dengan `Depreciation Expense – Admin Revisi {runId}`
30. Klik `[Save]`
31. Verifikasi toast `Success, account has been updated.` tampil
32. Muat ulang halaman
33. Ketik Search `{runId}`, tekan Enter
34. Verifikasi baris Account Code `5-6001-{runId}` memuat Account Name `Depreciation Expense – Admin Revisi {runId}`

### Activate single dijalankan sampai sukses
35. Klik Switch Status pada baris Account Code `4-7101-{runId}`
36. Verifikasi dialog `Activate Account` tampil dengan teks `Are you sure you want to activate it?`
37. Klik `[Activate]`
38. Verifikasi toast `Success, account has been activated.` tampil
39. Verifikasi Switch Status pada baris Account Code `4-7101-{runId}` Active

### Deactivate single dijalankan sampai sukses
40. Klik Switch Status pada baris Account Code `5-6101-{runId}`
41. Verifikasi dialog `Deactivate Account` tampil dengan teks `Are you sure you want to deactivate it?`
42. Klik `[Deactivate]`
43. Verifikasi toast `Success, account has been deactivated.` tampil
44. Verifikasi Switch Status pada baris Account Code `5-6101-{runId}` Inactive

### Bulk Activate dijalankan sampai sukses
45. Centang baris Account Code `2-1101-{runId}`
46. Centang baris Account Code `2-1102-{runId}`
47. Klik `Bulk Action`
48. Klik `Activate`
49. Verifikasi dialog `Activate Accounts` tampil dengan teks `Are you sure you want to activate them?`
50. Klik `[Activate]`
51. Verifikasi toast `Success, account has been activated.` tampil
52. Verifikasi Switch Status pada baris Account Code `2-1101-{runId}` dan `2-1102-{runId}` Active

### Bulk Deactivate dijalankan sampai sukses
53. Centang baris Account Code `2-1101-{runId}`
54. Centang baris Account Code `2-1102-{runId}`
55. Klik `Bulk Action`
56. Klik `Deactivate`
57. Verifikasi dialog `Deactivate Accounts` tampil dengan teks `Are you sure you want to deactivate them?`
58. Klik `[Deactivate]`
59. Verifikasi toast `Success, account has been deactivated.` tampil
60. Verifikasi Switch Status pada baris Account Code `2-1101-{runId}` dan `2-1102-{runId}` Inactive
