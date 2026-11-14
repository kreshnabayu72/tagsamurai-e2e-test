---
id: TC-FA-FACO-E2E-069-konsumen-opsi-akun-dep-asset-class
title: "Create, Edit, Activate, Deactivate, dan Delete akun tercermin di opsi akun Asset Class"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FACO-LOGIC-01b, S-12, S-14, "§9.7#p4", "§9.7#r16", "§9.7#r18", "§9.7#r21", "§9.7#r23", "§9.7#r26", "EB-XM-2@asset-class"]
smoke: []
dependsOn: ["Asset Class: opsi akun pada form Asset Class"]
trace:
  FACO-LOGIC-01b: [20, 22]
  S-12: [49, 50, 52, 55, 58, 62]
  S-14: [18, 38, 41, 44]
  "§9.7#p4": [18, 19, 72, 73]
  "§9.7#r16": 18
  "§9.7#r18": 24
  "§9.7#r21": 38
  "§9.7#r23": 41
  "§9.7#r26": 44
  "EB-XM-2@asset-class": [18, 24, 44]
anchor: [40, 43]
coverage:
  web: automated
---

# Create, Edit, Activate, Deactivate, dan Delete akun tercermin di opsi akun Asset Class

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-069-1: Account Code `KSA-{runId}`, Account Name `Mesin Produksi {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-069-8).
  - DU-069-2: Account Code `KSD-{runId}`, Account Name `Mesin Cadangan {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-069-3: Account Code `KSE-{runId}`, Account Name `Mesin Utama Beban {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-069-4: Account Code `KSF-{runId}`, Account Name `Akumulasi Lama {runId}`, Account Function `Accumulated Depreciation`, Status Inactive, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-069-5: Account Code `KSG-{runId}`, Account Name `Rugi Pelepasan Aset {runId}`, Account Function `Loss on Disposal`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class, bukan nilai default company.
  - DU-069-6: Account Code `KSL-{runId}`, Account Name `Rugi Pelepasan Cadangan {runId}`, Account Function `Loss on Disposal`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-069-7: Account Code `KSH-{runId}`, Account Name `Laba Lama {runId}`, Account Function `Gain on Disposal`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-069-8), bukan nilai default company.
  - DU-069-8: Asset Class `Konsumen Utama {runId}` dengan Asset Cost `KSA-{runId}` dan Gain on Disposal `KSH-{runId}`.
  - Akun yang dibuat spec ini: Account Code `KSC-{runId}`, Account Name `Laba Pelepasan Aset {runId}`, Account Function `Gain on Disposal` (DU-069-9).
  - Account Code `KSC-{runId}` diubah menjadi `KSI-{runId}` (DU-069-10), dan Account Name `Mesin Produksi {runId}` pada DU-069-1 diubah menjadi `Mesin Produksi Baru {runId}` (DU-069-11).
  - Account Code `KSA-{runId}` pada DU-069-1 diubah menjadi `KSJ-{runId}` (DU-069-12), selagi akun itu dipakai Asset Class `Konsumen Utama {runId}` dan belum pernah diekspor.

## Test Steps

### Create dan Edit akun tercermin di opsi akun Asset Class
1. Klik `[+ Account]`
2. Isi Account Code `KSC-{runId}`
3. Isi Account Name `Laba Pelepasan Aset {runId}`
4. Pilih Account Function `Gain on Disposal`
5. Klik `[Submit]`
6. Ketik Search `{runId}`, tekan Enter
7. Klik `⋯` pada baris `KSC-{runId}`
8. Klik `Edit`
9. Ganti isi Account Code menjadi `KSI-{runId}`
10. Klik `[Save]`
11. Klik `⋯` pada baris `KSA-{runId}`
12. Klik `Edit`
13. Ganti isi Account Name menjadi `Mesin Produksi Baru {runId}`
14. Klik `[Save]`
15. Buka tab Asset Class
16. Buka form Asset Class `Konsumen Utama {runId}`
17. Buka Select akun Gain on Disposal
18. Verifikasi opsi dengan Account Code `KSI-{runId}` tampil
19. Verifikasi opsi dengan Account Code `KSC-{runId}` tidak tampil
20. Verifikasi opsi dengan Account Code `KSL-{runId}` yang ber-function Loss on Disposal tampil pada field Gain on Disposal
21. Buka Select akun Loss on Disposal
22. Verifikasi opsi dengan Account Code `KSI-{runId}` yang ber-function Gain on Disposal tampil pada field Loss on Disposal
23. Buka Select akun Asset Cost
24. Verifikasi opsi akun memuat Account Name `Mesin Produksi Baru {runId}`
25. Tutup form Asset Class, form belum diubah

### Activate, Deactivate, dan Delete akun tercermin di opsi akun Asset Class
26. Buka tab Chart of Accounts
27. Ketik Search `{runId}`, tekan Enter
28. Klik switch Status baris `KSF-{runId}`
29. Klik `[Activate]` pada dialog
30. Klik switch Status baris `KSD-{runId}`
31. Klik `[Deactivate]` pada dialog
32. Klik `⋯` pada baris `KSG-{runId}`
33. Klik `Delete`
34. Klik `[Delete]` pada dialog
35. Buka tab Asset Class
36. Buka form Asset Class `Konsumen Utama {runId}`
37. Buka Select akun Accumulated Depreciation
38. Verifikasi opsi dengan Account Code `KSF-{runId}` tampil
39. Buka Select akun Depreciation Expense
40. Verifikasi opsi dengan Account Code `KSE-{runId}` tampil
41. Verifikasi opsi dengan Account Code `KSD-{runId}` tidak tampil
42. Buka Select akun Loss on Disposal
43. Verifikasi opsi dengan Account Code `KSL-{runId}` tampil
44. Verifikasi opsi dengan Account Code `KSG-{runId}` tidak tampil
45. Tutup form Asset Class, form belum diubah

### Asset Class memakai dan melepas akun menghitung ulang Used By dan guard Deactivate
46. Asset Class `Konsumen Utama {runId}` mengganti akun Gain on Disposal dari `KSH-{runId}` menjadi `KSI-{runId}`
47. Buka tab Chart of Accounts
48. Ketik Search `{runId}`, tekan Enter
49. Verifikasi Used By baris `KSI-{runId}` bernilai `1`
50. Verifikasi Used By baris `KSH-{runId}` bernilai `0`
51. Klik switch Status baris `KSI-{runId}`
52. Verifikasi dialog `Cannot Deactivate Account` tampil
53. Klik `[OK]`
54. Klik angka Used By `1` pada baris `KSI-{runId}`
55. Verifikasi popup `Used By` memuat Asset Class `Konsumen Utama {runId}`
56. Klik `✕` pada popup Used By

### Guard Deactivate dan Delete terbuka kembali sesudah akun dilepas
57. Klik switch Status baris `KSH-{runId}`
58. Verifikasi dialog `Deactivate Account` tampil, bukan `Cannot Deactivate Account`
59. Klik `[Cancel]`
60. Klik `⋯` pada baris `KSH-{runId}`
61. Klik `Delete`
62. Verifikasi dialog `Delete Account` tampil, bukan `Cannot Delete Account`
63. Klik `[Cancel]`

### Edit Account Code akun yang dipakai Asset Class tercermin pada akun terpilih
64. Ketik Search `{runId}`, tekan Enter
65. Klik `⋯` pada baris `KSA-{runId}`
66. Klik `Edit`
67. Ganti isi Account Code menjadi `KSJ-{runId}`
68. Klik `[Save]`
69. Buka tab Asset Class
70. Buka form Asset Class `Konsumen Utama {runId}`
71. Buka Select akun Asset Cost
72. Verifikasi akun terpilih pada field Asset Cost menampilkan Account Code `KSJ-{runId}`
73. Verifikasi opsi dengan Account Code `KSJ-{runId}` tampil
74. Tutup form Asset Class, form belum diubah
