---
id: TC-FA-FATR-E2E-005-guard-assignee
title: "Guard Allowed assignee menolak Save dan Add override"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules:
  - "§4.1#r127"
  - "§6#r23"
  - "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f"
  - "§9.2#b32"
  - "§9.2#b33"
  - "§9.4.2#r73"
  - "§9.4.2#r75"
  - "§9.4.2#r79"
  - "§9.9#r12"
  - "§9.9#r17"
  - "§4.4#r2"
  - "§4.1#r123"
  - "§4.1#r125"
  - "§4.1#r126"
  - "§4.1#r129"
  - "§9.2#b106"
  - "§9.4.2#r74"
  - "EB-ERR-4"
smoke:
  - "§4.1#r123"
  - "§4.1#r125"
  - "§4.1#r126"
  - "§4.1#r129"
  - "§9.2#b106"
  - "§9.4.2#r74"
  - "EB-ERR-4"
dependsOn: []
trace:
  "§4.1#r127": 19
  "§6#r23": 19
  "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f": [19, 39]
  "§9.2#b32": 19
  "§9.2#b33": 17
  "§9.4.2#r73": 9
  "§9.4.2#r75": [19, 20]
  "§9.4.2#r79": [36, 65]
  "§9.9#r12": 19
  "§9.9#r17": 36
  "§4.4#r2": 18
  "§4.1#r123": 9
  "§4.1#r125": 9
  "§4.1#r126": [19, 25]
  "§4.1#r129": 36
  "§9.2#b106": [36, 53]
  "§9.4.2#r74": 19
  "EB-ERR-4": 25
coverage:
  web: automated
---

# Guard Allowed assignee menolak Save dan Add override

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-005-1: Category leaf `Crane {runId}`, tanpa sub-Category, ada di entitas aktor. Semua field Inherit, sehingga Allow Assign, Allowed assignee: Employee, dan Allowed assignee: Division bernilai efektif `Allow`, `ON`, dan `ON`.
  - DU-005-2: Category leaf `Tower Light {runId}`, tanpa sub-Category, ada di entitas aktor. Di tab Assign: Allow Assign bernilai sendiri `Deny`, Allowed assignee: Employee bernilai sendiri `OFF`, Allowed assignee: Division bernilai sendiri `OFF`.
  - DU-005-3: Group `Gudang Utara {runId}`.
  - DU-005-4: Group `Gudang Selatan {runId}`.
  - DU-005-5: Group `Gudang Barat {runId}`.
  - DU-005-6: Group `Gudang Timur {runId}`.
  - DU-005-7: Asset Name `Mobile Crane {runId}`, Category `Crane {runId}`.
  - DU-005-8: Asset Name `Tower Light Set {runId}`, Category `Tower Light {runId}`.
  - DU-005-9: Asset `Mobile Crane {runId} - 1`, Asset Name DU-005-7, di Group `Gudang Utara {runId}`.
  - DU-005-10: Asset `Mobile Crane {runId} - 2`, Asset Name DU-005-7, di Group `Gudang Selatan {runId}`.
  - DU-005-11: Asset `Mobile Crane {runId} - 3`, Asset Name DU-005-7, di Group `Gudang Barat {runId}`.
  - DU-005-12: Asset `Tower Light Set {runId} - 1`, Asset Name DU-005-8, di Group `Gudang Timur {runId}`.
  - DU-005-13: Override aktif di Category `Crane {runId}`, transaksi Assign: Scope `Group`, Target `Gudang Utara {runId}`, field Allow Assign bernilai `Allow`.
- Kondisi:
  - Company default entitas aktor bernilai bawaan: Allow Assign `Allow`, Allowed assignee: Employee `ON`, Allowed assignee: Division `ON`.
  - Plan entitas aktor menyediakan tab Borrow dan tab Assign.

## Test Steps

### Save dengan Allowed assignee Employee dan Division sama-sama OFF ditolak
1. Ketik Search Sidebar Category Tree `Crane {runId}`, tekan Enter
2. Klik Category leaf `Crane {runId}`
3. Klik tab `Assign`
4. Klik `[Set own value]` pada field `Allowed assignee: Employee`
5. Klik switch `Allowed assignee: Employee` sehingga bernilai `OFF`
6. Klik `[Set own value]` pada field `Allowed assignee: Division`
7. Klik switch `Allowed assignee: Division` sehingga bernilai `OFF`
8. Klik `[Save]`
9. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kedua kontrol `Allowed assignee: Employee` dan `Allowed assignee: Division`

