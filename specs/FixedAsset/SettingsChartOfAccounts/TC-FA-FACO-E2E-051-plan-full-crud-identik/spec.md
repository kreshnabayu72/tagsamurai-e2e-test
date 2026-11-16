---
id: TC-FA-FACO-E2E-051-plan-full-crud-identik
title: "Create, Edit, dan Delete akun identik di plan Growth, Professional, dan Enterprise"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.10#r2", "§9.10#r3", "§9.10#r4", "EB-AKS-8"]
smoke: []
dependsOn: []
trace:
  "§9.10#r2": [9, 11, 16, 17, 21, 22]
  "§9.10#r3": [31, 33, 38, 39, 43, 44]
  "§9.10#r4": [53, 55, 60, 61, 65, 66]
  "EB-AKS-8": [9, 11, 16, 17, 21, 22, 31, 33, 38, 39, 43, 44, 53, 55, 60, 61, 65, 66]
anchor: []
coverage:
  web: automated
---

# Create, Edit, dan Delete akun identik di plan Growth, Professional, dan Enterprise

## Prerequisites
- Aktor: Default User (Total Control permanen) pada tiap entitas khusus, satu per tier plan, yang tidak dipakai spec lain.
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-051-1: Entitas `Client Growth {runId}` dengan plan Growth, level fitur Chart of Accounts `Full`.
  - DU-051-2: Entitas `Client Professional {runId}` dengan plan Professional, level fitur Chart of Accounts `Full`.
  - DU-051-3: Entitas `Client Enterprise {runId}` dengan plan Enterprise, level fitur Chart of Accounts `Full`.

## Test Steps

### Create, Edit, dan Delete akun di plan Growth
1. Masuk sebagai Default User entitas `Client Growth {runId}`
2. Buka halaman Settings > Accounting
3. Klik tab `Chart of Accounts`
4. Klik `+ Account`
5. Isi Account Code `7-3001-{runId}`
6. Isi Account Name `Machinery Cost {runId}`
7. Pilih Account Function `Asset Cost`
8. Klik `[Submit]`
9. Verifikasi toast `Success, account has been created.` tampil
10. Ketik Search `7-3001-{runId}`, tekan Enter
11. Verifikasi baris Account Code `7-3001-{runId}` tampil dengan Account Name `Machinery Cost {runId}`
12. Klik ikon `⋯` pada baris Account Code `7-3001-{runId}`
13. Klik `Edit`
14. Ganti Account Name dengan `Machinery Cost Revisi {runId}`
15. Klik `[Save]`
16. Verifikasi toast `Success, account has been updated.` tampil
17. Verifikasi baris Account Code `7-3001-{runId}` memuat Account Name `Machinery Cost Revisi {runId}`
18. Klik ikon `⋯` pada baris Account Code `7-3001-{runId}`
19. Klik `Delete`
20. Klik `[Delete]` pada dialog `Delete Account`
21. Verifikasi toast `Success, account has been deleted.` tampil
22. Verifikasi empty state `No results found` tampil karena akun `7-3001-{runId}` sudah dihapus

### Create, Edit, dan Delete akun di plan Professional
23. Masuk sebagai Default User entitas `Client Professional {runId}`
24. Buka halaman Settings > Accounting
25. Klik tab `Chart of Accounts`
26. Klik `+ Account`
27. Isi Account Code `7-3002-{runId}`
28. Isi Account Name `Furniture Cost {runId}`
29. Pilih Account Function `Asset Cost`
30. Klik `[Submit]`
31. Verifikasi toast `Success, account has been created.` tampil
32. Ketik Search `7-3002-{runId}`, tekan Enter
33. Verifikasi baris Account Code `7-3002-{runId}` tampil dengan Account Name `Furniture Cost {runId}`
34. Klik ikon `⋯` pada baris Account Code `7-3002-{runId}`
35. Klik `Edit`
36. Ganti Account Name dengan `Furniture Cost Revisi {runId}`
37. Klik `[Save]`
38. Verifikasi toast `Success, account has been updated.` tampil
39. Verifikasi baris Account Code `7-3002-{runId}` memuat Account Name `Furniture Cost Revisi {runId}`
40. Klik ikon `⋯` pada baris Account Code `7-3002-{runId}`
41. Klik `Delete`
42. Klik `[Delete]` pada dialog `Delete Account`
43. Verifikasi toast `Success, account has been deleted.` tampil
44. Verifikasi empty state `No results found` tampil karena akun `7-3002-{runId}` sudah dihapus

### Create, Edit, dan Delete akun di plan Enterprise
45. Masuk sebagai Default User entitas `Client Enterprise {runId}`
46. Buka halaman Settings > Accounting
47. Klik tab `Chart of Accounts`
48. Klik `+ Account`
49. Isi Account Code `7-3003-{runId}`
50. Isi Account Name `Vehicle Cost {runId}`
51. Pilih Account Function `Asset Cost`
52. Klik `[Submit]`
53. Verifikasi toast `Success, account has been created.` tampil
54. Ketik Search `7-3003-{runId}`, tekan Enter
55. Verifikasi baris Account Code `7-3003-{runId}` tampil dengan Account Name `Vehicle Cost {runId}`
56. Klik ikon `⋯` pada baris Account Code `7-3003-{runId}`
57. Klik `Edit`
58. Ganti Account Name dengan `Vehicle Cost Revisi {runId}`
59. Klik `[Save]`
60. Verifikasi toast `Success, account has been updated.` tampil
61. Verifikasi baris Account Code `7-3003-{runId}` memuat Account Name `Vehicle Cost Revisi {runId}`
62. Klik ikon `⋯` pada baris Account Code `7-3003-{runId}`
63. Klik `Delete`
64. Klik `[Delete]` pada dialog `Delete Account`
65. Verifikasi toast `Success, account has been deleted.` tampil
66. Verifikasi empty state `No results found` tampil karena akun `7-3003-{runId}` sudah dihapus
