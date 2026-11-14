---
id: TC-FA-FACO-E2E-048-entitas-suspended-expired
title: "Aksi tulis Chart of Accounts ditolak saat entitas Suspended atau Expired"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["T-11", "§[F-FACO-01] Create Account#p1", "§[F-FACO-02] Edit Account#p1", "§9.4.2#r28", "EB-AKS-7"]
smoke: []
dependsOn: []
trace:
  "T-11": [20, 30, 43, 53]
  "§[F-FACO-01] Create Account#p1": [20, 43]
  "§[F-FACO-02] Edit Account#p1": [30, 53]
  "§9.4.2#r28": [20, 23, 30, 32, 43, 46, 53, 55]
  "EB-AKS-7": [20, 30, 43, 53]
anchor: [9, 14, 37]
coverage:
  web: automated
---

# Aksi tulis Chart of Accounts ditolak saat entitas Suspended atau Expired

## Prerequisites
- Aktor: Default User (Total Control permanen) pada tiap entitas; spec ini memakai tiga entitas khusus yang tidak dipakai spec lain.
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-048-1: Entitas `Client Aktif {runId}` berstatus Active.
  - DU-048-2: Entitas `Client Suspended {runId}` berstatus Suspended.
  - DU-048-3: Entitas `Client Expired {runId}` berstatus Expired.
  - DU-048-4: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor, pada entitas `Client Suspended {runId}`.
  - DU-048-5: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor, pada entitas `Client Expired {runId}`.

## Test Steps

### Pembanding di entitas Active: Create Account berhasil
1. Masuk sebagai Default User entitas `Client Aktif {runId}`
2. Buka halaman Settings > Accounting
3. Klik tab `Chart of Accounts`
4. Klik `+ Account`
5. Isi Account Code `7-2001-{runId}`
6. Isi Account Name `Office Equipment Cost {runId}`
7. Pilih Account Function `Asset Cost`
8. Klik `[Submit]`
9. Verifikasi toast `Success, account has been created.` tampil

### Aksi tulis ditolak di entitas Suspended
10. Masuk sebagai Default User entitas `Client Suspended {runId}`
11. Buka halaman Settings > Accounting
12. Klik tab `Chart of Accounts`
13. Ketik Search `{runId}`, tekan Enter
14. Verifikasi baris Account Code `5-6001-{runId}` tampil di tabel
15. Klik `+ Account`
16. Isi Account Code `8-1001-{runId}`
17. Isi Account Name `Land Improvement Cost {runId}`
18. Pilih Account Function `Asset Cost`
19. Klik `[Submit]`
20. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
21. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
22. Ganti isi kotak search dengan `8-1001-{runId}`, tekan Enter
23. Verifikasi empty state `No results found` tampil karena akun `8-1001-{runId}` tidak tercipta
24. Klik `(←)` pada kotak Search
25. Ketik Search `{runId}`, tekan Enter
26. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
27. Klik `Edit`
28. Ganti Account Name dengan `Depreciation Expense – Admin Revisi S {runId}`
29. Klik `[Save]`
30. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
31. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
32. Verifikasi baris Account Code `5-6001-{runId}` tetap memuat Account Name `Depreciation Expense – Admin {runId}`

### Aksi tulis ditolak di entitas Expired
33. Masuk sebagai Default User entitas `Client Expired {runId}`
34. Buka halaman Settings > Accounting
35. Klik tab `Chart of Accounts`
36. Ketik Search `{runId}`, tekan Enter
37. Verifikasi baris Account Code `5-6001-{runId}` tampil di tabel
38. Klik `+ Account`
39. Isi Account Code `8-1002-{runId}`
40. Isi Account Name `Building Improvement Cost {runId}`
41. Pilih Account Function `Asset Cost`
42. Klik `[Submit]`
43. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
44. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
45. Ganti isi kotak search dengan `8-1002-{runId}`, tekan Enter
46. Verifikasi empty state `No results found` tampil karena akun `8-1002-{runId}` tidak tercipta
47. Klik `(←)` pada kotak Search
48. Ketik Search `{runId}`, tekan Enter
49. Klik ikon `⋯` pada baris Account Code `5-6001-{runId}`
50. Klik `Edit`
51. Ganti Account Name dengan `Depreciation Expense – Admin Revisi E {runId}`
52. Klik `[Save]`
53. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
54. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
55. Verifikasi baris Account Code `5-6001-{runId}` tetap memuat Account Name `Depreciation Expense – Admin {runId}`
