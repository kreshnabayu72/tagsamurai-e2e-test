---
id: TC-FA-FATR-E2E-005-guard-assignee
title: "Guard Allowed assignee menolak Save dan Add override"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules:
  - "§4.1#r117"
  - "§6#r23"
  - "AU-BAGIAN-asampaiAU-BAGIAN-o,AU-NILAI-asampaiAU-NILAI-j,AU-TOOLTIP-asampaiAU-TOOLTIP-d"
  - "§9.2#b32"
  - "§9.2#b33"
  - "§9.4.2#r65"
  - "§9.4.2#r67"
  - "§9.4.2#r71"
  - "§9.9#r12"
  - "§9.9#r17"
  - "§4.1#r113"
  - "§4.1#r115"
  - "§4.1#r116"
  - "§4.1#r119"
  - "§9.2#b106"
  - "§9.4.2#r66"
  - "EB-ERR-4"
smoke:
  - "§4.1#r113"
  - "§4.1#r115"
  - "§4.1#r116"
  - "§4.1#r119"
  - "§9.2#b106"
  - "§9.4.2#r66"
  - "EB-ERR-4"
dependsOn: []
trace:
  "§4.1#r117": 18
  "§6#r23": 18
  "AU-BAGIAN-asampaiAU-BAGIAN-o,AU-NILAI-asampaiAU-NILAI-j,AU-TOOLTIP-asampaiAU-TOOLTIP-d": [18, 38]
  "§9.2#b32": 18
  "§9.2#b33": 17
  "§9.4.2#r65": 9
  "§9.4.2#r67": [18, 19]
  "§9.4.2#r71": [35, 64]
  "§9.9#r12": 18
  "§9.9#r17": 35
  "§4.1#r113": 9
  "§4.1#r115": 9
  "§4.1#r116": [18, 24]
  "§4.1#r119": 35
  "§9.2#b106": [35, 52]
  "§9.4.2#r66": 18
  "EB-ERR-4": 24
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
18. Verifikasi pesan `At least one assignee type must be enabled` tampil pada baris override Target `Gudang Utara {runId}` di tabel Overrides
19. Verifikasi kontrol `Allowed assignee: Employee` dan `Allowed assignee: Division` tidak dirender
20. Muat ulang halaman dan setujui konfirmasi bawaan browser untuk meninggalkan halaman
21. Ketik Search Sidebar Category Tree `Crane {runId}`, tekan Enter
22. Klik Category leaf `Crane {runId}`
23. Klik tab `Assign`
24. Verifikasi field `Allow Assign` menampilkan teks `Inherit — Allow (from Company default)`

### Submit Add override dengan kombinasi OFF/OFF ditolak lalu dievaluasi ulang
25. Klik `[+ Override]`
26. Pilih `Group` pada `Scope`
27. Klik `[Select Group]`
28. Ketik Search pada dialog Select Group `Gudang Selatan {runId}`, tekan Enter
29. Centang `Gudang Selatan {runId}`
30. Klik `[Select]`
31. Pilih `Allowed assignee: Employee` pada Field baris pertama
32. Klik `+ Add field`
33. Pilih `Allowed assignee: Division` pada Field baris kedua
34. Klik `[Submit]`
35. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol Value baris `Allowed assignee: Employee` dan baris `Allowed assignee: Division`
36. Klik switch Value baris `Allowed assignee: Division` sehingga bernilai `ON`
37. Klik `[Submit]`
38. Verifikasi baris override Target `Gudang Selatan {runId}` tampil di tabel Overrides

### Submit Add override pada aset yang nilai efektif Allow Assign-nya Deny tidak dievaluasi
39. Klik `[+ Override]`
40. Pilih `Group` pada `Scope`
41. Klik `[Select Group]`
42. Ketik Search pada dialog Select Group `Gudang Barat {runId}`, tekan Enter
43. Centang `Gudang Barat {runId}`
44. Klik `[Select]`
45. Pilih `Allow Assign` pada Field baris pertama
46. Pilih `Deny` pada Value baris `Allow Assign`
47. Klik `+ Add field`
48. Pilih `Allowed assignee: Employee` pada Field baris kedua
49. Klik `+ Add field`
50. Pilih `Allowed assignee: Division` pada Field baris ketiga
51. Klik `[Submit]`
52. Verifikasi baris override Target `Gudang Barat {runId}` tampil di tabel Overrides

### Submit Add override Allow di bawah Category Deny ditolak
53. Ganti isi kotak search Sidebar Category Tree dengan `Tower Light {runId}`, tekan Enter
54. Klik Category leaf `Tower Light {runId}`
55. Klik `[+ Override]`
56. Pilih `Group` pada `Scope`
57. Klik `[Select Group]`
58. Ketik Search pada dialog Select Group `Gudang Timur {runId}`, tekan Enter
59. Centang `Gudang Timur {runId}`
60. Klik `[Select]`
61. Pilih `Allow Assign` pada Field baris pertama
62. Pilih `Allow` pada Value baris `Allow Assign`
63. Klik `[Submit]`
64. Verifikasi pesan `At least one assignee type must be enabled` tampil di bawah kontrol Value baris `Allow Assign`
