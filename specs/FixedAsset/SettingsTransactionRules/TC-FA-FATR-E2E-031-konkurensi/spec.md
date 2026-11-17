---
id: TC-FA-FATR-E2E-031-konkurensi
title: "Dua aktor mengubah Settings dan override yang sama"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.2#b66", "§9.4.2#r32", "§9.4.2#r96", "§9.4.2#r97", "§9.4.2#r98", "§9.4.4#r17", "§9.4.4#r32", "§9.2#b39", "§9.2#b65", "§9.2#b180", "§9.6#r19", "EB-CON-2"]
smoke: ["§9.2#b39", "§9.2#b65", "§9.2#b180", "§9.6#r19", "EB-CON-2"]
dependsOn: []
trace:
  "§9.2#b66": 26
  "§9.4.2#r32": [46, 47]
  "§9.4.2#r96": 30
  "§9.4.2#r97": 26
  "§9.4.2#r98": [33, 34]
  "§9.4.4#r17": [33, 34]
  "§9.4.4#r32": 47
  "§9.2#b39": [14, 15]
  "§9.2#b65": 30
  "§9.2#b180": 47
  "§9.6#r19": 30
  "EB-CON-2": [63, 69]
anchor: [25, 41]
coverage:
  web: automated
---

# Dua aktor mengubah Settings dan override yang sama

## Prerequisites
- Aktor: Aktor A dan Aktor B, keduanya Total Control, masing-masing dengan sesinya sendiri.
- Layar awal: Settings > Transaction Settings, untuk Aktor A dan Aktor B.
- Data:
  - DU-031-1: Category leaf `Laptop {runId}` dengan Max extensions bernilai sendiri `1` dan Max assets per borrower (concurrent) bernilai sendiri `3` pada tab Borrow.
  - DU-031-2: Group `Proyek Karawang {runId}`, ada di entitas aktor.
  - DU-031-3: Group `Workshop {runId}`, ada di entitas aktor.
  - DU-031-4: Group `Proyek Bekasi {runId}`, ada di entitas aktor.
  - DU-031-5: override Scope `Group`, Target `Proyek Karawang {runId}`, Overridden `Max extensions (2)`, Category `Laptop {runId}`, transaksi `Borrow`.
  - DU-031-6: override Scope `Group`, Target `Proyek Bekasi {runId}`, Overridden `Max extensions (1)`, Category `Laptop {runId}`, transaksi `Borrow`.

## Test Steps

### Dua Save pada field berbeda tidak saling menimpa
1. Aktor A: pilih Category `Laptop {runId}` pada Sidebar Category Tree
2. Aktor A: klik tab `Borrow`
3. Aktor B: pilih Category `Laptop {runId}` pada Sidebar Category Tree
4. Aktor B: klik tab `Borrow`
5. Aktor A: ubah Max extensions menjadi `2`
6. Aktor B: ubah Max assets per borrower (concurrent) menjadi `5`
7. Aktor A: klik `[Save]`
8. Aktor A: klik `[Save]` pada dialog Save Changes
9. Aktor B: klik `[Save]`
10. Aktor B: klik `[Save]` pada dialog Save Changes
11. Aktor A: muat ulang halaman
12. Aktor A: pilih Category `Laptop {runId}` pada Sidebar Category Tree
13. Aktor A: klik tab `Borrow`
14. Verifikasi Max extensions pada layar Aktor A menampilkan `2`
15. Verifikasi Max assets per borrower (concurrent) pada layar Aktor A menampilkan `5`

### Dua Save pada field yang sama: Save terakhir menimpa tanpa dialog konflik
16. Aktor B: muat ulang halaman
17. Aktor B: pilih Category `Laptop {runId}` pada Sidebar Category Tree
18. Aktor B: klik tab `Borrow`
19. Aktor A: ubah Max extensions menjadi `3`
20. Aktor B: ubah Max extensions menjadi `4`
21. Aktor A: klik `[Save]`
22. Aktor A: klik `[Save]` pada dialog Save Changes
23. Aktor B: klik `[Save]`
24. Aktor B: klik `[Save]` pada dialog Save Changes
25. Verifikasi toast `Success, settings have been saved.` tampil pada layar Aktor B
26. Verifikasi layar Aktor B tidak menampilkan dialog konflik
27. Aktor A: muat ulang halaman
28. Aktor A: pilih Category `Laptop {runId}` pada Sidebar Category Tree
29. Aktor A: klik tab `Borrow`
30. Verifikasi Max extensions pada layar Aktor A menampilkan `4`

### Tiap Save tercatat sendiri di Changelog
31. Aktor A: klik ikon Changelog di header
32. Aktor A: ketik Search `{runId}`, tekan Enter
33. Verifikasi entri Category `Laptop {runId}`, Field `Borrow (Max extensions)`, Old Value `2`, New Value `3` tampil
34. Verifikasi entri Category `Laptop {runId}`, Field `Borrow (Max extensions)`, Old Value `3`, New Value `4` tampil
35. Tekan `Esc` untuk menutup dialog Changelog

### Override yang sudah dihapus aktor lain dihapus lagi
36. Aktor B: klik `⋯` pada baris `Proyek Karawang {runId}`
37. Aktor B: klik `Delete`
38. Aktor A: klik `⋯` pada baris `Proyek Karawang {runId}`
39. Aktor A: klik `Delete`
40. Aktor A: klik `[Delete]` pada dialog Delete Override
41. Verifikasi toast `Success, override has been deleted.` tampil pada layar Aktor A
42. Aktor B: klik `[Delete]` pada dialog Delete Override
43. Aktor B: muat ulang halaman
44. Aktor B: pilih Category `Laptop {runId}` pada Sidebar Category Tree
45. Aktor B: klik tab `Borrow`
46. Verifikasi baris `Proyek Bekasi {runId}` tetap tampil di tabel Overrides pada layar Aktor B
47. Verifikasi baris `Proyek Karawang {runId}` tidak tampil di tabel Overrides pada layar Aktor B

### Dua aktor menambah override dengan target, Category, dan transaksi yang sama
48. Aktor A: klik `[+ Override]`
49. Aktor A: pilih Scope `Group`
50. Aktor A: klik `[Select Group]`
51. Aktor A: centang `Workshop {runId}` pada dialog Select Group
52. Aktor A: klik `[Select]`
53. Aktor A: pilih Field `Max extensions`
54. Aktor A: isi Value `2`
55. Aktor B: klik `[+ Override]`
56. Aktor B: pilih Scope `Group`
57. Aktor B: klik `[Select Group]`
58. Aktor B: centang `Workshop {runId}` pada dialog Select Group
59. Aktor B: klik `[Select]`
60. Aktor B: pilih Field `Max extensions`
61. Aktor B: isi Value `2`
62. Aktor A dan Aktor B klik `[Submit]` pada dialog masing-masing secara bersamaan
63. Verifikasi tepat satu dari kedua dialog Add override tertutup, dan dialog yang lain tetap terbuka dengan pesan `An active override already exists for this target, category, and transaction. Delete it first` di bawah Target
64. Klik `✕` pada dialog Add override yang masih terbuka, lalu klik `[Leave]` pada dialog Unsaved Changes
65. Aktor A: muat ulang halaman
66. Aktor A: pilih Category `Laptop {runId}` pada Sidebar Category Tree
67. Aktor A: klik tab `Borrow`
68. Aktor A: ketik Search `Workshop {runId}`, tekan Enter
69. Verifikasi tabel Overrides memuat tepat satu baris `Workshop {runId}`
