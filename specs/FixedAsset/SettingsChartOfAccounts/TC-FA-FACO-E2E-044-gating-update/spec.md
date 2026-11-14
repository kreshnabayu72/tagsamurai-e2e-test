---
id: TC-FA-FACO-E2E-044-gating-update
title: "Manage accounting huruf Update menjalankan Edit, Activate, dan Deactivate"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§2.1#r3", "§2.1#r7", "§[F-FACO-02] Edit Account#p1", "§[F-FACO-04] Deactivate Account#p1", "EB-AKS-5@edit-account", "EB-AKS-5@activate-account", "EB-AKS-5@deactivate-account", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12"]
smoke: []
dependsOn: []
trace:
  "§2.1#r3": 35
  "§2.1#r7": [35, 38, 42, 47, 55, 63]
  "§[F-FACO-02] Edit Account#p1": 35
  "§[F-FACO-04] Deactivate Account#p1": [45, 47, 61]
  "EB-AKS-5@edit-account": [35, 38]
  "EB-AKS-5@activate-account": [40, 42, 43, 53, 55, 56]
  "EB-AKS-5@deactivate-account": [45, 47, 48, 61, 63, 64]
  "§4.8#r1": 2
  "§4.8#r2": [6, 7, 8, 9]
  "§4.8#r3": 10
  "§4.8#r4": [11, 13]
  "§4.8#r5": 15
  "§4.8#r6": 16
  "§4.8#r7": [17, 20]
  "§4.8#r8": 22
  "§4.8#r9": 23
  "§4.8#r10": 26
  "§4.8#r11": 28
  "§4.8#r12": 29
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
  - DU-044-4: akun Account Code `1-1001-{runId}`, Account Name `Fixed Assets – Equipment {runId}`, Account Function `Asset Cost`, Status Active, Used By `3`, belum pernah diekspor.
  - DU-044-5: akun Account Code `4-7101-{runId}`, Account Name `Loss on Disposal {runId}`, Account Function `Loss on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-044-6: akun Account Code `5-6101-{runId}`, Account Name `Depreciation Expense – Warehouse {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-044-7: akun Account Code `2-1101-{runId}`, Account Name `Accumulated Depreciation – Vehicles {runId}`, Account Function `Accumulated Depreciation`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-044-8: akun Account Code `2-1102-{runId}`, Account Name `Accumulated Depreciation – Office {runId}`, Account Function `Accumulated Depreciation`, Status Inactive, Used By `0`, belum pernah diekspor.

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

### Huruf Update menambah Switch Status, bulk Activate dan Deactivate, serta Edit
15. Verifikasi tombol `+ Account` tidak dirender di toolbar
16. Verifikasi Switch Status pada baris Account Code `5-6001-{runId}` Enabled
17. Verifikasi kolom Checkbox tampil di tabel
18. Centang baris Account Code `5-6001-{runId}`
19. Centang baris Account Code `4-7001-{runId}`
20. Verifikasi Bulk Action Bar tampil dengan counter `2 Accounts selected`
21. Klik `Bulk Action`
22. Verifikasi aksi bulk `Activate` dan `Deactivate` tampil
23. Verifikasi aksi bulk `Delete` tidak ada pada daftar aksi
24. Tekan Esc untuk menutup daftar aksi bulk
25. Klik ikon `×` pada Bulk Action Bar
26. Verifikasi ikon `⋯` tampil pada baris Account Code `5-6001-{runId}`
27. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
28. Verifikasi row action `Edit` tampil
29. Verifikasi row action `Delete` tidak dirender
30. Tekan Esc untuk menutup menu aksi baris

### Edit Account dijalankan sampai sukses
31. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
32. Klik `Edit`
33. Ganti Account Name dengan `Depreciation Expense – Admin Revisi {runId}`
34. Klik `[Save]`
35. Verifikasi toast `Success, account has been updated.` tampil
36. Muat ulang halaman
37. Ketik Search `{runId}`, tekan Enter
38. Verifikasi baris Account Code `5-6001-{runId}` memuat Account Name `Depreciation Expense – Admin Revisi {runId}`

### Activate single dijalankan sampai sukses
39. Klik Switch Status pada baris Account Code `4-7101-{runId}`
40. Verifikasi dialog `Activate Account` tampil dengan teks `Are you sure you want to activate it?`
41. Klik `[Activate]`
42. Verifikasi toast `Success, account has been activated.` tampil
43. Verifikasi Switch Status pada baris Account Code `4-7101-{runId}` Active

### Deactivate single dijalankan sampai sukses
44. Klik Switch Status pada baris Account Code `5-6101-{runId}`
45. Verifikasi dialog `Deactivate Account` tampil dengan teks `Are you sure you want to deactivate it?`
46. Klik `[Deactivate]`
47. Verifikasi toast `Success, account has been deactivated.` tampil
48. Verifikasi Switch Status pada baris Account Code `5-6101-{runId}` Inactive

### Bulk Activate dijalankan sampai sukses
49. Centang baris Account Code `2-1101-{runId}`
50. Centang baris Account Code `2-1102-{runId}`
51. Klik `Bulk Action`
52. Klik `Activate`
53. Verifikasi dialog `Activate Accounts` tampil dengan teks `Are you sure you want to activate them?`
54. Klik `[Activate]`
55. Verifikasi toast `Success, account has been activated.` tampil
56. Verifikasi Switch Status pada baris Account Code `2-1101-{runId}` dan `2-1102-{runId}` Active

### Bulk Deactivate dijalankan sampai sukses
57. Centang baris Account Code `2-1101-{runId}`
58. Centang baris Account Code `2-1102-{runId}`
59. Klik `Bulk Action`
60. Klik `Deactivate`
61. Verifikasi dialog `Deactivate Accounts` tampil dengan teks `Are you sure you want to deactivate them?`
62. Klik `[Deactivate]`
63. Verifikasi toast `Success, account has been deactivated.` tampil
64. Verifikasi Switch Status pada baris Account Code `2-1101-{runId}` dan `2-1102-{runId}` Inactive