### Save ditolak karena aset yang dibuka override Allow di bawah Category Deny berkombinasi OFF/OFF
10. Klik `[Set own value]` pada field `Allow Assign`
11. Pilih `Deny` pada field `Allow Assign`
12. Kosongkan kotak Search Sidebar Category Tree, tekan Enter
13. Klik `All categories`
14. Klik tab `Borrow`
15. Klik `[Save]`
16. Klik `[Save]` pada dialog Save Changes
17. Verifikasi node `Crane {runId}` terpilih dan tab `Assign` aktif
18. Verifikasi field `Allow Assign` pada Category `Crane {runId}` masih bernilai sendiri `Deny` sebagai draft yang belum disimpan, dibuat sebelum pindah ke `All categories`
19. Verifikasi pesan `At least one assignee type must be enabled` tampil pada baris override Target `Gudang Utara {runId}` di tabel Overrides
20. Verifikasi kontrol `Allowed assignee: Employee` dan `Allowed assignee: Division` tidak dirender
21. Muat ulang halaman dan setujui konfirmasi bawaan browser untuk meninggalkan halaman
22. Ketik Search Sidebar Category Tree `Crane {runId}`, tekan Enter
23. Klik Category leaf `Crane {runId}`
24. Klik tab `Assign`
25. Verifikasi field `Allow Assign` menampilkan teks `Inherit — Allow (from Company default)`

### Submit Add override dengan kombinasi OFF/OFF ditolak lalu dievaluasi ulang
26. Klik `[+ Override]`
27. Pilih `Group` pada `Scope`
28. Klik `[Select Group]`
29. Ketik Search pada dialog Select Group `Gudang Selatan {runId}`, tekan Enter
30. Centang `Gudang Selatan {runId}`
31. Klik `[Select]`
32. Pilih `Allowed assignee: Employee` pada Field baris pertama
33. Klik `+ Add field`
34. Pilih `Allowed assignee: Division` pada Field baris kedua
35. Klik `[Submit]`
36. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol Value baris `Allowed assignee: Employee` dan baris `Allowed assignee: Division`
37. Klik switch Value baris `Allowed assignee: Division` sehingga bernilai `ON`
38. Klik `[Submit]`
39. Verifikasi baris override Target `Gudang Selatan {runId}` tampil di tabel Overrides

### Submit Add override pada aset yang nilai efektif Allow Assign-nya Deny tidak dievaluasi
40. Klik `[+ Override]`
41. Pilih `Group` pada `Scope`
42. Klik `[Select Group]`
43. Ketik Search pada dialog Select Group `Gudang Barat {runId}`, tekan Enter
44. Centang `Gudang Barat {runId}`
45. Klik `[Select]`
46. Pilih `Allow Assign` pada Field baris pertama
47. Pilih `Deny` pada Value baris `Allow Assign`
48. Klik `+ Add field`
49. Pilih `Allowed assignee: Employee` pada Field baris kedua
50. Klik `+ Add field`
51. Pilih `Allowed assignee: Division` pada Field baris ketiga
52. Klik `[Submit]`
53. Verifikasi baris override Target `Gudang Barat {runId}` tampil di tabel Overrides

### Submit Add override Allow di bawah Category Deny ditolak
54. Ganti isi kotak search Sidebar Category Tree dengan `Tower Light {runId}`, tekan Enter
55. Klik Category leaf `Tower Light {runId}`
56. Klik `[+ Override]`
57. Pilih `Group` pada `Scope`
58. Klik `[Select Group]`
59. Ketik Search pada dialog Select Group `Gudang Timur {runId}`, tekan Enter
60. Centang `Gudang Timur {runId}`
61. Klik `[Select]`
62. Pilih `Allow Assign` pada Field baris pertama
63. Pilih `Allow` pada Value baris `Allow Assign`
64. Klik `[Submit]`
65. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol Value baris `Allow Assign`
